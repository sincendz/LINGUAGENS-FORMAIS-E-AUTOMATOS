
def main():
    
    sigma = eval(input())
    (states1, edges1, initial1, final1) = eval(input())
    (states2, edges2, initial2, final2) = eval(input())
    
    #adicionando um par ordenado relacionando
    #os dois autômatos 
    states3 = []
    for x in states1:
        for y in states2:
            states3.append( (x,y) )
    
    
    edges3 = {}
    #edges3[ ((1,2), '0')] = (2,3)
    edges3 = {}
    for state_pair in states3:
        for symbol in sigma:
            state1, state2 = state_pair
            new_state1 = edges1.get((state1, symbol))
            new_state2 = edges2.get((state2, symbol))
            if new_state1 is not None and new_state2 is not None:
                new_state_pair = (new_state1, new_state2)
                edges3[(state_pair, symbol)] = new_state_pair

    
    final3 = []
    for x in final1:
        for y in final2:
            final3.append( (x,y) )
    
    initial3 = (initial1, initial2)

    
    #teste(states3, edges3, initial3, final3)             


