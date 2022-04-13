@Products
Feature: Consulta produtos no site da Petz

  Scenario Outline: Consultar Produtos
    Given que estou no site da Petz
    When busco pelo produto "<produto>"
    Then exibe os resultados como "<nome_produto>" e "<preco_produto>" e adiciono no carrinho
    Then exibe a pagina do carrinho com o "<nome_produto>" e "<preco_produto>"

    Examples:
      |      produto      |                                     nome_produto                                     | preco_produto |
      | Petisco Doguitos  |        Petisco Doguitos Rodízio para Cães Adultos e Filhotes Sabor Carne - 65g       |    R$ 7,55    |
      | Biscoito Dog Chow | Biscoito Dog Chow Extra Life para Cães Adultos de Raças Pequenas e Mini Sabor Frango |    R$ 20,50   |