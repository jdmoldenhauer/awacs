# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon SageMaker"
prefix = "sagemaker"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddAssociation = Action("AddAssociation")
AddTags = Action("AddTags")
AssociateTrialComponent = Action("AssociateTrialComponent")
BatchDescribeModelPackage = Action("BatchDescribeModelPackage")
BatchGetMetrics = Action("BatchGetMetrics")
BatchGetRecord = Action("BatchGetRecord")
BatchPutMetrics = Action("BatchPutMetrics")
CreateAction = Action("CreateAction")
CreateAlgorithm = Action("CreateAlgorithm")
CreateApp = Action("CreateApp")
CreateAppImageConfig = Action("CreateAppImageConfig")
CreateArtifact = Action("CreateArtifact")
CreateAutoMLJob = Action("CreateAutoMLJob")
CreateCodeRepository = Action("CreateCodeRepository")
CreateCompilationJob = Action("CreateCompilationJob")
CreateContext = Action("CreateContext")
CreateDataQualityJobDefinition = Action("CreateDataQualityJobDefinition")
CreateDeviceFleet = Action("CreateDeviceFleet")
CreateDomain = Action("CreateDomain")
CreateEdgePackagingJob = Action("CreateEdgePackagingJob")
CreateEndpoint = Action("CreateEndpoint")
CreateEndpointConfig = Action("CreateEndpointConfig")
CreateExperiment = Action("CreateExperiment")
CreateFeatureGroup = Action("CreateFeatureGroup")
CreateFlowDefinition = Action("CreateFlowDefinition")
CreateHumanTaskUi = Action("CreateHumanTaskUi")
CreateHyperParameterTuningJob = Action("CreateHyperParameterTuningJob")
CreateImage = Action("CreateImage")
CreateImageVersion = Action("CreateImageVersion")
CreateInferenceRecommendationsJob = Action("CreateInferenceRecommendationsJob")
CreateLabelingJob = Action("CreateLabelingJob")
CreateLineageGroupPolicy = Action("CreateLineageGroupPolicy")
CreateModel = Action("CreateModel")
CreateModelBiasJobDefinition = Action("CreateModelBiasJobDefinition")
CreateModelExplainabilityJobDefinition = Action(
    "CreateModelExplainabilityJobDefinition"
)
CreateModelPackage = Action("CreateModelPackage")
CreateModelPackageGroup = Action("CreateModelPackageGroup")
CreateModelQualityJobDefinition = Action("CreateModelQualityJobDefinition")
CreateMonitoringSchedule = Action("CreateMonitoringSchedule")
CreateNotebookInstance = Action("CreateNotebookInstance")
CreateNotebookInstanceLifecycleConfig = Action("CreateNotebookInstanceLifecycleConfig")
CreatePipeline = Action("CreatePipeline")
CreatePresignedDomainUrl = Action("CreatePresignedDomainUrl")
CreatePresignedNotebookInstanceUrl = Action("CreatePresignedNotebookInstanceUrl")
CreateProcessingJob = Action("CreateProcessingJob")
CreateProject = Action("CreateProject")
CreateStudioLifecycleConfig = Action("CreateStudioLifecycleConfig")
CreateTrainingJob = Action("CreateTrainingJob")
CreateTransformJob = Action("CreateTransformJob")
CreateTrial = Action("CreateTrial")
CreateTrialComponent = Action("CreateTrialComponent")
CreateUserProfile = Action("CreateUserProfile")
CreateWorkforce = Action("CreateWorkforce")
CreateWorkteam = Action("CreateWorkteam")
DeleteAction = Action("DeleteAction")
DeleteAlgorithm = Action("DeleteAlgorithm")
DeleteApp = Action("DeleteApp")
DeleteAppImageConfig = Action("DeleteAppImageConfig")
DeleteArtifact = Action("DeleteArtifact")
DeleteAssociation = Action("DeleteAssociation")
DeleteCodeRepository = Action("DeleteCodeRepository")
DeleteContext = Action("DeleteContext")
DeleteDataQualityJobDefinition = Action("DeleteDataQualityJobDefinition")
DeleteDeviceFleet = Action("DeleteDeviceFleet")
DeleteDomain = Action("DeleteDomain")
DeleteEndpoint = Action("DeleteEndpoint")
DeleteEndpointConfig = Action("DeleteEndpointConfig")
DeleteExperiment = Action("DeleteExperiment")
DeleteFeatureGroup = Action("DeleteFeatureGroup")
DeleteFlowDefinition = Action("DeleteFlowDefinition")
DeleteHumanLoop = Action("DeleteHumanLoop")
DeleteHumanTaskUi = Action("DeleteHumanTaskUi")
DeleteImage = Action("DeleteImage")
DeleteImageVersion = Action("DeleteImageVersion")
DeleteLineageGroupPolicy = Action("DeleteLineageGroupPolicy")
DeleteModel = Action("DeleteModel")
DeleteModelBiasJobDefinition = Action("DeleteModelBiasJobDefinition")
DeleteModelExplainabilityJobDefinition = Action(
    "DeleteModelExplainabilityJobDefinition"
)
DeleteModelPackage = Action("DeleteModelPackage")
DeleteModelPackageGroup = Action("DeleteModelPackageGroup")
DeleteModelPackageGroupPolicy = Action("DeleteModelPackageGroupPolicy")
DeleteModelQualityJobDefinition = Action("DeleteModelQualityJobDefinition")
DeleteMonitoringSchedule = Action("DeleteMonitoringSchedule")
DeleteNotebookInstance = Action("DeleteNotebookInstance")
DeleteNotebookInstanceLifecycleConfig = Action("DeleteNotebookInstanceLifecycleConfig")
DeletePipeline = Action("DeletePipeline")
DeleteProject = Action("DeleteProject")
DeleteRecord = Action("DeleteRecord")
DeleteStudioLifecycleConfig = Action("DeleteStudioLifecycleConfig")
DeleteTags = Action("DeleteTags")
DeleteTrial = Action("DeleteTrial")
DeleteTrialComponent = Action("DeleteTrialComponent")
DeleteUserProfile = Action("DeleteUserProfile")
DeleteWorkforce = Action("DeleteWorkforce")
DeleteWorkteam = Action("DeleteWorkteam")
DeregisterDevices = Action("DeregisterDevices")
DescribeAction = Action("DescribeAction")
DescribeAlgorithm = Action("DescribeAlgorithm")
DescribeApp = Action("DescribeApp")
DescribeAppImageConfig = Action("DescribeAppImageConfig")
DescribeArtifact = Action("DescribeArtifact")
DescribeAutoMLJob = Action("DescribeAutoMLJob")
DescribeCodeRepository = Action("DescribeCodeRepository")
DescribeCompilationJob = Action("DescribeCompilationJob")
DescribeContext = Action("DescribeContext")
DescribeDataQualityJobDefinition = Action("DescribeDataQualityJobDefinition")
DescribeDevice = Action("DescribeDevice")
DescribeDeviceFleet = Action("DescribeDeviceFleet")
DescribeDomain = Action("DescribeDomain")
DescribeEdgePackagingJob = Action("DescribeEdgePackagingJob")
DescribeEndpoint = Action("DescribeEndpoint")
DescribeEndpointConfig = Action("DescribeEndpointConfig")
DescribeExperiment = Action("DescribeExperiment")
DescribeFeatureGroup = Action("DescribeFeatureGroup")
DescribeFlowDefinition = Action("DescribeFlowDefinition")
DescribeHumanLoop = Action("DescribeHumanLoop")
DescribeHumanTaskUi = Action("DescribeHumanTaskUi")
DescribeHyperParameterTuningJob = Action("DescribeHyperParameterTuningJob")
DescribeImage = Action("DescribeImage")
DescribeImageVersion = Action("DescribeImageVersion")
DescribeInferenceRecommendationsJob = Action("DescribeInferenceRecommendationsJob")
DescribeLabelingJob = Action("DescribeLabelingJob")
DescribeLineageGroup = Action("DescribeLineageGroup")
DescribeModel = Action("DescribeModel")
DescribeModelBiasJobDefinition = Action("DescribeModelBiasJobDefinition")
DescribeModelExplainabilityJobDefinition = Action(
    "DescribeModelExplainabilityJobDefinition"
)
DescribeModelPackage = Action("DescribeModelPackage")
DescribeModelPackageGroup = Action("DescribeModelPackageGroup")
DescribeModelQualityJobDefinition = Action("DescribeModelQualityJobDefinition")
DescribeMonitoringSchedule = Action("DescribeMonitoringSchedule")
DescribeNotebookInstance = Action("DescribeNotebookInstance")
DescribeNotebookInstanceLifecycleConfig = Action(
    "DescribeNotebookInstanceLifecycleConfig"
)
DescribePipeline = Action("DescribePipeline")
DescribePipelineDefinitionForExecution = Action(
    "DescribePipelineDefinitionForExecution"
)
DescribePipelineExecution = Action("DescribePipelineExecution")
DescribeProcessingJob = Action("DescribeProcessingJob")
DescribeProject = Action("DescribeProject")
DescribeStudioLifecycleConfig = Action("DescribeStudioLifecycleConfig")
DescribeSubscribedWorkteam = Action("DescribeSubscribedWorkteam")
DescribeTrainingJob = Action("DescribeTrainingJob")
DescribeTransformJob = Action("DescribeTransformJob")
DescribeTrial = Action("DescribeTrial")
DescribeTrialComponent = Action("DescribeTrialComponent")
DescribeUserProfile = Action("DescribeUserProfile")
DescribeWorkforce = Action("DescribeWorkforce")
DescribeWorkteam = Action("DescribeWorkteam")
DisableSagemakerServicecatalogPortfolio = Action(
    "DisableSagemakerServicecatalogPortfolio"
)
DisassociateTrialComponent = Action("DisassociateTrialComponent")
EnableSagemakerServicecatalogPortfolio = Action(
    "EnableSagemakerServicecatalogPortfolio"
)
GetDeviceFleetReport = Action("GetDeviceFleetReport")
GetDeviceRegistration = Action("GetDeviceRegistration")
GetLineageGroupPolicy = Action("GetLineageGroupPolicy")
GetModelPackageGroupPolicy = Action("GetModelPackageGroupPolicy")
GetRecord = Action("GetRecord")
GetSagemakerServicecatalogPortfolioStatus = Action(
    "GetSagemakerServicecatalogPortfolioStatus"
)
GetSearchSuggestions = Action("GetSearchSuggestions")
InvokeEndpoint = Action("InvokeEndpoint")
InvokeEndpointAsync = Action("InvokeEndpointAsync")
ListActions = Action("ListActions")
ListAlgorithms = Action("ListAlgorithms")
ListAppImageConfigs = Action("ListAppImageConfigs")
ListApps = Action("ListApps")
ListArtifacts = Action("ListArtifacts")
ListAssociations = Action("ListAssociations")
ListAutoMLJobs = Action("ListAutoMLJobs")
ListCandidatesForAutoMLJob = Action("ListCandidatesForAutoMLJob")
ListCodeRepositories = Action("ListCodeRepositories")
ListCompilationJobs = Action("ListCompilationJobs")
ListContexts = Action("ListContexts")
ListDataQualityJobDefinitions = Action("ListDataQualityJobDefinitions")
ListDeviceFleets = Action("ListDeviceFleets")
ListDevices = Action("ListDevices")
ListDomains = Action("ListDomains")
ListEdgePackagingJobs = Action("ListEdgePackagingJobs")
ListEndpointConfigs = Action("ListEndpointConfigs")
ListEndpoints = Action("ListEndpoints")
ListExperiments = Action("ListExperiments")
ListFeatureGroups = Action("ListFeatureGroups")
ListFlowDefinitions = Action("ListFlowDefinitions")
ListHumanLoops = Action("ListHumanLoops")
ListHumanTaskUis = Action("ListHumanTaskUis")
ListHyperParameterTuningJobs = Action("ListHyperParameterTuningJobs")
ListImageVersions = Action("ListImageVersions")
ListImages = Action("ListImages")
ListInferenceRecommendationsJobs = Action("ListInferenceRecommendationsJobs")
ListLabelingJobs = Action("ListLabelingJobs")
ListLabelingJobsForWorkteam = Action("ListLabelingJobsForWorkteam")
ListLineageGroups = Action("ListLineageGroups")
ListModelBiasJobDefinitions = Action("ListModelBiasJobDefinitions")
ListModelExplainabilityJobDefinitions = Action("ListModelExplainabilityJobDefinitions")
ListModelMetadata = Action("ListModelMetadata")
ListModelPackageGroups = Action("ListModelPackageGroups")
ListModelPackages = Action("ListModelPackages")
ListModelQualityJobDefinitions = Action("ListModelQualityJobDefinitions")
ListModels = Action("ListModels")
ListMonitoringExecutions = Action("ListMonitoringExecutions")
ListMonitoringSchedules = Action("ListMonitoringSchedules")
ListNotebookInstanceLifecycleConfigs = Action("ListNotebookInstanceLifecycleConfigs")
ListNotebookInstances = Action("ListNotebookInstances")
ListPipelineExecutionSteps = Action("ListPipelineExecutionSteps")
ListPipelineExecutions = Action("ListPipelineExecutions")
ListPipelineParametersForExecution = Action("ListPipelineParametersForExecution")
ListPipelines = Action("ListPipelines")
ListProcessingJobs = Action("ListProcessingJobs")
ListProjects = Action("ListProjects")
ListStudioLifecycleConfigs = Action("ListStudioLifecycleConfigs")
ListSubscribedWorkteams = Action("ListSubscribedWorkteams")
ListTags = Action("ListTags")
ListTrainingJobs = Action("ListTrainingJobs")
ListTrainingJobsForHyperParameterTuningJob = Action(
    "ListTrainingJobsForHyperParameterTuningJob"
)
ListTransformJobs = Action("ListTransformJobs")
ListTrialComponents = Action("ListTrialComponents")
ListTrials = Action("ListTrials")
ListUserProfiles = Action("ListUserProfiles")
ListWorkforces = Action("ListWorkforces")
ListWorkteams = Action("ListWorkteams")
PutLineageGroupPolicy = Action("PutLineageGroupPolicy")
PutModelPackageGroupPolicy = Action("PutModelPackageGroupPolicy")
PutRecord = Action("PutRecord")
QueryLineage = Action("QueryLineage")
RegisterDevices = Action("RegisterDevices")
RenderUiTemplate = Action("RenderUiTemplate")
RetryPipelineExecution = Action("RetryPipelineExecution")
Search = Action("Search")
SendHeartbeat = Action("SendHeartbeat")
SendPipelineExecutionStepFailure = Action("SendPipelineExecutionStepFailure")
SendPipelineExecutionStepSuccess = Action("SendPipelineExecutionStepSuccess")
StartHumanLoop = Action("StartHumanLoop")
StartMonitoringSchedule = Action("StartMonitoringSchedule")
StartNotebookInstance = Action("StartNotebookInstance")
StartPipelineExecution = Action("StartPipelineExecution")
StopAutoMLJob = Action("StopAutoMLJob")
StopCompilationJob = Action("StopCompilationJob")
StopEdgePackagingJob = Action("StopEdgePackagingJob")
StopHumanLoop = Action("StopHumanLoop")
StopHyperParameterTuningJob = Action("StopHyperParameterTuningJob")
StopInferenceRecommendationsJob = Action("StopInferenceRecommendationsJob")
StopLabelingJob = Action("StopLabelingJob")
StopMonitoringSchedule = Action("StopMonitoringSchedule")
StopNotebookInstance = Action("StopNotebookInstance")
StopPipelineExecution = Action("StopPipelineExecution")
StopProcessingJob = Action("StopProcessingJob")
StopTrainingJob = Action("StopTrainingJob")
StopTransformJob = Action("StopTransformJob")
UpdateAction = Action("UpdateAction")
UpdateAppImageConfig = Action("UpdateAppImageConfig")
UpdateArtifact = Action("UpdateArtifact")
UpdateCodeRepository = Action("UpdateCodeRepository")
UpdateContext = Action("UpdateContext")
UpdateDeviceFleet = Action("UpdateDeviceFleet")
UpdateDevices = Action("UpdateDevices")
UpdateDomain = Action("UpdateDomain")
UpdateEndpoint = Action("UpdateEndpoint")
UpdateEndpointWeightsAndCapacities = Action("UpdateEndpointWeightsAndCapacities")
UpdateExperiment = Action("UpdateExperiment")
UpdateImage = Action("UpdateImage")
UpdateModelPackage = Action("UpdateModelPackage")
UpdateMonitoringSchedule = Action("UpdateMonitoringSchedule")
UpdateNotebookInstance = Action("UpdateNotebookInstance")
UpdateNotebookInstanceLifecycleConfig = Action("UpdateNotebookInstanceLifecycleConfig")
UpdatePipeline = Action("UpdatePipeline")
UpdatePipelineExecution = Action("UpdatePipelineExecution")
UpdateProject = Action("UpdateProject")
UpdateTrainingJob = Action("UpdateTrainingJob")
UpdateTrial = Action("UpdateTrial")
UpdateTrialComponent = Action("UpdateTrialComponent")
UpdateUserProfile = Action("UpdateUserProfile")
UpdateWorkforce = Action("UpdateWorkforce")
UpdateWorkteam = Action("UpdateWorkteam")
