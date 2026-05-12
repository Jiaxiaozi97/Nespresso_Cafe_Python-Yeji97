# ============================================
# SHOW MENU FUNCTION
# ============================================


def show_menu():

    print("\n====================================")
    print("        NESPRESSO CAFE MENU")
    print("====================================\n")

    with open("DATA/menu.txt", "r") as file:

        for line in file:
            print(line.strip())