def cell_status(cf, x, y):
    cnt = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if cf[j][i]:
                cnt += 1
    if cf[y][x]:
        cnt -= 1
        if cnt == 2 or cnt == 3:
            return 1
        return 0
    if cnt == 3:
        return 1
    return 0