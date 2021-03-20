
from telethon import events
import asyncio
import random
import re



@register(outgoing=True, pattern=r"^\.gaali(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
 
    await asyncio.sleep(0.5)
    
    x=(random.randrange(1,6))
    
    if x==1:

        await event.edit("**Main roz teri behno ki banjar chut me apna lawda daalke andar haryali lata tha magar aaj unke ke baare me sunke mujhe bhut afsos huwa ki unko ab bada loudha chahye ab mera balatkaaari lawda lagataar 4 ghante tk apne muh me kon rakhega vo teri behne hi thi jo apni kaali magar rasilli chut mere saamne khol deti aur zameen pe naagin ki tarah rengne lgti thi jaise ki kisine unki chut pe naariyal tod diya ho vo b bada wala mumbai ka naariyal..apni chennal maa ko b nhi bhej rahe mere paas to main kaixe tum logo se vaada karu ki main teri maa chodd dungaw ab agar tun sach me chahta hai ki main tum dono k mc ki chut me dhammal karu to mera lawda apne muh me rakho aur kaho Sameer hamare sage papa hain Aur agar tb b tjhe apni maa ki kaali chut mere saamne nahi rakhi to tumhare ghar me ghuske tumhari maa ka balatkaar kar dungaw jaixe delhi me huwa tha ab teri chudi hui kuttiyo ki tarah apni gaand hilaate hue mere aage kalapna mt ni to tumhari fatti bhoxdi me 100 ched karunga!**")

    if x==2:

        await event.edit("**Beta baap se bakchodi nahi samjha na warna chut mai talwar daalunga ,gand mai jhaadu daalke mor banaunga bhaag bhadve chut maaru  teri maa ki chut mai chappal,ghoda,danda,pathar,wire,giraffe,tiger,talwar Teri maa ko deepak kalal teri maa ko johny bhaiya teri maa ko mai , neta neta har koi kehta tisri manjil pe rehta teri maa ko chodu gand marne jaisa ,tera baap bajaye dol teri maa bajaye pungi teri behen nache nangi usko chode saare bhangi,teri maa meri fan ,teri maa meri randi ,teri maa ko negro, bhadve nikal teri maa nangi karke chodunga samjha bhadva saala,chudne ka shok hai kya tujhe bete aisa chodunga na ghar tak bache dete jayegi tu bhaag madharchod papa bol bete lagta teri gand mai colgate ghisna padega beta,gand mai aalu daalunga tere,galat bande se panga liya beta tu chudega buri tarah add karke pel diye jaaoge samjhe aur bhaag bhi nahi paoge beta Papa hai ham tumhare gand mai ghapak kar se hath daalunga tere tujhe ghodi banakar chodunga samjhi hat randi saali**")

    
