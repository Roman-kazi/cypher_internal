import tkinter
import neo_4j_demo
from flask import Flask, render_template,request
#import visualization_backedend
from tkinter import filedialog

app = Flask(__name__,template_folder='template')


@app.route('/')
def index():

    return render_template('HomePage.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    neo_4j_demo.backend(file_path)
    return ('nothing')

@app.route('/visualizer')
def visualizer():
    return render_template('Visualizer.html')



if __name__ == "__main__":
    app.run(debug=True)