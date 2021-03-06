"""Dkube Launcher for kubeflow pipelines

Usage:
    dkube.py [--name=NAME] [--token=TOKEN] [--command=COMMAND] [--training=TRAINING] [--preprocessing=PREPROCESSING] [--serving=SERVING] [--custom=CUSTOM] [--visualizer=VISUALIZER] [--runid=RUNID] [--workflowid=WORKFLOWID]
    dkube.py (-h | --help)
    dkube.py --version

Options:
    -h --help                           Show this screen.
    --version                           Show version.
    --name=NAME                         User specified name of the pipeline stage
    --token=TOKEN                       Authentication token of logged in user
    --command=COMMAND                   Command to execute. project/dataset/model/training/preprocessing/serving/custom.
    --training=TRAINING                 Training job definition. JSON str of dkube.sdk.rsrcs:DkubeTraining
    --preprocessing=PREPROCESSING       Preprocessing job definition. JSON str of dkube.sdk.rsrcs:DkubePreprocessing
    --serving=SERVING                   Serving job definition. JSON str of dkube.sdk.rsrcs:DkubeServing
    --custom=CUSTOM                     Custom job definition. JSON str of dkube.sdk.rsrcs.DkubeCustom 
    --visualizer=VISUALIZER             Details of visualizer to be associated this dkube job.
    --runid=RUNID                       Unique ID of the pipeline run for back reference.
    --workflowid=WORKFLOWID             Unique ID of the pipeline workflow for back reference.
"""

from .docopt import docopt
from pyfiglet import Figlet

import os

from dkube.sdk import *

from dkube.sdk.internal import dkube_client
from dkube_client.rest import ApiException

from url_normalize import url_normalize

# Configure API key authorization: d3apikey
configuration = dkube_client.Configuration()
configuration.api_key_prefix['Authorization'] = 'Bearer'

dkubeURL = 'http://dkube-controller-master.dkube.cluster.local:5000'
configuration.host = url_normalize('{}/dkube/v2/controller'.format(dkubeURL))
configuration.verify_ssl = False


def run_outputs(user, _class, name):
    gresponse = api.jobs_get_collection_one(user, _class, name)
    job = gresponse.to_dict()['data']['job']
    uuid = job['parameters']['generated']['uuid'] 

    with open("/tmp/rundetails") as op:
        op.write(json.dumps(job))

    lresponse = api.get_one_run_lineage(user, _class, uuid)
    outputs = lresponse.to_dict()['data']['outputs']

    with open("/tmp/artifacts") as op:
        op.write(json.dumps(outputs))

def command_serving(user='', serving='', runid='', **kwargs):
    runname = generate('plserving')
    run = json.loads(serving)
    run['name'] = name
    run['parameters']['class'] = 'serving'
    run['parameters']['tags'].extend(['owner=pipeline', 'stage='+name, 'workflowid='+workflowid, 'runid='+runid])

    api.jobs_add_one(user, run, run='true')
    while True:
        response = api.jobs_get_collection_one(user, 'serving', runname)
        status = response.to_dict()['data']['job']['parameters']['generated']['status']
        state, reason = status['state'], status['reason']
        if state.lower() in ['complete', 'failed', 'error']:
            print("run {} - completed with state {} and reason {}".format(runname, state, reason))
            return
        else:
            print("run {} - waiting for completion, current state {}".format(runname, state))
            time.sleep(10)

    #generate the outputs, next stage can pick from here
    run_outputs(user, 'serving', runname)


def command_preprocessing(user='', preprocessing='', runid='', **kwargs):
    runname = generate('pldata')
    run = json.loads(preprocessing)
    run['name'] = runname
    run['parameters']['class'] = 'preprocessing'
    run['parameters']['tags'].extend(['owner=pipeline', 'stage='+name, 'workflowid='+workflowid, 'runid='+runid])

    api.jobs_add_one(user, runname, run='true')
    while True:
        response = api.jobs_get_collection_one(user, 'preprocessing', runname)
        status = response.to_dict()['data']['job']['parameters']['generated']['status']
        state, reason = status['state'], status['reason']
        if state.lower() in ['complete', 'failed', 'error']:
            print("run {} - completed with state {} and reason {}".format(runname, state, reason))
            return
        else:
            print("run {} - waiting for completion, current state {}".format(runname, state))
            time.sleep(10)

    #generate the outputs, next stage can pick from here
    run_outputs(user, 'preprocessing', runname)

def command_training(user='', training='', runid='', **kwargs):
    runname = generate('pltraining')
    run = json.loads(training)
    run['name'] = runname
    run['parameters']['class'] = 'training'
    run['parameters']['tags'].extend(['owner=pipeline', 'stage='+name, 'workflowid='+workflowid, 'runid='+runid])

    api.jobs_add_one(user, run, run='true')
    while True:
        response = api.jobs_get_collection_one(user, 'training', runname)
        status = response.to_dict()['data']['job']['parameters']['generated']['status']
        state, reason = status['state'], status['reason']
        if state.lower() in ['complete', 'failed', 'error']:
            print("run {} - completed with state {} and reason {}".format(runname, state, reason))
            return
        else:
            print("run {} - waiting for completion, current state {}".format(runname, state))
            time.sleep(10)

    #generate the outputs, next stage can pick from here
    run_outputs(user, 'training', runname)

def validate_token(token):
    configuration.api_key['Authorization'] = token

    api = dkube_client.DkubeApi(dkube_client.ApiClient(configuration))

    response = api.tokeninfo()
    claims = response['data']
    user = claims['user']
    role = claims['role']

    return user, role

def main():
    args = docopt(__doc__, version='1.4')
    data = {}
    for key, val in kwargs.items():
        data[key.lstrip('--')] = val

    command = data['command']

    f = Figlet(font='slant')
    print(f.renderText('Dkube {}'.format(command.capitalize())))

    user, role = validate_token(data['token'])
    data.update({'user': user, 'role': role})
    fn = 'command_{}'.format(command)
    globals()[fn](**data)
