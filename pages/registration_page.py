from selene import browser, have, by
from models.users import User


class RegistrationPage:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def register(self, user: User):
        self.fill(user).submit()
        return self

    def fill(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element(
            f'label[for="gender-radio-{user.gender_number}"]'
        ).click()
        browser.element('#userNumber').type(user.phone)

        # Дата рождения
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(
            '.react-datepicker__month-select'
        ).element(f'option[value="{user.birth_month_value}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(
            '.react-datepicker__year-select'
        ).element(f'option[value="{user.birth_year}"]').click()
        browser.element(
            f'.react-datepicker__day--0{user.birth_day}'
        ).click()

        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.element(
            f'label[for="hobbies-checkbox-{user.hobby_number}"]'
        ).click()
        browser.element('#uploadPicture').send_keys(
            str(user.picture.resolve())
        )
        browser.element('#currentAddress').type(user.address)
        browser.element('#state').click()
        browser.element('#state').element(by.text(user.state)).click()
        browser.element('#city').click()
        browser.element('#city').element(by.text(user.city)).click()

        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_registered(self, user: User):
        browser.element('#example-modal-sizes-title-lg').should(
            have.exact_text('Thanks for submitting the form')
        )
        browser.element('.table-responsive').all('tr').should(
            have.exact_texts(
                'Label Values',
                f'Student Name {user.first_name} {user.last_name}',
                f'Student Email {user.email}',
                f'Gender {user.gender}',
                f'Mobile {user.phone}',
                f'Date of Birth {user.birth_day} {user.birth_month},{user.birth_year}',
                f'Subjects {user.subject}',
                f'Hobbies {user.hobby}',
                f'Picture {user.picture.name}',
                f'Address {user.address}',
                f'State and City {user.state} {user.city}',
            )
        )


registration_page = RegistrationPage()
