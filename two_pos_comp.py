__author__ = 'kaushik'

def string_match(a, b):
      ct = 0
      two_sbtr_a = {}
      two_sbtr_b = {}
      for i in range(len(a) - 1):
            two_sbtr_a[i] = a[i] + a [i + 1]

      for  j in range(len(b) - 1):
            two_sbtr_b[j] = b[j] + b [j + 1]
            if two_sbtr_a[j] == two_sbtr_b[j]:
                ct += 1
      return ct





print (string_match('abc', 'axc'))