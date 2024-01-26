# Credits
# Authored by Raghav Potdar - 1/18/24
    #1 https://www.youtube.com/watch?v=q5HiD5PNuck --> Laid the basis of AI implementation 
    #2 https://www.youtube.com/watch?v=fsjXq2XURTY --> Introduced the import of string & choice function
    # Jeremiah helped with the creation of main.

#IMPORTS + API Key
import random
import string
import openai
#openai.api_key = "ADD YOUR OWN API KEY HERE"

# Step 1
    # Asks how long the user wants the password to be. pswdLength = Password character length.
def passwordLength():
    while True:
        try:
            print ("Welcome to the password generator!")
            pswdLength = int(input("How many characters do you want your password to be? "))
            break
        except ValueError:
            print("Input a number!")
    
    return pswdLength

# May add function in the future. Would ask use if they would like a full upper or lowercase password.
def UpperOrLower():
    pass


# Step 2
    # Creates a password soley based off character length.
def createPassword(pswdLength):

    # Defines characters as letters + digits.
    chars = string.ascii_letters + string.digits

    # Password begins as an empty string.
    password = ""

    # The loop will run 'pswdLength' # of times. Each time, a character is randomly selected from "chars" --> choice function
    # of the random module, and the password is formed from there. Help from #2.
    for i in range(pswdLength):
        password += random.choice(chars)
    
    # Return jumbo mumbo password! With a password <= 8 characters, users are encouraged to create a new password.
    if pswdLength > 8:
        print("Good character choice! The longer a password is, the more possible permutations it has, making it harder and harder for cybercriminals to crack.\n" + password)
    if pswdLength <= 8:
        # Fun fact: In testing, my friend asked for a 8 characters password. Noting returned until I added "=" to the equation. Fun way to find a error.
        print("Here ya go! But are you sure you don't want a more complex password? The longer a password is, the more possible permutations it has, making it harder and harder for cybercriminals to crack.\n", password)


# Step 3
    # Asks if the user wants a new password, either by (1) using the same process, or through (2) AI from ChatGPT - Open AI.
def NewOrAI():
    response = input("Do you want a new password? ")
    if response.lower() in ["yes", "y" , "sure" , "ok" , "okie doke"]:
        response = input("Here we go again...\nDo you want to do this same process again, or utilize AI? ")
        if response.lower() in ["same process", "same" , "again"]:
            print("Ok!")
            TEST = True
            while True:
                # Same code seen in main
                pswdLength = passwordLength()
                createPassword(pswdLength)
                NewOrAI()
                pass

        # AI code - gaining new character length + special info variables
        if response.lower() in ["ai", "AI", "artifical intelligence", "chatgpt", "openai"]:
            AIPassLength = input("Cool! How many characters do you want your password to be? ")
            AIPassRequire = input("Do you want the password to include something? \nAn example being a uppercase letter(s), numerical value(s), phrase(s), etc. \nPlease detail: ")
            # My favorite part of the code.
            TEST = False

        
    if response == "no":
        print("Ok! Keep your data safe.")
        TEST = True
        #pass

    # AI CORE CODE - I can't fiddle with this. #1
    # Is a function in a function frowned upon? Or is this nested function fine?
    if TEST == False:
        def chat_with_gpt (prompt):
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response. choices[0].message.content.strip()

        # AI CODE - Could fiddle with this!
        if __name__ == "__main__":
        # According to Google, it "checks if the script is being run as the main program.""
                # Looking for a singular string.
                response = chat_with_gpt ("Please create a password with a character length of" + AIPassLength + ", and please incorpate this as well:" + AIPassRequire)
                print ("AI: ", response)

# Step 4
    # Main
    # Jeremiah helped me with making this!
def main():
    while True:
        pswdLength = passwordLength()
        createPassword(pswdLength)
        NewOrAI()
        break
main()

