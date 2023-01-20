#sample inputs
array_input = [[1,0,1,1], [1,1,0,1], [1,1,1,0]]
array_input_1 = [[1,1,0,0,1,1], [0,1,1,0,0,1], [0,0,0,1,0,1], [1,1,1,1,0,1]]
array_input_2 = [[1,0,0,0,0,1], [1,1,0,0,1,1], [0,1,1,1,1,0], [0,0,1,1,0,0]]
array_input_3 = [[1,0,0,0,0,1], [1,1,0,0,1,1], [0,1,1,0,1,0], [0,0,1,1,0,0]]

marked = set()

def river_lengths(array):

    rivers = []
       
    for row_pos, row in enumerate(array):
        for col_pos, element in enumerate(row):
            
            river_length_count = 0
            if element == 1 and (row_pos,col_pos) not in marked:
                marked.add((row_pos, col_pos))
                river_length_count += 1

                stack = [(row_pos, col_pos)]
                while stack:
                    current = stack.pop()
                    neighbor_positions = neighbors(current, array)
                    
                    for n in neighbor_positions:
                        r, c = n
                        if array[r][c] == 1 and n not in marked:
                            marked.add(n)
                            river_length_count += 1
                            stack.append(n)
                rivers.append(river_length_count)
    return rivers
                    

def neighbors(pos, array):
    x, y = pos
    neighbor_list = []

    #left neighbor
    if y > 0:
        neighbor_list.append((x, y-1))
    
    #right neighbor
    if y < len(array[x])-1:
        neighbor_list.append((x, y+1))

    #up neighbor
    if x > 0:
        neighbor_list.append((x-1, y))

    #down neighbor
    if x < len(array)-1:
        neighbor_list.append((x+1, y))

    return neighbor_list


if __name__ == "__main__":
    print(river_lengths(array_input))
