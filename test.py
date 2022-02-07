
# On a chessboard, positions are marked with letters between a and h for the column and a
# number between 1 and 8 for the row. The first place on the board, a1, is black. The next
# is white, alternating across a row. Odd rows start with black, even rows start with white.

# Give a 2 character input string with a letter (a-h) and a number (1-8), print "Black" or
# "White" indicating if the square is black or white.
 
inputStr = 'b4'
dic={"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
print("Black") if ( int(inputStr[1]) + (dic[inputStr[0]] % 2) ) % 2 == 0 else print("White")

# Given a sequence lst, return the longest n so that 
# the first n elements equal the last n elements (with no overlapping).

# Dada uma sequência lst, devolva o maior n tal que
# os primeiros n elementos igualam os últimos n elementos (sem sobreposição).

# def firstEqualLast(lst):
#     count = maxi = 0
#     rep = ""
#     s = " ".join([str(x) for x in lst])
#     for i in range(len(lst)):
#         p = " ".join([str(x) for x in lst[:i]])
#         if p in s[1:]:
#             count = len(p.split())
#             if count > maxi:
#                 maxi = count
#                 rep = p.split()
#             if maxi > len(lst)/2: # se forem todos iguais a repetição é metade
#                 maxi = round(maxi/2)
#                 rep = p.split()[:len(lst)//2]
#     return maxi

def firstEqualLast(lst):
    maxi = 0
    for i in range(len(lst)):
        if lst[:i] == lst[-i:]:
            maxi = len(lst)//2 if i > len(lst)//2 else len(lst[:i])
    return maxi

print(firstEqualLast([1,2,3,1,2,3]))         #3
print(firstEqualLast([1,2,3,4,5,6,1,2,3,4]))   #4
print(firstEqualLast([5,6,6,5,1,5,6,6,5]))     #4
print(firstEqualLast([8,8,8,8,8,8,8,8,8,8,8,8])) # 6
print(firstEqualLast([])) #0 
print(firstEqualLast([1])) #0
print(firstEqualLast("ab")) #0
print(firstEqualLast("aaaaaa")) #3

# Given a string s and a string t, return a string in which all the characters 
# of s that occur in t have been replaced by a _ sign. The comparisons are 
# case sensitive.

def replaceCharactersWithUnderscores(t, s):
    x = set(s)
    newStr=[]
    for char in t:
       if char in x:
          newStr.append("_")
       else:
          newStr.append(char)
    return "".join(newStr)

    # Given a string s, return the longest prefix that is repeated somewhere else in the string. 
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

# def longestPrefixRepeated(s):
#     count = maxi = 0
#     rep = ""
#     for i in range(len(s)):
#         p = s[:i]
#         if p in s[1:]:
#             count = len(p)
#             if count > maxi:
#                 maxi = count
#                 rep = p
#             if count > len(s)/2:
#                maxi = round(maxi/2)
#                rep = p[:len(s)//2]
#     return rep

def longestPrefixRepeated_(s):
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    i = 0
    while True:
        if s1 in s2:
            return s1
        else:
            s2 = s1[-1] + s2
            s1 = s1[:len(s)//2-(i+1)]
            i += 1

def longestPrefixRepeated(lst):
    maxi = ""
    count = 0
    end = len(lst)+1
    for i in range(end):
        for j in range(i, end):
            if lst[:i] == lst[j:j+i]:
                maxi = (lst[:end//2]) if i > end//2 else (lst[:i])
                count = len(maxi)
    return maxi, count

print(longestPrefixRepeated('aaaaaa')) # aaa
print(longestPrefixRepeated('test')) #t
print(longestPrefixRepeated('abcdabejf')) #ab
print(longestPrefixRepeated('')) #
print(longestPrefixRepeated('dogcatdog')) #dog
print(longestPrefixRepeated('dogcatdo')) #do
print(longestPrefixRepeated('abcdef')) #
print(longestPrefixRepeated([1,2,3,1,2,3]))         #3
print(longestPrefixRepeated([1,2,3,4,5,6,1,2,3,4]))   #4
print(longestPrefixRepeated([5,6,6,5,1,5,6,6,5]))     #4
print(longestPrefixRepeated([8,8,8,8,8,8,8,8,8,8,8,8])) # 6
print(longestPrefixRepeated([])) #0 
print(longestPrefixRepeated([1])) #0
print(longestPrefixRepeated("ab")) #0
print(longestPrefixRepeated("aaaaaa")) #3

#A função main define uma lista de tuplos com informação sobre acções de diversas empresas transacionadas em bolsas de várias cidades. Cada tuplo contém os campos: empresa, cidade, preço-de-abertura, preço-de-fecho, volume.
#
#Defina uma função printStocks(stocks) para mostrar a tabela com as colunas formatadas como no exemplo abaixo. Inclua uma coluna com a valorização da ação em percentagem. Por exemplo, se o preço de abertura for 10.00 e o de fecho for 9.50, a valorização será de -5\%. Note que esta função é chamada pela função main e não deve modificar a lista passada no argumento.
#
#    INTC      London              34.25     34.45   1792860    0.6%
#    TSLA      London             221.33    229.63    398520    3.8%
#    EA        Paris               72.63     68.98   1189510   -5.0%
#    INTC      Tokyo               33.22     34.29   4509110    3.2%
#    TSLA      Paris              217.35    217.75    252500    0.2%
#    ATML      Frankfurt            8.23      8.36    810440    1.6%


def printStocks(stks):
   for stk in stks:
      print("{:<10} {:<10} {:>9.2f} {:>9.2f} {:>9} {:>6.1f}%".format(stk[0], stk[1], stk[2], stk[3], stk[4], (-(1 - (stk[3] / stk[2])) *100)))


# A função main define uma lista de tuplos com informação sobre acções de diversas empresas transacionadas em bolsas de várias cidades.
#  Cada tuplo contém os campos: empresa, cidade, preço-de-abertura, preço-de-fecho, volume.

# Acrescente os argumentos adequados à função sorted para obter uma tabela ordenada alfabeticamente pelo nome da empresa e, para a mesma empresa, 
# por ordem decrescente do volume transacionado.

#stocks2 = sorted(stocks, key = lambda t: (t[0], -t[4])  )

def companyVolume(stocks, city):
    lst = []
    for stk in stocks:
       if stk[1] == city:
          lst.append((stk[0], stk[4]))
    return lst


# O código abaixo lida com comboios de mercadorias. Cada comboio é representado por uma lista de vagões e cada vagão é uma lista com 
# o tipo e a quantidade de mercadoria que transporta. Por exemplo,

# t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]

# representa um comboio com 5 vagões: o primeiro vagão tem 30 toneladas de carvão, o segundo tem 50 toneladas de arroz, etc.

# A função principal define um dicionário trains que associa nomes a comboios. 
# Complete a função trainsPerMerchandise(trains) para criar um dicionário que a cada tipo de mercadoria associe o conjunto dos nomes dos 
# comboios que a transportam.

def trainsPerMerchandise(trains):
    dic = {}
    for train, vag in trains.items():
            for merc in vag:
                   dic.setdefault(merc[0], set()).add(train)
    return dic

# A função main define uma lista de tuplos com informação sobre acções de diversas empresas transacionadas em bolsas de várias cidades. Cada tuplo contém os campos: empresa, cidade, preço-de-abertura, preço-de-fecho, volume.

# O ficheiro stocks.txt contém informação de mais ações. Cada linha corresponde a uma ação, com os campos separados por TABs. como neste excerto:

# ERIC    Lisbon  9.1 9.58283128  428800
# TSLA    London  221.33  229.63  398520
# INTC    Tokyo   33.22001    34.28999    4509110

# Complete a função load para ler ficheiros com esse formato e devolver uma lista de tuplos com o mesmo formato (tipos) da variável stocks.

def load(fname):
    lst= []
    with open(fname, 'r') as fin:
        for line in fin:
            line = line.strip().split("\t")
            lst.append(tuple([line[0], line[1], float(line[2]), float(line[3]), int(line[4])]))
    return lst


# O código abaixo lida com comboios de mercadorias. Cada comboio é representado por uma lista de vagões e cada vagão é uma lista com o tipo e a quantidade de mercadoria que transporta. Por exemplo,

# t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]

# representa um comboio com 5 vagões: o primeiro vagão tem 30 toneladas de carvão, o segundo tem 50 toneladas de arroz, etc.

# Complete a função unload(t, m, q), que deve descarregar do comboio t uma quantidade q de mercadoria de tipo m. Para isso, deve percorrer os vagões um a um, a partir do último, e descarregar total ou parcialmente os que tiverem a mercadoria pretendida até perfazer a quantidade pedida. Os vagões totalmente descarregados devem ser retirados do comboio, mas os restantes têm de ficar no comboio pela ordem original. Se conseguir descarregar toda a quantidade pedida, a função deve devolver zero. Se não, deve devolver a quantidade que não conseguiu descarregar.

def unload(t,m,q):
    exc = q
    resto = 0
    for vag in range(len(t)-1,-1,-1):
        if t[vag][0] == m:
            if resto > 0:
                exc = t[vag][1] - resto
            else:
                exc = t[vag][1] - q
            if exc > 0:
                t[vag][1] = exc
                exc = 0
                break
            elif exc <0:
                t.pop(vag)
                resto = abs(exc)
    return exc if (exc >= 0) else resto


t = [['coal',30],['rice',50],['iron',5],['rice',42],['coal',45]]
print(t)
print(unload(t, 'rice', 40))
print(t)
print(unload(t, 'coal', 50))
print(t)
print(unload(t, 'iron', 20))
print(t)

# t: [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]
# unload(t, 'rice', 40) -> 0
# t: [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 2], ['coal', 45]]
# unload(t, 'coal', 50) -> 0
# t: [['coal', 25], ['rice', 50], ['iron', 5], ['rice', 2]]
# unload(t, 'iron', 20) -> 15
# t: [['coal', 25], ['rice', 50], ['rice', 2]]
print()
t = [['coal', 50], ['rice', 40], ['rice', 5], ['rice', 10], ['coal', 20]]
print(t)
print(unload(t, 'rice', 40))
print(t)
print(unload(t, 'coal', 50))
print(t)
print(unload(t, 'iron', 20))
print(t)


# t: [['coal', 50], ['rice', 40], ['rice', 5], ['rice', 10], ['coal', 20]]
# unload(t, 'rice', 40) -> 0
# t: [['coal', 50], ['rice', 15], ['coal', 20]]
# unload(t, 'coal', 50) -> 0
# t: [['coal', 20], ['rice', 15]]
# unload(t, 'iron', 20) -> 20
# t: [['coal', 20], ['rice', 15]]


# Complete onlyCaps(S) para devolver uma string que contenha apenas as letras maiúsculas da string S. Por exemplo, onlyCaps("John Fitzgerald Kennedy") deve devolver "JFK". A solução tem de ser recursiva e não pode usar ciclos.
def onlyCaps(s):
   # NOTE: ch.isupper() -> True if ch is uppercase.
    if len(s) == 0:
       return ""
    return s[0] + onlyCaps(s[1:]) if s[0].isupper() else onlyCaps(s[1:])