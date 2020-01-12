from selenium import webdriver
import datetime
from time import sleep

class RenewBot:
    def __init__(self,cardNumber,pin):
        self.driver = webdriver.Chrome()
        self.driver.get("https://account.torontopubliclibrary.ca/checkouts")
        sleep(2)
        card_num_field = self.driver.find_element_by_id('userID')
        pin_num_field = self.driver.find_element_by_id('password')
        card_num_field.send_keys(cardNumber)
        pin_num_field.send_keys(pin)


        sign_in = self.driver.find_element_by_xpath('//*[@id="form_signin"]/div/button')
        sign_in.click()

        #Navigate to Checkouts
        sleep(2)
        self.driver.get("https://account.torontopubliclibrary.ca/checkouts")
        sleep(3)
        due_date = self.driver.find_element_by_class_name('date').text
        year = '2020'
        month = due_date.split()[2]
        day = due_date.split()[1]
        expiryString = month + ' ' + day + ' ' + year 
        
        currentDate = datetime.datetime.now()
        expiryDate = datetime.datetime.strptime(expiryString, '%b %d %Y')

        daysSinceExpiry = (currentDate-expiryDate).days
        
        print(daysSinceExpiry)
        sleep(2)
        print('time to renew')

        
        renewButton = self.driver.find_element_by_xpath('//*[@id="PageContent"]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[8]/button')
        
        if daysSinceExpiry >= 0:
            renewButton.click()


RenewBot('your library card number','your library card pin')