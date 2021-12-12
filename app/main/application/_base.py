# -*- encoding: utf-8 -*-

from flask_restful import reqparse, Resource

from ...utils import ResponseFormatter

class BaseResource(Resource):
    """Base Class for Master Tables"""

    def __init__(self):
        # default constructor
        self.formatter  = ResponseFormatter() # format response
        self.req_parser = reqparse.RequestParser() # parse incoming params


    @property
    def args(self):
        """Return all Request Parser Arguments"""

        return self.req_parser.parse_args()
