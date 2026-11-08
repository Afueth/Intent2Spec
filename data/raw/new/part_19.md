## Example 1

**Intent:**
browser add-on that grabs the citation of whatever article im reading

**Spec:**
```
Type:       Browser extension (citation capture)
Data model: Citation(id, title, authors, year, journal, doi, url, captured_at)
            Style(id, name)
Features:   - Read title, authors, DOI and date from the page's meta tags
            - Fall back to Crossref lookup when only a DOI is found
            - Format the citation in APA, MLA or Chicago
            - Copy the formatted citation to the clipboard in one click
            - Keep a list of captured citations in the popup
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, Crossref REST API, citation-js
```

---

## Example 2

**Intent:**
I watch a lot of recorded lectures on YouTube for my uni course and I want to type notes that are linked to the exact second of the video, so when I click a note it jumps back there.

**Spec:**
```
Type:       Browser extension (lecture video notes)
Data model: Video(id, platform, video_id, title)
            Note(id, video_id -> Video, timestamp_seconds, text, created_at)
Features:   - Add a note stamped with the current playback time
            - Show notes in a side panel next to the video
            - Seek the video to a note's timestamp when it is clicked
            - Export all notes for a video as Markdown
            - Search notes across all saved videos
Storage:    IndexedDB (via Dexie.js)
Tech stack: TypeScript, Chrome Extension Manifest V3, YouTube IFrame Player API, Dexie.js
```

---

## Example 3

**Intent:**
Zotero plugin that auto-renames PDF attachments

**Spec:**
```
Type:       Plugin (Zotero)
Data model: RenameRule(id, pattern, max_title_length, lowercase)
Features:   - Rename attached PDFs using a pattern like {author}_{year}_{title}
            - Strip illegal filename characters and trim long titles
            - Rename automatically when a new attachment is added
            - Add a right-click menu item to rename selected items
            - Show a preview of the new name in the preferences pane
Storage:    Zotero preferences store
Tech stack: JavaScript, Zotero 7 plugin API (bootstrap.js)
```

---

## Example 4

**Intent:**
something for recruiters to save private notes on LinkedIn profiles

**Spec:**
```
Type:       Browser extension (recruiter notes)
Data model: Candidate(id, profile_url, name, headline)
            Note(id, candidate_id -> Candidate, text, stage, created_at)
Features:   - Detect when a LinkedIn profile page is open
            - Show a notes panel beside the profile
            - Tag each candidate with a pipeline stage (sourced, contacted, interviewing)
            - Show a badge on profiles that already have notes
            - Export candidates and notes to CSV
API:        REST
            GET  /candidates?url={profile_url}
            POST /candidates
            POST /candidates/{id}/notes
Storage:    Firebase Firestore
Tech stack: JavaScript, Chrome Extension Manifest V3, Firebase
```

---

## Example 5

**Intent:**
a jira plugin that shows how long each ticket sat in every status

**Spec:**
```
Type:       Plugin (Jira Cloud)
Data model: StatusChange(id, issue_key, from_status, to_status, changed_at)
Features:   - Read the issue changelog through the Jira REST API
            - Calculate total time spent in each status
            - Show a bar chart of time per status on the issue view
            - Highlight statuses that exceed a configurable limit
            - Show average time in status for a whole project
API:        Jira REST
            GET  /rest/api/3/issue/{issueKey}/changelog
Storage:    Forge storage API
Tech stack: Atlassian Forge, JavaScript, React (Forge UI Kit)
```

---

## Example 6

**Intent:**
obsidian plugin to turn my daily notes into a habit tracker heatmap

**Spec:**
```
Type:       Plugin (Obsidian)
Data model: HabitSetting(name, frontmatter_key, color)
Features:   - Read habit checkboxes from the frontmatter of daily notes
            - Draw a year heatmap per habit inside a code block
            - Show the current and longest streak
            - Open the daily note when a heatmap cell is clicked
            - Let users pick habits and colors in a settings tab
Storage:    Obsidian plugin data.json
Tech stack: TypeScript, Obsidian API, esbuild
```

---

## Example 7

**Intent:**
blender addon that makes low poly rocks

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Add a "Low Poly Rock" entry to the Add Mesh menu
            - Generate a rock from a subdivided icosphere with random vertex displacement
            - Expose seed, size, roughness and face count in the redo panel
            - Apply flat shading and an optional decimate modifier
            - Generate a batch of varied rocks in a grid
Tech stack: Python, Blender bpy API
```

---

## Example 8

**Intent:**
Hello, I am real estate agent. I want small tool in Chrome, when I open house listing on Zillow it shows me price per square meter and how long it is on market. Thank you.

**Spec:**
```
Type:       Browser extension (real estate)
Data model: ListingSnapshot(id, url, price, area_sqft, days_on_market, viewed_at)
Features:   - Read price, living area and listing date from the listing page
            - Calculate price per square foot and per square meter
            - Show days on market in an overlay badge
            - Save viewed listings to a comparison list
            - Export the comparison list to CSV
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 9

**Intent:**
anki addon to show a little chart of how many cards i did per hour of the day

**Spec:**
```
Type:       Plugin (Anki add-on)
Features:   - Query the review log from the collection database
            - Group reviews by hour of the day for a chosen date range
            - Show average retention per hour
            - Draw a bar chart in a new Stats window
            - Add a menu item under Tools to open it
Storage:    Anki collection (SQLite revlog table)
Tech stack: Python, Anki add-on API, PyQt6, Matplotlib
```

---

## Example 10

**Intent:**
OBS plugin that shows a countdown timer before my stream starts

**Spec:**
```
Type:       Plugin (OBS Studio)
Features:   - Add a "Countdown" text source type
            - Count down to a set clock time or a duration
            - Show custom text when the timer reaches zero
            - Switch to a chosen scene automatically when the countdown ends
            - Let users set font, color and format in the source properties
Tech stack: C, OBS Studio plugin API (libobs), CMake
```

---

## Example 11

**Intent:**
make a home assistant integration for my cheap wifi plant sensor

**Spec:**
```
Type:       Plugin (Home Assistant custom integration)
Data model: PlantSensor(id, ip_address, name)
            Reading(sensor_id -> PlantSensor, moisture_pct, temperature_c, light_lux, battery_pct, recorded_at)
Features:   - Discover sensors on the local network with zeroconf
            - Set up devices through a config flow in the UI
            - Create sensor entities for moisture, temperature, light and battery
            - Poll each device every 5 minutes with a DataUpdateCoordinator
            - Fire an event when moisture drops below a threshold
Storage:    Home Assistant recorder (SQLite)
Tech stack: Python, Home Assistant integration framework, aiohttp
```

---

## Example 12

**Intent:**
grafana panel that shows a server rack layout with temps on each server

**Spec:**
```
Type:       Plugin (Grafana panel)
Data model: RackSlot(rack_name, position_u, height_u, host, temperature_metric)
Features:   - Draw racks and servers as boxes by rack unit position
            - Color each server by its latest temperature value
            - Show host details and a sparkline on hover
            - Configure rack layout as JSON in panel options
            - Link each server to a drill-down dashboard
Tech stack: TypeScript, React, Grafana plugin SDK (@grafana/data, @grafana/ui)
```

---

## Example 13

**Intent:**
raycast extension to search our company wiki

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Search wiki pages as the user types
            - Show page title, space and last edited date in the list
            - Show a Markdown preview of the selected page
            - Open the page in the browser or copy its link
            - Cache recent results for fast repeat searches
API:        REST
            GET  /wiki/rest/api/search?cql={query}
Tech stack: TypeScript, React, Raycast API, Confluence Cloud REST API
```

---

## Example 14

**Intent:**
i have dyslexia and reading long websites is hard. can you make a chrome thing that changes the font, adds more space between lines and lets me follow with a colored line under my mouse

**Spec:**
```
Type:       Browser extension (reading accessibility)
Data model: ReadingSettings(font_family, font_size, line_height, letter_spacing, ruler_color, ruler_enabled)
Features:   - Replace page fonts with a dyslexia-friendly font like OpenDyslexic
            - Adjust line height, letter spacing and word spacing with sliders
            - Show a colored reading ruler that follows the mouse
            - Tint the page background with a soft overlay color
            - Remember settings per website
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3, CSS injection
```

---

## Example 15

**Intent:**
Moodle plugin where teachers can give students badges for good forum posts

**Spec:**
```
Type:       Plugin (Moodle local plugin)
Data model: ForumBadge(id, name, image_url, course_id)
            Award(id, badge_id -> ForumBadge, user_id, post_id, awarded_by, awarded_at)
Features:   - Add an "Award badge" button under each forum post for teachers
            - Let teachers create badge types per course
            - Show awarded badges next to the student's name in the forum
            - Show a leaderboard block of badges in the course
            - Notify the student when they receive a badge
Storage:    Moodle database (via $DB API)
Tech stack: PHP, Moodle Plugin API, Mustache templates
```

---

## Example 16

**Intent:**
discord activity where people in a voice channel can draw together

**Spec:**
```
Type:       Plugin (Discord activity)
Data model: Canvas(id, channel_id, created_at)
            Stroke(id, canvas_id -> Canvas, user_id, color, width, points_json)
Features:   - Open a shared drawing canvas inside the voice channel
            - Sync strokes between participants in real time
            - Show each participant's cursor with their Discord avatar
            - Let users pick colors and brush size and undo their own strokes
            - Save the finished drawing as a PNG to the channel
API:        WebSocket
            /ws/canvas/{channel_id}
Storage:    Redis (live canvas state)
Tech stack: TypeScript, Discord Embedded App SDK, Colyseus, HTML Canvas
```

---

## Example 17

**Intent:**
json viewer for chrome that also lets me filter with jsonpath

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Detect raw JSON responses and render them as a collapsible tree
            - Highlight syntax and show array lengths
            - Filter the document with a JSONPath expression
            - Copy the path of any clicked node
            - Switch between tree view and raw view
Tech stack: TypeScript, Chrome Extension Manifest V3, jsonpath-plus
```

---

## Example 18

**Intent:**
Unity editor tool that finds all the assets that nothing uses anymore

**Spec:**
```
Type:       Plugin (Unity editor extension)
Features:   - Scan the project for assets not referenced by any scene or prefab
            - Build the reference graph from AssetDatabase dependencies
            - List unused assets grouped by type and size
            - Exclude folders like Resources and StreamingAssets
            - Move selected unused assets to an archive folder
Tech stack: C#, Unity Editor API (EditorWindow, AssetDatabase)
```

---

## Example 19

**Intent:**
godot plugin, dialogue editor with nodes

**Spec:**
```
Type:       Plugin (Godot editor plugin)
Data model: DialogueNode(id, speaker, text, position)
            Choice(id, node_id -> DialogueNode, text, next_node_id, condition)
Features:   - Add a dock with a GraphEdit-based dialogue editor
            - Create speaker lines and branching choices as connected nodes
            - Save dialogues as custom Resource files
            - Validate that every choice leads to an existing node
            - Provide a runtime DialogueRunner node that plays a dialogue
Storage:    Godot .tres resource files
Tech stack: GDScript, Godot 4 EditorPlugin API
```

---

## Example 20

**Intent:**
For my journalism work I often need proof of what a web page said at a certain time. I want to click a button and the page is saved to the Wayback Machine and I get the archive link and also a local screenshot with date.

**Spec:**
```
Type:       Browser extension (web archiving)
Data model: Capture(id, page_url, archive_url, screenshot_file, sha256, captured_at)
Features:   - Submit the current page to the Wayback Machine Save Page Now API
            - Take a full-page screenshot with the date and URL stamped on it
            - Save the screenshot with a SHA-256 hash for integrity
            - Keep a log of captures with their archive links
            - Export the capture log as CSV for a story file
API:        REST
            POST https://web.archive.org/save
Storage:    IndexedDB, local downloads folder
Tech stack: JavaScript, Chrome Extension Manifest V3, Internet Archive SPN2 API
```

---

## Example 21

**Intent:**
chrome extension for my kid that blocks youtube after 1 hour a day

**Spec:**
```
Type:       Browser extension (parental controls)
Data model: Limit(site_pattern, daily_minutes)
            UsageDay(date, site_pattern, minutes_used)
Features:   - Track active time on YouTube per day
            - Block the site with a friendly page when the limit is reached
            - Let the parent set limits per site behind a PIN
            - Reset counters at midnight
            - Show a weekly usage chart to the parent
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3 (alarms, declarativeNetRequest)
```

---

## Example 22

**Intent:**
logseq plugin to pull my kindle highlights

**Spec:**
```
Type:       Plugin (Logseq)
Data model: Book(title, author, page_name)
            Highlight(id, book_title -> Book, text, location, added_at)
Features:   - Import highlights from a Kindle "My Clippings.txt" file
            - Create one Logseq page per book
            - Add each highlight as a block with its location
            - Skip highlights that were already imported
            - Add a slash command to run the import
Input:      Kindle My Clippings.txt file
Storage:    Logseq graph (Markdown pages)
Tech stack: TypeScript, Logseq Plugin SDK (@logseq/libs)
```

---

## Example 23

**Intent:**
trello power-up that shows a burndown chart for the board

**Spec:**
```
Type:       Plugin (Trello Power-Up)
Data model: CardEstimate(card_id, points)
            Sprint(board_id, start_date, end_date)
Features:   - Add a story points field to each card
            - Let users set sprint start and end dates for the board
            - Calculate remaining points per day from card moves into Done
            - Show a burndown chart in a board button popup
            - Show the points total on list headers
API:        Trello REST
            GET  /1/boards/{id}/actions
Storage:    Trello pluginData (t.set / t.get)
Tech stack: JavaScript, Trello Power-Up client library, Chart.js
```

---

## Example 24

**Intent:**
zoom app that runs a quick poll with emojis during meetings

**Spec:**
```
Type:       Plugin (Zoom App)
Data model: Poll(id, meeting_id, question, options_json, created_by)
            Vote(id, poll_id -> Poll, participant_id, option)
Features:   - Let the host create a poll with emoji answer options
            - Show the poll to all participants in the Zoom Apps panel
            - Update results live as votes come in
            - Close the poll and show final results
            - Keep poll history per meeting
API:        REST
            POST /polls
            POST /polls/{id}/votes
            GET  /polls/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, Zoom Apps SDK, Node.js, Express, Socket.IO
```

---

## Example 25

**Intent:**
teams bot that does daily standups

**Spec:**
```
Type:       Bot (Microsoft Teams)
Data model: Team(id, channel_id, standup_time, timezone)
            Answer(id, team_id -> Team, user_id, yesterday, today, blockers, date)
Features:   - Message each team member privately at standup time
            - Ask yesterday, today and blockers questions with an Adaptive Card
            - Post a combined summary to the team channel
            - Highlight members who reported blockers
            - Skip weekends and configured holidays
Storage:    Azure Cosmos DB
Tech stack: C#, Bot Framework SDK, Adaptive Cards, Azure Functions
```

---

## Example 26

**Intent:**
canvas lms tool that shows students which assignments are due this week in a nice calendar

**Spec:**
```
Type:       Plugin (Canvas LTI 1.3 tool)
Features:   - Launch inside a Canvas course navigation tab
            - Fetch upcoming assignments through the Canvas REST API
            - Show assignments in a week calendar colored by course
            - Mark assignments already submitted
            - Export the week to an .ics calendar file
API:        Canvas REST
            GET  /api/v1/users/self/upcoming_events
            GET  /api/v1/courses/{id}/assignments
Tech stack: Python, Flask, PyLTI1p3, FullCalendar
```

---

## Example 27

**Intent:**
photoshop plugin to export all layers as separate pngs with the right names for my game

**Spec:**
```
Type:       Plugin (Photoshop UXP)
Features:   - List all visible layers and groups in the document
            - Export each layer as a trimmed PNG named after the layer
            - Export at 1x and 2x scale
            - Write a JSON file with each layer's position and size
            - Let users choose the output folder
Tech stack: JavaScript, Adobe UXP, Photoshop batchPlay API
```

---

## Example 28

**Intent:**
gimp script to add a watermark to a whole folder of images

**Spec:**
```
Type:       Plugin (GIMP Python plug-in)
Features:   - Register a menu entry under Filters > Batch
            - Open each image in a chosen folder
            - Place a text or logo watermark in a chosen corner with set opacity
            - Scale the watermark relative to image width
            - Save results to an output folder keeping the original format
Input:      Input folder, watermark text or image, corner, opacity
Tech stack: Python, GIMP 3 Python API (GObject Introspection)
```

---

## Example 29

**Intent:**
i sell on etsy and writing the tags is so boring. an extension that suggests tags when i make a listing pls

**Spec:**
```
Type:       Browser extension (seller listing helper)
Data model: TagSuggestion(keyword, source, score)
Features:   - Detect the Etsy listing editor page
            - Suggest tags from the listing title and description
            - Show character counts so tags stay under 20 characters
            - Insert chosen tags into the tag field with one click
            - Warn about duplicate or repeated words in tags
API:        Etsy Open API v3
            GET  /v3/application/listings/active?keywords={q}
Tech stack: JavaScript, Chrome Extension Manifest V3, Etsy Open API v3
```

---

## Example 30

**Intent:**
im learning spanish and want words i saved to get highlighted on every website i visit

**Spec:**
```
Type:       Browser extension (language learning)
Data model: Word(id, text, translation, status, added_at)
Features:   - Save a word from any page with a right-click menu item
            - Highlight saved words on every page with a color by status (new, learning, known)
            - Show the translation in a tooltip on hover
            - Change a word's status from the tooltip
            - Export words as a CSV for flashcard apps
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, MutationObserver
```

---

## Example 31

**Intent:**
github PR helper that adds a checklist comment

**Spec:**
```
Type:       Browser extension (developer tools)
Data model: ChecklistTemplate(id, repo_pattern, items_json)
Features:   - Detect GitHub pull request pages
            - Add a "Insert checklist" button near the comment box
            - Fill the checklist from a template matched to the repository
            - Show how many checklist items are still unchecked in the PR header
            - Edit templates in the options page
API:        GitHub REST
            POST /repos/{owner}/{repo}/issues/{number}/comments
Storage:    chrome.storage.sync
Tech stack: TypeScript, Chrome Extension Manifest V3, GitHub REST API
```

---

## Example 32

**Intent:**
confluence macro that shows our service status from statuspage

**Spec:**
```
Type:       Plugin (Confluence Cloud macro)
Features:   - Add a macro that users can insert into any page
            - Fetch current component status from the Statuspage API
            - Show each component with a colored status badge
            - Show active incidents with their latest update
            - Cache status for 60 seconds
API:        Statuspage REST
            GET  /api/v2/summary.json
Tech stack: Atlassian Forge, TypeScript, Forge UI Kit
```

---

## Example 33

**Intent:**
need a firefox addon that shows all the network calls a page makes so i can debug our API without opening devtools every time

**Spec:**
```
Type:       Browser extension (API request inspector)
Data model: RequestEntry(id, tab_id, method, url, status, duration_ms, request_body, response_body, time)
Features:   - Record requests from the active tab with the webRequest API
            - Show method, URL, status and timing in a sidebar list
            - Filter by domain, method or status code
            - Show request and response bodies for fetch and XHR calls
            - Copy any request as a cURL command
Tech stack: JavaScript, Firefox WebExtensions API (webRequest, sidebar_action)
```

---

## Example 34

**Intent:**
browser extension that pulls the paper info from arxiv and pubmed pages into a bibtex

**Spec:**
```
Type:       Browser extension (paper metadata)
Data model: Paper(id, source, external_id, title, authors, year, venue, abstract)
Features:   - Detect arXiv and PubMed article pages
            - Fetch metadata from the arXiv API or NCBI E-utilities
            - Generate a BibTeX entry with a clean citation key
            - Copy the BibTeX or download it as a .bib file
            - Keep a reading list of saved papers
API:        REST
            GET  http://export.arxiv.org/api/query?id_list={id}
            GET  https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={id}
Storage:    chrome.storage.local
Tech stack: TypeScript, Chrome Extension Manifest V3
```

---

## Example 35

**Intent:**
low vision helper - make everything on screen bigger and high contrast with one key

**Spec:**
```
Type:       Browser extension (low vision accessibility)
Data model: Profile(zoom_level, contrast_mode, cursor_size, enabled_sites)
Features:   - Toggle high-contrast mode with a keyboard shortcut
            - Zoom page text without breaking layout
            - Enlarge the mouse cursor and focus outline
            - Read the selected text aloud with speech synthesis
            - Save a profile per website
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3, Web Speech API
```

---

## Example 36

**Intent:**
alfred workflow to convert time zones quick

**Spec:**
```
Type:       Plugin (Alfred workflow)
Features:   - Parse input like "3pm london to tokyo"
            - Convert times between city time zones
            - Show results for a saved list of favourite cities
            - Copy the converted time with Enter
            - Handle daylight saving time correctly
Input:      Typed query in the Alfred bar
Tech stack: Python, Alfred Script Filter JSON, zoneinfo
```

---

## Example 37

**Intent:**
My partner works in a call center and uses Zendesk all day. She wants a little thing that shows the customer's local time and weather next to the ticket because she always forgets about time zones when she promises callbacks.

**Spec:**
```
Type:       Plugin (Zendesk app)
Features:   - Read the requester's city from the ticket's user fields
            - Show the customer's current local time in the ticket sidebar
            - Show current weather for that city
            - Warn when it is outside 8am-8pm for the customer
            - Suggest a callback time in the agent's own time zone
API:        REST
            GET  https://api.openweathermap.org/data/2.5/weather?q={city}
Tech stack: JavaScript, Zendesk Apps Framework (ZAF), OpenWeatherMap API
```

---

## Example 38

**Intent:**
Hi, I am teacher in Poland. I need plugin for Moodle that make quiz questions from text I paste. Please make it simple for use.

**Spec:**
```
Type:       Plugin (Moodle question bank tool)
Data model: GeneratedQuestion(id, course_id, question_text, answers_json, correct_index, status)
Features:   - Add a page where the teacher pastes a lesson text
            - Generate multiple-choice questions from the text with an LLM
            - Let the teacher edit or discard each question before saving
            - Import approved questions into the course question bank
            - Support Polish and English text
Storage:    Moodle database
Tech stack: PHP, Moodle Plugin API, OpenAI API
```

---

## Example 39

**Intent:**
home assistant card that shows which trash bin goes out tomorrow

**Spec:**
```
Type:       Plugin (Home Assistant Lovelace card)
Features:   - Read pickup dates from a calendar entity
            - Show the next pickup with a bin icon and color per waste type
            - Highlight the card when pickup is tomorrow
            - Show the next three pickups in a list
            - Configure waste types and colors in the card editor
Tech stack: TypeScript, Lit, Home Assistant custom card API
```

---

## Example 40

**Intent:**
blender add on to batch export every selected object as fbx for unity

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Add an export panel to the 3D viewport sidebar
            - Export each selected object to its own FBX file named after the object
            - Reset object location to the origin during export
            - Apply Unity axis settings (Y up, -Z forward) and scale
            - Remember the last export folder
Tech stack: Python, Blender bpy API
```

---

## Example 41

**Intent:**
unity tool for level designers to place prefabs along a curve

**Spec:**
```
Type:       Plugin (Unity editor extension)
Data model: PrefabPath(id, control_points, prefab, spacing, random_rotation)
Features:   - Draw an editable Bezier curve in the Scene view
            - Place a chosen prefab at even spacing along the curve
            - Randomize rotation and scale within set ranges
            - Snap placed objects to the ground with raycasts
            - Support undo for every placement change
Tech stack: C#, Unity Editor API (Handles, Undo, EditorTool)
```

---

## Example 42

**Intent:**
zotero thing that tells me when a paper in my library got retracted

**Spec:**
```
Type:       Plugin (Zotero)
Data model: RetractionCheck(item_id, doi, is_retracted, notice_url, checked_at)
Features:   - Check DOIs in the library against the Retraction Watch data in Crossref
            - Add a "Retracted" tag and colored marker to affected items
            - Show the retraction notice link in the item pane
            - Re-check the library weekly
            - Show a summary of newly found retractions
API:        Crossref REST
            GET  /works/{doi}
Storage:    Zotero database (item tags and notes)
Tech stack: JavaScript, Zotero 7 plugin API, Crossref API
```

---

## Example 43

**Intent:**
obsidian plugin to quiz me on my notes with spaced repetition

**Spec:**
```
Type:       Plugin (Obsidian)
Data model: Card(id, note_path, question, answer, ease, interval_days, due_date)
Features:   - Create cards from lines written as "question :: answer"
            - Schedule reviews with the SM-2 algorithm
            - Show due cards in a review modal
            - Rate answers as Again, Hard, Good or Easy
            - Show the number of due cards in the status bar
Storage:    Obsidian plugin data.json
Tech stack: TypeScript, Obsidian API
```

---

## Example 44

**Intent:**
discord bot for our dnd group to track initiative

**Spec:**
```
Type:       Bot (Discord)
Data model: Encounter(id, channel_id, round, active_index)
            Combatant(id, encounter_id -> Encounter, name, initiative, hp, is_player)
Features:   - Start an encounter with a slash command
            - Add players and monsters with their initiative rolls
            - Sort combatants and show whose turn it is
            - Advance turns and rounds with a button
            - Track hit points and remove defeated monsters
Storage:    SQLite
Tech stack: Python, discord.py
```

---

## Example 45

**Intent:**
OBS plugin that blurs my screen when a password field is on screen

**Spec:**
```
Type:       Plugin (OBS Studio filter)
Features:   - Add a "Privacy Blur" video filter for capture sources
            - Detect sensitive window titles from a configurable keyword list
            - Apply a Gaussian blur to the source while a match is active
            - Show an on-stream "content hidden" label
            - Add a hotkey to toggle the blur manually
Tech stack: C++, OBS Studio plugin API (libobs), HLSL effect shader
```

---

## Example 46

**Intent:**
grafana datasource for our internal metrics api

**Spec:**
```
Type:       Plugin (Grafana data source)
Features:   - Let users set the API URL and key in a config editor
            - Run queries against the metrics API with a query editor
            - Convert responses to Grafana data frames
            - Support template variables for host and service
            - Add a health check that tests the connection
API:        REST
            GET  /api/metrics/query?metric={name}&from={t}&to={t}
Tech stack: Go (backend), TypeScript, React, Grafana plugin SDK
```

---

## Example 47

**Intent:**
raycast command to start and stop my toggl timer

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Show the currently running timer in the menu bar
            - Start a timer with a description and project
            - Stop the running timer
            - List recent time entries to restart one
            - Show today's total tracked time
API:        Toggl Track REST
            GET  /api/v9/me/time_entries/current
            POST /api/v9/workspaces/{id}/time_entries
            PATCH /api/v9/workspaces/{id}/time_entries/{id}/stop
Tech stack: TypeScript, React, Raycast API
```

---

## Example 48

**Intent:**
something in gmail? no wait - in outlook - that reminds me if i forgot an attachment

**Spec:**
```
Type:       Plugin (Outlook add-in)
Features:   - Check the message body for words like "attached" or "attachment" on send
            - Block sending and show a warning when no attachment is present
            - Support custom trigger words in several languages
            - Let the user send anyway with one click
            - Work in Outlook desktop and Outlook on the web
Tech stack: JavaScript, Office.js, Outlook Smart Alerts (OnMessageSend event)
```

---

## Example 49

**Intent:**
a chrome extension that turns amazon prices into how many hours i'd need to work to buy it lol

**Spec:**
```
Type:       Browser extension (shopping awareness)
Data model: Settings(hourly_wage, currency)
Features:   - Ask for the user's hourly wage on first run
            - Find prices on Amazon product and search pages
            - Show the price as hours and minutes of work next to each price
            - Update prices that load dynamically
            - Toggle the overlay on and off from the toolbar
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 50

**Intent:**
anki plugin that adds pronunciation audio to my vocab cards automatically

**Spec:**
```
Type:       Plugin (Anki add-on)
Features:   - Add an "Add audio" action to the card browser
            - Generate speech for the word field with a text-to-speech service
            - Save audio files into the Anki media folder
            - Insert the [sound:] tag into the audio field
            - Skip notes that already have audio
Tech stack: Python, Anki add-on API, gTTS
```

---

## Example 51

**Intent:**
godot plugin that lets me paint tiles with random variations

**Spec:**
```
Type:       Plugin (Godot editor plugin)
Features:   - Add a brush mode to the TileMap editor
            - Pick a random tile from a weighted variation set on each stroke
            - Configure variation sets in an inspector resource
            - Support undo and redo for painted areas
            - Fill a rectangle with random variations
Tech stack: GDScript, Godot 4 EditorPlugin API
```

---

## Example 52

**Intent:**
logseq plugin that makes a weekly review page from my journals

**Spec:**
```
Type:       Plugin (Logseq)
Features:   - Collect TODO, DONE and tagged blocks from the last seven journal pages
            - Create a "Week NN review" page with sections per category
            - Embed block references instead of copying text
            - Count completed tasks for the week
            - Run from a slash command or a toolbar button
Storage:    Logseq graph
Tech stack: JavaScript, Logseq Plugin SDK
```

---

## Example 53

**Intent:**
I run a small property management business and when I look at listings on Rightmove I copy everything into my spreadsheet by hand which takes forever. Could a browser button just copy the address, price, bedrooms and agent into Google Sheets?

**Spec:**
```
Type:       Browser extension (property listing capture)
Data model: CapturedListing(url, address, price, bedrooms, property_type, agent_name, captured_at)
Features:   - Read address, price, bedrooms and agent from the listing page
            - Show captured fields for a quick check before saving
            - Append the listing as a new row in a chosen Google Sheet
            - Warn when the listing URL is already in the sheet
            - Let the user pick the target spreadsheet in options
API:        Google Sheets REST
            POST /v4/spreadsheets/{id}/values/{range}:append
Tech stack: JavaScript, Chrome Extension Manifest V3, chrome.identity, Google Sheets API
```

---

## Example 54

**Intent:**
Teams message extension to search our product docs and paste a link

**Spec:**
```
Type:       Plugin (Microsoft Teams message extension)
Features:   - Add a search command in the Teams compose box
            - Search product documentation by keyword
            - Show results as cards with title and summary
            - Insert a link card into the chat when a result is picked
            - Unfurl doc links pasted into messages
API:        REST
            GET  /api/docs/search?q={query}
