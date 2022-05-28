X = list()
i = 0
while i<10:
    X.append(int(input()))
    if X[i]<1:
        X[i]=1
        print(f'X[{i}] = {X[i]}')
    else:
        print(f'X[{i}] = {X[i]}')
    i+=1