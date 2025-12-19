def read_file(filename,method='line'):
    try:
        if method == 'all':
            with open(filename, 'r', encoding='utf-8') as file: #Чтение всего файла
                return file.read()
            
        elif method == 'line':
            with open (filename,'r', encoding='utf-8') as file: #Построчное чтение
                lines = []  # Создаем список для всех строк
                for line in file:
                    lines.append(line.strip())  # Добавляем каждую строку
                return lines  # Возвращаем ВСЕ строки после цикла
            
    except:
        return 'FileNotFoundError'
    
print(read_file(filename= 'exmple.txt',method='line'))
