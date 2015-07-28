from eulagizer import Eulagizer
import twitter
import random
import os


def run():
    # set up eulagizer
    gizer = Eulagizer('corpus')

    # initialize
    tweet = None

    # 20 attempts to generate real tweet
    for i in range(20):
        # make eula
        try:
            eula = gizer.run(length=500,
                             product='Eulagizer', company='Central Headquarters',
                             website='github.com/aschn/eulagizer')
        except RuntimeError:
            continue

        # split into sentences
        sentences = [s.strip()+'.' for s in eula.split('.')]

        # select sentences between 20 and 139 characters
        choices = filter(lambda s: len(s) > 20 and len(s) < 140, sentences)

        # if choices exist, choose one
        if choices:
            tweet = random.choice(choices)
            break

    # send tweet
    if tweet:
        api = twitter.Api(consumer_key=os.environ.get('TWITTER_CONSUMER_KEY'),
                          consumer_secret=os.environ.get('TWITTER_CONSUMER_SECRET'),
                          access_token_key=os.environ.get('TWITTER_ACCESS_KEY'),
                          access_token_secret=os.environ.get('TWITTER_ACCESS_SECRET'))
        api.PostUpdate(tweet)

    # return
    return tweet


if __name__ == '__main__':
    tweet = run()
    print tweet
