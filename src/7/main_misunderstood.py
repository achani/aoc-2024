
def eval(nums, mask):
  if len(nums) == 1:
    return nums[0]
  val = nums[0]
  for i in range(len(mask)):
    val = val + nums[i+1] if mask[i] == "0" else val * nums[i+1]
  return val

def is_valid(puzzle):
  ans,nums = puzzle[0], puzzle[1]
  for val in val_generator(nums):
    if val == ans: 
      return True
  return False

def val_generator(nums):
  if len(nums) == 1:
    yield nums[0]
    return
  no_operators = len(nums)-1
  counter = "0"*no_operators
  while counter != "1" + "0"*no_operators:
    yield eval(nums,counter)
    counter = ("{0:0"+str(no_operators)+ "b}").format(int(counter,2)+1)

def is_valid_with_concat(puzzle):
  if is_valid(puzzle):
    return True
  ans,nums = puzzle[0], puzzle[1]
  no_operators = len(nums)-1
  for i in range(no_operators):
    left, right = nums[0:i+1], nums[i+1:]
    for left_val in val_generator(left):
      for right_val in val_generator(right):
        if ans == int(str(left_val)+str(right_val)):
          return True
  return False

def solve_part1():
  valid_puzzles = list(filter(lambda p: is_valid(p),puzzles))
  print(f"Part 1: {sum([p[0] for p in valid_puzzles])}")

def solve_part2():
  valid_puzzles = list(filter(lambda p: is_valid_with_concat(p),puzzles))
  print(f"Part 2: {sum([p[0] for p in valid_puzzles])}")

with open('/Users/ajay/dev/projects/aoc-2024/src/7/test.txt', 'r') as f: 
  lines = f.read().splitlines()
  puzzles = [(int(p[0]), [int(x) for x in p[1].strip().split(" ")]) for p in list(map(lambda x: x.split(":"),lines))]
  solve_part1()
  solve_part2()
