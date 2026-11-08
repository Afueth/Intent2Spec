## Example 1

**Intent:**
analyse my class test scores

**Spec:**
```
Type:       Data analysis script (grade analysis)
Features:   - Load student scores from a CSV file
            - Compute mean, median and standard deviation per test
            - Flag students scoring below the pass mark
            - Plot a histogram of scores for each test
            - Export a summary table to Excel
Input:      CSV file with columns: student_id, student_name, test_name, score, max_score
Tech stack: Python, pandas, matplotlib, openpyxl
```

---

## Example 2

**Intent:**
I'm a high school maths teacher and every term I end up with three spreadsheets of quiz marks, homework marks and exam marks. I'd love something that combines them with my weightings and tells me who improved and who is slipping compared to last term.

**Spec:**
```
Type:       Data analysis script (weighted grade tracking)
Features:   - Merge quiz, homework and exam spreadsheets on student ID
            - Apply configurable weightings to compute a term grade
            - Compare each student's term grade with the previous term
            - Flag students whose grade dropped by more than 10 percent
            - Generate a per-class report with improvers and decliners
Input:      Three Excel files (quizzes, homework, exams) plus last term's grade file
Tech stack: Python, pandas, openpyxl
```

---

## Example 3

**Intent:**
dashboard showing school attendance trends by week and year group

**Spec:**
```
Type:       Data dashboard (school attendance)
Data model: Student(id, name, year_group, form)
            AttendanceRecord(id, student_id -> Student, date, session, status)
Features:   - Show weekly attendance rate per year group as a line chart
            - Highlight students with attendance below 90 percent
            - Filter by form, year group and date range
            - Compare this term with the same term last year
            - Export a list of persistent absentees to CSV
Storage:    PostgreSQL
Tech stack: Python, Streamlit, pandas, Plotly
```

---

## Example 4

**Intent:**
hospital ER wait time analysis from our triage log

**Spec:**
```
Type:       Data analysis script (emergency department wait times)
Features:   - Load triage and discharge timestamps from the log export
            - Calculate door-to-doctor and total length-of-stay times
            - Break down wait times by triage category and hour of day
            - Identify the busiest hours using a heatmap
            - Report the share of patients seen within the 4-hour target
Input:      CSV export with columns: visit_id, arrival_time, triage_time, seen_time, discharge_time, triage_category
Tech stack: Python, pandas, seaborn
```

---

## Example 5

**Intent:**
predict how much electricity our office building will use tomorrow

**Spec:**
```
Type:       Machine learning model (energy usage forecasting)
Features:   - Load hourly smart meter readings and local weather data
            - Engineer features such as hour, weekday, holiday flag and outdoor temperature
            - Train a gradient boosting regressor for next-day hourly usage
            - Evaluate with mean absolute percentage error on a held-out month
            - Output a 24-hour forecast with prediction intervals
Input:      CSV of hourly kWh readings and a weather history CSV
Tech stack: Python, pandas, LightGBM, scikit-learn
```

---

## Example 6

**Intent:**
i have years of farm data rainfall fertilizer and harvest, can a computer guess how much wheat ill get this year

**Spec:**
```
Type:       Machine learning model (crop yield prediction)
Features:   - Combine field records, rainfall totals and fertilizer amounts per season
            - Train a random forest regressor on past harvests
            - Show which factors matter most using feature importance
            - Predict this season's yield per field with an error range
            - Export predictions to a spreadsheet
Input:      Excel files with field, season, rainfall_mm, fertilizer_kg_per_ha, sowing_date, yield_t_per_ha
Tech stack: Python, pandas, scikit-learn, openpyxl
```

---

## Example 7

**Intent:**
count cars and trucks passing in a traffic camera video

**Spec:**
```
Type:       Machine learning model (vehicle counting from video)
Features:   - Detect vehicles in each video frame with a pretrained object detector
            - Track vehicles across frames to avoid double counting
            - Count vehicles crossing a user-defined line, split by class
            - Export counts per 15-minute interval to CSV
            - Save an annotated video with bounding boxes and counts
Input:      MP4 video file and the coordinates of the counting line
Tech stack: Python, YOLOv8 (Ultralytics), ByteTrack, OpenCV
```

---

## Example 8

**Intent:**
We put trail cameras in the forest and have 40,000 photos. Most are empty. Can you sort out which ones have animals and what species?

**Spec:**
```
Type:       Machine learning model (camera-trap image classification)
Features:   - Filter out empty frames with an animal detection model
            - Classify detected animals into species with a fine-tuned image classifier
            - Write each image's species and confidence to a CSV
            - Move low-confidence images to a folder for manual review
            - Summarise detections per camera and per species
Input:      Folders of JPEG images organised by camera ID, with EXIF timestamps
Tech stack: Python, PyTorch, MegaDetector, timm (EfficientNet)
```

---

## Example 9

**Intent:**
detect scratches on metal parts from our production line camera

**Spec:**
```
Type:       Machine learning model (visual defect detection)
Data model: Inspection(id, part_serial, image_path, captured_at, defect_score, result)
            DefectRegion(id, inspection_id -> Inspection, x, y, width, height, defect_type)
Features:   - Capture images from the line camera when a part passes the sensor
            - Run a defect segmentation model to locate scratches and dents
            - Mark parts as pass or fail using a configurable score threshold
            - Store inspection results with defect regions
            - Show daily defect rates per shift
Storage:    PostgreSQL (results), local disk (images)
Tech stack: Python, PyTorch, OpenCV, FastAPI
```

---

## Example 10

**Intent:**
turn recordings of our team meetings into written notes with action items

**Spec:**
```
Type:       Data pipeline (meeting transcription and summarisation)
Features:   - Transcribe uploaded audio with speaker diarization
            - Split the transcript by speaker with timestamps
            - Summarise key decisions with a language model
            - Extract action items with owner and due date
            - Email the notes to all attendees
Input:      Audio files (MP3, M4A, WAV) from meeting recordings
Storage:    S3 (audio), PostgreSQL (transcripts and notes)
Tech stack: Python, OpenAI Whisper, pyannote.audio, Claude API
```

---

## Example 11

**Intent:**
sentiment of the reviews on our product pages

**Spec:**
```
Type:       Data analysis script (product review sentiment)
Features:   - Load reviews exported from the shop platform
            - Classify each review as positive, neutral or negative with a pretrained transformer
            - Extract the most common complaint phrases from negative reviews
            - Chart sentiment per product and per month
            - Export results to CSV
Input:      CSV with columns: review_id, product_id, rating, review_text, created_at
Tech stack: Python, Hugging Face Transformers, pandas, matplotlib
```

---

## Example 12

**Intent:**
We get hundreds of CVs per job posting. I want a tool to rank them against the job description, but HR is worried about bias, so it must check that it doesn't treat women or older applicants unfairly.

**Spec:**
```
Type:       Web application (resume screening with fairness checks)
Data model: JobPosting(id, title, description, requirements)
            Resume(id, job_id -> JobPosting, file_path, parsed_text, match_score)
            FairnessReport(id, job_id -> JobPosting, metric, group, value, created_at)
Features:   - Parse uploaded PDF and DOCX resumes into text
            - Score resumes against the job description using embeddings
            - Remove names, photos and birth dates before scoring
            - Compute selection rates by gender and age band and flag disparate impact
            - Show a ranked shortlist with the reasons for each score
Storage:    PostgreSQL
Tech stack: Python, FastAPI, sentence-transformers, Fairlearn, React
```

---

## Example 13

**Intent:**
flag suspicious card transactions for our small bank

**Spec:**
```
Type:       Machine learning model (transaction fraud detection)
Features:   - Engineer features such as amount deviation, merchant category and time since last transaction
            - Train an XGBoost classifier on labelled historical fraud cases
            - Handle class imbalance with class weights
            - Score new transactions in real time through an API
            - Send high-risk transactions to an analyst review queue
Storage:    PostgreSQL
Tech stack: Python, XGBoost, FastAPI, Kafka
```

---

## Example 14

**Intent:**
why are our gym members cancelling

**Spec:**
```
Type:       Data analysis script (membership churn analysis)
Features:   - Load member, visit and cancellation data
            - Compare visit frequency in the 60 days before cancellation with active members
            - Break down churn rate by membership plan, age band and join month
            - Fit a logistic regression to find the strongest churn drivers
            - Produce a short PDF report with charts
Input:      CSV exports of members, check-ins and cancellations
Tech stack: Python, pandas, statsmodels, matplotlib
```

---

## Example 15

**Intent:**
how many of each item should my bakery bake tomorrow based on past sales

**Spec:**
```
Type:       Machine learning model (bakery demand forecasting)
Features:   - Load daily sales per item from the till export
            - Add weekday, holiday and weather features
            - Train a forecasting model per item
            - Predict tomorrow's demand and add a safety margin
            - Print a bake list with quantities per item
Input:      Daily POS export (CSV) with date, item, quantity_sold, quantity_wasted
Tech stack: Python, pandas, Prophet
```

---

## Example 16

**Intent:**
did our new checkout button actually increase sales or was it luck

**Spec:**
```
Type:       Data analysis script (A/B test analysis)
Features:   - Load visitor-level experiment data with variant and conversion
            - Compute conversion rate and confidence interval per variant
            - Run a two-proportion z-test for significance
            - Check for sample ratio mismatch between variants
            - Report the uplift with a plain-language conclusion
Input:      CSV with columns: user_id, variant, converted, revenue
Tech stack: Python, pandas, SciPy, statsmodels
```

---

## Example 17

**Intent:**
we did a staff survey with a comment box and got 900 comments, too many to read, group them into themes please

**Spec:**
```
Type:       Data analysis script (survey open-text clustering)
Features:   - Clean and deduplicate the free-text answers
            - Embed each comment with a sentence embedding model
            - Cluster comments into themes with HDBSCAN
            - Label each theme with its top keywords and three example comments
            - Export themes with counts to Excel
Input:      Excel file with one comment per row
Tech stack: Python, sentence-transformers, BERTopic, pandas
```

---

## Example 18

**Intent:**
track what hashtags are trending about our city on social media every day

**Spec:**
```
Type:       Scheduled script (social media trend tracking)
Data model: Post(id, platform, text, hashtags, posted_at, likes)
            TrendSnapshot(id, date, hashtag, mention_count, growth_rate)
Features:   - Collect public posts mentioning the city through platform APIs every hour
            - Extract and normalise hashtags
            - Compute daily mention counts and growth compared with the 7-day average
            - Flag hashtags with sudden spikes
            - Send a daily trend digest by email
Storage:    PostgreSQL
Tech stack: Python, Mastodon API, Reddit API (PRAW), APScheduler
```

---

## Example 19

**Intent:**
basketball stats for my youth team, points rebounds assists per player per game

**Spec:**
```
Type:       Web application (player statistics)
Data model: Player(id, name, jersey_number)
            Game(id, opponent, date, home_away)
            StatLine(id, game_id -> Game, player_id -> Player, points, rebounds, assists, minutes)
Features:   - Enter stat lines after each game
            - Show season averages per player
            - Rank players by points, rebounds and assists
            - Show a game-by-game chart for each player
            - Export season stats to CSV
Storage:    SQLite
Tech stack: Python, Flask, Chart.js
```

---

## Example 20

**Intent:**
Election results from the government open data site, I want maps of turnout by district

**Spec:**
```
Type:       Data analysis script (election data mapping)
Features:   - Download official results CSV and district boundary GeoJSON
            - Compute turnout percentage per district
            - Join results to district boundaries
            - Draw a choropleth map of turnout
            - Save the map as an interactive HTML file
Input:      Results CSV (district_code, registered_voters, votes_cast) and a GeoJSON boundary file
Tech stack: Python, pandas, GeoPandas, Folium
```

---

## Example 21

**Intent:**
Our school has a little weather station on the roof logging temperature, humidity and wind. I want a website that shows the live readings and graphs for the last month for the students.

**Spec:**
```
Type:       Data dashboard (weather station)
Data model: Reading(id, station_id, recorded_at, temperature_c, humidity_pct, wind_speed_ms, wind_dir_deg, pressure_hpa)
Features:   - Receive readings from the station every minute
            - Show current conditions on a live page
            - Plot the last 30 days of temperature, humidity and wind
            - Show daily minimum and maximum temperatures
            - Export data for a date range as CSV
Storage:    InfluxDB
Tech stack: Python, FastAPI, Grafana
```

---

## Example 22

**Intent:**
our plate reader exports messy csvs i need to calculate concentrations from a standard curve

**Spec:**
```
Type:       Data analysis script (lab plate reader processing)
Features:   - Parse 96-well plate reader CSV exports into a tidy table
            - Subtract blank well absorbance
            - Fit a four-parameter logistic standard curve
            - Calculate sample concentrations from the curve
            - Flag replicates with a coefficient of variation above 15 percent
Input:      Plate reader CSV export and a plate layout file mapping wells to samples and standards
Tech stack: Python, pandas, SciPy, matplotlib
```

---

## Example 23

**Intent:**
Scan my paper receipts and put the amounts into a spreadsheet

**Spec:**
```
Type:       Command-line script (receipt OCR)
Features:   - Read receipt images from a folder
            - Extract text with OCR
            - Parse merchant name, date and total amount
            - Write one row per receipt to an Excel file
            - List receipts where the total could not be found
Input:      Folder of JPEG or PNG receipt photos
Tech stack: Python, Tesseract (pytesseract), OpenCV, openpyxl
```

---

## Example 24

**Intent:**
translate our help center articles into spanish french and german automatically when we publish them

**Spec:**
```
Type:       Data pipeline (documentation translation)
Data model: Article(id, slug, title, body_markdown, updated_at)
            Translation(id, article_id -> Article, language, title, body_markdown, status, translated_at)
Features:   - Detect new or changed articles through a CMS webhook
            - Translate the article with a machine translation API while keeping Markdown formatting
            - Apply a glossary of product terms that must not be translated
            - Mark translations for human review before publishing
            - Publish approved translations back to the CMS
Storage:    PostgreSQL
Tech stack: Python, DeepL API, FastAPI
```

---

## Example 25

**Intent:**
an AI that fills in insurance claim forms from customer emails

**Spec:**
```
Type:       Bot (LLM form-filling agent)
Data model: Claim(id, policy_number, claimant_name, incident_date, incident_type, description, amount, status)
            EmailMessage(id, sender, subject, body, received_at, claim_id -> Claim)
Features:   - Read incoming emails from the claims inbox
            - Extract claim fields from the email and attachments with a language model
            - Ask the customer by email for missing required fields
            - Validate the policy number against the policy database
            - Submit the completed claim form and log every step
Storage:    PostgreSQL
Tech stack: Python, Claude API (tool use), IMAP, FastAPI
```

---

## Example 26

**Intent:**
bot that reviews pull requests on github and comments on possible bugs

**Spec:**
```
Type:       Bot (code review assistant)
Features:   - Receive pull request events through a GitHub App webhook
            - Fetch the diff and related files
            - Ask a language model to review for bugs, security issues and style
            - Post inline review comments on the relevant lines
            - Skip generated files and files above a size limit
Tech stack: TypeScript, Node.js, Probot, Claude API
```

---

## Example 27

**Intent:**
help my students improve their essays without just rewriting them

**Spec:**
```
Type:       Web application (writing tutor)
Data model: Student(id, name, class_id)
            Essay(id, student_id -> Student, title, text, submitted_at)
            Feedback(id, essay_id -> Essay, category, comment, paragraph_index)
Features:   - Submit an essay draft
            - Give feedback on structure, argument and grammar without rewriting sentences
            - Highlight paragraphs with comments attached
            - Let the teacher review and edit AI feedback before release
            - Track how scores change between drafts
Storage:    PostgreSQL
Tech stack: Python, Django, Claude API, HTMX
```

---

## Example 28

**Intent:**
practice job interviews with an AI that asks me questions and tells me how I did

**Spec:**
```
Type:       Web application (interview practice bot)
Data model: User(id, email, target_role)
            Session(id, user_id -> User, role, started_at)
            Answer(id, session_id -> Session, question, transcript, score, feedback)
Features:   - Generate interview questions for the chosen role and seniority
            - Record spoken answers and transcribe them
            - Score each answer on structure, relevance and clarity
            - Give specific improvement tips with a model answer
            - Show progress across sessions
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, OpenAI Whisper API, Claude API
```

---

## Example 29

**Intent:**
plz make smth that reads the water meter photos my techs send and logs the number

**Spec:**
```
Type:       Mobile application with backend (meter reading OCR)
Data model: Meter(id, serial_number, address)
            MeterReading(id, meter_id -> Meter, technician_id, photo_url, value, confidence, read_at)
Features:   - Take a photo of the meter in the app
            - Detect the digit window and read the value with OCR
            - Show the recognised value for the technician to confirm or correct
            - Reject readings lower than the previous reading
            - Export readings per billing period
Storage:    PostgreSQL, S3 (photos)
Tech stack: Flutter, Python, FastAPI, PaddleOCR
```

---

## Example 30

**Intent:**
My wife runs a small online shop selling handmade candles. Every Christmas she runs out of the popular scents and has too many of the others. Could we use last years' orders to plan how much wax and fragrance to buy?

**Spec:**
```
Type:       Data analysis script (seasonal inventory planning)
Features:   - Load past orders exported from the shop
            - Calculate monthly sales per scent and size
            - Project next season's demand using last year's growth
            - Convert candle quantities into wax and fragrance oil amounts using recipes
            - Produce a purchase list with order dates based on supplier lead times
Input:      Order export CSV and a recipe sheet with grams of wax and oil per candle size
Tech stack: Python, pandas, openpyxl
```

---

## Example 31

**Intent:**
realtime count of people in our library using the entrance sensors

**Spec:**
```
Type:       IoT system (occupancy counting)
Data model: Sensor(id, location, type)
            CountEvent(id, sensor_id -> Sensor, direction, occurred_at)
            OccupancySnapshot(id, timestamp, count)
Features:   - Receive in/out events from door sensors over MQTT
            - Keep a running occupancy count
            - Reset the count at closing time
            - Show current occupancy on a public display page
            - Chart hourly occupancy for each weekday
Storage:    TimescaleDB
Tech stack: ESP32, MQTT (Mosquitto), Node-RED, Grafana
```

---

## Example 32

**Intent:**
quero analisar as notas dos alunos por disciplina, quais disciplinas tem mais reprovação

**Spec:**
```
Type:       Data analysis script (failure rate by subject)
Features:   - Load final grades per student and subject
            - Compute pass and fail rates per subject and class
            - Rank subjects by failure rate
            - Compare failure rates between teachers of the same subject
            - Export charts and tables to a PDF report
Input:      Excel file with columns: student, class, subject, teacher, final_grade
Tech stack: Python, pandas, matplotlib, ReportLab
```

---

## Example 33

**Intent:**
Clinic wants to know which patients will not come to their appointment

**Spec:**
```
Type:       Machine learning model (appointment no-show prediction)
Features:   - Build features from appointment lead time, weekday, past no-shows and SMS reminder status
            - Train a logistic regression and a gradient boosting model and compare them
            - Calibrate predicted probabilities
            - Flag tomorrow's appointments with high no-show risk
            - Report precision and recall on a validation set
Input:      Appointment history CSV with patient_id, booked_at, appointment_at, reminder_sent, attended
Tech stack: Python, scikit-learn, pandas
```

---

## Example 34

**Intent:**
pipeline to process DNA sequencing variant files and make a table of mutations per sample

**Spec:**
```
Type:       Data pipeline (genomic variant processing)
Features:   - Read VCF files for each sample
            - Filter variants by quality score and read depth
            - Annotate variants with gene names
            - Merge samples into one mutation matrix
            - Export the matrix and per-gene counts to CSV
Input:      Folder of VCF files and a sample sheet CSV
Tech stack: Python, Snakemake, cyvcf2, pandas
```

---

## Example 35

**Intent:**
chatbot for our museum that answers visitor questions about the exhibits in several languages

**Spec:**
```
Type:       Chatbot (museum guide)
Data model: Exhibit(id, name, room, description, period)
            Conversation(id, language, started_at)
            Message(id, conversation_id -> Conversation, role, text, created_at)
Features:   - Answer questions about exhibits using the museum's exhibit descriptions
            - Detect the visitor's language and reply in it
            - Recommend related exhibits nearby
            - Show a QR code per exhibit that opens the chat with context
            - Log unanswered questions for staff
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, Claude API, Vue.js
```

---

## Example 36

**Intent:**
speech to text for my lectures so deaf students can read along live

**Spec:**
```
Type:       Web application (live lecture captioning)
Data model: LectureSession(id, lecturer_id, code, started_at, ended_at)
            CaptionSegment(id, session_id -> LectureSession, text, start_ms, end_ms)
Features:   - Stream microphone audio from the lecturer's browser
            - Transcribe speech in real time
            - Push captions to students' screens with low delay
            - Let students adjust font size and contrast
            - Save a full transcript after the lecture
Storage:    PostgreSQL
Tech stack: Python, FastAPI, faster-whisper, React
```

---

## Example 37

**Intent:**
analyze my running data from strava export, am i getting faster

**Spec:**
```
Type:       Data analysis script (running performance trends)
Features:   - Parse activity files from the Strava export
            - Compute pace, distance and heart rate per run
            - Estimate pace at a fixed heart rate over time
            - Plot a monthly trend of 5k and 10k equivalent times
            - Summarise weekly training volume
Input:      Strava bulk export folder (activities.csv and GPX/FIT files)
Tech stack: Python, pandas, fitparse, gpxpy, matplotlib
```

---

## Example 38

**Intent:**
I need to clean up our customer address list, lots of duplicates spelled differently

**Spec:**
```
Type:       Data analysis script (address deduplication)
Features:   - Normalise addresses: case, abbreviations and postcode format
            - Find likely duplicates with fuzzy string matching
            - Group duplicates and pick a master record
            - Export a merged list and a review sheet of uncertain matches
Input:      CSV with customer_id, name, street, city, postcode
Tech stack: Python, pandas, RapidFuzz, recordlinkage
```

---

## Example 39

**Intent:**
classify customer support tickets by urgency for our IT helpdesk

**Spec:**
```
Type:       Machine learning model (ticket urgency classification)
Features:   - Train a text classifier on past tickets labelled low, medium, high and critical
            - Combine ticket text with metadata such as department and affected system
            - Evaluate with a confusion matrix and macro F1
            - Expose a prediction endpoint for the helpdesk system
            - Retrain monthly on newly labelled tickets
Tech stack: Python, scikit-learn (TF-IDF + logistic regression), FastAPI
```

---

## Example 40

**Intent:**
watch our warehouse temperature sensors and alert if the freezer gets too warm

**Spec:**
```
Type:       IoT system (cold storage monitoring)
Data model: Sensor(id, zone, min_temp_c, max_temp_c)
            Reading(id, sensor_id -> Sensor, temp_c, recorded_at)
            Alert(id, sensor_id -> Sensor, started_at, resolved_at, peak_temp_c)
Features:   - Collect temperature readings every minute over LoRaWAN
            - Raise an alert when a reading stays above the limit for 10 minutes
            - Send SMS and email alerts to the on-call person
            - Show a dashboard of all zones with current status
            - Export temperature logs for food safety audits
Storage:    InfluxDB
Tech stack: The Things Network, Node-RED, InfluxDB, Grafana, Twilio
```

---

## Example 41

**Intent:**
some kind of tool to read scanned student enrolment forms and put them into our school database

**Spec:**
```
Type:       Data pipeline (form OCR extraction)
Features:   - Read scanned PDF forms from a shared folder
            - Extract handwritten and printed fields with a document AI service
            - Map extracted values to database columns
            - Send forms with low-confidence fields to a staff review screen
            - Insert verified records into the student database
Input:      Scanned PDF enrolment forms (fixed layout)
Storage:    Microsoft SQL Server
Tech stack: Python, Azure AI Document Intelligence, pyodbc
```

---

## Example 42

**Intent:**
which of our bus routes are always late

**Spec:**
```
Type:       Data analysis script (public transport punctuality)
Features:   - Load scheduled and actual stop times from GTFS and AVL data
            - Compute delay per stop, route and hour
            - Rank routes by average and 90th percentile delay
            - Plot delay along each route on a map
            - Export a punctuality table per route
Input:      GTFS feed (stop_times.txt) and vehicle location logs (CSV)
Tech stack: Python, pandas, GeoPandas, Folium
```

---

## Example 43

**Intent:**
My dad has diabetes and his glucose meter exports CSV. Can you make something to show him patterns, like which times of day are high, in big simple charts?

**Spec:**
```
Type:       Data analysis script (glucose pattern report)
Features:   - Load glucose readings from the meter's CSV export
            - Group readings by time of day and weekday
            - Calculate time in range, average and variability
            - Draw large, high-contrast charts of daily patterns
            - Save a one-page PDF to share with the doctor
Input:      Glucose meter CSV export with timestamp and mg/dL value
Tech stack: Python, pandas, matplotlib, ReportLab
```

---

## Example 44

**Intent:**
Discord bot that summarises the last day of chat in a channel

**Spec:**
```
Type:       Bot (Discord chat summariser)
Features:   - Respond to a /summary slash command in any channel
            - Fetch messages from the past 24 hours
            - Summarise main topics and decisions with a language model
            - Mention who raised each topic
            - Post a scheduled daily summary in a chosen channel
Tech stack: Python, discord.py, Claude API
```

---

## Example 45

**Intent:**
Find which of our machines will break down soon from the vibration sensors

**Spec:**
```
Type:       Machine learning model (predictive maintenance)
Features:   - Ingest vibration and temperature readings per machine
            - Extract frequency-domain features with FFT
            - Train an anomaly detection model on normal operating data
            - Estimate remaining useful life from past failure records
            - Alert maintenance staff when risk rises above a threshold
Input:      Time series of sensor readings and a maintenance log of failures
Tech stack: Python, NumPy, SciPy, scikit-learn (Isolation Forest), MLflow
```

---

## Example 46

**Intent:**
wanna know which songs in my spotify history i actually listen to the most at night vs morning

**Spec:**
```
Type:       Data analysis script (listening habits)
Features:   - Load the Spotify extended streaming history JSON files
            - Group plays by hour of day
            - Find top tracks and artists for morning, afternoon, evening and night
            - Show total listening time per day part
            - Plot a heatmap of listening by weekday and hour
Input:      Spotify extended streaming history export (JSON)
Tech stack: Python, pandas, seaborn
```

---

## Example 47

**Intent:**
an LLM agent that books meeting rooms when people ask in Slack

**Spec:**
```
Type:       Bot (Slack room booking agent)
Data model: Room(id, name, capacity, floor, has_video)
            Booking(id, room_id -> Room, user_slack_id, starts_at, ends_at, title)
Features:   - Understand requests like "room for 6 tomorrow at 2" with a language model
            - Check room availability via the calendar API
            - Book the best matching room and confirm in the thread
            - Cancel or move bookings on request
            - Ask a clarifying question when details are missing
Storage:    PostgreSQL
Tech stack: Python, Slack Bolt, Claude API (tool use), Microsoft Graph API
```

---

## Example 48

**Intent:**
tool that compares two versions of a contract and tells the lawyer what changed in plain words

**Spec:**
```
Type:       Web application (contract diff and summary)
Data model: Comparison(id, user_id, original_file, revised_file, created_at)
            Change(id, comparison_id -> Comparison, clause, change_type, original_text, revised_text, summary)
Features:   - Upload two DOCX or PDF versions of a contract
            - Align clauses and detect added, removed and modified text
            - Summarise each change in plain language with a language model
            - Highlight changes that affect liability, payment or termination
            - Export a change report as PDF
Storage:    PostgreSQL, S3 (files)
Tech stack: Python, FastAPI, python-docx, pdfplumber, Claude API
```

---

## Example 49

**Intent:**
Pull my apple health steps and sleep and see if sleeping more makes me walk more

**Spec:**
```
Type:       Data analysis script (sleep and activity correlation)
Features:   - Parse the Apple Health export XML
            - Extract daily step counts and sleep duration
            - Align sleep with the following day's steps
            - Compute correlation and fit a simple regression
            - Plot steps against sleep with a trend line
Input:      Apple Health export.zip (export.xml)
Tech stack: Python, pandas, lxml, statsmodels, matplotlib
```

---

## Example 50

**Intent:**
Mi empresa tiene tienda online, quiero saber que productos se compran juntos

**Spec:**
```
Type:       Data analysis script (market basket analysis)
Features:   - Load order lines and group them into baskets
            - Find frequent item sets with the Apriori algorithm
            - Generate association rules with support, confidence and lift
            - List the top product pairs for cross-selling
            - Export rules to Excel
Input:      CSV with order_id, product_id, product_name
Tech stack: Python, pandas, mlxtend
```

---

## Example 51

**Intent:**
Monitor river water level from sensors and warn villages before flooding

**Spec:**
```
Type:       IoT system (flood early warning)
Data model: Station(id, river, location, warning_level_m, danger_level_m)
            LevelReading(id, station_id -> Station, level_m, recorded_at)
            Warning(id, station_id -> Station, level, issued_at)
Features:   - Collect water level readings from ultrasonic sensors over GSM
            - Calculate the rate of rise per hour
            - Issue warnings when levels or rise rates pass thresholds
            - Send SMS warnings to registered village contacts
            - Show stations and levels on a public map
Storage:    PostgreSQL with TimescaleDB
Tech stack: Arduino (SIM800), Python, FastAPI, Leaflet, Africa's Talking SMS API
```

---

## Example 52

**Intent:**
tag photos of plant leaves as healthy or diseased for our greenhouse

**Spec:**
```
Type:       Machine learning model (plant disease classification)
Features:   - Fine-tune a pretrained CNN on labelled leaf images
            - Augment images with rotation, flips and colour jitter
            - Classify leaves into healthy and named disease classes
            - Report per-class precision and recall
            - Export the model to TensorFlow Lite for a phone app
Input:      Folder of leaf images sorted into class subfolders
Tech stack: Python, TensorFlow, Keras (MobileNetV3)
```

---

## Example 53

**Intent:**
track how parking lot fills up during the day from a camera

**Spec:**
```
Type:       Machine learning model (parking occupancy detection)
Data model: ParkingSpace(id, lot_id, polygon)
            OccupancyLog(id, space_id -> ParkingSpace, occupied, recorded_at)
Features:   - Let an admin draw parking space polygons on a camera snapshot
            - Classify each space as free or occupied every minute
            - Store occupancy history
            - Show live free spaces on a web page
            - Chart average occupancy by hour of day
Storage:    SQLite
Tech stack: Python, OpenCV, PyTorch, Flask
```

---

