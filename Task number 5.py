text = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,totam rem aperiam, eaque ipsa quae ab illo inventore veritatis Et et et et et quasi architecto beatae vitae dictasunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quiaconsequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est,qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius moditempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minimaveniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex eacommodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quamnihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"



sentence_stop_symbol = (".", "?", "!")
sentence_count = 0
for symbol in sentence_stop_symbol:
    sentence_count += text.count(symbol)

print("Sentences count:", sentence_count)


word = ""
words = []
delimiters = (".", ".", "!", " ", "?")
for symbol in text:
    if symbol in delimiters:
            if len(word) > 0:    
                words.append(word.lower())
                word = ""
    else:
        word += symbol

word_match = words.count("et")
print(word_match) 


letterCount = len(text)
print("Symbol couunt: ", letterCount)

symbolCountWithoutSpaces = 0
for symbol in text: 
    if symbol != " ":
        symbolCountWithoutSpaces += 1

print("Symbol without spaces;", symbolCountWithoutSpaces)


pos = 120
if text[pos + 1] not in delimiters:
    pos = text[:pos + 1].rfind(" ")

if text[pos] in delimiters:
    pos -= 1

print(f"{text[:pos]}... ")