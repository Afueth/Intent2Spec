## Example 1

**Intent:**
block youtube shorts

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Hide the Shorts shelf on the YouTube home and subscriptions pages
            - Redirect /shorts/ URLs to the normal watch page
            - Remove the Shorts tab from the sidebar
            - Toggle blocking on or off from the toolbar popup
Storage:    chrome.storage.sync (on/off setting)
Tech stack: JavaScript, Chrome Manifest V3, content script with MutationObserver, declarativeNetRequest (redirects)
```

---

## Example 2

**Intent:**
A browser add-on that tells me how long I've spent on each website today.

**Spec:**
```
Type:       Browser extension (productivity)
Data model: DailyUsage(date, domain, seconds_active)
Features:   - Track the active tab's domain using tab and window focus events
            - Pause tracking when the browser is idle for 60 seconds
            - Show today's top sites with time in the popup
            - Show a 7-day bar chart on an options page
            - Reset counters at midnight
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, service worker, chrome.idle and chrome.tabs APIs, Chart.js
```

---

## Example 3

**Intent:**
i keep forgetting what tabs i had open yesterday can u make something that saves them

**Spec:**
```
Type:       Browser extension (productivity)
Data model: Session(id, name, saved_at)
            SavedTab(session_id -> Session, title, url, pinned)
Features:   - Save all open tabs in the current window as a named session
            - Auto-save a snapshot every 30 minutes
            - List saved sessions in the popup with tab counts
            - Restore a session into a new window
            - Delete old sessions
Storage:    chrome.storage.local
Tech stack: TypeScript, Chrome Manifest V3, service worker, chrome.tabs and chrome.alarms APIs
```

---

## Example 4

**Intent:**
Extension that strips tracking parameters like utm_source and fbclid from links I click.

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Remove known tracking query parameters (utm_*, fbclid, gclid, mc_eid) before navigation
            - Clean links copied to the clipboard from the context menu
            - Let the user add custom parameters to strip
            - Show a count of cleaned URLs in the toolbar badge
Storage:    chrome.storage.sync (custom parameter list, counters)
Tech stack: JavaScript, Chrome Manifest V3, declarativeNetRequest with regexSubstitution rules, chrome.contextMenus
```

---

## Example 5

**Intent:**
dark mode for every site

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Invert page colours with a CSS filter while keeping images and videos un-inverted
            - Toggle dark mode per site from the popup
            - Remember the per-site choice
            - Adjust brightness and contrast with sliders
Storage:    chrome.storage.sync (per-domain settings)
Tech stack: JavaScript, Chrome Manifest V3, content script, chrome.scripting.insertCSS
```

---

## Example 6

**Intent:**
I sell handmade candles on Shopify and want customers to see a little banner saying "order in the next X hours to ship today". Can that be done as an app block?

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Data model: ShopSettings(shop_domain, cutoff_time, timezone, closed_weekdays, banner_text)
Features:   - Show a countdown banner on product pages until the daily shipping cutoff
            - Switch the message to the next shipping day after the cutoff or on closed days
            - Let the merchant set cutoff time, timezone and text in the admin
            - Provide the banner as a theme app extension block the merchant can place
API:        REST
            GET /api/settings
            PUT /api/settings
Storage:    PostgreSQL (shop settings)
Tech stack: Node.js, Shopify CLI, Remix app template, Theme App Extension (Liquid + JavaScript), Polaris
```

---

## Example 7

**Intent:**
wordpress plugin that shows reading time on top of blog posts

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Count words in the post content and estimate minutes at 200 words per minute
            - Prepend "X min read" above the post content with the the_content filter
            - Provide a [reading_time] shortcode for custom placement
            - Add a settings page for words-per-minute and label text
Storage:    WordPress options table (wp_options)
Tech stack: PHP, WordPress Plugin API (hooks, filters, Settings API)
```

---

## Example 8

**Intent:**
VS Code extension that counts my TODO comments across the whole project and lists them in a sidebar.

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Scan workspace files for TODO, FIXME and HACK comments
            - Show results grouped by file in a tree view in the activity bar
            - Jump to the line when an item is clicked
            - Refresh the list on file save
            - Show the total count in the status bar
Tech stack: TypeScript, VS Code Extension API (TreeDataProvider, workspace.findFiles), ripgrep via child process
```

---

## Example 9

**Intent:**
Google Sheets thing where I pick a column and it removes duplicate rows but keeps the newest one, apps script please

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Add a custom menu "Dedupe" to the spreadsheet
            - Ask the user to choose the key column and the date column in a sidebar
            - Keep only the row with the latest date for each key value
            - Copy the removed rows to a "Removed" sheet as a backup
            - Show how many rows were removed
Tech stack: Google Apps Script, HtmlService (sidebar), SpreadsheetApp
```

---

## Example 10

**Intent:**
Figma plugin to rename all selected layers with a number at the end like Card 1, Card 2...

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Read the current selection of layers
            - Rename layers with a base name and an incrementing number
            - Let the user choose start number, padding and order (top-to-bottom or left-to-right)
            - Preview the new names before applying
            - Support undo as a single history step
Tech stack: TypeScript, Figma Plugin API, HTML UI iframe
```

---

## Example 11

**Intent:**
Can there be a Gmail add-on that, when I open an email, shows if the sender is already in our CRM?

**Spec:**
```
Type:       Plugin (Gmail add-on)
Auth:       Google OAuth (Workspace add-on scopes) plus CRM API token stored per user
Features:   - Read the sender address of the open message
            - Look up the contact in the CRM by email
            - Show contact name, company and last deal stage in a card
            - Offer a button to create a new CRM contact if not found
Storage:    Apps Script PropertiesService (per-user API token)
Tech stack: Google Apps Script, CardService (Workspace add-on), UrlFetchApp, HubSpot REST API
```

---

## Example 12

**Intent:**
obsidian plugin that makes a daily note with the weather in it

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Create today's daily note from a template on startup if it doesn't exist
            - Fetch current weather and forecast for a configured city
            - Insert weather into the note at a {{weather}} placeholder
            - Add a settings tab for city, units and API key
Storage:    Obsidian plugin data.json (settings)
Tech stack: TypeScript, Obsidian Plugin API, Open-Meteo API
```

---

## Example 13

**Intent:**
New tab page with a big clock, a todo list and a nice photo background.

**Spec:**
```
Type:       Browser extension (new tab page)
Data model: Todo(id, text, done, created_at)
Features:   - Override the new tab page with a custom HTML page
            - Show the time and date in large text
            - Add, tick off and delete todos
            - Load a daily background photo and cache it for the day
            - Show photo credit in the corner
Storage:    chrome.storage.local (todos, cached photo)
Tech stack: JavaScript, Chrome Manifest V3 (chrome_url_overrides), Unsplash API
```

---

## Example 14

**Intent:**
price history for amazon

**Spec:**
```
Type:       Browser extension (shopping)
Data model: PricePoint(product_asin, price, currency, seen_at)
Features:   - Detect product pages and read the ASIN and current price with a content script
            - Record the price each time the page is visited
            - Show a small price-history chart under the price
            - Alert when the price drops below a target set by the user
Storage:    IndexedDB (price history), chrome.storage.sync (targets)
Tech stack: TypeScript, Chrome Manifest V3, content script, chrome.notifications, uPlot
```

---

## Example 15

**Intent:**
Hello, I am teacher in Brazil. I need extension for Chrome which read aloud the text I select, because some my students have dificulty reading.

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Add a "Read aloud" item to the right-click menu for selected text
            - Speak the text with the browser's speech synthesis
            - Let the user choose voice, language (e.g. Portuguese) and speed in the popup
            - Highlight each word while it is spoken
            - Stop or pause with a keyboard shortcut
Storage:    chrome.storage.sync (voice and speed settings)
Tech stack: JavaScript, Chrome Manifest V3, chrome.contextMenus, chrome.tts API, chrome.commands
```

---

## Example 16

**Intent:**
WooCommerce plugin: give a 10% discount automatically if someone's cart has 3 or more items from the same category.

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Count cart items per product category on cart update
            - Apply a percentage fee/discount when a category reaches the threshold
            - Show a notice telling shoppers how many more items unlock the discount
            - Add admin settings for threshold, percentage and excluded categories
Storage:    WordPress options table
Tech stack: PHP, WooCommerce hooks (woocommerce_cart_calculate_fees, woocommerce_before_cart), WordPress Settings API
```

---

## Example 17

**Intent:**
jetbrains plugin to copy the current file path relative to project root

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Add an action to the editor tab and project view context menus
            - Copy the file path relative to the project root to the clipboard
            - Offer variants with line number (path:line) and as a Markdown link
            - Bind the action to a default keyboard shortcut
            - Show a balloon notification after copying
Tech stack: Kotlin, IntelliJ Platform SDK, Gradle IntelliJ Plugin
```

---

## Example 18

**Intent:**
so i read a lot of long articles at work and i always lose my place when i switch tabs or close the laptop. would love something that just remembers how far down i scrolled on every article and brings me back there when i open it again, nothing fancy

**Spec:**
```
Type:       Browser extension (reading)
Data model: ScrollPosition(url, scroll_percent, updated_at)
Features:   - Save the scroll position of a page as a percentage when the user scrolls (debounced)
            - Restore the position when the same URL is opened again
            - Ignore pages shorter than two screens
            - Show a "Resume reading" toast with an option to start from the top
            - Delete positions older than 30 days
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 19

**Intent:**
Excel add-in that converts currency in selected cells using today's rates.

**Spec:**
```
Type:       Plugin (Excel add-in)
Features:   - Read the selected range with the Office JavaScript API
            - Fetch today's exchange rates for a chosen source and target currency
            - Write converted values into the adjacent column
            - Add a custom function =CONVERTFX(amount, from, to)
            - Show the rate date in the task pane
Tech stack: TypeScript, Office Add-ins (Office.js, Excel JavaScript API, custom functions), Frankfurter exchange rate API
```

---

## Example 20

**Intent:**
Outlook add-in that warns me before sending an email to someone outside my company

**Spec:**
```
Type:       Plugin (Outlook add-in)
Features:   - Run on send using the OnMessageSend event-based activation
            - Compare recipient domains against the organisation's domain list
            - Show a warning dialog listing external recipients
            - Let the user cancel or send anyway
            - Allow an admin to configure internal domains
Storage:    Office roamingSettings (domain list)
Tech stack: JavaScript, Office Add-ins (Office.js, Smart Alerts), XML manifest
```

---

## Example 21

**Intent:**
firefox extension to block cookie popups

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Hide common cookie consent banners with a maintained CSS selector list
            - Click "reject all" automatically when a known consent framework is detected
            - Restore page scrolling locked by banners
            - Let the user disable the extension per site
Storage:    browser.storage.local (selector list, site exceptions)
Tech stack: JavaScript, Firefox WebExtensions API (Manifest V3), content scripts
```

---

## Example 22

**Intent:**
i want a chrome extension that puts a little note on any website, like a sticky note, and it stays there when i come back

**Spec:**
```
Type:       Browser extension (productivity)
Data model: StickyNote(id, url, text, x, y, color, created_at)
Features:   - Add a sticky note to the current page from the popup or context menu
            - Drag notes around and edit text in place
            - Save notes per URL and show them again on revisit
            - List all notes across sites in the popup
            - Delete a note
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, content script with Shadow DOM for note styling
```

---

## Example 23

**Intent:**
Notion integration that sends my new Notion tasks to Google Calendar as events

**Spec:**
```
Type:       Webhook service (Notion integration)
Auth:       Notion internal integration token, Google OAuth 2.0
Data model: SyncedTask(notion_page_id, calendar_event_id, last_edited_time)
Features:   - Poll a Notion database for tasks with a due date every 5 minutes
            - Create a Google Calendar event for each new task
            - Update the event when the task's title or date changes
            - Delete the event when the task is archived
Storage:    SQLite (page-to-event mapping)
Tech stack: Python, Notion API (notion-client), Google Calendar API, APScheduler
```

---

## Example 24

**Intent:**
VS Code theme extension with warm colors that are easy on the eyes

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Define a dark and a light colour theme with warm, low-contrast tones
            - Provide semantic token colours for common languages
            - Style the workbench (sidebar, tabs, status bar, terminal)
            - Package and publish to the VS Code Marketplace
Tech stack: JSON (VS Code color theme), vsce
```

---

## Example 25

**Intent:**
Make a Chrome extension for developers that pretty prints JSON when I open a JSON URL.

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Detect responses served as application/json
            - Render JSON as a collapsible, syntax-highlighted tree
            - Toggle between raw and formatted views
            - Copy a value's JSON path on click
            - Support dark and light themes
Tech stack: TypeScript, Chrome Manifest V3, content script, Preact
```

---

## Example 26

**Intent:**
hey so my mom uses facebook a lot and gets scared by all the political stuff, could an extension hide posts with certain words? she's not techy so needs to be super easy

**Spec:**
```
Type:       Browser extension (productivity)
Data model: Settings(blocked_words, show_placeholder)
Features:   - Hide feed posts that contain any word from a blocked list
            - Show a collapsed "Hidden post" placeholder that can be expanded
            - Provide a simple popup with large text to add or remove words
            - Ship with an optional starter list of political keywords
            - Re-check new posts as the feed scrolls
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script with MutationObserver
```

---

## Example 27

**Intent:**
wp plugin for a simple FAQ accordion

**Spec:**
```
Type:       Plugin (WordPress)
Data model: FAQ(question, answer, menu_order, faq_category)
Features:   - Register an FAQ custom post type and category taxonomy
            - Render FAQs as an accessible accordion with the [faq category="..."] shortcode
            - Provide a Gutenberg block with the same output
            - Add FAQPage schema.org JSON-LD for search engines
Storage:    WordPress database (posts, terms)
Tech stack: PHP, WordPress hooks, Block API (React/JSX), vanilla JavaScript
```

---

## Example 28

**Intent:**
Google Docs add-on that checks my essay for passive voice

**Spec:**
```
Type:       Plugin (Google Docs add-on)
Features:   - Read the document body text paragraph by paragraph
            - Detect passive constructions (form of "to be" + past participle)
            - Highlight matches in yellow in the document
            - List findings in a sidebar with click-to-select
            - Clear highlights with one button
Tech stack: Google Apps Script, DocumentApp, HtmlService sidebar
```

---

## Example 29

**Intent:**
Figma plugin that checks color contrast of text layers against their background

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Find all text layers in the selection or current page
            - Determine each text's fill colour and the nearest background fill behind it
            - Calculate the WCAG contrast ratio
            - Flag layers that fail AA or AAA in a list
            - Select the layer on the canvas when clicked in the list
Tech stack: TypeScript, Figma Plugin API, React UI
```

---

## Example 30

**Intent:**
browser extension: right click on an image -> search it on reverse image search sites

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Add a context menu entry on images
            - Offer sub-items for several reverse image search engines
            - Open the search with the image URL in a new tab
            - Let the user enable or disable engines in options
Storage:    chrome.storage.sync (enabled engines)
Tech stack: JavaScript, Chrome Manifest V3, chrome.contextMenus
```

---

## Example 31

**Intent:**
something to stop me from going on reddit during work hours

**Spec:**
```
Type:       Browser extension (productivity)
Data model: BlockRule(domain, days, start_time, end_time)
Features:   - Block listed domains during a configured weekly schedule
            - Show a calm "Back to work" page instead of the site
            - Allow a 5-minute snooze limited to 3 times per day
            - Add sites to the block list from the popup
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, declarativeNetRequest dynamic rules, chrome.alarms
```

---

## Example 32

**Intent:**
Im building a little game in my free time and want to let players make mods. How would a mod loader work where people drop Lua scripts into a folder and they add new items?

**Spec:**
```
Type:       Desktop game (mod loader)
Data model: ModManifest(id, name, version, author, dependencies, entry_script)
            ItemDefinition(id, mod_id, name, sprite_path, stats)
Features:   - Scan a mods folder for subfolders containing a mod.json manifest
            - Resolve load order from declared dependencies
            - Run each mod's Lua script in a sandbox without file or OS access
            - Expose a register_item() API for mods to add new items
            - Report mod errors in an in-game log without crashing
Storage:    Local file system (mods folder)
Tech stack: C#, MonoGame, MoonSharp (Lua interpreter)
```

---

## Example 33

**Intent:**
shopify app to let customers upload a photo when they buy a custom product

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Data model: Upload(id, shop_domain, file_url, order_id, line_item_key, uploaded_at)
Features:   - Add an upload button to product pages through a theme app extension
            - Store uploaded files and attach the file URL as a line item property
            - Validate file type and size (JPG/PNG, max 10 MB)
            - Show uploads next to each order in the app's admin page
API:        REST
            POST /api/uploads
            GET /api/orders/{id}/uploads
Storage:    Amazon S3 (files), PostgreSQL (upload records)
Tech stack: Node.js, Shopify CLI, Remix, Theme App Extension, Polaris
```

---

## Example 34

**Intent:**
chrome extension that copies the page title and url as a markdown link with one click

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Copy [title](url) of the active tab when the toolbar icon is clicked
            - Offer other formats (plain, HTML, org-mode) via the context menu
            - Show a brief "Copied" badge
            - Bind a keyboard shortcut to the default format
Storage:    chrome.storage.sync (default format)
Tech stack: JavaScript, Chrome Manifest V3, chrome.action, Clipboard API via offscreen document
```

---

## Example 35

**Intent:**
Obsidian plugin that shows how many words I wrote today across all notes.

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Data model: DailyCount(date, words_added)
Features:   - Track word count changes on each file modify event
            - Sum words added per day across the vault
            - Show today's total in the status bar
            - Show a goal progress bar and a history view
            - Configure the daily word goal in settings
Storage:    Obsidian plugin data.json
Tech stack: TypeScript, Obsidian Plugin API
```

---

## Example 36

**Intent:**
dictionary popup when i double click a word

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Detect double-clicked words in a content script
            - Look up the definition from a free dictionary API
            - Show a small popup near the word with definition and pronunciation
            - Play pronunciation audio when available
            - Save looked-up words to a list
Storage:    chrome.storage.local (saved words)
Tech stack: JavaScript, Chrome Manifest V3, content script, Free Dictionary API
```

---

## Example 37

**Intent:**
An Apps Script add-on for Google Forms that closes the form automatically after 100 responses.

**Spec:**
```
Type:       Plugin (Google Forms add-on)
Features:   - Let the form owner set a response limit and an optional close date in a sidebar
            - Install an onFormSubmit trigger that counts responses
            - Stop accepting responses when the limit or date is reached
            - Set a custom "form closed" message
            - Email the owner when the form closes
Storage:    Apps Script PropertiesService (form settings)
Tech stack: Google Apps Script, FormApp, ScriptApp triggers, MailApp
```

---

## Example 38

**Intent:**
Plz make a VS Code extension where I highlight code and it explains it with AI

**Spec:**
```
Type:       Plugin (VS Code extension)
Auth:       User's OpenAI API key stored in VS Code SecretStorage
Features:   - Add an "Explain selection" command to the editor context menu
            - Send the selected code and language to an LLM API
            - Show the explanation in a webview panel beside the editor
            - Stream the response as it is generated
            - Let the user ask a follow-up question
Tech stack: TypeScript, VS Code Extension API (commands, webview, SecretStorage), OpenAI API
```

---

## Example 39

**Intent:**
password generator in the toolbar

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Generate a random password in the popup with crypto.getRandomValues
            - Set length and toggle uppercase, digits and symbols
            - Copy the password to the clipboard with one click
            - Fill the focused password field on the page from the context menu
Storage:    chrome.storage.sync (generator preferences)
Tech stack: JavaScript, Chrome Manifest V3, chrome.scripting
```

---

## Example 40

**Intent:**
WordPress plugin to show a popup asking visitors to join my newsletter after they scroll halfway, connect to Mailchimp.

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Show a modal signup form when the visitor scrolls past 50% of the page
            - Submit the email to a Mailchimp audience through a REST endpoint
            - Hide the popup for 30 days after closing or subscribing with a cookie
            - Let the admin set the heading, text, delay and audience ID
            - Exclude chosen pages
API:        WordPress REST API
            POST /wp-json/newsletter-popup/v1/subscribe
Storage:    WordPress options table
Tech stack: PHP, WordPress REST API, Mailchimp Marketing API, vanilla JavaScript
```

---

## Example 41

**Intent:**
My boss wants every new Google Sheet row from our form sent to a Slack channel. Apps script ok.

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Install an onFormSubmit trigger on the response spreadsheet
            - Format the new row as a Slack message with field names and values
            - Post the message to a Slack incoming webhook URL
            - Let the user set the webhook URL and which columns to include from a menu dialog
            - Log failed posts to a hidden sheet
Storage:    Apps Script PropertiesService (webhook URL)
Tech stack: Google Apps Script, UrlFetchApp, Slack Incoming Webhooks
```

---

## Example 42

**Intent:**
extensión de chrome para traducir? no, I mean I want hover over a word and see translation in Spanish, english is not my first language

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Detect the word under the mouse after a short hover delay
            - Translate the word or selected sentence into the user's language
            - Show the translation in a tooltip near the cursor
            - Let the user choose the target language and turn hover mode on or off
            - Keep a list of translated words for review
Storage:    chrome.storage.sync (settings), chrome.storage.local (word list)
Tech stack: JavaScript, Chrome Manifest V3, content script, LibreTranslate API
```

---

## Example 43

**Intent:**
tab limiter so i cant open more than 10 tabs

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Count open tabs across all windows on tab creation
            - Close the newly opened tab and show a notification when the limit is exceeded
            - Let the user set the maximum number of tabs
            - Show current tab count on the toolbar badge
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, service worker, chrome.tabs, chrome.notifications
```

---

## Example 44

**Intent:**
A Figma plugin that exports all the colors in my file as CSS variables.

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Read local paint styles and variables from the file
            - Convert colour names to kebab-case CSS custom property names
            - Output a :root block with hex or rgba values
            - Offer alternative output formats (SCSS, Tailwind config JSON)
            - Copy the result or download it as a file
Tech stack: TypeScript, Figma Plugin API, HTML UI
```

---

## Example 45

**Intent:**
accessibility checker extension for web developers

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Run an accessibility audit on the current page from a DevTools panel
            - List violations grouped by severity with the WCAG rule
            - Highlight the offending element on the page when selected
            - Re-run the audit after page changes
            - Export results as JSON
Tech stack: TypeScript, Chrome Manifest V3, chrome.devtools.panels, axe-core
```

---

## Example 46

**Intent:**
i need a plugin for my wordpress site that hides the admin bar for everyone who is not an admin

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Hide the front-end admin bar for users without the manage_options capability
            - Let the admin choose which roles still see it
            - Optionally redirect non-admins away from /wp-admin to the homepage
Storage:    WordPress options table
Tech stack: PHP, WordPress hooks (show_admin_bar filter, admin_init)
```

---

## Example 47

**Intent:**
Chrome extension that shows the Wayback Machine version if a page is 404

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Detect 404 and 5xx responses for top-level navigations
            - Query the Wayback Machine availability API for the URL
            - Show a banner offering the latest archived copy
            - Add a toolbar button to save the current page to the archive
Tech stack: JavaScript, Chrome Manifest V3, chrome.webRequest (onCompleted), Wayback Machine Availability API
```

---

## Example 48

**Intent:**
VS Code extension for my team that inserts our standard file header comment with author and date.

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Add a command that inserts a header comment at the top of the active file
            - Fill in author from git config, current date and file name
            - Use the correct comment syntax for the file's language
            - Optionally insert the header automatically on new file creation
            - Read the header template from workspace settings
Tech stack: TypeScript, VS Code Extension API (commands, workspace.onDidCreateFiles, configuration)
```

---

## Example 49

**Intent:**
Can I make a Minecraft-like block game have plugins? I want a server plugin system for my own voxel game in Java where plugins can listen to events like player join or block break.

