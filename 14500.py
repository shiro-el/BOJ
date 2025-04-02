import sys
n, m = map(int, input().split())
L = []
for i in range(n):
    L.append(list(map(int, sys.stdin.readline().split())))
maxTetro = 0

####
for i in range(n):
    for j in range(m-3):
        sumTetro = L[i][j] + L[i][j+1] + L[i][j+2] + L[i][j+3]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "####")
#
#
#
#
for i in range(n-3):
    for j in range(m):
        sumTetro = L[i][j] + L[i+1][j] + L[i+2][j] + L[i+3][j]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "#.#.#.#")
##
##
for i in range(n-1):
    for j in range(m-1):
        sumTetro = L[i][j] + L[i][j+1] + L[i+1][j] + L[i+1][j+1]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "##.##")
###
 #
for i in range(n-1):
    for j in range(m-2):
        sumTetro = L[i][j] + L[i][j+1] + L[i][j+2] + L[i+1][j+1]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "###./#")
#
##
#
for i in range(n-2):
    for j in range(m-1):
        sumTetro = L[i][j] + L[i+1][j] + L[i+1][j+1] + L[i+2][j]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "#.##.#")
 #
###
for i in range(n-1):
    for j in range(m-2):
        sumTetro = L[i][j+1] + L[i+1][j] + L[i+1][j+1] + L[i+1][j+2]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "/#.###")
 #
##
 #
for i in range(n-2):
    for j in range(m-1):
        sumTetro = L[i][j+1] + L[i+1][j] + L[i+1][j+1] + L[i+2][j+1]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "/#.##./#")
#
#
##
for i in range(n-2):
    for j in range(m-1):
        sumTetro = L[i][j] + L[i+1][j] + L[i+2][j] + L[i+2][j+1]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "#.#.##")
###
#
for i in range(n-1):
    for j in range(m-2):
        sumTetro = L[i][j] + L[i][j+1] + L[i][j+2] + L[i+1][j]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "###.#")
##
 #
 #
for i in range(n-2):
    for j in range(m-1):
        sumTetro = L[i][j] + L[i][j+1] + L[i+1][j+1] + L[i+2][j+1]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "##./#./#")
  #
###
for i in range(n-1):
    for j in range(m-2):
        sumTetro = L[i][j+2] + L[i+1][j] + L[i+1][j+1] + L[i+1][j+2]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "//#.###")
 #
 #
##
for i in range(n-2):
    for j in range(m-1):
        sumTetro = L[i][j+1] + L[i+1][j+1] + L[i+2][j] + L[i+2][j+1]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "/#./#.##")
###
  #
for i in range(n-1):
    for j in range(m-2):
        sumTetro = L[i][j] + L[i][j+1] + L[i][j+2] + L[i+1][j+2]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "###.//#")
##
#
#
for i in range(n-2):
    for j in range(m-1):
        sumTetro = L[i][j] + L[i][j+1] + L[i+1][j] + L[i+2][j]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "##.#.#")
#
###
for i in range(n-1):
    for j in range(m-2):
        sumTetro = L[i][j] + L[i+1][j] + L[i+1][j+1] + L[i+1][j+2]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "#.###")
#
##
 #
for i in range(n-2):
    for j in range(m-1):
        sumTetro = L[i][j] + L[i+1][j] + L[i+1][j+1] + L[i+2][j+1]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "#.##./#")
 ##
##
for i in range(n-1):
    for j in range(m-2):
        sumTetro = L[i][j+1] + L[i][j+2] + L[i+1][j] + L[i+1][j+1]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "/##.##")
 #
##
#
for i in range(n-2):
    for j in range(m-1):
        sumTetro = L[i][j+1] + L[i+1][j] + L[i+1][j+1] + L[i+2][j]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "/#.##.#")
##
 ##
for i in range(n-1):
    for j in range(m-2):
        sumTetro = L[i][j] + L[i][j+1] + L[i+1][j+1] + L[i+1][j+2]
        if sumTetro > maxTetro:
            maxTetro = sumTetro
#print(maxTetro, "##./##")
print(maxTetro)