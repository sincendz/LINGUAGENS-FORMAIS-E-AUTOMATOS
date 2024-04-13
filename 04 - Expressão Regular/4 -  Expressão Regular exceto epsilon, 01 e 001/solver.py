from regexp import *

def main():
    str = input()
    la = Literal('0')
    lb = Literal('1')
    C = Concat(Concat(la,Concat(Star(la),Star(Concat(lb,lb)))),Star(Concat(lb,la)))
    D = Concat(Star(lb),Star(la))
    E = Or(C,D)
    print( E.matches(str) )


if __name__ == "__main__":
    main()