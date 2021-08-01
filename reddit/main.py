from reddit_client import gather_subreddits, handle_posts

text_file= open("hello.txt", "w")

relevant_subreddits = gather_subreddits("photo")
handle_posts(relevant_subreddits)