Tech stack: TypeScript, Teams Toolkit, Bot Framework SDK, Azure AI Search
```

---

## Example 55

**Intent:**
My daughter is 9 and she is starting to use the family laptop for homework. I don't want to spy on her, but I'd like to know which sites she spends most time on each week and get a short email summary on Sunday.

**Spec:**
```
Type:       Browser extension (family activity summary)
Data model: Child(id, name, parent_id)
            DomainVisit(id, child_id -> Child, domain, seconds, date)
Features:   - Track active time per domain without recording full URLs
            - Upload daily totals to the parent's account
            - Send a weekly summary email every Sunday with the top 10 sites
            - Let the parent add sites to a "homework" category
            - Show the child a visible icon so tracking is transparent
API:        REST
            POST /visits/batch
            GET  /children/{id}/weekly
Storage:    PostgreSQL
Tech stack: JavaScript (Chrome Extension Manifest V3), Node.js, Express, SendGrid
```

---

## Example 56

**Intent:**
firefox addon to see a reddit user's account age and karma on hover

**Spec:**
```
Type:       Browser extension (Reddit user info)
Features:   - Detect username links on Reddit pages
            - Fetch account age and karma from the user's about.json on hover
            - Show a small tooltip card with the info
            - Flag accounts younger than 30 days
            - Cache user info for one hour
API:        Reddit JSON
            GET  /user/{name}/about.json
Tech stack: JavaScript, Firefox WebExtensions API
```

---

## Example 57

**Intent:**
chrome extention for ebay sellers to calculate profit after fees and shipping befor i list somthing

**Spec:**
```
Type:       Browser extension (seller profit calculator)
Data model: FeeProfile(category, final_value_fee_pct, fixed_fee, payment_fee_pct)
            Calculation(item_title, sale_price, cost, shipping_cost, profit)
Features:   - Show a profit panel on the eBay listing form
            - Read the price and category from the form
            - Calculate eBay fees, shipping and net profit
            - Show the profit margin in percent with a color warning when low
            - Save fee profiles per category
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 58

**Intent:**
an extension that saves the slides and transcript from coursera videos for revision

**Spec:**
```
Type:       Browser extension (course revision notes)
Data model: Lecture(id, course_name, title, url)
            TranscriptLine(id, lecture_id -> Lecture, start_seconds, text)
            Bookmark(id, lecture_id -> Lecture, start_seconds, note)
Features:   - Capture the transcript of the current lecture with timestamps
            - Let the student bookmark moments with a short note
            - Combine bookmarks and transcript into a revision page
            - Export a lecture's revision page as PDF
            - Search across saved transcripts
Storage:    IndexedDB
Tech stack: TypeScript, Chrome Extension Manifest V3, jsPDF
```

---

## Example 59

**Intent:**
jira thing that auto assigns bugs to whoever is on call

**Spec:**
```
Type:       Plugin (Jira Cloud automation app)
Data model: OnCallSchedule(id, project_key, user_account_id, start_at, end_at)
Features:   - Listen for new issues of type Bug
            - Look up the on-call person from the schedule
            - Assign the issue and add an "on-call" label
            - Post a comment explaining the auto assignment
            - Let admins edit the schedule in a project settings page
API:        Jira REST
            PUT  /rest/api/3/issue/{issueKey}/assignee
Storage:    Forge storage API
Tech stack: Atlassian Forge, JavaScript, Forge triggers (avi:jira:created:issue)
```

---

## Example 60

**Intent:**
vs code is covered, but I want a JetBrains plugin that shows TODO comments with git blame author

**Spec:**
```
Type:       Plugin (IntelliJ Platform)
Features:   - Find TODO and FIXME comments in the project
            - Show the git blame author and date for each TODO
            - Add a tool window listing TODOs grouped by author
            - Filter TODOs older than a chosen number of days
            - Jump to the source line on double-click
Tech stack: Kotlin, IntelliJ Platform SDK, Git4Idea
```

---

## Example 61

**Intent:**
plugin for blender that makes the render send a message to my phone when it's done

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Hook into the render_complete and render_cancel handlers
            - Send a push notification with render time and frame count
            - Attach a small preview image of the final frame
            - Let the user enter an ntfy topic in add-on preferences
            - Notify also when an animation render fails
API:        REST
            POST https://ntfy.sh/{topic}
Tech stack: Python, Blender bpy API, ntfy.sh
```

---

## Example 62

**Intent:**
obsidian plugin for my writing: count words per chapter and show progress to my goal

**Spec:**
```
Type:       Plugin (Obsidian)
Data model: Project(folder_path, word_goal, deadline)
            DailyCount(date, words_written)
Features:   - Count words in every note of a project folder
            - Show words per chapter in a side panel
            - Show progress toward the word goal and words needed per day until the deadline
            - Record words written each day
            - Exclude frontmatter and comments from counts
Storage:    Obsidian plugin data.json
Tech stack: TypeScript, Obsidian API
```

---

## Example 63

**Intent:**
we use Confluence for meeting notes and nobody follows up on action items. I want a plugin that finds all the task checkboxes on meeting pages and makes a report of open ones by person.

**Spec:**
```
Type:       Plugin (Confluence Cloud app)
Data model: ActionItem(id, page_id, text, assignee_account_id, due_date, completed)
Features:   - Find tasks on pages with the "meeting-notes" label
            - Group open tasks by assignee
            - Show overdue tasks in red
            - Send a weekly digest to each assignee
            - Add a report page under the space's apps menu
API:        Confluence REST
            GET  /wiki/api/v2/tasks?status=incomplete
Storage:    Forge storage API
Tech stack: Atlassian Forge, TypeScript, React (Custom UI)
```

---

## Example 64

**Intent:**
chrome thing that lets me compare two json responses side by side

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Open a compare page from the toolbar
            - Paste or load two JSON documents
            - Show a structural diff with added, removed and changed keys highlighted
            - Ignore key order and optional fields
            - Copy a diff report as text
Tech stack: TypeScript, Chrome Extension Manifest V3, jsondiffpatch
```

---

## Example 65

**Intent:**
home assistant integration for my electric car charger's local api

**Spec:**
```
Type:       Plugin (Home Assistant custom integration)
Data model: Charger(id, host, serial)
            ChargeSession(charger_id -> Charger, energy_kwh, started_at, ended_at)
Features:   - Set up the charger by IP address through a config flow
            - Create sensors for power, session energy and charger state
            - Add a switch to start and stop charging
            - Add a number entity to set the max current
            - Expose a service to charge only during cheap tariff hours
Storage:    Home Assistant recorder
Tech stack: Python, Home Assistant integration framework, aiohttp
```

---

## Example 66

**Intent:**
grafana panel plugin like a speedometer but for multiple values

**Spec:**
```
Type:       Plugin (Grafana panel)
Features:   - Draw several radial gauges in one panel from multiple series
            - Set min, max and threshold colors per gauge
            - Show the value and unit in the gauge center
            - Arrange gauges in a responsive grid
            - Animate needle changes on refresh
Tech stack: TypeScript, React, Grafana plugin SDK, D3.js
```

---

## Example 67

**Intent:**
i want a zotero plugin which puts a reading status like to read, reading, done on each paper

**Spec:**
```
Type:       Plugin (Zotero)
Data model: ReadingStatus(item_id, status, changed_at)
Features:   - Add a "Reading status" column to the items list
            - Set status from the right-click menu or a keyboard shortcut
            - Color-code items by status
            - Filter the library by status
            - Record when an item was marked done
Storage:    Zotero database (extra field)
Tech stack: JavaScript, Zotero 7 plugin API
```

---

## Example 68

**Intent:**
canvas lms plugin for peer review where students rate each others group work

**Spec:**
```
Type:       Plugin (Canvas LTI 1.3 tool)
Data model: Group(id, course_id, name)
            PeerRating(id, group_id -> Group, rater_user_id, ratee_user_id, score, comment)
Features:   - Load group membership from Canvas
            - Let each student rate teammates on set criteria
            - Hide raters' names from the students being rated
            - Show the teacher an averaged score table per student
            - Send final scores to the Canvas gradebook via AGS
API:        LTI Advantage
            POST /lti/launch
            POST /api/ratings
            GET  /api/groups/{id}/summary
Storage:    PostgreSQL
Tech stack: Python, Django, PyLTI1p3
```

---

## Example 69

**Intent:**
anki addon that pauses my review if I've been going for 30 minutes

**Spec:**
```
Type:       Plugin (Anki add-on)
Features:   - Start a timer when a review session begins
            - Show a break reminder after a configurable number of minutes
            - Lock the review screen during a 5-minute break
            - Show cards reviewed and time spent before the break
            - Let the user skip a break with a confirmation
Tech stack: Python, Anki add-on API (aqt hooks), PyQt6
```

---

## Example 70

**Intent:**
Hi! In my company we use Jira and Microsoft Teams. Please make app so when issue is moved to Done, Teams channel gets nice message with who did it.

**Spec:**
```
Type:       Webhook service (Jira to Teams)
Data model: Mapping(id, jira_project_key, teams_webhook_url)
Features:   - Receive Jira issue-updated webhooks
            - Detect transitions to the Done status
            - Post an Adaptive Card to the mapped Teams channel with issue key, title and assignee
            - Let admins map projects to channels
            - Retry failed posts up to three times
API:        REST
            POST /webhooks/jira
            GET  /mappings
            POST /mappings
Storage:    SQLite
Tech stack: Python, FastAPI, Adaptive Cards
```

---

## Example 71

**Intent:**
Unity editor window that shows all the scenes in the build and lets me open them fast

**Spec:**
```
Type:       Plugin (Unity editor extension)
Features:   - List all scenes from Build Settings in a dockable window
            - Open a scene with one click (with save prompt)
            - Search scenes by name
            - Mark favourite scenes at the top
            - Show scenes not in the build in a separate section
Tech stack: C#, Unity Editor API (EditorWindow, EditorSceneManager)
```

---

## Example 72

**Intent:**
an extension for students that blocks distracting sites only during the hours I set for studying

**Spec:**
```
Type:       Browser extension (study focus)
Data model: Schedule(day_of_week, start_time, end_time)
            BlockedSite(pattern)
Features:   - Block listed sites during scheduled study blocks
            - Show a motivational page with time remaining when blocked
            - Allow a 5-minute emergency unlock once per block
            - Show a weekly report of blocked attempts
            - Sync settings across browsers
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3 (declarativeNetRequest, alarms)
```

---

## Example 73

**Intent:**
opening github actions logs is a pain. extension that collapses noise and jumps to the first error

**Spec:**
```
Type:       Browser extension (developer tools)
Features:   - Detect GitHub Actions job log pages
            - Find the first line matching error patterns and scroll to it
            - Highlight error and warning lines
            - Collapse long dependency install sections
            - Add a button to copy the failing step's log
Tech stack: TypeScript, Chrome Extension Manifest V3
```

---

## Example 74

**Intent:**
obs plugin that shows my heart rate from a bluetooth chest strap

**Spec:**
```
Type:       Plugin (OBS Studio)
Features:   - Connect to a Bluetooth LE heart rate monitor
            - Read the standard Heart Rate Measurement characteristic
            - Add a text source that shows the current BPM
            - Change color when the BPM passes set zones
            - Log heart rate over the stream to a CSV file
Tech stack: C++, OBS Studio plugin API, SimpleBLE
```

---

## Example 75

**Intent:**
logseq plugin which turns a block list into a mind map

**Spec:**
```
Type:       Plugin (Logseq)
Features:   - Add a context menu item "Show as mind map" to blocks
            - Build a tree from the block and its children
            - Render the tree as an interactive mind map
            - Expand and collapse branches
            - Export the mind map as SVG
Tech stack: TypeScript, Logseq Plugin SDK, markmap
```

---

## Example 76

**Intent:**
im a tutor and use zoom. want an app inside zoom that shows a shared whiteboard with math formulas

**Spec:**
```
Type:       Plugin (Zoom App)
Data model: Board(id, meeting_id, created_at)
            Element(id, board_id -> Board, kind, latex, x, y, author_id)
Features:   - Open a shared whiteboard for all meeting participants
            - Type formulas in LaTeX and render them with KaTeX
            - Draw freehand and move elements
            - Sync changes in real time
            - Save the board as a PDF after the meeting
API:        WebSocket
            /ws/boards/{id}
Storage:    PostgreSQL, Redis
Tech stack: TypeScript, Zoom Apps SDK, React, Yjs, KaTeX
```

---

## Example 77

**Intent:**
discord bot that posts free game deals in a channel

**Spec:**
```
Type:       Bot (Discord)
Data model: Guild(id, channel_id, platforms)
            PostedDeal(id, deal_id, guild_id -> Guild, posted_at)
Features:   - Check deal sources every hour for free games
            - Post an embed with title, store, image and end date
            - Let admins choose stores (Steam, Epic, GOG) with a slash command
            - Avoid posting the same deal twice
            - Ping an optional role on new deals
Storage:    SQLite
Tech stack: Node.js, discord.js, node-cron
```

---

## Example 78

**Intent:**
Teams tab app for booking the office parking spots

**Spec:**
```
Type:       Plugin (Microsoft Teams tab)
Data model: ParkingSpot(id, label, is_ev)
            Booking(id, spot_id -> ParkingSpot, user_id, date)
Features:   - Show today's and tomorrow's free spots in a grid
            - Book a spot for a date with one click
            - Cancel a booking
            - Limit each user to one booking per day
            - Let admins add or disable spots
API:        REST
            GET  /spots?date={date}
            POST /bookings
            DELETE /bookings/{id}
Storage:    Azure SQL Database
Tech stack: TypeScript, Teams Toolkit, React, Fluent UI, Azure Functions
```

---

## Example 79

**Intent:**
gimp plugin to make sprite sheets from layers

**Spec:**
```
Type:       Plugin (GIMP Python plug-in)
Features:   - Arrange every layer of the image into a grid sheet
            - Let the user choose columns, padding and frame size
            - Export the sheet as PNG
            - Write a JSON file with frame coordinates
            - Keep layer order as animation order
Tech stack: Python, GIMP 3 Python API
```

---

## Example 80

**Intent:**
photoshop plugin that checks if my print design has bleed and the right dpi

**Spec:**
```
Type:       Plugin (Photoshop UXP)
Features:   - Read document size, resolution and color mode
            - Warn when resolution is below 300 dpi
            - Check that the canvas includes a chosen bleed margin
            - Warn when the color mode is not CMYK
            - Show a pass/fail checklist in a panel
Tech stack: JavaScript, Adobe UXP, Photoshop DOM API
```

---

## Example 81

**Intent:**
browser extension for language learners that shows netflix subtitles in two languages at once

**Spec:**
```
Type:       Browser extension (dual subtitles)
Data model: Settings(primary_language, secondary_language, font_size)
Features:   - Read subtitle tracks from the streaming player
            - Show a second subtitle line in the chosen language
            - Translate the line when a second track is missing
            - Pause and show word definitions when a word is clicked
            - Save clicked words to a vocabulary list
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, DeepL API
```

---

## Example 82

**Intent:**
raycast extension to look up a npm package and see weekly downloads

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Search npm packages as the user types
            - Show version, description and weekly downloads
            - Show bundle size from Bundlephobia
            - Copy the install command for npm, yarn or pnpm
            - Open the package on npmjs.com or its repository
API:        REST
            GET  https://registry.npmjs.org/-/v1/search?text={q}
            GET  https://api.npmjs.org/downloads/point/last-week/{pkg}
Tech stack: TypeScript, React, Raycast API
```

---

## Example 83

**Intent:**
godot editor plugin to check all my scenes for missing scripts or broken references

**Spec:**
```
Type:       Plugin (Godot editor plugin)
Features:   - Scan all .tscn files in the project
            - Report nodes with missing scripts or resources
            - Report broken signal connections
            - Show results in a bottom panel with clickable paths
            - Run the check automatically before export
Tech stack: GDScript, Godot 4 EditorPlugin API, EditorExportPlugin
```

---

## Example 84

**Intent:**
chrome extension for real estate agents that shows the school ratings and commute time for any address on the page

**Spec:**
```
Type:       Browser extension (real estate)
Data model: AddressInfo(address, lat, lng, school_ratings_json, commute_minutes, fetched_at)
Features:   - Detect street addresses on the page and underline them
            - Geocode the address on hover
            - Show nearby school ratings in a popover
            - Calculate commute time to a saved work address
            - Cache results per address
API:        REST
            GET  https://maps.googleapis.com/maps/api/geocode/json
            GET  https://maps.googleapis.com/maps/api/distancematrix/json
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, Google Maps Platform APIs
```

---

## Example 85

**Intent:**
plugin for my shopify? no its woocommerce... no wait, its for prestashop: show low stock in the dashboard

**Spec:**
```
Type:       Plugin (PrestaShop module)
Data model: StockAlert(product_id, threshold, last_alerted_at)
Features:   - Add a dashboard widget listing products below their stock threshold
            - Let the shop owner set a threshold per product
            - Email the owner a daily low-stock list
            - Link each product to its edit page
            - Sort by days of stock left based on recent sales
Storage:    MySQL (PrestaShop database)
Tech stack: PHP, PrestaShop module API, Smarty
```

---

## Example 86

**Intent:**
i read a lot of research and i want an extension that shows if a paper is open access and gives me the free pdf link

**Spec:**
```
Type:       Browser extension (open access finder)
Features:   - Find the DOI on journal article pages
            - Query the Unpaywall API for an open access version
            - Show a green tab with a link to the free PDF when found
            - Show the open access type (gold, green, hybrid)
            - Keep a history of papers checked
API:        REST
            GET  https://api.unpaywall.org/v2/{doi}?email={email}
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, Unpaywall API
```

---

## Example 87

**Intent:**
Trello power up for recipe boards, show cooking time and ingredients on the card front

**Spec:**
```
Type:       Plugin (Trello Power-Up)
Data model: RecipeInfo(card_id, prep_minutes, cook_minutes, servings, ingredients_json)
Features:   - Add a form to cards for prep time, cook time and servings
            - Show total time as a card badge
            - Show an ingredient list in the card back section
            - Combine ingredients from chosen cards into a shopping list
            - Scale ingredient amounts by servings
Storage:    Trello pluginData
Tech stack: JavaScript, Trello Power-Up client library
```

---

## Example 88

**Intent:**
Discord activity where my friends can play a trivia quiz together in the voice channel, questions about movies

**Spec:**
```
Type:       Plugin (Discord activity)
Data model: Game(id, channel_id, state, round)
            Question(id, category, text, options_json, answer_index)
            Score(game_id -> Game, user_id, points)
Features:   - Start a game for everyone in the voice channel
            - Show the same question to all players with a 15-second timer
            - Give more points for faster correct answers
            - Show a scoreboard between rounds
            - Let the host choose the number of rounds
API:        WebSocket
            /ws/game/{channel_id}
Storage:    PostgreSQL (questions), in-memory game state
Tech stack: TypeScript, Discord Embedded App SDK, Node.js, Socket.IO, React
```

---

## Example 89

**Intent:**
home assistant automation blueprint plus card to show if the washing machine is done using a smart plug

**Spec:**
```
Type:       Plugin (Home Assistant blueprint and Lovelace card)
Features:   - Detect a wash cycle from the smart plug's power readings
            - Mark the cycle finished when power stays low for 3 minutes
            - Send a mobile notification when the wash is done
            - Show cycle state and elapsed time on a dashboard card
            - Remind again if the door is not opened after 30 minutes
Tech stack: YAML (Home Assistant blueprint), TypeScript, Lit
```

---

## Example 90

**Intent:**
chrome extension that lets me annotate PDFs in the browser for my thesis and export the highlights

**Spec:**
```
Type:       Browser extension (PDF annotation)
Data model: Document(id, url, title, hash)
            Annotation(id, document_id -> Document, page, rects_json, color, text, comment)
Features:   - Open PDFs in a custom viewer
            - Highlight text in several colors with comments
            - Save annotations per document
            - Export highlights and comments as Markdown with page numbers
            - Search across all annotations
Storage:    IndexedDB
Tech stack: TypeScript, Chrome Extension Manifest V3, PDF.js
```

---

## Example 91

**Intent:**
alfred workflow to search my bookmarks from firefox

**Spec:**
```
Type:       Plugin (Alfred workflow)
Features:   - Read bookmarks from the Firefox places.sqlite database
            - Match bookmarks by title and URL with fuzzy search
            - Show favicons and folder path in results
            - Open the selected bookmark in Firefox
            - Refresh the cached index every hour
Input:      Typed query in the Alfred bar
Storage:    Local cache file
Tech stack: Python, sqlite3, Alfred Script Filter JSON
```

---

## Example 92

**Intent:**
plugin for jira that warns when a sprint has more story points than the team velocity

**Spec:**
```
Type:       Plugin (Jira Cloud)
Data model: VelocityRecord(board_id, sprint_id, completed_points)
Features:   - Calculate average velocity from the last three closed sprints
            - Show planned points against velocity on the backlog
            - Show a warning banner when planned points exceed velocity by 10%
            - Let team leads override the velocity
            - Show a trend chart of velocity
API:        Jira Agile REST
            GET  /rest/agile/1.0/board/{boardId}/sprint
            GET  /rest/agile/1.0/sprint/{sprintId}/issue
Storage:    Forge storage API
Tech stack: Atlassian Forge, TypeScript, React
```

---

## Example 93

**Intent:**
browser addon that reads the article to me with a nice voice and highlights the words

**Spec:**
```
Type:       Browser extension (read aloud)
Data model: Settings(voice_name, rate, pitch, highlight_color)
Features:   - Extract the main article text with a readability parser
            - Read it aloud with the Web Speech API
            - Highlight each word as it is spoken
            - Let the user pause, skip paragraphs and change speed
            - Start reading from a clicked paragraph
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3, Mozilla Readability, Web Speech API
```

---

## Example 94

**Intent:**
unity tool that bakes my level into a minimap png

**Spec:**
```
Type:       Plugin (Unity editor extension)
Features:   - Place a top-down orthographic camera over the level bounds
            - Render selected layers to a RenderTexture at a set resolution
            - Save the result as a PNG in the project
            - Write the world bounds into a ScriptableObject for runtime mapping
            - Rebake with one button after level changes
Tech stack: C#, Unity Editor API
```

---

## Example 95

**Intent:**
i am researcher in biology, I want Zotero plugin that gets citation count for each paper and show it in column

**Spec:**
```
Type:       Plugin (Zotero)
Data model: CitationCount(item_id, doi, count, source, updated_at)
Features:   - Look up citation counts by DOI from OpenAlex
            - Add a sortable "Citations" column to the items list
            - Update counts for selected items or the whole library
            - Refresh counts automatically once a month
            - Show the last update date in the item pane
API:        REST
            GET  https://api.openalex.org/works/doi:{doi}
Storage:    Zotero database (extra field)
Tech stack: JavaScript, Zotero 7 plugin API, OpenAlex API
```

---

## Example 96

**Intent:**
obsidian plugin that shows my upcoming google calendar events in the sidebar

**Spec:**
```
Type:       Plugin (Obsidian)
Features:   - Show today's and tomorrow's events in a side panel
            - Create a meeting note from an event with a template
            - Link the note back into the event list
            - Refresh events every 10 minutes
            - Let users choose which calendars to show
API:        Google Calendar REST
            GET  /calendar/v3/calendars/{id}/events
Tech stack: TypeScript, Obsidian API, Google Calendar API
```

---

## Example 97

**Intent:**
a chrome extension to help people with ADHD read: bold the first half of every word

**Spec:**
```
Type:       Browser extension (reading aid)
Data model: Settings(enabled, bold_ratio, excluded_sites)
Features:   - Bold the first part of each word in page text
            - Adjust how much of each word is bolded
            - Skip code blocks, inputs and editable areas
            - Turn on or off per site from the popup
            - Process new content as the page updates
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3, TreeWalker API
```

---

## Example 98

**Intent:**
OBS script to automatically switch scenes when I'm not talking for a while

**Spec:**
```
Type:       Plugin (OBS Studio script)
Features:   - Monitor the microphone audio level
            - Switch to a "BRB" scene after a set number of silent seconds
            - Switch back when speech resumes
            - Ignore short pauses under a threshold
            - Configure the scenes and timings in the script settings
Tech stack: Python, OBS Studio scripting API (obspython)
```

---

## Example 99

**Intent:**
foundry vtt module that rolls random loot from tables when a monster dies

**Spec:**
```
Type:       Plugin (Foundry VTT module)
Data model: LootTable(id, name, creature_type, cr_min, cr_max)
            LootEntry(id, table_id -> LootTable, item_uuid, weight, quantity_formula)
Features:   - Detect when an NPC token drops to 0 HP
            - Pick a loot table by creature type and challenge rating
            - Roll items with weights and dice quantity formulas
            - Add the loot to the token's inventory as a lootable container
            - Post a chat card listing the loot for the GM
Storage:    Foundry world database (flags and compendiums)
Tech stack: JavaScript, Foundry VTT API (Hooks, RollTable)
```

---

## Example 100

**Intent:**
roblox studio plugin to align and evenly space selected parts

**Spec:**
```
Type:       Plugin (Roblox Studio)
Features:   - Add a toolbar button that opens an alignment widget
            - Align selected parts on X, Y or Z by min, center or max
            - Distribute parts with equal spacing
            - Support undo through ChangeHistoryService
            - Remember the last used options
Tech stack: Luau, Roblox Studio plugin API
```

---

## Example 101

**Intent:**
minecraft server plugin, players can claim land with a golden shovel

**Spec:**
```
Type:       Plugin (Minecraft Paper server)
Data model: Claim(id, owner_uuid, world, min_x, min_z, max_x, max_z, created_at)
            Trust(claim_id -> Claim, player_uuid, level)
Features:   - Create a claim by right-clicking two corners with a golden shovel
            - Block other players from breaking or placing blocks in a claim
            - Let owners trust players with /trust and /untrust
            - Give claim blocks to players based on play time
            - Show claim borders with particles
Storage:    SQLite
Tech stack: Java, Paper API, Gradle
```

---

## Example 102

**Intent:**
stream deck plugin to mute zoom and show if im muted on the button

**Spec:**
```
Type:       Plugin (Elgato Stream Deck)
Features:   - Toggle mute in the Zoom desktop app
            - Show a red or green button image for the current mute state
            - Toggle video with a second action
            - Detect when Zoom is not running and grey out the buttons
            - Poll state every second
Tech stack: TypeScript, Stream Deck SDK (Node.js)
```

---

## Example 103

**Intent:**
i do 3d printing and use cura. want a plugin that adds a pause at a height so i can change filament color

**Spec:**
```
Type:       Plugin (Ultimaker Cura post-processing script)
Features:   - Let the user choose one or more layer heights
            - Insert a pause G-code (M600 or M0) at the chosen layers
            - Park the print head and retract filament before the pause
            - Show a message on the printer display
            - Resume at the right temperature and position
Input:      Sliced G-code and the chosen layer heights
Tech stack: Python, Cura post-processing script API
```

---

## Example 104

**Intent:**
QGIS plugin to download OpenStreetMap buildings for the current map view

**Spec:**
```
Type:       Plugin (QGIS)
Features:   - Add a toolbar button that uses the current map extent
            - Query the Overpass API for building footprints
            - Load results as a polygon layer with OSM tags as attributes
            - Warn when the area is too large
            - Save the layer as GeoPackage
API:        Overpass
            POST https://overpass-api.de/api/interpreter
Tech stack: Python, PyQGIS, Qt (PyQt5)
```

---

## Example 105

**Intent:**
kicad plugin that exports my bill of materials with prices from digikey

**Spec:**
```
Type:       Plugin (KiCad action plugin)
Data model: BomLine(reference_designators, value, footprint, mpn, quantity, unit_price, stock)
Features:   - Read components and part numbers from the PCB
            - Group identical parts into BOM lines
            - Look up price and stock for each part number
            - Calculate total cost for a chosen board quantity
            - Export the BOM as CSV and XLSX
API:        DigiKey REST
            POST /products/v4/search/keyword
Tech stack: Python, KiCad pcbnew API, openpyxl
```

---

## Example 106

**Intent:**
thunderbird add on that sorts newsletters into a folder automatically

**Spec:**
```
Type:       Plugin (Thunderbird add-on)
Data model: Rule(sender_pattern, target_folder)
Features:   - Detect newsletters by List-Unsubscribe headers
            - Move them into a "Newsletters" folder
            - Let users add or remove senders from a rule list
            - Show a weekly digest of unread newsletters
            - Add a one-click unsubscribe button in the message view
Storage:    browser.storage.local
Tech stack: JavaScript, Thunderbird MailExtensions API
```

---

## Example 107

**Intent:**
calibre plugin that fetches the goodreads rating for my books

**Spec:**
```
Type:       Plugin (Calibre)
Data model: BookRating(book_id, rating, ratings_count, fetched_at)
Features:   - Add a toolbar action to fetch ratings for selected books
            - Search by ISBN, then by title and author
            - Save the rating into a custom column
            - Skip books updated in the last 30 days
            - Show a progress dialog during fetches
Storage:    Calibre library database (custom column)
Tech stack: Python, Calibre plugin API, Qt
```

---

## Example 108

**Intent:**
jellyfin plugin that skips the intro of tv shows

**Spec:**
```
Type:       Plugin (Jellyfin server)
Data model: IntroSegment(episode_id, start_seconds, end_seconds, confidence)
Features:   - Compare audio fingerprints across episodes of a season
            - Detect the shared intro segment
            - Store intro start and end per episode
            - Show a "Skip intro" button in supported clients
            - Run detection as a scheduled task for new episodes
Storage:    Jellyfin plugin database (SQLite)
Tech stack: C#, .NET, Jellyfin plugin API, Chromaprint
```

---

## Example 109

**Intent:**
neovim plugin that shows the current git branch and changed files in a float

**Spec:**
```
Type:       Plugin (Neovim)
Features:   - Open a floating window with a keymap
            - Show the current branch and ahead/behind counts
            - List changed files with status letters
            - Open a file by pressing Enter on it
            - Stage or unstage a file with a key
Tech stack: Lua, Neovim API, git CLI
```

---

## Example 110

**Intent:**
zsh plugin that reminds me of the alias when I type the full command

**Spec:**
```
Type:       Plugin (Zsh)
Features:   - Hook into preexec to inspect each command
            - Find aliases whose expansion matches the typed command
            - Print a short reminder with the alias name
            - Ignore commands listed in an exclude variable
            - Optionally block the command until the alias is used
