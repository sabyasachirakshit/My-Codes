def plant_trees(w, l, g):
    if w == l:
        if w > 3:
            tot_space = (w**2)-4
        else:
            tot_space = 8
        used_space = (w+l)-2

        return tot_space-used_space


print(plant_trees(3, 3, 1))
print(plant_trees(3, 3, 3))
print(plant_trees(3, 3, 2))
