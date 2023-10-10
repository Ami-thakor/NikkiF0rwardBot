#!/usr/bin/env python3
# pylint: disable=missing-docstring,unused-import,invalid-name,wildcard-import,unused-wildcard-import,broad-exception-caught,bare-except,unused-argument,import-error
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

from plugins.dele import *
from plugins.database import *
from plugins.buttons import *

SUDO_USERS = [6198910870, 6298547816, 6379854466,
              6308864158, 5294965763, 874964742]


START_TEXT = "Hlw am Auto Forward Bot"
@Client.on_message(filters.user(SUDO_USERS) & filters.command(['start']))
async def start_message(_, M: Message):
    await M.reply_text(START_TEXT)


@Client.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(['view', 'list']))
async def list_message(_, msg: Message):
    try:
        col_list = await get_all_cats()
        button = await button_from_list(col_list, 'view')
        if not button:
            return await msg.reply_text("Please first add at least one category then try again.")
        await msg.reply_text("Which List Want to See", reply_markup=button, quote=True)
    except:
        pass


@Client.on_message(filters.command('category') & filters.reply & filters.user(SUDO_USERS))
async def add_new_category(app: Client, msg: Message):
    try:
        text = msg.text
        _, name = text.split("/category ")
        if len(name) > 27:
            return await msg.reply_text("Please try short name for category (5-28 letters)")

        if len(name) < 5:
            return await msg.reply_text("Please try long name for category (5-28 letters)")
        cats = await get_all_channel_ids(categories)
        if len(cats) > 9:
            return await msg.reply_text("Maximum limit 9 reached delete any then try again.")

        try:
            if msg.reply_to_message.forward_from_chat:
                chat_id = str(msg.reply_to_message.forward_from_chat.id)
                await add_category(chat_id, name)
                await msg.reply_text("This category has been added, check /list to see. what the f#uck")

        except Exception as ex:
            await msg.reply_text(str(ex))
    except:
        pass


ADD_PATTERN = r"^/add\s-?\d+$"
REMOVE_PATTERN = r"^/remove\s-?\d+$"


@Client.on_message(filters.private & filters.user(SUDO_USERS) & filters.regex(ADD_PATTERN))
async def adding_channel(app: Client, msg: Message):
    try:
        col_list = await get_all_cats()
        button = await button_from_list(col_list, 'add')
        if not button:
            return await msg.reply_text("Please first add at least one category then try again.")
        await msg.reply_text("Which List Want to Add this channel", reply_markup=button, quote=True)
    except:
        pass

# /add -100812546978


@Client.on_message(filters.private & filters.user(SUDO_USERS) & filters.regex(REMOVE_PATTERN))
async def remove_channel(app: Client, msg: Message):
    try:

        col_list = await get_all_cats()
        button = await button_from_list(col_list, 'remove')
        if not button:
            return await msg.reply_text("Please first add at least one category then try again.")
        await msg.reply_text("Select List Want to Remove this channel", reply_markup=button, quote=True)
    except:
        pass


@Client.on_message(filters.private & filters.user(SUDO_USERS) & filters.command('delete'))
async def delete_category(app: Client, msg: Message):
    try:
        col_list = await get_all_cats()
        button = await button_from_list(col_list, 'delete')
        if not button:
            return await msg.reply_text("Please first add at least one category then try again.")
        await msg.reply_text("Select Category that you Want to Delete", reply_markup=button, quote=True)
    except:
        pass


# & filters.user(SUDO_USERS)
@Client.on_message(filters.channel & filters.incoming)
async def Handler_All_Channels(app: Client, msg: Message):
    try:

        curr_id = msg.chat.id
        await asyncio.sleep(2)
        result = await show_category(curr_id)
        if not result:
            return
        # cat_id = result["_id"]
        chats_list = result["chat_ids"]
        if len(chats_list) == 0:
            return
        caption = None
        failed = []
        success = []
        text = "Finished"

        for chat in chats_list:
            if msg.caption:
                caption = msg.caption.html
                try:
                    await msg.copy(chat, caption=caption)
                    success.append(chat)
                except:
                    failed.append(chat)

            if msg.text:
                try:
                    await msg.copy(chat)
                    success.append(chat)
                except:
                    failed.append(chat)

    except:
        pass
