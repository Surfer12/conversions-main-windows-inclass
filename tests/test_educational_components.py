import unittest
from unittest.mock import patch
import io
import sys
from pathlib import Path

# Add the parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from educational.educational_components import (
    show_quiz,
    show_interactive_simulation,
    show_detailed_explanation,
    show_concept_map,
    show_learning_path
)

class TestEducationalComponents(unittest.TestCase):
    """Test cases for educational components."""
    
    def setUp(self):
        """Set up test cases."""
        self.held_output = io.StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        """Clean up after tests."""
        sys.stdout = self.original_stdout
        self.held_output.close()
    
    @patch('builtins.input', side_effect=['1', '1'])
    def test_quiz_binary_basics(self, mock_input):
        """Test the quiz functionality with binary basics topic."""
        show_quiz()
        output = self.held_output.getvalue()
        
        # Check if quiz header is present
        self.assertIn("Binary Number System Quiz", output)
        # Check if binary basics questions are shown
        self.assertIn("What is the decimal equivalent of binary 1010?", output)
    
    @patch('builtins.input', side_effect=['1', '1010', '1011'])
    def test_interactive_simulation_binary_addition(self, mock_input):
        """Test the binary addition simulation."""
        show_interactive_simulation()
        output = self.held_output.getvalue()
        
        # Check if simulation header is present
        self.assertIn("Binary Addition Simulator", output)
        # Check if step-by-step addition is shown
        self.assertIn("Step-by-step Addition:", output)
    
    @patch('builtins.input', side_effect=['1'])
    def test_detailed_explanation_number_systems(self, mock_input):
        """Test the detailed explanation functionality."""
        show_detailed_explanation()
        output = self.held_output.getvalue()
        
        # Check if explanation header is present
        self.assertIn("Number Systems and Base Conversion", output)
        # Check if content is shown
        self.assertIn("Decimal (Base-10):", output)
        self.assertIn("Binary (Base-2):", output)
    
    @patch('builtins.input', side_effect=['binary'])
    def test_concept_map(self, mock_input):
        """Test the concept map visualization."""
        show_concept_map()
        output = self.held_output.getvalue()
        
        # Check if concept map is displayed
        self.assertIn("Binary Number Systems", output)
        self.assertIn("Number Representation", output)
    
    @patch('builtins.input', side_effect=['beginner'])
    def test_learning_path(self, mock_input):
        """Test the learning path functionality."""
        show_learning_path()
        output = self.held_output.getvalue()
        
        # Check if learning path is shown
        self.assertIn("Learning Path", output)
        self.assertIn("Current Topics:", output)
        self.assertIn("Next Topics:", output)

if __name__ == '__main__':
    unittest.main() 