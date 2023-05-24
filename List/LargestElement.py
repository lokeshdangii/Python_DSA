def getLargest(l):

    for x in l:
        for y in l:
            if y>x:
                break
        else:
            return x 
    else:
        return None


def gatMax(l):

    if not l:
        return None
    else:
        res = l[0]
        for i in range(1,len(l)):
            if l[i]> res:
                res  = l[i]

        return res

l1 = [10,20,5,25,40]
print(getLargest(l1))



