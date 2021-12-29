# BudgetItem

### Migrations
Assumes existing MySQL server.
- Create MySQL schema 'budget'
- Setup/Run Migration
```
make migrate
```

### Building/Running Locally
Assumes existing MySQL server.
- Create .env file in project root with the following configs
  - SQLALCHEMY_DATABASE_URI
  - SQLALCHEMY_TRACK_MODIFICATIONS
- Install Project dependencies
```
make dependencies
```
- Create python virtual environment
```
make install
```
- Run
```
make run
```

### Building/Running via Docker
Assumes existing MySQL server and docker installed.
- Create .env.docker file in project root with the following configs
  - SQLALCHEMY_DATABASE_URI
  - SQLALCHEMY_TRACK_MODIFICATIONS
- Build dockerfile
```
make build-docker
```
- Run dockerfile
```
make run-docker
```


### Run Tests
Assumes project is installed locally.

