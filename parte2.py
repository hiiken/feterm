
###FUNÇÕES

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


###FIM DAS FUNÇÕES



###CÓDIGO ESTRUTURAL


dados = []
pmArray = {}
vArray = {}


arrayPressao = [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]
arrayVolumes = [42.0, 40.0, 38.0, 35.0, 33.0, 32.0, 30.0, 28.0, 27.0]
arrayTeste = []
arrayFinal = []

for n in arrayVolumes:
    nx = 100 / n
    arrayFinal.append(nx)
    nf = truncate(nx, 4)
    arrayTeste.append(nf)
print("  Volume em 4 casas sem arredondar:\n\n ", arrayTeste)

####erro 10²/v²

arrayFinalErro = []
arrayFinalErroCompleto = []


erroVolume = 0.5
for i in arrayVolumes:
    ix = (100 / (i ** 2)) * erroVolume
    arrayFinalErroCompleto.append(ix)
    ix = truncate(ix, 4)
    arrayFinalErro.append(ix)
print("\n\n\033[1;31m Erro em 4 casas sem arredondar:\033[0;0m \n\n ", arrayFinalErro)
print("\n\n")







###PARTE 3 QUICA CUADRADO

erroQQ = 0
for ita in range(0, len(arrayPressao)):
    erroQQ += 1/(0.02**2)

##print(erroQQ)



###x

somax = 0

for itb in range(0, len(arrayPressao)):
    somax += arrayFinal[itb]/(0.02**2)
xFinal = somax*(1/erroQQ)
##print(xFinal)


###x²
somax2 = 0
for itc in range(0, len(arrayPressao)):
    somax2 += (arrayFinal[itc]**2)/(0.02**2)

x2Final = somax2*(1/erroQQ)
##print(x2Final)

###y
somay = 0
for itd in range(0, len(arrayPressao)):
    somay += arrayPressao[itd]/(0.02**2)
yFinal = somay*(1/erroQQ)
##print(yFinal)
##xy

somaxy = 0
for ite in range(0, len(arrayPressao)):
    somaxy += (arrayPressao[ite]*arrayFinal[ite])/(0.02**2)
xyFinal = somaxy*(1/erroQQ)
##print(xyFinal)

a = ((xFinal)*(yFinal) - (xyFinal))/((xFinal**2) - x2Final)
b = yFinal - (a * xFinal)

print("A = {}".format(a))
print("\nB = {}".format(b))
