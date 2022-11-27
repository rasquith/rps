# Rock Paper Scissors Submission

This is a response to following challenge. This project is in progress (not complete).
```
This coding challenge is to implement a two-player game of rock, paper, scissors in the web browser.
```

*PLEASE NOTE: This was an interesting take-home and I lost track of time getting into it. I learned some stuff. I'm pretty sure I went over time. Please judge me accordingly.*

## Architecture

[Flask](https://palletsprojects.com/p/flask/)<br>
[Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)<br>
[Jinja](https://palletsprojects.com/p/jinja/)<br>

What's still missing:
<ul>
<li>A database -- probably a nosql database, like MongoDB or DynamoDB. Each item would hold info for one game and would update as the game state changed.</li>
<li>A JavaScript Socket.IO framework and a JavaScript framework for user interfaces. I dropped some Jinja templates in here to get something down, but the front end is really not there.</li>
<li>Tests...no tests yet, but there should be some there. I'd use pytest for the python functions.</li>
<li>The infrastructure to host this :D</li>
</ul>


## Getting Started

You can download this project from [github](https://github.com/rasquith/rps).

