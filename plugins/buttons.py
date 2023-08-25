from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def button_from_list(col_list: list, action='view'):
    if len(col_list) == 0:
        return None
    Inline_list = []
    row = []

    for cat in col_list:
        title = cat['title']
        cat_id = cat["_id"]
        ns = title.lower()
        inline = InlineKeyboardButton(
            f"{ns}", callback_data=f"{action}#{str(cat_id)}")
        row.append(inline)

        if len(row) == 3:
            Inline_list.append(row)
            row = []

    if row:  # Add any remaining buttons if not a multiple of 3
        Inline_list.append(row)

    # Add the "Cancel" button
    cancel_button = InlineKeyboardButton("Cancel ❌", callback_data="cancel")
    Inline_list.append([cancel_button])

    return InlineKeyboardMarkup(Inline_list)
