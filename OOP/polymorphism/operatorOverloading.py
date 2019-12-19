# class book:
#     def __init__(self,pages):
#         self.pages=pages
#
#     def __str__(self):
#         return str(self.pages)
#
#     def __add__(self, other):     #magic method
#         return (self.pages+other.pages)
#
# b1=book(100)
# b2=book(200)
# print(b1)
# print(b1+b2) #whenever there is an operator used between objects,the pgm checks for a corresponding special method;here it is '__add__'




# class book:
#     def __init__(self,pages):
#         self.pages=pages
#
#     def __str__(self):
#         return str(self.pages)
#
#     def __add__(self, other):
#         return book(self.pages+other.pages)
#
# b1=book(100)
# b2=book(200)
# b3=book(300)
# print(b1+b2+b3)





# class book:
#     def __init__(self,pages):
#         self.pages=pages
#
#     def __str__(self):
#         return str(self.pages)
#
#     def __sub__(self, other):
#         return book(self.pages-other.pages)
#
# b1=book(200)
# b2=book(100)
# print(b1-b2)


#special case for sub using add mehtod:
# class book:
#     def __init__(self,pages):
#         self.pages=pages
#
#     def __str__(self):
#         return str(self.pages)
#
#     def __add__(self, other):
#         return book(self.pages-other.pages)
#
# b1=book(200)
# b2=book(100)
# print(b1+b2)
#just the method name and operator need to be same





class book:
    def __init__(self,pages):
        self.pages=pages

    def __str__(self):
        return str(self.pages)

    def __truediv__(self, other):
        return book(self.pages/other.pages)

b1=book(200)
b2=book(100)
print(b1/b2)



