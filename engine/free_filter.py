def check_free_airdrop(item):
    """
    Kaliya aqbal hawlo la xaqiijiyey inay bilaash yihiin.
    Unknown requirements lama aqbalayo.
    """

    requirements = [
        item.get("gas_required"),
        item.get("deposit_required"),
        item.get("investment_required"),
        item.get("paid_subscription_required")
    ]

    if any(value is True for value in requirements):
        return False

    # Xog aan la xaqiijin lama aqbalayo.
    if any(value is None for value in requirements):
        return False

    if item.get("free_verified") is not True:
        return False

    if item.get("exchange_kyc_required") is True:
        return False

    return True
