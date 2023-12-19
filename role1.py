'''class Product:
    def __init__(self, name, quantity, purchase_price, sale_price):
        self.name = name
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.sale_price = sale_price


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def search_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def get_product_quantity(self, product):
        return product.quantity

    def get_all_products(self):
        return self.products


class Transaction:
    def __init__(self, transaction_type, date, product, quantity, price, buyer_name):
        self.transaction_type = transaction_type
        self.date = date
        self.product = product
        self.quantity = quantity
        self.price = price
        self.buyer_name = buyer_name


class Sales:
    def __init__(self):
        self.transactions = []

    def add_sale(self, sale):
        self.transactions.append(sale)

    def calculate_monthly_sales(self):
        # Calculate and return the total sales for the month
        total_sales = 0
        for sale in self.transactions:
            total_sales += sale.price * sale.quantity
        return total_sales


class Purchases:
    def __init__(self):
        self.transactions = []

    def add_purchase(self, purchase):
        self.transactions.append(purchase)

    def calculate_monthly_purchases(self):
        # Calculate and return the total purchases for the month
        total_purchases = 0
        for purchase in self.transactions:
            total_purchases += purchase.price * purchase.quantity
        return total_purchases


class StoreSystem:
    def __init__(self):
        self.inventory = Inventory()
        self.sales = Sales()
        self.purchases = Purchases()

    def add_product_to_inventory(self, product):
        self.inventory.add_product(product)

    def record_sale(self, sale):
        self.sales.add_sale(sale)

    def record_purchase(self, purchase):
        self.purchases.add_purchase(purchase)

    def calculate_monthly_profit(self):
        total_sales = self.sales.calculate_monthly_sales()
        total_purchases = self.purchases.calculate_monthly_purchases()
        monthly_profit = total_sales - total_purchases
        return monthly_profit'''

class Product:
    def __init__(self, name, quantity, purchase_price, selling_price):
        self.name = name
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.selling_price = selling_price

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_inventory(self):
        return self.products

class Transaction:
    def __init__(self, transaction_type, product, quantity, price, date, buyer_seller):
        self.transaction_type = transaction_type
        self.product = product
        self.quantity = quantity
        self.price = price
        self.date = date
        self.buyer_seller = buyer_seller

class SalesSystem:
    def __init__(self):
        self.inventory = Inventory()
        self.transactions = []

    def add_product_to_inventory(self, product):
        self.inventory.add_product(product)

    def add_sale_transaction(self, product, quantity, price, date, buyer):
        transaction = Transaction("Sale", product, quantity, price, date, buyer)
        self.transactions.append(transaction)
        product.quantity -= quantity

    def add_purchase_transaction(self, product, quantity, price, date, seller):
        transaction = Transaction("Purchase", product, quantity, price, date, seller)
        self.transactions.append(transaction)
        product.quantity += quantity

    def generate_monthly_report(self):
        total_sales = 0
        total_purchases = 0
        total_profit = 0

        for transaction in self.transactions:
            if transaction.transaction_type == "Sale":
                total_sales += transaction.price * transaction.quantity
            elif transaction.transaction_type == "Purchase":
                total_purchases += transaction.price * transaction.quantity

        total_profit = total_sales - total_purchases

        report = f"Monthly Report:\nTotal Sales: {total_sales}\nTotal Purchases: {total_purchases}\nTotal Profit: {total_profit}"
        return report

# نمونه استفاده از سامانه فروش
sales_system = SalesSystem()

# اضافه کردن محصولات به موجودی
product1 = Product("Laptop", 10, 1000, 1500)
product2 = Product("Phone", 20, 500, 800)
sales_system.add_product_to_inventory(product1)
sales_system.add_product_to_inventory(product2)

# ثبت تراکنش‌های فروش و خرید
sales_system.add_sale_transaction(product1, 2, 1500, "2023-12-19", "John")
sales_system.add_purchase_transaction(product2, 5, 600, "2023-12-18", "Supplier A")

# تولید گزارش ماهانه
monthly_report = sales_system.generate_monthly_report()
print(monthly_report)