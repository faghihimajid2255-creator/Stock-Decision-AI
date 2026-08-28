"""
تنظیمات پروژهٔ سیستم تصمیم‌گیری خریدفروش هوشمند
Configuration for Stock Decision AI System
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ========== تنظیمات API ==========
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')  # هوش مصنوعی Groq
TSETMC_BASE_URL = 'https://service.tsetmc.com/api'  # بورس تهران
FINNHUB_API_KEY = os.getenv('FINNHUB_API_KEY', '')  # اخبار
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY', '')  # اخبار جهانی

# ========== تنظیمات داده‌بیس ==========
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///stock_decision.db')

# ========== تنظیمات Dashboard ==========
FLASK_PORT = 5000
FLASK_DEBUG = True
DASHBOARD_REFRESH_INTERVAL = 30  # ثانیه

# ========== تنظیمات تحلیل ==========
MIN_VOLUME = 1000000  # حداقل حجم معامله
MIN_PRICE_CHANGE = 2  # حداقل درصد تغییر قیمت
LIQUIDITY_THRESHOLD = 50000000000  # آستانهٔ نقدینگی

# ========== تنظیمات سیگنال‌های خریدفروش ==========
BUY_SIGNALS = {
    'min_smart_money_inflow': 5000000000,  # حداقل جریان پول هوشمند
    'min_technical_score': 70,  # حداقل امتیاز تکنیکالی
    'support_level_proximity': 2,  # درصد فاصله از سطح حمایت
    'volume_spike_multiplier': 1.5,  # ضریب افزایش حجم
}

SELL_SIGNALS = {
    'correction_percentage': 5,  # درصد اصلاح
    'resistance_proximity': 2,  # درصد فاصله از سطح مقاومت
    'smart_money_outflow': 3000000000,  # خروج پول هوشمند
    'price_above_ma200': True,  # قیمت بالای میانگین 200 روزه
}

# ========== تنظیمات نظارت اخبار ==========
NEWS_SOURCES = [
    'https://www.tsetmc.com',
    'https://news.ir',
    'https://www.reuters.com',
]
NEWS_CHECK_INTERVAL = 3600  # هر ساعت

# ========== تنظیمات هشدارها ==========
ALERT_CHANNELS = {
    'console': True,
    'email': False,
    'telegram': False,
    'webhook': False,
}

# ========== تنظیمات زمان ==========
MARKET_OPEN_TIME = '09:00'  # 9 صبح (وقت تهران)
MARKET_CLOSE_TIME = '15:30'  # 3:30 بعدازظهر
TIMEZONE = 'Asia/Tehran'

# ========== تنظیمات AI ==========
AI_MODEL = 'groq-mixtral'  # مدل هوش مصنوعی
AI_TEMPERATURE = 0.3  # دمای مدل (کمتر = دقیق‌تر)
AI_MAX_TOKENS = 2000  # حداکثر توکن

# ========== تنظیمات لاگ ==========
LOG_LEVEL = 'INFO'
LOG_FILE = 'logs/stock_decision.log'

# ========== تنظیمات کش ==========
CACHE_ENABLED = True
CACHE_TTL = 300  # ثانیه

# ========== تنظیمات بیک‌آپ ==========
AUTO_BACKUP = True
BACKUP_INTERVAL = 86400  # روزانه
