import random
cart = {}
item_amount =[]
Total = 0

store = {
          "black shoes": {"product_id": 101, "category_id": "C10", "price": 21},
          "red shoes": {"product_id": 102, "category_id": "C20", "price": 22},
          "white shoes": {"product_id": 103, "category_id": "C30", "price": 23},
          "black shirt": {"product_id": 201, "category_id": "S10", "price": 31},
          "red shirt": {"product_id": 202, "category_id": "S20", "price": 32},
          "white shirt": {"product_id": 203, "category_id": "S30", "price": 33},
          "black pants": {"product_id": 301, "category_id": "P10", "price": 41},
          "red pants": {"product_id": 302, "category_id": "P20", "price": 42},
          "white pants": {"product_id": 303, "category_id": "P30", "price": 43},

        }
store_items = list(store.keys())

######________Welcome Note_________#####
print("Welcome to Miriam's Shop.")

# ######______ Create a session ID if login is successful______#####
def session_id():
    session_id = random.randrange(100000, 999999)
    print(f"Your session ID is: {session_id}")

#######___________To display items in store in a more palatablle manner_________######
def StoreItems():
    for item in store:
        price = store[item]["price"]
        print(f"{item} = ${price} each")

#####_______ Shopping. from adding items to cart to check out._____######


def shopping():
        item = input("Type catalogue item that you want to buy; example, red shoes. Type 'c' to check out.\n").lower()
        if item in store_items:
            price = store[item]["price"]
            print(f"Each item cost ${price}")
            if item in cart:
                modify = input("Item already in cart. Would you like to reduce item, y/n?").lower()
                if modify == "n":
                    pass
                elif modify == "y":
                    quantity = int(input("How many items do you want to buy?"))
                    item_price = price * quantity
                    cart[item] = quantity
                    global Total
                    Total -= item_price
                    print(f"Items in cart: {cart}")
                    print(f'Total price: ${Total}')
                    CheckOut()
                else:
                    input("Would you like to reduce item, Please type 'y' for yes or 'n' for no.")
            else:
                choice = input("How many items do you want to buy?")
                try:
                    quantity = int(choice)
                    item_price = price * quantity
                    cart[item] = quantity
                    Total += item_price
                    print(f"Items in cart: {cart}")
                    print(f'Total price: ${Total}')
                except:
                    print("Sorry, your entry was invalid. Please choose the item again.")
        else:
            print("Invalid choice, back to the store")

        if item == "c":
            print("You are checking out.")
            print(f"Your items in cart: {cart}\nYour total price: ${Total}")
            check = input("Do you want to remove an item?Please enter 'y' for yes or 'n' for no.").lower()
            #when you choose no theres a continued loop to login and error you have not entered a correct response
            if check == "y":
                remove_item()
                print("You are checking out.")
                print(f"Your items in cart: {cart}\nYour total price: ${Total}")
                CheckOut()

            if check == "n":
                CheckOut()
        else:
            #print("Sorry, please enter an item from the catalogue.")
            shopping()
#### To remove an item from the cart. This is called inside the shopping function above.#######
def remove_item():
    print(cart)
    global Total
    print(Total)
    r_item = input("Type the name of the item you want to remove example red shoes.\n")
    if r_item in cart:
        n_item = int(input("Type the number of items you want to keep. Type 0 if you want to remove all."))
        price1 = store[r_item]["price"]
        if n_item == 0:
            del cart[r_item]
            print(cart)
        if n_item > 0:
            item_price1 = price1 * n_item
            cart[r_item] = n_item
            # global Total
            Total -= item_price1
            print(cart)
            print(f'${Total}')
    else:
        print("Item not valid, try again or you will proceed to check out")
        remove_item()

#######____Payment methods. Also called inside shopping function.______######
def CheckOut():
    print("""\n How would you like to make your payment?
       1  Credit card Visa / Mastercard
       2  Debit card Visa / Mastercard
       3  Paypal 
       4  Klarna  """)
    payment = False
    while not payment:

        choice = int(input("\n\nenter your choice : "))
        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            print(f"""\n Your Total price is $ {Total}. 
            Your payment has been successfully placed! 
            Thank you for shopping with us and have a great day.""")
            payment = True
            exit()
        else:
            print("""\n Sorry, the payment option is unavailable. 
            How would you like to make your payment?
            1  Credit card Visa / Mastercard
            2  Debit card Visa / Mastercard
            3  Paypal 
            4  Klarna  """)


####____Admin Rights. Editing the catalogue (store function).______######

######_____ To add a product to the store. Note this does not change the store permanently.
def add_product():
    name = input("What is the name of the item you want to add? Example, blue pants")
    store[name] = {}
    product = int(input("What is the product I.D.? For example, a 3 digit number."))
    category = input("What is the category I.D.? example, b34 ")
    cost = input("What is the price? type the number only. Do not include $. ")
    store[name]["product_id"] = product
    store[name]["category_id"] = category
    store[name]["price"] = cost
    print(store)

#######_______To remove an item from the catalogue, the store function.
def remove_product():
    print(store)
    remove_item = input("Enter the key for the product you want to remove. Example, red shoes.")
    if remove_item in store_items:
        del store[remove_item]
        print('Item was successfully removed. Please see store')
        print(store)
    else:
        print("Sorry, that product is not in the catalogue.")

#_________The function that allows the administrator to chose to add or delete from a catalogue._____####
def admin_edit():
    a_choice = input("Edit catalogue. Enter 'a' to add a product or 'r' to remove product from catalogue").lower()
    if a_choice == "a":
        add_product()
    elif a_choice == "r":
        remove_product()
    else:
        print("Sorry, incorrect entry.")

####_________Dictionaries with user name and password; admin name and password. ________####

User_dict = {"peter": "pet123", "tim": "tim789"}
Admin_dict = {"dotty": "dot123", "mary": "mar345"}

######_________check if user login is correct___________###
def user_login():
    user_name_input = input("Enter a username.\n").lower()
    if user_name_input in User_dict:
        user_password_input = input("Enter a password.\n").lower()
        if user_password_input == User_dict[user_name_input]:
          print("User login successfully.")
          session_id()
          print("Let's go shopping!! Items in store:")
          print(store_items)
          shopping()
        else:
            print("Sorry, incorrect password. Start over.")
            user_login()
    else:
         print("Sorry, incorrect username.")
         user_login()

#####________Check admin login_______######
def admin_login():
    admin_name_input = input("Enter an admin username.\n").lower()
    if admin_name_input in Admin_dict:
        admin_password_input = input("Enter an admin password.\n").lower()
        if admin_password_input == Admin_dict[admin_name_input]:
          print("Login success!")
          session_id()
          admin_edit()
          admin_edit()
          exit()

        else:
            print("Sorry, incorrect password. Please start over:")
            admin_login()
    else:
         print("Sorry, incorrect username.")
         admin_login()

#######________To choose if the person is a user or an admin__________####
def login():
    guess = input("Are you a user or an admin. Enter 'u' for user or 'a' for admin.").lower()
    if guess == "u":
        user_login()
    if guess == "a":
        admin_login()
    #else:
        #print("You have not entered a correct response.")

login()



purchase = True
while purchase:

    shopping()

