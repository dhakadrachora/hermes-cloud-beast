# ⚡ Hermes Agent 24x7 Cloud Deployment

Deploy your 24x7 autonomous Hermes Agent with Groq (Llama-3.3-70B) & Telegram Bot on Railway or Render for 100% FREE!

## 🚀 1-Click Deployment Steps:

### 1. Push this folder to your GitHub:
```bash
git init
git add .
git commit -m "Deploy 24x7 Hermes Cloud Agent"
git branch -M main
git remote add origin https://github.com/dhakadrachora/hermes-cloud-agent.git
git push -u origin main
```

### 2. Deploy on Railway.app / Render.com:
1. Open [Railway.app](https://railway.app) or [Render.com](https://render.com)
2. Click **New Project** -> **Deploy from GitHub repo** -> Select `hermes-cloud-agent`
3. Add Environment Variables:
   - `LLM_PROVIDER`: `openai`
   - `LLM_API_BASE`: `https://api.groq.com/openai/v1`
   - `LLM_MODEL`: `llama-3.3-70b-versatile`
   - `LLM_API_KEY`: *(Your Groq API key from console.groq.com)*
   - `TELEGRAM_BOT_TOKEN`: *(Your Telegram Bot Token)*
   - `ALLOWED_USER_IDS`: `8332012112`
4. Click **Deploy**!

That's it! Your bot is live 24x7 on the cloud with zero laptop battery drain.
