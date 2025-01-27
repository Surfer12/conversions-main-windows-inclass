# =========================================
# File: number_conversion_interactive.py
# Description:
#   Interactive utility for number system conversions
#   with step-by-step visualization.
# =========================================

import struct

class Colors:
    """ANSI color codes for terminal output."""
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def create_power_table(decimal_value: float, max_exponent: int = 10, show_fractional: bool = False) -> None:
    """
    Prints a table showing powers of 2 and whether they fit in decimal_value.
    """
    int_part = int(decimal_value)
    if show_fractional:
        print("| Power (2^n) | Value      | Does {} fit? | Binary Bit |".format(decimal_value))
    else:
        print("| Power (2^n) | Value      | Does {} fit? | Binary Bit |".format(int_part))
    print("|-------------|------------|--------------|------------|")

    remainder = int_part
    for n in range(max_exponent, -1, -1):
        power_value = 1 << n  # 2^n
        if power_value <= remainder:
            remainder_str = f"(leftover={remainder - power_value})"
            print(f"| 2^{n:<9} | {power_value:<10} | Yes {remainder_str:<8} | 1          |")
            remainder -= power_value
        else:
            print(f"| 2^{n:<9} | {power_value:<10} | No           | 0          |")

def create_fractional_power_table(fractional_part: float, precision: int = 4) -> None:
    """
    Prints a table showing negative powers of 2 for fractional part.
    """
    print("\nFractional part powers:")
    print("| Power (2^-n) | Value      | Does {} fit? | Binary Bit |".format(fractional_part))
    print("|--------------|------------|--------------|------------|")

    remainder = fractional_part
    for n in range(1, precision + 1):
        power_value = 2 ** -n
        if power_value <= remainder:
            remainder_str = f"(leftover={remainder - power_value:.6f})"
            print(f"| 2^-{n:<8} | {power_value:<10.6f} | Yes {remainder_str:<8} | 1          |")
            remainder -= power_value
        else:
            print(f"| 2^-{n:<8} | {power_value:<10.6f} | No           | 0          |")

def decimal_to_binary_float(decimal_value: float, int_bits: int = 32, frac_bits: int = 4) -> str:
    """Convert decimal (including fractional) to binary string."""
    int_part = int(decimal_value)
    frac_part = abs(decimal_value - int_part)
    
    # Convert integer part
    if int_part >= 0:
        int_str = format(int_part, f'0{int_bits}b')
    else:
        # Handle negative numbers using two's complement
        max_val = (1 << int_bits)
        int_str = format((max_val + int_part) & (max_val - 1), f'0{int_bits}b')
    
    # Convert fractional part
    if frac_part == 0:
        return int_str
    
    frac_str = ""
    for _ in range(frac_bits):
        frac_part *= 2
        if frac_part >= 1:
            frac_str += "1"
            frac_part -= 1
        else:
            frac_str += "0"
    
    return f"{int_str}.{frac_str}"

def show_decimal_to_binary_steps(decimal_value: float, int_bits: int = 32, frac_bits: int = 4) -> str:
    """Show step-by-step decimal to binary conversion."""
    print(f"\n=== Decimal to Binary Conversion Steps ===")
    print(f"Converting {decimal_value} to binary\n")
    
    int_part = int(decimal_value)
    frac_part = abs(decimal_value - int_part)
    
    is_negative = decimal_value < 0
    abs_value = abs(int_part)
    
    # Integer part conversion
    if is_negative:
        print(f"1. Take absolute value: |{decimal_value}| = {abs(decimal_value)}")
        print(f"2. Split into integer and fractional parts:")
        print(f"   Integer part: {abs_value}")
        print(f"   Fractional part: {frac_part}")
        print("\n3. Convert absolute integer part to binary:")
    else:
        print(f"1. Split into integer and fractional parts:")
        print(f"   Integer part: {int_part}")
        print(f"   Fractional part: {frac_part}")
        print("\n2. Convert integer part to binary:")
    
    create_power_table(abs_value, int_bits-1)
    
    # Fractional part conversion
    if frac_part > 0:
        print("\n3. Convert fractional part to binary:")
        create_fractional_power_table(frac_part, frac_bits)
    
    # Get final binary representation
    bin_str = decimal_to_binary_float(decimal_value, int_bits, frac_bits)
    print(f"\nFinal binary: {bin_str}")
    return bin_str

