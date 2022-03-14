films, N= dict(),int(input())
for i in range(N):
    filmVote = input()
    if filmVote in films:   
        films[filmVote]+=1
    else:
        films[filmVote] = 1

for i in (sorted(films,key = lambda x: films[x])[::-1]):
    print(i+" "+str(films[i]))
