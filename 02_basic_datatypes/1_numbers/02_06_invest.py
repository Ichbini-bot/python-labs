'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

# Formula compound interest rate: Cn = Co * (1 + p / 100)^n

capital = float(input("Pls enter Investment Amount: "))
interest = float(input("Pls enter interst rate: "))
years = float (input("How man years would u like to invest your money: "))

future_value = capital * (1 + interest / 100) ** years

print(future_value)



