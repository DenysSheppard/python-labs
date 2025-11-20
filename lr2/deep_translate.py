from googletrans import Translator, LANGUAGES

def TransLate(text: str, lang: str) -> str:
    translator = Translator()
    lang = lang.lower().strip()
    dest_code = lang
    
    if lang not in LANGUAGES:
        for code, name in LANGUAGES.items():
            if name.lower() == lang:
                dest_code = code
                break
    
    try:
        translation = translator.translate(text, dest=dest_code)
        return translation.text
    except Exception as e:
        return f"Error: {e}"

def LangDetect(txt: str) -> str:
    translator = Translator()
    try:
        detection = translator.detect(txt)
        return f"Detected: {detection.lang} (confidence: {detection.confidence})"
    except Exception as e:
        return f"Detection Error: {e}"

def CodeLang(lang: str) -> str:
    lang = lang.lower().strip()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return "Unknown Language"

if __name__ == "__main__":
    print("--- ЛОКАЛЬНИЙ ЗАПУСК (Latest Version) ---")
    
    try:
        user_text = input("Введіть текст: ").strip()
        user_lang = input("Введіть мову: ").strip()

        print(f"\n[Local] Визначено мову: {LangDetect(user_text)}")
        print(f"[Local] Переклад: {TransLate(user_text, user_lang)}")
        print(f"[Local] Код мови: {CodeLang(user_lang)}")
        
    except Exception as e:
        print(f"Помилка: {e}")