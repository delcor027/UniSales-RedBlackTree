class Node:
    """
    Classe para representar um nó em uma árvore rubro-negra.

    Atributos:
        data (int): O valor armazenado no nó.
        color (str): A cor do nó, 'red' ou 'black'.
        parent (Node): Referência ao nó pai.
        left (Node): Referência ao nó filho à esquerda.
        right (Node): Referência ao nó filho à direita.
    """
    def __init__(self, data, color="red"):
        """
        Inicializa um novo nó.

        Parâmetros:
            data (int): O valor a ser armazenado no nó.
            color (str, opcional): A cor do nó. Padrão para 'red'.
        """
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

