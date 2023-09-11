s = """\
1,5,4,2,3
5,1,4,3,2
5,2,1,4,3
5,4,2,1,3
5,2,4,3,1
5,4,2,3,1
"""

s = s.strip()  # Remove leading/trailing whitespace

a = []

for line in s.split("\n"):
    elements = line.split(",")
    for element in elements:
        if element == "1":
            element = "5"
        elif element == "2":
            element = "4"
        elif element == "3":
            element = "3"
        elif element == "4":
            element = "2"
        elif element == "5":
            element = "1"
        a.append(element)

modified_lines = []

for i in range(0, len(a), len(elements)):
    modified_lines.append(a[i : i + len(elements)])

for line in modified_lines:
    print(",".join(line))


def abcxyz():
    pass


abcxyz = 3