**Spec:**
```
Type:       Desktop game (server plugin system)
Data model: PluginDescriptor(name, version, main_class, depends)
Features:   - Load plugin JAR files from a plugins folder at server start
            - Read a plugin.yml descriptor and call the main class's onEnable and onDisable
            - Provide an event bus with PlayerJoinEvent, BlockBreakEvent and cancellable events
            - Let plugins register chat commands
            - Isolate each plugin with its own class loader
Storage:    Local file system (plugins folder, per-plugin config files)
Tech stack: Java, URLClassLoader, SnakeYAML
```

---

## Example 50

**Intent:**
keyboard shortcuts for youtube speed

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Increase or decrease video playback speed with keyboard shortcuts
            - Allow speeds above 2x up to 4x
            - Show the current speed as an overlay on the video
            - Remember the last used speed
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script (HTMLMediaElement.playbackRate)
```

---

## Example 51

**Intent:**
an excel add-in to make a quick gantt chart from a list of tasks with start and end dates

**Spec:**
```
Type:       Plugin (Excel add-in)
Features:   - Read a selected table with task, start date and end date columns
            - Create a new sheet with one column per day or week
            - Fill cells between start and end with a colour per task
            - Add today's date marker
            - Rebuild the chart when the user clicks Refresh in the task pane
Tech stack: JavaScript, Office Add-ins (Office.js, Excel JavaScript API), React task pane
```

---

## Example 52

**Intent:**
screenshot whole page extension

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Capture the full scrolling page by scrolling and stitching visible-area captures
            - Capture only a selected region by dragging
            - Open the result in an editor tab to crop and annotate
            - Download as PNG or PDF
Tech stack: JavaScript, Chrome Manifest V3, chrome.tabs.captureVisibleTab, OffscreenCanvas, jsPDF
```

---

## Example 53

**Intent:**
I'd like a Chrome extension that warns me when a site I'm typing my password into is not HTTPS.

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Detect focus on password inputs in a content script
            - Check whether the page or the form action uses plain HTTP
            - Show a red warning bar above the field
            - Let the user dismiss the warning for a specific site
Storage:    chrome.storage.local (dismissed sites)
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 54

**Intent:**
coupon finder that tries codes at checkout

**Spec:**
```
Type:       Browser extension (shopping)
Data model: CouponCode(store_domain, code, description, last_worked_at, success_count)
Features:   - Detect checkout pages of supported stores by URL and DOM selectors
            - Fetch known coupon codes for the store from a backend
            - Apply each code in the promo field and read the resulting total
            - Keep the code that gives the biggest saving
            - Report which codes worked back to the backend
API:        REST
            GET /coupons?domain={domain}
            POST /coupons/{id}/result
Storage:    PostgreSQL (backend coupon database)
Tech stack: TypeScript, Chrome Manifest V3, content scripts, Node.js + Express backend
```

---

## Example 55

**Intent:**
chrome extension to mute all tabs except the one im looking at

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Mute every audible tab except the active one when the active tab changes
            - Unmute the tab when the user switches to it
            - Toggle the feature from the toolbar button
            - Add a whitelist of sites that are never muted (e.g. music players)
Storage:    chrome.storage.sync (whitelist, enabled state)
Tech stack: JavaScript, Chrome Manifest V3, service worker, chrome.tabs.update (muted)
```

---

## Example 56

**Intent:**
I'm dyslexic and find most websites hard to read. I want an extension that changes the font to OpenDyslexic, makes lines further apart and maybe adds a coloured overlay like the plastic sheets I use with books.

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Replace page fonts with OpenDyslexic using an injected stylesheet
            - Increase line height, letter spacing and word spacing with sliders
            - Add a tinted colour overlay with adjustable colour and opacity
            - Show a reading ruler that follows the mouse
            - Apply settings to all sites or per site
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script, bundled OpenDyslexic web font
```

---

## Example 57

**Intent:**
React DevTools-like thing but for my Vue app's state, as a chrome devtools panel

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Add a DevTools panel that connects to the inspected page
            - Inject a script that reads the Vue app's Pinia stores
            - Show store state as an editable tree
            - Record state mutations in a timeline with diffs
            - Allow time-travel by restoring an earlier snapshot
Tech stack: TypeScript, Chrome Manifest V3, chrome.devtools.panels, chrome.runtime ports, Vue 3
```

---

## Example 58

**Intent:**
WP plugin that lets members download PDFs only if they are logged in

**Spec:**
```
Type:       Plugin (WordPress)
Data model: ProtectedFile(attachment_id, allowed_roles, download_count)
Features:   - Mark media library PDFs as protected
            - Serve protected files through a PHP endpoint that checks login and role
            - Block direct access to the protected upload folder with .htaccess rules
            - Count downloads per file
            - Provide a [protected_download id=".."] shortcode for links
Storage:    WordPress database (post meta)
Tech stack: PHP, WordPress hooks, Media Library, Apache .htaccess
```

---

## Example 59

**Intent:**
an add-on for google sheets that pulls my stock prices every hour

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Read ticker symbols from column A of a "Portfolio" sheet
            - Fetch latest prices from a stock quote API
            - Write price, daily change and timestamp to the next columns
            - Run on a time-driven trigger every hour during market hours
            - Calculate total portfolio value
Storage:    Apps Script PropertiesService (API key)
Tech stack: Google Apps Script, UrlFetchApp, ScriptApp time-based triggers, Alpha Vantage API
```

---

## Example 60

**Intent:**
VS Code extension that runs prettier on save only for files I've changed in git.

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Listen for document save events
            - Check if the file is modified or untracked in git using the built-in Git extension API
            - Format modified files with Prettier using the project's config
            - Skip unchanged files and files in .prettierignore
            - Add a setting to turn the behaviour on or off
Tech stack: TypeScript, VS Code Extension API (onWillSaveTextDocument, vscode.git API), Prettier
```

---

## Example 61

**Intent:**
hide all the like counts and follower numbers on social media, they make me anxious

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Hide like, retweet, view and follower counts on supported social sites with CSS rules
            - Keep the buttons usable while hiding the numbers
            - Let the user pick which counters to hide per site
            - Reveal counts temporarily by holding a key
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content scripts, injected CSS
```

---

## Example 62

**Intent:**
Figma plugin that fills text layers with realistic fake data like names, emails, addresses.

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Show data categories (name, email, phone, address, date, price) in the plugin UI
            - Fill selected text layers with random values of the chosen type
            - Use layer names like "#email" to auto-detect the data type
            - Load fonts before changing text
            - Allow choosing a locale for the generated data
Tech stack: TypeScript, Figma Plugin API (loadFontAsync), Faker.js
```

---

## Example 63

**Intent:**
Gmail add on to save attachments to google drive in a folder by sender name

**Spec:**
```
Type:       Plugin (Gmail add-on)
Auth:       Google OAuth (Gmail and Drive scopes)
Features:   - Show a card with the open message's attachments
            - Create or find a Drive folder named after the sender
            - Save selected attachments into that folder
            - Add a "Save all" button
            - Show links to the saved files
Tech stack: Google Apps Script, CardService, GmailApp, DriveApp
```

---

## Example 64

**Intent:**
obsidian plugin to show my notes on a map if they have coordinates in front matter

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Read latitude and longitude from each note's frontmatter via metadataCache
            - Show all notes as markers on an interactive map view
            - Open the note when a marker is clicked
            - Filter markers by tag
            - Add a command to insert coordinates for a searched place
Tech stack: TypeScript, Obsidian Plugin API (ItemView, metadataCache), Leaflet, OpenStreetMap tiles, Nominatim geocoding
```

---

## Example 65

**Intent:**
Hi! My English not so good. I want make plugin for WordPress where customer can book appointment in my hair salon, choose day and hour.

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Service(id, name, duration_minutes, price)
            Appointment(id, service_id -> Service, customer_name, phone, email, start_at, status)
            OpeningHours(weekday, open_time, close_time)
Features:   - Show a booking form with service, date and free time slots via shortcode
            - Calculate free slots from opening hours and existing appointments
            - Send confirmation emails to customer and salon
            - Let the owner confirm, cancel and view appointments in wp-admin
API:        WordPress REST API
            GET /wp-json/salon/v1/slots?date={date}&service={id}
            POST /wp-json/salon/v1/appointments
Storage:    Custom MySQL tables via $wpdb
Tech stack: PHP, WordPress REST API, wp_mail, vanilla JavaScript
```

---

## Example 66

**Intent:**
price comparison extension for books

**Spec:**
```
Type:       Browser extension (shopping)
Features:   - Detect ISBN on book product pages
            - Query several bookstores' prices through a backend
            - Show a sidebar with prices and shipping, sorted cheapest first
            - Link directly to each store's product page
            - Cache results for an hour
API:        REST
            GET /prices?isbn={isbn}
Storage:    Redis (backend price cache)
Tech stack: JavaScript, Chrome Manifest V3, content script, Python + FastAPI backend
```

---

## Example 67

**Intent:**
I'd like a JetBrains plugin that shows a warning if a method is longer than 50 lines.

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Add a local inspection that measures method body length
            - Highlight methods over the configured line limit
            - Offer a quick-fix to run Extract Method
            - Make the line limit configurable in inspection settings
            - Support Java and Kotlin files
Tech stack: Kotlin, IntelliJ Platform SDK (LocalInspectionTool, PSI)
```

---

## Example 68

**Intent:**
font identifier when i hover text

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Toggle an inspect mode from the toolbar
            - Show font family, size, weight, line height and colour on hover
            - Detect which font in the stack is actually rendered
            - Copy the CSS of a clicked element
Tech stack: JavaScript, Chrome Manifest V3, content script (getComputedStyle, document.fonts)
```

---

## Example 69

**Intent:**
woocommerce plugin show "only 3 left in stock" on product page

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Show a low-stock message when stock quantity is under a threshold
            - Hook into woocommerce_single_product_summary to render the message
            - Show the message on variable products per selected variation
            - Let the admin set threshold, text and colour
Storage:    WordPress options table
Tech stack: PHP, WooCommerce hooks, JavaScript (found_variation event)
```

---

## Example 70

**Intent:**
So I'm a freelance writer and I keep notes in Notion for every client, and I'd love a Chrome extension where I can highlight text on any website and send it straight into a Notion page for that client with the source link, without copy pasting all day.

**Spec:**
```
Type:       Browser extension (productivity)
Auth:       Notion OAuth (public integration)
Data model: ClientPage(name, notion_page_id)
            Clip(text, source_url, page_title, clipped_at)
Features:   - Add a "Send to Notion" context menu item for selected text
            - Let the user choose the client page from a list fetched from Notion
            - Append the text as a quote block with the source link and date
            - Remember the last used client page
            - Show a success notification
Storage:    chrome.storage.local (OAuth token, client list cache)
Tech stack: TypeScript, Chrome Manifest V3, chrome.identity.launchWebAuthFlow, Notion API
```

---

## Example 71

**Intent:**
google calendar add-on that shows how many hours of meetings i have this week

**Spec:**
```
Type:       Plugin (Google Calendar add-on)
Features:   - Read events from the primary calendar for the current week
            - Sum meeting hours, excluding all-day and declined events
            - Show totals per day in a card on the sidebar
            - Compare with last week
            - Highlight days over a set limit
Tech stack: Google Apps Script, CardService, CalendarApp
```

---

## Example 72

**Intent:**
chrome extension to save youtube video timestamps with notes

**Spec:**
```
Type:       Browser extension (productivity)
Data model: VideoNote(video_id, video_title, timestamp_seconds, note, created_at)
Features:   - Add a "Add note" button under the YouTube player
            - Save the current time with a typed note
            - List notes for the video with clickable timestamps that seek the player
            - Show all notes across videos in the popup
            - Export notes as Markdown
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 73

**Intent:**
VS Code: show the size of imported npm packages next to the import line

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Parse import and require statements in JS/TS files
            - Look up each package's minified and gzipped size from a size API
            - Show the size as an inline decoration after the line
            - Colour the text green, yellow or red by size
            - Cache results per package version
Storage:    VS Code globalState (size cache)
Tech stack: TypeScript, VS Code Extension API (TextEditorDecorationType), Bundlephobia API
```

---

## Example 74

**Intent:**
Excel add in for invoice numbering, every time I click it gives next number and saves it

**Spec:**
```
Type:       Plugin (Excel add-in)
Features:   - Add a ribbon button "Next invoice number"
            - Read the last used number from a hidden settings sheet
            - Write the next number with a prefix (e.g. INV-2026-0042) into the selected cell
            - Save the new number back
            - Let the user set the prefix and starting number in a task pane
Storage:    Hidden worksheet in the workbook
Tech stack: JavaScript, Office Add-ins (Office.js, Excel JavaScript API, ribbon commands)
```

---

## Example 75

**Intent:**
webpage word counter extension

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Count words and characters in the selected text
            - Count words of the whole page's main article if nothing is selected
            - Show reading time estimate
            - Show results in the popup
Tech stack: JavaScript, Chrome Manifest V3, chrome.scripting.executeScript, Mozilla Readability
```

---

## Example 76

**Intent:**
Chrome extension that automatically switches to dark mode at sunset.

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Calculate sunrise and sunset from the user's location
            - Enable a dark stylesheet on all pages between sunset and sunrise
            - Re-check the schedule with chrome.alarms every 15 minutes
            - Allow a manual override from the popup
            - Let the user set a fixed schedule instead of sun times
Storage:    chrome.storage.sync (location, schedule, overrides)
Tech stack: JavaScript, Chrome Manifest V3, chrome.alarms, SunCalc library
```

---

## Example 77

**Intent:**
wordpress plugin that adds a table of contents to long posts from the headings

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Parse H2-H4 headings in the post content
            - Add anchor IDs to headings that lack them
            - Insert a collapsible table of contents before the first heading
            - Only add it to posts with at least 3 headings
            - Offer a [toc] shortcode and a setting to disable per post
Storage:    WordPress options table, post meta (per-post disable)
Tech stack: PHP, WordPress the_content filter, DOMDocument
```

---

## Example 78

**Intent:**
make my own firefox new tab with my bookmarks as big tiles

**Spec:**
```
Type:       Browser extension (new tab page)
Features:   - Replace the Firefox new tab page
            - Read a chosen bookmarks folder and show each bookmark as a tile with favicon
            - Drag tiles to reorder
            - Add a search box that searches bookmarks and the web
            - Choose tile size and background colour
Storage:    browser.storage.local (layout settings)
Tech stack: JavaScript, Firefox WebExtensions API (chrome_url_overrides, bookmarks API)
```

---

## Example 79

**Intent:**
A Gmail add-on to snooze-reply: write a reply now and have it sent tomorrow morning.

**Spec:**
```
Type:       Plugin (Gmail add-on)
Auth:       Google OAuth (Gmail compose and send scopes)
Data model: ScheduledReply(draft_id, thread_id, send_at)
Features:   - Show a compose action "Send later" with date/time options
            - Save the reply as a draft and store the scheduled time
            - Send due drafts with a time-driven trigger every minute
            - List and cancel scheduled replies in the add-on card
Storage:    Apps Script PropertiesService (scheduled list)
Tech stack: Google Apps Script, CardService (compose trigger), GmailApp, time-driven triggers
```

---

## Example 80

**Intent:**
I run a small online shop on Shopify and every time I add products I have to type the same SEO description pattern. Could an app fill SEO title and meta description for all products from a template like "{title} - handmade by Mia | Free shipping"?

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Data model: SeoTemplate(shop_domain, title_template, description_template)
Features:   - Let the merchant write templates with placeholders ({title}, {vendor}, {type}, {price})
            - Preview generated SEO text for a few products
            - Apply templates to all or selected products with bulk GraphQL mutations
            - Skip products that already have custom SEO text unless overwrite is checked
            - Apply templates to new products via the products/create webhook
API:        Shopify Admin GraphQL API
Storage:    SQLite via Prisma (templates)
Tech stack: Node.js, Shopify CLI, Remix, Polaris, Shopify webhooks
```

---

## Example 81

**Intent:**
highlight all external links on a page with a little icon

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Find links whose host differs from the current page's host
            - Append an external-link icon to them
            - Optionally make external links open in a new tab
            - Toggle per site from the popup
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 82

**Intent:**
vs code extension to see my leetcode problems and submit from editor

**Spec:**
```
Type:       Plugin (VS Code extension)
Auth:       Session cookie from the user's browser login, stored in SecretStorage
Features:   - List problems by difficulty and tag in a sidebar tree view
            - Open a problem's description in a webview and create a solution file
            - Run the solution against sample tests through the site's API
            - Submit the solution and show the verdict
            - Mark solved problems with a checkmark
Storage:    VS Code SecretStorage (session), local workspace folder (solution files)
Tech stack: TypeScript, VS Code Extension API, LeetCode GraphQL API
```

---

## Example 83

**Intent:**
chrome extension that blocks ads on news sites but lets me whitelist the ones i like

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Block requests to known ad and tracker domains with static filter lists
            - Hide leftover empty ad containers with cosmetic CSS filters
            - Whitelist the current site from the popup
            - Show the number of blocked requests per page on the badge
Storage:    chrome.storage.sync (whitelist)
Tech stack: JavaScript, Chrome Manifest V3, declarativeNetRequest (static rulesets and allowAllRequests rules), EasyList
```

---

## Example 84

**Intent:**
figma plugin to generate a color palette from one base color

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Pick a base colour in the plugin UI
            - Generate tints and shades (50-900 scale) in OKLCH
            - Show the palette with contrast ratios against white and black
            - Create colour styles or variables in the file
            - Draw swatches as rectangles on the canvas
Tech stack: TypeScript, Figma Plugin API, culori library, Svelte UI
```

---

## Example 85

**Intent:**
As a librarian I need a simple add-on in Google Sheets: I paste ISBN numbers and it fills title, author, publisher and year.

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Add a menu item "Fill book details"
            - Read ISBNs from the selected range
            - Look up each ISBN in a book metadata API
            - Write title, author, publisher and year into the next columns
            - Mark rows not found in red
Tech stack: Google Apps Script, UrlFetchApp, Open Library Books API
```

---

## Example 86

**Intent:**
i want an extension where i can save recipes from any website into one place, without all the long stories

**Spec:**
```
Type:       Browser extension (productivity)
Data model: Recipe(id, title, source_url, image_url, ingredients, steps, saved_at)
Features:   - Extract the recipe from schema.org Recipe JSON-LD on the page
            - Show a clean preview with ingredients and steps only
            - Save the recipe to a list in the extension
            - View saved recipes on an extension page with search
            - Print a recipe in a simple layout
Storage:    IndexedDB (via Dexie.js)
Tech stack: TypeScript, Chrome Manifest V3, content script, Dexie.js
```

---

## Example 87

**Intent:**
Outlook add-in to insert email templates

**Spec:**
```
Type:       Plugin (Outlook add-in)
Data model: Template(id, name, subject, body_html)
Features:   - Show saved templates in a task pane while composing
            - Insert a template's body at the cursor and optionally set the subject
            - Create, edit and delete templates
            - Fill placeholders like {first_name} from the recipient
Storage:    Office roamingSettings
Tech stack: TypeScript, Office Add-ins (Office.js, Outlook compose API), React, Fluent UI
```

---

## Example 88

**Intent:**
Can you make a Notion widget for a habit tracker I can embed in a page?

**Spec:**
```
Type:       Web application (embeddable widget)
Data model: Habit(id, widget_id, name, color)
            CheckIn(habit_id -> Habit, date)
Features:   - Show habits as a grid of the last 30 days
            - Toggle a day's check-in by clicking
            - Show current and longest streak per habit
            - Generate a unique embed URL that is pasted into Notion with /embed
API:        REST
            GET /api/widgets/{id}/habits
            POST /api/habits/{id}/checkins
            DELETE /api/habits/{id}/checkins/{date}
Storage:    Supabase (PostgreSQL)
Tech stack: Next.js, React, Supabase
```

---

## Example 89

**Intent:**
chrome ext for job hunting, save job posts from linkedin and indeed into a tracker with status

**Spec:**
```
Type:       Browser extension (productivity)
Data model: JobApplication(id, title, company, location, url, source, status, applied_at, notes)
Features:   - Add a "Save job" button on job post pages
            - Extract title, company and location from the page
            - Track status (saved, applied, interview, offer, rejected) in a kanban board page
            - Add notes and follow-up dates
            - Export the tracker as CSV
Storage:    chrome.storage.local
Tech stack: TypeScript, Chrome Manifest V3, content scripts, React (options page)
```

---

## Example 90

**Intent:**
a jetbrains plugin that shows git blame info at end of the current line

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Get blame data for the open file from the VCS integration
            - Show author, relative date and commit summary as an inlay at the end of the caret line
            - Show full commit details in a popup on hover
            - Let the user turn it off or change the format
Tech stack: Kotlin, IntelliJ Platform SDK (EditorCustomElementRenderer, Git4Idea)
```

---

## Example 91

**Intent:**
Simple extension to make my Chrome popup windows always on top? If not possible, then picture-in-picture for any video.

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Find the largest playing video on the page
            - Open it in picture-in-picture with one toolbar click
            - Add a keyboard shortcut to toggle picture-in-picture
            - Enable picture-in-picture on sites that disable it with disablePictureInPicture
Tech stack: JavaScript, Chrome Manifest V3, chrome.scripting, Picture-in-Picture Web API
```

---

## Example 92

**Intent:**
woo plugin to export orders to csv every night and email it to accounting

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Schedule a daily WP-Cron event at a configured time
            - Query completed orders from the last 24 hours
            - Build a CSV with order number, date, customer, totals and tax
            - Email the CSV as an attachment to configured addresses
            - Allow a manual export from the admin
Storage:    WordPress options table (settings), uploads folder (temporary CSV)
Tech stack: PHP, WooCommerce CRUD (wc_get_orders), WP-Cron, wp_mail
```

---

## Example 93

**Intent:**
Tampermonkey style userscript manager but simpler, just for me

**Spec:**
```
Type:       Browser extension (developer tools)
Data model: UserScript(id, name, match_patterns, code, enabled)
Features:   - Create and edit scripts in a code editor on the options page
            - Register enabled scripts for matching URLs with the userScripts API
            - Enable or disable scripts from the popup
            - Import and export scripts as .user.js files
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, chrome.userScripts API, CodeMirror 6
```

---

## Example 94

**Intent:**
when i paste in google docs it keeps the ugly formatting, add-on to clean it

**Spec:**
```
Type:       Plugin (Google Docs add-on)
Features:   - Add a menu item "Clean formatting" for the selection or the whole document
            - Reset font family and size to the document's normal text style
            - Remove background colours and odd text colours
            - Remove empty paragraphs and double spaces
            - Keep bold, italic and links
Tech stack: Google Apps Script, DocumentApp
```

---

## Example 95

**Intent:**
VS Code extension that shows a pomodoro timer in the status bar

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Start, pause and reset a pomodoro from the status bar item or command palette
            - Show remaining minutes in the status bar
            - Show a notification when work or break time ends
            - Configure work and break durations
            - Count completed pomodoros per day
Storage:    VS Code globalState
Tech stack: TypeScript, VS Code Extension API (StatusBarItem, window.showInformationMessage)
```

---

## Example 96

**Intent:**
Ich möchte eine Erweiterung, die mir zeigt, ob ein Online-Shop seriös ist, before I buy something. Sorry, mixing German.

**Spec:**
```
Type:       Browser extension (shopping)
Features:   - Detect shop pages by checkout or cart elements
            - Check the domain age via WHOIS through a backend
            - Check for an imprint (Impressum), HTTPS and known trust seals
            - Look up the shop in a list of reported fake shops
            - Show a traffic-light rating in the toolbar badge with reasons in the popup
API:        REST
            GET /check?domain={domain}
Storage:    Redis (backend cache of checks)
Tech stack: JavaScript, Chrome Manifest V3, content script, Python + FastAPI backend, python-whois
```

---

## Example 97

**Intent:**
plugin for game mod: a mod manager desktop app where i can enable/disable mods and it handles load order

**Spec:**
```
Type:       Desktop application (mod manager)
Data model: Mod(id, name, version, folder_path, enabled, load_order)
            Profile(id, name, enabled_mod_ids)
