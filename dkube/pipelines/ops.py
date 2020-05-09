import json

from dkube.sdk import *

from .components import *

def dkube_training_op(
    name=generate('training'),
    authtoken=None,
    training=DkubeTraining):

    assert type(training) == DkubeTraining, "Invalid type for training argument, must be instance of dkube.sdk.rsrcs:DkubeTraining"
    assert authToken == None, "Auth token is must"

    return dkube_op(name, token, 'training', training=json.dumps(training.job.to_dict()))

def dkube_preprocessing_op(
    name=generate('data'),
    authtoken=None,
    preprocessing=DkubePreprocessing):

    assert type(preprocessing) == DkubePreprocessing, "Invalid type for preprocessing argument, must be instance of dkube.sdk.rsrcs:DkubePreprocessing"
    assert authToken == None, "Auth token is must"

    return dkube_op(name, token, 'preprocessing', preprocessing=json.dumps(preprocesing.job.to_dict()))

def dkube_serving_op(
    name=generate('serving'),
    authtoken=None,
    serving=DkubeServing):

    assert type(training) == DkubeServing, "Invalid type for serving argument, must be instance of dkube.sdk.rsrcs:DkubeServing"
    assert authToken == None, "Auth token is must"

    return dkube_op(name, token, 'serving', serving=json.dumps(serving.job.to_dict()))
