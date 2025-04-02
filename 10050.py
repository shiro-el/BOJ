def sol(n, pt):
    if n < 8:
        if n == 3:
            print('{} to {} \n{} to {} \n{} to {}'.format(pt + 2, pt - 1, pt + 5, pt + 2, pt + 3, pt - 3))

        elif n == 4:
            print('{} to {} \n{} to {} \n{} to {} \n{} to {}'.format(pt + 6, pt - 1, pt + 3, pt + 6, pt, pt + 3, pt + 7, pt))
        
        elif n == 5:
            print('{} to {} \n{} to {} \n{} to {} \n{} to {} \n{} to {}'.format(pt + 8, pt - 1, pt + 3, pt + 8, pt + 6, pt + 3, pt, pt + 6, pt + 9, pt))
        
        elif n == 6:
            print('{} to {} \n{} to {} \n{} to {} \n{} to {} \n{} to {} \n{} to {}'.format(pt + 10, pt - 1, pt + 7, pt + 10, pt + 2, pt + 7, pt + 6, pt + 2, pt, pt + 6, pt + 11, pt))
        
        elif n == 7:
            print('{} to {} \n{} to {} \n{} to {} \n{} to {} \n{} to {} \n{} to {} \n{} to {}'.format(pt + 12, pt - 1, pt + 5, pt + 12, pt + 8, pt + 5, pt + 3, pt + 8, pt + 9, pt + 3, pt, pt + 9, pt + 13, pt))
    else:
        print('{} to {} \n{} to {}'.format(pt + 2*n-2, pt - 1, pt + 3, pt + 2*n - 2))
        sol(n - 4, pt + 4)
        print('{} to {} \n{} to {}'.format(pt, pt + 2*n - 5, pt + 2*n - 1, pt))

sol(int(input()), 0)