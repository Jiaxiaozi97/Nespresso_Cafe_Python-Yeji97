# ============================================
# INVOICE CLASS
# ============================================


class Invoice:

    def __init__(self,
                 customer,
                 order,
                 payment_method,
                 table_number):

        self.__customer = customer
        self.__order = order
        self.__payment_method = payment_method
        self.__table_number = table_number

    # ========================================
    # DISPLAY INVOICE
    # ========================================

    def generate_invoice(self):

        print("\n====================================")
        print("          NESPRESSO CAFE")
        print("====================================")

        print(
            f"\nCustomer : {self.__customer.get_name()}"
        )

        print(
            f"Table    : {self.__table_number}"
        )

        print("\n------------------------------------")

        for item in self.__order.get_items():

            print(
                f"{item['name']} "
                f"x{item['quantity']} "
                f"= ${item['total']}"
            )

        print("\n------------------------------------")

        subtotal = self.__order.get_total_amount()

        discount = 0

        if self.__customer.get_membership() == "Silver":
            discount = subtotal * 0.10

        elif self.__customer.get_membership() == "Gold":
            discount = subtotal * 0.20

        final_total = subtotal - discount

        print(f"Subtotal        : ${subtotal}")
        print(f"Discount        : ${discount}")
        print(f"Final Total     : ${final_total}")

        print(
            f"Payment Method  : {self.__payment_method}"
        )

        print("====================================")