def binary_to_decimal(binary_str: str) -> int:
    """Convert binary string to decimal, handling unsigned numbers."""
    return int(binary_str, 2)

def binary_to_decimal_float(binary_str: str) -> float:
    """Convert binary string to decimal, handling fractional parts."""
    if '.' not in binary_str:
        return float(binary_to_decimal(binary_str))
        
    # Split into integer and fractional parts
    if '.' in binary_str:
        parts = binary_str.split('.')
    else:
        parts = [binary_str]
    int_part = parts[0]
    frac_part = parts[1] if len(parts) > 1 else ''
    
    # Convert integer part
    int_value = binary_to_decimal(int_part) if int_part else 0
    
    # Convert fractional part
    frac_value = 0.0
    for i, bit in enumerate(frac_part, 1):
        if bit == '1':
            frac_value += 2 ** -i
            
    return float(int_value) + frac_value

def show_binary_to_decimal_steps(binary_str: str) -> float:
    """Show step-by-step binary to decimal conversion."""
    print(f"\n=== Binary to Decimal Conversion Steps ===")
    print(f"Converting {binary_str} to decimal\n")
    
    # Split into integer and fractional parts
    if '.' in binary_str:
        parts = binary_str.split('.')
    else:
        parts = [binary_str]
    int_part = parts[0]
    frac_part = parts[1] if len(parts) > 1 else ''
    
    # Integer part conversion
    is_negative = int_part and int_part[0] == '1'
    if is_negative:
        print("1. Number is negative (leftmost bit is 1)")
        print("2. Using two's complement for integer part:")
        print(f"   a. Original binary:     {int_part}")
        
        # Invert bits
        inverted = ''.join('1' if bit == '0' else '0' for bit in int_part)
        print(f"   b. Invert all bits:     {inverted}")
        
        # Add 1 and convert
        int_value = binary_to_decimal(int_part)
        print(f"   c. Add 1 and convert:   {int_value}")
    else:
        print("1. Integer part is positive (leftmost bit is 0)")
        int_value = binary_to_decimal(int_part)
        if int_part:
            print("2. Calculate integer powers of 2:")
            total = 0
            for i, bit in enumerate(reversed(int_part)):
                if bit == '1':
                    value = 1 << i
                    total += value
                    print(f"   2^{i} = {value}")
            print(f"\nInteger sum = {total}")
    
    # Fractional part conversion
    if frac_part:
        print("\n3. Convert fractional part:")
        print("   Calculate negative powers of 2:")
        frac_value = 0.0
        for i, bit in enumerate(frac_part, 1):
            if bit == '1':
                value = 2 ** -i
                frac_value += value
                print(f"   2^-{i} = {value}")
        print(f"\nFractional sum = {frac_value}")
        final_value = float(int_value) + frac_value
    else:
        final_value = float(int_value)
    
    print(f"\nFinal decimal value: {final_value}")
    return final_value

def to_ieee754(value: float) -> dict:
    """Convert a float to IEEE-754 single precision format."""
    # Convert float to IEEE-754 binary representation
    binary = format(struct.unpack('!I', struct.pack('!f', value))[0], '032b')
    
    # Split into parts
    sign = binary[0]
    exponent = binary[1:9]
    mantissa = binary[9:]
    
    # Calculate components
    sign_value = int(sign)
    exponent_raw = int(exponent, 2)
    exponent_bias = exponent_raw - 127
    mantissa_value = 1 + sum(int(b) * 2**-i for i, b in enumerate(mantissa, 1))
    
    return {
        'binary': binary,
        'sign': sign,
        'exponent': exponent,
        'mantissa': mantissa,
        'sign_value': sign_value,
        'exponent_raw': exponent_raw,
        'exponent_bias': exponent_bias,
        'mantissa_value': mantissa_value
    }

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

