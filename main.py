import datetime
from product import Product
from inventory import Inventory
from invoice import Invoice

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. View All Products")
        print("5. Record Sale")
        print("6. Record Return")
        print("7. Generate Invoice")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(product_id, name, category, price, quantity)
            inventory.add_product(product)
            print("Product added successfully.")

        elif choice == '2':
            product_id = input("Enter product ID: ")
            field = input("Enter field to update (price/quantity): ")
            value = input(f"Enter new {field}: ")
            if field == 'price':
                inventory.update_product(product_id, price=float(value))
            elif field == 'quantity':
                inventory.update_product(product_id, quantity=int(value))
            print("Product updated successfully.")

        elif choice == '3':
            product_id = input("Enter product ID to remove: ")
            inventory.remove_product(product_id)
            print("Product removed successfully.")

        elif choice == '4':
            products = inventory.view_all_products()
            for product in products:
                print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: {product.price}, Quantity: {product.quantity}")

        elif choice == '5':
            transaction_id = input("Enter transaction ID: ")
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity sold: "))
            sale_price = float(input("Enter sale price: "))
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            inventory.record_sale(transaction_id, product_id, quantity, sale_price, date)
            print("Sale recorded successfully.")

        elif choice == '6':
            transaction_id = input("Enter transaction ID: ")
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity returned: "))
            reason = input("Enter reason for return: ")
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            inventory.record_return(transaction_id, product_id, quantity, reason, date)
            print("Return recorded successfully.")

        elif choice == '7':
            invoice_id = input("Enter invoice ID: ")
            filename = input("Enter filename for the PDF: ")
            invoice = Invoice(invoice_id, inventory.transactions,inventory.products)
            invoice.generate_pdf(filename)
            print("Invoice generated successfully.")

        elif choice == '8':
            print("Exiting the application.")
            break

if __name__ == "__main__":
    main()


