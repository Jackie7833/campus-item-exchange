from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import random


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "api" / "templates" / "front"

FONT_CANDIDATES = [
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
]


def font(size, bold=False):
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size, index=0)
    return ImageFont.load_default()


TITLE_FONT = font(58)
SUBTITLE_FONT = font(30)
NAME_FONT = font(52)
LABEL_FONT = font(25)
TEXT_FONT = font(39)
WATERMARK_FONT = font(72)
SMALL_FONT = font(22)


STUDENTS = [
    {"idx": 1, "account": "student01", "nick": "北工小李", "name": "李明", "gender": "男", "phone": "13823888001", "email": "20230001@bjut.edu.cn", "department": "信息学部", "major": "人工智能产品方向", "status": "是", "reply": "测试样例：身份信息已审核通过"},
    {"idx": 2, "account": "student02", "nick": "晴天同学", "name": "王雨晴", "gender": "女", "phone": "13823888002", "email": "20230002@bjut.edu.cn", "department": "经济与管理学院", "major": "信息管理与信息系统", "status": "待审核", "reply": "测试样例：待人工复核"},
    {"idx": 3, "account": "student03", "nick": "实验楼阿涵", "name": "张子涵", "gender": "女", "phone": "13823888003", "email": "20230003@bjut.edu.cn", "department": "信息学部", "major": "软件工程", "status": "是", "reply": "测试样例：身份信息已审核通过"},
    {"idx": 4, "account": "student04", "nick": "骑行小陈", "name": "陈思远", "gender": "男", "phone": "13823888004", "email": "20230004@bjut.edu.cn", "department": "城市建设学部", "major": "智能建造", "status": "待审核", "reply": "测试样例：待人工复核"},
    {"idx": 5, "account": "student05", "nick": "图书馆宁宁", "name": "刘佳宁", "gender": "女", "phone": "13823888005", "email": "20230005@bjut.edu.cn", "department": "艺术设计学院", "major": "数字媒体设计", "status": "否", "reply": "测试样例：证件图不清晰，请重新上传"},
    {"idx": 6, "account": "student06", "nick": "键盘赵同学", "name": "赵一鸣", "gender": "男", "phone": "13823888006", "email": "20230006@bjut.edu.cn", "department": "信息学部", "major": "计算机科学与技术", "status": "是", "reply": "测试样例：身份信息已审核通过"},
    {"idx": 7, "account": "student07", "nick": "青柠可欣", "name": "周可欣", "gender": "女", "phone": "13823888007", "email": "20230007@bjut.edu.cn", "department": "文法学部", "major": "社会学", "status": "待审核", "reply": "测试样例：待人工复核"},
    {"idx": 8, "account": "student08", "nick": "篮球小吴", "name": "吴浩然", "gender": "男", "phone": "13823888008", "email": "20230008@bjut.edu.cn", "department": "材料与制造学部", "major": "智能制造工程", "status": "是", "reply": "测试样例：身份信息已审核通过"},
]


