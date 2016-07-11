#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from thrift.Thrift import TType


class ThriftJSONDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        self._thrift_class = kwargs.pop('thrift_class')
        super(ThriftJSONDecoder, self).__init__(*args, **kwargs)

    def decode(self, json_str):
        if isinstance(json_str, dict):
            dct = json_str
        else:
            dct = super(ThriftJSONDecoder, self).decode(json_str)
        return self._convert(dct, TType.STRUCT,
                             (self._thrift_class, self._thrift_class.thrift_spec))

    def _convert(self, val, ttype, ttype_info):
        if ttype == TType.STRUCT:
            (thrift_class, thrift_spec) = ttype_info
            ret = thrift_class()
            for field in thrift_spec:
                if field is None:
                    continue
                (tag, field_ttype, field_name, field_ttype_info, dummy) = field
                if field_name not in val:
                    continue
                converted_val = self._convert(val[field_name], field_ttype, field_ttype_info)
                setattr(ret, field_name, converted_val)
        elif ttype == TType.LIST:
            (element_ttype, element_ttype_info) = ttype_info
            ret = [self._convert(x, element_ttype, element_ttype_info) for x in val]
        elif ttype == TType.SET:
            (element_ttype, element_ttype_info) = ttype_info
            ret = set([self._convert(x, element_ttype, element_ttype_info) for x in val])
        elif ttype == TType.MAP:
            (key_ttype, key_ttype_info, val_ttype, val_ttype_info) = ttype_info
            ret = dict([(self._convert(k, key_ttype, key_ttype_info),
                         self._convert(v, val_ttype, val_ttype_info)) for (k, v) in val.iteritems()])
        elif ttype == TType.STRING:
            if isinstance(val, unicode):
                ret = val.encode("utf8")
            else:
                ret = str(val)
        elif ttype == TType.DOUBLE:
            ret = float(val)
        elif ttype == TType.I64:
            ret = long(val)
        elif ttype == TType.I32 or ttype == TType.I16 or ttype == TType.BYTE:
            ret = int(val)
        elif ttype == TType.BOOL:
            ret = bool(val)
        else:
            raise TypeError('Unrecognized thrift field type: %d' % ttype)
        return ret


def json2thrift(json_str, thrift_class):
    return json.loads(json_str, cls=ThriftJSONDecoder, thrift_class=thrift_class)

dict2thrift = json2thrift
