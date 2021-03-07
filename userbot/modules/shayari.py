
from telethon import events
import asyncio
import random
import re

from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern=f"shayari$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
 
    await asyncio.sleep(0.5)
    
    x=(random.randrange(1,6))
    
    if x==1:

        await event.edit("`\"Main Uska Ho Nahi Sakta,    Woh Meri Ho Nahi Sakti.\"`")

    if x==2:

        await event.edit("`\"Woh Aaye Lakh Khwaabon Main,    Sapna Sach Ho Nahi Sakta.\"`")

    if x==3:

        await event.edit("`\"Mere Nazdeek Ho Kar Bhi,      Nahi Hai Woh Sath Mere.\"`")

    if x==4:

        await event.edit("`\"Usse Neend Nahi Aati,      Yaha Main So Nahi Sakta.\"`")

    if x==5:

        await event.edit("`\"Mohabbat Ka Jo Rishta Hai,     Naa Jaane Kaisa Rishta Hai.\"`")

    if x==6:

        await event.edit("`\"Mera Ho Ke Bhi Koi,     Mera Ho Nahi Sakta!!!.\"`")

