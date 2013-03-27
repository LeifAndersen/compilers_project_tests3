try:
  try:
    try:
      print("Begin...")
      raise Exception
    except:
      raise Exception
  except:
    raise Exception
except:
  print("Good!")
