import datetime
import time
import random
import uuid

from mypackage import file_module
from mypackage import math_module


def menu():

    while True:

        print("\n----- MENU -----")
        print("1. Date and Time")
        print("2. Date Difference")
        print("3. Random Number")
        print("4. Random OTP")
        print("5. Generate UUID")
        print("6. Circle Area")
        print("7. Factorial")
        print("8. Save Text")
        print("9. Read Text")
        print("10. Show Module Functions")
        print("11. Countdown")
        print("12. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            now = datetime.datetime.now()
            print(now.strftime("%d-%m-%Y %H:%M:%S"))

        elif choice == 2:
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")

            date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

            print("Difference:", abs((date2 - date1).days), "days")

        elif choice == 3:
            print("Random Number:", random.randint(1, 100))

        elif choice == 4:
            otp = ""

            for i in range(4):
                otp += str(random.randint(0, 9))

            print("OTP:", otp)

        elif choice == 5:
            print("UUID:", uuid.uuid4())

        elif choice == 6:
            r = float(input("Enter radius: "))
            print("Area:", math_module.circle_area(r))

        elif choice == 7:
            n = int(input("Enter number: "))
            print("Factorial:", math_module.factorial(n))

        elif choice == 8:
            text = input("Enter text: ")
            file_module.save_text(text)
            print("Text saved")

        elif choice == 9:
            file_module.read_text()

        elif choice == 10:
            print(dir(random))

        elif choice == 11:
            n = int(input("Enter seconds: "))

            while n > 0:
                print(n)
                time.sleep(1)
                n = n - 1

            print("Time Over")

        elif choice == 12:
            print("Thank you")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()