from pyinstrument import Profiler
from flask import Flask, request, g, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return 'Управление дроном'

@app.before_request
def before_request():
    #if "profile" in request.args:
    g.is_profiling = "profile" in request.args
    if g.is_profiling:
        g.profile = Profiler()
        g.profile.start()

@app.after_request
def after_request(response):
    if g.is_profiling:
        g.profile.stop()
        output_html = g.profile.output_html()
        return make_response(output_html)
    return response

if __name__ == "__main__":
    app.run(debug=True)
