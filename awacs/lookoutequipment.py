# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Lookout for Equipment'
prefix = 'lookoutequipment'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateDataset = Action('CreateDataset')
CreateInferenceScheduler = Action('CreateInferenceScheduler')
CreateModel = Action('CreateModel')
DeleteDataset = Action('DeleteDataset')
DeleteInferenceScheduler = Action('DeleteInferenceScheduler')
DeleteModel = Action('DeleteModel')
DescribeDataIngestionJob = Action('DescribeDataIngestionJob')
DescribeDataset = Action('DescribeDataset')
DescribeInferenceScheduler = Action('DescribeInferenceScheduler')
DescribeModel = Action('DescribeModel')
ListDataIngestionJobs = Action('ListDataIngestionJobs')
ListDatasets = Action('ListDatasets')
ListInferenceExecutions = Action('ListInferenceExecutions')
ListInferenceSchedulers = Action('ListInferenceSchedulers')
ListModels = Action('ListModels')
ListTagsForResource = Action('ListTagsForResource')
StartDataIngestionJob = Action('StartDataIngestionJob')
StartInferenceScheduler = Action('StartInferenceScheduler')
StopInferenceScheduler = Action('StopInferenceScheduler')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateInferenceScheduler = Action('UpdateInferenceScheduler')