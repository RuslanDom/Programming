speakers_file = open("9.3_List_speakers.txt", 'r', encoding='utf-8')

symbol_count = []
for i_line in speakers_file:
    print(i_line, end='')  # Печатает строки
    symbol_count.append(f"Кол-во символов в строке '{i_line.strip('\n')}' == {str(len(i_line))}")  # Добавляет в список кол-во символов в строке в формате str
symbol_count_str = '\n'.join(symbol_count)  # Объединяет получившийся список в строку через разделитель \n

speakers_file.close()


counts_file = open('result_write.txt', 'w', encoding='utf-8')
counts_file.write(symbol_count_str)

counts_file.close()
