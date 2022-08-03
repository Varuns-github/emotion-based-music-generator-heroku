import random

angry = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/angry_3_lookback.wav",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/angry_5_lookback.wav",
];

disgust = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/disgust_3_lookback.wav",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/disgust_5_lookback.wav",
];

fear = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/fear_3_lookback.wav",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/fear_5_lookback.wav",
];

happy = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/happy_3_lookback.wav",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/happy_5_lookback.wav",
]

neutral = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/neutral_3_lookback.wav",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/neutral_5_lookback.wav",
]

sad = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/sad_3_lookback.wav",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/sad_5_lookback.wav",
]

surprise = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/surprise_3_lookback.wav",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/PredictedMusic/surprise_5_lookback.wav",
]


def return_music_url(emotion):
    if emotion == "Angry":
        # return a random url from the list
        return angry
    elif emotion == "Disgust":
        return disgust
    elif emotion == "Fear":
        return fear
    elif emotion == "Happy":
        return happy
    elif emotion == "Neutral":
        return neutral
    elif emotion == "Sad":
        return sad
    elif emotion == "Surprise":
        return surprise
    else:
        return neutral