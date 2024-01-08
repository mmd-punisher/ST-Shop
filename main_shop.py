import tkinter as tk


class Shop:
    def __init__(self, product_file='products.txt'):
        self.product_file = product_file

    def update_counts(self, prd_index, new_count):  # nothing to return
        with open(self.product_file, 'r') as file:
            product_info = file.readlines()[0]
        product_list = product_info.split('*')
        for item in range(len(product_list)):
            product = product_list[item].split('-')
            if item == prd_index:
                product[2] = str(new_count)
            product_list[item] = '-'.join(product)

        updated_info = '*'.join(product_list)
        with open(self.product_file, 'w') as file:
            file.write(updated_info)

    def display_file(self, file_path):
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
                        update_count = int(prd_parts[2]) - int(count_input)
                        self.update_counts(product_list.index(product), update_count)  # change quantity on file
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

                        print('\033[1;30;42mTnx for your shopping\033[0;0m')
                        print("You can find your shopping list in the 'factor.txt' file.")

                        self.display_file('factor.txt')

                    elif pass_key.lower() == "cancel":
                        return
                    else:
                        print("INVALID INPUT")
                        return
        return sell_product

    def buy_products(self):  # TODO: complete this
        inventory_id_list, inventory_prd_list, inventory_count_list, inventory_price_list, inventory_purchase_price_list = self.inventory()
        return inventory_id_list, inventory_prd_list


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
                pass

            elif admin_key == '3':
                pass

            else:
                print('INVALID INPUT')
        else:
            print('\033[1;30;41mWrong username or password\033[0;0m')
            exit()

    elif start_key == '2':  # OK: status -- OK
        print('\033[1;31;43m---- The Menu ----\033[0;0m\n')
        print('1 - View store inventory \n2 - buying from shop')
        customer_key = str(input('Enter the action number: '))

        if customer_key == '1':
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

        elif customer_key == '2':  # NEEDTO: Show file with os
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

# Buy Products
# print(the_obj.buy_products())


# root = tk.Tk()
# with open('factor.txt', 'r') as file:
#     content = file.read()
# text_box = tk.Text(root)
# root.title('Factor')
# text_box.insert(tk.END, content)
# text_box.pack()
# root.mainloop()
