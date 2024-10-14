#
# Exercise 8
# Write a program to print the inputted value as it is and break the loop if the value is 'done'.
# Example run of the program
# :hello there
# hello there
# :finished
# finished
# :done
# Done

# while True:
#     user_input = input(":")
#     if user_input.lower() == 'done':
#         print("Done")
#         break
#     else:
#         print(user_input)

# Exercise 9
# Write a program that prints the numbers from 1 to 20. But for multiples of three print "Fizz"instead of the number
# and for the multiple of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"

# for i in range(1,21):
#     if i%3==0 and i%5==0 :
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)


# Exercise 10
# Write a program to print the following pattern:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# i=5
# while(i>0):
#     j=i
#     while(j>0):
#         print(j,end=" ")
#         j-=1
#     print()
#     i-=1