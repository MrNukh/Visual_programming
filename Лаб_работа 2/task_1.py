# TODO Напишите функцию для поиска индекса товара
def search_products(list_products, product_find):
    for i in range(len(list_products)):
        if list_products[i] == product_find:
            return i
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    # TODO Вызовите функцию, что получить индекс товара
    index_item = search_products(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
