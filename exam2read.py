import sys

first_num = 0

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def main(f, begin_num):
    file = open(f)

    while 1:
        count = 0
        count_num = 0
        continue_num = 0
        lines = file.readlines()
        if not lines:
            break
        for i in range(len(lines)):
            if lines[i][0:1] == '第':
                count_num = count_num + 1
                if is_number(lines[i][2:3]):
                    strs = str(int(lines[i][1:3]) + begin_num) + "."
                else:
                    strs = str(int(lines[i][1:2]) + begin_num) + "."
                for j in lines[i+1]:
                    if j == '(':
                        break
                    strs += j
                    continue_num += 1
                strs += "**"
                if lines[i+3][0:1] == 'B':
                    count = 3
                if lines[i+4][0:1] == 'C':
                    count = 4
                if lines[i+5][0:1] == 'D':
                    count = 5
                if lines[i+2][0:1] != 'A':
                    count += 1
                def find_true(x):
                    return {
                        'A':2,
                        'B':3,
                        'C':4,
                        'D':5,
                    }.get(x)
                strs += lines[i+find_true(lines[i+count+3][3:4])][2:-1]
                strs += "**" + lines[i+1][continue_num + 2:-1] + "\n"
                print(strs)
                continue_num = 0
            else:
                pass
        return count_num

for i in sys.argv[1:]:
    try:
        main(i, first_num)
    except Exception as e:
        print(e)