Tech stack: Zsh, oh-my-zsh plugin format
```

---

## Example 111

**Intent:**
jupyter extension that shows how long each cell took and when it ran

**Spec:**
```
Type:       Plugin (JupyterLab extension)
Features:   - Record start and end time of each cell execution
            - Show duration and finish time under each cell
            - Save timings in cell metadata
            - Highlight cells that took longer than a threshold
            - Add a summary table of slowest cells
Tech stack: TypeScript, JupyterLab extension API
```

---

## Example 112

**Intent:**
pytest plugin that retries flaky tests and reports them separately

**Spec:**
```
Type:       Plugin (pytest)
Features:   - Add a --retries command-line option
            - Rerun failed tests up to the set number of times
            - Mark tests that passed after a retry as flaky
            - Print a flaky tests section in the terminal summary
            - Write flaky tests to a JSON report
Tech stack: Python, pytest hook API
```

---

## Example 113

**Intent:**
eslint plugin for our team: no console.log in production code and no hardcoded urls

**Spec:**
```
Type:       Plugin (ESLint)
Features:   - Add a rule that forbids console.log outside test files
            - Add a rule that flags hardcoded http and https URLs
            - Allow URLs from an allowlist in the rule options
            - Provide an auto-fix that removes console.log calls
            - Export a recommended config
Tech stack: JavaScript, ESLint rule API, AST (ESTree)
```

---

## Example 114

**Intent:**
vite plugin that makes a list of all images used and warns if one is too big

**Spec:**
```
Type:       Plugin (Vite)
Features:   - Collect every image imported during the build
            - Record file size and dimensions of each image
            - Warn in the build output when an image exceeds a size limit
            - Write an image report JSON into the dist folder
            - Fail the build in CI when limits are exceeded
Tech stack: TypeScript, Vite plugin API (Rollup hooks), sharp
```

---

## Example 115

**Intent:**
mkdocs plugin to show last updated date and author for each page from git

**Spec:**
```
Type:       Plugin (MkDocs)
Features:   - Read the last commit date and author for each Markdown file
            - Show "Last updated" and author at the bottom of pages
            - Format dates for the site's locale
            - Fall back to file modified time when git is unavailable
            - Skip pages listed in an exclude option
Tech stack: Python, MkDocs plugin API, GitPython
```

---

## Example 116

**Intent:**
power bi custom visual that shows a calendar heatmap

**Spec:**
```
Type:       Plugin (Power BI custom visual)
Features:   - Accept a date field and a measure from the data view
            - Draw a year calendar with one colored cell per day
            - Let users set the color scale in the format pane
            - Show the exact value in a tooltip
            - Support cross-filtering when a day is clicked
Tech stack: TypeScript, Power BI Visuals API, D3.js
```

---

## Example 117

**Intent:**
tableau extension for writing comments on a dashboard that everyone can see

**Spec:**
```
Type:       Plugin (Tableau dashboard extension)
Data model: Comment(id, dashboard_id, worksheet, author, text, created_at)
Features:   - Show a comments panel inside the dashboard
            - Add a comment linked to the current filter selection
            - Restore filters when a comment is clicked
            - Mention colleagues by name
            - Delete own comments
API:        REST
            GET  /comments?dashboard={id}
            POST /comments
            DELETE /comments/{id}
Storage:    PostgreSQL
Tech stack: JavaScript, Tableau Extensions API, Node.js, Express
```

---

## Example 118

**Intent:**
salesforce component on the account page that shows open support tickets from zendesk

**Spec:**
```
Type:       Plugin (Salesforce Lightning Web Component)
Features:   - Show on the Account record page
            - Find the Zendesk organization by account domain
            - List open tickets with status and priority
            - Link each ticket to Zendesk
            - Refresh with a button
API:        Zendesk REST
            GET  /api/v2/organizations/{id}/tickets
Tech stack: JavaScript, Lightning Web Components, Apex, Named Credentials
```

---

## Example 119

**Intent:**
Hello. I want a plugin for SketchUp that counts how many of each component is in my model and the price. I am carpenter and I do this by hand now.

**Spec:**
```
Type:       Plugin (SketchUp extension)
Data model: ComponentPrice(definition_name, unit_price, unit)
Features:   - Count instances of each component definition in the model
            - Let the user enter a price for each component
            - Calculate the total cost of the model
            - Export the list to CSV
            - Update counts when the model changes
Storage:    SketchUp model attributes
Tech stack: Ruby, SketchUp Ruby API, HtmlDialog
```

---

## Example 120

**Intent:**
revit add-in that renames all the sheets with our office naming rule

**Spec:**
```
Type:       Plugin (Revit add-in)
Features:   - Load the naming rule (discipline-number-title) from a settings file
            - Preview new sheet numbers and names in a dialog
            - Rename sheets in one transaction
            - Skip sheets that already follow the rule
            - Write a log of changes
Tech stack: C#, Revit API, WPF
```

---

## Example 121

**Intent:**
autocad lisp that numbers all my parking spaces

**Spec:**
```
Type:       Plugin (AutoCAD AutoLISP routine)
Features:   - Ask the user to pick parking space blocks in order
            - Insert a number text at the center of each block
            - Let the user set a starting number and prefix
            - Keep text height relative to the drawing scale
            - Update a block attribute instead when one exists
Tech stack: AutoLISP
```

---

## Example 122

**Intent:**
lightroom plugin to export my photos straight to my portfolio website

**Spec:**
```
Type:       Plugin (Lightroom Classic publish service)
Features:   - Add a publish service for the portfolio
            - Upload exported photos to a chosen gallery
            - Send title, caption and keywords with each photo
            - Update photos on the site when they are re-edited
            - Delete photos from the site when removed from the collection
API:        REST
            POST /api/galleries/{id}/photos
            PUT  /api/photos/{id}
            DELETE /api/photos/{id}
Tech stack: Lua, Lightroom Classic SDK
```

---

## Example 123

**Intent:**
davinci resolve script that adds markers at every beat of the music

**Spec:**
```
Type:       Plugin (DaVinci Resolve script)
Features:   - Read the audio of the selected music clip
            - Detect beats with a beat tracking algorithm
            - Add timeline markers at each beat
            - Let the user add markers only on every 2nd or 4th beat
            - Color markers for downbeats differently
Tech stack: Python, DaVinci Resolve scripting API, librosa
```

---

## Example 124

**Intent:**
after effects script that makes lower thirds from a csv of names

**Spec:**
```
Type:       Plugin (After Effects ExtendScript)
Features:   - Read a CSV of names and titles
            - Duplicate a template composition for each row
            - Replace the text layers with the row values
            - Add each new comp to the render queue
            - Name comps after the person
Input:      CSV file and a template composition
Tech stack: ExtendScript (JavaScript), After Effects scripting API
```

---

## Example 125

**Intent:**
audacity plugin that removes long silences in podcasts

**Spec:**
```
Type:       Plugin (Audacity Nyquist plug-in)
Features:   - Find silent sections below a set dB level
            - Shorten silences longer than a threshold to a fixed length
            - Keep a small padding around speech
            - Show how much time was removed
            - Let users set threshold and minimum length in a dialog
Tech stack: Nyquist (Lisp), Audacity plug-in API
```

---

## Example 126

**Intent:**
musescore plugin that colors notes outside the instrument range

**Spec:**
```
Type:       Plugin (MuseScore)
Data model: InstrumentRange(instrument_id, low_pitch, high_pitch, comfortable_low, comfortable_high)
Features:   - Read each note's pitch and its staff instrument
            - Color notes outside the playable range red
            - Color notes outside the comfortable range orange
            - Show a list of problem measures
            - Reset note colors with a second command
Tech stack: QML, JavaScript, MuseScore plugin API
```

---

## Example 127

**Intent:**
aseprite script to export each tag as its own gif

**Spec:**
```
Type:       Plugin (Aseprite Lua script)
Features:   - List all animation tags in the sprite
            - Export each tag as a GIF named after the tag
            - Let the user set scale and output folder in a dialog
            - Respect frame durations
            - Skip hidden layers
Tech stack: Lua, Aseprite scripting API
```

---

## Example 128

**Intent:**
tiled extension to check my map has no unreachable areas

**Spec:**
```
Type:       Plugin (Tiled map editor extension)
Features:   - Read the collision layer of the current map
            - Flood fill walkable tiles from the player start object
            - Highlight walkable areas that cannot be reached
            - Show a count of unreachable regions
            - Run the check before saving
Tech stack: JavaScript, Tiled scripting API
```

---

## Example 129

**Intent:**
krita plugin that gives me a random drawing prompt and a timer for practice

**Spec:**
```
Type:       Plugin (Krita Python plug-in)
Data model: Prompt(id, category, text)
Features:   - Show a docker with a random prompt from chosen categories
            - Start a countdown timer for the sketch
            - Save the canvas automatically when time runs out
            - Keep a log of prompts and saved files
            - Let users add their own prompts
Storage:    JSON file in the Krita resources folder
Tech stack: Python, Krita scripting API, PyQt5
```

---

## Example 130

**Intent:**
inkscape extension that makes a laser cut box with finger joints

**Spec:**
```
Type:       Plugin (Inkscape extension)
Features:   - Ask for width, height, depth and material thickness
            - Generate six panels with finger joints
            - Add kerf compensation
            - Lay out panels on the page without overlap
            - Draw cut lines as hairline red strokes
Tech stack: Python, Inkscape extension API (inkex)
```

---

## Example 131

**Intent:**
freecad thing for making gears

**Spec:**
```
Type:       Plugin (FreeCAD workbench)
Features:   - Create spur gears from module, tooth count and pressure angle
            - Create helical gears with a helix angle
            - Keep gear parameters editable in the property view
            - Add a center bore with a keyway
            - Check meshing distance between two selected gears
Tech stack: Python, FreeCAD API, Part workbench
```

---

## Example 132

**Intent:**
Hey so my band uses ableton live and the drummer wants a Max for Live device that sends the tempo to his light rig over DMX

**Spec:**
```
Type:       Plugin (Max for Live device)
Features:   - Read the Live set tempo and beat position
            - Send a DMX pulse on every beat to a chosen channel
            - Map tempo to a color value on a second channel
            - Support an Art-Net output over the network
            - Let the user set the universe and channels in the device UI
Tech stack: Max/MSP, Max for Live, Live Object Model, Art-Net
```

---

## Example 133

**Intent:**
a vst plugin, simple tape delay with wow and flutter

**Spec:**
```
Type:       Plugin (VST3 audio effect)
Features:   - Delay audio with time, feedback and mix controls
            - Modulate delay time with slow wow and fast flutter LFOs
            - Add soft saturation in the feedback loop
            - Sync delay time to the host tempo
            - Show a simple GUI with knobs
Tech stack: C++, JUCE, VST3 SDK
```

---

## Example 134

**Intent:**
kodi addon for watching my local library's free film streaming service

**Spec:**
```
Type:       Plugin (Kodi video add-on)
Features:   - Log in with library card credentials
            - Browse films by genre and new arrivals
            - Search the catalog
            - Play streams with Kodi's player
            - Remember the remaining monthly loans
API:        REST
            GET  /api/films?genre={g}
            GET  /api/films/{id}/stream
Tech stack: Python, Kodi add-on API (xbmcplugin, xbmcgui)
```

---

## Example 135

**Intent:**
vlc extension that shows song lyrics while the music plays

**Spec:**
```
Type:       Plugin (VLC Lua extension)
Features:   - Read artist and title from the playing track's metadata
            - Fetch lyrics from a lyrics API
            - Show lyrics in a dialog window
            - Scroll synced lyrics when timestamps exist
            - Cache lyrics per track
API:        REST
            GET  https://lrclib.net/api/get?artist_name={a}&track_name={t}
Tech stack: Lua, VLC extension API
```

---

## Example 136

**Intent:**
nextcloud app where my family logs which chores are done

**Spec:**
```
Type:       Plugin (Nextcloud app)
Data model: Chore(id, name, points, frequency_days)
            Completion(id, chore_id -> Chore, user_id, completed_at)
Features:   - Create chores with points and a repeat interval
            - Mark chores done from a list
            - Show who did what this week
            - Show a points leaderboard
            - Highlight overdue chores
API:        REST
            GET  /apps/chores/api/chores
            POST /apps/chores/api/completions
Storage:    Nextcloud database (MariaDB)
Tech stack: PHP, Nextcloud App Framework, Vue.js
```

---

## Example 137

**Intent:**
discourse plugin to give users a badge for their first accepted solution

**Spec:**
```
Type:       Plugin (Discourse)
Features:   - Listen for posts marked as the accepted solution
            - Grant a "First Solution" badge on the first one
            - Post a congratulations message to the user
            - Show solution count on user cards
            - Add a site setting to turn it off
Storage:    Discourse PostgreSQL database
Tech stack: Ruby, Ruby on Rails, Discourse plugin API, Ember.js
```

---

## Example 138

**Intent:**
jenkins plugin that posts build results to our mattermost

**Spec:**
```
Type:       Plugin (Jenkins)
Features:   - Add a post-build step for Mattermost notifications
            - Send build status, duration and changes to a channel webhook
            - Mention the committer on failure
            - Configure the webhook URL globally and per job
            - Support pipeline syntax with a mattermostSend step
API:        REST
            POST {mattermost_webhook_url}
Tech stack: Java, Jenkins plugin API, Maven
```

---

## Example 139

**Intent:**
backstage plugin that shows the on-call person for each service

**Spec:**
```
Type:       Plugin (Backstage)
Features:   - Add an "On call" card to the service entity page
            - Read the PagerDuty service ID from entity annotations
            - Show the current on-call engineer and escalation policy
            - Show open incidents for the service
            - Link to trigger an incident
API:        PagerDuty REST
            GET  /oncalls?schedule_ids[]={id}
            GET  /incidents?service_ids[]={id}
Tech stack: TypeScript, React, Backstage plugin API
```

---

## Example 140

**Intent:**
kubectl plugin to show which pods use the most memory compared to their limits

**Spec:**
```
Type:       Plugin (kubectl)
Features:   - Read pod metrics from the metrics API
            - Compare memory usage with each container's limit
            - Sort pods by usage percentage
            - Color rows above 80%
            - Filter by namespace or label selector
Tech stack: Go, client-go, Kubernetes metrics API, krew
```

---

## Example 141

**Intent:**
helo, i need wordpress-like but for joomla, a module that shows prayer times for my city on mosque website

**Spec:**
```
Type:       Plugin (Joomla module)
Data model: Settings(city, country, calculation_method, timezone)
Features:   - Fetch daily prayer times for the configured city
            - Show the five prayer times in a table
            - Highlight the next prayer with a countdown
            - Let the admin choose the calculation method
            - Cache times for the day
API:        REST
            GET  https://api.aladhan.com/v1/timingsByCity
Tech stack: PHP, Joomla 5 module API
```

---

## Example 142

**Intent:**
drupal module that adds a reading time estimate to every article

**Spec:**
```
Type:       Plugin (Drupal module)
Features:   - Count words in the article body field
            - Calculate reading time at a configurable words per minute
            - Show "X min read" above the article
            - Store the value in a field updated on save
            - Add the reading time to Views
Tech stack: PHP, Drupal 10 module API
```

---

## Example 143

**Intent:**
chrome extension that blurs spoilers about tv shows i'm watching

**Spec:**
```
Type:       Browser extension (spoiler blocker)
Data model: WatchedShow(id, name, keywords, current_episode)
Features:   - Let the user list shows and character names to hide
            - Blur page text and images containing those keywords
            - Reveal a blurred item on click
            - Scan new content on social media feeds as it loads
            - Pause blocking for a show after the user finishes it
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3, MutationObserver
```

---

## Example 144

**Intent:**
browser extension that warns me if a website im on had a data breach

**Spec:**
```
Type:       Browser extension (breach warning)
Features:   - Check the current site's domain against the Have I Been Pwned breach list
            - Show a warning badge on the toolbar icon
            - Show breach date and leaked data types in the popup
            - Refresh the breach list daily
            - Let the user dismiss warnings per site
API:        HIBP REST
            GET  https://haveibeenpwned.com/api/v3/breaches
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 145

**Intent:**
ok so i'm doing my masters and every time i read a paper online i forget where i found it and what i thought about it. i'd love something in the browser where i click once and it saves the paper title, link, and lets me write two lines about why it matters, and later i can see everything grouped by my thesis chapters

**Spec:**
```
Type:       Browser extension (research reading log)
Data model: Chapter(id, title, order)
            SavedPaper(id, title, url, doi, chapter_id -> Chapter, why_it_matters, saved_at)
Features:   - Save the current paper's title, URL and DOI with one click
            - Add a short "why it matters" note in the popup
            - Assign the paper to a thesis chapter
            - Show all saved papers grouped by chapter on an overview page
            - Export a chapter's papers as a BibTeX file
Storage:    IndexedDB (via Dexie.js)
Tech stack: TypeScript, Chrome Extension Manifest V3, Dexie.js
```

---

## Example 146

**Intent:**
plz make chrome extnsion that shows me how much i spent on amazon this year, i think its alot lol

**Spec:**
```
Type:       Browser extension (spending tracker)
Data model: Order(id, order_number, date, total, currency)
Features:   - Read orders from the Amazon order history pages page by page
            - Sum spending by month and by year
            - Show a bar chart of monthly spending in the popup
            - Show the most expensive orders
            - Keep all data local in the browser
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, Chart.js
```

---

## Example 147

**Intent:**
I'm a high school teacher and we use Google Classroom. I want a Chrome extension that lets me leave the same feedback comments quickly when I grade, like a comment bank, because I type the same things 100 times.

**Spec:**
```
Type:       Browser extension (grading comment bank)
Data model: Comment(id, text, category, uses_count)
            Category(id, name)
Features:   - Store reusable feedback comments grouped by category
            - Open the comment bank with a keyboard shortcut in the grading view
            - Insert a comment into the focused text box
            - Fill placeholders like {name} with the student's first name
            - Sort comments by most used
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 148

**Intent:**
zoom app that takes attendance for my online class and puts it in a spreadsheet

**Spec:**
```
Type:       Plugin (Zoom App)
Data model: Session(id, meeting_id, date)
            Attendance(session_id -> Session, participant_name, email, joined_at, left_at, minutes)
Features:   - Read the participant list when the meeting ends
            - Calculate minutes attended for each person
            - Mark students below a minimum time as late
            - Append the attendance to a Google Sheet per class
            - Show today's attendance in the Zoom side panel
API:        Zoom REST
            GET  /v2/past_meetings/{meetingUUID}/participants
Storage:    Google Sheets
Tech stack: Node.js, Zoom Apps SDK, Zoom REST API, Google Sheets API
```

---

## Example 149

**Intent:**
jira plugin that makes release notes from the tickets in a version

**Spec:**
```
Type:       Plugin (Jira Cloud)
Features:   - Add a "Generate release notes" action on the release page
            - Collect issues in the fix version grouped by issue type
            - Use a custom field for the public description when it is filled
            - Render the notes in Markdown or HTML
            - Publish the notes as a Confluence page
API:        Jira REST
            GET  /rest/api/3/search?jql=fixVersion={id}
Tech stack: Atlassian Forge, TypeScript, Confluence REST API
```

---

## Example 150

**Intent:**
obsidian plugin that turns links to youtube into a nice card with thumbnail

**Spec:**
```
Type:       Plugin (Obsidian)
Features:   - Detect YouTube links in reading view
            - Fetch title, channel and thumbnail with the oEmbed endpoint
            - Render the link as a card with the thumbnail
            - Add a command to convert a pasted link into a card block
            - Cache video info in plugin data
API:        REST
            GET  https://www.youtube.com/oembed?url={url}&format=json
Storage:    Obsidian plugin data.json
Tech stack: TypeScript, Obsidian API
```

---

## Example 151

**Intent:**
i need blender addon where i click and it makes a turntable animation of my model for portfolio

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Create a camera and an empty at the model's center
            - Animate a full 360 degree rotation over a chosen number of frames
            - Add a three-point light setup and neutral background
            - Set render resolution and output path
            - Start the render from one button
Tech stack: Python, Blender bpy API
```

---

## Example 152

**Intent:**
Our customer success team lives in HubSpot. I want a card on each company record that shows their product usage from our own database, like last login and number of active users.

**Spec:**
```
Type:       Plugin (HubSpot UI extension)
Features:   - Show a usage card in the company record sidebar
            - Look up the company by domain in our product database
            - Show last login, active users and plan
            - Flag accounts with no logins in 14 days
            - Link to the internal admin page
API:        REST
            GET  /usage/companies?domain={domain}
Tech stack: TypeScript, React, HubSpot UI Extensions, Node.js serverless functions
```

---

## Example 153

**Intent:**
miro app that turns sticky notes into jira tickets

**Spec:**
```
Type:       Plugin (Miro app)
Features:   - Let the user select sticky notes on the board
            - Create one Jira issue per sticky note with its text as the summary
            - Let the user pick the Jira project and issue type
            - Add the issue link back onto the sticky note
            - Change the sticky note color once created
API:        Jira REST
            POST /rest/api/3/issue
Tech stack: TypeScript, Miro Web SDK, Jira Cloud REST API
```

---

## Example 154

**Intent:**
airtable extension that shows records on a map

**Spec:**
```
Type:       Plugin (Airtable extension)
Features:   - Let the user pick a table and an address or lat/lng field
            - Geocode addresses and cache coordinates in a field
            - Show records as markers on a map
            - Open the record when a marker is clicked
            - Color markers by a single-select field
Tech stack: JavaScript, React, Airtable Blocks SDK, Leaflet
```

---

## Example 155

**Intent:**
whats a good way to have notion pages for each github issue automatically

**Spec:**
```
Type:       Webhook service (GitHub to Notion sync)
Data model: IssueLink(github_issue_id, repo, notion_page_id)
Features:   - Receive GitHub issue webhooks
            - Create a Notion database page for each new issue
            - Update status, labels and assignee when the issue changes
            - Archive the page when the issue is closed
            - Verify GitHub webhook signatures
API:        REST
            POST /webhooks/github
Storage:    SQLite
Tech stack: Node.js, Express, Notion API, Octokit
```

---

## Example 156

**Intent:**
hi i'm a mod on a big discord server and people keep posting scam links. need a bot that deletes them and times out the person

**Spec:**
```
Type:       Bot (Discord moderation)
Data model: BlockedDomain(domain, added_by, added_at)
            Incident(id, guild_id, user_id, message_content, url, action, created_at)
Features:   - Check every message for links
            - Delete messages with links to known scam domains
            - Time out the sender for a set duration
            - Log incidents to a mod channel
            - Let mods add or remove domains with slash commands
Storage:    PostgreSQL
Tech stack: Python, discord.py, asyncpg
```

---

## Example 157

**Intent:**
home assistant integration for my apartment buildings laundry room website so i can see which machines are free

**Spec:**
```
Type:       Plugin (Home Assistant custom integration)
Features:   - Log in to the laundry portal and keep the session
            - Scrape machine status every 2 minutes
            - Create a binary sensor per machine (free or busy)
            - Create a sensor for minutes remaining
            - Notify when a chosen machine becomes free
Tech stack: Python, Home Assistant integration framework, aiohttp, BeautifulSoup
```

---

## Example 158

**Intent:**
grafana app plugin for our sre team to write postmortems linked to dashboards

**Spec:**
```
Type:       Plugin (Grafana app)
Data model: Postmortem(id, title, incident_start, incident_end, summary, root_cause, author_id)
            ActionItem(id, postmortem_id -> Postmortem, text, owner, done)
            LinkedPanel(postmortem_id -> Postmortem, dashboard_uid, panel_id)
Features:   - Create postmortems from a template
            - Attach dashboard panels at the incident's time range
            - List action items with owners and status
            - Show all postmortems in a searchable list
            - Export a postmortem as Markdown
API:        REST
            GET  /api/plugins/postmortems/resources/postmortems
            POST /api/plugins/postmortems/resources/postmortems
Storage:    SQLite (plugin backend)
Tech stack: Go, TypeScript, React, Grafana plugin SDK
```

---

## Example 159

**Intent:**
raycast extension: paste clipboard as plain text with smart quotes fixed

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Read the current clipboard text
            - Strip formatting and convert curly quotes to straight quotes
            - Collapse repeated spaces and fix line breaks
            - Paste the cleaned text into the front app
            - Offer other options like Title Case and lowercase
Tech stack: TypeScript, Raycast API
```

---

## Example 160

**Intent:**
logseq plugin where i can see a calendar of my journal pages and which days are empty

**Spec:**
```
Type:       Plugin (Logseq)
Features:   - Show a month calendar in the right sidebar
            - Mark days that have journal pages with content
            - Show word count per day as dot size
            - Open a journal page by clicking its day
            - Create a missing journal page from the calendar
Tech stack: TypeScript, Logseq Plugin SDK, React
```

---

## Example 161

**Intent:**
anki addon that imports words from my kindle vocabulary builder

**Spec:**
```
Type:       Plugin (Anki add-on)
Features:   - Read the Kindle vocab.db SQLite file
            - List looked-up words with their book and sentence
            - Let the user pick which words to import
            - Create notes with word, context sentence and book title
            - Look up definitions from a dictionary API
Input:      Kindle vocab.db file
Tech stack: Python, Anki add-on API, sqlite3, PyQt6
```

---

## Example 162

**Intent:**
zotero plugin to send selected papers to my e-reader

**Spec:**
```
Type:       Plugin (Zotero)
Data model: Device(id, name, kind, email_or_path)
Features:   - Add a "Send to device" item to the right-click menu
            - Send PDFs to a Kindle by email
            - Copy PDFs to a mounted reader like Kobo or reMarkable folder
            - Rename files as "Author - Title"
            - Tag items as sent
Storage:    Zotero preferences
Tech stack: JavaScript, Zotero 7 plugin API, nodemailer
```

---

## Example 163

**Intent:**
chrome extension for job seekers that tracks every job i apply to on linkedin and indeed

**Spec:**
```
Type:       Browser extension (job application tracker)
Data model: Application(id, company, title, url, source, status, applied_at, notes)
Features:   - Detect "Apply" clicks on LinkedIn and Indeed job pages
            - Save company, title and URL automatically
            - Track status (applied, interview, offer, rejected)
            - Show a kanban board of applications in a new tab
            - Remind the user to follow up after 7 days
Storage:    IndexedDB
Tech stack: TypeScript, Chrome Extension Manifest V3, React
```

---

## Example 164

**Intent:**
browser extension that shows the real reviews score on amazon by filtering fake looking ones

**Spec:**
```
Type:       Browser extension (review analysis)
Data model: ReviewAnalysis(product_id, total_reviews, suspicious_count, adjusted_rating, analyzed_at)
Features:   - Collect reviews from the product review pages
            - Flag suspicious reviews (burst dates, unverified purchases, repeated phrases)
            - Calculate an adjusted rating without flagged reviews
            - Show the adjusted rating next to the original
            - Explain why reviews were flagged
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 165

**Intent:**
unity editor thing that shows which scripts are slow in the profiler by name

**Spec:**
```
Type:       Plugin (Unity editor extension)
Features:   - Read profiler frame data from the current session
            - Aggregate time per MonoBehaviour method over many frames
            - Show the top 20 slowest methods in a table
            - Highlight GC allocations per method
            - Export results as CSV
Tech stack: C#, Unity Editor API, ProfilerDriver, FrameDataView
```

---

## Example 166

**Intent:**
godot tool that makes a level from a png where each color is a tile

**Spec:**
```
Type:       Plugin (Godot editor plugin)
Features:   - Let the user pick a PNG and a color-to-tile mapping
            - Read each pixel's color
            - Paint the matching tile into a TileMapLayer
            - Warn about colors without a mapping
            - Re-import the level when the PNG changes
Tech stack: GDScript, Godot 4 EditorPlugin API, EditorImportPlugin
```

---

## Example 167

**Intent:**
obs plugin to show chat messages from youtube and twitch together on stream

**Spec:**
```
Type:       Plugin (OBS Studio browser source overlay)
Features:   - Connect to Twitch chat through IRC over WebSocket
            - Poll the YouTube live chat API
            - Merge messages into one list with platform icons
            - Show the list as a transparent browser source
            - Hide messages from bots and blocked words
API:        YouTube REST
            GET  /youtube/v3/liveChat/messages
Tech stack: JavaScript, Node.js, tmi.js, YouTube Data API v3
```

---

## Example 168

**Intent:**
chrome extension that tells me if a recipe site is mostly ads and just shows the recipe

**Spec:**
```
Type:       Browser extension (recipe reader)
Features:   - Find schema.org Recipe data on the page
            - Show ingredients and steps in a clean overlay
            - Scale ingredient quantities by servings
            - Keep the screen awake while cooking
            - Print the clean recipe
Tech stack: JavaScript, Chrome Extension Manifest V3, Screen Wake Lock API
```

---

## Example 169

**Intent:**
im a nurse student and i want anki addon that makes cards from my lecture powerpoints

**Spec:**
```
Type:       Plugin (Anki add-on)
Features:   - Import a .pptx file chosen by the user
            - Create one card per slide with the title as front and bullet text as back
            - Add slide images to the back of cards
            - Tag cards with the lecture name
            - Preview cards before adding
Input:      PowerPoint (.pptx) file
Tech stack: Python, Anki add-on API, python-pptx
```

---

## Example 170

**Intent:**
Canvas plugin so teachers can see which students haven't opened the course in a week

**Spec:**
```
Type:       Plugin (Canvas LTI 1.3 tool)
Features:   - Read last activity dates from Canvas enrollments
            - List students inactive for more than 7 days
            - Send a message to selected students through Canvas inbox
            - Show a chart of daily active students
            - Export the list to CSV
API:        Canvas REST
            GET  /api/v1/courses/{id}/enrollments
            POST /api/v1/conversations
Tech stack: Python, Flask, PyLTI1p3, Canvas REST API
```

---

## Example 171

**Intent:**
teams app where people can give each other kudos and see a wall of them

**Spec:**
```
Type:       Plugin (Microsoft Teams app)
Data model: Kudos(id, from_user_id, to_user_id, message, value_tag, created_at)
Features:   - Send kudos with a message and a company value tag from a message extension
            - Post a card to the team channel
            - Show a kudos wall tab with filters by value
            - Show monthly top receivers
            - Let admins edit value tags
API:        REST
            POST /kudos
            GET  /kudos?team={id}
Storage:    Azure Table Storage
Tech stack: TypeScript, Teams Toolkit, React, Azure Functions
```

---

## Example 172

**Intent:**
Hi, I make wedding photos. I need Lightroom plugin, when I export it makes watermark with my logo and also put the client name in the file

