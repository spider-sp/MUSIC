import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS, USER
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["رستر"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ تم اعاده تشغيل السورس**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.command(["الاوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""اهلا بيك يا {m.from_user.mention} 👋
ده سورس ميوزك في الكول 😉
اوامر التشغيل 😅
لتشغيل الاغاني 😂👍
`{HNDLR}تشغيل` + اسم الاغنيه او لينك 
مثل 😒
{HNDLR}تشغيل البخت
لأقاف الاغنية او الفيديو مؤقتآ ⏸
`{HNDLR}ايقاف`
لتشغيل الاغنيه بعد الايقاف مؤقتآ ▶️
`{HNDLR}كمل`
لتشغيل فيديو في الكول 🤓
`{HNDLR}تشغيل_فيديو` + اسم الاغنيه او لينك
مثل 🤬
{HNDLR}تشغيل_فيديو البخت
لتوقيف الاغنيه خالص ⏹ 
{HNDLR}انهاء
لتحميل الاغاني ⏬
`{HNDLR}تحميل` + اسم الاغنيه او اللينك
مثل 😢
{HNDLR}تحميل البخت
لتحميل الفديوهات ⏬
`{HNDLR}تحميل_فيديو` + اسم الاغنيه او اللينك
مثل 😴
{HNDLR}تحميل_فيديو البخت
لتشغيل الاغنيه التاليه 😺
`{HNDLR}التالي`
علشان تعرف الاغاني في الانتظار 😴
`{HNDLR}الانتظار` 
لو السورس هنج 😤
`{HNDLR}رستر`

السورس :- {USER}

𝑩𝒀 :-『𝐒𝐏𝐈𝐃𝐄𝐑』༒『@OOFMO』
𝑪𝑯 :- @OOFMOO"""
    await m.reply(HELP)
@Client.on_message(filters.command(["السورس"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋  اهلا {m.from_user.mention}!
ده سورس ميوزك يا بروو تبع SPIDER
𝑩𝒀 :『𝐒𝐏𝐈𝐃𝐄𝐑』༒『@OOFMO』
𝑪𝑯 : @OOFMOO
"""
    await m.reply(REPO, disable_web_page_preview=True)
