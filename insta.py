import instaloader
import csv

class GetInstagramProfile():
    def __init__(self) -> None:
        self.L = instaloader.Instaloader()

    def get_post_info_csv(self,username):
        with open(username+'.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            posts = instaloader.Profile.from_username(self.L.context, username).get_posts()
            for post in posts:
              
                posturl = "https://www.instagram.com/p/"+post.shortcode
                print("post url: "+posturl)
               # writer.writerow(["post",post.mediaid, post.profile, post.caption, post.date, post.location, posturl,  post.typename, post.mediacount, post.caption_hashtags, post.caption_mentions, post.tagged_users, post.likes, post.comments,  post.title,  post.url ])
                #writer.writerow(["post",post.profile, post.caption, post.date,posturl])#post.typename,post.caption_hashtags, post.caption_mentions, post.tagged_users, post.likes, post.comments,  post.title,  posturl ])
                writer.writerow(["post",post.date, post.location, posturl,  post.typename, post.mediacount, post.caption_hashtags, post.caption_mentions, post.tagged_users, post.likes, post.comments])
               

if __name__=="__main__":
    cls = GetInstagramProfile()
    cls.get_post_info_csv("saarang_iitmadras")