cat > password_check.py <<'PY'
import hashlib
import requests

def check_password(password: str) -> int:
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    for line in r.text.splitlines():
        h, count = line.split(":")
        if h == suffix:
            return int(count)
    return 0

if __name__ == "__main__":
    print("🔐 Comprobador de contraseñas comprometidas (HIBP, k-anonymity)")
    pwd = input("Introduce una contraseña para verificar: ")
    hits = check_password(pwd)
    if hits:
        print(f"⚠️ Aparece {hits:,} veces en filtraciones. ¡No la uses!")
    else:
        print("✅ No aparece en las listas conocidas. Aun así, usa una contraseña robusta y única.")
PY
