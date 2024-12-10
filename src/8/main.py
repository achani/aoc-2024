def scan_grid():
  antenna_locations = dict()
  for i, row in enumerate(grid):
    for j, c in enumerate(row):
      if c == ".":
        continue
      antenna_locations.setdefault(c,[]).append((i,j))
  return antenna_locations


def find_hotspots(c, find_all=False): 
  hotspots = set()
  locations = antenna_locations[c]
  if len(locations) <= 1:
    return hotspots 
  all_pairs = [(a, b) for idx, a in enumerate(locations) for b in locations[idx + 1:]]
  for (a,b) in all_pairs: 
    keep_going, n = True, 1
    while keep_going:
      keep_going = False
      hotspot1, hotspot2 = ((n+1)*a[0]-n*b[0], (n+1)*a[1]-n*b[1]), ((n+1)*b[0]-n*a[0], (n+1)*b[1]-n*a[1])
      if 0 <= hotspot1[0] < len(grid) and 0 <= hotspot1[1] < len(grid[0]): 
        hotspots.add(hotspot1)
        keep_going = find_all
      if 0 <= hotspot2[0] < len(grid) and 0 <= hotspot2[1] < len(grid[0]):
        hotspots.add(hotspot2) 
        keep_going = find_all
      n += 1
    if find_all:
      hotspots.update([a,b])
  return hotspots


def solve_part1():
  hotspots = set()
  for c in antenna_locations.keys():
    hotspots.update(find_hotspots(c))
  print(f"Part 1: {len(hotspots)}")


def solve_part2():
  hotspots = set()
  for c in antenna_locations.keys():
    hotspots.update(find_hotspots(c,find_all=True))
  print(f"Part 2: {len(hotspots)}")


with open("input.txt", 'r') as f:
  lines = f.read().splitlines()
  grid  = [list(row) for row in lines]

antenna_locations = scan_grid()

solve_part1()
solve_part2()