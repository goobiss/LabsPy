from module.my_module2 import LangDetect, TransLate, CodeLang, LanguageList
from module.my_module2 import Style

def main():
    # Вхідні дані
    text = "Привіт як життя мої друзі?"
    src_language = "uk"
    dest_language = "en"
    detection_set = "all"
    output_method = "screen"  # Можна змінити на 'txt' для збереження у файл

    try:
        # Виявлення мови
        detection_result = LangDetect(text, set=detection_set)
        print(f"Результат виявлення мови: {detection_result}")

        # Переклад тексту
        translated_text = TransLate(text, src=src_language, dest=dest_language)
        print(f"Перекладений текст: {translated_text}")

        # Отримання коду мови
        language_code = CodeLang(src_language)
        print(f"Код мови: {language_code}")

        # Виведення результатів
        LanguageList(output_method, text)
        print(Style.RESET_ALL)

    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == '__main__':
    main()
