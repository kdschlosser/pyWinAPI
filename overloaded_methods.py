# -*- coding: utf-8 -*-

import sys

PY3 = sys.version_info[0] >= 3

declared_overloads = {}


def _get_func_name(arg_names, arg_defaults):

    if len(arg_defaults) < len(arg_names):
        args = arg_names[:-len(arg_defaults)]
        arg_names = arg_names[-len(arg_defaults):]
    else:
        args = []

    for i, arg_name in enumerate(arg_names):
        arg_default = (
            str(type(arg_defaults[i])).split("'", 1)[1].rsplit("'")[0]
        )
        args += [arg_name + '=' + arg_default]

    return args


class _OverloadedMetaClass(type):

    def __new__(mcs, name, bases, dct):

        if declared_overloads:
            dct['__overloaded_funcs'] = {}

            for func_name, overloaded_funcs in declared_overloads.items():
                if func_name in dct:
                    del dct[func_name]

                for items in overloaded_funcs:
                    name = items[0]
                    wrapper = items[3]
                    dct[name] = wrapper

                dct['__overloaded_funcs'][func_name] = overloaded_funcs[:]

            declared_overloads.clear()

        return type.__new__(mcs, name, bases, dct)


def overload(func):
    arg_names = func.__code__.co_varnames
    arg_defaults = func.__defaults__

    if func.__name__ not in declared_overloads:
        declared_overloads[func.__name__] = []

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    if arg_names and arg_names[0] == 'self':
        arg_names =arg_names[1:]

    args = _get_func_name(arg_names, arg_defaults)

    wrapper.__name__ = 'overloaded_{0}({1})'.format(
        func.__name__,
        ', '.join(args)
    )

    declared_overloads[func.__name__] += [
        [wrapper.__name__, arg_names, arg_defaults, wrapper]
    ]

    return wrapper


class _OverloadedWrapper(object):

    def __init__(self, parent, name, funcs):
        self.parent = parent
        self.__name__ = name
        self.funcs = funcs

    def __call__(self, *args, **kwargs):

        for wrapper_name, arg_names, arg_defaults, wrapper in self.funcs:

            if len(args) + len(list(kwargs.keys())) != len(arg_names):
                continue

            if len(arg_defaults) != len(list(kwargs.keys())):
                continue

            kwarg_types = []

            arg_defaults = list(type(arg) for arg in arg_defaults)

            if len(arg_defaults) < len(arg_names):
                keyword_names = arg_names[-len(arg_defaults):]
            else:
                keyword_names = arg_names

            for name in keyword_names:
                if name in kwargs:
                    kwarg_types += [type(kwargs[name])]

            if kwarg_types != arg_defaults:
                continue

            return getattr(self.parent, wrapper_name)(*args, **kwargs)


if PY3:
    class OverloadedClass(object, metaclass=_OverloadedMetaClass):

        def __getattr__(self, item):
            if item in self.__dict__:
                return self.__dict__[item]

            if '__overloaded_funcs' in self.__class__.__dict__:
                if item in self.__class__.__dict__['__overloaded_funcs']:
                    return _OverloadedWrapper(
                        self,
                        item,
                        self.__class__.__dict__['__overloaded_funcs'][item]
                    )

            if item in self.__class__.__dict__:
                return self.__class__.__dict__[item]

            raise AttributeError(item)

else:
    class OverloadedClass(object):
        __metaclass__ = _OverloadedMetaClass

        def __getattr__(self, item):
            if item in self.__dict__:
                return self.__dict__[item]

            if '__overloaded_funcs' in self.__class__.__dict__:
                if item in self.__class__.__dict__['__overloaded_funcs']:
                    return _OverloadedWrapper(
                        self,
                        item,
                        self.__class__.__dict__['__overloaded_funcs'][item]
                    )

            if item in self.__class__.__dict__:
                return self.__class__.__dict__[item]

raise AttributeError(item)
