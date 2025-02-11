import reflex as rx
from ...wrappers.component.state import ComponentWrapperState

data = [
    {"month": "Jan", "desktop": 186},
    {"month": "Feb", "desktop": 305},
    {"month": "Mar", "desktop": 237},
    {"month": "Apr", "desktop": 73},
    {"month": "May", "desktop": 209},
    {"month": "Jun", "desktop": 214},
]


def barchart_v2():
    return rx.center(
        rx.vstack(
            rx.vstack(
                rx.heading("Bar Chart - Horizontal", size="5", weight="bold"),
                rx.text("January - June 2024", size="1", color=rx.color("slate", 11)),
                spacing="1",
            ),
            rx.divider(height="1rem", opacity="0"),
            rx.recharts.bar_chart(
                rx.recharts.graphing_tooltip(
                    label_style={"fontWeight": "700"},
                    item_style={"padding": "0px"},
                    separator=":",
                ),
                rx.recharts.bar(
                    data_key="desktop",
                    fill=ComponentWrapperState.default_theme[0],
                ),
                rx.recharts.x_axis(type_="number", hide=True),
                rx.recharts.y_axis(data_key="month", type_="category", axis_line=False),
                data=data,
                layout="vertical",
                width="100%",
                height=300,
                bar_size=25,
                bar_gap=2,
                bar_category_gap=0,
                margin={"left": -20},
            ),
            rx.vstack(
                rx.heading("Trending up by 5.2% this month", size="3", weight="bold"),
                rx.text(
                    "Showing total visitors for the last 6 months",
                    size="1",
                    color=rx.color("slate", 11),
                ),
                spacing="1",
            ),
            width="100%",
        ),
        width="100%",
        padding="12px",
    )
