# =========================================
# File: educational_components.py
# Description:
#   Educational visualizations and interactive
#   learning components for binary number systems.
# =========================================

import sys
from pathlib import Path

# Add the root directory to Python path
root_dir = Path(__file__).parent.parent
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

from typing import List, Tuple, Dict
from core.number_conversion import Colors

def show_concept_map(topic: str = "binary") -> None:
    """Display a concept map for binary number system topics."""
    topics = {
        "binary": {
            "title": "Binary Number Systems",
            "concepts": [
                ("Number Representation", ["Unsigned", "Signed (Two's Complement)", "Fixed-point", "Floating-point"]),
                ("Basic Operations", ["Addition", "Subtraction", "Multiplication", "Division"]),
                ("Digital Logic", ["Gates", "Adders", "Multiplexers"]),
                ("Applications", ["Memory Addressing", "Data Storage", "ALU Operations"])
            ]
        },
        "arithmetic": {
            "title": "Binary Arithmetic",
            "concepts": [
                ("Addition", ["Half Adder", "Full Adder", "Ripple Carry", "Carry Look-ahead"]),
                ("Subtraction", ["Two's Complement", "Borrow Chain", "Add Negative"]),
                ("Multiplication", ["Partial Products", "Booth's Algorithm", "Shift-and-Add"]),
                ("Division", ["Restoring", "Non-restoring", "SRT Division"])
            ]
        }
    }
    
    if topic not in topics:
        print(f"Topic '{topic}' not found. Available topics: {', '.join(topics.keys())}")
        return
    
    topic_data = topics[topic]
    
    # Display concept map
    print(f"\n=== {topic_data['title']} Concept Map ===\n")
    print("┌" + "─" * 60 + "┐")
    print(f"│{topic_data['title']:^60}│")
    print("└" + "─" * 60 + "┘")
    
    for concept, subtopics in topic_data["concepts"]:
        print(f"\n{Colors.BOLD}{concept}{Colors.ENDC}")
        print("├─" + "─" * 40)
        for subtopic in subtopics:
            print(f"│  • {subtopic}")

def show_learning_path(current_level: str = "beginner") -> None:
    """Display a recommended learning path based on current level."""
    levels = {
        "beginner": {
            "current_topics": [
                "Binary counting (0s and 1s)",
                "Basic number conversion (decimal ↔ binary)",
                "Simple addition (no carry)"
            ],
            "next_topics": [
                "Carry in addition",
                "Binary subtraction",
                "Fixed-width numbers"
            ],
            "prerequisites": []
        },
        "intermediate": {
            "current_topics": [
                "Two's complement representation",
                "Multiplication algorithms",
                "Basic circuit components"
            ],
            "next_topics": [
                "Division algorithms",
                "Floating-point representation",
                "ALU design concepts"
            ],
            "prerequisites": ["beginner"]
        },
        "advanced": {
            "current_topics": [
                "Optimized arithmetic circuits",
                "IEEE-754 implementation",
                "Error detection/correction"
            ],
            "next_topics": [
                "Custom number formats",
                "Hardware optimization",
                "Advanced ALU features"
            ],
            "prerequisites": ["beginner", "intermediate"]
        }
    }
    
    if current_level not in levels:
        print(f"Level '{current_level}' not found. Available levels: {', '.join(levels.keys())}")
        return
    
    level_data = levels[current_level]
    
    print(f"\n=== Learning Path ({current_level.title()} Level) ===\n")
    
    if level_data["prerequisites"]:
        print(f"{Colors.YELLOW}Prerequisites:{Colors.ENDC}")
        for prereq in level_data["prerequisites"]:
            print(f"• Complete {prereq.title()} level")
        print()
    
    print(f"{Colors.GREEN}Current Topics:{Colors.ENDC}")
    for topic in level_data["current_topics"]:
        print(f"• {topic}")
    
    print(f"\n{Colors.BLUE}Next Topics:{Colors.ENDC}")
    for topic in level_data["next_topics"]:
        print(f"• {topic}")

