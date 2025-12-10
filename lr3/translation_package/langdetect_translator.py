# translation_package/langdetect_translator.py

from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs, LangDetectException

def TransLate(text: str, scr: str, dest: str) -> str:
    """Перекладає текст на задану мову."""
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        result = translator.translate(text)
        return result
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    """Визначає мову за допомогою langdetect."""
    try:
        if set == "lang":
            return detect(text)
        elif set == "confidence":
            # detect_langs повертає список об'єктів з мовою та впевненістю
            result = detect_langs(text)
            if result:
                return str(result[0].prob)  # Повертаємо найвищу впевненість
            return "Не вдалося визначити"
        elif set == "all":
            result = detect_langs(text)
            if result:
                best = result[0]
                return f"Мова: {best.lang}, Confidence: {best.prob}"
            return "Не вдалося визначити"
        else:
            return "Невірний параметр set"
    except LangDetectException as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang: str) -> str:
    """Конвертує між кодом та назвою мови."""
    languages = {
        'en': 'english', 'english': 'en',
        'uk': 'ukrainian', 'ukrainian': 'uk',
        'fr': 'french', 'french': 'fr',
        'de': 'german', 'german': 'de',
        'es': 'spanish', 'spanish': 'es',
        'ru': 'russian', 'russian': 'ru'
    }
    lang_lower = lang.lower()
    return languages.get(lang_lower, f"Мову '{lang}' не знайдено.")

def LanguageList(out: str = "screen", text: str = None) -> str:
    """Виводить список мов."""
    try:
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
            filename = "langdetect_languages_list.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"Таблицю збережено у файл: {filename}")
        else:
            return "Невірний параметр out"

        return "Ok"
    except Exception as e:
        return f"Помилка у LanguageList: {e}"