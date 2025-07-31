#!/usr/bin/env node

import readline from "readline";
import fs from "fs";
import { exec } from "child_process";
import { setTimeout as wait } from "timers/promises";
import fetch from "node-fetch";
import chalk from "chalk";

// SAIIM Logo
console.clear();
console.log(chalk.cyan(`
███████╗ █████╗ ██╗██╗███╗   ███╗
██╔════╝██╔══██╗██║██║████╗ ████║
███████╗███████║██║██║██╔████╔██║
╚════██║██╔══██║██║██║██║╚██╔╝██║
███████║██║  ██║██║██║██║ ╚═╝ ██║
╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝     ╚═╝
`));

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Utility Input
const ask = (q) => new Promise((res) => rl.question(q, res));

// Clean cookie
const cleanCookie = (raw) => raw.replace(/\s/g, '').replace(/;/g, '; ');

// Load messages
const loadMessages = (path) => fs.readFileSync(path, "utf-8").split("\n").filter(Boolean);

// Sender
async function sendMessage({ cookie, chatID, messages, prefix, delay, isE2EE }) {
  let index = 0;
  while (true) {
    let msg = `${prefix} ${messages[index]}`;
    index = (index + 1) % messages.length;

    const url = isE2EE
      ? `https://www.facebook.com/api/graphql/`
      : `https://www.facebook.com/messages/send/?thread_id=${chatID}`;

    const headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': cleanCookie(cookie),
      'User-Agent': 'Mozilla/5.0 (Linux; Android 10)',
    };

    const body = isE2EE
      ? `variables={"message":"${encodeURIComponent(msg)}","thread_id":"${chatID}"}` // dummy
      : `message=${encodeURIComponent(msg)}&client=mercury`;

    try {
      const res = await fetch(url, {
        method: "POST",
        headers,
        body
      });

      console.log(chalk.green(`[✓] Sent: ${msg} | Status: ${res.status}`));
    } catch (err) {
      console.log(chalk.red(`[x] Error sending: ${msg}`));
    }

    await wait(delay);
  }
}

// Main Runner
async function main() {
  console.log(chalk.yellow(`[1] Normal Chat\n[2] E2EE Chat`));
  const mode = await ask(chalk.blue("Choose (1 or 2): "));
  const chatID = await ask(chalk.magenta("Chat ID: "));
  const messageFile = await ask(chalk.magenta("Path to message file: "));
  const prefix = await ask(chalk.magenta("Prefix: "));
  const delay = parseInt(await ask(chalk.magenta("Delay in ms: ")), 10);
  const cookie = await ask(chalk.magenta("Paste browser cookie: "));

  const messages = loadMessages(messageFile);
  rl.close();

  await sendMessage({
    cookie,
    chatID,
    messages,
    prefix,
    delay,
    isE2EE: mode.trim() === "2"
  });
}

main();
