class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.product_id} | {self.name} | {self.category} | ${self.price:.2f} | {self.stock_quantity} in stock"


class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}
        self.users = {"admin": {"password": "adminpass", "role": "Admin"},
                      "user": {"password": "userpass", "role": "User"}}
        self.ADULT_AGE = 18  # Constant used if required for any age check.

    def login(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == password:
            return user["role"]
        else:
            print("Invalid credentials. Access denied.")
            return None

    def add_product(self, product):
        if product.product_id in self.inventory:
            print("Product already exists. Update the product instead.")
        else:
            self.inventory[product.product_id] = product
            print(f"Product '{product.name}' added to inventory.")

    def update_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        if product_id in self.inventory:
            product = self.inventory[product_id]
            if name:
                product.name = name
            if category:
                product.category = category
            if price:
                product.price = price
            if stock_quantity is not None:
                product.stock_quantity = stock_quantity
            print("Product updated successfully.")
        else:
            print("Product not found.")

    def remove_product(self, product_id):
        if product_id in self.inventory:
            del self.inventory[product_id]
            print("Product removed from inventory.")
        else:
            print("Product not found.")

    def display_inventory(self):
        if self.inventory:
            print("\nCurrent Inventory:")
            for product in self.inventory.values():
                print(product)
        else:
            print("Inventory is empty.")

    def search_product(self, name):
        found_products = [product for product in self.inventory.values() if product.name == name]
        if found_products:
            for product in found_products:
                print(product)
        else:
            print("No product found with that name.")

    def low_stock_alert(self, threshold=5):
        low_stock_products = [product for product in self.inventory.values() if product.stock_quantity <= threshold]
        if low_stock_products:
            print("Low Stock Alert:")
            for product in low_stock_products:
                print(f"{product.name} has low stock: {product.stock_quantity} remaining.")
        else:
            print("All products have sufficient stock.")


def main():
    ims = InventoryManagementSystem()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    role = ims.login(username, password)

    if role == "Admin":
        print(f"Welcome {username}!")
        while True:
            print("\nOptions:")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Remove Product")
            print("4. View Inventory")
            print("5. Search Product")
            print("6. Check Low Stock Alert")
            print("7. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                product_id = input("Enter product ID: ")
                name = input("Enter product name: ")
                category = input("Enter product category: ")
                price = float(input("Enter product price: "))
                stock_quantity = int(input("Enter stock quantity: "))
                product = Product(product_id, name, category, price, stock_quantity)
                ims.add_product(product)

            elif choice == "2":
                product_id = input("Enter product ID to update: ")
                name = input("Enter new product name (leave blank to keep current): ") or None
                category = input("Enter new category (leave blank to keep current): ") or None
                price = input("Enter new price (leave blank to keep current): ")
                price = float(price) if price else None
                stock_quantity = input("Enter new stock quantity (leave blank to keep current): ")
                stock_quantity = int(stock_quantity) if stock_quantity else None
                ims.update_product(product_id, name, category, price, stock_quantity)

            elif choice == "3":
                product_id = input("Enter product ID to remove: ")
                ims.remove_product(product_id)

            elif choice == "4":
                ims.display_inventory()

            elif choice == "5":
                name = input("Enter product name to search: ")
                ims.search_product(name)

            elif choice == "6":
                threshold = int(input("Enter stock threshold for low stock alert: "))
                ims.low_stock_alert(threshold)

            elif choice == "7":
                print("Exiting...")
                break

            else:
                print("Invalid option. Please try again.")

    elif role == "User":
        print(f"Welcome {username}! You can view the inventory.")
        ims.display_inventory()

if __name__ == "__main__":
    main()

