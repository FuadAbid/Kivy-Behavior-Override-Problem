from __future__ import annotations

__all__ = ("BackgroundBehavior",)

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import (
    ColorProperty,
    VariableListProperty, 
    StringProperty,
)

Builder.load_string("""
#: import RelativeLayout kivy.uix.relativelayout.RelativeLayout


<BackgroundBehavior>
    canvas.before:
        Color:
            rgba: self._bg_color
        SmoothRoundedRectangle:
            size: self.size
            pos: self.pos if not isinstance(self, RelativeLayout) else (0, 0)
            radius: self.radius
            source: self.background
""", 
filename='background_bahvior.kv'
)


class BackgroundBehavior:
    background = StringProperty()
    radius = VariableListProperty([0, 0, 0, 0])
    bg_color = ColorProperty()

    _bg_color = ColorProperty([0, 0, 0, 0])

    def on_bg_color(self, instance, color: list | str):
        """Fired when the values of :attr:`bg_color` change."""
        
        if (
            hasattr(self, "theme_cls")
            and self.theme_cls.theme_style_switch_animation
            and self.__class__.__name__ != "MDDropdownMenu"
        ):
            Animation(
                _bg_color=color,
                d=self.theme_cls.theme_style_switch_animation_duration,
                t="linear",
            ).start(self)
        
        else:
            self._bg_color = color