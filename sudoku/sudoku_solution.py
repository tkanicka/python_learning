import copy

def make_2d(sudoka_list, step):
    list_2d = []
    for i in range(0, len(sudoka_list), step):
        list_2d.append(sudoka_list[i: i + step])

    return list_2d

def print_sudoka(sudoka):
      for x in sudoka:
            print(x)

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

def valid(sudoka,position, position_value):
      row = check_row(sudoka, position, position_value)
      column = check_column(sudoka, position, position_value)
      box = check_square(sudoka, position, position_value)

      if row == False or column == False or box == False:
            return False

      return True


def solve_sudoka1(sudoka):
      if check_sudoka(sudoka) == True:
                  states = [sudoka]
                  while len(states) > 0:
                        current_sudoka = states.pop()
                        position = find_empty(current_sudoka)
                        if position == None:
                              return current_sudoka
                        for position_value in range(1, 10):
                              if valid(current_sudoka, position, position_value)== True:
                                    s = copy.deepcopy(current_sudoka)
                                    s[position[0]][position[1]] = position_value
                                    states.append(s)

file = open("sudoka.txt", "r")
text = file.read()
sudoka = []
numbers = ["0","1","2","3","4","5","6","7","8","9"]
if len(text) == 81:
      for x in text:
            if x in numbers:
                  sudoka.append(int(x))

sudoka = make_2d(sudoka, 9)

print_sudoka(sudoka)
print()
print_sudoka(solve_sudoka1(sudoka))







