# Exemplo de NFA que aceita as strings binárias com o penúltimo dígito igual a 1
edges = {  (0,'0') : [0,1],
           (0,'1') : [0],
           (1,'0') : [0],
           (1,'1') : [2],
}
initial   =  0 # estado inicial
accepting = [2] # conjunto de estado final

def nfa(string, current, edges, accepting): 
    if string == "":
        return  current in accepting        
    else:
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if nfa(string[1:], next, edges, accepting):
                    return True
        return False
        

string = input()
print ( nfa(string, initial, edges, accepting) )