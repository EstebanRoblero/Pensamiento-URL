
# Número de días a registrar
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes",]
niveles_azucar = [130, 160, 95, 175, 160] # mg/dL
niveles_sal = [2000, 2400, 1800, 2400, 2700] # mg
presion = [115, 130, 110, 125, 175] # mmHg
diastolica =[75, 85,70, 78, 95]

#sangre
def la_azucar (nivel):
    if 70<= nivel <= 140:
        return "saludable normal prueba de sangre "
    else:
        return "fuera del rango de la sangre "


def la_sal (nivel):
    if nivel <=2300:
        return "sal estable"
    else:
        return "mucha sal en exceso"
    

def clasificar_presion(sistolica, diastolica=80):
    if sistolica <120 and diastolica <80:
        return "BIEN NORMAL"
    elif 120 <= sistolica <= 129 and diastolica <80:
        return "ELEVADA"
    elif 130 <= sistolica <=139 or 80 <= diastolica <=89:
        return "ETAPA 2 DE HIPERTENSION"
    else:
        return "ES INDEFINIDO"


print(" -----------EVALUACION DIRAIRA----------- SIUUUUUUUU")

print()

for i in range(len(dias)):
    azuar= la_azucar(niveles_azucar[i])
    sall= la_sal (niveles_sal[i])
    presionn= clasificar_presion(presion[i], diastolica[i])

    print(f"{dias[i]}:  ")
    print(f" Azucar: {niveles_azucar[i]} en mg(dl ) == {azuar}")
    print(f" La sal: {niveles_sal[i]} en mg== {sall}")
    print(f" la presion: {presion[i]}/ {diastolica[i]} en mmHg =={presionn}")

    if azuar != "saludable normal" or  sall != "sal estable" or presionn != "BIEN NORMAL":
        print("  EYY ALERTAAA!! ESTE PAREMETRO ESTA FUERA DE SALUDABLE")
    print()
    print()



promedio_azu =sum(niveles_azucar)/ len (niveles_azucar)
promedio_sa= sum (niveles_sal)/ len  (niveles_sal)
promedio_pre=sum (presion)/ len (presion)
promedio_dia=sum (diastolica)/ len (diastolica)


print("--------------------- LOS PROMEDIO FINALES-------------------- SIUUUUU")
print(f" LA AZUCAR EL PROEMDIO ES: {promedio_azu:.1f} en mg/dL")
print(f" EL PROMEDIO DE SAL ES: {promedio_sa:.1f} en mg")
print(f" EL PROMEDIO DE PRESION ES: {promedio_pre:.1f}/{promedio_dia:.1f} en mmHg")




