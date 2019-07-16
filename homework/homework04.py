# bencoding
# http://www.bittorrent.org/beps/bep_0003.html

"""
Strings are length-prefixed base ten followed by a colon and the string.
For example 4:spam corresponds to 'spam'.

>>> encode(b'spam')
b'4:spam'

Integers are represented by an 'i' followed by the number in base 10 followed by an 'e'.
For example i3e corresponds to 3 and i-3e corresponds to -3.
Integers have no size limitation. i-0e is invalid.
All encodings with a leading zero, such as i03e, are invalid,
other than i0e, which of course corresponds to 0.

>>> decode(b'i3e')
3
>>> decode(b'i-3e')
-3
>>> decode(b'i0e')
0
>>> decode(b'i03e')
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 0: '03'
 

Lists are encoded as an 'l' followed by their elements (also bencoded) followed by an 'e'.
For example l4:spam4:eggse corresponds to ['spam', 'eggs'].

>>> decode(b'l4:spam4:eggse')
[b'spam', b'eggs']

Dictionaries are encoded as a 'd' followed by a list of alternating keys
and their corresponding values followed by an 'e'.
For example, d3:cow3:moo4:spam4:eggse corresponds to {'cow': 'moo', 'spam': 'eggs'}
Keys must be strings and appear in sorted order (sorted as raw strings, not alphanumerics).

>>> decode(b'd3:cow3:moo4:spam4:eggse')
OrderedDict([(b'cow', b'moo'), (b'spam', b'eggs')])

"""
def encode(val):
  if type(val) is bytes:
    return str.encode(str(len(val)))+b':'+val

  elif type(val) is int:    
    return str.encode('i'+str(val)+'e')

  elif type(val) is str: 
    if val.isdigit():
      #number which start with 0 
      if val.startswith('0') and len(val) > 1:
        raise ValueError('invalid literal for int() with base 0: {}'.format(val))
      #regular digit, just in string
      return str.encode('i'+str(val)+'e')
    #negative digit in string
    elif val.lstrip('-').isdigit():
      return str.encode('i'+str(val)+'e')
    return str.encode(str(len(val))+':'+val)

  if type(val) is list:
    res = b''
    for i in val:
      res += encode(i)
    return (b'l'+res+b'e')
  
  if type(val) is dict:
    res = b''
    for key in sorted(val.keys()):
      if type(key) in (bytes, str):
        res += encode(key)+encode(val[key])
      else:
        raise ValueError('invalid type for dict key, not bytes: {}'.format(type(key)))
    return(b'd'+res+b'e')


def decode(val):
    re_str = re.match(r"^(\d+):(\w*)", val)
    re_int = re.match(r"^i(-?\d+)e", val)
    re_list = re.match(r"^l(.*)e", val)
    re_dict = re.match(r"^d(.*)e", val)

    if re_str:
        return val.split(':')[1][:int(re_str.group(1))], val[int(re_str.group(1))+2:]

    if re_int:
        return re_int.group(1), val[re_int.span()[1]:]

    if re_list:
        res = []
        list = re_list.group(1)
        while list:
            a, b = decode(list)
            res.append(a)
            list = b
        return res, val[re_list.span()[1]:]

    if re_dict:
        res = {}
        content = re_dict.group(1)
        while content:
            if content[0].isdigit():
                a1, b1 = decode(content)
                res.update({a1: None})
                a2, b2 = decode(b1)
                res[a1] = a2
                content = b2
        return res, val[re_dict.span()[1]:]
        
	
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)
