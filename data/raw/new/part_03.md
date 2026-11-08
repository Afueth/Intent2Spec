## Example 1

**Intent:**
pill reminder for my mum

**Spec:**
```
Type:       Mobile application
Data model: Medication(id, name, dose, form)
            Schedule(id, medication_id -> Medication, time_of_day, days_of_week)
            DoseLog(id, schedule_id -> Schedule, taken_at, status)
Features:   - Add medications with dose and form (tablet, drops, injection)
            - Schedule reminders for set times and weekdays
            - Send a local notification at each dose time
            - Mark a dose as taken, skipped or snoozed
            - Show a weekly adherence summary
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_local_notifications, sqflite
```

---

## Example 2

**Intent:**
I keep forgetting to water my houseplants and some of them need it more often than others. Can you make an app for that?

**Spec:**
```
Type:       Mobile application
Data model: Plant(id, name, species, photo_path, room, water_every_days)
            WateringEvent(id, plant_id -> Plant, watered_at, note)
Features:   - Add plants with a photo, room and watering interval
            - Calculate the next watering date for each plant
            - Send a morning notification listing plants due today
            - Log a watering with one tap
            - Show plants sorted by how overdue they are
Storage:    Local on-device database (SQLite)
Tech stack: React Native, Expo Notifications, expo-sqlite
```

---

## Example 3

**Intent:**
sleep diary app, iphone only, swiftui

**Spec:**
```
Type:       Mobile application
Data model: SleepEntry(id, bed_time, wake_time, sleep_quality, awakenings, note)
            Factor(id, name)
            EntryFactor(entry_id -> SleepEntry, factor_id -> Factor)
Features:   - Log bedtime, wake time and a 1-5 quality rating each morning
            - Tag nights with factors like caffeine, alcohol or late screen time
            - Calculate sleep duration and weekly average
            - Chart sleep duration and quality over 30 days
            - Compare average quality on nights with and without each factor
Storage:    SwiftData (on-device)
Tech stack: Swift, SwiftUI, SwiftData, Swift Charts
```

---

## Example 4

**Intent:**
i want to track my running. distance, time, pace, and see the route on a map after

**Spec:**
```
Type:       Mobile application
Data model: Run(id, started_at, duration_s, distance_m, avg_pace_s_per_km, calories)
            RoutePoint(id, run_id -> Run, lat, lng, altitude, recorded_at)
Features:   - Record a run using GPS in the background
            - Show live distance, time and current pace while running
            - Draw the finished route on a map
            - Split the run into per-kilometre pace splits
            - List past runs with weekly distance totals
Storage:    Room (SQLite) on-device
Tech stack: Kotlin, Jetpack Compose, Fused Location Provider, Room, Google Maps SDK
```

---

## Example 5

**Intent:**
budget app where i put in my salary and then every expense and it tells me how much i can still spend this month

**Spec:**
```
Type:       Mobile application
Data model: Income(id, amount, received_on, source)
            Category(id, name, monthly_limit)
            Expense(id, amount, category_id -> Category, spent_on, note)
Features:   - Enter monthly income and recurring bills
            - Add expenses with amount, category and date
            - Show remaining money for the month after bills and expenses
            - Show remaining budget per category
            - Warn when a category goes over its limit
Storage:    Hive (local key-value database)
Tech stack: Flutter, Hive, fl_chart
```

---

## Example 6

**Intent:**
flashcards for learning japanese kanji

**Spec:**
```
Type:       Mobile application
Data model: Deck(id, name)
            Card(id, deck_id -> Deck, kanji, readings, meaning, example)
            Review(id, card_id -> Card, reviewed_at, grade, interval_days, ease_factor, due_on)
Features:   - Create decks and cards with kanji, readings and meaning
            - Schedule reviews with the SM-2 spaced repetition algorithm
            - Show today's due cards and grade each answer
            - Draw kanji with a finger on a practice canvas
            - Show daily review streak and cards learned
Storage:    WatermelonDB (SQLite) on-device
Tech stack: React Native, react-native-skia (drawing canvas), WatermelonDB
```

---

## Example 7

**Intent:**
Hello, I am travelling to Italy next month with my wife and I want app for make list of things to pack, and check them when I put in luggage. Thank you.

**Spec:**
```
Type:       Mobile application
Data model: Trip(id, name, destination, start_date, end_date)
            Bag(id, trip_id -> Trip, name, owner)
            PackingItem(id, bag_id -> Bag, name, quantity, is_packed)
Features:   - Create a trip with dates and destination
            - Add bags per person and items to each bag
            - Check off items as they are packed
            - Copy a packing list from an earlier trip
            - Show how many items are still unpacked per bag
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift (SQLite)
```

---

## Example 8

**Intent:**
dog walk tracker

**Spec:**
```
Type:       Mobile application
Data model: Dog(id, name, breed, photo_path)
            Walk(id, dog_id -> Dog, started_at, duration_min, distance_m, pee, poo)
Features:   - Start and stop a walk with a timer and GPS distance
            - Record pee and poo stops during a walk
            - Show daily walk time per dog against a goal
            - List walk history in a calendar view
Storage:    Core Data (on-device)
Tech stack: Swift, SwiftUI, Core Location, Core Data
```

---

## Example 9

**Intent:**
I'm trying to cut down on sugar and I want something simple where I log what I eat and it adds up grams of sugar for the day, nothing fancy, no account.

**Spec:**
```
Type:       Mobile application
Data model: Food(id, name, sugar_g_per_100g, is_custom)
            Entry(id, food_id -> Food, grams, eaten_at, meal)
Features:   - Search a bundled food list for sugar content
            - Add custom foods with sugar per 100 g
            - Log a portion in grams to a meal
            - Show total sugar today against a daily limit
            - Show a 7-day sugar trend chart
Storage:    Room (SQLite) on-device with a bundled food database
Tech stack: Kotlin, Jetpack Compose, Room, Vico charts
```

---

## Example 10

**Intent:**
habit tracker w streaks pls

**Spec:**
```
Type:       Mobile application
Data model: Habit(id, name, icon, color, frequency, target_per_period)
            Checkin(id, habit_id -> Habit, date)
Features:   - Create habits with daily or weekly frequency
            - Check in a habit for today with one tap
            - Calculate current and longest streaks
            - Show a year heatmap of check-ins per habit
            - Remind the user at a chosen time if not checked in
Storage:    MMKV (on-device key-value storage)
Tech stack: React Native, MMKV, Notifee
```

---

## Example 11

**Intent:**
guitar practice log in flutter, with a metronome inside

**Spec:**
```
Type:       Mobile application
Data model: PracticeSession(id, started_at, duration_min, focus, notes)
            Exercise(id, name, target_bpm)
            ExerciseLog(id, session_id -> PracticeSession, exercise_id -> Exercise, bpm_reached)
Features:   - Run a metronome with adjustable BPM and time signature
            - Time practice sessions and tag their focus
            - Log the BPM reached on each exercise
            - Chart BPM progress per exercise over time
            - Show weekly practice minutes
Storage:    Isar (on-device database)
Tech stack: Flutter, just_audio (metronome clicks), Isar
```

---

## Example 12

**Intent:**
an app that reads my book list and tells me how many pages i read per week

**Spec:**
```
Type:       Mobile application
Data model: Book(id, title, author, total_pages, status, started_on, finished_on)
            ReadingSession(id, book_id -> Book, date, start_page, end_page)
Features:   - Add books by scanning the ISBN barcode
            - Log reading sessions with start and end page
            - Calculate pages read per week
            - Show progress percentage for books in progress
            - List finished books by year
Storage:    SwiftData (on-device)
Tech stack: Swift, SwiftUI, VisionKit (barcode scanner), SwiftData
```

---

## Example 13

**Intent:**
my kid is diabetic type 1 and i need to log his blood sugar and insulin doses so i can show the doctor every 3 months

**Spec:**
```
Type:       Mobile application
Data model: GlucoseReading(id, value_mmol, measured_at, context)
            InsulinDose(id, units, insulin_type, given_at)
            Meal(id, carbs_g, eaten_at, note)
Features:   - Log glucose readings with context (before meal, after meal, night)
            - Log insulin doses by type and units
            - Log meals with carbohydrate grams
            - Show a daily timeline of readings, meals and doses
            - Export a 90-day report as PDF for the doctor
Storage:    Local on-device database (SQLite, encrypted with SQLCipher)
Tech stack: Flutter, sqflite, pdf package
```

---

## Example 14

**Intent:**
water intake but for my apple watch

**Spec:**
```
Type:       Mobile application (watchOS companion)
Data model: Drink(id, amount_ml, drink_type, logged_at)
            Goal(daily_ml)
Features:   - Log a drink from the watch with preset sizes
            - Show progress toward the daily goal as a ring
            - Sync drinks to Apple Health
            - Show a complication with today's total
            - Tap a reminder notification to log a glass
Storage:    HealthKit and SwiftData (on-device)
Tech stack: Swift, SwiftUI, WatchKit, HealthKit, WidgetKit (complications)
```

---

## Example 15

**Intent:**
offline app to convert units when cooking (cups, grams, ml, oz)

**Spec:**
```
Type:       Mobile application (offline)
Data model: Ingredient(id, name, grams_per_cup)
            FavouriteConversion(id, from_unit, to_unit, ingredient_id -> Ingredient)
Features:   - Convert between volume and weight units
            - Use ingredient density for cup to gram conversions
            - Scale a recipe quantity by a factor
            - Save favourite conversions for quick access
Storage:    Bundled ingredient table in a local SQLite file
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 16

**Intent:**
Something to remind me to stretch every hour when I sit at desk, with short videos of the stretch

**Spec:**
```
Type:       Mobile application
Data model: Stretch(id, name, body_area, duration_s, video_path)
            Routine(id, name)
            RoutineStretch(routine_id -> Routine, stretch_id -> Stretch, position)
            SessionLog(id, routine_id -> Routine, completed_at)
Features:   - Send a notification every hour during working hours
            - Play a short stretch routine with bundled videos
            - Build custom routines from the stretch library
            - Skip reminders during calendar meetings
            - Count completed sessions per day
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-video, Notifee, SQLite
```

---

## Example 17

**Intent:**
plant id app that takes a picture of leaf and says if the plant is sick

**Spec:**
```
Type:       Mobile application (on-device ML)
Data model: Diagnosis(id, photo_path, predicted_disease, confidence, taken_at)
            Disease(id, name, description, treatment)
Features:   - Take or choose a photo of a leaf
            - Classify the leaf disease with an on-device image model
            - Show top 3 predictions with confidence
            - Show treatment advice for the predicted disease
            - Keep a history of scans per plant
Storage:    Room (SQLite) on-device
Tech stack: Kotlin, Jetpack Compose, CameraX, TensorFlow Lite (MobileNet fine-tuned on PlantVillage), Room
```

---

## Example 18

**Intent:**
period tracker that doesnt send my data anywhere

**Spec:**
```
Type:       Mobile application (offline, privacy-focused)
Data model: Cycle(id, start_date, end_date)
            DayLog(id, date, flow, symptoms, mood, note)
Features:   - Log period start and end days
            - Log daily symptoms, flow and mood
            - Predict the next period and fertile window from past cycles
            - Lock the app with a PIN or biometrics
            - Export and import an encrypted backup file
Storage:    Encrypted local database (SQLCipher), no network access
Tech stack: Flutter, sqflite_sqlcipher, local_auth
```

---

## Example 19

**Intent:**
shopping list my wife and me can both use

**Spec:**
```
Type:       Mobile application with backend
Auth:       Sign in with Google or Apple; share a list by invite link
Data model: User(id, name, email)
            List(id, name, owner_id -> User)
            ListMember(list_id -> List, user_id -> User)
            Item(id, list_id -> List, name, quantity, is_bought, added_by -> User)
Features:   - Create shopping lists and invite a partner
            - Add items with quantity
            - Tick items as bought and sync in real time
            - Clear bought items
            - Work offline and sync when back online
Storage:    Cloud Firestore (with offline persistence)
Tech stack: Flutter, Firebase Auth, Cloud Firestore
```

---

## Example 20

**Intent:**
i want an app to log my migraines, when they happen, how bad, what i ate, weather, so i can find triggers

**Spec:**
```
Type:       Mobile application
Data model: Migraine(id, started_at, ended_at, severity, medication_taken, relief)
            Trigger(id, name)
            MigraineTrigger(migraine_id -> Migraine, trigger_id -> Trigger)
            WeatherSnapshot(id, migraine_id -> Migraine, pressure_hpa, temp_c)
Features:   - Log a migraine with start time, severity and medication
            - Tag possible triggers like food, sleep or stress
            - Save barometric pressure automatically from a weather API
            - Show a calendar of migraine days
            - Rank triggers by how often they appear before attacks
Storage:    Core Data (on-device)
Tech stack: Swift, SwiftUI, WeatherKit, Core Data
```

---

## Example 21

**Intent:**
Bird watching list. I want to write which birds I saw and where.

**Spec:**
```
Type:       Mobile application
Data model: Species(id, common_name, latin_name)
            Sighting(id, species_id -> Species, seen_at, lat, lng, count, photo_path, note)
Features:   - Search a bundled species list by name
            - Log a sighting with GPS location and count
            - Attach a photo to a sighting
            - Show sightings on a map
            - Show a life list of all species seen
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-maps, expo-sqlite
```

---

## Example 22

**Intent:**
Make me an app for my vinyl record collection

**Spec:**
```
Type:       Mobile application
Data model: Record(id, artist, title, year, label, format, condition, cover_path, purchase_price)
            Wishlist(id, artist, title, max_price)
Features:   - Add records by scanning the barcode and looking up Discogs
            - Store condition, format and purchase price
            - Search and sort the collection by artist or year
            - Keep a wishlist of records to buy
            - Show collection size and total value
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, mobile_scanner, Discogs API, Drift
```

---

## Example 23

**Intent:**
workout log for the gym. sets reps weight

**Spec:**
```
Type:       Mobile application
Data model: Exercise(id, name, muscle_group)
            Workout(id, date, notes)
            Set(id, workout_id -> Workout, exercise_id -> Exercise, reps, weight_kg, rpe)
Features:   - Start a workout and add exercises
            - Log sets with reps, weight and RPE
            - Show the previous session's numbers for each exercise
            - Run a rest timer between sets
            - Chart estimated one-rep max per exercise
Storage:    Room (SQLite) on-device
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 24

**Intent:**
a journal where i write one line a day and later it shows me what i wrote same day last years

**Spec:**
```
Type:       Mobile application
Data model: Entry(id, date, text, mood)
Features:   - Write one short entry per day with a character limit
            - Show entries from the same date in previous years
            - Remind the user each evening to write
            - Search entries by keyword
            - Export all entries as a text file
Storage:    SwiftData (on-device), optional iCloud sync with CloudKit
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 25

**Intent:**
app that helps me fast 16:8

**Spec:**
```
Type:       Mobile application
Data model: Fast(id, started_at, ended_at, target_hours, completed)
            Weight(id, kg, measured_on)
Features:   - Start and stop a fast with a live countdown
            - Choose a fasting plan like 16:8 or 18:6
            - Notify when the eating window opens and closes
            - Show fasting history and success rate
            - Log weight alongside fasts
Storage:    AsyncStorage (on-device)
Tech stack: React Native, Notifee, AsyncStorage
```

---

## Example 26

**Intent:**
ok so my grandma is going blind slowly and she still wants to read her mail. I want something on her android phone where she points the camera and it reads the text out loud to her. big buttons please she is 84

**Spec:**
```
Type:       Mobile application (accessibility)
Features:   - Capture text from the camera with one large button
            - Recognise text on-device with OCR
            - Read the text aloud with text-to-speech
            - Let her pause, repeat or slow down the speech
            - Use a high-contrast large-button layout with TalkBack support
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, CameraX, ML Kit Text Recognition, Android TextToSpeech
```

---

## Example 27

**Intent:**
savings goals app. like save 500 for new phone and see the progress bar

**Spec:**
```
Type:       Mobile application
Data model: Goal(id, name, target_amount, deadline, icon)
            Deposit(id, goal_id -> Goal, amount, deposited_on)
Features:   - Create savings goals with target and deadline
            - Add deposits and withdrawals to a goal
            - Show a progress bar and amount left
            - Calculate how much to save per week to reach the deadline
            - Celebrate when a goal is reached
Storage:    Hive (on-device)
Tech stack: Flutter, Hive
```

---

## Example 28

**Intent:**
kotlin app that counts my steps and shows a graph

**Spec:**
```
Type:       Mobile application
Data model: StepDay(date, steps, goal)
Features:   - Read daily steps from Health Connect
            - Show today's steps against a goal
            - Chart steps for the last 7 and 30 days
            - Send a notification when the goal is reached
Storage:    Room (cached daily totals), Health Connect as source
Tech stack: Kotlin, Jetpack Compose, Health Connect API, Room, Vico charts
```

---

## Example 29

**Intent:**
I want a baby tracker. feeding times, diapers, sleep. my wife and I take turns at night and we are SO tired

**Spec:**
```
Type:       Mobile application with backend
Auth:       Family account with invite code shared between parents
Data model: Baby(id, name, birth_date)
            Feeding(id, baby_id -> Baby, type, side, amount_ml, started_at, ended_at, logged_by)
            Diaper(id, baby_id -> Baby, kind, changed_at)
            Nap(id, baby_id -> Baby, started_at, ended_at)
Features:   - Log feedings, diapers and sleep with one-tap buttons
            - Show time since last feeding on the home screen
            - Sync entries between both parents' phones
            - Show daily totals and a 24-hour timeline
            - Use a dark night mode with large buttons
Storage:    Firebase Firestore with offline cache
Tech stack: React Native, Firebase Auth, Firestore
```

---

## Example 30

**Intent:**
wat app can help me memorize bible verses

**Spec:**
```
Type:       Mobile application
Data model: Verse(id, reference, text, translation)
            Practice(id, verse_id -> Verse, practiced_at, score)
Features:   - Add verses by reference and text
            - Practice by hiding words progressively
            - Type the verse from memory and score accuracy
            - Schedule reviews with spaced repetition
            - Show memorised verse count
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 31

**Intent:**
coffee brew timer for pour over

**Spec:**
```
Type:       Mobile application (offline)
Data model: Recipe(id, name, coffee_g, water_g, grind, temp_c)
            Step(id, recipe_id -> Recipe, position, label, pour_to_g, at_second)
            Brew(id, recipe_id -> Recipe, brewed_at, rating, note)
Features:   - Save brew recipes with ratio, grind and water temperature
            - Run a step-by-step timer with pour targets
            - Play a sound at each step
            - Rate brews and add tasting notes
Storage:    SwiftData (on-device)
Tech stack: Swift, SwiftUI, AVFoundation, SwiftData
```

---

## Example 32

**Intent:**
Je voudrais an app for split money with friends on holiday, who pay what and who owes who at the end

**Spec:**
```
Type:       Mobile application
Data model: Trip(id, name, currency)
            Person(id, trip_id -> Trip, name)
            Expense(id, trip_id -> Trip, paid_by -> Person, amount, description, spent_on)
            Share(expense_id -> Expense, person_id -> Person, amount)
Features:   - Create a trip and add people
            - Add expenses split equally or by custom amounts
            - Calculate each person's balance
            - Compute the minimum set of payments to settle up
            - Share the summary as text or PDF
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, share_plus
```

---

## Example 33

**Intent:**
anxiety app with breathing exercises

**Spec:**
```
Type:       Mobile application
Data model: BreathingPattern(id, name, inhale_s, hold_s, exhale_s, hold_after_s)
            Session(id, pattern_id -> BreathingPattern, started_at, duration_s, anxiety_before, anxiety_after)
Features:   - Guide breathing with an animated expanding circle
            - Offer patterns like box breathing and 4-7-8
            - Use haptic feedback for each phase
            - Rate anxiety before and after a session
            - Show sessions and average improvement over time
Storage:    Local on-device database (SQLite)
Tech stack: React Native, Reanimated, expo-haptics, expo-sqlite
```

---

## Example 34

**Intent:**
app for car maintenance, oil change, tires etc and remind me

**Spec:**
```
Type:       Mobile application
Data model: Vehicle(id, name, make, model, year, odometer_km)
            ServiceType(id, name, interval_km, interval_months)
            ServiceRecord(id, vehicle_id -> Vehicle, service_type_id -> ServiceType, done_on, odometer_km, cost, receipt_path)
Features:   - Add vehicles with current odometer
            - Log services with cost and a receipt photo
            - Calculate the next due date and mileage per service
            - Notify when a service is due soon
            - Show total maintenance cost per year
Storage:    Room (SQLite) on-device
Tech stack: Kotlin, Jetpack Compose, Room, WorkManager
```

---

## Example 35

**Intent:**
track my moods

**Spec:**
```
Type:       Mobile application
Data model: MoodEntry(id, mood_level, emotions, note, created_at)
            Activity(id, name, icon)
            EntryActivity(entry_id -> MoodEntry, activity_id -> Activity)
Features:   - Log mood on a 5-point scale with emotion tags
            - Tag what you did that day
            - Show a monthly mood calendar
            - Find activities linked with better moods
            - Remind once a day to check in
Storage:    Isar (on-device)
Tech stack: Flutter, Isar, fl_chart
```

---

## Example 36

**Intent:**
i do watercolor painting as hobby and want to keep a catalog of my paints colors and which brand

**Spec:**
```
Type:       Mobile application
Data model: Paint(id, brand, name, pigment_code, color_hex, lightfastness, transparency, owned)
            Swatch(id, paint_id -> Paint, photo_path)
            Palette(id, name)
            PalettePaint(palette_id -> Palette, paint_id -> Paint)
Features:   - Add paints with brand, pigment code and properties
            - Photograph a swatch card and pick its colour
            - Group paints into palettes
            - Filter paints by pigment or brand
            - Mark paints to rebuy
Storage:    SwiftData (on-device)
Tech stack: Swift, SwiftUI, PhotosUI, SwiftData
```

---

## Example 37

**Intent:**
Hi! I teach piano to kids and want an app for my students to log their practice at home, but it can be on their phone only, no server.

**Spec:**
```
Type:       Mobile application
Data model: Piece(id, title, composer, assigned_on)
            Practice(id, piece_id -> Piece, date, minutes, hands, difficulty_note)
            Sticker(id, awarded_for, earned_on)
Features:   - List pieces assigned by the teacher
            - Log practice minutes per piece with a timer
            - Award stickers for daily streaks
            - Record short audio clips of playing
            - Export a weekly practice report to show at the lesson
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, record (audio), sqflite, pdf
```

---

## Example 38

**Intent:**
language vocab app. i add words i see in netflix and it quizzes me

**Spec:**
```
Type:       Mobile application
Data model: Word(id, term, translation, example_sentence, source, added_at)
            QuizResult(id, word_id -> Word, answered_at, correct)
Features:   - Add words with translation and an example sentence
            - Quiz with multiple choice and typed answers
            - Prioritise words answered wrong recently
            - Pronounce words with text-to-speech
            - Show words learned per week
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-speech, expo-sqlite
```

---

## Example 39

**Intent:**
blood pressure log

**Spec:**
```
Type:       Mobile application
Data model: Reading(id, systolic, diastolic, pulse, arm, position, measured_at, note)
Features:   - Log readings with systolic, diastolic and pulse
            - Classify each reading by blood pressure category
            - Chart morning and evening averages
            - Remind to measure twice a day
            - Export readings as CSV or PDF for a doctor
Storage:    Room (SQLite) on-device
Tech stack: Kotlin, Jetpack Compose, Room, Vico
```

---

## Example 40

**Intent:**
something to keep all my warranty papers and receipts so i know when warranty ends

**Spec:**
```
Type:       Mobile application
Data model: Item(id, name, store, bought_on, price, warranty_months, category)
            Document(id, item_id -> Item, file_path, kind)
Features:   - Scan receipts and warranty cards with the camera
            - Store purchase date and warranty length
            - Calculate warranty expiry dates
            - Notify one month before a warranty ends
            - Search items by name or store
Storage:    Core Data with files in the app sandbox
Tech stack: Swift, SwiftUI, VisionKit document scanner, Core Data
```

---

## Example 41

**Intent:**
Make chore chart for my 3 kids with points they can trade for screen time

**Spec:**
```
Type:       Mobile application (family, offline)
Data model: Child(id, name, avatar, pin)
            Chore(id, title, points, recurrence)
            ChoreAssignment(id, chore_id -> Chore, child_id -> Child, due_on, done_at, approved)
            Reward(id, title, cost_points)
            Redemption(id, child_id -> Child, reward_id -> Reward, redeemed_at)
Features:   - Create chores with points and recurrence
            - Assign chores to each child
            - Let children mark chores done and parents approve
            - Track each child's points balance
            - Redeem points for rewards like screen time
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, local_auth (parent mode)
```

---

## Example 42

**Intent:**
im a nurse on shifts and i need to see my shift calendar and how much hours i did this month

**Spec:**
```
Type:       Mobile application
Data model: ShiftType(id, name, start_time, end_time, color)
            Shift(id, shift_type_id -> ShiftType, date, actual_start, actual_end, note)
Features:   - Define shift types like early, late and night
            - Fill in the month calendar by tapping shift types
            - Calculate hours worked per month including night hours
            - Show overtime against contracted hours
            - Export the calendar to the phone calendar
Storage:    Room (SQLite) on-device
Tech stack: Kotlin, Jetpack Compose, Room, CalendarContract
```

---

## Example 43

**Intent:**
aquarium water test tracker

**Spec:**
```
Type:       Mobile application
Data model: Tank(id, name, volume_l, type)
            WaterTest(id, tank_id -> Tank, tested_at, ph, ammonia, nitrite, nitrate, temp_c)
            WaterChange(id, tank_id -> Tank, done_at, percent)
Features:   - Log water parameters per tank
            - Highlight values outside safe ranges
            - Chart each parameter over time
            - Log water changes
            - Remind about weekly tests
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Victory Native
```

---

## Example 44

**Intent:**
me want app to remember where i park car

**Spec:**
```
Type:       Mobile application (offline)
Data model: ParkingSpot(id, lat, lng, saved_at, photo_path, floor, note, meter_expires_at)
Features:   - Save the current GPS location with one tap
            - Add a photo and note like floor or level
            - Show walking directions back to the car
            - Set a reminder for parking meter expiry
            - Keep a short history of spots
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Core Location, MapKit, UserNotifications
```

---

## Example 45

**Intent:**
I'd like an app that helps me study for my driving theory test, with the official question bank and mock exams

**Spec:**
```
Type:       Mobile application
Data model: Question(id, category, text, image_path, options, correct_option, explanation)
            Attempt(id, question_id -> Question, answered_at, chosen_option, correct)
            MockExam(id, started_at, score, passed)
Features:   - Practise questions by category
            - Show explanations after each answer
            - Run timed mock exams with the official pass mark
            - Repeat questions answered wrong
            - Show readiness per category
Storage:    Bundled question bank in SQLite, progress in local SQLite
Tech stack: Flutter, sqflite
```

---

