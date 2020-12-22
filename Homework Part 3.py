text = "Etiam in porta mauris, ut lacinia dui. Suspendisse maximus ipsum purus, vitae cursus mauris blandit eu. Integer tempor non neque eget eleifend. Morbi id nulla nec lectus lobortis imperdiet eget mollis enim. Donec sed quam a mi maximus suscipit lacinia vel sapien. Vivamus dolor nisl, interdum eget porttitor in, malesuada ut mi. Nam ac fermentum velit, non gravida sem. Nullam ante leo, volutpat vel sapien nec, dignissim faucibus lacus. Proin sed ligula vitae est porttitor vulputate convallis sed mi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent viverra, ante eget ultricies venenatis nulla mauris euismod velit, vitae pretium neque massa at nunc. Nulla id dictum nunc. Integer efficitur dictum felis sed maximus. Cras ultrices erat vitae mauris rhoncus blandit. Morbi ultrices at elit vel dignissim. Etiam libero risus, mattis iaculis magna ac, egestas varius odio." 


inputLetter = ""

while True:
    try:
        inputLetter = input("Please, enter letter: ")
        inputLetter = inputLetter.lower()
        assert len(inputLetter) == 1
        break
    except:
        print("Please enter letter only one: ")

word = ""
words = []
delimiters = (" ", ".", ",", "?", "!")
for symbol in text:
    if symbol in delimiters:
        if len(word) > 0:
            words.append(word)
            word = ""
    else:
        word += symbol

first_letter_count = 0
for word in words:
    if word[0].lower() == inputLetter:
        first_letter_count += 1

word_Math_percentage = first_letter_count / len(words) * 100
print(f"Letters was found: {first_letter_count}")
print(f"Persentage is {word_Math_percentage}")

word_lenght = len(words[0])
for word  in words:
    tmp_lenght = len(word)
    if word_lenght > tmp_lenght:
        word_lenght = tmp_lenght

print("Min word lengh" , word_lenght)