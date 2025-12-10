# translation_package/google_translator_v4.py
# Виправлена версія для googletrans 4.0.2 (асинхронний API)

import asyncio
from googletrans import Translator, LANGUAGES, LANGCODES

# --- Головні синхронні функції, які імпортуються ---
def TransLate(text: str, scr: str, dest: str) -> str:
    """Перекладає текст на задану мову."""
    return asyncio.run(_translate_async(text, scr, dest))

def LangDetect(text: str, set: str = "all") -> str:
    """Визначає мову та коефіцієнт довіри."""
    return asyncio.run(_detect_async(text, set))

# Допоміжні асинхронні функції
async def _translate_async(text: str, scr: str, dest: str) -> str:
    """Асинхронна функція для перекладу."""
    try:
        async with Translator() as translator:
            result = await translator.translate(text, src=scr, dest=dest)
            return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

async def _detect_async(text: str, set: str) -> str:
    """Асинхронна функція для визначення мови."""
    try:
        async with Translator() as translator:
            detection = await translator.detect(text)
            
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        elif set == "all":
            return f"Мова: {detection.lang}, Confidence: {detection.confidence}"
        else:
            return "Невірний параметр set."
    except Exception as e:
        return f"Помилка визначення мови: {e}"

# --- Решта функцій залишаються синхронними (не вимагають правок) ---
def CodeLang(lang: str) -> str:
    """Конвертує між кодом та назвою мови."""
    lang_lower = lang.lower()
    if len(lang_lower) in (2, 3):  # Якщо це код
        return LANGUAGES.get(lang_lower, f"Код '{lang}' не знайдено.")
    else:  # Якщо це назва
        # Шукаємо код за назвою
        for code, name in LANGUAGES.items():
            if name.lower() == lang_lower:
                return code
        # Перевіряємо додаткові відображення
        if lang_lower in LANGCODES:
            return LANGCODES[lang_lower]
        return f"Мову '{lang}' не знайдено."

def LanguageList(out: str = "screen", text: str = None) -> str:
    """Виводить таблицю мов. Для перекладу використовує TransLate."""
    try:
        lines = []
        lines.append(f"{'N':<4} {'ISO-639':<8} {'Мова':<25} {'Переклад':<30}")
        lines.append("-" * 75)

        for i, (code, name) in enumerate(list(LANGUAGES.items())[:30], 1):  # Перші 30 мов для швидкості
            translation = ""
            if text:
                translation = TransLate(text, "auto", code)  # Використовуємо нашу головну функцію
            lines.append(f"{i:<4} {code:<8} {name:<25} {translation:<30}")

        result = "\n".join(lines)

        if out == "screen":
            print(result)
        elif out == "file":
            filename = "languages_list.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"Таблицю збережено у файл: {filename}")
        else:
            return "Невірний параметр 'out'."
        return "Ok"
    except Exception as e:
        return f"Помилка у LanguageList: {e}"