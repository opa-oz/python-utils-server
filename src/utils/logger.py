import time
from .bcolors import BColors


class Logger:
    def __init__(self, prefix='Untagged'):
        self.prefix = prefix.upper()

    def info(self, *args):
        ts = time.asctime()
        print(f'[{ts}]{BColors.GREEN}{BColors.BOLD}[{self.prefix}]:{BColors.END} ', *args)

    def error(self, *args):
        ts = time.asctime()
        print(f'[{ts}]{BColors.RED}{BColors.BOLD}[{self.prefix}]:{BColors.END} ', *args)

    def warn(self, *args):
        ts = time.asctime()
        print(f'[{ts}]{BColors.YELLOW}{BColors.BOLD}[{self.prefix}]:{BColors.END} ', *args)

    def debug(self, *args):
        ts = time.asctime()
        print(f'[{ts}]{BColors.BLUE}{BColors.BOLD}[{self.prefix}]:{BColors.END} ', *args)
