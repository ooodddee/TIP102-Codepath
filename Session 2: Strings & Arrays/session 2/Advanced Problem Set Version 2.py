# Problem 1: Matrix Addition
def add_matrices(matrix1, matrix2):
  if not matrix1 and not matrix2:
    return []
  if not matrix1:
    return matrix2
  if not matrix2:
    return matrix1

  rows, cols = len(matrix1), len(matrix1[0])
  res = [[0] * cols for _ in range(rows)]

  for r in range(rows):
    for c in range(cols):
      res[r][c] = matrix1[r][c] + matrix2[r][c]
  return res
  
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(add_matrices(matrix1, matrix2))

# Problem 2: Two-Pointer Palindrome
def is_palindrome(s):
  if not s:
    return True

  l, r = 0, len(s) - 1
  while l < r:
    if s[l] != s[r]:
      return False
    l += 1
    r -= 1
  return True

s = "madam"
print(is_palindrome(s))

s = "madamweb"
print(is_palindrome(s))

# Problem 3: Squash Spaces
# def squash_spaces(s):

# Problem 4: Two-Pointer Two Sum
def two_sum(nums, target):
  hm = {}
  for i, n in enumerate(nums):
    if target - n in hm:
      return [hm[target - n], i]
    hm[n] = i 

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))

# Problem 5: Three Sum
def three_sum(nums):
  if not nums:
    return []
  
  nums.sort()
  res = []
  n = len(nums)
  for i in range(n - 2):
    x = nums[i]
    if i > 0 and nums[i] == nums[i - 1]:
      continue
    if x > 0:
      break 
    l, r = i + 1, n - 1
    while l < r:
      s = x + nums[l] + nums[r]
      if s < 0:
        l += 1
      elif s > 0:
        r -= 1
      else:
        res.append([x, nums[l], nums[r]])
        l += 1
        while l < r and nums[l] == nums[l - 1]:
          l += 1
        r -= 1
        while l < r and nums[r] == nums[r + 1]:
          r -= 1
  return res

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))

# Problem 6: Insert Interval