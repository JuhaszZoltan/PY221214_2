szo:str = input('írj be egy szót: ')

ek:str = 'áéíóöőúüűÁÉÍÓÖŐÚÜŰ'
en:str = 'aeiooouuuAEIOOOUUU'
ekmsz:str = ''

for betu in szo:
    if betu not in ek:
        ekmsz += betu
    else:
        i:int = ek.index(betu)
        ekmsz += en[i]
print(ekmsz)