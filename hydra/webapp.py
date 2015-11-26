import logging

from flask import Flask, request
from jinja2 import Environment, PackageLoader


def setup_logging():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s: '
                               '(%(threadName)-10s) %(message)s')


app = Flask('hydra-ui', static_folder='hydra_ui/static/AdminLTE-2.3.0', static_url_path='/static')


@app.route('/ui', methods=['GET'])
def index():
    if request.method == 'GET':
        env = Environment(loader=PackageLoader('hydra_ui'))
        template_index = env.get_template('template_index.html')
        return template_index.render()


@app.route('/ui/pipelines', methods=['GET'])
def pipeline_view():
    if request.method == 'GET':
        env = Environment(loader=PackageLoader('hydra_ui'))
        template_index = env.get_template('template_pipeline.html')
        return template_index.render()


if __name__ == "__main__":
    setup_logging()
    app.run()