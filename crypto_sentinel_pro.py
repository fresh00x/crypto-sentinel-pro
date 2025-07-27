crypto_sentinel_pro.py

import os import logging import requests from datetime import datetime from apscheduler.schedulers.background import BackgroundScheduler from telegram import Bot from dotenv import load_dotenv

load_dotenv()

Env variables

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN") TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_TOKEN)

logging.basicConfig(level=logging.INFO) scheduler = BackgroundScheduler()

FAVORITES = ["bitcoin", "ethereum", "pepe", "solana", "cardano", "sui", "tether-gold"]

Dummy data fetch function (replace with real API calls)

def fetch_crypto_data(): # Here you can plug into CoinGecko, CoinMarketCap, LunarCrush, etc. return { "bitcoin": {"price": 30200, "volume": 1000000000, "change": 1.5}, "pepe": {"price": 0.00000123, "volume": 90000000, "change": 20.1}, # ... add more }

def analyze_market(): try: data = fetch_crypto_data() anomalies = [] for coin, stats in data.items(): if abs(stats['change']) > 10: anomalies.append(f"🚨 {coin.upper()} bouge fortement: {stats['change']}%")

if anomalies:
        message = "\n".join(anomalies)
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
except Exception as e:
    logging.error(f"Erreur analyse marché: {e}")

def daily_report(): try: message = f"📊 Rapport quotidien - {datetime.now().strftime('%Y-%m-%d')}\n" data = fetch_crypto_data() for fav in FAVORITES: if fav in data: d = data[fav] message += f"{fav.upper()}: ${d['price']} | Vol: {d['volume']} | Δ: {d['change']}%\n" bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message) except Exception as e: logging.error(f"Erreur rapport quotidien: {e}")

Schedule

scheduler.add_job(daily_report, 'cron', hour=5, minute=0) scheduler.add_job(analyze_market, 'interval', minutes=15) scheduler.start()

logging.info("Crypto Sentinel Pro en marche ✅")

Keep alive

import time while True: time.sleep(60)

