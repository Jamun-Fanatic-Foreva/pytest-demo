def add(a,b):
	return (a+b)

def subtract(a,b):
	return (a-b)

def multiply(a,b):
	return (a*b)

def divide(a,b):
	assert b is not 0, 'ZeroError: b cannot be zero'
	return (a/b)

def main():
    while True:
        num = input('Enter numbers:  ')
        a,b = num.split(' ')
        a,b = float(a), float(b)
        print('Add = {}, Subtract = {}'.format(add(a,b), subtract(a,b)))
        print('Multiply = {0}, Divide = {1}'.format(multiply(a,b), divide(a,b)))
        
        ch = input('0 to quit, 1 to continue    ')
        if int(ch) == 0:
            break
        else:
           print("\033[H\033[J")
            
    print('Thank You!')


if __name__ == '__main__':
    main()