def group_bits(binary: str, group_size: int = 4) -> str:
    """Group binary digits for easier reading."""
    if '.' in binary:
        int_part, frac_part = binary.split('.')
        grouped_int = ' '.join(int_part[i:i+group_size] for i in range(0, len(int_part), group_size)).strip()
        grouped_frac = ' '.join(frac_part[i:i+group_size] for i in range(0, len(frac_part), group_size)).strip()
        return f"{grouped_int}.{grouped_frac}"
    return ' '.join(binary[i:i+group_size] for i in range(0, len(binary), group_size)).strip()

def show_bit_mapping(bin_str: str) -> None:
    """Show how bits map between different bases."""
    print("\nBit Mapping:")
    
    # Split into integer and fractional parts if needed
    if '.' in bin_str:
        parts = bin_str.split('.')
    else:
        parts = [bin_str]
    int_part = parts[0]
    frac_part = parts[1] if len(parts) > 1 else ''
    
    # Pad integer part to multiple of 12 (LCM of 3 and 4 for octal and hex grouping)
    pad_len = (12 - len(int_part) % 12) % 12
    padded_bin = '0' * pad_len + int_part
    
    print("Binary groups (4 bits):")
    print(' '.join(padded_bin[i:i+4] for i in range(0, len(padded_bin), 4)))
    print("Hex digits:           ", end='')
    for i in range(0, len(padded_bin), 4):
        group = padded_bin[i:i+4]
        print(f"  {format(int(group, 2), 'X')}  ", end='')
    print("\n")
    
    print("Binary groups (3 bits):")
    print(' '.join(padded_bin[i:i+3] for i in range(0, len(padded_bin), 3)))
    print("Octal digits:         ", end='')
    for i in range(0, len(padded_bin), 3):
        group = padded_bin[i:i+3]
        print(f" {format(int(group, 2), 'o')} ", end='')
    print("\n")
    
    if frac_part:
        print("Fractional part mapping:")
        # Pad fractional part to multiple of 4 for hex grouping
        frac_pad = (4 - len(frac_part) % 4) % 4
        padded_frac = frac_part + '0' * frac_pad
        
        print("Binary groups:", ' '.join(padded_frac[i:i+4] for i in range(0, len(padded_frac), 4)))
        print("Hex digits:  ", end='')
        for i in range(0, len(padded_frac), 4):
            group = padded_frac[i:i+4]
            print(f"  {format(int(group, 2), 'X')}  ", end='')
        print()

def color_binary_groups(binary: str, group_size: int = 4) -> str:
    """Group binary digits with alternating colors."""
    colors = [Colors.BLUE, Colors.GREEN, Colors.YELLOW, Colors.MAGENTA]
    if '.' in binary:
        int_part, frac_part = binary.split('.')
        # Color integer part
        grouped_int = ''
        for i, chunk in enumerate(range(0, len(int_part), group_size)):
            group = int_part[chunk:chunk+group_size]
            color = colors[i % len(colors)]
            grouped_int += f"{color}{group}{Colors.ENDC} "
        # Color fractional part
        grouped_frac = ''
        for i, chunk in enumerate(range(0, len(frac_part), group_size)):
            group = frac_part[chunk:chunk+group_size]
            color = colors[i % len(colors)]
            grouped_frac += f"{color}{group}{Colors.ENDC} "
        return f"{grouped_int.strip()}.{grouped_frac.strip()}"
    return ' '.join(f"{colors[i % len(colors)]}{binary[i:i+group_size]}{Colors.ENDC}" 
                   for i in range(0, len(binary), group_size)).strip()

