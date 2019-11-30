import datetime
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from django.utils import timezone
from selenium import webdriver
from polls.models import Question, Choice


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (days < 0 for questions published
    in the past, days > 0 for questions published in the future).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    question = Question.objects.create(question_text=question_text, pub_date=time)
    return question

class SeleniumTestCase(LiveServerTestCase):

    username = 'bamee'
    password = '123'

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='/Users/bamee/Downloads/chromedriver')
        super(SeleniumTestCase, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(SeleniumTestCase, self).tearDown()

    def test_find_header(self):
        self.browser.get(self.live_server_url + '/polls/')
        header = self.browser.find_element_by_tag_name('h1')
        self.assertEqual('Current Polls', header.text)

    def test_find_poll(self):
        test_question = create_question('Test', days=0)
        self.browser.get(self.live_server_url + '/polls/')
        question = self.browser.find_element_by_id(f"question{test_question.id}")
        self.assertEqual('Test', question.text)

    def test_poll_hyperlink(self):
        question = create_question('Test', days=0)
        self.browser.get(self.live_server_url + '/polls/')
        links = self.browser.find_elements_by_tag_name('a')
        links[1].click()
        self.assertEqual(self.browser.current_url, self.live_server_url + '/polls/' + f"{question.id}/")

    def test_question_result(self):
        question = create_question('Test', days=0)
        choice = Choice.objects.create(choice_text='test choice', question=question)
        User.objects.create_user(self.username, password=self.password)
        self.browser.get(self.live_server_url + '/accounts/login')
        self.browser.find_element_by_id("id_username").send_keys(self.username)
        self.browser.find_element_by_id("id_password").send_keys(self.password)
        self.browser.find_element_by_id("login_info").click()
        link = self.browser.find_element_by_tag_name('a')
        link.click()
        choice1 = self.browser.find_element_by_id(f"choice{choice.id}")
        choice1.click()
        self.browser.find_element_by_id(f"vote_button").click()
        self.assertEqual(self.browser.current_url, self.live_server_url + '/polls/' + f"{question.id}/results/")