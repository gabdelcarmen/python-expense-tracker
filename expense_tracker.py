import pandas as pd
import os
from datetime import datetime

def load_or_create_excel(file_path="expense. xlsx"):
    if os.path.exists(file_path):
        print(f"Loading existing file: {file_patch}")
        df = pd.read_excel(file_path)
    else:
        print(f"Creating new file: {file_path}")
        df = pd.DataFrame(columns=["Date", "Type", "Category", "Description", "Amount"])
    return df


def save_to_excel(df, file_path = "expenses.xlsx"):
    with pd.ExcelWriter(file_path, engine = "openpyxl") as writer:
        df.to_excel(writer, sheet_name = "Transactions", index = False)

        worksheet = writer.sheets["Transactions"]
        if len(df) > 0:
            from openpyxl.worksheet.table import Table, TableStyleInfo
            tab = Table(displayname = "Expense Tracker", ref = f"A1:E{len(df)+1}")
            style = TableStyleInfo(name = "TableStyleMedium9", showRowStrips = True)
            tab.tableStyleInfo = style
            worksheet.add_table(tab)
    
    print(f"Data saved to {file_path}")


def add_transaction():
    while True:

        print("Transactions: \n\n"
              "1. Expense\n"
              "2. Income\n"
              "3. Back\n")
        print("Choose a number to navigate\n")
        
        try:
            transaction_choice = int(input("Navigate by choosing a number (1-3): "))

            if transaction_choice == 1:
                print("Categories: \n"
                    "1. School\n"
                    "2. Leisure\n"
                    "3. Hobby\n"
                    "4. Products\n"
                    "5. Back")

                expense_choice = int(input("Navigate by choosing a number (1-5): "))

                if expense_choice == "":
                    print("Please enter a number (1-5)")

                elif expense_choice == 1:


                elif expense_choice == 2:

                
                elif expense_choice == 3:


                elif expense_choice == 4:


                elif expense_choice == 5:
                    break

        
            if transaction_choice == 2:
                print("Categories: \n"
                "1. Allowance\n"
                "2. Personal\n"
                "3. Back")
            
                income_choice = int(input("Navigate by choosing a number(1-3): "))

                if income_choice == "":
                    print("Please enter a number (1-3)")
                
                elif income_choice == 1:

                
                elif income_choice == 2:

                
                elif income_choice == 3:
                    break

def view_transactions():


def entry():


def summary():


def main():

    while True:
        print("Expense Tracker\n"
              "--------------------------------------------------------------\n\n")
        print("1. Add Transaction\n"
              "2. View All Transactions\n"
              "3. Edit Entry\n"
              "4. View Summary\n"
              "5. Exit")

        try:
            choice = int(input("Navigate by choosing a number (1-5): "))

            if choice == "":
                print("Please enter a number (1-5)")

            elif choice == 1:
                add_transaction()

            elif choice == 2:
                view_transactions()

            elif choice == 3:
                entry()

            elif choice == 4:
                summary()

            elif choice == 5:
                break

            else:
                print("Please enter a number (1-5)")

        except ValueError:
            print("Please enter a number (1-5)")


main()