## Example 46

**Intent:**
tiny app to count how many cigarettes i smoke a day bc im trying to quit

**Spec:**
```
Type:       Mobile application
Data model: Cigarette(id, smoked_at, trigger)
            QuitPlan(daily_limit, price_per_pack, cigs_per_pack)
Features:   - Log a cigarette with one tap and optional trigger
            - Show today's count against a daily limit
            - Show money spent and saved
            - Show time since last cigarette
            - Chart daily counts over time
Storage:    Room (SQLite) on-device
Tech stack: Kotlin, Jetpack Compose, DataStore, Room
```

---

## Example 47

**Intent:**
recipe box app for my family recipes, with photos, and when cooking keep the screen on

**Spec:**
```
Type:       Mobile application
Data model: Recipe(id, title, servings, prep_min, cook_min, photo_path, source)
            Ingredient(id, recipe_id -> Recipe, name, quantity, unit)
            Step(id, recipe_id -> Recipe, position, text)
Features:   - Add recipes with photos, ingredients and steps
            - Scale ingredient amounts by servings
            - Open a cooking mode that keeps the screen awake
            - Search recipes by ingredient
            - Tag recipes by category
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-keep-awake, expo-image-picker, expo-sqlite
```

---

## Example 48

**Intent:**
hey can u build me app for tracking my crypto coins, just my holdings, prices from internet

**Spec:**
```
Type:       Mobile application
Data model: Holding(id, coin_symbol, amount, avg_buy_price)
            Transaction(id, coin_symbol, type, amount, price, executed_at)
Features:   - Add buy and sell transactions per coin
            - Fetch current prices from the CoinGecko API
            - Show portfolio value and profit or loss
            - Show allocation as a pie chart
            - Cache last prices for offline viewing
Storage:    Hive (on-device)
Tech stack: Flutter, CoinGecko API, Hive, fl_chart
```

---

## Example 49

**Intent:**
allergy diary for pollen season

**Spec:**
```
Type:       Mobile application
Data model: SymptomLog(id, date, sneezing, itchy_eyes, congestion, medication_taken)
            PollenReading(id, date, tree, grass, weed)
Features:   - Log daily allergy symptoms with sliders
            - Fetch the daily pollen forecast for the user's location
            - Chart symptoms against pollen levels
            - Remind to take antihistamines
            - Warn on high pollen days in the morning
Storage:    SwiftData (on-device)
Tech stack: Swift, SwiftUI, Google Pollen API, SwiftData
```

---

## Example 50

**Intent:**
for my dad who has parkinsons, an app to measure tremor with the phone sensors

**Spec:**
```
Type:       Mobile application (health sensing)
Data model: TremorTest(id, recorded_at, hand, duration_s, dominant_freq_hz, amplitude, medication_state)
            RawSample(id, test_id -> TremorTest, t_ms, ax, ay, az)
Features:   - Record accelerometer data while the phone is held for 30 seconds
            - Compute tremor frequency and amplitude with FFT
            - Tag tests by hand and medication on/off state
            - Chart tremor amplitude over weeks
            - Export results for the neurologist
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Android SensorManager, JTransforms (FFT), Room
```

---

## Example 51

**Intent:**
Stamp collection catalog

**Spec:**
```
Type:       Mobile application
Data model: Stamp(id, country, year, face_value, catalog_number, condition, photo_path, album_id -> Album)
            Album(id, name)
Features:   - Add stamps with country, year and catalog number
            - Photograph each stamp
            - Organise stamps into albums
            - Filter by country and year
            - Show collection count per country
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, image_picker, Drift
```

---

## Example 52

**Intent:**
pomodoro timer that also logs what i studied

**Spec:**
```
Type:       Mobile application
Data model: Subject(id, name, color)
            FocusSession(id, subject_id -> Subject, started_at, duration_min, completed)
Features:   - Run 25-minute focus and 5-minute break timers
            - Choose a subject before each session
            - Keep the timer running in the background with a notification
            - Show study minutes per subject per week
            - Block the phone with Do Not Disturb during focus
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Foreground Service, Room
```

---

## Example 53

**Intent:**
An app where I can see all my subscriptions and how much they cost me in a year

**Spec:**
```
Type:       Mobile application
Data model: Subscription(id, name, price, currency, billing_cycle, next_renewal, category, cancel_url)
Features:   - Add subscriptions with price and billing cycle
            - Calculate monthly and yearly totals
            - Notify a few days before each renewal
            - Show spending by category
            - Mark subscriptions to cancel
Storage:    SwiftData (on-device)
Tech stack: Swift, SwiftUI, SwiftData, UserNotifications
```

---

## Example 54

**Intent:**
i got a small vegetable garden and want to plan what to plant when based on my area, and keep notes what grew good

**Spec:**
```
Type:       Mobile application
Data model: Crop(id, name, sow_indoor_weeks, sow_outdoor_weeks, days_to_harvest, spacing_cm)
            Bed(id, name, width_cm, length_cm)
            Planting(id, crop_id -> Crop, bed_id -> Bed, sown_on, harvested_on, yield_note, rating)
Features:   - Set the last frost date for the user's area
            - Show a sowing calendar per crop based on frost date
            - Plan which crops go in each bed
            - Log harvests and rate how well each crop did
            - Remind when it is time to sow or transplant
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 55

**Intent:**
fertility basal temperature chart

**Spec:**
```
Type:       Mobile application
Data model: TempReading(id, date, temp_c, time_taken, disturbed)
            CycleDay(id, date, cervical_mucus, period_flow)
Features:   - Log morning basal body temperature
            - Plot a temperature chart per cycle
            - Detect the temperature shift after ovulation
            - Mark disturbed readings to exclude them
            - Export a cycle chart as an image
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-svg, expo-sqlite
```

---

## Example 56

**Intent:**
hearing test app with headphones

**Spec:**
```
Type:       Mobile application (accessibility)
Data model: HearingTest(id, taken_at, headphones_model)
            Threshold(id, test_id -> HearingTest, ear, frequency_hz, db_level)
Features:   - Play pure tones at 250 Hz to 8 kHz in each ear
            - Find the quietest heard level with an up-down method
            - Draw an audiogram of the results
            - Compare results with earlier tests
            - Warn that the test is not a medical diagnosis
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVAudioEngine, Swift Charts, SwiftData
```

---

## Example 57

**Intent:**
flashcard app in react native where i can import from csv

**Spec:**
```
Type:       Mobile application
Data model: Deck(id, name, created_at)
            Card(id, deck_id -> Deck, front, back, due_at, interval_days, ease)
Features:   - Import cards from a CSV file with front and back columns
            - Study due cards with flip animation
            - Schedule cards with spaced repetition
            - Export a deck back to CSV
            - Show study statistics per deck
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-document-picker, papaparse, expo-sqlite
```

---

## Example 58

**Intent:**
tool for measuring room size with phone camera AR

**Spec:**
```
Type:       Mobile application (augmented reality)
Data model: Room(id, name, created_at)
            Measurement(id, room_id -> Room, label, length_m, start_point, end_point)
Features:   - Detect floor and wall planes with AR
            - Measure distances by tapping two points
            - Calculate room floor area
            - Save measurements per room
            - Export a simple floor plan image
Storage:    Local on-device database (SQLite)
Tech stack: Swift, ARKit, RealityKit, SwiftUI, SwiftData
```

---

## Example 59

**Intent:**
I want to log my cats vet visits vaccine and weight, i have 4 cats

**Spec:**
```
Type:       Mobile application
Data model: Cat(id, name, birth_date, breed, photo_path, chip_number)
            WeightLog(id, cat_id -> Cat, kg, measured_on)
            Vaccination(id, cat_id -> Cat, vaccine, given_on, next_due)
            VetVisit(id, cat_id -> Cat, visited_on, reason, cost, notes)
Features:   - Keep a profile for each cat
            - Log weight and chart it over time
            - Record vaccinations and notify when the next is due
            - Log vet visits with cost and notes
            - Show total vet spending per cat
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, flutter_local_notifications
```

---

## Example 60

**Intent:**
offline maps for hiking with my own gpx tracks

**Spec:**
```
Type:       Mobile application (offline)
Data model: Track(id, name, file_path, distance_m, elevation_gain_m, imported_at)
            MapRegion(id, name, bounds, zoom_min, zoom_max, size_mb)
Features:   - Download map tiles for a region for offline use
            - Import GPX tracks and show them on the map
            - Show current position and distance remaining on the track
            - Show an elevation profile
            - Record a new track and export it as GPX
Storage:    MBTiles files and SQLite on-device
Tech stack: Kotlin, Jetpack Compose, MapLibre Native, Room
```

---

## Example 61

**Intent:**
sobriety counter

**Spec:**
```
Type:       Mobile application
Data model: SobrietyStart(id, substance, started_on, daily_cost)
            Milestone(id, days, reached_on)
            Journal(id, written_on, text, craving_level)
Features:   - Show days, hours and minutes sober
            - Calculate money saved
            - Unlock milestone badges at 1, 7, 30 and 365 days
            - Write a daily journal with craving level
            - Reset the counter while keeping history
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, expo-notifications
```

---

## Example 62

**Intent:**
I'd like a bullet journal style app with daily, monthly and future logs.

**Spec:**
```
Type:       Mobile application
Data model: Entry(id, date, kind, text, status, collection_id -> Collection)
            Collection(id, title, type)
Features:   - Write rapid-log entries as tasks, events or notes
            - Mark tasks done, migrated or cancelled
            - Migrate open tasks to the next day or month
            - Keep monthly and future logs
            - Create custom collections like reading lists
Storage:    SwiftData (on-device)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 63

**Intent:**
barcode scan my pantry and tell me when stuff expires

**Spec:**
```
Type:       Mobile application
Data model: Product(id, barcode, name, brand, image_url)
            PantryItem(id, product_id -> Product, quantity, location, expires_on, added_on)
Features:   - Scan a barcode and look up the product on Open Food Facts
            - Add the expiry date and storage location
            - List items expiring in the next 7 days
            - Notify the day before an item expires
            - Suggest using expiring items first
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, ML Kit Barcode Scanning, Open Food Facts API, Room
```

---

## Example 64

**Intent:**
chess opening trainer

**Spec:**
```
Type:       Mobile application (offline)
Data model: Opening(id, name, eco_code, color)
            Line(id, opening_id -> Opening, moves_pgn)
            DrillResult(id, line_id -> Line, drilled_at, mistakes)
Features:   - Show a chessboard where the user plays the opening moves
            - Check each move against saved lines
            - Import repertoire lines from PGN
            - Repeat lines with mistakes more often
            - Show mastery per opening
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, chess (Dart move validation), sqflite
```

---

## Example 65

**Intent:**
Something simple to write down how much my electricity meter is every month and show if I use more than last year

**Spec:**
```
Type:       Mobile application
Data model: MeterReading(id, meter_type, value, read_on, photo_path)
            Tariff(id, meter_type, price_per_unit, valid_from)
Features:   - Log meter readings with an optional photo
            - Calculate monthly usage from consecutive readings
            - Compare usage with the same month last year
            - Estimate costs from the tariff
            - Support electricity, gas and water meters
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-camera, expo-sqlite
```

---

## Example 66

**Intent:**
knitting row counter that i can tap with big button

**Spec:**
```
Type:       Mobile application
Data model: Project(id, name, pattern_name, yarn, needle_size)
            Counter(id, project_id -> Project, label, value, repeat_every)
Features:   - Increment a row counter with a large tap area or the volume button
            - Keep several counters per project
            - Reset a counter automatically after a repeat
            - Keep the screen on while knitting
            - Save notes and pattern photos per project
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 67

**Intent:**
swimming laps counter for apple watch

**Spec:**
```
Type:       Mobile application (watchOS)
Data model: SwimWorkout(id, started_at, pool_length_m, laps, distance_m, duration_s)
            LapSplit(id, workout_id -> SwimWorkout, lap_number, duration_s, stroke)
Features:   - Start a pool swim workout with a chosen pool length
            - Count laps and detect stroke type from motion
            - Show per-lap split times
            - Save workouts to Apple Health
            - Show weekly swim distance on the iPhone
Storage:    HealthKit and SwiftData (on-device)
Tech stack: Swift, SwiftUI, HealthKit (HKWorkoutSession), WatchConnectivity
```

---

## Example 68

**Intent:**
need app to remember birthdays of all my relatives and suggest gifts

**Spec:**
```
Type:       Mobile application
Data model: Person(id, name, birthday, relation, photo_path)
            GiftIdea(id, person_id -> Person, idea, price, url, given_on)
Features:   - Import birthdays from phone contacts
            - Notify a week before and on the birthday
            - Show upcoming birthdays with age turning
            - Keep gift ideas per person
            - Mark gifts as given to avoid repeats
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Contacts Provider, Room, WorkManager
```

---

## Example 69

**Intent:**
a calorie counter but with taking a photo of the food

**Spec:**
```
Type:       Mobile application with backend
Data model: Meal(id, photo_path, eaten_at, meal_type)
            MealItem(id, meal_id -> Meal, food_name, grams, kcal, protein_g, carbs_g, fat_g)
Features:   - Take a photo of a meal
            - Recognise foods and estimate portions with a vision model
            - Let the user correct foods and grams
            - Calculate calories and macros per meal
            - Show daily totals against a calorie goal
API:        REST
            POST /analyze-meal (photo upload)
Storage:    SQLite on-device; photos sent only for analysis
Tech stack: Flutter, FastAPI backend, vision model for food recognition, USDA FoodData Central
```

---

## Example 70

**Intent:**
Hey, I'm a uni student and I always lose track of which assignments are due when and how much they count for my grade. I'd love an app where I put in my courses, the assignments and weights, and it tells me what grade I need on the final to pass.

**Spec:**
```
Type:       Mobile application
Data model: Course(id, name, credits, target_grade)
            Assessment(id, course_id -> Course, title, weight_percent, due_on, score, max_score)
Features:   - Add courses with their assessments and weights
            - Enter scores as they come in
            - Calculate the current weighted grade per course
            - Calculate the score needed on remaining work to reach a target
            - List upcoming deadlines across all courses
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, expo-notifications
```

---

## Example 71

**Intent:**
shake phone to log something quick

**Spec:**
```
Type:       Mobile application (offline)
Data model: QuickLog(id, category, logged_at, lat, lng)
            Category(id, name, icon, position)
Features:   - Detect a shake gesture with the accelerometer
            - Log the default category with a timestamp on shake
            - Pick another category from a quick menu
            - Optionally save GPS location
            - Show counts per category per day
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, SensorManager, Room
```

---

## Example 72

**Intent:**
track my caffeine so i dont drink coffee too late

**Spec:**
```
Type:       Mobile application
Data model: Drink(id, name, caffeine_mg, consumed_at)
            Preset(id, name, caffeine_mg)
Features:   - Log drinks from presets like espresso or energy drink
            - Model caffeine still in the body using a half-life curve
            - Show when caffeine will drop below a sleep-friendly level
            - Warn when logging after a cutoff time
            - Sync caffeine to Apple Health
Storage:    SwiftData (on-device)
Tech stack: Swift, SwiftUI, HealthKit, Swift Charts, SwiftData
```

---

## Example 73

**Intent:**
i want a tracker for my eczema flare ups with photos so i can compare

**Spec:**
```
Type:       Mobile application
Data model: Flare(id, started_on, body_area, severity, itch_level)
            FlarePhoto(id, flare_id -> Flare, taken_at, file_path)
            Product(id, name, type)
            ProductUse(id, product_id -> Product, used_on)
Features:   - Log flare-ups by body area and severity
            - Take dated photos to compare skin over time
            - Show photos side by side
            - Log creams and products used
            - Chart itch levels against products
Storage:    Drift (SQLite) with photos stored in app storage, excluded from the gallery
Tech stack: Flutter, camera, Drift
```

---

## Example 74

**Intent:**
travel itinerary app, flights hotels and activities in a timeline, works without internet abroad

**Spec:**
```
Type:       Mobile application (offline-first)
Data model: Trip(id, title, start_date, end_date)
            ItineraryItem(id, trip_id -> Trip, kind, title, starts_at, ends_at, location, confirmation_code, notes)
            Attachment(id, item_id -> ItineraryItem, file_path)
Features:   - Create trips with a day-by-day timeline
            - Add flights, hotels and activities with confirmation codes
            - Attach PDF tickets and booking emails
            - Show the next item on the home screen
            - Work fully offline once saved
Storage:    Isar (on-device) with attachments in app storage
Tech stack: Flutter, Isar, file_picker
```

---

## Example 75

**Intent:**
count reps with camera for pushups

**Spec:**
```
Type:       Mobile application (on-device ML)
Data model: ExerciseSession(id, exercise, reps, started_at, duration_s)
Features:   - Detect body pose from the front camera
            - Count push-up and squat reps from joint angles
            - Announce each rep with voice
            - Save sessions with rep totals
            - Show weekly rep totals per exercise
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, CameraX, ML Kit Pose Detection, Room, TextToSpeech
```

---

## Example 76

**Intent:**
Diary app with password

**Spec:**
```
Type:       Mobile application
Data model: Entry(id, title, body, created_at, updated_at, mood)
            Photo(id, entry_id -> Entry, file_path)
Features:   - Write diary entries with title, text and photos
            - Lock the app with a passcode or Face ID
            - Encrypt entries on the device
            - Search entries by text and date
            - Show entries in a calendar view
Storage:    Encrypted SQLite (SQLCipher) on-device
Tech stack: Swift, SwiftUI, GRDB with SQLCipher, LocalAuthentication
```

---

## Example 77

**Intent:**
bouldering logbook, grades and gyms

**Spec:**
```
Type:       Mobile application
Data model: Gym(id, name, grading_system)
            Climb(id, gym_id -> Gym, grade, color, wall, attempts, sent, climbed_on, photo_path)
Features:   - Log boulder problems with grade, colour and attempts
            - Mark flashes and sends
            - Show highest grade sent per month
            - Convert between V-scale and Font grades
            - Show a session summary after each visit
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Victory Native
```

---

## Example 78

**Intent:**
medicine stock tracker so i dont run out

**Spec:**
```
Type:       Mobile application
Data model: Medicine(id, name, pills_per_pack, pills_left, daily_dose, refill_threshold)
            Refill(id, medicine_id -> Medicine, added_pills, refilled_on)
Features:   - Track remaining pills for each medicine
            - Decrease stock automatically by the daily dose
            - Estimate the date each medicine runs out
            - Notify when stock is below the refill threshold
            - Log refills
Storage:    Hive (on-device)
Tech stack: Flutter, Hive, flutter_local_notifications
```

---

## Example 79

**Intent:**
sign language alphabet learning app for kids

**Spec:**
```
Type:       Mobile application (education)
Data model: Sign(id, letter, video_path, image_path)
            Progress(id, sign_id -> Sign, correct_count, last_practiced)
Features:   - Show each letter with a looping video of the hand sign
            - Quiz children by showing a sign and four letters
            - Check signs made to the camera with a hand-pose model
            - Award stars for correct answers
            - Track which letters are learned
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVKit, Vision (hand pose detection), Core ML
```

---

## Example 80

**Intent:**
app to log fishing catches and spots

**Spec:**
```
Type:       Mobile application
Data model: Spot(id, name, lat, lng, water_type)
            Catch(id, spot_id -> Spot, species, length_cm, weight_kg, bait, caught_at, photo_path, released)
            Conditions(id, catch_id -> Catch, weather, water_temp_c, moon_phase)
Features:   - Save fishing spots privately on a map
            - Log catches with species, size, bait and photo
            - Record weather and moon phase automatically
            - Show which bait works best per species
            - Show catches per spot
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Google Maps SDK, Room, OpenWeatherMap API
```

---

## Example 81

**Intent:**
im really bad with money and i get paid weekly, i want an app that splits my paycheck into envelopes like rent food fun savings and i can see how much is left in each

**Spec:**
```
Type:       Mobile application
Data model: Envelope(id, name, percent_of_pay, balance)
            Paycheck(id, amount, received_on)
            Spend(id, envelope_id -> Envelope, amount, note, spent_on)
Features:   - Set envelopes with a percentage of each paycheck
            - Split a new paycheck across envelopes automatically
            - Log spending from an envelope
            - Show each envelope's remaining balance
            - Move money between envelopes
Storage:    WatermelonDB (SQLite) on-device
Tech stack: React Native, WatermelonDB
```

---

## Example 82

**Intent:**
app to log my sons football training and matches, goals, minutes played

**Spec:**
```
Type:       Mobile application
Data model: Season(id, name, team)
            Match(id, season_id -> Season, opponent, played_on, home, goals_for, goals_against)
            PlayerStat(id, match_id -> Match, minutes, goals, assists, rating)
            Training(id, date, duration_min, focus)
Features:   - Log matches with score and opponent
            - Record minutes, goals and assists per match
            - Log training sessions
            - Show season totals and averages
            - Share a season summary image
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, screenshot (image sharing)
```

---

## Example 83

**Intent:**
noise meter decibel

**Spec:**
```
Type:       Mobile application (offline utility)
Data model: Measurement(id, started_at, duration_s, avg_db, max_db, location_label)
Features:   - Measure sound level in dB from the microphone
            - Show live, average and peak values
            - Draw a live level graph
            - Save measurements with a label
            - Warn when level stays above 85 dB
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVAudioEngine, SwiftData
```

---

## Example 84

**Intent:**
i am lose my keys always. want app with bluetooth tag to find

**Spec:**
```
Type:       Mobile application (Bluetooth companion)
Data model: Tag(id, name, mac_address, icon, last_seen_lat, last_seen_lng, last_seen_at)
Features:   - Pair a Bluetooth Low Energy key tag
            - Make the tag beep from the app
            - Show signal strength as a hotter/colder indicator
            - Save the last location where the tag was seen
            - Alert when leaving the tag behind
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Android BLE API, Fused Location Provider, Room
```

---

## Example 85

**Intent:**
a gratitude journal, 3 things per day, in flutter

**Spec:**
```
Type:       Mobile application
Data model: GratitudeDay(id, date, item1, item2, item3, photo_path)
Features:   - Write three things you are grateful for each day
            - Remind in the evening
            - Show a random past entry on bad days
            - Show the current writing streak
            - Export entries as PDF
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, flutter_local_notifications, pdf
```

---

## Example 86

**Intent:**
posture reminder using airpods head tracking

**Spec:**
```
Type:       Mobile application (wearable companion)
Data model: PostureSample(id, recorded_at, pitch_deg)
            Session(id, started_at, ended_at, bad_posture_s)
Features:   - Read head pitch from AirPods motion sensors
            - Detect when the head tilts forward too long
            - Give a gentle audio or haptic alert
            - Show daily time in good vs bad posture
            - Calibrate the neutral head position
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, CoreMotion (CMHeadphoneMotionManager), SwiftData
```

---

## Example 87

**Intent:**
weight loss tracker with bmi

**Spec:**
```
Type:       Mobile application
Data model: Profile(height_cm, goal_kg, start_kg)
            WeighIn(id, kg, measured_on, photo_path)
Features:   - Log weight with date
            - Calculate BMI and its category
            - Chart weight with a 7-day moving average
            - Show progress toward the goal weight
            - Store optional progress photos
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, Health Connect
```

---

## Example 88

**Intent:**
I want to have a app on my phone that I can photograph business cards, no wait, my receipts, and it reads the total and shop and saves as expense

**Spec:**
```
Type:       Mobile application
Data model: Receipt(id, image_path, merchant, total, currency, purchased_on, category)
            LineItem(id, receipt_id -> Receipt, description, amount)
Features:   - Photograph a receipt with edge detection
            - Extract merchant, date and total with on-device OCR
            - Let the user correct the extracted fields
            - Categorise expenses
            - Export expenses for a month as CSV
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, google_mlkit_text_recognition, edge_detection, sqflite
```

---

## Example 89

**Intent:**
daily language lesson streak like duolingo but for my own sentences

**Spec:**
```
Type:       Mobile application
Data model: Sentence(id, native, target, audio_path, tags)
            Lesson(id, date, completed)
            Answer(id, lesson_id -> Lesson, sentence_id -> Sentence, correct)
Features:   - Add sentences with translation and recorded audio
            - Build a daily lesson of 10 sentences
            - Practise with translate, listen and word-order exercises
            - Keep a daily streak with reminders
            - Repeat sentences answered wrong
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-av, expo-sqlite
```

---

## Example 90

**Intent:**
offline first aid guide

**Spec:**
```
Type:       Mobile application (offline)
Data model: Topic(id, title, category, steps_markdown, image_path)
            Favourite(topic_id -> Topic)
Features:   - Browse first aid topics like burns, choking and CPR
            - Show step-by-step instructions with pictures
            - Run a CPR compression metronome at 110 BPM
            - Call the local emergency number with one tap
            - Work completely without internet
Storage:    Bundled content in a local SQLite file
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 91

**Intent:**
ios widget that shows how many days until my vacation

**Spec:**
```
Type:       Mobile application (iOS widget)
Data model: Countdown(id, title, target_date, emoji, color)
Features:   - Create countdowns to dates
            - Show days remaining on a home screen widget
            - Show a lock screen widget
            - Pick which countdown each widget shows
Storage:    App Group shared UserDefaults
Tech stack: Swift, SwiftUI, WidgetKit, App Intents
```

---

## Example 92

**Intent:**
sun position for photography golden hour

**Spec:**
```
Type:       Mobile application (photography utility)
Data model: Location(id, name, lat, lng)
            ShootPlan(id, location_id -> Location, date, notes)
Features:   - Calculate sunrise, sunset, golden and blue hour for a location and date
            - Show the sun direction on a map
            - Show moonrise and moon phase
            - Save shooting locations
            - Notify before golden hour begins
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, suncalc (Dart port), flutter_map, sqflite
```

---

## Example 93

**Intent:**
grocery price tracker so i know which store is cheapest for the stuff i buy

**Spec:**
```
Type:       Mobile application
Data model: Store(id, name)
            Product(id, name, unit)
            Price(id, product_id -> Product, store_id -> Store, price, recorded_on)
Features:   - Record product prices per store
            - Show the cheapest store for each product
            - Compare price history for a product
            - Calculate the cheapest store for a whole shopping list
            - Scan barcodes to find products fast
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-barcode-scanner, expo-sqlite
```

---

## Example 94

**Intent:**
Book club app where we vote on next book

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email magic-link login; join a club with an invite code
Data model: User(id, name, email)
            Club(id, name, invite_code)
            Membership(club_id -> Club, user_id -> User)
            BookSuggestion(id, club_id -> Club, title, author, suggested_by -> User)
            Vote(suggestion_id -> BookSuggestion, user_id -> User)
Features:   - Create a club and invite members
            - Suggest books for the next round
            - Vote on suggestions
            - Announce the winning book and meeting date
            - Discuss chapters in a simple thread
Storage:    Supabase Postgres
Tech stack: Flutter, Supabase (Auth, Postgres, Realtime)
```

---

## Example 95

**Intent:**
kegel exercise timer

**Spec:**
```
Type:       Mobile application
Data model: Routine(id, name, squeeze_s, relax_s, reps)
            Session(id, routine_id -> Routine, completed_at)
