
from heapq import heappush, heappop, heapify
from collections import defaultdict
class compress:
    def huffman_code(freq):
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
        return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    # Ejemplo de uso
    text = "Hola, esto es un ejemplo de texto para comprimir con el algoritmo de códigos de longitud variable."
    freq = defaultdict(int)
    for symbol in text:
        freq[symbol] += 1
    huff = huffman_code(freq)
    print("Símbolo\tFrecuencia\tCódigo Huffman")
    for p in huff:
        print("%s\t\t%s\t\t%s" % (p[0], freq[p[0]], p[1]))
