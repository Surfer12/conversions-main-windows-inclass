# =========================================
# File: circuit_visualization.py
# Description:
#   Circuit-level visualization of binary operations
#   showing gates and digital logic implementation.
# =========================================

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

def show_half_adder(a: int, b: int) -> None:
    """Visualize a half adder circuit with inputs and outputs."""
    sum_bit = a ^ b  # XOR
    carry = a & b    # AND
    
    print("\n=== Half Adder Circuit ===")
    print(f"Inputs:  A = {a}, B = {b}")
    print("\nCircuit Diagram:")
    print("     A─────┬─────►XOR──────►Sum")
    print("           │      ▲")
    print("           │      │")
    print("     B─────┼──────┘")
    print("           │")
    print("           └─────►AND──────►Carry")
    print("\nGate Operations:")
    print(f"XOR Gate: {a} ⊕ {b} = {sum_bit}")
    print(f"AND Gate: {a} & {b} = {carry}")
    print("\nOutputs:")
    print(f"Sum:   {sum_bit}")
    print(f"Carry: {carry}")

def show_full_adder(a: int, b: int, c_in: int) -> None:
    """Visualize a full adder circuit with inputs and outputs."""
    # First half adder
    sum1 = a ^ b
    carry1 = a & b
    
    # Second half adder
    sum_out = sum1 ^ c_in
    carry2 = sum1 & c_in
    
    # OR gate for final carry
    carry_out = carry1 | carry2
    
    print("\n=== Full Adder Circuit ===")
    print(f"Inputs: A = {a}, B = {b}, Carry_in = {c_in}")
    print("\nCircuit Diagram:")
    print("     A─────┬─────►XOR─────┬─────►XOR──────►Sum")
    print("           │      ▲       │      ▲")
    print("           │      │       │      │")
    print("     B─────┼──────┘       │      │")
    print("           │              │      │")
    print("           └─────►AND─────┼──────┘")
    print("                  │       │")
    print("                  │       │")
    print("   Cin───────────┼───────┘")
    print("                  │")
    print("                  └─────►OR───────►Carry")
    print("\nGate Operations:")
    print("First Half Adder:")
    print(f"XOR1: {a} ⊕ {b} = {sum1}")
    print(f"AND1: {a} & {b} = {carry1}")
    print("\nSecond Half Adder:")
    print(f"XOR2: {sum1} ⊕ {c_in} = {sum_out}")
    print(f"AND2: {sum1} & {c_in} = {carry2}")
    print("\nFinal Carry:")
    print(f"OR: {carry1} | {carry2} = {carry_out}")
    print("\nOutputs:")
    print(f"Sum:        {sum_out}")
    print(f"Carry_out:  {carry_out}")

def show_ripple_carry_adder(a: str, b: str) -> None:
    """Visualize a ripple carry adder for multi-bit addition."""
    # Ensure equal length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    print(f"\n=== {max_len}-bit Ripple Carry Adder ===")
    print("Input binary numbers:")
    print(f"A: {a}")
    print(f"B: {b}")
    
    # Process each bit position
    carry = 0
    result = ""
    carries = []
    
    print("\nBit-by-bit addition with full adders:")
    for i in range(max_len-1, -1, -1):
        bit_a = int(a[i])
        bit_b = int(b[i])
        
        # Calculate full adder outputs
        sum1 = bit_a ^ bit_b
        carry1 = bit_a & bit_b
        sum_out = sum1 ^ carry
        carry2 = sum1 & carry
        carry_next = carry1 | carry2
        
        print(f"\nBit position {max_len-1-i}:")
        print(f"Full Adder {i}:")
        print(f"  Inputs:  A={bit_a}, B={bit_b}, Cin={carry}")
        print(f"  Outputs: Sum={sum_out}, Cout={carry_next}")
        
        result = str(sum_out) + result
        carries.append(carry)
        carry = carry_next
    
    if carry:
        result = '1' + result
        carries.append(carry)
    
    print("\nFinal Result:")
    print(f"  {''.join(str(c) for c in carries[:-1])}  (Carries)")
    print(f"  {a}")
    print(f"+ {b}")
    print(f"  {'-' * max_len}")
    print(f"  {result}")

def show_circuit_menu() -> None:
    """Show menu for circuit-level visualizations."""
    while True:
        print("\n=== Circuit Visualization Menu ===")
        print("1. Half Adder")
        print("2. Full Adder")
        print("3. Ripple Carry Adder")
        print("4. Return to Main Menu")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            print("\nEnter two 1-bit numbers (0 or 1):")
            try:
                a = int(input("A: "))
                b = int(input("B: "))
                if a not in (0, 1) or b not in (0, 1):
                    print("Inputs must be 0 or 1")
                    continue
                show_half_adder(a, b)
            except ValueError:
                print("Invalid input")
                
        elif choice == "2":
            print("\nEnter three 1-bit numbers (0 or 1):")
            try:
                a = int(input("A: "))
                b = int(input("B: "))
                c = int(input("Carry in: "))
                if a not in (0, 1) or b not in (0, 1) or c not in (0, 1):
                    print("Inputs must be 0 or 1")
                    continue
                show_full_adder(a, b, c)
            except ValueError:
                print("Invalid input")
                
        elif choice == "3":
            print("\nEnter two binary numbers:")
            a = input("First number (e.g., 1101): ").strip()
            b = input("Second number (e.g., 1001): ").strip()
            if not all(bit in '01' for bit in a + b):
                print("Invalid binary numbers")
                continue
            show_ripple_carry_adder(a, b)
            
        elif choice == "4":
            break
        
        else:
            print("Invalid choice") 