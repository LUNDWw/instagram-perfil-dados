import instaloader
import requests
import re

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

def coletar_dados_perfil_privado(username):
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

usuario_privado = input("Digite o nome de usuário do perfil privado: ")
coletar_dados_perfil_privado(usuario_privado)