## Example 1

**Intent:**
predict which customers will buy again

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Build customer features from order history (recency, frequency, monetary value)
            - Label customers who ordered again within 90 days as positive
            - Split the data into train and test sets by time
            - Train a gradient boosting classifier and report precision, recall and ROC AUC
            - Score all active customers with a repurchase probability
            - Export the top-scored customers to a CSV for the marketing team
Input:      Orders CSV with customer_id, order_date, order_total
Storage:    Local files (model file, scored CSV)
Tech stack: Python, pandas, scikit-learn, LightGBM
```

---

## Example 2

**Intent:**
dashboard for our website traffic

**Spec:**
```
Type:       Data dashboard (web analytics)
Features:   - Pull daily sessions, users, bounce rate and conversions from Google Analytics 4
            - Show traffic trends over time as line charts
            - Break down traffic by channel, device and country
            - Show the top landing pages and their conversion rate
            - Filter all charts by date range
Storage:    BigQuery (GA4 export)
Tech stack: Looker Studio, Google Analytics 4, BigQuery
```

---

## Example 3

**Intent:**
I run a small online shop on Shopify and every month I export the orders and try to figure out which products are doing well and which are dying. I'd love a script that just does this for me and gives me a simple report.

**Spec:**
```
Type:       Data analysis script (sales report)
Features:   - Load the monthly Shopify orders export
            - Calculate units sold and revenue per product for the current and previous month
            - Flag products whose sales dropped more than 30% month over month
            - Rank the top 10 and bottom 10 products by revenue
            - Save a bar chart of revenue per product
            - Write a one-page HTML report with the tables and charts
Input:      Shopify orders CSV export
Storage:    Local files (HTML report, PNG charts)
Tech stack: Python, pandas, matplotlib, Jinja2
```

---

## Example 4

**Intent:**
chatbot that answers questions about our employee handbook pdf

**Spec:**
```
Type:       Chatbot (document Q&A)
Features:   - Split the handbook PDF into overlapping text chunks
            - Create embeddings for each chunk and store them in a vector database
            - Retrieve the most relevant chunks for each employee question
            - Generate an answer with an LLM using only the retrieved text
            - Show the handbook section and page number used for the answer
            - Reply "I don't know" when no relevant section is found
Input:      Employee handbook PDF
Storage:    Chroma (vector database)
Tech stack: Python, LangChain, OpenAI API (embeddings and chat), Chroma, Streamlit
```

---

## Example 5

**Intent:**
forecast how many ice creams we sell next week based on weather

**Spec:**
```
Type:       Machine learning model (forecasting)
Features:   - Join daily sales history with historical weather (temperature, rain, sunshine hours)
            - Add calendar features such as weekday, holidays and school vacations
            - Train a regression model on past days and test it on the most recent 8 weeks
            - Report mean absolute error against a same-day-last-week baseline
            - Forecast daily sales for the next 7 days using the weather forecast
Input:      Daily sales CSV, weather API forecast
Storage:    Local CSV files
Tech stack: Python, pandas, scikit-learn, Open-Meteo API
```

---

## Example 6

**Intent:**
i have a bunch of csv files from our sensors every day and need them cleaned and put in one database table automaticaly

**Spec:**
```
Type:       Data pipeline (ETL)
Features:   - Watch an input folder for new sensor CSV files every day
            - Parse timestamps into UTC and convert units to a standard format
            - Drop duplicate rows and readings outside valid sensor ranges
            - Load clean rows into one PostgreSQL table with a sensor_id column
            - Move processed files to an archive folder
            - Log the number of rows loaded and rejected per file
Input:      Daily sensor CSV files
Storage:    PostgreSQL
Tech stack: Python, pandas, SQLAlchemy, cron
```

---

## Example 7

**Intent:**
In Power BI, I need a report of our HR data showing headcount, hires and leavers by department each month.

**Spec:**
```
Type:       Data dashboard (HR report)
Features:   - Import employee records with hire date, leave date and department
            - Calculate monthly headcount, hires and leavers with DAX measures
            - Show turnover rate per department as a line chart
            - Add slicers for department, location and year
            - Show a table of departments ranked by turnover
Input:      Employee records from the HR system (Excel export)
Tech stack: Power BI Desktop, DAX, Power Query
```

---

## Example 8

**Intent:**
hey can u make something that tells me if a tweet is positive or negative

**Spec:**
```
Type:       Machine learning model (sentiment analysis)
Features:   - Load a labelled dataset of tweets with positive and negative labels
            - Clean text by removing links, mentions and extra whitespace
            - Fine-tune a pretrained DistilBERT model for binary classification
            - Evaluate accuracy and F1 score on a held-out test set
            - Predict the sentiment and confidence for any new tweet text
Input:      Tweet text
Storage:    Local files (model weights)
Tech stack: Python, Hugging Face Transformers, PyTorch, datasets
```

---

## Example 9

**Intent:**
We have a call center and I want to know how many agents to schedule each hour next month. We have 3 years of call volume data per half-hour.

**Spec:**
```
Type:       Machine learning model (time series forecasting)
Features:   - Aggregate call volumes into hourly buckets
            - Model daily, weekly and yearly seasonality plus public holidays
            - Train on the first 30 months and validate on the last 6 months
            - Forecast hourly call volume for the next month with prediction intervals
            - Convert forecast volume into required agents using an Erlang C formula
            - Export the hourly staffing plan to Excel
Input:      Call volume history CSV (timestamp, calls, avg_handle_time)
Storage:    Local files (forecast Excel)
Tech stack: Python, Prophet, pandas, openpyxl
```

---

## Example 10

**Intent:**
analyze my running data from strava

**Spec:**
```
Type:       Data analysis script (fitness)
Features:   - Download all activities through the Strava API
            - Calculate weekly distance, average pace and elevation gain
            - Plot pace trend over time for runs of similar distance
            - Find personal bests for 5k, 10k and half marathon
            - Show heart rate zones distribution per month
Input:      Strava API access token
Storage:    Local CSV cache of activities
Tech stack: Python, stravalib, pandas, matplotlib, Jupyter
```

---

## Example 11

**Intent:**
i want detect fraud in credit card transaction, data is very unbalanced, only few fraud

**Spec:**
```
Type:       Machine learning model (anomaly detection)
Features:   - Load transactions with amount, time, merchant and card features
            - Split data into train and test sets with stratification on the fraud label
            - Handle class imbalance with SMOTE oversampling and class weights
            - Train an XGBoost classifier and tune the decision threshold
            - Evaluate with precision, recall and PR AUC instead of accuracy
            - Show the most important features with SHAP values
Input:      Transactions CSV with a fraud label
Storage:    Local files (trained model)
Tech stack: Python, pandas, XGBoost, imbalanced-learn, SHAP
```

---

## Example 12

**Intent:**
a bot in our slack that answers questions about our sales database in plain english

**Spec:**
```
Type:       Bot (Slack, text-to-SQL)
Features:   - Receive questions mentioned to the bot in Slack channels
            - Send the question and the database schema to an LLM to generate a SQL query
            - Allow only read-only SELECT queries and block everything else
            - Run the query on a read replica and format the result as a table
            - Attach a chart when the result is a time series
            - Show the generated SQL so users can check it
Storage:    PostgreSQL read replica
Tech stack: Python, Slack Bolt, OpenAI API, SQLAlchemy, matplotlib
```

---

## Example 13

**Intent:**
survey results excel

**Spec:**
```
Type:       Data analysis script (survey)
Features:   - Load survey responses from an Excel file
            - Count answers for each multiple-choice question
            - Calculate averages for rating scale questions
            - Cross-tabulate answers by age group and gender
            - Create a bar chart for each question
            - Save all tables and charts into a new Excel report
Input:      Excel file of survey responses (one row per respondent)
Storage:    Local Excel file (report)
Tech stack: Python, pandas, openpyxl, matplotlib
```

---

## Example 14

**Intent:**
I teach chemistry at a high school and my students always ask the same questions at night before the test. Could I make a tutor bot that explains things step by step but doesnt just give the homework answers?

**Spec:**
```
Type:       Chatbot (tutoring)
Data model: Conversation(id, student_alias, started_at)
            Message(id, conversation_id -> Conversation, role, text, created_at)
Features:   - Answer chemistry questions with step-by-step explanations
            - Ask the student guiding questions instead of giving full homework solutions
            - Use the teacher's course notes as reference material through retrieval
            - Generate short practice questions on a requested topic
            - Let the teacher review anonymous chat logs to see common difficulties
Storage:    SQLite (chat logs), FAISS (course notes index)
Tech stack: Python, FastAPI, Anthropic Claude API, FAISS, React
```

---

## Example 15

**Intent:**
recommend similar products on our webshop product page

**Spec:**
```
Type:       Machine learning model (recommendation)
Features:   - Build item-item similarity from products bought together in the same orders
            - Combine with text similarity of product titles and descriptions
            - Return the top 8 similar products for a product id
            - Exclude out-of-stock items from recommendations
            - Recompute similarities nightly
API:        REST
            GET /products/{id}/similar
Storage:    Redis (precomputed recommendations)
Tech stack: Python, pandas, scikit-learn (TF-IDF, cosine similarity), FastAPI, Redis
```

---

## Example 16

**Intent:**
script that pulls stock prices and calculates moving averages

**Spec:**
```
Type:       Data analysis script (finance)
Features:   - Download daily closing prices for a list of tickers
            - Calculate 50-day and 200-day moving averages
            - Detect golden cross and death cross events
            - Plot price with moving averages for each ticker
            - Save signals to a CSV file
Input:      List of ticker symbols and a date range
Storage:    Local CSV files
Tech stack: Python, yfinance, pandas, matplotlib
```

---

## Example 17

**Intent:**
need a pipeline that moves our app events from kafka into snowflake every few min

**Spec:**
```
Type:       Data pipeline (streaming ingestion)
Features:   - Consume app event messages from a Kafka topic
            - Validate each event against a JSON schema
            - Batch events into micro-batches every 5 minutes
            - Load batches into a Snowflake raw events table
            - Send invalid events to a dead-letter topic
            - Expose consumer lag metrics for monitoring
Storage:    Snowflake, Kafka (dead-letter topic)
Tech stack: Kafka Connect, Snowflake Kafka Connector, Python, Prometheus
```

---

## Example 18

**Intent:**
Je voudrais a model what can say which language a text is written

**Spec:**
```
Type:       Machine learning model (language identification)
Features:   - Collect a labelled text dataset covering the target languages
            - Extract character n-gram features from each text
            - Train a multinomial Naive Bayes classifier
            - Evaluate accuracy per language on a test set
            - Return the predicted language and probability for a new text
Input:      Short text string
Storage:    Local file (pickled model)
Tech stack: Python, scikit-learn
```

---

## Example 19

**Intent:**
count the cars in photos from our parking lot camera

**Spec:**
```
Type:       Machine learning model (object detection)
Features:   - Capture a frame from the parking lot camera every 5 minutes
            - Detect cars in the frame with a pretrained YOLO model
            - Count detected cars and compare with the total number of spaces
            - Store occupancy counts with timestamps
            - Show an occupancy-by-hour chart for the last week
Storage:    SQLite (occupancy counts)
Tech stack: Python, Ultralytics YOLOv8, OpenCV, matplotlib
```

---

## Example 20

**Intent:**
Our marketing team wants a weekly email with last week's ad performance across Google Ads and Facebook so they stop logging into both every Monday.

**Spec:**
```
Type:       Scheduled script (reporting)
Features:   - Fetch last week's spend, clicks, impressions and conversions from Google Ads and Meta Ads APIs
            - Combine both sources into one table per campaign
            - Calculate CTR, CPC and cost per conversion
            - Compare each metric with the previous week
            - Send an HTML email summary with a table to the marketing list every Monday at 8:00
Storage:    Google Sheets (weekly history)
Tech stack: Python, google-ads, facebook-business SDK, pandas, SendGrid, cron
```

---

## Example 21

**Intent:**
what the best way to see which of our products get returned most and why

**Spec:**
```
Type:       Data analysis script (returns analysis)
Features:   - Join returns data with orders and product data
            - Calculate return rate per product and category
            - Group free-text return reasons into themes with keyword matching
            - Rank products with the highest return rate and minimum order volume
            - Plot the main return reasons per category
Input:      Orders CSV and returns CSV with reason text
Tech stack: Python, pandas, seaborn, Jupyter
```

---

## Example 22

**Intent:**
in R pls - i have blood pressure readings from a clinical trial, two groups, want to know if the drug worked

**Spec:**
```
Type:       Data analysis script (clinical statistics)
Features:   - Load patient readings for treatment and placebo groups
            - Check normality of the change in blood pressure with Shapiro-Wilk tests
            - Compare groups with a t-test or Wilcoxon test as appropriate
            - Fit a mixed-effects model for repeated measurements over visits
            - Report effect size and 95% confidence intervals
            - Plot mean blood pressure per visit by group
Input:      CSV with patient_id, group, visit, systolic, diastolic
Tech stack: R, tidyverse, lme4, ggplot2, R Markdown
```

---

## Example 23

**Intent:**
tool that summarizes long customer reviews

**Spec:**
```
Type:       Web application (LLM summarisation)
Features:   - Paste or upload a CSV of customer reviews
            - Summarise reviews into main positives and negatives with an LLM
            - Group reviews by product before summarising
            - Show how many reviews mention each theme
            - Export summaries to a CSV
Input:      CSV of reviews (product, rating, text)
Tech stack: Python, Streamlit, OpenAI API, pandas
```

---

## Example 24

**Intent:**
i work for a city council and we have bike counters at 12 places in town that log every passing bike. i'm not a programmer really but i know a bit of python. my boss wants to know if the new bike lanes changed anything and he wants nice graphs

**Spec:**
```
Type:       Data analysis script (before/after study)
Features:   - Load hourly counts from all 12 counters
            - Clean gaps and obvious counter faults
            - Compare average daily counts before and after the bike lane opening date
            - Adjust for weather and season by comparing the same months year over year
            - Plot daily counts per counter with the opening date marked
            - Export charts and a summary table for the report
Input:      Counter export CSVs (counter_id, timestamp, count)
Tech stack: Python, pandas, matplotlib, Jupyter Notebook
```

---

## Example 25

**Intent:**
Tableau dashboard showing our hotel occupancy and average room rate

**Spec:**
```
Type:       Data dashboard (hospitality)
Features:   - Show occupancy rate, ADR and RevPAR per day and month
            - Compare each month with the same month last year
            - Break down bookings by channel and room type
            - Show booking lead time distribution
            - Filter by hotel property and date range
Input:      Booking export from the property management system
Tech stack: Tableau Desktop, Tableau Server
```

---

## Example 26

**Intent:**
detect defects on circuit boards from camera images

**Spec:**
```
Type:       Machine learning model (image classification)
Features:   - Load images of good and defective boards labelled by defect type
            - Augment images with rotation, brightness and noise changes
            - Fine-tune a pretrained EfficientNet on the defect classes
            - Report recall for each defect class and the confusion matrix
            - Run inference on new images and flag defective boards
            - Save flagged images with the predicted defect type
Input:      Labelled board images (one folder per class)
Storage:    Local files (model and flagged images)
Tech stack: Python, PyTorch, timm, OpenCV
```

---

## Example 27

**Intent:**
cluster my customers into groups

**Spec:**
```
Type:       Machine learning model (clustering)
Features:   - Build features per customer such as spend, order count, average basket and category mix
            - Scale the features with standardisation
            - Choose the number of clusters with the elbow method and silhouette score
            - Group customers with K-means
            - Describe each segment with its average feature values
            - Save each customer's segment label to CSV
Input:      Customer orders CSV
Tech stack: Python, pandas, scikit-learn, seaborn
```

---

## Example 28

**Intent:**
website where students upload essays and an ai gives feedback on structure and grammar

**Spec:**
```
Type:       Web application (LLM feedback)
Auth:       Student and teacher login (email + password)
Data model: User(id, email, password_hash, role)
            Essay(id, student_id -> User, title, text, submitted_at)
            Feedback(id, essay_id -> Essay, structure_notes, grammar_notes, score)
Features:   - Upload an essay as text or a .docx file
            - Generate feedback on structure, argument and grammar with an LLM
            - Highlight grammar issues in the essay text
            - Let teachers view and edit feedback before releasing it
            - Track scores across a student's essays
API:        REST
            POST /essays
            GET /essays/{id}/feedback
            PUT /feedback/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, OpenAI API, python-docx
```

---

## Example 29

**Intent:**
monitor our server logs and alert when something weird happens

**Spec:**
```
Type:       Machine learning model (log anomaly detection)
Features:   - Parse server logs into structured fields and log templates
            - Count log template frequencies in 5-minute windows
            - Train an Isolation Forest on normal periods
            - Score each new window and flag anomalies
            - Send an alert to Slack with the unusual log lines
Input:      Application log files
Storage:    Elasticsearch
Tech stack: Python, Drain3 (log parsing), scikit-learn, Slack webhook
```

---

## Example 30

**Intent:**
Could you set up a daily pipeline that grabs exchange rates from the European Central Bank and stores them so our finance reports can use them?

**Spec:**
```
Type:       Data pipeline (ETL)
Features:   - Download the daily euro reference rates XML from the ECB
            - Parse the currency codes and rates
            - Skip weekends and holidays when no rates are published
            - Insert new rates into a database table without duplicates
            - Backfill missing days on the first run
Storage:    PostgreSQL
Tech stack: Python, requests, lxml, Apache Airflow
```

---

## Example 31

**Intent:**
predict house rent in my city from the size, rooms and location

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Clean listing data and remove duplicates and outliers
            - Encode location with neighbourhood one-hot features and distance to the city centre
            - Split into train and test sets
            - Train a random forest regressor and compare with linear regression
            - Report mean absolute error and R² on the test set
            - Predict the rent for a new apartment
Input:      Rental listings CSV (size_m2, rooms, floor, neighbourhood, lat, lon, rent)
Tech stack: Python, pandas, scikit-learn
```

---

## Example 32

**Intent:**
football player stats dashboard

**Spec:**
```
Type:       Data dashboard (sports analytics)
Features:   - Load per-match player stats (goals, assists, xG, passes, minutes)
            - Show a player profile with per-90-minute stats
            - Compare two players on a radar chart
            - Rank players by any stat with a minimum minutes filter
            - Filter by league, season and position
Input:      Player match statistics CSV
Tech stack: Python, Plotly Dash, pandas
```

---

## Example 33

**Intent:**
Make customer support chatbot for our internet provider website, it must answer from our FAQ and when it can't, it create a ticket.

**Spec:**
```
Type:       Chatbot (customer support)
Data model: Conversation(id, customer_email, started_at, resolved)
            Ticket(id, conversation_id -> Conversation, summary, status, created_at)
Features:   - Answer customer questions using retrieval over the FAQ articles
            - Keep conversation context across messages
            - Detect when the answer confidence is low or the customer asks for a human
            - Create a support ticket with a summary of the conversation
            - Show the ticket number to the customer
API:        REST
            POST /chat
            POST /tickets
Storage:    PostgreSQL, pgvector (FAQ embeddings)
Tech stack: Python, FastAPI, OpenAI API, pgvector, JavaScript chat widget
```

---

## Example 34

**Intent:**
jupyter notebook to explore the titanic data

**Spec:**
```
Type:       Data analysis script (exploratory)
Features:   - Load the Titanic passenger dataset
            - Show missing values and basic statistics per column
            - Plot survival rate by sex, class and age group
            - Show correlations between numeric features
            - Fill missing ages with the median by passenger class
Input:      Titanic CSV (train.csv)
Tech stack: Python, Jupyter Notebook, pandas, seaborn
```

---

## Example 35

**Intent:**
transcribe our meeting recordings and summarize them

**Spec:**
```
Type:       Command-line tool (speech-to-text and summarisation)
Features:   - Transcribe audio files with a speech recognition model
            - Label speakers in the transcript
            - Summarise the meeting into key points, decisions and action items with an LLM
            - Save the transcript and summary as Markdown files
            - Process all recordings in a folder in one run
Input:      Folder of meeting audio files (.mp3, .m4a, .wav)
Storage:    Local Markdown files
Tech stack: Python, OpenAI Whisper, pyannote.audio, Anthropic Claude API
```

---

## Example 36

**Intent:**
ok so my dad has a small farm with 3 greenhouses and he has these cheap sensors logging temp and humidity to sd cards. he copies the files to his laptop every week. he wants to see graphs and know when it was too cold at night. hes not techy at all

**Spec:**
```
Type:       Data analysis script (sensor report)
Features:   - Read all sensor log files from a chosen folder
            - Merge readings from the three greenhouses into one table
            - Plot temperature and humidity per greenhouse for the past week
            - List nights when temperature dropped below a set minimum
            - Save the charts and the cold-night list as a PDF report
Input:      Folder of sensor log CSV files from the SD cards
Storage:    Local PDF report
Tech stack: Python, pandas, matplotlib, PyInstaller (one-click executable)
```

---

## Example 37

**Intent:**
real time dashboard of orders coming in for our restaurant chain

**Spec:**
```
Type:       Data dashboard (real-time)
Features:   - Stream new orders from the POS database
            - Show orders per minute and revenue today per restaurant
            - Show a live map of restaurants colored by order volume
            - Show average preparation time per restaurant
            - Highlight restaurants with no orders in the last 30 minutes
Storage:    PostgreSQL (orders), Redis (live counters)
Tech stack: Grafana, PostgreSQL, Redis, Python (stream consumer)
```

---

## Example 38

**Intent:**
build me an image search where i type words and find matching photos in my collection

**Spec:**
```
Type:       Machine learning model (image search)
Features:   - Compute CLIP image embeddings for every photo in a folder
            - Store embeddings in a vector index
            - Encode a text query with the CLIP text encoder
            - Return the most similar photos by cosine similarity
            - Show results as a thumbnail grid
Input:      Folder of photos and a text query
Storage:    FAISS index on disk
Tech stack: Python, OpenCLIP, FAISS, Gradio
```

---

## Example 39

**Intent:**
Excel macro that makes a pivot of sales by region and month

**Spec:**
```
Type:       Plugin (Excel VBA macro)
Features:   - Read the sales data sheet into a pivot cache
            - Create a pivot table with regions as rows and months as columns
            - Sum revenue and count orders in the pivot
            - Add a pivot chart next to the table
            - Refresh the pivot with one button
Input:      Sales sheet with date, region, revenue columns
Tech stack: Excel, VBA
```

---

## Example 40

**Intent:**
estimate the age of trees from drone images

**Spec:**
```
Type:       Machine learning model (image regression)
Features:   - Tile drone orthophotos into crops around each tree
            - Match crops with field-measured tree ages
            - Fine-tune a pretrained ResNet with a regression output
            - Report mean absolute error in years on a test set of trees
            - Predict ages for new crops and export a map layer
Input:      Drone orthophotos (GeoTIFF) and field measurements CSV
Storage:    Local files (model, GeoJSON results)
Tech stack: Python, PyTorch, rasterio, GeoPandas
```

---

## Example 41

**Intent:**
crypto price dashboard

**Spec:**
```
Type:       Data dashboard (finance)
Features:   - Fetch current and historical prices from the CoinGecko API
            - Show price charts for selected coins with 1d, 7d, 30d and 1y ranges
            - Show 24h change and market cap in a table
            - Track a personal portfolio value from entered holdings
            - Refresh prices every minute
Storage:    Browser localStorage (portfolio holdings)
Tech stack: React, Recharts, CoinGecko API
```

---

## Example 42

**Intent:**
we have 10 years of retail sales by store and I need to forecast for budget planning next year, our team works in databricks

**Spec:**
```
Type:       Machine learning model (forecasting)
Features:   - Aggregate sales into weekly totals per store
            - Train one forecasting model per store in parallel
            - Include holidays and promotions as external regressors
            - Backtest each model on the last 52 weeks and report MAPE
            - Forecast weekly sales for the next 52 weeks per store
            - Write forecasts to a Delta table for the budget team
Input:      Sales Delta table (store_id, date, sales, promo_flag)
Storage:    Delta Lake tables
Tech stack: Databricks, PySpark, Prophet, MLflow
```

---

## Example 43

**Intent:**
chat with my own notes

**Spec:**
```
Type:       Chatbot (personal knowledge RAG)
Features:   - Index all Markdown notes from a folder
            - Split notes into chunks and create embeddings locally
            - Answer questions with links to the source notes
            - Update the index when notes change
            - Run fully offline with a local LLM
Input:      Folder of Markdown notes
Storage:    Chroma (local vector database)
Tech stack: Python, LlamaIndex, Ollama, Chroma
```

---

## Example 44

**Intent:**
tell me if a mushroom photo is poisonous

**Spec:**
```
Type:       Machine learning model (image classification)
Features:   - Collect labelled mushroom images by species
            - Fine-tune a pretrained image model to recognise the species
            - Map each species to edible, poisonous or unknown
            - Show the top 3 species with confidence
            - Always show a safety warning not to eat mushrooms based on the app
Input:      Photo of a mushroom
Tech stack: Python, PyTorch, torchvision, Gradio
```

---

## Example 45

**Intent:**
weekly report of github repo activity for my open source project

**Spec:**
```
Type:       Scheduled script (reporting)
Features:   - Fetch issues, pull requests, stars and commits from the GitHub API for the past week
            - Count new and closed issues and merged pull requests
            - List new contributors
            - Calculate median time to first response on issues
            - Post the summary as a GitHub Discussion every Monday
Tech stack: Python, PyGithub, GitHub Actions (schedule)
```