**Spec:**
```
Type:       Plugin (Lightroom Classic export filter)
Features:   - Add an export post-process action
            - Place the logo image as a watermark with set size and opacity
            - Read the client name from a custom metadata field
            - Rename files as client-name_sequence
            - Skip the watermark for a "client originals" preset
Tech stack: Lua, Lightroom Classic SDK, ImageMagick
```

---

## Example 173

**Intent:**
moodle block showing upcoming exams countdown

**Spec:**
```
Type:       Plugin (Moodle block)
Features:   - Read quiz and assignment deadlines in the course
            - Show a countdown for the next three exams
            - Mark exams the student already submitted
            - Let teachers flag which activities count as exams
            - Display in the course sidebar
Storage:    Moodle database
Tech stack: PHP, Moodle Block API, Mustache
```

---

## Example 174

**Intent:**
trello power up that shows the weather for cards with a date and location

**Spec:**
```
Type:       Plugin (Trello Power-Up)
Features:   - Add a location field to cards
            - Read the card due date
            - Show a forecast badge for the date and location
            - Show a detailed forecast on the card back
            - Update badges every three hours
API:        REST
            GET  https://api.open-meteo.com/v1/forecast
Storage:    Trello pluginData
Tech stack: JavaScript, Trello Power-Up client library, Open-Meteo API
```

---

## Example 175

**Intent:**
confluence plugin that checks pages for broken links

**Spec:**
```
Type:       Plugin (Confluence Cloud app)
Data model: LinkCheck(page_id, url, status_code, checked_at)
Features:   - Scan pages in a space for external links
            - Request each link and record the HTTP status
            - Show broken links per page in a report
            - Re-check weekly with a scheduled trigger
            - Notify page owners about broken links
API:        Confluence REST
            GET  /wiki/api/v2/spaces/{id}/pages
Storage:    Forge storage API
Tech stack: Atlassian Forge, TypeScript, Forge scheduled triggers
```

---

## Example 176

**Intent:**
photoshop plugin that makes all the app icon sizes from one image

**Spec:**
```
Type:       Plugin (Photoshop UXP)
Features:   - Use the open 1024x1024 document as the source
            - Export icons at every iOS and Android size
            - Name files following platform conventions
            - Generate a Contents.json for Xcode
            - Warn when the source is not square
Tech stack: JavaScript, Adobe UXP, Photoshop batchPlay API
```

---

## Example 177

**Intent:**
gimp plugin that removes the background from product photos

**Spec:**
```
Type:       Plugin (GIMP Python plug-in)
Features:   - Send the active layer to a local background removal model
            - Add the result as a new layer with a mask
            - Refine edges with a feather radius option
            - Fill the background with white or keep transparency
            - Process a folder in batch mode
Tech stack: Python, GIMP 3 Python API, rembg
```

---

## Example 178

**Intent:**
extension for language learners where i can select a sentence on a page and save it as a flashcard with translation

**Spec:**
```
Type:       Browser extension (sentence mining)
Data model: SentenceCard(id, sentence, translation, source_url, target_word, created_at)
Features:   - Add a context menu item to save the selected sentence
            - Translate the sentence with a translation API
            - Mark the target word in the sentence
            - Send the card to Anki through AnkiConnect
            - Keep a local list of mined sentences
API:        AnkiConnect
            POST http://localhost:8765 (addNote)
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, DeepL API, AnkiConnect
```

---

## Example 179

**Intent:**
I have macular degeneration and small text on websites is really hard for me. My son says there are extensions but they are confusing. I need one big button that makes the page readable.

**Spec:**
```
Type:       Browser extension (low vision reading mode)
Data model: Settings(text_size, color_scheme, line_spacing)
Features:   - Turn on a reading mode with one large toolbar button
            - Show the main page text in a large font with high contrast
            - Offer three simple color schemes (black on white, yellow on black, white on blue)
            - Read the page aloud with a play button
            - Remember the setting for every site
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3, Mozilla Readability, Web Speech API
```

---

## Example 180

**Intent:**
github extension that shows file sizes and lets me download one folder

**Spec:**
```
Type:       Browser extension (GitHub helper)
Features:   - Show file sizes next to files in repository listings
            - Show total repository size in the header
            - Add a download button to folder pages
            - Download a single folder as a ZIP using the contents API
            - Support private repositories with a token
API:        GitHub REST
            GET  /repos/{owner}/{repo}/contents/{path}
Tech stack: TypeScript, Chrome Extension Manifest V3, JSZip
```

---

## Example 181

**Intent:**
i make youtube videos and i want a chrome extension that shows tags and upload time of other people's videos

**Spec:**
```
Type:       Browser extension (creator research)
Features:   - Read the video's keywords from the watch page
            - Show tags in a panel under the video
            - Show the exact upload date and time
            - Show views per hour since upload
            - Copy all tags with one click
API:        YouTube Data REST
            GET  /youtube/v3/videos?part=snippet,statistics&id={id}
Tech stack: JavaScript, Chrome Extension Manifest V3, YouTube Data API v3
```

---

## Example 182

**Intent:**
home assistant integration thats for the bus stop near me showing next departures

**Spec:**
```
Type:       Plugin (Home Assistant custom integration)
Features:   - Configure the stop ID and lines through a config flow
            - Fetch real-time departures from a GTFS-Realtime feed
            - Create a sensor for the next departure in minutes
            - Add attributes with the next five departures
            - Mark delayed departures
Tech stack: Python, Home Assistant integration framework, gtfs-realtime-bindings
```

---

## Example 183

**Intent:**
grafana panel that is a status board with green/red tiles per service

**Spec:**
```
Type:       Plugin (Grafana panel)
Features:   - Show one tile per series with its name
            - Color tiles by threshold rules
            - Show the time since the last state change
            - Make tiles clickable with data links
            - Configure tile size and columns in panel options
Tech stack: TypeScript, React, Grafana plugin SDK
```

---

## Example 184

**Intent:**
something to make discord show what song im playing on my local music player

**Spec:**
```
Type:       Desktop application (Discord Rich Presence)
Features:   - Read the currently playing track from MPRIS or the media session
            - Set Discord Rich Presence with title, artist and album
            - Show elapsed time and album art when available
            - Clear the status when playback stops
            - Run in the system tray
Tech stack: Python, pypresence, dbus-next
```

---

## Example 185

**Intent:**
obsidian plugin for d&d campaign notes that rolls dice when i click a formula

**Spec:**
```
Type:       Plugin (Obsidian)
Features:   - Detect dice formulas like 2d6+3 in notes
            - Roll the dice when the formula is clicked
            - Show the result and individual rolls in a notice
            - Keep a roll history in a side panel
            - Support rolling from tables in notes
Storage:    Obsidian plugin data.json
Tech stack: TypeScript, Obsidian API, rpg-dice-roller
```

---

## Example 186

**Intent:**
jira plugn that shows a tickets age in days on the board cards, old ones in red

**Spec:**
```
Type:       Plugin (Jira Cloud)
Features:   - Calculate days since each issue was created
            - Show the age as a badge on board cards
            - Color badges yellow after 7 days and red after 14
            - Let admins set thresholds per project
            - Exclude issues in the Done column
API:        Jira REST
            GET  /rest/api/3/search?jql=project={key}
Tech stack: Atlassian Forge, TypeScript, React
```

---

## Example 187

**Intent:**
my lab uses electronic lab notebook online, and I want firefox addon that copies the chemical name I select and shows structure from pubchem

**Spec:**
```
Type:       Browser extension (chemistry lookup)
Features:   - Add a context menu item for selected chemical names
            - Look up the compound in PubChem
            - Show the 2D structure image, formula and molar mass in a popup
            - Copy the SMILES string with one click
            - Link to the full PubChem page
API:        PubChem PUG REST
            GET  /rest/pug/compound/name/{name}/property/MolecularFormula,MolecularWeight,CanonicalSMILES/JSON
Tech stack: JavaScript, Firefox WebExtensions API, PubChem PUG REST
```

---

## Example 188

**Intent:**
obs studio plugin replay buffer clips get named with game name and uploaded to google drive

**Spec:**
```
Type:       Plugin (OBS Studio script)
Features:   - Listen for the replay buffer saved event
            - Detect the game from the active window title
            - Rename the clip as game_date_time.mp4
            - Upload the clip to a Drive folder per game
            - Copy the share link to the clipboard
Tech stack: Python, OBS Studio scripting API, Google Drive API
```

---

## Example 189

**Intent:**
i teach piano and want a zoom app with a little metronome everyone hears in sync

**Spec:**
```
Type:       Plugin (Zoom App)
Features:   - Let the host set tempo and time signature
            - Sync beat start across participants using server time
            - Play clicks locally on each device to avoid audio lag
            - Show a visual beat indicator
            - Let students tap along and show their timing accuracy
API:        WebSocket
            /ws/metronome/{meeting_id}
Tech stack: TypeScript, Zoom Apps SDK, Web Audio API, Node.js
```

---

## Example 190

**Intent:**
blender addon checks my model before i sell it on a 3d marketplace, like ngons, non manifold, missing uvs

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Count n-gons, triangles and quads in selected meshes
            - Find non-manifold edges and loose vertices
            - Check that every mesh has a UV map and no overlapping UVs
            - Check that scale and rotation are applied
            - Show a report panel with select buttons for each problem
Tech stack: Python, Blender bpy API, bmesh
```

---

## Example 191

**Intent:**
Can you design a Raycast extension for our support team: type an order number, see the order status from our Shopify store and the shipping tracking?

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Search orders by number
            - Show order status, items and customer
            - Show tracking number and carrier status
            - Copy a customer reply template with the details
            - Open the order in Shopify admin
API:        Shopify Admin GraphQL
            POST /admin/api/2024-07/graphql.json
Tech stack: TypeScript, React, Raycast API, Shopify Admin GraphQL API
```

---

## Example 192

**Intent:**
pls i want discord bot that tell us when our minecraft server is down

**Spec:**
```
Type:       Bot (Discord)
Data model: ServerWatch(id, guild_id, channel_id, host, port, last_status, last_checked)
Features:   - Ping the Minecraft server every minute
            - Post a message when it goes down or comes back
            - Show player count and version with a /status command
            - Mention a role on outages
            - Keep a 24-hour uptime percentage
Storage:    SQLite
Tech stack: Python, discord.py, mcstatus
```

---

## Example 193

**Intent:**
chrome extension for second-hand sellers on vinted to bump relist old items

**Spec:**
```
Type:       Browser extension (reseller listing helper)
Data model: TrackedItem(id, title, price, listed_at, views, favourites)
Features:   - List the user's items with age, views and favourites
            - Flag items older than 30 days with few views
            - Duplicate an old listing into a new draft with the same photos and text
            - Suggest a price drop percentage
            - Keep a history of relisted items
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 194

**Intent:**
Hi team, I am product manager in India. We want Confluence app that shows the Jira epics roadmap as timeline on any page, it should update automatically.

**Spec:**
```
Type:       Plugin (Confluence Cloud macro)
Features:   - Insert a roadmap macro with a Jira project or JQL filter
            - Show epics as bars on a monthly timeline by start and due dates
            - Color bars by status
            - Show progress from child issue completion
            - Refresh data on each page view
API:        Jira REST
            GET  /rest/api/3/search?jql={jql}
Tech stack: Atlassian Forge, TypeScript, React (Custom UI)
```

---

## Example 195

**Intent:**
obsidian plugin that auto links names of people when i type them

**Spec:**
```
Type:       Plugin (Obsidian)
Features:   - Read note titles from a "People" folder
            - Detect those names while typing
            - Suggest turning a name into a wiki link
            - Support aliases from frontmatter
            - Add a command to link all names in the current note
Tech stack: TypeScript, Obsidian API, CodeMirror 6
```

---

## Example 196

**Intent:**
unity editor extension for localization: a table where i edit all the text keys and languages

**Spec:**
```
Type:       Plugin (Unity editor extension)
Data model: LocalizationTable(id, languages)
            Entry(key, table_id -> LocalizationTable, translations_json)
Features:   - Show a spreadsheet-like window with keys as rows and languages as columns
            - Add, rename and delete keys
            - Highlight missing translations
            - Import and export CSV for translators
            - Generate a C# class with constants for keys
Storage:    ScriptableObject assets
Tech stack: C#, Unity Editor API (EditorWindow, UI Toolkit)
```

---

## Example 197

**Intent:**
zotero plugin to make a literature review table from selected papers

**Spec:**
```
Type:       Plugin (Zotero)
Data model: ReviewColumn(id, name, source_field)
Features:   - Let the user define columns like method, sample size and findings
            - Fill columns from item fields and notes
            - Show the table in a new tab
            - Edit cells and save them as child notes
            - Export the table to CSV or Word
Tech stack: JavaScript, Zotero 7 plugin API, docx.js
```

---

## Example 198

**Intent:**
browser extension to help my grandma, make all buttons huge and remove ads on the news site she reads

**Spec:**
```
Type:       Browser extension (senior-friendly browsing)
Data model: SiteRule(domain, hide_selectors, font_scale)
Features:   - Enlarge buttons, links and text on chosen sites
            - Hide ad and pop-up elements with filter rules
            - Remove auto-playing videos
            - Add a large "Back" button floating on the page
            - Let a family member set it up remotely through synced settings
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3 (declarativeNetRequest)
```

---

## Example 199

**Intent:**
anki addon thats a heatmap for my reviews but by deck

**Spec:**
```
Type:       Plugin (Anki add-on)
Features:   - Read review history per deck
            - Draw a calendar heatmap for each deck
            - Show the streak for each deck
            - Show the heatmaps in the deck browser screen
            - Let users hide decks from the view
Tech stack: Python, Anki add-on API, HTML/JavaScript webview
```

---

## Example 200

**Intent:**
moodle plugin that lets students book a time slot with the teacher for consultation

**Spec:**
```
Type:       Plugin (Moodle activity module)
Data model: Slot(id, course_module_id, teacher_id, start_time, duration_minutes, location)
            Booking(id, slot_id -> Slot, student_id, note)
Features:   - Let teachers create time slots in bulk
            - Let students book one free slot
            - Send calendar events to both people
            - Let students cancel up to 24 hours before
            - Show the teacher a list of bookings per day
Storage:    Moodle database
Tech stack: PHP, Moodle Activity Module API, Moodle Calendar API
```

---

## Example 201

**Intent:**
i want a chrome extension that saves my place in long articles, like a bookmark for scroll position

**Spec:**
```
Type:       Browser extension (reading position)
Data model: Position(url, scroll_percent, paragraph_text, updated_at)
Features:   - Save the scroll position of long articles automatically
            - Show a "continue reading" prompt when returning to the page
            - Find the saved paragraph even if the layout changed
            - List unfinished articles in the popup
            - Remove articles that are finished
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 202

**Intent:**
logseq plugin for pomodoro on a task block

**Spec:**
```
Type:       Plugin (Logseq)
Features:   - Add a slash command that inserts a pomodoro timer into a block
            - Count down 25 minutes and play a sound at the end
            - Log completed pomodoros as a block property
            - Show today's pomodoro count in the toolbar
            - Start a 5-minute break timer after each pomodoro
Tech stack: TypeScript, Logseq Plugin SDK
```

---

## Example 203

**Intent:**
teams bot that answers HR questions from our handbook

**Spec:**
```
Type:       Bot (Microsoft Teams)
Data model: HandbookChunk(id, section, text, embedding)
Features:   - Answer questions in chat using the employee handbook
            - Show the handbook section used as a source
            - Say when it cannot find an answer and give the HR contact
            - Re-index the handbook when HR uploads a new version
            - Log unanswered questions for HR
Storage:    PostgreSQL with pgvector
Tech stack: Python, Bot Framework SDK, Azure OpenAI, pgvector
```

---

## Example 204

**Intent:**
home assistant plugin to show my solar panel production vs house usage as a flow animation

**Spec:**
```
Type:       Plugin (Home Assistant Lovelace card)
Features:   - Read solar, grid, battery and home power sensors
            - Draw animated flows between solar, grid, battery and home icons
            - Scale animation speed by power
            - Show daily energy totals
            - Configure entity IDs in a visual card editor
Tech stack: TypeScript, Lit, Home Assistant custom card API
```

---

## Example 205

**Intent:**
grafana plugin to show a world map of where our users come from with dots sized by count

**Spec:**
```
Type:       Plugin (Grafana panel)
Features:   - Read country codes or coordinates from the query result
            - Draw a world map with circles sized by count
            - Color circles by a second metric
            - Show a tooltip with country and values
            - Zoom and pan the map
Tech stack: TypeScript, React, Grafana plugin SDK, d3-geo
```

---

## Example 206

**Intent:**
i need a chrome extension for my seo job that shows meta tags, headings and word count of any page

**Spec:**
```
Type:       Browser extension (SEO audit)
Features:   - Show title, meta description and their lengths
            - List H1 to H6 headings in an outline
            - Count words and internal and external links
            - Show canonical, robots and hreflang tags
            - Flag missing alt text on images
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 207

**Intent:**
discord bot for study groups: pomodoro sessions in voice channels

**Spec:**
```
Type:       Bot (Discord)
Data model: StudySession(id, guild_id, voice_channel_id, work_minutes, break_minutes, started_at)
            StudyStats(user_id, guild_id, total_minutes)
Features:   - Start a group pomodoro with a slash command
            - Announce work and break periods in the channel
            - Play a short sound in the voice channel at each change
            - Track study minutes for each member in the channel
            - Show a weekly study leaderboard
Storage:    PostgreSQL
Tech stack: Node.js, discord.js, @discordjs/voice
```

---

## Example 208

**Intent:**
OBS plugin to show my keyboard and mouse presses for tutorial videos

**Spec:**
```
Type:       Plugin (OBS Studio)
Features:   - Capture global key and mouse button events
            - Show pressed keys as on-screen keycaps
            - Combine modifier shortcuts like Ctrl+Shift+S
            - Fade keys out after a delay
            - Let users style keycaps in source properties
Tech stack: C++, OBS Studio plugin API, libuiohook
```

---

## Example 209

**Intent:**
wanna make a chrome extention that shows if a news article is from a site that leans left or right

**Spec:**
```
Type:       Browser extension (news source info)
Data model: SourceRating(domain, bias_label, factual_rating, source_url)
Features:   - Look up the current site's domain in a bias ratings list
            - Show a colored badge with the bias label
            - Show factual reporting rating in the popup
            - Link to the source of the rating
            - Update the ratings list weekly
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 210

**Intent:**
photoshop plugin with a panel of our brand colors and fonts so the design team stays consistent

**Spec:**
```
Type:       Plugin (Photoshop UXP)
Data model: BrandKit(id, name, colors_json, fonts_json, logos)
Features:   - Show brand colors as swatches in a panel
            - Set foreground color with one click
            - Apply brand text styles to the selected text layer
            - Place logos from the kit
            - Load the kit from a shared JSON URL
Tech stack: JavaScript, Adobe UXP, React, Spectrum Web Components
```

---

## Example 211

**Intent:**
gimp plugin to batch resize and convert photos to webp for my blog

**Spec:**
```
Type:       Plugin (GIMP Python plug-in)
Features:   - Pick an input folder and an output folder
            - Resize images to a max width keeping aspect ratio
            - Export as WebP with a quality setting
            - Strip EXIF location data
            - Show progress and a summary when done
Tech stack: Python, GIMP 3 Python API
```

---

## Example 212

**Intent:**
Godot plugin where I write enemy stats in a table and it makes resource files

**Spec:**
```
Type:       Plugin (Godot editor plugin)
Data model: EnemyStats(id, name, hp, damage, speed, drop_table)
Features:   - Show a table editor in a main screen tab
            - Add, edit and delete enemy rows
            - Save each row as an EnemyStats .tres resource
            - Import and export the table as CSV
            - Validate number ranges
Storage:    Godot resource files
Tech stack: GDScript, Godot 4 EditorPlugin API
```

---

## Example 213

**Intent:**
an extension that helps me read japanese by showing furigana over kanji

**Spec:**
```
Type:       Browser extension (Japanese reading aid)
Features:   - Find kanji in page text
            - Add furigana readings using ruby tags
            - Hide furigana for kanji the user marks as known
            - Show a dictionary popup on hover
            - Turn on per site
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, kuromoji.js
```

---

## Example 214

**Intent:**
I'm a solo developer and I use GitHub a lot. When someone opens a PR on my repos I want a browser extension notification and a badge count of PRs waiting for my review, so I don't need to check the site constantly.

**Spec:**
```
Type:       Browser extension (GitHub notifications)
Features:   - Poll for PRs where the user is a requested reviewer every 5 minutes
            - Show the count as a badge on the toolbar icon
            - Show a desktop notification for each new PR
            - List PRs in the popup with repo, title and age
            - Mark a PR as seen
API:        GitHub REST
            GET  /search/issues?q=is:pr+is:open+review-requested:{user}
Storage:    chrome.storage.local
Tech stack: TypeScript, Chrome Extension Manifest V3 (alarms, notifications)
```

---

## Example 215

**Intent:**
alfred workflow that searches my obsidian vault

**Spec:**
```
Type:       Plugin (Alfred workflow)
Features:   - Search note titles and contents with ripgrep
            - Show results with the matching line as subtitle
            - Open the note in Obsidian with an obsidian:// URL
            - Create a new note when there is no match
            - Support a quick-capture keyword to append to the daily note
Input:      Typed query in the Alfred bar
Tech stack: Python, ripgrep, Alfred Script Filter JSON
```

---

## Example 216

**Intent:**
canvas lms extension for teachers: grade essays with a rubric side panel and keyboard shortcuts

**Spec:**
```
Type:       Browser extension (Canvas SpeedGrader helper)
Features:   - Detect the Canvas SpeedGrader page
            - Show rubric criteria in a side panel with number keys to score
            - Move to the next student with a shortcut
            - Insert saved comments into the comment box
            - Show grading progress for the assignment
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 217

**Intent:**
blender script that makes a lot of trees from a few settings

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Generate trunk and branches with a recursive L-system
            - Control height, branch angle, levels and randomness
            - Add leaf particles on the branch tips
            - Generate several variations at once
            - Add a "Tree" entry to the Add menu
Tech stack: Python, Blender bpy API, bmesh
```

---

## Example 218

**Intent:**
an addon for firefox that removes tracking parameters from links when i copy them

**Spec:**
```
Type:       Browser extension (clean links)
Data model: ParamRule(name, domain_pattern)
Features:   - Remove utm_, fbclid, gclid and similar parameters from copied links
            - Clean links when the user clicks them
            - Unwrap redirect links from search engines
            - Let the user add their own parameter rules
            - Show how many parameters were removed today
Storage:    browser.storage.local
Tech stack: JavaScript, Firefox WebExtensions API (clipboardWrite, webRequest)
```

---

## Example 219

**Intent:**
stream deck plugin to control my smart lights from home assistant

**Spec:**
```
Type:       Plugin (Elgato Stream Deck)
Features:   - Add a light toggle action configured with an entity ID
            - Show the light's on/off state on the key
            - Change brightness with dial rotation on Stream Deck+
            - Trigger a scene with a second action
            - Reconnect automatically when Home Assistant restarts
API:        WebSocket
            ws://{ha_host}/api/websocket
Tech stack: TypeScript, Stream Deck SDK, home-assistant-js-websocket
```

---

## Example 220

**Intent:**
cura plugin that estimates the cost of a print from filament price and electricity

**Spec:**
```
Type:       Plugin (Ultimaker Cura)
Data model: Material(name, price_per_kg, density)
            Settings(electricity_price_kwh, printer_watts)
Features:   - Read filament weight and print time from the slice result
            - Calculate material cost from the price per kg
            - Calculate electricity cost from printer watts and time
            - Show total cost in the print panel
            - Let users set prices per material
Tech stack: Python, Cura plugin API, QML
```

---

## Example 221

**Intent:**
minecraft plugin so players can sell items in shops made from chests

**Spec:**
```
Type:       Plugin (Minecraft Paper server)
Data model: Shop(id, owner_uuid, world, x, y, z, item, price, amount, is_buy)
Features:   - Create a shop by placing a sign on a chest with item and price
            - Let players buy or sell by right-clicking the sign
            - Transfer money through the Vault economy
            - Prevent other players from opening shop chests
            - Notify owners when a shop is out of stock
Storage:    SQLite
Tech stack: Java, Paper API, Vault API
```

---

## Example 222

**Intent:**
power bi visual that is like a gantt chart for our projects

**Spec:**
```
Type:       Plugin (Power BI custom visual)
Features:   - Accept task name, start date, end date and progress fields
            - Draw tasks as bars on a time axis
            - Show progress as a filled part of each bar
            - Group tasks by a category field
            - Show a today line
Tech stack: TypeScript, Power BI Visuals API, D3.js
```

---

## Example 223

**Intent:**
jupyterlab extension to show the variables in memory and their sizes

**Spec:**
```
Type:       Plugin (JupyterLab extension)
Features:   - Show a side panel with variables in the current kernel
            - Show type, shape and memory size of each variable
            - Refresh after each cell execution
            - Delete a variable from the panel
            - Sort by size
Tech stack: TypeScript, JupyterLab extension API, Python kernel comm
```

---

## Example 224

**Intent:**
rstudio addin that formats my ggplot code and adds labels

**Spec:**
```
Type:       Plugin (RStudio addin)
Features:   - Read the selected ggplot code
            - Reformat it with one layer per line
            - Add labs() for title and axis labels when missing
            - Add a theme from a chosen preset
            - Replace the selection with the new code
Tech stack: R, rstudioapi, styler
```

---

## Example 225

**Intent:**
neovim plugin that runs the test under my cursor

**Spec:**
```
Type:       Plugin (Neovim)
Features:   - Find the test function at the cursor with Tree-sitter
            - Build the test command for pytest, Jest or go test
            - Run it in a split terminal
            - Show pass or fail signs in the gutter
            - Rerun the last test with a keymap
Tech stack: Lua, Neovim API, nvim-treesitter
```

---

## Example 226

**Intent:**
thunderbird add-on: when i get an email with a meeting time it suggests adding to calendar

**Spec:**
```
Type:       Plugin (Thunderbird add-on)
Features:   - Scan opened emails for dates and times
            - Show a bar with "Add to calendar" when a time is found
            - Prefill the event title from the email subject
            - Handle time zones written in the email
            - Add the event to the chosen calendar
Tech stack: JavaScript, Thunderbird MailExtensions API, chrono-node
```

---

## Example 227

**Intent:**
chrome extension for real estate investors that calculates rental yield on listing pages

**Spec:**
```
Type:       Browser extension (property investment)
Data model: Assumptions(down_payment_pct, interest_rate, expenses_pct, vacancy_pct)
Features:   - Read the listing price from the page
            - Estimate monthly rent from a rent API by address
            - Calculate gross yield, net yield and cash flow
            - Let the user edit assumptions in the panel
            - Save analyzed properties to a list
API:        REST
            GET  /rent-estimate?address={address}
Storage:    chrome.storage.local
Tech stack: TypeScript, Chrome Extension Manifest V3, React
```

---

## Example 228

**Intent:**
octoprint plugin that stops the print if the camera sees spaghetti

**Spec:**
```
Type:       Plugin (OctoPrint)
Data model: Detection(id, print_job, confidence, snapshot_path, detected_at)
Features:   - Grab a webcam snapshot every 30 seconds while printing
            - Run an object detection model trained on failed prints
            - Pause the print when failure confidence passes a threshold
            - Send a notification with the snapshot
            - Let the user tune sensitivity in the settings tab
Storage:    OctoPrint plugin data folder
Tech stack: Python, OctoPrint plugin API, ONNX Runtime, Jinja2
```

---

## Example 229

**Intent:**
node-red node that reads from my modbus energy meter

**Spec:**
```
Type:       Plugin (Node-RED node)
Features:   - Connect to a Modbus TCP or RTU device
            - Read voltage, current, power and energy registers
            - Scale and label register values
            - Output a JSON message at a set interval
            - Show connection status on the node
Tech stack: JavaScript, Node-RED node API, modbus-serial
```

---

## Example 230

**Intent:**
n8n community node for our internal invoicing API

**Spec:**
```
Type:       Plugin (n8n community node)
Features:   - Add operations to create, get and list invoices
            - Add an operation to mark an invoice paid
            - Add a trigger node that polls for new invoices
            - Map invoice fields to n8n item properties
            - Handle pagination for list operations
API:        REST
            GET  /invoices
            POST /invoices
            GET  /invoices/{id}
            POST /invoices/{id}/pay
Tech stack: TypeScript, n8n nodes API
```

---

## Example 231

**Intent:**
esphome custom component for a cheap chinese air quality sensor on uart

**Spec:**
```
Type:       Plugin (ESPHome external component)
Features:   - Read frames from the sensor over UART
            - Validate frame checksums
            - Publish PM1.0, PM2.5 and PM10 as sensors
            - Support a configurable update interval in YAML
            - Put the sensor to sleep between readings
Tech stack: C++, ESPHome component API, Python (config schema)
```

---

## Example 232

**Intent:**
twitch extension panel that shows my current pc specs and game settings

**Spec:**
```
Type:       Plugin (Twitch extension)
Data model: StreamerConfig(channel_id, specs_json, game_settings_json)
Features:   - Let the broadcaster enter PC specs in the config page
            - Save game settings per game
            - Show the current game's settings to viewers in a panel
            - Detect the current game from the stream category
            - Style the panel in dark and light themes
API:        Twitch Configuration Service
            PUT  /extensions/configurations
Tech stack: JavaScript, Twitch Extensions helper, React
```

---

## Example 233

**Intent:**
my brother streams on twitch and wants a bot that runs a points game where viewers bet on if he dies in the next boss fight

**Spec:**
```
Type:       Bot (Twitch chat)
Data model: Viewer(id, username, points)
            Bet(id, round_id, viewer_id -> Viewer, outcome, amount)
            Round(id, status, result)
Features:   - Give viewers points for time spent watching
            - Open a bet round with a mod command
            - Let viewers bet points on "win" or "die"
            - Pay out winners when the mod sets the result
            - Show the top 10 points leaderboard with !top
Storage:    SQLite
Tech stack: Node.js, tmi.js, Twitch Helix API
```

---

## Example 234

**Intent:**
matrix bot that translates messages in our international room

**Spec:**
```
Type:       Bot (Matrix)
Data model: RoomSettings(room_id, target_languages)
Features:   - Detect the language of each message
            - Reply in a thread with translations into the room's target languages
            - Skip messages already in a target language
            - Let room admins set languages with a !lang command
            - Support encrypted rooms
Tech stack: Python, matrix-nio, LibreTranslate API
```

