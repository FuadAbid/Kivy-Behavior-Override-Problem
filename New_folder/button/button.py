from New_folder.behaviors import (
    ShadowBehavior,
    BackgroundBehavior, 
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label

class FButton(
    ShadowBehavior,
    BackgroundBehavior, 
    ButtonBehavior, 
    Label, 
): ...