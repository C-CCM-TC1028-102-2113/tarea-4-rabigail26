def main():
    #escribe tu código abajo de esta línea
    pass
##promedio
suma=0
num=float(input('ingrese los digitos'))
cont=0
while num >0:
       suma= suma+num
       cont=cont+1
       num=float(input('ingrese los digitos'))
promedio=suma/cont
    
print(promedio)
if __name__=='__main__':
    main()