---

## Example 235

**Intent:**
telegram bot for our flat to split grocery bills

**Spec:**
```
Type:       Bot (Telegram)
Data model: Group(id, chat_id)
            Expense(id, group_id -> Group, payer_id, amount, description, created_at)
            Share(expense_id -> Expense, user_id, amount)
Features:   - Add an expense with /spent 23.50 groceries
            - Split it equally among group members by default
            - Show who owes whom with /balance
            - Settle a debt with /paid
            - Export the month's expenses as CSV
Storage:    SQLite
Tech stack: Python, python-telegram-bot
```

---

## Example 236

**Intent:**
slack app that asks the team for a mood check every friday

**Spec:**
```
Type:       Bot (Slack app)
Data model: MoodResponse(id, team_id, user_id, week, score, comment)
Features:   - Send a DM every Friday with a 1-5 mood scale
            - Allow an optional anonymous comment
            - Post an aggregated weekly average to a channel
            - Show a trend chart on the App Home tab
            - Never show individual answers to managers
API:        Slack Web API
            POST /api/chat.postMessage
            POST /api/views.publish
Storage:    PostgreSQL
Tech stack: Python, Slack Bolt, APScheduler
```

---

## Example 237

**Intent:**
mattermost plugin to make a quick poll with /poll

**Spec:**
```
Type:       Plugin (Mattermost)
Data model: Poll(id, channel_id, creator_id, question, options_json, anonymous, closed)
            Vote(poll_id -> Poll, user_id, option_index)
Features:   - Create a poll with a slash command
            - Show options as buttons in the post
            - Update the vote count when users click
            - Allow anonymous polls
            - End the poll and show final results
Storage:    Mattermost KV store
Tech stack: Go (server plugin), React (webapp plugin), Mattermost plugin API
```

---

## Example 238

**Intent:**
linear integration that creates issues from our customer feedback form

**Spec:**
```
Type:       Webhook service (feedback to Linear)
Data model: Feedback(id, email, message, category, linear_issue_id, created_at)
Features:   - Receive form submissions by webhook
            - Create a Linear issue in the team for the feedback category
            - Add a "customer-feedback" label and the customer email
            - Merge feedback into an existing issue when titles match closely
            - Reply to the customer when the issue is completed
API:        REST
            POST /webhooks/feedback
            POST /webhooks/linear
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, Linear GraphQL SDK
```

---

## Example 239

**Intent:**
asana app that shows time tracked on each task from harvest

**Spec:**
```
Type:       Plugin (Asana app component)
Features:   - Show a widget on Asana tasks with tracked hours
            - Link Harvest time entries to tasks by URL
            - Start a Harvest timer from the task
            - Show hours against the task estimate
            - Sum hours for the whole project
API:        Harvest REST
            GET  /v2/time_entries?external_reference_id={task_id}
Tech stack: TypeScript, Asana App Components, Node.js, Harvest API v2
```

---

## Example 240

**Intent:**
monday.com app that sends a text message when an item status changes

**Spec:**
```
Type:       Plugin (monday.com integration)
Features:   - Add an integration recipe "When status changes to X, send SMS to Y"
            - Read the phone number from a column
            - Send the SMS through Twilio
            - Log sent messages in an item update
            - Handle failed sends with a retry
API:        REST
            POST /monday/actions/send-sms
Tech stack: Node.js, monday apps SDK, Twilio API
```

---

## Example 241

**Intent:**
todoist extension that adds tasks for each line of pasted text

**Spec:**
```
Type:       Plugin (Todoist UI extension)
Features:   - Open a dialog to paste multiple lines
            - Turn each line into a task in the chosen project
            - Parse due dates written in the line
            - Turn indented lines into subtasks
            - Show a preview before creating
API:        Todoist REST
            POST /rest/v2/tasks
Tech stack: TypeScript, Todoist UI Extensions SDK, Doist Card
```

---

## Example 242

**Intent:**
joplin plugin that makes a table of contents for long notes

**Spec:**
```
Type:       Plugin (Joplin)
Features:   - Read headings from the current note
            - Show a clickable table of contents in a side panel
            - Scroll the editor to a heading on click
            - Highlight the current section while scrolling
            - Insert a TOC block into the note with a command
Tech stack: TypeScript, Joplin Plugin API
```

---

## Example 243

**Intent:**
excalidraw for obsidian is there, but I want a plugin that makes flashcards from my excalidraw drawings by hiding labels

**Spec:**
```
Type:       Plugin (Obsidian)
Features:   - Read text elements from an Excalidraw drawing
            - Create image-occlusion cards that hide one label at a time
            - Show cards in a review modal
            - Schedule reviews with spaced repetition
            - Update cards when the drawing changes
Storage:    Obsidian plugin data.json
Tech stack: TypeScript, Obsidian API, Excalidraw plugin API
```

---

## Example 244

**Intent:**
draw.io plugin that makes a network diagram from a csv of devices

**Spec:**
```
Type:       Plugin (draw.io / diagrams.net)
Features:   - Import a CSV with device name, type, IP and connected-to columns
            - Place shapes using network icons for each type
            - Draw links between connected devices
            - Lay out the diagram automatically
            - Show IP addresses as labels
Input:      CSV file of devices
Tech stack: JavaScript, draw.io plugin API, mxGraph
```

---

## Example 245

**Intent:**
docusaurus plugin that shows an edit-this-page and 'was this helpful' vote at the bottom

**Spec:**
```
Type:       Plugin (Docusaurus)
Data model: Feedback(id, page_path, helpful, comment, created_at)
Features:   - Add a "Was this helpful?" widget at the end of each doc
            - Send votes and comments to an API
            - Show an "Edit this page" link to GitHub
            - Let site owners turn it off per page
            - Show results in a small admin page
API:        REST
            POST /feedback
            GET  /feedback/summary
Storage:    PostgreSQL
Tech stack: TypeScript, React, Docusaurus plugin API, Node.js
```

---

## Example 246

**Intent:**
sphinx extension that adds a copy button to code blocks and hides prompts

**Spec:**
```
Type:       Plugin (Sphinx extension)
Features:   - Add a copy button to each code block
            - Strip prompts like ">>> " and "$ " from copied text
            - Show a "Copied!" tooltip
            - Let projects configure prompt patterns in conf.py
            - Work with the common HTML themes
Tech stack: Python, Sphinx extension API, JavaScript
```

---

## Example 247

**Intent:**
babel plugin that removes test ids from production builds

**Spec:**
```
Type:       Plugin (Babel)
Features:   - Find JSX attributes named data-testid
            - Remove them when NODE_ENV is production
            - Let users configure extra attribute names
            - Keep attributes in test builds
            - Report how many were removed
Tech stack: JavaScript, Babel plugin API
```

---

## Example 248

**Intent:**
prettier plugin that sorts the keys in our json config files alphabetically

**Spec:**
```
Type:       Plugin (Prettier)
Features:   - Parse JSON files with the existing parser
            - Sort object keys alphabetically at every level
            - Keep a list of keys that must stay first like "name" and "version"
            - Leave arrays in their original order
            - Apply only to files matching a glob option
Tech stack: JavaScript, Prettier plugin API
```

---

## Example 249

**Intent:**
webpack plugin to upload source maps to our error tracker after build then delete them

**Spec:**
```
Type:       Plugin (webpack)
Features:   - Collect generated .map files after emit
            - Upload each source map with the release version
            - Delete source maps from the output folder
            - Skip upload in development mode
            - Fail the build on upload errors only when configured
API:        REST
            POST /api/releases/{version}/sourcemaps
Tech stack: TypeScript, webpack plugin API (compiler hooks)
```

---

## Example 250

**Intent:**
astro integration that makes open graph images for every blog post

**Spec:**
```
Type:       Plugin (Astro integration)
Features:   - Read each blog post's title, date and author at build time
            - Render a 1200x630 image from a template
            - Save images in the output folder
            - Add og:image meta tags to each page
            - Cache images for unchanged posts
Tech stack: TypeScript, Astro integration API, Satori, resvg
```

---

## Example 251

**Intent:**
nuxt module that adds cookie consent and blocks analytics until accepted

**Spec:**
```
Type:       Plugin (Nuxt module)
Data model: ConsentState(necessary, analytics, marketing, updated_at)
Features:   - Show a consent banner on first visit
            - Block configured analytics scripts until consent
            - Let visitors change choices from a settings dialog
            - Save choices in a cookie for 12 months
            - Expose a composable to check consent in components
Storage:    Browser cookie
Tech stack: TypeScript, Nuxt 3 module API, Vue 3
```

---

## Example 252

**Intent:**
strapi plugin that schedules publishing of articles

**Spec:**
```
Type:       Plugin (Strapi)
Data model: Schedule(id, content_type, entry_id, action, run_at, status)
Features:   - Add a "Schedule" button to the content edit view
            - Publish or unpublish entries at the set time
            - Run a cron task every minute to process due schedules
            - Show upcoming schedules in a plugin page
            - Cancel a schedule
Storage:    Strapi database (PostgreSQL)
Tech stack: JavaScript, Strapi 4 plugin API, React
```

---

## Example 253

**Intent:**
directus extension, a dashboard panel showing todays orders total

**Spec:**
```
Type:       Plugin (Directus panel extension)
Features:   - Query the orders collection for today
            - Show the total amount and order count
            - Compare with the same day last week
            - Let users choose the currency field and date field
            - Refresh every minute
Tech stack: Vue 3, Directus extensions SDK
```

---

## Example 254

**Intent:**
keycloak extension that only allows login from our company ip range

**Spec:**
```
Type:       Plugin (Keycloak authenticator SPI)
Features:   - Add an authenticator step to login flows
            - Check the client IP against allowed CIDR ranges
            - Deny login with a custom message outside the range
            - Let admins configure ranges per realm
            - Log denied attempts as events
Tech stack: Java, Keycloak SPI, Maven
```

---

## Example 255

**Intent:**
traefik plugin to add a maintenance page when a file exists

**Spec:**
```
Type:       Plugin (Traefik middleware)
Features:   - Check for a maintenance flag file on each request
            - Return a 503 maintenance page when the file exists
            - Let configured IPs bypass maintenance mode
            - Serve a custom HTML template
            - Set a Retry-After header
Tech stack: Go, Traefik plugin system (Yaegi)
```

---

## Example 256

**Intent:**
wireshark plugin to decode my custom game network protocol

**Spec:**
```
Type:       Plugin (Wireshark Lua dissector)
Features:   - Register a dissector on the game's UDP port
            - Parse header fields (packet type, sequence, length)
            - Decode payloads for movement, chat and state packets
            - Show fields in the packet details tree
            - Add filters like gameproto.type == 3
Tech stack: Lua, Wireshark dissector API
```

---

## Example 257

**Intent:**
ghidra script to find all strings that look like urls and api keys

**Spec:**
```
Type:       Plugin (Ghidra script)
Features:   - Scan defined strings in the program
            - Match URL, IP address and key-like patterns
            - List matches with their addresses
            - Show functions that reference each match
            - Export results to CSV
Tech stack: Java, Ghidra scripting API
```

---

## Example 258

**Intent:**
dbeaver plugin that shows a query cost warning before running on production

**Spec:**
```
Type:       Plugin (DBeaver)
Features:   - Detect connections marked as production
            - Run EXPLAIN on the query before executing
            - Warn when the estimated rows or cost exceed a limit
            - Block DELETE and UPDATE without WHERE
            - Let the user continue after confirming
Tech stack: Java, Eclipse plugin API, DBeaver SDK
```

---

## Example 259

**Intent:**
insomnia plugin that signs my requests with hmac like our api wants

**Spec:**
```
Type:       Plugin (Insomnia)
Features:   - Add a request hook that runs before each request
            - Build the canonical string from method, path, timestamp and body
            - Sign it with HMAC-SHA256 using a secret from the environment
            - Add signature and timestamp headers
            - Skip requests without the secret configured
Tech stack: JavaScript, Insomnia plugin API, Node.js crypto
```

---

## Example 260

**Intent:**
airflow provider for our company's data warehouse api

**Spec:**
```
Type:       Plugin (Apache Airflow provider)
Features:   - Add a connection type for the warehouse
            - Add a hook to run queries and fetch results
            - Add an operator that runs a SQL file
            - Add a sensor that waits for a table partition
            - Show the warehouse query ID as an extra link
Tech stack: Python, Apache Airflow provider API
```

---

## Example 261

**Intent:**
dbt package with macros that check my tables for freshness and empty columns

**Spec:**
```
Type:       Plugin (dbt package)
Features:   - Add a test that fails when a model's newest row is older than N hours
            - Add a test for columns that are fully null
            - Add a test for unexpected row count drops
            - Write results to an audit table
            - Document all macros in the package README
Tech stack: SQL, Jinja, dbt-core
```

---

## Example 262

**Intent:**
napari plugin that counts cells in my microscope images

**Spec:**
```
Type:       Plugin (napari)
Features:   - Add a widget to segment nuclei in the active image layer
            - Use a pretrained segmentation model
            - Show labels as a new layer
            - Count cells and measure their areas
            - Export measurements to CSV
Tech stack: Python, napari plugin API (npe2), Cellpose, magicgui
```

---

## Example 263

**Intent:**
imagej plugin to measure root length in plant photos

**Spec:**
```
Type:       Plugin (ImageJ/Fiji)
Features:   - Threshold the root image into a binary mask
            - Skeletonize the mask
            - Measure total and primary root length
            - Calibrate pixels to millimeters with a scale bar
            - Save results to a table for many images
Tech stack: Java, ImageJ API, Skeletonize3D
```

---

## Example 264

**Intent:**
pymol plugin that colors my protein by mutation frequency from a csv

**Spec:**
```
Type:       Plugin (PyMOL)
Features:   - Load a CSV of residue numbers and frequencies
            - Map values to a color gradient
            - Color residues of the loaded structure
            - Show a color legend
            - Label the top 10 residues
Input:      CSV file with residue numbers and frequencies
Tech stack: Python, PyMOL API, Tkinter
```

---

## Example 265

**Intent:**
arcgis pro add-in that checks parcels for overlaps

**Spec:**
```
Type:       Plugin (ArcGIS Pro add-in)
Features:   - Select a parcel polygon layer
            - Find overlapping parcel pairs
            - Create a layer of overlap areas
            - Show overlap area per pair in a table
            - Zoom to an overlap when clicked
Tech stack: C#, ArcGIS Pro SDK for .NET
```

---

## Example 266

**Intent:**
openrefine extension to geocode an address column

**Spec:**
```
Type:       Plugin (OpenRefine extension)
Features:   - Add a column menu "Geocode" for address columns
            - Send addresses to Nominatim with rate limiting
            - Add latitude and longitude columns
            - Cache results to avoid repeated calls
            - Mark rows that could not be geocoded
API:        REST
            GET  https://nominatim.openstreetmap.org/search?q={address}&format=json
Tech stack: Java, OpenRefine extension API, JavaScript
```

---

## Example 267

**Intent:**
houdini shelf tool to export my sim cache to the farm

**Spec:**
```
Type:       Plugin (Houdini Python shelf tool)
Features:   - Find File Cache nodes in the scene
            - Show them in a dialog with frame ranges
            - Submit selected nodes as jobs to the render farm
            - Set priority and chunk size
            - Show job IDs after submission
API:        REST
            POST /api/jobs
Tech stack: Python, Houdini hou API, PySide2, Deadline Web Service
```

---

## Example 268

**Intent:**
maya script that renames joints in a skeleton to the unreal naming

**Spec:**
```
Type:       Plugin (Maya Python script)
Features:   - Read the selected skeleton hierarchy
            - Match joints by position and chain to standard names
            - Rename joints with left and right suffixes
            - Show a mapping table for manual fixes
            - Save mappings as presets
Tech stack: Python, Maya cmds API, PySide2
```

---

## Example 269

**Intent:**
unreal editor tool that finds actors with too many polygons in the level

**Spec:**
```
Type:       Plugin (Unreal Engine editor utility)
Features:   - Scan static mesh actors in the current level
            - List triangle counts per actor
            - Highlight actors over a budget
            - Select the actor in the viewport on click
            - Export the list as CSV
Tech stack: Python, Unreal Engine Editor Scripting, Editor Utility Widget
```

---

## Example 270

**Intent:**
rpg maker mz plugin for a day and night cycle

**Spec:**
```
Type:       Plugin (RPG Maker MZ)
Data model: TimeState(hour, minute, day)
Features:   - Advance an in-game clock while the player walks
            - Tint the screen by time of day
            - Store the hour in a game variable for events
            - Add plugin commands to set or pause time
            - Show a small clock on the map screen
Tech stack: JavaScript, RPG Maker MZ plugin API
```

---

## Example 271

**Intent:**
renpy thing that adds a phone messenger screen to my visual novel

**Spec:**
```
Type:       Plugin (Ren'Py extension)
Data model: Message(id, contact, text, is_player, sent_at)
Features:   - Show a phone screen with a chat list
            - Add messages with a simple statement in scripts
            - Animate typing dots before replies
            - Let the player choose replies as menu options
            - Save chat history with the game
Tech stack: Ren'Py (Python), Ren'Py screen language
```

---

## Example 272

**Intent:**
stardew valley mod that shows how much each crop will sell for when i hover

**Spec:**
```
Type:       Plugin (Stardew Valley SMAPI mod)
Features:   - Detect hovering over crops and items
            - Show sell price for normal, silver, gold and iridium quality
            - Include profession bonuses in the price
            - Show days left until harvest
            - Let users toggle the overlay with a key
Tech stack: C#, SMAPI
```

---

## Example 273

**Intent:**
factorio mod that shows a list of everything running low in my logistic network

**Spec:**
```
Type:       Plugin (Factorio mod)
Features:   - Read item counts in each logistic network
            - Compare against thresholds set by the player
            - Show low items in a GUI panel
            - Play an alert when an item hits zero
            - Let players set thresholds by clicking items
Tech stack: Lua, Factorio modding API
```

---

## Example 274

**Intent:**
steam deck plugin to show battery health and how long until empty

**Spec:**
```
Type:       Plugin (Decky Loader)
Features:   - Read battery capacity, design capacity and charge rate
            - Show battery health in percent
            - Estimate time to empty from current draw
            - Show a graph of the last hour
            - Warn at a custom battery level
Tech stack: TypeScript, React, Decky Loader API, Python backend
```

---

## Example 275

**Intent:**
Good day. I am working in a library in Germany. We want plugin for Koha catalog so readers can see on map in which shelf the book is. Is possible?

**Spec:**
```
Type:       Plugin (Koha library system)
Data model: Shelf(id, label, floor, x, y, call_number_from, call_number_to)
Features:   - Map call number ranges to shelves
            - Show a floor plan with the shelf highlighted on the book detail page
            - Let librarians draw shelves on an uploaded floor plan image
            - Support several floors
            - Show the map in German and English
Storage:    Koha MariaDB database (plugin tables)
Tech stack: Perl, Koha plugin system, JavaScript, SVG
```

---

## Example 276

**Intent:**
i do online tutoring and use google meet, want a chrome extension that times how long each student talks so i make sure im not talking the whole time lol

**Spec:**
```
Type:       Browser extension (talk time tracker)
Data model: MeetingStats(meeting_id, date)
            SpeakerTime(meeting_id -> MeetingStats, participant_name, seconds)
Features:   - Detect the active speaker indicator in Google Meet
            - Add up talk time for each participant
            - Show a live bar chart of talk shares in an overlay
            - Save stats when the meeting ends
            - Show history for past lessons
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, MutationObserver
```

---

## Example 277

**Intent:**
so I'm a hobby astronomer and I use Stellarium on my laptop. I want a plugin that shows me which objects from my own observing list are above the horizon tonight and the best time to see them, because I keep missing them

**Spec:**
```
Type:       Plugin (Stellarium)
Data model: ObservingTarget(id, name, ra, dec, priority, observed)
Features:   - Import an observing list from CSV
            - Calculate rise, transit and set times for tonight at the user's location
            - Show targets above a minimum altitude sorted by best viewing time
            - Center the sky view on a target when clicked
            - Mark targets as observed with a date
Storage:    Local JSON file in the Stellarium user folder
Tech stack: C++, Stellarium plugin API, Qt
```

---

## Example 278

**Intent:**
chrome extention for amazon kdp authors to see the bsr of my books every day

**Spec:**
```
Type:       Browser extension (author sales rank tracker)
Data model: Book(asin, title, marketplace)
            RankSnapshot(asin -> Book, rank, category_ranks_json, taken_at)
Features:   - Let the author add books by ASIN
            - Fetch each book's Best Sellers Rank once a day
            - Draw a rank history chart per book
            - Notify when a book enters a top 100 category
            - Export history to CSV
Storage:    IndexedDB
Tech stack: JavaScript, Chrome Extension Manifest V3 (alarms), Chart.js
```

---

## Example 279

**Intent:**
hey can u make an obs plugin where viewers donating makes a confetti effect on the screen

**Spec:**
```
Type:       Plugin (OBS Studio browser source overlay)
Features:   - Connect to the Streamlabs donation socket
            - Trigger a confetti animation on each donation
            - Scale the confetti amount by the donation size
            - Show the donor name and message for a few seconds
            - Queue alerts so they do not overlap
Tech stack: JavaScript, canvas-confetti, Streamlabs Socket API
```

---

## Example 280

**Intent:**
Hello, I am working as accountant and we use Xero. Can you make Chrome extension which shows in Xero the exchange rate from our central bank for the invoice date? Xero rate is different and we must use official one.

**Spec:**
```
Type:       Browser extension (accounting helper)
Features:   - Detect the invoice date and currency on Xero invoice pages
            - Fetch the official central bank rate for that date
            - Show the rate next to Xero's rate with the difference
            - Copy the official rate into the rate field with a button
            - Cache rates per day
API:        REST
            GET  https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 281

**Intent:**
I keep a big list of recipes in Obsidian and I want to plan meals for the week: drag recipes into days and get a combined shopping list from their ingredient sections

**Spec:**
```
Type:       Plugin (Obsidian)
Data model: MealPlan(week_start, days_json)
            Ingredient(name, quantity, unit, recipe_path)
Features:   - Show a weekly planner view with seven day columns
            - Drag recipe notes onto days
            - Read the "Ingredients" section of each planned recipe
            - Combine and sum matching ingredients into a shopping list note
            - Group the shopping list by aisle category
Storage:    Obsidian plugin data.json, Markdown notes
Tech stack: TypeScript, Obsidian API, Svelte
```

---

## Example 282

**Intent:**
discord bot that reminds our raid team 30 min before raid and tracks who signed up

**Spec:**
```
Type:       Bot (Discord)
Data model: Raid(id, guild_id, title, starts_at, slots)
            Signup(raid_id -> Raid, user_id, role, status)
Features:   - Create a raid event with a slash command
            - Let members sign up as tank, healer or damage with buttons
            - Show the roster in an updating embed
            - Ping signed-up members 30 minutes before start
            - Move late signups to a bench list when slots are full
Storage:    PostgreSQL
Tech stack: Node.js, discord.js, node-cron
```

---

## Example 283

**Intent:**
zotero addon that summarizes the pdf with ai and puts it into a note

**Spec:**
```
Type:       Plugin (Zotero)
Features:   - Extract text from the item's PDF attachment
            - Send chunks to an LLM to build a structured summary
            - Create a child note with summary, methods and key findings
            - Let the user edit the prompt template
            - Skip items that already have a summary note
Tech stack: JavaScript, Zotero 7 plugin API, OpenAI API
```

---

## Example 284

**Intent:**
blender add-on for architects: turn a 2D floor plan image into walls

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Load a floor plan image as a reference
            - Detect wall lines with edge detection
            - Extrude detected walls to a set height and thickness
            - Let the user set the scale with two clicked points
            - Cut door and window openings from marked rectangles
Tech stack: Python, Blender bpy API, OpenCV
```

---

## Example 285

**Intent:**
home assistant integration for my aquarium controller so i can see ph and temperature

**Spec:**
```
Type:       Plugin (Home Assistant custom integration)
Features:   - Connect to the controller's local REST API
            - Create sensors for pH, temperature and conductivity
            - Create switches for lights, heater and pump outlets
            - Alert when pH leaves a safe range
            - Add a feed mode button that stops the pump for 10 minutes
API:        REST
            GET  /api/status
            POST /api/outlets/{id}
Tech stack: Python, Home Assistant integration framework, aiohttp
```

---

## Example 286

**Intent:**
grafana panel showing a calendar heat map of github commits from a json api

**Spec:**
```
Type:       Plugin (Grafana panel)
Features:   - Read time and value fields from the query result
            - Draw day cells grouped into weeks and months
            - Set colors with a threshold or gradient
            - Show day totals on hover
            - Support time zone from the dashboard
Tech stack: TypeScript, React, Grafana plugin SDK, D3.js
```

---

## Example 287

**Intent:**
raycast extension for my team's on-call: show who is on call and page them

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Show current on-call people per schedule
            - Create an alert to page someone with a message
            - List open alerts with priority
            - Acknowledge or close an alert
            - Open the alert in the browser
API:        Opsgenie REST
            GET  /v2/schedules/{id}/on-calls
            POST /v2/alerts
            POST /v2/alerts/{id}/acknowledge
Tech stack: TypeScript, React, Raycast API
```

---

## Example 288

**Intent:**
teams app for a hospital ward to swap shifts with each other

**Spec:**
```
Type:       Plugin (Microsoft Teams app)
Data model: Shift(id, ward_id, user_id, start_at, end_at, role)
            SwapRequest(id, shift_id -> Shift, requested_by, accepted_by, status)
Features:   - Show the user's upcoming shifts in a tab
            - Post a shift for swap to the ward channel as a card
            - Let colleagues with the same role accept the swap
            - Require the ward manager to approve swaps
            - Update both people's schedules after approval
API:        REST
            GET  /shifts?user={id}
            POST /swaps
            POST /swaps/{id}/accept
            POST /swaps/{id}/approve
Storage:    Azure SQL Database
Tech stack: C#, ASP.NET Core, Teams Toolkit, Adaptive Cards
```

---

## Example 289

**Intent:**
Our school uses Canvas and many kids have reading difficulties. Could there be a tool inside Canvas that reads assignment instructions aloud and lets them answer by voice?

**Spec:**
```
Type:       Plugin (Canvas LTI 1.3 tool)
Features:   - Read assignment instructions aloud with adjustable speed
            - Highlight words as they are read
            - Record a spoken answer in the browser
            - Transcribe the answer to text for the student to review
            - Submit text and audio to Canvas as the assignment submission
API:        Canvas REST
            POST /api/v1/courses/{id}/assignments/{id}/submissions
Tech stack: TypeScript, React, Node.js, ltijs, Web Speech API, Whisper API
```

---

## Example 290

**Intent:**
anki add on for medical students that links each card to the right page in my textbook pdf

**Spec:**
```
Type:       Plugin (Anki add-on)
Data model: PdfLink(note_id, pdf_path, page)
Features:   - Add a "Link PDF page" button in the editor
            - Open the linked PDF at the right page from the card back
            - Search the PDF for the card's keywords to suggest pages
            - Store links in a hidden note field
            - Show a list of cards linked to each page
Tech stack: Python, Anki add-on API, PyMuPDF
```

---

## Example 291

**Intent:**
i want jira to post in our slack channel every morning which tickets are blocked

**Spec:**
```
Type:       Scheduled script (Jira blocked tickets digest)
Features:   - Run every weekday at 9am
            - Query Jira for issues with status Blocked or the "blocked" flag
            - Group issues by assignee
            - Post a formatted message to a Slack channel
            - Skip posting when nothing is blocked
API:        Jira REST
            GET  /rest/api/3/search?jql={jql}
Tech stack: Python, requests, Slack Web API, cron
```

---

## Example 292

**Intent:**
Trello power-up that adds a 'waiting on client' timer to cards

**Spec:**
```
Type:       Plugin (Trello Power-Up)
Data model: WaitState(card_id, started_at, total_wait_seconds)
Features:   - Add a button to start and stop waiting time on a card
            - Show a badge with days waiting
            - Sum total waiting time across all waits
            - Color the badge red after 5 days
            - Show a board report of cards waiting the longest
Storage:    Trello pluginData
Tech stack: JavaScript, Trello Power-Up client library
```

---

## Example 293

**Intent:**
firefox extention that shows which cookies a site set and deletes them when i close the tab

**Spec:**
```
Type:       Browser extension (cookie cleanup)
Data model: Whitelist(domain)
Features:   - List cookies set by the current site in the popup
            - Delete a site's cookies when its last tab closes
            - Keep cookies for whitelisted domains
            - Show a count of cookies removed today
            - Remove local storage and IndexedDB data too
Storage:    browser.storage.local
Tech stack: JavaScript, Firefox WebExtensions API (cookies, browsingData, tabs)
```

---

## Example 294

**Intent:**
Chrome extension that helps recruiters: when on a github profile, sum up the languages and show recent activity and email if public

**Spec:**
```
Type:       Browser extension (technical recruiting)
Features:   - Detect GitHub user profile pages
            - Sum languages across the user's public repositories
            - Show contributions in the last 90 days
            - Show the public email from recent commits if available
            - Save the profile to a candidate list
API:        GitHub REST
            GET  /users/{user}/repos
            GET  /users/{user}/events/public
Storage:    chrome.storage.local
Tech stack: TypeScript, Chrome Extension Manifest V3
```

---

## Example 295

**Intent:**
a extension to put a timer on every tab so i see how long i been on a page

**Spec:**
```
Type:       Browser extension (tab timer)
Features:   - Track active time per tab
            - Show the time on the toolbar badge
            - Show total time per site today in the popup
            - Pause counting when the window is unfocused
            - Reset daily at midnight
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 296

**Intent:**
photoshop plugin to swap the text in a template from a spreadsheet and save a jpg for each row, for our event badges

**Spec:**
```
Type:       Plugin (Photoshop UXP)
Features:   - Load a CSV with one row per badge
            - Map CSV columns to named text layers
            - Replace a photo layer from an image path column
            - Export a JPG for each row named after a chosen column
            - Show progress and skip rows with errors
Input:      CSV file and a PSD template with named layers
Tech stack: JavaScript, Adobe UXP, Photoshop batchPlay API
```

---

## Example 297

**Intent:**
unity editor tool to make sure every prefab has the correct layer and tag

