LANGUAGES = {
    'ru': 'Русский',
    'en': 'Английский',
    'uz': 'Узбекский',
    'fr': 'Французкий',
    'zh-cn': 'Китайский',
    'de': 'Немецкий'
}

# Функция для получения ключа по значению
def get_key(lang):
    for k, v in LANGUAGES.items():
        if lang == v:
            return k