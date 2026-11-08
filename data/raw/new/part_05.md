## Example 1

**Intent:**
a tray app that reminds me to stand up every hour

**Spec:**
```
Type:       Desktop application (system tray)
Data model: Settings(interval_minutes, quiet_start, quiet_end, sound_enabled)
Features:   - Run in the system tray with a countdown in the tooltip
            - Show a desktop notification when the interval ends
            - Snooze a reminder for 10 minutes from the notification
            - Pause reminders during set quiet hours
            - Start automatically when the computer boots
Storage:    Local JSON settings file
Tech stack: Python, pystray, plyer (notifications)
```

---

## Example 2

**Intent:**
photo organiser for my messy pictures folder

**Spec:**
```
Type:       Desktop application (file organiser)
Data model: Photo(id, path, taken_at, camera_model, hash)
            Album(id, name)
            AlbumPhoto(album_id -> Album, photo_id -> Photo)
Features:   - Import a folder and read EXIF dates from every photo
            - Move photos into Year/Month folders
            - Detect exact duplicates by file hash
            - Show a thumbnail grid with a date timeline
            - Group photos into named albums
Storage:    SQLite (photo index), thumbnails cached on disk
Tech stack: C#, .NET 8, WPF, MetadataExtractor
```

---

## Example 3

**Intent:**
I want to make a puzzle game where you slide coloured tiles to match patterns, in the browser

**Spec:**
```
Type:       Browser game (puzzle)
Data model: Level(id, grid_size, start_tiles, target_pattern, par_moves)
Features:   - Render the tile grid on an HTML canvas
            - Slide a whole row or column with mouse drag or swipe
            - Check the grid against the target pattern after each move
            - Count moves and award 1-3 stars against par
            - Unlock the next level after a win
            - Save level progress between sessions
Storage:    Browser localStorage (progress and stars)
Tech stack: TypeScript, HTML5 Canvas, Vite
```

---

## Example 4

**Intent:**
simple markdown notes app for windows that works offline

**Spec:**
```
Type:       Desktop application (note-taking)
Data model: Note(id, title, body_markdown, folder_id -> Folder, updated_at)
            Folder(id, name)
Features:   - Create, edit and delete notes in a split editor and preview
            - Organise notes into folders
            - Search all notes by full text
            - Autosave while typing
            - Export a note to PDF or HTML
Storage:    Markdown files on disk, SQLite FTS5 search index
Tech stack: Electron, React, CodeMirror, markdown-it
```

---

## Example 5

**Intent:**
can u make a game where ur a little frog jumping between lily pads and the pads sink if u stay too long

**Spec:**
```
Type:       Browser game (platformer)
Features:   - Draw the pond and frog with animated sprites
            - Charge a jump by holding the space bar and release to leap
            - Sink each lily pad after a short timer once the frog lands
            - Detect collision between the frog and pads to decide landing or splash
            - Speed up pad sinking as the score grows
            - Show score and best score on a game-over screen
Storage:    Browser localStorage (best score)
Tech stack: JavaScript, Phaser 3
```

---

## Example 6

**Intent:**
Convert videos to mp4 by dragging them onto a window.

**Spec:**
```
Type:       Desktop application (media converter)
Data model: ConversionJob(id, source_path, output_path, preset, status, progress)
Features:   - Accept video files dropped onto the main window
            - Convert each file to H.264 MP4 with a chosen quality preset
            - Show a progress bar per file in a queue
            - Run up to two conversions in parallel
            - Open the output folder when the queue finishes
Tech stack: Python, PySide6, FFmpeg (via subprocess)
```

---

## Example 7

**Intent:**
My kids are 7 and 9 and they always fight about who gets to use the computer, and I'd love a little program that shows a timer for each of them, locks the screen when their time is up, and lets me (the parent) add extra time with a PIN. We run Windows at home.

**Spec:**
```
Type:       Desktop application (parental control)
Auth:       Parent PIN (hashed) to change settings or add time
Data model: Child(id, name, daily_minutes, used_minutes_today)
            Session(id, child_id -> Child, started_at, ended_at)
Features:   - Pick which child is using the computer at login
            - Show a floating countdown of remaining minutes
            - Lock the screen with a full-screen overlay when time runs out
            - Add extra minutes after entering the parent PIN
            - Reset each child's allowance at midnight
            - Show a weekly usage report per child
Storage:    SQLite database in the user's AppData folder
Tech stack: C#, .NET 8, WinForms
```

---

## Example 8

**Intent:**
idle game about growing a mushroom farm

**Spec:**
```
Type:       Browser game (idle)
Data model: SaveState(spores, mushrooms_per_second, upgrades_json, last_saved_at)
Features:   - Click to harvest mushrooms manually
            - Buy farm upgrades that raise mushrooms per second
            - Grow production while the tab is closed using the saved timestamp
            - Unlock new mushroom species at milestones
            - Autosave every 30 seconds
Storage:    Browser localStorage (save state)
Tech stack: JavaScript, Vue 3
```

---

## Example 9

**Intent:**
i need a screen recorder that records just one window and saves as gif

**Spec:**
```
Type:       Desktop application (screen recorder)
Features:   - Pick a window to record from a list of open windows
            - Capture frames at a chosen frame rate
            - Start and stop recording with a global hotkey
            - Trim the start and end before saving
            - Encode and save the clip as an optimised GIF
Tech stack: Python, mss (screen capture), PyQt6, imageio
```

---

## Example 10

**Intent:**
Hello, I want application for my small shop to make invoices without internet, I am in Kenya and connection is often down.

**Spec:**
```
Type:       Desktop application (offline business tool)
Data model: Customer(id, name, phone, address)
            Product(id, name, unit_price, stock)
            Invoice(id, customer_id -> Customer, number, issued_at, total)
            InvoiceLine(id, invoice_id -> Invoice, product_id -> Product, quantity, price)
Features:   - Add and edit customers and products
            - Create an invoice by picking products and quantities
            - Calculate totals with VAT automatically
            - Print the invoice or save it as PDF
            - Reduce product stock when an invoice is saved
            - Back up the database to a USB drive
Storage:    SQLite local database
Tech stack: Java, JavaFX, JasperReports (PDF)
```

---

## Example 11

**Intent:**
a card game in godot where you build a deck of spells

**Spec:**
```
Type:       Desktop game (deck-building card game)
Data model: Card(id, name, cost, effect_type, power)
            RunSave(deck_card_ids, floor, health, gold)
Features:   - Deal a hand of 5 cards from the shuffled deck each turn
            - Play cards by spending mana to attack or shield
            - Run simple enemy AI that shows its next intended move
            - Offer a choice of 3 new cards after each victory
            - Save run progress between floors
Storage:    Local save file (Godot user:// JSON)
Tech stack: Godot 4, GDScript
```

---

## Example 12

**Intent:**
drawing app for kids

**Spec:**
```
Type:       Desktop application (drawing)
Features:   - Draw freehand with brushes in big bright colours
            - Fill closed areas with the paint bucket tool
            - Stamp fun shapes and stickers on the canvas
            - Undo and redo strokes
            - Save drawings as PNG to a gallery folder
Storage:    PNG files in a local Pictures subfolder
Tech stack: Python, Pygame
```

---

## Example 13

**Intent:**
quiz game for my class about world capitals that runs on the classroom projector

**Spec:**
```
Type:       Desktop game (quiz)
Data model: Question(id, country, capital, wrong_options, region)
            Team(id, name, score)
Features:   - Show a question with four answer buttons in large text
            - Run a countdown timer for each question
            - Let the teacher mark which team answered first
            - Keep a scoreboard for up to 6 teams
            - Filter questions by continent before starting
Storage:    Questions in a local CSV file
Tech stack: Python, Tkinter
```

---

## Example 14

**Intent:**
app launcher like spotlight but for linux

**Spec:**
```
Type:       Desktop application (launcher)
Data model: LaunchItem(id, name, exec_path, icon_path, launch_count)
Features:   - Open a search bar with a global hotkey
            - Index installed applications from .desktop files
            - Fuzzy-match the typed text against app names
            - Rank results by how often each app is launched
            - Run simple calculations typed into the bar
Storage:    SQLite (launch counts)
Tech stack: Rust, GTK4 (gtk-rs)
```

---

## Example 15

**Intent:**
hey so i do a podcast with my friend and we record on separate mics and the levels are always different, i want a little program where i drop both audio files in and it makes them the same loudness and lines them up, nothing fancy, i use a mac

**Spec:**
```
Type:       Desktop application (audio tool)
Features:   - Load two audio tracks by drag and drop
            - Measure loudness of each track in LUFS
            - Normalise both tracks to a target loudness of -16 LUFS
            - Align the tracks by cross-correlating a clap or shared sound
            - Export a mixed stereo WAV or MP3
Tech stack: Swift, SwiftUI, AVFoundation, FFmpeg
```

---

## Example 16

**Intent:**
multiplayer drawing guessing game for friends on phones

**Spec:**
```
Type:       Mobile game (multiplayer party)
Data model: Room(id, code, round, current_drawer_id)
            Player(id, room_id -> Room, nickname, score)
            Word(id, text, difficulty)
Features:   - Create a room and share a 4-letter join code
            - Give the drawer a secret word and a drawing canvas
            - Stream strokes to other players in real time
            - Let others type guesses and score faster correct guesses higher
            - Rotate the drawer each round and show a final leaderboard
Storage:    Redis (live rooms), PostgreSQL (word list)
Tech stack: Flutter, Node.js, Socket.IO
```

---

## Example 17

**Intent:**
tool that shrinks all my photos before i email them

**Spec:**
```
Type:       Desktop application (image resizer)
Features:   - Add photos by drag and drop or folder picker
            - Resize to a chosen maximum width and height keeping aspect ratio
            - Set JPEG quality with a slider and preview the file size
            - Strip EXIF location data on request
            - Save copies to an output folder without touching originals
Tech stack: Python, PyQt6, Pillow
```

---

## Example 18

**Intent:**
pygame space shooter but the ship can only shoot backwards

**Spec:**
```
Type:       Desktop game (shooter)
Features:   - Scroll the starfield background in a fixed game loop at 60 FPS
            - Fire bullets only behind the ship while enemies come from both sides
            - Detect sprite collisions between bullets, enemies and the ship
            - Spawn enemy waves that get faster every level
            - Play sound effects and background music
            - Save the high score to a local file
Storage:    Local JSON file (high scores)
Tech stack: Python, Pygame
```

---

## Example 19

**Intent:**
Clipboard history manager for Windows

**Spec:**
```
Type:       Desktop application (system tray)
Data model: ClipItem(id, content_type, text, image_path, copied_at, pinned)
Features:   - Record every text and image copied to the clipboard
            - Open a history popup with Ctrl+Shift+V
            - Search clipboard history by text
            - Pin items so they are never removed
            - Keep the last 500 items and delete older ones
Storage:    SQLite database, images saved as PNG files
Tech stack: C#, .NET 8, WPF
```

---

## Example 20

**Intent:**
me and my wife running a small bakery, we need program on computer for orders of cakes for birthdays, who ordered, when to pick up, what decoration. No internet needed.

**Spec:**
```
Type:       Desktop application (offline business tool)
Data model: Customer(id, name, phone)
            CakeOrder(id, customer_id -> Customer, flavour, size, decoration_notes, pickup_at, price, deposit_paid, status)
Features:   - Add cake orders with flavour, size and decoration notes
            - Show a calendar of upcoming pickups
            - Highlight orders due tomorrow
            - Mark deposits paid and orders collected
            - Print an order slip for the kitchen
Storage:    SQLite local database
Tech stack: Python, PySide6
```

---

## Example 21

**Intent:**
game where you sort recycling into the right bins before it falls

**Spec:**
```
Type:       Browser game (educational arcade)
Data model: Item(id, name, sprite, correct_bin)
Features:   - Drop rubbish items from the top of the screen at increasing speed
            - Move items left and right into paper, plastic, glass or general bins
            - Award points for correct bins and show a short fact on mistakes
            - End the game after three wrong sorts
            - Show a summary of which items were missorted
Storage:    Browser localStorage (high score)
Tech stack: JavaScript, HTML5 Canvas
```

---

## Example 22

**Intent:**
unity mobile game, you rotate a planet to catch falling meteors in craters

**Spec:**
```
Type:       Mobile game (arcade)
Features:   - Rotate the planet by swiping left and right
            - Spawn meteors along random paths toward the planet
            - Detect when a meteor lands in a crater versus hits the surface
            - Add new craters and faster meteors as levels progress
            - Store high score and unlocked planet skins locally
            - Show rewarded ads for an extra life
Storage:    Unity PlayerPrefs (high score and skins)
Tech stack: Unity, C#, Unity Ads
```

---

## Example 23

**Intent:**
music player that plays my local mp3 folder with nice ui

**Spec:**
```
Type:       Desktop application (media player)
Data model: Track(id, path, title, artist, album, duration, play_count)
            Playlist(id, name)
            PlaylistTrack(playlist_id -> Playlist, track_id -> Track, position)
Features:   - Scan a music folder and read ID3 tags
            - Browse by artist, album and song
            - Play, pause, skip and seek with a progress bar
            - Create and reorder playlists
            - Shuffle and repeat modes
            - Show album art from embedded tags
Storage:    SQLite library database
Tech stack: Electron, React, howler.js, music-metadata
```

---

## Example 24

**Intent:**
bulk rename files with rules

**Spec:**
```
Type:       Desktop application (file utility)
Features:   - Load files from a folder with a file-type filter
            - Build rename rules: find and replace, add prefix, add counter, change case
            - Preview old and new names side by side before applying
            - Apply the renames and undo the last batch
            - Save rule sets as presets
Storage:    Local JSON file (presets and undo log)
Tech stack: Rust, Tauri, Svelte
```

---

## Example 25

**Intent:**
wanna make a 2d platformer where gravity flips when you press a button

**Spec:**
```
Type:       Desktop game (platformer)
Data model: Level(id, tilemap_file, checkpoint_positions)
Features:   - Move and jump with keyboard or gamepad
            - Flip gravity upside down with a button press
            - Handle tile collision on floors and ceilings
            - Kill the player on spikes and respawn at the last checkpoint
            - Load levels from tilemap files
            - Show a level timer and best times
Storage:    Local save file (unlocked levels and best times)
Tech stack: Godot 4, GDScript, Tiled tilemaps
```

---

## Example 26

**Intent:**
soundboard app for streamers

**Spec:**
```
Type:       Desktop application (audio tool)
Data model: Sound(id, name, file_path, hotkey, volume)
            Board(id, name)
Features:   - Add sound clips to a grid of buttons
            - Play a clip by clicking or pressing its global hotkey
            - Set volume per clip
            - Route output to a chosen audio device such as a virtual cable
            - Switch between multiple boards
Storage:    Local JSON config file
Tech stack: C++, Qt 6, miniaudio
```

---

## Example 27

**Intent:**
i teach piano and want a program where students see notes on the screen and play them on a midi keyboard and it says if they were right

**Spec:**
```
Type:       Desktop application (music education)
Data model: Exercise(id, name, notes_sequence, tempo)
            Attempt(id, exercise_id -> Exercise, student_name, accuracy, played_at)
Features:   - Show notes on a scrolling staff
            - Read key presses from a connected MIDI keyboard
            - Mark each note green when correct and red when wrong
            - Calculate accuracy and timing score for the exercise
            - Save each student's attempts and show their progress
Storage:    SQLite local database
Tech stack: Python, mido (MIDI), PyQt6
```

---

## Example 28

**Intent:**
word puzzle game for phone

**Spec:**
```
Type:       Mobile game (word puzzle)
Data model: Puzzle(id, letters, valid_words, date)
            Progress(puzzle_id, found_words, hints_used)
Features:   - Show a wheel of 7 letters to connect by swiping
            - Check swiped words against a dictionary
            - Fill found words into a crossword-style grid
            - Give hints that reveal one letter
            - Release one new daily puzzle
Storage:    Local SQLite database
Tech stack: React Native, Expo
```

---

## Example 29

**Intent:**
timer for pomodoro in my menu bar mac

**Spec:**
```
Type:       Desktop application (menu bar)
Data model: Session(id, kind, started_at, duration_minutes, completed)
Features:   - Show the remaining time in the macOS menu bar
            - Run 25-minute work and 5-minute break cycles
            - Play a sound and notify when a cycle ends
            - Count completed pomodoros per day
            - Show a weekly chart of focus time
Storage:    Local SQLite database
Tech stack: Swift, SwiftUI (MenuBarExtra)
```

---

## Example 30

**Intent:**
board game for 2 players on the same computer where you place walls to trap the other one

**Spec:**
```
Type:       Desktop game (board game)
Features:   - Draw a 9x9 board with two pawns
            - Move a pawn one square or place a wall on your turn
            - Check with path-finding that a wall never fully blocks a player
            - Win when your pawn reaches the opposite side
            - Undo the last move
Tech stack: Java, LibGDX
```

---

## Example 31

**Intent:**
I'm a wedding photographer and after every wedding I have like 3000 photos and I need to go through them fast and pick the good ones, flagging and rating, then export the picks. Lightroom is too slow on my laptop for culling.

**Spec:**
```
Type:       Desktop application (photo culling)
Data model: Shoot(id, folder_path, imported_at)
            Photo(id, shoot_id -> Shoot, file_path, rating, flag, preview_path)
Features:   - Import a folder of RAW and JPEG files using embedded previews for speed
            - Step through photos full screen with arrow keys
            - Rate with number keys and flag picks or rejects
            - Compare two similar shots side by side
            - Filter by rating or flag
            - Copy or export the picked files to a new folder
Storage:    SQLite catalog, preview cache on disk
Tech stack: C++, Qt 6, LibRaw
```

---

## Example 32

**Intent:**
Write a drum machine program

**Spec:**
```
Type:       Desktop application (music)
Data model: Pattern(id, name, bpm, steps_json)
            Kit(id, name, sample_paths)
Features:   - Show a 16-step sequencer grid for 8 drum sounds
            - Play the pattern in a loop at a set BPM
            - Swap between drum kits made of WAV samples
            - Adjust swing and per-track volume
            - Save and load patterns
            - Export the loop to WAV
Storage:    Local JSON pattern files
Tech stack: C++, JUCE
```

---

## Example 33

**Intent:**
game to learn times tables for kids

**Spec:**
```
Type:       Browser game (educational)
Data model: PlayerProgress(table, correct_count, wrong_count, stars)
Features:   - Pick a times table from 1 to 12
            - Ask multiplication questions against a timer
            - Give stars and an animation for correct answers
            - Repeat questions the child got wrong more often
            - Show progress per table with stars
Storage:    Browser localStorage
Tech stack: HTML, CSS, JavaScript
```

---

## Example 34

**Intent:**
invetory app for my garage workshop tools no internet

**Spec:**
```
Type:       Desktop application (inventory)
Data model: Tool(id, name, category, location, condition, lent_to, photo_path)
Features:   - Add tools with category, shelf location and photo
            - Search tools by name or location
            - Mark a tool as lent to someone and when
            - List tools needing repair
            - Print labels with QR codes for shelves
Storage:    SQLite local database
Tech stack: Python, Tkinter, qrcode
```

---

## Example 35

**Intent:**
mobile idle game where you run a lighthouse and keep ships safe

**Spec:**
```
Type:       Mobile game (idle)
Data model: SaveState(coins, lamp_level, keepers, ships_saved, last_online_at)
Features:   - Earn coins automatically for each ship that passes safely
            - Upgrade the lamp, lens and fog horn to increase income
            - Hire keepers who work while offline
            - Trigger storm events that need tapping to keep the light on
            - Calculate offline earnings on return
Storage:    Local save file, cloud save via Google Play Games
Tech stack: Unity, C#
```

---

## Example 36

**Intent:**
whats a good way to make a desktop app that shows all my files by size so i can delete the big ones

**Spec:**
```
Type:       Desktop application (disk usage)
Features:   - Scan a drive or folder recursively in a background thread
            - Show folders as a treemap sized by disk usage
            - List the 100 largest files
            - Open the containing folder or move a file to trash
            - Filter by file type such as video or archives
Tech stack: Go, Fyne
```

---

## Example 37

**Intent:**
Je veux an app to make subtitles for my videos, i write in french and english

**Spec:**
```
Type:       Desktop application (video tool)
Data model: Project(id, video_path, language)
            Subtitle(id, project_id -> Project, start_ms, end_ms, text)
Features:   - Play the video with a waveform timeline
            - Add subtitle lines with start and end times by hotkey
            - Generate a first draft with speech recognition in French or English
            - Edit text and timing in a list
            - Export to SRT and VTT
Storage:    Local project files (JSON)
Tech stack: Python, PySide6, python-vlc, OpenAI Whisper (local)
```

---

## Example 38

**Intent:**
chess variant on a hexagon board for two players online in the browser

**Spec:**
```
Type:       Browser game (board game, multiplayer)
Data model: Game(id, white_player_id, black_player_id, moves, status)
            Player(id, nickname, rating)
Features:   - Draw a hexagonal board with piece sprites
            - Validate moves using hex-grid movement rules
            - Match two players by room link
            - Sync moves in real time
            - Detect check, checkmate and stalemate
            - Keep a move list and allow resign
Storage:    PostgreSQL (games and ratings)
Tech stack: TypeScript, PixiJS, Node.js, Socket.IO
```

---

## Example 39

**Intent:**
desktop timer for speedrunning with splits

**Spec:**
```
Type:       Desktop application (speedrun timer)
Data model: Run(id, game, category, attempts)
            Split(id, run_id -> Run, name, best_segment_ms, pb_time_ms)
Features:   - Start, split, undo split and reset with global hotkeys
            - Show each split with delta against personal best
            - Highlight gold splits in a different colour
            - Save personal bests and attempt count
            - Customise the layout and colours
Storage:    Local XML split files
Tech stack: C#, .NET, Avalonia UI
```

---

## Example 40

**Intent:**
an mp3 tag editor

**Spec:**
```
Type:       Desktop application (media utility)
Features:   - Load a folder of MP3 and FLAC files
            - Edit title, artist, album, year and track number in a table
            - Set album art for many files at once
            - Fill tags from file names using a pattern
            - Save changes back to the files
Tech stack: Python, PyQt6, mutagen
```

---

## Example 41

**Intent:**
dice rolling game for 2-4 players on one tablet

**Spec:**
```
Type:       Mobile game (party dice)
Features:   - Roll five dice with a shake gesture or button
            - Hold dice between up to three rolls
            - Score combinations on a shared scorecard
            - Pass the tablet between players with a turn screen
            - Show final ranking and confetti for the winner
Tech stack: Flutter, Flame engine
```

---

## Example 42

**Intent:**
hi, i am student from vietnam, i want make game about cooking pho for school project, player need put ingredients in right order and time

**Spec:**
```
Type:       Browser game (cooking)
Data model: Recipe(id, name, steps, time_limits)
            Customer(id, order_recipe_id -> Recipe, patience)
Features:   - Show customers arriving with a bowl order
            - Drag ingredients into the pot in the correct order
            - Run timers for broth and noodles that burn if left too long
            - Score each bowl by order and timing
            - Unlock new recipes after each day
Storage:    Browser localStorage (unlocked days)
Tech stack: JavaScript, Phaser 3
```

---

## Example 43

**Intent:**
secure password vault offline desktop

**Spec:**
```
Type:       Desktop application (password manager)
Auth:       Master password, key derived with Argon2id
Data model: Entry(id, title, username, password_encrypted, url, notes, updated_at)
Features:   - Lock and unlock the vault with a master password
            - Add, edit and delete login entries
            - Generate strong random passwords
            - Copy a password to the clipboard and clear it after 20 seconds
            - Lock automatically after inactivity
Storage:    Single encrypted vault file (AES-256-GCM)
Tech stack: Rust, Tauri, React
```

---

## Example 44

**Intent:**
escape room puzzle game in 3D

**Spec:**
```
Type:       Desktop game (puzzle, 3D)
Data model: SaveGame(room_id, inventory_items, solved_puzzles)
Features:   - Move in first person and inspect objects
            - Pick up items into an inventory and combine them
            - Solve lock puzzles with codes found in the room
            - Trigger door animations when puzzles are solved
            - Save progress per room
Storage:    Local save file
Tech stack: Unity, C#
```

---

## Example 45

**Intent:**
little app that shows weather on my desktop as a widget

