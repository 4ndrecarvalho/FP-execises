"""
A sequência de Fibonacci começa com os números 0 e 1.  Depois, cada elemento
consecutivo da sequência obtém-se pela soma dos dois elementos anteriores.
Complete a função genFibonacci(n) para _devolver_ uma lista com os n primeiros
números de Fibonacci.  Por exemplo, se n=6, deve devolver [0, 1, 1, 2, 3, 5].
A função só tem de funcionar para n>=2.

The Fibonacci sequence starts with the numbers 0 and 1. Then each consecutive
element of the sequence is obtained by the sum of the two previous elements.
Complete the genFibonacci(n) function to _return_ a list of the first n
Fibonacci numbers. For example, if n=6, it should return [0, 1, 1, 2, 3, 5].
The function only has to work for n>=2.
"""

def genFibonacci(n):
   # Complete ...
   a = []
   for i in range(0, n):
      if i == 0:
         v0 = 0
      elif i == 1:
         v1 = 1
      else:
         v2 = v0 + v1
         v0 = v1 
         v1 = v2
      a.append(v2 if i > 1 else v1 if i == 1 else v0)
   return a

# Ou...     

def genFibonacci(n):
    fibNum = [0,1]
    [fibNum.append(fibNum[0+i] + fibNum[1+i]) for i in range(n-2)]
    return fibNum if n > 1 else fibNum[1] if n == 1 else fibNum[0]
     


"""
Imagine que está a fazer palavras cruzadas (em Inglês) e falta-lhe uma
palavra com o padrão "?YS???Y", onde os "?" representam letras por preencher.
Complete este programa para o ajudar a descobrir a palavra.
O programa já inclui instruções para ler uma lista de palavras inglesas a
partir do ficheiro wordlist.txt.
"""

# This function reads words from a file.
def load(fname):
   with open(fname) as f:
      lst = []
      for line in f:
         words = line.strip().split()
         lst.extend(words)
   return lst


""" a)
Complete a função matchesPattern(s, pattern) para devolver
True se s corresponder ao padrão fornecido e False, no caso contrário.
Uma string s corresponde ao padrão se e só se tiver os mesmos carateres
que o padrão nas mesmas posições, exceto onde o padrão tem ?.
Nas posições dos ?, não importa que carateres estão na string s.
A correspondência não deve fazer distinção entre maiúsculas e minúsculas.
"""
def matchesPattern(s, pattern):
   # Complete ...
   s = s.lower()
   pattern = pattern.lower()
   if len(s) != len(pattern):
      return False
   for i, w in enumerate(pattern):
      if w == "?":
         pass
      elif s[i] != w:
         return False
   return True
      

""" b)
Complete a função filterPattern(lst, pattern) para extrair duma lista de strings
as strings que têm o padrão dado.
Sugestão: use a função matchesPattern para testar cada palavra.
"""
def filterPattern(lst, pattern):
   # Complete ...
   words = [word for word in lst if matchesPattern(word,pattern)]
   return words
      
   


def main():
   print("a)")
   print( matchesPattern("secret", "s?c??t") )  #-> True
   print( matchesPattern("secreta", "s?c??t") ) #-> False
   print( matchesPattern("socket", "s?c??t") )  #-> True
   print( matchesPattern("soccer", "s?c??t") )  #-> False
   print( matchesPattern("SEcrEt", "?ecr?t") )  #-> True
   print( matchesPattern("SEcrET", "?ecr?t") )  #-> True
   print( matchesPattern("SecrEt", "?ECR?T") )  #-> True

   words = load("wordlist.txt")

   print("b)")
   # Solution to "S?C??T"
   lst = FILTERPATTERN(words, "s?c??t")
   print(lst)

   assert isinstance(lst, list),  "result lst should be a list"
   assert "secret" in lst,  "result should contain 'secret'"

   # Solution to "?YS???Y"
   lst = filterPattern(words, "?ys???y")
   print(lst)


