import module_manager
module_manager.review()

# CITATION: https://blog.xrds.acm.org/2017/01/build-natural-language-processing-based-intelligent-assistant-using-python-easy/
import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

from nltk.corpus import stopwords
import regex
def index_sort(list_var):
        length = len(list_var)
        list_index = list(range(0, length))
        x  = list_var
        for i in range(length):
                for j in range(length):
                        if x[list_index[i]] > x[list_index[j]]:
                                temp = list_index[i]
                                list_index[i] = list_index[j]
                                list_index[j] = temp
        return list_index

def bot_response(user_input):
        user_input = user_input.lower() # Convert the users input to all lowercase letters
        sentence_list.append(user_input) # Append the users response to the list of sentence tokens
        bot_response='' # Create an empty response for the bot
        cm = CountVectorizer().fit_transform(sentence_list) # Create the count matrix
        similarity_scores = cosine_similarity(cm[-1], cm) # Get the similarity scores to the users input
        flatten = similarity_scores.flatten() # Reduce the dimensionality of the similarity scores
        index = index_sort(flatten) # Sort the index from 
        index = index[1:] # Get all of the similarity scores except the first (the query itself)
        response_flag=0 # Set a flag letting us know if the text contains a similarity score greater than 0.0
        # Loop the through the index list and get the 'n' number of sentences as the response
        j = 0
        for i in range(0, len(index)):
                if flatten[index[i]] > 0.0:
                        bot_response = bot_response+' '+sentence_list[index[i]]
                        response_flag = 1
                        j = j+1
                if j > 2:
                        break  
        # if no sentence contains a similarity score greater than 0.0 then print 'I apologize, I don't understand'
        if(response_flag==0):
                bot_response = bot_response+' '+"I apologize, I don't understand."
                sentence_list.remove(user_input) #Remove the users response from the sentence tokens
        
        return bot_response

userinput = input("Enter something: ")
bot_response(userinput)

textlist = []

text = "I ran into a wall."
regex.split("[\s\.\,]", text)

tokens = nltk.word_tokenize(text)
print(tokens)

stop_words = set(stopwords.words('english'))
clean_tokens = [w for w in tokens if not w in stop_words]
print(clean_tokens)

tagged = nltk.pos_tag(clean_tokens)
print(tagged)

print(nltk.ne_chunk(tagged)) 

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