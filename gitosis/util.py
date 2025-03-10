import errno
import os
from configparser import NoSectionError, NoOptionError

def mkdir(*a, **kw):
    try:
        os.mkdir(*a, **kw)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise

def getRepositoryDir(config):
    repositories = os.path.expanduser('~')
    try:
        path = config.get('gitosis', 'repositories')
    except (NoSectionError, NoOptionError):
        repositories = os.path.join(repositories, 'repositories')
    else:
        repositories = os.path.join(repositories, path)
    return repositories

def getGeneratedFilesDir(config):
    try:
        generated = config.get('gitosis', 'generate-files-in')
    except (NoSectionError, NoOptionError):
        generated = os.path.expanduser('~/gitosis')
    return generated

def getSSHAuthorizedKeysPath(config):
    try:
        path = config.get('gitosis', 'ssh-authorized-keys-path')
    except (NoSectionError, NoOptionError):
        path = os.path.expanduser('~/.ssh/authorized_keys')
    return path

def getSSHPrincipalsPath(config):
    try:
        path = config.get('gitosis', 'ssh-principals-path')
    except (NoSectionError, NoOptionError):
        path = os.path.expanduser('~/.ssh/principals')
    return path

def getAllowedSSHPrincipals(config):
    try:
        principals = config.get('gitosis', 'allowedPrincipals')
    except (NoSectionError, NoOptionError):
        principals = "git"
    return principals
