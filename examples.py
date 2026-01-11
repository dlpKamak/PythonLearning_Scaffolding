"""
Examples of using the Code Block Highlighter library
Perfect for teaching children about code structure and indentation
"""

from code_blocks import highlight, CodeBlockHighlighter


# Example 1: Basic usage - your original example
print("=" * 80)
print("EXAMPLE 1: Your Game Code")
print("=" * 80)

game_code = """while(corn_collects_all == true):
    if(block != 'chickens'):
        move_forward(1)
        turn_north()
        move_forward(1)
        turn_east()"""

highlight(game_code, style='indent', show_lines=True)


# Example 2: Python loops
print("\n" + "=" * 80)
print("EXAMPLE 2: Nested Loops")
print("=" * 80)

loop_code = """for i in range(5):
    print("Outer loop:", i)
    for j in range(3):
        print("  Inner loop:", j)
        if j == 2:
            print("    Last iteration!")"""

highlight(loop_code, style='indent', show_lines=True)


# Example 3: Function definition
print("\n" + "=" * 80)
print("EXAMPLE 3: Function with Conditions")
print("=" * 80)

function_code = """def check_grade(score):
    if score >= 90:
        print("Grade: A")
        return "Excellent!"
    elif score >= 80:
        print("Grade: B")
        return "Good job!"
    else:
        print("Grade: C or below")
        return "Keep trying!"

result = check_grade(85)"""

highlight(function_code, style='indent', show_lines=True)


# Example 4: Block indicator style
print("\n" + "=" * 80)
print("EXAMPLE 4: Block Indicators (shows nesting with │)")
print("=" * 80)

highlight(loop_code, style='blocks', show_lines=False)


# Example 5: Custom usage with the class
print("\n" + "=" * 80)
print("EXAMPLE 5: Advanced - Creating Custom Highlighter")
print("=" * 80)

highlighter = CodeBlockHighlighter()

class_code = """class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        if self.name:
            print(f"{self.name} makes a sound")
        else:
            print("Unknown animal")

dog = Animal("Rex")
dog.speak()"""

print(highlighter.highlight_code(class_code, show_lines=True))


print("\n" + "=" * 80)
print("Tips for Teaching:")
print("=" * 80)
print("""
1. Each color represents a different level of indentation
2. Code at the same color level "belongs together"
3. Darker/first color = main code (not indented)
4. Each new indent = entering a new "block" of code
5. Code inside blocks only runs when the condition above it is true

Try modifying the examples above to see how the colors change!
""")
