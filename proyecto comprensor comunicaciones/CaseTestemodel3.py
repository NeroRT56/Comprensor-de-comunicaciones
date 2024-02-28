import unittest
from model3 import HuffmanCoding


from collections import defaultdict
import unittest
#from huffman_coding import HuffmanCoding

class TestHuffmanCoding(unittest.TestCase):

    def test_compression_decompression(self):
        input_text = "hello world"
        huffman = HuffmanCoding("test.txt")
        compressed_file = huffman.compress()
        huffman.decompress(compressed_file)

        with open("test.txt", 'r') as file:
            decompressed_text = file.read()

        self.assertEqual(input_text, decompressed_text)

    def test_padding(self):
        huffman = HuffmanCoding("test.txt")
        padded_text = huffman.pad_encoded_text("1010101")
        self.assertEqual(len(padded_text) % 8, 0)

    def test_frequency_dict(self):
        huffman = HuffmanCoding("test.txt")
        frequency = huffman.make_frequency_dict("hello")
        self.assertEqual(frequency, {'h': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_huffman_code(self):
        freq = {'a':5, 'b': 9, 'c': 12, 'd': 13, 'e':16, 'f': 45}
        expected_result =[('f','0'),('d','10')('e','11'),('c','100'),('b','101'),('a','110')]

        result = HuffmanCoding(freq)
        self.assertEqual(result, expected_result)

    def test_huffman_code_empty_input(self):
        freq = {}
        expected_result = []
        result = HuffmanCoding.compress(freq)

        self.assertEqual(freq, expected_result) 
    def test_huffman_code_single_symbol(self):
        freq = {'a':1}
        expected_result = [('a','0')]
        
        result = HuffmanCoding.compress(freq)
        self.assertEqual(result, expected_result)
        