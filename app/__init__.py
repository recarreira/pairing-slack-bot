from slacker import Slacker

def run(slack_key):
    slack = Slacker(slack_key)

    slack.chat.post_message('#general', 'Opa')