def show_practice_problem(topic: str = "addition", difficulty: str = "easy") -> None:
    """Generate and display a practice problem with solution steps."""
    problems = {
        "addition": {
            "easy": {
                "description": "Add two 4-bit binary numbers",
                "problem": ("1010", "0011"),  # 10 + 3
                "solution_steps": [
                    "1. Align numbers right-justified",
                    "2. Add bits column by column",
                    "3. Propagate carry when sum ≥ 2"
                ]
            },
            "medium": {
                "description": "Add two 8-bit numbers with multiple carries",
                "problem": ("11011011", "00110101"),  # 219 + 53
                "solution_steps": [
                    "1. Identify potential carry positions",
                    "2. Track carry chain propagation",
                    "3. Verify final carry out"
                ]
            }
        },
        "subtraction": {
            "easy": {
                "description": "Subtract using two's complement",
                "problem": ("1000", "0011"),  # 8 - 3
                "solution_steps": [
                    "1. Convert subtrahend to two's complement",
                    "2. Add the numbers",
                    "3. Check for borrow propagation"
                ]
            }
        }
    }
    
    if topic not in problems or difficulty not in problems[topic]:
        print(f"Problem not found for topic '{topic}' and difficulty '{difficulty}'")
        return
    
    problem_data = problems[topic][difficulty]
    
    print(f"\n=== Practice Problem ({difficulty.title()} {topic.title()}) ===\n")
    print(f"Task: {problem_data['description']}")
    
    if isinstance(problem_data["problem"], tuple):
        a, b = problem_data["problem"]
        print(f"\nProblem:")
        print(f"  {a}")
        print(f"  {b}")
    else:
        print(f"\nProblem: {problem_data['problem']}")
    
    input("Press Enter to see solution steps...")
    
    print("\nSolution Steps:")
    for i, step in enumerate(problem_data["solution_steps"], 1):
        print(f"{i}. {step}")

def show_interactive_tutorial(topic: str = "binary_basics") -> None:
    """Display an interactive tutorial with explanations and examples."""
    tutorials = {
        "binary_basics": {
            "title": "Binary Number Basics",
            "sections": [
                {
                    "name": "What is Binary?",
                    "content": [
                        "Binary is a base-2 number system using only 0s and 1s.",
                        "Each position represents a power of 2:",
                        "... 8s(2³) 4s(2²) 2s(2¹) 1s(2⁰)"
                    ]
                },
                {
                    "name": "Converting to Decimal",
                    "content": [
                        "To convert binary to decimal:",
                        "1. Identify position values",
                        "2. Multiply each 1 by its position value",
                        "3. Sum all values"
                    ],
                    "example": {
                        "binary": "1101",
                        "steps": [
                            "1 × 2³ = 8",
                            "1 × 2² = 4",
                            "0 × 2¹ = 0",
                            "1 × 2⁰ = 1",
                            "8 + 4 + 0 + 1 = 13"
                        ]
                    }
                }
            ]
        }
    }
    
    if topic not in tutorials:
        print(f"Tutorial '{topic}' not found. Available tutorials: {', '.join(tutorials.keys())}")
        return
    
    tutorial = tutorials[topic]
    
    print(f"\n=== {tutorial['title']} ===\n")
    
    for section in tutorial["sections"]:
        print(f"{Colors.BOLD}{section['name']}{Colors.ENDC}")
        print("─" * len(section["name"]))
        
        for line in section["content"]:
            print(line)
        
        if "example" in section:
            print(f"\n{Colors.GREEN}Example:{Colors.ENDC}")
            print(f"Binary number: {section['example']['binary']}")
            print("\nSolution:")
            for step in section['example']['steps']:
                print(f"  {step}")
        
        input("\nPress Enter to continue...")
        print("\n" + "─" * 40 + "\n")

