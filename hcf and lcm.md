# HCF - Euclidean algorithm

## recursion method
```
def hcf(a, b):
    if b == 0:
        return a;
    return hcf(b, a%b);
```
## looping
```
def hcf(a, b):
    while b:
        a, b = b, a%b
    return a
```
# LCM
```
def lcm(a, b):
     return a * b // hcf(a, b)
```
