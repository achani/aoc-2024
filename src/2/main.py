def is_safe_with_dampner(r):
  if is_safe(r):
    return True
  for i in range(len(r)):
    if is_safe(r[0:i] + r[i+1:]):
      return True
  return False


def is_safe(r):
  changes = [r[i+1] - r[i] for i in range(len(r)-1)]
  count_unsafe_changes = len(list(filter(lambda i: abs(i) > 3 or abs(i)<1, changes)))
  count_no_changes = len(list(filter(lambda i: i == 0, changes))) 
  count_positive_changes = len(list(filter(lambda i: i > 0, changes)))
  return  count_unsafe_changes == 0 and count_no_changes == 0 and (count_positive_changes == len(changes) or count_positive_changes == 0)


def solve_part1():
  safe_count = len(list(filter(lambda r: is_safe(r),reports)))
  print(f"Part 1: {safe_count}")


with open("input.txt", "r") as f:
  lines = f.read().splitlines()
  reports = [[int(i) for i in line.split()] for line in lines]
  print(f"Part 1: {len(list(filter(lambda r: is_safe(r),reports)))}")
  print(f"Part 2: {len(list(filter(lambda r: is_safe_with_dampner(r),reports)))}")