## Example 54

**Intent:**
newsletter signups data, show me which blog posts bring the most subscribers

**Spec:**
```
Type:       Data analysis script (content attribution)
Features:   - Join signup events with the page the visitor came from
            - Count signups per blog post and per traffic source
            - Compute signup conversion rate per post
            - Rank posts by subscribers gained in the last 90 days
            - Chart the top 15 posts
Input:      Analytics export CSV (page_path, sessions) and signup events CSV (email_hash, signup_page, signed_up_at)
Tech stack: Python, pandas, Plotly
```

---

## Example 55

**Intent:**
Every week I copy numbers from 12 supplier price PDFs into Excel. Make it automatic.

**Spec:**
```
Type:       Scheduled script (PDF price extraction)
Features:   - Download new price list PDFs from the supplier email inbox
            - Extract product tables from each PDF
            - Normalise product codes, units and currency
            - Update the master price spreadsheet
            - Highlight prices that changed by more than 5 percent
Input:      Supplier PDF price lists (email attachments)
Tech stack: Python, pdfplumber, camelot, openpyxl, imaplib
```

---

## Example 56

**Intent:**
help me analyze 10 years of my home electricity bills to see if the solar panels paid off

**Spec:**
```
Type:       Data analysis script (solar payback analysis)
Features:   - Load monthly electricity bills before and after the solar installation
            - Adjust consumption for tariff changes
            - Estimate monthly savings and feed-in income
            - Calculate cumulative savings against the installation cost
            - Show the payback year on a chart
Input:      Spreadsheet with month, kWh_imported, kWh_exported, cost, tariff
Tech stack: Python, pandas, matplotlib
```

---

## Example 57

**Intent:**
telegram bot that transcribes voice messages people send to it

**Spec:**
```
Type:       Bot (Telegram voice transcription)
Features:   - Receive voice messages and audio files in private and group chats
            - Convert audio to WAV with ffmpeg
            - Transcribe audio and detect the language
            - Reply with the text as a quote to the original message
            - Limit audio length to 10 minutes per message
Tech stack: Python, python-telegram-bot, faster-whisper, ffmpeg
```

---

## Example 58

**Intent:**
An app for our quality control team where they upload a CSV of measurements and see if the process is in control

**Spec:**
```
Type:       Web application (statistical process control)
Data model: Process(id, name, lower_spec, upper_spec)
            Measurement(id, process_id -> Process, sample_group, value, measured_at)
Features:   - Upload measurements from a CSV file
            - Draw X-bar and R control charts
            - Apply Western Electric rules to flag out-of-control points
            - Calculate Cp and Cpk process capability
            - Export charts and statistics to PDF
Storage:    PostgreSQL
Tech stack: Python, Django, pandas, Plotly
```

---

## Example 59

**Intent:**
count birds species from audio recordings in my garden

**Spec:**
```
Type:       Machine learning model (bird sound identification)
Features:   - Split long recordings into 3-second segments
            - Run a pretrained bird sound classifier on each segment
            - Keep detections above a confidence threshold
            - Summarise species detected per day and hour
            - Export detections with timestamps to CSV
Input:      WAV recordings from a garden recorder
Tech stack: Python, BirdNET-Analyzer, librosa, pandas
```

---

## Example 60

**Intent:**
let me ask questions about our sales database in normal english instead of SQL

**Spec:**
```
Type:       Web application (natural language to SQL)
Data model: QueryLog(id, user_email, question, generated_sql, row_count, created_at)
Features:   - Read the database schema and table descriptions
            - Turn a question into a read-only SQL query with a language model
            - Show the generated SQL for the user to check before running
            - Run the query and display results as a table or chart
            - Block queries that modify data or touch restricted tables
Storage:    PostgreSQL (read-only replica), SQLite (query log)
Tech stack: Python, FastAPI, Claude API, sqlglot, React
```

---

## Example 61

**Intent:**
reading level checker for kids books

**Spec:**
```
Type:       Command-line tool (readability scoring)
Features:   - Read text from TXT, DOCX or EPUB files
            - Calculate Flesch-Kincaid grade and other readability scores
            - List the hardest words in the text by frequency rank
            - Suggest an age band for the book
            - Output a short report to the terminal or JSON
Input:      Path to a book file
Tech stack: Python, textstat, ebooklib, python-docx
```

---

## Example 62

**Intent:**
hey so i run a food bank and we log every family visit in google sheets. i want to see how many families come each month, which neighborhoods, and if it's going up since prices went up

**Spec:**
```
Type:       Data dashboard (food bank visits)
Features:   - Read visit records from the Google Sheet on a schedule
            - Count unique families and total visits per month
            - Map visits by neighbourhood using postcodes
            - Show year-over-year change in monthly visits
            - Filter by household size and first-time visitors
Input:      Google Sheet with visit_date, family_id, postcode, household_size
Tech stack: Python, gspread, pandas, Streamlit, Plotly
```

---

## Example 63

**Intent:**
detect if students are copying each others code assignments

**Spec:**
```
Type:       Command-line tool (code plagiarism detection)
Features:   - Load all student submissions for an assignment from a folder
            - Normalise code by removing comments, whitespace and renaming identifiers
            - Compare every pair of submissions with token-based fingerprinting
            - Rank pairs by similarity score
            - Generate an HTML report showing matching sections side by side
Input:      Folder with one subfolder per student containing source files
Tech stack: Python, Pygments (tokenising), winnowing algorithm, Jinja2
```

---

## Example 64

**Intent:**
How busy will our restaurant be on Friday night? we want to plan staff

**Spec:**
```
Type:       Machine learning model (restaurant covers forecasting)
Features:   - Load past reservations and walk-in counts per service
            - Add features for weekday, holidays, local events and weather
            - Train a model to predict covers per hour
            - Convert predicted covers into recommended staff numbers
            - Show next week's forecast in a simple table
Input:      Reservation system export and a daily covers spreadsheet
Tech stack: Python, pandas, scikit-learn, Prophet
```

---

## Example 65

**Intent:**
pipeline to load our sensor data from the factory PLCs into a data warehouse every 5 minutes

**Spec:**
```
Type:       Data pipeline (industrial sensor ingestion)
Features:   - Read tag values from PLCs over OPC UA
            - Buffer readings locally when the network is down
            - Validate value ranges and units for each tag
            - Load batches into the warehouse every 5 minutes
            - Track pipeline lag and failed loads on a status page
Storage:    Snowflake
Tech stack: Python, asyncua, Apache Airflow, Snowflake connector
```

---

## Example 66

**Intent:**
check if our loan approval model is fair across ethnic groups

**Spec:**
```
Type:       Data analysis script (model fairness audit)
Features:   - Load model predictions together with protected attributes held separately
            - Compute approval rates, false positive and false negative rates per group
            - Calculate demographic parity and equalised odds differences
            - Plot metrics per group with confidence intervals
            - Write a summary report with groups that fail the agreed thresholds
Input:      CSV of applicant_id, prediction, actual_outcome and a separate CSV of protected attributes
Tech stack: Python, Fairlearn, pandas, matplotlib
```

---

## Example 67

**Intent:**
Our hotel gets reviews on several booking sites. I'd like one place to see them all, with the main things guests complain about each month, like noise or breakfast.

**Spec:**
```
Type:       Web application (hotel review aggregation and topic analysis)
Data model: Review(id, source, rating, text, language, stayed_at, fetched_at)
            ReviewTopic(id, review_id -> Review, topic, sentiment)
Features:   - Import reviews from each booking site export or API
            - Translate non-English reviews to English
            - Tag each review with topics such as cleanliness, noise, staff and breakfast
            - Score sentiment per topic
            - Show monthly topic trends and the latest negative comments
Storage:    PostgreSQL
Tech stack: Python, Django, Hugging Face Transformers, DeepL API, Chart.js
```

---

## Example 68

**Intent:**
speech to text for doctor's notes

**Spec:**
```
Type:       Mobile application with backend (clinical dictation)
Data model: Clinician(id, name, specialty)
            Dictation(id, clinician_id -> Clinician, patient_ref, audio_url, transcript, status, created_at)
Features:   - Record dictation on the phone
            - Transcribe audio with a medical vocabulary model
            - Format the transcript into SOAP note sections
            - Let the clinician edit and sign off the note
            - Send the signed note to the EHR via HL7 FHIR
Storage:    PostgreSQL (encrypted at rest), S3 (audio)
Tech stack: Swift (iOS), Python, FastAPI, AWS Transcribe Medical
```

---

## Example 69

**Intent:**
i want to see wich teachers have the best results in final exams compared with how good students were before

**Spec:**
```
Type:       Data analysis script (value-added analysis)
Features:   - Join prior attainment scores with final exam results
            - Fit a regression of final score on prior score
            - Compute each student's residual as value added
            - Average value added per teacher with confidence intervals
            - Plot teachers with small sample sizes in grey
Input:      CSV with student_id, teacher, prior_score, final_score
Tech stack: Python, pandas, statsmodels, matplotlib
```

---

## Example 70

**Intent:**
wildfire smoke air quality map from cheap sensors around town

**Spec:**
```
Type:       Data dashboard (community air quality)
Data model: Sensor(id, name, lat, lon, owner)
            AirReading(id, sensor_id -> Sensor, pm25, pm10, humidity, recorded_at)
Features:   - Pull readings from the sensor network API every 10 minutes
            - Apply a humidity correction to PM2.5 values
            - Convert PM2.5 to an air quality index category
            - Show sensors on a colour-coded map
            - Plot 24-hour history for each sensor
Storage:    PostgreSQL with PostGIS
Tech stack: Python, PurpleAir API, Dash, Plotly Mapbox
```

---

## Example 71

**Intent:**
ML model that predicts if a student will drop out of university in first year

**Spec:**
```
Type:       Machine learning model (student dropout risk)
Features:   - Build features from entry grades, attendance, LMS logins and first-term marks
            - Train a gradient boosting classifier with cross-validation
            - Explain individual predictions with SHAP values
            - Check prediction quality separately for different student groups
            - Export a risk list for student advisers each month
Input:      Student records CSV, LMS activity log, attendance export
Tech stack: Python, pandas, XGBoost, SHAP
```

---

## Example 72

**Intent:**
count how many fish pass the fish ladder using underwater camera

**Spec:**
```
Type:       Machine learning model (fish counting from video)
Features:   - Detect fish in underwater video frames
            - Track individual fish across frames
            - Count upstream and downstream crossings of a virtual line
            - Estimate fish length from a calibration marker
            - Export hourly counts and size distributions to CSV
Input:      Underwater video files with timestamps
Tech stack: Python, YOLOv8, DeepSORT, OpenCV
```

---

## Example 73

**Intent:**
rate my podcast episodes by how often listeners drop off

**Spec:**
```
Type:       Data analysis script (podcast retention analysis)
Features:   - Load per-episode listening retention data from the hosting platform export
            - Compute average listen-through rate per episode
            - Find the timestamps where the biggest drop-offs happen
            - Compare episode length, guest and topic with retention
            - Chart retention curves for the best and worst episodes
Input:      CSV export with episode_id, second, listeners_remaining, plus an episode metadata sheet
Tech stack: Python, pandas, matplotlib
```

---

## Example 74

**Intent:**
I volunteer for a cat rescue. We have a spreadsheet of every cat we took in since 2015 with intake date, age, colour and adoption date. I'd love to know what makes cats get adopted faster, black cats seem to wait longer.

**Spec:**
```
Type:       Data analysis script (adoption time analysis)
Features:   - Load the intake and adoption spreadsheet
            - Calculate days to adoption for each cat
            - Compare adoption times by colour, age group and intake season
            - Fit a survival model that handles cats still waiting
            - Plot Kaplan-Meier curves for each colour group
Input:      Excel file with cat_id, intake_date, age_months, colour, sex, adoption_date
Tech stack: Python, pandas, lifelines, matplotlib
```

---

## Example 75

**Intent:**
python script that pulls covid and flu case counts from the public health api and graphs them weekly

**Spec:**
```
Type:       Scheduled script (public health data tracking)
Features:   - Download weekly case counts from the public health open data API
            - Store the history in a local database
            - Compute 4-week rolling averages
            - Plot weekly cases for both diseases on one chart
            - Save the chart and a CSV to a shared folder every Monday
Input:      Public health open data API endpoint
Storage:    SQLite
Tech stack: Python, requests, pandas, matplotlib, cron
```

---

## Example 76

**Intent:**
LLM that grades short answer questions using the teacher's marking scheme

**Spec:**
```
Type:       Web application (short answer auto-grading)
Data model: Assessment(id, title, teacher_id)
            Question(id, assessment_id -> Assessment, text, marking_scheme, max_marks)
            StudentAnswer(id, question_id -> Question, student_name, text, suggested_marks, final_marks, rationale)
Features:   - Upload questions with a marking scheme
            - Import student answers from a CSV
            - Suggest marks with a language model citing the marking points met
            - Let the teacher accept or override every mark
            - Export final marks to the school gradebook format
Storage:    PostgreSQL
Tech stack: Python, Flask, Claude API, Bootstrap
```

---

## Example 77

**Intent:**
wine quality prediction from lab measurements

**Spec:**
```
Type:       Machine learning model (wine quality regression)
Features:   - Load chemical measurements such as acidity, sugar, sulphates and alcohol
            - Explore correlations with quality scores
            - Train and compare random forest and gradient boosting models
            - Tune hyperparameters with cross-validation
            - Save the best model and report feature importance
Input:      CSV with physicochemical measurements and a quality score from 0 to 10
Tech stack: Python, scikit-learn, pandas, joblib
```

---

## Example 78

**Intent:**
find out which ads on our tv channel get the most phone calls after airing

**Spec:**
```
Type:       Data analysis script (TV ad response attribution)
Features:   - Load the ad airing schedule and the call centre call log
            - Estimate a baseline call rate per minute of the day
            - Count calls above baseline in the 10 minutes after each airing
            - Rank ads, channels and time slots by response
            - Plot response curves for the top ads
Input:      Ad schedule CSV (ad_id, channel, aired_at) and call log CSV (call_time, number_dialled)
Tech stack: Python, pandas, NumPy, matplotlib
```

---

## Example 79

**Intent:**
An assistant that helps nurses write handover notes from the patient chart

**Spec:**
```
Type:       Web application (clinical handover summariser)
Data model: HandoverNote(id, patient_id, author_id, shift, content, created_at)
Features:   - Pull recent vitals, medications and nursing notes for a patient
            - Draft a handover in SBAR format with a language model
            - Highlight abnormal vitals and pending tasks
            - Let the nurse edit and confirm the note before saving
            - Keep an audit log of drafts and edits
Storage:    PostgreSQL
Tech stack: Python, FastAPI, HL7 FHIR API, Claude API, React
```

---

## Example 80

**Intent:**
twitter-like posts about our brand classify into complaint, question, praise

**Spec:**
```
Type:       Machine learning model (social post intent classification)
Features:   - Collect brand mentions from social platforms
            - Label a starter set of posts into complaint, question, praise and other
            - Fine-tune a small transformer on the labelled posts
            - Route complaints and questions to the support inbox
            - Report weekly counts per category
Tech stack: Python, Hugging Face Transformers (DistilBERT), pandas
```

---

## Example 81

**Intent:**
Weather station data from several farms, find frost risk nights

**Spec:**
```
Type:       Data analysis script (frost risk detection)
Features:   - Merge hourly temperature and humidity data from multiple stations
            - Compute dew point from temperature and humidity
            - Flag nights where temperature drops below 2 degrees C
            - Compare frost frequency between stations and months
            - Export a frost calendar per station
Input:      CSV files per station with timestamp, temperature_c, humidity_pct, wind_speed
Tech stack: Python, pandas, MetPy, matplotlib
```

---

## Example 82

**Intent:**
auto-tag our photo library: people, places, objects

**Spec:**
```
Type:       Data pipeline (photo auto-tagging)
Data model: Photo(id, path, taken_at, lat, lon)
            Tag(id, photo_id -> Photo, label, source, confidence)
            FaceCluster(id, name)
Features:   - Scan the photo library for new images
            - Detect objects and scenes with an image tagging model
            - Cluster faces and let the user name each cluster
            - Reverse-geocode GPS coordinates into place names
            - Store tags so photos can be searched by keyword
Storage:    SQLite
Tech stack: Python, CLIP, InsightFace, geopy
```

---

## Example 83

**Intent:**
i have a csv of all the books in our school library and borrow history, what books are never borrowed

**Spec:**
```
Type:       Data analysis script (library circulation analysis)
Features:   - Load the catalogue and loan history
            - Count loans per title over the last 3 years
            - List titles never borrowed, grouped by shelf section
            - Find the most borrowed authors and genres
            - Export a weeding candidate list to Excel
Input:      catalogue.csv (book_id, title, author, section, added_date) and loans.csv (book_id, borrowed_at)
Tech stack: Python, pandas, openpyxl
```

---

## Example 84

**Intent:**
transcribe and translate youtube videos from japanese to english subtitles

**Spec:**
```
Type:       Command-line tool (subtitle generation and translation)
Features:   - Download audio from a video URL
            - Transcribe Japanese speech with timestamps
            - Translate each segment into English
            - Split long segments to fit subtitle length limits
            - Write SRT subtitle files for both languages
Input:      Video URL or local video file
Tech stack: Python, yt-dlp, faster-whisper, DeepL API, pysrt
```

---

## Example 85

**Intent:**
a model to estimate house prices in our town for our real estate agents

**Spec:**
```
Type:       Machine learning model (property valuation)
Features:   - Clean past sale records: remove outliers and duplicates
            - Engineer features such as size, rooms, age, distance to centre and school zone
            - Train a gradient boosting model with log-transformed prices
            - Report mean absolute error by neighbourhood
            - Serve valuations through a simple web form with comparable sales
Tech stack: Python, pandas, LightGBM, FastAPI
```

---

## Example 86

**Intent:**
what time of day do our customers open our emails

**Spec:**
```
Type:       Data analysis script (email engagement timing)
Features:   - Load email send and open events from the email platform export
            - Convert timestamps to each recipient's local time zone
            - Calculate open rate by hour and weekday
            - Compare segments such as new and returning customers
            - Recommend the best send window per segment
Input:      CSV with recipient_id, timezone, sent_at, opened_at, segment
Tech stack: Python, pandas, seaborn
```

---

## Example 87

**Intent:**
I'm a nutritionist and my clients send me photos of their meals. It takes forever to estimate calories. Can AI look at the photo and give me a rough breakdown that I can correct?

**Spec:**
```
Type:       Web application (meal photo nutrition estimation)
Data model: Client(id, name, nutritionist_id)
            MealPhoto(id, client_id -> Client, image_url, taken_at)
            MealEstimate(id, photo_id -> MealPhoto, food_items, calories, protein_g, carbs_g, fat_g, corrected)
Features:   - Let clients upload meal photos from their phone
            - Identify food items and portion sizes with a vision model
            - Estimate calories and macronutrients from a food database
            - Let the nutritionist correct items and amounts
            - Show daily totals per client
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Claude API (vision), USDA FoodData Central API
```

---

## Example 88

**Intent:**
news articles: cluster them into stories so we don't show 10 copies of the same story

**Spec:**
```
Type:       Data pipeline (news story clustering)
Features:   - Ingest articles from RSS feeds every 15 minutes
            - Embed headline and lead paragraph
            - Assign each article to an existing story cluster or start a new one
            - Pick a representative headline per cluster
            - Expose clusters to the news app through an API
Storage:    PostgreSQL with pgvector
Tech stack: Python, feedparser, sentence-transformers, FastAPI
```

---

## Example 89

**Intent:**
script that checks a csv of lab results and highlights out of range values

**Spec:**
```
Type:       Command-line script (lab results range check)
Features:   - Load lab results and a reference range table
            - Match each test to its reference range by sex and age
            - Flag values as low, normal or high
            - Write a colour-coded Excel file
            - Print a count of flagged results per test
Input:      results.csv (patient_id, sex, age, test_code, value) and ranges.csv
Tech stack: Python, pandas, openpyxl
```

---

## Example 90

**Intent:**
bot that answers questions about our employee handbook in Microsoft Teams

**Spec:**
```
Type:       Bot (HR handbook assistant)
Features:   - Index the handbook PDF and policy pages into a vector store
            - Answer questions in Teams with citations to the relevant section
            - Say clearly when the handbook does not cover the question
            - Escalate to HR with a button
            - Re-index automatically when a policy file changes
Storage:    Azure AI Search
Tech stack: C#, Bot Framework SDK, Azure OpenAI Service
```

---

## Example 91

**Intent:**
monitor the noise level near the construction site and report violations

**Spec:**
```
Type:       IoT system (noise monitoring)
Data model: NoiseMeter(id, location, limit_db_day, limit_db_night)
            NoiseReading(id, meter_id -> NoiseMeter, laeq_db, lmax_db, recorded_at)
            Violation(id, meter_id -> NoiseMeter, started_at, ended_at, max_db)
Features:   - Record LAeq and Lmax every minute from sound level meters
            - Compare readings against day and night limits
            - Log violations lasting more than 5 minutes
            - Notify the site manager in real time
            - Generate a weekly compliance report for the council
Storage:    PostgreSQL
Tech stack: Raspberry Pi, Python, MQTT, Grafana
```

---

## Example 92

**Intent:**
sales calls recorded, want to know which phrases the top reps use

**Spec:**
```
Type:       Data analysis script (sales call conversation analysis)
Features:   - Transcribe recorded sales calls with speaker labels
            - Calculate talk-to-listen ratio per rep
            - Extract frequent phrases and questions per rep
            - Compare phrases used by top and bottom performers by win rate
            - Export findings and example snippets to a report
Input:      Call recordings (WAV) and a CRM export with rep and deal outcome
Tech stack: Python, AssemblyAI API, spaCy, pandas
```

---

## Example 93

**Intent:**
Model to say if a mushroom photo is poisonous? just for fun, I know not to trust it

**Spec:**
```
Type:       Machine learning model (mushroom image classification)
Features:   - Fine-tune a pretrained vision model on labelled mushroom species images
            - Map species to edibility categories
            - Show the top 3 species with confidence
            - Always show a warning that results are not safe for foraging decisions
            - Export the model for use in a small web demo
Input:      Mushroom image dataset with species labels
Tech stack: Python, PyTorch, timm, Gradio
```

---

## Example 94

**Intent:**
Our call center wants to forecast how many calls we'll get each half hour next week

**Spec:**
```
Type:       Machine learning model (call volume forecasting)
Features:   - Load historical call counts in 30-minute intervals
            - Model daily and weekly seasonality and holidays
            - Forecast the next 7 days at 30-minute resolution
            - Convert forecast volume to required agents using Erlang C
            - Export the staffing plan to Excel
Input:      Call log CSV with call start times
Tech stack: Python, statsforecast, pandas, pyworkforce
```

---

## Example 95

**Intent:**
i want to see which streets in my city have the most bike accidents

**Spec:**
```
Type:       Data analysis script (cycling accident hotspots)
Features:   - Load police collision records with coordinates
            - Filter collisions involving bicycles
            - Snap collisions to the nearest street segment
            - Rank streets by collisions per kilometre
            - Draw a heatmap and a top-20 table
Input:      Collision CSV (date, lat, lon, vehicles_involved, severity) and an OpenStreetMap extract
Tech stack: Python, GeoPandas, OSMnx, Folium
```

---

## Example 96

**Intent:**
an agent that applies for building permits by filling the city's online form for our clients

**Spec:**
```
Type:       Bot (LLM web form-filling agent)
Data model: Client(id, name, address, contact)
            PermitApplication(id, client_id -> Client, project_type, status, submitted_at, confirmation_number)
Features:   - Collect project details from the client intake form
            - Map details onto the city permit form fields with a language model
            - Fill the online form in a headless browser
            - Pause for human approval before submitting
            - Save confirmation numbers and screenshots of each step
Storage:    PostgreSQL
Tech stack: Python, Playwright, Claude API (tool use)
```

---

## Example 97

**Intent:**
grading multiple choice bubble sheets from phone photos

**Spec:**
```
Type:       Mobile application (bubble sheet scanner)
Data model: AnswerKey(id, test_name, answers)
            ScannedSheet(id, key_id -> AnswerKey, student_id, answers, score, scanned_at)
Features:   - Detect the sheet corners and correct perspective
            - Read filled bubbles for each question
            - Compare answers with the answer key and compute the score
            - Show per-question error rates for the class
            - Export scores to CSV
Storage:    Local SQLite on the device
Tech stack: Kotlin (Android), OpenCV for Android
```

---

## Example 98

**Intent:**
analysis of our app crash logs to find the top causes

**Spec:**
```
Type:       Data analysis script (crash log analysis)
Features:   - Load crash reports with stack traces
            - Group crashes by normalised stack trace signature
            - Count affected users per signature and app version
            - Rank signatures by user impact
            - Show which app versions introduced each crash group
Input:      JSON export of crash reports (stack_trace, app_version, device, user_id, timestamp)
Tech stack: Python, pandas, regex, matplotlib
```

---

## Example 99

**Intent:**
wanna predict which customers will upgrade to premium plan

**Spec:**
```
Type:       Machine learning model (upgrade propensity)
Features:   - Build features from feature usage, team size and trial activity
            - Train a classifier on past upgrade outcomes
            - Evaluate with ROC AUC and lift at the top 10 percent
            - Score all free accounts weekly
            - Push the top scored accounts to the CRM for the sales team
Tech stack: Python, scikit-learn, pandas, HubSpot API
```

---

## Example 100

**Intent:**
Je voudrais analyser les temps d'attente aux caisses de notre supermarché avec les données des tickets

**Spec:**
```
Type:       Data analysis script (checkout queue analysis)
Features:   - Load till transaction timestamps per checkout lane
            - Estimate customers per 15 minutes and service time per transaction
            - Estimate queue length with a queueing model
            - Find time slots where more lanes should be open
            - Plot the recommended number of open lanes per hour
Input:      Till export CSV (lane_id, transaction_start, transaction_end, items)
Tech stack: Python, pandas, NumPy, matplotlib
```

---

## Example 101

**Intent:**
score how risky each supplier is using news and financial data

**Spec:**
```
Type:       Data pipeline (supplier risk scoring)
Data model: Supplier(id, name, country, category)
            RiskSignal(id, supplier_id -> Supplier, source, signal_type, severity, detected_at)
            RiskScore(id, supplier_id -> Supplier, score, computed_at)
Features:   - Pull supplier news articles and financial ratios daily
            - Classify news into risk events such as strikes, lawsuits and bankruptcy
            - Combine signals into a weighted risk score
            - Alert buyers when a supplier score jumps
            - Show a risk dashboard per category
Storage:    PostgreSQL
Tech stack: Python, Apache Airflow, NewsAPI, Hugging Face Transformers, Metabase
```

---

## Example 102

**Intent:**
automatically blur faces and license plates in our street photos

**Spec:**
```
Type:       Command-line tool (photo anonymisation)
Features:   - Detect faces and licence plates in each image
            - Apply Gaussian blur to detected regions
            - Process folders in parallel
            - Write blurred copies to an output folder, keeping EXIF data
            - Log images where nothing was detected for spot checks
Input:      Folder of street-level JPEG photos
Tech stack: Python, OpenCV, RetinaFace, YOLOv8 (licence plate model)
```

---

## Example 103

**Intent:**
analyse my company's slack to see which teams talk to each other the most

**Spec:**
```
Type:       Data analysis script (team communication network)
Features:   - Load a Slack workspace export
            - Map each user to their team
            - Count cross-team messages and mentions
            - Build a team-to-team network graph
            - Visualise the network with edge thickness by message volume
Input:      Slack export ZIP and a CSV mapping users to teams
Tech stack: Python, pandas, NetworkX, pyvis
```

---

## Example 104

**Intent:**
sort the incoming invoices by supplier and read the total and due date

**Spec:**
```
Type:       Data pipeline (invoice data extraction)
Data model: Invoice(id, supplier_id -> Supplier, invoice_number, total, currency, due_date, file_path, status)
            Supplier(id, name, vat_number)
Features:   - Watch an email inbox for invoice attachments
            - Extract supplier, invoice number, total and due date with a document parser
            - Match the supplier by VAT number
            - Flag duplicate invoice numbers
            - Send extracted data to the accounting system
Storage:    PostgreSQL
Tech stack: Python, Amazon Textract, FastAPI, Xero API
```

---

## Example 105

**Intent:**
classify the sound of our machines to know if a bearing is going bad

**Spec:**
```
Type:       Machine learning model (acoustic anomaly detection)
Features:   - Record audio clips from microphones near each machine
            - Convert clips to log-mel spectrograms
            - Train an autoencoder on normal machine sounds
            - Score new clips by reconstruction error
            - Raise an alert when the anomaly score stays high
Input:      WAV clips from machine microphones
Tech stack: Python, librosa, PyTorch
```

---

## Example 106

**Intent:**
give me a script to compare the prices of the same products in 3 online shops every day

**Spec:**
```
Type:       Scheduled script (price comparison scraping)
Data model: Product(id, name, ean)
            PriceObservation(id, product_id -> Product, shop, price, in_stock, observed_at)
Features:   - Scrape product pages from three shops by EAN
            - Store a daily price per shop
            - Find the cheapest shop for each product
            - Detect price drops of more than 10 percent
            - Email a daily summary table
Storage:    SQLite
Tech stack: Python, httpx, BeautifulSoup, pandas, cron
```

---

## Example 107

**Intent:**
AI writing assistant that checks my thesis for consistent citations and terms

**Spec:**
```
Type:       Desktop application (thesis consistency checker)
Features:   - Open a DOCX or LaTeX thesis
            - Check that every in-text citation has a bibliography entry and vice versa
            - Find inconsistent spelling of key terms and abbreviations
            - Flag abbreviations used before they are defined
            - Show issues in a list that jumps to the location in the document
Input:      Thesis file (.docx or .tex) and bibliography (.bib)
Tech stack: Python, PySide6, python-docx, bibtexparser
```

---

## Example 108

**Intent:**
pls help, survey from 300 farmers in excel, need charts by region

**Spec:**
```
Type:       Data analysis script (farmer survey summary)
Features:   - Load the survey responses from Excel
            - Clean region names and coded answers
            - Summarise each question by region with counts and percentages
            - Draw bar charts per question and region
            - Save all charts into one PowerPoint file
Input:      Excel file with one row per farmer and one column per question
Tech stack: Python, pandas, matplotlib, python-pptx
```

---

## Example 109

**Intent:**
estimate how many solar panels fit on a roof from a satellite image

