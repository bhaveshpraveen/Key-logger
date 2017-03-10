from pyxhook import HookManager
from keypress import OnKeyPress


def mainlin():
    hook = HookManager()
    hook.KeyDown = OnKeyPress
    hook.HookKeyboard()
    hook.start()