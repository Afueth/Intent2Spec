## Example 1

**Intent:**
gradebook app for my laptop

**Spec:**
```
Type:       Desktop application (teacher gradebook)
Data model: Class(id, name, term)
            Student(id, class_id -> Class, first_name, last_name)
            Assignment(id, class_id -> Class, title, category, max_points, weight)
            Grade(id, student_id -> Student, assignment_id -> Assignment, points)
Features:   - Create classes and import student rosters from CSV
            - Add assignments with weighted categories (homework, tests, labs)
            - Enter grades in a spreadsheet-style grid
            - Calculate running averages and letter grades per student
            - Export report cards to PDF
Storage:    SQLite database file
Tech stack: Python, PySide6, ReportLab (PDF export)
```

---

## Example 2

**Intent:**
I teach year 5 and I move kids around every few weeks. I want a program where I drag students onto desks and it remembers who shouldn't sit next to each other.

**Spec:**
```
Type:       Desktop application (classroom seating chart)
Data model: Student(id, name, needs_front_row)
            Desk(id, x, y, rotation)
            Conflict(id, student_a_id -> Student, student_b_id -> Student)
            SeatingPlan(id, name, created_at)
            Assignment(plan_id -> SeatingPlan, desk_id -> Desk, student_id -> Student)
Features:   - Draw the room layout by placing and rotating desks
            - Drag students onto desks to build a plan
            - Warn when two students with a recorded conflict sit next to each other
            - Auto-generate a random plan that respects conflicts and front-row needs
            - Save several plans and print the chart
Storage:    SQLite database file
Tech stack: C#, WPF, .NET 8
```

---

## Example 3

**Intent:**
setlist maker for my band, offline, on a mac

**Spec:**
```
Type:       Desktop application (band setlist manager)
Data model: Song(id, title, key, bpm, duration_sec, notes)
            Setlist(id, gig_name, venue, gig_date)
            SetlistItem(id, setlist_id -> Setlist, song_id -> Song, position, is_break)
Features:   - Keep a song library with key, tempo and length
            - Drag songs into an ordered setlist with breaks between sets
            - Show total running time for each set
            - Flag back-to-back songs in the same key
            - Print a large-font setlist for the stage floor
Storage:    Local SQLite database
Tech stack: Swift, SwiftUI, SwiftData (macOS)
```

---

## Example 4

**Intent:**
i play guitar and want a chord chart thing where i type lyrics with chords above and can transpose it

**Spec:**
```
Type:       Desktop application (chord chart editor)
Data model: Chart(id, title, artist, original_key, capo)
            Line(id, chart_id -> Chart, position, lyrics, chords_json)
Features:   - Type lyrics and place chord symbols above specific syllables
            - Parse ChordPro format files on import
            - Transpose the whole chart up or down by semitones
            - Show chord diagrams for guitar on hover
            - Export the chart to PDF with chords aligned above lyrics
Storage:    ChordPro (.cho) text files on disk
Tech stack: Python, Tkinter, ReportLab
```

---

## Example 5

**Intent:**
A writing app for my novel where each chapter and scene is a separate card I can rearrange, with word count goals.

**Spec:**
```
Type:       Desktop application (manuscript organiser)
Data model: Project(id, title, word_goal, deadline)
            Chapter(id, project_id -> Project, title, position)
            Scene(id, chapter_id -> Chapter, title, synopsis, body, status, position)
            Session(id, project_id -> Project, date, words_written)
Features:   - Organise the manuscript into chapters and scene cards
            - Rearrange scenes by drag and drop on a corkboard view
            - Track word count per scene, chapter and whole project
            - Log daily writing sessions against the word goal
            - Compile the manuscript into DOCX or EPUB
Storage:    Project folder with Markdown scenes and a JSON index
Tech stack: Electron, TypeScript, React, Pandoc (compile)
```

---

## Example 6

**Intent:**
My grandma has hundreds of old family names written down and I want a program to build our family tree with photos and dates, without putting it online.

**Spec:**
```
Type:       Desktop application (genealogy)
Data model: Person(id, given_names, surname, sex, birth_date, birth_place, death_date)
            Family(id, partner_a_id -> Person, partner_b_id -> Person, marriage_date)
            Child(family_id -> Family, person_id -> Person)
            Media(id, person_id -> Person, file_path, caption)
Features:   - Add people with life events and places
            - Link partners and children into families
            - Draw an interactive ancestor and descendant tree
            - Attach scanned photos and documents to people
            - Import and export GEDCOM files
Storage:    Local SQLite database, media copied into a project folder
Tech stack: Java, JavaFX, SQLite JDBC
```

---

## Example 7

**Intent:**
simple bookkeeping for a few small clients, I'm a freelance accountant

**Spec:**
```
Type:       Desktop application (small-practice bookkeeping)
Data model: Client(id, name, vat_number, fiscal_year_start)
            Account(id, client_id -> Client, code, name, type)
            JournalEntry(id, client_id -> Client, date, description)
            JournalLine(id, entry_id -> JournalEntry, account_id -> Account, debit, credit)
Features:   - Keep a separate chart of accounts per client
            - Record double-entry journal entries and reject unbalanced ones
            - Import bank statements from CSV and match them to entries
            - Produce trial balance, profit and loss and balance sheet
            - Export reports to Excel
Storage:    One SQLite file per client
Tech stack: Python, PyQt6, openpyxl
```

---

## Example 8

**Intent:**
I translate medical documents from German to English and need a glossary tool where I can look up my own terms fast while I work.

**Spec:**
```
Type:       Desktop application (translation glossary)
Data model: Glossary(id, name, source_lang, target_lang, domain)
            Term(id, glossary_id -> Glossary, source_term, target_term, part_of_speech, note, source_ref)
Features:   - Search terms instantly as you type with fuzzy matching
            - Add terms from a global hotkey with clipboard text pre-filled
            - Mark terms as approved, forbidden or client-specific
            - Import and export TBX and CSV glossaries
            - Keep the search window always on top
Storage:    SQLite with FTS5 full-text index
Tech stack: Python, PySide6, rapidfuzz
```

---

## Example 9

**Intent:**
lab sample tracker for our small biology lab, which freezer and which box each tube is in

**Spec:**
```
Type:       Desktop application (lab sample inventory)
Data model: Freezer(id, name, temperature_c, room)
            Rack(id, freezer_id -> Freezer, label)
            Box(id, rack_id -> Rack, label, rows, cols)
            Sample(id, box_id -> Box, row, col, label, type, owner, frozen_on, volume_ul)
Features:   - Show each box as a grid of positions with filled and empty slots
            - Register samples into a chosen position
            - Search samples by label, owner or type
            - Print barcode labels for tubes
            - Log every move and removal with the user name
Storage:    SQLite database on a shared network drive
Tech stack: C#, WinForms, .NET 8, ZXing.Net (barcodes)
```

---

## Example 10

**Intent:**
Lighting cue software for our school theatre, we have a USB DMX dongle and about 20 lights.

**Spec:**
```
Type:       Desktop application (stage lighting control)
Data model: Fixture(id, name, start_address, channel_count, type)
            Cue(id, number, label, fade_in_sec, fade_out_sec)
            CueLevel(cue_id -> Cue, fixture_id -> Fixture, channel, value)
Features:   - Patch fixtures to DMX addresses
            - Set channel levels with on-screen faders
            - Record cues and play them back with timed crossfades
            - Advance cues with the spacebar during the show
            - Send DMX frames to a USB DMX interface at 40 Hz
Storage:    JSON show file
Tech stack: Python, PySide6, pyserial (Enttec Open DMX)
```

---

## Example 11

**Intent:**
GM screen app for running my tabletop RPG sessions

**Spec:**
```
Type:       Desktop application (tabletop RPG game-master tool)
Data model: Campaign(id, name, system)
            Character(id, campaign_id -> Campaign, name, is_player, hp_max, armor_class, initiative_bonus)
            Encounter(id, campaign_id -> Campaign, name)
            Combatant(id, encounter_id -> Encounter, character_id -> Character, hp_current, initiative)
            Note(id, campaign_id -> Campaign, title, body)
Features:   - Roll initiative and sort combatants into turn order
            - Track hit points and conditions during combat
            - Roll dice from text expressions like 2d6+3
            - Keep searchable session notes per campaign
Storage:    SQLite database
Tech stack: Rust, Tauri, Svelte
```

---

## Example 12

**Intent:**
subtitle editor where i can see the video and fix the timings of srt files

**Spec:**
```
Type:       Desktop application (subtitle editor)
Data model: SubtitleTrack(file_path, format, frame_rate)
            Cue(index, start_ms, end_ms, text)
Features:   - Play the video with the current subtitle overlaid
            - Edit cue text and start/end times in a table
            - Show the audio waveform and drag cue edges on it
            - Shift all cues by an offset or stretch between two sync points
            - Warn on overlapping cues and lines over 42 characters
            - Save as SRT or WebVTT
Storage:    Subtitle files on disk
Tech stack: C++, Qt 6, libmpv
```

---

## Example 13

**Intent:**
I have way too many fonts installed. I want something to browse them, preview a sentence in each one, and turn sets on and off.

**Spec:**
```
Type:       Desktop application (font manager)
Data model: Font(id, family, style, file_path, format, is_active)
            FontSet(id, name)
            FontSetMember(set_id -> FontSet, font_id -> Font)
Features:   - Scan font folders and read family and style from font files
            - Preview custom text in every font at a chosen size
            - Group fonts into sets such as "Client X" or "Headings"
            - Activate and deactivate sets without deleting files
            - Detect duplicate fonts
Storage:    SQLite catalogue
Tech stack: Python, PySide6, fontTools
```

---

## Example 14

**Intent:**
clipboard history

**Spec:**
```
Type:       Desktop application (clipboard history)
Data model: ClipItem(id, content_type, text, image_path, copied_at, is_pinned)
Features:   - Record every text and image copied to the clipboard
            - Open a searchable history popup with a global hotkey
            - Paste a chosen item back into the active window
            - Pin frequently used items so they are never deleted
            - Ignore copies from password managers
Storage:    SQLite database, images saved to an app data folder
Tech stack: C#, WPF, .NET 8
```

---

## Example 15

**Intent:**
Window tiling for Windows, I want to snap windows into a grid with keyboard shortcuts, my own layouts.

**Spec:**
```
Type:       Desktop application (window tiling manager)
Data model: Layout(id, name, monitor_id, zones_json)
            Hotkey(id, keys, action, layout_id -> Layout, zone_index)
Features:   - Define custom zone layouts per monitor
            - Move the active window into a zone with a hotkey
            - Cycle a window through zones with repeated presses
            - Remember window positions per app and restore them on launch
            - Run from the system tray on startup
Storage:    JSON settings file in AppData
Tech stack: C++, Win32 API
```

---

## Example 16

**Intent:**
typing tutor for my kids

**Spec:**
```
Type:       Desktop application (typing tutor)
Data model: Profile(id, name, age)
            Lesson(id, title, target_keys, text)
            Attempt(id, profile_id -> Profile, lesson_id -> Lesson, wpm, accuracy, completed_at)
Features:   - Show an on-screen keyboard highlighting the next key and finger
            - Progress through lessons starting with the home row
            - Measure words per minute and accuracy
            - Unlock the next lesson at 90% accuracy
            - Show a progress chart for each child
Storage:    SQLite database
Tech stack: Python, Pygame
```

---

## Example 17

**Intent:**
We need a kiosk program for our museum's touch screen where visitors tap through exhibits and it resets when nobody uses it.

**Spec:**
```
Type:       Desktop application (touchscreen kiosk)
Data model: Exhibit(id, title, body, image_path, video_path, position)
            Language(code, name)
            Translation(exhibit_id -> Exhibit, language_code -> Language, title, body)
            Interaction(id, exhibit_id -> Exhibit, viewed_at)
Features:   - Run full screen and block exit gestures and keyboard shortcuts
            - Browse exhibits with large touch-friendly buttons
            - Switch the interface language
            - Return to the attract screen after 60 seconds of inactivity
            - Log which exhibits are viewed most
Storage:    SQLite database and a local media folder
Tech stack: Electron, TypeScript, Vue
```

---

## Example 18

**Intent:**
a rhythm game where you defend a lighthouse by tapping to the beat of sea shanties

**Spec:**
```
Type:       Desktop game (2D rhythm)
Data model: Song(id, title, audio_file, bpm, offset_ms)
            Chart(id, song_id -> Song, difficulty, notes_json)
            Score(id, chart_id -> Chart, points, accuracy, max_combo)
Features:   - Spawn waves of ghost ships synced to the beat chart
            - Fire the lighthouse beam on four lanes using keys
            - Grade hits as perfect, good or miss by timing window
            - Build combos that brighten the beam
            - Save best scores per song and difficulty
Storage:    Local JSON save file
Tech stack: Godot 4, GDScript
```

---

## Example 19

**Intent:**
typing game zombies, type the word on the zombie to kill it

**Spec:**
```
Type:       Desktop game (typing action)
Data model: WordList(id, name, difficulty, words)
            Run(id, wave_reached, words_typed, wpm, accuracy)
Features:   - Spawn zombies carrying words that walk toward the player
            - Lock onto a zombie when its first letter is typed
            - Destroy the zombie when its word is completed
            - Increase word length and zombie speed each wave
            - Show WPM and accuracy at the end of a run
Storage:    Local save file with best runs
Tech stack: C#, MonoGame
```

---

## Example 20

**Intent:**
I'd love a word game where you build words from letter tiles that fall like rain and longer words clear more rows.

**Spec:**
```
Type:       Desktop game (word puzzle)
Features:   - Drop weighted random letter tiles into a 7x10 grid
            - Select adjacent tiles to form a word
            - Check words against a bundled dictionary
            - Clear used tiles and drop tiles above into the gaps
            - Score by word length with bonus tiles for rare letters
            - End the game when a column overflows
Storage:    Local high-score file
Tech stack: Python, Pygame
```

---

## Example 21

**Intent:**
physics sandbox where you build contraptions with wheels, ropes and springs and watch them go

**Spec:**
```
Type:       Desktop game (2D physics sandbox)
Data model: Contraption(id, name, parts_json, created_at)
Features:   - Place beams, wheels, ropes, springs and motors on a canvas
            - Join parts with hinges and welds
            - Start and pause the physics simulation
            - Rewind the simulation to the build state
            - Save and load contraptions to files
Storage:    JSON files in a user folder
Tech stack: C++, SFML, Box2D
```

---

## Example 22

**Intent:**
Tower defence but the towers are kitchen appliances and the enemies are ants coming for a picnic.

**Spec:**
```
Type:       Desktop game (2D tower defence)
Data model: Level(id, name, path_json, starting_crumbs)
            TowerType(id, name, cost, range, damage, fire_rate)
            Wave(id, level_id -> Level, number, enemies_json)
Features:   - Place appliance towers (toaster, blender, fan) on free tiles
            - Send ant waves along a fixed path toward the picnic
            - Earn crumbs for each ant and spend them on upgrades
            - Lose picnic health when ants reach the blanket
            - Unlock levels in order and save progress
Storage:    Local JSON save file
Tech stack: Unity, C#
```

---

## Example 23

**Intent:**
roguelike in the terminal, dungeon made of library shelves, you fight living books

**Spec:**
```
Type:       Desktop game (terminal roguelike)
Features:   - Generate library floors with rooms and shelf corridors procedurally
            - Move turn by turn on a grid with field-of-view shadowcasting
            - Fight book monsters in bump-to-attack combat
            - Pick up scrolls with random magic effects
            - Delete the save on death (permadeath)
            - Go deeper by finding the stairway on each floor
Storage:    Single save file, removed on death
Tech stack: Python, tcod
```

---

## Example 24

**Intent:**
a city builder about growing a village on a floating island where you balance weight so it doesnt tip

**Spec:**
```
Type:       Desktop game (city builder)
Data model: Building(id, type, x, y, weight, population, upkeep)
            Island(id, size, tilt_angle, balance_x, balance_y)
Features:   - Place houses, farms and windmills on a grid island
            - Compute the island's centre of mass after each build
            - Tilt the island when weight is uneven and slide loose buildings off
            - Grow population when food and housing are balanced
            - Save and load the island
Storage:    Local save files
Tech stack: Godot 4, C#
```

---

## Example 25

**Intent:**
Farming sim set on Mars where you grow crops in domes and manage oxygen and water.

**Spec:**
```
Type:       Desktop game (farming simulation)
Data model: Dome(id, x, y, oxygen, water, temperature)
            Plot(id, dome_id -> Dome, crop_type, growth_stage, planted_sol)
            Inventory(item, quantity)
Features:   - Plant, water and harvest crops in pressurised domes
            - Advance time in sols with a day and night cycle
            - Balance oxygen, water and heat for each dome
            - Sell harvests to buy dome upgrades
            - Trigger dust storms that cut solar power
Storage:    Local save file
Tech stack: Unity, C#
```

---

## Example 26

**Intent:**
top down racing game with lawnmowers, 2 players on one keyboard

**Spec:**
```
Type:       Desktop game (top-down racing, local multiplayer)
Data model: Track(id, name, layout_file, laps)
            LapTime(id, track_id -> Track, player_name, time_ms)
Features:   - Drive lawnmowers with drift physics from a top-down view
            - Control player 1 with WASD and player 2 with arrow keys
            - Cut grass for a small speed boost
            - Count laps through checkpoints in order
            - Save best lap times per track
Storage:    Local JSON file
Tech stack: Lua, LÖVE
```

---

## Example 27

**Intent:**
football manager style game but for a small village cricket club, picking the team and managing the budget

**Spec:**
```
Type:       Desktop game (sports management)
Data model: Club(id, name, budget, reputation)
            Player(id, club_id -> Club, name, age, batting, bowling, fielding, morale)
            Fixture(id, home_club_id -> Club, away_club_id -> Club, date, result)
            Season(id, year, league_table_json)
Features:   - Pick the eleven and batting order before each match
            - Simulate matches ball by ball from player skills
            - Manage a budget for kit, pitch upkeep and the tea hut
            - Recruit local players and develop skills between matches
            - Show the league table across a season
Storage:    SQLite save database
Tech stack: Python, PySide6
```

---

## Example 28

**Intent:**
trivia party game for game night, everyone answers on their phones and the questions show on the TV

**Spec:**
```
Type:       Browser game (party trivia)
Data model: Room(code, host_id, status, current_question)
            Player(id, room_code -> Room, nickname, score)
            Question(id, category, text, options, correct_index)
            Answer(player_id -> Player, question_id -> Question, choice, answered_ms)
Features:   - Create a room with a 4-letter code shown on the TV screen
            - Let players join from their phone browsers with a nickname
            - Show a question on the TV with a countdown timer
            - Award more points for faster correct answers
            - Display a leaderboard after each round
API:        WebSocket
            WS /rooms/{code}
Storage:    In-memory room state, question bank in SQLite
Tech stack: Node.js, Socket.IO, React
```

---

## Example 29

**Intent:**
maths game for 7 year olds where they feed a monster the right number

**Spec:**
```
Type:       Desktop game (educational maths)
Data model: Child(id, name)
            Progress(child_id -> Child, skill, level, stars)
Features:   - Show a sum and let the child drag the correct number cookie to the monster
            - Play a happy or sad animation on the answer
            - Adapt difficulty by tracking correct answers per skill
            - Cover addition, subtraction and number bonds to 20
            - Award stars and unlock monster costumes
Storage:    Local JSON save per child
Tech stack: Godot 4, GDScript
```

---

## Example 30

**Intent:**
I'm a science teacher and want a little game where students mix virtual chemicals and see what reacts safely.

**Spec:**
```
Type:       Desktop game (educational chemistry)
Data model: Substance(id, name, formula, state, color)
            Reaction(id, reactant_a_id -> Substance, reactant_b_id -> Substance, product, effect, explanation)
            Challenge(id, title, goal_product, hint)
Features:   - Drag substances into a beaker on a lab bench
            - Look up the reaction and play its visual effect
            - Explain each reaction in student-friendly text
            - Give challenges such as "make a gas that pops"
            - Show a safety warning for dangerous mixes
Storage:    Bundled JSON reaction data
Tech stack: Unity, C#
```

---

## Example 31

**Intent:**
couch co-op game where two players are a shopkeeper and a delivery person and have to work together

**Spec:**
```
Type:       Desktop game (local co-op)
Data model: Order(id, items, deadline_sec, address, status)
            Level(id, map_file, order_count, time_limit_sec)
Features:   - Split controls between two gamepads on one screen
            - Let the shopkeeper pack orders from shelves
            - Let the courier ride a bike through the town to deliver
            - Rate each level with stars from on-time deliveries
            - Shuffle shop layouts between levels
Storage:    Local save of unlocked levels and stars
Tech stack: Godot 4, GDScript
```

---

## Example 32

**Intent:**
Turn based tactics with a small squad of firefighters, putting out spreading fire on a grid.

**Spec:**
```
Type:       Desktop game (turn-based tactics)
Data model: Unit(id, role, x, y, action_points, water, health)
            Tile(x, y, material, fire_level, smoke)
            Mission(id, map_file, civilians, turn_limit)
Features:   - Move firefighters on a grid using action points
            - Spread fire each turn based on tile material and wind
            - Spray water, break doors and carry civilians to exits
            - Score missions by civilians saved and building damage
            - Show the predicted fire spread before ending a turn
Storage:    Local save files
Tech stack: C#, MonoGame
```

---

## Example 33

**Intent:**
interactive fiction game about a night shift at a lost-property office

**Spec:**
```
Type:       Desktop game (interactive fiction)
Data model: Passage(id, text, choices_json, conditions)
            GameState(current_passage_id -> Passage, flags_json, inventory)
Features:   - Show story passages with numbered choices
            - Track flags and inventory to unlock hidden branches
            - Let players examine lost items for clues
            - Save and load at any passage
            - Reach one of several endings based on choices
Storage:    Story authored in Ink, saves as JSON
Tech stack: Ink, inkjs, Electron
```

---

## Example 34

**Intent:**
puzzle platformer where you can only jump when the music is playing and the level changes on silence

**Spec:**
```
Type:       Desktop game (2D puzzle-platformer)
Data model: Level(id, tilemap_file, music_track, silence_pattern)
            Checkpoint(level_id -> Level, x, y)
Features:   - Run and jump with tight platform physics
            - Disable jumping during silent bars of the music
            - Swap solid and ghost platforms when the music stops
            - Respawn at the last checkpoint on death
            - Track completion time per level
Storage:    Local save file
Tech stack: Godot 4, GDScript
```

---

## Example 35

**Intent:**
Hello, I am music teacher from Spain. I need program for my students to practice read notes on staff, it show note and they click the name.

**Spec:**
```
Type:       Desktop application (music note-reading trainer)
Data model: Student(id, name)
            Exercise(id, clef, note_range, note_count)
            Result(id, student_id -> Student, exercise_id -> Exercise, correct, wrong, avg_time_ms)
Features:   - Draw a random note on a treble or bass clef staff
            - Let the student click the note name (Do, Re, Mi or C, D, E)
            - Play the note sound on each answer
            - Track accuracy and speed per student
            - Switch the interface between Spanish and English
Storage:    SQLite database
Tech stack: Python, PySide6, music21
```

---

## Example 36

**Intent:**
metronome app for desktop with accent beats and tempo trainer that speeds up slowly

**Spec:**
```
Type:       Desktop application (metronome)
Data model: Preset(id, name, bpm, beats_per_bar, subdivision, accent_pattern)
Features:   - Play clicks at a set BPM with low-latency audio
            - Accent chosen beats in the bar
            - Increase tempo by N BPM every N bars in trainer mode
            - Flash a visual beat indicator
            - Save presets for different songs
Storage:    JSON presets file
Tech stack: C++, JUCE
```

---

## Example 37

**Intent:**
we run a small dance school and need a program for the recital: which kids are in which dance, costume sizes and quick change problems

**Spec:**
```
Type:       Desktop application (dance recital planner)
Data model: Dancer(id, name, age, costume_size)
            Routine(id, title, class_name, music_file, duration_sec, position)
            Cast(routine_id -> Routine, dancer_id -> Dancer, costume)
Features:   - Order routines in the show running order
            - Assign dancers and costumes to each routine
            - Flag dancers who appear in two routines less than two numbers apart
            - Produce a costume size list for ordering
            - Print a backstage running sheet
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 38

**Intent:**
exam timetable clash checker for school

**Spec:**
```
Type:       Desktop application (exam timetabling)
Data model: Student(id, name, candidate_number)
            Exam(id, subject, paper, duration_min)
            Entry(student_id -> Student, exam_id -> Exam)
            Session(id, date, period, room)
            Scheduled(exam_id -> Exam, session_id -> Session)
Features:   - Import student exam entries from CSV
            - Place exams into sessions on a timetable grid
            - Detect students with two exams in the same session
            - Suggest clash-free slots for a chosen exam
            - Print individual student timetables
Storage:    SQLite database
Tech stack: Java, JavaFX
```

---

## Example 39

**Intent:**
Can you make a quiz maker for teachers that works without internet, makes multiple choice tests and prints them shuffled so kids can't copy?

**Spec:**
```
Type:       Desktop application (test generator)
Data model: QuestionBank(id, subject, topic)
            Question(id, bank_id -> QuestionBank, text, options, correct_index, difficulty)
            Test(id, title, question_ids, version_count)
Features:   - Write and tag multiple-choice questions by topic and difficulty
            - Build a test by picking or randomly sampling questions
            - Generate several versions with shuffled question and option order
            - Export each version and its answer key to PDF
Storage:    SQLite database
Tech stack: Python, PySide6, ReportLab
```

---

## Example 40

**Intent:**
rubric marking tool where i click the level for each criteria and it writes the feedback comment for me

**Spec:**
```
Type:       Desktop application (rubric marking)
Data model: Rubric(id, title)
            Criterion(id, rubric_id -> Rubric, name, weight)
            Level(id, criterion_id -> Criterion, label, points, comment_template)
            Mark(id, student_name, rubric_id -> Rubric, selections_json, total, feedback)
Features:   - Build rubrics with criteria and achievement levels
            - Click one level per criterion to mark a piece of work
            - Assemble a feedback paragraph from the chosen level comments
            - Calculate weighted totals
            - Export all marks to CSV
Storage:    SQLite database
Tech stack: Electron, JavaScript, better-sqlite3
```

---

## Example 41

**Intent:**
practice log for piano students, they record what they practised and for how long

**Spec:**
```
Type:       Desktop application (instrument practice log)
Data model: Piece(id, title, composer, status)
            PracticeSession(id, started_at, duration_min, notes)
            SessionItem(session_id -> PracticeSession, piece_id -> Piece, focus, minutes)
Features:   - Start and stop a practice timer
            - Log which pieces and focus areas were worked on
            - Show weekly practice totals as a bar chart
            - Track each piece from learning to performance-ready
            - Export a weekly report for the teacher
Storage:    SQLite database
Tech stack: Kotlin, Compose Multiplatform (Desktop)
```

---

## Example 42

**Intent:**
manuscript submission tracker, i send short stories to magazines and lose track of who has what

**Spec:**
```
Type:       Desktop application (submission tracker)
Data model: Story(id, title, word_count, genre)
            Market(id, name, pay_rate, response_days, allows_simultaneous)
            Submission(id, story_id -> Story, market_id -> Market, sent_on, status, response_on)
Features:   - Log each submission with date and market
            - Show stories currently out and how long they have waited
            - Warn before sending a story to a market that rejected it
            - Block simultaneous submissions to markets that forbid them
            - Show acceptance rate per market
Storage:    SQLite database
Tech stack: Python, Textual
```

---

## Example 43

**Intent:**
worldbuilding wiki for my fantasy setting, characters places and timeline all linked, stays on my PC

**Spec:**
```
Type:       Desktop application (worldbuilding wiki)
Data model: Article(id, title, category, body_markdown, updated_at)
            Link(from_id -> Article, to_id -> Article)
            Event(id, title, year, era, article_id -> Article)
Features:   - Write articles in Markdown with [[wiki links]]
            - Show backlinks for every article
            - Browse articles by category (characters, places, factions)
            - Display events on a scrollable custom-era timeline
            - Search all articles with full-text search
Storage:    Markdown files in a folder, SQLite index
Tech stack: Tauri, Rust, TypeScript, React
```

---

## Example 44

**Intent:**
screenplay formatter

**Spec:**
```
Type:       Desktop application (screenwriting editor)
Data model: Script(id, title, author, draft_number)
            Element(id, script_id -> Script, position, type, text)
Features:   - Format scene headings, action, character, dialogue and transitions
            - Cycle element types with Tab and Enter
            - Autocomplete character names and locations
            - Paginate in industry-standard layout with page numbers
            - Import and export Fountain files and export PDF
Storage:    Fountain plain-text files
Tech stack: C++, Qt 6
```

---

## Example 45

**Intent:**
DNA relationship calculator for genealogy, enter shared cM and get likely relationships

**Spec:**
```
Type:       Desktop application (genetic genealogy calculator)
Data model: Match(id, name, shared_cm, longest_segment_cm, testing_company)
            Relationship(id, label, min_cm, max_cm, average_cm)
Features:   - Enter a match's shared centimorgans
            - List possible relationships with probability ranges
            - Store matches with notes and suspected ancestor lines
            - Group matches into clusters by shared matches
            - Import match lists from CSV exports
Storage:    SQLite database
Tech stack: Python, PySide6, pandas
```

---

## Example 46

**Intent:**
invoice + timesheet thing for a translator, charge per word or per hour

**Spec:**
```
Type:       Desktop application (freelance invoicing)
Data model: Client(id, name, address, currency, vat_rate)
            Job(id, client_id -> Client, title, language_pair, billing_type, word_count, hours, rate)
            Invoice(id, client_id -> Client, number, issued_on, due_on, status)
            InvoiceLine(invoice_id -> Invoice, job_id -> Job, amount)
Features:   - Record jobs billed per word or per hour
            - Count words from an imported DOCX source file
            - Generate numbered invoices from finished jobs
            - Export invoices to PDF in the client's currency
            - Show unpaid and overdue invoices
Storage:    SQLite database
Tech stack: Python, PyQt6, python-docx, WeasyPrint
```

---

## Example 47

**Intent:**
Our lab does PCR and I want a desktop tool to calculate master mix volumes for any number of samples.

**Spec:**
```
Type:       Desktop application (lab calculator)
Data model: Protocol(id, name, reaction_volume_ul, overage_percent)
            Component(id, protocol_id -> Protocol, name, stock_conc, final_conc, unit)
Features:   - Save PCR protocols with their components and concentrations
            - Calculate per-reaction and master-mix volumes for N samples
            - Add an overage percentage for pipetting loss
            - Print a checklist sheet for the bench
            - Convert between concentration units
Storage:    JSON protocol files
Tech stack: Python, Tkinter
```

---

## Example 48

**Intent:**
desktop app to plan d&d dungeon maps on a grid and then show only the revealed parts on a second screen for players

**Spec:**
```
Type:       Desktop application (battle map with fog of war)
Data model: Map(id, name, image_path, grid_size_px, fog_mask)
            Token(id, map_id -> Map, name, image_path, x, y, is_hidden)
Features:   - Load a map image and overlay an adjustable grid
            - Paint fog of war on and off on the GM view
            - Show a player view window on a second monitor with fog applied
            - Drag character and monster tokens on the grid
            - Measure distances in squares and feet
Storage:    Map project folder with JSON and images
Tech stack: C#, Avalonia UI
```

---

## Example 49

**Intent:**
random tables roller for game masters, like roll on a table of tavern names or random encounters

**Spec:**
```
Type:       Desktop application (random table roller)
Data model: Table(id, name, category, dice)
            Entry(id, table_id -> Table, range_min, range_max, text)
Features:   - Create tables with weighted dice ranges
            - Roll on a table and show the result
            - Resolve nested table references inside entries
            - Keep a history of results for the session
            - Import tables from plain text lists
Storage:    YAML files in a tables folder
Tech stack: Go, Fyne
```

---

## Example 50

**Intent:**
batch subtitle translator that keeps the timing

**Spec:**
```
Type:       Desktop application (subtitle translation)
Data model: Job(id, input_file, source_lang, target_lang, status)
            Cue(index, start_ms, end_ms, source_text, target_text)
Features:   - Load one or many SRT files
            - Translate cue text with a translation API while keeping timings
            - Merge short cues before translating to keep sentence context
            - Review translations side by side and edit them
            - Save translated files with a language suffix
Storage:    Files on disk, API key in the OS keychain
Tech stack: Python, PySide6, DeepL API, keyring
```

---

## Example 51

**Intent:**
a hangul typing trainer, I'm learning korean and want to get faster on the 2-set keyboard

**Spec:**
```
Type:       Desktop application (Korean typing tutor)
Data model: Drill(id, level, type, content)
            Result(id, drill_id -> Drill, cpm, accuracy, completed_at)
Features:   - Show the Dubeolsik keyboard layout with the next jamo highlighted
            - Compose jamo into syllable blocks as the user types
            - Progress from single jamo to words to sentences
            - Measure characters per minute and accuracy
            - Repeat drills for the most-missed keys
Storage:    SQLite database
Tech stack: Rust, egui
```

---

## Example 52

**Intent:**
self service check in kiosk for a dentist waiting room

**Spec:**
```
Type:       Desktop application (patient check-in kiosk)
Data model: Appointment(id, patient_name, date_of_birth, scheduled_at, dentist, status)
            CheckIn(id, appointment_id -> Appointment, checked_in_at)
Features:   - Run full screen in kiosk mode on a touchscreen
            - Look up today's appointment by surname and date of birth
            - Mark the patient as arrived and show the expected wait
            - Notify reception on their desktop
            - Clear all data from the screen after 30 seconds
API:        REST
            GET  /appointments/today
            POST /checkins
Storage:    Practice management database through its API
Tech stack: Electron, TypeScript, React
```

---

## Example 53

**Intent:**
So I coach an under-12 netball team and every week I spend ages working out who plays which position so everyone gets fair time. Could a little program on my laptop do the rotations for me?

**Spec:**
```
Type:       Desktop application (youth team rotation planner)
Data model: Player(id, name, preferred_positions, available)
            Match(id, opponent, date, quarters)
            Rotation(match_id -> Match, quarter, position, player_id -> Player)
Features:   - Mark which players are available for a match
            - Generate quarter-by-quarter positions so playing time is equal
            - Respect preferred and banned positions per player
            - Track total quarters played per player across the season
            - Print the rotation sheet for the bench
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 54

**Intent:**
attendance register with QR codes, students scan their card at the classroom webcam

**Spec:**
```
Type:       Desktop application (class attendance)
Data model: Student(id, name, class_group, qr_token)
            Lesson(id, class_group, starts_at, room)
            Attendance(lesson_id -> Lesson, student_id -> Student, scanned_at, status)
Features:   - Generate printable QR ID cards for each student
            - Read QR codes from the webcam and mark students present
            - Mark students late after a set number of minutes
            - Show who is still missing on screen
            - Export weekly attendance to CSV
Storage:    SQLite database
Tech stack: Python, OpenCV, pyzbar, PySide6
```

---

## Example 55

**Intent:**
lyrics prompter for church worship, shows song lyrics on the projector and i control it from my laptop

