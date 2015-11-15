import threading


class Engine(threading.Thread):
    def __init__(self, listener, parser, rule, actions):
        self._listener = listener
        self._parser = parser
        self._rule = rule
        self._action = actions


if __name__ == '__main__':
    engine = Engine()
    engine.start()
