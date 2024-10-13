def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    row_count = 0;
    # content = file.read()
    # return content
    keys = []
    values = []
    for i in strings:
        row_count += 1
        byte_num = file.tell()
        file.write(f'{str(i)}\n')

        keys.append((row_count, byte_num))
        values.append(str(i))
        strings_items = dict(zip(keys, values))
    file.close()
    return strings_items

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

