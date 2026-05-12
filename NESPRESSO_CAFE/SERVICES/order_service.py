from MODELS.order import Order


MENU_FILE = "DATA/menu.txt"


# ============================================
# SEARCH MENU ITEM
# ============================================


def search_menu_item(item_code):

    with open(MENU_FILE, "r") as file:

        for line in file:

            if "[" in line:

                try:

                    code = line.split("]")[0][1:]

                    if code == item_code:

                        item_data = line.split("]")[1].strip()

                        item_name = item_data.split("|")[0].strip()

                        item_price = float(
                            item_data.split("|")[1]
                            .replace("$", "")
                            .strip()
                        )

                        return item_name, item_price

                except:
                    continue

    return None


# ============================================
# TAKE ORDER
# ============================================


def take_order(customer):

    order = Order(customer)

    while True:

        print("\n====================================")
        print("             ORDER MENU")
        print("====================================")

        print("\n1. Show Menu")
        print("2. Add Item")
        print("3. Show Cart")
        print("4. Checkout")

        choice = input("\nEnter your choice : ")

        # ====================================
        # SHOW MENU
        # ====================================

        if choice == "1":

            with open(MENU_FILE, "r") as file:

                for line in file:
                    print(line.strip())

        # ====================================
        # ADD ITEM
        # ====================================

        elif choice == "2":

            item_code = input(
                "\nEnter item code : "
            ).upper()

            item = search_menu_item(item_code)

            if item:

                item_name = item[0]
                item_price = item[1]

                quantity = int(
                    input("Enter quantity : ")
                )

                order.add_item(
                    item_name,
                    quantity,
                    item_price
                )

            else:

                print("\nInvalid item code.")

        # ====================================
        # SHOW CART
        # ====================================

        elif choice == "3":

            order.show_order()

        # ====================================
        # CHECKOUT
        # ====================================

        elif choice == "4":

            return order

        else:

            print("\nInvalid choice.")

# ============================================
# SAVE ORDER
# ============================================

def save_order(order,
               table_number,
               payment_method):

    ORDER_FILE = "DATA/orders.txt"

    customer_name = (
        order.get_customer().get_name()
    )

    total_amount = (
        order.get_total_amount()
    )

    with open(ORDER_FILE, "a") as file:

        file.write(
            f"{customer_name} | "
            f"Table {table_number} | "
            f"${total_amount} | "
            f"{payment_method}\n"
        )