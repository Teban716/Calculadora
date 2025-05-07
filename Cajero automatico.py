banco=[]
def menu():
    while True:
        print('-----------------------------------------------')
        print("MENU")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Saldo")
        print("4. Salir")
        print('-----------------------------------------------')
        opcion = pedir_numero_positivo('Elige lo que deseas realizar:    ')
        print('-----------------------------------------------')
        if opcion == 1:
            depositar()
        elif opcion == 2: 
            retirar()
        elif opcion == 3:
            saldo()
        elif opcion == 4:
            break
        else:
            print('Numero Invalido')

def pedir_numero_positivo(prompt):
    while(True):
        try:
            numero = float(input(prompt))
            if numero > 0:
                return numero
            else:
                print("El numero no es positivo")
        except ValueError:
            print("El numero es invalido")

def depositar():
    depositar = pedir_numero_positivo("Ingrese su valor a depositar;    $")
    banco.append(depositar)
    suma = sum(banco)
    print("\nDEPOSITO EXITOSO")
    print(f"Se ha depositado ${suma}")

def retirar():
    if banco == 0:
        print("FONDOS INSUFICIENTE")
    retirar = pedir_numero_positivo("Cuanto vas a retirar:    $")
    if retirar > banco[0]:
        print("FONDOS INSUFICIENTE")
        menu()
    retirar_negativo = retirar * (-1)
    banco.append(retirar_negativo)
    suma = sum(banco)
    print("\n RETIRO EXITOSO")
    print(f"Se ha retirado ${suma}")

def saldo():
    print(banco)

menu()