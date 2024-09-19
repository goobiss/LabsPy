from module.my_module1 import LangDetect, TransLate, CodeLang, LanguageList
from module.my_module1 import Fore, Style

def main():
    # Вхідні дані
    text = "Як життя друзі?"
    src_language = "uk"
    dest_language = "fr"  # Вкажіть мову призначення
    detection_set = "all"
    output_method = "txt"  # Можна змінити на 'screen' для виведення на екран

    try:
        # Виявлення мови
        detection_result = LangDetect(text, set=detection_set)
        print(Fore.RED + f"Результат виявлення мови: {detection_result}")

        # Переклад тексту
        if dest_language:
            translated_text = TransLate(text, src=src_language, dest=dest_language)
            print(Fore.GREEN + f"Перекладений текст: {translated_text}")
        else:
            print(Fore.YELLOW + "Мова призначення не вказана.")

        # Отримання коду мови
        language_code = CodeLang(src_language)
        print(Fore.BLUE + f"Код мови: {language_code}")

        # Виведення результатів
        if output_method == "txt":
            LanguageList(output_method, text)
            print("Результат збережено у файл.")
        elif output_method == "screen":
            LanguageList(output_method, text)
            print("Результат виведено на екран.")
        else:
            print(Fore.RED + "Невідомий метод виведення.")

        print(Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")
        print(Style.RESET_ALL)

if __name__ == '__main__':
    main()
