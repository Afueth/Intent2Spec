## Example 1

**Intent:**
baby feeding tracker

**Spec:**
```
Type:       Mobile application (baby log)
Data model: Baby(id, name, birth_date)
            Feeding(id, baby_id -> Baby, type, side, amount_ml, started_at, ended_at)
Features:   - Start and stop a breastfeeding timer per side
            - Log bottle feeds with amount in ml or oz
            - Show time since the last feed on the home screen
            - Show daily totals and a 7-day chart
            - Remind when the next feed is due
Storage:    Local on-device database (SQLite)
Tech stack: Flutter (Android and iOS)
```

---

## Example 2

**Intent:**
My wife and I take turns at night with our newborn and we keep forgetting who changed the last diaper and when. Can we have an app that both our phones see?

**Spec:**
```
Type:       Mobile application with backend (shared baby log)
Auth:       Email login, family group joined by invite code
Data model: Family(id, name, invite_code)
            Caregiver(id, family_id -> Family, name, email)
            DiaperChange(id, family_id -> Family, caregiver_id -> Caregiver, kind, changed_at, note)
Features:   - Log a diaper change as wet, dirty or both in one tap
            - Show who logged the last change and how long ago
            - Sync entries between both parents in real time
            - Show daily wet and dirty counts for the pediatrician
API:        REST
            POST /families/join
            GET  /families/{id}/diapers
            POST /families/{id}/diapers
Storage:    Firebase Firestore
Tech stack: React Native, Firebase Auth, Firestore
```

---

## Example 3

**Intent:**
app to log my baby's milestones like first smile first steps with photos

**Spec:**
```
Type:       Mobile application (milestone journal)
Data model: Child(id, name, birth_date)
            Milestone(id, child_id -> Child, title, category, achieved_on, photo_path, note)
Features:   - Add a milestone with date, photo and note
            - Show the child's age in weeks and months at each milestone
            - Suggest common milestones for the current age range
            - Show a scrollable timeline of all milestones
            - Export the timeline as a PDF photo book
Storage:    Local SQLite database, photos in app storage
Tech stack: Swift, SwiftUI, Core Data
```

---

## Example 4

**Intent:**
pumping log for breast milk, need to know whats in the freezer too

**Spec:**
```
Type:       Mobile application (breast milk log)
Data model: PumpSession(id, started_at, duration_min, left_ml, right_ml)
            MilkBag(id, session_id -> PumpSession, volume_ml, stored_at, location, expires_on, used)
Features:   - Log pumping sessions with volume per side
            - Create freezer bags from a session
            - List stored bags sorted by oldest first
            - Warn when a bag is close to its expiry date
            - Mark bags as used
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 5

**Intent:**
I'm 14 weeks pregnant and I want something simple that tells me how big the baby is this week and lets me write how I'm feeling, nothing with ads or accounts please

**Spec:**
```
Type:       Mobile application (pregnancy tracker)
Data model: Pregnancy(id, due_date)
            WeekInfo(week, size_comparison, development_notes)
            JournalEntry(id, date, mood, symptoms, text)
Features:   - Calculate the current week and days from the due date
            - Show the baby size and development notes for the week
            - Write a daily journal entry with mood and symptoms
            - Show a countdown to the due date
            - Keep all data on the phone with no account
Storage:    Local on-device storage (SQLite), bundled week content as JSON
Tech stack: Flutter, sqflite
```

---

## Example 6

**Intent:**
contraction timer for labor

**Spec:**
```
Type:       Mobile application (contraction timer)
Data model: Contraction(id, started_at, ended_at)
Features:   - Start and stop a contraction with one large button
            - Show duration and interval for each contraction
            - Calculate the average over the last hour
            - Alert when contractions match the 5-1-1 pattern
            - Share the log with a midwife as text
Storage:    Local on-device storage
Tech stack: React Native, AsyncStorage
```

---

## Example 7

**Intent:**
kick counter for pregnancy

**Spec:**
```
Type:       Mobile application (fetal kick counter)
Data model: KickSession(id, started_at, ended_at, kick_count)
Features:   - Count kicks with a tap during a session
            - Stop the session automatically at 10 kicks
            - Show how long it took to reach 10 kicks
            - Show a history of past sessions
            - Remind the user to count at the same time each day
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI
```

---

## Example 8

**Intent:**
My mum is 82 and lives alone. I want her to press one button on her phone every morning to say she's ok, and if she doesn't by 10am I get a message.

**Spec:**
```
Type:       Mobile application with backend (elderly check-in)
Auth:       Phone number login with SMS code
Data model: Senior(id, name, phone, check_in_deadline)
            Contact(id, senior_id -> Senior, name, phone, push_token)
            CheckIn(id, senior_id -> Senior, checked_in_at)
Features:   - Show one large "I'm OK" button on the senior's phone
            - Record each daily check-in with a timestamp
            - Notify contacts by push and SMS when the deadline passes with no check-in
            - Let contacts see the check-in history
            - Let contacts change the deadline time
API:        REST
            POST /checkins
            GET  /seniors/{id}/checkins
            PUT  /seniors/{id}/settings
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Express, Twilio SMS, Firebase Cloud Messaging
```

---

## Example 9

**Intent:**
my dad has parkinsons, want to note his tremors and meds times so I can show the neurologist

**Spec:**
```
Type:       Mobile application (symptom tracker)
Data model: Patient(id, name)
            SymptomLog(id, patient_id -> Patient, symptom, severity, logged_at, note)
            DoseLog(id, patient_id -> Patient, medication, taken_at)
Features:   - Log tremor, stiffness and freezing episodes with a 1-5 severity
            - Log medication doses with time taken
            - Show symptoms and doses together on one daily timeline
            - Highlight "off" periods between doses
            - Export a 30-day report as PDF
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 10

**Intent:**
migraine diary app

**Spec:**
```
Type:       Mobile application (migraine diary)
Data model: Attack(id, started_at, ended_at, pain_level, aura, location)
            Trigger(id, name)
            AttackTrigger(attack_id -> Attack, trigger_id -> Trigger)
            Relief(id, attack_id -> Attack, medication, effective)
Features:   - Log an attack with pain level, aura and pain location
            - Tag possible triggers like sleep, food or weather
            - Record which medication was taken and if it helped
            - Show attacks per month on a calendar
            - Rank triggers by how often they appear before attacks
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, fl_chart
```

---

## Example 11

**Intent:**
i have crohns and want to log food and bathroom trips and pain to find patterns

**Spec:**
```
Type:       Mobile application (IBD symptom tracker)
Data model: Meal(id, eaten_at, foods, note)
            BowelMovement(id, occurred_at, bristol_type, urgency, blood)
            PainLog(id, logged_at, level, location)
Features:   - Log meals with free-text foods
            - Log bowel movements with Bristol stool type and urgency
            - Log abdominal pain with level and location
            - Show a combined daily timeline
            - Highlight foods that often appear within 24 hours before a flare
Storage:    Local on-device database (SQLite)
Tech stack: React Native, WatermelonDB
```

---

## Example 12

**Intent:**
I have bad food allergies (peanuts and sesame). I want to scan a barcode in the shop and get told straight away if the product is safe for me.

**Spec:**
```
Type:       Mobile application (allergen scanner)
Data model: Allergen(id, name, synonyms)
            UserAllergen(allergen_id -> Allergen, severity)
            ScanHistory(id, barcode, product_name, result, scanned_at)
Features:   - Scan product barcodes with the camera
            - Look up ingredients from Open Food Facts
            - Match ingredients and "may contain" warnings against the user's allergens and synonyms
            - Show a green, amber or red result screen
            - Keep a history of scanned products
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, ML Kit Barcode Scanning, Open Food Facts API
```

---

## Example 13

**Intent:**
gluten free scanner for my daughter who has celiac

**Spec:**
```
Type:       Mobile application (gluten checker)
Data model: Product(barcode, name, ingredients, gluten_status, checked_at)
            SafeList(id, barcode, note)
Features:   - Scan a barcode and fetch the ingredient list
            - Flag wheat, barley, rye and malt ingredients
            - Mark products as safe or unsafe for the family
            - Save products to a personal safe list
            - Work offline using cached results
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, mobile_scanner, Open Food Facts API
```

---

## Example 14

**Intent:**
car maintenance log

**Spec:**
```
Type:       Mobile application (vehicle maintenance log)
Data model: Vehicle(id, make, model, year, plate, odometer_km)
            ServiceRecord(id, vehicle_id -> Vehicle, service_type, date, odometer_km, cost, garage, note)
Features:   - Add vehicles with current odometer
            - Log services such as oil change, tyres and brakes
            - Show the next due service by date or mileage
            - Show total maintenance cost per year
            - Attach a photo of each receipt
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 15

**Intent:**
I have an old motorbike and two cars and I always forget when the MOT, tax and insurance are due. Just want reminders for each one.

**Spec:**
```
Type:       Mobile application (vehicle renewal reminders)
Data model: Vehicle(id, name, plate, type)
            Renewal(id, vehicle_id -> Vehicle, kind, due_date, remind_days_before, done)
Features:   - Add vehicles of any type with a name and plate
            - Add renewals like MOT, road tax and insurance with due dates
            - Send a local notification a set number of days before each due date
            - Show all upcoming renewals sorted by date
            - Roll a renewal forward by one year when marked done
Storage:    Local on-device storage (SQLite)
Tech stack: React Native, Notifee (local notifications)
```

---

## Example 16

**Intent:**
fuel log app to calcualte my mpg

**Spec:**
```
Type:       Mobile application (fuel economy log)
Data model: Vehicle(id, name, fuel_type)
            FillUp(id, vehicle_id -> Vehicle, date, odometer, litres, price_per_litre, full_tank)
Features:   - Log each fill-up with odometer, litres and price
            - Calculate consumption between full-tank fill-ups in mpg or L/100km
            - Show monthly fuel spending
            - Chart consumption over time
            - Export fill-ups to CSV
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, Vico charts
```

---

## Example 17

**Intent:**
home maintenance reminders like change the furnace filter, clean gutters, test smoke alarms

**Spec:**
```
Type:       Mobile application (home maintenance scheduler)
Data model: Home(id, name)
            Task(id, home_id -> Home, title, interval_days, season, last_done_on, note)
            Completion(id, task_id -> Task, done_on, cost)
Features:   - Start with a template of common home maintenance tasks
            - Set a repeat interval or season for each task
            - Send a reminder when a task is due
            - Mark tasks done and record the cost
            - Show an overdue list on the home screen
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 18

**Intent:**
Every time something breaks I can never find the receipt or know if it's still under warranty. I want to take a photo of the receipt and have the app tell me when warranty ends.

**Spec:**
```
Type:       Mobile application (warranty and receipt keeper)
Data model: Item(id, name, store, purchase_date, price, warranty_months, category)
            ReceiptImage(id, item_id -> Item, file_path)
Features:   - Photograph receipts and attach them to an item
            - Read store, date and total from the receipt with on-device OCR
            - Calculate the warranty end date
            - Remind one month before warranty expires
            - Search items by name, store or category
Storage:    Local on-device database (SQLite), images in app storage
Tech stack: Kotlin, Jetpack Compose, ML Kit Text Recognition, Room
```

---

## Example 19

**Intent:**
wine tasting notes app

**Spec:**
```
Type:       Mobile application (wine journal)
Data model: Wine(id, name, producer, vintage, region, grape, label_photo)
            TastingNote(id, wine_id -> Wine, tasted_on, rating, aroma, palate, finish, price)
Features:   - Add a wine with a photo of the label
            - Write tasting notes with aroma, palate and finish
            - Rate wines out of 5
            - Filter wines by grape, region or rating
            - Show favourite producers
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Core Data
```

---

## Example 20

**Intent:**
i want to log every coffee i brew, grind size, dose, time, how it tasted, so i can dial in espresso

**Spec:**
```
Type:       Mobile application (espresso brew log)
Data model: Bean(id, roaster, name, roast_date, origin)
            Shot(id, bean_id -> Bean, grind_setting, dose_g, yield_g, time_s, water_temp_c, taste_rating, notes, pulled_at)
Features:   - Log each shot with dose, yield, time and grind setting
            - Calculate the brew ratio automatically
            - Rate taste as sour, balanced or bitter
            - Show the best-rated recipe for each bean
            - Warn when beans are more than 30 days past roast date
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Hive
```

---

## Example 21

**Intent:**
tea collection and steeping timer

**Spec:**
```
Type:       Mobile application (tea journal and timer)
Data model: Tea(id, name, type, vendor, steep_temp_c, steep_time_s, grams_per_cup)
            Session(id, tea_id -> Tea, steeped_at, infusion_count, rating, notes)
Features:   - Store teas with recommended temperature and steep time
            - Start a steeping timer preset for the chosen tea
            - Track multiple infusions with increasing times
            - Rate and note each session
            - Show remaining stock by tea
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Expo Notifications
```

---

## Example 22

**Intent:**
fishing log where i put the spot on map, the fish, weight, bait and the weather

**Spec:**
```
Type:       Mobile application (fishing log)
Data model: Spot(id, name, lat, lng)
            Catch(id, spot_id -> Spot, species, weight_kg, length_cm, bait, caught_at, photo_path, water_temp_c, weather)
Features:   - Save fishing spots on a map with GPS
            - Log catches with species, weight, length and bait
            - Fill in the weather automatically from the current location
            - Show which baits work best per species
            - Keep spots private on the device
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Google Maps SDK, Open-Meteo API
```

---

## Example 23

**Intent:**
rock climbing logbook for routes I send at the gym and outdoors

**Spec:**
```
Type:       Mobile application (climbing logbook)
Data model: Crag(id, name, type, location)
            Route(id, crag_id -> Crag, name, grade, style)
            Ascent(id, route_id -> Route, date, attempt_type, attempts, note)
Features:   - Log ascents as flash, onsight, redpoint or attempt
            - Support both French and V/YDS grades
            - Show the highest grade sent per style
            - Show a pyramid chart of sends by grade
            - Track sessions per week
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Swift Charts
```

---

## Example 24

**Intent:**
I like hiking and I want an app that records my track with GPS even with no signal in the mountains, and shows it on a map I downloaded before.

**Spec:**
```
Type:       Mobile application (offline hiking tracker)
Data model: Hike(id, name, started_at, ended_at, distance_m, elevation_gain_m)
            TrackPoint(id, hike_id -> Hike, lat, lng, altitude, recorded_at)
            MapRegion(id, name, bounds, downloaded_at)
Features:   - Download map tiles for a region before the trip
            - Record a GPS track in the background without network
            - Show distance, elevation gain and time live
            - Show past hikes on the offline map
            - Export tracks as GPX
Storage:    Local on-device database (SQLite), MBTiles for map tiles
Tech stack: Kotlin, Jetpack Compose, MapLibre Native, Fused Location Provider
```

---

## Example 25

**Intent:**
stargazing app that tells me what planets are up tonight

**Spec:**
```
Type:       Mobile application (astronomy guide)
Data model: Observer(lat, lng, timezone)
            CelestialObject(id, name, type, ra, dec)
            Observation(id, object_id -> CelestialObject, observed_at, note)
Features:   - Calculate which planets are above the horizon tonight from the user's location
            - Show rise, set and best viewing times
            - Show moon phase and darkness hours
            - Point the phone at the sky to see object names using the compass
            - Log observations with notes
Storage:    Local on-device storage (SQLite)
Tech stack: Swift, SwiftUI, CoreLocation, CoreMotion, SwiftAA (astronomy calculations)
```

---

## Example 26

**Intent:**
birdwatching list app

**Spec:**
```
Type:       Mobile application (birding life list)
Data model: Species(id, common_name, scientific_name, family)
            Sighting(id, species_id -> Species, seen_at, lat, lng, count, note, photo_path)
Features:   - Search a bundled species list by common or scientific name
            - Log sightings with location, count and photo
            - Keep a life list of species seen at least once
            - Show a yearly list and counts
            - Show sightings on a map
Storage:    Local on-device database (SQLite) with bundled species data
Tech stack: Flutter, sqflite, flutter_map
```

---

## Example 27

**Intent:**
i want to practise spanish verbs conjugation on the bus, fast drills not lessons

**Spec:**
```
Type:       Mobile application (verb conjugation drills)
Data model: Verb(id, infinitive, english, group)
            Conjugation(verb_id -> Verb, tense, person, form)
            Attempt(id, verb_id -> Verb, tense, person, correct, answered_at)
Features:   - Drill random verb and tense combinations with a timed answer
            - Accept answers with or without accents and point out missing accents
            - Choose which tenses to practise
            - Repeat verbs the user gets wrong more often
            - Show accuracy per tense
Storage:    Local on-device database (SQLite) with bundled verb tables
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 28

**Intent:**
music theory trainer for intervals and chords by ear

**Spec:**
```
Type:       Mobile application (ear training)
Data model: Exercise(id, type, difficulty)
            Attempt(id, exercise_type, question, answer, correct, answered_at)
Features:   - Play random intervals and ask the user to name them
            - Play chords and ask for major, minor, diminished or augmented
            - Choose which intervals or chord types to include
            - Show accuracy per interval over time
            - Generate tones with a built-in piano sound
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, AVAudioEngine
```

---

## Example 29

**Intent:**
guitar tuner

**Spec:**
```
Type:       Mobile application (instrument tuner)
Features:   - Capture audio from the microphone
            - Detect the pitch with an autocorrelation algorithm
            - Show the nearest note and how many cents sharp or flat
            - Offer standard and alternate tunings like Drop D and DADGAD
            - Show a needle that turns green when in tune
Tech stack: Kotlin, Android AudioRecord, TarsosDSP
```

---

## Example 30

**Intent:**
metronome app for drum practise with accent on first beat and a tempo trainer that speeds up slowly

**Spec:**
```
Type:       Mobile application (metronome)
Data model: Preset(id, name, bpm, beats_per_bar, subdivision, accent_pattern)
            PracticeLog(id, preset_id -> Preset, minutes, started_at)
Features:   - Play a sample-accurate click at 30-300 BPM
            - Accent the first beat of each bar
            - Support subdivisions like eighths and triplets
            - Increase tempo by a set BPM every N bars
            - Save presets and log practice time
Storage:    Local on-device database (SQLite)
Tech stack: Swift, AVAudioEngine, SwiftUI
```

---

## Example 31

**Intent:**
an app to practise sign language alphabet with the camera checking my hand

**Spec:**
```
Type:       Mobile application (sign language practice)
Data model: Sign(letter, reference_video)
            Attempt(id, letter, recognised_letter, correct, attempted_at)
Features:   - Show a reference video for each fingerspelled letter
            - Detect hand landmarks from the front camera
            - Classify the hand shape against the target letter
            - Give instant feedback when the sign is correct
            - Track which letters need more practice
Storage:    Local on-device storage
Tech stack: Kotlin, CameraX, MediaPipe Hands, TensorFlow Lite
```

---

## Example 32

**Intent:**
I'm losing my sight and want to learn Braille. An app that teaches the letters and quizzes me, it has to work with TalkBack.

**Spec:**
```
Type:       Mobile application (Braille learning)
Data model: BrailleCell(character, dots)
            Lesson(id, title, characters)
            Progress(lesson_id -> Lesson, accuracy, completed_at)
Features:   - Teach Braille letters with dot numbers read aloud
            - Let the user enter dots on a six-key on-screen layout
            - Quiz the user and give spoken feedback
            - Support TalkBack with labelled controls and large touch targets
            - Track progress per lesson
Storage:    Local on-device storage (Room)
Tech stack: Kotlin, Jetpack Compose, Android TextToSpeech
```

---

## Example 33

**Intent:**
colour blind helper - point camera and tell me the colour

**Spec:**
```
Type:       Mobile application (colour identifier)
Features:   - Show a live camera view with a crosshair
            - Name the colour under the crosshair in plain words
            - Speak the colour name aloud on tap
            - Freeze the frame to inspect a still image
            - Offer filters that boost red-green contrast
Tech stack: Swift, AVFoundation, Core Image, AVSpeechSynthesizer
```

---

## Example 34

**Intent:**
unit converter that works offline, cooking and engineering units

**Spec:**
```
Type:       Mobile application (unit converter)
Data model: Unit(id, category, name, symbol, factor_to_base, offset)
            Favourite(id, from_unit_id -> Unit, to_unit_id -> Unit)
Features:   - Convert between units in length, mass, volume, temperature, pressure and energy
            - Include cooking units like cups and tablespoons
            - Convert as the user types
            - Save favourite conversions
            - Work fully offline
Storage:    Local on-device storage (bundled unit table)
Tech stack: Flutter
```

---

## Example 35

**Intent:**
tip calculator that splits the bill and rounds up

**Spec:**
```
Type:       Mobile application (tip calculator)
Data model: Settings(default_tip_percent, round_up, currency)
Features:   - Enter the bill total and choose a tip percentage
            - Split the total between any number of people
            - Round each share up to the nearest whole amount
            - Show tip, total and per-person share
            - Remember the default tip percentage
Storage:    Local on-device storage (UserDefaults)
Tech stack: Swift, SwiftUI
```

---

## Example 36

**Intent:**
We do soil surveys in places with no reception. Need an app to drop points on a map, fill a form for each sample and sync to the office later.

**Spec:**
```
Type:       Mobile application with backend (offline field data collection)
Auth:       Organisation login with email and password
Data model: Project(id, name, area_bounds)
            SamplePoint(id, project_id -> Project, lat, lng, depth_cm, soil_type, moisture, photo_path, collected_by, collected_at, synced)
Features:   - Download project maps for offline use
            - Drop sample points with GPS and a form
            - Attach photos to each sample
            - Queue records offline and sync when connected
            - Resolve conflicts by latest edit time
API:        REST
            GET  /projects
            POST /projects/{id}/samples/batch
Storage:    SQLite on device, PostgreSQL with PostGIS on server
Tech stack: Kotlin, Jetpack Compose, MapLibre, Ktor, PostgreSQL
```

---

## Example 37

**Intent:**
measure rooms with my phone camera for flooring quotes

**Spec:**
```
Type:       Mobile application (AR room measurement)
Data model: Room(id, name, floor_area_m2, perimeter_m, created_at)
            Corner(id, room_id -> Room, x, z, order)
Features:   - Detect the floor plane with AR
            - Place corners by tapping to trace a room outline
            - Calculate floor area and perimeter
            - Add a waste percentage for flooring quotes
            - Export a floor plan sketch with measurements as PDF
Storage:    Local on-device database (Core Data)
Tech stack: Swift, ARKit, RealityKit, SwiftUI
```

---

## Example 38

**Intent:**
recipe scaler, I put a recipe for 4 and it makes it for 10

**Spec:**
```
Type:       Mobile application (recipe scaler)
Data model: Recipe(id, title, servings)
            Ingredient(id, recipe_id -> Recipe, name, quantity, unit)
Features:   - Enter or paste a recipe with servings
            - Scale all ingredient quantities to a new number of servings
            - Convert awkward amounts to sensible units (e.g. 48 tsp to 1 cup)
            - Round to kitchen-friendly fractions
            - Save scaled versions
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 39

**Intent:**
Sunday meal prep planner, which containers go to which day and what to cook first

**Spec:**
```
Type:       Mobile application (meal prep planner)
Data model: Recipe(id, name, portions, prep_minutes, fridge_days)
            PrepPlan(id, week_start)
            PlannedPortion(id, plan_id -> PrepPlan, recipe_id -> Recipe, eat_on, meal)
Features:   - Choose recipes and portions for the week
            - Assign portions to days and meals
            - Warn when a portion would be eaten after its fridge life
            - Order cooking steps so ovens and hobs are used in parallel
            - Generate a combined shopping list
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 40

**Intent:**
home inventory for insurance, photo of each thing and how much it cost

**Spec:**
```
Type:       Mobile application (home inventory)
Data model: Room(id, name)
            Item(id, room_id -> Room, name, brand, serial_number, purchase_price, purchase_date, photo_path)
Features:   - Add items room by room with photos
            - Scan serial numbers with OCR
            - Show the total value per room and for the home
            - Export a full inventory report as PDF for insurers
            - Back up data to a file the user chooses
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, ML Kit Text Recognition
```

---

## Example 41

**Intent:**
we're moving house in 6 weeks, need a checklist by week and to know what's in each box

**Spec:**
```
Type:       Mobile application (moving planner)
Data model: Move(id, move_date, from_address, to_address)
            ChecklistTask(id, move_id -> Move, title, weeks_before, done)
            Box(id, move_id -> Move, label, room, qr_code)
            BoxItem(id, box_id -> Box, name)
Features:   - Generate a week-by-week checklist counting back from the move date
            - Create boxes with a room and printable QR label
            - List the contents of each box
            - Scan a box QR code to see what's inside
            - Search for an item across all boxes
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-camera, expo-print
```

---

## Example 42

**Intent:**
wedding planner app for me and my fiance, guest list, budget, and vendors

**Spec:**
```
Type:       Mobile application with backend (wedding planner)
Auth:       Email login, shared plan for two partners
Data model: Wedding(id, date, venue, total_budget)
            Guest(id, wedding_id -> Wedding, name, side, rsvp, meal_choice, table_no)
            Vendor(id, wedding_id -> Wedding, type, name, phone, cost, deposit_paid)
            Expense(id, wedding_id -> Wedding, category, amount, paid_on)
Features:   - Manage the guest list with RSVP and meal choice
            - Track spending against the budget by category
            - Store vendors with contact details and payment status
            - Show a countdown and task checklist
            - Sync changes between both partners
API:        REST
            GET  /weddings/{id}/guests
            POST /weddings/{id}/guests
            PATCH /guests/{id}
            GET  /weddings/{id}/budget
Storage:    Supabase (PostgreSQL)
Tech stack: Flutter, Supabase
```

---

## Example 43

**Intent:**
chores app for my kids where they get pocket money for each job they do

**Spec:**
```
Type:       Mobile application (kids chores and allowance)
Data model: Child(id, name, avatar, balance)
            Chore(id, title, reward, repeat_days)
            ChoreCompletion(id, chore_id -> Chore, child_id -> Child, done_on, approved)
            Payout(id, child_id -> Child, amount, paid_on)
Features:   - Assign chores to each child with a reward value
            - Let children tick off chores on a shared family tablet
            - Let a parent approve completions with a PIN
            - Add approved rewards to each child's balance
            - Record payouts and show balance history
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Hive
```

---

## Example 44

**Intent:**
pls make an app for car parking where i park in big parking and forget where my car

**Spec:**
```
Type:       Mobile application (parked car finder)
Data model: ParkingSpot(id, lat, lng, level, note, photo_path, parked_at, meter_expires_at)
Features:   - Save the current GPS location when parking
            - Add the level, bay number and a photo
            - Show walking directions back to the car
            - Remind before the parking meter expires
            - Keep a short history of past spots
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, Google Maps SDK
```

---

## Example 45

**Intent:**
I keep a log of my daughter's asthma, puffer use and peak flow readings for her doctor. Would love an app instead of paper.

**Spec:**
```
Type:       Mobile application (child asthma diary)
Data model: Child(id, name, personal_best_lpm)
            PeakFlow(id, child_id -> Child, reading_lpm, measured_at)
            InhalerUse(id, child_id -> Child, inhaler, puffs, used_at, reason)
Features:   - Log peak flow readings morning and evening
            - Colour readings by green, yellow and red zones from personal best
            - Log reliever and preventer inhaler use
            - Chart readings over 4 weeks
            - Export a PDF summary for the doctor
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Swift Charts
```

---

## Example 46

**Intent:**
blood sugar log for type 1 diabetes with insulin doses and carbs

**Spec:**
```
Type:       Mobile application (diabetes log)
Data model: GlucoseReading(id, mg_dl, measured_at, context)
            InsulinDose(id, type, units, given_at)
            CarbEntry(id, grams, eaten_at, description)
Features:   - Log glucose readings with before or after meal context
            - Log bolus and basal insulin doses
            - Log carbohydrates per meal
            - Show time-in-range for the last 14 days
            - Overlay readings, doses and carbs on one chart
Storage:    Local on-device storage, Apple HealthKit
Tech stack: Swift, SwiftUI, HealthKit
```

---

## Example 47

**Intent:**
kid growth chart, height and weight vs the who percentiles

**Spec:**
```
Type:       Mobile application (child growth tracker)
Data model: Child(id, name, sex, birth_date)
            Measurement(id, child_id -> Child, measured_on, height_cm, weight_kg, head_cm)
Features:   - Record height, weight and head circumference
            - Calculate the child's age at each measurement
            - Plot measurements on WHO percentile curves
            - Show the current percentile for each metric
            - Support multiple children
Storage:    Local on-device database (SQLite), bundled WHO tables
Tech stack: Flutter, fl_chart
```

---

## Example 48

**Intent:**
Hello, I am teacher of piano in Poland. I want app where my students record how many minutes they practise every day and I can see it.

**Spec:**
```
Type:       Mobile application with backend (music practice log)
Auth:       Teacher account with email; students join with a class code
Data model: Teacher(id, name, email)
            Student(id, teacher_id -> Teacher, name)
            PracticeSession(id, student_id -> Student, piece, minutes, practised_on, note)
Features:   - Let students start a practice timer and save the session
            - Let students note which piece they practised
            - Show the teacher weekly minutes per student
            - Show a streak to motivate students
            - Let the teacher leave a short comment on a week
API:        REST
            POST /classes/join
            POST /sessions
            GET  /teachers/{id}/students/summary
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express, PostgreSQL
```

---

## Example 49

**Intent:**
an app to check my well water test results over the years

**Spec:**
```
Type:       Mobile application (water quality log)
Data model: Well(id, name, location)
            WaterTest(id, well_id -> Well, tested_on, lab, ph, nitrate_mg_l, coliform_present, hardness_mg_l, iron_mg_l)
Features:   - Record lab test results per parameter
            - Compare each value against drinking water limits
            - Highlight parameters over the limit in red
            - Chart each parameter over the years
            - Remind when the yearly test is due
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 50

**Intent:**
sourdough starter feeding reminder and bake log

**Spec:**
```
Type:       Mobile application (sourdough log)
Data model: Starter(id, name, flour_type, ratio)
            Feeding(id, starter_id -> Starter, fed_at, flour_g, water_g, rise_percent)
            Bake(id, starter_id -> Starter, baked_on, hydration_percent, bulk_hours, rating, photo_path)
Features:   - Log starter feedings with flour and water amounts
            - Remind when the next feeding is due
            - Log bakes with hydration and bulk fermentation time
            - Calculate baker's percentages for a target dough weight
            - Show a photo gallery of past bakes
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Expo Notifications
```

---

## Example 51

**Intent:**
baby sleep log with nap predictions

**Spec:**
```
Type:       Mobile application (infant sleep tracker)
Data model: Baby(id, name, birth_date)
            SleepSession(id, baby_id -> Baby, started_at, ended_at, location)
Features:   - Start and stop naps and night sleep with one tap
            - Calculate total sleep per 24 hours
            - Suggest the next nap time from age-based wake windows
            - Show a 7-day sleep pattern chart
            - Compare totals against typical ranges for the baby's age
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 52

**Intent:**
twins! need to track feeds for two babies at once without mixing them up

**Spec:**
```
Type:       Mobile application (twin feeding log)
Data model: Baby(id, name, colour)
            Feed(id, baby_id -> Baby, method, amount_ml, started_at, ended_at)
Features:   - Show both babies side by side with their own colours
            - Start a feed for one or both babies at the same time
            - Show time since last feed for each twin
            - Show separate daily totals per baby
            - Undo the last entry in case of a wrong tap
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 53

**Intent:**
my son started solids and I want to note every new food and if he had a reaction

**Spec:**
```
Type:       Mobile application (baby food introduction log)
Data model: Food(id, name, allergen_group)
            Introduction(id, food_id -> Food, first_tried_on, reaction, reaction_notes, liked)
Features:   - Log each new food with the date first tried
            - Record reactions like rash or vomiting
            - Flag the top allergens and track exposures to each
            - Suggest waiting 3 days between new allergens
            - Show a list of foods tried and liked
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 54

**Intent:**
vaccine schedule for my kids with reminders

**Spec:**
```
Type:       Mobile application (child vaccination tracker)
Data model: Child(id, name, birth_date, country)
            Vaccine(id, name, due_age_months)
            Dose(id, child_id -> Child, vaccine_id -> Vaccine, given_on, clinic, batch_no)
Features:   - Generate the vaccine schedule from the child's birth date
            - Mark doses as given with clinic and batch number
            - Remind parents two weeks before a dose is due
            - Show overdue vaccines
            - Export the record as a PDF
Storage:    Local on-device database (SQLite), bundled national schedule
Tech stack: React Native, expo-sqlite, Expo Notifications
```

---

## Example 55

**Intent:**
teething tracker which teeth came in when

**Spec:**
```
Type:       Mobile application (baby teeth chart)
Data model: Child(id, name, birth_date)
            Tooth(id, child_id -> Child, position_code, erupted_on, lost_on)
Features:   - Show an interactive mouth diagram of all 20 baby teeth
            - Tap a tooth to record when it came in
            - Show typical eruption ages for each tooth
            - Record when teeth fall out later
            - Show a timeline of tooth events
Storage:    Local on-device storage
Tech stack: Flutter, CustomPainter
```

---

## Example 56

**Intent:**
I'm a single dad with a toddler and I'm terrible at knowing when he last had medicine like calpol for fever, so I don't double dose. Simple thing please.

**Spec:**
```
Type:       Mobile application (child medicine dose timer)
Data model: Child(id, name, weight_kg)
            Medicine(id, name, min_hours_between, max_doses_per_day)
            DoseGiven(id, child_id -> Child, medicine_id -> Medicine, amount_ml, given_at)
