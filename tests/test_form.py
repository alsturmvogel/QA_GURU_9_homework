from pages.registration_page import registration_page
from models import users


def test_register_student():
    student = users.student

    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)