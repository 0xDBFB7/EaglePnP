inputf = open('./Rev10.mnt','r')
output = open('./output.txt','a')
x1 = 5.0*25.4
width = 0.31496063*25.4
parts = {'0.1uf': [x1,2*25.4], '10uf': [x1+(width*1),2*25.4], '1k': [x1+(width*2),2*25.4], '10k': [x1+(width*3),2*25.4]}

def pick(loc):
    output.write('G00 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z5;' + '\n')
    output.write('G00 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z0;'+ '\n')
    output.write('G01 X' + str(loc[0]+(0.157480315)*25.4) + ' Y' + str(loc[1]) + ' Z0;'+ '\n')
    output.write('G00 X' + str(loc[0]+(0.157480315)*25.4) + ' Y' + str(loc[1]) + ' Z5;'+ '\n')
    output.write('G00 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z5;'+ '\n')
    output.write('M107;'+ '\n')
    output.write('G01 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z0;'+ '\n')
    output.write('G01 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z5;'+ '\n')
for line in inputf:
    temp=line.split()
    print(temp[4])
    if(temp[4] in parts):
        pick(parts[temp[4]])
        output.write('G00 X' + str(float(temp[1])*25.4) + ' Y' + str(float(temp[2])*25.4) + ' Z5;'+ '\n')
        output.write('G01 X' + str(float(temp[1])*25.4) + ' Y' + str(float(temp[2])*25.4) + ' Z0.2;'+ '\n')
        output.write('M108;'+ '\n')
        output.write('G01 X' + str(float(temp[1])*25.4) + ' Y' + str(float(temp[2])*25.4) + ' Z5;'+ '\n')
        output.write('M19 P' + str(temp[3]) + '\n')

