import sys
print(f"Версія Python: {sys.version}")

from translation_package.deep_translator_module import (
    TransLate, CodeLang, LanguageList
)

def main():
    print("\n=== Демонстрація модуля Deep Translator ===\n")

    print("1. Тестування TransLate:")
    text = "Good morning"
    translation = TransLate(text, "auto", "fr")
    print(f"   '{text}' -> '{translation}'\n")
    
    print("2. Тестування CodeLang:")
    tests = ["english", "fr", "German"]
    for test in tests:
        result = CodeLang(test)
        print(f"   '{test}' -> '{result}'")
    print()
    
    print("3. Тестування LanguageList (скорочений список на екрані):")
    result = LanguageList("screen", "Hello")
    print(f"   Результат: {result}")

if __name__ == "__main__":
    main()