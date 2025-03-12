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

TOKEN = "8072368645:AAEQ38wkKj7dWUpErRzaGPyL6qg3dsMGZM0" 
Safeguard_Image = Image.open('assets/safeguard.jpg')


User_btn = InlineKeyboardButton(text = "👤 User message bot", callback_data="user_btn")
Popup_btn = InlineKeyboardButton(text = "💬 Instant Popup", callback_data="popup_btn")
Support_button = InlineKeyboardButton(text="💬 Support", url="https://t.me/whalesharka", callback_data="Support_button")

async def clickHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the button click."""
    print("clickHandler")
    query = update.callback_query
    await query.answer()
    # Extract the callback data from the clicked button
    callback_data = query.data
    

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    keyboard = [[User_btn, Popup_btn]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = f"""
test_channel is being protected by @Safeguard
""" 
    bio = BytesIO()
    Safeguard_Image.save(bio, format="JPEG")
    bio.seek(0)
    await update.message.reply_photo(photo=bio, caption=message, reply_markup=reply_markup) 

if __name__== '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CallbackQueryHandler(clickHandler))
    application.run_polling()