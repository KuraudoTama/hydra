class BaseAction(object):
    def __init__(self, config):
        raise NotImplementedError

    def do(self):
        raise NotImplementedError

