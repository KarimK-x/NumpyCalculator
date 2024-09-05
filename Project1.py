# *********FINISHED*********
# Function calculating the statistics about each row,column, and total of a 2d Array

import numpy as np
np.set_printoptions(precision=1) #numpy outputs will be 1dp for readability

print("Enter your array of 9 numbers! ")
oldlist = [int(input("Enter a num: ")) for i in range(9)]
    
oldlist = np.array(oldlist)
oldlist = oldlist.reshape(3,3)

def calculate(mylist):
    
    
    mymean = [np.mean(mylist,axis =1), np.mean(mylist, axis = 0), round(np.mean(mylist), 1)]
    myvar = [np.var(mylist,axis =1), np.var(mylist, axis = 0), round(np.var(mylist),1)]
    mystdev = [np.std(mylist,axis =1), np.std(mylist, axis = 0), round(np.std(mylist),1)]
    mymax = [np.max(mylist,axis =1), np.max(mylist, axis = 0), np.max(mylist)]
    mymin = [np.min(mylist,axis =1), np.min(mylist, axis = 0), np.min(mylist)]
    mysum = [np.sum(mylist,axis =1), np.sum(mylist, axis = 0), np.sum(mylist)]
    
    #storing results in dictionary
    result = {
        "mean" : mymean,
        "variance": myvar,
        "stdev": mystdev,
        "max" : mymax,
        "minim" : mymin,
        "sum" : mysum
    }
    
    row_labels = ["Rows", "Columns", "Total"]
    
    for key, value in result.items():
        print(f"------{key.upper()}------")
        for index,item in enumerate(value):
            print(f"{row_labels[index]}: {item}")
        print('---------')

    return 0

calculate(oldlist)



