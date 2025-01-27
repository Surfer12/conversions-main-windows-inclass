import unittest
import sys
import io
from contextlib import redirect_stdout

# Import the functions to test
from number_conversion_interactive import (
    decimal_to_binary_float,
    binary_to_decimal_float,
    to_ieee754,
    to_base32,
    perform_binary_arithmetic,
    show_decimal_to_binary_steps,
    show_binary_to_decimal_steps
)

class TestNumberConversion(unittest.TestCase):
    def test_decimal_to_binary(self):
        # Test positive integers
        self.assertEqual(decimal_to_binary_float(1), '00000000000000000000000000000001')
        self.assertEqual(decimal_to_binary_float(10), '00000000000000000000000000001010')
        
        # Test negative integers
        self.assertTrue(decimal_to_binary_float(-5).startswith('1'))
        
        # Test fractional numbers
        self.assertTrue('.' in decimal_to_binary_float(1.5))
        
    def test_binary_to_decimal(self):
        # Test positive binary conversions
        self.assertEqual(binary_to_decimal_float('1'), 1.0)
        self.assertEqual(binary_to_decimal_float('1010'), 10.0)
        
        # Test binary with fractional part
        self.assertAlmostEqual(binary_to_decimal_float('1.1'), 1.5)
        
    def test_ieee754(self):
        # Test IEEE-754 conversion for various numbers
        ieee_1 = to_ieee754(1.0)
        self.assertEqual(ieee_1['sign'], '0')
        self.assertEqual(ieee_1['exponent'], '01111111')
        
        ieee_neg = to_ieee754(-1.0)
        self.assertEqual(ieee_neg['sign'], '1')
        
    def test_base32_conversion(self):
        # Test base32 conversion
        self.assertEqual(to_base32(1), 'B')
        self.assertEqual(to_base32(10), 'K')
        
    def test_binary_arithmetic(self):
        # Test addition
        result, _ = perform_binary_arithmetic('1010', '0101', 'add')
        self.assertEqual(result, '1111')
        
        # Test subtraction
        result, _ = perform_binary_arithmetic('1010', '0101', 'subtract')
        self.assertEqual(result, '0101')
        
        # Test multiplication
        result, _ = perform_binary_arithmetic('1010', '0011', 'multiply')
        self.assertEqual(result, '00011110')
        
    def test_conversion_steps(self):
        # Capture stdout to check step-by-step explanations
        def run_conversion_test(conversion_func, input_value):
            f = io.StringIO()
            with redirect_stdout(f):
                conversion_func(input_value)
            output = f.getvalue()
            return output
        
        # Test decimal to binary steps
        decimal_steps = run_conversion_test(show_decimal_to_binary_steps, 10)
        self.assertIn('Decimal to Binary Conversion Steps', decimal_steps)
        
        # Test binary to decimal steps
        binary_steps = run_conversion_test(show_binary_to_decimal_steps, '1010')
        self.assertIn('Binary to Decimal Conversion Steps', binary_steps)

def main():
    unittest.main()

if __name__ == '__main__':
    main() 