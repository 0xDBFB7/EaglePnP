inputf = open('./Rev10.mnt','r')
output = open('./output.txt','a')
x1 = 0.0
width = 0.31496063
parts = {'0.1uf': [x1,0], '10uf': [x1+(width*1),0], '1k': [x1+(width*2),0], '10k': [x1+(width*3),0]}

def pick(loc):
    output.write('G00 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z0.5;' + '\n')
    output.write('G00 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z-0.1;'+ '\n')
    output.write('G01 X' + str(loc[0]+0.157480315) + ' Y' + str(loc[1]) + ' Z-0.1;'+ '\n')
    output.write('G00 X' + str(loc[0]+0.157480315) + ' Y' + str(loc[1]) + ' Z0.5;'+ '\n')
    output.write('G00 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z0.5;'+ '\n')
    output.write('M19 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z0.5;'+ '\n')
    output.write('M106;'+ '\n')
    output.write('G01 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z0;'+ '\n')
    output.write('G01 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z0.5;'+ '\n')
for line in inputf:
    temp=line.split()
    print(temp[4])
    if(temp[4] in parts):
        pick(parts[temp[4]])
        output.write('G00 X' + str(temp[1]) + ' Y' + str(temp[2]) + ' Z1;'+ '\n')
        output.write('G01 X' + str(temp[1]) + ' Y' + str(temp[2]) + ' Z0.2;'+ '\n')
        output.write('M107;'+ '\n')