**Spec:**
```
Type:       Machine learning model (rooftop solar potential)
Features:   - Fetch a satellite image for an address
            - Segment the roof outline and obstacles
            - Estimate roof orientation and usable area
            - Calculate how many standard panels fit and expected yearly kWh
            - Return a marked-up image with the panel layout
Tech stack: Python, PyTorch (U-Net), Google Maps Static API, PVGIS API, FastAPI
```

---

## Example 110

**Intent:**
Model that predicts length of hospital stay at admission

**Spec:**
```
Type:       Machine learning model (length of stay prediction)
Features:   - Build features from admission diagnosis, age, comorbidities and admission source
            - Train a gradient boosting regressor
            - Report error in days by department
            - Explain predictions per patient with SHAP
            - Provide predictions to bed management through an API
Tech stack: Python, pandas, CatBoost, SHAP, FastAPI
```

---

## Example 111

**Intent:**
detect when people fall down in the elderly care home using cameras, without storing video

**Spec:**
```
Type:       Machine learning model (fall detection)
Data model: Camera(id, room, active)
            FallEvent(id, camera_id -> Camera, detected_at, confidence, acknowledged_by, acknowledged_at)
Features:   - Run pose estimation on camera frames on a local edge device
            - Detect falls from sudden changes in body keypoints
            - Send an alert to staff phones within seconds
            - Store only skeleton keypoints, never raw video
            - Let staff acknowledge alerts and mark false alarms
Storage:    SQLite on the edge device
Tech stack: Python, NVIDIA Jetson, MediaPipe Pose, MQTT
```

---

## Example 112

**Intent:**
tutor bot for learning spanish by chatting

**Spec:**
```
Type:       Chatbot (language learning tutor)
Data model: Learner(id, email, level, native_language)
            ChatSession(id, learner_id -> Learner, topic, started_at)
            Correction(id, session_id -> ChatSession, original, corrected, explanation)
Features:   - Chat in Spanish at the learner's CEFR level
            - Correct mistakes gently with short explanations
            - Save corrections to a review list
            - Suggest conversation topics
            - Quiz the learner on past mistakes
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Claude API
```

---

## Example 113

**Intent:**
i manage 5 vending machines and want to know when to refill each

**Spec:**
```
Type:       Data analysis script (vending restock planning)
Features:   - Load sales per machine and slot from the telemetry export
            - Estimate daily sales rate per product
            - Predict days until each slot is empty
            - Build a refill route for machines that need restocking soon
            - Print a packing list per machine
Input:      Telemetry CSV (machine_id, slot, product, sold_at) and current stock levels
Tech stack: Python, pandas, OR-Tools
```

---

## Example 114

**Intent:**
Ich brauche ein Skript, das unsere Stromzählerdaten von 50 Gebäuden auf Ausreißer prüft

**Spec:**
```
Type:       Data analysis script (meter data anomaly detection)
Features:   - Load 15-minute meter readings for all buildings
            - Detect gaps, negative values and frozen readings
            - Flag outliers with a rolling median and MAD rule
            - Summarise data quality per building
            - Export flagged periods to Excel
Input:      CSV files per building with timestamp and kWh
Tech stack: Python, pandas, NumPy, openpyxl
```

---

## Example 115

**Intent:**
dashboard for our clinic showing how many patients per doctor per day

**Spec:**
```
Type:       Data dashboard (clinic patient volume)
Features:   - Load appointments from the practice management system database
            - Show patients seen per doctor per day
            - Show average consultation length
            - Compare booked and walk-in patients
            - Filter by date range and clinic location
Storage:    MySQL (read-only)
Tech stack: Metabase
```

---

## Example 116

**Intent:**
semantic search over thousands of scientific papers in our lab

**Spec:**
```
Type:       Web application (paper semantic search)
Data model: Paper(id, title, authors, year, abstract, pdf_path)
            Chunk(id, paper_id -> Paper, text, embedding)
Features:   - Upload PDFs or import by DOI
            - Extract text and split into chunks
            - Search by meaning with embedding similarity
            - Show matching passages with links to the page in the PDF
            - Filter results by year and author
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, GROBID, sentence-transformers, Svelte
```

---

## Example 117

**Intent:**
tennis match stats from video

**Spec:**
```
Type:       Machine learning model (tennis match analysis)
Features:   - Detect the court lines, players and ball in each frame
            - Track ball trajectory and estimate bounce points
            - Classify shots as forehand, backhand, serve or volley
            - Compute rally length and winners per player
            - Export a match statistics report
Input:      Match video recorded from behind the baseline
Tech stack: Python, OpenCV, YOLOv8, PyTorch
```

---

## Example 118

**Intent:**
soil moisture sensors in my vegetable garden tell me when to water

**Spec:**
```
Type:       IoT system (garden irrigation monitoring)
Data model: Bed(id, name, crop, moisture_threshold)
            MoistureReading(id, bed_id -> Bed, moisture_pct, soil_temp_c, recorded_at)
Features:   - Read capacitive soil moisture sensors every 15 minutes
            - Send readings to a home server over WiFi
            - Notify my phone when a bed is below its threshold
            - Skip alerts when rain is forecast
            - Show moisture history per bed
Storage:    SQLite
Tech stack: ESP8266, MicroPython, Home Assistant
```

---

## Example 119

**Intent:**
analyze customer support chat logs to find what people ask the most

**Spec:**
```
Type:       Data analysis script (support chat topic mining)
Features:   - Load chat transcripts and keep only customer messages
            - Remove greetings and personal data such as emails and phone numbers
            - Extract topics with BERTopic
            - Rank topics by volume and average chat length
            - Export example chats for each top topic
Input:      JSON export of chat transcripts
Tech stack: Python, BERTopic, Presidio, pandas
```

---

## Example 120

**Intent:**
my sister is a midwife researcher and has a big csv of births, she wants to see if c-section rates differ between hospitals after adjusting for mothers age and risk

**Spec:**
```
Type:       Data analysis script (risk-adjusted hospital comparison)
Features:   - Load birth records with hospital, maternal age, parity and risk factors
            - Fit a logistic regression for caesarean delivery with case-mix covariates
            - Compute observed and expected rates per hospital
            - Draw a funnel plot to show hospitals outside control limits
            - Export an adjusted rate table
Input:      CSV of births with hospital_id, maternal_age, parity, risk_flags, delivery_mode
Tech stack: R, tidyverse, ggplot2
```

---

## Example 121

**Intent:**
Build a pipeline in Airflow that takes our app event logs from S3 each night and builds daily active user tables

**Spec:**
```
Type:       Data pipeline (product analytics)
Features:   - Load the previous day's JSON event logs from S3
            - Validate event schemas and quarantine bad records
            - Deduplicate events by event ID
            - Build daily, weekly and monthly active user tables
            - Send a Slack message if the job fails or row counts drop sharply
Storage:    Amazon Redshift
Tech stack: Apache Airflow, Python, dbt, Amazon S3
```

---

## Example 122

**Intent:**
Analyse grades of my piano students over exams years

**Spec:**
```
Type:       Data analysis script (music exam results)
Features:   - Load exam results per student, grade level and year
            - Calculate pass, merit and distinction rates per grade
            - Track how long students take between grade levels
            - Compare results by exam board section such as pieces, scales and aural
            - Plot progress timelines per student
Input:      Spreadsheet with student, exam_date, grade_level, section_scores, result
Tech stack: Python, pandas, matplotlib
```

---

## Example 123

**Intent:**
speech to text app for my grandma who can't hear well, phone shows what people say

**Spec:**
```
Type:       Mobile application (live captions for hard of hearing)
Features:   - Listen through the phone microphone and show live captions
            - Use large, adjustable text with high contrast
            - Work offline with an on-device speech model
            - Let the user save a conversation transcript
            - Show who is speaking when two voices are detected
Storage:    Local device storage
Tech stack: Kotlin (Android), Vosk speech recognition
```

---

## Example 124

**Intent:**
model to read handwritten digits from old census forms

**Spec:**
```
Type:       Machine learning model (handwritten digit recognition)
Features:   - Crop numeric fields from scanned census form images using the form template
            - Segment fields into single digits
            - Classify digits with a CNN trained on MNIST and fine-tuned on labelled samples
            - Mark low-confidence digits for manual transcription
            - Export recognised values per form to CSV
Input:      Scanned form images (TIFF) and a field coordinate template
Tech stack: Python, OpenCV, PyTorch
```

---

## Example 125

**Intent:**
wats the best time to post on instagram for my bakery page

**Spec:**
```
Type:       Data analysis script (social posting time analysis)
Features:   - Load post insights exported from Instagram
            - Calculate engagement rate per post
            - Group engagement by weekday and hour posted
            - Compare reels, photos and carousels
            - Recommend the top 3 posting times
Input:      CSV export of post insights (posted_at, type, reach, likes, comments, saves)
Tech stack: Python, pandas, seaborn
```

---

## Example 126

**Intent:**
agent that reads our customer emails and drafts replies for the support team to approve

**Spec:**
```
Type:       Web application (support reply drafting agent)
Data model: Ticket(id, customer_email, subject, body, status, received_at)
            DraftReply(id, ticket_id -> Ticket, text, sources, approved_by, sent_at)
Features:   - Pull new tickets from the helpdesk
            - Look up order status and account details through tools
            - Draft a reply with a language model citing the knowledge base
            - Let an agent edit, approve or reject the draft
            - Track how often drafts are sent unchanged
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Claude API (tool use), Zendesk API, React
```

---

## Example 127

**Intent:**
Check if our warehouse pickers are getting faster after the new layout

**Spec:**
```
Type:       Data analysis script (before/after productivity analysis)
Features:   - Load pick events with picker, location and timestamp
            - Calculate picks per hour per picker
            - Compare the 8 weeks before and after the layout change
            - Control for order size and picker experience with a regression
            - Plot weekly picks per hour with the change date marked
Input:      WMS pick log CSV (picker_id, order_id, location, picked_at)
Tech stack: Python, pandas, statsmodels, matplotlib
```

---

## Example 128

**Intent:**
digitize old handwritten recipe cards from my mom

**Spec:**
```
Type:       Command-line tool (handwritten recipe transcription)
Features:   - Read photos of recipe cards
            - Transcribe handwriting with a vision-capable language model
            - Structure each recipe into title, ingredients and steps
            - Save each recipe as a Markdown file
            - Keep the original photo linked in each file
Input:      Folder of recipe card photos
Tech stack: Python, Claude API (vision), Pillow
```

---

## Example 129

**Intent:**
count the number of trees in drone images of our orchard

**Spec:**
```
Type:       Machine learning model (tree counting from drone imagery)
Features:   - Stitch drone images into an orthomosaic
            - Detect individual tree crowns
            - Count trees per block and find missing trees in rows
            - Estimate crown size per tree
            - Export tree locations as a GeoJSON file
Input:      Drone images with GPS tags
Tech stack: Python, OpenDroneMap, DeepForest, GeoPandas
```

---

## Example 130

**Intent:**
What's the gender pay gap in our company? HR gave me a payroll export

**Spec:**
```
Type:       Data analysis script (gender pay gap analysis)
Features:   - Load payroll records with job level, department and tenure
            - Compute mean and median hourly pay gaps
            - Compare pay by gender within the same job level
            - Fit a regression to estimate the adjusted gap
            - Produce charts and tables for the statutory report
Input:      Payroll CSV (employee_id, gender, job_level, department, hours, pay, bonus, start_date)
Tech stack: Python, pandas, statsmodels, matplotlib
```

---

## Example 131

**Intent:**
forecast the number of tourists visiting our island each month next year

**Spec:**
```
Type:       Machine learning model (tourism demand forecasting)
Features:   - Load monthly arrival statistics for the past 15 years
            - Handle the pandemic years as an intervention
            - Fit a seasonal ARIMA model
            - Forecast the next 12 months with prediction intervals
            - Plot forecast against history
Input:      CSV with month and arrivals
Tech stack: R, forecast package, ggplot2
```

---

## Example 132

**Intent:**
Use Power BI to show our hospital bed occupancy across wards

**Spec:**
```
Type:       Data dashboard (bed occupancy)
Features:   - Connect to the patient administration system database
            - Show current occupied, free and blocked beds per ward
            - Show occupancy trend over the last 90 days
            - Highlight wards above 95 percent occupancy
            - Drill down from hospital to ward to bed
Storage:    Microsoft SQL Server
Tech stack: Power BI, DAX, Power Query
```

---

## Example 133

**Intent:**
detect potholes from dashcam video of our city's garbage trucks

**Spec:**
```
Type:       Machine learning model (pothole detection)
Data model: Detection(id, video_id, frame_time, lat, lon, confidence, image_path)
            Pothole(id, lat, lon, first_seen, last_seen, detection_count, status)
Features:   - Extract frames with GPS positions from dashcam footage
            - Detect potholes with an object detection model
            - Merge repeated detections of the same pothole by location
            - Show potholes on a map for the roads department
            - Mark potholes as repaired
Storage:    PostgreSQL with PostGIS
Tech stack: Python, YOLOv8, OpenCV, Leaflet
```

---

## Example 134

**Intent:**
tiny script: give it a csv, it tells me missing values and weird columns

**Spec:**
```
Type:       Command-line script (data profiling)
Features:   - Load any CSV file
            - Report column types, missing value counts and unique counts
            - Detect mixed types and numbers stored as text
            - Show basic stats for numeric columns
            - Save an HTML profile report
Input:      Path to a CSV file
Tech stack: Python, pandas, ydata-profiling
```

---

## Example 135

**Intent:**
I teach a coding bootcamp and want an assistant that gives students hints on their bugs but never the full solution

**Spec:**
```
Type:       Web application (programming hint assistant)
Data model: Exercise(id, title, description, tests)
            Submission(id, exercise_id -> Exercise, student_id, code, test_output, created_at)
            Hint(id, submission_id -> Submission, level, text)
Features:   - Run student code against the exercise tests in a sandbox
            - Give graduated hints, from a nudge to a pointer at the bug line
            - Refuse to output a complete solution
            - Limit hints per exercise
            - Show instructors which exercises need the most hints
Storage:    PostgreSQL
Tech stack: TypeScript, Node.js, Docker (sandbox), Claude API
```

---

## Example 136

**Intent:**
Which shelf positions sell more? We moved products around the shop and have the sales

**Spec:**
```
Type:       Data analysis script (shelf placement effect)
Features:   - Load product placement history and daily sales
            - Label each product-day with shelf height and aisle position
            - Compare sales per placement with a fixed effects regression
            - Control for promotions and seasonality
            - Show the estimated uplift of eye-level placement
Input:      placements.csv (product_id, shelf_level, start_date, end_date) and daily_sales.csv
Tech stack: Python, pandas, linearmodels
```

---

## Example 137

**Intent:**
classify bird photos people upload to our nature club site

**Spec:**
```
Type:       Web application (bird photo identification)
Data model: Member(id, email, name)
            Sighting(id, member_id -> Member, photo_url, species, confidence, location, seen_at, verified)
Features:   - Upload a bird photo with location and date
            - Suggest the top 5 species with a classifier
            - Let experienced members verify or correct species
            - Show a map of verified sightings
            - Show a monthly species list for the region
Storage:    PostgreSQL
Tech stack: Python, Django, PyTorch (EfficientNet), Leaflet
```

---

## Example 138

**Intent:**
we have badge swipe data, find out which meeting rooms nobody uses

**Spec:**
```
Type:       Data analysis script (room utilisation)
Features:   - Load access swipe events per room
            - Join with the room booking calendar export
            - Calculate actual use against booked hours per room
            - Find rooms booked but not used (no-shows)
            - Rank rooms by utilisation with a chart
Input:      Access control CSV (badge_id, door_id, swiped_at) and booking CSV
Tech stack: Python, pandas, Plotly
```

---

## Example 139

**Intent:**
GPT style chatbot that helps tenants report maintenance problems and creates tickets

**Spec:**
```
Type:       Chatbot (tenant maintenance intake)
Data model: Tenant(id, name, unit, phone)
            MaintenanceTicket(id, tenant_id -> Tenant, category, description, urgency, photo_url, status, created_at)
Features:   - Ask follow-up questions to understand the problem
            - Classify category and urgency
            - Ask for a photo when useful
            - Create a ticket in the maintenance system
            - Tell the tenant immediately to call emergency services for gas leaks or flooding
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Claude API, Twilio (WhatsApp)
```

---

## Example 140

**Intent:**
compare test scores of schools in our state over 10 years from public data

**Spec:**
```
Type:       Data analysis script (school performance trends)
Features:   - Download yearly school results files from the state education portal
            - Harmonise school identifiers that changed over time
            - Compute proficiency rate trends per school and district
            - Identify schools with the largest improvements and declines
            - Plot trends for selected schools
Input:      Yearly CSV files from the state education data portal
Tech stack: Python, pandas, Plotly
```

---

## Example 141

**Intent:**
wildlife roadkill reports from citizens, show hotspots

**Spec:**
```
Type:       Web application (roadkill reporting map)
Data model: Report(id, species, lat, lon, observed_at, photo_url, reporter_id)
            Species(id, common_name, scientific_name)
Features:   - Report a roadkill sighting with location and photo
            - Suggest species from the photo
            - Show reports on a map
            - Calculate hotspot road segments with kernel density
            - Export data for wildlife researchers
Storage:    PostgreSQL with PostGIS
Tech stack: Python, GeoDjango, Leaflet
```

---

## Example 142

**Intent:**
help me turn interview transcripts from my research into coded themes

**Spec:**
```
Type:       Data analysis script (qualitative coding assistant)
Features:   - Load interview transcripts
            - Split transcripts into meaningful segments
            - Suggest codes for each segment from my codebook with a language model
            - Let me accept or change codes in an exported spreadsheet
            - Count code frequency per participant
Input:      DOCX transcripts and a codebook spreadsheet
Tech stack: Python, python-docx, Claude API, pandas
```

---

## Example 143

**Intent:**
sensor on the beehive to know weight and temperature remotely

**Spec:**
```
Type:       IoT system (beehive monitoring)
Data model: Hive(id, name, apiary)
            HiveReading(id, hive_id -> Hive, weight_kg, inside_temp_c, humidity_pct, recorded_at)
Features:   - Measure hive weight with load cells and inside temperature
            - Send readings once an hour over LoRa
            - Detect swarming from sudden weight drops
            - Show nectar flow as daily weight change
            - Alert when brood temperature goes out of range
Storage:    InfluxDB
Tech stack: Arduino (HX711, DS18B20), LoRaWAN, Grafana
```

---

## Example 144

**Intent:**
i want to analyse football passes from match event data and see who connects with who

**Spec:**
```
Type:       Data analysis script (football passing networks)
Features:   - Load event data for a match
            - Filter successful passes between players
            - Compute average positions for each player
            - Draw a passing network with edge width by pass count
            - Compute centrality to find key playmakers
Input:      Match event JSON (StatsBomb open data format)
Tech stack: Python, statsbombpy, mplsoccer, NetworkX
```

---

## Example 145

**Intent:**
realtime dashboard of how many people use each gym machine

**Spec:**
```
Type:       IoT system (gym equipment usage)
Data model: Machine(id, name, type, zone)
            UsageSession(id, machine_id -> Machine, started_at, ended_at)
Features:   - Detect machine use with motion sensors on each machine
            - Create usage sessions from start and stop events
            - Show which machines are free right now
            - Show busiest hours per machine type
            - Recommend equipment to buy based on demand
Storage:    PostgreSQL
Tech stack: ESP32, MQTT, Python, FastAPI, Vue.js
```

---

## Example 146

**Intent:**
summarise long customer feedback calls into 5 bullet points with python

**Spec:**
```
Type:       Command-line script (call summarisation)
Features:   - Transcribe each recording with timestamps
            - Summarise the call into 5 bullet points
            - Extract mentioned products and feature requests
            - Save summaries as a CSV with one row per call
            - Skip calls shorter than one minute
Input:      Folder of call recordings (MP3)
Tech stack: Python, OpenAI Whisper, Claude API, pandas
```

---

## Example 147

**Intent:**
Model to predict which kids in our district need reading support at age 6

**Spec:**
```
Type:       Machine learning model (early reading risk screening)
Features:   - Combine kindergarten screening scores, attendance and language background
            - Train an interpretable logistic regression
            - Choose a cut-off that catches most at-risk children
            - Check error rates across demographic groups
            - Produce a list for reading specialists with the main risk factors per child
Input:      CSV of kindergarten assessment data and later reading outcomes
Tech stack: Python, scikit-learn, Fairlearn, pandas
```

---

## Example 148

**Intent:**
help us understand why our website visitors leave on the pricing page

**Spec:**
```
Type:       Data analysis script (funnel drop-off analysis)
Features:   - Load page view events with session IDs
            - Build the funnel from landing page to signup
            - Compute drop-off rate at each step
            - Compare drop-off by device, country and traffic source
            - Show the most common paths taken after the pricing page
Input:      Event export (session_id, page, timestamp, device, country, source)
Tech stack: Python, pandas, Plotly (Sankey diagram)
```

---

## Example 149

**Intent:**
ocr for old newspapers in our town archive so people can search them

**Spec:**
```
Type:       Web application (historical newspaper archive search)
Data model: Issue(id, newspaper, publication_date)
            Page(id, issue_id -> Issue, page_number, image_path, ocr_text)
Features:   - Run OCR on scanned newspaper pages with layout detection
            - Correct common OCR errors with a spelling model
            - Index text for full-text search
            - Show search hits highlighted on the page image
            - Browse issues by date
Storage:    PostgreSQL, Elasticsearch
Tech stack: Python, Tesseract, Kraken OCR, Django, OpenSeadragon
```

---

## Example 150

**Intent:**
k-means cluster our customers into groups from purchase data

**Spec:**
```
Type:       Data analysis script (customer segmentation)
Features:   - Compute recency, frequency and monetary value per customer
            - Scale features and choose the number of clusters with silhouette scores
            - Run k-means clustering
            - Describe each cluster with average values
            - Export customer IDs with their segment
Input:      Orders CSV (customer_id, order_date, amount)
Tech stack: Python, pandas, scikit-learn
```

---

## Example 151

**Intent:**
a tool to check the accessibility of PDFs our university publishes

**Spec:**
```
Type:       Command-line tool (PDF accessibility checker)
Features:   - Check that each PDF is tagged and has a document title and language
            - Detect images without alternative text
            - Check heading structure and reading order
            - Flag scanned pages with no text layer
            - Output a report per file with a pass or fail summary
Input:      Folder of PDF files or a list of URLs
Tech stack: Python, pikepdf, veraPDF (PDF/UA validation)
```

---

## Example 152

**Intent:**
track the moods i write in my journal app over time with AI

**Spec:**
```
Type:       Data analysis script (journal mood tracking)
Features:   - Export journal entries with dates
            - Score each entry's emotions with a pretrained emotion classifier
            - Compute weekly average mood scores
            - Find words most linked to good and bad days
            - Plot mood over time with notable entries labelled
Input:      Journal export (JSON or Markdown files with dates)
Tech stack: Python, Hugging Face Transformers, pandas, matplotlib
```

---

## Example 153

**Intent:**
anomaly detection on our server logs to catch weird behavior

**Spec:**
```
Type:       Machine learning model (log anomaly detection)
Features:   - Parse raw logs into templates with Drain
            - Count template frequencies in 5-minute windows
            - Train an Isolation Forest on normal periods
            - Score new windows in near real time
            - Send alerts with the top unusual log templates to Slack
Input:      Application log stream
Tech stack: Python, drain3, scikit-learn, Kafka
```

---

## Example 154

**Intent:**
Plz build smth to tell which of my youtube video titles got best clickrate

**Spec:**
```
Type:       Data analysis script (YouTube title performance)
Features:   - Pull video statistics through the YouTube Analytics API
            - Calculate click-through rate and average view duration per video
            - Extract title features such as length, numbers and questions
            - Compare CTR across title features
            - List the top and bottom 10 titles
Input:      YouTube channel access via OAuth
Tech stack: Python, google-api-python-client, pandas
```

---

## Example 155

**Intent:**
we're an NGO that has malaria case data per village, map it and find clusters

**Spec:**
```
Type:       Data analysis script (disease case clustering)
Features:   - Load case counts and village coordinates
            - Compute incidence per 1,000 population
            - Detect spatial clusters with a scan statistic
            - Map incidence and clusters
            - Export a list of villages in high-risk clusters
Input:      CSV with village_id, lat, lon, population, cases, month
Tech stack: R, sf, SpatialEpi, leaflet
```

---

## Example 156

**Intent:**
A desktop app where I can drag in a folder of microscope images and count the cells

**Spec:**
```
Type:       Desktop application (cell counting)
Features:   - Load microscope images from a folder
            - Segment cells with a pretrained segmentation model
            - Count cells and measure their area per image
            - Let the user adjust detection thresholds and see an overlay
            - Export counts and measurements to CSV
Input:      Folder of TIFF microscope images
Tech stack: Python, Cellpose, napari
```

---

## Example 157

**Intent:**
Interview transcripts of job candidates should be scored on the same rubric by an AI, but we want humans to make the decision

**Spec:**
```
Type:       Web application (structured interview scoring assistant)
Data model: Role(id, title, rubric)
            Interview(id, role_id -> Role, candidate_ref, transcript, recorded_at)
            RubricScore(id, interview_id -> Interview, criterion, ai_score, evidence, human_score)
Features:   - Upload interview transcripts
            - Score each rubric criterion with a quoted evidence passage
            - Hide candidate names and demographic details from the scorer
            - Require a human score for every criterion before a decision
            - Compare AI and human scores to monitor agreement
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Claude API, React
```

---

## Example 158

**Intent:**
Mi tesis: datos de temperatura de 30 estaciones meteorologicas, quiero ver tendencias de calentamiento

**Spec:**
```
Type:       Data analysis script (climate trend analysis)
Features:   - Load daily temperature series from 30 stations
            - Fill short gaps and flag stations with too much missing data
            - Compute annual mean temperature anomalies
            - Estimate trends with the Mann-Kendall test and Sen's slope
            - Map trend magnitude per station
Input:      CSV per station with date, tmin, tmax
Tech stack: Python, pandas, pymannkendall, Cartopy
```

---

## Example 159

**Intent:**
Show me what words people search on our website but find nothing

**Spec:**
```
Type:       Data analysis script (zero-result search analysis)
Features:   - Load site search logs
            - Find queries that returned zero results
            - Group similar queries with fuzzy matching
            - Rank query groups by frequency
            - Suggest synonyms or missing content for top groups
Input:      Search log CSV (query, results_count, searched_at)
Tech stack: Python, pandas, RapidFuzz
```

---

## Example 160

**Intent:**
Make a model that reads chest x-rays and flags possible pneumonia for a radiologist to check first

**Spec:**
```
Type:       Machine learning model (chest X-ray triage)
Features:   - Preprocess DICOM images to normalised arrays
            - Fine-tune a DenseNet on labelled chest X-ray datasets
            - Output a pneumonia probability and a heatmap of the region
            - Re-order the radiologist worklist by risk
            - Report sensitivity and specificity on a held-out hospital dataset
Input:      DICOM chest X-ray images with labels
Tech stack: Python, PyTorch, MONAI, pydicom
```

---

## Example 161

**Intent:**
I want a bot on Twitch that detects toxic chat messages and times out the user

**Spec:**
```
Type:       Bot (Twitch chat moderation)
Features:   - Read chat messages from a Twitch channel
            - Score each message for toxicity with a classifier
            - Delete messages above a threshold and time out repeat offenders
            - Let moderators whitelist words and users
            - Log moderation actions for review
Tech stack: Python, TwitchIO, Detoxify
```

---

## Example 162

**Intent:**
forecast hourly electricity price for my battery to charge cheap

**Spec:**
```
Type:       Machine learning model (electricity price forecasting)
Features:   - Download day-ahead market prices and wind and solar forecasts
            - Train a model for next-day hourly prices
            - Plan battery charge and discharge hours to maximise savings
            - Respect battery capacity and charging power limits
            - Send the schedule to the home battery controller
Input:      Day-ahead price API and weather forecast API
Tech stack: Python, ENTSO-E API, LightGBM, PuLP
```

---

## Example 163

**Intent:**
what day of week has the most accidents at our factory

**Spec:**
```
Type:       Data analysis script (workplace incident analysis)
Features:   - Load the incident register
            - Count incidents per weekday, shift and department
            - Normalise counts by hours worked
            - Show the most common incident types
            - Plot incident rates by weekday and shift
Input:      Excel incident register (date, time, shift, department, type, severity)
Tech stack: Python, pandas, matplotlib
```

---

## Example 164

**Intent:**
simple webpage where i upload a photo of a math problem and it explains the solution step by step

**Spec:**
```
Type:       Web application (math homework explainer)
Features:   - Upload or take a photo of a math problem
            - Read the problem with a vision model and confirm it with the user
            - Explain the solution step by step
            - Let the user ask about any step
            - Offer a similar practice problem
Tech stack: Python, Flask, Claude API (vision), MathJax
```

---

## Example 165

**Intent:**
pipeline that cleans our raw clinical trial data and produces SDTM datasets

**Spec:**
```
Type:       Data pipeline (clinical trial data standardisation)
Features:   - Import raw EDC exports
            - Map raw variables to SDTM domains such as DM, AE and VS
            - Apply controlled terminology
            - Run validation checks and list issues
            - Write SAS transport (XPT) files and define.xml
Input:      EDC export CSVs and a mapping specification spreadsheet
Tech stack: R, admiral, sdtm.oak, xportr
```

---

## Example 166

**Intent:**
homework completion rates by class

**Spec:**
```
Type:       Data analysis script (homework completion tracking)
Features:   - Load homework submission records from the learning platform export
            - Compute completion rate per student, class and subject
            - Find students missing three or more assignments in a row
            - Compare completion before and after holidays
            - Export a list for form tutors
Input:      CSV export with student_id, class, subject, assignment_id, due_date, submitted_at
Tech stack: Python, pandas, openpyxl
```

---

## Example 167

**Intent:**
sleep apnea detection from overnight oximeter data

**Spec:**
```
Type:       Data analysis script (oxygen desaturation analysis)
Features:   - Load overnight SpO2 and pulse readings
            - Remove motion artefacts and invalid readings
            - Detect desaturation events of 3 percent or more
            - Compute the oxygen desaturation index per hour
            - Plot the night with events marked
Input:      Oximeter CSV export (timestamp, spo2, pulse)
Tech stack: Python, pandas, SciPy, matplotlib
```

---

## Example 168

**Intent:**
a thing that listens to a classroom recording and tells the teacher how much they talked vs the students