---

## Example 46

**Intent:**
sql queries to find which marketing campaign brings customers that spend the most

**Spec:**
```
Type:       Data analysis script (SQL)
Features:   - Join customers with their first-touch campaign
            - Calculate total revenue per customer over the first 12 months
            - Aggregate average customer lifetime value per campaign
            - Rank campaigns by lifetime value and acquisition cost ratio
            - Save results as a view for reporting
Storage:    PostgreSQL (view)
Tech stack: SQL (PostgreSQL)
```

---

## Example 47

**Intent:**
i scraped 50k recipes and want to predict cooking time from ingredients and steps

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Parse ingredients and steps into text features
            - Extract numeric features such as number of ingredients and steps
            - Vectorise text with TF-IDF
            - Train a gradient boosting regressor on log cooking time
            - Report median absolute error in minutes on a test set
Input:      Recipes JSON (title, ingredients, steps, total_time)
Tech stack: Python, scikit-learn, LightGBM, pandas
```

---

## Example 48

**Intent:**
Hello, I am researcher in biology. I have many microscope images of cells and I need to count the cells in each image automatic, now we count by hand and it take weeks.

**Spec:**
```
Type:       Data analysis script (image analysis)
Features:   - Load microscope images in batch from a folder
            - Segment cells with a pretrained Cellpose model
            - Count cells and measure their area per image
            - Save an overlay image showing the detected cells
            - Export counts and areas per image to a CSV
Input:      Folder of microscope images (.tif)
Storage:    Local CSV and overlay images
Tech stack: Python, Cellpose, scikit-image, pandas
```

---

## Example 49

**Intent:**
model to tell if an email is spam

**Spec:**
```
Type:       Machine learning model (text classification)
Features:   - Load a labelled email dataset
            - Clean email bodies and extract TF-IDF features
            - Train a logistic regression classifier
            - Evaluate precision and recall on a test set
            - Predict spam probability for a new email
Input:      Email text
Tech stack: Python, scikit-learn, pandas
```

---

## Example 50

**Intent:**
Our sales reps forget to update the CRM, so I want an AI that listens to call recordings and fills in the deal notes and next steps automatically.

**Spec:**
```
Type:       Data pipeline (LLM extraction)
Features:   - Fetch new call recordings from the phone system
            - Transcribe calls with a speech-to-text model
            - Extract customer needs, objections, budget and next steps with an LLM into JSON
            - Match the call to the deal by phone number
            - Write the extracted notes to the deal in the CRM
Input:      Call recordings (audio files)
Storage:    HubSpot CRM
Tech stack: Python, OpenAI Whisper API, OpenAI API (structured output), HubSpot API
```

---

## Example 51

**Intent:**
covid case data per country visualize

**Spec:**
```
Type:       Data analysis script (visualisation)
Features:   - Download the Our World in Data COVID-19 dataset
            - Compute 7-day rolling average of new cases per million
            - Plot case curves for selected countries
            - Draw a world choropleth map for a chosen date
            - Save charts as PNG files
Tech stack: Python, pandas, Plotly
```

---

## Example 52

**Intent:**
scoring leads in our crm by how likely they become customers

**Spec:**
```
Type:       Machine learning model (lead scoring)
Features:   - Export historical leads with source, industry, company size and activity counts
            - Label leads that converted within 60 days
            - Train a logistic regression and a random forest and compare ROC AUC
            - Calibrate predicted probabilities
            - Write a lead score from 0 to 100 back to the CRM nightly
Storage:    Salesforce (lead score field)
Tech stack: Python, scikit-learn, simple-salesforce, Airflow
```

---

## Example 53

**Intent:**
grafana dashboards for our app metrics

**Spec:**
```
Type:       Data dashboard (monitoring)
Features:   - Collect request rate, error rate and latency from the app
            - Show p50, p95 and p99 latency per endpoint
            - Show error rate per service with thresholds
            - Add alerts when error rate stays above 2% for 5 minutes
            - Show CPU and memory usage per container
Storage:    Prometheus
Tech stack: Grafana, Prometheus, Prometheus client library
```

---

## Example 54

**Intent:**
predict student dropout risk at our university

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Combine grades, attendance, credits earned and enrolment data per student
            - Label students who dropped out within the next semester
            - Split train and test sets by academic year
            - Train a gradient boosting classifier and report recall and F1
            - Explain each risk score with the top contributing features
            - Export a list of at-risk students for advisers
Input:      Student records from the university database
Tech stack: Python, pandas, scikit-learn, SHAP
```

---

## Example 55

**Intent:**
speech to text for my podcast to make subtitles

**Spec:**
```
Type:       Command-line tool (transcription)
Features:   - Transcribe an audio or video file with Whisper
            - Split the transcript into subtitle lines with timings
            - Export SRT and VTT subtitle files
            - Support choosing the language and model size
Input:      Podcast audio or video file
Tech stack: Python, openai-whisper, ffmpeg
```

---

## Example 56

**Intent:**
summarize my company's google search console data every month in google sheets

**Spec:**
```
Type:       Scheduled script (reporting)
Features:   - Fetch clicks, impressions, CTR and position by query and page from the Search Console API
            - Aggregate the past month's totals
            - Compare with the previous month
            - Write results into a new monthly tab in a Google Sheet
            - Highlight queries with the biggest drops
Storage:    Google Sheets
Tech stack: Google Apps Script, Search Console API
```

---

## Example 57

**Intent:**
what type of flowers is this

**Spec:**
```
Type:       Machine learning model (image classification)
Features:   - Use the Oxford 102 Flowers dataset split into train, validation and test
            - Fine-tune a pretrained ResNet50 on the 102 classes
            - Report top-1 and top-5 accuracy
            - Predict the flower name for an uploaded photo
Input:      Flower photo
Tech stack: Python, PyTorch, torchvision, Gradio
```

---

## Example 58

**Intent:**
dbt project to clean up our raw stripe data into revenue tables

**Spec:**
```
Type:       Data pipeline (ELT transformations)
Features:   - Define staging models for Stripe charges, refunds, invoices and subscriptions
            - Convert amounts from cents and currencies to a base currency
            - Build a monthly recurring revenue model per customer
            - Calculate new, expansion, contraction and churned MRR
            - Add dbt tests for unique ids and not-null amounts
Storage:    Snowflake
Tech stack: dbt, SQL, Fivetran (Stripe connector)
```

---

## Example 59

**Intent:**
soo i got all my whatsapp chats exported and i wanna see stats like who texts more and at what time lol

**Spec:**
```
Type:       Data analysis script (chat statistics)
Features:   - Parse the exported WhatsApp chat text file into date, time, sender and message
            - Count messages and words per person
            - Plot messages by hour of day and by weekday
            - Find the most used words and emojis per person
            - Show average reply time between people
Input:      WhatsApp exported chat .txt file
Tech stack: Python, pandas, matplotlib, emoji
```

---

## Example 60

**Intent:**
churn dashboard in looker

**Spec:**
```
Type:       Data dashboard (customer churn)
Features:   - Define a LookML model for subscriptions and cancellations
            - Show monthly churn rate and retention by signup cohort
            - Break down churn by plan, country and acquisition channel
            - Show reasons given in cancellation surveys
            - Filter by date range and plan
Storage:    BigQuery
Tech stack: Looker, LookML, BigQuery
```

---

## Example 61

**Intent:**
machine learning to predict the price of used cars i saw on a website

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Clean scraped listings and remove duplicates and unrealistic prices
            - Encode brand, model, fuel type and gearbox as categorical features
            - Train a CatBoost regressor on log price
            - Report mean absolute percentage error on a test set
            - Predict a fair price for a new listing and flag underpriced ones
Input:      Used car listings CSV (brand, model, year, mileage, fuel, gearbox, price)
Tech stack: Python, pandas, CatBoost
```

---

## Example 62

**Intent:**
My wife runs a yoga studio with about 300 members and she keeps everything in Google Sheets: classes, attendance, payments. She asked me to make her something that shows which classes are popular, which members stopped coming, and how much money comes in each month.

**Spec:**
```
Type:       Data dashboard (small business)
Features:   - Read attendance and payment tabs from Google Sheets
            - Show attendance per class type and time slot
            - List members with no attendance in the last 30 days
            - Show monthly revenue by membership type
            - Refresh automatically every day
Input:      Google Sheets workbook (classes, attendance, payments)
Tech stack: Looker Studio, Google Sheets connector
```

---

## Example 63

**Intent:**
rag over our confluence wiki for engineers

**Spec:**
```
Type:       Chatbot (document Q&A)
Auth:       Single sign-on with the company Google Workspace account
Features:   - Export all Confluence pages through the Confluence API every night
            - Chunk pages by heading and store embeddings in a vector database
            - Answer questions with retrieved chunks and an LLM
            - Cite page titles and links in every answer
            - Respect space permissions so users only see pages they can access
Storage:    Qdrant (vector database)
Tech stack: Python, LlamaIndex, Qdrant, OpenAI API, Slack Bolt (chat interface)
```

---

## Example 64

**Intent:**
predict if a patient has diabetes from health measurements

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load the Pima Indians Diabetes dataset
            - Replace impossible zero values in glucose, blood pressure and BMI with the median
            - Split into stratified train and test sets
            - Train logistic regression, random forest and XGBoost with cross-validation
            - Compare models with ROC AUC and recall
            - Show feature importance for the best model
Input:      CSV with pregnancies, glucose, blood_pressure, bmi, age, outcome
Tech stack: Python, scikit-learn, XGBoost, Jupyter
```

---

## Example 65

**Intent:**
pls help me make sense of my electricity usage data from smart meter, its every 30 min

**Spec:**
```
Type:       Data analysis script (energy usage)
Features:   - Load half-hourly smart meter readings
            - Calculate daily, weekly and monthly consumption
            - Show an average daily load profile by hour
            - Compare weekdays with weekends
            - Estimate cost with a day and night tariff
            - Highlight days with unusually high usage
Input:      Smart meter CSV (timestamp, kWh)
Tech stack: Python, pandas, matplotlib, Jupyter
```

---

## Example 66

**Intent:**
an api that takes a product photo and returns tags like color and category

**Spec:**
```
Type:       REST API service (image tagging)
Features:   - Accept an image upload
            - Predict the product category with a fine-tuned image classifier
            - Extract the dominant colors with k-means on pixel values
            - Return tags with confidence scores as JSON
            - Reject files that are not images or larger than 10 MB
API:        REST
            POST /tag
Tech stack: Python, FastAPI, PyTorch, scikit-learn, Pillow
```

---

## Example 67

**Intent:**
i want to know which words appear most in trump vs biden speeches

**Spec:**
```
Type:       Data analysis script (text analysis)
Features:   - Load speech transcripts labelled by speaker
            - Tokenise text and remove stop words
            - Count word and bigram frequencies per speaker
            - Find the most distinctive words per speaker with log-odds ratio
            - Draw word clouds and bar charts of top words
Input:      Folder of speech transcripts as text files
Tech stack: Python, NLTK, pandas, wordcloud, matplotlib
```

---

## Example 68

**Intent:**
Using Airflow, I need an ETL job that copies yesterday's orders from our MySQL app database into BigQuery every night at 2am.

**Spec:**
```
Type:       Data pipeline (ETL)
Features:   - Extract orders updated in the previous day from MySQL
            - Convert data types and timestamps to UTC
            - Load the data into a BigQuery staging table
            - Merge staging rows into the orders table with upserts
            - Retry failed tasks three times and email on failure
Storage:    BigQuery
Tech stack: Apache Airflow, Python, MySQL, Google Cloud BigQuery
```

---

## Example 69

**Intent:**
recommendation of books for our library users

**Spec:**
```
Type:       Machine learning model (recommendation)
Features:   - Build a user-book matrix from loan history
            - Train an implicit feedback matrix factorisation model with ALS
            - Recommend 10 books per user that they have not borrowed
            - Fall back to popular books in favourite genres for new users
            - Evaluate with precision@10 on held-out loans
Input:      Loan history (user_id, book_id, loan_date)
Storage:    PostgreSQL (recommendations table)
Tech stack: Python, implicit, pandas, SciPy
```

---

## Example 70

**Intent:**
we get thousands of contracts and need to pull out the dates, parties and amounts

**Spec:**
```
Type:       Data pipeline (document extraction)
Features:   - Extract text from PDF contracts with OCR for scanned pages
            - Ask an LLM to return parties, start date, end date, amounts and renewal terms as JSON
            - Validate extracted dates and amounts
            - Save extracted fields to a database table per contract
            - Flag contracts with missing fields for manual review
Input:      Folder of contract PDFs
Storage:    PostgreSQL
Tech stack: Python, Tesseract OCR, pdfplumber, Anthropic Claude API, Pydantic
```

---

## Example 71

**Intent:**
tennis match predictor

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load historical ATP match results with player rankings and surfaces
            - Compute Elo ratings per player overall and per surface
            - Build features from Elo difference, head-to-head and recent form
            - Train a logistic regression to predict the winner
            - Evaluate log loss and accuracy on the last season
Input:      ATP match results CSVs
Tech stack: Python, pandas, scikit-learn
```

---

## Example 72

**Intent:**
website visitor heatmap analysis from clicks

**Spec:**
```
Type:       Data analysis script (web analytics)
Features:   - Load click events with page URL, x and y coordinates and screen width
            - Normalise coordinates to the page width
            - Create a click density heatmap per page
            - Overlay the heatmap on a page screenshot
            - Compare click heatmaps for mobile and desktop
Input:      Click events CSV and page screenshots
Tech stack: Python, pandas, NumPy, matplotlib, Pillow
```

---

## Example 73

**Intent:**
i got a kaggle competition about predicting house prices, help me set up a good pipeline

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Load train and test CSVs and check missing values
            - Impute missing values and encode categorical features in a scikit-learn pipeline
            - Log-transform the sale price target
            - Train ridge regression, LightGBM and XGBoost with 5-fold cross-validation
            - Blend the best models and write a submission CSV
Input:      Kaggle train.csv and test.csv
Tech stack: Python, pandas, scikit-learn, LightGBM, XGBoost
```

---

## Example 74

**Intent:**
make a dashboard in excel for my small company finances

**Spec:**
```
Type:       Data dashboard (Excel)
Features:   - Import monthly income and expense transactions into a table
            - Summarise revenue, costs and profit per month with pivot tables
            - Show a profit trend line chart and an expense breakdown pie chart
            - Compare actuals with the yearly budget
            - Add slicers for month and category
Input:      Transactions sheet (date, category, amount, type)
Tech stack: Microsoft Excel (pivot tables, charts, slicers)
```

---

## Example 75

**Intent:**
i want to see what stuff my customers buy together

**Spec:**
```
Type:       Data analysis script (market basket analysis)
Features:   - Load order lines and group them into baskets per order
            - Find frequent itemsets with the Apriori algorithm
            - Generate association rules with support, confidence and lift
            - Filter rules by minimum support and lift
            - Export the top rules to a CSV
Input:      Order lines CSV (order_id, product_name)
Tech stack: Python, pandas, mlxtend
```

---

## Example 76

**Intent:**
our hospital wants a model to read chest x-rays and flag possible pneumonia for the radiologist to look first

**Spec:**
```
Type:       Machine learning model (medical image classification)
Features:   - Load labelled chest X-ray images and split train, validation and test sets by patient
            - Fine-tune a pretrained DenseNet121
            - Handle class imbalance with weighted loss
            - Report sensitivity, specificity and ROC AUC
            - Show Grad-CAM heatmaps of the regions that drove the prediction
            - Sort the radiologist worklist by predicted probability
Input:      Chest X-ray images (DICOM)
Tech stack: Python, PyTorch, MONAI, pydicom
```

---

## Example 77

**Intent:**
Every week I download the same 6 reports from different systems and merge them in Excel by hand to make one KPI sheet for the director, it takes my whole Monday morning and I make mistakes.

**Spec:**
```
Type:       Scheduled script (report automation)
Features:   - Read the six weekly report files from a shared folder
            - Clean column names and join the reports on week and department
            - Calculate the KPI figures used in the director's sheet
            - Write the KPI sheet into an Excel template with formatting
            - Email the finished file to the director every Monday at 9:00
            - Log errors when a source file is missing
Input:      Six weekly report exports (Excel/CSV)
Storage:    Shared network folder
Tech stack: Python, pandas, openpyxl, Windows Task Scheduler
```

---

## Example 78

**Intent:**
bot that posts daily covid stats to our discord

**Spec:**
```
Type:       Bot (Discord)
Features:   - Fetch the latest case numbers from a public API every morning
            - Compare with the previous day
            - Format a message with numbers and arrows for up and down
            - Post the message to a set channel
            - Answer a !stats command for a given country
Tech stack: Python, discord.py, requests, APScheduler
```

---

## Example 79

**Intent:**
Analise of the questionnaire we gave to 400 nurses about burnout, we use SPSS normaly but want try python

**Spec:**
```
Type:       Data analysis script (survey statistics)
Features:   - Load the SPSS .sav file with variable labels
            - Calculate burnout scale scores from the item responses
            - Check reliability of each scale with Cronbach's alpha
            - Compare scores between wards with ANOVA
            - Run a regression of burnout on working hours and experience
            - Save tables and charts for the report
Input:      SPSS .sav survey file
Tech stack: Python, pyreadstat, pandas, pingouin, statsmodels, seaborn
```

---

## Example 80

**Intent:**
predict energy consumption of our building next day

**Spec:**
```
Type:       Machine learning model (forecasting)
Features:   - Combine hourly meter readings with weather data and occupancy schedules
            - Create lag features and hour, weekday and holiday features
            - Train a LightGBM model on past data with time-based validation
            - Forecast hourly consumption for the next 24 hours
            - Compare forecast with actuals each day and log the error
Input:      Hourly energy meter data, weather forecast API
Storage:    InfluxDB
Tech stack: Python, LightGBM, pandas, InfluxDB client
```

---

## Example 81

**Intent:**
tiny script to find duplicate rows in a csv

**Spec:**
```
Type:       Command-line script (data cleaning)
Features:   - Read a CSV file
            - Find exact duplicate rows
            - Find duplicates on chosen key columns
            - Print the number of duplicates and examples
            - Save a deduplicated copy of the file
Input:      CSV file path and optional key column names
Tech stack: Python, pandas, argparse
```

---

## Example 82

**Intent:**
chatbot for hotel guests to ask about breakfast time, wifi and stuff, in many languages

**Spec:**
```
Type:       Chatbot (hospitality FAQ)
Data model: HotelInfo(id, topic, content, updated_at)
            ChatLog(id, language, question, answer, handed_over, created_at)
Features:   - Answer questions from a hotel information document
            - Detect the guest's language and reply in the same language
            - Hand over to reception staff when the question needs a person
            - Let staff update the hotel information without code
            - Log unanswered questions for the staff
Storage:    SQLite
Tech stack: Python, FastAPI, OpenAI API, WhatsApp Business API
```

---

## Example 83

**Intent:**
anomaly detection on factory machine vibration

**Spec:**
```
Type:       Machine learning model (anomaly detection)
Features:   - Read vibration signals from accelerometers at a fixed sample rate
            - Extract features such as RMS, kurtosis and FFT band energies per window
            - Train an autoencoder on data from healthy machines
            - Flag windows with high reconstruction error as anomalies
            - Send an alert with the machine id and time
Input:      Accelerometer data streams
Storage:    InfluxDB
Tech stack: Python, TensorFlow/Keras, SciPy, MQTT
```

---

## Example 84

**Intent:**
analyse NBA shot data and make shot charts

**Spec:**
```
Type:       Data analysis script (sports analytics)
Features:   - Download shot location data for a player and season from the NBA stats API
            - Draw shots on a half-court diagram colored by made or missed
            - Calculate field goal percentage by court zone
            - Compare a player's zone percentages with the league average
            - Save shot charts as PNG
Tech stack: Python, nba_api, pandas, matplotlib
```

---

## Example 85

**Intent:**
knime workflow for cleaning customer address data

**Spec:**
```
Type:       Data pipeline (data cleaning)
Features:   - Read customer records from an Excel file
            - Standardise street names, postal codes and capitalisation
            - Validate postal codes against a reference list
            - Find likely duplicate customers with fuzzy string matching
            - Write clean records and a list of problems to separate files
Input:      Customer Excel file
Tech stack: KNIME Analytics Platform
```

---

## Example 86

**Intent:**
we are a small NGO and we did a household survey in 5 villages with KoboToolbox, about water access. I need to make charts for the donor report but I only know a little Excel

**Spec:**
```
Type:       Data analysis script (survey report)
Features:   - Download the survey responses from the KoboToolbox API
            - Clean responses and translate choice codes into labels
            - Calculate access indicators per village (distance to water, liters per person)
            - Create bar charts per indicator and village
            - Export tables and charts into a Word document for the donor report
Input:      KoboToolbox form responses
Tech stack: Python, pandas, matplotlib, python-docx, KoboToolbox API
```

---

## Example 87

**Intent:**
classify news articles into topics

**Spec:**
```
Type:       Machine learning model (text classification)
Features:   - Load news articles labelled with topics such as politics, sports, business and tech
            - Create sentence embeddings for each article
            - Train a logistic regression classifier on the embeddings
            - Evaluate macro F1 on a test set
            - Predict the topic of new articles
Input:      Article text
Tech stack: Python, sentence-transformers, scikit-learn
```

---

## Example 88

**Intent:**
Our sales team wants an AI assistant that writes the first draft of proposals using our past winning proposals as examples.

**Spec:**
```
Type:       Web application (LLM document generation)
Auth:       Company Microsoft 365 login (single sign-on)
Features:   - Index past winning proposals in a vector database
            - Enter client name, industry and requirements in a form
            - Retrieve the most similar past proposals as examples
            - Generate a proposal draft section by section with an LLM
            - Export the draft as a Word document
Storage:    Azure AI Search (vector index), Azure Blob Storage
Tech stack: Python, Azure OpenAI, Azure AI Search, Streamlit, python-docx
```

---

## Example 89

**Intent:**
someting that cleans messy dates in excel files, people write them all different ways

**Spec:**
```
Type:       Command-line script (data cleaning)
Features:   - Read an Excel file and a chosen date column
            - Parse many date formats (dd/mm/yyyy, mm-dd-yy, written months)
            - Ask whether ambiguous dates are day-first or month-first
            - Write the cleaned dates in ISO format to a new column
            - List rows that could not be parsed
Input:      Excel file and the date column name
Tech stack: Python, pandas, python-dateutil, openpyxl
```

---

## Example 90

**Intent:**
dashboard showing our support team performance from zendesk

**Spec:**
```
Type:       Data dashboard (support analytics)
Features:   - Import tickets with created, solved and first response times from Zendesk
            - Show tickets created and solved per day
            - Show median first response and resolution time per agent
            - Show customer satisfaction scores over time
            - Filter by channel, priority and team
Storage:    PostgreSQL (synced tickets)
Tech stack: Metabase, PostgreSQL, Python (Zendesk API sync)
```

---

## Example 91

**Intent:**
deep learning model that generates captions for images

**Spec:**
```
Type:       Machine learning model (image captioning)
Features:   - Load the COCO captions dataset
            - Encode images with a pretrained vision encoder
            - Train a transformer decoder to generate captions
            - Evaluate with BLEU and CIDEr scores
            - Generate a caption for a new image with beam search
Input:      Image file
Tech stack: Python, PyTorch, Hugging Face Transformers
```

---

## Example 92

**Intent:**
monthly finance report pdf from our accounting export

**Spec:**
```
Type:       Scheduled script (finance reporting)
Features:   - Load the general ledger export from the accounting system
            - Build an income statement and balance summary for the month
            - Compare each line with budget and last year
            - Plot revenue and cost trends
            - Generate a formatted PDF report
Input:      General ledger CSV, budget Excel file
Storage:    Local PDF files
Tech stack: Python, pandas, matplotlib, WeasyPrint
```

---

## Example 93

**Intent:**
help i need to predict how many people will show up for our events, we have data from 200 past events

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Use features such as RSVP count, event type, weekday, weather and ticket price
            - Split past events into train and test sets
            - Train a random forest regressor and compare with an RSVP ratio baseline
            - Report mean absolute error in attendees
            - Predict attendance for an upcoming event
Input:      Past events spreadsheet
Tech stack: Python, pandas, scikit-learn
```

---

## Example 94

**Intent:**
write me a script that checks our web shop prices every day vs competitors and makes a graph

**Spec:**
```
Type:       Scheduled script (price monitoring)
Features:   - Scrape competitor prices for a list of product URLs each day
            - Store prices with dates
            - Calculate the price difference to our price per product
            - Plot price history per product
            - Send a summary when a competitor becomes cheaper
Input:      CSV of products with our price and competitor URLs
Storage:    SQLite
Tech stack: Python, requests, BeautifulSoup, pandas, matplotlib, cron
```

---

## Example 95

**Intent:**
Wie kann ich mit Python die Wetterdaten von DWD analysieren? Ich will Trends der Temperatur von 50 Jahren sehen

**Spec:**
```
Type:       Data analysis script (climate data)
Features:   - Download daily temperature data for a station from the DWD open data server
            - Calculate yearly mean temperatures
            - Fit a linear trend and report warming per decade
            - Plot yearly means with a 10-year rolling average
            - Count hot days above 30 °C per year
