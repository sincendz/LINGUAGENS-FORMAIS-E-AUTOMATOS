def sufixos(x):
    if x == "":
        return [""]
    else:
        a = x[0]
        z = x[1:]
        return [x] + sufixos(z)
        
def main():
    x = input()
    
    print( sufixos(x) )


if __name__ == "__main__":
    main()
    