
def main():
    #escribe tu código abajo de esta línea
    pass

indice= int(input("Dame el índice: "))
suma=0
inicio=1
while indice > 0:
    indice = indice-1
    suma=suma+inicio
    inicio=suma-inicio
print (suma)
if __name__=='__main__':
    main()
