#Programa que calcula el indice de masa corporal de una persona
print("  ______________________________________________________\n")
print("|\tCALCULADORA DE INDICE DE MASA CORPORAL")
print("  ______________________________________________________")
#creamos una funcion llamada val_n para validar si son letras lo que esta ingresando 
def val_n():
    return nombre
while True: 
    #Le pedimos al usuario que ingrese su nombre y lo guardamos en la variable edad
    nombre = input("| Ingrese su nombre: " )
    #validamos si la cadena es alfabetica y si no mostrar un mensaje
    if nombre.isalpha() :
        break
    else:
        print("| Error es un numero o esta vacio")    
#Fin de la funcion
#creamos una funcion llamada val_a_p para validar si son letras lo que esta ingresando 
def val_a_p():
    return a_p
while True: 
    #Le pedimos al usuario que ingrese su nombre y lo guardamos en la variable edad
    a_p = input("| Ingrese su apellido paterno: " )
    #validamos si la cadena es alfabetica y si no mostrar un mensaje
    if a_p.isalpha() :
        break
    else:
        print("| Error es un numero o esta vacio")    
#Fin de la funcion
#creamos una funcion llamada val_a_m para validar si son letras lo que esta ingresando 
def val_a_m():
    return a_m
while True: 
    #Le pedimos al usuario que ingrese su nombre y lo guardamos en la variable edad
    a_m = input("| Ingrese su apellido materno: " )
    #validamos si la cadena es alfabetica y si no mostrar un mensaje
    if a_m.isalpha() :
        break
    else:
        print("| Error es un numero o esta vacio")    
#Fin de la funcion
#creamos una funcion llamada val_edad para validar si es un numero lo que esta ingresando 
def val_edad():
    return edad
while True: 
    try:
        #Le pedimos al usuario que ingrese su altura y lo guardamos en la variable edad
        edad = int(input("| Ingrese su edad en años: " ))
        #validamos si es un numero positivo de lo contrario ingresar hasta que sea positivo
        if int(edad) > 0:
            break
        else:           
            print ("| Error escribe un numero positivo")     
    except ValueError:
            print("| Error no es un numero ingresar nuevamente")
#Fin de la funcion
#creamos una funcion llamada val_altura para validar si es un numero lo que esta ingresando 
def val_altura():
    return altura
while True: 
    try:
        #Le pedimos al usuario que ingrese su altura y lo guardamos en la variable altura
        altura = float(input("| Ingrese su altura en metros: " ))
        #validamos si es un numero positivo de lo contrario ingresar hasta que sea positivo
        if int(altura) > 0:
            break
        else:           
            print ("| Error escribe un numero positivo")     
    except ValueError:
            print("| Error no es un numero ingresar nuevamente")
#Fin de la funcion
#creamos una funcion llamada val_peso para validar si es un numero lo que esta ingresando 
def val_peso():
    return peso
while True: 
    try:
        #Le pedimos al usuario que ingrese su peso y lo guardamos en la variable peso
        peso = float(input("| Ingrese su peso en Kilogramos: "))
        #validamos si es un numero positivo de lo contrario ingresar hasta que sea positivo
        if int(peso) > 0:
            break
        else:           
            print ("| Error escribe un numero positivo")  
    except ValueError:
        print("| Error no es un numero ingresar nuevamente")
#Fin de la funcion
#Mandamos a llamar a la funcion
val_n()
val_a_p()
val_a_m()
val_edad()
val_altura()
val_peso()
#Calculamos el indice de masa corporal dividiendo peso entre su altura al cuadrado y lo guardamos en la variable imc
imc = peso/altura**2
#Validamos si es mayor de edad o no
if(edad < 18):
    print("| Usted es menor de edad")
else:
    print("| Usted es mayor de edad")
#Validamos su imc y en que categoria esta
if imc >= 0 and imc<= 18.99:
#imprimmos su nombre, edad, altura, peso y el resultado del calculo de su indice de masa corporal
    print(f"| Datos que ingreso Nombre completo : {nombre} {a_p} {a_m} y su edad es: {edad} años")
    print(f"| Datos que ingreso Estatura : {altura} m y su peso es de: {peso} kg")
    print(f"| Su indice de masa corporal es: {imc:.2f} \n| Lo que indica que esta muy Bajo de Peso")
elif imc >= 19.00 and imc <= 24.99 :
    print(f"| Datos que ingreso Nombre completo : {nombre} {a_p} {a_m} y su edad es: {edad} años")
    print(f"| Datos que ingreso Estatura : {altura} m y su peso es de: {peso} kg")
    print(f"| Su indice de masa corporal es: {imc:.2f} \n| Lo que indica que esta normal")
elif imc >= 25.00 and imc <= 29.99 :
    print(f"| Datos que ingreso Nombre completo : {nombre} {a_p} {a_m} y su edad es: {edad} años")
    print(f"| Datos que ingreso Estatura : {altura} m y su peso es de: {peso} kg")
    print(f"| Su indice de masa corporal es: {imc:.2f} \n| Lo que indica que tiene sobrepeso")
elif imc >= 30.00 and imc <= 34.99 :
    print(f"| Datos que ingreso Nombre completo : {nombre} {a_p} {a_m} y su edad es: {edad} años")
    print(f"| Datos que ingreso Estatura : {altura} m y su peso es de: {peso} kg")
    print(f"| Su indice de masa corporal es: {imc:.2f} \n| Lo que indica que tiene obesidad leve")
elif imc >= 35.00 and imc <= 39.99 :
    print(f"| Datos que ingreso Nombre completo : {nombre} {a_p} {a_m} y su edad es: {edad} años")
    print(f"| Datos que ingreso Estatura : {altura} m y su peso es de: {peso} kg")
    print(f"| Su indice de masa corporal es: {imc:.2f} \n| Lo que indica que tiene obesidad media")
elif imc >= 40.00 :
    print(f"| Datos que ingreso Nombre completo : {nombre} {a_p} {a_m} y su edad es: {edad} años")
    print(f"| Datos que ingreso Estatura : {altura} m y su peso es de: {peso} kg")
    print(f"| Su indice de masa corporal es: {imc:.2f} \n| Lo que indica que tiene obesidad alta")