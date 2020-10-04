from fabric.api import local, cd, run, env, prefix

env.hosts = ['cloud']


def deploy():
    local('git push')
    with prefix('source ~/.virtualenvs/aprendepython/bin/activate'):
        with cd('~/code/aprendepython'):
            run('git pull')
            run('pip install -r requirements.txt')
            run('make dirhtml')
