// gta6-meme-x-01 entry (akun 4): the meme is the post on X, not this
// program. This file only carries POST.json — the post's address — into
// /output, where the gate reads it. No network, no wall clock, one file.
import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const SRC = join(BOT_DIR, "POST.json");

if (!existsSync(SRC)) {
  console.error(`POST.json not found in the repository: ${SRC}`);
  process.exit(1);
}

mkdirSync(OUT_DIR, { recursive: true });
copyFileSync(SRC, join(OUT_DIR, "POST.json"));

// Guard: the existsSync check above is the real guard — without POST.json
// in the repository, the gate would see an empty output and fail.
