#!/usr/bin/python3
import requests
from string import ascii_letters, digits
from random import choice
class HFContest:
    """ Class to achieve flags for users"""
    def __init__(self, url, contest, task, task_token, user_token = ""):
        try:
            if not isinstance(url, str):
                raise Exception('url must be str type')
            if not isinstance(contest, int):
                raise Exception('contest must be int type')
            if not isinstance(task, int):
                raise Exception('task must be int type')
            if not isinstance(task_token, str):
                raise Exception('task_token must be str type')
            if user_token is not "" and not isinstance(user_token, str):
                raise Exception('user_token must be str type')
            self.url = url
            self.contest = contest
            self.task = task
            self.task_token = task_token
            self.user_token = user_token
        except Exception as ex:
            print(ex)

    def check_user_token(self, user_token):
        """ Check user token lenght """
        return isinstance(user_token, str) and len(user_token) == 80

    def random_flag(self):
        return ''.join(choice(ascii_letters + digits) for _ in range(30))

    def approve_task(self, user_token = '', flag = ''):
        """ Check task on the selected server """
        user_token = user_token if len(user_token) > 0 else self.user_token
        if not self.check_user_token(user_token):
            return -1, 'User token in incorrect format!'
        data = {
            'flag': flag if flag is not '' else self.random_flag(),
            'contest_guid': self.contest,
            'task_guid': self.task,
            'task_token': self.task_token,
            'token': user_token
        }
        headers = {'user-agent': 'hackforces-client-py/0.0.2'}
        try:
            r = requests.post("{}/api/task.check".format(self.url), data=data, headers=headers, timeout=5)
            if r.status_code == 200:
                return 200, "OK"
            elif r.status_code < 500:
                try:
                    msg = r.json()['message']
                    return r.status_code, msg
                except Exception as ex:
                    return r.status_code, r.text
            else:
                return r.status_code, r.text
        except requests.exceptions.RequestException as ex:
            return -1, ex
