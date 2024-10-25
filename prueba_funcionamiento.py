from huffman.huffmancoding import HuffmanCoding
from huffman.huffmandecoding import HuffmanDecoding

prueba = HuffmanCoding()
text_code = prueba.encode("Hola mundo !")

prueba2 = HuffmanDecoding()
text_decoded = prueba2.decode(text_code, prueba.getTree())

print("Text code: ", text_code)
print("Text decoded: ", text_decoded)
print("Table code: ", prueba.getTable())
print("Summary: ", prueba.getSummary())
