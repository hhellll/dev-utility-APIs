/**
 * Background Remover AI — JavaScript (Node.js 18+) example.
 *
 * Usage:
 *   RAPIDAPI_KEY=your_key node javascript_example.js photo.jpg
 *   RAPIDAPI_KEY=your_key node javascript_example.js --url https://example.com/photo.jpg
 *
 * Get your key by subscribing (free plan available) at:
 *   https://rapidapi.com/Hitler-HlDevZDwP/api/background-remover-ai5
 */
import { readFile, writeFile } from "node:fs/promises";

const API_URL = "https://background-remover-ai5.p.rapidapi.com/remove-background";
const API_HOST = "background-remover-ai5.p.rapidapi.com";

const key = process.env.RAPIDAPI_KEY;
if (!key) {
  console.error("Set RAPIDAPI_KEY first (see the RapidAPI page for your key).");
  process.exit(1);
}

const headers = { "X-RapidAPI-Key": key, "X-RapidAPI-Host": API_HOST };
const args = process.argv.slice(2);
const form = new FormData();

if (args[0] === "--url") {
  form.append("image_url", args[1]);
} else if (args[0]) {
  form.append("image", new Blob([await readFile(args[0])]), args[0]);
} else {
  console.error("Usage: node javascript_example.js <photo.jpg | --url URL>");
  process.exit(1);
}

const res = await fetch(API_URL, { method: "POST", headers, body: form });
if (!res.ok) throw new Error(`API error: ${res.status} ${await res.text()}`);

await writeFile("result.png", Buffer.from(await res.arrayBuffer()));
console.log("Saved result.png");
