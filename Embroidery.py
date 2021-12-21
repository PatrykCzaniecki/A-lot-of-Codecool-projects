def draw_rectangle(width, height, border_width, fill_color, border_color):
    if border_width % 2 == 0:
        variable = width
    else:
        variable = width - 1
    for row in range(height):
        for col in range(variable):
            if border_width == 0:
                print(f"{border_color} ", end = "")    
            if border_width == 1:
                if row == 0 or row == 5:
                    print(f"{border_color} ", end = "")
                elif col == 0:
                    print(f"{border_color} ", end = "")
                elif ((col == 5 and row == 1) or (col == 5 and row == 2) or 
                    (col == 5 and row == 3) or (col == 5 and row == 4)):
                    print(f"{border_color} ", end = "")
                    continue
                elif (row == 1 or row == 2 or row == 3 or row == 4):
                    print(f"{fill_color} ", end = "")
            if border_width == 2:
                if row == 0 or row == 1 or row == 4 or row == 5:
                    print(f"{border_color} ", end = "")
                    continue
                elif col == 0 or col == 1:
                    print(f"{border_color} ", end = "")
                    continue
                elif ((col == 5 and row == 2) or (col == 5 and row == 3) or 
                    (col == 6 and row == 2) or (col == 6 and row == 3)):
                    print(f"{border_color} ", end = "")
                    continue
                elif (row == 2 or row == 3):
                    print(f"{fill_color} ", end = "")
                    continue
        print()

# width = 7 
# height = 6
# border_color = 2
# fill_color = 4
# border_width = 1 
# draw_rectangle(width, height, border_width, fill_color, border_color) 

def draw_triangle(width, height, fill_color, border_color, fill_inside_color):
    for row in range(height):
        for col in range(width):
            if row == 0 and row + col == 3:
               print(f"{fill_color} ", end = "")
               continue
            elif row == 3:
                print(f"{fill_color} ", end = "")
                continue
            elif row == 1 and (row + col == 3 or col - row == 3):
                print(f"{fill_color} ", end = "")
                continue
            elif row == 1 and col + row == 4:
                print(f"{fill_inside_color} ", end = "")
                continue
            elif row == 2 and (row + col == 3 or col - row == 3):
                print(f"{fill_color} ", end = "")
                continue
            elif row == 2 and (row + col == 5 or col - row == 2 or col + row == 4):
                print(f"{fill_inside_color} ", end = "")
                continue
            else:
                print(f"{border_color} ", end = "")
                continue 
        print()

# width = 7
# height = 4
# border_color = 0
# fill_color = 1
# fill_inside_color = 2
# draw_triangle(width, height, fill_color, border_color, fill_inside_color)

def draw_christmas_tree(width, height, fill_color, fill_inside_color, border_color):
    for row in range(height):
        for col in range(width):
            if row == 0 and col == 5:
                print(f"{fill_color} ", end = "")
                continue
            elif (row == 1 or row == 2) and (row + col == 5 or col - row == 5):
                print(f"{fill_color} ", end = "")
                continue
            elif (row == 3 or row == 4 or row == 5) and (row + col == 7 or col - row == 3):
                print(f"{fill_color} ", end = "")
                continue
            elif (row == 6 or row == 7 or row == 8) and (row + col == 9 or col - row == 1):
                print(f"{fill_color} ", end = "")
                continue
            elif (row == 9 or row == 10) and (row + col == 11 or col - row == -1):
                print(f"{fill_color} ", end = "")
                continue
            elif row == 11:
                print(f"{fill_color} ", end = "")
                continue
            elif col == 5 and row != 0:
                print(f"{fill_inside_color} ", end = "")
                continue
            elif row == 2 and (col - row == 2 or col - row == 4):
                print(f"{fill_inside_color} ", end = "")
                continue
            elif row == 4 and (col - row == 0 or col - row == 2):
                print(f"{fill_inside_color} ", end = "")
                continue  
            elif row == 5 and (col - row == -2 or col - row == -1 or col - row == 1 or col - row == 2):
                print(f"{fill_inside_color} ", end = "")
                continue
            elif row == 6 and (col - row == -2 or col - row == 0):
                print(f"{fill_inside_color} ", end = "")
                continue   
            elif row == 7 and (col - row == -4 or col - row == -3 or col - row == -1 or col - row == 0):
                print(f"{fill_inside_color} ", end = "")
                continue  
            elif row == 8 and (col - row == -6 or col - row == -5 or col - row == -4 or col - row == -2 or col - row == -1 or col - row == 0):
                print(f"{fill_inside_color} ", end = "")
                continue  
            elif row == 9 and (col - row == -6 or col - row == -5 or col - row == -3 or col - row == -2):
                print(f"{fill_inside_color} ", end = "")
                continue 
            elif row == 10 and (col - row == -8 or col - row == -7 or col - row == -6 or col - row == -4 or col - row == -3 or col - row == -2):
                print(f"{fill_inside_color} ", end = "")
                continue 
            else:
                print(f"{border_color} ", end = "")
        print()
    print()

# width = 11
# height = 12
# border_color = 0
# fill_color = 1
# fill_inside_color = 2
# draw_christmas_tree(width, height, fill_color, fill_inside_color, border_color)

# def draw_circle(radius):
#     matrix = []
#     return matrix

# def embroider(matrix, color_scheme):
#     for row in matrix:
#         for cell in row:
#             print(color_scheme[cell], end='')
#         print()
#     print()

# if __name__ == '__main__':
#     color_scheme = {0: ' ', 1: '*', 2: '.'}
    # embroider([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0], [0, 1, 2, 2, 2, 1, 0], [1, 1, 1, 1, 1, 1, 1]], color_scheme)

    # This should have the same output:
    # embroider(draw_triangle(4, border_color=1, fill_color=2), color_scheme)