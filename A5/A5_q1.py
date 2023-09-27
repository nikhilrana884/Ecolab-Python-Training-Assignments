class Triangle:
    pass
#valid triangle
t1 = Triangle()
t1.s1=3
t1.s2=4
t1.s3=5

#invalid triangle
t2 = Triangle()
t2.s1=4
t2.s2=8
t2.s3=16  


class Circle: 
    pass


c=Circle()
c.radius=7


def perimeter(obj):
    if type(obj) is Triangle:
        if obj.s1>0 and obj.s2>0 and obj.s3>0 and \
            obj.s1+obj.s2 > obj.s3 and \
            obj.s2+obj.s3 > obj.s1 and \
            obj.s1+obj.s3 > obj.s2:
            return obj.s1+obj.s2+obj.s3
        else:
            return float('nan')

    if type(obj) is Circle:
        return 2 * 3.14 * obj.radius
    else:
        return float('nan')
    
print(perimeter(t1))
print(perimeter(t2))
print(perimeter(c))