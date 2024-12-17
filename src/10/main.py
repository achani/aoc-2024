
from collections import deque
from copy import deepcopy

def find_all_zeros():
  zeros = []
  for i, row in enumerate(grid):
    for j, c in enumerate(row):
      if c == 0: 
        zeros.append((i,j))
  return zeros


def find_all_next_positions(height,row,col):
  next_positions = []
  offsets = [(0,1), (0,-1), (1,0),(-1,0)]
  for dr, dc in offsets:
      nr, nc = row+dr, col+dc
      if not len(grid) > nr >= 0 or not len(grid[0]) > nc >= 0: continue
      if grid[nr][nc] == height+1:
        next_positions.append((nr,nc))
  return next_positions


def get_trail_score_and_rating(trail_head):
  trails = set()
  trail_ends = set()
  trail_paths = deque()
  trail_paths.append((0,trail_head,(trail_head,)))
  while len(trail_paths) > 0:
    height, (row,col), trail = trail_paths.pop()
    trail = list(trail)
    next_positions = find_all_next_positions(height,row,col)
    new_height = height + 1
    for pos in next_positions:
      new_trail = deepcopy(trail)
      new_trail.append(pos)
      trails.add(tuple(new_trail))
      if new_height == 9:
        trail_ends.add(pos)
      else:
        trail_paths.append((new_height, pos, tuple(new_trail)))
  valid_trails = list(filter(lambda t: len(t)==10, trails))
  return len(trail_ends), len(valid_trails)


with open("input.txt", 'r') as f:
  lines = f.read().splitlines()
  grid  = [[int(i) for i in list(row)] for row in lines]
  zeros = find_all_zeros()
  scores_and_ratings = list(map(lambda z: get_trail_score_and_rating(z),zeros))
  print(f"Part 1: {sum([r[0] for r in scores_and_ratings])}")
  print(f"Part 2: {sum([r[1] for r in scores_and_ratings])}")
