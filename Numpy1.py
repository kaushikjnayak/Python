import numpy as np

languages =  [ 'Mandarin ', 'Spanish', 'English', 'Hindi', 'Arabic', 'Portuguese', 'Bengali', 'Russian', 'Japanese', 'Punjabi' ]

speakers = [ 955, 405, 360, 310, 295, 215, 205, 155, 125, 100 ]

langnp   =  np.array(languages)
speaknp  = np.array(speakers, dtype=int)


#Generate a 4x2 array of Random numbers.
randomnum = np.random.randn(4,2)


print (randomnum)
print (randomnum.shape)

#Create a mxn (1x2) arrays with all elements as 0.
testnp = np.zeros((1,2))

#Create a mxn (1x2) arrays with all elements as 1.

testnp2 = np.ones((4,2))

print (testnp)
print (testnp2[1][1])

#converts speaknp into floating point
speaknp = speaknp.astype(np.float64)

print(speaknp[0])