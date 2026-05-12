# ============================================
# ORDER CLASS
# ============================================


class Order:

    def __init__(self, customer):

        self.__customer = customer
        self.__items = []
        self.__total_amount = 0

    # ========================================
    # ADD ITEM
    # ========================================

    def add_item(self,
                 item_name,
                 quantity,
                 item_price):

        item_total = quantity * item_price

        item_data = {
            "name": item_name,
            "quantity": quantity,
            "price": item_price,
            "total": item_total
        }

        self.__items.append(item_data)

        self.__total_amount += item_total

        print(f"\n{item_name} added successfully.")

    # ========================================
    # SHOW ORDER
    # ========================================

    def show_order(self):

        print("\n====================================")
        print("           CURRENT ORDER")
        print("====================================\n")

        if len(self.__items) == 0:

            print("Cart is empty.")
            return

        for item in self.__items:

            print(
                f"{item['name']} "
                f"x{item['quantity']} "
                f"= ${item['total']}"
            )

        print("\n------------------------------------")
        print(f"Total Amount : ${self.__total_amount}")

    # ========================================
    # GETTERS
    # ========================================

    def get_total_amount(self):
        return self.__total_amount

    def get_items(self):
        return self.__items

    def get_customer(self):
        return self.__customer
