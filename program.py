# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

result = ""
x = 0
for myNumber in range(32):
  x = myNumber+1
  if x == 1:
    result = str("1") + "\n"
  elif x % 15 == 0:
    result = str(result) + "FizzBuzz\n"
  elif x % 3 == 0:
    result = str(result) + "Fizz\n"
  elif x % 5 == 0:
    result = str(result) + "Buzz\n"
  else:
    result = str(result) + str(x) + "\n"

print(result)
