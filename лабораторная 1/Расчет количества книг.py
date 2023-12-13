# TODO Найдите количество книг, которое можно разместить на дискете

disk_capacity = 1.44 # Объем дискеты 1.44 (Мб)
number_of_page = 100 # Количество страниц в книге
line = 50 # Строк в странице
symbol_line = 25 # Количество символов в странице
code_memory = 4 # Размер символа занимаемый на диске (байт)

disk_capacity *= 1024 * 1024 # Переводим объем в байты
capacity_book = symbol_line * line * number_of_page * code_memory # Объем занимаемый одной книгой
number_of_books =  disk_capacity / capacity_book
print("Количество книг, помещающихся на дискету:", round(number_of_books))
