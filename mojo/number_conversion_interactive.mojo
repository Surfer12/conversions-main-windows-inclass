from utils.table_generator import create_power_table
from decimal_to_binary_v2 import decimal_to_binary
from binary_to_decimal import binary_to_decimal

# =========================================
# File: number_conversion_interactive.mojo
# Description:
#   Interactive utility for number system conversions
#   with step-by-step visualization.
# =========================================

struct ConversionResult:
    var type: String
    var value: Int
    
    fn __init__(inout self, type: String, value: Int):
        self.type = type
        self.value = value

fn show_decimal_to_binary_steps(decimal_value: Int, bit_length: Int) -> String:
    """
    Shows step-by-step decimal to binary conversion with a power table.
    Returns the final binary representation.
    """
    print("\n=== Decimal to Binary Conversion Steps ===")
    print("Converting", decimal_value, "to", bit_length, "-bit binary\n")
    
    # Show power table for positive numbers or absolute value of negative
    let is_negative = decimal_value < 0
    let abs_value = abs(decimal_value)
    
    if is_negative:
        print("1. Take absolute value: |", decimal_value, "| = ", abs_value)
        print("2. Convert absolute value to binary:")
    
    # Generate and show power table
    create_power_table(abs_value, bit_length-1)
    
    # Get binary representation
    let bin_str: String
    if is_negative:
        print("\n3. For negative numbers, use two's complement:")
        bin_str = decimal_to_binary(decimal_value, bit_length)
        print("   a. Get positive binary:  ", decimal_to_binary(abs_value, bit_length))
        print("   b. Invert all bits:      ", bin_str)
        print("   c. Add 1:                ", bin_str)
    else:
        bin_str = decimal_to_binary(decimal_value, bit_length)
    
    print("\nFinal", bit_length, "-bit binary:", bin_str)
    return bin_str

fn show_binary_to_decimal_steps(binary_str: String) -> Int:
    """
    Shows step-by-step binary to decimal conversion.
    Returns the final decimal value.
    """
    print("\n=== Binary to Decimal Conversion Steps ===")
    print("Converting", binary_str, "to decimal\n")
    
    let is_negative = binary_str[0] == '1'
    var decimal_val: Int
    
    if is_negative:
        print("1. Number is negative (leftmost bit is 1)")
        print("2. Using two's complement to convert:")
        print("   a. Original binary:    ", binary_str)
        
        # Invert bits
        var inverted = ""
        for i in range(len(binary_str)):
            if binary_str[i] == '0':
                inverted += "1"
            else:
                inverted += "0"
        print("   b. Invert all bits:    ", inverted)
        
        # Add 1 and convert
        decimal_val = binary_to_decimal(binary_str)
        print("   c. Add 1 and convert:  ", decimal_val)
    else:
        print("1. Number is positive (leftmost bit is 0)")
        decimal_val = binary_to_decimal(binary_str)
        
        # Show power calculation
        print("2. Calculate powers of 2:")
        var total = 0
        for i in range(len(binary_str)-1, -1, -1):
            if binary_str[i] == '1':
                let value = 1 << (len(binary_str) - 1 - i)
                total += value
                print("   2^", len(binary_str) - 1 - i, " = ", value)
        print("\nSum of powers =", total)
    
    print("\nFinal decimal value:", decimal_val)
    return decimal_val

fn get_user_input() -> ConversionResult:
    """Gets conversion type and value from user."""
    print("\n=== Number System Converter ===")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    let choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        let value = input("Enter decimal number: ")
        return ConversionResult("decimal", atol(value))
    else:
        let value = input("Enter binary number: ")
        return ConversionResult("binary", atol(value))

fn main():
    while True:
        try:
            let result = get_user_input()
            
            if result.type == "decimal":
                let _ = show_decimal_to_binary_steps(result.value, 32)
            else:
                let _ = show_binary_to_decimal_steps(str(result.value))
                
            let again = input("\nConvert another number? (y/n): ")
            if again != "y":
                break
                
        except:
            print("Error: Invalid input")
            continue

main() 