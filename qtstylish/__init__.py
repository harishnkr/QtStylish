# Set version
from importlib.metadata import version
__version__ = version('qtstylish')

# Imports
from qtstylish.qtstylish import dark, light, ThemeSwitcher
from qtstylish.demo_widget import DemoWidget
from qtstylish.modern_window import ModernWindow

__all__ = ["dark", "light", "ThemeSwitcher",
           "DemoWidget", "ModernWindow", "__version__"]
