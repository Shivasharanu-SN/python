# 1. print Hello World

print("Hello World")

# 2. Check Even or Odd

def isEven(num):
    if num%2 == 0:
        return True
    return False

# 3. Find the largest of three numbers

def largest_of_three_numbers(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    

# 4. Factorial of a number 

def factorial_iterative(num):
    total = 1
    for i in range(1,num+1):
        total *= i
    return total

def factorial_recursive(num):
    if num==0 and num==1:
        return 1
    return num * factorial_recursive(num-1)


# 5. Fibonacci series
# 0,1,1,2,3,5,8

def fibonacci_iterative(num):
    a, b = 0,1
    for i in range(num):
        print(a, end=" ")
        a,b = b,a+b
        

# 6. Check Prime Number 

def check_prime(num):
    if num <= 1 :
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

# 7. Reverse a string 

def reverse(text):
    n = len(text)
    text1 = ''
    for i in range(n-1,-1,-1):
        text1 += text[i] 

    return text1

# 8. Sum of digits

def sum_of_digits(num):

    total = 0
    while num > 0:
        total += num%10
        num = num//10
    return total

# 9. Check if a string is palindrome

def check_is_text_palindrome(text):
    """palindrome text is a text which is same when read in both directions eg: MADAM"""
    n = len(text)
    for i in range(n//2):
        if text[i] != text[n-1-i]:
            return False
    return True

# 10. Check if a number is palindrome

def check_is_number_palindrome(num):
    num1,num2 = 0,num
    while num > 0:
        num1 = num1*10 + num%10
        num = num//10
    
    if num1 == num2:
        return True
    return False

