'''
1. Building a Modular Online Bookstore System
Objective:
The objective of this assignment is to create a modular online bookstore system using Python. 
The focus will be on applying the principle of modularity to enhance code organization, maintainability, 
and scalability. The system will be broken down into different modules, each handling specific functionalities of the bookstore.

Task 1: Designing the Book Module

Create a module for managing book-related functionalities. This includes classes and functions for book attributes, 
book availability, and any other book-specific operations.

Problem Statement:

The bookstore system requires a dedicated module for handling various aspects related to books, 
such as title, author, price, and stock status.

Code Example:

book.py

class Book:
    # Define book attributes and methods
    pass

# Additional functions related to book management
Expected Outcome:

A main.py module that effectively integrates the book, user, and cart modules, allowing for a smooth and modular operation 
of the online bookstore system. The integration should highlight the benefits of modularity in software design.
'''
from book import User as U

def main():
    username_input = input("Enter Username: ")
    user = U(username_input)
# Kept carts outside of a module to move objects around easier
    users_cart = {}

    inventory = {"Fiction":{},
             "Non Fiction":{},
             "History":{},
             "Mystery":{},
             "Science":{},
             "Romance":{}}

    print("Welcome to the Book Store Systems")
    while True:
        print("Main Menu:\n1. Admin\n2. Search Books\n3. View Cart\n4. Add To Cart\n5. Exit")
        menu_choice = input("Choose one of our menu options: ")
        if menu_choice == "1":
            U.admin_control(user,inventory)
            print(inventory)
        elif menu_choice == "2":
            U.searching_inventory(user,inventory)
        elif menu_choice == "3":
            U.users_cart(user,users_cart)
        elif menu_choice == "4":
            U.adding_items_user_cart(user,users_cart,inventory)
        elif menu_choice == "5":
            print("Thank you for using Book Store Systems")
            break
        else:
            print("Invalid input")

main()


