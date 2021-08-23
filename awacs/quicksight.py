# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon QuickSight"
prefix = "quicksight"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelIngestion = Action("CancelIngestion")
CreateAccountCustomization = Action("CreateAccountCustomization")
CreateAdmin = Action("CreateAdmin")
CreateAnalysis = Action("CreateAnalysis")
CreateCustomPermissions = Action("CreateCustomPermissions")
CreateDashboard = Action("CreateDashboard")
CreateDataSet = Action("CreateDataSet")
CreateDataSource = Action("CreateDataSource")
CreateGroup = Action("CreateGroup")
CreateGroupMembership = Action("CreateGroupMembership")
CreateIAMPolicyAssignment = Action("CreateIAMPolicyAssignment")
CreateIngestion = Action("CreateIngestion")
CreateNamespace = Action("CreateNamespace")
CreateReader = Action("CreateReader")
CreateTemplate = Action("CreateTemplate")
CreateTemplateAlias = Action("CreateTemplateAlias")
CreateTheme = Action("CreateTheme")
CreateThemeAlias = Action("CreateThemeAlias")
CreateUser = Action("CreateUser")
CreateVPCConnection = Action("CreateVPCConnection")
DeleteAccountCustomization = Action("DeleteAccountCustomization")
DeleteAnalysis = Action("DeleteAnalysis")
DeleteCustomPermissions = Action("DeleteCustomPermissions")
DeleteDashboard = Action("DeleteDashboard")
DeleteDataSet = Action("DeleteDataSet")
DeleteDataSource = Action("DeleteDataSource")
DeleteGroup = Action("DeleteGroup")
DeleteGroupMembership = Action("DeleteGroupMembership")
DeleteIAMPolicyAssignment = Action("DeleteIAMPolicyAssignment")
DeleteNamespace = Action("DeleteNamespace")
DeleteTemplate = Action("DeleteTemplate")
DeleteTemplateAlias = Action("DeleteTemplateAlias")
DeleteTheme = Action("DeleteTheme")
DeleteThemeAlias = Action("DeleteThemeAlias")
DeleteUser = Action("DeleteUser")
DeleteUserByPrincipalId = Action("DeleteUserByPrincipalId")
DeleteVPCConnection = Action("DeleteVPCConnection")
DescribeAccountCustomization = Action("DescribeAccountCustomization")
DescribeAccountSettings = Action("DescribeAccountSettings")
DescribeAnalysis = Action("DescribeAnalysis")
DescribeAnalysisPermissions = Action("DescribeAnalysisPermissions")
DescribeCustomPermissions = Action("DescribeCustomPermissions")
DescribeDashboard = Action("DescribeDashboard")
DescribeDashboardPermissions = Action("DescribeDashboardPermissions")
DescribeDataSet = Action("DescribeDataSet")
DescribeDataSetPermissions = Action("DescribeDataSetPermissions")
DescribeDataSource = Action("DescribeDataSource")
DescribeDataSourcePermissions = Action("DescribeDataSourcePermissions")
DescribeGroup = Action("DescribeGroup")
DescribeIAMPolicyAssignment = Action("DescribeIAMPolicyAssignment")
DescribeIngestion = Action("DescribeIngestion")
DescribeNamespace = Action("DescribeNamespace")
DescribeTemplate = Action("DescribeTemplate")
DescribeTemplateAlias = Action("DescribeTemplateAlias")
DescribeTemplatePermissions = Action("DescribeTemplatePermissions")
DescribeTheme = Action("DescribeTheme")
DescribeThemeAlias = Action("DescribeThemeAlias")
DescribeThemePermissions = Action("DescribeThemePermissions")
DescribeUser = Action("DescribeUser")
GenerateEmbedUrlForAnonymousUser = Action("GenerateEmbedUrlForAnonymousUser")
GenerateEmbedUrlForRegisteredUser = Action("GenerateEmbedUrlForRegisteredUser")
GetAnonymousUserEmbedUrl = Action("GetAnonymousUserEmbedUrl")
GetAuthCode = Action("GetAuthCode")
GetDashboardEmbedUrl = Action("GetDashboardEmbedUrl")
GetGroupMapping = Action("GetGroupMapping")
GetSessionEmbedUrl = Action("GetSessionEmbedUrl")
ListAnalyses = Action("ListAnalyses")
ListCustomPermissions = Action("ListCustomPermissions")
ListDashboardVersions = Action("ListDashboardVersions")
ListDashboards = Action("ListDashboards")
ListDataSets = Action("ListDataSets")
ListDataSources = Action("ListDataSources")
ListGroupMemberships = Action("ListGroupMemberships")
ListGroups = Action("ListGroups")
ListIAMPolicyAssignments = Action("ListIAMPolicyAssignments")
ListIAMPolicyAssignmentsForUser = Action("ListIAMPolicyAssignmentsForUser")
ListIngestions = Action("ListIngestions")
ListNamespaces = Action("ListNamespaces")
ListTagsForResource = Action("ListTagsForResource")
ListTemplateAliases = Action("ListTemplateAliases")
ListTemplateVersions = Action("ListTemplateVersions")
ListTemplates = Action("ListTemplates")
ListThemeAliases = Action("ListThemeAliases")
ListThemeVersions = Action("ListThemeVersions")
ListThemes = Action("ListThemes")
ListUserGroups = Action("ListUserGroups")
ListUsers = Action("ListUsers")
PassDataSet = Action("PassDataSet")
PassDataSource = Action("PassDataSource")
RegisterUser = Action("RegisterUser")
RestoreAnalysis = Action("RestoreAnalysis")
SearchAnalyses = Action("SearchAnalyses")
SearchDashboards = Action("SearchDashboards")
SearchDirectoryGroups = Action("SearchDirectoryGroups")
SetGroupMapping = Action("SetGroupMapping")
Subscribe = Action("Subscribe")
TagResource = Action("TagResource")
Unsubscribe = Action("Unsubscribe")
UntagResource = Action("UntagResource")
UpdateAccountCustomization = Action("UpdateAccountCustomization")
UpdateAccountSettings = Action("UpdateAccountSettings")
UpdateAnalysis = Action("UpdateAnalysis")
UpdateAnalysisPermissions = Action("UpdateAnalysisPermissions")
UpdateCustomPermissions = Action("UpdateCustomPermissions")
UpdateDashboard = Action("UpdateDashboard")
UpdateDashboardPermissions = Action("UpdateDashboardPermissions")
UpdateDashboardPublishedVersion = Action("UpdateDashboardPublishedVersion")
UpdateDataSet = Action("UpdateDataSet")
UpdateDataSetPermissions = Action("UpdateDataSetPermissions")
UpdateDataSource = Action("UpdateDataSource")
UpdateDataSourcePermissions = Action("UpdateDataSourcePermissions")
UpdateGroup = Action("UpdateGroup")
UpdateIAMPolicyAssignment = Action("UpdateIAMPolicyAssignment")
UpdateTemplate = Action("UpdateTemplate")
UpdateTemplateAlias = Action("UpdateTemplateAlias")
UpdateTemplatePermissions = Action("UpdateTemplatePermissions")
UpdateTheme = Action("UpdateTheme")
UpdateThemeAlias = Action("UpdateThemeAlias")
UpdateThemePermissions = Action("UpdateThemePermissions")
UpdateUser = Action("UpdateUser")