**Spec:**
```
Type:       Plugin (Unity editor extension)
Data model: PrefabRule(folder, required_layer, required_tag, required_components)
Features:   - Define rules per folder in a ScriptableObject
            - Check all prefabs against the rules
            - List violations in a window
            - Fix layer and tag with one button
            - Run the check before builds with IPreprocessBuildWithReport
Tech stack: C#, Unity Editor API
```

---

## Example 298

**Intent:**
godot plugin to take screenshots of all my scenes for a catalog

**Spec:**
```
Type:       Plugin (Godot editor plugin)
Features:   - Open each scene from a chosen folder
            - Render it from its camera into a viewport texture
            - Save a PNG thumbnail per scene
            - Build an HTML gallery page of thumbnails
            - Skip scenes without a camera
Tech stack: GDScript, Godot 4 EditorPlugin API
```

---

## Example 299

**Intent:**
i want my LinkedIn posts saved to a spreadsheet with likes and comments so i can see which ones work, chrome extension

**Spec:**
```
Type:       Browser extension (social analytics)
Data model: PostStat(post_url, posted_at, text_preview, reactions, comments, reposts, captured_at)
Features:   - Read the user's posts from their activity page
            - Capture reactions, comments and reposts for each post
            - Append or update rows in a Google Sheet
            - Mark the best performing posts
            - Run a capture on a button click
API:        Google Sheets REST
            POST /v4/spreadsheets/{id}/values/{range}:append
Tech stack: JavaScript, Chrome Extension Manifest V3, Google Sheets API
```

---

## Example 300

**Intent:**
moodle report showing which students did not watch the lecture videos fully

**Spec:**
```
Type:       Plugin (Moodle report plugin)
Data model: VideoProgress(id, user_id, cm_id, seconds_watched, duration, last_position, updated_at)
Features:   - Track video playback progress for course videos
            - Show a table of students and percent watched per video
            - Highlight students under 50%
            - Filter by group
            - Export the report to Excel
Storage:    Moodle database
Tech stack: PHP, Moodle Report API, JavaScript (Video.js events)
```

---

## Example 301

**Intent:**
alfred workflow to open my projects in vscode by fuzzy search

**Spec:**
```
Type:       Plugin (Alfred workflow)
Features:   - Scan configured folders for Git repositories
            - Fuzzy match the typed text against project names
            - Open the chosen project in VS Code
            - Open in terminal with a modifier key
            - Rank recently opened projects higher
Input:      Typed query in the Alfred bar
Storage:    Local JSON cache
Tech stack: Go, Alfred Script Filter JSON
```

---

## Example 302

**Intent:**
zoom app that shows live captions translated to spanish for my parents

**Spec:**
```
Type:       Plugin (Zoom App)
Features:   - Read the meeting's live transcript through the Zoom Apps SDK
            - Translate each caption line to the chosen language
            - Show translated captions in a large font in the app panel
            - Let each participant pick their own language
            - Save the translated transcript after the meeting
Tech stack: TypeScript, Zoom Apps SDK, React, Google Cloud Translation API
```

---

## Example 303

**Intent:**
confluence plugin that shows page reading time and who has read it

**Spec:**
```
Type:       Plugin (Confluence Cloud app)
Data model: PageRead(page_id, account_id, read_at)
Features:   - Show estimated reading time at the top of pages
            - Record when a user scrolls to the end of a page
            - Show the page owner a list of readers
            - Let owners request read confirmation from a group
            - Remind people who have not read the page
API:        Confluence REST
            GET  /wiki/api/v2/pages/{id}
Storage:    Forge storage API
Tech stack: Atlassian Forge, TypeScript, React
```

---

## Example 304

**Intent:**
i run an online thrift store on depop and grailed, want chrome thing where i fill the listing once and it cross posts to both

**Spec:**
```
Type:       Browser extension (cross-listing tool)
Data model: Item(id, title, description, price, size, brand, condition, photos)
            Listing(item_id -> Item, platform, external_id, status)
Features:   - Save an item once with photos and details
            - Fill the listing form on each platform automatically
            - Map size and condition values to each platform's options
            - Track where each item is listed
            - Remind the seller to delist on the other platform after a sale
Storage:    IndexedDB
Tech stack: TypeScript, Chrome Extension Manifest V3, React
```

---

## Example 305

**Intent:**
chrome extension for students that makes a quizlet set from the vocab table on a page

**Spec:**
```
Type:       Browser extension (study set builder)
Features:   - Detect two-column tables on the page
            - Let the student pick term and definition columns
            - Preview the cards
            - Export as tab-separated text for Quizlet import
            - Export as an Anki .apkg deck
Tech stack: JavaScript, Chrome Extension Manifest V3, genanki-js
```

---

## Example 306

**Intent:**
a extension for people with color blindness that changes the colors on charts so i can tell them apart

**Spec:**
```
Type:       Browser extension (color vision accessibility)
Data model: Settings(cvd_type, strength, enabled_sites)
Features:   - Apply an SVG color filter tuned to the chosen color vision type
            - Let the user pick protanopia, deuteranopia or tritanopia
            - Add patterns to chart areas in SVG and canvas charts where possible
            - Show the color name under the cursor with a hotkey
            - Turn on per site
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3, SVG filters
```

---

## Example 307

**Intent:**
we need a jetbrains plugin for our internal design system: autocomplete component names and props

**Spec:**
```
Type:       Plugin (IntelliJ Platform)
Features:   - Load component metadata from the design system's JSON manifest
            - Autocomplete component tags in JSX and TSX
            - Autocomplete props with types and allowed values
            - Show prop documentation in quick docs
            - Warn about deprecated components
Tech stack: Kotlin, IntelliJ Platform SDK, JavaScript PSI
```

---

## Example 308

**Intent:**
obs plugin that saves a highlight when i say "clip that"

**Spec:**
```
Type:       Plugin (OBS Studio)
Features:   - Listen to the microphone with offline speech recognition
            - Detect the phrase "clip that"
            - Save the replay buffer when detected
            - Add a marker file with the timestamp
            - Show a small on-screen confirmation
Tech stack: C++, OBS Studio plugin API, Vosk
```

---

## Example 309

**Intent:**
logseq plugin to sync my tasks with todoist both ways

**Spec:**
```
Type:       Plugin (Logseq)
Data model: TaskLink(block_uuid, todoist_task_id, last_synced_at)
Features:   - Push TODO blocks with a #todoist tag to Todoist
            - Pull Todoist tasks into today's journal
            - Mark tasks done in both places
            - Sync due dates
            - Resolve conflicts by latest change
API:        Todoist REST
            GET  /rest/v2/tasks
            POST /rest/v2/tasks
            POST /rest/v2/tasks/{id}/close
Tech stack: TypeScript, Logseq Plugin SDK, Todoist REST API
```

---

## Example 310

**Intent:**
discord activity, a chill farming game where everyone in the call shares one farm

**Spec:**
```
Type:       Plugin (Discord activity game)
Data model: Farm(id, guild_id, day, coins)
            Plot(id, farm_id -> Farm, x, y, crop, planted_day, watered)
Features:   - Show a shared tile farm for everyone in the voice channel
            - Let players plant, water and harvest crops
            - Grow crops in real time across sessions
            - Sell harvests for shared coins to buy new seeds
            - Show each player's avatar walking on the farm
API:        WebSocket
            /ws/farm/{guild_id}
Storage:    PostgreSQL
Tech stack: TypeScript, Discord Embedded App SDK, Phaser, Colyseus
```

---

## Example 311

**Intent:**
blender addon that bakes all my textures for a game export in one click

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Create image textures for base color, normal, roughness and AO
            - Bake each map for the selected objects
            - Pack baked images into the .blend or save as PNG
            - Build a simple material using the baked maps
            - Let users set resolution and margin
Tech stack: Python, Blender bpy API (Cycles bake)
```

---

## Example 312

**Intent:**
browser extension that shows nutrition info when i hover over food on grocery websites

**Spec:**
```
Type:       Browser extension (nutrition lookup)
Features:   - Detect product names on supported grocery sites
            - Look up nutrition data on Open Food Facts
            - Show calories, sugar, salt and Nutri-Score in a tooltip
            - Highlight products that contain chosen allergens
            - Cache lookups
API:        REST
            GET  https://world.openfoodfacts.org/cgi/search.pl?search_terms={q}&json=1
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, Open Food Facts API
```

---

## Example 313

**Intent:**
I'm doing a PhD in history and I spend days in online archives reading scanned letters. I want a Firefox add-on to transcribe a letter next to the scan and tag people and places, then export everything together.

**Spec:**
```
Type:       Browser extension (archive transcription)
Data model: Document(id, archive_url, image_url, title)
            Transcription(id, document_id -> Document, text, updated_at)
            Tag(id, document_id -> Document, kind, name, span_start, span_end)
Features:   - Open a transcription panel beside the scanned image
            - Save transcriptions per archive page
            - Tag people, places and dates in the text
            - List all tagged entities across documents
            - Export documents with tags as TEI XML or CSV
Storage:    IndexedDB
Tech stack: JavaScript, Firefox WebExtensions API, Dexie.js
```

---

## Example 314

**Intent:**
something for my dad, he has parkinsons and his hands shake. browser extension that stops accidental double clicks

**Spec:**
```
Type:       Browser extension (motor accessibility)
Data model: Settings(min_click_interval_ms, enlarge_targets)
Features:   - Ignore repeated clicks within a set time window
            - Make small links and buttons easier to hit by enlarging their click area
            - Ask for confirmation before submitting forms
            - Add a large undo-close-tab button
            - Let a helper adjust settings
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 315

**Intent:**
unity package that shows debug info on screen in builds, fps memory and custom values

**Spec:**
```
Type:       Plugin (Unity package)
Features:   - Show FPS, frame time and memory in an overlay
            - Let scripts add custom values with a simple API
            - Toggle the overlay with a key or three-finger tap
            - Show a frame time graph
            - Strip the overlay from release builds
Tech stack: C#, Unity UI Toolkit, Unity Package Manager
```

---

## Example 316

**Intent:**
i want the zotero to tell me duplicated papers smarter, with similar titles not exact

**Spec:**
```
Type:       Plugin (Zotero)
Features:   - Compare titles with fuzzy matching and normalized DOIs
            - Group likely duplicates with a similarity score
            - Show groups in a review window
            - Merge items with one click keeping attachments
            - Mark pairs as "not duplicate" to ignore them
Storage:    Zotero preferences (ignored pairs)
Tech stack: JavaScript, Zotero 7 plugin API, fuse.js
```

---

## Example 317

**Intent:**
gimp plug-in that turns a photo into pixel art with a limited palette

**Spec:**
```
Type:       Plugin (GIMP Python plug-in)
Features:   - Downscale the image to a chosen pixel size
            - Reduce colors to a chosen palette (GameBoy, PICO-8 or custom)
            - Apply optional ordered dithering
            - Upscale with nearest neighbour for preview
            - Export the palette as a .gpl file
Tech stack: Python, GIMP 3 Python API, Pillow
```

---

## Example 318

**Intent:**
Hi I sell on Amazon from Turkey, I need chrome extension which shows on product page how many sellers and the buy box price history, simple please

**Spec:**
```
Type:       Browser extension (marketplace seller research)
Data model: PriceSnapshot(asin, buy_box_price, seller_count, taken_at)
Features:   - Show seller count on product pages
            - Record the buy box price each time the page is visited
            - Show a small price history chart
            - Show estimated Amazon fees for the price
            - Support Amazon.com.tr and Amazon.com
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, Chart.js
```

---

## Example 319

**Intent:**
home assistant thing to tell me when my kid's school bus is close, using the bus company tracker website

**Spec:**
```
Type:       Plugin (Home Assistant custom integration)
Features:   - Read the bus position from the tracker website every minute on school days
            - Calculate the distance to the home stop
            - Create a sensor with estimated minutes away
            - Send a phone notification when the bus is 5 minutes away
            - Only run during set morning and afternoon windows
Tech stack: Python, Home Assistant integration framework, aiohttp, geopy
```

---

## Example 320

**Intent:**
teams bot that creates a ticket in servicenow from a chat message

**Spec:**
```
Type:       Bot (Microsoft Teams)
Features:   - Add a message action "Create incident"
            - Prefill short description from the message text
            - Ask for category and urgency in an Adaptive Card
            - Create the incident in ServiceNow
            - Reply with the incident number and link
API:        ServiceNow REST
            POST /api/now/table/incident
Tech stack: TypeScript, Teams Toolkit, Bot Framework SDK
```

---

## Example 321

**Intent:**
need chrome ext 4 my etsy shop that shows which listings r about to expire

**Spec:**
```
Type:       Browser extension (Etsy shop helper)
Features:   - Fetch active listings with their expiry dates
            - List listings expiring in the next 14 days
            - Show a badge count on the toolbar icon
            - Open the renew page for a listing
            - Notify once a day about expiring listings
API:        Etsy Open API v3
            GET  /v3/application/shops/{shop_id}/listings/active
Tech stack: JavaScript, Chrome Extension Manifest V3 (alarms), Etsy Open API v3
```

---

## Example 322

**Intent:**
jira addon that lets customers vote on feature requests in the service portal

**Spec:**
```
Type:       Plugin (Jira Service Management app)
Data model: Vote(issue_key, customer_account_id, created_at)
Features:   - Show an upvote button on feature request issues in the portal
            - Count one vote per customer
            - Show vote counts on a public request list
            - Sort the internal backlog by votes
            - Notify voters when the request is released
Storage:    Forge storage API
Tech stack: Atlassian Forge, TypeScript, React (Custom UI)
```

---

## Example 323

**Intent:**
obsidian plugin that hides my private notes when i share my screen

**Spec:**
```
Type:       Plugin (Obsidian)
Data model: Settings(private_tags, private_folders, blur_enabled)
Features:   - Mark notes as private with a tag or folder
            - Blur private note contents and titles with a toggle command
            - Hide private notes from the file explorer while in presentation mode
            - Show a status bar indicator when privacy mode is on
            - Turn privacy mode on with a hotkey
Tech stack: TypeScript, Obsidian API
```

---

## Example 324

**Intent:**
kodi addon that plays my local radio stations with their logos

**Spec:**
```
Type:       Plugin (Kodi audio add-on)
Data model: Station(id, name, stream_url, logo_url, country)
Features:   - Browse stations by country from the Radio Browser API
            - Play streams in Kodi's audio player
            - Show station logos and now-playing titles
            - Save favourite stations
            - Search stations by name
API:        REST
            GET  https://de1.api.radio-browser.info/json/stations/bycountry/{country}
Tech stack: Python, Kodi add-on API
```

---

## Example 325

**Intent:**
i write fan fiction on ao3 and want a browser extension that keeps word count stats for all my works over time

**Spec:**
```
Type:       Browser extension (writer stats)
Data model: Work(id, title, url)
            StatSnapshot(work_id -> Work, words, hits, kudos, comments, taken_at)
Features:   - Read stats for all works from the user's stats page
            - Save a snapshot once a day
            - Show charts of hits and kudos over time per work
            - Show which chapters got the most comments
            - Export history to CSV
Storage:    IndexedDB
Tech stack: JavaScript, Chrome Extension Manifest V3, Chart.js
```

---

## Example 326

**Intent:**
blender add on so i can import my drone photogrammetry points and make terrain

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Import point clouds from PLY or LAS files
            - Downsample points to a target count
            - Build a terrain mesh with Delaunay triangulation
            - Apply vertex colors from the point cloud
            - Set real-world scale from the file units
Input:      PLY or LAS point cloud file
Tech stack: Python, Blender bpy API, laspy, SciPy
```

---

## Example 327

**Intent:**
Raycast command to see my AWS bill this month and per service

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Show month-to-date cost and forecast
            - List costs per service sorted by amount
            - Compare with last month
            - Show a daily cost sparkline
            - Open the AWS Cost Explorer page
API:        AWS Cost Explorer
            GetCostAndUsage
            GetCostForecast
Tech stack: TypeScript, React, Raycast API, AWS SDK for JavaScript v3
```

---

## Example 328

**Intent:**
grafana plugin which shows logs from our app in a timeline with color by level

**Spec:**
```
Type:       Plugin (Grafana panel)
Features:   - Read log lines with time, level and message fields
            - Draw events on a horizontal timeline colored by level
            - Zoom the timeline with the dashboard time picker
            - Show the full message on click
            - Filter levels with toggle buttons
Tech stack: TypeScript, React, Grafana plugin SDK
```

---

## Example 329

**Intent:**
minecraft plugin that gives daily login rewards with a streak

**Spec:**
```
Type:       Plugin (Minecraft Paper server)
Data model: PlayerStreak(uuid, last_claim_date, streak_days)
Features:   - Open a reward GUI with /daily
            - Give rewards defined per streak day in a config file
            - Reset the streak after a missed day
            - Remind players on join if they have not claimed
            - Show the top streaks with /daily top
Storage:    SQLite
Tech stack: Java, Paper API, Gradle
```

---

## Example 330

**Intent:**
anki plugin which makes the review screen dark and less straining at night only

**Spec:**
```
Type:       Plugin (Anki add-on)
Features:   - Switch the reviewer to a dark theme between set hours
            - Lower brightness of images on cards
            - Use a warm text color
            - Keep the main window theme unchanged
            - Let users set hours in the add-on config
Tech stack: Python, Anki add-on API, CSS
```

---

## Example 331

**Intent:**
I volunteer for a food bank and we track donations in Airtable. can there be a button in Airtable that prints a receipt PDF for the donor?

**Spec:**
```
Type:       Plugin (Airtable extension)
Features:   - Add a button field action that opens the extension for a record
            - Fill a receipt template with donor name, items, weight and date
            - Generate a PDF receipt
            - Email the PDF to the donor's address
            - Mark the record as "receipt sent"
API:        REST
            POST /api/receipts/email
Tech stack: JavaScript, React, Airtable Blocks SDK, pdf-lib, SendGrid
```

---

## Example 332

**Intent:**
unity tool that turns my sprite sheet into animation clips by row

**Spec:**
```
Type:       Plugin (Unity editor extension)
Features:   - Slice a texture into a grid of sprites
            - Treat each row as an animation
            - Create AnimationClips with a set frame rate
            - Name clips from a list the user types
            - Build an Animator Controller with the clips as states
Tech stack: C#, Unity Editor API (AssetDatabase, AnimationUtility)
```

---

## Example 333

**Intent:**
chrome extension for medical students that defines medical terms on hover

**Spec:**
```
Type:       Browser extension (medical dictionary)
Features:   - Detect medical terms on pages from a term list
            - Underline detected terms lightly
            - Show a short definition and pronunciation on hover
            - Save unknown terms to a review list
            - Turn highlighting on or off per site
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, MeSH vocabulary data
```

---

## Example 334

**Intent:**
zoom app for running a standup that times each person

**Spec:**
```
Type:       Plugin (Zoom App)
Features:   - Load the meeting participants into a speaking order
            - Shuffle the order on request
            - Show a 2-minute timer for the current speaker
            - Move to the next speaker with one click
            - Post notes taken during the standup to Slack
API:        Slack Web API
            POST /api/chat.postMessage
Tech stack: TypeScript, Zoom Apps SDK, React
```

---

## Example 335

**Intent:**
firefox addon that shows page load time and size in the toolbar

**Spec:**
```
Type:       Browser extension (performance)
Features:   - Read navigation timing for each page
            - Show load time on the toolbar badge
            - Show transferred size and request count in the popup
            - Color the badge by speed
            - Keep stats for the last 50 pages
Tech stack: JavaScript, Firefox WebExtensions API, Performance API
```

---

## Example 336

**Intent:**
chrome extension to save tweets with images into notion

**Spec:**
```
Type:       Browser extension (social bookmarking)
Features:   - Add a "Save to Notion" button on posts
            - Send the post text, author, date and link to a Notion database
            - Upload attached images to the page
            - Let the user add tags before saving
            - Pick the target database in options
API:        Notion REST
            POST /v1/pages
Tech stack: TypeScript, Chrome Extension Manifest V3, Notion API
```

---

## Example 337

**Intent:**
discord bot for a language exchange server: pairs people learning each others languages

**Spec:**
```
Type:       Bot (Discord)
Data model: Member(user_id, native_languages, learning_languages, timezone, level)
            Match(id, user_a, user_b, created_at, active)
Features:   - Let members register languages with a slash command
            - Match members whose native and learning languages swap
            - Prefer partners in nearby time zones
            - Create a private thread for each new pair
            - Let members ask for a new match
Storage:    PostgreSQL
Tech stack: Python, discord.py, asyncpg
```

---

## Example 338

**Intent:**
teams tab for a law firm to record billable hours per client from inside teams

**Spec:**
```
Type:       Plugin (Microsoft Teams tab)
Data model: Client(id, name)
            Matter(id, client_id -> Client, name)
            TimeEntry(id, matter_id -> Matter, user_id, minutes, description, date)
Features:   - Log time with matter, minutes and description
            - Start a timer from the tab
            - Show the user's entries for the week
            - Show totals per matter for partners
            - Export entries for invoicing as CSV
API:        REST
            GET  /time-entries?week={date}
            POST /time-entries
            GET  /matters
Storage:    Azure SQL Database
Tech stack: TypeScript, Teams Toolkit, React, Fluent UI, ASP.NET Core
```

---

## Example 339

**Intent:**
home assistant integration that reads my water meter with a camera and ocr

**Spec:**
```
Type:       Plugin (Home Assistant custom integration)
Features:   - Take a snapshot from a camera entity on a schedule
            - Crop the meter digits region
            - Read digits with a small OCR model
            - Reject readings lower than the last reading
            - Expose a water usage sensor in the Energy dashboard
Tech stack: Python, Home Assistant integration framework, OpenCV, Tesseract
```

---

## Example 340

**Intent:**
i do weddings and want a lightroom plugin that culls blurry photos and closed eyes automatically

**Spec:**
```
Type:       Plugin (Lightroom Classic)
Features:   - Analyze selected photos for sharpness with a Laplacian score
            - Detect closed eyes with a face landmark model
            - Set a reject flag or a color label on bad photos
            - Show a summary of how many photos were flagged
            - Let the user set sharpness thresholds
Tech stack: Lua, Lightroom Classic SDK, Python helper (OpenCV, MediaPipe)
```

---

## Example 341

**Intent:**
moodle plugin for language teachers to record pronunciation homework

**Spec:**
```
Type:       Plugin (Moodle assignment submission plugin)
Features:   - Add an audio recorder to assignment submissions
            - Limit recording length
            - Let teachers listen and add timed audio comments
            - Show the reference audio next to the student recording
            - Store recordings in the Moodle file system
Storage:    Moodle file API
Tech stack: PHP, Moodle Assignment Submission API, JavaScript (MediaRecorder)
```

---

## Example 342

**Intent:**
godot plugin that shows a list of all signals in the scene and what they connect to

**Spec:**
```
Type:       Plugin (Godot editor plugin)
Features:   - Walk the edited scene tree
            - List each node's connected signals and target methods
            - Show the list in a bottom panel
            - Jump to the target script method on click
            - Flag connections to methods that no longer exist
Tech stack: GDScript, Godot 4 EditorPlugin API
```

---

## Example 343

**Intent:**
obs studio plugin to make my webcam background blurry without green screen

**Spec:**
```
Type:       Plugin (OBS Studio filter)
Features:   - Add a "Background Blur" filter for video sources
            - Segment the person with a selfie segmentation model
            - Blur everything outside the mask
            - Let the user set blur strength and mask smoothing
            - Use the GPU when available
Tech stack: C++, OBS Studio plugin API, ONNX Runtime, MediaPipe Selfie Segmentation model
```

---

## Example 344

**Intent:**
Our board game cafe uses Discord for bookings. I'd like an activity where people can pick a table on a floor plan and book a time slot without leaving Discord.

**Spec:**
```
Type:       Plugin (Discord activity)
Data model: CafeTable(id, label, seats, x, y)
            Reservation(id, table_id -> CafeTable, discord_user_id, starts_at, ends_at, party_size)
Features:   - Show the cafe floor plan with free and taken tables
            - Pick a date, time and party size
            - Book a table and get a confirmation DM
            - Cancel a reservation
            - Let staff see all reservations for the day
API:        REST
            GET  /tables/availability?date={date}
            POST /reservations
            DELETE /reservations/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, Discord Embedded App SDK, React, Node.js, Express
```

---

## Example 345

**Intent:**
jetbrains plugin that shows the sql explain plan as a tree when i hover a query string

**Spec:**
```
Type:       Plugin (IntelliJ Platform)
Features:   - Detect SQL strings in Java and Kotlin code
            - Run EXPLAIN against the configured data source
            - Show the plan as a tree in a popup
            - Highlight full table scans
            - Cache plans until the query text changes
Tech stack: Kotlin, IntelliJ Platform SDK, Database Tools API
```

---

## Example 346

**Intent:**
chrome extension for property managers that pulls tenant applications from zillow rentals into a checklist

**Spec:**
```
Type:       Browser extension (rental applications)
Data model: Applicant(id, name, email, income, move_in_date, listing_url)
            ChecklistItem(applicant_id -> Applicant, item, done)
Features:   - Capture applicant details from the rental applications page
            - Create a screening checklist for each applicant (ID, income, references)
            - Calculate income-to-rent ratio
            - Sort applicants by move-in date
            - Export a summary PDF per applicant
Storage:    IndexedDB
Tech stack: JavaScript, Chrome Extension Manifest V3, jsPDF
```

---

## Example 347

**Intent:**
neovim plugin that shows a word count and reading time for markdown files in the statusline

**Spec:**
```
Type:       Plugin (Neovim)
Features:   - Count words in the current Markdown buffer
            - Ignore code blocks and front matter
            - Show words and reading time in the statusline
            - Count only the visual selection when in visual mode
            - Update on text change with a debounce
Tech stack: Lua, Neovim API, lualine component
```

---

## Example 348

**Intent:**
vlc extension to skip ads in my recorded tv shows using a list of times

**Spec:**
```
Type:       Plugin (VLC Lua extension)
Data model: SkipSegment(file_name, start_seconds, end_seconds)
Features:   - Load skip segments from a file next to the video
            - Jump over a segment when playback enters it
            - Mark a new segment with two key presses
            - Save segments for the file
            - Show a short "skipped" message
Tech stack: Lua, VLC extension API
```

---

## Example 349

**Intent:**
calibre plugin that sends book progress to a goodreads like site

**Spec:**
```
Type:       Plugin (Calibre)
Features:   - Read reading progress from a custom column
            - Find the book on the site by ISBN
            - Update the reading status and percent
            - Mark the book finished when progress hits 100%
            - Log sync results
API:        REST
            GET  /api/books?isbn={isbn}
            PUT  /api/user/books/{id}/progress
Tech stack: Python, Calibre plugin API
```

---

## Example 350

**Intent:**
cura plugin to warn me if the model is too big for my bed or has overhangs over 60 degrees

**Spec:**
```
Type:       Plugin (Ultimaker Cura)
Features:   - Check the model bounding box against the printer build volume
            - Calculate face angles to find overhangs above a set angle
            - Show a warning message with the overhang area
            - Highlight overhang faces in the preview
            - Suggest enabling supports
Tech stack: Python, Cura plugin API, NumPy
```

---

## Example 351

**Intent:**
a chrome extension that turns any webpage into a printable worksheet for my ESL students, with a word bank

**Spec:**
```
Type:       Browser extension (ESL worksheet maker)
Features:   - Extract the main article text
            - Let the teacher click words to blank out
            - Build a word bank from the removed words
            - Add comprehension question lines at the end
            - Print or save as PDF
Tech stack: JavaScript, Chrome Extension Manifest V3, Mozilla Readability
```

---

## Example 352

**Intent:**
browser extension for journalists that pulls whois, dns and hosting info for the site i'm on

**Spec:**
```
Type:       Browser extension (OSINT site info)
Features:   - Show the domain's registration date and registrar from RDAP
            - Show DNS records and hosting provider
            - Show the site's IP and country
            - Show the first Wayback Machine capture date
            - Copy a summary for research notes
API:        REST
            GET  https://rdap.org/domain/{domain}
            GET  https://dns.google/resolve?name={domain}&type=A
            GET  https://archive.org/wayback/available?url={domain}&timestamp=19900101
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 353

**Intent:**
i need a plugin for logseq that shows a progress bar for a project page by its tasks

**Spec:**
```
Type:       Plugin (Logseq)
Features:   - Count TODO and DONE blocks on a page and its references
            - Render a progress bar macro {{renderer :progress}}
            - Update when tasks change
            - Show progress per child block when nested
            - Color the bar by percent
Tech stack: JavaScript, Logseq Plugin SDK
```

---

## Example 354

**Intent:**
thunderbird addon that encrypts attachments with a password before sending

**Spec:**
```
Type:       Plugin (Thunderbird add-on)
Features:   - Add a "Protect attachments" toggle in the compose window
            - Pack attachments into an AES-256 encrypted ZIP
            - Generate a random password
            - Copy the password to the clipboard to send separately
            - Remove the original attachments from the message
Tech stack: JavaScript, Thunderbird MailExtensions API, zip.js
```

---

## Example 355

**Intent:**
confluence macro that renders our openapi spec nicely

**Spec:**
```
Type:       Plugin (Confluence Cloud macro)
Features:   - Let the user paste or link an OpenAPI 3 file
            - Render endpoints grouped by tag with request and response schemas
            - Show example requests in curl
            - Fold and unfold endpoint sections
            - Warn when the spec is invalid
Tech stack: Atlassian Forge, TypeScript, React, Redoc
```

---

## Example 356

**Intent:**
trello power-up that makes a new card every monday for weekly chores

**Spec:**
```
Type:       Plugin (Trello Power-Up)
Data model: RecurringCard(id, board_id, list_id, title, checklist_json, rule, next_run_at)
Features:   - Set a card to repeat daily, weekly or monthly
            - Create a copy in a chosen list on schedule
            - Copy checklists and labels
            - Show a repeat icon on recurring cards
            - Pause or delete a recurrence
API:        Trello REST
            POST /1/cards
Storage:    PostgreSQL
Tech stack: JavaScript, Trello Power-Up client library, Node.js, node-cron
```

---

## Example 357

**Intent:**
photoshop plugin to check text layers for spelling in german and english

**Spec:**
```
Type:       Plugin (Photoshop UXP)
Features:   - Collect text from all text layers
            - Spell-check in German and English
            - List mistakes with the layer name
            - Select the layer when a mistake is clicked
            - Replace the word with a suggestion
