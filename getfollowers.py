from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import pandas as pd
from userinfo import your_username,your_password #to bring your username and password from another file

class Instagram:
    def __init__(self,your_username,your_password):
        chromedriver_path = '/usr/local/bin/chromedriver' #the file path in your computer
        self.browser=webdriver.Chrome(executable_path=chromedriver_path)
        self.your_username=your_username
        self.your_password=your_password
        self.signIn()

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login')
        sleep(3)
   
        username_input=self.browser.find_element_by_name('username') #your personal username
        username_input.send_keys(self.your_username)
        password_input=self.browser.find_element_by_name('password') #your password
        password_input.send_keys(self.your_password)
        password_input.send_keys(Keys.ENTER)
        sleep(7)

        # for_popup = self.browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        # for_popup.click() #use these two lines if you get pop up 
        # sleep(3)

    def existing_users(self):
        
        
        self.browser.get('https://www.instagram.com/mmeventt/')
        items=self.browser.find_elements_by_css_selector('li.Y8-fY')   
        items[2].click()
        sleep(5)
        extg_userlist=[]
        
        username=self.browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[2]').text
        print(username)
        extg_userlist.append(username)
        print(extg_userlist)
        

        # action=webdriver.ActionChains(self.browser)      
        # dialog=self.browser.find_element_by_css_selector('div[role=dialog]')
        
        # dialog.click()
        # action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        # time.sleep(2)

        extg_user_df = pd.DataFrame(extg_userlist)
        extg_user_df.to_csv('takipci/extg_userslist.csv',index=True)
        

        
        


    def actions(self):
        
        hashtags= ['giftboxes','mysucculent','giftideas','succulentlove'] #choose your hashtags as your interests
        

        new_followed = []
        comment=0
        tag = 0
        followed = 0
        likes = 0


        for hashtag in hashtags:
            
            self.browser.get('https://www.instagram.com/explore/tags/'+ hashtags[tag] + '/')
            sleep(5)
            first_pic = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]')
            first_pic.click()
            sleep(randint(1,2))  
            tag += 1

                   
            for x in range(0,100):
                username = self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
                

                if self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                    self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                    new_followed.append(username)
                    followed += 1

                    #to like
                    like = self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click() 
                    likes += 1
                    sleep(randint(20,26))
                    

                    # to make comment
                    comment_type=randint(1,15)  
                    self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button').click()
                    comment_box=self.browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea')                             
                    
                    #i created different if statements, you can diversify
                    if comment_type==1:
                        comment_box.send_keys('Really cool!')
                    elif comment_type==2:
                        comment_box.send_keys('Nice Pic, Loved it!')
                    elif comment_type==3 or comment_type==4 :
                        comment_box.send_keys('Awesome Pic!')
                    elif comment_type==5 or comment_type==6 :
                        comment_box.send_keys('Awesome Pic!')
                    elif comment_type==7 or comment_type==8 :
                        comment_box.send_keys('So Cool!')
                    else:
                        continue
                    if comment_type  >8 : 
                        comment+=1                        
                    comment_box.send_keys(Keys.ENTER)
                     
                    sleep(5)

                self.browser.find_element_by_link_text('Next').click()
                sleep(randint(19,29))
                
                    
                
                    

        updated_user_df = pd.DataFrame(new_followed)
        updated_user_df.to_csv('takipci/newuserlist.csv',mode='a', index=True,header=False) #to send new users to our file

        print('{} Liked,{} Commented Photos.'.format(likes,comment))
        print('{} New People Followed'.format(followed))
        print(new_followed)

    def unfollow(self):
        new_userslist=[]
        new_userslist=pd.read_csv('takipci/newuserlist.csv', delimiter=',')
        new_userslist=list(new_userslist['0'])
        sleep(3)
        
        for x in range(0,80):
            self.browser.get('https://www.instagram.com/'+your_username+'/')
            items=self.browser.find_elements_by_css_selector('li.Y8-fY')   
            items[2].click()
            sleep(randint(10,15))
            
            

            for i in range(0,2):
                        
                
                followers=self.browser.find_element_by_css_selector('div[role=dialog]').find_elements_by_tag_name('li') 
                d_username=followers[i].find_element_by_tag_name('a').text  
                print(d_username)
                if d_username  in new_userslist:
                    followers[i].find_element_by_tag_name('button').click()
                    sleep(randint(3,5))
                    self.browser.find_element_by_class_name('mt3GC').find_element_by_tag_name('button').click()
                    sleep(randint(3,5))
                else:
                    break
                
            self.browser.refresh() #i keep refresh the pages instead of scroll down to not get some errors
            # sleep(randint(600,650)) #to keep account safe 2 unfollow per ten minute
            sleep(2)
    

instagram=Instagram(your_username,your_password)
instagram.actions()
# instagram.unfollow()
# instagram.existing_users()
