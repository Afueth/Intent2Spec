## Example 1

**Intent:**
a dotfiles manager for my linux machines

**Spec:**
```
Type:       Command-line tool (dotfiles manager)
Features:   - Keep config files in one git repository under ~/.dotfiles
            - Create symlinks from the repo into the home directory
            - Back up existing files before replacing them with links
            - Show which dotfiles are linked, missing or changed
            - Pull and re-link the latest dotfiles on another machine
Input:      Path to the dotfiles repository and an optional host profile name
Storage:    Git repository, YAML manifest of file mappings
Tech stack: Python, Click, GitPython, PyYAML
```

---

## Example 2

**Intent:**
I keep messing up my ~/.ssh/config file when I add new servers. Can I get a tool that adds and lists hosts for me?

**Spec:**
```
Type:       Command-line tool (SSH config helper)
Features:   - Add a Host entry with hostname, user, port and identity file
            - List all configured hosts in a table
            - Remove or rename a host entry
            - Validate the config and warn about duplicate Host names
            - Back up the config before every change
Input:      Host details as command arguments
Storage:    ~/.ssh/config file
Tech stack: Python, Typer, Rich (tables)
```

---

## Example 3

**Intent:**
check when ssl certs on my websites expire

**Spec:**
```
Type:       Scheduled script (SSL certificate monitor)
Features:   - Connect to each domain on port 443 and read its certificate
            - Calculate the days left until expiry
            - Flag certificates expiring within 21 days
            - Send an email summary of all domains and their expiry dates
Input:      Text file with one domain per line
Tech stack: Python, ssl and socket modules, smtplib, cron
```

---

## Example 4

**Intent:**
hey so i run a small home network with a raspberry pi, a nas and like 6 other devices and i want to see which ports are open on each one so i know nothing is exposed that shouldnt be, only my own network obviously

**Spec:**
```
Type:       Command-line tool (local network port scanner)
Features:   - Discover live hosts on a given subnet with ping sweeps
            - Scan the common TCP ports on each live host
            - Show open ports with the guessed service name
            - Compare the results with the previous scan and highlight new open ports
            - Export the results to a JSON file
Input:      Subnet in CIDR notation (e.g. 192.168.1.0/24)
Storage:    JSON files of past scan results
Tech stack: Python, python-nmap, Rich
```

---

## Example 5

**Intent:**
what is eating my disk space

**Spec:**
```
Type:       Command-line tool (disk usage analyser)
Features:   - Walk a directory tree and total the size of each folder
            - Show the 20 largest folders and files sorted by size
            - Draw a simple bar chart of sizes in the terminal
            - Filter results by file extension
            - Skip mounted network drives
Input:      Starting directory path
Tech stack: Rust, clap, walkdir
```

---

## Example 6

**Intent:**
my music folder has the same songs many times in different formats and names, i want to find the duplicates

**Spec:**
```
Type:       Command-line script (duplicate music finder)
Features:   - Scan a music folder for audio files (.mp3, .flac, .m4a, .ogg)
            - Read artist, title and duration from each file's tags
            - Group tracks with matching tags and duration within 2 seconds
            - Compute audio fingerprints to catch duplicates with wrong tags
            - Write a report listing each duplicate group with file paths and bitrates
Input:      Path to the music library
Tech stack: Python, mutagen, pyacoustid (Chromaprint)
```

---

## Example 7

**Intent:**
i have like 900 ebooks (epub and pdf) all over the place with stupid file names. want a tool that reads the title and author and puts them in folders like Author/Title.epub

**Spec:**
```
Type:       Command-line tool (ebook library organiser)
Features:   - Find all .epub and .pdf files under a folder
            - Read title and author from EPUB metadata and PDF document info
            - Move each book to Library/Author/Title.ext
            - Put books with missing metadata in an Unsorted folder
            - Run in dry-run mode to preview the moves first
Input:      Source folder and target library folder
Tech stack: Python, ebooklib, pypdf, Click
```

---

## Example 8

**Intent:**
Download new episodes from my podcast feeds automatically.

**Spec:**
```
Type:       Scheduled script (podcast downloader)
Data model: Feed(url, title, last_checked)
            Episode(guid, feed_url -> Feed, title, published_at, file_path)
Features:   - Read the list of RSS feed URLs from a config file
            - Parse each feed and find episodes not yet downloaded
            - Download the audio files into one folder per podcast
            - Name files as YYYY-MM-DD - Episode title.mp3
            - Delete episodes older than a set number of days
Storage:    SQLite (downloaded episodes)
Tech stack: Python, feedparser, requests, cron
```

---

## Example 9

**Intent:**
the subtitles for my movie are 3 seconds late, fix it

**Spec:**
```
Type:       Command-line script (subtitle timing shift)
Features:   - Read an .srt subtitle file
            - Shift every cue's start and end time by a given offset in milliseconds
            - Stretch timings linearly between two reference points for frame-rate drift
            - Write the corrected subtitles to a new file
Input:      Path to the .srt file and the offset (e.g. -3000 ms)
Tech stack: Python, pysrt
```

---

## Example 10

**Intent:**
I'm a freelance translator and I need to make invoices as PDFs from the command line. I have my clients in a file and I just want to type the client, the hours and the rate.

**Spec:**
```
Type:       Command-line tool (invoice PDF generator)
Data model: Client(id, name, address, vat_number, email)
            Invoice(number, client_id -> Client, issue_date, due_date, lines, total)
Features:   - Create an invoice for a client with line items of hours and rate
            - Number invoices automatically per year (2026-001, 2026-002)
            - Calculate subtotal, VAT and total
            - Render the invoice to PDF with my logo and bank details
            - List past invoices and mark them as paid
Input:      Client name, hours, rate and description as arguments
Storage:    YAML file (clients), SQLite (invoices)
Tech stack: Python, Typer, Jinja2, WeasyPrint
```

---

## Example 11

**Intent:**
sort my bank csv into categories like groceries rent fuel etc

**Spec:**
```
Type:       Command-line script (bank transaction categoriser)
Features:   - Read a bank statement export in CSV
            - Match each transaction description against keyword rules per category
            - Mark unmatched transactions as Uncategorised for review
            - Write a categorised CSV and a total per category per month
            - Learn new rules when the user assigns a category to an unmatched payee
Input:      Bank CSV file and a rules file (category -> keywords)
Storage:    JSON rules file
Tech stack: Python, pandas
```

---

## Example 12

**Intent:**
tax time is a nightmare. i scan all my receipts to one folder as pdfs and jpgs. want something that reads the date and amount and sorts them into folders by year and type (medical, donations, work stuff)

**Spec:**
```
Type:       Command-line script (tax receipt sorter)
Features:   - Run OCR on each receipt image and PDF
            - Extract the date, total amount and merchant name
            - Guess a category from merchant keywords
            - Move each receipt into Year/Category folders with a renamed file
            - Write a CSV summary of totals per category for the tax year
Input:      Folder of scanned receipts
Tech stack: Python, pytesseract, pdf2image, pandas
```

---

## Example 13

**Intent:**
export my calendar events to a csv

**Spec:**
```
Type:       Command-line script (calendar export)
Features:   - Read events from an .ics file or a CalDAV URL
            - Expand recurring events within a date range
            - Write title, start, end, location and description to CSV
            - Convert all times to a chosen timezone
Input:      Path to .ics file or CalDAV URL, start and end dates
Tech stack: Python, icalendar, recurring-ical-events, caldav
```

---

## Example 14

**Intent:**
I have three phones worth of contacts merged and now everybody is in there 2 or 3 times. Need to clean that up.

**Spec:**
```
Type:       Command-line tool (contact deduplication)
Features:   - Import contacts from a vCard (.vcf) file
            - Normalise phone numbers to international format
            - Find duplicates by matching phone, email or similar names
            - Merge duplicates and keep every unique number and email
            - Export the cleaned contacts to a new .vcf file
Input:      vCard file exported from the phone or Google Contacts
Tech stack: Python, vobject, phonenumbers, rapidfuzz
```

---

## Example 15

**Intent:**
Clean a messy CSV: trim spaces, fix dates, drop empty rows.

**Spec:**
```
Type:       Command-line script (CSV cleaner)
Features:   - Trim whitespace in every cell
            - Remove fully empty rows and duplicate rows
            - Parse mixed date formats and write them as ISO 8601
            - Standardise column names to snake_case
            - Report how many cells were changed per column
Input:      Input CSV file and output path
Tech stack: Python, pandas, python-dateutil
```

---

## Example 16

**Intent:**
need to check csv files from our suppliers have the right columns and types before we import them

**Spec:**
```
Type:       Command-line tool (CSV validator)
Features:   - Load a schema file that lists required columns, types and allowed values
            - Check every row of the CSV against the schema
            - Report errors with row number, column and reason
            - Exit with a non-zero code when errors are found for use in CI
            - Write invalid rows to a separate file
Input:      CSV file and a schema file (YAML)
Tech stack: Python, pandera, PyYAML, Click
```

---

## Example 17

**Intent:**
lint all yaml and json files in the repo

**Spec:**
```
Type:       Command-line tool (config linter)
Features:   - Find all .yaml, .yml and .json files in a directory
            - Check that each file parses and report syntax errors with line numbers
            - Enforce indentation and key ordering rules
            - Validate files against a JSON Schema when one is configured
            - Return a non-zero exit code on any error
Input:      Directory path and optional rules config
Tech stack: Node.js, js-yaml, Ajv
```

---

## Example 18

**Intent:**
We need fake but realistic data in our dev Postgres database, users, orders and products, so the frontend people have something to look at. Writing INSERTs by hand is getting old.

**Spec:**
```
Type:       Command-line tool (database seeder)
Data model: User(id, name, email, created_at)
            Product(id, name, price, stock)
            Order(id, user_id -> User, created_at, status)
            OrderItem(id, order_id -> Order, product_id -> Product, quantity)
Features:   - Generate a set number of fake users, products and orders
            - Keep foreign keys valid between generated rows
            - Truncate tables before seeding when asked
            - Use a fixed random seed for repeatable data
            - Insert rows in batches for speed
Input:      Database URL and row counts per table
Storage:    PostgreSQL
Tech stack: Python, Faker, SQLAlchemy, Click
```

---

## Example 19

**Intent:**
helper for writing database migrations, so I don't forget the down part

**Spec:**
```
Type:       Command-line tool (schema migration helper)
Features:   - Create a new timestamped migration with up and down SQL files
            - Apply pending migrations in order inside a transaction
            - Roll back the last migration using its down file
            - Show which migrations are applied and pending
            - Refuse to create a migration with an empty down file
Input:      Database URL and migrations folder
Storage:    schema_migrations table in the target database
Tech stack: Go, cobra, pgx
```

---

## Example 20

**Intent:**
load test our api, see how many requests per second it handles

**Spec:**
```
Type:       Command-line tool (API load tester)
Features:   - Send concurrent HTTP requests to a URL for a set duration
            - Ramp up the number of virtual users step by step
            - Record latency for every request
            - Show requests per second, error rate and p50/p95/p99 latency
            - Save the results as JSON for comparison between runs
Input:      Target URL, method, headers, concurrency and duration
Tech stack: Go, net/http, goroutines
```

---

## Example 21

**Intent:**
make me a mock data generator that makes JSON files from a template

**Spec:**
```
Type:       Command-line tool (mock data generator)
Features:   - Read a JSON template with field types like name, email, date and uuid
            - Generate a given number of records from the template
            - Support nested objects and arrays in the template
            - Write the output as JSON or newline-delimited JSON
            - Use a seed for reproducible output
Input:      Template file, record count and output path
Tech stack: Node.js, @faker-js/faker, commander
```

---

## Example 22

**Intent:**
generate a changelog from my commit messages

**Spec:**
```
Type:       Command-line tool (changelog generator)
Features:   - Read commits since the last git tag
            - Parse Conventional Commit prefixes (feat, fix, docs, chore)
            - Group entries into Features, Bug fixes and Other sections
            - Prepend a new version section to CHANGELOG.md
            - Link each entry to its commit hash
Input:      Git repository path and new version number
Tech stack: Python, GitPython, Jinja2
```

---

## Example 23

**Intent:**
Bump the version number everywhere in my project when I do a release (package.json, the python file, the docs).

**Spec:**
```
Type:       Command-line tool (release version bumper)
Features:   - Read the current version from a config file
            - Bump the major, minor or patch number following semantic versioning
            - Replace the version string in every listed file
            - Create a git commit and an annotated tag for the new version
            - Show a diff preview before writing changes
Input:      Part to bump (major, minor, patch) and config file listing files
Tech stack: Python, semver, GitPython, Click
```

---

## Example 24

**Intent:**
every source file needs our license header at the top, I want to check and add it

**Spec:**
```
Type:       Command-line tool (license header checker)
Features:   - Scan source files by extension (.py, .js, .go, .java)
            - Check that each file starts with the configured license header
            - Insert the header with the right comment style when missing
            - Update the year in existing headers
            - Exit with an error in check mode for CI pipelines
Input:      Project directory and a header template file
Tech stack: Go, cobra, filepath.Walk
```

---

## Example 25

**Intent:**
weekly report of which of our npm and pip dependencies are outdated

**Spec:**
```
Type:       Scheduled script (dependency update report)
Features:   - Read package.json and requirements.txt from each listed repository
            - Query the npm and PyPI registries for the latest versions
            - Classify each update as major, minor or patch
            - Flag packages with known security advisories
            - Post the report as a Markdown table to a Slack channel
Input:      List of repository paths
Tech stack: Python, requests, packaging, Slack webhook, cron
```

---

## Example 26

**Intent:**
which of our tests are flaky?? they fail randomly in CI and nobody knows which ones

**Spec:**
```
Type:       Command-line tool (test flakiness report)
Data model: TestRun(id, commit_sha, started_at)
            TestResult(run_id -> TestRun, test_name, status, duration_ms)
Features:   - Import JUnit XML reports from CI runs
            - Store each test's pass and fail history
            - Mark tests as flaky when they both pass and fail on the same commit
            - Rank tests by flake rate over the last 30 days
            - Print a report with the worst offenders
Input:      Folder of JUnit XML files
Storage:    SQLite
Tech stack: Python, junitparser, SQLite, Rich
```

---

## Example 27

**Intent:**
A dashboard to see all my cron jobs, when they last ran and if they failed.

**Spec:**
```
Type:       Data dashboard (cron job monitor)
Data model: Job(id, name, schedule, host)
            Run(id, job_id -> Job, started_at, finished_at, exit_code, output_tail)
Features:   - Receive a ping from a wrapper script at job start and end
            - Show each job with last run time, duration and status
            - Mark jobs as late when a run is missed by its schedule
            - Show the last 50 lines of output for failed runs
            - Send an email when a job fails or is late
API:        REST
            POST /jobs/{name}/start
            POST /jobs/{name}/finish
            GET  /jobs
Storage:    SQLite
Tech stack: Python, Flask, croniter, Chart.js
```

---

## Example 28

**Intent:**
docker is using 80gb on my laptop, clean it up

**Spec:**
```
Type:       Command-line script (Docker cleanup)
Features:   - List stopped containers, dangling images and unused volumes with their sizes
            - Remove containers stopped for more than 7 days
            - Remove dangling and unused images except a protected list
            - Prune the build cache
            - Show how much space was freed
Tech stack: Bash, Docker CLI
```

---

## Example 29

**Intent:**
switching kubernetes contexts and namespaces is so annoying, i always type the long command wrong

**Spec:**
```
Type:       Command-line tool (Kubernetes context switcher)
Features:   - List all contexts from the kubeconfig with the current one highlighted
            - Switch context with a fuzzy-search picker
            - Switch the default namespace for the current context
            - Show a warning colour when the context name contains prod
            - Remember the previous context and switch back with one command
Input:      Kubeconfig file (~/.kube/config)
Tech stack: Go, client-go, promptui
```

---

## Example 30

**Intent:**
monthly AWS cost report broken down by service, emailed to me

**Spec:**
```
Type:       Scheduled script (cloud cost report)
Features:   - Query AWS Cost Explorer for last month's cost by service
            - Compare each service with the previous month and show the change
            - Highlight services whose cost grew by more than 20%
            - Render an HTML email with a table and totals
            - Send the email on the 2nd of every month
Tech stack: Python, boto3, Jinja2, AWS SES, cron
```

---

## Example 31

**Intent:**
Ich möchte ein Tool, das meine Dotfiles zwischen Laptop und Server synchron hält... sorry in english: tool to keep dotfiles same on laptop and server, but some lines different per machine

**Spec:**
```
Type:       Command-line tool (templated dotfiles sync)
Features:   - Store dotfiles as templates with per-host variables
            - Render each template with the values for the current hostname
            - Write the rendered files to their target paths
            - Show a diff between the rendered file and the file on disk
            - Push and pull the templates through a git remote
Input:      Templates folder and a hosts.yaml with per-host variables
Storage:    Git repository
Tech stack: Python, Jinja2, PyYAML, GitPython
```

---

## Example 32

**Intent:**
script to check my domains dns records are still right

**Spec:**
```
Type:       Scheduled script (DNS record checker)
Features:   - Read expected records (A, AAAA, MX, TXT, CNAME) per domain from a config file
            - Query public resolvers for the current records
            - Report any record that is missing or has a different value
            - Check that SPF and DMARC TXT records exist
            - Send a Telegram message when something changed
Input:      YAML file of domains and expected records
Tech stack: Python, dnspython, PyYAML, Telegram Bot API
```

---

## Example 33

**Intent:**
please i need program for the terminal what can show which folder is biggest in my server, like ncdu but only for print the report to file because i run it in cron

**Spec:**
```
Type:       Scheduled script (disk usage report)
Features:   - Scan the given mount points and total sizes per directory up to depth 3
            - Sort directories by size and keep the top 50
            - Compare with yesterday's report and show growth per directory
            - Write the report to a dated text file
            - Warn when a filesystem is more than 85% full
Input:      List of mount points
Storage:    Dated text reports in /var/log/disk-report
Tech stack: Bash, du, df, sort, cron
```

---

## Example 34

**Intent:**
rename my podcast mp3s using the id3 tags

**Spec:**
```
Type:       Command-line script (audio file renamer)
Features:   - Read ID3 tags (album, track number, title) from each MP3
            - Rename files to "Album - 01 - Title.mp3"
            - Remove characters not allowed in file names
            - Print each rename before doing it
Input:      Folder of MP3 files
Tech stack: Python, mutagen
```

---

## Example 35

**Intent:**
I study Japanese and want to download the auto subtitles of youtube videos and convert them to a clean text file with timestamps for flashcards

**Spec:**
```
Type:       Command-line script (subtitle extractor)
Features:   - Download the subtitle track for a video URL in a chosen language
            - Convert the VTT subtitles to plain lines with start timestamps
            - Merge duplicate overlapping lines from auto captions
            - Export the lines as a tab-separated file ready for Anki import
Input:      Video URL and language code (e.g. ja)
Tech stack: Python, yt-dlp, webvtt-py
```

---

## Example 36

**Intent:**
generate a ssh key, put it on server, add to config. all in one command pls

**Spec:**
```
Type:       Command-line script (SSH setup)
Features:   - Generate a new ed25519 key pair with a name based on the host
            - Copy the public key to the remote server's authorized_keys
            - Add a matching Host entry to ~/.ssh/config
            - Test the login with the new key and report success
Input:      Hostname, username and an alias for the host
Tech stack: Bash, ssh-keygen, ssh-copy-id
```

---

## Example 37

**Intent:**
My wife and I share expenses and the bank gives us a CSV each month. I'd like a script that splits the shared stuff (anything tagged groceries, utilities, rent) 50/50 and tells me who owes who.

**Spec:**
```
Type:       Command-line script (shared expense splitter)
Features:   - Read both partners' bank CSV exports
            - Tag transactions as shared using category keyword rules
            - Sum shared spending paid by each person
            - Calculate the balance and print who owes whom
            - Write a monthly summary CSV with the shared transactions
Input:      Two bank CSV files and a rules file
Tech stack: Python, pandas
```

---

## Example 38

**Intent:**
Convert my Goodreads export into a nice markdown reading log.

**Spec:**
```
Type:       Command-line script (reading log generator)
Features:   - Read the Goodreads library export CSV
            - Keep only books on the read shelf
            - Group books by the year they were finished
            - Write a Markdown file with title, author, rating and date per book
            - Add yearly counts at the top of each section
Input:      goodreads_library_export.csv
Tech stack: Python, csv module
```

---

## Example 39

**Intent:**
postgres backup restore test - i want to know my backups actually work

**Spec:**
```
Type:       Scheduled script (backup restore verification)
Features:   - Find the newest database dump in the backup folder
            - Restore it into a temporary PostgreSQL container
            - Run sanity queries comparing row counts with the production database
            - Remove the temporary container afterwards
            - Send an alert if the restore or checks fail
Input:      Backup folder path and production database URL
Tech stack: Bash, Docker, psql, pg_restore
```

---

## Example 40

**Intent:**
tool to tell me when my domain names are about to expire

**Spec:**
```
Type:       Scheduled script (domain expiry checker)
Features:   - Look up WHOIS data for each domain in a list
            - Parse the registry expiry date
            - Warn when a domain expires within 30 days
            - Send a summary email once a week
Input:      Text file of domain names
Tech stack: Python, python-whois, smtplib, cron
```

---

## Example 41

**Intent:**
mock REST server from an openapi file so frontend can work before backend is done

**Spec:**
```
Type:       Command-line tool (mock API server)
Features:   - Read an OpenAPI 3 specification file
            - Start a local HTTP server with every path and method from the spec
            - Return example responses from the spec or generate them from the schemas
            - Validate incoming request bodies against the schemas
            - Add an optional random delay to simulate a slow network
Input:      OpenAPI YAML or JSON file and port number
Tech stack: Node.js, Express, @apidevtools/swagger-parser, json-schema-faker
```

---

## Example 42

**Intent:**
kubectl logs from all pods of a deployment at once with colors

**Spec:**
```
Type:       Command-line tool (multi-pod log tailer)
Features:   - Find all pods matching a deployment or label selector
            - Stream logs from every pod and container at the same time
            - Prefix each line with the pod name in its own colour
            - Follow new pods when the deployment scales or restarts
            - Filter lines with a regular expression
Input:      Namespace and deployment name or label selector
Tech stack: Go, client-go, fatih/color
```

---

## Example 43

**Intent:**
find dupes in my contacts csv from outlook and merge them

**Spec:**
```
Type:       Command-line script (CSV contact merger)
Features:   - Read the Outlook contacts CSV export
            - Normalise names, emails and phone numbers
            - Group rows that share an email or phone number
            - Merge each group into one row keeping all non-empty fields
            - Write the merged contacts to a new CSV
Input:      Outlook contacts CSV
Tech stack: Python, pandas, phonenumbers
```

---

## Example 44

**Intent:**
hello, i am working in small company and we have many json config for different customers. i need tool that compare two json and show the difference in nice way, not all text only the keys that changed

**Spec:**
```
Type:       Command-line tool (JSON diff)
Features:   - Load two JSON files
            - Compare them key by key, including nested objects and arrays
            - Show added, removed and changed keys with their full path
            - Colour the output green, red and yellow
            - Ignore keys listed in an ignore file
Input:      Two JSON file paths
Tech stack: Python, deepdiff, Rich
```

---

## Example 45

**Intent:**
I want to know how long each of my GitHub Actions workflows takes and how much they cost us

**Spec:**
```
Type:       Command-line tool (CI usage report)
Features:   - Fetch workflow runs for a repository from the GitHub API for a date range
            - Sum run minutes per workflow and per runner type
            - Estimate cost using the per-minute price for each runner
            - Show the slowest jobs and their average duration
            - Export the report to CSV
Input:      Repository name, date range and a GitHub token
Tech stack: Python, PyGithub, pandas
```

---

## Example 46

**Intent:**
wanna split my huge sql dump into one file per table

**Spec:**
```
Type:       Command-line script (SQL dump splitter)
Features:   - Read a MySQL or PostgreSQL plain-text dump line by line
            - Detect CREATE TABLE and INSERT statements for each table
            - Write each table's statements to its own .sql file
            - Keep header settings in a shared file
Input:      Path to the .sql dump file and output directory
Tech stack: Python (streaming file reading)
```

---

## Example 47

**Intent:**
check all links in our docs folder still work

**Spec:**
```
Type:       Command-line tool (documentation link checker)
Features:   - Find all Markdown files in a folder
            - Extract internal and external links
            - Check that internal links point to existing files and headings
            - Send HEAD requests to external links with a concurrency limit
            - Report broken links with file and line number
Input:      Docs folder path
Tech stack: Rust, pulldown-cmark, reqwest, tokio
```

---

## Example 48

**Intent:**
a cli where i type a cron expression and it tells me in plain english when it runs plus next 5 times

**Spec:**
```
Type:       Command-line tool (cron expression explainer)
Features:   - Parse a standard five-field cron expression
            - Describe the schedule in plain English
            - List the next five run times in the local timezone
            - Report invalid fields with a clear message
Input:      Cron expression as an argument
Tech stack: Python, croniter, cron-descriptor
```

---

## Example 49

**Intent:**
Get rid of old kubernetes namespaces that our preview deployments leave behind.

**Spec:**
```
Type:       Scheduled script (Kubernetes preview cleanup)
Features:   - List namespaces with the label type=preview
            - Check the age of each namespace and its linked pull request status
            - Delete namespaces older than 3 days or whose pull request is closed
            - Post a summary of deleted namespaces to Slack
Tech stack: Python, kubernetes client, PyGithub, cron
```

---

## Example 50

**Intent:**
Our team's Azure bill keeps growing and nobody knows why. I'd like a daily script that pulls the cost by resource group and tags and tells us if anything spiked compared to the previous week.

**Spec:**
```
Type:       Scheduled script (Azure cost anomaly report)
Features:   - Query the Azure Cost Management API for daily cost by resource group and tag
            - Store daily totals for trend comparison
            - Compare each resource group with its average over the previous 7 days
            - Flag spikes above 30% and list the top cost drivers
            - Send the report to a Microsoft Teams channel
Storage:    SQLite (daily cost history)
Tech stack: Python, azure-mgmt-costmanagement, Teams incoming webhook
```

---

## Example 51

**Intent:**
tool for renaming tv show subtitle files to match the video file names

**Spec:**
```
Type:       Command-line script (subtitle renamer)
Features:   - Find video and subtitle files in a folder
            - Match subtitles to videos by season and episode number (S01E02)
            - Rename each subtitle to the video name with the language code (.en.srt)
            - List subtitles that could not be matched
Input:      Folder containing video and subtitle files
Tech stack: Python, guessit
```

