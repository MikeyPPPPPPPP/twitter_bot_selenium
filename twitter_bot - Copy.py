from selenium import webdriver
import time
import bs4 as bs
import urllib.request
import random
import pyautogui

share = ['tictok exposed https://youtu.be/32HLZycYOnw @YouTube ']

stupid_replys = ["reddit 50 50","how old are you? hopfully older that 20.","DUNC!","Mabey?",\
                 "What is the financal gain?","Great, makes me feel great",\
                 "Runt","See ya chump","How dose this affect you politicly",\
                 "One word,  Elon Musk","SIMP",\
                 "How","Explain","no money no food","in the hall of the mountain king",\
                 "this is for you bill, Bill Cosby ","fill in the blank, Anti-",\
                 "Is the pope still relevent","hack starbucks","This is great, we need more",\
                 "how original", "fight the power","ya because, well you know","this is vary sad",\
                 "take this with a grain of salt","down a bottle of ever clear",\
                 "Jeff who?","this is comparable to Ed Gein","how many lungs are on earth?"]        
Tabs = ["COVID-19","Trending","News","Sports","Entertainment"]        



class randomization_engine:
    
    def __init__(self):
        self.rev_counter = 0
        self.timed = 10
        self.master = 5

        self.Min = 1
        self.Max = 10
        self.Like = 2
        self.Rel = 4
        self.For_me = 2

    def master_t(self):
        time.sleep(self.master)

    def tab_time(self):
        t = (self.For_me + self.Like + self.Max)/ self.Rel
        self.timed += abs(t - self.master) + self.master
        time.sleep(self.timed)
        
    def by_tweet(self):
        t = (self.Min + self.Like + self.Rel)/ 3
        time.sleep((self.Min + self.Like + self.Rel)/ 3)
        self.rev_counter += abs(t - self.master)

    def full_mix(self):
        self.Min = random.randint(1,2)
        self.Max = 5
        self.Like = random.randint(2,3)
        self.Rel = random.randint(4,5)
        self.For_me = random.randint(1,2)
        







    
