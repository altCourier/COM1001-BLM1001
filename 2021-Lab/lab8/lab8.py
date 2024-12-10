info=input().split(",")
info=list(map(int,info)) #to make strings into integers


def place_tables(info):
    #arrange them in the right place and the left place
    left_tables=[]
    right_tables=[]
    for i in range(1,info[0]+1):
        if i%2==0:
            if i in info and i!=info[0]:
                right_tables.append("#")
            else:
                right_tables.append(i)
        else:
            if i in info and i!=info[0]:
                left_tables.append("#")
            else:
                left_tables.append(i)

    #find the sublist of them
    sitting_together = [] #final list
    sitting = [] #blank list for nested lists
    count = 0
    for i in range(len(right_tables)):
        if str(right_tables[i]).isdigit() and str(left_tables[i]).isdigit():
            sitting.extend([right_tables[i], left_tables[i]])
            sitting.sort()
            sitting_together.append(sitting)
        sitting=[]
    sitting_near(right_tables,sitting_together)
    sitting_near(left_tables,sitting_together)

    return len(sitting_together) #return the number of the people who can sit together

def sitting_near(liste,sublists):
    """Function for people who sit together so we don't need to write it for left side and right side each"""

    sits=[] # blank list for creating final nested list
    for count in range(len(liste)-1):
        if str(liste[count]).isdigit() and str(liste[count+1]).isdigit(): #to control if they are occupied
            sits.extend([liste[count],liste[count+1]])
            sits.sort()
            sublists.append(sits)
            sits.clear() #to clear the list
    return sublists

print(place_tables(info))