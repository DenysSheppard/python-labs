# translation_package/deep_translator_module.py

import sys
from deep_translator import GoogleTranslator, single_detection
from deep_translator.exceptions import NotValidPayload, TranslationNotFound

# Перевірка версії Python
if sys.version_info >= (3, 13):
    print("Увага: Цей модуль розроблено для версій Python < 3.13. Можлива несумісність.")

def TransLate(text: str, scr: str, dest: str) -> str:
    """Перекладає текст на задану мову."""
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        result = translator.translate(text)
        return result
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    """
    Для deep-translator потрібен API-ключ для визначення мови.
    Якщо ключ відсутній, повертаємо помилку.
    """
    try:
        # У цій версії deep-translator потрібен API-ключ для single_detection
        # Якщо ключа немає, можна використати переклад з auto для визначення
        if set == "lang":
            # Спрощений підхід: перекладаємо на англійську та дивимось source
            translator = GoogleTranslator(source='auto', target='en')
            # У deep-translator немає прямого доступу до визначеної мови після перекладу
            # Тому повертаємо заглушку
            return "auto"  # На жаль, deep-translator не повертає визначену мову
        elif set in ("confidence", "all"):
            return "Для deep-translator потрібен API-ключ для визначення мови."
        else:
            return "Невірний параметр set"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang: str) -> str:
    """Спрощена реалізація, оскільки deep-translator має обмежений список мов."""
    # Словник основних мов для deep-translator
    languages = {
        'english': 'en', 'en': 'english',
        'ukrainian': 'uk', 'uk': 'ukrainian',
        'french': 'fr', 'fr': 'french',
        'german': 'de', 'de': 'german',
        'spanish': 'es', 'es': 'spanish',
        'russian': 'ru', 'ru': 'russian'
    }
    lang_lower = lang.lower()
    if lang_lower in languages:
        return languages[lang_lower]
    return f"Мову '{lang}' не знайдено в словнику."

def LanguageList(out: str = "screen", text: str = None) -> str:
    """Виводить список підтримуваних мов."""
    try:
        # Отримуємо список мов з GoogleTranslator
        langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
        lines = []
        lines.append(f"{'N':<4} {'Код':<8} {'Мова':<25} {'Переклад':<30}")
        lines.append("-" * 75)

        for i, (code, name) in enumerate(langs_dict.items(), 1):
            translation = ""
            if text:
                try:
                    translation = TransLate(text, "auto", code)
                except:
                    translation = "[помилка]"
            lines.append(f"{i:<4} {code:<8} {name:<25} {translation:<30}")

        result = "\n".join(lines)

        if out == "screen":
            print(result)
        elif out == "file":
            filename = "deep_languages_list.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"Таблицю збережено у файл: {filename}")
        else:
            return "Невірний параметр out"

        return "Ok"
    except Exception as e:
        return f"Помилка у LanguageList: {e}"