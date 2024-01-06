product_file = open('products.txt', 'r+')


def inventory():
    products_info = str(product_file.readlines()[0])  # str of all products
    product_info = products_info.split('*')
    prd_list = []
    for i in range(len(product_info)):  # split all products info
        prd = product_info[i].split('-')
        prd_list.append(prd)

    inventory_prd_list = []
    inventory_count_list = []
    for i in range(len(prd_list)):  # generate inventory lists (name and count)
        inventory_prd_list.append(prd_list[i][0])
        inventory_count_list.append(prd_list[i][1])

    inventory_list = []
    for i in range(len(inventory_prd_list)):  # inventory list [prd, count]
        inventory_list.append(inventory_prd_list[i])
        inventory_list.append(inventory_count_list[i])

    print(inventory_prd_list)


inventory()
