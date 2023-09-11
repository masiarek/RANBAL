# from "candidates in rows" to columns
def transp_cand_in_rows(rows):
    rows = rows.strip().split("\n")
    headers = [row.split(":")[0] for row in rows]
    rows = [list(map(int, row.split(":")[1].split(","))) for row in rows]
    columns = list(map(list, zip(*rows)))
    columns.insert(0, headers)
    data_columns = "\n".join([",".join(map(str, col)) for col in columns])

    return data_columns


data_source = """\
Cab: 1,3,1
B: 3,0,0
C: 1,2,0
"""

transposed_data = transp_cand_in_rows(data_source)
print(transposed_data)
