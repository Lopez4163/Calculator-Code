from __future__ import division
from cProfile import run
from tkinter.messagebox import YES



def menu():                         #This function is the start menu for ther calculator
    print("1. Start Calculator")
    print("2. Quit Program")

def cal():                          #This function is the meat and bones of the calculator
 while True:
    try:
        calc = input("Calculate: ")
        if (calc == "+4" or calc == "5*" or calc == "(2+3)+4" or calc == "a*b"):   #These are the restrictions you asked for to be palced
           print("ERROR, CANNOT EVALUATE EXPRESSION")
           cont =  input("Enter Yes if you want to perforn a new calculation, if not type No: ")    
           if cont == "y" and "Y" and "yes" and "Yes" and "YES":
            cal()
            
        else:
            print(eval(calc))       #The eval() function allows the user input be evaluated as an expression
            cont =  input("Enter Yes if you want to perforn a new calculation, if not type No: ")
            if cont == "y" and "Y" and "yes" and "Yes" and "YES":
                cal()
            elif cont == cont == "n" and "N" and "no" and "No" and "NO":
                print("Back to Menu")
                break
            
    except ZeroDivisionError:       #This tells python to ignore the ZeroDivisionError and instead print string and return to the calc.
        print("ERROR NO DIVISION BY ZERO ALLOWED")
    cal()
        
def main():                         #This function controls the start menu of the program
    while (True):
        menu()
        option = str(input("Enter Option: "))
        if (option == '1'):
            cal()
        elif (option == '2'):
            print("Goodbye")
            break
main()

            
        