Input:      DWD station id
Tech stack: Python, pandas, wetterdienst, matplotlib
```

---

## Example 96

**Intent:**
An LLM tool that reads customer complaints and categorizes them plus pulls out the product name.

**Spec:**
```
Type:       Data pipeline (LLM classification)
Features:   - Read new complaints from the support inbox export
            - Send each complaint to an LLM with a fixed category list
            - Extract the product name and severity as structured JSON
            - Validate the output against a schema and retry on errors
            - Write results to a table for reporting
Input:      Complaints CSV or email export
Storage:    PostgreSQL
Tech stack: Python, OpenAI API (structured outputs), Pydantic, pandas
```

---

## Example 97

**Intent:**
retention cohort chart for our mobile app

**Spec:**
```
Type:       Data analysis script (cohort analysis)
Features:   - Load user signups and daily activity events
            - Assign each user to a weekly signup cohort
            - Calculate the share of each cohort active in week 1 to week 12
            - Draw a cohort retention heatmap
            - Compare retention of iOS and Android users
Input:      Events export (user_id, event_date, signup_date, platform)
Tech stack: Python, pandas, seaborn
```

---

## Example 98

**Intent:**
what's driving our employee satisfaction scores

**Spec:**
```
Type:       Data analysis script (driver analysis)
Features:   - Load engagement survey item scores and overall satisfaction
            - Calculate correlation of each item with satisfaction
            - Fit a regression with relative importance analysis
            - Plot items by importance and average score in a priority matrix
            - Break results down by department
Input:      Survey results CSV
Tech stack: Python, pandas, statsmodels, matplotlib
```

---

## Example 99

**Intent:**
detect faces in videos and blur them for privacy

**Spec:**
```
Type:       Command-line tool (video processing)
Features:   - Read a video frame by frame
            - Detect faces in each frame with a face detection model
            - Track faces between frames to avoid flicker
            - Apply Gaussian blur to face regions
            - Write the blurred video with the original audio
Input:      Video file
Tech stack: Python, OpenCV, MediaPipe, ffmpeg
```

---

## Example 100

**Intent:**
dashbord for my etsy shop sales pls

**Spec:**
```
Type:       Data dashboard (e-commerce)
Features:   - Import Etsy order CSV exports
            - Show revenue, orders and average order value per month
            - Show top selling listings
            - Show sales by country on a map
            - Show fees and net profit per month
Input:      Etsy orders and listings CSV exports
Tech stack: Python, Streamlit, pandas, Plotly
```

---

## Example 101

**Intent:**
predict delivery delays for our trucks

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Combine past trips with route distance, departure time, driver, weather and traffic data
            - Label trips that arrived more than 30 minutes late
            - Train a gradient boosting classifier
            - Report recall and precision for late trips
            - Score planned trips each morning and list those at risk
Input:      Trip history from the transport management system
Storage:    PostgreSQL
Tech stack: Python, pandas, LightGBM
```

---

## Example 102

**Intent:**
I'd like to fine-tune a small open source LLM on our company's support answers so it writes in our tone.

**Spec:**
```
Type:       Machine learning model (LLM fine-tuning)
Features:   - Export resolved support tickets as question and answer pairs
            - Remove personal data from the text
            - Fine-tune a small open LLM with LoRA adapters
            - Evaluate replies against a held-out set with human ratings
            - Serve the fine-tuned model behind an API for agents
Input:      Support ticket export
API:        REST
            POST /generate-reply
Tech stack: Python, Hugging Face Transformers, PEFT (LoRA), vLLM
```

---

## Example 103

**Intent:**
scrape and analyse job postings salaries by city

**Spec:**
```
Type:       Data analysis script (labour market)
Features:   - Load scraped job postings with title, city and salary text
            - Parse salary ranges into yearly numbers
            - Normalise job titles into role groups
            - Calculate median salary per role and city
            - Plot salary distributions per city
Input:      Job postings CSV
Tech stack: Python, pandas, regex, seaborn
```

---

## Example 104

**Intent:**
hey i'm a game dev and want to analyze how players move through levels in my game, where they die and quit

**Spec:**
```
Type:       Data analysis script (game analytics)
Features:   - Load gameplay events (level start, death, quit, completion) with positions
            - Calculate completion and quit rates per level as a funnel
            - Draw heatmaps of death positions on each level map
            - Find the levels with the largest player drop-off
            - Compare average attempts per level
Input:      Game telemetry events JSON
Tech stack: Python, pandas, matplotlib, Jupyter
```

---

## Example 105

**Intent:**
data warehouse for our small company

**Spec:**
```
Type:       Infrastructure setup (data warehouse)
Features:   - Set up a cloud data warehouse with raw, staging and mart schemas
            - Sync data from the CRM, accounting and web shop with managed connectors
            - Model fact and dimension tables in a star schema
            - Schedule transformations every night
            - Connect a BI tool for dashboards
Storage:    BigQuery
Tech stack: BigQuery, Airbyte, dbt, Metabase
```

---

## Example 106

**Intent:**
Can a model guess what grade an essay would get? I have 3000 graded essays from past years.

**Spec:**
```
Type:       Machine learning model (automated essay scoring)
Features:   - Load essays with their teacher grades
            - Fine-tune a pretrained DeBERTa model as a regressor on the grade
            - Use 5-fold cross-validation to estimate performance
            - Report quadratic weighted kappa against teacher grades
            - Predict a grade for a new essay with a confidence range
Input:      Essays CSV (text, grade)
Tech stack: Python, Hugging Face Transformers, PyTorch
```

---

## Example 107

**Intent:**
Matlab script to analyse EEG recordings

**Spec:**
```
Type:       Data analysis script (neuroscience)
Features:   - Load EEG recordings and channel locations
            - Filter signals with a band-pass filter and remove line noise
            - Remove eye-blink artifacts with ICA
            - Calculate power in delta, theta, alpha and beta bands per channel
            - Plot topographic maps of band power
Input:      EEG files (.edf)
Tech stack: MATLAB, EEGLAB
```

---

## Example 108

**Intent:**
voice assistant that answers questions about our product manual

**Spec:**
```
Type:       Chatbot (voice, document Q&A)
Features:   - Record the user's spoken question
            - Convert speech to text
            - Retrieve relevant manual sections with embeddings
            - Generate a short answer with an LLM
            - Read the answer aloud with text-to-speech
Input:      Product manual PDF
Storage:    FAISS index
Tech stack: Python, Whisper, LangChain, FAISS, OpenAI API, ElevenLabs API
```

---

## Example 109

**Intent:**
predict next month inventory needs

**Spec:**
```
Type:       Machine learning model (demand forecasting)
Features:   - Aggregate past sales into monthly units per SKU
            - Forecast next month demand per SKU with exponential smoothing
            - Add safety stock based on forecast error and lead time
            - Compare forecast demand with current stock to suggest order quantities
            - Export the reorder list to Excel
Input:      Sales history and current stock CSVs
Tech stack: Python, pandas, statsmodels, openpyxl
```

---

## Example 110

**Intent:**
u know those apps that tell u what song is playing, can i make one for bird sounds

**Spec:**
```
Type:       Machine learning model (audio classification)
Features:   - Load labelled bird call recordings by species
            - Convert audio clips into mel spectrograms
            - Fine-tune a pretrained audio CNN on the spectrograms
            - Report top-1 and top-5 accuracy per species
            - Predict the species for a new recording with confidence
Input:      Audio recording (.wav or .mp3)
Tech stack: Python, PyTorch, torchaudio, librosa
```

---

## Example 111

**Intent:**
dashboard for teachers to see student quiz results by topic

**Spec:**
```
Type:       Data dashboard (education)
Auth:       Teacher login with school Google account
Features:   - Import quiz results from the learning platform export
            - Show average score per topic and per class
            - Highlight students below 50% on any topic
            - Show score trend over the term
            - Filter by class, quiz and date
Storage:    PostgreSQL
Tech stack: Python, Streamlit, pandas, Plotly, Google OAuth
```

---

## Example 112

**Intent:**
summarize daily news on a topic and send it to me

**Spec:**
```
Type:       Scheduled script (LLM news digest)
Features:   - Fetch new articles from a list of RSS feeds every morning
            - Filter articles matching chosen keywords
            - Remove near-duplicate articles about the same story
            - Summarise each story in 3 sentences with an LLM
            - Email the digest with links to the originals
Input:      List of RSS feeds and keywords
Storage:    SQLite (seen articles)
Tech stack: Python, feedparser, Anthropic Claude API, smtplib, cron
```

---

## Example 113

**Intent:**
An SQL + Python job to calculate our customer lifetime value by month of acquisition and channel.

**Spec:**
```
Type:       Data analysis script (customer lifetime value)
Features:   - Query orders and customer acquisition channel from the database
            - Assign customers to monthly acquisition cohorts
            - Calculate cumulative revenue per customer at 3, 6 and 12 months
            - Average lifetime value per cohort and channel
            - Plot LTV curves per channel
Storage:    PostgreSQL
Tech stack: Python, SQL, pandas, SQLAlchemy, matplotlib
```

---

## Example 114

**Intent:**
i have pictures of handwritten forms and i want the text in a spreadsheet

**Spec:**
```
Type:       Data pipeline (OCR extraction)
Features:   - Load scanned form images from a folder
            - Detect and crop the form fields using a template layout
            - Recognise handwritten text with a handwriting OCR model
            - Write one row per form with a column per field to a spreadsheet
            - Flag low-confidence fields for manual checking
Input:      Folder of scanned form images
Storage:    Excel file
Tech stack: Python, OpenCV, Azure AI Document Intelligence, openpyxl
```

---

## Example 115

**Intent:**
identify plant species from leaf photos for my biology class app

**Spec:**
```
Type:       Machine learning model (image classification)
Features:   - Collect leaf images for the local plant species
            - Fine-tune MobileNetV3 for on-device use
            - Report accuracy per species on a test set
            - Convert the model to TensorFlow Lite
            - Return the top 3 species with confidence
Input:      Leaf photo from a phone camera
Tech stack: Python, TensorFlow, Keras, TensorFlow Lite
```

---

## Example 116

**Intent:**
compare A/B test results for our landing page

**Spec:**
```
Type:       Data analysis script (A/B testing)
Features:   - Load visitors and conversions for variants A and B
            - Calculate conversion rate and relative uplift
            - Test significance with a two-proportion z-test
            - Show the 95% confidence interval of the difference
            - Check sample ratio mismatch between variants
Input:      Experiment results CSV (variant, visitor_id, converted)
Tech stack: Python, pandas, statsmodels, SciPy
```

---

## Example 117

**Intent:**
we track deliveries with GPS every 30 sec and want a map dashboard of where drivers spend too much time

**Spec:**
```
Type:       Data dashboard (geospatial)
Features:   - Load GPS points per vehicle and trip
            - Detect stops longer than 10 minutes
            - Show stops on a map clustered by location
            - Show total stop time per driver per day
            - Filter by date, driver and region
Storage:    PostGIS
Tech stack: Python, Streamlit, GeoPandas, pydeck, PostGIS
```

---

## Example 118

**Intent:**
Dear sir, I want make the model for predict the rice price in my country market for next 3 month, I have price data from 2010 monthly.

**Spec:**
```
Type:       Machine learning model (time series forecasting)
Features:   - Load monthly rice prices since 2010
            - Check trend and seasonality with decomposition
            - Fit a SARIMA model chosen with AIC
            - Validate on the last 12 months and report MAPE
            - Forecast the next 3 months with confidence intervals
            - Plot history and forecast together
Input:      Monthly price CSV (month, price)
Tech stack: Python, pandas, statsmodels, matplotlib
```

---

## Example 119

**Intent:**
an ai that answers questions about our database schema for new devs

**Spec:**
```
Type:       Chatbot (codebase/schema Q&A)
Features:   - Read table and column definitions and comments from the database
            - Index schema descriptions and example queries as embeddings
            - Answer questions like "where are invoices stored" with table names
            - Suggest example SQL for a question
            - Refresh the index when migrations run
Storage:    Chroma (vector index)
Tech stack: Python, SQLAlchemy (schema reflection), LangChain, Chroma, OpenAI API
```

---

## Example 120

**Intent:**
Google Sheets formula stuff to track my monthly budget against what i spend

**Spec:**
```
Type:       Data dashboard (spreadsheet)
Features:   - Record expenses in a table with date, category and amount
            - Sum spending per category per month with SUMIFS
            - Compare spending with the budget and show the difference
            - Color categories over budget in red with conditional formatting
            - Chart spending per category per month
Tech stack: Google Sheets (SUMIFS, QUERY, conditional formatting, charts)
```

---

## Example 121

**Intent:**
predict the number of bikes rented per hour

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Load the hourly bike sharing dataset with weather and calendar fields
            - Create features for hour, weekday, season and holiday
            - Split train and test sets by time
            - Train a gradient boosting regressor and tune it with cross-validation
            - Report RMSLE and plot predicted vs actual rentals
Input:      Hourly bike rentals CSV
Tech stack: Python, pandas, scikit-learn, XGBoost
```

---

## Example 122

**Intent:**
tool where i paste a youtube link and get the summary of the video

**Spec:**
```
Type:       Web application (LLM summarisation)
Features:   - Accept a YouTube video URL
            - Fetch the video transcript, or transcribe the audio if none exists
            - Summarise the transcript into key points with timestamps
            - Answer follow-up questions about the video
            - Copy the summary as Markdown
Tech stack: Python, Flask, youtube-transcript-api, yt-dlp, OpenAI API
```

---

## Example 123

**Intent:**
dbt + snowflake for our product analytics events

**Spec:**
```
Type:       Data pipeline (ELT transformations)
Features:   - Stage raw product events from the Snowflake landing table
            - Sessionise events with a 30-minute inactivity gap
            - Build daily active users and feature usage models
            - Build a funnel model for signup to first key action
            - Test models with dbt tests and document them
Storage:    Snowflake
Tech stack: dbt Core, Snowflake, SQL
```

---

## Example 124

**Intent:**
The procurement team asked me to look at which suppliers are always late. We have purchase orders with promised and actual delivery dates for two years.

**Spec:**
```
Type:       Data analysis script (supplier performance)
Features:   - Load purchase orders with promised and actual delivery dates
            - Calculate days late and on-time delivery rate per supplier
            - Rank suppliers by on-time rate with a minimum number of orders
            - Show whether lateness is getting better or worse per quarter
            - Export a supplier scorecard to Excel
Input:      Purchase orders Excel export
Tech stack: Python, pandas, openpyxl, matplotlib
```

---

## Example 125

**Intent:**
ai that detects if a product review is fake

**Spec:**
```
Type:       Machine learning model (text classification)
Features:   - Load a labelled dataset of genuine and fake reviews
            - Combine text embeddings with reviewer features such as account age and review count
            - Train a classifier and tune the threshold for precision
            - Evaluate precision, recall and F1 on a test set
            - Score new reviews and send high-risk ones to moderators
Input:      Review text and reviewer metadata
Tech stack: Python, sentence-transformers, scikit-learn, pandas
```

---

## Example 126

**Intent:**
track brand mentions on reddit and see sentiment over time

**Spec:**
```
Type:       Data pipeline (social listening)
Features:   - Search Reddit for posts and comments mentioning the brand every hour
            - Store new mentions without duplicates
            - Score sentiment of each mention with a pretrained model
            - Aggregate daily mention counts and average sentiment
            - Show trends in a simple dashboard
Storage:    PostgreSQL
Tech stack: Python, PRAW, Hugging Face Transformers, Streamlit
```

---

## Example 127

**Intent:**
forecast how many patients come to the ER each day

**Spec:**
```
Type:       Machine learning model (forecasting)
Features:   - Aggregate ER arrivals per day from admission records
            - Add weekday, holiday, weather and flu season features
            - Train a model and backtest on the last year
            - Forecast arrivals for the next 14 days with prediction intervals
            - Show the forecast to the staff planners in a dashboard
Input:      ER admissions export
Tech stack: Python, pandas, statsforecast, Streamlit
```

---

## Example 128

**Intent:**
hi! we're a nonprofit food bank and we have spreadsheets of every family we serve each week. the board wants numbers: how many families, how many kids, is it going up. i've never done data stuff. can it be in google sheets since thats what we use

**Spec:**
```
Type:       Data dashboard (spreadsheet)
Features:   - Combine weekly visit sheets into one master table
            - Count unique families and total children served per week and month
            - Show the trend of families served with a line chart
            - Compare this year with last year by month
            - Create a summary tab for the board
Input:      Weekly visit spreadsheets
Tech stack: Google Sheets (QUERY, UNIQUE, pivot tables, charts)
```

---

## Example 129

**Intent:**
detect anomalies in our monthly expense reports, like duplicate or weird claims

**Spec:**
```
Type:       Data analysis script (expense audit)
Features:   - Load expense claims with employee, date, amount, category and merchant
            - Find exact and near-duplicate claims
            - Flag amounts far above the employee's or category's usual range
            - Flag claims on weekends and holidays
            - Export flagged claims with the reason for review
Input:      Expense claims CSV
Tech stack: Python, pandas, scikit-learn (Isolation Forest)
```

---

## Example 130

**Intent:**
chatbot to help ppl pick the right insurance plan

**Spec:**
```
Type:       Chatbot (guided recommendation)
Data model: Plan(id, name, monthly_price, deductible, coverage_json)
            Session(id, answers_json, recommended_plan_ids, created_at)
Features:   - Ask the user about age, family, budget and health needs
            - Compare plans from the plan catalog against the answers
            - Explain the recommended plans in plain language with an LLM
            - Show a comparison table of 2-3 plans
            - Hand over to a human advisor on request
Storage:    PostgreSQL
Tech stack: Python, FastAPI, OpenAI API (function calling), React
```

---

## Example 131

**Intent:**
PyTorch model to recognize handwritten digits

**Spec:**
```
Type:       Machine learning model (image classification)
Features:   - Load the MNIST dataset with train and test splits
            - Define a small convolutional neural network
            - Train with Adam and cross-entropy loss
            - Report test accuracy and a confusion matrix
            - Save the model and predict a digit from an image file
Input:      28x28 grayscale digit images
Tech stack: Python, PyTorch, torchvision
```

---

## Example 132

**Intent:**
Map of crime incidents in our city by type and month

**Spec:**
```
Type:       Data dashboard (geospatial)
Features:   - Load open data crime incidents with coordinates and type
            - Show incidents on an interactive map as a heatmap
            - Filter by crime type and month
            - Show counts per neighbourhood in a choropleth
            - Show monthly trend per crime type
Input:      City open data crime CSV
Tech stack: Python, Folium, GeoPandas, Streamlit
```

---

## Example 133

**Intent:**
pipeline to sync our hubspot deals into a reporting database every hour

**Spec:**
```
Type:       Data pipeline (ELT)
Features:   - Extract deals, companies and contacts updated since the last run from the HubSpot API
            - Flatten nested properties into columns
            - Upsert records into reporting tables
            - Track the last sync timestamp
            - Alert on API errors
Storage:    PostgreSQL
Tech stack: Airbyte, PostgreSQL
```

---

## Example 134

**Intent:**
i want to estimate how many calories are in my food from a picture

**Spec:**
```
Type:       Machine learning model (image recognition)
Features:   - Recognise food items in a photo with a model trained on Food-101
            - Estimate portion size with a reference object in the photo
            - Look up calories per 100 g for each food
            - Return total estimated calories and per-item breakdown
            - Let the user correct the detected foods
Input:      Food photo
Tech stack: Python, PyTorch, USDA FoodData Central API, FastAPI
```

---

## Example 135

**Intent:**
R shiny app to explore our clinical study data

**Spec:**
```
Type:       Data dashboard (R Shiny)
Auth:       Login for study team members
Features:   - Load study visits and lab results
            - Show patient enrolment over time per site
            - Plot lab values over time per patient
            - Compare outcomes between treatment arms
            - Download filtered data as CSV
Storage:    PostgreSQL
Tech stack: R, Shiny, tidyverse, plotly
```

---

## Example 136

**Intent:**
analyse my company's slack to see which channels are active

**Spec:**
```
Type:       Data analysis script (collaboration analytics)
Features:   - Export message counts per channel through the Slack API
            - Calculate messages per channel per week
            - Find channels with no activity in the last 90 days
            - Show the most active hours of the day
            - Save results to a CSV and chart
Tech stack: Python, slack_sdk, pandas, matplotlib
```

---

## Example 137

**Intent:**
recomend movies based on what i liked, small project for school

**Spec:**
```
Type:       Machine learning model (recommendation)
Features:   - Load the MovieLens small dataset
            - Build a user-movie rating matrix
            - Find similar movies with item-based cosine similarity
            - Recommend top 10 unseen movies for a user
            - Evaluate with RMSE on held-out ratings
Input:      User id or a list of liked movies
Tech stack: Python, pandas, scikit-learn
```

---

## Example 138

**Intent:**
model that reads support emails and drafts a reply for the agent

**Spec:**
```
Type:       Web application (LLM assistant)
Features:   - Fetch new support emails from the helpdesk
            - Retrieve similar resolved tickets and help articles
            - Draft a reply with an LLM using the retrieved context
            - Let the agent edit and send the draft
            - Track how much of each draft agents changed
Storage:    PostgreSQL, pgvector
Tech stack: Python, FastAPI, OpenAI API, pgvector, Freshdesk API
```

---

## Example 139

**Intent:**
Plz make me something that reads my monthly bank statement PDF and tells me where my money went, I'm terrible with money

**Spec:**
```
Type:       Data analysis script (personal finance)
Features:   - Extract transactions from the bank statement PDF
            - Categorise transactions with an LLM into groceries, rent, transport, eating out and more
            - Sum spending per category for the month
            - Show a pie chart of spending
            - Compare with the previous month
Input:      Bank statement PDF
Tech stack: Python, pdfplumber, pandas, OpenAI API, matplotlib
```

---

## Example 140

**Intent:**
astronomy data: find exoplanets in kepler light curves

**Spec:**
```
Type:       Machine learning model (time series classification)
Features:   - Download Kepler light curves for labelled stars
            - Detrend and normalise each light curve
            - Search for periodic dips with a box least squares periodogram
            - Train a 1D CNN on folded light curves to classify planet candidates
            - Report precision and recall on a held-out set
Input:      Kepler light curve FITS files
Tech stack: Python, lightkurve, Astropy, PyTorch
```

---

## Example 141

**Intent:**
stock portfolio risk analysis

**Spec:**
```
Type:       Data analysis script (finance)
Features:   - Load holdings and download historical daily prices
            - Calculate daily returns and portfolio volatility
            - Calculate Value at Risk with historical simulation
            - Show correlation matrix of holdings
            - Calculate Sharpe ratio and max drawdown
Input:      Holdings CSV (ticker, shares)
Tech stack: Python, yfinance, pandas, NumPy
```

---

## Example 142

**Intent:**
We record every machine stop in the factory in an Excel log with a reason. I'd like a Power BI report to see where we lose the most production time.

**Spec:**
```
Type:       Data dashboard (manufacturing)
Features:   - Import the downtime log from Excel
            - Calculate total downtime per machine, reason and shift
            - Show a Pareto chart of downtime reasons
            - Calculate OEE availability per machine per week
            - Filter by line, machine and date
Input:      Downtime log Excel
Tech stack: Power BI, Power Query, DAX
```

---

## Example 143

**Intent:**
whats the best time to post on instagram based on my insights

**Spec:**
```
Type:       Data analysis script (social media)
Features:   - Load post-level Instagram insights export
            - Calculate engagement rate per post
            - Average engagement rate by weekday and hour
            - Show a weekday by hour heatmap
            - List the top 5 time slots
Input:      Instagram insights CSV
Tech stack: Python, pandas, seaborn
```

---

## Example 144

**Intent:**
model to predict the strength of concrete

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Load mix design data (cement, water, aggregates, additives, age)
            - Split train and test sets
            - Train gradient boosting and neural network regressors
            - Report RMSE and R²
            - Show partial dependence of strength on water-cement ratio
Input:      Concrete mix CSV
Tech stack: Python, scikit-learn, pandas
```

---

## Example 145

**Intent:**
ingest weather api every hour into a data lake

**Spec:**
```
Type:       Data pipeline (ingestion)
Features:   - Call the weather API for a list of locations every hour
            - Save raw JSON responses partitioned by date
            - Convert raw files into Parquet with a fixed schema
            - Register tables in a data catalog for querying
            - Alert on failed API calls
Storage:    Amazon S3 (data lake)
Tech stack: AWS Lambda, Amazon EventBridge, AWS Glue, Amazon Athena, Python
```

---

## Example 146

**Intent:**
a chatbot that teaches spanish by talking with me

**Spec:**
```
Type:       Chatbot (language tutoring)
Data model: Learner(id, level)
            VocabItem(id, learner_id -> Learner, word, translation, times_missed)
Features:   - Hold conversations in Spanish at the learner's level
            - Correct grammar mistakes and explain them in English
            - Suggest new vocabulary related to the conversation
            - Save words the learner struggles with for review
            - Switch between topics like travel, food and work
Storage:    SQLite
Tech stack: Python, FastAPI, OpenAI API, React
```

---

## Example 147

**Intent:**
i need to clean addresses and geocode 20k customers to lat long

