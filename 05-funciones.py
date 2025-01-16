import os


def funcion1():
    os.system("cls")
    num1=int(input('Numero1: '))
    num2=int(input('Numero2: '))

    suma= num1+num2


    print(f'Resultado: {res}')

    input("Regresar a Menu")




def funcion2():
    os.system("cls")
    num1=int(input('Numero1: '))
    num2=int(input('Numero2: '))

    res= nu-num2


    print(f'Resultado: {res}')

     input("Regresar a Menu")



def funcion3():
    os.system("cls")
    num1=int(input('Numero1: '))
    num2=int(input('Numero2: '))

    res= num1*num2

    print(f'Resultado: {res}')

     input("Regresar a Menu")



def funcion4():
    num1=int(input('Numero1: '))
    num2=int(input('Numero2: '))

    res= num1/num2

    print(f'Resultado: {res}')

     input("Regresar a Menu")


def funcion5():
    os.system("cls")
    print("Salir")


#elif es para declarar y verificar que la condicion es verdadera o se este cumpliendo 

def run():
    os.system("cls")
    print('1. suma')
    print('2. resta')
    print('3. multiplicacion')
    print('4. divicion')
    print('5. salir')
    op=int(input('Opcion: '))
    elif op==1:
        funcion1()

    elif op==2:
        funcion2()   
    
    elif op==3:
        funcion3()
    
    elif op==4:
        funcion4()

    elif op==5:
        funcion5()


        break
    else:
        print('Por favor seleccione una opcion correcta')
         input("continuar")




#run()

if __name__=="__main__":
    run()


