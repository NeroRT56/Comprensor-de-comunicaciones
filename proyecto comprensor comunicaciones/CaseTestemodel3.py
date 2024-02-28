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