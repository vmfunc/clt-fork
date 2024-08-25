from subprocess import call
import sys


def exec_script(path):
    try:
        call([sys.executable, path])
    except Exception as e:
        return e