**Spec:**
```
Type:       Desktop application (widget)
Features:   - Show current temperature and an icon in a small always-on-top window
            - Show a 3-day forecast on hover
            - Detect location from IP or a typed city
            - Refresh every 30 minutes
            - Let the user drag the widget and remember its position
Storage:    Local JSON settings
Tech stack: Electron, Open-Meteo API
```

---

## Example 46

**Intent:**
timelapse maker from a folder of photos

**Spec:**
```
Type:       Desktop application (video tool)
Features:   - Import a sequence of images sorted by name or date
            - Set frame rate and output resolution
            - Deflicker by averaging brightness between frames
            - Preview the timelapse before export
            - Render the video to MP4
Tech stack: Python, OpenCV, PySide6
```

---

## Example 47

**Intent:**
browser game like a maze where the walls move every 10 seconds

**Spec:**
```
Type:       Browser game (maze)
Features:   - Generate a random maze with depth-first search
            - Move the player with arrow keys using grid collision
            - Regenerate part of the maze every 10 seconds without trapping the player
            - Show a warning animation before walls shift
            - Track time to reach the exit
Storage:    Browser localStorage (best times)
Tech stack: JavaScript, HTML5 Canvas
```

---

## Example 48

**Intent:**
app to keep my recipes on my laptop with pictures

**Spec:**
```
Type:       Desktop application (recipe manager)
Data model: Recipe(id, title, ingredients, steps, servings, photo_path, tags)
Features:   - Add recipes with ingredients, steps and a photo
            - Search recipes by ingredient or tag
            - Scale ingredient amounts by number of servings
            - Print a recipe card
            - Import recipes from a pasted text block
Storage:    SQLite local database
Tech stack: Python, Flet
```

---

## Example 49

**Intent:**
tamagotchi style pet for the desktop that walks along the taskbar

**Spec:**
```
Type:       Desktop application (desktop pet)
Data model: PetState(name, hunger, happiness, energy, age_days, last_seen_at)
Features:   - Show an animated pet sprite in a transparent always-on-top window
            - Walk the pet along the bottom of the screen
            - Feed and play with the pet from a right-click menu
            - Lower hunger and happiness over time even while closed
            - Sleep when the user is idle
Storage:    Local JSON save file
Tech stack: C#, .NET 8, WPF (transparent window)
```

---

## Example 50

**Intent:**
ok so my dad has a small taxi company with 6 cars and he does everything on paper, who drove which car, the fuel, the money at end of day. he is not good with computers. i want simple program on his pc to write this down and see the month totals

**Spec:**
```
Type:       Desktop application (offline business tool)
Data model: Driver(id, name, phone)
            Car(id, plate, model)
            Shift(id, driver_id -> Driver, car_id -> Car, date, km_start, km_end, fuel_cost, cash_collected)
Features:   - Enter a shift with big simple forms
            - Calculate kilometres driven and net income per shift
            - Show monthly totals per driver and per car
            - Flag cars that are due for service by kilometres
            - Export the month to Excel
Storage:    SQLite local database
Tech stack: Python, PySide6, openpyxl
```

---

## Example 51

**Intent:**
rhythm game where you tap with the beat of your own songs

**Spec:**
```
Type:       Desktop game (rhythm)
Features:   - Load any MP3 or OGG file from disk
            - Detect beats with onset detection to create note charts
            - Scroll notes down four lanes in time with the audio
            - Judge hits as perfect, good or miss
            - Show combo, accuracy and a grade at the end
            - Save the best score per song
Storage:    Local JSON file (scores per song hash)
Tech stack: Python, Pygame, librosa
```

---

## Example 52

**Intent:**
screenshot tool that lets me draw arrows and blur stuff

**Spec:**
```
Type:       Desktop application (screenshot)
Features:   - Capture a region, a window or the full screen with a hotkey
            - Draw arrows, boxes and text on the screenshot
            - Blur or pixelate sensitive areas
            - Copy the result to the clipboard or save as PNG
            - Keep a history of recent screenshots
Tech stack: C++, Qt 6
```

---

## Example 53

**Intent:**
memory card matching game with animals for toddlers on ipad

**Spec:**
```
Type:       Mobile game (memory)
Features:   - Show a grid of face-down animal cards
            - Flip cards with a tap and play the animal sound
            - Keep matched pairs face up
            - Adjust grid size from 4 to 16 cards
            - Celebrate with an animation when all pairs are found
Tech stack: Swift, SpriteKit
```

---

## Example 54

**Intent:**
tray app that switches my audio output between headphones and speakers

**Spec:**
```
Type:       Desktop application (system tray)
Features:   - List all audio output devices in the tray menu
            - Switch the default output device with one click
            - Bind a global hotkey to cycle devices
            - Show a notification with the new device name
            - Start with Windows
Storage:    Local JSON settings
Tech stack: C#, .NET, NAudio
```

---

## Example 55

**Intent:**
tower defense where the towers are kitchen appliances

**Spec:**
```
Type:       Browser game (tower defense)
Data model: Level(id, path_points, waves_json, starting_money)
            Tower(id, name, cost, range, damage, fire_rate)
Features:   - Place toaster, blender and fridge towers on grid cells beside the path
            - Move ant enemies along waypoints with health bars
            - Fire projectiles at the nearest enemy in range
            - Earn coins per kill to buy and upgrade towers
            - Lose lives when enemies reach the pantry
            - Unlock levels after clearing all waves
Storage:    Browser localStorage (level progress)
Tech stack: TypeScript, Phaser 3
```

---

## Example 56

**Intent:**
Electron app to track how much time I spend in each program

**Spec:**
```
Type:       Desktop application (time tracker)
Data model: ActivitySample(id, app_name, window_title, started_at, duration_s)
            Category(id, name, app_patterns)
Features:   - Record the active window every 5 seconds in the background
            - Pause tracking when the user is idle for 5 minutes
            - Assign apps to categories like work, social and games
            - Show daily and weekly charts per app and category
            - Export activity to CSV
Storage:    SQLite local database
Tech stack: Electron, active-win, better-sqlite3, Chart.js
```

---

## Example 57

**Intent:**
font viewer

**Spec:**
```
Type:       Desktop application (font manager)
Features:   - List installed and folder fonts with a live preview
            - Type custom preview text and change the size
            - Compare up to four fonts side by side
            - Show glyph map and font metadata
            - Filter fonts by serif, sans, mono or script
Tech stack: Python, PySide6, fontTools
```

---

## Example 58

**Intent:**
i make youtube videos and want a tool that cuts out the silent parts automatically

**Spec:**
```
Type:       Desktop application (video editing)
Features:   - Load a video file and extract its audio track
            - Detect silent sections below a loudness threshold
            - Show detected cuts on a timeline for review
            - Adjust padding around kept speech
            - Export the trimmed video or an XML edit list for Premiere and Resolve
Tech stack: Python, FFmpeg, PySide6, pydub
```

---

## Example 59

**Intent:**
snake but there are two snakes on one keyboard

**Spec:**
```
Type:       Desktop game (local multiplayer arcade)
Features:   - Control two snakes with WASD and arrow keys on a shared grid
            - Spawn food that grows whichever snake eats it
            - Kill a snake that hits a wall, itself or the other snake
            - Play best of five rounds
            - Show round wins for each player
Tech stack: C, raylib
```

---

## Example 60

**Intent:**
offline app to keep patient appointments for my physio clinic, 2 computers

**Spec:**
```
Type:       Desktop application (offline business tool)
Auth:       Staff login with username and password (bcrypt)
Data model: Patient(id, name, phone, birth_date, notes)
            Therapist(id, name)
            Appointment(id, patient_id -> Patient, therapist_id -> Therapist, starts_at, duration_min, status)
Features:   - Book, move and cancel appointments in a weekly calendar view
            - Prevent double booking of a therapist
            - Keep treatment notes per patient visit
            - Print a daily schedule
            - Share the database between two PCs on the local network
Storage:    PostgreSQL on one office PC, accessed over the LAN
Tech stack: C#, .NET 8, WPF, Npgsql
```

---

## Example 61

**Intent:**
platformer where you are a candle and you melt over time

**Spec:**
```
Type:       Desktop game (platformer)
Features:   - Shrink the candle sprite as wax melts every second
            - Refill wax at checkpoints on candle holders
            - Light torches to open doors and reveal platforms
            - Put out the flame instantly in water
            - Use tile collision and coyote-time jumping
            - Rank levels by remaining wax
Storage:    Local save file (level records)
Tech stack: Godot 4, GDScript
```

---

## Example 62

**Intent:**
bird sounds quiz app

**Spec:**
```
Type:       Mobile game (quiz)
Data model: Bird(id, name, audio_file, image_file, region)
            QuizResult(id, score, region, played_at)
Features:   - Play a bird call and offer four photo answers
            - Filter birds by region
            - Reveal the bird's name and a fun fact after each answer
            - Keep a list of birds the player keeps missing
            - Show past quiz scores
Storage:    Local SQLite, bundled audio assets
Tech stack: Kotlin, Jetpack Compose, ExoPlayer
```

---

## Example 63

**Intent:**
make me a solitaire style card game but original

**Spec:**
```
Type:       Browser game (solitaire card game)
Features:   - Deal cards into a ring of seven piles around a centre
            - Move cards onto the centre pile when they are one rank higher or lower
            - Draw from the stock when no moves remain
            - Detect when no moves are left and end the round
            - Score by cards cleared and remaining time
            - Animate card movement and flips
Storage:    Browser localStorage (stats)
Tech stack: JavaScript, HTML, CSS (DOM cards)
```

---

## Example 64

**Intent:**
system tray thing that shows my cpu temp

**Spec:**
```
Type:       Desktop application (system tray)
Features:   - Read CPU and GPU temperature sensors every 2 seconds
            - Show the current temperature as a tray icon number
            - Change icon colour above warning thresholds
            - Show a small graph of the last 10 minutes on click
            - Notify when temperature stays above the limit
Tech stack: C#, .NET, LibreHardwareMonitor
```

---

## Example 65

**Intent:**
I'd like to build a jigsaw puzzle program where you can load your own photo and it cuts it into pieces.

**Spec:**
```
Type:       Desktop game (jigsaw puzzle)
Features:   - Load any image and cut it into 24 to 500 pieces with tab shapes
            - Scatter pieces around the board
            - Drag pieces and snap them together when they fit
            - Rotate pieces in hard mode
            - Save an unfinished puzzle and continue later
Storage:    Local save files (piece positions as JSON)
Tech stack: Python, Pygame, Pillow
```

---

## Example 66

**Intent:**
hi my mom is 70 and she likes crosswords, can i make app on her tablet with big letters

**Spec:**
```
Type:       Mobile game (crossword)
Data model: Puzzle(id, grid, clues, solution)
            Progress(puzzle_id, filled_cells, completed)
Features:   - Show the crossword with extra-large cells and fonts
            - Highlight the current clue and word
            - Type with a large on-screen keyboard
            - Reveal one letter or check the word on request
            - Bundle 100 puzzles and remember progress
Storage:    Local SQLite database
Tech stack: Flutter
```

---

## Example 67

**Intent:**
tauri app to batch convert images between png jpg webp

**Spec:**
```
Type:       Desktop application (image converter)
Features:   - Drop images or a folder into the window
            - Choose output format PNG, JPEG, WebP or AVIF
            - Set quality and optional max dimensions
            - Convert files in parallel with a progress list
            - Keep original filenames in the output folder
Tech stack: Tauri, Rust (image crate), Svelte
```

---

## Example 68

**Intent:**
game about running a tiny post office, sorting letters by postcode

**Spec:**
```
Type:       Browser game (time management)
Features:   - Show letters arriving on a conveyor belt with postcodes
            - Drag each letter into the matching district box
            - Speed up the belt each in-game day
            - Add special parcels that need a stamp first
            - Pay the player and buy upgrades between days
            - Save the current day
Storage:    Browser localStorage
Tech stack: TypeScript, PixiJS
```

---

## Example 69

**Intent:**
screen ruler and color picker tool

**Spec:**
```
Type:       Desktop application (designer utility)
Features:   - Show a draggable on-screen ruler in pixels
            - Pick any colour on screen with a magnifier
            - Copy colours as HEX, RGB or HSL
            - Keep a history of picked colours
            - Toggle tools with global hotkeys
Tech stack: Electron
```

---

## Example 70

**Intent:**
im blind in one eye and get headaches from screens, i want a thing that dims the screen and makes it warmer at night and reminds me to look away every 20 min

**Spec:**
```
Type:       Desktop application (eye care)
Data model: Settings(day_temperature_k, night_temperature_k, sunset_time, break_interval_min)
Features:   - Shift screen colour temperature warmer after sunset
            - Dim brightness with an overlay or gamma adjustment
            - Show a 20-20-20 reminder every 20 minutes
            - Count down a 20-second look-away break
            - Disable temporarily for one hour from the tray
Storage:    Local JSON settings
Tech stack: Python, pystray, Windows gamma ramp API (ctypes)
```

---

## Example 71

**Intent:**
pixel art editor

**Spec:**
```
Type:       Desktop application (drawing)
Data model: Sprite(id, width, height, palette, frames)
Features:   - Draw on a zoomable pixel grid with pencil, eraser and fill
            - Use limited colour palettes
            - Add animation frames with onion skin
            - Preview the animation at a set FPS
            - Export to PNG, sprite sheet or GIF
Storage:    Local project files (JSON)
Tech stack: C++, SDL2, Dear ImGui
```

---

## Example 72

**Intent:**
trivia game i can play with my family on the tv, phones are the buzzers

**Spec:**
```
Type:       Browser game (party quiz)
Data model: Room(id, code, state, question_index)
            Player(id, room_id -> Room, name, score)
            Question(id, text, options, answer, category)
Features:   - Show questions on the TV browser as the host screen
            - Join from phones with a room code to use them as buzzers
            - Lock in the first buzz and accept or reject the answer
            - Track scores and show a leaderboard between rounds
            - Pick categories before the game
Storage:    In-memory rooms, questions in a JSON file
Tech stack: Node.js, Socket.IO, Svelte
```

---

## Example 73

**Intent:**
Desktop app where I can track my reading, books and pages per day.

**Spec:**
```
Type:       Desktop application (reading tracker)
Data model: Book(id, title, author, total_pages, status, started_at, finished_at)
            ReadingLog(id, book_id -> Book, date, pages_read)
Features:   - Add books with title, author and page count
            - Log pages read each day
            - Show progress bars for current books
            - Show a yearly goal and books finished
            - Chart pages per day over the month
Storage:    SQLite local database
Tech stack: Python, Tkinter, matplotlib
```

---

## Example 74

**Intent:**
unreal engine racing game with small toy cars on a kitchen table

**Spec:**
```
Type:       Desktop game (racing, 3D)
Features:   - Drive toy cars with arcade physics on tabletop tracks
            - Place checkpoints to validate laps
            - Race against AI cars that follow splines
            - Show lap times and position
            - Support local split-screen for two players
            - Save best lap per track
Storage:    Local save game slots
Tech stack: Unreal Engine 5, C++, Blueprints
```

---

## Example 75

**Intent:**
app to tidy downloads folder automatically

**Spec:**
```
Type:       Desktop application (file organiser)
Data model: Rule(id, extension_pattern, target_folder, age_days)
Features:   - Watch the Downloads folder for new files
            - Move files to folders by type using rules
            - Delete installers older than a set number of days
            - Show a log of moved files
            - Undo the last move from the tray menu
Storage:    Local JSON rules file
Tech stack: Python, watchdog, pystray
```

---

## Example 76

**Intent:**
plz i need game for learning english words for kids in my country, picture and they choose the word, we use old android phones

**Spec:**
```
Type:       Mobile game (educational)
Data model: Word(id, text, image_file, audio_file, level)
            Progress(word_id, times_correct)
Features:   - Show a picture and three word choices
            - Play the spoken word after each answer
            - Move to harder levels after 10 correct answers
            - Work fully offline with small bundled images
            - Give stars and badges for streaks
Storage:    Local SQLite database
Tech stack: Kotlin, Android Views (minSdk 21)
```

---

## Example 77

**Intent:**
An audio recorder for dictation with timestamps and bookmarks.

**Spec:**
```
Type:       Desktop application (audio recorder)
Data model: Recording(id, file_path, title, created_at, duration_s)
            Bookmark(id, recording_id -> Recording, time_s, label)
Features:   - Record from the chosen microphone with level meter
            - Pause and resume within one recording
            - Add bookmarks with a hotkey while recording
            - Play back and jump to bookmarks
            - Save as MP3 or WAV
Storage:    Audio files on disk, SQLite index
Tech stack: C#, .NET, NAudio, WPF
```

---

## Example 78

**Intent:**
falling blocks game but the blocks are made of liquid

**Spec:**
```
Type:       Browser game (puzzle)
Features:   - Drop shapes made of liquid particles into a well
            - Simulate the liquid flowing with a cellular automaton
            - Clear rows that are fully filled with one colour
            - Mix colours when different liquids touch
            - Speed up as rows are cleared
Storage:    Browser localStorage (high score)
Tech stack: JavaScript, WebGL
```

---

## Example 79

**Intent:**
python script game, text adventure in a haunted house

**Spec:**
```
Type:       Desktop game (text adventure)
Data model: Room(id, description, exits, items)
            SaveGame(current_room, inventory, flags)
Features:   - Parse commands like go north, take key and use lamp
            - Describe rooms and items
            - Lock rooms until the right item is used
            - Add random ghost events
            - Save and load the game
Storage:    Local JSON save file
Tech stack: Python (standard library)
```

---

## Example 80

**Intent:**
kanban board desktop for my personal tasks

**Spec:**
```
Type:       Desktop application (task board)
Data model: Board(id, name)
            Column(id, board_id -> Board, name, position)
            Card(id, column_id -> Column, title, description, due_date, position)
Features:   - Create boards with custom columns
            - Drag cards between columns
            - Add due dates and colour labels
            - Search cards across boards
            - Archive finished cards
Storage:    SQLite local database
Tech stack: Electron, Vue 3, SortableJS
```

---

## Example 81

**Intent:**
game where u fly a paper plane through an office and avoid fans

**Spec:**
```
Type:       Mobile game (endless flyer)
Features:   - Glide the paper plane by tilting the phone
            - Generate office obstacles procedurally as the level scrolls
            - Push the plane with fan wind zones
            - Collect paper clips as coins
            - Unlock plane designs with coins
            - Save high score
Storage:    Local storage (PlayerPrefs)
Tech stack: Unity, C#
```

---

## Example 82

**Intent:**
duplicate file finder for my external drive

**Spec:**
```
Type:       Desktop application (file utility)
Features:   - Scan a drive and group files by size first
            - Hash same-size files with xxHash to confirm duplicates
            - List duplicate groups with paths and sizes
            - Select which copies to keep with auto-select rules
            - Move unwanted copies to the recycle bin
Tech stack: Go, Wails, React
```

---

## Example 83

**Intent:**
board game about trading spices between islands for 2 to 4 players, hotseat on pc

**Spec:**
```
Type:       Desktop game (board game, hotseat)
Data model: GameState(turn, current_player, island_prices, players_json)
Features:   - Draw an island map with ports and sea routes
            - Move ships along routes and buy or sell spices at ports
            - Change prices when players trade
            - Draw random event cards like storms and pirates
            - Win by reaching a gold target
            - Save and resume a game
Storage:    Local JSON save file
Tech stack: C#, MonoGame
```

---

## Example 84

**Intent:**
video player that remembers where I stopped in every file

**Spec:**
```
Type:       Desktop application (media player)
Data model: PlaybackPosition(file_hash, file_path, position_s, duration_s, updated_at)
Features:   - Play common video formats with hardware decoding
            - Resume each file from where it was stopped
            - Show a recently watched list with progress bars
            - Load subtitles and switch audio tracks
            - Control speed and skip with keyboard shortcuts
Storage:    SQLite local database
Tech stack: C++, Qt 6, libmpv
```

---

## Example 85

**Intent:**
guitar tuner for my laptop

**Spec:**
```
Type:       Desktop application (music utility)
Features:   - Listen to the microphone input
            - Detect pitch with autocorrelation
            - Show the nearest note and cents off on a needle
            - Support standard and drop D tunings
            - Play reference tones
Tech stack: Python, sounddevice, NumPy, PyQt6
```

---

## Example 86

**Intent:**
Hello! I am a teacher in Brazil. I want a game where students answer math questions to move a car in a race, all students on same computer screen, two teams.

**Spec:**
```
Type:       Desktop game (educational race)
Data model: Question(id, text, answer, difficulty)
Features:   - Show two cars on a race track, one per team
            - Display a math question for both teams at once
            - Move the team's car forward when they answer first and correctly
            - Let the teacher choose operation and difficulty
            - Declare the winner at the finish line
Storage:    Questions in a local JSON file
Tech stack: Python, Pygame
```

---

## Example 87

**Intent:**
wallpaper changer that uses my own photos

**Spec:**
```
Type:       Desktop application (system tray)
Features:   - Pick one or more folders of photos
            - Change the desktop wallpaper at a set interval
            - Choose shuffle or in-order mode
            - Skip to the next wallpaper from the tray
            - Fit, fill or centre images by aspect ratio
Storage:    Local JSON settings
Tech stack: Go, systray, Windows SystemParametersInfo API
```

---

## Example 88

**Intent:**
rpg about a librarian fighting monsters made of overdue books

**Spec:**
```
Type:       Desktop game (RPG)
Data model: Character(id, name, level, hp, xp, skills)
            Item(id, name, effect)
            SaveSlot(id, location, party_json, inventory_json)
Features:   - Explore library floors in a top-down tile map
            - Fight turn-based battles against book monsters
            - Learn new skills when levelling up
            - Equip and use items like bookmarks and coffee
            - Save at reading desks
Storage:    Local save slot files
Tech stack: Godot 4, GDScript
```

---

## Example 89

**Intent:**
a notes app that is encrypted

**Spec:**
```
Type:       Desktop application (note-taking)
Auth:       Passphrase unlock, key derived with scrypt
Data model: Note(id, title, body_encrypted, tags, updated_at)
Features:   - Unlock notes with a passphrase
            - Write notes in rich text
            - Encrypt every note with AES-GCM before saving
            - Tag and search decrypted notes in memory
            - Auto-lock after 5 minutes idle
Storage:    Encrypted SQLite database (SQLCipher)
Tech stack: Python, PySide6, SQLCipher
```

---

## Example 90

**Intent:**
game where you are a tiny robot vacuum cleaning a house

**Spec:**
```
Type:       Browser game (puzzle)
Data model: Level(id, layout, dirt_tiles, battery_limit)
Features:   - Program the robot's path with arrow commands before it runs
            - Play back the program step by step on a grid
            - Collect dirt tiles and avoid stairs and pets
            - Return to the dock before the battery runs out
            - Score levels by commands used
Storage:    Browser localStorage
Tech stack: TypeScript, HTML5 Canvas
```

---

## Example 91

**Intent:**
i want to make lofi beats on my computer

**Spec:**
```
Type:       Desktop application (music production)
Data model: Project(id, bpm, key, tracks_json)
Features:   - Sequence drum samples on a step grid
            - Play chords from a piano roll with a set key
            - Add vinyl crackle, low-pass and tape wobble effects
            - Loop sections and arrange them on a timeline
            - Export the song to WAV and MP3
Storage:    Local project files
Tech stack: C++, JUCE
```

---

## Example 92

**Intent:**
ebook reader for epub on linux

**Spec:**
```
Type:       Desktop application (ebook reader)
Data model: Book(id, path, title, author, cover_path, last_location)
            Highlight(id, book_id -> Book, cfi, text, note)
Features:   - Open and render EPUB files
            - Remember reading position per book
            - Change font, size and dark mode
            - Highlight text and add notes
            - Show a library grid with covers
Storage:    SQLite library database
Tech stack: Python, GTK4, WebKitGTK, ebooklib
```

---

## Example 93

**Intent:**
hangman with a twist where letters you guess wrong become enemies

**Spec:**
```
Type:       Browser game (word)
Features:   - Pick a secret word from a category list
            - Accept letter guesses from the keyboard
            - Spawn a walking letter enemy for every wrong guess
            - Let the player shoot enemies to win back lives
            - Reveal the word when solved or lost
Tech stack: JavaScript, Kaboom.js
```

---

## Example 94

**Intent:**
tool to merge and split pdfs on my computer

