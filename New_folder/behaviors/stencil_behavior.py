__all__ = ("StencilBehavior",)

from kivy.lang import Builder
from kivy.properties import VariableListProperty

Builder.load_string(
"""
#: import RelativeLayout kivy.uix.relativelayout.RelativeLayout

<StencilBehavior>
    canvas.before:
        StencilPush
        RoundedRectangle:
            pos: self.pos if not isinstance(self, RelativeLayout) else [0, 0]
            size: self.size
            radius: self.radius if hasattr(self, "radius") and len(self.radius) else [0, 0, 0, 0]
        StencilUse
    canvas.after:
        StencilUnUse
        RoundedRectangle:
            pos: self.pos if not isinstance(self, RelativeLayout) else [0, 0]
            size: self.size
            radius: self.radius if hasattr(self, "radius") and len(self.radius) else [0, 0, 0, 0]
        StencilPop
""", 
filename='stencil_bahvior.kv'
)


class StencilBehavior:
    """Base class for controlling the stencil instructions of the widget."""

    radius = VariableListProperty([0], length=4)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return True
            
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            return True
            
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if not self.collide_point(*touch.pos):
            return True
            
        super().on_touch_up(touch)
