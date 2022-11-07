numero_do_candidato_1 = 1
numero_do_candidato_2 = 2
votos_do_candidato_1 = 0
votos_do_candidato_2 = 0
cpf = 0
voto = 0
listacpf = []
listavoto = []
zeresima = 0
if votos_do_candidato_1 == 0 and votos_do_candidato_2 == 0 and cpf == 0 and voto == 0:
    print('validaçao zerésima')
else:
    zeresima += 1

if zeresima == 0:
    quantidade = int(input('numero de participantes: '))
    for i in range(quantidade):
        cpf = int(input('digite o cpf: '))
        voto = int(input('digite o voto: '))
        if voto == numero_do_candidato_1:
            votos_do_candidato_1 = votos_do_candidato_1 + 1
        else:
            voto == numero_do_candidato_2
            votos_do_candidato_2 = votos_do_candidato_2 + 1
        listacpf.append(cpf)
        listavoto.append(voto)
    print(f' cpf: {listacpf}\n votos: {listavoto}\n numero de votos candidadto 1: {votos_do_candidato_1}\n numero de votos candidadto 2: {votos_do_candidato_2}')
else:
    print('variaveis nao nulas')
