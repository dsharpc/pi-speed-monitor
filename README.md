# pi-speed-monitor
Project for tracking internet download and upload speeds. The app uses a crontab schedule to make measurements every 10 minutes and store them in a Postgres database.


# Requirements

For development in a non arm32 system (RPi's architechture), you need to follow
the following steps to install qemu and enable it in Docker. [Source][https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/]

```
sudo apt-get install qemu binfmt-support qemu-user-static # Install the qemu packages
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes # This step will execute the registering scripts

docker run --rm -t arm64v8/ubuntu uname -m # Testing the emulation environment
#aarch64
```

# Execution  

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