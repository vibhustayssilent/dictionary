#create a dictionary and take input from user and return the meaning of the word from the dictionary




d1={"quantum mechanics":"the field of science that deals with nuclear particles like electrons and muons,and deals with probabilistic approaches of reality",
    
"meditation":"meditation is a practice in which an individual uses a technique to train attention and awareness and detach from reflexive, achieving a mentally clear and emotionally calm and stable state"
    ,"gooning":"is a sexual technique whereby an orgasm is controlled (that is, delayed or prevented"}


print("enter the word")
word = input()

if word == "quantum mechanics":
    print(d1["quantum mechanics"])

elif word == "meditation":
    print(d1["meditation"])

elif word == "gooning":
 print(d1["gooning"])

else:
    print("word not found,update the dictionary")






