Features:   - Scan a game's mods folder and read each mod's manifest
            - Enable or disable mods by moving them between active and disabled folders
            - Reorder load order with drag and drop and save it to a load-order file
            - Detect file conflicts between mods
            - Switch between saved mod profiles
Storage:    Local JSON file (profiles), game folder
Tech stack: C#, .NET 8, Avalonia UI
```

---

## Example 98

**Intent:**
Chrome extension that summarises the article I'm reading

**Spec:**
```
Type:       Browser extension (reading)
Auth:       User-supplied LLM API key stored in chrome.storage.local
Features:   - Extract the main article text with Readability
            - Send the text to an LLM API with a summary prompt
            - Show a bullet summary in the side panel
            - Choose summary length (short, medium, detailed)
            - Copy the summary
Tech stack: TypeScript, Chrome Manifest V3, chrome.sidePanel, Mozilla Readability, OpenAI API
```

---

## Example 99

**Intent:**
chrome extension, autofill my address on shipping forms

**Spec:**
```
Type:       Browser extension (shopping)
Data model: AddressProfile(id, label, full_name, street, city, postal_code, country, phone, email)
Features:   - Save several address profiles on the options page
            - Detect shipping form fields by name, autocomplete and label
            - Fill the form from the chosen profile via the popup
            - Trigger input and change events so site validation works
Storage:    chrome.storage.local (encrypted with a user passphrase via Web Crypto)
Tech stack: JavaScript, Chrome Manifest V3, chrome.scripting, Web Crypto API
```

---

## Example 100

**Intent:**
close duplicate tabs

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Detect tabs with the same URL (ignoring hash and tracking parameters)
            - Close duplicates and keep the oldest or the active one
            - Run automatically when a new tab loads or on demand from the popup
            - Show how many duplicates were closed
Storage:    chrome.storage.sync (settings)
Tech stack: JavaScript, Chrome Manifest V3, chrome.tabs API
```

---

## Example 101

**Intent:**
color picker from any webpage

**Spec:**
```
Type:       Browser extension (developer tools)
Data model: PickedColor(hex, picked_at, page_url)
Features:   - Pick a colour from anywhere on screen with the EyeDropper API
            - Show the colour as HEX, RGB and HSL
            - Copy any format with one click
            - Keep a history of the last 20 colours
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, EyeDropper API
```

---

## Example 102

**Intent:**
chrome extension that groups my tabs by website automatically

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Group tabs that share the same domain into a tab group
            - Name and colour each group after the site
            - Regroup when new tabs open
            - Ignore pinned tabs
            - Collapse all groups with one popup button
Storage:    chrome.storage.sync (settings)
Tech stack: JavaScript, Chrome Manifest V3, chrome.tabGroups and chrome.tabs APIs
```

---

## Example 103

**Intent:**
show qr code of current page so i can open it on my phone

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Generate a QR code for the active tab's URL in the popup
            - Generate a QR code for selected text or a link via the context menu
            - Download the QR code as PNG
            - Adjust size
Tech stack: JavaScript, Chrome Manifest V3, qrcode-generator library
```

---

## Example 104

**Intent:**
Extension that converts prices on foreign shopping sites into my currency as I browse.

**Spec:**
```
Type:       Browser extension (shopping)
Features:   - Find price strings with currency symbols or codes in page text
            - Convert them to the user's home currency using daily rates
            - Show the converted value in brackets next to the original price
            - Refresh rates once a day in the service worker
            - Let the user pick the home currency
Storage:    chrome.storage.local (rates cache, settings)
Tech stack: JavaScript, Chrome Manifest V3, content script, chrome.alarms, Frankfurter API
```

---

## Example 105

**Intent:**
timezone thing - when i see "3pm EST" on a page, show it in my time

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Detect times with time zone abbreviations or UTC offsets in page text
            - Convert them to the user's local time zone
            - Show the local time in a tooltip on hover
            - Handle daylight saving correctly
            - Allow turning it off per site
Tech stack: TypeScript, Chrome Manifest V3, content script, Luxon
```

---

## Example 106

**Intent:**
im a web dev and i always need to test how my site looks on phone, tablet, desktop at the same time, extension that shows all sizes side by side would be great

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Open an extension page showing the current URL in several iframes at device widths
            - Provide presets for common phones, tablets and desktops
            - Sync scrolling across all frames
            - Remove X-Frame-Options and frame-ancestors headers for the tested site so it can be framed
            - Take a screenshot of all views
Tech stack: TypeScript, Chrome Manifest V3, declarativeNetRequest (modifyHeaders), React
```

---

## Example 107

**Intent:**
chrome extension to edit cookies for testing

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - List cookies for the current site in the popup
            - Edit name, value, domain, path, expiry and flags
            - Add and delete cookies
            - Export and import cookies as JSON
            - Search cookies by name
Tech stack: JavaScript, Chrome Manifest V3, chrome.cookies API, Vue 3
```

---

## Example 108

**Intent:**
modify request headers extension for api testing

**Spec:**
```
Type:       Browser extension (developer tools)
Data model: HeaderProfile(id, name, url_filter, headers[name, value, operation], enabled)
Features:   - Create profiles with request headers to add, change or remove
            - Limit a profile to URL patterns
            - Toggle profiles on and off from the popup
            - Apply headers with dynamic declarativeNetRequest rules
            - Show a badge when a profile is active
Storage:    chrome.storage.local
Tech stack: TypeScript, Chrome Manifest V3, declarativeNetRequest (modifyHeaders)
```

---

## Example 109

**Intent:**
An extension that checks all the links on a page and highlights broken ones in red.

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Collect all anchor URLs on the current page
            - Send HEAD requests (falling back to GET) from the service worker with limited concurrency
            - Mark broken links (4xx, 5xx, network error) in red and redirects in orange
            - Show a summary list in the popup
            - Export results as CSV
Tech stack: JavaScript, Chrome Manifest V3, service worker fetch, host permissions <all_urls>
```

---

## Example 110

**Intent:**
twitter/x thread reader, unroll threads into one page

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Detect when the user opens a post that starts a thread by the same author
            - Collect the author's consecutive replies from the page as it loads
            - Show the full thread as one clean article in a reader overlay
            - Copy the thread as plain text or Markdown
Tech stack: JavaScript, Chrome Manifest V3, content script with MutationObserver
```

---

## Example 111

**Intent:**
Hide comments sections everywhere, they ruin my mood.

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Hide comment sections on popular sites with site-specific CSS selectors
            - Hide generic elements with ids or classes like "comments" or "disqus_thread"
            - Add a "Show comments" button to reveal them on a page
            - Let the user add custom selectors
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 112

**Intent:**
recipe extension that scales ingredient amounts when i change servings

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Read recipeIngredient and recipeYield from schema.org JSON-LD
            - Parse quantities including fractions like 1 1/2 and ½
            - Show a servings selector above the ingredient list
            - Rewrite quantities on the page for the chosen servings
            - Convert between metric and imperial units
Tech stack: TypeScript, Chrome Manifest V3, content script
```

---

## Example 113

**Intent:**
track my packages in one place - extension that detects tracking numbers on order pages

**Spec:**
```
Type:       Browser extension (shopping)
Data model: Shipment(tracking_number, carrier, label, last_status, last_checked_at)
Features:   - Detect tracking numbers in pages and emails viewed in the browser using carrier regex patterns
            - Save a shipment with one click
            - Check status periodically through a tracking API
            - Notify on status changes like "Out for delivery"
            - List all shipments in the popup
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, chrome.alarms, chrome.notifications, AfterShip API
```

---

## Example 114

**Intent:**
Wishlist extension where I save products from different shops and see them in one list with their prices.

**Spec:**
```
Type:       Browser extension (shopping)
Data model: WishItem(id, title, price, currency, image_url, url, shop, added_at)
Features:   - Save the current product from the popup using Open Graph and schema.org Product data
            - Show all items in a grid on a dashboard page
            - Re-check prices weekly and show changes
            - Sort by shop, price or date
            - Share the list as a read-only link
API:        REST
            POST /lists
            GET /lists/{share_id}
Storage:    chrome.storage.local (items), Firebase Firestore (shared lists)
Tech stack: TypeScript, Chrome Manifest V3, chrome.alarms, Firebase
```

---

## Example 115

**Intent:**
fake review detector for product pages

**Spec:**
```
Type:       Browser extension (shopping)
Features:   - Collect review text, ratings and dates from the product page
            - Send them to a backend scoring model
            - Flag suspicious patterns (bursts of 5-star reviews on the same days, repeated phrases, very short reviews)
            - Show an adjusted rating and a trust grade near the stars
API:        REST
            POST /analyze
Tech stack: JavaScript, Chrome Manifest V3, content script, Python FastAPI backend, scikit-learn
```

---

## Example 116

**Intent:**
vscode extension: mask values in .env files so they dont show when I share my screen

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Detect .env and .env.* files when opened
            - Cover values after the = sign with a decoration that shows asterisks
            - Reveal a value on hover or with a toggle command
            - Add a status bar toggle to mask or unmask all
Tech stack: TypeScript, VS Code Extension API (TextEditorDecorationType, HoverProvider)
```

---

## Example 117

**Intent:**
VS Code extension that sorts Tailwind classes in the right order when I save.

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Find class and className attribute values in HTML, JSX, Vue and Svelte files
            - Sort classes in Tailwind's recommended order using the project's tailwind config
            - Remove duplicate classes
            - Apply on save when enabled in settings
            - Provide a manual "Sort classes" command
Tech stack: TypeScript, VS Code Extension API (onWillSaveTextDocument, TextEdit), tailwindcss package
```

---

## Example 118

**Intent:**
a vs code extension to view csv files as a table

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Register a custom editor for .csv and .tsv files
            - Show data in a sortable, filterable table in a webview
            - Detect the delimiter automatically
            - Edit cells and write the changes back to the file
            - Handle large files with virtual scrolling
Tech stack: TypeScript, VS Code Extension API (CustomTextEditorProvider, webview), Papa Parse, AG Grid
```

---

## Example 119

**Intent:**
VS Code extension for i18n: when I hover a translation key like t('home.title') show the English text

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Find translation JSON files in a configured locales folder
            - Show the translated value for the key under the cursor in a hover
            - Show the value inline after the key as a faded decoration
            - Warn about keys missing from any locale
            - Offer a quick fix to add a missing key
Tech stack: TypeScript, VS Code Extension API (HoverProvider, DiagnosticCollection, CodeActionProvider)
```

---

## Example 120

**Intent:**
I want an extension in vs code that formats SQL inside python strings

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Detect string literals that start with SQL keywords or are tagged with a # sql comment
            - Format the SQL with consistent keyword case and indentation
            - Keep the string's quote style and indentation level
            - Run via a command or code action on the selection
Tech stack: TypeScript, VS Code Extension API (CodeActionProvider), sql-formatter
```

---

## Example 121

**Intent:**
color the log files in vscode, errors red warnings yellow

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Register a "log" language for .log files
            - Highlight ERROR, WARN, INFO and DEBUG levels with a TextMate grammar
            - Highlight timestamps, IP addresses, URLs and quoted strings
            - Add a command to filter the view to only error lines
Tech stack: TypeScript, VS Code Extension API, TextMate grammar (JSON)
```

---

## Example 122

**Intent:**
VS Code extension to bookmark lines and jump between them

**Spec:**
```
Type:       Plugin (VS Code extension)
Data model: Bookmark(file_uri, line, label)
Features:   - Toggle a bookmark on the current line with a shortcut
            - Show a gutter icon on bookmarked lines
            - Jump to next or previous bookmark
            - List all bookmarks in a sidebar view
            - Keep bookmark lines correct when text above them changes
Storage:    VS Code workspaceState
Tech stack: TypeScript, VS Code Extension API
```

---

## Example 123

**Intent:**
JetBrains plugin that translates selected text between English and Chinese

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Add a "Translate" action to the editor context menu
            - Detect the language of the selection
            - Show the translation in a popup
            - Replace the selection with the translation via an alternate action
            - Configure the translation service and API key
Storage:    IntelliJ PasswordSafe (API key), PersistentStateComponent (settings)
Tech stack: Kotlin, IntelliJ Platform SDK, DeepL API
```

---

## Example 124

**Intent:**
PyCharm plugin that runs pytest for the test function under my cursor with a hotkey

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Find the test function or class at the caret using PSI
            - Create and run a pytest run configuration for it
            - Re-run the last test with a second shortcut
            - Show pass/fail result in a notification
Tech stack: Kotlin, IntelliJ Platform SDK (PSI, RunManager), Python plugin API
```

---

## Example 125

**Intent:**
WordPress maintenance mode plugin

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Show a maintenance page to visitors who are not logged in
            - Return HTTP 503 with a Retry-After header
            - Let admins customise heading, text, logo and background
            - Allow access for chosen IP addresses
            - Show a notice in the admin bar while maintenance mode is on
Storage:    WordPress options table
Tech stack: PHP, WordPress hooks (template_redirect), Settings API
```

---

## Example 126

**Intent:**
wordpress plugin to manage 301 redirects

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Redirect(id, source_path, target_url, status_code, hits, last_hit_at)
Features:   - Add, edit and delete redirects in an admin table
            - Match exact paths or regular expressions
            - Redirect early on the template_redirect hook
            - Count hits per redirect
            - Log 404 errors and create a redirect from a logged 404
Storage:    Custom MySQL table via $wpdb
Tech stack: PHP, WordPress hooks, WP_List_Table
```

---

## Example 127

**Intent:**
related posts plugin for WP that shows 3 similar articles at the bottom

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Find posts sharing the most tags and categories with the current post
            - Show 3 related posts with thumbnail and title after the content
            - Cache results with transients
            - Provide a block and a [related_posts] shortcode
            - Exclude chosen categories
Storage:    WordPress transients
Tech stack: PHP, WP_Query, WordPress Block API
```

---

## Example 128

**Intent:**
My photography blog has hundreds of images without alt text, which is bad for blind visitors and SEO. A plugin that generates alt text with AI for my media library would save me weeks.

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Find images in the media library with empty alt text
            - Send each image to a vision model to generate a short description
            - Save the description to the _wp_attachment_image_alt meta
            - Process images in background batches with Action Scheduler
            - Let the admin review and edit generated alt text before publishing
            - Generate alt text automatically on upload
Storage:    WordPress post meta, options table (API key)
Tech stack: PHP, WordPress hooks, Action Scheduler, OpenAI vision API
```

---

## Example 129

**Intent:**
GDPR cookie banner for wordpress that actually blocks google analytics until consent

**Spec:**
```
Type:       Plugin (WordPress)
Data model: ConsentLog(id, consent_id, categories, ip_hash, created_at)
Features:   - Show a consent banner with accept, reject and settings options
            - Store consent per category (necessary, analytics, marketing) in a cookie
            - Block registered scripts by changing their type to text/plain until consent
            - Load blocked scripts after consent without reload
            - Log consent records for compliance
Storage:    Custom MySQL table (consent log), WordPress options (settings)
Tech stack: PHP, WordPress script_loader_tag filter, vanilla JavaScript
```

---

## Example 130

**Intent:**
custom login page wp plugin with my logo

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Replace the WordPress logo on wp-login.php with an uploaded logo
            - Set background image and colours
            - Change the logo link to the site's home page
            - Add custom CSS from the settings page
Storage:    WordPress options table
Tech stack: PHP, WordPress hooks (login_enqueue_scripts, login_headerurl), Media uploader
```

---

## Example 131

**Intent:**
Plugin to duplicate pages and posts in WordPress with one click.

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Add a "Duplicate" link to post and page row actions
            - Copy title, content, excerpt, taxonomies and custom fields
            - Save the copy as a draft
            - Redirect to edit the new draft
            - Restrict the action to users who can edit posts
Tech stack: PHP, WordPress hooks (post_row_actions, admin_action_), wp_insert_post
```

---

## Example 132

**Intent:**
wordpress events calendar plugin for my church, events with date time and place, show upcoming on homepage

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Event(title, description, start_at, end_at, location, recurring_rule)
Features:   - Register an Event post type with date, time and location fields
            - Show a monthly calendar view with a shortcode
            - Show the next 5 upcoming events in a widget
            - Support weekly recurring events
            - Add an "Add to calendar" .ics download link
Storage:    WordPress database (posts, post meta)
Tech stack: PHP, WordPress hooks, FullCalendar.js
```

---

## Example 133

**Intent:**
testimonials slider wordpress

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Testimonial(quote, author_name, author_role, photo, rating)
Features:   - Register a Testimonial post type
            - Show testimonials in an auto-playing, swipeable slider
            - Provide a block with options for speed and number shown
            - Show star ratings
            - Add Review schema markup
Storage:    WordPress database
Tech stack: PHP, WordPress Block API, Swiper.js
```

---

## Example 134

**Intent:**
Shopify back in stock alerts app

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Data model: StockAlert(id, shop_domain, variant_id, email, created_at, notified_at)
Features:   - Show a "Notify me" form on sold-out variants via a theme app extension
            - Save the customer's email for the variant
            - Listen to inventory_levels/update webhooks
            - Email subscribers when the variant is back in stock
            - Show signup counts per product in the admin
API:        REST
            POST /apps/alerts/subscribe (app proxy)
Storage:    PostgreSQL
Tech stack: Node.js, Shopify CLI, Remix, Theme App Extension, App Proxy, SendGrid
```

---

## Example 135

**Intent:**
shopify size chart app

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Data model: SizeChart(id, shop_domain, name, table_json, unit)
            ChartAssignment(chart_id -> SizeChart, collection_id, product_type)
Features:   - Build size charts with a table editor in the admin
            - Assign charts to collections or product types
            - Show a "Size guide" link that opens the chart in a modal on product pages
            - Toggle between cm and inches
Storage:    Shopify metaobjects
Tech stack: Node.js, Shopify CLI, Remix, Polaris, Theme App Extension
```

---

## Example 136

**Intent:**
age verification popup on my shopify store (we sell wine)

**Spec:**
```
Type:       Plugin (Shopify app)
Features:   - Show a full-screen "Are you 18+?" modal on first visit
            - Remember confirmation in a cookie for 30 days
            - Redirect visitors who decline to a configured URL
            - Let the merchant set minimum age, text and logo
Tech stack: Shopify Theme App Extension (app embed block), Liquid, JavaScript
```

---

## Example 137

**Intent:**
Shopify app: product reviews with photos, customers get an email a week after delivery asking for review

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Data model: Review(id, shop_domain, product_id, order_id, rating, body, photo_urls, status, created_at)
            ReviewRequest(order_id, send_at, sent_at)
Features:   - Schedule a review request email 7 days after fulfillment via the fulfillments/create webhook
            - Let customers submit a rating, text and photos from a link
            - Moderate reviews in the admin before publishing
            - Show reviews and average rating in a theme app block
            - Add product rating structured data
Storage:    PostgreSQL, Amazon S3 (photos)
Tech stack: Node.js, Shopify CLI, Remix, BullMQ, Postmark, Theme App Extension
```

---

## Example 138

**Intent:**
figma plugin to insert icons from a big free icon library by searching

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Search an icon set by keyword in the plugin UI
            - Show results as a grid of previews
            - Insert the clicked icon as an SVG vector node at the viewport centre
            - Choose size, stroke width and colour before inserting
Tech stack: TypeScript, Figma Plugin API (createNodeFromSvg), Iconify API
```

---

## Example 139

**Intent:**
Figma plugin that creates a layout grid of 12 columns automatically for any frame

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Apply a column layout grid to the selected frames
            - Let the user set columns, gutter and margin
            - Provide presets for desktop, tablet and mobile
            - Add a baseline row grid optionally
            - Save custom presets
Storage:    figma.clientStorage (presets)
Tech stack: TypeScript, Figma Plugin API (layoutGrids)
```

---

## Example 140

**Intent:**
figma plugin that exports my frames as react components

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Read the selected frame's node tree
            - Convert auto layout frames to flexbox divs and text to elements
            - Map fills, strokes, radius and typography to Tailwind classes
            - Export images as assets
            - Show the generated JSX with a copy button
Tech stack: TypeScript, Figma Plugin API, Prettier (standalone)
```

---

## Example 141

**Intent:**
sync design tokens from figma variables to github

**Spec:**
```
Type:       Plugin (Figma plugin)
Auth:       GitHub personal access token stored in figma.clientStorage
Features:   - Read variable collections and modes from the file
            - Convert them to W3C design token JSON
            - Create a branch and commit the tokens file to a repository
            - Open a pull request with a summary of changed tokens
Tech stack: TypeScript, Figma Plugin API (variables), GitHub REST API
```

---

## Example 142

**Intent:**
spell checker for figma text layers

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Collect text from all text layers on the current page
            - Check spelling with a dictionary for the chosen language
            - List misspelled words with the layer they appear in
            - Replace a word with a suggestion directly in the layer
            - Ignore words added to a personal dictionary
Storage:    figma.clientStorage (personal dictionary)
Tech stack: TypeScript, Figma Plugin API, nspell with Hunspell dictionaries
```

---

## Example 143

**Intent:**
fill figma image placeholders with random photos by keyword

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Take a keyword such as "coffee" in the plugin UI
            - Fetch matching photos from a stock photo API
            - Fill each selected shape with a different photo as an image fill
            - Keep the shape's crop mode as fill
Tech stack: TypeScript, Figma Plugin API (createImage), Unsplash API
```

---

## Example 144

**Intent:**
Make charts in figma from a CSV

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Paste or upload CSV data in the plugin UI
            - Choose bar, line or pie chart
            - Draw the chart with editable vector shapes and text labels
            - Apply colours from the file's colour styles
            - Redraw the chart when the data changes
Tech stack: TypeScript, Figma Plugin API, d3-scale, Papa Parse
```

---

## Example 145

**Intent:**
obsidian flashcards plugin, I write Q::A in notes and it quizzes me with spaced repetition

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Data model: Card(id, note_path, question, answer, ease, interval_days, due_date)
Features:   - Parse "question::answer" lines from notes
            - Schedule reviews with the SM-2 algorithm
            - Show a review modal with show-answer and again/hard/good/easy buttons
            - Show number of due cards in the status bar
            - Update cards when notes change
Storage:    Obsidian plugin data.json
Tech stack: TypeScript, Obsidian Plugin API
```

---

## Example 146

**Intent:**
obsidian kanban board from my task notes pls

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Collect tasks (- [ ] lines) from notes in a chosen folder
            - Show them on a kanban board view with columns by #status tag
            - Drag a card to another column and update the tag in the source note
            - Open the source note when a card is clicked
            - Add a new task from a column
Tech stack: TypeScript, Obsidian Plugin API (ItemView, Vault.process), SortableJS
```

---

## Example 147

**Intent:**
i want my kindle highlights in obsidian automaticaly, one note per book

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Data model: BookNote(title, author, asin, highlights[text, location, note])
Features:   - Import highlights from the Kindle "My Clippings.txt" file
            - Group highlights by book and create one note per book
            - Add highlights as blockquotes with location numbers
            - Append only new highlights on re-import
            - Use a configurable note template
Storage:    Obsidian vault (Markdown notes), plugin data.json (imported highlight hashes)
Tech stack: TypeScript, Obsidian Plugin API
```

---

## Example 148

**Intent:**
obsidian git backup every 10 min

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Commit all vault changes every N minutes with a timestamp message
            - Pull before push to avoid conflicts
            - Push to a configured remote
            - Show last backup time in the status bar
            - Notify on errors such as merge conflicts
