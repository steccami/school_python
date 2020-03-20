class atom(object):
    #__x = 10000 #private
    x=10000
    atno_to_symbol = {1:"H",2:"He",3:"Li",4:"Be",5:"B",6:"C"}
    
    def __init__(self,atno,x,y,z):
        self.atno = atno
        self.position = (x,y,z)
    
    def symbol(self): # a class method
        #self.x = 3 #test instance variable
        #atom.x = 3 #test static variable
        return self.atno_to_symbol[self.atno]
        
    def __repr__(self): # overloads printing
        return '%d %10.4f %10.4f %10.4f Variable x=%d'%(self.atno, self.position[0],self.position[1],self.position[2], self.x)
    
    def static_method(a,b):#This is a static method!
        return a + " " + b + " from static method"

at = atom(6,0.0,1.0,2.0)
at.symbol()
#print(at.x) #if x is public
#print(atom.static_method("a","b"))
print(at)
#at2= atom(3,0.0,3.0,3.0)
#print(at2)

'''
class atom_child(atom):
    def new_method(self):
        print("I'm just a child")
        
c = atom_child(5,0.0,1.0,2.0)
print(c)
c.new_method()
'''