# Draft Examples

First drafts of intent -> spec pairs, used to work out the spec format (step 01).
The format rules are in `docs/spec_format.md`.

---

## Example 1

**Intent:**
I want a website where people can sign up and save their favourite recipes.

**Spec:**
```
Type:       Web application (CRUD)
Auth:       User registration and login (email + password, hashed with bcrypt)
Data model: User(id, email, password_hash)
            Recipe(id, user_id -> User, title, ingredients, steps, is_favourite)
Features:   - Create, read, update and delete recipes
            - Mark recipes as favourite
            - List a user's favourite recipes
API:        REST
            POST /signup
            POST /login
            GET  /recipes
            POST /recipes
            PUT  /recipes/{id}
            DELETE /recipes/{id}
Storage:    SQLite (development), PostgreSQL (production)
Tech stack: Python, FastAPI, HTML/CSS/JavaScript frontend
```

---

## Example 2

**Intent:**
An app on my phone to keep track of how much water I drink each day, and remind me if I forget.

**Spec:**
```
Type:       Mobile application
Data model: WaterLog(id, amount_ml, logged_at)
            Settings(daily_goal_ml, reminder_interval_minutes)
Features:   - Log a drink with its amount
            - Show total intake for today against the daily goal
            - Show history for past days
            - Send push notification reminders at a set interval
Storage:    Local on-device database (SQLite)
Tech stack: Flutter (Android and iOS)
```

---

## Example 3

**Intent:**
something that renames all the photos in a folder by the date they were taken

**Spec:**
```
Type:       Command-line script (automation)
Features:   - Scan a folder for image files (.jpg, .jpeg, .png, .heic)
            - Read the "date taken" from each photo's EXIF metadata
            - Rename each file to YYYY-MM-DD_HHMMSS.ext
            - Add a number suffix when two photos share the same timestamp
            - Skip files with no EXIF date and report them
Input:      Path to a folder of image files
Tech stack: Python, Pillow (EXIF reading)
```

---

## Example 4

**Intent:**
a backend that other apps can call to get the weather for a city

**Spec:**
```
Type:       REST API service
Auth:       API key per client app (sent in the X-API-Key header)
Data model: ApiClient(id, name, api_key_hash, created_at)
            WeatherCache(city, data_json, fetched_at)
Features:   - Return current weather for a city by name
            - Return a 5-day forecast for a city
            - Cache results for 10 minutes to reduce calls to the weather provider
            - Reject requests with a missing or invalid API key
            - Limit each client to 100 requests per minute
API:        REST
            GET  /weather/current?city={name}
            GET  /weather/forecast?city={name}
Storage:    Redis (cache), PostgreSQL (API clients)
Tech stack: Python, FastAPI, OpenWeatherMap API
```

---

## Example 5

**Intent:**
I want to make a simple snake game I can play in my browser

**Spec:**
```
Type:       Browser game (2D)
Features:   - Draw the game board on an HTML canvas
            - Move the snake with the arrow keys
            - Place food at a random empty cell
            - Grow the snake and add a point when it eats food
            - End the game when the snake hits a wall or itself
            - Save the high score between sessions
Storage:    Browser localStorage (high score)
Tech stack: HTML, CSS, JavaScript (Canvas API)
```

---

## Example 6

**Intent:**
look at my sales excel file and tell me which product sold the most every month

**Spec:**
```
Type:       Data analysis script
Features:   - Load the sales data from an Excel file
            - Clean the data: remove empty rows, parse dates
            - Group sales by month and product
            - Find the top-selling product for each month
            - Plot monthly sales of the top products as a bar chart
            - Export the results to a new Excel file
Input:      Excel file (.xlsx) with columns: date, product, quantity, price
Tech stack: Python, pandas, openpyxl, matplotlib
```

---

## Example 7

**Intent:**
something in chrome that blocks youtube while im working

**Spec:**
```
Type:       Browser extension
Features:   - Block chosen websites during set working hours
            - Show a "blocked" page instead of the site
            - Let the user edit the list of blocked sites
            - Let the user set working hours and working days
            - Turn blocking on or off from the toolbar button
Storage:    chrome.storage.sync (settings)
Tech stack: JavaScript, Chrome Extension Manifest V3 (declarativeNetRequest)
```

---

## Example 8

**Intent:**
a chat bot on my shop website that can answer customer questions about products and delivery

**Spec:**
```
Type:       Chatbot (web widget)
Data model: Document(id, title, content, embedding)
            Conversation(id, started_at)
            Message(id, conversation_id -> Conversation, role, text, created_at)
Features:   - Show a chat window on every page of the website
            - Answer questions using the shop's product and delivery information
            - Find relevant information with semantic search (RAG)
            - Hand over to a human by email when the bot cannot answer
            - Save conversations for later review
API:        REST
            POST /chat
            GET  /conversations/{id}
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, LLM API, JavaScript chat widget
```

---

## Example 9

**Intent:**
I need a page where I can see my server's CPU and memory usage live

**Spec:**
```
Type:       Monitoring dashboard (web)
Auth:       Single admin login (username + password)
Data model: Metric(id, server_id, cpu_percent, memory_percent, recorded_at)
Features:   - Collect CPU and memory usage every 5 seconds
            - Show live line charts of CPU and memory usage
            - Show history for the last 24 hours
            - Highlight values above a set threshold
            - Delete data older than 7 days
API:        REST + WebSocket
            GET  /metrics?from={time}&to={time}
            WS   /metrics/live
Storage:    SQLite
Tech stack: Python, FastAPI, psutil, JavaScript, Chart.js
```

---

## Example 10

**Intent:**
a notes app for my laptop that works without internet

**Spec:**
```
Type:       Desktop application
Data model: Note(id, title, body, tags, created_at, updated_at)
Features:   - Create, edit and delete notes
            - Search notes by title, text or tag
            - Format notes with Markdown
            - Save changes automatically
            - Export a note as a Markdown or PDF file
Storage:    Local SQLite database
Tech stack: Electron, React, TypeScript
```
