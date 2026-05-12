from MODELS.table import Table


TABLE_FILE = "DATA/tables.txt"


# ============================================
# LOAD TABLES
# ============================================


def load_tables():

    tables = []

    with open(TABLE_FILE, "r") as file:

        for line in file:

            data = line.strip().split(" | ")

            table_number = int(data[0])
            status = data[1]
            customer_name = data[2]

            table = Table(
                table_number,
                status,
                customer_name
            )

            tables.append(table)

    return tables


# ============================================
# SAVE TABLES
# ============================================


def save_tables(tables):

    with open(TABLE_FILE, "w") as file:

        for table in tables:

            file.write(
                f"{table.get_table_number()} | "
                f"{table.get_status()} | "
                f"{table.get_customer_name()}\n"
            )


# ============================================
# SHOW TABLES
# ============================================


def show_tables():

    print("\n====================================")
    print("            TABLE STATUS")
    print("====================================\n")

    tables = load_tables()

    for table in tables:
        table.display_table()


# ============================================
# ASSIGN TABLE
# ============================================


def assign_table(customer):

    while True:

        tables = load_tables()

        show_tables()

        table_number = int(
            input("\nEnter table number : ")
        )

        for table in tables:

            if table.get_table_number() == table_number:

                if table.get_status() == "Free":

                    table.set_status("Occupied")
                    table.set_customer_name(
                        customer.get_name()
                    )

                    save_tables(tables)

                    print(
                        f"\nTable {table_number} assigned successfully."
                    )

                    return table

                else:

                    print("\nTable is not available.")
                    break


# ============================================
# FREE TABLE
# ============================================


def free_table(table_number):

    tables = load_tables()

    for table in tables:

        if table.get_table_number() == table_number:

            table.set_status("Free")
            table.set_customer_name("None")

    save_tables(tables)

    print(f"\nTable {table_number} is now free.")


# ============================================
# RESERVE TABLE
# ============================================


def reserve_table(table_number):

    tables = load_tables()

    for table in tables:

        if table.get_table_number() == table_number:

            table.set_status("Reserved")
            table.set_customer_name("None")

    save_tables(tables)

    print(f"\nTable {table_number} reserved successfully.")
