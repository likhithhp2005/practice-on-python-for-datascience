
                                                          # sample project

# 🛒 Online Shopping Cart Project

# Product catalog (dictionary with product id as key)
products = {
    1: {"name": "Laptop", "price": 50000, "stock": 5},
    2: {"name": "Phone", "price": 20000, "stock": 10},
    3: {"name": "Headphones", "price": 1500, "stock": 15},
    4: {"name": "Charger", "price": 700, "stock": 20}
}

# Empty cart dictionary
cart = {}

# Function to display available products
def show_products():
    print("\nAvailable Products:")
    print("ID\tName\t\tPrice\tStock")
    for pid, details in products.items():
        print(f"{pid}\t{details['name']}\t{details['price']}\t{details['stock']}")

# Function to add products to cart
def add_to_cart():
    show_products()
    try:
        pid = int(input("Enter Product ID to add: "))
        if pid not in products:
            print("Invalid Product ID!")
            return
        qty = int(input("Enter quantity: "))
        if qty > products[pid]["stock"]:
            print("Sorry, not enough stock!")
            return
        if pid in cart:
            cart[pid] += qty
        else:
            cart[pid] = qty
        products[pid]["stock"] -= qty
        print(f"{products[pid]['name']} added to cart.")
    except ValueError:
        print("Invalid input!")

# Function to remove products from cart
def remove_from_cart():
    if not cart:
        print("Cart is empty!")
        return
    print("\nItems in Cart:")
    for pid, qty in cart.items():
        print(f"{pid} - {products[pid]['name']} : {qty}")
    try:
        pid = int(input("Enter Product ID to remove: "))
        if pid not in cart:
            print("Product not in cart!")
            return
        qty = int(input("Enter quantity to remove: "))
        if qty >= cart[pid]:
            products[pid]["stock"] += cart[pid]
            del cart[pid]
        else:
            cart[pid] -= qty
            products[pid]["stock"] += qty
        print("Item updated in cart.")   
    except ValueError:
        print("Invalid input!")

# Function to view cart and total
def view_cart():
    if not cart:
        print("Cart is empty!")
        return
    total = 0
    print("\nYour Cart:")
    print("Name\tQuantity\tPrice")
    for pid, qty in cart.items():
        name = products[pid]["name"]
        price = products[pid]["price"] * qty
        total += price
        print(f"{name}\t{qty}\t\t{price}")
    print(f"Total Amount: {total}")

# Function to checkout and save receipt
def checkout():
    if not cart:
        print("Cart is empty!")
        return
    total = 0
    print("\n--- Bill ---")
    with open("receipt.txt", "w") as f:
        f.write("----- Receipt -----\n")
        f.write("Name\tQuantity\tPrice\n")
        for pid, qty in cart.items():
            name = products[pid]["name"]
            price = products[pid]["price"] * qty
            total += price
            f.write(f"{name}\t{qty}\t{price}\n")
        f.write(f"Total Amount: {total}\n")
        f.write("-------------------\n")
    print(f"Total Amount to pay: {total}")
    print("Receipt saved as 'receipt.txt'")
    cart.clear()  # Empty the cart after checkout

# Main menu loop
while True:
    print("\n--- Online Shopping Cart ---")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            show_products()
        elif choice == 2:
            add_to_cart()
        elif choice == 3:
            remove_from_cart()
        elif choice == 4:
            view_cart()
        elif choice == 5:
            checkout()
        elif choice == 6:
            print("Thank you for shopping! Goodbye!")
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")