#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class ThriftJSONEncoder(json.JSONEncoder):

    def default(self, o):
        if not hasattr(o, 'thrift_spec'):
            return super(ThriftJSONEncoder, self).default(o)

        spec = getattr(o, 'thrift_spec')
        ret = {}
        for field in spec:
            if field is None:
                continue
            (tag, field_ttype, field_name, field_ttype_info, default) = field
            if field_name in o.__dict__:
                val = o.__dict__[field_name]
                if val != default:
                    ret[field_name] = val
        return ret


def thrift2json(obj):
    return json.dumps(obj, cls=ThriftJSONEncoder)


def thrift2dict(obj):
    str = thrift2json(obj)
    return json.loads(str)
