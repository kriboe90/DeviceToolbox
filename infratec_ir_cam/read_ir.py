from io import open
import numpy as np

def read_ir_image(file):
    all_temperatures = []
    with open(file, 'r', encoding='WINDOWS 1252') as ir_file:
        read_data = False
        for line in ir_file:
            if 'Data' in line:
                read_data = True
                continue
            if read_data == True:
                line = line.replace(',', '.')
                line = line.replace(';', ' ')
                line_data = line.split()
                print(line_data)
                line_temperatures = list(map(float, line_data))
                if line_temperatures:
                    all_temperatures.append(line_temperatures)
        return np.array(all_temperatures)