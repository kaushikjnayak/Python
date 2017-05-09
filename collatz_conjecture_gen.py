# Verify Collatz Conjecture upto n Natural number.
# https://en.wikipedia.org/wiki/Collatz_conjecture

def collatzgen(num):
  if type(num) == int:
    
    for i in range(1,num):
      iter = 0
      r = i
      while ( r != 1):
          if r % 2 == 0:
             r =  int(r/2)
          else: 
             r = 3*r + 1
          iter += 1
      print   ( "Number - {} ,final = {} ,Total iterations - {}".format(i,r,iter))    
  else:
     print ( "{} is non-numeric".format(num))

collatzgen(10000)
