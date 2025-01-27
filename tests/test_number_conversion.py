import unittest
from core.number_conversion import (
    decimal_to_binary_float,
    binary_to_decimal_float,
    to_base32,
    group_bits,
    color_binary_groups,
    parse_number
)

class TestNumberConversion(unittest.TestCase):
    """Test suite for number conversion utility."""
    
    def setUp(self):
        """Set up test environment."""
        self.maxDiff = None  # Show full diff for assertion errors

    def test_hex_to_decimal(self):
        """Test hexadecimal to decimal conversion."""
        test_cases = [
            ("0x1A", 26),
            ("0xFF", 255),
            ("0x100", 256),
            ("0x1A.8", 26.5),  # 8/16 = 0.5
            ("0xFF.4", 255.25),  # 4/16 = 0.25
            ("1A", 26),  # Without prefix
            ("FF", 255),  # Without prefix
            ("1A.8", 26.5),  # Without prefix, with fraction
        ]
        
        for hex_str, expected in test_cases:
            with self.subTest(hex=hex_str):
                # Remove 0x prefix if present
                hex_str = hex_str[2:] if hex_str.startswith('0x') else hex_str
                if '.' in hex_str:
                    int_part, frac_part = hex_str.split('.')
                    result = float.fromhex(f"0x{int_part}.{frac_part}")
                else:
                    result = float.fromhex(f"0x{hex_str}")
                self.assertEqual(result, expected)

    def test_decimal_to_binary(self):
        """Test decimal to binary conversion."""
        test_cases = [
            (42, "00000000000000000000000000101010"),
            (0, "00000000000000000000000000000000"),
            (-42, "11111111111111111111111111010110"),
            (255, "00000000000000000000000011111111"),
            (3.75, "00000000000000000000000000000011.1100"),
            (-3.75, "11111111111111111111111111111101.1100"),
            (26.5, "00000000000000000000000000011010.1000"),  # 0x1A.8
        ]
        
        for decimal, expected in test_cases:
            with self.subTest(decimal=decimal):
                result = decimal_to_binary_float(decimal)
                self.assertEqual(result, expected)
    
    def test_binary_to_decimal(self):
        """Test binary to decimal conversion."""
        test_cases = [
            ("00101010", 42),
            ("00000000", 0),
            ("11111111", 255),
            ("00000011.11", 3.75),
            ("1111111111111111", 65535),
            ("00011010.1000", 26.5),  # 0x1A.8
        ]
        
        for binary, expected in test_cases:
            with self.subTest(binary=binary):
                result = binary_to_decimal_float(binary)
                self.assertEqual(result, expected)
    
    def test_base32_conversion(self):
        """Test base32 conversion using standard alphabet (0-9, A-V).
        For values 0-9, uses decimal digits.
        For values 10-31, uses letters A-V.
        """
        test_cases = [
            (26, "Q"),      # 26 = 0x1A = 26 base 32
            (255, "7V"),    # 255 = 0xFF = 7*32 + 31 = "7V"
            (256, "80"),    # 256 = 0x100 = 8*32 + 0 = "80"
            (26.5, "Q.G"),  # 26.5 = 0x1A.8 = "Q.G"
            (42, "1A"),     # 42 = 1*32 + 10 = "1A"
            (1024, "100"),  # 1024 = 1*32^2 + 0*32 + 0 = "100"
            (3.75, "3.N"),  # 3.75 = 3 + 0.75 = "3.N"
        ]
        
        for decimal, expected in test_cases:
            with self.subTest(decimal=decimal):
                result = to_base32(decimal)
                self.assertEqual(result, expected)
    
    def test_number_parsing(self):
        """Test number parsing in different bases."""
        test_cases = [
            ("42", 10, 42),
            ("0b101010", 2, 42),
            ("0x2A", 16, 42),
            ("0o52", 8, 42),
            ("1A", 16, 26),  # Hex without prefix
            ("FF", 16, 255), # Hex without prefix
            ("1100", 2, 12), # Binary without prefix
        ]
        
        for number_str, base, expected in test_cases:
            with self.subTest(number=number_str, base=base):
                result = parse_number(number_str, base)
                self.assertEqual(result, expected)
    
    def test_bit_grouping(self):
        """Test binary digit grouping."""
        test_cases = [
            ("1010", 2, "10 10"),
            ("1111", 4, "1111"),
            ("101010", 3, "101 010"),
            ("1010.1010", 2, "10 10.10 10"),
            ("11010.1000", 4, "1101 0.1000"),  # 0x1A.8
        ]
        
        for binary, group_size, expected in test_cases:
            with self.subTest(binary=binary, group_size=group_size):
                result = group_bits(binary, group_size)
                self.assertEqual(result, expected)
    
    def test_color_grouping(self):
        """Test color-coded binary grouping."""
        # Note: This test only checks if the function runs without errors
        # since testing ANSI color codes in strings is complex
        test_cases = ["1010", "1111", "101010", "1010.1010"]
        
        for binary in test_cases:
            with self.subTest(binary=binary):
                result = color_binary_groups(binary)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), len(binary))
    
    def test_invalid_inputs(self):
        """Test handling of invalid inputs."""
        # Test invalid hex
        with self.assertRaises(ValueError):
            float.fromhex("0xGG")
        
        # Test invalid binary
        with self.assertRaises(ValueError):
            binary_to_decimal_float("00102")  # Invalid binary digit
        
        # Test invalid base32
        with self.assertRaises(ValueError):
            to_base32(-1)  # Negative numbers not supported
        
        # Test invalid number parsing
        with self.assertRaises(ValueError):
            parse_number("0xGG", 16)  # Invalid hex
        with self.assertRaises(ValueError):
            parse_number("0b102", 2)  # Invalid binary

if __name__ == '__main__':
    unittest.main() 