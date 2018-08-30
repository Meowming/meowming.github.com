def fib(n):
    assert n>=0, 'fib cannot have negative n('+str(n)+')'
    if    n == 0: return 1
    elif  n == 1: return 1
    else:         return fib(n-1) + fib(n-2)


class Count_Argument_Use:
    def __init__(self,func):
        self.func = func
        self.dict = {}

    def __call__(self,argu):
        if argu in self.dict:
            self.dict[argu] = self.dict[argu] + 1
        else:
            self.dict[argu] = 1
        return fib(argu)

x = Count_Argument_Use(fib)
print(x(10))
print(x.dict)
