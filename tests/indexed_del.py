def f(x):
  print(x)
  return {"foo": [1, 2, 3]}

print(f(3))

i = 1
del f(3)["foo"][i]
