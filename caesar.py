#imports the funtions to be able to make a GUI
from graphics import *

#imports function to allow user to browse for file to be encrypted/decrypted
from tkinter.filedialog import askopenfilename

#imports function to be able to use randrange() function
from random import randrange

#imports funtions to be able to do mathematical calculations
import math

#imports functions that allow the animation to be slowed down/sped up
from time import sleep

#parameterized function for the splash screen
def animate(gwin):

    #the message screen to introduce the program will be drawn on the outsides first
    text1 = Text(Point(0, 50), "Jay's Caesar")
    text2 = Text(Point(100, 50), "Cipher Encoder/Decoder")
    text3 = Text(Point(50, 20), "Click Anywhere to Begin")

    #draw text to window
    text1.draw(gwin)
    text2.draw(gwin)
    text3.draw(gwin)

    #use a for loop to move the text objects, i.e. "animating" the objects
    #range(9) sets up the text objects to the center of the screen
    for i in range(9):

        #.move() shifts the object by (x, y) - positive and negative imply movements in different directions
        text1.move(5, 0)
        text2.move(-5, 0)

        #sleep function allows the animation to be reasonably paced
        sleep(0.4)

        #text colors are selected randomly, and changed every time the loop runs
        text1.setFill(color_rgb(randrange(0, 255),randrange(0, 255), randrange(0, 255)))
        text2.setFill(color_rgb(randrange(0, 255),randrange(0, 255), randrange(0, 255)))
        text3.setFill(color_rgb(randrange(0, 255),randrange(0, 255), randrange(0, 255)))

    #check for mouseclick anywhere on the screen
    pt = gwin.getMouse()
    if (0 <= pt.getX() <= 100) and (0 <= pt.getY() <= 100):

        #undraw everything from the splash screen, essentially "initializing" the main program
        text1.undraw()
        text2.undraw()
        text3.undraw()

#draws a "button" using a Zelle Rectangle object.
#pt1 and pt2 are Zelle point objects that will be set when this functions
#label is the text that labels the button
def drawButton(gwin, pt1, pt2, label, color):
    #sets the shape, location, and color of the "button", and draws it to the window
    button1=Rectangle(pt1, pt2)
    button1.setFill(color)
    button1.draw(gwin)

    #Put label on button

    #mid vairables allow the label to be centered in the label
    midX = (pt1.getX() + pt2.getX())/2
    midY = (pt1.getY() + pt2.getY())/2

    #sets the color, location of the button label, and draws it to the window
    button1Label = Text(Point(midX, midY), label)
    button1Label.setFill("white")
    button1Label.draw(gwin)

#decode function decodes any string
#userString is either a string input directly from the window or from a text file
#key is the integer value that's inputted from the window
def decode(userString, key):

    #accumulator string that will hold the final message
    #gets incremented each time the for loop runs
    decoded = ""

    #alphabet variable so that there are no "magic" numbers
    alphabet = 26

    #loop that parses through each of the characters in the input userString
    for char in userString:

        #check if the character is an alphabet and...
        if char.isalpha():
            #convert it into its ASCII value and subtract the key
            #subtract because we are decoding -- moving back from the original encrypted message
            number = ord(char) - key

        #since we want to keep all characters that are not in the alphabet the same...
        else:
            #we directly add them to the accumulator variable without performing the decryption on them
            decoded += char

        #don't use elif or else statements from here on because we want this to happen even after the else function above

        #check if the character is lower case and...
        if char.islower():
            #check whether its ASCII value is less than the ASCII value for a lowercase "a"
            while number < 97:
                #adds 26 so that all the characters "wrap around" to still be alphabets
                number += alphabet
            #converts the new ASCII value back into a character and adds it to the accumulator string
            decoded += chr(number)

        #check if the character is upper case and...
        if char.isupper():
            #check whether its ASCII value is less than the ASCII value for an uppercase "A"
            while number < 65:
                #adds 26 so that all the characters "wrap around" to still be alphabets
                number += alphabet
            #converts the new ASCII value back into a character and adds it to the accumulator string
            decoded += chr(number)

    #return the decoded message with the user prompt to indicate what/where the message is
    return "Your decoded message is: " + decoded

