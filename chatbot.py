import nltk
from nltk.chat.util import Chat, reflections
from tkinter import *
from PIL import Image, ImageTk
pairs = [
    [r"my name is (.*)",["Hello %1, How are you today ?",]],
    [r"I am (.*)",["Hello %1, How are you today ?",]],
    [r"hi|hey|hello", ["Hello!", "Hey there!", "Hi! How can I help you?"]],
    [r"what is your name?|what's your name?", ["I am a chatbot.", "You can call me ChatBot."]],
    [r"how are you ?", ["I'm just a bot, but I'm here to help you!", "I don't have feelings, but thanks for asking."]],
    [r"sorry (.*)",["Its alright","Its OK, never mind",]],
    [r"I'm fine|fine|I'm good",["Great to hear that, How can I help you?",]],
    [r"i'm (.*) doing good",["Nice to hear that","How can I help you?:)",]],
    [r"(.*) age?",["I'm a computer program dudenSeriously you are asking me this?",]],
    [r"what (.*) want ?",["Make me an offer I can't refuse",]],
    [r"(.*) (location|city) ?",['karachi',]],
    [r"i work in (.*)?",["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]],
    [r"(.*)raining in (.*)",["No rain since last week here in %2","Damn its raining too much here in %2"]],
    [r"how (.*) health(.*)",["I'm a computer program, so I'm always healthy ",]],
    [r"(.*) (sports|game) ?",["I'm a very big fan of Football",]],
    [r"who (.*) sportsperson ?",["Messy","Ronaldo","Roony"]],
    [r"who (.*) (moviestar|actor)?",
    ["Fahad Mustafa",'Mehwish Hayat','Humayoun Saeed']],
    [r"i am looking for online guides and courses to learn data science, can you suggest?",["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]],
    [r"quit",["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]],
    [r"bye|goodbye", ["Goodbye! Have a great day.", "See you later!", "Bye!"]],
    [r"how is the weather in (.*)?", ["The weather in %1 is currently %2.", "I'm not sure. You can check a weather website for accurate information."]],
    [r"tell me a joke|joke", ["Why don't scientists trust atoms? Because they make up everything!", "I'm afraid I'm not very good at telling jokes."]],
    [r"give me advice|advice", ["Don't worry about things you can't control.", "Take deep breaths and try to relax.", "Stay positive and keep moving forward."]],
    [r"tell me about (.*)", ["%1 is a fascinating topic. I can look up more information for you if you'd like."]],
    [r"thank you|thanks", ["You're welcome!", "No problem.", "Glad I could help!"]],
    [r"yes|yeah|ofcourse",["Okay then, let's Google it!",]],
    [r"okay|sure|Alright|Alright then", ["You're welcome!", "No problem.", "Glad I could help!"]],
    [r"help", ["Sure, what do you need help with?", "I'm here to assist you. What can I do for you?"]],
    [r".*", ["I'm not sure I understand.", "Could you please rephrase that?", "I'm still learning. Can you ask me something else?"]]
]

window=Tk()

window.title("CHATBOT")
window.geometry("580x660")
window.maxsize(580, 660)
window.minsize(300, 300)
window.config(bg='#2F4F4F')
chatbot = Chat(pairs, reflections)

def send(event=None):
    user_input = entry.get()
    response = chatbot.respond(user_input)
    chat_history.config(state=NORMAL)
    chat_history.insert(END, "You: " + user_input + "\n")
    chat_history.insert(END, "Bot: " + response + "\n\n")
    chat_history.config(state=DISABLED)
    entry.delete(0, END)
def resize_image(image_path, new_width, new_height):
    image = Image.open(image_path)
    resized_image = image.resize((new_width, new_height))
    return ImageTk.PhotoImage(resized_image)
label_frame = Frame(window, bg="#2F4F4F")
label_frame.pack(fill=X)

greeting_label = Label(label_frame, text="HEY! HOW CAN I HELP YOU?\nLET'S HAVE SOME CONVERSATION!", height=3, font=("Hobo Std", 16,'bold'), bg="#2F4F4F", fg="#DCDCDC")
greeting_label.pack(fill=X)
img = resize_image("chatbot.png", new_width=140, new_height=90)
fimg = Label(label_frame, image=img,bg='#2F4F4F')
fimg.place(x=470,y=0)

history_frame = Frame(window)
history_frame.pack(expand=True, fill=BOTH)
chat_history = Text(history_frame, wrap="word",bg='#2F4F4F',fg="#F7F7F7",font=("roboto",14,"bold"))
chat_history.pack(expand=True, fill=BOTH)
chat_history.config(state=DISABLED)
entry = Entry(window,bg="white",fg="black",font=("roboto",14,"bold"))
entry.pack(side=LEFT, expand=True, fill=X,anchor=SW)
entry.bind("<Return>", send)
submit_button = Button(window, text="Send", command=send)
submit_button.pack(side=RIGHT)
window.mainloop()