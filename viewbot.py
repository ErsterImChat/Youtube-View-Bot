import time
from pytube import *
import pafy
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from colorama import *
from selenium.webdriver.chrome.service import Service


# Defining the Channel URL
try:
    print("Please enter your Channel-URL now:")
    c = Channel(input())
except:
    print("That is not a valid Channel URL")
    quit()


# Asking if all Videos from the Channel should be player
print("Do you want to watch all Videos from this Channel? (yes/no): ")
all_videos = input()

match all_videos:
    case "no":
        print("How many Videos do you want to watch?: ")
        video_amount = input()

# Asking if the Videos should be played till the end
print("Do you want to watch the Videos till the End? (yes/no): ")
watch_till_end = input()
match watch_till_end:
    case "no":
        print("How long do you want to watch the Videos (seconds): ")
        watch_duration = input()

# Making Chrome Headless and intitializing a Selenium Webdriver to view the Videos
# also disabling logging of the Webdriver Manager and initializing colorama
init()


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-logging")
options.add_argument('--headless')
options.add_experimental_option("excludeSwitches", ["enable-logging"])


ChromeDriverManager(log_level=0)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


# Accepting YouTube Cookies

driver.get("https://youtube.com")
time.sleep(5)
CookieButton = driver.find_element(by=By.XPATH, value="/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button")
CookieButton.click()




match watch_till_end:

    case "yes":

        # Introducing an endless for-Loop which runs through all Videos from the Channel

        video_player_counter = 1

        while True:

            match all_videos:

                case "yes":

                    for url in c.video_urls:

                        # Going to the URL of the Video
                        driver.get(url)

                        # Get the Video Duration using Package "pafy"
                        # and waiting that Time till watching the next.
                        v = pafy.new(url)
                        print(Fore.MAGENTA + str(video_player_counter) + ". Video plays now")
                        video_player_counter += 1
                        time.sleep(v.length)

                case "no":

                    for url in c.video_urls[int(video_amount)]:
                        # Going to the URL of the Video
                        driver.get(url)

                        # Get the Video Duration using Package "pafy"
                        # and waiting that Time till watching the next.
                        v = pafy.new(url)
                        print(Fore.MAGENTA + str(video_player_counter) + ". Video plays now")
                        video_player_counter += 1
                        time.sleep(v.length)



    case "no":

        # Introducing an endless for-Loop which runs through all Videos from the Channel

        video_player_counter = 1

        while True:

            match all_videos:

                case "yes":

                    for url in c.video_urls:
                        # Going to the URL of the Video
                        driver.get(url)

                        print(Fore.MAGENTA + str(video_player_counter) + ". Video plays now")
                        video_player_counter += 1
                        time.sleep(int(watch_duration))

                case "no":

                    for url in c.video_urls[:int(video_amount)]:
                        # Going to the URL of the Video
                        driver.get(url)

                        print(Fore.MAGENTA + str(video_player_counter) + ". Video plays now")
                        video_player_counter += 1
                        time.sleep(int(watch_duration))
