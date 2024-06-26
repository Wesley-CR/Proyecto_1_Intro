def numeroInvalido(repeticiones: int, numeros: list[int], divisor: list[int] = []) -> bool:
    numerosRepetidos = {}
    for i in numeros:
        if i in numerosRepetidos:
            numerosRepetidos[i] += 1
        else:
            numerosRepetidos[i] = 1
        if numerosRepetidos[i] > repeticiones:
            return True
    if divisor:
        for i in divisor:
            if i in numerosRepetidos:
                numerosRepetidos[i] += 1
            else:
                numerosRepetidos[i] = 1
            if numerosRepetidos[i] > repeticiones:
                return True
    return False
    
def sacarDivisor(numerador: int, resultado: int) -> list[int]:
   divisorPartes = []
   divisor = numerador//resultado
   while divisor != 0 :
      divisorPartes.append(divisor%10)
      divisor = divisor//10
   while len(divisorPartes) != 5:
      divisorPartes.append(0)
   return divisorPartes

respuestas = {}

def encontrador(n,reps) -> list[str]:
    tmpForDictionary = str(n) + " " + str(reps)
    listaSoluciones = []
    if tmpForDictionary in respuestas:
        return respuestas[tmpForDictionary]
    for a in range(100000):
        a_list = []
        if tmp//n < 1000: continue
        for x in str(a):
            a_list.append(int(x))
        if numeroInvalido(reps, a_list): continue
        if a % n == 0 and not numeroInvalido(reps, a_list, sacarDivisor(a, n)):
            listaSoluciones.append(f"{a}/{a//n}={n}")

    respuestas.update({tmpForDictionary: listaSoluciones})
    return listaSoluciones

                     
def main() -> None:
   inputs = int(input())
   while inputs != 0:
      inputs -= 1
      divisor, repeticiones = map(int, input().split())
      encontrador(divisor,repeticiones)

main()
