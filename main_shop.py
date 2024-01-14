import tkinter as tk


class Shop:
    def __init__(self, product_file='products.txt'):
        self.product_file = product_file

    def update_counts(self, prd_index, new_count, opr):  # nothing to return
        with open(self.product_file, 'r') as file:
            product_info = file.readlines()[0]
        product_list = product_info.split('*')
        for item in range(len(product_list)):
            product = product_list[item].split('-')
            if item == prd_index:
                if opr == '-':
                    prd_c = int(product[2])
                    prd_c = prd_c - int(new_count)
                    product[2] = str(prd_c)
                else:
                    prd_c = int(product[2])
                    prd_c = prd_c + int(new_count)
                    product[2] = str(prd_c)

            product_list[item] = '-'.join(product)

        updated_info = '*'.join(product_list)
        with open(self.product_file, 'w') as file:
            file.write(updated_info)

    @staticmethod
    def display_file(file_path):
        root = tk.Tk()
        with open(file_path, 'r') as file:
            content = file.read()
        text_box = tk.Text(root)
        root.title('Factor')
        text_box.insert(tk.END, content)
        text_box.pack()
        root.mainloop()

    def inventory(self):
        with open(self.product_file, 'r') as file:
            product_info = file.readline()

        inventory_id_list = []
        inventory_prd_list = []
        inventory_count_list = []
        inventory_price_list = []
        inventory_purchase_price_list = []

        product_list = product_info.split('*')
        for product in product_list:
            prd_parts = product.split('-')
            inventory_id_list.append(prd_parts[0])
            inventory_prd_list.append(prd_parts[1])
            inventory_count_list.append(prd_parts[2])
            inventory_purchase_price_list.append(prd_parts[3])
            inventory_price_list.append(prd_parts[4])

        return (
            inventory_id_list,
            inventory_prd_list,
            inventory_count_list,
            inventory_price_list,
            inventory_purchase_price_list)

    def sell(self, id_input, count_input):
        with open(self.product_file, 'r') as file:
            product_info = file.readline()

        product_list = product_info.split('*')
        sell_product = {}

        for product in product_list:
            prd_parts = product.split('-')
            if prd_parts[0] == id_input:
                if int(count_input) > int(prd_parts[2]) or int(count_input) == 0:
                    print(
                        f"The inventory of the '{prd_parts[1]}' is {prd_parts[2]}. Please choose a different quantity or product.")
                    return
                else:
                    total_price = int(prd_parts[4]) * int(count_input)
                    print(f"Total price for {count_input} of '{prd_parts[1]}' is {total_price} $")
                    customer_name = input("Enter your name please: ")
                    customer_email = input("Enter your email: ")
                    customer_address = input("Enter your address: ")
                    pass_key = input(
                        "Press \033[1;36;36mEnter \033[0;0mto continue shopping(type \033[1;31;31m'cancel'\033[0;0m to cancel your shopping): ")
                    if pass_key == "":
                        self.update_counts(product_list.index(product), count_input, opr='-')  # change quantity on file

                        profit_file = open("profit.txt", "a")
                        content = '+' + str(count_input) + '*' + str(prd_parts[4]) + '#'
                        profit_file.write(content)

                        sell_product = {
                            'product id': prd_parts[0],
                            'product name': prd_parts[1],
                            'product price': prd_parts[4],
                            'product quantity': count_input,
                            'total price': total_price,
                            'customer name': customer_name,
                            'customer email': customer_email,
                            'customer address': customer_address
                        }

                        with open('factor.txt', 'w') as file:
                            file.write("This is your shopping factor\n\n")
                            for key, value in sell_product.items():
                                file.write(f"{key}: {value}\n")

                        print("You can find your shopping list in the 'factor.txt' file.")
                        yes_no_fac = input("Want to see ur factor? (yes/no) ")
                        if yes_no_fac.lower() == 'yes':
                            self.display_file('factor.txt')
                            print('\033[1;30;42mTnx for your shopping\033[0;0m')
                        else:
                            print('\033[1;30;42mTnx for your shopping\033[0;0m')
                            exit()

                    elif pass_key.lower() == "cancel":
                        return
                    else:
                        print("INVALID INPUT")
                        return
        return sell_product

    def buy_products(self):

        inventory_objj = self.inventory()
        list_idb = inventory_objj[0]
        list_nameb = inventory_objj[1]
        list_countb = inventory_objj[2]
        list_purchase_priceb = inventory_objj[4]
        list_priceb = inventory_objj[3]

        new_name = input('Product name: ')
        new_count = int(input('Quantity: '))
        name_buy_lower = new_name.replace(" ", "").lower()
        list_name_lower = [''] * len(list_idb)
        for nm in range(len(list_nameb)):
            list_name_lower[nm] = list_nameb[nm].replace(" ", "").lower()
        flag_f = False
        for m in range(len(list_name_lower)):
            if name_buy_lower == list_name_lower[m]:
                index_prd_name = m
                flag_f = True
                break
        if flag_f:
            new_index = index_prd_name
            self.update_counts(new_index, new_count, opr='+')
            print('\033[1;30;42mProduct updated successfully!\033[0;0m')
            new_purchase = list_purchase_priceb[new_index]

            profit_file = open("profit.txt", "a")
            content = '-' + str(new_count) + '*' + str(new_purchase) + '#'
            profit_file.write(content)

        else:
            new_purchase = int(input('Purchase price: '))
            new_price = int(input('Sales price: '))
            id_buy = int(list_idb[-1]) + 1
            list_idb.append(id_buy)
            list_nameb.append(new_name)
            list_countb.append(new_count)
            list_purchase_priceb.append(new_purchase)
            list_priceb.append(new_price)
            str_2_write = ''
            with open(self.product_file, 'w') as file:
                for item in range(len(list_idb)):
                    str_2_write += (str(list_idb[item]) + '-' +
                                    str(list_nameb[item]) + '-' +
                                    str(list_countb[item]) + '-' +
                                    str(list_purchase_priceb[item]) + '-' +
                                    str(list_priceb[item]) + '*')
                str_2_write = str_2_write.rstrip('*')
                file.write(str_2_write)
            print('\033[1;30;42mProduct added successfully!\033[0;0m')

            profit_file = open("profit.txt", "a")
            content = '-' + str(new_count) + '*' + str(new_purchase) + '#'
            profit_file.write(content)

    def profit_and_loss(self):
        try:
            with open("profit.txt", 'r') as file:
                profit_info = str(file.readline())
                profit_info = profit_info.rstrip('#')  # delete the last sharp
                profit_list = profit_info.split('#')
                profit_result = 0
                for p in range(len(profit_list)):
                    profit_items = profit_list[p].split('*')
                    count_p = int(profit_items[0])
                    price_p = int(profit_items[1])
                    profit_result += count_p * price_p
        except:
            profit_result = 'No content'
        return profit_result


