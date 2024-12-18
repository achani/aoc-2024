
def blink(stone):
  new_arrangement = []
  if stone == 0: new_arrangement.append(1)
  elif (len(str(stone)) % 2 == 0):
    stone_str= str(stone)
    length = len(stone_str)
    new_arrangement.append(int(stone_str[0:length//2]))
    new_arrangement.append(int(stone_str[length//2:]))
  else:
    new_arrangement.append(stone*2024)
  return new_arrangement


def get_count_after_n_blinks(stone, n):
  if (stone,n) in cache: return cache[(stone,n)]
  new_arrangement = blink(stone)
  count = 0
  if n == 1: 
    count += len(new_arrangement)
  else:
    for stn in new_arrangement:
      count+= get_count_after_n_blinks(stn,n-1)
  cache[(stone,n)] = count
  return count


if __name__ == "__main__":
  cache = {}
  with open('input.txt','r') as f:
    stones = [int(i) for i in f.read().split(" ")]
    ans_part1 = 0
    ans_part2 = 0

    for stone in stones:
      ans_part1 += get_count_after_n_blinks(stone, 25)
      ans_part2 += get_count_after_n_blinks(stone, 75)
    print(f"Part 1: {ans_part1}")
    print(f"Part 2: {ans_part2}")