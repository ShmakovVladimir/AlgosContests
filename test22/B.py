def prefHash(text: str) -> list:
    hashes,base,module = [ord(text[0])]+[0]*(len(text)),91,10**12
    for i in range(1,len(text)):
        hashes[i] = hashes[i-1]*base+ord(text[i])
        hashes[i]%=module
    return hashes
template,text = input(),input()
prefixes,h = prefHash(text),prefHash(template)[-1]
answer = []
for i in range(len(text)-len(template)):
    if (prefixes[i+len(template)]-prefixes[i]*(91**len(template))) == h:
        answer.append(i)
if answer == []:
    print(-1)
    exit()
print(" ".join(map(str, answer)))


