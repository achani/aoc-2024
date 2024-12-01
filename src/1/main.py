
import math
from collections import defaultdict


def solve_part1():
    list1.sort()
    list2.sort()
    sum = 0
    for i in range(len(list1)):
        sum += abs(list1[i] - list2[i])
    print(f"Part 1: {sum}")
      

def solve_part2():
  list2_counts = defaultdict(int)
  ans = 0
  for i in list2: 
      list2_counts[i] += 1
  for i in list1: 
      ans += i * list2_counts[i]
  print(f"Part 2: {ans}")


list1 = []
list2 = []
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    list1 = list(map(lambda i: int(i.split()[0]), lines))
    list2 = list(map(lambda i: int(i.split()[1]), lines))
    solve_part1()
    solve_part2()
