__all__ = ("ShadowBehavior",)

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    NumericProperty,
    VariableListProperty,
)

Builder.load_string(
"""
<ShadowBehavior>
    canvas.before:
        Color:
            rgba: self.shadow_color
        BoxShadow:
            pos: self.pos if not isinstance(self, RelativeLayout) else (0, 0)
            size: self.size
            blur_radius: self.shadow_size
""", 
filename='shadow_behavior.kv'
)


class ShadowBehavior:
    shadow_size = NumericProperty()
    shadow_radius = VariableListProperty([0], length=4)
    shadow_color = ColorProperty([0, 0, 0, 0.6])