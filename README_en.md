# BaseComponents Library
> [Flet Official Website](https://flet.dev)

> WARN: The README for this language is AI-translated. Please refer to the Simplified Chinese version of the README for actual details.

[zh_cn](README.md)  |  [en](README_en.md)

Flet_BaseComponents is a reusable component library designed for Flet applications, providing a set of unified UI components and a theme management system to help developers quickly build applications with consistent appearance and user experience.

## Directory Structure

```
BaseComponents/
├── __init__.py          # Exports all components
├── textComponents.py    # Text-related components
├── buttonComponents.py  # Button-related components
├── inputComponents.py   # Input-related components
├── cardComponents.py    # Card-related components
├── layoutComponents.py  # Layout-related components
└── themeManager.py      # Theme manager
```

## Component Introduction

### Text Components (textComponents.py)

Provides various text styles and layout components:

- `center_text(text, size=30, color=None, **kwargs)` - Create centered text
- `right_text(text, size=30, color=None, **kwargs)` - Create right-aligned text
- `left_text(text, size=30, color=None, **kwargs)` - Create left-aligned text
- `heading(text, level=1, color=None)` - Create heading text (level 1-6)
- `body(text, size=14, color=None)` - Create body text
- `caption(text, color=None)` - Create caption text
- `link(text, url=None, on_click=None, underline=True)` - Create link text

Example:
```python
from BaseComponents import *

# Create different types of text
page.add(
    heading("Main Title", level=1),
    body("This is a paragraph of body text"),
    caption("This is a caption text"),
    link("Underlined link", url="https://example.com"),
    link("Link without underline", url="https://example.com", underline=False)
)
```

### Button Components (buttonComponents.py)

Provides multiple styled button components:

- `primary_button(text, on_click=None, width=None, height=None)` - Primary button
- `secondary_button(text, on_click=None, width=None, height=None)` - Secondary button
- `icon_button(icon, on_click=None, tooltip=None)` - Icon button

Example:
```python
from BaseComponents import *

def button_clicked(e):
    print("Button clicked")

page.add(
    primary_button("Primary Action", on_click=button_clicked),
    secondary_button("Secondary Action", on_click=button_clicked),
    icon_button(icons.ADD, on_click=button_clicked, tooltip="Add")
)
```

### Input Components (inputComponents.py)

Provides commonly used input controls:

- `text_field(label, hint_text=None, on_change=None, width=None)` - Text input field
- `dropdown(label, options, on_change=None, width=None)` - Dropdown selection box
- `checkbox(label, value=False, on_change=None)` - Checkbox

Example:
```python
from BaseComponents import *

def on_text_change(e):
    print(f"Text changed: {e.control.value}")

def on_dropdown_change(e):
    print(f"Selection changed: {e.control.value}")

page.add(
    text_field("Username", hint_text="Please enter username", on_change=on_text_change),
    dropdown("Options", ["Option 1", "Option 2", "Option 3"], on_change=on_dropdown_change),
    checkbox("Agree to terms")
)
```

### Card Components (cardComponents.py)

Provides feature-rich card components supporting titles, action buttons, images, click events, etc.:

- `Card.create(...)` - Create custom card (full functionality)
- `simple_card(content, ...)` - Create simple card
- `titled_card(title, content, actions=None, ...)` - Create titled card
- `image_card(image_src, content=None, ...)` - Create image card
- `outlined_card(content, ...)` - Create outlined card
- `clickable_card(content, on_click, ...)` - Create clickable card

Example:
```python
from BaseComponents import *

# Simple card
page.add(
    simple_card("This is a simple card")
)

# Titled card
page.add(
    titled_card(
        title="Card Title",
        content="This is the card content",
        actions=[
            primary_button("Confirm"),
            secondary_button("Cancel")
        ]
    )
)

# Image card
page.add(
    image_card(
        image_src="https://picsum.photos/300/200",
        title="Image Title",
        content="This is the content of the image card"
    )
)

# Clickable card
def card_clicked(e):
    print("Card clicked")

page.add(
    clickable_card(
        content="Click me",
        on_click=card_clicked
    )
)
```

### Layout Components (layoutComponents.py)

Provides page layout and responsive design components:

- `ScrollablePage.create(...)` - Create scrollable page layout
- `scrollable_page(content, ...)` - Convenience function to create scrollable page layout
- `ResponsiveLayout.create(...)` - Create responsive layout container
- `responsive_layout(content, ...)` - Convenience function to create responsive layout container

Example:
```python
from BaseComponents import *

# Create scrollable page with alignment control
demo_content = [
    heading("Page Title"),
    body("Page content..."),
    # More content...
]

# Left aligned (default)
scrollable_content = scrollable_page(
    content=demo_content,
    horizontal_alignment=ft.CrossAxisAlignment.START
)

# Center aligned
scrollable_content_center = scrollable_page(
    content=demo_content,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
)

# Right aligned
scrollable_content_right = scrollable_page(
    content=demo_content,
    horizontal_alignment=ft.CrossAxisAlignment.END
)

page.add(scrollable_content)

# Create responsive layout
responsive_content = responsive_layout(
    content=ft.Text("Responsive content"),
    width=400,
    height=300
)
page.add(responsive_content)
```

## Theme System (themeManager.py)

Provides unified theme color management and automatic adaptation functionality.

### Theme Colors

Predefined color constants:
- PRIMARY - Primary color
- SECONDARY - Secondary color
- SUCCESS - Success color
- WARNING - Warning color
- ERROR - Error color
- BACKGROUND - Background color
- SURFACE - Surface color
- TEXT_PRIMARY - Primary text color
- TEXT_SECONDARY - Secondary text color

### Theme Functions

- `get_theme_colors()` - Get current theme color configuration
- `switch_theme(theme)` - Switch theme ("light" or "dark")
- `auto_detect_theme()` - Automatically detect system theme
- `themed_button(text, on_click=None, button_type="primary")` - Themed button
- `themed_text(text, text_type="body")` - Themed text
- `themed_container(content, container_type="card")` - Themed container

Example:
```python
from BaseComponents import *

# Automatically detect system theme
auto_detect_theme()

# Manually switch theme
switch_theme("dark")  # or "light"

# Using themed components
page.add(
    themed_button("Themed Button", button_type="success"),
    themed_text("Themed Text", text_type="heading"),
    themed_container(content)
)
```

## Usage

1. Import components:
```python
from BaseComponents import *
```

2. Use components in page:
```python
def main(page: ft.Page):
    # Set window size
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = True
    
    # Enable page scrolling
    page.scroll = ft.ScrollMode.AUTO
    
    page.add(
        heading("Welcome to BaseComponents"),
        body("This is a sample application"),
        primary_button("Click Me", on_click=lambda e: print("Click event"))
    )

ft.app(main)
```

## Automatic Theme Adaptation

BaseComponents supports automatically detecting the user's system theme settings (dark or light mode) and applying themes accordingly. This is implemented through the `darkdetect` library, which needs to be installed separately:

```bash
pip install darkdetect
```

At application startup, the theme manager will automatically detect the system theme and apply the corresponding color scheme.

## Custom Themes

You can customize the color scheme by modifying the [AppColors](file:///D:/GitHub/Source_Codes2/flet_basecomponents/BaseComponents/themeManager.py#L5-L43) class in [themeManager.py](file:///D:/GitHub/Source_Codes2/flet_basecomponents/BaseComponents/themeManager.py), or switch themes at runtime using the `switch_theme()` function.

## Window Size and Scrolling Features

BaseComponents now supports window size control and content scrolling features:

1. Set window size:
```python
page.window_width = 800
page.window_height = 600
page.window_resizable = True
```

2. Enable page scrolling:
```python
page.scroll = ft.ScrollMode.AUTO
```

3. Use scrollable layout components:
```python
content = [/* Your page content */]
# Left aligned (default)
scrollable_content = scrollable_page(
    content=content,
    horizontal_alignment=ft.CrossAxisAlignment.START
)
page.add(scrollable_content)
```

When the page content exceeds the window size, users can scroll to view all content. Alignment parameters can be used to control content alignment:
- `ft.CrossAxisAlignment.START` - Left align
- `ft.CrossAxisAlignment.CENTER` - Center align
- `ft.CrossAxisAlignment.END` - Right align

## LICENSE
Flet_BaseComponents was created under the [MIT License](LICENSE).

This project is built on the Flet framework, so please comply with Flet's license agreement: [Apache License 2.0](flet_LICENSE).