# tests multi-assignment with repeated lvals, mixed-scope lvals and indexed lvals
a = "a"
b = [{ "a" : [{ "b" : [{ "c" : [{ "d" : [{"e" : [1,2,3,4] }]}]}]}]}]
c = "old c"
d = { "a" : { "b" : [1] } }

def func(a):
  global b, c, d
  
  e = b
  print(e[0]["a"][0]["b"][0]["c"][0]["d"][0]["e"][1])
  
  a,b[0]["a"][0]["b"][0]["c"][0]["d"][0]["e"][1],c,d["a"]["b"][0],c,e  = "A","b","c",3*100+d["a"]["b"][0],"new c", 1
  
  print(a)
  print(b[0]["a"][0]["b"][0]["c"][0]["d"][0]["e"][1])
  print(c)
  print(e)
  
  return a

result = func(a)
print(a)
print(d["a"]["b"][0])
print(result)
