def ladder(K: list,M: int):
    maximumPos = K.index(max(K))
    a = K[:maximumPos+1]
    a.append(K[maximumPos]+1)
    a+=K[maximumPos::-1]
    if M == 0:
        print(sum(K))
        return
    ladder(a,M-1)
ladder([int(input())],int(input())-1)
    
