# =========================================
# File: main.py
# Description:
#   Main entry point for the Binary Number System
#   Educational Tool (BNSET)
# =========================================

from core.number_conversion import (
    decimal_to_binary_float,
    binary_to_decimal_float,
    to_ieee754,
    group_bits,
    color_binary_groups,
    parse_number,
    to_base32
)
from visualization.circuit_visualization import show_circuit_menu
from educational.educational_components import main as educational_menu

def show_decimal_to_binary_steps(value: float, int_bits: int = 64) -> None:
    """Show step-by-step decimal to binary conversion."""
    print(f"\n=== Decimal to Binary Conversion Steps ===")
    print(f"Converting {value} to {int_bits}-bit binary\n")
    
    int_part = int(value)
    frac_part = abs(value - int_part)
    
    # Show range for the specified bit size
    max_positive = (1 << (int_bits - 1)) - 1
    min_negative = -(1 << (int_bits - 1))
    print(f"Valid range for {int_bits}-bit signed numbers:")
    print(f"  Maximum positive: {max_positive}")
    print(f"  Minimum negative: {min_negative}\n")
    
    # Convert and show result
    try:
        bin_str = decimal_to_binary_float(value, int_bits=int_bits)
        print(f"Final binary: {bin_str}")
        return bin_str
    except ValueError as e:
        print(f"Error: {e}")
        return None

def show_binary_to_decimal_steps(binary_str: str) -> float:
    """Show step-by-step binary to decimal conversion."""
    if not binary_str:
        print("Error: Empty binary string")
        return None

    if not all(bit in '01' for bit in binary_str):
        print("Error: Invalid binary string")
        return None

    print(f"\n=== Binary to Decimal Conversion Steps ===")
    print(f"Converting {binary_str} to decimal\n")
    
    result = binary_to_decimal_float(binary_str)
    print(f"\nFinal decimal value: {result}")
    return result

def show_ieee754_visualization(value: float) -> None:
    """Show detailed IEEE-754 single precision representation."""
    print("\n=== IEEE-754 Single Precision Visualization ===")
    print(f"Converting {value} to IEEE-754 format\n")
    
    ieee = to_ieee754(value)
    
    # Show binary layout
    print("Binary layout (32 bits):")
    print("| Sign | Exponent | Mantissa |")
    print("|-------|-----------|-----------|")
    print(f"|   {ieee['sign']}   | {ieee['exponent']} | {ieee['mantissa']} |")
    
    # Show detailed breakdown
    print("\nComponent breakdown:")
    print(f"1. Sign bit: {ieee['sign']} ({'negative' if ieee['sign_value'] else 'positive'})")
    print(f"2. Exponent: {ieee['exponent']} (binary) = {ieee['exponent_raw']} (decimal)")
    print(f"   - Bias: 127")
    print(f"   - Actual exponent: {ieee['exponent_raw']} - 127 = {ieee['exponent_bias']}")
    print(f"3. Mantissa: 1.{ieee['mantissa']} = {ieee['mantissa_value']}")
    
    # Show final calculation
    print("\nFinal value calculation:")
    print(f"(-1)^{ieee['sign_value']} × {ieee['mantissa_value']} × 2^{ieee['exponent_bias']}")
    print(f"= {value}")

def show_multi_base_layout(value: float) -> None:
    """Show the number in multiple bases with visualization."""
    print("\n=== Multi-Base Representation ===")
    
    # Handle integer and fractional parts separately
    int_part = int(value)
    frac_part = abs(value - int_part)
    
    # Format in different bases
    bin_str = decimal_to_binary_float(value)
    hex_str = format(abs(int_part), 'X')
    oct_str = format(abs(int_part), 'o')
    base32_str = to_base32(abs(value))
    
    # Create layout table
    print("\nNumber Layout:")
    print("┌─────────┬────────────────────────────────────────┐")
    print("│ Base    │ Representation                         │")
    print("├─────────┼────────────────────────────────────────┤")
    print(f"│ Base 10 │ {value:<40} │")
    print(f"│ Base 16 │ {'-' if value < 0 else ''}0x{hex_str:<38} │")
    print(f"│ Base 32 │ {'-' if value < 0 else ''}{base32_str:<40} │")
    print(f"│ Base 8  │ {'-' if value < 0 else ''}0o{oct_str:<38} │")
    
    # Show binary with color grouping
    colored_bin = color_binary_groups(bin_str)
    print(f"│ Base 2  │ {colored_bin:<40} │")
    print("└─────────┴────────────────────────────────────────┘")
    
    # Show bit patterns with grouping
    print("\nBit Patterns:")
    print(f"Grouped binary: {group_bits(bin_str)}")

def main():
    """Main menu for the Binary Number System Educational Tool."""
    while True:
        print("\n=== Binary Number System Educational Tool (BNSET) ===")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Show IEEE-754 Format")
        print("4. Show Multi-Base Layout")
        print("5. Circuit Visualization")
        print("6. Educational Tools")
        print("7. Exit")
        
        try:
            choice = input("\nEnter choice (1-7): ")
            
            if choice == "1":
                value = float(input("Enter decimal number: "))
                bit_size = int(input("Enter bit size (8, 16, 32, 64, etc.): "))
                if bit_size <= 0 or (bit_size & (bit_size - 1)) != 0:  # Check if power of 2
                    print("Error: Bit size must be a positive power of 2")
                    continue
                bin_str = show_decimal_to_binary_steps(value, bit_size)
                if bin_str:  # Only show additional visualizations if conversion succeeded
                    show_ieee754_visualization(value)
                    show_multi_base_layout(value)
            elif choice == "2":
                value = input("Enter binary number: ")
                result = show_binary_to_decimal_steps(value)
                if result is not None:
                    if '.' in value:  # Show IEEE-754 for fractional results
                        show_ieee754_visualization(result)
                    show_multi_base_layout(float(result))
            elif choice == "3":
                value = float(input("Enter decimal number for IEEE-754 visualization: "))
                show_ieee754_visualization(value)
                show_multi_base_layout(value)
            elif choice == "4":
                value = float(input("Enter decimal number for multi-base visualization: "))
                show_multi_base_layout(value)
            elif choice == "5":
                show_circuit_menu()
            elif choice == "6":
                educational_menu()
            elif choice == "7":
                print("\nThank you for using BNSET!")
                break
                
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
            continue
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main() 