Storage:    Git repository (vault folder)
Tech stack: TypeScript, Obsidian Plugin API, isomorphic-git (desktop and mobile)
```

---

## Example 149

**Intent:**
An Obsidian plugin that suggests tags for a note using AI based on its content and my existing tags.

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Auth:       User's LLM API key in plugin settings
Features:   - Collect all existing tags in the vault
            - Send the note content and tag list to an LLM
            - Show suggested tags in a modal with checkboxes
            - Add the chosen tags to the note's frontmatter
            - Prefer existing tags over new ones
Storage:    Obsidian plugin data.json (settings)
Tech stack: TypeScript, Obsidian Plugin API (processFrontMatter), Anthropic Messages API
```

---

## Example 150

**Intent:**
obsidian - pull citations from zotero into my notes

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Read the Zotero library through the Better BibTeX local API
            - Search references with a fuzzy suggest modal
            - Insert a formatted citation and create a literature note from a template
            - Include title, authors, year, DOI and annotations
            - Update literature notes when annotations change
Tech stack: TypeScript, Obsidian Plugin API (FuzzySuggestModal), Zotero Better BibTeX JSON-RPC
```

---

## Example 151

**Intent:**
Mail merge in google sheets, send personalised emails to everyone in the list

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Choose a Gmail draft as the template
            - Replace {{Column Name}} placeholders with each row's values
            - Send emails to the address column with a daily quota check
            - Write "Sent" and timestamp to a status column
            - Skip rows already sent
Tech stack: Google Apps Script, GmailApp, SpreadsheetApp, HtmlService sidebar
```

---

## Example 152

**Intent:**
i do invoices in google sheets, want a button that makes a pdf invoice from the selected row and puts it in drive

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Read client, items, amounts and due date from the selected row
            - Copy a Google Docs invoice template and fill placeholders
            - Export the document as PDF into a Drive folder
            - Write the PDF link back to the row
            - Optionally email the PDF to the client
Tech stack: Google Apps Script, DocumentApp, DriveApp, MailApp
```

---

## Example 153

**Intent:**
translate a whole column in sheets to french

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Let the user select a source column and target language from a sidebar
            - Translate each cell with LanguageApp
            - Write translations to a new column next to the source
            - Process in batches to stay within execution time limits
            - Skip empty cells
Tech stack: Google Apps Script, LanguageApp, HtmlService
```

---

## Example 154

**Intent:**
For my school I need a Sheets add-on: teachers tick attendance with checkboxes and it calculates % per student and colors low ones.

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Create an attendance sheet with student names and one checkbox column per date
            - Add a new date column from a menu
            - Calculate each student's attendance percentage
            - Highlight students under 80% with conditional formatting
            - Build a monthly summary sheet
Tech stack: Google Apps Script, SpreadsheetApp (data validation, conditional format rules)
```

---

## Example 155

**Intent:**
Sheets add-on to categorize my bank transactions automaticaly by keywords

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Data model: CategoryRule(keyword, category)
Features:   - Store keyword-to-category rules in a "Rules" sheet
            - Match each transaction description against the rules
            - Fill the category column for uncategorised rows
            - Suggest new rules for frequent uncategorised merchants
            - Create a pivot summary by month and category
Tech stack: Google Apps Script, SpreadsheetApp
```

---

## Example 156

**Intent:**
generate qr codes in google sheets for every row link

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Read URLs from a selected column
            - Generate a QR code image for each URL
            - Insert the images into the adjacent cells with CellImageBuilder
            - Choose QR size and error correction level
Tech stack: Google Apps Script, QuickChart QR API, SpreadsheetApp
```

---

## Example 157

**Intent:**
regex extract custom function for sheets

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Add custom functions REGEX_ALL(text, pattern) and REGEX_GROUP(text, pattern, n)
            - Return all matches as a spilled array
            - Support flags like case-insensitive
            - Show function help in autocomplete with JSDoc
Tech stack: Google Apps Script (custom functions)
```

---

## Example 158

**Intent:**
google docs addon for citations APA MLA

**Spec:**
```
Type:       Plugin (Google Docs add-on)
Data model: Source(id, type, authors, title, year, publisher, url, doi)
Features:   - Search a source by DOI, ISBN or URL in a sidebar
            - Fill in source fields automatically from metadata APIs
            - Insert in-text citations at the cursor
            - Generate a formatted bibliography at the end of the document
            - Switch between APA and MLA styles
Storage:    Document properties (sources list)
Tech stack: Google Apps Script, DocumentApp, Crossref API, citation-js (bundled)
```

---

## Example 159

**Intent:**
Google Docs add-on that shows word count goal progress while I write my novel chapters.

**Spec:**
```
Type:       Plugin (Google Docs add-on)
Features:   - Let the user set a target word count for the document
            - Count words in the body excluding headings
            - Show a progress bar in the sidebar that refreshes every 30 seconds
            - Track words written per day
            - Show a celebration message when the goal is reached
Storage:    PropertiesService (document properties)
Tech stack: Google Apps Script, DocumentApp, HtmlService sidebar
```

---

## Example 160

**Intent:**
google slides add on that puts a countdown timer on the slide

**Spec:**
```
Type:       Plugin (Google Slides add-on)
Features:   - Insert a timer box on the current slide from the sidebar
            - Set the duration in minutes
            - Update the timer text every second while presenting from the sidebar controls
            - Change the box colour when time runs out
Tech stack: Google Apps Script, SlidesApp, HtmlService
```

---

## Example 161

**Intent:**
slides add-on to make quiz slides from a list of questions in a sheet

**Spec:**
```
Type:       Plugin (Google Slides add-on)
Features:   - Choose a Google Sheet with question, options and answer columns
            - Create one slide per question with options laid out as boxes
            - Add an answer slide after each question
            - Apply the presentation's theme and layouts
Tech stack: Google Apps Script, SlidesApp, SpreadsheetApp
```

---

## Example 162

**Intent:**
excel add-in that cleans data: trim spaces, fix capitals, remove empty rows

**Spec:**
```
Type:       Plugin (Excel add-in)
Features:   - Trim leading, trailing and double spaces in the selected range
            - Convert text to Proper, UPPER or lower case
            - Remove completely empty rows
            - Convert numbers stored as text into numbers
            - Preview the number of changes before applying
Tech stack: TypeScript, Office Add-ins (Excel JavaScript API), React task pane
```

---

## Example 163

**Intent:**
Excel add-in to split a class list into random groups of 4.

**Spec:**
```
Type:       Plugin (Excel add-in)
Features:   - Read student names from the selected column
            - Shuffle and split them into groups of a chosen size
            - Spread leftover students across groups
            - Write groups to a new sheet with headers
            - Reshuffle on button click
Tech stack: JavaScript, Office Add-ins (Excel JavaScript API)
```

---

## Example 164

**Intent:**
Hi, I am accountant from Poland, need add-in to Excel which check if NIP (tax number) in the column is correct and also take company name from government database.

**Spec:**
```
Type:       Plugin (Excel add-in)
Features:   - Validate each NIP in the selected column with the checksum algorithm
            - Mark invalid numbers in red
            - Query the government VAT whitelist API for valid numbers
            - Write company name and VAT status to the next columns
            - Show a summary of checked, invalid and inactive numbers
Tech stack: TypeScript, Office Add-ins (Excel JavaScript API), Polish Ministry of Finance White List API
```

---

## Example 165

**Intent:**
gmail unsubscribe helper, list all newsletters and unsubscribe in one click

**Spec:**
```
Type:       Plugin (Gmail add-on)
Auth:       Google OAuth (Gmail read and modify scopes)
Features:   - Find messages with a List-Unsubscribe header from the last 90 days
            - Group them by sender with message counts
            - Unsubscribe using one-click POST or mailto from the header
            - Archive or delete all past mail from the sender
            - Show results in a card list
Tech stack: Google Apps Script, CardService, Gmail advanced service
```

---

## Example 166

**Intent:**
Gmail add-on that labels emails from my clients automatically using a list in a spreadsheet

**Spec:**
```
Type:       Plugin (Gmail add-on)
Features:   - Read client names and email domains from a Google Sheet
            - Run on a 10-minute trigger over new inbox threads
            - Apply a label "Clients/<Name>" to matching threads
            - Create missing labels automatically
            - Show the client for the open email in a contextual card
Tech stack: Google Apps Script, GmailApp, SpreadsheetApp, CardService
```

---

## Example 167

**Intent:**
outlook add-in that saves the email as pdf to onedrive

**Spec:**
```
Type:       Plugin (Outlook add-in)
Auth:       Microsoft Entra ID single sign-on (Microsoft Graph Files.ReadWrite scope)
Features:   - Add a "Save as PDF" button to the message read surface
            - Convert the email body and headers to PDF
            - Upload the PDF to a chosen OneDrive folder through Microsoft Graph
            - Include attachments as separate files optionally
Tech stack: TypeScript, Office Add-ins (Office.js), Microsoft Graph API, Azure Function (PDF conversion with Puppeteer)
```

---

## Example 168

**Intent:**
outlook addin, translate the email im reading

**Spec:**
```
Type:       Plugin (Outlook add-in)
Features:   - Read the body of the selected message
            - Detect its language
            - Translate it into the user's preferred language
            - Show the translation in the task pane
            - Translate a reply draft back into the sender's language
Tech stack: JavaScript, Office Add-ins (Office.js), Azure AI Translator
```

---

## Example 169

**Intent:**
game modding tool: a simple level editor for my 2d platformer that saves levels as json

**Spec:**
```
Type:       Desktop application (level editor)
Data model: Level(name, width, height, tileset, tiles[][], entities[type, x, y, properties])
Features:   - Paint tiles on a grid with a tile palette
            - Place entities like enemies, coins and spawn points
            - Edit entity properties in a side panel
            - Save and load levels as JSON files
            - Test-play the level by launching the game with the file
Storage:    Local JSON files
Tech stack: Godot 4 (GDScript, editor run as a standalone tool)
```

---

## Example 170

**Intent:**
save file editor for the game i made, so testers can edit gold and level

**Spec:**
```
Type:       Desktop application (save editor)
Features:   - Open the game's save file and decode it (Base64 + JSON)
            - Show fields like gold, level, inventory and unlocked areas in a form
            - Validate values against allowed ranges
            - Save changes back with a backup of the original
            - Verify the save file checksum
Storage:    Local file system
Tech stack: Python, Tkinter
```

---

## Example 171

**Intent:**
texture pack tool - takes a folder of pngs, checks sizes and packs them into a zip mod

**Spec:**
```
Type:       Command-line tool (mod packaging)
Features:   - Check that every PNG is a power-of-two size and matches the expected texture names
            - Report missing or extra textures compared to a reference list
            - Generate a pack manifest with name, version and author
            - Package everything into a zip with the right folder structure
            - Create a preview thumbnail
Input:      Folder of PNG textures, reference texture list
Tech stack: Python, Pillow, zipfile, Click
```

---

## Example 172

**Intent:**
speedrun timer overlay for my games, splits with hotkeys

**Spec:**
```
Type:       Desktop application (speedrun timer)
Data model: Run(id, game_name, category, attempts)
            Split(run_id -> Run, name, best_time_ms, pb_time_ms)
Features:   - Start, split, undo and reset with global hotkeys
            - Show splits with time difference against personal best in green or red
            - Save personal bests and best segments
            - Show the timer in an always-on-top, transparent window for streaming
            - Import and export splits as JSON
Storage:    Local JSON files
Tech stack: Rust, egui (eframe), global-hotkey crate
```

---

## Example 173

**Intent:**
procedural dungeon map generator for tabletop games, export png

**Spec:**
```
Type:       Command-line tool (game tool)
Features:   - Generate a dungeon with rooms and corridors using BSP partitioning
            - Place doors, stairs and treasure markers
            - Accept a seed so maps can be recreated
            - Render the map as a grid PNG with optional numbering
            - Export room descriptions as Markdown
Input:      Map size, room count, seed
Tech stack: Python, Pillow, Click
```

---

## Example 174

**Intent:**
dice roller for online tabletop as browser extension, roll 2d6+3 from any page

**Spec:**
```
Type:       Browser extension (productivity)
Data model: RollResult(expression, rolls, total, rolled_at)
Features:   - Parse dice expressions like 2d6+3, 4d6kh3 and d20 advantage
            - Roll from the popup or by selecting text and using the context menu
            - Show each die result and the total
            - Keep a roll history
            - Copy the result as text for chat
Storage:    chrome.storage.local (history)
Tech stack: TypeScript, Chrome Manifest V3
```

---

## Example 175

**Intent:**
modding api for my unity game so players can add new weapons with json and pngs

**Spec:**
```
Type:       Desktop game (modding support)
Data model: WeaponMod(id, name, damage, fire_rate, ammo, sprite_file, sound_file)
Features:   - Load weapon definition JSON files from a mods folder at startup
            - Load sprites and sounds from the mod folder at runtime
            - Validate fields and skip broken mods with a log message
            - Add loaded weapons to the in-game shop and drop tables
            - Show a mods menu to enable or disable mods
Storage:    Local file system (StreamingAssets/Mods, persistent data path)
Tech stack: C#, Unity, Newtonsoft.Json, UnityWebRequest (loading images and audio)
```

---

## Example 176

**Intent:**
so basically i built a small multiplayer game server in node and some friends want to add custom game modes. i dont want them touching my code, so i want some kind of plugin system where they write a js file with hooks like onPlayerJoin, onTick, onChat and the server loads it

**Spec:**
```
Type:       Desktop game (server plugin system)
Features:   - Load plugin .js files from a plugins folder at startup
            - Call exported hooks (onLoad, onPlayerJoin, onTick, onChat) with a limited API object
            - Run each plugin in a separate worker thread with a time budget per tick
            - Let plugins send messages to players and change game state through API calls
            - Reload plugins with an admin command without restarting the server
Storage:    Local file system (plugins folder)
Tech stack: Node.js, worker_threads, ws (WebSocket server)
```

---

## Example 177

**Intent:**
vscode ext to preview markdown with mermaid diagrams

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Extend the built-in Markdown preview with a markdown-it plugin
            - Render ```mermaid code blocks as diagrams
            - Follow the editor's light or dark theme
            - Export a diagram as SVG or PNG
Tech stack: TypeScript, VS Code Extension API (markdown.markdownItPlugins, markdown.previewScripts), Mermaid
```

---

## Example 178

**Intent:**
VS Code snippets manager where I can save code snippets from selection and search them later

**Spec:**
```
Type:       Plugin (VS Code extension)
Data model: Snippet(id, title, language, body, tags, created_at)
Features:   - Save the selected code as a snippet with title and tags
            - Search snippets in a quick pick
            - Insert the chosen snippet at the cursor
            - Browse snippets by language in a tree view
            - Sync snippets through Settings Sync
Storage:    VS Code globalState (with setKeysForSync)
Tech stack: TypeScript, VS Code Extension API
```

---

## Example 179

**Intent:**
vs code extension that warns me when i'm committing a file with console.log in it

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Scan staged files for console.log, debugger and print statements
            - Show a warning dialog before commit from the Source Control view
            - List the offending lines in the Problems panel
            - Allow ignoring with a // keep-log comment
Tech stack: TypeScript, VS Code Extension API (vscode.git API, DiagnosticCollection)
```

---

## Example 180

**Intent:**
vscode extension for docker compose files: show which services are running and start/stop them

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Parse docker-compose.yml in the workspace
            - Show services with their status in a tree view
            - Start, stop and restart services from context menu actions
            - Stream service logs to an output channel
            - Add CodeLens "Up" and "Down" buttons above each service
Tech stack: TypeScript, VS Code Extension API, Docker CLI (docker compose), yaml package
```

---

## Example 181

**Intent:**
Python venv switcher in the vscode status bar

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Find virtual environments (.venv, venv, conda, poetry) in the workspace
            - Show the active environment in the status bar
            - Switch environment from a quick pick
            - Update the Python extension's interpreter setting
            - Create a new venv from a requirements file
Tech stack: TypeScript, VS Code Extension API, Python extension API
```

---

## Example 182

**Intent:**
spell check in code comments and strings, camelCase aware

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Split identifiers in camelCase and snake_case into words
            - Check words in comments, strings and identifiers against dictionaries
            - Show misspellings as diagnostics with suggestions
            - Add words to a workspace dictionary
            - Support programming-specific word lists
Storage:    Workspace settings (custom words)
Tech stack: TypeScript, VS Code Extension API, cspell-lib
```

---

## Example 183

**Intent:**
JetBrains plugin with rainbow colors for brackets

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Color matching brackets by nesting depth
            - Support round, square, curly and angle brackets
            - Let the user configure colours for light and dark themes
            - Support Java, Kotlin, JS, Python and XML
Tech stack: Kotlin, IntelliJ Platform SDK (Annotator, HighlightVisitor)
```

---

## Example 184

**Intent:**
intellij plugin that generates builder classes for java classes

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Add a "Generate > Builder" action in Java classes
            - Let the user choose fields in a dialog
            - Generate a static inner Builder class with fluent setters and build()
            - Regenerate and update the builder when fields change
Tech stack: Java, IntelliJ Platform SDK (PSI, PsiElementFactory, CodeInsightAction)
```

---

## Example 185

**Intent:**
Android Studio plugin that converts a hex color to a Compose Color() call

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Detect hex colour strings in Kotlin files
            - Offer an intention action to convert to Color(0xFFRRGGBB)
            - Show a colour swatch in the gutter
            - Convert colors in colors.xml to a Compose Color.kt file
Tech stack: Kotlin, IntelliJ Platform SDK (IntentionAction, LineMarkerProvider), Android Studio
```

---

## Example 186

**Intent:**
chrome extension to make google search ignore pinterest and quora results

**Spec:**
```
Type:       Browser extension (productivity)
Data model: BlockedSite(domain)
Features:   - Hide search results from blocked domains on Google result pages
            - Add a "Block this site" link to each result
            - Manage the blocked list in the popup
            - Show how many results were hidden
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 187

**Intent:**
extension: grayscale the web after 10pm to help me stop scrolling

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Apply a grayscale CSS filter to all pages during a configured time window
            - Update open tabs when the window starts or ends
            - Allow a one-time 15-minute pause
            - Exclude chosen sites
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, chrome.alarms, chrome.scripting
```

---

## Example 188

**Intent:**
zoom every website to 125% by default but remember sites i change

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Set a default zoom level for all sites
            - Remember per-site zoom when the user changes it
            - Apply zoom on tab update
            - Reset a site's zoom from the popup
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, chrome.tabs.setZoom, chrome.tabs.onZoomChange
```

---

## Example 189

**Intent:**
Extension for people with tremors: makes clickable things bigger and adds a confirm step for important buttons.

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Enlarge clickable targets (links, buttons, inputs) to at least 44px with injected CSS
            - Add extra spacing between adjacent links
            - Ask for confirmation before clicking buttons labelled delete, buy, send or submit
            - Ignore double clicks within 500 ms
            - Configure size and features in the popup
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 190

**Intent:**
hello, my father is almost blind, he use only keyboard. Is possible extension that read aloud the page when he press one key and he can jump between headings?

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Read the main content of the page aloud with one shortcut
            - Jump to next and previous heading with keys and read it
            - Pause, resume and change speed with keys
            - Announce link text and open the focused link with Enter
            - Show a large high-contrast focus outline
Storage:    chrome.storage.sync (speech settings)
Tech stack: JavaScript, Chrome Manifest V3, chrome.commands, chrome.tts, content script, Mozilla Readability
```

---

## Example 191

**Intent:**
caption any video with speech to text

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Capture audio of the current tab with tabCapture in an offscreen document
            - Stream audio to a speech-to-text service
            - Show live captions in a draggable overlay on the page
            - Change caption font size and background
            - Save the transcript as a text file
Tech stack: TypeScript, Chrome Manifest V3, chrome.tabCapture, offscreen documents, Deepgram streaming API
```

---

## Example 192

**Intent:**
tab suspender

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Discard tabs that have been inactive for a configured time
            - Skip pinned, audible and whitelisted tabs
            - Discard all other tabs from the popup
            - Show memory saved estimate in the popup
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, chrome.tabs.discard, chrome.alarms
```

---

## Example 193

**Intent:**
vimium but simpler, just hit f and type letters to click links

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Show letter hints over every clickable element when F is pressed
            - Click the element whose hint is typed
            - Open in a new tab with Shift+F
            - Scroll with j and k
            - Ignore keys while typing in input fields
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 194

**Intent:**
has my password been leaked? check it when i type it in signup forms

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Detect new-password fields on signup and change-password forms
            - Hash the typed password with SHA-1 and send only the first 5 characters to the breach API (k-anonymity)
            - Show a warning under the field if the password appears in breaches
            - Never store or log the password
Tech stack: JavaScript, Chrome Manifest V3, content script, Web Crypto API, Have I Been Pwned Pwned Passwords API
```

---

## Example 195

**Intent:**
gimme a throwaway email address generator in the browser for signups

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Create a temporary email address from the popup
            - Fill the focused email field with it
            - Poll the inbox and show incoming messages in the popup
            - Extract and copy verification codes
            - Delete the address after a set time
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, Mail.tm API
```

---

## Example 196

**Intent:**
block the invisible tracking pixels in my webmail

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Detect 1x1 images and known tracker image hosts in opened emails
            - Block those image requests with declarativeNetRequest rules
            - Show an eye icon in the email view with the number of trackers blocked
            - Allow images for trusted senders
Storage:    chrome.storage.sync (trusted senders)
Tech stack: JavaScript, Chrome Manifest V3, content script for Gmail and Outlook web, declarativeNetRequest
```

---

## Example 197

**Intent:**
show me which of my installed extensions have scary permissions

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - List installed extensions with the chrome.management API
            - Rate each by its permissions and host access (e.g. all sites, read history)
            - Explain each permission in plain language
            - Disable or uninstall an extension from the list
            - Alert when an installed extension updates and gains new permissions
Storage:    chrome.storage.local (last known permissions)
Tech stack: JavaScript, Chrome Manifest V3, chrome.management API
```

---

## Example 198

**Intent:**
webrtc leak blocker

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Set WebRTC IP handling policy to disable non-proxied UDP
            - Toggle protection from the popup
            - Run a self-test that shows which IPs are exposed
Tech stack: JavaScript, Chrome Manifest V3, chrome.privacy.network.webRTCIPHandlingPolicy
```

---

## Example 199

**Intent:**
unit price on grocery websites, like price per kg so i can compare

**Spec:**
```
Type:       Browser extension (shopping)
Features:   - Read product price and package size from product tiles on supported grocery sites
            - Parse sizes like 500 g, 1.5 L and 6 x 330 ml
            - Show price per kg, per litre or per item next to each price
            - Highlight the cheapest unit price on the page
            - Let users sort listings by unit price
Tech stack: TypeScript, Chrome Manifest V3, content scripts
```

---

## Example 200

**Intent:**
I have a nut allergy and online grocery shopping is stressful because I have to read every ingredient list. Could an extension highlight allergens on product pages and warn me?

**Spec:**
```
Type:       Browser extension (shopping)
Data model: AllergenProfile(allergens, custom_keywords)
Features:   - Let the user choose allergens (nuts, peanuts, gluten, milk, egg, soy, etc.)
            - Scan ingredient and "may contain" text on product pages
            - Highlight matching words in red
            - Show a warning banner at the top of the page
            - Include synonyms (e.g. almond, hazelnut, cashew for tree nuts)
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 201

**Intent:**
Extension that makes me wait 24 hours before buying something expensive.

**Spec:**
```
Type:       Browser extension (shopping)
Data model: PendingPurchase(id, product_title, price, url, added_at)
Features:   - Detect "Buy now" and checkout clicks on shopping sites
            - Intercept purchases above a price threshold with a cooldown page
            - Save the item to a waiting list with a 24-hour timer
            - Notify when the waiting time is over
            - Show how much money was saved by cancelled purchases
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, content scripts, chrome.alarms, chrome.notifications
```

---

## Example 202

**Intent:**
find a used version of what im looking at on ebay or other second hand sites

**Spec:**
```
Type:       Browser extension (shopping)
Features:   - Read the product name from the current shop page
            - Search second-hand marketplaces for the same item through their search APIs
            - Show the cheapest used listings in a side panel
            - Link to each listing
