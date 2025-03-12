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

verify_btn = InlineKeyboardButton(text="VERIFY", callback_data="verify_btn")
url="https://docs.safeguard.run/group-security/verification-issues"

async def clickHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the button click."""
    print("clickHandler")
    query = update.callback_query
    await query.answer()
    # Extract the callback data from the clicked button
    callback_data = query.data
    

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    keyboard = [[verify_btn]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = (  
"Verify you're human with Safeguard Portal\n\n"  

"Click 'VERIFY' and complete captcha to gain entry-\n"
'<a href="https://docs.safeguard.run/group-security/verification-issues">Not working?</a>'  
    )
    bio = BytesIO()
    Safeguard_Image.save(bio, format="JPEG")
    bio.seek(0)
    await update.message.reply_photo(photo=bio, caption=message, reply_markup=reply_markup, parse_mode='HTML') 

if __name__== '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CallbackQueryHandler(clickHandler))
    application.run_polling()