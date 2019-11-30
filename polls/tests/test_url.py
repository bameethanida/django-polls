from selenium import webdriver
import requests


def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    all_links = []
    browser = webdriver.Chrome(executable_path='/Users/bamee/Downloads/chromedriver')
    browser.get(url)
    elements = browser.find_elements_by_tag_name("a")
    for ele in elements:
        all_links.append(ele.get_attribute('href'))
    browser.close()
    return all_links


def invalid_urls(urllist):
    invalid_links = []
    for url in urllist:
        r = requests.head(url)
        if r.status_code == 404:
            invalid_links.append(url)
    return invalid_links


if __name__ == "__main__":
    link_list = get_links("https://cpske.github.io/ISP/")
    for url in link_list:
        print("Valid: " + url)
    print()
    invalid_url = invalid_urls(link_list)
    for inv_url in invalid_url:
        print("Invalid: " + inv_url)