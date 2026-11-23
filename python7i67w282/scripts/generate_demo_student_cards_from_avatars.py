from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "api" / "templates" / "front"

FONT_CANDIDATES = [
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
]


STUDENTS = [
    {"idx": 1, "name": "李明", "gender": "男", "department": "信息学部", "major": "AI 产品与校园服务"},
    {"idx": 2, "name": "王雨晴", "gender": "女", "department": "经济与管理学院", "major": "信息管理与信息系统"},
    {"idx": 3, "name": "张子涵", "gender": "女", "department": "信息学部", "major": "软件工程"},
    {"idx": 4, "name": "陈思远", "gender": "男", "department": "城市建设学部", "major": "智能建造"},
    {"idx": 5, "name": "刘佳宁", "gender": "女", "department": "艺术设计学院", "major": "数字媒体设计"},
    {"idx": 6, "name": "赵一鸣", "gender": "男", "department": "信息学部", "major": "计算机科学与技术"},
    {"idx": 7, "name": "周可欣", "gender": "女", "department": "文法学部", "major": "社会学"},
    {"idx": 8, "name": "吴浩然", "gender": "男", "department": "材料与制造学部", "major": "智能制造工程"},
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
    px = img.load()
    w, h = img.size
    for _ in range(w * h // 70):
        x = random.randrange(w)
        y = random.randrange(h)
        delta = random.randint(-amount, amount)
        r, g, b = px[x, y]
        px[x, y] = tuple(max(0, min(255, c + delta)) for c in (r, g, b))
    return img


def draw_card(student):
    idx = student["idx"]
    avatar_path = ASSET_DIR / f"demo_avatar_{idx:02d}.jpg"
    if not avatar_path.exists():
        avatar_path = ASSET_DIR / f"campus_avatar_{idx:02d}.jpg"

    w, h = 1720, 1080
    img = Image.new("RGB", (w, h), "#f8dcc8")
    draw = ImageDraw.Draw(img)

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
    img.paste(photo, (140, 366))

    rows = [
        ("姓名 / Name", student["name"]),
        ("性别 / Gender", student["gender"]),
        ("测试编号 / Demo No.", f"DEMO{20230000 + idx:08d}"),
        ("学部 / Department", student["department"]),
        ("方向 / Major", student["major"]),
    ]
    y = 350
    for label, value in rows:
        draw.text((670, y), label, fill="#7c6b60", font=font(25))
        draw.text((670, y + 36), value, fill="#161616", font=font(54 if label.startswith("姓名") else 40))
        y += 128

    draw.text((1104, 398), "非官方证件", fill="#cf6740", font=font(86))
    draw.text((1107, 492), "PORTFOLIO SAMPLE", fill="#cf6740", font=font(42))
    draw.text((258, 620), "DEMO ONLY", fill="#cf7656", font=font(112))
    draw.text((725, 750), "DEMO ONLY", fill="#cf7656", font=font(112))

    draw.text((112, 982), "仅用于作品集与测试演示，不作为真实身份凭证。", fill="#95583a", font=font(30))
    draw.text((1240, 982), "DEMO ONLY / NOT AN OFFICIAL ID", fill="#95583a", font=font(28))

    img = add_noise(img, 20260525 + idx).filter(ImageFilter.SMOOTH_MORE)
    output = ASSET_DIR / f"demo_student_card_{idx:02d}.jpg"
    img.save(output, quality=94)
    return output


def main():
    outputs = [draw_card(student) for student in STUDENTS]
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
