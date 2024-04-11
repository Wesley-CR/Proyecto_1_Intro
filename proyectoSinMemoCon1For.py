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
    
def sacarDivisor(nominador: int, resultado: int) -> list[int]:
   divisorPartes = []
   divisor = nominador//resultado
   while divisor != 0 :
      divisorPartes.append(divisor%10)
      divisor = divisor//10
   while len(divisorPartes) != 5:
      divisorPartes.append(0)
   return divisorPartes

def encontrador(n,reps) -> list[str]:
    listaSoluciones = []
    for a in range(100000):
        a_list = []
        for x in str(a):
            a_list.append(int(x))
        if numeroInvalido(reps, a_list): continue
        if a % n == 0 and not numeroInvalido(reps, a_list, sacarDivisor(a, n)):
            listaSoluciones.append(f"{a}/{a//n}={n}")
    return listaSoluciones

                     
def main() -> None:
   inputs = int(input())
   while inputs != 0:
      inputs -= 1
      divisor, repeticiones = map(int, input().split())
      encontrador(divisor,repeticiones)

main()
