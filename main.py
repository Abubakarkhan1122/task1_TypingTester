from time import *

#through RapidAPI to generate a random words
import http.client
conn = http.client.HTTPSConnection("random-words5.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "f2c4608ce6mshbd9d53e105cb95ep17eff6jsn41e2c5dce629",
    'X-RapidAPI-Host': "random-words5.p.rapidapi.com"
}

conn.request("GET", "/getRandom", headers=headers)

res = conn.getresponse()
data = res.read()


# print(data.decode("utf-8"))

#this fun finds the errors in the given strings
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1

    return error





#this fun helps to find the time duration
def speed_delay( test_s, test_e, userinput):
    time_delay = test_e - test_s
    time_rounded = round(time_delay,2)
    speed = len(userinput)/time_rounded
    return round(speed)
print("**** Typing Speed Tests ****")
print(data.decode())
time1 = time()
test_input = input("Enter the text to be typed: ")
time2 = time()
print("User Typed:",test_input)
print("No. of letters", len(test_input))

#for accuracy
one_word_accuracy = 100 / len(test_input)
accuracy = one_word_accuracy * len(test_input)
if data.decode() != test_input:
    accuracy = one_word_accuracy * len(test_input)
else:
    print()
print("Time taken by the user:",speed_delay (time1,time2,test_input), "sec")
print("Error:", mistake (data.decode(),test_input))
print("Accuracy:", accuracy)






if __name__ == '__main__':
    print("thankyou for using this program")