Features:   - Guide squeeze and relax phases with animation and vibration
            - Offer beginner to advanced routines
            - Remind three times a day discreetly
            - Track daily completion
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Core Haptics, SwiftData
```

---

## Example 96

**Intent:**
track the mileage of my running shoes

**Spec:**
```
Type:       Mobile application
Data model: Shoe(id, brand, model, bought_on, max_km, retired)
            Run(id, shoe_id -> Shoe, distance_km, date)
Features:   - Add shoes with an expected lifetime in km
            - Assign runs to shoes or import them from Strava
            - Show total km per shoe
            - Notify when a shoe nears its limit
            - Retire shoes and keep their history
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Strava API, Room
```

---

## Example 97

**Intent:**
whats a good app to make for me to learn morse code

**Spec:**
```
Type:       Mobile application (education, offline)
Data model: Lesson(id, letters, order)
            Progress(id, lesson_id -> Lesson, accuracy, completed_at)
Features:   - Play Morse code letters as audio tones
            - Teach letters with the Koch method
            - Let the user tap dots and dashes on the screen
            - Translate text to Morse and flash the torch
            - Track accuracy per lesson
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_soloud (tone generation), torch_light, Hive
```

---

## Example 98

**Intent:**
mood + period + sleep in one app pls i hate having 3 apps

**Spec:**
```
Type:       Mobile application
Data model: DayLog(id, date, mood, energy, sleep_hours, period_flow, symptoms, note)
Features:   - Log mood, sleep and period in one daily screen
            - Read sleep hours from Apple Health
            - Predict the next period
            - Show how mood changes across the cycle
            - Chart all three on one timeline
Storage:    SwiftData (on-device)
Tech stack: Swift, SwiftUI, HealthKit, Swift Charts, SwiftData
```

---

## Example 99

**Intent:**
An app to scan and organise my kids' school drawings so I can throw away the paper

**Spec:**
```
Type:       Mobile application
Data model: Child(id, name, birth_date)
            Artwork(id, child_id -> Child, image_path, title, created_on, grade_level)
Features:   - Scan drawings with automatic cropping
            - Tag each artwork by child and date
            - Browse artworks per child by school year
            - Mark favourites
            - Export a yearly photo book as PDF
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, ML Kit Document Scanner, Room, PdfDocument
```

---

## Example 100

**Intent:**
thing to write down dreams when i wake up, voice too

**Spec:**
```
Type:       Mobile application
Data model: Dream(id, recorded_at, title, text, audio_path, lucid, tags)
Features:   - Record a dream by voice right after waking
            - Transcribe the recording on-device
            - Tag dreams and mark lucid ones
            - Search dreams by keyword or tag
            - Show recurring themes
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Speech framework, AVFoundation, SwiftData
```

---

## Example 101

**Intent:**
wardrobe app what clothes i have and outfits

**Spec:**
```
Type:       Mobile application
Data model: Garment(id, category, color, brand, season, photo_path, times_worn)
            Outfit(id, name)
            OutfitGarment(outfit_id -> Outfit, garment_id -> Garment)
            WornLog(id, outfit_id -> Outfit, worn_on)
Features:   - Photograph clothes and remove the background
            - Tag garments by category, colour and season
            - Combine garments into outfits
            - Log what was worn each day
            - Show garments never worn
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-image-picker, on-device background removal, expo-sqlite
```

---

## Example 102

**Intent:**
offline password manager, no cloud

**Spec:**
```
Type:       Mobile application (offline, security)
Data model: VaultEntry(id, title, username, password_enc, url, notes_enc, updated_at)
            VaultMeta(salt, kdf_params)
Features:   - Encrypt the vault with a master password using Argon2 and AES-GCM
            - Add, edit and search entries
            - Generate strong passwords
            - Unlock with biometrics after first login
            - Export an encrypted backup file
Storage:    Encrypted local file in app storage
Tech stack: Kotlin, Jetpack Compose, Android Keystore, BiometricPrompt, Argon2kt
```

---

## Example 103

**Intent:**
workout timer for HIIT, tabata

**Spec:**
```
Type:       Mobile application
Data model: Timer(id, name, work_s, rest_s, rounds, sets, set_rest_s)
Features:   - Create interval timers with work, rest and rounds
            - Announce phases with sounds and voice
            - Keep running with the screen locked
            - Show the current round and time left large on screen
            - Save favourite timers
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, audioplayers, wakelock_plus, Hive
```

---

## Example 104

**Intent:**
i want an app to rate every beer i try with photo and where i drank it

**Spec:**
```
Type:       Mobile application
Data model: Beer(id, name, brewery, style, abv)
            Tasting(id, beer_id -> Beer, rating, notes, photo_path, place, tasted_on)
Features:   - Log tastings with rating, notes and photo
            - Save where the beer was drunk
            - Search past beers before ordering again
            - Show favourite styles and breweries
            - Show a map of tasting places
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-location, react-native-maps, expo-sqlite
```

---

## Example 105

**Intent:**
Simple app for my elderly father to call family by tapping their photo

**Spec:**
```
Type:       Mobile application (accessibility)
Data model: Contact(id, name, phone, photo_path, position)
Features:   - Show large photo tiles of family members
            - Call a contact with one tap
            - Let a caregiver edit contacts behind a PIN
            - Read the contact name aloud before calling
            - Prevent accidental exits from the app
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Android Telecom intents, Room
```

---

## Example 106

**Intent:**
I play board games with friends every week and I'd like to log who won each game and keep a leaderboard over the year

**Spec:**
```
Type:       Mobile application
Data model: Player(id, name)
            Game(id, title, min_players, max_players)
            Play(id, game_id -> Game, played_on, duration_min)
            PlayResult(play_id -> Play, player_id -> Player, score, won)
Features:   - Log game sessions with players and scores
            - Track winners per game
            - Show a yearly leaderboard by wins
            - Show most played games
            - Import the game list from BoardGameGeek
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, BoardGameGeek XML API
```

---

## Example 107

**Intent:**
menstrual cup reminder lol

**Spec:**
```
Type:       Mobile application
Data model: Insertion(id, inserted_at, removed_at)
            Settings(max_hours)
Features:   - Start a timer when the cup is inserted
            - Notify before the maximum wear time
            - Log removal
            - Show the current wear duration
Storage:    AsyncStorage (on-device)
Tech stack: React Native, Notifee, AsyncStorage
```

---

## Example 108

**Intent:**
home inventory for insurance, every room every item with photos and price

**Spec:**
```
Type:       Mobile application
Data model: Room(id, name)
            Item(id, room_id -> Room, name, brand, serial_number, purchase_price, purchased_on, photo_path)
            Receipt(id, item_id -> Item, file_path)
Features:   - Add items room by room with photos
            - Store serial numbers and purchase prices
            - Attach receipts
            - Show total value per room
            - Export a PDF inventory for an insurance claim
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, PhotosUI, SwiftData, PDFKit
```

---

## Example 109

**Intent:**
language exchange voice notes practice offline

**Spec:**
```
Type:       Mobile application (offline)
Data model: Prompt(id, text, language, level)
            Recording(id, prompt_id -> Prompt, file_path, recorded_at, self_rating)
Features:   - Show speaking prompts by level
            - Record answers as voice notes
            - Play back and compare with a native reference recording
            - Rate fluency on each recording
            - Track minutes spoken per week
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, record, just_audio, sqflite
```

---

## Example 110

**Intent:**
tide times for my beach fishing

**Spec:**
```
Type:       Mobile application
Data model: Station(id, name, lat, lng)
            TideCache(station_id -> Station, date, high_low_json)
Features:   - Find the nearest tide station
            - Show high and low tide times for the next 7 days
            - Draw a tide height curve
            - Save favourite stations
            - Cache tide data for offline use
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, NOAA Tides and Currents API, Room
```

---

## Example 111

**Intent:**
rosary prayer counter

**Spec:**
```
Type:       Mobile application (offline)
Data model: Prayer(id, name, text)
            Session(id, mystery_set, started_at, completed)
Features:   - Guide through each bead with a tap
            - Show the prayer text for each bead
            - Pick the mysteries of the day automatically
            - Vibrate at each decade
            - Track completed rosaries
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 112

**Intent:**
keep track of who borrowed my books and tools

**Spec:**
```
Type:       Mobile application
Data model: Item(id, name, kind, photo_path)
            Loan(id, item_id -> Item, borrower_name, borrower_phone, lent_on, due_on, returned_on)
Features:   - Add items with a photo
            - Record who borrowed an item and when
            - Set a return date and remind
            - Send a friendly reminder text to the borrower
            - Show items currently lent out
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, url_launcher (SMS)
```

---

## Example 113

**Intent:**
practice sight reading notes for piano

**Spec:**
```
Type:       Mobile application (education)
Data model: Exercise(id, clef, note_range, key_signature)
            Result(id, exercise_id -> Exercise, played_at, correct, response_ms)
Features:   - Show a random note on a staff
            - Let the user answer on an on-screen keyboard
            - Listen to a real piano through the microphone with pitch detection
            - Track accuracy and speed per note
            - Increase difficulty as accuracy improves
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, TarsosDSP (pitch detection), Room
```

---

## Example 114

**Intent:**
app for my insulin pump? no, just carb counting for meals

**Spec:**
```
Type:       Mobile application
Data model: Food(id, name, carbs_per_100g, serving_g)
            MealLog(id, eaten_at)
            MealFood(meal_id -> MealLog, food_id -> Food, grams)
Features:   - Search foods for carbohydrate content
            - Build a meal and sum the carbs
            - Calculate an insulin dose suggestion from a carb ratio
            - Save frequent meals
            - Show daily carb totals
Storage:    Bundled food database and logs in on-device SQLite
Tech stack: React Native, expo-sqlite
```

---

## Example 115

**Intent:**
vacation photo map, put all my trip photos on a world map by location

**Spec:**
```
Type:       Mobile application
Data model: PhotoRef(id, asset_id, lat, lng, taken_at, trip_id -> Trip)
            Trip(id, name, start_date, end_date)
Features:   - Read GPS coordinates from photos in the library
            - Cluster photos on a world map
            - Group photos into trips by date
            - Show countries visited
            - Play a slideshow of a trip
Storage:    SwiftData (references to Photos library assets)
Tech stack: Swift, SwiftUI, PhotoKit, MapKit, SwiftData
```

---

## Example 116

**Intent:**
compass and level tool

**Spec:**
```
Type:       Mobile application (offline utility)
Features:   - Show a compass heading from the magnetometer
            - Switch between true and magnetic north
            - Show a bubble level for flat surfaces
            - Calibrate the level to a reference surface
            - Lock the reading on screen
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, SensorManager
```

---

## Example 117

**Intent:**
daily step challenge with my sister, we both use android

**Spec:**
```
Type:       Mobile application with backend
Auth:       Sign in with Google
Data model: User(id, name, avatar)
            Challenge(id, name, start_date, end_date)
            ChallengeMember(challenge_id -> Challenge, user_id -> User)
            DailySteps(user_id -> User, date, steps)
Features:   - Read daily steps from Health Connect
            - Create a challenge and invite by link
            - Upload daily totals and rank members
            - Show a daily and weekly leaderboard
            - Notify when someone overtakes you
Storage:    Firebase Firestore
Tech stack: Kotlin, Jetpack Compose, Health Connect, Firebase Auth, Firestore
```

---

## Example 118

**Intent:**
Plant care app but for succulents specifically, with light and soil notes

**Spec:**
```
Type:       Mobile application
Data model: Succulent(id, name, genus, pot_size_cm, soil_mix, light_level, photo_path)
            CareLog(id, succulent_id -> Succulent, kind, done_on, note)
            Propagation(id, parent_id -> Succulent, method, started_on, rooted_on)
Features:   - Profile each succulent with soil mix and light
            - Suggest watering by season (less in winter dormancy)
            - Log watering, repotting and fertilising
            - Track leaf and cutting propagations
            - Show a photo timeline per plant
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Isar, image_picker
```

---

## Example 119

**Intent:**
memory game for my grandpa with dementia, photos of family

**Spec:**
```
Type:       Mobile game (accessibility)
Data model: FamilyPhoto(id, image_path, name, relation)
            GameResult(id, played_at, pairs, mistakes, duration_s)
Features:   - Build matching card games from family photos
            - Read the person's name aloud on a match
            - Use large cards and simple layouts
            - Adjust difficulty by number of pairs
            - Track results for caregivers
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_tts, sqflite
```

---

## Example 120

**Intent:**
what i spend on my motorcycle trips, fuel and stuff, in kotlin

**Spec:**
```
Type:       Mobile application
Data model: Bike(id, name, tank_l)
            FuelUp(id, bike_id -> Bike, litres, price_total, odometer_km, filled_on, full_tank)
            TripCost(id, trip_name, category, amount, spent_on)
Features:   - Log fuel stops with litres, price and odometer
            - Calculate consumption in L/100 km between full tanks
            - Log other trip costs like tolls and hotels
            - Show cost per km
            - Chart fuel prices over time
Storage:    Room (SQLite) on-device
Tech stack: Kotlin, Jetpack Compose, Room, Vico
```

---

## Example 121

**Intent:**
a reading timer for kids so they read 20 min a day and parents see

**Spec:**
```
Type:       Mobile application
Data model: Child(id, name)
            ReadingLog(id, child_id -> Child, book_title, minutes, read_on)
Features:   - Run a 20-minute reading timer per child
            - Log the book title after each session
            - Show a weekly reading chart for parents
            - Award badges for streaks
            - Export a reading log for school
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, react-native-svg-charts
```

---

## Example 122

**Intent:**
toothbrush timer for my kids so they brush 2 minutes, make it fun

**Spec:**
```
Type:       Mobile application (kids)
Data model: Child(id, name, avatar)
            BrushSession(id, child_id -> Child, brushed_at, duration_s, time_of_day)
Features:   - Run a 2-minute timer split into four 30-second mouth zones
            - Play an animation and music while brushing
            - Award a sticker for each completed session
            - Show a morning and evening chart per child
            - Remind parents if a session is missed
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Rive (animations), audioplayers, Hive
```

---

## Example 123

**Intent:**
contact lens change reminder

**Spec:**
```
Type:       Mobile application
Data model: LensPair(id, brand, type, opened_on, replace_after_days, eye)
            Stock(id, brand, boxes_left)
Features:   - Log when a new pair of lenses is opened
            - Calculate the replacement date for daily, two-week or monthly lenses
            - Notify on the replacement day
            - Track remaining boxes and warn when low
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, UserNotifications, SwiftData
```

---

## Example 124

**Intent:**
remind me to put sunscreen again at the beach based on uv

**Spec:**
```
Type:       Mobile application
Data model: Application(id, applied_at, spf, water_exposure)
            UvReading(id, fetched_at, uv_index)
Features:   - Fetch the current UV index for the user's location
            - Log a sunscreen application with SPF
            - Calculate the reapply time from UV and swimming
            - Notify when it is time to reapply
            - Show today's UV forecast
Storage:    AsyncStorage (on-device)
Tech stack: React Native, expo-location, OpenUV API, Notifee, AsyncStorage
```

---

## Example 125

**Intent:**
20 20 20 eye rule reminder while on phone

**Spec:**
```
Type:       Mobile application (background service)
Data model: BreakLog(id, prompted_at, taken)
Features:   - Detect continuous screen-on time
            - Notify every 20 minutes to look 20 feet away for 20 seconds
            - Show a 20-second countdown overlay
            - Pause reminders while charging or in quiet hours
            - Show breaks taken per day
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Foreground Service, Room
```

---

## Example 126

**Intent:**
ibs food symptom diary low fodmap

**Spec:**
```
Type:       Mobile application
Data model: Food(id, name, fodmap_level, fodmap_groups)
            MealEntry(id, eaten_at, food_ids)
            Symptom(id, occurred_at, bloating, pain, bowel_type)
Features:   - Log meals from a FODMAP-rated food list
            - Log symptoms with the Bristol stool scale
            - Track reintroduction phases per FODMAP group
            - Find foods often eaten before bad symptoms
            - Export a report for a dietitian
Storage:    Drift (SQLite) on-device
Tech stack: Flutter, Drift, pdf
```

---

## Example 127

**Intent:**
I'm pregnant with my first and want an app that shows what week I'm in and lets me count the baby's kicks in the evening

**Spec:**
```
Type:       Mobile application
Data model: Pregnancy(id, due_date, lmp_date)
            KickSession(id, started_at, ended_at, kick_count)
            Appointment(id, scheduled_at, type, notes)
Features:   - Calculate the current pregnancy week from the due date
            - Show what happens in each week
            - Count kicks with a big tap button and time to 10 kicks
            - Keep a list of prenatal appointments
            - Write a weekly bump journal with photos
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 128

**Intent:**
contraction timer

**Spec:**
```
Type:       Mobile application
Data model: Contraction(id, started_at, ended_at, intensity)
Features:   - Start and stop contractions with one button
            - Show duration and interval between contractions
            - Highlight when the 5-1-1 rule is met
            - Share the log with a partner by text
Storage:    On-device (in-memory with SQLite backup)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 129

**Intent:**
breast pump log - how much ml each side and when, and freezer bags with date

**Spec:**
```
Type:       Mobile application
Data model: PumpSession(id, started_at, duration_min, left_ml, right_ml)
            MilkBag(id, session_id -> PumpSession, ml, stored_on, location, used_on)
Features:   - Log pumping sessions per side
            - Show daily total output
            - Label freezer bags with date and amount
            - List bags oldest first and warn before 6 months
            - Mark bags as used
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Notifee
```

---

## Example 130

**Intent:**
my baby was born small and I want to plot her weight and height against the WHO growth curves

**Spec:**
```
Type:       Mobile application
Data model: Child(id, name, sex, birth_date, gestational_weeks)
            Measurement(id, child_id -> Child, measured_on, weight_kg, length_cm, head_cm)
Features:   - Log weight, length and head circumference
            - Plot measurements on WHO growth charts
            - Calculate percentiles for each measurement
            - Correct age for premature birth
            - Export charts as PDF for the paediatrician
Storage:    Bundled WHO growth tables and measurements in on-device SQLite
Tech stack: Flutter, fl_chart, sqflite, pdf
```

---

## Example 131

**Intent:**
weekly meal planner that makes the shopping list for me

**Spec:**
```
Type:       Mobile application
Data model: Recipe(id, name, servings)
            RecipeIngredient(id, recipe_id -> Recipe, name, quantity, unit, aisle)
            PlanSlot(id, date, meal, recipe_id -> Recipe, servings)
            ShoppingItem(id, name, quantity, unit, aisle, checked)
Features:   - Drag recipes into a weekly meal grid
            - Scale recipe servings per slot
            - Generate a shopping list that merges the same ingredients
            - Group the list by supermarket aisle
            - Tick items while shopping
Storage:    Room (SQLite) on-device
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 132

**Intent:**
macro tracker for bodybuilding, protein carbs fat targets per day, and different targets on training days

**Spec:**
```
Type:       Mobile application
Data model: MacroTarget(id, day_type, protein_g, carbs_g, fat_g)
            Food(id, name, barcode, protein_100g, carbs_100g, fat_100g)
            FoodLog(id, food_id -> Food, grams, logged_at)
Features:   - Set separate macro targets for training and rest days
            - Log foods by search or barcode
            - Show remaining protein, carbs and fat as progress rings
            - Copy yesterday's meals
            - Show weekly macro adherence
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, VisionKit, Open Food Facts API, SwiftData
```

---

## Example 133

**Intent:**
freezer inventory, what is in which drawer

**Spec:**
```
Type:       Mobile application
Data model: Drawer(id, name, position)
            FrozenItem(id, drawer_id -> Drawer, name, portions, frozen_on, use_by)
Features:   - Add items to a freezer drawer with portions
            - Show the freezer by drawer
            - Decrease portions when used
            - Sort items by frozen date
            - Remind about items frozen longer than 3 months
Storage:    Hive (on-device)
Tech stack: Flutter, Hive
```

---

## Example 134

**Intent:**
wine cellar inventory with bottle positions in my rack

**Spec:**
```
Type:       Mobile application
Data model: Wine(id, name, producer, vintage, region, grape, drink_from, drink_until, price)
            Bottle(id, wine_id -> Wine, rack, row, col)
            Tasting(id, wine_id -> Wine, tasted_on, score, notes)
Features:   - Add wines and place bottles in a rack grid
            - Show the rack visually with filled slots
            - Show wines in their drinking window
            - Remove a bottle when opened and add tasting notes
            - Show cellar value
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, react-native-svg
```

---

## Example 135

**Intent:**
tea steeping timer with different teas temps and times

**Spec:**
```
Type:       Mobile application (offline)
Data model: Tea(id, name, type, temp_c, steep_s, grams_per_cup, infusions)
Features:   - Pick a tea and start its steeping timer
            - Show the water temperature to use
            - Increase steep time for each re-infusion
            - Notify when steeping is done
            - Add custom teas
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData, UserNotifications
```

---

## Example 136

**Intent:**
sourdough starter feeding schedule and bake log

**Spec:**
```
Type:       Mobile application
Data model: Starter(id, name, flour, hydration_percent)
            Feeding(id, starter_id -> Starter, fed_at, flour_g, water_g, rise_percent)
            Bake(id, starter_id -> Starter, baked_on, recipe, hydration, notes, photo_path, rating)
Features:   - Log starter feedings with ratios
            - Notify when the starter should peak
            - Calculate a bake schedule backwards from a target time
            - Log bakes with photos and ratings
            - Calculate baker's percentages
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, flutter_local_notifications
```

---

## Example 137

**Intent:**
homebrew beer batch log with gravity readings

**Spec:**
```
Type:       Mobile application
Data model: Recipe(id, name, style, og_target, fg_target, ibu)
            Batch(id, recipe_id -> Recipe, brewed_on, volume_l, status)
            GravityReading(id, batch_id -> Batch, read_at, gravity, temp_c)
Features:   - Save beer recipes with targets
            - Start batches from recipes
            - Log gravity readings during fermentation
            - Calculate ABV and attenuation
            - Remind when to dry-hop or bottle
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 138

**Intent:**
cycling computer app that connects to my bluetooth speed and cadence sensor

**Spec:**
```
Type:       Mobile application (Bluetooth sensors)
Data model: Ride(id, started_at, duration_s, distance_m, avg_speed, avg_cadence, avg_hr)
            Sensor(id, name, ble_address, type, wheel_circumference_mm)
Features:   - Pair BLE speed, cadence and heart rate sensors
            - Show live speed, cadence and heart rate
            - Record rides with GPS
            - Calculate distance from wheel revolutions when GPS is weak
            - Export rides as FIT or GPX files
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_reactive_ble, geolocator, Drift
```

---

## Example 139

**Intent:**
heart rate zone training with my chest strap

**Spec:**
```
Type:       Mobile application
Data model: Profile(max_hr, resting_hr)
            Workout(id, started_at, duration_s)
            HrSample(id, workout_id -> Workout, t_s, bpm)
Features:   - Connect a Bluetooth heart rate strap
            - Calculate five heart rate zones from max and resting HR
            - Show the current zone in a large colour block
            - Vibrate when leaving the target zone
            - Show time spent in each zone after the workout
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Core Bluetooth, HealthKit, SwiftData
```

---

## Example 140

**Intent:**
yoga sequence builder for teaching my classes

**Spec:**
```
Type:       Mobile application
Data model: Pose(id, name, sanskrit_name, image_path, category)
            Sequence(id, title, level, duration_min)
            SequencePose(sequence_id -> Sequence, pose_id -> Pose, position, hold_breaths, side)
Features:   - Browse a pose library with images
            - Build sequences by dragging poses
            - Set holds and sides per pose
            - Play a sequence with timed cues
            - Export a sequence as a printable PDF
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-draggable-flatlist, expo-sqlite, expo-print
```

---

## Example 141

**Intent:**
a quiet sitting timer that rings a tibetan bowl sound at start, every 10 min, and at the end

**Spec:**
```
Type:       Mobile application
Data model: Preset(id, name, duration_min, interval_bell_min, bell_sound, warmup_s)
            Sit(id, preset_id -> Preset, sat_at, duration_min)
Features:   - Run a meditation timer with start, interval and end bells
            - Choose bell sounds
            - Save timer presets
            - Log mindful minutes to Apple Health
            - Show total minutes and streaks
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVFoundation, HealthKit, SwiftData
```

---

## Example 142

**Intent:**
hangboard timer for climbing finger training

**Spec:**
```
Type:       Mobile application
Data model: Workout(id, name, hang_s, rest_s, reps, sets, set_rest_s)
            Session(id, workout_id -> Workout, done_on, edge_mm, added_weight_kg)
Features:   - Create hangboard protocols like 7/3 repeaters
            - Run the timer with audio beeps
            - Log edge size and added weight
            - Chart strength progress
            - Remind on training days
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, SoundPool
```

---

## Example 143

**Intent:**
golf scorecard app with gps distance to green

**Spec:**
```
Type:       Mobile application
Data model: Course(id, name)
            Hole(id, course_id -> Course, number, par, green_lat, green_lng)
            Round(id, course_id -> Course, played_on)
            Score(id, round_id -> Round, hole_id -> Hole, strokes, putts, fairway_hit)
Features:   - Download course hole layouts
            - Show GPS distance to the front, middle and back of the green
            - Enter strokes and putts per hole
            - Calculate score to par and stats
            - Show round history and handicap estimate
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, geolocator, sqflite
```

---

## Example 144

**Intent:**
tennis score keeper on my wrist, wear os

**Spec:**
```
Type:       Mobile application (Wear OS)
Data model: Match(id, opponent, started_at, best_of, winner)
            SetScore(id, match_id -> Match, set_number, my_games, their_games, tiebreak)
Features:   - Add a point for me or the opponent with a tap
            - Track games, sets and tiebreaks with tennis rules
            - Undo the last point
            - Sync finished matches to the phone
            - Show match history
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Compose for Wear OS, Wearable Data Layer API, Room
```

---

## Example 145

**Intent:**
darts scorer for 501

**Spec:**
```
Type:       Mobile application (offline)
Data model: Player(id, name)
            Game(id, mode, started_at, winner_id -> Player)
            Turn(id, game_id -> Game, player_id -> Player, dart1, dart2, dart3, total)
Features:   - Score 501 and 301 games with double out
            - Enter darts by tapping a dartboard
            - Suggest checkouts for remaining scores
            - Show averages per player
            - Keep game history
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-svg, expo-sqlite
```

---

## Example 146

**Intent:**
marathon training plan app that adjusts if i miss runs

**Spec:**
```
Type:       Mobile application
Data model: Plan(id, race_date, goal_time, level)
            PlannedRun(id, plan_id -> Plan, date, type, distance_km, pace_target)
            CompletedRun(id, planned_run_id -> PlannedRun, distance_km, duration_s, feeling)
Features:   - Generate a 16-week plan from race date and goal time
            - Show this week's runs
            - Mark runs done with distance and feeling
            - Reschedule the week when a run is missed
            - Show long-run progression
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, HealthKit (import runs), SwiftData
```

