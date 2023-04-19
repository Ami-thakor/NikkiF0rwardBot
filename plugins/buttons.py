from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Define your inline keyboard
DESI_DEL_LIST_BTN = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Yes", callback_data="yesdesidel"),
            InlineKeyboardButton("No", callback_data="cancel")
        ]
    ]
)


# Define your inline keyboard
WEBX_DEL_LIST_BTN = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Yes", callback_data="yeswebdel"),
            InlineKeyboardButton("No", callback_data="cancel")
        ]
    ]
)



LIST_DELETE_BUTTON = InlineKeyboardMarkup(
    [
         [
            InlineKeyboardButton("Desi All", callback_data="listdel#desi"),
            InlineKeyboardButton("WEBx All", callback_data="listdel#webx"),
        ],
        [
            InlineKeyboardButton("Cancel", callback_data="cancel")
        ]
    ]
)



# Define your inline keyboard
DELE_MSGS_BTN = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("DESI-Delete", callback_data="delall#desi"),
            InlineKeyboardButton("WEBx-Delete", callback_data="delall#webx"),
        ],
        [
            InlineKeyboardButton("Cancel", callback_data="cancel")
        ]
    ]
)


ADD_NEW_CHAT_BTN = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("DESI List", callback_data="add#desi"),
            InlineKeyboardButton("WEBx List", callback_data="add#webx"),
            InlineKeyboardButton("Ignore List", callback_data="add#ignore")
            
        ],[InlineKeyboardButton("Cancel", callback_data="cancel")]
    ]
)

REMOVE_CHAT_BTN = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("DESI List", callback_data="remove-desi"),
            InlineKeyboardButton("WEBx List", callback_data="remove-webx"),
            InlineKeyboardButton("Ignore List", callback_data="remove-ignore")
        ],[InlineKeyboardButton("Cancel", callback_data="cancel")]
    ]
)


VIEW_CHANNELS_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("DESI List", callback_data="view-desi"),
            InlineKeyboardButton("WEBx List", callback_data="view-webx"),
        ],
        [InlineKeyboardButton("Cancel", callback_data="cancel")]
    ]
)