Tech stack: JavaScript, Chrome Manifest V3, chrome.sidePanel, eBay Browse API
```

---

## Example 203

**Intent:**
footnotes popup on wikipedia and blogs instead of jumping to bottom

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Detect footnote reference links pointing to anchors on the same page
            - Show the footnote text in a popover on hover or tap
            - Keep the page scroll position unchanged
            - Support common footnote markup patterns
Tech stack: JavaScript, Chrome Manifest V3, content script, Floating UI
```

---

## Example 204

**Intent:**
wiki hover previews for links on any site

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Detect links to Wikipedia articles
            - Fetch the article summary and thumbnail on hover
            - Show a preview card near the link
            - Cache summaries for the session
Tech stack: JavaScript, Chrome Manifest V3, content script, Wikipedia REST API (page/summary)
```

---

## Example 205

**Intent:**
bionic reading style extension, bold first half of words

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Bold the first part of each word in paragraph text
            - Adjust the fixation strength (how many letters are bold)
            - Skip code blocks, inputs and navigation
            - Toggle on and off per site with a shortcut
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script (TreeWalker)
```

---

## Example 206

**Intent:**
read later list in my browser that syncs between my laptop and work pc

**Spec:**
```
Type:       Browser extension (reading)
Data model: Article(id, url, title, excerpt, added_at, read_at)
Features:   - Save the current page with one click
            - Show unread articles in the popup sorted by date
            - Mark articles as read or delete them
            - Sync the list across devices
            - Show the unread count on the badge
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3
```

---

## Example 207

**Intent:**
highlight text on webpages in colors and see my highlights again when I come back, export them

**Spec:**
```
Type:       Browser extension (reading)
Data model: Highlight(id, url, text, color, xpath_range, note, created_at)
Features:   - Highlight selected text in one of four colours
            - Re-apply highlights when the page is revisited using stored text ranges
            - Add a note to a highlight
            - List all highlights by page on a dashboard
            - Export highlights as Markdown
Storage:    IndexedDB
Tech stack: TypeScript, Chrome Manifest V3, content script, rangy-style range serialisation
```

---

## Example 208

**Intent:**
chrome extension for learning words: every time i look up a word it saves it and quizzes me later on new tab

**Spec:**
```
Type:       Browser extension (new tab page)
Data model: VocabWord(word, definition, example_sentence, source_url, box_level, next_review)
Features:   - Save words looked up via the context menu with their definition
            - Show a quiz card on the new tab page for due words
            - Move words between Leitner boxes based on answers
            - Show progress stats
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3 (chrome_url_overrides), Free Dictionary API
```

---

## Example 209

**Intent:**
color blind filter for websites

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Apply SVG colour matrix filters to the page for protanopia, deuteranopia and tritanopia correction
            - Simulate colour blindness types for designers
            - Switch modes from the popup
            - Apply per site or globally
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script, SVG feColorMatrix
```

---

## Example 210

**Intent:**
images without alt text are a pain with my screen reader, can an extension describe them with AI

**Spec:**
```
Type:       Browser extension (accessibility)
Auth:       User's API key for the vision model in extension settings
Features:   - Find images on the page with missing or empty alt text
            - Send image URLs to a vision model for a short description
            - Set the description as the image's alt attribute
            - Mark generated descriptions with a prefix "AI description:"
            - Process only visible images to limit cost
Storage:    chrome.storage.local (cached descriptions)
Tech stack: JavaScript, Chrome Manifest V3, content script, OpenAI vision API
```

---

## Example 211

**Intent:**
new tab with weather and my google calendar events today

**Spec:**
```
Type:       Browser extension (new tab page)
Auth:       Google OAuth via chrome.identity (calendar.readonly scope)
Features:   - Show current weather and today's forecast for the user's location
            - Show today's calendar events with times
            - Show a clock and greeting
            - Let the user pick temperature units
Storage:    chrome.storage.local (cached weather)
Tech stack: JavaScript, Chrome Manifest V3 (chrome_url_overrides), Google Calendar API, Open-Meteo API
```

---

## Example 212

**Intent:**
new tab that shows a random quote and my habits checklist for today

**Spec:**
```
Type:       Browser extension (new tab page)
Data model: Habit(id, name)
            HabitCheck(habit_id -> Habit, date)
Features:   - Show a random quote from a bundled list
            - Show today's habits with checkboxes
            - Show the current streak for each habit
            - Add and remove habits in settings
Storage:    chrome.storage.sync
Tech stack: HTML, CSS, JavaScript, Chrome Manifest V3
```

---

## Example 213

**Intent:**
minimal new tab page just a search box and nothing else, dark

**Spec:**
```
Type:       Browser extension (new tab page)
Features:   - Show a centred search box on a dark background
            - Search with the browser's default search engine via chrome.search
            - Focus the box automatically
            - Show recently closed tabs below the box on demand
Tech stack: HTML, CSS, JavaScript, Chrome Manifest V3, chrome.search, chrome.sessions
```

---

## Example 214

**Intent:**
new tab countdown to my wedding day lol

**Spec:**
```
Type:       Browser extension (new tab page)
Features:   - Show days, hours and minutes until a chosen date
            - Let the user set the event name, date and a background photo
            - Show a short message on the day itself
            - Support several countdowns shown as cards
Storage:    chrome.storage.local (settings, uploaded photo as data URL)
Tech stack: HTML, CSS, JavaScript, Chrome Manifest V3
```

---

## Example 215

**Intent:**
new tab page shows my github notifications and PRs waiting for my review

**Spec:**
```
Type:       Browser extension (new tab page)
Auth:       GitHub personal access token stored in chrome.storage.local
Features:   - Show unread GitHub notifications grouped by repository
            - Show pull requests requesting the user's review
            - Mark notifications as read
            - Refresh every 5 minutes
Tech stack: TypeScript, Chrome Manifest V3, GitHub REST API (Octokit)
```

---

## Example 216

**Intent:**
github extension that shows a file tree sidebar when browsing repos

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Add a collapsible file tree sidebar on GitHub repository pages
            - Load the tree with the Git Trees API
            - Navigate to files without full page reloads
            - Support private repositories with a personal access token
            - Remember sidebar width
Storage:    chrome.storage.local (token, width)
Tech stack: TypeScript, Chrome Manifest V3, content script, GitHub REST API
```

---

## Example 217

**Intent:**
on github PR page, add a button to copy all changed file names

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Add a "Copy file list" button on pull request Files changed tabs
            - Read changed files from the GitHub API
            - Copy paths as a newline list or Markdown checklist
Tech stack: JavaScript, Chrome Manifest V3, content script, GitHub REST API
```

---

## Example 218

**Intent:**
website tech detector, what framework and cms does this site use

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Inspect page HTML, scripts, meta tags, cookies and global variables
            - Match them against a fingerprint database
            - Show detected technologies by category (CMS, framework, analytics, CDN)
            - Show the version when detectable
Tech stack: JavaScript, Chrome Manifest V3, content script, chrome.scripting (MAIN world), Wappalyzer-style fingerprints
```

---

## Example 219

**Intent:**
seo checker extension shows title, meta description, h1s, canonical

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Read title, meta description, canonical, robots and Open Graph tags
            - List the heading structure H1-H6
            - Warn about missing or too long title and description
            - Count images without alt text
            - Check hreflang links
Tech stack: JavaScript, Chrome Manifest V3, chrome.scripting, React popup
```

---

## Example 220

**Intent:**
core web vitals badge for any page I visit

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Measure LCP, INP and CLS on each page load
            - Show the worst metric as a coloured badge (good, needs improvement, poor)
            - Show all values in the popup
            - Log values to the console optionally
Tech stack: JavaScript, Chrome Manifest V3, content script, web-vitals library
```

---

## Example 221

**Intent:**
mock api responses in the browser so i can test my frontend without the backend

**Spec:**
```
Type:       Browser extension (developer tools)
Data model: MockRule(id, url_pattern, method, status, response_body, delay_ms, enabled)
Features:   - Create rules that match request URLs and methods
            - Return a mock JSON response with status and delay
            - Patch fetch and XMLHttpRequest in the page's MAIN world
            - Toggle rules from a DevTools panel
            - Import and export rules as JSON
Storage:    chrome.storage.local
Tech stack: TypeScript, Chrome Manifest V3, chrome.devtools.panels, content script (world: MAIN)
```

---

## Example 222

**Intent:**
fill forms with fake data for testing

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Detect form fields by type, name and label
            - Fill them with realistic fake data (names, emails, addresses, dates)
            - Respect selects, checkboxes, radios and required fields
            - Fill from a keyboard shortcut
            - Define custom rules per field name
Storage:    chrome.storage.sync (custom rules)
Tech stack: JavaScript, Chrome Manifest V3, chrome.commands, Faker.js
```

---

## Example 223

**Intent:**
websocket inspector in devtools, see messages pretty

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Attach to the tab with the chrome.debugger API
            - Capture WebSocket frames sent and received
            - Show messages in a DevTools panel with JSON formatting
            - Filter by text and direction
            - Pause and clear the log
Tech stack: TypeScript, Chrome Manifest V3, chrome.debugger (Network domain), chrome.devtools.panels
```

---

## Example 224

**Intent:**
measure stuff on screen in pixels like a ruler

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Draw a measuring box by dragging on the page
            - Show width and height in pixels
            - Snap guides to element edges
            - Show the distance between two hovered elements
Tech stack: JavaScript, Chrome Manifest V3, content script overlay
```

---

## Example 225

**Intent:**
lorem ipsum generator for when im filling forms in dev

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Generate lorem ipsum words, sentences or paragraphs in the popup
            - Insert text into the focused field from the context menu
            - Copy to clipboard
            - Choose length
Tech stack: JavaScript, Chrome Manifest V3, chrome.contextMenus
```

---

## Example 226

**Intent:**
vscode rest client, send requests written in .http files

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Parse requests in .http files separated by ###
            - Show a "Send request" CodeLens above each request
            - Show response status, headers and body in a side panel
            - Support variables and environments from a settings file
            - Save response history
Tech stack: TypeScript, VS Code Extension API (CodeLensProvider, webview), undici
```

---

## Example 227

**Intent:**
preview regex matches live as I type in vs code

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Open a regex tester panel for a regex literal under the cursor
            - Let the user enter sample text
            - Highlight matches and capture groups live
            - Explain the pattern in plain English
Tech stack: TypeScript, VS Code Extension API (webview), regexp-tree
```

---

## Example 228

**Intent:**
show test coverage in vscode gutter green red

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Find lcov.info or cobertura XML coverage files in the workspace
            - Show covered and uncovered lines with gutter colours
            - Show coverage percentage for the open file in the status bar
            - Reload when the coverage file changes
Tech stack: TypeScript, VS Code Extension API (decorations, FileSystemWatcher), lcov-parse
```

---

## Example 229

**Intent:**
track how much time i spend coding per project in vscode

**Spec:**
```
Type:       Plugin (VS Code extension)
Data model: CodingSession(project, language, start_at, end_at)
Features:   - Detect activity from edits, saves and focus events
            - Count time per workspace and language with a 2-minute idle timeout
            - Show today's time in the status bar
            - Show a weekly report in a webview with charts
            - Export data as CSV
Storage:    Local SQLite file in the extension's global storage
Tech stack: TypeScript, VS Code Extension API, better-sqlite3, Chart.js
```

---

## Example 230

**Intent:**
paste json in vscode and get typescript interfaces

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Add a "Paste JSON as Types" command
            - Read JSON from the clipboard
            - Generate TypeScript interfaces with nested types and optional fields
            - Insert at the cursor
            - Support other targets like Go structs and Python dataclasses
Tech stack: TypeScript, VS Code Extension API, quicktype-core
```

---

## Example 231

**Intent:**
vscode generate commit message with ai from my staged changes

**Spec:**
```
Type:       Plugin (VS Code extension)
Auth:       API key stored in VS Code SecretStorage
Features:   - Read the staged diff via the built-in Git extension API
            - Send the diff to an LLM with a Conventional Commits prompt
            - Fill the Source Control input box with the message
            - Add a button in the Source Control title bar
            - Let the user choose language and style
Tech stack: TypeScript, VS Code Extension API (scm, SecretStorage), Anthropic Messages API
```

---

## Example 232

**Intent:**
kubernetes yaml validation in vs code

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Detect Kubernetes manifests by apiVersion and kind
            - Validate them against the Kubernetes JSON schemas for a chosen version
            - Show errors in the Problems panel
            - Provide completion for fields
            - Add a command to apply the file with kubectl
Tech stack: TypeScript, VS Code Extension API, YAML Language Server, kubectl
```

---

## Example 233

**Intent:**
jetbrains plugin to convert JSON into Kotlin data classes

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Open a dialog to paste JSON
            - Generate Kotlin data classes with nested classes and nullable types
            - Add kotlinx.serialization or Gson annotations optionally
            - Insert classes into the current file or new files
Tech stack: Kotlin, IntelliJ Platform SDK (DialogWrapper, PSI), kotlinx.serialization
```

---

## Example 234

**Intent:**
switch case of selected text in intellij: camelCase snake_case kebab etc

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Add actions to convert selection between camelCase, PascalCase, snake_case, kebab-case and UPPER_CASE
            - Cycle through styles with one shortcut
            - Work with multiple carets
            - Support undo
Tech stack: Kotlin, IntelliJ Platform SDK (EditorAction, WriteCommandAction)
```

---

## Example 235

**Intent:**
PhpStorm plugin that lists all my Laravel routes and jumps to the controller

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Run php artisan route:list --json in the project
            - Show routes in a tool window with method, URI and name
            - Filter by text
            - Navigate to the controller method on double click
            - Refresh on route file changes
Tech stack: Kotlin, IntelliJ Platform SDK (ToolWindowFactory), PHP plugin PSI
```

---

## Example 236

**Intent:**
GoLand plugin that adds json tags to struct fields

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Add an intention on Go structs to add json tags
            - Convert field names to snake_case or camelCase
            - Add omitempty optionally
            - Update existing tags without duplicating
Tech stack: Kotlin, IntelliJ Platform SDK, Go plugin PSI
```

---

## Example 237

**Intent:**
wp contact form plugin that saves messages and stops spam

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Message(id, name, email, subject, body, ip_hash, created_at, is_spam)
Features:   - Render a contact form with the [contact_form] shortcode
            - Validate and sanitize fields and verify a nonce
            - Block spam with a honeypot field and a minimum fill time
            - Save messages to the database and email the site admin
            - List and delete messages in wp-admin
Storage:    Custom MySQL table via $wpdb
Tech stack: PHP, WordPress hooks, wp_mail, admin-post.php handler
```

---

## Example 238

**Intent:**
limit login attempts wordpress

**Spec:**
```
Type:       Plugin (WordPress)
Data model: LoginAttempt(ip_address, attempts, locked_until)
Features:   - Count failed logins per IP with the wp_login_failed hook
            - Lock out an IP for 20 minutes after 5 failures
            - Show remaining attempts on the login form
            - Email the admin on repeated lockouts
            - Whitelist IPs in settings
Storage:    WordPress transients (attempt counters), options table (settings)
Tech stack: PHP, WordPress hooks (authenticate filter, wp_login_failed)
```

---

## Example 239

**Intent:**
two factor login for my wordpress with google authenticator app

**Spec:**
```
Type:       Plugin (WordPress)
Data model: UserMeta(totp_secret_encrypted, backup_codes_hashed, two_factor_enabled)
Features:   - Let users enable 2FA on their profile by scanning a QR code
            - Ask for a 6-digit TOTP code after the password step
            - Generate one-time backup codes
            - Allow admins to require 2FA for certain roles
            - Allow admins to reset a user's 2FA
Storage:    WordPress user meta
Tech stack: PHP, WordPress hooks (wp_authenticate_user, login_form), RFC 6238 TOTP, endroid/qr-code
```

---

## Example 240

**Intent:**
converting all my uploaded images to webp so the site loads faster, plugin for wordpress

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Create a WebP copy of each uploaded JPEG and PNG and its thumbnails
            - Bulk-convert existing media library images in background batches
            - Serve WebP via <picture> tags when the browser supports it
            - Set the compression quality in settings
            - Delete WebP copies when the original is deleted
Tech stack: PHP, WordPress hooks (wp_generate_attachment_metadata), GD or Imagick, Action Scheduler
```

---

## Example 241

**Intent:**
i run a recipe blog on wordpress and want a nice recipe card block with ingredients, steps, prep time, a print button and the google recipe schema thing so i show up with stars and pictures in search

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Rating(post_id, stars, ip_hash, created_at)
Features:   - Provide a Gutenberg Recipe Card block with fields for times, servings, ingredients and steps
            - Render a clean card on the front end with a jump-to-recipe button
            - Output schema.org Recipe JSON-LD including aggregateRating
            - Add a print view without the blog layout
            - Let readers rate the recipe with stars
Storage:    Block attributes in post content, custom table (ratings)
Tech stack: PHP, WordPress Block API (React/JSX, block.json), WordPress REST API
```

---

## Example 242

**Intent:**
donation form with stripe on wordpress for our animal shelter, monthly or once

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Donation(id, donor_name, email, amount, currency, frequency, stripe_session_id, status, created_at)
Features:   - Show a donation form with preset amounts, custom amount and once/monthly choice
            - Create a Stripe Checkout session in payment or subscription mode
            - Record donations via Stripe webhooks
            - Email a thank-you receipt
            - List donations and totals in wp-admin
API:        WordPress REST API
            POST /wp-json/shelter-donate/v1/checkout
            POST /wp-json/shelter-donate/v1/stripe-webhook
Storage:    Custom MySQL table via $wpdb
Tech stack: PHP, WordPress REST API, stripe-php
```

---

## Example 243

**Intent:**
WhatsApp chat button floating on my wordpress site

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Show a floating WhatsApp button in a chosen corner
            - Open a wa.me link with the business number and a pre-filled message
            - Show a greeting bubble after a delay
            - Hide on chosen pages or outside business hours
Storage:    WordPress options table
Tech stack: PHP, WordPress hooks (wp_footer), CSS, vanilla JavaScript
```

---

## Example 244

**Intent:**
announcement bar top of site wordpress, can close it

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Show a dismissible bar at the top of every page
            - Set text, link, colours and start/end dates
            - Remember dismissal in localStorage per announcement version
            - Show different messages for logged-in users
Storage:    WordPress options table
Tech stack: PHP, WordPress hooks (wp_body_open), vanilla JavaScript
```

---

## Example 245

**Intent:**
reading progress bar on top of the posts

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Show a thin progress bar fixed at the top of single posts
            - Update the bar width on scroll based on the article length
            - Choose colour, height and position in settings
            - Only load the script on chosen post types
Tech stack: PHP, WordPress hooks (wp_enqueue_scripts), vanilla JavaScript
```

---

## Example 246

**Intent:**
Want a plugin that lets me edit what each user role can do in wordpress, like let editors manage menus

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - List roles and their capabilities in an admin screen
            - Add or remove capabilities from a role with checkboxes
            - Create new roles by cloning an existing one
            - Export and import role settings as JSON
            - Prevent removing the administrator's critical capabilities
Storage:    WordPress options table (wp_user_roles)
Tech stack: PHP, WordPress Roles API (WP_Roles, add_cap, remove_cap)
```

---

## Example 247

**Intent:**
Elementor widget for a pricing table with 3 plans

**Spec:**
```
Type:       Plugin (WordPress Elementor add-on)
Features:   - Register a Pricing Table widget in Elementor
            - Add controls for plan names, prices, features and button links
            - Mark one plan as "Most popular"
            - Add style controls for colours, typography and spacing
            - Switch between monthly and yearly prices with a toggle
Tech stack: PHP, Elementor Widget API (Widget_Base, controls), JavaScript
```

---

## Example 248

**Intent:**
import posts from a csv file to wordpress

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Upload a CSV in an admin page
            - Map CSV columns to title, content, excerpt, categories, tags and custom fields
            - Import rows in batches with AJAX progress
            - Download featured images from URLs
            - Skip rows whose title already exists
Tech stack: PHP, WordPress hooks, wp_insert_post, media_sideload_image, admin-ajax
```

---

## Example 249

**Intent:**
database cleanup tool for wp, delete revisions spam comments transients

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Count post revisions, auto-drafts, trashed posts, spam comments and expired transients
            - Delete selected items with one click
            - Optimize database tables
            - Schedule weekly cleanup with WP-Cron
            - Show space saved
Tech stack: PHP, $wpdb, WP-Cron
```

---

## Example 250

**Intent:**
activity log for wordpress, who changed what

**Spec:**
```
Type:       Plugin (WordPress)
Data model: ActivityEntry(id, user_id, action, object_type, object_id, details, ip_address, created_at)
Features:   - Log logins, post edits, plugin and theme changes, and setting updates
            - Show the log in an admin table with filters by user, action and date
            - Export entries as CSV
            - Delete entries older than 90 days automatically
Storage:    Custom MySQL table via $wpdb
Tech stack: PHP, WordPress hooks (wp_login, save_post, activated_plugin, updated_option), WP_List_Table
```

---

## Example 251

**Intent:**
guest post submission form on frontend, saved as pending

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Show a submission form with title, content, category and featured image via shortcode
            - Save submissions as pending posts with the author's name and email in post meta
            - Notify editors by email
            - Limit uploads to images under 2 MB
            - Protect the form with a nonce and reCAPTCHA
Tech stack: PHP, WordPress hooks, wp_insert_post, media_handle_upload, Google reCAPTCHA v3
```

---

## Example 252

**Intent:**
job board plugin wordpress, companies post jobs, people apply with cv

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Job(title, description, company, location, type, salary, expires_at)
            Application(id, job_id, name, email, cv_attachment_id, cover_letter, created_at)
Features:   - Let logged-in employers post jobs from a front-end form
            - List jobs with filters for location and type
            - Let candidates apply with a CV upload
            - Email applications to the employer
            - Expire jobs after 30 days with WP-Cron
Storage:    WordPress database (posts, post meta), custom table (applications)
Tech stack: PHP, WordPress hooks, WP_Query, WP-Cron
```

---

## Example 253

**Intent:**
restaurant menu plugin with categories, prices, allergens

**Spec:**
```
Type:       Plugin (WordPress)
Data model: MenuItem(name, description, price, allergens, is_vegan, menu_section)
Features:   - Register a Menu Item post type with price and allergen fields
            - Display the menu grouped by section via a block
            - Show allergen and vegan icons
            - Hide items marked unavailable
            - Print-friendly menu view
Storage:    WordPress database
Tech stack: PHP, WordPress Block API
```

---

## Example 254

**Intent:**
store locator for wordpress with google map and search by postcode

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Store(name, address, lat, lng, phone, opening_hours)
Features:   - Geocode store addresses on save
            - Search stores near a postcode or the visitor's location
            - Show results on a map and as a list sorted by distance
            - Get directions link for each store
API:        WordPress REST API
            GET /wp-json/stores/v1/near?lat={lat}&lng={lng}&radius={km}
Storage:    WordPress database (posts, post meta)
Tech stack: PHP, WordPress REST API, Google Maps JavaScript API, Geocoding API
```

---

## Example 255

**Intent:**
woocommerce minimum order amount

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Block checkout when the cart subtotal is under a set minimum
            - Show a notice on cart and checkout with the missing amount
            - Set different minimums per shipping zone
            - Exclude certain user roles
Storage:    WordPress options table
Tech stack: PHP, WooCommerce hooks (woocommerce_check_cart_items, wc_add_notice)
```

---

## Example 256

**Intent:**
let customers pick a delivery date at checkout in woocommerce, not sundays, not holidays

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Add a date picker field to the checkout
            - Disable Sundays, holidays and dates within a minimum lead time
            - Limit the number of orders per day
            - Save the date as order meta and show it in admin, emails and the thank-you page
            - Sort admin orders by delivery date
Storage:    Order meta (HPOS compatible), options table (holidays, limits)
Tech stack: PHP, WooCommerce hooks (woocommerce_after_order_notes, woocommerce_checkout_create_order), flatpickr
```

