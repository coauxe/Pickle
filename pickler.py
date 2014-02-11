import pickle


favorite_color = {"lion":"yellow", "kitty": "red"}
pickle.dump(favorite_color, open("save.p","wb"))


fave_colour = pickle.load(open("save.p","rb")) 
