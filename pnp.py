inputf = open('./Rev10.mnt','r')
output = open('./output.gcode','w+')
index_part_0_x = 71.0
index_part_0_y = 27.6
index_part_0_z = 0
nozzle_part_0_x = 111.25
nozzle_part_0_y = 76.2
nozzle_part_0_z = 22.7
nozzle_null_x = 20
nozzle_null_y = 20
nozzle_null_z = 32
safe_height = 35
width = 11 #x
parts = {'0.1uf': 0, '1k': 1, '10uf': 2}

def pick(loc):
    output.write('G00 Z' + str(safe_height) + ';\n') ##Raise to a safe height
    output.write('G00 X' + str(index_part_0_x-(loc*width)) + ' Y' + str(index_part_0_y) + ' Z' + str(safe_height) + ';\n') ##move over to the part index hole
    output.write('G00 X' + str(index_part_0_x-(loc*width)) + ' Y' + str(index_part_0_y) + ' Z' + str(0) + ';\n') ##lower into the index hole
    output.write('G01 F100 X' + str(index_part_0_x-(loc*width)) + ' Y' + str(index_part_0_y+4.0) + ' Z' + str(0) + ';\n') ##index
    output.write('G00 X' + str(index_part_0_x-(loc*width)) + ' Y' + str(index_part_0_y+4) + ' Z' + str(safe_height) + ';\n')##lift back up
    output.write('G00 X' + str(nozzle_part_0_x-(loc*width)) + ' Y' + str(nozzle_part_0_y) + ' Z' + str(safe_height) + ';\n')##Bring the nozzle over
    output.write('M107;'+ '\n') ##Vacuum on
    output.write('G00 X' + str(nozzle_part_0_x-(loc*width)) + ' Y' + str(nozzle_part_0_y) + ' Z' + str(nozzle_part_0_z) + ';\n')##Drop the nozzle and the bass
    output.write('G00 X' + str(nozzle_part_0_x-(loc*width)) + ' Y' + str(nozzle_part_0_y) + ' Z' + str(safe_height) + ';\n')##and back up.
    ##Here we should turn the bed or the part.
def place(loc):
    output.write('G00 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z' + str(safe_height) + ';\n')
    output.write('G00 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z' + str(nozzle_null_z) + ';\n')
    output.write('M108;'+ '\n')
    output.write('G4 P1000;'+ '\n')
    output.write('G00 X' + str(loc[0]) + ' Y' + str(loc[1]) + ' Z' + str(safe_height) + ';\n')
for line in inputf:
    temp=line.split()
    print(temp[4])
    if(temp[4] in parts and (int(temp[3]) == 270 or int(temp[3]) == 90)):
        pick(parts[temp[4]])
        place([nozzle_null_x+float(temp[1]),nozzle_null_y+float(temp[2])])
output.close()
