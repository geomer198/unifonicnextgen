"""
    unifonicnextgen

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from unifonicnextgen.api_helper import APIHelper
from unifonicnextgen.configuration import Configuration
from unifonicnextgen.controllers.base_controller import BaseController
from unifonicnextgen.exceptions.api_exception import APIException
from unifonicnextgen.http.auth.basic_auth import BasicAuth
from unifonicnextgen.models.get_message_query_response import GetMessageQueryResponse
from unifonicnextgen.models.send_wrapper_response import SendWrapperResponse


class WrapperController(BaseController):

    """A Controller to access Endpoints in the unifonicnextgen API."""

    def create_get_msg_query(self, appsid, msgid, to=None):
        """Does a POST request to /wrapper/msgQuery.

        Unifonic Get message query API allows you to get details of specified
        message.

        Args:
            appsid (string): A character string that uniquely identifies your
                app
            msgid (long|int): A unique ID that identifies a message
            to (long|int, optional): Destination mobile number, mobile numbers
                must be in international format without 00 or + Example:
                (4452023498)

        Returns:
            GetMessageQueryResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(appsid=appsid, msgid=msgid)

        # Prepare query URL
        _url_path = "/wrapper/msgQuery"
        _query_builder = Configuration.get_base_uri(Configuration.Server.BASE_URL)
        _query_builder += _url_path
        _query_parameters = {"appsid": appsid, "msgid": msgid, "to": to}
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder, _query_parameters, Configuration.array_serialization
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {"accept": "application/json"}

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException("Authentication failed", _context)
        elif _context.response.status_code == 402:
            raise APIException("Missing parameter AppSid", _context)
        elif _context.response.status_code == 432:
            raise APIException("MessageId must be numeric", _context)
        elif _context.response.status_code == 452:
            raise APIException(
                "User must specify either messageId or recipient parameter", _context
            )
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(
            _context.response.raw_body, GetMessageQueryResponse.from_dictionary
        )

    def create_send_message(
        self, appsid, msg, to, sender, base_encode=False, encoding="UCS2"
    ):
        """Does a POST request to /wrapper/sendSMS.php.

        Unifonic Send Wrapper API allows you to send  text messages to
        multiple users at the same time

        Args:
            appsid (string): A character string that uniquely identifies your
                app
            msg (string): Message body supports both English and unicodes
                characters, concatenated messages is supported
            to (long|int): Destination mobile number, mobile numbers must be
                in international format without 00 or + Example: (4452023498)
            sender (string): The SenderID to send from, App default SenderID
                is used unless else stated
            base_encode (bool, optional): Binary-to-text encoding schemes that
                represent binary data in an ASCII string format
            encoding (string, optional): Converts information from a source
                into symbols for communication or storage, GSM7 for English
                and UCS2 for Arabic

        Returns:
            SendWrapperResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(appsid=appsid, msg=msg, to=to, sender=sender)

        # Prepare query URL
        _url_path = "/wrapper/sendSMS.php"
        _query_builder = Configuration.get_base_uri(Configuration.Server.BASE_URL)
        _query_builder += _url_path
        _query_parameters = {
            "appsid": appsid,
            "msg": msg,
            "to": to,
            "sender": sender,
            "baseEncode": base_encode,
            "encoding": encoding,
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder, _query_parameters, Configuration.array_serialization
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {"accept": "application/json"}

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException("Authentication failed", _context)
        elif _context.response.status_code == 402:
            raise APIException("Missing parameter AppSid", _context)
        elif _context.response.status_code == 459:
            raise APIException(
                "Authentication parameters are incorrectly base64 encoded", _context
            )
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(
            _context.response.raw_body, SendWrapperResponse.from_dictionary
        )