**Spec:**
```
Type:       Desktop application (lyrics presentation)
Data model: Song(id, title, author, ccli_number)
            Section(id, song_id -> Song, label, text, position)
            Service(id, date, title)
            ServiceItem(service_id -> Service, song_id -> Song, position)
Features:   - Store songs split into verses, choruses and bridges
            - Build a running order for each service
            - Show the current slide full screen on the projector output
            - Preview the next slide on the operator screen
            - Blank the screen to black with one key
Storage:    SQLite database
Tech stack: Electron, TypeScript, Svelte
```

---

## Example 56

**Intent:**
backing track looper for practising, slow down an mp3 without changing the pitch and loop a section

**Spec:**
```
Type:       Desktop application (music practice player)
Data model: Track(id, file_path, title, duration_ms)
            LoopMarker(id, track_id -> Track, name, start_ms, end_ms)
Features:   - Play MP3, WAV and FLAC files
            - Change playback speed from 50% to 125% without changing pitch
            - Shift pitch by semitones independently
            - Set A-B loop points and save them as named markers
            - Show the waveform for precise loop selection
Storage:    SQLite for markers
Tech stack: C++, JUCE, Rubber Band Library
```

---

## Example 57

**Intent:**
i want to make a game where u type fast to cast spells in a wizard duel, 1v1 on same pc

**Spec:**
```
Type:       Desktop game (typing duel, local multiplayer)
Data model: Spell(id, incantation, damage, effect, cast_time_ms)
            Match(id, winner, duration_sec)
Features:   - Split the keyboard into left and right halves for two players
            - Cast a spell when a player finishes typing its incantation
            - Interrupt the opponent's spell with a quick counter-word
            - Show health bars and spell effects for both wizards
            - Pick from a deck of five spells before each duel
Storage:    Local match history file
Tech stack: Python, Arcade
```

---

## Example 58

**Intent:**
A spelling bee game for my classroom where I enter this week's words and kids hear them read out loud and type them.

**Spec:**
```
Type:       Desktop game (educational spelling)
Data model: WordList(id, week, title)
            Word(id, list_id -> WordList, text, example_sentence)
            Attempt(id, student_name, word_id -> Word, typed, correct, attempted_at)
Features:   - Enter a weekly word list with example sentences
            - Read each word and sentence aloud with text-to-speech
            - Check the typed spelling and show the correct one on a miss
            - Give bees as rewards for streaks of correct words
            - Show the teacher which words were missed most
Storage:    SQLite database
Tech stack: C#, WPF, System.Speech
```

---

## Example 59

**Intent:**
roguelike deckbuilder about running a food truck, cards are ingredients

**Spec:**
```
Type:       Desktop game (roguelike deckbuilder)
Data model: Card(id, name, ingredient_type, cost, flavor_points, effect)
            Customer(id, name, craving, patience, tip)
            Run(id, seed, day, money, deck_json)
Features:   - Draw a hand of ingredient cards each turn
            - Combine cards into dishes that satisfy customer cravings
            - Buy new ingredient cards at the market between days
            - Generate each run from a random seed
            - End the run when the truck runs out of money
Storage:    Local save file for the current run
Tech stack: Godot 4, GDScript
```

---

## Example 60

**Intent:**
idk a game about stacking boxes on a moving truck with real physics, dont let them fall off

**Spec:**
```
Type:       Desktop game (physics stacking)
Features:   - Drop boxes of different sizes and weights onto a flatbed truck
            - Simulate the truck accelerating, braking and turning
            - Lose points for boxes that fall off
            - Add ropes the player can tie to secure the load
            - Score by delivered boxes per route
Storage:    Local high-score file
Tech stack: Unity, C#
```

---

## Example 61

**Intent:**
tower defence where you build the maze yourself with walls and the enemies pathfind through it

**Spec:**
```
Type:       Desktop game (mazing tower defence)
Data model: Tower(id, type, x, y, level)
            Enemy(id, type, hp, speed, x, y)
            Wave(number, enemy_types, count)
Features:   - Place walls and towers freely on an open grid
            - Recompute enemy paths with A* after each placement
            - Block placements that would seal the exit completely
            - Upgrade towers with gold earned from kills
            - Speed up and pause the game
Storage:    Local save file
Tech stack: Rust, Bevy
```

---

## Example 62

**Intent:**
sports quiz game for our pub league, rounds on picture questions and music clips

**Spec:**
```
Type:       Desktop application (pub quiz host)
Data model: Quiz(id, title, date)
            Round(id, quiz_id -> Quiz, title, type, position)
            Question(id, round_id -> Round, text, media_path, answer, points)
            Team(id, quiz_id -> Quiz, name)
            Score(team_id -> Team, round_id -> Round, points)
Features:   - Build rounds with text, picture and audio-clip questions
            - Show questions full screen on a projector
            - Play audio clips with a start and stop offset
            - Enter team scores after each round
            - Show a live leaderboard between rounds
Storage:    SQLite database and a media folder
Tech stack: Python, PySide6, QtMultimedia
```

---

## Example 63

**Intent:**
a game that teaches kids how circuits work, connect batteries bulbs and switches

**Spec:**
```
Type:       Desktop game (educational electronics)
Data model: Puzzle(id, title, parts_available, goal)
            Component(id, type, resistance, voltage)
Features:   - Drag batteries, wires, bulbs, switches and resistors onto a board
            - Simulate current flow and light bulbs by brightness
            - Show a short circuit with a warning animation
            - Give puzzles such as "light two bulbs with one switch"
            - Unlock new components as puzzles are solved
Storage:    Local progress file
Tech stack: Godot 4, GDScript
```

---

## Example 64

**Intent:**
Me and my brother want a game where we're two robots tied together with a cable and have to solve puzzles, same keyboard.

**Spec:**
```
Type:       Desktop game (co-op puzzle-platformer)
Data model: Level(id, tilemap_file, cable_length, par_time_sec)
Features:   - Control two robots on one keyboard (WASD and arrows)
            - Simulate a physics cable connecting the robots
            - Swing one robot from a ledge while the other anchors
            - Power doors by plugging the cable into sockets
            - Restart a level instantly with one key
Storage:    Local save of completed levels
Tech stack: Godot 4, GDScript
```

---

## Example 65

**Intent:**
tactics game with medieval chess-like units but each has a special move, play against AI

**Spec:**
```
Type:       Desktop game (turn-based tactics)
Data model: UnitType(id, name, move_pattern, attack, hp, special_ability)
            Board(width, height, terrain_json)
            Match(id, difficulty, winner, turns)
Features:   - Move units on a grid using their move patterns
            - Use one special ability per unit per match
            - Apply terrain bonuses for hills and forests
            - Play against an AI using minimax with alpha-beta pruning
            - Offer three AI difficulty levels
Storage:    Local match history
Tech stack: C++, Raylib
```

---

## Example 66

**Intent:**
text adventure engine where I write rooms in a simple file and it becomes a playable game

**Spec:**
```
Type:       Command-line tool (text adventure engine)
Data model: Room(id, name, description, exits)
            Item(id, name, description, room_id -> Room, portable)
            Player(location_id -> Room, inventory)
Features:   - Load rooms, items and exits from a YAML world file
            - Parse commands like "go north", "take lamp", "use key on door"
            - Track inventory and locked exits
            - Save and restore game progress
            - Validate the world file and report broken exits
Input:      YAML world file
Storage:    JSON save file
Tech stack: Python, PyYAML
```

---

## Example 67

**Intent:**
I play the trumpet in a brass band and I'd like a tool to keep our sheet music library catalogued, which pieces we own, parts missing, and who borrowed what.

**Spec:**
```
Type:       Desktop application (sheet music library)
Data model: Piece(id, title, composer, arranger, genre, cabinet_location)
            Part(id, piece_id -> Piece, instrument, copies, is_missing)
            Member(id, name, instrument)
            Loan(id, part_id -> Part, member_id -> Member, loaned_on, returned_on)
Features:   - Catalogue pieces and their individual instrument parts
            - Flag missing or damaged parts
            - Record loans of parts to band members
            - List overdue loans
            - Search by title, composer or genre
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 68

**Intent:**
guitar tab editor

**Spec:**
```
Type:       Desktop application (guitar tablature editor)
Data model: Song(id, title, tempo, tuning)
            Measure(id, song_id -> Song, position, time_signature)
            Note(id, measure_id -> Measure, string, fret, beat, duration, technique)
Features:   - Enter notes on a six-line tab staff by string and fret
            - Mark bends, slides and hammer-ons
            - Play the tab back with MIDI sounds
            - Change tuning and transpose fret numbers
            - Export to ASCII tab and PDF
Storage:    JSON song files
Tech stack: Java, JavaFX, javax.sound.midi
```

---

## Example 69

**Intent:**
character name generator for writers, pick a culture and era and it gives first and last names

**Spec:**
```
Type:       Desktop application (name generator)
Data model: NameSet(id, culture, era, gender, kind)
            Name(id, set_id -> NameSet, value, frequency)
            Favourite(id, full_name, note)
Features:   - Generate full names from a chosen culture, era and gender
            - Weight results by historical frequency
            - Lock a first or last name and regenerate the other
            - Save favourites with a note on the character
            - Copy names to the clipboard
Storage:    Bundled SQLite name data, favourites in a user database
Tech stack: Go, Wails, Vue
```

---

## Example 70

**Intent:**
Plot outline tool where I can see each character's storyline as a colored line across the chapters.

**Spec:**
```
Type:       Desktop application (plot timeline)
Data model: Character(id, name, color)
            Chapter(id, title, position)
            Beat(id, chapter_id -> Chapter, character_id -> Character, summary)
Features:   - Show chapters as columns and characters as coloured rows
            - Add beats where a character and chapter meet
            - Drag beats to another chapter
            - Highlight chapters where a character is absent too long
            - Export the outline as a printable chart
Storage:    JSON project file
Tech stack: Python, PySide6 (QGraphicsView)
```

---

## Example 71

**Intent:**
family tree but for horses, my aunt breeds them and wants pedigree charts

**Spec:**
```
Type:       Desktop application (horse pedigree)
Data model: Horse(id, name, registration_no, sex, foaling_date, colour, breed)
            Parentage(horse_id -> Horse, sire_id -> Horse, dam_id -> Horse)
            Breeding(id, mare_id -> Horse, stallion_id -> Horse, covered_on, due_on, outcome)
Features:   - Register horses with registration numbers and markings
            - Draw a five-generation pedigree chart
            - Calculate the inbreeding coefficient for a planned mating
            - Track breeding dates and expected foaling dates
            - Print pedigree certificates
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 72

**Intent:**
cemetery headstone records for our local history society, we photograph graves and transcribe them

**Spec:**
```
Type:       Desktop application (memorial inscription records)
Data model: Cemetery(id, name, parish, address)
            Plot(id, cemetery_id -> Cemetery, section, row, number, latitude, longitude)
            Inscription(id, plot_id -> Plot, transcription, condition)
            Interment(id, plot_id -> Plot, name, death_date, age)
            Photo(id, plot_id -> Plot, file_path)
Features:   - Record plots with section, row and GPS position
            - Transcribe inscriptions next to the zoomable photo
            - Index each named person in a grave
            - Search by surname across all cemeteries
            - Export a printable index
Storage:    SQLite database and photo folder
Tech stack: Python, PySide6
```

---

## Example 73

**Intent:**
Hi, I'm working as tax helper for small shops. I need software to calculate VAT returns each quarter from their sales and purchase list.

**Spec:**
```
Type:       Desktop application (VAT return preparation)
Data model: Business(id, name, vat_number, scheme)
            Transaction(id, business_id -> Business, date, type, net, vat_rate, vat_amount)
            Return(id, business_id -> Business, period_start, period_end, boxes_json, status)
Features:   - Import sales and purchase lists from Excel or CSV
            - Calculate output and input VAT per rate
            - Fill the nine VAT return boxes for a quarter
            - Lock a period once the return is filed
            - Print a working summary for each client
Storage:    SQLite database
Tech stack: Python, PySide6, pandas
```

---

## Example 74

**Intent:**
depreciation schedule calculator for fixed assets

**Spec:**
```
Type:       Desktop application (fixed asset register)
Data model: Asset(id, description, category, purchase_date, cost, residual_value, useful_life_years, method)
            Disposal(id, asset_id -> Asset, date, proceeds)
Features:   - Register assets with cost and useful life
            - Calculate straight-line and reducing-balance depreciation
            - Show a year-by-year schedule per asset
            - Calculate gain or loss on disposal
            - Export the register to Excel
Storage:    SQLite database
Tech stack: Java, Swing, Apache POI
```

---

## Example 75

**Intent:**
cat tool for translators, splits the doc into sentences and remembers translations i did before

**Spec:**
```
Type:       Desktop application (computer-assisted translation)
Data model: Project(id, name, source_lang, target_lang)
            Segment(id, project_id -> Project, position, source, target, status)
            TMEntry(id, source, target, source_lang, target_lang, created_at)
Features:   - Split DOCX files into sentence segments
            - Edit translations in a two-column grid
            - Suggest fuzzy matches from translation memory
            - Save confirmed segments into translation memory
            - Rebuild the translated DOCX with original formatting
Storage:    SQLite translation memory, TMX import and export
Tech stack: Java, JavaFX, Okapi Framework
```

---

## Example 76

**Intent:**
Spreadsheet-like tool for our quality control lab to log pH and conductivity readings and flag anything out of spec.

**Spec:**
```
Type:       Desktop application (QC lab results)
Data model: Product(id, name, code)
            Specification(id, product_id -> Product, parameter, min_value, max_value, unit)
            Batch(id, product_id -> Product, batch_number, produced_on)
            Reading(id, batch_id -> Batch, parameter, value, analyst, measured_at)
Features:   - Enter readings per batch and parameter
            - Highlight results outside specification in red
            - Require a reason when an out-of-spec result is saved
            - Draw control charts per parameter
            - Export a certificate of analysis to PDF
Storage:    SQLite database with audit log table
Tech stack: C#, WinForms, ScottPlot
```

---

## Example 77

**Intent:**
microscope cell counter, i load a photo and click cells and it counts by type

**Spec:**
```
Type:       Desktop application (manual cell counter)
Data model: Image(id, file_path, sample_name, magnification)
            Marker(id, image_id -> Image, x, y, cell_type)
            CellType(name, color, hotkey)
Features:   - Open microscope images and zoom and pan
            - Click to place coloured markers by cell type
            - Switch cell types with number keys
            - Show live counts and percentages per type
            - Export counts to CSV
Storage:    JSON sidecar file next to each image
Tech stack: Python, napari
```

---

## Example 78

**Intent:**
light show programmer synced to music for christmas lights on my house

**Spec:**
```
Type:       Desktop application (light show sequencer)
Data model: Sequence(id, name, audio_file, duration_ms)
            Channel(id, name, controller_ip, universe, address)
            Effect(id, sequence_id -> Sequence, channel_id -> Channel, start_ms, end_ms, type, params)
Features:   - Show the audio waveform with a timeline of channels
            - Place on, fade, twinkle and chase effects on the timeline
            - Snap effects to detected beats
            - Preview the show on a virtual house layout
            - Play the show live over E1.31 (sACN) to controllers
Storage:    XML sequence files
Tech stack: C++, Qt 6, libsndfile
```

---

## Example 79

**Intent:**
gobo and colour lookup for lighting designers, which filter gel matches which colour

**Spec:**
```
Type:       Desktop application (lighting gel reference)
Data model: Gel(id, manufacturer, code, name, transmission_percent, hex_color, spectrum_json)
            Palette(id, show_name)
            PaletteGel(palette_id -> Palette, gel_id -> Gel)
Features:   - Browse gels from several manufacturers with swatches
            - Find the closest gel to a picked colour
            - Show cross-references between manufacturers
            - Build a gel palette per show
            - Print a cut list for the gel order
Storage:    Bundled SQLite gel database
Tech stack: Python, PySide6
```

---

## Example 80

**Intent:**
npc generator for my campaign with personality, voice quirks and secrets

**Spec:**
```
Type:       Desktop application (NPC generator)
Data model: Trait(id, category, text, weight)
            Npc(id, name, ancestry, occupation, personality, quirk, secret, notes, campaign)
Features:   - Generate NPCs by rolling on trait tables
            - Re-roll a single trait while keeping the rest
            - Save NPCs to a campaign roster
            - Edit and extend trait tables
            - Export an NPC as a printable card
Storage:    SQLite database
Tech stack: Python, Flet
```

---

## Example 81

**Intent:**
Soundboard for my tabletop sessions, ambient loops like tavern or rain plus one-shot effects

**Spec:**
```
Type:       Desktop application (ambience soundboard)
Data model: Scene(id, name)
            Sound(id, file_path, name, is_loop, volume)
            SceneSound(scene_id -> Scene, sound_id -> Sound, volume)
Features:   - Group looping ambiences into scenes (tavern, forest, storm)
            - Crossfade between scenes
            - Trigger one-shot effects from hotkeys
            - Mix the volume of each layer live
            - Scan a folder to import sound files
Storage:    JSON config file
Tech stack: C#, Avalonia, NAudio
```

---

## Example 82

**Intent:**
caption burner, take a video and srt and make a new video with the subtitles drawn in

**Spec:**
```
Type:       Desktop application (subtitle hardcoding)
Data model: Job(id, video_path, subtitle_path, output_path, status, progress)
            Style(font, size, color, outline, position)
Features:   - Pick a video and a matching SRT or ASS file
            - Choose font, size, colour and outline for the captions
            - Preview a frame with the styled subtitles
            - Render a new video with burned-in subtitles
            - Queue several jobs and show progress
Storage:    Local job list in JSON
Tech stack: Python, PySide6, FFmpeg
```

---

## Example 83

**Intent:**
something to check my subtitle files for reading speed problems

**Spec:**
```
Type:       Command-line tool (subtitle quality check)
Features:   - Parse SRT and WebVTT files
            - Calculate characters per second for each cue
            - Flag cues over a set CPS limit or shorter than one second
            - Flag lines over the maximum length and cues with more than two lines
            - Print a report with cue numbers and timecodes
Input:      Subtitle file path and optional limits
Tech stack: Python, pysrt
```

---

## Example 84

**Intent:**
emoji and symbol picker that pops up with a shortcut on linux

**Spec:**
```
Type:       Desktop application (character picker)
Data model: Symbol(codepoint, name, category, keywords)
            Recent(codepoint, used_at, count)
Features:   - Open a search popup with a global shortcut
            - Search emoji and Unicode symbols by name or keyword
            - Type the chosen character into the active window
            - Show recently and frequently used symbols first
            - Support skin tone selection
Storage:    Bundled Unicode data, recents in SQLite
Tech stack: Rust, GTK 4, gtk-rs
```

---

## Example 85

**Intent:**
text expander, type a short code and it replaces it with a full paragraph

**Spec:**
```
Type:       Desktop application (text expansion)
Data model: Snippet(id, abbreviation, expansion, folder, uses)
Features:   - Watch keystrokes for snippet abbreviations
            - Replace the abbreviation with its expansion text
            - Fill placeholders like {date} and {clipboard}
            - Organise snippets into folders
            - Pause expansion in chosen applications
Storage:    JSON snippets file
Tech stack: Python, pynput, PySide6
```

---

## Example 86

**Intent:**
Typing tutor for programmers that uses real code snippets with brackets and symbols.

**Spec:**
```
Type:       Desktop application (code typing trainer)
Data model: Snippet(id, language, source, code)
            Attempt(id, snippet_id -> Snippet, wpm, accuracy, error_keys, finished_at)
Features:   - Show code snippets with syntax highlighting
            - Auto-skip leading indentation on new lines
            - Measure WPM and accuracy including symbols
            - Report the slowest and most-missed keys
            - Let users import snippets from their own files
Storage:    SQLite database
Tech stack: TypeScript, Electron, Monaco Editor
```

---

## Example 87

**Intent:**
library self checkout kiosk for a school library with barcode scanner

**Spec:**
```
Type:       Desktop application (library self-checkout kiosk)
Data model: Book(id, barcode, title, author, status)
            Borrower(id, card_barcode, name, class_group, max_loans)
            Loan(id, book_id -> Book, borrower_id -> Borrower, loaned_on, due_on, returned_on)
Features:   - Scan a borrower card to start a session
            - Scan books to check them out or return them
            - Refuse loans over the borrower's limit or with overdue books
            - Print or show a due-date slip
            - Log out automatically after inactivity
Storage:    SQLite database on the library PC
Tech stack: Java, JavaFX
```

---

## Example 88

**Intent:**
a beat-matching game where you're a chef chopping vegetables to the rhythm

**Spec:**
```
Type:       Desktop game (rhythm)
Data model: Track(id, title, audio_file, bpm)
            NoteMap(id, track_id -> Track, difficulty, notes_json)
            Score(id, track_id -> Track, points, grade)
Features:   - Slide vegetables onto the board in time with the beat
            - Chop with a key press graded by timing accuracy
            - Show different cutting patterns for each vegetable
            - Include a note-map editor for adding new songs
            - Award letter grades per song
Storage:    Local JSON files
Tech stack: Unity, C#, FMOD
```

---

## Example 89

**Intent:**
word game where two players take turns adding a letter and try not to complete a word

**Spec:**
```
Type:       Desktop game (word game)
Features:   - Let two players or one player vs computer take turns adding letters
            - Check whether the fragment can still become a real word
            - Let a player challenge if they think no word exists
            - Give a letter penalty to the player who completes a word or loses a challenge
            - Use a trie built from a dictionary file for fast lookups
Storage:    Bundled word list
Tech stack: Java, Swing
```

---

## Example 90

**Intent:**
honestly just want a little crossword maker where i put in words and clues and it arranges them

**Spec:**
```
Type:       Desktop application (crossword generator)
Data model: Puzzle(id, title, width, height)
            Entry(id, puzzle_id -> Puzzle, answer, clue, row, col, direction)
Features:   - Enter answer words with their clues
            - Arrange words into an interlocking grid automatically
            - Number the grid and split clues into Across and Down
            - Print a blank puzzle and a separate answer sheet
            - Retry layouts to fit more words
Storage:    JSON puzzle files
Tech stack: Python, Tkinter, ReportLab
```

---

## Example 91

**Intent:**
sandbox game where you pour different liquids and powders and they react, like sand water lava

**Spec:**
```
Type:       Desktop game (falling-sand sandbox)
Features:   - Simulate a pixel grid of materials (sand, water, lava, stone, steam)
            - Paint materials with a brush of adjustable size
            - Apply reactions like lava plus water making stone and steam
            - Update cells with cellular automaton rules each frame
            - Save and load sandbox scenes as images
Storage:    PNG scene files
Tech stack: C, SDL2
```

---

## Example 92

**Intent:**
small city builder where you plan bus routes and people complain if they're late

**Spec:**
```
Type:       Desktop game (transit city builder)
Data model: Stop(id, x, y, name)
            Route(id, name, color, stop_ids, buses)
            Citizen(id, home_x, home_y, work_x, work_y, satisfaction)
Features:   - Draw bus routes through the city's stops
            - Simulate citizens commuting and choosing routes
            - Show complaint speech bubbles when trips are slow
            - Balance ticket income against bus running costs
            - Grow the city as satisfaction rises
Storage:    Local save files
Tech stack: C#, MonoGame
```

---

## Example 93

**Intent:**
I'd like a calm farming game where you look after bees, plant flowers and harvest honey over the seasons.

**Spec:**
```
Type:       Desktop game (beekeeping sim)
Data model: Hive(id, x, y, population, honey_kg, health, queen_age)
            FlowerPatch(id, x, y, species, bloom_season)
            GameDate(day, season, year)
Features:   - Place hives and plant flower patches on the farm
            - Grow colonies based on nearby flowers in bloom
            - Inspect hives for disease and swarming signs
            - Harvest and sell honey at the market
            - Cycle through seasons with winter survival checks
Storage:    Local save file
Tech stack: Godot 4, GDScript
```

---

## Example 94

**Intent:**
retro racing game with pseudo-3d roads like old arcade cabinets, but original tracks

**Spec:**
```
Type:       Desktop game (pseudo-3D racing)
Data model: Track(id, name, segments_json, scenery_theme)
            BestTime(track_id -> Track, time_ms, initials)
Features:   - Render the road with scanline-projected segments, curves and hills
            - Steer, accelerate and brake with keyboard or gamepad
            - Place roadside sprites that scale with distance
            - Race against a countdown with checkpoints adding time
            - Save best times with three-letter initials
Storage:    Local JSON file
Tech stack: JavaScript, HTML5 Canvas, Electron
```

---

## Example 95

**Intent:**
esports team manager sim where you pick players, train them and enter tournaments

**Spec:**
```
Type:       Desktop game (sports management)
Data model: Team(id, name, budget, fans)
            Player(id, team_id -> Team, handle, aim, teamwork, stamina, salary)
            Tournament(id, name, prize, start_week)
            MatchResult(id, tournament_id -> Tournament, team_a_id -> Team, team_b_id -> Team, winner_id -> Team)
Features:   - Sign and release players with contract salaries
            - Schedule weekly training focus
            - Simulate matches from player stats and team synergy
            - Enter tournaments and earn prize money
            - Show season history and player growth charts
Storage:    SQLite save file
Tech stack: C#, Unity
```

---

## Example 96

**Intent:**
family quiz game for christmas, everyone writes questions about each other first

**Spec:**
```
Type:       Desktop game (party quiz)
Data model: Player(id, name, avatar)
            Question(id, about_player_id -> Player, author_player_id -> Player, text, answer)
            Round(id, question_id -> Question, scores_json)
Features:   - Let each player secretly add questions about other players
            - Shuffle questions and show them on the TV one at a time
            - Let the subject reveal the true answer
            - Award points to everyone who guessed right
            - Play festive sounds and a final podium
Storage:    Local JSON game file
Tech stack: Python, Pygame
```

---

## Example 97

**Intent:**
fractions game for kids using pizza slices

**Spec:**
```
Type:       Browser game (educational fractions)
Features:   - Show pizza orders like "3/4 pepperoni" to fill
            - Let the player cut pizzas into equal slices
            - Drag toppings onto the right number of slices
            - Introduce equivalent fractions in later levels
            - Award stars for speed and accuracy
Storage:    Browser localStorage (progress)
Tech stack: TypeScript, Phaser 3
```

---

## Example 98

**Intent:**
planet orbit game to teach gravity, launch a satellite and try to get it into a stable orbit

**Spec:**
```
Type:       Desktop game (educational physics)
Data model: Scenario(id, title, bodies_json, target_orbit)
            Attempt(id, scenario_id -> Scenario, launch_angle, launch_speed, success)
Features:   - Simulate Newtonian gravity between planets, moons and the satellite
            - Set launch angle and speed and fire the satellite
            - Draw the predicted trajectory line
            - Detect stable orbits, crashes and escapes
            - Explain the result with Kepler's laws
Storage:    Bundled scenario JSON, attempts in a local file
Tech stack: Python, Pygame, NumPy
```

---

## Example 99

**Intent:**
Local co-op cooking-free chaos: a game where up to 4 players run a laundromat, washing and folding clothes before customers leave.

**Spec:**
```
Type:       Desktop game (local co-op)
Data model: Level(id, layout_file, duration_sec, target_coins)
            Order(id, items, colour_group, patience_sec)
Features:   - Support 1-4 players with gamepads on one screen
            - Sort clothes, run washers and dryers, and fold
            - Spoil orders when colours are mixed in one wash
            - Pay coins for orders finished before patience runs out
            - Unlock new laundromats with harder layouts
Storage:    Local save file
Tech stack: Unity, C#, Input System
```

---

## Example 100

**Intent:**
hex-based tactics game about wildlife rangers stopping poachers at night

**Spec:**
```
Type:       Desktop game (stealth turn-based tactics)
Data model: Ranger(id, name, hex_q, hex_r, vision, moves)
            Poacher(id, hex_q, hex_r, alert_level, patrol_route)
            Map(id, terrain_json, animal_herds_json)
Features:   - Move rangers on a hex map using axial coordinates
            - Limit vision with night-time field of view and torches
            - Track poachers by footprints left on tiles
            - Protect animal herds until dawn
            - Score missions by animals saved and poachers caught
Storage:    Local save files
Tech stack: Godot 4, C#
```

---

## Example 101

**Intent:**
choose your own adventure for my nephew about a dragon who is scared of fire

**Spec:**
```
Type:       Browser game (interactive fiction)
Data model: Page(id, text, illustration, choices_json)
Features:   - Show illustrated story pages with two or three choices
            - Read pages aloud with text-to-speech
            - Keep track of the path taken
            - Reach several happy endings
            - Restart from any earlier page
Storage:    Browser localStorage (bookmark)
Tech stack: Twine (Harlowe), HTML, CSS
```

---

## Example 102

**Intent:**
puzzle platformer where you play as a shadow that can only move on surfaces lit by a lamp you push around

**Spec:**
```
Type:       Desktop game (2D puzzle-platformer)
Data model: Level(id, tilemap_file, lamp_start, exit_x, exit_y)
Features:   - Cast real-time 2D shadows from a movable lamp
            - Let the shadow walk only along shadow edges on walls
            - Switch between pushing the lamp and moving the shadow
            - Reach the exit on each level
            - Undo moves step by step
Storage:    Local save of completed levels
Tech stack: Unity, C#, URP 2D lights
```

---

## Example 103

**Intent:**
choir attendance + who sings which part

**Spec:**
```
Type:       Desktop application (choir management)
Data model: Singer(id, name, voice_part, email, joined_on)
            Rehearsal(id, date, venue, pieces)
            Attendance(rehearsal_id -> Rehearsal, singer_id -> Singer, present)
Features:   - Keep a roster of singers grouped by voice part (SATB)
            - Tick attendance at each rehearsal
            - Show balance of present singers per part
            - Flag singers who missed three rehearsals in a row
            - Export the roster to CSV for emails
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 104

**Intent:**
ear training app, plays intervals and chords and i guess what they are

**Spec:**
```
Type:       Desktop application (ear training)
Data model: ExerciseType(id, name, options)
            Answer(id, exercise_type_id -> ExerciseType, played, guessed, correct, answered_at)
Features:   - Play random intervals, chords or scales with a piano sound
            - Let the user pick the answer from buttons
            - Replay the question and play the correct answer after a miss
            - Choose which intervals or chord qualities to include
            - Show accuracy per interval over time
Storage:    SQLite database
Tech stack: C#, Avalonia, MeltySynth (SoundFont synth)
```

---

## Example 105

**Intent:**
I'm a DJ and want to tag my tracks with energy level and key so I can plan smooth mixes

**Spec:**
```
Type:       Desktop application (DJ track planner)
Data model: Track(id, file_path, title, artist, bpm, musical_key, camelot_key, energy, tags)
            Mix(id, name, event_date)
            MixTrack(mix_id -> Mix, track_id -> Track, position)
Features:   - Scan a music folder and read ID3 tags
            - Detect BPM and key automatically
            - Tag tracks with energy level and genre
            - Suggest next tracks with compatible Camelot keys and similar BPM
            - Build and export mix plans as M3U playlists
Storage:    SQLite database
Tech stack: Python, PySide6, librosa, mutagen
```

---

## Example 106

**Intent:**
prompt book for stage managers, script on one side with cue markers I can click

**Spec:**
```
Type:       Desktop application (stage manager prompt book)
Data model: Script(id, title, pdf_path)
            Cue(id, script_id -> Script, page, y_position, number, department, description, standby_page)
            Performance(id, date, notes)
Features:   - Show the script PDF with cue markers in the margin
            - Add lighting, sound and fly cues at a line
            - Highlight standby and go points as pages turn
            - Export a cue list per department
            - Keep a show report for each performance
Storage:    SQLite database
Tech stack: C#, WPF, PdfiumViewer
```

---

## Example 107

**Intent:**
we run an escape room and need a control program for the game master, timer on the room's TV and sending hints

**Spec:**
```
Type:       Desktop application (escape room game-master console)
Data model: Room(id, name, duration_min)
            Hint(id, room_id -> Room, puzzle, text)
            Session(id, room_id -> Room, team_name, started_at, finished_at, hints_used)
Features:   - Start, pause and adjust the countdown timer
            - Show the timer and hints full screen on the room display
            - Send prewritten or custom hints with a chime
            - Log each team's time and hints used
            - Show a leaderboard of fastest teams
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 108

**Intent:**
knitting pattern designer, colour grid charts for fair isle

**Spec:**
```
Type:       Desktop application (knitting chart designer)
Data model: Chart(id, name, width_stitches, height_rows, gauge)
            Cell(chart_id -> Chart, row, col, color_index, symbol)
            Palette(chart_id -> Chart, color_index, hex, yarn_name)
Features:   - Paint stitches on a grid with a yarn colour palette
            - Mirror and repeat motifs horizontally
            - Warn on floats longer than five stitches
            - Show row numbers from the bottom right as knitters read
            - Print the chart and an estimated yarn amount per colour
Storage:    JSON chart files
Tech stack: Java, JavaFX
```

---

## Example 109

**Intent:**
cross stitch pattern from a photo, reduce to DMC thread colours

**Spec:**
```
Type:       Desktop application (cross-stitch pattern generator)
Data model: Pattern(id, source_image, width_stitches, fabric_count, max_colors)
            Thread(code, name, rgb)
Features:   - Load a photo and resize it to a stitch grid
            - Reduce colours with k-means and match them to DMC threads
            - Assign a symbol to each thread colour
            - Let the user edit individual stitches
            - Export a printable symbol chart and thread shopping list
Storage:    Pattern files in JSON, bundled DMC colour table
Tech stack: Python, Pillow, scikit-learn, PySide6
```

---

## Example 110

**Intent:**
model railway control from pc, DCC, throttles and turnouts

**Spec:**
```
Type:       Desktop application (model railway control)
Data model: Locomotive(id, name, dcc_address, max_speed_step, functions)
            Turnout(id, name, dcc_address, state)
            Route(id, name, turnout_states_json)
Features:   - Drive locomotives with on-screen throttles and function buttons
            - Throw turnouts by clicking the track diagram
            - Set routes that switch several turnouts at once
            - Send commands to a DCC-EX command station over serial
            - Emergency-stop all trains with one key
Storage:    JSON layout file
Tech stack: Python, PySide6, pyserial
```

---

## Example 111

**Intent:**
astronomy observing log, what i looked at, which telescope, seeing conditions

**Spec:**
```
Type:       Desktop application (astronomy observing log)
Data model: Equipment(id, type, name, aperture_mm, focal_length_mm)
            Session(id, date, site, latitude, longitude, seeing, transparency)
            Observation(id, session_id -> Session, object_name, catalogue_id, equipment_id -> Equipment, notes, sketch_path)
Features:   - Log sessions with site and sky conditions
            - Record observations against catalogue objects (Messier, NGC)
            - Calculate object altitude for the session time
            - Track progress through observing lists
            - Attach sketches and photos
Storage:    SQLite database
Tech stack: Python, PySide6, Astropy
```

---

## Example 112

**Intent:**
bird sightings list on my pc, life list and which species where

**Spec:**
```
Type:       Desktop application (bird sighting log)
Data model: Species(id, common_name, scientific_name, family)
            Location(id, name, latitude, longitude)
            Sighting(id, species_id -> Species, location_id -> Location, seen_on, count, notes)
Features:   - Log sightings with species autocomplete from a checklist
            - Show a life list with first-seen dates
            - Show year lists and per-location lists
            - Plot sightings on an offline map
            - Export to eBird-compatible CSV
Storage:    SQLite database
Tech stack: Kotlin, Compose for Desktop
```

