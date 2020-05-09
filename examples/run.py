import sys
import pdb;pdb.set_trace()
#sys.path.insert(0, '/home/dkube/ahmed/dkube-sdk-2.0/dkube')

from dkube.sdk import *
from dkube.sdk.lib.api import *

if __name__ == "__main__":
    
    project = DkubeProject('oc', name='mak1')
    project.update_project_source(source='github')
    project.update_github_details('https://github.com/oneconvergence/dkube-examples/tree/2.0.3/tensorflow/classification/mnist/digits/classifier/program', branch='2.0.6')
    

    dataset = DkubeDataset('oc', name='mak1')
    dataset.update_dataset_source(source='github')
    dataset.update_github_details('https://github.com/oneconvergence/dkube-examples/tree/2.0.3/tensorflow/classification/mnist/digits/classifier/program', branch='2.0.6')

    odataset = DkubeDataset('oc', name='mak2')
    odataset.update_dataset_source(source='dvs')

    model = DkubeModel('oc', name='mak1')
    model.update_model_source(source='dvs')


    training = DkubeTraining('oc')
    training.update_startupscript(startup_script='sleep 30')
    training.add_project('mak1')
    training.add_input_dataset('mak1', mountpath='/opt/dkube/input')
    training.add_output_model('mak1', mountpath='/opt/dkube/output')

    print(training.job.to_dict())

    preprocessing = DkubePreprocessing('oc')
    preprocessing.update_startupscript(startup_script='sleep 30')
    preprocessing.add_project('mak1')
    preprocessing.add_input_dataset('mak1', mountpath='/opt/dkube/input')
    preprocessing.add_output_dataset('mak2', mountpath='/opt/dkube/output')


    api = DkubeApi(dkubeURL='https://192.168.200.106:32222', authToken='eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc0YmNkZjBmZWJmNDRiOGRhZGQxZWIyOGM2MjhkYWYxIn0.eyJ1c2VybmFtZSI6Im9jIiwicm9sZSI6Im9wZXJhdG9yIiwiaWF0IjoxNTg3NzIxNTE4LCJpc3MiOiJES3ViZSJ9.OQmeuygUqH9qPSUm-SrqeyTdekMOH0E3XBeaCYLSmEh-oRXRL3XhEtLnHhXn6KPzXWkEuDo1W_FyrUEpXZsXXHP-Fjt1cF08IXmSxWIRRw9-dcAuPJxBzgmxyJWpTVlSiwN8HhfJNuTPk8sSUhzPLmBD4eEN3gGS3FP7_VdvXDOpgYW7__IkN7qpfkdz6H0mMeAcsazDbZ1ZwMoVkBq-Ad6UnQ-5FvfWYxVPPKD95QGmpGz7TpAmbYHMFWTWIgyxuQnw24W72wn1Un21C1P9HUTSIPLQHqO6sbhHaZVmWGdzcMN1wmGSWqJucKyQHUCntVyx0axDMDbXSnuwNuBWaQ')
    #api.create_project(project)
    #api.create_dataset(dataset)
    #api.create_model(model)
    #api.create_training_run(training)

    #api.create_dataset(odataset)
    #api.create_preprocessing_run(preprocessing)

    #claims = api.validate_token()

    from dkube.sdk.internal import dkube_client
    from dkube_client.rest import ApiException

    from url_normalize import url_normalize

    # Configure API key authorization: d3apikey
    configuration = dkube_client.Configuration()
    configuration.api_key_prefix['Authorization'] = 'Bearer'

    dkubeURL = 'https://192.168.200.106:32222'
    token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc0YmNkZjBmZWJmNDRiOGRhZGQxZWIyOGM2MjhkYWYxIn0.eyJ1c2VybmFtZSI6Im9jIiwicm9sZSI6Im9wZXJhdG9yIiwiaWF0IjoxNTg3NzIxNTE4LCJpc3MiOiJES3ViZSJ9.OQmeuygUqH9qPSUm-SrqeyTdekMOH0E3XBeaCYLSmEh-oRXRL3XhEtLnHhXn6KPzXWkEuDo1W_FyrUEpXZsXXHP-Fjt1cF08IXmSxWIRRw9-dcAuPJxBzgmxyJWpTVlSiwN8HhfJNuTPk8sSUhzPLmBD4eEN3gGS3FP7_VdvXDOpgYW7__IkN7qpfkdz6H0mMeAcsazDbZ1ZwMoVkBq-Ad6UnQ-5FvfWYxVPPKD95QGmpGz7TpAmbYHMFWTWIgyxuQnw24W72wn1Un21C1P9HUTSIPLQHqO6sbhHaZVmWGdzcMN1wmGSWqJucKyQHUCntVyx0axDMDbXSnuwNuBWaQ'
    configuration.host = url_normalize('{}/dkube/v2/controller'.format(dkubeURL))
    configuration.api_key['Authorization'] = token
    configuration.verify_ssl = False

    api = dkube_client.DkubeApi(dkube_client.ApiClient(configuration))
    jdict = preprocessing.job.to_dict()
    jdict['parameters']['class'] = 'preprocessing'
    #jdict = {'version': None, 'name': 'data-0528', 'description': '', 'parameters': {'class': 'preprocessing', 'gpu_allocation': None, 'priority': None, 'training': None, 'notebook': None, 'inference': None, 'preprocessing': {'kind': 'preprocessing', 'executor': {'choice': 'custom', 'custom': {'image': {'path': 'docker.io/ocdr/dkube-datascience-tf-cpu:v1.13', 'username': None, 'password': None, 'runas': None}}}, 'datums': {'workspace': {'data': {'name': 'oc:mak1', 'version': None, 'mountpath': None}, 'script': 'sleep 30'}, 'models': None, 'datasets': [{'name': 'oc:mak1', 'version': None, 'mountpath': '/opt/dkube/input'}], 'outputs': [{'name': 'oc:mak2', 'version': None, 'mountpath': '/opt/dkube/output'}]}, 'tags': [], 'config': {'envs': None, 'file': {'name': None, 'body': None}}}, 'custom': None, 'run': {'template': None, 'group': 'default'}, 'generated': None}}
    #response = api.jobs_add_one('oc', jdict, run='true')
    response = api.jobs_get_collection_one('oc', 'preprocessing', 'data-3797')
    print(response.to_dict())
    uuid = response.to_dict()['data']['job']['parameters']['generated']['uuid']
    response = api.get_one_run_lineage('oc', 'preprocessing', uuid)
