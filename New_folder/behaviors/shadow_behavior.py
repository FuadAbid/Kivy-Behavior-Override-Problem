__all__ = ("ShadowBehavior",)

from kivy.lang import Builder
from kivy.properties import (
    NumericProperty,
)

Builder.load_string(
"""
<ShadowBehavior>
    canvas.before:
        Color:
            rgba: 0, 0, 0, .6
        BoxShadow:
            pos: self.pos if not isinstance(self, RelativeLayout) else (0, 0)
            size: self.size
            blur_radius: self.shadow_size
""", 
filename='shadow_behavior.kv'
)


class ShadowBehavior:
    shadow_size = NumericProperty()
