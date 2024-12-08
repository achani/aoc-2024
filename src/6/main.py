
def scan_grid():
  obstructions = []
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == "#":
        obstructions.append((i,j)) 
      if grid[i][j] in ['^','<', '>','v']:
        guard_pos = ((i,j), look_directions[grid[i][j]])
  return guard_pos, obstructions

def walk_till_obstruction(curr_pos,curr_dir,update_covered_blocks=True):
  dir = -1 if curr_dir in ['N', 'W'] else 1 #we move in the increasing or decreasing order of row or col number
  fix_dim = 1 if curr_dir in ['N', 'S'] else 0 #depending on the direction, one axis is fixed and the other is variable.
  variable_dim = 1-fix_dim

  def is_in_the_way(o):
    if o[fix_dim] != curr_pos[fix_dim]:
      return False
    return o[variable_dim] > curr_pos[variable_dim] if dir > 0 else o[variable_dim] < curr_pos[variable_dim]
  
  obstructions  = list(filter(is_in_the_way, all_obstructions))
  if len(obstructions) == 0:
    next_pos, next_dir = None, None
    first_obstacle = -1 if curr_dir in ['N', 'W'] else len(grid) if curr_dir == "S" else len(grid[0])
  else:
    first_obstacle = dir * min([o[variable_dim]*dir for o in obstructions])
    new_pos_var_dim = first_obstacle - 1 * dir
    next_pos = (new_pos_var_dim, curr_pos[fix_dim]) if variable_dim == 0 else (curr_pos[fix_dim], new_pos_var_dim)
    next_dir = next_dir_lookup[curr_dir]
  if update_covered_blocks:
    for i in range(curr_pos[variable_dim], first_obstacle - 1 * dir, 1 * dir):
      covered_block = (i + 1 * dir, curr_pos[fix_dim]) if variable_dim == 0 else (curr_pos[fix_dim], i + 1 * dir)
      if covered_block not in covered_blocks:
        covered_blocks[covered_block] = 0
  return next_pos, next_dir


def solve_part2():
  possibilities = 0
  for block,_ in covered_blocks.items():
    seen_situations = {}
    curr_pos, curr_dir = guard_pos
    seen_situations[(curr_pos, curr_dir)] = 0
    all_obstructions.append(block)
    while True:
      next_pos, next_dir = walk_till_obstruction(curr_pos, curr_dir, False)
      if (next_pos,next_dir) in seen_situations:
        possibilities += 1
        break
      else:
        seen_situations[(next_pos,next_dir)] = 0
      if next_pos is None: 
        break
      curr_pos, curr_dir = next_pos, next_dir
    all_obstructions.remove(block)
  print(f"Part 2: {possibilities}")


def solve_part1():
  curr_pos, curr_dir = guard_pos
  covered_blocks[curr_pos] = 0
  while True:
    next_pos, next_dir = walk_till_obstruction(curr_pos, curr_dir)
    if next_pos is None: 
      break
    curr_pos, curr_dir = next_pos, next_dir
  print(f"Part 1: {len(covered_blocks.keys())}")


look_directions = {'^': 'N', '<':'W', '>':'E', 'v': 'S'}
next_dir_lookup = {'N':'E','E':'S','S':'W','W':'N'}
covered_blocks = dict()
with open("input.txt", 'r') as f:
  lines = f.read().splitlines()
  grid  = [list(row) for row in lines]
  guard_pos, all_obstructions = scan_grid()
  
solve_part1()
solve_part2()