# Price-Negotiator FastAPI OpenAI Chat

This repository contains a simple web application that utilizes FastAPI and OpenAI to create a chat interface. Users can input messages, and the assistant will respond based on the OpenAI model's predictions.

This project creates a simple web-based chat interface using FastAPI and OpenAI's language model. Users can type messages into a web form, and the application will send these messages to the OpenAI model, which generates a response. The response is then displayed back on the web page, simulating a conversation between the user and an AI assistant.

Here's a more detailed breakdown of what the project does:

Web Interface:

Provides an HTML form where users can input their messages.
Displays the user's message and the assistant's response on the same page.
Backend Server:

Uses FastAPI to set up a server that listens for incoming requests from the web interface.
Handles form submissions from the web interface, sending the user's message to the OpenAI API.
Receives the response from the OpenAI API and sends it back to the web interface to be displayed.
OpenAI Integration:

Connects to the OpenAI API using the provided API key.
Sends user input to the OpenAI model and retrieves the generated response.
Overall, this project demonstrates how to integrate FastAPI with OpenAI to create an interactive chat application that leverages advanced language processing capabilities.