def show_skill_assessment() -> Dict[str, str]:
    """Conduct a skill assessment and return recommended topics."""
    questions = [
        {
            "text": "Can you convert decimal numbers to binary?",
            "options": ["Not yet", "Basic conversions", "Including fractional parts", "Advanced/All cases"],
            "weight": "number_representation"
        },
        {
            "text": "How comfortable are you with binary arithmetic?",
            "options": ["Not started", "Addition only", "Add/Subtract", "All operations"],
            "weight": "arithmetic"
        },
        {
            "text": "Understanding of two's complement?",
            "options": ["What's that?", "Basic concept", "Can perform conversions", "Expert"],
            "weight": "signed_numbers"
        },
        {
            "text": "Experience with digital logic?",
            "options": ["None", "Basic gates", "Adder circuits", "Complex circuits"],
            "weight": "circuits"
        }
    ]
    
    scores = {
        "number_representation": 0,
        "arithmetic": 0,
        "signed_numbers": 0,
        "circuits": 0
    }
    
    print("\n=== Skill Assessment ===\n")
    print("Answer these questions to get personalized learning recommendations:\n")
    
    for i, q in enumerate(questions, 1):
        print(f"\n{i}. {q['text']}")
        for j, opt in enumerate(q['options']):
            print(f"   {j + 1}. {opt}")
        
        while True:
            try:
                choice = int(input("\nYour choice (1-4): "))
                if 1 <= choice <= 4:
                    scores[q['weight']] = choice
                    break
                print("Please enter a number between 1 and 4")
            except ValueError:
                print("Please enter a valid number")
    
    # Generate recommendations
    recommendations = {}
    
    for topic, score in scores.items():
        if score <= 2:
            recommendations[topic] = "beginner"
        elif score == 3:
            recommendations[topic] = "intermediate"
        else:
            recommendations[topic] = "advanced"
    
    print("\n=== Assessment Results ===\n")
    for topic, level in recommendations.items():
        print(f"{topic.replace('_', ' ').title()}: {level.title()} level")
    
    return recommendations

def main():
    print("Welcome to the Educational Tools Menu!")
    while True:
        print("\n=== Educational Tools ===")
        print("1. Show Concept Map")
        print("2. View Learning Path")
        print("3. Practice Problems")
        print("4. Interactive Tutorial")
        print("5. Skill Assessment")
        print("6. Quizzes")
        print("7. Interactive Simulations")
        print("8. Detailed Explanations")
        print("9. Help")
        print("10. Return to Main Menu")

        choice = input("\nEnter choice (1-10): ")

        if choice == "1":
            topic = input("Enter topic (binary/arithmetic): ").lower()
            show_concept_map(topic)
        elif choice == "2":
            level = input("Enter current level (beginner/intermediate/advanced): ").lower()
            show_learning_path(level)
        elif choice == "3":
            topic = input("Enter topic (addition/subtraction): ").lower()
            difficulty = input("Enter difficulty (easy/medium): ").lower()
            show_practice_problem(topic, difficulty)
        elif choice == "4":
            show_interactive_tutorial()
        elif choice == "5":
            show_skill_assessment()
        elif choice == "6":
            show_quiz()
        elif choice == "7":
            show_interactive_simulation()
        elif choice == "8":
            show_detailed_explanation()
        elif choice == "9":
            show_help()
        elif choice == "10":
            break

        input("\nPress Enter to continue...")

def show_quiz():
    """Interactive quiz module with different topics and difficulty levels."""
    quizzes = {
        "binary_basics": {
            "name": "Binary Number Basics",
            "questions": [
                {
                    "question": "What is the decimal equivalent of binary 1010?",
                    "options": ["8", "10", "12", "14"],
                    "correct": 1,  # 10
                    "explanation": "1010 = 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8 + 0 + 2 + 0 = 10"
                },
                {
                    "question": "Which power of 2 does the leftmost bit represent in an 8-bit number?",
                    "options": ["2⁸", "2⁷", "2⁶", "2⁰"],
                    "correct": 1,  # 2⁷
                    "explanation": "In an 8-bit number, bits are numbered 7 to 0 from left to right"
                }
            ]
        },
        "two_complement": {
            "name": "Two's Complement",
            "questions": [
                {
                    "question": "What is -5 in 8-bit two's complement?",
                    "options": ["11111011", "11111010", "00000101", "11110101"],
                    "correct": 0,  # 11111011
                    "explanation": "Steps: 5 = 00000101, invert = 11111010, add 1 = 11111011"
                }
            ]
        }
    }
    
    print("\n=== Binary Number System Quiz ===")
    print("\nAvailable Topics:")
    for i, (topic_id, topic) in enumerate(quizzes.items(), 1):
        print(f"{i}. {topic['name']}")
    
    try:
        topic_choice = int(input("\nChoose a topic (enter number): ")) - 1
        if topic_choice < 0 or topic_choice >= len(quizzes):
            print("Invalid topic choice")
            return
            
        topic_id = list(quizzes.keys())[topic_choice]
        topic = quizzes[topic_id]
        
        print(f"\n=== {topic['name']} Quiz ===")
        score = 0
        total = len(topic['questions'])
        
        for i, q in enumerate(topic['questions'], 1):
            print(f"\nQuestion {i}/{total}:")
            print(q['question'])
            for j, opt in enumerate(q['options'], 1):
                print(f"{j}. {opt}")
            
            try:
                answer = int(input("\nYour answer (enter number): ")) - 1
                if answer == q['correct']:
                    print(f"\n{Colors.GREEN}Correct!{Colors.ENDC}")
                    score += 1
                else:
                    print(f"\n{Colors.RED}Incorrect.{Colors.ENDC}")
                print(f"Explanation: {q['explanation']}")
            except ValueError:
                print("Invalid input. Skipping question.")
        
        print(f"\nQuiz Complete! Score: {score}/{total} ({score/total*100:.1f}%)")
        
    except ValueError:
        print("Invalid input")
        return

