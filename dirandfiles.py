import os
import shutil

# 1. Показать папки, файлы и всё вместе
def list_contents(path):
    print("Папки:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Файлы:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("Всё вместе:", os.listdir(path))

list_contents(".")  # Текущая папка


# 2. Проверка прав доступа к файлу/папке
def check_access(path):
    print("Существует:", os.path.exists(path))
    print("Читается:", os.access(path, os.R_OK))
    print("Записывается:", os.access(path, os.W_OK))
    print("Запускается:", os.access(path, os.X_OK))

check_access("test.txt")


# 3. Разделить путь на папку и имя файла
def path_info(path):
    if os.path.exists(path):
        print("Папка:", os.path.dirname(path))
        print("Файл:", os.path.basename(path))
    else:
        print("Такого пути нет.")

path_info("example/test.txt")


# 4. Подсчитать строки в файле
def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print("Строк в файле:", len(lines))




# 5. Записать список в файл
def write_list_to_file(filename, items):
    with open(filename, "w", encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n")

write_list_to_file("output.txt", ["яблоко", "банан", "вишня"])


# 6. Создать 26 файлов от A.txt до Z.txt
def generate_files():
    for letter in range(65, 91):  # ASCII буквы A-Z
        with open(f"{chr(letter)}.txt", "w") as file:
            file.write(f"Файл {chr(letter)}")

generate_files()


# 7. Скопировать файл
def copy_file(source, destination):
    shutil.copy(source, destination)



# 8. Удалить файл (проверить доступ)
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("Файл удалён.")
        else:
            print("Нет прав на удаление.")
    else:
        print("Файл не найден.")



