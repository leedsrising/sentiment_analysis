# importing the module 
import praw
import logging

# initialize with appropriate values 
from constants import client_id, client_secret, username, password, user_agent, post_title, post_body, post_body_no_self, relevant_subreddits

logging.basicConfig(filename='reddit_posts.log', level=logging.DEBUG, filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# creating an authorized reddit instance 
reddit = praw.Reddit(client_id = client_id,  
                     client_secret = client_secret,  
                     username = username,  
                     password = password, 
                     user_agent = user_agent)
reddit.validate_on_submit = True

def post_to_subreddit(subreddit, p_body, p_title):
        return reddit.subreddit(subreddit).submit(title=p_title, selftext=p_body)

# def gather_subreddits(query):
#         relevant_subreddits = []
#         for submission in reddit.subreddit("all").search(query):
#                 if (submission.subreddit.display_name in relevant_subreddits):
#                         continue
#                 else:
#                         relevant_subreddits.append(submission.subreddit.display_name)
#         return relevant_subreddits

def handle_posts(subreddits):
        for subreddit in relevant_subreddits:
                try:
                        post = post_to_subreddit(subreddit, post_body, post_title)
                        logging.info(post.url)
                except:
                        try:
                                post = post_to_subreddit(subreddit, post_body_no_self, post_title)
                                logging.info(post.url)
                        except:
                                continue
                        continue

# relevant_subreddits = gather_subreddits("photo")
handle_posts(relevant_subreddits)