**Spec:**
```
Type:       Data pipeline (geocoding)
Features:   - Read customer addresses from a CSV
            - Standardise address formatting
            - Geocode each address with a geocoding API with rate limiting
            - Cache results to avoid repeat lookups
            - Write latitude, longitude and match quality to a new CSV
Input:      Customer addresses CSV
Storage:    SQLite (geocode cache)
Tech stack: Python, pandas, geopy, Nominatim or Google Geocoding API
```

---

## Example 148

**Intent:**
dashboard of my youtube channel analytics

**Spec:**
```
Type:       Data dashboard (creator analytics)
Features:   - Fetch views, watch time, subscribers and revenue from the YouTube Analytics API
            - Show daily trends per metric
            - Rank videos by views and average view duration
            - Show traffic sources and top countries
            - Compare the last 28 days with the previous 28
Tech stack: Python, Streamlit, YouTube Analytics API, Plotly
```

---

## Example 149

**Intent:**
which marketing channel give us best ROI? we have spend and sales per week for 3 years

**Spec:**
```
Type:       Machine learning model (marketing mix modelling)
Features:   - Load weekly spend per channel and weekly sales
            - Apply adstock and saturation transforms to channel spend
            - Fit a Bayesian regression of sales on transformed spend plus seasonality
            - Estimate ROI and contribution per channel
            - Simulate sales for different budget splits
Input:      Weekly spend and sales CSV
Tech stack: Python, PyMC-Marketing, pandas
```

---

## Example 150

**Intent:**
run sentiment on our app store reviews

**Spec:**
```
Type:       Data analysis script (review analysis)
Features:   - Download recent reviews from the App Store and Google Play
            - Score sentiment of each review
            - Extract common topics with BERTopic
            - Show sentiment trend by app version
            - List the most common complaints
Tech stack: Python, app-store-scraper, google-play-scraper, Hugging Face Transformers, BERTopic
```

---

## Example 151

**Intent:**
auto tag support tickets in jira using ai

**Spec:**
```
Type:       Webhook service (LLM classification)
Features:   - Receive a Jira webhook when an issue is created
            - Classify the issue into component and priority with an LLM
            - Add labels and set the component through the Jira API
            - Skip issues that already have labels
            - Log every decision for review
API:        REST
            POST /webhooks/jira
Tech stack: Python, FastAPI, Jira REST API, OpenAI API
```

---

## Example 152

**Intent:**
My PhD project: I have gene expression data from RNA-seq for 40 samples, treated vs control, and I need to find which genes are differentially expressed.

**Spec:**
```
Type:       Data analysis script (bioinformatics)
Features:   - Load the raw count matrix and sample metadata
            - Filter lowly expressed genes
            - Normalise counts and run differential expression with DESeq2
            - Adjust p-values for multiple testing
            - Draw a volcano plot and a heatmap of top genes
            - Run gene set enrichment on significant genes
Input:      Count matrix CSV and sample metadata CSV
Tech stack: R, DESeq2, ggplot2, clusterProfiler
```

---

## Example 153

**Intent:**
what if i want an ai to read invoices and fill our accounting software

**Spec:**
```
Type:       Data pipeline (document AI)
Features:   - Collect invoice PDFs from an email inbox
            - Extract supplier, invoice number, dates, line items, VAT and totals
            - Check that line items add up to the total
            - Match the supplier to existing vendors
            - Create a draft bill in the accounting software
            - Send unclear invoices to a review queue
Storage:    PostgreSQL (processing status)
Tech stack: Python, Google Document AI (Invoice Parser), Xero API
```

---

## Example 154

**Intent:**
excel predict sales next year with trend

**Spec:**
```
Type:       Data analysis script (Excel forecasting)
Features:   - Arrange monthly sales history in a table
            - Use the FORECAST.ETS function to forecast the next 12 months
            - Show upper and lower confidence bounds
            - Chart history and forecast together
            - Compare the forecast total with this year
Input:      Monthly sales in an Excel sheet
Tech stack: Microsoft Excel (FORECAST.ETS, Forecast Sheet)
```

---

## Example 155

**Intent:**
python script to find outliers in lab measurements

**Spec:**
```
Type:       Data analysis script (quality control)
Features:   - Load lab measurements per sample and test
            - Detect outliers with the IQR rule and z-scores per test
            - Plot measurements with outliers highlighted
            - Flag samples with outliers on multiple tests
            - Save an outlier report CSV
Input:      Lab results CSV
Tech stack: Python, pandas, SciPy, matplotlib
```

---

## Example 156

**Intent:**
ml model that tells which machine part will fail soon

**Spec:**
```
Type:       Machine learning model (predictive maintenance)
Features:   - Combine sensor readings, maintenance logs and failure records per machine
            - Create rolling window features over the last 24 hours
            - Label windows that are followed by a failure within 7 days
            - Train a classifier with time-based validation
            - Report recall at a fixed false alarm rate
            - Produce a daily risk list of machines
Input:      Sensor history and maintenance logs
Storage:    PostgreSQL
Tech stack: Python, pandas, LightGBM, Airflow
```

---

## Example 157

**Intent:**
idk how to start but i want ai to sort my photos by whos in them

**Spec:**
```
Type:       Desktop application (face clustering)
Features:   - Scan a photo folder and detect faces in each photo
            - Create face embeddings with a pretrained face recognition model
            - Group similar faces into clusters with DBSCAN
            - Let the user name each cluster
            - Filter photos by person name
Input:      Folder of photos
Storage:    SQLite (faces, clusters, names)
Tech stack: Python, face_recognition (dlib), scikit-learn, PySide6
```

---

## Example 158

**Intent:**
churn model for our gym members

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Build features from visit frequency, membership length, payment issues and class bookings
            - Label members who cancelled within the next 60 days
            - Train a random forest with stratified cross-validation
            - Report recall and precision for churners
            - Score current members weekly and list those at risk
Input:      Member and check-in exports from the gym software
Tech stack: Python, pandas, scikit-learn
```

---

## Example 159

**Intent:**
weekly email that tells our sales managers their team numbers from salesforce

**Spec:**
```
Type:       Scheduled script (reporting)
Features:   - Query closed-won deals, pipeline and activities per rep from Salesforce
            - Calculate quota attainment per rep and team
            - Compare with the previous week
            - Render a personalised HTML email per manager
            - Send emails every Monday morning
Tech stack: Python, simple-salesforce, Jinja2, Amazon SES, AWS Lambda (scheduled)
```

---

## Example 160

**Intent:**
data pipline that take files from sftp every nite and load to sql server

**Spec:**
```
Type:       Data pipeline (ETL)
Features:   - Connect to the SFTP server every night and list new files
            - Download new files and keep a record of processed files
            - Validate columns and data types
            - Bulk load valid rows into SQL Server staging tables
            - Run a stored procedure to merge staging into final tables
            - Email a summary of loaded and failed files
Storage:    SQL Server
Tech stack: SQL Server Integration Services (SSIS), SQL Server Agent
```

---

## Example 161

**Intent:**
make a model to predict the next word like on phone keyboard

**Spec:**
```
Type:       Machine learning model (language model)
Features:   - Collect and clean a text corpus
            - Tokenise text into words and build a vocabulary
            - Train an LSTM language model to predict the next word
            - Evaluate perplexity on a validation set
            - Suggest the top 3 next words for a typed phrase
Input:      Text corpus files
Tech stack: Python, PyTorch
```

---

## Example 162

**Intent:**
I'm a freelance data person and a client sent me 5 years of sales from 40 stores in messy Excel files, one per store per year, with slightly different columns. They want one clean dataset and an overview of growth per store.

**Spec:**
```
Type:       Data analysis script (data consolidation)
Features:   - Read all store Excel files from a folder
            - Map differing column names to one standard schema
            - Add store and year columns from file names
            - Clean dates, amounts and missing values
            - Combine everything into one Parquet dataset
            - Calculate yearly revenue and growth per store with a summary chart
Input:      Folder of 200 Excel files
Storage:    Parquet file
Tech stack: Python, pandas, openpyxl, pyarrow, matplotlib
```

---

## Example 163

**Intent:**
a model that predicts how long a support ticket will take to close

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Use ticket category, priority, channel, text length and agent team as features
            - Add TF-IDF features from the ticket subject
            - Train a gradient boosting model on log resolution hours
            - Report median absolute error
            - Show estimated resolution time to agents when tickets arrive
Input:      Closed tickets export
Tech stack: Python, scikit-learn, LightGBM
```

---

## Example 164

**Intent:**
build a rag chatbot over our legal documents but it must run on our own servers, no cloud

**Spec:**
```
Type:       Chatbot (on-premise document Q&A)
Auth:       Login with company Active Directory (LDAP)
Features:   - Ingest Word and PDF legal documents into chunks
            - Create embeddings with a local embedding model
            - Store vectors in a self-hosted vector database
            - Answer questions with a locally hosted LLM and cite document sections
            - Log questions and answers for audit
Storage:    Milvus (self-hosted vector database), PostgreSQL (audit log)
Tech stack: Python, LlamaIndex, vLLM (Llama 3), BGE embeddings, Milvus
```

---

## Example 165

**Intent:**
kpi dashboard for ceo

**Spec:**
```
Type:       Data dashboard (executive KPIs)
Features:   - Show revenue, gross margin, new customers and cash balance for the current month
            - Compare each KPI with target and last year
            - Show 12-month trend sparklines
            - Highlight KPIs that miss target in red
            - Refresh data every night
Storage:    Snowflake
Tech stack: Power BI, Snowflake connector
```

---

## Example 166

**Intent:**
i want see if there is relation between weather and our restaurant sales, i have daily sales of 2 year

**Spec:**
```
Type:       Data analysis script (correlation analysis)
Features:   - Load daily sales and download historical weather for the restaurant location
            - Join sales and weather by date
            - Calculate correlation between sales and temperature, rain and wind
            - Fit a regression controlling for weekday and holidays
            - Plot sales against temperature with a trend line
Input:      Daily sales CSV
Tech stack: Python, pandas, Meteostat, statsmodels, seaborn
```

---

## Example 167

**Intent:**
detect when someone is not wearing helmet on construction site camera

**Spec:**
```
Type:       Machine learning model (object detection)
Features:   - Label images with person, helmet and no-helmet boxes
            - Train a YOLO object detection model on the labelled images
            - Evaluate mAP on a validation set
            - Run detection on the live camera stream
            - Save a snapshot and alert the site manager when a person without a helmet is detected
Input:      RTSP camera stream
Storage:    Local disk (snapshots)
Tech stack: Python, Ultralytics YOLOv8, OpenCV, Label Studio
```

---

## Example 168

**Intent:**
Analyze my Fitbit sleep data in a Jupyter notebook

**Spec:**
```
Type:       Data analysis script (health data)
Features:   - Load sleep logs from the Fitbit data export
            - Calculate total sleep, deep sleep and REM per night
            - Plot sleep duration over time with a 7-day average
            - Compare sleep on weekdays and weekends
            - Check correlation between steps and sleep quality
Input:      Fitbit data export (JSON files)
Tech stack: Python, Jupyter Notebook, pandas, matplotlib
```

---

## Example 169

**Intent:**
api that predicts if a loan applicant will default

**Spec:**
```
Type:       REST API service (ML model serving)
Auth:       API key per client application
Features:   - Load a trained credit default model at startup
            - Validate applicant input fields
            - Return default probability and a risk band
            - Return the top reasons for the score
            - Log each request and prediction for monitoring
API:        REST
            POST /predict
            GET /health
Storage:    PostgreSQL (prediction log)
Tech stack: Python, FastAPI, scikit-learn, joblib, Docker
```

---

## Example 170

**Intent:**
sales funnel analysis

**Spec:**
```
Type:       Data analysis script (funnel analysis)
Features:   - Load leads with stage timestamps
            - Count leads reaching each funnel stage
            - Calculate conversion rate between stages
            - Calculate average days spent in each stage
            - Compare funnels by lead source
Input:      CRM leads export
Tech stack: Python, pandas, Plotly
```

---

## Example 171

**Intent:**
whats the easiest way to make my data from google forms into a live dashboard

**Spec:**
```
Type:       Data dashboard (survey)
Features:   - Connect the Google Forms response sheet as a data source
            - Show response count over time
            - Show a chart for each multiple-choice question
            - Show averages for rating questions
            - Add filters for date and respondent group
Input:      Google Forms response sheet
Tech stack: Looker Studio, Google Sheets
```

---

## Example 172

**Intent:**
fine tune bert to find names and companies in text

**Spec:**
```
Type:       Machine learning model (named entity recognition)
Features:   - Load a labelled NER dataset in BIO format
            - Tokenise text and align labels with subword tokens
            - Fine-tune a BERT model for token classification
            - Evaluate entity-level precision, recall and F1
            - Extract person and organisation names from new text
Input:      Raw text
Tech stack: Python, Hugging Face Transformers, datasets, seqeval
```

---

## Example 173

**Intent:**
forecast our website traffic for next quarter

**Spec:**
```
Type:       Machine learning model (forecasting)
Features:   - Load daily sessions from analytics
            - Model weekly and yearly seasonality and holiday effects
            - Validate on the last 90 days
            - Forecast daily sessions for the next 90 days
            - Plot the forecast with uncertainty intervals
Input:      Daily sessions CSV
Tech stack: Python, Prophet, pandas
```

---

## Example 174

**Intent:**
chat bot on telegram that answers questions about crypto prices and news

**Spec:**
```
Type:       Bot (Telegram)
Features:   - Reply to /price commands with the current price and 24h change
            - Send a daily market summary to subscribers
            - Fetch latest crypto news and summarise them with an LLM
            - Set price alerts that trigger a message
            - Store user subscriptions and alerts
Storage:    SQLite
Tech stack: Python, python-telegram-bot, CoinGecko API, OpenAI API
```

---

## Example 175

**Intent:**
i want my pc to know if my cat is on the kitchen table using a webcam lol

**Spec:**
```
Type:       Machine learning model (object detection)
Features:   - Read frames from a webcam
            - Detect cats with a pretrained COCO object detection model
            - Check if the cat box overlaps a marked table area
            - Play a sound when the cat is on the table
            - Save a photo of each event
Input:      Webcam video stream
Tech stack: Python, OpenCV, Ultralytics YOLOv8
```

---

## Example 176

**Intent:**
Our school district has standardized test scores for 5 years and the superintendent wants to know if the tutoring program helped.

**Spec:**
```
Type:       Data analysis script (program evaluation)
Features:   - Join test scores with tutoring participation by student
            - Match tutored and non-tutored students on prior scores and demographics with propensity scores
            - Compare score gains between matched groups
            - Report the effect with confidence intervals
            - Break results down by grade and school
Input:      Student test scores and program rosters
Tech stack: R, MatchIt, tidyverse, ggplot2
```

---

## Example 177

**Intent:**
recommendation engine for news articles on our site

**Spec:**
```
Type:       Machine learning model (recommendation)
Features:   - Track article views per user
            - Create article embeddings from title and text
            - Build user profiles from recently read article embeddings
            - Recommend fresh articles closest to the user profile
            - Mix in trending articles for new users
API:        REST
            GET /recommendations?user_id={id}
Storage:    Redis, Qdrant
Tech stack: Python, sentence-transformers, Qdrant, FastAPI
```

---

## Example 178

**Intent:**
compare salaries men and women in our company

**Spec:**
```
Type:       Data analysis script (pay equity)
Features:   - Load employee salary, gender, role, level, tenure and location
            - Calculate the raw pay gap by gender
            - Fit a regression on log salary controlling for role, level, tenure and location
            - Report the adjusted pay gap with confidence interval
            - Show pay gap per department
Input:      HR salary export
Tech stack: Python, pandas, statsmodels
```

---

## Example 179

**Intent:**
plz help, model that predicts sales for each product in each store, like 50k combinations

**Spec:**
```
Type:       Machine learning model (hierarchical forecasting)
Features:   - Prepare daily sales per store and product
            - Create lag, rolling mean, price and promotion features
            - Train one global LightGBM model across all series
            - Validate with a rolling time-based backtest and WRMSSE
            - Forecast the next 28 days for all store-product pairs
Input:      Daily sales, prices and calendar tables
Storage:    Parquet files
Tech stack: Python, Polars, LightGBM
```

---

## Example 180

**Intent:**
show me how to use spark to process our big log files

**Spec:**
```
Type:       Data pipeline (batch processing)
Features:   - Read compressed log files from object storage
            - Parse log lines into columns with regex
            - Filter out health check requests
            - Aggregate requests, errors and latency per endpoint per hour
            - Write results to partitioned Parquet tables
Input:      Gzipped web server logs in S3
Storage:    Amazon S3 (Parquet)
Tech stack: Apache Spark (PySpark), Amazon EMR
```

---

## Example 181

**Intent:**
ai helper for doctors that summarizes patient history before appointment

**Spec:**
```
Type:       Web application (clinical summarisation)
Auth:       Hospital single sign-on with role-based access for clinicians
Features:   - Load the patient's past notes, diagnoses, medications and lab results
            - Summarise the history into a one-page brief with an LLM
            - Link every summary point to its source record
            - Highlight recent abnormal lab results
            - Log every access for audit
Storage:    PostgreSQL (audit log)
Tech stack: Python, FastAPI, FHIR API, Azure OpenAI (private deployment), React
```

---

## Example 182

**Intent:**
I have a list of 10k company names that are written different ways and need to match them to our master list

**Spec:**
```
Type:       Data analysis script (entity matching)
Features:   - Normalise names by removing legal suffixes, punctuation and case
            - Generate candidate matches with TF-IDF character n-gram similarity
            - Score candidates with fuzzy matching ratios
            - Accept matches above a threshold and list uncertain ones
            - Write a mapping CSV of input name to master id
Input:      Input names CSV and master list CSV
Tech stack: Python, pandas, scikit-learn, RapidFuzz
```

---

## Example 183

**Intent:**
hockey team stats tracker with charts

**Spec:**
```
Type:       Data dashboard (sports)
Features:   - Enter game results and player goals, assists and penalty minutes
            - Show standings and player point leaders
            - Show goals per game trend
            - Show plus/minus per player
            - Export stats to CSV
Storage:    SQLite
Tech stack: Python, Streamlit, pandas, Altair
```

---

## Example 184

**Intent:**
chatgpt like thing for our internal company data but secure

**Spec:**
```
Type:       Chatbot (enterprise assistant)
Auth:       Single sign-on with Microsoft Entra ID
Features:   - Connect to SharePoint, Confluence and Google Drive sources
            - Index documents with permissions attached to each chunk
            - Answer questions only from documents the user can access
            - Cite sources with links
            - Keep chat history per user
            - Let admins see usage statistics
Storage:    Azure AI Search, Azure Cosmos DB (chat history)
Tech stack: Python, Azure OpenAI, Azure AI Search, Microsoft Graph API, React
```

---

## Example 185

**Intent:**
weather station data cleaning

**Spec:**
```
Type:       Data analysis script (data cleaning)
Features:   - Load raw weather station readings
            - Flag values outside physical limits
            - Detect stuck sensors with repeated identical values
            - Fill short gaps with linear interpolation
            - Save cleaned data with quality flags
Input:      Raw station CSV files
Tech stack: Python, pandas, NumPy
```

---

## Example 186

**Intent:**
i want to predict which of our online ads will get clicked

**Spec:**
```
Type:       Machine learning model (click-through rate prediction)
Features:   - Load ad impression logs with user, ad and context features
            - Hash high-cardinality categorical features
            - Train a logistic regression and a factorization machine
            - Evaluate log loss and AUC on the latest day
            - Output predicted CTR for each ad and user context
Input:      Impression logs with click labels
Tech stack: Python, scikit-learn, xLearn
```

---

## Example 187

**Intent:**
script to download and merge all the census tables for my county

**Spec:**
```
Type:       Data analysis script (public data)
Features:   - Download selected tables from the Census API for all tracts in a county
            - Rename variable codes to readable names
            - Merge tables into one dataset per tract
            - Calculate derived rates such as poverty rate
            - Join tract boundaries and save as a GeoPackage
Input:      State and county FIPS codes
Storage:    GeoPackage file
Tech stack: Python, census, pandas, GeoPandas
```

---

## Example 188

**Intent:**
yo i trade forex and want to backtest a strategy on 10 years of hourly data

**Spec:**
```
Type:       Data analysis script (backtesting)
Features:   - Load hourly OHLC data for currency pairs
            - Implement entry and exit rules from indicators
            - Simulate trades with spread and commission
            - Calculate total return, win rate, Sharpe ratio and max drawdown
            - Plot the equity curve and trade markers
Input:      Hourly OHLC CSV per currency pair
Tech stack: Python, pandas, backtesting.py
```

---

## Example 189

**Intent:**
sort incoming CVs for a job and rank them

**Spec:**
```
Type:       Web application (LLM resume screening)
Auth:       Recruiter login
Data model: Job(id, title, description)
            Candidate(id, job_id -> Job, cv_text, score, reasons)
Features:   - Upload a job description and a batch of CV PDFs
            - Extract skills, experience and education from each CV
            - Score each CV against the job requirements with an LLM and a rubric
            - Rank candidates with a short reason for each score
            - Remove names and photos from the view to reduce bias
Storage:    PostgreSQL
Tech stack: Python, Django, pdfplumber, Anthropic Claude API
```

---

## Example 190

**Intent:**
model that predicts traffic jams on highway segments

**Spec:**
```
Type:       Machine learning model (spatio-temporal forecasting)
Features:   - Load speed sensor readings per highway segment every 5 minutes
            - Build a graph of connected segments
            - Train a graph neural network to forecast speed 30 minutes ahead
            - Compare with a historical average baseline using MAE
            - Flag segments where predicted speed drops below a congestion threshold
Input:      Traffic sensor data
Tech stack: Python, PyTorch, PyTorch Geometric Temporal
```

---

## Example 191

**Intent:**
Turn our raw clickstream into user sessions and page paths

**Spec:**
```
Type:       Data pipeline (sessionisation)
Features:   - Read raw click events ordered by user and time
            - Split events into sessions after 30 minutes of inactivity
            - Build the ordered page path per session
            - Calculate session duration and pages per session
            - Write sessions to a warehouse table
Storage:    BigQuery
Tech stack: SQL (BigQuery window functions), dbt
```

---

## Example 192

**Intent:**
i need to show my thesis results with nice charts, data is in excel

**Spec:**
```
Type:       Data analysis script (visualisation)
Features:   - Load experiment results from Excel sheets
            - Calculate means and standard errors per group
            - Draw bar charts with error bars and significance marks
            - Draw scatter plots with regression lines
            - Export charts as high-resolution PDF and PNG
Input:      Excel workbook with results
Tech stack: Python, pandas, seaborn, matplotlib
```

---

## Example 193

**Intent:**
llm that turns meeting notes into jira tickets

**Spec:**
```
Type:       Command-line tool (LLM extraction)
Features:   - Read meeting notes from a text or Markdown file
            - Extract action items with owner, title and description with an LLM
            - Show extracted tickets for confirmation
            - Create confirmed tickets in a Jira project
            - Print links to the created tickets
Input:      Meeting notes file and Jira project key
Tech stack: Python, OpenAI API, Jira REST API, Typer
```

---

## Example 194

**Intent:**
dashboard of air pollution in our city from public sensors

**Spec:**
```
Type:       Data dashboard (environmental)
Features:   - Fetch PM2.5 and NO2 readings from the OpenAQ API every hour
            - Show sensors on a map colored by air quality index
            - Show 24-hour and 30-day trends per sensor
            - Compare readings with WHO guideline levels
            - Show daily city average ranking
Storage:    TimescaleDB
Tech stack: Grafana, TimescaleDB, Python (ingestion), OpenAQ API
```

---

## Example 195

**Intent:**
build a model that can tell what emotion is in someones voice

**Spec:**
```
Type:       Machine learning model (speech emotion recognition)
Features:   - Load labelled speech emotion datasets
            - Extract audio embeddings with a pretrained wav2vec 2.0 model
            - Train a classifier head for emotions
            - Report accuracy and confusion matrix per emotion
            - Predict emotion for a new audio clip
Input:      Speech audio clip
Tech stack: Python, PyTorch, Hugging Face Transformers, torchaudio
```

---

## Example 196

**Intent:**
we run 30 apartment buildings and want to predict which ones will need big repairs next year

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Combine building age, past repair costs, inspection scores and work order counts
            - Label buildings with major repair costs in the following year
            - Train a gradient boosting model with cross-validation
            - Explain each prediction with SHAP
            - Rank buildings by predicted risk for budget planning
Input:      Building and maintenance records
Tech stack: Python, pandas, XGBoost, SHAP
```

---

## Example 197

**Intent:**
power bi report on our customer support calls

**Spec:**
```
Type:       Data dashboard (call center)
Features:   - Import call records from the phone system
            - Show calls per hour and day with answer and abandon rates
            - Show average wait time and handle time per agent
            - Show service level against target
            - Drill down from month to day
Input:      Call records CSV export
Tech stack: Power BI, Power Query, DAX
```

---

## Example 198

**Intent:**
Jupyter notebook to clean and explore a messy real estate dataset

**Spec:**
```
Type:       Data analysis script (exploratory)
Features:   - Load the dataset and inspect types and missing values
            - Fix price and area columns stored as text
            - Remove duplicates and impossible values
            - Plot price distributions by city and property type
            - Show correlations between price and features
Input:      Real estate listings CSV
Tech stack: Python, Jupyter, pandas, seaborn
```

---

## Example 199

**Intent:**
auto generate weekly insights from our data warehouse with gpt

**Spec:**
```
Type:       Scheduled script (LLM reporting)
Features:   - Run a fixed set of SQL queries for weekly KPIs
            - Detect the largest changes compared with the previous week
            - Ask an LLM to write short plain-language insights from the numbers
            - Post insights and a chart to a Slack channel
            - Store the weekly results for history
