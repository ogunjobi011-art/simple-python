#This is a python function that loads a bank data from a text file
DATA_FILE = "bank_data.txt"
#this stores the name of the file containing the bank info

def load_data():
    try:
# This tells Python:“Try to run this code, but if something goes wrong, handle the error.”
        file = open(DATA_FILE, "r") 
# open the file in read mode
        lines = file.readlines() 
# read all lines from the file and store them in a list called lines   
        file.close()

        names = lines[0].strip()
 #strip() removes any leading or trailing whitespace characters (like spaces or newlines)
 #  from the string.
        balance = float(lines[1].strip())
#float() converts the string to a floating-point number
        expenses = []
 # This is an empty list that will store the expense dictionaries
        
        for line in lines[2:]:
# This loop iterates over each line in the lines list, starting from the third line (index 2)
            description, category, amount = line.strip().split("|")
#strip() removes whitespace, and split("|") splits the line into three parts based on the "|" character.
#  These parts are assigned to description, category, and amount variables.
            
            expenses.append({
                "description": description,
                "category": category,
                "amount": float(amount) 
            })
#append means to add a new dictionary to the expenses list.
#  Each dictionary contains the description, category, and amount of an expense.
            return names, balance, expenses
        
    except FileNotFoundError:
        return None, 0, []
# This handles the case where the file does not exist. It returns None for names, 0 for balance,
#  and an empty list for expenses.
    except Exception as error:
        print("Error loading data:", error)
        return None, 0, []
 # This handles any other exceptions that might occur while loading the data. 

 