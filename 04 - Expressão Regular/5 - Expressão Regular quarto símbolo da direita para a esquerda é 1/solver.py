from regexp import *

def main():
    str = input()
    la = Literal('0')
    lb = Literal('1')
    C = Or(la,lb)
    D = Concat(Concat(C,C),Concat(C,Concat(lb,Epsilon())))
    E = Concat(D,Star(C))
    print( E.matches(str) )


if __name__ == "__main__":
    main()