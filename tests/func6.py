a = 3
def b(c):
 return c+3
def c(d): return d+a
def e(a,b,c): return c(a,b)
def q(b,c):
 return b(c)
def z(c): return b(a+c)

print(e(z,c(b(3)),q))
