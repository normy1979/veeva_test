import pytest
import os
from application import init_app, db
from application.models.models import Veevainfo

from selenium import webdriver
from application.tests.LoginTest import LoginTest
from application.tests.RecordSubjectDataTest import RecordSubjectDataTest

import time

@pytest.fixture(scope="module")
def app():
    app = init_app()
    app.config.update({
        "TESTING": True,
    })

    # Setup DB   
    with app.app_context():
        exists = Veevainfo.query.filter_by(username='mrfleshe@umich.edu').first()
        if not exists:
            put1 = Veevainfo(username='mrfleshe@umich.edu', password='VeevaRTSM', rtsm_url='https://rtsm-val.veeva.com/VEV-901/')
            db.session.add(put1)
            db.session.commit()
            
    yield app
    
    if os.path.exists("testing.sqlite"):
        os.remove("testing.sqlite")


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()


@pytest.fixture(scope="module")
def runner(app):
    return app.test_cli_runner()

@pytest.fixture(scope="module")
def setup_driver(app):
    print("Initiating chrome driver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")

    pytest.driver = webdriver.Chrome(options = chrome_options)
    
    with app.app_context():
        veeva_users = Veevainfo.query.all()
    print(str(veeva_users[0].rtsm_url))
    pytest.driver.get(str(veeva_users[0].rtsm_url))

    yield pytest.driver
    pytest.driver.close()

def test_login(setup_driver, app):
    with app.app_context():
        veeva_users = Veevainfo.query.all()
        
    login_test = LoginTest(pytest.driver, veeva_users[0].username, veeva_users[0].password)
    login_test.login()
    assert(pytest.driver.current_url == "https://rtsm-val.veeva.com/VEV-901/Subjects.aspx")
    time.sleep(2)
    
def test_record_subject(setup_driver):     
    record_subject_test = RecordSubjectDataTest(pytest.driver)
    site_number = record_subject_test.click()
    time.sleep(2)
    assert site_number == "103"
    
def test_home(client):
    response = client.get("/")
    assert b"<p>mrfleshe@umich.edu" in response.data
