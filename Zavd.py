from googletrans import Translator, LANGUAGES

translator = Translator()


def TransLate(text: str, scr: str, dest: str) -> str:
    """
    Функція повертає текст перекладений на задану мову, або повідомлення про помилку.
    text – текст, який необхідно перекласти;
    scr – назва або код мови заданого тексту, відповідно до стандарту ISO-639,
    або значення ‘auto’;
    dest – назва або код мови на яку необхідно перевести заданий текст,
    відповідно до стандарту ISO-639
    """
    try:
        translation = translator.translate(text, src=scr, dest=dest)
        return translation.text
    except Exception as e:
        return f"Error: {e}"


def LangDetect(text: str, set: str = "all") -> str:
    """
    Функція визначає мову та коефіцієнт довіри для заданого тексту,
    або повертає повідомлення про помилку.
    text – текст для якого потрібно визначити мову та коефіцієнт довіри;
    set = “lang” – функція повертає тільки мову тексту
    set = “confidence” – функція повертає тільки коефіцієнт довіри
    set = “all” (по замовченню) – функція повертає мову і коефіцієнт довіри
    """
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"{detection.lang}, {detection.confidence}"
    except Exception as e:
        return f"Error: {e}"


def CodeLang(lang: str) -> str:
    """
    Функція повертає код мови (відповідно до таблиці), якщо в параметрі lang міститься назва
    мови, або повертає назву мови, якщо в параметрі lang міститься її код,
    або повідомлення про помилку
    lang – назва або код мови
    """
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang]
    elif lang in LANGUAGES.values():
        for key, value in LANGUAGES.items():
            if value == lang:
                return key
    else:
        return "Error: Invalid language or code."


def LanguageList(out: str = "screen", text: str = None) -> str:
    """
    Виводить в файл або на екран таблицю всіх мов, що підтримуються, та їх кодів,
    а також текст, перекладений на цю мову. Повертає ‘Ok’, якщо всі операції виконані,
    або повідомлення про помилку.
    out = “screen” (по замовченню) – вивести таблицю на екран
    out = “file” – вивести таблицю в файл. (Тип файлу на розсуд студента)
    text – текст, який необхідно перекласти. Якщо параметр відсутній, то відповідна колонка
    в таблиці також повинна бути відсутня.
    """
    try:
        headers = ["N", "Language", "ISO-639 code"]
        if text:
            headers.append("Text")

        rows = []
        for i, (lang_code, lang_name) in enumerate(LANGUAGES.items(), start=1):
            row = [str(i), lang_name.capitalize(), lang_code]
            if text:
                translated_text = TransLate(text, 'auto', lang_code)
                row.append(translated_text)
            rows.append(row)

        # Вивід таблиці
        if out == "screen":
            # Форматуємо та виводимо на екран
            col_widths = [max(len(str(cell)) for cell in column) for column in zip(*rows, headers)]
            print(" | ".join(header.ljust(width) for header, width in zip(headers, col_widths)))
            print("-" * (sum(col_widths) + len(col_widths) * 3))
            for row in rows:
                print(" | ".join(str(cell).ljust(width) for cell, width in zip(row, col_widths)))
        elif out == "file":
            # Записуємо в файл
            with open("languages_table.txt", "w", encoding="utf-8") as file:
                file.write(" | ".join(headers) + "\n")
                file.write("-" * (sum(len(header) for header in headers) + len(headers) * 3) + "\n")
                for row in rows:
                    file.write(" | ".join(row) + "\n")
        else:
            return "Error: Invalid output option."

        return "Ok"
    except Exception as e:
        return f"Error: {e}"


# Приклад виклику функції
print(LanguageList("screen", "Добрий день"))
