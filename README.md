# A-Simple-Note-Taking-Web-App
An easy to use and deploy web app built using Flask

# Features:

* Simple flask Web application, easy to use and *very* easy to deploy locally
* Written in simple Python. Even a beginner Python developer can contribute to this
* Support for mysql, so you can easily play with it
* REST API for retrieving data easily

# Requirements:

Execute the following command to install the required third party libraries:<br />

`pip3 install -r requirements.txt`

# Usage:
Clone this repository:

`git clone https://github.com/OmkarPathak/A-Simple-Note-Taking-Web-App.git`

Install the dependencies by simply executing:

`pip3 install -r requirements.txt`

Run this command to start the app:

`python3 rest.py

Visit `0.0.0.0:5000` on your web browser

Happy Noting :)

Built with ♥ by [`Ankit Jain`]

# Results

## Creating a new note

Request POST : http://localhost:5000/add
request body json format

{
	"note":"I am making flask api",
}

## Viewing a note

Request GET: http://localhost:5000/notedata
request with querystring 
http://localhost:5000/notedata/3

## Delete a note

Request with querystring  DELETE : http://localhost:5000/delete/2


## Update note data

Request PUT : http://localhost:5000/update
request body

{
	"id":2,
	"note":"API complete"
}



# Thanks