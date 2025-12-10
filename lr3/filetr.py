import json
import os
import sys
from pathlib import Path

def analyze_text(text):
    chars = len(text)
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')
    return chars, words, sentences

def load_module(module_name):
    try:
        if module_name == "google_translator_v4":
            from translation_package.google_translator_v4 import TransLate, LangDetect
        elif module_name == "deep_translator_module":
            from translation_package.deep_translator_module import TransLate, LangDetect
        elif module_name == "langdetect_translator":
            from translation_package.langdetect_translator import TransLate, LangDetect
        else:
            raise ValueError(f"Невідомий модуль: {module_name}")
        return TransLate, LangDetect
    except ImportError as e:
        print(f"Помилка завантаження модуля {module_name}: {e}")
        sys.exit(1)

def main():
    print("=== Програма перекладу файлів ===\n")
    
    config_file = "config.json"
    if not os.path.exists(config_file):
        print(f"Помилка: Файл конфігурації '{config_file}' не знайдено.")
        return
    
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    input_file = config.get("input_file", "")
    target_lang = config.get("target_language", "en")
    module_name = config.get("translation_module", "google_translator_v4")
    output_dest = config.get("output_destination", "screen")
    max_chars = config.get("max_chars", 600)
    max_words = config.get("max_words", 100)
    max_sentences = config.get("max_sentences", 5)

    if not os.path.exists(input_file):
        print(f"Помилка: Вхідний файл '{input_file}' не знайдено.")
        return
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            full_text = f.read()
        
        total_chars, total_words, total_sentences = analyze_text(full_text)
        
        print("I. Аналіз файлу:")
        print(f"   Назва файлу: {input_file}")
        print(f"   Розмір файлу: {os.path.getsize(input_file)} байт")
        print(f"   Кількість символів: {total_chars}")
        print(f"   Кількість слів: {total_words}")
        print(f"   Кількість речень: {total_sentences}")
        
        from translation_package.google_translator_v4 import LangDetect
        lang_result = LangDetect(full_text[:100], "lang")
        print(f"   Мова тексту: {lang_result}")
        print()
        
        print("II. Зчитування тексту з обмеженнями:")
        text_to_translate = ""
        chars_count = 0
        words_count = 0
        sentences_count = 0
        
        for char in full_text:
            text_to_translate += char
            chars_count += 1
            
            if chars_count >= max_chars:
                print(f"   Досягнуто обмеження символів ({max_chars})")
                break
            
            if char in '.!?':
                sentences_count += 1
                if sentences_count >= max_sentences:
                    print(f"   Досягнуто обмеження речень ({max_sentences})")
                    break
        
        words = text_to_translate.split()
        if len(words) >= max_words:
            text_to_translate = ' '.join(words[:max_words])
            print(f"   Досягнуто обмеження слів ({max_words})")
        
        print(f"   Зчитано символів: {len(text_to_translate)}")
        print(f"   Зчитано слів: {len(text_to_translate.split())}")
        print(f"   Зчитано речень: {text_to_translate.count('.') + text_to_translate.count('!') + text_to_translate.count('?')}")
        print()
        
        TransLateFunc, _ = load_module(module_name)
        
        print("III. Виконання перекладу...")
        translated_text = TransLateFunc(text_to_translate, "auto", target_lang)
        
        print(f"\nIV. Результат перекладу:")
        print(f"   Модуль: {module_name}")
        print(f"   Цільова мова: {target_lang}")
        
        if output_dest == "screen":
            print(f"   Перекладений текст:\n---\n{translated_text}\n---")
        elif output_dest == "file":
            input_path = Path(input_file)
            output_filename = f"{input_path.stem}_{target_lang}{input_path.suffix}"
            
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(translated_text)
            
            print(f"   Переклад збережено у файл: {output_filename}")
            print("   Статус: Ok")
        else:
            print(f"   Невірний параметр виводу: {output_dest}")
    
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()