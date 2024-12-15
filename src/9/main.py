def get_available_spaces():
  available_spaces, file_locations, curr_index, file_id = [], [], 0, 0
  for i, segment_size in enumerate(disk_map):
    if i % 2 == 0:
      file_locations.append((file_id, curr_index, segment_size))
      file_id += 1
    else: 
      available_spaces.append((curr_index,segment_size))
    curr_index += disk_map[i]
  return available_spaces, file_locations


def get_checksum(file_id, start_index, block_count):
  return file_id * ((start_index - 1)*block_count + (block_count * (block_count+1))//2)


def solve_part2():
  available_spaces, file_locations = get_available_spaces()
  new_file_locations = []
  for file_id, file_start_index, file_size in file_locations[::-1]:
    moved = False
    for i, (space_index, space_size) in enumerate(available_spaces):
      if space_index > file_start_index: break
      if space_size >= file_size:
        moved, moved_to = True, i
        new_file_locations.append((file_id,space_index,file_size))
        break
    if moved:
      if space_size > file_size:
        space_index, space_size = available_spaces[moved_to]
        available_spaces[moved_to] = (space_index + file_size, space_size - file_size)
      else: 
        del available_spaces[moved_to]
    else:
      new_file_locations.append((file_id, file_start_index, file_size))

  ans = 0
  for file_id, file_start_index, file_size in new_file_locations:
    ans += get_checksum(file_id, file_start_index, file_size)
  print(f"Part 2: {ans}")
    

def solve_part1():
  ans,space_index = 0, 1 #spaces start at index 1
  next_file_to_move = len(disk_map) - 2 if len(disk_map)  % 2 == 0 else len(disk_map)  - 1
  blocks_remaining_from_current_file = disk_map[next_file_to_move]
  spaces_available = disk_map[space_index]
  curr_index,curr_seg, curr_seg_size = 0, 0, disk_map[0]
  while space_index < next_file_to_move:
    if curr_seg % 2 == 0: 
      file_id = curr_seg // 2
      blocks_processed = curr_seg_size
      ans += get_checksum(file_id, curr_index, blocks_processed)
      curr_index += blocks_processed
      curr_seg += 1
      curr_seg_size = disk_map[curr_seg]
    elif blocks_remaining_from_current_file > 0:
      file_id = next_file_to_move // 2
      if blocks_remaining_from_current_file <= spaces_available:
        spaces_available -= blocks_remaining_from_current_file
        blocks_processed = blocks_remaining_from_current_file
        next_file_to_move -= 2
        blocks_remaining_from_current_file = disk_map[next_file_to_move]
      else: 
        blocks_processed = spaces_available
        blocks_remaining_from_current_file -= spaces_available
        spaces_available = 0 
      ans += get_checksum(file_id, curr_index, blocks_processed)
      curr_index += blocks_processed
      if spaces_available == 0: 
        curr_seg += 1
        curr_seg_size = disk_map[curr_seg]
        space_index += 2
        spaces_available = disk_map[space_index]
        
  if disk_map[next_file_to_move] > blocks_remaining_from_current_file > 0 : 
    blocks_processed = blocks_remaining_from_current_file
    ans += get_checksum(file_id, curr_index, blocks_processed)
  print(f"Part 1: {ans}" )  


with open('input.txt', 'r') as f:
  disk_map = [int(i) for i in list(f.read())]
  solve_part1()
  solve_part2()