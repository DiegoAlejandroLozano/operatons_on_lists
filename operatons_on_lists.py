def ejecutar_comandos(dic_comandos):
    mi_lista = []
    for clave, valor in dic_comandos.items():
        if clave.find('insert') != -1:
            mi_lista.insert(valor[0], valor[1])
        elif clave.find('print') != -1:
            print(mi_lista)
        elif clave.find('remove') != -1:
            mi_lista.remove(valor[0])
        elif clave.find('append') != -1:
            mi_lista.append(valor[0])
        elif clave.find('sort') != -1:
            mi_lista.sort()
        elif clave.find('pop') != -1:
            mi_lista.pop()
        elif clave.find('reverse') != -1:
            mi_lista.reverse()


def main():
    n = int(input())
    dic_comandos = {}
    for _ in range(n):
        nombre_comando, *argumentos = input().split(' ')
        lista_comandos = [ int(element) for element in argumentos ] 
        dic_comandos[str(_)+nombre_comando] = lista_comandos
    ejecutar_comandos(dic_comandos)    


if __name__ == '__main__':
    main()
