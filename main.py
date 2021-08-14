from pprint import pprint
cook_book = {}
with open('text.txt') as file:
    for line in file:
        dish = line.strip()
        cook_book[dish] = []

        quantity = int(file.readline().strip())
        for i in range(0, quantity):
            l = file.readline().strip()
            s = l.split(' | ')
            d = {'ingredient_name': s[0], 'quantity': s[1], 'measure': s[2]}
            cook_book[dish].append(d)
        file.readline()
        # print()
# pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        for item in cook_book[dish]:
            res[item['ingredient_name']] = {'measure': item['measure'], 'quantity': int(item['quantity']) * 2}
    pprint(res)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
