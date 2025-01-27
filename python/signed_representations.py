# =========================================
# File: signed_representations.py
# Description:
#   Visualization of different signed number representations
#   and overflow detection.
# =========================================

from typing import Tuple

def show_number_representations(value: int, bits: int = 8) -> None:
    """Show different signed number representations."""
    print(f"\n=== Signed Number Representations ({bits}-bit) ===")
    print(f"Decimal value: {value}")
    
    # Calculate ranges
    max_unsigned = (1 << bits) - 1
    max_signed = (1 << (bits - 1)) - 1
    min_signed = -(1 << (bits - 1))
    
    # Check for overflow
    if abs(value) > max_signed:
        print(f"\nWarning: Value {value} exceeds {bits}-bit signed range [{min_signed}, {max_signed}]")
        print("Results below show wrapped/modulo behavior")
    
    # Unsigned representation (for comparison)
    unsigned_pattern = format(value & ((1 << bits) - 1), f'0{bits}b')
    print(f"\nUnsigned binary:  {unsigned_pattern}")
    print(f"Unsigned decimal: {int(unsigned_pattern, 2)}")
    
    # Sign-magnitude representation
    sign_bit = '1' if value < 0 else '0'
    magnitude = format(abs(value) & ((1 << (bits-1)) - 1), f'0{bits-1}b')
    sign_magnitude = sign_bit + magnitude
    print(f"\nSign-magnitude:")
    print(f"Binary:  {sign_bit} {magnitude}")
    print(f"         │ └─ Magnitude bits")
    print(f"         └─── Sign bit (0=positive, 1=negative)")
    
    # One's complement
    if value < 0:
        ones_complement = ''.join('1' if b == '0' else '0' for b in format(abs(value), f'0{bits}b'))
    else:
        ones_complement = format(value, f'0{bits}b')
    print(f"\nOne's complement:")
    print(f"Binary:  {ones_complement}")
    if value < 0:
        print("(Inverted all bits of positive number)")
    
    # Two's complement
    if value < 0:
        twos_complement = format((1 << bits) + value, f'0{bits}b')
    else:
        twos_complement = format(value, f'0{bits}b')
    print(f"\nTwo's complement:")
    print(f"Binary:  {twos_complement}")
    if value < 0:
        print("(One's complement + 1)")
    
    # Show ranges
    print(f"\nValid ranges for {bits}-bit numbers:")
    print(f"Unsigned:        0 to {max_unsigned}")
    print(f"Sign-magnitude: -{max_signed} to {max_signed}")
    print(f"One's complement: -{max_signed} to {max_signed}")
    print(f"Two's complement: {min_signed} to {max_signed}")

def check_overflow(a: int, b: int, result: int, bits: int = 8, operation: str = 'add') -> Tuple[bool, str]:
    """Check for overflow in arithmetic operations."""
    max_val = (1 << (bits - 1)) - 1
    min_val = -(1 << (bits - 1))
    
    if operation == 'add':
        # Overflow in addition occurs when:
        # 1. Both numbers are positive but sum exceeds max_val
        # 2. Both numbers are negative but sum is less than min_val
        if (a > 0 and b > 0 and result > max_val) or \
           (a < 0 and b < 0 and result < min_val):
            return True, f"Result {result} exceeds {bits}-bit signed range [{min_val}, {max_val}]"
    elif operation == 'subtract':
        # Overflow in subtraction occurs when:
        # 1. First number is positive, second is negative, and result exceeds max_val
        # 2. First number is negative, second is positive, and result is less than min_val
        if (a > 0 and b < 0 and result > max_val) or \
           (a < 0 and b > 0 and result < min_val):
            return True, f"Result {result} exceeds {bits}-bit signed range [{min_val}, {max_val}]"
    elif operation == 'multiply':
        # For multiplication, we need to check:
        # 1. If result exceeds the bit width (simple check)
        # 2. For signed numbers, check sign rules
        if result < min_val or result > max_val:
            msg = f"Multiplication result {result} exceeds {bits}-bit range [{min_val}, {max_val}]"
            # Add sign analysis
            if (a < 0 and b < 0 and result < 0) or \
               (a > 0 and b > 0 and result < 0) or \
               (a * b > 0 and result < 0):
                msg += "\nSign error: incorrect sign in result"
            return True, msg
    elif operation == 'divide':
        # For division, we need to check:
        # 1. Division by zero (should be caught earlier)
        # 2. Special case: MIN_INT / -1 (results in overflow due to two's complement)
        if b == 0:
            return True, "Division by zero"
        elif a == min_val and b == -1:
            return True, f"Special case overflow: {min_val} / -1 exceeds {bits}-bit range"
        elif result < min_val or result > max_val:
            return True, f"Division result {result} exceeds {bits}-bit range [{min_val}, {max_val}]"
    
    return False, ""

