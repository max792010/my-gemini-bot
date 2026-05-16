import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from google import genai

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Gemini 2.5-flash ကို တိုက်ရိုက်ခေါ်ပြီး API Key ကို အသစ်လဲထားပါတယ်
client = genai.Client(api_key="AIzaSyAs9qDUaNl1wq6tvL75uoaeLTFCW7MgFug")

async def h(u, c):
    if not u.message or not u.message.text:
        return
    try:
        r = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=u.message.text
        )
        if r and r.text:
            await u.message.reply_text(r.text)
        else:
            await u.message.reply_text("Sorry, I could not generate a response. Please try again.")
    except Exception as e:
        print(f"Error occurred: {e}")
        try:
            await u.message.reply_text("System busy, please check later.")
        except:
            pass

if __name__ == "__main__":
    print("MAX BOT IS RUNNING ON GEMINI 2.5...")
    app = ApplicationBuilder().token("8660847889:AAFEwvkz4SxepB2VL-80pN-e1S__56OmFG8").build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), h))
    app.run_polling()