class TwitterBot:
    #stupid_replys = ["what?","DUNC!","Mabey?","what is the financal gain?","great, makes me feel great","runt","see ya chump","how dose this affect you politicly","one word,  Elon Musk"]
    def __init__(self):
        self.paths = []#for the spider
        self.hashtages = []#for splider
        self.spider_depth = 10#for spider
        self.spider_counter = 0
        self.randome_users = []
        self.followed_followers = []
        self.trendy_hashtags = ['#love','#instagood','#photooftheday','#fashion','#beautiful','#happy','#cute','#tbt','#life','#music','#amazing','#nofilter','#sunset','#motivation','#instamood','#foodporn']
        
        self.randimization = randomization_engine()
        self.browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.url = "https://twitter.com/" #You can paste any id
        self.username = "" #Enter your id
        self.password = ""  #Enter your password
        self.browser.get(self.url)
        time.sleep(2)

    def press_heart_button(self):
        self.browser.find_element_by_xpath('//*[@data-testid="like"]').click()

    def retweet(self):
        self.browser.find_element_by_xpath('//*[@data-testid="retweet"]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@data-testid="retweetConfirm"]').click()

    
    def settings_error(self):
        time.sleep(2)
        if self.browser.current_url == 'https://twitter.com/settings':
            time.sleep(2)
            self.browser.execute_script("window.history.go(-1)")
        else:
            pass
        
    def stop_me(self):
        time.sleep(1)
        self.browser.quit()
        
    def login(self):
        #clicks login
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div').click()    
        time.sleep(2)
        #enters username
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').click()
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(self.username)
        #enter password
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').click()
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(self.password)
        #click login buttom
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span').click()
        time.sleep(2)

    def Home(self):
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[1]/h1/a').click()
        time.sleep(2)
        
    def tweet(self, crap):
        try:
            pyautogui.write(crap)
            #self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(crap)#browser.find_elements_by_class_name('//*[@data-testid="tweetTextarea_0"]').send_keys(crap)
            #self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div').send_keys(crap)
            time.sleep(1)
            
            #click tweet
            self.browser.find_element_by_xpath('//*[@data-testid="tweetButton"]').click()
        except:
            pass
        #self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span').click()
    #tis will click the first 3 trending topics 
    def explore_button(self):
        try:
            self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div/div').click()
            time.sleep(3)
        except:
            self.browser.get('https://twitter.com/explore')


    def tab(self,ta):
        self.browser.get('https://twitter.com/explore/tabs/'+ta.lower())
        
    
    

    def just_heart_button(self,tab_name):
        #clicks trending button
        self.browser.find_element_by_link_text(tab_name).click()
        time.sleep(3)
        for x in range(5,20):
            
            try:
                self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div['+str(x)+']/div/div').click()
        
                time.sleep(3)
                
                #this will randomly like the tweet
                self.press_heart_button()
                
                
                
            except:
                pass
            self.explore_button()
            time.sleep(3)



    def trash_talk_headline(self,tab_name):
        #clicks trending button
        self.browser.find_element_by_link_text(tab_name).click()
        time.sleep(1)
        for x in range(5,20):
            
            try:
                self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div['+str(x)+']/div/div').click()
        
                time.sleep(1)
                
                #this will randomly like or retweet
                twash = random.randint(0,6)
                if twash > 3:
                    self.retweet()
                self.press_heart_button()
                
                
                #this will click the reply button
                self.browser.find_element_by_xpath('//*[@data-testid="reply"]').click()
                crap_to_say = share#stupid_replys[random.randint(0,len(stupid_replys)-1)]
                time.sleep(4)
                self.browser.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div').click()
                self.browser.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div').send_keys(crap_to_say)
                time.sleep(5)
                try:
                    self.browser.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]/div').click()
                except:
                    try:
                        self.browser.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div').click()
                        self.browser.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div').send_keys(str(random.randint(1,100)))
                        self.browser.find_element_by_xpath('//*[@data-testid="tweetButton"]').click()
                    except:
                        self.browser.find_element_by_xpath('//*[@aria-label="close"]').click()
            except:
                pass
            self.explore_button()
            time.sleep(3)

    def share_my_video(self,tab_name):
        #clicks trending button
        try:
            
            self.browser.find_element_by_link_text(tab_name).click()
            time.sleep(1)
            for x in range(5,20):
            
                try:
                    self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div['+str(x)+']/div/div').click()
            
                    time.sleep(1)
                    
                    #this will randomly like or retweet
                    twash = random.randint(0,6)
                    if twash > 3:
                        self.retweet()
                    self.press_heart_button()
                    
                    
                    #this will click the reply button
                    try:
                        self.browser.find_element_by_xpath('//*[@data-testid="reply"]').click()
                    except:
                        self.browser.execute_script("window.scrollTo(0,50)")
                        time.sleep(1)
                        
                        self.browser.find_element_by_xpath('//*[@data-testid="reply"]').click()
                        
                    print('tweeting')#life tictok exposed https://youtu.be/32HLZycYOnw @YouTube 3 #amazing tictok exposed https://youtu.be/32HLZycYOnw @YouTube 
                    time.sleep(1)
                    #t = 896I compleatly agree with you https://youtu.be/BQ7kMKTb-eA via @YouTube 
                    try:
                        t = str(random.randint(1,1000))+' '+str(random.choice(self.trendy_hashtags))+' '+'tictok exposed https://youtu.be/32HLZycYOnw @YouTube '
                        self.tweet(t)
                    except Exception as inst:
                        print(inst)
                        print('failed')
                        pass
                    
                except Exception as inst:
                    print(inst)
                    pass
                if ' ' in tab_name:
                    self.explore_button()
                    time.sleep(3)
                else:
                    
                    self.tab(tab_name)
                    #self.explore_button()
                    time.sleep(3)
        except:
            self.explore_button()
            time.sleep(3)
        
        
            


    def spider_legs(self,url):#spider via trends and hash tags
        '''
        #clicks trending button
        self.browser.find_element_by_link_text(tab_name).click()
        time.sleep(1)
        bot.browser.current_url
        '''
        
        self.spider_counter += 1
        self.browser.get(url)
            
        try:
            li = self.browser.find_elements_by_tag_name('div')
            for x in li[2].text.split('\n'):
                print(x)
                if x.startswith('#') == True:
                    if x not in self.hashtages:
                        self.hashtages.append(x)
                        self.paths.append('https://twitter.com/search?q='+x)
                else:
                    pass
                    
        except:
            pass
        try:
            if self.spider_depth != self.spider_counter:
                self.spider_legs('https://twitter.com/search?q='+self.hashtages[-1])
        except:
            time.sleep(1)
            self.browser.find_element_by_xpath('//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div[1]/a').click()
            time.sleep(1)
            self.spider_legs(url)

    def find_people(self):
        #clicks trending button
        self.browser.find_element_by_link_text("Trending").click()
        time.sleep(3)
        #//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[4]/div/div/div/div[2]/span
        #//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[5]/div/div/div/div[2]/span
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        for x in range(4,40):
            try:
                self.randome_users.append(self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div['+str(x)+']/div/div/div/div[2]/span').text)
            except:
                pass

    def get_all_posts(self,tab_name):
        #clicks trending button
        self.browser.find_element_by_link_text(tab_name).click()
        time.sleep(1)
        for x in range(5,20):
            time.sleep(4)
            self.settings_error()#error handeling
            try:#this will click seach post 
                self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div['+str(x)+']').click()
                time.sleep(3)
                self.settings_error()#error handeling
                try:
                    
                    self.browser.find_element_by_xpath('//*[@role="article"]').click()
                    self.settings_error()#error handeling
                    
                    #this will reply and like
                    self.press_heart_button()
                    #this will click the reply button
                    try:
                        self.browser.find_element_by_xpath('//*[@data-testid="reply"]').click()
                    except:
                        self.browser.execute_script("window.scrollTo(0,50)")
                        time.sleep(1)
                                
                        self.browser.find_element_by_xpath('//*[@data-testid="reply"]').click()
                                
                    print('tweeting')#life tictok exposed https://youtu.be/32HLZycYOnw @YouTube 3 #amazing tictok exposed https://youtu.be/32HLZycYOnw @YouTube 
                    time.sleep(3)
                        #t = 896I compleatly agree with you https://youtu.be/BQ7kMKTb-eA via @YouTube 
                    try:
                        t = str(random.randint(1,1000))+' '+str(random.choice(self.trendy_hashtags))+' '+'follow me please'
                        self.tweet(t)
                    except Exception as inst:
                        print(inst)
                        print('failed')
                        pass

                    #this will go back a page
                    self.browser.execute_script("window.history.go(-1)")
                except Exception as e:
                    print('skipped post ')
                    print(e)
                '''
                for post in range(1,5):
                    try:
                        time.sleep(5)
                        #this will click the post
                        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[5]/div/div/section/div/div/div['+str(post)+']').click()
                        time.sleep(5)



                        #this will reply and like
                        self.press_heart_button()
                        #this will click the reply button
                        try:
                            self.browser.find_element_by_xpath('//*[@data-testid="reply"]').click()
                        except:
                            self.browser.execute_script("window.scrollTo(0,50)")
                            time.sleep(1)
                            
                            self.browser.find_element_by_xpath('//*[@data-testid="reply"]').click()
                            
                        print('tweeting')#life tictok exposed https://youtu.be/32HLZycYOnw @YouTube 3 #amazing tictok exposed https://youtu.be/32HLZycYOnw @YouTube 
                        time.sleep(3)
                        #t = 896I compleatly agree with you https://youtu.be/BQ7kMKTb-eA via @YouTube 
                        try:
                            t = str(random.randint(1,1000))+' '+str(random.choice(self.trendy_hashtags))+' '+'tictok exposed https://youtu.be/32HLZycYOnw @YouTube '
                            self.tweet(t)
                        except Exception as inst:
                            print(inst)
                            print('failed')
                            pass

                        #this will go back a page
                        self.browser.execute_script("window.history.go(-1)")
                    except Exception as e:
                        print('skipped post ')
                        print(e)
                '''
                
                #this will ensure we go back to the starting point for the next post
                self.explore_button()
                time.sleep(3)
                self.browser.find_element_by_link_text(tab_name).click()
                time.sleep(1)
                
            except:
                pass
            self.explore_button()
            time.sleep(3)

bot = TwitterBot()
print("Logging In")
bot.login()

bot.Home()
print('Deploying BOT')
bot.explore_button()
'''
for x in Tabs:
    bot.get_all_posts(x)
'''
for x in Tabs:
    
    print("on Tab "+x)
    #bot.just_heart_button(x)
    bot.share_my_video(x)


bot.stop_me()
print("Stopped")


