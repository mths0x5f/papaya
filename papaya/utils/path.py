import os
import sys
import sysconfig

from papaya.utils.interpreter import get_impl_tag

_PYTHON_PACKAGES_DIRNAME = 'python-packages'


def find_executable(executable, path=os.environ['PATH']):
    """ Find the path of a named executable. """
    paths = path.split(os.pathsep)
    ext_list = ['']

    if sys.platform == 'win32':
        path_ext = os.environ['PATHEXT'].lower().split(os.pathsep)
        _, ext = os.path.splitext(executable)
        if ext.lower() not in path_ext:
            ext_list = path_ext

    for ext in ext_list:
        exec_name = executable + ext
        for p in paths:
            f = os.path.join(p, exec_name)
            if os.path.isfile(f):
                return f

    return None


def get_python_packages_path(base_path='.',
                             ver=sysconfig.get_python_version(),
                             impl_tag=get_impl_tag('CPython'),
                             impl_ver=sysconfig.get_python_version(),
                             platform=sysconfig.get_platform()):
    """ Get value for use as PYTHONPATH of the packages directory path.

    Keyword arguments:
        base_path: Base path for the directory, default: cwd
        ver: Python language version, default: caller Python version
        impl_tag: Tag of Python implementation, default: CPython tag,
            (this is completely arbitrary)
        impl_ver: Version of Python implementation, default: caller
            Python version (again this is completely arbitrary)
        platform: Platform info (OS name, version and interpreter arch),
            default: caller execution of sysconfig.get_platform()
            (architecture meaning returned by this method is dependent
            of platform specifics)
    """
    base_path = os.path.abspath(base_path)
    python = ('py{}-{}{}-{}'.format(ver, impl_tag, impl_ver, platform))

    return os.path.join(base_path, _PYTHON_PACKAGES_DIRNAME, python)


def get_pythonpath(**kwargs):
    """ Get value for use as PYTHONPATH, including user definition.
    For generation of the packages directory path, this function accepts
    all keywords arguments of get_python_packages_path.
    """
    paths = [get_python_packages_path(**kwargs)]
    if os.environ.get('PYTHONPATH'):
        paths.insert(0, os.environ.get('PYTHONPATH'))

    return os.path.pathsep.join(paths)
