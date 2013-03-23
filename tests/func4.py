a = 3
def b():
 global a
 a = 2
 def b():
  a = 4
  def b():
   nonlocal a
   a = 5
   def b():
    a = 6
    print(a)
   print(a)
   b()
   print(a)
  print(a)
  b()
  print(a)
 print(a)
 b()
 print(a)
print(a)
b()
print(a)

