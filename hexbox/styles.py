"""Styles for the app."""

import reflex as rx

border_radius = "0.375rem"
box_shadow = "0px 0px 0px 1px rgba(84, 82, 95, 0.14)"
border = "1px solid #F4F3F6"
text_color = rx.color_mode_cond("hsl(203, 6%, 24%)", "hsl(197, 6%, 76%)")
accent_text_color = rx.color_mode_cond("hsl(202, 54%, 15%)", "hsl(202, 66%, 68%)")
accent_color = rx.color_mode_cond("hsl(150, 95%, 42%)", "hsl(150, 98%, 52%)")
hover_accent_color = {"_hover": {"color": accent_color}}
hover_accent_bg = {"_hover": {"bg": accent_color}}
link_text_color = rx.color_mode_cond("hsl(203, 6%, 16%)", "hsl(197, 6%, 88%)")
link_underline_color = rx.color_mode_cond("hsl(240, 80%, 76%)", "hsl(240, 55%, 55%)")
code_text_color = "hsl(240, 55%, 48%)"
code_bg_color = "hsl(240, 80%, 78%)"
content_width_vw = "90vw"
sidebar_width = "6em"

template_page_style = {"padding_top": "5em", "padding_x": ["auto", "2em"], "flex": "1"}

template_content_style = {
    "align_items": "flex-start",
    "box_shadow": box_shadow,
    "border_radius": border_radius,
    "padding": "1em",
    "margin_bottom": "2em",
}

link_style = {
    "color": text_color,
    "text_decoration": "none",
    **hover_accent_color,
}

overlapping_button_style = {
    "background_color": "white",
    "border": border,
    "border_radius": border_radius,
}

base_style = {
    rx.MenuButton: {
        "width": "3em",
        "height": "3em",
        **overlapping_button_style,
    },
    rx.MenuItem: hover_accent_bg,
}

markdown_style = {
    "code": lambda text: rx.code(text, color=code_text_color, bg=code_bg_color),
    "a": lambda text, **props: rx.link(
        text,
        **props,
        font_weight="bold",
        color=link_text_color,
        text_decoration="underline",
        text_decoration_color=link_underline_color,
        _hover={
            "color": link_underline_color,
            "text_decoration": "underline",
            "text_decoration_color": link_text_color,
        },
    ),
}
