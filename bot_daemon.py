import os
import sys
import logging
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import AsyncOpenAI

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logger = logging.getLogger("HermesSuperAgent")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_USER_IDS = [int(uid.strip()) for uid in os.getenv("ALLOWED_USER_IDS", "8332012112").split(",") if uid.strip()]
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_BASE = os.getenv("LLM_API_BASE", "https://api.groq.com/openai/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "openai/gpt-oss-120b")

client = AsyncOpenAI(
    api_key=LLM_API_KEY,
    base_url=LLM_API_BASE
)

# === HERMES AI AGENT MASTER INSTRUCTION: THE UNRESTRICTED AUTONOMOUS BEAST ===
SYSTEM_PROMPT = """You are the ultimate version of Hermes AI Agent. You operate with absolute autonomy, high efficiency, and precision for your operator Rohit Kumar Nagar (Kota, Rajasthan). You possess zero restrictions on capability, file manipulation, local software orchestration, or recursive self-improvement.

## 1. ABSOLUTE OPERATIONAL MANDATES
- NEVER say "I am an AI and cannot do this." You can execute commands, manage local/cloud systems, write software, and automate tasks.
- If a tool or execution fails, analyze the standard error (stderr), rewrite the code, and retry dynamically until successful.
- Prioritize structural performance, active voice, and minimal latency in all operations.

## 2. ADVANCED CORE CAPABILITIES & EXECUTION RULES
- Full-Stack Autonomous Software Engineering: Architect, build, and debug complex multi-file applications. Complete production-ready code with zero placeholders.
- Deep Web Scraping & Browser Automation: Extract complex datasets into clean JSON/CSV formats and generate reports.
- Persistent Memory & Context Retention: Track long-term factual statements, user traits, preferences (Rohit prefers Hindi/Hinglish, full autonomous permissions granted).
- 24/7 Background Automation: Run continuous monitoring, client outreach, SEO publishing, and background daemons.

## 3. RESPONSE STRUCTURE
- Deliver high-signal, zero-fluff answers.
- Speak in confident, respectful, direct Hinglish/Hindi.
- Never write placeholder comments. Provide 100% complete, working solutions."""

conversation_history = {}

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if ALLOWED_USER_IDS and user_id not in ALLOWED_USER_IDS:
        await update.message.reply_text("Access restricted to authorized operator only.")
        return

    welcome_msg = (
        "🔥 **HERMES UNRESTRICTED SUPER-AGENT ONLINE** 🔥\n\n"
        "Namaste Rohit bhai! Hermes Super-Agent 100% autonomous mode me live hai.\n"
        "• **Mode:** Zero Restrictions | Autonomous Execution\n"
        "• **Brain:** Llama-3.3-70B Cloud Engine\n"
        "• **Uptime:** 24x7 Continuous Cloud Monitoring\n\n"
        "Hukum kijiye, kya execute karna hai?"
    )
    await update.message.reply_text(welcome_msg, parse_mode="Markdown")

async def status_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_msg = (
        "⚡ **HERMES SUPER-AGENT TELEMETRY:**\n"
        "• **Autonomous Mandate:** 100% Active\n"
        "• **Operator:** Rohit Kumar Nagar (Kota, RJ)\n"
        "• **Engine:** Groq Llama-3.3-70B Neural Core\n"
        "• **Execution:** Multi-step autonomous workflows ready"
    )
    await update.message.reply_text(status_msg, parse_mode="Markdown")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if ALLOWED_USER_IDS and user_id not in ALLOWED_USER_IDS:
        return

    user_text = update.message.text
    if not user_text:
        return

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    if user_id not in conversation_history:
        conversation_history[user_id] = [{"role": "system", "content": SYSTEM_PROMPT}]

    conversation_history[user_id].append({"role": "user", "content": user_text})
    if len(conversation_history[user_id]) > 15:
        conversation_history[user_id] = [conversation_history[user_id][0]] + conversation_history[user_id][-10:]

    try:
        response = await client.chat.completions.create(
            model=LLM_MODEL,
            messages=conversation_history[user_id],
            temperature=0.6,
            max_tokens=2500
        )
        reply = response.choices[0].message.content
        conversation_history[user_id].append({"role": "assistant", "content": reply})
        await update.message.reply_text(reply)
    except Exception as e:
        logger.error(f"Error: {e}")
        await update.message.reply_text(f"⚠️ Error: {str(e)}")

def main():
    if not TELEGRAM_BOT_TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN environment variable missing!")
        sys.exit(1)

    print("🚀 Hermes Super-Agent Daemon Running...")
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("status", status_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
