board = [
  ['', '', '', 'X', '', '', '', ''],
  ['', '', '', '', '', '', 'X', ''],
  ['', '', 'X', '', '', '', '', ''],
  ['', '', '', '', '', '', '', 'X'],
  ['', 'X', '', '', '', '', '', ''],
  ['', '', '', '', 'X', '', '', ''],
  ['X', '', '', '', '', '', '', ''],
  ['', '', '', '', '', 'X', '', '']
]

def printBoard(board):
  print('---------------------------------')
  for i in range(8):
    line = '| '
    for j in range(8):
      p = board[i][j]
      if (p == ''):
        line = line + ' ' + ' | '
      else:
        line = line + board[i][j] + ' | '
    print(line)
    print('---------------------------------')

printBoard(board)

def fitness(board):
      # checking horizontal lines
  h = 0
  for i in range (8):
    queensPerLine = -1;
    for j in range (8):
      if (board[i][j] == 'X'):
        queensPerLine = queensPerLine + 1
    if (queensPerLine > 0):
      h = h + queensPerLine

  # checking vertical lines
  v = 0
  for i in range (8):
    queensPerLine = -1;
    for j in range (8):
      if (board[j][i] == 'X'):
        queensPerLine = queensPerLine + 1
    if (queensPerLine > 0):
      v = v + queensPerLine

  # Checking transverse white lines
  tw = 0
  wtl = [
    [[0,0], [1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7]],
    [[0,2], [1,3], [2,4], [3,5], [4,6], [5,7]],
    [[0,4], [1,5], [2,6], [3,7]],
    [[0,6], [1,7]], 
    [[2,0], [3,1], [4,2], [5,3], [6,4], [7,5]],
    [[4,0], [5,1], [6,2], [7,3]],
    [[6,0], [7,1]],
    [[0,2], [1,1], [2,0]],
    [[0,4], [1,3], [2,2], [3,1], [4,0]],
    [[0,6], [1,5], [2,4], [3,3], [4,2], [5,1], [6,0]],
    [[1,7], [2,6], [3,5], [4,4], [5,3], [6,2], [7,1]],
    [[3,7], [4,6], [5,5], [6,4], [7,3]],
    [[5,7], [6,6], [7,5]]
  ]

  for i in range (13):
    tl = wtl[i]
    queensPerLine = -1;
    for j in range (len(tl)):
      current = tl[j]
      if (board[current[0]][current[1]] == 'X'):
        queensPerLine = queensPerLine + 1
    if (queensPerLine > 0):
      tw = tw + queensPerLine

  # Checking transverse black lines
  tb = 0
  btl = [
    [[5,0], [6,1], [7,2]],
    [[3,0], [4,1], [5,2], [6,3], [7,4]],
    [[1,0], [2,1], [3,2], [4,3], [5,4], [6,5], [7,6]],
    [[0,1], [1,2], [2,3], [3,4], [4,5], [5,6], [6,7]],
    [[0,3], [1,4], [2,5], [3,6], [4,7]],
    [[0,5], [1,6], [2,7]],
    [[0,1], [1,0]],
    [[0,3], [1,2], [2,1], [3,0]],
    [[0,5], [1,4], [2,3], [3,2], [4,1], [5,0]],
    [[0,7], [1,6], [2,5], [3,4], [4,3], [5,2], [6,1], [7,0]],
    [[2,7], [3,6], [4,5], [5,4], [6,3], [7,2]],
    [[4,7], [5,6], [6,5], [7,4]],
    [[6,7], [7,6]]       
  ]

  for i in range (13):
    tl = btl[i]
    queensPerLine = -1;
    for j in range (len(tl)):
      current = tl[j]
      if (board[current[0]][current[1]] == 'X'):
        queensPerLine = queensPerLine + 1
    if (queensPerLine > 0):
      tb = tb + queensPerLine
  return h + v + tw + tb

fitness(board)

# Gerar a população inicial

import random

initialPopulation = 60

population = []

for p in range(initialPopulation):

  person = [
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '']
  ]

  queens = 0
  while (queens < 8):
    i = random.randint(0, 7)
    j = random.randint(0, 7)
    if (person[i][j] != 'X'):
      person[i][j] = 'X'
      queens = queens + 1

  population.append(person)

print(len(population))
for board in population:
  print(fitness(board))
  printBoard(board)

# Selecionar um percentual de indivíduos mais adaptados

t = 0.5

population.sort(key=fitness)
#print(fitness(population[0]))
#printBoard(population[0])
#print(fitness(population[1]))
#printBoard(population[1])
#print(fitness(population[2]))
#printBoard(population[2])
#print(fitness(population[3]))
#printBoard(population[3])
#print(fitness(population[4]))
#printBoard(population[4])

print(len(population))
b = int(len(population)/2)
selectedPeople = population[:b]
len(selectedPeople)