**Spec:**
```
Type:       Data analysis script (classroom talk-time analysis)
Features:   - Run speaker diarization on the lesson recording
            - Identify the teacher's voice from a short enrolment sample
            - Compute teacher and student talk-time percentages
            - Count questions asked by the teacher
            - Show a timeline of who spoke when
Input:      Lesson audio recording (WAV or MP3) and a 30-second teacher voice sample
Tech stack: Python, pyannote.audio, faster-whisper, matplotlib
```

---

## Example 169

**Intent:**
churn analysis for my saas, cohort charts

**Spec:**
```
Type:       Data analysis script (subscription cohort retention)
Features:   - Load subscription start and cancel dates
            - Group customers into monthly signup cohorts
            - Compute retention for each cohort by month since signup
            - Draw a cohort retention heatmap
            - Calculate monthly revenue churn and net revenue retention
Input:      Stripe subscriptions export (CSV)
Tech stack: Python, pandas, seaborn
```

---

## Example 170

**Intent:**
My uncle owns 3 petrol stations and wants to know how much fuel to order each week so the tanks never run dry

**Spec:**
```
Type:       Data analysis script (fuel replenishment planning)
Features:   - Load daily tank level readings and deliveries per station
            - Estimate daily fuel sales per grade
            - Forecast next week's sales with weekly seasonality
            - Calculate order quantities that respect tank capacity and safety stock
            - Print an order sheet per station
Input:      Tank gauge export CSV (station, grade, date, level_litres, delivery_litres)
Tech stack: Python, pandas, statsmodels
```

---

## Example 171

**Intent:**
identify which species of whale is singing from hydrophone recordings

**Spec:**
```
Type:       Machine learning model (marine mammal call classification)
Features:   - Split hydrophone recordings into overlapping windows
            - Convert windows to spectrograms
            - Detect candidate calls with an energy detector
            - Classify calls by species with a CNN
            - Export detections with time, species and confidence
Input:      Long hydrophone recordings (FLAC)
Tech stack: Python, librosa, TensorFlow, pandas
```

---

## Example 172

**Intent:**
sentiment over time of what news says about our company

**Spec:**
```
Type:       Scheduled script (media sentiment tracking)
Data model: Article(id, source, url, title, published_at, sentiment_score)
Features:   - Search news APIs daily for the company name
            - Remove duplicate syndicated articles
            - Score article sentiment with a financial sentiment model
            - Compute weekly average sentiment and volume
            - Email a chart of the trend with the most negative headlines
Storage:    SQLite
Tech stack: Python, NewsAPI, FinBERT, matplotlib
```

---

## Example 173

**Intent:**
kids reading app that listens to child reading aloud and marks words they got wrong

**Spec:**
```
Type:       Mobile application (reading fluency assessment)
Data model: Child(id, name, reading_level)
            ReadingSession(id, child_id -> Child, passage_id, words_correct_per_minute, recorded_at)
            WordError(id, session_id -> ReadingSession, word, error_type)
Features:   - Show a passage at the child's level
            - Record the child reading aloud
            - Align speech recognition output with the passage text
            - Mark skipped, substituted and mispronounced words
            - Track words correct per minute over time for parents
Storage:    Firebase Firestore
Tech stack: Flutter, Google Cloud Speech-to-Text, Firebase
```

---

## Example 174

**Intent:**
analyze grocery receipts to track inflation on what I buy

**Spec:**
```
Type:       Data analysis script (personal inflation tracking)
Features:   - Load itemised grocery purchases from receipt scans
            - Match the same product across shops and pack sizes
            - Compute price per unit over time
            - Calculate a personal inflation index weighted by my spending
            - Compare it with the official consumer price index
Input:      CSV of receipt line items (date, shop, item, quantity, unit, price)
Tech stack: Python, pandas, RapidFuzz, matplotlib
```

---

## Example 175

**Intent:**
anpr camera at our car park gate to open for registered cars

**Spec:**
```
Type:       IoT system (licence plate gate control)
Data model: Vehicle(id, plate_number, owner_name, valid_until)
            GateEvent(id, plate_read, confidence, matched_vehicle_id -> Vehicle, decision, image_path, occurred_at)
Features:   - Capture an image when a car stops at the gate
            - Read the plate number with ANPR
            - Open the gate for registered vehicles via a relay
            - Log every event with the image
            - Let admins add vehicles and view logs in a web page
Storage:    SQLite
Tech stack: Raspberry Pi, Python, OpenALPR, Flask
```

---

## Example 176

**Intent:**
build a gradio demo for my image captioning model

**Spec:**
```
Type:       Web application (image captioning demo)
Features:   - Upload an image or take one from the webcam
            - Generate a caption with the trained model
            - Show the top 3 captions with beam search scores
            - Let users rate captions as good or bad
            - Log ratings to a CSV for later evaluation
Tech stack: Python, Gradio, PyTorch, Hugging Face Transformers
```

---

## Example 177

**Intent:**
help, my phd lab collects mouse behaviour videos and someone watches them by hand to score grooming

**Spec:**
```
Type:       Machine learning model (animal behaviour classification)
Features:   - Track body keypoints of the mouse in each video with pose estimation
            - Compute movement features from keypoints
            - Train a classifier on hand-scored grooming bouts
            - Score new videos and output bout start and end times
            - Compare automatic and manual scores with agreement statistics
Input:      Top-down mouse videos and hand-scored annotation files
Tech stack: Python, DeepLabCut, SimBA, scikit-learn
```

---

## Example 178

**Intent:**
Create a dashboard in Tableau about our school district's budget per student

**Spec:**
```
Type:       Data dashboard (school budget per pupil)
Features:   - Combine budget lines with enrolment numbers per school
            - Show spending per pupil by school and category
            - Compare schools against the district average
            - Show five-year trends
            - Filter by school level and spending category
Input:      Budget Excel files and enrolment CSV
Tech stack: Tableau
```

---

## Example 179

**Intent:**
tool for journalists to check if a quote has appeared online before

**Spec:**
```
Type:       Web application (quote provenance search)
Features:   - Paste a quote and search the web for exact and close matches
            - Sort matches by earliest publication date
            - Show the context around each match
            - Flag quotes commonly misattributed to famous people
            - Save searches in a project for later
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Bing Web Search API, Wayback Machine API
```

---

## Example 180

**Intent:**
speech-to-text + translation for our church service so visitors can follow in their language

**Spec:**
```
Type:       Web application (live sermon translation)
Data model: Service(id, title, started_at)
            Segment(id, service_id -> Service, source_text, start_ms)
            SegmentTranslation(id, segment_id -> Segment, language, text)
Features:   - Capture the preacher's microphone feed
            - Transcribe speech live
            - Translate each sentence into selected languages
            - Let visitors open a link and pick their language on their phone
            - Save the full bilingual transcript after the service
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Deepgram API, Google Cloud Translation, Vue.js
```

---

## Example 181

**Intent:**
check which doctors prescribe much more antibiotics than others

**Spec:**
```
Type:       Data analysis script (prescribing variation analysis)
Features:   - Load prescription records per prescriber
            - Compute antibiotic prescriptions per 1,000 patients
            - Adjust rates for patient age mix
            - Flag prescribers above the 95th percentile
            - Show a funnel plot of practice rates
Input:      Prescription data CSV (prescriber_id, practice, drug_class, items, patient_count)
Tech stack: Python, pandas, matplotlib
```

---

## Example 182

**Intent:**
An AI that writes alt text for all the images on our website

**Spec:**
```
Type:       Command-line tool (alt text generation)
Features:   - Crawl the website and find images with missing or poor alt text
            - Generate concise alt text with a vision language model using page context
            - Mark decorative images for empty alt attributes
            - Export suggestions to a CSV for editors to review
            - Push approved alt text back to the CMS
Input:      Website URL or sitemap
Tech stack: Python, Scrapy, Claude API (vision), WordPress REST API
```

---

## Example 183

**Intent:**
predict which roads need repair next year

**Spec:**
```
Type:       Machine learning model (road maintenance prioritisation)
Features:   - Combine pavement condition surveys, traffic volume, road age and weather
            - Train a model to predict next year's condition index
            - Rank segments by predicted deterioration and traffic
            - Estimate repair cost per segment
            - Export a prioritised list as a GIS layer
Input:      Pavement survey CSV, traffic counts and road segment shapefile
Tech stack: Python, GeoPandas, XGBoost
```

---

## Example 184

**Intent:**
compare crime stats before and after streetlights were installed

**Spec:**
```
Type:       Data analysis script (intervention impact analysis)
Features:   - Load police incident data with locations and dates
            - Select streets with new lights and comparable control streets
            - Count night-time incidents per month for both groups
            - Estimate the effect with a difference-in-differences model
            - Plot trends with the installation date marked
Input:      Incident CSV (date, time, lat, lon, category) and streetlight installation list
Tech stack: Python, GeoPandas, statsmodels, matplotlib
```

---

## Example 185

**Intent:**
whatsapp bot for farmers to ask about crop diseases by sending a photo

**Spec:**
```
Type:       Bot (WhatsApp crop advisory)
Data model: Farmer(id, phone, region, language)
            Query(id, farmer_id -> Farmer, image_url, crop, diagnosis, advice, created_at)
Features:   - Receive a crop photo and question over WhatsApp
            - Classify the disease with an image model
            - Reply with treatment advice in the farmer's language
            - Send a voice note for farmers who prefer audio
            - Escalate unclear cases to an agronomist
Storage:    PostgreSQL
Tech stack: Python, FastAPI, WhatsApp Business Cloud API, TensorFlow
```

---

## Example 186

**Intent:**
which features of our app do people actually use

**Spec:**
```
Type:       Data analysis script (feature adoption analysis)
Features:   - Load product event data
            - Map events to named features
            - Compute percent of active users using each feature weekly
            - Find features used by retained users more than churned users
            - Chart adoption for the last 6 months
Input:      Event export (user_id, event_name, timestamp) and a feature mapping sheet
Tech stack: Python, pandas, Plotly
```

---

## Example 187

**Intent:**
we need to anonymize patient records before sharing them with researchers

**Spec:**
```
Type:       Data pipeline (clinical data de-identification)
Features:   - Remove direct identifiers such as names, addresses and phone numbers
            - Detect identifiers in free-text notes with named entity recognition
            - Shift dates by a random offset per patient
            - Generalise ages over 89 and rare postcodes
            - Check k-anonymity on quasi-identifiers before release
Input:      Patient tables (CSV) and clinical notes (text)
Tech stack: Python, Microsoft Presidio, pandas, ARX (k-anonymity)
```

---

## Example 188

**Intent:**
robot vacuum style map of where my cat walks using little BLE tag

**Spec:**
```
Type:       IoT system (pet indoor tracking)
Features:   - Place BLE receivers in each room
            - Estimate the tag's room from signal strength
            - Log room changes with timestamps
            - Show a heatmap of time spent per room
            - Alert if the cat enters a forbidden room
Storage:    SQLite
Tech stack: ESP32, ESPresense, Home Assistant, MQTT
```

---

## Example 189

**Intent:**
rank our sales leads by how likely they are to buy, we use salesforce

**Spec:**
```
Type:       Machine learning model (lead scoring)
Features:   - Pull leads and their activity history from Salesforce
            - Build features from company size, industry, source and engagement
            - Train a gradient boosting classifier on converted leads
            - Write the score back to a custom Salesforce field nightly
            - Show the top reasons for each lead's score
Tech stack: Python, simple-salesforce, LightGBM, SHAP
```

---

## Example 190

**Intent:**
graphs of my bitcoin mining rig temperature and hashrate

**Spec:**
```
Type:       Data dashboard (mining rig monitoring)
Features:   - Collect GPU temperature, fan speed, power and hashrate every 30 seconds
            - Store metrics in a time series database
            - Show live and historical graphs
            - Alert by Telegram when a GPU overheats or hashrate drops
            - Calculate daily power cost
Storage:    Prometheus
Tech stack: Python (exporter), Prometheus, Grafana
```

---

## Example 191

**Intent:**
an AI that checks our marketing copy against brand guidelines

**Spec:**
```
Type:       Web application (brand guideline checker)
Data model: Guideline(id, category, rule, examples)
            CopyCheck(id, user_id, text, issues, created_at)
Features:   - Paste or upload marketing copy
            - Check tone, banned words and terminology against the guidelines with a language model
            - Highlight each issue with the rule it breaks
            - Suggest compliant alternatives
            - Let brand managers edit guidelines
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Claude API
```

---

## Example 192

**Intent:**
Figure out from our point of sale which menu items make the most profit, not just sales

**Spec:**
```
Type:       Data analysis script (menu engineering)
Features:   - Load item sales from the POS export
            - Join with recipe costs per item
            - Calculate contribution margin and popularity per item
            - Classify items into stars, plowhorses, puzzles and dogs
            - Plot the menu engineering matrix
Input:      POS sales CSV and a recipe cost spreadsheet
Tech stack: Python, pandas, matplotlib
```

---

## Example 193

**Intent:**
forecast how many students will enroll in each course next semester

**Spec:**
```
Type:       Machine learning model (course enrolment forecasting)
Features:   - Load historical enrolments per course and term
            - Add features for programme intake, prerequisites passed and course changes
            - Train a regression model per course group
            - Predict next term's enrolment with intervals
            - Recommend the number of sections per course
Input:      Enrolment history CSV and current student progress data
Tech stack: Python, pandas, scikit-learn
```

---

## Example 194

**Intent:**
transcribe police bodycam audio for court records

**Spec:**
```
Type:       Data pipeline (evidence transcription)
Data model: Recording(id, case_number, officer_id, file_path, sha256, recorded_at)
            Transcript(id, recording_id -> Recording, text, reviewed_by, reviewed_at)
Features:   - Ingest recordings and store a hash for chain of custody
            - Transcribe audio with timestamps and speaker labels
            - Let a clerk review and correct the transcript
            - Lock the transcript after review
            - Export a certified transcript PDF
Storage:    PostgreSQL, encrypted object storage
Tech stack: Python, WhisperX, Django, ReportLab
```

---

## Example 195

**Intent:**
Check our wind turbines SCADA data for underperforming turbines

**Spec:**
```
Type:       Data analysis script (wind turbine performance)
Features:   - Load 10-minute SCADA data per turbine
            - Filter out curtailment and downtime periods
            - Build an empirical power curve per turbine
            - Compare each turbine against the farm reference curve
            - Rank turbines by estimated lost energy
Input:      SCADA CSV (turbine_id, timestamp, wind_speed, power_kw, status)
Tech stack: Python, pandas, NumPy, matplotlib
```

---

## Example 196

**Intent:**
text classifier for legal documents: contract, NDA, invoice, letter

**Spec:**
```
Type:       Machine learning model (legal document type classification)
Features:   - Extract text from PDF and DOCX files
            - Train a classifier on labelled documents
            - Use the first two pages and layout features
            - Evaluate accuracy per document type
            - Provide a CLI that sorts a folder of documents into subfolders by type
Input:      Labelled folder of documents
Tech stack: Python, pdfplumber, scikit-learn, Typer
```

---

## Example 197

**Intent:**
how long do our github issues stay open, by label

**Spec:**
```
Type:       Data analysis script (issue resolution time)
Features:   - Fetch issues and their labels through the GitHub API
            - Compute time to first response and time to close
            - Break down times by label and assignee
            - Find long-open issues without activity
            - Plot monthly median resolution time
Input:      GitHub repository name and access token
Tech stack: Python, PyGithub, pandas, matplotlib
```

---

## Example 198

**Intent:**
ok so i do pottery and sell at markets, i kept a notebook of every sale for 2 years, typed it into excel. which items and which markets are worth my time

**Spec:**
```
Type:       Data analysis script (market stall sales analysis)
Features:   - Load sales records from the spreadsheet
            - Calculate revenue and items sold per market day
            - Subtract stall fees and travel costs per market
            - Rank markets by profit per hour
            - Show best-selling item types by season
Input:      Excel file with date, market, item_type, price, plus a sheet of market fees and hours
Tech stack: Python, pandas, matplotlib
```

---

## Example 199

**Intent:**
Build me a REST API that returns air pollution forecasts per neighbourhood

**Spec:**
```
Type:       REST API service (air quality forecast)
Data model: Neighbourhood(id, name, geometry)
            Forecast(id, neighbourhood_id -> Neighbourhood, valid_at, pm25, no2, o3, aqi)
Features:   - Pull hourly model forecasts from the regional air quality service
            - Aggregate gridded forecasts to neighbourhood polygons
            - Compute an air quality index per hour
            - Return forecasts for the next 48 hours
            - Cache responses for 30 minutes
Storage:    PostgreSQL with PostGIS, Redis
Tech stack: Python, FastAPI, xarray, Copernicus CAMS API
```

---

## Example 200

**Intent:**
speech analytics: detect angry customers in call center calls

**Spec:**
```
Type:       Machine learning model (speech emotion detection)
Features:   - Extract acoustic features such as pitch, energy and speaking rate
            - Combine audio features with transcript sentiment
            - Train a classifier for calm, frustrated and angry
            - Mark the time points where anger appears
            - Alert supervisors for live calls above an anger threshold
Input:      Call audio with labelled emotion segments
Tech stack: Python, openSMILE, faster-whisper, PyTorch
```

---

## Example 201

**Intent:**
tell me if students' scores went down after we switched to online exams

**Spec:**
```
Type:       Data analysis script (exam mode comparison)
Features:   - Load exam scores from paper and online years
            - Match courses and exam types across years
            - Compare score distributions with a Mann-Whitney test
            - Control for course and cohort with a mixed-effects model
            - Plot score distributions side by side
Input:      Exam results CSV (course, year, mode, student_id, score)
Tech stack: R, lme4, ggplot2
```

---

## Example 202

**Intent:**
classify recycling items from a camera above the conveyor belt

**Spec:**
```
Type:       Machine learning model (waste sorting vision)
Features:   - Capture images of items on the conveyor
            - Classify items into plastic types, paper, metal and glass
            - Send the class and position to the air-jet sorter
            - Track sorting accuracy from manual audits
            - Run inference on an edge GPU at 30 frames per second
Tech stack: Python, PyTorch, TensorRT, NVIDIA Jetson, OpenCV
```

---

## Example 203

**Intent:**
Data dashboard of our donation campaign that the team can see live

**Spec:**
```
Type:       Data dashboard (fundraising campaign)
Features:   - Pull donations from the payment platform every 5 minutes
            - Show total raised against the goal
            - Show donations per day and per channel
            - Show average gift and new versus returning donors
            - Show a live ticker of recent donations without personal details
Tech stack: Python, Stripe API, Streamlit
```

---

## Example 204

**Intent:**
Can we predict drug side effects from the structure of the molecule? school project

**Spec:**
```
Type:       Machine learning model (molecular toxicity prediction)
Features:   - Load molecules as SMILES strings with side-effect labels
            - Convert molecules to Morgan fingerprints
            - Train a multi-label classifier
            - Evaluate with ROC AUC per side effect
            - Show which substructures increase predicted risk
Input:      SIDER or Tox21 dataset (CSV with SMILES and labels)
Tech stack: Python, RDKit, scikit-learn
```

---

## Example 205

**Intent:**
Build a Kafka pipeline that enriches clickstream events with user country and device in real time

**Spec:**
```
Type:       Data pipeline (real-time clickstream enrichment)
Features:   - Consume raw click events from a Kafka topic
            - Look up country from IP address with a GeoIP database
            - Parse device and browser from the user agent
            - Drop bot traffic
            - Publish enriched events to a new topic and to the data lake
Storage:    Apache Kafka, Amazon S3 (Parquet)
Tech stack: Java, Kafka Streams, MaxMind GeoIP2, ua-parser
```

---

## Example 206

**Intent:**
Help me compare the nutrition of school lunch menus against government guidelines

**Spec:**
```
Type:       Data analysis script (school meal nutrition check)
Features:   - Load weekly menus with recipes and portion sizes
            - Calculate nutrients per meal from a food composition table
            - Compare averages against the official guidelines
            - Flag days high in salt or sugar
            - Produce a report per school
Input:      Menu spreadsheet and recipe ingredient lists
Tech stack: Python, pandas, openpyxl
```

---

## Example 207

**Intent:**
alert me when stock prices in my watchlist move more than usual

**Spec:**
```
Type:       Scheduled script (stock volatility alerts)
Features:   - Fetch intraday prices for watchlist tickers every 15 minutes during market hours
            - Compute returns against each stock's 30-day volatility
            - Alert when a move exceeds 2 standard deviations
            - Include recent news headlines in the alert
            - Send alerts by Telegram
Tech stack: Python, yfinance, pandas, python-telegram-bot
```

---

## Example 208

**Intent:**
how many hours do my employees actually work vs their contracts, from the time clock data

**Spec:**
```
Type:       Data analysis script (time clock analysis)
Features:   - Load clock-in and clock-out events
            - Pair events into shifts and handle missing clock-outs
            - Compute weekly hours per employee
            - Compare with contracted hours and flag overtime
            - Export a monthly summary for payroll
Input:      Time clock CSV (employee_id, event_type, timestamp) and contract hours sheet
Tech stack: Python, pandas, openpyxl
```

---

## Example 209

**Intent:**
Language model that helps fill out disability benefit application forms

**Spec:**
```
Type:       Web application (benefit form assistant)
Data model: Applicant(id, email)
            Application(id, applicant_id -> Applicant, form_type, answers, status)
            Document(id, application_id -> Application, file_url, doc_type)
Features:   - Ask the applicant questions in plain language
            - Map answers to the official form fields
            - Explain what each question means with examples
            - Check for missing answers and supporting documents
            - Generate a filled PDF form for the applicant to review and submit
Storage:    PostgreSQL
Tech stack: Python, Django, Claude API, pypdf
```

---

## Example 210

**Intent:**
clustering of patients with similar symptoms from survey

**Spec:**
```
Type:       Data analysis script (symptom profile clustering)
Features:   - Load symptom checklist responses
            - Encode symptom answers and handle missing data
            - Cluster patients with latent class analysis
            - Describe each class by its most common symptoms
            - Compare classes by age and sex
Input:      CSV with one row per patient and binary symptom columns
Tech stack: R, poLCA, tidyverse
```

---

## Example 211

**Intent:**
ai that writes product descriptions from our supplier spreadsheets

**Spec:**
```
Type:       Command-line tool (product description generation)
Features:   - Read product attributes from a supplier spreadsheet
            - Generate SEO-friendly descriptions with a language model
            - Keep a consistent tone using a style guide prompt
            - Flag products with missing attributes instead of guessing
            - Write descriptions back to a new column
Input:      Excel file of products with attributes
Tech stack: Python, openpyxl, Claude API
```

---

## Example 212

**Intent:**
Is there a link between noise outside schools and test scores? I have both datasets

**Spec:**
```
Type:       Data analysis script (environmental exposure correlation)
Features:   - Join school locations with modelled road noise levels
            - Merge school test score averages
            - Control for deprivation index and school size
            - Fit a multiple regression
            - Map schools coloured by noise exposure
Input:      School CSV with coordinates and scores, and a noise raster (GeoTIFF)
Tech stack: Python, GeoPandas, rasterio, statsmodels
```

---

## Example 213

**Intent:**
Make a bot that posts daily stats of our open-source project to Discord

**Spec:**
```
Type:       Bot (open-source project stats)
Features:   - Collect stars, forks, downloads and open issues daily
            - Compare with the previous day and week
            - Post a formatted summary in a Discord channel
            - Celebrate milestones such as 1,000 stars
            - Store daily history for charts
Storage:    SQLite
Tech stack: Python, PyGithub, PyPI Stats API, discord.py
```

---

## Example 214

**Intent:**
read the gas meter dial with a webcam and log my usage

**Spec:**
```
Type:       IoT system (analogue meter reading)
Features:   - Capture a webcam image every 5 minutes
            - Read dial positions with image processing
            - Convert dial readings to cubic metres
            - Store readings and compute hourly usage
            - Show daily gas use on a dashboard
Storage:    InfluxDB
Tech stack: Raspberry Pi, Python, OpenCV, Grafana
```

---

## Example 215

**Intent:**
help me pick the best location for a new pharmacy using census data

**Spec:**
```
Type:       Data analysis script (site selection analysis)
Features:   - Load census population and age data per area
            - Map existing pharmacies
            - Compute travel time from each area to the nearest pharmacy
            - Score candidate sites by underserved elderly population
            - Map the top 10 candidate locations
Input:      Census CSV per area, area boundaries and pharmacy locations
Tech stack: Python, GeoPandas, OSMnx, Folium
```

---

## Example 216

**Intent:**
attendance csv -> which kids miss mondays

**Spec:**
```
Type:       Command-line script (weekday absence pattern)
Features:   - Load daily attendance records
            - Compute absence rate per student for each weekday
            - Flag students whose Monday or Friday absence is double their average
            - Print a sorted list of flagged students
            - Save the result to CSV
Input:      Attendance CSV (student_id, date, present)
Tech stack: Python, pandas
```

---

## Example 217

**Intent:**
hi i'm a nurse manager, we track falls of patients on paper and then excel, can you show which wards and times have most falls

**Spec:**
```
Type:       Data analysis script (inpatient falls analysis)
Features:   - Load the falls register
            - Count falls per ward, hour of day and day of week
            - Normalise by occupied bed days per ward
            - Show a heatmap of falls by ward and hour
            - Summarise injury severity per ward
Input:      Excel falls register (date, time, ward, injury_level) and monthly bed days sheet
Tech stack: Python, pandas, seaborn
```

---

## Example 218

**Intent:**
crowd counting from a photo of a protest

**Spec:**
```
Type:       Machine learning model (crowd density estimation)
Features:   - Load a high-resolution crowd image
            - Predict a density map with a pretrained crowd counting network
            - Sum the density map to estimate the number of people
            - Split large images into tiles to keep resolution
            - Save the density heatmap overlay and estimate
Input:      JPEG image of a crowd
Tech stack: Python, PyTorch, CSRNet, OpenCV
```

---

## Example 219

**Intent:**
wanna make a pipeline to get all the spotify podcast reviews in and tag topics

**Spec:**
```
Type:       Data pipeline (podcast review topic tagging)
Features:   - Collect listener reviews from podcast platforms daily
            - Store new reviews and skip ones already seen
            - Tag topics such as audio quality, host, guests and ads
            - Score sentiment per review
            - Write a weekly CSV for the producers
Storage:    PostgreSQL
Tech stack: Python, Prefect, Apple Podcasts RSS, Hugging Face Transformers
```

---

## Example 220

**Intent:**
mi jefe quiere un modelo para predecir cuantos productos se devolveran

**Spec:**
```
Type:       Machine learning model (product return prediction)
Features:   - Build features from product category, size, price, discount and customer return history
            - Train a classifier to predict return probability per order line
            - Aggregate predictions into expected returns per week
            - Show products with the highest return risk
            - Report accuracy on last quarter's orders
Input:      Orders and returns history CSV
Tech stack: Python, pandas, CatBoost
```

---

## Example 221

**Intent:**
Evaluate our chatbot answers automatically against a set of test questions

**Spec:**
```
Type:       Command-line tool (LLM answer evaluation)
Features:   - Load a test set of questions with reference answers
            - Call the chatbot API for each question
            - Grade answers for correctness and groundedness with an LLM judge
            - Measure latency and refusal rate
            - Compare results with the previous run in an HTML report
Input:      YAML test set and the chatbot endpoint URL
Tech stack: Python, Claude API, pytest, Jinja2
```

---

## Example 222

**Intent:**
how polluted is our river: we did water samples at 20 points for 2 years

**Spec:**
```
Type:       Data analysis script (water quality monitoring)
Features:   - Load lab results for nitrate, phosphate, E. coli and dissolved oxygen
            - Compare values with environmental quality standards
            - Compute trends per sampling point
            - Map points coloured by compliance
            - Identify upstream-downstream changes along the river
Input:      Sample results CSV (site_id, date, parameter, value, unit) and site coordinates
Tech stack: R, tidyverse, sf, leaflet
```

---

## Example 223

**Intent:**
rate potholes severity too? no, i need an app where my road crew logs road signs and AI reads the sign type from a photo

**Spec:**
```
Type:       Mobile application with backend (road sign inventory)
Data model: Sign(id, sign_type, lat, lon, condition, photo_url, recorded_by, recorded_at)
Features:   - Take a photo of a road sign with GPS location
            - Classify the sign type with an on-device model
            - Let the crew correct the type and rate condition
            - Sync records when back online
            - Show all signs on a map for the office
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, TensorFlow Lite, Node.js, Express
```

---

## Example 224

**Intent:**
Compute school league tables from the published exam results

**Spec:**
```
Type:       Data analysis script (school ranking)
Features:   - Load published exam results per school
            - Compute average points score and pass rates
            - Rank schools within each region
            - Show rank changes from last year
            - Export a ranked table to Excel
Input:      CSV of results per school and year
Tech stack: Python, pandas, openpyxl
```

---

## Example 225

**Intent:**
sentiment of tweets about a football club before and after each match

**Spec:**
```
Type:       Data analysis script (fan sentiment around matches)
Features:   - Load posts mentioning the club with timestamps
            - Align posts with match kickoff times
            - Score sentiment of each post
            - Compare sentiment in the 24 hours before and after each match by result
            - Plot sentiment swings for the season
Input:      Posts CSV (text, created_at) and fixtures CSV (date, opponent, result)
Tech stack: Python, VADER, pandas, matplotlib
```

---

## Example 226

**Intent:**
a dashboard of my home solar panel production vs the weather forecast

**Spec:**
```
Type:       Data dashboard (solar production monitoring)
Features:   - Pull production data from the inverter API every 5 minutes
            - Fetch irradiance forecasts for my location
            - Show actual against expected production
            - Compute daily and monthly yield
            - Alert when production is far below expected on a sunny day
Storage:    InfluxDB
Tech stack: Python, SolarEdge API, Solcast API, Grafana
```

---

## Example 227

**Intent:**
I'm writing a novel and want an AI critique partner that comments on pacing and dialogue per chapter

**Spec:**
```
Type:       Desktop application (manuscript critique assistant)
Features:   - Import a manuscript from DOCX or Scrivener export
            - Split the manuscript into chapters
            - Comment on pacing, dialogue and point-of-view consistency per chapter
            - Track characters and flag inconsistent details
            - Save comments in a side panel linked to text passages
Input:      Manuscript file (.docx)
Tech stack: Python, PySide6, python-docx, Claude API
```

---

## Example 228

**Intent:**
vaccination coverage per district from health ministry data

