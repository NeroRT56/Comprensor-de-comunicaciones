import os
from heapq import heappush, heappop, heapify
from collections import defaultdict
class comprehension:

    def huffman_code(self, freq):
        heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
        heapify(heap)
        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        return dict(sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))

    def compress(self, input_file_path, output_file_path):
        # Leer el archivo de entrada
        with open(input_file_path, 'r') as input_file:
            input_data = input_file.read()

        # Calcular la frecuencia de cada símbolo en el archivo
        freq = defaultdict(int)
        for symbol in input_data:
            freq[symbol] += 1

        # Obtener los códigos de Huffman correspondientes
        huff = comprehension.huffman_code(self,freq)

        # Escribir los códigos de Huffman en el archivo de salida
        with open(output_file_path, 'w') as output_file:
            for symbol in huff:
                output_file.write(symbol + ':' + huff[symbol] + '\n')

        # Comprimir el archivo de entrada utilizando los códigos de Huffman
        compressed_data = ''
        for symbol in input_data:
            compressed_data += huff[symbol]

        # Escribir los datos comprimidos en el archivo de salida
        with open(output_file_path, 'ab') as output_file:
            while len(compressed_data) % 8 != 0:
                compressed_data += '0'
            for i in range(0, len(compressed_data), 8):
                byte = compressed_data[i:i+8]
                output_file.write(bytes([int(byte, 2)]))

        # Calcular la tasa de compresión
        input_file_size = os.path.getsize(input_file_path)
        output_file_size = os.path.getsize(output_file_path)
        compression_ratio = output_file_size / input_file_size
        print('Tasa de compresión: {:.2f}'.format(compression_ratio))

    def decompress(input_file_path, output_file_path):
        # Leer los códigos de Huffman del archivo de entrada
        huff = {}
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                symbol, code = line.strip().split(':')
                huff[code] = symbol

        # Leer los datos comprimidos del archivo de entrada
        compressed_data = ''
        with open(input_file_path, 'rb') as input_file:
            input_file.seek(len('\n'.join(huff.values())).encode().find(b'\n') + 1)
            byte = input_file.read(1)
            while byte:
                compressed_data += bin(ord(byte))[2:].rjust(8, '0')
                byte = input_file.read(1)

        # Decodificar los datos comprimidos utilizando los códigos de Huffman
        decoded_data = ''
        code = ''
        for bit in compressed_data:
            code += bit
            if code in huff:
                decoded_data += huff[code]
                code = ''

        # Escribir los datos descomprimidos en el archivo de salida
        with open(output_file_path, 'w') as output_file:
            output_file.write(decoded_data)

    # Ejemplo de uso
    input_file_path = 'input.txt'
    compressed_file_path = 'compressed.bin'
    decompressed_file_path = 'output.txt'

    compress(input_file_path, compressed_file_path)
    decompress(compressed_file_path, decompressed_file_path)
    """
    Para utilizar esta clase, se puede crear una instancia de HuffmanCoding y llamar a los métodos compress() y decompress() según sea necesario. Por ejemplo:
    python
    Para utilizar este código, se puede llamar a las funciones compress y decompress según sea necesario. Por ejemplo:
    python
    
    input_file_path = 'input.txt'
    compressed_file_path = 'compressed.bin'
    decompressed_file_path = 'output.txt'

    compress(input_file_path, compressed_file_path)
    decompress(compressed_file_path, decompressed_file_path)
    """