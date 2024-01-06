class shop:
    def __init__(self, prd_file=open('products.txt', 'r+')):
        self.product_file = prd_file

    def inventory(self):
        products_info = str(self.product_file.readlines()[0])  # str of all products
        product_info = products_info.split('*')
        prd_list = []
        for i in range(len(product_info)):  # split all products info
            prd = product_info[i].split('-')
            prd_list.append(prd)

        inventory_id_list = []
        inventory_prd_list = []
        inventory_count_list = []
        inventory_price_list = []
        for j in range(len(prd_list)):  # generate inventory lists (id, name and count)
            inventory_id_list.append(prd_list[j][0])
            inventory_prd_list.append(prd_list[j][1])
            inventory_count_list.append(prd_list[j][2])
            inventory_price_list.append(prd_list[j][4])

        inventory_list = []
        for k in range(len(inventory_prd_list)):  # inventory list [prd, count]
            inventory_list.append(inventory_prd_list[k])
            inventory_list.append(inventory_count_list[k])

        return inventory_id_list, inventory_prd_list, inventory_count_list, inventory_price_list

    def sell(self):
        obj = shop()
        inventory_obj = obj.inventory()
        list_id = inventory_obj[0]
        list_name = inventory_obj[1]
        list_count = inventory_obj[2]
        list_price = inventory_obj[3]
        id_sell_input = str(input("Enter the id of product you want to buy: "))
        id_sell_index = ''
        for i in range(len(list_id)):
            if list_id[i] == id_sell_input:
                id_sell_index = i
        if id_sell_index == '':
            print('The id of product does not exist.')
            exit()
        count_sell_input = str(input("Enter the count of product you want to buy: "))
        if int(count_sell_input) > int(list_count[id_sell_index]) :
            print(f'The inventory of the "{list_name[id_sell_index]}" is {list_count[id_sell_index]}, you want more...')
        else:
            print(f'Total price {count_sell_input} of "{list_name[id_sell_index]}" is {int(list_price[id_sell_index]) * int(count_sell_input)} dollars')
            pass_key = input('If you wanna continue and buy, pls press Enter (type "cancel" to cancel your shopping)')
            if pass_key == '':
                success_message = 'tanx for your shopping'
                print(success_message)
            elif pass_key == 'cancel':
                exit()

        return id_sell_index



the_obj = shop(prd_file=open('products.txt', 'r+'))
# the_obj = shop()

# Inventory Part
"""inventory_obj = the_obj.inventory()
list_id = inventory_obj[0]
list_name = inventory_obj[1]
list_count = inventory_obj[2]
list_price = inventory_obj[3]
print('---- INVENTORIES ----')
for i in range(len(list_id)):
    print('Name: ' + list_name[i])
    print('Price: ' + list_price[i] + ' $')
    message = ''
    if list_count[i] == '0':
        message = ' All Sold...'
    print('Count: ' + list_count[i] + message)
    print()"""

# Sell Part
print('---- SELLING ----')
sell_obj = the_obj.sell()
# print(sell_obj)