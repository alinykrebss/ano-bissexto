#multiplo de 4 
#nao pode ser divisivel por 100 a nao ser que seja por 400

ano = float(input("me informe um ano "))

if (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
    print(" eh bissexto")

else:
 print ("nao eh bissexto")
 