#encode function decodes any string
#userString is either a string input directly from the window or from a text file
#key is the integer value that's inputted from the window       
def encode(userString, key):

    #accumulator string that will hold the final message
    #gets incremented each time the for loop runs
    encoded = ""

    #alphabet variable so that there are no "magic" numbers
    alphabet = 26

    #loop that parses through each of the characters in the input userString
    for char in userString:
        #check if the character is an alphabet and...
        if char.isalpha():
            #convert it into its ASCII value and subtract the key
            #subtract because we are decoding -- moving back from the original encrypted message
            number = ord(char) + key

        #since we want to keep all characters that are not in the alphabet the same...
        else:
            encoded += char

        #don't use elif or else statements from here on because we want this to happen even after the else function above

        #check if the character is lower case and...
        if char.islower():
            #check whether its ASCII value is greater than the ASCII value for a lowercase "z"
            while number > 122:
                #adds 26 so that all the characters "wrap around" to still be alphabets
                number -= alphabet
            #converts the new ASCII value back into a character and adds it to the accumulator string
            encoded += chr(number)

        #check if the character is upper case and...
        if char.isupper():
            #check whether its ASCII value is greater than the ASCII value for an uppercase "Z"
            while number > 90:
                #adds 26 so that all the characters "wrap around" to still be alphabets
                number -= alphabet
            #since we want to keep all characters that are not in the alphabet the same...    
            encoded += chr(number)

    #return the decoded message with the user prompt to indicate what/where the message is       
    return "Your encoded message is: " + encoded

