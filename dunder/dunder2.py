class mylist(list):
    def __add__(self,other):
        if len(self)!= len(other):
            return "bu elemanlar toplanamaz"
        else:
            result= mylist()
            for i in range(len(self)):
                result.append(self[i] + other[i])
        return result

liste1=mylist([1,2,3])
liste2=mylist([4,5,6])

print(liste1 + liste2)
