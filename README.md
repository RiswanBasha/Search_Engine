# Article Search Engine - Riswan Basha Saleem Basha
## Overview
This Python application searches for recent news articles on a user-defined topic and outputs the top-15 relevant articles. It provides summaries and named entities from the article headlines and saves all search results to a CSV file.

## How to Run the Code

1. **Clone the Repository**
   ```bash
   https://github.com/RiswanBasha/Search_Engine.git
   cd [folder]
   ```
2. **Set Up a Virtual Environment**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   or
    ```
   conda create --name myenv python=3.8
   conda activate myenv
   ```
3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
4. **Environment Variables**
   set the NEWSAPI_KEY in your environmental variables which you can find here [newsapi](https://newsapi.org/docs).
   1. Go to the link,
   2. Register your account
   3. Get API Key for free
5. **Run the Application**

   ```
   python Article_Search.py
   or
   Jupyter Notebook
   ```
   Follow the Prompts
   - Enter a search topic.
   - Choose your preferred language (English or German).
   View Results
   - Check the console for the top-15 articles' summaries and named entities.
   - Find a detailed list of all fetched articles in news_articles.csv.
     
## Result
   Enter a topic to search for (or type 'exit' to quit):  **IPL**
   
   Which language do you prefer? English or German:  **en**
   
   Title: Sonam Delivers High Octane Style And Dance Moves In A Bejewelled Jumpsuit 
   URL: https://www.ndtv.com/lifestyle/sonam-bajwa-delivers-high-octane-style-and-dance-moves-in-a-bejewelled-fringe-jumpsuit-5379739 
   Date: 2024-04-05T08:14:11Z
   
   ---------------------------------------------------------------------------
   Title: SRH vs CSK Pitch Report: Key players, head-to-head statistics, weather update, and other details 
   URL: https://economictimes.indiatimes.com/news/sports/srh-vs-csk-ipl-2024-pitch-report-rajiv-gandhi-international-stadium-today-match-gujarat-titans-punjab-kings-dream-11-predictions-pat-cummins-ruturaj-gaikwad/articleshow/109059914.cms 
   Date: 2024-04-05T08:08:36Z
   
   ---------------------------------------------------------------------------
   Title: Virat Kohli under lot of pressure this IPL, other RCB batters need to support him: Steve Smith 
   URL: https://economictimes.indiatimes.com/news/sports/virat-kohli-under-lot-of-pressure-this-ipl-other-rcb-batters-need-to-support-him-steve-smith/articleshow/109058866.cms 
   Date: 2024-04-05T07:28:02Z
   
   ---------------------------------------------------------------------------
   Title: Broad backs struggling Buttler to discover form in IPL 
   URL: https://www.channelnewsasia.com/sport/broad-backs-struggling-buttler-discover-form-ipl-4244886 
   Date: 2024-04-05T07:09:37Z
   
   ---------------------------------------------------------------------------
   Title: SC directs collective hearing for online gaming GST cases 
   URL: https://www.livemint.com/industry/sc-directs-collective-hearing-for-online-gaming-gst-cases-11712299872017.html 
   Date: 2024-04-05T06:58:40Z
   
   ---------------------------------------------------------------------------
   Title: GT vs PBKS IPL 2024: From “accidental purchase” to ‘hero’, Shashank Singh turns match winner for Preity Zinta and Punjab 
   URL: https://economictimes.indiatimes.com/news/sports/gt-vs-pbks-ipl-2024-from-accidental-purchase-to-hero-shashank-singh-turns-match-winner-for-preity-zinta-and-punjab/articleshow/109054334.cms 
   Date: 2024-04-05T05:29:44Z
   
   ---------------------------------------------------------------------------
   Title: Travis Head Auditions For Cricket World Cup Spot At Indian Premier League 
   URL: https://www.forbes.com/sites/tristanlavalette/2024/04/05/travis-head-auditions-for-cricket-world-cup-spot-at-indian-premier-league/ 
   Date: 2024-04-05T04:36:51Z
   
   ---------------------------------------------------------------------------
   Title: RBI MPC Announcement: RBI keeps benchmark repo rate unchanged at 6.5%, says Governor Shaktikanta Das 
   URL: https://www.livemint.com/industry/banking/rbi-mpc-announcement-rbi-keeps-benchmark-repo-rate-unchanged-at-6-5-says-governor-shaktikanta-das-11712291099016.html 
   Date: 2024-04-05T04:35:00Z
   
   ---------------------------------------------------------------------------
   Title: PBKS stages sensational comeback to defeat GT in TATA IPL 2024 thriller 
   URL: https://english.khabarhub.com/2024/05/349454/ 
   Date: 2024-04-05T01:45:54Z
   
   ---------------------------------------------------------------------------
   Title: Markram's half-century helps Sunrisers past Super Kings - IPL scorecard 
   URL: https://www.bbc.co.uk/sport/cricket/scorecard/ECKE1220446 
   Date: 2024-04-05T00:00:00Z
   
   ---------------------------------------------------------------------------
   Title: Angkrish Raghuvanshi Thanks ‘Guru’ Abhishek Nayar After Stunning Fifty Against Delhi Capitals 
   URL: https://thehillstimes.in/sports/angkrish-raghuvanshi-thanks-guru-abhishek-nayar-after-stunning-fifty-against-delhi-capitals 
   Date: 2024-04-04T21:50:31Z
   
   ---------------------------------------------------------------------------
   Title: Mayank Yadav Can Be Fast-Tracked Into International Cricket, India Have Got Something Special: Stuart Broad 
   URL: https://thehillstimes.in/sports/mayank-yadav-can-be-fast-tracked-into-international-cricket-india-have-got-something-special-stuart-broad 
   Date: 2024-04-04T21:45:40Z
   
   ---------------------------------------------------------------------------
   Title: Mustafizur Rahman-Less CSK Face Unpredictable Sunrisers Hyderabad 
   URL: https://thehillstimes.in/sports/mustafizur-rahman-less-csk-face-unpredictable-sunrisers-hyderabad 
   Date: 2024-04-04T21:35:55Z
   
   ---------------------------------------------------------------------------
   Title: IPL Records Highest Ever TV Viewership In First 10 Matches, Says Official Broadcaster 
   URL: https://thehillstimes.in/sports/ipl-records-highest-ever-tv-viewership-in-first-10-matches-says-official-broadcaster 
   Date: 2024-04-04T21:30:37Z
   
   ---------------------------------------------------------------------------
   Title: Rishabh Pant Fined Rs 24 Lakh For Second Over Rate Offence 
   URL: https://thehillstimes.in/sports/rishabh-pant-fined-rs-24-lakh-for-second-over-rate-offence 
   Date: 2024-04-04T21:25:52Z
   
   ---------------------------------------------------------------------------
   
   Summary of headlines:
   
   - Sonam Delivers High Octane Style And Dance Moves In A Bejewelled Jumpsuit
   - SRH vs CSK Pitch Report: Key players, head-to-head statistics, weather update, and other details
   - Virat Kohli under lot of pressure this IPL, other RCB batters need to support him: Steve Smith
   - Broad backs struggling Buttler to discover form in IPL
   - SC directs collective hearing for online gaming GST cases
   - GT vs PBKS IPL 2024: From “accidental purchase” to ‘hero’, Shashank Singh turns match winner for Preity Zinta and Punjab
   - Travis Head Auditions For Cricket World Cup Spot At Indian Premier League
   - RBI MPC Announcement: RBI keeps benchmark repo rate unchanged at 6.5%, says Governor Shaktikanta Das
   - PBKS stages sensational comeback to defeat GT in TATA IPL 2024 thriller
   - Markram's half-century helps Sunrisers past Super Kings - IPL scorecard
   - Angkrish Raghuvanshi Thanks ‘Guru’ Abhishek Nayar After Stunning Fifty Against Delhi Capitals
   - Mayank Yadav Can Be Fast-Tracked Into International Cricket, India Have Got Something Special: Stuart Broad
   - Mustafizur Rahman-Less CSK Face Unpredictable Sunrisers Hyderabad
   - IPL Records Highest Ever TV Viewership In First 10 Matches, Says Official Broadcaster
   - Rishabh Pant Fined Rs 24 Lakh For Second Over Rate Offence
   
   Named Entities (sorted by frequency):
   
   [('IPL', 13), ('KKR', 13), ('2024', 11), ('Indian', 5), ('DC', 5), ('first', 4), ('10', 4), ('Gujarat', 4), ('Titans', 4), ('Punjab Kings', 4), ('Kolkata', 4), ('Virat Kohli', 3), ('RCB', 3), ('India', 3), ('35', 3), ('Delhi', 3), ('Delhi Capitals', 3), ('Shashank Singh', 2), ('Punjab', 2), ('Sunrisers', 2), ('USA', 2), ('Gill', 2), ('5th', 2), ('NCLAT', 2), ('Surrey', 2), ('Angkrish Raghuvanshi', 2), ('Rabada', 2), ('4th', 2), ('MS Dhoni', 2), ('Rohit Sharma', 2), ('Hardik Pandya', 2), ('Alliant Energy Co.', 2), ('NASDAQ', 2), ('LNT', 2), ('today', 2), ('Sanjay Singh', 2), ('second', 2), ('Narine', 2), ('272', 2), ('third', 2), ('Venus Concept', 2), ('Kolkata Knight Riders', 2), ('BJP', 2), ('Sonam Delivers', 1), ('CSK Pitch Report', 1), ('Steve Smith', 1), ('Buttler', 1), ('SC', 1), ('Travis Head Auditions', 1), ('World Cup Spot', 1), ('Indian Premier League', 1), ('RBI MPC Announcement', 1), ('RBI', 1), ('6.5%', 1), ('Shaktikanta Das', 1), ('TATA IPL 2024', 1), ('Markram', 1), ('half-century', 1), ('Super Kings - IPL', 1), ('Raghuvanshi Thanks ‘Guru', 1), ('Abhishek Nayar', 1), ('Stuart Broad', 1), ('Mustafizur Rahman-Less CSK Face Unpredictable Sunrisers Hyderabad', 1), ('IPL Records Highest Ever TV Viewership', 1), ('Broadcaster', 1), ('Rishabh Pant Fined Rs', 1), ('Williamson', 1), ('Ashutosh Sharma', 1), ('Updated Points Table', 1), ('3', 1), ('Stewart', 1), ('Aakash Chopra', 1), ("Shubman Gill's", 1), ('half', 1), ('Air India', 1), ('Tata', 1), ('Vistara', 1), ('Speedster Kagiso', 1), ('Wriddhiman Saha', 1), ('Delhi High Court', 1), ('244', 1), ('Ericsson', 1), ('seven', 1), ('28 per cent', 1), ('TAM', 1), ('GT', 1), ('PBKS Live Score Updates', 1), ('Sachin Tendulkar', 1), ('Sreesanth', 1), ('World Cup', 1), ('5', 1), ('Proteas', 1), ('Rob Walter', 1), ('Alia Bhatt', 1), ('Gucci', 1), ('Madrid', 1), ('Zodiac', 1), ('IPL Cricketers', 1), ('County Championship', 1), ('Rinku Singh', 1), ('Star Sports', 1), ('₹1', 1), ('Over 10,000', 1), ('Q1 2024', 1), ('Disney Star', 1), ('Blue Trust Inc.', 1), ('1,038', 1), ('Ajith Kumar', 1), ('Natarajan', 1), ('Doja Cat', 1), ('Nargis Fakhri', 1), ('David Dhawan', 1), ('The Defective Detectives', 1), ('three', 1), ('Shweta Gulati', 1), ('25', 1), ('fifty', 1), ('PBKS Pitch Report', 1), ('Ahmedabad', 1), ('Andre Russel', 1), ("Ishant Sharma's", 1), ('JSW Sports', 1), ('₹', 1), ('350', 1), ('Starc', 1), ('Virat', 1), ('AB de Villiers', 1), ('Kohli', 1), ('Andre Russell', 1), ('200', 1), ('Tihar', 1), ('Katchatheevu', 1), ('Malaysia Airlines', 1), ('Mayank Yadav', 1), ('106', 1), ('Kagiso', 1), ('Accuracy', 1), ('Lahiru Kumara Claims', 1), ('4', 1), ('Sri Lanka Wins', 1), ('Sunil Narine', 1), ('Rishabh Pant', 1), ('David Warner', 1), ('Rupali Ganguly', 1), ('Anupamaa', 1), ('Retinal GABAergic Alterations', 1), ('Suryakumar', 1), ('April 7', 1), ('11', 1), ('TGA', 1), ('AAP', 1), ('Atishi', 1), ('Bansuri Swaraj', 1), ('Upbeat Delhi Capitals', 1), ('KKR Live Score', 1), ('2nd', 1), ('Vizag', 1), ('Toss', 1), ('XI', 1), ('AdvisorNet Financial Inc Lowers Stake', 1), ('Ambati', 1), ('Rayudu', 1), ('KKR IPL Live Score 2024:', 1), ('Can Delhi Capitals', 1), ('Visakhapatnam', 1), ('Bengaluru', 1), ('Rs 86,000', 1), ('IPL Match', 1), ('CSK', 1), ('Friday', 1), ("Mumbai Indians'", 1), ("Hardik Pandya'", 1), ("Child of the wind' Yadav", 1)]
   Enter a topic to search for (or type 'exit' to quit):  exit

**Unit Testing**

![image](https://github.com/RiswanBasha/Search_Engine/assets/52401793/f4491e46-7747-4ed1-b1e2-964a1cd1359e)
