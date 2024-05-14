import getpass
from aigency_api.core import login, print_success, print_error, print_info, ai_team_list, new_chat, chat_session

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
                print(f"{member['ai_id']}: {member['ai_name']}")
            ai_id = input("Başlamak istediğiniz AI ID'yi girin: ")
            chat_data, ai_name = new_chat(token, ai_id)
            if chat_data:
                print_success(f"Mesajlaşma başlıyor... {ai_name} ile sohbet ediyorsunuz.")
                chat_session(token, chat_data["chat_id"], ai_name)
    else:
        print_error("Giriş başarısız.")

if __name__ == "__main__":
    main()
