"""
from:
A,B,C
1,2,1
3,0,0
1,2,0


to:
A: 1,3,1
B: 2,0,2
C: 1,0,0

"""


def transp_cand_in_columns(cand_in_columns):
    lines = cand_in_columns.strip().split("\n")
    header = lines[0].split(",")
    rows = [line.split(",") for line in lines[1:]]

    transposed_data = {}
    for i, column in enumerate(header):
        transposed_data[column] = [row[i] for row in rows]

    return transposed_data


data_from = """\
A,B,C
1,2,1
3,0,0
1,2,0
"""

transposed_data = transp_cand_in_columns(data_from)

for key, values in transposed_data.items():
    print(f"{key}: {','.join(values)}")
