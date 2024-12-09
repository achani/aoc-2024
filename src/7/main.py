
def eval(nums, mask, with_concat=False):
  if len(nums) == 1:
    return nums[0]
  val = nums[0]
  for i in range(len(mask)):
    if with_concat:
      match mask[i]:
        case "0":
          val = val + nums[i+1]
        case "1":
          val = val * nums[i+1]
        case "2":
          val = int(str(val)+ str(nums[i+1]))
    else:
      val = val + nums[i+1] if mask[i] == "0" else val * nums[i+1]
  return val

def is_valid(puzzle, with_concat = False):
  ans,nums = puzzle[0], puzzle[1]
  if len(nums) == 1:
    return ans == nums[0]
  no_operators = len(nums)-1
  base = 3 if with_concat else 2
  for mask in mask_generator(base, no_operators):
    #print(mask)
    if len(mask) > no_operators:
      break
    val = eval(nums,mask,with_concat)
    if val == ans: 
      return True
  return False

def mask_generator(b,min_l):
  counter = 0
  while True:
    n = counter
    digits = []
    while n:
      digits.append(str(n%b))
      n //= b
    val = "".join(digits[::-1])
    counter += 1
    yield val if len(digits) >= min_l else "0"*(min_l-len(digits))+val

def solve_part1():
  valid_puzzles = list(filter(lambda p: is_valid(p),puzzles))
  print(f"Part 1: {sum([p[0] for p in valid_puzzles])}")

def solve_part2():
  valid_puzzles = list(filter(lambda p: is_valid(p,with_concat=True),puzzles))
  print(f"Part 2: {sum([p[0] for p in valid_puzzles])}")

with open('input.txt', 'r') as f: 
  lines = f.read().splitlines()
  puzzles = [(int(p[0]), [int(x) for x in p[1].strip().split(" ")]) for p in list(map(lambda x: x.split(":"),lines))]
  solve_part1()
  solve_part2()