a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12,13]
c = []

#iterate through items in list a
for itema in a:
    #iterate through items in list b
    for itemb in b:
        #compare if item in list a equals item in list b
        if(itema == itemb):
            #add the equal item to list c
            c.append(itema)

#print(c) outputs [1, 1, 2, 3, 5, 8, 13]
#use a dictionary since a dictionary can't contain duplicate keys
c = list(dict.fromkeys(c))
#prints [1, 2, 3, 5, 8, 13]
print(c)  
