def toggle_bits(n):
    # Convert the integer to binary and strip the '0b' prefix
    binary_rep = bin(n)[2:]
    
    # Toggle the bits
    toggled_binary_rep = ''.join('0' if bit == '1' else '1' for bit in binary_rep)
    
    # Convert the toggled binary string back to a decimal integer
    result = int(toggled_binary_rep, 2)
    
    return result

# Example usage:
input_num = int(input("Enter the number you want to toggle: "))
output_num = toggle_bits(input_num)
print(output_num)
