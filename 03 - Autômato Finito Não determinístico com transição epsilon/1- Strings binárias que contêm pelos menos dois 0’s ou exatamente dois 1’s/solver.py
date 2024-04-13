# Strings binárias que começam ou terminam com 01
edges = { (0, '') :  [1,2],
                   
          (1, '0') : [6],
          #(1, '1') : [6],
          
          (2, '1') : [3],
          #(2, '0') : [2],
          #(2, '') : [2],
          
          (3, '1') : [4],
          (3, '0') : [8],
          
          (4, '0') : [4],
          (4, '1') : [5],
          #(4, '') : [2],
          
          #(5, '0') : [6],
          (5, '1') : [5],

          (6, '0') : [7],
          #(6, '1') : [4],

          (7, '0') : [7],
          (7, '1') : [7],

          (8, '0') : [7],
          (8, '1') : [4]
 }
initial   = 0
accepting = [4,7] 

def epsilon_nfa(string, current, edges, accepting): 
    #print ("current: " + str(current) + "string: " + string )    
    if string == "":
        return  current in accepting       
    else:
        if (current, '') in edges:
          for next in edges[(current,'')]:
            if epsilon_nfa(string, next, edges, accepting):
                    return True
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if epsilon_nfa(string[1:], next, edges, accepting):
                    return True
        
        return False
        

string = input()
print (epsilon_nfa( string , initial, edges, accepting) )      