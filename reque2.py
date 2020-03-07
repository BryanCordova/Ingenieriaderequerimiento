print("*********************************************")
print("*----------- Bienvenido Usuario ------------*")
print("*********************************************")
print("*         Digite  -1  para culminar         *")
print("*********************************************")
correcto=False
while (not correcto):
        try:
            a = float(input("Ingrese la Remuneracion Mensual del cliente: "))
            if a==-1:
                break
            grati = float(input("Ingrese la gratificacion total del cliente: "))
            if grati==-1:
                break
            if a<0 or grati<0:
                print(" ")
                print("La Remuneracion y Gratificacion deben ser positivos")
                print(" ")
                print("---------------------------------------------------")
                print(" ")
            else:
                c = a * 12 + grati
                if c > 29400:
                    NetAnual = c - 29400
                    UITs = NetAnual / 4300
                    # Cuando excede el 8%
                    subt1 = (5 * 4300) * 0.08
                    # Cuando excede el 14%
                    subt2 = subt1 + (20 * 4300 - 5 * 4300) * 0.14
                    # Cuando excede el 17%
                    subt3 = subt2 + (35 * 4300 - 20 * 4300) * 0.17
                    # Cuando excede el 20%
                    subt4 = subt3 + (45 * 4300 - 20 * 4300) * 0.20
                    if UITs <= 5:
                        impuesto = NetAnual * 0.08
                        print(" ")
                        print(" -> Remuneracion Bruta Anual: S/." + str(c))
                        print(" -> Remuneracion Neta Anual: S/." + str(NetAnual))
                        print(" -> Impuesto Anual Proyectado: S/." + str(impuesto))
                        print(" ")
                        print("--------------------------------------------------")
                        print(" ")
                    elif UITs > 5 and UITs <= 20:
                        dif = (NetAnual - 5 * 4300) * 0.14
                        impuesto = subt1 + dif
                        print(" ")
                        print(" -> Remuneracion Bruta Anual: S/." + str(c))
                        print(" -> Remuneracion Neta Anual: S/." + str(NetAnual))
                        print(" -> Impuesto Anual Proyectado: S/." + str(impuesto))
                        print(" ")
                        print("--------------------------------------------------")
                        print(" ")
                    elif UITs > 20 and UITs <= 35:
                        dif = (NetAnual - 20 * 4300) * 0.17
                        impuesto = subt2 + dif
                        print(" ")
                        print(" -> Remuneracion Bruta Anual: S/." + str(c))
                        print(" -> Remuneracion Neta Anual: S/." + str(NetAnual))
                        print(" -> Impuesto Anual Proyectado: S/." + str(impuesto))
                        print(" ")
                        print("--------------------------------------------------")
                        print(" ")
                    elif UITs > 35 and UITs <= 45:
                        dif = (NetAnual - 35 * 4300) * 20
                        impuesto = subt3 + dif
                        print(" ")
                        print(" -> Remuneracion Bruta Anual: S/." + str(c))
                        print(" -> Remuneracion Neta Anual: S/." + str(NetAnual))
                        print(" -> Impuesto Anual Proyectado: S/." + str(impuesto))
                        print(" ")
                        print("--------------------------------------------------")
                        print(" ")
                    else:
                        dif = (NetAnual - 45 * 4300) * 0.30
                        impuesto = subt4 + dif
                        print(" ")
                        print(" -> Remuneracion Bruta Anual: S/." + str(c))
                        print(" -> Remuneracion Neta Anual: S/." + str(NetAnual))
                        print(" -> Impuesto Anual Proyectado: S/." + str(impuesto))
                        print(" ")
                        print("--------------------------------------------------")
                        print(" ")
                else:
                    print(" ")
                    print(" El cliente no esta sujeto a retención")
                    print(" ")
                    print("----------------------------------------------")
                    print(" ")
        except ValueError:
            print(" Error: El valor ingresado debe ser un numero")
            print(" ")
            print("----------------------------------------------")
            print(" ")


