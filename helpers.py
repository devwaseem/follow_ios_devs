import time, sys
from termcolor import cprint
from config import WAIT_TIME, USE_EMOJI

def wait(t=WAIT_TIME):
    time.sleep(t)
    
def info(text,flush=False, end='\n'):
    if flush: flushLine()
    symbol = "⚙️  " if USE_EMOJI else "[*] "
    cprint(symbol+text, 'cyan',end=end)
    
def warning(text,flush=False,end='\n'):
    if flush: flushLine()
    symbol = "👀 " if USE_EMOJI else "[!] "
    cprint(symbol+text,'yellow',end=end)

def success(text,flush=False,end='\n'):
    if flush: flushLine()
    symbol = "✅ " if USE_EMOJI else "[✓] "
    cprint(symbol+text,'green',end=end)
    
def error(text,flush=False,end='\n'):
    if flush: flushLine()
    symbol = "🚫 " if USE_EMOJI else "[✗] "
    cprint(symbol+text,'red', file=sys.stderr,end=end)
    
def flushLine(space = 100):
    print(" "* space,end="\r")

class ElementPaths:
    username_login_field = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
    password_login_field = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
    follow_button = "//span[text()='Follow']/ancestor::div[@role='button']"
    unfollow_button = "//span[text()='Following']/ancestor::div[@role='button']"
    
class TwitterURL:
    base = "https://twitter.com"
    login = base + "/login"
    home = base + "/home"

    def profile(username):
        return TwitterURL.base + "/" + username

