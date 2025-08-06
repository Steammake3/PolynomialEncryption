from itertools import zip_longest

def strip(L, v):
    if len(L) == 0:
        return L

    i = len(L) - 1
    while i >= 0 and L[i] == v:
        i -= 1

    return L[:i+1]


class Polynomial:

    def __init__(self, coef : list =[], field = int, manual : bool = True):
        self.coefficients = [field(i) for i in coef[::-1]] if manual else coef
        self.field = field
    
    def __repr__(self):
        return ' + '.join(['%s x^%d' % (a,i) if i > 0 else '%s'%a
                              for i,a in enumerate(self.coefficients)])

    def __str__(self):
        return self.__repr__()
    
    def eval(self, x):
        retval = self.field(0)
        for exp, val in enumerate(self.coefficients):
            if val: retval += val * pow(x, exp)
        
        return retval

    def __add__(self, other):
        retvalraw = [
            sum(x) for x in zip_longest(self, other, fillvalue=self.field(0))
        ]
        return Polynomial(retvalraw, self.field, manual = False)


    def __mul__(self, other):
        new_coefficients = [0] * (len(self) + len(other) - 1)

        for i, a in enumerate(self):
            for j, b in enumerate(other):
                new_coefficients[i+j] += a*b

        return Polynomial(strip(new_coefficients, 0), self.field, manual = False)

    def __iter__(self):
        return iter(self.coefficients)

    def __neg__(self):
        return Polynomial([-x for x in self], self.field, manual = False)

    def __sub__(self, other):
        return self + (-other)

    def __len__(self):
        return len(self.coefficients)
    
    def __call__(self, x):
        return self.eval(x)