**Spec:**
```
Type:       Data analysis script (immunisation coverage)
Features:   - Load doses administered and target population per district
            - Compute coverage for each vaccine and dose
            - Calculate dropout rate between first and third doses
            - Flag districts below 80 percent coverage
            - Map coverage by district
Input:      Health ministry Excel files and district shapefile
Tech stack: Python, pandas, GeoPandas, matplotlib
```

---

## Example 229

**Intent:**
count people walking into my shop from the security camera

**Spec:**
```
Type:       Machine learning model (store footfall counting)
Features:   - Detect people in the camera stream
            - Track people to count entries and exits through the door zone
            - Exclude staff wearing uniforms with a colour classifier
            - Store hourly counts
            - Compute conversion rate by joining with POS transactions
Storage:    SQLite
Tech stack: Python, YOLOv8, ByteTrack, OpenCV
```

---

## Example 230

**Intent:**
we want to estimate carbon footprint of our company from expenses data

**Spec:**
```
Type:       Data analysis script (spend-based carbon accounting)
Features:   - Load expense lines with category and amount
            - Map categories to spend-based emission factors
            - Calculate emissions per category and scope
            - Use activity data instead where available, such as fuel litres
            - Produce a summary report by scope and month
Input:      Expense export CSV and an emission factor table
Tech stack: Python, pandas, openpyxl
```

---

## Example 231

**Intent:**
Data pipeline: scrape public procurement tenders daily and classify by sector

**Spec:**
```
Type:       Data pipeline (public tender monitoring)
Data model: Tender(id, source, title, description, buyer, value, deadline, sector, url, published_at)
Features:   - Scrape new tenders from government procurement portals daily
            - Normalise buyer names and currency
            - Classify tenders into sectors using CPV codes and text
            - Match tenders to saved client interests
            - Email new matching tenders each morning
Storage:    PostgreSQL
Tech stack: Python, Scrapy, Apache Airflow, scikit-learn
```

---

## Example 232

**Intent:**
track my kids screen time from the router logs

**Spec:**
```
Type:       Data analysis script (household screen time)
Features:   - Load DNS query logs from the router
            - Map devices to each child by MAC address
            - Map domains to apps and categories
            - Estimate active minutes per app per day
            - Show a weekly report per child
Input:      DNS log export from Pi-hole and a device mapping file
Tech stack: Python, pandas, matplotlib
```

---

## Example 233

**Intent:**
An LLM agent that does our monthly expense report: reads receipts from email, fills the company expense form

**Spec:**
```
Type:       Bot (expense report agent)
Data model: Receipt(id, source_email_id, merchant, date, amount, currency, category, image_path)
            ExpenseReport(id, month, status, submitted_at)
Features:   - Search the mailbox for receipt emails and attachments
            - Extract merchant, date, amount and currency
            - Categorise expenses according to company policy
            - Fill the expense form in the finance system through its API
            - Ask the user to confirm before submitting
Storage:    SQLite
Tech stack: Python, Microsoft Graph API, Claude API (tool use), SAP Concur API
```

---

## Example 234

**Intent:**
detect weeds vs crops in images from a field robot

**Spec:**
```
Type:       Machine learning model (weed segmentation)
Features:   - Train a semantic segmentation model on labelled field images
            - Separate crop, weed and soil pixels
            - Output weed centroids in robot coordinates
            - Run in real time on the robot's onboard computer
            - Report intersection over union per class
Input:      RGB field images with pixel-level masks
Tech stack: Python, PyTorch, segmentation_models_pytorch, ONNX Runtime
```

---

## Example 235

**Intent:**
show which suppliers deliver late most often

**Spec:**
```
Type:       Data analysis script (supplier delivery performance)
Features:   - Load purchase orders with promised and actual delivery dates
            - Calculate on-time delivery rate per supplier
            - Compute average days late
            - Show trend per supplier by quarter
            - Rank suppliers and export a scorecard
Input:      ERP purchase order export (CSV)
Tech stack: Python, pandas, matplotlib
```

---

## Example 236

**Intent:**
build a REST api in Go that runs our ONNX image model

**Spec:**
```
Type:       REST API service (image model inference)
Features:   - Accept image uploads as multipart or base64
            - Resize and normalise images
            - Run inference with the ONNX model
            - Return top-5 labels with probabilities
            - Expose Prometheus metrics for latency and request count
Tech stack: Go, onnxruntime-go, Gin, Prometheus
```

---

## Example 237

**Intent:**
tell me if our teachers' grades are harder in some classes than others

**Spec:**
```
Type:       Data analysis script (grading consistency)
Features:   - Load coursework grades and standardised test scores for the same students
            - Compare each teacher's average grade with their students' test scores
            - Detect lenient or harsh grading with a mixed-effects model
            - Show the distribution of grades per teacher
            - Flag outliers for moderation
Input:      CSV with student_id, teacher, subject, coursework_grade, test_score
Tech stack: R, lme4, ggplot2
```

---

## Example 238

**Intent:**
generate quiz questions from a pdf textbook chapter

**Spec:**
```
Type:       Command-line tool (quiz question generation)
Features:   - Extract text from a PDF chapter
            - Generate multiple-choice and short-answer questions with a language model
            - Include the source page for each question
            - Avoid duplicate questions
            - Export to a Moodle XML quiz file
Input:      PDF textbook chapter and number of questions
Tech stack: Python, pdfplumber, Claude API, lxml
```

---

## Example 239

**Intent:**
Analyse which neighbourhoods in our city have the most noise complaints at night

**Spec:**
```
Type:       Data analysis script (noise complaint analysis)
Features:   - Load 311 service requests and filter noise complaints
            - Assign complaints to neighbourhoods with a spatial join
            - Count night-time complaints per 1,000 residents
            - Break down by complaint type such as music, construction and traffic
            - Map rates and show monthly trends
Input:      311 requests CSV and neighbourhood boundaries GeoJSON
Tech stack: Python, GeoPandas, pandas, Folium
```

---

## Example 240

**Intent:**
i hav a big folder of scanned docs, make them searchable pdfs

**Spec:**
```
Type:       Command-line tool (OCR to searchable PDF)
Features:   - Find all scanned PDF and image files in a folder
            - Deskew and clean each page
            - Add an invisible OCR text layer
            - Detect the document language automatically
            - Write searchable PDFs to an output folder
Input:      Folder of scanned PDFs and images
Tech stack: Python, OCRmyPDF, Tesseract
```

---

## Example 241

**Intent:**
predict if a customer will pay their invoice late

**Spec:**
```
Type:       Machine learning model (late payment prediction)
Features:   - Build features from customer payment history, invoice amount and terms
            - Train a classifier on paid invoices
            - Predict the probability of payment more than 30 days late
            - Flag high-risk invoices for early reminders
            - Show model performance by customer segment
Input:      Accounts receivable history CSV
Tech stack: Python, pandas, scikit-learn, XGBoost
```

---

## Example 242

**Intent:**
Find duplicate questions on our community Q&A forum

**Spec:**
```
Type:       Machine learning model (duplicate question detection)
Features:   - Embed each question title and body
            - Retrieve nearest neighbours for new questions
            - Score candidate pairs with a cross-encoder
            - Suggest possible duplicates while the user is typing
            - Let moderators merge confirmed duplicates
Storage:    PostgreSQL with pgvector
Tech stack: Python, sentence-transformers, FastAPI
```

---

## Example 243

**Intent:**
analyze how fast our ambulances get to emergencies across the county

**Spec:**
```
Type:       Data analysis script (ambulance response times)
Features:   - Load dispatch records with call, dispatch and arrival times
            - Compute response time percentiles per area and priority
            - Map incidents that exceeded the target time
            - Compare response times by time of day
            - Model coverage from current stations with drive-time isochrones
Input:      Dispatch CSV (call_id, priority, lat, lon, call_time, arrival_time) and station locations
Tech stack: Python, GeoPandas, OpenRouteService API, Folium
```

---

## Example 244

**Intent:**
Slack bot that tells us every morning yesterday's sign-ups and revenue

**Spec:**
```
Type:       Bot (daily metrics digest)
Features:   - Query yesterday's sign-ups and revenue from the database
            - Compare with the same weekday last week
            - Format a short message with up and down arrows
            - Post it to a Slack channel at 9:00
            - Include a link to the full dashboard
Storage:    PostgreSQL (read-only)
Tech stack: Python, Slack SDK, SQLAlchemy, cron
```

---

## Example 245

**Intent:**
let my students ask questions about our course materials and get answers with page references

**Spec:**
```
Type:       Chatbot (course materials assistant)
Data model: Course(id, name)
            Material(id, course_id -> Course, title, file_path)
            Chunk(id, material_id -> Material, page, text, embedding)
Features:   - Index lecture slides, notes and readings per course
            - Answer student questions with citations to page numbers
            - Refuse to answer graded assignment questions directly
            - Show instructors common questions
            - Update the index when new materials are uploaded
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, LTI 1.3, Claude API
```

---

## Example 246

**Intent:**
a scale in our cafeteria that logs food waste per dish, then reports

**Spec:**
```
Type:       IoT system (food waste tracking)
Data model: Dish(id, name, category)
            WasteLog(id, dish_id -> Dish, weight_g, logged_at, meal_service)
Features:   - Weigh discarded food on a connected scale
            - Let staff tap the dish name on a tablet
            - Log weight per dish and meal service
            - Report weekly waste per dish and cost
            - Show the dishes with the most waste per serving
Storage:    PostgreSQL
Tech stack: Raspberry Pi, HX711 load cell, Python, Flask
```

---

## Example 247

**Intent:**
Want to scrape real estate listings and track how long houses stay on the market

**Spec:**
```
Type:       Scheduled script (property listing tracking)
Data model: Listing(id, portal_id, address, price, bedrooms, first_seen, last_seen, status)
            PriceChange(id, listing_id -> Listing, old_price, new_price, changed_at)
Features:   - Scrape listings from property portals daily
            - Detect new, changed and removed listings
            - Record price reductions
            - Compute days on market per area
            - Export weekly statistics to CSV
Storage:    SQLite
Tech stack: Python, Playwright, pandas
```

---

## Example 248

**Intent:**
Analyze my company's IT tickets to see what takes longest to fix

**Spec:**
```
Type:       Data analysis script (IT service desk analysis)
Features:   - Load tickets with category, priority and timestamps
            - Compute time to resolve per category and priority
            - Find categories that breach SLA most often
            - Show reopened tickets by category
            - Plot monthly volume and resolution time
Input:      ServiceNow export (CSV)
Tech stack: Python, pandas, Plotly
```

---

## Example 249

**Intent:**
I'd like to use my microphone to detect when my baby cries and send a notification to my phone

**Spec:**
```
Type:       IoT system (baby cry detection)
Features:   - Listen to the microphone continuously on a small device
            - Detect crying with a pretrained audio classifier
            - Ignore short noises under 5 seconds
            - Send a push notification to my phone
            - Log crying times to see sleep patterns
Storage:    SQLite
Tech stack: Raspberry Pi, Python, YAMNet (TensorFlow Lite), Pushover API
```

---

## Example 250

**Intent:**
how good is our weather forecast? compare predicted vs actual

**Spec:**
```
Type:       Data analysis script (forecast verification)
Features:   - Load archived forecasts and observed weather per day
            - Compute mean absolute error for temperature by lead time
            - Compute Brier score for rain probability
            - Plot reliability diagrams
            - Compare accuracy by season
Input:      Forecast archive CSV and observation CSV
Tech stack: Python, pandas, xskillscore, matplotlib
```

---

## Example 251

**Intent:**
Model that tags support emails with the product they are about

**Spec:**
```
Type:       Machine learning model (email product tagging)
Features:   - Extract product names and model numbers with named entity recognition
            - Train a classifier for emails without explicit product mentions
            - Combine both into a product prediction with confidence
            - Add the tag to the helpdesk ticket
            - Measure accuracy on a manually tagged sample
Tech stack: Python, spaCy, scikit-learn, Freshdesk API
```

---

## Example 252

**Intent:**
track how my plants grow with a timelapse camera and measure leaf area

**Spec:**
```
Type:       Data analysis script (plant growth phenotyping)
Features:   - Load timelapse images in order
            - Segment plant pixels from the background by colour
            - Calculate projected leaf area per image in square centimetres
            - Plot growth curves per plant
            - Create a timelapse video with the area overlaid
Input:      Folder of timestamped images and a calibration marker size
Tech stack: Python, OpenCV, PlantCV, matplotlib
```

---

## Example 253

**Intent:**
build something that tells shops nearby how many customers they'll get based on events in town

**Spec:**
```
Type:       Web application (event-driven footfall forecast)
Data model: Shop(id, name, lat, lon, category)
            Event(id, name, venue, lat, lon, starts_at, expected_attendance)
            FootfallForecast(id, shop_id -> Shop, date, expected_visitors)
Features:   - Import local events from public event APIs
            - Train a model linking past events to shop footfall
            - Forecast footfall per shop for the next 14 days
            - Explain which events drive each forecast
            - Send a weekly forecast email
Storage:    PostgreSQL
Tech stack: Python, Django, LightGBM, Ticketmaster API
```

---

## Example 254

**Intent:**
transcribe my voice memos and sort them into todo, ideas, journal

**Spec:**
```
Type:       Command-line script (voice memo sorting)
Features:   - Watch a folder for new voice memo files
            - Transcribe each memo
            - Classify the memo as todo, idea or journal with a language model
            - Append it to the matching Markdown file with the date
            - Move processed audio to an archive folder
Input:      Folder of voice memos (M4A)
Tech stack: Python, faster-whisper, Claude API, watchdog
```

---

## Example 255

**Intent:**
Weekly report: power consumption of our data center racks vs. temperature

**Spec:**
```
Type:       Scheduled script (data centre power report)
Features:   - Pull PDU power readings and inlet temperature sensor data
            - Compute weekly average and peak power per rack
            - Calculate power usage effectiveness
            - Flag racks near their power budget
            - Generate a PDF report and email it to facilities
Input:      PDU SNMP data and temperature sensor API
Tech stack: Python, pysnmp, pandas, WeasyPrint
```

---

## Example 256

**Intent:**
detect fake reviews on our marketplace

**Spec:**
```
Type:       Machine learning model (fake review detection)
Features:   - Build features from review text, reviewer history and timing bursts
            - Detect near-duplicate review text across accounts
            - Train a classifier on reviews removed by moderators
            - Score new reviews before publishing
            - Send high-scoring reviews to moderation
Tech stack: Python, scikit-learn, datasketch (MinHash), pandas
```

---

## Example 257

**Intent:**
analyse the vote records of our city council members, who votes together

**Spec:**
```
Type:       Data analysis script (council voting blocs)
Features:   - Load roll-call votes for each motion
            - Build a member-by-vote matrix
            - Compute agreement rates between every pair of members
            - Cluster members into voting blocs
            - Plot an agreement heatmap and a 2D map of members
Input:      CSV of votes (motion_id, date, member, vote)
Tech stack: Python, pandas, scikit-learn, seaborn
```

---

## Example 258

**Intent:**
build me a lightweight R shiny app to explore our lab's qPCR results

**Spec:**
```
Type:       Web application (qPCR results explorer)
Features:   - Upload qPCR export files
            - Calculate delta-delta Ct values against a reference gene
            - Show fold change per gene and condition
            - Flag wells with poor amplification
            - Download tables and plots
Input:      qPCR instrument export (CSV)
Tech stack: R, Shiny, tidyverse, ggplot2
```

---

## Example 259

**Intent:**
Forecast sales of umbrellas based on weather forecast lol

**Spec:**
```
Type:       Machine learning model (weather-driven demand forecasting)
Features:   - Join daily sales with historical rainfall and temperature
            - Train a regression model on weather and calendar features
            - Pull the 7-day weather forecast
            - Predict daily umbrella sales per store
            - Suggest store transfers before rainy days
Input:      Daily sales CSV and weather history
Tech stack: Python, pandas, scikit-learn, Open-Meteo API
```

---

## Example 260

**Intent:**
translate our app strings to 10 languages and check the translations fit the buttons

**Spec:**
```
Type:       Command-line tool (UI string localisation)
Features:   - Read source strings from the app's JSON or XLIFF files
            - Translate missing strings with a translation API
            - Keep placeholders such as {name} intact
            - Warn when a translation is much longer than the source
            - Write updated files per language
Input:      Localisation files directory
Tech stack: Node.js, TypeScript, DeepL API
```

---

## Example 261

**Intent:**
i need to know which hours our power grid substation is overloaded from SCADA exports

**Spec:**
```
Type:       Data analysis script (substation loading analysis)
Features:   - Load transformer loading data at 15-minute resolution
            - Compare loading with the transformer rating
            - Count overload hours per month
            - Find typical overload days by season
            - Plot load duration curves
Input:      SCADA CSV (timestamp, transformer_id, load_mva) and ratings sheet
Tech stack: Python, pandas, matplotlib
```

---

## Example 262

**Intent:**
An app for birdwatchers that records song and tells the species right on the phone without internet

**Spec:**
```
Type:       Mobile application (offline bird song identification)
Data model: Recording(id, file_path, lat, lon, recorded_at)
            Identification(id, recording_id -> Recording, species, confidence)
Features:   - Record bird song with the phone microphone
            - Identify species with an on-device audio model
            - Show top matches with photos and confidence
            - Save recordings with GPS location
            - Work fully offline
Storage:    Local SQLite
Tech stack: Swift (iOS), Core ML, AVFoundation
```

---

## Example 263

**Intent:**
Visualise all the bike-share trips in our city as flows between stations

**Spec:**
```
Type:       Data analysis script (bike-share flow analysis)
Features:   - Load trip records with start and end stations
            - Aggregate trips by station pair and hour
            - Find stations that run empty or full
            - Draw flow lines between stations on a map
            - Show a weekday versus weekend comparison
Input:      Bike-share trips CSV and station locations
Tech stack: Python, pandas, kepler.gl
```

---

## Example 264

**Intent:**
ai assistant for my small law office that drafts letters from templates and case notes

**Spec:**
```
Type:       Web application (legal letter drafting)
Data model: Case(id, client_name, matter_type, notes)
            Template(id, name, body)
            Letter(id, case_id -> Case, template_id -> Template, draft, status)
Features:   - Pick a template and a case
            - Fill in details from case notes with a language model
            - Highlight any facts the model inferred
            - Let the lawyer edit and approve the draft
            - Export the letter to DOCX on letterhead
Storage:    PostgreSQL
Tech stack: Python, Django, Claude API, python-docx
```

---

## Example 265

**Intent:**
late bus data -> parents app?

**Spec:**
```
Type:       Mobile application with backend (school bus arrival predictions)
Data model: Route(id, name)
            Stop(id, route_id -> Route, name, lat, lon)
            BusPosition(id, route_id -> Route, lat, lon, recorded_at)
Features:   - Receive GPS positions from school buses every 15 seconds
            - Predict arrival times at each stop from current speed and past trips
            - Let parents follow their child's stop
            - Notify parents when the bus is 5 minutes away
            - Report daily delays to the transport office
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI, Firebase Cloud Messaging
```

---

## Example 266

**Intent:**
teacher here. kids do online reading quizzes, i want to see who reads a lot but scores low, maybe they need help

**Spec:**
```
Type:       Data analysis script (reading quiz engagement vs performance)
Features:   - Load quiz results and books read per student
            - Compute average score and reading volume per student
            - Place students in a quadrant chart of volume against score
            - List students with high volume and low scores
            - Export the list with recent quiz titles
Input:      Reading platform export CSV (student, book, word_count, quiz_score, date)
Tech stack: Python, pandas, matplotlib
```

---

## Example 267

**Intent:**
analize the waiting times in my dental clinic, patients say they wait too long

**Spec:**
```
Type:       Data analysis script (clinic waiting time analysis)
Features:   - Load check-in, called-in and check-out times from the booking system
            - Compute waiting time per appointment
            - Compare waits by dentist, treatment type and hour
            - Find appointment types that overrun their slot
            - Suggest slot lengths per treatment type from median durations
Input:      Booking system export (CSV)
Tech stack: Python, pandas, seaborn
```

---

## Example 268

**Intent:**
estimate how full the city's recycling bins are from fill-level sensors and plan pickup routes

**Spec:**
```
Type:       IoT system (smart waste collection)
Data model: Bin(id, lat, lon, capacity_l, type)
            FillReading(id, bin_id -> Bin, fill_pct, recorded_at)
            CollectionRoute(id, date, truck_id, bin_ids)
Features:   - Receive ultrasonic fill-level readings over NB-IoT
            - Predict when each bin will be full
            - Select bins to empty tomorrow
            - Optimise collection routes for each truck
            - Show bins and routes on a map for dispatchers
Storage:    PostgreSQL with PostGIS
Tech stack: Python, FastAPI, Google OR-Tools, Leaflet
```

---

## Example 269

**Intent:**
ppl in my discord post memes, auto detect NSFW images and delete

**Spec:**
```
Type:       Bot (Discord image moderation)
Features:   - Check every image posted in the server
            - Classify images with an NSFW detection model
            - Delete flagged images and warn the user
            - Allow NSFW-marked channels to skip checks
            - Log removed images for moderators to appeal
Tech stack: Python, discord.py, NudeNet
```

---

## Example 270

**Intent:**
Please create something that reads daily COVID wastewater data and shows trends per sewage plant

**Spec:**
```
Type:       Data dashboard (wastewater surveillance)
Features:   - Download viral concentration data per treatment plant
            - Normalise concentrations by flow and population
            - Smooth with a 7-day rolling average
            - Show trends per plant with significant increases flagged
            - Map plants coloured by current trend
Input:      Public wastewater surveillance CSV
Tech stack: Python, pandas, Dash, Plotly
```

---

## Example 271

**Intent:**
speech recognition for kids' spelling tests, they say the word and spell it

**Spec:**
```
Type:       Web application (spoken spelling practice)
Data model: WordList(id, teacher_id, name, words)
            Attempt(id, student_id, word, spoken_letters, correct, created_at)
Features:   - Read a word aloud with text-to-speech
            - Let the child spell it letter by letter into the microphone
            - Recognise spoken letters
            - Mark the attempt and show the right spelling
            - Show teachers which words the class finds hardest
Storage:    PostgreSQL
Tech stack: TypeScript, React, Web Speech API, Node.js
```

---

## Example 272

**Intent:**
we run a summer camp, want to analyse parent feedback forms both ratings and comments

**Spec:**
```
Type:       Data analysis script (camp feedback analysis)
Features:   - Load feedback form responses
            - Summarise rating questions by session and age group
            - Classify comments as praise, complaint or suggestion
            - Extract the most mentioned activities
            - Create a summary PDF for the camp director
Input:      Google Forms response CSV
Tech stack: Python, pandas, Claude API, ReportLab
```

---

## Example 273

**Intent:**
what are the chances my flight is delayed based on past data

**Spec:**
```
Type:       Machine learning model (flight delay prediction)
Features:   - Load historical flight records with departure delays
            - Add weather at origin and destination
            - Train a classifier for delays over 15 minutes
            - Predict delay probability for a given flight number and date
            - Show the airline's on-time history for that route
Input:      Public flight on-time performance data
Tech stack: Python, pandas, LightGBM, Meteostat
```

---

## Example 274

**Intent:**
Build an Apache Spark job that computes daily store-level sales features for our ML team

**Spec:**
```
Type:       Data pipeline (feature engineering)
Features:   - Read transaction data from the data lake
            - Compute rolling 7, 28 and 90-day sales per store and product
            - Add holiday and promotion flags
            - Write features as partitioned Parquet
            - Register the feature table in the feature store
Storage:    Delta Lake
Tech stack: PySpark, Databricks, Feast
```

---

## Example 275

**Intent:**
Every month we got PDF bank statements from 4 banks, need them in one spreadsheet categorised

**Spec:**
```
Type:       Command-line script (bank statement parsing)
Features:   - Detect which bank each PDF statement comes from
            - Parse transaction tables with bank-specific rules
            - Normalise dates, amounts and descriptions
            - Categorise transactions with keyword rules
            - Write all transactions to one Excel sheet with a category summary
Input:      Folder of PDF bank statements
Tech stack: Python, pdfplumber, pandas, openpyxl
```

---

## Example 276

**Intent:**
Write an R script to find which genes are differentially expressed in my RNA-seq data

**Spec:**
```
Type:       Data analysis script (differential gene expression)
Features:   - Load the gene count matrix and sample metadata
            - Filter low-count genes
            - Run differential expression between conditions
            - Correct p-values for multiple testing
            - Draw a volcano plot and heatmap of top genes
Input:      Count matrix (CSV) and sample sheet
Tech stack: R, DESeq2, ggplot2, pheatmap
```

---

## Example 277

**Intent:**
an app that tells blind people what's in front of them using the phone camera

**Spec:**
```
Type:       Mobile application (scene description for visually impaired)
Features:   - Capture an image when the user taps anywhere on the screen
            - Describe the scene with a vision language model
            - Read the description aloud
            - Read printed text such as labels and signs
            - Let the user ask follow-up questions by voice
Tech stack: Swift (iOS), AVFoundation, Claude API (vision), VoiceOver support
```

---

## Example 278

**Intent:**
who are the most influential accounts talking about electric cars

**Spec:**
```
Type:       Data analysis script (social network influence analysis)
Features:   - Collect posts and reposts mentioning electric car keywords
            - Build a repost and mention network
            - Compute PageRank and betweenness per account
            - Detect communities in the network
            - List top accounts per community
Input:      Social media posts export (JSON)
Tech stack: Python, NetworkX, python-louvain, pandas
```

---

## Example 279

**Intent:**
detect empty shelves in supermarket from ceiling cameras

**Spec:**
```
Type:       Machine learning model (out-of-stock detection)
Data model: Camera(id, aisle, shelf_section)
            GapDetection(id, camera_id -> Camera, bbox, detected_at, resolved_at)
Features:   - Capture shelf images every 10 minutes
            - Detect gaps on the shelf with an object detector
            - Map gaps to products using the planogram
            - Alert staff with the aisle and product
            - Report out-of-stock duration per product
Storage:    PostgreSQL
Tech stack: Python, YOLOv8, OpenCV, FastAPI
```

---

## Example 280

**Intent:**
track how my employees feel with a weekly 3 question pulse survey and show trends

**Spec:**
```
Type:       Web application (employee pulse survey)
Data model: Survey(id, week, questions)
            Response(id, survey_id -> Survey, team, answers, submitted_at)
Features:   - Send a weekly 3-question survey by email and Teams
            - Keep answers anonymous and only show teams of 5 or more
            - Show trends per team and question
            - Summarise free-text comments by theme
            - Alert managers when scores drop sharply
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor, Azure OpenAI Service
```

---

## Example 281

**Intent:**
Can you help me use machine learning to sort my email into folders

**Spec:**
```
Type:       Machine learning model (email folder classification)
Features:   - Read emails and their current folders over IMAP
            - Train a text classifier on subject, sender and body
            - Predict a folder for new incoming emails
            - Move emails only when confidence is high
            - Learn from emails the user moves manually
Tech stack: Python, imaplib, scikit-learn
```

---

## Example 282

**Intent:**
Help me find patterns in our hospital's sepsis cases from the EHR data

**Spec:**
```
Type:       Data analysis script (sepsis cohort analysis)
Features:   - Identify sepsis cases from diagnosis codes and lab criteria
            - Compute time from arrival to antibiotics
            - Compare mortality by time-to-antibiotics band
            - Show vital sign trajectories before diagnosis
            - Summarise cases by ward and month
Input:      EHR extracts (admissions, vitals, labs, medications) as CSV
Tech stack: Python, pandas, matplotlib
```

---

## Example 283

**Intent:**
rate exam difficulty of each question from student answers (item analysis)

**Spec:**
```
Type:       Data analysis script (exam item analysis)
Features:   - Load student answers per question
            - Compute difficulty index and discrimination index per question
            - Analyse distractors for multiple-choice questions
            - Compute Cronbach's alpha for the exam
            - Flag questions to revise
Input:      Answer matrix CSV (student_id, q1..qn) and answer key
Tech stack: Python, pandas, NumPy
```

---

## Example 284

**Intent:**
Tiny flask api that returns sentiment for a sentence

**Spec:**
```
Type:       REST API service (sentiment analysis)
Features:   - Accept a sentence or list of sentences in JSON
            - Return a sentiment label and score
            - Load the model once at startup
            - Limit input length to 512 tokens
            - Return clear errors for bad input
Tech stack: Python, Flask, Hugging Face Transformers
```

---

## Example 285

**Intent:**
dashboard of hospital lab turnaround times per test type

**Spec:**
```
Type:       Data dashboard (lab turnaround time)
Features:   - Load order, receipt and result timestamps from the lab system
            - Compute turnaround time per test and priority
            - Show the percentage meeting targets
            - Show trends by hour and weekday
            - Drill down to delayed samples
Storage:    Microsoft SQL Server (lab system replica)
Tech stack: Python, Streamlit, pandas
```

---

## Example 286

**Intent:**
ich möchte die Pünktlichkeit unserer Lieferfahrer analysieren mit GPS Daten

**Spec:**
```
Type:       Data analysis script (delivery punctuality analysis)
Features:   - Load GPS tracks and planned delivery windows
            - Detect arrival time at each delivery address
            - Compute on-time rate per driver and route
            - Find stops with long dwell times
            - Map late deliveries
Input:      GPS export (driver_id, lat, lon, timestamp) and delivery plan CSV
Tech stack: Python, pandas, GeoPandas, Folium
```

---

## Example 287

**Intent:**
Generate meeting minutes in my company's template from Zoom recordings

**Spec:**
```
Type:       Data pipeline (meeting minutes generation)
Features:   - Download new cloud recordings through the Zoom API
            - Transcribe with speaker names from the Zoom transcript
            - Fill the company minutes template: attendees, decisions, actions
            - Save minutes as DOCX in SharePoint
            - Notify the organiser to review
Tech stack: Python, Zoom API, Claude API, python-docx, Microsoft Graph API
```

---

## Example 288

**Intent:**
predict sea ice / no wait, predict snow depth at our ski resort for the next week

**Spec:**
```
Type:       Machine learning model (snow depth forecasting)
Features:   - Load historical snow depth readings and weather
            - Add forecast snowfall, temperature and wind
            - Train a model for daily snow depth change
            - Forecast snow depth for the next 7 days per slope sensor
            - Show forecasts to slope managers
Input:      Snow sensor CSV and weather forecast API
Tech stack: Python, pandas, scikit-learn, Open-Meteo API
```

---

## Example 289

**Intent:**
Explore why some of my Kickstarter-style campaigns succeed: data from 5000 campaigns

