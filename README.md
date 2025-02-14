# Run and deploy using Heroku

```sh
heroku login
heroku container:login
heroku create # and get the name returned
heroku container:push web --app [name] # the process will execute it
heroku open --app [name]
```
