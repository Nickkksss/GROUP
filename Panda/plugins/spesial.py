from . import mention, USERID
import random
from Panda.events import register

ketuakelas = USERID

pengguna = [
    f"Perkenalkan Nama saya {mention}\nTerimah Kasih Ganteng 😏",
    f"Saya {mention} Hadir Kang mas ucok butet neng atau apalah 😂😏",
    f"Terimakasih buat owner Yang ganteng 😊",
    f"Kamshamida owner ganteng 😂 ",
    f"✅ {mention} Aktif  ✅",
]

DEV = [5061420797, 1593802955, 5057493677, 1338398753, 1743866353]
        
@register(incoming=True, from_users=DEV, pattern=r"^absen$")
async def _(event): 
    salam = await event.reply(random.choice(pengguna))
    await asyncio.sleep(10)
    await salam.delete()
    

