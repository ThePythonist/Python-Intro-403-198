banks = {
    "mellat": {
        "name": "ملت",
        "symbol": "وبملت",
        "industry": "مالی",
        "shareholders": [
            {"دولت جمهوری اسلامی ایران": 11.16},
            {"سرمایه گذاری ‌های استانی": 11.16},
            {"شرکت گروه مالی ملت (سهامی عام)": 5.73},
            {"صندوق تامین آتیه کارکنان بانک ملت": 2.85},
        ],
        "subsidiaries": ["بانکداری ایران", "فرهنگی ورزشی پرسپولیس"],
    },
    "pasargad": {},
    "saman": {},
}

# print(banks["pasargad"])
# print(banks["mellat"])
print(banks["mellat"]["shareholders"][0])
print(banks["mellat"]["shareholders"][1])
print(banks["mellat"]["shareholders"][2])
print(banks["mellat"]["shareholders"][3])
