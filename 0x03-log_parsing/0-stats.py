#!/usr/bin/env python3
"""
_summary_
"""
from typing import List, Union, Any
import sys
import re


i = 1
my_status_hash = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
file_size = 0
pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] "(\S+ \S+ \S+)" (\d{3}) (\d+)$'


def matchLine(arg: str) -> List[Any]:
    if re.match(pattern, arg):
        arg_list = arg.split()

        return [arg_list[-2], int(arg_list[-1])]
    return []


for line in sys.stdin:
    if "Exit" == line.rstrip():
        break
    # print(matchLine(line))
    # print(line)

    arg_list = matchLine(line)

    if len(arg_list) == 2:
        file_size += arg_list[1]
        my_status_hash[int(arg_list[0])] += 1

    if i % 10 == 0:
        print(f"File size: {file_size}")
        for k, v in my_status_hash.items():
            if v:
                print(f"{k}: {v}")

    i += 1
