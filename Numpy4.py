import numpy as np


arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#print 3rd element(2nd index ) element in first (o index th ) array
print (arr2d[0,2])

#print 3rd element(2nd index ) element in first(0:1)  array

print (arr2d[0:1,2])

languages =  [ 'Mandarin ', 'Spanish', 'English', 'Hindi', 'Arabic', 'Portuguese', 'Bengali', 'Russian', 'Japanese', 'Punjabi' ]

speakers = [ 955, 405, 360, 310, 295, 215, 205, 155, 125, 100 ]

langnp   =  np.array(languages)
speaknp  = np.array(speakers, dtype=int)

#Boolean Indexing.
print(langnp ==  'English')
print (speaknp[speaknp >= 300])

print (langnp[speaknp >= 300])

#overwrite langnp to contain all strings greater than 300 to contain avrage population
speaknp[speaknp >= 300] = np.average(speakers)

print(speaknp)