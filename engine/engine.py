import threading
from listeners import base_listener
from parsers import base_parser
from rules import rules_engine
from actions import base_action


class Engine(threading.Thread):
    def __init__(self, listener, parser, rules_engine, actions):
        threading.Thread.__init__(self, name='Engine')
        self._listener = listener
        self._parser = parser
        self._rules_engine = rules_engine
        self._action = actions


if __name__ == '__main__':
    listener = base_listener.BaseListener()
    parser = base_parser.BaseParser()
    rules_engine = rules_engine.RulesEngine()
    actions = list()
    actions.append(base_action.BaseAction)

    engine = Engine(listener, parser, rules_engine, actions)

    engine.start()
