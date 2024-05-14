from colorama import Fore, Style, init
import requests
import getpass

# colorama'yı başlat (otomatik olarak renkleri sıfırlar)
init(autoreset=True)

def print_success(message):
    print(Fore.GREEN + message)

def print_error(message):
    print(Fore.RED + message)

def print_info(message):
    print(Fore.CYAN + message)

# API'ye login işlemi
def login(email, password):
    url = "https://aigency.dev/api/v1/login/"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"email": email, "password": password}
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"] if response.status_code == 200 else None

# AI ekibini listeleme
def ai_team_list(access_token):
    url = f"https://aigency.dev/api/v1/ai-team-list/?access_token={access_token}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Yeni chat başlatma
def new_chat(access_token, ai_id):
    url = "https://aigency.dev/api/v1/newChat"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"access_token": access_token, "ai_id": ai_id}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        chat_data = response.json()
        # chat_data içinden ai_name bilgisini de çekiyoruz
        return chat_data, chat_data.get("ai_name", "Unknown AI")
    else:
        return None, "Unknown AI"

# Chat'e devam etme
def resume_chat(access_token, chat_id):
    url = "https://aigency.dev/api/v1/resumeChat"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"access_token": access_token, "chat_id": chat_id}
    response = requests.post(url, headers=headers, data=data)
    return response.json() if response.status_code == 200 else None

# Chat'i sıfırlama
def reset_chat(access_token, chat_id):
    url = "https://aigency.dev/api/v1/resetChat"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"access_token": access_token, "chat_id": chat_id}
    response = requests.post(url, headers=headers, data=data)
    return response.json() if response.status_code == 200 else None

# Mesaj gönderme ve yanıtlama
def send_message(access_token, chat_id, message):
    url = "https://aigency.dev/api/v1/sendMessage"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"access_token": access_token, "chat_id": chat_id, "message": message}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        response_data = response.json()
        # Yanıttan yalnızca gerekli "message" bölümünü alıyoruz
        ai_response = response_data.get("answer", {}).get("message", "Yanıt alınamadı.")
        return ai_response
    else:
        return f"Hata: {response.status_code} - {response.text}"

def chat_session(access_token, chat_id, ai_name):
    while True:
        user_input = input("Mesajınız: ")
        if user_input.startswith("/"):
            if user_input == "/exit":
                print("Sohbet sonlandırılıyor.")
                break
            elif user_input == "/reset":
                print("Sohbet sıfırlandı:", reset_chat(access_token, chat_id))
                continue
            elif user_input == "/newchat":
                ai_id = input("Yeni AI ID'yi girin: ")
                new_chat_data, ai_name = new_chat(access_token, ai_id)
                if new_chat_data:
                    print("Yeni sohbet başladı:", ai_name)
                    chat_id = new_chat_data.get("chat_id", chat_id)
                continue
        else:
            response = send_message(access_token, chat_id, user_input)
            print(f"{ai_name}:", response)

def main():
    email = input("E-posta adresinizi girin: ")
    password = getpass.getpass("Şifrenizi girin: ")
    token = login(email, password)
    if token:
        print_success("Giriş başarılı.")
        team = ai_team_list(token)
        if team:
            print_info("Ekibimiz:")
            for member in team:
                print(f"{Fore.YELLOW}{member['ai_id']}: {Fore.LIGHTBLUE_EX}{member['ai_name']}")
            ai_id = input("Başlamak istediğiniz AI ID'yi girin: ")
            chat_data, ai_name = new_chat(token, ai_id)
            if chat_data:
                print_success(f"Mesajlaşma başlıyor... {ai_name} ile sohbet ediyorsunuz.")
                chat_session(token, chat_data["chat_id"], ai_name)
    else:
        print_error("Giriş başarısız.")
