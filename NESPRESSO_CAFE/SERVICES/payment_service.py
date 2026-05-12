# ============================================
# PAYMENT SYSTEM
# ============================================


def process_payment(total_amount):

    print("\n====================================")
    print("           PAYMENT MENU")
    print("====================================")

    print("\n1. Cash")
    print("2. Card")

    choice = input("\nSelect payment method : ")

    if choice == "1":
        payment_method = "Cash"

    elif choice == "2":
        payment_method = "Card"

    else:
        payment_method = "Unknown"

    print(f"\nPayment of ${total_amount} successful.")

    return payment_method
