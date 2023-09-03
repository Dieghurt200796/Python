#Challenges Website: https://projecteuler.net/archives
#Some problems have been skipped for lack of interest or ability to solve

#Problem 1
def output_problem1():
    addition=0

    for i in range(1000):
        if i%3==0:
            addition+=i
        elif i%5 ==0:
            addition+=i

    print(addition)
# output_problem1()

#Problem 2:
def output_problem2():
    x=1
    y=2
    fibonacci=3
    addition=2
    while fibonacci<4000000:
        x=y
        y=fibonacci
        fibonacci=x+y
        if y%2==0:
            addition+=y
    print(addition)
# output_problem2()

# Problem 3
def prime_factors_problem3(number : int):
    prime_factors = []
    new_number = number
    decomposed = False
    while not decomposed:
        multiplication_result = 1
        for i in range(int(new_number//2)):
            if new_number/(i+2) == new_number//(i+2):
                prime_factors.append((i+2))
                new_number = new_number/(i+2)
                break
            if i == (new_number//2 - 1):
                prime_factors.append(new_number)
        
        for i in prime_factors:
            multiplication_result*=i
        
        if multiplication_result == number:
            decomposed = True
            
    return prime_factors
def output_problem3():
    number = int(input("Input an integer\n"))
    prime_factors = prime_factors_problem3(number)
    max_factor = max(prime_factors)

    return max_factor
# print(int(output_problem3()))

#Problem 4
def output_problem4():
    a=100
    b=100
    largest_palindrome=0

    for i in range(900):
        a+=1
        b=100
        for j in range(900):
            b+=1
            num=a*b
            rev_num=0
            while num>0:
                rev_num=rev_num*10+num%10
                num=num//10
            if a*b==rev_num:
                if largest_palindrome<a*b:
                    largest_palindrome=a*b


    print(largest_palindrome)
# output_problem4()

#Problem 5
def output_problem5():
    smallest_multiple=0
    divisible=0
    x=0
    while divisible<20:
        smallest_multiple+=2*3*5*7*11*13*17*19 #multiply by all prime numbers from 1-20
        divisible=0
        x+=1
        for i in range(20):
            if smallest_multiple%(i+1)==0:
                divisible+=1
        if x>=1000000:
            x=0
            print(smallest_multiple)
    print(smallest_multiple)
# output_problem5()

#Problem 6
def output_problem6():
    x=0
    y=0
    temp_number=0
    sum_of_squares=0
    square_of_sums=0

    for i in range(100):
        x+=1
        y+=1
        temp_number+=y
        sum_of_squares+=x**2
    square_of_sums=temp_number**2
    print(square_of_sums-sum_of_squares)
# output_problem6()

# Problem 7:
def prime_finder_problem7(limit : int):
    prime = True
    primes = []
    number = 2
    while len(primes) < limit:
        is_prime = True
        for prime in primes:
            if number%prime == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(number)
        
        number+=1


    return primes
def output_problem7():
    primes = prime_finder_problem7(10001)
    last_prime = primes[-1]

    return last_prime
# print(output_problem7())

# Problem 8:
def output_problem8():
    number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    number_digits = []
    max_multiplication = 0
    multiplication = 1
    for digit in str(number):
        number_digits.append(int(digit))
    
    for i in range(len(number_digits)-13):
        multiplication = 1
        for j in range(13):
            multiplication*=number_digits[i+j]
        if multiplication>max_multiplication: max_multiplication = multiplication
    
    return max_multiplication
# print(output_problem8())

# Problem 9:
def output_problem9():
    solution_found = False
    a=1
    b=2
    c=3

    while not solution_found:
        for i in range(332):
            for j in range(499):
                for k in range(997):
                    a=i+1
                    b=j+1
                    c=k+1
                    if a+b+c == 1000 and a**2 + b**2 == c**2:
                        return a*b*c
# print(output_problem9())

# Problem 10: TRY TO MAKE MORE EFFICIENT?
def output_problem10():
    primes_below = 2_000_000
    primes = []
    for i in range(primes_below):
        prime = True
        if i > 1:
            for number in primes:
                if i % number == 0:
                    prime = False
                    break
            if prime: primes.append(i)
    return sum(primes)
# print(output_problem10())

# Problem 11:
def format_grid_problem11():
    grid = []
    print("Enter grid, manually separating rows or pasting grid with pre-separated rows")
    for _ in range(20):
        grid.append(input().split(sep=' '))
    for i in range(20):
        for j in range(20):
            grid[i][j]=int(grid[i][j])
    return grid
def output_problem11():
    grid = format_grid_problem11()
    max_product = 0
    # Find products in horizontal line
    for i in range(len(grid)):
        for j in range(len(grid[i])-3):
            product = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
            if max_product < product: max_product = product
    # Find products in vertical line
    for i in range(len(grid)-3):
        for j in range(len(grid[i])):
            product = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
            if max_product < product: max_product = product
    # Find products in diagonal (left to right)
    for i in range(len(grid)-3):
        for j in range(len(grid[i])-3):
            product = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
            if max_product < product: max_product = product
    # Find products in diagonal (right to left)
    for i in range(len(grid)-3):
        for j in range(len(grid[i])-3):
            product = grid[i][j + 3] * grid[i + 1][j + 2] * grid[i + 2][j + 1] * grid[i + 3][j]
            if max_product < product: max_product = product

    return max_product
# print(output_problem11())


#Problem 16
def output_problem16():
    x=2**1000
    sum=0
    number=0
    x_str=str(x)
    for i in range(len(str(x))):
        y=int(x_str[i])
        number=int(y)
        sum+=number
    print(sum)
# output_problem16()

#Problem 19
def output_problem19():
    day=1
    month=1
    year=1901
    letter_day_number=2
    letter_day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    x=0
    while year<2001:
        if day==1 and letter_day_number==7:
            print(letter_day)
            x+=1
        if month==12 and day==31:
            month=1
            day=1
            year+=1
        elif (month==9 or month==4 or month==6 or month==11) and day==30:
            month+=1
            day=1
        elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10) and day==31:
            day=1
            month+=1
        elif month==2 and day==28 and year%4!=0:
            month+=1
            day=1
        elif month==2 and day==29 and year%4==0:
            month+=1
            day=1
        else:
            day+=1
        if letter_day_number!=7:
            letter_day_number+=1
        else:
            letter_day_number=1
    print(x)
# output_problem19()

#Problem 20
def output_problem20():
    factorial_number=100
    factorial_solution=1
    addition_of_values=0
    while factorial_number>0:
        factorial_solution*=factorial_number
        factorial_number-=1
    str_factorial=str(factorial_solution)
    for i in range(len(str_factorial)):
        addition_of_values+=int(str_factorial[i])
    print(addition_of_values)
# output_problem20()