def rounded_rectangle(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_avatar(student):
    random.seed(student["idx"])
    size = 520
    img = Image.new("RGB", (size, size), "#f3f6f8")
    draw = ImageDraw.Draw(img)
    colors = ["#3066BE", "#00A896", "#F26A4F", "#6C5CE7", "#2D9CDB", "#B85C38", "#008080", "#8E44AD"]
    bg = colors[(student["idx"] - 1) % len(colors)]
    draw.ellipse((28, 28, size - 28, size - 28), fill=bg)
    draw.ellipse((168, 112, 352, 296), fill="#f4d2bd")
    draw.rounded_rectangle((122, 286, 398, 500), radius=115, fill="#172033")
    draw.arc((150, 95, 370, 285), 190, 350, fill="#2b211e", width=52)
    draw.ellipse((207, 205, 224, 222), fill="#33251f")
    draw.ellipse((296, 205, 313, 222), fill="#33251f")
    draw.arc((228, 230, 292, 280), 15, 165, fill="#8d4d44", width=5)
    initial = student["name"][0]
    draw.text((38, 34), initial, fill=(255, 255, 255, 80), font=font(112))
    draw.text((size - 142, size - 70), "DEMO", fill=(255, 255, 255), font=SMALL_FONT)
    path = ASSET_DIR / f"demo_avatar_{student['idx']:02d}.jpg"
    img.save(path, quality=92)


def draw_student_card(student):
    w, h = 1720, 1080
    img = Image.new("RGB", (w, h), "#f7d9c5")
    draw = ImageDraw.Draw(img)

    for y in range(h):
        r = int(247 - y * 18 / h)
        g = int(217 - y * 34 / h)
        b = int(197 - y * 42 / h)
        draw.line((0, y, w, y), fill=(r, g, b))

    random.seed(student["idx"] * 17)
    for _ in range(9500):
        x = random.randrange(w)
        y = random.randrange(h)
        tone = random.randrange(-12, 13)
        base = img.getpixel((x, y))
        img.putpixel((x, y), tuple(max(0, min(255, c + tone)) for c in base))

    draw = ImageDraw.Draw(img)
    rounded_rectangle(draw, (20, 20, w - 20, h - 20), 40, None, "#d6a889", 3)

    draw.ellipse((92, 95, 250, 253), fill="#0c77b8", outline="#e7f5ff", width=8)
    draw.text((125, 124), "CL", fill="white", font=font(64))
    draw.text((112, 205), "DEMO", fill="#d8efff", font=SMALL_FONT)
    draw.text((300, 118), "校园物品流转平台", fill="#1269a8", font=TITLE_FONT)
    draw.text((305, 187), "Campus Circulation Platform", fill="#6790aa", font=SUBTITLE_FONT)
    draw.text((760, 122), "测试学生身份卡", fill="#4a5568", font=SUBTITLE_FONT)
    draw.text((760, 172), "DEMO STUDENT PROFILE CARD", fill="#4a5568", font=SUBTITLE_FONT)

    for i in range(-1, 3):
        draw.text((300 + i * 500, 465 + i * 125), "DEMO ONLY", fill=(205, 105, 85), font=WATERMARK_FONT)
    draw.text((1135, 410), "非官方证件", fill=(211, 105, 62), font=font(84))
    draw.text((1138, 500), "PORTFOLIO SAMPLE", fill=(211, 105, 62), font=font(40))

    avatar_path = ASSET_DIR / f"demo_avatar_{student['idx']:02d}.jpg"
    avatar = Image.open(avatar_path).resize((430, 520)).filter(ImageFilter.SMOOTH_MORE)
    rounded_rectangle(draw, (118, 360, 588, 910), 18, "#fff8f2", "#efc3a7", 3)
    img.paste(avatar, (138, 378))

    x0 = 660
    y0 = 360
    rows = [
        ("姓名 / Name", student["name"]),
        ("性别 / Gender", student["gender"]),
        ("测试编号 / Demo No.", f"DEMO{20230000 + student['idx']:08d}"),
        ("学部 / Department", student["department"]),
        ("方向 / Major", student["major"]),
    ]
    for label, value in rows:
        draw.text((x0, y0), label, fill="#7b6a5e", font=LABEL_FONT)
        draw.text((x0, y0 + 34), value, fill="#171717", font=NAME_FONT if label.startswith("姓名") else TEXT_FONT)
        y0 += 125

    draw.text((112, 982), "仅用于校园物品流转平台作品集演示，不作为真实身份凭证。", fill="#9a5d3c", font=font(28))
    draw.text((1260, 982), "DEMO ONLY / NOT AN OFFICIAL ID", fill="#9a5d3c", font=font(28))

    path = ASSET_DIR / f"demo_student_card_{student['idx']:02d}.jpg"
    img.save(path, quality=92)


def main():
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    for student in STUDENTS:
        draw_avatar(student)
        draw_student_card(student)
    print(f"generated {len(STUDENTS)} demo student cards in {ASSET_DIR}")


if __name__ == "__main__":
    main()
