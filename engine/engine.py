from actions import base_action
from listeners import base_listener
from parsers import base_parser
from rules import rules_engine


class Engine(object):
    def __init__(self, **params):
        self._listener = params.get('listener')
        self._filter = params.get('filter')
        self._rule_engine = params.get('rule_engine')
        self._actions = params.get('actions')

    def launch(self):
        pass

    def terminate(self):
        pass




if __name__ == '__main__':
    listener = base_listener.BaseListener()
    parser = base_parser.BaseParser()
    rules_engine = rules_engine.RulesEngine()
    actions = list()
    actions.append(base_action.BaseAction)

    engine = Engine(l=listener)
    engine.start()
