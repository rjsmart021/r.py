#Mini-Project:E-commerce API
import re
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/fitness_center_db'
db = SQLAlchemy(app)

#Function to display menu
def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. add Customer")
    print("2. Read Customer")
    print("3. Update Customer")
    print("4. Delete Customer")
    print("5. Create CustomerAccount")
    print("6. Read CustomerAccount")
    print("7. Update CustomerAccount")
    print("8. Delete CustomerAccount")
    print("10. Create product")
    print("11. Read product")
    print("12. Update product")
    print("13. Delete product")
    print("14. place order")
    print("15. retrieve order")
    print("16.Quit")
    
product_list ={}
customerlist = {}
#Function to add a Customer
def add_customer(customers):
    print("\nAdding a new customer:")
    Name = input("Enter Name:")
    customerID = input("Enter customer ID")
    email = input("Enter Customer Email:")
    additional_info = input("Enter additional information (optional): ")
    Customer = {"customerName": Name, "customerID": customerID, "Customeremail": email, "Additional Info": additional_info}
    Customer[Name] = Name
    print("customer added successfully!")


#Function to read a Customer
def read_customer(customer):
    print("\nReading customerID:")
    customerID = input("Enter customerID:")
    if customerID in customer:
        print("customer details:")
        print(customerlist[customerID])
        customer.display_info()
    else:
        print("Customer not found.")

#Function to Update a Customer
def update_customer(customer):
    print("\nEditing an existing contact:")
    email = input("Enter the email of the contact you want to edit: ")
    if email in customer:
        print("Existing details:")
        print(customer[email])
        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        additional_info = input("Enter new additional information: ")
        customer[email]["Name"] = name
        customer[email]["Phone"] = phone
        customer[email]["Additional Info"] = additional_info
        print("Contact edited successfully!")
    else:
        print("Contact not found.")

# Function to delete a customer
def delete_customer(customer):
    print("\nDeleting a customer:")
    email = input("Enter the email of the customer you want to delete: ")
    if email in customer:
        del customer[email]
        print("Customer deleted successfully!")
    else:
        print("Customer not found.")

# Function to validate email format
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

#Function to add a CustomerAccount
def add_customerAccount(customerAccount):
    print("\nAdding a new customer:")
    Name = input("Enter Name:")
    customerID = input("Enter customer ID")
    email = input("Enter customer email")
    Username = input("Enter Customer Username")
    Password = input("Enter Customer Pasword")
    additional_info = input("Enter additional information (optional): ")
    CustomerAccount = {"customerName": Name, "customerID": customerID, "Customeremail": email, "Username": Username,"Password": Password,"Additional Info": additional_info}
    customer[Name] = Name
    print("customer added successfully!")

#Function to read a CustomerAccount
def read_customerAccount(customerAccount):
    print("\nReading customerID:")
    customerID = input("Enter customerID:")
    if customerID in customer:
        print("customer details:")
        print(customerlist[customerID])
        customer.display_info()
    else:
        print("Customer not found.")

#Function to Update a CustomerAccount
def update_customerAccount(customerAccount):
    print("\nEditing an existing contact:")
    email = input("Enter the email of the contact you want to edit: ")
    if email in customerAccount:
        print("Existing details:")
        print(customerAccount[email])
        username = input("Enter new Username")
        password = input("Enter new pasword")
        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        additional_info = input("Enter new additional information: ")
        customerAccount[email]["Name"] = name
        customerAccount[email]["Phone"] = phone
        customerAccount[email]["Additional Info"] = additional_info
        customerAccount[email]["Username"] = username
        customerAccount[email]["password"] = password
        print("Contact edited successfully!")
    else:
        print("Contact not found.")

#Function to delete a CustomerAccount
def delete_customerAccount(customer):
    print("\nDeleting a customer:")
    email = input("Enter the email of the customer you want to delete: ")
    if email in customer:
        del customer[email]
        print("Customer deleted successfully!")
    else:
        print("Customer not found.")

#Function to Create Product
def add_product(product):
    print("\nAdding a new product:")
    productName = input("Enter Name:")
    productID = input("Enter product ID")
    additional_info = input("Enter additional information (optional): ")
    Product = {"productName": productName, "productID": productID, "Additional Info": additional_info}
    product[productName] = productName
    print("customer added successfully!")

#Function to read a product
def read_product(product):
    print("\nReading productID:")
    productID = input("Enter productID:")
    if productID in product:
        print("product details:")
        print(product[productID])
        product.display_info()
    else:
        print("Customer not found.")

#Function to Update a product
def edit_product(product):
    print("\nEditing an existing product:")
    productID = input("Enter the productID of the product you want to edit: ")
    if productID in product:
        print("Existing details:")
        print(product[productID])
        name = input("Enter new name: ")
        additional_info = input("Enter new additional information: ")
        product[productID]["Name"] = name
        product[productID]["additional_info"] = additional_info
        print("product edited successfully!")
    else:
        print("Product not found.")

# Function to delete a product
def delete_product(product):
    print("\nDeleting a product:")
    productID = input("Enter the productID of the product you want to delete: ")
    if productID in product:
        del product[productID]
        print("product deleted successfully!")
    else:
        print("product not found.")
#List Products
# Function to display all product
def display_all_productlist(product):
    print("\nAll productlist:")
    for product in product_list:
        print("productID:", productID)
        print("ProductName:", ProductName)
        print("Additional_info:", additional_info)
    Product = {"productName": Name, "productID": productID, "Additional Info": additional_info}
    Product[ProductName] = ProductName
#Place Order
def order_product(order):
    print("\nAll productlist:")
    for product in order:
        productID = input("productID:")
        productName = input("ProductName:")
        additional_info = input("Enter additional information (optional): ")
        order = {"productName": productName, "productID": productID, "Additional Info": additional_info}
        order[productName] = productName
        print("customer added successfully!")

#Retrieve Order:
def retrieve_order(order):
    print("\nAll productlist:")
    for product in order:
        print("productID:", productID)
        print("ProductName:", ProductName)
        print(order)

# Main function
def main():
    customer= {}
    customerAccount= {}
    product = {}
    order = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_customer(customer)
        elif choice == "2":
            read_customer(customer)
        elif choice == "3":
            update_customer(customer)
        elif choice == "4":
            delete_customer(customer)
        elif choice == "5":
            add_customerAccount(customerAccount)
        elif choice == "6":
            read_customerAccount(customerAccount)
        elif choice == "7":
            update_customerAccount(customerAccount)
        elif choice == "8":
            delete_customerAccount(customerAccount)
        elif choice == "9":
            add_product(product)
        elif choice == "10":
            read_product(product)
        elif choice == "11":
            edit_product(product)
        elif choice == "12":
            delete_product(product)
        elif choice == "13":
            display_all_productlist(product)
        elif choice == "14":
            order_product(order)
        elif choice == "15":
            retrieve_order(order)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 15.")

if __name__ == "__main__":
    main()
