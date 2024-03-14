'''
Capstone Project
Assume that you have been approached by a small financial company and asked to create a program that allows 
the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.

Print an intro of what the program is doing and explain what an investment and bond calculator is.
Ask the user to choose between an "investment calculator" or a "bond calculator" by inputting either "investment" or bond.
If neither are entered, print an error.

If "investment" is inputted ask the user to input the following:
- Amount of money they want to deposit
- Interest Rate
- Number of Years they plan on investing
Will then ask the user if they want to calculate either "Simple" or "Compound" interest.
Prints the answer the user has asked for.

Simple Interest formula is:     A = P *(1 + r*t)
Compound Interest formula is:   A = P * math.pow((1+r),t)
r = interest
P = Deposit
t = Number of years



If "bond" was in inputted ask the user to input the following:
- Current value of the house.
- Interest rate.
- Number of Months they plan to take to repay the bond.

Will then calculate the how much their repayment be each month and print.
Bond Formaula is:       Repayment = (i * P)/(1 - (1 + i)**(-n))
P - Value of House
i - interest rate
n - number of months

please input either bond or investment
'''
import math #import futher math codes into program

print ("Hi, Welcome To Your Very Own Financial Calculator! \n\nHere we can calculate either your 'Home Loan Repayments' or just a simple 'Investment Calculator' ")
print ("First lets explain what both calculators do:")
print ("Investment - Calculates the amount of interest you'll earn on your investments.")
print ("Home Loan Repayment - Calculates the amount you'll have to pay on your home loan.")
#Intro

choice = str(input("\nPlease input either 'Investment' or 'Bond', Depending on which calculator you want to use: ")).lower()
#Ask the user in input either investment or bond and store as "choice"
#Anything that the user inputs, automatically converts in to lower case using ".lower()""
x = "investment" #store the input 'investment' as 'x'
y = "bond"  #store the input 'bond' as 'y'

if choice == x: #if user inputs 'investment' do the following:
    print ("\nYou Have Chosen To Use The Investment Calculator.\nPlease Enter The Following: ") #intro to investments
    deposit = float(input("Amount You Want To Deposit: ")) #ask user to input amount they want to deposit and store.
    rate = float(input("Interest Rate: ")) #ask user to input the amount of interest they want and store.
    percent = rate / 100 #turns the interest rate into a percentage.
    year = float(input("Amount Of Year(s) You Want To Invest In: ")) #ask user to input the amount of years they want to invest in and store.
    
    print ("Do you want to calculate 'Simple Interest' or Compound Interest?")
    print ("\nSimple Interest - Interest you get depending on what you initially deposited per year e.g you deposited £1000 and your interest rate is at 10%, each year you will get £100 ")
    print ("Compound Interest - Interest you get depending on what you initially deposisted plus the your total interest earnings for that year e.g. you deposited £1000 and your interest rate is at 10% for 2years. Your first year you'll get £1100 and your second year you'll take that £1100 and plus 10% on that of that which equals to £1210 ")
    #intro to simple and compound interests
    
    interest = input ("\nWhat type of Interest would you like to calculate? Input Either 'Simple' or 'Compound'").lower() #asks user to input either simple or compound.
    s = "simple" #store 'simple' as a variable
    c = "compound" #store 'compound' as a variable

    simple = deposit * (1 + year * percent) #calculates simple interest
    compound = deposit * math.pow ((1 + percent), year) #calculates compound interest
    round_simple = round(simple,2) #rounds simple to 2 decimal places
    round_compound = round(compound, 2) #rounds compound to 2 decimal places
    
    if interest == s: #if user inputs 'simple' do the following:
        print ("_____________________________________")
        print (f"Deposit - \t£{deposit}")
        print (f"Interest - \t{rate}%")
        print (f"Year(s) - \t{year} year")
        print (f"Total - \t£{round_simple} ")
        print ("_____________________________________")
        #prints out a table showing you the following information: Deposit, Interest, Years and Total amount.
        
        
    if interest == c: #if user inputs 'compound' do the following:
        print ("_____________________________________")
        print (f"Deposit - \t£{deposit}")
        print (f"Interest - \t{rate}%")
        print (f"Year(s) - \t{year} year")
        print (f"Total - \t£{round_compound} ")
        print ("_____________________________________")
        #prints out a table showing you the following information: Deposit, Interest, Years and Total amount   .
         
    elif interest != s and c:
        print ("Error! You Did Not Enter 'Simple' Or 'Compound'.") #if user doesnt input 'simple' or 'compound' print this message.
        



if choice == y: #if user inputs 'bond' do the following:
    print ("\nYou Have Chosen To Use The 'Home Load Calculator'.\nPlease Enter The Following: ") #intro to bonds
    house = float(input("How Much Would You Like To Borrow For Your House: ")) #ask user to input the amount they want to borrow. store this
    rate = float(input("How Much Interest Do You Want To Apply: ")) #ask user to input the amount of interest they want apply and store.
    percent = rate / 100 #turns the interest rate into a percentage.
    month_interest = percent / 12 #turns the interest rate into months.
    month = int(input("How Many Month(s) Do You Plan To Take To Repay The Bond: ")) #ask user to input how long would they like to take to repay this ammount
    
    payment = (month_interest * house) / (1 - ( 1 + month_interest) ** (- month)) #calculates how much they would pay each month to repay back this bond.
    round_payment = (round(payment, 2)) #rounds payment to 2 decimal places
    
    
    print ("_____________________________________")
    print (f"Loan - \t\t\t£{house}")
    print (f"Interest - \t\t{rate}%")
    print (f"Month(s) To Repay - \t{month} Month(s)")
    print (f"Total - \t\t£{round_payment} per Month(s) ")
    print ("_____________________________________")
    #prints out a table showing you the following information: loan, interest, how many months they want the loan for and amount they need to pay each month.
    
elif choice != x and y:
    print ("Error! You Did Not Enter 'Investment' or 'Bond'.")
    #if user did not input 'investment' or 'bond' print this message.
