import string

# define braille space character
braille_space = '000000'
# define braille uppercase prefix
braille_upper = '000001'
# define braille alpha characters
braille_alpha = [
    '100000', # a
    '110000', # b
    '100100', # c
    '100110', # d
    '100010', # e
    '110100', # f
    '110110', # g
    '110010', # h
    '010100', # i
    '010110', # j
    '101000', # k
    '111000', # l
    '101100', # m
    '101110', # n
    '101010', # o
    '111100', # p
    '111110', # q
    '111010', # r
    '011100', # s
    '011110', # t
    '101001', # u
    '111001', # v
    '010111', # w
    '101101', # x
    '101111', # y
    '101011', # z
]

# merge braille lowercase, uppercase and space characters into a single list
braille_list = braille_alpha + [braille_upper + s for s in braille_alpha] + [braille_space]
# merge ascii lowercase, uppercase and space characters intto a single list
ascii_list = list(string.ascii_lowercase + string.ascii_uppercase + " ")

# create translastion table
translation_table = dict(zip(ascii_list, braille_list))

def answer(plaintext):
    characters = list(plaintext)
    braille = [translation_table[v] for v in characters if v in characters]
    return ''.join(braille)
