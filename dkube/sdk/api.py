"""
.. module:: DKube API
   :synopsis: Helper class which provides high level methods for user to integrate at workflow level.
	      Import like below in your application::
		from dkube.sdk import *

.. moduleauthor:: Ahmed Khan <github.com/mak-454>


"""

from dkube.sdk.internal.api_base import *
from dkube.sdk.rsrcs import *

import time

"""
    **DkubeApi Python class**

    This class encapsules all the high level dkube workflow functions.

    - Example::

	from dkube.sdk import *
	dapi = DkubeApi()

    - Inputs

	- URL
	    FQDN endpoint at which DKube platform is deployed

	    Example::

		- http://dkube-controller-master.dkube.cluster.local:5000
		- https://dkube.ai:32222

	    .. note:: If not provided then the value is picked from *DKUBE_ACCESS_URL* env variable. If not found then http://dkube-controller-master.dkube.cluster.local:5000 is used assuming the access is internal to the DKube cluster

	- token
	    Access token for the APIs, without which DKube will return 40x codes

	    .. note:: If not provided then the value is picked from *DKUBE_ACCESS_TOKEN* env variable. ASSERTs if env is not defined.
"""
		
class DkubeApi(ApiBase):
    def __init__(self, URL=None, token=None, common_tags=[], req_timeout=None, req_retries=None):
        if URL == None:
            self.url = os.getenv(
                "DKUBE_ACCESS_URL", "http://dkube-controller-master.dkube.cluster.local:5000")
        if token == None:
            self.token = os.getenv("DKUBE_ACCESS_TOKEN", None)
            assert self.token == None, "TOKEN must be specified either by passing argument or by setting DKUBE_ACCESS_TOKEN env variable"

        self.common_tags = common_tags
        super().__init__(self.url, self.token)

    def validate_token(self):
        return super().validate_token()

    def create_training_run(self, run: DkubeTraining, wait_for_completion=True):
        assert type(
            run) == DkubeTraining, "Invalid type for run, value must be instance of rsrcs:DkubeTraining class"
        super().create_run(run)
        while wait_for_completion:
            status = super().get_run('training', run.user, run.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['complete', 'failed', 'error']:
                print(
                    "run {} - completed with state {} and reason {}".format(run.name, state, reason))
                break
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(run.name, state))
                time.sleep(10)

    def get_training_run(self, user, name):
        return super().get_run('training', user, name)

    def list_training_runs(self, user, filters='*'):
        return super().list_runs('training', user, name)

    def delete_training_run(self, user, name):
        super().delete_run('training', user, name)

    def create_preprocessing_run(self, run: DkubePreprocessing, wait_for_completion=True):
        assert type(
            run) == DkubePreprocessing, "Invalid type for run, value must be instance of rsrcs:DkubePreprocessing class"
        super().create_run(run)
        while wait_for_completion:
            status = super().get_run('preprocessing', run.user, run.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['complete', 'failed', 'error']:
                print(
                    "run {} - completed with state {} and reason {}".format(run.name, state, reason))
                break
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(run.name, state))
                time.sleep(10)

    def get_preprocessing_run(self, user, name):
        return super().get_run('preprocessing', user, name)

    def list_preprocessing_runs(self, user, filters='*'):
        return super().list_runs('preprocessing', user, name)

    def delete_preprocessing_run(self, user, name):
        super().delete_run('preprocessing', user, name)

    def create_serving_run(self, run: DkubeServing, wait_for_completion=True):
        assert type(
            run) == DkubeServing, "Invalid type for run, value must be instance of rsrcs:DkubeServing class"
        super().create_run(run)
        while wait_for_completion:
            status = super().get_run(self, 'inference', user, run.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['complete', 'failed', 'error']:
                print(
                    "run {} - completed with state {} and reason {}".format(run.name, state, reason))
                break
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(run.name, state))
                time.sleep(10)

    def get_serving_run(self, user, name):
        return super().get_run('serving', user, name)

    def list_serving_runs(self, user, filters='*'):
        return super().list_runs('serving', user, name)

    def delete_serving_run(self, user, name):
        super().delete_run('serving', user, name)

    def create_project(self, project: DkubeProject, wait_for_completion=True):
        assert type(
            project) == DkubeProject, "Invalid type for run, value must be instance of rsrcs:DkubeProject class"
        super().create_repo(project)
        while wait_for_completion:
            status = super().get_repo('program', project.user, project.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['ready', 'failed', 'error']:
                print(
                    "project {} - completed with state {} and reason {}".format(project.name, state, reason))
                break
            else:
                print(
                    "project {} - waiting for completion, current state {}".format(project.name, state))
                time.sleep(10)

    def get_project(self, user, name):
        return super().get_repo('program', user, name)

    def list_projects(self, user, filters='*'):
        return super().list_repos('program', user, name)

    def delete_project(self, user, name):
        super().delete_repo('program', user, name)

    def create_dataset(self, dataset: DkubeDataset, wait_for_completion=True):
        assert type(
            dataset) == DkubeDataset, "Invalid type for run, value must be instance of rsrcs:DkubeDataset class"
        super().create_repo(dataset)
        while wait_for_completion:
            status = super().get_repo('dataset', dataset.user, dataset.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['ready', 'failed', 'error']:
                print(
                    "dataset {} - completed with state {} and reason {}".format(dataset.name, state, reason))
                break
            else:
                print(
                    "dataset {} - waiting for completion, current state {}".format(dataset.name, state))
                time.sleep(10)

    def get_dataset(self, user, name):
        return super().get_repo('dataset', user, name)

    def list_datasets(self, user, filters='*'):
        return super().list_repos('dataset', user, name)

    def delete_dataset(self, user, name):
        super().delete_repo('dataset', user, name)

    def create_model(self, model: DkubeModel, wait_for_completion=True):
        assert type(
            model) == DkubeModel, "Invalid type for run, value must be instance of rsrcs:DkubeModel class"
        super().create_repo(model)
        while wait_for_completion:
            status = super().get_repo('model', model.user, model.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['ready', 'failed', 'error']:
                print(
                    "model {} - completed with state {} and reason {}".format(model.name, state, reason))
                break
            else:
                print(
                    "model {} - waiting for completion, current state {}".format(model.name, state))
                time.sleep(10)

    def get_model(self, user, name):
        return super().get_repo('model', user, name)

    def list_models(self, user, filters='*'):
        return super().list_repos('model', user, name)

    def delete_model(self, user, name):
        super().delete_repo('model', user, name)

    def get_head_version(self, category, user, repo):
        pass

    def get_latest_version(self, category, user, repo):
        pass

    def list_versions(self, category, user, repo):
        pass

    def get_version(self, category, user, repo, version):
        pass

    def get_training_outputs(self, user, runname):
        training_run = self.get_training_run(user, runname)
        uuid = training_run['job']['parameters']['generated']['uuid']
        run_lineage = super().get_run_lineage('training', user, uuid)
        return run_lineage['outputs']
