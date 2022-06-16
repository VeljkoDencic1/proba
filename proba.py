from collections import Counter
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = input()
    lista = Counter(map(int,input().split()))
    ljudi = input()
    
    N = int(n)
    M = int(ljudi)
    zarada = 0
    
    for dete in range(M):
        xi, vrsta = map(int,input().split())
        if vrsta in lista and lista[vrsta] > 0:
            lista[vrsta] -= 1
            zarada += xi
    print(zarada)
    print (lista)
    
    return 0

if __name__ == '__main__':
    main()



    # proba za gits