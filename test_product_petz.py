import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Test_Simple_Petz():
    def setup_method(self):
        self.driver = webdriver.Chrome('drivers/chromedriver100.exe')
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_consultar_produto(self):
        nome_produto = 'Ração Nutricon Turtle para Tartarugas'
        tamanho_produto = '25g'
        preco_produto = 'R$ 14,99'

        # Home Page
        self.driver.get('https://www.petz.com.br')

        self.driver.find_element(By.ID, 'aceiteLgpd').click()
        self.driver.find_element(By.ID, 'search').click()
        self.driver.find_element(By.ID, 'search').send_keys('Ração Nutricon Turtle para Tartarugas')
        self.driver.find_element(By.ID, 'search').send_keys(Keys.ENTER)

        # Product Page
        self.driver.implicitly_wait(20)

        print(f'Achou o produto!')
        assert self.driver.find_element(By.CSS_SELECTOR, 'div.product-title').text == nome_produto
        print(f'Validou o produto!')

        self.driver.find_element(By.CSS_SELECTOR, 'button.size-select-button').click()
        self.driver.find_element(By.ID, '151954').click()

        assert self.driver.find_element(By.CSS_SELECTOR, 'div.item-name').text == tamanho_produto
        print(f'Validou o tamanho!')

        time.sleep(5)

        assert self.driver.find_element(By.CSS_SELECTOR, 'div.current-price-left').text == preco_produto
        print(f'Validou o preco!')

        assert self.driver.title == 'Alimento para tartaruga: escolha o stick da Nutricon | Petz'
        print(f'Valida o titulo da aba!')

        self.driver.find_element(By.CSS_SELECTOR, 'button#adicionarAoCarrinho.btn.btn-add-to-cart').click()
        print(f'Produto no Carrinho!')


        # Cart Page
        assert self.driver.find_element(By.CSS_SELECTOR, 'div.product-title').text == nome_produto
        print(f'Valida o nome do produto!')
        assert self.driver.find_element(By.CSS_SELECTOR, 'div.current-price-left').text == preco_produto
        print(f'Valida o preco do produto!')