#main function
def main():

    #graphical window for caesar cipher, set to the dimensions 1000x700
    win = GraphWin("Caesar Cipher", 1000, 700)

    #Set the coordinates in the window so that
    #the lower left corner is the point (0, 0)
    #and the upper right corner is the point (100, 100).
    #This way the values along the y-axis increase
    #going upward, like in math class.
    win.setCoords(0, 0, 100, 100)

    #set background to a beautiful "fall" themed color
    win.setBackground("cornsilk1")

    #call the animate function and initialize splash screen 
    animate(win)

    #create an entry box for the userString
    inputString = Entry(Point(50,85), 50)
    inputString.draw(win)

    #create an entry box for the Key
    inputKey = Entry(Point(50,75), 20)
    inputKey.draw(win)

    #create an entry box for the Key that is used for encryption/decryption of text files
    inputKeyUser = Entry(Point(50, 44), 10)
    inputKeyUser.draw(win)

    #draw a button with in the win graphical window, with the given points, the given labels, and the given color (3 parameters for the "drawButton" function)
    #encode button:
    drawButton(win, Point(20, 50), Point(50, 60), "Encode", "blue3")
    #decode button:
    drawButton(win, Point(50, 50), Point(80, 60), "Decode", "blue3")
    #encrypt a text file button:
    drawButton(win, Point(20, 30), Point(50, 40), "Text Encryption", "red3")
    #decrypt a text file button:
    drawButton(win, Point(50, 30), Point(80, 40), "Text Decryption", "red3")
    #exit button
    drawButton(win, Point(40, 10), Point(60, 0), "Exit", "black")

    #giving the user an introduction to the program, including the definition of a caesar cipher
    instructText1 = Text(Point(50, 97), "Welcome to this Caesar Cipher Encryption/Decryption Tool!")
    instructText2 = Text(Point(50, 95), "A Caesar cipher is a simple substitution cipher based on the idea of shifting each letter of the plaintext message a fixed number of positions in the alphabet.")
    instructText3 = Text(Point(50, 93), "Here, you can either enter plain text into the box below, or click on the File Encode/Decode Buttons to have a WHOLE text file translated!")
    instructText1.setFill("black")
    instructText2.setFill("black")
    instructText3.setFill("black")
    instructText1.draw(win)
    instructText2.draw(win)
    instructText3.draw(win)

    #instructing the user to enter a plaintext string to be either encoded or decoded
    promptText = Text(Point(50, 90), "Enter message to be encoded or decoded:")
    promptText.setFill("black")
    promptText.draw(win)

    #instructing the user to enter a key between the numbers 1-26 (inclusive) for the string to be shifted by
    promptKey = Text(Point(50, 80), "Enter Key (1-26):")
    promptKey.setFill("black")
    promptKey.draw(win)

    #instructing the user to enter a key between the numbers 1-26 (inclusive) for the string to be shifted by -- but specifically for the Text File selected by the user
    promptFile = Text(Point(50, 47), "Enter Key (1-26) and click either Text Function to choose which file you would like to be encrypted or decrypted:")
    promptFile.setFill("black")
    promptFile.draw(win)    

    #get a mouse click!
    pt = win.getMouse()
    #pull out the string from the input box, and use this string to be encoded/decoded
    userString = inputString.getText()

    #accumulator text function that "prints" out the encoded/decoded message, or tells the user whether their message has been saved to a new file
    text = Text(Point(50, 65), "")
    text.setFill("black")
    text.draw(win)

    #the while loops runs until the exit button is clicked
    while not((20 < pt.getX() < 80) and (10 < pt.getY() < 20)):

        #checks for mouse click and makes the encrypt button work
        if (20 <= pt.getX() <= 50) and (50 <= pt.getY() <= 60):
            #gets the user string from the input box
            userString = inputString.getText()
            #gets the key from the input box and instead of leaving it as a string, turns it into an integer so that it can be processed by encode function
            key = int(inputKey.getText())

            #while loop repromts the user if an invalid key is entered
            while not(1 < key < 26):
                promptKey.setText("Invalid Key. Please enter a number between 1 and 26 and click Encode again.")
                #allows another mouse click
                pt = win.getMouse()
                key = int(inputKey.getText())

            #sets the empty text to the encoded message and "prints" to the window by calling the function using the userString and the key
            text.setText(encode(userString, key))

        #checks for mouse click and makes the decrypt button work
        elif (50 <= pt.getX() <= 80) and (50 <= pt.getY() <= 60):
            #gets the user string from the input box
            userString = inputString.getText()
            #gets the key from the input box and instead of leaving it as a string, turns it into an integer so that it can be processed by decode function
            key = int(inputKey.getText())

            #while loop repromts the user if an invalid key is entered
            while not(1 < key < 26):
                promptKey.setText("Invalid Key. Please enter a number between 1 and 26 and click Decode again.")
                #allows another mouse click
                pt = win.getMouse()
                key = int(inputKey.getText())

            #sets the empty text to the decoded message and "prints" to the window by calling the function using the userString and the key
            text.setText(decode(userString, key))
        
        #checks for mouse click and makes the encrypt text button work
        elif (20 <= pt.getX() <= 50) and (30 <= pt.getY() <= 40):
            #allows user to browse for any text file to be encoded, not just one in the same folder, and they don't have to type in the name
            infile = askopenfilename()
            #open the file
            inputfile = open(infile, "r")
            #read the file in
            userString = inputfile.read()

            #gets the key from the input box and instead of leaving it as a string, turns it into an integer so that it can be processed by decode function
            key = int(inputKeyUser.getText())

            #while loop repromts the user if an invalid key is entered
            while not(1 < key < 26):
                promptFile.setText("Invalid Key. Please enter a number between 1 and 26 and click Encode again.")
                #allows another mouse click
                pt = win.getMouse()
                key = int(inputKeyUser.getText())

            #create a new file for the encrypted message to be written into
            encryptedfile = open("encryptedfile.txt", "w")
            #call the encode function to encode all the text from the input file
            encryptedText = encode(userString, key)
            #write the encoded text into the new file
            encryptedfile.write(encryptedText)

            #close both the files to save them
            inputfile.close()
            encryptedfile.close()

            #change the accumulator Text to notify the user that their file has been encrypted
            text.setText("Done! Open the file called 'encryptedfile.txt' to see your message.")

            
        #checks for mouse click and makes the decrypt text button work
        elif (50 <= pt.getX() <= 80) and (30 <= pt.getY() <= 40):
            #allows user to browse for any text file to be decoded, not just one in the same folder, and they don't have to type in the name
            infile = askopenfilename()
            #open the file
            inputfile = open(infile, "r")
            #read the file in
            userString = inputfile.read()
            
            #gets the key from the input box and instead of leaving it as a string, turns it into an integer so that it can be processed by decode function
            key = int(inputKeyUser.getText())

            #while loop repromts the user if an invalid key is entered
            while not(1 < key < 26):
                promptFile.setText("Invalid Key. Please enter a number between 1 and 26 and click Decode again.")
                #allows another mouse click
                pt = win.getMouse()
                key = int(inputKeyUser.getText())

            #create a new file for the decrypted message to be written into
            decryptedfile = open("decryptedfile.txt", "w")
            #call the encode function to encode all the text from the input file
            decryptedText = decode(userString, key)
            #write the encoded text into the new file
            decryptedfile.write(decryptedText)

            #close both the files to save them
            inputfile.close()
            decryptedfile.close()

            #change the accumulator Text to notify the user that their file has been decrypted
            text.setText("Done! Open the file called 'decryptedtext.txt' to see your message.")

        #exit button
        elif (40 <= pt.getX() <= 60) and (0 <= pt.getY() <= 10):
            win.close()

        #allow multiple clicks outside the buttons    
        pt = win.getMouse()
    win.close()

#call the main function  
main()
