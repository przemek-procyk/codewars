def land_perimeter(arr):
    island_size = 0
    for peri in range(len(arr)):
        for land in range(len(arr[peri])):
            if arr[peri][land] == "X":
                island_size += 4
                if land > 0 and arr[peri][land - 1] == "X":
                    island_size -= 1
                if land < (len(arr[peri]) - 1) and arr[peri][land + 1] == "X":
                    island_size -= 1
                if peri > 0 and arr[peri - 1][land] == "X":
                    island_size -= 1
                if peri < (len(arr) - 1) and arr[peri + 1][land] == "X":
                    island_size -= 1
    return f'Total land perimeter: {island_size}'


b= ['XOOXO',
  'XOOXO',
  'OOOXO',
  'XXOXO',
  'OXOOO']
print(land_perimeter(b))