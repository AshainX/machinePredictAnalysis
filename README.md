# Machine Predict Analysis REST API

This repository contains a REST API built using FastAPI for predicting the machine downtime. The API uses a pre-trained logistic regression model.

## Clone the Repository

Check if git is installed by going into your terminal or command prompt and type 
```bash
 git --version
```
if it shows "git version 2.47.1.windows.2" etc then its installed otherwise install it from below website according to your distro you are using
[Install GIT Link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

To clone the repository, run the following command in your terminal:

```bash
git clone https://github.com/AshainX/machinePredictAnalysis.git
cd machinePredictAnalysis
```

## Setting Up the Environment

Ensure you have Python installed (version 3.8 or higher is recommended). It is advisable to use a virtual environment for this project.

### Create a Virtual Environment

Run the following command to create a virtual environment:

```bash
python -m venv venv
```
### Activate the Virtual Environment

- **On Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **On MacOS**:
  ```bash
  source venv/bin/activate
  ```
#### Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the API
To run the API, use uvicorn, a fast ASGI server:

```bash
uvicorn modelprediction:app --reload
```
then you can check the server at port given there you can for example :

```bash
#this is for example only
INFO:     Will watch for changes in these directories: ['C:\\Users\\ashut\\Documents\\GitHub\\machinePredictAnalysis']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28372] using WatchFiles
INFO:     Started server process [14224]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

This will start the server then you can go to browser and there wont be showing anything 
here we will open Postman:

## Testing the API with Postman

1. **Open Postman** and create a new request.
2. **Set the request method** to `POST`.
3. **Enter the URL**: `http://localhost:8000/predict` or `http://127.0.0.1:8000/predict` as your server is written there.
4. **In the body**, select `raw` and set the format to `JSON`. Use the following format for input data:

   ```json
   {
     "Temperature": 45.0,
     "Run_Time": 120.5
   }
   ```

   you will get an output in response section down below for example:

  ```json
  {
    "Downtime": "Yes",
    "Confidence": 0.77
  }
  ```

