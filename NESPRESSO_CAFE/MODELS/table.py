# ============================================
# TABLE CLASS
# ============================================


class Table:

    def __init__(self,
                 table_number,
                 status="Free",
                 customer_name="None"):

        self.__table_number = table_number
        self.__status = status
        self.__customer_name = customer_name

    # ========================================
    # GETTERS
    # ========================================

    def get_table_number(self):
        return self.__table_number

    def get_status(self):
        return self.__status

    def get_customer_name(self):
        return self.__customer_name

    # ========================================
    # SETTERS
    # ========================================

    def set_status(self, new_status):
        self.__status = new_status

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    # ========================================
    # DISPLAY TABLE
    # ========================================

    def display_table(self):

        print(
            f"Table {self.__table_number} | "
            f"{self.__status} | "
            f"{self.__customer_name}"
        )
