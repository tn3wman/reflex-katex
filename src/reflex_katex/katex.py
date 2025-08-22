"""Reflex custom component for KaTeX."""

import reflex as rx

# Shared KaTeX styling - injected once
_KATEX_STYLES = """
// Show only MathML rendering, hide HTML version
const katexStyles = `
.katex-html {
    display: none !important;
}
.katex-mathml {
    display: inline !important;
}
`;

if (typeof document !== 'undefined' && !document.getElementById('katex-styles')) {
    const style = document.createElement('style');
    style.id = 'katex-styles';
    style.textContent = katexStyles;
    document.head.appendChild(style);
}
"""

class InlineMath(rx.Component):
    """KaTeX inline math component."""

    library = "react-katex"
    tag = "InlineMath"
    math: rx.Var[str]
    
    def _get_imports(self):
        return {"react-katex": {"InlineMath", "BlockMath"}, "katex/dist/katex.min.css": set()}
    
    def _get_custom_code(self) -> str:
        return _KATEX_STYLES
    

def inline_math(expression: str, **props) -> InlineMath:
    """Create an inline math component using KaTeX.
    
    Args:
        expression: LaTeX mathematical expression (e.g., "x^2", "\\frac{1}{2}")
        **props: Additional component properties
        
    Returns:
        InlineMath component for inline mathematical expressions
    """
    return InlineMath.create(math=expression, **props)


class BlockMath(rx.Component):
    """KaTeX block math component."""

    library = "react-katex"
    tag = "BlockMath"
    math: rx.Var[str]
    
    def _get_imports(self):
        return {"react-katex": {"InlineMath", "BlockMath"}, "katex/dist/katex.min.css": set()}
    
    def _get_custom_code(self) -> str:
        return _KATEX_STYLES


def block_math(expression: str, **props) -> BlockMath:
    """Create a block math component using KaTeX.
    
    Args:
        expression: LaTeX mathematical expression (e.g., "\\int_0^\\infty x^2 dx")
        **props: Additional component properties
        
    Returns:
        BlockMath component for display mathematical expressions
    """
    return BlockMath.create(math=expression, **props)