Storage:    Snowflake
Tech stack: Python, Snowflake connector, OpenAI API, Slack SDK, Airflow
```

---

## Example 200

**Intent:**
tool to label images for training my model

**Spec:**
```
Type:       Web application (data labelling)
Auth:       Login for labelling team members
Data model: Project(id, name, label_set)
            Image(id, project_id -> Project, path, status)
            Annotation(id, image_id -> Image, user_id, label, bbox_json)
Features:   - Upload a batch of images to a project
            - Draw bounding boxes and choose a label
            - Assign images to labellers
            - Review and approve annotations
            - Export annotations in COCO and YOLO format
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, Django, React, Konva.js
```

---

## Example 201

**Intent:**
churn prediction for my saas, data in postgres, want it in a notebook first

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Query accounts, usage events and billing data from PostgreSQL
            - Build features such as logins per week, seats used and support tickets
            - Label accounts that cancelled within 30 days
            - Train and compare logistic regression and LightGBM
            - Report ROC AUC and a lift chart
            - Save the best model with MLflow
Storage:    PostgreSQL, MLflow tracking server
Tech stack: Python, Jupyter, SQLAlchemy, pandas, LightGBM, MLflow
```

---

## Example 202

**Intent:**
map where my blog readers come from

**Spec:**
```
Type:       Data analysis script (web analytics)
Features:   - Export sessions by country and city from the analytics tool
            - Geocode cities to coordinates
            - Plot readers on a world map sized by sessions
            - Show top 10 countries in a table
            - Save the map as an HTML file
Input:      Analytics CSV export
Tech stack: Python, pandas, Plotly
```

---

## Example 203

**Intent:**
I volunteer for a local football club and we film our matches. I'd love something that tracks the players and the ball in the video and shows a heatmap of where each player was, like the pros have.

**Spec:**
```
Type:       Machine learning model (video tracking)
Features:   - Detect players and the ball in each video frame with an object detection model
            - Track players across frames with a multi-object tracker
            - Map pixel positions to pitch coordinates with a homography
            - Let the user assign track ids to player names
            - Draw a position heatmap per player on a pitch diagram
Input:      Match video file
Storage:    Local CSV files (tracking data)
Tech stack: Python, Ultralytics YOLOv8, ByteTrack, OpenCV, mplsoccer
```

---

## Example 204

**Intent:**
pipeline that anonymises customer data before analysts can use it

**Spec:**
```
Type:       Data pipeline (data masking)
Features:   - Read customer tables from the production replica
            - Hash email and phone with a salted hash
            - Replace names with fake names consistently
            - Generalise birth dates to year and postcodes to region
            - Write masked tables to the analytics schema nightly
Storage:    PostgreSQL (analytics schema)
Tech stack: Python, pandas, Faker, Apache Airflow
```

---

## Example 205

**Intent:**
what features of my app do people actually use

**Spec:**
```
Type:       Data analysis script (product analytics)
Features:   - Load product event logs
            - Map events to features
            - Calculate weekly active users per feature and adoption rate
            - Compare feature usage between free and paid users
            - Show features used by less than 5% of users
Input:      Product events export (user_id, event_name, timestamp, plan)
Tech stack: Python, pandas, Plotly
```

---

## Example 206

**Intent:**
ML to predict crop disease outbreaks from weather

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Combine daily weather with historical disease reports per region
            - Create features such as leaf wetness hours, rolling humidity and temperature
            - Label weeks with a reported outbreak
            - Train a random forest with time-based validation
            - Send weekly risk levels per region to advisers
Input:      Weather data and outbreak reports
Tech stack: Python, pandas, scikit-learn
```

---

## Example 207

**Intent:**
hi i wanna make a bot for my discord that can answer questions about our minecraft server rules

**Spec:**
```
Type:       Bot (Discord, document Q&A)
Features:   - Load the server rules and FAQ from a text file
            - Create embeddings of each rule
            - Answer questions mentioned to the bot using the most relevant rules
            - Quote the rule number in the answer
            - Let admins reload the rules with a command
Input:      Rules text file
Tech stack: Python, discord.py, sentence-transformers, OpenAI API
```

---

## Example 208

**Intent:**
SAS code to analyse insurance claims frequency

**Spec:**
```
Type:       Data analysis script (actuarial)
Features:   - Load policy and claim tables
            - Calculate claim frequency per exposure year by risk group
            - Fit a Poisson GLM with exposure offset
            - Report relativities per rating factor
            - Check model fit with deviance residuals
Input:      Policy and claims datasets
Tech stack: SAS (PROC GENMOD, PROC SQL)
```

---

## Example 209

**Intent:**
compare my two years of running races times

**Spec:**
```
Type:       Data analysis script (personal sports)
Features:   - Load race results with date, distance and time
            - Convert times to pace per kilometer
            - Compare average pace per distance between the two years
            - Plot pace over time per distance
            - Show improvement percentage
Input:      Spreadsheet of race results
Tech stack: Python, pandas, matplotlib
```

---

## Example 210

**Intent:**
Our customers write in English, German and French; we need sentiment analysis that works for all three on our survey comments.

**Spec:**
```
Type:       Machine learning model (multilingual sentiment)
Features:   - Load survey comments with language detection
            - Score sentiment with a multilingual transformer model
            - Fine-tune on a few hundred labelled comments per language
            - Evaluate F1 per language
            - Aggregate sentiment per question and country
Input:      Survey comments CSV
Tech stack: Python, Hugging Face Transformers (XLM-RoBERTa), pandas
```

---

## Example 211

**Intent:**
ask questions about my spreadsheet in normal english

**Spec:**
```
Type:       Web application (LLM data analysis)
Features:   - Upload a CSV or Excel file
            - Send column names and sample rows to an LLM
            - Generate and run pandas code to answer the question in a sandbox
            - Show the answer as text, table or chart
            - Show the generated code
Input:      CSV or Excel file
Tech stack: Python, Streamlit, pandas, OpenAI API
```

---

## Example 212

**Intent:**
data pipeline to collect tweets about elections for research

**Spec:**
```
Type:       Data pipeline (social media collection)
Features:   - Query the X API for posts matching election keywords and hashtags
            - Store raw posts with author and engagement metadata
            - Remove duplicates and retweets
            - Detect language and keep selected languages
            - Export daily datasets for researchers
Storage:    MongoDB
Tech stack: Python, X API v2, pymongo, cron
```

---

## Example 213

**Intent:**
tesla stock prediction with lstm

**Spec:**
```
Type:       Machine learning model (time series forecasting)
Features:   - Download daily price history
            - Scale prices and build sliding windows of 60 days
            - Train an LSTM to predict the next day's close
            - Compare with a naive last-value baseline using RMSE
            - Plot predicted vs actual prices on the test period
Input:      Ticker symbol
Tech stack: Python, yfinance, TensorFlow/Keras, scikit-learn
```

---

## Example 214

**Intent:**
analyse our customer support chat logs to find what people ask most

**Spec:**
```
Type:       Data analysis script (topic modelling)
Features:   - Load chat transcripts and keep customer messages
            - Create sentence embeddings
            - Cluster messages into topics with BERTopic
            - Name each topic with its top keywords
            - Show the share of chats per topic per month
Input:      Chat transcripts export
Tech stack: Python, BERTopic, sentence-transformers, pandas
```

---

## Example 215

**Intent:**
monthly board report charts in powerpoint automatically

**Spec:**
```
Type:       Scheduled script (report automation)
Features:   - Query monthly figures from the finance database
            - Create charts for revenue, costs and headcount
            - Fill a PowerPoint template with charts and numbers
            - Add commentary placeholders for the CFO
            - Save the deck to a shared folder at month end
Storage:    SharePoint folder
Tech stack: Python, pandas, matplotlib, python-pptx
```

---

## Example 216

**Intent:**
anomaly detection for website traffic drops

**Spec:**
```
Type:       Machine learning model (anomaly detection)
Features:   - Load hourly sessions per site section
            - Forecast expected traffic with seasonal decomposition
            - Flag hours where actual traffic falls outside the prediction interval
            - Group consecutive anomalies into incidents
            - Alert the team on Slack with a chart
Storage:    BigQuery
Tech stack: Python, statsmodels, pandas, Slack webhook, Cloud Scheduler
```

---

## Example 217

**Intent:**
Hello, my company do the logistics and I want to optimize the routes of delivery trucks using data of the past deliveries, is machine learning possible?

**Spec:**
```
Type:       Data analysis script (route optimisation)
Features:   - Load delivery addresses, time windows and truck capacities
            - Estimate travel times from past delivery GPS data
            - Solve a vehicle routing problem with time windows
            - Compare planned route distance with past routes
            - Export routes per truck to a map and CSV
Input:      Daily deliveries CSV and historical GPS data
Tech stack: Python, Google OR-Tools, pandas, Folium
```

---

## Example 218

**Intent:**
dashboard for my podcast downloads from different platforms

**Spec:**
```
Type:       Data dashboard (media analytics)
Features:   - Import download stats from Spotify, Apple Podcasts and the hosting provider
            - Combine downloads per episode and platform
            - Show downloads in the first 7 and 30 days per episode
            - Show listener countries
            - Show growth month over month
Input:      Platform CSV exports
Tech stack: Python, Streamlit, pandas, Altair
```

---

## Example 219

**Intent:**
generate synthetic data that looks like our customer table for testing

**Spec:**
```
Type:       Machine learning model (synthetic data generation)
Features:   - Learn column distributions and correlations from the real table
            - Train a generative model such as CTGAN
            - Generate any number of synthetic rows
            - Compare real and synthetic data with quality reports
            - Check that no synthetic row copies a real customer
Input:      Customer table CSV
Tech stack: Python, SDV (Synthetic Data Vault)
```

---

## Example 220

**Intent:**
count words in all my documents

**Spec:**
```
Type:       Command-line script (text statistics)
Features:   - Read all .txt, .md and .docx files in a folder
            - Count words per file
            - Show total words and average per file
            - Sort files by word count
            - Save results to a CSV
Input:      Folder path
Tech stack: Python, python-docx
```

---

## Example 221

**Intent:**
wanna build a little ai thing that tells me if my plant needs water from a photo

**Spec:**
```
Type:       Machine learning model (image classification)
Features:   - Collect photos of healthy and wilting plants
            - Fine-tune a small pretrained image model on the two classes
            - Report accuracy on a test set
            - Return "needs water" or "looks fine" with confidence
            - Run in a simple web page that accepts phone photos
Input:      Plant photo
Tech stack: Python, PyTorch, Hugging Face Spaces, Gradio
```

---

## Example 222

**Intent:**
KPI tracking for a call center in tableau

**Spec:**
```
Type:       Data dashboard (call center)
Features:   - Show first call resolution rate, average handle time and CSAT per team
            - Show calls per interval against forecast
            - Show agent leaderboard
            - Show trends per week
            - Filter by queue and team
Storage:    SQL Server
Tech stack: Tableau, SQL Server
```

---

## Example 223

**Intent:**
python script compare two excel files and show differences

**Spec:**
```
Type:       Command-line script (data comparison)
Features:   - Read two Excel files with the same structure
            - Match rows on a key column
            - Find added, removed and changed rows
            - Highlight changed cells in an output Excel file
            - Print a summary of differences
Input:      Two Excel files and the key column name
Tech stack: Python, pandas, openpyxl
```

---

## Example 224

**Intent:**
I need a model for predict the customer lifetime value in our telecom company for the next 2 years

**Spec:**
```
Type:       Machine learning model (customer lifetime value)
Features:   - Build customer features from tenure, plan, monthly spend, usage and support contacts
            - Estimate churn probability with a survival model
            - Predict expected monthly revenue
            - Combine survival and revenue into a 24-month CLV
            - Segment customers by CLV for marketing
Input:      Customer and billing history
Tech stack: Python, lifelines, scikit-learn, pandas
```

---

## Example 225

**Intent:**
ETL from google analytics to our postgres

**Spec:**
```
Type:       Data pipeline (ETL)
Features:   - Request daily reports from the Google Analytics Data API
            - Extract sessions, users, conversions by date, source and page
            - Load results into PostgreSQL tables
            - Re-load the last 3 days to capture late data
            - Run every day at 6:00
Storage:    PostgreSQL
Tech stack: Python, google-analytics-data, psycopg, cron
```

---

## Example 226

**Intent:**
football betting odds value finder

**Spec:**
```
Type:       Data analysis script (sports betting)
Features:   - Load bookmaker odds for upcoming matches
            - Estimate match outcome probabilities with a Poisson goals model
            - Convert odds to implied probabilities without the margin
            - Find bets where model probability exceeds implied probability
            - Track results of past picks
Input:      Historical results and odds CSVs
Tech stack: Python, pandas, SciPy, statsmodels
```

---

## Example 227

**Intent:**
a chatbot for our university that helps students find courses

**Spec:**
```
Type:       Chatbot (course advisor)
Features:   - Answer questions about courses using the course catalog
            - Filter courses by credits, semester and prerequisites
            - Recommend courses based on the student's interests
            - Explain prerequisites and schedules
            - Link to the official course page
Input:      Course catalog JSON
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, pgvector, OpenAI API, React
```

---

## Example 228

**Intent:**
detect potholes from dashcam video

**Spec:**
```
Type:       Machine learning model (object detection)
Features:   - Extract frames from dashcam videos
            - Label potholes with bounding boxes
            - Train an object detection model
            - Attach GPS coordinates to each detection
            - Export detected potholes to a map layer
Input:      Dashcam video with GPS track
Storage:    GeoJSON file
Tech stack: Python, Ultralytics YOLOv8, OpenCV, GeoPandas
```

---

## Example 229

**Intent:**
R script to make survival curves for cancer patients

**Spec:**
```
Type:       Data analysis script (survival analysis)
Features:   - Load patient follow-up times and event status
            - Draw Kaplan-Meier curves by treatment group
            - Compare groups with a log-rank test
            - Fit a Cox proportional hazards model with covariates
            - Check the proportional hazards assumption
Input:      Patient data CSV
Tech stack: R, survival, survminer
```

---

## Example 230

**Intent:**
inventory dashboard that shows low stock items

**Spec:**
```
Type:       Data dashboard (inventory)
Features:   - Load current stock levels and reorder points
            - Show items below reorder point
            - Show days of stock left based on average daily sales
            - Show stock value per category
            - Filter by warehouse
Storage:    MySQL
Tech stack: Metabase, MySQL
```

---

## Example 231

**Intent:**
I'm a journalist and I got 2,000 pages of leaked PDFs. I need to search them, find names and see who is connected to whom.

**Spec:**
```
Type:       Data pipeline (document investigation)
Features:   - Extract text from PDFs with OCR for scanned pages
            - Index all text for full-text search
            - Extract people, organisations and places with named entity recognition
            - Build a co-occurrence network of entities
            - Show the network in an interactive graph viewer
Input:      Folder of PDF documents
Storage:    Elasticsearch
Tech stack: Python, Tesseract OCR, spaCy, Elasticsearch, NetworkX, Gephi
```

---

## Example 232

**Intent:**
a model that writes product descriptions from specs

**Spec:**
```
Type:       Web application (LLM content generation)
Features:   - Upload a CSV of product attributes
            - Generate a description per product with an LLM and a style guide prompt
            - Keep length and tone consistent
            - Let editors approve or regenerate each description
            - Export approved descriptions to CSV
Input:      Product attributes CSV
Storage:    SQLite
Tech stack: Python, Streamlit, Anthropic Claude API, pandas
```

---

## Example 233

**Intent:**
track website uptime and response time and make graphs

**Spec:**
```
Type:       Scheduled script (monitoring)
Features:   - Request a list of URLs every minute
            - Record status code and response time
            - Calculate uptime percentage per day
            - Plot response times over the last 7 days
            - Send an email when a site is down 3 times in a row
Storage:    SQLite
Tech stack: Python, requests, matplotlib, APScheduler
```

---

## Example 234

**Intent:**
Excel VBA to clean customer list: trim spaces, fix capitals, remove duplicates

**Spec:**
```
Type:       Plugin (Excel VBA macro)
Features:   - Trim leading and trailing spaces in all text cells
            - Convert names to proper case
            - Format phone numbers consistently
            - Remove duplicate rows based on email
            - Report the number of changes in a message box
Input:      Customer list worksheet
Tech stack: Excel, VBA
```

---

## Example 235

**Intent:**
crowd counting from camera for a shopping mall

**Spec:**
```
Type:       Machine learning model (crowd counting)
Features:   - Read frames from mall cameras every minute
            - Estimate people count with a density map model
            - Aggregate counts per zone and hour
            - Show occupancy trends on a dashboard
            - Alert when a zone is over capacity
Storage:    TimescaleDB
Tech stack: Python, PyTorch (CSRNet), OpenCV, Grafana
```

---

## Example 236

**Intent:**
i want to forecast my monthly expenses

**Spec:**
```
Type:       Data analysis script (personal finance forecasting)
Features:   - Load past monthly spending per category
            - Calculate average and trend per category
            - Forecast next month per category with a moving average
            - Add known upcoming expenses
            - Show forecast vs budget
Input:      Monthly expenses CSV
Tech stack: Python, pandas
```

---

## Example 237

**Intent:**
a quality check pipeline for our data warehouse tables using great expectations

**Spec:**
```
Type:       Data pipeline (data quality)
Features:   - Define expectations for nulls, uniqueness, ranges and allowed values per table
            - Run checks after each nightly load
            - Stop downstream jobs when a critical check fails
            - Publish a data docs report with results
            - Send failures to Slack
Storage:    Snowflake
Tech stack: Great Expectations, Apache Airflow, Snowflake, Slack webhook
```

---

## Example 238

**Intent:**
tell me what our competitors are posting on linkedin and summarise

**Spec:**
```
Type:       Scheduled script (LLM competitive monitoring)
Features:   - Collect recent public posts from a list of competitor company pages
            - Store posts with dates and engagement
            - Summarise themes and announcements each week with an LLM
            - Compare posting frequency between competitors
            - Email the weekly summary
Storage:    SQLite
Tech stack: Python, Apify (LinkedIn scraper), OpenAI API, pandas
```

---

## Example 239

**Intent:**
OCR for receipts to track my expenses

**Spec:**
```
Type:       Mobile application (receipt scanning)
Features:   - Take a photo of a receipt
            - Extract store name, date, total and tax with OCR
            - Let the user correct extracted fields
            - Assign a category
            - Show monthly totals per category
Storage:    Local SQLite on device
Tech stack: Flutter, Google ML Kit (text recognition)
```

---

## Example 240

**Intent:**
forecast solar panel power for tomorrow

**Spec:**
```
Type:       Machine learning model (forecasting)
Features:   - Combine past inverter output with weather data (irradiance, cloud cover, temperature)
            - Add sun position features for each hour
            - Train a gradient boosting model
            - Forecast hourly power for the next day from the weather forecast
            - Compare forecast and actual output daily
Input:      Inverter export CSV, weather API
Tech stack: Python, pvlib, LightGBM, Open-Meteo API
```

---

## Example 241

**Intent:**
check if survey answers differ between age groups statisticaly

**Spec:**
```
Type:       Data analysis script (statistical testing)
Features:   - Load survey responses and age groups
            - Run chi-square tests for categorical questions
            - Run Kruskal-Wallis tests for rating questions
            - Correct p-values for multiple comparisons
            - Report significant differences in a table
Input:      Survey responses CSV
Tech stack: Python, pandas, SciPy, statsmodels
```

---

## Example 242

**Intent:**
snowflake cost dashboard

**Spec:**
```
Type:       Data dashboard (cloud cost)
Features:   - Query warehouse credit usage from Snowflake account usage views
            - Show daily credits per warehouse
            - Show the most expensive queries and users
            - Show storage costs over time
            - Alert when daily credits exceed a budget
Storage:    Snowflake
Tech stack: Streamlit in Snowflake, SQL
```

---

## Example 243

**Intent:**
im studying for data science interview, make me a project predicting heart disease

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load the UCI heart disease dataset
            - Explore features and handle missing values
            - Train logistic regression, random forest and SVM with cross-validation
            - Compare models with ROC AUC, recall and F1
            - Explain the best model with feature importance
Input:      Heart disease CSV
Tech stack: Python, Jupyter, scikit-learn, pandas, seaborn
```

---

## Example 244

**Intent:**
show where the customers drop off on our checkout page

**Spec:**
```
Type:       Data analysis script (funnel analysis)
Features:   - Load checkout events (cart, shipping, payment, confirmation)
            - Count users reaching each step per day
            - Calculate drop-off rate between steps
            - Compare drop-off by device and browser
            - Plot the funnel
Input:      Event logs from the web analytics tool
Tech stack: Python, pandas, Plotly
```

---

## Example 245

**Intent:**
can i use AI to detect plagiarism in student code assignments

**Spec:**
```
Type:       Command-line tool (code similarity)
Features:   - Read all submissions from a folder
            - Normalise code by removing comments and renaming variables
            - Compare submissions pairwise with token-based similarity
            - Create code embeddings to catch rewritten logic
            - Report the most similar pairs with highlighted matching parts
Input:      Folder of student submissions
Tech stack: Python, tree-sitter, CodeBERT embeddings, scikit-learn
```

---

## Example 246

**Intent:**
pipeline that takes our iot sensor stream into a time series database

**Spec:**
```
Type:       Data pipeline (IoT ingestion)
Features:   - Subscribe to sensor messages on MQTT topics
            - Parse and validate readings
            - Write readings to a time series database in batches
            - Downsample old data to hourly averages
            - Alert when a sensor stops sending data
Storage:    InfluxDB
Tech stack: Telegraf, Mosquitto MQTT, InfluxDB, Grafana
```

---

## Example 247

**Intent:**
an AI tutor for kids that helps with math homework and adapts the difficulty

**Spec:**
```
Type:       Chatbot (adaptive tutoring)
Auth:       Parent account with child profiles
Data model: Child(id, parent_id, name, grade)
            Attempt(id, child_id -> Child, topic, question, correct, created_at)
Features:   - Generate math problems for the child's grade and topic
            - Give hints step by step instead of answers
            - Raise or lower difficulty based on recent answers
            - Show the parent progress per topic
            - Filter content to be safe for children
Storage:    PostgreSQL
Tech stack: Python, FastAPI, OpenAI API, React Native
```

---

## Example 248

**Intent:**
need sumthing to predict if our wine customers will order again b4 xmas

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Build customer features from past orders, last Christmas purchases and newsletter clicks
            - Label customers who ordered in the December period last year
            - Train a logistic regression model
            - Report ROC AUC on a holdout set
            - Export a ranked list of customers for a pre-Christmas campaign
Input:      Orders and newsletter CSV exports
Tech stack: Python, pandas, scikit-learn
```

---

## Example 249

**Intent:**
i have like 300 pdf research papers and want to ask questions across all of them

**Spec:**
```
Type:       Chatbot (research paper Q&A)
Features:   - Extract text and sections from each PDF
            - Chunk papers and create embeddings
            - Retrieve relevant chunks across all papers for a question
            - Generate an answer citing paper titles and pages
            - Compare what different papers say about a topic
Input:      Folder of PDF papers
Storage:    LanceDB (local vector database)
Tech stack: Python, PyMuPDF, LlamaIndex, LanceDB, Anthropic Claude API
```

---

## Example 250

**Intent:**
Hi, I manage a chain of 12 pharmacies. Every morning I look at yesterday's sales per pharmacy in three different programs. Can I get one screen that shows everything, including which medicines are close to running out?

**Spec:**
```
Type:       Data dashboard (retail operations)
Features:   - Load yesterday's sales per pharmacy from the POS database every night
            - Show revenue and transactions per pharmacy compared with the same day last week
            - Show stock levels and days of cover per medicine
            - Highlight medicines with less than 3 days of stock
            - Filter by pharmacy and product group
Storage:    PostgreSQL (reporting copy)
Tech stack: Power BI, PostgreSQL, Python (nightly sync)
```

---

## Example 251

**Intent:**
object tracking for counting people walking in and out a door

**Spec:**
```
Type:       Machine learning model (people counting)
Features:   - Detect people in each frame of the door camera
            - Track each person across frames
            - Count crossings of a virtual line in each direction
            - Store hourly in and out counts
            - Show current occupancy
Input:      Camera video stream
Storage:    SQLite
Tech stack: Python, Ultralytics YOLOv8, ByteTrack, OpenCV
```

---

## Example 252

**Intent:**
hourly etl of orders from shopify to bigquery

**Spec:**
```
Type:       Data pipeline (ETL)
Features:   - Fetch orders updated since the last run through the Shopify Admin API
            - Flatten line items into a separate table
            - Load orders and line items into BigQuery
            - Deduplicate on order id keeping the latest version
            - Run every hour on a schedule
Storage:    BigQuery
Tech stack: Python, Cloud Functions, Cloud Scheduler, Shopify Admin API
```

---

## Example 253

**Intent:**
model that classifies x-ray images of welds as good or bad

**Spec:**
```
Type:       Machine learning model (image classification)
Features:   - Load labelled weld radiographs
            - Normalise and crop images to the weld area
            - Fine-tune a pretrained ResNet
            - Report recall on defective welds and false alarm rate
            - Show heatmaps of the suspected defect area
