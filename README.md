# 🧠 s8eagv1 – Modular Cognitive Agent Framework

`s8eagv1` is a modular AI agent framework designed to run multi-tool LLM agents using [MCP](https://github.com/mcptools/mcp) (Model Control Protocol). It supports dynamic tool composition, Google Sheets integration, Telegram-based agent control, and local embeddings.

[Demo](https://youtu.be/esfzxu_XPtw)

---

## 🚀 Features

- 🧩 **MultiMCP**: Integrates multiple MCP tool servers over both `stdio` and `http`
- 🤖 **Custom Agent**: Structured agent planning and execution using `AgentLoop`
- 📄 **Google Sheets Tools**: Create, update, and share spreadsheets via an HTTP (SSE) MCP server
- 📡 **Telegram Bot Interface**: Send query to your agent via chat, simply send a message
- 🔍 **Semantic Search**: Embed and index local files using `nomic-ai/nomic-embed-text-v1`
- 🧠 **LLM Interop**: Use models like `gemini-2.0-flash` through your local orchestration
- 🔧 **Extensible Tool Servers**: Easily add new tools via Python MCP wrappers

---

## 🧪 Step 2: Set Environment

```
TELEGRAM_BOT_TOKEN=your_token_here
DRIVE_FOLDER_ID=your_google_drive_folder_id
GOOGLE_CREDENTIALS=service_account.json
```

set evironment variable to run sse MCP server for Google Sheet operations, refer this [repo](https://github.com/xing5/mcp-google-sheets/blob/main/README.md).
```
export DRIVE_FOLDER_ID=<folder_id_in_which_sheets_are_created>
```

## Run Http (SSE) Google Spreadsheet MCP Server

```
cd s8eagv1/mcp_servers/mcp_google_sheets
python server.py
```

## 🚀 Step 3: Run the Telegram Bot
```
python TelegramBot.py

```
