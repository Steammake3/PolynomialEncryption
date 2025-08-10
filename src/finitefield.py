def eGCD(a, b):
   if abs(b) > abs(a):
      (x,y,d) = eGCD(b, a)
      return (y,x,d)

   if abs(b) == 0: return (1, 0, a)

   x1, x2, y1, y2 = 0, 1, 1, 0
   while abs(b) > 0:
      q, r = divmod(a,b)
      x = x2 - q*x1
      y = y2 - q*y1
      a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y

   return (x2, y2, a)

def isprime(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

def GF(p):
   class IntegerModP:
        def __init__(self, n):
            self.n = n % p
            self.field = IntegerModP

        def __neg__(self): return IntegerModP(-self.n)
        def __eq__(self, other): return isinstance(other, IntegerModP) and self.n == other.n
        def __abs__(self): return abs(self.n)
        def __str__(self): return str(self.n)
        def __int__(self): return self.n
        def __repr__(self): return '%d (mod %d)' % (self.n, self.p)
        def __pow__(self, exp): return IntegerModP(pow(self.n, exp, self.p))

        def __divmod__(self, divisor):
            q,r = divmod(self.n, divisor.n)
            return (IntegerModP(q), IntegerModP(r))

        def inverse(self):
            return IntegerModP(pow(self.n, self.p-2, self.p))

        def __add__(self, other):
            return IntegerModP(self.n + other) if isinstance(other, int) else IntegerModP(self.n + other.n)
        def __sub__(self, other):
            return IntegerModP(self.n - other) if isinstance(other, int) else IntegerModP(self.n - other.n)
        def __mul__(self, other):
            return IntegerModP(self.n * other) if isinstance(other, int) else IntegerModP(self.n * other.n)
        def __div__(self, other):
            return self*IntegerModP(other).inverse() if isinstance(other, int) else self * other.inverse()

        def __radd__(self, other):
            return IntegerModP(self.n + other) if isinstance(other, int) else IntegerModP(self.n + other.n)
        def __rsub__(self, other):
            return IntegerModP(other - self.n) if isinstance(other, int) else IntegerModP(other.n - self.n)
        def __rmul__(self, other):
            return IntegerModP(self.n * other) if isinstance(other, int) else self * other
        def __rdiv__(self, other):
            return IntegerModP(other%self.p)*self.inverse() if isinstance(other, int) else other * self.inverse()

        def __mod__(self, other):
            return self.n % other
        def __rmod__(self, other):
            raise TypeError("Do not use Galois Fields as divisors for modulus!! >:(")

   IntegerModP.p = p
   IntegerModP.__name__ = 'Z/%d' % (p)
   if not isprime(p): raise ValueError("p must be prime!!!!!!!!!!!!!")
   return IntegerModP