Input:      Weld X-ray images
Tech stack: Python, PyTorch, torchvision, pytorch-grad-cam
```

---

## Example 254

**Intent:**
ok so our survey has open text answers and there are 5000 of them and nobody wants to read them. can AI group them by theme and count

**Spec:**
```
Type:       Data analysis script (LLM text coding)
Features:   - Load open-text survey answers
            - Ask an LLM to propose a theme list from a sample of answers
            - Assign each answer to one or more themes with an LLM
            - Count answers per theme and pick example quotes
            - Export a theme table and quotes to Excel
Input:      Survey answers Excel file
Tech stack: Python, pandas, OpenAI API, openpyxl
```

---

## Example 255

**Intent:**
compare prices of houses before and after the new train station opened

**Spec:**
```
Type:       Data analysis script (difference-in-differences)
Features:   - Load house sales with dates and coordinates
            - Mark houses within 1 km of the station as treated
            - Compare price changes of treated and control areas before and after opening
            - Fit a difference-in-differences regression with house controls
            - Plot average price per quarter for both groups
Input:      House sales CSV
Tech stack: Python, pandas, GeoPandas, statsmodels
```

---

## Example 256

**Intent:**
in tableau make a map of our store sales by state

**Spec:**
```
Type:       Data dashboard (geographic sales)
Features:   - Connect to the store sales data
            - Show a filled map of sales by state
            - Show sales per store as sized points
            - Add a tooltip with revenue, growth and store count
            - Filter by year and product category
Input:      Store sales table with state and city
Tech stack: Tableau Desktop
```

---

## Example 257

**Intent:**
alert me when someone logs in from a weird location

**Spec:**
```
Type:       Machine learning model (anomaly detection)
Features:   - Collect login events with IP address, geolocation, device and time
            - Build a profile of usual locations and devices per user
            - Score new logins by distance from usual locations and impossible travel speed
            - Flag high-scoring logins
            - Send an alert to the security team
Input:      Authentication logs
Storage:    Elasticsearch
Tech stack: Python, MaxMind GeoIP2, scikit-learn, Elasticsearch
```

---

## Example 258

**Intent:**
dashboard in grafana for my home solar and battery

**Spec:**
```
Type:       Data dashboard (home energy)
Features:   - Collect solar production, battery level and grid import every minute
            - Show live power flows
            - Show daily production and self-consumption
            - Show battery charge history
            - Show money saved per month
Storage:    InfluxDB
Tech stack: Grafana, InfluxDB, Home Assistant
```

---

## Example 259

**Intent:**
please make a model what can read car number plates from camera

**Spec:**
```
Type:       Machine learning model (license plate recognition)
Features:   - Detect license plates in camera frames with an object detection model
            - Crop and straighten each plate
            - Read characters with an OCR model
            - Validate the text against the plate format
            - Log plate numbers with time and camera
Input:      Camera images or video stream
Storage:    PostgreSQL
Tech stack: Python, Ultralytics YOLOv8, PaddleOCR, OpenCV
```

---

## Example 260

**Intent:**
an llm agent that answers questions using our internal APIs

**Spec:**
```
Type:       Chatbot (tool-using agent)
Auth:       Company single sign-on
Features:   - Describe internal API endpoints as tools for the LLM
            - Let the LLM choose and call tools to get order, customer and inventory data
            - Combine tool results into an answer
            - Ask for confirmation before any action that changes data
            - Log every tool call
Storage:    PostgreSQL (conversation and tool logs)
Tech stack: Python, Anthropic Claude API (tool use), FastAPI, React
```

---

## Example 261

**Intent:**
customer segmentation with RFM in excel

**Spec:**
```
Type:       Data analysis script (RFM segmentation)
Features:   - Calculate recency, frequency and monetary value per customer with pivot tables
            - Score each metric into quintiles with PERCENTRANK
            - Combine scores into RFM segments such as champions and at risk
            - Count customers and revenue per segment
            - Chart segment sizes
Input:      Orders sheet
Tech stack: Microsoft Excel (pivot tables, formulas)
```

---

## Example 262

**Intent:**
whats the best model to predict if a flight will be delayed

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load historical flight records with airline, airports, scheduled time and weather
            - Label flights delayed by more than 15 minutes
            - Encode categorical features with target encoding
            - Train a gradient boosting classifier with time-based validation
            - Report ROC AUC, precision and recall
Input:      Flight records CSV
Tech stack: Python, pandas, CatBoost
```

---

## Example 263

**Intent:**
crawl reddit wallstreetbets and see which stocks are hyped

**Spec:**
```
Type:       Data analysis script (social sentiment)
Features:   - Collect posts and comments from the subreddit
            - Extract stock tickers mentioned in each text
            - Count mentions per ticker per day
            - Score sentiment of each mention
            - Show the top mentioned tickers with sentiment
Tech stack: Python, PRAW, pandas, VADER
```

---

## Example 264

**Intent:**
For my master thesis I collected EMG muscle signals from 20 participants doing 6 hand gestures and want to classify the gesture from the signal.

**Spec:**
```
Type:       Machine learning model (signal classification)
Features:   - Filter raw EMG signals and segment them into windows
            - Extract time-domain and frequency-domain features per channel
            - Train SVM and random forest classifiers
            - Evaluate with leave-one-subject-out cross-validation
            - Report accuracy and confusion matrix per gesture
Input:      EMG recordings with gesture labels
Tech stack: Python, SciPy, scikit-learn, NumPy
```

---

## Example 265

**Intent:**
chatbot for my restaurant that takes table reservations

**Spec:**
```
Type:       Chatbot (reservations)
Data model: Table(id, seats)
            Reservation(id, table_id -> Table, name, phone, party_size, datetime)
Features:   - Understand reservation requests in natural language
            - Check table availability for the date, time and party size
            - Confirm the booking and save it
            - Change or cancel an existing reservation
            - Answer questions about opening hours and menu
Storage:    PostgreSQL
Tech stack: Python, FastAPI, OpenAI API (function calling), WhatsApp Business API
```

---

## Example 266

**Intent:**
realtime fraud scoring for online payments

**Spec:**
```
Type:       REST API service (real-time ML scoring)
Features:   - Receive payment events with card, device, IP and amount
            - Look up streaming features such as transactions per card in the last hour
            - Score the payment with a trained gradient boosting model in under 50 ms
            - Return approve, review or decline
            - Store scores and outcomes for retraining
API:        REST
            POST /score
Storage:    Redis (feature store), PostgreSQL (score log)
Tech stack: Python, FastAPI, XGBoost, Redis, Feast
```

---

## Example 267

**Intent:**
polars script to aggregate big csv of sales

**Spec:**
```
Type:       Data analysis script (large data aggregation)
Features:   - Scan large CSV files lazily
            - Filter by date range
            - Aggregate revenue and units by product and month
            - Join product categories
            - Write results to Parquet and CSV
Input:      Large sales CSV files
Tech stack: Python, Polars
```

---

## Example 268

**Intent:**
i want an ai to read my emails every morning and tell me which are important

**Spec:**
```
Type:       Scheduled script (LLM email triage)
Features:   - Fetch unread emails from the last 24 hours through the Gmail API
            - Classify each email as urgent, important, newsletter or ignore with an LLM
            - Summarise urgent and important emails in one line each
            - Send the digest to the user at 7:00
            - Learn from emails the user marks as wrongly classified
Storage:    SQLite (feedback)
Tech stack: Python, Gmail API, OpenAI API, cron
```

---

## Example 269

**Intent:**
scientific data: process mass spectrometry files and find peaks

**Spec:**
```
Type:       Data analysis script (analytical chemistry)
Features:   - Read mzML mass spectrometry files
            - Smooth spectra and subtract the baseline
            - Detect peaks with intensity and m/z
            - Match peaks to a compound library within a tolerance
            - Export peak tables per sample
Input:      Folder of mzML files
Tech stack: Python, pyOpenMS, NumPy, pandas
```

---

## Example 270

**Intent:**
dashbord that shows how our ads perform on tiktok and insta

**Spec:**
```
Type:       Data dashboard (marketing)
Features:   - Pull daily spend, impressions, clicks and conversions from TikTok Ads and Meta Ads
            - Combine into one table by campaign and platform
            - Show cost per acquisition and ROAS per platform
            - Show trends per day
            - Filter by campaign and date
Storage:    Google BigQuery
Tech stack: Supermetrics, BigQuery, Looker Studio
```

---

## Example 271

**Intent:**
model to tell apart cats and dogs for learning deep learning

**Spec:**
```
Type:       Machine learning model (image classification)
Features:   - Load the cats vs dogs image dataset
            - Split into train, validation and test sets
            - Train a small CNN from scratch
            - Compare with transfer learning from a pretrained model
            - Plot accuracy and loss curves
Input:      Folder of cat and dog images
Tech stack: Python, TensorFlow, Keras
```

---

## Example 272

**Intent:**
data pipeline for our clinic appointments into a dashboard, must be gdpr compliant

**Spec:**
```
Type:       Data pipeline (ETL with privacy controls)
Features:   - Extract appointments from the clinic system daily
            - Remove direct identifiers and replace patient ids with pseudonyms
            - Aggregate appointments, no-shows and wait times per clinic
            - Load aggregates into a reporting database in the EU
            - Restrict access to the reporting database by role
Storage:    PostgreSQL (EU region)
Tech stack: Python, dbt, PostgreSQL, Metabase
```

---

## Example 273

**Intent:**
forecast how much we will spend on aws next month

**Spec:**
```
Type:       Data analysis script (cost forecasting)
Features:   - Fetch daily costs per service from AWS Cost Explorer
            - Forecast month-end spend with a linear trend on the current month
            - Compare with budget and last month
            - Show the services with the biggest increases
            - Post a summary to Slack every Monday
Tech stack: Python, boto3, pandas, Slack webhook
```

---

## Example 274

**Intent:**
recommendations for which product to show next in our email newsletter

**Spec:**
```
Type:       Machine learning model (recommendation)
Features:   - Build user-product interactions from purchases, views and email clicks
            - Train a LightFM hybrid model with product features
            - Generate top 4 products per subscriber before each send
            - Exclude already purchased products
            - Measure click-through uplift with an A/B test
Storage:    PostgreSQL
Tech stack: Python, LightFM, pandas, Mailchimp API
```

---

## Example 275

**Intent:**
what is our nps by country and is it improving

**Spec:**
```
Type:       Data analysis script (NPS)
Features:   - Load survey scores with country and date
            - Classify respondents as promoters, passives and detractors
            - Calculate NPS per country per quarter
            - Add confidence intervals with bootstrapping
            - Plot NPS trend per country
Input:      NPS survey export
Tech stack: Python, pandas, NumPy, matplotlib
```

---

## Example 276

**Intent:**
hey so im a nurse and we have to fill out these fall risk forms for every patient and i was thinking could AI look at the patient record and predict who will fall? we have like 5 years of incident reports

**Spec:**
```
Type:       Machine learning model (clinical risk prediction)
Features:   - Combine patient records (age, diagnoses, medications, mobility scores) with fall incident reports
            - Label admissions with a recorded fall
            - Train an interpretable logistic regression and a gradient boosting model
            - Report sensitivity and specificity compared with the current fall risk score
            - Show the main risk factors behind each prediction
Input:      Patient records and incident reports export
Tech stack: Python, pandas, scikit-learn, SHAP
```

---

## Example 277

**Intent:**
script to convert json api responses into a flat table

**Spec:**
```
Type:       Command-line script (data transformation)
Features:   - Read JSON files from a folder
            - Flatten nested objects into dotted column names
            - Explode arrays into separate rows
            - Combine all files into one table
            - Write the result as CSV or Parquet
Input:      Folder of JSON files
Tech stack: Python, pandas (json_normalize), pyarrow
```

---

## Example 278

**Intent:**
Could you build a tool that checks the answers of our customer service chatbot for wrong information?

**Spec:**
```
Type:       Data analysis script (LLM evaluation)
Features:   - Load chatbot conversations and the knowledge base
            - Ask a judge LLM whether each answer is supported by the knowledge base
            - Score answers for correctness and helpfulness
            - Flag unsupported claims with the conversation link
            - Report the hallucination rate per week
Input:      Chatbot conversation logs, knowledge base articles
Tech stack: Python, Anthropic Claude API, pandas
```

---

## Example 279

**Intent:**
weekly dashboard of gym attendance

**Spec:**
```
Type:       Data dashboard (fitness)
Features:   - Load check-in records
            - Show check-ins per day and hour heatmap
            - Show attendance per class
            - Show active member count per week
            - Compare with the same week last year
Input:      Check-in CSV export
Tech stack: Google Looker Studio, Google Sheets
```

---

## Example 280

**Intent:**
dataflow to read pubsub events and write aggregated metrics to bigquery

**Spec:**
```
Type:       Data pipeline (streaming)
Features:   - Read app events from a Pub/Sub subscription
            - Parse and validate event JSON
            - Aggregate events per type in 1-minute windows
            - Handle late events with watermarks
            - Write aggregated metrics to BigQuery
Storage:    BigQuery
Tech stack: Apache Beam (Python), Google Cloud Dataflow, Pub/Sub
```

---

## Example 281

**Intent:**
ai that suggest tags for my blog posts

**Spec:**
```
Type:       Machine learning model (multi-label classification)
Features:   - Load past posts with their tags
            - Create embeddings for each post
            - Train a multi-label classifier on the embeddings
            - Suggest the top 5 tags with scores for a new post
            - Evaluate with micro F1 on a test set
Input:      Blog post text
Tech stack: Python, sentence-transformers, scikit-learn
```

---

## Example 282

**Intent:**
i got temperature data from 200 weather stations over 30 yrs need to make a map of warming trend

**Spec:**
```
Type:       Data analysis script (spatial climate analysis)
Features:   - Load daily station temperatures and station coordinates
            - Calculate yearly averages per station
            - Fit a linear trend per station and keep stations with enough data
            - Interpolate trends onto a grid with kriging
            - Draw a map of warming per decade
Input:      Station data CSVs and station list
Tech stack: Python, pandas, PyKrige, Cartopy, matplotlib
```

---

## Example 283

**Intent:**
llm bot for slack that answers HR policy questions

**Spec:**
```
Type:       Bot (Slack, document Q&A)
Features:   - Index HR policy documents from Google Drive
            - Answer questions in direct messages using retrieved policy text
            - Cite the policy name and section
            - Suggest contacting HR for personal cases
            - Re-index documents every night
Storage:    Pinecone (vector database)
Tech stack: Python, Slack Bolt, Pinecone, OpenAI API, Google Drive API
```

---

## Example 284

**Intent:**
simple linear regression in R for my homework

**Spec:**
```
Type:       Data analysis script (regression)
Features:   - Load the dataset from CSV
            - Plot the two variables as a scatter plot
            - Fit a simple linear regression with lm
            - Show coefficients, R² and p-values
            - Plot residuals to check assumptions
Input:      CSV with two numeric columns
Tech stack: R, ggplot2
```

---

## Example 285

**Intent:**
use ai to translate our product catalog to 5 languages and keep terms consistent

**Spec:**
```
Type:       Data pipeline (LLM translation)
Features:   - Load the product catalog from CSV
            - Translate titles and descriptions with an LLM into 5 languages
            - Apply a glossary of fixed product terms
            - Check output length and missing placeholders
            - Write translated columns back to the catalog
Input:      Product catalog CSV and glossary
Tech stack: Python, DeepL API, pandas
```

---

## Example 286

**Intent:**
detect if text was written by ai

**Spec:**
```
Type:       Machine learning model (text classification)
Features:   - Collect human-written and AI-generated texts on the same topics
            - Compute perplexity features with a small language model
            - Fine-tune a RoBERTa classifier
            - Evaluate accuracy and false positive rate on unseen sources
            - Return a probability with a warning about uncertainty
Input:      Text passage
Tech stack: Python, Hugging Face Transformers, PyTorch
```

---

## Example 287

**Intent:**
analyse my company's energy bills from different sites

**Spec:**
```
Type:       Data analysis script (energy costs)
Features:   - Load monthly bills per site with kWh and cost
            - Calculate cost per kWh and per square meter
            - Compare sites with each other
            - Show consumption trend per site
            - Flag bills with unusual jumps
Input:      Energy bills spreadsheet
Tech stack: Python, pandas, matplotlib
```

---

## Example 288

**Intent:**
I'd like to build a model in scikit-learn that predicts if a mortgage application gets approved, mainly to learn ML pipelines properly.

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load the loan application dataset
            - Build a scikit-learn Pipeline with imputers, scalers and one-hot encoders
            - Tune hyperparameters with GridSearchCV
            - Evaluate on a test set with ROC AUC and a confusion matrix
            - Save the fitted pipeline with joblib
Input:      Loan applications CSV
Tech stack: Python, scikit-learn, pandas, joblib
```

---

## Example 289

**Intent:**
notebook that compares covid vaccination rates with deaths across countries

**Spec:**
```
Type:       Data analysis script (public health)
Features:   - Download vaccination and mortality data
            - Align countries and dates
            - Calculate deaths per million in each wave
            - Plot vaccination rate against death rate with a regression line
            - Control for age structure with median age
Tech stack: Python, Jupyter, pandas, seaborn, statsmodels
```

---

## Example 290

**Intent:**
show live tweets about our brand on a big screen in the office

**Spec:**
```
Type:       Data dashboard (social media wall)
Features:   - Stream new posts mentioning the brand
            - Filter out offensive content
            - Show posts as cards on a full-screen page
            - Show mention count and sentiment of the last 24 hours
            - Refresh automatically
Tech stack: Node.js, Socket.IO, X API, React
```

---

## Example 291

**Intent:**
we sell on amazon and want to know which keywords bring sales

**Spec:**
```
Type:       Data analysis script (marketplace advertising)
Features:   - Load Amazon Ads search term reports
            - Aggregate spend, clicks, orders and sales per search term
            - Calculate ACOS and conversion rate
            - List search terms with spend but no sales
            - Suggest negative keywords and high-performing keywords
Input:      Amazon Ads search term report
Tech stack: Python, pandas, openpyxl
```

---

## Example 292

**Intent:**
real-time dashboard of our factory line output

**Spec:**
```
Type:       Data dashboard (manufacturing)
Features:   - Read counts of good and rejected parts from PLCs every 10 seconds
            - Show units per hour against target
            - Show reject rate per station
            - Show machine status (running, idle, down)
            - Keep shift history
Storage:    TimescaleDB
Tech stack: Node-RED, OPC UA, TimescaleDB, Grafana
```

---

## Example 293

**Intent:**
chat bot that helps people fill government forms

**Spec:**
```
Type:       Chatbot (form assistant)
Features:   - Explain each form field in plain language
            - Ask the user questions step by step
            - Validate answers such as dates and ID numbers
            - Fill a PDF form with the answers
            - Support several languages
Input:      PDF form template
Tech stack: Python, FastAPI, OpenAI API, pypdf
```

---

## Example 294

**Intent:**
ml for predicting employee attrition in R

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load HR data with tenure, salary, satisfaction and performance
            - Split into train and test sets
            - Train a random forest with tidymodels
            - Report ROC AUC and variable importance
            - Predict attrition probability for current employees
Input:      HR data CSV
Tech stack: R, tidymodels, ranger
```

---

## Example 295

**Intent:**
we have a lot of log data in elastic and want to see trends in errors

**Spec:**
```
Type:       Data dashboard (log analytics)
Features:   - Query error logs from Elasticsearch indices
            - Show error count per service per hour
            - Show top error messages
            - Compare error rate with the previous week
            - Alert when errors spike
Storage:    Elasticsearch
Tech stack: Kibana, Elasticsearch
```

---

## Example 296

**Intent:**
i need a script that downloads tables from wikipedia and saves to csv

**Spec:**
```
Type:       Command-line script (web data extraction)
Features:   - Download a Wikipedia page by URL
            - Find all tables on the page
            - Clean headers and footnote markers
            - Save each table as a separate CSV
            - Print the table names and sizes
Input:      Wikipedia page URL
Tech stack: Python, pandas (read_html), requests
```

---

## Example 297

**Intent:**
ml to tell what kind of waste is in a picture for a recycling bin

**Spec:**
```
Type:       Machine learning model (image classification)
Features:   - Collect images of plastic, paper, glass, metal and general waste
            - Fine-tune a small pretrained CNN
            - Quantise the model to run on a Raspberry Pi
            - Report accuracy per class
            - Light the LED for the right bin
Input:      Camera image
Tech stack: Python, TensorFlow Lite, Raspberry Pi, picamera2
```

---

## Example 298

**Intent:**
Our product managers want to know how long users take from signup to first purchase and what speeds it up.

**Spec:**
```
Type:       Data analysis script (time-to-event)
Features:   - Calculate days from signup to first purchase per user
            - Treat users without a purchase as censored
            - Draw Kaplan-Meier curves by acquisition channel
            - Fit a Cox model with onboarding actions as covariates
            - Report which actions shorten time to purchase
Input:      Users and events tables
Tech stack: Python, lifelines, pandas
```

---

## Example 299

**Intent:**
guess the price of airbnb listings

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Load Inside Airbnb listings for a city
            - Extract features from room type, capacity, amenities, reviews and location
            - Add text features from the listing description
            - Train a LightGBM regressor on log nightly price
            - Report MAE and compare neighbourhoods by residuals
Input:      Inside Airbnb listings CSV
Tech stack: Python, pandas, LightGBM, scikit-learn
```

---

## Example 300

**Intent:**
help me make a dashboard for my freelance hours and income using notion data

**Spec:**
```
Type:       Data dashboard (personal business)
Features:   - Read time entries and invoices from Notion databases through the API
            - Show hours worked per client per week
            - Show income per month and effective hourly rate
            - Show unpaid invoices
            - Refresh on demand
Tech stack: Python, notion-client, Streamlit, pandas
```

---

## Example 301

**Intent:**
model that predicts if a song will be a hit using spotify features

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load tracks with audio features (danceability, energy, tempo, valence)
            - Label tracks that reached the top 100
            - Train a random forest classifier
            - Report F1 score and ROC AUC
            - Show which audio features matter most
Input:      Spotify tracks dataset CSV
Tech stack: Python, pandas, scikit-learn, Spotipy
```

---

## Example 302

**Intent:**
water quality data from river sampling, I need statistics and charts for the yearly report

**Spec:**
```
Type:       Data analysis script (environmental monitoring)
Features:   - Load sampling results per site and parameter
            - Compare each value with legal limit values
            - Calculate yearly mean, min, max and exceedance count per site
            - Test for trends over years with the Mann-Kendall test
            - Produce charts and tables for the report
Input:      Sampling results Excel
Tech stack: Python, pandas, pymannkendall, matplotlib
```

---

## Example 303

**Intent:**
thing that reads my handwritten notes photos and makes them searchable

**Spec:**
```
Type:       Web application (handwriting OCR search)
Features:   - Upload photos of handwritten pages
            - Convert handwriting to text with an OCR model
            - Index the text for full-text and semantic search
            - Show the original photo next to search results
            - Tag pages by notebook and date
Storage:    SQLite with FTS5, local image folder
Tech stack: Python, Flask, Google Cloud Vision API, sentence-transformers
```

---

## Example 304

**Intent:**
churn analysis for our newsletter subscribers

**Spec:**
```
Type:       Data analysis script (subscriber churn)
Features:   - Load subscriber list with signup date, opens and unsubscribe date
            - Calculate monthly unsubscribe rate
            - Compare churn by signup source
            - Show open rate decline before unsubscribing
            - List subscribers with no opens in 90 days
Input:      Newsletter platform export
Tech stack: Python, pandas, matplotlib
```

---

## Example 305

**Intent:**
im doing a hackathon and want to make an app that tells you which bus will be crowded

**Spec:**
```
Type:       Machine learning model (occupancy prediction)
Features:   - Load historical ticket validations per bus trip and stop
            - Aggregate passengers on board per trip segment
            - Train a model using route, time of day, weekday and weather
            - Predict occupancy level (low, medium, high) for upcoming trips
            - Serve predictions through an API for the app
API:        REST
            GET /trips/{id}/crowding
Tech stack: Python, LightGBM, FastAPI
```

---

## Example 306

**Intent:**
monthly ETL that merges data from 3 old databases into one warehouse

**Spec:**
```
Type:       Data pipeline (ETL consolidation)
Features:   - Extract customers, products and orders from three legacy databases
            - Map each source schema to a common model
            - Deduplicate customers across sources
            - Load conformed dimensions and fact tables
            - Write a reconciliation report of row counts per source
Storage:    PostgreSQL (warehouse)
Tech stack: Python, SQLAlchemy, pandas, Prefect
```

---

## Example 307

**Intent:**
forecast hospital bed occupancy

**Spec:**
```
Type:       Machine learning model (forecasting)
Features:   - Calculate daily occupied beds per ward from admissions and discharges
            - Add weekday, holiday and seasonal features
            - Train a forecasting model per ward
            - Forecast occupancy 14 days ahead with intervals
            - Warn when forecast exceeds ward capacity
Input:      Admission and discharge records
Tech stack: Python, statsforecast, pandas
```

---

## Example 308

**Intent:**
make me a python dashboard that pulls our jira tickets and shows sprint progress

**Spec:**
```
Type:       Data dashboard (project analytics)
Features:   - Fetch issues and sprints from the Jira API
            - Show a burndown chart for the active sprint
            - Show velocity over past sprints
            - Show open issues by status and assignee
            - Refresh every 15 minutes
Tech stack: Python, Plotly Dash, Jira REST API
```

