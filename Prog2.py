class reverse:
    def rev(self, text):
        words = text.split()
        rev = words[::-1]
        return "".join(rev)
        
obj = reverse()
print(obj.rev("Python is very easy"))