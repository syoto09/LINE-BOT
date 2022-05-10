LINE bot
===============
![cosine](https://lh3.googleusercontent.com/0gmz1W51c7NuDAGp3Zgu6lhpyI0qZeWM9Dpj0g66hAwQlvsnSeSNoUXaK8IWClOZWJnLztLOIoFy0s68dNcEJBtGhaJZtDVTzSDK647WFFYlTDG5mYUZxI0_NDgDKxetyc0df_9Dig=w2400)
## Technology 
 * [LINE account](https://line.me/en/)
 * [Python](https://www.python.org/downloads/) 
 * [Flask](https://flask.palletsprojects.com/en/2.1.x/)
 * [ngrok](https://ngrok.com/)

### 1, Create LINE channels


### 2, Construnc the environment 


    $ pip install line-bot-sdk
    $ pip install flask 
### 3, Implement the bot program  [Reference](https://github.com/line/line-bot-sdk-python)

### 4, Excute Flask and ngrok
    $ flask run 
    ./ngrok http 5000



### @app.route("/callback") 
 1 - If you sent the message to my bot, my bot will send your message back  to you

 2 - If you sent "Thank you" to my bot, my bot reply "No problem" 

 