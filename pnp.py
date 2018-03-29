import sys
input_file = open(sys.argv[1],'r')
#feeders = open('machine.json,'r')
output_file = open('./output.gcode','w+')

##############################

####Where's the rightmost output-side corner of the feeder on the bed?#######
feeder_offsets = [0,0,20]

#nozzle_locations defines the x,y,z coordinates that the nozzle will pick the part up from, relative to the feeder offsets defined above.
feeder_dict = {'0.1uf': {"nozzle_locations":[71.0,27.6,0], "index_locations":[71.0,27.6,0], "index_distances": [0,5,0]}, \
		    '1k': {"nozzle_locations":[71.0,27.6,0], "index_locations":[71.0,27.6,0], "index_distances": [0,5,0]}}

board_offsets = [0,-20,20]


safe_height = 35
index_register_feedrate = 300
index_feedrate = 100
rotate_feedrate = 10
rapid_feedrate = 5000
rapid_with_part_feedrate = 3000
##############################

#current_angle = 0

def pick(part, offset):
    output_file.write('G00 F{} Z{};\n'.format(rapid_feedrate,safe_height)) ##Raise to a safe height

    output_file.write('G00 X{} Y{};\n'.format(part["index_locations"][0],\
                                         part["index_locations"][1])) ##move over to the part index hole

    output_file.write('G01 F{} X{} Y{} Z{};\n'.format(index_register_feedrate, \
  					part["index_locations"][0]+offset[0],\
				        part["index_locations"][1]+offset[1],\
					part["index_locations"][2]+offset[2])) ##lower into the index hole

    output_file.write('G00 F{} X{} Y{} Z{};\n'.format(index_feedrate, \
					part["index_locations"][0]+offset[0]+part["index_distances"][0],\
	         		 	part["index_locations"][1]+offset[1]+part["index_distances"][1],\
					part["index_locations"][2]+offset[2]+part["index_distances"][2])) ##Index!

    output_file.write('G00 F{} Z{};\n'.format(rapid_feedrate,safe_height)) ##Raise to a safe height

    output_file.write('G00 F{} X{} Y{};\n'.format(index_register_feedrate, \
  					part["nozzle_locations"][0]+offset[0],\
				        part["nozzle_locations"][1]+offset[1])) #Align the nozzle with the part

    output_file.write('G00 F{} Z{};\n'.format(rapid_feedrate,part["nozzle_locations"][2]+offset[2])) ##Drop le nozzle

    output_file.write('M106;\n') ##Vacuum on
    output_file.write('G4 P500;\n') ##Wait for the part to be lifted
    output_file.write('G00 F{} Z{};\n'.format(rapid_with_part_feedrate, safe_height)) ##Raise to a safe height

def rotate(angle, feedrate):
    #todo: optimize direction.
    #global current_angle
    #The nozzle rotate system is set up to rotate once per mm.
    output_file.write('G01 F{} E{}'.format(feedrate*60,(angle/360.0)))

def place(location, offset):

    output_file.write('G00 F{} Z{};\n'.format(rapid_with_part_feedrate,safe_height)) ##Make sure we're at a safe height

    output_file.write('G00 X{} Y{};\n'.format(	location[0]+offset[0],\
						location[1]+offset[1])) ##Align the part

    output_file.write('G00 Z{};\n'.format(offset[2]))##Seat the part

    output_file.write('M107;\n')
    output_file.write('G4 P1000;\n') ##Wait for the part to fall

    output_file.write('G00 F{} Z{};\n'.format(rapid_feedrate,safe_height)) ##Raise to a safe height

for line in input_file:
    input_line=line.split()
    part_name = input_line[4]
    print(input_line)
    if(part_name in feeder_dict):
	print("Feeder entry exists, placing...")
        pick(feeder_dict[part_name],feeder_offsets)
	rotate(float(input_line[3]),rotate_feedrate)
        place([float(input_line[1]),float(input_line[2])],board_offsets)
    else:
	print("Feeder entry does not exist!")
output_file.close()
