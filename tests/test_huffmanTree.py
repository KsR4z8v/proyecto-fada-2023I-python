from huffman.huffmanbinarytree import HuffmanBinaryTree

def test_MethodsTree():
    arb1 = HuffmanBinaryTree(12,
                             HuffmanBinaryTree(
                                 5,
                                 HuffmanBinaryTree("t"),
                                 HuffmanBinaryTree("l")              
                             ),
                            HuffmanBinaryTree(7,
                                HuffmanBinaryTree(2,HuffmanBinaryTree("d"),HuffmanBinaryTree("a")),
                                HuffmanBinaryTree(5,HuffmanBinaryTree("g"),HuffmanBinaryTree("k"))
                                )                          
                             )

    assert arb1.calculate_Cant_Nodes() == 11
    assert arb1.calculate_Depth() == 4
    
    
    
def test_MethodsTree2():
    arb2 = HuffmanBinaryTree(30,
                             HuffmanBinaryTree(3,
                                               HuffmanBinaryTree("k"),
                                               HuffmanBinaryTree("w")),
                             
                             HuffmanBinaryTree(27,
                                               HuffmanBinaryTree(2,
                                                                 HuffmanBinaryTree("h"),
                                                                 HuffmanBinaryTree("ñ")),
                                               
                                               HuffmanBinaryTree(25,
                                                                 HuffmanBinaryTree(24,HuffmanBinaryTree(10,
                                                                                                        HuffmanBinaryTree("1"),
                                                                                                        HuffmanBinaryTree("n")
                                                                                                        ),
                                                                                   HuffmanBinaryTree(14,
                                                                                                        HuffmanBinaryTree("@"),
                                                                                                        HuffmanBinaryTree("22")
                                                                                                        ))
                                                                 ,
                                                                 HuffmanBinaryTree(1,None,HuffmanBinaryTree("p"))
                                                                 )
                                 
                             )
                             )
    
    assert arb2.calculate_Cant_Nodes() == 18
    assert arb2.calculate_Depth() == 6
    
