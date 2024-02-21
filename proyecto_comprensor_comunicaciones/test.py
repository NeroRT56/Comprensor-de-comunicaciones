#primero importar las pruebas y el modelo
import unittest
import model2
from collections import defaultdict

# construimos la clase prueba 

class comprehensionTest:
    
    def testZero(self):

        text = "ABRACADABRA"
        #text = "Hola, esto es un ejemplo de texto para comprimir con el algoritmo de códigos de longitud variable."
        freq = defaultdict(int)
        for symbol in text:
            freq[symbol] += 1
        huff = model2.huffman_code(freq)
        print("Símbolo\tFrecuencia\tCódigo Huffman")
        for p in huff:
            print("%s\t\t%s\t\t%s" % (p[0], freq[p[0]], p[1]))
        huffman = model2.huffman_code(text)
        encoded_text, tree = huffman.compress()
        decoded_text = huffman.decompress(encoded_text, tree)

        assert decoded_text == text
    
    """
    
    def testMayus(self):
        pass



    def testMinus(self):
        pass

    def testChange(self):
        pass

    
    def test_4(self):
        pass

    def test_5(self):
        pass

    def test_6(self):
        pass

    def test_7(self):
        pass

    def test_8(self):
        pass

    def test_9(self):
        pass

    def test_10(self):
        pass

    def test_11(self):
        pass

    def test_12(self):
        pass

    def test_13(self):
        pass

    def test_14(self):
        pass

    def test_15(self):
        pass

    def test_16(self):
        pass

    def test_17(self):
        pass

    def test_18(self):
        pass

    def test_19(self):
        pass

    def test_20(self):
        pass
"""
if __name__ == "__name__":
    unittest.main()