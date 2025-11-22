# app.py
# ============================================
# Demo file for Secret Scanning Lab with Gitleaks
# ============================================
# ⚠️ ATTENTION :
# Ce fichier contient volontairement un FAUX secret
# pour un exercice pédagogique. NE JAMAIS faire ça
# dans un vrai projet en production.

import time

def connect_to_aws_demo():
    """
    Fake function to simulate a connection to an AWS service
    using a hardcoded access key and secret key.
    This is ONLY for teaching secret scanning.
    """

    # ❌ Mauvaise pratique VOLONTAIRE pour le lab :
    # Fausse clé d'accès AWS (pattern classique AKIA...)
    aws_access_key_id = "AKIA1234567890FAKEKEYDEMO"
    aws_secret_access_key = "wJalrXUtnFEMI_K7MDENG_bPxRfiCYFAKESECRETKEY123"

    print("=== AWS Demo Connection ===")
    print("Using hardcoded AWS credentials (DEMO ONLY)")
    print(f"AWS_ACCESS_KEY_ID: {aws_access_key_id}")
    print(f"AWS_SECRET_ACCESS_KEY: {aws_secret_access_key}")
    print("Simulating connection to AWS S3 demo bucket...")
    time.sleep(1)
    print("✅ Demo connection finished (no real call done).")

def main():
    print("Starting Secret Scanning demo app...")
    connect_to_aws_demo()
    print("End of demo. Now run Gitleaks in your CI pipeline to detect the secret!")

if __name__ == "__main__":
    main()
