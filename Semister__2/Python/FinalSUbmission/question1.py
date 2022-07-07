# importing time module
import time

def primeNator(range_number):
    init_time = time.time()
    prime_lst = []
    for num in range(2,range_number+1):
        if num > 1:
            for i in range(2,num):
                if (num%i) == 0:
                    break
            else:
                prime_lst.append(num)
    final_time = time.time()
    return (final_time - init_time),prime_lst

while True:
    try:
        try:
            range_number = int(input("Enter the number : "))
            break
        except Exception:
            print("Please enter number only.")
    except KeyboardInterrupt:
        print("Enter the number and then enter.")

prog_execution_time,prime_numbers = primeNator(range_number)
print(f"The program took {prog_execution_time} seconds to generate prime numbers from 0 to {range_number}")