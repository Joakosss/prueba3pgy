import os, msvcrt, numpy, random
from colorama import Fore
filas=50
colegio=numpy.empty([filas,7],object)
#.append
encontrado=0
anotaciones=[]
anotaciones.append ("Estudiante come en clases")
anotaciones.append ("Estudiante molesta a sus compañeros")
anotaciones.append ("Estudiante sale de la sala sin autorizacion")
anotaciones.append ("Estudiante no quiere ingresar a clases")
anotaciones.append ("Estudiante rompe celular de compañero")
anotaciones.append ("Estudiante rompe una ventana")
anotaciones.append ("Estudiante trata de 'OJALA TE MUERAS' a su compañera")
anotaciones.append ("Estudiante raya mesa de su compañera")
anotaciones.append ("Estudiante insulta al profesor en practica")
anotaciones.append ("Estudiante no trae materiales")
anotaciones.append ("Estudiante se come la colacion de su compañera")



def printr(texto):
    print(f"{Fore.RED}{texto}{Fore.RESET}")
def printv(texto):
    print(f"{Fore.GREEN}{texto}{Fore.RESET}")
def printa(texto):
    print(f"{Fore.YELLOW}{texto}{Fore.RESET}")
def printazul(texto):
    print(f"{Fore.BLUE}{texto}{Fore.RESET}")

def limpiarpantalla():
    printa(">>>>>>>>PRESIONE PARA CONTINUAR<<<<<<<<<")
    msvcrt.getch()
    os.system("cls")

def validar(rut):
    for y in range(filas):
        if colegio[y,0]==rut:
            #rut ya registrado
            return 2
        else:
            #rut no registrado pasa
            return 1

def espacio():
    for y in range(filas):
        if colegio[y,0]==None:
            return 1 #1 hay espacio
        else:
            return 2 #no hay espacio

def buscarrut(rut):
    for y in range(filas):
        if colegio[y,0]==rut:
            return 1 #1 rut encontrado
        else:
            return 2 #rut no encontrado


def op1(rut):
    if espacio==2:
        printr("No hay espacio disponible")
    else:
        printv(f"Registrando {rut}")
        nombre=str(input("Ingrese nombre: ")).capitalize()
        while len(nombre)<=1 or len(nombre)>=31:
            nombre=str(input("Reintente, ingrese nombre valido: ")).capitalize()  
        edad=int(input("Ingrese edad: "))
        while edad<=3:
            edad=int(input("Reintente, ingrese edad valida (mayor 4 años): "))
        genero=int(input("""1)Femenino
2)Masculino
3)Otro
Ingrese genero: """))
        while genero<=0 or genero>=4:
            genero=int(input("Reintente, ingrese genero: "))
        prom=float(input("Ingrese promedio (formato: 5.9): "))
        fecha=input("Ingrese fecha matricula (dia/mes/año): ")
        apoderado=str(input("Ingrese nombre apoderado: ")).capitalize()

        for y in range(filas):
            colegio[y,0]=rut
            colegio[y,1]=nombre
            colegio[y,2]=edad
            colegio[y,3]=prom
            colegio[y,4]=fecha
            colegio[y,6]=apoderado
            if genero==1:
                colegio[y,5]="Femenino"
            elif genero==2:
                colegio[y,5]="Masculino"
            elif genero==3:
                colegio[y,5]="Otro"
            break

def op2(rut):
    if buscarrut(rut)==2:
        printr("Rut no encontrado")
    else:
        for y in range(filas):
            if colegio[y,0]==rut:
              printazul (f"""Rut:\t\t\t{colegio[y,0]}
Nombre:\t\t\t{colegio[y,1]}      
Edad:\t\t\t{colegio[y,2]}
Genero:\t\t\t{colegio[y,5]}
Promedio:\t\t{colegio[y,3]}
Fecha matricula:\t{colegio[y,4]}
Apoderado:\t\t{colegio[y,6]}
""")

def op3_2(rut):
    for y in range(filas):
         if colegio[y,0]==rut:
            printazul(f"""Certificado de notas
---------------------------------------------
{colegio[y,1]} rut: {colegio[y,0]}
---------------------------------------------
Lenguaje\t{random.randrange(2,7)}
Matematicas\t{random.randrange(2,7)}
Ingles\t\t{random.randrange(2,7)}
Ciencias\t{random.randrange(2,7)}
Artes\t\t{random.randrange(2,7)}
Ed Fisica\t{random.randrange(2,7)}""")

def op3_1(rut):
    for y in range(filas):
        if colegio[y,0]==rut:
            printazul(f"""Anotaciones
---------------------------------------------
{colegio[y,1]} rut: {colegio[y,0]}
---------------------------------------------""")
            pase=random.randrange(0,2)
            if pase==1 or pase==2:
                printazul(anotaciones[(random.randint(0,10))])
                pase=random.randrange(0,2)
                if pase==1 or pase==2:
                    printazul(anotaciones[(random.randint(0,10))])
                    pase=random.randrange(0,2)
                    if pase==1:
                        printazul(anotaciones[(random.randint(0,10))])
                        pase=random.randrange(0,1)
                        if pase==1:
                            printazul(anotaciones[(random.randint(0,10))])
                            pase=random.randrange(0,1)
            else:
                printazul("Estudiante no cuenta con anotaciones")

def op3_3(rut):
    for y in range(filas):
         if colegio[y,0]==rut:
            printazul(f"""Certificado alumno regular
---------------------------------------------
Ministerio de eduacion certifica que estudiante
{colegio[y,1]} rut {colegio[y,0]} 
estudia en el colegio San Charlis
---------------------------------------------""")
def salida():
    printr("Hasta la proxima")
    

