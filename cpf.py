n = int(input())
senhas = []
for x in range(n):
    senha = ""
    nome, cpf = input().split()
    for i, x in enumerate(nome):
        let = ord(x)
        let = let+int(cpf[i])
        if(let > ord('z')):
            # let -= ord('z')
            let -= 26
        c = chr(let)
        senha += c
    senha += cpf[-2]+ cpf[-1]
    senhas.append([nome, senha])

senhas.sort()
for nome, senha in senhas:
    print(nome, senha)


