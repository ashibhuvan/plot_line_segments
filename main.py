import matplotlib.pyplot as plt
import json
json = json.loads(open('1-split.json').read())
#print(json['lines'])
print("hello world")
xlist = []
ylist = []

#print(json['lines'][0]['end'])

for i in json['lines']:
    temp = []
    temp.append(i['start'][0])
    temp.append(i['end'][0])


    y_temp = []
    y_temp.append(i['start'][1])
    y_temp.append(i['end'][1])

    xlist.extend(temp)
    xlist.append(None)
    ylist.extend(y_temp)
    ylist.append(None)

print(xlist)
print(ylist)
plt.autoscale(True, 'both')
plt.plot(xlist,ylist,'b-')
plt.show()

