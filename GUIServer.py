Optional:
- check if file exists
don't close without saving
time since saved
Current time
diff
undo/ redo
- syntax highlighting
PROJECT_DIRS = "dirs.conf"
PROJECT_DIRS_LIST =
PROJECT_DIR_FIRST =
from flask import Flask, request
app Flask(_name_)
import re
import datetimee
import OS
@app.route ( '/'))
def hello_world ):
return...
@app.route ( ' /save/', methods = [ 'GET',
def save () :
'POST' ])
print("dsaf")
if 'path' in request.form and 'content' in request.form
with open (request.form[ "path' ], "w") as f1:
f1.write (request.form[ 'content'])
now = datetime.datetime.now()
return "Saved:
+ now.strftime("%Y-%m-%d %H:%M:%S")
@app.route ( "/dirlist/', methods=[ 'GET' , 'POST'1)
def dirList() :
output= ""
if 'project_dir_selector' in request. form:
filter ="
if 'filter' in request.form:
# filter is optional
filter = request.form['filter ']
output += dirlist2(request. form[ 'project_dir_selector ' 1, filter)
return output
def dirlist2 (dir, filter):
output =
files = os.1istdir (dir)
print( "debug:"+ filter)
if filter != ":
for i in files:
m = re.search (filter, i)
if m:
output += "<tr><td onclick=\ "openMyFile("" + dir + "/" + i + "')\">" + i
+ "</td></tr>"
else
for i in files
output += "<tr><td onclick=\ "openMy File('" + dir + "/"+i+ "')\">" + i+
"</td></tr>"
return output
@app.route ( "/openmyfile/', method s = [ ' POST'])
def openMy File ():
output =
if 'path' in request.form:
with open ( request.form[ ' path' ], "r") as f1
output = f1. read ()
return output
@app.route ( "/edit/', methods = [ 'GET',
def edit() :
' POST' ])
f1 = open ("edit.html",
output = f1.read ()
f1.close()
"r")
d = dirlist2 (PROJECT DIR_FIRST, "")
output = re.sub (r'<! -- PROJECT_DIRS_ LIST
output = re.sub (r' <th> <td> - - - </td> </th> ',
-> ', PR0J ECT_DIRS_LIST,
d, output)
output)
datal = ""
if 'data1' in request.form:
# fill editor with data from before submit
datal += request.form[ "data1']
output = re.sub (r'<! - - DATA1 GOES HERE - -> ' , data1, output)
else:
# fill editor with blank initial data
output = re.sub (r'<! - - DATA1 GOES HERE- - > ',
output)
if 'filename1 in request.form:
filename1 = request. form[ 'filename1']
output = re.sub (r'<! - - FILE1 GOES HERE- ->',
f2 = open (filename1, "w")
f2.write (data1)
f2.close()
filename1,
output)
else:
output)
output = re.sub (r'<! - - FILE1 GOES HERE- ->'
return output
@app.route ( '/<string: name>/)
def my_default (name):
f1 = open ("static_ files/" + name, "rb")
data1 = f1.read()
f1.close()
return data1
f1 = open (PROJ ECT_DIRS5)
dirs = f1.readlines ()
f1.close()
PROJECT DIR FIRST = dirs [0]. strip ()
PROJECT DIRS LIST += "<select id='project_dir_selector' onchange=' projectDirselect () '>"
for v in dirs[:]:
PROJECT DIRS LIST += "<option value=\ +V.Strip() + "\">" + V.strip () +"</option>"
PROJECT DIRS_LIST += "</select>"
#app.run ()
app.run (host= '0.0.0.0')
