inp_str = input('Введите строку цифр, заканчивая точкой: \n')
num = list(inp_str[:-1]) # собираем цифры в листы и выбрасываем точку

my_dict = {i: num.count(i) for i in num}  # собираем словарь где ключ - цифра, а значение - кол-во повторений

def sort_dictionary_by_value(dictionary):
    list_of_sorted_pairs = [(k, dictionary[k]) for k in sorted(dictionary.keys(), key = dictionary.get)]
    return list_of_sorted_pairs
    # Cоздаём кортежи (ключ, значение) из отсортированных элементов по ключу равному "значение ключа"
    # Также отсортированы будут и ключи, имеющие одно значение
    # после сделанных операций возвращаем получившийся список

new_dict = sort_dictionary_by_value(my_dict)

a = list()
for x in new_dict:  # вытаскиваем из кортежа (ключ:значение) ключи и собираем их в список, это наши цифры
    a.append(x[0])

print(*a, sep="")  # звёздочка распаковывает список и возвращает каждый элемент без пробела

