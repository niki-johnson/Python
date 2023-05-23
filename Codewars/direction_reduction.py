"""
Write a function dirReduc which will take an array of strings 
and returns an array of strings with the needless directions removed 
(W<->E or S<->N side by side).
"""


def remover_dir(coordenadas):

    flag_coord = []
    for i in range(len(coordenadas) - 1):
        if coordenadas[i] + coordenadas[i+1] == 0:
            flag_coord.append(i)
            flag_coord.append(i+1)
            break

    new_coord = []
    for i in range(len(coordenadas)):
        if i in flag_coord:
            continue
        else:
            new_coord.append(coordenadas[i])

    if len(coordenadas) == len(new_coord):
        return new_coord

    elif len(new_coord) == 1:
        return new_coord

    else:
        return remover_dir(new_coord)


def dirReduc(arr):

    coord = list(map(lambda x: x.lower(), arr))
    coord_num = list(map(lambda x: 1 if x == 'north' else -
                     1 if x == 'south' else 2 if x == 'east' else -2, coord))

    new_coord = remover_dir(coord_num)

    coord_final = list(map(lambda x: 'north' if x == 1 else
                           'south' if x == -1 else 'east' if x == 2 else 'west', new_coord))

    return coord_final


def dirReduc2(arr):
    opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST',
                'SOUTH': 'NORTH', 'WEST': 'EAST'}
    new_plan = []
    for d in arr:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan


def dirReduc3(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH", '').replace(
        "SOUTH NORTH", '').replace("EAST WEST", '').replace("WEST EAST", '')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3


if __name__ == '__main__':
    print(dirReduc2(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST",
          "NORTH", "NORTH", "NORTH", "WEST", "WEST", "WEST"]))
