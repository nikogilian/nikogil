from tkinter import *
import os
from flask import Flask, render_template_string
from PIL import Image, ImageTk


app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string(html_code)

def publish():
    global html_code
    html_code = html_input.get("1.0", END)
    app.run(host='0.0.0.0', port=80)

root = Tk()
root.geometry('300x250')
root.title('Flask website publisher')

default_html = """<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>"""

html_label = Label(root, text="Code for the flask website goes here:")
html_label.pack()
html_input = Text(root, height=10)
html_input.insert(END, default_html)
html_input.pack()

# Create publish button
publish_button = Button(root, text="Publish this to the web with flask \n (Window will crash. Look in the console for output)", command=publish)
publish_button.pack()

root.mainloop()
