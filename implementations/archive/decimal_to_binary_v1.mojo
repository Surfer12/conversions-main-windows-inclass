# =========================================
# File: decimal_to_binary_v1.mojo
# Description:
#   Function for converting decimal to binary.
# =========================================

# -----------------------------------------
# 1. Decimal to Binary Conversion
# -----------------------------------------
fn decimal_to_binary(decimal_value: Int, bit_length: Int = 32) -> String:
    """
    Converts a decimal number to its binary representation.
    Uses two's complement for negative numbers.
    """
    if decimal_value >= 0:
        return format(decimal_value, "0" + str(bit_length) + "b")
    else:
        var positive_value = -decimal_value
        if positive_value >= (1 << bit_length):
            raise ValueError("Value too negative for the provided bit length.")
        let bin_pos = format(positive_value, "0" + str(bit_length) + "b")
        var inverted_bits = ""
        for bit in bin_pos:
            if bit == '0':
                inverted_bits = inverted_bits + '1'
            else:
                inverted_bits = inverted_bits + '0'
        let twos_comp_int = int(inverted_bits, base=2) + 1
        let twos_comp_str = format(twos_comp_int, "0" + str(bit_length) + "b")
        return twos_comp_str

fn twos_complement(binary: String) -> String:
    inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary)
    decimal_value = int(inverted_bits, 2) + 1
    return bin(decimal_value)[2:]

fn main():
    decimal_value = 42
    binary_representation = decimal_to_binary(decimal_value)
    print(f"Binary representation of {decimal_value}: {binary_representation}")

main()