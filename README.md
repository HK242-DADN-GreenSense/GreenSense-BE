# GreenSense-BE

## Setting up the environment

- Create an python virtual environment by running the following command in the terminal

``` bash
    python3 -m venv .venv
```

- Activate the virtual environment
  
``` bash
    . .venv/bin/activate
```

- Install all library listed in the file `requirement.txt`
  
``` bash
    pip install -r requirement.txt
```

## Run monitor and DB updator process

``` bash
    cd .. && python3 -m greensense_be.iot_monitor.app
```

## Run Flask

Open another terminal in greensense_be folder and run the following command:

``` bash
    cd .. && python3 -m greensense_be.__init__
```
