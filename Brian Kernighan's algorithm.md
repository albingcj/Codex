
# Brian Kernighan's algorithm 
For counting the number of set bits (1s) in an integer, also known as the Bit Counting Algorithm. 
This algorithm is a very efficient way to count the number of set bits in a binary number.

`O(log n)`


### Python
```
def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

number = 42 
result = count_set_bits(number)
print(f"Number of set bits in {number} is {result}")
```
