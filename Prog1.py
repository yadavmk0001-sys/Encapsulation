class myclass:
    
    __privateVar = 27
    
    def __privMeth(self):
        print("I'm inside a myclass")
    
    def hello(self):
        print("Private variable value is : ", myclass.__privateVar)
        
a = myclass()
a.hello()
a._myclass__privMeth()