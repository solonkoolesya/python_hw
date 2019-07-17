# bencoding
# http://www.bittorrent.org/beps/bep_0003.html
import re
from  collections import OrderedDict

def encode(val):
  if type(val) is bytes:
    return str.encode(str(len(val)))+b':'+val

  elif type(val) is int:
    return str.encode('i'+str(val)+'e')

  elif type(val) is str:
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
        raise ValueError('invalid type for dict key, not bytestring\string: {}'.format(type(key)))
    return(b'd'+res+b'e')


def decode(val):
    val_dec = val.decode()

    def decode_inner(val):
        re_str = re.match(r"^(\d+):(\w*)", val)
        re_int = re.match(r"^i(-?\d+)e", val)
        re_list = re.match(r"^l(.*)e", val)
        re_dict = re.match(r"^d(.*)e", val)

        if re_str:
            res = re_str.group(1)
            return str.encode(val.split(':')[1][:int(res)]), val[int(res)+2:]

        if re_int:
            res = re_int.group(1)
            end_index = re_int.span()[1]
            if len(res) > 1 and res[0] == '0':
                raise ValueError('invalid literal for int() with base 0: {}'.format(res))
            else:
                return int(res), val[end_index:]

        if re_list:
            res = []
            content = re_list.group(1)
            end_index = re_list.span()[1]
            while content:
                a, b = decode_inner(content)
                res.append(a)
                content = b
            return res, val[end_index:]

        if re_dict:
            res = {}
            content = re_dict.group(1)
            end_index = re_dict.span()[1]
            while content:
                if content[0].isdigit():
                    a1, b1 = decode_inner(content)
                    res.update({a1: None})
                    a2, b2 = decode_inner(b1)
                    res[a1], content = a2, b2
            return OrderedDict(res), val[end_index:]

    return decode_inner(val_dec)[0]
	
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)
