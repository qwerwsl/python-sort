newlist=[]
def myreverse(alist):
    for i in range(len(alist)):
        i += 1
        newlist.append(alist[len(alist)-i])
    return newlist
print(myreverse([5.7,8,36,58,20]))
