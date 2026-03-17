def encryption_tutorial():
    cypher = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, ' ': 26, '!': 27, '.': 28, '?': 29, '*': 30, '£': 31}
    msg = input('\nEnter a message to convert: ')

    #for each character in the message, get the value from cypher
    #05b -> 5 bit binary
    bin_num = ' '.join(format(cypher.get(char.upper(), ord(char)), '05b') for char in msg)
    
    print('\n')
    print('Original Message:', msg, '\n')
    print('Message in Binary:', bin_num, '\n')
    
    # Get swap positions from user
    user_key1 = int(input('Enter the first bit position to swap : '))
    user_key2 = int(input('Enter the second bit position to swap : '))
    
    key1 = user_key1 -1 #convert to zero based index
    key2 = user_key2 -1

    #swap the specified bits using list manipulation
    encrypted_bin = ' '.join(
        ''.join(
            #not key1 orkey2 -> do nothing, otherwise swap when the index matches the key
            c[bit_index] if bit_index not in [key1, key2] else (c[key2] if bit_index == key1 else c[key1])
            for bit_index in range(5)
        ) if len(c) == 5 else c
        for c in bin_num.split()
    )

    print('Encrypted Binary:', encrypted_bin, '\n')

    inverse_cypher = {number: char for char, number in cypher.items()}
    cryptogram = ''.join(inverse_cypher.get(int(part, 2), '?') for part in encrypted_bin.split())
    print('Encrypted Message:', cryptogram, '\n')
    return bin_num, encrypted_bin

encryption_tutorial()
