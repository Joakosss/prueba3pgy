import funcione as fu
fu.os.system("cls")


while True:
    try:
        fu.limpiarpantalla()
        fu.printv("""San Charlis
1)Registrar
2)Buscar 
3)Certificados
4)Salir""")
        opcion=int(input("Selecione: "))

        if opcion==1:
            fu.printv("Registrar")
            rut=int(input("Ingrese rut (sin dv ni puntos):"))
            fu.op1(rut)
        elif opcion==2:
            fu.printv("Buscar")
            rut=int(input("Ingrese rut que desea buscar (sin dv ni puntos):"))
            fu.op2(rut)
        elif opcion==3:
            fu.printv("Certificados")
            rut=int(input("Ingrese rut que desea buscar (sin dv ni puntos):"))
            if fu.buscarrut(rut)==2:
                fu.printr("Rut no encontrado")
            else:
                fu.printv("""1)Anotaciones 
2)Certificado de notas 
3)Certificado de alumno regular""")
                opcion=int(input("Selecione: "))

                if opcion==1:
                    fu.printv("Anotaciones")
                    fu.op3_1(rut)
                elif opcion==2:
                    fu.printv("Certificado de notas")
                    fu.op3_2(rut)
                elif opcion==3:
                    fu.printv("Certificado de alumno regular")
                    fu.op3_3(rut)
                else:
                    fu.printr("Opcion no valida")
        elif opcion==4:
            fu.printv("Salir")
            fu.salida()
            break
    except:
        fu.printr("Error, reintente")