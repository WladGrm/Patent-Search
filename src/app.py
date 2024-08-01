from flask import Flask, render_template, request
from search import *
from lang_processor import *

lang_processor = TranslatorT5()
semanticsearch = SemanticSearch()


app = Flask(__name__)


@app.route('/')
def msg():
    return render_template('index.html')

                           
@app.route("/all-mpnet-base-v2", methods=['POST', 'GET'])
def search():
    search_term = request.form["input"]
    D, I = semanticsearch.s_v([lang_processor.translate(search_term)], index, num_results=20)
    res = semanticsearch.indx(I)
    return render_template('search.html', res=res)


# main driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
