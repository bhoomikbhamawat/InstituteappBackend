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
``` {"status": 1, "name":"testname" , "roll":12313123, "phone": "1232423535", "department":"Mining", "year":"2019" }```

- Response if new reg
``` {"status": 2}```

_______

### Login/register
``` http://iitbhuapp.tk/login ```

#### Expected POST req

``` {"email":"asdjabda@akf.com", "name":"testname" , "roll":12313123, "phone": "1232423535", "department":"Mining", "year":"2019", "fcmtoken":"2131232dasasdasdasdwasd" }```

#### Expected POST res

- Response if anything goes wrong
``` {"status": 0}```

- Response if registered 
``` {"status": 2}```

- Response if new reg
``` {"status": 1}```

_________

### Feed stories
```http://iitbhuapp.tk/feed```

#### Expected POST req

``` {"roll":15075002}```

#### Expected POST res

- Response if anything goes wrong
``` {"status": 0}```

- Response if everything is fine

```{
    "status": 1,
    "notif": [
        {
            "club": "Indian Music Club",
            "clubimage": "/media/download.png",#will appear when club image is added
            "council": "Cultural Council",
            "councilimage": "/media/abc.jpeg",#will appear when council image is added
            "title": "asd",
            "description": "ad",
            "datetime": "2019-05-31T10:53:10Z",
            "location": "ds",
            "viewedcount": 1,
            "interestedcount": 1,
            "notifid": 1
        },
        {
            "club": "Western Music Club",
            "council": "Cultural Council",
            "councilimage": "/media/abc.jpeg",#will appear when council image is added
            "title": "test1",
            "description": "test",
            "image": "/media/back.jpg",
            "datetime": "2019-05-31T17:55:29Z",
            "location": "testloc",
            "viewedcount": 1,
            "interestedcount": 0,
            "notifid": 2
        }
    ]
}
```
___________
### Interested
```http://iitbhuapp.tk/interested```

#### Expected POST req

``` {
	"roll":213,
	"notifid":1
}
```

#### Expected POST res

- Response if anything goes wrong
``` {"status": 0}```

- Response if everything is fine
``` {"status": 1}```

- Response if already intersted
``` {"status": 2}```


___________
### Complain
```http://iitbhuapp.tk/postcomplain```

#### Expected POST req

``` {
	"roll":213,
	"complain":"test complain",
	"anonymous":1 #0 if you dont want to be anonymous
}
```

#### Expected POST res

- Response if anything goes wrong
``` {"status": 0}```

- Response if everything is fine
``` {"status": 1}```

___________________

### Contributors
[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/0)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/0)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/1)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/1)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/2)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/2)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/3)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/3)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/4)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/4)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/5)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/5)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/6)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/6)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/7)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/7)
