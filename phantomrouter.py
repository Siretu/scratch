import time
import argparse
from selenium import webdriver
from BeautifulSoup import BeautifulSoup

def psource(s):
    soup = BeautifulSoup(s)
    print soup.prettify()

def forwardPort(args):
    # Open page
    driver = webdriver.PhantomJS("/home/siretu/work/phantomjs/bin/phantomjs")
    driver.get("http://%s:%s@192.168.1.1" % (args.user, args.password))
    
    # Select top
    driver.switch_to_frame(driver.find_element_by_id("topframe"))
    
    # Go to advanced
    driver.find_element_by_id("advanced_label").click()
    
    # Click advanced menu
    driver.find_element_by_id("advanced_bt").click()

    # Go to port forwarding menu
    dt = driver.find_element_by_id("forwarding_triggering")
    dt.find_element_by_xpath(".//a").click()

    # Switch to main frame
    driver.switch_to_frame(driver.find_element_by_id("formframe"))
    
    # Add port forwarding
    driver.find_element_by_id("add_long").click()

    # Wait for it to load
    print "Loading"
    time.sleep(10)

    # Fill in info
    driver.find_element_by_name("portname").send_keys(args.name)
    driver.find_element_by_name("port_start").send_keys(args.port_start)
    driver.find_element_by_name("port_end").send_keys(args.port_end)
    driver.find_element_by_name("server_ip4").send_keys(args.ip.split(".")[-1])

    # Submit
    driver.find_element_by_name("Apply").click()

def main():
    parser = argparse.ArgumentParser(description='Forwards a port')
    parser.add_argument("-u","--user",help="Username for router login",required=True)
    parser.add_argument("-p","--password",help="Password for router login",required=True)
    parser.add_argument("-n","--name",help="Name for the port forwarding rule",required=True)
    parser.add_argument("-ps","--port-start",help="Start for the range of ports",required=True)
    parser.add_argument("-pe","--port-end",help="End for the range of ports",required=True)
    parser.add_argument("-i","--ip",help="Local ip to forward to",required=True)
    args = parser.parse_args()
    print vars(args)
    start = time.time()
    forwardPort(args)
    print "Took %fs" % (time.time() - start)

if __name__ == "__main__":
    main()