**Spec:**
```
Type:       Desktop application (PDF tool)
Features:   - Merge several PDFs in a chosen order
            - Split a PDF by page ranges
            - Rotate and delete pages with thumbnail previews
            - Reorder pages by drag and drop
            - Save the result as a new file
Tech stack: Python, PySide6, pypdf, PyMuPDF
```

---

## Example 95

**Intent:**
My brother and I want to make a co-op game where one player is a giant and the other is tiny and they have to help each other. We know some C#.

**Spec:**
```
Type:       Desktop game (co-op puzzle platformer)
Features:   - Control a giant and a tiny character with split controls on one keyboard or two gamepads
            - Let the giant lift and throw the tiny one
            - Let the tiny one crawl through vents to press switches
            - Design levels that need both abilities
            - Respawn both at shared checkpoints
Storage:    Local save file (level progress)
Tech stack: Unity, C#, Unity Input System
```

---

## Example 96

**Intent:**
an app that shows a big clock for when I'm presenting

**Spec:**
```
Type:       Desktop application (presentation timer)
Features:   - Show a full-screen countdown on a second monitor
            - Turn yellow at 5 minutes and red at 1 minute
            - Start, pause and reset with keyboard shortcuts
            - Show elapsed and remaining time
            - Set presets for common talk lengths
Storage:    Local JSON presets
Tech stack: Electron
```

---

## Example 97

**Intent:**
idle factory game on phone

**Spec:**
```
Type:       Mobile game (idle)
Data model: SaveState(cash, machines_json, research_points, last_online_at)
Features:   - Build conveyor machines that turn ore into products
            - Upgrade machine speed and output
            - Earn money while offline
            - Research new product lines
            - Prestige to reset with a permanent multiplier
Storage:    Local save file with cloud backup
Tech stack: Flutter, Flame
```

---

## Example 98

**Intent:**
tool to make thumbnails of all my videos in a contact sheet

**Spec:**
```
Type:       Desktop application (video utility)
Features:   - Pick a video file or a whole folder
            - Grab frames at evenly spaced times
            - Arrange frames in a grid with timestamps
            - Add file name, duration and resolution in a header
            - Save contact sheets as JPEG
Tech stack: Python, FFmpeg, Pillow, Tkinter
```

---

## Example 99

**Intent:**
fishing game where u catch fish and fill a museum

**Spec:**
```
Type:       Desktop game (casual fishing)
Data model: FishSpecies(id, name, rarity, season, location)
            Collection(species_id -> FishSpecies, caught_count, biggest_size)
Features:   - Cast the line and play a timing minigame to reel in
            - Spawn fish by location, time of day and season
            - Donate one of each fish to fill museum displays
            - Sell extra fish to buy better rods
            - Save the collection and money
Storage:    Local save file
Tech stack: Godot 4, C#
```

---

## Example 100

**Intent:**
c++ app to view 3d models stl obj

**Spec:**
```
Type:       Desktop application (3D viewer)
Features:   - Open STL, OBJ and PLY files
            - Orbit, pan and zoom with the mouse
            - Toggle wireframe and solid shading
            - Show model size and triangle count
            - Take a screenshot of the view
Tech stack: C++, Qt 6, OpenGL, Assimp
```

---

## Example 101

**Intent:**
launcher for my retro emulators and roms

**Spec:**
```
Type:       Desktop application (game launcher)
Data model: Emulator(id, name, exe_path, args)
            Rom(id, path, title, system, cover_path, play_count, last_played)
Features:   - Scan ROM folders and detect the system by file extension
            - Download cover art from an online database
            - Launch ROMs with the matching emulator
            - Browse with a gamepad in a full-screen mode
            - Track play count and recently played
Storage:    SQLite library database
Tech stack: C#, .NET, Avalonia UI, SDL2 (gamepad)
```

---

## Example 102

**Intent:**
shop simulator where you run a plant nursery

**Spec:**
```
Type:       Desktop game (simulation)
Data model: Plant(id, species, growth_stage, water_level, price)
            Customer(id, wanted_species, budget)
Features:   - Plant seeds and water them in pots
            - Grow plants through stages over in-game days
            - Serve customers who ask for specific plants
            - Set prices and buy more shelves
            - Handle pests that hurt unwatered plants
Storage:    Local save file
Tech stack: Unity, C#
```

---

## Example 103

**Intent:**
a quick note popup on hotkey

**Spec:**
```
Type:       Desktop application (quick capture)
Data model: QuickNote(id, text, created_at)
Features:   - Open a small note window with a global hotkey
            - Save the note on Enter and hide the window
            - List all quick notes in a searchable view
            - Copy a note back to the clipboard
            - Export notes to a text file
Storage:    SQLite local database
Tech stack: Rust, Tauri, SolidJS
```

---

## Example 104

**Intent:**
tic tac toe on a 3d cube for my browser

**Spec:**
```
Type:       Browser game (board game, 3D)
Features:   - Render a 4x4x4 cube grid in 3D
            - Rotate the cube with the mouse
            - Place X or O by clicking a cell
            - Check all 76 winning lines
            - Play against a minimax AI with depth limit
Tech stack: JavaScript, Three.js
```

---

## Example 105

**Intent:**
write in pygame a game where you are a bee pollinating flowers before winter

**Spec:**
```
Type:       Desktop game (arcade)
Features:   - Fly the bee with arrow keys over a scrolling meadow
            - Pollinate flowers by touching them to grow the hive
            - Avoid wasps and rain clouds
            - Run a season timer that ends at winter
            - Show hive size as the final score
Storage:    Local text file (high score)
Tech stack: Python, Pygame
```

---

## Example 106

**Intent:**
mobile puzzle where you connect pipes to water a garden

**Spec:**
```
Type:       Mobile game (puzzle)
Data model: Level(id, grid, pipe_tiles, source_cells, plant_cells, move_limit)
Features:   - Rotate pipe tiles by tapping
            - Flow water from the source along connected pipes
            - Water all plants to complete the level
            - Limit taps per level for three stars
            - Unlock garden worlds with new pipe types
Storage:    Local save data
Tech stack: Godot 4, GDScript (Android and iOS export)
```

---

## Example 107

**Intent:**
sticky notes on the desktop

**Spec:**
```
Type:       Desktop application (sticky notes)
Data model: StickyNote(id, text, colour, x, y, width, height, always_on_top)
Features:   - Create sticky notes that float on the desktop
            - Change the colour and size of each note
            - Remember note positions after restart
            - Pin notes above other windows
            - Search and restore hidden notes
Storage:    Local JSON file
Tech stack: Electron
```

---

## Example 108

**Intent:**
hey i run a dog grooming place and want a simple program for clients and their dogs and what we did last time

**Spec:**
```
Type:       Desktop application (offline business tool)
Data model: Client(id, name, phone)
            Dog(id, client_id -> Client, name, breed, notes)
            Visit(id, dog_id -> Dog, date, services, price, groomer)
Features:   - Add clients and their dogs
            - Record each grooming visit with services and price
            - Show the last visit and notes when a dog is selected
            - Find dogs due for a groom after 8 weeks
            - Print a simple receipt
Storage:    SQLite local database
Tech stack: Python, PySide6
```

---

## Example 109

**Intent:**
browser game where you defend a castle by drawing shapes with the mouse

**Spec:**
```
Type:       Browser game (action)
Features:   - Spawn enemies marching toward the castle with shape symbols above them
            - Recognise mouse-drawn shapes with a $1 gesture recogniser
            - Destroy enemies whose symbol matches the drawn shape
            - Add bosses that need sequences of shapes
            - Track score and waves survived
Storage:    Browser localStorage
Tech stack: JavaScript, HTML5 Canvas, $1 Unistroke Recognizer
```

---

## Example 110

**Intent:**
I want to make my own little music player for vinyl rips in FLAC that shows big album covers and nothing else, on Linux, maybe Rust because I'm learning it.

**Spec:**
```
Type:       Desktop application (media player)
Data model: Album(id, title, artist, year, cover_path, folder_path)
            Track(id, album_id -> Album, title, number, path)
Features:   - Scan a music folder and group FLAC tracks into albums
            - Show a full-screen grid of album covers
            - Play an album gaplessly
            - Control playback with media keys
            - Show the current track over the cover
Storage:    SQLite library index
Tech stack: Rust, egui, symphonia (FLAC decoding), rodio
```

---

## Example 111

**Intent:**
Make an app to resize and watermark product photos for my online shop.

**Spec:**
```
Type:       Desktop application (image batch tool)
Features:   - Load a folder of product photos
            - Resize to square 1200x1200 with white padding
            - Add a logo watermark with chosen opacity and corner
            - Rename files with a SKU prefix
            - Export to JPEG in an output folder
Tech stack: C#, .NET 8, ImageSharp, WinForms
```

---

## Example 112

**Intent:**
online card game for 4 players where you bid and play tricks, original rules

**Spec:**
```
Type:       Browser game (trick-taking card game, multiplayer)
Data model: Table(id, code, dealer_seat, round, trump_suit)
            Seat(id, table_id -> Table, player_name, bid, tricks_won, score)
Features:   - Seat four players at a table with a share link
            - Deal 13 cards and run a bidding round
            - Enforce follow-suit rules and decide each trick winner
            - Score bids against tricks won
            - Replace disconnected players with a simple bot
Storage:    Redis (live tables)
Tech stack: TypeScript, React, Node.js, Colyseus
```

---

## Example 113

**Intent:**
little game in lua where you stack cats

**Spec:**
```
Type:       Desktop game (physics stacking)
Features:   - Drop cat sprites from a swinging crane
            - Simulate stacking with 2D rigid body physics
            - End the game when a cat falls off the platform
            - Raise the camera as the tower grows
            - Save the tallest tower height
Storage:    Local save file
Tech stack: Lua, LÖVE (love2d), Box2D
```

---

## Example 114

**Intent:**
macro recorder for repetitive clicks

**Spec:**
```
Type:       Desktop application (automation)
Data model: Macro(id, name, events_json, hotkey, repeat_count)
Features:   - Record mouse clicks, movement and key presses
            - Play back a macro with a hotkey
            - Set repeat count and speed
            - Add delays and edit steps in a list
            - Stop playback instantly with Esc
Storage:    Local JSON macro files
Tech stack: Python, pynput, PyQt6
```

---

## Example 115

**Intent:**
game for my phone where you guess the year of old photos

**Spec:**
```
Type:       Mobile game (trivia)
Data model: Photo(id, image_url, year, caption, source)
            Round(id, score, played_at)
Features:   - Show a historic photo and a year slider
            - Score each guess by how close it is to the real year
            - Reveal the photo's story after each guess
            - Play five photos per round
            - Share the round score
Storage:    Local SQLite (photo pack and scores)
Tech stack: React Native, Expo
```

---

## Example 116

**Intent:**
sound effects generator for my game jam, like retro bleeps

**Spec:**
```
Type:       Desktop application (audio tool)
Features:   - Generate retro sounds from presets like jump, coin, explosion and laser
            - Tweak waveform, envelope, pitch slide and noise with sliders
            - Randomise or mutate a sound
            - Play the sound instantly on change
            - Export to WAV
Tech stack: C++, SDL2, Dear ImGui
```

---

## Example 117

**Intent:**
the app should help me learn typing faster, with stats

**Spec:**
```
Type:       Desktop application (typing tutor)
Data model: Lesson(id, title, text, level)
            Result(id, lesson_id -> Lesson, wpm, accuracy, errors_by_key, taken_at)
Features:   - Show lesson text and highlight the next character
            - Measure words per minute and accuracy
            - Show a heatmap of keys with most errors
            - Create practice drills from weak keys
            - Chart WPM progress over time
Storage:    SQLite local database
Tech stack: Python, Textual
```

---

## Example 118

**Intent:**
idle game where you train a pigeon army

**Spec:**
```
Type:       Browser game (idle)
Data model: SaveState(breadcrumbs, pigeons, coops, generals, last_tick_at)
Features:   - Tap to scatter breadcrumbs and recruit pigeons
            - Build coops that produce pigeons per second
            - Send pigeons on missions that return rewards after a timer
            - Unlock pigeon generals with passive bonuses
            - Calculate offline progress on load
Storage:    Browser localStorage
Tech stack: JavaScript, React
```

---

## Example 119

**Intent:**
window manager helper that snaps windows to a grid on windows 10

**Spec:**
```
Type:       Desktop application (window management)
Data model: Layout(id, name, zones_json, hotkey)
Features:   - Define custom grid layouts with zones
            - Snap the active window to a zone with a hotkey
            - Show zone overlay while dragging a window with Shift
            - Save layouts per monitor
            - Restore window positions after unplugging a monitor
Storage:    Local JSON layouts
Tech stack: C++, Win32 API
```

---

## Example 120

**Intent:**
math adventure game for grade 3, you open treasure chests by solving problems

**Spec:**
```
Type:       Browser game (educational adventure)
Data model: Problem(id, topic, question, answer, difficulty)
            Progress(island, chests_opened, coins)
Features:   - Walk a pirate around islands in a top-down view
            - Open chests by answering a math problem
            - Adjust difficulty to the child's success rate
            - Spend coins on hats and parrots
            - Show a progress report for parents
Storage:    Browser localStorage
Tech stack: TypeScript, Phaser 3
```

---

## Example 121

**Intent:**
offline gym membership software

**Spec:**
```
Type:       Desktop application (offline business tool)
Data model: Member(id, name, phone, photo_path, plan, expires_on)
            CheckIn(id, member_id -> Member, checked_in_at)
            Payment(id, member_id -> Member, amount, paid_at)
Features:   - Register members with photo and plan
            - Check members in by ID or barcode scan
            - Warn when a membership has expired
            - Record payments and renew plans
            - Show daily check-ins and monthly revenue
Storage:    SQLite local database
Tech stack: Java, JavaFX
```

---

## Example 122

**Intent:**
bro make a game where ur a shopping cart and u gotta collect stuff in a supermarket without crashing

**Spec:**
```
Type:       Mobile game (arcade)
Features:   - Steer the cart with on-screen joystick
            - Spawn shopping list items in random aisles
            - Detect collisions with shelves and other shoppers
            - Slow down the cart as it gets heavier
            - Score by items collected before the store closes
Storage:    Local high score storage
Tech stack: Unity, C#
```

---

## Example 123

**Intent:**
drag and drop app to make simple slideshows from photos with music

**Spec:**
```
Type:       Desktop application (video creation)
Features:   - Add photos and arrange them on a timeline
            - Apply pan-and-zoom and crossfade transitions
            - Add a music track and fit slide duration to it
            - Preview the slideshow
            - Render to 1080p MP4
Tech stack: Python, MoviePy, PySide6
```

---

## Example 124

**Intent:**
game where you guess what animal from just a small zoomed part of the picture, and it zooms out more each time

**Spec:**
```
Type:       Browser game (guessing)
Data model: Puzzle(id, image_url, answer, aliases)
Features:   - Show a tightly zoomed crop of an animal photo
            - Zoom out a step after each wrong guess
            - Accept typed answers with fuzzy matching and aliases
            - Score more points for fewer zoom steps
            - Give one new puzzle per day
Storage:    Puzzles in a JSON file, browser localStorage for streaks
Tech stack: HTML, CSS, JavaScript
```

---

## Example 125

**Intent:**
For the warehouse we need a desktop thing that prints barcode labels from a CSV

**Spec:**
```
Type:       Desktop application (label printing)
Features:   - Import a CSV and preview rows
            - Design a label layout with barcode, name and price
            - Generate Code 128 or EAN-13 barcodes
            - Print to a thermal label printer with a set label size
            - Print a quantity per row
Input:      CSV file with SKU, product name and price columns
Tech stack: C#, .NET 8, WPF, ZXing.Net
```

---

## Example 126

**Intent:**
3d marble rolling game, tilt the level

**Spec:**
```
Type:       Desktop game (3D physics puzzle)
Features:   - Tilt the board with mouse or arrow keys
            - Roll the marble with rigid body physics
            - Add holes, moving platforms and bumpers
            - Collect gems and reach the goal
            - Record best times per level
Storage:    Local save file
Tech stack: Godot 4, GDScript
```

---

## Example 127

**Intent:**
i need program to learn japanese kana with flashcards and spaced repetition

**Spec:**
```
Type:       Desktop application (flashcards)
Data model: Card(id, front, back, deck)
            Review(card_id -> Card, ease, interval_days, due_on, last_result)
Features:   - Show kana cards and reveal the romaji
            - Grade answers as again, hard, good or easy
            - Schedule reviews with the SM-2 algorithm
            - Play pronunciation audio
            - Show cards due today and retention stats
Storage:    SQLite local database
Tech stack: Python, PySide6
```

---

## Example 128

**Intent:**
browser extension... no wait, a desktop app that blocks distracting websites while i study

**Spec:**
```
Type:       Desktop application (focus blocker)
Data model: BlockList(id, name, domains)
            FocusSession(id, started_at, duration_min, completed)
Features:   - Edit lists of blocked domains
            - Start a focus session for a set time
            - Block domains by editing the hosts file during the session
            - Prevent stopping early unless a long phrase is typed
            - Show focus history
Storage:    Local JSON settings
Tech stack: Python, PyQt6 (runs with admin rights)
```

---

## Example 129

**Intent:**
a little racing game in the terminal

**Spec:**
```
Type:       Desktop game (terminal)
Features:   - Draw a scrolling road with ASCII characters
            - Steer left and right with arrow keys
            - Spawn other cars and oil spills
            - Detect collisions and end the run
            - Speed up over time and show the distance
Tech stack: Python, curses
```

---

## Example 130

**Intent:**
animation app for stop motion with my webcam

**Spec:**
```
Type:       Desktop application (stop motion)
Data model: Project(id, name, fps)
            Frame(id, project_id -> Project, index, image_path)
Features:   - Show the live webcam feed with onion skin of the last frame
            - Capture a frame with spacebar
            - Delete or reorder frames
            - Play back the animation at a set FPS
            - Export to MP4 or GIF
Storage:    Frames saved as PNG in a project folder
Tech stack: Python, OpenCV, PySide6
```

---

## Example 131

**Intent:**
game where you are an ant colony digging tunnels

**Spec:**
```
Type:       Desktop game (simulation)
Features:   - Dig tunnels in a 2D destructible soil grid
            - Assign ants to digging, foraging and nursing
            - Simulate ants following pheromone trails to food
            - Grow the queen's brood when food is stored
            - Defend against beetles that invade tunnels
            - Save and load colonies
Storage:    Local save files
Tech stack: C#, MonoGame
```

---

## Example 132

**Intent:**
weekly meal planner desktop with shopping list

**Spec:**
```
Type:       Desktop application (meal planner)
Data model: Recipe(id, name, ingredients_json)
            MealPlan(id, date, meal_slot, recipe_id -> Recipe)
Features:   - Drag recipes onto a weekly calendar
            - Generate a shopping list merging ingredients
            - Group the shopping list by store aisle
            - Print or copy the list
            - Reuse a previous week's plan
Storage:    SQLite local database
Tech stack: Electron, Svelte
```

---

## Example 133

**Intent:**
Need a timer program for my boxing classes with rounds and rest and loud bell.

**Spec:**
```
Type:       Desktop application (interval timer)
Data model: Workout(id, name, rounds, round_s, rest_s, warning_s)
Features:   - Set number of rounds, round length and rest length
            - Show a huge countdown readable from across the gym
            - Ring a bell at round start and end
            - Beep a warning 10 seconds before the end
            - Save workouts as presets
Storage:    Local JSON presets
Tech stack: Python, Pygame
```

---

## Example 134

**Intent:**
mobile game where you rotate a city block to guide a car home

**Spec:**
```
Type:       Mobile game (puzzle)
Features:   - Rotate square city tiles by tapping them
            - Drive the car automatically along connected roads
            - Fail the level if the car hits a dead end
            - Add one-way streets and traffic lights in later levels
            - Show stars for minimal rotations
Storage:    Local save data
Tech stack: Swift, SpriteKit
```

---

## Example 135

**Intent:**
something to make my home videos smaller without losing quality

**Spec:**
```
Type:       Desktop application (video compressor)
Features:   - Add videos by drag and drop
            - Re-encode with H.265 at a chosen CRF
            - Show estimated output size before encoding
            - Keep audio and metadata
            - Use GPU encoding when available
Tech stack: Python, PySide6, FFmpeg (libx265, NVENC)
```

---

## Example 136

**Intent:**
game for 2 players on 1 phone, air hockey

**Spec:**
```
Type:       Mobile game (local multiplayer)
Features:   - Split the screen into two halves for two thumbs
            - Track multi-touch paddles
            - Simulate puck physics with wall bounces
            - Score goals and play to 7
            - Add power-ups like double puck
Tech stack: Flutter, Flame, Forge2D
```

---

## Example 137

**Intent:**
i want a soft for making family tree on my pc, we are big family in Nigeria with many cousins

**Spec:**
```
Type:       Desktop application (genealogy)
Data model: Person(id, first_name, last_name, birth_date, death_date, photo_path, notes)
            Relationship(id, person_id -> Person, related_id -> Person, kind)
Features:   - Add family members with photos and dates
            - Link parents, children and spouses
            - Draw the tree as a zoomable diagram
            - Search for any relative
            - Export the tree to PDF for printing
Storage:    SQLite local database
Tech stack: Python, PySide6, Graphviz
```

---

## Example 138

**Intent:**
browser roguelike where each floor is a different season

**Spec:**
```
Type:       Browser game (roguelike)
Features:   - Generate dungeon floors with BSP room splitting
            - Change tiles, enemies and weather per season floor
            - Move turn by turn on a grid
            - Fight with bump attacks and pick up items
            - Permadeath with a run summary screen
Storage:    Browser localStorage (run history)
Tech stack: JavaScript, rot.js
```

---

## Example 139

**Intent:**
webcam app that takes a photo every time i sit with bad posture

**Spec:**
```
Type:       Desktop application (posture monitor)
Features:   - Read webcam frames every few seconds
            - Estimate head and shoulder position with pose detection
            - Compare against a calibrated good posture
            - Notify when bad posture lasts over a minute
            - Show daily posture score
Storage:    Local SQLite (posture log)
Tech stack: Python, OpenCV, MediaPipe, pystray
```

---

## Example 140

**Intent:**
a quiz maker for teachers that exports a quiz game to play offline

**Spec:**
```
Type:       Desktop application (quiz authoring)
Data model: Quiz(id, title)
            Question(id, quiz_id -> Quiz, text, options, correct_index, image_path)
Features:   - Create quizzes with multiple-choice questions and images
            - Reorder and preview questions
            - Export a quiz as a standalone HTML game file
            - Import questions from a spreadsheet
            - Show results at the end of the exported game
Storage:    SQLite local database
Tech stack: Electron, React
```

---

## Example 141

**Intent:**
pet hotel booking for my small business, mac

**Spec:**
```
Type:       Desktop application (offline business tool)
Data model: Owner(id, name, phone)
            Pet(id, owner_id -> Owner, name, species, needs)
            Booking(id, pet_id -> Pet, kennel_no, check_in, check_out, price)
Features:   - Show kennels on an occupancy calendar
            - Book pets into kennels for date ranges
            - Note feeding and medication needs
            - Print a daily care sheet
            - Calculate the bill on checkout
Storage:    Core Data (SQLite)
Tech stack: Swift, SwiftUI
```

---

## Example 142

**Intent:**
shooter but you can only move when you shoot

**Spec:**
```
Type:       Browser game (action)
Features:   - Aim with the mouse and fire to push the player backwards with recoil
            - Freeze player movement when not shooting
            - Spawn enemy waves in an arena
            - Detect bullet and enemy collisions
            - Manage limited ammo with pickups
Storage:    Browser localStorage (best wave)
Tech stack: TypeScript, Phaser 3
```

---

## Example 143

**Intent:**
desktop app that converts my handwritten note photos to text

**Spec:**
```
Type:       Desktop application (OCR)
Features:   - Import photos of handwritten pages
            - Straighten and enhance contrast
            - Run handwriting OCR on each page
            - Edit recognised text next to the image
            - Export to TXT or DOCX
Tech stack: Python, PySide6, OpenCV, TrOCR (Hugging Face)
```

---

## Example 144

**Intent:**
puzzle where you place mirrors to reflect lasers to targets

**Spec:**
```
Type:       Browser game (puzzle)
Data model: Level(id, grid, lasers, targets, mirror_count)
Features:   - Place and rotate mirrors on grid cells
            - Trace laser beams with reflection rules
            - Light all targets to win
            - Add colour filters and splitters
            - Save completed levels
Storage:    Browser localStorage
Tech stack: JavaScript, HTML5 Canvas
```

