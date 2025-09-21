# Problem 1: Transpose Matrix
def transpose(matrix):
  '''
  input: 2D integer array 
  output: 2D integer array 

  row -> column
  column -> row

  (0,0) (0,1) (0,2)          (0,0) (1,0) (2,0)
  (1,0) (1,1) (1,2)  --->    (0,1) (1,1) (2,1)
  (2,0) (2,1) (2,2)          (0,2) (1,2) (2,2)

  '''
  rows, cols = len(matrix), len(matrix[0])
  res = [[0] * rows for _ in range(cols)]

  for r in range(rows):
    for c in range(cols):
      res[c][r] = matrix[r][c]
  return res

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))

# Problem 2: Two-Pointer Reverse List
def reverse_list(lst):
  """
  input: a list
  output: reverse list
  """
  l, r = 0, len(lst) - 1
  while l < r:
    lst[l], lst[r] = lst[r], lst[l]
    l += 1
    r -= 1
  return lst

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))

# Problem 3: Remove Duplicates
def remove_dupes(items):
  """
  input: sorted array
  output: integer -> length of the modified array
  """
  l = 0

  for r in range(1, len(items)):
    if items[r] != items[r - 1]:
      l += 1
      items[l], items[r] = items[r], items[l]
  return l + 1

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))