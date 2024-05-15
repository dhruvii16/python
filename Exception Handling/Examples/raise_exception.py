num = [3,4,5,6]
if len(num) > 3:
    raise Exception(f'length of given list must be less than 3 or equal to but is {len(num)}')