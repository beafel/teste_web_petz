import time

from behave import given, when, then
from selenium import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from features import environment


def before_feature(context, feature):
    if 'Products' in feature.tag:
        context.execute_steps(
            # pode ser incluidas outras acoes
        )


@given(u'que estou no site da Petz')
def step_impl(context):
    context.driver.get('https://www.petz.com.br/')

    print(f'Acessou Petz')


@when(u'busco pelo produto "{produto}"')
def research_product(context, produto):
    context.driver.find_element(By.CSS_SELECTOR, 'button#aceiteLgpd.policy-button').click()
    context.driver.find_element(By.ID, 'search').click()
    context.driver.find_element(By.ID, 'search').send_keys(produto)
    context.driver.find_element(By.ID, 'search').send_keys(Keys.ENTER)

    print(f'Buscou por {produto}')
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//body/div[9]/div[2]/categoryid[1]/div[2]/div[2]/div[3]/ul[1]/li[1]/a[2]/h3[1]').click()

    print(f'Selecionou o {produto}')
    time.sleep(2)


@then(u'exibe os resultados como "{nome_produto}" e "{preco_produto}" e adiciono no carrinho')
def validate_product(context, nome_produto, preco_produto):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.product-title').text == nome_produto
    print(f'Validou {nome_produto}')

    assert context.driver.find_element(By.CSS_SELECTOR, 'div.product-top-price').text == preco_produto
    print(f'Validou {preco_produto}')

    context.driver.find_element(By.ID, 'adicionarAoCarrinho').click()
    print(f'Adicionou no carrinho')

    time.sleep(2)

@then(u'exibe a pagina do carrinho com o "{nome_produto}" e "{preco_produto}"')
def validate_add_cart(context, nome_produto, preco_produto):
    assert context.driver.title == 'Carrinho | Petz'
    print(f'Validou a aba - Carrinho')

    # context.driver.find_element(By.CSS_SELECTOR, 'a.button.tx-green.m-t-08.fn-s09.is-large.bg-transparent.outlined').click()

    assert context.driver.find_element(By.XPATH, '//div[2]/div/div[2]/div[2]').text == nome_produto
    print(f'Validou {nome_produto} no carrinho')

    assert context.driver.find_element(By.XPATH, '//div[2]/div[2]/div/div[3]').text == preco_produto
    print(f'Validou {preco_produto} no carrinho')
