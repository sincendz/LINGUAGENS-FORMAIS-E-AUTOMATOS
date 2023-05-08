def prefixo(x, y):
    ## Coloque seu código aqui
    if x == "":
        return True
    elif x != "" and y == "":
        return False
    else:
        a = x[0]
        z = x[1:]
        b = y[0]
        w = y[1:]
        return a == b and prefixo(z,w)
def main():
    x = input()
    y = input()
    print( prefixo(x,y) )


if __name__ == "__main__":
    main()