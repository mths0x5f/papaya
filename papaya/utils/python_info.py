import json
import platform
import sys
import sysconfig


def _version_str_to_tuple(string):
    """ Convert version string of format x.y.z to a tuple """
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
    if sys.implementation.name == "pypy":  # new in Python 3.3
        return sys.pypy_version_info[:3]
    else:
        return sys.implementation.version[:3]


def _get_python_impl_target_platform():
    """ Get the value for implementation target platform """
    return sysconfig.get_platform()  # sysconfig is the way to go


def _get_python_package_namespace():
    return 'python{}+{}{}+{}'.format('%d.%d' % _get_python_version()[:2],
                                     _get_python_impl_name(),
                                     '%d.%d' % _get_python_impl_version()[:2],
                                     _get_python_impl_target_platform())


def get_python_info():
    return {
        'python': {
            'version': _get_python_version(),
            'implementation': {
                'name': _get_python_impl_name(),
                'version': _get_python_impl_version(),
                'platform': _get_python_impl_target_platform()
            },
            'package_namespace': _get_python_package_namespace()
        }
    }


if __name__ == '__main__':
    print(json.dumps(get_python_info(), separators=(',', ':')))