**Spec:**
```
Type:       Data analysis script (crowdfunding success analysis)
Features:   - Load campaign data with goal, duration, category and outcome
            - Compute success rates by category and goal size
            - Analyse title and description length effects
            - Fit a logistic regression for success
            - Plot the key factors
Input:      CSV of campaigns (goal, pledged, backers, category, launched_at, deadline, state)
Tech stack: Python, pandas, statsmodels, seaborn
```

---

## Example 290

**Intent:**
An AI that reviews SQL queries in our dbt repo for performance problems

**Spec:**
```
Type:       Bot (SQL review assistant)
Features:   - Run on every pull request that changes dbt models
            - Parse SQL and detect patterns like SELECT *, cross joins and missing filters on partitions
            - Ask a language model to explain issues and suggest fixes
            - Post a review comment on the pull request
            - Pass or fail the CI check based on severity
Tech stack: Python, sqlglot, GitHub Actions, Claude API
```

---

## Example 291

**Intent:**
a mobile app that scans business cards and saves them to my contacts

**Spec:**
```
Type:       Mobile application (business card scanner)
Features:   - Take a photo of a business card
            - Run on-device OCR
            - Parse name, company, title, phone and email
            - Let the user correct fields
            - Save as a phone contact and export vCard
Tech stack: Kotlin (Android), ML Kit Text Recognition
```

---

## Example 292

**Intent:**
analyse our drug trial adverse events by treatment arm

**Spec:**
```
Type:       Data analysis script (adverse event analysis)
Features:   - Load adverse event and subject data
            - Code events by MedDRA system organ class
            - Count subjects with events per arm
            - Compute risk differences with confidence intervals
            - Produce safety tables in RTF
Input:      ADaM datasets ADSL and ADAE (SAS XPT)
Tech stack: R, haven, gtsummary, rtables
```

---

## Example 293

**Intent:**
AI tutor for learning to play chess by explaining my mistakes

**Spec:**
```
Type:       Web application (chess game review tutor)
Data model: User(id, email, rating)
            Game(id, user_id -> User, pgn, played_at)
            Mistake(id, game_id -> Game, move_number, played_move, best_move, explanation)
Features:   - Import games by PGN or from online chess platforms
            - Analyse each move with a chess engine
            - Find blunders and mistakes by evaluation drop
            - Explain each mistake in plain language with a language model
            - Build practice puzzles from the user's own mistakes
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Stockfish, python-chess, Claude API
```

---

## Example 294

**Intent:**
model to estimate the age of a fish from a photo of its scale

**Spec:**
```
Type:       Machine learning model (fish age estimation)
Features:   - Load images of fish scales labelled with expert age readings
            - Fine-tune a CNN regression model
            - Report mean absolute error in years
            - Show a saliency map of growth rings used
            - Flag predictions with high uncertainty for expert reading
Input:      Scale images and age labels CSV
Tech stack: Python, PyTorch, timm, Captum
```

---

## Example 295

**Intent:**
we have a csv with hours studied and grades for 200 students, is there a correlation

**Spec:**
```
Type:       Data analysis script (study time correlation)
Features:   - Load the CSV
            - Remove invalid or missing values
            - Compute Pearson and Spearman correlation
            - Plot a scatter plot with a regression line
            - Print a plain-language interpretation
Input:      CSV with student_id, hours_studied, grade
Tech stack: Python, pandas, SciPy, seaborn
```

---

## Example 296

**Intent:**
tool for scientists to extract tables from published PDFs into CSV

**Spec:**
```
Type:       Command-line tool (PDF table extraction)
Features:   - Detect tables on each page of a PDF
            - Extract cells keeping merged headers
            - Handle tables that continue across pages
            - Save each table as a separate CSV
            - Write a log of pages with tables that could not be parsed
Input:      PDF file or folder of PDFs
Tech stack: Python, camelot, pdfplumber, pandas
```

---

## Example 297

**Intent:**
Make an Alexa-like voice assistant for our warehouse workers to ask stock levels hands free

**Spec:**
```
Type:       Mobile application with backend (voice stock lookup)
Features:   - Listen for a push-to-talk button on the headset
            - Recognise product names and SKU numbers
            - Look up stock level and location in the WMS
            - Speak the answer back
            - Log queries for unknown products
Tech stack: Kotlin (Android), Vosk, Python, FastAPI
```

---

## Example 298

**Intent:**
compare housing affordability across cities using public income and rent data

**Spec:**
```
Type:       Data analysis script (housing affordability)
Features:   - Download median rent and median household income per city
            - Compute rent-to-income ratios
            - Rank cities by affordability
            - Show ten-year changes
            - Draw a scatter of rent growth against income growth
Input:      Public statistics CSV files
Tech stack: Python, pandas, Plotly
```

---

## Example 299

**Intent:**
automatically extract key dates and parties from lease agreements

**Spec:**
```
Type:       Data pipeline (lease abstraction)
Data model: Lease(id, file_path, tenant, landlord, start_date, end_date, rent, renewal_notice_date, break_clause)
Features:   - Read lease PDFs including scanned ones
            - Extract parties, dates, rent and break clauses with a language model
            - Show the source text for every extracted field
            - Let a paralegal confirm the fields
            - Create calendar reminders for notice dates
Storage:    PostgreSQL
Tech stack: Python, OCRmyPDF, Claude API, Django
```

---

## Example 300

**Intent:**
what are the most common words in Shakespeare plays per character

**Spec:**
```
Type:       Data analysis script (text analysis of plays)
Features:   - Load play texts in TEI XML
            - Split lines by speaking character
            - Remove stopwords and lemmatise
            - Compute TF-IDF distinctive words per character
            - Plot word clouds for the main characters
Input:      TEI XML files of the plays
Tech stack: Python, lxml, spaCy, scikit-learn, wordcloud
```

---

## Example 301

**Intent:**
Hi I have a fishing boat and want to log my catches and see where fish are best

**Spec:**
```
Type:       Mobile application (fishing catch log)
Data model: Trip(id, date, boat)
            Catch(id, trip_id -> Trip, species, weight_kg, lat, lon, depth_m, water_temp_c, caught_at)
Features:   - Log catches with GPS position and species
            - Record water temperature and depth
            - Show a heatmap of catches per species
            - Show best months and times per species
            - Work offline at sea and sync later
Storage:    Local SQLite with cloud sync
Tech stack: Flutter, sqflite, Supabase
```

---

## Example 302

**Intent:**
data pipeline to sync our school's student info system to google classroom

**Spec:**
```
Type:       Data pipeline (roster synchronisation)
Features:   - Read classes, teachers and enrolments from the student information system API
            - Create or update courses in Google Classroom
            - Add and remove students to match enrolments
            - Skip archived classes
            - Log every change and email errors to IT
Tech stack: Python, Google Classroom API, Apache Airflow
```

---

## Example 303

**Intent:**
realtime gunshot detection from microphones in the park

**Spec:**
```
Type:       IoT system (acoustic gunshot detection)
Data model: Sensor(id, lat, lon)
            AcousticEvent(id, sensor_id -> Sensor, event_type, confidence, detected_at)
Features:   - Detect impulsive sounds on each sensor
            - Classify gunshots against fireworks and car backfires
            - Triangulate the location from arrival time differences
            - Alert the dispatch centre with a map position
            - Keep audio clips only for confirmed events
Storage:    PostgreSQL with PostGIS
Tech stack: Raspberry Pi, Python, TensorFlow Lite, MQTT, GPS time sync
```

---

## Example 304

**Intent:**
something that rates how well people pronounce english words

**Spec:**
```
Type:       Web application (pronunciation scoring)
Features:   - Show a word or sentence to read aloud
            - Record the user's voice
            - Align audio with expected phonemes
            - Score each phoneme and show the weak sounds
            - Play a native reference recording
Tech stack: Python, FastAPI, Montreal Forced Aligner, wav2vec 2.0, React
```

---

## Example 305

**Intent:**
use Excel only, no programming: track student test scores and show charts per class

**Spec:**
```
Type:       Data analysis script (spreadsheet grade tracker)
Features:   - Enter scores in a structured Excel table per class
            - Calculate averages and grade bands with formulas
            - Use conditional formatting to highlight low scores
            - Show charts per class with a pivot chart
            - Filter by subject with slicers
Input:      Excel workbook with one table per class
Tech stack: Microsoft Excel (tables, PivotTables, slicers)
```

---

## Example 306

**Intent:**
crop yield from satellite NDVI images for our cooperative's fields

**Spec:**
```
Type:       Data pipeline (satellite crop monitoring)
Features:   - Download Sentinel-2 images for field boundaries every 5 days
            - Mask clouds and compute NDVI per field
            - Build NDVI time series per field
            - Predict end-of-season yield from NDVI features
            - Show fields with low vegetation on a map
Input:      Field boundary shapefile
Tech stack: Python, Sentinel Hub API, rasterio, scikit-learn
```

---

## Example 307

**Intent:**
ocr of medicine boxes to check expiry dates in our pharmacy stockroom

**Spec:**
```
Type:       Mobile application (medicine expiry scanner)
Data model: Product(id, name, gtin)
            StockItem(id, product_id -> Product, batch, expiry_date, location, scanned_at)
Features:   - Scan the DataMatrix code to read GTIN, batch and expiry
            - Fall back to OCR on the printed expiry date
            - Save items with shelf location
            - List items expiring in the next 90 days
            - Export the list for returns
Storage:    Local SQLite
Tech stack: Kotlin (Android), ML Kit Barcode Scanning, ML Kit Text Recognition
```

---

## Example 308

**Intent:**
something to tell me what my competitors are writing about on their blogs every week

**Spec:**
```
Type:       Scheduled script (competitor content monitoring)
Features:   - Check competitor blog RSS feeds and sitemaps weekly
            - Fetch new articles
            - Summarise each article in two sentences
            - Group articles by topic
            - Email a weekly digest with links
Storage:    SQLite
Tech stack: Python, feedparser, trafilatura, Claude API
```

---

## Example 309

**Intent:**
train a model on my handwriting to make a font? no, to recognize my handwritten notes

**Spec:**
```
Type:       Machine learning model (personal handwriting recognition)
Features:   - Segment note pages into text lines
            - Fine-tune a handwriting recognition model on my transcribed lines
            - Transcribe new pages into text
            - Measure character error rate on held-out pages
            - Export notes as Markdown
Input:      Scanned note pages and a set of manually transcribed lines
Tech stack: Python, TrOCR (Hugging Face Transformers), OpenCV
```

---

## Example 310

**Intent:**
Analyse hotel occupancy and room prices to recommend price per night

**Spec:**
```
Type:       Machine learning model (hotel dynamic pricing)
Features:   - Load bookings with booking date, stay date and price
            - Model demand by days before arrival, season and events
            - Estimate price elasticity per room type
            - Recommend nightly prices for the next 90 days
            - Compare recommendations with competitor rates
Input:      PMS booking export and competitor rate data
Tech stack: Python, pandas, scikit-learn, SciPy (optimisation)
```

---

## Example 311

**Intent:**
count laps in a swimming pool from an underwater camera

**Spec:**
```
Type:       Machine learning model (swim lap counting)
Features:   - Detect swimmers per lane
            - Track swimmers across frames
            - Count turns at the pool wall
            - Estimate stroke rate from arm movement
            - Show lap counts on a poolside screen
Tech stack: Python, YOLOv8, OpenCV, MediaPipe
```

---

## Example 312

**Intent:**
we want to see where our volunteers live compared to where our events are

**Spec:**
```
Type:       Data analysis script (volunteer geography)
Features:   - Geocode volunteer postcodes
            - Load event locations
            - Compute distance from each volunteer to each event
            - Map volunteers and events
            - Find events with few volunteers within 10 km
Input:      Volunteer CSV with postcodes and event CSV with addresses
Tech stack: Python, geopy, GeoPandas, Folium
```

---

## Example 313

**Intent:**
agent that monitors our cloud bill and explains why it went up

**Spec:**
```
Type:       Scheduled script (cloud cost anomaly explanation)
Features:   - Pull daily cost data per service and tag
            - Detect days with unusual cost increases
            - Break increases down by service, region and resource
            - Write a short explanation with a language model
            - Post the explanation to Slack
Tech stack: Python, AWS Cost Explorer API, Claude API, Slack SDK
```

---

## Example 314

**Intent:**
gpa calculator for whole school from report cards

**Spec:**
```
Type:       Command-line script (GPA calculation)
Features:   - Load course grades and credit hours per student
            - Convert letter grades to grade points
            - Compute term and cumulative GPA
            - Rank students within each year group
            - Export GPA lists to Excel
Input:      Grades CSV (student_id, term, course, credits, letter_grade)
Tech stack: Python, pandas, openpyxl
```

---

## Example 315

**Intent:**
my hospital wants to predict which patients come back within 30 days after discharge

**Spec:**
```
Type:       Machine learning model (30-day readmission prediction)
Features:   - Build features from diagnoses, prior admissions, length of stay and medications
            - Train a gradient boosting classifier
            - Calibrate risk scores
            - Show the top risk factors per patient
            - Send a high-risk list to discharge nurses daily
Input:      Admission and discharge records from the EHR
Tech stack: Python, pandas, LightGBM, SHAP
```

---

## Example 316

**Intent:**
count how many times each word appears in a big text file

**Spec:**
```
Type:       Command-line script (word frequency count)
Features:   - Read a text file of any size line by line
            - Lowercase and strip punctuation
            - Count word frequencies
            - Print the top N words
            - Optionally save all counts to CSV
Input:      Path to a text file and N
Tech stack: Python (collections.Counter, argparse)
```

---

## Example 317

**Intent:**
so i coach a cross country team and record splits on my watch, i want to see who paces well and who goes out too fast

**Spec:**
```
Type:       Data analysis script (race pacing analysis)
Features:   - Load split times per runner and race
            - Compute pace per kilometre
            - Measure positive and negative splits
            - Rank runners by pacing consistency
            - Plot pace profiles per runner
Input:      CSV with runner, race, km, split_time
Tech stack: Python, pandas, matplotlib
```

---

## Example 318

**Intent:**
analyse traffic sensor counts on highway, find congestion hours

**Spec:**
```
Type:       Data analysis script (highway congestion analysis)
Features:   - Load loop detector counts and speeds per 5 minutes
            - Flag congestion when speed drops below 50 km/h
            - Compute congestion hours per segment and weekday
            - Draw speed heatmaps by time and location
            - Compare this year with last year
Input:      Detector CSV (detector_id, timestamp, volume, speed)
Tech stack: Python, pandas, seaborn
```

---

## Example 319

**Intent:**
website that lets citizens explore city budget data

**Spec:**
```
Type:       Web application (open budget explorer)
Data model: BudgetLine(id, year, department, program, category, amount)
Features:   - Show spending by department as an interactive treemap
            - Compare years side by side
            - Search for programs by keyword
            - Show per-resident spending
            - Download data as CSV
Storage:    PostgreSQL
Tech stack: TypeScript, SvelteKit, D3.js, Node.js
```

---

## Example 320

**Intent:**
ML to spot counterfeit products from photos

**Spec:**
```
Type:       Machine learning model (counterfeit product detection)
Features:   - Collect images of genuine and counterfeit products
            - Train a classifier focused on logo, stitching and label details
            - Compare close-up patches with reference images using a Siamese network
            - Return authenticity score with highlighted areas
            - Route uncertain cases to an expert
Input:      Labelled product images
Tech stack: Python, PyTorch, timm, FastAPI
```

---

## Example 321

**Intent:**
smth that listens to my guitar and tells me if im in tune and what chords i play

**Spec:**
```
Type:       Mobile application (guitar tuner and chord recognition)
Features:   - Capture audio from the microphone
            - Detect pitch and show tuning offset in cents
            - Recognise chords from chroma features
            - Show a timeline of chords played
            - Work offline
Tech stack: Flutter, Dart FFI, Essentia (C++)
```

---

## Example 322

**Intent:**
Analyze my small hotel's booking sources, which ones cost more in commission

**Spec:**
```
Type:       Data analysis script (booking channel cost analysis)
Features:   - Load reservations with source and price
            - Apply commission rates per channel
            - Compute net revenue per channel
            - Compare cancellation rates by channel
            - Chart share of bookings and net revenue per channel
Input:      Reservation export CSV and a commission rates table
Tech stack: Python, pandas, matplotlib
```

---

## Example 323

**Intent:**
An AI helper inside Google Sheets that cleans messy addresses and names

**Spec:**
```
Type:       Plugin (Google Sheets data cleaning add-on)
Features:   - Add a sidebar menu in Google Sheets
            - Normalise names, capitalisation and whitespace
            - Standardise addresses using a geocoding API
            - Detect duplicates and highlight them
            - Show a preview before writing changes
Tech stack: Google Apps Script, Google Maps Geocoding API
```

---

## Example 324

**Intent:**
anomaly alerts for patient vital signs in ICU

**Spec:**
```
Type:       Machine learning model (ICU deterioration early warning)
Features:   - Stream heart rate, blood pressure, SpO2 and respiratory rate
            - Compute an early warning score every minute
            - Detect abnormal trends with a recurrent model
            - Alert nurses when risk passes a threshold
            - Suppress repeated alerts within 15 minutes
Input:      Bedside monitor data stream (HL7)
Tech stack: Python, PyTorch, Apache Kafka
```

---

## Example 325

**Intent:**
Shows which wifi access points in our campus are overloaded

**Spec:**
```
Type:       Data dashboard (campus WiFi load)
Features:   - Pull client counts and bandwidth per access point from the controller
            - Show a floor map coloured by load
            - Show peak hours per building
            - Flag access points with high retry rates
            - Recommend where to add access points
Tech stack: Python, UniFi Controller API, Grafana, InfluxDB
```

---

## Example 326

**Intent:**
i do research on bees and have hundreds of hours of hive entrance video, need to count bees going in and out

**Spec:**
```
Type:       Machine learning model (bee traffic counting)
Features:   - Detect bees at the hive entrance in each frame
            - Track bees and decide direction in or out
            - Count bee traffic per minute
            - Detect pollen loads on returning bees
            - Export counts with timestamps to CSV
Input:      Hive entrance videos (MP4)
Tech stack: Python, YOLOv8, SORT tracker, OpenCV
```

---

## Example 327

**Intent:**
Pipeline: export Shopify orders to BigQuery every hour

**Spec:**
```
Type:       Data pipeline (e-commerce order sync)
Features:   - Fetch new and updated orders through the Shopify Admin API
            - Flatten line items, discounts and refunds
            - Upsert records into BigQuery tables
            - Track the last sync time
            - Alert on API rate limit errors
Storage:    Google BigQuery
Tech stack: Python, Google Cloud Functions, Cloud Scheduler, Shopify Admin API
```

---

## Example 328

**Intent:**
help my students practice debate with an AI opponent

**Spec:**
```
Type:       Web application (debate practice partner)
Data model: Motion(id, text, difficulty)
            Debate(id, student_id, motion_id -> Motion, side, transcript, score)
Features:   - Pick a motion and side
            - Argue against the student with a language model in timed rounds
            - Rebut the student's arguments with evidence-based counterpoints
            - Score the student on argument, rebuttal and clarity
            - Give feedback after the debate
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Claude API
```

---

## Example 329

**Intent:**
analyse our electric vehicle charging station usage

**Spec:**
```
Type:       Data analysis script (EV charging analysis)
Features:   - Load charging sessions with start, end and energy
            - Compute utilisation per charger
            - Measure idle time after charging finishes
            - Show peak demand per hour
            - Estimate revenue per charger
Input:      Charging sessions CSV (charger_id, start, end, kwh, fee)
Tech stack: Python, pandas, matplotlib
```

---

## Example 330

**Intent:**
guess the language of each text in a spreadsheet column

**Spec:**
```
Type:       Command-line script (language detection)
Features:   - Load a spreadsheet and the chosen text column
            - Detect the language of each cell
            - Add language code and confidence columns
            - Mark short texts as uncertain
            - Save the updated spreadsheet
Input:      Excel or CSV file and column name
Tech stack: Python, pandas, fastText (lid.176)
```

---

## Example 331

**Intent:**
Please create a model that predicts the energy rating of buildings from their basic data

**Spec:**
```
Type:       Machine learning model (building energy rating prediction)
Features:   - Load building records with age, floor area, type, heating system and insulation
            - Encode categorical features
            - Train a multiclass classifier for energy rating A to G
            - Evaluate with balanced accuracy
            - Explain which features improve the rating most
Input:      Energy certificate dataset CSV
Tech stack: Python, pandas, CatBoost, SHAP
```

---

## Example 332

**Intent:**
we got sales calls recorded in spanish, need them in english text

**Spec:**
```
Type:       Data pipeline (call transcription and translation)
Features:   - Pick up new recordings from cloud storage
            - Transcribe Spanish audio with timestamps
            - Translate transcripts to English
            - Store both versions linked to the call record
            - Make transcripts searchable
Storage:    PostgreSQL
Tech stack: Python, AWS Transcribe, AWS Translate, Amazon S3
```

---

## Example 333

**Intent:**
simple dashboard: lemonade stand sales each day (school project)

**Spec:**
```
Type:       Data dashboard (lemonade stand sales)
Features:   - Enter cups sold and price each day in a form
            - Show total money earned
            - Show a bar chart of cups per day
            - Show the best selling day
            - Save data in the browser
Storage:    Browser localStorage
Tech stack: HTML, CSS, JavaScript, Chart.js
```

---

## Example 334

**Intent:**
clean up a column of free text job titles into standard categories

**Spec:**
```
Type:       Data analysis script (job title normalisation)
Features:   - Load job titles from a CSV
            - Clean abbreviations and typos
            - Match titles to a standard occupation list with embeddings
            - Return the best match with a similarity score
            - Export unmatched titles for manual coding
Input:      CSV with a job_title column and a standard occupation list
Tech stack: Python, pandas, sentence-transformers
```

---

## Example 335

**Intent:**
a site where farmers upload soil test results and get fertiliser recommendations

**Spec:**
```
Type:       Web application (fertiliser recommendation)
Data model: Farm(id, owner_id, name, region)
            SoilTest(id, farm_id -> Farm, ph, nitrogen, phosphorus, potassium, organic_matter, tested_at)
            Recommendation(id, soil_test_id -> SoilTest, crop, product, rate_kg_ha)
Features:   - Enter or upload soil test results
            - Choose the planned crop
            - Calculate nutrient needs from agronomic tables
            - Recommend fertiliser products and amounts
            - Show history of tests per field
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 336

**Intent:**
Find out if our customer satisfaction scores depend on which agent answered

**Spec:**
```
Type:       Data analysis script (agent CSAT analysis)
Features:   - Load survey scores linked to tickets and agents
            - Compute average CSAT per agent with confidence intervals
            - Control for ticket category and channel
            - Find agents significantly above or below average
            - Chart results
Input:      CSAT export CSV (ticket_id, agent, category, channel, score)
Tech stack: Python, pandas, statsmodels, seaborn
```

---

## Example 337

**Intent:**
build a recommender for which online course a learner should take next

**Spec:**
```
Type:       Machine learning model (course recommendation)
Features:   - Build a learner-course interaction matrix from completions and ratings
            - Train a matrix factorisation model
            - Add course prerequisites and skill tags
            - Recommend the next 5 courses per learner
            - Evaluate with precision at 5 on held-out completions
Input:      Learner activity CSV and course catalogue
Tech stack: Python, implicit, pandas
```

---

## Example 338

**Intent:**
the plant we work at has thousands of maintenance work orders written in free text, find recurring problems

**Spec:**
```
Type:       Data analysis script (maintenance text mining)
Features:   - Load work order descriptions with equipment IDs
            - Clean jargon and abbreviations with a custom dictionary
            - Cluster descriptions into failure modes
            - Count failure modes per equipment type
            - List equipment with the most repeat failures
Input:      CMMS work order export (CSV)
Tech stack: Python, spaCy, scikit-learn, pandas
```

---

## Example 339

**Intent:**
make a chatbot that helps people check if they qualify for food assistance

**Spec:**
```
Type:       Chatbot (benefits eligibility screener)
Features:   - Ask about household size, income and expenses step by step
            - Apply the official eligibility rules to estimate qualification
            - Explain the result and which documents are needed
            - Show the nearest office and how to apply
            - Never store personal answers after the session ends
Tech stack: TypeScript, Node.js, Claude API, React
```

---

## Example 340

**Intent:**
monitor my aquarium water temp and ph

**Spec:**
```
Type:       IoT system (aquarium monitoring)
Features:   - Read temperature and pH probes every 5 minutes
            - Show current values on a small OLED display
            - Send readings to a cloud dashboard
            - Alert by phone when values leave the safe range
            - Turn the heater relay on or off automatically
Storage:    Adafruit IO
Tech stack: ESP32, Arduino, Adafruit IO, IFTTT
```

---

## Example 341

**Intent:**
show the most common reasons for 911 calls by hour

**Spec:**
```
Type:       Data analysis script (emergency call analysis)
Features:   - Load call records with incident type and time
            - Group incident types into categories
            - Count calls per category and hour of day
            - Show a heatmap of categories by hour
            - Compare weekends and weekdays
Input:      CAD call export CSV (call_id, received_at, incident_type)
Tech stack: Python, pandas, seaborn
```

---

## Example 342

**Intent:**
AI that reads lab notebooks pictures and makes them searchable

**Spec:**
```
Type:       Web application (lab notebook digitisation)
Data model: Notebook(id, owner_id, title)
            NotebookPage(id, notebook_id -> Notebook, image_url, transcription, page_date)
Features:   - Upload photos of notebook pages
            - Transcribe handwriting, tables and sketches with a vision model
            - Extract dates and sample IDs
            - Search across all pages
            - Export pages as PDF with text layer
Storage:    PostgreSQL, S3
Tech stack: Python, FastAPI, Claude API (vision), React
```

---

## Example 343

**Intent:**
Python script: track my weight from smart scale export and predict when I hit my goal

**Spec:**
```
Type:       Data analysis script (weight trend projection)
Features:   - Load weight measurements from the scale export
            - Smooth daily noise with an exponential moving average
            - Estimate weekly rate of change
            - Project the date to reach the goal weight
            - Plot weight, trend and projection
Input:      Smart scale CSV (date, weight_kg)
Tech stack: Python, pandas, matplotlib
```

---

## Example 344

**Intent:**
Our NGO collects survey data on tablets in villages with no internet, then syncs. Need analysis dashboards after.

**Spec:**
```
Type:       Data pipeline (offline field survey collection)
Features:   - Collect survey forms offline on tablets
            - Sync submissions when a connection is available
            - Validate and clean submissions in a central database
            - Compute indicators per village and survey round
            - Show indicators on a dashboard
Storage:    PostgreSQL
Tech stack: KoboToolbox, Python, pandas, Metabase
```

---

## Example 345

**Intent:**
model predicting price of used cars for our dealership

**Spec:**
```
Type:       Machine learning model (used car pricing)
Features:   - Clean listings: mileage, age, make, model, trim and condition
            - Encode make and model with target encoding
            - Train a gradient boosting regressor
            - Report error by price band
            - Provide a pricing form for salespeople
Tech stack: Python, pandas, LightGBM, Streamlit
```

---

## Example 346

**Intent:**
summarize long legal court judgments into one page

**Spec:**
```
Type:       Command-line tool (court judgment summarisation)
Features:   - Read judgments from PDF or HTML
            - Split long documents into sections
            - Summarise facts, issues, holding and reasoning
            - Keep paragraph references for each point
            - Save the summary as Markdown
Input:      Judgment file (PDF or HTML)
Tech stack: Python, pdfplumber, Claude API
```

---

## Example 347

**Intent:**
are the kids in our after school program improving their maths? we test them 3 times a year

**Spec:**
```
Type:       Data analysis script (program progress evaluation)
Features:   - Load test scores from three assessment points
            - Compute score gains per student
            - Compare gains by attendance level
            - Test whether gains are significant with a paired t-test
            - Produce charts for the funder report
Input:      CSV with student_id, attendance_days, test1, test2, test3
Tech stack: Python, pandas, SciPy, matplotlib
```

---

## Example 348

**Intent:**
detect potholes? no, detect cracks in concrete bridges from drone photos

**Spec:**
```
Type:       Machine learning model (concrete crack detection)
Features:   - Tile high-resolution drone images
            - Segment cracks with a U-Net model
            - Measure crack length and width in millimetres using ground sampling distance
            - Map cracks to bridge components
            - Export an inspection report with images
Input:      Drone images with flight metadata
Tech stack: Python, PyTorch, OpenCV, ReportLab
```

---

## Example 349

**Intent:**
a scheduled job that downloads weather forecasts and warns our farm workers about heat stress

**Spec:**
```
Type:       Scheduled script (heat stress warnings)
Features:   - Download hourly temperature and humidity forecasts every morning
            - Compute the heat index per hour
            - Find hours above caution and danger levels
            - Send SMS warnings with recommended break schedules
            - Log warnings sent per day
Tech stack: Python, Open-Meteo API, Twilio, cron
```

---

## Example 350

**Intent:**
tool to label images quickly for our ML dataset

**Spec:**
```
Type:       Web application (image annotation tool)
Data model: Project(id, name, label_set)
            Image(id, project_id -> Project, path, status)
            Annotation(id, image_id -> Image, annotator_id, label, bbox)
Features:   - Upload images to a project
            - Draw bounding boxes and choose labels with keyboard shortcuts
            - Pre-label images with an existing model
            - Review and approve annotations
            - Export in COCO and YOLO formats
Storage:    PostgreSQL, S3
Tech stack: Python, FastAPI, React, Konva.js
```

---

## Example 351

**Intent:**
analise de sentimento dos comentarios do youtube do nosso canal

**Spec:**
```
Type:       Data analysis script (YouTube comment sentiment)
Features:   - Collect comments from all channel videos through the YouTube API
            - Score sentiment with a Portuguese language model
            - Compute sentiment per video
            - Find the most common topics in negative comments
            - Export results to CSV
Input:      YouTube channel ID and API key
Tech stack: Python, google-api-python-client, Hugging Face Transformers (BERTimbau), pandas
```

---

## Example 352

**Intent:**
alert parents if their kid's grades drop

**Spec:**
```
Type:       Scheduled script (grade drop notifications)
Features:   - Fetch the latest grades from the school information system nightly
            - Compare each student's current average with their previous average
            - Detect drops of more than one grade band
            - Email parents with the subject and new grade
            - Let parents opt out
Tech stack: Python, PowerSchool API, SendGrid
```

---

## Example 353

**Intent:**
count insects on yellow sticky traps photos in our greenhouse

**Spec:**
```
Type:       Machine learning model (sticky trap insect counting)
Features:   - Detect and crop the trap in each photo
            - Detect insects with an object detection model
            - Classify insects into whitefly, thrips and aphid
            - Count insects per trap and date
            - Chart pest pressure trends per greenhouse zone
