#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException, SessionNotCreatedException
from urllib3.exceptions import NewConnectionError, MaxRetryError
from os import getcwd, system
import config
from helpers import *
from banner import banner

DRIVER_PATH = getcwd() + '/driver/phantomjs'

    
class FollowiOSDevs:
        
    def __init__(self, username: str, password: str):
      self.username = username
      self.password = password
      try:
        info("Starting browser...", end="\r")
        self.browser = webdriver.Safari()
        success("Browser started", flush=True)
      except SessionNotCreatedException:
          error("Please close existing safari automation window",flush=True)
          self.browser = None
      
    def login(self):
        if self.browser == None:
            return False
        browser = self.browser
        try:
            masked_password = "*" * len(self.password)
            info("Trying to login as @"+self.username + " with password: "+masked_password , end="\r")
            browser.get(TwitterURL.login)
            wait()
            username_field = browser.find_element_by_xpath(ElementPaths.username_login_field)
            password_field = browser.find_element_by_xpath(ElementPaths.password_login_field)
            username_field.send_keys(self.username)
            password_field.send_keys(self.password)
            password_field.send_keys(Keys.RETURN)
            wait()
            if browser.current_url == TwitterURL.home:
                success("Login Successful", flush=True)
                return True
        except:
            pass
        error("Login failed. Please check your username or password", flush=True)
        return False
            
    def follow(self, username: str):
        browser = self.browser
        browser.get(TwitterURL.profile(username))
        wait()
        try:            
            follow_button_element = browser.find_elements_by_xpath(ElementPaths.follow_button)
            unfollow_button_element = browser.find_elements_by_xpath(ElementPaths.unfollow_button)
            if len(follow_button_element) > 0:
                wait()
                follow_button_element[0].click()
                wait(1)
                success("Followed @"+username, flush=True)
            elif len(unfollow_button_element) > 0:
                success("User @"+username+ " followed already", flush=True)
            else:
                warning("Account doesn't exists for handle: @"+username, flush=True)
                                
        except NoSuchElementException:
            error("Something went wrong when following @"+username, flush=True)
    
    def follow_devs(self, handles):
        try:
            if not self.login():
                return
            if self.username in handles: 
                handles.remove(self.username)
            total_handles = len(handles)
            for index,handle in enumerate(handles):
                info("["+str(index+1)+"/"+ str(total_handles) + "] Trying to follow @"+handle, end="\r")
                self.follow(handle)
        except:
            pass
            
    def quit(self):
        if self.browser == None:
            return
        info("Quitting...", flush=True)
        self.browser.quit()
        wait(1)
        success("Bye", flush=True)

def start():
    handles = get_handles()
    app = FollowiOSDevs(username=config.USERNAME,password=config.PASSWORD)
    app.follow_devs(handles)
    # app.follow(handles[4])
    app.quit()


def get_handles():
    import json 
    handle_file = open('handles.json') 
    handles = json.load(handle_file)
    handle_file.close()
    return handles

if __name__ == '__main__':
    system('clear')
    banner()
    if config.USERNAME == "" or config.PASSWORD == "":
        error("Please enter the credentials in config.py file")
    else:  
        try:
            start()
        except Exception:
            pass