---

## Example 145

**Intent:**
car maintenance log for my cars

**Spec:**
```
Type:       Desktop application (vehicle log)
Data model: Vehicle(id, make, model, plate, odometer)
            ServiceRecord(id, vehicle_id -> Vehicle, date, odometer, type, cost, notes)
Features:   - Add vehicles with current mileage
            - Log services like oil changes and tyres
            - Remind when the next service is due by date or mileage
            - Show total cost per vehicle per year
            - Attach receipt photos
Storage:    SQLite local database
Tech stack: Python, Tkinter
```

---

## Example 146

**Intent:**
plateformer game in game maker where the hero is a sock lost in a washing machine

**Spec:**
```
Type:       Desktop game (platformer)
Features:   - Run and jump through spinning drum levels
            - Rotate the level around the player as the drum turns
            - Avoid soap bubbles and buttons
            - Find the matching sock at the end of each level
            - Collect lint as coins
Storage:    Local save (INI file)
Tech stack: GameMaker, GML
```

---

## Example 147

**Intent:**
virtual piano on my computer keyboard

**Spec:**
```
Type:       Desktop application (music)
Features:   - Map computer keys to two octaves of piano notes
            - Play sampled piano sounds with low latency
            - Show pressed keys on an on-screen keyboard
            - Shift octaves up and down
            - Record and play back a melody
Tech stack: JavaScript, Electron, Tone.js
```

---

## Example 148

**Intent:**
strategy game where you grow a forest and fight off loggers

**Spec:**
```
Type:       Desktop game (real-time strategy)
Features:   - Plant trees that spread seeds over the map
            - Gather sunlight and water as resources
            - Grow thorn bushes and animals to defend
            - Send waves of logger units toward the forest
            - Win by covering 70 percent of the map
Storage:    Local save files
Tech stack: Unity, C#
```

---

## Example 149

**Intent:**
a gif maker from video clips

**Spec:**
```
Type:       Desktop application (GIF maker)
Features:   - Open a video and pick start and end times on a timeline
            - Crop and resize the frame
            - Add caption text
            - Set frame rate and colour count
            - Export optimised GIF with gifski
Tech stack: Rust, Tauri, FFmpeg, gifski
```

---

## Example 150

**Intent:**
offline cash register for my small cafe with touchscreen

**Spec:**
```
Type:       Desktop application (point of sale)
Data model: MenuItem(id, name, category, price)
            Sale(id, total, payment_method, created_at)
            SaleLine(id, sale_id -> Sale, menu_item_id -> MenuItem, quantity, price)
Features:   - Show menu items as large touch buttons by category
            - Build an order and apply discounts
            - Take cash or card payments and calculate change
            - Print receipts to a thermal printer
            - Show end-of-day sales report
Storage:    SQLite local database
Tech stack: Electron, React, node-thermal-printer
```

---

## Example 151

**Intent:**
a mobile game to practise reading clocks for kids

**Spec:**
```
Type:       Mobile game (educational)
Features:   - Show an analog clock and ask what time it is
            - Let the child drag the clock hands to a given time
            - Start with o'clock and half past and add harder times
            - Reward correct answers with stickers
            - Read times aloud with text-to-speech
Storage:    Local storage (progress and stickers)
Tech stack: Flutter, flutter_tts
```

---

## Example 152

**Intent:**
minesweeper with hexagons

**Spec:**
```
Type:       Browser game (puzzle)
Features:   - Generate a hexagonal grid with randomly placed mines
            - Show the count of neighbouring mines on six sides
            - Flood-reveal empty cells
            - Flag suspected mines with right click
            - Guarantee the first click is safe
            - Track best times per difficulty
Storage:    Browser localStorage
Tech stack: TypeScript, SVG
```

---

## Example 153

**Intent:**
audiobook player

**Spec:**
```
Type:       Desktop application (media player)
Data model: Audiobook(id, title, author, folder_path, cover_path)
            Progress(audiobook_id -> Audiobook, chapter_index, position_s)
Features:   - Import audiobook folders and M4B files with chapters
            - Resume from the last position per book
            - Change playback speed without pitch change
            - Set a sleep timer
            - Add bookmarks with notes
Storage:    SQLite local database
Tech stack: Python, PySide6, python-vlc
```

---

## Example 154

**Intent:**
invoice maker freelance

**Spec:**
```
Type:       Desktop application (invoicing)
Data model: Client(id, name, email, address)
            Invoice(id, client_id -> Client, number, issued_on, due_on, status)
            LineItem(id, invoice_id -> Invoice, description, hours, rate)
Features:   - Store client details
            - Create invoices with hourly line items
            - Number invoices automatically
            - Generate a PDF with my logo
            - Mark invoices paid and list overdue ones
Storage:    SQLite local database
Tech stack: Python, Flet, ReportLab
```

---

## Example 155

**Intent:**
snowball fight game lan

**Spec:**
```
Type:       Desktop game (multiplayer, LAN)
Features:   - Host or join a match on the local network
            - Move characters in a top-down arena
            - Throw snowballs with travel time and collision detection
            - Build snow walls for cover
            - Play first to 10 hits
Tech stack: Godot 4, GDScript, ENet multiplayer
```

---

## Example 156

**Intent:**
color palette generator

**Spec:**
```
Type:       Desktop application (design tool)
Features:   - Generate 5-colour palettes from harmony rules
            - Lock colours and regenerate the rest
            - Extract a palette from an image
            - Check text contrast for accessibility
            - Export palettes as CSS, JSON or ASE
Storage:    Local JSON (saved palettes)
Tech stack: Electron, chroma.js
```

---

## Example 157

**Intent:**
sudoku but with letters

**Spec:**
```
Type:       Mobile game (logic puzzle)
Data model: Puzzle(id, grid, solution, difficulty, hidden_word)
Features:   - Generate 9x9 puzzles with nine letters instead of digits
            - Validate unique solutions with a backtracking solver
            - Reveal a hidden word along the diagonal when solved
            - Add pencil marks and undo
            - Offer easy, medium and hard
Storage:    Local SQLite
Tech stack: Kotlin, Jetpack Compose
```

---

## Example 158

**Intent:**
tray app mute mic hotkey

**Spec:**
```
Type:       Desktop application (system tray)
Features:   - Toggle the microphone mute with a global hotkey
            - Show a red or green tray icon for mute state
            - Show a small on-screen indicator when muted
            - Play a short sound on toggle
            - Start with the system
Tech stack: C#, .NET, NAudio (CoreAudio)
```

---

## Example 159

**Intent:**
bowling game 3d

**Spec:**
```
Type:       Desktop game (sports, 3D)
Features:   - Aim and set spin with the mouse
            - Simulate ball and pin physics
            - Score ten frames with strikes and spares
            - Support up to 4 local players
            - Show a replay of each throw
Tech stack: Unity, C#
```

---

## Example 160

**Intent:**
screen magnifier

**Spec:**
```
Type:       Desktop application (accessibility)
Features:   - Show a magnified lens that follows the mouse
            - Zoom from 2x to 10x with the scroll wheel
            - Invert colours for readability
            - Dock the magnifier as a fixed panel
            - Toggle with a hotkey
Tech stack: C++, Win32 Magnification API
```

---

## Example 161

**Intent:**
chord chart maker for guitar

**Spec:**
```
Type:       Desktop application (music tool)
Data model: Song(id, title, key, sections_json)
Features:   - Write lyrics with chords above the words
            - Transpose the whole song to another key
            - Show chord diagrams for each chord used
            - Switch between guitar and ukulele diagrams
            - Export to PDF
Storage:    Local JSON song files
Tech stack: Python, PySide6, ReportLab
```

---

## Example 162

**Intent:**
kids coloring book app ipad

**Spec:**
```
Type:       Mobile application (colouring)
Features:   - Show line-art pages to colour
            - Fill areas with a tap using flood fill
            - Paint with crayons and glitter brushes
            - Save finished pictures to the photo library
            - Lock settings behind a parent gate
Tech stack: Swift, SwiftUI, PencilKit
```

---

## Example 163

**Intent:**
card game about cats knocking things off tables

**Spec:**
```
Type:       Browser game (card game)
Features:   - Deal each player a hand of cat action cards
            - Push objects toward the table edge with card effects
            - Score when an object falls off
            - Play against two AI opponents
            - Show animated knocks and crashes
Storage:    Browser localStorage (wins)
Tech stack: JavaScript, React, Framer Motion
```

---

## Example 164

**Intent:**
lightweight code snippet manager

**Spec:**
```
Type:       Desktop application (snippet manager)
Data model: Snippet(id, title, language, code, tags, updated_at)
Features:   - Save snippets with syntax highlighting
            - Tag and search snippets
            - Copy a snippet with one click
            - Open a quick search with a global hotkey
            - Sync the library through a chosen folder like Dropbox
Storage:    SQLite database in a user-chosen folder
Tech stack: Tauri, Rust, React, Monaco Editor
```

---

## Example 165

**Intent:**
a racing game for phone where you draw the track

**Spec:**
```
Type:       Mobile game (racing)
Features:   - Draw a closed track with a finger
            - Smooth the drawn path into a spline road
            - Race a car around it against ghost opponents
            - Detect off-road and slow the car
            - Share tracks as a code
Storage:    Local save of drawn tracks
Tech stack: Unity, C#
```

---

## Example 166

**Intent:**
screen time stats for my pc

**Spec:**
```
Type:       Desktop application (usage stats)
Data model: DailyUsage(date, active_minutes, first_active_at, last_active_at)
Features:   - Track active computer time by checking input idle state
            - Show today's screen time in the tray
            - Chart daily usage for the past month
            - Set a daily limit with a warning
            - Export to CSV
Storage:    SQLite local database
Tech stack: Go, systray
```

---

## Example 167

**Intent:**
fps game in a small arena with robots

**Spec:**
```
Type:       Desktop game (first-person shooter)
Features:   - Move with WASD and look with the mouse
            - Shoot hitscan weapons with raycasts
            - Spawn robot enemies that navigate with a navmesh
            - Pick up health and ammo
            - Increase wave difficulty and track kills
Tech stack: Godot 4, GDScript
```

---

## Example 168

**Intent:**
ascii art converter

**Spec:**
```
Type:       Desktop application (image tool)
Features:   - Load an image and convert it to ASCII characters
            - Adjust width and character set
            - Preview in a monospace view
            - Invert for dark backgrounds
            - Copy or save as TXT or HTML
Tech stack: Python, Tkinter, Pillow
```

---

## Example 169

**Intent:**
stopwatch with laps

**Spec:**
```
Type:       Desktop application (utility)
Features:   - Start, stop and reset with the space bar
            - Record lap times in a list
            - Highlight the fastest and slowest lap
            - Keep the window always on top
            - Copy laps as text
Tech stack: C#, WinForms
```

---

## Example 170

**Intent:**
solar system sim for school

**Spec:**
```
Type:       Desktop application (educational simulation)
Features:   - Animate planets orbiting the sun with real orbital periods
            - Speed up or slow down time
            - Click a planet to show facts
            - Toggle orbit lines and labels
            - Zoom and rotate the 3D view
Tech stack: Python, VPython
```

---

## Example 171

**Intent:**
idle bakery game

**Spec:**
```
Type:       Mobile game (idle)
Data model: SaveState(coins, ovens, bakers, recipes_unlocked, last_online_at)
Features:   - Tap to bake bread
            - Hire bakers that bake automatically
            - Unlock pastries that sell for more
            - Earn offline income up to 8 hours
            - Show upgrade costs that scale exponentially
Storage:    Local save file
Tech stack: Unity, C#
```

---

## Example 172

**Intent:**
making a coop dungeon crawler in python arcade library for me and my roommate

**Spec:**
```
Type:       Desktop game (co-op dungeon crawler)
Features:   - Control two heroes with keyboard and gamepad
            - Generate dungeon rooms with random layouts
            - Fight enemies with melee and ranged attacks
            - Share loot that drops from chests
            - Share a camera that zooms to fit both players
Storage:    Local save file (unlocked heroes)
Tech stack: Python, Arcade
```

---

## Example 173

**Intent:**
helo i want aplication in my computer for school library, students borrow books and return, i am librarian in small village school in Indonesia, no internet

**Spec:**
```
Type:       Desktop application (library management)
Data model: Book(id, title, author, isbn, copies)
            Student(id, name, class)
            Loan(id, book_id -> Book, student_id -> Student, borrowed_on, due_on, returned_on)
Features:   - Add books and students
            - Lend a book to a student with a due date
            - Mark books returned
            - List overdue loans by class
            - Search books by title or author
Storage:    SQLite local database
Tech stack: Python, Tkinter
```

---

## Example 174

**Intent:**
so basically i want to record my screen AND my webcam in the corner for tutorials, and also my mic, and then be able to cut the bad parts. i'm on windows and obs is too complicated for me honestly

**Spec:**
```
Type:       Desktop application (screen recorder)
Features:   - Record the screen, webcam overlay and microphone in one click
            - Drag and resize the webcam bubble before recording
            - Pause and resume recording
            - Cut out unwanted parts on a simple timeline
            - Export to MP4
Tech stack: Electron, desktopCapturer, MediaRecorder, FFmpeg
```

---

## Example 175

**Intent:**
a game like a slot car race but you control with your voice volume

**Spec:**
```
Type:       Desktop game (voice-controlled racing)
Features:   - Read microphone volume every frame
            - Speed up the car the louder the player is
            - Throw the car off the track if too fast in curves
            - Support two players with two microphones
            - Show lap times
Tech stack: Python, Pygame, sounddevice
```

---

## Example 176

**Intent:**
My sister has a nail salon and keeps a paper book with appointments and what colours each lady liked, can you design a small desktop program for that. She has an old laptop with Windows 7.

**Spec:**
```
Type:       Desktop application (offline business tool)
Data model: Client(id, name, phone, favourite_colours, allergies)
            Appointment(id, client_id -> Client, starts_at, service, price, notes)
Features:   - Book appointments in a daily list view
            - Show the client's favourite colours and allergies when booking
            - Record price and service after the visit
            - Find clients by name or phone
            - Show weekly income
Storage:    SQLite local database
Tech stack: Python 3.8, Tkinter (runs on Windows 7)
```

---

## Example 177

**Intent:**
an incremental game about mining asteroids in space

**Spec:**
```
Type:       Browser game (incremental)
Data model: SaveState(credits, ore, drones, upgrades_json, last_tick_at)
Features:   - Click asteroids to mine ore
            - Build drones that mine automatically
            - Refine ore into higher-value metals
            - Unlock new asteroid belts with rarer ores
            - Save progress and add offline gains
Storage:    Browser localStorage
Tech stack: TypeScript, Svelte
```

---

## Example 178

**Intent:**
i make pottery and want to keep track of glazes and firing results with pics

**Spec:**
```
Type:       Desktop application (craft log)
Data model: Glaze(id, name, recipe, colour)
            Piece(id, clay_body, glaze_id -> Glaze, firing_temp, cone, result_notes, photo_path, fired_on)
Features:   - Record glaze recipes
            - Log each fired piece with glaze, cone and photo
            - Compare results of one glaze across firings
            - Search by glaze or clay body
            - Show photos in a gallery
Storage:    SQLite local database, photos in a folder
Tech stack: Python, PySide6
```

---

## Example 179

**Intent:**
mobile game where you build bridges for animals to cross a river

**Spec:**
```
Type:       Mobile game (physics puzzle)
Features:   - Place wood beams and ropes between anchor points
            - Simulate load with a 2D physics stress model
            - Send animals of different weight across
            - Break overloaded beams
            - Rate solutions by cost
Storage:    Local save data
Tech stack: Unity, C#
```

---

## Example 180

**Intent:**
crossplatform electron app to annotate pdfs

**Spec:**
```
Type:       Desktop application (PDF annotation)
Data model: Annotation(id, file_hash, page, kind, rect, colour, text)
Features:   - Open and render PDFs
            - Highlight, underline and add sticky notes
            - Draw freehand on pages
            - List all annotations in a sidebar
            - Save annotations into the PDF
Tech stack: Electron, PDF.js, pdf-lib
```

---

## Example 181

**Intent:**
guess the flag game

**Spec:**
```
Type:       Browser game (quiz)
Features:   - Show a country flag and four country names
            - Increase difficulty by including similar flags
            - Give a streak bonus
            - End after three mistakes
            - Show a review of missed flags
Tech stack: HTML, CSS, JavaScript
```

---

## Example 182

**Intent:**
dj mixing app for parties, two decks

**Spec:**
```
Type:       Desktop application (DJ software)
Data model: Track(id, path, title, artist, bpm, key)
Features:   - Load tracks onto two decks with waveforms
            - Detect BPM and sync tempos
            - Crossfade between decks
            - Set cue points and loops
            - Apply EQ and filter per deck
Storage:    SQLite track library
Tech stack: C++, JUCE
```

---

## Example 183

**Intent:**
pinball table game

**Spec:**
```
Type:       Desktop game (pinball)
Features:   - Simulate the ball with 2D physics, gravity and bumpers
            - Control left and right flippers with keys
            - Score targets, ramps and combos
            - Nudge the table with a tilt limit
            - Save high scores with initials
Storage:    Local high score file
Tech stack: C#, MonoGame, Aether.Physics2D
```

---

## Example 184

**Intent:**
worldbuilding wiki for my fantasy novel, offline

**Spec:**
```
Type:       Desktop application (worldbuilding)
Data model: Article(id, title, category, body_markdown)
            Link(from_id -> Article, to_id -> Article)
            MapPin(id, article_id -> Article, x, y)
Features:   - Write articles for characters, places and events
            - Link articles with wiki-style double brackets
            - Show backlinks for each article
            - Pin places on an uploaded map image
            - Build a timeline from event dates
Storage:    SQLite local database
Tech stack: Tauri, Svelte, SQLite
```

---

## Example 185

**Intent:**
game where you control traffic lights at a busy crossing

**Spec:**
```
Type:       Mobile game (traffic management)
Features:   - Spawn cars from four directions at increasing rates
            - Tap lights to switch them between red and green
            - Detect car collisions and end the game
            - Add ambulances that must pass quickly
            - Score by cars passed safely
Tech stack: Godot 4, GDScript
```

---

## Example 186

**Intent:**
windows app to schedule my pc shutdown

**Spec:**
```
Type:       Desktop application (utility)
Features:   - Shut down, restart or sleep at a set time
            - Shut down after a countdown
            - Shut down when a download finishes by watching network idle
            - Cancel with one click
            - Warn one minute before
Tech stack: C#, WinForms
```

---

## Example 187

**Intent:**
i want a game where you sing notes to open doors, pitch detection

**Spec:**
```
Type:       Desktop game (puzzle)
Features:   - Detect the pitch the player sings through the microphone
            - Open doors when a target note is held
            - Solve melody locks with a sequence of notes
            - Show a pitch meter on screen
            - Adapt the note range to the player's voice
Tech stack: Godot 4, GDScript, AudioEffectSpectrumAnalyzer
```

---

## Example 188

**Intent:**
maths quiz game for 2 kids on one tablet head to head

**Spec:**
```
Type:       Mobile game (educational, local multiplayer)
Features:   - Split the screen into two mirrored halves
            - Show the same math question to both sides
            - Award the point to whoever taps the right answer first
            - Penalise wrong taps with a short freeze
            - Play first to 10
Tech stack: Flutter
```

---

## Example 189

**Intent:**
app for making flowcharts offline

**Spec:**
```
Type:       Desktop application (diagramming)
Data model: Diagram(id, name)
            Node(id, diagram_id -> Diagram, shape, text, x, y)
            Edge(id, from_node_id -> Node, to_node_id -> Node, label)
Features:   - Drag shapes onto a canvas
            - Connect shapes with arrows that follow when moved
            - Edit labels inline
            - Align and snap to grid
            - Export as PNG and SVG
Storage:    Local JSON diagram files
Tech stack: Electron, React Flow
```

---

## Example 190

**Intent:**
night sky planetarium on the desktop

**Spec:**
```
Type:       Desktop application (astronomy)
Features:   - Show stars and planets for any location and time
            - Search and centre on a named object
            - Draw constellation lines
            - Show rise and set times
            - Speed time forward to watch the sky move
Tech stack: Python, PyQt6, Skyfield
```

---

## Example 191

**Intent:**
game for kids where they feed monsters the right shape

**Spec:**
```
Type:       Mobile game (educational, toddlers)
Features:   - Show a monster with a shape on its belly
            - Drag matching shapes into its mouth
            - Play happy and silly sounds
            - Add colours and sizes in harder levels
            - Never show a fail screen
Tech stack: Unity, C#
```

---

## Example 192

**Intent:**
little app to record what i spend at the market each day, very simple, i dont have internet at home

**Spec:**
```
Type:       Desktop application (expense log)
Data model: Expense(id, date, item, amount, category)
Features:   - Add an expense with amount and category
            - Show today's and this month's total
            - List expenses by day
            - Chart spending by category
            - Export to CSV
Storage:    SQLite local database
Tech stack: Python, Tkinter
```

---

## Example 193

**Intent:**
a horror game in unity but not too scary, for teenagers

**Spec:**
```
Type:       Desktop game (horror, 3D)
Features:   - Explore a dark school at night with a flashlight
            - Manage flashlight battery with pickups
            - Hide from a wandering creature using line-of-sight AI
            - Solve notes and key puzzles to unlock rooms
            - Use checkpoints with autosave
Storage:    Local save file
Tech stack: Unity, C#
```

---

## Example 194

**Intent:**
wanna build an app that scans my old photo prints with my scanner and splits them

**Spec:**
```
Type:       Desktop application (scanning)
Features:   - Scan a page with several prints using the TWAIN or WIA scanner driver
            - Detect each photo's edges automatically
            - Crop and straighten each photo
            - Save each photo as a separate JPEG
            - Name files with a date and counter
Tech stack: Python, OpenCV, pytwain, PySide6
```

---

## Example 195

**Intent:**
rhythm boxing game with webcam

**Spec:**
```
Type:       Desktop game (motion rhythm)
Features:   - Track the player's hands with webcam pose estimation
            - Show targets synced to the music beat
            - Score punches that hit targets on time
            - Show a combo meter and calories estimate
            - Pick songs from a bundled list
Tech stack: Python, Pygame, MediaPipe
```

---

## Example 196

**Intent:**
mac app to batch rename and resize screenshots

**Spec:**
```
Type:       Desktop application (file utility)
Features:   - Watch the screenshot folder
            - Rename new screenshots with app name and date
            - Resize retina screenshots to half size
            - Move them into dated folders
            - Show recent changes in the menu bar
Tech stack: Swift, SwiftUI, FSEvents
```

---

## Example 197

**Intent:**
puzzle game about folding paper

**Spec:**
```
Type:       Browser game (puzzle)
Data model: Level(id, paper_shape, target_shape, max_folds)
Features:   - Show a sheet of paper on a grid
            - Fold the paper along valid lines by dragging
            - Animate folds in 3D
            - Match the target silhouette to win
            - Undo folds
Storage:    Browser localStorage
Tech stack: TypeScript, Three.js
```

---

## Example 198

**Intent:**
diary app with mood

**Spec:**
```
Type:       Desktop application (journal)
Data model: Entry(id, date, text, mood, tags)
Features:   - Write one diary entry per day
            - Pick a mood from five emojis
            - Show moods on a calendar heatmap
            - Search entries
            - Lock the diary with a PIN
Storage:    SQLite local database
Tech stack: Electron, Vue 3
```

---

## Example 199

**Intent:**
block breaker game with physics bricks that fall

**Spec:**
```
Type:       Browser game (arcade)
Features:   - Bounce the ball off a paddle to hit bricks
            - Knock bricks loose so they fall with physics
            - Catch falling bricks for bonus points
            - Drop power-ups like multi-ball
            - Load levels from JSON
Storage:    Browser localStorage
Tech stack: JavaScript, Matter.js
```

---

## Example 200

**Intent:**
farming game where crops are musical instruments and the farm plays a song

**Spec:**
```
Type:       Desktop game (farming, music)
Data model: Plot(id, x, y, crop_type, growth_stage, watered)
            SaveState(day, coins, unlocked_crops)
Features:   - Plant instrument crops like drum beets and flute reeds on a grid
            - Grow crops through stages each in-game day
            - Play a looping song where each grown crop adds its instrument
            - Sell harvested crops at the market
            - Save the farm each night
Storage:    Local save file
Tech stack: Godot 4, GDScript
```

