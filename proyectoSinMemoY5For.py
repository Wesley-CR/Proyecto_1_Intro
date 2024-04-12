import sys

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

def encontrador(n,reps) -> list[str]:
   listaSoluciones = []
   for a in range(10):
      for b in range(10):
         if numeroInvalido(reps,[a,b]): continue
         for c in range(10):
            if numeroInvalido(reps,[a,b,c]): continue
            for d in range(10):
               if numeroInvalido(reps,[a,b,c,d]): continue
               for e in range(10):
                  numeros = [a,b,c,d,e]
                  if numeroInvalido(reps,numeros): continue
                  tmp = a * 10000 + b * 1000 + c * 100 + d * 10 + e
                  if a % n == 0 and not numeroInvalido(reps, numeros, sacarDivisor(a, n)):
                     listaSoluciones.append(f"{a}/{a//n}={n}")
   return listaSoluciones
                     
def main() -> None:
   inputs = int(input())
   while inputs != 0:
      inputs -= 1
      divisor, repeticiones = map(int, input().split())
      print(*encontrador(divisor,repeticiones), sep='\n')

main()