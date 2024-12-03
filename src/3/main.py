import re
pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'

def get_result(input):
  ans = 0
  matches = re.findall(pattern, input)
  for match in matches: 
    nums = match.replace("mul(","").replace(")","").split(",")
    ans += int(nums[0]) * int(nums[1])
  return ans

def solve_part1():
  print(f"Part 1: {get_result(content)}")

def solve_part2():
  ans = 0
  parts = content.split("do()")
  for part in parts:
    active_part = part.split("don't()")[0]
    ans += get_result(active_part)
  print(f"Part 2: {ans}")


with open("input.txt", "r") as f:
  content = f.read()

solve_part1()
solve_part2()