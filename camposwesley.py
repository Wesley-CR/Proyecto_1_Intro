#El dominio es un numero entero que van a ser las repeticiones y dos listas de numeros enteros para verificar cuales numeros se repiten dentro de ambas listas
#El codominio es un booleano el cual devuelve True si el numero es invalido y False si es valido
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

#El dominio son 2 numeros enteros, uno para el numerador y otro para obtener el denominador
#El codominio es una lista de enteros que contiene los digitos del denominador a ser verificado
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
#El dominio son 2 numeros enteros, 1 >= n <=20 y 1 >= R <= 5
#El codominio es una lista de strings con todas las soluciones a un caso
def encontrador(n: int,reps: int) -> list[str]:
   solucion = str(n) + " " + str(reps)
   if solucion in respuestas:
      return respuestas[solucion]
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
                  if tmp//n < 1000: continue
                  if tmp % n == 0 and not numeroInvalido(reps, numeros, sacarDivisor(tmp, n)):
                     listaSoluciones.append(f"{tmp}/{tmp//n}={n}")
   respuestas.update({solucion: listaSoluciones})
   return listaSoluciones
                     
def main() -> None:
   inputs = int(input())
   while inputs != 0:
      inputs -= 1
      divisor, repeticiones = map(int, input().split())
      print(*encontrador(divisor,repeticiones), sep='\n')

main()
