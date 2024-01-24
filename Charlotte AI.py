from PIL import Image as PILImage, ImageTk
from time import strftime
from tkinter import *
import random
import pyttsx3
import json

user_name = input("System: Whats your name?: ")

password = input("System: password: ")
if password == "jarvis":
    while True:
        gender_ask = input("System: What's your gender? (male, female or non-binary): ")
        if gender_ask == "male":
            gender_input = "sir"
            break
        elif gender_ask == "female":
            gender_input = "ma'am"
            break
        elif gender_ask == "non-binary":
            gender_input = "fren"
            break
        else:
            print("System: That is not an option listed above")

else:
    print("System: Password incorrect!")
    exit()


char_window = Tk()
char_window.attributes("-fullscreen", True)
char_window.config(bg="black")


background_name_Hor = Label(char_window, text="C. H. A. R. L. O. T. T. E.", bg='black', fg="dark blue",
                            font=('Engravers MT', 80))
background_name_Hor.place(x=0, y=500)

background_lining = Label(char_window, text='=========================', bg='black', fg='dark blue',
                          font=("Arial", 100))
background_lining.place(x=0, y=140)


def update_rotation(image_label, angle_var, rotation_speed=1):
    angle_var[0] += rotation_speed
    rotated_image = char_image_pil.rotate(angle_var[0])
    rotated_image_tk = ImageTk.PhotoImage(rotated_image)
    image_label.configure(image=rotated_image_tk)
    image_label.image = rotated_image_tk  # Keep a reference to prevent garbage collection
    char_window.after(50, update_rotation, image_label, angle_var, rotation_speed)


char_image_pil = PILImage.open("C:/Users/Evert/Documents/J.A.R.V.I.S. Project/Data Files/16589-200.png")
char_image_tk = ImageTk.PhotoImage(char_image_pil)

# Create a label to display the image
image_label = Label(char_window, image=char_image_tk)
image_label.pack()

# Set up rotation variables
angle_var = [0]  # Using a list to make it mutable

# Start the rotation update loop
char_window.after(0, update_rotation, image_label, angle_var)


voice = pyttsx3.init()
voices = voice.getProperty('voices')

desired_voice_name = "Microsoft Hazel Desktop - English (Great Britain)"
for v in voices:
    if desired_voice_name.lower() in v.name.lower():
        voice.setProperty('voice', v.id)
        break

voice.setProperty("rate", 150)
voice.setProperty("volume", 1.0)


current_time = strftime("%H:%M:%S")
current_date = strftime("%A the %d of %B, %Y")


file_path = "C:/Users/Evert/Documents/J.A.R.V.I.S. Project/Data Files/Response Data.JSON"


def load_responses_from_file(file_path):
    with open(file_path) as file:
        responses_data = json.load(file)
    return responses_data


    # Corrected: Load responses_data from the file using the function
responses_data = load_responses_from_file(file_path)


def response_text(input_text):
    responses = responses_data.get("responses", {})
    how_responses = responses_data.get("how_responses", {})

    for key, value in responses.items():
        responses[key] = [response.format(user_name=user_name, current_time=current_time, current_date=current_date,
                                          gender_input=gender_input) for response in value]

        # Replace placeholders in how_responses
    for key, value in how_responses.items():
        how_responses[key] = [response.format(user_name=user_name, current_time=current_time, current_date=current_date,
                                              gender_input=gender_input) for response in value]

    if 'hello' in input_text.lower() or "hi" in input_text.lower() or "hey" in input_text.lower():
        return random.choice(responses['greeting'])
    elif 'can you do' in input_text.lower():
        return random.choice(responses['functionality'])
    elif 'what' and 'time' in input_text.lower():
        return random.choice(responses['time'])
    elif 'what' and 'date' in input_text.lower():
        return random.choice(responses['date'])
    elif 'you there' in input_text.lower():
        return random.choice(responses['sleep'])
    elif 'how are you' in input_text.lower():
        return random.choice(responses['how are you'])
    elif 'how' and "asleep" in input_text.lower():
        return random.choice(responses['sleepyhead'])
    elif 'what' and 'your name' in input_text.lower():
        return random.choice(responses['name'])
    elif "exit" in input_text.lower() or "quit" in input_text.lower():
        exit()
    elif 'how' and 'prevent' and 'boredom' in input_text.lower():
        return random.choice(how_responses['boredom'])
    elif 'how' and 'minecraft' and 'world' in input_text.lower():
        return random.choice(how_responses['mc world'])
    elif 'how' and 'build' and 'computer' in input_text.lower():
        return random.choice(how_responses['computer'])
    elif 'how' and 'build' and 'server' in input_text.lower():
        return random.choice(how_responses['server'])
    elif 'how' and 'build' and 'speaker' in input_text.lower():
        return random.choice(how_responses['speaker'])
    elif 'how do you work' in input_text.lower() or 'how do you function' in input_text.lower():
        return random.choice(how_responses['your func'])
#        elif 'look up' and 'a site' in input_text.lower():
#            print("Char: What site would you like to search?")
#            websearch_string = input("You: ")
#            import webbrowser
#            webbrowser.open("Https://www." + websearch_string)
    elif 'how' and 'much' and 'water' in input_text.lower():
        return random.choice(how_responses['water need'])
    elif 'how' and 'much' and 'feet' and 'in a meter' in input_text.lower():
        return random.choice(how_responses['ft to m'])
    elif 'how' and 'many' and 'inch' and 'in a foot' in input_text.lower():
        return random.choice(how_responses['inch to ft'])
    elif 'how' and 'much' and 'cm' and 'in a foot' in input_text.lower():
        return random.choice(how_responses['cm to ft'])
    elif 'how' and 'much' and 'cm' and 'in an inch' in input_text.lower():
        return random.choice(how_responses['ft to m'])
    elif 'how' and 'many' and 'km' and 'in a mile' in input_text.lower():
        return random.choice(how_responses['ft to m'])

    else:
        return ("I'm not really sure how to respond to that. maybe try asking if differently or add the "
                "question to the database")


def use_user_input():

    user_input = text_input.get()
    response = response_text(user_input)

    # Maximum characters per line
    max_chars_per_line = 40

    # Split the response into words
    words = response.split()

    # Initialize variables
    current_line = ""
    formatted_lines = []

    # Iterate through words and create lines
    for word in words:
        if len(current_line) + len(word) + 1 <= max_chars_per_line:
            # Add the word to the current line
            current_line += " " + word if current_line else word
        else:
            # Start a new line with the current word
            formatted_lines.append(current_line)
            current_line = word

    # Add the last line
    formatted_lines.append(current_line)

    # Join the lines with newline characters
    formatted_response = "\n".join(formatted_lines)
    user_input_response = Label(char_window, text=user_name + ": " + user_input, fg="white", bg="black")
    user_input_response.pack()
    char_output_response = Label(char_window, text="Char: " + formatted_response, fg="white", bg="black")
    char_output_response.pack()
    char_window.update()
    voice.say(response)
    voice.runAndWait()
    text_input.delete(0, 'end')
    user_input_response.after(5, user_input_response.destroy())
    char_output_response.after(5, char_output_response.destroy())

    # Set focus on the entry widget
    text_input.focus()


text_input = Entry(char_window, width=40, font=("Helvetica", 16))
text_input.pack(pady=20)

submit_button = Button(char_window, command=use_user_input, text="Submit", bg='black', fg="dark blue",
                       font=("OCR A Extended", 16))
submit_button.pack()

char_window.bind("<Return>", use_user_input())

char_window.mainloop()
