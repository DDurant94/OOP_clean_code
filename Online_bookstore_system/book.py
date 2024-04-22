import re
class Book:
  def __init__(self, product_id, book_name, book_author, book_price, book_stock):
    self.product_id = product_id
    self.book_name = book_name
    self.book_author = book_author
    self.__book_price = book_price
    self.book_stock = book_stock
    
  def get_book_price(self):
    return self.__book_price
  
  def set_book_price(self,new_price):
    self.__book_price == new_price
    print(f"Price of {self.book_name} has been changed to {new_price:.2f}")

  def sell_price(self):
    # Auto mark up for any book entered into the system markup is 20%
    mark_up = .20
    book_sell_price = self.get_book_price() * mark_up + self.get_book_price()
    return book_sell_price

  def check_availability(self):
    return self.book_stock > 0

  def update_stock(self,quantity):
    # updating the stock once the cart is checked out
    if self.book_stock >= quantity:
      self.book_stock -= quantity

  def view_stock_item_customer(self):
    # How the customer views stock 
    print(f"Title: {self.book_name}, Author: {self.book_author}\nAvailable Stock: {self.book_stock}\nPrice: ${self.sell_price():.2f}")

  def view_stock_item_admin(self):
    # how the admin would view stock
    print(f"Book ID Number: {self.product_id}\n Title: {self.book_name}, Author: {self.book_author}\nAvailable Stock: {self.book_stock}\nAt Cost Price: ${self.get_book_price():.2F} Selling Price: ${self.sell_price():.2f} Profit of each sale is ${(self.sell_price()-self.get_book_price()):.2f}")


class Cart:

  def add_to_cart(self,users_cart,inventory):
    # Adding to users cart checking to see if the items are in the cart or dont 
    try:
      book_type = input("Enter the Genre of book [Fiction, Non Fiction, History, Mystery, Science, Romance]: ").title()
      book_name = input("Enter the name of book: ").title()
      quantity = int(input("Enter quantity: "))
      if book_name in inventory[book_type] and Book.check_availability(inventory[book_type][book_name]):
        if book_name in users_cart:
          users_cart[book_name] += quantity,inventory[book_type][book_name]
          print(f"{quantity} of {book_name} was added to your cart")
          return users_cart
        else:
          users_cart[book_name] = quantity,inventory[book_type][book_name]
          print(f"{quantity} of {book_name} was added to your cart")
          return users_cart
        
    except ValueError:
      print("Enter a Number")
    except KeyError:
      print("Wrong Genre")
      
      
  def cart(self,users_cart,user):
    # Cart and checkout is in all one function 
    total = 0
    print(f"\n{user}'s Cart\n")
    for item, quantity in users_cart.items():
      total += Book.sell_price(quantity[1]) * quantity[0]
      print(f"Title: {item}: Quantity: {quantity[0]} ${Book.sell_price(quantity[1]):.2f} Each")
      # 10% tax is added to the total 
    print(f"Total Cart Cost ${total *.10 + total:.2f}\n")
    checkout = input("Do you want to check out [Yes/No]: ").lower()
    if checkout == "yes":
      print("Order has been processed. Thank you for your business!\n")
      for item, quantity in users_cart.items():
        Book.update_stock(quantity[1],quantity[0])
      users_cart.clear()
    elif checkout == "no":
      pass
    else:
      print("Invalid choice") 


class User:
  def __init__(self,username):
    self._username = username
    self.get_cart = Cart()
    self.admin = Admin()
    
  def get_username(self):
      return self._username
  
  def admin_control(self,inventory):
     self.admin.admin_menu(inventory)

  def users_cart(self,users_cart):
     user = self.get_username()
     self.get_cart.cart(users_cart,user)
  
  def adding_items_user_cart(self,user_cart,inventory):
     self.get_cart.add_to_cart(user_cart,inventory)

  def searching_inventory(self,inventory):
    # allowing user to see the inventory from user prospective
    try:
      book_type = input("Enter the Genre of book [Fiction, Non Fiction, History, Mystery, Science, Romance]: ").title()
      book_name = input("Enter the name of book: ").title()
      if book_name in inventory[book_type]:
          Book.view_stock_item_customer(inventory[book_type][book_name])
      else:
        print("Book Not Found")
    except KeyError:
       print("Book Title Not Found")


class Admin:
  def admin_menu(self,inventory):
    # password protected admin main menu for entering all the info for the book store
    set_password = r"^@BookStore_303!$"
    password_input = input("Enter Password: ")
    password_validation = re.match(set_password,password_input)
    if password_validation:
        while True:    
            print("Admin Menu:\n1. Add Book\n2. Change Price\n3. Delete Item\n4. View Stock\n5. Exit")
            admin_input = input("Choose one of our menu options: ")
            if admin_input == "1":
                Admin.add_book(self,inventory)
            elif admin_input == "2":
                Admin.change_pricing(self,inventory)
            elif admin_input == "3":
                Admin.remove_item(self,inventory)
            elif admin_input == "4":
                Admin.view_stock(self,inventory)

            elif admin_input == "5":
                break
            else:
                print("Invalid Input")

  def add_book(self,inventory):
    # Entering all info for adding a book
    try:
        book_type = input("Enter the Genre of book [Fiction, Non Fiction, History, Mystery, Science, Romance]: ").title()
        book_id = input("Enter the book ID number: ")
        book_name = input("Enter the name of book: ").title()
        book_author = input("Enter the author of the book: ").title()
        book_price = float(input("Enter the price of the book: "))
        book_stock = int(input("Enter the total number of books: "))
        inventory[book_type][book_name] = Book(book_id, book_name, book_author, book_price, book_stock)
    except ValueError:
        print("Enter in a price")
    except KeyError:
        print("Wrong Genre")

  def change_pricing(self,inventory):
        # changing the price of a book if new stock comes in 
        book_type = input("Enter the Genre of book [Fiction, Non Fiction, History, Mystery, Science, Romance]: ").title()
        book_name = input("Enter the name of book: ").title()
        if book_name in inventory[book_type]:
            new_price = float(input("Enter in new price: ")) 
            Book.set_book_price(inventory[book_type][book_name],new_price)
        else:
            print("Book not Found")

  def remove_item(self,inventory):
      # removing stock from the store
      book_type = input("Enter the Genre of book [Fiction, Non Fiction, History, Mystery, Science, Romance]: ").title()
      book_name = input("Enter the name of book: ").title()
      if book_name in inventory[book_type]:
        del inventory[book_type][book_name]
      else:
        print("Book not Found")
  
  def view_stock(self,inventory):
      # viewing stock from the admin perspective
      while True:
        print("View Menu:\n1. View All\n2. View by book\n3. Exit")
        view_choice = input("Choose one of our menu options: ")
        if view_choice == "1":
            for genre, book in inventory.items():
                for item in book.items():
                    Book.view_stock_item_admin(item[1])
        elif view_choice == "2":
          book_type = input("Enter the Genre of book [Fiction, Non Fiction, History, Mystery, Science, Romance]: ").title()
          book_name = input("Enter the name of book: ").title()
          if book_name in inventory[book_type]:
              Book.view_stock_item_admin(inventory[book_type][book_name])
          else:
              print("Book Not found")
        elif view_choice == "3":
            break
        else:
            print("Invalid Choice")