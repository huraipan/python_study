import pickle

data = {
    "목표1" : "매일 팔굽혀 펴기 100회",
    "목표2" : "매일 코딩 공부 1시간"
}

file = open("./myvenv/Chapter10/data.pickle", "wb")
pickle.dump(data, file)
file.close()

file = open("./myvenv/Chapter10/data.pickle", "rb")
data = pickle.load(file)
print(data)
file.close()