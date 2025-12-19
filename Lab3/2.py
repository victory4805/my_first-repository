def write_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return f'all good'

def append_to_file(dop_text, filename):
    with open(filename,'a', encoding='utf-8') as file:
        file.write('\n' + dop_text)

text = input('Введите текст для записи в файл: ')
write_to_file(text, 'user_input.txt')
print('Текст записан')

dop_text = input('Введите текст для добавления: ')
append_to_file(dop_text, 'user_input.txt')
print('Текст добавлен')