import operator
def logic_algorithm():
    '''allows user to select a logical operator and apply it
    to their message and the set key'''

    msg = input("Please enter secret message: ")
    print(f"Available operators: {', '.join(LOGIC_OPERATORS.keys())}")
    operator_choice = input("Choose operator (xor/and/or/nand): ")
    
    # Dynamically select the function using factory pattern
    logic_func = get_operator(operator_choice)
    
    key = "test"
    final_hex=""
    final_bin=""
    
    # perform encryption using the selected operator
    for i, c in enumerate(msg):
        chars = ord(c)  # convert character to integer code point
        key_val = ord(key[i % len(key)])  # wrap key index when message longer than key
        logic_val = logic_func(chars, key_val)  # apply selected operator dynamically

        final_bin += format(logic_val, '08b')  # append binary representation
        final_hex += format(logic_val, '02x')  # append hex representation

    print(f"\nOriginal Message: {msg}")
    print(f"Binary Message: {[ord(c) for c in msg]}")
    print(f"Binary Key: {key}")
    print(f"Operator: {operator_choice}")
    print(f"Encrypted Binary: {final_bin}")
    print(f"Encrypted Hex: {final_hex}\n")
    
    return final_bin, final_hex, msg

# Factory dictionary - maps operator names to functions
LOGIC_OPERATORS = {
    'xor': operator.xor,
    'and': operator.and_,
    'or': operator.or_,
    'nand': lambda a, b: not (a and b),  # NAND: NOT AND
}

def get_operator(choice):
    """Return the operator function based on user choice."""
    return LOGIC_OPERATORS.get(choice.lower(), operator.xor)  # defaults to xor

logic_algorithm()

