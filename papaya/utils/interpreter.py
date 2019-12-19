import os
import subprocess
import sys


def get_impl_tag(impl):
    return {
        'CPython': 'cp',
        'PyPy': 'pp',
        'IronPython': 'ip',
        'Jython': 'jy'
    }.get(impl, impl.lower())


def run_python_interpreter(executable=sys.executable,
                           arguments=None, environment=None):
    """  """
    arguments = arguments if arguments else list()
    environment = environment if environment else dict()

    environment.update({**os.environ})

    return subprocess.run([executable, *arguments], env=environment)
