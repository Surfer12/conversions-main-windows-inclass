# number_conversion.mojo

# Alias or define a Float type if needed
# (Earliest Mojo doesn't have a built-in 'Float' type like Python)
type Float = Float64  # or use 'Python.Float' if bridging to Python

# 1) POWER-OF-2 TABLE
def create_power_table(decimal_value: Int, max_exponent: Int = 10) -> None:
    # Prints a markdown-style table from 2^max_exponent down to 2^0
    print("| Power (2^n) | Value | Fits? | Binary Bit |")
    print("|---|---|---|---|")

    var remainder = decimal_value
    for n in range(max_exponent, -1, -1):
        let power_value = (1 << n)  # 2^n
        if power_value <= remainder:
            let leftover = remainder - power_value
            print("| 2^" + str(n) + " | " + str(power_value) + 
                  " | Yes (leftover=" + str(leftover) + ") | 1 |")
            remainder = leftover
        else:
            print("| 2^" + str(n) + " | " + str(power_value) + 
                  " | No | 0 |")

# 2) DECIMAL <-> BINARY
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

# 3) DECIMAL <-> HEX
def decimal_to_hex(decimal_value: Int) -> String:
    if decimal_value >= 0:
        return hex(decimal_value)[2:]
    else:
        return "-" + hex(-decimal_value)[2:]

def hex_to_decimal(hex_str: String) -> Int raises:
    if len(hex_str) == 0:
        raise ValueError("Empty hex string")

    if hex_str.startswith("-"):
        return -(int(hex_str[1:], base=16))
    else:
        return int(hex_str, base=16)

# 4) OPTIONAL FLOAT->IEEE 754 (SINGLE PRECISION)
#    If we want to call Python's 'struct', do:
from Python import import_module
struct = import_module("struct")  # this might raise
def float_to_ieee754_single(value: Float) raises -> String:
    # Pseudocode for single-precision
    # We'll assume a "float" is stored in 'value'
    let pack_result = struct.invoke("pack", [">f", value])  # may raise
    let raw_tuple = struct.invoke("unpack", [">I", pack_result])  # may raise
    # raw_tuple is a 1-element tuple => raw_int
    let raw_int = raw_tuple[0]
    return format(raw_int, "032b")

def ieee754_single_to_float(ieee_binary: String) raises -> Float:
    let raw_int = int(ieee_binary, base=2)  # may raise
    let pack_bytes = struct.invoke("pack", [">I", raw_int])  # may raise
    let float_tuple = struct.invoke("unpack", [">f", pack_bytes])  # may raise
    return float_tuple[0]

# 5) FRACTION -> BINARY
def fraction_to_binary(fraction: Float, max_bits: Int = 8) -> String:
    if fraction < 0.0:
        raise ValueError("Fraction must be non-negative")

    var bits = ""
    var value = fraction
    for i in range(max_bits):
        value = value * 2.0
        if value >= 1.0:
            bits = bits + "1"
            value = value - 1.0
        else:
            bits = bits + "0"

        if value == 0.0:
            break
    return bits

# MAIN DEMO
def main() raises -> None:
    # 1) Table for integer part 11
    print("## Power-of-2 Table for 11")
    create_power_table(11, 10)
    print("")

    # 2) decimal -> binary -> decimal roundtrip
    var dec_val: Int = -42
    var bin_rep = decimal_to_binary(dec_val, 16)
    var roundtrip_dec = binary_to_decimal(bin_rep)  # may raise
    print("Decimal: " + str(dec_val) + 
          " -> Binary(16-bit): " + bin_rep + 
          " -> Back: " + str(roundtrip_dec))

    # 3) decimal -> hex -> decimal roundtrip
    var dec_hex_val: Int = 255
    var hex_rep = decimal_to_hex(dec_hex_val)
    var roundtrip_hex_dec = hex_to_decimal(hex_rep)  # may raise
    print("Decimal: " + str(dec_hex_val) +
          " -> Hex: " + hex_rep +
          " -> Back: " + str(roundtrip_hex_dec))

    # 4) Float -> IEEE 754 single -> float
    var fval: Float = -123.456
    var f_ieee = float_to_ieee754_single(fval)  # may raise
    var f_round = ieee754_single_to_float(f_ieee)  # may raise
    print("Float value: " + str(fval))
    print("IEEE754 single: " + f_ieee)
    print("Converted back: " + str(f_round))

    # 5) Fraction example for 0.25
    # integer = 11 -> binary=1011
    # fraction=0.25 -> 0.01 in binary
    var fraction_bits = fraction_to_binary(0.25, 8)
    print("Example 11.25 => integer=11 (binary=1011) + fraction=0.25 (binary=0." 
          + fraction_bits + ") => 1011." + fraction_bits)

# Uncomment the call to actually run:
# main()