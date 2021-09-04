#sistema de calculadora
#esta es la segunda version de la calculadora en python, espero que les guste ;D

esp = "" #espacios
var1 = 0
var2 = 0
var3 = 0
var4 = 0
var5 = 0
var6 = 0
var7 = 0
var8 = 0
var9 = 0
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
        print(esp)
        print("por ejemplo 2,3,4,5,6,7,8,9")
        va_c_s = int(input("cuantas cifras? = "))
        
        def cifras_2():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
        
            resultado_s = var1 + var2
        
            print(esp)
            print(text ,resultado_s)
        
            print("_______________________________________________________________")
            print(esp)
            pantalla()
        
        def cifras_3():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))

            resultado_s = var1 + var2 + var3
            
            print(esp)
            print(text, resultado_s)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_4():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))

            resultado_s = var1 + var2 + var3 + var4
            
            print(esp)
            print(text, resultado_s)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_5():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            resultado_s = var1 + var2 + var3 + var4 + var5
            
            print(esp)
            print(text, resultado_s)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_6():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            resultado_s = var1 + var2 + var3 + var4 + var5 + var6

            print(esp)
            print(text, resultado_s)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

            
        def cifras_7():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            resultado_s = var1 + var2 + var3 + var4 + var5 + var6 + var7
  
            print(esp)
            print(text, resultado_s)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_8():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            var8 = int(input("el octavo valor = "))
            resultado_s = var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8
  
            print(esp)
            print(text, resultado_s)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_9():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            var8 = int(input("el octavo valor = "))
            var9 = int(input("el noveno valor ="))
            resultado_s = var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8
  
            print(esp)
            print(text, resultado_s)
            print("_______________________________________________________________")
            print(esp)
            pantalla()


               #funciones 
        if (va_c_s == 2):
            cifras_2()
        elif (va_c_s == 3):
            cifras_3()
        elif (va_c_s == 4):
            cifras_4()
        elif (va_c_s == 5):
            cifras_5()
        elif (va_c_s == 6):
            cifras_6()
        elif (va_c_s == 7):
            cifras_7()
        elif (va_c_s == 8):
            crifras_8()

        elif (va_c_s < 2):
            print("no ay crifras tan bajas")
            print(esp)
            pantalla()

              
    def resta():
        print(esp)
        print("por ejemplo 2,3,4,5,6,7,8,9")
        va_c_r = int(input("cuantas cifras? = "))
        
        def cifras_2():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
        
            resultado_r = var1 - var2
        
            print(esp)
            print(text ,resultado_r)
        
            print("_______________________________________________________________")
            print(esp)
            pantalla()
        
        def cifras_3():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))

            resultado_r = var1 - var2 - var3
            
            print(esp)
            print(text, resultado_r)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_4():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))

            resultado_r = var1 - var2 - var3 - var4
            
            print(esp)
            print(text, resultado_r)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_5():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            resultado_r = var1 - var2 - var3 - var4 - var5
            
            print(esp)
            print(text, resultado_r)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_6():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            resultado_r = var1 - var2 - var3 - var4 - var5 - var6

            print(esp)
            print(text, resultado_r)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

            
        def cifras_7():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            resultado_r = var1 - var2 - var3 - var4 - var5 - var6 - var7
  
            print(esp)
            print(text, resultado_r)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_8():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            var8 = int(input("el octavo valor = "))
            resultado_r = var1 - var2 - var3 - var4 - var5 - var6 - var7 - var8
  
            print(esp)
            print(text, resultado_r)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_9():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            var8 = int(input("el octavo valor = "))
            var9 = int(input("el noveno valor ="))
            resultado_r = var1 - var2 - var3 - var4 - var5 - var6 - var7 - var8
  
            print(esp)
            print(text, resultado_r)
            print("_______________________________________________________________")
            print(esp)
            pantalla()


               #funciones 
        if (va_c_r == 2):
            cifras_2()
        elif (va_c_r == 3):
            cifras_3()
        elif (va_c_r == 4):
            cifras_4()
        elif (va_c_r == 5):
            cifras_5()
        elif (va_c_r == 6):
            cifras_6()
        elif (va_c_r == 7):
            cifras_7()
        elif (va_c_r == 8):
            crifras_8()

        elif (va_c_r < 2):
            print("no ay crifras tan bajas")
            print(esp)
            pantalla()


    def multi():
        print(esp)
        print("por ejemplo 2,3,4,5,6,7,8,9")
        va_c_m = int(input("cuantas cifras? = "))
        
        def cifras_2():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
        
            resultado_m = var1 * var2
        
            print(esp)
            print(text ,resultado_m)
        
            print("_______________________________________________________________")
            print(esp)
            pantalla()
        
        def cifras_3():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))

            resultado_m = var1 * var2 * var3
            
            print(esp)
            print(text, resultado_m)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_4():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))

            resultado_m = var1 * var2 * var3 * var4
            
            print(esp)
            print(text, resultado_m)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_5():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            resultado_m = var1 * var2 * var3 * var4 * var5
            
            print(esp)
            print(text, resultado_m)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_6():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            resultado_m = var1 * var2 * var3 * var4 * var5 * var6

            print(esp)
            print(text, resultado_m)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

            
        def cifras_7():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            resultado_m = var1 * var2 * var3 * var4 * var5 * var6 * var7
  
            print(esp)
            print(text, resultado_m)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_8():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            var8 = int(input("el octavo valor = "))
            resultado_m = var1 * var2 * var3 * var4 * var5 * var6 * var7 * var8
  
            print(esp)
            print(text, resultado_m)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_9():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            var8 = int(input("el octavo valor = "))
            var9 = int(input("el noveno valor ="))
            resultado_m = var1 * var2 * var3 * var4 * var5 * var6 * var7 * var8
  
            print(esp)
            print(text, resultado_m)
            print("_______________________________________________________________")
            print(esp)
            pantalla()


               #funciones 
        if (va_c_m == 2):
            cifras_2()
        elif (va_c_m == 3):
            cifras_3()
        elif (va_c_m == 4):
            cifras_4()
        elif (va_c_m == 5):
            cifras_5()
        elif (va_c_m == 6):
            cifras_6()
        elif (va_c_m == 7):
            cifras_7()
        elif (va_c_m == 8):
            crifras_8()

        elif (va_c_m < 2):
            print("no ay crifras tan bajas")
            print(esp)
            pantalla()


    def divi():
        print(esp)
        print("por ejemplo 2,3,4,5,6,7,8,9")
        va_c_d = int(input("cuantas cifras? = "))
        
        def cifras_2():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
        
            resultado_d = var1 / var2
        
            print(esp)
            print(text ,resultado_d)
        
            print("_______________________________________________________________")
            print(esp)
            pantalla()
        
        def cifras_3():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))

            resultado_d = var1 / var2 / var3
            
            print(esp)
            print(text, resultado_d)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_4():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))

            resultado_d = var1 / var2 / var3 / var4
            
            print(esp)
            print(text, resultado_d)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_5():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            resultado_d = var1 / var2 / var3 / var4 / var5
            
            print(esp)
            print(text, resultado_d)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_6():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            resultado_d = var1 / var2 / var3 / var4 / var5 / var6

            print(esp)
            print(text, resultado_d)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

            
        def cifras_7():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            resultado_d = var1 / var2 / var3 / var4 / var5 / var6 / var7
  
            print(esp)
            print(text, resultado_d)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_8():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            var8 = int(input("el octavo valor = "))
            resultado_d = var1 / var2 / var3 / var4 / var5 / var6 / var7 / var8
  
            print(esp)
            print(text, resultado_d)
            print("_______________________________________________________________")
            print(esp)
            pantalla()

        def cifras_9():
            print(esp)
            var1 = int(input("el primer valor = "))
            var2 = int(input("el segundo valor = "))
            var3 = int(input("el tercer valor = "))
            var4 = int(input("el cuarto valor = "))
            var5 = int(input("el quinto valor = "))
            var6 = int(input("el sexto valor = "))
            var7 = int(input("el septimo valor = "))
            var8 = int(input("el octavo valor = "))
            var9 = int(input("el noveno valor ="))
            resultado_d = var1 / var2 / var3 / var4 / var5 / var6 / var7 / var8
  
            print(esp)
            print(text, resultado_d)
            print("_______________________________________________________________")
            print(esp)
            pantalla()


               #funciones 
        if (va_c_d == 2):
            cifras_2()
        elif (va_c_d == 3):
            cifras_3()
        elif (va_c_d == 4):
            cifras_4()
        elif (va_c_d == 5):
            cifras_5()
        elif (va_c_d == 6):
            cifras_6()
        elif (va_c_d == 7):
            cifras_7()
        elif (va_c_d == 8):
            crifras_8()

        elif (va_c_d < 2):
            print("no ay crifras tan bajas")
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

