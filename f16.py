# karakterek:list[chr] = ['g', 'h', 'j', 'r', 'q', 'a', 's', 'x', 'a', 'i']
# karakterek.sort()
# print(karakterek)

karakterek:list[chr] = list(input('írj be egy szót: '))
karakterek.sort()

rendezett:str = ''.join(karakterek)
print(f'szó karakterei rendezve: {rendezett}')