#####################################
#         Functions                 #
#####################################
def array_to_string(arr):    
    str1 = ''
    for i in arr:
        str1 = str1 + i
    return str1

#####################################
#         Handle Data               #
#####################################

#    1     2   3   4   5
cell_data = ["aaa","c","e","b","d"]
grid_leng = len(cell_data)

#    3     1   1   1   1
cell_counts = []

#    123   4   5   6   7
cell_ch = 0
cell_tch = 0

# Counts array chars
# Tallies total chars
for i in range(grid_leng):
    cell_ch = len(cell_data[i])
    cell_tch = cell_tch + cell_ch
    
    cell_counts.append(cell_ch)

cell_tch = cell_tch + (3 * grid_leng)

print(f'GRID length:{grid_leng}')
print(f'cell length:{cell_tch}')
print(f'cell data_t: {cell_data}')
print(f'cell data_c: {cell_counts}')
print()

#####################################
#         Rows (entries)            #
#####################################





#####################################
#         Generate Grid             #
#####################################
desired_lines = 1
cell_heig = desired_lines * 3

# cell_heig = y
xe = cell_tch - 1
ye = cell_heig - 1
ze = 0
step_1 = 2
dist_1 = 4
step_2 = 4
dist_2 = 4

row = []
rows = 2

print(f"x_end: {xe}")
print(f"y_end: {ye}")
# print(f"z_end: {ze}")
print()

# x = row
# y = col
# Left = Min
# Right = Max


for z in range(rows):
    for y in range(cell_heig):
        for x in range(cell_tch):
            if (0 < x < xe) and (0 < y < ye):
                if (x == step_1):
                    row.append('a')
                    step_1 = step_1 + dist_1
                elif (x == step_2):
                    row.append('e')
                    step_2 = step_2 + dist_2
                else:
                    row.append('o')
            
            # Top            
            elif (x == 0) and (y == 0):
                row.append('1')
            elif (0 < x < xe) and (y == 0):
                row.append('2')
            elif (x == xe) and (y == 0):
                row.append('3')
            
            # Right
            elif (x == xe) and (0 < y < ye):
                row.append('4')

            # Bottom
            if z != ze:
                if (x == xe) and (y == ye):
                    row.append('5')
                elif (0 < x < xe) and (y > 0):
                    row.append('6')
                elif (x == 0) and (y == ye):
                    row.append('7')
    
                # Left
                elif (x == 0) and (0 < y < ye):
                    row.append('8')
    
                else: row.append('x')
            elif z == ze:
                if (x == xe) and (y == ye):
                    row.append('5')
                elif (0 < x < xe) and (y > 0):
                    row.append('6')
                elif (x == 0) and (y == ye):
                    row.append('7')
    
                # Left
                elif (x == 0) and (0 < y < ye):
                    row.append('8')
                
        row.append('\n')        

#####################################
#         Main Program              #
#####################################
row = array_to_string(row)
print(row)
