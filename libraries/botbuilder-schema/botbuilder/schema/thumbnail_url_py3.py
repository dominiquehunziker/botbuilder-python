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


class ThumbnailUrl(Model):
    """Thumbnail URL.

    :param url: URL pointing to the thumbnail to use for media content
    :type url: str
    :param alt: HTML alt text to include on this thumbnail image
    :type alt: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'alt': {'key': 'alt', 'type': 'str'},
    }

    def __init__(self, *, url: str=None, alt: str=None, **kwargs) -> None:
        super(ThumbnailUrl, self).__init__(**kwargs)
        self.url = url
        self.alt = alt