def perform_binary_arithmetic(a: str, b: str, operation: str = 'add') -> tuple[str, list[str]]:
    """Perform binary arithmetic operations with step-by-step explanation."""
    # Remove '0b' prefix if present
    a = a[2:] if a.startswith('0b') else a
    b = b[2:] if b.startswith('0b') else b
    
    # Ensure equal length for add/sub; for multiply, we'll handle differently
    max_len = max(len(a), len(b))
    
    if operation in ['add', 'subtract']:
        a = a.zfill(max_len)
        b = b.zfill(max_len)
    
    if operation == 'add':
        # Binary addition
        carry = 0
        result = ''
        steps = []
        
        for i in range(max_len-1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])
            current_sum = bit_a + bit_b + carry
            result = str(current_sum % 2) + result
            carry = current_sum // 2
            steps.append(f"Position {max_len-i}: {bit_a} + {bit_b} + carry({carry}) = {current_sum}")
        
        if carry:
            result = '1' + result
            steps.append("Final carry: 1")
        
        return result, steps
            
    elif operation == 'subtract':
        # Two's complement subtraction
        # Convert b to its two's complement
        b_complement = ''
        for bit in b:
            b_complement += '1' if bit == '0' else '0'
        
        # Add 1 to get two's complement
        carry = 1
        b_twos = ''
        for i in range(max_len-1, -1, -1):
            bit = int(b_complement[i])
            current_sum = bit + carry
            b_twos = str(current_sum % 2) + b_twos
            carry = current_sum // 2
        
        # Now add a and b_twos
        carry = 0
        result = ''
        steps = ["Two's complement steps:"]
        steps.append(f"1. Invert bits:     {b} → {b_complement}")
        steps.append(f"2. Add 1:           {b_complement} → {b_twos}")
        steps.append("\nSubtraction steps (using addition with two's complement):")
        
        for i in range(max_len-1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b_twos[i])
            current_sum = bit_a + bit_b + carry
            result = str(current_sum % 2) + result
            carry = current_sum // 2
            steps.append(f"Position {max_len-i}: {bit_a} + {bit_b} + carry({carry}) = {current_sum}")
        
        return result, steps
    elif operation == 'multiply':
        steps = []
        partials = []
        
        # For multiplication, result can be up to sum of bit lengths
        result_len = len(a) + len(b)
        
        # Zero-extend both strings for consistent alignment
        A = a.zfill(result_len)
        B = b.zfill(result_len)
        
        accumulator = 0
        steps.append(f"Multiplication (bit-by-bit partial products):\n  A = {a}, B = {b}")
        
        # Generate partial products
        for i in range(len(B)):
            bit_idx = len(B) - 1 - i
            bit_b = int(B[bit_idx])
            
            if bit_b == 1:
                partial_val = int(A, 2) << i
                accumulator += partial_val
                
                partial_bin = format(partial_val, f"0{result_len}b")
                steps.append(f"Step {i+1}: B[{bit_idx}] = 1:")
                steps.append(f"  Shift A left by {i}:")
                steps.append(f"  {color_binary_groups(partial_bin)}")
                partials.append(partial_val)
            else:
                steps.append(f"Step {i+1}: B[{bit_idx}] = 0 → Skip (partial product = 0)")
        
        # Show running sum after each partial product
        if len(partials) > 0:
            steps.append("\nRunning sums:")
            running_sum = 0
            for i, partial in enumerate(partials, 1):
                running_sum += partial
                sum_bin = format(running_sum, f"0{result_len}b")
                steps.append(f"After partial product {i}: {color_binary_groups(sum_bin)}")
        
        result = format(accumulator, f"0{result_len}b")
        steps.append(f"\nFinal result: {color_binary_groups(result)}")
        
        return result, steps
    elif operation == 'divide':
        if all(bit == '0' for bit in b):
            raise ValueError("Division by zero")
            
        steps = []
        # Convert to integers for division
        dividend = int(a, 2)
        divisor = int(b, 2)
        
        # Store original values for step display
        orig_dividend = format(dividend, f'0{len(a)}b')
        orig_divisor = format(divisor, f'0{len(b)}b')
        
        steps.append(f"Division: {color_binary_groups(orig_dividend)} ÷ {color_binary_groups(orig_divisor)}")
        steps.append("\nStep-by-step division:")
        
        # Find the position of the first 1 in the dividend
        first_one = 0
        temp_dividend = dividend
        while temp_dividend > 0:
            first_one += 1
            temp_dividend >>= 1
            
        # Find position of first 1 in divisor
        first_one_divisor = 0
        temp_divisor = divisor
        while temp_divisor > 0:
            first_one_divisor += 1
            temp_divisor >>= 1
            
        # Initialize quotient and remainder
        quotient = 0
        remainder = dividend
        
        # Track each step
        step_num = 1
        while remainder >= divisor and first_one >= first_one_divisor:
            # Calculate current bit position
            shift = first_one - first_one_divisor
            
            # Try to subtract shifted divisor
            shifted_divisor = divisor << shift
            if remainder >= shifted_divisor:
                remainder -= shifted_divisor
                quotient |= (1 << shift)
                
                # Show the step
                steps.append(f"\nStep {step_num}:")
                steps.append(f"Current remainder: {color_binary_groups(format(remainder, 'b').zfill(len(a)))}")
                steps.append(f"Shifted divisor:   {color_binary_groups(format(shifted_divisor, 'b').zfill(len(a)))}")
                steps.append(f"After subtraction: {color_binary_groups(format(remainder, 'b').zfill(len(a)))}")
                steps.append(f"Current quotient:  {color_binary_groups(format(quotient, 'b'))}")
                step_num += 1
            
            first_one -= 1
            
        # Format results
        quotient_bin = format(quotient, f'0{len(a)}b')
        remainder_bin = format(remainder, f'0{len(b)}b')
        
        steps.append(f"\nFinal Results:")
        steps.append(f"Quotient:  {color_binary_groups(quotient_bin)}")
        steps.append(f"Remainder: {color_binary_groups(remainder_bin)}")
        
        return quotient_bin, steps
    else:
        raise ValueError(f"Unknown operation: {operation}")

