from mixwords import mix_words, inverse_mix_words, split_into_words, combine_words, mix_state, inverse_mix_state
from key_generation import key_gen

def xor_128(num1,num2):
    # XORs two 128 bit values (and ensures result is 128 bits)
    # Responsible: Max Stott
    return (num1 ^ num2) & ((1 << 128) - 1 )

def rot32(word,rotation):
    # Performs left rotations (may not be necessary depending on python libraries)
    # Responsible: Max Stott
    return ((word << rotation ) | (word >>(32-rotation))) & 0xFFFFFFFF # Shifts left by value of "rotation" and wraps around.

def sub_bytes(state):
    # Applies S-Box substitution layer
    # Responsible:
    pass

def inverse_sub_bytes(state):
    # Reverses S-Box Substitution
    # Responsible:
    pass

def permute_bits(state):
    # Applies P-Box permutation layer
    # Responsible:
    pass

def inverse_permute_bits(state):
    # Reverses P-Box permutation
    # Responsible:
    pass

def mix_layer(state):
    # Applies word mixing layer
    # Responsible: Max Stott
    return mix_state(state)

def inverse_mix_layer(state):
    # Reverses mixing layer 
    # Responsible: Max Stott
    return inverse_mix_state(state)

def key_schedule(master_key):
    # Generates round keys from 128-bit master key
    # Responsible:Jack Fitz
    pass

def constant_schedule():
    # Generates round constants
    # Responsible: neil
    pass

def round_function(state,round_key,round_constant):
    # Defines one full encryption round, to be used within encryption block
    # Responsible: (this relies on every other function - collaborative)
    pass

def inverse_round_function(state,round_key,round_constant):
    # Reverses one full encryption round, to be used within decryption block
    # Responsible: (this relies on every other function - collaborative)
    pass

def encrypt_block(masterkey,plaintext):
    # Main Encryption Function
    # Responsible: (this relies on every other function - collaborative)
    pass

def decrypt_block(ciphertext,masterkey):
    # Main Decryption Function
    # Responsible: (this relies on every other function - collaborative)
    pass