---

## Example 257

**Intent:**
woocomerce pdf invoice attached to the order email

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Generate a PDF invoice with sequential invoice numbers when an order is completed
            - Use the shop's logo, address and VAT number
            - Attach the PDF to the customer's completed-order email
            - Let admins download invoices from the order screen
            - Let customers download from My Account
Tech stack: PHP, WooCommerce hooks (woocommerce_email_attachments), Dompdf
```

---

## Example 258

**Intent:**
gift wrap option on checkout with extra fee

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Add a "Gift wrap this order" checkbox and gift message field at checkout
            - Add a fee to the cart totals when checked
            - Save the message to the order
            - Show gift wrap and message on packing slips and admin order view
Tech stack: PHP, WooCommerce hooks (woocommerce_cart_calculate_fees, woocommerce_review_order_before_payment), AJAX update_checkout
```

---

## Example 259

**Intent:**
loyalty points for my woocommerce shop, 1 point per euro, use points for discount

**Spec:**
```
Type:       Plugin (WooCommerce)
Data model: PointsLedger(id, user_id, order_id, points, reason, created_at)
Features:   - Award points when an order is completed
            - Show the points balance in My Account and on product pages
            - Let customers redeem points for a cart discount at checkout
            - Remove points when an order is refunded
            - Let admins adjust points manually
Storage:    Custom MySQL table via $wpdb
Tech stack: PHP, WooCommerce hooks (woocommerce_order_status_completed, woocommerce_cart_calculate_fees)
```

---

## Example 260

**Intent:**
wholesale prices for B2B customers who log in, normal prices for others

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Add a wholesale_customer role
            - Add a wholesale price field to products and variations
            - Show the wholesale price to that role in shop, cart and checkout
            - Set minimum quantities for wholesale customers
            - Hide selected products from retail customers
Storage:    Product meta
Tech stack: PHP, WooCommerce hooks (woocommerce_product_get_price, woocommerce_product_variation_get_price)
```

---

## Example 261

**Intent:**
abandoned cart emails woocommerce

**Spec:**
```
Type:       Plugin (WooCommerce)
Data model: AbandonedCart(id, email, cart_contents_json, total, recovery_token, last_activity_at, emails_sent, recovered)
Features:   - Capture the email as soon as it is typed at checkout
            - Mark carts as abandoned after 1 hour of inactivity
            - Send up to 3 reminder emails with a recovery link
            - Restore the cart from the recovery link
            - Stop emails when the order is placed
Storage:    Custom MySQL table via $wpdb
Tech stack: PHP, WooCommerce hooks, Action Scheduler, WC_Email
```

---

## Example 262

**Intent:**
quantity discount table on product page like buy 5 get 10% off

**Spec:**
```
Type:       Plugin (WooCommerce)
Data model: DiscountTier(product_id, min_quantity, percent_off)
Features:   - Add quantity tiers per product in the product editor
            - Show a tier table on the product page
            - Apply the matching tier price in the cart
            - Highlight the active tier when the quantity changes
Storage:    Product meta
Tech stack: PHP, WooCommerce hooks (woocommerce_before_calculate_totals), JavaScript
```

---

## Example 263

**Intent:**
Hello, we are small farm in Kenya, sell vegetables box with WooCommerce. Need plugin that customer choose pickup place and time slot, maximum 10 people per slot.

**Spec:**
```
Type:       Plugin (WooCommerce)
Data model: PickupLocation(id, name, address)
            PickupSlot(id, location_id -> PickupLocation, weekday, start_time, end_time, capacity)
Features:   - Show pickup location and time slot selectors at checkout
            - Hide full slots when 10 orders are booked
            - Save the chosen slot to the order
            - Show a daily pickup list per location in wp-admin
            - Include pickup details in the order emails
Storage:    Custom MySQL tables via $wpdb, order meta
Tech stack: PHP, WooCommerce hooks, vanilla JavaScript
```

---

## Example 264

**Intent:**
hide prices on woocommerce until people login

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Hide prices and add-to-cart buttons for guests
            - Show a "Log in to see prices" link instead
            - Apply to the whole shop or selected categories
            - Block adding to cart by direct URL for guests
Tech stack: PHP, WooCommerce hooks (woocommerce_get_price_html, woocommerce_is_purchasable)
```

---

## Example 265

**Intent:**
shopify free shipping progress bar in cart

**Spec:**
```
Type:       Plugin (Shopify app)
Features:   - Show a progress bar in the cart drawer and cart page with the amount left for free shipping
            - Read the threshold from app settings
            - Update live when cart changes via the Cart AJAX API
            - Support multiple currencies with Shopify Markets conversion
            - Show a success message when reached
Tech stack: Shopify Theme App Extension (app embed), Liquid, JavaScript, Shopify Cart AJAX API
```

---

## Example 266

**Intent:**
shopify bundle discount, buy shampoo + conditioner get 15% off, with shopify functions

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Data model: Bundle(id, shop_domain, product_ids, percent_off)
Features:   - Let the merchant define product bundles in the admin
            - Apply the discount when all bundle products are in the cart with a Discount Function
            - Store bundle config in a discount metafield
            - Show a bundle offer block on the product page
Tech stack: Shopify Functions (Rust or JavaScript), Shopify CLI, Remix, Polaris, Theme App Extension
```

---

## Example 267

**Intent:**
upsell offer on shopify checkout page, show a related product they can add with one click

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant, Shopify Plus checkout)
Data model: UpsellRule(id, trigger_product_id, offer_product_id, discount_percent)
            UpsellEvent(rule_id, event_type, created_at)
Features:   - Render an offer in the checkout using a Checkout UI extension
            - Pick the product from merchant-defined rules based on cart contents
            - Add the product to the checkout with applyCartLinesChange
            - Track views and conversions
Storage:    PostgreSQL
Tech stack: Shopify Checkout UI Extensions (React), Shopify CLI, Remix
```

---

## Example 268

**Intent:**
sync shopify inventory with google sheet both ways

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install, Google OAuth (Sheets scope)
Data model: SyncConfig(shop_domain, spreadsheet_id, location_id, last_synced_at)
Features:   - Export products, variants, SKUs and stock levels to a Google Sheet
            - Update Shopify inventory when quantities change in the sheet
            - Update the sheet on inventory_levels/update webhooks
            - Show sync log and errors in the admin
Storage:    PostgreSQL
Tech stack: Node.js, Shopify Admin GraphQL API, Google Sheets API, Remix, BullMQ
```

---

## Example 269

**Intent:**
auto tag shopify orders, like "VIP" if total over 500 or "international"

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Data model: TagRule(id, shop_domain, condition_field, operator, value, tag)
Features:   - Build rules with conditions on total, country, product, discount code or customer order count
            - Listen to orders/create webhooks
            - Add tags to matching orders with the tagsAdd mutation
            - Apply rules retroactively to past orders
Storage:    PostgreSQL
Tech stack: Node.js, Shopify CLI, Remix, Polaris, Shopify Admin GraphQL API
```

---

## Example 270

**Intent:**
shopify gift message field on cart page

**Spec:**
```
Type:       Plugin (Shopify app)
Features:   - Add a gift message textarea and "This is a gift" checkbox to the cart
            - Save them as cart attributes
            - Show them on the order in the admin and packing slip
            - Limit message length
Tech stack: Shopify Theme App Extension (app block), Liquid, JavaScript, Cart AJAX API
```

---

## Example 271

**Intent:**
pre order button shopify when product out of stock, charge later

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Features:   - Replace "Sold out" with a "Pre-order" button for chosen products
            - Create selling plans with deferred payment using the Selling Plans API
            - Show the expected ship date on the product page
            - Tag pre-order orders
            - Remind the merchant to collect payment before shipping
Storage:    Shopify metafields
Tech stack: Node.js, Shopify CLI, Remix, Shopify Admin GraphQL API (sellingPlanGroupCreate), Theme App Extension
```

---

## Example 272

**Intent:**
Our shop sells in Germany and the Netherlands and I'm tired of manually translating every product. Could a Shopify app translate product titles and descriptions with DeepL and push them into Shopify's translations, but let me fix the ones that come out weird?

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Data model: TranslationJob(id, shop_domain, locale, status, product_count, created_at)
Features:   - List products with their translation status per locale
            - Translate titles, descriptions and SEO fields with DeepL, preserving HTML
            - Save translations with the translationsRegister mutation
            - Let the merchant review and edit before publishing
            - Translate new products automatically from products/create webhooks
Storage:    PostgreSQL
Tech stack: Node.js, Shopify CLI, Remix, Polaris, DeepL API, Shopify Admin GraphQL API
```

---

## Example 273

**Intent:**
shopify show estimated delivery date on product page depending on the customer's country

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Data model: DeliveryRule(id, shop_domain, country_code, processing_days, transit_min_days, transit_max_days)
Features:   - Let the merchant set processing and transit days per country in the admin
            - Detect the visitor's country from Shopify localization
            - Show "Arrives between Tue 12 and Fri 15 Nov" on product pages, skipping weekends
            - Store rules in a shop metafield read by the theme block
Storage:    Shopify metafields
Tech stack: Node.js, Shopify CLI, Remix, Polaris, Theme App Extension (Liquid, JavaScript)
```

---

## Example 274

**Intent:**
figma find and replace text across the whole file

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Search text in all text layers on the current page or all pages
            - Support case-sensitive and regex search
            - Preview matches with their layer names
            - Replace one or all matches, loading fonts first
            - Zoom to a match when clicked
Tech stack: TypeScript, Figma Plugin API (findAllWithCriteria, loadFontAsync)
```

---

## Example 275

**Intent:**
figma plugin that renames layers automatically to something meaningful instead of Frame 247

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Walk the selected layers and their children
            - Name text layers after their content and frames after their role (button, card, header, icon)
            - Use auto layout direction and child types to guess roles
            - Skip layers that already have custom names
            - Preview names before applying
Tech stack: TypeScript, Figma Plugin API
```

---

## Example 276

**Intent:**
design lint in figma, find colors and fonts that aren't from our styles

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Scan the selection or page for fills, strokes, text and effects
            - Flag values not linked to a style or variable
            - Group issues by type and layer
            - Suggest the closest matching style and apply it with one click
            - Ignore hidden and locked layers
Tech stack: TypeScript, Figma Plugin API, React UI
```

---

## Example 277

**Intent:**
figma to flutter code

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Read the selected frame's layout, text styles and colours
            - Convert auto layout to Row and Column widgets with spacing and padding
            - Convert text layers to Text widgets with TextStyle
            - Export colours as a Flutter theme file
            - Show Dart code with a copy button
Tech stack: TypeScript, Figma Plugin API
```

---

## Example 278

**Intent:**
find unused color styles in my figma file

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - List all local paint, text and effect styles
            - Scan every page for nodes that use each style
            - Show styles with zero uses
            - Delete selected unused styles
            - Show usage counts for the rest
Tech stack: TypeScript, Figma Plugin API (getLocalPaintStylesAsync, loadAllPagesAsync)
```

---

## Example 279

**Intent:**
figma: which components from our library are used the most across our files

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Scan all pages for component instances
            - Group instances by main component and library
            - Show counts sorted by usage
            - Detect detached instances by layer names matching components
            - Export the report as CSV
Tech stack: TypeScript, Figma Plugin API (InstanceNode.getMainComponentAsync)
```

---

## Example 280

**Intent:**
Our app is translated into 6 languages and the designers always ask me what the German text looks like in the designs. A Figma plugin that pulls translations from our Google Sheet and swaps the text in the frames by key would be really helpful.

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Read translation rows (key, en, de, fr, ...) from a published Google Sheet CSV
            - Link text layers to keys by layer name like "#home.title"
            - Switch all linked layers to a chosen language
            - Flag layers whose text overflows its frame after switching
            - Duplicate a frame per language
Tech stack: TypeScript, Figma Plugin API, Papa Parse
```

---

## Example 281

**Intent:**
avatars plugin figma

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Fill selected shapes with random avatar photos or illustrated avatars
            - Choose style, gender and age range
            - Avoid repeating the same avatar in one selection
            - Insert as image fills keeping the shape mask
Tech stack: TypeScript, Figma Plugin API, DiceBear API, randomuser.me API
```

---

## Example 282

**Intent:**
make a figma plugin to turn a frame into an animated gif by frames

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Use the selected frames as animation frames in layer order
            - Export each frame as PNG with exportAsync
            - Encode them into a GIF in the plugin UI
            - Set frame delay and loop count
            - Download the GIF
Tech stack: TypeScript, Figma Plugin API (exportAsync), gif.js
```

---

## Example 283

**Intent:**
isometric mockup figma plugin

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Take the selected frame and export it as an image
            - Apply an isometric transform (rotate and skew) to a copy
            - Choose angle presets (left, right, top)
            - Add an optional drop shadow
Tech stack: TypeScript, Figma Plugin API (relativeTransform)
```

---

## Example 284

**Intent:**
plugin for figma accessibility notes, so devs know tab order and aria labels

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Add numbered tab-order markers next to interactive elements
            - Attach annotations for ARIA labels, roles and heading levels
            - Store notes in plugin data on each node
            - Generate an annotation layer beside the frame
            - Export all notes as Markdown for developers
Tech stack: TypeScript, Figma Plugin API (setPluginData), Preact UI
```

---

## Example 285

**Intent:**
obsidian pomodoro timer in status bar that logs sessions to daily note

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Start and stop a pomodoro from a command or the status bar
            - Show the countdown in the status bar
            - Play a sound when a session ends
            - Append "- 🍅 25 min - <task>" to today's daily note
            - Configure work and break lengths
Storage:    Obsidian plugin data.json (settings)
Tech stack: TypeScript, Obsidian Plugin API
```

---

## Example 286

**Intent:**
obsidian calendar view for my daily notes, dots for days with notes

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Show a monthly calendar in the right sidebar
            - Mark days that have a daily note, with dot size by word count
            - Open or create the daily note when a day is clicked
            - Show week numbers and open weekly notes
Tech stack: TypeScript, Obsidian Plugin API (ItemView), Svelte
```

---

## Example 287

**Intent:**
obsidian find broken links and orphaned notes

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - List links that point to non-existent notes using metadataCache.unresolvedLinks
            - List notes with no incoming or outgoing links
            - Create a missing note or remove the link with one click
            - Ignore folders set in settings
Tech stack: TypeScript, Obsidian Plugin API (metadataCache)
```

---

## Example 288

**Intent:**
publish an obsidian note to my wordpress blog with one command

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Auth:       WordPress application password stored in plugin settings
Features:   - Convert the current note's Markdown to HTML
            - Upload embedded images to the WordPress media library
            - Create or update a post via the WordPress REST API
            - Save the post ID in frontmatter to update later
            - Map tags and categories from frontmatter
Tech stack: TypeScript, Obsidian Plugin API, WordPress REST API, markdown-it
```

---

## Example 289

**Intent:**
obsidian plugin to compress pasted images and save them in an attachments folder

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Intercept image pastes and drops in the editor
            - Resize to a maximum width and convert to WebP or JPEG
            - Save to a configured attachments folder with a date-based name
            - Insert the embed link at the cursor
Tech stack: TypeScript, Obsidian Plugin API (editor-paste event), Canvas API
```

---

## Example 290

**Intent:**
export obsidian notes with headings as questions into anki

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Turn headings as fronts and the text below as backs in notes tagged #anki
            - Send cards to Anki through the AnkiConnect API
            - Update existing cards when the note changes using stored note IDs
            - Put cards in a deck named after the folder
Storage:    Obsidian plugin data.json (card ID mapping)
Tech stack: TypeScript, Obsidian Plugin API, AnkiConnect
```

---

## Example 291

**Intent:**
obsidian habit tracker grid from checkboxes in daily notes

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Read habits from checklist items in daily notes
            - Render a grid of days vs habits in a code block processor
            - Colour cells for done and missed days
            - Show streaks per habit
Tech stack: TypeScript, Obsidian Plugin API (registerMarkdownCodeBlockProcessor)
```

---

## Example 292

**Intent:**
notion database to google sheets sync every hour

**Spec:**
```
Type:       Scheduled script (Notion integration)
Auth:       Notion integration token, Google service account
Features:   - Query all pages of a Notion database with pagination
            - Flatten properties (title, select, date, number, relation) into columns
            - Overwrite a Google Sheet tab with the data
            - Run hourly on a schedule
            - Log errors to a separate tab
Tech stack: Python, Notion API (notion-client), gspread, GitHub Actions cron
```

---

## Example 293

**Intent:**
turn my notion pages into a blog website

**Spec:**
```
Type:       Web application (static site from Notion)
Auth:       Notion integration token (build time)
Features:   - Fetch published pages from a Notion database at build time
            - Render Notion blocks (text, headings, images, code, callouts) to HTML
            - Generate a post list with tags and dates
            - Download images into the build so links don't expire
            - Rebuild via a deploy hook
Tech stack: Next.js (static export), Notion API, react-notion-x, Vercel
```

---

## Example 294

**Intent:**
recurring tasks in notion - when i tick a weekly task it should create the next one

**Spec:**
```
Type:       Webhook service (Notion integration)
Auth:       Notion integration token
Features:   - Receive Notion webhooks for page property changes
            - Detect tasks marked Done that have a Recurrence property
            - Create a copy with the next due date (daily, weekly, monthly)
            - Leave the completed task untouched
API:        REST
            POST /webhooks/notion
Tech stack: Node.js, Express, Notion API (@notionhq/client)
```

---

## Example 295

**Intent:**
notion progress bar widget i can embed

**Spec:**
```
Type:       Web application (embeddable widget)
Features:   - Show a progress bar from URL parameters (value, max, colour, label)
            - Render a clean, transparent-background page for Notion /embed
            - Provide a builder page that generates the embed URL
            - Support light and dark styles
Tech stack: HTML, CSS, JavaScript, GitHub Pages
```

---

## Example 296

**Intent:**
Slack bot that adds a message to my notion database when I react with :notion:

**Spec:**
```
Type:       Bot (Slack and Notion integration)
Auth:       Slack OAuth (reactions:read, channels:history), Notion integration token
Features:   - Listen for reaction_added events with the :notion: emoji
            - Fetch the message text, author and permalink
            - Create a page in a Notion database with those properties
            - Reply in thread with the Notion link
Tech stack: Python, Slack Bolt, Notion API
```

---

## Example 297

**Intent:**
weekly email with what i finished in notion

**Spec:**
```
Type:       Scheduled script (Notion integration)
Auth:       Notion integration token
Features:   - Query a tasks database for items completed in the last 7 days
            - Group them by project
            - Format an HTML email summary
            - Send it every Friday at 5 pm
Tech stack: Python, Notion API, smtplib, cron
```

---

## Example 298

**Intent:**
sheets: log every change someone makes with who and when

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Install an onEdit trigger
            - Record sheet, cell, old value, new value, user email and timestamp
            - Append entries to a protected "Changelog" sheet
            - Ignore edits to the changelog itself
Tech stack: Google Apps Script (installable onEdit trigger), SpreadsheetApp, Session
```

---

## Example 299

**Intent:**
Google forms quiz autograder with partial credit and feedback emails

**Spec:**
```
Type:       Plugin (Google Forms add-on)
Data model: AnswerKey(question_id, correct_answers, points, partial_credit)
Features:   - Let the teacher set answer keys and points in a sidebar
            - Grade responses on submit with partial credit for checkbox questions
            - Write scores to the response sheet
            - Email each student their score and feedback
Tech stack: Google Apps Script, FormApp, MailApp, SpreadsheetApp
```

---

## Example 300

**Intent:**
email reminders for unpaid invoices from a google sheet

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Read invoices with client email, amount, due date and status
            - Find unpaid invoices that are overdue or due in 3 days
            - Send polite reminder emails from a template
            - Record the reminder date to avoid duplicates
            - Run daily on a time trigger
Tech stack: Google Apps Script, GmailApp, SpreadsheetApp, time-driven triggers
```

---

## Example 301

**Intent:**
weather function for google sheets =WEATHER("Paris")

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Add a custom function WEATHER(city, [field])
            - Return temperature, condition or humidity
            - Cache results for 30 minutes with CacheService
            - Return a clear error for unknown cities
Tech stack: Google Apps Script (custom functions), UrlFetchApp, Open-Meteo Geocoding and Forecast APIs
```

---

## Example 302

**Intent:**
crypto prices in sheets that update

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Add a custom function CRYPTO(symbol, currency)
            - Fetch prices with a cached request
            - Add a menu option to refresh all prices
            - Show 24h change with another function
Tech stack: Google Apps Script, UrlFetchApp, CacheService, CoinGecko API
```

---

## Example 303

**Intent:**
excel business days function that skips our company holidays

**Spec:**
```
Type:       Plugin (Excel add-in)
Features:   - Add custom functions WORKDAYS_CO(start, end) and ADD_WORKDAYS_CO(date, n)
            - Read company holidays from a named range or a shared URL
            - Exclude weekends with configurable weekend days
            - Return errors for invalid dates
Tech stack: TypeScript, Office Add-ins (Excel custom functions)
```

---

## Example 304

**Intent:**
compare two excel sheets and highlight what changed

**Spec:**
```
Type:       Plugin (Excel add-in)
Features:   - Choose two worksheets and a key column in the task pane
            - Match rows by key
            - Highlight changed cells in yellow, added rows in green and missing rows in red
            - Write a summary report sheet of all differences
Tech stack: TypeScript, Office Add-ins (Excel JavaScript API), React
```

---

## Example 305

**Intent:**
excel addin that explains a formula in plain english

**Spec:**
```
Type:       Plugin (Excel add-in)
Features:   - Read the formula of the selected cell
            - Send it to an LLM with referenced cell values
            - Show a plain-English explanation in the task pane
            - Break down nested functions step by step
Tech stack: TypeScript, Office Add-ins (Excel JavaScript API), Azure OpenAI
```

---

## Example 306

**Intent:**
Word add-in that checks our documents follow the company style guide (banned words, title case headings)

**Spec:**
```
Type:       Plugin (Word add-in)
Features:   - Read paragraphs and headings from the document
            - Flag banned and discouraged words from a shared list
            - Check headings for title case
            - Show issues in a task pane and select the text when clicked
            - Apply suggested fixes
Tech stack: TypeScript, Office Add-ins (Word JavaScript API), React, Fluent UI
```

---

## Example 307

**Intent:**
powerpoint add-in to insert our brand icons

**Spec:**
```
Type:       Plugin (PowerPoint add-in)
Features:   - Show a searchable grid of company icons in the task pane
            - Insert a chosen icon as SVG on the current slide
            - Recolour icons with brand colours before inserting
            - Load the icon set from a company URL
Tech stack: TypeScript, Office Add-ins (PowerPoint JavaScript API, setSelectedDataAsync with SVG)
```

---

## Example 308

**Intent:**
follow up reminder in gmail if no one replies in 3 days

**Spec:**
```
Type:       Plugin (Gmail add-on)
Auth:       Google OAuth (Gmail modify scope)
Features:   - Add a "Remind me if no reply" button when composing or reading a sent message
            - Store the thread ID and due date
            - Check daily whether the thread has a newer message from someone else
            - Move unanswered threads back to the inbox with a "Follow up" label
Storage:    Apps Script PropertiesService
Tech stack: Google Apps Script, CardService, GmailApp, time-driven triggers
```

---

## Example 309

**Intent:**
gmail email to trello card

**Spec:**
```
Type:       Plugin (Gmail add-on)
Auth:       Google OAuth, Trello API key and token
Features:   - Show a card for the open email with board and list pickers
            - Create a Trello card with the subject as title and body excerpt as description
            - Attach a link back to the email
            - Set due date and labels
