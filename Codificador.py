from __future__ import print_function
from __future__ import division
from functools import*
#Author:A01374009
#convert string to hex
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)

#convert hex repr to string
def toStr(s):
    return s and chr(int(s[:2], base=16)) + toStr(s[2:]) or ''
def main():
    print("Bienvenido al decodificador y codificador")
    print("¿Que deseas hacer?, (escribe un numero)")
    print("1.CODIFICAR")
    print("2.DECODIFICAR")
    print("3.Salir")
    opcion =int(input("Opcion:  "))
    while opcion != 3:
        if opcion == 1:
            s=(input("Introdusca el texto que quiere codificar: "))
            print(toHex(s))
        elif opcion==2:
            s=(input("Introdusca el texto que quiere codificar: "))
            print(toStr(s))
        else:
            print("Opcion no valida")
        opcion =int(input("Opcion:  "))
main()
    
