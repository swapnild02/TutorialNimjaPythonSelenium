from abc import ABC,abstractmethod
class LoginPageInterface(ABC):

    @abstractmethod
    def enter_email_address(self, email_address):
        pass

    @abstractmethod
    def enter_password(self, password_text):
        pass

    @abstractmethod
    def click_on_login_button(self):
        pass

    @abstractmethod
    def retrieve_warning_message(self):
        pass
