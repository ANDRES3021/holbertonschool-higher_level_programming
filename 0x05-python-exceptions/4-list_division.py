#!/usr/bin/python3
from unittest import result


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
            continue
        except(ZeroDivisionError):
            print('division by 0')
        except(IndexError):
            print('out of range')
        except(TypeError):
            print('wrong type')
        finally:
            pass
    return result