Input:      Photos of sticky traps with zone and date
Tech stack: Python, YOLOv8, OpenCV, pandas
```

---

## Example 354

**Intent:**
my company want to know: which of our job ads gets more applicants and why

**Spec:**
```
Type:       Data analysis script (job ad performance)
Features:   - Load job ads with title, salary, location and text
            - Count applicants per ad and per day posted
            - Analyse effects of salary visibility, remote option and ad length
            - Fit a regression on applicant counts
            - List recommendations for future ads
Input:      ATS export CSV of jobs and applications
Tech stack: Python, pandas, statsmodels
```

---

## Example 355

**Intent:**
Add a "summarize" button to our internal wiki

**Spec:**
```
Type:       Plugin (wiki summarisation)
Features:   - Add a summarise button to every wiki page
            - Send the page content to a language model
            - Show a short summary in a side panel
            - Cache summaries until the page is edited
            - Respect page permissions
Tech stack: Java, Atlassian Confluence plugin SDK, Claude API
```

---

## Example 356

**Intent:**
Quero mapear os acidentes de transito na minha cidade usando os dados abertos

**Spec:**
```
Type:       Data analysis script (traffic accident mapping)
Features:   - Download the open accident dataset
            - Clean coordinates and remove invalid points
            - Classify accidents by severity and vehicle type
            - Create a heatmap of accidents
            - List the 20 most dangerous intersections
Input:      Open data CSV of traffic accidents
Tech stack: Python, pandas, Folium
```

---

## Example 357

**Intent:**
predict wildfire risk per area for the next days

**Spec:**
```
Type:       Machine learning model (wildfire risk forecasting)
Features:   - Combine weather forecasts, vegetation dryness indices and past fire records
            - Grid the region into 1 km cells
            - Train a classifier for fire occurrence per cell and day
            - Produce a daily risk map for the next 5 days
            - Publish the map as map tiles
Input:      Weather forecast data, MODIS fire history and NDVI rasters
Tech stack: Python, xarray, XGBoost, GeoPandas, GDAL
```

---

## Example 358

**Intent:**
speech to text notes for my veterinary consults

**Spec:**
```
Type:       Mobile application with backend (veterinary consult notes)
Data model: Patient(id, name, species, owner_name)
            Consult(id, patient_id -> Patient, audio_url, transcript, notes, created_at)
Features:   - Record the consult on a tablet
            - Transcribe the conversation
            - Generate structured notes: history, exam, diagnosis and plan
            - Let the vet edit and sign notes
            - Export notes to the practice management system
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI, Deepgram API, Claude API
```

---

## Example 359

**Intent:**
help me find out why our machine learning model got worse last month

**Spec:**
```
Type:       Data analysis script (model drift investigation)
Features:   - Load prediction logs with features and outcomes
            - Compare feature distributions between two periods with PSI
            - Compute accuracy per month and segment
            - Find segments where error increased most
            - Produce a drift report
Input:      Prediction log Parquet files
Tech stack: Python, pandas, Evidently
```

---

## Example 360

**Intent:**
forecasting how many beds we need in our hospital in winter flu season

**Spec:**
```
Type:       Machine learning model (seasonal bed demand forecasting)
Features:   - Load daily admissions and occupancy history
            - Add influenza surveillance data as a leading indicator
            - Forecast daily occupancy for 8 weeks
            - Simulate scenarios for mild and severe seasons
            - Report the number of extra beds needed per week
Input:      Admissions CSV and public flu surveillance data
Tech stack: Python, pandas, Prophet
```

---

## Example 361

**Intent:**
CLI tool to split audio files by silence and transcribe each part

**Spec:**
```
Type:       Command-line tool (audio splitting and transcription)
Features:   - Detect silences longer than a set duration
            - Split audio into separate files
            - Transcribe each part
            - Name files by index and the first words spoken
            - Write an index CSV with start times and text
Input:      Audio file and silence settings
Tech stack: Python, pydub, faster-whisper, Typer
```

---

## Example 362

**Intent:**
which students are at risk of failing based on moodle activity

**Spec:**
```
Type:       Machine learning model (LMS activity risk prediction)
Features:   - Export Moodle logs, quiz grades and assignment submissions
            - Compute weekly engagement features per student
            - Train a classifier on past course outcomes
            - Score current students every week
            - Send at-risk lists to tutors with the main reasons
Input:      Moodle log export and gradebook CSV
Tech stack: Python, pandas, scikit-learn
```

---

## Example 363

**Intent:**
tool that turns my spreadsheet of experiment results into publication-ready plots

**Spec:**
```
Type:       Command-line tool (scientific plotting)
Features:   - Load data from Excel or CSV
            - Plot means with error bars per group
            - Add significance markers from t-tests
            - Use journal style fonts and sizes
            - Save figures as PDF and 300 dpi PNG
Input:      Spreadsheet with group and measurement columns and a YAML plot config
Tech stack: Python, pandas, matplotlib, SciPy
```

---

## Example 364

**Intent:**
realtime transcription of radio scanner traffic to text

**Spec:**
```
Type:       Data pipeline (radio transcription)
Features:   - Capture audio from a software-defined radio
            - Split transmissions by squelch
            - Transcribe each transmission
            - Tag transmissions with channel and time
            - Show a live searchable feed in the browser
Storage:    SQLite
Tech stack: Python, GNU Radio, faster-whisper, FastAPI, WebSocket
```

---

## Example 365

**Intent:**
monthly report of my etsy shop numbers emailed to me

**Spec:**
```
Type:       Scheduled script (shop monthly report)
Features:   - Fetch orders and listings from the Etsy API
            - Compute revenue, orders, average order value and top listings
            - Compare with the previous month
            - Build an HTML email with charts
            - Send on the first day of each month
Tech stack: Python, Etsy Open API, pandas, matplotlib, smtplib
```

---

## Example 366

**Intent:**
analyse cow milk yields from our milking robot data to find sick cows early

**Spec:**
```
Type:       Data analysis script (dairy herd health monitoring)
Features:   - Load daily milk yield, conductivity and rumination per cow
            - Compute each cow's expected yield from her lactation curve
            - Flag cows with sudden yield drops or high conductivity
            - Rank cows to check today
            - Plot history for flagged cows
Input:      Milking robot export CSV
Tech stack: Python, pandas, SciPy
```

---

## Example 367

**Intent:**
I'd like to build a model that detects sarcasm in tweets for my linguistics thesis

**Spec:**
```
Type:       Machine learning model (sarcasm detection)
Features:   - Load a labelled sarcasm dataset
            - Fine-tune a RoBERTa model
            - Compare with a logistic regression baseline
            - Evaluate with F1 and analyse errors
            - Report results per topic
Input:      Labelled tweets CSV (text, is_sarcastic)
Tech stack: Python, Hugging Face Transformers, scikit-learn
```

---

## Example 368

**Intent:**
our town wants to know how many tourists vs locals use the beach, from wifi probe data

**Spec:**
```
Type:       Data analysis script (visitor counting from WiFi probes)
Features:   - Load anonymised device hash detections per sensor
            - Classify devices as residents or visitors by how often they appear
            - Count unique devices per day
            - Estimate dwell time
            - Show daily visitors and residents over the season
Input:      WiFi probe CSV (device_hash, sensor_id, seen_at)
Tech stack: Python, pandas, matplotlib
```

---

## Example 369

**Intent:**
build a kids storytelling app where AI makes a story with the child's name and pictures

**Spec:**
```
Type:       Mobile application with backend (personalised story generator)
Data model: Child(id, parent_id, name, age, interests)
            Story(id, child_id -> Child, title, text, image_urls, created_at)
Features:   - Create a child profile with name, age and interests
            - Generate an age-appropriate story with a language model
            - Generate illustrations for each page
            - Read the story aloud with text-to-speech
            - Save favourite stories to a library
Storage:    PostgreSQL, S3
Tech stack: Flutter, Python, FastAPI, Claude API, image generation API
```

---

## Example 370

**Intent:**
extract data from scanned lab reports and plot my blood tests over the years

**Spec:**
```
Type:       Data analysis script (personal lab history)
Features:   - OCR scanned lab report PDFs
            - Extract test name, value, unit and date
            - Normalise test names and units
            - Store results in a table
            - Plot each test over time with reference ranges
Input:      Folder of lab report PDFs
Tech stack: Python, OCRmyPDF, pdfplumber, pandas, matplotlib
```

---

## Example 371

**Intent:**
speed camera data, are drivers slower after the new signs

**Spec:**
```
Type:       Data analysis script (speed change evaluation)
Features:   - Load vehicle speed records before and after the signs were installed
            - Compute mean and 85th percentile speeds
            - Compute the share exceeding the limit
            - Test differences with a bootstrap
            - Plot speed distributions before and after
Input:      Speed detector CSV (timestamp, speed_kmh)
Tech stack: Python, pandas, NumPy, matplotlib
```

---

## Example 372

**Intent:**
An ML service that predicts how long a delivery will take

**Spec:**
```
Type:       REST API service (delivery time estimation)
Features:   - Accept pickup, drop-off, time and order size
            - Get route distance and traffic estimate
            - Predict delivery time with a trained model
            - Return estimate with a confidence range
            - Log predictions and actual times for retraining
Storage:    PostgreSQL
Tech stack: Python, FastAPI, LightGBM, OSRM
```

---

## Example 373

**Intent:**
Hey, just need to merge 50 excel files from our branches into one and sum by product

**Spec:**
```
Type:       Command-line script (Excel consolidation)
Features:   - Read all Excel files in a folder
            - Check each file has the expected columns
            - Add a branch column from the file name
            - Combine files and sum quantities by product
            - Save the consolidated workbook
Input:      Folder of branch Excel files
Tech stack: Python, pandas, openpyxl
```

---

## Example 374

**Intent:**
Use YOLO to count apples on trees for harvest estimate

**Spec:**
```
Type:       Machine learning model (fruit counting)
Features:   - Detect apples in tree images
            - Track apples across video frames from both sides of the row
            - Avoid double counting with tracking
            - Estimate apples per tree and per row
            - Convert counts to estimated tonnes
Input:      Video recorded along orchard rows
Tech stack: Python, YOLOv8 (Ultralytics), ByteTrack, OpenCV
```

---

## Example 375

**Intent:**
comment toxicity on our news site: hide the worst automatically

**Spec:**
```
Type:       Web application (comment moderation)
Data model: Comment(id, article_id, author_id, text, toxicity_score, status, created_at)
Features:   - Score each new comment for toxicity
            - Hide comments above a high threshold automatically
            - Queue borderline comments for moderators
            - Let moderators approve or remove with one click
            - Report moderation volume per day
Storage:    PostgreSQL
Tech stack: Python, Django, Perspective API
```

---

## Example 376

**Intent:**
Build an ETL that reads IoT sensor JSON from MQTT and saves it into TimescaleDB

**Spec:**
```
Type:       Data pipeline (MQTT to time series database)
Features:   - Subscribe to sensor topics on the MQTT broker
            - Validate JSON payloads against a schema
            - Convert units and timestamps to UTC
            - Batch insert readings into hypertables
            - Retry and buffer when the database is unavailable
Storage:    TimescaleDB
Tech stack: Go, Eclipse Paho MQTT, pgx
```

---

## Example 377

**Intent:**
what makes some of our sales reps close more deals

**Spec:**
```
Type:       Data analysis script (sales rep performance drivers)
Features:   - Load CRM opportunities and activities per rep
            - Compute win rate, deal size and cycle length per rep
            - Count calls, emails and meetings per deal
            - Compare activity patterns of top and bottom performers
            - Present findings with charts
Input:      CRM export CSV of opportunities and activities
Tech stack: Python, pandas, seaborn
```

---

## Example 378

**Intent:**
I'd like an AI tutor for my 10 year old that teaches fractions with questions and hints

**Spec:**
```
Type:       Web application (fractions tutor for children)
Data model: Child(id, parent_id, name, grade)
            Exercise(id, topic, difficulty, question, answer)
            Attempt(id, child_id -> Child, exercise_id -> Exercise, answer, correct, hints_used)
Features:   - Ask fraction questions that adapt to the child's level
            - Give hints one step at a time
            - Show visual fraction bars
            - Praise effort and explain mistakes kindly
            - Show parents weekly progress
Storage:    PostgreSQL
Tech stack: TypeScript, React, Node.js, Claude API
```

---

## Example 379

**Intent:**
fraud detection for insurance claims

**Spec:**
```
Type:       Machine learning model (insurance claim fraud scoring)
Features:   - Build features from claim amount, timing, claimant history and provider
            - Detect shared phone numbers and addresses across claims with a graph
            - Train a classifier on investigated claims
            - Score new claims and explain the top factors
            - Send high scores to the special investigations unit
Tech stack: Python, pandas, NetworkX, XGBoost, SHAP
```

---

## Example 380

**Intent:**
which hours do people use our city's public toilets? sensors on doors

**Spec:**
```
Type:       Data analysis script (public toilet usage)
Features:   - Load door open events per toilet
            - Count uses per hour and weekday
            - Find busiest toilets and times
            - Estimate when cleaning is needed by use count
            - Show a weekly usage heatmap per toilet
Input:      Door sensor CSV (toilet_id, opened_at)
Tech stack: Python, pandas, seaborn
```

---

## Example 381

**Intent:**
Let users upload a song and get the lyrics transcribed with timing for karaoke

**Spec:**
```
Type:       Web application (karaoke lyric timing)
Features:   - Upload an audio file
            - Separate vocals from music
            - Transcribe vocals with word-level timestamps
            - Let users correct words in an editor
            - Export LRC and SRT lyric files
Storage:    S3, PostgreSQL
Tech stack: Python, Demucs, WhisperX, FastAPI, React
```

---

## Example 382

**Intent:**
compare temperature inside classrooms with outdoor temperature to find rooms that overheat

**Spec:**
```
Type:       Data analysis script (classroom overheating)
Features:   - Load indoor sensor readings per classroom
            - Load outdoor temperatures for the same period
            - Count school hours above 26 degrees C per room
            - Compare indoor-outdoor difference by room orientation
            - Rank rooms for shading or ventilation work
Input:      Indoor sensor CSV and outdoor weather CSV
Tech stack: Python, pandas, matplotlib
```

---

## Example 383

**Intent:**
tool that reads our inventory count sheets (handwritten numbers) and updates the system

**Spec:**
```
Type:       Data pipeline (handwritten count sheet capture)
Features:   - Scan count sheets with a fixed layout
            - Read product codes from printed barcodes
            - Recognise handwritten quantities
            - Show low-confidence cells for manual entry
            - Post counts to the inventory system API
Input:      Scanned count sheets (PDF)
Tech stack: Python, OpenCV, pyzbar, TrOCR, requests
```

---

## Example 384

**Intent:**
AI agent that researches companies and fills our CRM fields

**Spec:**
```
Type:       Bot (company research agent)
Features:   - Take a company name or domain from new CRM records
            - Search the web and the company site
            - Extract industry, size, location and description
            - Fill CRM fields with source links
            - Mark fields it could not verify
Tech stack: Python, Claude API (tool use), Tavily Search API, HubSpot API
```

---

## Example 385

**Intent:**
check the temperature of vaccines fridges at all our clinics, alert if out of 2-8 degrees

**Spec:**
```
Type:       IoT system (vaccine cold chain monitoring)
Data model: Clinic(id, name, contact_phone)
            Fridge(id, clinic_id -> Clinic, label)
            TempReading(id, fridge_id -> Fridge, temp_c, recorded_at)
            Excursion(id, fridge_id -> Fridge, started_at, ended_at, min_temp, max_temp)
Features:   - Log fridge temperatures every 5 minutes
            - Detect excursions outside 2-8 degrees C
            - Send SMS alerts to clinic staff
            - Record staff actions for each excursion
            - Produce monthly cold chain reports
Storage:    PostgreSQL
Tech stack: ESP32, LoRaWAN, Python, FastAPI, Twilio
```

---

## Example 386

**Intent:**
data analysis of which household appliances use the most power from my smart plugs

**Spec:**
```
Type:       Data analysis script (appliance energy breakdown)
Features:   - Load power readings from each smart plug
            - Compute daily kWh per appliance
            - Estimate standby power use
            - Calculate monthly cost per appliance
            - Show a pie chart and a ranked table
Input:      Smart plug CSV exports
Tech stack: Python, pandas, matplotlib
```

---

## Example 387

**Intent:**
predict which trees in our city will fall in a storm

**Spec:**
```
Type:       Machine learning model (tree failure risk)
Features:   - Combine the tree inventory with species, height, trunk diameter and condition
            - Add soil type and wind exposure
            - Train a classifier on past storm failures
            - Map risk scores for every tree
            - Export a priority list for arborist inspections
Input:      Tree inventory CSV and storm damage records
Tech stack: Python, GeoPandas, scikit-learn
```

---

## Example 388

**Intent:**
sistema para analizar las notas de mis alumnos de ingles y ver en que habilidad fallan mas

**Spec:**
```
Type:       Data analysis script (language skills analysis)
Features:   - Load scores for listening, reading, writing and speaking
            - Compute average per skill and per student
            - Find each student's weakest skill
            - Group students by weakest skill
            - Create charts per class
Input:      Excel file with student and four skill scores
Tech stack: Python, pandas, matplotlib
```

---

## Example 389

**Intent:**
a dashboard of my apartment building's water usage per unit

**Spec:**
```
Type:       Data dashboard (building water consumption)
Features:   - Collect readings from smart water meters per unit
            - Show daily usage per unit
            - Flag possible leaks from constant overnight flow
            - Compare units by usage per resident
            - Generate monthly bills from the readings
Storage:    PostgreSQL
Tech stack: Python, Dash, Plotly, Modbus
```

---

## Example 390

**Intent:**
Show me a heatmap of where our delivery drones fly and how high

**Spec:**
```
Type:       Data analysis script (drone flight log analysis)
Features:   - Load flight logs with GPS position and altitude
            - Aggregate positions into a grid
            - Draw a heatmap of flight density
            - Show altitude profiles per route
            - Flag flights above the legal altitude limit
Input:      Drone flight logs (CSV or DJI log export)
Tech stack: Python, pandas, kepler.gl
```

---

## Example 391

**Intent:**
Speech-to-text keyboard for a language with no good support (Swahili)

**Spec:**
```
Type:       Mobile application (Swahili voice keyboard)
Features:   - Provide a custom keyboard with a microphone button
            - Transcribe Swahili speech with a fine-tuned model
            - Insert text into any app
            - Add punctuation automatically
            - Learn new words the user adds
Tech stack: Kotlin (Android), Whisper (fine-tuned on Common Voice Swahili), TensorFlow Lite
```

---

## Example 392

**Intent:**
help me spot outliers in my company's expense claims

**Spec:**
```
Type:       Data analysis script (expense claim outliers)
Features:   - Load expense claims with employee, category and amount
            - Compare each claim with the category median
            - Detect duplicate claims with the same amount and date
            - Flag weekend and holiday claims
            - Export a review list
Input:      Expense system export CSV
Tech stack: Python, pandas
```

---

## Example 393

**Intent:**
Can a computer tell which wine regions a wine review is talking about? I have 100k reviews

**Spec:**
```
Type:       Machine learning model (wine review region classification)
Features:   - Load reviews with known regions
            - Train a text classifier on review text
            - Evaluate top-1 and top-3 accuracy
            - Show the most predictive words per region
            - Predict regions for unlabelled reviews
Input:      Wine reviews CSV (description, region)
Tech stack: Python, scikit-learn, pandas
```

---

## Example 394

**Intent:**
Build an ingestion pipeline on Azure for our hospital's appointment data into a lakehouse

**Spec:**
```
Type:       Data pipeline (healthcare lakehouse ingestion)
Features:   - Extract appointment tables from the on-premise database nightly
            - Land raw data as Parquet
            - Clean and deduplicate into silver tables
            - Build gold tables for no-show and utilisation reporting
            - Mask patient identifiers in gold tables
Storage:    Azure Data Lake Storage, Delta Lake
Tech stack: Azure Data Factory, Azure Databricks, PySpark
```

---

## Example 395

**Intent:**
track wildlife sightings from hikers on our trail with an app

**Spec:**
```
Type:       Mobile application with backend (trail wildlife sightings)
Data model: Sighting(id, user_id, species, count, lat, lon, photo_url, seen_at)
Features:   - Log a sighting with photo and GPS
            - Suggest species from the photo
            - Show sightings on a trail map
            - Show a list of recent sightings
            - Let rangers export data
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Node.js, Express, iNaturalist API
```

---

## Example 396

**Intent:**
AI that suggests better variable names in python code

**Spec:**
```
Type:       Plugin (VS Code variable naming assistant)
Features:   - Find short or unclear variable names in the open file
            - Suggest descriptive names with a language model
            - Show suggestions as code actions
            - Rename all references safely
            - Ignore loop counters like i and j
Tech stack: TypeScript, VS Code Extension API, Claude API
```

---

## Example 397

**Intent:**
analyze data from our solar-powered water pumps in villages, find which ones are failing

**Spec:**
```
Type:       Data analysis script (remote pump performance)
Features:   - Load daily flow and solar irradiance data per pump
            - Compute litres pumped per unit of sunlight
            - Detect pumps with declining efficiency
            - Flag pumps with zero flow on sunny days
            - Produce a maintenance priority list
Input:      Telemetry CSV per pump and irradiance data
Tech stack: Python, pandas, matplotlib
```

---

## Example 398

**Intent:**
please, i want program to know which customer will not renew phone contract

**Spec:**
```
Type:       Machine learning model (telecom contract churn prediction)
Features:   - Build features from usage, complaints, contract length and payment history
            - Train a gradient boosting classifier
            - Handle class imbalance
            - Rank customers ending their contract in the next 60 days by risk
            - Show reasons for each high-risk customer
Input:      Customer and usage data CSV
Tech stack: Python, pandas, LightGBM, SHAP
```

---

## Example 399

**Intent:**
a bot in our Mattermost that answers "how many X did we sell" from our database

**Spec:**
```
Type:       Bot (chat analytics assistant)
Features:   - Listen for questions mentioning the bot
            - Translate questions into read-only SQL with a language model
            - Run queries on a reporting replica
            - Reply with a number or a small table
            - Refuse questions about personal customer data
Tech stack: Python, Mattermost API, Claude API, SQLAlchemy
```

---

## Example 400

**Intent:**
Is the new teaching method working? Compare two groups test results, I have a pre and post test

**Spec:**
```
Type:       Data analysis script (teaching method comparison)
Features:   - Load pre-test and post-test scores for both groups
            - Check group balance at pre-test
            - Compare post-test scores adjusting for pre-test with ANCOVA
            - Compute effect size
            - Plot group means with confidence intervals
Input:      CSV with student_id, group, pre_score, post_score
Tech stack: R, tidyverse, emmeans, ggplot2
```

---

## Example 401

**Intent:**
scan QR codes on parcels and log when they arrive at each depot

**Spec:**
```
Type:       Mobile application with backend (parcel scanning)
Data model: Parcel(id, tracking_code, destination)
            ScanEvent(id, parcel_id -> Parcel, depot, scanned_by, scanned_at)
Features:   - Scan parcel QR codes with the phone camera
            - Record depot and time for each scan
            - Warn when a parcel is at the wrong depot
            - Work offline and sync later
            - Show parcel journey history
Storage:    PostgreSQL
Tech stack: Flutter, Go, PostgreSQL
```

---

## Example 402

**Intent:**
visualize our museum visitor paths from the ticket scanner gates

**Spec:**
```
Type:       Data analysis script (visitor flow analysis)
Features:   - Load gate scan events per ticket
            - Reconstruct the order of rooms visited
            - Compute time spent per room
            - Draw a Sankey diagram of common paths
            - Find rooms most often skipped
Input:      Gate scan CSV (ticket_id, gate_id, scanned_at)
Tech stack: Python, pandas, Plotly
```

---

## Example 403

**Intent:**
speech to text for court hearings in two languages mixed

**Spec:**
```
Type:       Data pipeline (bilingual hearing transcription)
Features:   - Transcribe hearing audio with code-switching support
            - Detect the language of each segment
            - Label speakers by role
            - Produce a transcript with timestamps
            - Let clerks correct and finalise the transcript
Input:      Hearing audio recordings
Storage:    PostgreSQL
Tech stack: Python, WhisperX, pyannote.audio, Django
```

---

## Example 404

**Intent:**
Analyse player ratings from our mobile game to balance characters

**Spec:**
```
Type:       Data analysis script (game balance analysis)
Features:   - Load match results with characters picked
            - Compute win rate and pick rate per character
            - Compute win rates by player skill bracket
            - Find overpowered and underused characters
            - Plot win rate against pick rate
Input:      Match logs CSV (match_id, player_rank, character, won)
Tech stack: Python, pandas, seaborn
```

---

## Example 405

**Intent:**
dog breed classifier app for my puppy school

**Spec:**
```
Type:       Mobile application (dog breed identification)
Features:   - Take or choose a photo of a dog
            - Predict top 3 breeds with confidence
            - Show breed information
            - Estimate mixed breeds with percentages
            - Run on the device
Tech stack: Swift (iOS), Core ML, Create ML
```

---

## Example 406

**Intent:**
Scraper + NLP: what do job ads ask for in data science skills this year

**Spec:**
```
Type:       Data analysis script (job market skill demand)
Features:   - Scrape data science job ads from job boards
            - Extract skills with a skill keyword list and NER
            - Count skill frequency by month and seniority
            - Compare with last year
            - Chart rising and falling skills
Input:      Job board search URLs
Tech stack: Python, Scrapy, spaCy, pandas, matplotlib
```

---

## Example 407

**Intent:**
water leak detection in our office building from water meter data

**Spec:**
```
Type:       Data analysis script (leak detection)
Features:   - Load hourly water meter readings
            - Compute minimum night flow per day
            - Flag nights with continuous flow above a threshold
            - Estimate litres lost per leak period
            - Send an email summary of suspected leaks
Input:      Water meter CSV (timestamp, litres)
Tech stack: Python, pandas, smtplib
```

---

## Example 408

**Intent:**
build a pipeline in dbt that turns our raw school data into clean reporting tables

**Spec:**
```
Type:       Data pipeline (education data modelling)
Features:   - Define source tables for students, enrolments, grades and attendance
            - Clean and standardise codes in staging models
            - Build fact and dimension tables
            - Add tests for uniqueness and referential integrity
            - Document models with descriptions
Storage:    PostgreSQL
Tech stack: dbt Core, SQL
```

---

## Example 409

**Intent:**
model that predicts customer lifetime value for our coffee subscription

**Spec:**
```
Type:       Machine learning model (customer lifetime value)
Features:   - Compute purchase frequency, recency and average order value
            - Fit BG/NBD and Gamma-Gamma models
            - Predict 12-month value per customer
            - Segment customers by predicted value
            - Export values to the email platform
Input:      Order history CSV
Tech stack: Python, lifetimes, pandas
```

---

## Example 410

**Intent:**
check if our A/B test on email subject lines had any effect on opens and clicks

**Spec:**
```
Type:       Data analysis script (email A/B test)
Features:   - Load sends, opens and clicks per variant
            - Compute open and click rates
            - Run chi-square tests
            - Compute confidence intervals for uplift
            - Write a short conclusion per metric
Input:      Email platform export CSV (recipient, variant, opened, clicked)
Tech stack: Python, pandas, SciPy
```

---

## Example 411

**Intent:**
seating chart from test scores

**Spec:**
```
Type:       Command-line script (classroom seating plan)
Features:   - Load student test scores and seating constraints
            - Pair stronger and weaker students as table partners
            - Keep listed students apart
            - Respect front-row needs
            - Print a seating chart as a grid
Input:      CSV of students with scores and a constraints file
Tech stack: Python, pandas
```

---

## Example 412

**Intent:**
Which of my teams' players are improving in their sprint times this season? I have data from GPS vests

**Spec:**
```
Type:       Data analysis script (athlete sprint performance)
Features:   - Load GPS vest session data per player
            - Extract top speed and number of sprints per session
            - Compute rolling averages per player
            - Flag players with falling top speed as possible fatigue
            - Plot season trends per player
Input:      GPS vest CSV exports (player, session_date, max_speed, sprint_count, distance)
Tech stack: Python, pandas, matplotlib
```

---

## Example 413

**Intent:**
digitize hospital paper consent forms and check they were all signed

**Spec:**
```
Type:       Data pipeline (consent form verification)
Features:   - Scan consent forms and classify the form type
            - Detect signature boxes and check they contain a signature
            - Read patient number and date with OCR
            - Match forms to scheduled procedures
            - List procedures with missing or unsigned consent
Input:      Scanned consent form PDFs and procedure schedule
Storage:    PostgreSQL
Tech stack: Python, OpenCV, Tesseract, pandas
```

---

## Example 414

**Intent:**
an ML model that tells how ripe a banana is from a photo

**Spec:**
```
Type:       Machine learning model (fruit ripeness classification)
Features:   - Collect banana photos labelled by ripeness stage
            - Fine-tune a small CNN
            - Predict stage from 1 to 7
            - Estimate days until overripe
            - Export a TensorFlow Lite model for a phone app
Input:      Labelled banana images
Tech stack: Python, TensorFlow, Keras
```

---

## Example 415

**Intent:**
Analyse our library's e-book usage vs print loans during the last 5 years

**Spec:**
```
Type:       Data analysis script (e-book vs print usage)
Features:   - Load e-book checkout and print loan records
            - Compute monthly usage for each format
            - Compare by genre and age group
            - Find titles popular in both formats
            - Chart format share over time
Input:      E-book platform export and ILS loans export (CSV)
Tech stack: Python, pandas, Plotly
```

---

## Example 416

**Intent:**
hlp me predict exam pass rate for my driving school students

**Spec:**
```
Type:       Machine learning model (driving test pass prediction)
Features:   - Build features from lessons taken, instructor, mock test scores and age
            - Train a logistic regression
            - Predict pass probability before booking a test
            - Recommend extra lessons for low-probability students
            - Report accuracy on last year's tests
Input:      Student records CSV
Tech stack: Python, scikit-learn, pandas
```

---

## Example 417

**Intent:**
Clustering of electricity customers by their daily load shape

**Spec:**
```
Type:       Data analysis script (load profile clustering)
Features:   - Load half-hourly consumption per customer
            - Normalise each daily profile
            - Cluster profiles with k-means
            - Plot the average load shape per cluster
            - Assign each customer to a dominant cluster
