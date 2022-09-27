# a = 1
# b = 1
# a = a + b
# b = b + a 

d = {} #dictiinary for storing calculated values

def fib(n):
    if n in d: return d[n] #avoiding repeated calculating
    if n > 2:
        d[n] = fib(n-1) + fib(n-2)
        return d[n]
    elif n == 2 or n == 1: return 1
    else: return 'too small n'
    

print(fib(10))

class udict(dict): #subclass for 
    def __missing__(self, key): 
        val = self[key-1] + self[key-2]
        self[key] = val
        return val

e = udict()
e[1] = 1
e[2] = 1


print(e[330])


# fib(4)= fib(3) + fib(2)= fib(1)+fib(2)+fib(2)
# fib(5) = fib (4) + fib(2)+fib(1)