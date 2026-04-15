from twilio.rest import Client
import time
import csv
import random
from datetime import datetime

# 🔐 Данные Twilio
ACCOUNT_SID = "your_sid"
AUTH_TOKEN = "your_token"
FROM_NUMBER = "+1234567890"
TO_NUMBER = "+336XXXXXXXX"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# ⚙️ Настройки теста
TOTAL_MESSAGES = 30
BASE_DELAY = 2  # базовая задержка

# 🧠 Генератор сообщений
def generate_message(i):
    msg_type = random.choice(["otp", "alert", "duplicate"])
    
    if msg_type == "otp":
        text = f"Your code is {random.randint(1000,9999)}"
    elif msg_type == "alert":
        text = f"Welcome! Test message #{i}"
    else:
        text = "Your code is 1234"  # дубликат
    
    return text, msg_type

# 📝 Запись в CSV
def log_to_csv(row):
    with open("results.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)

def send_test():
    for i in range(TOTAL_MESSAGES):
        text, msg_type = generate_message(i)

        timestamp = datetime.now().isoformat()

        try:
            start = time.time()

            message = client.messages.create(
                body=text,
                from_=FROM_NUMBER,
                to=TO_NUMBER
            )

            delay = time.time() - start

            print(f"[{i+1}] Sent: {text}")

            log_to_csv([
                timestamp,
                text,
                msg_type,
                delay,
                "unknown",  # вручную потом отметишь (пришло/нет)
                "unknown"
            ])

        except Exception as e:
            print("Error:", e)

        # 🔀 динамическая нагрузка
        sleep_time = BASE_DELAY / random.uniform(0.5, 2)
        time.sleep(sleep_time)

if __name__ == "__main__":
    # заголовок CSV (один раз)
    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "timestamp", "message", "type", "delay", "received", "spam"
        ])

    send_test()