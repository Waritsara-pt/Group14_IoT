
import lcd
import time
import ui

# =========================
# ข้อมูลของทีม
# =========================

TEAM_NAME = "Group14"
MOTTO = "มั่วอย่างมีระบบ"

MEMBERS = [
    ("กัญญาณัฐ", "Recorder"),
    ("จิรายุ", "Navigator"),
    ("วริศรา", "Driver")
]


# =========================
# แสดงข้อมูลใน Console
# =========================

lcd.clear()

lcd.print("<h2>จอต้อนรับทีม</h2>")
lcd.print("ชื่อทีม: ", TEAM_NAME)
lcd.print("คำขวัญ: ", MOTTO)

for i in range(len(MEMBERS)):
    name = MEMBERS[i][0]
    role = MEMBERS[i][1]

    lcd.print("สมาชิก", i + 1, ":", name, "-", role)
    time.sleep_ms(300)

lcd.print("<span class=ok>พร้อมลุย!</span>")


# =========================
# แสดงหน้าจอ Playground
# =========================

ui.screen()
time.sleep_ms(200)

# สี
COL_TEXT = 0xE8EAED
COL_DIM = 0x9AA3AF
COL_CARD = 0x171B22
COL_OK = 0x30A46C
COL_RUN = 0x4A9EFF


# =========================
# ส่วนหัวของทีม
# =========================

ui.Panel(
    x=16, y=8,
    w=760, h=372,
    color=COL_CARD,
    min=COL_DIM,
    max=12,
    value=1
)

ui.Label(
    "จอต้อนรับทีม",
    x=32, y=16,
    color=COL_DIM,
    value=20
)

ui.Label(
    TEAM_NAME,
    x=32, y=40,
    color=COL_TEXT,
    value=28
)

ui.Label(
    MOTTO,
    x=32, y=84,
    color=COL_OK,
    value=20
)


# =========================
# รายชื่อสมาชิกและหน้าที่
# =========================

ui.Label(
    "สมาชิกในทีม",
    x=32, y=120,
    color=COL_DIM,
    value=20
)

tbl = ui.Table(
    x=32, y=150,
    w=500, h=210,
    cols=2
)

tbl.col_width(0, 200)
tbl.col_width(1, 250)

tbl.add_row("ชื่อสมาชิก", "หน้าที่")

for i in range(len(MEMBERS)):
    name = MEMBERS[i][0]
    role = MEMBERS[i][1]

    tbl.add_row(name, role)

    ui.poll()
    time.sleep_ms(300)

ui.poll()

