---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    NOTE: This is a guide on how to install pre-requisites, run and test the results of a simple Flask-based application reflecting the requirements for a technical interview consisting of using simple API requests
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Step 0

* Install Python and Pip as libraries ( for Linux Debian Only ), for Windows systems one needs to go to the official Python website https://www.python.org/downloads/:

```bash
  sudo apt update
  sudo apt install python3
  sudo apt install python3-pip
  sudo apt git # in case the user does not have git

```

### Step 1 

* Install 'requests' and 'Flask' python modules with pip:

```bash
  pip install Flask
  pip install requests
```

### Step 2

* Clone the git repo with the application

```bash
git clone https://github.com/j52794dd/Epilogue_Interview.git
```

### Step 3

* Go in the application folder and start it, then open your preferred browser and type this address: http://127.0.0.1:5000

```bash
cd Epilogue_Interview
flask run # This will automatically open the port 5000 of the localhost
```

### (Optional) Step

Open the application with a different port ( here port 9875 will be used, but any available port can be chosen )

```bash
sudo ss -ltnp  # Check listening ports
flask run --port 9875 # Run the application on the port 9875
```
Access the results:

* http://127.0.0.1:9875

  It should look like this:
  
  ![image](https://github.com/j52794dd/Epilogue_Interview/assets/73079562/7829a56c-0b00-47bc-bce7-9c6ffabd9af6)

