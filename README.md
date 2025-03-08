# Run and deploy using Heroku

![Estado del proyecto](https://img.shields.io/badge/status-activo-brightgreen)
![Última versión](https://img.shields.io/github/v/release/AND3SIL4/easy-api)

```sh
heroku login
heroku container:login
heroku create # and get the name returned
heroku container:push web --app [name] # the process will execute it
heroku open --app [name]
```
