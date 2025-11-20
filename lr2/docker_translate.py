from googletrans import Translator, LANGUAGES

try:
    from googletrans import LANGCODES
except ImportError:
    LANGCODES = {v.lower(): k for k, v in LANGUAGES.items()}

def TransLate(text: str, lang: str) -> str:
    translator = Translator()
    lang = lang.lower().strip()
    dest_code = None

    if lang in LANGUAGES:
        dest_code = lang
    elif lang in LANGCODES:
        dest_code = LANGCODES[lang]
    else:
        for code, name in LANGUAGES.items():
            if name.lower() == lang:
                dest_code = code
                break
    
    if dest_code is None:
        dest_code = lang 

    try:
        translation = translator.translate(text, dest=dest_code)
        return translation.text
    except Exception as e:
        return f"Docker Error: {e} (Target code was: {dest_code})"

def LangDetect(txt: str) -> str:
    translator = Translator()
    try:
        detection = translator.detect(txt)
        return f"Detected(lang={detection.lang}, confidence={detection.confidence})"
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str) -> str:
    lang = lang.lower().strip()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    try:
        from googletrans import LANGCODES
        if lang in LANGCODES:
            return LANGCODES[lang]
    except:
        pass
        
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return "Not Found"

if __name__ == "__main__":
    print("--- ЗАПУСК В КОНТЕЙНЕРІ (v3.1.0a0) ---")
    
    try:
        user_text = input("Docker Input Text: ").strip()
        user_lang = input("Docker Input Lang: ").strip()

        print(f"\n[Docker] Detected: {LangDetect(user_text)}")
        print(f"[Docker] Translated: {TransLate(user_text, user_lang)}")
        
    except EOFError:
        print("Помилка: Запустіть контейнер з прапорцем -it")
    except Exception as e:
        print(f"System Error: {e}")