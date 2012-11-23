"""Contains setter functions designed to be used inline with
factory definitions to inject dynamic values into models as
and when they are built."""


class Sequence(object):
    def __init__(self):
        self.seq_num = 0

    def next(self):
        self.seq_num = self.seq_num + 1
        return self.seq_num


def sequence(fn):
    """Defines a sequential value for a factory attribute. On each successive
    invocation of this helper (i.e. when a new instance of a document is
    created by the enclosing factory) the given function is passed a
    sequentially incrementing number which should be used to return a dynamic
    value to be used on the model instance."""
    sequence = Sequence()

    def build(*args):
        return fn(sequence.next())
    return build


def dependent(fn):
    """Declares a value for a factory attribute which depends on other values
    in the document in order to be set. The given function or lambda is
    passed the document and should return the value to set."""
    def build(obj):
        return fn(obj)

    return build