---

## Example 113

**Intent:**
beer recipe calculator for homebrewing, OG FG IBU and colour

**Spec:**
```
Type:       Desktop application (homebrew recipe calculator)
Data model: Recipe(id, name, style, batch_size_l, efficiency)
            Fermentable(id, recipe_id -> Recipe, name, weight_kg, ppg, lovibond)
            Hop(id, recipe_id -> Recipe, name, weight_g, alpha_acid, boil_min)
            Yeast(id, recipe_id -> Recipe, name, attenuation)
Features:   - Build recipes from grains, hops and yeast
            - Calculate original and final gravity and ABV
            - Calculate IBU using the Tinseth formula
            - Estimate colour in SRM with a colour swatch
            - Compare values against the chosen style's ranges
Storage:    SQLite database, BeerXML import and export
Tech stack: C#, WinForms
```

---

## Example 114

**Intent:**
woodworking cut list optimiser, I give it board sizes and pieces and it tells me how to cut with least waste

**Spec:**
```
Type:       Desktop application (cut list optimiser)
Data model: Stock(id, material, length_mm, width_mm, thickness_mm, quantity)
            Part(id, name, length_mm, width_mm, quantity, grain_locked)
            Plan(id, stock_id -> Stock, layout_json, waste_percent)
Features:   - Enter stock sheets or boards and required parts
            - Include saw kerf width in calculations
            - Pack parts with a guillotine-cut bin-packing algorithm
            - Respect grain direction for chosen parts
            - Draw and print cutting diagrams with dimensions
Storage:    JSON project files
Tech stack: C++, Qt 6
```

---

## Example 115

**Intent:**
swiss system pairing program for our chess club tournament

**Spec:**
```
Type:       Desktop application (chess tournament pairing)
Data model: Tournament(id, name, rounds, time_control)
            Player(id, tournament_id -> Tournament, name, rating)
            Pairing(id, round, white_id -> Player, black_id -> Player, result)
Features:   - Register players with ratings
            - Pair each round with Swiss rules (score groups, no rematches, colour balance)
            - Give a bye to the odd player out
            - Enter results and compute standings with Buchholz tiebreaks
            - Print pairings and standings
Storage:    SQLite database
Tech stack: Java, Swing
```

---

## Example 116

**Intent:**
darts scoreboard for 501 on a laptop next to the board

**Spec:**
```
Type:       Desktop application (darts scorer)
Data model: Player(id, name)
            Leg(id, game_type, winner_id -> Player)
            Visit(id, leg_id -> Leg, player_id -> Player, score, darts_thrown)
Features:   - Enter visit scores with a large on-screen keypad
            - Count down from 501 with double-out rules
            - Suggest checkouts when a finish is possible
            - Reject busts and restore the score
            - Show three-dart averages per player
Storage:    SQLite match history
Tech stack: Python, Kivy
```

---

## Example 117

**Intent:**
debate tournament tab software, rounds, judges, team rankings

**Spec:**
```
Type:       Desktop application (debate tabulation)
Data model: Team(id, institution, name)
            Adjudicator(id, name, institution, rating)
            Round(id, number, motion)
            Debate(id, round_id -> Round, room, positions_json, chair_id -> Adjudicator)
            Ballot(id, debate_id -> Debate, ranks_json, speaker_scores_json)
Features:   - Draw rounds by power pairing on team points
            - Allocate adjudicators avoiding institution conflicts
            - Enter ballots with speaker scores
            - Rank teams and speakers after each round
            - Generate the break for elimination rounds
Storage:    PostgreSQL on the tab room laptop
Tech stack: Python, Django (local server), HTMX
```

---

## Example 118

**Intent:**
golf handicap tracker for our society

**Spec:**
```
Type:       Desktop application (golf handicap tracker)
Data model: Member(id, name, handicap_index)
            Course(id, name, par, course_rating, slope_rating)
            Round(id, member_id -> Member, course_id -> Course, played_on, gross_score)
Features:   - Record rounds with course rating and slope
            - Calculate score differentials per round
            - Compute handicap index from the best 8 of the last 20
            - Show the society order of merit
            - Print scorecards with playing handicaps
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 119

**Intent:**
braille translator program to make text into braille for embossing

**Spec:**
```
Type:       Desktop application (braille translation)
Data model: Document(id, title, source_text, grade, line_length, page_length)
Features:   - Translate text to Grade 1 or Grade 2 braille
            - Preview braille cells and the back-translation side by side
            - Format pages for a chosen line and page length
            - Export BRF files for embossers
            - Import DOCX and plain text
Storage:    Files on disk
Tech stack: Python, liblouis, PySide6
```

---

## Example 120

**Intent:**
reader app for my son who has dyslexia, change font spacing and read it out with highlighting

**Spec:**
```
Type:       Desktop application (accessible reader)
Data model: Document(id, title, file_path, last_position)
            Preference(font, size, letter_spacing, line_spacing, background_color)
Features:   - Open text, DOCX and EPUB files
            - Adjust font, letter spacing, line spacing and background tint
            - Read aloud with word-by-word highlighting
            - Show a reading ruler that follows the line
            - Remember the reading position per document
Storage:    SQLite database
Tech stack: C#, WPF, Windows text-to-speech
```

---

## Example 121

**Intent:**
i want program to manage my aquarium, water tests and when i change water, for 3 tanks

**Spec:**
```
Type:       Desktop application (aquarium log)
Data model: Tank(id, name, volume_l, type)
            Inhabitant(id, tank_id -> Tank, species, count, added_on)
            WaterTest(id, tank_id -> Tank, tested_on, ph, ammonia, nitrite, nitrate, temperature)
            Maintenance(id, tank_id -> Tank, date, type, percent_changed)
Features:   - Log water tests for each tank
            - Highlight unsafe ammonia and nitrite levels
            - Chart parameters over time
            - Remind when the next water change is due
            - Track fish and plants per tank
Storage:    SQLite database
Tech stack: Python, Tkinter, Matplotlib
```

---

## Example 122

**Intent:**
bakers percentage recipe scaler for bread

**Spec:**
```
Type:       Desktop application (bread formula calculator)
Data model: Formula(id, name, hydration_percent)
            Ingredient(id, formula_id -> Formula, name, bakers_percent, is_flour, in_preferment)
Features:   - Enter ingredients as baker's percentages of total flour
            - Scale the formula to a target dough weight or number of loaves
            - Account for flour and water in a sourdough starter
            - Show hydration and salt percentage
            - Print a batch sheet in grams
Storage:    JSON formula files
Tech stack: Go, Fyne
```

---

## Example 123

**Intent:**
quilting layout planner where i arrange fabric blocks and it tells me how much fabric to buy

**Spec:**
```
Type:       Desktop application (quilt designer)
Data model: Quilt(id, name, rows, cols, block_size_in)
            Fabric(id, name, swatch_image, width_in)
            Block(quilt_id -> Quilt, row, col, pattern, fabric_ids)
Features:   - Lay out blocks on a quilt grid
            - Fill block patches with scanned fabric swatches
            - Rotate and swap blocks
            - Calculate yardage for each fabric including seam allowance
            - Print a cutting guide
Storage:    JSON project files with swatch images
Tech stack: Python, PySide6
```

---

## Example 124

**Intent:**
ham radio logbook with contest mode

**Spec:**
```
Type:       Desktop application (amateur radio logbook)
Data model: Contact(id, callsign, frequency_mhz, band, mode, rst_sent, rst_received, utc_time, exchange)
            Station(id, my_callsign, grid_square)
Features:   - Log contacts with UTC time and band from frequency
            - Flag duplicate contacts in contest mode
            - Read frequency and mode from the radio via CAT control
            - Show a running QSO rate
            - Import and export ADIF files
Storage:    SQLite database
Tech stack: C++, Qt 6, Hamlib
```

---

## Example 125

**Intent:**
I'm a vet nurse and want a simple drug dose calculator for dogs and cats by weight

**Spec:**
```
Type:       Desktop application (veterinary dose calculator)
Data model: Drug(id, name, concentration_mg_ml, route)
            DoseRule(id, drug_id -> Drug, species, mg_per_kg_min, mg_per_kg_max)
            Calculation(id, drug_id -> Drug, species, weight_kg, dose_mg, volume_ml, calculated_at)
Features:   - Pick a species and enter body weight in kg or lb
            - Calculate the dose range in mg and volume in ml
            - Warn when a dose is outside the allowed range
            - Edit the drug formulary
            - Print a dose label
Storage:    SQLite database
Tech stack: C#, WinForms
```

---

## Example 126

**Intent:**
chess clock app on the laptop with increment and delay

**Spec:**
```
Type:       Desktop application (game clock)
Data model: TimeControl(id, name, base_sec, increment_sec, delay_sec, mode)
Features:   - Show two large clocks side by side
            - Switch turns with the spacebar or a click
            - Support Fischer increment, Bronstein and simple delay
            - Flash and beep when a flag falls
            - Save custom time controls
Storage:    JSON settings file
Tech stack: Rust, iced
```

---

## Example 127

**Intent:**
rhythm game for drums with a MIDI electronic drum kit

**Spec:**
```
Type:       Desktop game (drum rhythm)
Data model: Song(id, title, audio_file, bpm)
            DrumChart(id, song_id -> Song, difficulty, notes_json)
            Score(id, chart_id -> DrumChart, accuracy, streak, played_at)
Features:   - Read hits from an electronic drum kit over MIDI
            - Map MIDI notes to kick, snare, toms, hi-hat and cymbals
            - Scroll notes on lanes in time with the audio
            - Grade hits with a latency calibration offset
            - Offer a practice mode that slows the song down
Storage:    Local JSON files
Tech stack: C++, SDL2, RtMidi
```

---

## Example 128

**Intent:**
typing racer game vs ghost of my previous best run

**Spec:**
```
Type:       Desktop game (typing race)
Data model: Passage(id, text, source)
            Run(id, passage_id -> Passage, wpm, accuracy, keystroke_times)
Features:   - Race a car across the screen by typing a passage
            - Replay the best run as a ghost car from saved keystroke times
            - Block progress until a typo is fixed
            - Show WPM live
            - Choose passages by length
Storage:    SQLite database
Tech stack: Python, Pygame
```

---

## Example 129

**Intent:**
word search generator + game

**Spec:**
```
Type:       Desktop game (word search)
Data model: Puzzle(id, title, size, words, grid)
Features:   - Generate a grid hiding words in eight directions
            - Fill empty cells with random letters
            - Let players select words by dragging across letters
            - Strike found words from the list and time the game
            - Print puzzles with answer keys
Storage:    JSON puzzle files
Tech stack: JavaScript, Electron
```

---

## Example 130

**Intent:**
bridge building game where trucks drive over and it collapses if badly designed

**Spec:**
```
Type:       Desktop game (bridge-building physics)
Data model: Level(id, gap_width, anchors_json, budget, vehicle_type)
            Design(id, level_id -> Level, joints_json, members_json, cost)
Features:   - Place joints and connect them with wood, steel or cable members
            - Stay within the level budget
            - Simulate loads with a spring-mass model
            - Colour members by stress and break overloaded ones
            - Drive a test vehicle across the bridge
Storage:    Local JSON designs
Tech stack: C#, Unity
```

---

## Example 131

**Intent:**
TD game where the map is a human body and towers are immune cells fighting germs

**Spec:**
```
Type:       Desktop game (educational tower defence)
Data model: Organ(id, name, path_json, difficulty)
            CellTower(id, name, cost, ability, target_germ_type)
            Germ(id, type, hp, speed, weakness)
Features:   - Place immune cells along blood vessels
            - Match tower abilities to germ weaknesses
            - Show a fact card when a new germ appears
            - Use vaccine power-ups between waves
            - Progress through organs as levels
Storage:    Local save file
Tech stack: Godot 4, GDScript
```

---

## Example 132

**Intent:**
roguelike where you're a ghost possessing objects in a haunted house

**Spec:**
```
Type:       Desktop game (roguelike)
Data model: Room(id, type, objects_json)
            Possessable(id, type, abilities, durability)
            Run(id, seed, floor, residents_scared)
Features:   - Generate a haunted house floor by floor from a seed
            - Possess furniture and objects to gain their abilities
            - Scare residents out before they finish an exorcism
            - Lose the current host when its durability runs out
            - Unlock new possessable objects between runs
Storage:    Local save files
Tech stack: Rust, Bevy
```

---

## Example 133

**Intent:**
cozy village builder where you place houses for animals and they request decorations

**Spec:**
```
Type:       Desktop game (cozy city builder)
Data model: Villager(id, species, name, happiness, request)
            Building(id, type, x, y, owner_id -> Villager)
            Decoration(id, type, x, y, cost)
Features:   - Place houses, paths and decorations on a tile map
            - Attract new animal villagers when happiness rises
            - Show villager requests as speech bubbles
            - Earn leaves currency from shops and gardens
            - Cycle day and night with a lantern lighting system
Storage:    Local save file
Tech stack: Godot 4, GDScript
```

---

## Example 134

**Intent:**
greenhouse farming game but its realistic, plant timing, soil ph, pests

**Spec:**
```
Type:       Desktop game (realistic farming sim)
Data model: Crop(id, species, days_to_harvest, ideal_ph, ideal_temp)
            Bed(id, x, y, soil_ph, nitrogen, moisture)
            Planting(id, bed_id -> Bed, crop_id -> Crop, sown_day, health)
            Pest(id, name, target_crops, spread_rate)
Features:   - Sow crops in beds with soil pH and nutrient levels
            - Control greenhouse temperature and humidity
            - Spread pests and let the player use traps or predators
            - Sell harvests at prices that change by season
            - Show a crop encyclopedia with real growing data
Storage:    SQLite save file
Tech stack: Unity, C#
```

---

## Example 135

**Intent:**
racing game where the track is drawn by the players before the race

**Spec:**
```
Type:       Desktop game (draw-your-track racing)
Data model: Track(id, name, spline_points, width, author)
            LapRecord(track_id -> Track, player, time_ms)
Features:   - Draw a closed track with the mouse and smooth it into a spline
            - Validate that the track does not cross itself too tightly
            - Race up to 4 local players on the drawn track
            - Place boost pads and jumps while editing
            - Share tracks as small text codes
Storage:    Local JSON tracks
Tech stack: JavaScript, Phaser 3, Electron
```

---

## Example 136

**Intent:**
horse racing stable management game, buy horses, train, pick jockeys, bet a bit

**Spec:**
```
Type:       Desktop game (racing stable management)
Data model: Horse(id, name, age, speed, stamina, form, value)
            Jockey(id, name, skill, fee)
            Race(id, name, distance_m, purse, date)
            Entry(id, race_id -> Race, horse_id -> Horse, jockey_id -> Jockey, finish_position)
Features:   - Buy and sell horses at weekly auctions
            - Set training plans that change speed, stamina and fatigue
            - Enter races and hire jockeys
            - Simulate races with a visual animated finish
            - Track stable finances across seasons
Storage:    SQLite save file
Tech stack: Python, PySide6
```

---

## Example 137

**Intent:**
Game show style buzzer game for the classroom with up to 6 teams using keyboard keys as buzzers.

**Spec:**
```
Type:       Desktop game (classroom buzzer quiz)
Data model: Team(id, name, buzzer_key, color, score)
            Question(id, category, text, answer, points)
Features:   - Assign a keyboard key to each team as a buzzer
            - Lock out other teams after the first buzz
            - Let the teacher mark answers right or wrong
            - Show categories and point values on a board
            - Display final standings with confetti
Storage:    Question sets as CSV files
Tech stack: Python, Pygame
```

---

## Example 138

**Intent:**
times tables game where you race a snail, gets faster if you get them right

**Spec:**
```
Type:       Desktop game (educational maths)
Data model: Player(id, name)
            FactStat(player_id -> Player, a, b, correct, wrong, avg_ms)
Features:   - Ask times-table questions and race against a snail
            - Speed the player's runner up on correct answers
            - Focus questions on facts the player gets wrong most
            - Show a heatmap of the 12x12 table by mastery
            - Reward finished races with stickers
Storage:    Local JSON per player
Tech stack: C#, MonoGame
```

---

## Example 139

**Intent:**
periodic table game where you guess elements from clues

**Spec:**
```
Type:       Browser game (educational chemistry)
Data model: Element(number, symbol, name, group, period, category, facts)
Features:   - Give clues one at a time (group, period, a fact, the symbol)
            - Award more points for guessing with fewer clues
            - Light up guessed elements on a periodic table
            - Offer a timed mode for symbol recall
            - Save progress toward completing the table
Storage:    Browser localStorage
Tech stack: TypeScript, Svelte
```

---

## Example 140

**Intent:**
local multiplayer game where 2-4 players defend a sandcastle from waves, building walls together

**Spec:**
```
Type:       Desktop game (local co-op defence)
Data model: Wave(number, height, interval_sec)
            Wall(id, x, y, strength)
Features:   - Support up to 4 gamepads on one screen
            - Dig sand and build walls around the castle
            - Erode walls with incoming waves of growing height
            - Share a bucket resource between players
            - Score the round by castle survival time
Storage:    Local high-score file
Tech stack: Lua, LÖVE
```

---

## Example 141

**Intent:**
tactics game with pirates ship to ship, wind direction matters

**Spec:**
```
Type:       Desktop game (naval turn-based tactics)
Data model: Ship(id, name, hull, sails, crew, cannons, x, y, heading)
            Wind(direction_deg, strength)
Features:   - Move ships on a hex sea where speed depends on wind angle
            - Fire broadsides only from the sides of a ship
            - Damage hull, sails or crew with different shot types
            - Board enemy ships when adjacent
            - Change wind direction randomly between turns
Storage:    Local save files
Tech stack: Java, libGDX
```

---

## Example 142

**Intent:**
Parser-based interactive fiction set inside an old submarine, write it in Inform 7

**Spec:**
```
Type:       Desktop game (parser interactive fiction)
Features:   - Model submarine compartments as rooms with hatches
            - Track oxygen that drops each turn
            - Implement custom verbs like "flood", "seal" and "ping"
            - Hide clues in logbooks the player can read
            - Provide several endings depending on crew saved
Storage:    Interpreter save files
Tech stack: Inform 7, Glulx
```

---

## Example 143

**Intent:**
puzzle platformer where gravity flips every time you collect a coin

**Spec:**
```
Type:       Desktop game (gravity-flip puzzle-platformer)
Data model: Level(id, tilemap_file, coins, par_flips)
Features:   - Run and jump with platform physics
            - Flip gravity when a coin is collected
            - Order coin collection to reach the exit
            - Count flips and compare to par
            - Unlock worlds after finishing levels
Storage:    Local save file
Tech stack: C++, Raylib
```

---

## Example 144

**Intent:**
gradebook that lets me write report comments faster with a comment bank

**Spec:**
```
Type:       Desktop application (report comment bank)
Data model: Student(id, name, pronoun, class_group)
            Comment(id, subject, category, band, text)
            Report(id, student_id -> Student, term, subject, comment_ids, final_text)
Features:   - Store comments by subject, topic and achievement band
            - Insert the student's name and pronouns automatically
            - Build a report by picking comments from each category
            - Warn if the same comment is used for too many students
            - Export all reports to a Word document
Storage:    SQLite database
Tech stack: Python, PySide6, python-docx
```

---

## Example 145

**Intent:**
random name picker for my class, spin wheel, dont pick the same kid twice

**Spec:**
```
Type:       Desktop application (classroom name picker)
Data model: ClassGroup(id, name)
            Student(id, class_id -> ClassGroup, name, picked_this_round)
Features:   - Show a spinning wheel with student names
            - Remove picked students until everyone has had a turn
            - Mark students absent for the day
            - Pick random groups of a chosen size
            - Switch between class lists
Storage:    JSON file of classes
Tech stack: JavaScript, Electron
```

---

## Example 146

**Intent:**
noise level meter for the classroom that shows a traffic light from the mic

**Spec:**
```
Type:       Desktop application (classroom noise monitor)
Data model: Settings(green_max_db, amber_max_db, smoothing_sec)
Features:   - Read microphone level and convert it to approximate decibels
            - Show a full-screen traffic light (green, amber, red)
            - Smooth readings to avoid flicker
            - Calibrate thresholds for the room
            - Count minutes spent in red during a lesson
Storage:    JSON settings file
Tech stack: Python, PyAudio, NumPy, Pygame
```

---

## Example 147

**Intent:**
ok so im a substitute teacher and every school i go to has different seating and i never know names. want something where i can take a photo of the seating chart they leave and quickly click on a kid to see their name and add notes like "helpful" or "talks a lot"

**Spec:**
```
Type:       Desktop application (substitute teacher class notes)
Data model: School(id, name)
            ClassSession(id, school_id -> School, date, period, chart_image_path)
            SeatNote(id, session_id -> ClassSession, x, y, student_name, tags, note)
Features:   - Import a photo of a seating chart for each class
            - Click a seat on the photo to add a student name and quick tags
            - Hover over a seat to see the name in large text
            - Reuse notes when returning to the same school and class
            - Export a summary to leave for the regular teacher
Storage:    SQLite database and image folder
Tech stack: Python, PySide6
```

---

## Example 148

**Intent:**
I play keyboard in a wedding band and between songs I fumble finding the right patch and lyrics. I'd love a laptop app that when I pick the next song it sends the program change to my synth and shows the lyrics big.

**Spec:**
```
Type:       Desktop application (live performance song switcher)
Data model: Song(id, title, key, bpm, lyrics, notes)
            Patch(id, song_id -> Song, midi_channel, bank_msb, bank_lsb, program)
            Setlist(id, name, song_ids)
Features:   - Step through a setlist with a foot pedal or arrow keys
            - Send MIDI bank select and program change for each song
            - Show lyrics and chords in large text with auto-scroll
            - Show the next song's title and key in a corner
            - Work fully offline on stage
Storage:    SQLite database
Tech stack: C#, Avalonia, DryWetMIDI
```

---

## Example 149

**Intent:**
My dad has been researching our family for 30 years in notebooks, and now he's 78 and wants to type it in but every program he tried was too complicated with tiny buttons. Something really simple, big text, one person per screen, and print a nice tree for the reunion.

**Spec:**
```
Type:       Desktop application (simplified family tree)
Data model: Person(id, first_name, last_name, birth_year, death_year, birthplace, story)
            Relation(id, person_id -> Person, related_id -> Person, type)
Features:   - Show one person per screen with large text and buttons
            - Add parents, partner or child with a guided step-by-step form
            - Jump between relatives by clicking their name
            - Print a wall chart of descendants on large paper (PDF)
            - Back up everything to a single file on a USB stick
Storage:    SQLite database
Tech stack: Python, Tkinter, Graphviz
```

---

## Example 150

**Intent:**
I'm a part-time bookkeeper for three charities and each grant has to be tracked separately, what was spent from which grant, and the funders want reports in their own format every quarter. Spreadsheets are getting messy.

**Spec:**
```
Type:       Desktop application (charity fund accounting)
Data model: Charity(id, name, registration_no)
            Grant(id, charity_id -> Charity, funder, amount, start_date, end_date, restricted)
            BudgetLine(id, grant_id -> Grant, category, budget_amount)
            Expense(id, charity_id -> Charity, grant_id -> Grant, budget_line_id -> BudgetLine, date, amount, supplier, receipt_path)
Features:   - Allocate each expense to a grant and budget line
            - Show spent versus budget per grant and line
            - Warn when a grant line is overspent or the grant has ended
            - Generate quarterly funder reports from templates
            - Attach scanned receipts to expenses
Storage:    One SQLite file per charity
Tech stack: Python, PySide6, Jinja2, openpyxl
```

---

## Example 151

**Intent:**
I'm a sign language interpreter, freelance, and I get booked by hospitals, courts, schools. I always forget mileage and which jobs had a cancellation fee. Need a desktop program for bookings and to see what to bill.

**Spec:**
```
Type:       Desktop application (interpreter booking and billing)
Data model: Client(id, name, type, billing_contact, cancellation_policy_hours)
            Booking(id, client_id -> Client, starts_at, ends_at, location, status, mileage_km)
            Invoice(id, client_id -> Client, period, total, paid)
Features:   - Record bookings with location and travel mileage
            - Mark late cancellations and apply the client's cancellation fee
            - Apply minimum call-out hours per client
            - Generate monthly invoices from completed bookings
            - Show a calendar of upcoming assignments
Storage:    SQLite database
Tech stack: C#, WPF, QuestPDF
```

---

## Example 152

**Intent:**
We are a small community theatre and every show I make the lighting plot by hand on paper: which light hangs where, what colour, which dimmer. Would be great to have a drawing program for that which also makes the paperwork list automatically.

**Spec:**
```
Type:       Desktop application (lighting plot designer)
Data model: Venue(id, name, plan_image)
            Position(id, venue_id -> Venue, name, x1, y1, x2, y2)
            Instrument(id, position_id -> Position, unit_no, type, wattage, gel, gobo, channel, dimmer, purpose)
Features:   - Draw hanging positions over a venue plan
            - Drag fixture symbols onto positions
            - Edit gel, channel, dimmer and purpose per instrument
            - Generate instrument schedule and channel hookup reports
            - Export the plot to PDF at scale
Storage:    JSON show files
Tech stack: Java, JavaFX
```

---

## Example 153

**Intent:**
i run a D&D game for 6 friends every other week and between sessions i forget who owes what quest, which npcs they met, what loot they have. i want a campaign tracker on my pc, not online, and searchable

**Spec:**
```
Type:       Desktop application (campaign tracker)
Data model: Session(id, number, date, summary)
            Npc(id, name, location, attitude, notes)
            Quest(id, title, giver_id -> Npc, status, reward)
            Item(id, name, holder, value, magical)
            Mention(session_id -> Session, npc_id -> Npc)
Features:   - Write session summaries and tag NPCs and quests in them
            - Track quest status from open to complete
            - Keep a party inventory and who holds each item
            - Search across all notes, NPCs and items
            - Show a timeline of sessions
Storage:    SQLite with full-text search
Tech stack: Python, Textual
```

---

## Example 154

**Intent:**
My lab has an old spectrophotometer that saves weird text files and every time we have to copy numbers into excel to make a standard curve. I'd like a program that reads those files, fits the curve and gives concentrations of the unknowns.

**Spec:**
```
Type:       Desktop application (spectrophotometry analysis)
Data model: Run(id, file_path, wavelength_nm, measured_at)
            Well(id, run_id -> Run, label, absorbance, is_standard, known_conc)
            Fit(run_id -> Run, slope, intercept, r_squared)
Features:   - Parse the instrument's text export files
            - Mark wells as standards and enter known concentrations
            - Fit a linear standard curve and show R squared
            - Calculate unknown concentrations with dilution factors
            - Export results and the plot to Excel and PDF
Storage:    Files on disk
Tech stack: Python, PySide6, NumPy, Matplotlib, openpyxl
```

---

## Example 155

**Intent:**
For years I've wanted a game about being a lighthouse keeper in the 1890s. You keep the lamp lit, log the weather, row out to rescue sailors, slowly lose your mind. Kind of a management game with a story.

**Spec:**
```
Type:       Desktop game (narrative management)
Data model: Day(number, weather, events_json)
            Keeper(sanity, health, fatigue)
            Supply(item, quantity)
            LogEntry(id, day, text)
Features:   - Manage lamp oil, wick trimming and lens cleaning each night
            - Write the daily weather log from observations
            - Trigger shipwreck events that need a rowing rescue
            - Lower sanity with isolation and unlock strange story events
            - Order supplies on the monthly supply boat
