# celery learning note

## 1. 运行 celery 项目实例

``` 
docker-compose up -d
```


## 2. redis 优先级任务

运行:

``` 
docker-compose -f docker-compose-redis-priority.yml up
```

celery redis 优先级测试, 参考项目: 
[reference: Tendrid/celery-redis-priority-test](https://github.com/Tendrid/celery-redis-priority-test)
