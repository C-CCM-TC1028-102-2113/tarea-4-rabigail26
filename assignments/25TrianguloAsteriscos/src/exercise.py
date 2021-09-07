
def main():
    #Escribe tu código debajo de esta línea
    pass
altura=int(input('dame la altura'))
asteriscos= "*"
espacio=" "



for i in range(altura):
    i=i+1
    area=i*asteriscos
    altura=altura-1
    n=altura*espacio 
    print(n,area)
    

if __name__=='__main__':
    main()
