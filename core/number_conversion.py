# =========================================
# File: number_conversion.py
# Description:
#   Core functionality for number system conversions
# =========================================

import struct
from typing import Tuple, List, Dict

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

def decimal_to_binary_float(decimal_value: float, int_bits: int = 64, frac_bits: int = 4) -> str:
    """Convert decimal (including fractional) to binary string.
    
    Args:
        decimal_value: The decimal number to convert
        int_bits: Number of bits for integer part (default 64)
        frac_bits: Number of bits for fractional part (default 4)
        
    Returns:
        Binary string representation
        
    Raises:
        ValueError: If the number is too large for the specified bit size
    """
    int_part = int(decimal_value)
    frac_part = abs(decimal_value - int_part)
    
    # Validate bit size
    max_positive = (1 << (int_bits - 1)) - 1
    min_negative = -(1 << (int_bits - 1))
    
    if int_part > max_positive or int_part < min_negative:
        raise ValueError(f"Number too large for {int_bits}-bit representation. Range: [{min_negative}, {max_positive}]")
    
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

def binary_to_decimal(binary_str: str) -> int:
    """Convert binary string to decimal, handling unsigned numbers."""
    return int(binary_str, 2)

def binary_to_decimal_float(binary_str: str) -> float:
    """Convert binary string to decimal, handling fractional parts."""
    if '.' not in binary_str:
        return float(binary_to_decimal(binary_str))
        
    int_part, frac_part = binary_str.split('.')
    
    # Convert integer part
    int_value = binary_to_decimal(int_part) if int_part else 0
    
    # Convert fractional part
    frac_value = 0.0
    for i, bit in enumerate(frac_part, 1):
        if bit == '1':
            frac_value += 2 ** -i
            
    return float(int_value) + frac_value

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

def group_bits(binary: str, group_size: int = 4) -> str:
    """Group binary digits for easier reading."""
    if '.' in binary:
        int_part, frac_part = binary.split('.')
        grouped_int = ' '.join(int_part[i:i+group_size] for i in range(0, len(int_part), group_size)).strip()
        grouped_frac = ' '.join(frac_part[i:i+group_size] for i in range(0, len(frac_part), group_size)).strip()
        return f"{grouped_int}.{grouped_frac}"
    return ' '.join(binary[i:i+group_size] for i in range(0, len(binary), group_size)).strip()

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

BASE32_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

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