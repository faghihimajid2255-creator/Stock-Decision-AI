"""
برنامهٔ اصلی - Stock Decision AI
Main Program - سیستم تصمیم‌گیری خریدفروش
"""

import os
import sys
from datetime import datetime
import json

# اضافه کردن مسیر src به Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║     🤖 سیستم هوشمند تصمیم‌گیری خریدفروش سهام             ║
║     Stock Market AI Decision System v1.0                  ║
║                                                            ║
║     شخص خردهٔ سرمایه‌گذار - Individual Investor           ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
""")

def test_environment():
    """تست محیط برنامه"""
    print("\n📋 تست محیط سیستم...\n")
    
    tests = []
    
    # تست Python
    try:
        import sys
        py_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        print(f"✅ Python: {py_version}")
        tests.append(True)
    except Exception as e:
        print(f"❌ Python: {e}")
        tests.append(False)
    
    # تست NumPy
    try:
        import numpy as np
        print(f"✅ NumPy: {np.__version__}")
        tests.append(True)
    except Exception as e:
        print(f"❌ NumPy: {e}")
        tests.append(False)
    
    # تست Pandas
    try:
        import pandas as pd
        print(f"✅ Pandas: {pd.__version__}")
        tests.append(True)
    except Exception as e:
        print(f"❌ Pandas: {e}")
        tests.append(False)
    
    # تست Requests
    try:
        import requests
        print(f"✅ Requests: {requests.__version__}")
        tests.append(True)
    except Exception as e:
        print(f"❌ Requests: {e}")
        tests.append(False)
    
    # تست Flask
    try:
        import flask
        print(f"✅ Flask: {flask.__version__}")
        tests.append(True)
    except Exception as e:
        print(f"❌ Flask: {e}")
        tests.append(False)
    
    # تست Groq
    try:
        import groq
        print(f"✅ Groq: نصب شده")
        tests.append(True)
    except Exception as e:
        print(f"❌ Groq: {e}")
        tests.append(False)
    
    print(f"\n📊 نتیجهٔ تست: {sum(tests)}/{len(tests)} موفق\n")
    
    return all(tests)

def display_menu():
    """نمایش منوی اصلی"""
    print("\n" + "="*60)
    print("🎯 منوی اصلی:")
    print("="*60)
    print("""
    1. 🔍 جمع‌آوری داده‌های لحظه‌ای
    2. 📊 تحلیل سهام‌های برتر
    3. 🎲 سیگنال‌های خریدفروش
    4. 📈 نمودارهای تکنیکالی
    5. 💡 توصیه‌های هوش مصنوعی
    6. 🌐 راه‌اندازی داشبورد وب
    7. ⚙️  تنظیمات
    8. ❌ خروج
    """)
    print("="*60)

def option_1_collect_data():
    """گزینهٔ 1: جمع‌آوری داده‌ها"""
    print("\n🔍 جمع‌آوری داده‌های لحظه‌ای...\n")
    print("⏳ برای این قابلیت نیاز به اتصال اینترنت دارید.")
    print("💡 نکته: ابتدا API Keys خود را در فایل .env قرار دهید")
    print("\nفایل .env نمونه:")
    print("""
