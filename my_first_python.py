"""
FizzBuzz
"""
# count = 0
# while (count < 101):
#     if (count % 5) == 0 and (count % 3) == 0:
#         print ("FizzBuzz")
#         count = count +1
#     elif (count % 3) == 0:
#         print ("Fizz")
#         count = count + 1
#     elif (count % 5) == 0:
#         print ("Buzz")
#         count = count +1
#     else:
#         print (count)
#         count = count + 1

"""
Even Fibonacci
"""
# a = 0
# b = 1
# add_these = []
#
# while b <= 4000000:
# 	if b % 2 == 0:
# 		print(b)
# 		add_these.append(b)
# 	a = b
# 	b = a + b
#
# total = sum(add_these)
# print(total)

"""
Largest Prime Number
"""
primes = []
for num in range(2,15):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           primes.insert(0, num)

print(primes[0])