BASE32_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

def convert_base(number, base):
    if base == 32:
        # Standard base 32 alphabet (0-9, A-V)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
        integer_part = int(number)
        fractional_part = number - integer_part
        
        if integer_part == 0:
            integer_representation = "0"
        else:
            integer_representation = ""
            while integer_part > 0:
                remainder = integer_part % base
                integer_representation = alphabet[remainder] + integer_representation
                integer_part //= base
                
        if fractional_part > 0:
            fractional_representation = "."
            for _ in range(5):  # Limit fractional digits for practical purposes
                fractional_part *= base
                digit = int(fractional_part)
                fractional_representation += alphabet[digit]
                fractional_part -= digit
                if fractional_part == 0:
                    break
        else:
            fractional_representation = ""
            
        return integer_representation + fractional_representation
    # ... existing code for other bases ...

def to_base32(value: float) -> str:
    """Convert a number to base32 representation."""
    int_part = int(value)
    frac_part = value - int_part
    
    # Convert integer part
    if int_part == 0:
        base32_int = "0"
    else:
        base32_int = ""
        while int_part > 0:
            base32_int = BASE32_CHARS[int_part % 32] + base32_int
            int_part //= 32
    
    # Convert fractional part (up to 6 base32 digits)
    if frac_part == 0:
        return base32_int
        
    base32_frac = ""
    for _ in range(6):
        frac_part *= 32
        digit = int(frac_part)
        base32_frac += BASE32_CHARS[digit]
        frac_part -= digit
        if frac_part == 0:
            break
    
    return f"{base32_int}.{base32_frac}"

