import requests
import json

def send_slack_alert(message):
    post = {	"text":"{0}".format(message)}
    slack_hook = "Your slack hook"
    response_slack = requests.post(slack_hook, data=json.dumps(post),headers={'Content-Type': 'application/json'})


def hello_world():
    send_slack_alert("Hello World")


hello_world()
