''' Compute the nth root of a real number '''

def nth_root(epsilon, n, x):
    
    low = 0
    high = x
    g = (high - low) / n
    
    while abs(g**n - x) > epsilon and g < x:
        if g**n > x:
            high = g
        else:
            low = g
            
        g = (high + low)/2
            
    return g


def main():
    
    epsilon = float(input('Margin of error:'))
    n = float(input('Nth Root:'))
    x = float(input('Number:'))
    print(nth_root(epsilon, n, x))
    
if __name__ == '__main__':
    main()