import module_manager
module_manager.review()

import nltk
nltk.download()

text = 'My name is Keren Huang'
import regex
regex.split("[\s\.\,]", text)

nltk.word_tokenize(text)

# CREATE AN AI CHATBOT WITH NLTK
'''
1. create a button on splash screen "AI Chatbot" that leads to a different page
2. have an instructions page prior to the AI Chatbot usage
        Instructions page will describe bot functionality
        small bar at the top indicating that AI Chatbot is "online" and ready to respond
3. chatbot should send a greeting message and user should be able to send a message
4. chatbot should communicate with different APIs depending on its role
        CHAT BOT FUNCTIONALITY:
            nearby food charity locations (?) given a city, state
5. chatbot should have ability to say that it cannot find what the user is looking for
6. chatbot should be programmed to respond to certain gestures like "thanks"
7. chatbot should have a good bye message when user clicks back arrow (top left most likely)


Complexity: Is there a way to get the screen to scroll when queries get long?
'''