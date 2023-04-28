from pathlib import Path

import pytest
from dna import DNA

DNA_SEQ1 = '''
TTGATGCCTAGCTTATGTCATGCGCCGCCCGCACGACTCGATAGCAGCATCGCCCGTTGTATAATTAAAACCCAAGATAT
AACGTACTCCCAAGGTCACGAAGAGAACCCCATGGGAGCGCATACGTGAAGTCTCACCCACAAAACGCCGGCTTCTAGCC
AGCGAGTCCGTCCCTAGAGGCGAATTCGGAAATACTTGCGAGTGAAGAGCGACATTGTTCTTCAGGCCGAATGGCAATAT
CAAAAGAGGTTCATGATCATTTATTTTGTACTACGTAGGTATGCGAACTGTTTAAGCTGCTACGATTTTCACGACTAGAG
'''.replace(
    '\n', ''
)

DNA_SEQ2 = '''
CAACGTGCGTGGGCTCCTGGACTACAGGTCCGTGTGGTGTACAAGCAAGGATACTCCGCAGGTTGAAGGTCAGCCCGGTT
ACGTCAGCCGGTCAACTATACGGTCTTACAGGCATATGATCTGTCCCGAAGTGGGATTACATGTCGCGAATGGGACATTA
CCCTTGGCGTCGTACGCTGCGTTGTGCGAATAGTTCGTCCCTTTCTACGCCATTTTAAAGTCTCCTCGTGCGTAGTGCTT
CGCTAGTCTCGTCGTCTAGACATGCCGAAGCAACCTCGCGATTGTCGCAATATCAGAACCCTTTGAAATTTGCGCAGCCA
'''.replace(
    '\n', ''
)

DNA_SEQ3 = '''
AACGTACTCCCAAGGTCACGAAGAGAACCCCATGGGAGCGCATACGTGAAGTCTCACCCACAAAACGCCGGCTTCTAGCC
CGCTAGTCTCGTCGTCTAGACATGCCGAAGCAACCTCGCGATTGTCGCAATATCAGAACCCTTTGAAATTTGCGCAGCCA
'''.replace(
    '\n', ''
)


@pytest.fixture
def dna1():
    return DNA(DNA_SEQ1)


@pytest.fixture
def dna2():
    return DNA(DNA_SEQ2)


@pytest.fixture
def dna3():
    return DNA(DNA_SEQ3)


def test_build_sequence(dna1: DNA):
    assert isinstance(dna1, DNA)
    assert len(dna1.sequence) == len(DNA_SEQ1)


def test_class_attributes():
    assert DNA.ADENINE == 'A'
    assert DNA.CYTOSINE == 'C'
    assert DNA.GUANINE == 'G'
    assert DNA.THYMINE == 'T'


def test_length(dna1):
    assert len(dna1) == len(DNA_SEQ1)


def test_str(dna1: DNA):
    assert str(dna1) == dna1.sequence


def test_num_adenines(dna1: DNA):
    assert dna1.adenines == 90


def test_num_cytosines(dna1: DNA):
    assert dna1.cytosines == 80


def test_num_guanines(dna1: DNA):
    assert dna1.guanines == 74


def test_num_thymines(dna1: DNA):
    assert dna1.thymines == 76


def test_sum_dna(dna1: DNA, dna2: DNA):
    DNA1_PLUS_DNA2 = '''TTGCTTGCTTGGTTTTGTGGTGTGCCGGTCGGTGTGGTGTATAGGCGCGTCTCCTGTTGTGTTTTTAGGTCCGCCGGTTT
ACGTTAGTCGGTCGGTTATGCGGTGTTCCCGGTGTGTGCTCTTTCGTGAAGTGTGATTCCCTGTCGGGCGTGTTCTATTC
CGCTTGTCGTTGTCTGGTGGGTTGTTCGGATATTTTTTCGCTTTCTGCGCGATTTTGTTGTTTCGTCGTGCTTGGTGTTT
CGCTAGTGTTTTCTTCTCGTTTTTTTTGTGCTACGTCGGTATTGTCGCTGTTTCAGCTGCTTTTGTTTTTTGGGCTGGCG
'''.replace(
        '\n', ''
    )
    result = dna1 + dna2
    assert result.sequence == DNA1_PLUS_DNA2


def test_sum_dna_when_different_sizes(dna1: DNA, dna3: DNA):
    DNA1_PLUS_DNA3 = '''TTGGTGCTTCGCTTGTGTCGTGGGGCGCCCGCTGGGCTCGCTTGCGTGAT
GTCTCGTTGTCTAATTGCCGGCTTCTATCTCGCTTGTTTCGTCGTTTAGG
CATGGCGCCGCATGGTCGCGCTTGTGTGAATTTTCGCCCCCTTTGCGCTT
TGTTCTGGCCAGCGAGTCCGTCCCTAGAGGCGAATTCGGAAATACTTGCG
AGTGAAGAGCGACATTGTTCTTCAGGCCGAATGGCAATATCAAAAGAGGT
TCATGATCATTTATTTTGTACTACGTAGGTATGCGAACTGTTTAAGCTGC
TACGATTTTCACGACTAGAG'''.replace(
        '\n', ''
    )
    result = dna1 + dna3
    assert result.sequence == DNA1_PLUS_DNA3

    result = dna3 + dna1
    assert result.sequence == DNA1_PLUS_DNA3


def test_stats(dna1: DNA):
    assert dna1.stats() == {'A': 28.125, 'C': 25.0, 'G': 23.125, 'T': 23.75}


def test_mul_dna(dna1: DNA, dna2: DNA):
    DNA1_MUL_DNA2 = '''CGTCGCTAACACTAACAGCGCCGAAGTAACGCGTCGAACTG
CATTTCTCAGTCACTGATCTTAGCTC'''.replace(
        '\n', ''
    )
    result = dna1 * dna2
    assert result.sequence == DNA1_MUL_DNA2


def test_mul_dna_when_different_sizes(dna1: DNA, dna3: DNA):
    DNA1_MUL_DNA3 = 'TCTCCCCGCGCACCAACACCGAACAGCGTAACCCC'
    result = dna1 * dna3
    assert result.sequence == DNA1_MUL_DNA3


def test_dump_to_file(dna1: DNA):
    test_file = Path('test1.dna')
    test_file.unlink(missing_ok=True)
    dna1.dump_to_file(test_file)
    assert test_file.read_text() == dna1.sequence
    test_file.unlink(missing_ok=True)


def test_build_from_file(dna1: DNA):
    test_file = Path('test1.dna')
    test_file.unlink(missing_ok=True)
    dna1.dump_to_file(test_file)
    dna = DNA.build_from_file(test_file)
    assert test_file.read_text() == dna.sequence
    test_file.unlink(missing_ok=True)


def test_getbase(dna1: DNA):
    assert dna1[0] == 'T'
    assert dna1[9] == 'A'


def test_setbase(dna1: DNA):
    dna1[0] = 'G'
    assert dna1.sequence[0] == 'G'
    dna1[9] = 'C'
    assert dna1.sequence[9] == 'C'


def test_setbase_when_unknown_base(dna1: DNA):
    dna1[0] = 'X'
    assert dna1.sequence[0] == 'A'
    dna1[9] = 'X'
    assert dna1.sequence[9] == 'A'
