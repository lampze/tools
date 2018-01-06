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
        lines = file.readlines()
        if not lines:
            break
        for i in range(len(lines)):
            if lines[i][0:1] == '第':
                count_num = count_num + 1
                if is_number(lines[i][2:3]):
                    strs = "<num>" + str(int(lines[i][1:3]) + begin_num) + "<main>"
                else:
                    strs = "<num>" + str(int(lines[i][1:2]) + begin_num) + "<main>"
                strs = strs + lines[i+1][0:-1] + "<A>" + lines[i+2][2:-1]
                if lines[i+3][0:1] == 'B':
                    strs = strs + "<B>" + lines[i+3][2:-1]
                    count = 3
                if lines[i+4][0:1] == 'C':
                    strs = strs + "<C>" + lines[i+4][2:-1]
                    count = 4
                if lines[i+5][0:1] == 'D':
                    strs = strs + "<D>" + lines[i+5][2:-1]
                    count = 5
                strs = strs + "<end>" + lines[i+count+3][3:4] + "</end>"
                print(strs)
            else:
                pass
        return count_num
            
for i in sys.argv[1:]:
    try:
        first_num += main(i, first_num)
    except:
        print("没有这个文件！！！")

