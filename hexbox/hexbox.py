"""Welcome to Reflex!."""

from hexbox import styles

# Import all the pages.
from hexbox.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style, overlay_component=None)
app.compile()
