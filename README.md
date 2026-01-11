# Code Block Highlighter 🎨

A Python library that highlights code blocks with colored backgrounds in the console, making it easier for children (and beginners) to understand code structure, indentation, and how blocks work.

## Why This Library?

Children learning to code often struggle with understanding indentation and block structure. This library provides **visual scaffolding** by:

- 🎨 Coloring different indentation levels with different background colors
- 📏 Showing clearly which code belongs to which block
- 🔢 Optional line numbers for reference
- 📊 Visual indicators (│) to show nesting depth

## Installation

Simply copy `code_blocks.py` to your project directory. No external dependencies required!

## Quick Start

```python
from code_blocks import highlight

# Your code as a string
code = """while(corn_collects_all == true):
    if(block != 'chickens'):
        move_forward(1)
        turn_north()
        move_forward(1)
        turn_east()"""

# Highlight it!
highlight(code, style='indent', show_lines=True)
```

## Features

### Two Highlighting Styles

1. **`indent`** - Full background colors for each line
   - Best for showing overall structure
   - Good for younger learners
   
2. **`blocks`** - Visual indicators (│) showing nesting
   - More compact
   - Good for understanding depth

### Options

- `show_lines` - Add line numbers (True/False)
- Auto-detects indentation size (2 or 4 spaces)

## Usage Examples

### Basic Usage

```python
from code_blocks import highlight

code = """for i in range(5):
    print(i)
    if i == 3:
        print("Found 3!")"""

highlight(code)
```

### Without Line Numbers

```python
highlight(code, style='indent', show_lines=False)
```

### Block Indicator Style

```python
highlight(code, style='blocks')
```

### Advanced: Using the Class

```python
from code_blocks import CodeBlockHighlighter

highlighter = CodeBlockHighlighter()

# Method 1: Full backgrounds
output = highlighter.highlight_code(code, show_lines=True)
print(output)

# Method 2: Block indicators
output = highlighter.highlight_blocks(code)
print(output)
```

## Color Scheme

The library uses 6 colors that cycle through as nesting increases:

1. 🟢 Dark Green - Level 0 (main code)
2. 🟡 Yellow/Tan - Level 1 (first indent)
3. 🟠 Orange/Brown - Level 2 (second indent)
4. 🟣 Purple - Level 3 (third indent)
5. 🔵 Blue - Level 4 (fourth indent)
6. 🔴 Red - Level 5+ (deep nesting)

## Teaching Tips

### For Children

1. **Start with simple examples**: Use code with just 1-2 levels of indentation
2. **Explain colors**: "Each color is like a different room in a house"
3. **Point out patterns**: "See how all the green code runs first?"
4. **Compare with/without colors**: Show the same code plain and highlighted

### Example Lesson Plan

1. Show uncolored code and ask "Which lines belong together?"
2. Show highlighted version: "The colors show you!"
3. Trace execution: "We start with green, when we enter the if, we go to yellow..."
4. Practice: Have them predict what color a new line would be

### Common Confusions This Solves

- **"Why won't my code run?"** → Often they can see the indentation is wrong
- **"What does this code do?"** → Colors show the flow and grouping
- **"How deep am I nested?"** → Each color = one level deeper
- **"When does this code execute?"** → "Only when you're inside the yellow block!"

## API Reference

### `highlight(code, style='blocks', show_lines=True)`

Convenience function to highlight and print code.

**Parameters:**
- `code` (str): The source code to highlight
- `style` (str): 'blocks' or 'indent' highlighting style
- `show_lines` (bool): Whether to show line numbers

### `CodeBlockHighlighter` Class

#### Methods

**`highlight_code(code, show_lines=True)`**
- Returns formatted string with full background colors
- Each indentation level gets a different color

**`highlight_blocks(code)`**
- Returns formatted string with visual block indicators (│)
- More compact, shows nesting depth

**`detect_indent_size(code)`**
- Auto-detects whether code uses 2 or 4 space indentation

**`get_indent_level(line)`**
- Returns the indentation level (0, 1, 2, etc.) for a line

## Limitations

- Works in terminals that support ANSI color codes
- Fixed line width of 80 characters (customizable in code)
- Best for Python-style indentation (spaces, not tabs)

## Extending the Library

Want to add features? Easy modifications:

### Custom Colors

Edit the `COLORS` list in the `CodeBlockHighlighter` class:

```python
COLORS = [
    '\033[48;5;22m',   # Your custom color codes here
    # Add more...
]
```

### Different Line Width

Change the padding calculation:

```python
padding = ' ' * (120 - len(line_num) - len(content))  # 120 instead of 80
```

### Support for Tabs

Modify `detect_indent_size` to handle tabs:

```python
if '\t' in line:
    self.indent_size = 'tab'
```

## Real-World Applications

- **Coding tutoring**: Show structure during lessons
- **Code review**: Help students see where their indentation is wrong
- **Debugging sessions**: Visualize the flow of nested conditionals
- **Documentation**: Create visual examples in teaching materials
- **Presentations**: Make code examples clearer for audiences

## Example Output

```
1) while(corn_collects_all == true):                [Green background]
2)     if(block != 'chickens'):                     [Yellow background]
3)         move_forward(1)                          [Orange background]
4)         turn_north()                             [Orange background]
5)         move_forward(1)                          [Orange background]
6)         turn_east()                              [Orange background]
```

## Contributing

This is an educational tool! Suggestions welcome:

- More color schemes
- Support for other languages
- Interactive features
- Export to HTML
- Jupyter notebook integration

## License

Free to use for educational purposes. Share with other educators!

## Credits

Created to help children understand code structure through visual learning.
Inspired by block-based programming environments like Scratch.

---

**Happy Teaching! 👨‍🏫👩‍🏫**
