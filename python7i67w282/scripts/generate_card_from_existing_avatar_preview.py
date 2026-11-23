from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "api" / "templates" / "front"
OUT = ROOT / "demo_outputs"

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


def cover_crop(img, size):
    target_w, target_h = size
    src_w, src_h = img.size
    scale = max(target_w / src_w, target_h / src_h)
    resized = img.resize((int(src_w * scale), int(src_h * scale)), Image.LANCZOS)
    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def add_noise(img, amount=6):
    random.seed(1225)
    px = img.load()
    w, h = img.size
    for _ in range(w * h // 50):
        x = random.randrange(w)
        y = random.randrange(h)
        delta = random.randint(-amount, amount)
        r, g, b = px[x, y]
        px[x, y] = (
            max(0, min(255, r + delta)),
            max(0, min(255, g + delta)),
            max(0, min(255, b + delta)),
        )
    return img


def make_card():
    OUT.mkdir(parents=True, exist_ok=True)
    avatar_path = ASSET_DIR / "campus_avatar_01.jpg"
    if not avatar_path.exists():
        avatar_path = ASSET_DIR / "demo_avatar_01.jpg"

    w, h = 1720, 1080
    img = Image.new("RGB", (w, h), "#f8dcc8")
    d = ImageDraw.Draw(img)

    for y in range(h):
        r = 251 - int(y * 22 / h)
        g = 224 - int(y * 42 / h)
        b = 207 - int(y * 50 / h)
        d.line((0, y, w, y), fill=(r, g, b))

    d.rounded_rectangle((18, 18, w - 18, h - 18), radius=44, outline="#d19b78", width=4)
    d.ellipse((96, 94, 256, 254), fill="#0878bd", outline="#e8f8ff", width=8)
    d.text((126, 122), "AI", fill="white", font=font(64))
    d.text((112, 205), "DEMO", fill="#d8efff", font=font(22))

    d.text((305, 116), "校园物品流转平台", fill="#1269a8", font=font(60))
    d.text((308, 188), "Campus Circulation Platform", fill="#668da6", font=font(30))
    d.text((764, 126), "测试学生身份卡", fill="#4a5568", font=font(31))
    d.text((764, 176), "DEMO STUDENT PROFILE CARD", fill="#4a5568", font=font(30))

    photo = Image.open(avatar_path).convert("RGB")
    photo = cover_crop(photo, (430, 520)).filter(ImageFilter.SMOOTH_MORE)
    d.rounded_rectangle((118, 346, 594, 928), radius=22, fill="#fff9f3", outline="#edc1a5", width=3)
    d.rounded_rectangle((139, 365, 571, 887), radius=12, fill="#ffffff")
    img.paste(photo, (140, 366))
    d.rectangle((140, 846, 570, 886), fill="#162235")
    d.text((292, 854), "头像来源：用户资料", fill="#ffffff", font=font(24))

    rows = [
        ("姓名 / Name", "李明"),
        ("性别 / Gender", "男"),
        ("测试编号 / Demo No.", "DEMO20230001"),
        ("学部 / Department", "信息学部"),
        ("方向 / Major", "AI 产品与校园服务"),
    ]
    y = 350
    for label, value in rows:
        d.text((670, y), label, fill="#7c6b60", font=font(25))
        d.text((670, y + 36), value, fill="#161616", font=font(54 if label.startswith("姓名") else 40))
        y += 128

    d.text((1104, 398), "非官方证件", fill="#cf6740", font=font(86))
    d.text((1107, 492), "PORTFOLIO SAMPLE", fill="#cf6740", font=font(42))
    d.text((252, 620), "DEMO ONLY", fill="#cf7656", font=font(112))
    d.text((725, 750), "DEMO ONLY", fill="#cf7656", font=font(112))

    d.text((112, 982), "仅用于作品集与测试演示，不作为真实身份凭证。", fill="#95583a", font=font(30))
    d.text((1240, 982), "DEMO ONLY / NOT AN OFFICIAL ID", fill="#95583a", font=font(28))

    img = add_noise(img).filter(ImageFilter.SMOOTH_MORE)
    out_path = OUT / "demo_student_card_from_avatar_sample.jpg"
    img.save(out_path, quality=94)
    print(out_path)


if __name__ == "__main__":
    make_card()