Tech stack: JavaScript, Adobe UXP, nspell, Hunspell dictionaries
```

---

## Example 358

**Intent:**
gimp plug-in that makes a contact sheet of a folder of photos with filenames

**Spec:**
```
Type:       Plugin (GIMP Python plug-in)
Features:   - Load every image from a folder
            - Scale images into a grid of thumbnails
            - Write each filename under its thumbnail
            - Choose page size and columns
            - Export one or more contact sheet pages as PDF
Tech stack: Python, GIMP 3 Python API
```

---

## Example 359

**Intent:**
grafana alerting contact point plugin to send alerts to our sms gateway

**Spec:**
```
Type:       Webhook service (Grafana alerts to SMS)
Features:   - Receive Grafana alert webhooks
            - Format a short SMS with alert name, status and value
            - Send SMS to on-call numbers through the gateway
            - Limit repeat messages for the same alert
            - Send a "resolved" SMS
API:        REST
            POST /grafana/alerts
Tech stack: Go, net/http, SMS gateway REST API
```

---

## Example 360

**Intent:**
i would like a chrome extension for my Arabic learning, it shows the harakat (vowel marks) on arabic text on pages

**Spec:**
```
Type:       Browser extension (Arabic reading aid)
Features:   - Detect Arabic text on the page
            - Add diacritics with a vocalization model
            - Toggle between original and vocalized text
            - Show transliteration on hover
            - Turn on per site
Tech stack: JavaScript, Chrome Extension Manifest V3, ONNX Runtime Web
```

---

## Example 361

**Intent:**
raycast extension to check if a domain is available

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Check a domain name with an RDAP lookup
            - Show availability for common TLDs at once
            - Show price from a registrar API
            - Open the registrar page to buy
            - Keep a list of checked domains
API:        REST
            GET  https://rdap.org/domain/{domain}
Tech stack: TypeScript, React, Raycast API
```

---

## Example 362

**Intent:**
blender addon that renders the same scene from all cameras in one go

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - List all cameras in the scene with checkboxes
            - Render each selected camera to a separate file
            - Name files after the camera
            - Support animation ranges per camera with markers
            - Show progress in the status bar
Tech stack: Python, Blender bpy API
```

---

## Example 363

**Intent:**
unity editor helper to set the import settings of all textures in a folder at once

**Spec:**
```
Type:       Plugin (Unity editor extension)
Data model: TexturePreset(folder, max_size, compression, generate_mipmaps, srgb)
Features:   - Define presets per folder
            - Apply max size, compression and mipmap settings on import
            - Reimport existing textures with one button
            - Show textures that differ from the preset
            - Support platform overrides for Android and iOS
Tech stack: C#, Unity Editor API (AssetPostprocessor, TextureImporter)
```

---

## Example 364

**Intent:**
alfred workflow to search jira tickets and open them

**Spec:**
```
Type:       Plugin (Alfred workflow)
Features:   - Search issues by key or text
            - Show status and assignee as subtitle
            - Open the issue in the browser
            - Copy the issue key with a modifier
            - Show issues assigned to me with a keyword
API:        Jira REST
            GET  /rest/api/3/search?jql={jql}
Tech stack: Python, Alfred Script Filter JSON
```

---

## Example 365

**Intent:**
obsidian plugin to publish a note to my ghost blog

**Spec:**
```
Type:       Plugin (Obsidian)
Features:   - Convert the note's Markdown to Ghost's HTML
            - Upload embedded images to Ghost
            - Create a draft or published post
            - Read title, tags and excerpt from frontmatter
            - Save the post URL back into frontmatter
API:        Ghost Admin REST
            POST /ghost/api/admin/posts/?source=html
            POST /ghost/api/admin/images/upload/
Tech stack: TypeScript, Obsidian API, Ghost Admin API
```

---

## Example 366

**Intent:**
I'm a real estate photographer and agents always ask me for the same edits. I want a Lightroom preset manager plugin where each agent has their own preset and the export goes into their own Dropbox folder.

**Spec:**
```
Type:       Plugin (Lightroom Classic)
Data model: Agent(id, name, preset_name, dropbox_folder, watermark)
Features:   - Keep a list of agents with their preset and Dropbox folder
            - Apply the agent's develop preset to selected photos
            - Export at MLS size limits
            - Upload exports to the agent's Dropbox folder
            - Send the agent a share link by email
API:        Dropbox REST
            POST /2/files/upload
            POST /2/sharing/create_shared_link_with_settings
Tech stack: Lua, Lightroom Classic SDK, Dropbox API v2
```

---

## Example 367

**Intent:**
chrome extension that highlights which words on a page are in the top 1000 most common english words so i know what to learn

**Spec:**
```
Type:       Browser extension (vocabulary level)
Data model: WordList(name, words)
            KnownWord(word, added_at)
Features:   - Color words by frequency band (top 1000, 1000-5000, rare)
            - Skip words the learner marked as known
            - Show the page's vocabulary difficulty as a percent
            - Click a word to see its definition
            - Choose word lists for other languages
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 368

**Intent:**
discord bot that posts when someone in our server starts streaming on twitch

**Spec:**
```
Type:       Bot (Discord)
Data model: TrackedStreamer(id, guild_id, twitch_login, discord_user_id, last_stream_id)
Features:   - Add streamers with a slash command
            - Subscribe to Twitch stream.online EventSub events
            - Post an embed with title, game and thumbnail
            - Give the streamer a "Live" role while streaming
            - Remove the role when the stream ends
API:        Twitch EventSub webhook
            POST /eventsub/callback
Storage:    SQLite
Tech stack: TypeScript, discord.js, Twitch Helix API
```

---

## Example 369

**Intent:**
plugin for jira where qa can attach a screen recording to a bug in one click

**Spec:**
```
Type:       Browser extension (Jira bug capture)
Features:   - Record the current tab or screen with audio
            - Capture console errors and network failures during recording
            - Create a Jira bug with the video attached
            - Prefill browser, OS and URL in the description
            - Pick the project and issue type in the popup
API:        Jira REST
            POST /rest/api/3/issue
            POST /rest/api/3/issue/{issueKey}/attachments
Tech stack: TypeScript, Chrome Extension Manifest V3 (tabCapture, offscreen), Jira Cloud REST API
```

---

## Example 370

**Intent:**
hey can i get a obsidian plugin that makes a graph of my spending from notes where i write "spent 12 on lunch"

**Spec:**
```
Type:       Plugin (Obsidian)
Data model: Expense(date, amount, category, note_path)
Features:   - Parse "spent <amount> on <thing>" lines in daily notes
            - Map things to categories with a keyword list
            - Show monthly totals by category in a chart view
            - Show the biggest expenses this month
            - Export expenses as CSV
Tech stack: TypeScript, Obsidian API, Chart.js
```

---

## Example 371

**Intent:**
home assistant integration for our church bells controller so we can schedule them

**Spec:**
```
Type:       Plugin (Home Assistant custom integration)
Features:   - Connect to the bell controller over its serial-to-network bridge
            - Create a button entity for each bell pattern
            - Create a switch to mute all bells
            - Expose a service to ring a pattern
            - Allow scheduling through Home Assistant automations
Tech stack: Python, Home Assistant integration framework, pyserial-asyncio
```

---

## Example 372

**Intent:**
grafana panel like a traffic light for our build pipelines

**Spec:**
```
Type:       Plugin (Grafana panel)
Features:   - Show one row per pipeline with stage circles
            - Color stages green, yellow or red by status field
            - Show duration of each stage
            - Link each pipeline to its CI page
            - Sort pipelines by last failure
Tech stack: TypeScript, React, Grafana plugin SDK
```

---

## Example 373

**Intent:**
zotero plugin to export my highlights from pdfs as markdown to obsidian

**Spec:**
```
Type:       Plugin (Zotero)
Features:   - Read annotations (highlights and comments) from the item's PDF
            - Format them as Markdown with page numbers and colors
            - Add a citation key and item metadata as frontmatter
            - Write the note into the Obsidian vault folder
            - Update the note when new highlights are added
Tech stack: JavaScript, Zotero 7 plugin API
```

---

## Example 374

**Intent:**
canvas plugin for language teachers, a conversation practice tool with an AI partner graded by rubric

**Spec:**
```
Type:       Plugin (Canvas LTI 1.3 tool)
Data model: Scenario(id, course_id, title, language, prompt, rubric_json)
            Attempt(id, scenario_id -> Scenario, student_id, transcript, score, feedback)
Features:   - Let teachers create conversation scenarios with a rubric
            - Let students chat with an AI partner in the target language
            - Score the conversation against the rubric
            - Show feedback on grammar and vocabulary
            - Send the score to the Canvas gradebook
API:        REST
            POST /lti/launch
            POST /attempts
            POST /attempts/{id}/messages
            POST /attempts/{id}/finish
Storage:    PostgreSQL
Tech stack: Python, FastAPI, PyLTI1p3, OpenAI API
```

---

## Example 375

**Intent:**
anki addon that makes cloze cards from a paragraph I paste by picking keywords

**Spec:**
```
Type:       Plugin (Anki add-on)
Features:   - Open a dialog to paste a paragraph
            - Suggest keywords by term frequency
            - Let the user click words to cloze
            - Create one cloze note with numbered deletions
            - Add the source as a field
Tech stack: Python, Anki add-on API, PyQt6
```

---

## Example 376

**Intent:**
obs plugin, a scene switcher that changes scene based on which app window is focused

**Spec:**
```
Type:       Plugin (OBS Studio)
Data model: Rule(window_title_pattern, scene_name, priority)
Features:   - Watch the focused window title
            - Switch to the scene of the first matching rule
            - Use a default scene when nothing matches
            - Add a delay to avoid rapid switching
            - Edit rules in a dock panel
Tech stack: C++, OBS Studio plugin API, Qt
```

---

## Example 377

**Intent:**
teams bot to check who is in the office today

**Spec:**
```
Type:       Bot (Microsoft Teams)
Data model: OfficeDay(user_id, date, location)
Features:   - Ask people each morning where they work today
            - Let people answer with buttons (office, home, away)
            - Answer "who is in the office" questions
            - Show a weekly office plan as a card
            - Remind people who did not answer
Storage:    Azure Table Storage
Tech stack: Python, Bot Framework SDK, Adaptive Cards
```

---

## Example 378

**Intent:**
chrome addon to compare prices of the same book on different sites

**Spec:**
```
Type:       Browser extension (book price comparison)
Features:   - Detect ISBN on book product pages
            - Look up prices on other stores and used-book sites
            - Show a price list with shipping in a popup
            - Highlight the cheapest option
            - Check the local library catalog for availability
API:        REST
            GET  /prices?isbn={isbn}
Tech stack: JavaScript, Chrome Extension Manifest V3, Node.js price lookup service
```

---

## Example 379

**Intent:**
blender addon for rigging: auto weight paint check, shows verts with no weights

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Find vertices without any vertex group weight
            - Find vertices with more than 4 influences
            - Select problem vertices in edit mode
            - Normalize weights for selected vertices
            - Show counts in a sidebar panel
Tech stack: Python, Blender bpy API, bmesh
```

---

## Example 380

**Intent:**
i make tutorials, want a chrome extension that zooms the screen where i click while recording

**Spec:**
```
Type:       Browser extension (tutorial recording helper)
Features:   - Show a click ripple at the mouse position
            - Zoom smoothly into the click area for a few seconds
            - Highlight the focused input
            - Show pressed keyboard shortcuts
            - Toggle effects with a hotkey
Tech stack: JavaScript, Chrome Extension Manifest V3, CSS transforms
```

---

## Example 381

**Intent:**
unity editor tool where designers tweak gameplay values in a table while playing and save them

**Spec:**
```
Type:       Plugin (Unity editor extension)
Features:   - Find ScriptableObjects marked with a [Tunable] attribute
            - Show their fields in one editable table
            - Keep changes made during play mode
            - Record a change history with undo
            - Export values to CSV
Tech stack: C#, Unity Editor API, UI Toolkit
```

---

## Example 382

**Intent:**
godot plugin to make 2d lights from a sprite's bright parts

**Spec:**
```
Type:       Plugin (Godot editor plugin)
Features:   - Read the selected sprite's texture
            - Find bright pixels above a threshold
            - Create PointLight2D nodes at bright areas
            - Set light color from the pixel color
            - Merge close lights into one
Tech stack: GDScript, Godot 4 EditorPlugin API
```

---

## Example 383

**Intent:**
chrome extension that tells me the carbon footprint of my flights on booking sites

**Spec:**
```
Type:       Browser extension (flight emissions)
Features:   - Detect flight results on supported booking sites
            - Estimate CO2 per passenger from route and aircraft
            - Show the estimate next to each flight
            - Highlight the lowest-emission option
            - Show a yearly total of booked flights
API:        REST
            POST https://travelimpactmodel.googleapis.com/v1/flights:computeFlightEmissions
Tech stack: JavaScript, Chrome Extension Manifest V3, Travel Impact Model API
```

---

## Example 384

**Intent:**
logseq plugin to import my readwise highlights

**Spec:**
```
Type:       Plugin (Logseq)
Features:   - Fetch highlights updated since the last sync
            - Create one page per book or article
            - Add highlights as blocks with their notes
            - Keep a sync cursor to avoid duplicates
            - Sync on startup and on command
API:        Readwise REST
            GET  /api/v2/export/?updatedAfter={date}
Tech stack: TypeScript, Logseq Plugin SDK, Readwise API
```

---

## Example 385

**Intent:**
alfred workflow to start a pomodoro and show time left

**Spec:**
```
Type:       Plugin (Alfred workflow)
Features:   - Start a 25-minute timer with a keyword
            - Show time remaining when the keyword is typed again
            - Post a macOS notification when time is up
            - Start a break automatically
            - Log completed pomodoros to a file
Tech stack: Bash, AppleScript, Alfred workflow
```

---

## Example 386

**Intent:**
confluence app where people can add emoji reactions to pages

**Spec:**
```
Type:       Plugin (Confluence Cloud app)
Data model: Reaction(page_id, account_id, emoji, created_at)
Features:   - Show a reaction bar at the bottom of pages
            - Let users add or remove emoji reactions
            - Show who reacted on hover
            - Show most reacted pages in a space report
            - Limit to a chosen emoji set
Storage:    Forge storage API
Tech stack: Atlassian Forge, TypeScript, React (Custom UI)
```

---

## Example 387

**Intent:**
firefox addon for developers that edits and replays a request from the network list

**Spec:**
```
Type:       Browser extension (API request replay)
Features:   - Capture requests from the current tab
            - Show method, URL, headers and body in an editor
            - Change any field and send the request again
            - Show the response with status, headers and pretty body
            - Save requests to a collection
Storage:    browser.storage.local
Tech stack: TypeScript, Firefox WebExtensions API (devtools panel, webRequest)
```

---

## Example 388

**Intent:**
chrome extension to help me fill job applications using my resume data

**Spec:**
```
Type:       Browser extension (form autofill for job applications)
Data model: Profile(name, email, phone, address, links_json)
            Experience(id, company, title, start_date, end_date, description)
            Education(id, school, degree, year)
Features:   - Store profile, experience and education once
            - Detect common fields in job application forms
            - Fill fields with matching profile data
            - Handle Workday and Greenhouse forms specially
            - Show which fields were filled for review
Storage:    chrome.storage.local
Tech stack: TypeScript, Chrome Extension Manifest V3, React
```

---

## Example 389

**Intent:**
Hello, me and my friends play Minecraft Bedrock, we want addon where you can tame dragons and ride them

**Spec:**
```
Type:       Plugin (Minecraft Bedrock add-on)
Features:   - Add a dragon entity with its own model and texture
            - Let players tame a dragon with a special item
            - Let tamed dragons be ridden and flown with controls
            - Make dragons follow their owner
            - Add dragon eggs that hatch over time
Tech stack: JSON (behavior and resource packs), JavaScript (Minecraft Script API), Blockbench
```

---

## Example 390

**Intent:**
photoshop plugin which makes a color palette from the image and saves as swatches

**Spec:**
```
Type:       Plugin (Photoshop UXP)
Features:   - Sample the active document's pixels
            - Find dominant colors with k-means
            - Show the palette with hex codes in a panel
            - Add the colors to the Swatches panel
            - Export the palette as ASE or JSON
Tech stack: JavaScript, Adobe UXP, Photoshop imaging API
```

---

## Example 391

**Intent:**
gimp plugin for photographers, add a white border and the camera exif settings under the photo

**Spec:**
```
Type:       Plugin (GIMP Python plug-in)
Features:   - Read camera, lens, focal length, aperture, shutter and ISO from EXIF
            - Extend the canvas with a white border
            - Write settings in small text under the photo
            - Let the user choose font and border size
            - Export as JPEG
Tech stack: Python, GIMP 3 Python API, GExiv2
```

---

## Example 392

**Intent:**
zoom app to play pictionary with my students

**Spec:**
```
Type:       Plugin (Zoom App game)
Data model: Round(id, meeting_id, drawer_id, word, started_at)
            Guess(round_id -> Round, participant_id, text, correct)
Features:   - Pick a drawer and give them a secret word
            - Share their drawing live to all participants
            - Let others type guesses
            - Give points for correct guesses based on speed
            - Let the teacher load custom word lists
API:        WebSocket
            /ws/pictionary/{meeting_id}
Tech stack: TypeScript, Zoom Apps SDK, React, Socket.IO
```

---

## Example 393

**Intent:**
moodle plugin that sends parents a weekly email with their kid's grades

**Spec:**
```
Type:       Plugin (Moodle local plugin)
Data model: ParentLink(id, parent_email, student_id, verified)
Features:   - Let students or admins link parent email addresses
            - Collect grades and missing assignments for the week
            - Send a weekly email digest to parents
            - Let parents unsubscribe
            - Respect a course setting to opt out
Storage:    Moodle database
Tech stack: PHP, Moodle Scheduled Task API, Moodle Messaging API
```

---

## Example 394

**Intent:**
trello power-up that estimates delivery dates with a monte carlo forecast

**Spec:**
```
Type:       Plugin (Trello Power-Up)
Features:   - Read card completion history from the board
            - Simulate future throughput with Monte Carlo runs
            - Show the date by which remaining cards finish with 50%, 85% and 95% confidence
            - Show a histogram of outcomes
            - Let users choose which lists count as done
API:        Trello REST
            GET  /1/boards/{id}/actions?filter=updateCard:idList
Tech stack: JavaScript, Trello Power-Up client library, Chart.js
```

---

## Example 395

**Intent:**
raycast extension to translate selected text with deepl

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Read the selected text from the front app
            - Translate it to a default target language
            - Detect the source language automatically
            - Copy or paste the translation
            - Switch target language from a dropdown
API:        DeepL REST
            POST /v2/translate
Tech stack: TypeScript, React, Raycast API
```

---

## Example 396

**Intent:**
blender addon to convert my scene to a game engine friendly gltf with lods

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Generate LOD meshes with a decimate modifier at chosen ratios
            - Name LODs with _LOD0, _LOD1 suffixes
            - Bake modifiers before export
            - Export the scene as glTF binary
            - Report triangle counts per LOD
Tech stack: Python, Blender bpy API, glTF exporter
```

---

## Example 397

**Intent:**
browser extension for a nonprofit that adds a 'donate to us' round up when people buy online

**Spec:**
```
Type:       Browser extension (round-up donations)
Data model: Donor(id, email, monthly_cap)
            RoundUp(id, donor_id -> Donor, store, order_total, amount, created_at)
Features:   - Detect order confirmation pages on supported stores
            - Calculate the round-up to the next whole amount
            - Ask the donor to confirm the round-up
            - Charge saved round-ups monthly up to a cap
            - Show total donated this year
API:        REST
            POST /roundups
            GET  /donors/me/summary
Storage:    PostgreSQL
Tech stack: JavaScript (Chrome Extension Manifest V3), Node.js, Stripe
```

---

## Example 398

**Intent:**
discord bot that converts times in messages to everyone's timezone

**Spec:**
```
Type:       Bot (Discord)
Data model: UserTimezone(user_id, timezone)
Features:   - Let users set their time zone with a slash command
            - Detect times like "8pm EST" in messages
            - Reply with a Discord timestamp that shows in each reader's local time
            - React with a clock emoji instead of replying when configured
            - Ignore messages in excluded channels
Storage:    SQLite
Tech stack: Python, discord.py, dateparser
```

---

## Example 399

**Intent:**
home assistant card that shows the next birthday from my contacts

**Spec:**
```
Type:       Plugin (Home Assistant Lovelace card)
Features:   - Read birthdays from a calendar entity
            - Show the next five birthdays with days remaining
            - Show the age they will turn
            - Highlight birthdays today
            - Set the number of entries in the card editor
Tech stack: TypeScript, Lit, Home Assistant custom card API
```

---

## Example 400

**Intent:**
obsidian plugin that tracks how many times i've reviewed each note and suggests old ones to revisit

**Spec:**
```
Type:       Plugin (Obsidian)
Data model: NoteReview(path, review_count, last_reviewed_at)
Features:   - Record when a note is opened for more than 30 seconds
            - Suggest notes not opened in a long time in a side panel
            - Weight suggestions by tags the user cares about
            - Mark a note as reviewed
            - Exclude folders like templates
Storage:    Obsidian plugin data.json
Tech stack: TypeScript, Obsidian API
```

---

## Example 401

**Intent:**
chrome extension for language teachers to make a listening exercise from any youtube video with gaps in subtitles

**Spec:**
```
Type:       Browser extension (listening exercise maker)
Features:   - Load the video's captions
            - Remove every nth word or chosen words
            - Play the video segment by segment
            - Let the student type missing words and check them
            - Share the exercise as a link
API:        REST
            POST /exercises
            GET  /exercises/{id}
Storage:    Firebase Firestore
Tech stack: JavaScript, Chrome Extension Manifest V3, YouTube IFrame Player API, Firebase
```

---

## Example 402

**Intent:**
jira plugin that blocks moving tickets to done if there is no linked pull request

**Spec:**
```
Type:       Plugin (Jira Cloud workflow validator)
Features:   - Add a workflow validator for the Done transition
            - Check the issue's development panel for linked pull requests
            - Block the transition with a clear message when none is found
            - Allow certain issue types to skip the check
            - Let admins configure exempt types
Tech stack: Atlassian Forge, TypeScript, Jira workflow validator module
```

---

## Example 403

**Intent:**
unity tool that generates a colliders for my 2d level tiles automatically

**Spec:**
```
Type:       Plugin (Unity editor extension)
Features:   - Read the Tilemap with solid tiles
            - Merge adjacent solid tiles into rectangles
            - Create BoxCollider2D or a CompositeCollider2D from the rectangles
            - Mark one-way platforms from a tile flag
            - Rebuild colliders after tile edits
Tech stack: C#, Unity Editor API, Unity Tilemap
```

---

## Example 404

**Intent:**
krita plugin to export my comic pages to the right sizes for webtoon

**Spec:**
```
Type:       Plugin (Krita Python plug-in)
Features:   - Take the open pages in order
            - Stack them vertically into one long strip
            - Resize to the webtoon width of 800 pixels
            - Split the strip into slices under the upload height limit
            - Export slices as numbered JPEGs
Tech stack: Python, Krita scripting API
```

---

## Example 405

**Intent:**
thunderbird add on that shows how long ago I last emailed this person

**Spec:**
```
Type:       Plugin (Thunderbird add-on)
Features:   - Read the recipient addresses in the compose window
            - Search sent mail for the last message to each recipient
            - Show "last emailed X days ago" under the address
            - Open the last message on click
            - Cache results per address
Tech stack: JavaScript, Thunderbird MailExtensions API
```

---

## Example 406

**Intent:**
wordpress is not mine, its for a mastodon instance: a plugin that shows trending local hashtags

**Spec:**
```
Type:       Web application (Mastodon trends widget)
Features:   - Fetch local timeline posts with the Mastodon API
            - Count hashtag usage over the last 24 hours
            - Show a ranked list with sparklines
            - Embed as an iframe widget
            - Refresh every 10 minutes
API:        Mastodon REST
            GET  /api/v1/timelines/public?local=true
Storage:    Redis
Tech stack: Python, FastAPI, Jinja2
```

---

## Example 407

**Intent:**
plugin for kicad that checks my board against my fab's design rules and makes a report

**Spec:**
```
Type:       Plugin (KiCad action plugin)
Data model: FabProfile(name, min_trace_mm, min_space_mm, min_drill_mm, min_annular_ring_mm)
Features:   - Choose a fab profile (JLCPCB, PCBWay or custom)
            - Check trace width, spacing, drill size and annular ring
            - List violations with their location
            - Zoom to a violation when selected
            - Export the report as HTML
Tech stack: Python, KiCad pcbnew API, wxPython
```

---

## Example 408

**Intent:**
chrome extension for medical coders to look up icd-10 codes from selected text

**Spec:**
```
Type:       Browser extension (medical coding)
Features:   - Add a context menu "Find ICD-10 code" for selected text
            - Search the ICD-10-CM list for matching terms
            - Show codes with descriptions in a popup
            - Copy a code with one click
            - Keep a favourites list of codes
API:        REST
            GET  https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms={text}
Tech stack: JavaScript, Chrome Extension Manifest V3, NLM Clinical Tables API
```

---

## Example 409

**Intent:**
a vst plugin that sidechains the bass to the kick automatically

**Spec:**
```
Type:       Plugin (VST3 audio effect)
Features:   - Accept a sidechain input from the kick track
            - Detect kick transients
            - Duck the main input volume with an envelope
            - Control depth, attack and release with knobs
            - Show the gain reduction meter
Tech stack: C++, JUCE, VST3 SDK
```

---

## Example 410

**Intent:**
soo my mom runs a tiny bakery and she takes orders on facebook messenger. can u make a chrome extention that turns a chat into an order with the cake, date and price so she stops losing them

**Spec:**
```
Type:       Browser extension (chat order capture)
Data model: Order(id, customer_name, item, pickup_date, price, notes, status, chat_url)
Features:   - Add an "Make order" button in Messenger conversations
            - Prefill customer name and selected message text
            - Pick the cake, pickup date and price in a small form
            - Show upcoming orders sorted by pickup date
            - Print a daily list of orders for the kitchen
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 411

**Intent:**
blender add-on for jewelry designers that calculates the metal weight of the ring

**Spec:**
```
Type:       Plugin (Blender add-on)
Data model: Metal(name, density_g_cm3)
Features:   - Calculate the volume of the selected closed mesh
            - Convert volume to weight for gold, silver and platinum
            - Warn when the mesh is not watertight
            - Show ring size from the inner diameter
            - Show results in a sidebar panel
Tech stack: Python, Blender bpy API, bmesh
```

---

## Example 412

**Intent:**
obsidian plugin to show all my notes on a map if they have coordinates in frontmatter

**Spec:**
```
Type:       Plugin (Obsidian)
Features:   - Read location coordinates from note frontmatter
            - Show notes as markers on a map view
            - Open a note by clicking its marker
            - Filter markers by tag
            - Cluster nearby markers
Tech stack: TypeScript, Obsidian API, Leaflet
```

---

## Example 413

**Intent:**
OBS plugin that shows a goal bar for subs on twitch

**Spec:**
```
Type:       Plugin (OBS Studio browser source overlay)
Features:   - Read the current subscriber count from the Twitch API
            - Show a progress bar toward a goal
            - Update in real time on new subs with EventSub
            - Animate when the goal is reached
            - Let the streamer set goal text and colors in a config page
API:        Twitch EventSub WebSocket
            wss://eventsub.wss.twitch.tv/ws
Tech stack: JavaScript, HTML/CSS, Twitch Helix API
```

---

## Example 414

**Intent:**
Hi, my company does tours in Italy. Our guides use Teams. I want a Teams bot that each morning sends the guide their tour group list and the meeting point with map.

**Spec:**
```
Type:       Bot (Microsoft Teams)
Data model: Guide(id, teams_user_id, name)
            Tour(id, guide_id -> Guide, date, meeting_point, lat, lng)
            Guest(id, tour_id -> Tour, name, phone, language)
Features:   - Send each guide a morning Adaptive Card with today's tours
            - List guests with language and phone
            - Show the meeting point with a map link
            - Let guides mark no-shows from the card
            - Alert the office when a guide has not opened the card by 8am
Storage:    Azure SQL Database
Tech stack: C#, Bot Framework SDK, Adaptive Cards, Azure Functions
```

---

## Example 415

**Intent:**
canvas tool to randomly pick a student to answer, and not the same one twice

**Spec:**
```
Type:       Plugin (Canvas LTI 1.3 tool)
Data model: PickHistory(course_id, student_id, picked_at)
Features:   - Load the course roster from Canvas
            - Pick a random student with an animation
            - Avoid students picked recently until everyone has had a turn
            - Let the teacher mark absent students
            - Reset the cycle
Storage:    SQLite
Tech stack: Python, Flask, PyLTI1p3
```

---

## Example 416

**Intent:**
anki addon for chinese learners that adds stroke order animations to cards

**Spec:**
```
Type:       Plugin (Anki add-on)
Features:   - Detect Chinese characters in a chosen field
            - Insert stroke order animations using Hanzi Writer data
            - Add a quiz mode where the learner draws the strokes
            - Bundle data so it works offline
            - Apply to selected notes from the browser
Tech stack: Python, Anki add-on API, JavaScript (Hanzi Writer)
```

---

## Example 417

**Intent:**
chrome thing that shows how much the stuff on my netflix list costs to rent or buy elsewhere

**Spec:**
```
Type:       Browser extension (streaming availability)
Features:   - Read titles on streaming service pages
            - Look up where each title can be streamed, rented or bought
            - Show prices and services in a hover card
            - Filter by the user's country
            - Mark titles leaving the service soon
API:        REST
            GET  /availability?title={title}&country={country}
Tech stack: JavaScript, Chrome Extension Manifest V3, JustWatch-like availability API
```

---

## Example 418

**Intent:**
jira plugin that shows estimated vs actual time on a dashboard gadget

**Spec:**
```
Type:       Plugin (Jira Cloud dashboard gadget)
Features:   - Read original estimate and time spent for issues in a JQL filter
            - Show estimate vs actual per issue as a bar chart
            - Show the overall accuracy percentage
            - Highlight issues over estimate by 50%
            - Group by assignee
API:        Jira REST
            GET  /rest/api/3/search?jql={jql}&fields=timeoriginalestimate,timespent
Tech stack: Atlassian Forge, TypeScript, React
```

---

## Example 419

