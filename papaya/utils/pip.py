import sys

from papaya.utils.interpreter import run_python_interpreter
from papaya.utils.path import get_python_packages_path
from papaya.utils.path import get_pythonpath


def pip_install(packages, arguments=None):
    arguments = arguments if arguments else []

    return run_python_interpreter(sys.executable, [
        '-m', 'pip', 'install',
        '--target', get_python_packages_path(),
        '--no-deps',
        *arguments,
        *packages
    ], {'PYTHONPATH': get_pythonpath()})
