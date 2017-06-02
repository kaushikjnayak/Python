def merge_the_tools(string, k):
    # your code goes here

    for i in range(0,len(string),k):
        t_ = string[i:i + k ]
        s = []
        [ s.append(i) for i in t_ if i not in s ]
        print (''.join(s))

string = input()
k = int(input())

merge_the_tools(string,k)