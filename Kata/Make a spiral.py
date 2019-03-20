"""
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
"""

bigmap = {'0':[], '1': [[1]],
          '2': [[1, 1], [0, 1]],
          '3': [[1, 1, 1], [0, 0, 1], [1, 1, 1]],
          '4': [ [1, 1, 1, 1], [0, 0, 0, 1],
               [1, 0, 0, 1], [1, 1, 1, 1]
               ],
          '5': [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1],
                [1, 1, 1, 0, 1], [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]],
          '8': [[1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]
          }


def spiralize(size=5):
    if str(size) in bigmap:
        return bigmap[str(size)]
    else:
        maps = [[0] * size for _ in range(size)]
        for row in range(size):
            for col in range(size):
                if row == 0:
                    maps[row][col] = 1
                elif row == size-1:
                    maps[row][col] = 1
                elif col == size - 1:
                    maps[row][col] = 1
                elif col == 0 and row > 1:
                    maps[row][col] = 1
        maps[2][1] = 1
        small_map = spiralize(size-4)
        for row in range(2, size-2):
            for col in range(2, size-2):
                maps[row][col] = small_map[row-2][col-2]

        bigmap[str(size)] = maps
        return maps

if __name__ == "__main__":
    print(spiralize(5),spiralize(5)==[[1,1,1,1,1],
                                    [0,0,0,0,1],
                                    [1,1,1,0,1],
                                    [1,0,0,0,1],
                                    [1,1,1,1,1]])
    print(spiralize(8),spiralize(8)==[[1,1,1,1,1,1,1,1],
                                    [0,0,0,0,0,0,0,1],
                                    [1,1,1,1,1,1,0,1],
                                    [1,0,0,0,0,1,0,1],
                                    [1,0,1,0,0,1,0,1],
                                    [1,0,1,1,1,1,0,1],
                                    [1,0,0,0,0,0,0,1],
                                    [1,1,1,1,1,1,1,1]])
    print(spiralize(2),spiralize(2)==[[1,1],
                                    [0,1]])
    print(spiralize(1),spiralize(1)==[[1]])
    print(spiralize(3),spiralize(3)==[[1,1,1],
                                    [0,0,1],
                                    [1,1,1]])
    print(spiralize(100))