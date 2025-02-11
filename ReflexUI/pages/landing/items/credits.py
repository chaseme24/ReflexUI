import reflex as rx
from dataclasses import dataclass, field
from typing import Callable, Dict, List


@dataclass
class CreditBannerStyle:
    base: Dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "justify": "center",
            "wrap": "wrap",
            "padding": "0.5em",
            "bg": rx.color("slate", 3),
            "border_top": f"1.5px solid {rx.color('slate')}",
            "border_bottom": f"1.5px solid {rx.color('slate')}",
        }
    )


CreditBannerStyle: CreditBannerStyle = CreditBannerStyle()

link: Callable[[str, str], rx.Component] = lambda name, url: rx.link(
    name,
    href=url,
    weight="bold",
    text_decoration="none",
    color="inherit",
    is_external=True,
)

credit_banner: Callable[[], rx.Component] = lambda: rx.hstack(
    rx.text(
        "Special thanks to ",
        link("@Reflex", "https://reflex.dev"),
        ", ",
        link("@unDraw", "https://undraw.co"),
        ", ",
        link("@shadcn/ui", "https://ui.shadcn.com/"),
        ", ",
        link("@buridan-ui", "https://buridan-ui.reflex.run/"),
        " and other amazing open-source projects for the inspiration!",
        color_scheme="gray",
        size="1",
        align="center",
    ),
    **CreditBannerStyle.base,
)
