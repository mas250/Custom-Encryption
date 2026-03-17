msg = input("Please enter secret message: ")
key = "test"
def xor_algorithm(text, key):
    final_hex=""
    final_bin=""
    for c in range(len(text)):
        chars = ord(text[c]) # ord transforms letters into unicode numbers
        key_val = ord(key[c % len(key)]) # % len() creates a circular index,
                                         # if key is "test", loops around
                                         # T>E>S>T>T>E>S>T 
        
        xor = chars ^ key_val # xor operation happens here (with ^ )
        
        final_bin += format(xor, '08b') # '08b' and '02x' formats strings into binary and
        final_hex += format(xor, '02x') # hexadecimal respectively
    print(f"Original Message: {text}\n")
    print(f"Encrypted Binary: {final_bin}\n")
    print(f"Encrypted Hex: {final_hex}\n")
    
xor_algorithm(msg,key)
    
    