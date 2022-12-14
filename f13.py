szo:str = input('írj be egy szót: ')
maganhangzok:str = 'aáeéiíoóöőuúüű'

c:int = 0
for betu in szo:
    if betu in maganhangzok:
        c += 1
print(f'magánhangzók száma a szóban: {c}')