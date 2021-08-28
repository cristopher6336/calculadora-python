#sistema de preguntas 

esp = "" #espacios
var1 = 0
var2 = 0
text = "este es el resultado = "

def pantalla(): #funcion primero
    print("   CALCULADORA  ")
    print(esp)
    print("1. sumas")
    print("2. restas")
    print("3. multiplicaciones")
    print("4. diviciones")
    print("5. salir")
    print(esp)
    ent = int(input("user> "))
    
    #funciones para hacer las operaciones
    def sumas():
        var1 = int(input("el primer valor = "))
        var2 = int(input("el segundo valor = "))
        
        resultado_s = var1 + var2
        
        print(esp)
        print(text ,resultado_s)
        
        print("_______________________________________________________________")
        print(esp)
        pantalla()

    def resta():
        var1 = int(input("el primer valor = "))
        var2 = int(input("el segundo valor = "))

        resultado_r = var1 - var2
        
        print(esp)  
        print(text, resultado_r)

        print("_______________________________________________________________")
        print(esp)
        pantalla()


    def multi():
        var1 = int(input("el primer valor = "))
        var2 = int(input("el segundo valor = "))

        resultado_m = var1 * var2
        
        print(esp)
        print(text, resultado_m)
  
        print("_______________________________________________________________")
        print(esp)
        pantalla()
   

    def divi():
        var1 = int(input("el primer valor = "))
        var2 = int(input("el segundo valor = "))

        resultado_d = var1 / var2
        
        print(esp)
        print(text, resultado_d)
 
        print("_______________________________________________________________")
        print(esp)
        pantalla()

    def salir():
        exit()

    if (ent == 1):
        sumas()
    elif (ent == 2):
        resta()
    elif (ent == 3):
        multi()
    elif (ent == 4):
        divi()
    elif(ent == 5):
        salir()
    else:
        print("escribe bien el comando")
        pantalla()

pantalla()

