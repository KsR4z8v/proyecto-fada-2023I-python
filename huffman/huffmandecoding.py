from huffman.huffmancoding import HuffmanCoding


class HuffmanDecoding:
    def __init__(self):
        pass

    def decode(self, text, tree):
        current_tree = tree
        decode_string = ""
        for i in text:
            if i == "0":
                current_tree = current_tree.get_left()
            elif i == "1":
                current_tree = current_tree.get_right()

            if current_tree.get_number_key() == -1:
                decode_string += current_tree.key
                current_tree = tree

        return decode_string
