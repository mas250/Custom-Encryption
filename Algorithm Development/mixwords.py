
def rot32(word,rotation):
    return ((word << rotation ) | (word >>(32-rotation))) & 0xFFFFFFFF # Shifts left by value of "rotation" and wraps around.

def mix_words(w0, w1, w2, w3):
    """
    Invertible mixing layer - takes 4 "words", chunks of state text,
    and XORs/shifts them. (might need to write more for the screenshot lol)
    dependencies: rot32 function
    """
    t0 = w0 ^ rot32(w1,3)
    t1 = w1 ^ rot32(t0,5)
    t2 = w2 ^ rot32(t1,7)
    t3 = w3 ^ rot32(t2,11)
    return t0,t1,t2,t3

def inverse_mix_words(t0,t1,t2,t3):
    """
    Inverse of the mix_words function. Reverts rotation/shift.
    dependencies: rot32 function
    """
    w3=t3 ^ rot32(t2,11)
    w2=t2 ^ rot32(t1,7)
    w1=t1 ^ rot32(t0,5)
    w0=t0 ^ rot32(w1,3)
    return w0,w1,w2,w3

def split_into_words(state):
    """
    Splits 128-bit integer into four "words".
    Example use: w0,w1,w2,w3 = split_into_words(state)
    """
    w0 = (state >> 96) & 0xFFFFFFFF # ">>" shifts section forward a certain number of bits. 128-32 = 96,
    w1 = (state>> 64) & 0xFFFFFFFF	# so the first 32 bits are placed at the end. "0xFFFFFFFF" is a 32 bit mask
    w2 = (state >> 32) & 0xFFFFFFFF	# and only keeps the final 32 bits.
    w3 = state  & 0xFFFFFFFF
    return w0,w1,w2,w3

def combine_words(w0,w1,w2,w3):
    """
    Combines four 32-bit words back into a full 128-bit integer.
    Example use: combine_words(w0,w1,w2,w3)
    """
    return ((w0 & 0xFFFFFFFF) << 96) | \
           ((w1 & 0xFFFFFFFF) << 64) | \
           ((w2 & 0xFFFFFFFF) << 32) | \
           (w3 & 0xFFFFFFFF)

def mix_state(state):
    """
    Applies the mixing layer to a 128-bit state
    """
    w0, w1, w2, w3 = split_into_words(state)
    t0, t1, t2, t3 = mix_words(w0, w1, w2, w3)
    return combine_words(t0, t1, t2, t3)

def inverse_mix_state(state):
    """
    Applies the inverse mixing layer to a 128-bit state.
    """
    t0, t1, t2, t3 = split_into_words(state)
    w0, w1, w2, w3 = inverse_mix_words(t0, t1, t2, t3)
    return combine_words(w0, w1, w2, w3)

"""
OPTIONAL TEST/DEBUG CODE:

def test_full_state_mix():
    state = 0x0123456789ABCDEFFEDCBA9876543210

    mixed = mix_state(state)
    recovered = inverse_mix_state(mixed)

    print("Original :", hex(state))
    print("Mixed    :", hex(mixed))
    print("Recovered:", hex(recovered))

    if state == recovered:
        print("Full state mixing works")
    else:
        print("FAIL")
        
"""