Features:   - Log a dose with one tap per medicine
            - Show when the next dose is allowed
            - Block or warn when the daily maximum would be exceeded
            - Log temperature readings next to doses
            - Show the last 48 hours of doses
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI
```

---

## Example 57

**Intent:**
fever log for kids temperatures

**Spec:**
```
Type:       Mobile application (fever tracker)
Data model: Child(id, name, age_months)
            TemperatureReading(id, child_id -> Child, celsius, method, measured_at, note)
Features:   - Log temperatures with method (ear, forehead, underarm)
            - Chart temperature over the illness
            - Show age-based guidance on when to call a doctor
            - Switch between Celsius and Fahrenheit
            - Share the log with a doctor as text
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 58

**Intent:**
potty training app with stickers for my daughter

**Spec:**
```
Type:       Mobile application (potty training chart)
Data model: Child(id, name)
            PottyEvent(id, child_id -> Child, type, success, occurred_at)
            Reward(id, child_id -> Child, sticker, earned_at)
Features:   - Log successes and accidents quickly
            - Award an animated sticker for each success
            - Remind parents to prompt a potty visit every set interval
            - Show a weekly chart of successes
            - Unlock a bigger reward after a set number of stickers
Storage:    Local on-device storage
Tech stack: Flutter, Hive, flutter_local_notifications
```

---

## Example 59

**Intent:**
screen time agreement app between me and my teenager

**Spec:**
```
Type:       Mobile application with backend (family screen time contract)
Auth:       Parent and teen accounts linked by family code
Data model: Family(id, code)
            Member(id, family_id -> Family, role, name)
            Rule(id, family_id -> Family, description, daily_minutes)
            TimeRequest(id, member_id -> Member, extra_minutes, reason, status)
Features:   - Write agreed rules that both sides accept
            - Let the teen request extra time with a reason
            - Let the parent approve or decline requests
            - Log daily usage entered by the teen
            - Show weekly compliance for both to see
API:        REST
            GET  /families/{id}/rules
            POST /requests
            PATCH /requests/{id}
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase Auth, Firestore
```

---

## Example 60

**Intent:**
babysitter info app, emergency numbers allergies bedtime routine all in one place to show the sitter

**Spec:**
```
Type:       Mobile application (babysitter handbook)
Data model: Child(id, name, allergies, bedtime, routine_notes)
            Contact(id, name, role, phone)
            HouseInfo(wifi, alarm_code, first_aid_location)
Features:   - Store each child's allergies, medicines and bedtime routine
            - Store emergency contacts with one-tap calling
            - Generate a share link or PDF for the sitter
            - Hide sensitive fields like alarm codes behind a PIN
            - Keep notes from each sitter visit
Storage:    Local on-device storage (encrypted)
Tech stack: React Native, expo-secure-store, expo-print
```

---

## Example 61

**Intent:**
school lunch planner for 3 kids so nobody gets the same thing twice in a week

**Spec:**
```
Type:       Mobile application (kids lunch planner)
Data model: Child(id, name, dislikes)
            LunchItem(id, name, category)
            Lunchbox(id, child_id -> Child, date, items)
Features:   - Build each child's lunchbox from main, snack and fruit items
            - Avoid repeating a main item in the same week
            - Respect each child's dislikes and allergies
            - Generate a weekly shopping list
            - Copy a good week as a template
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 62

**Intent:**
Hi, my children go to two houses (me and their dad) and we need calendar of which days they are with who. We don't talk much so app is better.

**Spec:**
```
Type:       Mobile application with backend (co-parenting calendar)
Auth:       Email login, two parents linked to a shared family
Data model: Family(id)
            Parent(id, family_id -> Family, name)
            CustodyDay(id, family_id -> Family, date, parent_id -> Parent)
            SwapRequest(id, family_id -> Family, date, requested_by -> Parent, status, message)
            Expense(id, family_id -> Family, description, amount, paid_by -> Parent)
Features:   - Show a colour-coded custody calendar
            - Generate a repeating schedule like week-on week-off
            - Request and approve day swaps
            - Log shared child expenses and split them
            - Keep a timestamped record of all changes
API:        REST
            GET  /families/{id}/calendar
            POST /swaps
            PATCH /swaps/{id}
            POST /expenses
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework, PostgreSQL
```

---

## Example 63

**Intent:**
baby name chooser where me and my partner swipe and see matches

**Spec:**
```
Type:       Mobile application with backend (baby name matcher)
Auth:       Anonymous accounts paired with a partner code
Data model: Name(id, name, gender, origin, meaning)
            Pair(id, code)
            Vote(id, pair_id -> Pair, user_id, name_id -> Name, liked)
Features:   - Swipe right or left on names
            - Filter names by gender, origin and length
            - Show names both partners liked as matches
            - Show the meaning and origin of each name
            - Rank matches with a final head-to-head round
API:        REST
            POST /pairs
            POST /votes
            GET  /pairs/{id}/matches
Storage:    Firebase Firestore
Tech stack: React Native, Firebase
```

---

## Example 64

**Intent:**
hospital bag checklist for pregnancy

**Spec:**
```
Type:       Mobile application (hospital bag checklist)
Data model: Item(id, name, category, for_whom, packed)
Features:   - Start with a ready-made list for mum, baby and partner
            - Tick items as they are packed
            - Add and remove custom items
            - Show progress per bag
            - Remind at 36 weeks if the bag is not ready
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 65

**Intent:**
pregnancy weight gain tracker that shows if im in the healthy range for my bmi

**Spec:**
```
Type:       Mobile application (pregnancy weight tracker)
Data model: Profile(height_cm, pre_pregnancy_weight_kg, due_date, twins)
            WeightEntry(id, weight_kg, measured_on)
Features:   - Calculate pre-pregnancy BMI
            - Show the recommended gain range for each week
            - Log weekly weigh-ins
            - Chart actual gain against the recommended band
            - Keep data private on the device
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, fl_chart
```

---

## Example 66

**Intent:**
blood pressure log for preeclampsia watching, midwife asked me to check twice a day

**Spec:**
```
Type:       Mobile application (pregnancy blood pressure log)
Data model: Reading(id, systolic, diastolic, pulse, measured_at, arm, symptoms)
Features:   - Log readings with systolic, diastolic and pulse
            - Remind morning and evening to take a reading
            - Alert when a reading is 140/90 or higher
            - Log symptoms like headache or swelling
            - Export readings for the midwife
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, WorkManager
```

---

## Example 67

**Intent:**
postpartum mood check in app, short daily questions

**Spec:**
```
Type:       Mobile application (postpartum mood tracker)
Data model: CheckIn(id, date, mood, sleep_hours, anxiety_level, note)
            ScreeningResult(id, taken_on, score)
Features:   - Ask three short questions each day
            - Run the Edinburgh postnatal depression questionnaire monthly
            - Show mood trends over weeks
            - Show helpline numbers when scores are high
            - Keep everything on the device with a passcode
Storage:    Local on-device database (encrypted SQLite)
Tech stack: Swift, SwiftUI, SQLCipher
```

---

## Example 68

**Intent:**
My grandmother has dementia and we have carers coming in. I'd like an app where each carer writes what they did and how she was, and the family can read it.

**Spec:**
```
Type:       Mobile application with backend (care visit log)
Auth:       Email login with family and carer roles
Data model: Client(id, name, care_notes)
            User(id, name, role)
            Visit(id, client_id -> Client, carer_id -> User, arrived_at, left_at, mood, ate, medication_given, notes)
Features:   - Let carers check in and out of each visit
            - Record meals, medication and mood during the visit
            - Let family members read visit notes in a feed
            - Notify family when a visit is missed
            - Store care instructions for carers to read
API:        REST
            POST /visits
            PATCH /visits/{id}
            GET  /clients/{id}/visits
Storage:    PostgreSQL
Tech stack: React Native, NestJS, PostgreSQL
```

---

## Example 69

**Intent:**
simple phone launcher for my elderly father, big buttons for calling family

**Spec:**
```
Type:       Mobile application (senior launcher)
Data model: Contact(id, name, phone, photo_path, position)
Features:   - Replace the home screen with a grid of large photo buttons
            - Call a contact with one tap
            - Show the date, time and battery in large text
            - Lock the layout so it can't be changed by accident
            - Let family edit contacts behind a PIN
Storage:    Local on-device storage
Tech stack: Kotlin, Android (home launcher activity), Jetpack Compose
```

---

## Example 70

**Intent:**
fall detection for my mom, phone in pocket alerts me if she falls

**Spec:**
```
Type:       Mobile application with backend (fall detection)
Auth:       Phone number login for the senior and caregivers
Data model: Senior(id, name, phone)
            Caregiver(id, senior_id -> Senior, phone, push_token)
            FallEvent(id, senior_id -> Senior, detected_at, lat, lng, cancelled)
Features:   - Monitor the accelerometer in the background for a fall pattern
            - Show a 30-second countdown so the senior can cancel false alarms
            - Send caregivers a push and SMS with GPS location
            - Let the senior trigger an SOS manually
            - Keep a history of fall events
API:        REST
            POST /falls
            PATCH /falls/{id}/cancel
            GET  /seniors/{id}/falls
Storage:    PostgreSQL
Tech stack: Kotlin, Android SensorManager, Spring Boot, Twilio
```

---

## Example 71

**Intent:**
hearing aid battery change log

**Spec:**
```
Type:       Mobile application (hearing aid battery tracker)
Data model: Device(id, side, battery_size)
            BatteryChange(id, device_id -> Device, changed_at)
            Stock(battery_size, count)
Features:   - Log battery changes for left and right aids
            - Show the average battery life in days
            - Predict the next change date
            - Track spare battery stock and warn when low
            - Remind to clean the aids weekly
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 72

**Intent:**
app for eczema flares, photo of skin each day and what creams I used

**Spec:**
```
Type:       Mobile application (eczema tracker)
Data model: BodyArea(id, name)
            SkinPhoto(id, area_id -> BodyArea, photo_path, taken_on, itch_level, redness)
            Treatment(id, name, type)
            Application(id, treatment_id -> Treatment, area_id -> BodyArea, applied_at)
Features:   - Take daily photos of affected areas with a guide overlay
            - Rate itch and redness each day
            - Log creams and medications applied per area
            - Compare photos side by side over time
            - Show flare days against treatments on a calendar
Storage:    Local on-device database (SQLite), photos in private app storage
Tech stack: Swift, SwiftUI, AVFoundation, Core Data
```

---

## Example 73

**Intent:**
chronic fatigue spoons tracker, plan my energy for the day

**Spec:**
```
Type:       Mobile application (energy pacing)
Data model: Activity(id, name, spoon_cost)
            DayPlan(id, date, spoons_available)
            PlannedActivity(id, plan_id -> DayPlan, activity_id -> Activity, done)
            Symptom(id, date, fatigue, pain, brain_fog)
Features:   - Set the number of spoons available each morning
            - Plan activities with spoon costs
            - Warn when the plan goes over budget
            - Log symptoms the next day to see post-exertional crashes
            - Show weekly energy use against symptom scores
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 74

**Intent:**
i have POTS, i want to log heart rate lying vs standing and salt and water intake

**Spec:**
```
Type:       Mobile application (POTS symptom log)
Data model: OrthostaticTest(id, tested_at, hr_lying, hr_standing_1min, hr_standing_10min, symptoms)
            IntakeLog(id, date, water_ml, salt_g)
            Episode(id, occurred_at, symptom, severity, trigger)
Features:   - Guide a 10-minute stand test with timers
            - Calculate the heart rate increase from lying to standing
            - Log daily water and salt intake
            - Log dizziness and fainting episodes
            - Read heart rate from a paired Bluetooth strap
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, Android Bluetooth LE
```

---

## Example 75

**Intent:**
pollen and hayfever diary that pulls the pollen count

**Spec:**
```
Type:       Mobile application (hay fever diary)
Data model: DailyLog(id, date, sneezing, itchy_eyes, congestion, antihistamine_taken)
            PollenData(date, grass, tree, weed)
Features:   - Rate symptoms each day on a simple scale
            - Fetch daily pollen counts for the user's location
            - Log antihistamine use
            - Chart symptoms against pollen levels
            - Send a morning alert on high pollen days
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Open-Meteo Air Quality API, sqflite
```

---

## Example 76

**Intent:**
I've got rheumatoid arthritis and the doctor asks every visit which joints hurt. App where I tap the joints on a body picture each day.

**Spec:**
```
Type:       Mobile application (joint pain tracker)
Data model: Joint(id, name, side)
            JointLog(id, joint_id -> Joint, date, pain, swelling, stiffness_minutes)
Features:   - Show a tappable body diagram of joints
            - Record pain and swelling per joint each day
            - Log morning stiffness duration
            - Show a heat map of most affected joints over a month
            - Export a summary for rheumatology appointments
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Core Data
```

---

## Example 77

**Intent:**
epilepsy seizure diary

**Spec:**
```
Type:       Mobile application (seizure diary)
Data model: Seizure(id, occurred_at, duration_s, type, aura, trigger, injuries, witness_note)
            MedChange(id, medication, dose_mg, changed_on)
Features:   - Log seizures with type, duration and possible triggers
            - Start a timer during a seizure for a witness
            - Record medication changes
            - Show seizure frequency per month against medication changes
            - Export the diary for a neurologist
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 78

**Intent:**
food allergy card app that translates my allergies for restaurants abroad

**Spec:**
```
Type:       Mobile application (allergy translation card)
Data model: Allergy(id, name, severity)
            Language(code, name)
            CardText(allergy_id -> Allergy, language_code, text)
Features:   - Choose allergies and severity from a list
            - Generate a restaurant card in the chosen language
            - Include phrases like "even traces can make me very ill"
            - Show the card full screen with large text
            - Work offline with bundled translations
Storage:    Local on-device storage (bundled phrase translations)
Tech stack: Flutter, flutter_localizations
```

---

## Example 79

**Intent:**
epipen expiry reminder for all the pens in the house and school

**Spec:**
```
Type:       Mobile application (auto-injector expiry tracker)
Data model: Pen(id, brand, dose_mg, location, expires_on, lot_number)
Features:   - Add each auto-injector with its location and expiry
            - Scan the expiry date from the box with the camera
            - Remind one month and one week before expiry
            - Show all pens sorted by expiry
            - Link to a video on how to use the pen
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, Vision (text recognition)
```

---

## Example 80

**Intent:**
tyre pressure and tread depth log for my car

**Spec:**
```
Type:       Mobile application (tyre log)
Data model: Vehicle(id, name, recommended_psi_front, recommended_psi_rear)
            TyreCheck(id, vehicle_id -> Vehicle, checked_on, fl_psi, fr_psi, rl_psi, rr_psi, fl_tread_mm, fr_tread_mm, rl_tread_mm, rr_tread_mm)
Features:   - Record pressure and tread depth for each tyre
            - Compare pressures against the recommended values
            - Warn when tread is below the legal limit
            - Remind to check pressures monthly
            - Track tyre rotation dates
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 81

**Intent:**
obd2 app that reads my car error codes over bluetooth and explains them in normal words

**Spec:**
```
Type:       Mobile application (OBD-II diagnostics)
Data model: Vehicle(id, name, vin)
            ScanResult(id, vehicle_id -> Vehicle, scanned_at)
            TroubleCode(id, scan_id -> ScanResult, code, description, severity)
Features:   - Connect to an ELM327 Bluetooth adapter
            - Read stored and pending trouble codes
            - Explain each code in plain language from a bundled database
            - Show live data like RPM and coolant temperature
            - Clear codes after a repair
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Android Bluetooth, Jetpack Compose
```

---

## Example 82

**Intent:**
electric car charging log, cost per kwh at home vs public chargers

**Spec:**
```
Type:       Mobile application (EV charging log)
Data model: Vehicle(id, name, battery_kwh)
            ChargeSession(id, vehicle_id -> Vehicle, location_type, started_at, kwh_added, cost, start_percent, end_percent)
Features:   - Log charging sessions at home or public stations
            - Calculate the cost per kWh and per 100 km
            - Compare home and public charging costs per month
            - Estimate range added per session
            - Export sessions to CSV
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, fl_chart
```

---

## Example 83

**Intent:**
bike maintenance tracker for chain and parts by kms ridden, I use strava

**Spec:**
```
Type:       Mobile application with backend (bicycle component tracker)
Auth:       Strava OAuth login
Data model: Bike(id, strava_gear_id, name)
            Component(id, bike_id -> Bike, type, installed_at_km, service_interval_km)
            ServiceLog(id, component_id -> Component, serviced_on, km, note)
Features:   - Import ride distances from Strava
            - Track kilometres on each component since install
            - Remind when a chain, tyres or brake pads need service
            - Log component replacements
            - Show component wear per bike
API:        REST
            GET  /bikes
            POST /components
            POST /webhooks/strava
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Strava API, PostgreSQL
```

---

## Example 84

**Intent:**
boat maintenance and engine hours log

**Spec:**
```
Type:       Mobile application (boat log)
Data model: Boat(id, name, engine_model)
            EngineHours(id, boat_id -> Boat, reading, recorded_on)
            MaintenanceTask(id, boat_id -> Boat, name, interval_hours, interval_months, last_done_hours, last_done_on)
Features:   - Log engine hour readings
            - Schedule tasks by engine hours or months
            - Show tasks due before the next trip
            - Log winterising and launch checklists
            - Attach part numbers and supplier notes
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 85

**Intent:**
appliance manual keeper, scan the model number and keep the pdf manual

**Spec:**
```
Type:       Mobile application (appliance manual library)
Data model: Appliance(id, name, brand, model_number, room, purchased_on)
            Manual(id, appliance_id -> Appliance, file_path, source_url)
Features:   - Scan the model number label with OCR
            - Attach PDF manuals from files or a download link
            - Open manuals offline in a built-in viewer
            - Group appliances by room
            - Store filter and part numbers for each appliance
Storage:    Local on-device database (SQLite), PDFs in app storage
Tech stack: Kotlin, Jetpack Compose, ML Kit, Android PdfRenderer
```

---

## Example 86

**Intent:**
paint colours app so I remember which paint is on which wall in the house

**Spec:**
```
Type:       Mobile application (home paint record)
Data model: Room(id, name)
            Surface(id, room_id -> Room, name, area_m2)
            PaintRecord(id, surface_id -> Surface, brand, colour_name, colour_code, finish, painted_on, swatch_photo)
Features:   - Record the paint brand, colour code and finish per wall
            - Attach a photo of the paint tin label
            - Calculate litres needed from the wall area and coats
            - Show a colour swatch preview
            - Search by colour name for touch-ups
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, expo-image-picker
```

---

## Example 87

**Intent:**
Our house has a septic tank, a water softener, a boiler and solar panels and I can never remember service dates or who serviced them last. I want contractor phone numbers too.

**Spec:**
```
Type:       Mobile application (home systems service log)
Data model: System(id, name, type, install_date, service_interval_months)
            Contractor(id, name, trade, phone)
            ServiceVisit(id, system_id -> System, contractor_id -> Contractor, visited_on, cost, notes)
Features:   - List home systems with install dates
            - Log each service visit with contractor and cost
            - Calculate the next due service and send reminders
            - Call a contractor directly from the app
            - Show yearly running costs per system
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, url_launcher
```

---

## Example 88

**Intent:**
whisky tasting journal

**Spec:**
```
Type:       Mobile application (whisky journal)
Data model: Bottle(id, distillery, name, age_years, abv, cask_type, region, opened_on, fill_level)
            Dram(id, bottle_id -> Bottle, tasted_on, nose, palate, finish, score)
Features:   - Add bottles with distillery, age and cask
            - Record tasting notes for nose, palate and finish
            - Score each dram out of 100
            - Track how full each open bottle is
            - Filter by region and cask type
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 89

**Intent:**
beer homebrew batch log with gravity readings and abv calc

**Spec:**
```
Type:       Mobile application (homebrew log)
Data model: Recipe(id, name, style, target_og, target_fg)
            Batch(id, recipe_id -> Recipe, brewed_on, volume_l, og, fg, bottled_on)
            GravityReading(id, batch_id -> Batch, gravity, temp_c, read_at)
Features:   - Log batches with original gravity
            - Record gravity readings during fermentation
            - Calculate ABV and apparent attenuation
            - Chart fermentation progress
            - Remind when to dry hop or bottle
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, fl_chart
```

---

## Example 90

**Intent:**
cheese tasting notes with photos, i go to many markets

**Spec:**
```
Type:       Mobile application (cheese journal)
Data model: Cheese(id, name, milk_type, country, producer, texture)
            Tasting(id, cheese_id -> Cheese, tasted_on, where_bought, price_per_kg, rating, notes, photo_path)
Features:   - Log cheeses with milk type, country and texture
            - Add tasting notes with a photo and rating
            - Record where it was bought and the price
            - Show cheeses on a world map by origin
            - Filter by milk type and rating
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, MapKit
```

---

## Example 91

**Intent:**
hunting log with gps of stands and what was seen, needs offline maps

**Spec:**
```
Type:       Mobile application (hunting log)
Data model: Stand(id, name, lat, lng, type)
            Hunt(id, stand_id -> Stand, date, start_time, end_time, wind_direction, temperature)
            Sighting(id, hunt_id -> Hunt, species, count, sex, time_seen)
Features:   - Mark stands and blinds on an offline map
            - Log each hunt with wind and weather
            - Record animal sightings during the hunt
            - Show best stands by wind direction
            - Keep all locations private on the device
Storage:    Local on-device database (SQLite), offline map tiles
Tech stack: Kotlin, Jetpack Compose, MapLibre Native
```

---

## Example 92

**Intent:**
scuba dive log app

**Spec:**
```
Type:       Mobile application (dive log)
Data model: DiveSite(id, name, lat, lng, max_depth_m)
            Dive(id, site_id -> DiveSite, dived_on, max_depth_m, bottom_time_min, start_bar, end_bar, water_temp_c, buddy, visibility_m)
Features:   - Log dives with depth, time and air used
            - Number dives automatically
            - Calculate air consumption rate
            - Show dive sites on a map
            - Let a buddy sign a dive with a finger signature
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, MapKit, PencilKit
```

---

## Example 93

**Intent:**
I want to log the mountains I've climbed. Got a list of the Munros and want to tick them off with the date and who I was with.

**Spec:**
```
Type:       Mobile application (peak bagging list)
Data model: Peak(id, name, height_m, region, lat, lng)
            Ascent(id, peak_id -> Peak, climbed_on, companions, weather, note, photo_path)
Features:   - Include a bundled list of peaks with heights
            - Tick off peaks with date and companions
            - Show climbed and remaining peaks on a map
            - Show progress as a percentage of the list
            - Sort remaining peaks by distance from home
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_map, sqflite
```

---

## Example 94

**Intent:**
moon phase calendar for my fishing and gardening

**Spec:**
```
Type:       Mobile application (moon phase calendar)
Features:   - Calculate the moon phase for any date
            - Show a monthly calendar with phase icons
            - Show moonrise and moonset times for the user's location
            - Highlight full and new moons
            - Send a notification before a full moon
Tech stack: Kotlin, Jetpack Compose, commons-suncalc
```

---

## Example 95

**Intent:**
app tells me when the ISS goes over my house

**Spec:**
```
Type:       Mobile application (satellite pass alerts)
Data model: Location(lat, lng, altitude_m)
            Pass(id, satellite, rise_at, max_elevation_deg, set_at, magnitude)
Features:   - Download the latest ISS orbital elements (TLE)
            - Predict visible passes for the user's location
            - Show the direction to look and the path across the sky
            - Notify 10 minutes before a bright pass
            - Filter passes by minimum elevation
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, CoreLocation, SGP4 orbit propagation library
```

---

## Example 96

**Intent:**
dark sky finder, show light pollution map and cloud forecast for the night

**Spec:**
```
Type:       Mobile application (dark sky planner)
Data model: SavedSite(id, name, lat, lng, bortle_class)
Features:   - Show a light pollution overlay on a map
            - Show hourly cloud cover for tonight at a chosen site
            - Show astronomical twilight and moon interference
            - Save favourite observing sites
            - Rate each night as good, okay or poor
Storage:    Local on-device storage
Tech stack: React Native, react-native-maps, Open-Meteo API
```

---

## Example 97

**Intent:**
bird song recognizer, record a bird and tell me what it is

**Spec:**
```
Type:       Mobile application (bird sound identification)
Data model: Recording(id, file_path, recorded_at, lat, lng)
            Detection(id, recording_id -> Recording, species, confidence, start_s, end_s)
Features:   - Record audio from the microphone
            - Convert audio to spectrograms
            - Classify species with an on-device TensorFlow Lite model
            - Show the top matches with confidence
            - Save recordings with location to a personal list
Storage:    Local on-device database (SQLite), audio files in app storage
Tech stack: Kotlin, TensorFlow Lite, Android AudioRecord, Jetpack Compose
```

---

## Example 98

**Intent:**
bird feeder visit counter for my garden, tap which bird came

**Spec:**
```
Type:       Mobile application (garden bird counter)
Data model: Species(id, name, image)
            Visit(id, species_id -> Species, counted_at, count, feeder)
Features:   - Show a grid of common garden birds with pictures
            - Tap a bird to add a visit
            - Track visits per feeder
            - Show monthly counts per species
            - Export counts for a garden bird survey
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 99

**Intent:**
japanese kana drills

**Spec:**
```
Type:       Mobile application (kana trainer)
Data model: Kana(id, character, romaji, script, row)
            Attempt(id, kana_id -> Kana, correct, response_ms, answered_at)
Features:   - Quiz hiragana and katakana with multiple choice
            - Let the user pick which rows to practise
            - Practise writing kana by tracing with a finger
            - Repeat slow or wrong characters more often
            - Show mastery per row
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, PencilKit
```

---

## Example 100

**Intent:**
chinese tones practise app, it plays a word and I choose the tone

**Spec:**
```
Type:       Mobile application (Mandarin tone trainer)
Data model: Syllable(id, pinyin, tone, audio_path)
            Attempt(id, syllable_id -> Syllable, chosen_tone, correct, answered_at)
Features:   - Play recorded syllables and ask for the tone
            - Practise tone pairs in two-syllable words
            - Record the user's voice and draw the pitch contour
            - Compare the user's contour with the native one
            - Show accuracy per tone
Storage:    Local on-device database (SQLite), bundled audio
Tech stack: Kotlin, Jetpack Compose, TarsosDSP
```

---

## Example 101

**Intent:**
Ich lerne Englisch. I want app for phrasal verbs with example sentences and a game for match them.

**Spec:**
```
Type:       Mobile application (phrasal verb trainer)
Data model: PhrasalVerb(id, verb, particle, meaning, example)
            Review(id, verb_id -> PhrasalVerb, ease, due_on)
Features:   - Show phrasal verbs with meaning and example sentences
            - Play a matching game of verbs and meanings
            - Fill-in-the-gap quizzes from example sentences
            - Schedule reviews with spaced repetition
            - Group verbs by base verb like get, take, put
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 102

**Intent:**
arabic alphabet app showing how letters change shape at start middle and end of a word

**Spec:**
```
Type:       Mobile application (Arabic script trainer)
Data model: Letter(id, name, isolated, initial, medial, final, sound_path)
            Progress(letter_id -> Letter, correct_count, wrong_count)
Features:   - Show the four forms of each letter
            - Play the letter sound
            - Quiz which form fits a position in a word
            - Let the user trace letters right to left
            - Track progress per letter
Storage:    Local on-device storage
Tech stack: React Native, react-native-svg, expo-av
```

---

## Example 103

**Intent:**
language exchange voice diary, i record myself speaking french 1 min every day and listen back

**Spec:**
```
Type:       Mobile application (speaking practice diary)
Data model: Recording(id, recorded_on, prompt, file_path, duration_s, transcript, self_rating)
Features:   - Show a daily speaking prompt
            - Record a one-minute voice clip
            - Transcribe the clip with on-device speech recognition
            - Rate fluency and play old recordings to compare
            - Keep a streak of days practised
Storage:    Local on-device database (SQLite), audio files
Tech stack: Swift, SwiftUI, AVFoundation, Speech framework
```

---

## Example 104

**Intent:**
vocab app that makes flashcards from words I highlight while reading ebooks

**Spec:**
```
Type:       Mobile application (reading vocabulary builder)
Data model: Book(id, title, language)
            Word(id, book_id -> Book, word, context_sentence, translation, added_at)
            Review(id, word_id -> Word, due_on, interval_days)
Features:   - Open EPUB files in a built-in reader
            - Tap a word to see a dictionary translation
            - Save the word with its sentence as context
            - Review saved words with spaced repetition
            - Show words learned per book
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Readium Kotlin toolkit, Room
```

---

## Example 105

**Intent:**
piano chord finder, i press notes and it tells me the chord name

**Spec:**
```
Type:       Mobile application (chord identifier)
Features:   - Show a two-octave on-screen piano keyboard
            - Play notes as keys are tapped
            - Name the chord from the selected notes including inversions
            - Show alternative names for the same chord
            - Show the chord's notes on a staff
Tech stack: Swift, SwiftUI, AudioKit
```

---

## Example 106

**Intent:**
sight reading trainer for treble and bass clef

**Spec:**
```
Type:       Mobile application (sight reading trainer)
Data model: Attempt(id, clef, note, answered_note, correct, response_ms, answered_at)
Features:   - Show random notes on a treble or bass staff
            - Let the user answer on a piano keyboard or note buttons
            - Accept answers from a MIDI keyboard over USB or Bluetooth
            - Increase the range as accuracy improves
            - Show the slowest notes to practise
Storage:    Local on-device storage
Tech stack: Kotlin, Android MIDI API, Jetpack Compose
```

---

## Example 107

**Intent:**
circle of fifths interactive app for my music theory class

**Spec:**
```
Type:       Mobile application (circle of fifths)
Features:   - Draw an interactive circle of fifths
            - Tap a key to show its scale, key signature and relative minor
            - Show the diatonic chords of the selected key
            - Play the scale or chords
            - Quiz key signatures
Tech stack: Flutter, CustomPainter, flutter_midi
```

---

## Example 108

**Intent:**
ukulele chord chart app with strumming patterns

**Spec:**
```
Type:       Mobile application (ukulele chords)
Data model: Chord(id, name, fingering, difficulty)
            StrumPattern(id, name, pattern, bpm)
            Favourite(chord_id -> Chord)
Features:   - Show chord diagrams for ukulele in GCEA tuning
            - Play the chord sound
            - Show strumming patterns with an animated metronome
            - Build a chord sheet for a song
            - Save favourite chords
Storage:    Local on-device storage
Tech stack: React Native, react-native-svg, expo-av
```

---

## Example 109

**Intent:**
drum practise app that listens and tells me if im early or late on the beat

**Spec:**
```
Type:       Mobile application (rhythm accuracy trainer)
Data model: Session(id, bpm, pattern, started_at, avg_offset_ms, accuracy)
Features:   - Play a click at the chosen tempo
            - Detect drum hits from the microphone with onset detection
            - Measure each hit's offset in milliseconds from the beat
            - Show a timing graph of early and late hits
            - Save session accuracy over time
Storage:    Local on-device database (SQLite)
Tech stack: Swift, AVAudioEngine, Accelerate (vDSP)
```

---

## Example 110

**Intent:**
vocal range tester and pitch practice for singing

**Spec:**
```
Type:       Mobile application (vocal pitch trainer)
Data model: RangeTest(id, lowest_note, highest_note, tested_on)
            Exercise(id, name, notes)
            Attempt(id, exercise_id -> Exercise, accuracy, attempted_at)
Features:   - Find the lowest and highest note the user can sing
            - Show the voice type such as alto or tenor
            - Play target notes and show live pitch on a graph
            - Score how closely the user matches each note
            - Track range changes over time
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, TarsosDSP, Jetpack Compose
```

---

## Example 111

**Intent:**
setlist app for my band gigs with song keys and tempos

**Spec:**
```
Type:       Mobile application (band setlist manager)
Data model: Song(id, title, key, bpm, duration_s, notes)
            Setlist(id, name, gig_date, venue)
            SetlistItem(id, setlist_id -> Setlist, song_id -> Song, position)
Features:   - Store songs with key, tempo and notes
            - Build setlists by dragging songs into order
            - Show total set length
            - Show a large-text stage view with the next song
            - Flash a tempo light for the count-in
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 112

**Intent:**
Can you make an Android app that reads text from photos and reads it out loud for someone with low vision? Like menus and letters.

**Spec:**
```
Type:       Mobile application (text reader for low vision)
Features:   - Capture text from the camera with on-device OCR
            - Read recognised text aloud with adjustable speed
            - Show text in large high-contrast font
            - Guide the user with audio cues when text is cut off at the edge
            - Save scanned documents for later listening
Storage:    Local on-device storage
Tech stack: Kotlin, CameraX, ML Kit Text Recognition, Android TextToSpeech
```

---

## Example 113

**Intent:**
magnifier app with flashlight and freeze frame

**Spec:**
```
Type:       Mobile application (digital magnifier)
Features:   - Show a live camera view with pinch zoom up to 10x
            - Turn on the flashlight from the same screen
            - Freeze the image to read it steadily
            - Apply high-contrast and inverted colour filters
            - Save frozen images to the gallery