**Intent:**
home assistant integration for my sauna controller

**Spec:**
```
Type:       Plugin (Home Assistant custom integration)
Features:   - Connect to the sauna controller's cloud API
            - Create a climate entity with target temperature
            - Add a sensor for current temperature and humidity
            - Add a switch for lights
            - Notify when the sauna reaches the target temperature
API:        REST
            GET  /api/devices/{id}/state
            POST /api/devices/{id}/heating
Tech stack: Python, Home Assistant integration framework, aiohttp
```

---

## Example 420

**Intent:**
zotero plugin to check if my references follow the journal's format before I submit

**Spec:**
```
Type:       Plugin (Zotero)
Data model: JournalRule(journal, required_fields, max_authors, doi_required)
Features:   - Check selected items for missing required fields
            - Check DOI presence and author name formatting
            - Flag titles in all caps
            - Show a checklist report per item
            - Open the item to fix it
Tech stack: JavaScript, Zotero 7 plugin API
```

---

## Example 421

**Intent:**
grafana panel for a factory floor: machines shown on a floor plan image with status colors

**Spec:**
```
Type:       Plugin (Grafana panel)
Data model: MachinePosition(machine_id, x_pct, y_pct, label)
Features:   - Show an uploaded floor plan image as background
            - Place machine markers by drag and drop in edit mode
            - Color markers by the machine's status metric
            - Show current values in a tooltip
            - Blink markers that are in alarm
Tech stack: TypeScript, React, Grafana plugin SDK
```

---

## Example 422

**Intent:**
discord bot that lets members anonymously vent to a channel with mod review

**Spec:**
```
Type:       Bot (Discord)
Data model: VentPost(id, guild_id, author_hash, text, status, created_at)
Features:   - Let members send a vent with a slash command in DMs
            - Queue posts for moderator approval
            - Post approved vents anonymously to a channel
            - Store only a hashed author ID for abuse handling
            - Show crisis resource links on posts with risky keywords
Storage:    PostgreSQL
Tech stack: Node.js, discord.js
```

---

## Example 423

**Intent:**
raycast extension to search emoji and kaomoji and copy them

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Search emoji by name and keyword
            - Search kaomoji by mood
            - Copy or paste the chosen symbol
            - Show recently used items first
            - Pick skin tone in preferences
Tech stack: TypeScript, React, Raycast API
```

---

## Example 424

**Intent:**
logseq plugin that turns a page into a slideshow

**Spec:**
```
Type:       Plugin (Logseq)
Features:   - Treat each top-level block as a slide
            - Render nested blocks as bullet points
            - Show images and code with syntax highlighting
            - Move with arrow keys in a fullscreen view
            - Export the slides to HTML
Tech stack: TypeScript, Logseq Plugin SDK, Reveal.js
```

---

## Example 425

**Intent:**
a chrome extension that warns me when im about to post something angry on social media

**Spec:**
```
Type:       Browser extension (mindful posting)
Features:   - Watch the text in post and comment boxes on social sites
            - Score the text's tone with a local sentiment model
            - Show a gentle warning before posting angry text
            - Offer a 1-minute delay before sending
            - Show a weekly count of warnings
Tech stack: JavaScript, Chrome Extension Manifest V3, TensorFlow.js
```

---

## Example 426

**Intent:**
unity editor plugin to batch rename gameobjects with patterns

**Spec:**
```
Type:       Plugin (Unity editor extension)
Features:   - Rename selected objects with a pattern like Enemy_{index}
            - Support find and replace and regex
            - Add prefixes and suffixes
            - Preview new names before applying
            - Support undo
Tech stack: C#, Unity Editor API
```

---

## Example 427

**Intent:**
godot plugin that shows a todo list from comments in all my scripts

**Spec:**
```
Type:       Plugin (Godot editor plugin)
Features:   - Scan GDScript and C# files for TODO and FIXME comments
            - List them in a bottom dock with file and line
            - Open the script at the line on click
            - Filter by tag
            - Rescan when files are saved
Tech stack: GDScript, Godot 4 EditorPlugin API
```

---

## Example 428

**Intent:**
photoshop plugin to make before after comparison images for my retouching portfolio

**Spec:**
```
Type:       Plugin (Photoshop UXP)
Features:   - Take a snapshot of the original from history
            - Combine before and after side by side or as a split slider frame
            - Add small "Before" and "After" labels
            - Export as JPEG at web size
            - Create an animated GIF version
Tech stack: JavaScript, Adobe UXP, Photoshop batchPlay API
```

---

## Example 429

**Intent:**
gimp script to find and fix red eye in all photos in a folder

**Spec:**
```
Type:       Plugin (GIMP Python plug-in)
Features:   - Detect faces and eyes with a cascade classifier
            - Find red pixels in the eye regions
            - Desaturate and darken the red areas
            - Save fixed images to an output folder
            - List images where no eyes were found
Tech stack: Python, GIMP 3 Python API, OpenCV
```

---

## Example 430

**Intent:**
chrome extension that lets me see historical prices on steam games

**Spec:**
```
Type:       Browser extension (game price history)
Features:   - Detect Steam store game pages
            - Show the lowest historical price and date
            - Draw a price history chart
            - Show current prices on other stores
            - Add a wishlist price alert
API:        REST
            GET  https://api.isthereanydeal.com/games/history/v2?id={id}
Tech stack: JavaScript, Chrome Extension Manifest V3, IsThereAnyDeal API
```

---

## Example 431

**Intent:**
confluence plugin for an onboarding checklist that each new hire ticks off

**Spec:**
```
Type:       Plugin (Confluence Cloud macro)
Data model: ChecklistProgress(page_id, account_id, item_id, done_at)
Features:   - Insert a checklist macro on onboarding pages
            - Save each user's own progress
            - Show the manager a progress table for new hires
            - Link items to other Confluence pages
            - Send a reminder for items open after a week
Storage:    Forge storage API
Tech stack: Atlassian Forge, TypeScript, React (Custom UI)
```

---

## Example 432

**Intent:**
trello power up that shows the git commits linked to a card

**Spec:**
```
Type:       Plugin (Trello Power-Up)
Features:   - Find commits that mention the card's short ID
            - Show commits with author and message on the card back
            - Show a commit count badge
            - Link to the commit on GitHub
            - Move the card to Done when a commit says "closes"
API:        GitHub REST
            GET  /search/commits?q={card_id}+repo:{repo}
Tech stack: JavaScript, Trello Power-Up client library, Node.js
```

---

## Example 433

**Intent:**
chrome extension to help people with anxiety, it hides like counts and follower numbers

**Spec:**
```
Type:       Browser extension (social media wellbeing)
Data model: Settings(hide_likes, hide_followers, hide_trending, enabled_sites)
Features:   - Hide like, share and view counts on supported sites
            - Hide follower counts on profiles
            - Hide trending sections
            - Reveal a number temporarily on click
            - Turn each option on or off per site
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3, CSS injection
```

---

## Example 434

**Intent:**
obs script that puts the current weather and time on my outdoor livestream

**Spec:**
```
Type:       Plugin (OBS Studio script)
Features:   - Fetch current weather for a set location every 10 minutes
            - Update a text source with temperature, wind and conditions
            - Show local time updated every second
            - Change an image source to a weather icon
            - Configure location and units in script settings
API:        REST
            GET  https://api.open-meteo.com/v1/forecast
Tech stack: Python, OBS Studio scripting API, Open-Meteo API
```

---

## Example 435

**Intent:**
moodle plugin to stop copy paste in essay quiz questions

**Spec:**
```
Type:       Plugin (Moodle question behaviour plugin)
Features:   - Disable paste into essay answer boxes
            - Log paste attempts with timestamps
            - Show the teacher a paste attempt count per attempt
            - Let teachers enable it per quiz
            - Show students a notice that paste is disabled
Storage:    Moodle database
Tech stack: PHP, Moodle Question API, JavaScript
```

---

## Example 436

**Intent:**
Hi, our dev team uses Gitea not GitHub. Need browser extension that shows build status from our Drone CI on the commit list in Gitea

**Spec:**
```
Type:       Browser extension (Gitea CI status)
Features:   - Detect Gitea commit list pages
            - Fetch build status for each commit from Drone
            - Show a status icon next to each commit
            - Link to the build log
            - Refresh status every 30 seconds while builds run
API:        Drone REST
            GET  /api/repos/{owner}/{repo}/builds?commit={sha}
Tech stack: TypeScript, Chrome Extension Manifest V3
```

---

## Example 437

**Intent:**
zoom app that suggests breaks when a meeting goes over 50 min

**Spec:**
```
Type:       Plugin (Zoom App)
Features:   - Track meeting duration
            - Show the host a break reminder at 50 minutes
            - Start a 5-minute break timer visible to everyone
            - Play a chime when the break ends
            - Let the host snooze reminders
Tech stack: TypeScript, Zoom Apps SDK, React
```

---

## Example 438

**Intent:**
firefox extension that shows the reading level of the text i select

**Spec:**
```
Type:       Browser extension (readability check)
Features:   - Calculate Flesch-Kincaid grade and reading ease for selected text
            - Show sentence and word counts
            - Highlight very long sentences
            - Suggest simpler words for common complex words
            - Show the result in a popup
Tech stack: JavaScript, Firefox WebExtensions API, text-readability
```

---

## Example 439

**Intent:**
i want a plugin for my kobo e-reader (koreader) that syncs highlights to my notion

**Spec:**
```
Type:       Plugin (KOReader)
Features:   - Read highlights and notes from the book's sidecar file
            - Create or update a Notion page per book
            - Add highlights as blocks with chapter and date
            - Sync only new highlights
            - Run sync from the menu when Wi-Fi is on
API:        Notion REST
            POST /v1/pages
            PATCH /v1/blocks/{id}/children
Tech stack: Lua, KOReader plugin API, Notion API
```

---

## Example 440

**Intent:**
home assistant lovelace card that shows a robot vacuum map with rooms you can click to clean

**Spec:**
```
Type:       Plugin (Home Assistant Lovelace card)
Features:   - Show the vacuum's map image from a camera entity
            - Draw clickable room areas defined in config
            - Start room cleaning by calling the vacuum service
            - Show the vacuum position and status
            - Let users select multiple rooms
Tech stack: TypeScript, Lit, Home Assistant custom card API
```

---

## Example 441

**Intent:**
blender addon that exports my animation as a sprite sheet for 2d games

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Render the animation from an orthographic camera
            - Render several directions by rotating the object
            - Pack frames into a sprite sheet image
            - Write a JSON file with frame rectangles
            - Trim empty space around frames
Tech stack: Python, Blender bpy API, Pillow
```

---

## Example 442

**Intent:**
chrome extension for language learners: chat with a tutor ai about the page you are reading in the target language

**Spec:**
```
Type:       Browser extension (AI language tutor)
Data model: ChatMessage(id, page_url, role, text, created_at)
Features:   - Open a side panel chat about the current page
            - Answer in the learner's target language at their level
            - Correct the learner's mistakes and explain them
            - Explain selected words or sentences
            - Save new words to a vocabulary list
Storage:    chrome.storage.local
Tech stack: TypeScript, Chrome Extension Manifest V3 (sidePanel), OpenAI API
```

---

## Example 443

**Intent:**
unity editor tool to compare two scenes and list differences

**Spec:**
```
Type:       Plugin (Unity editor extension)
Features:   - Pick two scene assets to compare
            - Match game objects by path
            - List added, removed and changed objects
            - Show changed component properties
            - Open the object in its scene when clicked
Tech stack: C#, Unity Editor API (SerializedObject, EditorSceneManager)
```

---

## Example 444

**Intent:**
zotero plugin that groups my library by research method automatically

**Spec:**
```
Type:       Plugin (Zotero)
Features:   - Read title and abstract of selected items
            - Classify each item's research method (survey, experiment, case study, review) with an LLM
            - Add the method as a tag
            - Let the user correct and lock a tag
            - Show counts per method
Tech stack: JavaScript, Zotero 7 plugin API, OpenAI API
```

---

## Example 445

**Intent:**
discord bot for a book club that schedules the meeting and tracks reading progress

**Spec:**
```
Type:       Bot (Discord)
Data model: Book(id, guild_id, title, chapters, meeting_at)
            Progress(book_id -> Book, user_id, chapter)
Features:   - Set the current book and meeting date with a slash command
            - Let members update their chapter
            - Show everyone's progress as a bar list
            - Remind members three days before the meeting
            - Hide spoilers with spoiler tags in a discussion thread
Storage:    SQLite
Tech stack: Python, discord.py, APScheduler
```

---

## Example 446

**Intent:**
alfred workflow to search and paste snippets from a github gist

**Spec:**
```
Type:       Plugin (Alfred workflow)
Features:   - Fetch the user's gists
            - Search gists by description and filename
            - Paste the gist content into the front app
            - Copy the gist URL with a modifier
            - Refresh the cache with a keyword
API:        GitHub REST
            GET  /gists
Tech stack: Python, Alfred Script Filter JSON
```

---

## Example 447

**Intent:**
grafana panel that shows a sankey diagram of traffic between services

**Spec:**
```
Type:       Plugin (Grafana panel)
Features:   - Read source, target and value fields
            - Draw a Sankey diagram of flows
            - Color links by source
            - Show values on hover
            - Let users set node width and padding
Tech stack: TypeScript, React, Grafana plugin SDK, d3-sankey
```

---

## Example 448

**Intent:**
i'm a voice actor and want a chrome extension that pulls the lines for my character from a script google doc

**Spec:**
```
Type:       Browser extension (script line extractor)
Features:   - Read the open Google Doc's text
            - Find lines for a chosen character name
            - Show only that character's lines with the cue line before
            - Number the lines
            - Export lines to a text file for recording
Tech stack: JavaScript, Chrome Extension Manifest V3, Google Docs API
```

---

## Example 449

**Intent:**
plz chrome extension 4 my uni portal, it logs me out every 10 min and i lose my essay

**Spec:**
```
Type:       Browser extension (session keep-alive and draft saver)
Data model: Draft(id, page_url, field_selector, text, saved_at)
Features:   - Send a keep-alive request to the portal at a set interval
            - Auto-save text typed in large text fields every 30 seconds
            - Restore a saved draft after an unexpected logout
            - Warn before the session expires
            - Limit the extension to the portal's domain
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3 (alarms)
```

---

## Example 450

**Intent:**
I'm a nurse educator. Our hospital uses Moodle for training and nurses must redo certificates yearly. Can a plugin email them a month before their certificate expires and show managers who is overdue?

**Spec:**
```
Type:       Plugin (Moodle local plugin)
Data model: Certification(id, user_id, course_id, completed_at, expires_at)
            Reminder(id, certification_id -> Certification, sent_at)
Features:   - Set expiry from course completion plus a validity period
            - Email nurses 30 and 7 days before expiry
            - Reset course progress when recertification opens
            - Show managers a report of overdue staff by ward
            - Export the report to Excel
Storage:    Moodle database
Tech stack: PHP, Moodle Scheduled Task API, Moodle Messaging API
```

---

## Example 451

**Intent:**
obsidian plugin that gives my notes a "freshness" color in the file list based on last edit

**Spec:**
```
Type:       Plugin (Obsidian)
Features:   - Read each note's last modified time
            - Color file names from green (recent) to grey (old)
            - Let users set the age ranges
            - Add a command to list the oldest notes
            - Ignore chosen folders
Tech stack: TypeScript, Obsidian API, CSS
```

---

## Example 452

**Intent:**
blender addon for 3d printing: hollow the model and add drain holes

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Create an inner offset shell with a set wall thickness
            - Join the shell with flipped normals to hollow the model
            - Add cylindrical drain holes at clicked points
            - Show the material saved in percent
            - Check the result is manifold
Tech stack: Python, Blender bpy API, bmesh
```

---

## Example 453

**Intent:**
teams app that does anonymous q&a for all hands meetings with upvotes

**Spec:**
```
Type:       Plugin (Microsoft Teams meeting app)
Data model: Question(id, meeting_id, text, anonymous, author_id, upvotes, answered)
            Upvote(question_id -> Question, user_id)
Features:   - Let attendees post questions anonymously or with their name
            - Let attendees upvote questions
            - Sort questions by votes in the side panel
            - Let the host mark questions as answered
            - Show the top question on the meeting stage
API:        REST
            GET  /meetings/{id}/questions
            POST /meetings/{id}/questions
            POST /questions/{id}/upvote
Storage:    Azure Cosmos DB
Tech stack: TypeScript, Teams Toolkit, React, Fluent UI, Azure Web PubSub
```

---

## Example 454

**Intent:**
chrome ext for dyscalculia, makes numbers on pages easier to read

**Spec:**
```
Type:       Browser extension (number reading aid)
Data model: Settings(group_digits, spell_out_numbers, color_digits)
Features:   - Add thousand separators to long numbers
            - Color alternating digit groups
            - Show a spoken version of a number on hover
            - Convert prices to rounded estimates on request
            - Enable per site
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3, Intl.NumberFormat
```

---

## Example 455

**Intent:**
unity tool that warns about missing references in the inspector before i hit play

**Spec:**
```
Type:       Plugin (Unity editor extension)
Features:   - Scan open scenes for null serialized object references on fields marked [Required]
            - List problems in a console-style window
            - Ping the object when an entry is clicked
            - Block entering play mode when problems exist (optional)
            - Run the check on scene save
Tech stack: C#, Unity Editor API (EditorApplication.playModeStateChanged)
```

---

## Example 456

**Intent:**
home assistant integration for my beehive scale

**Spec:**
```
Type:       Plugin (Home Assistant custom integration)
Features:   - Read weight, temperature and humidity from the hive scale's MQTT topics
            - Create sensors per hive
            - Calculate daily weight change
            - Alert on sudden weight drops that may mean swarming
            - Show a long-term statistics graph
Tech stack: Python, Home Assistant integration framework, MQTT
```

---

## Example 457

**Intent:**
grafana panel plugin that is a big single number with a trend arrow for tv screens

**Spec:**
```
Type:       Plugin (Grafana panel)
Features:   - Show the latest value in a very large font
            - Show an arrow and percent change against the previous period
            - Color the background by thresholds
            - Fit text to the panel size
            - Show a small label and unit
Tech stack: TypeScript, React, Grafana plugin SDK
```

---

## Example 458

**Intent:**
raycast extension to control my spotify playback and like songs

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Show the current track with artwork
            - Play, pause and skip tracks
            - Like or unlike the current song
            - Search and play songs, albums and playlists
            - Add the current song to a playlist
API:        Spotify Web API
            GET  /v1/me/player
            PUT  /v1/me/player/play
            PUT  /v1/me/tracks
Tech stack: TypeScript, React, Raycast API, Spotify Web API
```

---

## Example 459

**Intent:**
canvas lms plugin, a reading log where students record minutes read and books

**Spec:**
```
Type:       Plugin (Canvas LTI 1.3 tool)
Data model: ReadingEntry(id, course_id, student_id, book_title, minutes, date)
Features:   - Let students add daily reading entries
            - Show each student a weekly total and streak
            - Show the teacher a class table
            - Grade completion of a weekly minutes goal
            - Sync the grade to Canvas
API:        REST
            POST /entries
            GET  /courses/{id}/summary
Storage:    PostgreSQL
Tech stack: Node.js, Express, ltijs, React
```

---

## Example 460

**Intent:**
zotero addon that suggests related papers i dont have from the references of my library

**Spec:**
```
Type:       Plugin (Zotero)
Features:   - Fetch references of library items from OpenAlex
            - Count how often each missing paper is cited by the user's items
            - Show the top missing papers in a pane
            - Add a paper to the library with one click
            - Hide suggestions the user dismisses
API:        REST
            GET  https://api.openalex.org/works/{id}
Tech stack: JavaScript, Zotero 7 plugin API, OpenAlex API
```

---

## Example 461

**Intent:**
discord bot that rolls character stats and saves character sheets for our campaign

**Spec:**
```
Type:       Bot (Discord)
Data model: Character(id, guild_id, owner_id, name, class, stats_json, hp, level)
Features:   - Roll ability scores with 4d6 drop lowest
            - Create a character sheet with a slash command
            - Show a sheet as an embed
            - Update HP and level
            - Roll checks using the character's modifiers
Storage:    SQLite
Tech stack: Python, discord.py
```

---

## Example 462

**Intent:**
anki addon that pulls example sentences for my words from tatoeba

**Spec:**
```
Type:       Plugin (Anki add-on)
Features:   - Read the word from a chosen field
            - Search Tatoeba for sentences in the target language with translations
            - Let the user pick a sentence
            - Fill the example and translation fields
            - Process many selected notes in batch
API:        REST
            GET  https://tatoeba.org/en/api_v0/search?query={word}&from={lang}&to={lang}
Tech stack: Python, Anki add-on API, requests
```

---

## Example 463

**Intent:**
OBS plugin that mutes the desktop audio automatically when a copyrighted song is detected

**Spec:**
```
Type:       Plugin (OBS Studio)
Features:   - Fingerprint desktop audio in short windows
            - Match fingerprints against a song recognition service
            - Mute the desktop audio source on a match
            - Unmute when the song ends
            - Log detected songs
Tech stack: C++, OBS Studio plugin API, Chromaprint, AcoustID API
```

---

## Example 464

**Intent:**
Photoshop plugin that resizes one design to all social media formats

**Spec:**
```
Type:       Plugin (Photoshop UXP)
Features:   - List social formats (Instagram post, story, Facebook cover, LinkedIn banner)
            - Create a new document per format
            - Scale and center the design with content-aware fill for edges
            - Keep text layers inside safe zones
            - Export all formats as PNG
Tech stack: JavaScript, Adobe UXP, Photoshop batchPlay API
```

---

## Example 465

**Intent:**
gimp plugin for astrophotography that stacks a bunch of photos to reduce noise

**Spec:**
```
Type:       Plugin (GIMP Python plug-in)
Features:   - Load a folder of frames
            - Align frames by detected stars
            - Stack with mean or median
            - Reject outlier pixels with sigma clipping
            - Open the result as a new image
Tech stack: Python, GIMP 3 Python API, NumPy, astroalign
```

---

## Example 466

**Intent:**
godot plugin for a quest editor

**Spec:**
```
Type:       Plugin (Godot editor plugin)
Data model: Quest(id, title, description, prerequisites)
            Objective(id, quest_id -> Quest, kind, target, amount)
            Reward(quest_id -> Quest, item, amount)
Features:   - Add a main screen tab to create quests
            - Add objectives like kill, collect and talk
            - Set prerequisites between quests
            - Save quests as Resource files
            - Provide a runtime QuestManager autoload
Storage:    Godot .tres resource files
Tech stack: GDScript, Godot 4 EditorPlugin API
```

---

## Example 467

**Intent:**
chrome extension for wholesale buyers that shows minimum order qty and price tiers on alibaba in my currency

**Spec:**
```
Type:       Browser extension (sourcing helper)
Features:   - Read price tiers and minimum order quantity from product pages
            - Convert prices to the user's currency
            - Calculate landed cost with shipping and duty estimates
            - Save suppliers to a comparison list
            - Export the list to CSV
API:        REST
            GET  https://api.frankfurter.app/latest?from=USD
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, Frankfurter API
```

---

## Example 468

**Intent:**
jira app that makes a weekly status report email for my stakeholders

**Spec:**
```
Type:       Plugin (Jira Cloud)
Features:   - Collect issues completed, started and blocked this week in a project
            - Summarize progress per epic
            - Build an HTML email with charts
            - Send it to a stakeholder list every Friday
            - Let the PM edit the summary before sending
API:        Jira REST
            GET  /rest/api/3/search?jql={jql}
Storage:    Forge storage API
Tech stack: Atlassian Forge, TypeScript, Forge scheduled triggers
```

---

## Example 469

**Intent:**
logseq plugin that shows a random old journal entry from this day years ago

**Spec:**
```
Type:       Plugin (Logseq)
Features:   - Find journal pages with the same day and month from past years
            - Show them in a sidebar "On this day" panel
            - Pick a random block when there are several
            - Open the original journal page on click
            - Run when the app starts
Tech stack: TypeScript, Logseq Plugin SDK
```

---

## Example 470

**Intent:**
i want firefox addon to save full pages as single html files for my research archive with tags

**Spec:**
```
Type:       Browser extension (page archiving)
Data model: SavedPage(id, url, title, tags, file_name, saved_at)
Features:   - Save the current page with images and styles inlined into one HTML file
            - Add tags and a note before saving
            - Keep an index of saved pages
            - Search saved pages by tag and title
            - Export the index as JSON
Storage:    IndexedDB, downloads folder
Tech stack: JavaScript, Firefox WebExtensions API, SingleFile core
```

---

## Example 471

**Intent:**
confluence plugin that converts a page into a quiz to test people read it

**Spec:**
```
Type:       Plugin (Confluence Cloud app)
Data model: Quiz(id, page_id, questions_json)
            QuizResult(quiz_id -> Quiz, account_id, score, taken_at)
Features:   - Generate multiple-choice questions from the page text
            - Let the page owner edit questions
            - Show a quiz button at the end of the page
            - Save each reader's score
            - Show the owner a results table
Storage:    Forge storage API
Tech stack: Atlassian Forge, TypeScript, React, LLM API
```

---

## Example 472

**Intent:**
trello power-up for a hiring board that shows candidate rating stars

**Spec:**
```
Type:       Plugin (Trello Power-Up)
Data model: Rating(card_id, member_id, stars, comment)
Features:   - Let each board member rate a candidate card from 1 to 5 stars
            - Show the average rating as a card badge
            - Hide others' ratings until a member has rated
            - Show all ratings and comments on the card back
            - Sort a list by average rating
Storage:    Trello pluginData
Tech stack: JavaScript, Trello Power-Up client library
```

---

## Example 473

**Intent:**
zoom app for a church to show song lyrics to everyone in the meeting

**Spec:**
```
Type:       Plugin (Zoom App)
Data model: Song(id, title, verses_json)
            Setlist(id, meeting_id, song_ids)
Features:   - Let the leader build a setlist from a song library
            - Show the current verse to all participants
            - Move to the next verse with one click
            - Show lyrics in large text with a dark background
            - Import songs from text files
API:        WebSocket
            /ws/lyrics/{meeting_id}
Storage:    PostgreSQL
Tech stack: TypeScript, Zoom Apps SDK, React, Node.js
```

---

## Example 474

**Intent:**
chrome ext that adds a "copy as markdown" for tables on any website

**Spec:**
```
Type:       Browser extension (table copy)
Features:   - Detect HTML tables on the page
            - Add a copy button on hover
            - Convert the table to a Markdown table
            - Also offer CSV and TSV formats
            - Handle merged cells by repeating values
Tech stack: JavaScript, Chrome Extension Manifest V3, Turndown
```

---

## Example 475

**Intent:**
home assistant card showing the electricity price for each hour today as bars

**Spec:**
```
Type:       Plugin (Home Assistant Lovelace card)
Features:   - Read hourly prices from a sensor's attributes
            - Draw bars for each hour with the current hour highlighted
            - Color cheap and expensive hours
            - Show the cheapest 3-hour window
            - Show tomorrow's prices when available
Tech stack: TypeScript, Lit, ApexCharts
```

---

## Example 476

**Intent:**
blender addon that makes a city block from simple settings

**Spec:**
```
Type:       Plugin (Blender add-on)
Features:   - Generate a grid of streets and lots
            - Place buildings with random heights and footprints
            - Add window patterns with a procedural material
            - Add sidewalks and street lights
            - Set seed, density and size in a panel
Tech stack: Python, Blender bpy API, Geometry Nodes
```

---

## Example 477

**Intent:**
unity editor tool for dialogue voice lines: checks each line has an audio file

**Spec:**
```
Type:       Plugin (Unity editor extension)
Data model: DialogueLine(id, character, text, audio_clip)
Features:   - Read dialogue lines from the project's dialogue assets
            - Match each line ID with an audio file in a folder
            - List lines without audio and audio without lines
            - Assign matching clips automatically
            - Export a recording script CSV for missing lines
Tech stack: C#, Unity Editor API
```

---

## Example 478

**Intent:**
discord bot to help our server run a weekly photo contest

**Spec:**
```
Type:       Bot (Discord)
Data model: Contest(id, guild_id, theme, starts_at, ends_at)
            Entry(id, contest_id -> Contest, user_id, image_url)
            Vote(entry_id -> Entry, voter_id)
Features:   - Announce a weekly theme
            - Accept one image entry per member
            - Open voting with buttons on each entry
            - Prevent voting for own entry
            - Announce winners and give a winner role
Storage:    PostgreSQL
Tech stack: TypeScript, discord.js
```

---

## Example 479

**Intent:**
raycast extension to quickly add expenses to my google sheet budget

**Spec:**
```
Type:       Plugin (Raycast extension)
Features:   - Open a form with amount, category and note
            - Append the expense to the budget sheet with today's date
            - Remember recent categories
            - Show this month's total per category
            - Undo the last entry
API:        Google Sheets REST
            POST /v4/spreadsheets/{id}/values/{range}:append
Tech stack: TypeScript, React, Raycast API, Google Sheets API
```

---

## Example 480

**Intent:**
obsidian plugin for students: turn lecture notes headings into a printable study guide with blank answers

**Spec:**
```
Type:       Plugin (Obsidian)
Features:   - Read headings and bullet points from the current note
            - Turn bold terms into blanks
            - Create a study guide note with questions from headings
            - Create an answer key note
            - Export both as PDF
Tech stack: TypeScript, Obsidian API
```

---

## Example 481

**Intent:**
grafana panel showing a gantt like timeline of batch jobs

**Spec:**
```
Type:       Plugin (Grafana panel)
Features:   - Read job name, start time, end time and status fields
            - Draw jobs as bars on a time axis
            - Color bars by status
            - Show job details on hover
            - Stack overlapping jobs in lanes
Tech stack: TypeScript, React, Grafana plugin SDK
```

---

## Example 482

**Intent:**
chrome extension that shows walk score and noise level for rental listings

**Spec:**
```
Type:       Browser extension (rental neighbourhood info)
Features:   - Detect the listing address on rental sites
            - Show walk, transit and bike scores
            - Show estimated noise level from road and airport maps
            - Show nearby grocery stores and parks count
            - Save notes about each listing
API:        REST
            GET  https://api.walkscore.com/score?address={address}&lat={lat}&lon={lon}
Storage:    chrome.storage.local
Tech stack: JavaScript, Chrome Extension Manifest V3, Walk Score API, OpenStreetMap Overpass API
```

---

