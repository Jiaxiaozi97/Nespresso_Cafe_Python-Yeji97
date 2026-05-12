from SERVICES.customer_service import load_customer

from SERVICES.table_service import (
    show_tables,
    assign_table,
    free_table,
    reserve_table
)

from SERVICES.order_service import (
    take_order,
    save_order
)

from SERVICES.payment_service import process_payment

from MODELS.invoice import Invoice

from cafe_data import show_menu


# ============================================
# MAIN MENU
# ============================================


def main_menu():

    while True:

        print("\n====================================")
        print("          NESPRESSO CAFE")
        print("====================================")

        print("\n1. New Customer Order")
        print("2. Table Management")
        print("3. Show Cafe Menu")
        print("4. Exit")

        choice = input("\nEnter your choice : ")

        # ====================================
        # NEW CUSTOMER ORDER
        # ====================================

        if choice == "1":

            customer = load_customer()

            assigned_table = assign_table(customer)

            order = take_order(customer)

            total_amount = order.get_total_amount()

            payment_method = process_payment(
                total_amount
            )

            invoice = Invoice(
                customer,
                order,
                payment_method,
                assigned_table.get_table_number()
            )

            invoice.generate_invoice()

            save_order(
                order,
                assigned_table.get_table_number(),
                payment_method
            )

            free_table(
                assigned_table.get_table_number()
            )

        # ====================================
        # TABLE MANAGEMENT
        # ====================================

        elif choice == "2":

            table_management_menu()

        # ====================================
        # SHOW MENU
        # ====================================

        elif choice == "3":

            show_menu()

        # ====================================
        # EXIT
        # ====================================

        elif choice == "4":

            print("\nThank you for visiting.")
            break

        else:

            print("\nInvalid choice.")


# ============================================
# TABLE MANAGEMENT MENU
# ============================================


def table_management_menu():

    while True:

        print("\n====================================")
        print("          TABLE MANAGEMENT")
        print("====================================")

        print("\n1. Show Tables")
        print("2. Free Table")
        print("3. Reserve Table")
        print("4. Back")

        choice = input("\nEnter your choice : ")

        # ====================================
        # SHOW TABLES
        # ====================================

        if choice == "1":

            show_tables()

        # ====================================
        # FREE TABLE
        # ====================================

        elif choice == "2":

            table_number = int(
                input("\nEnter table number : ")
            )

            free_table(table_number)

        # ====================================
        # RESERVE TABLE
        # ====================================

        elif choice == "3":

            table_number = int(
                input("\nEnter table number : ")
            )

            reserve_table(table_number)

        # ====================================
        # BACK
        # ====================================

        elif choice == "4":

            break

        else:

            print("\nInvalid choice.")


# ============================================
# START PROGRAM
# ============================================


main_menu()
