numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
search_element_index = 0 # Обозначили искомый индекс предполагаемого элемента
ffg = 0
i = 0
for index in range(len(numbers)):
    if numbers[index] is None:
        g = index
    else:
        ffg = (numbers[index] + ffg)
        i = i + 1
fdf = ffg / i
numbers[g] = round(fdf,3)
print("Измененный список:", numbers)
