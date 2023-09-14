def hcf(a,b):
    if b == 0:
        return a;
    return hcf(b, a%b);
def lcm(a,b):
     return a*b // hcf(a,b)
print (lcm(10,20))
print (hcf(10,20))
