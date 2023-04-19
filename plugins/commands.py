#!/usr/bin/env python3
# pylint: disable=missing-docstring,unused-import,invalid-name,wildcard-import,unused-wildcard-import,broad-exception-caught,bare-except,unused-argument,import-error

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from plugins.dele import *
from plugins.database import *
from plugins.buttons import *

SUDO_USERS = [5294965763,874964742,5144980226,839221827]
@Client.on_message(filters.command(['start']))
async def start_message(_, M: Message):
    await M.reply_text("Hlw Join @CrazeBots")


# to add new channel to collection
@Client.on_message(filters.user(SUDO_USERS) & filters.command(['help']))
async def add_message(a: Client, msg: Message):
    await msg.reply_text("`/add` `/remove` `/listdel` `/view /list` `/info` `/id` `/wforward` `/wcopy` `/dforward` `/delall`")


    
# to add new channel to collection
@Client.on_message(filters.user(SUDO_USERS) & filters.command(['add']))
async def add_message(a: Client, msg: Message):
    await msg.reply_text("Select List to Add Your Channel", reply_markup=ADD_NEW_CHAT_BTN, quote=True)

# to remove channel from collection
@Client.on_message(filters.user(SUDO_USERS) & filters.command(['remove']))
async def rem_message(a: Client, msg: Message):
    await msg.reply_text("Select List to Remove Your Channel", reply_markup=REMOVE_CHAT_BTN, quote=True)


# to delete all channels from collection
@Client.on_message(filters.user(SUDO_USERS) & filters.command(['listdel']))
async def listdel_message(_, msg: Message):
    await msg.reply_text("Select List to Delete", reply_markup=LIST_DELETE_BUTTON)

# view all channels from lists
@Client.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(['view', 'list']))
async def list_message(_, msg: Message):
    await msg.reply_text("Which List Want to See", reply_markup=VIEW_CHANNELS_BUTTON)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(['info']))
async def info_message(_, msg: Message):
    try:
        chat_id = msg.text.split("/info ")[-1]
        output = await get_chat_info(chat_id)
        await msg.reply_text(output)
    except Exception as ex:
        await msg.reply_text(str(ex))


@Client.on_message(filters.user(SUDO_USERS) & filters.command(['id']))
async def id_message(_, msg: Message):
    chat_id = ''
    try:
        if msg.reply_to_message:
            if msg.reply_to_message.forward_from_chat:
                chat_id = str(msg.reply_to_message.forward_from_chat.id)
        userid = msg.from_user.id
        text = f"UserID: `{userid}`\nChatID: `{chat_id}`"

        await msg.reply_text(text)
    except Exception as ex:
        await msg.reply_text(str(ex))


@Client.on_message(filters.user(SUDO_USERS) & filters.command(['wforward']))
async def wforward_message(_, msg: Message):
    try:
        if not msg.reply_to_message:
            return await msg.reply_text(msg.text)

        text = "Finished"
        DELE_MSG_IDS = {}
        SUCCESS = 1
        FAILED_CHATS = []

        chat_ids = await get_all_channel_ids(web_col)
        start_msg = await msg.reply_text("Forwarding Started")
        IGNORE_IDS = await get_all_channel_ids(ignore_col)

        for chat_id in chat_ids:
            if chat_id in IGNORE_IDS:
                continue
            if SUCCESS % 20 == 0:
                try:
                    await start_msg.edit_text(f"In Progress:\nSuccess: {SUCCESS}")
                except:
                    pass
            try:
                sent_msg = await msg.reply_to_message.forward(chat_id, disable_notification=True)
                ch_id = sent_msg.chat.id
                m_id = sent_msg.id
                DELE_MSG_IDS[ch_id] = m_id
                SUCCESS += 1
                await asyncio.sleep(0.2)

            except:
                FAILED_CHATS.append(chat_id)

            text = f"{text}\n{SUCCESS}" + "\n".join(FAILED_CHATS)

        await msg_dict_func(DELE_MSG_IDS, 'WEBX')

        await start_msg.edit_text(text)

    except Exception as ex:
        await msg.reply_text(str(ex))




@Client.on_message(filters.user(SUDO_USERS) & filters.command(['wcopy']))
async def wcopy_message(_, msg: Message):
    try:
        if not msg.reply_to_message:
            return await msg.reply_text(msg.text)

        text = "Finished"
        DELE_MSG_IDS = {}
        SUCCESS = 1
        FAILED_CHATS = []

        chat_ids = await get_all_channel_ids(web_col)
        start_msg = await msg.reply_text("Copying Started")
        IGNORE_IDS = await get_all_channel_ids(ignore_col)

        for chat_id in chat_ids:
            if chat_id in IGNORE_IDS:
                continue
            if SUCCESS % 20 == 0:
                try:
                    await start_msg.edit_text(f"In Progress:\nSuccess: {SUCCESS}")
                except:
                    pass
            try:
                sent_msg = await msg.reply_to_message.copy(chat_id, disable_notification=True)
                ch_id = sent_msg.chat.id
                m_id = sent_msg.id
                DELE_MSG_IDS[ch_id] = m_id
                SUCCESS += 1
                await asyncio.sleep(0.2)

            except:
                FAILED_CHATS.append(chat_id)

            text = f"{text}\n{SUCCESS}" + "\n".join(FAILED_CHATS)

        await msg_dict_func(DELE_MSG_IDS, 'WEBX')

        await start_msg.edit_text(text)

    except Exception as ex:
        await msg.reply_text(str(ex))





@Client.on_message(filters.user(SUDO_USERS) & filters.command(['dforward']))
async def dforward_message(_, msg: Message):
    try:
        if not msg.reply_to_message:
            return await msg.reply_text(msg.text)

        text = "Finished"
        DELE_MSG_IDS = {}
        SUCCESS = 1
        FAILED_CHATS = []

        chat_ids = await get_all_channel_ids(desi_col)
        start_msg = await msg.reply_text("Forwarding Started")
        IGNORE_IDS = await get_all_channel_ids(ignore_col)

        for chat_id in chat_ids:
            if chat_id in IGNORE_IDS:
                continue
            if SUCCESS % 20 == 0:
                try:
                    await start_msg.edit_text(f"In Progress:\nSuccess: {SUCCESS}")
                except:
                    pass
            try:
                sent_msg = await msg.reply_to_message.forward(chat_id, disable_notification=True)
                ch_id = sent_msg.chat.id
                m_id = sent_msg.id
                DELE_MSG_IDS[ch_id] = m_id
                SUCCESS += 1
                await asyncio.sleep(0.2)

            except:
                FAILED_CHATS.append(chat_id)

            text = f"{text}\n{SUCCESS}" + "\n".join(FAILED_CHATS)

        await msg_dict_func(DELE_MSG_IDS, 'DESIX')

        await start_msg.edit_text(text)

    except Exception as ex:
        await msg.reply_text(str(ex))


@Client.on_message(filters.user(SUDO_USERS) & filters.command(['delall']))
async def delete_last_msg(app, msg):
    await msg.reply_text("Choose From Below Lists", reply_markup=DELE_MSGS_BTN,quote=True)
