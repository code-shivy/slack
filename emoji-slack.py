import requests
import json

def send_slack_alert(message):
    print("Sending slack_alert")
    post = {	"text":"{0}".format(message)}
    slack_hook = "Slack webhook  URL"
    response_slack = requests.post(slack_hook, data=json.dumps(post),headers={'Content-Type': 'application/json'})
    print(response_slack)


def hello_world():
    message1 = """
    :large_green_circle: Hello World
    """

    send_slack_alert(message1)

    message2 = """ 
    :red_circle: Error Hello World"""

    send_slack_alert(message2)
hello_world()
