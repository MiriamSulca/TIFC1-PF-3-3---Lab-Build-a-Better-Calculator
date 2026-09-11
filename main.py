def main():
  print("Hello learners!")

#Funcion de addmultiplenumbers([num, num, ..])
def addmultiplenumbers(numbers):
  response = 0
  for number in numbers:
      response = response + number
  return response
  
#Funcion de multiplymultiplenumbers([num, num, ..])
def multiplymultiplenumbers(numbers):
  response = 1
  for number in numbers:
      response = response * number
  return response

#Funcion isiteven(num)
def isiteven(num):
    if isitaninteger(num) and num % 2 == 0:
        return True
    else:
        return False

#Funcion isitaninteger(num)
def isitaninteger(num):
    if num == int(num):
        return True
    else:
        return False
    
def main():
   print("Hello learners!")
   print(addmultiplenumbers([10,9,23]))
   print (multiplymultiplenumbers([5,6,7]))
   print (isiteven(3))
   print(isitaninteger(2))
if __name__=="__main__":
  main()
if __name__=="__main__":
  main()
