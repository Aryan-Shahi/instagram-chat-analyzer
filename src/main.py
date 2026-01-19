import json
import string
import os

# file_path = "../data/message_1.json"
# with open(file_path, "r", encoding="utf-8") as file:
#     data = json.load(file)
 
 
CHAT_FOLDER = "../data/inbox/chat_folder_sahil"
all_messages = []   

for filename in os.listdir(CHAT_FOLDER):
    if filename.startswith("message_") and filename.endswith(".json"):
        file_path = os.path.join(CHAT_FOLDER, filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            all_messages.extend(data.get("messages",[]))
        
all_messages.sort(key=lambda x: x.get("timestamp_ms", 0))

messages = all_messages
print("Total messages loaded: ", len(messages))
#print(data.keys()) # to understand metadata 

# participants = data["participants"]
# for person in participants:
#     print(person["name"])
    
    
    
    

# first_message = messages[0]
# print(first_message)

# for message in messages[:5]:
#     sender = message.get("sender_name", "Unknown") # unknown is default value
#     text = message.get("content", None) #get method is safe, returns none if key doesnt exist unlike messages["sender_name"] which crashes if key doesnt exist
    
#     if text: #takes only non empty string. proceed only if text has actual content
#         print(f"{sender}->{text}")
        
        
        
## Message count per person

message_count = {}  # Empty dictionary 
for message in messages:
    sender = message.get("sender_name", "Unknown")
    
    if sender == "Meta AI":
        continue
    
    #initialize if not exists
    if sender not in message_count:
        message_count[sender] = 0 #message key dictionary ma vako "sender"(key) ko value = 0 {"alice": 0}
    
    message_count[sender] += 1

print("\nMessage count per person:")   
for sender, count in message_count.items():         ## Less readable version: for sender in message_count: count = message_count[sender]# 
    print(sender, "->", count)
    
# .item() le paisa ma change garxa message_count = {"Alice": 1500, "Bob": 800} changes to message_count.items() → [("Alice", 1500), ("Bob", 800)]/
# each pait is a tuble with (key, value)


text_message_count = {}
reaction_count = {}

for message in messages:
    sender = message.get("sender_name","Unknown")
    text = message.get("content", "")
    
    if sender == "Meta AI":
        continue
    
    if not text:
        continue
    
    if sender not in text_message_count:
        text_message_count[sender] = 0
        
    if sender not in reaction_count:
        reaction_count[sender] = 0
        
    if text.lower().startswith("reacted"):
        reaction_count[sender] +=1
    else:
        text_message_count[sender]+=1
        
print("\nText-only message count:")
for sender, count in text_message_count.items():
    print(sender, "->", count)
        
print("\nReaction count:")
for sender, count in reaction_count.items():
        print(sender, "->", count)
        
        
char_count = {}        
word_count = {}
text_count_for_avg = {}

        
for message in messages:
    sender = message.get("sender_name","Unknown")
    text = message.get("content", "")
    
    if sender == "Meta AI":
        continue
    
    if not text:
        continue
    
    if sender not in char_count:
        char_count[sender] = 0
        word_count[sender] = 0
        text_count_for_avg[sender] = 0
        
    char_count[sender] += len(text)
    
    words = text.split() #divides text by spaces into a list of words "Hello how are you?" → ["Hello", "how", "are", "you?"]
    word_count[sender] += len(words)
    
    text_count_for_avg[sender] += 1
        
print("\nText metrics per person:")
for sender in char_count:
    avg_length = char_count[sender]/text_count_for_avg[sender]
    print(f"{sender}-> Average length: {round(avg_length, 2)} chars, Total words:{word_count[sender]}")
    
    
    
# # most used word per person
# stopwords = {                           #words so common we cant say its the most used
#     "i", "you", "me", "my", "we", "us",
#     "the", "a", "an", "and", "or", "but",
#     "to", "of", "in", "on", "for", "with",
#     "is", "are", "was", "were", "am",
#     "it", "this", "that",
#     "u", "ur", 
#     #"im", "idk", "ok", "okay"
# }

# word_frequency = {}

# if sender not in word_frequency:
#     word_frequency[sender] = {}
    
# clean_text = text.lower()
# # remove punctuation
# clean_text = clean_text.translate(
#     str.maketrans("", "", string.punctuation)
#     )

# words = clean_text.split()

# for word in words:
#     if word in stopwords:
#         continue

    
#     if word not in word_frequency[sender]:
#         word_frequency[sender][word] = 0
        
#     word_frequency[sender][word]+= 1
    
    
# print("\nTop 10 most used words per person: ")
# for sender, words_dict in word_frequency.items():
#     print(f"\n{sender}:")
#     sorted_words = sorted(
#         words_dict.items(),
#         key=lambda x: x[1],
#         reverse=True
#     )
    
#     for word, count in sorted_words[:10]:
#         print(f"  {word}-> {count}")
        

import string

# stopwords = {
#     "i", "you", "me", "my", "we", "us",
#     "the", "a", "an", "and", "or", "but",
#     "to", "of", "in", "on", "for", "with",
#     "is", "are", "was", "were", "am",
#     "it", "this", "that",
#     "u", "ur"
# }


stopwords = {
    "i","you","me","my","we","us","the","a","an","and","or","but",
    "to","of","in","on","for","with","is","are","was","were","am",
    "it","this","that","your","u","ur",
    "ma","ta","xa","ho","ni","ko","la","na","k","hmm","haha"
}

word_frequency = {}
total_words_debug = 0

for message in messages:
    sender = message.get("sender_name")
    text = message.get("content")

    if not text or not sender:
        continue

    if sender not in word_frequency:
        word_frequency[sender] = {}

    clean_text = text.lower()
    clean_text = clean_text.translate(
        str.maketrans("", "", string.punctuation)
    )

    words = clean_text.split()

    for word in words:
        if word in stopwords:
            continue

        total_words_debug += 1

        if word not in word_frequency[sender]:
            word_frequency[sender][word] = 0

        word_frequency[sender][word] += 1

print("\nTop 10 most used words per person:")

for sender, words_dict in word_frequency.items():
    print(f"\n{sender}:")
    sorted_words = sorted(
        words_dict.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for word, count in sorted_words[:10]:
        print(f"  {word} -> {count}")

print("\nDEBUG total words processed:", total_words_debug)



# CLEAN CONVERSATIONAL WORD ANALYSIS


system_phrases = [
    "sent an attachment",
    "sent a reel",
    "reacted",
    "sent a message",
    "shared"
]



clean_word_frequency = {}

for message in messages:
    sender = message.get("sender_name")
    text = message.get("content")

    if not sender or not text:
        continue

    lower_text = text.lower()

    skip = False
    for phrase in system_phrases:
        if phrase in lower_text:
            skip = True
            break

    if skip:
        continue

    if sender not in clean_word_frequency:
        clean_word_frequency[sender] = {}

    clean_text = lower_text.translate(
        str.maketrans("", "", string.punctuation)
    )

    words = clean_text.split()

    for word in words:
        if not word.isalpha():
            continue
        if len(word) < 2:
            continue
        if word in stopwords:
            continue

        if word not in clean_word_frequency[sender]:
            clean_word_frequency[sender][word] = 0

        clean_word_frequency[sender][word] += 1

print("\nSTEP 42.2 — Clean top words per person:")

for sender, words_dict in clean_word_frequency.items():
    print(f"\n{sender}:")
    sorted_words = sorted(
        words_dict.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for word, count in sorted_words[:10]:
        print(f"  {word} -> {count}")


# ATTACHMENT, REEL & MEDIA ANALYSIS

media_stats = {}
for message in messages:
    sender = message.get("sender_name")
    text = message.get("content", "").lower()

    if not sender:
        continue
    
    if sender not in media_stats:
        media_stats[sender] = {
            "attachments": 0,
            "reels": 0,
            "photos": 0,
            "videos": 0,
            "audio": 0
        }
        
    if "sent an attachment" in text:
        media_stats[sender]["attachments"]+=1
        
    if "sent a reel" in text:
        media_stats[sender]["reels"] += 1

    if message.get("photos"):
        media_stats[sender]["photos"] += len(message["photos"])

    if message.get("videos"):
        media_stats[sender]["videos"] += len(message["videos"])

    if message.get("audio_files"):
        media_stats[sender]["audio"] += len(message["audio_files"])
        
print("\n Media behavior per person")
for sender, stats in media_stats.items():
    print(f"\n{sender}:")
    for k,v in stats.items():
        print(f"  {k} -> {v}")