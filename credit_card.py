''' Credit Card Calculator '''

''' Problem 1 - Paying the Minimum'''   
def min_payment(balance, r):
    
    min_payrate = float(input('Enter your minimum payment rate: '))
    total_payments = 0
    
    for i in range(1,13):
        
        month_payment = balance*min_payrate
        total_payments += month_payment 

        interest = balance*(r/12)
        principal = month_payment - interest
        balance = balance - principal
        
        print('Month: ', i)
        print('Minimum monthly payment: ', "%.2f" % round(month_payment,2))
        print('Principal paid: ', "%.2f" % round(principal,2))
        print('Remaining balance: ', "%.2f" % round(balance,2))      
    
    print('RESULT')    
    print('Total paid amount: ', "%.2f" % total_payments)
    print('Remaining balance: ', "%.2f" % round(balance,2))


''' Problem 2 - Paying Debt Off in a Year '''
def payoff_oneyear(balance, r):

    for guess in list(range(10,int(balance),10)):
        new_balance = balance
        num_payments = 0
        
        while new_balance > 0 and num_payments < 13: ##find number of months to payoff
            new_balance = new_balance*(1 + r/12) - guess
            num_payments += 1
            
        if num_payments < 13 and new_balance <= 0:
            break
        
    print('RESULT')    
    print('Monthly payment to pay off debt in 1 year: ', "%.0f" % guess)
    print('Number of months needed: ', "%.0f" % num_payments)
    print('Balance: ', "%.2f" % new_balance)
    
    
''' Problem 3 - Paying Off Debt in a Year with Bisection Search '''
def bisection(balance, r):
    low = balance/12
    high = (balance*(1 + r/12)**12)/12
    tolerance = .2
    
    while abs(balance) > tolerance:
        guess = (high + low)/2
        new_balance = balance
        
        for i in range(1,13):
            new_balance = new_balance*(1 + r/12) - guess
            
        if new_balance > 0:
            low = guess
        else:
            high = guess
    
    print('RESULT')    
    print('Monthly payment to pay off debt in 1 year: ', "%.0f" % guess)
    #print('Number of months needed: ', "%.0f" % num_payments)
    print('Balance: ', "%.2f" % new_balance) 
    
def main(): 

    balance = float(input('Enter your initial balance: '))
    r = float(input('Enter your annual credit card interest rate: '))
    program = int(input('Enter program number: '))

    if program == 1:
        min_payment(balance, r)
    elif program == 2:
        payoff_oneyear(balance, r)
    elif program == 3:
        bisection(balance, r)
    else:
        print('Not a valid program number.')

if __name__ == '__main__':
    main()
    