---

## Example 147

**Intent:**
sauna and cold plunge log

**Spec:**
```
Type:       Mobile application
Data model: Session(id, kind, started_at, duration_min, temperature_c, heart_rate_avg, note)
Features:   - Time sauna and cold plunge rounds
            - Log temperature and duration per round
            - Read heart rate from the watch
            - Show weekly minutes of heat and cold
            - Show contrast session history
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, HealthKit, SwiftData
```

---

## Example 148

**Intent:**
skincare routine checklist morning and night with which products and if my skin reacts

**Spec:**
```
Type:       Mobile application
Data model: Product(id, name, brand, type, active_ingredient, opened_on, pao_months)
            Routine(id, time_of_day)
            RoutineStep(routine_id -> Routine, product_id -> Product, position)
            SkinLog(id, date, condition, breakouts, photo_path)
Features:   - Build morning and evening routines with products in order
            - Check off steps each day
            - Warn about conflicting actives like retinol and AHA
            - Track product expiry after opening
            - Log skin condition with photos
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, image_picker
```

---

## Example 149

**Intent:**
Hello, my hair is falling and doctor gave me minoxidil. I want take photo same angle every month to see if it works.

**Spec:**
```
Type:       Mobile application
Data model: HairPhoto(id, taken_on, angle, file_path)
            Treatment(id, name, started_on, dose)
Features:   - Show a camera overlay guide to match previous photo angles
            - Save photos by angle (top, front, crown)
            - Compare two dates side by side with a slider
            - Remind monthly to take photos
            - Log treatments and when they started
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, CameraX, Jetpack Compose, Room
```

---

## Example 150

**Intent:**
stop biting nails help

**Spec:**
```
Type:       Mobile application
Data model: Urge(id, occurred_at, resisted, situation)
            Goal(id, days_target, started_on)
Features:   - Log urges and whether they were resisted
            - Tag situations like stress or boredom
            - Show days without biting
            - Suggest a replacement action when logging an urge
            - Show weekly progress
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 151

**Intent:**
debt snowball calculator, I have 5 credit cards and a car loan

**Spec:**
```
Type:       Mobile application
Data model: Debt(id, name, balance, apr, min_payment)
            Payment(id, debt_id -> Debt, amount, paid_on)
            Plan(strategy, extra_monthly)
Features:   - Add debts with balance, APR and minimum payment
            - Order debts by snowball or avalanche strategy
            - Calculate a payoff date and total interest
            - Log payments and update balances
            - Chart remaining debt over time
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Isar, fl_chart
```

---

## Example 152

**Intent:**
net worth tracker monthly

**Spec:**
```
Type:       Mobile application
Data model: Account(id, name, type, currency, is_liability)
            Snapshot(id, account_id -> Account, balance, recorded_on)
Features:   - Add assets and liabilities
            - Enter balances once a month
            - Calculate net worth per month
            - Chart net worth over time
            - Convert foreign currencies to a base currency
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Swift Charts, SwiftData, Frankfurter exchange rate API
```

---

## Example 153

**Intent:**
loan calculator offline, monthly payment and table

**Spec:**
```
Type:       Mobile application (offline)
Data model: SavedLoan(id, name, principal, annual_rate, term_months, start_date)
Features:   - Calculate the monthly payment from amount, rate and term
            - Show a full amortization schedule
            - Show the effect of extra monthly payments
            - Save loans to compare
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 154

**Intent:**
tip calculator and split the bill

**Spec:**
```
Type:       Mobile application (offline)
Features:   - Enter the bill total and tip percentage
            - Split the total between a number of people
            - Round each share up to a whole amount
            - Remember the last used tip percentage
Storage:    DataStore (preferences)
Tech stack: Kotlin, Jetpack Compose, DataStore
```

---

## Example 155

**Intent:**
currency converter that works offline when I travel

**Spec:**
```
Type:       Mobile application (offline-first)
Data model: Rate(base, target, rate, fetched_at)
            FavouritePair(id, from_currency, to_currency)
Features:   - Convert between currencies
            - Download latest rates when online
            - Use cached rates offline and show their age
            - Save favourite currency pairs
            - Show a 30-day rate chart
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Frankfurter API, Hive
```

---

## Example 156

**Intent:**
im freelance graphic designer and i need to track my expenses that are tax deductible, like software and equipment, with the receipt photo

**Spec:**
```
Type:       Mobile application
Data model: Expense(id, description, amount, vat_amount, category, spent_on, receipt_path, deductible_percent)
            Category(id, name, tax_code)
Features:   - Log expenses with receipt photos
            - Set a deductible percentage per expense
            - Total deductible amounts per tax year
            - Show VAT paid per quarter
            - Export a CSV and receipt ZIP for the accountant
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-image-picker, expo-sqlite, jszip
```

---

## Example 157

**Intent:**
pocket money app for kids with a fake bank

**Spec:**
```
Type:       Mobile application (family)
Data model: Kid(id, name, balance)
            Transaction(id, kid_id -> Kid, amount, type, note, created_at)
            Allowance(id, kid_id -> Kid, amount, weekday)
Features:   - Pay weekly allowance automatically
            - Record spending and gifts
            - Pay interest on savings to teach saving
            - Show each child's balance and history
            - Set savings goals per child
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 158

**Intent:**
lego sets i own and which pieces are missing

**Spec:**
```
Type:       Mobile application
Data model: Set(id, set_number, name, year, theme, image_url)
            Part(id, set_id -> Set, part_number, color, quantity_needed, quantity_found)
Features:   - Add sets by set number using the Rebrickable API
            - Load the parts list for each set
            - Mark found and missing pieces
            - Show a list of missing pieces to order
            - Show the collection by theme
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Rebrickable API, Drift
```

---

## Example 159

**Intent:**
pokemon card collection, scan the card and show price

**Spec:**
```
Type:       Mobile application
Data model: Card(id, name, set_name, number, rarity, image_url, market_price)
            OwnedCard(id, card_id -> Card, condition, quantity, binder)
Features:   - Scan a card with the camera and match it
            - Look up card details and prices from the Pokémon TCG API
            - Track quantity and condition
            - Organise cards into binders
            - Show total collection value
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, CameraX, ML Kit Text Recognition, Pokémon TCG API, Room
```

---

## Example 160

**Intent:**
video game backlog

**Spec:**
```
Type:       Mobile application
Data model: Game(id, title, platform, status, hours_played, rating, started_on, finished_on, cover_url)
Features:   - Search games via the IGDB API and add them
            - Set status: backlog, playing, finished, dropped
            - Log hours played
            - Pick a random game from the backlog
            - Show games finished per year
Storage:    Local on-device database (SQLite)
Tech stack: React Native, IGDB API, expo-sqlite
```

---

## Example 161

**Intent:**
Movie diary, everything I watch with stars and where I watched it

**Spec:**
```
Type:       Mobile application
Data model: Film(id, title, year, tmdb_id, poster_url)
            Viewing(id, film_id -> Film, watched_on, rating, place, rewatch, review)
Features:   - Search films with the TMDB API
            - Log viewings with rating and place
            - Mark rewatches
            - Show films watched per month
            - Show top-rated films of the year
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, TMDB API, SwiftData
```

---

## Example 162

**Intent:**
guitar chord and lyrics songbook for when i play at parties

**Spec:**
```
Type:       Mobile application (offline)
Data model: Song(id, title, artist, key, capo, content_chordpro)
            Setlist(id, name)
            SetlistSong(setlist_id -> Setlist, song_id -> Song, position)
Features:   - Store songs in ChordPro format
            - Transpose chords up or down
            - Auto-scroll lyrics at an adjustable speed
            - Build setlists
            - Show chord diagrams on tap
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 163

**Intent:**
tuner for ukulele

**Spec:**
```
Type:       Mobile application (offline utility)
Features:   - Detect pitch from the microphone
            - Show the nearest string and how sharp or flat it is
            - Support standard GCEA and baritone tuning
            - Play a reference tone for each string
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, TarsosDSP
```

---

## Example 164

**Intent:**
ear training app intervals and chords

**Spec:**
```
Type:       Mobile application (education)
Data model: Exercise(id, kind, items)
            Answer(id, exercise_id -> Exercise, asked, answered, correct, answered_at)
Features:   - Play intervals, chords and scales with a piano sound
            - Ask the user to identify what they heard
            - Choose ascending, descending or harmonic intervals
            - Track accuracy per interval
            - Focus practice on weak intervals
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVAudioUnitSampler, SwiftData
```

---

## Example 165

**Intent:**
singing app that shows if im on pitch

**Spec:**
```
Type:       Mobile application
Data model: Exercise(id, name, notes)
            Attempt(id, exercise_id -> Exercise, recorded_at, accuracy_percent)
Features:   - Detect the sung pitch in real time from the microphone
            - Draw the target notes and the user's pitch line
            - Play warm-up scales
            - Score pitch accuracy per exercise
            - Record and play back attempts
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-audio-api, pitchy (pitch detection), expo-sqlite
```

---

## Example 166

**Intent:**
film photography log for my analog camera, which roll, iso, settings each shot

**Spec:**
```
Type:       Mobile application
Data model: Camera(id, name, format)
            Roll(id, camera_id -> Camera, film_stock, iso, loaded_on, developed_on, lab)
            Shot(id, roll_id -> Roll, frame, aperture, shutter, lens, lat, lng, note)
Features:   - Track rolls loaded in each camera
            - Log each frame's aperture, shutter and location
            - Mark rolls as developed with the lab
            - Show settings per frame next to scans
            - Export shot data as CSV
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, geolocator, Drift
```

---

## Example 167

**Intent:**
light meter app for my old camera that has no meter

**Spec:**
```
Type:       Mobile application (photography utility)
Data model: Reading(id, ev, iso, aperture, shutter, taken_at)
Features:   - Measure scene brightness with the camera exposure values
            - Calculate EV for a chosen ISO
            - Suggest shutter speed for a chosen aperture
            - Support spot metering by tapping the preview
            - Calibrate against a known meter
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVFoundation
```

---

## Example 168

**Intent:**
nd filter long exposure calculator

**Spec:**
```
Type:       Mobile application (offline utility)
Features:   - Enter the base shutter speed
            - Choose ND filter strengths like ND8, ND64, ND1000
            - Calculate the long exposure time
            - Start a countdown timer for bulb mode
            - Save favourite filter combinations
Storage:    DataStore (preferences)
Tech stack: Kotlin, Jetpack Compose, DataStore
```

---

## Example 169

**Intent:**
remove location from my photos before i post them

**Spec:**
```
Type:       Mobile application (privacy utility)
Features:   - Pick one or many photos from the gallery
            - Show the EXIF metadata including GPS
            - Strip location and device data from copies
            - Save cleaned copies or share them directly
            - Keep the original photos untouched
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, image (EXIF editing), photo_manager, share_plus
```

---

## Example 170

**Intent:**
find duplicate photos on my phone and delete them

**Spec:**
```
Type:       Mobile application (photo utility)
Data model: PhotoHash(asset_id, phash, size_bytes, taken_at)
            DuplicateGroup(id, asset_ids, kept_asset_id)
Features:   - Scan the photo library and compute perceptual hashes
            - Group exact and near-duplicate photos
            - Suggest the best photo in each group by sharpness
            - Delete selected duplicates in batch
            - Show storage freed
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, PhotoKit, Vision (feature prints), SwiftData
```

---

## Example 171

**Intent:**
QR code scanner and generator without ads

**Spec:**
```
Type:       Mobile application (offline utility)
Data model: ScanHistory(id, content, format, scanned_at)
            Generated(id, content, type, created_at)
Features:   - Scan QR codes and barcodes with the camera
            - Detect URL, Wi-Fi and contact codes and offer actions
            - Generate QR codes for text, links and Wi-Fi
            - Keep a scan history
            - Share generated codes as images
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, CameraX, ML Kit Barcode Scanning, ZXing (generation), Room
```

---

## Example 172

**Intent:**
medical id app with my allergies and blood type for paramedics

**Spec:**
```
Type:       Mobile application (offline)
Data model: MedicalProfile(name, birth_date, blood_type, allergies, conditions, medications, organ_donor)
            EmergencyContact(id, name, phone, relation)
Features:   - Store blood type, allergies, conditions and medications
            - Show the info on a lock screen widget
            - Generate a lock screen wallpaper image with the key info
            - Call emergency contacts from the app
            - Work without internet
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, home_widget, Hive
```

---

## Example 173

**Intent:**
sos button that sends my location to my family if something happens when i walk home at night

**Spec:**
```
Type:       Mobile application
Data model: Contact(id, name, phone)
            Alert(id, sent_at, lat, lng, delivered)
Features:   - Trigger an SOS with a long press or pressing power button 5 times
            - Send an SMS with a live location link to chosen contacts
            - Start a "walk me home" timer that alerts if not cancelled
            - Record audio when SOS is active
            - Log sent alerts
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, SmsManager, Fused Location Provider, Room
```

---

## Example 174

**Intent:**
fall detection for my mom on her apple watch, call me if she falls

**Spec:**
```
Type:       Mobile application (watchOS companion)
Data model: Caregiver(id, name, phone)
            FallEvent(id, detected_at, lat, lng, confirmed, alert_sent)
Features:   - Detect hard falls with the watch motion sensors
            - Ask on the watch if she is OK with a countdown
            - Call and text caregivers if there is no response
            - Include her location in the alert
            - Keep a log of fall events
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, CoreMotion (CMFallDetectionManager), CallKit, MessageUI
```

---

## Example 175

**Intent:**
turn my phone into a hearing amplifier with my earbuds

**Spec:**
```
Type:       Mobile application (accessibility)
Data model: Profile(id, name, gain_db, eq_bands, noise_reduction)
Features:   - Stream the microphone to wired or Bluetooth earbuds with low latency
            - Adjust volume and frequency equaliser
            - Reduce background noise
            - Save profiles for places like restaurant or TV
            - Show a large on-off button
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Oboe (low-latency audio), Room
```

---

## Example 176

**Intent:**
help for color blind, point camera and it tells the color

**Spec:**
```
Type:       Mobile application (accessibility)
Features:   - Show the live camera with a centre crosshair
            - Name the colour under the crosshair
            - Read the colour name aloud with VoiceOver
            - Highlight a chosen colour in the image
            - Freeze the frame to inspect
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVFoundation, Core Image
```

---

## Example 177

**Intent:**
My cousin's son is autistic and nonverbal. They want a tablet app with picture buttons he can press and it speaks the word, and the parents can add their own photos.

**Spec:**
```
Type:       Mobile application (AAC, accessibility)
Data model: Board(id, name, grid_size)
            Symbol(id, board_id -> Board, label, image_path, audio_path, position, color)
            UsageLog(id, symbol_id -> Symbol, pressed_at)
Features:   - Show a grid of picture buttons on a board
            - Speak the label with text-to-speech or a recorded voice
            - Build sentences from several buttons
            - Let parents add symbols with their own photos behind a lock
            - Show which symbols are used most
Storage:    Local on-device database (SQLite)
Tech stack: Flutter (tablet layout), flutter_tts, image_picker, Drift
```

---

## Example 178

**Intent:**
visual schedule for autistic kid, pictures of morning routine steps

**Spec:**
```
Type:       Mobile application
Data model: Routine(id, name, time_of_day)
            Step(id, routine_id -> Routine, label, image_path, position, minutes)
Features:   - Build routines from picture steps
            - Show the current step large with a visual timer
            - Tick off steps with a satisfying animation
            - Show what comes next
            - Let parents edit routines behind a PIN
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-reanimated, expo-sqlite
```

---

## Example 179

**Intent:**
something for my adhd where i put a big task and it breaks it in small steps and i do one at a time

**Spec:**
```
Type:       Mobile application
Data model: Task(id, title, created_at, done)
            Step(id, task_id -> Task, text, position, estimate_min, done_at)
Features:   - Enter a big task and split it into small steps
            - Suggest steps with an on-device language model
            - Show only the current step in focus mode
            - Run a short timer per step
            - Celebrate each finished step
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Apple Foundation Models framework, SwiftData
```

---

## Example 180

**Intent:**
my dog has diabetes and needs insulin twice a day with food, help me not forget and log it

**Spec:**
```
Type:       Mobile application
Data model: Pet(id, name, weight_kg)
            InsulinShot(id, pet_id -> Pet, units, given_at, given_by, site)
            Feeding(id, pet_id -> Pet, eaten_percent, fed_at)
            GlucoseCurve(id, pet_id -> Pet, measured_at, value)
Features:   - Remind at feeding and injection times
            - Log shots with units and injection site
            - Log how much food was eaten
            - Warn if a shot was already logged to avoid double dosing
            - Show glucose curve readings
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, flutter_local_notifications
```

---

## Example 181

**Intent:**
horse riding log

**Spec:**
```
Type:       Mobile application
Data model: Horse(id, name, breed, age)
            Ride(id, horse_id -> Horse, ridden_on, duration_min, discipline, gaits, notes)
            Farrier(id, horse_id -> Horse, visited_on, cost)
Features:   - Log rides with duration and discipline
            - Track walk, trot and canter time with GPS speed
            - Record farrier and vet visits
            - Remind when the farrier is due
            - Show riding time per horse
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Fused Location Provider, Room
```

---

## Example 182

**Intent:**
how many eggs my chickens lay every day

**Spec:**
```
Type:       Mobile application
Data model: Hen(id, name, breed, hatched_on)
            EggLog(id, date, count, hen_id -> Hen)
            FeedPurchase(id, bought_on, kg, cost)
Features:   - Log daily egg counts, optionally per hen
            - Show weekly and monthly production
            - Log feed purchases
            - Calculate cost per egg
            - Track egg sales
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Victory Native
```

---

## Example 183

**Intent:**
beekeeping hive inspection notes

**Spec:**
```
Type:       Mobile application
Data model: Apiary(id, name, lat, lng)
            Hive(id, apiary_id -> Apiary, name, queen_year, queen_marked)
            Inspection(id, hive_id -> Hive, inspected_on, temper, brood_frames, queen_seen, varroa_count, notes)
            Harvest(id, hive_id -> Hive, harvested_on, kg)
Features:   - Record inspections with brood frames and queen sightings
            - Log varroa counts and treatments
            - Track honey harvests per hive
            - Remind about the next inspection
            - Use large controls usable with gloves
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, geolocator
```

---

## Example 184

**Intent:**
reptile feeding and shedding log, i have 2 geckos and a ball python

**Spec:**
```
Type:       Mobile application
Data model: Reptile(id, name, species, morph, hatched_on)
            Feeding(id, reptile_id -> Reptile, prey, prey_size, fed_on, refused)
            Shed(id, reptile_id -> Reptile, shed_on, complete)
            Weight(id, reptile_id -> Reptile, grams, weighed_on)
Features:   - Log feedings including refused meals
            - Log sheds and whether they were complete
            - Track weight over time
            - Remind when the next feeding is due per animal
            - Show feeding history per reptile
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 185

**Intent:**
dog training clicker and progress for each trick

**Spec:**
```
Type:       Mobile application
Data model: Dog(id, name)
            Command(id, name, stage)
            TrainingSession(id, dog_id -> Dog, command_id -> Command, trained_on, reps, success_rate)
Features:   - Play a clicker sound with a big button
            - Track commands through stages like lure, cue and proofing
            - Log short sessions with success rate
            - Suggest which command to practise next
            - Show progress per dog
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-av, expo-sqlite
```

---

## Example 186

**Intent:**
puppy potty training log so we can see the pattern

**Spec:**
```
Type:       Mobile application
Data model: Event(id, kind, location, occurred_at, logged_by)
Features:   - Log pee, poo, meal, nap and play events with one tap
            - Mark accidents inside vs success outside
            - Predict the next likely potty time
            - Remind to take the puppy out
            - Show success rate per week
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Hive, flutter_local_notifications
```

---

## Example 187

**Intent:**
bonsai care diary

**Spec:**
```
Type:       Mobile application
Data model: Tree(id, name, species, style, acquired_on, photo_path)
            Task(id, tree_id -> Tree, kind, done_on, notes)
Features:   - Profile each tree with species and style
            - Log pruning, wiring, repotting and fertilising
            - Remind to remove wire before it bites
            - Show a seasonal care calendar per species
            - Keep a photo timeline per tree
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 188

**Intent:**
mushroom foraging journal with gps but private

**Spec:**
```
Type:       Mobile application (offline, privacy-focused)
Data model: Find(id, species_guess, confidence, found_on, lat, lng, habitat, substrate, photo_path, notes)
Features:   - Log finds with photos, habitat and substrate
            - Save GPS locations stored only on the device
            - Show finds on an offline map
            - Show which months each spot produced
            - Warn that identification needs expert confirmation
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, MapLibre Native (offline tiles), Room
```

---

## Example 189

**Intent:**
seed packet inventory so i know what seeds i have and how old

**Spec:**
```
Type:       Mobile application
Data model: SeedPacket(id, crop, variety, supplier, packed_year, quantity, germination_rate, photo_path)
            GerminationTest(id, packet_id -> SeedPacket, tested_on, seeds_tested, seeds_sprouted)
Features:   - Scan seed packets with a photo
            - Track variety, supplier and pack year
            - Warn when seeds are past their viability
            - Log germination tests
            - Filter seeds by sowing month
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, image_picker, Drift
```

---

## Example 190

**Intent:**
compost pile temp log

**Spec:**
```
Type:       Mobile application
Data model: Pile(id, name, started_on)
            Reading(id, pile_id -> Pile, temp_c, moisture, read_on)
            Turn(id, pile_id -> Pile, turned_on)
Features:   - Log compost temperatures
            - Chart temperature to see hot phases
            - Remind to turn the pile when temperature drops
            - Log materials added
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 191

**Intent:**
lawn care schedule - mow, feed, weed, by season

**Spec:**
```
Type:       Mobile application
Data model: Lawn(id, name, area_m2, grass_type)
            LawnTask(id, lawn_id -> Lawn, kind, product, done_on, next_due)
Features:   - Generate a seasonal schedule by grass type
            - Log mowing with cutting height
            - Calculate fertiliser amount by lawn area
            - Remind before tasks are due
            - Skip mowing reminders on rainy days using a weather API
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, OpenWeatherMap API
```

---

## Example 192

**Intent:**
hydroponic garden ph and ec log

**Spec:**
```
Type:       Mobile application
Data model: System(id, name, type, reservoir_l)
            Measurement(id, system_id -> System, ph, ec, water_temp_c, measured_at)
            NutrientDose(id, system_id -> System, nutrient, ml, dosed_at)
Features:   - Log pH, EC and water temperature
            - Highlight readings outside the crop's range
            - Calculate nutrient doses for the reservoir size
            - Remind to change the reservoir
            - Chart readings over time
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, fl_chart
```

---

## Example 193

**Intent:**
weather based packing list, it looks at the forecast where im going and tells me what clothes

**Spec:**
```
Type:       Mobile application
Data model: Trip(id, destination, lat, lng, start_date, end_date)
            PackItem(id, trip_id -> Trip, name, quantity, reason, packed)
Features:   - Fetch the forecast for the destination and dates
            - Generate clothing suggestions from temperature and rain
            - Add trip-type items like beach or business
            - Check off items as packed
            - Save the list for offline use
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, WeatherKit, SwiftData
```

---

## Example 194

**Intent:**
Is it possible to have app that store my passport, visa and insurance documents and tell me before they expire? I travel a lot for work.

**Spec:**
```
Type:       Mobile application
Data model: Document(id, type, holder_name, number, issued_on, expires_on, country, file_path)
            Reminder(id, document_id -> Document, days_before)
Features:   - Scan documents with the camera
            - Store expiry dates and numbers
            - Notify 6 months and 1 month before expiry
            - Lock documents behind Face ID
            - Keep encrypted copies available offline
Storage:    Encrypted on-device storage (Keychain key, encrypted files)
Tech stack: Swift, SwiftUI, VisionKit, LocalAuthentication, CryptoKit
```

---

## Example 195

**Intent:**
jet lag planner

**Spec:**
```
Type:       Mobile application
Data model: Flight(id, from_tz, to_tz, departs_at, arrives_at)
            PlanStep(id, flight_id -> Flight, at, action)
Features:   - Enter a flight with departure and arrival time zones
            - Generate a schedule for light exposure, sleep and caffeine
            - Shift bedtime gradually before departure
            - Notify each step
            - Show the plan as a timeline
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, timezone, flutter_local_notifications, Hive
```

---

## Example 196

**Intent:**
scratch map countries ive been

**Spec:**
```
Type:       Mobile application
Data model: Country(code, name, continent)
            Visit(id, country_code, first_visited_on, notes)
Features:   - Tap countries on a world map to mark them visited
            - Show percentage of the world and per continent
            - Add a first-visit date and notes
            - Share a map image
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-svg (world map), expo-sqlite
```

---

## Example 197

**Intent:**
camping trip checklist and log of the campsites we liked

**Spec:**
```
Type:       Mobile application
Data model: Campsite(id, name, lat, lng, rating, has_water, has_toilets, notes)
            Trip(id, campsite_id -> Campsite, start_date, nights)
            GearItem(id, name, category)
            TripGear(trip_id -> Trip, gear_id -> GearItem, packed)
Features:   - Keep a reusable gear list by category
            - Make a checklist per trip from the gear list
            - Log campsites with amenities and rating
            - Show campsites on a map
            - Note what to bring next time
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Google Maps SDK, Room
```

---

## Example 198

**Intent:**
offline phrasebook spanish with audio

**Spec:**
```
Type:       Mobile application (offline)
Data model: Phrase(id, category, english, spanish, phonetic, audio_path)
            Favourite(phrase_id -> Phrase)
Features:   - Browse phrases by category like food, directions and emergencies
            - Play native audio for each phrase
            - Show a large-text mode to show to locals
            - Search phrases
            - Save favourites
Storage:    Bundled phrases and audio files in app assets, SQLite index
Tech stack: Flutter, just_audio, sqflite
```

---

## Example 199

**Intent:**
travel journal with a page per day, photos and the places we went

**Spec:**
```
Type:       Mobile application
Data model: Journey(id, title, start_date, end_date, cover_path)
            DayPage(id, journey_id -> Journey, date, text, weather)
            Place(id, day_id -> DayPage, name, lat, lng)
            Photo(id, day_id -> DayPage, asset_id)
Features:   - Create a page per travel day
            - Add photos and places visited
            - Show the route of each day on a map
            - Fill in the weather automatically
            - Export the journey as a PDF book
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, MapKit, PhotoKit, SwiftData, PDFKit
```

---

## Example 200

**Intent:**
flight log, all the flights i took with airline, airport, distance

**Spec:**
```
Type:       Mobile application
Data model: Airport(iata, name, lat, lng)
            Flight(id, flight_no, airline, from_iata, to_iata, flown_on, seat, aircraft)
Features:   - Add flights by flight number and date
            - Calculate great-circle distance
            - Draw flown routes on a world map
            - Show totals for distance, flights and airports
            - Import flights from a boarding pass barcode
