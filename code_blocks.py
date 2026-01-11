"""
Code Blocks Highlighter - A learning tool for understanding code structure
Highlights nested blocks with different background colors in the console
"""

import re
from typing import List, Tuple, Optional


class CodeBlockHighlighter:
    """Highlights code blocks with colored backgrounds to show structure"""
    
    # ANSI escape codes for colored backgrounds
    COLORS = [
        '\033[48;5;22m',   # Dark green
        '\033[48;5;58m',   # Yellow/tan
        '\033[48;5;94m',   # Orange/brown
        '\033[48;5;54m',   # Purple
        '\033[48;5;24m',   # Blue
        '\033[48;5;88m',   # Red
    ]
    RESET = '\033[0m'
    WHITE_TEXT = '\033[97m'
    
    def __init__(self):
        self.indent_size = 4  # Default Python indentation
        
    def detect_indent_size(self, code: str) -> int:
        """Auto-detect indentation size from code"""
        lines = code.split('\n')
        for line in lines:
            if line and line[0] == ' ':
                # Count leading spaces
                spaces = len(line) - len(line.lstrip())
                if spaces > 0:
                    return spaces
        return 4
    
    def get_indent_level(self, line: str) -> int:
        """Calculate indentation level of a line"""
        if not line.strip():
            return 0
        leading_spaces = len(line) - len(line.lstrip())
        return leading_spaces // self.indent_size
    
    def highlight_code(self, code: str, show_lines: bool = True) -> str:
        """
        Highlight code blocks with colored backgrounds
        
        Args:
            code: The source code to highlight
            show_lines: Whether to show line numbers
            
        Returns:
            Formatted string with ANSI color codes
        """
        lines = code.split('\n')
        self.indent_size = self.detect_indent_size(code)
        
        result = []
        max_line_num_width = len(str(len(lines)))
        
        for i, line in enumerate(lines, 1):
            if not line.strip():
                result.append('')
                continue
                
            indent_level = self.get_indent_level(line)
            color = self.COLORS[indent_level % len(self.COLORS)]
            
            # Prepare line number
            line_num = f"{i:>{max_line_num_width}}) " if show_lines else ""
            
            # Calculate padding to fill the line
            content = line.rstrip()
            padding = ' ' * (80 - len(line_num) - len(content))
            
            # Format with color
            formatted = f"{line_num}{color}{self.WHITE_TEXT}{content}{padding}{self.RESET}"
            result.append(formatted)
        
        return '\n'.join(result)
    
    def highlight_blocks(self, code: str) -> str:
        """
        Highlight code blocks with visible block boundaries
        
        Args:
            code: The source code to highlight
            
        Returns:
            Formatted string with block indicators
        """
        lines = code.split('\n')
        self.indent_size = self.detect_indent_size(code)
        
        result = []
        block_stack = [0]  # Track nesting levels
        
        for i, line in enumerate(lines):
            if not line.strip():
                result.append('')
                continue
            
            indent_level = self.get_indent_level(line)
            
            # Detect block changes
            if indent_level > block_stack[-1]:
                # Entering new block
                block_stack.append(indent_level)
            elif indent_level < block_stack[-1]:
                # Exiting block(s)
                while block_stack and block_stack[-1] > indent_level:
                    block_stack.pop()
            
            # Choose color based on current nesting
            color = self.COLORS[len(block_stack) - 1 % len(self.COLORS)]
            
            # Add visual block indicator
            block_indicator = '│ ' * (indent_level) if indent_level > 0 else ''
            content = line.lstrip()
            
            # Format with color and padding
            padding = ' ' * (80 - len(block_indicator) - len(content))
            formatted = f"{color}{self.WHITE_TEXT}{block_indicator}{content}{padding}{self.RESET}"
            result.append(formatted)
        
        return '\n'.join(result)


def highlight(code: str, style: str = 'blocks', show_lines: bool = True) -> None:
    """
    Convenience function to highlight and print code
    
    Args:
        code: Source code to highlight
        style: 'blocks' or 'indent' highlighting style
        show_lines: Whether to show line numbers
    """
    highlighter = CodeBlockHighlighter()
    
    if style == 'indent':
        output = highlighter.highlight_code(code, show_lines)
    else:
        output = highlighter.highlight_blocks(code)
    
    print(output)


def demo():
    """Demonstrate the code block highlighter with examples"""
    
    example1 = """while(corn_collects_all == true):
    if(block != 'chickens'):
        move_forward(1)
        turn_north()
        move_forward(1)
        turn_east()"""
    
    example2 = """def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)"""
    
    example3 = """for i in range(3):
    print(f"Outer loop {i}")
    for j in range(2):
        print(f"  Inner loop {j}")
        if j == 1:
            print("    Deepest level!")"""
    
    print("=" * 80)
    print("CODE BLOCK HIGHLIGHTER - Demo")
    print("=" * 80)
    print()
    
    print("Example 1: Simple nested blocks (with line numbers)")
    print("-" * 80)
    highlight(example1, style='indent', show_lines=True)
    print()
    
    print("Example 2: Function with conditional (block indicators)")
    print("-" * 80)
    highlight(example2, style='blocks', show_lines=False)
    print()
    
    print("Example 3: Deeply nested loops (with line numbers)")
    print("-" * 80)
    highlight(example3, style='indent', show_lines=True)
    print()


if __name__ == '__main__':
    demo()
