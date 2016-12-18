''' Credit Card Calculator '''

''' Problem 1 '''   
def main(): 
    balance = float(input('Enter your initial balance: '))
    r = float(input('Enter your annual credit card interest rate: '))
    min_payrate = float(input('Enter your minimum payment rate: '))
    
    total_payments = 0
    
    for i in range(1,13):
        
        month_payment = balance*min_payrate
        total_payments += month_payment 
#        balance = pay_cycle(balance)
        
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

if __name__ == '__main__':
    main()