---

## Example 309

**Intent:**
does our discount campaign really increase sales or just move them

**Spec:**
```
Type:       Data analysis script (causal impact)
Features:   - Load daily sales of products in and out of the campaign
            - Use non-campaign products as control series
            - Estimate campaign effect with Bayesian structural time series
            - Check for sales dips after the campaign
            - Report incremental revenue with a credible interval
Input:      Daily sales CSV
Tech stack: Python, tfcausalimpact, pandas
```

---

## Example 310

**Intent:**
question answering bot for our software API docs

**Spec:**
```
Type:       Chatbot (developer documentation)
Features:   - Crawl the API documentation site
            - Chunk pages keeping code blocks intact
            - Retrieve relevant sections and generate answers with code examples
            - Link to the source page
            - Collect thumbs up and down feedback
Storage:    Weaviate (vector database)
Tech stack: Python, LlamaIndex, Weaviate, OpenAI API, Next.js
```

---

## Example 311

**Intent:**
estimate how much cars will sell next quarter in each country we export to

**Spec:**
```
Type:       Machine learning model (forecasting)
Features:   - Collect quarterly sales per country with GDP, fuel price and interest rate data
            - Train a regression model per country with economic features
            - Backtest on the last 8 quarters
            - Forecast next quarter with scenarios
            - Present results in a table per country
Input:      Sales history and economic indicators
Tech stack: Python, statsmodels, pandas
```

---

## Example 312

**Intent:**
i want to know which of my linkedin posts did best and why

**Spec:**
```
Type:       Data analysis script (content analytics)
Features:   - Load LinkedIn post analytics export
            - Calculate engagement rate per post
            - Compare by post type, length and posting time
            - Find words common in top posts
            - Chart engagement over time
Input:      LinkedIn analytics Excel export
Tech stack: Python, pandas, seaborn
```

---

## Example 313

**Intent:**
I'm a hydrologist and I want to predict river water levels 3 days ahead from upstream gauges and rainfall.

**Spec:**
```
Type:       Machine learning model (hydrological forecasting)
Features:   - Load hourly water levels from upstream and target gauges plus rainfall
            - Create lagged features covering travel times between gauges
            - Train an LSTM for 72-hour ahead forecasts
            - Compare with a persistence baseline using Nash-Sutcliffe efficiency
            - Send warnings when forecast passes flood thresholds
Input:      Gauge and rainfall time series
Tech stack: Python, PyTorch, pandas
```

---

## Example 314

**Intent:**
pls build a pipeline that cleans our crm data every week

**Spec:**
```
Type:       Scheduled script (data quality)
Features:   - Export contacts and companies from the CRM
            - Standardise country names, phone formats and emails
            - Find duplicate contacts with fuzzy matching
            - Merge or flag duplicates
            - Write a weekly report of fixes
Storage:    HubSpot
Tech stack: Python, HubSpot API, RapidFuzz, phonenumbers
```

---

## Example 315

**Intent:**
shiny dashboard for agriculture yields by region

**Spec:**
```
Type:       Data dashboard (R Shiny)
Features:   - Load yields per crop, region and year
            - Show a choropleth map of yield per region
            - Show yield trends per crop
            - Compare regions side by side
            - Download filtered data
Input:      Yield data CSV and region shapefile
Tech stack: R, Shiny, sf, leaflet, ggplot2
```

---

## Example 316

**Intent:**
count how many times words appear in my excel column

**Spec:**
```
Type:       Data analysis script (text frequency)
Features:   - Read a chosen text column from an Excel sheet
            - Split text into words and lowercase them
            - Remove common stop words
            - Count word frequencies
            - Write the top words to a new sheet
Input:      Excel file and column name
Tech stack: Python, pandas, openpyxl
```

---

## Example 317

**Intent:**
we need to predict which insurance claims are fraudulent so investigators look at the right ones first

**Spec:**
```
Type:       Machine learning model (fraud classification)
Features:   - Combine claim details, policy history and claimant network features
            - Label claims confirmed as fraud by investigators
            - Train a gradient boosting model with class weights
            - Evaluate precision in the top 5% of scores
            - Show reason codes for each flagged claim
            - Rank open claims for investigators daily
Input:      Claims and policies database
Storage:    PostgreSQL
Tech stack: Python, XGBoost, SHAP, NetworkX
```

---

## Example 318

**Intent:**
ai detect sarcasm in comments lol

**Spec:**
```
Type:       Machine learning model (text classification)
Features:   - Load a labelled sarcasm dataset
            - Fine-tune a RoBERTa model
            - Evaluate F1 on a test set
            - Predict sarcasm probability for new comments
            - Show examples of wrong predictions
Input:      Comment text
Tech stack: Python, Hugging Face Transformers
```

---

## Example 319

**Intent:**
our team uses dbt and we need a metrics layer so everyone uses same revenue definition

**Spec:**
```
Type:       Data pipeline (semantic layer)
Features:   - Define semantic models for orders and customers
            - Define revenue, active customers and AOV metrics once
            - Expose metrics with dimensions such as date, region and channel
            - Test metric values against finance figures
            - Connect the BI tool to the semantic layer
Storage:    Snowflake
Tech stack: dbt Semantic Layer (MetricFlow), Snowflake
```

---

## Example 320

**Intent:**
track my weight and predict when ill hit my goal

**Spec:**
```
Type:       Data analysis script (personal health)
Features:   - Load daily weight entries
            - Smooth weights with a 7-day moving average
            - Fit a linear trend on the last 4 weeks
            - Estimate the date when the goal weight is reached
            - Plot weights, trend and goal line
Input:      Weight log CSV
Tech stack: Python, pandas, NumPy, matplotlib
```

---

## Example 321

**Intent:**
Could we use machine learning to sort our scanned documents into invoices, contracts, letters and receipts?

**Spec:**
```
Type:       Machine learning model (document classification)
Features:   - OCR scanned documents to text
            - Combine text features and page layout features
            - Train a classifier on labelled examples per document type
            - Report accuracy per type
            - Move each new document to the folder for its type
Input:      Scanned PDF documents
Tech stack: Python, Tesseract OCR, Hugging Face Transformers (LayoutLMv3)
```

---

## Example 322

**Intent:**
report of the most used hashtags in our industry each week

**Spec:**
```
Type:       Scheduled script (social media trends)
Features:   - Collect posts from industry accounts
            - Extract hashtags from each post
            - Count hashtags per week
            - Show rising hashtags compared with last week
            - Email the weekly top 20
Storage:    SQLite
Tech stack: Python, Instaloader, pandas, smtplib
```

---

## Example 323

**Intent:**
rain prediction tomorrow with ml for my weather station

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load years of station readings (pressure, humidity, temperature, wind)
            - Create features such as pressure change over 3 hours
            - Label days followed by rain
            - Train a gradient boosting classifier
            - Report precision and recall for rain days
Input:      Weather station data CSV
Tech stack: Python, pandas, scikit-learn
```

---

## Example 324

**Intent:**
Want a Power BI dashboard on our sales pipeline from Dynamics 365.

**Spec:**
```
Type:       Data dashboard (sales pipeline)
Features:   - Connect to Dynamics 365 opportunities
            - Show pipeline value per stage and owner
            - Show win rate and average deal size
            - Show expected revenue by close month
            - Drill down to individual opportunities
Tech stack: Power BI, Dynamics 365 connector, DAX
```

---

## Example 325

**Intent:**
build vector search for our product catalog so search works even with typos and synonyms

**Spec:**
```
Type:       REST API service (semantic search)
Features:   - Create embeddings for product titles and descriptions
            - Store embeddings in a vector database
            - Combine vector search with keyword search for hybrid ranking
            - Apply filters for category and price
            - Return ranked products for a query
API:        REST
            GET /search?q={query}
Storage:    Elasticsearch (dense vectors and BM25)
Tech stack: Python, sentence-transformers, Elasticsearch, FastAPI
```

---

## Example 326

**Intent:**
my boss gave me 20 years of hurricane data and wants to know if they get stronger

**Spec:**
```
Type:       Data analysis script (climate statistics)
Features:   - Load hurricane tracks with maximum wind speed per storm
            - Calculate counts and average maximum intensity per year
            - Test the trend in intensity with linear regression and Mann-Kendall
            - Compare share of major hurricanes per decade
            - Plot results with trend lines
Input:      Hurricane database CSV (HURDAT2)
Tech stack: Python, pandas, SciPy, matplotlib
```

---

## Example 327

**Intent:**
llm that grades quiz short answers

**Spec:**
```
Type:       Command-line tool (LLM grading)
Features:   - Read questions, model answers and student answers from a CSV
            - Grade each answer with an LLM using a rubric
            - Return a score and short feedback
            - Flag answers where the model is uncertain
            - Write grades back to the CSV
Input:      Answers CSV
Tech stack: Python, Anthropic Claude API, pandas
```

---

## Example 328

**Intent:**
python to scrape house listing every day and see price trend

**Spec:**
```
Type:       Scheduled script (data collection)
Features:   - Scrape listings from a real estate site each day
            - Store listing id, price, size and location with the date
            - Track price changes per listing
            - Calculate median price per square meter per area each week
            - Plot the trend
Storage:    SQLite
Tech stack: Python, Playwright, pandas, matplotlib
```

---

## Example 329

**Intent:**
identify what language is spoken in an audio file

**Spec:**
```
Type:       Machine learning model (spoken language identification)
Features:   - Load audio and resample to 16 kHz
            - Run a pretrained speech model for language identification
            - Return the top 3 languages with probabilities
            - Process all files in a folder
            - Save results to a CSV
Input:      Audio files
Tech stack: Python, SpeechBrain, torchaudio
```

---

## Example 330

**Intent:**
hiii i run a little coffee shop and want to see which drinks sell best at which time of day, my till exports csv

**Spec:**
```
Type:       Data analysis script (sales by time)
Features:   - Load till CSV exports
            - Group sales by drink and hour of day
            - Show the top drinks for morning, afternoon and evening
            - Show a heatmap of sales by weekday and hour
            - Save the charts as images
Input:      Till CSV exports
Tech stack: Python, pandas, seaborn
```

---

## Example 331

**Intent:**
classify customer calls by reason using the transcripts

**Spec:**
```
Type:       Machine learning model (text classification)
Features:   - Load call transcripts with reason labels
            - Clean transcripts and remove agent greetings
            - Fine-tune a transformer classifier
            - Report macro F1 per reason
            - Classify new calls and update reason dashboards
Input:      Call transcripts
Tech stack: Python, Hugging Face Transformers, pandas
```

---

## Example 332

**Intent:**
Our SaaS needs product usage analytics without sending data to google, self-hosted.

**Spec:**
```
Type:       Infrastructure setup (self-hosted analytics)
Features:   - Deploy a self-hosted product analytics server
            - Add the tracking script to the web app
            - Track page views and custom events
            - Build funnels and retention reports
            - Keep all data on our own servers
Storage:    ClickHouse, PostgreSQL
Tech stack: PostHog (self-hosted), Docker Compose
```

---

## Example 333

**Intent:**
pls make python code to read excel with many sheets and combine

**Spec:**
```
Type:       Command-line script (data consolidation)
Features:   - Open an Excel file with many sheets
            - Read every sheet into a table
            - Add a column with the sheet name
            - Combine all sheets into one table
            - Save as a new Excel or CSV file
Input:      Excel workbook
Tech stack: Python, pandas, openpyxl
```

---

## Example 334

**Intent:**
model that recognises sign language letters from webcam

**Spec:**
```
Type:       Machine learning model (gesture recognition)
Features:   - Detect hand landmarks in each webcam frame
            - Use landmark coordinates as features
            - Train a classifier on recorded letters
            - Show the predicted letter live on screen
            - Report accuracy per letter
Input:      Webcam stream
Tech stack: Python, MediaPipe, scikit-learn, OpenCV
```

---

## Example 335

**Intent:**
Every quarter I calculate our carbon footprint by hand from fuel, electricity and travel spreadsheets. I want this automated with a nice summary.

**Spec:**
```
Type:       Data analysis script (carbon accounting)
Features:   - Load fuel, electricity and business travel data
            - Apply emission factors for scope 1, 2 and 3 categories
            - Calculate CO2e per site and category
            - Compare with the previous quarter
            - Generate a summary report with charts
Input:      Activity data spreadsheets and emission factor table
Tech stack: Python, pandas, matplotlib, openpyxl
```

---

## Example 336

**Intent:**
what neighbourhood should i open my bakery in, data analysis

**Spec:**
```
Type:       Data analysis script (location analysis)
Features:   - Load population density, income and foot traffic data per neighbourhood
            - Map existing bakeries from OpenStreetMap
            - Calculate demand and competition scores per area
            - Rank neighbourhoods by a weighted score
            - Show scores on a map
Input:      Census data and OpenStreetMap data
Tech stack: Python, GeoPandas, OSMnx, Folium
```

---

## Example 337

**Intent:**
anomaly detection in our payroll

**Spec:**
```
Type:       Data analysis script (payroll audit)
Features:   - Load monthly payroll per employee
            - Flag pay changes above 20% month over month
            - Find duplicate bank accounts across employees
            - Flag employees paid after their leave date
            - Export exceptions for review
Input:      Payroll exports
Tech stack: Python, pandas
```

---

## Example 338

**Intent:**
deploy our trained model so it retrains automatically when data drifts

**Spec:**
```
Type:       Infrastructure setup (MLOps)
Features:   - Track model versions and metrics in a model registry
            - Monitor input feature drift and prediction quality daily
            - Trigger a retraining pipeline when drift passes a threshold
            - Promote the new model only if it beats the current one
            - Roll back to the previous model with one command
Storage:    MLflow (model registry), S3 (artifacts)
Tech stack: MLflow, Evidently AI, Kubeflow Pipelines, Kubernetes
```

---

## Example 339

**Intent:**
help analyze results of our employee engagement survey per team without revealing individuals

**Spec:**
```
Type:       Data analysis script (anonymised survey reporting)
Features:   - Load survey responses with team codes
            - Hide results for teams with fewer than 5 responses
            - Calculate average scores per question and team
            - Compare each team with the company average
            - Export a report per team manager
Input:      Survey responses CSV
Tech stack: Python, pandas, Jinja2, WeasyPrint
```

---

## Example 340

**Intent:**
an app where i upload a song and it splits vocals and instruments

**Spec:**
```
Type:       Web application (audio source separation)
Features:   - Upload an audio file
            - Separate vocals, drums, bass and other instruments with a pretrained model
            - Play each separated track in the browser
            - Download separated tracks as WAV
            - Process jobs in a background queue
Storage:    Local file storage
Tech stack: Python, Demucs, FastAPI, Celery, Redis
```

---

## Example 341

**Intent:**
script to calculate stats of my students grades per subject

**Spec:**
```
Type:       Data analysis script (education)
Features:   - Load grades per student and subject
            - Calculate average, median and standard deviation per subject
            - Show grade distribution per subject
            - List students below the passing grade
            - Save summary to Excel
Input:      Grades Excel file
Tech stack: Python, pandas, openpyxl
```

---

## Example 342

**Intent:**
i need forecasting of the electricity price for day ahead market

**Spec:**
```
Type:       Machine learning model (price forecasting)
Features:   - Load historical hourly day-ahead prices, load forecasts and wind and solar forecasts
            - Create calendar and lag features
            - Train a gradient boosting model per hour of day
            - Evaluate MAE against a same-hour-last-week baseline
            - Forecast the next day's 24 hourly prices
Input:      ENTSO-E market data
Tech stack: Python, entsoe-py, LightGBM, pandas
```

---

## Example 343

**Intent:**
show me what customers say about each feature in g2 reviews

**Spec:**
```
Type:       Data analysis script (aspect-based sentiment)
Features:   - Load scraped G2 reviews
            - Detect mentions of product features in each review
            - Score sentiment for each feature mention with an LLM
            - Aggregate positive and negative mentions per feature
            - Chart feature sentiment
Input:      Reviews CSV
Tech stack: Python, pandas, OpenAI API, Plotly
```

---

## Example 344

**Intent:**
dashboard for school attendance with alerts for absent kids

**Spec:**
```
Type:       Data dashboard (education)
Auth:       Staff login
Features:   - Import daily attendance from the school system
            - Show attendance rate per class and grade
            - List students below 90% attendance
            - Show chronic absence trend
            - Email form teachers a weekly list of absent students
Storage:    PostgreSQL
Tech stack: Python, Django, Chart.js
```

---

## Example 345

**Intent:**
build a pipeline that converts our old access database to postgres and keeps it updated

**Spec:**
```
Type:       Data pipeline (migration and sync)
Features:   - Read tables from the Microsoft Access database
            - Map Access data types to PostgreSQL types
            - Create tables and load the data
            - Sync changed rows every night
            - Report rows that failed to convert
Storage:    PostgreSQL
Tech stack: Python, pyodbc, SQLAlchemy, Windows Task Scheduler
```

---

## Example 346

**Intent:**
predict the score of the next match in fantasy football for each player

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Load past gameweek points with minutes, opponent strength and home or away
            - Create rolling form features
            - Train a gradient boosting regressor
            - Evaluate MAE per position
            - Predict points for the next gameweek and suggest a team within budget
Input:      Fantasy Premier League API data
Tech stack: Python, pandas, LightGBM, PuLP (team optimisation)
```

---

## Example 347

**Intent:**
a bot that answers questions from our sql database in microsoft teams

**Spec:**
```
Type:       Bot (Microsoft Teams, text-to-SQL)
Auth:       Microsoft Entra ID single sign-on
Features:   - Receive questions in a Teams chat
            - Generate SQL from the question and the schema with an LLM
            - Run only read-only queries with row limits
            - Reply with a table or adaptive card chart
            - Save questions and queries for review
Storage:    Azure SQL Database
Tech stack: Python, Microsoft Bot Framework, Azure OpenAI, pyodbc
```

---

## Example 348

**Intent:**
predict parking spot availability downtown

**Spec:**
```
Type:       Machine learning model (occupancy forecasting)
Features:   - Load parking sensor occupancy per spot every 5 minutes
            - Aggregate occupancy per street block
            - Train a model with time, weekday, event and weather features
            - Predict free spots per block 30 and 60 minutes ahead
            - Serve predictions to the city parking app
API:        REST
            GET /blocks/{id}/availability
Tech stack: Python, LightGBM, FastAPI, PostgreSQL
```

---

## Example 349

**Intent:**
mi jefe quiere un dashboard of the sales by vendor, we use google sheets and data studio

**Spec:**
```
Type:       Data dashboard (sales by salesperson)
Features:   - Connect the sales Google Sheet
            - Show revenue and number of sales per salesperson
            - Show monthly progress against each salesperson's target
            - Rank salespeople
            - Filter by month and region
Input:      Sales Google Sheet
Tech stack: Looker Studio (Data Studio), Google Sheets
```

---

## Example 350

**Intent:**
model to estimate how long a machine part takes to produce

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Load past production jobs with material, dimensions, operations and machine
            - Train a random forest regressor on production time
            - Report MAE in minutes
            - Predict production time for new quotes
            - Show uncertainty ranges with quantile regression
Input:      Production job history
Tech stack: Python, pandas, scikit-learn
```

---

## Example 351

**Intent:**
summarize 1000s of customer feedback forms into a monthly report with ai

**Spec:**
```
Type:       Scheduled script (LLM report)
Features:   - Collect the month's feedback form submissions
            - Classify each into themes and sentiment with an LLM
            - Count themes and pick representative quotes
            - Write a short narrative summary of changes since last month
            - Produce a PDF report
Input:      Feedback forms export
Tech stack: Python, OpenAI API, pandas, ReportLab
```

---

## Example 352

**Intent:**
I am working in a bank and want to check transactions for money laundering patterns like many small deposits

**Spec:**
```
Type:       Data analysis script (AML monitoring)
Features:   - Load account transactions
            - Detect structuring with many cash deposits just below the reporting threshold
            - Flag rapid in-and-out movements of funds
            - Build a graph of transfers to find circular flows
            - Score accounts and export cases for analysts
Input:      Transactions table
Storage:    PostgreSQL
Tech stack: Python, pandas, NetworkX
```

---

## Example 353

**Intent:**
train a yolo model on my own images

**Spec:**
```
Type:       Machine learning model (object detection)
Features:   - Organise labelled images and YOLO-format labels into train and validation folders
            - Write the dataset YAML with class names
            - Fine-tune a pretrained YOLOv8 model
            - Review mAP and per-class precision
            - Export the model to ONNX
Input:      Labelled images
Tech stack: Python, Ultralytics YOLOv8, Roboflow (labelling)
```

---

## Example 354

**Intent:**
ETL job for my school project, from csv files to a star schema in mysql

**Spec:**
```
Type:       Data pipeline (ETL)
Features:   - Read sales CSV files
            - Clean and validate fields
            - Build date, product, store and customer dimension tables
            - Load the sales fact table with foreign keys
            - Write SQL queries to check totals
Storage:    MySQL
Tech stack: Python, pandas, mysql-connector-python
```

---

## Example 355

**Intent:**
dashboard to watch our machine learning model in production

**Spec:**
```
Type:       Data dashboard (model monitoring)
Features:   - Log model inputs and predictions
            - Show prediction volume and latency over time
            - Show data drift per feature compared with training data
            - Show accuracy when true labels arrive
            - Alert when drift or accuracy passes a threshold
Storage:    PostgreSQL
Tech stack: Evidently AI, Grafana, PostgreSQL
```

---

## Example 356

**Intent:**
whats the probability my team wins the league, simulate rest of season

**Spec:**
```
Type:       Data analysis script (Monte Carlo simulation)
Features:   - Load current standings and remaining fixtures
            - Estimate team attack and defence strengths from results
            - Simulate remaining matches 10,000 times with a Poisson model
            - Calculate probability of each finishing position
            - Show a table of title, top 4 and relegation chances
Input:      Results and fixtures CSV
Tech stack: Python, NumPy, pandas
```

---

## Example 357

**Intent:**
help me understand my company data, there is like 30 tables in postgres and nobody documented anything

**Spec:**
```
Type:       Data analysis script (data profiling)
Features:   - Connect to the database and list all tables and columns
            - Profile row counts, null rates and distinct values per column
            - Detect likely foreign key relations from matching column names and values
            - Generate an entity relationship diagram
            - Write a data dictionary to Markdown
Storage:    PostgreSQL
Tech stack: Python, SQLAlchemy, ydata-profiling, ERAlchemy
```

---

## Example 358

**Intent:**
classify bird images from my garden feeder camera

**Spec:**
```
Type:       Machine learning model (image classification)
Features:   - Capture images when motion is detected at the feeder
            - Classify the bird species with a model fine-tuned on local species
            - Ignore frames with no bird
            - Log species and time per visit
            - Show daily species counts
Input:      Feeder camera images
Storage:    SQLite
Tech stack: Python, PyTorch, Raspberry Pi, OpenCV
```

---

## Example 359

**Intent:**
build an llm chatbot that helps our sales team find answers in our product specs and price lists

**Spec:**
```
Type:       Chatbot (sales enablement)
Auth:       Company Google login
Features:   - Index product specs PDFs and price list spreadsheets
            - Answer questions with retrieved specs and prices
            - Compare two products side by side
            - Always show the date of the price list used
            - Admins upload new versions to replace old documents
Storage:    pgvector (PostgreSQL)
Tech stack: Python, LangChain, OpenAI API, pgvector, Streamlit
```

---

## Example 360

**Intent:**
stats on my chess games from lichess

**Spec:**
```
Type:       Data analysis script (game statistics)
Features:   - Download all games for a username from the Lichess API
            - Calculate win, draw and loss rate by color and time control
            - Find the openings with best and worst results
            - Plot rating history
            - Show results by time of day
Input:      Lichess username
Tech stack: Python, python-chess, berserk, pandas
```

---

## Example 361

**Intent:**
i need a model what predict the gold price, for my investing

**Spec:**
```
Type:       Machine learning model (time series forecasting)
Features:   - Download daily gold prices and related series (USD index, interest rates, oil)
            - Create lag and return features
            - Train a gradient boosting model to predict next week's return
            - Backtest with walk-forward validation
            - Report directional accuracy against a buy-and-hold baseline
Input:      Price data from public APIs
Tech stack: Python, yfinance, pandas, XGBoost
```

---

## Example 362

**Intent:**
CSV to charts web tool for my non technical coworkers

**Spec:**
```
Type:       Web application (data visualisation)
Features:   - Upload a CSV file
            - Detect column types
            - Pick chart type and columns from dropdowns
            - Show interactive charts
            - Download charts as PNG
Tech stack: Python, Streamlit, pandas, Plotly
```

---

## Example 363

**Intent:**
the warehouse team scans every package, can we predict how many staff we need per shift next week

**Spec:**
```
Type:       Machine learning model (workload forecasting)
Features:   - Aggregate package scans per shift from scan logs
            - Add incoming order backlog and promotion calendar features
            - Forecast packages per shift for next week
            - Convert packages into staff needed with productivity rates
            - Export the staffing plan
Input:      Scan logs and order data
Tech stack: Python, pandas, LightGBM
```

---

## Example 364

**Intent:**
use machine learning to group similar support articles and find duplicates

**Spec:**
```
Type:       Data analysis script (semantic clustering)
Features:   - Load help center articles
            - Create embeddings for each article
            - Find article pairs with cosine similarity above a threshold
            - Cluster articles into topics
            - Export duplicate candidates and clusters for the content team
