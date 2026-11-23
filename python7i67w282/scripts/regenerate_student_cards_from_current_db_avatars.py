from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json
import random
import sys


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "api" / "templates" / "front"
DEFAULT_INPUT = Path("/private/tmp/current_yonghu_list.json")

FONT_CANDIDATES = [
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
]


def font(size):
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size, index=0)
    return ImageFont.load_default()


def fit_inside(img, size, fill="#f8dcc8"):
    target_w, target_h = size
    src_w, src_h = img.size
    scale = min(target_w / src_w, target_h / src_h)
    resized = img.resize((int(src_w * scale), int(src_h * scale)), Image.LANCZOS)
    canvas = Image.new("RGB", size, fill)
    left = (target_w - resized.width) // 2
    top = (target_h - resized.height) // 2
    canvas.paste(resized, (left, top))
    return canvas


def add_noise(img, seed, amount=4):
    random.seed(seed)
    pixels = img.load()
    w, h = img.size
    for _ in range(w * h // 70):
        x = random.randrange(w)
        y = random.randrange(h)
        delta = random.randint(-amount, amount)
        r, g, b = pixels[x, y]
        pixels[x, y] = tuple(max(0, min(255, value + delta)) for value in (r, g, b))
    return img


def local_upload_path(value):
    if not value:
        return None
    if value.startswith("upload/"):
        return ASSET_DIR / value.replace("upload/", "", 1)
    return ASSET_DIR / value


def draw_card(user):
    user_id = int(user["id"])
    avatar_path = local_upload_path(user.get("touxiang"))
    if not avatar_path or not avatar_path.exists():
        raise FileNotFoundError(f"avatar not found for user {user_id}: {user.get('touxiang')}")

    w, h = 1720, 1080
    image = Image.new("RGB", (w, h), "#f8dcc8")
    draw = ImageDraw.Draw(image)

    for y in range(h):
        r = 251 - int(y * 20 / h)
        g = 224 - int(y * 38 / h)
        b = 207 - int(y * 45 / h)
        draw.line((0, y, w, y), fill=(r, g, b))

    draw.rounded_rectangle((20, 20, w - 20, h - 20), radius=42, outline="#d19b78", width=4)
    draw.ellipse((96, 94, 256, 254), fill="#0878bd", outline="#e8f8ff", width=8)
    draw.text((126, 122), "AI", fill="white", font=font(64))
    draw.text((112, 205), "DEMO", fill="#d8efff", font=font(22))
    draw.text((305, 116), "校园物品流转平台", fill="#1269a8", font=font(60))
    draw.text((308, 188), "Campus Circulation Platform", fill="#668da6", font=font(30))
    draw.text((764, 126), "测试学生身份卡", fill="#4a5568", font=font(31))
    draw.text((764, 176), "DEMO STUDENT PROFILE CARD", fill="#4a5568", font=font(30))

    avatar = Image.open(avatar_path).convert("RGB")
    photo = fit_inside(avatar, (430, 520), fill="#f8dcc8").filter(ImageFilter.SMOOTH_MORE)
    image.paste(photo, (140, 366))

    rows = [
        ("姓名 / Name", user.get("xingming") or user.get("nicheng") or "测试用户"),
        ("性别 / Gender", user.get("xingbie") or "未填写"),
        ("测试编号 / Demo No.", f"DEMO{20230000 + user_id:08d}"),
        ("身份 / Role", user.get("shenfen") or "学生"),
        ("账号 / Account", user.get("zhanghao") or ""),
    ]
    y = 350
    for label, value in rows:
        draw.text((670, y), label, fill="#7c6b60", font=font(25))
        draw.text((670, y + 36), str(value), fill="#161616", font=font(54 if label.startswith("姓名") else 40))
        y += 128

    draw.text((1104, 398), "非官方证件", fill="#cf6740", font=font(86))
    draw.text((1107, 492), "PORTFOLIO SAMPLE", fill="#cf6740", font=font(42))
    draw.text((258, 620), "DEMO ONLY", fill="#cf7656", font=font(112))
    draw.text((725, 750), "DEMO ONLY", fill="#cf7656", font=font(112))
    draw.text((112, 982), "仅用于作品集与测试演示，不作为真实身份凭证。", fill="#95583a", font=font(30))
    draw.text((1240, 982), "DEMO ONLY / NOT AN OFFICIAL ID", fill="#95583a", font=font(28))

    image = add_noise(image, 20260525 + user_id).filter(ImageFilter.SMOOTH_MORE)
    output = ASSET_DIR / f"demo_student_card_{user_id - 10:02d}.jpg"
    image.save(output, quality=94)
    return output


def main():
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    payload = json.loads(source.read_text(encoding="utf-8"))
    users = payload["data"]["list"]
    for user in users:
        output = draw_card(user)
        print(f"{user['id']} {user.get('touxiang')} -> upload/{output.name}")


if __name__ == "__main__":
    main()
