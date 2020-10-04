import pathlib
from fabric.api import local, cd, run, env, prefix

PROJECT = pathlib.Path('.').parent.absolute().parts[-1]
env.hosts = ['cloud']


def deploy():
    local('git push')
    with prefix(f'source ~/.virtualenvs/{PROJECT}/bin/activate'):
        with cd(f'~/code/{PROJECT}'):
            run('git pull')
            run('pip install -r requirements.txt')
            run('make dirhtml')
