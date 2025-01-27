import unittest
import io
import sys
from contextlib import contextmanager
from ..visualization.circuit_visualization import (
    show_half_adder,
    show_full_adder,
    show_ripple_carry_adder
)

@contextmanager
def capture_output():
    """Capture stdout for testing."""
    new_out = io.StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out

class TestCircuitVisualization(unittest.TestCase):
    """Test suite for circuit visualization module."""
    
    def test_half_adder(self):
        """Test half adder visualization."""
        test_cases = [
            (0, 0, 0, 0),  # (a, b, expected_sum, expected_carry)
            (0, 1, 1, 0),
            (1, 0, 1, 0),
            (1, 1, 0, 1),
        ]
        
        for a, b, expected_sum, expected_carry in test_cases:
            with self.subTest(a=a, b=b):
                with capture_output() as output:
                    show_half_adder(a, b)
                    output_text = output.getvalue()
                    
                    # Check if output contains correct results
                    self.assertIn(f"Sum:   {expected_sum}", output_text)
                    self.assertIn(f"Carry: {expected_carry}", output_text)
                    
                    # Check if circuit diagram is present
                    self.assertIn("Circuit Diagram:", output_text)
                    self.assertIn("XOR", output_text)
                    self.assertIn("AND", output_text)
    
    def test_full_adder(self):
        """Test full adder visualization."""
        test_cases = [
            (0, 0, 0, 0, 0),  # (a, b, c_in, expected_sum, expected_carry)
            (0, 0, 1, 1, 0),
            (0, 1, 0, 1, 0),
            (0, 1, 1, 0, 1),
            (1, 0, 0, 1, 0),
            (1, 0, 1, 0, 1),
            (1, 1, 0, 0, 1),
            (1, 1, 1, 1, 1),
        ]
        
        for a, b, c_in, expected_sum, expected_carry in test_cases:
            with self.subTest(a=a, b=b, c_in=c_in):
                with capture_output() as output:
                    show_full_adder(a, b, c_in)
                    output_text = output.getvalue()
                    
                    # Check if output contains correct results
                    self.assertIn(f"Sum:        {expected_sum}", output_text)
                    self.assertIn(f"Carry_out:  {expected_carry}", output_text)
                    
                    # Check if circuit diagram is present
                    self.assertIn("Circuit Diagram:", output_text)
                    self.assertIn("XOR", output_text)
                    self.assertIn("AND", output_text)
                    self.assertIn("OR", output_text)
    
    def test_ripple_carry_adder(self):
        """Test ripple carry adder visualization."""
        test_cases = [
            ("0101", "0011", "1000"),  # 5 + 3 = 8
            ("1111", "0001", "10000"), # 15 + 1 = 16
            ("1010", "0101", "1111"),  # 10 + 5 = 15
        ]
        
        for a, b, expected_sum in test_cases:
            with self.subTest(a=a, b=b):
                with capture_output() as output:
                    show_ripple_carry_adder(a, b)
                    output_text = output.getvalue()
                    
                    # Check if output contains input numbers
                    self.assertIn(f"A: {a}", output_text)
                    self.assertIn(f"B: {b}", output_text)
                    
                    # Check if final result is present
                    self.assertIn("Final Result:", output_text)
                    self.assertIn(expected_sum, output_text.replace(" ", ""))
                    
                    # Check if bit-by-bit addition is shown
                    self.assertIn("Bit-by-bit addition", output_text)
                    self.assertIn("Full Adder", output_text)

def run_tests():
    """Run all tests with detailed output."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCircuitVisualization)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    run_tests() 