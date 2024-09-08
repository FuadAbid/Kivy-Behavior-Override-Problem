__all__ = ("BackgroundBehavior",)

from kivy.lang import Builder
from kivy.properties import (
    ColorProperty,
    VariableListProperty, 
)

Builder.load_string("""
#: import RelativeLayout kivy.uix.relativelayout.RelativeLayout


<BackgroundBehavior>
    canvas.before:
        Color:
            rgba: self.bg_color
        SmoothRoundedRectangle:
            size: self.size
            pos: self.pos if not isinstance(self, RelativeLayout) else (0, 0)
            radius: self.radius

""", 
filename='background_bahvior.kv'
)


class BackgroundBehavior:
    radius = VariableListProperty([0,])
    bg_color = ColorProperty([0, 0, 0, 0])
