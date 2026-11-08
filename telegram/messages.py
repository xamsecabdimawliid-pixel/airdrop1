def format_airdrop(item):
    grade = item["grade"]
    score = item["security_score"]

    return f"""
🚀 SAIB AIRDROP ALERT

🪙 Mashruuca: {item['name']}

🏆 Grade: {grade}

🛡️ Security Score: {score}/100

🌐 Network: {item.get('network', 'Unknown')}

💰 Qiimaha ka qaybgalka: FREE
⛽ Gas Fee: Lama xaqiijin
📥 Deposit: Lama xaqiijin

📝 Sharaxaad:
{item.get('description', 'Faahfaahin dheeraad ah lama hayo.')}

📋 Sida loo bilaabo:
1. Akhri shuruudaha rasmiga ah.
2. Hubi network-ka.
3. Adeegso wallet-kaaga Airdrop-ka.
4. Ha saxiixin wax aadan fahmin.

💵 Lacag samaynta:
Token-ka marka la qaybiyo, hubi listing-kiisa
iyo liquidity-giisa ka hor iibinta.

⚠️ SAIB: Baaritaan hordhac ah.
Ma jiro dammaanad amni ama faa'iido.

🌐 Website:
{item['url']}
"""
