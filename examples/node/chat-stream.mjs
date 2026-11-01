// Chat streaming dengan OpenAI SDK (Node.js 18+).
// Install: npm install   |   Jalankan: HUB_AI_KEY=pt-store-... npm start
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.HUB_AI_KEY,
  baseURL: process.env.HUB_AI_BASE_URL || "https://api.ptstore.my.id/v1",
});

const stream = await client.chat.completions.create({
  model: process.env.HUB_AI_MODEL || "hubai/laguna-s-2.1",
  messages: [{ role: "user", content: "Halo!" }],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || "");
}
process.stdout.write("\n");
