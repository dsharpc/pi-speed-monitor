# Pi Speed Monitor ⏲️
Project for tracking internet download and upload speeds. The app uses a crontab schedule to make measurements every 10 minutes and store them in a Postgres database.

**Note: This tool was built and tested to work on a Raspberry Pi 4 running 64-bit Ubuntu 20.04**

# Execution ⚙️

To run the system, clone the repo and use the following to create the database and initialise the cronjob.

```
docker-compose up -d
```

If it's the first time the containers have been initialised, use the following command to create the table in the database:

```
docker-compose exec app python main.py build_table
```

Once the table exists, you can either manually run the following to execute a command:

```
docker-compose exec app python main.py measure
```

This will make a speed measurement and write to the database. 

Otherwise, cron will execute this command every 10 minutes by default. To change the frequency, update the crontab file and then rebuild the image.

# Superset  📊

The superset container will be initialised as part of the Docker Compose. It runs a development server by default. To access it on your browser, go to:

```
# if running locally
localhost:8088

# if running on a different server (RPi)
<ip_address>:8088
```

You should now see the superset login page. The login details are set in the Dockerfile. Username is `admin` and password is `admin`.

The connection to the local database has already been set-up. Click on the Speed Measurements dashboard to explore the data.
