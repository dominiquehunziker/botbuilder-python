# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PaymentOptions(Model):
    """Provides information about the options desired for the payment request.

    :param request_payer_name: Indicates whether the user agent should collect
     and return the payer's name as part of the payment request
    :type request_payer_name: bool
    :param request_payer_email: Indicates whether the user agent should
     collect and return the payer's email address as part of the payment
     request
    :type request_payer_email: bool
    :param request_payer_phone: Indicates whether the user agent should
     collect and return the payer's phone number as part of the payment request
    :type request_payer_phone: bool
    :param request_shipping: Indicates whether the user agent should collect
     and return a shipping address as part of the payment request
    :type request_shipping: bool
    :param shipping_type: If requestShipping is set to true, then the
     shippingType field may be used to influence the way the user agent
     presents the user interface for gathering the shipping address
    :type shipping_type: str
    """

    _attribute_map = {
        'request_payer_name': {'key': 'requestPayerName', 'type': 'bool'},
        'request_payer_email': {'key': 'requestPayerEmail', 'type': 'bool'},
        'request_payer_phone': {'key': 'requestPayerPhone', 'type': 'bool'},
        'request_shipping': {'key': 'requestShipping', 'type': 'bool'},
        'shipping_type': {'key': 'shippingType', 'type': 'str'},
    }

    def __init__(self, *, request_payer_name: bool=None, request_payer_email: bool=None, request_payer_phone: bool=None, request_shipping: bool=None, shipping_type: str=None, **kwargs) -> None:
        super(PaymentOptions, self).__init__(**kwargs)
        self.request_payer_name = request_payer_name
        self.request_payer_email = request_payer_email
        self.request_payer_phone = request_payer_phone
        self.request_shipping = request_shipping
        self.shipping_type = shipping_type
