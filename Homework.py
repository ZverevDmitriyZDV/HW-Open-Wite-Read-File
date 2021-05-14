import os

with open(os.path.join(os.getcwd(), "recipes.txt"), 'r', encoding='utf-8') as file:
    cook_book = {}
    for file_line in file:
        line = file_line.strip()
        if line.count('|') == 0 and line != '':
            dish_name = line
            dish_elem = []
            file.readline()
        elif line != '':
            ingredient_name, quantity, measure = line.split(' | ')
            dish_elem.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            cook_book[dish_name] = dish_elem


def format_dict(dict):
    result = ''
    for key in dict.keys():
        value_prt = ''
        for elem in dict[key]:
            value_prt += f'{elem}\n'
        result += f'{key} : [\n{value_prt}]\n'
    return result


def format_dict_v2(dict):
    result = ''
    for key in dict.keys():
        result += f'{key} : {dict[key]}\n'
    return result


def get_shop_list_by_dishes(dishes, person_count):
    product_list = {}
    for dish in dishes:
        dish_needed = cook_book.get(dish, False)
        if dish_needed:
            for product in dish_needed:
                ing_measure = product['measure']
                ing_name = product['ingredient_name']
                ing_qty = product['quantity'] * person_count
                exist_list = product_list.get(ing_name, False)

                if exist_list:
                    ing_qty += exist_list['quantity']
                product_list[ing_name] = {'measure': ing_measure, 'quantity': ing_qty}
    return product_list


print(format_dict(cook_book))

list_shop = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(format_dict_v2(list_shop))

list_shop2 = get_shop_list_by_dishes(['Запеченный картофель', 'Запеченный картофель2', 'Омлет', 'Фахитос'], 7)
print(format_dict_v2(list_shop2))
