# • Sistema que verifica o seu signo

# • Entrada

print('\n\t\t • Horóscopo • \n\t\t')

dia = int(input("Informe o dia em que você nasceu: \n").strip())
mês = int(input("Informe o mês em que você nasceu: \n").strip())

# Processamento

if dia>=20 and dia<=31 and mês==3 or dia>=1 and dia<=20 and  mês==4:
   print ("Seu signo é: Áries!")
elif dia>=21 and dia<=30 and mês==4 or dia>=1 and dia<=20 and mês==5:
   print ("Seu signo é: Touro!")
elif dia>=21 and dia<=31 and mês==5 or dia>=1 and dia<=20 and mês==6:
   print ("Seu signo é: Gêmeos!")
elif dia>=21 and dia<=30 and mês==6 or dia>=1 and dia<=21 and mês==7:
   print ("Seu signo é: Cancer!")
elif dia>=22 and dia<=31 and mês==7 or dia>=1 and dia<=22 and mês==8:
   print ("Seu signo é: Leão!")
elif dia>=22 and dia<=31 and mês==8 or dia>=1 and dia<=22 and mês==9:
   print ("Seu signo é: Virgem!")
elif dia>=22 and dia<=30 and mês==9 or dia>=1 and dia<=22 and mês==10:
   print ("Seu signo é: libra!")
elif dia>=23 and dia <=31 and mês==10 or dia>=1 and dia<=21 and mês==11:
   print ("Seu signo é: Escorpiao!")
elif dia>=22 and dia<=30 and mês==11 or dia>=1 and dia<=21 and mês==12:
   print ("Seu signo é: Sagitário!")
elif dia>=22 and dia<=31 and mês==12 or dia>=1 and dia<=20 and mês==1:
  (print ("Seu signo é: Capricornio!"))
elif dia>=21 and dia<=31 and mês==1 or dia>=1 and dia<=18 and mês==2:
  print ("Seu signo é: Aquario!")
elif dia>=19 and dia<=29 and mês==2 or dia>=1 and dia<=19 and mês==3:
  print ("Seu signo é: Peixes!")
else:
  print ("mês ou dia invalido!")