def show_interactive_simulation():
    """Interactive simulation of binary operations and conversions."""
    simulations = {
        "binary_addition": {
            "name": "Binary Addition Simulator",
            "description": "Step through binary addition with carry visualization"
        },
        "two_complement": {
            "name": "Two's Complement Converter",
            "description": "Convert between decimal and two's complement representation"
        }
    }
    
    print("\n=== Interactive Binary Simulations ===")
    print("\nAvailable Simulations:")
    for i, (sim_id, sim) in enumerate(simulations.items(), 1):
        print(f"{i}. {sim['name']}")
        print(f"   {sim['description']}")
    
    try:
        choice = int(input("\nChoose a simulation (enter number): ")) - 1
        if choice < 0 or choice >= len(simulations):
            print("Invalid simulation choice")
            return
            
        sim_id = list(simulations.keys())[choice]
        
        if sim_id == "binary_addition":
            print("\n=== Binary Addition Simulator ===")
            try:
                num1 = input("Enter first binary number: ")
                num2 = input("Enter second binary number: ")
                
                # Validate binary input
                if not all(bit in '01' for bit in num1 + num2):
                    print("Invalid binary numbers. Use only 0s and 1s.")
                    return
                
                # Pad to equal length
                max_len = max(len(num1), len(num2))
                num1 = num1.zfill(max_len)
                num2 = num2.zfill(max_len)
                
                print("\nStep-by-step Addition:")
                print(f"  {num1}")
                print(f"+ {num2}")
                print("  " + "-" * max_len)
                
                result = ""
                carry = 0
                
                # Process right to left
                for i in range(max_len-1, -1, -1):
                    bit1 = int(num1[i])
                    bit2 = int(num2[i])
                    current_sum = bit1 + bit2 + carry
                    
                    # Show step
                    print(f"\nPosition {max_len-i}:")
                    print(f"  {bit1} + {bit2} + carry({carry}) = {current_sum}")
                    
                    result = str(current_sum % 2) + result
                    carry = current_sum // 2
                    
                    # Show current state
                    print(f"Current result: {result.zfill(max_len)}")
                    if carry:
                        print(f"Carry out: {carry}")
                
                print("\nFinal Result:")
                if carry:
                    result = "1" + result
                print(f"  {num1}")
                print(f"+ {num2}")
                print("  " + "-" * len(result))
                print(f"  {result}")
                
            except ValueError:
                print("Invalid input")
                return
                
        elif sim_id == "two_complement":
            print("\n=== Two's Complement Converter ===")
            try:
                num = int(input("Enter decimal number to convert: "))
                bits = 8  # Using 8-bit representation
                
                if num >= 2**(bits-1) or num < -(2**(bits-1)):
                    print(f"Number too large for {bits}-bit representation")
                    return
                
                if num >= 0:
                    result = format(num, f'0{bits}b')
                    print(f"\nPositive number, direct conversion:")
                    print(f"Result: {result}")
                else:
                    # Step 1: Get absolute value in binary
                    abs_val = format(abs(num), f'0{bits}b')
                    print(f"\nStep 1: Convert |{num}| to binary:")
                    print(f"  {abs_val}")
                    
                    # Step 2: Invert bits
                    inverted = ''.join('1' if bit == '0' else '0' for bit in abs_val)
                    print("\nStep 2: Invert all bits:")
                    print(f"  {inverted}")
                    
                    # Step 3: Add 1
                    result = format((int(inverted, 2) + 1) & ((1 << bits) - 1), f'0{bits}b')
                    print("\nStep 3: Add 1:")
                    print(f"  {result}")
                    
                print(f"\nFinal {bits}-bit two's complement representation:")
                print(f"  {result}")
                
            except ValueError:
                print("Invalid input")
                return
    
    except ValueError:
        print("Invalid input")
        return

