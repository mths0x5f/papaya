import json
import platform
import sys
import sysconfig


def _version_str_to_tuple(string):
    return tuple(int(n) for n in str(string).split('.'))


def _get_python_version():
    """ Get the language version as a tuple """
    # platform is the easiest place to get from
    return _version_str_to_tuple(platform.python_version())


def _get_python_impl_name():
    """ Get the implementation name in lowercase """
    return sys.implementation.name  # sys.implementation new in Python 3.3


def _get_python_impl_version():
    """ Get the implementation version as a tuple """
    # Some implementations may not honor sys.implementation
    # PyPy is one of them
    if sys.implementation.name == "pypy":
        return sys.pypy_version_info[:3]
    else:
        return sys.implementation.version[:3]  # new in Python 3.3


def _get_python_impl_target_platform():
    """ Get the value for implementation target platform """
    return sysconfig.get_platform()  # sysconfig is the way to go


def get_python_info():
    return {'python': {'version': _get_python_version(),
                       'impl': {
                           'name': _get_python_impl_name(),
                           'version': _get_python_impl_version(),
                           'platform': _get_python_impl_target_platform()
                       }}}


if __name__ == '__main__':
    print(json.dumps(get_python_info(), separators=(',', ':')))
