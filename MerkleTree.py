# No final quero retornar cada hash: Ha, Hb,... Hab, Hcd,... Habcdefgh
# Ha, Hb,... Hz estão contidas na variável "leaves[]"
# As restantes hashes estão contidas na  variável "parents[]"

def hashcode(*args):
    if len(args) == 1:
        return args[0] % 1000_000_007
    elif len(args) == 2:
        mod = 1000_000_007
        return ((args[0] % mod) + (args[1] % mod)) % mod
    else:
        return


class MerkleNode:

    # Cada node (e par de nodes) vai ter um pai (a partir de nível N) e dois filhos (a partir de nível N - 1)
    def __init__(self, hashed_node):
        self.hash = hashed_node
        self.parent = None
        self.left = None
        self.right = None


class MerkleTree:

    def __init__(self, transacoes):  # Cria a primeira linha de hashes a partir das transações (inputs)
        self.hashed_nodes = []

        leaves = []  # Ha, Hb, Hc,....

        for transacao in transacoes:
            node = hashcode(transacao)  # Aplica a função hash a cada input
            leaves.append(MerkleNode(node))

        self.create_merkle_tree(leaves)

    def create_merkle_tree(self, leaves):  # Função recursiva que retorna no final a raíz

        if len(leaves) == 1:  # Condição se houver apenas 1 input
            self.hashed_nodes.append(leaves[0].hash)
            return

        parents = []

        for i in range(0, len(leaves), 2):
            left_child = leaves[i]
            right_child = leaves[i + 1]
            self.hashed_nodes.append(left_child.hash)
            self.hashed_nodes.append(right_child.hash)
            parents.append(self.create_parent(left_child, right_child))

        return self.create_merkle_tree(parents)

    def create_parent(self, left, right):
        parent = MerkleNode(hashcode(left.hash, right.hash))
        parent.left = left
        parent.right = right
        left.parent = parent
        right.parent = parent
        # print(f"Left child: {parent.left.hash} <--- Parent: {parent.hash} ---> Right Child: {parent.right.hash}")
        return parent
