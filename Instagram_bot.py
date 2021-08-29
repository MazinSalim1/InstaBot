#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time, random
from instagram_private_api import Client, ClientCompatPatch


# In[18]:


def like_tags(tags,ppt):
    global posts
    posts= {}
    for i in range(len(tags)):
        print(f'Liking posts tagged: {tags[i]}')
        results = api.feed_tag(tag = tags[i],rank_token= Client.generate_uuid())
        c=0
        for i in range(len(results['items'])):
            if results['items'][i]['code'] not in list(posts.keys()):
                link=results['items'][i]['code']
                mid=results['items'][i]['id']
                uid=str(results['items'][i]['user']['pk'])
                name=results['items'][i]['user']['username']
                api.post_like(media_id = mid)
                print('Liked post---> https://www.instagram.com/p/'+link)
                posts[link]=[mid,uid,name]
                c+=1
                if c == ppt: break
                time.sleep(5)


# In[24]:


#len(posts)
#follow_liked(10)
#commenting(50)


# In[20]:


def follow_liked(percent):
    num= round(len(posts)*percent/100)
    tocom=random.sample(list(posts.keys()),num)
    print(f'Following {percent}% of account that you liked posts from...')
    for i in tocom:
        api.friendships_create(user_id= posts[i][1])
        print("Followed user---> "+posts[i][2])
        time.sleep(5)


# In[4]:


def commenting(percent):
    print("Commeting...")
    comments=['🔥🔥🔥','👍🏼👍🏼👍🏼','🤩🤩🤩','👌🏽👌🏽👌🏽','✌️✌️✌️']
    lim= round(len(posts)*percent/100)
    for i in random.sample(list(posts.keys()),lim):
        comm=random.sample(comments , 1)
        api.post_comment(media_id =posts[i][0] , comment_text= comm[0])   
        print(f'Commented Successfuly on the post https://www.instagram.com/p/{i}')
        time.sleep(5)


# In[5]:


len(posts)


# In[219]:


commenting(10)


# In[15]:


def main():
    user_name = 'iamzansir'
    password = 'mishalia'
    #Set your parameters
    tags= ['Warzone','callofduty']
    #Posts per Tag to like
    ppt = 10 
    
    global api
    try:
        api = Client(user_name, password)
        print('Login Sucess...')
    except Exception as e:
        print(f'Login Failed. \nError: {e}')

    like_tags(tags, ppt)
    #input is the % of accounts to follow (accounts whose post you liked)
    follow_liked(20)
    commenting(50)


# In[25]:


if __name__== main():
    main()


# In[ ]:




