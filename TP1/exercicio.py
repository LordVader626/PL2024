dataset = open('emd.csv', 'r')
next(dataset)
output = open("output.txt", "w")

modalidades = []
escaloes = [0] * 20
totalAtletas = 0
totalFederados = 0


def calc_array_pos(idade):
    return idade // 5


for line in dataset:
    totalAtletas += 1
    parsed_data = line.split(',')
    if parsed_data[11] == "true":
        totalFederados += 1
    pos = calc_array_pos(int(parsed_data[5]))
    if parsed_data[8] not in modalidades:
        modalidades.append(parsed_data[8])
    escaloes[pos] += 1

def percentagens():
    aptos = (totalFederados/totalAtletas) * 100
    inaptos = 100 - aptos
    return aptos, inaptos

def geraOutput():
    percents = percentagens()
    output.write(f'Atletas Aptos = {percents[0]:.2f}%\n')
    output.write(f'Atletas Inaptos = {percents[1]:.2f}%\n\n')

    output.write("Escalões: \n")
    escalao_idade = 0
    for escalao in escaloes:
        if escalao != 0:
            output.write(f'{escalao_idade}-{escalao_idade + 4} = {(escalao / totalAtletas) * 100:.2f}%\n')
        escalao_idade += 5
    output.write("\n")

    output.write("Modalidades: \n")
    modalidades.sort()
    for categoria in modalidades:
        output.write(f'{categoria}\n')


geraOutput()