Tech stack: Google Apps Script, CardService, Trello REST API
```

---

## Example 310

**Intent:**
find big attachments in my gmail so i can free space

**Spec:**
```
Type:       Plugin (Gmail add-on)
Features:   - Search messages larger than a chosen size
            - List them sorted by size with sender and date
            - Save attachments to Drive before deleting
            - Move selected messages to trash
Tech stack: Google Apps Script, CardService, GmailApp (search "larger:"), DriveApp
```

---

## Example 311

**Intent:**
outlook signature manager for all staff with same design

**Spec:**
```
Type:       Plugin (Outlook add-in)
Auth:       Microsoft Entra ID SSO (User.Read)
Features:   - Insert a company signature automatically on new message and reply with event-based activation
            - Fill name, title and phone from the user's Microsoft Graph profile
            - Use different templates for new emails and replies
            - Let admins update the template centrally
Tech stack: JavaScript, Office Add-ins (OnNewMessageCompose event, setSignatureAsync), Microsoft Graph
```

---

## Example 312

**Intent:**
Outlook button to report phishing to our IT team

**Spec:**
```
Type:       Plugin (Outlook add-in)
Features:   - Add a "Report phishing" button on the read surface
            - Forward the email as an attachment to the security mailbox
            - Move the email to Junk
            - Show a thank-you message
Tech stack: JavaScript, Office Add-ins (Office.js, Outlook REST/Graph), XML manifest
```

---

## Example 313

**Intent:**
outlook meeting cost calculator, shows how much a meeting costs based on number of people

**Spec:**
```
Type:       Plugin (Outlook add-in)
Features:   - Read the attendee count and duration while composing a meeting
            - Multiply by an average hourly cost set by the user
            - Show the estimated cost in the task pane
            - Update live when attendees or times change
Storage:    Office roamingSettings (hourly cost)
Tech stack: JavaScript, Office Add-ins (Outlook appointment compose API, ItemChanged events)
```

---

## Example 314

**Intent:**
meeting notes template in outlook calendar invite

**Spec:**
```
Type:       Plugin (Outlook add-in)
Auth:       Microsoft Entra ID SSO (Notes.ReadWrite)
Features:   - Add a button to insert an agenda and notes template into a meeting body
            - Fill in date, attendees and title automatically
            - Save notes after the meeting to OneNote
            - Keep several templates
Tech stack: TypeScript, Office Add-ins (Office.js), Microsoft Graph OneNote API
```

---

## Example 315

**Intent:**
game mod update checker, tells me if any of my installed mods have new versions

**Spec:**
```
Type:       Command-line tool (mod management)
Data model: InstalledMod(id, name, installed_version, source_url)
Features:   - Read installed mods and versions from manifest files
            - Query each mod's release source (GitHub releases or a mod site API) for the latest version
            - Print a table of outdated mods with changelog links
            - Download updates on request with backups
Input:      Path to the mods folder
Tech stack: Python, requests, Rich, Typer
```

---

## Example 316

**Intent:**
tool to translate my game mod's text files into other languages

**Spec:**
```
Type:       Command-line tool (mod localization)
Features:   - Extract strings from mod localization files (JSON or YAML)
            - Translate missing keys with a machine translation API
            - Keep placeholders like {player} and %d intact
            - Write new locale files with the same structure
            - Report untranslated or too-long strings
Input:      Mod folder path, target languages
Tech stack: Python, DeepL API, PyYAML
```

---

## Example 317

**Intent:**
sprite sheet packer for my game sprites

**Spec:**
```
Type:       Command-line tool (game tool)
Features:   - Pack PNG sprites from a folder into one or more atlas images using a bin-packing algorithm
            - Trim transparent borders
            - Write a JSON atlas with frame positions
            - Add padding to avoid bleeding
            - Group animation frames by file name prefix
Input:      Folder of PNG sprites, max atlas size
Tech stack: Python, Pillow, rectpack
```

---

## Example 318

**Intent:**
crosshair overlay app for games that dont have a good one

**Spec:**
```
Type:       Desktop application (game overlay)
Features:   - Draw a crosshair in a transparent, click-through, always-on-top window centred on the screen
            - Choose shape, size, colour and thickness
            - Save several presets
            - Toggle visibility with a global hotkey
Storage:    Local JSON settings file
Tech stack: C#, .NET 8, WPF (transparent topmost window)
```

---

## Example 319

**Intent:**
generate a wiki website from my mod's item json files

**Spec:**
```
Type:       Command-line tool (static site generator)
Features:   - Read item, recipe and creature definitions from mod JSON files
            - Generate one HTML page per entry with stats and images
            - Create category index pages and search
            - Link recipes to their ingredients
Input:      Mod data folder
Tech stack: Python, Jinja2, Lunr.js
```

---

## Example 320

**Intent:**
grammer checker for everything i type in the browser

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Watch text typed into textareas and contenteditable fields
            - Send text to a grammar checking API after a typing pause
            - Underline issues and show suggestions on hover
            - Apply a suggestion with one click
            - Disable on chosen sites
Storage:    chrome.storage.sync (disabled sites, language)
Tech stack: TypeScript, Chrome Manifest V3, content script, LanguageTool API
```

---

## Example 321

**Intent:**
make a jira ticket from any page quick

**Spec:**
```
Type:       Browser extension (productivity)
Auth:       Atlassian OAuth 2.0 (3LO) via chrome.identity.launchWebAuthFlow
Features:   - Open a popup form with project, issue type, summary and description
            - Pre-fill the description with the page URL and selected text
            - Attach a screenshot of the visible tab
            - Create the issue via the Jira REST API and show its key with a link
Storage:    chrome.storage.local (tokens, last used project)
Tech stack: TypeScript, Chrome Manifest V3, Jira Cloud REST API v3
```

---

## Example 322

**Intent:**
see whats in localstorage and sessionstorage of a site and edit it

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Show localStorage and sessionStorage keys and values in a DevTools panel
            - Edit, add and delete entries
            - Pretty-print JSON values
            - Search keys
            - Export storage as JSON
Tech stack: JavaScript, Chrome Manifest V3, chrome.devtools.inspectedWindow.eval, Vue 3
```

---

## Example 323

**Intent:**
live css editor that remembers my css per site

**Spec:**
```
Type:       Browser extension (developer tools)
Data model: SiteStyle(domain, css, enabled)
Features:   - Open a CSS editor panel on any page
            - Apply the CSS live while typing
            - Save CSS per domain and re-inject it on later visits
            - Toggle custom styles on and off
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, chrome.scripting.insertCSS, CodeMirror 6
```

---

## Example 324

**Intent:**
toggle CORS off for local dev testing

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Add Access-Control-Allow-Origin and related headers to responses with declarativeNetRequest
            - Apply only to URL patterns the user lists
            - Toggle on and off from the toolbar with a red badge when on
            - Auto-disable after one hour
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, declarativeNetRequest (modifyHeaders on responseHeaders), chrome.alarms
```

---

## Example 325

**Intent:**
focus mode - when i turn it on, only my work sites open, everything else blocked till timer ends

**Spec:**
```
Type:       Browser extension (productivity)
Data model: FocusSession(start_at, duration_minutes, completed)
Features:   - Start a focus session with a duration from the popup
            - Allow only sites on an allowlist during the session
            - Show a blocked page with the remaining time
            - Prevent ending the session early unless a phrase is typed
            - Keep a log of completed sessions
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, declarativeNetRequest dynamic rules, chrome.alarms
```

---

## Example 326

**Intent:**
linkedin feed is just bragging, hide the feed but keep messages and jobs

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Hide the main feed on the LinkedIn home page
            - Keep navigation, messaging, notifications and jobs usable
            - Show a short motivational line instead of the feed
            - Toggle back on temporarily from the popup
Tech stack: JavaScript, Chrome Manifest V3, content script with injected CSS
```

---

## Example 327

**Intent:**
rss feed detector, shows button if page has a feed

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Find RSS and Atom <link> tags on the current page
            - Try common feed paths (/feed, /rss.xml) when none are linked
            - Show the toolbar icon as active when a feed is found
            - Copy the feed URL or open it in a chosen reader
Tech stack: JavaScript, Chrome Manifest V3, content script, chrome.action
```

---

## Example 328

**Intent:**
send this article to my kindle

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Extract the main article with Readability
            - Convert it to an EPUB with title, author and images
            - Email it to the user's Send-to-Kindle address through a small backend
            - Show a confirmation in the popup
API:        REST
            POST /send
Tech stack: TypeScript, Chrome Manifest V3, Mozilla Readability, epub-gen, Node.js backend with Nodemailer
```

---

## Example 329

**Intent:**
mouse gestures to go back, close tab, reopen tab

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Track right-button drag movements in a content script
            - Recognise directions like left (back), right (forward), down-right (close tab) and down-left (reopen tab)
            - Draw the gesture trail while dragging
            - Let the user remap gestures in options
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script, chrome.tabs and chrome.sessions APIs
```

---

## Example 330

**Intent:**
my kids (8 and 11) use the family laptop, i want to give them 1 hour of youtube a day and then it locks, and i want to see what they watched

**Spec:**
```
Type:       Browser extension (parental controls)
Auth:       Parent PIN (hashed) to change settings
Data model: DailyLimit(domain, minutes_per_day)
            WatchLog(video_title, url, watched_at, seconds)
Features:   - Count time spent on limited sites per day
            - Block the site with a friendly page when the limit is reached
            - Log watched video titles
            - Show a parent dashboard protected by the PIN
            - Allow extra time with the PIN
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, chrome.alarms, declarativeNetRequest, content script
```

---

## Example 331

**Intent:**
firefox extension that keeps facebook in its own container so it cant track me

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Create a dedicated container for Facebook domains
            - Open Facebook links in that container automatically
            - Reopen non-Facebook links from inside the container in the default container
            - Clear Facebook cookies from the default container on install
Tech stack: JavaScript, Firefox WebExtensions API (contextualIdentities, webRequest), Manifest V2 for Firefox
```

---

## Example 332

**Intent:**
canvas fingerprint protection

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Inject a script into the page's MAIN world before other scripts
            - Add small random noise to canvas toDataURL and getImageData results per session
            - Spoof WebGL vendor and renderer strings
            - Allow disabling per site when it breaks pages
Storage:    chrome.storage.sync (site exceptions)
Tech stack: JavaScript, Chrome Manifest V3, content script (run_at document_start, world MAIN)
```

---

## Example 333

**Intent:**
remind me to use cashback when i visit a shop that has it

**Spec:**
```
Type:       Browser extension (shopping)
Data model: CashbackOffer(store_domain, rate, portal_url, updated_at)
Features:   - Download a list of stores with cashback offers daily
            - Show a reminder banner when visiting a matching store
            - Link to activate the cashback through the portal
            - Snooze reminders per store for a day
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, content script, chrome.alarms
```

---

## Example 334

**Intent:**
find the return policy on a shop website quickly

**Spec:**
```
Type:       Browser extension (shopping)
Features:   - Search the current site's footer and help links for return or refund pages
            - Fetch the page and extract the return window, conditions and who pays shipping
            - Show a short summary in the popup
            - Link to the full policy
Tech stack: TypeScript, Chrome Manifest V3, chrome.scripting, OpenAI API (summary)
```

---

## Example 335

**Intent:**
track how much i spend online by reading order confirmation pages

**Spec:**
```
Type:       Browser extension (shopping)
Data model: Purchase(id, store, order_number, total, currency, purchased_at)
Features:   - Detect order confirmation pages by URL and text patterns
            - Extract order number and total
            - Save the purchase after the user confirms in a small prompt
            - Show monthly spending by store in a dashboard
            - Set a monthly budget with a warning
Storage:    IndexedDB
Tech stack: JavaScript, Chrome Manifest V3, content scripts, Chart.js
```

---

## Example 336

**Intent:**
pdf annotator in the browser for pdfs i open

**Spec:**
```
Type:       Browser extension (reading)
Data model: Annotation(pdf_url_hash, page, type, rect, color, text)
Features:   - Open PDF links in a custom viewer page
            - Highlight text, add notes and draw on pages
            - Save annotations per PDF
            - Export the PDF with annotations embedded
Storage:    IndexedDB
Tech stack: TypeScript, Chrome Manifest V3, PDF.js, pdf-lib
```

---

## Example 337

**Intent:**
new tab kanban board for my personal tasks

**Spec:**
```
Type:       Browser extension (new tab page)
Data model: Card(id, column, title, notes, order)
Features:   - Show To do, Doing and Done columns on the new tab page
            - Add, edit and drag cards between columns
            - Archive done cards older than a week
            - Sync the board across devices
Storage:    chrome.storage.sync
Tech stack: React, Vite, dnd-kit, Chrome Manifest V3 (chrome_url_overrides)
```

---

## Example 338

**Intent:**
new tab shows my stock watchlist

**Spec:**
```
Type:       Browser extension (new tab page)
Data model: WatchItem(symbol, added_at)
Features:   - Show watchlist symbols with price and daily change
            - Show a sparkline for each symbol
            - Add and remove symbols
            - Refresh every 5 minutes during market hours
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, Finnhub API
```

---

## Example 339

**Intent:**
Safari extension to hide the autoplay videos on news sites

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Pause autoplaying videos on page load
            - Remove muted autoplay attribute from video elements as they appear
            - Hide sticky floating video players
            - Allow autoplay per site
Storage:    browser.storage.local
Tech stack: Swift (container app), Safari Web Extension (JavaScript, Manifest V3), Xcode
```

---

## Example 340

**Intent:**
an edge extension that adds a sidebar notepad

**Spec:**
```
Type:       Browser extension (productivity)
Data model: Note(id, title, body, updated_at)
Features:   - Open a notepad in the browser side panel
            - Save notes automatically while typing
            - Support multiple notes with titles
            - Insert the current page link into the note
Storage:    chrome.storage.local
Tech stack: JavaScript, Microsoft Edge (Chromium) Manifest V3, chrome.sidePanel API
```

---

## Example 341

**Intent:**
Thunderbird add-on that sends a reminder if I forget an attachment when I write "attached"

**Spec:**
```
Type:       Plugin (Thunderbird add-on)
Features:   - Check the message body on send for words like attached, attachment, enclosed
            - Warn when no attachment is added
            - Support keywords in several languages
            - Let the user send anyway
Tech stack: JavaScript, Thunderbird MailExtensions API (compose.onBeforeSend)
```

---

## Example 342

**Intent:**
vs code color picker for colors in css and tailwind config

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Detect hex, rgb and hsl colours in CSS, SCSS and JS files
            - Show colour swatches with a DocumentColorProvider
            - Open the built-in colour picker to edit them
            - Convert between colour formats with a command
Tech stack: TypeScript, VS Code Extension API (DocumentColorProvider)
```

---

## Example 343

**Intent:**
quickly switch between my projects in vscode

**Spec:**
```
Type:       Plugin (VS Code extension)
Data model: Project(name, root_path, tags)
Features:   - Save the current folder as a project
            - Open a project from a quick pick in the current or new window
            - Auto-detect git repositories in configured folders
            - Show projects in a sidebar grouped by tag
Storage:    VS Code globalState
Tech stack: TypeScript, VS Code Extension API
```

---

## Example 344

**Intent:**
vscode extension with buttons for my favorite terminal commands

**Spec:**
```
Type:       Plugin (VS Code extension)
Data model: CommandButton(label, command, cwd)
Features:   - Read buttons from a workspace settings file
            - Show buttons in the status bar or a sidebar view
            - Run the command in a named terminal when clicked
            - Reuse the terminal if it already exists
Tech stack: TypeScript, VS Code Extension API (StatusBarItem, window.createTerminal)
```

---

## Example 345

**Intent:**
translate code comments to english, my team writes in chinese

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Detect comments with non-English text
            - Show the English translation on hover
            - Translate all comments in a file into a side-by-side preview
            - Replace comments in place with a command
Tech stack: TypeScript, VS Code Extension API (HoverProvider), Google Cloud Translation API
```

---

## Example 346

**Intent:**
terraform plan summary inside vscode

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Run terraform plan -json for the current module
            - Summarise resources to add, change and destroy in a tree view
            - Highlight destroy actions in red
            - Jump to the resource block in the .tf file
Tech stack: TypeScript, VS Code Extension API, Terraform CLI
```

---

## Example 347

**Intent:**
show how long each jupyter cell took to run, in vs code notebooks

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Listen for notebook cell execution events
            - Record start and end times per cell
            - Show duration in the cell status bar
            - Show the slowest cells in a summary view
Tech stack: TypeScript, VS Code Extension API (NotebookCellStatusBarItemProvider, notebook events)
```

---

## Example 348

**Intent:**
vscode extension to check my jsx for accessibility problems while typing

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Lint JSX and TSX files with accessibility rules on change
            - Show issues like missing alt text and buttons without labels as diagnostics
            - Link each issue to documentation
            - Offer quick fixes for simple issues
Tech stack: TypeScript, VS Code Extension API (DiagnosticCollection), ESLint with eslint-plugin-jsx-a11y
```

---

## Example 349

**Intent:**
jetbrains plugin shows how long my sql queries took in the editor next to the query

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Listen for query execution in the Database tools
            - Record execution time per query text
            - Show the last duration as an inlay hint above the query
            - Warn when a query is slower than a threshold
Tech stack: Kotlin, IntelliJ Platform SDK, DataGrip/Database Tools plugin API
```

---

## Example 350

**Intent:**
Blender add-on that renames and organizes objects by type into collections

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Add a panel in the 3D viewport sidebar
            - Move objects into collections by type (meshes, lights, cameras, empties)
            - Rename objects with a prefix and number
            - Remove empty collections
            - Support undo
Tech stack: Python, Blender Python API (bpy)
```

---

## Example 351

**Intent:**
blender addon export selected objects one by one as separate fbx files

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Export each selected object to its own FBX file named after the object
            - Reset each object's location to the origin during export
            - Choose export folder and scale
            - Report exported files in the info bar
Tech stack: Python, Blender Python API (bpy.ops.export_scene.fbx)
```

---

## Example 352

**Intent:**
anki add-on that shows how many cards I need to do per day to finish a deck by exam date

**Spec:**
```
Type:       Plugin (Anki add-on)
Features:   - Let the user set an exam date per deck
            - Count new and review cards remaining
            - Calculate the cards per day needed
            - Show the number on the deck browser screen
Storage:    Anki collection config
Tech stack: Python, Anki add-on API (aqt hooks), Qt
```

---

## Example 353

**Intent:**
logseq plugin that shows a random old journal entry every day

**Spec:**
```
Type:       Plugin (Logseq plugin)
Features:   - Pick a random journal page from more than 30 days ago
            - Show it in a sidebar panel on startup
            - Add a button to show another one
            - Link to open the full page
Tech stack: TypeScript, Logseq Plugin API (@logseq/libs)
```

---

## Example 354

**Intent:**
joplin plugin to make a table of contents in notes

**Spec:**
```
Type:       Plugin (Joplin plugin)
Features:   - Parse headings of the current note
            - Show a clickable table of contents in a side panel
            - Scroll the editor to a heading when clicked
            - Update on note change
Tech stack: TypeScript, Joplin Plugin API
```

---

## Example 355

**Intent:**
raycast extension to search my bookmarks from all browsers

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Read bookmarks from Chrome, Firefox and Safari profile files
            - Search them with fuzzy matching
            - Open a bookmark in its browser
            - Copy the URL with an action
Tech stack: TypeScript, React, Raycast API
```

---

## Example 356

**Intent:**
grafana panel plugin that shows a status grid of my servers

**Spec:**
```
Type:       Plugin (Grafana panel plugin)
Features:   - Render one tile per server from query results
            - Colour tiles by status thresholds
            - Show the latest value and last update time
            - Link each tile to a drill-down dashboard
            - Configure columns and thresholds in panel options
Tech stack: TypeScript, React, Grafana plugin SDK (@grafana/data, @grafana/ui)
```

---

## Example 357

**Intent:**
jupyterlab extension that adds a button to clear outputs and restart then run all

**Spec:**
```
Type:       Plugin (JupyterLab extension)
Features:   - Add a toolbar button to notebooks
            - Clear all outputs, restart the kernel and run all cells
            - Ask for confirmation before restarting
            - Add a command palette entry and shortcut
Tech stack: TypeScript, JupyterLab extension API (@jupyterlab/notebook)
```

---

## Example 358

**Intent:**
zotero plugin that renames pdf attachments to author_year_title

**Spec:**
```
Type:       Plugin (Zotero plugin)
Features:   - Rename PDF attachments using parent item metadata
            - Run automatically when a new PDF is added
            - Shorten long titles and remove illegal characters
            - Add a context-menu action to rename selected items
Tech stack: JavaScript, Zotero 7 plugin API (bootstrap)
```

---

## Example 359

**Intent:**
wp membership plugin, some posts only for paying members

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Membership(user_id, level, stripe_subscription_id, status, expires_at)
Features:   - Mark posts as members-only with a checkbox in the editor
            - Show a teaser and a join box to non-members
            - Sell monthly memberships with Stripe Checkout
            - Update membership status from Stripe webhooks
            - Show members and their status in wp-admin
API:        WordPress REST API
            POST /wp-json/members/v1/checkout
            POST /wp-json/members/v1/stripe-webhook
Storage:    Custom MySQL table via $wpdb, post meta
Tech stack: PHP, WordPress hooks (the_content filter), stripe-php
```

---

## Example 360

**Intent:**
quiz plugin for wordpress for my online course, students get score and certificate

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Quiz(title, questions_json, pass_mark)
            QuizAttempt(id, quiz_id, user_id, score, passed, created_at)
Features:   - Build quizzes with multiple choice questions in a block
            - Grade answers on submit and show the score
            - Save attempts for logged-in students
            - Generate a PDF certificate when the pass mark is reached
            - Show attempts per student in wp-admin
Storage:    WordPress database, custom table (attempts)
Tech stack: PHP, WordPress Block API, WordPress REST API, Dompdf
```

---

## Example 361

**Intent:**
wordpress search is bad, make it use algolia

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Index posts, pages and products into an Algolia index on save and delete
            - Bulk reindex from a settings page
            - Replace the search form with instant search results as you type
            - Respect post status and exclude private content
Storage:    Algolia index, WordPress options (API keys)
Tech stack: PHP, WordPress hooks (save_post, delete_post), algoliasearch-client-php, InstantSearch.js
```

---

## Example 362

**Intent:**
wp broken link checker that runs weekly and emails me

**Spec:**
```
Type:       Plugin (WordPress)
Data model: LinkCheck(url, post_id, status_code, last_checked_at)
Features:   - Extract links from published posts and pages
            - Check each link's HTTP status in background batches
            - Email a weekly report of broken links
            - Show broken links in an admin table with an "Edit post" link
            - Unlink or update a URL from the table
Storage:    Custom MySQL table via $wpdb
Tech stack: PHP, WP-Cron, wp_remote_head, WP_List_Table
```

---

## Example 363

**Intent:**
sticky header plugin

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Make the theme's header stick to the top on scroll using a CSS selector from settings
            - Shrink the header and add a shadow after scrolling 100px
            - Hide on scroll down and show on scroll up optionally
            - Disable on mobile
Storage:    WordPress options table
Tech stack: PHP, WordPress hooks (wp_enqueue_scripts), vanilla JavaScript, CSS
```

---

## Example 364

**Intent:**
author box under posts with photo bio and social links

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Add bio and social profile fields to user profiles
            - Show an author box after single posts
            - Use the Gravatar or an uploaded photo
            - Provide a block for custom placement
Storage:    WordPress user meta
Tech stack: PHP, WordPress hooks (the_content, show_user_profile), Block API
```

---

## Example 365

**Intent:**
real estate listings wordpress with filters price bedrooms location

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Property(title, description, price, bedrooms, bathrooms, area_m2, city, status, gallery_ids)
Features:   - Register a Property post type with custom fields
            - Show a listings page with filters for price range, bedrooms and city
            - Show a property page with gallery and map
            - Add an enquiry form that emails the agent
Storage:    WordPress database (posts, post meta)
Tech stack: PHP, WP_Query with meta_query, Leaflet, wp_mail
```

