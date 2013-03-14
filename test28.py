a = 3
def b():
 a = 4
 def c():
  a = 5
  def d():
   print(a)
  d()
 c()
 print(a)
b()

