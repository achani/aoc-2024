
def parse_machine(m):
  parts = m.split('\n')
  A = tuple([int(x.strip()[2:]) for x in parts[0].split(":")[1].strip().split(",")])
  B = tuple([int(x.strip()[2:]) for x in parts[1].split(":")[1].strip().split(",")])
  prize = tuple([int(x.strip()[2:]) for x in parts[2].split(":")[1].strip().split(",")])
  return (A,B,prize)


def solve_part1():
  total_tokens = 0
  for (Ax,Ay),(Bx,By),(Px,Py) in machines:
    has_solution = False
    min_tokens = float('inf')
    for A_count in range(1,101):
      for B_count in range(1,101):
        if Ax * A_count + Bx * B_count == Px and Ay * A_count + By * B_count == Py: 
          tokens = COSTA * A_count + COSTB * B_count
          min_tokens = min(tokens,min_tokens)
          has_solution = True
    if has_solution:
      total_tokens += min_tokens
  print(f"Part 1: {total_tokens}")


def solve_part2():
  total_tokens = 0 
  for (Ax,Ay),(Bx,By),(Px,Py) in machines:
    Px = Px + 10000000000000
    Py = Py + 10000000000000
    B_count = (Py*Ax - Ay*Px) / (Ax * By - Ay * Bx)
    A_count = (Px - Bx * B_count) / Ax
    if float(A_count).is_integer() and float(B_count).is_integer():
      total_tokens += COSTA * A_count + COSTB * B_count
  print(f"Part 2: {int(total_tokens)}")


with open("input.txt", "r") as f: 
  machines = f.read().split("\n\n")
  machines = [parse_machine(m) for m in machines]
  COSTA, COSTB = 3,1
  solve_part1()
  solve_part2()