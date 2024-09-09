"""
CREATE TABLE eurovision_winners (
    ID INTEGER PRIMARY KEY UNIQUE,
    year INTEGER PRIMARY KEY,
    country TEXT NOT NULL,
    winner TEXT NOT NULL,
    host_country TEXT NOT NULL,
    song_name TEXT NOT NULL
);
--------------------------------------------------------------------------------
INSERT INTO eurovision_winners (year, country, winner, host_country, song_name)

1	1956	Switzerland	Lys Assia	Switzerland	Refrain
2	1957	Netherlands	Corry Brokken	Germany	Net als toen
3	1958	France	Andre Claveau	Netherlands	Dors mon amour
4	1959	Netherlands	Teddy Scholten	France	Een beetje
5	1960	France	Jacqueline Boyer	United Kingdom	Tom Pillibi
6	1961	Luxembourg	Jean-Claude Pascal	France	Nous les amoureux
7	1962	France	Isabelle Aubret	Luxembourg	Un premier amour
8	1963	Denmark	Grethe and Jorgen Ingmann	United Kingdom	Dansevise
9	1964	Italy	Gigliola Cinquetti	Denmark	Non ho leta
10	1965	Luxembourg	France Gall	Italy	Poupee de cire poupee de son
11	1966	Austria	Udo Jurgens	Luxembourg	Merci Cherie
12	1967	United Kingdom	Sandie Shaw	Austria	Puppet on a String
13	1968	Spain	Massiel	United Kingdom	La la la
14	1969	Spain	Salome	Spain	Vivo cantando
15	1970	Ireland	Dana	Netherlands	All Kinds of Everything
16	1971	Monaco	Severine	Ireland	Un banc un arbre une rue
17	1972	Luxembourg	Vicky Leandros	United Kingdom	Apres toi
18	1973	Luxembourg	Anne-Marie David	Luxembourg	Tu te reconnaitras
19	1974	Sweden	ABBA	United Kingdom	Waterloo
20	1975	Netherlands	Teach-In	Sweden	Ding-a-dong
21	1976	United Kingdom	Brotherhood of Man	Netherlands	Save Your Kisses for Me
22	1977	France	Marie Myriam	United Kingdom	Loiseau et lenfant
23	1978	Israel	Izhar Cohen and the Alphabeta	France	A-Ba-Ni-Bi
24	1979	Israel	Milk and Honey	Israel	Hallelujah
25	1980	Ireland	Johnny Logan	Netherlands	Whats Another Year
26	1981	United Kingdom	Bucks Fizz	Ireland	Making Your Mind Up
27	1982	Germany	Nicole	United Kingdom	Ein bisschen Frieden
28	1983	Luxembourg	Corinne Hermes	Germany	Si la vie est cadeau
29	1984	Sweden	Herreys	Luxembourg	Diggi-Loo Diggi-Ley
30	1985	Norway	Bobbysocks	Sweden	La det swinge
31	1986	Belgium	Sandra Kim	Norway	Jaime la vie
32	1987	Ireland	Johnny Logan	Belgium	Hold Me Now
33	1988	Switzerland	Celine Dion	Ireland	Ne partez pas sans moi
34	1989	Yugoslavia	Riva	Switzerland	Rock Me
35	1990	Italy	Toto Cutugno	Yugoslavia	Insieme 1992
36	1991	Sweden	Carola	Italy	Fangad av en stormvind
37	1992	Ireland	Linda Martin	Sweden	Why Me
38	1993	Ireland	Niamh Kavanagh	Ireland	In Your Eyes
39	1994	Ireland	Paul Harrington and Charlie McGettigan	Ireland	Rock n Roll Kids
40	1995	Norway	Secret Garden	Ireland	Nocturne
41	1996	Ireland	Eimear Quinn	Norway	The Voice
42	1997	United Kingdom	Katrina and the Waves	Ireland	Love Shine a Light
43	1998	Israel	Dana International	United Kingdom	Diva
44	1999	Sweden	Charlotte Nilsson	Israel	Take Me to Your Heaven
45	2000	Denmark	Olsen Brothers	Sweden	Fly on the Wings of Love
46	2001	Estonia	Tanel Padar Dave Benton and 2XL	Denmark	Everybody
47	2002	Latvia	Marie N	Estonia	I Wanna
48	2003	Turkey	Sertab Erener	Latvia	Everyway That I Can
49	2004	Ukraine	Ruslana	Turkey	Wild Dances
50	2005	Greece	Helena Paparizou	Ukraine	My Number One
51	2006	Finland	Lordi	Greece	Hard Rock Hallelujah
52	2007	Serbia	Marija Serifovic	Finland	Molitva
53	2008	Russia	Dima Bilan	Serbia	Believe
54	2009	Norway	Alexander Rybak	Russia	Fairytale
55	2010	Germany	Lena	Norway	Satellite
56	2011	Azerbaijan	Ell and Nikki	Germany	Running Scared
57	2012	Sweden	Loreen	Azerbaijan	Euphoria
58	2013	Denmark	Emmelie de Forest	Sweden	Only Teardrops
59	2014	Austria	Conchita Wurst	Denmark	Rise Like a Phoenix
60	2015	Sweden	Mans Zelmerlow	Austria	Heroes
61	2016	Ukraine	Jamala	Sweden	1944
62	2017	Portugal	Salvador Sobral	Ukraine	Amar pelos dois
63	2018	Israel	Netta	Portugal	Toy
64	2019	Netherlands	Duncan Laurence	Israel	Arcade
65	2021	Italy	Maneskin	Netherlands	Zitti e buoni
66	2022	Ukraine	Kalush Orchestra	Italy	Stefania
67	2023	Sweden	Loreen	United Kingdom	Tattoo
68	2024	Switzerland	Nemo	Sweden	The Code
---------------------------------------------------------------------
CREATE TABLE song_details (
    year INTEGER PRIMARY KEY,
    song_length_seconds INTEGER NOT NULL,
    solo_performance BOOLEAN NOT NULL,
    genre TEXT NOT NULL,
    language TEXT NOT NULL
----------------------------------------------------------------------------
כמה פעמים זכתה ישראל באירוויזיון?
SELECT country, COUNT(*)
FROM eurovision_winners
WHERE country = 'Israel';
-- Israel = 4 --
-------------------------------------------------------------------------
כמה פעמים המדינה המארחת זכתה בתחרות האירוויזיון?

SELECT country, COUNT(*)
FROM eurovision_winners
WHERE country = 'Sweden';
-- Sweden = 7 --
-------------------------------------------------------------------------
באילו שנים זכתה ישראל?

SELECT year FROM eurovision_winners
WHERE country = 'Israel';

output:
year
-----
1978
1979
1998
2018
-------------------------------------------------------------
מה אורך השיר המנצח הקצר ביותר באירוויזיון?

SELECT MIN(song_length_seconds) AS shortest_song_length
FROM song_details;

output:
160
------------------------------------------------------------
SELECT *
FROM eurovision_winners
JOIN song_details
ON eurovision_winners.year = song_details.year;

output:
1	1956	Switzerland	Lys Assia	Switzerland	Refrain	1956	180	1	Chanson	French
2	1957	Netherlands	Corry Brokken	Germany	Net als toen	1957	180	1	Chanson	Dutch
3	1958	France	Andre Claveau	Netherlands	Dors mon amour	1958	195	1	Chanson	French
4	1959	Netherlands	Teddy Scholten	France	Een beetje	1959	165	1	Schlager	Dutch
5	1960	France	Jacqueline Boyer	United Kingdom	Tom Pillibi	1960	190	1	Chanson	French
6	1961	Luxembourg	Jean-Claude Pascal	France	Nous les amoureux	1961	195	1	Chanson	French
7	1962	France	Isabelle Aubret	Luxembourg	Un premier amour	1962	210	1	Chanson	French
8	1963	Denmark	Grethe and Jorgen Ingmann	United Kingdom	Dansevise	1963	190	0	Pop	Danish
9	1964	Italy	Gigliola Cinquetti	Denmark	Non ho leta	1964	175	1	Pop	Italian
10	1965	Luxembourg	France Gall	Italy	Poupee de cire poupee de son	1965	175	1	Pop	French
11	1966	Austria	Udo Jurgens	Luxembourg	Merci Cherie	1966	200	1	Chanson	German
12	1967	United Kingdom	Sandie Shaw	Austria	Puppet on a String	1967	160	1	Pop	English
13	1968	Spain	Massiel	United Kingdom	La la la	1968	185	1	Pop	Spanish
14	1969	Spain	Salome	Spain	Vivo cantando	1969	180	0	Pop	Spanish
15	1970	Ireland	Dana	Netherlands	All Kinds of Everything	1970	190	1	Pop	English
16	1971	Monaco	Severine	Ireland	Un banc un arbre une rue	1971	180	1	Chanson	French
17	1972	Luxembourg	Vicky Leandros	United Kingdom	Apres toi	1972	185	1	Pop	French
18	1973	Luxembourg	Anne-Marie David	Luxembourg	Tu te reconnaitras	1973	190	1	Pop	French
19	1974	Sweden	ABBA	United Kingdom	Waterloo	1974	170	0	Pop	English
20	1975	Netherlands	Teach-In	Sweden	Ding-a-dong	1975	170	0	Pop	English
21	1976	United Kingdom	Brotherhood of Man	Netherlands	Save Your Kisses for Me	1976	165	0	Pop	English
22	1977	France	Marie Myriam	United Kingdom	Loiseau et lenfant	1977	170	1	Pop	French
23	1978	Israel	Izhar Cohen and the Alphabeta	France	A-Ba-Ni-Bi	1978	185	0	Pop	Hebrew
24	1979	Israel	Milk and Honey	Israel	Hallelujah	1979	180	0	Pop	Hebrew
25	1980	Ireland	Johnny Logan	Netherlands	Whats Another Year	1980	175	1	Pop	English
26	1981	United Kingdom	Bucks Fizz	Ireland	Making Your Mind Up	1981	165	0	Pop	English
27	1982	Germany	Nicole	United Kingdom	Ein bisschen Frieden	1982	165	1	Pop	German
28	1983	Luxembourg	Corinne Hermes	Germany	Si la vie est cadeau	1983	175	1	Pop	French
29	1984	Sweden	Herreys	Luxembourg	Diggi-Loo Diggi-Ley	1984	165	0	Pop	Swedish
30	1985	Norway	Bobbysocks	Sweden	La det swinge	1985	170	0	Pop	Norwegian
31	1986	Belgium	Sandra Kim	Norway	Jaime la vie	1986	175	1	Pop	French
32	1987	Ireland	Johnny Logan	Belgium	Hold Me Now	1987	180	1	Pop	English
33	1988	Switzerland	Celine Dion	Ireland	Ne partez pas sans moi	1988	185	1	Pop	French
34	1989	Yugoslavia	Riva	Switzerland	Rock Me	1989	185	0	Pop	Serbo-Croatian
35	1990	Italy	Toto Cutugno	Yugoslavia	Insieme 1992	1990	170	1	Pop	Italian
36	1991	Sweden	Carola	Italy	Fangad av en stormvind	1991	180	1	Pop	Swedish
37	1992	Ireland	Linda Martin	Sweden	Why Me	1992	180	1	Pop	English
38	1993	Ireland	Niamh Kavanagh	Ireland	In Your Eyes	1993	180	1	Pop	English
39	1994	Ireland	Paul Harrington and Charlie McGettigan	Ireland	Rock n Roll Kids	1994	195	0	Pop	English
40	1995	Norway	Secret Garden	Ireland	Nocturne	1995	180	0	Classical	English
41	1996	Ireland	Eimear Quinn	Norway	The Voice	1996	175	1	Pop	English
42	1997	United Kingdom	Katrina and the Waves	Ireland	Love Shine a Light	1997	175	0	Pop	English
43	1998	Israel	Dana International	United Kingdom	Diva	1998	175	1	Pop	English
44	1999	Sweden	Charlotte Nilsson	Israel	Take Me to Your Heaven	1999	180	1	Pop	English
45	2000	Denmark	Olsen Brothers	Sweden	Fly on the Wings of Love	2000	180	0	Pop	English
46	2001	Estonia	Tanel Padar Dave Benton and 2XL	Denmark	Everybody	2001	175	0	Pop	English
47	2002	Latvia	Marie N	Estonia	I Wanna	2002	185	1	Pop	English
48	2003	Turkey	Sertab Erener	Latvia	Everyway That I Can	2003	180	1	Pop	English
49	2004	Ukraine	Ruslana	Turkey	Wild Dances	2004	185	0	Pop	English
50	2005	Greece	Helena Paparizou	Ukraine	My Number One	2005	180	1	Pop	English
51	2006	Finland	Lordi	Greece	Hard Rock Hallelujah	2006	180	0	Hard Rock	English
52	2007	Serbia	Marija Serifovic	Finland	Molitva	2007	180	1	Pop	Serbian
53	2008	Russia	Dima Bilan	Serbia	Believe	2008	180	1	Pop	English
54	2009	Norway	Alexander Rybak	Russia	Fairytale	2009	180	1	Pop	English
55	2010	Germany	Lena	Norway	Satellite	2010	175	1	Pop	English
56	2011	Azerbaijan	Ell and Nikki	Germany	Running Scared	2011	185	0	Pop	English
57	2012	Sweden	Loreen	Azerbaijan	Euphoria	2012	175	1	Pop	English
58	2013	Denmark	Emmelie de Forest	Sweden	Only Teardrops	2013	175	1	Pop	English
59	2014	Austria	Conchita Wurst	Denmark	Rise Like a Phoenix	2014	185	1	Pop	English
60	2015	Sweden	Mans Zelmerlow	Austria	Heroes	2015	180	1	Pop	English
61	2016	Ukraine	Jamala	Sweden	1944	2016	180	1	Pop	English
62	2017	Portugal	Salvador Sobral	Ukraine	Amar pelos dois	2017	175	1	Ballad	Portuguese
63	2018	Israel	Netta	Portugal	Toy	2018	175	1	Pop	English
64	2019	Netherlands	Duncan Laurence	Israel	Arcade	2019	175	1	Pop	English
65	2021	Italy	Maneskin	Netherlands	Zitti e buoni	2021	175	0	Rock	English
66	2022	Ukraine	Kalush Orchestra	Italy	Stefania	2022	180	0	Folk-Rap	Ukrainian
67	2023	Sweden	Loreen	United Kingdom	Tattoo	2023	175	1	Pop	English
68	2024	Switzerland	Nemo	Sweden	The Code	2024	180	1	Pop	English
--------------------------------------------------------------------------------------------------------------
אילו שירים זכו באירוויזיון עם ביצוע סולו?

SELECT eurovision_winners.song_name, eurovision_winners.year, eurovision_winners.winner
FROM eurovision_winners
JOIN song_details
ON eurovision_winners.year = song_details.year
WHERE song_details.solo_performance = TRUE;

output:
Refrain	1956	Lys Assia
Net als toen	1957	Corry Brokken
Dors mon amour	1958	Andre Claveau
Een beetje	1959	Teddy Scholten
Tom Pillibi	1960	Jacqueline Boyer
Nous les amoureux	1961	Jean-Claude Pascal
Un premier amour	1962	Isabelle Aubret
Non ho leta	1964	Gigliola Cinquetti
Poupee de cire poupee de son	1965	France Gall
Merci Cherie	1966	Udo Jurgens
Puppet on a String	1967	Sandie Shaw
La la la	1968	Massiel
All Kinds of Everything	1970	Dana
Un banc un arbre une rue	1971	Severine
Apres toi	1972	Vicky Leandros
Tu te reconnaitras	1973	Anne-Marie David
Loiseau et lenfant	1977	Marie Myriam
Whats Another Year	1980	Johnny Logan
Ein bisschen Frieden	1982	Nicole
Si la vie est cadeau	1983	Corinne Hermes
Jaime la vie	1986	Sandra Kim
Hold Me Now	1987	Johnny Logan
Ne partez pas sans moi	1988	Celine Dion
Insieme 1992	1990	Toto Cutugno
Fangad av en stormvind	1991	Carola
Why Me	1992	Linda Martin
In Your Eyes	1993	Niamh Kavanagh
The Voice	1996	Eimear Quinn
Diva	1998	Dana International
Take Me to Your Heaven	1999	Charlotte Nilsson
I Wanna	2002	Marie N
Everyway That I Can	2003	Sertab Erener
My Number One	2005	Helena Paparizou
Molitva	2007	Marija Serifovic
Believe	2008	Dima Bilan
Fairytale	2009	Alexander Rybak
Satellite	2010	Lena
Euphoria	2012	Loreen
Only Teardrops	2013	Emmelie de Forest
Rise Like a Phoenix	2014	Conchita Wurst
Heroes	2015	Mans Zelmerlow
1944	2016	Jamala
Amar pelos dois	2017	Salvador Sobral
Toy	2018	Netta
Arcade	2019	Duncan Laurence
Tattoo	2023	Loreen
The Code	2024	Nemo
----------------------------------------------------------------------------------------
כמה שירים שניצחו היו בשפה האנגלית?

SELECT COUNT(*) AS english_songs
FROM eurovision_winners
JOIN song_details
ON eurovision_winners.year = song_details.year
WHERE song_details.language = 'English';

output: 37
-----------------------------------------------------------
מה אורך ממוצע של שירי הארוויזיון?

SELECT AVG(song_length_seconds) AS average_song_length
FROM song_details;

output: 179.264705882353
--------------------------------------------------------------
באיזה שנה זכה השיר Hallelujah בארוויזיון?

SELECT year
FROM eurovision_winners
WHERE song_name = 'Hallelujah';

output: 1979
------------------------------------------------------
באיזו שנה היה הזוכה הראשון שביצע הופעה שאינה סולו? רמז השתמש ב- MIN ,
solo_performance = False אם בדוק

SELECT MIN(eurovision_winners.year) AS first_non_solo_year
FROM eurovision_winners
JOIN song_details
ON eurovision_winners.year = song_details.year
WHERE song_details.solo_performance = FALSE;

output: 1963
--------------------------------------------------------
מה היה אורך השיר הארוך ביותר שזכה באירוויזיון? רמז - MAX
*בונוס: מה היה שמו של שיר זה?

SELECT eurovision_winners.song_name, song_details.song_length_seconds
FROM eurovision_winners
JOIN song_details
ON eurovision_winners.year = song_details.year
WHERE song_details.song_length_seconds = (
    SELECT MAX(song_length_seconds) FROM song_details
);

output: Un premier amour	210
-----------------------------------------------------------------------------
*בונוס: איזו מדינה זכתה הכי הרבה פעמים באירוויזיון?

SELECT country, COUNT(*) AS win_count
FROM eurovision_winners
GROUP BY country              פקודה זו משמשת כדי לקבץ את התוצאות לפי כל מדינה. לכל מדינה נספרות הזכיות שלה בנפרד.
ORDER BY win_count DESC     חלק זה של השאילתה מסדר את התוצאות לפי מספר הזכיות  בסדר יורד, כך שהמדינה עם מספר הזכיות הגדול ביותר תופיע ראשונה.
LIMIT 1;                פקודה זו מגבילה את השאילתה להחזיר רק את התוצאה הראשונה, כלומר את המדינה עם מספר הזכיות הגבוה ביותר.

output: Sweden	7
----------------------------------------------------------
*בונוס: מיין את המדינות הזוכות באירוויזיון בסדר יורד לפי מספר הזכיות.
רמז: צור קבוצות לפי מדינות, השתמש ב- (*)Count כדי לספור כמה פעמים מופיעה כל
מדינה. קרא לשדה זה wins( alias), ואז מיין בסדר יורד לפי wins

SELECT country, COUNT(*) AS wins
FROM eurovision_winners
GROUP BY country
ORDER BY wins DESC;

output:
Sweden	7
Ireland	7
Luxembourg	5
United Kingdom	4
Netherlands	4
Israel	4
France	4
Ukraine	3
Switzerland	3
Norway	3
Italy	3
Denmark	3
Spain	2
Germany	2
Austria	2
Yugoslavia	1
Turkey	1
Serbia	1
Russia	1
Portugal	1
Monaco	1
Latvia	1
Greece	1
Finland	1
Estonia	1
Belgium	1
Azerbaijan	1
------------------------------------------------------
הדפס את כל השירים שזכו והיו בשפה הצרפתית

SELECT eurovision_winners.song_name, eurovision_winners.year, eurovision_winners.winner    בוחרים את שם השיר, השנה והזמר (המנצח) מתוך טבלת המנצחים.
FROM eurovision_winners
JOIN song_details
ON eurovision_winners.year = song_details.year
WHERE song_details.language = 'French';

output:
Refrain	1956	Lys Assia
Dors mon amour	1958	Andre Claveau
Tom Pillibi	1960	Jacqueline Boyer
Nous les amoureux	1961	Jean-Claude Pascal
Un premier amour	1962	Isabelle Aubret
Poupee de cire poupee de son	1965	France Gall
Un banc un arbre une rue	1971	Severine
Apres toi	1972	Vicky Leandros
Tu te reconnaitras	1973	Anne-Marie David
Loiseau et lenfant	1977	Marie Myriam
Si la vie est cadeau	1983	Corinne Hermes
Jaime la vie	1986	Sandra Kim
Ne partez pas sans moi	1988	Celine Dion
------------------------------------------------------------------------------------

מתי ישראל זכתה פעם ראשונה? מתי פעם אחרונה?

SELECT MIN(year) AS first_win, MAX(year) AS last_win
FROM eurovision_winners
WHERE country = 'Israel';

output:
1978	2018
---------------------------------------------------------------------

הדפס את שם השיר, מדינה, שנה ואורך השיר ממויין לפי אורך השיר מהארוך לקצר

output:
Un premier amour	France	1962	210
Merci Cherie	Austria	1966	200
Dors mon amour	France	1958	195
Nous les amoureux	Luxembourg	1961	195
Rock n Roll Kids	Ireland	1994	195
Tom Pillibi	France	1960	190
Dansevise	Denmark	1963	190
All Kinds of Everything	Ireland	1970	190
Tu te reconnaitras	Luxembourg	1973	190
La la la	Spain	1968	185
Apres toi	Luxembourg	1972	185
A-Ba-Ni-Bi	Israel	1978	185
Ne partez pas sans moi	Switzerland	1988	185
Rock Me	Yugoslavia	1989	185
I Wanna	Latvia	2002	185
Wild Dances	Ukraine	2004	185
Running Scared	Azerbaijan	2011	185
Rise Like a Phoenix	Austria	2014	185
Refrain	Switzerland	1956	180
Net als toen	Netherlands	1957	180
Vivo cantando	Spain	1969	180
Un banc un arbre une rue	Monaco	1971	180
Hallelujah	Israel	1979	180
Hold Me Now	Ireland	1987	180
Fangad av en stormvind	Sweden	1991	180
Why Me	Ireland	1992	180
In Your Eyes	Ireland	1993	180
Nocturne	Norway	1995	180
Take Me to Your Heaven	Sweden	1999	180
Fly on the Wings of Love	Denmark	2000	180
Everyway That I Can	Turkey	2003	180
My Number One	Greece	2005	180
Hard Rock Hallelujah	Finland	2006	180
Molitva	Serbia	2007	180
Believe	Russia	2008	180
Fairytale	Norway	2009	180
Heroes	Sweden	2015	180
1944	Ukraine	2016	180
Stefania	Ukraine	2022	180
The Code	Switzerland	2024	180
Non ho leta	Italy	1964	175
Poupee de cire poupee de son	Luxembourg	1965	175
Whats Another Year	Ireland	1980	175
Si la vie est cadeau	Luxembourg	1983	175
Jaime la vie	Belgium	1986	175
The Voice	Ireland	1996	175
Love Shine a Light	United Kingdom	1997	175
Diva	Israel	1998	175
Everybody	Estonia	2001	175
Satellite	Germany	2010	175
Euphoria	Sweden	2012	175
Only Teardrops	Denmark	2013	175
Amar pelos dois	Portugal	2017	175
Toy	Israel	2018	175
Arcade	Netherlands	2019	175
Zitti e buoni	Italy	2021	175
Tattoo	Sweden	2023	175
Waterloo	Sweden	1974	170
Ding-a-dong	Netherlands	1975	170
Loiseau et lenfant	France	1977	170
La det swinge	Norway	1985	170
Insieme 1992	Italy	1990	170
Een beetje	Netherlands	1959	165
Save Your Kisses for Me	United Kingdom	1976	165
Making Your Mind Up	United Kingdom	1981	165
Ein bisschen Frieden	Germany	1982	165
Diggi-Loo Diggi-Ley	Sweden	1984	165
Puppet on a String	United Kingdom	1967	160
------------------------------------------------------------------------

*בונוס: מצא את המדינות שבהם השיר המנצח היה יותר ארוך מהממוצע

SELECT eurovision_winners.country, eurovision_winners.song_name, song_details.song_length_seconds
FROM eurovision_winners
JOIN song_details
ON eurovision_winners.year = song_details.year
WHERE song_details.song_length_seconds > (
    SELECT AVG(song_length_seconds) FROM song_details
);

output:
Switzerland	Refrain	180
Netherlands	Net als toen	180
France	Dors mon amour	195
France	Tom Pillibi	190
Luxembourg	Nous les amoureux	195
France	Un premier amour	210
Denmark	Dansevise	190
Austria	Merci Cherie	200
Spain	La la la	185
Spain	Vivo cantando	180
Ireland	All Kinds of Everything	190
Monaco	Un banc un arbre une rue	180
Luxembourg	Apres toi	185
Luxembourg	Tu te reconnaitras	190
Israel	A-Ba-Ni-Bi	185
Israel	Hallelujah	180
Ireland	Hold Me Now	180
Switzerland	Ne partez pas sans moi	185
Yugoslavia	Rock Me	185
Sweden	Fangad av en stormvind	180
Ireland	Why Me	180
Ireland	In Your Eyes	180
Ireland	Rock n Roll Kids	195
Norway	Nocturne	180
Sweden	Take Me to Your Heaven	180
Denmark	Fly on the Wings of Love	180
Latvia	I Wanna	185
Turkey	Everyway That I Can	180
Ukraine	Wild Dances	185
Greece	My Number One	180
Finland	Hard Rock Hallelujah	180
Serbia	Molitva	180
Russia	Believe	180
Norway	Fairytale	180
Azerbaijan	Running Scared	185
Austria	Rise Like a Phoenix	185
Sweden	Heroes	180
Ukraine	1944	180
Ukraine	Stefania	180
Switzerland	The Code	180
----------------------------------------------------------------------------------------

.18 מה השיר עם הביצוע הכי קצר שהיה סולו? רמז: JOIN ומיון לפי אורך שיר בסדר עושה ואז
השתמש ב - 1 LIMIT

SELECT eurovision_winners.song_name, eurovision_winners.year, eurovision_winners.winner, song_details.song_length_seconds
FROM eurovision_winners
JOIN song_details
ON eurovision_winners.year = song_details.year
WHERE song_details.solo_performance = TRUE
ORDER BY song_details.song_length_seconds ASC
LIMIT 1;

output:
Puppet on a String	1967	Sandie Shaw	160
-----------------------------------------------------------------------------------------------------

הדפס כל מדינה , ואת ממוצע אורך השירים שלה.

SELECT eurovision_winners.country, AVG(song_details.song_length_seconds) AS avg_song_length
FROM eurovision_winners
JOIN song_details
ON eurovision_winners.year = song_details.year
GROUP BY eurovision_winners.country;

output:
Austria	192.5
Azerbaijan	185.0
Belgium	175.0
Denmark	181.666666666667
Estonia	175.0
Finland	180.0
France	191.25
Germany	170.0
Greece	180.0
Ireland	182.142857142857
Israel	178.75
Italy	173.333333333333
Latvia	185.0
Luxembourg	184.0
Monaco	180.0
Netherlands	172.5
Norway	176.666666666667
Portugal	175.0
Russia	180.0
Serbia	180.0
Spain	182.5
Sweden	175.0
Switzerland	181.666666666667
Turkey	180.0
Ukraine	181.666666666667
United Kingdom	166.25
Yugoslavia	185.0
-----------------------------------------------------------------------

כמה שירים שניצחו לא היו בשפה האנגלית?

SELECT COUNT(*) AS non_english_wins
FROM eurovision_winners
JOIN song_details
ON eurovision_winners.year = song_details.year
WHERE song_details.language != 'English';

output:
31
---------------------------------------------------------------------------

כמה סוגים שונים של genre הגיעו לארוויזיון?

SELECT COUNT(DISTINCT genre) AS unique_genres
FROM song_details;

output:
8
----------------------------------------------------------

*בונוס: מי הזמרת האחרונה מטעם ישראל שהופיעה בארוויזיון? רמז: מיין את השנים בסדר
יורד והשתמש ב- 1 LIMIT

SELECT winner, year, song_name
FROM eurovision_winners
WHERE country = 'Israel'
ORDER BY year DESC
LIMIT 1;

output:
Netta	2018	Toy
----------------------------------------------------------


"""