def show_carry_chain(a: str, b: str, operation: str = 'add') -> None:
    """Visualize carry/borrow chain in binary arithmetic."""
    print("\nCarry Chain Visualization:")
    print("  " + " ".join(a))  # First number
    print(f"{'+ ' if operation == 'add' else '- '}" + " ".join(b))  # Second number
    print("  " + "-" * (len(a) * 2 - 1))  # Separator line
    
    carries = []
    result = []
    carry = 0
    
    if operation == 'add':
        # Process addition from right to left
        for i in range(len(a)-1, -1, -1):
            bit_sum = int(a[i]) + int(b[i]) + carry
            carries.append(bit_sum // 2)
            result.append(str(bit_sum % 2))
            carry = bit_sum // 2
    else:
        # Process subtraction (using two's complement)
        b_complement = ''.join('1' if bit == '0' else '0' for bit in b)
        carry = 1
        for i in range(len(b_complement)-1, -1, -1):
            bit_sum = int(b_complement[i]) + carry
            b_complement = b_complement[:i] + str(bit_sum % 2) + b_complement[i+1:]
            carry = bit_sum // 2
        
        # Now add a and b_complement
        carry = 0
        for i in range(len(a)-1, -1, -1):
            bit_sum = int(a[i]) + int(b_complement[i]) + carry
            carries.append(bit_sum // 2)
            result.append(str(bit_sum % 2))
            carry = bit_sum // 2
    
    # Show carries
    carries.reverse()
    result.reverse()
    if any(carries):
        print("  " + " ".join(str(c) for c in carries) + "  ← Carries")
    print("  " + " ".join(result) + "  ← Result")

def show_overflow_cases(bits: int = 4) -> None:
    """Demonstrate common overflow scenarios with visual explanations."""
    print(f"\n=== Overflow Demonstration ({bits}-bit numbers) ===")
    
    # Calculate ranges
    max_val = (1 << (bits - 1)) - 1
    min_val = -(1 << (bits - 1))
    
    print(f"\nValid ranges for {bits}-bit signed numbers:")
    print(f"Maximum positive: {max_val:4} = {format(max_val, f'0{bits}b')}")
    print(f"Minimum negative: {min_val:4} = {format((1 << bits) + min_val, f'0{bits}b')}")
    
    # Case 1: Maximum positive + 1
    print("\n1. Maximum Positive + 1 Overflow:")
    a, b = max_val, 1
    result = a + b
    print(f"   {a:4} + {b:4} = {result:4}")
    print(f"   {format(a, f'0{bits}b')} (max positive)")
    print(f" + {format(b, f'0{bits}b')}")
    print(f"   {'-' * bits}")
    result_bin = format(result & ((1 << bits) - 1), f'0{bits}b')
    print(f"   {result_bin} (wraps to negative!)")
    
    # Case 2: Minimum negative - 1
    print("\n2. Minimum Negative - 1 Overflow:")
    a, b = min_val, -1
    result = a + b
    print(f"   {a:4} + {b:4} = {result:4}")
    print(f"   {format((1 << bits) + a, f'0{bits}b')} (min negative)")
    print(f" + {format((1 << bits) + b, f'0{bits}b')} (-1 in two's complement)")
    print(f"   {'-' * bits}")
    result_bin = format(result & ((1 << bits) - 1), f'0{bits}b')
    print(f"   {result_bin} (wraps to positive!)")
    
    # Case 3: Positive + Positive → Negative
    print("\n3. Positive + Positive → Negative Overflow:")
    a = max_val - 1
    b = 3
    result = a + b
    print(f"   {a:4} + {b:4} = {result:4}")
    print(f"   {format(a, f'0{bits}b')}")
    print(f" + {format(b, f'0{bits}b')}")
    print(f"   {'-' * bits}")
    result_bin = format(result & ((1 << bits) - 1), f'0{bits}b')
    print(f"   {result_bin} (result appears negative)")
    
    # Case 4: Negative + Negative → Positive
    print("\n4. Negative + Negative → Positive Overflow:")
    a = min_val + 1
    b = -3
    result = a + b
    print(f"   {a:4} + {b:4} = {result:4}")
    print(f"   {format((1 << bits) + a, f'0{bits}b')}")
    print(f" + {format((1 << bits) + b, f'0{bits}b')}")
    print(f"   {'-' * bits}")
    result_bin = format(result & ((1 << bits) - 1), f'0{bits}b')
    print(f"   {result_bin} (result appears positive)")
    
    # Case 5: Multiplication Overflow
    print("\n5. Multiplication Overflow:")
    a = max_val // 2
    b = 3
    result = a * b
    print(f"   {a:4} × {b:4} = {result:4}")
    print(f"   {format(a, f'0{bits}b')} × {format(b, f'0{bits}b')}")
    print(f"   {'-' * bits}")
    result_bin = format(result & ((1 << bits) - 1), f'0{bits}b')
    print(f"   {result_bin} (truncated result)")
    
    # Case 6: Special Division Overflow (MIN_INT / -1)
    print("\n6. Special Division Case (MIN_INT ÷ -1):")
    a = min_val
    b = -1
    try:
        result = a // b
        print(f"   {a:4} ÷ {b:4} = {result:4}")
        print(f"   {format((1 << bits) + a, f'0{bits}b')} ÷ {format((1 << bits) + b, f'0{bits}b')}")
        print("   This causes overflow because the positive result exceeds the maximum positive value")
    except ZeroDivisionError:
        print("   Division by zero") 