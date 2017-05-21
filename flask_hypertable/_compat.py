import sys

PY2 = sys.version_info[0] == 2

_identity = lambda x: x


if PY2:
    chr = chr
    text_type = str
    string_types = (str, str)
    integer_types = (int, int)
    from urllib.request import urlretrieve

    text_to_native = lambda s, enc: s.encode(enc)

    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

    from io import StringIO as BytesIO
    from io import StringIO
    import pickle as pickle
    import configparser as configparser

    
    range_type = xrange

    cmp = cmp

    input = raw_input
    from string import lower as ascii_lowercase
    import urllib.parse

    def console_to_str(s):
        return s.decode('utf_8')

    exec('def reraise(tp, value, tb=None):\n raise tp, value, tb')

else:
    chr = chr
    text_type = str
    string_types = (str,)
    integer_types = (int, )

    text_to_native = lambda s, enc: s

    iterkeys = lambda d: iter(list(d.keys()))
    itervalues = lambda d: iter(list(d.values()))
    iteritems = lambda d: iter(list(d.items()))

    from io import StringIO, BytesIO
    import pickle
    import configparser

    izip = zip
    imap = map
    range_type = range

    cmp = lambda a, b: (a > b) - (a < b)

    input = input
    from string import ascii_lowercase
    import urllib.parse as urllib
    import urllib.parse as urlparse
    from urllib.request import urlretrieve

    console_encoding = sys.__stdout__.encoding

    def console_to_str(s):
        """ From pypa/pip project, pip.backwardwardcompat. License MIT. """
        try:
            return s.decode(console_encoding)
        except UnicodeDecodeError:
            return s.decode('utf_8')

    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value
        raise value


number_types = integer_types + (float,)