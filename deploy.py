import os
import sys
import json
import webbrowser
import time
import requests
import random
import string

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    C = Fore.CYAN + Style.BRIGHT      # برای اطلاعات و هدرها
    G = Fore.GREEN + Style.BRIGHT     # برای موفقیت
    R = Fore.RED + Style.BRIGHT       # برای خطاها
    Y = Fore.YELLOW + Style.BRIGHT    # برای هشدارها
    M = Fore.MAGENTA + Style.BRIGHT   # برای نکات
    W = Fore.WHITE + Style.BRIGHT     # سفید روشن
    RES = Style.RESET_ALL             # ریست کردن رنگ
except ImportError:
    C = ""
    G = ""
    R = ""
    Y = ""
    M = ""
    W = ""
    RES = ""

def generate_random_suffix(length=8):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

def exit_app():
    input(f"\n{W}برای خروج دکمه Enter را بزنید...{RES}")
    sys.exit(1)

def main():
    print(f"{C}="*50)
    print(f"{C}*** Zeus Panel Auto-Deployer ***")
    print(f"{C}="*50)

    print(f"{C}[*] Downloading zeus.js from GitHub...{RES}")
    raw_url = "https://raw.githubusercontent.com/IR-NETLIFY/zeus/refs/heads/main/zeus.js"
    try:
        response = requests.get(raw_url, timeout=15)
        if response.status_code == 200:
            with open('zeus.js', 'wb') as f:
                f.write(response.content)
            print(f"{G}[OK] zeus.js downloaded successfully.{RES}")
        else:
            print(f"{R}[ERROR] Error downloading zeus.js: HTTP {response.status_code}{RES}")
            exit_app()
    except requests.exceptions.RequestException as e:
        print(f"{R}[ERROR] Network error while downloading zeus.js: {e}{RES}")
        exit_app()
    except Exception as e:
        print(f"{R}[ERROR] Failed to save zeus.js: {e}{RES}")
        exit_app()

    token_url = "https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=%5B%7B%22key%22%3A%22workers_scripts%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22workers_kv_storage%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22d1%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22account_settings%22%2C%22type%22%3A%22read%22%7D%2C%7B%22key%22%3A%22workers_subdomain%22%2C%22type%22%3A%22edit%22%7D%5D&accountId=*&zoneId=all&name=Zeus-Deployer-Token"
    
    print(f"\n{C}[*] Opening Cloudflare API Token page in your default browser...{RES}")
    try:
        webbrowser.open(token_url)
    except:
        pass
    
    time.sleep(1)
    print(f"{M}[*] Click 'Continue to summary' and 'Create Token' copy the token.{RES}")

    token = input(f"{W}[?] Please enter your Cloudflare API Token: {RES}\n").strip()
    if not token:
        print(f"{R}[ERROR] Token cannot be empty.{RES}")
        exit_app()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    print(f"\n{C}[*] Fetching Account ID...{RES}")
    try:
        res = requests.get("https://api.cloudflare.com/client/v4/accounts", headers=headers, timeout=15)
        if res.status_code != 200 or not res.json().get('success'):
            print(f"{R}[ERROR] Error fetching account: {res.text}{RES}")
            exit_app()
        
        accounts = res.json().get('result', [])
        if not accounts:
            print(f"{R}[ERROR] No Cloudflare accounts found for this token.{RES}")
            exit_app()
        
        account_id = accounts[0]['id']
        print(f"{G}[OK] Found Account ID: {account_id}{RES}")
    except requests.exceptions.RequestException as e:
        print(f"{R}[ERROR] Network error while fetching Account ID: {e}{RES}")
        exit_app()

    print(f"\n{C}[*] Checking workers.dev subdomain...{RES}")
    dev_sub = None
    try:
        subdomain_check_res = requests.get(f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/subdomain", headers=headers, timeout=15)
        
        if subdomain_check_res.status_code == 200 and subdomain_check_res.json().get('success'):
            dev_sub = subdomain_check_res.json()['result'].get('subdomain')
            if dev_sub:
                print(f"{G}[OK] Found existing subdomain: {dev_sub}.workers.dev{RES}")
            else:
                new_subdomain = f"zeus-{generate_random_suffix(6)}"
                print(f"{Y}[WARNING] No subdomain found. Creating a random one: {new_subdomain}.workers.dev ...{RES}")
                
                create_sub_res = requests.put(
                    f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/subdomain",
                    headers=headers,
                    json={"subdomain": new_subdomain},
                    timeout=15
                )
                
                if create_sub_res.status_code == 200 and create_sub_res.json().get('success'):
                    dev_sub = new_subdomain
                    print(f"{G}[OK] Subdomain '{dev_sub}.workers.dev' created successfully!{RES}")
                else:
                    print(f"\n{R}[ERROR] Failed to create subdomain automatically.{RES}")
                    print(f"{Y}[WARNING] IF THIS IS A BRAND NEW ACCOUNT, YOU MUST DO THE FOLLOWING:")
                    print("   1. Verify your Cloudflare account email address.")
                    print("   2. Go to the Cloudflare Dashboard -> 'Workers & Pages'.")
                    print(f"   3. Click 'Set up' to accept the Terms of Service.{RES}")
                    print(f"\n{R}API Error Details: {create_sub_res.text}{RES}")
                    exit_app()
        else:
            print(f"{R}[ERROR] Failed to check subdomain: {subdomain_check_res.text}{RES}")
            exit_app()
    except requests.exceptions.RequestException as e:
        print(f"{R}[ERROR] Network error while checking subdomain: {e}{RES}")
        exit_app()

    unique_suffix = generate_random_suffix()
    worker_name = f"zeus-panel-{unique_suffix}"
    db_name = f"zeus-db-{unique_suffix}"
    db_uuid = None
    
    print(f"\n{C}[*] Configuring D1 Database ('{db_name}')...{RES}")
    try:
        db_create_res = requests.post(
            f"https://api.cloudflare.com/client/v4/accounts/{account_id}/d1/database",
            headers=headers,
            json={"name": db_name},
            timeout=15
        )
        
        if db_create_res.status_code == 200 and db_create_res.json().get('success'):
            db_uuid = db_create_res.json()['result']['uuid']
            print(f"{G}[OK] Created new D1 Database. UUID: {db_uuid}{RES}")
        else:
            if "terms of service" in db_create_res.text.lower() or db_create_res.status_code in [400, 403]:
                 print(f"\n{R}[ERROR] Failed to create D1 Database due to account restrictions.{RES}")
                 print(f"{Y}[WARNING] Please visit your Cloudflare Dashboard -> 'D1' and accept the Terms of Service first.{RES}")
                 exit_app()
                 
            print(f"{Y}[WARNING] Database creation failed (might already exist). Searching...{RES}")
            db_list_res = requests.get(
                f"https://api.cloudflare.com/client/v4/accounts/{account_id}/d1/database",
                headers=headers,
                timeout=15
            )
            if db_list_res.status_code == 200:
                databases = db_list_res.json().get('result', [])
                for db in databases:
                    if db['name'] == db_name:
                        db_uuid = db['uuid']
                        print(f"{G}[OK] Found existing D1 Database. UUID: {db_uuid}{RES}")
                        break
        
        if not db_uuid:
            print(f"{R}[ERROR] Could not create or find the D1 database.{RES}")
            exit_app()
    except requests.exceptions.RequestException as e:
        print(f"{R}[ERROR] Network error while configuring database: {e}{RES}")
        exit_app()

    print(f"\n{C}[*] Deploying Worker ('{worker_name}')...{RES}")
    try:
        metadata = {
            "main_module": "zeus.js",
            "compatibility_date": "2024-02-08",
            "bindings": [
                {
                    "type": "d1",
                    "name": "DB",
                    "id": db_uuid
                }
            ]
        }

        with open('zeus.js', 'rb') as f:
            js_content = f.read()

        files = {
            'metadata': (None, json.dumps(metadata), 'application/json'),
            'zeus.js': ('zeus.js', js_content, 'application/javascript+module')
        }

        deploy_headers = {"Authorization": f"Bearer {token}"} 
        
        deploy_res = requests.put(
            f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts/{worker_name}",
            headers=deploy_headers,
            files=files,
            timeout=30
        )

        if deploy_res.status_code == 200 and deploy_res.json().get('success'):
            print(f"{G}[OK] Worker '{worker_name}' deployed successfully!{RES}")
        else:
            print(f"{R}[ERROR] Error deploying worker: {deploy_res.text}{RES}")
            exit_app()
    except Exception as e:
        print(f"{R}[ERROR] Error during deployment process: {e}{RES}")
        exit_app()

    print(f"\n{C}[*] Enabling workers.dev subdomain...{RES}")
    try:
        subdomain_res = requests.post(
            f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts/{worker_name}/subdomain",
            headers=headers,
            json={"enabled": True},
            timeout=15
        )

        if subdomain_res.status_code == 200 and subdomain_res.json().get('success'):
            print(f"{G}[OK] workers.dev route enabled!{RES}")
            
            final_url = f"https://{worker_name}.{dev_sub}.workers.dev"
            panel_url = f"{final_url}/panel"
            
            print(f"{G}="*50)
            print(f"{G}[SUCCESS] All Done! Your panel is live at:")
            print(f"{G} -> {W}{panel_url}{RES}")
            print(f"{G}="*50)
            
            try:
                time.sleep(2)
                webbrowser.open(panel_url)
            except Exception:
                pass
        else:
            print(f"{Y}[WARNING] Could not enable workers.dev automatically: {subdomain_res.text}{RES}")
            exit_app()
    except requests.exceptions.RequestException as e:
        print(f"{R}[ERROR] Network error while enabling subdomain: {e}{RES}")
        exit_app()

    print(f"\n{W}Press Enter to exit...{RES}")
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{R}[CANCELLED] Deployment cancelled by user.{RES}")
        input(f"\n{W}برای خروج دکمه Enter را بزنید...{RES}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{R}[CRITICAL ERROR] An unexpected error occurred: {e}{RES}")
        input(f"\n{W}برای خروج دکمه Enter را بزنید...{RES}")
        sys.exit(1)