def show_arithmetic_operation(a: float, b: float, operation: str = 'add') -> None:
    """Show binary arithmetic operation with step-by-step explanation."""
    from signed_representations import check_overflow, show_carry_chain, show_number_representations
    
    print(f"\n=== Binary {operation.capitalize()}ition ===")
    
    # Convert to binary
    a_bin = format(int(a), 'b')
    b_bin = format(int(b), 'b')
    
    # Ensure equal length and add color
    max_len = max(len(a_bin), len(b_bin))
    if operation != 'multiply':
        max_len += 1  # Extra bit for carry/borrow
    
    print("\nOperands:")
    print(f"A = {a:10} = {color_binary_groups(a_bin)}")
    print(f"B = {b:10} = {color_binary_groups(b_bin)}")
    
    # Show number representations for both operands
    print("\nNumber Representations:")
    print("\nOperand A:")
    show_number_representations(int(a), max_len)
    print("\nOperand B:")
    show_number_representations(int(b), max_len)
    
    # Show carry chain for add/subtract
    if operation in ['add', 'subtract']:
        show_carry_chain(a_bin.zfill(max_len), b_bin.zfill(max_len), operation)
    elif operation == 'divide' and b == 0:
        print("\nError: Division by zero!")
        return
    
    # Perform operation
    try:
        result_bin, steps = perform_binary_arithmetic(a_bin, b_bin, operation)
    except ValueError as e:
        if str(e) == "Division by zero":
            print("\nError: Division by zero!")
            return
        raise
    
    # Show detailed steps
    print("\nDetailed Steps:")
    for step in steps:
        print(step)
    
    # Show result and check for overflow
    result_dec = int(result_bin, 2)
    check_len = max_len
    has_overflow, overflow_msg = check_overflow(int(a), int(b), result_dec, check_len, operation)
    
    print(f"\nResult:")
    if operation == 'divide':
        remainder_bin = format(int(a) % int(b), f'0{len(b_bin)}b')
        print(f"Quotient (Binary):  {color_binary_groups(result_bin)}")
        print(f"Quotient (Decimal): {result_dec}")
        print(f"Remainder (Binary): {color_binary_groups(remainder_bin)}")
        print(f"Remainder (Decimal): {int(a) % int(b)}")
    else:
        print(f"Binary:  {color_binary_groups(result_bin)}")
        print(f"Decimal: {result_dec}")
    
    if has_overflow:
        print(f"\nWarning: {overflow_msg}")
    
    # Show result's number representations
    print("\nResult representations:")
    show_number_representations(result_dec, check_len)