---

## Example 201

**Intent:**
tiny app to rename my podcast episodes from the rss feed titles

**Spec:**
```
Type:       Desktop application (file utility)
Features:   - Fetch the podcast RSS feed
            - Match local files to episodes by duration or GUID
            - Rename files to episode number and title
            - Write title and date into ID3 tags
            - Preview changes before applying
Input:      RSS feed URL and a folder of downloaded MP3 files
Tech stack: Python, feedparser, mutagen, Tkinter
```

---

## Example 202

**Intent:**
typing game where you shoot zombies by typing words

**Spec:**
```
Type:       Browser game (typing)
Features:   - Spawn zombies with words above their heads
            - Lock onto a zombie when its first letter is typed
            - Destroy it when the word is completed
            - Increase word length and speed per wave
            - Show WPM and accuracy at game over
Storage:    Browser localStorage
Tech stack: TypeScript, Phaser 3
```

---

## Example 203

**Intent:**
i would like for my grandfather a big buttons music player for his old songs, he cannot see well and confused by computers

**Spec:**
```
Type:       Desktop application (accessible media player)
Features:   - Show only three huge buttons: play, next and stop
            - Play songs from one folder in order
            - Read the song name aloud with text-to-speech
            - Start playing automatically when the computer turns on
            - Hide all menus and settings behind a key combo
Tech stack: Python, Tkinter, python-vlc, pyttsx3
```

---

## Example 204

**Intent:**
home budget app desktop wpf

**Spec:**
```
Type:       Desktop application (budgeting)
Data model: Account(id, name, balance)
            Category(id, name, monthly_budget)
            Transaction(id, account_id -> Account, category_id -> Category, date, amount, note)
Features:   - Record income and expenses per account
            - Set monthly budgets per category
            - Show budget progress bars
            - Import bank CSV statements
            - Chart spending trends by month
Storage:    SQLite local database
Tech stack: C#, .NET 8, WPF, LiveCharts2
```

---

## Example 205

**Intent:**
browser game where you're a cloud raining on fires

**Spec:**
```
Type:       Browser game (arcade)
Features:   - Move the cloud across a scrolling forest with the mouse
            - Hold click to rain and drain the water meter
            - Refill water by flying over lakes
            - Spread fires across trees over time
            - Lose when too much forest burns
Storage:    Browser localStorage
Tech stack: JavaScript, Kaboom.js
```

---

## Example 206

**Intent:**
an app where i can practice drawing with timed reference photos

**Spec:**
```
Type:       Desktop application (art practice)
Features:   - Load a folder of reference photos
            - Show photos one at a time for 30 seconds to 10 minutes
            - Play a sound at each switch
            - Flip or grayscale the image
            - Log practice sessions
Storage:    Local JSON session log
Tech stack: Electron
```

---

## Example 207

**Intent:**
2d fighting game for two players same keyboard

**Spec:**
```
Type:       Desktop game (fighting)
Features:   - Animate fighters with sprite sheets
            - Read combo inputs from a buffered input queue
            - Detect hits with hitboxes and hurtboxes
            - Show health bars and a round timer
            - Play best of three rounds
Tech stack: C++, SFML
```

---

## Example 208

**Intent:**
photo booth app for a wedding with a webcam and a button

**Spec:**
```
Type:       Desktop application (photo booth)
Features:   - Show a full-screen live preview
            - Start a 3-2-1 countdown when the button or space is pressed
            - Take four photos and arrange them in a strip with a custom frame
            - Print the strip to a photo printer
            - Save every strip to a folder
Tech stack: Python, OpenCV, Pygame, Pillow
```

---

## Example 209

**Intent:**
a mobile game to learn the periodic table

**Spec:**
```
Type:       Mobile game (educational)
Data model: Element(id, symbol, name, number, group, fact)
            Progress(element_id -> Element, mastered)
Features:   - Play matching rounds between symbols and names
            - Place elements on an empty periodic table
            - Unlock fun facts as elements are mastered
            - Repeat weak elements more often
            - Track mastery per group
Storage:    Local SQLite
Tech stack: React Native, Expo
```

---

## Example 210

**Intent:**
gonna make a tetris like game in rust where pieces are pentominoes

**Spec:**
```
Type:       Desktop game (falling blocks puzzle)
Features:   - Spawn the 12 pentomino pieces with a bag randomiser
            - Rotate pieces with wall kicks
            - Clear full lines and score combos
            - Speed up gravity per level
            - Show the next three pieces and a hold slot
Tech stack: Rust, Bevy
```

---

## Example 211

**Intent:**
my laptop should stop charging at 80% but it cant, so warn me to pull the plug

**Spec:**
```
Type:       Desktop application (system tray)
Features:   - Read battery percentage and charging state
            - Notify when charging reaches a set upper limit
            - Notify when discharging hits a lower limit
            - Show battery health and cycle count
            - Repeat the alert every 5 minutes until unplugged
Storage:    Local JSON settings
Tech stack: Python, psutil, pystray, plyer
```

---

## Example 212

**Intent:**
Can you spec a small Java desktop game where you manage a fish tank, feed fish, clean the water, breed them.

**Spec:**
```
Type:       Desktop game (simulation)
Data model: Fish(id, species, age, hunger, health, gender)
            Tank(water_quality, temperature, coins)
Features:   - Show fish swimming with simple steering behaviour
            - Feed fish and drop water quality as food rots
            - Clean the tank to restore water quality
            - Breed adult fish pairs to get babies
            - Sell fish to buy decorations and new species
            - Save the tank state
Storage:    Local JSON save file
Tech stack: Java, LibGDX
```

---

## Example 213

**Intent:**
an app like a whiteboard to explain things on my second monitor while teaching on zoom

**Spec:**
```
Type:       Desktop application (whiteboard)
Features:   - Draw with pen, highlighter and shapes on an infinite canvas
            - Add text and paste images
            - Switch pages and go back
            - Draw over the screen in a transparent overlay mode
            - Export pages as PDF
Tech stack: Electron, Fabric.js
```

---

## Example 214

**Intent:**
mobile quiz game about our city's history for a museum

**Spec:**
```
Type:       Mobile game (location quiz)
Data model: Stop(id, name, latitude, longitude, question, answer_options, correct_index)
            Visit(stop_id -> Stop, answered_correctly)
Features:   - Show a map of the museum's city walking route
            - Unlock a quiz question when the player is near a stop
            - Award badges for correct answers
            - Show historical photos after answering
            - Work offline with bundled content
Storage:    Local SQLite
Tech stack: Flutter, flutter_map (offline tiles), geolocator
```

---

## Example 215

**Intent:**
tool to make app icons in all sizes from one png

**Spec:**
```
Type:       Desktop application (icon generator)
Features:   - Load a square source PNG
            - Generate all iOS, Android, Windows ICO and macOS ICNS sizes
            - Add optional rounded corners and padding
            - Preview icons on a sample home screen
            - Export into platform folders
Tech stack: Python, Pillow, PySide6
```

---

## Example 216

**Intent:**
stealth game where you are a cat stealing food from a kitchen

**Spec:**
```
Type:       Desktop game (stealth)
Features:   - Sneak through a kitchen in a top-down view
            - Show the cook's vision cone and patrol path
            - Make noise when running or knocking objects
            - Hide under tables and in boxes
            - Collect food items and escape through the cat flap
Tech stack: Godot 4, GDScript
```

---

## Example 217

**Intent:**
an mp4 to mp3 converter thats really simple

**Spec:**
```
Type:       Desktop application (media converter)
Features:   - Drop video files into the window
            - Extract the audio track to MP3
            - Choose bitrate 128, 192 or 320 kbps
            - Show progress per file
            - Save next to the original file
Tech stack: Python, Tkinter, FFmpeg
```

---

## Example 218

**Intent:**
im starting a little etsy shop and need a desktop thing to track my materials cost and work out prices for my handmade earrings

**Spec:**
```
Type:       Desktop application (pricing calculator)
Data model: Material(id, name, unit_cost, unit)
            Product(id, name, labour_minutes, hourly_rate, markup_pct)
            ProductMaterial(product_id -> Product, material_id -> Material, quantity)
Features:   - Store materials with unit costs
            - Build a product from materials and labour time
            - Calculate cost, wholesale and retail price
            - Update all prices when a material cost changes
            - Export a price list
Storage:    SQLite local database
Tech stack: Python, Flet
```

---

## Example 219

**Intent:**
an endless runner where the world is a hand drawn notebook

**Spec:**
```
Type:       Mobile game (endless runner)
Features:   - Run automatically across procedurally generated doodle platforms
            - Jump and slide with taps and swipes
            - Draw a short bridge with your finger over gaps using ink
            - Collect ink drops to refill ink
            - Save high scores and unlock character doodles
Storage:    Local save data
Tech stack: Unity, C#
```

---

## Example 220

**Intent:**
kaleidoscope drawing app

**Spec:**
```
Type:       Desktop application (creative drawing)
Features:   - Mirror strokes around a centre with 4 to 16 segments
            - Pick brush size, colour and gradient
            - Animate slow rotation of the canvas
            - Undo strokes
            - Save as PNG
Tech stack: JavaScript, p5.js, Electron
```

---

## Example 221

**Intent:**
i want to code a battleship style game but on a hex map with submarines that move

**Spec:**
```
Type:       Desktop game (strategy)
Features:   - Place fleets on a hidden hex grid
            - Move submarines one hex per turn
            - Fire at hexes and mark hit or miss
            - Use sonar pings to reveal nearby ships
            - Play against AI that hunts after hits
Tech stack: Python, Pygame
```

---

## Example 222

**Intent:**
Hi, I am graphic designer from Poland. I need a program which collects my inspiration images, I drop them and add tags, and show like moodboard.

**Spec:**
```
Type:       Desktop application (moodboard)
Data model: Image(id, file_path, source_url, added_at)
            Tag(id, name)
            ImageTag(image_id -> Image, tag_id -> Tag)
            Board(id, name, layout_json)
Features:   - Drop images from the browser or desktop
            - Tag images and filter by tags
            - Arrange images freely on boards
            - Extract main colours from each image
            - Export a board as PNG
Storage:    SQLite local database, images copied into a library folder
Tech stack: Electron, React, sharp
```

---

## Example 223

**Intent:**
battery monitor for wireless mouse and headset

**Spec:**
```
Type:       Desktop application (system tray)
Features:   - Read battery levels of Bluetooth devices
            - Show each device's level in the tray menu
            - Warn when a device drops below 15 percent
            - Show the time since last charge
            - Refresh every 10 minutes
Tech stack: C#, .NET, Windows.Devices.Bluetooth (WinRT)
```

---

## Example 224

**Intent:**
card collecting game where you catch bugs in a garden on phone

**Spec:**
```
Type:       Mobile game (collecting)
Data model: BugSpecies(id, name, rarity, habitat, season)
            CaughtBug(id, species_id -> BugSpecies, size, caught_at)
Features:   - Search garden scenes by tapping leaves and stones
            - Catch bugs with a timing net minigame
            - Add each bug as a card to a collection album
            - Rotate available bugs by real-world season
            - Trade duplicate cards for rare ones
Storage:    Local SQLite
Tech stack: Kotlin, Jetpack Compose, Canvas
```

---

## Example 225

**Intent:**
midi controller mapper

**Spec:**
```
Type:       Desktop application (MIDI utility)
Data model: Mapping(id, midi_channel, cc_number, action_type, action_value)
Features:   - List connected MIDI devices
            - Learn a mapping by moving a knob or pressing a pad
            - Map controls to keyboard shortcuts or system volume
            - Save mapping profiles per app
            - Show incoming MIDI messages in a monitor
Storage:    Local JSON profiles
Tech stack: Python, mido, python-rtmidi, PyQt6
```

---

## Example 226

**Intent:**
game where u build a rocket and launch it with real-ish physics

**Spec:**
```
Type:       Desktop game (simulation)
Features:   - Build rockets from engines, tanks and capsules
            - Simulate thrust, mass and fuel burn
            - Simulate gravity and simple atmospheric drag
            - Reach orbit or crash
            - Unlock new parts by reaching altitude goals
Storage:    Local save files (rocket designs)
Tech stack: Unity, C#
```

---

## Example 227

**Intent:**
chat with myself notes app, like notes as messages

**Spec:**
```
Type:       Desktop application (note-taking)
Data model: Message(id, text, image_path, created_at, pinned)
Features:   - Write notes as chat messages in a single thread
            - Paste images and links
            - Pin important messages
            - Search by text and date
            - Export the thread to Markdown
Storage:    SQLite local database
Tech stack: Tauri, React
```

---

## Example 228

**Intent:**
kids game to learn letters by tracing them on tablet

**Spec:**
```
Type:       Mobile game (educational)
Features:   - Show a large letter with a dotted path
            - Check tracing accuracy against the stroke path
            - Animate the stroke order first
            - Play the letter sound and an example word
            - Unlock a sticker for each finished letter
Storage:    Local storage (progress)
Tech stack: Swift, SwiftUI, PencilKit
```

---

## Example 229

**Intent:**
An image viewer that's super fast for big folders.

**Spec:**
```
Type:       Desktop application (image viewer)
Features:   - Open huge folders instantly with lazy thumbnail loading
            - Preload next and previous images
            - Zoom and pan smoothly with GPU rendering
            - Delete or move images with single keys
            - Show EXIF info in an overlay
Tech stack: Rust, wgpu, image crate, winit
```

---

## Example 230

**Intent:**
soccer game top down for 2v2 on the same pc with controllers

**Spec:**
```
Type:       Desktop game (sports)
Features:   - Support four gamepads with player selection
            - Control players and pass or shoot with buttons
            - Simulate ball physics and goals
            - Switch AI teammates if fewer players join
            - Play timed matches with a scoreboard
Tech stack: Godot 4, GDScript
```

---

## Example 231

**Intent:**
secret santa drawing app for our family on the laptop

**Spec:**
```
Type:       Desktop application (gift exchange)
Data model: Participant(id, name, email, exclusions)
            Assignment(giver_id -> Participant, receiver_id -> Participant)
Features:   - Add participants and people they cannot draw, like partners
            - Draw assignments so nobody gets themselves
            - Reveal each person's match privately one by one
            - Remember last year to avoid repeats
            - Email each person their match
Storage:    Local JSON file
Tech stack: Python, Tkinter, smtplib
```

---

## Example 232

**Intent:**
idle game about a wizard school

**Spec:**
```
Type:       Browser game (idle)
Data model: SaveState(mana, students, teachers, classrooms, spells_json, last_tick_at)
Features:   - Enrol students who generate mana over time
            - Hire teachers to boost a subject
            - Build new classrooms to unlock spells
            - Run exams that grant bonus mana
            - Save progress automatically
Storage:    Browser localStorage
Tech stack: JavaScript, Vue 3
```

---

## Example 233

**Intent:**
camera app on desktop for document scanning with phone? no, with webcam

**Spec:**
```
Type:       Desktop application (document scanner)
Features:   - Show the webcam feed and detect the page edges
            - Capture and correct the perspective
            - Enhance to black and white
            - Collect multiple pages into one document
            - Save as PDF
Tech stack: Python, OpenCV, img2pdf, PySide6
```

---

## Example 234

**Intent:**
game where two players share one keyboard to pilot one spaceship, one steers one shoots

**Spec:**
```
Type:       Desktop game (co-op shooter)
Features:   - Give one player steering and thrust keys
            - Give the other player turret aiming and firing keys
            - Spawn asteroid fields and enemy ships
            - Share a hull health bar
            - Score waves survived
Tech stack: C, raylib
```

---

## Example 235

**Intent:**
offline app for a church to manage members and donations

**Spec:**
```
Type:       Desktop application (offline management)
Data model: Member(id, name, phone, address, family_id)
            Donation(id, member_id -> Member, amount, fund, date)
Features:   - Register members and group them into families
            - Record donations by fund
            - Print yearly donation statements
            - Show birthdays this month
            - Back up data to a USB stick
Storage:    SQLite local database
Tech stack: Python, PySide6, ReportLab
```

---

## Example 236

**Intent:**
platformer where you can rewind time 5 seconds

**Spec:**
```
Type:       Desktop game (platformer)
Features:   - Record player and object state every frame into a ring buffer
            - Rewind up to 5 seconds while holding a key
            - Use rewinding to solve platform timing puzzles
            - Make some objects immune to rewind
            - Show a rewind energy bar
Tech stack: Unity, C#
```

---

## Example 237

**Intent:**
subtitle syncer, my subs are always a few seconds off

**Spec:**
```
Type:       Desktop application (subtitle tool)
Features:   - Load a video and its SRT file
            - Shift all subtitles by a set offset
            - Fix drift by syncing two reference lines
            - Auto-sync using speech detection on the audio
            - Save the corrected SRT
Tech stack: Python, pysubs2, FFmpeg, Tkinter
```

---

## Example 238

**Intent:**
an app to make my own crossword puzzles to print for my students

**Spec:**
```
Type:       Desktop application (puzzle maker)
Data model: Puzzle(id, title)
            Entry(id, puzzle_id -> Puzzle, word, clue)
Features:   - Enter words and clues
            - Generate a crossword layout that fits as many words as possible
            - Number the grid and list across and down clues
            - Print the puzzle and an answer key
            - Save puzzles to edit later
Storage:    Local JSON files
Tech stack: Python, Tkinter, ReportLab
```

---

## Example 239

**Intent:**
mobile game where you guide sheep into a pen by whistling (tapping)

**Spec:**
```
Type:       Mobile game (herding)
Features:   - Simulate a flock with boids flocking behaviour
            - Tap to move the dog and scare sheep away
            - Herd all sheep into the pen before time runs out
            - Add wolves and rivers in later levels
            - Rate levels by time and lost sheep
Tech stack: Godot 4, GDScript
```

---

## Example 240

**Intent:**
video player for language learners with dual subtitles

**Spec:**
```
Type:       Desktop application (language learning player)
Data model: SavedWord(id, word, sentence, video_path, timestamp_s)
Features:   - Play videos with two subtitle tracks at once
            - Pause automatically at the end of each line
            - Click a word to see a dictionary definition
            - Save words with their sentence
            - Repeat the current line with one key
Storage:    SQLite local database
Tech stack: Electron, libmpv, React
```

---

## Example 241

**Intent:**
casino style card game but no real money, with chips, original rules

**Spec:**
```
Type:       Desktop game (card game)
Features:   - Deal a three-card hand against the dealer
            - Let the player raise, fold or swap one card
            - Rank hands with an original scoring table
            - Track chips and allow buying more for free
            - Show statistics of hands won
Storage:    Local JSON save
Tech stack: C#, Godot 4 (.NET)
```

---

## Example 242

**Intent:**
snipping tool that also reads text from the screenshot

**Spec:**
```
Type:       Desktop application (screenshot OCR)
Features:   - Select a screen region with a hotkey
            - Run OCR on the captured region
            - Copy recognised text to the clipboard
            - Translate the text on request
            - Keep a history of captures
Tech stack: Python, mss, Tesseract (pytesseract), PyQt6
```

---

## Example 243

**Intent:**
game in scratch? no i mean javascript, where a cat jumps on rooftops at night

**Spec:**
```
Type:       Browser game (platformer)
Features:   - Generate rooftops of random heights and gaps
            - Jump with variable height by holding space
            - Collect fish and avoid chimneys with smoke
            - Increase speed over time
            - Show the night city parallax background
Storage:    Browser localStorage
Tech stack: JavaScript, HTML5 Canvas
```

---

## Example 244

**Intent:**
a slideshow of my photos as a screensaver

**Spec:**
```
Type:       Desktop application (screensaver)
Features:   - Show photos from a chosen folder full screen
            - Fade between photos with Ken Burns motion
            - Show the date taken in a corner
            - Exit on mouse move or key press
            - Configure folder and timing in a settings dialog
Storage:    Windows registry (settings)
Tech stack: C#, .NET, WinForms (.scr screensaver)
```

---

## Example 245

**Intent:**
game about delivering pizza on a bike in a small town

**Spec:**
```
Type:       Mobile game (delivery)
Features:   - Ride a bike through a town map with on-screen controls
            - Pick up orders from the pizzeria
            - Show a minimap with the delivery address
            - Lose tips as pizzas get cold over time
            - Upgrade the bike and delivery bag
Storage:    Local save data
Tech stack: Unity, C#
```

---

## Example 246

**Intent:**
offline flashcards for medical students with images

**Spec:**
```
Type:       Desktop application (flashcards)
Data model: Deck(id, name)
            Card(id, deck_id -> Deck, front, back, image_path, occlusion_boxes)
            ReviewState(card_id -> Card, due_on, interval_days, ease)
Features:   - Create cards with text and images
            - Hide parts of anatomy images with occlusion boxes
            - Review due cards with spaced repetition
            - Show stats by deck
            - Import decks from CSV
Storage:    SQLite local database
Tech stack: Electron, React
```

---

## Example 247

**Intent:**
fishing for words game - letters swim around and you catch them to spell

**Spec:**
```
Type:       Browser game (word)
Features:   - Animate letter fish swimming across the screen
            - Catch a fish by clicking and add its letter to a word tray
            - Submit words checked against a dictionary
            - Score longer words higher
            - Run on a 2-minute timer
Tech stack: JavaScript, PixiJS
```

---

## Example 248

**Intent:**
speedreading app that flashes one word at a time

**Spec:**
```
Type:       Desktop application (reading)
Features:   - Paste text or open TXT, PDF and EPUB files
            - Show one word at a time at a set words-per-minute
            - Highlight the focus letter of each word
            - Pause and step back by sentence
            - Remember position per document
Storage:    Local JSON (positions)
Tech stack: Python, PySide6, PyMuPDF
```

---

## Example 249

**Intent:**
puzzle platformer where you swap places with your shadow

**Spec:**
```
Type:       Desktop game (puzzle platformer)
Features:   - Cast the player's shadow from moving light sources
            - Swap the player with the shadow's position on a key press
            - Use shadows on walls to reach high ledges
            - Move lamps to change shadow angles
            - Load hand-built levels from a tilemap
Storage:    Local save file
Tech stack: Godot 4, GDScript
```

---

## Example 250

**Intent:**
lyrics display app for karaoke nights at home

**Spec:**
```
Type:       Desktop application (karaoke)
Data model: Song(id, audio_path, lrc_path, title, artist)
            QueueEntry(id, song_id -> Song, singer_name, position)
Features:   - Play songs with synced LRC lyrics highlighted word by word
            - Show lyrics full screen on a TV
            - Queue songs with singer names
            - Lower the vocal track with a centre-channel filter
            - Change key without changing speed
Storage:    SQLite song library
Tech stack: C#, .NET, Avalonia UI, NAudio, SoundTouch
```

---

## Example 251

**Intent:**
game where you run a tiny island airport and land planes

**Spec:**
```
Type:       Mobile game (traffic control)
Features:   - Draw landing paths for incoming planes with a finger
            - Detect near-misses and collisions between planes
            - Unload passengers at gates to earn coins
            - Add runways and gates as upgrades
            - Increase plane frequency over time
Storage:    Local save data
Tech stack: Flutter, Flame
```

---

## Example 252

**Intent:**
password generator tray

**Spec:**
```
Type:       Desktop application (system tray)
Features:   - Generate a password from the tray menu with one click
            - Set length and character types
            - Generate memorable passphrases from a word list
            - Copy to clipboard and clear after 30 seconds
            - Show password strength
Tech stack: Rust, tray-icon crate
```

---

## Example 253

**Intent:**
hi im 14 and want to make a game where you are a pizza and you roll down hills eating toppings, i have unity installed

**Spec:**
```
Type:       Desktop game (3D physics)
Features:   - Roll a pizza ball down 3D hills with rigid body physics
            - Steer with arrow keys or WASD
            - Collect toppings that stick to the pizza and make it bigger
            - Avoid forks and ovens that end the run
            - Show a score and a topping count at the finish
Storage:    Unity PlayerPrefs (best score)
Tech stack: Unity, C#
```

---

## Example 254

**Intent:**
file sync between my laptop and external drive, one way

