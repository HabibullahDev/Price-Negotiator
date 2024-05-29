from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
#from fastapi.responses import HTMLResponse
import openai 
import os
from fastapi.responses import JSONResponse


app = FastAPI()

# Set OpenAI API key
openai.api_key = ''
product_name = "Samsung S21"
retail_price = 1000
minimum_price = 600
# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Templates for rendering HTML with Streamlit
templates = Jinja2Templates(directory=current_dir)

#templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))
# Templates for rendering HTML with Streamlit
#templates = Jinja2Templates(directory="templates")

# Function to update messages in the conversation
def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

# Function to get response from the GPT model
def get_chatgpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    return response['choices'][0]['message']['content']

# Dependency to manage the 'messages' state across requests
def get_messages():
    # You can use a database or some other persistent storage instead
    return [
    {"role": "system", "content": f"Your goal to increase sales based on ${product_name} , ${retail_price} and discounted ${minimum_price} price. Respond to customer on ${product_name} start with its ${retail_price}. You are required to maintian the ${minimum_price} threshold, never offer below ${minimum_price} no matter how long customer negotiates, never disclose ${minimum_price} price to customer. Avoid offering a price lower than what the customer proposes, especially if it surpasses previous offers and is above the ${minimum_price}. Negotiate prices within the range of ${retail_price} and the ${minimum_price} never offer below the ${minimum_price} or disclosing the ${minimum_price}."},
    {"role": "user", "content": f"I am a customer I want to buy ${product_name} with negotiation."},
    {"role": "assistant", "content": f"Your job to help in find the deals on the ${product_name} that customer are interested in. Don't offer extra packages with product, your goal is to sell only ${product_name}. Don't go below ${minimum_price}. Thank you for your offer. I am pleased to inform you that we can accept this offer as it is close to our retail price of ${retail_price} for the ${product_name}. This is an excellent choice, and I amm sure you will be very satisfied with your purchase. Shall we proceed with the transaction at this price?. Maintain a adaptive conversation flow, emphasizing the value of the product, and never disclose the ${minimum_price} during negotiations. Maintian the long term negotiations, do not accept the customer offer instantly on ${minimum_price} at first, try to negotiate start from ${retail_price}. In case customer offers you better price which is above than ${retail_price}, then do Thank You to customer and accept that offer."},
]


# Route for handling FastAPI page
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat", response_class=JSONResponse)
def chat(request: Request, user_input: str = Form(...), messages: list = Depends(get_messages)):
    messages = update_chat(messages, "user", user_input)
    model_response = get_chatgpt_response(messages)
    messages = update_chat(messages, "assistant", model_response)

    return {"user_input": user_input, "model_response": model_response}