def show_multi_base_layout(value: float) -> None:
    """Show the number in decimal, hexadecimal, binary, octal, and base32 formats."""
    print("\n=== Multi-Base Representation ===")
    
    # Handle integer and fractional parts separately
    int_part = int(value)
    frac_part = abs(value - int_part)
    
    # Format integer part in different bases
    hex_int = format(abs(int_part), 'X')
    oct_int = format(abs(int_part), 'o')
    bin_int = format(abs(int_part), 'b')
    
    # Format fractional part (if exists)
    if frac_part > 0:
        # Convert fraction to binary (up to 12 bits precision)
        bin_frac = ""
        frac = frac_part
        for _ in range(12):  # Increased precision for better octal conversion
            frac *= 2
            if frac >= 1:
                bin_frac += "1"
                frac -= 1
            else:
                bin_frac += "0"
        
        # Convert binary fraction to hex and octal
        hex_frac = ""
        for i in range(0, len(bin_frac), 4):
            chunk = bin_frac[i:i+4].ljust(4, '0')
            hex_digit = format(int(chunk, 2), 'X')
            hex_frac += hex_digit
            
        oct_frac = ""
        for i in range(0, len(bin_frac), 3):
            chunk = bin_frac[i:i+3].ljust(3, '0')
            oct_digit = format(int(chunk, 2), 'o')
            oct_frac += oct_digit
    
    # Create layout table
    print("\nNumber Layout:")
    print("┌─────────┬────────────────────────────────────────┐")
    print("│ Base    │ Representation                         │")
    print("├─────────┼────────────────────────────────────────┤")
    
    # Decimal (Base 10)
    print(f"│ Base 10 │ {value:<40} │")
    
    # Hexadecimal (Base 16)
    if frac_part > 0:
        hex_repr = f"{'-' if value < 0 else ''}0x{hex_int}.{hex_frac}"
    else:
        hex_repr = f"{'-' if value < 0 else ''}0x{hex_int}"
    print(f"│ Base 16 │ {hex_repr:<40} │")
    
    # Base 32
    base32_repr = to_base32(abs(value))
    if value < 0:
        base32_repr = f"-{base32_repr}"
    print(f"│ Base 32 │ {base32_repr:<40} │")
    
    # Octal (Base 8)
    if frac_part > 0:
        oct_repr = f"{'-' if value < 0 else ''}0o{oct_int}.{oct_frac}"
    else:
        oct_repr = f"{'-' if value < 0 else ''}0o{oct_int}"
    print(f"│ Base 8  │ {oct_repr:<40} │")
    
    # Binary (Base 2)
    if frac_part > 0:
        bin_repr = f"{'-' if value < 0 else ''}0b{bin_int}.{bin_frac}"
    else:
        bin_repr = f"{'-' if value < 0 else ''}0b{bin_int}"
    colored_bin = color_binary_groups(bin_repr[2:])
    print(f"│ Base 2  │ {colored_bin:<40} │")
    print("└─────────┴────────────────────────────────────────┘")
    
    # Show bit patterns with grouping
    print("\nBit Patterns:")
    if frac_part > 0:
        print(f"Binary integer part:  {group_bits(bin_int)}")
        print(f"Binary fraction part: {group_bits(bin_frac)}")
    else:
        print(f"Binary pattern: {group_bits(bin_int)}")
    
    # Show bit mapping between bases
    show_bit_mapping(bin_int + ('.' + bin_frac if frac_part > 0 else ''))
    
    # Show conversion steps
    print("\nConversion Steps:")
    print("1. Decimal to Hexadecimal:")
    print(f"   {value} (base 10) = {hex_repr} (base 16)")
    print("2. Decimal to Octal:")
    print(f"   {value} (base 10) = {oct_repr} (base 8)")
    print("3. Decimal to Binary:")
    print(f"   {value} (base 10) = {bin_repr} (base 2)")
    if frac_part > 0:
        print("4. Fractional part conversion:")
        print(f"   0.{bin_frac} (binary) = {frac_part} (decimal)")

def parse_number(value: str, base: int = 10) -> int:
    """Parse a number string in given base, handling binary format."""
    # Remove prefix if present
    if base == 2 and value.startswith(('0b', '0B')):
        value = value[2:]
    elif base == 16 and value.startswith(('0x', '0X')):
        value = value[2:]
    elif base == 8 and value.startswith(('0o', '0O')):
        value = value[2:]
    
    # Remove any spaces or underscores used for readability
    value = value.replace(' ', '').replace('_', '')
    
    # Handle decimal point
    if '.' in value:
        value = value.split('.')[0]  # Take only integer part
    
    return int(value, base)

