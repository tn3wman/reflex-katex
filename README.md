# reflex-katex

A Reflex custom component library for rendering beautiful mathematical expressions using KaTeX.

## Installation

```bash
pip install reflex-katex
```

## Quick Start

```python
import reflex as rx
from reflex_katex import inline_math, block_math

def index():
    return rx.vstack(
        rx.text(
            "Here's an inline equation: ",
            inline_math("E = mc^2"),
            " in the middle of text."
        ),
        rx.text("And here's a display equation:"),
        block_math("\\int_0^\\infty e^{-x^2} dx = \\frac{\\sqrt{\\pi}}{2}"),
        spacing="4"
    )

app = rx.App()
app.add_page(index)
```

## Features

- 🔢 **Inline Math**: Render LaTeX expressions within text flow
- 📐 **Block Math**: Display centered mathematical equations
- 🎨 **Beautiful Rendering**: Powered by KaTeX for fast, high-quality output
- 🔧 **Simple API**: Easy-to-use functions that integrate seamlessly with Reflex
- ♿ **Accessible**: Proper MathML output for screen readers

## Usage

### Inline Math

Use `inline_math()` to render mathematical expressions within text:

```python
rx.text(
    "The quadratic formula is ",
    inline_math("x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}"),
    " and it's very useful."
)
```

### Block Math

Use `block_math()` for display equations that should be centered and prominent:

```python
block_math("\\sum_{n=1}^{\\infty} \\frac{1}{n^2} = \\frac{\\pi^2}{6}")
```

### LaTeX Syntax

reflex-katex supports standard LaTeX mathematical notation:

```python
# Fractions
inline_math("\\frac{1}{2}")

# Superscripts and subscripts
inline_math("x^2 + y_1")

# Greek letters
inline_math("\\alpha + \\beta = \\gamma")

# Integrals
block_math("\\int_a^b f(x) dx")

# Matrices
block_math("\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}")

# Complex expressions
block_math("f(x) = \\begin{cases} x^2 & \\text{if } x \\geq 0 \\\\ -x^2 & \\text{if } x < 0 \\end{cases}")
```

### Passing Additional Props

Both functions accept additional component properties:

```python
inline_math("x^2", style={"color": "blue"})
block_math("\\sum x_i", class_name="my-equation")
```

## Examples

### Scientific Notation
```python
rx.vstack(
    rx.heading("Scientific Formulas"),
    rx.text("Einstein's mass-energy equivalence: ", inline_math("E = mc^2")),
    rx.text("Schrödinger equation:"),
    block_math("i\\hbar\\frac{\\partial}{\\partial t}\\Psi = \\hat{H}\\Psi"),
    rx.text("Newton's second law: ", inline_math("F = ma")),
)
```

### Mathematical Concepts
```python
rx.vstack(
    rx.heading("Calculus"),
    rx.text("Derivative definition:"),
    block_math("f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}"),
    rx.text("Fundamental theorem of calculus:"),
    block_math("\\int_a^b f'(x) dx = f(b) - f(a)"),
)
```

### Statistics
```python
rx.vstack(
    rx.heading("Statistics"),
    rx.text("Normal distribution probability density:"),
    block_math("f(x) = \\frac{1}{\\sigma\\sqrt{2\\pi}} e^{-\\frac{1}{2}\\left(\\frac{x-\\mu}{\\sigma}\\right)^2}"),
    rx.text("Sample variance: ", inline_math("s^2 = \\frac{1}{n-1}\\sum_{i=1}^n (x_i - \\bar{x})^2")),
)
```

## API Reference

### `inline_math(expression: str, **props) -> InlineMath`

Renders a LaTeX expression inline within text.

**Parameters:**
- `expression` (str): LaTeX mathematical expression
- `**props`: Additional component properties

**Returns:** InlineMath component

### `block_math(expression: str, **props) -> BlockMath`

Renders a LaTeX expression as a centered display equation.

**Parameters:**
- `expression` (str): LaTeX mathematical expression  
- `**props`: Additional component properties

**Returns:** BlockMath component

## Supported LaTeX

reflex-katex supports a wide range of LaTeX mathematical notation through KaTeX. For a complete list of supported functions and symbols, see the [KaTeX documentation](https://katex.org/docs/supported.html).

Common categories include:
- Basic math: `+`, `-`, `*`, `/`, `=`, `<`, `>`
- Fractions: `\frac{a}{b}`
- Exponents/subscripts: `x^2`, `x_1`
- Roots: `\sqrt{x}`, `\sqrt[n]{x}`
- Greek letters: `\alpha`, `\beta`, `\gamma`, etc.
- Calculus: `\int`, `\sum`, `\prod`, `\lim`
- Logic: `\land`, `\lor`, `\neg`, `\forall`, `\exists`
- Sets: `\in`, `\subset`, `\cup`, `\cap`
- And much more!

## Requirements

- Python 3.8+
- Reflex >= 0.8.0
- A modern web browser with JavaScript enabled

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [KaTeX](https://katex.org/) - Fast math typesetting for the web
- [react-katex](https://github.com/MatejMazur/react-katex) - React components for KaTeX
- [Reflex](https://reflex.dev/) - The web framework for Python