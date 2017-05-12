import numpy as np


new = np.array([ 'Bengaluru', 'Mumbai', 'Chennai','Kolkata'])
old = np.array([ 'Bangalore', 'Bombay', 'Madras','Calcutta' ])
touse = np.array([ True,False,False,None ])

#equivalent to [ old if  touse[index(old)] is True or None else new; new if touse(new) is True else old]
print (np.where(touse,old,new))


#equivalent to [ new if  touse[index(new)] is True  or None else old; old if touse(old) is True else new]

print (np.where(touse,new,old))



