import secrets

def key_gen():
    
    # Randomly generates 16 bytes / 128 bits.
    key_bytes = secrets.token_bytes(16)

    #converts to hex string
    key_hex = key_bytes.hex()
    return key_bytes,key_hex


"""
TEST/DEBUG SCRIPT
mykey_bytes,mykey_hex = key_gen()
print(f"Hex Key: {mykey_hex}")
print(f"Key Length: {len(mykey_bytes) * 8} bits") # Bytes * 8 shows how many bits are in the string

"""