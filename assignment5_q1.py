 
class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    
    def sqSum(self):
        sum=self.x**2+self.y**2+self.z**2
        return(sum)

obj= Point(2,4,6)
print(obj.sqSum())


        