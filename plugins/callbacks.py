#!/usr/bin/env python3
# pylint: disable=missing-docstring,unused-import,invalid-name,wildcard-import,unused-wildcard-import,broad-exception-caught,bare-except,unused-argument,import-error,undefined-variable

import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from plugins.database import *
from plugins.dele import *


# query for add chat to particular list
@Client.on_callback_query(filters.regex(r'^add'))
async def add_new_channel_query(app: Client, query: CallbackQuery):
    try:
        msg = query.message.reply_to_message
        cat_id = query.data.split("#")[1]

        channel_id = msg.text.split("/add ")[1]
        await update_by_id(cat_id, channel_id)

        ms = await msg.reply_text(f"Added `{channel_id}`")

    except Exception as ex:
        await query.message.reply_text(str(ex))

    finally:
        await query.message.delete()


# query for add chat to particular list
@Client.on_callback_query(filters.regex(r'^delete'))
async def sure_delete_category(app: Client, query: CallbackQuery):
    button = []
    try:
        cat_id = query.data.split("#")[1]
        
        # sure_button = # Add the "Cancel" button
        sure_button = InlineKeyboardButton(
            "Sure ❌", callback_data=f"sure#{str(cat_id)}")
        cancel_button = InlineKeyboardButton(
            "Cancel ✔️", callback_data="cancel")

        cancel_button2 = InlineKeyboardButton(
            "Don't delete ✅", callback_data="cancel")

        # Create a list of buttons
        button = [[sure_button], [cancel_button], [cancel_button2]]

        # Shuffle the list to randomize the order
        random.shuffle(button)

        sure = InlineKeyboardMarkup(button)
        await query.message.edit_text("Are you Sure and want delete this category.", reply_markup=sure)
    except:
        pass

REPORT_MAN = 1286693857
# query for add chat to particular list
@Client.on_callback_query(filters.regex(r'^sure'))
async def delete_category(app: Client, query: CallbackQuery):
    try:
        msg = query.message.reply_to_message
        cat_id = query.data.split("#")[1]
        result = await show_category(cat_id)
        name = result['title']
        data = await show_category(cat_id)

        basic_info = f"Category Name: {data['title']}\nSource Channel ID: {data['_id']}\n"

        text = f"{basic_info}\nTotal CHannels: {len(data['chat_ids'])}\n" + "\n".join(str(item)
                                                                                      for item in data['chat_ids'])
        with open('report.txt', 'w', encoding='utf-8') as file:
            file.write(text)
        user = query.from_user.id

        try:
            await app.send_document(user, "report.txt")
        except:
            pass

        await delete_channel_id(categories, cat_id)

        ms = await msg.reply_text(f"Deleted `{name}` category.")

    except Exception as ex:
        await query.message.reply_text(str(ex))

    finally:
        await query.message.delete()


# query for add chat to particular list


@Client.on_callback_query(filters.regex(r'^remove'))
async def remove_channel_query(app: Client, query: CallbackQuery):
    try:
        msg = query.message.reply_to_message
        cat_id = query.data.split("#")[1]

        channel_id = msg.text.split("/remove ")[1]
        await remove_by_id(cat_id, channel_id)

        ms = await msg.reply_text(f"Removed `{channel_id}`")

    except Exception as ex:
        await query.message.reply_text(str(ex))

    finally:
        await query.message.delete()


@Client.on_callback_query(filters.regex(r'^view'))
async def views_channel_query(app: Client, query: CallbackQuery):
    try:
        cat_id = query.data.split("#")[1]
        data = await show_category(cat_id)

        basic_info = f"Category Name: {data['title']}\nSource Channel ID: {data['_id']}\n"

        text = f"{basic_info}\nTotal CHannels: {len(data['chat_ids'])}\n" + "\n".join(str(item)
                                                                                      for item in data['chat_ids'])
        with open('report.txt', 'w', encoding='utf-8') as file:
            file.write(text)

        user = query.from_user.id

        try:
            await app.send_document(user, "report.txt")
        except:
            pass

    except Exception as ex:
        await query.message.reply_text(str(ex))
    finally:
        await query.message.delete()


@Client.on_callback_query(filters.regex(r'^cancel$'))
async def cancel_button(_, query: CallbackQuery):
    msg = query.message
    try:
        await msg.delete()
    except:
        pass
