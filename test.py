# from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# VIEW_CHANNELS_BUTTON = InlineKeyboardMarkup(
#     [
#         [
#             InlineKeyboardButton("DESI List", callback_data="view-desi"),
#             InlineKeyboardButton("WEBx List", callback_data="view-webx"),
#             InlineKeyboardButton("Ignore List", callback_data="ignore_list")
#         ],
#         [InlineKeyboardButton("Cancel", callback_data="cancel")]
#     ]
# )


# async def button_from_list(col_list:list):
#     Inline_list = []
#     for btn_text in col_list:
#         ns = btn_text.uppercase()
#         inline = InlineKeyboardButton(f"{ns}", callback_data=f"{btn_text}")
#         Inline_list.append(inline)

    

    



# #     BUTTON = InlineKeyboardMarkup(
# #     [
# #         [
# #             InlineKeyboardButton("DESI List", callback_data="view-desi"),
# #             InlineKeyboardButton("WEBx List", callback_data="view-webx"),
# #             InlineKeyboardButton("Ignore List", callback_data="ignore_list")
# #         ],
# #         [InlineKeyboardButton("Cancel", callback_data="cancel")]
# #     ]
# # )

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def button_from_list(col_list: list):
    Inline_list = []
    row = []
    
    for btn_text in col_list:
        ns = btn_text.upper()
        inline = InlineKeyboardButton(f"{ns}", callback_data=f"{btn_text}")
        row.append(inline)
        
        if len(row) == 3:
            Inline_list.append(row)
            row = []
    
    if row:  # Add any remaining buttons if not a multiple of 3
        Inline_list.append(row)
    
    return InlineKeyboardMarkup(Inline_list)


