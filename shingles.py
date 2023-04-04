def prepare_shingles_char(text, l):

    shingles = set([])
    for i in range(len(text)):
        shingles.add(text[i: i+l])

    return shingles

def prepare_shingles_word(text, l):

    text = text.split()
    shingles = set([])

    for i in range(len(text)):
        shitext = ""
        for j in text[i:i+l]:
            shitext+=j

        shingles.add(shitext)

    return shingles

def prep_text(text):

    cleantext = ""
    for c in text:
        if c.isalpha() or c == " ":
            cleantext+=c.lower()

    return cleantext    

def similarity(shingle1, shingle2):

    common = shingle1.intersection(shingle2)
    shingle1.update(shingle2)

    return len(common)/len(shingle1)*100


file1 = open("AI/13chil.txt", "r")
text1 = file1.read()
file2 = open("AI/3wishes.txt", "r")
text2 = file2.read()

text1 = prep_text(text1)
text1 = prep_text(text2)

shi1 = prepare_shingles_char(text1, 5)
shi2 = prepare_shingles_char(text2, 5)

print(f"{similarity(shi1, shi2)}%")