"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import reflex as rx
from reflex_katex import inline_math, block_math

class State(rx.State):
    """The app state."""
    pass

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to reflex-katex demo!", size="9"),
            rx.heading("Basic KaTeX example with Latex"),
            rx.text(
                "Here is an example of inline math: ",
                inline_math("\\int_0^\\infty x^2 dx"),
                " and you can now see how it is inline."
            ),
            rx.text(
                "Here is an example of block math: ",
                block_math("\\int_0^\\infty x^2 dx"),
                " and you can now see how it is block.",
            ),
        width="100vw",
        height="100vh",
        align="center",
        )
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
