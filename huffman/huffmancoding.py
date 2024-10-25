
from huffman.huffmanbinarytree import HuffmanBinaryTree
from huffman.Queue_ import Queue
from huffman.Monton import Heap


class HuffmanCoding:
    def __init__(self):
        pass

    def buildFrecuenciesTable(self, text):

        self.table_Frecuencies = {}
        for i in text:
            if self.table_Frecuencies.get(i):
                self.table_Frecuencies[i] += 1
            else:
                self.table_Frecuencies[i] = 1

    def buildHeapLefNodes(self) -> Heap:

        self.size = len(self.table_Frecuencies)
        heap = Heap(self.size)
        q = Queue(self.size)

        for c, f in self.table_Frecuencies.items():
            q.enqueue((f, HuffmanBinaryTree(key=c)))

        heap.arr = q.queue
        return heap

    def buildHuffmanBinaryTree(self, heap):

        n = self.size-1
        while n >= 1:
            heap.heap_sort()
            i = heap.arr[0]
            j = heap.arr[1]
            total = i[0] + j[0]
            heap.arr[0] = (total, HuffmanBinaryTree(
                key=total, left=i[1], right=j[1]))
            heap.arr[1] = (float('inf'),)
            n -= 1
        self.huffmanBinaryTree = heap.arr[0][1]

    def calculateCompressPercentage(self, text_code, text):

        x = len(text_code)
        y = 256*len(text)
        self.percentage = (1 - x/y)*100

    def encode(self, text):

        #validation string
        if(text==""):
            raise Exception('A string with characters is required !')
        
        self.buildFrecuenciesTable(text)
        heap = self.buildHeapLefNodes()

        self.buildHuffmanBinaryTree(heap)
        self.table_codes = self.build_Table_Codes(self.huffmanBinaryTree)

        # recorro la cadena recibida y codifico el mensaje
        text_code = ""
        for i in text:
            text_code += self.table_codes[i]

        self.calculateCompressPercentage(text_code, text)

       # guardo el string en un binario
        cola = Queue(len(text_code))
        for i in text_code:
            cola.enqueue(int(i))
        f = open("salida.bin", "wb")
        arr = bytearray(cola.queue)
        f.write(arr)
        f.close()
        return text_code
        # Funcion temporal

    def build_Table_Codes(self, arb, table={}, r=""):

        table_codes = table
        if arb.get_number_key() == -1:
            table_codes[arb.key] = r

        if arb.left is not None:
            self.build_Table_Codes(arb.left, table_codes, r+"0")

        if arb.right is not None:
            self.build_Table_Codes(arb.right, table_codes, r+"1")

        return table_codes

    def getTree(self):

        return self.huffmanBinaryTree

    def getTable(self):
        return self.table_codes

    def getSummary(self):
        summary = {"percentage_compression": self.percentage,
                   "depth_tree": self.huffmanBinaryTree.calculate_Depth(),
                   "quantity_nodes": self.huffmanBinaryTree.calculate_Cant_Nodes()}
        return summary
