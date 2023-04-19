#!/usr/bin/env python3
# pylint: disable=missing-docstring,unused-import,invalid-name,wildcard-import,unused-wildcard-import,broad-exception-caught,bare-except,unused-argument,import-error,undefined-variable

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from plugins.database import *
from plugins.helpers import split_list
from plugins.dele import *


# query to reset full list
@Client.on_callback_query(filters.regex(r'^listdel'))
async def dele_btn_for_desi(_, query: CallbackQuery):
    try:
        msg = query.message
        coll = desi_col
    
        cb_data = query.data.split("#")[-1]

        if cb_data == "webx":
            coll = web_col

        await msg.delete()
        ms = await msg.reply_text("Deleting ALL Channels")
        num = 1
        DESI_CHANNELS = await get_all_channel_ids(coll)
        for channel_id in DESI_CHANNELS:
            try:
                await delete_channel_id(coll, channel_id)
                await ms.edit_text(f"{channel_id} Channel deleted Successfully index {num}.")
                num += 1
                await asyncio.sleep(0.5)
            except:
                pass
        await ms.edit_text("Task Completed")
    except Exception as ex:
        await query.message.reply_text(str(ex))



# query for add chat to particular list
@Client.on_callback_query(filters.regex(r'^add'))
async def add_new_channel_query(app: Client, query: CallbackQuery):
    try:
        msg = query.message.reply_to_message
        coll = desi_col
        channel_id = msg.text.split("/add ")[1]
        ms = await msg.reply_text(f"Adding `{channel_id}`")
    
        cb_data = query.data.split("#")[-1]

        if cb_data == "webx":
            coll = web_col

        elif cb_data == "ignore":
            coll = ignore_col
            await ms.edit_text(f"{channel_id} Channel added Successfully.")
            return await add_ignore_id(channel_id)

        await add_channel_id(coll, channel_id, app)
        await ms.edit_text(f"{channel_id} Channel added Successfully.")
    except Exception as ex:
        await query.message.reply_text(str(ex))

    await query.message.delete()

# query for remove chat from particular list
@Client.on_callback_query(filters.regex(r'^remove'))
async def remove_channel_query(app: Client, query: CallbackQuery):
    try:
        msg = query.message.reply_to_message
        coll = desi_col
        channel_id = msg.text.split("/remove ")[1]
        ms = await msg.reply_text(f"Removing `{channel_id}`")
    
        cb_data = query.data.split("-")[-1]

        if cb_data == "webx":
            coll = web_col

        elif cb_data == "ignore":
            coll = ignore_col
            await ms.edit_text(f"{channel_id} Channel Removed Successfully.")
            return await add_ignore_id(channel_id)

        await delete_channel_id(coll, channel_id)
        await ms.edit_text(f"{channel_id} Channel Removed Successfully.")
    except Exception as ex:
        await query.message.reply_text(str(ex))

    await query.message.delete()

# query for view all channels as list and subs
@Client.on_callback_query(filters.regex(r'^view'))
async def views_channel_query(app: Client, query: CallbackQuery):
    try:
        M = query.message
        coll = desi_col
    
        cb_data = query.data.split("-")[-1]

        if cb_data == "webx":
            coll = web_col

        total_channels_text, info_list, total_subs_text = await get_all_chat_info(coll)
        text = total_channels_text + '\n'.join(info_list) + '\n' + total_subs_text
        result = split_list(info_list)
        await M.delete()
        if len(result) == 1:
            pass
        elif len(result) == 2:
            text1 = total_channels_text + "\n".join(result[0])
            text2 = '\n'.join(result[1]) + '\n' + total_subs_text
            await M.reply_text(text1)
            return await M.reply_text(text2)

        elif len(result) == 3:
            text1 = total_channels_text + "\n".join(result[0])
            text2 = '\n'.join(result[1])
            text3 = '\n'.join(result[2]) + '\n' + total_subs_text
            await M.reply_text(text1)
            await M.reply_text(text2)
            return await M.reply_text(text3)

        await M.reply_text(text)
    except Exception as ex:
        await query.message.reply_text(str(ex))
    
    


# query for delete old messages 
@Client.on_callback_query(filters.regex(r'^delall'))
async def dele_all_query(app: Client, query: CallbackQuery):
    try:
        file = "DESIX"
        msg = query.message.reply_to_message
    
        cb_data = query.data
        msg_id = int(msg.text.split('/delall ')[-1])

        list_name = cb_data.split("#")[1]

        if list_name == "webx":
            file = "WEBX"

        if not os.path.exists(f"{file}-DELEMSGs.dat"):
            return
        dele_dic = await showdata(file)
        suc_task = 0
        for i in dele_dic:
            try:
                await app.delete_messages(i, dele_dic[i] + msg_id)
                suc_task += 1
                print(suc_task, 'Deleted ✔️')

            except Exception as e:
                print(e)
        print(f'Sucesss Task : {suc_task} \nField Task :{len(dele_dic)-suc_task}')
    
    except Exception as ex:
        await query.message.reply_text(str(ex))

    await query.message.delete()


@Client.on_callback_query(filters.regex(r'^cancel$'))
async def cancel_button(_, query: CallbackQuery):
    msg = query.message
    try:
        await msg.delete()
    except:
        pass