Storage:    Bundled airport database, flights in on-device SQLite
Tech stack: Kotlin, Jetpack Compose, ML Kit Barcode Scanning (PDF417), Room
```

---

## Example 201

**Intent:**
scuba dive log

**Spec:**
```
Type:       Mobile application
Data model: Dive(id, number, site, dived_on, max_depth_m, bottom_time_min, water_temp_c, visibility_m, buddy)
            Equipment(id, name, type, serviced_on)
            DiveEquipment(dive_id -> Dive, equipment_id -> Equipment)
Features:   - Log dives with depth, time and conditions
            - Import dive profiles from a Bluetooth dive computer
            - Draw the depth profile chart
            - Track equipment and service dates
            - Show totals and certifications
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Core Bluetooth, Swift Charts, SwiftData
```

---

## Example 202

**Intent:**
ski days counter with resort and vertical meters

**Spec:**
```
Type:       Mobile application
Data model: Resort(id, name, country)
            SkiDay(id, resort_id -> Resort, date, vertical_m, runs, top_speed_kmh, snow)
Features:   - Track runs and vertical with GPS and altitude
            - Detect lifts vs descents automatically
            - Log days per resort
            - Show season totals
            - Save battery with a low-power tracking mode
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, geolocator, sensors_plus (barometer), Drift
```

---

## Example 203

**Intent:**
surf sessions log with the swell that day

**Spec:**
```
Type:       Mobile application
Data model: Spot(id, name, lat, lng)
            Session(id, spot_id -> Spot, started_at, duration_min, waves_caught, board, rating)
            SwellSnapshot(id, session_id -> Session, height_m, period_s, direction_deg, wind_kmh)
Features:   - Log surf sessions with board and rating
            - Fetch swell and wind data for the spot and time
            - Find conditions that gave the best sessions
            - Show session history per spot
            - Show a quiver of boards
Storage:    Local on-device database (SQLite)
Tech stack: React Native, Open-Meteo Marine API, expo-sqlite
```

---

## Example 204

**Intent:**
star gazing log what i saw with my telescope

**Spec:**
```
Type:       Mobile application
Data model: Object(id, name, type, catalog_id, ra, dec)
            Observation(id, object_id -> Object, observed_at, instrument, eyepiece, seeing, notes, sketch_path)
Features:   - Search Messier, NGC and planet objects
            - Log observations with instrument and seeing
            - Draw sketches of the view
            - Show what is visible tonight from the user's location
            - Use a red night-vision display mode
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 205

**Intent:**
family calendar for the kids activities, football, piano, who drives

**Spec:**
```
Type:       Mobile application with backend
Auth:       Family group with invite link; sign in with Apple or Google
Data model: Family(id, name)
            Member(id, family_id -> Family, name, role, color)
            Activity(id, family_id -> Family, title, child_id -> Member, starts_at, ends_at, recurrence, location)
            DriverAssignment(activity_id -> Activity, driver_id -> Member)
Features:   - Add recurring activities per child
            - Assign who drives to and from each activity
            - Show a colour-coded week view
            - Notify drivers before pickups
            - Sync between all family members' phones
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase Auth, Firestore, Firebase Cloud Messaging
```

---

## Example 206

**Intent:**
school lunchbox ideas and what my kids actually ate

**Spec:**
```
Type:       Mobile application
Data model: Kid(id, name, dislikes)
            LunchItem(id, name, category)
            Lunch(id, kid_id -> Kid, date)
            LunchContent(lunch_id -> Lunch, item_id -> LunchItem, eaten)
Features:   - Plan lunchboxes for the week per child
            - Suggest combos from fruit, main and snack
            - Mark which items came back uneaten
            - Avoid items a child keeps leaving
            - Create a shopping list for the week
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 207

**Intent:**
carpool rota between 4 families for school

**Spec:**
```
Type:       Mobile application with backend
Auth:       Phone number sign-in with SMS code
Data model: Family(id, name, seats)
            Carpool(id, name)
            Run(id, carpool_id -> Carpool, date, direction, driver_family_id -> Family)
            SwapRequest(id, run_id -> Run, from_family -> Family, status)
Features:   - Generate a fair driving rota
            - Show who drives each day
            - Request and accept swaps
            - Notify the driver the evening before
            - Count runs per family
Storage:    Supabase Postgres
Tech stack: React Native, Supabase
```

---

## Example 208

**Intent:**
family tree app

**Spec:**
```
Type:       Mobile application
Data model: Person(id, first_name, last_name, birth_date, death_date, birth_place, photo_path, notes)
            Relationship(id, person_a -> Person, person_b -> Person, kind)
Features:   - Add people with dates and photos
            - Link parents, children and spouses
            - Draw an interactive tree view
            - Import and export GEDCOM files
            - Search people by name
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, graphview, Drift
```

---

## Example 209

**Intent:**
me and my 2 brothers take care of our dad who has alzheimers, we want one place to log his meds, mood, appointments, and who visited

**Spec:**
```
Type:       Mobile application with backend
Auth:       Shared care circle via email invite
Data model: CareRecipient(id, name)
            Caregiver(id, name, email)
            Note(id, author_id -> Caregiver, kind, text, created_at)
            Appointment(id, title, at, assigned_to -> Caregiver)
            MedDose(id, medication, given_at, given_by -> Caregiver)
Features:   - Log visits, mood and incidents in a shared feed
            - Record medication given and by whom
            - Schedule appointments and assign a sibling
            - Notify the circle about important notes
            - Show a weekly summary
Storage:    Firebase Firestore
Tech stack: Kotlin, Jetpack Compose, Firebase Auth, Firestore, FCM
```

---

## Example 210

**Intent:**
babysitter info app - allergies, bedtimes, emergency numbers, all in one link

**Spec:**
```
Type:       Mobile application
Data model: Child(id, name, allergies, bedtime, routines)
            HouseInfo(wifi, alarm_code_hint, rules)
            Contact(id, name, phone, role)
Features:   - Store each child's routines, allergies and bedtime
            - Store emergency contacts and house info
            - Generate a shareable PDF or QR code for the sitter
            - Call contacts with one tap
            - Hide sensitive info until a PIN is entered
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-print, react-native-qrcode-svg, expo-sqlite
```

---

## Example 211

**Intent:**
wedding budget planner

**Spec:**
```
Type:       Mobile application
Data model: Category(id, name, budget)
            Vendor(id, category_id -> Category, name, contact, quoted, paid, deposit_due)
            Payment(id, vendor_id -> Vendor, amount, paid_on)
Features:   - Set a total budget split by category
            - Add vendors with quotes
            - Track deposits and payments
            - Remind about payment due dates
            - Show spent vs budget per category
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, fl_chart
```

---

## Example 212

**Intent:**
moving house checklist with boxes and whats in them

**Spec:**
```
Type:       Mobile application
Data model: Box(id, number, room, contents, fragile, qr_code)
            Task(id, title, due_on, done)
Features:   - Number boxes and list contents per box
            - Print QR labels for boxes
            - Scan a box label to see its contents
            - Search which box has an item
            - Follow a moving checklist with due dates
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, ML Kit Barcode Scanning, Room
```

---

## Example 213

**Intent:**
home maintenance reminders like change furnace filter, clean gutters

**Spec:**
```
Type:       Mobile application
Data model: Task(id, title, interval_months, season, last_done, next_due, notes)
            Log(id, task_id -> Task, done_on, cost)
Features:   - Start from a template of common home tasks
            - Set intervals per task
            - Notify when tasks are due
            - Log when tasks are done with cost
            - Show the year's maintenance calendar
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData, UserNotifications
```

---

## Example 214

**Intent:**
leftovers tracker, what is in fridge from when

**Spec:**
```
Type:       Mobile application
Data model: Leftover(id, name, cooked_on, container, eat_by, eaten)
Features:   - Add leftovers with a cooked date
            - Set eat-by days by food type
            - Show the fridge list ordered by urgency
            - Notify on the eat-by day
            - Track food thrown away per month
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Notifee
```

---

## Example 215

**Intent:**
keto app track ketones and net carbs

**Spec:**
```
Type:       Mobile application
Data model: KetoneReading(id, value_mmol, method, measured_at)
            FoodEntry(id, name, net_carbs_g, fat_g, protein_g, eaten_at)
Features:   - Log blood or breath ketone readings
            - Log food with net carbs
            - Show daily net carbs against a 20 g limit
            - Chart ketones over time
            - Show days in ketosis
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 216

**Intent:**
companion for my freestyle libre CGM to see glucose and add notes

**Spec:**
```
Type:       Mobile application (health)
Data model: GlucoseSample(id, mmol, measured_at, trend)
            Note(id, at, kind, text)
Features:   - Read glucose data from Apple Health written by the CGM app
            - Show a 24-hour glucose graph with target range
            - Add meal, exercise and insulin notes on the timeline
            - Calculate time in range
            - Alert on high or low readings
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, HealthKit, Swift Charts, SwiftData
```

---

## Example 217

**Intent:**
asthma peak flow diary and inhaler use

**Spec:**
```
Type:       Mobile application
Data model: PeakFlow(id, value_lpm, measured_at, best_of_three)
            InhalerUse(id, inhaler, puffs, used_at, reason)
            Profile(personal_best_lpm)
Features:   - Log peak flow readings morning and evening
            - Show green, yellow and red zones from personal best
            - Log reliever inhaler puffs
            - Warn when reliever use is high in a week
            - Export a diary for the asthma nurse
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, fl_chart, pdf
```

---

## Example 218

**Intent:**
My physio gave me knee exercises with sets and reps and i always forget which ones, i want app with the list and tick them each day

**Spec:**
```
Type:       Mobile application
Data model: Exercise(id, name, sets, reps, hold_s, instructions, video_path)
            DailyCompletion(id, exercise_id -> Exercise, date, sets_done, pain_level)
Features:   - Enter exercises from the physio with sets, reps and holds
            - Show today's checklist
            - Run a hold timer for each rep
            - Rate pain after exercises
            - Show adherence for the physio appointment
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, expo-av
```

---

## Example 219

**Intent:**
measure my knee bend angle with the phone after surgery

**Spec:**
```
Type:       Mobile application (health sensing)
Data model: AngleMeasurement(id, joint, flexion_deg, extension_deg, measured_on)
Features:   - Strap the phone to the shin and measure flexion with the gyroscope
            - Calibrate zero with the leg straight
            - Record maximum flexion and extension
            - Chart range of motion over recovery
            - Set target angles from the surgeon
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, SensorManager (rotation vector), Room
```

---

## Example 220

**Intent:**
chronic pain journal, where it hurts on a body map

**Spec:**
```
Type:       Mobile application
Data model: PainEntry(id, recorded_at, intensity, type, triggers, medication)
            PainLocation(id, entry_id -> PainEntry, body_region, side)
Features:   - Tap pain locations on a front and back body map
            - Rate intensity and type like burning or stabbing
            - Log medication and triggers
            - Show a heatmap of where pain occurs
            - Export a report for the doctor
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData, PDFKit
```

---

## Example 221

**Intent:**
CBT thought record app

**Spec:**
```
Type:       Mobile application
Data model: ThoughtRecord(id, created_at, situation, automatic_thought, emotion, intensity_before, evidence_for, evidence_against, balanced_thought, intensity_after)
            Distortion(id, name)
            RecordDistortion(record_id -> ThoughtRecord, distortion_id -> Distortion)
Features:   - Guide the user through a thought record step by step
            - Tag cognitive distortions
            - Rate emotion intensity before and after
            - Review past records
            - Lock the app with a PIN
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, local_auth
```

---

## Example 222

**Intent:**
panic attack sos screen

**Spec:**
```
Type:       Mobile application (offline)
Data model: Episode(id, started_at, duration_min, intensity, what_helped)
Features:   - Open a calming screen with one tap from a widget
            - Guide grounding with the 5-4-3-2-1 technique
            - Run paced breathing with haptics
            - Play a saved voice message from a trusted person
            - Log episodes afterwards
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Glance (widget), Room
```

---

## Example 223

**Intent:**
white noise app for sleeping, mix rain and fan sounds

**Spec:**
```
Type:       Mobile application (offline)
Data model: Sound(id, name, file_path)
            Mix(id, name)
            MixSound(mix_id -> Mix, sound_id -> Sound, volume)
Features:   - Play looping sounds like rain, fan and waves
            - Mix several sounds with separate volumes
            - Set a sleep timer with fade out
            - Save favourite mixes
            - Keep playing in the background
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVAudioEngine, SwiftData
```

---

## Example 224

**Intent:**
alarm that wakes me in light sleep phase

**Spec:**
```
Type:       Mobile application
Data model: Alarm(id, wake_by, window_min, sound)
            Night(id, started_at, ended_at, woke_at)
            MotionSample(id, night_id -> Night, t, activity)
Features:   - Set a wake-up window like 6:30 to 7:00
            - Track movement in bed with the accelerometer
            - Detect light sleep from movement
            - Ring the alarm at the lightest moment in the window
            - Show a night movement graph
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Foreground Service, SensorManager, Room
```

---

## Example 225

**Intent:**
record my snoring at night

**Spec:**
```
Type:       Mobile application
Data model: Night(id, started_at, ended_at, snore_minutes)
            SnoreClip(id, night_id -> Night, at, duration_s, loudness_db, file_path)
Features:   - Record during the night and save only loud segments
            - Detect snoring with an on-device sound classifier
            - Show snoring minutes per night
            - Play back clips
            - Tag remedies tried and compare nights
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVAudioRecorder, SoundAnalysis, SwiftData
```

---

## Example 226

**Intent:**
power nap timer 20 min

**Spec:**
```
Type:       Mobile application (offline)
Features:   - Start a nap timer with presets of 10, 20 and 30 minutes
            - Add time to fall asleep before the countdown
            - Wake gently with rising volume
            - Enable Do Not Disturb during the nap
Storage:    SharedPreferences (last used preset)
Tech stack: Kotlin, Jetpack Compose, AlarmManager
```

---

## Example 227

**Intent:**
kids height marks on the door but in an app

**Spec:**
```
Type:       Mobile application
Data model: Child(id, name, birth_date)
            HeightMark(id, child_id -> Child, height_cm, measured_on, photo_path)
Features:   - Record heights per child
            - Draw a growth chart
            - Show a virtual door with dated marks
            - Calculate growth per year
            - Add a photo for each measurement
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, CustomPainter
```

---

## Example 228

**Intent:**
teen learner driver log hours day night

**Spec:**
```
Type:       Mobile application
Data model: Learner(id, name, permit_date, required_hours, required_night_hours)
            Drive(id, learner_id -> Learner, started_at, ended_at, is_night, supervisor, conditions, distance_km)
Features:   - Time drives with GPS distance
            - Mark day and night driving automatically by sunset time
            - Log supervisor and conditions
            - Show hours toward state requirements
            - Export a log sheet as PDF
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-location, expo-sqlite, expo-print
```

---

## Example 229

**Intent:**
bucket list app

**Spec:**
```
Type:       Mobile application
Data model: Goal(id, title, category, target_year, done_on, photo_path, story)
Features:   - Add life goals with category and target year
            - Mark goals done with a photo and story
            - Show progress per category
            - Show a random goal for inspiration
            - Share completed goals
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 230

**Intent:**
a place to save quotes from books with the page

**Spec:**
```
Type:       Mobile application
Data model: Book(id, title, author)
            Quote(id, book_id -> Book, text, page, tags, saved_at)
Features:   - Capture a quote by photographing the page and selecting text
            - Link quotes to books and pages
            - Tag and search quotes
            - Show a daily random quote widget
            - Export quotes as Markdown
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, ML Kit Text Recognition, Glance, Room
```

---

## Example 231

**Intent:**
times tables game for my daughter grade 3

**Spec:**
```
Type:       Mobile game (education)
Data model: Fact(a, b, mastery)
            Round(id, played_at, score, duration_s)
Features:   - Ask multiplication facts in timed rounds
            - Give more practice on facts answered wrong
            - Reward stars and unlock characters
            - Show which tables are mastered
            - Read questions aloud
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Flame, Hive
```

---

## Example 232

**Intent:**
spelling words practice for weekly school test

**Spec:**
```
Type:       Mobile application
Data model: WordList(id, week_of, name)
            Word(id, list_id -> WordList, word, audio_path)
            Attempt(id, word_id -> Word, typed, correct, attempted_at)
Features:   - Enter or photograph the weekly spelling list
            - Read each word aloud and let the child type it
            - Record a parent's voice for each word
            - Repeat wrong words
            - Show a score per test
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVSpeechSynthesizer, VisionKit, SwiftData
```

---

## Example 233

**Intent:**
periodic table app offline for chemistry class

**Spec:**
```
Type:       Mobile application (offline, education)
Data model: Element(atomic_number, symbol, name, mass, group, period, category, electron_config, description)
Features:   - Show an interactive periodic table colour-coded by category
            - Show element details on tap
            - Search by name or symbol
            - Quiz element symbols
            - Calculate molar mass of a formula
Storage:    Bundled element data (JSON) loaded into memory
Tech stack: React Native, react-native-svg
```

---

## Example 234

**Intent:**
anatomy flashcards for med school with images where i have to label

**Spec:**
```
Type:       Mobile application
Data model: Image(id, title, system, file_path)
            Label(id, image_id -> Image, name, x, y)
            Review(id, label_id -> Label, reviewed_at, correct, due_on)
Features:   - Import anatomy images and place labels
            - Hide labels and quiz by tapping locations
            - Quiz by naming a highlighted structure
            - Schedule reviews per label with spaced repetition
            - Filter by body system
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, photo_view, Drift
```

---

## Example 235

**Intent:**
exam countdown that makes a study plan till the exam

**Spec:**
```
Type:       Mobile application
Data model: Exam(id, subject, date, topics_count)
            Topic(id, exam_id -> Exam, name, done)
            StudyBlock(id, topic_id -> Topic, date, minutes, completed)
Features:   - Add exams with dates and topics
            - Spread topics across the remaining days
            - Show today's study blocks
            - Re-plan when blocks are missed
            - Show days left per exam
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, WorkManager
```

---

## Example 236

**Intent:**
record lectures and put bookmarks when prof says important stuff

**Spec:**
```
Type:       Mobile application
Data model: Lecture(id, course, title, recorded_at, file_path, duration_s)
            Bookmark(id, lecture_id -> Lecture, at_s, label)
Features:   - Record lecture audio in the background
            - Tap to add a bookmark at the current time
            - Jump to bookmarks when playing back
            - Transcribe recordings on-device
            - Search transcripts
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVAudioRecorder, Speech framework, SwiftData
```

---

## Example 237

**Intent:**
menopause symptom tracker hot flashes sleep mood

**Spec:**
```
Type:       Mobile application
Data model: Symptom(id, name)
            DailyLog(id, date, hot_flashes, night_sweats, sleep_quality, mood, notes)
            DailySymptom(log_id -> DailyLog, symptom_id -> Symptom, severity)
            Treatment(id, name, started_on, stopped_on)
Features:   - Log hot flashes with a quick tap counter
            - Rate daily symptoms like sleep, mood and joint pain
            - Track HRT and other treatments
            - Chart symptoms before and after starting a treatment
            - Export a summary for the GP
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, fl_chart
```

---

## Example 238

**Intent:**
i have hashimotos, i want to save all my blood test results TSH T4 etc and see a graph over the years

**Spec:**
```
Type:       Mobile application
Data model: LabTest(id, name, unit, ref_low, ref_high)
            LabResult(id, test_id -> LabTest, value, taken_on, lab_name, report_path)
            Medication(id, name, dose_mcg, started_on)
Features:   - Enter lab results with units and reference ranges
            - Photograph lab reports and extract values with OCR
            - Flag results outside the reference range
            - Chart each test over time with dose changes marked
            - Export results as PDF
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Vision (text recognition), Swift Charts, SwiftData
```

---

## Example 239

**Intent:**
family vaccination records

**Spec:**
```
Type:       Mobile application
Data model: Person(id, name, birth_date)
            Vaccine(id, name, doses_required)
            Dose(id, person_id -> Person, vaccine_id -> Vaccine, dose_number, given_on, batch_number, clinic)
Features:   - Keep vaccination records per family member
            - Store batch numbers and clinics
            - Show which doses are due next by schedule
            - Remind before a dose is due
            - Export a vaccination card for travel
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 240

**Intent:**
invisalign wear time tracker 22h a day

**Spec:**
```
Type:       Mobile application
Data model: Aligner(id, number, started_on, days)
            OutPeriod(id, removed_at, put_back_at, reason)
Features:   - Start a timer when aligners are taken out
            - Remind to put them back after 30 minutes
            - Calculate daily wear time against 22 hours
            - Count days left on the current aligner and remind to switch
            - Show wear history per aligner
Storage:    Local on-device database (SQLite)
Tech stack: React Native, Notifee, expo-sqlite
```

---

## Example 241

**Intent:**
save my glasses prescription and when i got new lenses

**Spec:**
```
Type:       Mobile application
Data model: Prescription(id, issued_on, optometrist, od_sphere, od_cylinder, od_axis, os_sphere, os_cylinder, os_axis, pd, photo_path)
            Purchase(id, prescription_id -> Prescription, kind, bought_on, price)
Features:   - Store prescriptions for each eye
            - Photograph the paper prescription
            - Compare changes between prescriptions
            - Remind about the next eye exam
            - Log glasses and lens purchases
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 242

**Intent:**
standing desk timer sit stand alternate

**Spec:**
```
Type:       Mobile application
Data model: Schedule(sit_min, stand_min, work_start, work_end)
            Interval(id, posture, started_at, ended_at)
Features:   - Alternate sit and stand reminders on a schedule
            - Show today's standing time
            - Pause during lunch
            - Show weekly standing totals
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, WorkManager, Room
```

---

## Example 243

**Intent:**
30 day plank challenge

**Spec:**
```
Type:       Mobile application
Data model: Challenge(id, name, start_date)
            DayTarget(challenge_id -> Challenge, day, seconds)
            Attempt(id, challenge_id -> Challenge, day, seconds_held, done_on)
Features:   - Show today's target hold time
            - Run a countdown with voice cues
            - Mark the day complete
            - Show a 30-day progress grid
            - Allow rest days
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_tts, Hive
```

---

## Example 244

**Intent:**
couch to 5k for my mom who never ran before

**Spec:**
```
Type:       Mobile application
Data model: Program(id, name, weeks)
            Workout(id, program_id -> Program, week, day, intervals_json)
            CompletedWorkout(id, workout_id -> Workout, done_at, distance_m)
Features:   - Follow a 9-week walk/run program
            - Announce run and walk intervals by voice over music
            - Keep running with the screen locked
            - Mark workouts done and unlock the next
            - Show progress through the program
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVSpeechSynthesizer, Core Location, SwiftData
```

---

## Example 245

**Intent:**
connect my rowing machine via bluetooth and log workouts

**Spec:**
```
Type:       Mobile application (Bluetooth fitness)
Data model: RowSession(id, started_at, duration_s, distance_m, avg_split_500m, avg_spm, calories)
            Stroke(id, session_id -> RowSession, t_s, spm, power_w)
Features:   - Connect to the rower using the Bluetooth FTMS profile
            - Show live split, stroke rate and power
            - Run interval workouts
            - Save sessions with stroke data
            - Chart split times over weeks
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Android BLE API, Room
```

---

## Example 246

**Intent:**
body measurements tracker waist arms chest

**Spec:**
```
Type:       Mobile application
Data model: Measurement(id, part, cm, measured_on)
            ProgressPhoto(id, pose, file_path, taken_on)
Features:   - Log body measurements for each part
            - Chart each measurement over time
            - Take progress photos by pose
            - Compare photos from two dates
            - Remind every two weeks
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-camera, expo-sqlite
```

---

## Example 247

**Intent:**
vitamins and supplements tracker

**Spec:**
```
Type:       Mobile application
Data model: Supplement(id, name, dose, unit, time_of_day, with_food, stock_count)
            Intake(id, supplement_id -> Supplement, taken_at)
Features:   - List supplements with dose and timing
            - Check off doses each day
            - Group by morning, lunch and evening
            - Track stock and warn when low
            - Show monthly adherence
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData, UserNotifications
```

---

## Example 248

**Intent:**
alcohol units counter, i want to drink less

**Spec:**
```
Type:       Mobile application
Data model: DrinkType(id, name, volume_ml, abv)
            Drink(id, drink_type_id -> DrinkType, consumed_at)
            Goal(weekly_units, dry_days_target)
Features:   - Log drinks from presets like pint of beer or glass of wine
            - Calculate alcohol units per drink
            - Show weekly units against a goal
            - Track dry days
            - Show money spent on alcohol
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 249

**Intent:**
i spend too much time on instagram and tiktok i want an app that makes me wait 10 sec before opening them

**Spec:**
```
Type:       Mobile application (digital wellbeing)
Data model: WatchedApp(id, package_name, delay_s, daily_limit_min)
            OpenAttempt(id, package_name, attempted_at, proceeded)
Features:   - Detect when a chosen app is opened
            - Show a breathing pause screen before continuing
            - Ask "do you really want to open it?"
            - Count how often the user gives up
            - Show daily time per watched app
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, AccessibilityService, UsageStatsManager, Room
```

---

## Example 250

**Intent:**
speed reading trainer, words flash one by one

**Spec:**
```
Type:       Mobile application
Data model: Text(id, title, content, source)
            Session(id, text_id -> Text, wpm, words_read, read_at)
Features:   - Import text from paste, EPUB or a web article
            - Show words one at a time at a set WPM
            - Pause on punctuation longer
            - Increase speed gradually
            - Quiz comprehension after reading
Storage:    Local on-device database (SQLite)
Tech stack: React Native, epubjs-rn, expo-sqlite
```

---

## Example 251

**Intent:**
library books due dates

**Spec:**
```
Type:       Mobile application
Data model: Library(id, name)
            Loan(id, library_id -> Library, title, borrowed_on, due_on, renewed_count, returned)
Features:   - Add borrowed books by scanning the ISBN
            - Show due dates sorted by soonest
            - Notify two days before due
            - Track renewals
            - List books per library card
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, mobile_scanner, Open Library API, sqflite
```

---

## Example 252

**Intent:**
anagram and crossword helper that works offline

**Spec:**
```
Type:       Mobile application (offline)
Features:   - Find anagrams of a set of letters
            - Solve crossword patterns like c?t?h
            - Filter results by word length
            - Show word definitions from a bundled dictionary
            - Support blank tiles for Scrabble
Storage:    Bundled word list and dictionary in SQLite
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 253

**Intent:**
take photo of a sudoku and solve it

**Spec:**
```
Type:       Mobile application (on-device vision)
Features:   - Detect the sudoku grid in a camera photo
            - Recognise digits in each cell
            - Let the user fix misread digits
            - Solve the puzzle with backtracking
            - Reveal one hint at a time or the full solution
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Vision, Core ML (digit classifier)
```

---

## Example 254

**Intent:**
rubiks cube timer with scrambles and averages

**Spec:**
```
Type:       Mobile application
Data model: Session(id, puzzle, name)
            Solve(id, session_id -> Session, scramble, time_ms, penalty, solved_at)