---

## Example 366

**Intent:**
woocommerce product add on: customer types text for engraving, +5 euro

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Add an "Engraving text" field to selected products with a character limit
            - Add a fixed fee to the item price when filled
            - Save the text as cart item data and order item meta
            - Show the text in cart, checkout, emails and admin order
Storage:    Product meta (settings), order item meta
Tech stack: PHP, WooCommerce hooks (woocommerce_add_cart_item_data, woocommerce_before_calculate_totals)
```

---

## Example 367

**Intent:**
product compare table woocommerce

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Add a "Compare" button to product cards
            - Keep up to 4 products in a compare list in the session
            - Show a table with price, rating and attributes side by side
            - Remove products from the comparison
Tech stack: PHP, WooCommerce hooks, WC_Session, JavaScript
```

---

## Example 368

**Intent:**
shopify wishlist app, customers save products with a heart

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant), customer account via App Proxy signature
Data model: WishlistItem(shop_domain, customer_id, product_id, variant_id, added_at)
Features:   - Add a heart button on product cards and pages via a theme app extension
            - Save items for logged-in customers and in localStorage for guests
            - Merge guest items on login
            - Show a wishlist page
            - Show the most wishlisted products in the admin
Storage:    PostgreSQL
Tech stack: Node.js, Shopify CLI, Remix, App Proxy, Theme App Extension
```

---

## Example 369

**Intent:**
shopify local pickup in store with a ready-for-pickup sms

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Data model: PickupOrder(order_id, location_id, ready_at, picked_up_at)
Features:   - List pickup orders for each location in the admin
            - Mark an order as ready for pickup
            - Send the customer an SMS with pickup instructions
            - Mark as picked up and fulfil the order
Storage:    PostgreSQL
Tech stack: Node.js, Shopify Admin GraphQL API (fulfillmentOrders), Remix, Polaris, Twilio
```

---

## Example 370

**Intent:**
figma qr code generator

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Enter a URL or text in the plugin UI
            - Generate a QR code as vector rectangles
            - Choose foreground and background colours
            - Insert it at the viewport centre
Tech stack: TypeScript, Figma Plugin API, qrcode library
```

---

## Example 371

**Intent:**
hey so im a uni student and i always have like 40 tabs open for research, i want something that lets me save all of them into a group for each assignment and write a little note why i saved each one, then later make a reference list from them in APA

**Spec:**
```
Type:       Browser extension (productivity)
Data model: Project(id, name, created_at)
            Source(id, project_id -> Project, title, url, author, published_date, note, accessed_at)
Features:   - Save all tabs or the current tab into an assignment project
            - Add a note to each saved source
            - Read author and date from page metadata
            - Generate an APA reference list for a project
            - Copy or export the list as a .docx-friendly text
Storage:    IndexedDB
Tech stack: TypeScript, Chrome Manifest V3, React (extension page), citation-js
```

---

## Example 372

**Intent:**
chrome extention that auto refresh a page every x seconds

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Set a refresh interval for the current tab from the popup
            - Reload the tab with chrome.alarms or a timer
            - Show a countdown on the badge
            - Stop when the page content contains a chosen keyword and notify
Tech stack: JavaScript, Chrome Manifest V3, chrome.alarms, chrome.notifications
```

---

## Example 373

**Intent:**
wanna block all the gambling sites for my brother, he asked me to help him

**Spec:**
```
Type:       Browser extension (privacy)
Auth:       Password set by the helper to disable or uninstall-protect settings
Features:   - Block a maintained list of gambling domains with declarativeNetRequest
            - Block searches containing gambling keywords
            - Show a supportive message with a helpline link
            - Require the helper's password to change settings
            - Notify the helper by email if the extension is disabled
Storage:    chrome.storage.local (hashed password, settings)
Tech stack: JavaScript, Chrome Manifest V3, declarativeNetRequest, chrome.management.onDisabled
```

---

## Example 374

**Intent:**
ext that saves every form i type so i dont lose text if the page crashes

**Spec:**
```
Type:       Browser extension (productivity)
Data model: FormDraft(url, field_selector, text, saved_at)
Features:   - Save text typed in textareas and contenteditable fields every few seconds
            - Offer to restore saved text when the same page is reopened
            - List recent drafts in the popup
            - Delete drafts after 7 days
            - Never save password or credit card fields
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 375

**Intent:**
Please, I need extension to show the exchange of my salary hours, I am freelancer from Philippines and paid in USD, when I see prices in PHP I want to know how many hours of work it cost.

**Spec:**
```
Type:       Browser extension (shopping)
Features:   - Let the user enter hourly rate in USD
            - Detect prices in PHP (₱) on shopping pages
            - Convert prices using the current USD/PHP rate
            - Show "≈ 3.5 hours of work" next to each price
            - Refresh the rate daily
Storage:    chrome.storage.sync (rate, settings)
Tech stack: JavaScript, Chrome Manifest V3, content script, chrome.alarms, Frankfurter API
```

---

## Example 376

**Intent:**
Me and my team want VS Code extension, when somebody open file which another person is editing in the same time, show warning. We use git but conflicts every day.

**Spec:**
```
Type:       Plugin (VS Code extension)
Auth:       Team token for the presence server
Data model: Presence(user_name, repo_id, file_path, last_seen_at)
Features:   - Report which files the user is currently editing to a small presence server
            - Show a warning when opening a file another teammate is editing
            - Show teammates' names in the editor tab via a status bar item
            - Expire presence after 5 minutes of inactivity
API:        WebSocket
            WS /presence
Storage:    Redis (presence with TTL)
Tech stack: TypeScript, VS Code Extension API, Node.js + ws server
```

---

## Example 377

**Intent:**
Bonjour, I want WordPress plugin for my bakery, customers order cakes online with date for picking up and pay on site. Sorry for my english.

**Spec:**
```
Type:       Plugin (WordPress)
Data model: CakeOrder(id, customer_name, phone, email, cake_type, size, message_on_cake, pickup_date, status)
Features:   - Show an order form with cake type, size, text on cake and pickup date via shortcode
            - Block pickup dates less than 2 days ahead and closed days
            - Email the bakery and the customer a confirmation
            - List orders by pickup date in wp-admin with status changes
Storage:    Custom MySQL table via $wpdb
Tech stack: PHP, WordPress hooks, wp_mail, flatpickr
```

---

## Example 378

**Intent:**
plz i need sheets addon that make a schedule for workers in restaurant, each person say what days they can work and it fill the week

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Features:   - Read staff availability from an "Availability" sheet
            - Read required staff per shift from a "Needs" sheet
            - Assign shifts fairly while respecting availability and max hours
            - Write the weekly roster to a new sheet with colours per person
            - Highlight shifts that could not be filled
Tech stack: Google Apps Script, SpreadsheetApp
```

---

## Example 379

**Intent:**
i want a figma plugin but i dont know how, it should make the same button in all sizes small medium large

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Take the selected button component
            - Create small, medium and large variants with scaled padding, font size and radius
            - Combine them into a component set with a Size property
            - Let the user set the scale values in the UI
Tech stack: TypeScript, Figma Plugin API (combineAsVariants)
```

---

## Example 380

**Intent:**
obsidian plugin pls: when i paste a youtube link it should make a note with title thumbnail and transcript

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Detect a pasted YouTube URL and offer to create a note
            - Fetch title, channel and thumbnail via oEmbed
            - Fetch the transcript when captions are available
            - Create a note from a template with timestamps linked to the video
Tech stack: TypeScript, Obsidian Plugin API (editor-paste event), YouTube oEmbed, youtube-transcript
```

---

## Example 381

**Intent:**
ok weird one. i play a lot of browser games and want an extension that shows a little overlay with a timer of how long ive been playing and nags me after an hour

**Spec:**
```
Type:       Browser extension (productivity)
Data model: PlaySession(domain, started_at, seconds)
Features:   - Let the user mark sites as game sites
            - Show a small draggable timer overlay on those sites
            - Show a reminder after a set time and every 15 minutes after that
            - Show total play time per day in the popup
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, content script, chrome.alarms
```

---

## Example 382

**Intent:**
a userscript that adds a download button to images on any gallery site

**Spec:**
```
Type:       Browser extension (userscript)
Features:   - Add a download button on hover over images larger than 200px
            - Download the highest-resolution source from srcset
            - Name files with page title and index
            - Download all images on the page as a zip
Tech stack: JavaScript, Tampermonkey/Violentmonkey userscript (GM_download), JSZip
```

---

## Example 383

**Intent:**
browser extension to rate how readable the text i wrote is

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Analyse the text in the focused editor or the selection
            - Compute Flesch reading ease and grade level
            - Highlight very long sentences and complex words
            - Show the score in a floating badge
Tech stack: JavaScript, Chrome Manifest V3, content script, text-readability library
```

---

## Example 384

**Intent:**
show me my screen time per site but for firefox and make it private, nothing leaves my computer

**Spec:**
```
Type:       Browser extension (productivity)
Data model: UsageEntry(date, domain, seconds)
Features:   - Track active time per domain using tab and window focus
            - Store data only locally
            - Show daily and weekly charts
            - Export and delete all data from settings
Storage:    browser.storage.local
Tech stack: JavaScript, Firefox WebExtensions API, Chart.js
```

---

## Example 385

**Intent:**
VS Code ext that reads my code out loud for when my eyes are tired

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Read the selection or current line aloud
            - Pronounce symbols and operators in words
            - Read the next line with a shortcut
            - Adjust voice and speed
Tech stack: TypeScript, VS Code Extension API, say.js (system text-to-speech)
```

---

## Example 386

**Intent:**
excel addin for teachers to make random seating plan

**Spec:**
```
Type:       Plugin (Excel add-in)
Features:   - Read student names from a selected column
            - Ask for rows and columns of desks
            - Place students randomly with an option to keep certain pairs apart
            - Draw the seating plan on a new sheet with borders
            - Reshuffle with one click
Tech stack: JavaScript, Office Add-ins (Excel JavaScript API)
```

---

## Example 387

**Intent:**
google docs add-on that makes a glossary from bold words

**Spec:**
```
Type:       Plugin (Google Docs add-on)
Features:   - Find all bold words and phrases in the document
            - Ask for or fetch a definition for each
            - Insert an alphabetical glossary section at the end
            - Link each term in the text to its glossary entry
Tech stack: Google Apps Script, DocumentApp, Free Dictionary API
```

---

## Example 388

**Intent:**
gmail add on: show sentiment of customer emails so we answer angry ones first

**Spec:**
```
Type:       Plugin (Gmail add-on)
Features:   - Analyse the open email's text sentiment
            - Show a mood score and label in the side card
            - Label inbox threads by sentiment with a 15-minute trigger
            - Create a filter view for "Urgent - negative"
Tech stack: Google Apps Script, CardService, GmailApp, Google Cloud Natural Language API
```

---

## Example 389

**Intent:**
chrome extension that copies a table from any webpage into csv or excel

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Highlight tables on hover in selection mode
            - Extract the clicked table including merged cells
            - Copy as CSV or TSV for pasting into spreadsheets
            - Download as .xlsx
Tech stack: JavaScript, Chrome Manifest V3, content script, SheetJS
```

---

## Example 390

**Intent:**
scrape product info to google sheets from a web page via extension

**Spec:**
```
Type:       Browser extension (productivity)
Auth:       Google OAuth via chrome.identity (Sheets scope)
Features:   - Let the user click elements to define fields (name, price, rating)
            - Save the field selectors as a recipe per site
            - Extract fields from the current page or all items in a list
            - Append rows to a chosen Google Sheet
Storage:    chrome.storage.local (recipes)
Tech stack: TypeScript, Chrome Manifest V3, content script, Google Sheets API
```

---

## Example 391

**Intent:**
Old person here, the text on websites is too small and grey. I just want everything bigger and black, please make it simple.

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Increase base font size on all pages
            - Make body text black on white with stronger contrast
            - Offer three large buttons (normal, big, very big) in the popup
            - Remember the choice for all sites
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, chrome.scripting.insertCSS
```

---

## Example 392

**Intent:**
line focus reading ruler

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Dim the page except a horizontal band around the mouse
            - Adjust band height and dim opacity
            - Move the band with arrow keys
            - Toggle with a keyboard shortcut
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script, chrome.commands
```

---

## Example 393

**Intent:**
show a warning if a site asks for camera or microphone

**Spec:**
```
Type:       Browser extension (privacy)
Features:   - Detect calls to getUserMedia by wrapping it in the page's MAIN world
            - Show a banner naming the site and device requested
            - Keep a log of sites that asked
            - Block requests for sites on a deny list
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, content script (world MAIN, document_start)
```

---

## Example 394

**Intent:**
auto-close tabs i havent looked at in 3 days, but save them first

**Spec:**
```
Type:       Browser extension (productivity)
Data model: ClosedTab(url, title, closed_at)
Features:   - Track last active time per tab
            - Close tabs inactive for a set number of days, skipping pinned tabs
            - Save closed tabs to a list
            - Reopen tabs from the list in the popup
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, chrome.tabs, chrome.alarms
```

---

## Example 395

**Intent:**
chrome extension giving me keyboard shortcut to switch to the last used tab

**Spec:**
```
Type:       Browser extension (productivity)
Features:   - Track tab activation order in the service worker
            - Switch to the previously active tab with Alt+Q
            - Cycle back further with repeated presses
            - Work across windows
Tech stack: JavaScript, Chrome Manifest V3, chrome.commands, chrome.tabs, chrome.storage.session
```

---

## Example 396

**Intent:**
hide spoilers for my tv shows on reddit twitter and youtube

**Spec:**
```
Type:       Browser extension (productivity)
Data model: SpoilerTerm(term, show_name, until_date)
Features:   - Let the user add show names and character names as spoiler terms
            - Blur posts, titles and thumbnails containing them
            - Reveal on click
            - Auto-expire terms after a set date
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script with MutationObserver
```

---

## Example 397

**Intent:**
show github stars and last commit date next to github links on any site

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Find links to GitHub repositories on the page
            - Fetch stars and last push date from the GitHub API
            - Show a small badge after each link
            - Cache results for a day to stay under rate limits
Storage:    chrome.storage.local (cache)
Tech stack: JavaScript, Chrome Manifest V3, content script, GitHub REST API
```

---

## Example 398

**Intent:**
stack overflow: show answers sorted by newest and mark outdated ones

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Re-sort answers by date on question pages
            - Mark answers older than a set number of years as possibly outdated
            - Show the answer's score and date prominently
            - Remember the preferred sort
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 399

**Intent:**
vscode extension to view sqlite database files

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Open .db and .sqlite files in a custom editor
            - List tables and views in a sidebar
            - Show table rows with paging
            - Run SQL queries and show results in a grid
Tech stack: TypeScript, VS Code Extension API (CustomReadonlyEditorProvider, webview), sql.js (WebAssembly)
```

---

## Example 400

**Intent:**
vs code: open the github page for the current line

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Read the git remote URL and current branch or commit
            - Build the GitHub URL with #L line anchors for the selection
            - Open it in the browser or copy it
            - Support GitLab and Bitbucket URL formats
Tech stack: TypeScript, VS Code Extension API, vscode.git API
```

---

## Example 401

**Intent:**
intellij plugin to show the todo count per file in the project tree

**Spec:**
```
Type:       Plugin (JetBrains IDE plugin)
Features:   - Count TODO items per file using the TODO index
            - Show the count next to file names in the project view
            - Update on file change
            - Hide counts in settings
Tech stack: Kotlin, IntelliJ Platform SDK (ProjectViewNodeDecorator, PsiTodoSearchHelper)
```

---

## Example 402

**Intent:**
wordpress plugin that shows a different hello message depending on time of day

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Provide a [greeting] shortcode
            - Show good morning, afternoon or evening based on the site timezone
            - Include the logged-in user's first name
            - Set custom messages in settings
Storage:    WordPress options table
Tech stack: PHP, WordPress Shortcode API, wp_date
```

---

## Example 403

**Intent:**
woocommerce: send a review request email a week after order completed

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Schedule an email 7 days after an order is completed
            - List purchased products with links to their review forms
            - Skip customers who already reviewed
            - Let admins set delay and email text
Tech stack: PHP, WooCommerce hooks (woocommerce_order_status_completed), Action Scheduler, WC_Email
```

---

## Example 404

**Intent:**
wordpress plugin that posts my new blog posts to mastodon automatically

**Spec:**
```
Type:       Plugin (WordPress)
Features:   - Post title, excerpt and link to Mastodon when a post is published
            - Add tags as hashtags
            - Store the toot URL in post meta
            - Let the author skip posting per post
Storage:    WordPress options (instance URL, access token), post meta
Tech stack: PHP, WordPress hooks (transition_post_status), Mastodon API
```

---

## Example 405

**Intent:**
woo product feed for google merchant center

**Spec:**
```
Type:       Plugin (WooCommerce)
Features:   - Generate an XML product feed with id, title, price, availability, image and GTIN
            - Map categories to Google product categories
            - Include variations as separate items
            - Regenerate the feed hourly and serve it at a fixed URL
Tech stack: PHP, WooCommerce product API, WP-Cron, XMLWriter
```

---

## Example 406

**Intent:**
chrome extension: block me from buying stuff after midnight lol

**Spec:**
```
Type:       Browser extension (shopping)
Features:   - Detect checkout and cart pages on shopping sites
            - Block them between midnight and 7 am with a sleepy reminder page
            - Allow adding items to a "decide tomorrow" list
            - Configure the hours
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, declarativeNetRequest, content script
```

---

## Example 407

**Intent:**
shopify app that hides payment methods like cash on delivery for orders over 300

**Spec:**
```
Type:       Plugin (Shopify app)
Auth:       Shopify OAuth app install (merchant)
Features:   - Let the merchant define rules by cart total, country or customer tag
            - Hide or reorder payment methods at checkout with a Payment Customization Function
            - Store rules in a metafield on the customization
            - Preview which methods show for a sample cart
Tech stack: Shopify Functions (JavaScript), Shopify CLI, Remix, Polaris
```

---

## Example 408

**Intent:**
figma plugin to export all icons as svg in a zip

**Spec:**
```
Type:       Plugin (Figma plugin)
Features:   - Find all components on a page named like icon/*
            - Export each as SVG with exportAsync
            - Name files from the component name in kebab-case
            - Bundle them into a zip for download
Tech stack: TypeScript, Figma Plugin API, JSZip
```

---

## Example 409

**Intent:**
obsidian: show reading time at top of each note

**Spec:**
```
Type:       Plugin (Obsidian plugin)
Features:   - Count words in the active note
            - Show estimated reading time in the status bar
            - Show it in the note header in reading view
            - Configure words per minute
Tech stack: TypeScript, Obsidian Plugin API
```

---

## Example 410

**Intent:**
notion clipper for youtube videos into my "watch later" database

**Spec:**
```
Type:       Browser extension (productivity)
Auth:       Notion integration token entered in options
Features:   - Add a "Save to Notion" button on YouTube watch pages
            - Create a page in a chosen database with title, channel, duration and URL
            - Set a status property to "To watch"
            - Show a confirmation toast
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Manifest V3, content script, Notion API
```

---

## Example 411

**Intent:**
discord rich presence for my own little indie game made in godot

**Spec:**
```
Type:       Desktop game (integration)
Features:   - Connect to the local Discord client via IPC
            - Show current level, character and elapsed time
            - Update presence when the player changes level
            - Disconnect cleanly on exit
Tech stack: Godot 4, GDScript, discord-rpc GDExtension
```

---

## Example 412

**Intent:**
lua console mod tool for my game so testers can spawn items while playing

**Spec:**
```
Type:       Desktop game (debug console)
Features:   - Open an in-game console with the ~ key
            - Run Lua commands with a sandboxed API (spawn_item, teleport, set_health)
            - Autocomplete command names
            - Keep command history
            - Disable in release builds
Tech stack: C++, SDL2, Lua 5.4, sol2
```

---

## Example 413

**Intent:**
hot reload for mod scripts so i dont have to restart the game every time

**Spec:**
```
Type:       Desktop game (mod tooling)
Features:   - Watch the mods folder for script file changes
            - Unload the changed mod's handlers and reload its script
            - Keep game state while reloading
            - Show reload errors in an on-screen log
Tech stack: C#, .NET FileSystemWatcher, MoonSharp, MonoGame
```

---

## Example 414

**Intent:**
map editor plugin for tiled to export to my game format

**Spec:**
```
Type:       Plugin (Tiled extension)
Features:   - Register a custom map format in Tiled
            - Export tile layers, object layers and properties to the game's JSON format
            - Validate required object properties before export
            - Import the format back into Tiled
Tech stack: JavaScript, Tiled scripting API (tiled.registerMapFormat)
```

---

## Example 415

**Intent:**
achievement tracker overlay for my steam-less indie game collection

**Spec:**
```
Type:       Desktop application (game tool)
Data model: Game(id, name, exe_path)
            Achievement(id, game_id -> Game, name, description, unlocked_at)
Features:   - Add games and define achievements manually
            - Mark achievements as unlocked with a hotkey while playing
            - Show a small overlay with progress
            - Show completion percentage per game
Storage:    SQLite
Tech stack: Python, PySide6, SQLite
```

---

## Example 416

**Intent:**
aseprite extension to export each layer as a separate png

**Spec:**
```
Type:       Plugin (Aseprite extension)
Features:   - Add a menu command to export layers
            - Save each visible layer as its own PNG named after the layer
            - Optionally export each frame of each layer
            - Choose the output folder and scale
Tech stack: Lua, Aseprite scripting API
```

---

## Example 417

**Intent:**
vs code extension for writing mods: autocomplete for my game's lua modding api

**Spec:**
```
Type:       Plugin (VS Code extension)
Features:   - Provide completions for the game's Lua API functions and events
            - Show function signatures and docs on hover
            - Validate mod.json manifests against a JSON schema
            - Add a command to package the mod as a zip
Tech stack: TypeScript, VS Code Extension API, Lua Language Server definition files, JSON Schema
```

---

## Example 418

**Intent:**
chrome extension: when i'm on a recipe site, convert cups and ounces to grams

**Spec:**
```
Type:       Browser extension (reading)
Features:   - Find volume and weight measurements in recipe text
            - Convert cups, tablespoons and ounces to grams and millilitres using ingredient densities
            - Show conversions inline in brackets
            - Toggle metric or imperial in the popup
Tech stack: JavaScript, Chrome Manifest V3, content script
```

---

## Example 419

**Intent:**
new tab page shows a world map with times in cities my team is in

**Spec:**
```
Type:       Browser extension (new tab page)
Data model: TeamCity(name, timezone, teammate_names)
Features:   - Show a world map with markers for chosen cities
            - Show local time and day/night status per city
            - Highlight cities currently within working hours
            - Add and remove cities in settings
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Manifest V3, Leaflet, Intl.DateTimeFormat
```

---

## Example 420

**Intent:**
browser extension that makes a summary of youtube video from the transcript

**Spec:**
```
Type:       Browser extension (reading)
Auth:       User's LLM API key in options
Features:   - Add a "Summarise" button on YouTube watch pages
            - Fetch the video's caption track
            - Send the transcript to an LLM for a summary with timestamps
            - Show the summary in a panel next to the video with clickable timestamps
Tech stack: TypeScript, Chrome Manifest V3, content script, OpenAI API
```

---

## Example 421

**Intent:**
sheets add-on that pulls my google analytics numbers into a sheet every monday

**Spec:**
```
Type:       Plugin (Google Sheets add-on)
Auth:       Google OAuth (analytics.readonly scope)
Features:   - Choose a GA4 property and metrics in a sidebar
            - Run a report for the last 7 days
            - Append the results as a new row
            - Run every Monday with a time trigger
            - Draw a chart of weekly trends
Tech stack: Google Apps Script, Google Analytics Data API (advanced service), SpreadsheetApp
```

---
