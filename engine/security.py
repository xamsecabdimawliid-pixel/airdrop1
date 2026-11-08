import re
from urllib.parse import urlparse

SUSPICIOUS_WORDS = [
    "drainer",
    "wallet-steal",
    "seed-phrase",
    "privatekey",
    "claim-free-token-now"
]

def check_url(url):
    try:
        parsed = urlparse(url)

        if parsed.scheme != "https":
            return False, "HTTPS ma jiro"

        if not parsed.hostname:
            return False, "Domain maqan"

        domain = parsed.hostname.lower()

        if domain.startswith("xn--"):
            return False, "Punycode domain"

        if re.match(r"^\d+\.\d+\.\d+\.\d+$", domain):
            return False, "IP address halkii domain"

        if any(word in url.lower() for word in SUSPICIOUS_WORDS):
            return False, "URL laga shakiyey"

        return True, "Basic URL checks passed"

    except Exception:
        return False, "URL invalid"


def calculate_security_score(
    official_source,
    domain_verified,
    no_seed_request,
    no_unlimited_approval,
    contract_verified
):
    checks = [
        (official_source, 20),
        (domain_verified, 20),
        (no_seed_request, 20),
        (no_unlimited_approval, 20),
        (contract_verified, 20)
    ]

    score = sum(
        points for passed, points in checks if passed is True
    )

    return score
