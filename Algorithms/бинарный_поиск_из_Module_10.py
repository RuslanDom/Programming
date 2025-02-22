from typing import Union, List
import copy
Number = Union[int, float, complex]

ARRAY = [1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6]

def find_insert_position(array: List[Number], number: Number) -> int:
    # РЕКУРСИЕЙ
    if len(array) <= 1:
        if number <= array[0]:
            return ARRAY.index(array[0])
        elif number > array[0]:
            return ARRAY.index(array[0]) + 1

    return find_insert_position(array[:len(array)//2], number) if number < array[:len(array)//2][-1] else find_insert_position(array[len(array)//2:], number)

    # ПЕРЕБОРОМ ЦИКЛОМ for

    # if len(array) != 0:
    #     for i_number in range(len(array)):
    #         if i_number == len(array) - 1:
    #             if array[i_number] >= number:
    #                 return i_number
    #             else:
    #                 return i_number + 1
    #         elif array[i_number] < number <= array[i_number + 1]:
    #             return i_number + 1
    #         elif array[i_number] >= number:
    #             return i_number
    # else:
    #     return 0

    # if len(array) != 0:
    #     for index in range(len(array)):
    #         if number < array[index]:
    #             return index
    #         elif index < len(array) - 1:
    #             continue
    #         else:
    #             return index + 1
    # else:
    #     return 0

    # a1 = copy.copy(array)
    # a2 = copy.copy(array)


    # Только ветвлением

    # while True:
    #     a1 = a1[:len(a1) // 2]
    #     a2 = a2[len(a2) // 2:]
    #     if len(a1) < 2 and len(a2) < 1:
    #         if number < a1[0]:
    #             return array.index(a1[0]) - 1
    #         else:
    #             return array.index(a1[0]) + 1
    #     elif len(a2) < 2 and len(a1) < 1:
    #         if number < a2[0]:
    #             return array.index(a2[0])
    #         else:
    #             return array.index(a2[0]) + 1
    #
    #     elif number < a1[-1]:
    #         if number < a1[0] and array[0] >= number:
    #             return  0
    #         elif number < a1[0] and array[0] <= number:
    #             return array.index(a1[0])
    #         elif number >= a1[-1]:
    #             return array.index(a1[-1]) + 1
    #         else:
    #             a2 = a1
    #     else:
    #         a1 = a2



if __name__ == '__main__':
    A: List[Number] = [1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6]
    # A: List[Number] = []
    x: Number = 3.5
    insert_position: int = find_insert_position(A, x)
    print(insert_position)
    # assert insert_position == 5


    A.insert(insert_position, x)
    print(A)
    # assert A == sorted(A)
