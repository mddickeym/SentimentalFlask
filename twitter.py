import tweepy
import vaderSentiment

class Twitter:

    CONSUMER_KEY = "u2w4FopTMw3xYSwjUSzSvhfe1"
    CONSUMER_SECRET = "wtFwfU9qIviOSjey8KY4gLWl37x6uyUJTdU3aKvGimi42jVJQt"
    ACCESS_TOKEN = "928463445481148416-0C1el66F4bTa8OJK2NO6QokHFUzkArJ"
    ACCESS_TOKEN_SECRET = "xaiZya5B5MesEL2zuecHUmCY2D1rHhMA0qSG2dN7XpC4U"


    auth = auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    analyzer = SentimentIntensityAnalyzer()

    query = 'tester'
    max_tweets = 100
    public_tweets = [status for status in tweepy.Cursor(
        api.search, q=query, lang="en").items(max_tweets)]

    data = [[obj.user.screen_name, obj.user.name, obj.user.id_str, obj.user.description, obj.created_at.year, obj.created_at.month, obj.created_at.day,
            "%s.%s" % (obj.created_at.hour, obj.created_at.minute), obj.id_str, obj.text, analyzer.polarity_scores(obj.text)["compound"]] for obj in public_tweets]
    df = pd.DataFrame(data, columns=['screen_name', 'name', 'twitter_id', 'description','year', 'month', 'date', 'time', 'tweet_id', 'tweet', 'compound_score'])

    # Create a list of positive tweets
    df_pos = df.sort_values(by="compound_score")
    # Create a list of negative tweets
    df_neg = df.sort_values(by="compound_score", ascending=False)

    df_summary_stats = df.describe()

    positive = 0
    neutral = 0
    negative = 0
    compound_scores = []

    for tweet in public_tweets:

        #print(tweet.text)
        # compound = analyzer.polarity_scores(tweet.text)["compound"]
        # compound_scores.append(compound)
        if(compound >= .05):
            positive += 1
        elif((compound > -0.05) and (compound < 0.05)):
            neutral += 1
        else:
            negative += 1
    # compound_average = round(numpy.mean(compound_scores), 5)
