def arithmetic_arranger(problems, answers = False):
    top = []
    second = []
    operator = []
    width = []
    total = []
    jessica = []

    if len(problems) > 5:
        return "Error: Too many problems."
        quit()
    else:
        for i in problems:
            x = i.split()
            int1 = x[0]
            sign = x[1]
            int2 = x[2]
            top.append(int1)
            operator.append(sign)
            second.append(int2)

            if sign not in ['+', '-']:
                return "Error: Operator must be '+' or '-'."
                quit()
            elif len(int1) > 4 or len(int2) > 4:
                return "Error: Numbers cannot be more than four digits."
                quit()
            elif not int1.isnumeric() or not int2.isnumeric():
                return "Error: Numbers must only contain digits."
                quit()

        t = 0
        while t < len(problems):
            width.append(max(len(top[t]), len(second[t])))
            t = t + 1

        q = 0
        while q < len(problems):
            if operator[q] == "+":
                total.append(int(top[q]) + int(second[q]))
            else:
                total.append((int(top[q]) - int(second[q])))
            q = q + 1

        y = 0
        for s in top:
            if s != top[-1] or y != len(top) - 1:
                jessica.append(top[y].rjust(width[y] + 2) + "    ")
            else:
                jessica.append((top[y].rjust(width[y] + 2)) + "\n")
            y = y + 1


        z = 0
        for d in second:
            if d != second[-1] or z != len(second) - 1:
                jessica.append(operator[z] + " " + second[z].rjust(width[z]) + "    ")
            else:
                jessica.append(operator[z] + " " + second[z].rjust(width[z]) + "\n")
            z = z + 1

        p = 0
        while p < len(total):
            if p != len(total) - 1:
                jessica.append("-" * (width[p] + 2) + "    ")
            elif answers is True:
                jessica.append("-" * (width[p] + 2) + "\n")
            else:
                jessica.append("-" * (width[p] + 2))
            p = p + 1


        if answers is True:
            r = 0
            for w in total:
                if w != total[-1]:
                    jessica.append(str(total[r]).rjust(width[r] + 2) + "    ")
                else:
                    jessica.append(str(total[r]).rjust(width[r] + 2))
                r = r + 1

        m = 0
        while m < len(jessica):
            jessica[m]
            m = m + 1

        final = "".join(jessica)
        
        return final
        
        return arithmetic_arranger