Input:      Help center export
Tech stack: Python, sentence-transformers, scikit-learn, pandas
```

---

## Example 365

**Intent:**
R markdown report of monthly sales automatically

**Spec:**
```
Type:       Scheduled script (R reporting)
Features:   - Query monthly sales from the database
            - Calculate totals, growth and top products
            - Create charts with ggplot2
            - Render a parameterised R Markdown report to PDF
            - Email the report on the first day of the month
Storage:    SQL Server
Tech stack: R, R Markdown, DBI, ggplot2, blastula, cron
```

---

## Example 366

**Intent:**
we have drone images of solar farms and want to find broken panels

**Spec:**
```
Type:       Machine learning model (defect detection)
Features:   - Tile thermal drone images into panel-sized crops
            - Label hotspots and cracked panels
            - Train a segmentation model to find defects
            - Map detections to panel ids with GPS
            - Export a list of panels to repair
Input:      Thermal drone images with GPS metadata
Tech stack: Python, PyTorch, segmentation-models-pytorch, rasterio
```

---

## Example 367

**Intent:**
python dashboard for tracking covid in nursing homes

**Spec:**
```
Type:       Data dashboard (public health)
Auth:       Login for health department staff
Features:   - Load weekly case and death reports per facility
            - Show cases per facility over time
            - Show facilities with outbreaks in the last 14 days
            - Show staff vaccination rates
            - Filter by county
Storage:    PostgreSQL
Tech stack: Python, Plotly Dash, dash-auth, pandas
```

---

## Example 368

**Intent:**
Can you make an LLM-based tool that reviews SQL queries written by analysts and suggests improvements?

**Spec:**
```
Type:       Command-line tool (LLM SQL review)
Features:   - Read a SQL file
            - Check the query for common problems with a SQL linter
            - Ask an LLM to suggest performance and readability improvements
            - Show the suggested rewritten query with a diff
            - Run both queries with EXPLAIN to compare costs
Input:      SQL file and database connection
Tech stack: Python, SQLFluff, Anthropic Claude API, psycopg
```

---

## Example 369

**Intent:**
how many visitors will come to the zoo tomorrow

**Spec:**
```
Type:       Machine learning model (forecasting)
Features:   - Load daily visitor counts with weather and school holidays
            - Train a regression model with weekday, holiday and weather features
            - Validate on the last season
            - Forecast tomorrow's visitors from the weather forecast
            - Show forecast in a morning email
Input:      Visitor counts CSV and weather API
Tech stack: Python, scikit-learn, pandas, Open-Meteo API
```

---

## Example 370

**Intent:**
script that checks my csv data against rules before importing

**Spec:**
```
Type:       Command-line script (data validation)
Features:   - Read a CSV file and a rules file
            - Check required columns, data types and allowed values
            - Check unique keys and date ranges
            - Print errors with row numbers
            - Exit with an error code when validation fails
Input:      CSV file and YAML rules file
Tech stack: Python, pandera, PyYAML
```

---

## Example 371

**Intent:**
i want to use AI to tag my music library by genre and mood

**Spec:**
```
Type:       Machine learning model (audio tagging)
Features:   - Scan audio files in the music library
            - Extract audio embeddings with a pretrained music model
            - Predict genre and mood tags
            - Write tags into the file metadata
            - Let the user correct tags
Input:      Music folder (.mp3, .flac)
Tech stack: Python, Essentia (pretrained models), mutagen
```

---

## Example 372

**Intent:**
weekly data pipeline for collecting public procurement tenders

**Spec:**
```
Type:       Data pipeline (web data collection)
Features:   - Fetch new tenders from the public procurement portal API
            - Extract buyer, title, value, deadline and category
            - Store tenders in a database
            - Match tenders against company keywords
            - Email matching tenders each Monday
Storage:    PostgreSQL
Tech stack: Python, requests, SQLAlchemy, GitHub Actions (schedule)
```

---

## Example 373

**Intent:**
tell me which of our job ads get most applicants

**Spec:**
```
Type:       Data analysis script (recruitment analytics)
Features:   - Load job postings and applications from the ATS export
            - Count applicants per posting and per day open
            - Compare by job title, location and salary shown
            - Find words in titles linked with more applicants
            - Chart results
Input:      ATS exports
Tech stack: Python, pandas, seaborn
```

---

## Example 374

**Intent:**
llm that answers parents questions about our kindergarten

**Spec:**
```
Type:       Chatbot (FAQ)
Features:   - Answer questions about opening hours, fees, meals and holidays
            - Use the kindergarten handbook as the only source
            - Reply in the parent's language
            - Refer to staff for questions about specific children
            - Let staff update the handbook text
Input:      Kindergarten handbook
Tech stack: Python, Voiceflow, OpenAI API
```

---

## Example 375

**Intent:**
pytorch lightning project for training on our tabular data

**Spec:**
```
Type:       Machine learning model (tabular deep learning)
Features:   - Load tabular data and encode categorical columns as embeddings
            - Define a LightningDataModule with train, validation and test splits
            - Train an MLP with early stopping
            - Log metrics to TensorBoard
            - Compare with a gradient boosting baseline
Input:      Tabular CSV data
Tech stack: Python, PyTorch Lightning, pandas, TensorBoard
```

---

## Example 376

**Intent:**
hey can i get a heatmap of when our website gets the most signups

**Spec:**
```
Type:       Data analysis script (web analytics)
Features:   - Load signup events with timestamps
            - Convert timestamps to local time
            - Count signups by weekday and hour
            - Draw a heatmap
            - Save it as an image
Input:      Signups CSV
Tech stack: Python, pandas, seaborn
```

---

## Example 377

**Intent:**
genomic variant data, filter and annotate vcf files

**Spec:**
```
Type:       Data pipeline (bioinformatics)
Features:   - Read VCF files per sample
            - Filter variants by quality, depth and allele frequency
            - Annotate variants with gene and predicted effect
            - Merge annotated variants across samples
            - Export a table of candidate variants
Input:      VCF files
Tech stack: Snakemake, bcftools, Ensembl VEP, Python
```

---

## Example 378

**Intent:**
ai tool to read scientific papers and extract the experimental results into a table

**Spec:**
```
Type:       Data pipeline (LLM information extraction)
Features:   - Extract text and tables from paper PDFs
            - Ask an LLM to return materials, conditions and measured values as JSON
            - Validate units and numeric ranges
            - Merge results from all papers into one dataset
            - Keep the source paper and page for each value
Input:      Folder of paper PDFs
Storage:    SQLite
Tech stack: Python, GROBID, Anthropic Claude API, Pydantic
```

---

## Example 379

**Intent:**
dashboard for my online course students progress

**Spec:**
```
Type:       Data dashboard (e-learning)
Features:   - Import lesson completions and quiz scores from the course platform
            - Show completion rate per lesson
            - Show where students stop the course
            - Show quiz score averages
            - List inactive students for follow-up
Input:      Course platform CSV export
Tech stack: Python, Streamlit, pandas
```

---

## Example 380

**Intent:**
predict hotel booking cancellations

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load bookings with lead time, deposit type, channel and special requests
            - Split train and test sets by arrival date
            - Train a gradient boosting classifier
            - Report ROC AUC and precision at a chosen threshold
            - Score upcoming bookings for overbooking decisions
Input:      Hotel bookings dataset
Tech stack: Python, pandas, LightGBM
```

---

## Example 381

**Intent:**
python script that merges survey data with census demographics

**Spec:**
```
Type:       Data analysis script (data integration)
Features:   - Load survey responses with postal codes
            - Download census demographics per postal area
            - Join survey data to demographics
            - Weight responses to match population by age and gender
            - Save the weighted dataset
Input:      Survey CSV
Tech stack: Python, pandas, ipfn (raking weights)
```

---

## Example 382

**Intent:**
anomaly detection in network traffic for our small office

**Spec:**
```
Type:       Machine learning model (network anomaly detection)
Features:   - Capture flow records from the router
            - Aggregate flows per device into features like bytes, ports and destinations
            - Train an Isolation Forest on normal weeks
            - Flag devices with unusual traffic
            - Send an email alert with details
Input:      NetFlow records
Tech stack: Python, nfdump, scikit-learn, pandas
```

---

## Example 383

**Intent:**
get all our app reviews translated and summarized every week

**Spec:**
```
Type:       Scheduled script (LLM review digest)
Features:   - Fetch new App Store and Google Play reviews
            - Translate non-English reviews
            - Summarise top praise and complaints
            - Count reviews by star rating
            - Post the summary to Slack
Tech stack: Python, OpenAI API, google-play-scraper, Slack SDK
```

---

## Example 384

**Intent:**
in jupyter i want to analyse the global temperatures dataset

**Spec:**
```
Type:       Data analysis script (exploratory)
Features:   - Load the global land temperature dataset
            - Calculate yearly averages globally and per country
            - Plot long-term trends with rolling averages
            - Compare warming per continent
            - Show the hottest years
Input:      Global temperatures CSV
Tech stack: Python, Jupyter, pandas, Plotly
```

---

## Example 385

**Intent:**
model to say if a news headline is clickbait

**Spec:**
```
Type:       Machine learning model (text classification)
Features:   - Load labelled clickbait and normal headlines
            - Extract TF-IDF word and character features
            - Train a linear SVM
            - Evaluate accuracy and F1
            - Classify headlines from an RSS feed
Input:      Headline text
Tech stack: Python, scikit-learn
```

---

## Example 386

**Intent:**
we sell subscription boxes, want a dashboard for MRR, churn and LTV

**Spec:**
```
Type:       Data dashboard (subscription metrics)
Features:   - Import subscriptions and payments from Stripe
            - Show MRR, new MRR and churned MRR per month
            - Show customer churn rate
            - Show average lifetime value
            - Show subscribers by plan
Storage:    PostgreSQL
Tech stack: Metabase, PostgreSQL, Stripe API sync script (Python)
```

---

## Example 387

**Intent:**
kids reading app that checks pronunciation with ai

**Spec:**
```
Type:       Mobile application with backend (speech assessment)
Auth:       Parent account with child profiles
Data model: Child(id, parent_id, name, level)
            ReadingAttempt(id, child_id -> Child, text_id, accuracy, recorded_at)
Features:   - Show a short text at the child's level
            - Record the child reading aloud
            - Compare speech with the expected text using speech recognition
            - Highlight mispronounced words
            - Show progress to parents
Storage:    Firebase Firestore
Tech stack: Flutter, Azure AI Speech (pronunciation assessment), Firebase
```

---

## Example 388

**Intent:**
Is there a way to automatically find wrong prices in our product database, like a typo making something 10x cheaper?

**Spec:**
```
Type:       Data analysis script (price anomaly detection)
Features:   - Load product prices with category and cost
            - Compare each price with the category median
            - Flag prices below cost or more than 5x away from similar products
            - Check for decimal shift errors
            - Export suspicious prices for review
Input:      Product catalog export
Tech stack: Python, pandas
```

---

## Example 389

**Intent:**
elt pipeline with fivetran into snowflake for finance

**Spec:**
```
Type:       Data pipeline (ELT)
Features:   - Connect NetSuite, Salesforce and Stripe with managed connectors
            - Load raw data into Snowflake
            - Transform into finance marts with dbt
            - Schedule syncs and transformations every 6 hours
            - Notify on failed syncs
Storage:    Snowflake
Tech stack: Fivetran, Snowflake, dbt Cloud
```

---

## Example 390

**Intent:**
chatbot that recommend recipes from what i have in fridge

**Spec:**
```
Type:       Chatbot (recipe recommendation)
Features:   - Ask the user which ingredients they have
            - Find recipes that use most of the ingredients
            - Suggest substitutions for missing ingredients
            - Respect diet preferences such as vegetarian
            - Give step-by-step cooking instructions
Storage:    PostgreSQL with pgvector (recipes)
Tech stack: Python, FastAPI, OpenAI API, pgvector
```

---

## Example 391

**Intent:**
analyse my strava cycling power data for training zones

**Spec:**
```
Type:       Data analysis script (cycling performance)
Features:   - Load power data from FIT files
            - Estimate functional threshold power from best 20-minute power
            - Calculate time in power zones per ride
            - Calculate training stress score per ride
            - Plot a power duration curve
Input:      Folder of FIT files
Tech stack: Python, fitparse, pandas, matplotlib
```

---

## Example 392

**Intent:**
model that predicts which students will fail the exam early in the semester

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Use first 4 weeks of LMS activity, quiz scores and attendance as features
            - Label students who failed the final exam
            - Train a logistic regression with cross-validation
            - Report recall at a fixed precision
            - Send at-risk lists to tutors
Input:      LMS activity logs and grades
Tech stack: Python, pandas, scikit-learn
```

---

## Example 393

**Intent:**
i want to visualize our org chart data and headcount by level

**Spec:**
```
Type:       Data analysis script (HR visualisation)
Features:   - Load employees with manager id and level
            - Build the reporting tree
            - Draw the org chart as a graph
            - Count headcount per level and department
            - Calculate span of control per manager
Input:      Employee list CSV
Tech stack: Python, pandas, NetworkX, Graphviz
```

---

## Example 394

**Intent:**
an assistant that writes SQL from questions for our analysts, run in notebook

**Spec:**
```
Type:       Data analysis script (LLM text-to-SQL)
Features:   - Load the database schema and column descriptions
            - Generate SQL from a natural language question with an LLM
            - Validate the SQL before running it
            - Run the query and show results as a DataFrame
            - Keep a history of questions and queries
Storage:    BigQuery
Tech stack: Python, Jupyter, Vanna.ai, BigQuery client
```

---

## Example 395

**Intent:**
find best price to sell our products for max profit

**Spec:**
```
Type:       Machine learning model (price optimisation)
Features:   - Estimate price elasticity per product from historical price changes and sales
            - Fit a demand model with price, season and promotion features
            - Simulate profit at different price points
            - Recommend the profit-maximising price within allowed limits
            - Show expected change in sales and profit
Input:      Sales and price history
Tech stack: Python, statsmodels, pandas, SciPy
```

---

## Example 396

**Intent:**
monitor our data pipelines and show freshness of each table

**Spec:**
```
Type:       Data dashboard (data observability)
Features:   - Read the last load time of each warehouse table
            - Compare with the expected update schedule
            - Show tables that are late in red
            - Show row count changes per load
            - Alert the data team on Slack
Storage:    Snowflake
Tech stack: Python, Streamlit, Snowflake connector, Slack webhook
```

---

## Example 397

**Intent:**
i made a survey in typeform and want to analyse it in python

**Spec:**
```
Type:       Data analysis script (survey)
Features:   - Fetch responses from the Typeform API
            - Convert answers into a table with one column per question
            - Summarise multiple choice and rating questions
            - Cross-tab answers by customer type
            - Save charts and a summary CSV
Tech stack: Python, requests, pandas, matplotlib
```

---

## Example 398

**Intent:**
Our call center agents want live suggestions while they talk to a customer, like what to say next.

**Spec:**
```
Type:       Web application (real-time LLM agent assist)
Features:   - Stream call audio to real-time speech-to-text
            - Detect the customer's intent from the live transcript
            - Retrieve matching knowledge base answers
            - Show suggested responses to the agent in a side panel
            - Summarise the call when it ends
Storage:    PostgreSQL, pgvector
Tech stack: Python, Deepgram API, OpenAI API, WebSockets, React
```

---

## Example 399

**Intent:**
python script to compute basic stats of a dataset and print report

**Spec:**
```
Type:       Command-line script (data profiling)
Features:   - Read a CSV or Excel file
            - Print row and column counts
            - Show mean, median, min and max for numeric columns
            - Show top values for text columns
            - Report missing values per column
Input:      Data file path
Tech stack: Python, pandas, argparse
```

---

## Example 400

**Intent:**
deep learning to segment roads from satellite images

**Spec:**
```
Type:       Machine learning model (semantic segmentation)
Features:   - Load satellite image tiles with road masks
            - Train a U-Net with a pretrained encoder
            - Evaluate IoU on validation tiles
            - Predict road masks on new images
            - Convert masks to vector road lines
Input:      Satellite image tiles (GeoTIFF)
Tech stack: Python, PyTorch, segmentation-models-pytorch, rasterio
```

---

## Example 401

**Intent:**
tableau dashboard of our employees training hours and compliance

**Spec:**
```
Type:       Data dashboard (HR compliance)
Features:   - Load training completion records
            - Show completion rate of mandatory courses per department
            - Show expiring certifications in the next 30 days
            - Show training hours per employee
            - Filter by department and course
Input:      LMS training export
Tech stack: Tableau
```

---

## Example 402

**Intent:**
Nightly job that pulls our competitor app rankings from the app store and stores them for trends.

**Spec:**
```
Type:       Scheduled script (data collection)
Features:   - Fetch top chart rankings for chosen categories and countries
            - Find the positions of our app and competitor apps
            - Store rankings with date
            - Plot ranking trends per app
            - Alert when our app drops more than 10 places
Storage:    PostgreSQL
Tech stack: Python, iTunes RSS API, pandas, cron
```

---

## Example 403

**Intent:**
model to detect diseases in cow from milk sensor data

**Spec:**
```
Type:       Machine learning model (animal health classification)
Features:   - Load milking robot data (yield, conductivity, temperature) per cow
            - Create features for changes from each cow's baseline
            - Label days before diagnosed mastitis cases
            - Train a gradient boosting classifier
            - Alert the farmer about cows at risk each day
Input:      Milking robot export
Tech stack: Python, pandas, LightGBM
```

---

## Example 404

**Intent:**
make a word cloud from my company reviews

**Spec:**
```
Type:       Data analysis script (text visualisation)
Features:   - Load review texts
            - Remove stop words and the company name
            - Lemmatise words
            - Generate word clouds for positive and negative reviews
            - Save as images
Input:      Reviews CSV
Tech stack: Python, spaCy, wordcloud
```

---

## Example 405

**Intent:**
ai that predicts what my customers will ask for and pre-writes answers

**Spec:**
```
Type:       Data analysis script (LLM FAQ generation)
Features:   - Load past customer questions from email and chat
            - Cluster similar questions with embeddings
            - Rank clusters by frequency
            - Write a draft answer for each top cluster with an LLM
            - Export a draft FAQ for review
Input:      Customer messages export
Tech stack: Python, sentence-transformers, HDBSCAN, OpenAI API
```

---

## Example 406

**Intent:**
realtime dashboard of website visitors on a map

**Spec:**
```
Type:       Data dashboard (real-time web analytics)
Features:   - Receive page view events from a tracking script
            - Look up visitor location from IP
            - Show active visitors on a world map
            - Show the current top pages
            - Keep counts for the last 30 minutes
Storage:    Redis
Tech stack: Node.js, Socket.IO, Redis, MaxMind GeoLite2, Leaflet
```

---

## Example 407

**Intent:**
sports betting model for nba points total

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Load team game logs with pace, offensive and defensive ratings
            - Create rolling features from the last 10 games
            - Train a regression model to predict total points
            - Compare predictions with bookmaker totals
            - Track model performance against closing lines
Input:      NBA game logs
Tech stack: Python, nba_api, pandas, scikit-learn
```

---

## Example 408

**Intent:**
we got sensor data from wind turbines, want find which turbines underperform

**Spec:**
```
Type:       Data analysis script (wind energy performance)
Features:   - Load 10-minute SCADA data per turbine
            - Filter out curtailment and downtime periods
            - Build the measured power curve per turbine
            - Compare each turbine with the fleet reference curve
            - Rank turbines by lost energy
Input:      SCADA data CSVs
Tech stack: Python, pandas, NumPy, matplotlib
```

---

## Example 409

**Intent:**
knowledge graph from our documents so ai can answer complex questions

**Spec:**
```
Type:       Data pipeline (knowledge graph RAG)
Features:   - Extract entities and relations from documents with an LLM
            - Store entities and relations in a graph database
            - Link mentions of the same entity across documents
            - Answer questions by combining graph queries and text retrieval
            - Show the source documents for each answer
Input:      Company documents
Storage:    Neo4j
Tech stack: Python, Neo4j, LangChain, OpenAI API
```

---

## Example 410

**Intent:**
forecast staffing for our restaurants using sales forecast

**Spec:**
```
Type:       Machine learning model (forecasting)
Features:   - Forecast sales per restaurant per 30-minute slot
            - Convert sales into labour hours with productivity targets
            - Respect minimum staffing rules
            - Build a weekly staffing plan per role
            - Compare planned with actual labour cost
Input:      POS sales history
Tech stack: Python, Prophet, pandas, PuLP
```

---

## Example 411

**Intent:**
give me a script that monitors a google sheet and makes charts when new data comes

**Spec:**
```
Type:       Scheduled script (spreadsheet charts)
Features:   - Read the Google Sheet every 15 minutes
            - Detect new rows since the last check
            - Update summary statistics
            - Regenerate charts
            - Upload charts into a Google Drive folder
Tech stack: Python, gspread, matplotlib, Google Drive API
```

---

## Example 412

**Intent:**
learn which of our emails get opened, subject line analysis

**Spec:**
```
Type:       Data analysis script (email marketing)
Features:   - Load campaign results with subject lines and open rates
            - Extract features like length, emojis, numbers and questions
            - Fit a regression of open rate on the features
            - Find words associated with high open rates
            - Suggest subject line patterns
Input:      Email campaign export
Tech stack: Python, pandas, statsmodels
```

---

## Example 413

**Intent:**
predict the yield of my apple orchard from photos of trees

**Spec:**
```
Type:       Machine learning model (fruit counting)
Features:   - Detect apples in tree photos with an object detection model
            - Count apples per tree and correct for hidden fruit with a calibration factor
            - Estimate yield per row from average apple weight
            - Compare estimates with harvest records
            - Export yield estimates per block
Input:      Tree photos with block and row ids
Tech stack: Python, Ultralytics YOLOv8, pandas
```

---

## Example 414

**Intent:**
lol my group chat argues about who is funniest, can u analyze reactions per person

**Spec:**
```
Type:       Data analysis script (chat statistics)
Features:   - Parse the exported Discord chat JSON
            - Count reactions received per person
            - Calculate reactions per message per person
            - Show the top 10 most reacted messages
            - Plot a leaderboard chart
Input:      Discord chat export JSON
Tech stack: Python, pandas, matplotlib
```

---

## Example 415

**Intent:**
We publish a city magazine and want to know which article topics bring subscribers.

**Spec:**
```
Type:       Data analysis script (content attribution)
Features:   - Join article page views with subscription events per session
            - Tag articles with topics
            - Count subscriptions after reading each topic
            - Calculate conversion rate per topic and author
            - Chart top converting topics
Input:      Analytics events and article metadata
Tech stack: Python, pandas, BigQuery, Plotly
```

---

## Example 416

**Intent:**
pipeline that pulls satellite NDVI for our fields every week

**Spec:**
```
Type:       Data pipeline (remote sensing)
Features:   - Search Sentinel-2 images for each field boundary every week
            - Mask clouds using the scene classification layer
            - Calculate mean NDVI per field
            - Store NDVI time series per field
            - Alert when NDVI drops sharply
Input:      Field boundaries GeoJSON
Storage:    PostGIS
Tech stack: Python, sentinelhub, rasterio, GeoPandas, PostGIS
```

---

## Example 417

**Intent:**
plz model to know if a phone review is about battery, camera or screen

**Spec:**
```
Type:       Machine learning model (multi-label classification)
Features:   - Label a sample of reviews with battery, camera and screen tags
            - Fine-tune a DistilBERT model for multi-label classification
            - Evaluate F1 per label
            - Tag all reviews in the dataset
            - Count tags per phone model
Input:      Phone reviews CSV
Tech stack: Python, Hugging Face Transformers, pandas
```

---

## Example 418

**Intent:**
Sir, I want to analyse the exam result of our 40 schools in district and find which school improve most

**Spec:**
```
Type:       Data analysis script (school performance)
Features:   - Load exam results per school and year
            - Calculate pass rate and average score per school per year
            - Calculate improvement from the first to the last year
            - Rank schools by improvement
            - Plot trends for the top and bottom 5 schools
Input:      Exam results Excel files per year
Tech stack: Python, pandas, matplotlib, openpyxl
```

---

## Example 419

**Intent:**
ai voice bot that answers phone calls for our dental clinic and books appointments

**Spec:**
```
Type:       Chatbot (voice, appointment booking)
Data model: Patient(id, name, phone)
            Appointment(id, patient_id -> Patient, dentist, starts_at, reason)
Features:   - Answer incoming calls with speech recognition and text-to-speech
            - Understand booking, cancelling and rescheduling requests
            - Check free slots in the clinic calendar
            - Confirm the appointment by SMS
            - Transfer the call to reception for emergencies
Storage:    PostgreSQL
Tech stack: Python, Twilio Voice, OpenAI Realtime API, FastAPI
```

---

## Example 420

**Intent:**
bayesian model for estimating conversion rates of small ad groups

**Spec:**
```
Type:       Machine learning model (Bayesian hierarchical model)
Features:   - Load clicks and conversions per ad group
            - Fit a hierarchical beta-binomial model sharing information across groups
            - Estimate each group's conversion rate with credible intervals
            - Rank ad groups by probability of beating the average
            - Plot shrunk vs raw estimates
Input:      Ad groups CSV (clicks, conversions)
Tech stack: Python, PyMC, ArviZ, pandas
```

---

