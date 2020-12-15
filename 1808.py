nc = input()

media = 0
fatores = 0
indicador = False
seq = '1'

nc = ''.join(reversed(nc))

for idx, x in enumerate(nc):

    if x == '0':
        seq = seq + '0'
        indicador = True
        continue
    elif x == '1' and indicador == True:
        media = media + float(seq)
        fatores = fatores + 1
        seq = '1'
        indicador = False
        continue

    media = media + float(x)
    fatores = fatores + 1

media = media / fatores
mediaFloat = "{:.2f}".format(media)
print (mediaFloat)
