import os
path = '/home/tarsier1/Desktop/uav_13_annotations_xml'
listPath = sorted(os.listdir(path))
print(listPath)
for i in listPath:
    number, extension = i.split('.')
    print(number)
    os.rename(path + '/' + i, path + '/' + number.zfill(12) + '.xml')
