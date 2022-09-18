class Point:
    def __init__(self, x, y):
        self.x = x
        self.y =y
    
    def get_halfway_point(self, target):
        x = (self.x + target.x)/2
        y = (self.y + target.y)/2
        return Point(round(x,1), round(y,1))

p = Point(3,4)
q=Point(5,12)
r = p.get_halfway_point(q)
print(type(r))
print(r.x, r.y)