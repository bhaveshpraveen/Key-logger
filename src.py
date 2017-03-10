import pyxhook
import sys
import mainlin


platform = sys.platform

if __name__ == '__main__' and platform == 'linux' or platform == 'linux2':
    mainlin.mainlin()

