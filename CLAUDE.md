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

## Architecture

### Package Structure
- `src/reflex_katex/`: Main package containing the KaTeX component
  - `katex.py`: Defines the `InlineMath` component that wraps `react-katex`
  - `__init__.py`: Exports the main component
- `katex_demo/`: Demo application showcasing the component usage
  - Contains a simple Reflex app demonstrating LaTeX math rendering

### Key Components
- **InlineMath**: The primary component for rendering inline LaTeX math expressions
  - Uses `react-katex` library
  - Inherits from `rx.Component`
  - Can render LaTeX expressions like `"\\(\\frac{10}{4x} \\approx 2^{12}\\)"`

### Dependencies
- Requires `reflex >= 0.8.0`
- Uses `react-katex` as the underlying JavaScript library
- Python 3.10+ required

## Development Notes

The main component file (`src/reflex_katex/katex.py`) contains commented-out code for alternative implementations (MathJax, Mantine components) that may be useful for future development or reference.

The demo application shows basic usage of the component within a Reflex app structure.