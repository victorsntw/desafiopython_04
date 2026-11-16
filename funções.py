def calcular_media(notas): # funções para calcular média
    soma = sum(notas) # soma as notas da lista notas com o sum
    media = soma/len(notas) #calcula a média pegando a soma e dividindo pela quantidade de notas na lista
    return media # retorna a média para salva e mostrar no print depois

def verificar_situacao(media): # outra função só que para média - aqui ele apenas retorna para depois motrar no relatório
    if media >= 7:
        return "Aprovado" # aprovado caso for igual ou maior que 7
    elif media >= 5:
        return "Recuperação" # recuperação se ficar entre 5 e 6.9
    else:
        return "Reprovado" # reprovado caso seja menor que 5
    
def exibir_relatorio(nome, media, situacao):
    print("=== RELATÓRIO ===")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("=================")

while True:
    nome = input("Digite aqui o nome do Aluno(Ou para encerrar 'Sair'):").strip()

    if nome.lower() == "sair":
        print("Saindo do sistema... até mais...")
        break

    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite aqui a nota {i} do aluno: ").strip())
                notas.append(nota)
                break
            except ValueError:
                print("Erro! digite apenas números para as notas!")

    # 🎯 AQUI VOCÊ CHAMA AS FUNÇÕES:
    media = calcular_media(notas)              # recebe a média
    situacao = verificar_situacao(media)       # recebe a situação
    exibir_relatorio(nome, media, situacao)    # imprime o relatório