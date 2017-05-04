import os
from app import run

if __name__ == '__main__':
    run(os.environ.get('SLACK_KEY'))
