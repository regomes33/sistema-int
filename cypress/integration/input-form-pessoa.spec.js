let name = ['Aarão', 'Benedito', 'Paula', 'Silvia', 'Miranda']
let rand_cpf
let rand_rg
let rand_cnh
let rand_cep = Math.floor(Math.random() * 1000000)
let rand_phone
let rand_number = Math.floor(Math.random() * 10000)

describe('Input form', () => {
  it('focuses input on load', () => {
    cy.visit('http://localhost:8000/')

    cy.get('input[name="username"]').type('regis')
    cy.get('input[name="password"]').type('d')
    cy.wait(500)
    cy.get('button[type="submit"]').click()

    cy.wait(500)
    cy.get('a[href="/pessoa/"]').click()
    cy.wait(1000)
    cy.get('#btnAdicionar').click()
    cy.wait(500)

    var rand_name = name[Math.floor(Math.random() * name.length)]
    cy.get('input[name="nome"]').type(rand_name)
    cy.get('input[name="sobrenome"]').type('Santos')
    cy.get('input[name="apelido"]').type('Cidão')
    cy.get('input[name="mae"]').type('Ivonete Santos')
    cy.get('input[name="pai"]').type('Benedito Santos')
    cy.get('#faccao').select('1')
    cy.get('input[name="nascimento"]').type('2020-06-12')
    cy.get("#id_observacao").type('Lorem ipsum dollor amet.')
    cy.wait(500)

    cy.get('#heading2').click()
    rand_cpf = Math.floor(Math.random() * 99999999999)
    cy.get('#id_cpf').type(rand_cpf)
    rand_rg = Math.floor(Math.random() * 99999999999)
    cy.get('#id_rg').type(rand_rg)
    rand_cnh = Math.floor(Math.random() * 1000000)
    cy.get('#id_cnh').type(rand_cnh)
    cy.wait(500)

    cy.get('#heading3').click()
    cy.get('#id_address').type('Rua da Glória')
    cy.get('#id_address_number').type(rand_number)
    cy.get('#id_complement').type('4º andar')
    cy.get('#id_district').select('1')
    cy.get('#id_cep').type(rand_cep)
    cy.wait(500)

    cy.get('#heading6').click()
    cy.get('#natureza1').select('1')
    cy.get('#qualificacao1').select('aut')
    cy.get('#arma1').select('1')
    cy.get('#status1').select('foragido')
    cy.get('#btnInfracao').click()
    cy.get('#natureza2').select('2')
    cy.get('#qualificacao2').select('aut')
    cy.get('#arma2').select('2')
    cy.get('#status2').select('morto')
    cy.get('#btnInfracao').click()
    cy.get('#natureza3').select('3')
    cy.get('#qualificacao3').select('coaut')
    cy.get('#arma3').select('3')
    cy.get('#status3').select('solto')
    cy.wait(500)

    cy.get('#heading7').click()
    cy.get('#ocorrencia1').select('1')
    cy.get('#btnOcorrencia').click()
    cy.get('#ocorrencia2').select('2')
    cy.wait(500)

    cy.get('#heading8').click()
    cy.get('#tipo1').select('cel')
    rand_phone = Math.floor(Math.random() * 10000000000)
    cy.get('#telefone1').type('(62) ' + rand_phone)
    cy.get('#btnContato').click()
    cy.get('#tipo2').select('cel')
    rand_phone = Math.floor(Math.random() * 10000000000)
    cy.get('#telefone2').type('(62) ' + rand_phone)
    cy.wait(500)

    cy.get('#heading9').click()
    cy.get('#comparsa_nome1').select('1')
    rand_cpf = Math.floor(Math.random() * 999999999999)
    cy.get('#comparsa_grau_parentesco1').type('Irmão')
    cy.get('#comparsa_observacao1').type('Cúmplice')
    cy.get('#btnComparsa').click()
    cy.get('#comparsa_nome2').select('2')
    rand_cpf = Math.floor(Math.random() * 999999999999)
    cy.get('#comparsa_grau_parentesco2').type('Primo')
    cy.get('#comparsa_observacao2').type('Disse que é inocente.')

    cy.get('#heading10').click()
    cy.get('#veiculo1').select('1')
    cy.get('#btnVeiculo').click()
    cy.get('#veiculo2').select('2')

    cy.get('button[type="submit"]').click()
  })
})
