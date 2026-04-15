# TWIspam
нагрузочный тест "SpamSmS"
🧪 Как проводить тест
1. Запускаешь отправку
python sender.py
2. На телефоне вручную отмечаешь в CSV:
received: yes / no  
spam: yes / no  
3. Анализируешь python analyzer.py
4. 📱 Что нужно перед началом - Зарегистрироваться в Twilio Получить :ACCOUNT_SID AUTH_TOKEN номер Twilio (отправитель)
5. Установить библиотеку:

   pip install twilio
