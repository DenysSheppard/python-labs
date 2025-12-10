import sys
sys.path.append('.')

from translation_package.google_translator_v4 import (
    TransLate, LangDetect, CodeLang, LanguageList
)

def main():
    print("=== Демонстрація модуля GoogleTrans ===\n")

    print("1. Тестування TransLate:")
    text = "Hello, world!"
    translation = TransLate(text, "en", "uk")
    print(f"   '{text}' -> '{translation}'\n")
    
    print("2. Тестування LangDetect:")
    for text in ["Hello world", "Привіт світ", "Bonjour le monde"]:
        result = LangDetect(text, "all")
        print(f"   '{text}' -> {result}")
    print()
    
    print("3. Тестування CodeLang:")
    tests = ["english", "uk", "French", "es"]
    for test in tests:
        result = CodeLang(test)
        print(f"   '{test}' -> '{result}'")
    print()
    
    print("4. Тестування LanguageList (екран):")
    result = LanguageList("screen", "Good morning")
    print(f"   Результат: {result}")
    
    print("\n5. Тестування LanguageList (файл):")
    result = LanguageList("file", "Good night")
    print(f"   Результат: {result}")

if __name__ == "__main__":
    main()