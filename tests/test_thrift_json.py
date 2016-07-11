#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_thrift_json
----------------------------------

Tests for `thrift_json` module.
"""
import json
import unittest

from thrift_json import json2thrift, dict2thrift, thrift2json, thrift2dict

from .features import ttypes


class TestThriftJSON(unittest.TestCase):

    def test_to_thrift(self):
        expired_at = 100000
        feature = ttypes.Feature()
        feature.name = "new search"
        feature.key = "new_search"
        feature.expired_at = expired_at
        feature.on = True
        path1 = [ttypes.Filter("device.version", "==", json.dumps("ios9.0")),
                 ttypes.Filter("device.city", "in", json.dumps(["北京", "厦门"]))]
        branch1 = ttypes.Branch()
        branch1.path = path1
        branch1.volume = 100
        leaf1 = [ttypes.Flag("versionA", 20), ttypes.Flag("versionB", 40)]
        branch1.leaf = leaf1
        feature.tree = [branch1]

        feature_dct = {
            'name': 'new search',
            'key': 'new_search',
            'on': True,
            'expired_at': expired_at,
            'tree': [
                {
                    'path': [
                        {'attr': 'device.version', 'op': '==', 'val': json.dumps("ios9.0")},
                        {'attr': 'device.city', 'op': 'in', 'val': json.dumps(['北京', '厦门'])},
                    ],
                    'volume': 100,
                    'leaf': [
                        {'name': 'versionA', 'weight': 20},
                        {'name': 'versionB', 'weight': 40},
                    ]

                }
            ]
        }
        feature1 = dict2thrift(feature_dct, ttypes.Feature)
        assert feature1 == feature
        feature2 = json2thrift(json.dumps(feature_dct), ttypes.Feature)
        assert feature2 == feature1

    def test_from_thrift(self):
        expired_at = 100000
        feature = ttypes.Feature()
        feature.name = "new search"
        feature.key = "new_search"
        feature.expired_at = expired_at
        feature.on = True
        path1 = [ttypes.Filter("device.version", "==", json.dumps("ios9.0")),
                 ttypes.Filter("device.city", "in", json.dumps(["北京", "厦门"]))]
        branch1 = ttypes.Branch()
        branch1.path = path1
        branch1.volume = 100
        leaf1 = [ttypes.Flag("versionA", 20), ttypes.Flag("versionB", 40)]
        branch1.leaf = leaf1
        feature.tree = [branch1]
        feature_dct = thrift2dict(feature)
        assert feature_dct['key'] == feature.key
