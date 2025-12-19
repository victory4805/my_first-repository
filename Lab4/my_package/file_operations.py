def create_file(filename, content=""):
    with open(filename, 'w', encoding='utf-8') as file: #Создаёт файл с заданным содержимым
        file.write(content)
    print(f"Файл {filename} создан")