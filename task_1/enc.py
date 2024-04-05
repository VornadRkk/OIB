import os
import json
from constant import Alphavit, Paths, shift


def read_json_file(file_path: str) -> dict:
    """
    Function to read data from a JSON file.

    Arguments:
    file_path (str): Path to the JSON file.

    Returns:
    dict: Dictionary containing data from the JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def ceasar_encrypt(text: str, shift: int) -> str:
    encrypted_text = ""
    text.upper()
    for x in text:
        if x in text:
            ind = Alphavit.index(x)
            encrypted_text += Alphavit[ind + shift]
        else:
            encrypted_text += x
    return encrypted_text


def main() -> None:
    """
    a function for working with file paths.
    parametrs: none
    return: none
    """
    paths_data = read_json_file(Paths)
    if paths_data:
        folder = paths_data.get("folder", "")
        first_text = paths_data.get("first_text", "")
        second_text = paths_data.get("second_text", "")

        if folder and first_text and second_text:
            try:
                with open(f"{folder}/{first_text}", "r", encoding="utf-8") as file:
                    text = file.read()
                    encrypted_text = ceasar_encrypt(text, shift)  # Используйте значение shift из модуля constant

                with open(f"{folder}/{second_text}", "w", encoding="utf-8") as file:
                    file.write(encrypted_text)

                print("Текст успешно зашифрован и сохранен в файле.")
            except FileNotFoundError:
                print("Один из файлов не найден.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        else:
            print("Не удалось получить пути к файлам из JSON-данных.")
    else:
        print("Не удалось прочитать данные из JSON-файла.")


if __name__ == "main":
    main()
