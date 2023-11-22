"""The home page of the app."""

from hexbox import styles
from hexbox.templates import template

import reflex as rx


@template(
    route="/",
    title="index",
    # image="/github.svg",
)
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    # with open("README.md", encoding="utf-8") as readme:
    #     content = readme.read()
    # return rx.markdown(content, component_map=styles.markdown_style)
    return rx.box(
        rx.text("haha yeet"),
        background_color=rx.color_mode_cond("#6767cb", "#343498"),
        align_items="center",
        justify_content="center",
        height="100%",
    )
