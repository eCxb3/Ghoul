import asyncio
import time
from time import sleep
from userbot.events import register
@register(outgoing=True, pattern="^.gul(.*)")
async def ed(e):
    await e.edit("Я гуль")
    sleep(2)
    a = 1000
    while True:
        c = a - 7
        await e.respond(str(a) + " - 7 = " + str(c))
        if c < 0:
            await e.respond("l l let me die")
            break
        else:
            a = c
    
            
        
