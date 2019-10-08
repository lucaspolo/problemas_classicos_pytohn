from typing import Dict
from sys import getsizeof as sizeof


class DNA:
    _code: Dict[str, int] = {
        'A': 0b00,
        'C': 0b01,
        'G': 0b10,
        'T': 0b11,
    }

    _reverse_code = {
        v: k for k, v in _code.items()
    }

    def __init__(self, dna: str):
        self._compress(dna)

    def _compress(self, dna: str):
        self._binary_dna: int = 1

        for gene in dna.upper():
            gene_code = self._code.get(gene)
            
            if gene_code is not None:
                self._binary_dna <<= 2
                self._binary_dna |= gene_code
            else:
                raise TypeError(f'Gene {gene} not found')

    def _decompress(self) -> str:
        dna_str: str = ''
        for i in range(0, self._binary_dna.bit_length() - 1, 2):
            gene_code = self._binary_dna >> i & 0b11
            dna_str += self._reverse_code.get(gene_code)

        return dna_str[::-1]

    def __str__(self) -> str:
        return self._decompress()


if __name__ == '__main__':
    dna_str = 'ACGTGTCAGATACA' * 800
    dna = DNA(dna_str)
    print(f'The original size is {sizeof(dna_str)}, compressed is {sizeof(dna._binary_dna)}')

