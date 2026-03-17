def ascii_to_binary_and_hex():
    msg = input('\nEnter a message to convert: ')

    bin_num = ''.join(format(ord(char), '08b') for char in msg)
    hex_num = ''.join(format(ord(char), '02x') for char in msg)
    
    print('\n')
    print('Original Message:', msg, '\n')
    print('Message in Binary:', bin_num, '\n')
    print('Message in Hexadecimal:', hex_num,'\n')
    
    return bin_num, hex_num

ascii_to_binary_and_hex()
