def raiz(num):
    raiz=num**0.5
    return raiz

while True:
    try:
        numero=float(input("ingrese un numero a calcular la raiz : "))
        break
    except ValueError:
        print("error,debe ingresar solamente numeros!!")
print(f"la raiz cuadrada de {numero} es : {raiz(numero)}")

print("sassos")