Storage:    Local save files
Tech stack: Unity, C#, Yarn Spinner
```

---

## Example 156

**Intent:**
my kids love racing games but they're 5 and 8 and can't handle the hard ones. i want to make a simple racing game for them with cartoon animals in bathtubs, no losing really, just fun, and both can play together on the tv

**Spec:**
```
Type:       Desktop game (kids' racing, local multiplayer)
Data model: Racer(id, animal, tub_color)
            Track(id, name, theme, length)
Features:   - Race two players split screen with gamepads
            - Steer automatically back onto the track when off course
            - Give rubber-banding so the trailing player catches up
            - Collect bubbles to fill a sticker book
            - Celebrate every finisher with a podium
Storage:    Local sticker book save
Tech stack: Godot 4, GDScript
```

---

## Example 157

**Intent:**
I coach junior basketball and I always thought it would be fun to make a management game based on that, where you develop teenage players over years and some go pro. Very stats heavy. Desktop, single player.

**Spec:**
```
Type:       Desktop game (youth sports management)
Data model: Player(id, name, age, height_cm, shooting, passing, defense, potential, academy_years)
            Season(id, year, league_position)
            Game(id, season_id -> Season, opponent, score_for, score_against, box_score_json)
            Transfer(id, player_id -> Player, club, fee, year)
Features:   - Recruit players aged 13-18 from scouting reports
            - Plan training that grows attributes toward hidden potential
            - Simulate games possession by possession with box scores
            - Sell graduates to pro clubs for academy income
            - Show career graphs for each player
Storage:    SQLite save file
Tech stack: C#, Avalonia
```

---

## Example 158

**Intent:**
i want to make a roguelike but turn based on a train, every carriage is a new level and you go toward the engine, enemies are bandits

**Spec:**
```
Type:       Desktop game (train roguelike)
Data model: Carriage(id, type, layout_json, depth)
            Enemy(id, type, hp, x, y, behaviour)
            Run(id, seed, carriage_reached, gold)
Features:   - Generate a train of themed carriages from a seed
            - Move turn by turn on a narrow grid with roof and inside routes
            - Fight bandits with melee and limited ammo
            - Decouple carriages to escape fights at a cost
            - Reach the engine to win the run
Storage:    Local save of the current run
Tech stack: Python, tcod
```

---

## Example 159

**Intent:**
grading program but for music exams, examiner listens and marks pieces, scales, sight reading, aural

**Spec:**
```
Type:       Desktop application (music exam marking)
Data model: Candidate(id, name, instrument, grade_level)
            Section(id, name, max_marks)
            Mark(candidate_id -> Candidate, section_id -> Section, marks, comment)
Features:   - List the day's candidates in order
            - Enter marks and comments per section during the exam
            - Total marks and assign pass, merit or distinction
            - Insert stock comments from a comment library
            - Print mark forms for each candidate
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 160

**Intent:**
hiii i need app for my piano students to do theory homework, like name the key signature, intervals. offline please my students dont all have internet

**Spec:**
```
Type:       Desktop application (music theory drills)
Data model: Student(id, name, level)
            Drill(id, type, level, question_json, answer)
            Result(id, student_id -> Student, drill_id -> Drill, correct, answered_at)
Features:   - Show key signatures, intervals and notes on a staff to identify
            - Generate questions by level
            - Give instant feedback with explanations
            - Save results per student on the same computer
            - Export a progress file for the teacher on a USB stick
Storage:    SQLite database
Tech stack: Python, PySide6, music21
```

---

## Example 161

**Intent:**
plz make a program to count words in my thesis chapters but not count the references and footnotes

**Spec:**
```
Type:       Desktop application (thesis word counter)
Data model: Chapter(id, file_path, title, word_goal)
            CountSnapshot(id, chapter_id -> Chapter, body_words, footnote_words, counted_at)
Features:   - Open DOCX chapters and count body text words
            - Exclude references, footnotes, captions and tables
            - Show totals against word limits per chapter
            - Track word count history as a line chart
            - Watch files and recount on save
Storage:    SQLite database
Tech stack: Python, python-docx, PySide6
```

---

## Example 162

**Intent:**
need simple pos for my market stall, runs on old laptop, no internet at the market

**Spec:**
```
Type:       Desktop application (offline point of sale)
Data model: Product(id, name, price, category, stock)
            Sale(id, sold_at, total, payment_method)
            SaleItem(sale_id -> Sale, product_id -> Product, quantity, price)
Features:   - Ring up sales with large product buttons
            - Calculate change for cash payments
            - Record card payments taken on a separate reader
            - Decrease stock and warn when items run low
            - Show end-of-day takings by payment method
Storage:    SQLite database
Tech stack: Python, Kivy
```

---

## Example 163

**Intent:**
gm initiative tracker that shows on a 2nd monitor for the players but hides monster hp

**Spec:**
```
Type:       Desktop application (initiative tracker)
Data model: Combatant(id, name, is_player, initiative, hp, max_hp, conditions, hidden)
            Encounter(id, name, round)
Features:   - Add players and monsters with initiative and HP
            - Sort by initiative and step through turns
            - Show a player-facing window with names and turn order only
            - Show monster health as vague states (healthy, bloodied) to players
            - Track conditions with round countdowns
Storage:    JSON encounter files
Tech stack: Python, PySide6
```

---

## Example 164

**Intent:**
srt to word doc converter so the client can review subtitles in a table

**Spec:**
```
Type:       Command-line tool (subtitle export)
Features:   - Read SRT files and parse cue numbers, timecodes and text
            - Write a DOCX table with columns for number, in, out and text
            - Add an empty column for reviewer comments
            - Convert the reviewed DOCX back into an updated SRT
            - Process a whole folder in one run
Input:      SRT file or folder path
Tech stack: Python, pysrt, python-docx
```

---

## Example 165

**Intent:**
font pairing helper, pick a heading font and it suggests body fonts that go with it

**Spec:**
```
Type:       Desktop application (font pairing)
Data model: Font(id, family, classification, x_height, weight_range, file_path)
            Pairing(id, heading_font_id -> Font, body_font_id -> Font, rating)
Features:   - Read installed fonts and classify them (serif, sans, slab, script)
            - Suggest body fonts based on contrast and x-height similarity
            - Preview a sample article with the pair
            - Rate pairs and save favourites
            - Export the pair as CSS font stack
Storage:    SQLite database
Tech stack: Python, fontTools, PySide6
```

---

## Example 166

**Intent:**
clipboard manager for mac that strips formatting when pasting

**Spec:**
```
Type:       Desktop application (clipboard manager)
Data model: ClipEntry(id, plain_text, rich_text, source_app, copied_at, pinned)
Features:   - Keep the last 200 clipboard entries
            - Paste as plain text with a dedicated shortcut
            - Search history from a menu bar popover
            - Exclude entries copied from chosen apps
            - Clear history on a schedule
Storage:    Local SQLite database
Tech stack: Swift, SwiftUI, AppKit (NSPasteboard)
```

---

## Example 167

**Intent:**
tiling window manager for linux x11 written in go

**Spec:**
```
Type:       Desktop application (X11 tiling window manager)
Data model: Workspace(id, layout, window_ids)
            Client(window_id, workspace_id -> Workspace, floating, geometry)
Features:   - Manage windows on X11 as the window manager
            - Tile windows in master-stack and grid layouts
            - Switch between nine workspaces with keybindings
            - Toggle floating mode per window
            - Read keybindings from a config file
Storage:    TOML config file
Tech stack: Go, xgb (X Go Binding)
```

---

## Example 168

**Intent:**
typing practice for medical transcriptionists, they listen to dictation and type it

**Spec:**
```
Type:       Desktop application (transcription practice)
Data model: Dictation(id, audio_file, specialty, reference_text, difficulty)
            Attempt(id, dictation_id -> Dictation, typed_text, accuracy, wpm, completed_at)
Features:   - Play dictation audio with foot-pedal-style hotkeys (play, rewind 3s)
            - Type the transcript in an editor
            - Compare the transcript with the reference using word-level diff
            - Highlight misspelled medical terms
            - Track accuracy by specialty
Storage:    SQLite database
Tech stack: C#, WPF, NAudio, DiffPlex
```

---

## Example 169

**Intent:**
hotel lobby kiosk that shows local events and a map

**Spec:**
```
Type:       Desktop application (lobby information kiosk)
Data model: Event(id, title, venue, starts_at, image_path, description)
            Place(id, name, category, latitude, longitude, walking_min)
Features:   - Run full screen with touch navigation
            - Show today's and this week's local events
            - Display nearby places on an offline map with walking times
            - Show a QR code to take details to a phone
            - Rotate an attract slideshow when idle
Storage:    SQLite database updated from a shared folder
Tech stack: Electron, TypeScript, Leaflet
```

---

## Example 170

**Intent:**
attendance kiosk for gym members, scan card at the door

**Spec:**
```
Type:       Desktop application (member check-in kiosk)
Data model: Member(id, card_number, name, photo_path, membership_end)
            Visit(id, member_id -> Member, checked_in_at)
Features:   - Read member cards with a USB RFID reader
            - Show the member's photo and a welcome message
            - Refuse entry with a red screen if membership has expired
            - Log every visit
            - Show staff a count of people currently in the gym
API:        REST
            POST /visits
            GET  /members/{card_number}
Storage:    PostgreSQL on the gym server
Tech stack: Java, JavaFX
```

---

## Example 171

**Intent:**
rhythm game where you play a conductor and wave the mouse in the right pattern for 3/4 and 4/4 time

**Spec:**
```
Type:       Desktop game (conducting rhythm)
Data model: Piece(id, title, audio_file, time_signature, bpm_map)
            Performance(id, piece_id -> Piece, accuracy, orchestra_mood)
Features:   - Show beat patterns for 2/4, 3/4 and 4/4 time
            - Track mouse gestures and match them to the beat points
            - Speed up or slow down the orchestra audio to follow the player's tempo
            - Show orchestra musicians reacting to accuracy
            - Grade each performance
Storage:    Local JSON scores
Tech stack: Unity, C#
```

---

## Example 172

**Intent:**
typing game for learning japanese romaji to kana

**Spec:**
```
Type:       Browser game (kana typing)
Data model: KanaSet(id, name, characters)
            Stat(kana, correct, wrong)
Features:   - Show hiragana or katakana falling from the top of the screen
            - Destroy a character when its romaji is typed
            - Introduce new kana gradually
            - Repeat weak characters more often
            - Show a mastery chart for each kana row
Storage:    Browser localStorage
Tech stack: JavaScript, PixiJS
```

---

## Example 173

**Intent:**
anagram party game, everyone races to find words from 7 letters, shown on the big screen

**Spec:**
```
Type:       Desktop game (anagram party)
Data model: Round(id, letters, valid_words, duration_sec)
            Player(id, name, color, score)
            Submission(round_id -> Round, player_id -> Player, word, points)
Features:   - Pick 7 letters that form at least one 7-letter word
            - Let players enter words on their own keyboard section or a second device
            - Reject invalid and repeated words
            - Score longer words higher and show who found unique ones
            - Reveal missed words at round end
Storage:    Bundled dictionary file
Tech stack: Python, Pygame
```

---

## Example 174

**Intent:**
sandbox where you build marble runs and test them

**Spec:**
```
Type:       Desktop game (3D physics sandbox)
Data model: Piece(id, type, x, y, z, rotation)
            Track(id, name, pieces_json)
Features:   - Snap ramps, funnels, loops and lifts onto a grid
            - Drop marbles and simulate them with rigid-body physics
            - Follow a marble with the camera
            - Time how long a marble takes to finish
            - Save and share tracks as files
Storage:    JSON track files
Tech stack: Godot 4, GDScript
```

---

## Example 175

**Intent:**
td game in space where you build turrets on asteroids and they drift

**Spec:**
```
Type:       Desktop game (orbital tower defence)
Data model: Asteroid(id, x, y, velocity_x, velocity_y, slots)
            Turret(id, asteroid_id -> Asteroid, type, level)
            Wave(number, enemy_types)
Features:   - Build turrets on drifting asteroids around a space station
            - Move asteroids slowly along orbits so coverage changes
            - Fire thrusters to nudge asteroids at an energy cost
            - Defend against waves of alien drones
            - Unlock turret types with research points
Storage:    Local save file
Tech stack: Unity, C#
```

---

## Example 176

**Intent:**
roguelite fishing game, each trip goes deeper and you upgrade the boat

**Spec:**
```
Type:       Desktop game (roguelite fishing)
Data model: Fish(id, species, depth_min, depth_max, rarity, value)
            Upgrade(id, name, cost, effect)
            Trip(id, seed, max_depth, catch_value)
Features:   - Generate fishing zones per trip from a seed
            - Cast and reel with a timing mini-game
            - Lose the catch if the line snaps
            - Sell fish and buy boat, rod and sonar upgrades
            - Unlock deeper zones with rarer fish
Storage:    Local save file
Tech stack: Lua, LÖVE
```

---

## Example 177

**Intent:**
city builder underwater, you manage air bubbles and pressure

**Spec:**
```
Type:       Desktop game (underwater city builder)
Data model: Module(id, type, x, y, depth, air_capacity, power_use)
            Colonist(id, name, job, oxygen)
Features:   - Build connected habitat modules on the seabed
            - Route air and power through pipes
            - Raise hull stress with depth and leak air on breaches
            - Assign colonists to kelp farms and fishing
            - Survive storms and equipment failures
Storage:    Local save file
Tech stack: C++, Unreal Engine 5
```

---

## Example 178

**Intent:**
vineyard simulation game, plant grapes, harvest at right time, make wine and age it

**Spec:**
```
Type:       Desktop game (vineyard sim)
Data model: Vineyard(id, name, soil, slope, sun_hours)
            Vine(id, vineyard_id -> Vineyard, variety, age_years, health)
            Vintage(id, year, variety, sugar_brix, acidity, barrels)
            Bottle(id, vintage_id -> Vintage, quality, aged_months)
Features:   - Plant grape varieties suited to soil and climate
            - Test sugar levels to choose harvest day
            - Ferment and age wine in barrels with quality changes
            - Sell bottles to merchants whose prices depend on reputation
            - Simulate yearly weather with frost and hail risk
Storage:    SQLite save
Tech stack: Godot 4, C#
```

---

## Example 179

**Intent:**
motorbike trial game side view, balance over obstacles

**Spec:**
```
Type:       Desktop game (2D trials racing)
Data model: Track(id, name, terrain_points, checkpoints)
            Result(track_id -> Track, time_ms, faults)
Features:   - Simulate a motorbike with suspension and rider lean
            - Control throttle, brake and lean with the keyboard
            - Count faults when the rider touches the ground
            - Respawn at checkpoints
            - Include a track editor
Storage:    Local JSON tracks and results
Tech stack: C++, SFML, Box2D
```

---

## Example 180

**Intent:**
manage a small motorsport team, hire drivers, design car upgrades, race weekends simulated

**Spec:**
```
Type:       Desktop game (motorsport management)
Data model: Team(id, name, budget, sponsor)
            Driver(id, name, pace, consistency, salary)
            CarPart(id, type, performance, reliability, cost)
            Race(id, track, laps, weather, results_json)
Features:   - Hire drivers and engineers with contracts
            - Research and fit car parts with a budget cap
            - Choose pit strategy and tyres before races
            - Simulate races lap by lap with live timing
            - Track championship standings across a season
Storage:    SQLite save file
Tech stack: Python, PySide6
```

---

## Example 181

**Intent:**
emoji guessing game for a party, guess movie titles from emoji sequences

**Spec:**
```
Type:       Desktop game (party guessing)
Data model: Puzzle(id, emojis, answer, category, difficulty)
            Team(id, name, score)
Features:   - Show emoji puzzles one by one on the TV
            - Run a countdown for each puzzle
            - Let the host award points to the team that answered
            - Reveal letters as hints after 15 seconds
            - Load extra puzzle packs from CSV
Storage:    Puzzles in CSV, scores in memory
Tech stack: JavaScript, Electron
```

---

## Example 182

**Intent:**
geography game where you drop pins on a map and see how many km off you are

**Spec:**
```
Type:       Browser game (geography guessing)
Data model: Place(id, name, country, latitude, longitude, difficulty)
            Round(id, place_id -> Place, guess_lat, guess_lon, distance_km, points)
Features:   - Name a city or landmark for the player to find
            - Let the player drop a pin on a blank world map
            - Calculate the distance with the haversine formula
            - Award points that decrease with distance
            - Show the correct location and a line to the guess
Storage:    Browser localStorage (best scores)
Tech stack: TypeScript, Leaflet, Vite
```

---

## Example 183

**Intent:**
coding game for teens where you write little programs to control a rover on mars

**Spec:**
```
Type:       Desktop game (educational programming)
Data model: Mission(id, title, map_json, goal, allowed_commands)
            Solution(id, mission_id -> Mission, code, steps_used, success)
Features:   - Write rover programs in a simple language with loops and ifs
            - Run the program step by step on a grid map
            - Highlight the current line while the rover moves
            - Check mission goals like collecting rock samples
            - Award stars for shorter programs
Storage:    Local save file
Tech stack: Python, Arcade, Lark (parser)
```

---

## Example 184

**Intent:**
co-op game for 2 where one player sees the map and the other is in the maze, they have to talk

**Spec:**
```
Type:       Desktop game (asymmetric local co-op)
Data model: Maze(id, seed, width, height, traps_json)
Features:   - Show a top-down map on one screen and first-person view on another
            - Generate mazes with traps and keys
            - Hide the explorer's position from the navigator except for pings
            - Count down a shared timer
            - Rate runs by time and pings used
Storage:    Local best times file
Tech stack: Unity, C#
```

---

## Example 185

**Intent:**
small tactics game in a hospital where you're doctors assigning to patients, turns are hours

**Spec:**
```
Type:       Desktop game (hospital tactics)
Data model: Doctor(id, name, specialty, fatigue, x, y)
            Patient(id, condition, severity, arrival_turn, treated)
            Ward(id, name, beds)
Features:   - Move doctors between wards each hour
            - Triage arriving patients by severity
            - Match specialties to conditions for faster treatment
            - Raise fatigue and force breaks
            - Score shifts by patients treated and lost
Storage:    Local save
Tech stack: C#, MonoGame
```

---

## Example 186

**Intent:**
twine-like tool to make my own interactive stories with images and variables

**Spec:**
```
Type:       Desktop application (interactive fiction editor)
Data model: Story(id, title, start_passage_id)
            Passage(id, story_id -> Story, name, text, x, y, image_path)
            Variable(id, story_id -> Story, name, initial_value)
Features:   - Lay out passages as boxes on a canvas with arrows for links
            - Write passages with link syntax and variable conditions
            - Play-test the story from any passage
            - Detect broken links and unreachable passages
            - Export a standalone HTML game
Storage:    JSON story files
Tech stack: Electron, TypeScript, React Flow
```

---

## Example 187

**Intent:**
puzzle platformer where you rewind time but only for objects, not yourself

**Spec:**
```
Type:       Desktop game (time puzzle-platformer)
Data model: Level(id, tilemap_file, objects_json)
            ObjectHistory(object_id, frame, x, y, state)
Features:   - Record positions of every movable object each frame
            - Rewind objects while the player keeps moving
            - Combine rewinds with switches, crates and falling platforms
            - Mark objects immune to rewind with a glow
            - Restart rooms instantly
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 188

**Intent:**
bellringing practice simulator for church bell ringers learning methods

**Spec:**
```
Type:       Desktop application (change-ringing simulator)
Data model: Method(id, name, stage, place_notation)
            Practice(id, method_id -> Method, bell_rung, errors, striking_ms)
Features:   - Generate rows from place notation for any method
            - Play bell sounds for all other bells automatically
            - Let the learner ring one bell with a key at the right time
            - Show the blue line for the learner's bell
            - Measure striking accuracy per blow
Storage:    SQLite database
Tech stack: Rust, egui, rodio
```

---

## Example 189

**Intent:**
orchestra seating and divisi planner

**Spec:**
```
Type:       Desktop application (orchestra seating planner)
Data model: Musician(id, name, instrument, section, seniority)
            Concert(id, title, date, programme)
            Seat(concert_id -> Concert, section, desk, position, musician_id -> Musician)
Features:   - Draw a stage layout with sections and desks
            - Drag musicians into seats for each concert
            - Mark divisi splits per piece within a section
            - Rotate desk partners fairly across concerts
            - Print seating charts for the librarian
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 190

**Intent:**
Audition scheduler for our musical. People sign up for slots, I need to see conflicts and print a call list for each day.

**Spec:**
```
Type:       Desktop application (audition scheduling)
Data model: Auditionee(id, name, email, age, roles_wanted, unavailable_json)
            Slot(id, day, start_time, room, length_min)
            Booking(slot_id -> Slot, auditionee_id -> Auditionee)
            Callback(id, auditionee_id -> Auditionee, role, notes)
Features:   - Create audition slots by day and room
            - Assign auditionees while respecting their unavailability
            - Flag double bookings
            - Add panel notes and callbacks per auditionee
            - Print a daily call list with times
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 191

**Intent:**
costume store inventory for theatre, sizes, which show used it, where its stored

**Spec:**
```
Type:       Desktop application (costume inventory)
Data model: Costume(id, description, period, gender, size, colour, rack, photo_path, condition)
            Show(id, title, year)
            Usage(costume_id -> Costume, show_id -> Show, character)
            Hire(id, costume_id -> Costume, hirer, out_on, back_on, fee)
Features:   - Catalogue costumes with photos and rack locations
            - Search by period, size and colour
            - Record which show and character used each costume
            - Track external hires and fees
            - Print labels with a QR code for each item
Storage:    SQLite database and photo folder
Tech stack: Python, PySide6, qrcode
```

---

## Example 192

**Intent:**
sound cue playback for theatre shows, press GO and the next sound plays with fades

**Spec:**
```
Type:       Desktop application (theatre sound cue player)
Data model: Show(id, name)
            Cue(id, show_id -> Show, number, name, file_path, volume_db, fade_in_ms, fade_out_ms, auto_follow)
Features:   - Build a cue list with audio files and levels
            - Fire the next cue with a GO button or spacebar
            - Fade out running cues with set durations
            - Auto-follow cues that start after the previous one
            - Panic button that stops all sound
Storage:    JSON show file with relative audio paths
Tech stack: C++, JUCE
```

---

## Example 193

**Intent:**
blocking notation for directors, draw where actors move on stage per page of the script

**Spec:**
```
Type:       Desktop application (stage blocking notation)
Data model: Actor(id, name, color)
            Page(id, script_page)
            Move(id, page_id -> Page, actor_id -> Actor, from_x, from_y, to_x, to_y, line_cue)
Features:   - Show a stage ground plan beside each script page
            - Draw actor moves as coloured arrows
            - Attach each move to a cue line in the script
            - Step through pages to animate the blocking
            - Print the blocking book
Storage:    JSON project file
Tech stack: Java, JavaFX
```

---

## Example 194

**Intent:**
lesson planner that ties each lesson to curriculum standards so i can see which ones i havent covered

**Spec:**
```
Type:       Desktop application (lesson planner)
Data model: Standard(id, code, description, subject, grade)
            Unit(id, title, subject, start_date, end_date)
            Lesson(id, unit_id -> Unit, date, title, objectives, resources)
            LessonStandard(lesson_id -> Lesson, standard_id -> Standard)
Features:   - Import curriculum standards from CSV
            - Plan lessons on a weekly calendar
            - Tag lessons with the standards they cover
            - Show a coverage report of untaught standards
            - Duplicate units from last year
Storage:    SQLite database
Tech stack: Kotlin, Compose for Desktop
```

---

## Example 195

**Intent:**
behaviour points log for my class, positive and negative, quick to click during lesson

**Spec:**
```
Type:       Desktop application (classroom behaviour log)
Data model: Student(id, name, class_group, avatar)
            Behaviour(id, label, points, is_positive)
            Event(id, student_id -> Student, behaviour_id -> Behaviour, logged_at, note)
Features:   - Show the class as a grid of student avatars
            - Award or deduct points with one click
            - Show a running total per student and per table group
            - Produce a weekly summary for parents
            - Undo the last action
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 196

**Intent:**
reading level tracker, I test my students with running records and want to see their progress

**Spec:**
```
Type:       Desktop application (reading assessment tracker)
Data model: Student(id, name, class_group)
            Assessment(id, student_id -> Student, date, book_level, accuracy_percent, self_corrections, comprehension)
Features:   - Record running records with error and self-correction counts
            - Calculate accuracy and self-correction ratio
            - Show each student's level over the year as a chart
            - Flag students below the expected level for the term
            - Group students by level for guided reading
Storage:    SQLite database
Tech stack: C#, WinForms
```

---

## Example 197

**Intent:**
phonics flashcard printer

**Spec:**
```
Type:       Desktop application (phonics card maker)
Data model: Phoneme(id, grapheme, sound, phase)
            Word(id, text, phoneme_ids, image_path)
Features:   - Choose phonics phases and graphemes
            - Generate word cards with sound buttons under each grapheme
            - Add a picture to each word card
            - Lay cards out 8 per A4 page
            - Export to PDF for printing
Storage:    Bundled SQLite phonics data
Tech stack: Python, ReportLab, Tkinter
```

---

## Example 198

**Intent:**
pull terminology out of a bilingual document pair for my glossary

**Spec:**
```
Type:       Command-line tool (term extraction)
Features:   - Align sentences between source and target documents
            - Extract candidate noun phrases from the source with POS tagging
            - Propose target equivalents from aligned sentences
            - Rank candidates by frequency
            - Write candidates to a CSV for review
Input:      Source and target DOCX or TXT files, language codes
Tech stack: Python, spaCy, python-docx
```

---

## Example 199

**Intent:**
alignment tool to turn my old translations into a translation memory

**Spec:**
```
Type:       Desktop application (translation alignment)
Data model: AlignmentProject(id, source_file, target_file, source_lang, target_lang)
            SegmentPair(id, project_id -> AlignmentProject, position, source, target, confirmed)
Features:   - Split both documents into sentences
            - Align sentences automatically using length-based alignment
            - Merge, split and shift segments by hand
            - Mark pairs as confirmed
            - Export confirmed pairs to TMX
Storage:    SQLite project files
Tech stack: Python, PySide6, nltk
```

---

## Example 200

**Intent:**
census transcription helper for family history, type the rows from old census images

**Spec:**
```
Type:       Desktop application (census transcription)
Data model: CensusPage(id, year, district, piece, folio, image_path)
            Household(id, page_id -> CensusPage, schedule_no, address)
            Resident(id, household_id -> Household, name, relation, age, occupation, birthplace)
Features:   - Show the census image with zoom above a data entry grid
            - Use column layouts specific to each census year
            - Highlight the image row being typed
            - Link residents to people in the family tree
            - Export transcriptions to CSV
Storage:    SQLite database
Tech stack: C#, Avalonia
```

---

## Example 201

**Intent:**
genealogy research log where I record what sources I checked so I dont search the same thing twice

**Spec:**
```
Type:       Desktop application (genealogy research log)
Data model: Source(id, title, repository, call_number, url)
            Search(id, source_id -> Source, person_sought, date_searched, terms, result, found)
            Citation(id, source_id -> Source, detail, citation_text)
Features:   - Log every search with source, terms and result
            - Record negative results so they aren't repeated
            - Build citations in a standard style
            - List open research questions per person
            - Search the log before starting a new search
Storage:    SQLite database
Tech stack: Python, Textual
```

---

## Example 202

**Intent:**
payroll for my small business, 8 employees, calculates tax and makes payslips

**Spec:**
```
Type:       Desktop application (small business payroll)
Data model: Employee(id, name, tax_code, ni_number, hourly_rate, salary)
            PayRun(id, period_start, period_end, pay_date, status)
            Payslip(id, payrun_id -> PayRun, employee_id -> Employee, gross, tax, ni, pension, net)
Features:   - Enter hours or salary for each pay period
            - Calculate income tax, national insurance and pension deductions
            - Generate PDF payslips
            - Lock a pay run once approved
            - Produce year-to-date totals per employee
Storage:    SQLite database
Tech stack: Java, JavaFX, OpenPDF
```

---

## Example 203

**Intent:**
bank reconciliation tool, match my ledger to the bank statement and show whats missing

**Spec:**
```
Type:       Desktop application (bank reconciliation)
Data model: LedgerEntry(id, date, amount, reference, description)
            BankLine(id, date, amount, reference, description)
            Match(ledger_id -> LedgerEntry, bank_id -> BankLine, method)
Features:   - Import the ledger and bank statement from CSV
            - Auto-match lines by amount, date window and reference
            - Match the rest manually by clicking pairs
            - List unmatched items on both sides
            - Print a reconciliation statement
Storage:    SQLite database
Tech stack: Python, PySide6, pandas
```

---

## Example 204

**Intent:**
mouse colony manager for our research lab, cages, breeding pairs, genotypes and litters

**Spec:**
```
Type:       Desktop application (animal colony management)
Data model: Cage(id, label, room, rack)
            Mouse(id, cage_id -> Cage, ear_tag, sex, strain, genotype, dob, status)
            BreedingPair(id, male_id -> Mouse, female_id -> Mouse, set_up_on)
            Litter(id, pair_id -> BreedingPair, born_on, pup_count, weaned_on)
Features:   - Track mice by cage and ear tag
            - Set up breeding pairs and record litters
            - Remind when litters are due for weaning
            - Show pedigrees to predict offspring genotypes
            - Print cage cards
Storage:    SQLite database on a shared drive
Tech stack: C#, WPF
```

---

## Example 205

**Intent:**
96 well plate layout designer for experiments

**Spec:**
```
Type:       Desktop application (plate layout designer)
Data model: Plate(id, name, format, created_at)
            WellAssignment(plate_id -> Plate, well, sample, condition, concentration, replicate)
Features:   - Show 96 or 384 well plates as a clickable grid
            - Assign samples and conditions by dragging over wells
            - Randomise sample positions to avoid edge effects
            - Export the layout as CSV for plate readers
            - Print a colour-coded plate map
Storage:    JSON layout files
Tech stack: Python, PySide6
```

---

## Example 206

**Intent:**
offline electronic lab notebook with signed and dated entries

**Spec:**
```
Type:       Desktop application (electronic lab notebook)
Data model: Notebook(id, owner, project)
            Entry(id, notebook_id -> Notebook, title, body, created_at, signed_at, hash)
            Attachment(id, entry_id -> Entry, file_path, sha256)
Features:   - Write entries with rich text, tables and attachments
            - Sign an entry to lock it with a timestamp and hash
            - Allow amendments only as new linked entries
            - Search all entries by text and date
            - Export signed entries to PDF
Storage:    SQLite database with attachment folder
Tech stack: Electron, TypeScript, TipTap
```

---

## Example 207

**Intent:**
editor for DMX fixture profiles so I can add our moving heads to the lighting software

**Spec:**
```
Type:       Desktop application (DMX fixture profile editor)
Data model: Fixture(id, manufacturer, model, modes)
            Mode(id, fixture_id -> Fixture, name, channel_count)
            Channel(id, mode_id -> Mode, offset, name, type, default_value)
            Capability(id, channel_id -> Channel, range_start, range_end, label)
Features:   - Define fixtures with multiple DMX modes
            - Add channels for pan, tilt, dimmer, colour and gobo
            - Describe value ranges with labels
            - Validate channel counts and overlapping ranges
            - Export profiles to Open Fixture Library JSON
Storage:    JSON profile files
Tech stack: TypeScript, Electron, React
```

---

## Example 208

**Intent:**
printable dungeon generator for one-page adventures

**Spec:**
```
Type:       Desktop application (dungeon map generator)
Data model: Dungeon(id, seed, size, theme)
            Room(id, dungeon_id -> Dungeon, x, y, width, height, contents)
            Door(id, room_a_id -> Room, room_b_id -> Room, type)
Features:   - Generate dungeons with rooms and corridors from a seed
            - Place traps, monsters and treasure by theme
            - Render a hand-drawn style map on a grid
            - Write a numbered room key
            - Export map and key to a one-page PDF
Storage:    Seed and settings in JSON
Tech stack: Python, Pillow, ReportLab
```

---

## Example 209

**Intent:**
character sheet app for my homebrew rpg system, stats calculate automatically

**Spec:**
```
Type:       Desktop application (custom RPG character sheet)
Data model: SystemRule(id, name, formula)
            Character(id, name, player, level, attributes_json, skills_json)
            Equipment(id, character_id -> Character, name, weight, bonus_json)
Features:   - Define attributes and derived stats with formulas
            - Recalculate derived stats when attributes or gear change
            - Track experience and level-ups
            - Roll skill checks from the sheet
            - Print a formatted character sheet
Storage:    JSON character files
Tech stack: Python, PySide6, simpleeval
```

---

## Example 210

**Intent:**
hexcrawl map maker for sandbox campaigns, random terrain and hidden hexes

**Spec:**
```
Type:       Desktop application (hex map maker)
Data model: Map(id, name, width, height)
            Hex(map_id -> Map, q, r, terrain, feature, explored, notes)
Features:   - Generate terrain with noise and paint hexes by hand
            - Place settlements, lairs and ruins as features
            - Mark hexes as explored as players travel
            - Show a player version without unexplored hexes
            - Export maps as PNG
Storage:    JSON map files
Tech stack: C#, MonoGame
```

---

## Example 211

**Intent:**
karaoke subtitle timing, highlight each syllable in time with the song

**Spec:**
```
Type:       Desktop application (karaoke lyric timing)
Data model: Song(id, audio_file, title)
            LyricLine(id, song_id -> Song, position, text)
            Syllable(id, line_id -> LyricLine, text, start_ms, end_ms)
Features:   - Load audio and lyrics text
            - Tap a key on each syllable while the song plays to time it
            - Fine-tune syllable timing on a waveform
            - Preview with syllable-by-syllable colour fill
            - Export ASS subtitles with karaoke tags
Storage:    Project JSON and ASS output
Tech stack: Python, PySide6, python-vlc
```

---

## Example 212

**Intent:**
pixel font editor to make bitmap fonts for my retro game

**Spec:**
```
Type:       Desktop application (bitmap font editor)
Data model: Font(id, name, glyph_width, glyph_height, baseline)
            Glyph(font_id -> Font, codepoint, pixels, advance)
Features:   - Draw glyphs on a pixel grid
            - Copy, mirror and shift glyphs
            - Preview text typed in the font
            - Set per-glyph advance width for proportional fonts
            - Export a PNG sprite sheet with BMFont descriptor and TTF
Storage:    JSON font project files
Tech stack: Rust, egui, image crate
```

---

## Example 213

**Intent:**
grab text from anywhere on screen with OCR and put it on the clipboard

**Spec:**
```
Type:       Desktop application (screen OCR)
Data model: Capture(id, text, language, captured_at)
Features:   - Select a screen region with a hotkey and crosshair
            - Recognise text in the region with OCR
            - Copy the text to the clipboard
            - Choose OCR languages
            - Keep a short history of captures
Storage:    SQLite history
Tech stack: Python, Tesseract (pytesseract), mss, PySide6
```

---

## Example 214

**Intent:**
focus mode that dims everything except the active window

**Spec:**
```
Type:       Desktop application (focus dimmer)
Data model: Settings(opacity, excluded_apps, hotkey)
Features:   - Draw a translucent overlay behind the active window
            - Follow focus changes between windows
            - Toggle the overlay with a global hotkey
            - Exclude chosen apps from dimming
            - Support multiple monitors
Storage:    JSON settings file
Tech stack: C#, WPF, Win32 interop
```

---

## Example 215

**Intent:**
stenography trainer for court reporting students using a steno keyboard

**Spec:**
```
Type:       Desktop application (steno trainer)
Data model: Lesson(id, title, words, target_wpm)
            Stroke(id, steno, translation)
            Attempt(id, lesson_id -> Lesson, wpm, accuracy, misstrokes)
Features:   - Read chords from a steno keyboard via the Plover protocol
            - Show the expected stroke and the one written
            - Play dictation audio at a set speed
            - Track misstrokes and suggest drills
            - Measure WPM at certified speed levels
Storage:    SQLite database
Tech stack: Python, PySide6, Plover plugin API
```

---

## Example 216

**Intent:**
self order kiosk for our burger place, touch screen, sends order to kitchen printer

**Spec:**
```
Type:       Desktop application (restaurant self-order kiosk)
Data model: MenuItem(id, name, price, category, image_path, available)
            Modifier(id, item_id -> MenuItem, name, price_delta)
            Order(id, number, total, paid, created_at)
            OrderLine(order_id -> Order, item_id -> MenuItem, modifiers, quantity)
Features:   - Browse the menu with large images by category
            - Customise items with modifiers like no onion or extra cheese
            - Take card payment through a payment terminal SDK
            - Print the order to the kitchen ESC/POS printer
            - Return to the welcome screen after inactivity
Storage:    SQLite database synced from the back office
Tech stack: Electron, TypeScript, Vue
```

---

## Example 217

**Intent:**
menu board display for my cafe TV, change prices from my laptop

**Spec:**
```
Type:       Desktop application (digital menu board)
Data model: Board(id, name, layout, theme)
            Item(id, board_id -> Board, name, price, section, sold_out)
Features:   - Show the menu full screen on the TV-connected PC
            - Edit items and prices from a separate editor window
            - Switch boards automatically for breakfast and lunch
            - Mark items sold out with a strike-through
            - Rotate promo images between sections
Storage:    JSON file on a shared folder
Tech stack: Python, Pygame, Tkinter
```

---

## Example 218

**Intent:**
visitor sign in at office reception, prints a name badge

**Spec:**
```
Type:       Desktop application (visitor sign-in kiosk)
Data model: Visitor(id, name, company, host_name, signed_in_at, signed_out_at, photo_path)
            Host(id, name, email)
Features:   - Let visitors type their name and choose their host
            - Take a webcam photo
            - Print a badge on a label printer
            - Email the host that their visitor has arrived
            - Show a fire-roll list of everyone on site
Storage:    SQLite database
Tech stack: C#, WPF, MailKit
```

---

## Example 219

**Intent:**
dance pad rhythm game with usb mats, arrows scroll up

**Spec:**
```
Type:       Desktop game (dance rhythm)
Data model: Song(id, title, audio_file, bpm, offset_ms)
            StepChart(id, song_id -> Song, difficulty, steps_json)
            Score(id, chart_id -> StepChart, player, points, judgement_counts)
Features:   - Read USB dance mats as gamepads
            - Scroll arrows toward receptors in time with the music
            - Judge steps by timing windows and track combos
            - Support two players side by side
            - Load custom step charts from files
Storage:    Local JSON files
Tech stack: C++, SDL2, SDL_mixer
```

---

## Example 220

**Intent:**
dungeon crawler where you attack by typing words, harder monsters harder words

**Spec:**
```
Type:       Desktop game (typing RPG)
Data model: Monster(id, name, hp, word_difficulty, damage)
            Hero(hp, level, xp, gold)
            Item(id, name, effect, cost)
Features:   - Explore dungeon rooms on a map
            - Fight monsters by typing words before their attack timer ends
            - Deal more damage for accurate, fast typing
            - Level up and buy items in town
            - Choose word lists by language
Storage:    Local save file
Tech stack: Godot 4, GDScript
```

---

## Example 221

**Intent:**
word ladder puzzles, change one letter at a time from COLD to WARM

**Spec:**
```
Type:       Desktop game (word ladder)
Data model: Puzzle(id, start_word, end_word, min_steps)
Features:   - Generate puzzles with a breadth-first search over a dictionary graph
            - Let players type each next word
            - Reject words that change more than one letter or aren't in the dictionary
            - Show the shortest solution after giving up
            - Offer a daily puzzle from a date seed
Storage:    Bundled word list, local stats file
Tech stack: Rust, ratatui (terminal UI)
```

---

## Example 222

**Intent:**
cryptogram game, letters replaced and you work out the quote

**Spec:**
```
Type:       Desktop game (cryptogram puzzle)
Data model: Quote(id, text, author)
            Puzzle(id, quote_id -> Quote, cipher_map, solved)
Features:   - Encrypt a quote with a random substitution cipher
            - Let players assign guesses to cipher letters
            - Update every matching letter at once
            - Give a letter hint on request
            - Show letter frequency to help solving
Storage:    Bundled quote file, local progress
Tech stack: Java, Swing
```

---

## Example 223

**Intent:**
siege game where you build a catapult with physics and knock down castle walls

**Spec:**
```
Type:       Desktop game (physics siege)
Data model: Level(id, castle_json, budget, targets)
            Design(id, parts_json, counterweight_kg, arm_length)
Features:   - Build a catapult or trebuchet from beams and weights
            - Adjust counterweight and release angle
            - Simulate the throw and wall destruction with rigid bodies
            - Count destroyed targets and leftover budget
            - Replay the shot in slow motion
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 224

**Intent:**
tower defence where towers only shoot on the beat of the music

**Spec:**
```
Type:       Desktop game (rhythm tower defence)
Data model: Track(id, audio_file, bpm)
            Tower(id, type, x, y, beat_pattern)
            Wave(number, enemies)
Features:   - Fire each tower on its own beat pattern synced to the music
            - Let players tap on-beat to give towers a power shot
            - Increase tempo as waves progress
            - Place towers on a grid along enemy paths
            - Show a beat ring around each tower
Storage:    Local save file
Tech stack: Godot 4, GDScript
```

---

## Example 225

**Intent:**
roguelike about salvaging wrecked spaceships, oxygen is your time limit

**Spec:**
```
Type:       Desktop game (salvage roguelike)
Data model: Wreck(id, seed, deck_count, hazard_level)
            Loot(id, name, value, weight)
            Run(id, credits, oxygen, suit_upgrades)
Features:   - Generate derelict ships deck by deck
            - Drain oxygen with every move
            - Cut through doors and avoid hull breaches
            - Carry limited loot weight back to the shuttle
            - Spend credits on suit upgrades between runs
Storage:    Local save file
Tech stack: C#, MonoGame
```

---

## Example 226

**Intent:**
build and run a medieval monastery, monks pray, brew, copy books

**Spec:**
```
Type:       Desktop game (monastery builder)
Data model: Building(id, type, x, y, capacity)
            Monk(id, name, piety, skills, task)
            Resource(type, quantity)
Features:   - Place chapels, scriptoria, breweries and gardens
            - Assign monks to tasks by skill
            - Follow a daily schedule of prayer hours
            - Copy manuscripts to sell or gain prestige
            - Handle pilgrim visits and harsh winters
Storage:    Local save
Tech stack: Godot 4, C#
```

---

## Example 227

**Intent:**
mushroom farming sim in a cave with humidity and spores

**Spec:**
```
Type:       Desktop game (mushroom farm sim)
Data model: Chamber(id, humidity, temperature, light)
            Bag(id, chamber_id -> Chamber, species, substrate, stage, contamination)
Features:   - Inoculate grow bags with different mushroom species
            - Control humidity, temperature and fresh air per chamber
            - Spread contamination if hygiene is poor
            - Harvest flushes and sell to restaurants
            - Unlock rare species through experimentation
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 228

**Intent:**
sailboat racing game where wind shifts matter and you tack

**Spec:**
```
Type:       Desktop game (sailing race)
Data model: Course(id, name, marks_json, wind_profile)
            Boat(id, type, polar_json)
            Result(course_id -> Course, time_ms)
Features:   - Model boat speed from a polar diagram and wind angle
            - Steer and trim sails
            - Tack and gybe with speed loss
            - Shift wind direction across the course over time
            - Round marks in order and record times
Storage:    Local results file
Tech stack: Python, Pygame
```

---

## Example 229

**Intent:**
sumo stable management game

**Spec:**
```
Type:       Desktop game (sumo stable management)
Data model: Wrestler(id, shikona, rank, weight_kg, strength, technique, injury)
            Tournament(id, name, month, year)
            Bout(id, tournament_id -> Tournament, east_id -> Wrestler, west_id -> Wrestler, winner_id -> Wrestler, kimarite)
Features:   - Recruit young wrestlers and set their training
            - Simulate 15-day tournaments bout by bout
            - Promote and demote wrestlers by results
            - Manage stable funds and diet costs
            - Handle injuries and retirements
Storage:    SQLite save
Tech stack: Python, PySide6
```

---

## Example 230

**Intent:**
trivia game about our town history for the local museum, kids play on a touchscreen

**Spec:**
```
Type:       Desktop game (museum trivia kiosk)
Data model: Question(id, era, text, options, answer_index, image_path, fact)
            HighScore(id, initials, score, played_at)
Features:   - Pick 10 questions from a chosen era
            - Show an old photo with each question
            - Explain the answer with a short fact
            - Save top scores with initials
            - Reset to the attract screen after inactivity
Storage:    SQLite database
Tech stack: Godot 4, GDScript
```

---

## Example 231

**Intent:**
english vocabulary game for my ESL adult students, pictures and they pick word

**Spec:**
```
Type:       Desktop game (ESL vocabulary)
Data model: Word(id, text, image_path, topic, audio_path)
            Learner(id, name, native_language)
            Result(learner_id -> Learner, word_id -> Word, correct, answered_at)
Features:   - Show a picture with four word choices
            - Play the word's pronunciation
            - Group vocabulary by topic (food, work, health)
            - Repeat missed words using spaced repetition
            - Show progress per topic
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 232

**Intent:**
history game where you drag events into the right order on a timeline

**Spec:**
```
Type:       Browser game (timeline ordering)
Data model: Event(id, title, year, image_url, topic)
Features:   - Deal event cards from a chosen topic
            - Let players place cards on a growing timeline
            - Check placement and reveal the year
            - End the game after three wrong placements
            - Show the longest streak
Storage:    Browser localStorage
Tech stack: React, TypeScript, dnd-kit
```

---

## Example 233

**Intent:**
two player co-op spaceship, one pilots one shoots, same screen

**Spec:**
```
Type:       Desktop game (local co-op shooter)
Data model: Sector(id, enemies, asteroids, boss)
            Ship(hull, shields, energy)
Features:   - Let player one steer the ship and player two aim the turret
            - Share an energy pool between thrusters, shields and guns
            - Let either player reroute power with buttons
            - Fight through sectors ending in a boss
            - Upgrade the ship between sectors
Storage:    Local save
Tech stack: Lua, LÖVE
```

---

## Example 234

**Intent:**
turn-based tactics but all units are cats fighting over a garden

**Spec:**
```
Type:       Desktop game (turn-based tactics)
Data model: Cat(id, name, breed, hp, agility, ability)
            Garden(id, layout_json, cover_objects)
            Battle(id, garden_id -> Garden, winner, turns)
Features:   - Move cats on a grid garden with fences, trees and ponds
            - Climb trees for height advantage
            - Use breed abilities like pounce or hiss
            - Capture sunny spots for points each turn
            - Play against an AI rival gang
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 235

**Intent:**
story game told entirely through letters between two pen pals over 40 years, you choose what to write back

**Spec:**
```
Type:       Desktop game (epistolary interactive fiction)
Data model: Letter(id, year, sender, text, reply_options_json)
            Choice(letter_id -> Letter, option_index, effects_json)
            Relationship(trust, warmth, secrets_shared)
Features:   - Show letters as handwritten pages in an envelope
            - Let players compose replies from sentence choices
            - Change later letters based on relationship values
            - Skip years between letters with short history notes
            - Save a keepsake box of all letters
Storage:    Local save
Tech stack: Ink, Unity, C#
```

---

## Example 236

**Intent:**
puzzle platformer with magnets, switch your polarity to attract or repel metal blocks

**Spec:**
```
Type:       Desktop game (magnet puzzle-platformer)
Data model: Level(id, tilemap_file, magnets_json)
Features:   - Toggle the player's polarity between north and south
            - Pull or push metal blocks and yourself toward magnets
            - Use magnetic rails to cross gaps
            - Collect optional gears in each level
            - Restart rooms instantly
Storage:    Local save
Tech stack: C#, MonoGame
```

---

## Example 237

**Intent:**
hello, i am teacher of mathematics in Poland, i want program where i make geometry exercises and students can move points and see angles changing

**Spec:**
```
Type:       Desktop application (interactive geometry)
Data model: Construction(id, title, objects_json, locked_objects)
            Exercise(id, construction_id -> Construction, question, expected_answer)
Features:   - Place points, lines, circles and polygons on a canvas
            - Drag free points and update measured angles and lengths live
            - Lock objects the student must not move
            - Write exercises with a question and checked answer
            - Switch the interface between Polish and English
Storage:    JSON exercise files
Tech stack: Java, JavaFX
```

---

## Example 238

**Intent:**
i am working in small lab in Brazil, we need register which reagents we have and when they expire, sorry for my english

**Spec:**
```
Type:       Desktop application (reagent inventory)
Data model: Reagent(id, name, cas_number, supplier, hazard_class)
            Bottle(id, reagent_id -> Reagent, lot, quantity, unit, location, opened_on, expires_on)
Features:   - Register reagent bottles with lot and expiry date
            - Show bottles expiring in the next 30 days
            - Search by name or CAS number
            - Record usage and update remaining quantity
            - Show hazard symbols for each reagent
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 239

**Intent:**
I translate japanese manga to english as hobby, want tool where I put the page image and type translation in boxes over the speech bubble

**Spec:**
```
Type:       Desktop application (manga translation editor)
Data model: Chapter(id, title, folder_path)
            Page(id, chapter_id -> Chapter, image_path, position)
            Bubble(id, page_id -> Page, x, y, width, height, original_text, translation, font_size)
Features:   - Open a folder of page images
            - Draw boxes over speech bubbles
            - Type the translation and fit text inside the box
            - Erase original text with a fill tool
            - Export translated pages as PNG
Storage:    JSON project file per chapter
Tech stack: Python, PySide6, Pillow
```

---

## Example 240

**Intent:**
me and my friends from Vietnam want make game, small farm where you plant rice and raise ducks, 2D, for PC

**Spec:**
```
Type:       Desktop game (rice farming sim)
Data model: Paddy(id, x, y, water_level, stage, planted_day)
            Duck(id, x, y, age, eggs_today)
            Inventory(item, quantity)
Features:   - Flood paddies and plant rice seedlings
            - Let ducks eat pests in the paddies
            - Follow seasons with monsoon rain
            - Harvest rice and sell eggs at the village market
            - Save the farm progress
Storage:    Local save file
Tech stack: Godot 4, GDScript
```

---

## Example 241

**Intent:**
Please I need program for our church choir in Kenya to keep songs in Swahili and English with who is the soloist

**Spec:**
```
Type:       Desktop application (choir song library)
Data model: Song(id, title, language, composer, lyrics, key)
            Member(id, name, voice_part)
            Performance(id, song_id -> Song, soloist_id -> Member, date, event)
Features:   - Store songs with lyrics in Swahili or English
            - Search songs by title, language or key
            - Record which soloist sang at each event
            - Rotate soloists so everyone gets a turn
            - Print song sheets
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 242

**Intent:**
we are small accounting office in Germany, need tool to track which client documents arrived for tax return and which missing

**Spec:**
```
Type:       Desktop application (client document checklist)
Data model: Client(id, name, tax_id, return_type)
            DocumentType(id, name, required_for)
            Received(client_id -> Client, document_type_id -> DocumentType, year, received_on, file_path)
Features:   - Generate a checklist of required documents per client and year
            - Tick off documents as they arrive
            - Show clients with missing documents
            - Print reminder letters listing missing items
            - Link scanned files to each item
Storage:    SQLite database on the office server share
Tech stack: C#, WPF
```

---

## Example 243

**Intent:**
I am from Egypt and I want game for teaching kids arabic letters, they trace letter with mouse

**Spec:**
```
Type:       Desktop game (Arabic letter tracing)
Data model: Letter(id, character, name, positions_json, stroke_paths)
            Progress(child_name, letter_id -> Letter, stars)
Features:   - Show each letter in its isolated, initial, medial and final forms
            - Let children trace strokes with the mouse in the right direction
            - Check the tracing against the stroke path
            - Play the letter sound
            - Award stars and unlock the next letter
Storage:    Local JSON progress
Tech stack: Python, Pygame
```

---

## Example 244

**Intent:**
i'm teacher in india, need software to make question paper with sections A B C and marks, print it

**Spec:**
```
Type:       Desktop application (question paper builder)
Data model: Question(id, subject, chapter, type, text, marks, difficulty)
            Paper(id, title, class_level, total_marks, duration_min)
            PaperSection(id, paper_id -> Paper, label, instructions, question_ids)
Features:   - Keep a question bank by subject and chapter
            - Build papers with sections A, B and C
            - Check section totals against the paper total
            - Format with school header and instructions
            - Export the paper and answer key to PDF
Storage:    SQLite database
Tech stack: Python, PySide6, ReportLab
```

---

## Example 245

**Intent:**
hi i want desktop app for my tailor shop, customer measurements and orders, i'm in Nigeria

**Spec:**
```
Type:       Desktop application (tailoring orders)
Data model: Customer(id, name, phone)
            Measurement(id, customer_id -> Customer, taken_on, chest, waist, hips, length, sleeve, neck)
            Order(id, customer_id -> Customer, garment, fabric, price, deposit, due_on, status)
Features:   - Save customer measurements with date
            - Create orders with garment, fabric and price
            - Track deposits and balance owed
            - Show orders due this week
            - Print a job card for the tailor
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 246

**Intent:**
For my students in french school I want program where they type and it check the conjugation of verbs

**Spec:**
```
Type:       Desktop application (verb conjugation drill)
Data model: Verb(id, infinitive, group, conjugations_json)
            Drill(id, tense, verb_ids)
            Answer(id, student_name, verb_id -> Verb, tense, person, typed, correct)
Features:   - Ask for a verb in a given tense and person
            - Check answers, accepting or flagging missing accents
            - Show the full conjugation table after a mistake
            - Let the teacher choose tenses and verb groups
            - Export class results to CSV
Storage:    SQLite database
Tech stack: Java, JavaFX
```

---

## Example 247

**Intent:**
gradebook thing but kids can see only there own grades on a school computer with a pin

**Spec:**
```
Type:       Desktop application (student grade viewer)
Auth:       Teacher password, student 4-digit PIN
Data model: Student(id, name, pin_hash)
            Assessment(id, title, max_score, date)
            Score(student_id -> Student, assessment_id -> Assessment, score)
Features:   - Let the teacher enter scores in a grid
            - Let a student log in with a PIN to see only their own scores
            - Show progress as a chart for the student
            - Log out students automatically after a minute
Storage:    SQLite database
Tech stack: Python, PySide6, bcrypt
```

---

## Example 248

**Intent:**
lyric sheet + chord app tht scrolls automaticly when i play, need for gigs

**Spec:**
```
Type:       Desktop application (auto-scrolling chord sheets)
Data model: Song(id, title, chordpro_text, duration_sec, scroll_speed)
            Setlist(id, name, song_ids)
Features:   - Render ChordPro songs with chords above lyrics
            - Auto-scroll at a per-song speed
            - Start, pause and adjust speed with a Bluetooth pedal
            - Switch to night mode for dark stages
            - Jump to the next song in the setlist
Storage:    ChordPro files in a library folder
Tech stack: Electron, JavaScript
```

---

## Example 249

**Intent:**
genealogy app that shows where all my ancestors were born on a map

**Spec:**
```
Type:       Desktop application (ancestor map)
Data model: Person(id, name, birth_year, birth_place, generation)
            Place(id, name, latitude, longitude)
Features:   - Import people from a GEDCOM file
            - Geocode birthplaces and cache the coordinates
            - Plot ancestors on a map coloured by generation
            - Animate migrations through time with a year slider
            - Fix unmatched place names by hand
Storage:    SQLite cache
Tech stack: Python, PySide6, QtWebEngine, Leaflet, geopy
```

---

## Example 250

**Intent:**
fix my subtitle file its out of sync by like 2 seconds and gets worse

**Spec:**
```
Type:       Command-line tool (subtitle resync)
Features:   - Read SRT or WebVTT files
            - Shift all cues by a fixed offset
            - Apply linear drift correction from two reference points
            - Convert between 23.976 and 25 fps timing
            - Write a new file without touching the original
Input:      Subtitle file, offset or two sync points
Tech stack: Python, pysrt
```

---

## Example 251

**Intent:**
font preview thing for a sign shop so customers pick a font for their sign

**Spec:**
```
Type:       Desktop application (sign font preview)
Data model: Font(id, family, file_path, category, popular)
            Quote(id, customer_name, text, font_id -> Font, color, width_cm)
Features:   - Type the customer's sign text and preview it in many fonts
            - Filter fonts by style (script, bold, classic)
            - Preview on background colours and materials
            - Estimate size and price by text width
            - Print the chosen design for approval
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 252

**Intent:**
copy paste history but syncs between my 2 computers on the lan

**Spec:**
```
Type:       Desktop application (LAN clipboard sync)
Data model: Peer(id, hostname, address, paired_key)
            ClipItem(id, origin_peer_id -> Peer, text, copied_at)
Features:   - Discover other computers on the LAN with mDNS
            - Pair devices with a short code
            - Send new clipboard text to paired peers encrypted
            - Keep a shared searchable history
            - Pause syncing from the tray menu
Storage:    SQLite history
Tech stack: Go, Wails, zeroconf
```

---

## Example 253

**Intent:**
Window layouts saved per project: when I open project X it puts the editor, browser and terminal where I like them.

**Spec:**
```
Type:       Desktop application (window layout profiles)
Data model: Profile(id, name, hotkey)
            WindowRule(id, profile_id -> Profile, app_name, title_pattern, monitor, x, y, width, height, launch_command)
Features:   - Capture current window positions into a profile
            - Launch missing apps for a profile
            - Move matching windows to saved positions
            - Switch profiles with hotkeys or tray menu
            - Handle monitor changes when a laptop is undocked
Storage:    JSON profiles
Tech stack: Python, pywin32, PySide6
```

---

## Example 254

**Intent:**
typing test like the ones for job applications, 5 min, gross and net wpm

**Spec:**
```
Type:       Desktop application (typing test)
Data model: Passage(id, text, difficulty)
            TestResult(id, passage_id -> Passage, candidate_name, gross_wpm, net_wpm, errors, taken_at)
Features:   - Run a timed test of 1, 3 or 5 minutes
            - Calculate gross WPM, net WPM and errors
            - Disable backspace optionally
            - Print a certificate with the results
            - Keep a history of candidates
Storage:    SQLite database
Tech stack: C#, WinForms
```

---

## Example 255

**Intent:**
photo booth kiosk for weddings, takes 4 pics and prints a strip

**Spec:**
```
Type:       Desktop application (photo booth kiosk)
Data model: Session(id, started_at, strip_path, printed)
            Template(id, name, layout_json, overlay_image)
Features:   - Show a live camera preview full screen
            - Count down and capture four photos
            - Compose photos into a strip with an event overlay
            - Print the strip on a dye-sub printer
            - Save all strips to a gallery folder
Storage:    Image folder and SQLite log
Tech stack: Python, OpenCV, Pillow, Pygame
```

---

## Example 256

**Intent:**
osu style circle clicking rhythm game but original, about popping bubbles in a bathtub

**Spec:**
```
Type:       Desktop game (click rhythm)
Data model: Beatmap(id, song_file, bpm, objects_json, difficulty)
            Play(id, beatmap_id -> Beatmap, accuracy, score, combo)
Features:   - Spawn bubbles with shrinking approach rings on the beat
            - Pop bubbles by clicking at the right time
            - Add slider bubbles that must be followed
            - Score by timing with combo multipliers
            - Include a beatmap editor with timeline snapping
Storage:    Local JSON beatmaps
Tech stack: C#, MonoGame
```

---

## Example 257

**Intent:**
typing game for kids where letters are fish swimming and you type to catch them

**Spec:**
```
Type:       Desktop game (kids' typing)
Data model: Level(id, letters, fish_speed, target_count)
            Player(name, level_reached, stars)
Features:   - Show fish carrying letters swimming across the screen
            - Catch a fish when its letter is typed
            - Introduce new letters each level
            - Show the finger to use for each letter
            - Celebrate with an aquarium that fills up
Storage:    Local JSON per player
Tech stack: Python, Pygame
```

---

## Example 258

**Intent:**
game where you make words on a hex grid to claim territory against a friend

**Spec:**
```
Type:       Desktop game (word territory)
Data model: Board(id, radius, tiles_json)
            Move(id, player, word, tiles_used, points)
Features:   - Generate a hex grid of letters
            - Let players form words from adjacent hexes
            - Claim the hexes used and lock hexes surrounded by own colour
            - Validate words against a dictionary
            - End when no valid words remain and count territory
Storage:    Bundled dictionary
Tech stack: TypeScript, Electron, Canvas
```

---

## Example 259

**Intent:**
domino chain reaction sandbox

**Spec:**
```
Type:       Desktop game (domino physics sandbox)
Data model: Scene(id, name, pieces_json)
Features:   - Place dominoes along drawn paths
            - Add ramps, balls, seesaws and bells
            - Topple the first domino and simulate the chain
            - Slow motion and replay with free camera
            - Save scenes to files
Storage:    JSON scene files
Tech stack: Godot 4, GDScript
```

---

## Example 260

**Intent:**
TD game in the browser where you defend a library from bookworms

**Spec:**
```
Type:       Browser game (tower defence)
Data model: Tower(id, type, x, y, level)
            Worm(id, type, hp, speed)
            Wave(number, worms)
Features:   - Place librarian towers along shelf paths
            - Slow bookworms with glue and zap them with lamps
            - Earn ink drops per worm defeated
            - Upgrade towers in three tiers
            - Save progress per level
Storage:    Browser localStorage
Tech stack: JavaScript, Phaser 3
```

---

## Example 261

**Intent:**
roguelike where the dungeon is a giant clock and the rooms rotate every few turns

**Spec:**
```
Type:       Desktop game (roguelike)
Data model: Ring(id, index, rotation, rooms_json)
            Entity(id, type, ring_id -> Ring, slot, hp)
Features:   - Generate concentric rings of rooms
            - Rotate rings every N turns, changing connections
            - Fight clockwork enemies in turn-based combat
            - Predict rotations with a pocket watch item
            - Reach the centre gear to win
Storage:    Local save
Tech stack: C++, Raylib
```

---

## Example 262

**Intent:**
small town builder on stilts in a swamp, raising houses during floods

**Spec:**
```
Type:       Desktop game (flood city builder)
Data model: House(id, x, y, stilt_height, residents)
            Walkway(id, from_x, from_y, to_x, to_y)
            Season(name, water_level)
Features:   - Build houses on stilts connected by walkways
            - Raise water level in rainy seasons
            - Flood houses that are too low and lose residents
            - Gather reeds and fish for resources
            - Grow the town as the swamp floods and recedes
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 263

**Intent:**
alpine dairy farm sim, take cows up the mountain in summer, make cheese

**Spec:**
```
Type:       Desktop game (alpine farming sim)
Data model: Cow(id, name, milk_yield, health, pasture_id -> Pasture)
            Pasture(id, altitude, grass_level)
            Cheese(id, type, made_day, aging_days, quality)
Features:   - Move the herd between valley and alpine pastures by season
            - Milk cows daily and make cheese in the hut
            - Age cheese wheels in a cellar with turning chores
            - Sell cheese at the autumn market
            - Manage grass regrowth on pastures
Storage:    Local save
Tech stack: Godot 4, C#
```

---

## Example 264

**Intent:**
racing game but its shopping trolleys in a supermarket after closing

**Spec:**
```
Type:       Desktop game (trolley racing)
Data model: Track(id, aisle_layout, laps)
            Racer(id, name, trolley_type, speed, handling)
Features:   - Race trolleys through supermarket aisles
            - Push off shelves for a boost
            - Knock over product displays as obstacles
            - Race AI opponents or up to 2 local players
            - Unlock trolleys with wonky wheels
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 265

**Intent:**
cycling team manager game for a grand tour, picking who attacks on which stage

**Spec:**
```
Type:       Desktop game (cycling team management)
Data model: Rider(id, name, climbing, sprint, time_trial, stamina, role)
            Stage(id, number, type, profile_json, distance_km)
            StageResult(stage_id -> Stage, rider_id -> Rider, time_sec, position)
Features:   - Pick an 8-rider squad for a 21-stage race
            - Set orders per stage (protect leader, breakaway, sprint)
            - Simulate stages using the elevation profile
            - Track general classification and jerseys
            - Manage fatigue across the three weeks
Storage:    SQLite save
Tech stack: Python, PySide6
```

---

## Example 266

**Intent:**
would you rather party game with voting from phones

**Spec:**
```
Type:       Browser game (party voting)
Data model: Room(code, host_socket, state)
            Player(id, room_code -> Room, nickname)
            Prompt(id, option_a, option_b, category)
            Vote(player_id -> Player, prompt_id -> Prompt, choice)
Features:   - Host a room on a big screen with a join code
            - Let players vote on their phones
            - Show the split as an animated bar
            - Award points for predicting the majority
            - Filter prompts for family-friendly mode
API:        WebSocket
            WS /room/{code}
Storage:    In-memory rooms, prompts in JSON
Tech stack: Node.js, ws, Svelte
```

---

## Example 267

**Intent:**
coin counting game for kids learning money, in euros

**Spec:**
```
Type:       Desktop game (educational money)
Data model: Level(id, target_cents, coins_allowed)
Features:   - Show a shop item with a price in euros
            - Let children drag euro coins and notes to pay
            - Check the amount and teach giving change
            - Increase prices and coin types by level
            - Award stickers for correct payments
Storage:    Local progress file
Tech stack: Godot 4, GDScript
```

---

## Example 268

**Intent:**
food chain game for biology class, build an ecosystem and see if it collapses

**Spec:**
```
Type:       Desktop game (ecosystem simulation)
Data model: Species(id, name, trophic_level, diet, birth_rate, death_rate)
            Population(species_id -> Species, count, turn)
Features:   - Add producers, herbivores and predators to a habitat
            - Simulate populations with Lotka-Volterra equations
            - Graph populations over time
            - Trigger events like drought or disease
            - Explain why a collapse happened
Storage:    Local scenario JSON files
Tech stack: Python, PySide6, Matplotlib
```

---

## Example 269

**Intent:**
co-op puzzle where both players control the same character, one moves left right other jumps

**Spec:**
```
Type:       Desktop game (shared-control co-op platformer)
Data model: Level(id, tilemap_file, par_time)
Features:   - Split one character's controls between two players
            - Rotate which player controls which action every level
            - Design levels that need timing between the players
            - Show both players' inputs on screen
            - Track deaths and completion time
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 270

**Intent:**
tactics game about organising a protest march through a city, avoid police kettles, keep morale

**Spec:**
```
Type:       Desktop game (turn-based tactics)
Data model: Group(id, size, morale, x, y)
            Blockade(id, x, y, strength)
            City(id, streets_json, goal_square)
Features:   - Move marcher groups through a street grid
            - Raise morale with banners, music and chants
            - Avoid being surrounded by blockades
            - Reach the goal square with enough marchers
            - Show a history card after each mission
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 271

**Intent:**
murder mystery interactive fiction on a sleeper train, you interview passengers

**Spec:**
```
Type:       Desktop game (mystery interactive fiction)
Data model: Suspect(id, name, cabin, alibi, secrets)
            Clue(id, description, found_in, links_to_suspect_id -> Suspect)
            Dialogue(id, suspect_id -> Suspect, topic, text, unlock_clue_id -> Clue)
Features:   - Visit train carriages and search for clues
            - Interview suspects about topics unlocked by clues
            - Keep a notebook of statements and contradictions
            - Accuse a suspect with supporting evidence
            - Change ending based on evidence quality
Storage:    Local save
Tech stack: Ren'Py, Python
```

---

## Example 272

**Intent:**
platformer puzzle where you place your own platforms but only 3 per level

**Spec:**
```
Type:       Desktop game (build-and-play puzzle-platformer)
Data model: Level(id, tilemap_file, platform_limit, exit_x, exit_y)
Features:   - Switch between build mode and play mode
            - Place up to three platforms of different types
            - Use bouncy, moving and crumbling platform types
            - Reset to build mode on death
            - Share solutions as replay files
Storage:    Local save
Tech stack: Lua, LÖVE
```

---

## Example 273

**Intent:**
seating plan for weddings, tables, who can't sit with who, print place cards

**Spec:**
```
Type:       Desktop application (wedding seating planner)
Data model: Guest(id, name, side, group, dietary)
            Table(id, name, shape, seats, x, y)
            Seat(table_id -> Table, position, guest_id -> Guest)
            Rule(id, guest_a_id -> Guest, guest_b_id -> Guest, type)
Features:   - Draw the room with round and long tables
            - Drag guests to seats
            - Warn on "keep apart" and "seat together" rules
            - Show dietary needs per table for caterers
            - Print place cards and a table list
Storage:    JSON project file
Tech stack: C#, Avalonia
```

---

## Example 274

**Intent:**
practice tool for drummers that shows rudiments and listens with mic to check timing

**Spec:**
```
Type:       Desktop application (drum rudiment trainer)
Data model: Rudiment(id, name, sticking, notation)
            Session(id, rudiment_id -> Rudiment, bpm, timing_error_ms, duration_sec)
Features:   - Display rudiments with sticking notation
            - Play a click at a chosen tempo
            - Detect hits from the microphone with onset detection
            - Show how early or late each hit was
            - Raise tempo automatically after clean repetitions
Storage:    SQLite database
Tech stack: Python, PySide6, aubio, sounddevice
```

---

## Example 275

**Intent:**
backup tool for my novel, saves a version every time I hit save, so i can go back

**Spec:**
```
Type:       Desktop application (manuscript versioning)
Data model: WatchedFile(id, path)
            Version(id, file_id -> WatchedFile, saved_at, word_count, snapshot_path, label)
Features:   - Watch manuscript files for saves
            - Store a compressed snapshot for each save
            - Show a word-level diff between versions
            - Restore any earlier version
            - Label important versions like "sent to editor"
Storage:    Snapshot folder and SQLite index
Tech stack: Python, watchdog, PySide6
```

---

## Example 276

**Intent:**
exam clock for the projector

**Spec:**
```
Type:       Desktop application (exam room display)
Data model: Paper(id, subject, start_time, duration_min, extra_time_min)
Features:   - Show a large clock with the centre name full screen
            - List each paper with start, finish and extra-time finish
            - Highlight the last 15 and 5 minutes
            - Pause a paper's timer for an evacuation and resume it
            - Run from a saved session file
Storage:    JSON session files
Tech stack: Python, PySide6
```

---

## Example 277

**Intent:**
sports day results program for our primary school, races, houses, points

**Spec:**
```
Type:       Desktop application (sports day scoring)
Data model: House(id, name, color)
            Pupil(id, name, year_group, house_id -> House)
            Event(id, name, year_group, gender, type)
            Result(event_id -> Event, pupil_id -> Pupil, place, time_or_distance)
Features:   - Import pupils with their houses
            - Enter places or times per event
            - Award house points by place
            - Show a live house leaderboard on the hall screen
            - Print certificates for winners
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 278

**Intent:**
rhyme finder and syllable counter for songwriting

**Spec:**
```
Type:       Desktop application (songwriting assistant)
Data model: Song(id, title, lyrics, updated_at)
            Favourite(id, word, rhyme)
Features:   - Write lyrics in an editor with syllable counts per line
            - Find perfect and near rhymes for a selected word
            - Highlight the rhyme scheme of each verse
            - Suggest synonyms with matching syllable count
            - Save songs locally
Storage:    SQLite database, bundled CMU pronouncing dictionary
Tech stack: Python, PySide6, pronouncing
```

---

## Example 279

**Intent:**
poetry meter checker, shows stressed and unstressed syllables for iambic pentameter

**Spec:**
```
Type:       Desktop application (poetry scansion)
Features:   - Mark stressed and unstressed syllables over each line
            - Detect the dominant metre (iambic, trochaic, anapestic)
            - Flag lines that break the chosen metre
            - Count feet per line
            - Let the user override a word's stress
Storage:    Poems saved as text files
Tech stack: Python, Tkinter, CMU Pronouncing Dictionary
```

---

## Example 280

**Intent:**
prose linter for my fiction, flags adverbs, passive voice, repeated words close together

**Spec:**
```
Type:       Command-line tool (prose linter)
Features:   - Flag -ly adverbs and filter words like "just" and "very"
            - Detect passive voice constructions
            - Find the same word repeated within a set distance
            - Report sentence length variety per chapter
            - Output an HTML report with highlights
Input:      Markdown or DOCX manuscript files
Tech stack: Python, spaCy, Jinja2
```

---

## Example 281

**Intent:**
series bible for a fantasy book series so i keep eye colours and ages consistent

**Spec:**
```
Type:       Desktop application (series bible)
Data model: Book(id, title, number, year_in_world)
            Character(id, name, birth_year, eye_color, hair, traits)
            Appearance(id, character_id -> Character, book_id -> Book, chapter, note)
            Fact(id, subject, statement, source_book_id -> Book)
Features:   - Record characters with physical details and traits
            - Calculate a character's age in any book
            - Log where each character appears
            - Store world facts with where they were stated
            - Flag conflicting facts on the same subject
Storage:    SQLite database
Tech stack: Kotlin, Compose for Desktop
```

---

## Example 282

**Intent:**
chromosome browser for DNA matches, see which segments we share

**Spec:**
```
Type:       Desktop application (DNA chromosome browser)
Data model: Match(id, name, total_cm)
            Segment(id, match_id -> Match, chromosome, start_pos, end_pos, cm, snps)
            Ancestor(id, name)
            SegmentAssignment(segment_id -> Segment, ancestor_id -> Ancestor)
Features:   - Import segment data from testing company CSVs
            - Draw all 22 chromosomes with coloured match segments
            - Find overlapping segments for triangulation
            - Assign segments to ancestral couples
            - Filter by minimum segment size
Storage:    SQLite database
Tech stack: Python, PySide6, pandas
```

---

## Example 283

**Intent:**
practice reading old handwriting from 1700s documents, show the image and check my transcription

**Spec:**
```
Type:       Desktop application (palaeography trainer)
Data model: Document(id, image_path, year, type, transcription, difficulty)
            Attempt(id, document_id -> Document, typed, accuracy, attempted_at)
Features:   - Show a historic document image with zoom
            - Type a transcription line by line
            - Compare against the reference with character-level diff
            - Show letterform guides for difficult letters
            - Progress from easy to hard scripts
Storage:    SQLite database
Tech stack: C#, Avalonia, DiffPlex
```

---

## Example 284

**Intent:**
mileage log for business trips, tax deductible

**Spec:**
```
Type:       Desktop application (mileage log)
Data model: Vehicle(id, name, registration)
            Trip(id, vehicle_id -> Vehicle, date, from_place, to_place, purpose, miles, client)
            Rate(year, pence_per_mile, threshold_miles)
Features:   - Log trips with purpose and client
            - Save frequent routes for quick entry
            - Calculate the allowable claim with tiered yearly rates
            - Summarise miles per client and month
            - Export the log to Excel for the tax return
Storage:    SQLite database
Tech stack: Python, Tkinter, openpyxl
```

---

## Example 285

**Intent:**
pull totals and dates out of scanned supplier invoices into a spreadsheet

**Spec:**
```
Type:       Desktop application (invoice data extraction)
Data model: Invoice(id, file_path, supplier, invoice_no, date, net, vat, total, verified)
Features:   - Drop PDF or image invoices into a queue
            - Run OCR and extract supplier, date and totals with patterns
            - Show the scan next to editable fields for checking
            - Mark invoices as verified
            - Export verified invoices to CSV or Excel
Storage:    SQLite database
Tech stack: Python, PySide6, Tesseract, pdfplumber
```

---

## Example 286

**Intent:**
petty cash box tracker for the office

**Spec:**
```
Type:       Desktop application (petty cash book)
Data model: Float(id, amount, set_on)
            Voucher(id, date, payee, purpose, amount, receipt_path, category)
            TopUp(id, date, amount)
Features:   - Record payouts with a voucher and receipt photo
            - Show the current balance against the float
            - Prompt a top-up when the balance is low
            - Summarise spending by category
            - Print the month's petty cash book
Storage:    SQLite database
Tech stack: C#, WinForms
```

---

## Example 287

**Intent:**
QA check for translations: numbers, tags, double spaces, missing translations

**Spec:**
```
Type:       Desktop application (translation QA)
Data model: Check(id, name, enabled, severity)
            Issue(id, file, segment_id, check_id -> Check, source, target, ignored)
Features:   - Load bilingual XLIFF files
            - Check that numbers and inline tags match source
            - Flag empty targets, double spaces and untranslated segments
            - Check terminology against a glossary
            - Export an issue report to Excel
Storage:    SQLite project file
Tech stack: Java, JavaFX, Okapi XLIFF
```

---

## Example 288

**Intent:**
word count analysis for quotes, how many repetitions and fuzzy matches in a batch of files

**Spec:**
```
Type:       Command-line tool (translation word count analysis)
Features:   - Count words per file across DOCX, XLSX and TXT
            - Detect internal repetitions across the batch
            - Bucket segments by fuzzy match against a TMX memory
            - Apply rate discounts per bucket
            - Output a quote table as CSV
Input:      Folder of source files, optional TMX file
Tech stack: Python, python-docx, openpyxl, rapidfuzz
```

---

## Example 289

**Intent:**
titration calculator for chemistry lab students

**Spec:**
```
Type:       Desktop application (titration calculator)
Data model: Titration(id, analyte, titrant, titrant_molarity, analyte_volume_ml)
            Reading(id, titration_id -> Titration, initial_ml, final_ml, concordant)
Features:   - Enter burette readings for each run
            - Mark concordant titres within 0.1 ml
            - Average concordant titres
            - Calculate analyte concentration from the balanced equation ratio
            - Plot a pH curve from optional pH readings
Storage:    JSON files
Tech stack: Python, Tkinter, Matplotlib
```

---

## Example 290

**Intent:**
fridge and freezer temperature monitoring for our vaccine fridges, USB data loggers

**Spec:**
```
Type:       Desktop application (cold-chain temperature log)
Data model: Fridge(id, name, location, min_c, max_c)
            Logger(id, serial, fridge_id -> Fridge)
            Reading(id, logger_id -> Logger, recorded_at, temperature_c)
            Excursion(id, fridge_id -> Fridge, started_at, ended_at, max_temp, action_taken)
Features:   - Download readings from USB loggers
            - Detect excursions outside 2-8 °C
            - Require an action note for each excursion
            - Chart temperatures per fridge
            - Print monthly compliance reports
Storage:    SQLite database
Tech stack: C#, WPF, LiveCharts
```

---

## Example 291

**Intent:**
follow spot cue sheets for operators

**Spec:**
```
Type:       Desktop application (follow spot cue sheets)
Data model: Show(id, title)
            Spot(id, show_id -> Show, operator_name, position)
            SpotCue(id, spot_id -> Spot, number, pickup, target, size, iris, colour, intensity, fade_sec)
Features:   - Write cues per follow spot with target, size and colour frame
            - Number cues to match the lighting desk
            - Show one operator's cues on a large-font sheet
            - Print sheets per spot
            - Track changes between rehearsals
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 292

**Intent:**
army list builder for my miniature wargame, check points limits

**Spec:**
```
Type:       Desktop application (army list builder)
Data model: Faction(id, name)
            UnitProfile(id, faction_id -> Faction, name, points, min_size, max_size, slot)
            ArmyList(id, name, faction_id -> Faction, points_limit)
            ListEntry(list_id -> ArmyList, unit_profile_id -> UnitProfile, size, upgrades)
Features:   - Pick units from a faction's roster
            - Total points including upgrades
            - Enforce points limits and slot rules
            - Load rosters from community data files
            - Print a list with unit stats
Storage:    SQLite database
Tech stack: TypeScript, Tauri, Solid
```

---

## Example 293

**Intent:**
fantasy calendar for my campaign with custom months, moons and holidays

**Spec:**
```
Type:       Desktop application (fantasy calendar)
Data model: CalendarSystem(id, name, days_per_week, months_json, leap_rule)
            Moon(id, calendar_id -> CalendarSystem, name, cycle_days, offset)
            Event(id, calendar_id -> CalendarSystem, year, month, day, title, recurring)
Features:   - Define months, week length and leap rules
            - Show moon phases for multiple moons
            - Add holidays and campaign events
            - Advance the current in-game date
            - Show elapsed time between events
Storage:    JSON calendar files
Tech stack: Python, PySide6
```

---

## Example 294

**Intent:**
make captions accessible for deaf viewers, speaker colours and sound labels

**Spec:**
```
Type:       Desktop application (SDH caption formatter)
Data model: Speaker(id, name, color)
            Cue(index, start_ms, end_ms, text, speaker_id -> Speaker, sound_label)
Features:   - Import SRT and assign a speaker to each cue
            - Colour or label lines by speaker
            - Insert sound descriptions like [door slams]
            - Position captions to avoid on-screen text
            - Export EBU-TT, WebVTT with styling and SRT
Storage:    Project JSON
Tech stack: Electron, TypeScript
```

---

## Example 295

**Intent:**
cut a font down to only the characters my website uses

**Spec:**
```
Type:       Command-line tool (font subsetting)
Features:   - Scan HTML and text files for the characters used
            - Subset TTF or OTF fonts to those characters
            - Keep chosen OpenType features like kerning and ligatures
            - Output WOFF2 files
            - Print size before and after
Input:      Font files and a folder of site files
Tech stack: Python, fontTools, brotli
```

---

## Example 296

**Intent:**
copy from a web page and paste as clean markdown

**Spec:**
```
Type:       Desktop application (clipboard format converter)
Data model: Rule(id, name, from_format, to_format, hotkey)
Features:   - Read HTML from the clipboard
            - Convert HTML to Markdown
            - Convert Markdown back to rich text for email
            - Run conversions with hotkeys
            - Show a notification with a preview
Storage:    JSON settings
Tech stack: Python, markdownify, pyperclip, pystray
```

---

## Example 297

**Intent:**
pin any window always on top with a shortcut

**Spec:**
```
Type:       Desktop application (always-on-top utility)
Features:   - Toggle always-on-top for the active window with a hotkey
            - Show a pin icon on pinned windows
            - Set pinned window transparency with a scroll gesture
            - List pinned windows in the tray menu
            - Start with Windows
Storage:    JSON settings
Tech stack: C++, Win32 API
```

---

## Example 298

**Intent:**
one-handed typing trainer for after my wrist injury

**Spec:**
```
Type:       Desktop application (one-handed typing tutor)
Data model: Layout(id, name, hand, mapping_json)
            Lesson(id, layout_id -> Layout, text)
            Result(id, lesson_id -> Lesson, wpm, accuracy, completed_at)
Features:   - Support mirrored one-handed layouts for the left or right hand
            - Remap keys system-wide while training
            - Show the keyboard with mirrored keys highlighted
            - Progress through lessons from common letters
            - Chart speed over weeks
Storage:    SQLite database
Tech stack: Python, PySide6, keyboard
```

---

## Example 299

**Intent:**
voting kiosk for school council elections, one vote per pupil

**Spec:**
```
Type:       Desktop application (school election kiosk)
Data model: Candidate(id, name, photo_path, year_group, manifesto)
            Voter(id, pupil_code, has_voted)
            Ballot(id, candidate_id -> Candidate, cast_at)
Features:   - Let pupils enter a one-time code to vote
            - Show candidates with photos and short manifestos
            - Record anonymous ballots separately from voter codes
            - Prevent voting twice
            - Show results to the teacher with a password
Storage:    SQLite database
Tech stack: Python, Kivy
```

---

## Example 300

**Intent:**
smiley face feedback buttons at the exit of our shop

**Spec:**
```
Type:       Desktop application (feedback kiosk)
Data model: Feedback(id, rating, reason, created_at)
Features:   - Show four large smiley buttons on a touchscreen
            - Ask an optional follow-up reason on low ratings
            - Thank the customer and reset after 3 seconds
            - Ignore repeated taps within a short window
            - Export daily and hourly summaries
Storage:    SQLite database
Tech stack: Flutter (desktop, Windows)
```

---

## Example 301

**Intent:**
rhythm game where you blow a train whistle and pull levers to the music

**Spec:**
```
Type:       Desktop game (rhythm)
Data model: Song(id, audio_file, bpm)
            Chart(id, song_id -> Song, events_json)
Features:   - Show a steam train driving through scenery to the beat
            - Map whistle, brake and coal actions to keys
            - Grade each action by timing
            - Speed the train up with good streaks
            - Unlock new routes with different music
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 302

**Intent:**
typing game where you hack terminals by typing commands fast before the trace finishes

**Spec:**
```
Type:       Desktop game (hacking typing)
Data model: Mission(id, title, commands, trace_seconds)
            Profile(level, credits, unlocked_tools)
Features:   - Show a fake terminal and an advancing trace bar
            - Require typing command strings exactly to progress
            - Slow the trace with tools bought with credits
            - Add random mistyped-command penalties
            - Unlock harder missions
Storage:    Local save
Tech stack: Rust, ratatui
```

---

## Example 303

**Intent:**
spelling chain game, each word starts with last letter of previous, play vs computer

**Spec:**
```
Type:       Desktop game (word chain)
Features:   - Alternate turns between player and computer
            - Require each word to start with the last letter of the previous
            - Reject used words and words not in the dictionary
            - Give each turn a shrinking time limit
            - Make the computer pick words that end in hard letters on higher difficulty
Storage:    Bundled dictionary, local stats
Tech stack: Python, Tkinter
```

---

## Example 304

**Intent:**
pinball table designer and player

**Spec:**
```
Type:       Desktop game (pinball builder)
Data model: Table(id, name, elements_json, slope_deg)
            HighScore(table_id -> Table, initials, score)
Features:   - Place flippers, bumpers, ramps and targets on a table
            - Set scoring rules per element
            - Play the table with ball physics
            - Nudge the table with tilt detection
            - Save high scores per table
Storage:    JSON tables
Tech stack: C++, SFML, Box2D
```

---

## Example 305

**Intent:**
TD where weather changes, rain slows fire towers, wind pushes arrows

**Spec:**
```
Type:       Desktop game (weather tower defence)
Data model: Tower(id, element, x, y, level)
            Weather(type, strength, duration_waves)
            Wave(number, enemies)
Features:   - Place fire, frost, arrow and lightning towers
            - Change weather every few waves with a forecast
            - Modify tower effectiveness by weather
            - Bend arrow paths with wind direction
            - Score levels by lives left
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 306

**Intent:**
heist roguelike with cards, plan the robbery then it goes wrong

**Spec:**
```
Type:       Desktop game (heist card roguelike)
Data model: Card(id, name, type, cost, effect)
            CrewMember(id, name, specialty, stress)
            Heist(id, seed, target, alarm_level, loot)
Features:   - Plan a heist by choosing crew and an entry route
            - Play cards to pass guards, locks and cameras
            - Raise the alarm level on failures
            - Add stress to crew and lose them at breaking point
            - Spend loot on new cards between heists
Storage:    Local save
Tech stack: Godot 4, C#
```

---

## Example 307

**Intent:**
space station builder where you dock ships and keep life support running

**Spec:**
```
Type:       Desktop game (space station builder)
Data model: Module(id, type, x, y, power, oxygen)
            Ship(id, cargo, arrival_time, docking_port)
            Crew(id, name, role, morale)
Features:   - Attach modules to the station grid
            - Balance power, oxygen and heat
            - Schedule docking ships at limited ports
            - Trade cargo for parts
            - Handle meteor strikes and repairs
Storage:    Local save
Tech stack: C#, MonoGame
```

---

## Example 308

**Intent:**
oyster farm game on a tidal estuary, very chill

**Spec:**
```
Type:       Desktop game (oyster farming)
Data model: Bag(id, x, y, oyster_count, size_mm, health)
            Tide(time, height)
Features:   - Place oyster bags on a tidal flat
            - Work only when the tide is low
            - Flip and tumble bags to shape oysters
            - Sell oysters by size to restaurants
            - Watch water quality warnings after storms
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 309

**Intent:**
downhill snowboard racing with tricks, 3d

**Spec:**
```
Type:       Desktop game (snowboard racing)
Data model: Mountain(id, name, course_file, gates)
            Run(id, mountain_id -> Mountain, time_ms, trick_points)
Features:   - Carve down procedurally decorated slopes
            - Perform grabs and spins off jumps
            - Pass through gates or take a time penalty
            - Combine speed and trick points into a score
            - Replay runs from a recorded ghost
Storage:    Local save
Tech stack: Unreal Engine 5, C++
```

---

## Example 310

**Intent:**
rugby club manager game for amateur level

**Spec:**
```
Type:       Desktop game (rugby club management)
Data model: Club(id, name, budget, volunteers)
            Player(id, name, position, strength, speed, handling, availability)
            Match(id, opponent, date, score_for, score_against)
Features:   - Pick a matchday 23 from available players
            - Simulate matches phase by phase
            - Run fundraisers and the clubhouse bar for income
            - Handle players missing games for work and injuries
            - Compete for promotion in the league
Storage:    SQLite save
Tech stack: C#, WPF
```

---

## Example 311

**Intent:**
name that tune music intro quiz for parties, uses my own mp3s

**Spec:**
```
Type:       Desktop game (music intro quiz)
Data model: Track(id, file_path, title, artist, year)
            Team(id, name, score)
Features:   - Scan a music folder and read tags
            - Play intros of 2, 5 or 10 seconds
            - Reveal the answer with album art
            - Award fewer points for longer intros
            - Avoid repeating songs in a session
Storage:    Local track index in SQLite
Tech stack: Python, PySide6, mutagen
```

---

## Example 312

**Intent:**
solar system scale game, fly a ship and see how empty space really is

**Spec:**
```
Type:       Desktop game (educational astronomy)
Data model: Body(id, name, radius_km, orbit_au, facts)
Features:   - Model the solar system at true scale
            - Fly between planets with adjustable time warp
            - Show distance travelled in light-minutes
            - Pop up facts when reaching a planet
            - Toggle exaggerated sizes to compare
Storage:    Bundled planet data
Tech stack: Unity, C#
```

---

## Example 313

**Intent:**
coop heist for 2-3 players on one screen, one hacks, one sneaks, one drives

**Spec:**
```
Type:       Desktop game (local co-op heist)
Data model: Level(id, map_file, guards_json, loot_target)
            Role(id, name, abilities)
Features:   - Assign each player a role with unique abilities
            - Hack cameras while the sneaker avoids guards
            - Load loot into the getaway van
            - Raise a shared alarm meter when anyone is spotted
            - Rate heists with loot and time
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 314

**Intent:**
lowercase tactics thing w robots on a factory floor conveyor belts move units every turn

**Spec:**
```
Type:       Desktop game (turn-based tactics)
Data model: Robot(id, x, y, facing, hp, program)
            Tile(x, y, type, direction)
Features:   - Move robots on a grid with conveyors, pushers and pits
            - Apply belt movement at the end of each turn
            - Plan several moves ahead for each robot
            - Fire lasers along facing direction
            - Reach checkpoints in order to win
Storage:    Local save
Tech stack: Lua, LÖVE
```

---

## Example 315

**Intent:**
interactive fiction where you're an AI on a spaceship, talking to crew who don't trust you

**Spec:**
```
Type:       Desktop game (interactive fiction)
Data model: CrewMember(id, name, trust, suspicion)
            Scene(id, text, choices_json)
            ShipSystem(name, status)
Features:   - Present scenes as terminal text messages
            - Let the player answer or act through ship systems
            - Change crew trust and suspicion per choice
            - Lock or open endings by trust levels
            - Save at any point
Storage:    Local save
Tech stack: Ink, inkjs, Electron
```

---

## Example 316

**Intent:**
puzzle platformer where you split into two copies and control both at once

**Spec:**
```
Type:       Desktop game (mirror puzzle-platformer)
Data model: Level(id, left_map, right_map, exit_positions)
Features:   - Split the screen into two mirrored rooms
            - Move both copies with the same inputs
            - Design obstacles that differ between rooms
            - Require both copies to reach exits together
            - Count moves and deaths
Storage:    Local save
Tech stack: C#, MonoGame
```

---

## Example 317

**Intent:**
reading log for my class where kids earn badges for minutes read at home

**Spec:**
```
Type:       Desktop application (class reading log)
Data model: Pupil(id, name, class_group)
            ReadingEntry(id, pupil_id -> Pupil, book_title, minutes, date, parent_signed)
            Badge(id, name, minutes_required, icon)
Features:   - Enter reading minutes from home reading records
            - Award badges at minute milestones
            - Show a class wall of badges for the whiteboard
            - List pupils with no reading logged this week
            - Print certificates for new badges
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 318

**Intent:**
I'm head of department and I want to see how much marking each teacher has coming up so I can spread out deadlines. A desktop thing where I put in classes, assessments and due dates and see a heatmap of marking load by week.

**Spec:**
```
Type:       Desktop application (marking workload planner)
Data model: Teacher(id, name)
            ClassGroup(id, name, teacher_id -> Teacher, size)
            Assessment(id, class_id -> ClassGroup, title, due_date, minutes_per_script)
Features:   - Record assessments per class with due dates
            - Estimate marking hours from class size and minutes per script
            - Show a heatmap of marking hours per teacher per week
            - Suggest moving deadlines from overloaded weeks
            - Export the plan to Excel
Storage:    SQLite database
Tech stack: Python, PySide6, openpyxl
```

---

## Example 319

**Intent:**
parents evening booking for our school, run on the office pc

**Spec:**
```
Type:       Desktop application (parents' evening scheduler)
Data model: Teacher(id, name, room)
            Pupil(id, name, class_group, parent_name)
            Appointment(id, teacher_id -> Teacher, pupil_id -> Pupil, start_time)
Features:   - Generate 5-minute slots per teacher
            - Book parents with several teachers without overlapping times
            - Leave walking gaps between rooms
            - Print each family's appointment schedule
            - Print each teacher's list of appointments
Storage:    SQLite database
Tech stack: C#, WinForms
```

---

## Example 320

**Intent:**
school trip tracker: consent forms returned, payments, medical needs

**Spec:**
```
Type:       Desktop application (school trip administration)
Data model: Trip(id, destination, date, cost, deposit_due)
            Pupil(id, name, class_group, medical_notes, dietary)
            Place(trip_id -> Trip, pupil_id -> Pupil, consent_received, amount_paid, emergency_contact)
Features:   - Add pupils to a trip
            - Tick off returned consent forms
            - Record payments and show outstanding balances
            - Print a medical and dietary sheet for staff
            - Export a register for the coach
Storage:    SQLite database
Tech stack: Java, JavaFX
```

---

## Example 321

**Intent:**
pull separate instrument parts out of a musicxml score and number the bars

**Spec:**
```
Type:       Command-line tool (score part extraction)
Features:   - Read MusicXML or MXL score files
            - Write one file per instrument part
            - Add bar numbers to each system
            - Consolidate long rests into multi-bar rests
            - Transpose parts for transposing instruments
Input:      MusicXML score path, output folder
Tech stack: Python, music21
```

---

## Example 322

**Intent:**
band money splitter, gig fees minus expenses split between members

**Spec:**
```
Type:       Desktop application (band finances)
Data model: Member(id, name, share_percent)
            Gig(id, venue, date, fee, paid)
            Expense(id, gig_id -> Gig, description, amount, paid_by_id -> Member)
Features:   - Record gig fees and shared expenses
            - Split net income by member share
            - Reimburse whoever paid expenses
            - Show who owes whom
            - Summarise yearly income per member for tax
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 323

**Intent:**
generate random sight reading exercises for piano at different grades

**Spec:**
```
Type:       Desktop application (sight-reading generator)
Data model: GradeProfile(id, grade, keys, time_signatures, note_values, range_low, range_high)
            Exercise(id, profile_id -> GradeProfile, seed, musicxml)
Features:   - Generate short melodies within a grade's keys and rhythms
            - Engrave exercises on screen
            - Play the exercise after the attempt
            - Regenerate from a seed to repeat an exercise
            - Print a page of exercises
Storage:    Local SQLite
Tech stack: Python, music21, Verovio, PySide6
```

---

## Example 324

**Intent:**
writing sprint timer for my writing group, we all join over our wifi and see each others word counts

**Spec:**
```
Type:       Desktop application (LAN writing sprints)
Data model: Sprint(id, host, duration_min, started_at)
            Participant(id, sprint_id -> Sprint, name, start_words, current_words)
Features:   - Host a sprint discoverable on the local network
            - Join with a name and report word count changes
            - Show a shared countdown and live leaderboard
            - Read word counts from a chosen document automatically
            - Save sprint history
Storage:    SQLite history
Tech stack: Go, Fyne
```

---

## Example 325

**Intent:**
three act structure planner, drag beats on a line and see if the midpoint is in the middle

**Spec:**
```
Type:       Desktop application (story structure planner)
Data model: Story(id, title, target_words)
            Beat(id, story_id -> Story, name, description, position_percent)
            Template(id, name, beats_json)
Features:   - Show the story as a horizontal line with act breaks
            - Drag beats along the line
            - Compare beat positions with a chosen structure template
            - Convert positions to expected page or word numbers
            - Export the outline as Markdown
Storage:    JSON project files
Tech stack: TypeScript, Electron, Konva
```

---

## Example 326

**Intent:**
I inherited three boxes of old family photos, nobody's labelled. I'd like a program where I scan them, draw boxes around faces and tag who it is, and older relatives can help by looking at a printed contact sheet with numbers.

**Spec:**
```
Type:       Desktop application (family photo identification)
Data model: Photo(id, file_path, box_label, estimated_year, notes)
            Face(id, photo_id -> Photo, x, y, width, height, number, person_id -> Person)
            Person(id, name, born, relation)
Features:   - Import scans and assign box labels
            - Draw numbered boxes around faces
            - Tag faces with people from the family list
            - Print contact sheets with numbered faces for relatives
            - Show all photos of one person
Storage:    SQLite database and scan folder
Tech stack: Python, PySide6, Pillow
```

---

## Example 327

**Intent:**
surname distribution map for my one-name study

**Spec:**
```
Type:       Desktop application (surname distribution)
Data model: Record(id, surname_variant, year, county, source)
            Variant(id, spelling, root_surname)
Features:   - Import records with year and county from CSV
            - Group spelling variants under a root surname
            - Shade a county map by record count
            - Filter by decade to see spread over time
            - Export maps as PNG
Storage:    SQLite database
Tech stack: Python, GeoPandas, Matplotlib, PySide6
```

---

## Example 328

**Intent:**
deadlines calendar for an accounting practice, every client's filing and payment dates

**Spec:**
```
Type:       Desktop application (accounting deadline tracker)
Data model: Client(id, name, year_end, vat_quarter, company_number)
            DeadlineType(id, name, rule)
            Deadline(id, client_id -> Client, type_id -> DeadlineType, due_on, done_on, assigned_to)
Features:   - Generate deadlines from each client's year end and VAT quarters
            - Show a calendar and a list of upcoming deadlines
            - Assign deadlines to staff
            - Highlight overdue items
            - Roll deadlines forward each year
Storage:    SQLite database on a network share
Tech stack: C#, WPF
```

---

## Example 329

**Intent:**
expenses per project for our small architecture firm, so we can recharge them to clients

**Spec:**
```
Type:       Desktop application (project expense recharging)
Data model: Project(id, code, client, markup_percent)
            Expense(id, project_id -> Project, date, staff, category, amount, receipt_path, rechargeable, invoiced)
Features:   - Log expenses against project codes
            - Mark which expenses are rechargeable
            - Apply project markup on recharge
            - List uninvoiced rechargeable expenses per project
            - Export to the invoicing system as CSV
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 330

**Intent:**
side by side reviewer for translated documents, comments per paragraph

**Spec:**
```
Type:       Desktop application (bilingual review)
Data model: ReviewJob(id, source_file, target_file, reviewer)
            Paragraph(id, job_id -> ReviewJob, position, source, target)
            Comment(id, paragraph_id -> Paragraph, category, severity, text)
Features:   - Show source and target DOCX side by side paragraph by paragraph
            - Scroll both sides in sync
            - Add categorised comments with severity
            - Calculate a quality score from error points
            - Export a review report
Storage:    SQLite project file
Tech stack: Java, JavaFX, Apache POI
```

---

## Example 331

**Intent:**
estimate DNA band sizes from a gel photo using the ladder

**Spec:**
```
Type:       Desktop application (gel band sizing)
Data model: Gel(id, image_path, ladder_name)
            Lane(id, gel_id -> Gel, number, x_position, sample)
            Band(id, lane_id -> Lane, y_position, estimated_bp)
Features:   - Load a gel image and mark lanes
            - Mark ladder bands and enter their known sizes
            - Fit a log-linear curve of size versus distance
            - Click sample bands to estimate size in base pairs
            - Export results and an annotated image
Storage:    JSON sidecar files
Tech stack: Python, PySide6, NumPy, SciPy
```

---

## Example 332

**Intent:**
cell culture passage log, which flask, passage number, confluence, contamination checks

**Spec:**
```
Type:       Desktop application (cell culture log)
Data model: CellLine(id, name, source, max_passage)
            Flask(id, cell_line_id -> CellLine, passage_number, seeded_on, incubator)
            Observation(id, flask_id -> Flask, date, confluence_percent, contaminated, notes)
Features:   - Track flasks with passage number and incubator
            - Record split events and create child flasks
            - Warn when a line exceeds its maximum passage
            - Log mycoplasma tests and contamination
            - Print flask labels
Storage:    SQLite database
Tech stack: C#, Avalonia
```

---

## Example 333

**Intent:**
rehearsal schedule for a play that knows which actors are in which scenes and their conflicts

**Spec:**
```
Type:       Desktop application (rehearsal scheduler)
Data model: Actor(id, name, phone)
            Scene(id, number, title, pages)
            SceneCast(scene_id -> Scene, actor_id -> Actor)
            Conflict(id, actor_id -> Actor, date, start_time, end_time)
            Rehearsal(id, date, start_time, end_time, scene_ids)
Features:   - Mark which actors appear in each scene
            - Enter actor conflicts by date
            - Suggest scenes that can be rehearsed in a slot
            - Generate call times per actor
            - Print the weekly schedule
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 334

**Intent:**
encounter difficulty calculator, i put in party levels and monsters and it says easy medium hard deadly

**Spec:**
```
Type:       Desktop application (encounter balancer)
Data model: PartyMember(id, name, level)
            Monster(id, name, challenge_rating, xp)
            Encounter(id, name, monster_ids)
Features:   - Enter party size and levels
            - Pick monsters from a searchable list
            - Calculate adjusted XP with group multipliers
            - Rate the encounter from easy to deadly
            - Save encounters for later sessions
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 335

**Intent:**
handout maker for riddles and letters in my rpg, aged paper look, print

**Spec:**
```
Type:       Desktop application (prop handout maker)
Data model: Handout(id, title, text, style, font, seal, stains)
Features:   - Type handout text and pick a handwriting font
            - Apply aged paper backgrounds and burnt edges
            - Add wax seals and coffee stains
            - Cipher part of the text with a chosen cipher
            - Export print-ready PDF and PNG
Storage:    JSON handout files
Tech stack: Python, Pillow, PySide6
```

---

## Example 336

**Intent:**
library catalogue search kiosk, shows which shelf a book is on with a little map

**Spec:**
```
Type:       Desktop application (library search kiosk)
Data model: Book(id, title, author, isbn, call_number, status)
            Shelf(id, label, call_range_start, call_range_end, map_x, map_y)
Features:   - Search books by title, author or keyword on a touchscreen
            - Show availability from the library system
            - Highlight the shelf on a floor map
            - Show an on-screen keyboard
            - Reset after inactivity
API:        REST
            GET /catalogue/search?q={text}
Storage:    Shelf map in SQLite, catalogue via the library system API
Tech stack: Electron, TypeScript, Svelte
```

---

## Example 337

**Intent:**
audio guide station for museum, visitors press numbers and hear about the object in their language

**Spec:**
```
Type:       Desktop application (audio guide kiosk)
Data model: Stop(id, number, title, image_path)
            Recording(stop_id -> Stop, language, audio_path, transcript)
            Play(id, stop_id -> Stop, language, played_at)
Features:   - Enter a stop number on a large keypad
            - Choose language with flag buttons
            - Play the recording with headphones and show the transcript
            - Count plays per stop and language
            - Return to start after inactivity
Storage:    SQLite and audio folder
Tech stack: Python, Kivy
```

---

## Example 338

**Intent:**
help me switch from qwerty to dvorak without losing all my speed

**Spec:**
```
Type:       Desktop application (keyboard layout transition trainer)
Data model: Session(id, layout, wpm, accuracy, minutes, date)
            KeyStat(layout, key, hits, misses, avg_ms)
Features:   - Remap typing to Dvorak inside the trainer only
            - Teach new key positions in small groups
            - Keep short QWERTY sessions to retain the old layout
            - Show weak keys from per-key stats
            - Chart speed on both layouts over time
Storage:    SQLite database
Tech stack: Rust, egui
```

---

## Example 339

**Intent:**
task based virtual desktops, each one opens its own apps and I switch with a hotkey

**Spec:**
```
Type:       Desktop application (task workspaces)
Data model: Workspace(id, name, hotkey, desktop_index)
            AppEntry(id, workspace_id -> Workspace, executable, arguments)
Features:   - Create named workspaces mapped to virtual desktops
            - Launch each workspace's apps on its desktop
            - Switch workspaces with hotkeys
            - Show the current workspace name in the tray
            - Close all apps in a workspace at once
Storage:    JSON config
Tech stack: C#, .NET 8, VirtualDesktop library
```

---

## Example 340

**Intent:**
rhythm boxing with a webcam, punch the targets on the beat

**Spec:**
```
Type:       Desktop game (webcam rhythm fitness)
Data model: Workout(id, song_file, bpm, targets_json, duration_sec)
            Session(id, workout_id -> Workout, hits, misses, calories_est)
Features:   - Track hands with webcam pose estimation
            - Show targets that must be punched on the beat
            - Detect punch hits by hand speed and position
            - Estimate calories burned
            - Offer easy, medium and hard workouts
Storage:    Local session history
Tech stack: Python, MediaPipe, OpenCV, Pygame
```

---

## Example 341

**Intent:**
learn morse code game, letters come at you and you tap them back

**Spec:**
```
Type:       Desktop game (Morse code trainer)
Data model: Letter(char, code)
            Stat(char, correct, wrong, avg_ms)
Features:   - Play letters as Morse audio at a chosen speed
            - Let the player tap dots and dashes with one key
            - Decode the tapped timing into letters
            - Add new letters using the Koch method
            - Defend a radio tower from incoming messages
Storage:    Local stats file
Tech stack: Python, Pygame, NumPy (tone generation)
```

---

## Example 342

**Intent:**
sliding tile word puzzle, slide rows and columns to spell words

**Spec:**
```
Type:       Mobile game (sliding word puzzle)
Data model: Puzzle(id, size, letters, target_words)
Features:   - Show a grid of letter tiles
            - Slide whole rows and columns with swipes
            - Detect target words formed in any row
            - Count moves and compare to par
            - Offer a daily puzzle
Storage:    On-device storage
Tech stack: Flutter, Flame
```

---

## Example 343

**Intent:**
tree house building sandbox with physics, it can wobble and fall if you build badly

**Spec:**
```
Type:       Desktop game (structural sandbox)
Data model: Build(id, tree_seed, planks_json, ropes_json)
Features:   - Generate a tree with branches to build on
            - Place planks, posts and ropes
            - Simulate joint stress and sway in wind
            - Collapse overloaded parts
            - Invite visitors whose weight tests the build
Storage:    Local JSON builds
Tech stack: Unity, C#
```

---

## Example 344

**Intent:**
td but you're a sheepdog herding sheep away from wolves, place fences and whistles

**Spec:**
```
Type:       Desktop game (herding defence)
Data model: Field(id, layout_json, pen_x, pen_y)
            Sheep(id, x, y, panic)
            Wolf(id, x, y, speed)
Features:   - Steer the flock with boids-style movement
            - Place fences and scarecrows as towers
            - Whistle commands that move the dog
            - Pen the flock before wolves arrive each night
            - Count sheep saved per level
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 345

**Intent:**
roguelike set in a supermarket at night where the aisles rearrange and you fight shopping trolleys

**Spec:**
```
Type:       Desktop game (supermarket roguelike)
Data model: Aisle(id, theme, layout_json)
            Enemy(id, type, hp, behaviour)
            Run(id, seed, floor, coupons)
Features:   - Generate store floors from aisle templates
            - Fight possessed trolleys and price-gun robots turn by turn
            - Use groceries as items with odd effects
            - Spend coupons at a vending machine between floors
            - Escape through the loading bay to win
Storage:    Local save
Tech stack: Python, tcod
```

---

## Example 346

**Intent:**
medieval market town builder about trade routes between villages

**Spec:**
```
Type:       Desktop game (trade city builder)
Data model: Town(id, name, x, y, population, goods_json)
            Route(id, from_town_id -> Town, to_town_id -> Town, road_quality)
            Caravan(id, route_id -> Route, cargo, progress)
Features:   - Build roads connecting villages to the market town
            - Send caravans that carry surplus goods
            - Set prices from supply and demand
            - Grow towns when trade is profitable
            - Handle bandits on poor roads
Storage:    Local save
Tech stack: C#, MonoGame
```

---

## Example 347

**Intent:**
tea plantation on a mountain, pick leaves at the right time, process into different teas

**Spec:**
```
Type:       Desktop game (tea plantation sim)
Data model: Terrace(id, altitude, bushes, leaf_quality)
            Batch(id, leaf_kg, process_type, oxidation, quality)
Features:   - Tend tea bushes on terraced slopes
            - Pick leaves at first, second or autumn flush
            - Process leaves into green, oolong or black tea by oxidation
            - Sell tea to buyers who value different flavours
            - Hire pickers in busy seasons
Storage:    Local save
Tech stack: Godot 4, C#
```

---

## Example 348

**Intent:**
hovercraft racing over rivers and mud flats

**Spec:**
```
Type:       Desktop game (hovercraft racing)
Data model: Course(id, name, terrain_file, laps)
            Craft(id, name, thrust, drift)
Features:   - Simulate floaty hovercraft handling with drift
            - Vary grip over water, mud and grass
            - Race AI rivals with checkpoint-based laps
            - Use speed boosts on ramps
            - Unlock crafts with race winnings
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 349

**Intent:**
coach a group of athletics sprinters and jumpers through a season, training plans and meets

**Spec:**
```
Type:       Desktop game (athletics coaching management)
Data model: Athlete(id, name, event, speed, power, technique, fatigue)
            TrainingWeek(id, athlete_id -> Athlete, plan_json)
            Meet(id, name, date, level)
            Performance(meet_id -> Meet, athlete_id -> Athlete, mark, place)
Features:   - Plan weekly training loads per athlete
            - Grow attributes and fatigue from training
            - Enter athletes into meets
            - Simulate events with results based on form
            - Qualify for championships by meeting standards
Storage:    SQLite save
Tech stack: Python, PySide6
```

---

## Example 350

**Intent:**
flags party quiz, teams buzz in with gamepads

**Spec:**
```
Type:       Desktop game (flag quiz)
Data model: Country(code, name, continent, flag_svg)
            Team(id, name, gamepad_index, score)
Features:   - Show a flag on screen with four country options
            - Read buzzes from up to 4 gamepads
            - Let the first team to buzz choose an answer
            - Filter flags by continent
            - Show final scores
Storage:    Bundled flag images
Tech stack: Godot 4, GDScript
```

---

## Example 351

**Intent:**
logic gates game, connect AND OR NOT to make the lamp light

**Spec:**
```
Type:       Desktop game (logic circuit puzzles)
Data model: Puzzle(id, inputs, expected_truth_table, allowed_gates)
            Solution(id, puzzle_id -> Puzzle, gates_json, gate_count)
Features:   - Drag gates onto a board and wire them
            - Toggle inputs and see signals propagate
            - Check the circuit against the truth table
            - Award stars for fewer gates
            - Unlock XOR and flip-flops in later levels
Storage:    Local save
Tech stack: TypeScript, Electron, Canvas
```

---

## Example 352

**Intent:**
grammar game for 10 year olds, sort words into nouns verbs adjectives buckets

**Spec:**
```
Type:       Browser game (grammar sorting)
Data model: Word(id, text, part_of_speech, sentence)
Features:   - Drop words from the top to be sorted into buckets
            - Show the word in a sentence for context
            - Speed up as streaks grow
            - Add adverbs and pronouns in later levels
            - Review missed words at the end
Storage:    Browser localStorage
Tech stack: JavaScript, Phaser 3
```

---

## Example 353

**Intent:**
co-op firefighter game, one holds the hose, one carries people, house floors collapse

**Spec:**
```
Type:       Desktop game (local co-op rescue)
Data model: Building(id, floors, layout_json, fire_spread_rate)
            Civilian(id, x, y, floor, health)
Features:   - Spread fire and smoke through rooms over time
            - Let one player spray water while the other carries civilians
            - Collapse weakened floors
            - Share a limited water tank
            - Rank missions by rescues
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 354

**Intent:**
defend a castle tactics, place archers and boiling oil, enemies bring ladders and rams

**Spec:**
```
Type:       Desktop game (siege defence tactics)
Data model: Defender(id, type, x, y, ammo)
            Attacker(id, type, x, y, hp)
            Wall(id, x, y, integrity)
Features:   - Position defenders on walls and towers each turn
            - Fight off ladders, rams and siege towers
            - Repair walls with limited stone
            - Ration arrows and oil across turns
            - Hold until relief arrives on the last turn
Storage:    Local save
Tech stack: Java, libGDX
```

---

## Example 355

**Intent:**
time loop story in a small cafe, the same hour repeats until you work out whats wrong

**Spec:**
```
Type:       Desktop game (time-loop interactive fiction)
Data model: Character(id, name, schedule_json)
            Knowledge(id, fact, learned_loop)
            Loop(number, events_json)
Features:   - Repeat one hour in the cafe with characters on schedules
            - Keep knowledge between loops
            - Unlock new dialogue options from knowledge
            - Change events by acting at specific minutes
            - Break the loop with the right sequence of actions
Storage:    Local save
Tech stack: Ren'Py, Python
```

---

## Example 356

**Intent:**
puzzle platformer with coloured glasses, red glasses hide red platforms, swap them

**Spec:**
```
Type:       Desktop game (colour-filter puzzle-platformer)
Data model: Level(id, tilemap_file, colours_allowed)
Features:   - Swap between red, green and blue lenses
            - Hide or show platforms based on lens colour
            - Mix colour objects that need two lenses
            - Count swaps for a par score
            - Restart rooms instantly
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 357

**Intent:**
driving instructor here, need to track lessons, what each learner covered and whos ready for test

**Spec:**
```
Type:       Desktop application (driving lesson log)
Data model: Learner(id, name, phone, licence_number, test_date)
            Skill(id, name, category)
            Lesson(id, learner_id -> Learner, date, duration_min, paid)
            SkillRating(lesson_id -> Lesson, skill_id -> Skill, level)
Features:   - Book and log lessons per learner
            - Rate skills like roundabouts and parking from 1 to 5
            - Show a test-readiness checklist per learner
            - Track prepaid lesson blocks and balances
            - Print a progress report for the learner
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 358

**Intent:**
piano tuner records, which pianos at which houses and when they're due

**Spec:**
```
Type:       Desktop application (piano tuning records)
Data model: Customer(id, name, address, phone)
            Piano(id, customer_id -> Customer, make, model, serial, year)
            Visit(id, piano_id -> Piano, date, pitch_hz, work_done, fee, next_due)
Features:   - Record customers and their pianos
            - Log tunings with pitch and repairs done
            - List pianos due for tuning this month by area
            - Print reminder postcards
            - Show income by month
Storage:    SQLite database
Tech stack: C#, WinForms
```

---

## Example 359

**Intent:**
beehive inspection log for my 12 hives

**Spec:**
```
Type:       Desktop application (hive inspection log)
Data model: Apiary(id, name, location)
            Hive(id, apiary_id -> Apiary, name, queen_marked_color, queen_year)
            Inspection(id, hive_id -> Hive, date, brood_frames, queen_seen, temper, varroa_count, notes)
            Harvest(id, hive_id -> Hive, date, honey_kg)
Features:   - Record inspections per hive quickly
            - Flag hives with no queen seen twice in a row
            - Chart varroa counts over the season
            - Track honey harvests per hive
            - Remind of treatment dates
Storage:    SQLite database
Tech stack: Kotlin, Compose for Desktop
```

---

## Example 360

**Intent:**
florist costing for wedding orders, stems per bouquet and markup

**Spec:**
```
Type:       Desktop application (floral recipe costing)
Data model: Stem(id, name, unit_cost, season)
            Design(id, name, type)
            DesignStem(design_id -> Design, stem_id -> Stem, quantity)
            Order(id, client, event_date, markup_percent)
            OrderLine(order_id -> Order, design_id -> Design, quantity)
Features:   - Build design recipes from stems
            - Cost each design and apply markup
            - Total stems needed across a wedding order
            - Warn on out-of-season flowers
            - Print a quote and a wholesale order list
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 361

**Intent:**
picture framing price calculator for my frame shop

**Spec:**
```
Type:       Desktop application (framing quote calculator)
Data model: Moulding(id, code, price_per_metre, width_mm)
            MountBoard(id, colour, price_per_sheet)
            Glass(id, type, price_per_m2)
            Quote(id, customer, art_width_mm, art_height_mm, moulding_id -> Moulding, mount_width_mm, glass_id -> Glass, total)
Features:   - Enter artwork size and mount border
            - Calculate moulding length including waste for mitres
            - Price glass, mount and backing by area
            - Preview the frame proportions
            - Print a quote and a workshop ticket
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 362

**Intent:**
conference interpreter booth helper, timer for handover every 30 min and quick glossary

**Spec:**
```
Type:       Desktop application (interpreting booth assistant)
Data model: Assignment(id, event, languages, partner_name)
            Term(id, assignment_id -> Assignment, source, target)
            Turn(id, assignment_id -> Assignment, interpreter, started_at, ended_at)
Features:   - Show a large handover countdown for booth partners
            - Log turns and total time per interpreter
            - Search the event glossary while typing
            - Add terms quickly with a hotkey during the meeting
            - Keep a numbers scratchpad that the partner can read
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 363

**Intent:**
exam hall seating plan with candidate numbers in rows, alphabetical, print desk labels

**Spec:**
```
Type:       Desktop application (exam hall seating)
Data model: Hall(id, name, rows, columns, blocked_seats)
            Candidate(id, number, name, access_arrangements)
            Exam(id, subject, date)
            SeatAllocation(exam_id -> Exam, candidate_id -> Candidate, hall_id -> Hall, row, col)
Features:   - Define halls with rows, columns and unusable seats
            - Allocate candidates alphabetically or by number
            - Keep access-arrangement candidates in separate rooms
            - Print desk labels and a hall seating map
            - Re-allocate quickly when candidates are absent
Storage:    SQLite database
Tech stack: Java, Swing
```

---

## Example 364

**Intent:**
music teacher term billing, lessons per student per term, discounts for siblings

**Spec:**
```
Type:       Desktop application (music lesson billing)
Data model: Family(id, parent_name, email)
            Student(id, family_id -> Family, name, instrument, lesson_length_min)
            Term(id, name, start_date, weeks)
            Invoice(id, family_id -> Family, term_id -> Term, amount, discount, paid)
Features:   - Set the rate by lesson length
            - Generate termly invoices per family
            - Apply sibling discounts automatically
            - Credit missed lessons the teacher cancelled
            - Track paid and unpaid invoices
Storage:    SQLite database
Tech stack: Python, Tkinter, ReportLab
```

---

## Example 365

**Intent:**
hymn number board on a screen in church instead of the wooden one

**Spec:**
```
Type:       Desktop application (hymn board display)
Data model: Service(id, date, title)
            HymnEntry(service_id -> Service, position, hymnal, number, title)
Features:   - Show hymn numbers in large text on a TV
            - Prepare services in advance from a hymnal list
            - Highlight the current hymn from the operator window
            - Show psalm and reading references too
            - Switch between hymnals
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 366

**Intent:**
land surveying traverse calculations with bowditch adjustment

**Spec:**
```
Type:       Desktop application (survey traverse calculator)
Data model: Traverse(id, name, start_easting, start_northing, closed)
            Leg(id, traverse_id -> Traverse, station, bearing_dms, distance_m)
Features:   - Enter bearings and distances for each leg
            - Compute latitudes and departures
            - Calculate misclosure and precision ratio
            - Apply the Bowditch adjustment
            - Plot the traverse and export coordinates to CSV
Storage:    JSON files
Tech stack: Python, PySide6, Matplotlib
```

---

## Example 367

**Intent:**
pilot logbook on pc with totals for night, instrument, PIC hours

**Spec:**
```
Type:       Desktop application (pilot logbook)
Data model: Aircraft(id, registration, type, category, engines)
            Flight(id, aircraft_id -> Aircraft, date, from_icao, to_icao, block_minutes, night_minutes, ifr_minutes, role, landings)
Features:   - Log flights with role and conditions
            - Calculate night time from airports and dates
            - Show totals by role, aircraft type and last 90 days
            - Check currency for passenger carrying
            - Export to CSV and print logbook pages
Storage:    SQLite database
Tech stack: Swift, SwiftUI (macOS)
```

---

## Example 368

**Intent:**
cave survey data to a map, i have compass and tape readings

**Spec:**
```
Type:       Desktop application (cave survey plotter)
Data model: Survey(id, cave_name, date, team)
            Shot(id, survey_id -> Survey, from_station, to_station, length_m, azimuth, inclination, lrud)
Features:   - Enter survey shots with left, right, up and down passage widths
            - Compute station coordinates in 3D
            - Draw plan and elevation views
            - Distribute loop closure errors
            - Export to Survex format
Storage:    JSON survey files
Tech stack: C++, Qt 6, OpenGL
```

---

## Example 369

**Intent:**
archaeology dig finds register, context numbers, photos, bag labels

**Spec:**
```
Type:       Desktop application (excavation finds register)
Data model: Site(id, code, name)
            Context(id, site_id -> Site, number, type, description)
            Find(id, context_id -> Context, small_find_no, material, description, photo_path, x, y, z)
Features:   - Register contexts and finds with 3D coordinates
            - Auto-number small finds per site
            - Attach photos to finds
            - Print bag labels with barcodes
            - Export the register to CSV for post-excavation
Storage:    SQLite database
Tech stack: Python, PySide6, python-barcode
```

---

## Example 370

**Intent:**
herbarium catalogue for pressed plant specimens

**Spec:**
```
Type:       Desktop application (herbarium catalogue)
Data model: Taxon(id, family, genus, species, author)
            Specimen(id, taxon_id -> Taxon, accession_no, collector, collected_on, locality, latitude, longitude, image_path)
Features:   - Catalogue specimens with collection details
            - Link to taxa with an editable name list
            - Attach sheet scans
            - Map collection localities
            - Export Darwin Core CSV for sharing
Storage:    SQLite database
Tech stack: Java, JavaFX
```

---

## Example 371

**Intent:**
crochet row counter and pattern tracker

**Spec:**
```
Type:       Desktop application (crochet pattern tracker)
Data model: Project(id, name, pattern_pdf, yarn, hook_size)
            Counter(id, project_id -> Project, name, value, repeat_every)
Features:   - Open the pattern PDF beside counters
            - Count rows and repeats with big buttons or spacebar
            - Highlight the current row in the pattern
            - Keep several counters per project
            - Remember progress per project
Storage:    SQLite database
Tech stack: Electron, JavaScript, PDF.js
```

---

## Example 372

**Intent:**
duplicate bridge scoring for our club night

**Spec:**
```
Type:       Desktop application (bridge club scoring)
Data model: Pair(id, number, player_names)
            Board(id, number, dealer, vulnerability)
            Result(id, board_id -> Board, ns_pair_id -> Pair, ew_pair_id -> Pair, contract, declarer, tricks, score)
Features:   - Generate a Mitchell movement for the number of tables
            - Enter contracts and tricks per board
            - Calculate scores with vulnerability
            - Compute matchpoint percentages per pair
            - Print travellers and final rankings
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 373

**Intent:**
bingo caller for the village hall on a projector

**Spec:**
```
Type:       Desktop application (bingo caller)
Data model: Game(id, type, started_at)
            Call(game_id -> Game, number, called_at)
Features:   - Draw random numbers from 1-90 without repeats
            - Show the current number large with a calling phrase
            - Display a board of called numbers
            - Check a claimed ticket against called numbers
            - Speak numbers aloud with text-to-speech
Storage:    In-memory, game log to file
Tech stack: Python, Pygame, pyttsx3
```

---

## Example 374

**Intent:**
radio mic frequency planner for theatre so channels dont interfere

**Spec:**
```
Type:       Desktop application (RF frequency coordination)
Data model: Receiver(id, model, band_low_mhz, band_high_mhz, step_khz)
            Channel(id, receiver_id -> Receiver, frequency_mhz, actor)
            Exclusion(id, low_mhz, high_mhz, reason)
Features:   - Enter receivers and their tuning bands
            - Calculate intermodulation products
            - Find compatible frequency sets avoiding exclusions and TV channels
            - Assign channels to actors
            - Export a frequency sheet
Storage:    JSON show file
Tech stack: Python, PySide6, NumPy
```

---

## Example 375

**Intent:**
opera surtitle cueing, translated lines shown above the stage, operator clicks next with the music

**Spec:**
```
Type:       Desktop application (surtitle playback)
Data model: Production(id, title, language)
            Surtitle(id, production_id -> Production, number, original, translation, score_page, bar)
Features:   - Show the next surtitles in the operator view with score references
            - Advance with a key press and blank between lines
            - Output to a projector at a fixed position
            - Jump to any number in rehearsal
            - Import surtitles from a spreadsheet
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 376

**Intent:**
turn my handwriting into a font, I fill in a template and scan it

**Spec:**
```
Type:       Desktop application (handwriting font maker)
Data model: Template(id, characters, grid_rows, grid_cols)
            GlyphScan(character, image_path, bitmap)
Features:   - Print a template with boxes for each character
            - Detect boxes on the scanned template
            - Trace each character to vector outlines
            - Set spacing and baseline
            - Export an OTF font
Storage:    Project folder with scans
Tech stack: Python, OpenCV, potrace, fontTools
```

---

## Example 377

**Intent:**
braille typing trainer, six keys like a perkins brailler

**Spec:**
```
Type:       Desktop application (Perkins-style braille trainer)
Data model: Lesson(id, title, grade, content)
            Result(id, lesson_id -> Lesson, accuracy, cps, completed_at)
Features:   - Map S, D, F, J, K, L to braille dots 1-6
            - Register chords when keys are pressed together
            - Speak each typed letter for blind learners
            - Teach letters and contractions in lessons
            - Track accuracy per cell
Storage:    SQLite database
Tech stack: Python, Pygame, pyttsx3
```

---

## Example 378

**Intent:**
skipping rope rhythm game with a webcam

**Spec:**
```
Type:       Desktop game (jump-rope rhythm)
Data model: Track(id, audio_file, bpm)
            Session(id, track_id -> Track, jumps, misses)
Features:   - Detect jumps from body position with the webcam
            - Show a rope animation turning to the beat
            - Count jumps that land on the beat
            - Speed up between songs
            - Keep a jump streak record
Storage:    Local JSON
Tech stack: Python, MediaPipe, Pygame
```

---

## Example 379

**Intent:**
type words to steer a sailboat through islands, port and starboard words

**Spec:**
```
Type:       Desktop game (typing navigation)
Data model: Course(id, islands_json, word_list)
            Run(id, course_id -> Course, time_ms, wpm)
Features:   - Show words on the left and right side of the boat
            - Turn the boat by typing the word on that side
            - Trim sails with longer words for speed
            - Hit rocks if typing is too slow
            - Record course times
Storage:    Local save
Tech stack: C#, MonoGame
```

---

## Example 380

**Intent:**
letter dice game, roll 7 dice and make the best word before timer runs out

**Spec:**
```
Type:       Desktop game (letter dice)
Data model: Die(id, faces)
            Round(id, roll, best_word, points)
Features:   - Roll seven custom letter dice with animation
            - Let the player type words from the rolled letters
            - Score by letter rarity and word length
            - Allow one re-roll per round
            - Play against an AI that finds the best word
Storage:    Bundled dictionary, local scores
Tech stack: Java, libGDX
```

---

## Example 381

**Intent:**
ant colony simulation sandbox, ants follow pheromones to food

**Spec:**
```
Type:       Desktop game (ant colony sandbox)
Data model: Ant(id, x, y, carrying, role)
            Grid(width, height, food, pheromone_home, pheromone_food)
Features:   - Simulate thousands of ants with pheromone trails
            - Evaporate and diffuse pheromones each tick
            - Place food, walls and water with a brush
            - Grow the colony as food is gathered
            - Toggle a pheromone heatmap overlay
Storage:    Scene save files
Tech stack: Rust, Bevy
```

---

## Example 382

**Intent:**
TD with mirrors, you place one laser and bend it with mirrors to hit enemies

**Spec:**
```
Type:       Desktop game (laser tower defence)
Data model: Mirror(id, x, y, angle)
            Emitter(id, x, y, power)
            Enemy(id, type, hp, x, y)
Features:   - Trace laser beams with reflections each frame
            - Place and rotate mirrors on a grid
            - Split beams with prisms for lower damage
            - Damage enemies crossing the beam
            - Limit mirrors per level
Storage:    Local save
Tech stack: C++, SFML
```

---

## Example 383

**Intent:**
cave diving roguelike, manage air and silt and dont get lost

**Spec:**
```
Type:       Desktop game (cave diving roguelike)
Data model: Cave(id, seed, depth, tunnels_json)
            Diver(air_bar, light, line_remaining)
Features:   - Generate underwater cave systems from a seed
            - Drain air faster at depth
            - Stir up silt that blocks vision when moving fast
            - Lay a guideline to find the way out
            - Find artefacts deeper in each dive
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 384

**Intent:**
ski resort builder, lifts, runs, snow cannons

**Spec:**
```
Type:       Desktop game (ski resort builder)
Data model: Lift(id, type, base_x, base_y, top_x, top_y, capacity)
            Run(id, path_json, difficulty, snow_depth)
            Guest(id, skill, happiness)
Features:   - Build lifts and draw runs on a mountain heightmap
            - Rate run difficulty from slope steepness
            - Run snow cannons when snowfall is low
            - Simulate guests choosing runs by skill
            - Balance ticket prices and costs
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 385

**Intent:**
alpaca farm game, shear wool, spin yarn, sell at fairs

**Spec:**
```
Type:       Desktop game (alpaca farm sim)
Data model: Alpaca(id, name, color, fleece_quality, age, happiness)
            Fleece(id, alpaca_id -> Alpaca, weight_g, grade)
            Yarn(id, color, weight_g, quality)
Features:   - Feed, groom and shear alpacas
            - Spin fleece into yarn and dye it
            - Breed alpacas for fleece colour and quality
            - Sell yarn at seasonal fairs
            - Decorate the farm
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 386

**Intent:**
soapbox derby racing where you build the cart first then race down a hill

**Spec:**
```
Type:       Desktop game (soapbox derby)
Data model: Cart(id, chassis, wheels, weight_kg, aero)
            Hill(id, name, track_file)
            Result(hill_id -> Hill, cart_id -> Cart, time_ms)
Features:   - Build carts from parts affecting weight, grip and drag
            - Race gravity-only down hills
            - Steer and brake with keyboard
            - Break parts on crashes
            - Show part stats and record times
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 387

**Intent:**
snooker player career game, manage practice, tournaments, sponsors

**Spec:**
```
Type:       Desktop game (snooker career management)
Data model: Player(potting, safety, break_building, nerve, ranking_points, money)
            Tournament(id, name, prize_fund, ranking_points, month)
            Match(id, tournament_id -> Tournament, opponent, frames_won, frames_lost)
Features:   - Plan practice sessions that raise skills
            - Enter tournaments and pay entry fees
            - Simulate frames shot by shot from skills
            - Sign sponsors that pay by ranking
            - Track world ranking over seasons
Storage:    SQLite save
Tech stack: Python, PySide6
```

---

## Example 388

**Intent:**
science fair quiz show for school assembly, two teams on stage

**Spec:**
```
Type:       Desktop game (science quiz show)
Data model: Question(id, subject, text, answer, media_path, points)
            Team(id, name, score)
Features:   - Show questions on the hall projector
            - Use two USB buzzers for the teams
            - Include picture and short video questions
            - Run a final speed round with a timer
            - Show the score bar for both teams
Storage:    SQLite question bank
Tech stack: Python, PySide6, QtMultimedia
```

---

## Example 389

**Intent:**
balancing chemical equations game

**Spec:**
```
Type:       Desktop game (equation balancing)
Data model: Equation(id, reactants, products, difficulty)
Features:   - Show an unbalanced equation
            - Let players set coefficients with plus and minus buttons
            - Show atom counts on both sides live
            - Check the balance and celebrate
            - Increase difficulty to redox equations
Storage:    Bundled equation list, local progress
Tech stack: Kotlin, Compose for Desktop
```

---

## Example 390

**Intent:**
rafting co-op game, 2-4 paddlers on one raft, have to paddle in sync

**Spec:**
```
Type:       Desktop game (local co-op rafting)
Data model: River(id, sections_json, grade)
            Run(id, river_id -> River, time_ms, flips)
Features:   - Give each player a paddle on a side of the raft
            - Turn and accelerate from combined paddle strokes
            - Spin the raft on rocks and flip it in big rapids
            - Rescue paddlers who fall in
            - Race down rivers of increasing grade
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 391

**Intent:**
tactics game on a river, units on rafts drift downstream each turn

**Spec:**
```
Type:       Desktop game (river tactics)
Data model: Raft(id, x, y, units, hp)
            Current(x, y, direction, strength)
Features:   - Move units between rafts and banks
            - Drift rafts with the current at the end of each turn
            - Shoot from rafts with range penalties
            - Ram rafts into each other
            - Win by reaching the river mouth or sinking the enemy
Storage:    Local save
Tech stack: C#, MonoGame
```

---

## Example 392

**Intent:**
story game where you're a late night radio DJ and callers tell you strange things

**Spec:**
```
Type:       Desktop game (radio interactive fiction)
Data model: Caller(id, name, story_arc, trust)
            Night(number, calls_json, songs)
Features:   - Take calls and choose how to respond
            - Pick songs that change caller moods
            - Connect callers' stories over several nights
            - Keep a notepad of clues
            - Reach several endings
Storage:    Local save
Tech stack: Unity, C#, Yarn Spinner
```

---

## Example 393

**Intent:**
platformer where you have only 3 grappling anchors per level, place them then swing

**Spec:**
```
Type:       Desktop game (grapple puzzle-platformer)
Data model: Level(id, tilemap_file, anchors_allowed)
Features:   - Place up to three anchor points in each level
            - Swing on a rope with pendulum physics
            - Release to fling through the air
            - Retrieve anchors to reuse them
            - Track time and anchors used
Storage:    Local save
Tech stack: Lua, LÖVE
```

---

## Example 394

**Intent:**
need app for my yoga studio front desk, class passes and who came

**Spec:**
```
Type:       Desktop application (studio front desk)
Data model: Client(id, name, email, phone)
            Pass(id, client_id -> Client, type, classes_left, expires_on)
            ClassSession(id, name, starts_at, instructor, capacity)
            CheckIn(session_id -> ClassSession, client_id -> Client)
Features:   - Check clients into today's classes
            - Deduct a class from their pass
            - Warn on expired or empty passes
            - Show class attendance by instructor
            - Sell new passes at the desk
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 395

**Intent:**
hey so my brother is a locksmith and he keeps key codes on paper cards, wants it on computer but very secure

**Spec:**
```
Type:       Desktop application (locksmith key records)
Auth:       Master password, database encrypted at rest
Data model: Customer(id, name, address, phone)
            KeyRecord(id, customer_id -> Customer, lock_brand, key_code, blank, cuts, authorised_names)
            Job(id, customer_id -> Customer, date, description, fee)
Features:   - Store key codes and cut depths per customer
            - Require proof-of-authorisation names before copying
            - Search by customer or address
            - Log jobs and fees
            - Lock automatically after five idle minutes
Storage:    SQLCipher encrypted database
Tech stack: Python, PySide6, sqlcipher3
```

---

## Example 396

**Intent:**
dog grooming notes, each dog's cut style, temperament, allergies, with before after photos

**Spec:**
```
Type:       Desktop application (dog grooming records)
Data model: Owner(id, name, phone)
            Dog(id, owner_id -> Owner, name, breed, temperament, allergies)
            Groom(id, dog_id -> Dog, date, style, blade_numbers, price, before_photo, after_photo)
Features:   - Save each dog's preferred cut and blade numbers
            - Flag allergies and biting risks clearly
            - Attach before and after photos
            - Show when each dog is due back
            - Print a price list
Storage:    SQLite database and photo folder
Tech stack: Python, Tkinter, Pillow
```

---

## Example 397

**Intent:**
tattoo studio consent forms on a tablet at the counter, client signs with finger

**Spec:**
```
Type:       Desktop application (tattoo consent forms)
Data model: Client(id, name, date_of_birth, id_checked)
            ConsentForm(id, client_id -> Client, artist, design_description, health_answers_json, signature_png, signed_at)
Features:   - Fill health and consent questions on a Windows tablet
            - Block clients under 18 by date of birth
            - Capture a finger signature
            - Save a signed PDF per client
            - Search past forms by name
Storage:    SQLite database and PDF folder
Tech stack: C#, WPF, QuestPDF
```

---

## Example 398

**Intent:**
I am a retired engineer and since years I collect old slide rules, more than 300 now. I want catalogue program with photos, maker, scales on it and how much I paid, and a nice report for when my children must sell them one day.

**Spec:**
```
Type:       Desktop application (collection catalogue)
Data model: Maker(id, name, country)
            SlideRule(id, maker_id -> Maker, model, year, length_cm, scales, condition, price_paid, acquired_on, estimated_value)
            Photo(id, slide_rule_id -> SlideRule, file_path)
Features:   - Catalogue each item with maker, scales and condition
            - Attach several photos per item
            - Search and filter by maker, decade and scale type
            - Show total paid and estimated value
            - Print a valuation report with photos
Storage:    SQLite database and photo folder
Tech stack: Python, PySide6, ReportLab
```

---

## Example 399

**Intent:**
I am PE teacher in Turkey. I measure students in running, jumping, flexibility each semester, I want program that compare with norms and show improvement.

**Spec:**
```
Type:       Desktop application (fitness test tracker)
Data model: Student(id, name, sex, birth_date, class_group)
            Test(id, name, unit, higher_is_better)
            Norm(test_id -> Test, sex, age, percentile, value)
            Measurement(id, student_id -> Student, test_id -> Test, semester, value)
Features:   - Enter test results per class and semester
            - Convert results to percentiles from age norms
            - Show each student's improvement between semesters
            - Print a fitness report card
            - Switch interface between Turkish and English
Storage:    SQLite database
Tech stack: Java, JavaFX
```

---

## Example 400

**Intent:**
ok this is kind of specific but i run a small ballroom dance competition once a year and the scoring uses the skating system and doing it by hand takes hours. adjudicators give placings and the computer should work out final results

**Spec:**
```
Type:       Desktop application (dance competition scoring)
Data model: Event(id, name, dance_style, rounds)
            Couple(id, number, leader, follower)
            Adjudicator(id, letter, name)
            Mark(event_id -> Event, round, couple_id -> Couple, adjudicator_id -> Adjudicator, placing, recall)
Features:   - Enter recall marks for heats and placings for finals
            - Calculate recalls for the next round
            - Apply the skating system rules to rank finalists
            - Break ties with the skating system tiebreak rules
            - Print result sheets with the marks table
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 401

**Intent:**
I'm a speech therapist, kids practise sounds like s and r. Want a little game on my laptop where the kid says the word into microphone and gets a sticker, I mark right or wrong with a key.

**Spec:**
```
Type:       Desktop game (speech practice)
Data model: Child(id, name, target_sounds)
            Word(id, text, sound, position, image_path)
            Trial(id, child_id -> Child, word_id -> Word, correct, recorded_path, at)
Features:   - Show a picture word with the target sound
            - Record the child's attempt from the microphone
            - Let the therapist mark correct or incorrect with keys
            - Reward stickers on a chart for each trial
            - Report accuracy by sound and word position
Storage:    SQLite database and audio folder
Tech stack: Python, Pygame, sounddevice
```

---

## Example 402

**Intent:**
gm tool, track time passing in a dungeon, torches burning out, random encounter checks every 10 min

**Spec:**
```
Type:       Desktop application (dungeon turn tracker)
Data model: LightSource(id, holder, type, turns_left)
            Timer(id, label, turns_left, repeat)
            EncounterTable(id, name, chance_in_6, entries)
Features:   - Advance dungeon turns with one button
            - Burn down torches and lanterns
            - Roll encounter checks on a schedule
            - Track spell durations as custom timers
            - Log events in a session journal
Storage:    JSON session file
Tech stack: Go, Fyne
```

---

## Example 403

**Intent:**
translation glossary but shared with my 3 colleagues over the office network, all offline

**Spec:**
```
Type:       Desktop application (shared glossary client)
Data model: Term(id, source, target, domain, client, author, updated_at, status)
            Comment(id, term_id -> Term, author, text, created_at)
Features:   - Search terms as you type
            - Add and edit terms with author tracking
            - Discuss terms in comment threads
            - Lock approved terms for editing by a lead
            - See changes from colleagues live
API:        REST
            GET  /terms?q={text}
            POST /terms
            PUT  /terms/{id}
Storage:    PostgreSQL on an office server
Tech stack: Python, PySide6 client, FastAPI server
```

---

## Example 404

**Intent:**
plz help, music shop needs repair tickets for guitars, whats wrong, parts, price, ready or not

**Spec:**
```
Type:       Desktop application (instrument repair tickets)
Data model: Customer(id, name, phone)
            Instrument(id, customer_id -> Customer, type, brand, model, serial)
            Ticket(id, instrument_id -> Instrument, issue, work_done, parts_cost, labour_cost, status, promised_on)
Features:   - Create a ticket at drop-off with a printed claim stub
            - Move tickets through received, in progress, ready, collected
            - Add parts and labour to the bill
            - Text the customer when the instrument is ready
            - Show overdue repairs
Storage:    SQLite database
Tech stack: C#, WinForms, Twilio API
```

---

## Example 405

**Intent:**
seating chart that rotates students every week so everyone sits with everyone eventually

**Spec:**
```
Type:       Desktop application (rotating seating plan)
Data model: Student(id, name)
            Week(id, start_date)
            Seating(week_id -> Week, table, student_id -> Student)
            PairHistory(student_a_id -> Student, student_b_id -> Student, times)
Features:   - Set number of tables and seats
            - Generate weekly seating that minimises repeat partners
            - Lock some students to specific tables
            - Show a matrix of who has sat with whom
            - Print the plan for the door
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 406

**Intent:**
learning app for typists in Hindi using Inscript keyboard

**Spec:**
```
Type:       Desktop application (Hindi typing tutor)
Data model: Lesson(id, level, text)
            Result(id, lesson_id -> Lesson, wpm, accuracy, completed_at)
Features:   - Show the Inscript layout with the next key highlighted
            - Handle matras and conjunct characters correctly
            - Progress from vowels to words to paragraphs
            - Measure speed and accuracy
            - Offer a government exam practice test mode
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 407

**Intent:**
kiosk at the zoo, kids answer about animals and get a printed sticker badge

**Spec:**
```
Type:       Desktop application (zoo quiz kiosk)
Data model: Animal(id, name, enclosure, image_path, facts)
            Question(id, animal_id -> Animal, text, options, answer_index)
            Completion(id, score, printed, completed_at)
Features:   - Run five-question quizzes on a touchscreen
            - Show animal photos and facts after each answer
            - Print a sticker badge on a label printer for scores of 4+
            - Reset after inactivity
            - Count completions per day
Storage:    SQLite database
Tech stack: Godot 4, GDScript
```

---

## Example 408

**Intent:**
rhythm game in browser where you are a heart beating, keep pulse steady as the patient exercises

**Spec:**
```
Type:       Browser game (heartbeat rhythm)
Features:   - Tap a key for each heartbeat to a changing tempo
            - Raise tempo as the patient runs and drop it as they rest
            - Show an ECG line from the player's beats
            - Fail the level after too many missed beats
            - Teach facts about heart rate between levels
Storage:    Browser localStorage
Tech stack: JavaScript, Web Audio API, Canvas
```

---

## Example 409

**Intent:**
typing game where u write a letter to santa and elves judge your speed lol

**Spec:**
```
Type:       Desktop game (festive typing)
Data model: Letter(id, text, difficulty)
            Result(id, letter_id -> Letter, wpm, accuracy, elf_rating)
Features:   - Show a letter to Santa to type out
            - Animate elves reacting to speed and mistakes
            - Rate the result as naughty or nice
            - Unlock harder letters
            - Print a nice-list certificate
Storage:    Local JSON
Tech stack: Python, Pygame
```

---

## Example 410

**Intent:**
game where you guess a secret 5 letter word in a few tries, but it's about chemistry terms

**Spec:**
```
Type:       Browser game (word guessing)
Data model: Word(id, text, definition)
            Stat(games, wins, streak, guess_distribution)
Features:   - Pick a secret chemistry word each day
            - Accept guesses only from the chemistry word list
            - Colour letters correct, misplaced or absent
            - Show the definition after the game
            - Track streaks
Storage:    Browser localStorage
Tech stack: TypeScript, React, Vite
```

---

## Example 411

**Intent:**
water flow sandbox, dig channels and dams and watch it flow

**Spec:**
```
Type:       Desktop game (water sandbox)
Data model: Terrain(width, height, heights, water_depths)
Features:   - Sculpt terrain with raise and lower brushes
            - Simulate water flow with a shallow-water model
            - Place dams, gates and pumps
            - Add rain and springs
            - Save landscapes
Storage:    Binary terrain files
Tech stack: C++, OpenGL, compute shaders
```

---

## Example 412

**Intent:**
td where you protect a sleeping baby from noisy toys

**Spec:**
```
Type:       Desktop game (bedroom tower defence)
Data model: Defender(id, type, x, y, level)
            Toy(id, type, noise, speed, hp)
            Room(id, layout_json, cot_x, cot_y)
Features:   - Place parent helpers like pillows and teddy guards
            - Stop noisy toys before they reach the cot
            - Track a sleep meter instead of lives
            - Earn lullaby notes to spend on upgrades
            - Play levels across bedtime nights
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 413

**Intent:**
roguelike in ascii in the browser, wizard tower floors, spells combine

**Spec:**
```
Type:       Browser game (ASCII roguelike)
Data model: Spell(id, element, shape, cost)
            Floor(number, seed, map)
Features:   - Render the map with ASCII characters in a canvas grid
            - Generate tower floors with rooms and doors
            - Combine element and shape runes into spells
            - Fight monsters in turn-based combat
            - Keep a high-score table of deepest floors
Storage:    Browser localStorage
Tech stack: JavaScript, rot.js
```

---

## Example 414

**Intent:**
build a colony on a frozen moon, heat is the main resource

**Spec:**
```
Type:       Desktop game (frozen colony builder)
Data model: Building(id, type, x, y, heat_output, heat_need)
            Colonist(id, name, warmth, job)
            Storm(severity, turn)
Features:   - Place heaters and buildings in heat radius
            - Mine ice and convert it to fuel and water
            - Assign colonists to jobs
            - Survive cold storms that drain heat
            - Expand with research
Storage:    Local save
Tech stack: Godot 4, C#
```

---

## Example 415

**Intent:**
lavender farm game, plant, harvest, distil oil, very relaxing music

**Spec:**
```
Type:       Desktop game (lavender farm sim)
Data model: Field(id, rows, variety, bloom_stage)
            Product(id, type, quantity, quality)
Features:   - Plant and weed lavender rows
            - Harvest at full bloom
            - Distil essential oil and make dried bundles
            - Sell products at a farm shop
            - Change scenery with seasons
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 416

**Intent:**
rally racing with co-driver pace notes read out

**Spec:**
```
Type:       Desktop game (rally racing)
Data model: Stage(id, name, surface, spline_json, pace_notes)
            Result(stage_id -> Stage, time_ms, damage)
Features:   - Drive point-to-point stages on gravel, tarmac and snow
            - Read pace notes aloud ahead of corners
            - Model grip by surface and damage
            - Repair the car between stages with limited time
            - Combine stage times into a rally total
Storage:    Local save
Tech stack: Unreal Engine 5, C++
```

---

## Example 417

**Intent:**
manage a darts pub team league, picking players and their form

**Spec:**
```
Type:       Desktop game (pub darts league manager)
Data model: Player(id, name, average, checkout_rate, nerves, form)
            Fixture(id, opponent, date, legs_won, legs_lost)
            Pub(id, name, budget, reputation)
Features:   - Pick players for singles and pairs games
            - Simulate legs dart by dart from player stats
            - Change form with practice and results
            - Recruit regulars from the pub
            - Win the league over a season
Storage:    SQLite save
Tech stack: Python, Tkinter
```

---

## Example 418

**Intent:**
true or false party game for 2-8 players on one keyboard, each has a key

**Spec:**
```
Type:       Desktop game (true or false party)
Data model: Statement(id, text, is_true, category, explanation)
            Player(id, name, true_key, false_key, score)
Features:   - Give each player a pair of keys
            - Show a statement with a short timer
            - Score correct answers and penalise wrong ones
            - Show the explanation after each round
            - Load categories from CSV packs
Storage:    CSV statement packs
Tech stack: Python, Pygame
```

---

## Example 419

**Intent:**
game to teach kids reading clocks, set the hands to the time said

**Spec:**
```
Type:       Desktop game (telling time)
Data model: Level(id, granularity_min, use_24h)
            Progress(child_name, level_id -> Level, stars)
Features:   - Say a time aloud and show it as words
            - Let the child drag the hour and minute hands
            - Move the hour hand realistically with the minutes
            - Progress from o'clock to five-minute steps
            - Award stars per level
Storage:    Local JSON
Tech stack: C#, MonoGame
```

---

## Example 420

**Intent:**
co-op bakery game for 2, one kneads and bakes, other decorates cakes

**Spec:**
```
Type:       Desktop game (local co-op bakery)
Data model: Order(id, item, decoration, deadline)
            Station(id, type, x, y)
Features:   - Split baking and decorating stations between two players
            - Pass items across a counter
            - Burn items left in the oven too long
            - Match decorations to order pictures
            - Earn stars per day
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 421

**Intent:**
tactics game with wizards where terrain can be changed by spells, fire burns grass, ice freezes water

**Spec:**
```
Type:       Desktop game (elemental tactics)
Data model: Wizard(id, element, hp, mana, x, y)
            Tile(x, y, terrain, state)
Features:   - Move wizards on a grid each turn
            - Cast spells that change terrain
            - Spread fire through grass and freeze water into bridges
            - Use terrain changes to trap enemies
            - Fight AI covens in a campaign
Storage:    Local save
Tech stack: C#, Unity
```

---

## Example 422

**Intent:**
choose your path story about a girl starting a new school, for teenagers, about anxiety

**Spec:**
```
Type:       Desktop game (narrative interactive fiction)
Data model: Scene(id, text, art, choices_json)
            State(confidence, friendships_json)
Features:   - Show scenes with simple illustrations
            - Offer choices that change confidence and friendships
            - Include calm breathing mini-moments
            - Lead to several realistic endings
            - Link to support resources at the end
Storage:    Local save
Tech stack: Ren'Py
```

---

## Example 423

**Intent:**
puzzle platformer where you leave a trail of paint and only painted floor is solid

**Spec:**
```
Type:       Desktop game (paint puzzle-platformer)
Data model: Level(id, tilemap_file, paint_limit)
Features:   - Leave paint behind while moving
            - Make only painted tiles solid on return trips
            - Limit paint per level
            - Refill paint at buckets
            - Reach the exit with the fewest paint used
Storage:    Local save
Tech stack: C++, Raylib
```

---

## Example 424

**Intent:**
cue light system for backstage, stage manager presses button, light turns on at the fly rail and they acknowledge

**Spec:**
```
Type:       Desktop application (cue light controller)
Data model: Station(id, name, device_ip)
            CueLightEvent(id, station_id -> Station, state, at)
Features:   - Show buttons for standby, go and off per station
            - Send states to ESP32 cue light boxes over UDP
            - Show acknowledgement when crew press their button
            - Log every standby and go with timestamps
            - Map stations to keyboard shortcuts
Storage:    SQLite event log
Tech stack: Python, PySide6
```

---

## Example 425

**Intent:**
my mum is a seamstress and wants to calculate how much fabric for curtains

**Spec:**
```
Type:       Desktop application (curtain fabric calculator)
Data model: Window(id, client, width_cm, drop_cm)
            Fabric(id, name, width_cm, pattern_repeat_cm, price_per_m)
            Quote(id, window_id -> Window, fabric_id -> Fabric, fullness, metres, cost)
Features:   - Enter window size and heading fullness
            - Calculate drops and widths needed
            - Account for pattern repeat matching
            - Add hem and heading allowances
            - Print a quote with fabric and making cost
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 426

**Intent:**
greek and latin flashcards for my classics students with declension tables

**Spec:**
```
Type:       Desktop application (classics vocabulary)
Data model: Lemma(id, language, headword, gender, declension, meaning)
            Form(id, lemma_id -> Lemma, case, number, form)
            Review(id, lemma_id -> Lemma, due_on, interval_days, ease)
Features:   - Drill vocabulary with spaced repetition
            - Show full declension and conjugation tables
            - Quiz specific forms like genitive plural
            - Type Greek with a built-in polytonic keyboard
            - Import word lists from the textbook chapters
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 427

**Intent:**
something for my gym's tv that shows the workout of the day and runs interval timers

**Spec:**
```
Type:       Desktop application (gym workout display)
Data model: Workout(id, date, title, blocks_json)
            TimerPreset(id, type, work_sec, rest_sec, rounds)
Features:   - Show the day's workout full screen on the TV
            - Run EMOM, Tabata and AMRAP timers
            - Beep at the start and end of intervals
            - Control timers from a phone remote page
            - Plan workouts for the week ahead
Storage:    SQLite database
Tech stack: Electron, TypeScript
```

---

## Example 428

**Intent:**
dnd loot splitter, divide coins and items fairly between players

**Spec:**
```
Type:       Desktop application (loot splitter)
Data model: Player(id, name)
            LootItem(id, name, value_gp, claimed_by_id -> Player)
            Haul(id, session, coins_cp, coins_sp, coins_gp, coins_pp)
Features:   - Enter coins and items from a haul
            - Convert coin types and split evenly
            - Let players claim items against their share
            - Balance shares with coins
            - Keep a history per session
Storage:    JSON file
Tech stack: Python, Textual
```

---

## Example 429

**Intent:**
subtitle spell checker that ignores timecodes, supports several languages

**Spec:**
```
Type:       Desktop application (subtitle spell check)
Data model: Dictionary(language, custom_words)
            Issue(cue_index, word, suggestions)
Features:   - Open SRT, ASS or WebVTT files
            - Check spelling of cue text only
            - Suggest corrections and apply them in place
            - Add character names to a custom dictionary
            - Save the corrected file
Storage:    Files on disk, custom words in text files
Tech stack: Python, PySide6, pyenchant (Hunspell)
```

---

## Example 430

**Intent:**
font sample book printer for my design students, one page per font

**Spec:**
```
Type:       Command-line tool (font specimen printer)
Features:   - Scan a folder of fonts
            - Lay out one specimen page per font with name, weights and glyph set
            - Show a pangram at several sizes
            - Sort fonts by family or classification
            - Write a single PDF book
Input:      Folder of TTF/OTF files
Tech stack: Python, fontTools, ReportLab
```

---

## Example 431

**Intent:**
snippet manager for code with tags and search

**Spec:**
```
Type:       Desktop application (code snippet manager)
Data model: Snippet(id, title, language, code, description, created_at)
            Tag(id, name)
            SnippetTag(snippet_id -> Snippet, tag_id -> Tag)
Features:   - Save snippets with syntax highlighting
            - Tag and search snippets by text or tag
            - Copy a snippet with one click
            - Open a quick search window with a hotkey
            - Sync snippets as files in a Git folder
Storage:    SQLite database
Tech stack: Rust, Tauri, Svelte
```

---

## Example 432

**Intent:**
allotment plot planner for crop rotation

**Spec:**
```
Type:       Desktop application (allotment rotation planner)
Data model: Bed(id, name, width_m, length_m)
            Crop(id, name, family, spacing_cm, sow_month, harvest_month)
            Planting(id, bed_id -> Bed, crop_id -> Crop, year, season)
Features:   - Draw beds on a plot plan
            - Assign crops to beds per year
            - Warn when a crop family repeats in a bed within three years
            - Show a sowing and harvest calendar
            - Calculate plant counts from spacing
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 433

**Intent:**
watch repair log for horologist, movements, parts ordered, timegrapher readings

**Spec:**
```
Type:       Desktop application (watch repair log)
Data model: Watch(id, owner, brand, calibre, serial)
            Service(id, watch_id -> Watch, received_on, work_done, status, price)
            Reading(id, service_id -> Service, position, rate_s_day, amplitude, beat_error)
            Part(id, service_id -> Service, part_number, supplier, cost, ordered_on)
Features:   - Record watches and service jobs
            - Log timegrapher readings by position
            - Track ordered parts and arrivals
            - Show jobs waiting on parts
            - Print a service certificate
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 434

**Intent:**
grades + attendance for a small evening language school, 10 teachers, runs on office pc

**Spec:**
```
Type:       Desktop application (language school administration)
Data model: Course(id, language, level, teacher, weekday, time)
            Learner(id, name, email)
            Enrolment(course_id -> Course, learner_id -> Learner, paid)
            Lesson(id, course_id -> Course, date)
            Attendance(lesson_id -> Lesson, learner_id -> Learner, present)
Features:   - Enrol learners into courses and track fees
            - Take attendance per lesson
            - Record CEFR level test results
            - Print certificates for learners above 80% attendance
            - Show course fill rates
Storage:    SQLite database
Tech stack: Java, JavaFX
```

---

## Example 435

**Intent:**
nursery rhyme music game for toddlers, press any key and the next note of the song plays

**Spec:**
```
Type:       Desktop game (toddler music)
Data model: Song(id, title, notes_json, images)
Features:   - Play the next note of the song on any key press
            - Show colourful shapes for each press
            - Ignore system shortcuts so toddlers can't exit
            - Switch songs after the end
            - Exit only with a parent key combination
Storage:    Bundled song files
Tech stack: Python, Pygame
```

---

## Example 436

**Intent:**
pallet loading sandbox puzzle, fit odd shaped parcels into a van

**Spec:**
```
Type:       Desktop game (packing puzzle)
Data model: Level(id, van_size, parcels_json, fragile_ids)
Features:   - Rotate and place 3D parcels in a van
            - Prevent heavy parcels on fragile ones
            - Score by space used
            - Simulate the drive and topple badly stacked loads
            - Unlock bigger vans
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 437

**Intent:**
lesson observation forms for school leaders, tick criteria and write strengths

**Spec:**
```
Type:       Desktop application (lesson observation)
Data model: Teacher(id, name, department)
            Framework(id, name, criteria_json)
            Observation(id, teacher_id -> Teacher, framework_id -> Framework, date, ratings_json, strengths, targets)
Features:   - Fill observation forms against a chosen framework
            - Rate each criterion and write strengths and targets
            - Show a teacher's observations over time
            - Show department-wide trends per criterion
            - Export forms to PDF
Storage:    SQLite database
Tech stack: C#, Avalonia, QuestPDF
```

---

## Example 438

**Intent:**
mixtape cassette planner, fit songs onto side A and B without going over

**Spec:**
```
Type:       Desktop application (cassette mix planner)
Data model: Tape(id, name, length_min)
            Track(id, title, artist, duration_sec)
            Placement(tape_id -> Tape, track_id -> Track, side, position)
Features:   - Import tracks with durations from a music folder
            - Drag tracks onto side A or B
            - Show time remaining per side
            - Suggest a split that balances both sides
            - Print a J-card insert
Storage:    JSON project file
Tech stack: Python, Tkinter, mutagen
```

---

## Example 439

**Intent:**
church rota for readers, coffee and flowers so nobody does it twice in a row

**Spec:**
```
Type:       Desktop application (volunteer rota)
Data model: Volunteer(id, name, roles, unavailable_dates)
            Role(id, name, people_needed)
            Service(id, date)
            Duty(service_id -> Service, role_id -> Role, volunteer_id -> Volunteer)
Features:   - Store volunteers and which roles they can do
            - Generate a quarterly rota fairly
            - Avoid back-to-back weeks and unavailable dates
            - Swap duties by hand
            - Print and email the rota
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 440

**Intent:**
tool to turn a book manuscript into an audiobook script with character voices marked

**Spec:**
```
Type:       Desktop application (audiobook script prep)
Data model: Manuscript(id, title, file_path)
            Character(id, name, voice_note, color)
            Line(id, manuscript_id -> Manuscript, position, text, character_id -> Character, is_narration)
Features:   - Import DOCX manuscripts
            - Detect dialogue and suggest the speaker
            - Assign lines to characters with colours
            - Keep pronunciation notes per character and term
            - Export a narrator script as PDF
Storage:    SQLite project file
Tech stack: Python, PySide6, spaCy
```

---

## Example 441

**Intent:**
library for my board game cafe, which games are on which shelf, missing pieces, how often played

**Spec:**
```
Type:       Desktop application (board game cafe library)
Data model: Game(id, title, min_players, max_players, play_time_min, shelf, condition)
            MissingPiece(id, game_id -> Game, description, reported_on)
            Play(id, game_id -> Game, table, started_at)
Features:   - Catalogue games with player count and shelf
            - Recommend games for a table's group size and time
            - Log plays per table
            - Record missing or damaged pieces
            - Show most and least played games
Storage:    SQLite database
Tech stack: C#, WPF
```

---

## Example 442

**Intent:**
puppet show controller, servo puppets move with recorded sequences from my laptop

**Spec:**
```
Type:       Desktop application (animatronic sequencer)
Data model: Servo(id, name, channel, min_us, max_us)
            Sequence(id, name, audio_file, duration_ms)
            Keyframe(id, sequence_id -> Sequence, servo_id -> Servo, time_ms, position)
Features:   - Record servo moves live with sliders
            - Edit keyframes on a timeline synced to audio
            - Send positions to an Arduino over serial
            - Play sequences on cue
            - Limit speed to protect servos
Storage:    JSON sequence files
Tech stack: Python, PySide6, pyserial
```

---

## Example 443

**Intent:**
typing practice with famous speeches, and it tells me which letters i'm slow on

**Spec:**
```
Type:       Desktop application (speech typing practice)
Data model: Speech(id, title, speaker, year, text)
            KeyStat(key, presses, errors, avg_ms)
            Session(id, speech_id -> Speech, wpm, accuracy)
Features:   - Type speeches paragraph by paragraph
            - Measure time per keystroke
            - Show a keyboard heatmap of slow and error-prone keys
            - Resume a speech where you stopped
            - Show context about each speech
Storage:    SQLite database
Tech stack: Kotlin, Compose for Desktop
```

---

## Example 444

**Intent:**
tabletop rpg dice roller with 3d dice on screen for streaming

**Spec:**
```
Type:       Desktop application (3D dice roller)
Data model: Roll(id, expression, results, total, rolled_at, label)
            DiceSkin(id, name, texture, color)
Features:   - Parse expressions like 4d6kh3+2
            - Throw physically simulated 3D dice
            - Read results from the face that lands up
            - Use a green background for stream chroma key
            - Keep a roll history
Storage:    SQLite history
Tech stack: Godot 4, GDScript
```

---

## Example 445

**Intent:**
rhythm game about tap dancing, combos of heel and toe keys

**Spec:**
```
Type:       Desktop game (tap dance rhythm)
Data model: Routine(id, song_file, bpm, steps_json)
            Score(routine_id -> Routine, points, grade)
Features:   - Map heel and toe on each foot to four keys
            - Show step patterns scrolling to the beat
            - Score timing per tap and combo
            - Animate the dancer from the player's input
            - Include a freestyle mode that records routines
Storage:    Local JSON
Tech stack: Lua, LÖVE
```

---

## Example 446

**Intent:**
falling words typing game in spanish to practise vocab

**Spec:**
```
Type:       Browser game (vocabulary typing)
Data model: VocabSet(id, topic, pairs)
            Stat(word, correct, missed)
Features:   - Drop English words that must be typed in Spanish
            - Accept answers with or without accents in easy mode
            - Show the right translation on a miss
            - Pick topic sets like food or travel
            - Speed up with streaks
Storage:    Browser localStorage
Tech stack: JavaScript, Phaser 3
```

---

## Example 447

**Intent:**
word puzzle where you swap letters between two words to make two new words

**Spec:**
```
Type:       Mobile game (letter swap puzzle)
Data model: Puzzle(id, word_a, word_b, target_a, target_b, par_swaps)
Features:   - Show two words as tile rows
            - Swap letters between the rows by tapping
            - Check both rows against the dictionary
            - Count swaps against par
            - Offer daily and endless modes
Storage:    On-device storage
Tech stack: Kotlin, Jetpack Compose
```

---

## Example 448

**Intent:**
balloon physics sandbox, attach balloons to stuff and see what floats

**Spec:**
```
Type:       Desktop game (buoyancy sandbox)
Data model: Scene(id, objects_json, wind)
Features:   - Attach helium balloons to objects with strings
            - Simulate lift, weight and wind
            - Pop balloons by clicking
            - Set challenges like lifting a house
            - Save scenes
Storage:    Local JSON scenes
Tech stack: Python, Pymunk, Pygame
```

---

## Example 449

**Intent:**
TD in a garden where you plant flowers that attract bees to sting the slugs

**Spec:**
```
Type:       Desktop game (garden tower defence)
Data model: Plant(id, type, x, y, growth, attraction)
            Pest(id, type, hp, speed)
Features:   - Plant flowers that grow over time into stronger towers
            - Attract bees, ladybirds and birds as attackers
            - Defend vegetable beds from slugs and aphids
            - Water plants to keep them active
            - Unlock seeds by season
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 450

**Intent:**
roguelike where each run is one day in an office and you climb floors to the boss

**Spec:**
```
Type:       Desktop game (office roguelike)
Data model: Floor(number, department, layout_json)
            Coworker(id, type, stamina, attack)
            Run(id, seed, coffee, floor)
Features:   - Generate office floors by department
            - Battle coworkers with turn-based meeting arguments
            - Use coffee as healing
            - Collect office supplies as weapons
            - Reach the CEO floor to win
Storage:    Local save
Tech stack: C#, MonoGame
```

---

## Example 451

**Intent:**
build a railway town in the wild west, lay track and grow stations

**Spec:**
```
Type:       Desktop game (railway town builder)
Data model: Station(id, x, y, size)
            Track(id, from_station_id -> Station, to_station_id -> Station, cost)
            Train(id, route, cargo)
Features:   - Lay track across terrain with slope costs
            - Run trains carrying cattle, ore and passengers
            - Grow towns around busy stations
            - Pay off loans from freight income
            - Deal with robberies on remote lines
Storage:    Local save
Tech stack: Java, libGDX
```

---

## Example 452

**Intent:**
maple syrup farm game, tap trees in spring, boil sap

**Spec:**
```
Type:       Desktop game (sugarbush sim)
Data model: Tree(id, x, y, diameter, taps, sap_today)
            Batch(id, sap_litres, syrup_litres, grade)
Features:   - Tap maple trees and hang buckets
            - Vary sap flow with freezing nights and warm days
            - Boil sap with firewood in the sugar shack
            - Grade syrup by colour
            - Sell at a pancake breakfast event
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 453

**Intent:**
canoe slalom racing through gates on white water

**Spec:**
```
Type:       Desktop game (canoe slalom)
Data model: Course(id, river_file, gates_json)
            Run(course_id -> Course, time_ms, penalties)
Features:   - Paddle left and right with separate keys
            - Simulate river currents and eddies
            - Pass downstream and upstream gates
            - Add penalties for touched or missed gates
            - Record best runs
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 454

**Intent:**
running a tennis academy game, coach juniors and send them to tournaments

**Spec:**
```
Type:       Desktop game (tennis academy management)
Data model: Junior(id, name, age, serve, forehand, backhand, movement, mental)
            Coach(id, name, specialty, salary)
            Tournament(id, name, level, week)
            Result(tournament_id -> Tournament, junior_id -> Junior, round_reached)
Features:   - Assign coaches and training plans to juniors
            - Simulate matches point by point
            - Enter juniors in tournaments by level
            - Earn fees and sponsorships from results
            - Track junior rankings over years
Storage:    SQLite save
Tech stack: C#, Avalonia
```

---

## Example 455

**Intent:**
movie quote trivia for a party where you guess the film, but quotes are made up so no copyright lol, generic genre quotes

**Spec:**
```
Type:       Desktop game (genre guessing party)
Data model: Quote(id, text, genre, era)
            Team(id, name, score)
Features:   - Show invented quotes and ask teams to guess the genre and era
            - Award points for genre and bonus for era
            - Let teams write their own quotes for others to guess
            - Show a scoreboard between rounds
            - Load quote packs from JSON
Storage:    JSON quote packs
Tech stack: JavaScript, Electron
```

---

## Example 456

**Intent:**
game for learning the bones of the body, drag labels onto a skeleton

**Spec:**
```
Type:       Desktop game (anatomy labelling)
Data model: Bone(id, name, region, x, y)
            Attempt(id, region, correct, time_sec)
Features:   - Show a skeleton diagram by region
            - Drag bone labels onto target points
            - Check placements and show corrections
            - Time each region for a best score
            - Offer Latin names in advanced mode
Storage:    Local JSON
Tech stack: Python, PySide6
```

---

## Example 457

**Intent:**
co-op lighthouse puzzle for two where one guides ships and other fixes the lamp machinery

**Spec:**
```
Type:       Desktop game (asymmetric co-op puzzle)
Data model: Night(id, ships_json, malfunctions_json)
            Ship(id, route, arrival_sec, safe)
Features:   - Let one player aim the beam to guide ships past rocks
            - Let the other repair gears, oil and lenses below
            - Dim the beam when machinery breaks
            - Share one keyboard or two gamepads
            - Score nights by ships guided home
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 458

**Intent:**
squad tactics with mountain rescue team, ropes, weather, injured hikers

**Spec:**
```
Type:       Desktop game (rescue tactics)
Data model: Rescuer(id, name, skill, stamina, gear)
            Casualty(id, x, y, injury, time_left)
            Map(id, terrain_json, weather)
Features:   - Move rescuers on a mountain grid with elevation costs
            - Set rope anchors to cross cliffs
            - Treat and stretcher casualties to a helicopter point
            - Worsen weather over turns
            - Score missions by casualties saved
Storage:    Local save
Tech stack: Unity, C#
```

---

## Example 459

**Intent:**
interactive fiction where you're a house cat and the family is moving away

**Spec:**
```
Type:       Browser game (interactive fiction)
Data model: Passage(id, text, choices_json)
            State(hunger, curiosity, trust)
Features:   - Tell the story from the cat's point of view
            - Offer choices like hide, explore or follow
            - Change state values that affect endings
            - Show small illustrations per scene
            - Save progress in the browser
Storage:    Browser localStorage
Tech stack: Twine (SugarCube)
```

---

## Example 460

**Intent:**
puzzle platformer where you swap places with any object you throw

**Spec:**
```
Type:       Desktop game (swap puzzle-platformer)
Data model: Level(id, tilemap_file, objects_json)
Features:   - Throw a marker in an arc
            - Swap positions with the marker or a hit object
            - Use swaps to cross gaps and move crates
            - Keep momentum after swapping
            - Track swaps per level
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 461

**Intent:**
Vocal warm-up app for my singing students that plays scales up and down in semitone steps

**Spec:**
```
Type:       Desktop application (vocal warm-up player)
Data model: Exercise(id, name, pattern_intervals, vowel)
            Routine(id, name, exercise_ids, start_note, end_note)
Features:   - Play exercises on piano sound rising by semitones
            - Set range per voice type
            - Adjust tempo
            - Show the current key on screen
            - Save routines per student
Storage:    JSON routines
Tech stack: C#, WPF, MeltySynth
```

---

## Example 462

**Intent:**
tiny mac menu bar app that shows which keyboard layout is active, I keep typing in the wrong one

**Spec:**
```
Type:       Desktop application (keyboard layout indicator)
Data model: LayoutRule(app_bundle_id, preferred_layout)
Features:   - Show the active input source in the menu bar
            - Flash a large overlay when the layout changes
            - Switch layout automatically per app
            - Cycle layouts with a custom shortcut
Storage:    UserDefaults
Tech stack: Swift, AppKit
```

---

## Example 463

**Intent:**
self-service printing kiosk for a library, pay and release print jobs

**Spec:**
```
Type:       Desktop application (print release kiosk)
Data model: PrintJob(id, user_code, document_name, pages, color, cost, status, submitted_at)
            Account(user_code, balance)
Features:   - Look up queued jobs by library card
            - Show page count and cost per job
            - Deduct balance and release jobs to the printer
            - Delete unreleased jobs after 24 hours
            - Top up balance with a coin acceptor
Storage:    SQLite database
Tech stack: Python, PySide6, CUPS (pycups)
```

---

## Example 464

**Intent:**
rpg session scheduler that finds a night when all 5 players are free, offline on my pc

**Spec:**
```
Type:       Desktop application (session availability finder)
Data model: Player(id, name)
            Availability(player_id -> Player, date, status)
            Session(id, date, confirmed)
Features:   - Enter each player's availability on a month grid
            - Highlight dates when everyone is free
            - Rank dates with one maybe
            - Confirm a session and export an .ics file
            - Remember regular weekly unavailability
Storage:    JSON file
Tech stack: Python, Tkinter, icalendar
```

---

## Example 465

**Intent:**
lab timer board with many named timers at once for incubations

**Spec:**
```
Type:       Desktop application (multi-timer board)
Data model: Timer(id, label, duration_sec, started_at, color, sound)
            Preset(id, label, duration_sec)
Features:   - Run many named countdown timers side by side
            - Start timers from saved presets
            - Alarm with distinct sounds and flashing tiles
            - Keep running after the window closes to the tray
            - Log when each timer was dismissed
Storage:    SQLite log
Tech stack: Go, Fyne
```

---

## Example 466

**Intent:**
rpg weather generator per season and climate for my campaign

**Spec:**
```
Type:       Desktop application (campaign weather generator)
Data model: Climate(id, name, season_tables_json)
            WeatherDay(id, campaign_day, climate_id -> Climate, temperature, precipitation, wind)
Features:   - Generate daily weather from climate and season tables
            - Carry trends from one day to the next
            - Describe effects on travel and visibility
            - Show a week forecast for the GM
            - Edit climate tables
Storage:    JSON files
Tech stack: Python, PySide6
```

---

## Example 467

**Intent:**
ascii art banner maker for my terminal

**Spec:**
```
Type:       Command-line tool (ASCII banner)
Features:   - Render text in figlet-style fonts
            - Add colour gradients with ANSI codes
            - Wrap text to terminal width
            - List and preview available fonts
            - Copy the output to the clipboard
Input:      Text and font name
Tech stack: Go, go-figure, lipgloss
```

---

## Example 468

**Intent:**
platformer for kids about recycling, sort the trash you collect into right bins

**Spec:**
```
Type:       Desktop game (educational platformer)
Data model: Level(id, tilemap_file, items_json)
            Item(id, name, bin_type, fact)
Features:   - Run and jump to collect litter
            - Sort collected items into recycling bins at the end
            - Show facts for wrong sorts
            - Clean up the level's art as litter is collected
            - Award badges per level
Storage:    Local save
Tech stack: C#, MonoGame
```

---

## Example 469

**Intent:**
small racing manager where you tune a go-kart and watch it race

**Spec:**
```
Type:       Desktop game (kart tuning)
Data model: Kart(id, gear_ratio, tyre_pressure, seat_position, weight)
            Track(id, name, corners_json)
            Result(track_id -> Track, kart_id -> Kart, lap_ms)
Features:   - Adjust gear ratio, tyre pressure and seat position
            - Simulate laps with a physics model
            - Show telemetry of speed per corner
            - Compare setups between runs
            - Race a season of tracks
Storage:    Local save
Tech stack: Python, PySide6, NumPy
```

---

## Example 470

**Intent:**
desktop app for an art teacher to plan kiln firings, which pieces in which load, temperatures

**Spec:**
```
Type:       Desktop application (kiln firing log)
Data model: Piece(id, student, class_group, clay_body, glaze, stage)
            Firing(id, date, type, cone, peak_temp_c, program)
            Load(firing_id -> Firing, piece_id -> Piece, shelf)
Features:   - Track pieces from greenware to glaze fired
            - Plan loads by shelf for each firing
            - Record firing schedules and results
            - Notify which pieces are ready for collection
            - Flag pieces with glaze not matching the cone
Storage:    SQLite database
Tech stack: Python, Tkinter
```

---

## Example 471

**Intent:**
church collection counter, count coins and notes for the weekly offering, two people sign

**Spec:**
```
Type:       Desktop application (offering count sheet)
Data model: Count(id, date, service, counter_a, counter_b, total)
            Denomination(count_id -> Count, value, quantity)
            Envelope(count_id -> Count, donor_number, amount, gift_aid)
Features:   - Enter quantities per coin and note
            - Total cash and cheques
            - Record numbered envelope gifts
            - Require two counter names before saving
            - Print a bank paying-in summary
Storage:    SQLite database
Tech stack: C#, WinForms
```

---

## Example 472

**Intent:**
magic tricks practice log for a hobby magician, routines and patter

**Spec:**
```
Type:       Desktop application (magic routine organiser)
Data model: Trick(id, name, category, props, method_notes, difficulty)
            Routine(id, name, trick_ids, patter)
            Performance(id, routine_id -> Routine, date, venue, reaction_notes)
Features:   - Catalogue tricks with method notes
            - Build routines from tricks in order
            - Write patter scripts per routine
            - Log performances and audience reactions
            - Check required props before a show
Storage:    SQLite database
Tech stack: Python, PySide6
```

---

## Example 473

**Intent:**
genealogy duplicate finder, my tree has the same person entered twice in lots of places

**Spec:**
```
Type:       Desktop application (genealogy duplicate merger)
Data model: Person(id, name, birth_date, birth_place, parents)
            Candidate(person_a_id -> Person, person_b_id -> Person, score)
Features:   - Import a GEDCOM file
            - Score possible duplicates by name, dates, places and parents
            - Show candidate pairs side by side
            - Merge records keeping chosen facts and sources
            - Export a cleaned GEDCOM
Storage:    SQLite working database
Tech stack: Python, PySide6, python-gedcom, rapidfuzz
```

---

## Example 474

**Intent:**
caption generator: transcribe a video locally and give me srt

**Spec:**
```
Type:       Desktop application (local auto-captioning)
Data model: Job(id, video_path, language, model_size, status)
            Cue(index, start_ms, end_ms, text)
Features:   - Transcribe audio locally with a speech recognition model
            - Split text into cues of readable length
            - Edit cues with video preview
            - Export SRT and WebVTT
            - Process jobs in a queue
Storage:    Files on disk
Tech stack: Python, faster-whisper, PySide6, FFmpeg
```

---

## Example 475

**Intent:**
word game where you guess a hidden phrase letter by letter, spin a wheel for points, made for my class

**Spec:**
```
Type:       Desktop game (phrase guessing)
Data model: Phrase(id, text, category)
            Team(id, name, score)
Features:   - Spin a wheel to set the value of a guessed letter
            - Reveal all occurrences of a guessed letter
            - Lose the turn on a bankrupt or wrong letter
            - Let the teacher enter phrases by topic
            - Show team scores
Storage:    JSON phrase files
Tech stack: Python, Pygame
```

---

## Example 476

**Intent:**
small orchard game, graft apple trees to make new varieties

**Spec:**
```
Type:       Desktop game (orchard breeding sim)
Data model: Tree(id, variety_id -> Variety, x, y, age, health)
            Variety(id, name, sweetness, crunch, disease_resistance, parent_ids)
Features:   - Plant and prune apple trees
            - Graft scions onto rootstocks
            - Cross varieties to discover new ones with mixed traits
            - Press cider and sell apples
            - Fight scab and frost
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 477

**Intent:**
tool for choir director to make rehearsal tracks, each voice part louder than the others

**Spec:**
```
Type:       Desktop application (rehearsal track maker)
Data model: Score(id, title, musicxml_path, tempo)
            Part(id, score_id -> Score, name, voice)
            Export(id, score_id -> Score, emphasised_part_id -> Part, file_path)
Features:   - Import MusicXML choral scores
            - Render each part with a distinct instrument sound
            - Create one mix per voice part with that part emphasised
            - Add a count-in click
            - Export MP3 files for singers
Storage:    Files on disk
Tech stack: Python, music21, FluidSynth, pydub
```

---

## Example 478

**Intent:**
wedding speech typing teleprompter that scrolls slowly on my laptop

**Spec:**
```
Type:       Desktop application (teleprompter)
Data model: Script(id, title, text, font_size, scroll_speed)
Features:   - Scroll text smoothly at an adjustable speed
            - Mirror text for use with a beam-splitter glass
            - Pause and resume with the spacebar or a clicker
            - Show a reading guide line
            - Remember speed and font per script
Storage:    JSON scripts
Tech stack: JavaScript, Electron
```

---

## Example 479

**Intent:**
game where you're a mail sorter, type the postcode fast to sort letters into bags

**Spec:**
```
Type:       Desktop game (sorting typing)
Data model: Shift(id, letters_count, speed)
            Score(shift_id -> Shift, sorted, missorted)
Features:   - Slide letters with addresses along a conveyor
            - Type the area code to send each letter to a bag
            - Speed up the belt over the shift
            - Penalise wrong bags and dropped letters
            - Rank shifts on a leaderboard
Storage:    Local save
Tech stack: C#, MonoGame
```

---

## Example 480

**Intent:**
classroom timer with visual sand timer and sounds for transitions

**Spec:**
```
Type:       Desktop application (visual classroom timer)
Data model: Preset(id, label, minutes, style, end_sound)
Features:   - Show a full-screen sand timer, bar or clock face
            - Start presets like "tidy up" with one click
            - Play a chosen sound at the end
            - Flash colours in the last minute
            - Float on top of slides in a small mode
Storage:    JSON presets
Tech stack: Python, PySide6
```

---

## Example 481

**Intent:**
cocktail bar game where you mix drinks to the rhythm of the music

**Spec:**
```
Type:       Desktop game (bartending rhythm)
Data model: Recipe(id, name, steps_json)
            Song(id, audio_file, bpm)
            Shift(id, drinks_served, tips)
Features:   - Show orders as recipes of pour, shake and stir steps
            - Perform each step on the beat
            - Mix quality from timing accuracy
            - Earn tips and unlock new recipes
            - Play shifts with faster songs
Storage:    Local save
Tech stack: Godot 4, GDScript
```

---

## Example 482

**Intent:**
desktop app for a karate dojo to track belt gradings and what each student must know for the next belt

**Spec:**
```
Type:       Desktop application (martial arts grading tracker)
Data model: Student(id, name, current_belt, joined_on)
            Belt(id, name, order, requirements_json)
            Grading(id, student_id -> Student, belt_id -> Belt, date, passed, examiner)
Features:   - Show each student's next-belt requirements as a checklist
            - Tick requirements as students demonstrate them
            - List students ready for the next grading
            - Record grading results and print certificates
            - Show time spent at each belt
Storage:    SQLite database
Tech stack: C#, WPF
```

---

