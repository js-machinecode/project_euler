# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

def largest_prime_factor(n):
  '''Returns the largest prime factor of n.'''
  
  # begin largest_prime at 1
  largest_prime = 1
  
  # Try every possible factor from 2 to sqrt(n).
  # If n has a factor larger than sqrt(n), then it must have a matching factor smaller than sqrt(n).
  
  for i in range(2, math.isqrt(n)+1):
    # while i divides n evenly, reassign n to n//i. 
    # This reduces n by every factor of i.
    while n % i == 0:
      # assign i to largest_prime, since i is a factor of n and is larger than the previous largest_prime.
      largest_prime = i
      n //= i
      
  # check to see if n is greater than 1. 
  if n > 1:
     # If n is greater than 1, then n itself is the largest prime factor of the original number.
     largest_prime = n

  return largest_prime

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
    print(largest_prime_factor(13))