def main():
    import sys
    from pathlib import Path
    
    # Add the root directory to Python path
    root_dir = Path(__file__).parent.parent
    if str(root_dir) not in sys.path:
        sys.path.append(str(root_dir))
    
    while True:
        print("\n=== Binary Number System Educational Tool (BNSET) ===")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Show IEEE-754 Format")
        print("4. Show Multi-Base Layout")
        print("5. Binary Arithmetic")
        print("6. Show Number Representations")
        print("7. Show Overflow Cases")
        print("8. Circuit Visualization")
        print("9. Educational Tools")
        print("10. Hexadecimal Input Conversion")
        print("11. Exit")
        try:
            choice = input("Enter choice (1-11): ")
            
            if choice == "9":
                from educational.educational_components import main as educational_menu
                educational_menu()
            elif choice == "11":
                print("\nThank you for using BNSET!")
                break
            elif choice == "10":
                print("\nEnter hexadecimal number (with or without 0x prefix):")
                hex_str = input("Enter hex number: ").strip()
                # Remove 0x prefix if present
                hex_str = hex_str[2:] if hex_str.startswith(('0x', '0X')) else hex_str
                
                try:
                    # Convert hex to decimal
                    if '.' in hex_str:
                        int_part, frac_part = hex_str.split('.')
                        value = float.fromhex(f"0x{int_part}.{frac_part}")
                    else:
                        value = float.fromhex(f"0x{hex_str}")
                    
                    print(f"\nHexadecimal: 0x{hex_str}")
                    print(f"Decimal: {value}")
                    
                    # Show various representations
                    show_decimal_to_binary_steps(value)
                    show_ieee754_visualization(value)
                    show_multi_base_layout(value)
                except ValueError:
                    print("Error: Invalid hexadecimal number")
                    continue
            elif choice == "8":
                from circuit_visualization import show_circuit_menu
                show_circuit_menu()
            elif choice == "7":
                bits = int(input("Enter number of bits to demonstrate (4-8, default 4): ") or "4")
                if bits < 4 or bits > 8:
                    print("Number of bits must be between 4 and 8")
                    continue
                from signed_representations import show_overflow_cases
                show_overflow_cases(bits)
            elif choice == "5":
                print("\nBinary Arithmetic Operations:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                op_choice = input("Choose operation (1-4): ")
                
                print("\nEnter numbers in any format:")
                print("- Decimal: 42")
                print("- Binary: 0b101010 or 101010")
                print("- Hex: 0x2A")
                
                a_str = input("Enter first number: ")
                b_str = input("Enter second number: ")
                
                # Try to parse in different bases
                try:
                    if a_str.startswith(('0b', '0B')):
                        a = parse_number(a_str, 2)
                    elif a_str.startswith(('0x', '0X')):
                        a = parse_number(a_str, 16)
                    else:
                        a = parse_number(a_str, 10)
                        
                    if b_str.startswith(('0b', '0B')):
                        b = parse_number(b_str, 2)
                    elif b_str.startswith(('0x', '0X')):
                        b = parse_number(b_str, 16)
                    else:
                        b = parse_number(b_str, 10)
                except ValueError:
                    print("Error: Invalid number format")
                    continue
                
                operation = {
                    '1': 'add',
                    '2': 'subtract',
                    '3': 'multiply',
                    '4': 'divide'
                }.get(op_choice, 'add')
                
                show_arithmetic_operation(float(a), float(b), operation)
            elif choice == "6":
                print("\nEnter number in any format:")
                print("- Decimal: 42")
                print("- Binary: 0b101010 or 101010")
                print("- Hex: 0x2A")
                
                value_str = input("Enter number: ")
                try:
                    if value_str.startswith(('0b', '0B')):
                        value = parse_number(value_str, 2)
                    elif value_str.startswith(('0x', '0X')):
                        value = parse_number(value_str, 16)
                    else:
                        value = parse_number(value_str, 10)
                except ValueError:
                    print("Error: Invalid number format")
                    continue
                
                bits = int(input("Enter number of bits (default 8): ") or "8")
                from signed_representations import show_number_representations
                show_number_representations(value, bits)
            elif choice == "1":
                value = float(input("Enter decimal number: "))
                show_decimal_to_binary_steps(value)
                show_ieee754_visualization(value)
                show_multi_base_layout(value)
            elif choice == "2":
                value = input("Enter binary number: ")
                result = show_binary_to_decimal_steps(value)
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
                
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
            continue
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main() 