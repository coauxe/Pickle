import pickle


favorite_color = {"lion":"yellow", "kitty": "red"}
pickle.dump(favorite_color, open("save.p","wb"))


fave_color = pickle.load(open("save.p","rb")) 
fave_color['new_key'] = 'new_value'

