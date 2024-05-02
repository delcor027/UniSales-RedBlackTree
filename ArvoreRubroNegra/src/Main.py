from RedBlackTree import RedBlackTree

class Main:
    def __init__(self):
        """
        Inicializa a classe Main e cria uma instância da árvore rubro-negra.
        """
        self.rb_tree = RedBlackTree()

    def run(self):
        """
        Executa operações na árvore rubro-negra, incluindo inserções, remoção,
        impressão da árvore e cálculo da altura.
        """
        self.rb_tree.insert(8)
        self.rb_tree.insert(18)
        self.rb_tree.insert(5)
        self.rb_tree.insert(15)
        self.rb_tree.insert(17)
        self.rb_tree.insert(25)
        self.rb_tree.remove(5)

        self.rb_tree.print_tree(self.rb_tree.get_root(), "", True)

        height = self.rb_tree.calculate_height(self.rb_tree.get_root())
        print("Altura da árvore:", height)

if __name__ == "__main__":
    main_instance = Main()
    main_instance.run()

