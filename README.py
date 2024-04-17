cook_book = {
    'домашние сырные палочки':[
        {'ingredient_name' : "сыр твердый", 'quantity' : 300, 'measure' : 'г'},
        {'ingredient_name' : 'яйцо', 'quantity' : 1, 'measure' : 'шт.'},
        {'ingredient_name' : 'масло растительное', 'quantity' : 70, 'measure' : 'мл'},
    ],
    'банановое мороженное с какао':[
        {'ingredient_name' : 'банан', 'quantity' : 2, 'measure' : 'шт'},
        {'ingredient_name' : 'какао', 'quantity' : 1, 'measure' : 'ст.л.'}
    ],
    'трюфели из сгущенного молока и какао':[
        {'ingredient_name' : 'сгущенное молоко', 'quantity' : 240, 'measure': 'г'},
        {'ingredient_name' : 'какао', 'quantity' : 100, 'measure' : 'г'}
    ]
}

def get_shop_list_by_dishes(dishes, person_count=1):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                ingredient_quantity = ingredient['quantity'] * person_count
                ingredient_measure = ingredient['measure']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': ingredient_quantity, 'measure': ingredient_measure}
                else:
                    shop_list[ingredient_name]['quantity'] += ingredient_quantity
        else:
            print(f'Блюдо {dish} не найдено')
    return shop_list

primer_1 = get_shop_list_by_dishes(['домашние сырные палочки'], 2)
print(primer_1)

                