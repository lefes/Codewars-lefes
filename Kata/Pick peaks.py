"""
In this kata, you will write a func that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak in position 3 with a value of 5 (arr[3] equals 5).

The output will be returned as a struct (PosPeaks) with two properties: Pos and Peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {Pos: [], Peaks: []}.

Example: PickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) returns {Pos: [3, 7], Peaks: [6, 3]}

All input arrays will be valid numeric arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus! [1, 2 , 2 , 2 , 1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: PickPeaks([1, 2, 2, 2, 1]) returns {Pos: [1], Peaks: [2]}

Have fun!
"""

def pick_peaks(arr):
    pos = []
    peaks = []
    for num in range(1, len(arr)-1):
        if arr[num] > arr[num-1] and arr[num] == arr[num+1]:
            for i in range(num+1, len(arr)):
                if arr[num] < arr[i]:
                    break
                elif arr[num] > arr[i]:
                    pos.append(num)
                    peaks.append(arr[num])
                    break
                elif arr[num] == arr[i]:
                    pass
        elif arr[num] > arr[num-1] and arr[num] > arr[num+1]:
            pos.append(num)
            peaks.append(arr[num])
    return {"pos":pos, "peaks":peaks}


if __name__ == '__main__':
    print('should support finding peaks')
    print(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {"pos": [3, 7], "peaks": [6, 3]})

    print('should support finding peaks, but should ignore peaks on the edge of the array')
    print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), {"pos": [3, 7], "peaks": [6, 3]})

    print(
        'should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau')
    print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]), {"pos": [3, 7, 10], "peaks": [6, 3, 2]})

    print(
        'should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau')
    print(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), {"pos": [2, 4], "peaks": [3, 2]})

    print('should support finding peaks, but should ignore peaks on the edge of the array')
    print(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]), {"pos": [2], "peaks": [3]})

    print('Test from random tester')
    print(pick_peaks([2, 15, 18, 15, -2, 11, -5, 8, 2, 20, 8, 13, 20, 20, -3, 4, -2, 0, 20, 0, 17, 20, 6, 1, 1, 15, 18, 10, -3, 14]))