# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental MediaTailor"
prefix = "mediatailor"


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource="", region="", account=""):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region, account=account)


DeletePlaybackConfiguration = Action("DeletePlaybackConfiguration")
GetPlaybackConfiguration = Action("GetPlaybackConfiguration")
ListPlaybackConfigurations = Action("ListPlaybackConfigurations")
ListTagsForResource = Action("ListTagsForResource")
PutPlaybackConfiguration = Action("PutPlaybackConfiguration")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