**Spec:**
```
Type:       Desktop application (backup)
Data model: SyncJob(id, source_path, target_path, exclude_patterns, last_run_at)
Features:   - Configure source and target folders
            - Copy new and changed files based on size and modified time
            - Optionally delete files removed from the source
            - Show a preview of changes before running
            - Log each run with copied counts
Storage:    Local JSON job config, log files
Tech stack: Go, Fyne
```

---

## Example 255

**Intent:**
i wanna mix photos into a collage

**Spec:**
```
Type:       Desktop application (collage maker)
Features:   - Choose a collage template grid
            - Drop photos into cells and pan or zoom each
            - Adjust borders, spacing and corner radius
            - Add text captions
            - Export at print resolution as JPEG
Tech stack: Electron, Konva.js
```

---

## Example 256

**Intent:**
board game where you build a train network on a map with friends online

**Spec:**
```
Type:       Browser game (board game, multiplayer)
Data model: Game(id, code, map_id, turn, status)
            Player(id, game_id -> Game, name, money, colour)
            Track(id, game_id -> Game, owner_id -> Player, from_city, to_city)
Features:   - Show a map of cities with possible track routes
            - Buy and lay track segments on your turn
            - Draw delivery cards and earn money for completed routes
            - Sync turns between players in real time
            - Show final scores and the longest network
Storage:    PostgreSQL (games), Redis (live state)
Tech stack: TypeScript, React, Node.js, Socket.IO
```

---

## Example 257

**Intent:**
tool to batch remove backgrounds from product photos

**Spec:**
```
Type:       Desktop application (image tool)
Features:   - Load a folder of product images
            - Remove backgrounds with an on-device segmentation model
            - Replace the background with white or transparent
            - Review and touch up masks with a brush
            - Export as PNG or JPEG
Tech stack: Python, rembg (U2-Net), PySide6
```

---

## Example 258

**Intent:**
memory game with sounds instead of pictures

**Spec:**
```
Type:       Browser game (memory)
Features:   - Show a grid of face-down tiles that each play a sound
            - Match tiles that play the same sound
            - Use instruments, animals and everyday sounds packs
            - Count moves and time
            - Add an accessible mode with keyboard navigation
Tech stack: HTML, CSS, JavaScript, Web Audio API
```

---

## Example 259

**Intent:**
tray app showing my internet speed up and down

**Spec:**
```
Type:       Desktop application (system tray)
Features:   - Measure upload and download bytes per second on the active interface
            - Show live speeds next to the tray icon
            - Run a speed test on demand
            - Graph usage for the last hour
            - Show daily data totals
Storage:    SQLite (daily totals)
Tech stack: C#, .NET, WPF
```

---

## Example 260

**Intent:**
a mobile game where you mix potions by combining colors

**Spec:**
```
Type:       Mobile game (puzzle)
Data model: Recipe(id, target_colour, allowed_ingredients, max_pours)
Features:   - Pour coloured liquids into a flask by tapping bottles
            - Mix colours with subtractive colour blending
            - Match the customer's requested potion colour
            - Score by how close the colour is
            - Unlock new ingredients and customers
Storage:    Local save data
Tech stack: Unity, C#
```

---

## Example 261

**Intent:**
desktop app to organise my sewing patterns pdf collection

**Spec:**
```
Type:       Desktop application (file organiser)
Data model: Pattern(id, file_path, name, designer, garment_type, sizes, fabric_needed, thumbnail_path)
Features:   - Import pattern PDFs and render cover thumbnails
            - Tag by garment type, size range and designer
            - Search and filter the collection
            - Open the PDF in the default viewer
            - Mark patterns as sewn with notes
Storage:    SQLite local database
Tech stack: Python, PySide6, PyMuPDF
```

---

## Example 262

**Intent:**
zombie survival game where you build barricades at night

**Spec:**
```
Type:       Desktop game (survival)
Features:   - Scavenge during the day in a top-down town
            - Build barricades from scavenged wood at night
            - Spawn zombie waves that path-find to weak barricades
            - Manage hunger and stamina
            - Save at the safe house
Storage:    Local save files
Tech stack: Unity, C#
```

---

## Example 263

**Intent:**
launcher for my steam epic and gog games all in one place

**Spec:**
```
Type:       Desktop application (game launcher)
Data model: Game(id, title, store, install_path, launch_uri, cover_path, playtime_minutes)
Features:   - Detect installed games from each store's local files
            - Show all games in one cover grid
            - Launch games through each store's URI
            - Track playtime per game
            - Filter by store and favourites
Storage:    SQLite local database
Tech stack: C#, .NET, Avalonia UI
```

---

## Example 264

**Intent:**
clicker game for my discord friends but as a desktop app with leaderboard

**Spec:**
```
Type:       Desktop game (clicker with online leaderboard)
Auth:       Username only, sent with a device token
Data model: Player(id, username, device_token, total_clicks, updated_at)
Features:   - Count clicks on a big button with combos
            - Buy auto-clickers and multipliers
            - Upload the score to a shared leaderboard every minute
            - Show the top 20 friends
            - Save progress locally
Storage:    Local JSON save, PostgreSQL leaderboard
Tech stack: Electron, Node.js, Express
```

---

## Example 265

**Intent:**
offline music theory trainer that plays intervals and i guess them

**Spec:**
```
Type:       Desktop application (ear training)
Data model: Session(id, exercise_type, correct, total, played_at)
Features:   - Play two notes and ask for the interval
            - Practise chords and scales too
            - Choose which intervals to include
            - Replay the sound as often as needed
            - Track accuracy per interval
Storage:    SQLite local database
Tech stack: Python, PySide6, FluidSynth
```

---

## Example 266

**Intent:**
physics sandbox where you draw shapes and they fall

**Spec:**
```
Type:       Browser game (sandbox)
Features:   - Draw freehand shapes that become rigid bodies
            - Add joints, springs and motors
            - Pause, step and reset the simulation
            - Drag objects with the mouse
            - Save and share scenes as JSON
Tech stack: JavaScript, Matter.js
```

---

## Example 267

**Intent:**
hey, I run a tiny bike repair shop, and I keep losing track of which bikes are in, what's wrong with them, and whether the customer was told it's ready. Something simple on our counter PC please.

**Spec:**
```
Type:       Desktop application (repair tracker)
Data model: Customer(id, name, phone)
            RepairJob(id, customer_id -> Customer, bike_description, problem, status, quote, received_on, ready_on, notified)
Features:   - Check in a bike with customer and problem description
            - Move jobs through received, in progress, waiting for parts and ready
            - Mark whether the customer was called
            - Print a tag for the bike
            - List jobs ready but not collected
Storage:    SQLite local database
Tech stack: Python, PySide6
```

---

## Example 268

**Intent:**
game where you design a roller coaster and riders rate it

**Spec:**
```
Type:       Desktop game (simulation)
Features:   - Build track pieces on a 3D grid
            - Simulate the cart with speed and g-forces along the track
            - Rate excitement and nausea from the ride data
            - Run test rides with a camera
            - Earn money to unlock new pieces
Storage:    Local save files
Tech stack: Unity, C#
```

---

## Example 269

**Intent:**
desktop countdown to events like birthdays and holidays

**Spec:**
```
Type:       Desktop application (widget)
Data model: Event(id, name, date, repeats_yearly, colour)
Features:   - Add events with a date and colour
            - Show days left in a small desktop widget
            - Repeat birthdays every year
            - Notify a day before
            - Sort by soonest
Storage:    Local JSON file
Tech stack: Electron
```

---

## Example 270

**Intent:**
a game where you play as a bus driver picking up passengers on time

**Spec:**
```
Type:       Desktop game (driving simulation)
Features:   - Drive a bus through a 3D city with arcade handling
            - Stop at bus stops to load passengers
            - Follow a timetable and earn bonuses for being on time
            - Lose rating for rough braking
            - Unlock new routes
Storage:    Local save files
Tech stack: Unreal Engine 5, Blueprints
```

---

## Example 271

**Intent:**
tool to compare two folders and show differences

**Spec:**
```
Type:       Desktop application (folder compare)
Features:   - Pick two folders
            - Compare by name, size and checksum
            - Show files only on the left, only on the right or changed
            - Copy selected files across
            - Show a text diff for changed text files
Tech stack: Python, PyQt6, difflib
```

---

## Example 272

**Intent:**
puzzle game about untangling headphone cables

**Spec:**
```
Type:       Mobile game (puzzle)
Features:   - Show nodes connected by tangled cables
            - Drag nodes to remove all crossings
            - Detect line segment intersections live
            - Generate levels with more nodes over time
            - Rate by moves used
Tech stack: Swift, SpriteKit
```

---

## Example 273

**Intent:**
image tagger that uses ai to auto tag my photos so i can search them

**Spec:**
```
Type:       Desktop application (photo search)
Data model: Photo(id, path, embedding, auto_tags, taken_at)
            Tag(id, name)
Features:   - Index a photo folder in the background
            - Generate tags with an on-device image model
            - Search photos with natural language using CLIP embeddings
            - Edit or add tags manually
            - Show results in a thumbnail grid
Storage:    SQLite with embeddings stored as blobs
Tech stack: Python, PySide6, open_clip, PyTorch
```

---

## Example 274

**Intent:**
a 'which is heavier' game for kids

**Spec:**
```
Type:       Browser game (educational)
Features:   - Show two objects on a balance scale
            - Let the child tap the heavier one
            - Animate the scale tipping to show the answer
            - Use everyday objects with real weights
            - Count correct answers in a round of ten
Tech stack: JavaScript, HTML5 Canvas
```

---

## Example 275

**Intent:**
speech to text dictation app desktop offline

**Spec:**
```
Type:       Desktop application (dictation)
Features:   - Start and stop dictation with a global hotkey
            - Transcribe speech locally with Whisper
            - Type the text into the currently focused app
            - Add punctuation automatically
            - Choose language and model size
Tech stack: Python, faster-whisper, sounddevice, pynput
```

---

## Example 276

**Intent:**
game where an octopus escapes an aquarium with 8 arms you control separately

**Spec:**
```
Type:       Desktop game (physics puzzle)
Features:   - Control each tentacle with a different key or gamepad axis
            - Simulate tentacles as physics chains
            - Grab objects and walls with suction
            - Climb out of tanks and across the lab
            - Use checkpoints between rooms
Tech stack: Godot 4, GDScript
```

---

## Example 277

**Intent:**
Need program for car rental company, cars, customers, contracts, daily price

**Spec:**
```
Type:       Desktop application (rental management)
Data model: Car(id, plate, model, daily_price, status)
            Customer(id, name, licence_no, phone)
            Contract(id, car_id -> Car, customer_id -> Customer, start_date, end_date, deposit, total)
Features:   - Show which cars are available for a date range
            - Create rental contracts with price calculation
            - Print a contract PDF to sign
            - Record returns with mileage and damages
            - Report revenue per car
Storage:    SQLite local database
Tech stack: Java, JavaFX, iText
```

---

## Example 278

**Intent:**
browser party game where everyone draws a monster part and they get combined

**Spec:**
```
Type:       Browser game (party, multiplayer)
Data model: Room(id, code, round)
            Player(id, room_id -> Room, name)
            Drawing(id, room_id -> Room, player_id -> Player, part, image_data)
Features:   - Join a room with a code
            - Assign each player a head, body or legs to draw
            - Hide other parts while drawing
            - Combine parts into finished monsters and reveal them
            - Vote for the funniest monster
Storage:    In-memory rooms
Tech stack: Node.js, Socket.IO, HTML5 Canvas
```

---

## Example 279

**Intent:**
audio visualizer for my music

**Spec:**
```
Type:       Desktop application (music visualiser)
Features:   - Capture system audio output
            - Run an FFT to get frequency bands
            - Draw bars, circles and particle effects that move to the music
            - Switch visual presets
            - Go full screen on a second monitor
Tech stack: C++, openFrameworks
```

---

## Example 280

**Intent:**
a word search generator and game

**Spec:**
```
Type:       Desktop application (word search)
Features:   - Enter a word list or choose a theme
            - Place words in a grid in eight directions
            - Play by dragging across letters
            - Print the puzzle with an answer key
            - Set grid size and difficulty
Tech stack: Python, Tkinter
```

---

## Example 281

**Intent:**
idle game where you run a space station

**Spec:**
```
Type:       Mobile game (idle)
Data model: SaveState(credits, modules_json, crew, research, last_online_at)
Features:   - Build station modules that produce oxygen, power and credits
            - Assign crew to modules
            - Balance power use against generation
            - Research upgrades over real time
            - Calculate offline progress
Storage:    Local save file
Tech stack: Godot 4, GDScript
```

---

## Example 282

**Intent:**
offline app to write screenplays with right formatting

**Spec:**
```
Type:       Desktop application (screenwriting)
Data model: Script(id, title, author)
            Element(id, script_id -> Script, type, text, position)
Features:   - Format scene headings, action, character and dialogue automatically
            - Switch element type with Tab and Enter
            - Show a scene navigator
            - Count pages
            - Export to PDF and Fountain
Storage:    Fountain text files
Tech stack: Electron, CodeMirror
```

---

## Example 283

**Intent:**
tank battle game local network

**Spec:**
```
Type:       Desktop game (multiplayer, LAN)
Features:   - Host a game and discover it on the local network
            - Drive tanks in a destructible arena
            - Fire shells that bounce off walls
            - Sync positions with client-side prediction
            - Keep score over five-minute matches
Tech stack: C#, MonoGame, LiteNetLib
```

---

## Example 284

**Intent:**
an app that tells me which photos are blurry so i can delete them

**Spec:**
```
Type:       Desktop application (photo cleanup)
Features:   - Scan a photo folder
            - Score sharpness with Laplacian variance
            - Flag closed eyes with face landmark detection
            - Show flagged photos for review
            - Move rejected photos to a separate folder
Tech stack: Python, OpenCV, PySide6
```

---

## Example 285

**Intent:**
a puzzle game that teaches programming with arrows

**Spec:**
```
Type:       Browser game (educational programming)
Features:   - Drag arrow and loop blocks into a program slot
            - Run the program to move a robot on a grid
            - Add conditions like if wall turn right
            - Unlock levels that need loops and functions
            - Show the number of blocks used
Storage:    Browser localStorage
Tech stack: TypeScript, Blockly, Phaser 3
```

---

## Example 286

**Intent:**
desktop tool to find and replace text in many files

**Spec:**
```
Type:       Desktop application (text utility)
Features:   - Choose a folder and file pattern
            - Search with plain text or regex
            - Preview every match with context
            - Replace selected matches
            - Back up files before changing them
Tech stack: Rust, egui, regex crate
```

---

## Example 287

**Intent:**
gardening planner offline

**Spec:**
```
Type:       Desktop application (garden planner)
Data model: Bed(id, name, width_cm, length_cm)
            Planting(id, bed_id -> Bed, plant_name, sow_date, x, y, harvested_on)
Features:   - Draw garden beds on a grid
            - Place plants with spacing guides
            - Show sowing and harvest dates on a calendar
            - Warn about bad companion plants
            - Remember past years for crop rotation
Storage:    SQLite local database
Tech stack: Python, PySide6
```

---

## Example 288

**Intent:**
quiz show buzzer system for school competition using usb buttons

**Spec:**
```
Type:       Desktop application (quiz buzzer)
Data model: Team(id, name, buzzer_key, score)
Features:   - Map each USB buzzer to a team
            - Lock out other teams after the first buzz
            - Show which team buzzed first with a sound
            - Let the host add or remove points
            - Show the scoreboard on a projector
Tech stack: Python, Pygame (joystick input)
```

---

## Example 289

**Intent:**
mobile game where you balance a stack of rocks

**Spec:**
```
Type:       Mobile game (physics)
Features:   - Drop rocks of random shapes onto a stack
            - Use 2D physics so the stack can topple
            - Rotate the rock before dropping
            - Score by stack height
            - Play calm ambient sounds
Tech stack: Unity, C#
```

---

## Example 290

**Intent:**
an app to keep my exam notes and generate quizzes from them

**Spec:**
```
Type:       Desktop application (study tool)
Data model: Note(id, subject, title, body)
            Question(id, note_id -> Note, text, answer, generated)
Features:   - Write notes by subject
            - Generate quiz questions from notes with a local language model
            - Edit generated questions
            - Run a quiz and track scores
            - Show weak topics
Storage:    SQLite local database
Tech stack: Python, PySide6, llama-cpp-python
```

---

## Example 291

**Intent:**
sokoban-like game where boxes are slippery ice

**Spec:**
```
Type:       Browser game (puzzle)
Data model: Level(id, grid, box_positions, targets)
Features:   - Push ice blocks that slide until they hit something
            - Move the player on a tile grid
            - Win when all blocks are on targets
            - Undo and restart
            - Load levels from a text format
Storage:    Browser localStorage
Tech stack: JavaScript, HTML5 Canvas
```

---

## Example 292

**Intent:**
yo can u spec a game wher ur a goose causing chaos in a park lol

**Spec:**
```
Type:       Desktop game (sandbox comedy)
Features:   - Waddle around a 3D park as a goose
            - Honk to scare park visitors with simple AI reactions
            - Grab and drag objects with the beak
            - Complete a to-do list of mischief goals
            - Save completed goals
Tech stack: Unity, C#
```

---

## Example 293

**Intent:**
need app 2 track my weed... i mean my lawn mowing business lol, clients and dates and payments

**Spec:**
```
Type:       Desktop application (offline business tool)
Data model: Client(id, name, address, phone, rate)
            Job(id, client_id -> Client, date, duration_min, price, paid)
Features:   - Keep a client list with addresses and rates
            - Schedule recurring mowing jobs
            - Mark jobs done and paid
            - Show unpaid jobs per client
            - Print a monthly statement
Storage:    SQLite local database
Tech stack: Python, Tkinter
```

---

## Example 294

**Intent:**
i want somthing to make my desktop icons hide when im not using the mouse

**Spec:**
```
Type:       Desktop application (system tray)
Features:   - Detect mouse and keyboard idle time
            - Hide desktop icons after a set idle delay
            - Show them again on mouse movement
            - Exclude times when a fullscreen app runs
            - Toggle from the tray
Tech stack: C++, Win32 API
```

---

## Example 295

**Intent:**
math game where numbers are falling and u make 10 by clicking two

**Spec:**
```
Type:       Browser game (math puzzle)
Features:   - Drop numbered bubbles from the top
            - Select two bubbles that add to 10 to pop them
            - End when bubbles reach the floor
            - Add bigger targets like 20 in later levels
            - Show score and combos
Tech stack: JavaScript, HTML5 Canvas
```

---

## Example 296

**Intent:**
plz make spec for app that shows lyrics of the song playing on spotify on my desktop

**Spec:**
```
Type:       Desktop application (lyrics overlay)
Auth:       Spotify OAuth login (PKCE)
Features:   - Read the currently playing track from the Spotify Web API
            - Fetch time-synced lyrics from a lyrics provider
            - Show the current line in a transparent always-on-top overlay
            - Adjust font size and position
            - Hide the overlay when nothing is playing
Tech stack: Electron, Spotify Web API, LRCLIB API
```

---

## Example 297

**Intent:**
my teenage son wants to learn programming by making a game, he likes football, can you plan a simple penalty kick game for him in python

**Spec:**
```
Type:       Desktop game (sports)
Features:   - Aim the shot with the mouse and set power with a timing bar
            - Move the goalkeeper to a random side with a short delay
            - Detect if the ball hits the goal area, the keeper or misses
            - Play a best of five shootout
            - Show score and simple animations
Tech stack: Python, Pygame
```

---

## Example 298

**Intent:**
kanji learning game for my phone with writing practice

**Spec:**
```
Type:       Mobile game (language learning)
Data model: Kanji(id, character, meanings, readings, stroke_paths, jlpt_level)
            Progress(kanji_id -> Kanji, level, next_review_at)
Features:   - Show a kanji's meaning and ask the player to draw it
            - Compare strokes to the correct order and direction
            - Review with spaced repetition
            - Filter by JLPT level
            - Earn points to unlock themed decks
Storage:    Local SQLite
Tech stack: Kotlin, Jetpack Compose
```

---

## Example 299

**Intent:**
a tool for my comic that lets me lay out panels and add speech bubbles

**Spec:**
```
Type:       Desktop application (comic layout)
Data model: Page(id, number, panels_json)
            Bubble(id, page_id -> Page, panel_index, text, shape, x, y)
Features:   - Choose a panel layout for each page
            - Place artwork into panels with cropping
            - Add speech and thought bubbles with tails
            - Edit text with comic fonts
            - Export pages to PNG and PDF
Storage:    Local project folder (JSON + images)
Tech stack: C++, Qt 6
```

---

## Example 300

**Intent:**
offline accounting for small shop, sales purchases tax report, we are in Pakistan, urdu and english

**Spec:**
```
Type:       Desktop application (accounting)
Data model: Account(id, name, type)
            Voucher(id, date, kind, description)
            Entry(id, voucher_id -> Voucher, account_id -> Account, debit, credit)
Features:   - Record sales and purchase vouchers with double entry
            - Show ledger and trial balance
            - Calculate sales tax for the period
            - Switch the interface between Urdu and English
            - Print reports to PDF
Storage:    SQLite local database
Tech stack: Python, PySide6 (Qt translations), ReportLab
```

---

## Example 301

**Intent:**
farm game but you're a bee keeper

**Spec:**
```
Type:       Mobile game (simulation)
Data model: Hive(id, bees, honey_ml, health, queen_age)
            SaveState(day, coins, hives_json)
Features:   - Place hives in a meadow and plant flowers nearby
            - Grow bee population based on nearby flowers
            - Harvest honey and sell it at the market
            - Treat hives for mites
            - Change seasons that affect flowers
Storage:    Local save file
Tech stack: Flutter, Flame
```

---

## Example 302

**Intent:**
Write me a spec for a desktop app that opens and edits CSV files like a spreadsheet but stays fast with million-row files.

**Spec:**
```
Type:       Desktop application (CSV editor)
Features:   - Open large CSV files using memory-mapped lazy loading
            - Show rows in a virtualised grid
            - Sort and filter by column
            - Edit cells and save changes
            - Detect delimiter and encoding automatically
Tech stack: Rust, egui, csv crate
```

---

## Example 303

**Intent:**
game where you are a delivery drone avoiding birds

**Spec:**
```
Type:       Browser game (arcade)
Features:   - Fly the drone with arrow keys in a side view
            - Pick up parcels and drop them on marked rooftops
            - Avoid flocks of birds and power lines
            - Manage battery and recharge on pads
            - Score deliveries before time runs out
Tech stack: TypeScript, Phaser 3
```

---

## Example 304

**Intent:**
i want a calculator for programmers on the desktop

**Spec:**
```
Type:       Desktop application (calculator)
Features:   - Calculate in decimal, hex, octal and binary
            - Show bitwise AND, OR, XOR and shifts
            - Toggle individual bits in a bit grid
            - Switch between 8, 16, 32 and 64-bit words
            - Keep a history of calculations
Tech stack: C#, WinUI 3
```

---

## Example 305

**Intent:**
ok weird idea but a game where you're a ghost and you have to scare people out of your house but you're really bad at it

**Spec:**
```
Type:       Desktop game (comedy puzzle)
Features:   - Possess household objects to move them
            - Pick scare actions with chances of making people laugh instead
            - Track a fear meter for each resident
            - Chain scares in the right order to fill fear meters
            - Win when all residents move out
Tech stack: Godot 4, GDScript
```

---

## Example 306

**Intent:**
picture in picture app that keeps a video always on top while i work

**Spec:**
```
Type:       Desktop application (media player)
Features:   - Play a local video or stream URL in a small borderless window
            - Keep the window always on top
            - Resize and snap to screen corners
            - Set opacity and click-through mode
            - Control with media keys
Tech stack: Electron, libmpv
```

---

## Example 307

**Intent:**
dungeon game where the map is drawn by the player before entering

**Spec:**
```
Type:       Desktop game (roguelike)
Features:   - Draw the dungeon layout with room and corridor tools
            - Fill drawn rooms with procedurally chosen monsters and loot
            - Enter the dungeon in top-down view
            - Fight in real time
            - Score by gold collected versus rooms drawn
Tech stack: Python, Arcade
```

---

## Example 308

**Intent:**
a better alt tab

**Spec:**
```
Type:       Desktop application (window switcher)
Features:   - Open a switcher with a hotkey that shows live window thumbnails
            - Filter windows by typing part of the title
            - Group windows by application
            - Close windows from the switcher
            - Remember the most recently used order
Tech stack: C++, Win32 API, DWM thumbnail API
```

