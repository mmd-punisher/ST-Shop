class Shop:
    def __init__(self, prd_file=open('products.txt', 'r+')):
        self.product_file = prd_file

    # def read_products(self):
    #     products_info = str(self.product_file.readlines()[0])  # str of all products
    #     product_info = products_info.split('*')
    #     prd_list = []
    #     for sht in range(len(product_info)):  # split all products info
    #         prd = product_info[sht].split('-')
    #         prd_list.append(prd)
    #     return prd_list

    def update_counts(self, prd_index, new_count):  # nothing to return
        products = open('products.txt', 'r+')
        products_info = products.readlines()[0]
        product_info = products_info.split('*')
        prd_list = []
        for sht in range(len(product_info)):  # split all products info
            prd = product_info[sht].split('-')
            prd_list.append(prd)
        prd_list[prd_index][2] = str(new_count)
        write_str = ''
        for l in range(len(prd_list)):
            for j in range(len(prd_list[0])):
                write_str += str(prd_list[l][j])
                if j == 4:
                    continue
                else:
                    write_str += '-'
            write_str += '*'
        write_str = write_str.rstrip('*')
        open('products.txt', 'w').close()
        open('products.txt', 'w').write(write_str)

    def inventory(self):
        products = open('products.txt', 'r+')
        products_info = products.readlines()[0]  # str of all products
        product_info = products_info.split('*')
        prd_list = []
        for sht in range(len(product_info)):  # split all products info
            prd = product_info[sht].split('-')
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
        self.product_file.close()

        return inventory_id_list, inventory_prd_list, inventory_count_list, inventory_price_list

    def sell(self, id_input, count_input):
        products = open('products.txt', 'r+')
        products_info = products.readlines()[0]
        product_info = products_info.split('*')
        prd_list = []
        for sht in range(len(product_info)):  # split all products info
            prd = product_info[sht].split('-')
            prd_list.append(prd)
        list_id_ = []
        list_name_ = []
        list_count_ = []
        list_price_ = []
        for j in range(len(prd_list)):  # generate inventory lists (id, name and count)
            list_id_.append(prd_list[j][0])
            list_name_.append(prd_list[j][1])
            list_count_.append(prd_list[j][2])
            list_price_.append(prd_list[j][4])
        id_sell_index = ''
        sell_product = {
            'product id': '',
            'product name': '',
            'product price': '',
            'product quantity': '',
            'total price': '',
            'customer name': '',
            'customer email': '',
            'customer address': '',
        }
        for ii in range(len(list_id_)):
            if list_id_[ii] == id_input:
                id_sell_index = ii
        if id_sell_index == '':
            print('The id of product does not exist.')
            exit()

        if int(count_input) > int(list_count_[id_sell_index]) or int(count_input) == 0:
            print(
                f'The inventory of the "{list_name_[id_sell_index]}" is {list_count_[id_sell_index]}, you want something else...')
        else:
            print(
                f'Total price {count_input} of "{list_name_[id_sell_index]}" is {int(list_price_[id_sell_index]) * int(count_input)} dollars')
            customer_name = str(input('Enter your name please: '))
            customer_email = str(input('Enter your email: '))
            customer_address = str(input('Enter your address: '))
            pass_key = input('If you wanna continue and buy, plz press Enter (type "cancel" to cancel your shopping)')
            if pass_key == '':
                update_count = int(list_count_[id_sell_index]) - int(count_input)
                self.update_counts(id_sell_index, update_count)
                sell_product.update({'product id': str(list_id_[id_sell_index]),
                                     'product name': str(list_name_[id_sell_index]),
                                     'product price': str(list_price_[id_sell_index]),
                                     'product quantity': str(count_input),
                                     'total price': str(int(list_price_[id_sell_index]) * int(count_input)),
                                     'customer name': customer_name,
                                     'customer email': customer_email,
                                     'customer address': customer_address})
                print('Tnx for your shopping')
            elif pass_key == 'cancel':
                exit()
            else:
                print('INVALID INPUT')
                exit()
            open('factor.txt', 'w').close()
            sell_keys = list(sell_product.keys())
            sell_values = list(sell_product.values())
            write_factor = 'This is your shopping factor\n\n'
            for e in range(len(sell_keys)):
                write_factor += sell_keys[e]
                write_factor += (' : ' + sell_values[e])
                write_factor += '\n'
            open('factor.txt', 'w').write(write_factor)
            print('You can get your shopping list in current folder named "factor.txt"')
        return sell_product


the_obj = Shop()

# Inventory Part
inventory_obj = the_obj.inventory()
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
    print()

# Sell Part
print('---- SELLING ----')
id_sell_input = str(input("Enter the id of product you want to buy: "))
count_sell_input = str(input("Enter the count of product you want to buy: "))
sell_obj = the_obj.sell(id_sell_input, count_sell_input)
