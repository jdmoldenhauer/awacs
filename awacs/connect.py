# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Connect"
prefix = "connect"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateApprovedOrigin = Action("AssociateApprovedOrigin")
AssociateBot = Action("AssociateBot")
AssociateCustomerProfilesDomain = Action("AssociateCustomerProfilesDomain")
AssociateDefaultVocabulary = Action("AssociateDefaultVocabulary")
AssociateInstanceStorageConfig = Action("AssociateInstanceStorageConfig")
AssociateLambdaFunction = Action("AssociateLambdaFunction")
AssociateLexBot = Action("AssociateLexBot")
AssociatePhoneNumberContactFlow = Action("AssociatePhoneNumberContactFlow")
AssociateQueueQuickConnects = Action("AssociateQueueQuickConnects")
AssociateRoutingProfileQueues = Action("AssociateRoutingProfileQueues")
AssociateSecurityKey = Action("AssociateSecurityKey")
BatchAssociateAnalyticsDataSet = Action("BatchAssociateAnalyticsDataSet")
BatchDisassociateAnalyticsDataSet = Action("BatchDisassociateAnalyticsDataSet")
ClaimPhoneNumber = Action("ClaimPhoneNumber")
CreateAgentStatus = Action("CreateAgentStatus")
CreateContactFlow = Action("CreateContactFlow")
CreateContactFlowModule = Action("CreateContactFlowModule")
CreateHoursOfOperation = Action("CreateHoursOfOperation")
CreateInstance = Action("CreateInstance")
CreateIntegrationAssociation = Action("CreateIntegrationAssociation")
CreateQueue = Action("CreateQueue")
CreateQuickConnect = Action("CreateQuickConnect")
CreateRoutingProfile = Action("CreateRoutingProfile")
CreateSecurityProfile = Action("CreateSecurityProfile")
CreateUseCase = Action("CreateUseCase")
CreateUser = Action("CreateUser")
CreateUserHierarchyGroup = Action("CreateUserHierarchyGroup")
CreateVocabulary = Action("CreateVocabulary")
DeleteContactFlow = Action("DeleteContactFlow")
DeleteContactFlowModule = Action("DeleteContactFlowModule")
DeleteHoursOfOperation = Action("DeleteHoursOfOperation")
DeleteInstance = Action("DeleteInstance")
DeleteIntegrationAssociation = Action("DeleteIntegrationAssociation")
DeleteQuickConnect = Action("DeleteQuickConnect")
DeleteSecurityProfile = Action("DeleteSecurityProfile")
DeleteUseCase = Action("DeleteUseCase")
DeleteUser = Action("DeleteUser")
DeleteUserHierarchyGroup = Action("DeleteUserHierarchyGroup")
DeleteVocabulary = Action("DeleteVocabulary")
DescribeAgentStatus = Action("DescribeAgentStatus")
DescribeContact = Action("DescribeContact")
DescribeContactFlow = Action("DescribeContactFlow")
DescribeContactFlowModule = Action("DescribeContactFlowModule")
DescribeHoursOfOperation = Action("DescribeHoursOfOperation")
DescribeInstance = Action("DescribeInstance")
DescribeInstanceAttribute = Action("DescribeInstanceAttribute")
DescribeInstanceStorageConfig = Action("DescribeInstanceStorageConfig")
DescribePhoneNumber = Action("DescribePhoneNumber")
DescribeQueue = Action("DescribeQueue")
DescribeQuickConnect = Action("DescribeQuickConnect")
DescribeRoutingProfile = Action("DescribeRoutingProfile")
DescribeSecurityProfile = Action("DescribeSecurityProfile")
DescribeUser = Action("DescribeUser")
DescribeUserHierarchyGroup = Action("DescribeUserHierarchyGroup")
DescribeUserHierarchyStructure = Action("DescribeUserHierarchyStructure")
DescribeVocabulary = Action("DescribeVocabulary")
DestroyInstance = Action("DestroyInstance")
DisassociateApprovedOrigin = Action("DisassociateApprovedOrigin")
DisassociateBot = Action("DisassociateBot")
DisassociateCustomerProfilesDomain = Action("DisassociateCustomerProfilesDomain")
DisassociateInstanceStorageConfig = Action("DisassociateInstanceStorageConfig")
DisassociateLambdaFunction = Action("DisassociateLambdaFunction")
DisassociateLexBot = Action("DisassociateLexBot")
DisassociatePhoneNumberContactFlow = Action("DisassociatePhoneNumberContactFlow")
DisassociateQueueQuickConnects = Action("DisassociateQueueQuickConnects")
DisassociateRoutingProfileQueues = Action("DisassociateRoutingProfileQueues")
DisassociateSecurityKey = Action("DisassociateSecurityKey")
GetContactAttributes = Action("GetContactAttributes")
GetCurrentMetricData = Action("GetCurrentMetricData")
GetFederationToken = Action("GetFederationToken")
GetFederationTokens = Action("GetFederationTokens")
GetMetricData = Action("GetMetricData")
ListAgentStatuses = Action("ListAgentStatuses")
ListApprovedOrigins = Action("ListApprovedOrigins")
ListBots = Action("ListBots")
ListContactFlowModules = Action("ListContactFlowModules")
ListContactFlows = Action("ListContactFlows")
ListContactReferences = Action("ListContactReferences")
ListDefaultVocabularies = Action("ListDefaultVocabularies")
ListHoursOfOperations = Action("ListHoursOfOperations")
ListInstanceAttributes = Action("ListInstanceAttributes")
ListInstanceStorageConfigs = Action("ListInstanceStorageConfigs")
ListInstances = Action("ListInstances")
ListIntegrationAssociations = Action("ListIntegrationAssociations")
ListLambdaFunctions = Action("ListLambdaFunctions")
ListLexBots = Action("ListLexBots")
ListPhoneNumbers = Action("ListPhoneNumbers")
ListPhoneNumbersV2 = Action("ListPhoneNumbersV2")
ListPrompts = Action("ListPrompts")
ListQueueQuickConnects = Action("ListQueueQuickConnects")
ListQueues = Action("ListQueues")
ListQuickConnects = Action("ListQuickConnects")
ListRealtimeContactAnalysisSegments = Action("ListRealtimeContactAnalysisSegments")
ListRoutingProfileQueues = Action("ListRoutingProfileQueues")
ListRoutingProfiles = Action("ListRoutingProfiles")
ListSecurityKeys = Action("ListSecurityKeys")
ListSecurityProfilePermissions = Action("ListSecurityProfilePermissions")
ListSecurityProfiles = Action("ListSecurityProfiles")
ListTagsForResource = Action("ListTagsForResource")
ListUseCases = Action("ListUseCases")
ListUserHierarchyGroups = Action("ListUserHierarchyGroups")
ListUsers = Action("ListUsers")
ModifyInstance = Action("ModifyInstance")
ReleasePhoneNumber = Action("ReleasePhoneNumber")
ResumeContactRecording = Action("ResumeContactRecording")
SearchAvailablePhoneNumbers = Action("SearchAvailablePhoneNumbers")
SearchUsers = Action("SearchUsers")
SearchVocabularies = Action("SearchVocabularies")
StartChatContact = Action("StartChatContact")
StartContactRecording = Action("StartContactRecording")
StartContactStreaming = Action("StartContactStreaming")
StartOutboundVoiceContact = Action("StartOutboundVoiceContact")
StartTaskContact = Action("StartTaskContact")
StopContact = Action("StopContact")
StopContactRecording = Action("StopContactRecording")
StopContactStreaming = Action("StopContactStreaming")
SuspendContactRecording = Action("SuspendContactRecording")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgentStatus = Action("UpdateAgentStatus")
UpdateContact = Action("UpdateContact")
UpdateContactAttributes = Action("UpdateContactAttributes")
UpdateContactFlowContent = Action("UpdateContactFlowContent")
UpdateContactFlowMetadata = Action("UpdateContactFlowMetadata")
UpdateContactFlowModuleContent = Action("UpdateContactFlowModuleContent")
UpdateContactFlowModuleMetadata = Action("UpdateContactFlowModuleMetadata")
UpdateContactFlowName = Action("UpdateContactFlowName")
UpdateContactSchedule = Action("UpdateContactSchedule")
UpdateHoursOfOperation = Action("UpdateHoursOfOperation")
UpdateInstanceAttribute = Action("UpdateInstanceAttribute")
UpdateInstanceStorageConfig = Action("UpdateInstanceStorageConfig")
UpdatePhoneNumber = Action("UpdatePhoneNumber")
UpdateQueueHoursOfOperation = Action("UpdateQueueHoursOfOperation")
UpdateQueueMaxContacts = Action("UpdateQueueMaxContacts")
UpdateQueueName = Action("UpdateQueueName")
UpdateQueueOutboundCallerConfig = Action("UpdateQueueOutboundCallerConfig")
UpdateQueueStatus = Action("UpdateQueueStatus")
UpdateQuickConnectConfig = Action("UpdateQuickConnectConfig")
UpdateQuickConnectName = Action("UpdateQuickConnectName")
UpdateRoutingProfileConcurrency = Action("UpdateRoutingProfileConcurrency")
UpdateRoutingProfileDefaultOutboundQueue = Action(
    "UpdateRoutingProfileDefaultOutboundQueue"
)
UpdateRoutingProfileName = Action("UpdateRoutingProfileName")
UpdateRoutingProfileQueues = Action("UpdateRoutingProfileQueues")
UpdateSecurityProfile = Action("UpdateSecurityProfile")
UpdateUserHierarchy = Action("UpdateUserHierarchy")
UpdateUserHierarchyGroupName = Action("UpdateUserHierarchyGroupName")
UpdateUserHierarchyStructure = Action("UpdateUserHierarchyStructure")
UpdateUserIdentityInfo = Action("UpdateUserIdentityInfo")
UpdateUserPhoneConfig = Action("UpdateUserPhoneConfig")
UpdateUserRoutingProfile = Action("UpdateUserRoutingProfile")
UpdateUserSecurityProfiles = Action("UpdateUserSecurityProfiles")
UpdatedescribeContent = Action("UpdatedescribeContent")
