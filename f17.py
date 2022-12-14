egyik:list[chr] = list(input('egyik szó: '))
masik:list[chr] = list(input('másik szó: '))

egyik.sort()
masik.sort()

if egyik == masik: print('anagramma')
else: print('nem anagramma')