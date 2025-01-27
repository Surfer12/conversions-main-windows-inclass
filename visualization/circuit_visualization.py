# =========================================
# File: circuit_visualization.py
# Description:
#   Circuit visualization components for binary operations
# =========================================

from typing import List, Tuple
from core.number_conversion import Colors

def show_half_adder(a: int, b: int) -> None:
    """Visualize a half adder circuit with given inputs."""
    sum_bit = a ^ b  # XOR
    carry = a & b    # AND
    
    print("\n=== Half Adder Circuit ===")
    print("Inputs:")
    print(f"A = {a}")
    print(f"B = {b}")
    
    print("\nCircuit Diagram:")
    print("   A ─┬─[XOR]─── Sum")
    print("      │")
    print("   B ─┴─[AND]─── Carry")
    
    print("\nResults:")
    print(f"Sum:   {sum_bit}")
    print(f"Carry: {carry}")

def show_full_adder(a: int, b: int, c_in: int) -> None:
    """Visualize a full adder circuit with given inputs."""
    # First half adder
    sum1 = a ^ b
    carry1 = a & b
    
    # Second half adder
    sum_out = sum1 ^ c_in
    carry2 = sum1 & c_in
    
    # OR gate for final carry
    carry_out = carry1 | carry2
    
    print("\n=== Full Adder Circuit ===")
    print("Inputs:")
    print(f"A:      {a}")
    print(f"B:      {b}")
    print(f"Carry_in: {c_in}")
    
    print("\nCircuit Diagram:")
    print("   A ─┬─[XOR]─┬─[XOR]─── Sum")
    print("      │       │")
    print("   B ─┴─[AND]─┤")
    print("              │")
    print("   Cin ──────[AND]─[OR]── Carry_out")
    
    print("\nResults:")
    print(f"Sum:        {sum_out}")
    print(f"Carry_out:  {carry_out}")

def show_ripple_carry_adder(a: str, b: str) -> None:
    """Visualize a ripple carry adder for two binary numbers."""
    # Ensure equal length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    print("\n=== Ripple Carry Adder ===")
    print(f"A: {a}")
    print(f"B: {b}")
    
    # Process each bit
    result = ""
    carry = 0
    print("\nBit-by-bit addition:")
    
    for i in range(max_len-1, -1, -1):
        bit_a = int(a[i])
        bit_b = int(b[i])
        
        # Show full adder for this position
        print(f"\nPosition {max_len-i-1} Full Adder:")
        print(f"A[{i}] = {bit_a}")
        print(f"B[{i}] = {bit_b}")
        print(f"Carry_in = {carry}")
        
        # Calculate results
        current_sum = bit_a ^ bit_b ^ carry
        carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b))
        
        result = str(current_sum) + result
        print(f"Sum = {current_sum}")
        print(f"Carry_out = {carry}")
    
    if carry:
        result = "1" + result
    
    print("\nFinal Result:")
    print(result)

def show_circuit_menu() -> None:
    """Display menu for circuit visualization options."""
    while True:
        print("\n=== Circuit Visualization Menu ===")
        print("1. Half Adder")
        print("2. Full Adder")
        print("3. Ripple Carry Adder")
        print("4. Return to Main Menu")
        
        choice = input("\nEnter choice (1-4): ")
        
        if choice == "1":
            a = int(input("Enter first bit (0/1): "))
            b = int(input("Enter second bit (0/1): "))
            if a not in (0, 1) or b not in (0, 1):
                print("Error: Bits must be 0 or 1")
                continue
            show_half_adder(a, b)
        elif choice == "2":
            a = int(input("Enter first bit (0/1): "))
            b = int(input("Enter second bit (0/1): "))
            c = int(input("Enter carry in (0/1): "))
            if a not in (0, 1) or b not in (0, 1) or c not in (0, 1):
                print("Error: Bits must be 0 or 1")
                continue
            show_full_adder(a, b, c)
        elif choice == "3":
            a = input("Enter first binary number: ")
            b = input("Enter second binary number: ")
            if not all(bit in '01' for bit in a + b):
                print("Error: Invalid binary number")
                continue
            show_ripple_carry_adder(a, b)
        elif choice == "4":
            break
        
        input("\nPress Enter to continue...") 