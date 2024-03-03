from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class AuctionTally():
    def tally(self, url, class_name):
        driver_manager = EdgeChromiumDriverManager()
        executable_path = driver_manager.install()
        edge_service = webdriver.EdgeService(executable_path=executable_path)
        options = webdriver.EdgeOptions()
        options.add_argument("--log-level=3")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Edge(service=edge_service, options=options)
        driver.get(url)
        driver.implicitly_wait(10)
        
        bids = driver.find_elements(By.CLASS_NAME, class_name)

        total = 0
        for bid in bids:
            total += float(bid.text[1:].replace(',', ''))

        return(total)
    
if __name__ == "__main__":
    tallier = AuctionTally()
    url = "https://tiltify.com/@dokibird/auctions/dokicharity2024"
    class_name = "iHbIIK"
    total = tallier.tally(url, class_name)
    print("${:,.2f}".format(round(total, 2)))
    
    