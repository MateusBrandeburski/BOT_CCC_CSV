from selenium import webdriver as driver_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from openpyxl import load_workbook
import time
import csv

def programa_ccc():

    #Acha, abre e seleciona a aba do arquivo xlsx
    caminho_arquivo = '/home/mateus/Projetos/BOT_CCC/Consulta_CCC.xlsx'
    arquivos_dados = load_workbook(caminho_arquivo)
    sheet_exporta_Dados = arquivos_dados['CNPJ_Consulta_CCC']

    #instruções Selenium
    options = Options()
    options.add_argument("user-data-dir=C:\\Users\\mateus\\AppData\\Local\\Google\\Chrome\\User Data\\Profile CCC")
    browser = driver_browser.Chrome(options=options)
    browser.maximize_window()
    
   
    def valida_cnpj():

        nao_localizado = browser.find_element(By.XPATH, '//*[@id="bodyPricipal"]/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]').text
        if nao_localizado == 'Contribuinte não localizado no Cadastro Centralizado de Contribuintes.':

            cnpj = cnpj_pesquisa
            uf = uf_pesquisa
            msg_erro = '(CCC NÃO LOCALIZADO!, PODER SER O UF DIGITADA ERRAD0!)'

            # Envia a msg para primeira aba do arquivo xlsx
            aba_importa_dados = arquivos_dados['Dados_Extraidos_CCC']
            linhaCorrenteAba_Encapsulamento = len(aba_importa_dados['A']) + 1

            colunaA = 'A' + str(linhaCorrenteAba_Encapsulamento)
            colunaB = 'B' + str(linhaCorrenteAba_Encapsulamento)
            colunaC = 'C' + str(linhaCorrenteAba_Encapsulamento)

            aba_importa_dados[colunaA] = msg_erro
            aba_importa_dados[colunaB] = uf
            aba_importa_dados[colunaC] = cnpj

            arquivos_dados.save(filename=caminho_arquivo)

        else:
            pass

    def cnpj_com_uma_inscricao():

        time.sleep(2)
        try:
            #Raspagem de dados.
            nome_empresa = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[1]/div[2]').text
            uf_com_numero = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[2]/div[2]').text
            situacao_cnpj = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[3]/div[4]').text
            inscricao_Estadual = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[4]/div[2]').text
            situacao_IE = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[4]/div[4]').text
            tipoIE = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[5]/div[2]').text
            cnae_principal = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[5]/div[4]').text
            dataDaSituacao_uf = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[6]/div[2]').text
            nome_fantasia = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[1]/div[2]').text
            dataInicioAtividade = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[2]/div[2]').text
            dataFimAtividade = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[2]/div[4]').text
            regime_tributacao = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[3]/div[2]').text
            informacaoDaIEComoDestinatario = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[4]/div[2]').text
            porteDaEmpresa = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[5]/div[2]').text
            cnae_principal2 = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[6]/div[2]').text
            credito_presumido = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[7]/div[2]').text
            tipo_produtor = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[8]/div[2]').text
            municipio_IBGE = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[1]/div[2]').text
            ufDeLocalizacao = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[1]/div[4]').text
            logradouro = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[2]/div[2]').text
            numero = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[2]/div[4]').text
            complemento = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[3]/div[2]').text
            cep = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[4]/div[2]').text
            bairro = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[3]/div[4]').text

            #Encapsulamento dos dados raspados.
            aba_importa_dados = arquivos_dados['Dados_Extraidos_CCC']
            linhaCorrenteAba_Encapsulamento = len(aba_importa_dados['A']) + 1

            colunaA = 'A' + str(linhaCorrenteAba_Encapsulamento)
            colunaB = 'B' + str(linhaCorrenteAba_Encapsulamento)
            colunaC = 'C' + str(linhaCorrenteAba_Encapsulamento)
            colunaD = 'D' + str(linhaCorrenteAba_Encapsulamento)
            colunaE = 'E' + str(linhaCorrenteAba_Encapsulamento)
            colunaF = 'F' + str(linhaCorrenteAba_Encapsulamento)
            colunaG = 'G' + str(linhaCorrenteAba_Encapsulamento)
            colunaH = 'H' + str(linhaCorrenteAba_Encapsulamento)
            colunaI = 'I' + str(linhaCorrenteAba_Encapsulamento)
            colunaJ = 'J' + str(linhaCorrenteAba_Encapsulamento)
            colunaK = 'K' + str(linhaCorrenteAba_Encapsulamento)
            colunaL = 'L' + str(linhaCorrenteAba_Encapsulamento)
            colunaM = 'M' + str(linhaCorrenteAba_Encapsulamento)
            colunaN = 'N' + str(linhaCorrenteAba_Encapsulamento)
            colunaO = 'O' + str(linhaCorrenteAba_Encapsulamento)
            colunaP = 'P' + str(linhaCorrenteAba_Encapsulamento)
            colunaQ = 'Q' + str(linhaCorrenteAba_Encapsulamento)
            colunaR = 'R' + str(linhaCorrenteAba_Encapsulamento)
            colunaS = 'S' + str(linhaCorrenteAba_Encapsulamento)
            colunaT = 'T' + str(linhaCorrenteAba_Encapsulamento)
            colunaU = 'U' + str(linhaCorrenteAba_Encapsulamento)
            colunaV = 'V' + str(linhaCorrenteAba_Encapsulamento)
            colunaW = 'W' + str(linhaCorrenteAba_Encapsulamento)
            colunaX = 'X' + str(linhaCorrenteAba_Encapsulamento)
            colunaY = 'Y' + str(linhaCorrenteAba_Encapsulamento)


            aba_importa_dados[colunaA] = nome_empresa
            aba_importa_dados[colunaB] = uf_com_numero
            aba_importa_dados[colunaC] = cnpj_pesquisa
            aba_importa_dados[colunaD] = situacao_cnpj
            aba_importa_dados[colunaE] = inscricao_Estadual
            aba_importa_dados[colunaF] = situacao_IE
            aba_importa_dados[colunaG] = tipoIE
            aba_importa_dados[colunaH] = cnae_principal
            aba_importa_dados[colunaI] = dataDaSituacao_uf
            aba_importa_dados[colunaJ] = nome_fantasia
            aba_importa_dados[colunaK] = dataInicioAtividade
            aba_importa_dados[colunaL] = dataFimAtividade
            aba_importa_dados[colunaM] = regime_tributacao
            aba_importa_dados[colunaN] = informacaoDaIEComoDestinatario
            aba_importa_dados[colunaO] = porteDaEmpresa
            aba_importa_dados[colunaP] = cnae_principal2
            aba_importa_dados[colunaQ] = credito_presumido
            aba_importa_dados[colunaR] = tipo_produtor
            aba_importa_dados[colunaS] = municipio_IBGE
            aba_importa_dados[colunaT] = ufDeLocalizacao
            aba_importa_dados[colunaU] = logradouro
            aba_importa_dados[colunaV] = numero
            aba_importa_dados[colunaW] = complemento
            aba_importa_dados[colunaX] = cep
            aba_importa_dados[colunaY] = bairro

            arquivos_dados.save(filename=caminho_arquivo)
            #importante - retorno para a próxima função dar falso e passar....
            browser.get('https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc')
        except:
            pass

    def cnpj_com_duasOuMais_inscricoes():

        try:
            elementoTabela = browser.find_element(By.XPATH, '//*[@id="ListaContribuintes"]')
            
            linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
            colunas = elementoTabela.find_elements(By.TAG_NAME, "td")
          
            
            for colunasAtual in linhas:
                                
                
                #instrução que procura dentro da coluna se existe o link com CNPJ clicável.
                try:
                    colunasAtual.find_element(By.LINK_TEXT, cnpj_pesquisa).click()

                    time.sleep(3)
                    #raspagem de dados
                    try:
                        nome_empresa = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[1]/div[2]').text
                    except:
                        nome_empresa = ''

                    try:
                        uf_com_numero = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[2]/div[2]').text
                    except:
                        uf_com_numero = ''

                    try:
                        situacao_cnpj = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[3]/div[4]').text
                    except:
                        situacao_cnpj = ''

                    try:
                        inscricao_Estadual = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[4]/div[2]').text
                    except:
                        inscricao_Estadual = ''

                    try:
                        situacao_IE = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[4]/div[4]').text
                    except:
                        situacao_IE = ''

                    try:
                        tipoIE = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[5]/div[2]').text
                    except:
                        tipoIE = ''

                    try:
                        cnae_principal = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[5]/div[4]').text
                    except:
                        cnae_principal = ''

                    try:
                        dataDaSituacao_uf = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[1]/div[2]/div[6]/div[2]').text
                    except:
                        dataDaSituacao_uf = ''

                    try:
                        nome_fantasia = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[1]/div[2]').text
                    except:
                        nome_fantasia = ''

                    try:
                        dataInicioAtividade = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[2]/div[2]').text
                    except:
                        dataInicioAtividade = ''

                    try:
                        dataFimAtividade = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[2]/div[4]').text
                    except:
                        dataFimAtividade = ''

                    try:
                        regime_tributacao = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[3]/div[2]').text
                    except:
                        regime_tributacao = ''

                    try:
                        informacaoDaIEComoDestinatario = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[4]/div[2]').text
                    except:
                        informacaoDaIEComoDestinatario = ''

                    try:
                        porteDaEmpresa = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[5]/div[2]').text
                    except:
                        porteDaEmpresa = ''

                    try:
                        cnae_principal2 = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[6]/div[2]').text
                    except:
                        cnae_principal2 = ''

                    try:
                        credito_presumido = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[7]/div[2]').text
                    except:
                        credito_presumido = ''

                    try:
                        tipo_produtor = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[2]/div[2]/div[8]/div[2]').text
                    except:
                        tipo_produtor = ''

                    try:
                        municipio_IBGE = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[1]/div[2]').text
                    except:
                        municipio_IBGE = ''

                    try:
                        ufDeLocalizacao = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[1]/div[4]').text
                    except:
                        ufDeLocalizacao = ''

                    try:
                        logradouro = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[2]/div[2]').text
                    except:
                        logradouro = ''

                    try:
                        numero = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[2]/div[4]').text
                    except:
                        numero = ''

                    try:
                        complemento = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[3]/div[2]').text
                    except:
                        complemento = ''

                    try:
                        cep = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[4]/div[2]').text
                    except:
                        cep = ''

                    try:
                        bairro = browser.find_element(By.XPATH, '//*[@id="tabContribuinte"]/div[3]/div[2]/div[3]/div[4]').text
                    except:
                        bairro = ''


                    # Encapsulamento dos dados raspados.
                    aba_importa_dados = arquivos_dados['Dados_Extraidos_CCC']
                    linhaCorrenteAba_Encapsulamento = len(aba_importa_dados['A']) + 1

                    colunaA = 'A' + str(linhaCorrenteAba_Encapsulamento)
                    colunaB = 'B' + str(linhaCorrenteAba_Encapsulamento)
                    colunaC = 'C' + str(linhaCorrenteAba_Encapsulamento)
                    colunaD = 'D' + str(linhaCorrenteAba_Encapsulamento)
                    colunaE = 'E' + str(linhaCorrenteAba_Encapsulamento)
                    colunaF = 'F' + str(linhaCorrenteAba_Encapsulamento)
                    colunaG = 'G' + str(linhaCorrenteAba_Encapsulamento)
                    colunaH = 'H' + str(linhaCorrenteAba_Encapsulamento)
                    colunaI = 'I' + str(linhaCorrenteAba_Encapsulamento)
                    colunaJ = 'J' + str(linhaCorrenteAba_Encapsulamento)
                    colunaK = 'K' + str(linhaCorrenteAba_Encapsulamento)
                    colunaL = 'L' + str(linhaCorrenteAba_Encapsulamento)
                    colunaM = 'M' + str(linhaCorrenteAba_Encapsulamento)
                    colunaN = 'N' + str(linhaCorrenteAba_Encapsulamento)
                    colunaO = 'O' + str(linhaCorrenteAba_Encapsulamento)
                    colunaP = 'P' + str(linhaCorrenteAba_Encapsulamento)
                    colunaQ = 'Q' + str(linhaCorrenteAba_Encapsulamento)
                    colunaR = 'R' + str(linhaCorrenteAba_Encapsulamento)
                    colunaS = 'S' + str(linhaCorrenteAba_Encapsulamento)
                    colunaT = 'T' + str(linhaCorrenteAba_Encapsulamento)
                    colunaU = 'U' + str(linhaCorrenteAba_Encapsulamento)
                    colunaV = 'V' + str(linhaCorrenteAba_Encapsulamento)
                    colunaW = 'W' + str(linhaCorrenteAba_Encapsulamento)
                    colunaX = 'X' + str(linhaCorrenteAba_Encapsulamento)
                    colunaY = 'Y' + str(linhaCorrenteAba_Encapsulamento)

                    aba_importa_dados[colunaA] = nome_empresa
                    aba_importa_dados[colunaB] = uf_com_numero
                    aba_importa_dados[colunaC] = cnpj_pesquisa
                    aba_importa_dados[colunaD] = situacao_cnpj
                    aba_importa_dados[colunaE] = inscricao_Estadual
                    aba_importa_dados[colunaF] = situacao_IE
                    aba_importa_dados[colunaG] = tipoIE
                    aba_importa_dados[colunaH] = cnae_principal
                    aba_importa_dados[colunaI] = dataDaSituacao_uf
                    aba_importa_dados[colunaJ] = nome_fantasia
                    aba_importa_dados[colunaK] = dataInicioAtividade
                    aba_importa_dados[colunaL] = dataFimAtividade
                    aba_importa_dados[colunaM] = regime_tributacao
                    aba_importa_dados[colunaN] = informacaoDaIEComoDestinatario
                    aba_importa_dados[colunaO] = porteDaEmpresa
                    aba_importa_dados[colunaP] = cnae_principal2
                    aba_importa_dados[colunaQ] = credito_presumido
                    aba_importa_dados[colunaR] = tipo_produtor
                    aba_importa_dados[colunaS] = municipio_IBGE
                    aba_importa_dados[colunaT] = ufDeLocalizacao
                    aba_importa_dados[colunaU] = logradouro
                    aba_importa_dados[colunaV] = numero
                    aba_importa_dados[colunaW] = complemento
                    aba_importa_dados[colunaX] = cep
                    aba_importa_dados[colunaY] = bairro

                    arquivos_dados.save(filename=caminho_arquivo)
                except:
                    pass
        except:
            pass

    with open('csv_teste1.csv', mode='r') as arq:
        leitor = csv.reader(arq, delimiter=',')
        for coluna in leitor:
        
            browser.get('https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc')
            #tempo para resolução do captcha
            time.sleep(57)
            
            # #VÁRIAVEL DE ARMAZENAMENTO CNPJ
            cnpj_pesquisa = coluna[0]
            browser.find_element(By.XPATH, '//*[@id="CodInscrMf"]').send_keys(cnpj_pesquisa)


            #VÁRIAVEL DE ARMAZENAMENTO UF
            uf_pesquisa = coluna[1]
            print(cnpj_pesquisa, uf_pesquisa)
            
            if uf_pesquisa == 'AC':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="12"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'AL':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="27"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'AM':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="13"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'AP':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="16"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'BA':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="29"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'CE':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="23"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()

                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'DF':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="53"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'ES':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="32"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'GO':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="52"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'MA':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="21"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'MG':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="31"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'MS':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="50"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'MT':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="51"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'PA':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="15"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'PB':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="25"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'PE':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="26"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'PI':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="22"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'RJ':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="33"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'RN':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="24"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'RO':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="11"]').click()
                    browser.implicitly_wait(2)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'RR':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="14"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'RS':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="43"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'SC':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="42"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'SE':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="28"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'SP':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="35"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'PR':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="41"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

            elif uf_pesquisa == 'TO':
                try:
                    browser.find_element(By.NAME, 'CodUf').click()
                    browser.find_element(By.XPATH, '//option[@value="17"]').click()
                    time.sleep(1)
                    browser.find_element(By.XPATH, '//*[@id="BtnPesquisarCodInscrMf"]').click()
                except:
                    continue
                time.sleep(2)

                valida_cnpj()
                cnpj_com_uma_inscricao()
                cnpj_com_duasOuMais_inscricoes()

        browser.close()

programa_ccc()
