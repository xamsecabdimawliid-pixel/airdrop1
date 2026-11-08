export default {
  async fetch(request, env) {
    return new Response(
      "SAIB Worker is online!",
      {
        headers: {
          "content-type": "text/plain"
        }
      }
    );
  }
};