Features:   - Generate WCA-style scrambles
            - Start and stop the timer by touching the screen
            - Add +2 and DNF penalties
            - Calculate ao5, ao12 and best times
            - Chart solve times
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Hive
```

---

## Example 255

**Intent:**
concert log every gig ive been to

**Spec:**
```
Type:       Mobile application
Data model: Artist(id, name)
            Venue(id, name, city)
            Concert(id, venue_id -> Venue, date, ticket_price, rating, setlist_url)
            ConcertArtist(concert_id -> Concert, artist_id -> Artist, headliner)
Features:   - Log concerts with artists and venue
            - Fetch setlists from setlist.fm
            - Show most seen artists
            - Show concerts per year
            - Attach ticket photos
Storage:    Local on-device database (SQLite)
Tech stack: React Native, setlist.fm API, expo-sqlite
```

---

## Example 256

**Intent:**
offline festival schedule planner, there is no signal at the festival

**Spec:**
```
Type:       Mobile application (offline)
Data model: Stage(id, name)
            Act(id, stage_id -> Stage, name, starts_at, ends_at)
            Pick(act_id -> Act, priority)
Features:   - Load the festival timetable once while online
            - Mark acts to see with priority
            - Show clashes between picks
            - Notify 15 minutes before an act
            - Show a personal timeline
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 257

**Intent:**
restaurant tried and want-to-try list

**Spec:**
```
Type:       Mobile application
Data model: Restaurant(id, name, cuisine, lat, lng, price_level, status)
            Visit(id, restaurant_id -> Restaurant, visited_on, rating, dishes, notes)
Features:   - Save restaurants to a want-to-try list
            - Log visits with rating and dishes
            - Show restaurants on a map
            - Filter by cuisine and price
            - Pick a random place to try
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, MapKit (place search), SwiftData
```

---

## Example 258

**Intent:**
home bar cocktail app shows what cocktails i can make with what bottles i have

**Spec:**
```
Type:       Mobile application
Data model: Ingredient(id, name, category, in_stock)
            Cocktail(id, name, method, glass, garnish)
            CocktailIngredient(cocktail_id -> Cocktail, ingredient_id -> Ingredient, amount_ml)
Features:   - Mark which bottles and mixers are in stock
            - Show cocktails that can be made right now
            - Show cocktails missing only one ingredient
            - Scale recipes for several drinks
            - Save favourites
Storage:    Bundled cocktail database plus user stock in SQLite
Tech stack: Flutter, sqflite
```

---

## Example 259

**Intent:**
bbq smoker app connects to my bluetooth meat thermometer

**Spec:**
```
Type:       Mobile application (Bluetooth companion)
Data model: Cook(id, meat, started_at, target_temp_c, finished_at)
            TempSample(id, cook_id -> Cook, t, probe, temp_c)
Features:   - Connect to a Bluetooth meat thermometer
            - Show live pit and meat temperatures
            - Alert when the target temperature is reached
            - Estimate time left from the temperature curve
            - Save cooks with notes
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-ble-plx, expo-sqlite
```

---

## Example 260

**Intent:**
pizza dough calculator

**Spec:**
```
Type:       Mobile application (offline)
Data model: DoughRecipe(id, name, balls, ball_weight_g, hydration, salt_percent, yeast_percent)
Features:   - Calculate flour, water, salt and yeast from ball count and weight
            - Adjust yeast for fermentation time and room temperature
            - Save dough recipes
            - Show a fermentation schedule
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 261

**Intent:**
celiac card that shows "i cannot eat gluten" in the local language when i travel

**Spec:**
```
Type:       Mobile application (offline)
Data model: Phrase(id, language, text)
            Profile(conditions, extra_notes)
Features:   - Show a dining card explaining gluten-free needs
            - Translate the card into many languages
            - Show the card large to restaurant staff
            - Add other allergies to the card
            - Work offline
Storage:    Bundled translations in app assets
Tech stack: Swift, SwiftUI
```

---

## Example 262

**Intent:**
scan ingredients list and tell me if its vegan

**Spec:**
```
Type:       Mobile application
Data model: Ingredient(id, name, aliases, status)
            Scan(id, product_name, result, scanned_at)
Features:   - Scan a barcode and look up ingredients on Open Food Facts
            - Read the ingredient list with OCR when the barcode is unknown
            - Flag non-vegan and maybe-vegan ingredients
            - Explain why an ingredient is flagged
            - Keep a scan history
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, CameraX, ML Kit, Open Food Facts API, Room
```

---

## Example 263

**Intent:**
baby first milestones journal, first smile first steps etc

**Spec:**
```
Type:       Mobile application
Data model: Child(id, name, birth_date)
            Milestone(id, child_id -> Child, kind, achieved_on, note, media_path)
Features:   - Record milestones with date, photo or video
            - Show a timeline of firsts
            - Show age at each milestone
            - Suggest upcoming milestones by age
            - Export a keepsake PDF
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, image_picker, video_player, Drift, pdf
```

---

## Example 264

**Intent:**
calculate paracetamol dose for my kid by weight

**Spec:**
```
Type:       Mobile application (offline)
Data model: Child(id, name, weight_kg)
            Dose(id, child_id -> Child, medicine, ml, given_at)
Features:   - Calculate dose from weight and syrup strength
            - Log doses given
            - Show when the next dose is allowed
            - Warn when the 24-hour maximum would be exceeded
            - Show a disclaimer to confirm with a pharmacist
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 265

**Intent:**
fever diary for kids when sick

**Spec:**
```
Type:       Mobile application
Data model: Child(id, name)
            TempReading(id, child_id -> Child, temp_c, method, measured_at)
            MedGiven(id, child_id -> Child, medicine, dose, given_at)
Features:   - Log temperatures with method
            - Log fever medicine
            - Chart temperature over the illness
            - Show time since last medicine
            - Share the log with the doctor
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 266

**Intent:**
flea and worm treatment reminders for my pets

**Spec:**
```
Type:       Mobile application
Data model: Pet(id, name, species, weight_kg)
            Treatment(id, pet_id -> Pet, product, kind, given_on, interval_weeks)
Features:   - Log flea, tick and worm treatments
            - Calculate when each is due again
            - Notify on due dates
            - Show treatment history per pet
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData, UserNotifications
```

---

## Example 267

**Intent:**
lost pet poster maker

**Spec:**
```
Type:       Mobile application
Data model: Pet(id, name, species, breed, colour, photo_path)
            Poster(id, pet_id -> Pet, last_seen_place, last_seen_at, contact_phone, reward)
Features:   - Fill in pet details and last-seen place
            - Generate a printable poster with photo and a QR code
            - Share the poster to social apps
            - Show a map of where it was seen
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, pdf, printing, qr_flutter
```

---

## Example 268

**Intent:**
bird feeder visitors count each morning

**Spec:**
```
Type:       Mobile application
Data model: Species(id, name)
            Count(id, species_id -> Species, number, counted_at, weather)
Features:   - Count birds per species with tap counters
            - Save each morning's count
            - Show which species visit most per month
            - Export counts in a format for citizen science surveys
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 269

**Intent:**
light meter for houseplants, is this spot bright enough

**Spec:**
```
Type:       Mobile application (plant utility)
Data model: Spot(id, name, room, avg_lux, measured_at)
            PlantNeed(id, plant_name, min_lux, max_lux)
Features:   - Measure light level with the phone's light sensor
            - Save readings for spots in the house
            - Compare spot light with a plant's needs
            - Suggest plants that suit a spot
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, SensorManager (TYPE_LIGHT), Room
```

---

## Example 270

**Intent:**
square foot garden planner drag plants into grid

**Spec:**
```
Type:       Mobile application
Data model: Bed(id, name, cols, rows)
            Cell(bed_id -> Bed, col, row, crop_id -> Crop, planted_on)
            Crop(id, name, per_square, icon)
Features:   - Create raised beds as grids
            - Drag crops into squares with per-square counts
            - Warn about bad companion plants next to each other
            - Show planting and harvest dates
            - Save layouts per season
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 271

**Intent:**
rain gauge log for my farm, mm per day

**Spec:**
```
Type:       Mobile application
Data model: Gauge(id, name, lat, lng)
            RainReading(id, gauge_id -> Gauge, mm, read_on)
Features:   - Log daily rainfall per gauge
            - Show monthly and yearly totals
            - Compare with the same period last year
            - Export to CSV
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 272

**Intent:**
loyalty cards wallet so i dont carry the plastic

**Spec:**
```
Type:       Mobile application
Data model: LoyaltyCard(id, store, barcode_value, barcode_format, color, note)
Features:   - Add cards by scanning their barcode
            - Show the barcode full screen at max brightness
            - Sort cards by most used
            - Show the nearest store's card when arriving
            - Back up cards to a file
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, VisionKit, Core Image (barcode generation), SwiftData
```

---

## Example 273

**Intent:**
gift card balances tracker

**Spec:**
```
Type:       Mobile application
Data model: GiftCard(id, store, number_last4, balance, expires_on)
            Spend(id, card_id -> GiftCard, amount, spent_on)
Features:   - Add gift cards with balance and expiry
            - Deduct spending
            - Notify before cards expire
            - Show total gift card balance
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-secure-store, expo-sqlite
```

---

## Example 274

**Intent:**
i flip stuff on ebay and want to track profit per item

**Spec:**
```
Type:       Mobile application
Data model: Item(id, title, bought_for, bought_on, source, listed_on, sold_for, sold_on, fees, shipping)
            Photo(id, item_id -> Item, file_path)
Features:   - Log items with purchase cost and source
            - Track status from bought to listed to sold
            - Calculate profit after fees and shipping
            - Show monthly profit
            - Show items unsold for over 60 days
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 275

**Intent:**
waitress here, want to log my tips per shift and see which days are best

**Spec:**
```
Type:       Mobile application
Data model: Shift(id, date, start_time, end_time, cash_tips, card_tips, sales, section)
Features:   - Log shifts with cash and card tips
            - Calculate tips per hour
            - Show best days of the week and shift times
            - Show weekly and monthly totals
            - Export for taxes
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 276

**Intent:**
52 week savings challenge

**Spec:**
```
Type:       Mobile application
Data model: Challenge(id, start_date, base_amount, reverse)
            Week(id, challenge_id -> Challenge, number, amount, saved)
Features:   - Generate weekly amounts that increase each week
            - Tick off each week when saved
            - Allow the reverse order
            - Show total saved
            - Remind every week
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 277

**Intent:**
dividend tracker for my stocks

**Spec:**
```
Type:       Mobile application
Data model: Holding(id, ticker, shares, avg_cost)
            Dividend(id, ticker, ex_date, pay_date, amount_per_share)
Features:   - Add holdings with share count
            - Fetch dividend history from a market data API
            - Show expected dividend income by month
            - Calculate yield on cost
            - Show a dividend calendar
Storage:    Local on-device database (SQLite)
Tech stack: React Native, Financial Modeling Prep API, expo-sqlite
```

---

## Example 278

**Intent:**
retirement calculator simple

**Spec:**
```
Type:       Mobile application (offline)
Data model: Scenario(id, name, current_age, retire_age, savings, monthly_contribution, return_rate, inflation)
Features:   - Project savings growth to retirement age
            - Adjust for inflation
            - Calculate sustainable monthly withdrawal
            - Compare scenarios side by side
            - Chart the projection
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, fl_chart, Hive
```

---

## Example 279

**Intent:**
log charity donations for my tax return

**Spec:**
```
Type:       Mobile application
Data model: Charity(id, name, registration_number)
            Donation(id, charity_id -> Charity, amount, donated_on, method, receipt_path, gift_aid)
Features:   - Log donations with receipts
            - Mark Gift Aid eligible donations
            - Total donations per tax year
            - Export a summary for the tax return
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 280

**Intent:**
EV charging log, kwh and cost each time

**Spec:**
```
Type:       Mobile application
Data model: Car(id, name, battery_kwh)
            ChargeSession(id, car_id -> Car, started_at, kwh, cost, location, charger_type, odometer_km)
Features:   - Log charging sessions with kWh and cost
            - Separate home and public charging
            - Calculate cost per 100 km
            - Compare with petrol cost
            - Show monthly charging spend
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData, Swift Charts
```

---

## Example 281

**Intent:**
bike maintenance log, chain wax every 300km

**Spec:**
```
Type:       Mobile application
Data model: Bike(id, name)
            Component(id, bike_id -> Bike, name, installed_on, km_at_install, service_every_km)
            Ride(id, bike_id -> Bike, km, date)
Features:   - Track km per bike and per component
            - Import rides from Strava
            - Notify when a component needs service
            - Log replacements
            - Show component wear
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Strava API, Drift
```

---

## Example 282

**Intent:**
offline bus timetable for my town, no internet on the bus

**Spec:**
```
Type:       Mobile application (offline)
Data model: Stop(id, name, lat, lng)
            Route(id, name, color)
            Trip(id, route_id -> Route, service_days)
            StopTime(trip_id -> Trip, stop_id -> Stop, departs_at, sequence)
Features:   - Import the town's GTFS timetable
            - Show next departures from a stop
            - Find the nearest stop with GPS
            - Save favourite stops
            - Update the timetable when online
Storage:    GTFS data in on-device SQLite
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 283

**Intent:**
wheelchair accessible places map, me and other users can rate ramps and toilets

**Spec:**
```
Type:       Mobile application with backend
Auth:       Sign in with email or Google
Data model: User(id, name)
            Place(id, name, lat, lng, category)
            AccessReview(id, place_id -> Place, user_id -> User, entrance, toilet, parking, photo_path, created_at)
Features:   - Show places on a map with accessibility ratings
            - Add reviews for entrance, toilet and parking
            - Upload photos of ramps and doors
            - Filter places by fully accessible
            - Support screen readers throughout
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Supabase (Auth, Postgres, Storage), react-native-maps
```

---

## Example 284

**Intent:**
my brother is deaf, want phone to vibrate and flash when doorbell or baby crying

**Spec:**
```
Type:       Mobile application (accessibility)
Data model: SoundType(id, name, enabled, vibration_pattern)
            Detection(id, sound_type_id -> SoundType, detected_at, confidence)
Features:   - Listen continuously with an on-device sound classifier
            - Detect doorbells, alarms and baby crying
            - Vibrate and flash the screen and torch
            - Send the alert to a paired smartwatch
            - Show a log of detected sounds
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Foreground Service, TensorFlow Lite (YAMNet), Wear OS Data Layer, Room
```

---

## Example 285

**Intent:**
big clock for my nan showing day of week and if its morning or night, she gets confused

**Spec:**
```
Type:       Mobile application (accessibility, tablet)
Features:   - Show the day, date and time in very large text
            - Show "morning", "afternoon", "evening" or "night" with pictures
            - Show a reminder message set by family
            - Keep the screen always on
            - Lock settings behind a PIN
Storage:    SharedPreferences
Tech stack: Kotlin, Jetpack Compose
```

---

## Example 286

**Intent:**
speech therapy practice for my son, R and S sounds

**Spec:**
```
Type:       Mobile application
Data model: Sound(id, phoneme, position)
            Word(id, sound_id -> Sound, text, image_path)
            Practice(id, word_id -> Word, recorded_at, audio_path, parent_rating)
Features:   - Show picture cards for a target sound
            - Record the child saying the word
            - Play back next to a model pronunciation
            - Let a parent rate each attempt
            - Track accuracy per sound and position
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVFoundation, SwiftData
```

---

## Example 287

**Intent:**
voice pitch trainer, i am trans woman working on my voice

**Spec:**
```
Type:       Mobile application
Data model: Exercise(id, name, target_hz_min, target_hz_max)
            Recording(id, exercise_id -> Exercise, recorded_at, avg_hz, resonance_score, file_path)
Features:   - Show live voice pitch in Hz against a target range
            - Run daily exercises like sirens and reading passages
            - Record and save practice clips
            - Chart average pitch over weeks
            - Keep all recordings private on the device
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, record, pitch_detector_dart, Drift
```

---

## Example 288

**Intent:**
letter tracing app for preschool

**Spec:**
```
Type:       Mobile application (kids education)
Data model: Letter(id, char, stroke_paths)
            Attempt(id, letter_id -> Letter, accuracy, attempted_at)
Features:   - Show letters with dotted stroke guides
            - Check tracing accuracy against the stroke path
            - Animate the correct stroke order
            - Reward with stickers
            - Track letters mastered
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, CustomPainter, Hive
```

---

## Example 289

**Intent:**
prayer times and qibla compass offline

**Spec:**
```
Type:       Mobile application (offline)
Data model: Location(id, name, lat, lng, timezone)
            Settings(calc_method, asr_method, adhan_sound)
Features:   - Calculate the five daily prayer times from location
            - Choose calculation methods
            - Play the adhan or a notification at each time
            - Show a qibla compass
            - Work without internet
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, adhan-java, SensorManager
```

---

## Example 290

**Intent:**
letter to my future self, opens in 5 years

**Spec:**
```
Type:       Mobile application
Data model: Letter(id, title, body, written_on, open_on, opened, attachment_path)
Features:   - Write letters with optional photos
            - Set an opening date
            - Keep letters locked until the date
            - Notify when a letter can be opened
            - Show a list of sealed letters with countdowns
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-notifications, expo-sqlite
```

---

## Example 291

**Intent:**
one second video diary

**Spec:**
```
Type:       Mobile application
Data model: Clip(id, date, file_path, duration_ms)
Features:   - Record or pick one second of video each day
            - Trim clips to one second
            - Remind each evening
            - Stitch clips into a monthly or yearly movie
            - Export the movie to the gallery
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVFoundation (AVMutableComposition), SwiftData
```

---

## Example 292

**Intent:**
write down funny things my kids say

**Spec:**
```
Type:       Mobile application
Data model: Kid(id, name, birth_date)
            Saying(id, kid_id -> Kid, text, said_on, context)
Features:   - Save quotes with the child's age automatically
            - Add context of what happened
            - Browse quotes by child
            - Share a quote as an image card
            - Back up to a file
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, screenshot, sqflite
```

---

## Example 293

**Intent:**
homework planner for my 11 yo, he forgets everything lol

**Spec:**
```
Type:       Mobile application
Data model: Subject(id, name, color)
            Homework(id, subject_id -> Subject, title, due_on, estimated_min, done_at, photo_path)
Features:   - Add homework with subject and due date
            - Photograph the task from the board or book
            - Show today's and tomorrow's homework
            - Remind after school
            - Let a parent see what is done
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-camera, expo-sqlite
```

---

## Example 294

**Intent:**
calligraphy practice sheets on ipad with pencil

**Spec:**
```
Type:       Mobile application (iPad)
Data model: Guide(id, name, style, slant_deg, x_height_mm)
            PracticeSheet(id, guide_id -> Guide, drawing_data, created_at)
Features:   - Show guide lines with slant and x-height
            - Draw with Apple Pencil pressure
            - Overlay model letters to trace
            - Save and compare practice sheets
            - Export sheets as PDF
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, PencilKit, SwiftData
```

---

## Example 295

**Intent:**
daily drawing prompt and i upload what i drew

**Spec:**
```
Type:       Mobile application
Data model: Prompt(id, text, date)
            Drawing(id, prompt_id -> Prompt, photo_path, created_at, minutes_spent)
Features:   - Show a new drawing prompt each day
            - Photograph or import the finished drawing
            - Show a gallery grid by month
            - Track the daily streak
            - Skip a prompt and get another
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, image_picker, Hive
```

---

## Example 296

**Intent:**
novel writing word count goal like nanowrimo

**Spec:**
```
Type:       Mobile application
Data model: Project(id, title, target_words, deadline)
            WritingSession(id, project_id -> Project, date, words_added, minutes)
Features:   - Set a word count goal and deadline
            - Log words written per session
            - Calculate words needed per day to finish
            - Show a progress chart with the target line
            - Keep a writing streak
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, Vico
```

---

## Example 297

**Intent:**
3d printer filament spool inventory how much is left

**Spec:**
```
Type:       Mobile application
Data model: Spool(id, brand, material, color, diameter_mm, initial_g, remaining_g, opened_on, dried_on)
            Print(id, spool_id -> Spool, name, grams_used, printed_on)
Features:   - Add spools with material and colour
            - Deduct grams used per print
            - Weigh a spool to update remaining filament
            - Print QR labels for spools
            - Warn when a spool is nearly empty
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, mobile_scanner, qr_flutter, Drift
```

---

## Example 298

**Intent:**
fabric stash for sewing, with how many meters and photo

**Spec:**
```
Type:       Mobile application
Data model: Fabric(id, type, color, pattern, width_cm, length_m, photo_path, bought_on, price)
            Project(id, name, pattern_name, status)
            ProjectFabric(project_id -> Project, fabric_id -> Fabric, meters_used)
Features:   - Photograph fabrics with type and length
            - Search the stash by colour and type
            - Assign fabric to sewing projects
            - Deduct used meters
            - Show total stash value
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, PhotosUI, SwiftData
```

---

## Example 299

**Intent:**
woodworking cut list optimizer, i give board sizes and pieces and it tells me how to cut

**Spec:**
```
Type:       Mobile application (offline)
Data model: Stock(id, length_mm, width_mm, quantity)
            Piece(id, name, length_mm, width_mm, quantity)
            CutPlan(id, created_at, waste_percent, layout_json)
Features:   - Enter stock boards and required pieces
            - Calculate an optimised cutting layout with saw kerf
            - Draw each board with its cuts
            - Show waste percentage
            - Save cut plans per project
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose (Canvas), Room
```

---

## Example 300

**Intent:**
crochet pattern row tracker with the pattern pdf open

**Spec:**
```
Type:       Mobile application
Data model: Pattern(id, name, pdf_path, current_page)
            Highlight(id, pattern_id -> Pattern, page, y_position)
            Counter(id, pattern_id -> Pattern, value)
Features:   - Open pattern PDFs inside the app
            - Move a highlighter bar to mark the current row
            - Count stitches and rows
            - Save the position per pattern
            - Add notes per page
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, pdfx, sqflite
```

---

## Example 301

**Intent:**
jigsaw puzzle collection and how long each took

**Spec:**
```
Type:       Mobile application
Data model: Puzzle(id, brand, title, pieces, photo_path, owned)
            Completion(id, puzzle_id -> Puzzle, started_on, finished_on, hours, missing_pieces)
Features:   - Catalogue puzzles with piece count
            - Log completions with time taken
            - Track missing pieces
            - Mark puzzles lent or swapped
            - Show pieces per hour stats
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 302

**Intent:**
perfume collection with notes and when i wear them

**Spec:**
```
Type:       Mobile application
Data model: Perfume(id, name, house, concentration, notes_top, notes_heart, notes_base, ml_left, photo_path)
            WearLog(id, perfume_id -> Perfume, worn_on, occasion, rating)
Features:   - Catalogue perfumes with fragrance notes
            - Log what was worn and the occasion
            - Suggest a perfume by season and weather
            - Track bottle level
            - Show least worn bottles
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, WeatherKit, SwiftData
```

---

## Example 303

**Intent:**
sneaker collection with what i paid and what theyre worth now

**Spec:**
```
Type:       Mobile application
Data model: Sneaker(id, brand, model, colorway, size, sku, paid, bought_on, condition, photo_path)
            ValueCheck(id, sneaker_id -> Sneaker, value, checked_on)
Features:   - Add pairs with SKU, size and price paid
            - Record current market value
            - Show gain or loss per pair
            - Log when each pair was worn
            - Show total collection value
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, image_picker
```

---

## Example 304

**Intent:**
my automatic watch gains seconds, app to track accuracy per day

**Spec:**
```
Type:       Mobile application
Data model: Watch(id, brand, model, movement)
            Measurement(id, watch_id -> Watch, measured_at, deviation_s, position)
Features:   - Sync to atomic time from an NTP server
            - Tap when the second hand hits 12 to record deviation
            - Calculate seconds per day gain or loss
            - Track accuracy by resting position
            - Keep a service history per watch
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, TrueTime (NTP), Room
```

---

## Example 305

**Intent:**
rock and mineral collection catalog

**Spec:**
```
Type:       Mobile application
Data model: Specimen(id, name, mineral_type, locality, found_on, hardness, size_mm, photo_path, purchased, price)
Features:   - Catalogue specimens with photos and locality
            - Record hardness and properties
            - Print specimen labels with numbers
            - Show finds on a map
            - Filter by mineral type
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-print, react-native-maps, expo-sqlite
```

---

## Example 306

**Intent:**
amateur radio contact log, qso, callsign frequency mode

**Spec:**
```
Type:       Mobile application
Data model: Qso(id, callsign, frequency_mhz, band, mode, rst_sent, rst_received, at_utc, grid_square, notes)
Features:   - Log contacts with callsign, band and mode
            - Use UTC time automatically
            - Look up callsigns via QRZ
            - Export logs as ADIF
            - Show DXCC countries worked
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, QRZ XML API, Drift
```

---

## Example 307

**Intent:**
geocaching offline log

**Spec:**
```
Type:       Mobile application (offline)
Data model: Cache(id, gc_code, name, lat, lng, type, difficulty, terrain, hint)
            Find(id, cache_id -> Cache, found_at, log_text)
Features:   - Import caches from GPX files
            - Navigate to a cache with compass and distance
            - Decode hints
            - Log finds offline
            - Export field notes for upload
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, MapLibre Native, Room
```

---

## Example 308

**Intent:**
metal detecting finds with gps where i dug them

**Spec:**
```
Type:       Mobile application
Data model: Site(id, name, permission_from, permission_until)
            Find(id, site_id -> Site, description, material, depth_cm, lat, lng, found_on, photo_path)
Features:   - Log finds with GPS location and depth
            - Photograph finds
            - Record landowner permission per site
            - Show find heatmap per site
            - Export finds for reporting to the authorities
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Core Location, MapKit, SwiftData
```

---

## Example 309

**Intent:**
notes on podcast episodes with timestamps

**Spec:**
```
Type:       Mobile application
Data model: Podcast(id, title, feed_url)
            Episode(id, podcast_id -> Podcast, title, audio_url)
            Note(id, episode_id -> Episode, at_s, text)
Features:   - Subscribe to podcasts by RSS feed
            - Play episodes in the app
            - Add notes at the current timestamp
            - Jump to a note's timestamp
            - Export notes as Markdown
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-track-player, rss-parser, expo-sqlite
```

---

## Example 310

**Intent:**
poems notebook with rhyme finder

**Spec:**
```
Type:       Mobile application
Data model: Poem(id, title, body, form, created_at, updated_at)
Features:   - Write and edit poems
            - Find rhymes for a selected word
            - Count syllables per line
            - Check haiku and sonnet structure
            - Organise poems in folders
Storage:    Bundled CMU pronunciation dictionary and poems in SQLite
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 311

**Intent:**
my band needs setlists and a log of gigs we played

**Spec:**
```
Type:       Mobile application with backend
Auth:       Band account with invite code
Data model: Band(id, name)
            Song(id, band_id -> Band, title, key, bpm, duration_s)
            Gig(id, band_id -> Band, venue, date, fee)
            SetlistEntry(gig_id -> Gig, song_id -> Song, position)