def show_detailed_explanation():
    """Show detailed explanations of binary number system concepts."""
    topics = {
        "number_systems": {
            "title": "Number Systems and Base Conversion",
            "content": [
                "A number system is a way to represent numbers using a specific set of digits.",
                "\nDecimal (Base-10):",
                "• Uses digits 0-9",
                "• Each position represents a power of 10",
                "• Example: 123 = 1×10² + 2×10¹ + 3×10⁰",
                "\nBinary (Base-2):",
                "• Uses digits 0-1",
                "• Each position represents a power of 2",
                "• Example: 1101 = 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 13"
            ]
        },
        "two_complement": {
            "title": "Two's Complement Representation",
            "content": [
                "Two's complement is a method for representing signed integers in binary.",
                "\nProperties:",
                "• Most significant bit (MSB) indicates sign (0=positive, 1=negative)",
                "• Positive numbers are represented normally",
                "• Negative numbers: invert all bits and add 1",
                "\nExample: Representing -5 in 8 bits:",
                "1. +5 in binary: 00000101",
                "2. Invert bits:  11111010",
                "3. Add 1:       11111011 (-5 in two's complement)"
            ]
        },
        "ieee_754": {
            "title": "IEEE-754 Floating Point Format",
            "content": [
                "IEEE-754 is the standard for representing floating-point numbers in binary.",
                "\nSingle Precision (32-bit) Format:",
                "• Sign bit (1 bit): 0=positive, 1=negative",
                "• Exponent (8 bits): biased by 127",
                "• Mantissa (23 bits): represents 1.fraction",
                "\nExample: Converting 5.75 to IEEE-754:",
                "1. 5.75 = 101.11 in binary",
                "2. Normalize: 1.0111 × 2²",
                "3. Exponent: 2 + 127 = 129 = 10000001",
                "4. Result: 0|10000001|01110000000000000000000"
            ]
        }
    }
    
    print("\n=== Detailed Binary Number System Explanations ===")
    print("\nAvailable Topics:")
    for i, (topic_id, topic) in enumerate(topics.items(), 1):
        print(f"{i}. {topic['title']}")
    
    try:
        choice = int(input("\nChoose a topic (enter number): ")) - 1
        if choice < 0 or choice >= len(topics):
            print("Invalid topic choice")
            return
            
        topic_id = list(topics.keys())[choice]
        topic = topics[topic_id]
        
        print(f"\n=== {topic['title']} ===")
        for line in topic['content']:
            print(line)
            
        print("\nPress Enter to continue...")
        input()
        
    except ValueError:
        print("Invalid input")
        return

def show_help():
    print("\n=== Help ===")
    print("Welcome to the Binary Number System Educational Tool (BNSET)!")
    print("This tool provides various features to help you understand and practice binary number systems.")
    print("\nAvailable Options:")
    print("1. Show Concept Map: Displays a concept map for binary number systems.")
    print("2. View Learning Path: Shows a recommended learning path based on your current level.")
    print("3. Practice Problems: Provides practice problems with solution steps.")
    print("4. Interactive Tutorial: Offers an interactive tutorial with explanations and examples.")
    print("5. Skill Assessment: Conducts a skill assessment and provides personalized learning recommendations.")
    print("6. Quizzes: Allows you to take quizzes to test your knowledge.")
    print("7. Interactive Simulations: Provides interactive simulations to enhance learning.")
    print("8. Detailed Explanations: Offers detailed explanations for various topics.")
    print("9. Help: Displays this help message.")
    print("10. Return to Main Menu: Returns to the main menu.")
    print("\nFor more information, please refer to the README.md file.")

if __name__ == "__main__":
    main() 