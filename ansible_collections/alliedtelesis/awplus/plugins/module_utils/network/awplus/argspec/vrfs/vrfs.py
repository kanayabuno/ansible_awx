#
# -*- coding: utf-8 -*-
# Copyright 2021 Allied Telesis
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the awplus_vrfs module
"""


class VrfsArgs(object):  # pylint: disable=R0903
    """The arg spec for the awplus_vrfs module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'elements': 'dict',
                     'options': {'description': {'type': 'str'},
                                 'export_map': {'type': 'str'},
                                 'id': {'required': True, 'type': 'str'},
                                 'import_map': {},
                                 'max_fib_routes': {'type': 'str'},
                                 'max_fib_routes_warning': {'type': 'str'},
                                 'max_static_routes': {'type': 'str'},
                                 'name': {'required': True, 'type': 'str'},
                                 'rd': {'type': 'str'},
                                 'route_target': {'options': {'direction': {'choices': ['import',
                                                                                        'export',
                                                                                        'both'],
                                                                            'type': 'str'},
                                                              'target': {'type': 'str'}},
                                                  'type': 'list'},
                                'router_id': {'type': 'str'}},
                                'type': 'list'},
                     'state': {'choices': ['merged', 'replaced', 'overridden', 'deleted'],
                               'default': 'merged',
                               'type': 'str'}}  # pylint: disable=C0301