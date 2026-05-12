from MODELS.customer import Customer


CUSTOMER_FILE = "DATA/customers.txt"


# ============================================
# SAVE CUSTOMER
# ============================================

def save_customer(customer):

    with open(CUSTOMER_FILE, "a") as file:

        file.write(
            f"{customer.get_name()} | "
            f"{customer.get_phone_number()} | "
            f"{customer.get_membership()} | "
            f"{customer.get_total_spent()}\n"
        )


# ============================================
# SEARCH CUSTOMER
# ============================================

def search_customer(phone_number):

    try:

        with open(CUSTOMER_FILE, "r") as file:

            for line in file:

                # --------------------------------
                # SKIP EMPTY LINES
                # --------------------------------

                if line.strip() == "":
                    continue

                data = line.strip().split(" | ")

                # --------------------------------
                # SAFETY CHECK
                # --------------------------------

                if len(data) < 4:
                    continue

                name = data[0]
                phone = data[1]
                membership = data[2]
                total_spent = float(data[3])

                # --------------------------------
                # MATCH CUSTOMER
                # --------------------------------

                if phone == phone_number:

                    customer = Customer(
                        name,
                        phone,
                        membership,
                        total_spent
                    )

                    return customer

    except FileNotFoundError:

        print("\nCustomer file not found.")

    return None


# ============================================
# CREATE CUSTOMER
# ============================================

def create_customer():

    print("\n====================================")
    print("           NEW CUSTOMER")
    print("====================================")

    name = input("\nEnter customer name : ")
    phone = input("Enter phone number  : ")

    customer = Customer(name, phone)

    save_customer(customer)

    print("\nCustomer created successfully.")

    return customer


# ============================================
# LOAD CUSTOMER
# ============================================

def load_customer():

    print("\n====================================")
    print("          CUSTOMER SEARCH")
    print("====================================")

    phone_number = input(
        "\nEnter customer phone number : "
    )

    existing_customer = search_customer(
        phone_number
    )

    # ----------------------------------------
    # RETURNING CUSTOMER
    # ----------------------------------------

    if existing_customer:

        print("\nReturning customer found.")

        existing_customer.display_customer()

        return existing_customer

    # ----------------------------------------
    # NEW CUSTOMER
    # ----------------------------------------

    else:

        print("\nCustomer not found.")

        return create_customer()


# ============================================
# UPDATE CUSTOMER DATA
# ============================================

def update_customer_data(updated_customer):

    customers = []

    # ----------------------------------------
    # LOAD ALL CUSTOMERS
    # ----------------------------------------

    with open(CUSTOMER_FILE, "r") as file:

        for line in file:

            if line.strip() == "":
                continue

            data = line.strip().split(" | ")

            if len(data) < 4:
                continue

            name = data[0]
            phone = data[1]
            membership = data[2]
            total_spent = float(data[3])

            customer = Customer(
                name,
                phone,
                membership,
                total_spent
            )

            # --------------------------------
            # UPDATE MATCHING CUSTOMER
            # --------------------------------

            if (
                customer.get_phone_number()
                ==
                updated_customer.get_phone_number()
            ):

                customer = updated_customer

            customers.append(customer)

    # ----------------------------------------
    # REWRITE CUSTOMER FILE
    # ----------------------------------------

    with open(CUSTOMER_FILE, "w") as file:

        for customer in customers:

            file.write(
                f"{customer.get_name()} | "
                f"{customer.get_phone_number()} | "
                f"{customer.get_membership()} | "
                f"{customer.get_total_spent()}\n"
            )