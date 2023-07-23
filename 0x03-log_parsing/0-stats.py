#!/usr/bin/env python3
"""
stats file
"""
#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''


import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


# from typing import List, Union, Any
# import sys
# import re


# i = 1
# my_status_hash = {
#     200: 0,
#     301: 0,
#     400: 0,
#     401: 0,
#     403: 0,
#     404: 0,
#     405: 0,
#     500: 0
# }
# file_size = 0
# pattern = (
#     r'''^(\d+\.\d+\.\d+\.\d+) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] "(\S+ \S+ \S+)" (\d{3}) (\d+)$'''
# )


# def matchLine(arg: str) -> List[Any]:
#     """_summary_

#     Args:
#         arg (str): _description_

#     Returns:
#         List[Any]: _description_
#     """
#     if re.match(pattern, arg):
#         arg_list = arg.split()

#         return [arg_list[-2], int(arg_list[-1])]
#     return []


# try:
#     for line in sys.stdin:
#         if 'Exit' == line.rstrip():
#             break
#         arg_list = matchLine(line)

#         if len(arg_list) == 2:
#             file_size += arg_list[1]
#             my_status_hash[int(arg_list[0])] += 1

#         if i % 10 == 0:
#             print(f"File size: {file_size}")
#             for k, v in my_status_hash.items():
#                 if v:
#                     print(f"{k}: {v}")
#         i += 1
# except Exception as err:
#     pass
# finally:
#     print(f"File size: {file_size}")
#     for k, v in sorted(my_status_hash.items()):
#         if v:
#             print(f"{k}: {v}")
