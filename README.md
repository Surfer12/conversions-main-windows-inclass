# Binary Number System Educational Tool (BNSET)

## Project Description

BNSET is a comprehensive educational tool designed to help users understand binary number systems, conversions, and digital circuit concepts. It provides an interactive environment for learning and visualizing various number system representations, with support for arbitrary-precision binary conversions.

### Key Features

1. **Number System Conversions**
   - Decimal to Binary (configurable bit width: 8, 16, 32, 64, etc.)
   - Binary to Decimal
   - Support for fractional numbers
   - Two's complement representation for negative numbers

2. **IEEE-754 Floating Point**
   - Single precision (32-bit) visualization
   - Detailed breakdown of sign, exponent, and mantissa
   - Step-by-step conversion process

3. **Multi-Base Representations**
   - Binary (Base-2)
   - Octal (Base-8)
   - Decimal (Base-10)
   - Hexadecimal (Base-16)
   - Base-32

4. **Visualization Features**
   - Color-coded binary grouping
   - Circuit visualization for binary operations
   - Bit pattern grouping for readability
   - Range validation for different bit widths

5. **Educational Components**
   - Interactive learning modules
   - Step-by-step conversion explanations
   - Circuit-level understanding of binary operations

## Educational Components

BNSET includes a variety of educational features designed to enhance learning and understanding of binary number systems and digital circuits:

- **Interactive Learning Modules**: Engage with interactive tutorials that guide you through binary conversions and arithmetic operations.
- **Step-by-Step Explanations**: Detailed walkthroughs of conversion processes, including binary addition, subtraction, and two's complement.
- **Practice Problems**: Test your knowledge with practice problems and quizzes designed to reinforce learning.
- **Concept Maps**: Visualize the relationships between different number systems and their conversions.
- **Skill Assessments**: Evaluate your understanding with skill assessments and receive feedback on areas for improvement.

## Circuit Visualization Features

BNSET provides tools for visualizing digital circuits and understanding their operations:

- **Circuit Diagrams**: View detailed diagrams of binary adders, including Ripple Carry Adders and Full Adders.
- **Binary Operation Animations**: Watch animations that demonstrate how binary operations are performed at the circuit level.
- **Bit Pattern Grouping**: Visualize how bits are grouped and processed in digital circuits.
- **Color-Coded Representations**: Use color coding to differentiate between different parts of a circuit and understand their functions.
- **Interactive Circuit Simulations**: Experiment with circuit simulations to see how changes in input affect the output.

## Solution Endpoints

### 1. Number Conversion Module (`core/number_conversion.py`)

```python
def decimal_to_binary_float(decimal_value: float, int_bits: int = 64, frac_bits: int = 4) -> str:
    """Convert decimal to binary with configurable precision."""
    # Supports arbitrary bit width
    # Handles negative numbers via two's complement
    # Returns: Binary string with optional fractional part
```

```python
def binary_to_decimal_float(binary_str: str) -> float:
    """Convert binary to decimal, supporting fractional parts."""
    # Handles both integer and fractional binary numbers
    # Returns: Decimal float value
```

```python
def to_ieee754(value: float) -> dict:
    """Convert float to IEEE-754 single precision format."""
    # Returns: Dictionary containing:
    # - sign bit
    # - exponent (raw and biased)
    # - mantissa
    # - component values
```

### 2. Main Interface (`main.py`)

```python
def show_decimal_to_binary_steps(value: float, int_bits: int = 64) -> None:
    """Interactive decimal to binary conversion with visualization."""
    # Shows valid ranges for bit width
    # Displays step-by-step conversion process
```

```python
def show_ieee754_visualization(value: float) -> None:
    """Detailed IEEE-754 format breakdown."""
    # Visual representation of IEEE-754 components
    # Component-wise explanation
```

```python
def show_multi_base_layout(value: float) -> None:
    """Multi-base representation with formatting."""
    # Displays number in multiple bases
    # Color-coded visualization
```

## Usage Examples

1. **Basic Decimal to Binary Conversion**
   ```python
   # Convert decimal to 16-bit binary
   value = 1234
   bit_size = 16
   binary = show_decimal_to_binary_steps(value, bit_size)
   ```

2. **IEEE-754 Floating Point Analysis**
   ```python
   # Analyze float in IEEE-754 format
   value = 123.456
   show_ieee754_visualization(value)
   ```

3. **Multi-Base Visualization**
   ```python
   # View number in multiple bases
   value = 42
   show_multi_base_layout(value)
   ```

## Valid Ranges

- 8-bit:  [-128, 127]
- 16-bit: [-32,768, 32,767]
- 32-bit: [-2,147,483,648, 2,147,483,647]
- 64-bit: [-9,223,372,036,854,775,808, 9,223,372,036,854,775,807]

## Dependencies

- Python 3.8+
- No external dependencies required

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/binary-number-system-tool.git
   cd binary-number-system-tool
   ```

2. Run the tool:
   ```bash
   python main.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest features.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 