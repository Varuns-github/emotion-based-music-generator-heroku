import random

from scipy import rand

angry = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/121.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/122.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/123.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/124.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/125.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/126.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/127.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/128.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/129.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/130.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/131.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/132.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/133.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/134.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/135.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/136.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/137.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/138.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/139.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/140.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/141.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/142.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/143.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/144.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/145.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/146.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/147.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/148.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/149.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Angry/150.mp3",
];

disgust = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/211.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/212.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/213.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/214.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/215.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/216.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/217.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/218.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/219.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/220.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/221.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/222.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/223.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/224.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/225.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/226.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/227.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/228.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/229.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/230.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/231.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/232.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/233.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/234.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/235.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/236.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/237.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/238.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/239.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Disgust/240.mp3",
];

fear = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/091.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/092.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/093.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/094.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/095.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/096.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/097.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/098.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/099.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/100.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/101.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/102.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/103.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/104.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/105.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/106.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/107.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/108.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/109.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/110.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/111.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/112.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/113.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/114.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/115.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/116.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/117.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/118.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/119.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Fear/120.mp3",
];

happy = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/001.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/002.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/003.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/004.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/005.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/006.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/007.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/008.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/009.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/010.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/011.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/012.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/013.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/014.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/015.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/016.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/017.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/018.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/019.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/020.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/021.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/022.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/023.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/024.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/025.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/026.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/027.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/028.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/029.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Happy/030.mp3",
]

neutral = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/061.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/062.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/063.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/064.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/065.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/066.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/067.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/068.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/069.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/070.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/071.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/072.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/073.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/074.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/075.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/076.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/077.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/078.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/079.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/080.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/081.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/082.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/083.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/084.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/085.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/086.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/087.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/088.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/089.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Neutral/090.mp3",
]

sad = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/031.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/032.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/033.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/034.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/035.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/036.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/037.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/038.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/039.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/040.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/041.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/042.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/043.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/044.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/045.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/046.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/047.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/048.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/049.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/050.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/051.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/052.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/053.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/054.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/055.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/056.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/057.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/058.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/059.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Sad/060.mp3",
]

surprise = [
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/151.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/152.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/153.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/154.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/155.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/156.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/157.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/158.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/159.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/160.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/161.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/162.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/163.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/164.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/165.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/166.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/167.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/168.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/169.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/170.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/171.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/172.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/173.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/174.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/175.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/176.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/177.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/178.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/179.mp3",
    "https://github.com/Varuns-github/emotion-based-music-generator/blob/main/MusicDataset/Surprise/180.mp3",
]


def return_music_url(emotion):
    if emotion == "Angry":
        # return a random url from the list
        return random.choice(angry)
    elif emotion == "Disgust":
        return random.choice(disgust)
    elif emotion == "Fear":
        return random.choice(fear)
    elif emotion == "Happy":
        return random.choice(happy)
    elif emotion == "Neutral":
        return random.choice(neutral)
    elif emotion == "Sad":
        return random.choice(sad)
    elif emotion == "Surprise":
        return random.choice(surprise)
    else:
        return random.choice(neutral)