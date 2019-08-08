"""

        - says file is written when it is not

    Optional:
        - check if file exists
        - don't close without saving
        - time since saved
            - Current time
            - diff
        - undo/ redo
        - syntax highlighting
"""

PROJECT_DIRS = "dirs.conf"
PROJECT_DIRS_LIST = ""
PROJECT_DIR_FIRST = ""

from flask import Flask, request
app = Flask(__name__)
import re
import datetime
import os


@app.route ( '/')
def hello_world():
    return "..."

@app.route('/save/', methods=['GET', 'POST'])
def save () :
    print("dsaf")
    if 'path' in request.form and 'content' in request.form:
        with open(request.form['path'], "w") as f1:
            f1.write(request.form['content'])
    now = datetime.datetime.now()
    return "Saved: " + now.strftime("%Y-%m-%d %H:%M:%S")

@app.route('/dirlist/', methods=['GET' , 'POST'])
def dirList() :
    output= ""
    if 'project_dir_selector' in request.form:
        filter =""
        if 'filter' in request.form:    # filter is optional
            filter = request.form['filter']
        output += dirlist2(request.form['project_dir_selector'], filter)
    return output

def dirlist2 (dir, filter):
    output = ""
    files = os.listdir(dir)
    print("debug:" + filter)
    if filter != "":
        for i in files:
            m = re.search(filter, i)
            if m:
                output += "<tr><td onclick=\"openMyFile('" + dir + "/" + i + "')\">" + i + "</td></tr>"
    else:
        for i in files:
            output += "<tr><td onclick=\"openMyFile('" + dir + "/" + i + "')\">" + i + "</td></tr>"
    return output

@app.route('/openmyfile/', methods=['POST'])
def openMyFile ():
    output = ""
    if 'path' in request.form:
        with open(request.form['path'], "r") as f1:
            output = f1.read()
    return output

@app.route('/edit/', methods=['GET', 'POST'])
def edit() :
    f1 = open("edit.html", "r")
    output = f1.read()
    f1.close()

    d = dirlist2(PROJECT_DIR_FIRST, "")
    output = re.sub(r'<!-- PROJECT_DIRS_LIST -->', PROJECT_DIRS_LIST, output)
    output = re.sub(r'<th><td>---</td></th>', d, output)
    print(d)
    print(PROJECT_DIR_FIRST)

    datal = ""
    if 'data1' in request.form:
        # fill editor with data from before submit
        datal += request.form['data1']
        output = re.sub(r'<!--DATA1 GOES HERE-->', data1, output)
    else:
        # fill editor with blank initial data
        output = re.sub(r'<!--DATA1 GOES HERE-->', "", output)

    if 'filename1' in request.form:
        filename1 = request.form['filename1']
        output = re.sub(r'<!--FILE1 GOES HERE-->', filename1, output)
        f2 = open(filename1, "w")
        f2.write (data1)
        f2.close()
    else:
        output = re.sub(r'<!--FILE1 GOES HERE-->', "", output)

    return output

@app.route('/<string:name>/')
def my_default(name):
    f1 = open("static_files/" + name, "rb")
    data1 = f1.read()
    f1.close()
    return data1

f1 = open(PROJECT_DIRS)
dirs = f1.readlines()
f1.close()
PROJECT_DIR_FIRST = dirs[0].strip()
PROJECT_DIRS_LIST += "<select id='project_dir_selector' onchange='projectDirSelect()'>"
for v in dirs[:]:
    PROJECT_DIRS_LIST += "<option value=\"" + v.strip() + "\">" + v.strip() + "</option>"
    PROJECT_DIRS_LIST += "</select>"

app.run ()  # local host
#app.run (host= '0.0.0.0') # external
