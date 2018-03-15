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


class ReceiptCard(Model):
    """A receipt card.

    :param title: Title of the card
    :type title: str
    :param items: Array of Receipt Items
    :type items: list[~botframework.connector.models.ReceiptItem]
    :param facts: Array of Fact Objects   Array of key-value pairs.
    :type facts: list[~botframework.connector.models.Fact]
    :param tap: This action will be activated when user taps on the card
    :type tap: ~botframework.connector.models.CardAction
    :param total: Total amount of money paid (or should be paid)
    :type total: str
    :param tax: Total amount of TAX paid(or should be paid)
    :type tax: str
    :param vat: Total amount of VAT paid(or should be paid)
    :type vat: str
    :param buttons: Set of actions applicable to the current card
    :type buttons: list[~botframework.connector.models.CardAction]
    """

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'items': {'key': 'items', 'type': '[ReceiptItem]'},
        'facts': {'key': 'facts', 'type': '[Fact]'},
        'tap': {'key': 'tap', 'type': 'CardAction'},
        'total': {'key': 'total', 'type': 'str'},
        'tax': {'key': 'tax', 'type': 'str'},
        'vat': {'key': 'vat', 'type': 'str'},
        'buttons': {'key': 'buttons', 'type': '[CardAction]'},
    }

    def __init__(self, *, title: str=None, items=None, facts=None, tap=None, total: str=None, tax: str=None, vat: str=None, buttons=None, **kwargs) -> None:
        super(ReceiptCard, self).__init__(**kwargs)
        self.title = title
        self.items = items
        self.facts = facts
        self.tap = tap
        self.total = total
        self.tax = tax
        self.vat = vat
        self.buttons = buttons
