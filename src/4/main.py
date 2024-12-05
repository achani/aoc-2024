
def match(row,col,dir,offset,ch):
  match dir: 
    case 'n': 
      return False if offset > row else grid[row-offset][col] == ch
    case 'ne':
      return False if (offset > row or offset >= cols-col) else grid[row-offset][col+offset] == ch
    case 'e':
      return False if (offset >= cols - col) else grid[row][col+offset] == ch
    case 'se': 
      return False if (offset >= rows - row or offset >= cols - col) else grid[row+offset][col+offset] == ch
    case 's': 
      return False if (offset >= rows - row) else grid[row + offset][col] == ch
    case 'sw':
      return False if (offset >= rows - row or offset > col) else grid[row+offset][col-offset] == ch
    case 'w':
      return False if (offset > col) else grid[row][col-offset] == ch
    case 'nw':
      return False if (offset > row or offset > col) else grid[row-offset][col-offset] == ch  


def solve_part1():
  xmas_count = 0
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == 'X':
        for dir in ['n','ne','e', 'se','s','sw','w','nw']:
          if match(r,c,dir,1,'M') and match(r,c,dir, 2,'A') and match(r,c,dir, 3,'S'):
            xmas_count += 1
  print(f"Part 1: {xmas_count}")

def solve_part2():
  xmas_count = 0
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == 'A':
        if ((match(r,c,'nw',1,'M') and match(r,c,'se',1,'S')) or (match(r,c,'nw',1,'S') and match(r,c,'se',1,'M'))) \
        and ((match(r,c,'ne',1,'M') and match(r,c,'sw',1,'S')) or (match(r,c,'ne',1,'S') and match(r,c,'sw',1,'M'))):
          xmas_count += 1
  print(f"Part 2: {xmas_count}")


with open("input.txt", 'r') as f:
  lines = f.read().splitlines()
  grid  = [list(row) for row in lines]
  rows,cols = len(grid), len(grid[0])

solve_part1()
solve_part2()

