from translation_package.langdetect_translator import (
    TransLate, LangDetect, CodeLang, LanguageList
)

def main():
    print("=== Демонстрація модуля з langdetect ===\n")
    
    print("1. Тестування TransLate:")
    text = "How are you?"
    translation = TransLate(text, "auto", "es")
    print(f"   '{text}' -> '{translation}'\n")
    
    print("2. Тестування LangDetect з langdetect:")
    test_texts = [
        "This is English text",
        "Це український текст",
        "Ceci est un texte français"
    ]
    for txt in test_texts:
        result = LangDetect(txt, "all")
        print(f"   '{txt[:20]}...' -> {result}")
    print()
    
    print("3. Тестування CodeLang:")
    print(f"   'english' -> '{CodeLang('english')}'")
    print(f"   'uk' -> '{CodeLang('uk')}'")
    print()
    
    print("4. Тестування LanguageList:")
    result = LanguageList("screen", "Thank you")
    print(f"   Результат: {result}")

if __name__ == "__main__":
    main()