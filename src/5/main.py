def intersect(list1, list2):
  return [value for value in list1 if value in list2]


def is_page_order_valid(page_order):
  for i in range(len(page_order)):
    if i > 0 and page_order[i] in rules_dict and len(intersect(page_order[0:i], rules_dict[page_order[i]])) > 0:
      return False
  return True


def solve_part1():
  ans = 0
  invalid_page_orders = []
  for page_order in page_orders:
    if is_page_order_valid(page_order):
      ans += page_order[len(page_order)//2]
    else:
      invalid_page_orders.append(page_order)

  print(f"Part 1: {ans}")
  return invalid_page_orders


def reorder_invlalid_page_order(page_order):
  for i in range(len(page_order)):
      if i > 0 and page_order[i] in rules_dict:
        intersaction = intersect(page_order[0:i], rules_dict[page_order[i]])
        if len(intersaction) > 0: 
          j = min(list(map(lambda x: page_order.index(x,0,i), intersaction)))
          page_order[j]=page_order[i]
          page_order[i]=intersaction[0]
          return page_order


def solve_part2(invalid_page_orders):
  ans = 0 
  for page_order in invalid_page_orders:
    while not is_page_order_valid(page_order):
      reorder_invlalid_page_order(page_order)
    ans += page_order[len(page_order)//2]
  print(f"Part 2: {ans}")


with open('input.txt', 'r') as f:
  rules, page_orders = f.read().split("\n\n")
  rules = rules.split('\n')
  page_orders = [[int(page) for page in page_order.split(',')] for page_order in page_orders.split('\n')]

rules_dict = {}
for rule in rules:
  before,after = rule.split("|") 
  before,after = int(before), int(after)

  if before in rules_dict:
    rules_dict[before].append(after)
  else:
    rules_dict[before] = [after]

invalid_page_orders = solve_part1()
solve_part2(invalid_page_orders)