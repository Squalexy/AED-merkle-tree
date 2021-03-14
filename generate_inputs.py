import random


def generate(num, n_transacoes):
    ficheiro = "input"
    with open(ficheiro + str(num) + ".in", 'w') as escrever:
        escrever.write(str(n_transacoes) + "\n")
        for j in range(n_transacoes):
            BBBB = str(random.randint(0, 10_000))
            dd = str(random.randint(1, 32)).zfill(2)
            mm = str(random.randint(0, 13)).zfill(2)
            aaaa = str(random.randint(2007, 2099)).zfill(4)
            escrever.write(BBBB + dd + mm + aaaa + " ")


# n = 1
# for i in range(20):
#    generate(n, pow(2, i))
#    n += 1

n = 21
for i in range(20, 31, 1):
    generate(n, pow(2, i))
    n += 1
