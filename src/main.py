import json

file_path = "../data/message_1.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
    
#print(data.keys()) # to understand metadata 

# participants = data["participants"]
# for person in participants:
#     print(person["name"])
    
    
    
    
messages = data["messages"]
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
    