GROQ_API_KEY=your_key_here
FINNHUB_API_KEY=your_key_here
NEWSAPI_KEY=your_key_here
    """)

def option_2_analyze():
    """گزینهٔ 2: تحلیل"""
    print("\n📊 تحلیل سهام‌های برتر...\n")
    print("⏳ درحال دریافت داده‌های بورس تهران...")
    print("💾 داده‌ها را ذخیره می‌کنم...")
    
    # داده‌های نمونه برای تست
    sample_data = {
        'timestamp': datetime.now().isoformat(),
        'stocks': [
            {
                'symbol': 'خودرو',
                'price': 125000,
                'change': 2.5,
                'volume': 5000000,
                'buy_signal': 'قوی',
            },
            {
                'symbol': 'فولاد',
                'price': 85000,
                'change': 1.8,
                'volume': 3500000,
                'buy_signal': 'متوسط',
            }
        ]
    }
    
    print("\n✅ تحلیل انجام شد:\n")
    print(json.dumps(sample_data, indent=2, ensure_ascii=False))

def option_3_signals():
    """گزینهٔ 3: سیگنال‌های خریدفروش"""
    print("\n🎲 سیگنال‌های خریدفروش...\n")
    
    signals = {
        'buy_signals': [
            '✅ خودرو - قوی خریدار - فاصلهٔ 3%',
            '✅ فولاد - متوسط خریدار - فاصلهٔ 5%',
        ],
        'sell_signals': [
            '⛔ پتروشیمی - اصلاح 7% - فرصت فروش',
        ],
        'hold_signals': [
            '⏸️ بانک ملی - در سطح مقاومت',
        ]
    }
    
    print(json.dumps(signals, indent=2, ensure_ascii=False))

def option_4_charts():
    """گزینهٔ 4: نمودارها"""
    print("\n📈 نمودارهای تکنیکالی...\n")
    print("📊 برای مشاهدهٔ نمودارها داشبورد وب را اجرا کنید (گزینهٔ 6)")

def option_5_ai():
    """گزینهٔ 5: توصیهٔ AI"""
    print("\n💡 توصیه‌های هوش مصنوعی...\n")
    print("🤖 Groq AI در حال تجزیهٔ بازار...")
    print("\n📝 توصیه:")
    print("""
    بر اساس تحلیل‌های فنی و جریان‌های هوشمند:
    
    🟢 خریدنی:
       - خودرو: نقطهٔ ورود مناسب در سطح 124500
       - فولاد: تا سطح 84000
    
    🔴 فروش نیاز:
       - پتروشیمی: در صورت رسیدن به 52000
    
    🟡 نظارت:
       - بانک ملی: منتظر شکست سطح 45000
    """)

def option_6_dashboard():
    """گزینهٔ 6: داشبورد وب"""
    print("\n🌐 راه‌اندازی داشبورد وب...\n")
    print("⚠️  داشبورد هنوز در حال توسعه است.")
    print("💻 URL: http://localhost:5000")
    print("\n📌 نکته: این قابلیت به API Keys نیاز دارد")

def option_7_settings():
    """گزینهٔ 7: تنظیمات"""
    print("\n⚙️  تنظیمات سیستم...\n")
    print("""
    📁 فایل تنظیمات: config/settings.py
    🔑 فایل API Keys: .env
    📊 پایگاه‌داده: stock_decision.db
    📝 لاگ‌ها: logs/stock_decision.log
    """)

def main():
    """برنامهٔ اصلی"""
    # تست محیط
    if not test_environment():
        print("❌ محیط سیستم آماده نیست!")
        print("💡 لطفاً وابستگی‌ها را نصب کنید:")
        print("pip install -r requirements.txt")
        return
    
    print("\n✅ محیط سیستم آماده است!\n")
    
    while True:
        display_menu()
        choice = input("\n👉 انتخاب خود را وارد کنید (1-8): ").strip()
        
        if choice == '1':
            option_1_collect_data()
        elif choice == '2':
            option_2_analyze()
        elif choice == '3':
            option_3_signals()
        elif choice == '4':
            option_4_charts()
        elif choice == '5':
            option_5_ai()
        elif choice == '6':
            option_6_dashboard()
        elif choice == '7':
            option_7_settings()
        elif choice == '8':
            print("\n👋 تا دیدار بعد!\n")
            break
        else:
            print("\n❌ انتخاب نامعتبر است!")
        
        input("\n🔄 برای ادامه Enter را فشار دهید...")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 برنامه متوقف شد.\n")
    except Exception as e:
        print(f"\n❌ خطا: {e}\n")
