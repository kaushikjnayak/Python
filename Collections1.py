from collections import OrderedDict
customerorders = OrderedDict()
Nooforders = int(input())

for i in range(Nooforders):
    *item_name,price = input().split()
    item = ' '.join(item_name)
    if item in customerorders:
        customerorders[item] += int(price)
    else:
        customerorders[item] = int(price)
for item,cost in customerorders.items():
    print (item,cost)