---

## Example 52

**Intent:**
in my team ppl keep committing .env files and keys by accident, need a check before push

**Spec:**
```
Type:       Command-line tool (secret scanner for git)
Features:   - Scan staged files for patterns like API keys, private keys and passwords
            - Block commits that add .env or .pem files
            - Allow known false positives through an ignore file
            - Install itself as a git pre-commit hook
            - Print the file and line of each finding
Input:      Git repository (staged changes)
Tech stack: Go, regexp, git hooks
```

---

## Example 53

**Intent:**
I want to generate a nice PDF price quote for my customers from a YAML file. I'm a carpenter so it's materials plus labour.

**Spec:**
```
Type:       Command-line tool (quote PDF generator)
Features:   - Read customer details, materials and labour hours from a YAML file
            - Calculate material cost, labour cost, VAT and total
            - Render a branded PDF quote with validity date
            - Number quotes automatically and keep a copy in an archive folder
Input:      Quote YAML file
Storage:    Archive folder of generated PDFs
Tech stack: Python, ReportLab, PyYAML
```

---

## Example 54

**Intent:**
pls make cli to check if website https redirect and HSTS header are ok

**Spec:**
```
Type:       Command-line tool (HTTPS configuration checker)
Features:   - Request the http:// URL and check it redirects to https://
            - Check the Strict-Transport-Security header and its max-age
            - Check the TLS version and certificate chain
            - Print a pass or fail line for every check
Input:      One or more domain names
Tech stack: Python, requests, ssl module
```

---

## Example 55

**Intent:**
ics file of all bank holidays for my country for the next 5 years

**Spec:**
```
Type:       Command-line script (holiday calendar generator)
Features:   - Look up public holidays for a country and region
            - Generate events for a range of years
            - Write all-day events to an .ics file
            - Add the holiday name in the chosen language
Input:      Country code, region and year range
Tech stack: Python, holidays, icalendar
```

---

## Example 56

**Intent:**
compare the schema of my staging and production databases

**Spec:**
```
Type:       Command-line tool (database schema diff)
Features:   - Connect to two databases and read tables, columns, indexes and constraints
            - Show tables and columns that exist in only one database
            - Show columns whose type or default differs
            - Generate the ALTER statements to make staging match production
Input:      Two database connection URLs
Tech stack: Python, SQLAlchemy inspector, Click
```

---

## Example 57

**Intent:**
random test data CSV with 10k rows, names emails dates amounts

**Spec:**
```
Type:       Command-line script (test CSV generator)
Features:   - Generate a set number of rows with name, email, date and amount columns
            - Keep amounts within a given minimum and maximum
            - Spread dates across a given range
            - Write the rows to a CSV file
Input:      Row count, output path and value ranges
Tech stack: Python, Faker, csv module
```

---

## Example 58

**Intent:**
I manage a few Linux servers and want a script that checks every morning that each one has disk space, recent backups, and the certs are not about to expire, all in one email.

**Spec:**
```
Type:       Scheduled script (server health report)
Features:   - Connect to each server over SSH
            - Check free disk space on every mounted filesystem
            - Check the age of the newest file in the backup folder
            - Check SSL certificate expiry for each configured domain
            - Send one combined HTML email with green, yellow and red statuses
Input:      YAML inventory of servers, backup paths and domains
Tech stack: Python, Paramiko, Jinja2, smtplib, cron
```

---

## Example 59

**Intent:**
bump docker image tags in my k8s yaml files to the newest version

**Spec:**
```
Type:       Command-line tool (image tag updater)
Features:   - Find container image references in Kubernetes YAML manifests
            - Query the container registry for the newest semver tag of each image
            - Update the tags in place while keeping YAML comments
            - Skip images pinned with a comment marker
            - Show a summary of old and new tags
Input:      Folder of Kubernetes manifests
Tech stack: Go, go-containerregistry, yaml.v3
```

---

## Example 60

**Intent:**
my scanned bank statements are pdf, need them as csv

**Spec:**
```
Type:       Command-line script (bank statement PDF to CSV)
Features:   - Extract tables from each page of a bank statement PDF
            - Detect date, description, debit and credit columns
            - Merge transactions that wrap onto two lines
            - Write all transactions to one CSV with a balance check
Input:      PDF bank statement
Tech stack: Python, pdfplumber, pandas
```

---

## Example 61

**Intent:**
Hi! For my thesis I need to check that a big folder of JSON files all follow the same structure, and list which ones don't. Can you specify a tool?

**Spec:**
```
Type:       Command-line tool (JSON schema validator)
Features:   - Load a JSON Schema file
            - Validate every JSON file in a folder against the schema
            - Report each invalid file with the failing path and message
            - Print a count of valid and invalid files
            - Optionally infer a draft schema from a sample file
Input:      Folder of JSON files and a schema file
Tech stack: Python, jsonschema, genson
```

---

## Example 62

**Intent:**
manage my ssh tunnels to databases without remembering the -L flags

**Spec:**
```
Type:       Command-line tool (SSH tunnel manager)
Features:   - Define named tunnels with jump host, local port and remote host:port
            - Start and stop tunnels in the background by name
            - List running tunnels with their PIDs and ports
            - Restart a tunnel automatically when the connection drops
            - Check that the local port is free before starting
Input:      Tunnel definitions in a YAML file
Storage:    YAML config, PID files in ~/.cache
Tech stack: Python, sshtunnel, Typer
```

---

## Example 63

**Intent:**
my known_hosts file is full of old servers that dont exist anymore

**Spec:**
```
Type:       Command-line script (known_hosts cleaner)
Features:   - Read every entry from ~/.ssh/known_hosts
            - Resolve hashed and plain host names where possible
            - Try to reach each host on port 22 with a short timeout
            - List unreachable hosts and remove them after confirmation
            - Keep a backup copy of the original file
Tech stack: Bash, ssh-keygen -R, nc
```

---

## Example 64

**Intent:**
remind me before my GPG keys expire

**Spec:**
```
Type:       Scheduled script (GPG key expiry reminder)
Features:   - List secret keys and subkeys from the local GPG keyring
            - Read the expiry date of each key and subkey
            - Warn by desktop notification 30 days before expiry
            - Print the command to extend the expiry date
Tech stack: Bash, gpg, notify-send, cron
```

---

## Example 65

