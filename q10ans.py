if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    minValue = min([x[1] for x in students])
    filters = [x for x in students if x[1] != minValue]
    newMinValue = min(x[1] for x in filters)
    newFi = [x[0] for x in filters if x[1] == newMinValue]
    newFi.sort()
    print(*newFi, sep='\n')