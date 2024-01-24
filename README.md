# Django Chatbot with ChatGPT

## Overview
This is a really small project with just a few views a bunch of JS code in the template.
The entire app consiste in a single chat where you can actually chat with ChatGPT.

## Python functionality

There two views inside of `views.py` that are made to make calls to the ChatGPT API. I've used documentations and articles in order to understand its functionalities.

- The first function-based view is `chat` and it renders the chat HTML
- This function also takes the messages comming from the JS code and send this message to the second View
- The second function-based view named `ask_openai` use the API params such as "model", "messages" and their respective format to send the previous message
- It received a JSON response and I just take the value from the key that I need `response.choices[0].message.content.strip()`


## JS functionality:

The JS code is complex. JS is not my main coding language, so I did a lot of research and investigation to make it work. Here are the steps:

- Gets the elemnts from the HTML
- Listen to the submit button and if the message (the user message) is empty then do nothing
- Creates a new element for the message sent and then clean/empty the user input box
- Then make a POST request via form encoding and get the JSON response
