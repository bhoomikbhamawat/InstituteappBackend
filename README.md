# InstituteappBackend

## API end points

### check registered
``` http://iitbhuapp.tk/checkreg ```

#### Expected POST req

``` {"email":"asdjabda@akf.com"}```

#### Expected POST res

- Response if anything goes wrong
``` {"status": 0}```

- Response if registered
``` {"status": 1, "name":"testname" , "roll":12313123, "phone": "1232423535", "department":"Mining" }```

- Response if new reg
``` {"status": 2}```

### Login/register
``` http://iitbhuapp.tk/login ```

#### Expected POST req

``` {"email":"asdjabda@akf.com", "name":"testname" , "roll":12313123, "phone": "1232423535", "department":"Mining", "fcmtoken":"2131232dasasdasdasdwasd" }```

#### Expected POST res

- Response if anything goes wrong
``` {"status": 0}```

- Response if registered 
``` {"status": 2}```

- Response if new reg
``` {"status": 1}```


