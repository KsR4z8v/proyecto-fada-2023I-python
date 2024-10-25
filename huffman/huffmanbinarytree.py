

class HuffmanBinaryTree:

    def __init__(self, key=None, left=None, right=None):

        self.key = key
        self.left = left
        self.right = right

    def get_number_key(self):
        return -1 if type(self.key) == str else self.key

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def calculate_Depth(self, deep=1, alts=[]):
        # el parametro alt es pasado en los llamados recursivos, al pasar el valor alts se esta pasando tambien
        # la referencia del mismo. asi cada llamado recursivo al agregar una nueva altura estara modificando el
        # la lista original
        if deep not in alts:
            alts.append(deep)

        if self.left is not None:
            self.left.calculate_Depth(deep + 1, alts)

        if self.right is not None:
            self.right.calculate_Depth(deep + 1, alts)

        # por ultimo se calcula la mayor altura que se recorrio en cada llamado
        return max(alts)

    def calculate_Cant_Nodes(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.calculate_Cant_Nodes() + self.right.calculate_Cant_Nodes()
        if self.right is not None:
            return 1 + self.right.calculate_Cant_Nodes()
        if self.left is not None:
            return 1 + self.left.calculate_Cant_Nodes()
        return 1
