#!/usr/bin/env python3
# pylint: disable=missing-docstring,unused-import,invalid-name,wildcard-import,unused-wildcard-import,broad-exception-caught,bare-except,unused-argument

import os
from pyrogram import Client


BOT_TOKEN = os.environ.get('BOT_TOKEN',
                           '6429401646:AAEg5fapauCi2kauxgPGvArcu_Xip2_gGK4')

plugins = dict(root="plugins")
API_ID = 16514976
API_HASH = '40bd8634b3836468bb2fb7eafe39d81a'


app = Client("NikkiForwardbot",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins=plugins,
             workers=5)



# os.system("clear")
print("Started :)")
app.run()
