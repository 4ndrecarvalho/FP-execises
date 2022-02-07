# Complete onlyCaps(S) para devolver uma string que contenha apenas as letras maiúsculas da string S. Por exemplo, onlyCaps("John Fitzgerald Kennedy") deve devolver "JFK". A solução tem de ser recursiva e não pode usar ciclos.

def onlyCaps(s):
   # NOTE: ch.isupper() -> True if ch is uppercase.
    if len(s) == 0:
       return ""
    return s[0] + onlyCaps(s[1:]) if s[0].isupper() else onlyCaps(s[1:])

def onlyCaps_noRec(s):
    string = ""
    for char in s:
        if char.isupper():
            string+=char
    return string

s= "tANta Dor de cabeça com tanta RecursividadE"

print("\n*** Só maiusculas ***")
print(onlyCaps_noRec(s))
print(onlyCaps(s))

def listSum(lst):
    return lst[0] if len(lst) == 1 else lst[0] + listSum(lst[1:])

print("\n*** Soma de listas ***")
print(" + ".join([ str(x) for x in [1,2,3,4] ]), "=", listSum([1,2,3,4]))
print(" + ".join([ str(x) for x in [1,3,5,7,9] ]), "=", listSum([1,3,5,7,9]))

def recFib(n):
    return 0 if n == 0 else 1 if n <= 2 else recFib(n-1) + recFib(n-2)

print("\n*** Fibonacci ***")
for i in range(0,10):
    print("Fib("+str(i)+") = ",recFib(i))

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
      return convertString[n]
    return toStr(n//base,base) + convertString[n%base]

print("\n*** Converção para base ***")
print("1453 na base 16 =", toStr(1453,16))

def invertString(string):
    if len(string) == 0:
        return ""
    return invertString(string[1:]) + string[0]

print("\n*** Inversão de strings ***")
print("Bela recursão!",">>>",invertString("Bela recursão!"))

def invertList(lst, mem = []):
    if len(lst) == 1:
        return [lst[0]]
    return [lst[-1]] + invertList(lst[:-1])

print("\n*** Inversão de lista ***")
print("[1, 2, 3] >>>",invertList([1,2,3]))

def isPal(string):
    if len(string) == 0:
        return True
    return string[0] == string[-1] and isPal(string[1:-1])

print("\n*** Palindromos ***")
print("ovo\t", isPal("ovo"))
print("boa\t", isPal("boa"))
print("batata\t", isPal("batata"))
print("catatac\t", isPal("catatac"))

def recFac(n):
    return 1 if n <= 1 else n * recFac(n-1)

print("\n*** Factorial ***")
for i in range(0,10):
    print(str(i)+"! = ",recFac(i))

def genConj(lst, n):
    if n == 0:
        return [""]
    return [ str(x)+str(c) for c in genConj(lst, n-1) for x in lst ]

print("\n*** Conjuntos ***")
print(genConj([1,2,3], 3))
print(genConj("abc", 3))

def genPerm(lst, n):
    if n > len(lst):
        n = len(lst)
    if n == 0:
        return [""]
    return [ str(x)+str(c) for c in genPerm(lst, n-1) for x in lst if str(x) not in str(c) ]

print("\n*** Permutações ***")
print(genPerm([1,2,3], 20))
print(genPerm("abc", 3))

def removeWhite(s):
    if len(s) == 0:
        return ""
    elif s[0] in " ": 
        return removeWhite(s[1:])
    return s[0] + removeWhite(s[1:])

def removeChars(s, chars=""):
    if len(s) == 0:
        return ""
    elif s[0] in chars: 
        return removeChars(s[1:], chars)
    return s[0] + removeChars(s[1:], chars)

print(removeWhite("madam i'm adam"))
print(isPal(removeWhite("x"))) # True
print(isPal(removeWhite("radar"))) # True
print(isPal(removeWhite("hello"))) # False
print(isPal(removeWhite(""))) # True
print(isPal(removeWhite("hannah"))) # True
print(isPal(removeWhite("madam i'm adam"))) # False
print(removeChars("mATeTE", "eia"))
