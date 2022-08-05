# version 1: normal iteration
def chop1(target_number: int, array_num: [int]) -> int:
    for idx in range(len(array_num)):
        if target_number == array_num[idx]:
            return idx
    return -1


# version 2: normal recursive
def chop2(target_number: int, array_num: [int]) -> int:
    array_len = len(array_num)
    if array_len == 0:
        return -1
    if array_num[0] == target_number:
        return 0
    else:
        idx = chop2(target_number, array_num[1:])
        return -1 if idx == -1 else idx + 1


# version 3: binary search
def chop3(target_number: int, array_num: [int]) -> int:
    start = 0
    end = len(array_num)
    if end == 0:
        return -1
    while start < end:
        split_idx = start + (end - start) // 2
        if target_number == array_num[split_idx]:
            return split_idx
        elif target_number < array_num[split_idx]:
            end = split_idx
        else:
            start = split_idx + 1
    return -1


# version 4: binary search in recursive shape
def chop4(target_number: int, array_num: [int]) -> int:
    array_len = len(array_num)
    if array_len == 0:
        return -1
    if array_num[0] == target_number:
        return 0
    else:
        split_idx = array_len // 2
        if target_number == array_num[split_idx]:
            return split_idx
        elif target_number < array_num[split_idx]:
            idx = chop4(target_number, array_num[0: split_idx])
            return -1 if idx == -1 else idx
        else:
            idx = chop4(target_number, array_num[split_idx + 1:])
            return -1 if idx == -1 else idx + split_idx + 1


# version 5: interpolation search
def chop(target_number: int, array_num: [int]) -> int:
    start = 0
    end = len(array_num) - 1
    if end < 0:
        return -1
    while (array_num[end] != array_num[start]) and (target_number >= array_num[start]) and (
            target_number <= array_num[end]):
        mid = start + ((target_number - array_num[start]) * (end - start) // (array_num[end] - array_num[start]))

        if array_num[mid] < target_number:
            start = mid + 1
        elif target_number < array_num[mid]:
            end = mid - 1
        else:
            return mid

    if target_number == array_num[start]:
        return start
    return -1