Tech stack: Swift, AVFoundation, Core Image
```

---

## Example 114

**Intent:**
app that vibrates when someone rings the doorbell or a baby cries, for deaf parents

**Spec:**
```
Type:       Mobile application (sound alert for deaf users)
Data model: SoundEvent(id, type, detected_at, confidence)
            AlertSetting(type, vibration_pattern, flash_enabled)
Features:   - Listen continuously with the microphone in the background
            - Classify sounds like doorbell, baby crying and smoke alarm
            - Vibrate with a pattern per sound type
            - Flash the screen and camera light
            - Show a history of detected sounds
Storage:    Local on-device storage
Tech stack: Kotlin, TensorFlow Lite (YAMNet), Android foreground service
```

---

## Example 115

**Intent:**
live captions app for conversations, text big on the screen

**Spec:**
```
Type:       Mobile application (live captioning)
Data model: Transcript(id, started_at, text)
Features:   - Transcribe speech live with on-device recognition
            - Show captions in large adjustable text
            - Flip the text so the other person can read it too
            - Save transcripts with a timestamp
            - Let the user type replies shown full screen
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, Speech framework
```

---

## Example 116

**Intent:**
aac app for my nonverbal son, picture buttons that speak

**Spec:**
```
Type:       Mobile application (AAC communication board)
Data model: Board(id, name, grid_size)
            Symbol(id, board_id -> Board, label, image_path, spoken_text, position, links_to_board_id)
Features:   - Show a grid of picture symbols that speak when tapped
            - Build sentences in a message bar
            - Link symbols to sub-boards like food or feelings
            - Let parents add photos and record custom voices
            - Lock editing behind a parent PIN
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_tts, sqflite
```

---

## Example 117

**Intent:**
dyslexia friendly reading app with special font and line focus

**Spec:**
```
Type:       Mobile application (dyslexia reading aid)
Data model: Document(id, title, text, last_position)
            Settings(font, letter_spacing, line_height, tint_colour)
Features:   - Import text from files, links or the camera
            - Display text in a dyslexia-friendly font with adjustable spacing
            - Highlight one line at a time with a reading ruler
            - Read text aloud with word highlighting
            - Apply a coloured overlay tint
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-speech, expo-sqlite
```

---

## Example 118

**Intent:**
colour contrast checker for designers, point camera at two colours

**Spec:**
```
Type:       Mobile application (colour contrast checker)
Features:   - Pick two colours from the camera or a photo
            - Show the hex codes of both colours
            - Calculate the WCAG contrast ratio
            - Show pass or fail for AA and AAA text sizes
            - Simulate how the pair looks with protanopia and deuteranopia
Tech stack: Kotlin, CameraX, Jetpack Compose
```

---

## Example 119

**Intent:**
currency converter that works on the plane with last saved rates

**Spec:**
```
Type:       Mobile application (offline currency converter)
Data model: Rate(currency_code, rate_to_usd, updated_at)
            Favourite(id, from_code, to_code)
Features:   - Fetch exchange rates when online
            - Cache rates for offline use and show their age
            - Convert as the user types
            - Show several currencies at once
            - Save favourite currency pairs
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, Frankfurter API
```

---

## Example 120

**Intent:**
shoe and clothing size converter us uk eu

**Spec:**
```
Type:       Mobile application (size converter)
Features:   - Convert shoe sizes between US, UK, EU and JP for men, women and kids
            - Convert clothing sizes for tops, trousers and dresses
            - Save the user's own sizes for each system
            - Show a size chart for selected brands
            - Work fully offline
Storage:    Local on-device storage
Tech stack: Flutter
```

---

## Example 121

**Intent:**
cooking converter cups to grams, depends on the ingredient

**Spec:**
```
Type:       Mobile application (baking measurement converter)
Data model: Ingredient(id, name, grams_per_cup)
Features:   - Convert cups, spoons and ounces to grams per ingredient density
            - Include a list of common baking ingredients
            - Add custom ingredients with their density
            - Convert oven temperatures and gas marks
            - Scale converted amounts by a factor
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 122

**Intent:**
split the restaurant bill by what each person ordered, not evenly

**Spec:**
```
Type:       Mobile application (itemised bill splitter)
Data model: Bill(id, created_at, tax, tip_percent)
            Person(id, bill_id -> Bill, name)
            Item(id, bill_id -> Bill, name, price)
            ItemShare(item_id -> Item, person_id -> Person)
Features:   - Scan the receipt and read items with OCR
            - Assign each item to one or more people
            - Split tax and tip proportionally
            - Show what each person owes
            - Share the result as a text message
Storage:    Local on-device storage
Tech stack: React Native, react-native-mlkit-ocr
```

---

## Example 123

**Intent:**
tip calculator for when i travel, knows how much to tip in each country

**Spec:**
```
Type:       Mobile application (travel tipping guide)
Data model: Country(code, name, restaurant_tip, taxi_tip, hotel_tip, notes)
Features:   - Detect the current country from location
            - Show tipping customs for restaurants, taxis and hotels
            - Calculate the tip in local currency
            - Let the user pick a country manually
            - Work offline with bundled data
Storage:    Local on-device storage (bundled JSON)
Tech stack: Swift, SwiftUI, CoreLocation
```

---

## Example 124

**Intent:**
I'm a builder. Need a calculator app for concrete, how many bags or cubic metres for a slab or footing.

**Spec:**
```
Type:       Mobile application (concrete calculator)
Data model: Job(id, name, created_at)
            Pour(id, job_id -> Job, shape, length_m, width_m, depth_m, diameter_m, quantity)
Features:   - Calculate volume for slabs, footings, columns and steps
            - Add a waste percentage
            - Convert volume to number of premix bags by bag size
            - Total multiple pours per job
            - Save jobs for quoting
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 125

**Intent:**
stair calculator for carpenters rise run stringer length

**Spec:**
```
Type:       Mobile application (stair calculator)
Features:   - Calculate the number of steps from total rise
            - Calculate riser height and tread depth within building code limits
            - Calculate stringer length and angle
            - Draw a stringer layout with measurements
            - Switch between metric and imperial
Tech stack: Kotlin, Jetpack Compose, Android Canvas
```

---

## Example 126

**Intent:**
electrician app for voltage drop and cable size

**Spec:**
```
Type:       Mobile application (electrical calculator)
Features:   - Calculate voltage drop for a cable length, size and load
            - Suggest the minimum cable size for a circuit
            - Calculate current from power and voltage
            - Support copper and aluminium conductors
            - Keep a history of calculations per job
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 127

**Intent:**
spirit level app plus angle finder for hanging pictures

**Spec:**
```
Type:       Mobile application (level and angle finder)
Features:   - Show a bubble level using the accelerometer
            - Measure angles in degrees with the phone edge
            - Calibrate the sensor on a flat surface
            - Lock the reading with a tap
            - Beep when the phone is perfectly level
Tech stack: Kotlin, Android SensorManager, Jetpack Compose
```

---

## Example 128

**Intent:**
plumber job log with photos before and after and parts used, offline because basements have no signal

**Spec:**
```
Type:       Mobile application (trade job log)
Data model: Customer(id, name, address, phone)
            Job(id, customer_id -> Customer, date, description, hours, status)
            Part(id, job_id -> Job, name, quantity, cost)
            JobPhoto(id, job_id -> Job, path, stage)
Features:   - Create jobs with customer details
            - Take before and after photos
            - Record parts used and hours worked
            - Generate a PDF invoice from the job
            - Work fully offline
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, pdf package
```

---

## Example 129

**Intent:**
tile calculator how many tiles for the bathroom floor and walls

**Spec:**
```
Type:       Mobile application (tile calculator)
Data model: Project(id, name)
            Surface(id, project_id -> Project, name, width_m, height_m, cutout_area_m2)
Features:   - Enter surfaces with dimensions and cut-outs like windows
            - Enter tile size and grout gap
            - Calculate tiles needed with a waste percentage
            - Calculate grout and adhesive quantities
            - Show the number of boxes to buy
Storage:    Local on-device storage
Tech stack: React Native, AsyncStorage
```

---

## Example 130

**Intent:**
an app to scale a cocktail recipe up for a party jug

