import pyttsx3
engine = pyttsx3.init()
engine.say("What is your name?")
engine.runAndWait()
name = input ()
engine.say ("Nice to meet you" + name)
engine.runAndWait()
myage = 1600000
engine.say ("How old are you?")
engine.runAndWait()
age = int(input())
age = myage - age
age = str(age)
engine.say("You're" + age + "years younger than me!")
engine.runAndWait()
