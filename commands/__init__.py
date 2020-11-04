from subtitle import (
    BASE_URL,
    get_lang,
    search_sub
)

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>Hi {update.effective_user.first_name}!, My Name Is 𝗔𝗟𝗟 𝗦𝗨𝗕𝗧𝗜𝗧𝗟𝗘 𝗕𝗢𝗧 🥳\n\nI'm A <u>𝗧𝗘𝗟𝗚𝗥𝗔𝗠 𝗦𝗨𝗕𝗧𝗜𝗧𝗟𝗘 𝗦𝗘𝗔𝗥𝗖𝗛 𝗥𝗢𝗕𝗢𝗧.</u>\n\nSend Me Any 𝗠𝗢𝗩𝗜𝗘 𝗡𝗔𝗠𝗘 & I'll Search My Database If It's Avaliable.\n\n𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @Modzilla 𝗜𝗳 𝗬𝗼𝘂 𝗟𝗼𝘃𝗲 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 ♥️.</b>, parse_mode="HTML")

def searching(update: Update, context: CallbackContext):
    if update.message.via_bot != None:
        return

    search_message = context.bot.send_message(chat_id=update.effective_chat.id, text="Searching your subtitle file")
    sub_name = update.effective_message.text
    full_index, title, keyword = search_sub(sub_name)
    inline_keyboard = []
    if len(full_index) == 0:
        context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=search_message.message_id, text="No results found")
        return
    
    index = full_index[:15]
    for i in index:
        subtitle = title[i-1]
        key = keyword[i-1]
        inline_keyboard.append([InlineKeyboardButton(subtitle, callback_data=f"{key}")])

    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=search_message.message_id, text=f"Got the following results for your query *{sub_name}*. Select the preffered type from the below options", parse_mode="Markdown", reply_markup=reply_markup)