**Spec:**
```
Type:       Mobile application (cocktail batch calculator)
Data model: Cocktail(id, name, glass)
            Ingredient(id, cocktail_id -> Cocktail, name, ml)
Features:   - Store cocktail recipes in ml or oz
            - Scale a recipe to a number of servings or jug size
            - Add a dilution percentage for batched drinks
            - Show the total alcohol per serving
            - Convert to bottle counts for shopping
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 131

**Intent:**
bread hydration calculator for bakers percentages

**Spec:**
```
Type:       Mobile application (baker's percentage calculator)
Data model: Formula(id, name, flour_g, water_pct, salt_pct, yeast_pct, levain_pct)
Features:   - Enter a formula in baker's percentages
            - Calculate ingredient weights for a target dough weight
            - Account for flour and water in the levain
            - Show final hydration
            - Save formulas
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, DataStore
```

---

## Example 132

**Intent:**
pantry inventory with expiry dates, scan barcode to add

**Spec:**
```
Type:       Mobile application (pantry tracker)
Data model: Product(barcode, name, brand)
            PantryItem(id, barcode -> Product, location, quantity, expires_on, added_on)
Features:   - Scan barcodes to add products
            - Enter expiry dates with a quick date picker
            - Group items by fridge, freezer and cupboard
            - Notify three days before items expire
            - Suggest using soon-to-expire items first
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, mobile_scanner, Open Food Facts API
```

---

## Example 133

**Intent:**
freezer inventory, what's in which drawer

**Spec:**
```
Type:       Mobile application (freezer inventory)
Data model: Freezer(id, name)
            Drawer(id, freezer_id -> Freezer, position)
            FrozenItem(id, drawer_id -> Drawer, name, portions, frozen_on, use_by)
Features:   - Organise items by freezer and drawer
            - Add items with portions and date frozen
            - Take one portion out with a tap
            - Show the oldest items first
            - Search for an item across all freezers
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, Core Data
```

---

## Example 134

**Intent:**
i collect board games and lend them to friends, keep track who has what

**Spec:**
```
Type:       Mobile application (board game collection and lending)
Data model: Game(id, title, bgg_id, players_min, players_max, play_time)
            Friend(id, name, phone)
            Loan(id, game_id -> Game, friend_id -> Friend, lent_on, returned_on)
Features:   - Add games by searching BoardGameGeek
            - Record who borrowed a game and when
            - Remind friends to return games after a set time
            - Filter games by player count and play time
            - Log plays with winners
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, BoardGameGeek XML API
```

---

## Example 135

**Intent:**
vinyl record collection catalog using discogs

**Spec:**
```
Type:       Mobile application (record collection)
Data model: Record(id, discogs_id, artist, title, year, label, format, condition)
            Wishlist(id, discogs_id, artist, title)
Features:   - Scan the barcode to find the release on Discogs
            - Store the media and sleeve condition
            - Show the estimated collection value
            - Keep a wishlist to check in shops
            - Sort by artist, year or label
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Discogs API, Room
```

---

## Example 136

**Intent:**
tool lending log - neighbours keep borrowing my drill

**Spec:**
```
Type:       Mobile application (tool lending tracker)
Data model: Tool(id, name, photo_path, value)
            Borrower(id, name, phone)
            Loan(id, tool_id -> Tool, borrower_id -> Borrower, lent_on, due_on, returned_on)
Features:   - Catalogue tools with photos
            - Log a loan with borrower and due date
            - Send a friendly SMS reminder when overdue
            - Show which tools are out
            - Show lending history per tool
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, url_launcher (SMS)
```

---

## Example 137

**Intent:**
wardrobe app, take pictures of my clothes and plan outfits

**Spec:**
```
Type:       Mobile application (digital wardrobe)
Data model: Garment(id, category, colour, season, photo_path, times_worn)
            Outfit(id, name)
            OutfitItem(outfit_id -> Outfit, garment_id -> Garment)
            WornLog(id, outfit_id -> Outfit, worn_on)
Features:   - Photograph clothes and remove the background
            - Tag items by category, colour and season
            - Build outfits from items
            - Log what was worn each day
            - Show items not worn in 6 months
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Vision (subject lifting), SwiftData
```

---

## Example 138

**Intent:**
house moving app, take photo of each box contents and print label

**Spec:**
```
Type:       Mobile application (moving box tracker)
Data model: Box(id, number, room, fragile, photo_path)
            Item(id, box_id -> Box, name)
Features:   - Create numbered boxes with a destination room
            - Photograph box contents
            - Print labels with large numbers and QR codes
            - Mark boxes as delivered and unpacked
            - Search an item to find its box
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, ZXing
```

---

## Example 139

**Intent:**
change of address checklist when moving, banks, doctor, etc

**Spec:**
```
Type:       Mobile application (change of address checklist)
Data model: Organisation(id, name, category, website, phone)
            Notification(id, organisation_id -> Organisation, notified_on, method, confirmed)
Features:   - Start with a list of common organisations to notify
            - Add custom organisations
            - Mark each as notified with the method used
            - Open the website or phone number from the app
            - Show what is still left to do
Storage:    Local on-device storage
Tech stack: React Native, AsyncStorage
```

---

## Example 140

**Intent:**
wedding seating chart app, drag guests to tables

**Spec:**
```
Type:       Mobile application (wedding seating planner)
Data model: Table(id, name, shape, seats, x, y)
            Guest(id, name, group, table_id -> Table, seat_no)
            Constraint(id, guest_a -> Guest, guest_b -> Guest, type)
Features:   - Draw the room with round and long tables
            - Drag guests onto seats
            - Mark guests who must or must not sit together
            - Warn when constraints are broken
            - Export the plan as an image for the venue
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 141

**Intent:**
wedding photo collector, guests scan a qr code at the table and upload pics to us

**Spec:**
```
Type:       Mobile application with backend (wedding photo sharing)
Auth:       Couple account with email; guests upload without an account using an event code
Data model: Event(id, couple_id, name, code, date)
            Photo(id, event_id -> Event, storage_key, uploaded_by_name, uploaded_at)
Features:   - Generate a QR code for the event
            - Let guests upload photos from the web or app without signing in
            - Show a live gallery during the reception
            - Let the couple download all photos as a zip
            - Hide photos the couple removes
API:        REST
            POST /events
            POST /events/{code}/photos
            GET  /events/{id}/photos
            DELETE /photos/{id}
Storage:    Amazon S3 (photos), PostgreSQL
Tech stack: React Native, Node.js, Express, AWS S3
```

---

## Example 142

**Intent:**
wedding day timeline app for the bridal party so everyone knows where to be

**Spec:**
```
Type:       Mobile application with backend (wedding day schedule)
Auth:       Magic link email login for the bridal party
Data model: Wedding(id, date)
            Member(id, wedding_id -> Wedding, name, role, phone)
            TimelineItem(id, wedding_id -> Wedding, starts_at, title, location, assigned_role)
Features:   - Show a minute-by-minute timeline for the day
            - Filter the timeline by role like bridesmaid or usher
            - Notify members 15 minutes before their next item
            - Let the planner shift all later items when things run late
            - Show maps to each location
API:        REST
            GET  /weddings/{id}/timeline
            PATCH /timeline/{id}
            POST /weddings/{id}/shift
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase Cloud Messaging, Firestore
```

---

## Example 143

**Intent:**
kids allowance with savings goals, they put money aside for a toy

**Spec:**
```
Type:       Mobile application (kids savings goals)
Data model: Child(id, name, weekly_allowance)
            Transaction(id, child_id -> Child, amount, type, note, created_at)
            Goal(id, child_id -> Child, name, target_amount, saved_amount, image_path)
Features:   - Add the weekly allowance automatically
            - Split money into spend, save and give jars
            - Set a savings goal with a picture
            - Show progress towards each goal
            - Let parents add interest as a reward for saving
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 144

**Intent:**
morning routine checklist for my ADHD kid with pictures and timer

**Spec:**
```
Type:       Mobile application (kids visual routine)
Data model: Routine(id, name, start_time)
            Step(id, routine_id -> Routine, title, icon, minutes, position)
            Run(id, routine_id -> Routine, date, completed_steps)
Features:   - Show routine steps as big picture cards
            - Run a visual countdown timer for each step
            - Celebrate with an animation when the routine is finished
            - Let parents edit steps and icons
            - Track how many mornings were completed
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 145

**Intent:**
knitting row counter

**Spec:**
```
Type:       Mobile application (knitting row counter)
Data model: Project(id, name, pattern_name, yarn, needle_mm)
            Counter(id, project_id -> Project, label, value, repeat_every)
Features:   - Count rows with a large tap target or volume buttons
            - Keep several counters per project like rows and repeats
            - Reset a repeat counter automatically after N rows
            - Attach the pattern PDF and mark the current line
            - Keep the screen awake while counting
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 146

**Intent:**
crochet pattern app where i can highlight the line i'm on in a pdf

**Spec:**
```
Type:       Mobile application (crochet pattern reader)
Data model: Pattern(id, title, file_path, current_page, highlight_y)
            Note(id, pattern_id -> Pattern, page, text)
Features:   - Import PDF patterns
            - Move a highlight bar line by line
            - Keep a stitch counter overlay on top of the pattern
            - Add notes to pages
            - Remember the position in each pattern
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, PDFKit
```

---

## Example 147

**Intent:**
yarn stash catalog so i dont buy more of what i have

**Spec:**
```
Type:       Mobile application (yarn stash)
Data model: Yarn(id, brand, name, weight, fibre, colour, dye_lot, metres_per_skein, skeins, photo_path)
Features:   - Add yarn with photo, weight and fibre
            - Track skeins and total metres
            - Search the stash by weight and colour
            - Check if there is enough yarn for a pattern's metre requirement
            - Mark yarn as used in a project
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 148

**Intent:**
sewing measurements app for my clients, I'm a dressmaker

**Spec:**
```
Type:       Mobile application (tailoring measurements)
Data model: Client(id, name, phone)
            MeasurementSet(id, client_id -> Client, taken_on, bust_cm, waist_cm, hips_cm, inseam_cm, shoulder_cm, sleeve_cm, notes)
            Order(id, client_id -> Client, garment, fabric, due_on, status)
Features:   - Store body measurements per client with dates
            - Compare measurements between fittings
            - Track garment orders and due dates
            - Attach fabric photos to orders
            - Search clients by name
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 149

**Intent:**
woodworking cut list optimizer, I enter the pieces and it tells me how to cut the sheets of plywood

**Spec:**
```
Type:       Mobile application (cut list optimiser)
Data model: Project(id, name, kerf_mm)
            Sheet(id, project_id -> Project, width_mm, height_mm, quantity)
            Piece(id, project_id -> Project, label, width_mm, height_mm, quantity, grain_locked)
Features:   - Enter stock sheet sizes and required pieces
            - Pack pieces onto sheets with a guillotine cutting algorithm
            - Account for saw blade kerf and grain direction
            - Draw a cutting diagram per sheet
            - Show material waste percentage
Storage:    Local on-device storage
Tech stack: Flutter, CustomPainter
```

---

## Example 150

**Intent:**
3d printing log what settings worked for each filament

**Spec:**
```
Type:       Mobile application (3D print log)
Data model: Printer(id, name, nozzle_mm)
            Filament(id, brand, material, colour, spool_weight_g, remaining_g)
            Print(id, printer_id -> Printer, filament_id -> Filament, model_name, nozzle_temp, bed_temp, speed, duration_min, grams_used, result, photo_path)
Features:   - Log prints with temperatures and speed
            - Subtract used grams from the spool
            - Mark prints as success or failure with a reason
            - Show the best settings per filament
            - Warn when a spool is nearly empty
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 151

**Intent:**
film photography roll log, iso, shutter, aperture per shot

**Spec:**
```
Type:       Mobile application (film shot log)
Data model: Camera(id, name)
            Roll(id, camera_id -> Camera, film_stock, iso, exposures, loaded_on, developed_on)
            Frame(id, roll_id -> Roll, number, aperture, shutter, lens, lat, lng, note)
Features:   - Start a roll with film stock and ISO
            - Log each frame's aperture and shutter speed quickly
            - Save the GPS location per frame
            - Mark rolls as developed
            - Export frame data to embed in scanned files
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, CoreLocation
```

---

## Example 152

**Intent:**
exposure calculator and light meter using phone camera

**Spec:**
```
Type:       Mobile application (light meter)
Features:   - Measure scene brightness with the camera as an EV value
            - Calculate shutter speed from a chosen ISO and aperture
            - Lock a value in aperture or shutter priority
            - Apply ND filter stops
            - Show results in standard full stops
Tech stack: Kotlin, CameraX, Jetpack Compose
```

---

## Example 153

**Intent:**
golden hour and blue hour times for photography, with sun direction on a map

**Spec:**
```
Type:       Mobile application (photography sun planner)
Data model: Location(id, name, lat, lng)
Features:   - Calculate sunrise, sunset, golden and blue hour for a date
            - Show sun and moon direction lines on a map
            - Pick any date to plan a shoot
            - Save favourite locations
            - Notify 30 minutes before golden hour
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, MapKit, Solar calculation library
```

---

## Example 154

**Intent:**
darts scorer for 501 with checkout suggestions

**Spec:**
```
Type:       Mobile application (darts scorer)
Data model: Player(id, name)
            Match(id, legs_to_win, started_at)
            Turn(id, match_id -> Match, player_id -> Player, score, darts_thrown, remaining)
Features:   - Keep score for 501 and 301 games
            - Enter each throw on a dartboard keypad
            - Suggest checkouts for scores of 170 and below
            - Calculate three-dart averages
            - Track legs and sets won
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 155

**Intent:**
golf scorecard with stats like fairways and putts, me and 3 friends

**Spec:**
```
Type:       Mobile application (golf scorecard)
Data model: Course(id, name, holes, par_per_hole)
            Round(id, course_id -> Course, played_on)
            PlayerScore(id, round_id -> Round, player_name, hole, strokes, putts, fairway_hit, gir)
Features:   - Enter scores for up to four players per hole
            - Track putts, fairways hit and greens in regulation
            - Calculate net scores with handicaps
            - Show stats across rounds
            - Save courses with par for each hole
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 156

**Intent:**
chess clock app with increment

**Spec:**
```
Type:       Mobile application (chess clock)
Data model: TimeControl(id, name, base_minutes, increment_s, delay_s)
Features:   - Show two large tap areas for each player
            - Support Fischer increment and Bronstein delay
            - Save custom time controls
            - Sound an alert when time runs out
            - Count moves for each player
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 157

**Intent:**
football referee app, timer, cards, goals log on my phone during the match

**Spec:**
```
Type:       Mobile application (referee match log)
Data model: Match(id, home_team, away_team, half_minutes, kicked_off_at)
            Event(id, match_id -> Match, minute, type, team, player_number, note)
Features:   - Run the match clock with added time
            - Log goals, yellow cards, red cards and substitutions
            - Vibrate at the end of each half
            - Show a match report after the final whistle
            - Share the report by email
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 158

**Intent:**
bowling score sheet app

**Spec:**
```
Type:       Mobile application (ten-pin bowling scorer)
Data model: Game(id, played_on, alley)
            Frame(id, game_id -> Game, number, roll1, roll2, roll3, score)
Features:   - Enter pins knocked down per roll
            - Calculate strikes and spares correctly
            - Show the running score per frame
            - Track average across games
            - Show strike and spare percentages
Storage:    Local on-device storage
Tech stack: React Native, AsyncStorage
```

---

## Example 159

**Intent:**
tide times and surf forecast for my local beach

**Spec:**
```
Type:       Mobile application (surf and tide forecast)
Data model: Spot(id, name, lat, lng, best_swell_direction, best_tide)
Features:   - Show tide times and heights for the next 7 days
            - Show swell height, period and direction
            - Show wind speed and direction
            - Rate each hour for surfing based on the spot's preferences
            - Save favourite spots
Storage:    Local on-device storage
Tech stack: Flutter, Open-Meteo Marine API, Stormglass API
```

---

## Example 160

**Intent:**
kayak trip log and a float plan I can send to someone before I go

**Spec:**
```
Type:       Mobile application (paddling float plan)
Data model: Trip(id, launch_point, takeout_point, planned_start, planned_return, people, boat_colour)
            Contact(id, name, phone)
            TrackPoint(id, trip_id -> Trip, lat, lng, recorded_at)
Features:   - Fill in a float plan with route, times and boat description
            - Send the plan to a contact by SMS
            - Record the GPS track during the trip
            - Remind the user to check in at the planned return time
            - Notify the contact if the user does not check in
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Fused Location Provider, WorkManager
```

---

## Example 161

**Intent:**
mushroom foraging journal with spots on map, private

**Spec:**
```
Type:       Mobile application (foraging journal)
Data model: Spot(id, lat, lng, habitat, note)
            Find(id, spot_id -> Spot, species, found_on, quantity_g, photo_path, confidence)
Features:   - Save find locations privately with GPS
            - Log species, quantity and habitat with photos
            - Show which months each spot produced
            - Mark finds as unconfirmed until verified
            - Protect the app with a PIN
Storage:    Local on-device database (encrypted SQLite)
Tech stack: Swift, SwiftUI, MapKit, SQLCipher
```

---

## Example 162

**Intent:**
geocache-like app for my scout group, I hide clues in the park and the kids find them with gps

**Spec:**
```
Type:       Mobile application with backend (scout treasure hunt)
Auth:       Leader account with email; scouts join with a hunt code
Data model: Hunt(id, leader_id, name, code)
            Checkpoint(id, hunt_id -> Hunt, lat, lng, clue, order)
            Team(id, hunt_id -> Hunt, name)
            Visit(id, team_id -> Team, checkpoint_id -> Checkpoint, reached_at)
Features:   - Let leaders place checkpoints on a map with clues
            - Show teams a compass arrow and distance to the next checkpoint
            - Unlock the next clue when a team is within 15 metres
            - Show a live leaderboard to the leader
            - Record finish times
API:        REST
            POST /hunts
            POST /hunts/{code}/teams
            POST /teams/{id}/visits
            GET  /hunts/{id}/leaderboard
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase, geolocator
```

---

## Example 163

**Intent:**
ski days log with resorts and vertical metres, use the phone gps

**Spec:**
```
Type:       Mobile application (ski day tracker)
Data model: Resort(id, name, country)
            SkiDay(id, resort_id -> Resort, date, vertical_m, distance_km, max_speed_kmh, runs)
Features:   - Track runs automatically with GPS and altitude
            - Calculate vertical descent, top speed and run count
            - Log days per resort
            - Show season totals
            - Save battery by lowering GPS frequency on lifts
Storage:    Local on-device database (SQLite)
Tech stack: Swift, CoreLocation, SwiftUI
```

---

## Example 164

**Intent:**
avalanche field observation app for backcountry, record snow pit tests

**Spec:**
```
Type:       Mobile application (snow pit observations)
Data model: Observation(id, lat, lng, elevation_m, aspect, slope_deg, observed_at)
            Layer(id, observation_id -> Observation, top_cm, bottom_cm, hardness, grain_type)
            StabilityTest(id, observation_id -> Observation, type, result, depth_cm)
Features:   - Record location, aspect and slope angle automatically
            - Enter snow layers with hardness and grain type
            - Log stability tests like ECT and CT
            - Draw a snow profile graph
            - Work fully offline and export as CAAML
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 165

**Intent:**
camping gear checklist so I don't forget the tent pegs again

**Spec:**
```
Type:       Mobile application (camping packing list)
Data model: GearItem(id, name, category, weight_g)
            Trip(id, name, type, nights)
            TripItem(trip_id -> Trip, gear_id -> GearItem, packed)
Features:   - Keep a master list of gear
            - Create trip lists from templates like car camping or backpacking
            - Tick items as packed
            - Show total pack weight
            - Copy last trip's list
Storage:    Local on-device database (SQLite)
Tech stack: React Native, WatermelonDB
```

---

## Example 166

**Intent:**
campfire cooking recipes offline

**Spec:**
```
Type:       Mobile application (outdoor cooking recipes)
Data model: Recipe(id, title, method, servings, cook_minutes, ingredients, steps, equipment)
Features:   - Browse recipes by cooking method like dutch oven or foil packet
            - Scale servings for group size
            - Generate a shopping list for chosen recipes
            - Mark favourites
            - Work offline with bundled recipes
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 167

**Intent:**
beekeeping app for hive inspections

**Spec:**
```
Type:       Mobile application (hive inspection log)
Data model: Apiary(id, name, lat, lng)
            Hive(id, apiary_id -> Apiary, name, queen_year, queen_marked)
            Inspection(id, hive_id -> Hive, inspected_on, temperament, brood_frames, queen_seen, eggs_seen, disease_signs, honey_frames, notes)
Features:   - Record inspections per hive with a quick checklist
            - Note queen status, brood and stores
            - Log varroa treatments and honey harvests
            - Remind the next inspection in 7 days
            - Use voice dictation when wearing gloves
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, Android SpeechRecognizer
```

---

## Example 168

**Intent:**
backyard chickens egg counter

**Spec:**
```
Type:       Mobile application (egg production log)
Data model: Hen(id, name, breed, hatched_on)
            EggLog(id, date, count, hen_id -> Hen)
            FeedPurchase(id, date, kg, cost)
Features:   - Log eggs collected each day
            - Optionally record which hen laid
            - Show eggs per week and month
            - Calculate cost per egg from feed purchases
            - Track eggs given away or sold
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 169

**Intent:**
I'm a small sheep farmer. I need to record lambing, ear tag numbers, which ewe had which lamb, weights. Out in the field, so offline.

**Spec:**
```
Type:       Mobile application (sheep flock records)
Data model: Ewe(id, tag_no, breed, born_on)
            Lamb(id, tag_no, ewe_id -> Ewe, born_on, sex, birth_weight_kg)
            Weighing(id, lamb_id -> Lamb, weighed_on, weight_kg)
            Treatment(id, animal_tag, product, dose, treated_on, withdrawal_until)
Features:   - Record lambings with ewe, sex and birth weight
            - Read ear tags with a Bluetooth EID reader
            - Log weighings and calculate daily weight gain
            - Log treatments with withdrawal periods
            - Work offline and export records to CSV
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, Android Bluetooth
```

---

## Example 170

**Intent:**
spray log for farm fields, chemical, rate, weather

**Spec:**
```
Type:       Mobile application (crop spray record)
Data model: Field(id, name, area_ha, crop)
            Product(id, name, active_ingredient, harvest_interval_days)
            SprayRecord(id, field_id -> Field, product_id -> Product, rate_per_ha, sprayed_on, wind_kmh, temp_c, operator)
Features:   - Record each spray with product, rate and operator
            - Fill wind and temperature automatically from a weather API
            - Calculate total product used per field
            - Show the earliest safe harvest date
            - Export records for compliance audits
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, Open-Meteo API
```

---

## Example 171

**Intent:**
ham radio contact logbook

**Spec:**
```
Type:       Mobile application (amateur radio logbook)
Data model: Contact(id, callsign, frequency_mhz, mode, rst_sent, rst_received, contacted_at, grid_square, name, note)
Features:   - Log contacts with frequency, mode and signal reports
            - Use UTC time automatically
            - Look up callsign details online
            - Show contacts on a world map by grid square
            - Export the log in ADIF format
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, QRZ XML API
```

---

## Example 172

**Intent:**
drone flight log with battery cycles

**Spec:**
```
Type:       Mobile application (drone flight log)
Data model: Drone(id, model, registration_no)
            Battery(id, label, cycles)
            Flight(id, drone_id -> Drone, battery_id -> Battery, started_at, duration_min, lat, lng, max_altitude_m, purpose)
Features:   - Log flights with location and duration
            - Track cycles per battery
            - Show total flight hours per drone
            - Show a pre-flight checklist
            - Export the log for licensing records
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 173

**Intent:**
model rocket launch log and altitude predictor

**Spec:**
```
Type:       Mobile application (model rocketry log)
Data model: Rocket(id, name, mass_g, diameter_mm, cd)
            Motor(id, designation, total_impulse_ns, burn_time_s)
            Launch(id, rocket_id -> Rocket, motor_id -> Motor, launched_on, altitude_m, recovered)
Features:   - Store rockets and motors
            - Predict apogee from mass, drag and motor thrust
            - Log actual altitude and recovery outcome
            - Compare predicted and actual altitudes
            - Show a pre-launch safety checklist
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 174

**Intent:**
coin collection app

**Spec:**
```
Type:       Mobile application (coin collection)
Data model: Coin(id, country, denomination, year, mint_mark, grade, purchase_price, photo_front, photo_back)
            Album(id, name)
Features:   - Add coins with front and back photos
            - Record grade and purchase price
            - Group coins into albums
            - Show gaps in a set by year
            - Show total collection value
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 175

**Intent:**
lego sets i own and the ones i want, check missing pieces

**Spec:**
```
Type:       Mobile application (LEGO collection manager)
Data model: Set(id, set_number, name, year, pieces, owned, built)
            MissingPart(id, set_id -> Set, part_number, colour, quantity)
Features:   - Search sets by number using the Rebrickable API
            - Mark sets as owned, wanted or built
            - Record missing parts per set
            - Show the total piece count owned
            - Export missing parts as a list
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Rebrickable API
```

---

## Example 176

**Intent:**
comic book collection with issue numbers so i know which ones im missing

**Spec:**
```
Type:       Mobile application (comic collection)
Data model: Series(id, title, publisher, start_year)
            Issue(id, series_id -> Series, number, cover_date, owned, condition, price_paid)
Features:   - Add series and their issues
            - Mark issues as owned with condition
            - Show missing issues per series
            - Scan comic barcodes to add issues
            - Show a want list for shopping
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, VisionKit barcode scanner
```

---

## Example 177

**Intent:**
stamp album app

**Spec:**
```
Type:       Mobile application (stamp collection)
Data model: Country(id, name)
            Stamp(id, country_id -> Country, catalogue_no, year, face_value, colour, used, condition, photo_path)
Features:   - Catalogue stamps by country and year
            - Record mint or used and condition
            - Photograph stamps with a crop guide
            - Show completeness per country
            - Search by catalogue number
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, image_cropper
```

---

## Example 178

**Intent:**
trading card scanner to price my pokemon cards

**Spec:**
```
Type:       Mobile application with backend (trading card price tracker)
Auth:       Email login
Data model: Card(id, set_code, number, name, rarity)
            OwnedCard(id, user_id, card_id -> Card, condition, quantity)
            PricePoint(id, card_id -> Card, price, recorded_on)
Features:   - Recognise a card from a photo by its set code and number
            - Fetch current market prices
            - Track collection value over time
            - Alert when a card's price moves more than 20%
            - Export the collection to CSV
API:        REST
            POST /cards/recognise
            GET  /collection
            POST /collection
            GET  /cards/{id}/prices
Storage:    PostgreSQL
Tech stack: Kotlin, ML Kit, FastAPI, PostgreSQL
```

---

## Example 179

**Intent:**
guitar pedal board planner, fits pedals on the board and adds up power draw

**Spec:**
```
Type:       Mobile application (pedalboard planner)
Data model: Pedal(id, name, width_mm, depth_mm, current_ma, voltage)
            Board(id, name, width_mm, depth_mm, power_outputs)
            Placement(board_id -> Board, pedal_id -> Pedal, x, y, rotation)
Features:   - Drag pedals onto a board to scale
            - Warn when pedals overlap or go off the board
            - Add up the total current draw
            - Check pedals against the power supply outputs
            - Save several board layouts
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 180

**Intent:**
hey, i play bass in a cover band and want an app to slow down songs without changing pitch so i can learn the parts

**Spec:**
```
Type:       Mobile application (music practice player)
Data model: Track(id, title, file_path, last_speed)
            LoopMarker(id, track_id -> Track, name, start_ms, end_ms)
Features:   - Import songs from the device
            - Slow down playback without changing pitch
            - Shift pitch by semitones
            - Set A-B loop markers for hard sections
            - Show a waveform for precise looping
Storage:    Local on-device database (SQLite)
Tech stack: Swift, AVAudioEngine (time-pitch unit), SwiftUI
```

---

## Example 181

**Intent:**
piano practise app that shows what notes I played on a midi keyboard as a piano roll

**Spec:**
```
Type:       Mobile application (MIDI practice recorder)
Data model: Recording(id, recorded_at, duration_s)
            NoteEvent(id, recording_id -> Recording, pitch, velocity, start_ms, end_ms)
Features:   - Connect a MIDI keyboard over USB or Bluetooth
            - Record note events with timing and velocity
            - Show recordings as a scrolling piano roll
            - Play recordings back with a built-in piano sound
            - Export recordings as MIDI files
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Android MIDI API, FluidSynth
```

---

## Example 182

**Intent:**
drum machine app for making simple beats on my phone

**Spec:**
```
Type:       Mobile application (step sequencer)
Data model: Pattern(id, name, bpm, steps)
            TrackRow(id, pattern_id -> Pattern, sample, steps_on, volume)
Features:   - Show a 16-step grid per drum sound
            - Play patterns in a loop at the chosen tempo
            - Adjust volume and swing per row
            - Save and load patterns
            - Export the loop as a WAV file
Storage:    Local on-device storage
Tech stack: Swift, AudioKit, SwiftUI
```

---

## Example 183

**Intent:**
theremin app using the phone motion

**Spec:**
```
Type:       Mobile application (motion theremin)
Features:   - Map phone tilt to pitch and roll to volume
            - Generate a continuous sine tone
            - Snap pitch to a chosen scale
            - Show the current note on screen
            - Record and save performances
Tech stack: Kotlin, Android SensorManager, Oboe (audio)
```

---

## Example 184

**Intent:**
hymn book app for our church choir with lyrics offline and the number lookup

**Spec:**
```
Type:       Mobile application (hymnal)
Data model: Hymn(id, number, title, lyrics, tune_name, key)
            Favourite(hymn_id -> Hymn)
            ServiceList(id, date, hymn_numbers)
Features:   - Look up hymns by number on a keypad
            - Search by title or line of lyrics
            - Adjust lyrics font size
            - Save the hymns for each Sunday service
            - Work offline
Storage:    Local on-device database (SQLite, bundled)
Tech stack: Flutter, sqflite
```

---

## Example 185

**Intent:**
prayer times and qibla compass

**Spec:**
```
Type:       Mobile application (prayer times)
Data model: Settings(calculation_method, asr_method, lat, lng)
Features:   - Calculate daily prayer times from location
            - Show a qibla direction compass
            - Notify at each prayer time with an adhan sound
            - Let the user choose the calculation method
            - Show a monthly timetable
Storage:    Local on-device storage
Tech stack: Kotlin, Adhan library, Android SensorManager, Jetpack Compose
```

---

## Example 186

**Intent:**
ivf injection schedule app, so many meds and times

**Spec:**
```
Type:       Mobile application (IVF medication schedule)
Data model: Cycle(id, started_on, clinic)
            Medication(id, cycle_id -> Cycle, name, dose, unit, time_of_day, start_day, end_day)
            Injection(id, medication_id -> Medication, given_at, site)
Features:   - Enter the clinic's medication protocol by cycle day
            - Remind at each injection time with the exact dose
            - Log injections with the body site used
            - Suggest rotating injection sites
            - Show the cycle calendar with scans and egg retrieval
Storage:    Local on-device database (encrypted SQLite)
Tech stack: Swift, SwiftUI, SQLCipher
```

---

## Example 187

**Intent:**
contact lens replacement reminder, monthly lenses and case

**Spec:**
```
Type:       Mobile application (contact lens tracker)
Data model: LensPair(id, type, opened_on, replace_days, left_power, right_power)
            CaseChange(id, changed_on)
Features:   - Log when a new pair is opened
            - Count days worn and remind on replacement day
            - Remind to change the lens case every 3 months
            - Track remaining lens stock
            - Store the prescription
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, DataStore
```

---

## Example 188

**Intent:**
retainer wear timer for my invisalign, need 22 hours a day

**Spec:**
```
Type:       Mobile application (aligner wear tracker)
Data model: Tray(id, number, started_on, days)
            OutOfMouth(id, removed_at, returned_at)
Features:   - Start a timer when aligners are taken out
            - Remind if aligners are out for more than 30 minutes
            - Show daily wear hours against the 22-hour goal
            - Count days on the current tray and remind to switch
            - Keep progress photos per tray
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Expo Notifications
```

---

## Example 189

**Intent:**
physio exercise app my physio can set and I tick off with videos

**Spec:**
```
Type:       Mobile application with backend (home exercise programme)
Auth:       Physio account and patient invite link
Data model: Physio(id, name, email)
            Patient(id, physio_id -> Physio, name)
            Exercise(id, name, video_url, instructions)
            Prescription(id, patient_id -> Patient, exercise_id -> Exercise, sets, reps, per_day)
            Completion(id, prescription_id -> Prescription, done_at, pain_level)
Features:   - Let the physio assign exercises with sets and reps
            - Show the patient a daily list with videos
            - Let the patient tick off sets and rate pain
            - Show the physio adherence per patient
            - Send daily reminders
API:        REST
            GET  /patients/{id}/programme
            POST /completions
            POST /prescriptions
            GET  /physios/{id}/adherence
Storage:    PostgreSQL, video files on S3
Tech stack: Flutter, FastAPI, PostgreSQL, AWS S3
```

---

## Example 190

**Intent:**
wound healing photos for my diabetic foot, same angle each day

**Spec:**
```
Type:       Mobile application (wound photo log)
Data model: Wound(id, location, first_seen_on)
            WoundPhoto(id, wound_id -> Wound, path, taken_on, length_mm, width_mm, pain, drainage)
Features:   - Take photos with a ghost overlay of the last photo for the same angle
            - Record wound size, pain and drainage
            - Compare photos side by side over weeks
            - Chart wound size over time
            - Share a report with the clinic
Storage:    Local on-device storage (encrypted)
Tech stack: Swift, AVFoundation, SwiftUI, CryptoKit
```

---

## Example 191

**Intent:**
hearing test app with tones in each ear

**Spec:**
```
Type:       Mobile application (hearing screening)
Data model: Test(id, taken_on, headphones_model)
            Threshold(id, test_id -> Test, ear, frequency_hz, db_level)
Features:   - Play pure tones at standard frequencies in each ear
            - Raise and lower volume until the user stops hearing it
            - Plot an audiogram for both ears
            - Compare results with earlier tests
            - Warn that results are not a medical diagnosis
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Android AudioTrack, Jetpack Compose
```

---

## Example 192

**Intent:**
tinnitus relief sounds and a log of how loud it is each day

**Spec:**
```
Type:       Mobile application (tinnitus management)
Data model: Sound(id, name, file_path)
            Mix(id, name, sound_volumes)
            LoudnessLog(id, date, loudness, distress, note)
Features:   - Play and mix masking sounds like rain and white noise
            - Tune a notched noise to the user's tinnitus pitch
            - Set a sleep timer
            - Log daily loudness and distress
            - Chart ratings over weeks
Storage:    Local on-device storage
Tech stack: Swift, AVAudioEngine, SwiftUI
```

---

## Example 193

**Intent:**
uv index sunscreen reminder app

**Spec:**
```
Type:       Mobile application (sun protection reminder)
Data model: Settings(skin_type, spf, lat, lng)
            Application(id, applied_at)
Features:   - Fetch the hourly UV index for the user's location
            - Estimate safe sun time from skin type and UV index
            - Remind to reapply sunscreen every 2 hours
            - Log applications
            - Notify in the morning on high UV days
Storage:    Local on-device storage
Tech stack: Flutter, Open-Meteo API, flutter_local_notifications
```

---

## Example 194

**Intent:**
noise level meter for my workplace complaint, record decibels with time

**Spec:**
```
Type:       Mobile application (sound level meter)
Data model: Measurement(id, started_at, duration_s, avg_db, max_db, lat, lng, note)
            Sample(id, measurement_id -> Measurement, db, at_ms)
Features:   - Measure sound level in dB(A) from the microphone
            - Show current, average and maximum levels
            - Record measurements with time and location
            - Calibrate against a reference meter offset
            - Export readings as CSV and PDF
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Android AudioRecord, Jetpack Compose
```

---

## Example 195

**Intent:**
earthquake felt report app using phone sensors, for a science class

**Spec:**
```
Type:       Mobile application (seismometer)
Data model: Recording(id, started_at, duration_s, peak_g)
            Sample(recording_id -> Recording, t_ms, x, y, z)
Features:   - Read the accelerometer at high frequency
            - Draw a live seismograph trace
            - Trigger recording when shaking passes a threshold
            - Show peak acceleration
            - Export samples as CSV for analysis
Storage:    Local on-device storage
Tech stack: Swift, CoreMotion, Swift Charts
```

---

## Example 196

**Intent:**
magnetometer app to find studs and metal in walls

**Spec:**
```
Type:       Mobile application (metal detector)
Features:   - Read the magnetometer continuously
            - Show field strength in microtesla
            - Beep faster as the signal increases
            - Calibrate against the background field
            - Show a graph of the last few seconds
Tech stack: Kotlin, Android SensorManager, Jetpack Compose
```

---

## Example 197

**Intent:**
building site diary for a site manager, weather, workers on site, deliveries, problems

**Spec:**
```
Type:       Mobile application with backend (construction site diary)
Auth:       Company login with email and password
Data model: Site(id, name, address)
            DiaryEntry(id, site_id -> Site, date, weather, author_id)
            Labour(id, entry_id -> DiaryEntry, trade, count)
            Delivery(id, entry_id -> DiaryEntry, supplier, items)
            Issue(id, entry_id -> DiaryEntry, description, photo_path)
Features:   - Create one diary entry per site per day
            - Fill weather automatically
            - Record labour counts by trade and deliveries
            - Log issues with photos
            - Export a weekly PDF report for the client
API:        REST
            GET  /sites/{id}/diary
            POST /sites/{id}/diary
            POST /diary/{id}/issues
Storage:    PostgreSQL, S3 for photos
Tech stack: React Native, Laravel, MySQL, AWS S3
```

---

## Example 198

**Intent:**
punch list app for snagging new houses, photo, pin on floorplan, assign to trade

**Spec:**
```
Type:       Mobile application with backend (snagging list)
Auth:       Email login with contractor and trade roles
Data model: Project(id, name)
            FloorPlan(id, project_id -> Project, image_path, level)
            Snag(id, plan_id -> FloorPlan, x, y, description, photo_path, trade, status, assigned_to)
Features:   - Upload floor plans as images or PDFs
            - Drop pins on the plan for each defect
            - Attach photos and assign a trade
            - Let trades mark snags fixed with a photo
            - Export open snags as a PDF
API:        REST
            GET  /projects/{id}/snags
            POST /snags
            PATCH /snags/{id}
Storage:    PostgreSQL, S3 for images
Tech stack: Flutter, Node.js, PostgreSQL
```

---

## Example 199

**Intent:**
roof pitch and area calculator from measurements

**Spec:**
```
Type:       Mobile application (roofing calculator)
Features:   - Measure roof pitch with the phone tilt sensor
            - Convert pitch between degrees and rise over run
            - Calculate roof area from footprint and pitch
            - Estimate shingles, underlayment and ridge caps
            - Add a waste factor for hips and valleys
Tech stack: Swift, CoreMotion, SwiftUI
```

---

## Example 200

**Intent:**
rebar weight and quantity calculator

**Spec:**
```
Type:       Mobile application (rebar calculator)
Data model: Schedule(id, name)
            BarLine(id, schedule_id -> Schedule, bar_size_mm, length_m, count, shape_code)
Features:   - Enter bar sizes, lengths and counts
            - Calculate total length and weight per bar size
            - Add lap lengths
            - Total a whole bar schedule
            - Export the schedule as a PDF
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 201

**Intent:**
tree survey app for arborists, tag number, species, height, health, gps

**Spec:**
```
Type:       Mobile application (tree survey)
Data model: Survey(id, client, site, surveyed_on)
            Tree(id, survey_id -> Survey, tag_no, species, height_m, dbh_cm, crown_spread_m, condition, risk, recommendation, lat, lng, photo_path)
Features:   - Record trees with GPS, species and measurements
            - Choose condition and risk ratings from lists
            - Recommend works like crown lift or fell
            - Show surveyed trees on an offline map
            - Export a survey table and shapefile
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, MapLibre
```

---

## Example 202

**Intent:**
wildlife transect counts, walk a route and tap species seen with position

**Spec:**
```
Type:       Mobile application (wildlife transect recorder)
Data model: Transect(id, name, route_geojson)
            Walk(id, transect_id -> Transect, started_at, observer, weather)
            Record(id, walk_id -> Walk, species, count, lat, lng, recorded_at)
Features:   - Load predefined transect routes
            - Record the walk's GPS track
            - Tap species buttons to add counts with position
            - Show sections of the route walked
            - Export records as CSV for analysis
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, geolocator, flutter_map
```

---

## Example 203

**Intent:**
archaeology dig finds register, context number, find number, photo, bag labels

**Spec:**
```
Type:       Mobile application (excavation finds register)
Data model: Site(id, code, name)
            Context(id, site_id -> Site, number, type, description)
            Find(id, context_id -> Context, find_no, material, description, photo_path, recorded_by, recorded_at)
Features:   - Register finds against a context
            - Generate find numbers automatically
            - Photograph finds with a scale bar
            - Print bag labels with QR codes over Bluetooth
            - Work offline and export to CSV
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, ZXing
```

---

## Example 204

**Intent:**
Our water company sends me out to read meters in villages. I'd like an app with a list of the meters on my route, I type in the reading, and it warns if the number looks wrong.

**Spec:**
```
Type:       Mobile application with backend (meter reading route)
Auth:       Employee login with company SSO
Data model: Route(id, name, date, reader_id)
            Meter(id, route_id -> Route, serial, address, lat, lng, last_reading)
            Reading(id, meter_id -> Meter, value, read_at, photo_path, note)
Features:   - Download the day's route with meters in order
            - Navigate to each meter on a map
            - Enter readings and warn when consumption is unusually high or low
            - Take a photo of the dial for disputed readings
            - Sync readings when back in coverage
API:        REST
            GET  /routes/today
            POST /readings/batch
Storage:    SQLite on device, SQL Server on backend
Tech stack: Kotlin, Jetpack Compose, ASP.NET Core, SQL Server
```

---

## Example 205

**Intent:**
fire extinguisher inspection app, scan tag, monthly check

**Spec:**
```
Type:       Mobile application with backend (fire equipment inspections)
Auth:       Inspector login with email
Data model: Building(id, name, address)
            Extinguisher(id, building_id -> Building, qr_code, type, location, expires_on)
            Inspection(id, extinguisher_id -> Extinguisher, inspected_at, pressure_ok, seal_ok, accessible, notes, inspector_id)
Features:   - Scan the QR tag on each extinguisher
            - Complete a monthly checklist
            - Flag failed items for replacement
            - Show units due or overdue per building
            - Export inspection records
API:        REST
            GET  /buildings/{id}/extinguishers
            POST /inspections
Storage:    PostgreSQL
Tech stack: React Native, expo-camera, Django REST Framework
```

---

## Example 206

**Intent:**
hey can u make app for my kid to practise times tables, like a game with timer

**Spec:**
```
Type:       Mobile application (times tables practice)
Data model: Attempt(id, a, b, answer, correct, response_ms, answered_at)
            Settings(tables_selected, time_limit_s)
Features:   - Choose which times tables to practise
            - Show quick-fire questions against a timer
            - Reward streaks with stars
            - Repeat facts the child gets wrong
            - Show a grid of mastered facts
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 207

**Intent:**
handwriting practise for my 5 year old, trace letters with finger

**Spec:**
```
Type:       Mobile application (letter tracing)
Data model: Letter(id, character, stroke_paths)
            Practice(id, letter_id -> Letter, accuracy, practised_at)
Features:   - Show letters with numbered stroke order
            - Let the child trace with a finger
            - Check strokes follow the right direction and order
            - Play a sound and animation when done
            - Track which letters need practice
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, PencilKit
```

---

## Example 208

**Intent:**
spelling test practise, teacher gives list each week, app reads word and kid types it

**Spec:**
```
Type:       Mobile application (spelling practice)
Data model: WordList(id, week_of, name)
            Word(id, list_id -> WordList, word, example_sentence)
            Attempt(id, word_id -> Word, typed, correct, attempted_at)
Features:   - Let a parent type in or photograph the weekly list
            - Read each word aloud with an example sentence
            - Let the child type the spelling
            - Show mistakes letter by letter
            - Repeat wrong words at the end
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Android TextToSpeech, ML Kit Text Recognition
```

---

## Example 209

**Intent:**
reading log for my kids school, minutes and books, teacher wants signed

**Spec:**
```
Type:       Mobile application (children's reading log)
Data model: Child(id, name)
            Book(id, title, author, isbn)
            ReadingSession(id, child_id -> Child, book_id -> Book, read_on, minutes, pages, parent_signature)
Features:   - Scan a book's ISBN to add it
            - Log daily reading minutes and pages
            - Capture a parent signature on screen
            - Show weekly totals
            - Export a weekly sheet as PDF for the teacher
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-signature-canvas, expo-print
```

---

## Example 210

**Intent:**
kids birthday party planner, guest list rsvp, party bag, cake order

**Spec:**
```
Type:       Mobile application (kids party planner)
Data model: Party(id, child_name, date, venue, theme, budget)
            Guest(id, party_id -> Party, child_name, parent_phone, rsvp, allergies)
            Task(id, party_id -> Party, title, due_on, done)
Features:   - Track invited children and RSVPs
            - Note allergies for food planning
            - Send reminder texts to parents who haven't replied
            - Keep a task list for cake, bags and decorations
            - Track spending against the budget
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, url_launcher
```

---

## Example 211

**Intent:**
baby shower game app with bingo cards guests play on their phones

**Spec:**
```
Type:       Mobile application with backend (party bingo)
Auth:       Host creates a room; guests join with a 4-letter code
Data model: Room(id, code, host_name, words)
            Player(id, room_id -> Room, name)
            Card(id, player_id -> Player, grid)
            Mark(card_id -> Card, cell)
Features:   - Let the host enter gift words for the bingo
            - Generate a unique card for each guest
            - Let guests mark cells as gifts are opened
            - Detect a bingo and announce the winner to everyone
            - Show the host a live list of players
API:        WebSocket + REST
            POST /rooms
            POST /rooms/{code}/join
            WS   /rooms/{code}
Storage:    Redis
Tech stack: React Native, Node.js, Socket.IO, Redis
```

---

## Example 212

**Intent:**
Je voudrais une application pour suivre les dents de lait de mes enfants et la petite souris, in english please

**Spec:**
```
Type:       Mobile application (tooth fairy tracker)
Data model: Child(id, name)
            LostTooth(id, child_id -> Child, tooth_position, lost_on, amount_given, note, photo_path)
Features:   - Record each lost tooth on a mouth diagram
            - Log the amount left by the tooth fairy
            - Save a photo and a short note
            - Show a timeline per child
            - Remind the parent at bedtime on the day a tooth is lost
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 213

**Intent:**
carpool app for school run with other parents, whose turn to drive

**Spec:**
```
Type:       Mobile application with backend (school carpool rota)
Auth:       Email login, carpool group joined by invite link
Data model: Group(id, name, school)
            Parent(id, group_id -> Group, name, seats)
            Child(id, parent_id -> Parent, name)
            Run(id, group_id -> Group, date, direction, driver_id -> Parent)
Features:   - Generate a fair driving rota from availability
            - Let parents swap runs
            - Notify the driver the night before
            - Show which children are in each car
            - Track drive counts to keep things fair
API:        REST
            GET  /groups/{id}/runs
            POST /runs/{id}/swap
            PUT  /parents/{id}/availability
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase
```

---

## Example 214

**Intent:**
a lost & found app for my kid's daycare where staff post photos of lost items and parents claim them

**Spec:**
```
Type:       Mobile application with backend (daycare lost property)
Auth:       Staff login; parents log in with email linked to the daycare
Data model: Daycare(id, name)
            LostItem(id, daycare_id -> Daycare, photo_path, description, found_on, status)
            Claim(id, item_id -> LostItem, parent_id, claimed_at)
Features:   - Let staff post found items with a photo
            - Show parents a feed of unclaimed items
            - Let parents claim an item
            - Notify staff of claims
            - Archive items unclaimed after 30 days
API:        REST
            GET  /daycares/{id}/items
            POST /items
            POST /items/{id}/claim
Storage:    PostgreSQL, S3 for photos
Tech stack: React Native, Express, PostgreSQL
```

---

## Example 215

**Intent:**
i am nurse doing home visits, i need list of patients for today with address and notes, no internet in some houses

**Spec:**
```
Type:       Mobile application with backend (home visit schedule)
Auth:       Staff login with organisation SSO
Data model: Nurse(id, name)
            Patient(id, name, address, lat, lng, care_notes)
            Visit(id, nurse_id -> Nurse, patient_id -> Patient, scheduled_at, status, notes, arrived_at, left_at)
Features:   - Download today's visits and patient notes for offline use
            - Show visits in route order on a map
            - Record arrival and departure times
            - Write visit notes offline
            - Sync notes when back online
API:        REST
            GET  /nurses/me/visits?date=
            PATCH /visits/{id}
Storage:    Encrypted SQLite on device, PostgreSQL on backend
Tech stack: Kotlin, Jetpack Compose, Room, Spring Boot
```

---

## Example 216

**Intent:**
cpr metronome and step guide for emergencies

**Spec:**
```
Type:       Mobile application (CPR guide)
Features:   - Play a compression beat at 110 per minute
            - Show step-by-step instructions with large text
            - Count cycles of 30 compressions and 2 breaths
            - Call emergency services with one button
            - Work offline and open from a lock screen widget
Tech stack: Swift, SwiftUI, AVFoundation, WidgetKit
```

---

## Example 217

**Intent:**
first aid guide offline for hiking

**Spec:**
```
Type:       Mobile application (offline first aid guide)
Data model: Topic(id, title, category, steps, image_path)
            Favourite(topic_id -> Topic)
Features:   - Browse first aid topics by situation like bleeding, burns or hypothermia
            - Show step-by-step instructions with pictures
            - Search by symptom
            - Store the user's own emergency info
            - Work fully offline
Storage:    Local on-device database (SQLite, bundled)
Tech stack: Flutter, sqflite
```

---

## Example 218

**Intent:**
medical ID app for my son with autism, shows a card if he gets lost

**Spec:**
```
Type:       Mobile application (emergency ID card)
Data model: Profile(name, photo_path, conditions, communication_tips, allergies)
            Contact(id, name, phone, relationship)
Features:   - Show an emergency card from the lock screen
            - Include communication tips for first responders
            - List emergency contacts with one-tap call
            - Share the location by SMS to contacts
            - Keep data on the device only
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, Android lock screen notification
```

---

## Example 219

**Intent:**
caregiver app to share appointment calendar of my mother between me and two brothers

**Spec:**
```
Type:       Mobile application with backend (family care calendar)
Auth:       Email login, family circle by invite
Data model: Circle(id, care_recipient_name)
            Member(id, circle_id -> Circle, name)
            Appointment(id, circle_id -> Circle, title, starts_at, location, driver_id -> Member, notes)
Features:   - Share a calendar of the parent's appointments
            - Volunteer to drive to an appointment
            - Notify everyone of new appointments
            - Add notes after each visit
            - Show unassigned appointments
API:        REST
            GET  /circles/{id}/appointments
            POST /appointments
            PATCH /appointments/{id}
Storage:    Firebase Firestore
Tech stack: React Native, Firebase
```

---

## Example 220

**Intent:**
pill organizer refill reminder for my grandma's weekly pill box

**Spec:**
```
Type:       Mobile application (pill box refill helper)
Data model: Medicine(id, name, strength, slots, pills_per_slot, stock)
            Refill(id, filled_on)
Features:   - Show which pills go in each morning, noon and night slot
            - Remind the caregiver on refill day
            - Subtract pills from stock after each refill
            - Warn when a prescription needs reordering
            - Show a picture of each pill
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 221

**Intent:**
grocery list app with big buttons and voice for my elderly father

**Spec:**
```
Type:       Mobile application (accessible shopping list)
Data model: Item(id, name, done, added_at)
Features:   - Add items by speaking
            - Show items in extra-large text with high contrast
            - Tick items off with a large tap area
            - Read the list aloud
            - Share the list with a family member by message
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, Android SpeechRecognizer
```

---

## Example 222

**Intent:**
a "did i lock the door" app where i take photo when I leave

**Spec:**
```
Type:       Mobile application (leaving-home check)
Data model: Check(id, item, photo_path, taken_at)
Features:   - Show a checklist of things like door, stove and iron
            - Take a photo of each item as proof
            - Show the latest photos when doubt hits later
            - Delete photos older than a day automatically
            - Add a home screen widget for fast access
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, WidgetKit
```

---

## Example 223

**Intent:**
dialysis fluid intake tracker

**Spec:**
```
Type:       Mobile application (dialysis fluid tracker)
Data model: Settings(daily_fluid_limit_ml, dry_weight_kg)
            FluidEntry(id, drink, amount_ml, logged_at)
            WeightEntry(id, weight_kg, measured_at, session)
Features:   - Log drinks and fluid-rich foods against a daily limit
            - Show remaining allowance as a big gauge
            - Log pre- and post-dialysis weights
            - Show weight gain between sessions
            - Warn when the limit is nearly reached
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 224

**Intent:**
low fodmap food checker for ibs

**Spec:**
```
Type:       Mobile application (FODMAP food guide)
Data model: Food(id, name, category, serving_g, fructans, lactose, fructose, polyols, gos, rating)
            Reaction(id, food_id -> Food, eaten_at, symptoms, severity)
Features:   - Search foods and show traffic-light FODMAP ratings
            - Show safe serving sizes
            - Run a reintroduction phase plan by FODMAP group
            - Log symptoms after test foods
            - Work offline with a bundled food list
Storage:    Local on-device database (SQLite, bundled)
Tech stack: Flutter, sqflite
```

---

## Example 225

**Intent:**
gout app to check purine in foods and log attacks

**Spec:**
```
Type:       Mobile application (gout manager)
Data model: Food(id, name, purine_mg_per_100g)
            Attack(id, started_at, joint, pain, treated_with)
            UricAcidTest(id, tested_on, mg_dl)
Features:   - Look up purine content of foods
            - Log gout attacks by joint and pain
            - Log uric acid test results
            - Chart uric acid against the target level
            - Show foods eaten in the 2 days before attacks
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 226

**Intent:**
thyroid tracker for levothyroxine dose and blood test results tsh t4

**Spec:**
```
Type:       Mobile application (thyroid tracker)
Data model: Dose(id, mcg, started_on)
            LabResult(id, tested_on, tsh, free_t4, free_t3)
            SymptomLog(id, date, energy, mood, weight_kg)
Features:   - Record dose changes
            - Log TSH, free T4 and free T3 results
            - Chart results against reference ranges with dose changes marked
            - Log energy and mood daily
            - Remind to take the tablet on an empty stomach
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Victory Native
```

---

## Example 227

**Intent:**
cpap usage log, hours per night and mask leaks

**Spec:**
```
Type:       Mobile application (CPAP therapy log)
Data model: Night(id, date, hours_used, ahi, leak_l_min, mask_fit, notes)
            Supply(id, item, replaced_on, replace_every_days)
Features:   - Import nightly data from the machine's SD card export
            - Log hours used, AHI and leak rate
            - Chart usage over 30 days against the 4-hour compliance target
            - Remind to replace masks, filters and tubing
            - Note how rested the user feels
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 228

**Intent:**
endometriosis pain diary with cycle days

**Spec:**
```
Type:       Mobile application (endometriosis symptom diary)
Data model: Cycle(id, started_on)
            DailyLog(id, date, pain_level, pain_locations, bleeding, fatigue, bowel_symptoms, painkillers)
Features:   - Log daily pain with location on a body map
            - Track cycle day automatically from period start dates
            - Record painkillers taken
            - Show pain by cycle day across several months
            - Export a report for a gynaecologist
Storage:    Local on-device database (encrypted SQLite)
Tech stack: Swift, SwiftUI, SQLCipher
```

---

## Example 229

**Intent:**
ostomy bag change log and supply count

**Spec:**
```
Type:       Mobile application (ostomy care log)
Data model: Change(id, changed_at, skin_condition, leak, note, photo_path)
            Supply(id, product, size, stock, reorder_at)
Features:   - Log appliance changes with skin condition
            - Record leaks and possible causes
            - Track supply stock and remind to reorder
            - Show average wear time
            - Keep stoma photos private
Storage:    Local on-device storage (encrypted)
Tech stack: Flutter, Hive (encrypted box)
```

---

## Example 230

**Intent:**
lupus flare tracker with symptoms and sun exposure

**Spec:**
```
Type:       Mobile application (lupus flare tracker)
Data model: DailyLog(id, date, joint_pain, fatigue, rash, fever, hair_loss, sun_minutes, stress)
            Flare(id, started_on, ended_on, severity, treatment)
Features:   - Rate key symptoms each day
            - Log time in the sun with UV index
            - Record flares and treatments
            - Show symptom trends before flares
            - Share a summary with the rheumatologist
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 231

**Intent:**
sickle cell pain crisis log and hydration reminders

**Spec:**
```
Type:       Mobile application (sickle cell care log)
Data model: Crisis(id, started_at, ended_at, pain_level, locations, hospital_visit, trigger)
            WaterLog(id, amount_ml, logged_at)
Features:   - Log pain crises with severity and location
            - Note triggers like cold, stress or dehydration
            - Remind to drink water regularly
            - Record hospital visits
            - Generate a crisis summary for doctors
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 232

**Intent:**
MS fatigue and walking test log

**Spec:**
```
Type:       Mobile application (multiple sclerosis self-monitoring)
Data model: WalkTest(id, tested_on, seconds_25ft)
            Fatigue(id, date, score)
            Relapse(id, started_on, symptoms, steroids_given)
Features:   - Time a 25-foot walk test with the stopwatch
            - Log daily fatigue scores
            - Record relapses and treatments
            - Chart walk times and fatigue over months
            - Remind about infusion appointments
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Swift Charts
```

---

## Example 233

**Intent:**
potassium checker for kidney disease diet

**Spec:**
```
Type:       Mobile application (renal diet helper)
Data model: Food(id, name, potassium_mg, phosphorus_mg, sodium_mg, per_g)
            MealEntry(id, food_id -> Food, grams, eaten_at)
Features:   - Search foods for potassium, phosphorus and sodium
            - Log meals with portion sizes
            - Total daily nutrients against limits set by the dietitian
            - Show low-potassium swaps
            - Work offline
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 234

**Intent:**
my kid has type 1 and goes to school, I want to see his CGM numbers and get a buzz if he's going low

**Spec:**
```
Type:       Mobile application with backend (remote glucose follower)
Auth:       Parent account with email; child's phone paired by code
Data model: Child(id, name, low_mg_dl, high_mg_dl)
            Reading(id, child_id -> Child, mg_dl, trend, read_at)
            Follower(id, child_id -> Child, push_token)
Features:   - Read CGM values on the child's phone from Apple HealthKit
            - Upload readings to the server every 5 minutes
            - Show live readings and trend arrows to parents
            - Alert parents on lows, highs and lost signal
            - Show a 24-hour graph
API:        REST
            POST /readings
            GET  /children/{id}/readings
            PUT  /children/{id}/thresholds
Storage:    PostgreSQL (TimescaleDB)
Tech stack: Swift, HealthKit, Go, Apple Push Notification service
```

---

## Example 235

**Intent:**
baby monitor using two old phones over wifi

**Spec:**
```
Type:       Mobile application (two-phone baby monitor)
Features:   - Pair a baby unit and parent unit on the same Wi-Fi
            - Stream audio and low-res video from the baby unit
            - Alert the parent unit when sound passes a threshold
            - Talk back to the baby with push-to-talk
            - Show the baby unit's battery level
Tech stack: Kotlin, WebRTC, Network Service Discovery
```

---

## Example 236

**Intent:**
white noise app for baby with sleep timer and fade out

**Spec:**
```
Type:       Mobile application (baby white noise)
Data model: Sound(id, name, file_path)
            Preset(id, sound_id -> Sound, volume, timer_minutes)
Features:   - Play seamless looping sounds like shush, heartbeat and rain
            - Set a timer with a gentle fade out
            - Restart playback when the baby cries using the microphone
            - Keep playing with the screen off
            - Save presets
Storage:    Local on-device storage
Tech stack: Swift, AVFoundation, SwiftUI
```

---

## Example 237

**Intent:**
monthly baby photos with age stickers like 3 months old

**Spec:**
```
Type:       Mobile application (baby monthly photo maker)
Data model: Child(id, name, birth_date)
            Photo(id, child_id -> Child, month_number, original_path, edited_path)
Features:   - Remind on each monthly birthday to take a photo
            - Add age stickers and text to photos
            - Line up photos with a guide overlay
            - Create a collage or video of the first year
            - Save to the camera roll
Storage:    Local on-device storage
Tech stack: Flutter, image package, ffmpeg_kit_flutter
```

---

## Example 238

**Intent:**
driving lessons log for my learner hours, need 120 hours with 20 at night for the license

**Spec:**
```
Type:       Mobile application (learner driver logbook)
Data model: Learner(id, name, licence_no)
            Supervisor(id, name, licence_no)
            Drive(id, supervisor_id -> Supervisor, started_at, ended_at, start_odometer, end_odometer, night, conditions, route)
Features:   - Start and stop drives with GPS route recording
            - Mark night drives automatically from sunset times
            - Total hours and night hours against the requirement
            - Record the supervising driver for each drive
            - Export a logbook PDF for the licensing office
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-location, expo-sqlite
```

---

## Example 239

**Intent:**
parking ticket and fine tracker so i pay before it doubles

**Spec:**
```
Type:       Mobile application (fine payment tracker)
Data model: Fine(id, reference, issued_on, amount, discount_until, discounted_amount, due_on, status, photo_path)
Features:   - Photograph the ticket and read the amount and date with OCR
            - Show the discount deadline countdown
            - Remind before the discount ends and before the due date
            - Mark fines as paid or appealed
            - Show total fines per year
Storage:    Local on-device storage
Tech stack: Kotlin, ML Kit Text Recognition, Jetpack Compose
```

---

## Example 240

**Intent:**
mileage log for taxes, i drive for work clients

**Spec:**
```
Type:       Mobile application (business mileage log)
Data model: Trip(id, started_at, ended_at, start_address, end_address, distance_km, purpose, client, is_business)
Features:   - Detect drives automatically using motion and GPS
            - Classify trips as business or personal with a swipe
            - Calculate the deductible amount at the tax rate
            - Add client and purpose to each trip
            - Export a yearly mileage report as CSV and PDF
Storage:    Local on-device database (SQLite)
Tech stack: Swift, CoreMotion, CoreLocation, SwiftUI
```

---

## Example 241

**Intent:**
car wash and detailing log lol i'm obsessed with my car

**Spec:**
```
Type:       Mobile application (car detailing log)
Data model: Car(id, name, paint_colour)
            Product(id, name, type)
            Detail(id, car_id -> Car, date, type, products_used, duration_min, photo_path, notes)
Features:   - Log washes, waxes and ceramic coatings
            - Record products used for each session
            - Remind when wax or sealant is due again
            - Show before and after photos
            - Track product stock
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 242

**Intent:**
road trip fuel stop planner for my old car with small tank

**Spec:**
```
Type:       Mobile application (fuel range planner)
Data model: Vehicle(id, tank_litres, consumption_l_100km)
            Trip(id, origin, destination, route_polyline)
            FuelStop(id, trip_id -> Trip, name, lat, lng, distance_km)
Features:   - Calculate range from tank size and consumption
            - Plan a route with a mapping API
            - Suggest fuel stations before the range runs out with a safety margin
            - Show stops on the map
            - Work offline once a trip is planned
Storage:    Local on-device storage
Tech stack: Kotlin, Google Maps SDK, Google Directions API, Google Places API
```

---

## Example 243

**Intent:**
motorcycle trip log with lean angle

**Spec:**
```
Type:       Mobile application (motorcycle ride recorder)
Data model: Ride(id, started_at, ended_at, distance_km, max_lean_left, max_lean_right, max_speed_kmh)
            Point(id, ride_id -> Ride, lat, lng, speed, lean_deg, at)
Features:   - Record rides with GPS
            - Measure lean angle with the gyroscope when mounted
            - Show max lean and speed per ride
            - Replay rides on a map coloured by lean angle
            - Export rides as GPX
Storage:    Local on-device database (SQLite)
Tech stack: Swift, CoreMotion, CoreLocation, MapKit
```

---

## Example 244

**Intent:**
landlord app for move-in inspection with photos of every room and tenant signature

**Spec:**
```
Type:       Mobile application (property inventory inspection)
Data model: Property(id, address)
            Inspection(id, property_id -> Property, type, date, tenant_name, signature_path)
            RoomCheck(id, inspection_id -> Inspection, room, item, condition, note, photo_path)
Features:   - Walk through rooms with a checklist of items
            - Rate condition and add photos per item
            - Capture tenant and landlord signatures
            - Compare move-in and move-out reports side by side
            - Export a timestamped PDF report
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, signature, pdf
```

---

## Example 245

**Intent:**
electricity meter readings to check my bill, i take a photo each month

**Spec:**
```
Type:       Mobile application (utility meter tracker)
Data model: Meter(id, type, unit, tariff_per_unit, standing_charge)
            Reading(id, meter_id -> Meter, value, read_on, photo_path)
Features:   - Photograph meters and read the number with OCR
            - Track electricity, gas and water meters
            - Calculate usage and cost between readings
            - Compare against the bill
            - Chart usage month by month
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, ML Kit Text Recognition, Room, Jetpack Compose
```

---

## Example 246

**Intent:**
secret santa app for my office, draws names and nobody can see who got who

**Spec:**
```
Type:       Mobile application with backend (gift exchange draw)
Auth:       Organiser creates a group; participants join with an emailed link
Data model: Exchange(id, organiser_email, name, budget, exchange_date)
            Participant(id, exchange_id -> Exchange, name, email, wishlist)
            Assignment(giver_id -> Participant, receiver_id -> Participant)
Features:   - Invite participants by email
            - Draw names randomly so nobody gets themselves
            - Respect exclusions like couples
            - Show each person only their own match
            - Let participants write a wish list
API:        REST
            POST /exchanges
            POST /exchanges/{id}/draw
            GET  /participants/{token}/match
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express, SendGrid
```

---

## Example 247

**Intent:**
thank you card tracker after the wedding, who gave what and if card sent

**Spec:**
```
Type:       Mobile application (thank-you note tracker)
Data model: Gift(id, from_names, description, received_on, address, card_sent, sent_on)
Features:   - Log gifts with the giver and description
            - Mark thank-you cards as written and sent
            - Show who still needs a card
            - Store addresses for envelopes
            - Export the list as CSV
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 248

**Intent:**
gift idea list for family birthdays so i remember what they said they wanted

**Spec:**
```
Type:       Mobile application (gift ideas)
Data model: Person(id, name, birthday, sizes)
            Idea(id, person_id -> Person, idea, link, price, given_on)
Features:   - Save gift ideas per person when they come up
            - Store clothing sizes and likes
            - Remind two weeks before each birthday
            - Mark ideas as bought and given
            - Avoid repeating gifts from past years
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 249

**Intent:**
funeral planning checklist when my dad died I was lost, want something to help others

**Spec:**
```
Type:       Mobile application (bereavement checklist)
Data model: Task(id, title, phase, description, done, due_on)
            Contact(id, name, organisation, phone, notes)
            Document(id, name, photo_path)
Features:   - Show tasks by phase like first days, funeral and estate
            - Explain each task in plain language
            - Track contacts like funeral director and solicitor
            - Store photos of key documents
            - Let tasks be shared with siblings by exporting a list
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 250

**Intent:**
wedding vows and speech teleprompter on phone

**Spec:**
```
Type:       Mobile application (speech teleprompter)
Data model: Script(id, title, text, scroll_speed, font_size)
Features:   - Write or paste a speech
            - Scroll text automatically at an adjustable speed
            - Mirror text for use with a teleprompter glass
            - Pause and resume with a tap
            - Rehearse with a timer showing estimated length
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 251

**Intent:**
event budget for a quinceañera, track vendors and what family members are paying for

**Spec:**
```
Type:       Mobile application (celebration budget)
Data model: Event(id, name, date, budget)
            Vendor(id, event_id -> Event, service, name, price, deposit, balance_due_on)
            Sponsor(id, event_id -> Event, name, item, amount)
Features:   - Track vendors with deposits and balances
            - Record family sponsors (padrinos) and what they cover
            - Show remaining budget
            - Remind of balance due dates
            - Export a summary to share with family
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 252

**Intent:**
hi i need app for my mosque to show iqamah times on a tv screen and phones

**Spec:**
```
Type:       Mobile application with backend (mosque prayer timetable)
Auth:       Admin login for mosque staff
Data model: Mosque(id, name, lat, lng)
            IqamahTime(id, mosque_id -> Mosque, date, prayer, adhan_at, iqamah_at)
            Announcement(id, mosque_id -> Mosque, text, expires_on)
Features:   - Calculate adhan times and let admins set iqamah times
            - Show a full-screen display mode for a TV
            - Show a countdown to the next iqamah
            - Post announcements
            - Notify followers when times change
API:        REST
            GET  /mosques/{id}/times
            PUT  /mosques/{id}/times
            POST /mosques/{id}/announcements
Storage:    PostgreSQL
Tech stack: Flutter, Dart Frog, PostgreSQL
```

---

## Example 253

**Intent:**
rosary prayer counter app

**Spec:**
```
Type:       Mobile application (prayer bead counter)
Data model: Prayer(id, name, text, repetitions)
            Session(id, prayer_id -> Prayer, count, completed_at)
Features:   - Count prayers with a tap or volume buttons
            - Show the mystery or prayer text for each decade
            - Vibrate at the end of each decade
            - Keep the screen dim and awake
            - Log completed sessions
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose
```

---

## Example 254

**Intent:**
shabbat candle lighting times

**Spec:**
```
Type:       Mobile application (candle lighting times)
Features:   - Calculate candle lighting and havdalah times from location
            - Show times for the coming weeks
            - Notify before candle lighting
            - Show the Hebrew date
            - Let the user set minutes before sunset per local custom
Tech stack: Swift, SwiftUI, KosherSwift
```

---

## Example 255

**Intent:**
fasting tracker for ramadan with suhoor and iftar alarms

**Spec:**
```
Type:       Mobile application (Ramadan fasting tracker)
Data model: FastDay(id, date, fasted, reason_missed, made_up_on)
Features:   - Show suhoor and iftar times for the location
            - Sound alarms before suhoor ends and at iftar
            - Mark each day fasted or missed
            - Track days to make up later
            - Show a 30-day progress view
Storage:    Local on-device storage
Tech stack: Flutter, adhan_dart, flutter_local_notifications
```

---

## Example 256

**Intent:**
app to learn the guitar fretboard notes

**Spec:**
```
Type:       Mobile application (fretboard trainer)
Data model: Attempt(id, string, fret, correct, response_ms, answered_at)
Features:   - Highlight a random fret and ask for the note name
            - Ask the user to find all positions of a note
            - Listen through the microphone to check the played note
            - Limit practice to chosen strings and fret ranges
            - Show a heat map of weak spots
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, TarsosDSP, Jetpack Compose
```

---

## Example 257

**Intent:**
a mandolin and violin tuner too, not just guitar, with custom temperament

**Spec:**
```
Type:       Mobile application (chromatic tuner)
Data model: Instrument(id, name, string_notes)
            Settings(reference_hz, temperament)
Features:   - Detect pitch with the YIN algorithm
            - Show cents offset for any chromatic note
            - Include presets for violin, viola, cello, mandolin and banjo
            - Change reference pitch from A=415 to A=446
            - Support just and meantone temperaments
Storage:    Local on-device storage
Tech stack: Swift, AVAudioEngine, Accelerate, SwiftUI
```

---

## Example 258

**Intent:**
harmonica tabs app with songs for beginners

**Spec:**
```
Type:       Mobile application (harmonica tabs)
Data model: Song(id, title, key, difficulty, tabs)
            Favourite(song_id -> Song)
Features:   - Show songs in hole-number tab notation
            - Filter songs by harmonica key and difficulty
            - Scroll tabs automatically in time with a tempo
            - Play a reference audio
            - Save favourites
Storage:    Local on-device database (SQLite, bundled)
Tech stack: React Native, expo-av, expo-sqlite
```

---

## Example 259

**Intent:**
braille translator, type text and see braille dots and back

**Spec:**
```
Type:       Mobile application (Braille translator)
Features:   - Translate typed text to Grade 1 and Grade 2 Braille
            - Show Braille cells as large dot graphics
            - Translate Braille entered on a six-dot keypad back to text
            - Read output aloud
            - Share as Unicode Braille text
Tech stack: Kotlin, liblouis, Jetpack Compose
```

---

## Example 260

**Intent:**
morse code trainer

**Spec:**
```
Type:       Mobile application (Morse code trainer)
Data model: Character(symbol, code)
            Attempt(id, symbol, correct, answered_at)
Features:   - Play characters as audio at adjustable speed with Farnsworth spacing
            - Let the user tap a key to send Morse
            - Decode tapped Morse to text
            - Teach letters in Koch method order
            - Track accuracy per character
Storage:    Local on-device storage
Tech stack: Swift, AVAudioEngine, SwiftUI
```

---

## Example 261

**Intent:**
sign language dictionary with videos

**Spec:**
```
Type:       Mobile application (sign language dictionary)
Data model: Sign(id, word, category, video_path, handshape)
            Favourite(sign_id -> Sign)
Features:   - Search signs by English word
            - Play looping video clips at slow speed
            - Browse signs by category like family or food
            - Save favourites into practice lists
            - Download video packs for offline use
Storage:    Local on-device database (SQLite), video files
Tech stack: Kotlin, ExoPlayer, Room, Jetpack Compose
```

---

## Example 262

**Intent:**
i want my 4 yr old to learn baby sign words, cards with pictures and a video of the sign

**Spec:**
```
Type:       Mobile application (baby sign flashcards)
Data model: Card(id, word, picture_path, video_path, category)
            Learned(card_id -> Card, learned_on)
Features:   - Show picture cards that play the sign video on tap
            - Group cards into themes like meals and bedtime
            - Mark signs the child has learned
            - Play a simple matching game
            - Keep everything offline with no ads
Storage:    Local on-device storage
Tech stack: Flutter, video_player, Hive
```

---

## Example 263

**Intent:**
colour blind mode for my photos, recolour so i can tell red and green apart

**Spec:**
```
Type:       Mobile application (colour vision correction)
Data model: Settings(cvd_type, strength)
Features:   - Apply daltonisation filters for protanopia, deuteranopia and tritanopia
            - Preview filters on the live camera
            - Process photos from the gallery
            - Adjust filter strength with a slider
            - Save corrected images
Storage:    Local on-device storage
Tech stack: Swift, Metal, Core Image, SwiftUI
```

---

## Example 264

**Intent:**
color blind test app with ishihara plates

**Spec:**
```
Type:       Mobile application (colour vision test)
Data model: Plate(id, image_path, normal_answer, cvd_answer, type)
            TestResult(id, taken_on, score, likely_type)
Features:   - Show Ishihara-style plates one at a time
            - Let the user type the number seen or skip
            - Score answers and estimate the type of colour deficiency
            - Explain results in plain words
            - Save past results
Storage:    Local on-device storage
Tech stack: React Native, AsyncStorage
```

---

## Example 265

**Intent:**
color matcher for clothes, tells me if my shirt and pants go together, im colourblind

**Spec:**
```
Type:       Mobile application (outfit colour matcher)
Features:   - Capture two clothing items with the camera
            - Name each colour in plain words
            - Rate how well the colours go together using colour theory rules
            - Suggest matching colours for an item
            - Speak the result aloud
Tech stack: Kotlin, CameraX, Jetpack Compose, Android TextToSpeech
```

---

## Example 266

**Intent:**
a screen reader friendly bus arrival app for blind users

**Spec:**
```
Type:       Mobile application (accessible transit arrivals)
Data model: Stop(id, name, lat, lng)
            FavouriteStop(stop_id -> Stop, nickname)
Features:   - Find the nearest stops using GPS
            - Announce upcoming arrivals with VoiceOver friendly labels
            - Vibrate when the chosen bus is 2 minutes away
            - Save favourite stops
            - Read stop names aloud as the user walks past
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, CoreLocation, GTFS-Realtime feed
```

---

## Example 267

**Intent:**
date calculator, how many days between dates and add days to a date

**Spec:**
```
Type:       Mobile application (date calculator)
Features:   - Calculate days, weeks and months between two dates
            - Add or subtract days from a date
            - Count only working days, excluding weekends and holidays
            - Show the weekday of any date
            - Save named countdowns
Tech stack: Kotlin, java.time, Jetpack Compose
```

---

## Example 268

**Intent:**
percentage calculator for discounts and markups

**Spec:**
```
Type:       Mobile application (percentage calculator)
Features:   - Calculate a discount price from a percentage off
            - Calculate markup and margin from cost and price
            - Find what percent one number is of another
            - Calculate percentage increase or decrease
            - Show a history of calculations
Storage:    Local on-device storage
Tech stack: Flutter
```

---

## Example 269

**Intent:**
loan payoff calculator for my car loan, what if i pay extra

**Spec:**
```
Type:       Mobile application (loan payoff calculator)
Data model: Loan(id, name, principal, annual_rate, term_months, start_date)
Features:   - Calculate the monthly payment from rate and term
            - Show a full amortisation schedule
            - Show how extra monthly payments shorten the loan
            - Show total interest saved
            - Compare two scenarios side by side
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, Swift Charts
```

---

## Example 270

**Intent:**
hourly pay calculator with overtime, shifts in a week

**Spec:**
```
Type:       Mobile application (shift pay calculator)
Data model: Job(id, name, hourly_rate, overtime_after_hours, overtime_multiplier)
            Shift(id, job_id -> Job, started_at, ended_at, break_minutes)
Features:   - Log shifts with start, end and breaks
            - Calculate weekly hours and overtime
            - Estimate gross pay per week
            - Support night and weekend rates
            - Compare against the payslip
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 271

**Intent:**
fraction calculator for woodworking, inches like 3 5/8 plus 2 7/16

**Spec:**
```
Type:       Mobile application (feet-inch fraction calculator)
Features:   - Enter measurements in feet, inches and fractions
            - Add, subtract, multiply and divide measurements
            - Round results to the nearest 1/16 or 1/32
            - Convert between fractional inches and millimetres
            - Keep a tape of calculations
Tech stack: Swift, SwiftUI
```

---

## Example 272

**Intent:**
GPA calculator for my uni courses

**Spec:**
```
Type:       Mobile application (GPA calculator)
Data model: Term(id, name)
            Course(id, term_id -> Term, name, credits, grade)
Features:   - Add courses per term with credits and grade
            - Calculate term and cumulative GPA
            - Support 4.0 and percentage scales
            - Show what grades are needed to reach a target GPA
            - Save terms locally
Storage:    Local on-device storage
Tech stack: React Native, AsyncStorage
```

---

## Example 273

**Intent:**
offline map app for geology field trips where I record strike and dip with the phone

**Spec:**
```
Type:       Mobile application (geological field compass)
Data model: Station(id, name, lat, lng, elevation_m)
            Measurement(id, station_id -> Station, type, strike_deg, dip_deg, rock_type, note, photo_path)
Features:   - Measure strike and dip by placing the phone on a surface
            - Record measurements with GPS on an offline map
            - Draw strike and dip symbols on the map
            - Attach photos and rock descriptions
            - Export data as CSV and KML
Storage:    Local on-device database (SQLite), offline map tiles
Tech stack: Kotlin, Android SensorManager, MapLibre Native, Room
```

---

## Example 274

**Intent:**
field app for collecting plant samples for herbarium, collector number, gps, habitat

**Spec:**
```
Type:       Mobile application (botanical specimen collection)
Data model: Collection(id, collector_no, species_guess, collected_on, lat, lng, elevation_m, habitat, associated_species, photo_path)
Features:   - Auto-increment collector numbers
            - Record GPS, elevation and habitat
            - Attach photos of the plant in situ
            - Print specimen labels as PDF
            - Export to Darwin Core CSV
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, geolocator, pdf
```

---

## Example 275

**Intent:**
water sampling app for river monitoring volunteers, readings and sync to our org

**Spec:**
```
Type:       Mobile application with backend (citizen science water monitoring)
Auth:       Volunteer login with email
Data model: Site(id, name, river, lat, lng)
            Sample(id, site_id -> Site, volunteer_id, sampled_at, temp_c, ph, turbidity_ntu, nitrate_ppm, photo_path)
Features:   - Show monitoring sites on an offline map
            - Record readings with test kit values
            - Validate readings against plausible ranges
            - Queue samples offline and upload later
            - Show trends per site
API:        REST
            GET  /sites
            POST /samples
            GET  /sites/{id}/samples
Storage:    SQLite on device, PostgreSQL on backend
Tech stack: React Native, WatermelonDB, Node.js, PostgreSQL
```

---

## Example 276

**Intent:**
surveyor app to log GPS points with a code and export to dxf

**Spec:**
```
Type:       Mobile application (field point logger)
Data model: Job(id, name, crs)
            Point(id, job_id -> Job, number, code, lat, lng, elevation_m, accuracy_m, note)
Features:   - Record points with GPS and an accuracy reading
            - Connect to an external GNSS receiver over Bluetooth
            - Assign feature codes from a list
            - Convert coordinates to the job's projection
            - Export points as CSV and DXF
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Room, PROJ, Android Bluetooth
```

---

## Example 277

**Intent:**
tape measure log for windows I measure for blinds

**Spec:**
```
Type:       Mobile application (window measurement log)
Data model: Customer(id, name, address)
            Window(id, customer_id -> Customer, room, width_mm, drop_mm, fit_type, notes, photo_path)
Features:   - Record measurements per window and room
            - Choose recess or exact fit
            - Attach a photo of each window
            - Generate a quote from blind prices per m2
            - Export an order sheet for the factory
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, pdf
```

---

## Example 278

**Intent:**
paint calculator, how many litres for my room

**Spec:**
```
Type:       Mobile application (paint calculator)
Features:   - Enter wall dimensions and number of doors and windows
            - Subtract openings from the wall area
            - Calculate litres needed for the number of coats
            - Use coverage per litre for the chosen paint
            - Round up to standard tin sizes
Tech stack: Kotlin, Jetpack Compose
```

---

## Example 279

**Intent:**
decking calculator for boards, joists and screws

**Spec:**
```
Type:       Mobile application (decking calculator)
Data model: Deck(id, name, length_m, width_m, board_width_mm, gap_mm, joist_spacing_mm)
Features:   - Calculate the number of deck boards from dimensions and gap
            - Calculate joists and bearers from spacing
            - Estimate screws and hidden fixings
            - Show a simple top-down layout
            - Export a materials list
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, Core Graphics
```

---

## Example 280

**Intent:**
Sunday roast timer, I put in what I'm cooking and it tells me when each thing goes in the oven so all ready at once

**Spec:**
```
Type:       Mobile application (meal timing planner)
Data model: Dish(id, name, cook_minutes, rest_minutes, oven_temp_c)
            Plan(id, serve_at)
Features:   - Add dishes with cook and rest times
            - Work backwards from the serving time
            - Show a timeline of when each dish goes in and comes out
            - Send notifications at each step
            - Warn when dishes need different oven temperatures
Storage:    Local on-device storage
Tech stack: Flutter, flutter_local_notifications
```

---

## Example 281

**Intent:**
meat smoker log, temps, wood type, how long, how it came out

**Spec:**
```
Type:       Mobile application (BBQ smoke log)
Data model: Cook(id, meat, weight_kg, wood, smoker_temp_c, started_at, ended_at, rating, notes)
            TempReading(id, cook_id -> Cook, meat_temp_c, pit_temp_c, read_at)
Features:   - Log cooks with meat, weight and wood
            - Record pit and meat temperatures over time
            - Read temperatures from a Bluetooth thermometer
            - Chart the cook and show the stall
            - Rate results to refine future cooks
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Android Bluetooth LE, Room, Vico
```

---

## Example 282

**Intent:**
canning and preserving log, what jars I made when and best before

**Spec:**
```
Type:       Mobile application (home canning log)
Data model: Batch(id, recipe, made_on, method, processing_minutes, jars, jar_size_ml)
            Jar(id, batch_id -> Batch, opened_on, shelf)
Features:   - Log batches with recipe and processing method
            - Calculate best-before dates
            - Print jar labels
            - Track jars on shelves and mark opened
            - Warn on altitude adjustments for processing time
Storage:    Local on-device storage
Tech stack: React Native, expo-sqlite, expo-print
```

---

## Example 283

**Intent:**
kombucha brewing tracker

**Spec:**
```
Type:       Mobile application (kombucha brew tracker)
Data model: Brew(id, started_on, volume_l, tea_type, sugar_g, f1_days, f2_started_on, flavours)
            Taste(id, brew_id -> Brew, tasted_on, sweetness, fizz)
Features:   - Track first and second fermentation dates
            - Remind when to taste or bottle
            - Log flavour combinations for second fermentation
            - Rate sweetness and fizz
            - Note SCOBY health
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 284

**Intent:**
recipe card scanner from my grandma's handwritten recipes

**Spec:**
```
Type:       Mobile application (handwritten recipe digitiser)
Data model: Recipe(id, title, ingredients, steps, original_photo_path, author)
Features:   - Photograph recipe cards
            - Convert handwriting to text with OCR
            - Edit and split text into ingredients and steps
            - Keep the original card image with the recipe
            - Export a family recipe book as PDF
Storage:    Local on-device database (SQLite)
Tech stack: Swift, VisionKit, Vision text recognition, SwiftUI
```

---

## Example 285

**Intent:**
shopping list per store aisle so i walk the shop once

**Spec:**
```
Type:       Mobile application (aisle-sorted shopping list)
Data model: Store(id, name)
            Aisle(id, store_id -> Store, number, name)
            ItemAisle(item_name, aisle_id -> Aisle)
            ListItem(id, name, quantity, checked)
Features:   - Set up aisles for each store
            - Remember which aisle each item is in
            - Sort the list by aisle for the selected store
            - Tick items while shopping
            - Share the list with a household member
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 286

**Intent:**
Batch cooking for a family of six on a tight budget. I want an app that costs each recipe per portion from the prices I paid.

**Spec:**
```
Type:       Mobile application (recipe costing)
Data model: Ingredient(id, name, pack_size, pack_unit, pack_price)
            Recipe(id, name, portions)
            RecipeIngredient(recipe_id -> Recipe, ingredient_id -> Ingredient, quantity, unit)
Features:   - Record ingredient prices from receipts
            - Calculate the cost per recipe and per portion
            - Update all recipe costs when a price changes
            - Sort recipes by cost per portion
            - Plan a weekly menu within a budget
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 287

**Intent:**
what to do with leftovers, i type what's in fridge it shows recipes

**Spec:**
```
Type:       Mobile application (leftover recipe finder)
Data model: Recipe(id, title, ingredients, steps, minutes)
            FridgeItem(id, name)
Features:   - Enter ingredients available
            - Match recipes that use the most available ingredients
            - Show missing ingredients for each recipe
            - Filter by cooking time
            - Work offline with a bundled recipe set
Storage:    Local on-device database (SQLite, bundled)
Tech stack: React Native, expo-sqlite
```

---

## Example 288

**Intent:**
wine cellar inventory, bin locations and drinking windows

**Spec:**
```
Type:       Mobile application (wine cellar manager)
Data model: Wine(id, producer, name, vintage, region, drink_from, drink_to)
            Bottle(id, wine_id -> Wine, rack, row, column, purchased_on, price, consumed_on)
Features:   - Record bottles with their rack position
            - Show a visual rack map
            - Highlight wines inside their drinking window
            - Mark bottles as drunk with a note
            - Show cellar value
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 289

**Intent:**
coffee bean roasting log for my home roaster

**Spec:**
```
Type:       Mobile application (coffee roast profiler)
Data model: GreenBean(id, origin, process, stock_g)
            Roast(id, bean_id -> GreenBean, roasted_on, charge_g, yield_g, first_crack_s, drop_s, profile_points)
Features:   - Log roast temperature points with a timer
            - Mark first crack and drop time
            - Calculate development time ratio and weight loss
            - Subtract green bean stock
            - Compare roast curves
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, Vico
```

---

## Example 290

**Intent:**
tea ceremony timer for gongfu brewing with many short steeps

**Spec:**
```
Type:       Mobile application (gongfu tea timer)
Data model: Profile(id, tea_name, first_steep_s, increment_s, max_steeps)
Features:   - Start steep timers that increase each round
            - Show the current steep number
            - Vibrate when a steep is done
            - Save profiles per tea
            - Keep the screen awake
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 291

**Intent:**
cocktail recipe app sorted by what bottles i have at home

**Spec:**
```
Type:       Mobile application (home bar cocktail finder)
Data model: Spirit(id, name, type)
            Cocktail(id, name, method, glass, garnish)
            CocktailIngredient(cocktail_id -> Cocktail, name, ml, spirit_type)
Features:   - Mark which bottles are in the home bar
            - Show cocktails that can be made now
            - Show cocktails missing one ingredient
            - Scale recipes for multiple drinks
            - Save favourites
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 292

**Intent:**
fly fishing fly box catalog and which flies work on which river

**Spec:**
```
Type:       Mobile application (fly box catalogue)
Data model: Fly(id, name, type, size, colour, count, photo_path)
            River(id, name)
            Outing(id, river_id -> River, date, hatch, water_temp_c)
            FlyResult(outing_id -> Outing, fly_id -> Fly, fish_caught)
Features:   - Catalogue flies by type and hook size
            - Log outings with hatches and water temperature
            - Record catches per fly
            - Show best flies per river and month
            - Warn when a fly is running low
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 293

**Intent:**
ice fishing hole log with depth and gps

**Spec:**
```
Type:       Mobile application (ice fishing log)
Data model: Lake(id, name)
            Hole(id, lake_id -> Lake, lat, lng, depth_m, ice_thickness_cm, drilled_on)
            Catch(id, hole_id -> Hole, species, length_cm, caught_at, lure)
Features:   - Mark holes with GPS on the lake
            - Log depth and ice thickness
            - Record catches per hole
            - Warn when ice thickness is below safe limits
            - Show productive holes on a map
Storage:    Local on-device database (SQLite)
Tech stack: Swift, MapKit, SwiftUI, Core Data
```

---

## Example 294

**Intent:**
bouldering board app, I want to set problems on our home wall and share with my roommates

**Spec:**
```
Type:       Mobile application with backend (home climbing wall problems)
Auth:       Email login, wall shared by invite code
Data model: Wall(id, name, photo_path, angle_deg)
            Hold(id, wall_id -> Wall, x, y)
            Problem(id, wall_id -> Wall, setter_id, name, grade, hold_ids)
            Ascent(id, problem_id -> Problem, user_id, sent_on)
Features:   - Upload a photo of the wall and mark hold positions
            - Create problems by tapping start, hand and finish holds
            - Grade problems and vote on grades
            - Log ascents
            - Share problems with everyone on the wall
API:        REST
            GET  /walls/{id}/problems
            POST /problems
            POST /problems/{id}/ascents
Storage:    Supabase (PostgreSQL)
Tech stack: Flutter, Supabase
```

---

## Example 295

**Intent:**
hangboard training timer for climbing, repeaters

**Spec:**
```
Type:       Mobile application (hangboard timer)
Data model: Workout(id, name, hang_s, rest_s, reps, sets, set_rest_s)
            Session(id, workout_id -> Workout, done_on, added_weight_kg, grip)
Features:   - Run interval timers for hangs, rests and sets
            - Announce each phase with sounds and voice
            - Save custom workouts
            - Log added weight and grip per session
            - Show progress over time
Storage:    Local on-device storage
Tech stack: React Native, expo-av, AsyncStorage
```

---

## Example 296

**Intent:**
trail running race pacing plan by checkpoints

**Spec:**
```
Type:       Mobile application (ultra race pacing planner)
Data model: Race(id, name, gpx_path, start_at)
            Checkpoint(id, race_id -> Race, name, km, cutoff_at, planned_arrival)
Features:   - Import the race course as GPX
            - Add checkpoints with cut-off times
            - Calculate planned arrival times with elevation-adjusted pace
            - Show margin against each cut-off
            - Share the plan with crew
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, gpx parser
```

---

## Example 297

**Intent:**
sailing log book for my yacht, positions, wind, engine hours

**Spec:**
```
Type:       Mobile application (yacht logbook)
Data model: Voyage(id, from_port, to_port, started_at, ended_at, crew)
            LogEntry(id, voyage_id -> Voyage, logged_at, lat, lng, course_deg, speed_kn, wind_dir, wind_kn, baro_hpa, engine_hours, note)
Features:   - Create log entries with GPS position automatically
            - Record wind, barometer and engine hours
            - Log hourly entries with a reminder
            - Show the voyage track on a chart
            - Export the logbook as PDF
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, CoreLocation, MapKit
```

---

## Example 298

**Intent:**
anchor alarm app, wake me if the boat drags

**Spec:**
```
Type:       Mobile application (anchor drag alarm)
Data model: Anchorage(id, lat, lng, radius_m, set_at)
Features:   - Mark the anchor position when dropped
            - Set a swing radius
            - Track the boat position in the background
            - Sound a loud alarm when outside the radius
            - Show the track around the anchor
Storage:    Local on-device storage
Tech stack: Kotlin, Fused Location Provider, foreground service, Jetpack Compose
```

---

## Example 299

**Intent:**
telescope eyepiece calculator, magnification and field of view

**Spec:**
```
Type:       Mobile application (telescope calculator)
Data model: Telescope(id, name, aperture_mm, focal_length_mm)
            Eyepiece(id, name, focal_length_mm, afov_deg)
Features:   - Calculate magnification for each eyepiece
            - Calculate true field of view and exit pupil
            - Show maximum useful magnification
            - Simulate what an object looks like in the eyepiece
            - Store the user's equipment
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 300

**Intent:**
messier marathon checklist

**Spec:**
```
Type:       Mobile application (Messier object checklist)
Data model: MessierObject(number, name, type, ra, dec, magnitude)
            Observation(id, number -> MessierObject, observed_at, instrument, notes)
Features:   - List all 110 Messier objects
            - Sort objects by when they are best visible tonight
            - Mark objects as observed with notes
            - Show progress through the catalogue
            - Use a red night-vision screen mode
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 301

**Intent:**
meteor shower calendar with alerts

**Spec:**
```
Type:       Mobile application (meteor shower alerts)
Data model: Shower(id, name, peak_date, zhr, radiant_ra, radiant_dec)
Features:   - List upcoming meteor showers with peak dates
            - Show expected rates and moon interference
            - Show where the radiant rises for the user
            - Notify the evening before a peak
            - Count meteors during a session with a tap
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 302

**Intent:**
aurora alert app for my location

**Spec:**
```
Type:       Mobile application with backend (aurora alerts)
Data model: Subscriber(id, push_token, lat, lng, min_kp)
Features:   - Fetch the Kp index and aurora forecast every 15 minutes
            - Calculate if aurora may be visible at the user's latitude
            - Send push alerts when Kp passes the user's threshold
            - Show cloud cover for tonight
            - Let users report sightings
API:        REST
            POST /subscribers
            PUT  /subscribers/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI, NOAA SWPC API, Firebase Cloud Messaging
```

---

## Example 303

**Intent:**
bird nest box monitoring for our nature group, check each box weekly in spring

**Spec:**
```
Type:       Mobile application with backend (nest box monitoring)
Auth:       Volunteer login
Data model: NestBox(id, code, lat, lng, type)
            Check(id, box_id -> NestBox, checked_on, volunteer_id, species, eggs, chicks, status)
Features:   - Show nest boxes on a map with last check date
            - Record eggs, chicks and species each visit
            - Flag boxes not checked this week
            - Show season totals per species
            - Sync results to the group's database
API:        REST
            GET  /boxes
            POST /checks
Storage:    SQLite offline, PostgreSQL on backend
Tech stack: React Native, Django REST Framework, PostgreSQL
```

---

## Example 304

**Intent:**
butterfly count app, identify by photo

**Spec:**
```
Type:       Mobile application (butterfly survey)
Data model: Species(id, name, image)
            Sighting(id, species_id -> Species, count, lat, lng, seen_at, photo_path)
Features:   - Identify butterflies from a photo with an on-device model
            - Choose from a picture key when unsure
            - Log counts with location
            - Run a timed 15-minute count
            - Export counts for a national survey
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, TensorFlow Lite, CameraX, Room
```

---

## Example 305

**Intent:**
whale and dolphin sightings from ferry, for volunteers

**Spec:**
```
Type:       Mobile application (marine mammal sightings)
Data model: Trip(id, vessel, route, started_at)
            Effort(id, trip_id -> Trip, started_at, ended_at, sea_state, visibility)
            Sighting(id, trip_id -> Trip, species, count, bearing_deg, distance_m, lat, lng, seen_at)
Features:   - Log survey effort periods with sea state
            - Record sightings with species, count, bearing and distance
            - Stamp each record with GPS and time
            - Work offline at sea
            - Export records as CSV
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, geolocator
```

---

## Example 306

**Intent:**
helo, i am from vietnam, i want app to learn english word with picture and sound for my children, no internet needed

**Spec:**
```
Type:       Mobile application (kids picture vocabulary)
Data model: Word(id, english, vietnamese, image_path, audio_path, topic)
            Progress(word_id -> Word, stars)
Features:   - Show picture cards with English word and spoken audio
            - Show the Vietnamese meaning on tap
            - Play a listening game where the child taps the right picture
            - Award stars for correct answers
            - Work fully offline
Storage:    Local on-device storage (bundled media)
Tech stack: Flutter, audioplayers, Hive
```

---

## Example 307

**Intent:**
app for learn korean hangul, i am brazilian

**Spec:**
```
Type:       Mobile application (Hangul trainer)
Data model: Jamo(id, character, romanization, type, audio_path)
            Syllable(id, text, jamo_ids)
            Attempt(id, item, correct, answered_at)
Features:   - Teach consonants and vowels with sounds
            - Show how jamo combine into syllable blocks
            - Quiz reading syllables aloud with audio answers
            - Let the user build syllables by dragging jamo
            - Show the interface in Portuguese
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 308

**Intent:**
please make me app for german articles der die das, i always make mistake

**Spec:**
```
Type:       Mobile application (German noun gender drill)
Data model: Noun(id, word, article, plural, english, frequency_rank)
            Review(noun_id -> Noun, ease, due_on)
Features:   - Show a noun and ask for der, die or das
            - Colour-code nouns by gender after answering
            - Teach ending rules like -ung is feminine
            - Review mistakes with spaced repetition
            - Start with the most frequent nouns
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 309

**Intent:**
I am learning Italian and want to listen to short dialogues and answer questions on the train without internet

**Spec:**
```
Type:       Mobile application (listening comprehension)
Data model: Dialogue(id, title, level, audio_path, transcript)
            Question(id, dialogue_id -> Dialogue, text, options, answer)
            Result(dialogue_id -> Dialogue, score, done_on)
Features:   - Play short dialogues with adjustable speed
            - Show comprehension questions after listening
            - Reveal the transcript with translations on tap
            - Download lesson packs by CEFR level
            - Track scores per level
Storage:    Local on-device storage
Tech stack: React Native, expo-av, expo-file-system
```

---

## Example 310

**Intent:**
irregular english verbs quiz for my students (I'm english teacher in turkey)

**Spec:**
```
Type:       Mobile application (irregular verb quiz)
Data model: Verb(id, base, past, participle, turkish)
            Attempt(id, verb_id -> Verb, form, correct, answered_at)
Features:   - Quiz past simple and past participle forms
            - Show Turkish meanings as hints
            - Group verbs by pattern like sing-sang-sung
            - Run timed challenge rounds
            - Show weakest verbs
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 311

**Intent:**
numbers in french listening, they say 97 and i must type it

**Spec:**
```
Type:       Mobile application (number listening drill)
Data model: Attempt(id, number, typed, correct, answered_at)
            Settings(min, max, speed)
Features:   - Speak random numbers with text-to-speech
            - Let the user type what they heard
            - Choose number ranges like 70-99 or years
            - Include prices and phone numbers
            - Show accuracy by range
Storage:    Local on-device storage
Tech stack: Kotlin, Android TextToSpeech, Jetpack Compose
```

---

## Example 312

**Intent:**
chord progression generator for songwriting

**Spec:**
```
Type:       Mobile application (songwriting chord helper)
Data model: Progression(id, name, key, chords, bpm)
Features:   - Choose a key and mood
            - Generate progressions from common patterns like I-V-vi-IV
            - Play progressions with a piano or guitar sound
            - Substitute chords with suggestions
            - Save progressions for songs
Storage:    Local on-device storage
Tech stack: Swift, AudioKit, SwiftUI
```

---

## Example 313

**Intent:**
guitar scale practice with backing track

**Spec:**
```
Type:       Mobile application (scale practice)
Features:   - Show scale shapes on a fretboard diagram
            - Play a backing track in the chosen key
            - Highlight root notes
            - Cycle through positions
            - Loop and change tempo
Tech stack: Kotlin, Jetpack Compose, ExoPlayer
```

---

## Example 314

**Intent:**
banjo roll patterns with metronome for practice

**Spec:**
```
Type:       Mobile application (banjo roll trainer)
Data model: Roll(id, name, pattern, finger_sequence)
            Practice(id, roll_id -> Roll, bpm, minutes, done_on)
Features:   - Show roll patterns in tab with finger labels
            - Play the roll at a chosen tempo
            - Increase tempo gradually
            - Log practice time per roll
            - Show highest clean tempo
Storage:    Local on-device storage
Tech stack: Flutter, just_audio, Hive
```

---

## Example 315

**Intent:**
bagpipe practice chanter tune book app with gracenotes

**Spec:**
```
Type:       Mobile application (pipe tune book)
Data model: Tune(id, title, type, time_signature, notation_path, audio_path)
            Practice(tune_id -> Tune, practised_on, minutes)
Features:   - Store tunes as sheet music images or ABC notation
            - Play audio at slower speeds
            - Filter tunes by type like march or jig
            - Log practice time
            - Build sets of tunes for competitions
Storage:    Local on-device database (SQLite)
Tech stack: React Native, abcjs (in WebView), expo-av
```

---

## Example 316

**Intent:**
audiobook speed reader for dyslexic teens that highlights each word

**Spec:**
```
Type:       Mobile application (read-along player)
Data model: Book(id, title, text_path, audio_path, sync_map_path)
            Progress(book_id -> Book, position_ms)
Features:   - Play audio with each word highlighted in sync
            - Adjust speed without changing pitch
            - Tap a word to hear it again
            - Use a dyslexia-friendly font
            - Remember the position in each book
Storage:    Local on-device storage
Tech stack: Kotlin, ExoPlayer, Jetpack Compose
```

---

## Example 317

**Intent:**
speech therapy practice app for my son who has a lisp, record s sounds

**Spec:**
```
Type:       Mobile application (articulation practice)
Data model: Word(id, text, target_sound, position, picture_path)
            Recording(id, word_id -> Word, file_path, recorded_on, parent_rating)
Features:   - Show picture words with the target sound at the start, middle or end
            - Record the child saying each word
            - Play back next to a model recording
            - Let the parent rate each attempt
            - Show progress per sound position
Storage:    Local on-device database (SQLite)
Tech stack: Swift, AVFoundation, SwiftUI
```

---

## Example 318

**Intent:**
stutter fluency app, practice slow speech with a pacing guide

**Spec:**
```
Type:       Mobile application (fluency practice)
Data model: Session(id, done_on, technique, minutes, self_rating)
            Passage(id, text, level)
Features:   - Show reading passages with a pacing guide that highlights syllables
            - Play delayed auditory feedback through headphones
            - Record practice and rate fluency
            - Log daily practice minutes
            - Show progress over weeks
Storage:    Local on-device storage
Tech stack: Kotlin, Oboe, Jetpack Compose
```

---

## Example 319

**Intent:**
visual timer for autistic kids that shows time running out as a coloured disc

**Spec:**
```
Type:       Mobile application (visual timer)
Data model: Preset(id, name, minutes, colour, sound)
Features:   - Show remaining time as a shrinking coloured disc
            - Hide numbers for children who can't read the clock
            - Play a gentle sound when time is up
            - Save presets for common activities
            - Show a "first, then" board with two picture cards
Storage:    Local on-device storage
Tech stack: Flutter, CustomPainter, Hive
```

---

## Example 320

**Intent:**
social stories maker for my autistic daughter with photos

**Spec:**
```
Type:       Mobile application (social story builder)
Data model: Story(id, title, created_at)
            Page(id, story_id -> Story, position, photo_path, text, audio_path)
Features:   - Create stories page by page with photos and short text
            - Record a parent's voice for each page
            - Read stories with swipe navigation
            - Use a calm, simple layout
            - Export stories as PDF to share with school
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVFoundation, PDFKit
```

---

## Example 321

**Intent:**
one-handed keyboard practice app for stroke recovery

**Spec:**
```
Type:       Mobile application (fine motor rehab exercises)
Data model: Exercise(id, name, type, level)
            Result(id, exercise_id -> Exercise, done_on, accuracy, time_s, hand)
Features:   - Run tapping, tracing and pinching exercises
            - Measure accuracy and time per exercise
            - Increase difficulty as scores improve
            - Record which hand was used
            - Share progress with a therapist
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 322

**Intent:**
emergency SOS for hiking that sends my location by sms when I hold the button

**Spec:**
```
Type:       Mobile application (SOS location sender)
Data model: Contact(id, name, phone)
            SosEvent(id, sent_at, lat, lng, accuracy_m)
Features:   - Send an SMS with GPS coordinates when the SOS button is held
            - Include a map link and battery level
            - Fall back to last known location if GPS is slow
            - Repeat the message every 10 minutes until cancelled
            - Show coordinates on screen to read out by phone
Storage:    Local on-device storage
Tech stack: Kotlin, Android SmsManager, Fused Location Provider
```

---

## Example 323

**Intent:**
what3words style - just show my grid reference for mountain rescue

**Spec:**
```
Type:       Mobile application (grid reference display)
Features:   - Show the current position as an OS grid reference and lat/long
            - Show GPS accuracy in metres
            - Read the location aloud
            - Copy or share the position by SMS
            - Work with no data connection
Tech stack: Swift, CoreLocation, SwiftUI
```

---

## Example 324

**Intent:**
compass app with declination and bearing to a saved point

**Spec:**
```
Type:       Mobile application (navigation compass)
Data model: Waypoint(id, name, lat, lng)
Features:   - Show a compass with true and magnetic north
            - Apply magnetic declination for the location
            - Save waypoints
            - Show bearing and distance to a waypoint
            - Lock a bearing to follow
Storage:    Local on-device storage
Tech stack: Kotlin, Android SensorManager, GeomagneticField, Jetpack Compose
```

---

## Example 325

**Intent:**
forest fire lookout app for reporting smoke with bearing from my tower

**Spec:**
```
Type:       Mobile application with backend (fire lookout reporting)
Auth:       Lookout staff login
Data model: Tower(id, name, lat, lng)
            SmokeReport(id, tower_id -> Tower, bearing_deg, estimated_distance_km, colour, size, reported_at, photo_path)
Features:   - Record smoke sightings with compass bearing
            - Attach a zoomed photo
            - Send reports to the dispatch centre
            - Plot intersecting bearings from multiple towers to locate the fire
            - Queue reports offline on poor signal
API:        REST
            POST /reports
            GET  /reports/active
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, NestJS, PostGIS
```

---

## Example 326

**Intent:**
snow plow route checklist for our municipal drivers

**Spec:**
```
Type:       Mobile application with backend (plough route tracker)
Auth:       Driver login with employee ID
Data model: Route(id, name, priority)
            Segment(id, route_id -> Route, name, geometry)
            Pass(id, segment_id -> Segment, driver_id, passed_at, salted)
Features:   - Show the driver's assigned route on a map
            - Mark segments as ploughed or salted automatically from GPS
            - Show uncleared segments to supervisors
            - Log salt usage
            - Work offline in poor coverage
API:        REST
            GET  /drivers/me/route
            POST /passes/batch
            GET  /segments/status
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin, MapLibre, Spring Boot, PostGIS
```

---

## Example 327

**Intent:**
elevator inspection app for technicians checklists per lift

**Spec:**
```
Type:       Mobile application with backend (lift inspection)
Auth:       Technician login
Data model: Lift(id, building, serial, qr_code)
            Checklist(id, name, items)
            Inspection(id, lift_id -> Lift, checklist_id -> Checklist, inspected_at, results_json, signature_path)
Features:   - Scan the lift's QR code to open its record
            - Complete the inspection checklist with pass or fail
            - Photograph faults
            - Capture the client signature
            - Generate a certificate PDF
API:        REST
            GET  /lifts/{qr}
            POST /inspections
Storage:    PostgreSQL
Tech stack: Flutter, ASP.NET Core, SQL Server
```

---

## Example 328

**Intent:**
solar panel installer app to measure roof angle and direction and estimate output

**Spec:**
```
Type:       Mobile application (solar site survey)
Data model: Survey(id, address, lat, lng)
            RoofFace(id, survey_id -> Survey, tilt_deg, azimuth_deg, area_m2, shading_percent)
Features:   - Measure roof tilt and azimuth with the phone sensors
            - Record usable area per roof face
            - Estimate annual output from location using PVGIS
            - Suggest panel count
            - Export a survey report
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Android SensorManager, PVGIS API, Room
```

---

## Example 329

**Intent:**
hvac duct sizing calculator for installers

**Spec:**
```
Type:       Mobile application (duct sizing calculator)
Features:   - Calculate duct size from airflow and friction rate
            - Convert between round and rectangular ducts
            - Calculate air velocity
            - Support imperial and metric units
            - Save calculations to jobs
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 330

**Intent:**
pool water chemistry log, chlorine ph alkalinity and how much to add

**Spec:**
```
Type:       Mobile application (pool chemistry log)
Data model: Pool(id, volume_l, type)
            Test(id, pool_id -> Pool, tested_on, free_chlorine, ph, alkalinity, cya, calcium)
            Dose(id, test_id -> Test, chemical, amount_g)
Features:   - Log test results
            - Compare readings against target ranges
            - Calculate chemical doses for the pool volume
            - Chart readings over the season
            - Remind to test twice a week
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, fl_chart
```

---

## Example 331

**Intent:**
hot tub maintenance reminders, water change, filter cleaning

**Spec:**
```
Type:       Mobile application (hot tub care)
Data model: Task(id, name, interval_days, last_done_on)
            WaterTest(id, tested_on, bromine, ph)
Features:   - Remind filter rinse, deep clean and water change
            - Log water tests
            - Suggest chemical amounts
            - Track filter replacement dates
            - Show a simple status screen
Storage:    Local on-device storage
Tech stack: React Native, AsyncStorage, Notifee
```

---

## Example 332

**Intent:**
generator and sump pump test log for my house

**Spec:**
```
Type:       Mobile application (backup equipment test log)
Data model: Equipment(id, name, type, test_interval_days)
            Test(id, equipment_id -> Equipment, tested_on, runtime_min, passed, note)
Features:   - List backup equipment like generators and sump pumps
            - Remind when a test run is due
            - Log test runs with pass or fail
            - Track fuel and oil changes
            - Show overdue tests
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 333

**Intent:**
snow day / storm prep checklist for my family with supplies count

**Spec:**
```
Type:       Mobile application (emergency preparedness kit)
Data model: Supply(id, name, category, quantity, needed_per_person_per_day, expires_on)
            Household(people, days_target)
Features:   - Calculate supplies needed for the household and days
            - Track current stock and expiry dates
            - Show shortfalls as a shopping list
            - Keep a family emergency plan with meeting points
            - Remind to rotate food and water every 6 months
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 334

**Intent:**
water heater and furnace age tracker so i know when to replace

**Spec:**
```
Type:       Mobile application (appliance lifespan tracker)
Data model: Appliance(id, name, installed_on, expected_life_years, model, serial, price)
Features:   - Record install dates and expected lifespan
            - Show remaining life as a bar
            - Warn when an appliance passes 80% of its life
            - Look up age from serial number formats
            - Estimate a replacement budget by year
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 335

**Intent:**
lawn mowing and fertilising schedule with weather

**Spec:**
```
Type:       Mobile application (lawn care schedule)
Data model: Lawn(id, area_m2, grass_type)
            Treatment(id, lawn_id -> Lawn, type, product, applied_on)
            MowLog(id, lawn_id -> Lawn, mowed_on, height_mm)
Features:   - Plan fertiliser, weed and seed treatments by season
            - Calculate product amounts from lawn area
            - Skip treatment reminders when rain is forecast
            - Log mowing with cut height
            - Show the season plan on a calendar
Storage:    Local on-device storage
Tech stack: Kotlin, Open-Meteo API, Room
```

---

## Example 336

**Intent:**
rv camper maintenance and checklist before trips

**Spec:**
```
Type:       Mobile application (RV maintenance)
Data model: Rv(id, name, year)
            System(id, rv_id -> Rv, name, interval_months, last_service_on)
            Checklist(id, name, items)
Features:   - Track systems like roof seals, generator and water heater
            - Remind service dates
            - Run departure and arrival checklists
            - Log tank dumps and propane fills
            - Store dimensions for bridge clearance
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 337

**Intent:**
track hours on my lawn tractor and chainsaw for oil changes

**Spec:**
```
Type:       Mobile application (small engine service log)
Data model: Machine(id, name, type, hours)
            Service(id, machine_id -> Machine, type, done_at_hours, done_on, parts)
Features:   - Log engine hours after each use
            - Set service intervals by hours
            - Remind when oil, spark plug or air filter is due
            - Record parts and costs
            - Store manuals and part numbers
Storage:    Local on-device storage
Tech stack: React Native, expo-sqlite
```

---

## Example 338

**Intent:**
bike lock code and frame number keeper in case its stolen

**Spec:**
```
Type:       Mobile application (bike registry)
Data model: Bike(id, make, model, colour, frame_number, purchase_price, purchased_on, photo_paths, lock_code)
Features:   - Store frame numbers, photos and receipts
            - Keep lock codes behind Face ID
            - Generate a stolen bike report PDF
            - Share details quickly with police
            - Back up an encrypted file
Storage:    Local on-device storage (encrypted)
Tech stack: Swift, LocalAuthentication, CryptoKit, SwiftUI
```

---

## Example 339

**Intent:**
kids allowance where they ask to spend and i approve, like bank for kids

**Spec:**
```
Type:       Mobile application with backend (family allowance ledger)
Auth:       Parent login with email; children log in with a PIN on a linked device
Data model: Family(id)
            Child(id, family_id -> Family, name, balance)
            SpendRequest(id, child_id -> Child, amount, reason, status)
            Transaction(id, child_id -> Child, amount, type, created_at)
Features:   - Pay allowance automatically each week
            - Let children request to spend with a reason
            - Let parents approve or decline on their phone
            - Show children their balance and history
            - Let parents add bonuses for chores
API:        REST
            GET  /children/{id}/balance
            POST /requests
            PATCH /requests/{id}
            POST /children/{id}/transactions
Storage:    PostgreSQL
Tech stack: React Native, Express, PostgreSQL
```

---

## Example 340

**Intent:**
chore wheel for roommates, rotates every week

**Spec:**
```
Type:       Mobile application with backend (roommate chore rotation)
Auth:       Email login, household joined by invite
Data model: Household(id, name)
            Member(id, household_id -> Household, name)
            Chore(id, household_id -> Household, name)
            Assignment(id, chore_id -> Chore, member_id -> Member, week_start, done)
Features:   - Rotate chores between members every week
            - Show a spinning wheel animation
            - Mark chores as done
            - Remind members on Sunday evening
            - Show who skips most often
API:        REST
            GET  /households/{id}/assignments
            PATCH /assignments/{id}
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase
```

---

## Example 341

**Intent:**
points for chores my kids can spend on screen time not money

**Spec:**
```
Type:       Mobile application (chore points for screen time)
Data model: Child(id, name, points)
            Chore(id, name, points)
            Redemption(id, child_id -> Child, minutes, points_spent, redeemed_at)
Features:   - Award points for completed chores
            - Convert points to screen time minutes
            - Start a screen time countdown when redeemed
            - Show each child's points
            - Require a parent PIN to approve
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 342

**Intent:**
teen driver app that tells me if my son speeds

**Spec:**
```
Type:       Mobile application with backend (teen driving monitor)
Auth:       Parent and teen accounts linked by family code
Data model: Driver(id, name)
            Trip(id, driver_id -> Driver, started_at, ended_at, distance_km, max_speed_kmh, hard_brakes, phone_use_s)
            Alert(id, trip_id -> Trip, type, at)
Features:   - Detect trips automatically on the teen's phone
            - Compare speed with posted limits from map data
            - Detect hard braking and phone handling while driving
            - Send the parent a trip summary
            - Score each week's driving
API:        REST
            POST /trips
            GET  /drivers/{id}/trips
Storage:    PostgreSQL
Tech stack: Kotlin, Activity Recognition API, Spring Boot, HERE Maps API
```

---

## Example 343

**Intent:**
homeschool attendance and subject hours log

**Spec:**
```
Type:       Mobile application (homeschool record keeper)
Data model: Student(id, name, grade)
            Subject(id, name)
            Lesson(id, student_id -> Student, subject_id -> Subject, date, minutes, notes)
Features:   - Log lessons per student and subject
            - Total instructional days and hours
            - Show progress against the state's required days
            - Attach work samples as photos
            - Export an annual report
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, pdf
```

---

## Example 344

**Intent:**
baby bath temp and room temp check w a bluetooth thermometer

**Spec:**
```
Type:       Mobile application (nursery temperature monitor)
Data model: Sensor(id, name, mac_address, location)
            Reading(id, sensor_id -> Sensor, temp_c, humidity, read_at)
Features:   - Pair Bluetooth LE temperature sensors
            - Show nursery and bath temperatures live
            - Alert when the nursery is too hot or cold
            - Suggest clothing layers for the room temperature
            - Chart overnight readings
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_blue_plus, sqflite
```

---

## Example 345

**Intent:**
breastfeeding app but in react native and i want it to work on apple watch too

**Spec:**
```
Type:       Mobile application (breastfeeding timer)
Data model: Feed(id, side, started_at, ended_at)
            Settings(reminder_interval_min)
Features:   - Start and switch sides with large buttons
            - Remember which side to start on next
            - Start and stop feeds from an Apple Watch
            - Show feeds per day and average length
            - Remind when the next feed is likely due
Storage:    Local on-device storage (SQLite), synced to the watch with WatchConnectivity
Tech stack: React Native, react-native-watch-connectivity, SwiftUI (watchOS)
```

---

## Example 346

**Intent:**
newborn jaundice check log, the nurse said watch the yellow colour and wet diapers

**Spec:**
```
Type:       Mobile application (newborn health checklist)
Data model: Baby(id, name, born_at)
            DailyCheck(id, baby_id -> Baby, date, skin_colour_score, wet_diapers, dirty_diapers, feeds, photo_path)
Features:   - Log daily skin colour with photo and a reference card
            - Count wet and dirty diapers against day-of-life targets
            - Show warning signs that need a doctor
            - Remind checks for the first two weeks
            - Share the log with the midwife
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, CameraX, Room, Jetpack Compose
```

---

## Example 347

**Intent:**
preemie nicu journal for parents, weight grams each day and milestones like first cuddle

**Spec:**
```
Type:       Mobile application (NICU journey journal)
Data model: Baby(id, name, born_at, gestation_weeks)
            Weight(id, baby_id -> Baby, grams, weighed_on)
            Milestone(id, baby_id -> Baby, title, date, photo_path, note)
Features:   - Log daily weights in grams
            - Show corrected age alongside actual age
            - Record milestones like first hold and first bottle
            - Keep a diary of questions for the doctors
            - Create a printable journey book
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 348

**Intent:**
so my partner is pregnant and i want an app for dads, weekly what to expect and a list of things i should do

**Spec:**
```
Type:       Mobile application (pregnancy guide for partners)
Data model: WeekContent(week, summary, partner_tips)
            Task(id, title, due_week, done)
Features:   - Calculate the current week from the due date
            - Show weekly baby development and how the mother may feel
            - Suggest practical tasks for the partner each week
            - Track appointments to attend
            - Share progress with the mother's app by text
Storage:    Local on-device storage (bundled content)
Tech stack: Flutter, Hive
```

---

## Example 349

**Intent:**
ovulation tracker with temps and test strips

**Spec:**
```
Type:       Mobile application (fertility tracker)
Data model: Cycle(id, started_on)
            DailyEntry(id, date, bbt_c, lh_result, cervical_mucus, intercourse)
Features:   - Log basal body temperature daily
            - Record LH test strip results with a photo
            - Detect the temperature shift to confirm ovulation
            - Predict the fertile window for the next cycle
            - Keep data private on the device
Storage:    Local on-device database (encrypted SQLite)
Tech stack: Kotlin, Jetpack Compose, SQLCipher
```

---

## Example 350

**Intent:**
postpartum pelvic floor exercise timer

**Spec:**
```
Type:       Mobile application (pelvic floor trainer)
Data model: Program(id, level, hold_s, rest_s, reps, quick_flicks)
            Session(id, program_id -> Program, done_at)
Features:   - Guide holds and rests with vibration and animation
            - Include quick flick sets
            - Progress through levels over weeks
            - Remind three times a day discreetly
            - Track sessions completed
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, Core Haptics
```

---

## Example 351

**Intent:**
my mom lives far away. I want a shared photo frame app where I send pics from my phone and they show on an old tablet at her house

**Spec:**
```
Type:       Mobile application with backend (family photo frame)
Auth:       Family members log in with email; the frame tablet pairs with a code
Data model: Frame(id, name, pairing_code)
            Member(id, email)
            Photo(id, frame_id -> Frame, member_id -> Member, storage_key, caption, sent_at)
Features:   - Send photos with captions to a frame
            - Run the tablet in full-screen slideshow mode
            - Show new photos first with a "new" badge
            - Let the senior tap a heart to send a like back
            - Turn the screen off at night
API:        REST
            POST /frames/pair
            POST /frames/{id}/photos
            GET  /frames/{id}/photos?since=
Storage:    Firebase Storage, Firestore
Tech stack: Flutter, Firebase
```

---

## Example 352

**Intent:**
medication video call reminder for grandpa - app rings like a call and shows the pill to take

**Spec:**
```
Type:       Mobile application (senior medication prompt)
Data model: Medication(id, name, photo_path, dose, times)
            Confirmation(id, medication_id -> Medication, scheduled_at, confirmed_at)
Features:   - Show a full-screen incoming-call style alert at each dose time
            - Show a large photo of the pill and dose
            - Confirm with one big button
            - Repeat the alert if not confirmed
            - Text a family member after two missed confirmations
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Android full-screen intent notifications, SmsManager
```

---

## Example 353

**Intent:**
wandering alert for dementia, geofence around house

**Spec:**
```
Type:       Mobile application with backend (dementia safe zone)
Auth:       Caregiver email login; patient phone linked by code
Data model: Patient(id, name, phone)
            SafeZone(id, patient_id -> Patient, lat, lng, radius_m, active_hours)
            LocationPing(id, patient_id -> Patient, lat, lng, at)
Features:   - Draw safe zones on a map around home
            - Track the patient's phone location in the background
            - Alert caregivers when the phone leaves a zone
            - Show the live location and recent path
            - Only alert during set hours
API:        REST
            POST /pings
            GET  /patients/{id}/location
            PUT  /patients/{id}/zones
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin, Geofencing API, Go, PostGIS
```

---

## Example 354

**Intent:**
memory games for my nan with dementia, simple and big

**Spec:**
```
Type:       Mobile game (memory exercises for seniors)
Data model: Session(id, game, score, played_at)
Features:   - Offer matching pairs, word recall and sequence games
            - Use large cards and high contrast
            - Adjust difficulty automatically
            - Use family photos as card images
            - Show scores to family over time
Storage:    Local on-device storage
Tech stack: Flutter, Flame
```

---

## Example 355

**Intent:**
hydration reminders for care home residents, staff tap who drank

**Spec:**
```
Type:       Mobile application (care home fluid chart)
Data model: Resident(id, name, room, target_ml)
            Drink(id, resident_id -> Resident, ml, given_at, staff_initials)
Features:   - Show residents as a grid with today's totals
            - Log drinks with preset cup sizes
            - Highlight residents behind their target by midday
            - Export daily fluid charts
            - Work on a shared ward tablet
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 356

**Intent:**
pressure sore turning chart for bedbound patient at home

**Spec:**
```
Type:       Mobile application (repositioning chart)
Data model: Patient(id, name, turn_interval_h)
            Turn(id, patient_id -> Patient, position, turned_at, skin_check, carer)
Features:   - Remind carers when the next turn is due
            - Log the new position like left, right or back
            - Suggest the next position in rotation
            - Record skin checks
            - Export the chart for district nurses
Storage:    Local on-device storage
Tech stack: React Native, expo-sqlite, Notifee
```

---

## Example 357

**Intent:**
food diary for my toddler who wont eat, track what he tried and how much

**Spec:**
```
Type:       Mobile application (picky eater log)
Data model: Food(id, name, category, colour, texture)
            Exposure(id, food_id -> Food, offered_at, amount_eaten, reaction)
Features:   - Log foods offered with amount eaten
            - Count exposures to each new food
            - Suggest similar foods using food chaining
            - Show variety by colour and food group
            - Celebrate new foods tried
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 358

**Intent:**
bedtime story recorder so grandparents can record stories and kids play them

**Spec:**
```
Type:       Mobile application with backend (recorded bedtime stories)
Auth:       Family group with email login
Data model: Family(id)
            Recording(id, family_id -> Family, reader_name, title, audio_key, cover_path, duration_s)
Features:   - Record a story with the book's cover photo
            - Share recordings with the family group
            - Play stories in a simple kids mode
            - Add a sleep timer
            - Download stories for offline playback
API:        REST
            POST /recordings
            GET  /families/{id}/recordings
Storage:    Firebase Storage, Firestore
Tech stack: Flutter, Firebase, just_audio
```

---

## Example 359

**Intent:**
kids reward chart for good behavior, stars and a prize

**Spec:**
```
Type:       Mobile application (reward chart)
Data model: Child(id, name)
            Behaviour(id, name)
            Star(id, child_id -> Child, behaviour_id -> Behaviour, earned_at)
            Prize(id, child_id -> Child, name, stars_needed, claimed)
Features:   - Award stars for chosen behaviours
            - Show a colourful chart per child
            - Set a prize with the number of stars needed
            - Celebrate when a prize is unlocked
            - Reset charts weekly
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, Lottie
```

---

## Example 360

**Intent:**
daycare app where teachers log naps meals diapers and parents see it live

**Spec:**
```
Type:       Mobile application with backend (daycare daily report)
Auth:       Staff and parent accounts with email login
Data model: Centre(id, name)
            Child(id, centre_id -> Centre, name, room)
            ActivityLog(id, child_id -> Child, type, details, logged_at, staff_id)
            Guardian(id, child_id -> Child, email)
Features:   - Let staff log meals, naps, diapers and activities quickly for several children
            - Push updates to parents in real time
            - Share photos with only the relevant parents
            - Send a daily summary at pickup
            - Record check-in and check-out times
API:        REST
            POST /logs
            GET  /children/{id}/logs?date=
            POST /attendance
Storage:    PostgreSQL, S3 for photos
Tech stack: React Native, Ruby on Rails, PostgreSQL
```

---

## Example 361

**Intent:**
lice check reminder lol school has outbreak again

**Spec:**
```
Type:       Mobile application (head lice treatment tracker)
Data model: Child(id, name)
            Check(id, child_id -> Child, checked_on, found)
            Treatment(id, child_id -> Child, product, treated_on)
Features:   - Log comb checks per child
            - Schedule a repeat treatment 7-10 days later
            - Remind every few days during an outbreak
            - Show a checklist for washing bedding
            - Keep a history per child
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 362

**Intent:**
pocket money app in swiftui, simple, one kid, add and subtract with reason

**Spec:**
```
Type:       Mobile application (pocket money ledger)
Data model: Entry(id, amount, reason, created_at)
Features:   - Add money with a reason
            - Subtract spending with a reason
            - Show the current balance large
            - Show a history list
            - Add a weekly allowance automatically
Storage:    Local on-device storage (SwiftData)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 363

**Intent:**
lost tooth? no, lost dog? no... lost KEYS. bluetooth tag finder app for cheap tags

**Spec:**
```
Type:       Mobile application (Bluetooth tag finder)
Data model: Tag(id, name, mac_address, last_lat, last_lng, last_seen_at)
Features:   - Pair low-cost Bluetooth LE tags
            - Show a hot-and-cold signal strength meter
            - Ring the tag
            - Record where the tag was last seen
            - Alert when leaving a tag behind
Storage:    Local on-device storage
Tech stack: Kotlin, Android Bluetooth LE, Jetpack Compose
```

---

## Example 364

**Intent:**
bus timetable offline for my rural route that only runs 3 times a day

**Spec:**
```
Type:       Mobile application (offline timetable)
Data model: Route(id, name)
            Stop(id, route_id -> Route, name, order)
            Departure(id, stop_id -> Stop, time, days)
Features:   - Show the next departures from the chosen stop
            - Work offline with timetables stored on the phone
            - Mark school holiday and Sunday schedules
            - Remind before the last bus
            - Update timetables when online
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 365

**Intent:**
im deaf and want my phone to flash when my name is said in the office

**Spec:**
```
Type:       Mobile application (name call alert)
Data model: Keyword(id, word)
            Detection(id, keyword, detected_at)
Features:   - Listen for chosen keywords with on-device speech recognition
            - Flash the screen and vibrate on detection
            - Show the sentence that was heard
            - Run in the background with low battery use
            - Log detections
Storage:    Local on-device storage
Tech stack: Swift, Speech framework, AVAudioEngine
```

---

## Example 366

**Intent:**
car seat expiry and recall checker

**Spec:**
```
Type:       Mobile application (car seat safety tracker)
Data model: CarSeat(id, brand, model, serial, manufactured_on, expires_on, child_name, installed_in)
Features:   - Scan the seat's label for model and date
            - Calculate the expiry date
            - Check recall lists for the model
            - Remind before expiry
            - Store install notes and the manual
Storage:    Local on-device storage
Tech stack: Kotlin, ML Kit, Room
```

---

## Example 367

**Intent:**
wedding guest app where guests see the schedule, the venue map and the dress code

**Spec:**
```
Type:       Mobile application with backend (wedding guest guide)
Auth:       Guests log in with an invite code
Data model: Wedding(id, couple_names, date)
            Event(id, wedding_id -> Wedding, name, starts_at, location, dress_code)
            Guest(id, wedding_id -> Wedding, name, code, rsvp)
Features:   - Show the schedule of events
            - Show venue locations with directions
            - Show dress code and accommodation details
            - Let guests RSVP and choose meals
            - Push updates from the couple
API:        REST
            GET  /weddings/{id}
            GET  /weddings/{id}/events
            PATCH /guests/{id}/rsvp
Storage:    Supabase (PostgreSQL)
Tech stack: React Native, Supabase
```

---

## Example 368

**Intent:**
wedding budget for indian wedding, lots of events mehndi sangeet etc

**Spec:**
```
Type:       Mobile application (multi-event wedding budget)
Data model: Wedding(id, total_budget)
            Event(id, wedding_id -> Wedding, name, date, guest_count)
            Expense(id, event_id -> Event, category, vendor, estimated, actual, paid)
Features:   - Budget separately for each event like mehndi, sangeet and reception
            - Track estimated and actual costs by category
            - Show per-guest cost per event
            - Track payments due to vendors
            - Show totals across all events
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 369

**Intent:**
dress fitting appointment and alterations tracker for brides at my bridal shop

**Spec:**
```
Type:       Mobile application with backend (bridal alterations)
Auth:       Staff login
Data model: Bride(id, name, phone, wedding_date)
            Dress(id, bride_id -> Bride, style, size, ordered_on, arrived_on)
            Fitting(id, dress_id -> Dress, scheduled_at, notes, alterations, seamstress)
Features:   - Track dress orders and arrival
            - Book fittings working back from the wedding date
            - Record alterations needed per fitting
            - Text brides appointment reminders
            - Show the seamstress workload
API:        REST
            GET  /fittings?week=
            POST /fittings
            PATCH /dresses/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Twilio
```

---

## Example 370

**Intent:**
house moving inventory for movers to quote, count furniture per room and estimate volume

**Spec:**
```
Type:       Mobile application (removal survey)
Data model: Survey(id, customer, address, date)
            FurnitureType(id, name, volume_m3)
            RoomItem(id, survey_id -> Survey, room, type_id -> FurnitureType, quantity)
Features:   - Count furniture room by room from a list
            - Calculate total volume in cubic metres
            - Suggest van size and crew
            - Note access issues like stairs
            - Generate a quote PDF
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 371

**Intent:**
utility setup checklist for new apartment, internet, power, renter insurance

**Spec:**
```
Type:       Mobile application (new home setup checklist)
Data model: Service(id, name, provider, account_no, start_date, monthly_cost, status)
Features:   - List services to set up for a new home
            - Track provider, account number and start date
            - Remind of setup deadlines before move-in
            - Show total monthly costs
            - Store provider phone numbers
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 372

**Intent:**
storage unit inventory, whats in my storage unit across town

**Spec:**
```
Type:       Mobile application (storage unit inventory)
Data model: Unit(id, facility, number, rent, access_code)
            Container(id, unit_id -> Unit, label, position, photo_path)
            Item(id, container_id -> Container, name)
Features:   - Record containers with position in the unit
            - Photograph contents
            - Search items across containers
            - Store the access code securely
            - Remind of rent due dates
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, expo-secure-store
```

---

## Example 373

**Intent:**
closet declutter app one in one out

**Spec:**
```
Type:       Mobile application (declutter tracker)
Data model: Item(id, name, category, photo_path, added_on, last_used_on, status)
Features:   - Photograph items and tag categories
            - Ask monthly whether items were used
            - Suggest items to donate
            - Track donated and sold items
            - Show progress as items removed
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 374

**Intent:**
garage sale pricing and sales tally for the day

**Spec:**
```
Type:       Mobile application (yard sale tracker)
Data model: Item(id, name, price, sold_price, sold, seller)
            Sale(id, date, location)
Features:   - Add items with prices
            - Mark items sold with the final price
            - Split earnings between family members
            - Show total takings
            - Record items left over to donate
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose
```

---

## Example 375

**Intent:**
guitar tuner using flutter, standard plus half step down

**Spec:**
```
Type:       Mobile application (guitar tuner)
Features:   - Read microphone input
            - Detect pitch with an FFT and harmonic product spectrum
            - Show the closest string and cents offset
            - Support standard and half-step-down tuning
            - Auto-detect which string is played
Tech stack: Flutter, flutter_audio_capture, pitch_detector_dart
```

---

## Example 376

**Intent:**
metronome in kotlin with polyrhythms like 3 against 4

**Spec:**
```
Type:       Mobile application (polyrhythm metronome)
Data model: Preset(id, name, bpm, rhythm_a, rhythm_b)
Features:   - Play two simultaneous pulses like 3:4 or 5:4
            - Use different sounds per pulse
            - Show a circular visualisation of both pulses
            - Mute either pulse to practise
            - Save presets
Storage:    Local on-device storage
Tech stack: Kotlin, Oboe, Jetpack Compose
```

---

## Example 377

**Intent:**
music flashcards for kids learning note names on the staff

**Spec:**
```
Type:       Mobile application (note reading for children)
Data model: Progress(note, correct, wrong)
Features:   - Show notes on a cartoon staff
            - Let children answer by tapping a coloured keyboard
            - Play the note sound
            - Unlock new notes as earlier ones are mastered
            - Reward with characters and stickers
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, AVFoundation
```

---

## Example 378

**Intent:**
recorder fingering chart app for school kids

**Spec:**
```
Type:       Mobile application (recorder fingering chart)
Features:   - Show the fingering diagram for each note
            - Play the note sound on tap
            - Show simple songs with fingerings above each note
            - Quiz fingerings
            - Switch between German and Baroque fingering
Tech stack: Flutter, audioplayers
```

---

## Example 379

**Intent:**
car service history i can hand over when i sell the car

**Spec:**
```
Type:       Mobile application (transferable vehicle history)
Data model: Vehicle(id, vin, make, model, year)
            Record(id, vehicle_id -> Vehicle, type, date, odometer_km, garage, cost, invoice_path)
Features:   - Decode the VIN to fill make, model and year
            - Log services with invoice photos
            - Show a verified-looking timeline of work done
            - Export a full history PDF for buyers
            - Show total cost of ownership
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, NHTSA vPIC API
```

---

## Example 380

**Intent:**
windshield chip and dent damage log for my lease return

**Spec:**
```
Type:       Mobile application (vehicle damage log)
Data model: Vehicle(id, name, lease_end_date)
            Damage(id, vehicle_id -> Vehicle, panel, type, size_mm, photo_path, found_on, repaired_on)
Features:   - Mark damage on a car outline diagram
            - Attach photos with date stamps
            - Measure size against a coin in the photo
            - Show unrepaired damage before lease return
            - Export a damage report
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, PencilKit
```

---

## Example 381

**Intent:**
classic car restoration project tracker, parts ordered, costs, photos

**Spec:**
```
Type:       Mobile application (restoration project log)
Data model: Project(id, car, budget)
            Task(id, project_id -> Project, area, title, status)
            Part(id, project_id -> Project, name, supplier, cost, ordered_on, arrived_on)
            Photo(id, project_id -> Project, path, taken_on, area)
Features:   - Track tasks by area like body, engine and interior
            - Log parts with supplier and arrival
            - Track spending against budget
            - Keep a photo timeline per area
            - Show a before-and-after gallery
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 382

**Intent:**
towing capacity calculator for my truck and caravan

**Spec:**
```
Type:       Mobile application (towing calculator)
Data model: Vehicle(id, name, kerb_kg, gvm_kg, gcm_kg, max_tow_kg, max_ball_kg)
            Trailer(id, name, atm_kg, tare_kg, ball_kg)
Features:   - Enter vehicle and trailer weights
            - Check towing capacity, GCM and ball weight
            - Add payload like passengers and luggage
            - Show a pass or fail for each limit
            - Save combinations
Storage:    Local on-device storage
Tech stack: React Native, AsyncStorage
```

---

## Example 383

**Intent:**
tyre size comparison calculator, if i fit bigger wheels what happens to speedo

**Spec:**
```
Type:       Mobile application (tyre size calculator)
Features:   - Enter current and new tyre sizes like 225/45R17
            - Calculate diameter, circumference and sidewall height
            - Show speedometer error at common speeds
            - Show percentage difference
            - Draw both tyres to scale
Tech stack: Swift, SwiftUI
```

---

## Example 384

**Intent:**
dashcam on my phone that loops and saves when I brake hard

**Spec:**
```
Type:       Mobile application (phone dashcam)
Data model: Clip(id, file_path, started_at, duration_s, lat, lng, protected)
Features:   - Record video in loop segments
            - Delete old segments when storage is full
            - Save and lock clips on hard braking detected by the accelerometer
            - Overlay speed and time on the video
            - Let the user save a clip with a tap
Storage:    Local on-device storage
Tech stack: Kotlin, CameraX, Android SensorManager
```

---

## Example 385

**Intent:**
parking time limit timer and photos of the parking sign

**Spec:**
```
Type:       Mobile application (parking timer)
Data model: Session(id, started_at, limit_minutes, sign_photo, lat, lng)
Features:   - Start a timer with the parking limit
            - Photograph the parking sign
            - Notify 10 minutes before time runs out
            - Show the car's location on a map
            - Add time when the meter is topped up
Storage:    Local on-device storage
Tech stack: Flutter, flutter_local_notifications, google_maps_flutter
```

---

## Example 386

**Intent:**
my car loan, insurance, rego, everything costs, total cost per km

**Spec:**
```
Type:       Mobile application (car cost of ownership)
Data model: Vehicle(id, name, purchase_price, purchased_on)
            Cost(id, vehicle_id -> Vehicle, category, amount, date)
            OdometerReading(id, vehicle_id -> Vehicle, km, read_on)
Features:   - Log all costs by category like fuel, insurance and repairs
            - Record odometer readings
            - Calculate cost per kilometre
            - Estimate depreciation
            - Show monthly cost breakdown
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Room, Vico
```

---

## Example 387

**Intent:**
home repair quotes comparison when I get 3 quotes from contractors

**Spec:**
```
Type:       Mobile application (quote comparison)
Data model: Job(id, title, description)
            Quote(id, job_id -> Job, contractor, phone, amount, start_date, warranty_months, notes, document_path)
Features:   - Create a job and add quotes from contractors
            - Attach quote documents and photos
            - Compare quotes side by side
            - Mark the chosen quote
            - Remind to follow up on missing quotes
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 388

**Intent:**
renovation budget per room with receipts

**Spec:**
```
Type:       Mobile application (renovation budget tracker)
Data model: Room(id, name, budget)
            Expense(id, room_id -> Room, item, supplier, amount, paid_on, receipt_path)
Features:   - Set a budget per room
            - Log expenses with receipt photos
            - Show spend against budget per room
            - Flag rooms over budget
            - Export expenses as CSV
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, expo-image-picker
```

---

## Example 389

**Intent:**
smoke alarm battery and test reminder for every alarm in the house

**Spec:**
```
Type:       Mobile application (smoke alarm tracker)
Data model: Alarm(id, location, type, installed_on, battery_changed_on, expires_on)
            Test(id, alarm_id -> Alarm, tested_on, passed)
Features:   - List each alarm by room
            - Remind monthly tests
            - Remind yearly battery changes
            - Warn when an alarm passes its 10-year life
            - Log test results
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, WorkManager
```

---

## Example 390

**Intent:**
household filters tracker, fridge water filter, air purifier, hoover

**Spec:**
```
Type:       Mobile application (filter replacement tracker)
Data model: Filter(id, appliance, part_number, interval_days, last_changed_on, buy_link)
Features:   - List filters with part numbers
            - Remind when each filter is due
            - Open a saved link to reorder
            - Log changes
            - Show upcoming changes for the month
Storage:    Local on-device storage
Tech stack: Flutter, Hive, flutter_local_notifications
```

---

## Example 391

**Intent:**
warranty tracker that reads email receipts? no just photos ok. but with cloud backup to google drive

**Spec:**
```
Type:       Mobile application (warranty vault with backup)
Auth:       Google sign-in for Drive backup
Data model: Purchase(id, product, store, date, price, warranty_until, receipt_path)
Features:   - Photograph receipts and crop automatically
            - Enter warranty length and calculate end date
            - Remind before warranty ends
            - Back up the database and images to Google Drive
            - Restore from backup on a new phone
Storage:    Local SQLite database, Google Drive app folder backup
Tech stack: Kotlin, Room, Google Drive API, ML Kit Document Scanner
```

---

## Example 392

**Intent:**
subscription free receipt scanner for tax deductions, sole trader

**Spec:**
```
Type:       Mobile application (expense receipt scanner)
Data model: Receipt(id, vendor, date, total, tax, category, image_path, tax_year)
Features:   - Scan receipts with edge detection
            - Extract vendor, date, total and tax with OCR
            - Assign tax categories
            - Show totals by category per tax year
            - Export a CSV and zip of images for the accountant
Storage:    Local on-device database (SQLite)
Tech stack: Swift, VisionKit, Vision, SwiftData
```

---

## Example 393

**Intent:**
espresso machine descaling and backflush reminders

**Spec:**
```
Type:       Mobile application (coffee machine care)
Data model: Machine(id, name, water_hardness)
            Task(id, machine_id -> Machine, type, interval_shots, interval_days, last_done_on, shots_since)
Features:   - Count shots pulled with a quick tap
            - Remind backflushing by shot count
            - Remind descaling based on water hardness
            - Track gasket and filter changes
            - Log tasks done
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, DataStore
```

---

## Example 394

**Intent:**
tea tasting notes for my tea shop customers, staff record which teas they liked

**Spec:**
```
Type:       Mobile application with backend (tea shop customer preferences)
Auth:       Staff login
Data model: Customer(id, name, phone)
            Tea(id, name, type, price_per_100g)
            Preference(id, customer_id -> Customer, tea_id -> Tea, rating, note, recorded_at)
Features:   - Look up a customer by phone
            - Record teas tried and ratings
            - Suggest new teas based on liked types
            - Show purchase history
            - Sync across shop tablets
API:        REST
            GET  /customers?phone=
            POST /preferences
            GET  /customers/{id}/suggestions
Storage:    PostgreSQL
Tech stack: Flutter, FastAPI, PostgreSQL
```

---

## Example 395

**Intent:**
sake tasting log

**Spec:**
```
Type:       Mobile application (sake journal)
Data model: Sake(id, name, brewery, prefecture, grade, polish_ratio, smv, label_photo)
            Tasting(id, sake_id -> Sake, tasted_on, temperature, rating, notes)
Features:   - Log sake with grade and polishing ratio
            - Record the serving temperature
            - Rate and note each tasting
            - Read the Japanese label with OCR and translate
            - Filter by grade and prefecture
Storage:    Local on-device database (SQLite)
Tech stack: Swift, Vision, Translation framework, SwiftUI
```

---

## Example 396

**Intent:**
craft beer check in app but private, only for me, no social

**Spec:**
```
Type:       Mobile application (private beer journal)
Data model: Beer(id, name, brewery, style, abv)
            CheckIn(id, beer_id -> Beer, drank_on, venue, rating, notes, photo_path)
Features:   - Log beers with style and ABV
            - Rate and note each beer
            - Track unique beers and styles tried
            - Show top-rated breweries
            - Keep everything on the device
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Room, Jetpack Compose
```

---

## Example 397

**Intent:**
chocolate tasting flight app for a tasting party, everyone scores on their phone

**Spec:**
```
Type:       Mobile application with backend (blind tasting party)
Auth:       Host creates a session; guests join with a code and nickname
Data model: Session(id, code, host_name)
            Sample(id, session_id -> Session, label, revealed_name)
            Score(id, sample_id -> Sample, guest_name, flavour, texture, overall)
Features:   - Let the host add numbered samples
            - Let guests score each sample on their phone
            - Hide names until the reveal
            - Show results ranked after the reveal
            - Show score averages per category
API:        REST
            POST /sessions
            POST /sessions/{code}/scores
            POST /sessions/{id}/reveal
            GET  /sessions/{id}/results
Storage:    Firebase Firestore
Tech stack: React Native, Firebase
```

---

## Example 398

**Intent:**
olive oil and honey tasting notes for my deli

**Spec:**
```
Type:       Mobile application (deli tasting notes)
Data model: Product(id, type, name, producer, origin, harvest_year)
            Note(id, product_id -> Product, tasted_on, aroma, taste, intensity, rating)
Features:   - Log products with origin and harvest year
            - Use tasting wheels for aroma notes
            - Rate intensity and quality
            - Compare products of the same type
            - Export tasting cards for the shop counter
Storage:    Local on-device storage
Tech stack: Flutter, sqflite, pdf
```

---

## Example 399

**Intent:**
climbing gear retirement tracker, ropes and harness dates and falls

**Spec:**
```
Type:       Mobile application (climbing gear log)
Data model: Gear(id, type, brand, model, bought_on, first_used_on, max_age_years)
            Use(id, gear_id -> Gear, used_on, falls, note)
Features:   - Log ropes, harnesses and slings with dates
            - Record uses and big falls
            - Warn when gear reaches its retirement age
            - Note damage inspections
            - Show retired gear history
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 400

**Intent:**
caving survey app for recording stations distance compass and clino

**Spec:**
```
Type:       Mobile application (cave survey)
Data model: Survey(id, cave, date, team)
            Shot(id, survey_id -> Survey, from_station, to_station, length_m, azimuth_deg, inclination_deg, left, right, up, down)
Features:   - Enter survey shots station to station
            - Read data from a Bluetooth DistoX device
            - Draw a live plan and elevation view
            - Detect loop closure errors
            - Export to Therion and Survex formats
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Android Bluetooth, Jetpack Compose
```

---

## Example 401

**Intent:**
canyoning rope length and rappel log

**Spec:**
```
Type:       Mobile application (canyoning trip log)
Data model: Canyon(id, name, region, rappels)
            Rappel(id, canyon_id -> Canyon, number, height_m, anchor_type)
            Trip(id, canyon_id -> Canyon, date, team, water_level, notes)
Features:   - Store canyons with rappel heights
            - Calculate rope length needed per canyon
            - Log trips with water level
            - Record anchor condition updates
            - Work offline
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 402

**Intent:**
paragliding flight log with thermals and gps track

**Spec:**
```
Type:       Mobile application (paragliding flight log)
Data model: Site(id, name, lat, lng)
            Flight(id, site_id -> Site, launched_at, landed_at, max_alt_m, max_climb_ms, distance_km, igc_path)
Features:   - Record flights with GPS and barometer altitude
            - Show a vario tone for climb rate
            - Mark thermals on the track
            - Export IGC files
            - Show total airtime per year
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Android barometer sensor, Room, MapLibre
```

---

## Example 403

**Intent:**
geocaching trip planner for my family, offline caches on map

**Spec:**
```
Type:       Mobile application (offline cache planner)
Data model: Cache(id, code, name, lat, lng, difficulty, terrain, hint)
            Find(id, cache_id -> Cache, found_on, log_text)
Features:   - Import caches from GPX files
            - Show caches on an offline map
            - Decode hints on tap
            - Navigate with compass and distance
            - Log finds for later upload
Storage:    Local on-device database (SQLite)
Tech stack: Swift, MapKit, SwiftUI
```

---

## Example 404

**Intent:**
hut to hut trek planner for the alps, stages, km, height, bookings

**Spec:**
```
Type:       Mobile application (multi-day trek planner)
Data model: Trek(id, name, start_date)
            Stage(id, trek_id -> Trek, day, from_hut, to_hut, distance_km, ascent_m, hours)
            Booking(id, stage_id -> Stage, hut, confirmed, deposit)
Features:   - Plan stages with distance, ascent and time
            - Track hut bookings and deposits
            - Show the route on an offline topo map
            - Store hut phone numbers
            - Check off stages during the trek
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_map, sqflite
```

---

## Example 405

**Intent:**
telescope astrophotography session log, exposure, gain, frames

**Spec:**
```
Type:       Mobile application (astrophotography log)
Data model: Target(id, name, type)
            Session(id, target_id -> Target, date, camera, telescope, filter, exposure_s, gain, frames, seeing, notes)
Features:   - Log sessions per target with capture settings
            - Calculate total integration time per target and filter
            - Record seeing and moon phase
            - Show targets visible tonight
            - Track processing status
Storage:    Local on-device storage
Tech stack: React Native, expo-sqlite
```

---

## Example 406

**Intent:**
polar alignment helper for my star tracker

**Spec:**
```
Type:       Mobile application (polar alignment helper)
Features:   - Show Polaris position on the reticle for the current time and location
            - Calculate the hour angle of Polaris
            - Show a compass and latitude level for rough alignment
            - Use a red night mode
            - Work offline
Tech stack: Kotlin, Jetpack Compose, Android SensorManager
```

---

## Example 407

**Intent:**
bird call quiz to learn songs before spring

**Spec:**
```
Type:       Mobile application (bird song quiz)
Data model: Species(id, name, audio_path, image_path, region)
            Attempt(id, species_id -> Species, correct, answered_at)
Features:   - Play a bird song and offer four species to choose
            - Filter species by region and habitat
            - Show the photo after answering
            - Repeat difficult species more often
            - Track accuracy per species
Storage:    Local on-device storage
Tech stack: Flutter, just_audio, Hive
```

---

## Example 408

**Intent:**
bird ringing data entry for licensed ringers

**Spec:**
```
Type:       Mobile application (bird ringing records)
Data model: Site(id, name, lat, lng)
            Capture(id, site_id -> Site, ring_no, species, age, sex, wing_mm, weight_g, caught_at, is_retrap)
Features:   - Enter captures quickly with species autocomplete
            - Flag retraps from earlier ring numbers
            - Validate measurements against species ranges
            - Track ring stock by size
            - Export in the national scheme's format
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Room, Jetpack Compose
```

---

## Example 409

**Intent:**
app that teaches music theory basics like scales and key signatures with little lessons

**Spec:**
```
Type:       Mobile application (music theory lessons)
Data model: Lesson(id, title, order, content)
            Exercise(id, lesson_id -> Lesson, type, question, answer)
            Progress(lesson_id -> Lesson, score, completed_on)
Features:   - Teach short lessons on notes, scales, intervals and keys
            - Follow each lesson with interactive exercises
            - Play examples with audio
            - Unlock lessons in order
            - Show progress through the course
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, AVFoundation
```

---

## Example 410

**Intent:**
language drill for medical spanish for nurses

**Spec:**
```
Type:       Mobile application (medical Spanish phrases)
Data model: Phrase(id, english, spanish, category, audio_path)
            Review(phrase_id -> Phrase, due_on, ease)
Features:   - Group phrases by situation like triage and pain assessment
            - Play native audio
            - Drill phrases with spaced repetition
            - Practise speaking with speech recognition scoring
            - Work offline at work
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Room, Android SpeechRecognizer
```

---

## Example 411

**Intent:**
sign language for nurses quick phrases to show deaf patients

**Spec:**
```
Type:       Mobile application (patient communication board)
Data model: Phrase(id, text, category, video_path, icon)
Features:   - Show quick phrases with sign language videos
            - Show icons for pain, toilet and water
            - Let the patient point to answers on a pain scale
            - Type and show text in large font
            - Work offline
Storage:    Local on-device storage
Tech stack: React Native, react-native-video
```

---

## Example 412

**Intent:**
braille music? no.. braille label maker app for blind people, scans and speaks my labelled jars using nfc tags

**Spec:**
```
Type:       Mobile application (NFC talking labels)
Data model: Label(id, tag_uid, text, audio_path, created_at)
Features:   - Write a spoken or typed label to an NFC sticker
            - Read a tag and speak its label aloud
            - Record a custom voice message per tag
            - Work fully with TalkBack
            - List all labels
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Android NFC, Android TextToSpeech
```

---

## Example 413

**Intent:**
ar measure for furniture, will this sofa fit in my living room

**Spec:**
```
Type:       Mobile application (AR furniture fit check)
Data model: Item(id, name, width_cm, depth_cm, height_cm)
Features:   - Enter furniture dimensions
            - Place a life-size box in the room with AR
            - Move and rotate the box on the floor
            - Warn when it overlaps detected walls
            - Save items to check again
Storage:    Local on-device storage
Tech stack: Swift, ARKit, RealityKit
```

---

## Example 414

**Intent:**
tiny house build planner with weight distribution on trailer

**Spec:**
```
Type:       Mobile application (tiny house planner)
Data model: Build(id, trailer_length_m, axle_position_m, max_weight_kg)
            Component(id, build_id -> Build, name, weight_kg, position_m)
Features:   - Add components with weight and position
            - Calculate total weight and tongue weight
            - Warn when weight is outside trailer limits
            - Suggest moving heavy items over the axles
            - Track build costs
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 415

**Intent:**
wallpaper rolls calculator

**Spec:**
```
Type:       Mobile application (wallpaper calculator)
Features:   - Enter wall widths and height
            - Enter roll width, length and pattern repeat
            - Calculate drops per roll and rolls needed
            - Account for doors and windows
            - Round up and add a spare roll
Tech stack: Kotlin, Jetpack Compose
```

---

## Example 416

**Intent:**
event countdown widget for our wedding day and honeymoon

**Spec:**
```
Type:       Mobile application (countdown widgets)
Data model: Countdown(id, title, target_at, photo_path, colour)
Features:   - Create countdowns with a photo
            - Show days, hours and minutes left
            - Add home screen widgets
            - Notify at milestones like 100 days
            - Archive past events
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, WidgetKit
```

---

## Example 417

**Intent:**
allowance app that teaches kids investing with fake stocks

**Spec:**
```
Type:       Mobile application (kids investing simulator)
Data model: Child(id, name, cash)
            Holding(id, child_id -> Child, symbol, shares, avg_price)
            Trade(id, child_id -> Child, symbol, shares, price, traded_at)
Features:   - Give children pretend money to invest
            - Fetch real delayed stock prices
            - Buy and sell shares with simple explanations
            - Show portfolio value over time
            - Let parents add bonus cash
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Alpha Vantage API
```

---

## Example 418

**Intent:**
lemonade stand money counter for my kids business

**Spec:**
```
Type:       Mobile application (kids lemonade stand)
Data model: Sale(id, cups, price, sold_at)
            Cost(id, item, amount)
Features:   - Tap to record cup sales
            - Record ingredient costs
            - Calculate profit
            - Show sales by hour
            - Celebrate profit goals
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 419

**Intent:**
breast pump parts sterilising reminder

**Spec:**
```
Type:       Mobile application (pump parts cleaning reminder)
Data model: Part(id, name, replace_every_days, last_replaced_on)
            Cleaning(id, cleaned_at, method)
Features:   - Remind to clean parts after each session
            - Log sterilising with method used
            - Remind replacing valves and membranes
            - Show the last clean time
            - Keep it quick with one-tap logging
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose
```

---

## Example 420

**Intent:**
hiccups and spit up tracker for reflux baby the doctor wants to see

**Spec:**
```
Type:       Mobile application (infant reflux log)
Data model: Episode(id, occurred_at, type, amount, after_feed_minutes, distress)
            Feed(id, started_at, amount_ml)
Features:   - Log spit-ups with size and distress level
            - Link each episode to the previous feed
            - Log feeds and positions
            - Show episodes per day
            - Export a report for the paediatrician
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 421

**Intent:**
baby sleep sounds and cry analyser hungry or tired

**Spec:**
```
Type:       Mobile application (cry classifier)
Data model: CryEvent(id, recorded_at, predicted_reason, confidence, parent_feedback)
Features:   - Record a short cry clip
            - Classify the cry as hungry, tired or discomfort with an on-device model
            - Let parents confirm the real reason
            - Use feedback to personalise predictions
            - Show patterns by time of day
Storage:    Local on-device storage
Tech stack: Swift, Core ML, AVFoundation
```

---

## Example 422

**Intent:**
kid height growth wall like the door frame marks but in an app

**Spec:**
```
Type:       Mobile application (height wall)
Data model: Child(id, name, colour)
            Mark(id, child_id -> Child, height_cm, measured_on, photo_path)
Features:   - Record heights for each child
            - Draw marks on a virtual door frame
            - Show growth between marks
            - Measure with AR as an option
            - Export the wall as an image
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, ARKit
```

---

## Example 423

**Intent:**
pregnancy appointments and questions to ask the doctor

**Spec:**
```
Type:       Mobile application (prenatal appointment notes)
Data model: Appointment(id, scheduled_at, type, clinician, notes)
            Question(id, appointment_id -> Appointment, text, answer)
Features:   - Schedule prenatal appointments with reminders
            - Write questions before each visit
            - Record answers and results like weight and blood pressure
            - Attach scan photos
            - Show a timeline of all visits
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 424

**Intent:**
morning sickness log what helps

**Spec:**
```
Type:       Mobile application (nausea tracker)
Data model: Episode(id, occurred_at, severity, vomited, trigger)
            Remedy(id, name)
            RemedyUse(episode_id -> Episode, remedy_id -> Remedy, helped)
Features:   - Log nausea with severity
            - Tag possible triggers like smells
            - Record remedies tried and if they helped
            - Show worst times of day
            - Show which remedies work best
Storage:    Local on-device storage
Tech stack: Kotlin, Room
```

---

## Example 425

**Intent:**
food cravings in pregnancy funny log to share

**Spec:**
```
Type:       Mobile application (pregnancy cravings journal)
Data model: Craving(id, food, week, logged_at, photo_path, note)
Features:   - Log cravings with the pregnancy week
            - Add photos
            - Show a timeline by trimester
            - Create a shareable cravings card
            - Count the most common cravings
Storage:    Local on-device storage
Tech stack: Flutter, Hive, screenshot
```

---

## Example 426

**Intent:**
elderly check in by phone call robot every evening

**Spec:**
```
Type:       Mobile application with backend (automated wellness call)
Auth:       Family member login with email
Data model: Senior(id, name, phone, call_time)
            Call(id, senior_id -> Senior, placed_at, answered, response)
            FamilyMember(id, senior_id -> Senior, phone)
Features:   - Place an automated phone call at a set time
            - Ask the senior to press 1 if fine or 2 for help
            - Alert family when the senior presses 2 or misses the call
            - Retry missed calls once
            - Show call history in the app
API:        REST
            PUT  /seniors/{id}/schedule
            GET  /seniors/{id}/calls
            POST /webhooks/twilio
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Twilio Voice
```

---

## Example 427

**Intent:**
old people exercise videos chair based, large text

**Spec:**
```
Type:       Mobile application (chair exercise programme)
Data model: Video(id, title, level, duration_min, file_path)
            Session(id, video_id -> Video, done_on)
Features:   - Offer short chair exercise videos by level
            - Use large buttons and text
            - Download videos for offline playback
            - Track sessions per week
            - Remind at a chosen time
Storage:    Local on-device storage
Tech stack: Kotlin, ExoPlayer, Jetpack Compose
```

---

## Example 428

**Intent:**
blood thinner inr log warfarin dose

**Spec:**
```
Type:       Mobile application (INR and warfarin log)
Data model: InrTest(id, tested_on, inr, target_low, target_high)
            Dose(id, date, mg, taken)
Features:   - Log INR results with the target range
            - Record daily warfarin doses
            - Show INR over time with the target band
            - Remind daily dose and next test date
            - Flag foods high in vitamin K
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Swift Charts
```

---

## Example 429

**Intent:**
hayfever? no — food allergy reaction diary for my son with photos of hives

**Spec:**
```
Type:       Mobile application (allergic reaction diary)
Data model: Reaction(id, occurred_at, suspected_food, symptoms, severity, treatment, photo_path)
Features:   - Log reactions with symptoms and severity
            - Record suspected foods and treatment like antihistamine
            - Attach photos of hives
            - Show reactions over time
            - Export for the allergist
Storage:    Local on-device storage
Tech stack: Kotlin, Room, CameraX
```

---

## Example 430

**Intent:**
restaurant allergen checker for staff, menu items and which of 14 allergens they have

**Spec:**
```
Type:       Mobile application with backend (restaurant allergen matrix)
Auth:       Staff PIN login per restaurant
Data model: Restaurant(id, name)
            Dish(id, restaurant_id -> Restaurant, name, allergens, may_contain)
            Ingredient(id, name, allergens)
Features:   - Build dishes from ingredients with allergen flags
            - Calculate dish allergens automatically
            - Let staff filter dishes safe for a guest's allergies
            - Show a printable allergen matrix
            - Sync menu changes to all devices
API:        REST
            GET  /restaurants/{id}/dishes
            POST /dishes
            GET  /dishes/safe?exclude=
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework, PostgreSQL
```

---

## Example 431

**Intent:**
oil change reminder app for my 3 cars, just km based

**Spec:**
```
Type:       Mobile application (oil change reminder)
Data model: Car(id, name, interval_km, last_change_km, current_km)
Features:   - Enter the odometer reading when filling up
            - Show km remaining until the next oil change
            - Remind when under 500 km remain
            - Log oil changes
            - Support several cars
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 432

**Intent:**
truck driver logbook hours of service

**Spec:**
```
Type:       Mobile application (driver hours log)
Data model: Driver(id, name, licence)
            DutyStatus(id, driver_id -> Driver, status, started_at, lat, lng)
Features:   - Switch between driving, on duty, off duty and sleeper
            - Calculate remaining driving and on-duty hours
            - Warn before hitting limits
            - Draw a daily log graph
            - Export daily logs as PDF
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Room, Jetpack Compose
```

---

## Example 433

**Intent:**
our community garden needs a watering rota, whos turn and did they do it

**Spec:**
```
Type:       Mobile application with backend (community garden rota)
Auth:       Email login for members
Data model: Garden(id, name)
            Member(id, garden_id -> Garden, name)
            Shift(id, garden_id -> Garden, date, member_id -> Member, done)
Features:   - Show the watering rota on a calendar
            - Let members sign up for days
            - Remind the member the morning of their shift
            - Mark the shift as done
            - Show uncovered days
API:        REST
            GET  /gardens/{id}/shifts
            PATCH /shifts/{id}
Storage:    Firebase Firestore
Tech stack: React Native, Firebase
```

---

## Example 434

**Intent:**
apartment building package room log for our concierge

**Spec:**
```
Type:       Mobile application with backend (parcel log)
Auth:       Concierge login
Data model: Resident(id, name, unit, phone)
            Parcel(id, resident_id -> Resident, carrier, received_at, shelf, picked_up_at, signature_path)
Features:   - Scan the parcel label to match the resident
            - Notify residents by SMS
            - Record the shelf location
            - Capture a signature on pickup
            - Show uncollected parcels older than a week
API:        REST
            POST /parcels
            PATCH /parcels/{id}/pickup
            GET  /parcels?status=waiting
Storage:    PostgreSQL
Tech stack: Kotlin, ML Kit, Spring Boot, Twilio
```

---

## Example 435

**Intent:**
Bonjour, je veux une app pour noter mes randonnées à cheval? non à vélo… OK in english: cycling touring daily log with camping spots

**Spec:**
```
Type:       Mobile application (bike touring journal)
Data model: Tour(id, name, started_on)
            Day(id, tour_id -> Tour, date, distance_km, ascent_m, notes)
            Camp(id, day_id -> Day, name, lat, lng, type, cost, rating)
Features:   - Record daily distance and climbing
            - Log camping spots with cost and rating
            - Show the whole tour on a map
            - Add photos to each day
            - Export the tour as GPX and PDF diary
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Room, MapLibre
```

---

## Example 436

**Intent:**
i'm a vet tech? no... i'm a farrier, need app for horses shoeing schedule and clients

**Spec:**
```
Type:       Mobile application (farrier client schedule)
Data model: Client(id, name, address, phone)
            Horse(id, client_id -> Client, name, shoe_type, interval_weeks, last_shod_on, notes)
Features:   - Track horses per client with shoeing interval
            - Show horses due this week
            - Plan the day's route
            - Log work done and price
            - Text clients appointment reminders
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, url_launcher
```

---

## Example 437

**Intent:**
knife sharpening angle guide using the phone tilt

**Spec:**
```
Type:       Mobile application (sharpening angle guide)
Features:   - Show the blade angle using the phone gyroscope
            - Set a target angle like 15 or 20 degrees
            - Beep when the angle drifts
            - Calibrate on the stone
            - Show a large readable display
Tech stack: Swift, CoreMotion, SwiftUI
```

---

## Example 438

**Intent:**
chess opening trainer offline

**Spec:**
```
Type:       Mobile application (chess opening trainer)
Data model: Opening(id, name, eco, moves_pgn)
            Drill(id, opening_id -> Opening, correct, wrong, due_on)
Features:   - Load an opening repertoire from PGN
            - Drill moves on an interactive board
            - Repeat lines with mistakes using spaced repetition
            - Show the opening name as moves are played
            - Work offline
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, chesslib, Jetpack Compose
```

---

## Example 439

**Intent:**
score keeper for card games like rummy with many rounds

**Spec:**
```
Type:       Mobile application (card game scorekeeper)
Data model: Game(id, name, target_score, started_at)
            Player(id, game_id -> Game, name)
            RoundScore(id, player_id -> Player, round, points)
Features:   - Add players and a target score
            - Enter points per round
            - Show running totals and the leader
            - Announce the winner at the target
            - Keep a history of games
Storage:    Local on-device storage
Tech stack: React Native, AsyncStorage
```

---

## Example 440

**Intent:**
table tennis scoreboard on a tablet with voice

**Spec:**
```
Type:       Mobile application (table tennis scoreboard)
Data model: Match(id, player_a, player_b, best_of, started_at)
            Game(id, match_id -> Match, score_a, score_b)
Features:   - Show large scores for both players
            - Track serve changes every two points
            - Handle deuce at 10-10
            - Announce scores with voice
            - Tap with a Bluetooth clicker
Storage:    Local on-device storage
Tech stack: Flutter, flutter_tts
```

---

## Example 441

**Intent:**
pickleball tournament round robin generator for our club

**Spec:**
```
Type:       Mobile application (round robin scheduler)
Data model: Event(id, name, courts)
            Player(id, event_id -> Event, name)
            Match(id, event_id -> Event, round, court, team_a, team_b, score_a, score_b)
Features:   - Generate rotating doubles partners
            - Assign matches to courts by round
            - Enter scores
            - Rank players by wins and point difference
            - Show the schedule on a big screen
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 442

**Intent:**
running club? no, swimming lap counter that you tap at the end of the pool

**Spec:**
```
Type:       Mobile application (lap counter)
Data model: Session(id, pool_length_m, laps, started_at, ended_at)
Features:   - Count laps with a large tap anywhere on the screen
            - Calculate distance from pool length
            - Show the last lap time
            - Work with a waterproof pouch
            - Save sessions
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose
```

---

## Example 443

**Intent:**
hey, quick one — offline dictionary for welsh english

**Spec:**
```
Type:       Mobile application (bilingual dictionary)
Data model: Entry(id, headword, language, part_of_speech, translations, mutations)
            Bookmark(entry_id -> Entry)
Features:   - Search Welsh and English headwords
            - Find words entered in mutated forms
            - Show pronunciation audio
            - Bookmark words
            - Work offline
Storage:    Local on-device database (SQLite, bundled)
Tech stack: Flutter, sqflite
```

---

## Example 444

**Intent:**
kanji stroke order practice with handwriting recognition

**Spec:**
```
Type:       Mobile application (kanji writing practice)
Data model: Kanji(id, character, meanings, readings, jlpt_level, strokes_svg)
            Review(kanji_id -> Kanji, due_on, ease)
Features:   - Animate stroke order
            - Recognise handwritten kanji drawn by the user
            - Check stroke count and order
            - Organise by JLPT level
            - Review with spaced repetition
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, ML Kit Digital Ink Recognition, Room
```

---

## Example 445

**Intent:**
listening ear game for my choir to practise harmony parts

**Spec:**
```
Type:       Mobile application (choir part practice)
Data model: Song(id, title)
            Part(id, song_id -> Song, voice, audio_path)
Features:   - Play songs with separate soprano, alto, tenor and bass tracks
            - Boost the user's own part and lower others
            - Mute the user's part to sing along
            - Loop sections
            - Change tempo
Storage:    Local on-device storage
Tech stack: Swift, AVAudioEngine, SwiftUI
```

---

## Example 446

**Intent:**
dj bpm counter tap

**Spec:**
```
Type:       Mobile application (BPM tapper)
Features:   - Calculate BPM from taps
            - Detect BPM from the microphone
            - Show half and double tempo
            - Reset after a pause
            - Keep a list of measured tracks
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, TarsosDSP
```

---

## Example 447

**Intent:**
accessible calculator with voice, for blind users

**Spec:**
```
Type:       Mobile application (talking calculator)
Data model: History(id, expression, result, at)
Features:   - Speak each key and result
            - Use large high-contrast keys
            - Support swipe gestures for operations
            - Read back the history
            - Work with TalkBack and VoiceOver
Storage:    Local on-device storage
Tech stack: React Native, expo-speech
```

---

## Example 448

**Intent:**
money identifier for blind people, camera says the banknote value

**Spec:**
```
Type:       Mobile application (banknote identifier)
Features:   - Recognise banknotes from the camera with an on-device model
            - Speak the value aloud
            - Vibrate a pattern per denomination
            - Support several currencies
            - Work offline
Tech stack: Kotlin, TensorFlow Lite, CameraX, Android TextToSpeech
```

---

## Example 449

**Intent:**
tip and tax calculator for us shopping when you visit, prices don't include tax

**Spec:**
```
Type:       Mobile application (US sales tax calculator)
Data model: State(code, name, base_rate)
Features:   - Detect the state from location
            - Add sales tax to shelf prices
            - Add common tip percentages for services
            - Convert the total to the home currency
            - Work offline with bundled rates
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, CoreLocation
```

---

## Example 450

**Intent:**
cooking temperature guide for meats

**Spec:**
```
Type:       Mobile application (meat temperature guide)
Data model: Meat(id, name, doneness, temp_c, rest_minutes)
Features:   - Show safe internal temperatures by meat and doneness
            - Switch Celsius and Fahrenheit
            - Show resting times
            - Run a cooking timer
            - Work offline
Tech stack: Flutter
```

---

## Example 451

**Intent:**
recipe scaling plus converting to metric from american recipes

**Spec:**
```
Type:       Mobile application (recipe converter)
Data model: Recipe(id, title, source_url, servings, ingredients)
Features:   - Paste a recipe or import from a URL
            - Convert cups and ounces to grams and ml by ingredient
            - Convert Fahrenheit to Celsius
            - Scale servings
            - Save converted recipes
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jsoup, Room
```

---

## Example 452

**Intent:**
meal prep containers portion calculator for macros

**Spec:**
```
Type:       Mobile application (portion splitter)
Data model: Batch(id, recipe, total_weight_g, calories, protein_g, carbs_g, fat_g, containers)
Features:   - Enter a cooked batch's total weight and nutrition
            - Split into a number of containers
            - Calculate grams per container for a calorie target
            - Show macros per container
            - Save batches
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI
```

---

## Example 453

**Intent:**
bulk cooking freezer meal labels with date and reheating instructions

**Spec:**
```
Type:       Mobile application (freezer meal labeller)
Data model: Meal(id, name, cooked_on, portions, reheat_instructions, use_by)
Features:   - Create meals with cook date and portions
            - Print labels on a Bluetooth label printer
            - Calculate the use-by date
            - Track portions left
            - Remind before meals expire
Storage:    Local on-device storage
Tech stack: Flutter, Hive, Bluetooth printing plugin
```

---

## Example 454

**Intent:**
home inventory for renters insurance — please make it in flutter and backup to dropbox

**Spec:**
```
Type:       Mobile application (renters inventory)
Auth:       Dropbox OAuth for backup
Data model: Item(id, name, room, value, purchased_on, photo_path, receipt_path)
Features:   - Add items with photos and receipts
            - Total value per room
            - Export a claim-ready PDF
            - Back up to Dropbox
            - Restore on a new device
Storage:    Local SQLite database, Dropbox backup
Tech stack: Flutter, sqflite, Dropbox API
```

---

## Example 455

**Intent:**
library book due dates for my whole family cards

**Spec:**
```
Type:       Mobile application (library loans tracker)
Data model: Member(id, name, card_no)
            Loan(id, member_id -> Member, title, isbn, due_on, returned)
Features:   - Scan ISBNs to add borrowed books
            - Track due dates per family member
            - Remind three days before due
            - Show everything due this week
            - Mark returned
Storage:    Local on-device storage
Tech stack: Kotlin, ML Kit Barcode Scanning, Room
```

---

## Example 456

**Intent:**
wedding rsvp app guests reply by scanning qr on the invitation

**Spec:**
```
Type:       Mobile application with backend (QR RSVP)
Auth:       Couple login with email; guests use a unique code
Data model: Wedding(id)
            Invitation(id, wedding_id -> Wedding, code, household, max_guests)
            Response(id, invitation_id -> Invitation, attending_count, meals, song_request)
Features:   - Generate a unique QR code per invitation
            - Let guests reply by scanning without an account
            - Collect meal choices and song requests
            - Show live RSVP totals to the couple
            - Export the final list
API:        REST
            GET  /invitations/{code}
            POST /invitations/{code}/response
            GET  /weddings/{id}/summary
Storage:    PostgreSQL
Tech stack: React Native, NestJS, PostgreSQL
```

---

## Example 457

**Intent:**
honeymoon fund? no, wedding dress shopping notes, which shop which dress price and photos

**Spec:**
```
Type:       Mobile application (dress shopping notes)
Data model: Shop(id, name, address)
            Dress(id, shop_id -> Shop, designer, style_name, price, rating, photo_path, notes)
Features:   - Save dresses tried with photos
            - Note shop, designer and price
            - Rate each dress
            - Compare favourites side by side
            - Share a shortlist with family
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 458

**Intent:**
allowance app with chores that repeat weekly, two kids, in react native with firebase so both parents see

**Spec:**
```
Type:       Mobile application with backend (shared chores and allowance)
Auth:       Firebase Auth for parents
Data model: Family(id)
            Child(id, family_id -> Family, name, balance)
            Chore(id, family_id -> Family, name, value, weekdays, child_id -> Child)
            Completion(id, chore_id -> Chore, date, approved_by)
Features:   - Set repeating chores per child
            - Let either parent approve completions
            - Update balances in real time on both phones
            - Pay out allowance and reset weekly
            - Show a weekly chore summary
Storage:    Firebase Firestore
Tech stack: React Native, Firebase Auth, Firestore
```

---

## Example 459

**Intent:**
kids pocket money abroad? no.. teen debit card spending log, she types what she spent

**Spec:**
```
Type:       Mobile application (teen spending diary)
Data model: Spend(id, amount, category, note, spent_at)
            Budget(category, monthly_limit)
Features:   - Log purchases quickly with categories
            - Set monthly limits per category
            - Show money left this month
            - Show a pie chart of spending
            - Encourage saving with a goal bar
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, Vico
```

---

## Example 460

**Intent:**
plants? no. aquarium? no. ant colony keeping log lol, my ants

**Spec:**
```
Type:       Mobile application (ant colony journal)
Data model: Colony(id, species, queen_found_on, formicarium)
            Census(id, colony_id -> Colony, counted_on, workers, brood)
            Feeding(id, colony_id -> Colony, fed_on, food)
Features:   - Track colonies by species
            - Log worker counts and brood
            - Record feedings
            - Remind hydration of the nest
            - Show colony growth chart
Storage:    Local on-device storage
Tech stack: Flutter, Hive, fl_chart
```

---

## Example 461

**Intent:**
grocery receipt price tracker to see inflation on the things i buy

**Spec:**
```
Type:       Mobile application (personal price tracker)
Data model: Product(id, name, unit)
            PricePoint(id, product_id -> Product, store, price, bought_on)
Features:   - Scan receipts and extract product lines
            - Match lines to tracked products
            - Chart price changes per product
            - Compare stores
            - Show personal inflation rate
Storage:    Local on-device database (SQLite)
Tech stack: Swift, Vision, SwiftData, Swift Charts
```

---

## Example 462

**Intent:**
bassinet rocking motion and baby sleep diary for my smart crib

**Spec:**
```
Type:       Mobile application (smart bassinet companion)
Data model: Bassinet(id, device_id, name)
            SleepEvent(id, bassinet_id -> Bassinet, started_at, ended_at, wake_count, motion_level)
Features:   - Connect to the bassinet over Bluetooth LE
            - Start and stop rocking at chosen speeds
            - Log sleep sessions automatically from bassinet sensors
            - Show nightly wake-ups
            - Adjust the sound and motion schedule
Storage:    Local on-device database (SQLite)
Tech stack: Swift, CoreBluetooth, SwiftUI
```

---

## Example 463

**Intent:**
family recipe book app where my aunts add recipes too

**Spec:**
```
Type:       Mobile application with backend (shared family cookbook)
Auth:       Email login, family cookbook joined by invite
Data model: Cookbook(id, name)
            Member(id, cookbook_id -> Cookbook, name)
            Recipe(id, cookbook_id -> Cookbook, author_id -> Member, title, ingredients, steps, photo_path, story)
Features:   - Let family members add recipes with photos and stories
            - Comment on and rate recipes
            - Scale recipes by servings
            - Search by ingredient
            - Print a family cookbook PDF
API:        REST
            GET  /cookbooks/{id}/recipes
            POST /recipes
            POST /recipes/{id}/comments
Storage:    Supabase (PostgreSQL), Supabase Storage
Tech stack: Flutter, Supabase
```

---

## Example 464

**Intent:**
fishing knots guide with animations offline

**Spec:**
```
Type:       Mobile application (fishing knots guide)
Data model: Knot(id, name, use, strength_percent, steps_animation)
            Favourite(knot_id -> Knot)
Features:   - Show knots with step-by-step animations
            - Filter knots by use like line-to-hook
            - Show breaking strength ratings
            - Save favourites
            - Work offline
Storage:    Local on-device storage
Tech stack: Kotlin, Lottie, Jetpack Compose
```

---

## Example 465

**Intent:**
snorkel spot finder with water visibility reports from friends

**Spec:**
```
Type:       Mobile application with backend (snorkel conditions sharing)
Auth:       Email login
Data model: Spot(id, name, lat, lng)
            Report(id, spot_id -> Spot, user_id, visibility_m, water_temp_c, current, reported_at, photo_path)
Features:   - Show snorkel spots on a map
            - Let friends post visibility and current reports
            - Show the latest conditions per spot
            - Show swell and wind forecast
            - Follow spots for alerts on good days
API:        REST
            GET  /spots
            POST /spots/{id}/reports
            GET  /spots/{id}/reports
Storage:    PostgreSQL
Tech stack: React Native, FastAPI, Open-Meteo Marine API
```

---

## Example 466

**Intent:**
lunar gardening? no, star chart for kids with constellation stories

**Spec:**
```
Type:       Mobile application (kids constellation guide)
Data model: Constellation(id, name, stars_json, story, audio_path)
            Found(constellation_id -> Constellation, found_on)
Features:   - Show the sky in the direction the phone points
            - Draw constellation lines and pictures
            - Narrate the myth behind each constellation
            - Let kids collect constellations they found
            - Use a red screen at night
Storage:    Local on-device storage
Tech stack: Swift, CoreMotion, SceneKit, AVFoundation
```

---

## Example 467

**Intent:**
emergency room wait diary for chronically ill, record visits and what they did

**Spec:**
```
Type:       Mobile application (hospital visit log)
Data model: Visit(id, hospital, arrived_at, left_at, reason, tests, diagnosis, discharge_notes)
            Document(id, visit_id -> Visit, photo_path)
Features:   - Log hospital and urgent care visits
            - Record tests, treatments and diagnosis
            - Photograph discharge papers
            - Show visit history for new doctors
            - Export a summary PDF
Storage:    Local on-device database (encrypted SQLite)
Tech stack: Kotlin, Room, SQLCipher
```

---

## Example 468

**Intent:**
headache? no I have vertigo, log dizzy spells and what I was doing

**Spec:**
```
Type:       Mobile application (vertigo diary)
Data model: Spell(id, started_at, duration_min, severity, type, position_change, nausea, activity)
Features:   - Log dizzy spells with duration and severity
            - Record what triggered it like turning in bed
            - Note nausea and hearing changes
            - Show spells per week
            - Guide Epley manoeuvre steps with timers
Storage:    Local on-device storage
Tech stack: Flutter, Hive
```

---

## Example 469

**Intent:**
piano tuning? no. drum tuning app that tells the pitch of each lug

**Spec:**
```
Type:       Mobile application (drum tuner)
Data model: Drum(id, name, size_in, target_hz)
            LugReading(id, drum_id -> Drum, lug, hz, read_at)
Features:   - Detect the pitch of a tap near each lug
            - Show which lugs are higher or lower than the target
            - Save target pitches per drum
            - Show the overall fundamental
            - Guide lug tuning in a star pattern
Storage:    Local on-device storage
Tech stack: Kotlin, TarsosDSP, Jetpack Compose
```

---

## Example 470

**Intent:**
practice log for my violin students with recordings they send me

**Spec:**
```
Type:       Mobile application with backend (student recording feedback)
Auth:       Teacher and student accounts with email
Data model: Teacher(id, name)
            Student(id, teacher_id -> Teacher, name)
            Submission(id, student_id -> Student, piece, audio_key, submitted_at)
            Feedback(id, submission_id -> Submission, text, timestamp_s)
Features:   - Let students record and submit practice clips
            - Let the teacher leave timestamped comments
            - Notify students of new feedback
            - Show each student's submission history
            - Track practice streaks
API:        REST
            POST /submissions
            GET  /teachers/{id}/submissions
            POST /submissions/{id}/feedback
Storage:    PostgreSQL, S3 for audio
Tech stack: Flutter, Laravel, MySQL, AWS S3
```

---

## Example 471

**Intent:**
vocabulary for my nursing exams? no, latin plant names quiz for horticulture students

**Spec:**
```
Type:       Mobile application (botanical Latin quiz)
Data model: Plant(id, latin_name, common_name, family, image_path)
            Review(plant_id -> Plant, due_on, ease)
Features:   - Show plant photos and ask for the Latin name
            - Accept typed answers with spelling tolerance
            - Explain the meaning of Latin epithets
            - Group plants by course list
            - Review with spaced repetition
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 472

**Intent:**
road sign quiz for my driving theory test in germany

**Spec:**
```
Type:       Mobile application (road sign quiz)
Data model: Sign(id, image_path, meaning, category)
            Attempt(id, sign_id -> Sign, correct, answered_at)
Features:   - Show road signs and multiple choice meanings
            - Group signs by warning, priority and prohibition
            - Repeat signs answered wrong
            - Run timed mock tests
            - Show readiness per category
Storage:    Local on-device storage
Tech stack: Kotlin, Room, Jetpack Compose
```

---

## Example 473

**Intent:**
unit converter for nurses, mg to ml, drip rates

**Spec:**
```
Type:       Mobile application (medication dosage calculator)
Features:   - Calculate volume to give from dose and concentration
            - Calculate IV drip rates in drops per minute and ml per hour
            - Calculate weight-based doses
            - Show the formula used for checking
            - Warn on unusually high results
Tech stack: Swift, SwiftUI
```

---

## Example 474

**Intent:**
baking pan size converter, recipe for round 9 inch but i have square 8

**Spec:**
```
Type:       Mobile application (pan size converter)
Features:   - Choose original and new pan shapes and sizes
            - Calculate the area ratio
            - Scale ingredient amounts accordingly
            - Suggest baking time adjustments
            - Support round, square, rectangular and loaf pans
Tech stack: Flutter
```

---

## Example 475

**Intent:**
wedding speech joke? no — wedding day emergency kit checklist for bridesmaids

**Spec:**
```
Type:       Mobile application (wedding day kit checklist)
Data model: KitItem(id, name, category, packed, assigned_to)
Features:   - Start with a full emergency kit list
            - Assign items to bridesmaids
            - Tick items as packed
            - Add custom items
            - Share the list as text
Storage:    Local on-device storage
Tech stack: React Native, AsyncStorage
```

---

## Example 476

**Intent:**
moving abroad checklist with visas, shipping, pets docs, closing bank accounts, by country

**Spec:**
```
Type:       Mobile application (international relocation planner)
Data model: Move(id, from_country, to_country, move_date)
            Task(id, move_id -> Move, title, category, due_on, done, document_path)
Features:   - Generate tasks from templates for origin and destination countries
            - Schedule tasks counting back from the move date
            - Attach documents to tasks
            - Track shipping quotes
            - Remind of upcoming deadlines
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Room, Jetpack Compose
```

---

## Example 477

**Intent:**
kids chores but its a game, they level up a character when they finish chores

**Spec:**
```
Type:       Mobile game (chore adventure)
Data model: Hero(id, child_name, level, xp, gold, outfit)
            Quest(id, title, xp_reward, gold_reward, repeat)
            QuestDone(id, quest_id -> Quest, hero_id -> Hero, done_on, approved)
Features:   - Turn chores into quests with XP and gold
            - Level up a customisable hero
            - Spend gold on outfits and pets in the game
            - Let parents approve completed quests
            - Show a weekly quest board
Storage:    Local on-device storage
Tech stack: Flutter, Flame, Hive
```

---

## Example 478

**Intent:**
hike leave no trace? I want offline trail notes for my local park volunteer patrol, report fallen trees

**Spec:**
```
Type:       Mobile application with backend (trail issue reporting)
Auth:       Volunteer login
Data model: Trail(id, name, geometry)
            Issue(id, trail_id -> Trail, type, lat, lng, photo_path, reported_at, status)
Features:   - Show trails on an offline map
            - Report issues like fallen trees and erosion with GPS and photo
            - Queue reports offline
            - Let rangers mark issues fixed
            - Show open issues per trail
API:        REST
            GET  /trails
            POST /issues
            PATCH /issues/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, MapLibre, Express, PostGIS
```

---

## Example 479

**Intent:**
bird photography? no, insect id app for my kids bug hunts

**Spec:**
```
Type:       Mobile application (kids bug hunt)
Data model: Species(id, name, group, fun_fact, image)
            Find(id, species_id -> Species, found_at, photo_path)
Features:   - Identify insects from a photo with an on-device model
            - Show a fun fact for each find
            - Build a collection book of found bugs
            - Award badges for groups found
            - Keep photos only on the device
Storage:    Local on-device storage
Tech stack: Swift, Core ML, SwiftUI
```

---

## Example 480

**Intent:**
meteor? no. sundial app lol, show where the shadow should be

**Spec:**
```
Type:       Mobile application (sundial helper)
Features:   - Calculate the sun's azimuth and altitude for the location
            - Show the shadow direction on a compass
            - Convert sundial time to clock time with the equation of time
            - Help align a garden sundial
            - Show sunrise and sunset
Tech stack: Kotlin, Android SensorManager, Jetpack Compose
```

---

## Example 481

**Intent:**
cleaning schedule for my house, room by room, daily weekly monthly

**Spec:**
```
Type:       Mobile application (home cleaning schedule)
Data model: Room(id, name)
            CleaningTask(id, room_id -> Room, name, frequency_days, last_done_on, minutes)
Features:   - Set tasks per room with frequency
            - Show today's tasks by priority
            - Mark tasks done
            - Fit tasks into a chosen time budget
            - Show a cleanliness score per room
Storage:    Local on-device storage
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 482

**Intent:**
braille? no, large print bingo caller app for my nursing home games

**Spec:**
```
Type:       Mobile application (bingo caller)
Data model: Game(id, started_at, called_numbers)
Features:   - Draw random numbers 1-75 or 1-90
            - Show the number in very large print
            - Announce numbers with voice and calls
            - Show a board of called numbers
            - Check a winning card
Storage:    Local on-device storage
Tech stack: Flutter, flutter_tts
```

---

## Example 483

**Intent:**
neighbour lending library for things like ladders tents, small app for our street

**Spec:**
```
Type:       Mobile application with backend (street lending library)
Auth:       Email login, street group by invite
Data model: Group(id, name)
            Member(id, group_id -> Group, name, address)
            Thing(id, owner_id -> Member, name, photo_path, available)
            Borrow(id, thing_id -> Thing, borrower_id -> Member, from_date, to_date, status)
Features:   - List items members are happy to lend
            - Request to borrow for dates
            - Let owners approve requests
            - Remind borrowers to return
            - Show what is available now
API:        REST
            GET  /groups/{id}/things
            POST /borrows
            PATCH /borrows/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 484

**Intent:**
track my kid's sports kit, which bag has shin pads, swimming stuff

**Spec:**
```
Type:       Mobile application (kids activity bag checklist)
Data model: Activity(id, name, weekday, child_name)
            KitItem(id, activity_id -> Activity, name)
Features:   - Set weekly activities per child
            - List the kit for each activity
            - Show tomorrow's bag checklist each evening
            - Tick items as packed
            - Notify the night before
Storage:    Local on-device storage
Tech stack: Kotlin, Jetpack Compose, WorkManager
```

---

## Example 485

**Intent:**
piano practice game where you play real notes to make a character jump

**Spec:**
```
Type:       Mobile game (pitch-controlled platformer)
Data model: Level(id, number, note_sequence)
            Score(level_id -> Level, stars, best_time_s)
Features:   - Listen to notes played on a real instrument
            - Make the character jump to platforms matching each note
            - Increase speed and range in later levels
            - Award stars for accuracy
            - Let users choose instrument range
Storage:    Local on-device storage
Tech stack: Unity, C#, microphone pitch detection
```

---

