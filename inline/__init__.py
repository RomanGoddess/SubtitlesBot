from uuid import uuid4

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineQueryResultDocument
)

from subtitle import (
    BASE_URL,
    get_lang,
    search_sub
)


def button(update, context):
    query = update.callback_query
    query.answer()
    sub = query.data
    index, language, link = get_lang(sub)

    if len(index) == 0:
        query.edit_message_text(text="Something went wrong")
        return

    inline_keyboard = []
    for i in range(len(index)):
        button_name = language[i-1]
        button_data = link[i-1]
        inline_keyboard.append([InlineKeyboardButton(f"{button_name.upper()}", switch_inline_query_current_chat=f"{button_data}")])

    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    query.edit_message_text(text="Select your language", reply_markup=reply_markup)

def inlinequery(update, context):
    query = update.inline_query.query
    inline = [
        [
            InlineKeyboardButton("𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣", url="https://telegram.dog/LeechZone"),
            InlineKeyboardButton("𝗢𝗨𝗥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url="https://t.me/joinchat/AAAAAE-44AkxSyqIMj1tdQ")
        ]
    ]
    results = [
        InlineQueryResultDocument(
            id=uuid4(),
            document_url=query,
            title="Get the File",
            mime_type="application/zip",
            reply_markup=InlineKeyboardMarkup(inline),
            caption="©️ @AllSubtitleBot\n\nUse @UnzipTGBot for unzipping this zip file or download the file and unzip manually"
        )
    ]
    update.inline_query.answer(results)
