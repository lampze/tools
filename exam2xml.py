import sys

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

def main(f):
    file = open(f)

    while 1:
        count = 0
        lines = file.readlines()
        if not lines:
            break
        for i in range(len(lines)):
            if lines[i][0:1] == '第':
                if is_number(lines[i][2:3]):
                    str = "<num>" + lines[i][1:3] + "<main>"
                else:
                    str = "<num>" + lines[i][1:2] + "<main>"
                str = str + lines[i+1][0:-1] + "<A>" + lines[i+2][2:-1]
                if lines[i+3][0:1] == 'B':
                    str = str + "<B>" + lines[i+3][2:-1]
                    count = 3
                if lines[i+4][0:1] == 'C':
                    str = str + "<C>" + lines[i+4][2:-1]
                    count = 4
                if lines[i+5][0:1] == 'D':
                    str = str + "<D>" + lines[i+5][2:-1]
                    count = 5
                str = str + "<end>" + lines[i+count+3][3:4] + "</end>"
                print(str)
            else:
                pass

for i in sys.argv[1:len(sys.argv)]:
    try:
        main(i)
    except:
        print("没有这个文件！！！")

