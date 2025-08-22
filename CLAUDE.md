# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Reflex custom component library for rendering KaTeX math expressions. The project provides a wrapper around the `react-katex` library to enable LaTeX math rendering in Reflex applications.

## Commands

### Development
- **Install dependencies**: `pip install -r katex_demo/requirements.txt` (for demo) or `pip install -e .` (for package development)
- **Run demo app**: `cd katex_demo && reflex run` 
- **Run tests**: `pytest` (uses pytest as configured in pyproject.toml)

### Build & Package
- **Build package**: Uses Poetry build system (`poetry build`)
- **Install in development mode**: `pip install -e .`
- **Publish to PyPI**: `poetry publish` (for manual publishing)

### Release Process
- Tags follow format `X.Y.Z` (no 'v' prefix)
- GitHub Actions automatically publishes to PyPI on tag push using trusted publishing
- Workflow validates version is newer than existing PyPI version before publishing

## Architecture

### Package Structure
- `src/reflex_katex/`: Main package containing the KaTeX components
  - `katex.py`: Defines both `InlineMath` and `BlockMath` components
  - `__init__.py`: Exports the main components
- `katex_demo/`: Demo application showcasing component usage

### Core Components

#### InlineMath & BlockMath Components
Both components wrap `react-katex` library and inherit from `rx.Component`:
- **InlineMath**: For inline mathematical expressions within text flow
- **BlockMath**: For display equations (centered, block-level)
- Both use shared CSS styling to show only MathML rendering (hides HTML version)
- Automatically import both React components and KaTeX CSS

#### Factory Functions
- `inline_math(expression: str, **props) -> InlineMath`
- `block_math(expression: str, **props) -> BlockMath`
- Accept LaTeX expressions and optional component properties

### Key Implementation Details

#### CSS Styling Strategy
The components inject custom CSS (`_KATEX_STYLES`) that:
- Hides the HTML rendering (`.katex-html { display: none !important; }`)
- Shows only MathML output (`.katex-mathml { display: inline !important; }`)
- This prevents duplication where both MathML and HTML versions were visible

#### Import Management
Both components use unified imports in `_get_imports()`:
- Import both `InlineMath` and `BlockMath` from `react-katex`
- Include `katex/dist/katex.min.css` for styling
- Prevents import conflicts when using multiple component types

### Dependencies
- Requires `reflex >= 0.8.0`
- Uses `react-katex` as the underlying JavaScript library
- Python 3.10+ required
- KaTeX CSS automatically included

## Development Notes

### Component API Design
Components accept standard LaTeX notation:
- Fractions: `\\frac{a}{b}`
- Superscripts/subscripts: `x^2`, `x_1`
- Greek letters: `\\alpha`, `\\beta`
- Complex expressions: `\\int_0^\\infty x^2 dx`

### Demo Application
The `katex_demo/` contains a working Reflex app demonstrating both inline and block math usage within text components. Use this for testing changes and validating rendering behavior.