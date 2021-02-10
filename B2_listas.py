#listas
numeros =[1,2,3,4]
print (numeros)

numeroextra =33

numeros.append(numeroextra)
print (numeros)

numeros.pop()
print (numeros)

numeros.reverse()
print (numeros)

for x in numeros:
  print ("you have the number %d of %d" % (x, len(numeros)))
  print ("your number is at %d position" % numeros.index(x))
  print ("your number appears %d times" % numeros.count(x))
  
numeros[4]=1
print (numeros)
