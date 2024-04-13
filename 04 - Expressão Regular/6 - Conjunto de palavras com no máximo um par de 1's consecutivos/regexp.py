class Reg: 
  def matches(w) -> bool:
    pass  
  
class Epsilon(Reg):
  def __init__(self):
    self.re1 = ""
  def __str__(self) -> str:
    return "e"
  def matches(self, w) -> bool:
    return w == ""
  

class Empty(Reg):
  def __init__(self):
    self.re1 = []
  def __str__(self) -> str:
    return "{}"
  def matches(self, w) -> bool:
    return w == []
  
  
class Literal(Reg):
  def __init__(self, a):
    self.re1 = a
  def __str__(self) -> str:
    return str(self.re1)    
  def matches(self, w) -> bool:
    return w == self.re1    
  def language(self):
    yield self.re1
class Or(Reg):
  def __init__(self, re1, re2):
    self.re1 = re1
    self.re2 = re2          
  def __str__(self):
     return "(" + str(self.re1) + "+" + str(self.re2) + ")"
  def matches(self, w):
    return self.re1.matches(w) or self.re2.matches(w)
 
    
    
        

class Concat(Reg):
  def __init__(self, re1, re2):
    self.re1 = re1
    self.re2 = re2    
  def __str__(self):
    return str(self.re1) + str(self.re2)
  def matches(self, w):
    for pos in range( len(w) +1):
      #print(w[0:pos] + "," + w[pos:])
      if self.re1.matches( w[0:pos] ) and self.re2.matches(w[pos:] ):
        return True
    return False
  

  

class Star(Reg):
  def __init__(self, re1):
    self.re1 = re1
  def __str__(self):
    return "(" + str(self.re1) + ")*"
  def matches(self, w):
    if w == "" :
      return True
    if len(w) == 1:
      return self.re1.matches(w)    
    else:
      for pos in range( len(w) + 1):
        if self.re1.matches( w[0:pos] ) and self.matches(w[pos:] ):
          return True
      return False
 
