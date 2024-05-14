from chatterbot import ChatBot

# naming the ChatBot calculator
# using mathematical evaluation logic
# the calculator AI will not learn with the user input
Bot = ChatBot(name='Calculator',
              read_only=True,
              logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
              storage_adapter="chatterbot.storage.SQLStorageAdapter")


# clear the screen and start the calculator
print('\033c')
print("Hello, I am a calculator. How may I help you?")
while (True):
    # take the input from the user
    user_input = input("me: ")

    # check if the user has typed quit to exit the prgram
    if user_input.lower() == 'quit':
        print("Exiting")
        break

    # otherwise, evaluate the user input
    # print invalid input if the AI is unable to comprehend the input
    try:
        response = Bot.get_response(user_input)
        print("Calculator:", response)
    except:
        print("Calculator: Please enter valid input.")


url = "https://simple-chatgpt-api.p.rapidapi.com/ask"


headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "OUR API KEY",
    "X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
}


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.1)

    # Clear the console output
    sys.stdout.write('\r')
    sys.stdout.flush()


def ask(question):
    payload = {"question": question}
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get("answer")


if __name__ == "__main__":
    print(pyfiglet.figlet_format("AI Chat BOT"))
    print("Enter the question to ask:")
    print()
    while True:
        # print("/>>  ", end="")
        question = str(input(">>  "))
        if (question == 'q'):
            print(">>  Bye! Thanks for Using...")
            break
        # loading
        done = False
        # here is the animation
        t = threading.Thread(target=animate)
        t.start()
        answer = ask(question)
        time.sleep(5)
        done = True
        t.join()
        print(">> ", answer)
        print()        