start_key = str(
    input('\033[1;30;42mWelcome to STORE\033[0;0m\nFirst you have to sett your role\u23F3 \n1 - Admin \n2 - Customer '
          '\n"q" to exit\nEnter number to continue: '))

username = ''
password = ''
while True:
    the_obj = Shop()
    if start_key == '1':
        if username != 'admin' and password != '1234':
            username = str(input('Enter your username: '))
            password = str(input('Enter your password: '))

        if username == 'admin' and password == '1234':
            print('\033[1;30;46m---- The Admin Menu ----\033[0;0m\n')
            print('1 - Full inventory\n2 - Buy products\n3 - Selling report ')
            admin_key = str(input('Enter the action number: '))

            if admin_key == '1':  # OK: status -- Full inventory
                inventory_obj = the_obj.inventory()
                list_id = inventory_obj[0]
                list_name = inventory_obj[1]
                list_count = inventory_obj[2]
                list_price = inventory_obj[3]
                list_purchase_price = inventory_obj[4]
                print('\033[3;30;44m---- FULL INVENTORIES ----\033[0;0m')
                for i in range(len(list_id)):
                    print(f'{i + 1} - Name: ' + list_name[i] + f' (ID: {list_id[i]})')
                    print('Purchase price: ' + list_purchase_price[i] + ' $')
                    print('Sales price : ' + list_price[i] + ' $')
                    message = ''
                    if list_count[i] == '0':
                        message = '\033[3;31;31m All Sold...\033[0;0m'
                    print('Count: ' + list_count[i] + message + '\n')

            elif admin_key == '2':
                print('\033[3;30;44m---- BUY PRODUCTS ----\033[0;0m')
                the_obj.buy_products()

            elif admin_key == '3':
                profit_obj = the_obj.profit_and_loss()
                if profit_obj == 0:
                    print(f'\033[3;33;33mYour profit is {str(profit_obj)} $\033[0;0m')
                elif profit_obj > 0:
                    print(f'\033[2;32;32mYour profit is {str(profit_obj)} $\033[0;0m')
                elif profit_obj < 0:
                    print(f'\033[2;31;31mYour profit is {str(profit_obj)} $\033[0;m')
                else:
                    print('\033[3;33;33mFile is Empty!\033[0;0m')

            else:
                print('INVALID INPUT')
        else:
            print('\033[1;30;41mWrong username or password\033[0;0m')
            exit()

    elif start_key == '2':
        print('\033[1;31;43m---- The Menu ----\033[0;0m\n')
        print('1 - View store inventory \n2 - buying from shop')
        customer_key = str(input('Enter the action number: '))

        if customer_key == '1':  # OK: status -- OK
            # Inventory Part
            inventory_obj = the_obj.inventory()
            list_id = inventory_obj[0]
            list_name = inventory_obj[1]
            list_count = inventory_obj[2]
            list_price = inventory_obj[3]
            print('\033[3;30;44m---- INVENTORIES ----\033[0;0m')

            for i in range(len(list_id)):
                print(f'{i + 1} - Name: ' + list_name[i] + f' (ID: {list_id[i]})')
                print('Price: ' + list_price[i] + ' $')
                message = ''
                if list_count[i] == '0':
                    message = '\033[3;31;31m All Sold...\033[0;0m'
                print('Count: ' + list_count[i] + message + '\n')

        elif customer_key == '2':
            # Sell Part
            print('\033[3;30;42m---- SELLING ----\033[0;0m')
            id_sell_input = str(input("Enter the \033[1;36;36mid\033[0;0m of product you want to buy: "))
            count_sell_input = str(input("Enter the \033[1;36;36mcount\033[0;0m of product you want to buy: "))
            sell_obj = the_obj.sell(id_sell_input, count_sell_input)
        elif customer_key == 'q':
            exit()
        else:
            print("INVALID INPUT")
            exit()
    elif start_key.lower() == 'q':  # OK: status -- OK
        exit()
    else:
        pass
    # OK: status -- OK
    quit_key = input('\033[3;35;35m Enter "q" to QUIT or press "Enter" to continue:\033[0;0m')
    role_change = str(input('\033[1;36;36mFor change the role, type "role" or press "Enter" to continue: \033[0;0m'))
    if quit_key.lower() == 'q':
        exit()
    else:
        pass
    if role_change == 'role':
        start_key = str(input('\n1 - Admin \n2 - Customer \n"q" to exit\nEnter number to continue: '))
        username = ''
        password = ''
    elif role_change == 'q':
        exit()
    else:
        pass
