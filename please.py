from flask import Flask, render_template, request, redirect, url_for, Response
import json

fembot = Flask(__name__)

@fembot.route('/payload', methods=['GET','POST'])
def parseIssue():
  if request.method == 'GET':
    return "This works, but you need to use POST, kid."
  if request.method == 'POST':
      issue = json.loads(request.form.get('payload'))
      print issue['issue'].keys()
      return "OK"
  
if __name__ == "__main__":
    fembot.run(debug=True, host="0.0.0.0",port=4567)
