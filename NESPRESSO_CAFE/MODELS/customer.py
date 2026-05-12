# ============================================
# CUSTOMER CLASS
# ============================================


class Customer:

    def __init__(self,
                 name,
                 phone_number,
                 membership="Regular",
                 total_spent=0):

        self.__name = name
        self.__phone_number = phone_number
        self.__membership = membership
        self.__total_spent = total_spent

    # ========================================
    # GETTERS
    # ========================================

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def get_membership(self):
        return self.__membership

    def get_total_spent(self):
        return self.__total_spent

    # ========================================
    # UPDATE SPENDING
    # ========================================

    def update_spending(self, amount):

        self.__total_spent += amount
        self.update_membership()

    # ========================================
    # UPDATE MEMBERSHIP
    # ========================================

    def update_membership(self):

        if self.__total_spent >= 5000:
            self.__membership = "Gold"

        elif self.__total_spent >= 2000:
            self.__membership = "Silver"

        else:
            self.__membership = "Regular"

    # ========================================
    # DISPLAY CUSTOMER
    # ========================================

    def display_customer(self):

        print("\n====================================")
        print("         CUSTOMER DETAILS")
        print("====================================")

        print(f"Name         : {self.__name}")
        print(f"Phone Number : {self.__phone_number}")
        print(f"Membership   : {self.__membership}")
        print(f"Total Spent  : ${self.__total_spent}")