Input:      Smart meter CSV (customer_id, timestamp, kwh)
Tech stack: Python, pandas, tslearn, matplotlib
```

---

## Example 418

**Intent:**
I need to know how my clinic's patients rate us in google reviews over time and what they say

**Spec:**
```
Type:       Data analysis script (clinic Google review analysis)
Features:   - Collect reviews through the Google Business Profile API
            - Plot average rating per month
            - Classify comments into topics such as wait time, staff and billing
            - Score sentiment per topic
            - List the most recent negative reviews
Tech stack: Python, Google Business Profile API, Claude API, pandas
```

---

## Example 419

**Intent:**
Bot on Telegram that answers questions about our university timetable

**Spec:**
```
Type:       Bot (timetable assistant)
Features:   - Load the timetable from the university iCal feeds
            - Answer questions like "where is my next class"
            - Let students subscribe to their course group
            - Send a morning message with the day's classes
            - Notify about room changes
Storage:    SQLite
Tech stack: Python, aiogram, icalendar
```

---

## Example 420

**Intent:**
estimate air quality inside classrooms from CO2 sensors and tell teachers to open windows

**Spec:**
```
Type:       IoT system (classroom CO2 monitoring)
Data model: Room(id, name, building)
            CO2Reading(id, room_id -> Room, ppm, temp_c, recorded_at)
Features:   - Measure CO2 every minute in each classroom
            - Show a traffic light on a small display
            - Notify the teacher when CO2 exceeds 1,200 ppm
            - Report daily time above limits per room
            - Show a dashboard for the facilities team
Storage:    InfluxDB
Tech stack: ESP32, SCD30 sensor, MQTT, Grafana
```

---

## Example 421

**Intent:**
Sentiment classifier for Arabic product reviews

**Spec:**
```
Type:       Machine learning model (Arabic review sentiment)
Features:   - Normalise Arabic text: diacritics, letter variants and elongation
            - Fine-tune an Arabic BERT model
            - Handle dialect and Modern Standard Arabic
            - Evaluate with macro F1
            - Serve predictions through an API
Tech stack: Python, Hugging Face Transformers (AraBERT), FastAPI
```

---

## Example 422

**Intent:**
show the busiest times at our ski lifts from gate scans

**Spec:**
```
Type:       Data dashboard (ski lift queue monitoring)
Features:   - Stream lift gate scans
            - Compute riders per lift per 10 minutes
            - Estimate queue wait from rider rate and lift capacity
            - Show live wait times on screens around the resort
            - Show historical busy times
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Redis, Vue.js
```

---

## Example 423

**Intent:**
write me a python script that reads all PDFs in a folder and finds every email address and phone number

**Spec:**
```
Type:       Command-line script (contact extraction from PDFs)
Features:   - Read text from every PDF in a folder
            - Find email addresses and phone numbers with regex
            - Normalise phone numbers to international format
            - Remove duplicates
            - Save results with the source file to CSV
Input:      Folder of PDF files
Tech stack: Python, pdfplumber, phonenumbers
```

---

## Example 424

**Intent:**
can you build me an AI resume tailor that adjusts my CV to each job posting but never invents experience

**Spec:**
```
Type:       Web application (CV tailoring assistant)
Data model: Profile(id, user_id, master_cv)
            JobPosting(id, user_id, url, text)
            TailoredCV(id, job_id -> JobPosting, content, created_at)
Features:   - Store a master CV with all experience
            - Paste a job posting URL or text
            - Reorder and reword bullet points to match the posting
            - Check that every claim exists in the master CV
            - Export the tailored CV as PDF
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Claude API, Puppeteer (PDF)
```

---

## Example 425

**Intent:**
Weekly attendance report to the principal with charts

**Spec:**
```
Type:       Scheduled script (weekly attendance report)
Features:   - Pull the week's attendance from the school database
            - Compute attendance per year group and class
            - Compare with the school target
            - Create charts and a list of students below 85 percent
            - Email the PDF report every Friday
Storage:    MySQL (school database)
Tech stack: Python, pandas, matplotlib, WeasyPrint, cron
```

---

## Example 426

**Intent:**
how long do patients wait for surgery by specialty

**Spec:**
```
Type:       Data analysis script (surgical waiting list analysis)
Features:   - Load waiting list entries with referral and surgery dates
            - Compute waiting time per specialty
            - Show the share waiting over 18 weeks
            - Forecast list size from referral and surgery rates
            - Chart median waits over time
Input:      Waiting list CSV (patient_ref, specialty, referred_at, operated_at)
Tech stack: Python, pandas, matplotlib
```

---

## Example 427

**Intent:**
train a model that detects helmets on construction workers from CCTV

**Spec:**
```
Type:       Machine learning model (PPE compliance detection)
Features:   - Detect workers in camera frames
            - Classify each worker as with or without a helmet and vest
            - Raise alerts when a worker without a helmet is seen in the work zone
            - Blur faces in saved alert images
            - Report daily compliance rate per camera
Tech stack: Python, YOLOv8, OpenCV
```

---

## Example 428

**Intent:**
dashboard for our community garden harvest logs

**Spec:**
```
Type:       Data dashboard (community garden harvest)
Features:   - Record harvests with plot, crop and weight through a form
            - Show total harvest per crop and month
            - Rank plots by yield per square metre
            - Show a season comparison
            - Export data for the annual report
Storage:    Google Sheets
Tech stack: Google Forms, Google Sheets, Looker Studio
```

---

## Example 429

**Intent:**
find out the best time of day to water plants by checking soil sensor data and evaporation

**Spec:**
```
Type:       Data analysis script (irrigation timing analysis)
Features:   - Load soil moisture readings and irrigation events
            - Measure moisture retained 6 hours after each watering
            - Compare watering times of day
            - Account for temperature and sunlight
            - Recommend the best watering time
Input:      Sensor CSV and irrigation log
Tech stack: Python, pandas, statsmodels
```

---

## Example 430

**Intent:**
a pipeline that moves new customer reviews from Trustpilot to our data warehouse daily

**Spec:**
```
Type:       Data pipeline (review ingestion)
Features:   - Fetch new reviews through the Trustpilot API
            - Deduplicate reviews already loaded
            - Add sentiment scores
            - Load reviews into the warehouse
            - Log row counts per run
Storage:    Snowflake
Tech stack: Python, Dagster, Trustpilot API
```

---

## Example 431

**Intent:**
i have csv of earthquakes, plot them on a world map sized by magnitude

**Spec:**
```
Type:       Data analysis script (earthquake mapping)
Features:   - Load the earthquake CSV
            - Filter by date range and minimum magnitude
            - Plot epicentres on a world map
            - Size and colour points by magnitude and depth
            - Save as an interactive HTML map
Input:      CSV with time, latitude, longitude, depth, magnitude
Tech stack: Python, pandas, Plotly
```

---

## Example 432

**Intent:**
chatbot that walks new employees through IT setup steps

**Spec:**
```
Type:       Chatbot (IT onboarding assistant)
Features:   - Greet new employees and check which laptop they received
            - Guide them through account, VPN and email setup step by step
            - Answer questions from IT documentation
            - Create a helpdesk ticket when a step fails
            - Report onboarding completion to IT
Tech stack: Python, Microsoft Bot Framework, Azure OpenAI Service, ServiceNow API
```

---

## Example 433

**Intent:**
My research group needs to process flow cytometry files and count cell populations automatically

**Spec:**
```
Type:       Data pipeline (flow cytometry gating)
Features:   - Read FCS files for each sample
            - Apply compensation and transformation
            - Gate cell populations with automated clustering
            - Count cells and percentages per population
            - Export a summary table and gating plots
Input:      Folder of FCS files and a sample sheet
Tech stack: Python, FlowKit, scikit-learn, matplotlib
```

---

## Example 434

**Intent:**
use the webcam to detect if I'm slouching and remind me to sit straight

**Spec:**
```
Type:       Desktop application (posture monitor)
Features:   - Capture webcam frames every few seconds
            - Estimate shoulder and head keypoints
            - Detect slouching compared with a calibrated good posture
            - Show a desktop notification after 2 minutes of slouching
            - Show daily posture statistics
Tech stack: Python, MediaPipe Pose, OpenCV, plyer
```

---

## Example 435

**Intent:**
predict demand for city bikes at each station next hour to plan rebalancing

**Spec:**
```
Type:       Machine learning model (bike-share demand forecasting)
Features:   - Build features from station history, time, weather and events
            - Train a model for pickups and drop-offs per station
            - Predict next-hour net flow
            - Recommend bikes to move between stations
            - Evaluate error per station
Input:      Trip history and weather data
Tech stack: Python, pandas, LightGBM
```

---

## Example 436

**Intent:**
Check the readability and jargon of our government website pages

**Spec:**
```
Type:       Command-line tool (plain language audit)
Features:   - Crawl site pages from a sitemap
            - Extract main text
            - Compute readability scores
            - Find jargon from a list of words with plain alternatives
            - Output a ranked report of pages to rewrite
Input:      Sitemap URL and jargon word list
Tech stack: Python, Scrapy, trafilatura, textstat
```

---

## Example 437

**Intent:**
analizar la asistencia a nuestro gimnasio y ver que clases se llenan

**Spec:**
```
Type:       Data analysis script (fitness class occupancy)
Features:   - Load class bookings and check-ins
            - Compute fill rate per class type, instructor and time slot
            - Find classes with waiting lists
            - Find no-show rates
            - Recommend schedule changes
Input:      Booking system export CSV
Tech stack: Python, pandas, seaborn
```

---

## Example 438

**Intent:**
tool for radiologists to compare tumor size across scans automatically

**Spec:**
```
Type:       Machine learning model (tumour segmentation and tracking)
Features:   - Load CT series in DICOM format
            - Segment the tumour with a 3D U-Net
            - Register follow-up scans to the baseline
            - Compute volume and longest diameter per scan
            - Report changes as percentage growth or shrinkage
Input:      CT DICOM series for baseline and follow-up
Tech stack: Python, MONAI, SimpleITK, pydicom
```

---

## Example 439

**Intent:**
classify tweets during disasters into needs like food, water, shelter

**Spec:**
```
Type:       Machine learning model (crisis message classification)
Features:   - Train a multi-label classifier on labelled crisis tweets
            - Detect needs such as food, water, shelter and medical help
            - Extract locations mentioned in tweets
            - Group messages by location and need
            - Show results on a map for relief teams
Tech stack: Python, Hugging Face Transformers, spaCy, Folium
```

---

## Example 440

**Intent:**
Measure how fast our website search returns results and if people click them

**Spec:**
```
Type:       Data analysis script (site search quality)
Features:   - Load search logs with latency and clicks
            - Compute median and 95th percentile latency
            - Compute click-through rate and mean reciprocal rank
            - Find queries with low click-through
            - Plot trends weekly
Input:      Search log CSV (query, latency_ms, results, clicked_position)
Tech stack: Python, pandas, matplotlib
```

---

## Example 441

**Intent:**
an app that reads nutrition labels on food packaging and tracks my sugar intake

**Spec:**
```
Type:       Mobile application (nutrition label scanner)
Data model: FoodItem(id, name, barcode, sugar_per_100g)
            IntakeLog(id, food_item_id -> FoodItem, grams, eaten_at)
Features:   - Scan the barcode and look up the product
            - Read the nutrition table with OCR if not found
            - Log how much was eaten
            - Show daily sugar against a limit
            - Show weekly trends
Storage:    Local SQLite
Tech stack: Flutter, Google ML Kit, Open Food Facts API
```

---

## Example 442

**Intent:**
plot how many students choose each university major over the last decade

**Spec:**
```
Type:       Data analysis script (major selection trends)
Features:   - Load enrolment counts per major and year
            - Group small majors into faculties
            - Compute percentage share per year
            - Plot a stacked area chart
            - Highlight the fastest growing majors
Input:      CSV with year, major, faculty, students
Tech stack: Python, pandas, Plotly
```

---

## Example 443

**Intent:**
automatic grading of programming assignments with unit tests

**Spec:**
```
Type:       Command-line tool (autograder)
Features:   - Collect student submissions from a folder
            - Run each submission against unit tests in an isolated container
            - Apply time and memory limits
            - Compute scores per test
            - Export grades and test logs to CSV
Input:      Submissions folder and test suite
Tech stack: Python, pytest, Docker
```

---

## Example 444

**Intent:**
forecast monthly water demand for our town for the next 5 years

**Spec:**
```
Type:       Machine learning model (long-term water demand forecasting)
Features:   - Load monthly water consumption and population data
            - Model seasonal patterns and temperature effects
            - Project population growth scenarios
            - Forecast demand for 60 months
            - Compare demand with supply capacity
Input:      Monthly consumption CSV, population projections and climate data
Tech stack: R, fable, tsibble, ggplot2
```

---

## Example 445

**Intent:**
Detect duplicate photos in my 50,000 photo library even if resized

**Spec:**
```
Type:       Command-line tool (duplicate photo finder)
Features:   - Scan folders for images
            - Compute perceptual hashes for each image
            - Group images with small hash distances
            - Pick the highest resolution image in each group
            - Move duplicates to a review folder
Input:      Root folder of photos
Tech stack: Python, imagehash, Pillow
```

---

## Example 446

**Intent:**
Analyse cricket ball-by-ball data to find each batter's weak bowling types

**Spec:**
```
Type:       Data analysis script (cricket batting matchups)
Features:   - Load ball-by-ball data
            - Compute strike rate and dismissal rate per batter against each bowling type
            - Require a minimum number of balls
            - Show matchup heatmaps
            - Rank batters' weakest matchups
Input:      Ball-by-ball JSON from Cricsheet
Tech stack: Python, pandas, seaborn
```

---

## Example 447

**Intent:**
smart doorbell that recognizes my family and tells me who is at the door

**Spec:**
```
Type:       IoT system (face recognition doorbell)
Data model: Person(id, name, face_embedding)
            Visit(id, person_id -> Person, snapshot_path, occurred_at)
Features:   - Capture a snapshot when the doorbell is pressed or motion is detected
            - Recognise known family members
            - Send a phone notification with the name or "unknown visitor"
            - Keep all face data on a local server
            - Show a visit history
Storage:    SQLite on a local server
Tech stack: Raspberry Pi, Python, face_recognition, Home Assistant
```

---

## Example 448

**Intent:**
find patterns in my credit card spending and where i can save

**Spec:**
```
Type:       Data analysis script (personal spending analysis)
Features:   - Load card transactions from CSV
            - Categorise merchants
            - Find recurring subscriptions
            - Compare monthly spending per category
            - Highlight categories above the 3-month average
Input:      Bank CSV export
Tech stack: Python, pandas, matplotlib
```

---

## Example 449

**Intent:**
a model to predict the solar power my panels will produce tomorrow

**Spec:**
```
Type:       Machine learning model (solar generation forecasting)
Features:   - Load hourly production history
            - Join with historical cloud cover and irradiance
            - Train a model with hour, season and weather features
            - Predict tomorrow's hourly production from the forecast
            - Compare predictions with actual production daily
Input:      Inverter export CSV and weather API
Tech stack: Python, pandas, scikit-learn, Open-Meteo API
```

---

## Example 450

**Intent:**
use large language model to write SQL documentation for each table in our warehouse

**Spec:**
```
Type:       Command-line tool (data catalogue documentation)
Features:   - Read table and column metadata from the warehouse
            - Sample a few rows per table
            - Generate table and column descriptions with a language model
            - Mark descriptions as AI-generated for review
            - Write descriptions to dbt YAML files
Input:      Warehouse connection settings
Tech stack: Python, Snowflake connector, Claude API, PyYAML
```

---

## Example 451

**Intent:**
we need to see which classes in our university have too many students for the room

**Spec:**
```
Type:       Data analysis script (room capacity check)
Features:   - Load the timetable with room assignments
            - Load room capacities
            - Compare enrolment with capacity per session
            - List over-capacity and badly under-used sessions
            - Suggest swaps with free rooms of the right size
Input:      Timetable CSV and rooms CSV
Tech stack: Python, pandas
```

---

## Example 452

**Intent:**
Data pipeline that downloads satellite night lights images and measures city growth

**Spec:**
```
Type:       Data pipeline (night-time lights analysis)
Features:   - Download monthly VIIRS night lights composites
            - Clip to city boundaries
            - Compute total radiance per city per month
            - Detect growth trends
            - Export a time series CSV and maps
Input:      City boundary GeoJSON
Tech stack: Python, Google Earth Engine API, rasterio, GeoPandas
```

---

## Example 453

**Intent:**
identify bird nests in power line inspection drone images

**Spec:**
```
Type:       Machine learning model (power line inspection)
Features:   - Detect towers, insulators and bird nests in drone images
            - Record the GPS location of each detection
            - Classify insulator damage
            - Prioritise findings by risk
            - Export findings for the maintenance team
Input:      Drone inspection images with GPS metadata
Tech stack: Python, YOLOv8, ExifRead, pandas
```

---

## Example 454

**Intent:**
whats the average response time of our team on whatsapp business chats

**Spec:**
```
Type:       Data analysis script (chat response time)
Features:   - Load chat export with sender and timestamps
            - Pair customer messages with the next agent reply
            - Compute response time per agent
            - Exclude out-of-hours messages
            - Plot response times by hour
Input:      WhatsApp Business chat export (TXT or CSV)
Tech stack: Python, pandas, matplotlib
```

---

## Example 455

**Intent:**
An LLM pipeline that classifies scientific abstracts into our research taxonomy

**Spec:**
```
Type:       Data pipeline (abstract classification)
Features:   - Fetch new abstracts from PubMed matching our search terms
            - Classify each into taxonomy categories with a language model
            - Store category and rationale
            - Sample 5 percent for human checks
            - Show weekly counts per category
Storage:    PostgreSQL
Tech stack: Python, Biopython (Entrez), Claude API, Prefect
```

---

## Example 456

**Intent:**
check the reading speed of my students with a timer app

**Spec:**
```
Type:       Mobile application (reading speed test)
Data model: Student(id, name, class)
            ReadingTest(id, student_id -> Student, passage_id, seconds, words, errors, tested_at)
Features:   - Show a passage and start a timer
            - Let the teacher tap words read incorrectly
            - Calculate words per minute and accuracy
            - Track progress per student
            - Export class results
Storage:    Local SQLite
Tech stack: Kotlin (Android), Jetpack Compose, Room
```

---

## Example 457

**Intent:**
model to estimate the calories burned from my smartwatch heart rate

**Spec:**
```
Type:       Machine learning model (calorie expenditure estimation)
Features:   - Load heart rate, accelerometer and activity type data
            - Combine with age, weight and sex
            - Train a regression model on labelled sessions
            - Estimate calories per minute
            - Compare with the watch's own estimate
Input:      Watch export CSV and user profile
Tech stack: Python, pandas, scikit-learn
```

---

## Example 458

**Intent:**
compare prices of rental cars across sites for my travel agency daily

**Spec:**
```
Type:       Scheduled script (rental car price monitoring)
Data model: Search(id, location, pickup_date, return_date)
            Quote(id, search_id -> Search, site, car_class, price, fetched_at)
Features:   - Run saved searches every morning
            - Collect prices per car class from each site
            - Store quotes over time
            - Find the cheapest site per search
            - Send a summary email with price changes
Storage:    PostgreSQL
Tech stack: Python, Playwright, pandas
```

---

## Example 459

**Intent:**
Analyse the effect of class size on student results in our district

**Spec:**
```
Type:       Data analysis script (class size effect)
Features:   - Load class sizes and student results
            - Join with prior attainment and school factors
            - Fit a multilevel model with students in classes in schools
            - Estimate the class size effect
            - Plot predicted scores by class size
Input:      CSV of students with class, school, class_size, prior_score, score
Tech stack: R, lme4, ggplot2
```

---

## Example 460

**Intent:**
text-to-speech audiobook from my blog posts

**Spec:**
```
Type:       Command-line tool (blog to audiobook)
Features:   - Fetch blog posts from the RSS feed
            - Clean text and remove code blocks
            - Convert each post to speech
            - Add intro and outro audio
            - Publish episodes to a podcast RSS feed
Input:      Blog RSS feed URL
Tech stack: Python, feedparser, Piper TTS, pydub
```

---

## Example 461

**Intent:**
Detect when cows are in heat from collar accelerometer data

**Spec:**
```
Type:       Machine learning model (cattle oestrus detection)
Features:   - Load activity counts from neck collars
            - Compute each cow's baseline activity
            - Detect activity peaks indicating heat
            - Alert the farmer with the best insemination window
            - Track detection accuracy against confirmed pregnancies
Input:      Collar activity CSV (cow_id, timestamp, activity)
Tech stack: Python, pandas, scikit-learn
```

---

## Example 462

**Intent:**
I want a scoreboard of which classrooms save the most electricity in our school competition

**Spec:**
```
Type:       Web application (energy saving competition)
Data model: Classroom(id, name, baseline_kwh)
            EnergyReading(id, classroom_id -> Classroom, kwh, date)
Features:   - Import daily sub-meter readings per classroom
            - Compute savings against each room's baseline
            - Show a ranked leaderboard
            - Show weekly winners
            - Show tips on the page for saving energy
Storage:    SQLite
Tech stack: Python, Flask, Chart.js
```

---

## Example 463

**Intent:**
ai tool to tag our ecommerce product images with color, style and pattern

**Spec:**
```
Type:       Data pipeline (product image attribute tagging)
Features:   - Load product images from the catalogue
            - Predict colour, pattern and style with zero-shot image classification
            - Write tags back to the product database
            - Send low-confidence tags to a review queue
            - Enable filtering by tags on the shop
Storage:    PostgreSQL
Tech stack: Python, CLIP, FastAPI
```

---

## Example 464

**Intent:**
script to anonymize names in interview transcripts before sharing

**Spec:**
```
Type:       Command-line script (transcript anonymisation)
Features:   - Read transcript text files
            - Detect person names, places and organisations
            - Replace them with consistent placeholders like PERSON_1
            - Save a key file separately
            - Write anonymised copies
Input:      Folder of transcript files
Tech stack: Python, spaCy
```

---

## Example 465

**Intent:**
explore a public dataset of olympic results, who wins most medals per capita

**Spec:**
```
Type:       Data analysis script (Olympic medals per capita)
Features:   - Load historical Olympic results
            - Join with country population data
            - Compute medals per million people
            - Rank countries by Games and overall
            - Plot the top 20 countries
Input:      Olympic results CSV and population CSV
Tech stack: Python, pandas, Plotly
```

---

## Example 466

**Intent:**
speech to sign language? no, make a tool that turns lecture videos into searchable transcripts by topic

**Spec:**
```
Type:       Web application (lecture video search)
Data model: Lecture(id, course, title, video_url)
            TranscriptSegment(id, lecture_id -> Lecture, start_s, text, embedding)
Features:   - Transcribe uploaded lecture videos
            - Split transcripts into topic segments
            - Search across lectures by keyword or meaning
            - Jump to the matching moment in the video
            - Generate a chapter list per lecture
Storage:    PostgreSQL with pgvector
Tech stack: Python, faster-whisper, FastAPI, React
```

---

## Example 467

**Intent:**
track my houseplants watering and use photos to see if they're healthy

**Spec:**
```
Type:       Mobile application (houseplant care tracker)
Data model: Plant(id, name, species, location, water_interval_days)
            WateringLog(id, plant_id -> Plant, watered_at)
            HealthCheck(id, plant_id -> Plant, photo_path, status, notes)
Features:   - Add plants with watering intervals
            - Remind me when a plant needs water
            - Log watering
            - Analyse plant photos for yellowing or wilting
            - Show each plant's history
Storage:    Local SQLite
Tech stack: React Native, Expo, TensorFlow.js
```

---

## Example 468

**Intent:**
Analyse 20 years of our marathon finish times by age group

**Spec:**
```
Type:       Data analysis script (marathon results analysis)
Features:   - Load finisher results from all years
            - Clean times and assign age groups
            - Compute median finish time by age group, sex and year
            - Compute participation trends
            - Plot finish time distributions per decade
Input:      Results CSV per year
Tech stack: Python, pandas, seaborn
```

---

## Example 469

**Intent:**
ML model to detect diabetic retinopathy from eye photos for a rural clinic

**Spec:**
```
Type:       Machine learning model (retinal image screening)
Features:   - Preprocess fundus photos: crop, colour normalise and resize
            - Fine-tune a CNN on graded retinal images
            - Predict referable retinopathy
            - Check image quality and ask for a retake if poor
            - Run on a laptop without internet
Input:      Labelled fundus photo dataset
Tech stack: Python, PyTorch, timm, ONNX Runtime
```

---

## Example 470

**Intent:**
summarize product reviews into pros and cons for each product page

**Spec:**
```
Type:       Data pipeline (review pros and cons summarisation)
Features:   - Collect reviews per product nightly
            - Skip products with fewer than 10 reviews
            - Summarise reviews into 3 pros and 3 cons with a language model
            - Store the summary with the review count
            - Show summaries on product pages
Storage:    PostgreSQL
Tech stack: Python, Claude API, Celery
```

---

## Example 471

**Intent:**
detention records, which kids and which teachers give the most

**Spec:**
```
Type:       Data analysis script (behaviour incident analysis)
Features:   - Load detention and behaviour incident records
            - Count incidents per student, teacher and reason
            - Find students with repeat incidents in a term
            - Compare rates by year group and lesson period
            - Export a summary for the pastoral team
Input:      Behaviour log CSV (student_id, teacher, reason, date, period)
Tech stack: Python, pandas, matplotlib
```

---

## Example 472

**Intent:**
i got temperature logger data from my beer fermentation, show me the curve and alert if too hot

**Spec:**
```
Type:       IoT system (fermentation monitoring)
Features:   - Read the fermenter temperature probe every minute
            - Plot the fermentation temperature curve
            - Alert by phone above a set temperature
            - Control a cooling relay automatically
            - Save each batch's log
Storage:    InfluxDB
Tech stack: Raspberry Pi, DS18B20, Python, Grafana
```

---

## Example 473

**Intent:**
Model that estimates traffic noise for any street using traffic counts and road type

**Spec:**
```
Type:       Machine learning model (road noise estimation)
Features:   - Combine noise measurements with traffic counts, speed limit and road surface
            - Train a regression model for daytime noise level
            - Predict noise for unmeasured streets
            - Map predicted noise for the city
            - Report model error by road type
Input:      Noise measurement CSV and road network data
Tech stack: Python, GeoPandas, scikit-learn
```

---

## Example 474

**Intent:**
sort voicemails by urgency and transcribe them for our plumbing company

**Spec:**
```
Type:       Data pipeline (voicemail triage)
Features:   - Fetch new voicemails from the phone system
            - Transcribe each voicemail
            - Classify urgency such as flooding or no hot water
            - Extract the caller's address and callback number
            - Push urgent jobs to the dispatcher by SMS
Tech stack: Python, Twilio, faster-whisper, Claude API
```

---

## Example 475

**Intent:**
which of our museum exhibitions brought the most visitors, adjusting for season

**Spec:**
```
Type:       Data analysis script (exhibition impact analysis)
Features:   - Load daily ticket sales and exhibition dates
            - Model baseline visitors by weekday and season
            - Estimate extra visitors during each exhibition
            - Rank exhibitions by uplift
            - Chart actual against baseline visitors
Input:      Daily ticket CSV and exhibition list
Tech stack: Python, pandas, statsmodels
```

---

## Example 476

**Intent:**
Build a REST API that returns the predicted crop yield for a field given its location and planting date

**Spec:**
```
Type:       REST API service (crop yield prediction)
Features:   - Accept field coordinates, crop and planting date
            - Fetch soil and weather data for the location
            - Run the trained yield model
            - Return predicted yield with an interval
            - Log requests for usage reporting
Tech stack: Python, FastAPI, scikit-learn, SoilGrids API
```

---

## Example 477

**Intent:**
wanna know if more people visit my blog when i post on tuesdays

**Spec:**
```
Type:       Data analysis script (posting day effect)
Features:   - Load page views and publish dates per post
            - Compute views in the first 7 days per post
            - Group posts by publish weekday
            - Test differences with a Kruskal-Wallis test
            - Plot views by weekday
Input:      Analytics export CSV and list of posts with dates
Tech stack: Python, pandas, SciPy
```

---

## Example 478

**Intent:**
a dashboard showing how many students use the school canteen each day and what they buy

**Spec:**
```
Type:       Data dashboard (school canteen sales)
Features:   - Load cashless payment transactions from the canteen till
            - Show daily meals sold by item
            - Show uptake by year group
            - Compare healthy and less healthy item sales
            - Filter by week and term
Storage:    MySQL
Tech stack: Python, Streamlit, pandas
```

---

## Example 479

**Intent:**
summarize github repos activity in plain english for our manager every friday

**Spec:**
```
Type:       Scheduled script (engineering activity summary)
Features:   - Collect merged pull requests, releases and closed issues for the week
            - Group changes by repository and theme
            - Write a plain-language summary with a language model
            - Highlight risks such as failing builds
            - Email the summary every Friday
Tech stack: Python, PyGithub, Claude API, SendGrid
```

---

## Example 480

**Intent:**
count the number of seeds in petri dish photos for germination tests

**Spec:**
```
Type:       Data analysis script (seed germination counting)
Features:   - Load petri dish photos
            - Detect the dish and mask the background
            - Segment seeds and detect sprouted ones by shape
            - Count total and germinated seeds
            - Export germination rates per dish to CSV
Input:      Folder of petri dish images
Tech stack: Python, OpenCV, scikit-image
```

---

## Example 481

**Intent:**
our fleet trucks have telematics, find drivers who brake harshly a lot

**Spec:**
```
Type:       Data analysis script (driver behaviour scoring)
Features:   - Load telematics events: harsh braking, acceleration and speeding
            - Normalise events per 100 km driven
            - Score each driver
            - Rank drivers and show trends per month
            - Export a coaching list
Input:      Telematics CSV (driver_id, event_type, timestamp, km_driven)
Tech stack: Python, pandas, matplotlib
```

---

## Example 482

**Intent:**
An AI study planner that makes a revision timetable from my exam dates and weak topics

**Spec:**
```
Type:       Web application (revision planner)
Data model: Exam(id, user_id, subject, date)
            Topic(id, exam_id -> Exam, name, confidence)
            StudySession(id, topic_id -> Topic, scheduled_at, minutes, done)
Features:   - Enter exams and topics with a confidence rating
            - Generate a timetable that spends more time on weak topics
            - Use spaced repetition for review sessions
            - Adjust the plan when sessions are missed
            - Sync sessions to Google Calendar
Storage:    PostgreSQL
Tech stack: Python, Django, Google Calendar API
```

---
