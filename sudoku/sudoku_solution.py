s1 = [[2, 0, 4, 0, 0, 8, 0, 0, 9],
      [0, 0, 9, 0, 0, 0, 2, 0, 8],
      [0, 6, 0, 0, 0, 2, 0, 3, 0],
      [0, 2, 5, 0, 0, 6, 0, 0, 4],
      [0, 4, 6, 0, 0, 0, 7, 8, 0],
      [7, 0, 0, 2, 0, 0, 5, 6, 0],
      [0, 9, 0, 6, 0, 0, 0, 2, 0],
      [4, 0, 7, 0, 0, 0, 8, 0, 0],
      [6, 0, 0, 4, 0, 0, 9, 0, 3]]


s1s = [[2, 7, 4, 3, 1, 8, 6, 5, 9],
      [3, 1, 9, 7, 6, 5, 2, 4, 8],
      [5, 6, 8, 9, 4, 2, 1, 3, 7],
      [1, 2, 5, 8, 7, 6, 3, 9, 4],
      [9, 4, 6, 1, 5, 3, 7, 8, 2],
      [7, 8, 3, 2, 9, 4, 5, 6, 1],
      [8, 9, 1, 6, 3, 7, 4, 2, 5],
      [4, 3, 7, 5, 2, 9, 8, 1, 6],
      [6, 5, 2, 4, 8, 1, 9, 7, 3]]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_empty(sudoka):
      for x in range(len(sudoka)):
            for y in range(len(sudoka[x])):
                  if sudoka[x][y] == 0:
                        return (x,y)
      return None
def check_row(sudoka, position, position_value):
      for i in range(len(sudoka)):
            if sudoka[position[0]][i] == position_value and position[1] != i:
                  return False
      return True
def check_column(sudoka, position,position_value ):
      for i in range(len(sudoka)):
            if sudoka[i][position[1]] == position_value and position[0] != i:
                  return False
      return True
def check_square(sudoka,position, position_value):
      square_position_row = position[0] // 3
      square_position_column = position[1] // 3

      for i in range(3*square_position_row, 3*square_position_row + 3):
            for j in range(3*square_position_column, 3*square_position_column + 3):
                  if sudoka[i][j] == position_value and (i,j) != position:
                        return False
      return True

def check_sudoka(sudoka):
      for x in range(len(sudoka)):
            for y in range(len(sudoka)):
                  if sudoka[x][y] != 0:
                        row = check_row(sudoka, position = (x,y),position_value = sudoka[x][y])
                        column = check_column(sudoka, position = (x,y),position_value = sudoka[x][y])
                        box = check_square(sudoka, position = (x,y),position_value = sudoka[x][y])

                        if row == False or column == False or box == False:
                              return False

      return True


def solve_sudoka(sudoka):
      if find_empty(sudoka) == None and check_sudoka(sudoka) == True:
            return sudoka

      else:
            states = [sudoka]
            while len(states)>0:
                  current_sudoka = states.pop()
                  if check_sudoka(current_sudoka) == True:

                        if find_empty(current_sudoka) == None:
                              return current_sudoka

                        else:
                              print(current_sudoka)
                              position = find_empty(current_sudoka)
                              for position_value in range(10):
                                    if check_square(current_sudoka,position, position_value) \
                                            and check_column(current_sudoka,position, position_value)\
                                            and check_row(current_sudoka,position, position_value) == True:
                                          current_sudoka[position[0]][position[1]] == position_value
                                          states.append(current_sudoka)

                                    current_sudoka[position[0]][position[1]] == 0
            return False

print(solve_sudoka(s1))






