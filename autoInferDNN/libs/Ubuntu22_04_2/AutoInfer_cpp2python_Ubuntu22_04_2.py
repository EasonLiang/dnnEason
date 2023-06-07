# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _AutoInfer_cpp2python_Ubuntu22_04_2
else:
    import _AutoInfer_cpp2python_Ubuntu22_04_2

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _AutoInfer_cpp2python_Ubuntu22_04_2.delete_SwigPyIterator

    def value(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator_equal(self, x)

    def copy(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator_copy(self)

    def next(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator_next(self)

    def __next__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator___next__(self)

    def previous(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator_previous(self)

    def advance(self, n):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _AutoInfer_cpp2python_Ubuntu22_04_2:
_AutoInfer_cpp2python_Ubuntu22_04_2.SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector___nonzero__(self)

    def __bool__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector___bool__(self)

    def __len__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector___setitem__(self, *args)

    def pop(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_pop(self)

    def append(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_append(self, x)

    def empty(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_empty(self)

    def size(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_size(self)

    def swap(self, v):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_swap(self, v)

    def begin(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_begin(self)

    def end(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_end(self)

    def rbegin(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_rbegin(self)

    def rend(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_rend(self)

    def clear(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_clear(self)

    def get_allocator(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_get_allocator(self)

    def pop_back(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_pop_back(self)

    def erase(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_erase(self, *args)

    def __init__(self, *args):
        _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_swiginit(self, _AutoInfer_cpp2python_Ubuntu22_04_2.new_IntVector(*args))

    def push_back(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_push_back(self, x)

    def front(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_front(self)

    def back(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_back(self)

    def assign(self, n, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_resize(self, *args)

    def insert(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_insert(self, *args)

    def reserve(self, n):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_reserve(self, n)

    def capacity(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_capacity(self)
    __swig_destroy__ = _AutoInfer_cpp2python_Ubuntu22_04_2.delete_IntVector

# Register IntVector in _AutoInfer_cpp2python_Ubuntu22_04_2:
_AutoInfer_cpp2python_Ubuntu22_04_2.IntVector_swigregister(IntVector)

class UInt32Vector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector___nonzero__(self)

    def __bool__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector___bool__(self)

    def __len__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector___len__(self)

    def __getslice__(self, i, j):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector___setitem__(self, *args)

    def pop(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_pop(self)

    def append(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_append(self, x)

    def empty(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_empty(self)

    def size(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_size(self)

    def swap(self, v):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_swap(self, v)

    def begin(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_begin(self)

    def end(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_end(self)

    def rbegin(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_rbegin(self)

    def rend(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_rend(self)

    def clear(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_clear(self)

    def get_allocator(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_get_allocator(self)

    def pop_back(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_pop_back(self)

    def erase(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_erase(self, *args)

    def __init__(self, *args):
        _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_swiginit(self, _AutoInfer_cpp2python_Ubuntu22_04_2.new_UInt32Vector(*args))

    def push_back(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_push_back(self, x)

    def front(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_front(self)

    def back(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_back(self)

    def assign(self, n, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_assign(self, n, x)

    def resize(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_resize(self, *args)

    def insert(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_insert(self, *args)

    def reserve(self, n):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_reserve(self, n)

    def capacity(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_capacity(self)
    __swig_destroy__ = _AutoInfer_cpp2python_Ubuntu22_04_2.delete_UInt32Vector

# Register UInt32Vector in _AutoInfer_cpp2python_Ubuntu22_04_2:
_AutoInfer_cpp2python_Ubuntu22_04_2.UInt32Vector_swigregister(UInt32Vector)

class StringVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector___nonzero__(self)

    def __bool__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector___bool__(self)

    def __len__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector___len__(self)

    def __getslice__(self, i, j):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector___setitem__(self, *args)

    def pop(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_pop(self)

    def append(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_append(self, x)

    def empty(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_empty(self)

    def size(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_size(self)

    def swap(self, v):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_swap(self, v)

    def begin(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_begin(self)

    def end(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_end(self)

    def rbegin(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_rbegin(self)

    def rend(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_rend(self)

    def clear(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_clear(self)

    def get_allocator(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_get_allocator(self)

    def pop_back(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_pop_back(self)

    def erase(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_erase(self, *args)

    def __init__(self, *args):
        _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_swiginit(self, _AutoInfer_cpp2python_Ubuntu22_04_2.new_StringVector(*args))

    def push_back(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_push_back(self, x)

    def front(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_front(self)

    def back(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_back(self)

    def assign(self, n, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_assign(self, n, x)

    def resize(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_resize(self, *args)

    def insert(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_insert(self, *args)

    def reserve(self, n):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_reserve(self, n)

    def capacity(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_capacity(self)
    __swig_destroy__ = _AutoInfer_cpp2python_Ubuntu22_04_2.delete_StringVector

# Register StringVector in _AutoInfer_cpp2python_Ubuntu22_04_2:
_AutoInfer_cpp2python_Ubuntu22_04_2.StringVector_swigregister(StringVector)

class FloatVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector___nonzero__(self)

    def __bool__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector___bool__(self)

    def __len__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector___len__(self)

    def __getslice__(self, i, j):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector___setitem__(self, *args)

    def pop(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_pop(self)

    def append(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_append(self, x)

    def empty(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_empty(self)

    def size(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_size(self)

    def swap(self, v):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_swap(self, v)

    def begin(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_begin(self)

    def end(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_end(self)

    def rbegin(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_rbegin(self)

    def rend(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_rend(self)

    def clear(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_clear(self)

    def get_allocator(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_get_allocator(self)

    def pop_back(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_pop_back(self)

    def erase(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_erase(self, *args)

    def __init__(self, *args):
        _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_swiginit(self, _AutoInfer_cpp2python_Ubuntu22_04_2.new_FloatVector(*args))

    def push_back(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_push_back(self, x)

    def front(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_front(self)

    def back(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_back(self)

    def assign(self, n, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_assign(self, n, x)

    def resize(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_resize(self, *args)

    def insert(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_insert(self, *args)

    def reserve(self, n):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_reserve(self, n)

    def capacity(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_capacity(self)
    __swig_destroy__ = _AutoInfer_cpp2python_Ubuntu22_04_2.delete_FloatVector

# Register FloatVector in _AutoInfer_cpp2python_Ubuntu22_04_2:
_AutoInfer_cpp2python_Ubuntu22_04_2.FloatVector_swigregister(FloatVector)

class DoubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector___bool__(self)

    def __len__(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_pop(self)

    def append(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_append(self, x)

    def empty(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_empty(self)

    def size(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_size(self)

    def swap(self, v):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_swap(self, v)

    def begin(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_begin(self)

    def end(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_end(self)

    def rbegin(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_rbegin(self)

    def rend(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_rend(self)

    def clear(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_clear(self)

    def get_allocator(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_swiginit(self, _AutoInfer_cpp2python_Ubuntu22_04_2.new_DoubleVector(*args))

    def push_back(self, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_push_back(self, x)

    def front(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_front(self)

    def back(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_back(self)

    def assign(self, n, x):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_reserve(self, n)

    def capacity(self):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_capacity(self)
    __swig_destroy__ = _AutoInfer_cpp2python_Ubuntu22_04_2.delete_DoubleVector

# Register DoubleVector in _AutoInfer_cpp2python_Ubuntu22_04_2:
_AutoInfer_cpp2python_Ubuntu22_04_2.DoubleVector_swigregister(DoubleVector)

input_i1 = _AutoInfer_cpp2python_Ubuntu22_04_2.input_i1
input_i2 = _AutoInfer_cpp2python_Ubuntu22_04_2.input_i2
output_o1 = _AutoInfer_cpp2python_Ubuntu22_04_2.output_o1
output_o2 = _AutoInfer_cpp2python_Ubuntu22_04_2.output_o2
PRECISION = _AutoInfer_cpp2python_Ubuntu22_04_2.PRECISION
MAGIC_EXCLUDE_double = _AutoInfer_cpp2python_Ubuntu22_04_2.MAGIC_EXCLUDE_double

def actvFunSigmoid(_in):
    return _AutoInfer_cpp2python_Ubuntu22_04_2.actvFunSigmoid(_in)

def actvFunTanH(_in):
    return _AutoInfer_cpp2python_Ubuntu22_04_2.actvFunTanH(_in)

def derivativeCalc(funPtr, fun_in):
    return _AutoInfer_cpp2python_Ubuntu22_04_2.derivativeCalc(funPtr, fun_in)

def getActivationFun(funName):
    return _AutoInfer_cpp2python_Ubuntu22_04_2.getActivationFun(funName)
class Eason(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _AutoInfer_cpp2python_Ubuntu22_04_2.Eason_swiginit(self, _AutoInfer_cpp2python_Ubuntu22_04_2.new_Eason())
    __swig_destroy__ = _AutoInfer_cpp2python_Ubuntu22_04_2.delete_Eason
    input = property(_AutoInfer_cpp2python_Ubuntu22_04_2.Eason_input_get, _AutoInfer_cpp2python_Ubuntu22_04_2.Eason_input_set)
    target_output = property(_AutoInfer_cpp2python_Ubuntu22_04_2.Eason_target_output_get, _AutoInfer_cpp2python_Ubuntu22_04_2.Eason_target_output_set)

    def setWeightBias(self, weights_h1n2_in, bias_h1n2_in, weights_end_in, bias_end_in, learning_rate_in):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.Eason_setWeightBias(self, weights_h1n2_in, bias_h1n2_in, weights_end_in, bias_end_in, learning_rate_in)

    def setInput_TargetOutput(self, input, target_output):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.Eason_setInput_TargetOutput(self, input, target_output)

    def train(self, turns=20, logOut=True, autoTrain=False, mse_threshold=0.0):
        return _AutoInfer_cpp2python_Ubuntu22_04_2.Eason_train(self, turns, logOut, autoTrain, mse_threshold)

# Register Eason in _AutoInfer_cpp2python_Ubuntu22_04_2:
_AutoInfer_cpp2python_Ubuntu22_04_2.Eason_swigregister(Eason)