Features:   - Keep the band's song list with key and tempo
            - Build setlists per gig and see total length
            - Share setlists with all members in real time
            - Log gigs with venue and fee
            - Show most played songs
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase Auth, Firestore
```

---

## Example 312

**Intent:**
drum rudiments practice with tempo goals

**Spec:**
```
Type:       Mobile application
Data model: Rudiment(id, name, sticking, target_bpm)
            Practice(id, rudiment_id -> Rudiment, bpm, minutes, practiced_on)
Features:   - Show the 40 standard rudiments with sticking
            - Practise with a built-in click
            - Log the tempo reached
            - Raise the target tempo when clean
            - Chart tempo per rudiment
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVAudioEngine, SwiftData
```

---

## Example 313

**Intent:**
comic book collection, issues i have and missing in a series

**Spec:**
```
Type:       Mobile application
Data model: Series(id, title, publisher, start_year)
            Issue(id, series_id -> Series, number, cover_date, owned, grade, price_paid)
Features:   - Add series and issues
            - Mark owned and missing issues
            - Scan comic barcodes
            - Show gaps in each series
            - Show total value
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-barcode-scanner, Comic Vine API, expo-sqlite
```

---

## Example 314

**Intent:**
timelapse app for my plants growing, take photo every hour

**Spec:**
```
Type:       Mobile application (camera utility)
Data model: Timelapse(id, name, interval_min, started_at, ended_at)
            Frame(id, timelapse_id -> Timelapse, file_path, taken_at)
Features:   - Capture a photo at a set interval in the background
            - Show a ghost overlay to align the phone
            - Pause at night or when dark
            - Render frames into a video
            - Export the video to the gallery
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, CameraX, Foreground Service, Media3 Transformer, Room
```

---

## Example 315

**Intent:**
put my watermark on all my photos before posting

**Spec:**
```
Type:       Mobile application (photo utility)
Data model: Watermark(id, name, text, logo_path, position, opacity, scale)
Features:   - Pick multiple photos
            - Add a text or logo watermark
            - Set position, opacity and size
            - Save watermark presets
            - Export watermarked copies in batch
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, image, photo_manager, Hive
```

---

## Example 316

**Intent:**
organise my screenshots automatically, receipts memes chats

**Spec:**
```
Type:       Mobile application (on-device ML)
Data model: Screenshot(id, asset_id, category, text, taken_at)
            Category(id, name)
Features:   - Find screenshots in the photo library
            - Read text in each screenshot on-device
            - Sort screenshots into categories like receipts and chats
            - Search screenshots by text
            - Bulk delete old ones
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, PhotoKit, Vision, Core ML, SwiftData
```

---

## Example 317

**Intent:**
magnifier with flashlight for reading small labels

**Spec:**
```
Type:       Mobile application (accessibility)
Features:   - Show the camera at up to 10x zoom
            - Turn on the torch
            - Freeze the image to read it
            - Apply high-contrast and inverted colour filters
            - Use large buttons and volume keys for zoom
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, CameraX
```

---

## Example 318

**Intent:**
live captions for conversations so my deaf grandpa can read what we say

**Spec:**
```
Type:       Mobile application (accessibility)
Data model: Transcript(id, started_at, text)
Features:   - Transcribe speech to text in real time
            - Show captions in very large text
            - Work offline with on-device speech recognition
            - Let the other person type replies
            - Save transcripts if wanted
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Speech framework (on-device recognition), SwiftData
```

---

## Example 319

**Intent:**
reading helper for dyslexia, special font, ruler line, read aloud

**Spec:**
```
Type:       Mobile application (accessibility)
Data model: Document(id, title, source, content, last_position)
Features:   - Import text from paste, photo or PDF
            - Show text with a dyslexia-friendly font and spacing
            - Show a moving reading ruler
            - Read aloud with word highlighting
            - Change background tint
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, google_mlkit_text_recognition, flutter_tts, sqflite
```

---

## Example 320

**Intent:**
fitness workouts for wheelchair users

**Spec:**
```
Type:       Mobile application
Data model: Exercise(id, name, muscle_group, video_path, seated)
            Workout(id, name)
            WorkoutExercise(workout_id -> Workout, exercise_id -> Exercise, reps, sets)
            Session(id, workout_id -> Workout, done_on)
Features:   - Browse seated exercises by muscle group
            - Follow guided workouts with videos
            - Use resistance band variations
            - Track completed sessions
            - Support switch control and VoiceOver
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVKit, SwiftData
```

---

## Example 321

**Intent:**
bill due date reminders

**Spec:**
```
Type:       Mobile application
Data model: Bill(id, payee, amount, due_day, recurrence, autopay)
            BillPayment(id, bill_id -> Bill, paid_on, amount)
Features:   - Add recurring bills with due day
            - Notify before each due date
            - Mark bills paid
            - Show upcoming bills this month
            - Show total monthly bills
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, WorkManager
```

---

## Example 322

**Intent:**
pilot logbook for my private flying, hours and aircraft

**Spec:**
```
Type:       Mobile application
Data model: Aircraft(id, registration, type, engine)
            Flight(id, aircraft_id -> Aircraft, date, from_icao, to_icao, block_off, block_on, pic_min, night_min, landings, remarks)
Features:   - Log flights with block times and landings
            - Calculate PIC, night and total hours
            - Track 90-day currency for passengers
            - Show totals per aircraft type
            - Export to PDF in logbook format
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, pdf
```

---

## Example 323

**Intent:**
jump rope counter

**Spec:**
```
Type:       Mobile application
Data model: Session(id, started_at, duration_s, jumps, max_streak)
Features:   - Count jumps with the phone accelerometer in a pocket
            - Show live count and jumps per minute
            - Run interval rounds
            - Save sessions
            - Show daily totals
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sensors, expo-sqlite
```

---

## Example 324

**Intent:**
bowling scores tracker

**Spec:**
```
Type:       Mobile application
Data model: Game(id, played_on, alley, total)
            Frame(id, game_id -> Game, number, roll1, roll2, roll3)
Features:   - Enter rolls frame by frame
            - Calculate scores with strikes and spares
            - Show average and high game
            - Track strike and spare percentages
            - Chart average over time
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 325

**Intent:**
disc golf scorecard for me and friends

**Spec:**
```
Type:       Mobile application
Data model: Course(id, name, holes)
            HolePar(course_id -> Course, hole, par)
            Round(id, course_id -> Course, played_on)
            PlayerScore(round_id -> Round, player_name, hole, throws)
Features:   - Add courses with par per hole
            - Score rounds for several players
            - Show score relative to par
            - Keep course records
            - Share a round summary
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 326

**Intent:**
whisky tasting notes

**Spec:**
```
Type:       Mobile application
Data model: Whisky(id, name, distillery, region, age, abv, cask)
            Tasting(id, whisky_id -> Whisky, tasted_on, nose, palate, finish, score, flavour_wheel)
Features:   - Log tastings with nose, palate and finish
            - Rate on a flavour wheel
            - Search whiskies by region
            - Show favourite flavour profiles
            - Track bottles owned
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, fl_chart (radar chart)
```

---

## Example 327

**Intent:**
fermentation tracker kimchi kombucha

**Spec:**
```
Type:       Mobile application
Data model: Ferment(id, kind, started_on, vessel, salt_percent, temp_c, ready_on)
            Check(id, ferment_id -> Ferment, checked_on, ph, taste_note, photo_path)
Features:   - Start ferments with recipe and salt percentage
            - Calculate brine salt amounts
            - Remind to burp jars and taste
            - Log checks with pH and photos
            - Show ferments ready soon
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Notifee
```

---

## Example 328

**Intent:**
home canning log with jars and dates

**Spec:**
```
Type:       Mobile application
Data model: Batch(id, recipe, method, processed_on, jars, jar_size_ml, shelf, best_before)
            JarUse(id, batch_id -> Batch, used_on)
Features:   - Log canning batches with method and processing time
            - Track jars by shelf
            - Mark jars as used
            - Warn about batches nearing best-before
            - Show stock per recipe
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 329

**Intent:**
rate coffee shops in my city

**Spec:**
```
Type:       Mobile application
Data model: CoffeeShop(id, name, lat, lng, wifi, outlets)
            Visit(id, shop_id -> CoffeeShop, visited_on, drink, rating, price)
Features:   - Log visits with drink and rating
            - Note wifi and power outlets for working
            - Show shops on a map
            - Rank shops by rating
            - Find nearest shops with wifi
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, MapKit, SwiftData
```

---

## Example 330

**Intent:**
museums i visited and favourite artworks

**Spec:**
```
Type:       Mobile application
Data model: Museum(id, name, city, country)
            Visit(id, museum_id -> Museum, visited_on)
            Artwork(id, visit_id -> Visit, title, artist, photo_path, note)
Features:   - Log museum visits
            - Save favourite artworks with photos
            - Search artworks by artist
            - Show museums on a map
            - Show visits per year
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_map, sqflite
```

---

## Example 331

**Intent:**
escape rooms we did, time and if we escaped

**Spec:**
```
Type:       Mobile application
Data model: Room(id, name, company, city, difficulty)
            Attempt(id, room_id -> Room, played_on, team, escaped, time_min, hints_used, rating)
Features:   - Log escape rooms with team and result
            - Track time and hints used
            - Rate rooms
            - Keep a wishlist of rooms
            - Show success rate
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 332

**Intent:**
drone flight log and preflight checklist

**Spec:**
```
Type:       Mobile application
Data model: Drone(id, model, serial, registration)
            Battery(id, label, cycles)
            Flight(id, drone_id -> Drone, battery_id -> Battery, location, started_at, duration_min, max_altitude_m)
Features:   - Run a preflight checklist before each flight
            - Check wind with a weather API
            - Log flights with battery used
            - Track battery cycles
            - Export a log for authorities
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Open-Meteo API, Room
```

---

## Example 333

**Intent:**
aquascape planted tank journal with photos every week

**Spec:**
```
Type:       Mobile application
Data model: Tank(id, name, volume_l, setup_on)
            Plant(id, tank_id -> Tank, species, planted_on)
            Entry(id, tank_id -> Tank, date, photo_path, co2_bps, fertiliser_ml, notes)
Features:   - Log weekly photos and maintenance
            - Track plants and when added
            - Log CO2 and fertiliser dosing
            - Compare photos over time
            - Remind dosing days
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 334

**Intent:**
candle making recipes fragrance load calculator

**Spec:**
```
Type:       Mobile application
Data model: Recipe(id, name, wax_type, wax_g, fragrance_percent, wick, vessel)
            Batch(id, recipe_id -> Recipe, made_on, candles, cure_until, burn_test_notes)
Features:   - Calculate fragrance oil grams from wax weight and load
            - Save recipes per vessel
            - Log batches with cure dates
            - Record burn test results
            - Notify when curing is done
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Hive
```

---

## Example 335

**Intent:**
soap making lye calculator

**Spec:**
```
Type:       Mobile application (offline)
Data model: Oil(id, name, sap_naoh, sap_koh)
            SoapRecipe(id, name, superfat_percent, water_ratio)
            RecipeOil(recipe_id -> SoapRecipe, oil_id -> Oil, grams)
Features:   - Choose oils and amounts
            - Calculate lye and water from SAP values
            - Apply a superfat percentage
            - Show bar hardness and cleansing estimates
            - Save recipes
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 336

**Intent:**
decision journal, write why i decide something and check later if it was good

**Spec:**
```
Type:       Mobile application
Data model: Decision(id, title, context, options, choice, expected_outcome, confidence, decided_on, review_on)
            Review(id, decision_id -> Decision, outcome, lesson, reviewed_on)
Features:   - Record decisions with options and expected outcome
            - Rate confidence
            - Schedule a review date
            - Prompt to review and rate the outcome
            - Show calibration of confidence vs outcomes
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, expo-notifications
```

---

## Example 337

**Intent:**
tarot journal for my daily pulls

**Spec:**
```
Type:       Mobile application
Data model: Card(id, name, arcana, suit, upright_meaning, reversed_meaning)
            Reading(id, date, spread, question, reflection)
            ReadingCard(reading_id -> Reading, card_id -> Card, position, reversed)
Features:   - Log daily pulls and spreads
            - Show card meanings
            - Write reflections
            - Show most drawn cards
            - Search past readings
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 338

**Intent:**
morning routine checklist with timer for each thing

**Spec:**
```
Type:       Mobile application
Data model: Routine(id, name)
            RoutineItem(id, routine_id -> Routine, title, minutes, position)
            Run(id, routine_id -> Routine, started_at, finished_at)
Features:   - Build a routine with timed steps
            - Run steps one after another with a countdown
            - Show if running late against a leave time
            - Track completion days
            - Start the routine from the alarm notification
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 339

**Intent:**
audiobook bookmarks and notes, i listen in the car

**Spec:**
```
Type:       Mobile application
Data model: Audiobook(id, title, author, file_path, position_s)
            Clip(id, audiobook_id -> Audiobook, at_s, voice_note_path, text)
Features:   - Play local audiobook files with chapter support
            - Bookmark with a big button or headphone press
            - Record a quick voice note on a bookmark
            - Remember position per book
            - Export notes
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, just_audio, audio_service, Drift
```

---

## Example 340

**Intent:**
visual timer for kids screen time, red disappearing circle

**Spec:**
```
Type:       Mobile application (kids)
Features:   - Set a timer with a shrinking red disc
            - Use large simple controls for kids
            - Play a gentle sound at the end
            - Show "5 minutes left" warning
            - Lock the timer with a parent PIN
Storage:    SharedPreferences
Tech stack: Kotlin, Jetpack Compose (Canvas)
```

---

## Example 341

**Intent:**
baby sign language words to teach

**Spec:**
```
Type:       Mobile application
Data model: Sign(id, word, category, video_path)
            Learned(sign_id -> Sign, first_used_on)
Features:   - Show videos for common baby signs
            - Group signs by category like food and family
            - Mark when the baby first uses a sign
            - Suggest signs to learn next
            - Show progress
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-av, expo-sqlite
```

---

## Example 342

**Intent:**
record when my kid loses each tooth

**Spec:**
```
Type:       Mobile application
Data model: Child(id, name)
            Tooth(id, child_id -> Child, position, lost_on, erupted_on, photo_path)
Features:   - Tap teeth on a mouth diagram
            - Record lost and new teeth dates
            - Add photos
            - Show the tooth fairy history
            - Show age at each tooth
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 343

**Intent:**
family emergency plan app with meeting point and contacts offline

**Spec:**
```
Type:       Mobile application (offline)
Data model: Member(id, name, phone, medical_notes)
            MeetingPoint(id, name, lat, lng, kind)
            ChecklistItem(id, title, done)
Features:   - Store family contacts and medical notes
            - Save local and out-of-town meeting points
            - Keep an emergency kit checklist
            - Show everything offline
            - Share the plan as a PDF
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, pdf, Hive
```

---

## Example 344

**Intent:**
instructions for my cat sitter, food amounts, meds, vet number

**Spec:**
```
Type:       Mobile application
Data model: Pet(id, name, food, amount_g, times, meds, quirks)
            Contact(id, name, phone, role)
            VisitLog(id, visited_at, fed, litter_cleaned, note, photo_path)
Features:   - Write care instructions per pet
            - Share instructions as a link or PDF
            - Let the sitter check off feeding and litter
            - Receive visit photos
            - Store vet and emergency contacts
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-print, expo-sqlite
```

---

## Example 345

**Intent:**
cat food and litter stock so i order before it runs out

**Spec:**
```
Type:       Mobile application
Data model: Supply(id, name, unit, quantity, daily_use, reorder_url)
Features:   - Track supply quantities
            - Estimate days left from daily use
            - Notify when supplies run low
            - Open the reorder link
            - Log purchases
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 346

**Intent:**
dog friendly places near me

**Spec:**
```
Type:       Mobile application with backend
Auth:       Sign in with Google or Apple
Data model: Place(id, name, lat, lng, category, water_bowl, off_leash)
            Review(id, place_id -> Place, user_id -> User, rating, text)
            User(id, name)
Features:   - Show dog-friendly cafes, parks and beaches on a map
            - Filter by off-leash and water available
            - Add new places
            - Review places
            - Save favourites
Storage:    Firebase Firestore with GeoFire queries
Tech stack: Flutter, Firebase, google_maps_flutter
```

---

## Example 347

**Intent:**
weather journal, i write the weather every day like my grandfather did

**Spec:**
```
Type:       Mobile application
Data model: WeatherDay(id, date, min_c, max_c, rain_mm, wind, sky, notes)
Features:   - Log daily min, max, rain and sky
            - Pre-fill values from a weather API
            - Compare the same day across years
            - Show monthly summaries
            - Export to CSV
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, WeatherKit, SwiftData
```

---

## Example 348

**Intent:**
babysitting hours and how much each family owes me

**Spec:**
```
Type:       Mobile application
Data model: Family(id, name, hourly_rate)
            Job(id, family_id -> Family, started_at, ended_at, kids, paid)
Features:   - Log babysitting jobs with start and end
            - Calculate pay per job from the family's rate
            - Track unpaid jobs
            - Show monthly earnings
            - Send a payment reminder message
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---

## Example 349

**Intent:**
stroke rehab hand exercise game on tablet

**Spec:**
```
Type:       Mobile game (rehabilitation)
Data model: Patient(id, name, affected_hand)
            Session(id, patient_id -> Patient, game, score, reaction_ms, played_at)
Features:   - Play reaching and tapping games that train hand movement
            - Adapt difficulty to the patient's reach
            - Measure reaction time and accuracy
            - Show progress for the therapist
            - Use large targets and calm colours
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Flame, Drift
```

---

## Example 350

**Intent:**
ramadan fasting times and log which days i fasted

**Spec:**
```
Type:       Mobile application
Data model: FastDay(id, date, fasted, missed_reason, made_up_on)
Features:   - Show suhoor and iftar times for the location
            - Notify before suhoor ends and at iftar
            - Log fasted and missed days
            - Track days to make up
            - Show Ramadan progress
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, adhan-java, Room
```

---

## Example 351

**Intent:**
saving for my kids college, want see how much i need and if im on track

**Spec:**
```
Type:       Mobile application
Data model: Child(id, name, birth_date, college_start_year)
            Fund(id, child_id -> Child, balance, monthly_contribution, expected_return)
            Deposit(id, fund_id -> Fund, amount, deposited_on)
Features:   - Estimate future college cost with tuition inflation
            - Project the fund balance to the start year
            - Show if each child is on track or short
            - Log deposits
            - Suggest the monthly amount needed
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Hive, fl_chart
```

---

## Example 352

**Intent:**
me and 3 roomates split rent and bills, who paid internet who paid electric, ugh its a mess

**Spec:**
```
Type:       Mobile application with backend
Auth:       Sign in with Google; join a household by invite code
Data model: Household(id, name)
            Roommate(id, household_id -> Household, name, share_percent)
            Bill(id, household_id -> Household, title, amount, due_on, paid_by -> Roommate)
            Settlement(id, from_id -> Roommate, to_id -> Roommate, amount, settled_on)
Features:   - Add shared bills and who paid them
            - Split bills by custom shares
            - Show who owes whom
            - Record settlements
            - Remind roommates of upcoming bills
Storage:    Supabase Postgres
Tech stack: React Native, Supabase
```

---

## Example 353

**Intent:**
commute log how long my drive to work takes each day so i can pick best time to leave

**Spec:**
```
Type:       Mobile application
Data model: Commute(id, direction, departed_at, arrived_at, route, traffic_note)
Features:   - Start and stop a commute with one tap or automatically by geofence
            - Record duration per route
            - Show average time by departure time
            - Suggest the best time to leave
            - Compare routes
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Geofencing API, Room
```

---

## Example 354

**Intent:**
stuttering practice app with slow speech and easy onset exercises

**Spec:**
```
Type:       Mobile application
Data model: Exercise(id, name, technique, text)
            Practice(id, exercise_id -> Exercise, recorded_at, wpm, self_rating, audio_path)
Features:   - Guide easy onset and slow speech exercises
            - Show a pacing bar for target syllables per second
            - Record practice and measure speaking rate
            - Rate fluency after each practice
            - Track practice minutes per day
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, AVFoundation, Speech framework, SwiftData
```

---

## Example 355

**Intent:**
daily bible devotional with reading plan

**Spec:**
```
Type:       Mobile application
Data model: Plan(id, name, days)
            PlanDay(id, plan_id -> Plan, day, passages)
            Completion(id, plan_day_id -> PlanDay, completed_on, reflection)
Features:   - Choose a reading plan like the Bible in a year
            - Show today's passages
            - Mark days complete and write a reflection
            - Catch up on missed days
            - Remind at a set time
Storage:    Bundled public-domain Bible text and progress in SQLite
Tech stack: Flutter, sqflite, flutter_local_notifications
```

---

## Example 356

**Intent:**
word of the day widget english

**Spec:**
```
Type:       Mobile application
Data model: Word(id, word, definition, example, part_of_speech, shown_on, saved)
Features:   - Show a new word each day
            - Display it on a home screen widget
            - Save words to a personal list
            - Quiz saved words weekly
Storage:    Bundled word list in SQLite
Tech stack: Kotlin, Jetpack Compose, Glance, Room
```

---

## Example 357

**Intent:**
garage sale app to price items and track what sold

**Spec:**
```
Type:       Mobile application
Data model: Item(id, name, price, photo_path, sold, sold_price, buyer_note)
Features:   - Add items with photo and price
            - Generate price stickers to print
            - Mark items sold with final price
            - Show total sales
            - Show unsold items for donation
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-print, expo-sqlite
```

---

## Example 358

**Intent:**
postcards collection from all over world

**Spec:**
```
Type:       Mobile application
Data model: Postcard(id, country, city, sender, received_on, front_photo, back_photo, stamp_note)
Features:   - Photograph both sides of each postcard
            - Record country, city and sender
            - Show postcards on a world map
            - Filter by country
            - Show count per country
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, MapKit, SwiftData
```

---

## Example 359

**Intent:**
fossil finds log with location and rock layer

**Spec:**
```
Type:       Mobile application
Data model: Fossil(id, name, taxon, period, formation, lat, lng, found_on, photo_path, size_mm)
Features:   - Log fossils with location and formation
            - Record geological period
            - Photograph with a scale bar
            - Show finds on a map
            - Export catalogue as CSV
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Google Maps SDK, Room
```

---

## Example 360

**Intent:**
insect photo collection, identify bugs i find in garden

**Spec:**
```
Type:       Mobile application (on-device ML)
Data model: Observation(id, photo_path, predicted_taxon, confidence, confirmed_taxon, observed_at, lat, lng)
Features:   - Photograph insects
            - Suggest species with an on-device image classifier
            - Confirm or correct the identification
            - Show a garden species list
            - Export observations to iNaturalist format
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, tflite_flutter, camera, Drift
```

---

## Example 361

**Intent:**
model railway layout inventory locos and wagons with dcc address

**Spec:**
```
Type:       Mobile application
Data model: Loco(id, name, maker, scale, dcc_address, photo_path)
            Wagon(id, name, maker, scale, photo_path)
            Service(id, loco_id -> Loco, serviced_on, notes)
Features:   - Catalogue locomotives and wagons
            - Store DCC addresses and decoders
            - Log servicing
            - Search by scale or maker
            - Show collection value
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 362

**Intent:**
fruit trees in my orchard, when to prune spray and pick

**Spec:**
```
Type:       Mobile application
Data model: Tree(id, kind, variety, rootstock, planted_on, row, position)
            Task(id, tree_id -> Tree, kind, done_on, notes)
            Harvest(id, tree_id -> Tree, kg, picked_on)
Features:   - Map trees by row and position
            - Show a seasonal calendar for pruning, spraying and thinning
            - Log tasks done per tree
            - Log harvests per tree
            - Compare yields per variety
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 363

**Intent:**
spice rack app what spices i have and when bought

**Spec:**
```
Type:       Mobile application
Data model: Spice(id, name, form, bought_on, jar_level, location)
Features:   - List spices with purchase date
            - Warn when spices are older than two years
            - Mark low jars and add them to a shopping list
            - Search before buying duplicates
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 364

**Intent:**
evening reflection 3 questions every night

**Spec:**
```
Type:       Mobile application
Data model: Reflection(id, date, went_well, could_improve, tomorrow_focus, energy)
Features:   - Ask three reflection questions each evening
            - Rate the day's energy
            - Show past reflections in a timeline
            - Remind at bedtime
            - Show weekly themes
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 365

**Intent:**
idea notebook, i talk and it saves the idea

**Spec:**
```
Type:       Mobile application
Data model: Idea(id, audio_path, transcript, tags, created_at, starred)
Features:   - Record a voice idea from a widget with one tap
            - Transcribe it on-device
            - Tag and star ideas
            - Search transcripts
            - Share an idea as text
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Glance, Android SpeechRecognizer, Room
```

---

## Example 366

**Intent:**
korean hangul learning with writing practice

**Spec:**
```
Type:       Mobile application
Data model: Jamo(id, char, romanization, stroke_order)
            Syllable(id, text, audio_path)
            Progress(id, item, correct_count, last_seen)
Features:   - Teach consonants and vowels with audio
            - Animate stroke order
            - Practise writing with a finger
            - Build syllables from letters
            - Quiz reading speed
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_tts, CustomPainter, Hive
```

---

## Example 367

**Intent:**
list of mountains i climbed, peak bagging

**Spec:**
```
Type:       Mobile application
Data model: Peak(id, name, height_m, region, lat, lng, list_name)
            Ascent(id, peak_id -> Peak, climbed_on, route, companions, photo_path)
Features:   - Load peak lists like the Munros
            - Mark peaks climbed with date and route
            - Show climbed and remaining peaks on a map
            - Show progress per list
            - Attach summit photos
Storage:    Bundled peak lists and ascents in SQLite
Tech stack: Swift, SwiftUI, MapKit, SwiftData
```

---

## Example 368

**Intent:**
kayak trip log with route and water conditions

**Spec:**
```
Type:       Mobile application
Data model: Trip(id, started_at, duration_min, distance_km, water_body, conditions, boat)
            TrackPoint(id, trip_id -> Trip, lat, lng, t)
Features:   - Record paddling routes with GPS
            - Log water and wind conditions
            - Show speed and distance
            - Save a float plan to share before leaving
            - List trips per boat
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Fused Location Provider, Room
```

---

## Example 369

**Intent:**
terrarium care log humidity and misting

**Spec:**
```
Type:       Mobile application
Data model: Terrarium(id, name, type, sealed)
            Reading(id, terrarium_id -> Terrarium, humidity, temp_c, read_at)
            Care(id, terrarium_id -> Terrarium, kind, done_on)
Features:   - Log humidity and temperature
            - Remind to mist open terrariums
            - Log trimming and cleaning
            - Show readings chart
            - Photo log per terrarium
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 370

**Intent:**
orchid rebloom tracker

**Spec:**
```
Type:       Mobile application
Data model: Orchid(id, name, genus, acquired_on, photo_path)
            Bloom(id, orchid_id -> Orchid, spike_on, first_flower_on, last_flower_on, flowers)
            Care(id, orchid_id -> Orchid, kind, done_on)
