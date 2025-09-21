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
  if not items:
    return 0
  
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

# Problem 4: Sort Array by Parity
def sort_by_parity(nums):
  """
  input:  integer array
  output: even + odd

  even: not n % 2
  odd: n % 2
  """
  if not nums or len(nums) == 1:
    return nums
  
  l, r = 0, len(nums) - 1
  while l < r:
    if not nums[l] % 2:
      l += 1
    elif nums[r] % 2:
      r += 1
    else:
      nums[l], nums[r] = nums[r], nums[l]
      l += 1
      r -= 1
  return nums

nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))

# Problem 5: Container with Most Honey
def most_honey(heights):
  """
  input: an integer array
  output: integer -> max area

  area -> height(min(left, right)) * length
  move lower height pointer
  """
  if not heights:
    return 0
  
  l, r = 0, len(heights) - 1
  res = float('-inf')

  while l <= r:
    area = min(heights[l], heights[r]) * (r - l)
    res = max(res, area)
    if heights[l] < heights[r]:
      l += 1
    else:
      r -= 1
  return res

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))

height = [1, 1]
print(most_honey(height))

# Problem 6: Merge Intervals
def merge_intervals(intervals):
  """
  input: 2d array
  output: non-overlapping 2d array

  sort by start
  end >= start: overlapping
  overlapping [start, end], start -> min(start), end -> max(end)
  """
  intervals.sort(key = lambda x: x[0])
  res = []
  res.append(intervals[0])

  for start, end in intervals[1:]:
    last = res[-1]
    if last[1] >= start:
      last[1] = max(end, last[1])
    else:
      res.append([start, end])
  return res

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))