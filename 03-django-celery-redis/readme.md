## django | celery | redis

#### run celery worker
```py
# first activate env | contain within the project folder
celery -A projectName worker -l INFO
```

#### run celery beat
```py
celery -A projectName beat -l INFO
```

#### run celery-worker + celery-beat (not recommended)
```py
celery -A projectName worker -B -l INFO
```
