from regexp import *

def main():
    str = input()
    la = Literal('0')
    lb = Literal('1')
    # A = Star(la)
    # B  = Concat(A,Concat(lb,A))
    # C = Concat(B,Concat(lb,A))
    # D = Or(B,C)

    la = Literal('0')
    lb = Literal('1')
    A = Star(la)
    B  = Concat(A,Concat(lb,A))
    C = Concat(B,Concat(lb,A))
    D = Or(B,C)
    E = Or(A,D)
    F = Concat(C,Concat(la,Concat(lb,A)))
    G = Or(C,D)
    H = Or(G,Or(A,F))
    print( H.matches(str) )


if __name__ == "__main__":
    main()