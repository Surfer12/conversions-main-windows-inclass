import unittest
from ..core.number_conversion import (
    decimal_to_binary_float,
    binary_to_decimal_float,
    to_base32,
    group_bits,
    color_binary_groups,
    parse_number,
    perform_binary_arithmetic
)
from ..visualization.circuit_visualization import (
    show_half_adder,
    show_full_adder,
    show_ripple_carry_adder
)
from ..core.signed_representations import check_overflow

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
    
    def test_binary_arithmetic(self):
        """Test binary arithmetic operations."""
        # Addition
        a, b = "101", "011"  # 5 + 3
        result, steps = perform_binary_arithmetic(a, b, 'add')
        self.assertEqual(int(result, 2), 8)
        self.assertIsInstance(steps, list)
        
        # Subtraction
        a, b = "1000", "0011"  # 8 - 3
        result, steps = perform_binary_arithmetic(a, b, 'subtract')
        self.assertEqual(int(result, 2), 5)
        self.assertIsInstance(steps, list)
        
        # Multiplication
        a, b = "101", "011"  # 5 * 3
        result, steps = perform_binary_arithmetic(a, b, 'multiply')
        self.assertEqual(int(result, 2), 15)
        self.assertIsInstance(steps, list)
        
        # Division
        a, b = "1111", "0011"  # 15 ÷ 3
        result, steps = perform_binary_arithmetic(a, b, 'divide')
        self.assertEqual(int(result, 2), 5)
        self.assertIsInstance(steps, list)
    
    def test_overflow_detection(self):
        """Test overflow detection in arithmetic operations."""
        # 4-bit overflow cases
        bits = 4
        max_val = (1 << (bits - 1)) - 1  # 7 for 4 bits
        min_val = -(1 << (bits - 1))     # -8 for 4 bits
        
        # Addition overflow
        has_overflow, _ = check_overflow(max_val, 1, max_val + 1, bits, 'add')
        self.assertTrue(has_overflow)
        
        # Subtraction overflow
        has_overflow, _ = check_overflow(min_val, 1, min_val - 1, bits, 'subtract')
        self.assertTrue(has_overflow)
        
        # Multiplication overflow
        has_overflow, _ = check_overflow(max_val, 2, max_val * 2, bits, 'multiply')
        self.assertTrue(has_overflow)
        
        # No overflow case
        has_overflow, _ = check_overflow(1, 1, 2, bits, 'add')
        self.assertFalse(has_overflow)
    
    def test_base32_conversion(self):
        """Test base32 conversion using standard alphabet (0-9, A-V)."""
        test_cases = [
            (26, "Q"),      # 0x1A
            (255, "7V"),    # 0xFF
            (256, "80"),    # 0x100
            (26.5, "Q.G"),  # 0x1A.8
            (42, "1A"),
            (1024, "U0"),
            (3.75, "3.N"),
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

def run_tests():
    """Run all tests with detailed output."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumberConversion)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    run_tests() 