---

## Example 309

**Intent:**
offline sheet music library for my band

**Spec:**
```
Type:       Desktop application (sheet music manager)
Data model: Score(id, title, composer, file_path, key, tags)
            Setlist(id, name, date)
            SetlistItem(setlist_id -> Setlist, score_id -> Score, position)
Features:   - Import PDF scores with title and composer
            - Tag by genre and key
            - Build setlists for gigs
            - Show scores full screen with page turns by pedal
            - Print a setlist
Storage:    SQLite local database
Tech stack: Python, PySide6, PyMuPDF
```

---

## Example 310

**Intent:**
math puzzle where you balance equations on a seesaw, for browser

**Spec:**
```
Type:       Browser game (math puzzle)
Features:   - Show a seesaw with number weights on one side
            - Drag number and operator blocks to balance it
            - Tip the seesaw animation based on the difference
            - Introduce unknowns like x in later levels
            - Give hints after three wrong tries
Storage:    Browser localStorage
Tech stack: JavaScript, Svelte
```

---

## Example 311

**Intent:**
windows app that tells me when someone is using my webcam

**Spec:**
```
Type:       Desktop application (privacy monitor)
Features:   - Watch webcam and microphone usage via registry consent store
            - Show which app is using the camera
            - Notify when a new app starts using it
            - Log usage history
            - Show a coloured tray icon while in use
Storage:    SQLite (usage log)
Tech stack: C#, .NET
```

---

## Example 312

**Intent:**
dino island survival game for mobile, small and offline

**Spec:**
```
Type:       Mobile game (survival)
Features:   - Explore a small island in top-down view
            - Gather wood and stone to craft tools
            - Avoid or fight dinosaurs with simple AI states
            - Build a raft to escape
            - Save automatically at camp
Storage:    Local save file
Tech stack: Unity, C#
```

---

## Example 313

**Intent:**
i draw on my wacom and want a reference image window that floats over my art program

**Spec:**
```
Type:       Desktop application (reference viewer)
Features:   - Paste or drop reference images into a floating window
            - Keep the window always on top
            - Zoom, flip and grayscale images
            - Make the window click-through
            - Arrange multiple references on a board
Storage:    Local session file (JSON)
Tech stack: C++, Qt 6
```

---

## Example 314

**Intent:**
game to teach kids saving money with a piggy bank

**Spec:**
```
Type:       Mobile game (educational)
Features:   - Earn coins by doing simple in-game chores
            - Decide to spend or save in a piggy bank
            - Set a saving goal for a toy
            - Add interest to savings each week
            - Show a chart of saved coins
Storage:    Local storage
Tech stack: Flutter
```

---

## Example 315

**Intent:**
Hi, I'd like a little app on my Mac that lets me set up different "modes" — work, gaming, sleep — and when I click one it changes my volume, opens certain apps, closes others, and switches dark mode.

**Spec:**
```
Type:       Desktop application (menu bar)
Data model: Mode(id, name, volume, dark_mode, apps_to_open, apps_to_close, do_not_disturb)
Features:   - Create modes with volume, dark mode and app lists
            - Switch modes from the menu bar
            - Open and quit apps for each mode
            - Toggle macOS dark mode
            - Assign a keyboard shortcut per mode
Storage:    Local JSON config
Tech stack: Swift, SwiftUI, AppleScript bridge
```

---

## Example 316

**Intent:**
cookie clicker style but you are a volcano

**Spec:**
```
Type:       Browser game (idle)
Data model: SaveState(magma, eruptions, upgrades_json, last_tick_at)
Features:   - Click the volcano to build magma
            - Buy upgrades like vents and lava tubes for passive magma
            - Trigger eruptions that convert magma to land
            - Grow an island as eruptions add land
            - Save progress every 30 seconds
Storage:    Browser localStorage
Tech stack: JavaScript, HTML, CSS
```

---

## Example 317

**Intent:**
desktop calendar for my shift work that understands rotating shifts

**Spec:**
```
Type:       Desktop application (shift planner)
Data model: ShiftPattern(id, name, cycle_days, sequence)
            Override(id, date, shift_code, note)
Features:   - Define a rotating shift pattern like 4 on 4 off
            - Show the pattern on a month calendar
            - Override single days for swaps and holidays
            - Count hours worked per month
            - Export to iCal
Storage:    SQLite local database
Tech stack: Python, PySide6, icalendar
```

---

## Example 318

**Intent:**
puzzle game where you rotate a room to make a ball fall into a hole, gravity

**Spec:**
```
Type:       Mobile game (gravity puzzle)
Features:   - Rotate the room 90 degrees with swipes
            - Let the ball fall with gravity after each rotation
            - Add crates that also fall and block paths
            - Win when the ball reaches the hole
            - Count rotations for stars
Tech stack: Godot 4, GDScript
```

---

## Example 319

**Intent:**
video downloader from my own security camera sd card files, they are weird format

**Spec:**
```
Type:       Desktop application (video converter)
Features:   - Scan the SD card for camera recording files
            - Read timestamps from file names
            - Remux raw H.264 streams into MP4
            - Join clips from the same hour
            - Show a timeline to pick clips to export
Input:      SD card folder with proprietary .h264 camera files
Tech stack: Python, FFmpeg, PySide6
```

---

## Example 320

**Intent:**
idle space trading game multiplayer leaderboard

**Spec:**
```
Type:       Browser game (idle, online leaderboard)
Auth:       Guest account with generated name, optional email login
Data model: Player(id, name, credits, ships, updated_at)
            Route(id, player_id -> Player, from_planet, to_planet, cargo)
Features:   - Set up trade routes between planets
            - Earn credits over time from active routes
            - Upgrade cargo ships
            - Submit net worth to a global leaderboard
            - Sync saves to the server
Storage:    PostgreSQL
Tech stack: TypeScript, React, Node.js, Fastify
```

---

## Example 321

**Intent:**
app to practice morse code

**Spec:**
```
Type:       Desktop application (morse trainer)
Features:   - Play random letters as morse audio at a set WPM
            - Type the letter heard and score it
            - Learn with the Koch method one letter at a time
            - Key morse with the space bar and decode it
            - Track accuracy per letter
Storage:    SQLite local database
Tech stack: Python, Pygame, NumPy (tone generation)
```

---

## Example 322

**Intent:**
give me a game where you control two characters with one stick each on a gamepad at the same time

**Spec:**
```
Type:       Desktop game (coordination)
Features:   - Move the left character with the left stick and the right with the right stick
            - Split the screen into two lanes with obstacles
            - Require both characters to survive
            - Add sync gates that need both to press at once
            - Increase scroll speed over time
Tech stack: Godot 4, GDScript
```

---

## Example 323

**Intent:**
offline quotation maker for construction work

**Spec:**
```
Type:       Desktop application (quoting)
Data model: Material(id, name, unit, unit_price)
            Quote(id, client_name, site_address, created_on, total)
            QuoteLine(id, quote_id -> Quote, material_id -> Material, quantity, labour_hours)
Features:   - Keep a materials price list
            - Build quotes from materials and labour
            - Add margin and VAT
            - Print a branded PDF quote
            - Convert an accepted quote to an invoice
Storage:    SQLite local database
Tech stack: C#, .NET 8, WPF, QuestPDF
```

---

## Example 324

**Intent:**
pong but 4 players

**Spec:**
```
Type:       Desktop game (local multiplayer)
Features:   - Place four paddles on four sides of a square arena
            - Map each paddle to different keys or gamepads
            - Bounce the ball with angle based on hit position
            - Eliminate a player after 5 goals
            - Replace absent players with AI
Tech stack: Lua, LÖVE
```

---

## Example 325

**Intent:**
audio cutter for ringtones

**Spec:**
```
Type:       Desktop application (audio editor)
Features:   - Open MP3, WAV and M4A files with a waveform
            - Select a range with draggable handles
            - Fade in and out
            - Preview the selection
            - Export as M4R or MP3
Tech stack: Electron, wavesurfer.js, FFmpeg
```

---

## Example 326

**Intent:**
app to show my code coding stats... no wait, a game to learn git commands

**Spec:**
```
Type:       Browser game (educational)
Features:   - Show a visual commit graph
            - Ask the player to reach a goal state using typed git commands
            - Simulate commit, branch, merge and rebase in memory
            - Unlock levels from basics to rebasing
            - Give hints and show the solution
Storage:    Browser localStorage
Tech stack: TypeScript, D3.js
```

---

## Example 327

**Intent:**
a desktop app that reads my kindle highlights file and organises them

**Spec:**
```
Type:       Desktop application (highlights manager)
Features:   - Import and parse My Clippings.txt
            - Group highlights by book
            - Remove duplicate highlights
            - Search across all highlights
            - Export a book's highlights to Markdown
Input:      My Clippings.txt file from a Kindle
Storage:    SQLite local database
Tech stack: Python, PySide6
```

---

## Example 328

**Intent:**
maze generator for kids to print

**Spec:**
```
Type:       Desktop application (puzzle maker)
Features:   - Generate rectangular or circular mazes
            - Set size and difficulty
            - Add start and end pictures
            - Print the maze with a separate solution page
            - Export as PDF or PNG
Tech stack: Python, Tkinter, ReportLab
```

---

## Example 329

**Intent:**
an rts game where you control ants vs termites with simple graphics

**Spec:**
```
Type:       Desktop game (real-time strategy)
Features:   - Select units with box selection
            - Gather food with worker units
            - Build nest chambers to unlock soldier types
            - Path-find units with A* on a grid
            - Fight termite AI that expands its mound
Tech stack: C#, MonoGame
```

---

## Example 330

**Intent:**
lightweight screen annotation for live demos, draw on top of everything

**Spec:**
```
Type:       Desktop application (screen annotation)
Features:   - Draw over the whole screen in a transparent overlay
            - Toggle draw mode with a hotkey
            - Highlight the mouse cursor with a circle
            - Show key presses on screen
            - Clear drawings with Esc
Tech stack: Rust, Tauri
```

---

## Example 331

**Intent:**
guess the song from a 1 second clip game, using my own mp3s

**Spec:**
```
Type:       Desktop game (music quiz)
Features:   - Scan the user's music folder for tracks
            - Play a random 1-second clip
            - Offer four title choices from the library
            - Extend the clip on wrong answers
            - Keep a score for up to 4 players
Tech stack: Python, Pygame, mutagen
```

---

## Example 332

**Intent:**
windows app to bulk compress pdfs for email

**Spec:**
```
Type:       Desktop application (PDF tool)
Features:   - Add PDFs by drag and drop
            - Compress images inside with a quality preset
            - Show size before and after
            - Keep originals and save compressed copies
            - Process files in parallel
Tech stack: C#, .NET, Ghostscript
```

---

## Example 333

**Intent:**
game about cleaning up a beach where you sort trash and save turtles

**Spec:**
```
Type:       Mobile game (casual educational)
Features:   - Rake the beach by swiping to uncover trash
            - Sort collected trash into recycling bins
            - Help baby turtles reach the sea
            - Show facts about ocean pollution
            - Unlock new beaches
Tech stack: Unity, C#
```

---

## Example 334

**Intent:**
habit tracker that lives in my menu bar, check off habits daily

**Spec:**
```
Type:       Desktop application (menu bar)
Data model: Habit(id, name, target_days_per_week, colour)
            CheckIn(habit_id -> Habit, date)
Features:   - Add habits with a weekly target
            - Tick habits off from the menu bar dropdown
            - Show current streaks
            - Show a year heatmap per habit
            - Remind at a chosen time if habits are unchecked
Storage:    Local SQLite
Tech stack: Swift, SwiftUI (MenuBarExtra)
```

---

## Example 335

**Intent:**
golf game on tiny planets

**Spec:**
```
Type:       Browser game (sports, physics)
Features:   - Aim and set power by dragging back from the ball
            - Simulate radial gravity around each small planet
            - Slingshot the ball between planets toward the hole
            - Count strokes per hole against par
            - Show a scorecard for 9 holes
Storage:    Browser localStorage
Tech stack: TypeScript, Phaser 3, Matter.js
```

---

## Example 336

**Intent:**
emoji picker app

**Spec:**
```
Type:       Desktop application (utility)
Features:   - Open a searchable emoji panel with a hotkey
            - Search emojis by name and keyword
            - Insert the chosen emoji into the active app
            - Show recently used emojis
            - Pick skin tones
Tech stack: Tauri, Svelte
```

---

## Example 337

**Intent:**
a card battle game where cards are kitchen ingredients and you cook combos

**Spec:**
```
Type:       Mobile game (card battler)
Data model: Card(id, name, flavour_type, power, cost)
            Deck(id, card_ids)
Features:   - Draw ingredient cards each turn
            - Combine ingredients into dishes for bonus damage
            - Battle AI chefs with health bars
            - Earn new cards after wins
            - Build and save custom decks
Storage:    Local SQLite
Tech stack: Unity, C#
```

---

## Example 338

**Intent:**
tray app for quick unit conversions

**Spec:**
```
Type:       Desktop application (system tray)
Features:   - Open a converter popup from the tray or a hotkey
            - Parse input like 5 ft in cm
            - Support length, weight, temperature and volume
            - Fetch currency rates once a day
            - Copy the result on Enter
Storage:    Local cache file (currency rates)
Tech stack: Python, PyQt6, pint
```

---

## Example 339

**Intent:**
I want to make a visual novel about a girl who moves to a new city, using renpy

**Spec:**
```
Type:       Desktop game (visual novel)
Data model: SaveSlot(id, label, variables, screenshot, saved_at)
Features:   - Show backgrounds, character sprites and dialogue boxes
            - Branch the story with player choices
            - Track relationship points with characters
            - Unlock multiple endings
            - Save, load and skip read text
Storage:    Ren'Py save files
Tech stack: Ren'Py, Python
```

---

## Example 340

**Intent:**
realy simple video editor for my kid youtube channel, cut, music, text

**Spec:**
```
Type:       Desktop application (video editor)
Features:   - Import clips onto a single timeline
            - Cut and trim clips
            - Add background music with volume control
            - Add title text with simple animations
            - Export to 1080p MP4 for YouTube
Tech stack: Electron, FFmpeg, React
```

---

## Example 341

**Intent:**
robot battle game where you program your robot with simple code before the fight

**Spec:**
```
Type:       Desktop game (programming strategy)
Features:   - Write robot behaviour in a simple script editor
            - Run the script in a sandboxed interpreter each tick
            - Simulate battles in an arena with sensors and weapons
            - Replay fights
            - Run tournaments between saved robots
Storage:    Local robot script files
Tech stack: Python, Pygame, Lua (via lupa) for robot scripts
```

---

## Example 342

**Intent:**
what would a mobile game about a lost balloon floating up look like

**Spec:**
```
Type:       Mobile game (endless vertical)
Features:   - Float the balloon upward automatically
            - Tilt the phone to move sideways
            - Avoid birds, branches and planes
            - Collect helium cans to stay afloat
            - Change backgrounds from city to space as height grows
Tech stack: Swift, SpriteKit, CoreMotion
```

---

## Example 343

**Intent:**
file encryptor desktop drag and drop

**Spec:**
```
Type:       Desktop application (encryption)
Features:   - Drop files to encrypt them with a password
            - Derive the key with Argon2id
            - Encrypt with AES-256-GCM into a .enc file
            - Decrypt by dropping .enc files
            - Securely delete originals on request
Tech stack: Rust, Tauri
```

---

## Example 344

**Intent:**
a sheep counting game to help kids fall asleep

**Spec:**
```
Type:       Mobile game (calm, bedtime)
Features:   - Show sheep jumping over a fence slowly
            - Tap to count each sheep aloud
            - Dim the screen and slow the music over time
            - Stop automatically after a set number
            - Use a dark warm colour theme
Tech stack: Flutter, just_audio
```

---

## Example 345

**Intent:**
desktop app for my dnd sessions, initiative tracker and monsters

**Spec:**
```
Type:       Desktop application (tabletop RPG helper)
Data model: Monster(id, name, ac, hp, stats_json)
            Encounter(id, name)
            Combatant(id, encounter_id -> Encounter, name, initiative, current_hp, conditions)
Features:   - Add players and monsters to an encounter
            - Roll and sort initiative
            - Track HP and conditions per combatant
            - Step through turns and rounds
            - Show monster stat blocks
Storage:    SQLite local database
Tech stack: Python, PySide6
```

---

## Example 346

**Intent:**
plane game where you fly between clouds in 3d, chill no enemies

**Spec:**
```
Type:       Desktop game (relaxing flight)
Features:   - Fly a small plane with simple arcade controls
            - Generate volumetric-looking clouds and islands
            - Collect floating rings for music notes
            - Change time of day
            - Take in-game photos
Tech stack: Unity, C#, Universal Render Pipeline
```

---

## Example 347

**Intent:**
launcher bar at the top of the screen with my favourite folders and apps

**Spec:**
```
Type:       Desktop application (dock)
Data model: DockItem(id, label, path, icon_path, position)
Features:   - Show a slim bar docked to the top edge
            - Add apps, folders and URLs by drag and drop
            - Reorder items
            - Auto-hide when not hovered
            - Show running app indicators
Storage:    Local JSON config
Tech stack: C#, .NET, WPF
```

---

## Example 348

**Intent:**
wordle like game but with numbers and maths

**Spec:**
```
Type:       Browser game (daily puzzle)
Features:   - Pick a daily hidden equation like 12+35=47
            - Accept guesses that are valid equations
            - Colour each character as correct, present or absent
            - Allow six guesses
            - Share a result grid as emoji
Storage:    Browser localStorage (streaks)
Tech stack: TypeScript, React
```

---

## Example 349

**Intent:**
i need program to manage my students grades, i am teacher in Morocco, many classes, print report card

**Spec:**
```
Type:       Desktop application (gradebook)
Data model: Class(id, name, year)
            Student(id, class_id -> Class, name)
            Subject(id, name, coefficient)
            Grade(id, student_id -> Student, subject_id -> Subject, term, value)
Features:   - Add classes, students and subjects
            - Enter grades per term in a table
            - Calculate weighted averages with coefficients
            - Rank students in each class
            - Print report cards in French or Arabic
Storage:    SQLite local database
Tech stack: Python, PySide6, ReportLab
```

---

## Example 350

**Intent:**
browser game about stacking delivery boxes in a truck efficiently

**Spec:**
```
Type:       Browser game (packing puzzle)
Features:   - Show the truck cargo area as a 2D grid
            - Drag and rotate boxes of different shapes into it
            - Require fragile boxes to be on top
            - Score by space used
            - Unlock bigger trucks and odd shapes
Tech stack: JavaScript, PixiJS
```

---

## Example 351

**Intent:**
tool to turn my handwriting into a font

**Spec:**
```
Type:       Desktop application (font creation)
Features:   - Print a template sheet with a box per character
            - Scan the filled sheet and detect boxes
            - Vectorise each glyph
            - Adjust spacing and baseline
            - Export a TTF font
Tech stack: Python, OpenCV, potrace, fontTools
```

---

## Example 352

**Intent:**
chess clock app

**Spec:**
```
Type:       Desktop application (game timer)
Features:   - Show two large clocks for two players
            - Switch clocks with spacebar or a click
            - Support increment and delay modes
            - Flash when time runs out
            - Save custom time controls
Tech stack: JavaScript, Electron
```

---

## Example 353

**Intent:**
game where you sail a boat with realistic wind

**Spec:**
```
Type:       Desktop game (sailing simulation)
Features:   - Simulate wind direction and sail angle to produce thrust
            - Steer with the rudder and trim the sail with keys
            - Race around buoys against the clock
            - Change wind gusts over time
            - Show a wind indicator and speed
Tech stack: Godot 4, C#
```

---

## Example 354

**Intent:**
plz help my mum she has a sewing business and wants to note measurements of each client

**Spec:**
```
Type:       Desktop application (client measurements)
Data model: Client(id, name, phone)
            Measurement(id, client_id -> Client, taken_on, bust, waist, hips, length, sleeve, notes)
            Order(id, client_id -> Client, garment, fabric, due_on, price, status)
Features:   - Store clients with their body measurements
            - Keep history of measurements over time
            - Record orders with due dates
            - Show orders due this week
            - Print a measurement sheet
Storage:    SQLite local database
Tech stack: Python, Tkinter
```

---

## Example 355

**Intent:**
shoot em up with bullet hell patterns

**Spec:**
```
Type:       Desktop game (bullet hell)
Features:   - Move a small ship with a tiny hitbox
            - Spawn bullet patterns from scripted spirals and waves
            - Pool bullets for performance
            - Use bombs to clear the screen
            - Fight a boss with phases
Tech stack: C++, SDL2
```

---

## Example 356

**Intent:**
an app that blocks my screen every 2 hours and makes me do stretches with pictures

**Spec:**
```
Type:       Desktop application (break reminder)
Data model: Stretch(id, name, image_path, duration_s)
Features:   - Show a full-screen break every 2 hours
            - Walk through stretches with pictures and timers
            - Allow skipping only after 10 seconds
            - Postpone during meetings by detecting full-screen apps
            - Count breaks taken per day
Storage:    Local JSON
Tech stack: Electron
```

---

## Example 357

**Intent:**
farming idle game where crops grow in real time even when the app is closed

**Spec:**
```
Type:       Mobile game (idle farming)
Data model: Field(id, crop, planted_at, grow_minutes)
            SaveState(coins, seeds_json)
Features:   - Plant crops that take real minutes to grow
            - Send a push notification when crops are ready
            - Harvest and sell crops
            - Expand fields with coins
            - Calculate growth from timestamps on app open
Storage:    Local SQLite
Tech stack: React Native, Expo Notifications
```

---

## Example 358

**Intent:**
a desktop thing where i can make a playlist that changes based on time of day

**Spec:**
```
Type:       Desktop application (media player)
Data model: Rule(id, start_time, end_time, playlist_folder, volume)
Features:   - Define time windows with a folder of songs each
            - Switch playlists automatically when the time changes
            - Fade between songs
            - Set volume per window
            - Run in the tray
Storage:    Local JSON rules
Tech stack: Python, python-vlc, pystray
```

---

## Example 359

**Intent:**
a mystery detective game where you read clues and accuse someone

**Spec:**
```
Type:       Desktop game (detective)
Data model: Case(id, title, suspects, clues, culprit)
            Notebook(case_id -> Case, found_clue_ids, notes)
Features:   - Explore crime scene rooms by clicking objects
            - Collect clues into a notebook
            - Interview suspects with dialogue trees
            - Link clues to suspects on a corkboard
            - Accuse a suspect and see the ending
Storage:    Local save file
Tech stack: Godot 4, GDScript, Dialogic
```

---

## Example 360

**Intent:**
app to make qr codes and print them

**Spec:**
```
Type:       Desktop application (QR generator)
Features:   - Generate QR codes for text, URL, Wi-Fi and contacts
            - Set colours and add a logo in the centre
            - Choose error correction level
            - Export PNG and SVG
            - Print a sheet of many codes
Tech stack: Python, qrcode, PySide6
```

---

## Example 361

**Intent:**
online word game for 2 players taking turns making words on a hex board

**Spec:**
```
Type:       Browser game (word game, multiplayer)
Auth:       Login with email magic link
Data model: Match(id, player1_id -> User, player2_id -> User, board, turn, status)
            User(id, email, name)
Features:   - Place letter tiles on a hexagonal board
            - Validate words against a dictionary
            - Score with bonus hexes
            - Play asynchronously with turn notifications
            - Show match history
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, PostgreSQL
```

---

## Example 362

**Intent:**
a desktop app for my tattoo studio with consent forms and photos

**Spec:**
```
Type:       Desktop application (studio management)
Data model: Client(id, name, birth_date, phone)
            Session(id, client_id -> Client, artist, date, description, price)
            ConsentForm(id, session_id -> Session, signature_image, signed_at)
            Photo(id, session_id -> Session, path)
Features:   - Book sessions with artists
            - Sign consent forms on a tablet screen
            - Check client age before booking
            - Attach before and after photos
            - Print a session summary
Storage:    SQLite local database, photos on disk
Tech stack: C#, .NET 8, WPF, InkCanvas
```

---

## Example 363

**Intent:**
a game about dodging raindrops as a sugar cube

**Spec:**
```
Type:       Browser game (arcade)
Features:   - Move the sugar cube left and right
            - Spawn raindrops that dissolve part of the cube
            - Shrink the cube on hits
            - Collect sugar crystals to regrow
            - End when the cube melts away
Tech stack: JavaScript, HTML5 Canvas
```

