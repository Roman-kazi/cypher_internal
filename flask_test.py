import subprocess
import neo_4j_demo
from flask import Flask, render_template

import easygui

app = Flask(__name__,template_folder='template')


@app.route('/')
def index():

    return render_template('HomePage.html')

#background process happening without any refreshing

@app.route('/background_process_test')
def background_process_test():
    subprocess(file_selector())
    return ('nothing')

def file_selector():

    file_path = easygui.fileopenbox()
    neo_4j_demo.backend(file_path)

    return 0



@app.route('/visualizer')
def visualizer():
    return render_template('Visualizer.html')



if __name__ == "__main__":
    app.run(debug=True)