**Intent:**
I exported my passwords from my password manager to CSV (I know, I'll delete it after). I want to check which ones appear in data breaches, without sending my passwords anywhere.

**Spec:**
```
Type:       Command-line script (breached password checker)
Features:   - Read the password manager CSV export
            - Hash each password with SHA-1 locally
            - Send only the first 5 hash characters to the Have I Been Pwned range API
            - Report entries whose password was found and how many times
            - Flag reused passwords across different sites
Input:      CSV export with site, username and password columns
Tech stack: Python, hashlib, requests
```

---

## Example 66

**Intent:**
make a QR code for our guest wifi from the terminal

**Spec:**
```
Type:       Command-line tool (Wi-Fi QR code generator)
Features:   - Build the WIFI:T:WPA;S:<ssid>;P:<password>;; string
            - Generate a QR code PNG or SVG
            - Print the QR code directly in the terminal
            - Add the network name as a caption under the image
Input:      SSID, password and security type
Tech stack: Python, qrcode, Pillow
```

---

## Example 67

**Intent:**
block ads and trackers on my laptop by updating the hosts file every week

**Spec:**
```
Type:       Scheduled script (hosts file blocklist updater)
Features:   - Download blocklists from a list of URLs
            - Merge and deduplicate the blocked domains
            - Keep a personal allowlist of domains never to block
            - Write the entries between marker comments in /etc/hosts
            - Flush the DNS cache after updating
Input:      Config file with blocklist URLs and allowlist
Tech stack: Python, requests, systemd timer
```

---

## Example 68

**Intent:**
switch between my local, staging and prod setups in /etc/hosts for testing

**Spec:**
```
Type:       Command-line tool (hosts file profile switcher)
Features:   - Store named profiles of host-to-IP mappings
            - Activate a profile by writing it into a managed block of /etc/hosts
            - Show which profile is active
            - Restore the original hosts file
            - Request sudo only for the write step
Input:      Profile name
Storage:    Profiles in ~/.config/hostswitch/profiles.toml
Tech stack: Rust, clap, toml
```

---

## Example 69

**Intent:**
Renew lets encrypt certs and reload nginx, and tell me if it failed

**Spec:**
```
Type:       Scheduled script (certificate renewal)
Features:   - Run certbot renew for all certificates
            - Test the nginx configuration before reloading
            - Reload nginx only when a certificate was renewed
            - Send an email with the certbot output when renewal fails
            - Log every run with a timestamp
Tech stack: Bash, certbot, nginx, systemd timer
```

---

## Example 70

**Intent:**
need https on localhost for my dev projects without browser warnings

**Spec:**
```
Type:       Command-line tool (local development certificate authority)
Features:   - Create a local root certificate authority once
            - Install the root certificate into the system and browser trust stores
            - Issue certificates for localhost and custom dev domains
            - Include subject alternative names for every given host
            - List and revoke issued certificates
Input:      One or more host names
Storage:    CA key and certificates in ~/.local/share/devca
Tech stack: Go, crypto/x509, cobra
```

---

## Example 71

**Intent:**
what is using port 3000 and kill it

**Spec:**
```
Type:       Command-line tool (port process finder)
Features:   - Find the process listening on a given TCP or UDP port
            - Show the PID, command name and user
            - Kill the process after confirmation, or force-kill with a flag
            - Work on Linux, macOS and Windows
Input:      Port number
Tech stack: Rust, sysinfo, netstat2
```

---

## Example 72

**Intent:**
split audiobook m4b into chapters

**Spec:**
```
Type:       Command-line script (audiobook chapter splitter)
Features:   - Read chapter markers from an M4B file
            - Export each chapter as a separate MP3 or M4A file
            - Name files with chapter number and title
            - Copy the cover art and author tags into each file
Input:      Path to the .m4b file and output format
Tech stack: Python, ffmpeg, mutagen
```

---

## Example 73

**Intent:**
which albums in my music collection are missing cover art

**Spec:**
```
Type:       Command-line script (missing album art finder)
Features:   - Scan the music library and group tracks by album folder
            - Check for embedded artwork in tracks and cover.jpg files
            - List albums without any cover
            - Download missing covers from the MusicBrainz Cover Art Archive when a release ID is tagged
Input:      Music library path
Tech stack: Python, mutagen, musicbrainzngs
```

---

## Example 74

**Intent:**
my m3u playlists broke after I moved my music to a new drive

**Spec:**
```
Type:       Command-line script (playlist path fixer)
Features:   - Read every .m3u and .m3u8 playlist in a folder
            - Check whether each referenced file still exists
            - Search the new library for a file with the same name and size
            - Rewrite the playlist with the new paths
            - List tracks that could not be found
Input:      Playlist folder and new music library path
Tech stack: Python, pathlib
```

---

## Example 75

**Intent:**
export all my spotify playlists to csv so i have a backup

**Spec:**
```
Type:       Command-line script (Spotify playlist export)
Auth:       Spotify OAuth (authorization code flow)
Features:   - Log in to the Spotify Web API
            - Fetch all playlists of the current user
            - Fetch every track with artist, album, duration and ISRC
            - Write one CSV per playlist into a dated folder
Tech stack: Python, spotipy, pandas
```

---

## Example 76

**Intent:**
kindle highlights to markdown notes, one file per book

**Spec:**
```
Type:       Command-line script (Kindle highlights exporter)
Features:   - Parse the "My Clippings.txt" file from a Kindle
            - Group highlights and notes by book title
            - Remove duplicate highlights created by editing
            - Write one Markdown file per book with location and date
            - Skip books already exported unless forced
Input:      Path to My Clippings.txt and output folder
Tech stack: Python, regex
```

---

## Example 77

**Intent:**
how long will it take me to read the books on my to-read pile? I have them as epubs.

**Spec:**
```
Type:       Command-line script (ebook reading time estimator)
Features:   - Extract the text from each EPUB file
            - Count the words per book
            - Estimate reading time from a words-per-minute setting
            - Print a table sorted by length with a total
Input:      Folder of EPUB files and reading speed
Tech stack: Python, ebooklib, BeautifulSoup
```

---

## Example 78

**Intent:**
Every morning I want one email with the new posts from the 30 blogs I follow instead of checking each site.

**Spec:**
```
Type:       Scheduled script (RSS email digest)
Data model: Feed(url, title)
            SeenItem(guid, feed_url -> Feed, seen_at)
Features:   - Read a list of RSS and Atom feeds
            - Collect items published since the last run
            - Group items by feed with title, summary and link
            - Send one HTML email digest
            - Skip feeds that fail and list them at the bottom
Storage:    SQLite (seen items)
Tech stack: Python, feedparser, Jinja2, smtplib, cron
```

---

## Example 79

**Intent:**
i record a little podcast with my friends and want to host it myself, need something that makes the rss feed from a folder of mp3s

**Spec:**
```
Type:       Command-line tool (podcast feed generator)
Features:   - Read episode MP3 files and a metadata YAML per episode
            - Get duration and file size of each episode
            - Generate an iTunes-compatible RSS feed
            - Upload the feed and new episodes to an S3 bucket
            - Validate the feed before uploading
Input:      Episodes folder and podcast.yaml with show details
Tech stack: Python, feedgen, mutagen, boto3
```

---

## Example 80

**Intent:**
combine english and spanish subtitles into one file so both show on screen

**Spec:**
```
Type:       Command-line script (dual-language subtitle merger)
Features:   - Read two .srt files for the same video
            - Match cues by overlapping time ranges
            - Merge the matched texts with the second language in italics below
            - Write the combined subtitles to a new .srt or .ass file
Input:      Two subtitle files and the output path
Tech stack: Python, pysubs2
```

---

## Example 81

**Intent:**
subtitles out of sync and the offset changes during the movie, can a tool fix it automatically from the audio?

**Spec:**
```
Type:       Command-line tool (automatic subtitle synchroniser)
Features:   - Extract the audio track from the video
            - Detect speech segments with voice activity detection
            - Find the best offset and scale between speech and subtitle timings
            - Rewrite the subtitles with corrected timings
            - Print the detected offset and a confidence score
Input:      Video file and subtitle file
Tech stack: Python, ffmpeg, webrtcvad, numpy, pysrt
```

---

## Example 82

**Intent:**
remind clients about unpaid invoices

**Spec:**
```
Type:       Scheduled script (unpaid invoice reminder)
Data model: Invoice(number, client_email, amount, due_date, paid, reminders_sent)
Features:   - Read open invoices from a CSV
            - Find invoices past their due date
            - Send a polite reminder email with the PDF attached
            - Send a firmer second reminder after 14 more days
            - Update the reminder count in the CSV
Input:      invoices.csv and a folder of invoice PDFs
Tech stack: Python, pandas, smtplib, cron
```

---

## Example 83

**Intent:**
simple terminal timer to track hours per client so I can bill them at the end of the month

**Spec:**
```
Type:       Command-line tool (time tracker)
Data model: Project(id, name, client, hourly_rate)
            TimeEntry(id, project_id -> Project, started_at, stopped_at, note)
Features:   - Start and stop a timer for a project
            - Add entries manually for forgotten work
            - Show today's and this week's hours per project
            - Export a monthly report with hours and amount per client to CSV
Storage:    SQLite in ~/.local/share
Tech stack: Go, cobra, modernc.org/sqlite
```

---

## Example 84

**Intent:**
For my self-employed taxes I need a mileage log. I have my Google location history export. Can a script pull out the car trips?

**Spec:**
```
Type:       Command-line script (mileage log generator)
Features:   - Read the location history JSON export
            - Keep only activity segments of type driving
            - Calculate distance, start and end address for each trip
            - Let the user mark trips as business or private in an interactive prompt
            - Write a mileage log CSV with a yearly total
Input:      Location history JSON file and the tax year
Tech stack: Python, pandas, geopy, questionary
```

---

## Example 85

**Intent:**
crypto tax: calculate gains with FIFO from my exchange trade history csv

**Spec:**
```
Type:       Command-line script (crypto capital gains calculator)
Features:   - Import trade history CSVs from several exchanges into one format
            - Convert every trade to the home currency at the trade date
            - Match sells to buys using first-in first-out
            - Separate short-term and long-term gains by holding period
            - Write a yearly gains report CSV
Input:      Exchange CSV exports and home currency
Tech stack: Python, pandas, CoinGecko API
```

---

## Example 86

**Intent:**
track my dividends from the broker export

**Spec:**
```
Type:       Command-line script (dividend tracker)
Features:   - Read dividend transactions from the broker's CSV export
            - Total dividends per stock, per month and per year
            - Show withholding tax paid per country
            - Print a yearly summary table and a monthly bar chart in the terminal
Input:      Broker CSV export
Tech stack: Python, pandas, plotext
```

---

## Example 87

**Intent:**
my travel expenses are in 5 currencies, i need them all in euro using the rate of that day

**Spec:**
```
Type:       Command-line script (expense currency converter)
Features:   - Read an expenses CSV with date, amount and currency columns
            - Fetch the ECB reference rate for each date and currency
            - Use the last available rate for weekends and holidays
            - Add amount_eur and rate columns to the output CSV
            - Cache downloaded rates locally
Input:      Expenses CSV
Storage:    Local JSON rate cache
Tech stack: Python, pandas, requests (ECB data API)
```

---

## Example 88

**Intent:**
convert bank csv to QIF so I can import it in my budgeting app

**Spec:**
```
Type:       Command-line tool (bank statement QIF/OFX converter)
Features:   - Read a bank CSV using a per-bank column mapping
            - Parse dates and amounts with the bank's locale format
            - Write transactions as QIF or OFX
            - Skip transactions already exported using a hash of each row
Input:      Bank CSV file and bank profile name
Storage:    Profiles in YAML, exported hashes in a text file
Tech stack: Python, pandas, ofxtools
```

---

## Example 89

**Intent:**
Merge my work calendar, my kids' school calendar and the football club calendar into one feed I can subscribe to on my phone.

**Spec:**
```
Type:       Scheduled script (calendar feed merger)
Features:   - Download several .ics feeds from URLs
            - Prefix event titles with the source name
            - Remove duplicate events with the same UID
            - Write the merged calendar to a single .ics file
            - Upload the file to a web folder for phone subscription
Input:      YAML list of feed URLs and prefixes
Tech stack: Python, icalendar, requests, rsync
```

---

## Example 90

**Intent:**
find a time when all 4 of us are free next week, we all have ics calendars

**Spec:**
```
Type:       Command-line tool (free time finder)
Features:   - Load several .ics calendars or URLs
            - Expand recurring events in the given week
            - Compute time slots where nobody is busy within working hours
            - List free slots of at least the given meeting length
Input:      Calendar files or URLs, week start date and meeting duration
Tech stack: Python, icalendar, recurring-ical-events
```

---

## Example 91

**Intent:**
birthday reminders from my phone contacts

**Spec:**
```
Type:       Scheduled script (birthday reminder)
Features:   - Read birthdays from a vCard export
            - Find birthdays in the next 7 days
            - Calculate the age the person turns when the year is known
            - Send a morning email or push notification with the list
Input:      contacts.vcf
Tech stack: Python, vobject, ntfy.sh, cron
```

---

## Example 92

**Intent:**
split a big csv into separate files by the value in one column (like one file per country)

**Spec:**
```
Type:       Command-line script (CSV splitter by column)
Features:   - Read a CSV in chunks to handle large files
            - Write rows to one file per distinct value of the chosen column
            - Copy the header row into every output file
            - Make file names safe from the column values
Input:      CSV file, column name and output folder
Tech stack: Python, pandas (chunked reading)
```

---

## Example 93

**Intent:**
like vlookup but for two csv files in the terminal

**Spec:**
```
Type:       Command-line tool (CSV join)
Features:   - Join two CSV files on one or more key columns
            - Support inner, left and full outer joins
            - Report keys that exist in only one file
            - Choose which columns to keep in the output
Input:      Two CSV files, key columns and join type
Tech stack: Rust, polars, clap
```

---

## Example 94

**Intent:**
give me a quick summary of a csv: columns, types, missing values, min max etc

**Spec:**
```
Type:       Command-line tool (CSV profiler)
Features:   - Infer the type of each column
            - Count missing and distinct values per column
            - Show min, max, mean and median for numeric columns
            - Show the most frequent values for text columns
            - Print the report as a table or save it as HTML
Input:      CSV file path
Tech stack: Python, polars, Rich
```

---

## Example 95

**Intent:**
We need to send a customer data export to an outside analytics firm but we must hide names, emails and phone numbers. The IDs should still match across files.

**Spec:**
```
Type:       Command-line tool (CSV anonymiser)
Features:   - Read column rules from a config (mask, hash, fake, drop)
            - Replace names and emails with consistent fake values
            - Hash ID columns with a secret salt so joins still work across files
            - Drop columns marked as sensitive
            - Process several CSV files with the same mapping
Input:      CSV files and a YAML rules file
Tech stack: Python, pandas, Faker, hashlib (HMAC)
```

---

## Example 96

**Intent:**
check my .env has all the variables from .env.example

**Spec:**
```
Type:       Command-line tool (env file checker)
Features:   - Parse .env and .env.example files
            - List variables missing from .env
            - List extra variables not in the example
            - Warn about empty values and duplicate keys
            - Exit with an error code for use in CI or pre-commit
Input:      Paths to .env and .env.example
Tech stack: Node.js, dotenv, commander
```

---

## Example 97

**Intent:**
sort the keys in my toml config files and fix formatting

**Spec:**
```
Type:       Command-line tool (TOML formatter)
Features:   - Parse TOML files and keep comments
            - Sort keys within each table alphabetically
            - Normalise indentation and spacing around equals signs
            - Check mode that reports unformatted files without changing them
Input:      One or more TOML file paths
Tech stack: Python, tomlkit
```

---

## Example 98

**Intent:**
linter for our Dockerfiles with our own company rules

**Spec:**
```
Type:       Command-line tool (Dockerfile linter)
Features:   - Parse Dockerfile instructions
            - Require pinned base image tags instead of latest
            - Require a non-root USER instruction
            - Warn when apt-get install runs without cleaning the cache
            - Load extra rules from a YAML file and report violations with line numbers
Input:      Dockerfile paths and rules file
Tech stack: Go, moby/buildkit parser, yaml.v3
```

---

## Example 99

**Intent:**
docker compose files keep failing because two services use the same port

**Spec:**
```
Type:       Command-line script (Compose port conflict checker)
Features:   - Read several docker-compose.yml files
            - Collect the host ports from each service's port mappings
            - Report ports used by more than one service or file
            - Check whether each host port is already in use on the machine
Input:      Paths to Compose files
Tech stack: Python, PyYAML, socket module
```

---

## Example 100

**Intent:**
show me which docker images are the biggest and which layers make them big

**Spec:**
```
Type:       Command-line tool (Docker image size report)
Features:   - List local images sorted by size
            - Show the layers of an image with the instruction that created each
            - Highlight layers larger than a threshold
            - Compare the size of two tags of the same image
Input:      Optional image name
Tech stack: Python, docker SDK, Rich
```

---

## Example 101

**Intent:**
scan our container images for vulnerabilities every night and send a short summary

**Spec:**
```
Type:       Scheduled script (container vulnerability summary)
Features:   - Read the list of images in use from the cluster
            - Run a vulnerability scanner on each image
            - Count critical and high findings per image
            - Compare with the previous night and list new vulnerabilities
            - Post the summary to a Slack channel
Storage:    JSON files of previous scan results
Tech stack: Bash, Trivy, jq, kubectl, Slack webhook
```

---

## Example 102

**Intent:**
are our kubernetes pods asking for way more cpu and memory than they use?

**Spec:**
```
Type:       Command-line tool (Kubernetes resource right-sizing report)
Features:   - Read CPU and memory requests and limits of every container
            - Query Prometheus for the 95th percentile usage over 7 days
            - Show over- and under-provisioned containers by percentage
            - Suggest new request values with headroom
            - Export the report to CSV
Input:      Namespace and Prometheus URL
Tech stack: Python, kubernetes client, prometheus-api-client, pandas
```

---

## Example 103

**Intent:**
decode a kubernetes secret quickly, base64 is annoying

**Spec:**
```
Type:       Command-line tool (Kubernetes secret viewer)
Features:   - Fetch a secret by name and namespace
            - Decode every base64 value and print key = value
            - Print one key only when given
            - Mask values by default and reveal them with a flag
Input:      Secret name and namespace
Tech stack: Go, client-go, cobra
```

---

## Example 104

**Intent:**
diff helm values between dev and prod

**Spec:**
```
Type:       Command-line tool (Helm values diff)
Features:   - Load two Helm values files and the chart defaults
            - Merge each with the defaults as Helm would
            - Show keys that differ, are added or removed with their full path
            - Render the full manifests and diff them when a flag is set
Input:      Chart path and two values files
Tech stack: Go, helm SDK, go-cmp
```

---

## Example 105

**Intent:**
Our terraform plans are hundreds of lines and reviewers don't read them. I want a short summary posted on the pull request.

**Spec:**
```
Type:       Command-line tool (Terraform plan summariser)
Features:   - Read the JSON output of terraform show -json plan
            - Count resources to add, change, replace and destroy
            - List resources that will be destroyed or replaced at the top
            - Group changes by module
            - Post the summary as a pull request comment
Input:      Terraform plan JSON file and pull request number
Tech stack: Python, PyGithub, Jinja2
```

---

## Example 106

**Intent:**
check every night if someone changed our cloud stuff by hand outside terraform

**Spec:**
```
Type:       Scheduled script (Terraform drift detection)
Features:   - Run terraform plan with -detailed-exitcode for each workspace
            - Detect workspaces whose plan shows changes
            - Save the plan output for each drifted workspace
            - Open a GitHub issue listing the drifted resources
Input:      List of Terraform workspace directories
Tech stack: Bash, Terraform CLI, GitHub CLI, cron
```

---

## Example 107

**Intent:**
find stuff in google cloud we pay for but don't use, like unattached disks and unused IPs

**Spec:**
```
Type:       Command-line tool (GCP idle resource finder)
Features:   - List persistent disks not attached to any VM
            - List reserved static IPs that are not in use
            - List stopped VMs older than 30 days
            - Estimate the monthly cost of each idle resource
            - Write the findings to CSV with project and zone
Input:      GCP project IDs
Tech stack: Python, google-cloud-compute, pandas
```

---

## Example 108

**Intent:**
check none of our S3 buckets are public

**Spec:**
```
Type:       Command-line script (S3 public access audit)
Features:   - List all buckets in the account
            - Check block public access settings, bucket policy and ACLs
            - Flag buckets that allow public read or write
            - Print a table of buckets with their status
Tech stack: Python, boto3
```

---

## Example 109

**Intent:**
find all AWS resources without an owner tag

**Spec:**
```
Type:       Scheduled script (AWS untagged resource report)
Features:   - Query the Resource Groups Tagging API in every region
            - List resources missing the owner or cost-center tag
            - Group findings by service and region
            - Email the report to the platform team weekly
Tech stack: Python, boto3, Jinja2, cron
```

---

## Example 110

**Intent:**
stop our dev EC2 instances at 8pm and start them at 7am on weekdays to save money

**Spec:**
```
Type:       Scheduled script (EC2 instance scheduler)
Features:   - Find instances tagged schedule=office-hours
            - Stop running instances at 20:00 local time
            - Start them at 07:00 on weekdays only
            - Skip instances tagged keep-running
            - Log each action to CloudWatch
Tech stack: Python, boto3, AWS Lambda, EventBridge schedule
```

---

## Example 111

**Intent:**
split the cloud bill per team using tags so each team sees what they spend

**Spec:**
```
Type:       Scheduled script (cloud cost allocation report)
Features:   - Export daily cost data grouped by the team tag
            - Spread shared and untagged costs across teams by usage share
            - Build one report per team with cost by service
            - Send each team lead their report by email monthly
Input:      Team-to-email mapping file
Tech stack: Python, boto3 (Cost Explorer), pandas, smtplib
```

---

## Example 112

**Intent:**
check if my graphql schema change will break the mobile app

**Spec:**
```
Type:       Command-line tool (GraphQL breaking change checker)
Features:   - Load the old and new GraphQL schemas
            - Detect removed fields, changed types and new required arguments
            - Classify each change as breaking, dangerous or safe
            - Fail the CI job when breaking changes are found
Input:      Two schema files or endpoint URLs
Tech stack: Node.js, graphql-inspector
```

---

## Example 113

**Intent:**
run contract tests against our api using the openapi spec

**Spec:**
```
Type:       Command-line tool (API contract tester)
Features:   - Read paths and response schemas from an OpenAPI file
            - Send requests to every GET endpoint with example parameters
            - Validate status codes and response bodies against the schemas
            - Report mismatches per endpoint
            - Output results in JUnit XML for CI
Input:      OpenAPI file and base URL
Tech stack: Python, schemathesis, pytest
```

---

## Example 114

**Intent:**
capture webhooks from stripe locally and replay them when I want

**Spec:**
```
Type:       Command-line tool (webhook capture and replay)
Data model: CapturedRequest(id, received_at, method, path, headers, body)
Features:   - Start a local HTTP endpoint that records every incoming request
            - List captured requests with time and path
            - Replay a captured request to a target URL
            - Edit the body before replaying
Storage:    SQLite
Tech stack: Go, net/http, modernc.org/sqlite
```

---

## Example 115

**Intent:**
compare speed of old endpoint vs new endpoint

**Spec:**
```
Type:       Command-line tool (endpoint benchmark comparison)
Features:   - Send the same number of requests to two URLs
            - Interleave requests to avoid bias
            - Show median and p95 latency side by side
            - Report the percentage difference and whether it is significant
Input:      Two URLs, request count and concurrency
Tech stack: Python, httpx, asyncio, scipy
```

---

## Example 116

**Intent:**
our app sends emails in dev and I want them caught instead of really sent

**Spec:**
```
Type:       Command-line tool (development SMTP catcher)
Features:   - Run a local SMTP server on a configurable port
            - Store every received email with headers and attachments
            - Show emails in a small web inbox
            - Print a one-line summary of each email in the terminal
Storage:    In-memory store with optional save to .eml files
Tech stack: Python, aiosmtpd, Flask
```

---

## Example 117

**Intent:**
copy a few customers from prod to my local db for debugging but with personal data scrambled

**Spec:**
```
Type:       Command-line tool (anonymised production subset)
Features:   - Select chosen customers and follow foreign keys to related rows
            - Mask personal columns listed in a config file
            - Keep referential integrity between the copied rows
            - Insert the subset into a local database
Input:      Source and target database URLs, customer IDs and mask config
Storage:    PostgreSQL
Tech stack: Python, SQLAlchemy, Faker
```

---

## Example 118

**Intent:**
log my laptop battery health over time

**Spec:**
```
Type:       Scheduled script (battery health logger)
Features:   - Read design capacity, full charge capacity and cycle count from the system
            - Calculate battery wear as a percentage
            - Append a dated row to a CSV every day
            - Print a trend chart of capacity over the months
Storage:    CSV file in the home directory
Tech stack: Python, psutil, upower (Linux), plotext, cron
```

---

## Example 119

**Intent:**
I always forget the syntax for systemd service files. I want to give a command and get a working service.

**Spec:**
```
Type:       Command-line tool (systemd unit generator)
Features:   - Ask for the command, working directory, user and restart policy
            - Generate a .service unit file
            - Optionally generate a matching .timer unit from a schedule
            - Install the unit, reload systemd and enable it
            - Show the status and last log lines after starting
Input:      Command to run and answers to interactive prompts
Tech stack: Python, Typer, Jinja2
```

---

## Example 120

**Intent:**
tell me when a systemd service on my server has failed

**Spec:**
```
Type:       Scheduled script (failed systemd unit alert)
Features:   - List units in the failed state every 5 minutes
            - Collect the last 20 journal lines for each failed unit
            - Send an alert only once per failure, not every run
            - Send a recovery message when the unit is running again
Storage:    State file of already-alerted units
Tech stack: Bash, systemctl, journalctl, curl (ntfy)
```

---

## Example 121

**Intent:**
when i get a new mac i want to reinstall all my apps and brew packages in one go

**Spec:**
```
Type:       Command-line script (package list export and restore)
Features:   - Export installed Homebrew formulae, casks and Mac App Store apps to a Brewfile
            - Commit the Brewfile to a dotfiles repository
            - Install everything from the Brewfile on a new machine
            - Report packages that failed to install
Tech stack: Bash, Homebrew Bundle, mas
```

---

## Example 122

**Intent:**
Bootstrap script for new developer laptops at our company (Ubuntu): install our tools, set up git, ssh key, docker.

**Spec:**
```
Type:       Command-line script (developer machine bootstrap)
Features:   - Install apt packages, Docker and language runtimes from a list
            - Configure git name and email from prompts
            - Generate an SSH key and print it for adding to GitHub
            - Clone the team's main repositories into ~/code
            - Make every step safe to run twice
Input:      Package list file and answers to prompts
Tech stack: Bash, apt, curl
```

---

## Example 123

**Intent:**
sync my vs code extensions list between computers

**Spec:**
```
Type:       Command-line script (VS Code extensions sync)
Features:   - Export the list of installed extensions to a text file
            - Install missing extensions from the list
            - Optionally remove extensions not in the list
            - Show the difference before changing anything
Input:      extensions.txt in a dotfiles repository
Tech stack: Bash, VS Code CLI (code --list-extensions)
```

---

## Example 124

**Intent:**
my bash history has thousands of duplicate commands

**Spec:**
```
Type:       Command-line script (shell history deduplicator)
Features:   - Read ~/.bash_history or ~/.zsh_history including timestamps
            - Remove duplicate commands and keep the newest occurrence
            - Remove commands matching a list of patterns such as passwords
            - Write the cleaned history back after making a backup
Tech stack: Python
```

---

## Example 125

**Intent:**
manage my shell aliases, add, list, delete without editing bashrc

**Spec:**
```
Type:       Command-line tool (shell alias manager)
Features:   - Add an alias with a name and command
            - List aliases with a description
            - Delete or rename an alias
            - Write aliases to a separate file sourced by bashrc and zshrc
            - Search aliases by keyword
Storage:    ~/.aliases file
Tech stack: Go, cobra
```

---

## Example 126

**Intent:**
clipboard history in terminal like on windows win+v

**Spec:**
```
Type:       Command-line tool (clipboard history)
Features:   - Run a background daemon that saves every new clipboard text
            - Keep the last 200 entries
            - Pick an old entry with a fuzzy finder and copy it back
            - Ignore entries that look like passwords from a password manager
Storage:    SQLite
Tech stack: Rust, arboard, rusqlite, skim
```

---

## Example 127

**Intent:**
format markdown tables so the columns line up

**Spec:**
```
Type:       Command-line tool (Markdown table formatter)
Features:   - Find tables in Markdown files
            - Pad cells so every column has the same width
            - Keep column alignment markers (:---, :---:)
            - Format files in place or print to stdout
Input:      Markdown files or stdin
Tech stack: Node.js, remark, remark-gfm
```

---

## Example 128

**Intent:**
list all the TODO and FIXME comments in our code with who wrote them

**Spec:**
```
Type:       Command-line tool (TODO comment report)
Features:   - Search source files for TODO, FIXME and HACK comments
            - Find the author and date of each line with git blame
            - Sort by age and show the oldest first
            - Export to CSV or Markdown
Input:      Repository path
Tech stack: Python, GitPython, Rich
```

---

## Example 129

**Intent:**
find npm packages in package.json we dont even use anymore

**Spec:**
```
Type:       Command-line tool (unused dependency finder)
Features:   - Read dependencies and devDependencies from package.json
            - Search the source files for import and require statements
            - List packages never imported
            - Treat packages used only in npm scripts or config files as used
Input:      Project folder
Tech stack: Node.js, @babel/parser, fast-glob
```

---

## Example 130

**Intent:**
Legal asked for a list of all open-source licenses in our product, from all the dependencies.

**Spec:**
```
Type:       Command-line tool (dependency license report)
Features:   - Read lockfiles (package-lock.json, poetry.lock, go.sum)
            - Look up the license of each direct and transitive dependency
            - Flag licenses not on the approved list (e.g. GPL, AGPL)
            - Generate a Markdown and CSV report with package, version and license
Input:      Project folder and approved licenses list
Tech stack: Python, requests (npm and PyPI registry APIs), pandas
```

---

## Example 131

**Intent:**
generate an SBOM for our app

**Spec:**
```
Type:       Command-line script (SBOM generator)
Features:   - Detect the package managers used in the project
            - Collect all components with name, version and package URL
            - Write the SBOM in CycloneDX JSON format
            - Attach the SBOM to the GitHub release
Input:      Project folder and release tag
Tech stack: Bash, Syft, GitHub CLI
```

---

## Example 132

**Intent:**
which folders in our monorepo have no owner in CODEOWNERS?

**Spec:**
```
Type:       Command-line tool (CODEOWNERS coverage checker)
Features:   - Parse the CODEOWNERS file and its patterns
            - Match every tracked file against the patterns in order
            - List folders and files with no owner
            - Show the number of files per owner
Input:      Repository path
Tech stack: Go, go-git, gitignore pattern matching
```

---

## Example 133

**Intent:**
show the test coverage change on each pull request

**Spec:**
```
Type:       Command-line tool (coverage diff reporter)
Features:   - Read coverage reports in Cobertura XML for the base and the PR branch
            - Calculate total coverage change
            - List changed lines that are not covered by tests
            - Post a comment on the pull request with the summary
Input:      Two coverage XML files and pull request number
Tech stack: Python, lxml, unidiff, PyGithub
```

---

## Example 134

**Intent:**
our pytest suite takes 20 min, which tests are slow

**Spec:**
```
Type:       Command-line tool (slow test report)
Features:   - Read pytest JUnit XML results from several CI runs
            - Average each test's duration
            - List the 30 slowest tests and slowest test files
            - Show how each test's time changed since last week
Input:      Folder of JUnit XML files
Tech stack: Python, junitparser, pandas
```

---

## Example 135

**Intent:**
generate test fixtures from a json schema

**Spec:**
```
Type:       Command-line tool (JSON Schema fixture generator)
Features:   - Read a JSON Schema file
            - Generate valid example objects respecting types, formats and enums
            - Generate invalid examples for negative tests
            - Write each fixture to a separate JSON file
Input:      Schema file and number of examples
Tech stack: Python, hypothesis-jsonschema, jsonschema
```

---

## Example 136

**Intent:**
format ugly SQL queries

**Spec:**
```
Type:       Command-line tool (SQL formatter)
Features:   - Format SQL files with consistent indentation and line breaks
            - Uppercase keywords
            - Support PostgreSQL, MySQL and BigQuery dialects
            - Check mode for CI that fails on unformatted files
Input:      SQL files or stdin
Tech stack: Python, sqlglot, Click
```

---

## Example 137

**Intent:**
which postgres queries are slowest, from pg_stat_statements

**Spec:**
```
Type:       Command-line tool (PostgreSQL slow query report)
Features:   - Query pg_stat_statements for total and mean execution time
            - Show the top queries by total time, calls and mean time
            - Normalise long queries for readability
            - Run EXPLAIN for a chosen query and show the plan
            - Reset the statistics after a report when asked
Input:      Database URL
Storage:    PostgreSQL (pg_stat_statements extension)
Tech stack: Python, psycopg, Rich
```

---

## Example 138

**Intent:**
how big is each table in our database and which ones are bloated

**Spec:**
```
Type:       Command-line script (database table size report)
Features:   - List every table with row estimate, table size, index size and total size
            - Estimate dead tuples and bloat percentage
            - Sort tables by total size
            - Save the report with a date to track growth
Input:      Database URL
Tech stack: Python, psycopg, pandas
```

---

## Example 139

**Intent:**
our redis is using too much memory and we dont know which keys

**Spec:**
```
Type:       Command-line tool (Redis memory analyser)
Features:   - Scan all keys with SCAN to avoid blocking the server
            - Get memory usage and TTL of each key
            - Group keys by prefix pattern (e.g. session:*)
            - Show prefixes using the most memory and keys without TTL
Input:      Redis URL and sample rate
Tech stack: Go, go-redis, cobra
```

---

## Example 140

**Intent:**
delete elasticsearch indices older than 30 days

**Spec:**
```
Type:       Scheduled script (Elasticsearch index cleanup)
Features:   - List indices matching a pattern such as logs-YYYY.MM.DD
            - Parse the date from each index name
            - Delete indices older than the retention period
            - Dry-run mode that only lists what would be deleted
Input:      Elasticsearch URL, index pattern and retention days
Tech stack: Python, elasticsearch-py, cron
```

---

## Example 141

**Intent:**
kafka lag watcher, page me if a consumer group gets too far behind on its topic

**Spec:**
```
Type:       Scheduled script (Kafka consumer lag monitor)
Features:   - List consumer groups and their topics
            - Calculate lag per partition from committed and latest offsets
            - Alert when total lag of a group exceeds its threshold
            - Send alerts to PagerDuty and recover when lag drops
Input:      Bootstrap servers and thresholds per group
Tech stack: Python, confluent-kafka, PagerDuty Events API
```

---

## Example 142

**Intent:**
check rabbitmq queues, if messages pile up send slack

**Spec:**
```
Type:       Scheduled script (RabbitMQ queue depth alert)
Features:   - Query the RabbitMQ management API for every queue
            - Compare message counts with a threshold per queue
            - Detect queues with no consumers
            - Post a Slack message for queues over the limit
Tech stack: Python, requests, Slack webhook, cron
```

---

## Example 143

**Intent:**
Copy secrets from one vault path to another when we create a new environment.

**Spec:**
```
Type:       Command-line tool (Vault secret copier)
Features:   - Read all secrets under a source path in HashiCorp Vault KV v2
            - Write them to a target path with the same structure
            - Skip keys that already exist unless forced
            - Show a list of copied keys without printing values
Input:      Source and target paths, Vault address and token
Tech stack: Go, HashiCorp Vault API client, cobra
```

---

## Example 144

**Intent:**
find AWS access keys older than 90 days

**Spec:**
```
Type:       Scheduled script (IAM access key age report)
Features:   - List all IAM users and their access keys
            - Calculate the age and last-used date of each key
            - Flag keys older than 90 days or unused for 30 days
            - Email each user and send a summary to the security team
Tech stack: Python, boto3, AWS SES, cron
```

---

## Example 145

**Intent:**
list lambdas no one has called in months

**Spec:**
```
Type:       Command-line script (unused Lambda function report)
Features:   - List Lambda functions in every region
            - Read the invocation count from CloudWatch for the last 90 days
            - List functions with zero invocations
            - Show runtime, last modified date and code size
Tech stack: Python, boto3
```

---

## Example 146

**Intent:**
set retention on all cloudwatch log groups so we stop paying for logs forever

**Spec:**
```
Type:       Command-line script (CloudWatch log retention setter)
Features:   - List log groups in the chosen regions
            - Find groups with no retention setting
            - Set retention to a chosen number of days
            - Print the stored bytes per group that will be cleaned up
Input:      Regions and retention days
Tech stack: Python, boto3
```

---

## Example 147

**Intent:**
Keep our Cloudflare DNS records in a YAML file in git and push changes from there, so we can review DNS changes in pull requests.

**Spec:**
```
Type:       Command-line tool (DNS records as code)
Features:   - Read zones and records from a YAML file
            - Fetch current records from the Cloudflare API
            - Show a plan of records to create, update and delete
            - Apply the plan after confirmation
            - Export existing records to YAML to get started
Input:      YAML records file and Cloudflare API token
Tech stack: Python, cloudflare SDK, PyYAML, Click
```

---

## Example 148

**Intent:**
my home internet IP changes and I want my domain to always point at it

**Spec:**
```
Type:       Scheduled script (dynamic DNS updater)
Features:   - Get the current public IPv4 and IPv6 address
            - Compare with the last known address
            - Update the A and AAAA records through the DNS provider API when changed
            - Log each change with a timestamp
Storage:    Text file with last known IP
Tech stack: Bash, curl, jq, systemd timer
```

---

## Example 149

**Intent:**
is my mail server ip on any spam blacklists

**Spec:**
```
Type:       Command-line tool (DNS blacklist checker)
Features:   - Reverse the IP address and query a list of DNSBL zones
            - Report the lists that contain the IP
            - Check that reverse DNS (PTR) matches the mail server name
            - Run on a schedule and alert when a new listing appears
Input:      IP address and optional hostname
Tech stack: Python, dnspython
```

---

## Example 150

**Intent:**
log my internet speed every hour so I can prove to my provider it's bad

**Spec:**
```
Type:       Scheduled script (internet speed logger)
Features:   - Run a speed test every hour
            - Save download, upload, ping and server to a CSV
            - Generate a chart of speeds per day
            - Summarise how often speed was below the contracted value
Storage:    CSV file
Tech stack: Python, speedtest-cli, matplotlib, cron
```

---

## Example 151

**Intent:**
ping a few hosts all the time and draw latency graph in terminal

**Spec:**
```
Type:       Command-line tool (live latency monitor)
Features:   - Ping several hosts in parallel every second
            - Draw a live latency graph per host in the terminal
            - Show packet loss percentage
            - Log timeouts with timestamps to a file
Input:      List of hosts
Tech stack: Go, pro-bing, termui
```

---

## Example 152

**Intent:**
wake my pc at home over the network from my laptop

**Spec:**
```
Type:       Command-line tool (Wake-on-LAN)
Features:   - Send a Wake-on-LAN magic packet to a MAC address
            - Save named devices with MAC and broadcast address
            - Wait and ping the device to confirm it woke up
Input:      Device name or MAC address
Storage:    TOML config of devices
Tech stack: Rust, clap
```

---

## Example 153

**Intent:**
show all devices in my wifi with manufacturer name

**Spec:**
```
Type:       Command-line tool (LAN device lister)
Features:   - Send ARP requests to every address in the local subnet
            - Collect IP and MAC address of each reply
            - Look up the vendor from the MAC prefix (OUI)
            - Remember known devices and highlight new ones
Input:      Network interface
Storage:    JSON file of known devices
Tech stack: Python, scapy, mac-vendor-lookup
```

---

## Example 154

**Intent:**
check the hard drives in my NAS for failing signs

**Spec:**
```
Type:       Scheduled script (SMART disk health check)
Features:   - Read SMART attributes for every disk
            - Check reallocated sectors, pending sectors and temperature
            - Run a short self-test weekly
            - Email a warning when a value crosses its threshold
Tech stack: Bash, smartmontools, msmtp, cron
```

---

## Example 155

**Intent:**
i want to get a message when my zfs pool scrub finds errors or a disk is degraded

**Spec:**
```
Type:       Scheduled script (ZFS pool health monitor)
Features:   - Run zpool status for every pool
            - Detect DEGRADED or FAULTED states and checksum errors
            - Start a monthly scrub and report its result
            - Send a Telegram message on problems
Tech stack: Bash, zpool, curl (Telegram Bot API), cron
```

---

## Example 156

**Intent:**
notify me when new versions of the docker images on my home server are out

**Spec:**
```
Type:       Scheduled script (container image update notifier)
Features:   - List running containers and their image tags
            - Query the registry for newer tags or a changed digest
            - Collect updates into one message
            - Send the message to a Discord channel once a day
Tech stack: Python, docker SDK, requests, Discord webhook
```

---

## Example 157

**Intent:**
our game server: log how many players are online every 5 min and make a weekly chart

**Spec:**
```
Type:       Scheduled script (game server player count logger)
Features:   - Query the server status port for the online player count
            - Store the count with a timestamp
            - Build a weekly chart of players by hour
            - Post the chart to a Discord channel each Sunday
Storage:    SQLite
Tech stack: Python, mcstatus, matplotlib, Discord webhook
```

---

## Example 158

**Intent:**
detect bpm of my dj tracks and write it in the tags

**Spec:**
```
Type:       Command-line script (BPM detector)
Features:   - Load each audio file in a folder
            - Estimate the tempo in beats per minute
            - Write the BPM into the file's tag
            - Skip files that already have a BPM tag
Input:      Folder of audio files
Tech stack: Python, librosa, mutagen
```

---

## Example 159

**Intent:**
some of my mp3s are super loud and others quiet. make them all same volume without re-encoding

**Spec:**
```
Type:       Command-line script (ReplayGain tagger)
Features:   - Analyse the loudness of each track
            - Calculate track and album gain values
            - Write ReplayGain tags without changing the audio data
            - Process albums folder by folder
Input:      Music library folder
Tech stack: Python, rsgain, mutagen
```

---

## Example 160

**Intent:**
Show me my music listening stats for the year from last.fm, like top artists per month.

**Spec:**
```
Type:       Command-line script (Last.fm yearly stats)
Features:   - Download all scrobbles for a user and year from the Last.fm API
            - Count plays per artist, album and track
            - Show the top 5 artists of each month
            - Print total listening time estimated from track durations
            - Save the scrobbles to CSV for reuse
Input:      Last.fm username, API key and year
Tech stack: Python, pylast, pandas
```

---

## Example 161

**Intent:**
Save web articles to read later and send them to my kindle as an ebook every Friday

**Spec:**
```
Type:       Scheduled script (read-later to Kindle)
Features:   - Read saved article URLs from a text file
            - Extract the main article text and images
            - Build one EPUB with a table of contents
            - Email the EPUB to the Kindle address
            - Clear the list after sending
Input:      articles.txt
Tech stack: Python, trafilatura, ebooklib, smtplib, cron
```

---

## Example 162

**Intent:**
fix series and series number in my calibre library from goodreads data

**Spec:**
```
Type:       Command-line script (Calibre series metadata fixer)
Features:   - List books in the Calibre library without series information
            - Search an online book API by title and author
            - Read series name and number from the result
            - Update the books with calibredb after confirmation
Input:      Calibre library path
Tech stack: Python, calibredb CLI, requests (Open Library API)
```

---

## Example 163

**Intent:**
organize my comic cbz files by series and issue number

**Spec:**
```
Type:       Command-line script (comic archive organiser)
Features:   - Read ComicInfo.xml from each CBZ archive
            - Fall back to parsing series and issue number from the file name
            - Move files to Series/Series #001.cbz
            - Report files that could not be parsed
Input:      Folder of CBZ and CBR files
Tech stack: Python, zipfile, rarfile
```

---

## Example 164

**Intent:**
transcribe my podcast episodes to text with timestamps so I can post them

**Spec:**
```
Type:       Command-line tool (podcast transcriber)
Features:   - Convert each episode to 16 kHz mono audio
            - Transcribe the audio with a local speech recognition model
            - Split the text into paragraphs with timestamps
            - Label speakers with diarization
            - Export as Markdown, SRT and plain text
Input:      Audio files and model size
Tech stack: Python, faster-whisper, pyannote.audio, ffmpeg
```

---

## Example 165

**Intent:**
put chapter marks in my podcast mp3 from the timestamps in the show notes

**Spec:**
```
Type:       Command-line script (podcast chapter tagger)
Features:   - Parse lines like 00:12:30 Topic title from a show notes file
            - Convert them into ID3 CHAP and CTOC frames
            - Write the chapters into the MP3
            - Print the chapter list for checking
Input:      MP3 file and show notes text file
Tech stack: Python, mutagen
```

---

## Example 166

**Intent:**
my blu-ray rips have image subtitles (PGS), i need text srt

**Spec:**
```
Type:       Command-line tool (image subtitle OCR)
Features:   - Extract the PGS subtitle stream from an MKV file
            - Decode each subtitle image with its timestamps
            - Run OCR on each image in the chosen language
            - Write the text and timings to an SRT file
            - List low-confidence lines for manual review
Input:      MKV file and subtitle language
Tech stack: Python, ffmpeg, pgsreader, pytesseract
```

---

## Example 167

**Intent:**
download missing subtitles for my whole movie folder

**Spec:**
```
Type:       Command-line tool (subtitle downloader)
Features:   - Scan a media library for videos without subtitles
            - Compute the OpenSubtitles hash of each video
            - Search for subtitles in preferred languages
            - Download the best match next to the video
            - Keep a log of videos with no subtitles found
Input:      Library folder and language codes
Storage:    Text log file
Tech stack: Python, subliminal
```

---

## Example 168

**Intent:**
Our customers in Germany now need e-invoices (ZUGFeRD), not just PDF. Make a tool that takes our invoice data and produces the right file.

**Spec:**
```
Type:       Command-line tool (ZUGFeRD e-invoice generator)
Features:   - Read invoice data from JSON (seller, buyer, lines, VAT)
            - Build the Factur-X/ZUGFeRD XML in the EN 16931 profile
            - Render a PDF/A-3 invoice and embed the XML
            - Validate the XML against the official schema
Input:      Invoice JSON file
Tech stack: Python, factur-x, WeasyPrint, lxml
```

---

## Example 169

**Intent:**
pay all my suppliers at once: create a SEPA transfer file from a csv for the bank upload

**Spec:**
```
Type:       Command-line script (SEPA payment file generator)
Features:   - Read payees, IBAN, BIC, amount and reference from a CSV
            - Validate every IBAN checksum
            - Build a pain.001 SEPA credit transfer XML
            - Print the number of payments and total amount
Input:      Payments CSV and debtor account details
Tech stack: Python, sepaxml, schwifty
```

---

## Example 170

**Intent:**
find all my subscriptions in my bank export, i think i pay for stuff i forgot

**Spec:**
```
Type:       Command-line script (recurring payment detector)
Features:   - Read 12 months of bank transactions from CSV
            - Group payments by cleaned payee name
            - Detect monthly and yearly patterns with similar amounts
            - List subscriptions with amount, frequency and yearly cost
            - Show subscriptions that recently increased in price
Input:      Bank CSV export
Tech stack: Python, pandas, rapidfuzz
```

---

## Example 171

**Intent:**
count my home office days from my work calendar for the tax deduction

**Spec:**
```
Type:       Command-line script (home office day counter)
Features:   - Read the work calendar from an .ics export
            - Find days with an all-day event named Home office or WFH
            - Exclude public holidays and vacation days
            - Print the count per month and the yearly total with the allowance amount
Input:      Calendar file and tax year
Tech stack: Python, icalendar, holidays
```

---

## Example 172

**Intent:**
password generator with real words that i can remember

**Spec:**
```
Type:       Command-line tool (passphrase generator)
Features:   - Pick random words from the EFF diceware word list using a secure random source
            - Set the number of words, separator and capitalisation
            - Optionally add a digit and symbol
            - Show the estimated entropy in bits
            - Copy the passphrase to the clipboard instead of printing it
Input:      Word count and options as flags
Tech stack: Python, secrets module, pyperclip
```

---

## Example 173

**Intent:**
my 2fa codes in the terminal instead of grabbing my phone every time

**Spec:**
```
Type:       Command-line tool (TOTP code generator)
Features:   - Import TOTP secrets from otpauth:// URIs or QR code images
            - Store secrets encrypted with a master password
            - Print the current code and seconds left for an account
            - Copy the code to the clipboard
            - List accounts with fuzzy search
Storage:    Encrypted file in ~/.config
Tech stack: Python, pyotp, cryptography, pyzbar
```

---

## Example 174

**Intent:**
encrypt my tax folder before i upload it to google drive

**Spec:**
```
Type:       Command-line script (folder encryption before upload)
Features:   - Pack the folder into a tar archive
            - Encrypt the archive with a recipient public key
            - Upload the encrypted file to a cloud remote
            - Decrypt and unpack with a restore command
Input:      Folder path and recipient key
Tech stack: Bash, age, tar, rclone
```

---

## Example 175

**Intent:**
We got a GDPR audit coming. Need to scan our shared drive for files that contain personal data like IBANs, emails, phone numbers, passport numbers.

**Spec:**
```
Type:       Command-line tool (personal data scanner)
Features:   - Walk a folder and extract text from TXT, CSV, DOCX, XLSX and PDF files
            - Detect IBANs, emails, phone numbers and ID numbers with patterns and checksums
            - Count matches per file and per type
            - Write a CSV report with file path, owner and last modified date
            - Never print the matched values themselves
Input:      Folder path
Tech stack: Python, python-docx, openpyxl, pdfplumber, schwifty
```

---

## Example 176

**Intent:**
define my ufw firewall rules in a yaml and apply them on all servers

**Spec:**
```
Type:       Command-line tool (firewall rules as code)
Features:   - Read allowed ports and source IP ranges per server group from YAML
            - Connect to each server over SSH
            - Compare the current ufw rules with the desired rules
            - Add missing rules and remove extra ones after confirmation
            - Keep SSH access open to avoid lock-out
Input:      Rules YAML and inventory file
Tech stack: Python, Fabric, PyYAML
```

---

## Example 177

**Intent:**
making wireguard configs for each family member phone is a pain. want one command per new device incl qr code

**Spec:**
```
Type:       Command-line tool (WireGuard peer generator)
Features:   - Generate a key pair and preshared key for a new peer
            - Pick the next free IP address in the VPN subnet
            - Add the peer to the server's wg0.conf and reload
            - Write the client config file
            - Show the client config as a QR code in the terminal
Input:      Peer name
Storage:    Server config and peers.json
Tech stack: Bash, wg, qrencode
```

---

## Example 178

**Intent:**
a prometheus exporter that tells grafana how many days are left on our ssl certs

**Spec:**
```
Type:       Command-line tool (certificate expiry Prometheus exporter)
Features:   - Read a list of endpoints (host:port) from a config file
            - Fetch each certificate on every scrape with a timeout
            - Expose days until expiry and probe success as metrics
            - Serve metrics on /metrics
API:        HTTP
            GET  /metrics
Tech stack: Go, prometheus/client_golang, crypto/tls
```

---

## Example 179

**Intent:**
java keystore certs expire and nobody notices, we have like 40 jks files on our app servers

**Spec:**
```
Type:       Scheduled script (Java keystore expiry check)
Features:   - Find .jks and .p12 files in the configured folders
            - List every certificate alias with its expiry date using keytool
            - Flag certificates expiring within 45 days
            - Send one email summary per server
Input:      Folders to search and keystore passwords file
Tech stack: Bash, keytool, mailx, cron
```

---

## Example 180

**Intent:**
I changed my DNS and want to see if the new IP shows up around the world yet

**Spec:**
```
Type:       Command-line tool (DNS propagation checker)
Features:   - Query a record type for a domain against 20 public resolvers in different countries
            - Show each resolver's answer and TTL in a table
            - Mark resolvers that return the expected value
            - Refresh every 30 seconds until all match
Input:      Domain, record type and expected value
Tech stack: Python, dnspython, Rich
```

---

## Example 181

**Intent:**
list all the subdomains of my company that appear in certificate transparency logs, so we find forgotten ones

**Spec:**
```
Type:       Command-line tool (subdomain inventory from CT logs)
Features:   - Query certificate transparency search for our domain
            - Extract unique subdomain names from the certificates
            - Resolve each name and check if it still answers on HTTPS
            - Compare with a known list and show new ones
Input:      Domain name and known subdomains file
Tech stack: Python, requests (crt.sh), dnspython
```

---

## Example 182

**Intent:**
check our robots.txt and sitemap.xml are fine

**Spec:**
```
Type:       Command-line tool (robots.txt and sitemap validator)
Features:   - Fetch and parse robots.txt
            - Check that the sitemap URLs listed there exist
            - Validate sitemap.xml against the sitemap schema
            - Request every URL in the sitemap and report non-200 responses or URLs blocked by robots.txt
Input:      Website base URL
Tech stack: Python, requests, lxml, urllib.robotparser
```

---

## Example 183

**Intent:**
make a status page html from some health checks that i can host on github pages

**Spec:**
```
Type:       Scheduled script (static status page generator)
Features:   - Run HTTP, TCP and DNS checks from a YAML config
            - Keep 90 days of results per check
            - Calculate uptime percentage per service
            - Render a static HTML status page with daily bars
            - Commit and push the page to a GitHub Pages repository
Storage:    JSON history file in the repository
Tech stack: Python, httpx, Jinja2, GitHub Actions schedule
```

---

## Example 184

**Intent:**
Turn our postman collection into a bunch of curl commands in a shell script

**Spec:**
```
Type:       Command-line tool (Postman to curl converter)
Features:   - Read a Postman collection v2.1 JSON file
            - Resolve collection and environment variables
            - Write one curl command per request with headers and body
            - Group commands by folder with comments
Input:      Collection file and environment file
Tech stack: Node.js, postman-collection, commander
```

---

## Example 185

**Intent:**
the website is slow and I saved a HAR from chrome, which requests are the problem?

**Spec:**
```
Type:       Command-line tool (HAR file analyser)
Features:   - Parse a HAR file from the browser dev tools
            - List the slowest requests with DNS, connect, wait and download times
            - Total the transferred bytes by domain and content type
            - Flag uncompressed and uncached resources
Input:      HAR file
Tech stack: Python, haralyzer, Rich
```

---

## Example 186

**Intent:**
decode jwt tokens in terminal and tell me when they expire

**Spec:**
```
Type:       Command-line tool (JWT decoder)
Features:   - Split a JWT into header, payload and signature
            - Pretty-print the decoded JSON
            - Show iat, nbf and exp as readable dates and time left
            - Verify the signature when a secret or public key is given
Input:      Token as argument or stdin
Tech stack: Rust, jsonwebtoken, clap
```

---

## Example 187

**Intent:**
generate typescript types from some example json responses

**Spec:**
```
Type:       Command-line tool (JSON to TypeScript type generator)
Features:   - Read one or more sample JSON files
            - Infer interfaces with nested types and arrays
            - Mark fields missing in some samples as optional
            - Write a .ts file with exported interfaces
Input:      Sample JSON files and root type name
Tech stack: Node.js, quicktype-core
```

---

## Example 188

**Intent:**
fake sensor data to mqtt so i can test my dashboard without real devices

**Spec:**
```
Type:       Command-line tool (MQTT sensor simulator)
Features:   - Define virtual sensors with topic, value range and interval in YAML
            - Generate realistic values with noise and slow drift
            - Publish JSON messages to an MQTT broker
            - Simulate sensors going offline at random
Input:      Sensor config YAML and broker URL
Tech stack: Python, paho-mqtt, numpy
```

---

## Example 189

**Intent:**
generate fake log lines (nginx and app logs) to load test our log pipeline

**Spec:**
```
Type:       Command-line tool (fake log generator)
Features:   - Generate nginx access log lines in combined format
            - Generate JSON application logs with levels and trace IDs
            - Control the rate in lines per second
            - Inject error bursts at set times
            - Write to a file, stdout or a TCP endpoint
Input:      Format, rate and duration
Tech stack: Go, gofakeit, cobra
```

---

## Example 190

**Intent:**
seed mongodb from json fixture files but keep references between them working

**Spec:**
```
Type:       Command-line tool (MongoDB fixture loader)
Features:   - Load JSON fixture files per collection
            - Replace symbolic references like @user:alice with generated ObjectIds
            - Drop collections before loading when asked
            - Create indexes defined in the fixtures
Input:      Fixtures folder and MongoDB URI
Storage:    MongoDB
Tech stack: Node.js, mongodb driver, commander
```

---

## Example 191

**Intent:**
we move from mysql to postgres, need to convert the schema

**Spec:**
```
Type:       Command-line tool (MySQL to PostgreSQL schema converter)
Features:   - Read the MySQL schema from a live database or dump
            - Map column types (TINYINT(1) to boolean, DATETIME to timestamp, AUTO_INCREMENT to identity)
            - Convert indexes, foreign keys and default values
            - Write PostgreSQL DDL to a file
            - List features that need manual work such as ENUM columns
Input:      MySQL connection URL or dump file
Tech stack: Python, sqlglot, SQLAlchemy
```

---

## Example 192

**Intent:**
lint our sql migrations so nobody locks a big table in production again

**Spec:**
```
Type:       Command-line tool (migration safety linter)
Features:   - Parse SQL migration files
            - Flag dangerous statements such as adding a NOT NULL column without default or creating an index without CONCURRENTLY
            - Warn about renaming or dropping columns still used by the app
            - Allow exceptions with an inline comment
            - Run as a CI step on changed migrations
Input:      Migration files
Tech stack: Python, sqlglot, Click
```

---

## Example 193

**Intent:**
write release notes from the pull requests merged since last release, sorted by their labels

**Spec:**
```
Type:       Command-line tool (release notes generator)
Features:   - Find the previous release tag
            - List pull requests merged since that tag via the GitHub API
            - Group them by labels (feature, bug, breaking)
            - Credit each author and list first-time contributors
            - Create a draft GitHub release with the notes
Input:      Repository and new tag name
Tech stack: Go, go-github, text/template
```

---

## Example 194

**Intent:**
We have a monorepo with 12 npm packages. When one changes, its version and the versions of packages that depend on it should be bumped together.

**Spec:**
```
Type:       Command-line tool (monorepo version coordinator)
Features:   - Detect which packages changed since their last release tag
            - Bump the version of changed packages
            - Bump dependent packages and update their dependency ranges
            - Write a changelog entry per package
            - Create one tag per released package
Input:      Monorepo root folder and bump type
Tech stack: Node.js, semver, simple-git
```

---

## Example 195

**Intent:**
CI should fail if the git tag version doesn't match the version in pyproject.toml

**Spec:**
```
Type:       Command-line script (release version consistency check)
Features:   - Read the tag name from the CI environment
            - Read the version from pyproject.toml
            - Compare both after stripping a leading v
            - Exit with an error message when they differ
Input:      Tag name and project file
Tech stack: Python, tomllib
```

---

## Example 196

**Intent:**
add SPDX license identifiers to all our files instead of the long license text

**Spec:**
```
Type:       Command-line tool (SPDX header converter)
Features:   - Detect long license header blocks at the top of files
            - Replace them with a single SPDX-License-Identifier line
            - Add a copyright line with the year of first commit
            - Leave generated and vendored files untouched
Input:      Repository path and license ID
Tech stack: Python, GitPython, regex
```

---

## Example 197

**Intent:**
auto merge dependabot PRs that are only patch updates and green CI

**Spec:**
```
Type:       Scheduled script (Dependabot auto-merge)
Features:   - List open pull requests from dependabot
            - Read the update type from the PR title or metadata
            - Check that all required checks passed
            - Approve and merge patch and minor dev-dependency updates
            - Comment on the PR why it was skipped otherwise
Tech stack: Python, PyGithub, GitHub Actions schedule
```

---

## Example 198

**Intent:**
go mod outdated report for all our go services

**Spec:**
```
Type:       Command-line script (Go module update report)
Features:   - Run go list -m -u all in each service folder
            - Collect modules with newer versions available
            - Mark major updates separately
            - Produce a combined Markdown table across services
Input:      Folder with Go service repositories
Tech stack: Go, os/exec, encoding/json
```

---

## Example 199

**Intent:**
in jest tests some fail then pass on retry, i want to know which ones

**Spec:**
```
Type:       Command-line tool (Jest retry flake detector)
Features:   - Read Jest JSON results from CI runs with retries enabled
            - Find tests that failed and then passed on retry
            - Count flakes per test over time
            - Open a GitHub issue for tests that flaked more than 3 times this week
Input:      Folder of Jest result files
Storage:    JSON history file
Tech stack: Node.js, @octokit/rest
```

---

## Example 200

**Intent:**
backup crontabs of all servers into git so we know who changed what

**Spec:**
```
Type:       Scheduled script (crontab inventory)
Features:   - Connect to every server in the inventory over SSH
            - Dump the crontab of each user and /etc/cron.d files
            - Save them to one folder per server in a git repository
            - Commit only when something changed with a diff summary
Input:      Inventory file of servers
Storage:    Git repository
Tech stack: Bash, ssh, git, cron
```

---

## Example 201

**Intent:**
convert my old crontab into systemd timers

**Spec:**
```
Type:       Command-line tool (crontab to systemd timer converter)
Features:   - Parse each line of a crontab
            - Translate the schedule into an OnCalendar expression
            - Generate a .service and a .timer file per job
            - Keep the environment variables set in the crontab
            - Print the commands to enable the timers
Input:      Crontab file
Tech stack: Python, Jinja2
```

---

## Example 202

**Intent:**
wich container keeps restarting or got killed for memory? docker only, no k8s

**Spec:**
```
Type:       Command-line tool (container restart report)
Features:   - Inspect every container for restart count and last exit code
            - Detect containers killed by the out-of-memory killer
            - Show the time of the last restart
            - Print the last log lines of unhealthy containers
Tech stack: Python, docker SDK, Rich
```

---

## Example 203

**Intent:**
wait in my script until all docker compose services are healthy before running tests

**Spec:**
```
Type:       Command-line tool (Compose health waiter)
Features:   - Read the services of a Compose project
            - Poll each container's health status
            - Exit when every service is healthy or fail after a timeout
            - Print the logs of services that never became healthy
Input:      Compose project name and timeout
Tech stack: Go, docker client, cobra
```

---

## Example 204

**Intent:**
show me all the pods in crashloop over all namespaces with the reason

**Spec:**
```
Type:       Command-line tool (CrashLoopBackOff report)
Features:   - List pods in every namespace
            - Find containers in CrashLoopBackOff or Error state
            - Show restart count, last exit code and termination reason
            - Print the last 20 log lines of the previous container
Tech stack: Python, kubernetes client, Rich
```

---

## Example 205

**Intent:**
tell me before cert-manager certificates in the cluster expire or fail to renew

**Spec:**
```
Type:       Scheduled script (cert-manager certificate monitor)
Features:   - List Certificate resources in every namespace
            - Read the notAfter date and Ready condition
            - Alert on certificates that are not ready or expire within 14 days
            - Post alerts to Slack with namespace and name
Tech stack: Python, kubernetes client (custom objects API), Slack webhook
```

---

## Example 206

**Intent:**
i have 5 kubeconfig files from different clusters and want them merged in one

**Spec:**
```
Type:       Command-line tool (kubeconfig merger)
Features:   - Load several kubeconfig files
            - Rename clusters, users and contexts that have the same name
            - Write one merged kubeconfig with a backup of the old one
            - Remove a cluster and its user and context by name
Input:      Kubeconfig file paths
Tech stack: Go, client-go clientcmd
```

---

## Example 207

**Intent:**
port-forward 6 services from k8s at once and keep them alive

**Spec:**
```
Type:       Command-line tool (multi port-forward manager)
Features:   - Read services, namespaces and local ports from a config file
            - Start a port-forward for each service
            - Reconnect when a port-forward drops
            - Show a live status table of all forwards
Input:      Config YAML
Tech stack: Go, client-go portforward, bubbletea
```

---

## Example 208

**Intent:**
every morning post yesterday's google cloud spend to our slack

**Spec:**
```
Type:       Scheduled script (GCP daily spend report)
Features:   - Query the BigQuery billing export for yesterday's cost per project and service
            - Compare with the same weekday last week
            - Post a short message with the total and the top 5 services to Slack
Tech stack: Python, google-cloud-bigquery, Slack webhook, Cloud Scheduler
```

---

## Example 209

**Intent:**
will we go over budget this month? predict the end of month cloud cost

**Spec:**
```
Type:       Command-line tool (cloud cost forecast)
Features:   - Load daily cost for the current and past 3 months
            - Forecast the month-end total from the daily trend
            - Compare the forecast with the monthly budget
            - Show the forecast and confidence range in the terminal
Input:      Monthly budget amount
Tech stack: Python, boto3 (Cost Explorer), pandas, statsmodels
```

---

## Example 210

**Intent:**
how much could we save if our worker nodes ran on spot instances

**Spec:**
```
Type:       Command-line script (spot savings estimate)
Features:   - List running EC2 instances by type and region
            - Fetch on-demand prices and spot price history
            - Estimate monthly savings per instance type
            - Show the interruption frequency for each type
Tech stack: Python, boto3 (Pricing API, EC2)
```

---

## Example 211

**Intent:**
find huge files I haven't opened in a year so I can delete them

**Spec:**
```
Type:       Command-line tool (stale large file finder)
Features:   - Scan a folder for files larger than a size threshold
            - Filter by last access or modification time
            - Show path, size and age sorted by size
            - Move selected files to the trash interactively
Input:      Folder, size threshold and age in days
Tech stack: Python, send2trash, questionary
```

---

## Example 212

**Intent:**
delete all the node_modules folders in my old projects

**Spec:**
```
Type:       Command-line tool (node_modules cleaner)
Features:   - Find node_modules folders under a root folder
            - Show the size of each and when the project was last modified
            - Select folders to delete in an interactive list
            - Show the total space freed
Input:      Root folder
Tech stack: Rust, walkdir, dialoguer
```

---

## Example 213

**Intent:**
some of my flac and mp3 files are corrupt, they skip or stop. find them

**Spec:**
```
Type:       Command-line script (corrupt audio file finder)
Features:   - Decode every audio file fully without playing it
            - Record decoding errors and truncated files
            - Verify the built-in MD5 of FLAC files
            - Write a list of broken files with the error message
Input:      Music folder
Tech stack: Bash, ffmpeg, flac --test
```

---

## Example 214

**Intent:**
Ich habe viele EPUBs gekauft. some of them dont open on my ereader, i want check all with tool

**Spec:**
```
Type:       Command-line script (batch EPUB validator)
Features:   - Run EPUBCheck on every EPUB in a folder
            - Collect errors and warnings per book
            - Show which books have fatal errors
            - Write a CSV summary
Input:      Folder of EPUB files
Tech stack: Python, EPUBCheck (Java), subprocess
```

---

## Example 215

**Intent:**
speed up podcasts and cut the silence before copying them to my old mp3 player

**Spec:**
```
Type:       Command-line script (podcast speed-up and silence trim)
Features:   - Remove silent parts longer than 0.5 seconds
            - Speed up audio by a factor without changing the pitch
            - Normalise loudness
            - Copy the processed files to the mounted player
Input:      Input folder, speed factor and player mount path
Tech stack: Bash, ffmpeg (silenceremove, atempo, loudnorm)
```

---

## Example 216

**Intent:**
translate srt subtitle to my language using deepl, keep the timings

**Spec:**
```
Type:       Command-line tool (subtitle translator)
Features:   - Parse an SRT file
            - Send cue texts to the DeepL API in batches
            - Keep line breaks and formatting tags
            - Write a new SRT with the same timings and the target language code in the name
Input:      SRT file, target language and DeepL API key
Tech stack: Python, pysrt, deepl
```

---

## Example 217

**Intent:**
i do retainers for 6 clients, same invoice every month just new number and date, automate it

**Spec:**
```
Type:       Scheduled script (recurring invoice generator)
Data model: Retainer(client_name, client_email, description, monthly_amount, currency)
Features:   - Read retainer clients from a YAML file
            - Create an invoice PDF on the 1st of each month with the next number
            - Email each invoice to the client
            - Append each invoice to a ledger CSV
Storage:    YAML (retainers), CSV (ledger)
Tech stack: Python, WeasyPrint, Jinja2, smtplib, cron
```

---

## Example 218

**Intent:**
download all invoice pdfs from stripe for last year for my accountant

**Spec:**
```
Type:       Command-line script (Stripe invoice downloader)
Features:   - List all invoices in a date range through the Stripe API
            - Download each invoice PDF
            - Name files by date, number and customer
            - Write a CSV index with amounts and status
            - Zip the folder
Input:      Stripe secret key and date range
Tech stack: Python, stripe, requests
```

---

## Example 219

**Intent:**
match the payments in my bank csv to my open invoices so I know who paid

**Spec:**
```
Type:       Command-line tool (payment reconciliation)
Features:   - Read bank transactions and open invoices from two CSVs
            - Match payments by invoice number in the reference text
            - Fall back to matching by amount and payer name
            - Mark invoices as paid, partially paid or unpaid
            - List payments that match no invoice
Input:      Bank CSV and invoices CSV
Tech stack: Python, pandas, rapidfuzz
```

---

## Example 220

**Intent:**
calculate my quarterly vat return from my sales csv

**Spec:**
```
Type:       Command-line script (VAT return calculator)
Features:   - Read sales and purchases CSVs for a quarter
            - Sum net amounts and VAT per tax rate
            - Calculate VAT payable minus input VAT
            - Print the totals in the layout of the tax form
Input:      Sales CSV, purchases CSV and quarter
Tech stack: Python, pandas
```

---

## Example 221

**Intent:**
make my amazon orders into an expense list with categories for my budget

**Spec:**
```
Type:       Command-line script (Amazon order history categoriser)
Features:   - Read the Amazon order history CSV
            - Assign a category to each item using keyword rules
            - Split orders with several items into separate rows
            - Write a monthly totals CSV per category
Input:      Order history CSV and rules file
Tech stack: Python, pandas
```

---

## Example 222

**Intent:**
my boss sends the shift rota as excel, i want the shifts in my phone calendar

**Spec:**
```
Type:       Command-line script (shift rota to calendar)
Features:   - Read the rota spreadsheet and find the row with my name
            - Map shift codes (E, L, N) to start and end times
            - Create one calendar event per shift
            - Write an .ics file to import on the phone
Input:      Rota .xlsx file, my name and shift code times
Tech stack: Python, openpyxl, icalendar
```

---

## Example 223

**Intent:**
How many hours per week do I actually spend in meetings? I'd like a report from my Google Calendar.

**Spec:**
```
Type:       Command-line script (meeting time report)
Auth:       Google OAuth (read-only calendar scope)
Features:   - Fetch events from Google Calendar for a date range
            - Count only accepted events with other attendees as meetings
            - Total meeting hours per week and per weekday
            - Show the most frequent recurring meetings and their yearly cost in hours
Input:      Date range
Tech stack: Python, google-api-python-client, pandas
```

---

## Example 224

**Intent:**
our sports club has the member list in excel and I want it in a google contacts group so i can email everyone

**Spec:**
```
Type:       Command-line script (member list to Google Contacts sync)
Auth:       Google OAuth (contacts scope)
Features:   - Read members with name, email and phone from the spreadsheet
            - Create or update a contact for each member
            - Add contacts to a club label
            - Remove the label from people no longer in the list
Input:      Member list .xlsx file
Tech stack: Python, openpyxl, Google People API
```

---

## Example 225

**Intent:**
csv files from different people open with weird characters and wrong columns. convert all to normal utf-8 comma csv

**Spec:**
```
Type:       Command-line script (CSV encoding and delimiter normaliser)
Features:   - Detect the file encoding of each CSV
            - Detect the delimiter (comma, semicolon, tab)
            - Rewrite the file as UTF-8 with comma delimiter
            - Report the detected encoding and delimiter per file
Input:      Folder of CSV files
Tech stack: Python, charset-normalizer, csv.Sniffer
```

---

## Example 226

**Intent:**
quickly search big JSON log files in the terminal by field, like level=error and user=42

**Spec:**
```
Type:       Command-line tool (JSON lines search)
Features:   - Stream large newline-delimited JSON files
            - Filter by field conditions such as level=error and duration>500
            - Select which fields to print as columns
            - Support gzipped files
Input:      JSONL files and filter expressions
Tech stack: Rust, serde_json, flate2, clap
```

---

## Example 227

**Intent:**
daily journal file from template, one command

**Spec:**
```
Type:       Command-line tool (daily journal)
Features:   - Create today's Markdown file as journal/YYYY/MM/YYYY-MM-DD.md from a template
            - Fill in the date, weekday and weather placeholders
            - Open the file in the user's $EDITOR
            - Link to yesterday's entry at the top
Input:      Optional date argument
Tech stack: Python, Jinja2, Click
```

---

## Example 228

**Intent:**
find broken [[wiki links]] in my markdown notes

**Spec:**
```
Type:       Command-line tool (note backlink checker)
Features:   - Scan a notes folder for [[wiki links]] and Markdown links
            - Report links pointing to notes that do not exist
            - Suggest the closest existing note name for each broken link
            - Build a backlinks section at the bottom of every note
Input:      Notes folder
Tech stack: Python, rapidfuzz, regex
```

---

## Example 229

**Intent:**
which notes in my obsidian vault are orphans, nothing links to them

**Spec:**
```
Type:       Command-line script (orphan note finder)
Features:   - Read every note in the vault
            - Build a graph of links between notes
            - List notes with no incoming links
            - Ignore daily notes and template folders
Input:      Vault folder path
Tech stack: Python, networkx
```

---

## Example 230

**Intent:**
I exported my browser bookmarks, it's like 2000 of them from 10 years. Which ones are dead?

**Spec:**
```
Type:       Command-line tool (bookmark link checker)
Features:   - Parse the bookmarks HTML export with folders
            - Check each URL with a HEAD request and fall back to GET
            - Mark dead links, redirects and timeouts
            - Write a cleaned bookmarks file without dead links
            - Save a CSV report of everything checked
Input:      bookmarks.html
Tech stack: Python, BeautifulSoup, httpx (async)
```

---

## Example 231

**Intent:**
what websites do i spend my time on, from my firefox history

**Spec:**
```
Type:       Command-line script (browser history stats)
Features:   - Copy and open the Firefox places.sqlite database
            - Count visits per domain for a date range
            - Show visits per hour of day
            - Print the top 25 domains with a bar chart
Input:      Firefox profile path and date range
Storage:    SQLite (read-only copy)
Tech stack: Python, sqlite3, pandas, plotext
```

---

## Example 232

**Intent:**
install all the fonts in a folder and tell me which ones i already have

**Spec:**
```
Type:       Command-line script (font installer)
Features:   - Find .ttf and .otf files in a folder
            - Read each font's family and style name
            - Skip fonts already installed
            - Copy new fonts to the user fonts folder and refresh the font cache
Input:      Folder of font files
Tech stack: Python, fontTools, fc-cache
```

---

## Example 233

**Intent:**
pomodoro timer in terminal that tracks how many I do per day

**Spec:**
```
Type:       Command-line tool (pomodoro timer)
Features:   - Run 25-minute work and 5-minute break timers with a progress bar
            - Play a sound and send a desktop notification at the end
            - Tag each pomodoro with a task name
            - Show pomodoros per day and per task for the week
Storage:    SQLite
Tech stack: Python, Rich, plyer, sqlite3
```

---

## Example 234

**Intent:**
habit tracker but in terminal, just tick off what i did today

**Spec:**
```
Type:       Command-line tool (habit tracker)
Data model: Habit(id, name, created_at)
            CheckIn(habit_id -> Habit, date)
Features:   - Add and remove habits
            - Mark habits done for today or a past date
            - Show a calendar grid of the last 8 weeks per habit
            - Show current and longest streaks
Storage:    SQLite
Tech stack: Go, cobra, lipgloss
```

---

## Example 235

**Intent:**
I'm learning Spanish and want flashcards in the terminal with spaced repetition, I don't like apps

**Spec:**
```
Type:       Command-line tool (spaced repetition flashcards)
Data model: Card(id, deck, front, back)
            Review(card_id -> Card, reviewed_at, grade, interval_days, ease)
Features:   - Import cards from a CSV of front and back
            - Show cards that are due today one by one
            - Grade each answer from 0 to 5
            - Schedule the next review with the SM-2 algorithm
            - Show stats of cards learned and due
Storage:    SQLite
Tech stack: Python, Textual
```

---

## Example 236

**Intent:**
typing speed test in the terminal with real sentences

**Spec:**
```
Type:       Command-line tool (typing speed test)
Features:   - Show a random passage from a text file
            - Colour correct and wrong characters as the user types
            - Calculate words per minute and accuracy
            - Save results and show progress over time
Storage:    CSV of past results
Tech stack: Python, curses
```

---

## Example 237

**Intent:**
cooking unit converter cups to grams etc

**Spec:**
```
Type:       Command-line tool (cooking unit converter)
Features:   - Convert between volume units (cups, tablespoons, ml) and weight units (grams, ounces)
            - Use ingredient densities for volume to weight (flour, sugar, butter)
            - Convert oven temperatures between Celsius, Fahrenheit and gas mark
            - Accept natural input like "2 cups flour"
Input:      Amount, unit and ingredient
Tech stack: Python, pint
```

---

## Example 238

**Intent:**
scale a recipe for 8 people instead of 4

**Spec:**
```
Type:       Command-line script (recipe scaler)
Features:   - Read a recipe in Markdown or YAML with ingredient quantities
            - Multiply quantities by the new servings ratio
            - Round to sensible kitchen amounts
            - Print the scaled recipe
Input:      Recipe file and number of servings
Tech stack: Python, PyYAML, fractions module
```

---

## Example 239

**Intent:**
I keep my recipes as markdown files. I want to pick recipes for the week and get one shopping list with everything added up.

**Spec:**
```
Type:       Command-line tool (meal plan shopping list)
Features:   - Parse ingredient lists from Markdown recipe files
            - Pick recipes for the week by name
            - Add up the same ingredients across recipes with unit conversion
            - Group the list by shop section
            - Print or send the list to a notes app
Input:      Recipes folder and chosen recipe names
Tech stack: Python, pint, markdown-it-py
```

---

## Example 240

**Intent:**
remind me to water my plants, each plant needs it on different days

**Spec:**
```
Type:       Scheduled script (plant watering reminder)
Data model: Plant(name, location, interval_days, last_watered)
Features:   - Read plants and watering intervals from a YAML file
            - Find plants due today
            - Send a push notification listing them
            - Mark plants as watered with a reply command
Storage:    YAML file
Tech stack: Python, ntfy.sh, cron
```

---

## Example 241

**Intent:**
Keep track of car maintenance, oil change tyres etc and tell me when next is due

**Spec:**
```
Type:       Command-line tool (car maintenance log)
Data model: Vehicle(id, name, current_km)
            Service(id, vehicle_id -> Vehicle, type, date, km, cost, notes)
            Interval(type, every_km, every_months)
Features:   - Log a service with date, mileage and cost
            - Update the current mileage
            - Show upcoming services by date or kilometres
            - Show total maintenance cost per year
Storage:    SQLite
Tech stack: Python, Typer, sqlite3
```

---

## Example 242

**Intent:**
log fuel and see my l/100km

**Spec:**
```
Type:       Command-line tool (fuel consumption tracker)
Features:   - Log each fill-up with litres, price and odometer reading
            - Calculate consumption between full tanks
            - Show average consumption and cost per 100 km
            - Plot consumption per month in the terminal
Storage:    CSV file
Tech stack: Go, cobra, asciigraph
```

---

## Example 243

**Intent:**
for my home insurance i should have a list of everything i own with price and photos. a terminal tool is fine

**Spec:**
```
Type:       Command-line tool (home inventory)
Data model: Item(id, name, room, category, purchase_date, price, serial_number)
            Photo(id, item_id -> Item, file_path)
Features:   - Add items with room, price and serial number
            - Attach photos and receipts to an item
            - List items per room with total value
            - Export the inventory to a PDF report for the insurer
Storage:    SQLite and a photos folder
Tech stack: Python, Typer, sqlite3, ReportLab
```

---

## Example 244

**Intent:**
tell me when the warranty on my stuff runs out

**Spec:**
```
Type:       Scheduled script (warranty expiry tracker)
Features:   - Read products with purchase date and warranty months from a CSV
            - Calculate each warranty end date
            - Send an email 30 days before a warranty ends
            - Attach the stored receipt PDF to the reminder
Input:      products.csv and receipts folder
Tech stack: Python, pandas, smtplib, cron
```

---

## Example 245

**Intent:**
I read my electricity meter every week and want to see my usage and what it costs

**Spec:**
```
Type:       Command-line tool (meter reading log)
Features:   - Add a meter reading with date
            - Calculate consumption between readings in kWh per day
            - Calculate cost with the tariff's unit price and standing charge
            - Project the yearly bill and compare with the monthly prepayment
Storage:    CSV file
Tech stack: Python, pandas, Click
```

---

## Example 246

**Intent:**
read data from my solar inverter every minute and save it

**Spec:**
```
Type:       Scheduled script (solar inverter logger)
Features:   - Read power, daily yield and grid feed-in registers over Modbus TCP
            - Store readings in a time-series database
            - Calculate daily totals at midnight
            - Retry when the inverter does not respond at night
Storage:    InfluxDB
Tech stack: Python, pymodbus, influxdb-client, systemd service
```

---

## Example 247

**Intent:**
monthly energy report from my shelly smart plugs

**Spec:**
```
Type:       Scheduled script (smart plug energy report)
Features:   - Query each Shelly plug's local HTTP API for energy counters
            - Store daily readings per device
            - Calculate kWh and cost per device for the month
            - Email a report with a bar chart
Storage:    SQLite
Tech stack: Python, requests, matplotlib, cron
```

---

## Example 248

**Intent:**
raspberry pi gets hot, log temperature and throttling

**Spec:**
```
Type:       Scheduled script (Raspberry Pi thermal logger)
Features:   - Read the CPU temperature and throttling flags with vcgencmd
            - Log them every minute to a CSV
            - Warn when under-voltage or throttling is detected
            - Plot the last 24 hours on request
Storage:    CSV file
Tech stack: Bash, vcgencmd, gnuplot, cron
```

---

## Example 249

**Intent:**
Log GPU usage and memory while my model trains, so I can see if the GPU is idle waiting for data.

**Spec:**
```
Type:       Command-line tool (GPU usage logger)
Features:   - Sample GPU utilisation, memory use, temperature and power every second
            - Write samples to CSV with timestamps
            - Summarise average utilisation and idle time when stopped
            - Wrap a command and log only while it runs
Input:      Command to run and sample interval
Tech stack: Python, pynvml
```

---

## Example 250

**Intent:**
compare my training runs, they are just csv logs in different folders

**Spec:**
```
Type:       Command-line tool (training run comparison)
Features:   - Find train_log.csv files in run folders
            - Read the run config from a JSON file next to each log
            - Show a table of runs with best validation loss and epoch
            - Plot the loss curves of chosen runs in one chart
Input:      Runs folder
Tech stack: Python, pandas, matplotlib
```

---

## Example 251

**Intent:**
split my image dataset into train val test folders but keep the classes balanced

**Spec:**
```
Type:       Command-line script (stratified dataset splitter)
Features:   - Read images from one subfolder per class
            - Split each class by given ratios
            - Copy or symlink files into train, val and test folders
            - Use a fixed seed and write the split lists to CSV
Input:      Dataset folder, ratios and seed
Tech stack: Python, scikit-learn (train_test_split)
```

---

## Example 252

**Intent:**
check if the labels in my dataset are balanced and if there are weird rows

**Spec:**
```
Type:       Command-line script (dataset label check)
Features:   - Load a labelled CSV dataset
            - Show the count and share of each label
            - Find duplicate texts with different labels
            - Find empty or very short inputs
            - Print a short report
Input:      CSV file and label column name
Tech stack: Python, pandas
```

---

## Example 253

**Intent:**
strip outputs from jupyter notebooks before commit

**Spec:**
```
Type:       Command-line tool (notebook output stripper)
Features:   - Remove cell outputs and execution counts from .ipynb files
            - Keep outputs for cells tagged keep_output
            - Install as a git pre-commit hook
            - Check mode that fails when outputs are present
Input:      Notebook files
Tech stack: Python, nbformat
```

---

## Example 254

**Intent:**
our notebooks in the repo break all the time, i want to know which still run top to bottom

**Spec:**
```
Type:       Scheduled script (notebook execution check)
Features:   - Find all notebooks in the repository
            - Execute each one in a clean kernel with a timeout
            - Record pass or fail with the failing cell and error
            - Write a Markdown report and post it to the team chat
Input:      Repository path
Tech stack: Python, nbclient, papermill, cron
```

---

## Example 255

**Intent:**
find old python virtualenvs on my disk eating space

**Spec:**
```
Type:       Command-line tool (virtualenv finder)
Features:   - Search for folders containing pyvenv.cfg
            - Show size, Python version and last used date of each
            - Show whether the parent project still exists
            - Delete selected environments
Input:      Root folder
Tech stack: Python, Click, Rich
```

---

## Example 256

**Intent:**
warn if requirements.txt has unpinned packages

**Spec:**
```
Type:       Command-line script (requirements pin checker)
Features:   - Parse requirements.txt including -r includes
            - Flag packages without an exact == version
            - Flag packages without hashes when strict mode is on
            - Exit non-zero on findings
Input:      Requirements file
Tech stack: Python, packaging
```

---

## Example 257

**Intent:**
new python project setup with our company structure in one command

**Spec:**
```
Type:       Command-line tool (project scaffolder)
Features:   - Ask for project name, description and Python version
            - Create the folder layout with src, tests and docs
            - Add pyproject.toml, pre-commit config and CI workflow from templates
            - Initialise git and a virtual environment
            - Run the first test to confirm everything works
Input:      Answers to prompts
Tech stack: Python, copier, Jinja2
```

---

## Example 258

**Intent:**
auto make a table of contents in my README

**Spec:**
```
Type:       Command-line tool (Markdown TOC generator)
Features:   - Read headings from a Markdown file
            - Build a nested list of links using GitHub anchor rules
            - Insert the list between TOC marker comments
            - Check mode for CI
Input:      Markdown file
Tech stack: Node.js, markdown-it, commander
```

---

## Example 259

**Intent:**
spell check our docs but don't flag our product names

**Spec:**
```
Type:       Command-line tool (docs spell checker)
Features:   - Check spelling of Markdown files while skipping code blocks and URLs
            - Load a project dictionary of allowed words
            - Report misspellings with file, line and suggestions
            - Add words to the dictionary interactively
Input:      Docs folder and dictionary file
Tech stack: Python, pyspellchecker, markdown-it-py
```

---

## Example 260

**Intent:**
Our app has translations in JSON files for en, de, fr, es. People add keys to English and forget the others. I want a check.

**Spec:**
```
Type:       Command-line tool (missing translation key checker)
Features:   - Load all locale JSON files including nested keys
            - Use the English file as the reference
            - List keys missing in each other language
            - List keys whose value is still the English text
            - Fail CI when keys are missing
Input:      Locales folder and reference language
Tech stack: Node.js, commander
```

---

## Example 261

**Intent:**
find translation keys nobody uses in the code anymore

**Spec:**
```
Type:       Command-line tool (unused translation key finder)
Features:   - Collect all keys from the locale files
            - Search the source code for t('key') and similar calls
            - List keys never referenced
            - Remove unused keys from all locale files when asked
Input:      Locales folder and source folder
Tech stack: Node.js, fast-glob, @babel/parser
```

---

## Example 262

**Intent:**
which css classes in our stylesheet are not used in any html or jsx

**Spec:**
```
Type:       Command-line tool (unused CSS finder)
Features:   - Parse CSS and SCSS files for class selectors
            - Scan HTML, JSX and template files for class names
            - List selectors that never match
            - Show an estimate of bytes that could be removed
Input:      Styles folder and source folder
Tech stack: Node.js, postcss, fast-glob
```

---

## Example 263

**Intent:**
fail the build if our javascript bundle gets too big

**Spec:**
```
Type:       Command-line tool (bundle size budget check)
Features:   - Read size budgets per file from a config
            - Measure raw and gzip size of each built file
            - Compare with the budget and with the main branch
            - Fail with a table of files over budget
Input:      Build output folder and budget config
Tech stack: Node.js, gzip-size, commander
```

---

## Example 264

**Intent:**
run lighthouse on our 10 main pages every night and keep the scores

**Spec:**
```
Type:       Scheduled script (Lighthouse score tracker)
Features:   - Run Lighthouse on each URL for mobile and desktop
            - Store performance, accessibility, SEO and best-practices scores
            - Compare with the previous night and flag drops of more than 5 points
            - Write an HTML summary page
Storage:    JSON score history
Tech stack: Node.js, lighthouse, chrome-launcher, cron
```

---

## Example 265

**Intent:**
check our pages for accessibility problems

**Spec:**
```
Type:       Command-line tool (accessibility checker)
Features:   - Open each URL in a headless browser
            - Run axe-core accessibility rules
            - Group violations by rule and impact
            - Write a report with the failing elements and help links
Input:      List of URLs
Tech stack: Node.js, Playwright, @axe-core/playwright
```

---

## Example 266

**Intent:**
lint our openapi files with our api style guide (kebab-case paths, plural nouns, etc)

**Spec:**
```
Type:       Command-line tool (OpenAPI style linter)
Features:   - Load OpenAPI 3 files
            - Check path naming, operation IDs and response codes against custom rules
            - Require descriptions and examples on every schema
            - Report problems with the JSON pointer of each location
Input:      OpenAPI files and ruleset file
Tech stack: Node.js, @stoplight/spectral-core
```

---

## Example 267

**Intent:**
find code still calling our deprecated v1 api endpoints

**Spec:**
```
Type:       Command-line tool (deprecated endpoint usage finder)
Features:   - Read the list of deprecated endpoints from a file
            - Search the codebases for matching URL strings and client calls
            - Show each match with repository, file and line
            - Count usage per endpoint
Input:      Deprecated endpoints file and folder of repositories
Tech stack: Go, regexp, cobra
```

---

## Example 268

**Intent:**
we have feature flags in code that are on for everyone since months, find them so we can delete

**Spec:**
```
Type:       Command-line tool (stale feature flag finder)
Features:   - Fetch all flags and their rollout state from the feature flag service API
            - Mark flags at 100% or 0% for more than 30 days as stale
            - Find references to each stale flag in the code
            - Print a cleanup list with file locations
Input:      Repository path and flag service API key
Tech stack: Python, requests, ripgrep
```

---

## Example 269

**Intent:**
we have the same app on staging and prod, compare the environment variables between them and show what's different

**Spec:**
```
Type:       Command-line tool (environment config comparison)
Features:   - Fetch config variables for two environments from the hosting provider API
            - Show variables missing in either environment
            - Show variables with different values, masking secrets
            - Ignore variables that are expected to differ
Input:      Two environment names and ignore list
Tech stack: Python, requests, Rich
```

---

## Example 270

**Intent:**
list github org members without 2fa

**Spec:**
```
Type:       Command-line script (GitHub 2FA audit)
Features:   - Query the GitHub API for organisation members with 2FA disabled
            - Show each member's login, name and teams
            - Write the list to CSV
            - Optionally email each member a reminder
Input:      Organisation name and admin token
Tech stack: Python, PyGithub
```

---

## Example 271

**Intent:**
gitlab runners that are offline for weeks, clean them up

**Spec:**
```
Type:       Command-line script (GitLab runner cleanup)
Features:   - List all runners through the GitLab API
            - Find runners not contacted for more than 14 days
            - Show their description, tags and last contact
            - Delete them after confirmation
Input:      GitLab URL and admin token
Tech stack: Python, python-gitlab
```

---

## Example 272

**Intent:**
need an inventory of all our jenkins jobs, which ones still run, which never succeed

**Spec:**
```
Type:       Command-line script (Jenkins job inventory)
Features:   - List every job and folder through the Jenkins API
            - Get the last build time and result of each job
            - Mark jobs not built in 6 months as unused
            - Mark jobs whose last 10 builds failed
            - Export everything to CSV
Input:      Jenkins URL and API token
Tech stack: Python, python-jenkins, pandas
```

---

## Example 273

**Intent:**
put my pagerduty on-call shifts in my calendar

**Spec:**
```
Type:       Scheduled script (on-call calendar sync)
Features:   - Fetch on-call shifts for a user from the PagerDuty API
            - Create calendar events for each shift
            - Update events when the schedule changes
            - Publish them as an .ics file the calendar app subscribes to
Tech stack: Python, pdpyras, icalendar, cron
```

---

## Example 274

**Intent:**
after an incident, make a timeline from the slack channel export

**Spec:**
```
Type:       Command-line script (incident timeline generator)
Features:   - Read a Slack channel export JSON for the incident
            - Keep messages marked with a timeline emoji or keyword
            - Convert timestamps to UTC and sort them
            - Write a Markdown timeline for the postmortem document
Input:      Slack export folder and incident channel name
Tech stack: Python, pandas
```

---

## Example 275

**Intent:**
monthly uptime report per service for our customers, from prometheus

**Spec:**
```
Type:       Scheduled script (monthly SLA report)
Features:   - Query Prometheus for the up and probe_success metrics of each service
            - Calculate monthly availability percentage
            - Compare with the SLA target and list breaches
            - Generate a PDF report per customer
Tech stack: Python, prometheus-api-client, Jinja2, WeasyPrint, cron
```

---

## Example 276

**Intent:**
make k6 load test script from a recording of me clicking through the site

**Spec:**
```
Type:       Command-line tool (HAR to k6 script converter)
Features:   - Read a HAR file recorded in the browser
            - Drop requests to third-party domains and static assets
            - Group requests into page steps with think time
            - Write a k6 JavaScript test with checks for status codes
Input:      HAR file and allowed domains
Tech stack: Node.js, k6
```

---

## Example 277

**Intent:**
load test our websocket chat server with 5000 fake clients

**Spec:**
```
Type:       Command-line tool (WebSocket load tester)
Features:   - Open thousands of concurrent WebSocket connections at a ramp-up rate
            - Send messages at a set rate per client
            - Measure connect time and message round-trip latency
            - Report failed connections and dropped messages
Input:      Server URL, client count and message rate
Tech stack: Go, gorilla/websocket
```

---

## Example 278

**Intent:**
health check our grpc services from the command line

**Spec:**
```
Type:       Command-line tool (gRPC health checker)
Features:   - Call the standard grpc.health.v1 Check method on each service
            - Support TLS and plaintext connections
            - Show the status of every service in a table
            - Exit non-zero when any service is not serving
Input:      List of host:port addresses
Tech stack: Go, grpc-go, cobra
```

---

## Example 279

**Intent:**
see all mqtt messages flying around on my broker

**Spec:**
```
Type:       Command-line tool (MQTT topic monitor)
Features:   - Subscribe to a topic filter such as #
            - Show messages live with topic, payload and time
            - Pretty-print JSON payloads
            - Show a count of messages per topic
            - Record messages to a file for replay
Input:      Broker URL and topic filter
Tech stack: Python, paho-mqtt, Rich
```

---

## Example 280

**Intent:**
serial monitor for arduino that saves everything to a file with time

**Spec:**
```
Type:       Command-line tool (serial port logger)
Features:   - List available serial ports
            - Connect at a chosen baud rate
            - Print incoming lines with timestamps
            - Save the log to a file
            - Send typed commands to the device
Input:      Port name and baud rate
Tech stack: Python, pyserial
```

---

## Example 281

**Intent:**
flash the same firmware on 30 esp32 boards and give each its own device name

**Spec:**
```
Type:       Command-line script (batch ESP32 flasher)
Features:   - Detect a newly connected ESP32 on USB
            - Flash the firmware binary
            - Write a unique device name and Wi-Fi config into the NVS partition
            - Log the MAC address and name to a CSV
            - Wait for the next board
Input:      Firmware file and name prefix
Tech stack: Python, esptool, pyserial
```

---

## Example 282

**Intent:**
scan for bluetooth low energy devices near me and show signal strength

**Spec:**
```
Type:       Command-line tool (BLE scanner)
Features:   - Scan for BLE advertisements for a set time
            - Show device name, address, RSSI and manufacturer
            - Sort devices by signal strength
            - Filter by name or service UUID
Input:      Scan duration
Tech stack: Python, bleak
```

---

## Example 283

**Intent:**
my CV as a yaml file and a command that makes a nice PDF

**Spec:**
```
Type:       Command-line tool (CV PDF generator)
Features:   - Read experience, education and skills from a YAML file
            - Render the CV with an HTML template and stylesheet
            - Export to PDF with clickable links
            - Build a short one-page version from items tagged short
Input:      cv.yaml and template name
Tech stack: Python, Jinja2, WeasyPrint, PyYAML
```

---

## Example 284

**Intent:**
business card qr code with my contact info

**Spec:**
```
Type:       Command-line tool (vCard QR generator)
Features:   - Build a vCard 3.0 string from name, phone, email and website
            - Encode it as a QR code
            - Export PNG and SVG at print resolution
            - Print a preview in the terminal
Input:      Contact details as flags
Tech stack: Python, segno
```

---

## Example 285

**Intent:**
im freelance and never know how much tax to put aside each quarter, i have my income in a csv

**Spec:**
```
Type:       Command-line script (quarterly tax estimate)
Features:   - Read invoiced income and expenses per month from CSV
            - Calculate profit so far this year
            - Estimate income tax with the progressive brackets from a config file
            - Show the amount to set aside this quarter
Input:      Income CSV and tax brackets YAML
Tech stack: Python, pandas, PyYAML
```

---

## Example 286

**Intent:**
get the numbers out of my monthly salary slip pdfs into one spreadsheet

**Spec:**
```
Type:       Command-line script (payslip PDF parser)
Features:   - Extract text from each payslip PDF
            - Find gross pay, net pay, tax and pension lines with patterns
            - Take the month from the payslip date
            - Write one row per month to a CSV with yearly totals
Input:      Folder of payslip PDFs
Tech stack: Python, pdfplumber, pandas
```

---

## Example 287

**Intent:**
if I save 300 a month with 5% return, how much do I have at 65? something in the terminal with a chart

**Spec:**
```
Type:       Command-line tool (savings projection)
Features:   - Take current savings, monthly contribution, return rate and years
            - Calculate the balance year by year with monthly compounding
            - Adjust for inflation when given
            - Draw the growth chart in the terminal
Input:      Numbers as flags
Tech stack: Python, plotext
```

---

## Example 288

**Intent:**
loan payment schedule

**Spec:**
```
Type:       Command-line tool (loan amortisation schedule)
Features:   - Calculate the monthly payment from amount, rate and term
            - List every payment split into interest and principal
            - Show remaining balance after each payment
            - Export the schedule to CSV
Input:      Loan amount, annual interest rate and term in months
Tech stack: Go, cobra, encoding/csv
```

---

## Example 289

**Intent:**
what happens if I pay an extra 200 a month on my mortgage, how many years do I save and how much interest

**Spec:**
```
Type:       Command-line tool (mortgage overpayment calculator)
Features:   - Calculate the normal repayment schedule
            - Recalculate with monthly or one-off overpayments
            - Show the new end date and months saved
            - Show the total interest saved
Input:      Balance, rate, remaining term and overpayment
Tech stack: Python, Click
```

---

## Example 290

**Intent:**
tell me what to buy to get my portfolio back to 60/40

**Spec:**
```
Type:       Command-line tool (portfolio rebalancing calculator)
Features:   - Read current holdings and target weights from a YAML file
            - Fetch current prices for each ticker
            - Calculate current weights and drift
            - Suggest buys using new cash before any sells
            - Round to whole shares
Input:      Portfolio YAML and cash to invest
Tech stack: Python, yfinance, PyYAML
```

---

## Example 291

**Intent:**
we went on a trip with 6 friends and everyone paid for different things, need to figure out who pays who with the least transfers

**Spec:**
```
Type:       Command-line tool (group expense settler)
Features:   - Read expenses with payer, amount and who shared them from CSV
            - Calculate each person's balance
            - Compute the minimum set of transfers to settle all debts
            - Print who pays whom and how much
Input:      Expenses CSV
Tech stack: Python, csv module
```

---

## Example 292

**Intent:**
calculate my final grade with weights for exams and homework

**Spec:**
```
Type:       Command-line tool (weighted grade calculator)
Features:   - Read course components with weights and scores from a TOML file
            - Calculate the current weighted average
            - Show the score needed on the final exam to reach a target grade
            - Warn when weights do not add up to 100%
Input:      Course TOML file and target grade
Tech stack: Python, tomllib
```

---

## Example 293

**Intent:**
Im a teacher, I need random groups of 4 from my class list but some kids should never be together

**Spec:**
```
Type:       Command-line tool (class group generator)
Features:   - Read student names from a text or CSV file
            - Make random groups of a chosen size
            - Respect pairs that must not be in the same group
            - Avoid repeating groups from previous sessions
            - Print the groups and save them to history
Input:      Class list, group size and exclusion pairs
Storage:    JSON history of past groups
Tech stack: Python, random module
```

---

## Example 294

**Intent:**
exam seating plan so friends dont sit next to each other

**Spec:**
```
Type:       Command-line tool (exam seating plan generator)
Features:   - Read the room layout as rows and seats
            - Read the student list with optional friend groups
            - Place students so no two from the same group are neighbours
            - Print a seating chart and export it to PDF
Input:      Room layout file and student list
Tech stack: Python, ReportLab
```

---

## Example 295

**Intent:**
check our school timetable for clashes, same teacher or room twice at the same time

**Spec:**
```
Type:       Command-line script (timetable clash checker)
Features:   - Read the timetable CSV with day, period, class, teacher and room
            - Find teachers assigned to two lessons in one period
            - Find rooms double-booked
            - Find classes with two lessons at once
            - Print each clash with the lessons involved
Input:      Timetable CSV
Tech stack: Python, pandas
```

---

## Example 296

**Intent:**
tournament bracket for our table tennis club, 23 players, with byes

**Spec:**
```
Type:       Command-line tool (tournament bracket generator)
Features:   - Read players with optional seeding
            - Create a single-elimination bracket with byes for top seeds
            - Record match results and advance winners
            - Print the bracket as text or save it as SVG
Input:      Players file
Storage:    JSON file with bracket state
Tech stack: Python, svgwrite
```

---

## Example 297

**Intent:**
league table from match results

**Spec:**
```
Type:       Command-line script (league table generator)
Features:   - Read match results from a CSV of home, away and scores
            - Calculate played, won, drawn, lost, goals and points
            - Sort by points, goal difference then goals scored
            - Print the table and export it to HTML
Input:      Results CSV and points rules
Tech stack: Python, pandas
```

---

## Example 298

**Intent:**
our choir takes attendance in a google sheet export, want stats who comes how often

**Spec:**
```
Type:       Command-line script (attendance statistics)
Features:   - Read the attendance CSV with one column per rehearsal
            - Calculate attendance rate per member and per voice part
            - List members below 70% attendance
            - Show attendance per rehearsal over the season
Input:      Attendance CSV
Tech stack: Python, pandas
```

---

## Example 299

**Intent:**
wedding seating plan: 120 guests, 12 tables, couples together, some people hate each other lol

**Spec:**
```
Type:       Command-line tool (seating plan optimiser)
Features:   - Read guests, groups and conflicts from a YAML file
            - Keep couples and families at the same table
            - Keep people with conflicts at different tables
            - Optimise for guests sitting with people they know
            - Export the plan per table to CSV
Input:      Guests YAML and number of tables with capacity
Tech stack: Python, OR-Tools (CP-SAT)
```

---

## Example 300

**Intent:**
secret santa draw that emails everyone their person, couples cant get each other

**Spec:**
```
Type:       Command-line script (secret santa draw)
Features:   - Read participants with emails and exclusions
            - Draw a random assignment where nobody gets themselves or an excluded person
            - Email each participant only their own match
            - Save an encrypted copy of the draw in case someone loses their email
Input:      Participants YAML and SMTP settings
Tech stack: Python, smtplib, cryptography
```

---

## Example 301

**Intent:**
Name badges for our conference from the registration CSV, printed 8 per A4 page.

**Spec:**
```
Type:       Command-line tool (name badge PDF generator)
Features:   - Read attendee name, company and ticket type from CSV
            - Lay out 8 badges per A4 page with cut marks
            - Colour the badge stripe by ticket type
            - Add a QR code with the attendee ID
            - Export one print-ready PDF
Input:      Registration CSV and logo image
Tech stack: Python, ReportLab, qrcode
```

---

## Example 302

**Intent:**
make certificate of attendance pdf for every participant of our workshop and email them

**Spec:**
```
Type:       Command-line script (attendance certificate generator)
Features:   - Read participants and workshop details from CSV
            - Fill an HTML certificate template with name, date and hours
            - Render one PDF per participant
            - Email each certificate as an attachment
Input:      Participants CSV and template
Tech stack: Python, Jinja2, WeasyPrint, smtplib
```

---

## Example 303

**Intent:**
our small charity needs to send donation receipts for tax to every donor at year end

**Spec:**
```
Type:       Command-line script (yearly donation receipts)
Features:   - Read donations from the accounting CSV export
            - Total donations per donor for the year
            - Generate a PDF receipt with the legal wording and receipt number
            - Email receipts to donors with an email address and list the rest for post
Input:      Donations CSV and year
Tech stack: Python, pandas, ReportLab, smtplib
```

---

## Example 304

**Intent:**
i rent out 3 flats and want to know who paid the rent and who is late

**Spec:**
```
Type:       Command-line tool (rent tracker)
Data model: Tenant(id, name, unit, monthly_rent, due_day)
            Payment(id, tenant_id -> Tenant, date, amount)
Features:   - Import rent payments from a bank CSV by matching tenant names
            - Show each tenant's paid and outstanding months
            - List late payments with days overdue
            - Print a yearly income summary per unit
Storage:    SQLite
Tech stack: Python, Typer, pandas
```

---

## Example 305

**Intent:**
split the heating and water bill between my tenants based on the size of their flats

**Spec:**
```
Type:       Command-line script (utility cost splitter)
Features:   - Read the yearly utility bills by cost type
            - Read units with floor area and number of occupants
            - Split each cost type by area or by occupants as configured
            - Subtract prepayments and show the balance per tenant
            - Generate a statement PDF per tenant
Input:      Bills YAML and units CSV
Tech stack: Python, pandas, ReportLab
```

---

## Example 306

**Intent:**
volunteer hours report for our ngo grant application

**Spec:**
```
Type:       Command-line script (volunteer hours report)
Features:   - Read volunteer sign-in records from CSV
            - Total hours per volunteer, per project and per month
            - Calculate the monetary value at a set hourly rate
            - Write an Excel report with one sheet per project
Input:      Sign-in CSV and hourly rate
Tech stack: Python, pandas, openpyxl
```

---

## Example 307

**Intent:**
I have a list of ISBNs from scanning my bookshelf, fill in title author year

**Spec:**
```
Type:       Command-line script (ISBN metadata lookup)
Features:   - Read ISBNs from a text file
            - Validate ISBN-10 and ISBN-13 check digits
            - Look up title, authors, publisher and year from an online book API
            - Write the results to CSV and list ISBNs not found
Input:      Text file of ISBNs
Tech stack: Python, isbnlib, requests (Open Library API)
```

---

## Example 308

**Intent:**
stats for my board game collection from boardgamegeek, like how many hours of games i own lol

**Spec:**
```
Type:       Command-line script (board game collection stats)
Features:   - Fetch a user's collection from the BoardGameGeek XML API
            - Get player count, play time and weight per game
            - Show totals and averages
            - List games suitable for a given number of players
Input:      BGG username
Tech stack: Python, requests, xml.etree
```

---

## Example 309

**Intent:**
what is my vinyl collection worth, I have it on discogs

**Spec:**
```
Type:       Command-line script (record collection valuation)
Features:   - Fetch the user's collection through the Discogs API
            - Get the lowest and median marketplace price per release
            - Sum the estimated value of the collection
            - List the 20 most valuable records
Input:      Discogs username and token
Tech stack: Python, python3-discogs-client, pandas
```

---

## Example 310

**Intent:**
wine cellar: tell me which bottles i should drink this year before they get too old

**Spec:**
```
Type:       Command-line tool (wine cellar tracker)
Data model: Wine(id, name, producer, vintage, quantity, drink_from, drink_until, location)
Features:   - Add bottles with vintage and drinking window
            - Remove a bottle when it is opened
            - List wines whose window ends this year
            - Show the cellar by location and type
Storage:    SQLite
Tech stack: Go, cobra, modernc.org/sqlite
```

---

## Example 311

**Intent:**
when should I sow my vegetables, based on the last frost date where i live

**Spec:**
```
Type:       Command-line tool (sowing calendar)
Features:   - Read the last spring frost date for the user's location
            - Read vegetables with weeks before or after frost for indoor and outdoor sowing
            - Calculate the sowing and planting dates
            - Export the dates to an .ics calendar
Input:      Location or frost date and vegetable list
Tech stack: Python, icalendar
```

---

## Example 312

**Intent:**
tell me when the space station flies over my house

**Spec:**
```
Type:       Command-line tool (satellite pass predictor)
Features:   - Download the latest orbital elements (TLE) for the ISS
            - Calculate passes over a location for the next 10 days
            - Show start time, maximum elevation and direction
            - Show only passes visible at night
Input:      Latitude, longitude and minimum elevation
Tech stack: Python, skyfield
```

---

## Example 313

**Intent:**
ham radio: i have logbooks from 3 programs in ADIF and want one clean log without double QSOs

**Spec:**
```
Type:       Command-line tool (ADIF logbook merger)
Features:   - Parse several ADIF log files
            - Normalise call signs, bands and times
            - Find duplicate contacts with the same call, band, mode and time within 5 minutes
            - Write one merged ADIF file
            - Print counts per band and mode
Input:      ADIF files
Tech stack: Python, adif-io
```

---

## Example 314

**Intent:**
my family tree file has the same people twice, find duplicates in the GEDCOM

**Spec:**
```
Type:       Command-line tool (GEDCOM duplicate finder)
Features:   - Parse individuals from a GEDCOM file
            - Compare names with fuzzy matching and birth years
            - Score candidate duplicate pairs
            - Show pairs with parents and spouses to help decide
Input:      GEDCOM file
Tech stack: Python, python-gedcom, rapidfuzz
```

---

## Example 315

**Intent:**
GEDCOM report of people with missing birth or death dates so I know what to research

**Spec:**
```
Type:       Command-line script (genealogy gap report)
Features:   - Read all individuals from the GEDCOM file
            - List people missing birth date, birth place or death date
            - Flag impossible dates such as a child born before a parent
            - Group the list by family line
Input:      GEDCOM file
Tech stack: Python, python-gedcom
```

---

## Example 316

**Intent:**
weekly running distance from my gpx files

**Spec:**
```
Type:       Command-line script (GPX running summary)
Features:   - Read every GPX file in a folder
            - Calculate distance, duration and average pace per run
            - Total distance per week
            - Show the longest run and fastest 5 km
Input:      Folder of GPX files
Tech stack: Python, gpxpy, pandas
```

---

## Example 317

**Intent:**
find my personal bests from my strava export

**Spec:**
```
Type:       Command-line script (personal best finder)
Features:   - Read activities.csv and activity files from the bulk export
            - Find the fastest 1 km, 5 km, 10 km and half marathon in each run
            - Show personal bests by year
            - Export the results to CSV
Input:      Strava export folder
Tech stack: Python, gpxpy, fitdecode, pandas
```

---

## Example 318

**Intent:**
join two gpx tracks into one because my watch stopped half way

**Spec:**
```
Type:       Command-line script (GPX track merger)
Features:   - Read two or more GPX files
            - Sort track points by time
            - Merge them into one track segment
            - Write the combined GPX
Input:      GPX files
Tech stack: Python, gpxpy
```

---

## Example 319

**Intent:**
elevation profile picture of my hike from gpx

**Spec:**
```
Type:       Command-line script (elevation profile plotter)
Features:   - Read the GPX track
            - Calculate cumulative distance
            - Smooth the elevation data
            - Plot elevation over distance and save it as PNG with total ascent
Input:      GPX file
Tech stack: Python, gpxpy, matplotlib
```

---

## Example 320

**Intent:**
which chess openings do i lose with most, i have my games as pgn

**Spec:**
```
Type:       Command-line script (chess opening stats)
Features:   - Parse games from a PGN file
            - Identify the opening by ECO code
            - Count wins, draws and losses per opening and colour
            - Show the worst openings with at least 10 games
Input:      PGN file and my username
Tech stack: Python, python-chess, pandas
```

---

## Example 321

**Intent:**
sudoku solver in terminal

**Spec:**
```
Type:       Command-line tool (Sudoku solver)
Features:   - Read a puzzle as 81 characters or a grid file
            - Solve it with constraint propagation and backtracking
            - Detect puzzles with no solution or several solutions
            - Print the solved grid
Input:      Puzzle string or file
Tech stack: Rust, clap
```

---

## Example 322

**Intent:**
crossword help: give pattern like c?t?h and get words

**Spec:**
```
Type:       Command-line tool (word pattern finder)
Features:   - Load a dictionary word list
            - Match words to a pattern with ? for unknown letters
            - Filter by word length and known letters
            - Find anagrams of given letters
Input:      Pattern and optional word list
Tech stack: Python, regex
```

---

## Example 323

**Intent:**
im writing a novel in markdown, one file per chapter. i want word count per chapter and how much i wrote each day

**Spec:**
```
Type:       Command-line tool (manuscript word count tracker)
Features:   - Count words in each chapter file, ignoring comments and Markdown syntax
            - Save the total once per day
            - Show words written today and a daily streak
            - Show progress towards a target word count
Storage:    CSV log of daily totals
Tech stack: Python, Click, Rich
```

---

## Example 324

**Intent:**
check my screenplay in fountain format for mistakes

**Spec:**
```
Type:       Command-line tool (Fountain screenplay checker)
Features:   - Parse a Fountain screenplay
            - Flag scene headings that do not start with INT. or EXT.
            - Find characters who speak only once, which may be typos
            - Estimate page count and runtime
            - List scenes with their characters
Input:      .fountain file
Tech stack: Python, regex
```

---

## Example 325

**Intent:**
transpose guitar chords in my songs up or down

**Spec:**
```
Type:       Command-line tool (chord transposer)
Features:   - Read a song file in ChordPro format
            - Transpose every chord by a number of semitones
            - Choose sharps or flats for the new key
            - Write the transposed song to a new file
Input:      ChordPro file and semitones
Tech stack: Python, regex
```

---

## Example 326

**Intent:**
generate a podcast style audio from my blog posts using text to speech

**Spec:**
```
Type:       Command-line tool (blog to audio converter)
Features:   - Fetch a blog post and extract the main text
            - Split the text into sentences under the TTS length limit
            - Generate speech for each chunk with a local TTS model
            - Join the chunks into one MP3 with ID3 tags
Input:      Post URL and voice name
Tech stack: Python, trafilatura, piper-tts, pydub
```

---

## Example 327

**Intent:**
Hello, I am a nurse and I make the vacation plan for our team in excel, I want a check that minimum 3 people always work each day

**Spec:**
```
Type:       Command-line script (staff coverage checker)
Features:   - Read the vacation plan spreadsheet with one row per person and one column per day
            - Count staff working each day
            - List days with fewer than the minimum
            - Highlight these days in a copy of the spreadsheet
Input:      Vacation plan .xlsx and minimum staff number
Tech stack: Python, openpyxl
```

---

## Example 328

**Intent:**
random but fair chores rotation for my roommates every week posted to our group chat

**Spec:**
```
Type:       Scheduled script (chores rotation)
Features:   - Read roommates and chores from a YAML file
            - Rotate chores so everyone gets each chore in turn
            - Skip people marked away for the week
            - Post the week's chore list to a Telegram group every Monday
Storage:    JSON state of the current rotation
Tech stack: Python, python-telegram-bot, cron
```

---

## Example 329

**Intent:**
Wir sind ein kleiner Sportverein. I need tool to make membership fee invoices for all members each year from csv and email them

**Spec:**
```
Type:       Command-line script (membership fee invoicing)
Features:   - Read members with fee category from CSV
            - Calculate the fee per category and family discounts
            - Generate a PDF invoice per member with bank details
            - Email invoices and list members without email
Input:      Members CSV and fee table
Tech stack: Python, pandas, WeasyPrint, smtplib
```

---

## Example 330

**Intent:**
Every friday i copy numbers from 3 cloud consoles into a status email for my manager: number of servers, monthly cost so far, open alerts. I want a script to make that email.

**Spec:**
```
Type:       Scheduled script (weekly infrastructure status email)
Features:   - Count running VMs in AWS, Azure and GCP
            - Get month-to-date cost from each provider
            - Count open alerts from the monitoring system
            - Fill an email template with the numbers and the change since last week
            - Send it every Friday at 9:00
Storage:    JSON file with last week's numbers
Tech stack: Python, boto3, azure-mgmt-compute, google-cloud-compute, smtplib, cron
```

---

## Example 331

**Intent:**
start my tmux with the same windows and panes for each project

**Spec:**
```
Type:       Command-line tool (tmux session launcher)
Features:   - Read a project layout from YAML with windows, panes and start commands
            - Create the tmux session with that layout
            - Attach to the session if it already exists
            - List and kill saved sessions
Input:      Project layout name
Storage:    YAML files in ~/.config/tmuxlaunch
Tech stack: Python, libtmux, PyYAML
```

---

## Example 332

**Intent:**
my own cheat sheets in the terminal, like tldr but my notes

**Spec:**
```
Type:       Command-line tool (personal cheat sheet viewer)
Features:   - Store cheat sheets as Markdown files per topic
            - Show a cheat sheet with syntax highlighting
            - Search all sheets for a keyword
            - Open a sheet in the editor to add notes
Storage:    Markdown files in ~/.cheats
Tech stack: Go, glamour, cobra
```

---

## Example 333

**Intent:**
i want my dotfiles public on github but some files have tokens in them. encrypt only those

**Spec:**
```
Type:       Command-line tool (encrypted dotfiles secrets)
Features:   - Mark files or YAML keys in the dotfiles repo as secret
            - Encrypt marked values with age keys before commit
            - Decrypt them when installing on a trusted machine
            - Refuse to commit when a marked file is unencrypted
Input:      Dotfiles repository and age key file
Tech stack: Bash, sops, age, git hooks
```

---

## Example 334

**Intent:**
run one command on 20 servers at the same time and see the output per server

**Spec:**
```
Type:       Command-line tool (parallel SSH runner)
Features:   - Read hosts from an inventory file or groups
            - Run a command on all hosts in parallel with a concurrency limit
            - Show output grouped by host with exit codes
            - Summarise successes and failures
            - Save the full output to a log folder
Input:      Host group and command
Tech stack: Go, golang.org/x/crypto/ssh, cobra
```

---

## Example 335

**Intent:**
who has ssh access to our servers? list all authorized keys everywhere

**Spec:**
```
Type:       Command-line script (authorized_keys audit)
Features:   - Connect to each server and read authorized_keys for every user
            - Calculate the fingerprint and comment of each key
            - Match fingerprints to a known people list
            - Flag unknown keys and keys of people who left
            - Write a CSV report
Input:      Server inventory and known keys file
Tech stack: Python, Paramiko, sshpubkeys
```

---

## Example 336

**Intent:**
SSH certificates for our team instead of copying public keys around everywhere

**Spec:**
```
Type:       Command-line tool (SSH certificate signer)
Features:   - Sign a user's public key with the team CA key
            - Set principals and a validity of 8 hours
            - Log every issued certificate with serial and user
            - Print the server config lines to trust the CA
Input:      User public key and principal names
Storage:    CA key in a secure file, issuance log CSV
Tech stack: Go, golang.org/x/crypto/ssh
```

---

## Example 337

**Intent:**
make a CSR with several domain names for our certificate provider

**Spec:**
```
Type:       Command-line tool (CSR generator)
Features:   - Generate an RSA or ECDSA private key
            - Build a certificate signing request with subject and SAN list
            - Save key and CSR as PEM files with safe permissions
            - Show the CSR contents for checking
Input:      Common name, extra domains and key type
Tech stack: Python, cryptography
```

---

## Example 338

**Intent:**
Our security team wants to know which of our servers still accept old TLS 1.0 or weak ciphers.

**Spec:**
```
Type:       Command-line tool (TLS cipher scanner)
Features:   - Connect to each host with every TLS version from 1.0 to 1.3
            - Enumerate the accepted cipher suites
            - Mark weak ciphers such as RC4, 3DES and CBC with SHA1
            - Grade each host and export results to CSV
Input:      List of host:port
Tech stack: Python, sslyze
```

---

## Example 339

**Intent:**
check my bind zone file before reloading

**Spec:**
```
Type:       Command-line tool (DNS zone file linter)
Features:   - Parse a BIND zone file
            - Check the SOA serial was increased
            - Detect CNAME records next to other records with the same name
            - Check that MX and NS targets resolve
            - Report errors with line numbers
Input:      Zone file and previous serial
Tech stack: Python, dnspython
```

---

## Example 340

**Intent:**
i have 500 ip addresses from our firewall log, give me hostnames

**Spec:**
```
Type:       Command-line script (bulk reverse DNS lookup)
Features:   - Read IP addresses from a file
            - Run reverse DNS lookups in parallel
            - Add the owning network name from WHOIS when there is no PTR
            - Write IP, hostname and network to CSV
Input:      Text file of IPs
Tech stack: Python, dnspython, ipwhois, asyncio
```

---

## Example 341

**Intent:**
subnet calculator

**Spec:**
```
Type:       Command-line tool (subnet calculator)
Features:   - Parse an IPv4 or IPv6 address with prefix length
            - Show network, broadcast, first and last host and host count
            - Split a network into smaller subnets
            - Check whether an address belongs to a subnet
Input:      CIDR notation
Tech stack: Rust, ipnet, clap
```

---

## Example 342

**Intent:**
small office, we write IP addresses on a paper. want simple tool to keep which device has which ip

**Spec:**
```
Type:       Command-line tool (simple IP address manager)
Data model: Subnet(id, cidr, name, vlan)
            Address(ip, subnet_id -> Subnet, hostname, mac, owner, note)
Features:   - Add subnets and reserve addresses for devices
            - Suggest the next free address in a subnet
            - Search by IP, hostname or MAC
            - Ping all addresses to find used but unregistered ones
Storage:    SQLite
Tech stack: Python, Typer, ipaddress module
```

---

## Example 343

**Intent:**
two devices fight over the same ip on my network sometimes, find out which

**Spec:**
```
Type:       Command-line tool (duplicate IP detector)
Features:   - Send ARP requests for every address in the subnet
            - Detect addresses answered by more than one MAC address
            - Watch ARP traffic and alert on changes for the same IP
            - Show the vendor of each conflicting device
Input:      Network interface and subnet
Tech stack: Python, scapy
```

---

## Example 344

**Intent:**
disk not full but no space left error, i think inodes

**Spec:**
```
Type:       Command-line tool (inode usage finder)
Features:   - Show inode usage per filesystem
            - Count files per directory recursively
            - List the directories with the most files
            - Show the oldest files in those directories
Input:      Starting path
Tech stack: Bash, find, df -i, sort
```

---

## Example 345

**Intent:**
check that my backup folder and the original have the same files

**Spec:**
```
Type:       Command-line tool (folder comparison)
Features:   - Walk two folders and compare relative paths
            - Compare sizes and modification times, and hashes with a flag
            - List files only on one side and files that differ
            - Exit non-zero when folders are not identical
Input:      Two folder paths
Tech stack: Go, crypto/sha256, cobra
```

---

## Example 346

**Intent:**
bought a cheap 256gb sd card online, check if it is fake

**Spec:**
```
Type:       Command-line tool (storage capacity verifier)
Features:   - Fill the card with test files containing known data
            - Read every file back and verify the content
            - Report the real usable capacity and corrupted areas
            - Measure read and write speed
Input:      Mount path of the card
Tech stack: Rust, clap
```

---

## Example 347

**Intent:**
my mp3 tags have junk like "www.downloadsite.com" and ALL CAPS titles, clean it

**Spec:**
```
Type:       Command-line script (music tag cleaner)
Features:   - Remove URLs and site names from all tag fields
            - Convert ALL CAPS titles and artists to title case
            - Trim extra spaces and fix "feat." spelling
            - Show changes per file before writing
Input:      Music folder
Tech stack: Python, mutagen, regex
```

---

## Example 348

**Intent:**
make a playlist of songs I havent listened to in a long time, i use mpd

**Spec:**
```
Type:       Command-line script (forgotten songs playlist)
Features:   - Read play counts and last-played dates from the MPD sticker database
            - Select tracks not played for 12 months
            - Shuffle and limit to a playlist length
            - Save the playlist into MPD
Input:      Months and number of tracks
Tech stack: Python, python-mpd2
```

---

## Example 349

**Intent:**
copy new ebooks to my kobo when i plug it in

**Spec:**
```
Type:       Command-line script (ereader sync)
Features:   - Detect the mounted Kobo device
            - Compare the library folder with the books on the device
            - Copy books not yet on the device
            - Optionally remove books marked as read
            - Unmount safely when done
Input:      Library folder
Tech stack: Bash, rsync, udisksctl
```

---

## Example 350

**Intent:**
merge my podcast subscriptions from 2 apps (OPML files) without duplicates

**Spec:**
```
Type:       Command-line script (OPML merger)
Features:   - Parse two or more OPML files
            - Normalise feed URLs (http/https, trailing slashes)
            - Remove duplicate feeds
            - Write one merged OPML file sorted by title
Input:      OPML files
Tech stack: Python, listparser
```

---

## Example 351

**Intent:**
check if my subtitles are too fast to read

**Spec:**
```
Type:       Command-line tool (subtitle reading speed checker)
Features:   - Read an SRT file
            - Calculate characters per second for each cue
            - Flag cues above the limit or shorter than one second
            - Flag lines longer than 42 characters
            - Print the problems with timestamps
Input:      SRT file and CPS limit
Tech stack: Python, pysrt
```

---

## Example 352

**Intent:**
auditor wants proof our invoice numbers have no gaps

**Spec:**
```
Type:       Command-line script (invoice number gap checker)
Features:   - Read invoice numbers and dates from the accounting export
            - Sort by number within each year series
            - Report missing and duplicate numbers
            - Report invoices whose date is earlier than the previous number's date
Input:      Invoices CSV
Tech stack: Python, pandas
```

---

## Example 353

**Intent:**
my bank only gives MT940 files, i need csv

**Spec:**
```
Type:       Command-line script (MT940 to CSV)
Features:   - Parse MT940 statement files
            - Extract date, amount, currency, counterparty and reference
            - Handle multiple statements per file
            - Write all transactions to one CSV
Input:      MT940 files
Tech stack: Python, mt-940
```

---

## Example 354

**Intent:**
I set a budget for each category every month, show me budget vs what I actually spent

**Spec:**
```
Type:       Command-line tool (budget vs actual report)
Features:   - Read the monthly budget per category from YAML
            - Read categorised transactions from CSV
            - Show budget, actual and difference per category
            - Colour categories over budget in red
            - Show year-to-date totals
Input:      Budget YAML and transactions CSV
Tech stack: Python, pandas, Rich
```

---

## Example 355

**Intent:**
depreciation schedule for the laptop and camera i bought for my business

**Spec:**
```
Type:       Command-line tool (depreciation calculator)
Features:   - Read assets with purchase date, cost and useful life
            - Calculate straight-line depreciation per year with a partial first year
            - Show the book value at each year end
            - Export the schedule for the tax return
Input:      Assets CSV
Tech stack: Python, pandas
```

---

## Example 356

**Intent:**
the school sent a new schedule ics, what changed from the old one?

**Spec:**
```
Type:       Command-line tool (calendar diff)
Features:   - Load two versions of an .ics calendar
            - Match events by UID and by title and date
            - List added, removed and moved events
            - Print changes sorted by date
Input:      Old and new .ics files
Tech stack: Python, icalendar
```

---

## Example 357

**Intent:**
phone numbers in our customer csv are in 10 formats, make them all +country format

**Spec:**
```
Type:       Command-line script (phone number normaliser)
Features:   - Read the phone column of a CSV
            - Parse numbers with a default country
            - Write them in E.164 format
            - Put invalid numbers in a separate report
Input:      CSV file, column name and default country
Tech stack: Python, phonenumbers, pandas
```

---

## Example 358

**Intent:**
take 1000 random rows from a 20gb csv

**Spec:**
```
Type:       Command-line tool (CSV random sampler)
Features:   - Stream the CSV without loading it into memory
            - Draw a uniform random sample with reservoir sampling
            - Keep the header row
            - Use a seed for repeatable samples
Input:      CSV file and sample size
Tech stack: Rust, csv crate, rand
```

---

## Example 359

**Intent:**
compare two exports of the same table and tell me which rows changed

**Spec:**
```
Type:       Command-line tool (CSV diff by key)
Features:   - Load two CSV files keyed by an ID column
            - Find added and removed rows
            - Find changed rows and show old and new values per column
            - Write the differences to a CSV or HTML report
Input:      Two CSV files and key column
Tech stack: Python, pandas
```

---

## Example 360

**Intent:**
run SQL queries on csv files without importing them anywhere

**Spec:**
```
Type:       Command-line tool (SQL over CSV)
Features:   - Register each CSV as a table named after the file
            - Run SQL queries with joins and aggregates
            - Infer column types automatically
            - Print results as a table or export to CSV
Input:      CSV files and a SQL query
Tech stack: Python, DuckDB
```

---

## Example 361

**Intent:**
merge several yaml config files into one, later ones override earlier

**Spec:**
```
Type:       Command-line tool (YAML config merger)
Features:   - Load YAML files in the given order
            - Deep-merge maps and replace or append lists as configured
            - Resolve anchors and aliases
            - Write the merged YAML and show which file set each key
Input:      YAML files in priority order
Tech stack: Python, ruamel.yaml
```

---

## Example 362

**Intent:**
json files show huge diffs in git just because keys move around. sort them

**Spec:**
```
Type:       Command-line tool (JSON canonicaliser)
Features:   - Sort object keys recursively
            - Use consistent indentation and a final newline
            - Optionally sort arrays of primitives
            - Run as a pre-commit hook on staged JSON files
Input:      JSON files
Tech stack: Node.js, json-stable-stringify
```

---

## Example 363

**Intent:**
turn a csv into SQL INSERT statements for our test db

**Spec:**
```
Type:       Command-line script (CSV to SQL inserts)
Features:   - Read a CSV and its header
            - Escape values and map empty cells to NULL
            - Generate multi-row INSERT statements for a table name
            - Write the SQL to a file
Input:      CSV file and table name
Tech stack: Python, csv module
```

---

## Example 364

**Intent:**
CI should fail if someone changed django models but forgot makemigrations

**Spec:**
```
Type:       Command-line script (missing migration check)
Features:   - Run makemigrations in check mode
            - Detect conflicting migrations with the same parent
            - Print which apps need new migrations
            - Exit with an error for the CI pipeline
Tech stack: Python, Django management commands, GitHub Actions
```

---

## Example 365

**Intent:**
check if all the api keys in our env file still work

**Spec:**
```
Type:       Command-line script (API key validity checker)
Features:   - Read keys from the .env file by known prefixes (Stripe, SendGrid, OpenWeather)
            - Call a cheap read-only endpoint for each service
            - Report valid, invalid and expired keys
            - Never print the keys themselves
Input:      .env file
Tech stack: Python, python-dotenv, httpx
```

---

## Example 366

**Intent:**
fake sftp server for our integration tests

**Spec:**
```
Type:       Command-line tool (test SFTP server)
Features:   - Start an SFTP server on a local port with a temporary root folder
            - Create users from a config with password or key login
            - Pre-load fixture files
            - Log every upload and download
Input:      Port and users config
Tech stack: Python, paramiko (SFTP server interface)
```

---

## Example 367

**Intent:**
lint our CHANGELOG.md so it follows keep a changelog

**Spec:**
```
Type:       Command-line tool (changelog format linter)
Features:   - Check that versions are in descending order with dates
            - Allow only the standard sections (Added, Changed, Deprecated, Removed, Fixed, Security)
            - Require an Unreleased section at the top
            - Check that comparison links exist for every version
Input:      CHANGELOG.md
Tech stack: Node.js, remark, commander
```

---

## Example 368

**Intent:**
we use calendar versioning like 2026.11.2, tag the next release automatically

**Spec:**
```
Type:       Command-line tool (CalVer release tagger)
Features:   - Find the latest CalVer tag in the repository
            - Compute the next version from today's date and a micro counter
            - Update version files
            - Create and push the annotated tag
Input:      Repository path
Tech stack: Python, GitPython
```

---

## Example 369

**Intent:**
make the NOTICE file with all the apache licensed dependencies

**Spec:**
```
Type:       Command-line script (NOTICE file generator)
Features:   - List dependencies with Apache-2.0 licenses
            - Download each package's NOTICE file if it has one
            - Combine them into one NOTICE file with headers
            - Show packages without a NOTICE
Input:      Project lockfile
Tech stack: Python, requests
```

---

## Example 370

**Intent:**
are the base images in our dockerfiles old?

**Spec:**
```
Type:       Command-line tool (base image freshness report)
Features:   - Find FROM lines in all Dockerfiles in a repository
            - Look up the creation date of each base image tag
            - Find newer tags in the same version line
            - Report images older than 90 days
Input:      Repository path
Tech stack: Go, go-containerregistry
```

---

## Example 371

**Intent:**
automatically mark flaky pytest tests with a quarantine marker so they dont block merges

**Spec:**
```
Type:       Command-line tool (flaky test quarantine)
Features:   - Read the list of flaky tests from the flakiness report
            - Add a quarantine marker to each test function in the code
            - Configure pytest so quarantined tests run but do not fail the build
            - Remove the marker when a test has been stable for 2 weeks
Input:      Flaky tests JSON and test folder
Tech stack: Python, libcst, pytest
```

---

## Example 372

**Intent:**
my cron jobs sometimes run twice at once and hang forever

**Spec:**
```
Type:       Command-line tool (cron job wrapper)
Features:   - Take a lock file so only one instance runs
            - Kill the job after a timeout
            - Capture output and only email it when the job fails
            - Record start, end and exit code to a log
Input:      Job name, timeout and command
Tech stack: Go, syscall flock, os/exec
```

---

## Example 373

**Intent:**
Our factory server has no internet. I need to move docker images there on a USB stick.

**Spec:**
```
Type:       Command-line script (offline Docker image transfer)
Features:   - Read a list of images and pull them
            - Save them into one compressed tar with a checksum file
            - Verify the checksum on the offline server
            - Load the images and retag them for the local registry
Input:      Images list file
Tech stack: Bash, Docker CLI, sha256sum
```

---

## Example 374

**Intent:**
someone started containers by hand on the server with docker run, make a compose file from them

**Spec:**
```
Type:       Command-line tool (compose file from running containers)
Features:   - Inspect running containers
            - Extract image, ports, volumes, environment and restart policy
            - Write a docker-compose.yml with one service per container
            - Leave out default values to keep the file short
Tech stack: Python, docker SDK, PyYAML
```

---

## Example 375

**Intent:**
before upgrading kubernetes find manifests that use removed api versions

**Spec:**
```
Type:       Command-line tool (deprecated Kubernetes API finder)
Features:   - Scan YAML manifests and Helm-rendered output
            - Compare apiVersion and kind with the removal list for the target version
            - Show each file and the replacement API version
            - Exit non-zero when removed APIs are found
Input:      Manifest folder and target Kubernetes version
Tech stack: Go, sigs.k8s.io/yaml, cobra
```

---

## Example 376

**Intent:**
show resource quota usage of every namespace

**Spec:**
```
Type:       Command-line tool (namespace quota report)
Features:   - List ResourceQuota objects in every namespace
            - Show used and hard limits for CPU, memory and pods
            - Highlight namespaces above 80% of any quota
            - Output as table or JSON
Tech stack: Python, kubernetes client, Rich
```

---

## Example 377

**Intent:**
which image version is running in each cluster for every deployment, dev stage prod side by side

**Spec:**
```
Type:       Command-line tool (cross-cluster version matrix)
Features:   - Connect to several kubeconfig contexts
            - List deployments and their container image tags
            - Build a table with one column per cluster
            - Highlight deployments whose versions differ
Input:      Context names and namespace
Tech stack: Go, client-go, tablewriter
```

---

## Example 378

**Intent:**
are we using our azure reserved instances or wasting them

**Spec:**
```
Type:       Command-line script (Azure reservation utilisation report)
Features:   - Fetch reservation utilisation from the Azure Consumption API
            - Show used and unused hours per reservation
            - List reservations below 80% utilisation
            - Estimate the money wasted per month
Tech stack: Python, azure-mgmt-consumption, pandas
```

---

## Example 379

**Intent:**
delete old ebs snapshots and amis we dont need anymore

**Spec:**
```
Type:       Command-line script (AWS snapshot and AMI cleanup)
Features:   - List snapshots and AMIs owned by the account
            - Skip snapshots used by a registered AMI
            - Select items older than the retention days without a keep tag
            - Delete them after confirmation and print the storage saved
Input:      Retention days and regions
Tech stack: Python, boto3
```

---

## Example 380

**Intent:**
record my terminal and make a gif for the readme

**Spec:**
```
Type:       Command-line tool (terminal session recorder)
Features:   - Record a shell session with timing to a cast file
            - Cut long pauses to a maximum length
            - Render the recording to an animated GIF with a chosen theme and font size
            - Replay the recording in the terminal
Input:      Output file name
Tech stack: Rust, portable-pty, gifski
```

---

## Example 381

**Intent:**
users always forget to say what system they have when they report bugs, give them a command that prints all the info

**Spec:**
```
Type:       Command-line tool (system info report for bug reports)
Features:   - Collect OS version, CPU, RAM, disk space and GPU
            - Collect the versions of our app and its main dependencies
            - Remove the user name and home path from the output
            - Print Markdown ready to paste into an issue and copy it to the clipboard
Tech stack: Python, psutil, platform module, pyperclip
```

---

## Example 382

**Intent:**
powershell script that lists all installed software with version on our windows pcs

**Spec:**
```
Type:       Command-line script (Windows software inventory)
Features:   - Read installed programs from the 32-bit and 64-bit uninstall registry keys
            - Collect name, version, publisher and install date
            - Run on remote PCs with Invoke-Command
            - Export one CSV with the computer name per row
Input:      List of computer names
Tech stack: PowerShell, Invoke-Command, Export-Csv
```

---

## Example 383

**Intent:**
windows: clean temp files and update all apps with winget every week

**Spec:**
```
Type:       Scheduled script (Windows maintenance)
Features:   - Delete files older than 7 days from user and system temp folders
            - Empty the recycle bin
            - Run winget upgrade for all packages silently
            - Write a log file with freed space and updated apps
Tech stack: PowerShell, winget, Task Scheduler
```

---

## Example 384

**Intent:**
mac: run my script every hour, I don't understand launchd plist files

**Spec:**
```
Type:       Command-line tool (launchd job generator)
Features:   - Ask for the script path, interval or calendar time and log file
            - Generate a LaunchAgent plist
            - Load it with launchctl and show its status
            - Unload and remove a job by label
Input:      Script path and schedule
Tech stack: Python, plistlib, Click
```

---

## Example 385

**Intent:**
which apps on my mac havent i opened in 6 months

**Spec:**
```
Type:       Command-line script (unused Mac app finder)
Features:   - List apps in /Applications and ~/Applications
            - Read each app's last used date from Spotlight metadata
            - Show apps not used in the given months with their size
            - Sort by size
Input:      Number of months
Tech stack: Bash, mdls, du
```

---

## Example 386

**Intent:**
print address labels from a csv on my brother label printer

**Spec:**
```
Type:       Command-line tool (label printer tool)
Features:   - Read addresses from a CSV
            - Lay out each address on the chosen label size
            - Send labels to a Brother QL printer over USB or network
            - Preview a label as PNG before printing
Input:      CSV file and label size
Tech stack: Python, brother_ql, Pillow
```

---

## Example 387

**Intent:**
find weak or old ssh keys in my .ssh folder

**Spec:**
```
Type:       Command-line script (SSH key strength audit)
Features:   - Find private and public keys in ~/.ssh
            - Read key type and bit length
            - Flag DSA keys and RSA keys under 3072 bits
            - Flag private keys without a passphrase
            - Suggest the command to create an ed25519 key
Tech stack: Python, cryptography
```

---

## Example 388

**Intent:**
rotate the postgres password for an app and update the kubernetes secret too

**Spec:**
```
Type:       Command-line script (database credential rotation)
Features:   - Generate a strong random password
            - Change the database user's password
            - Update the Kubernetes secret with the new value
            - Restart the deployment with a rolling restart
            - Verify the app connects after restart
Input:      Database user, secret name and deployment
Tech stack: Python, psycopg, kubernetes client
```

---

## Example 389

**Intent:**
find duplicate and weak passwords in 1password using its cli

**Spec:**
```
Type:       Command-line script (password vault audit)
Features:   - List all login items with the 1Password CLI
            - Read passwords in memory only
            - Find passwords reused across items
            - Flag passwords shorter than 12 characters
            - Print item titles only, never passwords
Tech stack: Bash, 1Password CLI (op), jq
```

---

## Example 390

**Intent:**
export all members of an active directory group to excel incl nested groups

**Spec:**
```
Type:       Command-line script (AD group member export)
Features:   - Connect to Active Directory over LDAPS
            - Resolve members of a group recursively
            - Collect name, email, department and account status
            - Export to an .xlsx file
Input:      Group name and domain controller
Tech stack: Python, ldap3, openpyxl
```

---

## Example 391

**Intent:**
disabled accounts in AD that are still in groups, clean up

**Spec:**
```
Type:       Command-line script (disabled account group cleanup)
Features:   - Find disabled user accounts in Active Directory
            - List the groups each one is still a member of
            - Remove them from groups after confirmation
            - Log every removal to a CSV
Tech stack: PowerShell, ActiveDirectory module
```

---

## Example 392

**Intent:**
how many microsoft 365 licenses do we pay for that nobody uses

**Spec:**
```
Type:       Command-line script (Microsoft 365 license usage report)
Auth:       Azure AD app registration (client credentials)
Features:   - Fetch subscribed license SKUs and assigned counts from Microsoft Graph
            - List users with licenses who have not signed in for 60 days
            - Calculate the monthly cost of unused licenses
            - Export the report to CSV
Tech stack: Python, msgraph-sdk, pandas
```

---

## Example 393

**Intent:**
google workspace users who didnt log in for 90 days

**Spec:**
```
Type:       Command-line script (inactive Workspace user report)
Auth:       Google service account with domain-wide delegation
Features:   - List all users through the Admin SDK Directory API
            - Read the last login time of each user
            - List users inactive for more than 90 days
            - Suspend them when a flag is given
Tech stack: Python, google-api-python-client
```

---

## Example 394

**Intent:**
archive slack channels with no messages in 6 months

**Spec:**
```
Type:       Scheduled script (inactive Slack channel archiver)
Features:   - List all public channels
            - Read the latest message timestamp of each channel
            - Post a warning in channels inactive for 5 months
            - Archive channels inactive for 6 months
            - Skip channels on an allowlist
Tech stack: Python, slack_sdk, cron
```

---

## Example 395

**Intent:**
export the jira sprint to csv for my sprint review slides

**Spec:**
```
Type:       Command-line script (Jira sprint export)
Features:   - Find the active or given sprint on a board
            - Fetch issues with key, summary, status, assignee and story points
            - Calculate completed and carried-over points
            - Write the issues to CSV
Input:      Board ID and optional sprint name
Tech stack: Python, jira
```

---

## Example 396

**Intent:**
create 50 jira tickets from a csv

**Spec:**
```
Type:       Command-line script (Jira bulk issue creator)
Features:   - Read summary, description, type, labels and parent epic from CSV
            - Create each issue through the Jira REST API
            - Link sub-tasks to their parents
            - Write the created issue keys back into the CSV
Input:      Issues CSV and project key
Tech stack: Python, jira
```

---

## Example 397

**Intent:**
export all github issues of our repo to csv including comments

**Spec:**
```
Type:       Command-line script (GitHub issues export)
Features:   - Fetch all open and closed issues with pagination
            - Skip pull requests
            - Include labels, assignees, milestone and comments
            - Write issues to CSV and comments to a second CSV
Input:      Repository name and token
Tech stack: Python, PyGithub, pandas
```

---

## Example 398

**Intent:**
our confluence is full of outdated pages, list the ones nobody touched in 2 years

**Spec:**
```
Type:       Command-line script (stale Confluence page report)
Features:   - List pages in a Confluence space via the REST API
            - Read last modified date and author of each page
            - Select pages older than 2 years
            - Export a CSV with page owners for review
Input:      Space key
Tech stack: Python, atlassian-python-api
```

---

## Example 399

**Intent:**
cleanup notion markdown export, the filenames have long ids and links are broken

**Spec:**
```
Type:       Command-line script (Notion export cleaner)
Features:   - Remove the 32-character IDs from file and folder names
            - Rewrite links between pages to the new names
            - Decode URL-encoded characters in links
            - Move attachments next to their pages
Input:      Unzipped Notion export folder
Tech stack: Python, pathlib, regex
```

---

## Example 400

**Intent:**
todo.txt in the terminal but with due dates and repeating tasks

**Spec:**
```
Type:       Command-line tool (todo.txt manager)
Features:   - Add, complete and delete tasks in todo.txt format
            - Support due:YYYY-MM-DD and rec:1w tags
            - Create the next task when a recurring task is completed
            - List tasks due today and overdue
            - Archive done tasks to done.txt
Storage:    todo.txt and done.txt
Tech stack: Go, cobra
```

---

## Example 401

**Intent:**
barcodes for our products, EAN-13, as images for labels

**Spec:**
```
Type:       Command-line tool (EAN-13 barcode generator)
Features:   - Read product codes from a CSV
            - Calculate or check the EAN-13 check digit
            - Generate a barcode image per product
            - Export an A4 sheet of barcodes as PDF
Input:      Products CSV
Tech stack: Python, python-barcode, ReportLab
```

---

## Example 402

**Intent:**
check our shopify product import csv before uploading, it fails with weird errors

**Spec:**
```
Type:       Command-line tool (Shopify product CSV validator)
Features:   - Check the required Shopify columns exist
            - Check that variants share the handle and option names of their product
            - Validate prices, weights and image URLs
            - Report errors by row with a clear message
Input:      Product CSV
Tech stack: Python, pandas
```

---

## Example 403

**Intent:**
tell me when stock of a product in my woocommerce shop goes under 5

**Spec:**
```
Type:       Scheduled script (low stock alert)
Features:   - Fetch products and variations with stock levels from the WooCommerce REST API
            - Find items below their threshold
            - Send one email with the list and supplier names
            - Do not repeat alerts until stock is restocked
Storage:    JSON file of already alerted items
Tech stack: Python, woocommerce, smtplib, cron
```

---

## Example 404

**Intent:**
i sell on etsy and want my orders as csv for the post office shipping tool

**Spec:**
```
Type:       Command-line script (Etsy orders to shipping CSV)
Auth:       Etsy API OAuth
Features:   - Fetch unshipped orders from the Etsy API
            - Map buyer address fields to the carrier's import columns
            - Choose the parcel size from the product weights
            - Write the shipping CSV
Tech stack: Python, requests, pandas
```

---

## Example 405

**Intent:**
track all my parcels from different carriers in one list in the terminal

**Spec:**
```
Type:       Command-line tool (parcel tracker)
Data model: Parcel(tracking_number, carrier, description, last_status, updated_at)
Features:   - Add parcels by tracking number and detect the carrier
            - Fetch the latest status from a tracking API
            - Show all parcels with status and last update
            - Remove delivered parcels after a week
Storage:    SQLite
Tech stack: Python, Typer, requests
```

---

## Example 406

**Intent:**
make a changelog for our api users from the differences between two openapi versions

**Spec:**
```
Type:       Command-line tool (API changelog generator)
Features:   - Compare two OpenAPI files
            - List new, removed and changed endpoints
            - List changed request and response fields
            - Mark breaking changes
            - Write a Markdown changelog section
Input:      Old and new OpenAPI files
Tech stack: Go, oasdiff
```

---

## Example 407

**Intent:**
how many connections can our postgres handle before queries get slow

**Spec:**
```
Type:       Command-line tool (database connection stress test)
Features:   - Open an increasing number of concurrent connections
            - Run a configurable query mix on each
            - Measure query latency and errors at each level
            - Report the point where latency rises sharply
Input:      Database URL, maximum connections and query file
Storage:    PostgreSQL
Tech stack: Go, pgx, cobra
```

---

## Example 408

**Intent:**
realistic fake time series for demo dashboards, like website visits with daily and weekly patterns

**Spec:**
```
Type:       Command-line tool (synthetic time series generator)
Features:   - Generate values at a chosen interval over a date range
            - Add trend, daily and weekly seasonality and noise
            - Add random spikes and outages
            - Export as CSV or write to InfluxDB
Input:      Config YAML with patterns
Tech stack: Python, numpy, pandas
```

---

## Example 409

**Intent:**
after migrating the database, compare row counts between old and new

**Spec:**
```
Type:       Command-line script (migration row count comparison)
Features:   - Connect to source and target databases
            - Count rows in every table on both sides
            - Compare checksums of key columns for chosen tables
            - Print tables with mismatches
Input:      Two database URLs
Tech stack: Python, SQLAlchemy
```

---

## Example 410

**Intent:**
who has which permissions in our postgres

**Spec:**
```
Type:       Command-line script (PostgreSQL permission audit)
Features:   - List roles and their memberships
            - List table and schema privileges per role
            - Flag roles with superuser or no password expiry
            - Export the audit to CSV
Input:      Database URL
Tech stack: Python, psycopg
```

---

## Example 411

**Intent:**
we have many small sqlite databases from our app installs, check them all for corruption and compact them

**Spec:**
```
Type:       Command-line script (SQLite maintenance)
Features:   - Find .db files under a folder
            - Run PRAGMA integrity_check on each
            - Run VACUUM on healthy databases
            - Report corrupted files and space saved
Input:      Folder path
Tech stack: Python, sqlite3
```

---

## Example 412

**Intent:**
draw an er diagram of our database

**Spec:**
```
Type:       Command-line tool (ER diagram generator)
Features:   - Read tables, columns and foreign keys from a live database
            - Generate a Mermaid or Graphviz diagram
            - Filter to a list of tables or a schema
            - Render to SVG or PNG
Input:      Database URL and output format
Tech stack: Python, SQLAlchemy, graphviz
```

---

## Example 413

**Intent:**
data dictionary in markdown for all our tables

**Spec:**
```
Type:       Command-line tool (data dictionary generator)
Features:   - Read tables, columns, types, nullability and comments
            - Include primary and foreign keys
            - Write one Markdown file per schema with a table per database table
            - Keep manually written descriptions when regenerating
Input:      Database URL and output folder
Tech stack: Python, SQLAlchemy, Jinja2
```

---

## Example 414

**Intent:**
run cargo audit on all our rust repos every week and open issues for vulnerable crates

**Spec:**
```
Type:       Scheduled script (Rust dependency audit)
Features:   - Clone or update each Rust repository
            - Run cargo audit with JSON output
            - Open a GitHub issue per new advisory
            - Close issues whose advisory no longer applies
Tech stack: Bash, cargo-audit, GitHub CLI, jq, cron
```

---

## Example 415

**Intent:**
turn our junit test results into a simple html page the managers can understand

**Spec:**
```
Type:       Command-line tool (test report generator)
Features:   - Read JUnit XML files
            - Show totals of passed, failed and skipped tests with a pie chart
            - List failed tests with error messages
            - Group results by test suite
            - Write a single HTML file
Input:      JUnit XML files
Tech stack: Python, junitparser, Jinja2, Chart.js
```

---

## Example 416

**Intent:**
compare screenshots of our pages before and after a change, show the differences

**Spec:**
```
Type:       Command-line tool (visual regression checker)
Features:   - Take screenshots of a list of URLs at several screen widths
            - Compare them with baseline images pixel by pixel
            - Create diff images that highlight changes
            - Fail when the difference is above a threshold
            - Update baselines with a flag
Input:      URL list and baseline folder
Tech stack: Node.js, Playwright, pixelmatch
```

---

## Example 417

**Intent:**
list all scheduled tasks on our windows servers and when they last ran

**Spec:**
```
Type:       Command-line script (Windows scheduled task inventory)
Features:   - Query scheduled tasks on each server
            - Collect task name, run-as user, last run time and last result
            - Flag tasks that failed or run as a domain admin
            - Export to CSV
Input:      List of server names
Tech stack: PowerShell, Get-ScheduledTask, Get-ScheduledTaskInfo
```

---

## Example 418

**Intent:**
our private docker registry is full, delete old image tags but keep the newest 10

**Spec:**
```
Type:       Scheduled script (container registry cleanup)
Features:   - List repositories and tags through the Registry HTTP API
            - Sort tags by creation date
            - Delete all but the newest 10 tags and protected tags
            - Trigger garbage collection to free disk space
Tech stack: Python, requests, cron
```

---

## Example 419

**Intent:**
report when our kubernetes autoscaler scaled up or down this week

**Spec:**
```
Type:       Command-line script (HPA scaling events report)
Features:   - Read events for HorizontalPodAutoscalers in all namespaces
            - List scale up and scale down events with time and replica counts
            - Show deployments that hit their maximum replicas
            - Export to CSV
Tech stack: Python, kubernetes client, pandas
```

---

## Example 420

**Intent:**
drain a kubernetes node safely and check pods moved fine

**Spec:**
```
Type:       Command-line tool (node drain helper)
Features:   - Check PodDisruptionBudgets before draining
            - Cordon and drain the node with a timeout
            - Wait until evicted pods are running on other nodes
            - Print pods that failed to reschedule
Input:      Node name
Tech stack: Go, client-go, cobra
```

---

## Example 421

**Intent:**
gcp service account keys older than 90 days

**Spec:**
```
Type:       Scheduled script (GCP service account key audit)
Features:   - List service accounts in each project
            - List user-managed keys with creation date
            - Flag keys older than 90 days
            - Send the list to the security email
Tech stack: Python, google-cloud-iam, smtplib, cron
```

---

## Example 422

**Intent:**
add missing tags to our azure resources based on their resource group

**Spec:**
```
Type:       Command-line script (Azure tag enforcer)
Features:   - Read tag rules per resource group from YAML
            - List resources missing the required tags
            - Add the tags from the rules
            - Show a dry-run plan before applying
Input:      Rules YAML
Tech stack: Python, azure-mgmt-resource
```

---

## Example 423

**Intent:**
cost per namespace in our kubernetes cluster for each team, monthly

**Spec:**
```
Type:       Scheduled script (Kubernetes namespace cost report)
Features:   - Query the OpenCost API for cost per namespace over the last month
            - Map namespaces to teams with labels
            - Split idle cluster cost proportionally
            - Email a report to each team
Tech stack: Python, requests, pandas, smtplib, cron
```

---

## Example 424

**Intent:**
learn morse code in terminal

**Spec:**
```
Type:       Command-line tool (Morse code trainer)
Features:   - Play random letters as Morse audio at a set speed
            - Let the user type what they heard and score the answer
            - Add new letters gradually with the Koch method
            - Track accuracy per letter between sessions
Storage:    JSON progress file
Tech stack: Python, numpy, sounddevice
```

---

## Example 425

**Intent:**
test my regex against some lines and show what matched, in the terminal

**Spec:**
```
Type:       Command-line tool (regex tester)
Features:   - Read sample lines from a file or stdin
            - Highlight matches and capture groups in colour
            - Show named groups as a table
            - Explain each part of the pattern in plain words
Input:      Pattern and sample text
Tech stack: Python, regex, Rich
```

---

## Example 426

**Intent:**
Our team is in Berlin, New York and Bangalore. I want a command that shows a good meeting time for all of us.

**Spec:**
```
Type:       Command-line tool (time zone meeting planner)
Features:   - Read team members' time zones and working hours
            - Show a 24-hour grid of local times for each zone
            - Highlight hours inside everyone's working hours
            - Convert a chosen time to every zone
Input:      Date and list of time zones
Tech stack: Python, zoneinfo, Rich
```

---

## Example 427

**Intent:**
how many working days between two dates without holidays

**Spec:**
```
Type:       Command-line tool (working day calculator)
Features:   - Count weekdays between two dates
            - Exclude public holidays for a country and region
            - Add a number of working days to a date
            - Show the list of excluded holidays
Input:      Dates, country and region
Tech stack: Python, holidays, Click
```

---

## Example 428

**Intent:**
httpie but i can save requests per project and reuse them

**Spec:**
```
Type:       Command-line tool (HTTP request collection runner)
Features:   - Save named requests with method, URL, headers and body in a project file
            - Use variables from environment files (dev, prod)
            - Run a saved request and pretty-print the response
            - Extract values from responses into variables for the next request
Input:      Request name and environment
Storage:    YAML file in the project folder
Tech stack: Go, net/http, cobra
```

---

## Example 429

**Intent:**
switching aws profiles and doing mfa every time is so slow

**Spec:**
```
Type:       Command-line tool (AWS profile and MFA helper)
Features:   - List profiles from the AWS config
            - Ask for the MFA code and get temporary credentials with STS
            - Cache the session until it expires
            - Export the credentials into the current shell
Input:      Profile name and MFA code
Tech stack: Python, boto3, Click
```

---

## Example 430

**Intent:**
log into 30 aws accounts with sso and make profiles for all of them automatically

**Spec:**
```
Type:       Command-line tool (AWS SSO profile generator)
Features:   - Log in to AWS IAM Identity Center with the device flow
            - List all accounts and roles the user can access
            - Write a named profile for each account and role to ~/.aws/config
            - Keep existing manual profiles unchanged
Tech stack: Python, boto3 (sso, sso-oidc)
```

---

## Example 431

**Intent:**
how big is every s3 bucket and how many files

**Spec:**
```
Type:       Command-line script (S3 bucket size report)
Features:   - List all buckets
            - Read size and object count from CloudWatch storage metrics
            - Split size by storage class
            - Print a table sorted by size
Tech stack: Python, boto3
```

---

## Example 432

**Intent:**
after deploy, invalidate cloudfront cache only for the files that changed

**Spec:**
```
Type:       Command-line script (CloudFront selective invalidation)
Features:   - Compare local build files with the S3 objects by ETag
            - Upload changed files
            - Create an invalidation for only the changed paths
            - Wait until the invalidation is complete
Input:      Build folder, bucket and distribution ID
Tech stack: Python, boto3
```

---

## Example 433

**Intent:**
we moved to a new server, which of our 60 domains still point at the old ip?

**Spec:**
```
Type:       Command-line script (domain IP checker)
Features:   - Read domains from a file
            - Resolve A and AAAA records for the domain and www
            - Flag domains resolving to the old IP
            - Print a table of domains and their current IPs
Input:      Domains file and old IP
Tech stack: Python, dnspython
```

---

## Example 434

**Intent:**
i have a pile of .crt and .key files and don't know which key belongs to which cert

**Spec:**
```
Type:       Command-line tool (certificate and key matcher)
Features:   - Read all certificate and private key files in a folder
            - Compare the public key of each certificate with each private key
            - Print matching pairs with subject and expiry
            - List certificates without a key
Input:      Folder of PEM files
Tech stack: Python, cryptography
```

---

## Example 435

**Intent:**
check from outside which ports on my home ip are open

**Spec:**
```
Type:       Command-line script (external port exposure check)
Features:   - Connect to a remote VPS over SSH
            - Scan the home public IP from the VPS for common ports
            - Compare open ports with the expected list
            - Report unexpected open ports
Input:      VPS host and expected ports
Tech stack: Bash, ssh, nmap
```

---

## Example 436

**Intent:**
how much space does each docker volume use and which container uses it

**Spec:**
```
Type:       Command-line script (Docker volume usage report)
Features:   - List all volumes with their mount points
            - Measure the size of each volume
            - Show containers that mount each volume
            - Mark volumes with no container
Tech stack: Bash, Docker CLI, du, jq
```

---

## Example 437

**Intent:**
I exported my Spotify liked songs as CSV. Which of them do I not have in my local music collection yet?

**Spec:**
```
Type:       Command-line script (missing songs finder)
Features:   - Read artist and title from the Spotify CSV
            - Read tags from the local music library
            - Match songs with fuzzy name matching
            - List songs missing locally grouped by artist
Input:      Spotify CSV and music folder
Tech stack: Python, mutagen, rapidfuzz
```

---

## Example 438

**Intent:**
put lyrics from my .lrc files into the mp3 tags so my player shows them

**Spec:**
```
Type:       Command-line script (lyrics embedder)
Features:   - Find .lrc files next to audio files with the same name
            - Embed synced lyrics as SYLT and plain lyrics as USLT frames
            - Skip files that already have lyrics
            - Report audio files without lyrics
Input:      Music folder
Tech stack: Python, mutagen
```

---

## Example 439

**Intent:**
same book bought twice in different editions, find duplicate ebooks by isbn or title

**Spec:**
```
Type:       Command-line script (duplicate ebook finder)
Features:   - Read ISBN, title and author from EPUB and PDF metadata
            - Group books with the same ISBN
            - Group books with very similar title and author
            - Show each group with file size and format
Input:      Ebook library folder
Tech stack: Python, ebooklib, pypdf, rapidfuzz
```

---

## Example 440

**Intent:**
only download the podcast episodes about topics i like, not all of them

**Spec:**
```
Type:       Scheduled script (keyword podcast downloader)
Features:   - Read feeds and keyword lists from config
            - Check new episodes' titles and descriptions for keywords
            - Download only matching episodes
            - Send a notification with the downloaded titles
Storage:    SQLite (seen episodes)
Tech stack: Python, feedparser, requests, cron
```

---

## Example 441

**Intent:**
pull the subtitles out of all my mkv files as srt

**Spec:**
```
Type:       Command-line script (MKV subtitle extractor)
Features:   - List subtitle tracks of each MKV with language and codec
            - Extract text tracks as SRT files
            - Name files with the track language code
            - Skip image-based subtitle tracks and report them
Input:      Folder of MKV files
Tech stack: Bash, mkvmerge, mkvextract, jq
```

---

## Example 442

**Intent:**
make invoices from my toggl time entries

**Spec:**
```
Type:       Command-line tool (Toggl to invoice)
Features:   - Fetch time entries for a client and month from the Toggl API
            - Group hours by project and task
            - Apply the client's hourly rate
            - Generate an invoice PDF with the hour breakdown
Input:      Client name, month and Toggl API token
Tech stack: Python, requests, WeasyPrint
```

---

## Example 443

**Intent:**
paypal csv is a mess, i want a clean list of sales and the fees for my bookkeeping

**Spec:**
```
Type:       Command-line script (PayPal report cleaner)
Features:   - Read the PayPal activity CSV
            - Keep completed payments and refunds only
            - Split gross, fee and net into separate columns
            - Convert foreign currency rows using PayPal's conversion lines
            - Write a monthly summary of sales and fees
Input:      PayPal CSV export
Tech stack: Python, pandas
```

---

## Example 444

**Intent:**
I use my phone and internet half for work, calculate the business part of the bills for my tax return

**Spec:**
```
Type:       Command-line script (business use expense calculator)
Features:   - Read monthly bills from CSV with category
            - Apply the business use percentage per category
            - Total the deductible amount per category for the year
            - Write a summary CSV for the tax advisor
Input:      Bills CSV and percentages YAML
Tech stack: Python, pandas
```

---

## Example 445

**Intent:**
print a wall planner for next year as a big pdf with holidays marked

**Spec:**
```
Type:       Command-line tool (year planner PDF)
Features:   - Draw a 12-month grid on A2 or A3 paper
            - Mark weekends and public holidays
            - Add birthdays from a CSV
            - Export a print-ready PDF
Input:      Year, country and paper size
Tech stack: Python, ReportLab, holidays
```

---

## Example 446

**Intent:**
stats from our whatsapp group chat export, who writes the most lol

**Spec:**
```
Type:       Command-line script (chat export statistics)
Features:   - Parse the exported chat text file
            - Count messages and words per person
            - Show the busiest hours and days
            - List the most used emojis
            - Print a summary and save charts as PNG
Input:      Chat export .txt file
Tech stack: Python, pandas, matplotlib, emoji
```

---

## Example 447

**Intent:**
numbers in my csv are like 1.234,56 (german) and excel breaks them

**Spec:**
```
Type:       Command-line script (decimal format converter)
Features:   - Detect columns with numbers in European format
            - Convert 1.234,56 to 1234.56
            - Leave text columns unchanged
            - Write the converted CSV
Input:      CSV file and optional column list
Tech stack: Python, pandas
```

---

## Example 448

**Intent:**
quick chart from a csv right in the terminal

**Spec:**
```
Type:       Command-line tool (terminal CSV charting)
Features:   - Read a CSV and choose x and y columns
            - Draw line, bar or scatter charts in the terminal
            - Group and sum values by a column
            - Save the chart as PNG when asked
Input:      CSV file and column names
Tech stack: Python, plotext, pandas
```

---

## Example 449

**Intent:**
generate readable docs from our json schemas

**Spec:**
```
Type:       Command-line tool (JSON Schema documentation generator)
Features:   - Read JSON Schema files with $ref references
            - Write a Markdown page per schema with a table of properties
            - Show types, required fields, enums and examples
            - Link referenced schemas between pages
Input:      Schemas folder and output folder
Tech stack: Python, jsonschema, Jinja2
```

---

## Example 450

**Intent:**
pin all github actions in our workflows to commit sha for security

**Spec:**
```
Type:       Command-line tool (GitHub Actions pinner)
Features:   - Find uses: lines in workflow YAML files
            - Resolve each tag to its commit SHA through the GitHub API
            - Replace the tag with the SHA and keep the tag as a comment
            - Report actions from unverified publishers
Input:      Repository path and GitHub token
Tech stack: Go, go-github, yaml.v3
```

---

## Example 451

**Intent:**
fill our firestore emulator with test data from json

**Spec:**
```
Type:       Command-line tool (Firestore seeder)
Features:   - Read collection documents from JSON files
            - Create subcollections from nested keys
            - Convert date strings to Firestore timestamps
            - Clear the emulator before seeding
Input:      Data folder and emulator host
Storage:    Firestore emulator
Tech stack: Node.js, firebase-admin
```

---

## Example 452

**Intent:**
we have 400 sql migration files, squash them into one baseline

**Spec:**
```
Type:       Command-line tool (migration squasher)
Features:   - Apply all migrations to an empty temporary database
            - Dump the resulting schema as one baseline SQL file
            - Mark the old migrations as applied in existing databases
            - Move old files into an archive folder
Input:      Migrations folder and database engine
Tech stack: Python, Docker, pg_dump
```

---

## Example 453

**Intent:**
some graphql queries kill our server, test the cost of our common queries

**Spec:**
```
Type:       Command-line tool (GraphQL query cost tester)
Features:   - Load query files and the schema
            - Calculate query depth and estimated cost per query
            - Run each query and measure response time
            - Flag queries over depth or cost limits
Input:      Queries folder and GraphQL endpoint
Tech stack: Node.js, graphql, graphql-query-complexity
```

---

## Example 454

**Intent:**
fake oauth login server for local development so i dont need real google login

**Spec:**
```
Type:       Command-line tool (mock OAuth2 provider)
Features:   - Serve authorize, token and userinfo endpoints for local use
            - Show a page to pick a test user instead of a password
            - Issue signed JWT access and ID tokens
            - Load test users and claims from a YAML file
API:        REST
            GET  /authorize
            POST /token
            GET  /userinfo
            GET  /.well-known/openid-configuration
Tech stack: Python, FastAPI, PyJWT
```

---

## Example 455

**Intent:**
reject commits whose message doesnt follow conventional commits

**Spec:**
```
Type:       Command-line tool (commit message linter)
Features:   - Check the message format type(scope): subject
            - Allow only configured types and scopes
            - Limit subject length
            - Run as a commit-msg git hook and in CI for a commit range
Input:      Commit message file or commit range
Tech stack: Rust, regex, git2
```

---

## Example 456

**Intent:**
will this go library release break people? check exported API changes

**Spec:**
```
Type:       Command-line tool (Go API compatibility checker)
Features:   - Compare exported identifiers between the last tag and the current code
            - Classify changes as compatible or incompatible
            - Suggest the next semantic version
            - Fail CI when an incompatible change has no major bump
Input:      Module path and previous tag
Tech stack: Go, golang.org/x/exp/apidiff
```

---

## Example 457

**Intent:**
which npm packages run install scripts, we want to know before installing

**Spec:**
```
Type:       Command-line tool (npm install script audit)
Features:   - Read the full dependency tree from package-lock.json
            - Find packages with preinstall, install or postinstall scripts
            - Show the script content for each
            - Compare with an approved list
Input:      Project folder
Tech stack: Node.js, @npmcli/arborist
```

---

## Example 458

**Intent:**
run one test 50 times to see if it is really flaky

**Spec:**
```
Type:       Command-line tool (test repeat runner)
Features:   - Run a single test command many times
            - Run in parallel with a worker limit
            - Count passes and failures
            - Save the output of failing runs
Input:      Test command and number of runs
Tech stack: Go, os/exec, cobra
```

---

## Example 459

**Intent:**
show me a timeline of when all my cron jobs run tomorrow so I see overlaps

**Spec:**
```
Type:       Command-line tool (crontab timeline)
Features:   - Parse all user and system crontabs
            - Compute every run time in a 24-hour window
            - Draw a timeline per job in the terminal
            - Highlight times when more than 3 jobs start at once
Input:      Date
Tech stack: Python, croniter, Rich
```

---

## Example 460

**Intent:**
which of my containers run as root

**Spec:**
```
Type:       Command-line script (root container check)
Features:   - Inspect every running container
            - Read the user the main process runs as
            - Check for privileged mode and added capabilities
            - Print a table and flag risky containers
Tech stack: Python, docker SDK
```

---

## Example 461

**Intent:**
docker logs filled my disk, show size per container and truncate the big ones

**Spec:**
```
Type:       Command-line script (Docker log size manager)
Features:   - Find the JSON log file of each container
            - Show log size per container
            - Truncate logs above a size after confirmation
            - Print the daemon.json settings to rotate logs
Tech stack: Bash, Docker CLI, jq, truncate
```

---

## Example 462

**Intent:**
check that all hostnames in our kubernetes ingresses resolve and have valid tls

**Spec:**
```
Type:       Command-line tool (ingress host checker)
Features:   - List Ingress resources in all namespaces
            - Resolve each host name
            - Check the TLS certificate is valid for the host
            - Report hosts with DNS or certificate problems
Tech stack: Go, client-go, crypto/tls
```

---

## Example 463

**Intent:**
our persistent volumes fill up and nobody notices

**Spec:**
```
Type:       Scheduled script (PVC usage alert)
Features:   - Query kubelet volume stats from Prometheus for every PVC
            - Calculate used percentage
            - Alert at 80% and 90% with namespace and pod
            - Post alerts to Slack
Tech stack: Python, prometheus-api-client, Slack webhook, cron
```

---

## Example 464

**Intent:**
when i change a configmap restart the deployments that use it

**Spec:**
```
Type:       Command-line tool (configmap restart helper)
Features:   - Find deployments that mount the ConfigMap or use it as env
            - Trigger a rolling restart for each
            - Wait until each rollout is complete
            - Print the restarted deployments
Input:      ConfigMap name and namespace
Tech stack: Go, client-go
```

---

## Example 465

**Intent:**
which lambda functions cost the most

**Spec:**
```
Type:       Command-line script (Lambda cost per function)
Features:   - Read invocations and duration per function from CloudWatch
            - Calculate cost from memory size, duration and request price
            - Rank functions by monthly cost
            - Suggest functions that may have too much memory
Tech stack: Python, boto3, pandas
```

---

## Example 466

**Intent:**
data transfer is a big part of our aws bill, break it down

**Spec:**
```
Type:       Command-line script (AWS data transfer cost breakdown)
Features:   - Query Cost Explorer filtered by data transfer usage types
            - Group cost by source region, destination and service
            - Show the top transfer paths
            - Compare with last month
Tech stack: Python, boto3, pandas
```

---

## Example 467

**Intent:**
list every public ip we have in all our aws accounts

**Spec:**
```
Type:       Command-line script (AWS public IP inventory)
Features:   - Assume a read-only role in each account
            - List Elastic IPs, public EC2 IPs and load balancer addresses in every region
            - Write account, region, resource and IP to CSV
Input:      List of account IDs and role name
Tech stack: Python, boto3
```

---

## Example 468

**Intent:**
our s3 buckets keep old versions and junk forever, suggest lifecycle rules

**Spec:**
```
Type:       Command-line script (S3 lifecycle recommender)
Features:   - Check each bucket for versioning and existing lifecycle rules
            - Measure noncurrent version storage and incomplete multipart uploads
            - Suggest rules to expire old versions and move old objects to cheaper classes
            - Estimate the monthly savings
Tech stack: Python, boto3
```

---

## Example 469

**Intent:**
homepage for my homelab that lists all my docker services with links, made automatically

**Spec:**
```
Type:       Command-line script (homelab dashboard generator)
Features:   - Read running containers and their labels
            - Build links from host names and published ports
            - Group services by a label
            - Write a static HTML page with icons
            - Regenerate when containers change
Tech stack: Python, docker SDK, Jinja2
```

---

## Example 470

**Intent:**
notify me when the power goes out and my ups is on battery

**Spec:**
```
Type:       Scheduled script (UPS status notifier)
Features:   - Read UPS status from Network UPS Tools every 30 seconds
            - Send a notification when the UPS switches to battery
            - Report battery charge and runtime left
            - Shut down chosen servers when the battery is low
Tech stack: Bash, upsc, ssh, ntfy.sh
```

---

## Example 471

**Intent:**
proxmox has too many old vm snapshots, delete ones older than 2 weeks

**Spec:**
```
Type:       Scheduled script (Proxmox snapshot cleanup)
Features:   - List VMs and containers on each node through the Proxmox API
            - List their snapshots with creation time
            - Delete snapshots older than the retention days except those named keep
            - Log what was deleted
Tech stack: Python, proxmoxer, cron
```

---

## Example 472

**Intent:**
daily summary from my pihole, how many ads blocked and top domains

**Spec:**
```
Type:       Scheduled script (Pi-hole daily summary)
Features:   - Query the Pi-hole API for yesterday's stats
            - Get total queries, blocked percentage and top blocked domains
            - List new clients seen on the network
            - Send the summary as a message
Tech stack: Python, requests, Telegram Bot API, cron
```

---

## Example 473

**Intent:**
walk around my house with the laptop and map where the wifi is weak

**Spec:**
```
Type:       Command-line tool (Wi-Fi signal survey)
Features:   - Ask for the room name at each point
            - Measure signal strength, noise and link speed
            - Repeat the measurement 5 times and average
            - Show a table of rooms ranked by signal
Storage:    CSV of measurements
Tech stack: Python, nmcli, Rich
```

---

## Example 474

**Intent:**
my internet keeps dropping, log every outage with time and how long

**Spec:**
```
Type:       Scheduled script (internet outage logger)
Features:   - Check connectivity to several hosts every 30 seconds
            - Record an outage when all checks fail
            - Record when the connection comes back and the duration
            - Print a monthly outage summary
Storage:    SQLite
Tech stack: Python, icmplib, systemd service
```

---

## Example 475

**Intent:**
are the clocks on our servers drifting

**Spec:**
```
Type:       Command-line script (NTP drift check)
Features:   - Connect to each server over SSH
            - Read the clock offset from chrony or timedatectl
            - Flag servers with offset above 100 ms or unsynchronised
            - Print a table sorted by offset
Input:      Server inventory
Tech stack: Bash, ssh, chronyc
```

---

## Example 476

**Intent:**
which of my servers need a reboot after updates

**Spec:**
```
Type:       Command-line script (reboot required check)
Features:   - Check each server for /var/run/reboot-required
            - List the packages that require the reboot
            - Show uptime and running kernel versus installed kernel
            - Print servers sorted by uptime
Input:      Server inventory
Tech stack: Bash, ssh
```

---

## Example 477

**Intent:**
hey can u make a small tool where i paste a cron line and it tells me if it would clash with my other jobs on the server

**Spec:**
```
Type:       Command-line tool (cron schedule clash checker)
Features:   - Read the existing crontab of the server
            - Parse the new cron expression
            - Find times in the next week when it runs together with other jobs
            - Show the clashing jobs and times
Input:      Cron expression and crontab file
Tech stack: Python, croniter
```

---

## Example 478

**Intent:**
i'm doctoral student, my experiments write many result json files, i need tool to collect all into one table and check no run is missing from the grid

**Spec:**
```
Type:       Command-line script (experiment results collector)
Features:   - Find result JSON files in run folders
            - Read parameters and metrics from each file
            - Build one table with a row per run
            - Compare with the expected parameter grid and list missing runs
            - Export to CSV
Input:      Results folder and grid config YAML
Tech stack: Python, pandas, PyYAML
```

---

## Example 479

**Intent:**
check that every server has the same ssh settings, like no root login and no password login

**Spec:**
```
Type:       Command-line script (SSH hardening audit)
Features:   - Read sshd_config on each server over SSH
            - Check PermitRootLogin, PasswordAuthentication and allowed ciphers
            - Compare with the required settings
            - Print a pass or fail table per server and setting
Input:      Server inventory and required settings
Tech stack: Python, Paramiko
```

---

## Example 480

**Intent:**
list which of my python projects use an old python version

**Spec:**
```
Type:       Command-line script (Python version inventory)
Features:   - Find pyproject.toml, setup.cfg and .python-version files under a folder
            - Read the required Python version of each project
            - Flag projects that need an end-of-life version
            - Print a table of projects and versions
Input:      Root folder of projects
Tech stack: Python, tomllib, packaging
```

---

## Example 481

**Intent:**
Sync my contact birthdays and anniversaries from a CSV into a separate calendar on Nextcloud.

**Spec:**
```
Type:       Command-line script (CSV dates to CalDAV calendar)
Features:   - Read names, birthdays and anniversaries from a CSV
            - Create yearly recurring all-day events
            - Update existing events instead of creating duplicates
            - Upload events to a Nextcloud calendar over CalDAV
Input:      CSV file, CalDAV URL and app password
Tech stack: Python, caldav, icalendar
```

---

