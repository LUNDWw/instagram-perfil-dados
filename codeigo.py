import instaloader
import requests
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

loader = instaloader.Instaloader()

def validar_links(links):
    print("\nValidando links encontrados...")
    for link in links:
        try:
            response = requests.head(link, timeout=5)
            if response.status_code == 200:
                print(f"Link válido: {link}")
            else:
                print(f"Link inválido ou inacessível ({response.status_code}): {link}")
        except requests.RequestException as e:
            print(f"Erro ao validar o link {link}: {e}")

def coletar_dados_perfil_privado_instaloader(username):
    try:
        perfil = instaloader.Profile.from_username(loader.context, username)

        print(f"Nome: {perfil.full_name}")
        print(f"Biografia: {perfil.biography}")
        print(f"Número de seguidores: {perfil.followers}")
        print(f"Número de perfis seguidos: {perfil.followees}")
        print(f"Número de posts: {perfil.mediacount}")

        if not perfil.biography:
            print("A biografia está vazia.")
            return

        links = re.findall(r'(https?://\S+|www\.\S+|\S+\.\S+)', perfil.biography)
        if links:
            print("Links encontrados na biografia:")
            for link in links:
                print(link)
            validar_links(links)
        else:
            print("Nenhum link encontrado na biografia.")
    except instaloader.exceptions.ProfileNotExistsException:
        print("Erro: O perfil não existe.")
    except Exception as e:
        print(f"Erro ao coletar dados do perfil: {e}")

def coletar_dados_perfil_privado_selenium(username):
    # Caminho para o Brave
    CAMINHO_BRAVE = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

    options = webdriver.ChromeOptions()
    options.binary_location = CAMINHO_BRAVE
    options.add_argument('--headless')  # opcional: roda sem abrir janela
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    # Usa webdriver_manager para baixar o ChromeDriver automaticamente
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        url = f"https://www.instagram.com/{username}/"
        driver.get(url)
        time.sleep(5)

        print(f"\n🔎 Acessando perfil: {url}")

        try:
            bio_element = driver.find_element(By.XPATH, "//div[contains(@class, '_aa_c')]")
            bio_text = bio_element.text.strip()
            print(f"\n📝 Biografia completa:\n{bio_text}")
        except:
            bio_text = ""
            print("\n📝 Biografia não encontrada.")

        links = re.findall(r"(https?://\S+|www\.\S+|\S+\.\S+)", bio_text)
        if links:
            print("\n🔗 Links encontrados:")
            for link in links:
                print(f"- {link}")

        stats = driver.find_elements(By.XPATH, "//ul[contains(@class,'_ac2a')]/li")
        if len(stats) >= 3:
            posts = stats[0].text
            seguidores = stats[1].text
            seguindo = stats[2].text

            print(f"\n📊 Estatísticas:")
            print(f"- Publicações: {posts}")
            print(f"- Seguidores: {seguidores}")
            print(f"- Seguindo: {seguindo}")
        else:
            print("\n❌ Não foi possível coletar as estatísticas.")

    except Exception as e:
        print(f"\n❗ Erro ao acessar o perfil: {e}")
    finally:
        driver.quit()

# ===== Execução =====

usuario = input("Digite o nome de usuário do Instagram: ")
metodo = input("Escolha o método (1 para Instaloader, 2 para Selenium): ")

if metodo == "1":
    coletar_dados_perfil_privado_instaloader(usuario)
elif metodo == "2":
    coletar_dados_perfil_privado_selenium(usuario)
else:
    print("Método inválido.")
