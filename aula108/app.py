from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r'user-data-dir=\Users\user\AppData\Local\Google\Chrome\User Data\Default')
        self.chrome = webdriver.Chrome(self.driver_path, options=self.options)

    def clica_sing_in(self):
        try:
            btn_sing_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sing_in.click()
        except Exception as erro:
            print(f'ERRO ao clicar em Sing in: {erro}')

    def faz_log_out(self):
        try:
            botao = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > div'
                '.Header-item.position-relative.mr-0.d-none.d-md-flex > detail'
                's > details-menu > form > button')
            botao.click()
        except Exception as erro:
            print(f'erro ao delogar: {erro}')

    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    def login_git(self, username, password):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_sing_in = self.chrome.find_element_by_name('commit')

            input_login.send_keys(username)
            input_password.send_keys(password)

            btn_sing_in.click()

        except Exception as erro:
            print(f'ERRO ao fazer login {erro}')

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header '
                                                              '> div.Header-item.position-relative.mr-0.d-none.d-md-fle'
                                                              'x > details')
            perfil.click()

        except Exception as erro:
            print(f'ERRO ao clicar no perfil: {erro}')

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa(r'https://github.com/')

    chrome.clica_perfil()
    sleep(3)
    chrome.faz_log_out()

    chrome.clica_sing_in()
    chrome.login_git('seu gmail', 'sua senha')

    chrome.clica_perfil()
    chrome.verifica_usuario('seu nome de usuário')

    sleep(7)
    chrome.sair()
