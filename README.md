I decided that I wanted to calculate odds of n-game streaks in the last year or so of Hikaru's games based off the actual win probabilities of each game derived from the player's ELO ratings. There are caveats:

1. The calculations use the ELO ratings of each player after the game, not before. This is what chess.com provides.

1. The calculations use chess.com ratings, not FIDE ratings.

1. I believe that I am calculating non-losing streaks (wins and draws combined), not pure winning streaks, because draws are "baked in" to the ELO win calculations. This means I am getting higher probabilities for streaks than calculations that exclude draws.

1. I did not separate out games by time control. All formats (blitz, rapid, etc.) are included.

1. I am only looking at rated games.

1. These probabilities are for streaks of exactly n games, not streaks of at least n games.

1. There may well be bugs in the code. I would appreciate review and commentary. The code I used is available on Github at https://github.com/guylsmith1972/hikaru_stats/blob/main/main.py


Here are my results. Due to numeric precision constraints, the probabilities for streaks less than 40 games evaluate to 100%, even though they are actually slightly less than 100% (less than the floating-point epsilon value):

Probabilities for 1-38 are all 100% due to numerical precision errors

Probability of a 39-game streak: 100.0%

Probability of a 40-game streak: 99.99999999999999%

Probability of a 41-game streak: 99.99999999999928%

Probability of a 42-game streak: 99.99999999996488%

Probability of a 43-game streak: 99.99999999893004%

Probability of a 44-game streak: 99.99999997809248%

Probability of a 45-game streak: 99.99999968626473%

Probability of a 46-game streak: 99.99999668764818%

Probability of a 47-game streak: 99.99997361334377%

Probability of a 48-game streak: 99.99983630024607%

Probability of a 49-game streak: 99.9991802693562%

Probability of a 50-game streak: 99.99662114054905%

Probability of a 51-game streak: 99.98829406418189%

Probability of a 52-game streak: 99.96529239112567%

Probability of a 53-game streak: 99.90985918115953%

Probability of a 54-game streak: 99.79228292008034%

Probability of a 55-game streak: 99.56542847582311%

Probability of a 56-game streak: 99.17103144979706%

Probability of a 57-game streak: 98.53793402698217%

Probability of a 58-game streak: 97.59637567042425%

Probability of a 59-game streak: 96.27571586735239%

Probability of a 60-game streak: 94.52695591427747%

Probability of a 61-game streak: 92.30977668984328%

Probability of a 62-game streak: 89.61993678120528%

Probability of a 63-game streak: 86.4622775889019%

Probability of a 64-game streak: 82.89357105995325%

Probability of a 65-game streak: 78.97274708891595%

Probability of a 66-game streak: 74.82867960926055%

Probability of a 67-game streak: 70.51513637626866%

Probability of a 68-game streak: 66.14639332091166%

Probability of a 69-game streak: 61.79010954402293%

Probability of a 70-game streak: 57.462466092992194%

Probability of a 71-game streak: 53.261729749705964%

Probability of a 72-game streak: 49.21784069030702%

Probability of a 73-game streak: 45.363703941975345%

Probability of a 74-game streak: 41.7333414551324%

Probability of a 75-game streak: 38.29042756667418%

Probability of a 76-game streak: 35.013098749948334%

Probability of a 77-game streak: 31.93153771442797%

Probability of a 78-game streak: 29.014081151768124%

Probability of a 79-game streak: 26.30244003544594%

Probability of a 80-game streak: 23.81551422826693%

Probability of a 81-game streak: 21.516455107188857%

Probability of a 82-game streak: 19.403669972423444%

Probability of a 83-game streak: 17.48767628119544%

Probability of a 84-game streak: 15.758984528817809%

Probability of a 85-game streak: 14.184046741957657%

Probability of a 86-game streak: 12.748329505990796%

Probability of a 87-game streak: 11.440126961048346%

Probability of a 88-game streak: 10.250894431335855%

Probability of a 89-game streak: 9.176172061930842%

Probability of a 90-game streak: 8.196074235261385%

Probability of a 91-game streak: 7.30203144257292%

Probability of a 92-game streak: 6.492148640186102%

Probability of a 93-game streak: 5.759861446512316%

Probability of a 94-game streak: 5.101883668410068%

Probability of a 95-game streak: 4.5124465883224385%

Probability of a 96-game streak: 3.986874343622593%

Probability of a 97-game streak: 3.522423909236816%

Probability of a 98-game streak: 3.1110650713580323%

Probability of a 99-game streak: 2.749874575493483%

Probability of a 100-game streak: 2.4287389900410905%