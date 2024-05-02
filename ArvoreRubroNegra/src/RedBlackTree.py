from Node import Node

class RedBlackTree:
    """
    Classe que implementa uma árvore rubro-negra.

    Atributos:
        TNULL (Node): Um nó nulo que representa o fim de um ramo.
        root (Node): A raiz da árvore rubro-negra.
    """
    def __init__(self):
        """
        Inicializa a árvore rubro-negra criando um nó TNULL que é utilizado
        como os filhos nulos de todos os nós folha e a raiz inicial.
        """
        self.TNULL = Node(data=0, color="black")
        self.root = self.TNULL

    def get_root(self):
        """
        Retorna o nó raiz da árvore rubro-negra.

        Retorno:
            Node: O nó raiz da árvore.
        """
        return self.root

    def __rotate_left(self, x):
        """
        Realiza uma rotação para a esquerda no nó fornecido.

        Parâmetros:
            x (Node): O nó sobre o qual a rotação será realizada.
        """
        y = x.right
        if y == self.TNULL:
            return
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def __rotate_right(self, x):
        """
        Realiza uma rotação para a direita no nó fornecido.

        Parâmetros:
            x (Node): O nó sobre o qual a rotação será realizada.
        """
        y = x.left
        if y == self.TNULL:
            return
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __fix_insert(self, k):
        """
        Corrige a árvore rubro-negra após a inserção de um novo nó.

        Parâmetros:
            k (Node): O nó que foi inserido e pode ter causado violações nas propriedades da árvore rubro-negra.
        """
        while k != self.root and k.parent.color == 'red':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.__rotate_right(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.__rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.__rotate_right(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.__rotate_left(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def insert(self, key):
        """
        Insere um novo nó com o dado valor na árvore rubro-negra.

        Parâmetros:
            key (int): O valor a ser inserido na árvore.
        """
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'red'

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 'black'
            return

        if node.parent.parent is None:
            return

        self.__fix_insert(node)

    def print_tree(self, node, indent, last):
        """
        Imprime a árvore rubro-negra de maneira formatada para visualização.

        Parâmetros:
            node (Node): O nó atual a ser impresso.
            indent (str): A indentação atual para este nó.
            last (bool): Se este nó é o último filho de seu pai.
        """
        if node != self.TNULL:
            print(indent, end='')
            if last:
                print("R----", end='')
                indent += "     "
            else:
                print("L----", end='')
                indent += "|    "

            s_color = "RED" if node.color == 'red' else "BLACK"
            print(f'({node.data}, {s_color})')
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

    def remove(self, data):
        """
        Remove o nó com o valor dado da árvore rubro-negra.

        Parâmetros:
            data (int): O valor do nó a ser removido.
        """
        self.delete_node_helper(self.root, data)

    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Não foi possível encontrar a chave na árvore")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'black':
            self.fix_delete(x)

    def rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def fix_delete(self, x):
        """
        Corrige a árvore rubro-negra após a remoção de um nó para manter todas as propriedades necessárias.

        Parâmetros:
            x (Node): O nó que pode necessitar de ajustes para garantir as propriedades da árvore.
        """
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.__rotate_left(x.parent)
                    s = x.parent.right

                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.right.color == 'black':
                        s.left.color = 'black'
                        s.color = 'red'
                        self.__rotate_right(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.right.color = 'black'
                    self.__rotate_left(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.__rotate_right(x.parent)
                    s = x.parent.left

                if s.right.color == 'black' and s.left.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.left.color == 'black':
                        s.right.color = 'black'
                        s.color = 'red'
                        self.__rotate_left(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.left.color = 'black'
                    self.__rotate_right(x.parent)
                    x = self.root
        x.color = 'black'

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def calculate_height(self, node):
        """
        Calcula a altura de um nó na árvore rubro-negra.

        Parâmetros:
            node (Node): O nó a partir do qual a altura será calculada.

        Retorno:
            int: A altura do nó.
        """
        if node == self.TNULL:
            return 0
        else:
            left_height = self.calculate_height(node.left)
            right_height = self.calculate_height(node.right)
            return max(left_height, right_height) + 1
