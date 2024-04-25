def recipes_list(file):
    cook_book = {}
    with open(file, 'rt', encoding='utf-8') as f:
        recipe_name = ''
        ingredient_list = []
        for line in f:
            if line.strip():
                recipe_name = line.strip()
                ingredient_num = int(f.readline())
                for _ in range(ingredient_num):
                    ingredient_dict = {}
                    num1, num2, num3 = f.readline().split('|')
                    ingredient_dict['ingredient_name'] = num1.strip()
                    ingredient_dict['quantity'] = num2.strip()
                    ingredient_dict['measure'] = num3.strip('\n')
                    ingredient_list.append(ingredient_dict)
                cook_book[recipe_name] = ingredient_list
                ingredient_list = []
    return cook_book


# Пример использования функции



def get_shop_list_by_dishes(dishes, person_count=1):
    cook_cook= recipes_list('recipes.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cook_cook:
            for ingredient in cook_cook[dish]:
                ingredient_name = ingredient['ingredient_name']
                ingredient_quantity = int(ingredient['quantity']) * person_count
                ingredient_measure = ingredient['measure']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': ingredient_quantity, 'measure': ingredient_measure}
                else:
                    shop_list[ingredient_name]['quantity'] += ingredient_quantity
        else:
            print(f'Блюдо {dish} не найдено')
    return shop_list



dishes_to_cook = ['домашние сырные палочки']
shop_list = get_shop_list_by_dishes(dishes_to_cook, 2)
print(shop_list)
