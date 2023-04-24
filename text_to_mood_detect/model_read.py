import pickle

with open('model_pickle', 'rb') as f:
    mp = pickle.load(f)

emotions_dict = {
    0: ('Sadness &#128577;'), 
    1: ('Joy &#128513;'), 
    2: ('Love &#128525;'), 
    3: ('Anger &#128545;'), 
    4: ('Fear &#128561;')
}



def Give_emotion(String):

    num_emo = ((mp.predict([String]))[0])
    emotion = String + "<br> <h1> Emotion = " + emotions_dict[num_emo]

    return emotion

if '__main__' == __name__:
    print(Give_emotion("Hello be in love"))