# hackforces-python
Lib for task checking


### How to install

#### Using pip

`pip install git+https://github.com/hackforces/hackforces-python.git`

### Using pypi (only test)

`pip install --index-url https://test.pypi.org/simple/ hackforces`

#### From source

```
git clone https://github.com/hackforces/hackforces-python.git
cd hackforces-python
pip install .
or
python setup.py install --user
```

### Usage

```
from hackforces import HFContest
contest = HFContest(url, contest, task, task_token, user_token='') # initial of instance
contest.check_task(user_token='', flag=' ') # send request after successfully completed task (if user fails, don't use this)
```

`url` **(required)** - address of api in the internet (without tailing **/api/**)
`contest` **(required)** - guid of contest (integer)
`task` **(required)** - guid of task (integer)
`task_token` **(required)** - string for auto accept users solution

`user_token` **(required)** - get this token from user (player)
`flag` **(optional)** - past unique flag these if you want

