def conversaoDados(Pm, V):
    a = 9.80665 / 100
    ie = 0.02
    immq = 0.05
    iv = 0.5
    ip = ((ie ** 2) + (immq ** 2) ** (1 / 2))

    Po = 0.58
    Pt = Pm + Po
    PV = Pt * V
    ipv = PV * (((ip) ** 2) / (Pt) ** 2 + ((iv) ** 2) / (V) ** 2) ** (1 / 2)

    dados.append({"PV": PV * a, "IPV": ipv * a})



def truncate(f, n):
    '''Truncar número sem arredondamento'''

    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d + '0' * n)[:n]])


dados = []
pmArray = {}
vArray = {}

arrayVolumes = [42.0, 40.0, 38.0, 35.0, 33.0, 32.0, 30.0, 28.0, 27.0]
arrayFinal = []

for n in arrayVolumes:
    nx = 100 / n
    nf = truncate(nx, 4)
    arrayFinal.append(nf)
print("  Volume em 4 casas sem arredondar:\n\n ", arrayFinal)

####erro 10²/v²

arrayFinalErro = []
erroVolume = 0.5
for i in arrayVolumes:
    ix = (100 / (i ** 2)) * erroVolume
    ix = truncate(ix, 4)
    arrayFinalErro.append(ix)
print("\n\n\033[1;31m Erro em 4 casas sem arredondar:\033[0;0m \n\n ", arrayFinalErro)
print("\n\n")
print(dados)
