def printMaxActivities(s, f):
    n = len(f)
    print('The following are selected')
    
    i = 0
    print(i, end=' ')

    for j in range(1, n):
        if s[j] >= f[i]:
            print(j, end= ' ')
            i = j

if __name__ == '__main__':

    s = [1, 3, 2, 0, 5, 8, 11]
    f = [3, 4, 5, 7, 9, 10, 12]

    printMaxActivities(s, f)