# Call main function:
if __name__ == "__main__":
   main()
   
   
   
 # Devolve o número de linhas da matriz M.
def matrows(M):
   return len(M)

# Complete para devolver o número de colunas da matriz M.
def matcols(M):
   return len(M[0])

# Complete a função para devolver uma matriz com m×n zeros.
def matzeros(m, n):
   N = [ 0 for i in range(n)]
   M = [ N.copy() for i in range(m)]
   return M

def matzerosTEST(m, n):
   M = matzeros(m, n)
   M[0][1] = 1   # should change just 1 element!
   return M

# Complete a função para multiplicar a matriz A pela matriz B.
# Complete a função para multiplicar a matriz A pela matriz B.
def matmult(A, B):
   assert matcols(A) == matrows(B)
   C = []
   c=0
   for i in range(len(A)):
      lstrow = []
      for j in range(len(B[0])):
         c=0
         for k in range(len(A[0])):
            c += A[i][k]* B[k][j]
         lstrow.append(c)
      C.append(lstrow)
   return C

def matmultTEST(A, B):
   C = matmult(A, B)
   return A, B, C

   
   
O Método de Hondt permite fazer a distribuição de deputados eleitos para uma assembleia de forma proporcional aos votos de cada partido. Considerando que V_i é o número de votos obtidos pelo partido i, o método determina o número N_i de lugares a atribuir a esse partido.

O método começa com N_i = 0 para todos os partidos e depois:

Calcula os quocientes Q_i = \frac{V_i}{N_i+1}.
Encontra o partido com o maior quociente e atribui-lhe um deputado (aumenta o N_i correspondente).
Se vários partidos tiverem quocientes iguais, atribui o deputado ao partido com menos votos.
Repete estes passos até todos os lugares estarem atribuídos.
Por exemplo, para distribuir 6 lugares por quatro partidos que tiveram as votações V = [15300, 12000, 6600, 5100] o processo deve seguir os passos abaixo.

Q: [15300, 12000, 6600, 5100] => +1 for party 0 => N: [1, 0, 0, 0]
Q: [ 7650, 12000, 6600, 5100] => +1 for party 1 => N: [1, 1, 0, 0]
Q: [ 7650,  6000, 6600, 5100] => +1 for party 0 => N: [2, 1, 0, 0]
Q: [ 5100,  6000, 6600, 5100] => +1 for party 2 => N: [2, 1, 1, 0]
Q: [ 5100,  6000, 3300, 5100] => +1 for party 1 => N: [2, 2, 1, 0]
Q: [ 5100,  4000, 3300, 5100] => +1 for party 3 => N: [2, 2, 1, 1]
Note que o 1º deputado vai para o partido 0, porque tem o quociente mais alto. Depois atualiza-se Q e repete-se. No último passo há dois partidos com Q máximo, por isso atribui-se o lugar ao partido menos votado.

Implemente uma função hondt(votes, numseats) que, dada uma lista com os números de votos em cada um partidos e dado o número de lugares disponíveis, calcule e devolva uma lista com a distribuição de deputados para cada partido. Por exemplo, hondt([15300, 12000, 6600, 5100], 6) deve devolver [2, 2, 1, 1].


def hondt(votes, numseats):
   quo = [0] * len(votes)
   partseats = [0] * len(votes)
   while numseats > 0:
      for part in range(len(votes)):
         quo[part] = votes[part] / (partseats[part]+1)
      maxIndex = partidoMax(quo, votes)
      partseats[maxIndex] += 1
      numseats -= 1
   return partseats
   
def partidoMax(quo, votes):
   maxquo = max(quo)
   maxIndexes = [i for i, qi in enumerate(quo) if qi == maxquo]
   maxIndex = maxIndexes[0]
   for i in maxIndexes:
      if votes[i] < votes[maxIndex]:
         maxIndex = i
   return maxIndex



   

