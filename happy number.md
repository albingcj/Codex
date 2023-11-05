# Slow Fast Algorithm
## Question:
A number is said to be happy number if adding the squares of the digits end up giving 1. Some times we end up in a loop. So we use slow fast algorithm.
Here we set a pointer to the current number and 1 to the 1 after it. after recursively calling if we get the same number that means it is looping.
## Example
IP : ```19```
OP : ```TRUE```
## Code Python
```
def is_happy(n):
    def square_sum(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit ** 2
            num //= 10
        return total

    slow = n
    fast = n
    while True:
        slow = square_sum(slow)
        fast = square_sum(square_sum(fast))
        
        if slow == fast:
            break

    return slow == 1
```