Features:   - Track spikes and blooms per orchid
            - Log watering and fertilising
            - Remind weekly watering
            - Show how long since the last bloom
            - Keep a photo timeline
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 371

**Intent:**
pill reminder that shows a picture of each pill so my grandad knows which one

**Spec:**
```
Type:       Mobile application (accessibility)
Data model: Pill(id, name, photo_path, color, shape, dose)
            DoseTime(id, pill_id -> Pill, time)
            Taken(id, dose_time_id -> DoseTime, taken_at)
Features:   - Show a photo of each pill to take now
            - Give a loud alarm and large confirm button
            - Read the pill name aloud
            - Notify a family member if a dose is missed
            - Let family set up pills behind a PIN
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, CameraX, AlarmManager, Room
```

---

## Example 372

**Intent:**
tinnitus relief sounds and log how loud the ringing is

**Spec:**
```
Type:       Mobile application
Data model: Sound(id, name, file_path, type)
            TinnitusLog(id, logged_at, loudness, annoyance, note)
Features:   - Play notched white noise and nature sounds
            - Match the tinnitus pitch with a tone generator
            - Log loudness and annoyance daily
            - Set a sleep timer
            - Show trends
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, just_audio, flutter_soloud, sqflite
```

---

## Example 373

**Intent:**
blood donation tracker when can i give again

**Spec:**
```
Type:       Mobile application
Data model: Donation(id, donated_on, type, centre, hemoglobin)
            Eligibility(type, wait_days)
Features:   - Log whole blood, plasma and platelet donations
            - Calculate the next eligible date by type
            - Notify when eligible
            - Show total donations and badges
            - Save hemoglobin results
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-notifications, expo-sqlite
```

---

## Example 374

**Intent:**
grief journal after my mom passed, prompts to write and memories

**Spec:**
```
Type:       Mobile application
Data model: Entry(id, written_on, prompt, text, mood)
            Memory(id, title, story, photo_path, date)
Features:   - Offer gentle daily writing prompts
            - Save memories with photos
            - Mark difficult dates like anniversaries with reminders
            - Keep everything private with a lock
            - Show a memory on chosen days
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, LocalAuthentication, SwiftData
```

---

## Example 375

**Intent:**
anger log, what made me angry and how i reacted

**Spec:**
```
Type:       Mobile application
Data model: Incident(id, occurred_at, trigger, intensity, reaction, consequence, better_response)
Features:   - Log incidents with trigger and intensity
            - Record reaction and a better response
            - Show common triggers
            - Offer a cool-down timer
            - Chart intensity over weeks
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 376

**Intent:**
vertigo exercises with timer, my doctor said do brandt daroff

**Spec:**
```
Type:       Mobile application
Data model: Exercise(id, name, steps, hold_s, reps)
            Session(id, exercise_id -> Exercise, done_at, dizziness_level)
Features:   - Guide Brandt-Daroff positions with pictures
            - Time each hold with voice cues
            - Rate dizziness after each session
            - Remind three times a day
            - Show improvement over days
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_tts, Hive
```

---

## Example 377

**Intent:**
yo can u make me a app 4 tracking my gains at gym but simple af, just bench squat deadlift

**Spec:**
```
Type:       Mobile application
Data model: Lift(id, name)
            Entry(id, lift_id -> Lift, weight_kg, reps, logged_on)
Features:   - Log bench, squat and deadlift sets
            - Show personal bests per lift
            - Calculate estimated one-rep max
            - Chart progress per lift
Storage:    AsyncStorage (on-device)
Tech stack: React Native, AsyncStorage
```

---

## Example 378

**Intent:**
plz app to remind drink water every hr but stop at night thx

**Spec:**
```
Type:       Mobile application
Data model: Settings(start_time, end_time, interval_min)
            Drink(id, logged_at, ml)
Features:   - Send water reminders every hour within waking hours
            - Stop reminders at night
            - Log a glass from the notification
            - Show today's glasses
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, WorkManager, DataStore
```

---

## Example 379

**Intent:**
need sumthing to track my sleep with my mi band data

**Spec:**
```
Type:       Mobile application (wearable companion)
Data model: SleepSession(id, start, end, deep_min, light_min, rem_min, awake_min)
            Note(id, date, text)
Features:   - Read sleep sessions synced to Health Connect from the band
            - Show sleep stages per night
            - Show a weekly average
            - Add notes on nights
            - Compare bedtime consistency
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Health Connect API, Room
```

---

## Example 380

**Intent:**
i want app for my garmin watch to show my plant watering reminders lol

**Spec:**
```
Type:       Mobile application (wearable companion)
Data model: Plant(id, name, water_every_days, last_watered)
Features:   - Keep plant watering schedules on the phone
            - Send due plants to the watch
            - Show a widget on the Garmin watch
            - Mark a plant watered from the watch
Storage:    Local on-device database (SQLite)
Tech stack: Garmin Connect IQ (Monkey C) watch widget, Kotlin Android companion app, Connect IQ Mobile SDK
```

---

## Example 381

**Intent:**
pixel watch app to log my coffee with a tap

**Spec:**
```
Type:       Mobile application (Wear OS)
Data model: Coffee(id, kind, caffeine_mg, logged_at)
Features:   - Log a coffee from a watch tile
            - Choose coffee type with a rotary input
            - Show today's cups and caffeine
            - Sync logs to the phone app
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Compose for Wear OS, Tiles API, Wearable Data Layer, Room
```

---

## Example 382

**Intent:**
galaxy watch interval timer that vibrates for running intervals

**Spec:**
```
Type:       Mobile application (Wear OS)
Data model: Workout(id, name, run_s, walk_s, rounds)
Features:   - Create run/walk interval workouts on the phone
            - Run the timer on the watch
            - Vibrate at each switch
            - Show heart rate during the workout
            - Save the workout to Health Connect
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Compose for Wear OS, Health Services, Health Connect
```

---

## Example 383

**Intent:**
can u make it in swiftui, a tracker for how many days i went outside for a walk

**Spec:**
```
Type:       Mobile application
Data model: Walk(id, date, minutes, steps)
Features:   - Mark days with a walk outside
            - Read walking minutes from HealthKit
            - Show a month calendar of walk days
            - Keep a streak
            - Remind if no walk by evening
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, HealthKit, SwiftData
```

---

## Example 384

**Intent:**
flutter app for counting how many books my class read, im a teacher, kids dont have phones so only on my tablet

**Spec:**
```
Type:       Mobile application (tablet, offline)
Data model: Student(id, name, avatar)
            BookRead(id, student_id -> Student, title, finished_on, rating)
Features:   - Add students with avatars
            - Log books each student finished
            - Show a class reading wall
            - Award reading badges
            - Export a term report
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift, pdf
```

---

## Example 385

**Intent:**
jetpack compose app to track my plant cuttings rooting in water

**Spec:**
```
Type:       Mobile application
Data model: Cutting(id, plant_name, taken_on, method, rooted_on, potted_on, photo_path)
Features:   - Log cuttings with date and method
            - Mark when roots appear
            - Remind to change the water weekly
            - Show days to root per plant
            - Keep photos
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, WorkManager
```

---

## Example 386

**Intent:**
react native app where i log my kid's allergic reactions to foods

**Spec:**
```
Type:       Mobile application
Data model: Food(id, name)
            Reaction(id, food_id -> Food, occurred_at, symptoms, severity, treatment, photo_path)
Features:   - Log reactions with food, symptoms and severity
            - Attach photos of rashes
            - Record treatment like antihistamine
            - Show suspected foods ranked
            - Export for the allergist
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-image-picker, expo-sqlite
```

---

## Example 387

**Intent:**
ionic app for my diving club to keep our own dive logs offline

**Spec:**
```
Type:       Mobile application (offline)
Data model: Diver(id, name, cert_level)
            Dive(id, diver_id -> Diver, site, dived_on, max_depth_m, duration_min, air_start_bar, air_end_bar)
Features:   - Log dives with depth, time and air used
            - Calculate air consumption rate
            - Show totals per diver
            - Export logs as CSV
            - Work offline on the boat
Storage:    Local on-device database (SQLite)
Tech stack: Ionic, Angular, Capacitor, SQLite plugin
```

---

## Example 388

**Intent:**
kotlin multiplatform app for both iphone and android, simple reading streak

**Spec:**
```
Type:       Mobile application
Data model: ReadingDay(id, date, minutes, book_title)
Features:   - Log reading minutes per day
            - Keep a streak
            - Remind at a set time
            - Show weekly minutes chart
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin Multiplatform, Compose Multiplatform, SQLDelight
```

---

## Example 389

**Intent:**
.NET MAUI app tracking my medications for my heart condition

**Spec:**
```
Type:       Mobile application
Data model: Medication(id, name, dose, times)
            DoseLog(id, medication_id -> Medication, taken_at)
            Vital(id, pulse, systolic, diastolic, measured_at)
Features:   - Schedule medication reminders
            - Mark doses as taken
            - Log pulse and blood pressure
            - Show a weekly adherence chart
            - Export data for the cardiologist
Storage:    Local on-device database (SQLite)
Tech stack: C#, .NET MAUI, sqlite-net-pcl, Plugin.LocalNotification
```

---

## Example 390

**Intent:**
want offline expense app in swift, multiple currencies because i live between 2 countries

**Spec:**
```
Type:       Mobile application
Data model: Account(id, name, currency)
            Expense(id, account_id -> Account, amount, currency, category, spent_on)
            Rate(base, target, rate, fetched_on)
Features:   - Log expenses in any currency
            - Convert totals to a home currency
            - Cache exchange rates for offline use
            - Show spending per country and category
            - Export CSV
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData, Frankfurter API
```

---

## Example 391

**Intent:**
Hello, I am from Brazil and I want app for practice my english pronunciation, I speak and app say if is correct.

**Spec:**
```
Type:       Mobile application
Data model: Phrase(id, text, level, audio_path)
            Attempt(id, phrase_id -> Phrase, transcript, score, attempted_at)
Features:   - Show phrases by level with native audio
            - Record the user speaking
            - Compare the transcript with the target phrase
            - Highlight mispronounced words
            - Track scores over time
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, speech_to_text, just_audio, sqflite
```

---

## Example 392

**Intent:**
Good day. I am retired and want to note my garden birds and the weather each day, my eyes are not so good, please big letters.

**Spec:**
```
Type:       Mobile application (accessibility)
Data model: Day(id, date, weather, temp_c)
            BirdSeen(id, day_id -> Day, species, count)
Features:   - Use large text and high-contrast buttons
            - Log birds seen with big counters
            - Fill in weather automatically
            - Show the month's birds
            - Read entries aloud
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Open-Meteo API, Room, TextToSpeech
```

---

## Example 393

**Intent:**
I am student from Vietnam, I need app to remember the new words in my class with picture

**Spec:**
```
Type:       Mobile application
Data model: Word(id, word, meaning_vi, image_path, example, lesson)
            Review(id, word_id -> Word, reviewed_at, correct, next_due)
Features:   - Add words with a photo and Vietnamese meaning
            - Group words by lesson
            - Review with picture flashcards
            - Schedule reviews with spaced repetition
            - Pronounce words aloud
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-image-picker, expo-speech, expo-sqlite
```

---

## Example 394

**Intent:**
Please app for count my steps and my wife steps in same phone, we share one phone

**Spec:**
```
Type:       Mobile application
Data model: Person(id, name, daily_goal)
            StepRecord(id, person_id -> Person, date, steps)
Features:   - Switch the active walker with one tap
            - Count steps with the phone sensor for the active person
            - Show each person's daily total
            - Show a weekly chart per person
            - Celebrate reached goals
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, SensorManager (step counter), Room
```

---

## Example 395

**Intent:**
I want to make application where I write my daily spends in rupees and see where all my salary going each month

**Spec:**
```
Type:       Mobile application
Data model: Category(id, name, icon)
            Spend(id, category_id -> Category, amount_inr, note, spent_on, payment_mode)
            Salary(id, month, amount_inr)
Features:   - Log daily spends in rupees with category
            - Record UPI, card or cash
            - Show monthly breakdown as a pie chart
            - Compare spending with salary
            - Show top categories
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Hive, fl_chart
```

---

## Example 396

**Intent:**
Bonjour, I search an app for my diabetic cat to note the glucose and insulin, my vet ask me

**Spec:**
```
Type:       Mobile application
Data model: Cat(id, name)
            Glucose(id, cat_id -> Cat, value_mg_dl, measured_at)
            Insulin(id, cat_id -> Cat, units, given_at)
Features:   - Log glucose readings and insulin doses
            - Build a glucose curve for a day
            - Remind injection times
            - Send a report to the vet by email
            - Show weekly averages
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Swift Charts, MessageUI, SwiftData
```

---

## Example 397

**Intent:**
Is possible to make app for my son with asthma where school teacher also can see when he use inhaler?

**Spec:**
```
Type:       Mobile application with backend
Auth:       Parent account; teacher invited by email with read-only access
Data model: Child(id, name)
            Guardian(id, child_id -> Child, email, role)
            InhalerUse(id, child_id -> Child, puffs, used_at, logged_by, reason)
Features:   - Log inhaler use from parent or teacher phones
            - Show today's uses to all guardians
            - Notify parents when the teacher logs a use
            - Show weekly use trends
            - Export a report for the doctor
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase Auth, Firestore, FCM
```

---

## Example 398

**Intent:**
Hallo, I need a app to plan my weekly swim training, I am in swim club masters

**Spec:**
```
Type:       Mobile application
Data model: Workout(id, date, total_m)
            WorkoutSet(id, workout_id -> Workout, reps, distance_m, stroke, interval_s, intensity)
Features:   - Build workouts as sets with distance, stroke and interval
            - Calculate total distance
            - Show a weekly training plan
            - Mark workouts done
            - Show monthly distance
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 399

**Intent:**
ok long story but my wife and i are trying for a baby for 2 years now and we do ivf, there is so many injections at exact times and appointments and i want one place where we both see the schedule and tick off the shots, and maybe also note how she feels each day because the doctor asks

**Spec:**
```
Type:       Mobile application with backend
Auth:       Shared couple account with invite link
Data model: Cycle(id, started_on, protocol)
            Injection(id, cycle_id -> Cycle, medication, dose, scheduled_at, given_at, given_by)
            Appointment(id, cycle_id -> Cycle, kind, at, notes)
            Wellbeing(id, cycle_id -> Cycle, date, mood, symptoms)
Features:   - Schedule injections at exact times with alarms on both phones
            - Tick off shots and record who gave them
            - List clinic appointments
            - Log daily mood and symptoms
            - Show the full cycle timeline
Storage:    Firebase Firestore with offline persistence
Tech stack: React Native, Firebase Auth, Firestore, Notifee
```

---

## Example 400

**Intent:**
so I've been running a little Instagram for my sourdough and now people ask me for my bake schedule, and honestly I just want an app on my phone where I put the time I want bread ready and it tells me backwards when to feed starter, mix, fold and shape, with alarms for each step

**Spec:**
```
Type:       Mobile application
Data model: Schedule(id, ready_at, recipe_name)
            Step(id, schedule_id -> Schedule, name, at, duration_min, done)
Features:   - Enter the time bread should be ready
            - Calculate step times backwards from fixed durations
            - Set an alarm for each step
            - Adjust durations for kitchen temperature
            - Save recipes as step templates
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_local_notifications, Hive
```

---

## Example 401

**Intent:**
my father is 78 and lives alone, he walks his dog every morning, and i'm always worried. i'd like him to just press one button on his phone when he's back home safe and if he doesn't by 10am i get a message. he's not good with phones so it must be very simple

**Spec:**
```
Type:       Mobile application with backend
Data model: Senior(id, name, deadline_time)
            CheckIn(id, senior_id -> Senior, checked_in_at)
            Watcher(id, senior_id -> Senior, phone)
Features:   - Show one large "I'm home" button
            - Record the daily check-in
            - Send an SMS to family if no check-in by the deadline
            - Let family change the deadline remotely
            - Show check-in history to family
API:        REST
            POST /checkins
            GET /seniors/{id}/status
Storage:    PostgreSQL
Tech stack: Kotlin (Android app), Python FastAPI backend, Twilio SMS, scheduled job
```

---

## Example 402

**Intent:**
i've got about 40 houseplants now (yes i know) and some are in my bedroom some living room some office, and the thing that kills me is fertilizing because each needs different amounts in growing season vs winter. app to handle that and not water too, i already have one for water

**Spec:**
```
Type:       Mobile application
Data model: Plant(id, name, room, fertilizer_id -> Fertilizer, dose_ml_per_l, growing_interval_weeks, dormant_interval_weeks)
            Fertilizer(id, name, npk)
            FeedLog(id, plant_id -> Plant, fed_on, dose_ml)
Features:   - Set fertiliser type and dose per plant
            - Switch intervals for growing and dormant season by month
            - Show plants to feed today grouped by room
            - Log feedings
            - Calculate fertiliser to mix for a watering can
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room, WorkManager
```

---

## Example 403

**Intent:**
background: im a phd student, i read like 10 papers a week on my phone and lose track. want an app to keep a reading list of pdfs, highlight, take notes, and tag by project. all on my phone offline, cloud is not allowed at my lab

**Spec:**
```
Type:       Mobile application (offline)
Data model: Paper(id, title, authors, year, file_path, status)
            Tag(id, name)
            PaperTag(paper_id -> Paper, tag_id -> Tag)
            Annotation(id, paper_id -> Paper, page, text, note, color)
Features:   - Import PDFs and extract title metadata
            - Highlight text and add notes in the reader
            - Tag papers by project
            - Track to-read, reading and done status
            - Export notes as BibTeX and Markdown
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, PDFKit, SwiftData
```

---

## Example 404

**Intent:**
we are a family of 5, 3 kids with different allergies (nuts, egg, dairy) and every time i shop or cook i have to check everything. i want an app where i scan a product and it tells me which of my kids can eat it

**Spec:**
```
Type:       Mobile application
Data model: Member(id, name, allergens)
            Product(id, barcode, name, allergens, traces)
            Scan(id, product_id -> Product, scanned_at)
Features:   - Store allergens per family member
            - Scan products and read allergens from Open Food Facts
            - Show per child if the product is safe
            - Warn on "may contain" traces
            - Keep a list of safe products
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, mobile_scanner, Open Food Facts API, Drift
```

---

## Example 405

**Intent:**
So my therapist wants me to track my sleep, mood, and when I take my ADHD meds to see if the timing affects my evening crash. I tried spreadsheets but I never do it. Something with a home screen widget would be nice because I live on my home screen

**Spec:**
```
Type:       Mobile application
Data model: MedDose(id, medication, mg, taken_at)
            MoodCheck(id, at, mood, focus, energy)
            SleepNight(id, bed_at, wake_at, quality)
Features:   - Log meds and mood from a home screen widget
            - Prompt short mood check-ins three times a day
            - Log sleep each morning
            - Show mood across the day relative to dose time
            - Export a summary for the therapist
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, WidgetKit, App Intents, SwiftData
```

---

## Example 406

**Intent:**
i do photography as a hobby and when i do portraits outside i always forget which locations had good light at which time of day. i want to save spots with photos, the sun direction, and notes like "good at 5pm in may"

**Spec:**
```
Type:       Mobile application
Data model: Spot(id, name, lat, lng, facing_deg, notes)
            SpotPhoto(id, spot_id -> Spot, file_path, taken_at, sun_azimuth, sun_altitude)
Features:   - Save spots with GPS and compass facing
            - Record sun position automatically for each photo
            - Show which spots get good light at a chosen time
            - Show spots on a map
            - Search notes
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Google Maps SDK, SunCalc port, Room
```

---

## Example 407

**Intent:**
ok this is weird but i collect bus tickets and train tickets from every city i visit, around 300, and want to catalog them with scan, city, date, transport type and see a map

**Spec:**
```
Type:       Mobile application
Data model: Ticket(id, city, country, transport_type, operator, travel_date, front_path, back_path)
Features:   - Scan tickets front and back with auto-cropping
            - Record city, operator and transport type
            - Show collected cities on a map
            - Filter by transport type
            - Show tickets per country
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, edge_detection, flutter_map, Drift
```

---

## Example 408

**Intent:**
my husband travels for work a lot and our kids (4 and 6) miss him. i want an app where he can record a bedtime story video or audio and the kids can play it at night with just one big picture button, kids cant read yet

**Spec:**
```
Type:       Mobile application with backend
Auth:       Parent accounts; kids' tablet paired with a code
Data model: Family(id, name)
            Recording(id, family_id -> Family, recorded_by, title, media_url, cover_image, created_at)
            Play(id, recording_id -> Recording, played_at)
Features:   - Let a parent record a video or audio story on their phone
            - Upload recordings to the family
            - Show stories on the kids' tablet as large picture buttons
            - Play with one tap and no menus
            - Show parents when a story was played
Storage:    Firebase Storage and Firestore
Tech stack: React Native, Firebase Storage, Firestore, expo-av
```

---

## Example 409

**Intent:**
guitar pedal board planner

**Spec:**
```
Type:       Mobile application
Data model: Pedal(id, brand, name, type, width_mm, depth_mm, current_ma, voltage)
            Board(id, name, width_mm, depth_mm, psu_ma)
            Placement(board_id -> Board, pedal_id -> Pedal, x_mm, y_mm, chain_position)
Features:   - Add pedals with dimensions and power draw
            - Drag pedals onto a scaled board
            - Order the signal chain
            - Check total current against the power supply
            - Save several board layouts
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Drift
```

---

## Example 410

**Intent:**
houseplant repotting log

**Spec:**
```
Type:       Mobile application
Data model: Plant(id, name)
            Repot(id, plant_id -> Plant, repotted_on, old_pot_cm, new_pot_cm, soil, root_condition)
Features:   - Log repots with pot size and soil
            - Note root condition
            - Remind to check yearly
            - Show pot size history
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, SwiftData
```

---

## Example 411

**Intent:**
kids pocket camera photo diary, no internet no sharing

**Spec:**
```
Type:       Mobile application (kids, offline)
Data model: Photo(id, file_path, taken_at, sticker)
            Album(id, name)
Features:   - Take photos with a simple big shutter button
            - Add fun stickers and frames
            - Sort photos into albums
            - Keep everything on the device with no sharing
            - Let parents export photos behind a PIN
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, CameraX, Room
```

---

## Example 412

**Intent:**
trivia quiz with my own questions for family game night offline

**Spec:**
```
Type:       Mobile game (offline)
Data model: Category(id, name)
            Question(id, category_id -> Category, text, answer, options, points)
            Team(id, name, score)
Features:   - Create categories and questions
            - Run a Jeopardy-style board
            - Track team scores
            - Show a timer for answers
            - Import questions from CSV
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite
```

---

## Example 413

**Intent:**
shell collection from beaches with where i found them

**Spec:**
```
Type:       Mobile application
Data model: Shell(id, species_guess, beach, lat, lng, found_on, size_mm, photo_path)
Features:   - Photograph shells
            - Save beach and GPS location
            - Show beaches on a map
            - Group shells by species
            - Show finds per trip
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, image_picker, flutter_map, Hive
```

---

## Example 414

**Intent:**
funko pop collection with box number and value

**Spec:**
```
Type:       Mobile application
Data model: Pop(id, name, series, box_number, exclusive, in_box, paid, value, photo_path)
Features:   - Add Pops by box number and series
            - Mark exclusives and in-box condition
            - Track price paid and current value
            - Show a wishlist
            - Show collection value
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 415

**Intent:**
side hustle income and hours, i do dog walking and tutoring

**Spec:**
```
Type:       Mobile application
Data model: Gig(id, name, rate_type)
            Job(id, gig_id -> Gig, date, hours, income, expenses)
Features:   - Log jobs per side hustle
            - Calculate hourly earnings after expenses
            - Compare hustles side by side
            - Estimate tax to set aside
            - Show monthly income
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, Swift Charts, SwiftData
```

---

## Example 416

**Intent:**
coupon and promo codes saver with expiry

**Spec:**
```
Type:       Mobile application
Data model: Coupon(id, store, code, discount, expires_on, photo_path, used)
Features:   - Save promo codes and photographed coupons
            - Copy a code with one tap
            - Notify before coupons expire
            - Hide used coupons
            - Search by store
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-clipboard, expo-sqlite
```

---

## Example 417

**Intent:**
trail running log with elevation and how my legs felt

**Spec:**
```
Type:       Mobile application
Data model: TrailRun(id, date, distance_km, elevation_gain_m, duration_s, terrain, leg_feel, gpx_path)
Features:   - Import GPX files from a watch
            - Show distance, elevation and grade-adjusted pace
            - Rate how legs felt
            - Show weekly vertical
            - Compare runs on the same trail
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, gpx, Drift, fl_chart
```

---

## Example 418

**Intent:**
sleep hygiene checklist before bed

**Spec:**
```
Type:       Mobile application
Data model: Habit(id, name)
            NightCheck(id, date, habit_id -> Habit, done)
            SleepRating(id, date, quality)
Features:   - Show a bedtime checklist like no screens and cool room
            - Rate sleep next morning
            - Find which habits relate to better sleep
            - Remind an hour before bed
Storage:    Local on-device database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 419

**Intent:**
contraceptive pill reminder that knows about the 7 day break

**Spec:**
```
Type:       Mobile application
Data model: Pack(id, started_on, active_days, break_days)
            PillTaken(id, pack_id -> Pack, day, taken_at)
Features:   - Remind daily at a set time
            - Handle 21/7 and continuous pack schedules
            - Skip reminders during the break week
            - Warn if a pill is more than 12 hours late
            - Remind to start a new pack
Storage:    Local on-device database (SQLite)
Tech stack: Swift, SwiftUI, UserNotifications, SwiftData
```

---

## Example 420

**Intent:**
smart ring sleep data import oura and show my own charts

**Spec:**
```
Type:       Mobile application (wearable companion)
Data model: SleepDay(id, date, score, hrv_ms, resting_hr, total_sleep_min)
            Tag(id, date, name)
Features:   - Import daily sleep data from the Oura API
            - Chart HRV and resting heart rate trends
            - Tag days with events like travel or alcohol
            - Compare averages with and without tags
            - Cache data on the device
Storage:    Local on-device database (SQLite)
Tech stack: React Native, Oura API v2, expo-sqlite, Victory Native
```

---

## Example 421

**Intent:**
kayak... no wait canoe camping packing by weight, i need to keep total under 30kg

**Spec:**
```
Type:       Mobile application
Data model: Gear(id, name, weight_g, category)
            Trip(id, name, max_kg)
            TripGear(trip_id -> Trip, gear_id -> Gear, quantity, packed)
Features:   - Keep a gear list with weights
            - Build a trip list and total the weight
            - Warn when over the weight limit
            - Show weight by category
            - Check off packed items
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite
```

---