---

## Example 364

**Intent:**
midi file player with falling notes like a piano tutorial

**Spec:**
```
Type:       Desktop application (piano visualiser)
Features:   - Open MIDI files
            - Show notes falling onto an on-screen keyboard
            - Play with a General MIDI synth
            - Slow down and loop sections
            - Show left and right hand in different colours
Tech stack: C++, SFML, FluidSynth
```

---

## Example 365

**Intent:**
app in c# for cataloguing my coin collection

**Spec:**
```
Type:       Desktop application (collection catalogue)
Data model: Coin(id, country, year, denomination, mint_mark, condition, value, photo_front, photo_back)
Features:   - Add coins with photos of both sides
            - Filter by country, year and condition
            - Track estimated value and total collection worth
            - Mark coins wanted for a wish list
            - Export to Excel
Storage:    SQLite local database
Tech stack: C#, .NET 8, WPF, ClosedXML
```

---

## Example 366

**Intent:**
mobile game where you pop bubbles to free fish but its a calm game

**Spec:**
```
Type:       Mobile game (casual)
Features:   - Show bubbles rising with fish inside
            - Pop bubbles with a tap to free the fish
            - Fill an aquarium with freed fish
            - Play soft ambient sounds
            - Have no timer or fail state
Tech stack: Godot 4, GDScript
```

---

## Example 367

**Intent:**
a tool that renames tv episodes from s01e01 messy names

**Spec:**
```
Type:       Desktop application (media renamer)
Features:   - Scan a folder of video files
            - Parse season and episode from messy names
            - Look up episode titles from TheTVDB
            - Rename to Show - S01E01 - Title format
            - Rename matching subtitle files too
Tech stack: Python, PySide6, guessit, TheTVDB API
```

---

## Example 368

**Intent:**
a solitaire game with dominoes

**Spec:**
```
Type:       Desktop game (dominoes solitaire)
Features:   - Deal dominoes into a pyramid layout
            - Remove pairs that add up to 12 pips
            - Only allow uncovered dominoes to be picked
            - Shuffle once when stuck
            - Track wins and best time
Storage:    Local JSON stats
Tech stack: Java, LibGDX
```

---

## Example 369

**Intent:**
an app that keeps a log of my migraines and possible triggers

**Spec:**
```
Type:       Desktop application (health log)
Data model: Episode(id, started_at, ended_at, severity, medication, notes)
            Trigger(id, name)
            EpisodeTrigger(episode_id -> Episode, trigger_id -> Trigger)
Features:   - Log migraine episodes with severity and medication
            - Tick possible triggers like sleep or food
            - Show a calendar of episodes
            - Chart which triggers appear most
            - Export a report for the doctor as PDF
Storage:    SQLite local database
Tech stack: Python, Flet, ReportLab
```

---

## Example 370

**Intent:**
browser game where you build a city on a tiny floating cube

**Spec:**
```
Type:       Browser game (city builder, 3D)
Features:   - Rotate a small cube world with the mouse
            - Place houses, farms and roads on tile faces
            - Grow population when needs are met
            - Balance happiness and resources
            - Save the cube to localStorage
Storage:    Browser localStorage
Tech stack: JavaScript, Three.js
```

---

## Example 371

**Intent:**
lan file share app for my office, no cloud

**Spec:**
```
Type:       Desktop application (LAN file sharing)
Features:   - Discover other computers on the LAN with mDNS
            - Send files by dragging onto a computer's name
            - Accept or decline incoming transfers
            - Show transfer speed and progress
            - Keep a transfer history
Tech stack: Go, Wails, React
```

---

## Example 372

**Intent:**
rhythm game for phone where you tap drums to traditional songs

**Spec:**
```
Type:       Mobile game (rhythm)
Data model: Song(id, title, audio_file, chart_file, difficulty)
            Score(song_id -> Song, best_score, best_combo)
Features:   - Show drum pads that light up in time with the song
            - Judge tap timing against the beat chart
            - Compensate for audio latency with calibration
            - Unlock songs by stars
            - Save best scores
Storage:    Local SQLite
Tech stack: Unity, C#
```

---

## Example 373

**Intent:**
offline app to plan a trip itinerary

**Spec:**
```
Type:       Desktop application (trip planner)
Data model: Trip(id, name, start_date, end_date)
            Activity(id, trip_id -> Trip, day, time, title, location, cost, notes)
Features:   - Create trips with dates
            - Add activities per day with times
            - Drag activities between days
            - Show the total budget
            - Print the itinerary
Storage:    SQLite local database
Tech stack: Electron, Vue 3
```

---

## Example 374

**Intent:**
i want a game that is like a garden where every plant is a habit you keep

**Spec:**
```
Type:       Mobile game (habit garden)
Data model: Habit(id, name, plant_type)
            CheckIn(habit_id -> Habit, date)
Features:   - Plant one plant per habit
            - Grow the plant each day the habit is checked in
            - Wilt plants slowly when habits are skipped
            - Unlock new plant types with streaks
            - Show the garden as a cosy scene
Storage:    Local storage
Tech stack: Flutter, Flame
```

---

## Example 375

**Intent:**
brick builder app to design lego-style models on computer

**Spec:**
```
Type:       Desktop application (3D design)
Data model: Model(id, name)
            Brick(id, model_id -> Model, type, colour, x, y, z, rotation)
Features:   - Place bricks on a 3D grid with snapping
            - Choose brick types and colours
            - Rotate and orbit the camera
            - Count the parts list
            - Export building steps as images
Storage:    Local JSON model files
Tech stack: C#, Unity
```

---

## Example 376

**Intent:**
write a pygame game where you are a bat using echolocation in the dark

**Spec:**
```
Type:       Desktop game (exploration)
Features:   - Keep the cave mostly dark
            - Send echolocation pulses that briefly reveal walls
            - Fly with arrow keys
            - Catch moths to refill energy
            - Detect wall collisions with the cave tilemap
Tech stack: Python, Pygame
```

---

## Example 377

**Intent:**
windows tool to clean temp files and empty recycle bin with one click

**Spec:**
```
Type:       Desktop application (system cleaner)
Features:   - Scan temp folders, browser caches and the recycle bin
            - Show the size that can be freed by category
            - Clean selected categories
            - Skip files in use
            - Schedule weekly cleaning
Tech stack: C#, .NET, WinForms
```

---

## Example 378

**Intent:**
app to make bingo cards for our community centre

**Spec:**
```
Type:       Desktop application (bingo generator)
Features:   - Generate unique 5x5 bingo cards
            - Use numbers or custom word lists
            - Print four cards per page
            - Run a caller screen that draws random numbers
            - Show called numbers on a board
Tech stack: Python, Tkinter, ReportLab
```

---

## Example 379

**Intent:**
noise generator for focus

**Spec:**
```
Type:       Desktop application (ambient sound)
Features:   - Play rain, cafe, fan and brown noise sounds
            - Mix several sounds with separate volume sliders
            - Save mixes as presets
            - Set a timer to fade out
            - Run from the tray
Storage:    Local JSON presets
Tech stack: Electron, Howler.js
```

---

## Example 380

**Intent:**
hex map editor for tabletop games

**Spec:**
```
Type:       Desktop application (map editor)
Data model: Map(id, name, width, height)
            Hex(map_id -> Map, q, r, terrain, label)
Features:   - Paint terrain types on a hex grid
            - Add labels and icons to hexes
            - Zoom and pan large maps
            - Print maps across multiple pages
            - Export PNG
Storage:    Local JSON map files
Tech stack: Python, PySide6
```

---

## Example 381

**Intent:**
game wher u r a slime that absorbs things to grow

**Spec:**
```
Type:       Browser game (arcade)
Features:   - Move the slime with the mouse
            - Absorb objects smaller than the slime to grow
            - Bounce off objects that are too big
            - Grow the camera zoom with size
            - Finish the level by reaching a target size
Tech stack: JavaScript, PixiJS
```

---

## Example 382

**Intent:**
progam for my restaurant tables, which table ordered what and the bill, we have 12 tables, in spanish please

**Spec:**
```
Type:       Desktop application (restaurant orders)
Data model: RestaurantTable(id, number, status)
            Order(id, table_id -> RestaurantTable, opened_at, closed_at, total)
            OrderItem(id, order_id -> Order, dish, quantity, price)
Features:   - Show 12 tables with free or busy colours
            - Add dishes to a table's order
            - Send the order to a kitchen printer
            - Split and print the bill
            - Show the interface in Spanish
Storage:    SQLite local database
Tech stack: C#, .NET 8, WPF (es-ES resources)
```

---

## Example 383

**Intent:**
dice roller for tabletop rpgs

**Spec:**
```
Type:       Desktop application (dice roller)
Features:   - Roll dice with notation like 2d6+3
            - Animate 3D dice rolls
            - Keep a roll history
            - Save favourite rolls as buttons
            - Support advantage and disadvantage
Tech stack: JavaScript, Electron, Three.js, cannon-es
```

---

## Example 384

**Intent:**
tiny game where you defend your sandcastle from waves

**Spec:**
```
Type:       Mobile game (casual defence)
Features:   - Build sand walls by swiping
            - Send waves of increasing size
            - Erode walls that waves hit
            - Rebuild between waves with limited sand
            - Score by waves the castle survives
Tech stack: Godot 4, GDScript
```

---

## Example 385

**Intent:**
i want app for practice english speaking, it listens and says my mistakes, i am from Turkey

**Spec:**
```
Type:       Desktop application (pronunciation practice)
Data model: Sentence(id, text, level)
            Attempt(id, sentence_id -> Sentence, transcript, score, recorded_at)
Features:   - Show a sentence and play a native recording
            - Record the user reading it
            - Transcribe speech and compare word by word
            - Highlight mispronounced words
            - Track scores over time
Storage:    SQLite local database
Tech stack: Python, PySide6, Whisper (local), pyttsx3
```

---

## Example 386

**Intent:**
battleship but with planets

**Spec:**
```
Type:       Browser game (strategy)
Features:   - Hide planets on a space grid
            - Fire probes at coordinates
            - Show hits, misses and nearby gravity hints
            - Play against AI
            - Show turns used
Tech stack: TypeScript, Vue 3
```

---

## Example 387

**Intent:**
screen recorder for mac that records system audio too

**Spec:**
```
Type:       Desktop application (screen recorder)
Features:   - Pick a display, window or region
            - Record system audio and microphone together
            - Show a floating stop button
            - Save to MOV or MP4
            - Trim the recording after stopping
Tech stack: Swift, ScreenCaptureKit, AVFoundation
```

---

## Example 388

**Intent:**
chill fishing game in the terminal lol

**Spec:**
```
Type:       Desktop game (terminal)
Features:   - Draw a lake with ASCII animation
            - Cast with a key and wait for a bite
            - Reel in with a timing prompt
            - Keep a log of fish caught
            - Save the log to a file
Tech stack: Python, Textual
```

---

## Example 389

**Intent:**
puzzle game where you are a train switch operator

**Spec:**
```
Type:       Browser game (puzzle)
Features:   - Show trains of different colours heading toward junctions
            - Click switches to route trains to matching stations
            - Detect crashes when trains meet
            - Speed up trains each level
            - Rate levels by trains delivered
Tech stack: JavaScript, HTML5 Canvas
```

---

## Example 390

**Intent:**
Is it possible to have a desktop program that watches a folder of scanned invoices and pulls out the date, supplier and total into a spreadsheet?

**Spec:**
```
Type:       Desktop application (document extraction)
Features:   - Watch the folder for new scans
            - Run OCR on each document
            - Extract date, supplier name and total with patterns
            - Let the user correct fields in a review table
            - Append rows to an Excel file
Input:      Folder of scanned invoice PDFs and images
Tech stack: Python, PySide6, Tesseract, openpyxl, watchdog
```

---

## Example 391

**Intent:**
avatar maker for my game where people pick hair eyes clothes

**Spec:**
```
Type:       Desktop application (avatar creator)
Features:   - Layer sprite parts for body, hair, eyes and clothes
            - Choose colours for each part with tinting
            - Randomise an avatar
            - Preview animations
            - Export a sprite sheet PNG
Tech stack: Godot 4, GDScript
```

---

## Example 392

**Intent:**
whack a mole but moles are bugs in code

**Spec:**
```
Type:       Browser game (arcade)
Features:   - Show a grid of code lines
            - Pop bugs out of random lines for short times
            - Hit bugs with a click to fix them
            - Penalise clicking on clean lines
            - Speed up over a 60-second round
Tech stack: JavaScript, HTML, CSS
```

---

## Example 393

**Intent:**
lightweight log viewer that tails big log files

**Spec:**
```
Type:       Desktop application (log viewer)
Features:   - Open large log files without loading them fully
            - Follow new lines in real time
            - Colour lines by level like ERROR and WARN
            - Filter with regex
            - Bookmark lines
Tech stack: Rust, egui
```

---

## Example 394

**Intent:**
bird watching log with photos and map

**Spec:**
```
Type:       Desktop application (nature log)
Data model: Sighting(id, species, count, seen_at, latitude, longitude, photo_path, notes)
Features:   - Log sightings with species, count and photo
            - Read GPS from photo EXIF
            - Show sightings on a map
            - Build a life list of species
            - Export to CSV
Storage:    SQLite local database
Tech stack: Python, PySide6, folium
```

---

## Example 395

**Intent:**
simple mobile game: tap to make a ball jump over lines

**Spec:**
```
Type:       Mobile game (hyper-casual)
Features:   - Bounce the ball when the screen is tapped
            - Scroll obstacles with gaps
            - Detect collisions with the obstacles
            - Increase speed every 10 points
            - Save the best score
Tech stack: Flutter, Flame
```

---

## Example 396

**Intent:**
offline bus ticket booking for small transport company office

**Spec:**
```
Type:       Desktop application (ticketing)
Data model: Route(id, origin, destination, price)
            Trip(id, route_id -> Route, departs_at, bus_no, seats)
            Ticket(id, trip_id -> Trip, seat_no, passenger_name, phone, paid)
Features:   - Show a seat map per trip
            - Sell tickets and block taken seats
            - Print tickets with a receipt printer
            - List passengers per trip for the driver
            - Report daily sales
Storage:    SQLite local database
Tech stack: Java, JavaFX
```

---

## Example 397

**Intent:**
color matching game for colorblind friendly

**Spec:**
```
Type:       Browser game (puzzle)
Features:   - Use patterns and symbols in addition to colours
            - Match three tiles in a row
            - Offer colour-blind palettes for different types
            - Cascade tiles after matches
            - Track score and moves
Tech stack: TypeScript, PixiJS
```

---

## Example 398

**Intent:**
home server dashboard but desktop app showing my raspberry pi stats

**Spec:**
```
Type:       Desktop application (monitoring)
Features:   - Connect to a Raspberry Pi over SSH
            - Show CPU, memory, temperature and disk usage
            - Graph stats over the last hour
            - Restart services from a list
            - Alert when temperature is too high
Tech stack: Python, PySide6, paramiko
```

---

## Example 399

**Intent:**
game where you are a lighthouse keeper guiding boats at night with the beam

**Spec:**
```
Type:       Desktop game (arcade)
Features:   - Rotate the lighthouse beam with the mouse
            - Show boats only when lit
            - Steer boats away from rocks by lighting safe paths
            - Increase fog and boat count each night
            - Score saved boats
Tech stack: Godot 4, GDScript
```

---

## Example 400

**Intent:**
a desktop app that lets me write music notation

**Spec:**
```
Type:       Desktop application (music notation)
Data model: Score(id, title, time_signature, key, staves_json)
Features:   - Enter notes with mouse and keyboard on a staff
            - Support rests, ties and dynamics
            - Play back the score
            - Transpose the score
            - Export to PDF and MusicXML
Storage:    Local MusicXML files
Tech stack: C++, Qt 6, FluidSynth
```

---

## Example 401

**Intent:**
i want game kids learn to count money coins in euros

**Spec:**
```
Type:       Mobile game (educational)
Features:   - Show a price tag and a tray of euro coins
            - Drag coins into a payment area
            - Check if the amount is exact
            - Add change-giving levels
            - Reward with shop stickers
Tech stack: Flutter
```

---

## Example 402

**Intent:**
tamagotchi but it's a plant and you need to water it in real life time

**Spec:**
```
Type:       Mobile game (virtual pet)
Data model: PlantState(name, water_level, sunlight, growth_stage, last_updated_at)
Features:   - Drop water level based on real elapsed time
            - Remind with push notifications when thirsty
            - Grow the plant through stages with care
            - Wilt the plant if neglected for days
            - Unlock new pots
Storage:    Local storage
Tech stack: React Native, Expo Notifications
```

---

## Example 403

**Intent:**
a desktop mind map app

**Spec:**
```
Type:       Desktop application (mind mapping)
Data model: MindMap(id, title)
            MapNode(id, map_id -> MindMap, parent_id -> MapNode, text, colour)
Features:   - Add child and sibling nodes with keyboard shortcuts
            - Lay out branches automatically
            - Collapse and expand branches
            - Drag nodes to re-parent them
            - Export as image or Markdown outline
Storage:    Local JSON files
Tech stack: Electron, D3.js
```

---

## Example 404

**Intent:**
an online quiz battle game for phones, 1v1 random opponent

**Spec:**
```
Type:       Mobile game (multiplayer quiz)
Auth:       Anonymous sign-in with optional Google login
Data model: Player(id, name, rating)
            Match(id, player1_id -> Player, player2_id -> Player, questions, scores, finished_at)
Features:   - Find a random opponent with similar rating
            - Play 7 timed questions in sync
            - Score faster answers higher
            - Update ratings after each match
            - Show match history
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase, Node.js
```

---

## Example 405

**Intent:**
auto clicker

**Spec:**
```
Type:       Desktop application (automation)
Features:   - Click at a set interval in milliseconds
            - Choose left, right or double click
            - Click at the cursor or a fixed position
            - Start and stop with a hotkey
            - Stop after a set number of clicks
Tech stack: Python, pynput, Tkinter
```

---

## Example 406

**Intent:**
im a DJ and want a tool to sort my tracks by key and bpm

**Spec:**
```
Type:       Desktop application (music library)
Data model: Track(id, path, title, artist, bpm, musical_key, energy)
Features:   - Analyse BPM and key for each track
            - Show keys in Camelot notation
            - Suggest harmonically compatible next tracks
            - Write BPM and key into file tags
            - Sort and filter the library
Storage:    SQLite local database
Tech stack: Python, librosa, essentia, PySide6
```

---

## Example 407

**Intent:**
browser game where you make a sandwich tower as tall as possible

**Spec:**
```
Type:       Browser game (stacking)
Features:   - Swing ingredients above the sandwich
            - Drop with a click
            - Trim overhanging parts like a stacking game
            - Add slippery ingredients
            - Score by height
Tech stack: JavaScript, Three.js
```

---

## Example 408

**Intent:**
gamepad tester

**Spec:**
```
Type:       Desktop application (utility)
Features:   - List connected gamepads
            - Show button presses and stick positions live
            - Visualise stick drift with a dead-zone circle
            - Test vibration motors
            - Show input latency
Tech stack: C, SDL2
```

---

## Example 409

**Intent:**
a family recipe book to print as a nice book for christmas

**Spec:**
```
Type:       Desktop application (book layout)
Data model: Recipe(id, title, author_relative, story, ingredients, steps, photo_path, chapter)
Features:   - Collect recipes with photos and family stories
            - Organise recipes into chapters
            - Lay out pages with a chosen template
            - Generate a table of contents
            - Export a print-ready PDF
Storage:    SQLite local database
Tech stack: Python, PySide6, WeasyPrint
```

---

## Example 410

**Intent:**
tile matching game with chinese style tiles but my own rules

**Spec:**
```
Type:       Desktop game (tile matching)
Features:   - Arrange tiles in stacked layers
            - Allow selecting only free tiles
            - Remove matching pairs
            - Shuffle remaining tiles when stuck
            - Include hint and undo
Storage:    Local JSON stats
Tech stack: C#, Godot 4 (.NET)
```

---

## Example 411

**Intent:**
desktop app for my photography clients to choose photos? no, just for me to send galleries, offline then export

**Spec:**
```
Type:       Desktop application (gallery export)
Features:   - Pick photos for a client gallery
            - Resize and watermark them
            - Generate a static HTML gallery with lightbox
            - Zip the gallery for sending
            - Remember galleries per client
Storage:    Local JSON
Tech stack: Python, Jinja2, Pillow, PySide6
```

---

## Example 412

**Intent:**
game where cats run a cafe and you serve other cats

**Spec:**
```
Type:       Mobile game (cafe management)
Features:   - Take orders from cat customers
            - Prepare drinks in timed mini-games
            - Earn tips for speed
            - Decorate the cafe
            - Unlock new cat staff
Storage:    Local save file
Tech stack: Unity, C#
```

---

## Example 413

**Intent:**
hangout timer app that splits screen time for board game turns

**Spec:**
```
Type:       Desktop application (turn timer)
Features:   - Add players with names and colours
            - Count each player's turn time
            - Pass the turn with a tap or space
            - Warn when a turn is too long
            - Show total time per player
Tech stack: JavaScript, Electron
```

---

## Example 414

**Intent:**
a strategy game about running a medieval village through winters

**Spec:**
```
Type:       Desktop game (colony management)
Features:   - Assign villagers to farm, chop wood and hunt
            - Store food and firewood for winter
            - Simulate seasons with crop growth
            - Handle random events like raids and sickness
            - Save and load villages
Tech stack: Unity, C#
```

---

## Example 415

**Intent:**
offline e-book maker, write and export epub

**Spec:**
```
Type:       Desktop application (ebook authoring)
Data model: Book(id, title, author, cover_path)
            Chapter(id, book_id -> Book, title, body_markdown, position)
Features:   - Write chapters in Markdown
            - Reorder chapters
            - Add a cover image and metadata
            - Preview the book
            - Export EPUB and PDF
Storage:    SQLite local database
Tech stack: Electron, React, Pandoc
```

---

## Example 416

**Intent:**
pls game for learning human body organs drag to right place

**Spec:**
```
Type:       Browser game (educational)
Features:   - Show a body outline
            - Drag organs to their correct place
            - Snap organs into place when close
            - Show organ facts on success
            - Time each attempt
Tech stack: HTML, CSS, JavaScript
```

---

## Example 417

**Intent:**
tool to find out what is using my disk space in my mac, but pretty

**Spec:**
```
Type:       Desktop application (disk usage)
Features:   - Scan disks and folders quickly in the background
            - Show a sunburst chart of folder sizes
            - Click to drill into folders
            - Reveal files in Finder
            - Move items to trash
Tech stack: Swift, SwiftUI, Swift Charts
```

---

## Example 418

**Intent:**
escape the lab platformer with portals

**Spec:**
```
Type:       Browser game (puzzle platformer)
Features:   - Place two linked portals with the mouse
            - Keep momentum through portals
            - Move with keyboard and jump
            - Solve test chambers with boxes and buttons
            - Save cleared chambers
Tech stack: TypeScript, Phaser 3
```

---

## Example 419

**Intent:**
weather station display on old laptop from my arduino sensors

**Spec:**
```
Type:       Desktop application (sensor display)
Features:   - Read sensor values from a serial port
            - Show big current readings
            - Graph the last 24 hours
            - Log readings to a file
            - Alert on frost temperature
Input:      Serial data from an Arduino with temperature, humidity and pressure sensors
Storage:    SQLite local database
Tech stack: Python, pyserial, PySide6, pyqtgraph
```

---

## Example 420

**Intent:**
a desktop app to plan knitting patterns on a grid

**Spec:**
```
Type:       Desktop application (craft design)
Data model: Chart(id, name, rows, columns, cells_json, palette)
Features:   - Paint stitches and colours on a stitch grid
            - Mirror and repeat motifs
            - Count stitches per colour
            - Show the current row while knitting
            - Print the chart with row numbers
Storage:    Local JSON chart files
Tech stack: Python, PySide6
```

---

## Example 421

**Intent:**
game where you guide glowing jellyfish home through a dark ocean

**Spec:**
```
Type:       Mobile game (casual)
Features:   - Draw a light path with a finger for jellyfish to follow
            - Avoid anglerfish that chase light
            - Collect plankton for points
            - Light up the reef as levels are cleared
            - Save progress per reef
Tech stack: Unity, C#
```

---
