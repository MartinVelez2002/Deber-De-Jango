import os 
os.system("cls")

pos = int(input("Digite la posición del número Fibonacci que desea conocer: ")) #Como primer paso, tenemos la capturación del dato y se lo asignamos a la variables "pos"

def fibo(pos): 
    #Se procede a evaluar el valor dado por el usuario y dependiendo de este, se realizarán las siguientes operaciones, donde tendrá dos caminos, uno por verdadero y el otro por falso, siendo destacado el lado por falso donde se harán todos los cálculos para la resolución del problema.
    if pos < 2: 
        return pos 

    else: 
        return fibo(pos-1) + fibo(pos-2)

print("El número Fibonacci de la posición dada es: ", fibo(pos))
#Presenta por pantalla el número Fibonacci con la posición otorgada por el usuario


