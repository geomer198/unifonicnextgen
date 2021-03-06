"""
    unifonicnextgen

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from unifonicnextgen.configuration import Configuration
from unifonicnextgen.controllers.rest_controller import RestController
from unifonicnextgen.controllers.wrapper_controller import WrapperController
from unifonicnextgen.decorators import lazy_property


class UnifonicnextgenClient(object):

    config = Configuration

    @lazy_property
    def rest(self):
        return RestController()

    @lazy_property
    def wrapper(self):
        return WrapperController()

    def __init__(self, basic_auth_user_name=None, basic_auth_password=None):
        if basic_auth_user_name is not None:
            Configuration.basic_auth_user_name = basic_auth_user_name
        if basic_auth_password is not None:
            Configuration.basic_auth_password = basic_auth_password
