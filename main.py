from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


@component
def mongoDB():
    
    ## Creating state
    alltodo = use_state([])
    ownername, set_ownername = use_state("")
    petname, set_petname = use_state("")
    password, set_password = use_state(0)
    gmail, set_gmail = use_state("")

    def mysubmit(event):
        newtodo = {"ownername": ownername,"petname":petname, "password": password, "gmail":gmail}

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo)
          # function call to login function using the submitted data
    

    # looping data from alltodo to show on web

    list = [
        
    ]

    def handle_event(event):
        print(event)

    return html.div(
        
      {"style": 
         {"padding": "50px",
          "background_image":"url(https://reactpy.neocities.org/photo/bigdogs.jpg)", 
          "background-size":"cover",
           "margin": "0px",
           "min-height": "700px",
           "min-width":"700px"
}
           },
           
        
        ## creating form for submission\
        html.form(
            {"on submit": mysubmit},
            html.h1({"style": {"font-family": "Arial", "font-size": "350%","color":"#7399bf"}}
                    ,"Login to Baw-Baw.com"),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Owner Name",
                    "on_change": lambda event: set_ownername(event["target"]["value"]),
                    "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "4px outset",
                            "border-radius": "10px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",                   
                            "outline": "none"}
                }
            ),
            html.br(),
            html.br(),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Pet Name",
                    "on_change": lambda event: set_petname(event["target"]["value"]),
                    "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "4px outset",
                            "border-radius": "10px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",                   
                            "outline": "none"}
                }
            

            ),
            html.br(),
            html.br(),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Password",
                    "on_change": lambda event: set_password(event["target"]["value"]),
                    "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "4px outset",
                            "border-radius": "10px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",                   
                            "outline": "none"}
                }
            

            ),
            html.br(),
            html.br(),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Gmail",
                    "on_change": lambda event: set_gmail(event["target"]["value"]),
                    "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "4px outset",
                            "border-radius": "10px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",                   
                            "outline": "none"}
                }

            ),
            # creating submit button on form
            html.br(),
            html.br(),
            html.button(
                {
                    "type":"Login",
                    "on_click": event(
                        lambda event: mysubmit(event), prevent_default=True
                    
                    ),
                    "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "groove",
                            "border-color": "#92a8d1",
                            "border-radius": "10px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box", 
                            "outline": "none"}
                },
                "Login",
            ),
        
        ),
        html.ul(list),
    )


app = FastAPI()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://dushan123:dushan2002@cluster0.gsl4t7v.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))
db = client["SignUp"]
collection = db["users"]
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



def login(
    login_data: dict,
):  
    # removed async, since await makes code execution pause for the promise to resolve anyway. doesnt matter.
    ownername = login_data["ownername"]
    petname = login_data["petname"]
    password = login_data["password"]
    gmail = login_data["gmail"]
    # Create a document to insert into the collection
    document = {"Ownername": ownername,"Petname": petname, "password": password,"gmail": gmail}
    # logger.info('sample log message')
    print(document)

    # Insert the document into the collection
    post_id = collection.insert_one(document).inserted_id  # insert document
    print(post_id)

    return {"message": "Login successful"}


configure(app, mongoDB)
