import pandas as pd
import matplotlib.pyplot as plt

# загрузка
df = pd.read_csv("results.csv")

# базовая очистка
df["delay"] = pd.to_numeric(df["delay"], errors="coerce")

# статистика
total = len(df)
avg_delay = df["delay"].mean()

print("Всего сообщений:", total)
print("Средняя задержка:", avg_delay)

# если ты вручную заполнишь received/spam:
if "received" in df.columns:
    received_rate = (df["received"] == "yes").mean()
    print("Delivery rate:", received_rate)

# 📈 график задержек
plt.figure()
plt.plot(df["delay"])
plt.title("Задержка отправки сообщений")
plt.xlabel("Номер сообщения")
plt.ylabel("Секунды")
plt.grid()

plt.savefig("delay_plot.png")
plt.show()