# =========================================
# File: binary_to_decimal.mojo
# Description:
#   Function for converting binary to decimal.
# =========================================

# -----------------------------------------
# 1. Binary to Decimal Conversion
# -----------------------------------------
fn binary_to_decimal(binary_str: String) -> Int raises: 
    """
    Converts a binary string to its decimal representation.
    Interprets two's complement if the leftmost bit is 1.
    """
    let bit_length = len(binary_str)
    if len(binary_str) == 0:
        raise ValueError("Empty binary string")

    if binary_str[0] == '0':
        return int(binary_str, base=2)
    else:
        var inverted_bits = ""
        for bit in binary_str:
            if bit == '1':
                inverted_bits = inverted_bits + '0'
            else:
                inverted_bits = inverted_bits + '1'
        var positive_part = int(inverted_bits, base=2) + 1
        return -positive_part

fn main():
    let binary_value = "11111111111111111111111110000101"
    let decimal_representation = binary_to_decimal(binary_value)
    print(f"Decimal representation of {binary_value}: {decimal_representation}")

main()