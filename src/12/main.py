def is_inside(r,c):
  return len(grid) > r >= 0 and len(grid[0]) > c >= 0

def measure_region(i,j,plant_type):
  directions = {"left": (0,-1),"right":(0,1),"down":(1,0),"up":(-1,0)}
  stack = [(i,j)]
  visited.add((i,j))
  perimeter, sides, area = 0,0,0
  while stack:
    r,c = stack.pop()
    area += 1
    different_neighbors = []
    for dir, (dr,dc) in directions.items(): 
      nr, nc = r+dr, c+dc
      if not is_inside(nr,nc) or grid[nr][nc] != plant_type:
        perimeter += 1
        different_neighbors.append(dir)
      if is_inside(nr,nc) and grid[nr][nc] == plant_type and (nr,nc) not in visited:
        stack.append((nr,nc))
        visited.add((nr,nc))
    for dir in different_neighbors:
      chk_dir = "left" if dir in ["up", "down"] else "up"
      cdr, cdc = directions[chk_dir]
      dr,dc = directions[dir]
      if is_inside(r+cdr,c+cdc) and grid[r+cdr][c+cdc] == grid[r][c]: 
        if not is_inside(r+cdr+dr,c+cdc+dc) or grid[r+cdr+dr][c+cdc+dc] != grid[r][c]:
          continue
      sides += 1
  return area, perimeter, sides

def solve():
  cost_part1, cost_part2 = 0, 0
  for r, row in enumerate(grid):
    for c, plant_type in enumerate(row):
      if (r,c) in visited: continue
      area, perimeter,sides = measure_region(r,c,plant_type)
      cost_part1 += area * perimeter
      cost_part2 += area * sides
  print(f"Part 1: {cost_part1}")
  print(f"Part 2: {cost_part2}")

with open("input.txt", "r") as f:
  grid = [list(row) for row in f.read().splitlines()]
  visited = set()
  solve()