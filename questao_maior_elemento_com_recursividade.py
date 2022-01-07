def maior(array):
  if len(array) == 0:
    print("Array vazio!")
  elif len(array) == 1:
    return array[0]
  else:
    num1 = array[0]
    num2 = maior(array[1:])
    if num1 > num2:
      return num1
    else:
      return num2
