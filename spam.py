def spam_finder(spam_keywords, messages):
    for message in messages:
        found = False
        for keyword in spam_keywords:
            if keyword.lower() in message.lower():
                print(f"Spam keyword '{keyword}' found in message: \"{message}\"\n")
                found = True
                break  
        if not found:
            print(f"No spam found in message: \"{message}\"\n")


spam_keywords = ["win", "free", "offer", "prize", "click here", "limited time", "urgent", "money guaranteed", "claim"]
messages = ["You have win a free Iphone!","Hi how are you?","Limited time offer, buy now!","Can we schedule our meeting?"]

spam_finder(spam_keywords, messages)
