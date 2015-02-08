"""
Store color names and get custom names according to env
"""

import os


VAR_CUSTOM  = 'COLORPRINT_CUSTOM'
VAR_DEFAULT = 'COLORPRINT_DEFAULT'

BASIC_MAPPING = {
    'reset':              (0,),
    'bold':               (1,),
    'bright':             (1,),
    'dim':                (2,),
    'underscore':         (4,),
    'underlined':         (4,),
    'blink':              (5,),
    'reverse':            (7,),
    'hidden':             (8,),
    'black':              (30,),
    'red':                (31,),
    'green':              (32,),
    'yellow':             (33,),
    'blue':               (34,),
    'magenta':            (35,),
    'purple':             (35,),
    'cyan':               (36,),
    'white':              (37,),
    'bgblack':            (40,),
    'bgred':              (41,),
    'bggreen':            (42,),
    'bgyellow':           (43,),
    'bgblue':             (44,),
    'bgmagenta':          (45,),
    'bgpurple':           (45,),
    'bgcyan':             (46,),
    'bgwhite':            (47,),
    }


def retrieve_custom_colors():
    mapping = BASIC_MAPPING
    var_custom = os.environ.get(VAR_CUSTOM)
    if var_custom is not None:
        try:
            '''
            Open file and parsing, then update `basic_mapping`
            If there is not such file or paring content failed, raise warning
            '''
        except OSError as e:
            Warning('can not open custom color file "%s"' % e.filename)
        except:
            Warning('parse custom color file failed')
    return mapping


class AttributeMapping(dict):
    retrieved = False

    def __getitem__(self, key):
        if not self.retrieved:
            self.update(retrieve_custom_colors())
            self.retrieved = True
        return super().__getitem__(key)


color_attr_mapping = AttributeMapping()
default_color = os.environ.get(VAR_DEFAULT, '')
