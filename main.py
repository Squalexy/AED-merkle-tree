from MerkleTree import MerkleTree
import math
from time import perf_counter


def print_tree(hashed_nodes):
    # print(hashed_nodes)
    hashed_nodes_reverse = hashed_nodes[::-1]
    # print(hashed_nodes_reverse)

    count = 1
    count_last = 0
    # print(int(math.log2(len(hashed_nodes_reverse) + 1)))
    for i in range(int(math.log2(len(hashed_nodes_reverse) + 1))):
        hashed_sliced = hashed_nodes_reverse[count_last:count]
        for elemento in hashed_sliced[::-1]:
            print(elemento)
        count_last = count
        count += 2 ** (i + 1)


def main():
    num_transacoes = int(input())
    transacoes = [int(i) for i in input().split()]
    # print(transacoes)

    tik = perf_counter()
    hashed_nodes = MerkleTree(transacoes).hashed_nodes
    tok = perf_counter()
    tempo_execucao = tok - tik
    print(tempo_execucao)

    # print_tree(hashed_nodes)


if __name__ == "__main__":
    main()
