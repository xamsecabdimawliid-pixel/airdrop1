export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Hubinta in Worker-ku shaqaynayo
    if (url.pathname === "/" && request.method === "GET") {
      return new Response("SAIB Worker is online!");
    }

    // Telegram webhook setup
    if (url.pathname === "/setup" && request.method === "GET") {
      if (!env.SETUP_SECRET || url.searchParams.get("key") !== env.SETUP_SECRET) {
        return new Response("Unauthorized", { status: 401 });
      }

      if (!env.TELEGRAM_BOT_TOKEN || !env.WEBHOOK_SECRET) {
        return new Response("Missing Telegram secrets", { status: 500 });
      }

      const webhookUrl = ${url.origin}/telegram;

      const result = await fetch(
        https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/setWebhook,
        {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify({
            url: webhookUrl,
            secret_token: env.WEBHOOK_SECRET
          })
        }
      );

      return new Response(await result.text(), {
        headers: { "content-type": "application/json" }
      });
    }

    // Telegram messages
    if (url.pathname === "/telegram" && request.method === "POST") {
      if (!env.TELEGRAM_BOT_TOKEN || !env.WEBHOOK_SECRET) {
        return new Response("Missing secrets", { status: 500 });
      }

      const secret = request.headers.get(
        "X-Telegram-Bot-Api-Secret-Token"
      );

      if (secret !== env.WEBHOOK_SECRET) {
        return new Response("Unauthorized", { status: 401 });
      }

      const update = await request.json();
      const message = update.message;

      if (message && message.chat && message.text) {
        const chatId = message.chat.id;
        const text = message.text.trim();

        let reply;

        if (text === "/start" || text.startsWith("/start ")) {
          reply =
            "👋 Ku soo dhawoow SAIB!\n\n" +
            "Somali Airdrop Intelligence Bot\n\n" +
            "Waxaan kuu diyaarinaynaa xogta airdrops-ka bilaashka ah.\n\n" +
            "Amnigaaga ilaali: waligaa ha dirin seed phrase ama private key.\n\n" +
            "Adeegso /help si aad u aragto amarrada.";
        } else if (text === "/help") {
          reply =
            "🤖 SAIB Commands\n\n" +
            "/start - Bilow bot-ka\n" +
            "/help - Caawimaad\n\n" +
            "Airdrop scanning weli waa la dhisayaa.";
        } else {
          reply =
            "Waan helay fariintaada! ✅\n\n" +
            "SAIB wali waa la dhisayaa. Adeegso /help.";
        }

        await fetch(
          https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage,
          {
            method: "POST",
            headers: { "content-type": "application/json" },
            body: JSON.stringify({
              chat_id: chatId,
              text: reply
            })
          }
        );
      }

      return new Response("OK");
    }

    return new Response("Not found", { status: 404 });
  }
};
