# =========================================
# File: decimal_to_binary_v2.mojo
# Description:
#   Function for converting decimal to binary.
# =========================================

# -----------------------------------------
# 1. Decimal to Binary Conversion
# -----------------------------------------
fn decimal_to_binary(decimal_value: Int, bit_length: Int = 32) -> String:
    """
    Converts an integer to its binary representation, using
    two's complement if it's negative, restricted to `bit_length` bits.
    """
    if decimal_value >= 0:
        # Positive or zero: just format it
        return format(decimal_value, f'0{bit_length}b')
    else:
        # Negative: compute two's complement within bit_length
        positive_value = -decimal_value
        if positive_value >= (1 << bit_length):
            raise ValueError("Value too negative for the provided bit length.")
        # Format as binary
        bin_pos = format(positive_value, f'0{bit_length}b')
        # Invert bits
        inverted_bits = ''.join('1' if bit == '0' else '0' for bit in bin_pos)
        # Add 1
        twos_comp_int = int(inverted_bits, 2) + 1
        # Convert back to binary string
        twos_comp_str = format(twos_comp_int, f'0{bit_length}b')
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