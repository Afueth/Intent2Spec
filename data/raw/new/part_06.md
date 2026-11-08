## Example 1

**Intent:**
sort my downloads folder by file type

**Spec:**
```
Type:       Command-line script (file organizer)
Features:   - Scan the Downloads folder (top level only)
            - Map extensions to categories (Documents, Images, Video, Archives, Installers)
            - Move each file into a matching subfolder, creating it if missing
            - Append a counter when a file with the same name already exists
            - Print a summary of how many files were moved per category
Input:      Path to the folder (defaults to ~/Downloads), optional --dry-run flag
Tech stack: Python, pathlib, shutil
```

---

## Example 2

**Intent:**
find duplicate photos on my external drive and tell me which ones I can delete

**Spec:**
```
Type:       Command-line tool (duplicate finder)
Features:   - Walk the drive recursively and collect image files
            - Group files by size first, then compare SHA-256 hashes within each group
            - List each duplicate group with paths and sizes
            - Write a CSV report of files safe to delete (all but the oldest copy)
            - Optionally move duplicates to a quarantine folder instead of deleting
Input:      Root path of the drive, --report path, --quarantine path
Tech stack: Python, hashlib, os.walk, csv
```

---

## Example 3

**Intent:**
convert a whole folder of word docs to pdf

**Spec:**
```
Type:       Command-line script (format conversion)
Features:   - Find all .doc and .docx files in a folder
            - Convert each one to PDF with LibreOffice in headless mode
            - Save the PDFs to an output folder with the same base names
            - Skip files whose PDF already exists and is newer
            - Log any files that fail to convert
Input:      Source folder path, output folder path
Tech stack: Bash, LibreOffice (soffice --headless --convert-to pdf)
```

---

## Example 4

**Intent:**
Every night at 2am I want my Documents folder copied to my NAS, but only the files that changed.

**Spec:**
```
Type:       Scheduled script (backup)
Features:   - Sync ~/Documents to a mounted NAS share using rsync incremental copy
            - Preserve timestamps and permissions
            - Keep deleted files in a dated backup directory instead of removing them
            - Write a log file for each run with transferred file count
            - Run every night at 02:00 via cron
Input:      Source folder, NAS mount path (set in a config file)
Tech stack: Bash, rsync, cron
```

---

## Example 5

**Intent:**
script that emails me when a website's price drops below what I want

**Spec:**
```
Type:       Scheduled script (price monitor)
Features:   - Load a list of product URLs with target prices from a YAML file
            - Fetch each product page and extract the price with a CSS selector
            - Compare the current price to the target price
            - Send an email alert with the product name, old price and new price when it drops below target
            - Record each check in a price history file
Input:      YAML config with URLs, CSS selectors and target prices
Tech stack: Python, requests, BeautifulSoup, smtplib, cron
```

---

## Example 6

**Intent:**
pdf merger

**Spec:**
```
Type:       Command-line tool (PDF utility)
Features:   - Merge several PDF files into one in the order given
            - Accept a glob pattern such as reports/*.pdf
            - Sort input files by name when a glob is used
            - Write the result to a file set with -o
Input:      List of PDF paths or a glob pattern, -o output path
Tech stack: Python, pypdf, argparse
```

---

## Example 7

**Intent:**
i have like 3000 mp3 files with garbage names, can it rename them using the song info inside

**Spec:**
```
Type:       Command-line script (audio renaming)
Features:   - Scan a folder recursively for .mp3 files
            - Read artist, title and track number from ID3 tags
            - Rename each file to "Artist - Title.mp3"
            - Remove characters that are not allowed in file names
            - Skip files with missing tags and list them at the end
            - Support --dry-run to preview the new names
Input:      Music folder path
Tech stack: Python, mutagen
```

---

## Example 8

**Intent:**
need something to resize all images in a folder to 1200px wide for my blog

**Spec:**
```
Type:       Command-line script (bulk image processing)
Features:   - Find .jpg, .jpeg, .png and .webp images in a folder
            - Resize each image to 1200 px wide, keeping the aspect ratio
            - Skip images that are already narrower than 1200 px
            - Save resized copies to an output folder with optional JPEG quality setting
            - Strip EXIF metadata from the output files
Input:      Input folder, output folder, --width and --quality flags
Tech stack: Python, Pillow
```

---

## Example 9

**Intent:**
powershell script to clean temp files older than 7 days on windows

**Spec:**
```
Type:       Command-line script (system maintenance)
Features:   - Delete files older than 7 days from %TEMP% and C:\Windows\Temp
            - Skip files that are locked or in use
            - Remove empty folders left behind
            - Report the number of files deleted and disk space freed
            - Support a -WhatIf switch to preview without deleting
Input:      Age threshold in days (default 7)
Tech stack: PowerShell, Windows Task Scheduler (optional weekly run)
```

---

## Example 10

**Intent:**
Can you make a tool that reads my web server access logs and tells me the top pages and which IPs hit me the most?

**Spec:**
```
Type:       Command-line tool (log analysis)
Features:   - Parse Nginx/Apache combined log format lines
            - Count requests per URL path and per client IP
            - Show the top N pages and top N IPs in a table
            - Count status codes (2xx, 3xx, 4xx, 5xx)
            - Filter by date range with --since and --until
            - Read gzip-compressed rotated logs directly
Input:      One or more log file paths, --top N, --since/--until dates
Tech stack: Python, argparse, gzip, collections.Counter
```

---

## Example 11

**Intent:**
excel files from each branch office, combine them into one sheet

**Spec:**
```
Type:       Command-line script (spreadsheet automation)
Features:   - Read every .xlsx file in a folder
            - Load the first sheet of each file and check that the column headers match
            - Add a "Branch" column taken from the file name
            - Append all rows into one combined sheet
            - Save the result as combined.xlsx with headers in bold
Input:      Folder of branch Excel files
Tech stack: Python, pandas, openpyxl
```

---

## Example 12

**Intent:**
back up my mysql database every day and keep only the last 14 backups

**Spec:**
```
Type:       Scheduled script (database backup)
Features:   - Dump the database with mysqldump using single-transaction mode
            - Compress the dump with gzip and name it with the date
            - Delete backups older than 14 days
            - Exit with a non-zero code and log an error if the dump fails
            - Run daily via cron
Input:      Database credentials from a ~/.my.cnf file, backup directory path
Tech stack: Bash, mysqldump, gzip, cron
```

---

## Example 13

**Intent:**
whenever someone emails me an invoice i want the attachment saved to a folder automatically

**Spec:**
```
Type:       Scheduled script (email automation)
Features:   - Connect to the mailbox over IMAP every 10 minutes
            - Search unread emails with PDF attachments and "invoice" in the subject
            - Save each attachment to a folder named by year and month
            - Mark processed emails as read and add a label
            - Skip attachments that were already saved (by file hash)
Input:      IMAP server, username and app password from environment variables
Tech stack: Python, imaplib, email, cron
```

---

## Example 14

**Intent:**
git helper that deletes local branches that are already merged

**Spec:**
```
Type:       Command-line tool (git helper)
Features:   - List local branches already merged into main
            - Exclude protected branches (main, master, develop, current branch)
            - Show the branches to be deleted and ask for confirmation
            - Delete confirmed branches with git branch -d
            - Optionally prune remote-tracking branches with --remote
Input:      Repository path (defaults to current directory), --yes flag to skip confirmation
Tech stack: Bash, git
```

---

## Example 15

**Intent:**
turn a csv into json

**Spec:**
```
Type:       Command-line tool (format conversion)
Features:   - Read a CSV file with a header row
            - Convert each row to a JSON object using the headers as keys
            - Detect numbers and booleans and output them with the right type
            - Write a JSON array to stdout or to a file with -o
            - Support a custom delimiter with -d
Input:      CSV file path or stdin
Tech stack: Node.js, csv-parse, commander
```

---

## Example 16

**Intent:**
hi i want convert my many .heic photos from iphone to jpg because windows not open them good

**Spec:**
```
Type:       Command-line script (image conversion)
Features:   - Find all .heic files in a folder and its subfolders
            - Convert each one to .jpg with adjustable quality
            - Keep the original date taken in the EXIF data
            - Save the JPG next to the original or in an output folder
            - Skip files that were already converted
Input:      Folder path, optional output folder
Tech stack: Python, pillow-heif, Pillow
```

---

## Example 17

**Intent:**
Write me a bash script that checks disk usage on my server and warns me in Slack when any partition goes over 85%.

**Spec:**
```
Type:       Scheduled script (disk monitoring)
Features:   - Read usage for every mounted partition with df
            - Compare each partition against an 85% threshold
            - Post a warning to a Slack incoming webhook with host name, mount point and usage
            - Avoid repeat alerts for the same partition within 6 hours
            - Run every 15 minutes via cron
Input:      Threshold percent and Slack webhook URL in a config file
Tech stack: Bash, df, curl, cron
```

---

## Example 18

**Intent:**
grab every picture off a gallery page and save it locally

**Spec:**
```
Type:       Command-line tool (web scraping)
Features:   - Fetch a web page and parse all img tags and srcset attributes
            - Resolve relative image URLs to absolute ones
            - Download each image to an output folder
            - Skip images smaller than a minimum size with --min-kb
            - Avoid downloading the same URL twice
Input:      Page URL, output folder, --min-kb
Tech stack: Python, requests, BeautifulSoup
```

---

## Example 19

**Intent:**
password generator in the terminal

**Spec:**
```
Type:       Command-line tool (password helper)
Features:   - Generate a random password of a chosen length
            - Toggle uppercase, digits and symbols with flags
            - Generate passphrases from a word list with --words N
            - Use a cryptographically secure random source
            - Copy the result to the clipboard with --copy
Input:      Flags: --length, --no-symbols, --words, --copy
Tech stack: Python, secrets module, pyperclip
```

---

## Example 20

**Intent:**
so my boss wants a weekly sales report every monday morning, right now i pull numbers from our postgres db by hand and paste them into excel, then email it. i'd love to automate the whole thing

**Spec:**
```
Type:       Scheduled script (report generation)
Features:   - Run SQL queries against PostgreSQL for last week's sales by product and by region
            - Build an Excel workbook with one sheet per summary and a totals row
            - Add a bar chart of sales by region
            - Email the workbook to a list of recipients with a short summary in the body
            - Run every Monday at 07:00 via cron
Input:      Database connection string, recipient list and SMTP settings in a .env file
Tech stack: Python, psycopg2, pandas, openpyxl, smtplib, cron
```

---

## Example 21

**Intent:**
monitor a folder and when a new file shows up, upload it to s3

**Spec:**
```
Type:       Command-line script (file sync)
Features:   - Watch a local folder for new or modified files
            - Upload each new file to an S3 bucket under the same relative path
            - Wait until the file has finished writing before uploading
            - Retry failed uploads with exponential backoff
            - Log each upload with time and size
Input:      Local folder path, S3 bucket name and prefix
Tech stack: Python, watchdog, boto3
```

---

## Example 22

**Intent:**
extract text from scanned pdfs so i can search them

**Spec:**
```
Type:       Command-line script (OCR)
Features:   - Find PDF files that have no text layer
            - Run OCR on every page
            - Write a new searchable PDF with an invisible text layer
            - Also save the extracted text as a .txt file
            - Process files in parallel using all CPU cores
Input:      Folder of scanned PDFs, --lang option (e.g. eng, deu)
Tech stack: Python, OCRmyPDF, Tesseract
```

---

## Example 23

**Intent:**
rename files to lowercase and replace spaces with underscores

**Spec:**
```
Type:       Command-line script (file renaming)
Features:   - Rename every file in a folder to lowercase
            - Replace spaces and repeated dashes with underscores
            - Apply the change recursively with -r
            - Detect name collisions and skip those files with a warning
            - Preview changes with --dry-run
Input:      Folder path
Tech stack: Bash, find, mv
```

---

## Example 24

**Intent:**
wat about a script that tells me when my website goes down

**Spec:**
```
Type:       Scheduled script (uptime monitor)
Features:   - Send an HTTP GET request to each URL in a list every 5 minutes
            - Treat timeouts and non-2xx responses as down
            - Send an email alert when a site goes down and again when it recovers
            - Measure and log response time for every check
            - Require two failed checks in a row before alerting
Input:      Text file with URLs, SMTP settings
Tech stack: Python, requests, smtplib, cron
```

---

## Example 25

**Intent:**
I take a lot of screen recordings in .mov format and they're huge. I'd like to shrink them all to mp4 without losing too much quality.

**Spec:**
```
Type:       Command-line script (video conversion)
Features:   - Find all .mov files in a folder
            - Re-encode each one to H.264 MP4 with a CRF quality setting
            - Keep the original resolution and audio
            - Show the size before and after for each file
            - Delete the original only when --delete-original is passed and the conversion succeeded
Input:      Folder path, --crf value (default 23)
Tech stack: Bash, ffmpeg
```

---

## Example 26

**Intent:**
Our team keeps forgetting to fill in the timesheet google sheet. Could a script check it on Friday afternoon and remind people who haven't?

**Spec:**
```
Type:       Scheduled script (spreadsheet reminder)
Features:   - Read the current week's rows from a Google Sheet
            - Find team members who have no hours entered for the week
            - Send each of them a reminder email with a link to the sheet
            - Post a summary of missing entries to the team lead
            - Run every Friday at 15:00 via cron
Input:      Spreadsheet ID, team member list with emails, service account key file
Tech stack: Python, gspread, Google Sheets API, smtplib, cron
```

---

## Example 27

**Intent:**
make a node cli that compresses png and jpg files in place

**Spec:**
```
Type:       Command-line tool (image optimization)
Features:   - Accept files, folders or glob patterns as arguments
            - Compress JPEGs with mozjpeg and PNGs with a lossy palette
            - Overwrite files only when the result is smaller
            - Print bytes saved per file and in total
            - Run several files in parallel
Input:      Paths or globs, --quality flag
Tech stack: Node.js, sharp, commander, fast-glob
```

---

## Example 28

**Intent:**
my csv is 4gb and excel chokes on it, chop it into pieces

**Spec:**
```
Type:       Command-line tool (CSV processing)
Features:   - Split a CSV into files of N rows each
            - Repeat the header row in every output file
            - Name parts with a numbered suffix (data_001.csv, data_002.csv)
            - Stream the input so very large files do not use much memory
Input:      CSV path, --rows N, output folder
Tech stack: Python, csv module
```

---

## Example 29

**Intent:**
need to archive old project folders: zip anything not touched for a year and move it to the archive drive

**Spec:**
```
Type:       Command-line script (archiving)
Features:   - List subfolders of a projects directory
            - Find folders where no file was modified in the last 365 days
            - Compress each one into a .zip named after the folder
            - Verify the zip archive before deleting the original folder
            - Move archives to the archive drive and log what was moved
Input:      Projects directory, archive drive path, --days threshold
Tech stack: Python, zipfile, shutil
```

---

## Example 30

**Intent:**
pls make me a thing where i paste a youtube playlist link and it downloads all the audio as mp3

**Spec:**
```
Type:       Command-line tool (media downloader)
Features:   - Accept a playlist URL as an argument
            - Download the audio of every video in the playlist
            - Convert audio to MP3 at 192 kbps
            - Name files with the playlist index and video title
            - Skip videos already downloaded using an archive file
Input:      Playlist URL, output folder
Tech stack: Python, yt-dlp, ffmpeg
```

---

## Example 31

**Intent:**
my obsidian vault has tons of urls, find the dead ones

**Spec:**
```
Type:       Command-line tool (link checker)
Features:   - Scan .md files in a folder recursively
            - Extract HTTP and HTTPS links from markdown link syntax and bare URLs
            - Send HEAD requests concurrently, falling back to GET when HEAD is not allowed
            - Report broken links with file name, line number and status code
            - Exit with a non-zero code when broken links are found
Input:      Notes folder path, --timeout seconds
Tech stack: Go, net/http, goroutines
```

---

## Example 32

**Intent:**
a cron job that pulls stock prices for my watchlist every hour during market hours and logs them

**Spec:**
```
Type:       Scheduled script (stock monitor)
Features:   - Read ticker symbols from a watchlist file
            - Fetch the latest price for each ticker from a market data API
            - Run only on weekdays between 9:30 and 16:00 exchange time
            - Append prices with timestamps to a CSV file per ticker
            - Print an alert line when a price moves more than 3% since the open
Input:      Watchlist file, API key in an environment variable
Tech stack: Python, yfinance, cron
```

---

## Example 33

**Intent:**
preview images for my video library so i can see what each clip is

**Spec:**
```
Type:       Command-line script (media processing)
Features:   - Find video files (.mp4, .mkv, .mov) in a folder
            - Grab a frame at 10% of each video's duration
            - Save it as a 320 px wide JPEG thumbnail
            - Create a contact sheet of 9 frames per video with --sheet
            - Skip videos that already have a thumbnail
Input:      Video folder path, output folder
Tech stack: Bash, ffmpeg, ffprobe
```

---

## Example 34

**Intent:**
Our server logs get too big. I want a script that compresses logs older than a day and deletes ones older than a month.

**Spec:**
```
Type:       Scheduled script (log rotation)
Features:   - Find .log files in a set of log directories
            - Compress files older than 1 day with gzip
            - Delete compressed logs older than 30 days
            - Skip files currently open by a process
            - Write a one-line summary per run to syslog
Input:      List of log directories in a config file
Tech stack: Bash, find, gzip, lsof, logger, cron
```

---

## Example 35

**Intent:**
find and replace text across hundreds of files

**Spec:**
```
Type:       Command-line tool (text processing)
Features:   - Search files matching a glob pattern for a string or regular expression
            - Replace matches with new text
            - Show a colored diff of changes before applying
            - Create .bak backups unless --no-backup is set
            - Report how many replacements were made in each file
Input:      Pattern, replacement, file glob, --regex flag
Tech stack: Rust, regex, globset, clap
```

---

## Example 36

**Intent:**
python script to fill out a word template with data from an excel sheet, one document per row

**Spec:**
```
Type:       Command-line script (document generation)
Features:   - Read rows from an Excel sheet
            - Fill placeholders like {{name}} in a .docx template with values from each row
            - Save one document per row named after a chosen column
            - Optionally convert each document to PDF with --pdf
            - Report rows with missing values
Input:      Excel file, .docx template, output folder
Tech stack: Python, openpyxl, docxtpl, docx2pdf
```

---

## Example 37

**Intent:**
make a script that checks which of my npm dependencies are outdated across all my projects

**Spec:**
```
Type:       Command-line tool (developer helper)
Features:   - Find every package.json under a root folder, skipping node_modules
            - Run npm outdated for each project and parse the JSON output
            - Show a table of package, current, wanted and latest versions per project
            - Highlight major version updates
            - Export the results as Markdown with --md
Input:      Root folder of projects
Tech stack: Node.js, child_process, cli-table3
```

---

## Example 38

**Intent:**
weekly cleanup of docker stuff on my server

**Spec:**
```
Type:       Scheduled script (system maintenance)
Features:   - Remove stopped containers older than 24 hours
            - Remove dangling images and unused networks
            - Prune build cache older than 7 days
            - Log disk space before and after cleanup
            - Run every Sunday at 03:00 via cron
Tech stack: Bash, Docker CLI, cron
```

---

## Example 39

**Intent:**
watermark my photos with my name in the corner

**Spec:**
```
Type:       Command-line script (bulk image processing)
Features:   - Add a text or PNG logo watermark to each image in a folder
            - Place it in a chosen corner with a margin
            - Scale the watermark relative to image width
            - Set watermark opacity with --opacity
            - Save the results to an output folder without touching the originals
Input:      Image folder, watermark text or logo file, --position, --opacity
Tech stack: Python, Pillow
```

---

## Example 40

**Intent:**
i want to send personalised emails to like 200 people from a spreadsheet, with their name in it

**Spec:**
```
Type:       Command-line script (email automation)
Features:   - Read recipients and their fields from a CSV or Excel file
            - Fill a subject and body template with each recipient's fields
            - Send emails through SMTP with a delay between messages to avoid rate limits
            - Log sent and failed addresses to a results file
            - Preview the first email with --test without sending
Input:      Recipient spreadsheet, email template file, SMTP settings in .env
Tech stack: Python, pandas, Jinja2, smtplib
```

---

## Example 41

**Intent:**
zip each folder separately

**Spec:**
```
Type:       Command-line script (archiving)
Features:   - Create one .zip archive per subfolder in a directory
            - Name each archive after its folder
            - Skip folders that already have an up-to-date archive
            - Optionally set a password with --password using AES encryption
Input:      Parent directory path
Tech stack: Python, pyzipper
```

---

## Example 42

**Intent:**
tool that tells me what's taking up space on my disk

**Spec:**
```
Type:       Command-line tool (disk usage)
Features:   - Scan a directory tree and total the size of each folder
            - Show the largest folders and files as a sorted list
            - Display sizes in human-readable units
            - Limit depth with --depth and results with --top
            - Skip other mounted file systems
Input:      Starting path, --depth, --top
Tech stack: Go, filepath.WalkDir
```

---

## Example 43

**Intent:**
auto commit and push my notes repo every hour

**Spec:**
```
Type:       Scheduled script (git sync)
Features:   - Check the notes repository for changes with git status
            - Stage all changes and commit with a timestamped message
            - Pull with rebase before pushing to avoid conflicts
            - Push to the remote and log the result
            - Skip the commit when there are no changes
Input:      Path to the notes repository
Tech stack: Bash, git, cron
```

---

## Example 44

**Intent:**
my students submit assignments as pdf with random names, i want to rename them by student id which is on the first page

**Spec:**
```
Type:       Command-line script (PDF renaming)
Features:   - Read the text of the first page of each PDF in a folder
            - Find the student ID with a regular expression (e.g. 8 digits)
            - Rename the file to <studentID>.pdf
            - Move files where no ID was found to a "check" folder
            - Write a CSV mapping old names to new names
Input:      Folder of PDFs, ID regex pattern
Tech stack: Python, pdfplumber, re
```

---

## Example 45

**Intent:**
make a script to convert excel sheets to csv, every sheet as separate file

**Spec:**
```
Type:       Command-line tool (format conversion)
Features:   - Open an .xlsx or .xls workbook
            - Export every sheet to its own CSV file named workbook_sheetname.csv
            - Keep dates in ISO format
            - Choose the output encoding with --encoding (default UTF-8)
            - Process a whole folder of workbooks at once
Input:      Workbook path or folder
Tech stack: Python, pandas, openpyxl, xlrd
```

---

## Example 46

**Intent:**
scrape job listings from a site every morning and email me the new ones

**Spec:**
```
Type:       Scheduled script (web scraping)
Features:   - Fetch job search result pages for saved keywords
            - Extract title, company, location and link for each listing
            - Compare listings against ones seen before and keep only new ones
            - Email a daily digest of new listings
            - Run every morning at 08:00 via cron
Input:      Keywords and search URL in a config file
Tech stack: Python, requests, BeautifulSoup, sqlite3, cron
```

---

## Example 47

**Intent:**
cli to count words in all my text files

**Spec:**
```
Type:       Command-line tool (text processing)
Features:   - Count words, lines and characters in each .txt and .md file
            - Show a total across all files
            - Sort output by word count
            - Read file names from a glob pattern
Input:      File paths or glob pattern
Tech stack: Python, argparse, glob
```

---

## Example 48

**Intent:**
Hello, in my company we receive many CSV with different separators and encodings, I need a tool for make them all the same format (UTF-8, comma).

**Spec:**
```
Type:       Command-line tool (CSV normalization)
Features:   - Detect the encoding of each CSV file
            - Detect the delimiter (comma, semicolon, tab, pipe)
            - Rewrite the file as UTF-8 with comma delimiters and quoted fields
            - Write normalized files to an output folder
            - Report the detected encoding and delimiter for each file
Input:      Input folder, output folder
Tech stack: Python, charset-normalizer, csv.Sniffer
```

---

## Example 49

**Intent:**
backup my phone photos from the folder that syncs to my pc into dated folders and remove duplicates

**Spec:**
```
Type:       Command-line script (photo backup)
Features:   - Copy new photos and videos from the sync folder to a backup folder
            - Sort them into YYYY/MM subfolders using EXIF date or file date
            - Skip files whose hash already exists in the backup
            - Keep a hash index so later runs are fast
            - Print how many files were copied and skipped
Input:      Sync folder path, backup root path
Tech stack: Python, Pillow, hashlib
```

---

## Example 50

**Intent:**
rotate all pages of a pdf

**Spec:**
```
Type:       Command-line tool (PDF utility)
Features:   - Rotate all pages of a PDF by 90, 180 or 270 degrees
            - Rotate only selected pages with --pages 1,3,5-8
            - Write the result to a new file instead of overwriting
            - Keep bookmarks and metadata
Input:      PDF path, --angle, --pages, -o output path
Tech stack: Python, pypdf, argparse
```

---

## Example 51

**Intent:**
extract all email addresses from a bunch of text files into one list

**Spec:**
```
Type:       Command-line tool (text extraction)
Features:   - Scan text, CSV and HTML files in a folder
            - Find email addresses with a regular expression
            - Lowercase and deduplicate the results
            - Write a sorted list to a text file
            - Show which file each address was found in with --with-source
Input:      Folder path or file glob
Tech stack: Python, re, pathlib
```

---

## Example 52

**Intent:**
I run a small online shop and every morning I download the orders CSV, then make packing slips by hand. Can a script turn that CSV into printable packing slips, one page per order?

**Spec:**
```
Type:       Command-line script (document generation)
Features:   - Read the orders CSV and group line items by order number
            - Render a packing slip per order with shop logo, customer address and item list
            - Combine all slips into one PDF with one page per order
            - Sort orders by shipping method
            - Name the output file with today's date
Input:      Orders CSV export, logo image, shop details in a config file
Tech stack: Python, pandas, Jinja2, WeasyPrint
```

---

## Example 53

**Intent:**
bash script to check ssl certificate expiry dates for a list of domains

**Spec:**
```
Type:       Scheduled script (certificate monitor)
Features:   - Read domain names from a text file
            - Connect to each domain on port 443 and read the certificate end date
            - Calculate days left until expiry
            - Print a table sorted by days left
            - Send an email when any certificate expires within 14 days
Input:      Domains file, warning threshold in days
Tech stack: Bash, openssl s_client, date, mail, cron
```

---

## Example 54

**Intent:**
convert markdown files to nice looking html pages

**Spec:**
```
Type:       Command-line tool (format conversion)
Features:   - Convert one .md file or a folder of .md files to HTML
            - Apply a CSS theme chosen with --theme
            - Add syntax highlighting for code blocks
            - Generate a table of contents from headings
            - Keep the folder structure in the output directory
Input:      Markdown file or folder, output folder
Tech stack: Python, markdown, Pygments, Jinja2
```

---

## Example 55

**Intent:**
script to check if my favourite sneakers are back in stock

**Spec:**
```
Type:       Scheduled script (stock monitor)
Features:   - Load product page URLs and the sizes to watch
            - Fetch each page every 30 minutes and check the size availability
            - Send a push notification through ntfy when a watched size is in stock
            - Send each in-stock alert only once until stock changes again
            - Use a random delay and a normal browser user agent between requests
Input:      Config file with URLs and sizes
Tech stack: Python, requests, BeautifulSoup, ntfy.sh, cron
```

---

## Example 56

**Intent:**
merge 2 csv files on a common column

**Spec:**
```
Type:       Command-line tool (CSV processing)
Features:   - Join two CSV files on a key column given with --on
            - Support inner, left and outer joins with --how
            - Rename clashing column names with suffixes
            - Write the merged result to a new CSV
            - Report rows that had no match
Input:      Two CSV file paths, --on column name, --how join type
Tech stack: Python, pandas, click
```

---

## Example 57

**Intent:**
on mac i want to automatically move screenshots off my desktop into a folder by month

**Spec:**
```
Type:       Scheduled script (file organizer)
Features:   - Find files on the Desktop whose names start with "Screenshot"
            - Move them into ~/Pictures/Screenshots/YYYY-MM based on creation date
            - Run every hour with a launchd agent
            - Avoid overwriting by adding a counter on name clashes
Input:      Desktop path and target folder (configurable at the top of the script)
Tech stack: Bash, macOS launchd, stat
```

---

## Example 58

**Intent:**
make a tool that tells me which files changed between two folders

**Spec:**
```
Type:       Command-line tool (folder comparison)
Features:   - Compare two directory trees recursively
            - List files that exist only on the left, only on the right, or differ
            - Compare by size and modification time, or by hash with --deep
            - Ignore paths matching patterns from --exclude
            - Output as text or JSON
Input:      Two folder paths, --deep, --exclude patterns
Tech stack: Python, filecmp, hashlib, argparse
```

---

## Example 59

**Intent:**
convert wav to mp3

**Spec:**
```
Type:       Command-line script (audio conversion)
Features:   - Convert every .wav file in a folder to .mp3
            - Set the bitrate with --bitrate (default 192k)
            - Copy tags when the WAV has metadata
            - Write output files next to the originals or to an output folder
Input:      Folder path, --bitrate
Tech stack: Bash, ffmpeg
```

---

## Example 60

**Intent:**
Every month I get bank statements as CSV from two banks with different formats, and I want a script that puts them together and sorts my spending into categories like groceries, rent, transport.

**Spec:**
```
Type:       Data analysis script (personal finance)
Features:   - Read statement CSVs from both banks and map their columns to date, description and amount
            - Assign a category to each transaction using keyword rules from a YAML file
            - Mark transactions with no matching rule as "Uncategorized"
            - Summarize total spending per category for the month
            - Export the combined transactions and summary to Excel
Input:      Folder of bank CSV files, category rules file
Tech stack: Python, pandas, PyYAML, openpyxl
```

---

## Example 61

**Intent:**
i need a script that pings all devices on my network and lists which are online

**Spec:**
```
Type:       Command-line tool (network scan)
Features:   - Scan a subnet range such as 192.168.1.0/24
            - Ping hosts concurrently with a short timeout
            - Look up each live host's hostname and MAC address
            - Print a table of IP, hostname and MAC
            - Save results to CSV with --csv
Input:      Subnet in CIDR notation
Tech stack: Python, ipaddress, concurrent.futures, scapy
```

---

## Example 62

**Intent:**
something to strip location data from my photos before i post them

**Spec:**
```
Type:       Command-line script (privacy cleanup)
Features:   - Find JPEG and HEIC images in a folder
            - Remove GPS tags from EXIF metadata
            - Keep other metadata such as date taken unless --all is set
            - Modify files in place or write cleaned copies to an output folder
            - Report which files contained location data
Input:      Folder of photos, --all, --output
Tech stack: ExifTool, Bash
```

---

## Example 63

**Intent:**
clean up old git branches on the remote that nobody touched for months

**Spec:**
```
Type:       Command-line tool (git helper)
Features:   - Fetch and list remote branches with their last commit date and author
            - Select branches with no commits for more than N days
            - Exclude protected branches by pattern
            - Print the list and delete them from origin after confirmation
            - Save the list of deleted branches with their last commit SHA for recovery
Input:      --days threshold, --protect patterns, --yes
Tech stack: Python, GitPython
```

---

## Example 64

**Intent:**
i wanna scrape the weather every day and keep a log in a csv

**Spec:**
```
Type:       Scheduled script (data collection)
Features:   - Call a weather API for a configured city once a day
            - Record date, min and max temperature, rain and wind speed
            - Append one row per day to a CSV file
            - Skip appending when today's row already exists
            - Run daily at 23:00 via cron
Input:      City name and API key in a .env file
Tech stack: Python, requests, OpenWeatherMap API, cron
```

---

## Example 65

**Intent:**
Make a CLI that encrypts a file with a password, and decrypts it again.

**Spec:**
```
Type:       Command-line tool (file encryption)
Features:   - Encrypt a file with a password using AES-256-GCM
            - Derive the key from the password with scrypt and a random salt
            - Decrypt the file back and detect wrong passwords or tampering
            - Prompt for the password without echoing it
            - Delete the original securely with --shred after encryption
Input:      encrypt or decrypt subcommand, file path
Tech stack: Python, cryptography, getpass
```

---

## Example 66

**Intent:**
batch crop photos to square for instagram

**Spec:**
```
Type:       Command-line script (bulk image processing)
Features:   - Crop each image to a centered 1:1 square
            - Resize the result to 1080x1080 px
            - Optionally pad with a white or blurred background instead of cropping with --pad
            - Save as high-quality JPEG in an output folder
Input:      Input folder, output folder, --pad
Tech stack: Python, Pillow
```

---

## Example 67

**Intent:**
python script that converts my old .xls files to .xlsx

**Spec:**
```
Type:       Command-line script (format conversion)
Features:   - Find all .xls files in a folder recursively
            - Open each one and save it as .xlsx, keeping all sheets
            - Keep cell values, number formats and column widths where possible
            - Write converted files next to the originals
            - List files that failed to open
Input:      Folder path
Tech stack: Python, xlrd, openpyxl
```

---

## Example 68

**Intent:**
get notified when a new version of some software i use is released on github

**Spec:**
```
Type:       Scheduled script (release monitor)
Features:   - Read a list of GitHub repositories from a file
            - Fetch the latest release of each repository through the GitHub API
            - Compare with the last seen release tag
            - Send a Telegram message with the release name and changelog link when a new release appears
            - Run every 6 hours via cron
Input:      Repositories file, GitHub token and Telegram bot token in environment variables
Tech stack: Python, requests, GitHub REST API, Telegram Bot API, cron
```

---

## Example 69

**Intent:**
tool for finding large files over 1gb on my drive

**Spec:**
```
Type:       Command-line tool (disk cleanup)
Features:   - Search a path recursively for files above a size threshold
            - Show results sorted by size with last access date
            - Filter by extension with --ext
            - Export the list to CSV
Input:      Path, --min-size (default 1G), --ext
Tech stack: Bash, find, sort, du
```

---

## Example 70

**Intent:**
windows batch file to back up my outlook pst file to onedrive every friday

**Spec:**
```
Type:       Scheduled script (backup)
Features:   - Close Outlook if it is running so the PST file is not locked
            - Copy the PST file to a OneDrive folder with the date in the name
            - Keep the 4 most recent copies and delete older ones
            - Log success or failure to a text file
            - Run every Friday at 18:00 with Task Scheduler
Input:      PST file path and OneDrive folder path set at the top of the script
Tech stack: Windows batch (cmd), robocopy, taskkill, Windows Task Scheduler
```

---

## Example 71

**Intent:**
extract all tables from pdf reports into excel

**Spec:**
```
Type:       Command-line script (data extraction)
Features:   - Detect tables on every page of a PDF
            - Extract each table into a DataFrame
            - Write each table to its own sheet in an Excel file
            - Name sheets by page number and table index
            - Process a whole folder of PDFs
Input:      PDF file or folder, output folder
Tech stack: Python, pdfplumber, pandas, openpyxl
```

---

## Example 72

**Intent:**
count how many lines of code are in my project by language

**Spec:**
```
Type:       Command-line tool (developer helper)
Features:   - Walk a project folder and skip folders in .gitignore
            - Detect the language of each file by extension
            - Count code, comment and blank lines
            - Print a table per language with totals
            - Output JSON with --json
Input:      Project folder path
Tech stack: Go, go-gitignore
```

---

## Example 73

**Intent:**
i want my raspberry pi to reboot itself if the wifi drops

**Spec:**
```
Type:       Scheduled script (network watchdog)
Features:   - Ping the router and a public DNS server every 5 minutes
            - Restart the wifi interface after two failed checks
            - Reboot the Pi if the connection is still down after restarting the interface
            - Log every failure and action to a file
            - Run via cron as root
Input:      Router IP and interface name (wlan0) set in the script
Tech stack: Bash, ping, ip link, cron
```

---

## Example 74

**Intent:**
renumber files in a folder like 001, 002, 003

**Spec:**
```
Type:       Command-line script (file renaming)
Features:   - Sort files in a folder by name, date or size
            - Rename them with a zero-padded counter and optional prefix
            - Keep the original file extension
            - Rename in two steps through temporary names to avoid collisions
            - Show a preview with --dry-run
Input:      Folder path, --prefix, --sort, --start
Tech stack: Python, pathlib
```

---

## Example 75

**Intent:**
Can I have a little script that each morning sends me an email with my calendar for the day and the weather?

**Spec:**
```
Type:       Scheduled script (daily digest)
Features:   - Read today's events from a Google Calendar
            - Fetch today's weather forecast for my city
            - Build an HTML email with the events in time order and the forecast
            - Send it every morning at 07:00
            - Skip sending on days with no events when --skip-empty is set
Input:      Calendar ID, city, API keys and SMTP settings in .env
Tech stack: Python, Google Calendar API, requests, smtplib, cron
```

---

## Example 76

**Intent:**
check passwords against have i been pwned

**Spec:**
```
Type:       Command-line tool (password helper)
Features:   - Read passwords from a prompt or a file
            - Hash each password with SHA-1
            - Query the Pwned Passwords range API with only the first 5 hash characters (k-anonymity)
            - Report how many times each password appeared in breaches
            - Never print or log the full password
Input:      Interactive prompt or file of passwords
Tech stack: Python, hashlib, requests, getpass
```

---

## Example 77

**Intent:**
sort my ebook collection into folders by author

**Spec:**
```
Type:       Command-line script (file organizer)
Features:   - Read author and title metadata from EPUB and PDF files
            - Move each book to Author/Title.ext
            - Fall back to parsing "Author - Title" from the file name
            - Collect books with no author into an "Unknown" folder
            - Write a log of all moves for undo
Input:      Ebook folder path
Tech stack: Python, ebooklib, pypdf
```

---

## Example 78

**Intent:**
get the subtitles out of mkv files

**Spec:**
```
Type:       Command-line script (media processing)
Features:   - List subtitle tracks in each .mkv file in a folder
            - Extract the selected language track to .srt with --lang
            - Name output files after the video and language code
            - Skip files with no matching subtitle track
Input:      Folder of MKV files, --lang code
Tech stack: Bash, mkvtoolnix (mkvmerge, mkvextract)
```

---

## Example 79

**Intent:**
so i have a minecraft server running on linux and i'd like to back up the world every 6 hours, but the server must save first or the files get corrupted, and keep a week of backups

**Spec:**
```
Type:       Scheduled script (game server backup)
Features:   - Send save-off and save-all commands to the server through RCON
            - Wait for the save to finish, then archive the world folder as tar.gz
            - Send save-on to resume saving
            - Delete backups older than 7 days
            - Run every 6 hours via cron
Input:      Server path, RCON host, port and password in a config file
Tech stack: Bash, mcrcon, tar, cron
```

---

## Example 80

**Intent:**
crawl my own website and list every page and its title

**Spec:**
```
Type:       Command-line tool (site crawler)
Features:   - Start from a URL and follow internal links only
            - Respect robots.txt and a max depth setting
            - Record each page's URL, title, status code and meta description
            - Export the results to CSV
            - Limit concurrency to avoid overloading the server
Input:      Start URL, --depth, --concurrency
Tech stack: Python, Scrapy
```

---

## Example 81

**Intent:**
script to make a gif from a video clip

**Spec:**
```
Type:       Command-line tool (media conversion)
Features:   - Cut a section of a video from --start to --end
            - Scale it to a given width and frame rate
            - Generate an optimized color palette for better GIF quality
            - Write the GIF to the output path
Input:      Video path, --start, --end, --width, --fps
Tech stack: Bash, ffmpeg (palettegen and paletteuse)
```

---

## Example 82

**Intent:**
tool that removes blank pages from scanned pdf

**Spec:**
```
Type:       Command-line tool (PDF utility)
Features:   - Render each page of a PDF to a small image
            - Measure the share of non-white pixels on each page
            - Remove pages below a blankness threshold
            - Save the cleaned PDF and list removed page numbers
Input:      PDF path, --threshold
Tech stack: Python, PyMuPDF, NumPy
```

---

## Example 83

**Intent:**
when my laptop battery is low make a sound and popup on linux

**Spec:**
```
Type:       Scheduled script (system notification)
Features:   - Read battery level and charging state from /sys/class/power_supply
            - Show a desktop notification when level falls below 15% while discharging
            - Play a warning sound
            - Repeat at most every 5 minutes until the charger is connected
            - Run every minute with a systemd user timer
Tech stack: Bash, notify-send, paplay, systemd timer
```

---

## Example 84

**Intent:**
I'd like a script that reads a list of URLs and saves each page as a PDF, for archiving articles I want to read later.

**Spec:**
```
Type:       Command-line tool (web archiving)
Features:   - Read URLs from a text file, one per line
            - Open each page in a headless browser and wait for it to load
            - Save the page as an A4 PDF named after the page title
            - Skip URLs already saved
            - Report URLs that failed to load
Input:      URL list file, output folder
Tech stack: Node.js, Puppeteer
```

---

## Example 85

**Intent:**
list all installed programs on windows to a file

**Spec:**
```
Type:       Command-line script (system inventory)
Features:   - Read installed programs from the 64-bit and 32-bit Uninstall registry keys
            - Collect name, version, publisher and install date
            - Remove duplicates and sort by name
            - Export the list to CSV
Input:      Output CSV path
Tech stack: PowerShell, Get-ItemProperty, Export-Csv
```

---

## Example 86

**Intent:**
compare two excel files and highlight what changed

**Spec:**
```
Type:       Command-line tool (spreadsheet diff)
Features:   - Load the same sheet from two Excel files
            - Match rows by a key column given with --key
            - Find added, removed and changed rows
            - Write a report workbook with changed cells highlighted in yellow
            - Print a short summary of the number of changes
Input:      Old file, new file, --key column, --sheet name
Tech stack: Python, pandas, openpyxl
```

---

## Example 87

**Intent:**
telegram bot that sends me server load every morning

**Spec:**
```
Type:       Scheduled script (server report)
Features:   - Collect CPU load, memory use, disk use and uptime
            - Format a short status message
            - Send it to a Telegram chat through the Bot API
            - Run every morning at 08:00 via cron
Input:      Bot token and chat ID in environment variables
Tech stack: Python, psutil, requests, Telegram Bot API, cron
```

---

## Example 88

**Intent:**
gen a changelog from my git commits

**Spec:**
```
Type:       Command-line tool (git helper)
Features:   - Read commits between two tags or since the last tag
            - Group commits by Conventional Commit type (feat, fix, docs, chore)
            - Link each entry to its commit hash
            - Prepend a new version section to CHANGELOG.md
            - Print to stdout with --dry-run
Input:      Repository path, --from and --to tags
Tech stack: Node.js, simple-git
```

---

## Example 89

**Intent:**
transcribe audio recordings of my meetings to text

**Spec:**
```
Type:       Command-line tool (speech-to-text)
Features:   - Accept audio files in MP3, M4A or WAV
            - Convert audio to 16 kHz mono with ffmpeg
            - Transcribe speech locally with a Whisper model
            - Write the transcript with timestamps as .txt and .srt
            - Choose model size with --model
Input:      Audio file or folder, --model, --language
Tech stack: Python, openai-whisper, ffmpeg
```

---

## Example 90

**Intent:**
dedupe lines in a text file but keep the order

**Spec:**
```
Type:       Command-line tool (text processing)
Features:   - Remove repeated lines while keeping the first occurrence
            - Ignore case with -i and surrounding whitespace with -w
            - Read from a file or stdin
            - Write to stdout or overwrite in place with --in-place
Input:      File path or stdin
Tech stack: Python, argparse
```

---

## Example 91

**Intent:**
Backup my home folder to an external usb drive with snapshots I can go back to

**Spec:**
```
Type:       Command-line script (backup)
Features:   - Detect that the external drive is mounted before starting
            - Create a dated snapshot folder using rsync with --link-dest so unchanged files are hard links
            - Exclude caches and folders from an exclude file
            - Keep daily snapshots for 30 days and monthly ones for a year
            - Print the snapshot size and duration
Input:      Source folder, drive mount point, exclude file
Tech stack: Bash, rsync
```

---

## Example 92

**Intent:**
make all my photos black and white

**Spec:**
```
Type:       Command-line script (bulk image processing)
Features:   - Convert every image in a folder to grayscale
            - Optionally boost contrast with --contrast
            - Keep the original format and quality
            - Save results with a _bw suffix
Input:      Folder path
Tech stack: Python, Pillow
```

---

## Example 93

**Intent:**
plz help i need to join like 50 mp4 clips from my gopro into one video in order

**Spec:**
```
Type:       Command-line script (video joining)
Features:   - Find .mp4 files in a folder and sort them by file name or recording time
            - Write an ffmpeg concat list file
            - Join the clips without re-encoding when codecs match
            - Fall back to re-encoding when clips have different settings
            - Save the joined video to the output path
Input:      Folder of clips, output file path
Tech stack: Bash, ffmpeg (concat demuxer)
```

---

## Example 94

**Intent:**
I am teacher, I have exam results in excel, I want automatically make a chart and average for each class and send to the other teachers.

**Spec:**
```
Type:       Command-line script (report generation)
Features:   - Read exam results from an Excel file with class, student and score columns
            - Calculate average, highest and lowest score per class
            - Draw a bar chart of class averages
            - Save a PDF report with the table and chart
            - Email the PDF to a list of teachers
Input:      Excel file, teacher email list, SMTP settings
Tech stack: Python, pandas, matplotlib, ReportLab, smtplib
```

---

## Example 95

**Intent:**
convert images to webp

**Spec:**
```
Type:       Command-line tool (image conversion)
Features:   - Convert JPEG and PNG files to WebP
            - Set quality with -q and lossless mode with --lossless
            - Keep transparency from PNG files
            - Process folders recursively and keep the structure
            - Show total size saved
Input:      Files or folders, -q, --lossless
Tech stack: Bash, cwebp (libwebp)
```

---

## Example 96

**Intent:**
wanna kill any process thats using more than 90% cpu for too long on my linux box

**Spec:**
```
Type:       Scheduled script (process watchdog)
Features:   - Sample CPU usage of all processes every minute
            - Track processes above 90% CPU across consecutive samples
            - Send SIGTERM to a process that stays above the limit for 10 minutes, then SIGKILL if it does not exit
            - Skip processes on a whitelist (e.g. sshd, systemd)
            - Log every kill with process name, PID and user
Input:      Config file with threshold, duration and whitelist
Tech stack: Python, psutil, systemd service
```

---

## Example 97

**Intent:**
Could you help me write a script that renames my scanned receipts using the date and shop name? I scan them with my phone and they all come out as scan_0001.pdf and so on.

**Spec:**
```
Type:       Command-line script (receipt renaming)
Features:   - Run OCR on each scanned receipt PDF or image
            - Find the purchase date with date regex patterns
            - Guess the shop name from the first lines of text
            - Rename the file to YYYY-MM-DD_Shop.pdf
            - Move files that could not be parsed to a "manual" folder
Input:      Folder of scans
Tech stack: Python, pytesseract, pdf2image, dateparser
```

---

## Example 98

**Intent:**
python script to pull my github repos list and clone all of them

**Spec:**
```
Type:       Command-line tool (git helper)
Features:   - Fetch all repositories of a user or organization through the GitHub API with pagination
            - Clone repositories that are not yet present locally
            - Run git pull on repositories that already exist
            - Include private repositories when a token is provided
            - Skip forks and archived repositories with flags
Input:      Username or org name, target folder, GitHub token in environment variable
Tech stack: Python, PyGithub, subprocess, git
```

---

## Example 99

**Intent:**
shrink pdf size

**Spec:**
```
Type:       Command-line tool (PDF compression)
Features:   - Compress a PDF by downsampling images
            - Choose a preset with --quality screen, ebook or printer
            - Keep the original when the result is not smaller
            - Print the size before and after
Input:      PDF path, --quality, -o output
Tech stack: Bash, Ghostscript
```

---

## Example 100

**Intent:**
script to check my servers are patched, list pending updates on each one over ssh

**Spec:**
```
Type:       Command-line tool (server maintenance)
Features:   - Read a host list from an inventory file
            - Connect to each host over SSH with key authentication
            - Run the package manager in check mode (apt or dnf) and count pending updates
            - Flag hosts with pending security updates or a required reboot
            - Print a summary table and save it as CSV
Input:      Inventory file with hosts and SSH user
Tech stack: Python, Paramiko, concurrent.futures
```

---

## Example 101

**Intent:**
sync a folder between my laptop and desktop both ways

**Spec:**
```
Type:       Command-line tool (two-way sync)
Features:   - Compare two folders by modification time and size
            - Copy new and changed files in both directions
            - Detect conflicts when a file changed on both sides and keep both copies
            - Propagate deletions using the state from the last sync
            - Preview actions with --dry-run
Input:      Local folder path, remote folder over SSH
Tech stack: Unison, Bash wrapper script
```

---

## Example 102

**Intent:**
scrape amazon wishlist prices daily and save to google sheet

**Spec:**
```
Type:       Scheduled script (price tracking)
Features:   - Load the public wishlist page and read every item's name and price
            - Handle pagination of long wishlists
            - Append today's prices to a Google Sheet with the date
            - Mark items whose price dropped since yesterday
            - Run daily via cron
Input:      Wishlist URL, Google service account key, sheet ID
Tech stack: Python, Playwright, gspread, cron
```

---

## Example 103

**Intent:**
Need a tool to quickly base64 encode and decode files from the terminal

**Spec:**
```
Type:       Command-line tool (encoding utility)
Features:   - Encode a file or stdin to Base64
            - Decode Base64 back to binary
            - Support URL-safe Base64 with --url
            - Wrap output lines at a set width or not at all
Input:      encode or decode subcommand, file path or stdin
Tech stack: Go, encoding/base64, cobra
```

---

## Example 104

**Intent:**
a script that goes through my email and unsubscribes from newsletters

**Spec:**
```
Type:       Command-line script (email cleanup)
Features:   - Scan the inbox over IMAP for emails with a List-Unsubscribe header
            - Group them by sender and show a count per sender
            - Let the user pick senders to unsubscribe from
            - Call the one-click unsubscribe URL or send the mailto request
            - Move all past emails from those senders to a folder
Input:      IMAP account details in .env
Tech stack: Python, imapclient, requests, questionary
```

---

## Example 105

**Intent:**
optimise all images in my wordpress uploads folder on the server, its getting huge

**Spec:**
```
Type:       Command-line script (image optimization)
Features:   - Scan wp-content/uploads recursively for JPEG and PNG files
            - Losslessly optimize JPEGs and strip metadata
            - Optimize PNGs with zopfli-level compression
            - Skip files processed before using a list of processed paths
            - Report total disk space saved
Input:      Uploads folder path
Tech stack: Bash, jpegoptim, optipng, find
```

---

## Example 106

**Intent:**
auto-generate a README table of contents

**Spec:**
```
Type:       Command-line tool (markdown helper)
Features:   - Parse headings from a Markdown file
            - Build a nested list of links using GitHub-style anchors
            - Insert or replace the TOC between marker comments
            - Limit heading depth with --max-level
Input:      Markdown file path
Tech stack: Node.js, remark
```

---

## Example 107

**Intent:**
hey i have alot of voice memos from my iphone (m4a) can u make them all mp3 and put the date in the name

**Spec:**
```
Type:       Command-line script (audio conversion)
Features:   - Find all .m4a files in a folder
            - Read the recording date from the file metadata or file date
            - Convert each one to MP3
            - Name the output YYYY-MM-DD_HHMM_originalname.mp3
            - Skip files already converted
Input:      Folder of voice memos
Tech stack: Python, ffmpeg-python, mutagen
```

---

## Example 108

**Intent:**
sql query results to excel every morning for the finance team

**Spec:**
```
Type:       Scheduled script (report export)
Features:   - Run a set of SQL files against SQL Server
            - Write each query's result to a separate sheet in one workbook
            - Format headers, freeze the top row and auto-size columns
            - Save the workbook to a shared network folder with the date in the name
            - Run on weekdays at 06:30 with Windows Task Scheduler
Input:      Folder of .sql files, connection string in a config file
Tech stack: Python, pyodbc, pandas, XlsxWriter, Windows Task Scheduler
```

---

## Example 109

**Intent:**
find all TODO comments in my code

**Spec:**
```
Type:       Command-line tool (developer helper)
Features:   - Search source files for TODO, FIXME and HACK comments
            - Show file, line number and comment text
            - Show the author and date of each line using git blame with --blame
            - Filter by tag with --tag
            - Output as a Markdown checklist with --md
Input:      Project path
Tech stack: Python, ripgrep (subprocess), git
```

---

## Example 110

**Intent:**
tool to bulk rename files with a regex

**Spec:**
```
Type:       Command-line tool (file renaming)
Features:   - Match file names against a regular expression
            - Rename them using a replacement with capture groups
            - Show old and new names side by side before applying
            - Abort if two files would get the same name
            - Write an undo log so the renames can be reverted
Input:      Pattern, replacement, file glob, --undo
Tech stack: Rust, regex, clap
```

---

## Example 111

**Intent:**
I manage a few WordPress sites and want a script that once a week checks each one responds, has a valid certificate, and the plugins are updated, then sends me a report.

**Spec:**
```
Type:       Scheduled script (site health report)
Features:   - Check that each site returns HTTP 200 and measure response time
            - Check SSL certificate days until expiry
            - Run wp plugin list over SSH to find plugins with available updates
            - Build an HTML report with one section per site
            - Email the report every Monday morning
Input:      Sites config with URLs and SSH details, SMTP settings
Tech stack: Python, requests, Paramiko, WP-CLI, Jinja2, cron
```

---

## Example 112

**Intent:**
unzip all zip files in a folder each to its own folder

**Spec:**
```
Type:       Command-line script (archive extraction)
Features:   - Find all .zip files in a folder
            - Extract each archive into a folder with the archive's name
            - Protect against path traversal entries (zip slip)
            - Delete archives after successful extraction with --delete
            - Report archives that are corrupt
Input:      Folder path
Tech stack: Python, zipfile
```

---

## Example 113

**Intent:**
convert epub to pdf

**Spec:**
```
Type:       Command-line tool (ebook conversion)
Features:   - Convert an EPUB file to PDF
            - Set page size and margins with flags
            - Convert a whole folder of EPUB files at once
            - Keep the book title in the PDF metadata
Input:      EPUB file or folder, --paper-size, --margin
Tech stack: Bash, Calibre ebook-convert
```

---

## Example 114

**Intent:**
check a folder of json files are all valid

**Spec:**
```
Type:       Command-line tool (JSON validation)
Features:   - Parse every .json file in a folder
            - Report syntax errors with file, line and column
            - Validate files against a JSON Schema with --schema
            - Exit with a non-zero code when any file is invalid
Input:      Folder path, optional schema file
Tech stack: Node.js, ajv, fast-glob
```

---

## Example 115

**Intent:**
monitor reddit for posts mentioning my product and send to discord

**Spec:**
```
Type:       Scheduled script (social monitoring)
Features:   - Search chosen subreddits for posts and comments with given keywords
            - Run every 10 minutes and only handle new items
            - Post each match to a Discord channel through a webhook with title, subreddit and link
            - Ignore posts from a list of excluded users
Input:      Keywords, subreddits, Reddit API credentials and Discord webhook URL in .env
Tech stack: Python, PRAW, requests, cron
```

---

## Example 116

**Intent:**
script to set up my new linux machine with all my tools

**Spec:**
```
Type:       Command-line script (machine setup)
Features:   - Install packages from a list with apt
            - Install language tools (pyenv, nvm) and set default versions
            - Clone dotfiles and create symlinks to the home folder
            - Set zsh as the default shell
            - Be idempotent so it can run again safely
Input:      Package list file, dotfiles repository URL
Tech stack: Bash, apt, git
```

---

## Example 117

**Intent:**
generate qr codes for a list of urls

**Spec:**
```
Type:       Command-line tool (QR code generator)
Features:   - Read URLs and labels from a CSV file
            - Generate a QR code image for each URL
            - Save as PNG or SVG with --format
            - Name each file after its label
            - Set size and error correction level with flags
Input:      CSV file with url and label columns
Tech stack: Python, qrcode, Pillow
```

---

## Example 118

**Intent:**
delete files older than 30 days in a folder on windows

**Spec:**
```
Type:       Scheduled script (file cleanup)
Features:   - Find files older than 30 days by last write time
            - Delete them and remove folders left empty
            - Exclude file types listed in a parameter
            - Write deleted file paths to a log file
            - Run daily with Task Scheduler
Input:      Folder path, -Days, -Exclude
Tech stack: PowerShell, Windows Task Scheduler
```

---

## Example 119

**Intent:**
im a photographer, after a shoot i have raw + jpg of every pic, i delete the bad jpgs and want the matching raws deleted too

**Spec:**
```
Type:       Command-line script (photo cleanup)
Features:   - Pair RAW files (.cr2, .nef, .arw, .dng) with JPEGs that share the same base name
            - List RAW files whose JPEG was deleted
            - Move those orphan RAW files to a trash folder instead of deleting
            - Show the count and total size before moving
            - Support --dry-run
Input:      Shoot folder path
Tech stack: Python, pathlib, send2trash
```

---

## Example 120

**Intent:**
weekly email of what changed in our shared drive

**Spec:**
```
Type:       Scheduled script (change report)
Features:   - Scan a shared folder and record each file's path, size and modification time
            - Compare with last week's snapshot
            - List added, deleted and modified files
            - Email the list to the team every Friday
            - Save the new snapshot
Input:      Shared folder path, recipient list
Tech stack: Python, smtplib, cron
```

---

## Example 121

**Intent:**
convert a folder of images into one pdf

**Spec:**
```
Type:       Command-line tool (image to PDF)
Features:   - Collect images from a folder sorted by name
            - Fit each image to an A4 page with correct orientation
            - Combine all pages into one PDF
            - Compress images with --quality to keep the PDF small
Input:      Image folder, output PDF path
Tech stack: Python, img2pdf, Pillow
```

---

## Example 122

**Intent:**
nginx logs: show me 404 errors grouped by url so I can fix broken links

**Spec:**
```
Type:       Command-line tool (log analysis)
Features:   - Parse Nginx access logs, including rotated .gz files
            - Keep only requests with status 404
            - Group by requested URL and count hits
            - Show the top referrers for each missing URL
            - Ignore bot user agents with --no-bots
Input:      Log file paths, --top N
Tech stack: Bash, zcat, awk, sort
```

---

## Example 123

**Intent:**
Is it possible to automatically download my bank statements? No, ok, then at least when I download them they should go to the right folder by account and month.

**Spec:**
```
Type:       Scheduled script (file organizer)
Features:   - Watch the Downloads folder for new PDF and CSV files
            - Detect the bank account from the file name or text inside the PDF
            - Detect the statement month from the content
            - Move the file to Statements/Account/YYYY-MM
            - Leave unknown files in place and log them
Input:      Rules file mapping account numbers to folder names
Tech stack: Python, watchdog, pdfplumber
```

---

## Example 124

**Intent:**
random password for wifi

**Spec:**
```
Type:       Command-line tool (password helper)
Features:   - Generate a WPA2 passphrase of a chosen length
            - Avoid characters that are easy to confuse (0/O, 1/l)
            - Print a QR code for joining the WiFi network in the terminal
            - Use a secure random source
Input:      --length, --ssid
Tech stack: Python, secrets, qrcode
```

---

## Example 125

**Intent:**
make a script that tars up my website files and database and uploads to backblaze b2 every night

**Spec:**
```
Type:       Scheduled script (offsite backup)
Features:   - Dump the website database with pg_dump
            - Archive the web root and the dump into one tar.gz file
            - Encrypt the archive with GPG using a public key
            - Upload it to a Backblaze B2 bucket
            - Delete remote backups older than 30 days
Input:      Paths, database name and B2 credentials in a .env file
Tech stack: Bash, pg_dump, tar, gpg, rclone, cron
```

---

## Example 126

**Intent:**
show weather in terminal

**Spec:**
```
Type:       Command-line tool (weather)
Features:   - Get the current weather for a city or the detected location
            - Show temperature, conditions, wind and humidity
            - Show a 3-day forecast with --forecast
            - Switch units with --imperial
Input:      City name (optional)
Tech stack: Go, Open-Meteo API, cobra
```

---

## Example 127

**Intent:**
remove the background noise from my podcast audio files

**Spec:**
```
Type:       Command-line script (audio processing)
Features:   - Process every WAV or MP3 file in a folder
            - Apply noise reduction using a noise profile from a silent section
            - Normalize loudness to -16 LUFS
            - Save processed files with a _clean suffix
Input:      Audio folder, optional noise sample file
Tech stack: Python, noisereduce, pydub, ffmpeg (loudnorm)
```

---

## Example 128

**Intent:**
need to fetch data from an api every hour and save it into postgres

**Spec:**
```
Type:       Scheduled script (data ingestion)
Features:   - Call a REST API endpoint every hour with an API key
            - Handle pagination until all records are fetched
            - Upsert records into a PostgreSQL table by ID
            - Retry on errors with backoff and log failures
            - Run via cron
Input:      API URL and key, database URL in environment variables
Tech stack: Python, requests, psycopg2, cron
```

---

## Example 129

**Intent:**
tool that reads a word document and counts how often each word appears

**Spec:**
```
Type:       Command-line tool (text analysis)
Features:   - Extract text from a .docx file
            - Split it into words, lowercase them and drop punctuation
            - Ignore common stop words unless --keep-stopwords
            - Print the top N words with counts
            - Save the full word list to CSV
Input:      .docx file path, --top N
Tech stack: Python, python-docx, collections.Counter
```

---

## Example 130

**Intent:**
convert all my .txt files encoding from latin1 to utf8

**Spec:**
```
Type:       Command-line script (encoding conversion)
Features:   - Find .txt files in a folder recursively
            - Detect files that are not valid UTF-8
            - Convert them from Latin-1 (or a given encoding) to UTF-8
            - Keep a .orig backup of each converted file
Input:      Folder path, --from encoding
Tech stack: Bash, iconv, file
```

---

## Example 131

**Intent:**
Automatically delete my old tweets? Not tweets actually, I mean old emails in gmail older than 2 years from promotions

**Spec:**
```
Type:       Scheduled script (email cleanup)
Features:   - Connect to Gmail with the Gmail API
            - Search for messages in the Promotions category older than 2 years
            - Move matching messages to trash in batches
            - Log how many messages were removed each run
            - Run monthly via cron
Input:      OAuth client credentials file, --older-than
Tech stack: Python, Gmail API (google-api-python-client), cron
```

---

## Example 132

**Intent:**
Hi! I'm not technical, but I want to keep a copy of my Google Photos on my own hard drive. Can that be done every week?

**Spec:**
```
Type:       Scheduled script (cloud photo backup)
Features:   - Copy new photos and videos from Google Photos to a local folder
            - Organize them by year and month
            - Skip items that were already downloaded
            - Run once a week and log how many new items were copied
Input:      Google account authorized once through rclone config, target folder
Tech stack: rclone (Google Photos backend), Bash, cron
```

---

## Example 133

**Intent:**
Create a command to list biggest tables in my postgres db

**Spec:**
```
Type:       Command-line tool (database helper)
Features:   - Query PostgreSQL system catalogs for table, index and total sizes
            - Sort by total size and show the top N
            - Show the estimated row count for each table
            - Output as a table or CSV
Input:      Connection string, --top N
Tech stack: Python, psycopg2, tabulate
```

---

## Example 134

**Intent:**
send an sms when my home server goes offline

**Spec:**
```
Type:       Scheduled script (uptime alert)
Features:   - Ping the home server's public address every 5 minutes from a cloud VM
            - Send an SMS through Twilio after 3 failed checks
            - Send a recovery SMS when it is back online
            - Store the current state to avoid repeated alerts
Input:      Host address, phone number and Twilio credentials in .env
Tech stack: Python, Twilio API, cron
```

---

## Example 135

**Intent:**
split a pdf into separate pages

**Spec:**
```
Type:       Command-line tool (PDF utility)
Features:   - Split a PDF into one file per page
            - Split into ranges with --ranges 1-3,4-10
            - Name output files with the original name and page numbers
            - Save to an output folder
Input:      PDF path, --ranges, output folder
Tech stack: Python, pypdf
```

---

## Example 136

**Intent:**
script to check which of my domains are about to expire

**Spec:**
```
Type:       Scheduled script (domain monitor)
Features:   - Read domain names from a file
            - Look up each domain's expiry date with WHOIS
            - Warn when a domain expires within 30 days
            - Email a weekly list sorted by expiry date
Input:      Domains file, SMTP settings
Tech stack: Python, python-whois, smtplib, cron
```

---

## Example 137

**Intent:**
reformat dates in a csv column from dd/mm/yyyy to yyyy-mm-dd

**Spec:**
```
Type:       Command-line tool (CSV processing)
Features:   - Read a CSV and select the date column with --column
            - Parse dates with the input format given in --from
            - Write them in the output format given in --to
            - Leave unparseable values unchanged and count them
            - Write to a new file or stdout
Input:      CSV path, --column, --from, --to
Tech stack: Python, csv, datetime
```

---

## Example 138

**Intent:**
add page numbers to a pdf

**Spec:**
```
Type:       Command-line tool (PDF utility)
Features:   - Stamp a page number on every page of a PDF
            - Choose position (bottom center, bottom right) and font size
            - Start numbering from a given page with --start-page
            - Use a format string such as "Page {n} of {total}"
Input:      PDF path, --position, --format, -o output
Tech stack: Python, pypdf, ReportLab
```

---

## Example 139

**Intent:**
ban IPs that keep failing ssh login on my vps

**Spec:**
```
Type:       Scheduled script (security)
Features:   - Parse /var/log/auth.log for failed SSH password attempts
            - Count failures per IP address in the last 10 minutes
            - Block IPs above the limit with a ufw deny rule
            - Unblock IPs after 24 hours
            - Never block IPs on an allow list
Input:      Thresholds and allow list in a config file
Tech stack: Python, ufw, systemd timer
```

---

## Example 140

**Intent:**
i need to fill the same pdf form for 80 employees from a spreadsheet

**Spec:**
```
Type:       Command-line script (PDF form filling)
Features:   - Read the form field names from a fillable PDF
            - Map spreadsheet columns to form fields using a mapping file
            - Fill one copy of the form per row
            - Flatten the filled form so it cannot be edited
            - Name each PDF after the employee's ID
Input:      Fillable PDF, Excel file, column-to-field mapping JSON
Tech stack: Python, pypdf, pandas
```

---

## Example 141

**Intent:**
Write a PowerShell script that lists Active Directory users who haven't logged in for 90 days and exports them to a CSV for our audit.

**Spec:**
```
Type:       Command-line script (Active Directory audit)
Features:   - Query AD for enabled user accounts with LastLogonTimestamp older than 90 days
            - Include name, username, department and last logon date
            - Exclude service accounts in a given OU
            - Export the result to CSV with today's date in the name
            - Optionally disable the accounts with -Disable
Input:      -Days, -ExcludeOU, -Disable
Tech stack: PowerShell, ActiveDirectory module
```

---

## Example 142

**Intent:**
split long audio into chunks at the silent parts

**Spec:**
```
Type:       Command-line tool (audio splitting)
Features:   - Detect silent sections longer than a minimum length
            - Split the audio at those points
            - Merge chunks shorter than a minimum duration into the next one
            - Export numbered chunk files in the original format
Input:      Audio file, --min-silence ms, --silence-thresh dB
Tech stack: Python, pydub, ffmpeg
```

---

## Example 143

**Intent:**
download every new episode of my podcasts automatically

**Spec:**
```
Type:       Scheduled script (podcast downloader)
Features:   - Read a list of podcast RSS feed URLs
            - Parse each feed and find episodes not downloaded yet
            - Download the audio enclosure to a folder per podcast
            - Name files with the episode date and title
            - Keep only the last N episodes per podcast
Input:      Feeds file, --keep N
Tech stack: Python, feedparser, requests, cron
```

---

## Example 144

**Intent:**
scan my git repos for passwords or api keys that got committed by mistake

**Spec:**
```
Type:       Command-line tool (secret scanner)
Features:   - Scan the working tree and full git history of a repository
            - Match known secret patterns (AWS keys, private keys, tokens) and high-entropy strings
            - Report file, commit and line for each finding
            - Ignore findings listed in an allow file
            - Exit non-zero so it can run in CI
Input:      Repository path, --history flag
Tech stack: Go, go-git, regexp
```

---

## Example 145

**Intent:**
shift subtitles timing by 2 seconds

**Spec:**
```
Type:       Command-line tool (subtitle editing)
Features:   - Parse an .srt subtitle file
            - Shift all timestamps forward or backward by a given offset
            - Scale timing between two frame rates with --fps-from and --fps-to
            - Write the corrected file
Input:      SRT file, --offset seconds
Tech stack: Python, pysrt
```

---

## Example 146

**Intent:**
my zoom attendance reports come as csv, i need total minutes per student for the whole semester

**Spec:**
```
Type:       Data analysis script (attendance)
Features:   - Read all Zoom participant CSV files from a folder
            - Normalize names and match students by email
            - Sum minutes per student per meeting and in total
            - Flag students under a minimum attendance percentage
            - Export a summary to Excel
Input:      Folder of Zoom CSVs, roster CSV
Tech stack: Python, pandas, openpyxl
```

---

## Example 147

**Intent:**
alert me when bitcoin goes above or below a price

**Spec:**
```
Type:       Scheduled script (crypto price alert)
Features:   - Fetch the current BTC price from the CoinGecko API every 5 minutes
            - Compare against upper and lower thresholds
            - Send a desktop or Telegram notification when a threshold is crossed
            - Send one alert per crossing, not on every check
Input:      Thresholds and notification settings in a config file
Tech stack: Python, requests, CoinGecko API, cron
```

---

## Example 148

**Intent:**
update everything on my mac with one command, brew, app store, npm globals

**Spec:**
```
Type:       Command-line script (system update)
Features:   - Run brew update, brew upgrade and brew cleanup
            - Update App Store apps with mas
            - Update global npm packages
            - Update pip packages installed with --user
            - Print a summary of what was updated and any errors
Tech stack: Bash (zsh compatible), Homebrew, mas, npm, pip
```

---

## Example 149

**Intent:**
check health of my hard drives

**Spec:**
```
Type:       Scheduled script (disk health)
Features:   - Read SMART data from all drives with smartctl
            - Check reallocated sectors, pending sectors and overall health
            - Email a warning when any value is above zero or the test fails
            - Run a short self-test weekly
            - Log results each day
Input:      Email address in a config file
Tech stack: Bash, smartmontools, mail, cron
```

---

## Example 150

**Intent:**
Our accountant wants every invoice PDF to have the invoice number in the file name. They're all from the same accounting software so the layout is the same.

**Spec:**
```
Type:       Command-line script (PDF renaming)
Features:   - Extract text from the first page of each invoice PDF
            - Find the invoice number and date with regex patterns for that layout
            - Rename files to INV-<number>_<date>.pdf
            - Report files where the number was not found
            - Keep a CSV log of old and new names
Input:      Folder of invoice PDFs
Tech stack: Python, pdfplumber, re
```

---

## Example 151

**Intent:**
extract audio from all my videos

**Spec:**
```
Type:       Command-line script (media processing)
Features:   - Find video files in a folder
            - Extract the audio track without re-encoding when possible
            - Convert to MP3 with --mp3
            - Name each audio file after its video
Input:      Folder path, --mp3
Tech stack: Bash, ffmpeg
```

---

## Example 152

**Intent:**
mirror our gitlab repos to github as backup every night

**Spec:**
```
Type:       Scheduled script (repository mirror)
Features:   - List all projects in a GitLab group through the API
            - Create matching private repositories on GitHub if they do not exist
            - Clone with --mirror or fetch updates for existing mirrors
            - Push all branches and tags with git push --mirror
            - Log failures per repository
Input:      GitLab group, GitLab and GitHub tokens in environment variables
Tech stack: Python, python-gitlab, PyGithub, git, cron
```

---

## Example 153

**Intent:**
tool to shorten long file paths on windows that are over 260 chars

**Spec:**
```
Type:       Command-line script (path fix)
Features:   - Scan a folder for files whose full path is over 260 characters
            - List them with their path length
            - Shorten folder or file names by trimming to a max length and adding a counter
            - Show a preview before renaming
            - Export the list to CSV
Input:      Folder path, -MaxLength, -WhatIf
Tech stack: PowerShell
```

---

## Example 154

**Intent:**
mask names and emails in a csv before sending it to a vendor

**Spec:**
```
Type:       Command-line tool (data anonymization)
Features:   - Read a CSV and select columns to mask with --columns
            - Replace emails and names with consistent fake values or salted hashes
            - Keep the same masked value for the same input so joins still work
            - Write the anonymized CSV
Input:      CSV path, --columns, --salt
Tech stack: Python, pandas, Faker, hashlib
```

---

## Example 155

**Intent:**
daily check that last night's backup actually happened

**Spec:**
```
Type:       Scheduled script (backup verification)
Features:   - Find the newest file in the backup folder
            - Check that it is less than 26 hours old and above a minimum size
            - Test the archive integrity (tar -tzf or gzip -t)
            - Send an alert email if any check fails
            - Send a short OK message on Mondays
Input:      Backup folder, minimum size, email address
Tech stack: Bash, gzip, tar, mail, cron
```

---

## Example 156

**Intent:**
favicon generator from one png

**Spec:**
```
Type:       Command-line tool (icon generation)
Features:   - Take a square PNG or SVG source image
            - Generate favicon.ico with 16, 32 and 48 px sizes
            - Generate apple-touch-icon and Android icons in standard sizes
            - Write a site.webmanifest and the HTML link tags to copy
Input:      Source image, output folder
Tech stack: Node.js, sharp, png-to-ico
```

---

## Example 157

**Intent:**
hi, my wife has bakery and she uses google sheet for orders, she want get a message at morning with today orders list

**Spec:**
```
Type:       Scheduled script (daily order summary)
Features:   - Read the orders Google Sheet
            - Select orders whose pickup date is today
            - Build a message with customer name, items and pickup time
            - Send the message by Telegram every morning at 6:00
            - Send "no orders today" when the list is empty
Input:      Sheet ID, service account key, Telegram bot token and chat ID
Tech stack: Python, gspread, Telegram Bot API, cron
```

---

## Example 158

**Intent:**
make a timelapse video from a folder of photos

**Spec:**
```
Type:       Command-line tool (timelapse)
Features:   - Sort photos by name or EXIF time
            - Encode them into an MP4 at a chosen frame rate
            - Scale to 1080p or 4K with --size
            - Add optional deflicker filter
Input:      Photo folder, --fps, --size, -o output
Tech stack: Bash, ffmpeg
```

---

## Example 159

**Intent:**
add a copyright header to all source files that are missing it

**Spec:**
```
Type:       Command-line tool (developer helper)
Features:   - Find source files by extension (.py, .js, .ts, .go)
            - Check whether the first lines already contain the header
            - Insert the header with the correct comment syntax per language
            - Keep shebang lines on top
            - Run in --check mode for CI without changing files
Input:      Project folder, header template file
Tech stack: Python, pathlib, argparse
```

---

## Example 160

**Intent:**
get notified when the library book i want is available

**Spec:**
```
Type:       Scheduled script (availability monitor)
Features:   - Search the library catalogue page for each book on a watch list
            - Read the availability status of each copy
            - Email me when any copy changes to "available"
            - Run twice a day
Input:      Watch list with book titles or catalogue IDs
Tech stack: Python, requests, BeautifulSoup, smtplib, cron
```

---

## Example 161

**Intent:**
create users in bulk from a csv on linux

**Spec:**
```
Type:       Command-line script (user provisioning)
Features:   - Read username, full name and groups from a CSV
            - Create each user with useradd and a home directory
            - Add users to the listed groups, creating groups if missing
            - Set a random temporary password and force change at first login
            - Skip users that already exist
Input:      CSV file
Tech stack: Bash, useradd, chpasswd, chage
```

---

## Example 162

**Intent:**
convert flac music library to aac for my phone but keep the folder structure

**Spec:**
```
Type:       Command-line script (audio conversion)
Features:   - Walk the FLAC library and mirror its folder structure in the output folder
            - Convert each .flac to .m4a AAC at 256 kbps
            - Copy tags and cover art
            - Copy cover image files as they are
            - Skip tracks already converted and newer than the source
Input:      Library path, output path
Tech stack: Bash, ffmpeg, GNU parallel
```

---

## Example 163

**Intent:**
find photos that are blurry so i can delete them

**Spec:**
```
Type:       Command-line tool (photo quality check)
Features:   - Load each image in a folder
            - Measure sharpness with the variance of the Laplacian
            - List images below a threshold sorted by score
            - Move blurry images to a review folder with --move
Input:      Photo folder, --threshold, --move
Tech stack: Python, OpenCV
```

---

## Example 164

**Intent:**
Sometimes I need a quick summary of a giant JSON log from our app: errors per service per hour. A CLI for that would be nice.

**Spec:**
```
Type:       Command-line tool (log analysis)
Features:   - Read JSON Lines log files or stdin
            - Filter records by level (ERROR, WARN)
            - Group counts by service field and hour
            - Print a table and an ASCII bar per service
            - Accept --from and --to time filters
Input:      Log file paths, --level, --from, --to
Tech stack: Go, encoding/json, tablewriter
```

---

## Example 165

**Intent:**
send my kindle the pdfs i drop in a folder

**Spec:**
```
Type:       Command-line script (send to Kindle)
Features:   - Watch a folder for new PDF and EPUB files
            - Email each file as an attachment to the Kindle address
            - Move sent files to a "sent" subfolder
            - Retry later if sending fails
Input:      Watched folder, Kindle email and SMTP settings in .env
Tech stack: Python, watchdog, smtplib
```

---

## Example 166

**Intent:**
what services failed on my server today

**Spec:**
```
Type:       Command-line tool (system check)
Features:   - List systemd units in failed state
            - Show the last 20 journal lines for each failed unit
            - Show units that restarted more than N times today
            - Restart failed units after confirmation with --restart
Tech stack: Bash, systemctl, journalctl
```

---

## Example 167

**Intent:**
Converting xml exports from our old system to csv please, the files have nested items

**Spec:**
```
Type:       Command-line tool (format conversion)
Features:   - Parse XML files and select repeating records with an XPath expression
            - Flatten nested elements into columns using dotted names
            - Write one row per record, or one row per nested item with --explode
            - Handle missing elements as empty values
            - Process a whole folder of XML files
Input:      XML file or folder, --record-xpath, --explode
Tech stack: Python, lxml, csv
```

---

## Example 168

**Intent:**
email myself a list of what i committed this week every friday

**Spec:**
```
Type:       Scheduled script (git activity report)
Features:   - Scan a list of local repositories
            - Collect my commits from the last 7 days by author email
            - Group commits by repository with message and date
            - Email the summary every Friday at 17:00
Input:      Repository paths and author email in a config file
Tech stack: Python, GitPython, smtplib, cron
```

---

## Example 169

**Intent:**
cleanup node_modules folders i dont need anymore

**Spec:**
```
Type:       Command-line tool (disk cleanup)
Features:   - Find node_modules folders under a root path
            - Show each one with its project and size
            - Select projects not modified in N days
            - Delete selected folders after confirmation
            - Print total space freed
Input:      Root path, --days
Tech stack: Node.js, fast-glob, inquirer
```

---

## Example 170

**Intent:**
make a script to get exchange rates every day and save them in an excel file

**Spec:**
```
Type:       Scheduled script (exchange rates)
Features:   - Fetch daily exchange rates for chosen currencies from the ECB feed
            - Append a row per day to an Excel sheet
            - Avoid duplicate rows when run twice on the same day
            - Highlight changes of more than 1% from the previous day
Input:      Currency list, Excel file path
Tech stack: Python, requests, openpyxl, cron
```

---

## Example 171

**Intent:**
need a terminal tool to convert units like kg to lbs, km to miles

**Spec:**
```
Type:       Command-line tool (unit converter)
Features:   - Convert between common units of length, weight, temperature and volume
            - Parse input like "5 km to mi"
            - Show results with a chosen number of decimals
            - List supported units with --list
Input:      Expression as arguments
Tech stack: Python, pint
```

---

## Example 172

**Intent:**
renew letsencrypt certs and restart nginx automatically

**Spec:**
```
Type:       Scheduled script (certificate renewal)
Features:   - Run certbot renew twice a day
            - Reload Nginx only when a certificate was renewed, using a deploy hook
            - Test the Nginx config before reloading
            - Email the admin if renewal fails
Tech stack: Bash, certbot, Nginx, systemd timer
```

---

## Example 173

**Intent:**
compare prices of the same product on 3 shops

**Spec:**
```
Type:       Command-line tool (price comparison)
Features:   - Read product names and shop URLs from a config file
            - Scrape the price from each shop page with a per-shop CSS selector
            - Normalize prices to the same currency
            - Print a table sorted by price with the cheapest highlighted
Input:      Config file with products, URLs and selectors
Tech stack: Node.js, axios, cheerio
```

---

## Example 174

**Intent:**
im on windows and want to rename hundreds of files by adding the date in front

**Spec:**
```
Type:       Command-line script (file renaming)
Features:   - Get all files in a folder
            - Prefix each name with its last write date as yyyy-MM-dd_
            - Skip files that already start with a date
            - Preview with -WhatIf before renaming
Input:      Folder path
Tech stack: PowerShell, Rename-Item
```

---

## Example 175

**Intent:**
generate a sitemap.xml for my static site

**Spec:**
```
Type:       Command-line tool (sitemap generator)
Features:   - Walk the built site folder for .html files
            - Convert file paths to URLs using a base URL
            - Use file modification time as lastmod
            - Exclude paths matching patterns
            - Write sitemap.xml to the site root
Input:      Site folder, --base-url, --exclude
Tech stack: Python, pathlib, xml.etree.ElementTree
```

---

## Example 176

**Intent:**
i want to track how long my scripts take each day so i can see if theyre getting slower

**Spec:**
```
Type:       Command-line tool (run timer)
Features:   - Wrap any command and measure wall time, CPU time and exit code
            - Append each run with the command name to a history database
            - Show the average and trend per command with a stats subcommand
            - Warn when a run is 50% slower than the average
Input:      Command to run after --
Tech stack: Python, subprocess, sqlite3, resource
```

---

## Example 177

**Intent:**
make an excel invoice for each client from timesheet hours

**Spec:**
```
Type:       Command-line script (invoice generation)
Features:   - Read time entries from a CSV with client, date, hours and description
            - Group entries by client for a given month
            - Fill an Excel invoice template with line items, hourly rate and totals
            - Give each invoice the next number from a counter file
            - Save one file per client
Input:      Timesheet CSV, --month, invoice template, client rates file
Tech stack: Python, pandas, openpyxl
```

---

## Example 178

**Intent:**
tail a log file and beep when the word ERROR shows up

**Spec:**
```
Type:       Command-line tool (log watcher)
Features:   - Follow a log file like tail -f, handling log rotation
            - Match lines against one or more patterns
            - Highlight matches in color
            - Play a sound or show a notification on match
            - Rate-limit alerts to one per 30 seconds
Input:      Log file path, --pattern (repeatable)
Tech stack: Python, watchdog, plyer
```

---

## Example 179

**Intent:**
convert svg logo to png in many sizes

**Spec:**
```
Type:       Command-line tool (image export)
Features:   - Render an SVG file to PNG
            - Export multiple widths given with --sizes 64,128,256,512
            - Keep transparency
            - Name output files logo-<size>.png
Input:      SVG path, --sizes, output folder
Tech stack: Node.js, sharp
```

---

## Example 180

**Intent:**
script to download all attachments from a gmail label

**Spec:**
```
Type:       Command-line script (email attachment download)
Features:   - Authenticate with the Gmail API using OAuth
            - List messages under a given label
            - Download every attachment to a folder named after the label
            - Prefix files with the email date to avoid name clashes
            - Skip attachments already downloaded
Input:      Label name, output folder, OAuth credentials file
Tech stack: Python, google-api-python-client
```

---

## Example 181

**Intent:**
check my website for slow pages

**Spec:**
```
Type:       Command-line tool (performance check)
Features:   - Read a list of URLs or a sitemap.xml
            - Request each page several times and measure time to first byte and total time
            - Report the median time and page size per URL
            - Flag pages slower than a threshold
Input:      URL list or sitemap URL, --runs, --threshold ms
Tech stack: Go, net/http, httptrace
```

---

## Example 182

**Intent:**
encrypt my .env file so i can commit it

**Spec:**
```
Type:       Command-line tool (secret management)
Features:   - Encrypt a .env file to .env.age with one or more recipient public keys
            - Decrypt it back for local use
            - Add the plain .env to .gitignore automatically
            - Show which keys changed between the encrypted and local version without printing values
Input:      encrypt, decrypt or diff subcommand
Tech stack: Bash, age
```

---

## Example 183

**Intent:**
watermark pdf pages with CONFIDENTIAL

**Spec:**
```
Type:       Command-line tool (PDF watermark)
Features:   - Overlay diagonal text on every page of a PDF
            - Set text, opacity, color and font size with flags
            - Apply to all PDFs in a folder at once
            - Write watermarked copies with a _wm suffix
Input:      PDF file or folder, --text, --opacity
Tech stack: Python, PyMuPDF
```

---

## Example 184

**Intent:**
ok so im running a discord community and we have a google form for event signups, the responses go into a sheet. i want a script that every evening checks new signups and posts the count and names to our discord channel. nothing fancy

**Spec:**
```
Type:       Scheduled script (signup summary)
Features:   - Read the form responses sheet with the Google Sheets API
            - Find rows added since the last run using the timestamp column
            - Post the number of new signups and their names to a Discord webhook
            - Save the last processed timestamp
            - Run every evening at 20:00
Input:      Sheet ID, service account key, Discord webhook URL
Tech stack: Python, gspread, requests, cron
```

---

## Example 185

**Intent:**
password protect all the pdfs in a folder

**Spec:**
```
Type:       Command-line script (PDF encryption)
Features:   - Encrypt each PDF in a folder with AES-256
            - Use one password from a prompt or a per-file password from a CSV
            - Disable printing or copying with permission flags
            - Save protected copies to an output folder
Input:      Folder of PDFs, optional passwords CSV
Tech stack: Bash, qpdf
```

---

## Example 186

**Intent:**
Ich möchte ein script, das jeden tag die neuen dateien vom FTP server holt. sorry my english, I mean download new files from ftp each day.

**Spec:**
```
Type:       Scheduled script (FTP download)
Features:   - Connect to the FTP server with FTPS
            - List files in the remote folder
            - Download files that are not yet present locally or have a different size
            - Verify the download size
            - Run daily via cron and log the downloaded files
Input:      Host, user, password and remote folder in a config file
Tech stack: Python, ftplib, cron
```

---

## Example 187

**Intent:**
pretty print and sort keys in all json files

**Spec:**
```
Type:       Command-line tool (JSON formatter)
Features:   - Reformat JSON files with a chosen indent
            - Sort object keys alphabetically with --sort-keys
            - Check mode that exits non-zero when a file is not formatted
            - Process globs of files in place
Input:      File glob, --indent, --check
Tech stack: Node.js, fast-glob
```

---

## Example 188

**Intent:**
report of how much each person changed in our repo

**Spec:**
```
Type:       Command-line tool (git statistics)
Features:   - Read git log with numstat for a date range
            - Sum commits, lines added and lines removed per author
            - Merge author aliases from a .mailmap file
            - Print a ranked table and export to CSV
Input:      Repository path, --since, --until
Tech stack: Python, subprocess (git log --numstat), pandas
```

---

## Example 189

**Intent:**
cut silence from beginning and end of all audio files

**Spec:**
```
Type:       Command-line script (audio trimming)
Features:   - Detect leading and trailing silence in each audio file
            - Trim it while keeping a short padding
            - Keep the original format and bitrate
            - Process a folder in parallel
Input:      Audio folder, --threshold dB, --padding ms
Tech stack: Bash, sox
```

---

## Example 190

**Intent:**
get all the pdf files linked on a webpage

**Spec:**
```
Type:       Command-line tool (bulk downloader)
Features:   - Load a web page and find links ending in .pdf
            - Follow links one level deep with --depth 1
            - Download each PDF and skip existing files
            - Keep the original file names, adding a counter for clashes
Input:      Page URL, output folder, --depth
Tech stack: Bash, wget (recursive with accept filter)
```

---

## Example 191

**Intent:**
script to restart my app if it crashes and send me a message

**Spec:**
```
Type:       Scheduled script (process watchdog)
Features:   - Check every minute whether the app process is running or the health URL responds
            - Restart the app with its start command when it is down
            - Send a Telegram message with the time and the last 20 log lines
            - Stop restarting after 5 failures in an hour and alert instead
Input:      Process name, health URL, start command, Telegram settings
Tech stack: Bash, curl, pgrep, cron
```

---

## Example 192

**Intent:**
convert docx to markdown

**Spec:**
```
Type:       Command-line tool (document conversion)
Features:   - Convert .docx files to Markdown keeping headings, lists, tables and links
            - Extract embedded images to a media folder
            - Process a single file or a folder
            - Choose GitHub-flavored Markdown output
Input:      File or folder, output folder
Tech stack: Bash, Pandoc
```

---

## Example 193

**Intent:**
i keep forgetting birthdays, can i have something that emails me a day before using a csv of names and dates

**Spec:**
```
Type:       Scheduled script (birthday reminders)
Features:   - Read names and birth dates from a CSV
            - Check every morning for birthdays tomorrow
            - Email a reminder with the person's name and age they will turn
            - Handle February 29 birthdays in non-leap years
Input:      Birthdays CSV, email settings
Tech stack: Python, csv, smtplib, cron
```

---

## Example 194

**Intent:**
Make a CLI to query a CSV with SQL

**Spec:**
```
Type:       Command-line tool (CSV query)
Features:   - Load one or more CSV files as tables named after the files
            - Run a SQL query given as an argument
            - Infer column types automatically
            - Print results as a table, CSV or JSON
Input:      CSV paths, SQL query, --format
Tech stack: Python, DuckDB, click
```

---

## Example 195

**Intent:**
my photos from different cameras have wrong times, shift them by a few hours

**Spec:**
```
Type:       Command-line script (photo metadata fix)
Features:   - Select photos by camera model or folder
            - Shift DateTimeOriginal and related EXIF dates by a given offset
            - Update the file modification time to match
            - Keep backups of the originals unless --overwrite is given
Input:      Folder, --offset (e.g. +3:00), --camera
Tech stack: ExifTool, Bash
```

---

## Example 196

**Intent:**
report all open ports on my servers every week

**Spec:**
```
Type:       Scheduled script (port audit)
Features:   - Scan a list of servers for open TCP ports with nmap
            - Compare results to an expected port list per server
            - Report unexpected open ports and expected ports that are closed
            - Email the report weekly
Input:      Server list and expected ports in a YAML file
Tech stack: Python, python-nmap, PyYAML, smtplib, cron
```

---

## Example 197

**Intent:**
need to grab table data from a website into csv

**Spec:**
```
Type:       Command-line tool (web table scraper)
Features:   - Fetch a web page and find all HTML tables
            - Pick a table by index or by a CSS selector
            - Use the header row as column names
            - Write the table to CSV
Input:      URL, --index or --selector, -o output
Tech stack: Python, pandas (read_html), lxml
```

---

## Example 198

**Intent:**
make my laptop wallpaper change to nasa picture of the day every morning

**Spec:**
```
Type:       Scheduled script (wallpaper)
Features:   - Fetch NASA's Astronomy Picture of the Day through the APOD API
            - Download the HD image (skip days when it is a video)
            - Set it as the desktop wallpaper
            - Keep the last 30 images in a folder
Input:      NASA API key
Tech stack: Python, requests, GNOME gsettings, cron
```

---

## Example 199

**Intent:**
tool to quickly compress a folder into tar.gz with date in the name

**Spec:**
```
Type:       Command-line tool (archiving)
Features:   - Create a tar.gz archive of a folder
            - Name it <folder>_YYYYMMDD_HHMM.tar.gz
            - Exclude patterns with --exclude
            - Use multi-threaded compression when pigz is available
            - Print the archive size
Input:      Folder path, --exclude, output folder
Tech stack: Bash, tar, pigz
```

---

## Example 200

**Intent:**
monitor apartment rental listings for new ones under 1200

**Spec:**
```
Type:       Scheduled script (listing monitor)
Features:   - Fetch rental search results for a city and filters
            - Parse price, size, address and link for each listing
            - Keep only listings under the price limit that were not seen before
            - Send new listings by email with the first photo
            - Run every 30 minutes
Input:      Search URL and price limit in a config file
Tech stack: Python, requests, BeautifulSoup, sqlite3, cron
```

---

## Example 201

**Intent:**
csv -> sqlite

**Spec:**
```
Type:       Command-line tool (data import)
Features:   - Create a SQLite table from a CSV file's header
            - Infer column types (integer, real, text)
            - Insert rows in batches inside a transaction
            - Append to or replace an existing table with flags
Input:      CSV path, database path, --table
Tech stack: Python, sqlite3, csv
```

---

## Example 202

**Intent:**
Is there a way to find all files on our file server that haven't been opened in 3 years, and give a list to management with sizes per department folder?

**Spec:**
```
Type:       Command-line script (storage report)
Features:   - Scan department folders on the file server
            - Find files whose last access and modification are older than 3 years
            - Sum size and count of stale files per department
            - Export a detailed CSV and an Excel summary per department
            - Run with read-only access so nothing is changed
Input:      Root share path, --years
Tech stack: PowerShell, Get-ChildItem, ImportExcel module
```

---

## Example 203

**Intent:**
auto reply email when i'm on vacation for a custom mailbox without that feature

**Spec:**
```
Type:       Scheduled script (email auto-reply)
Features:   - Check the inbox over IMAP every 5 minutes for new messages
            - Send an out-of-office reply using a template with the return date
            - Reply only once per sender during the vacation period
            - Skip mailing lists and no-reply senders
            - Stop after the configured end date
Input:      IMAP/SMTP settings, start and end dates, reply template
Tech stack: Python, imaplib, smtplib, cron
```

---

## Example 204

**Intent:**
generate test data csv with fake names and addresses

**Spec:**
```
Type:       Command-line tool (test data generator)
Features:   - Generate N rows of fake data
            - Choose columns from a list (name, email, address, phone, date, company)
            - Set the locale for realistic local data
            - Use a seed for repeatable output
            - Write CSV or JSON
Input:      --rows, --columns, --locale, --seed
Tech stack: Python, Faker, click
```

---

## Example 205

**Intent:**
hourly snapshot of my zfs datasets and delete old ones

**Spec:**
```
Type:       Scheduled script (ZFS snapshots)
Features:   - Create a snapshot of each configured dataset every hour
            - Name snapshots with a timestamp prefix
            - Keep 24 hourly, 7 daily and 4 weekly snapshots
            - Destroy snapshots outside the retention policy
            - Log created and destroyed snapshots
Input:      Dataset list and retention settings
Tech stack: Bash, zfs, cron
```

---

## Example 206

**Intent:**
im learning japanese, i want to pull all the words from my anki export and count which kanji appear most

**Spec:**
```
Type:       Data analysis script (text analysis)
Features:   - Read the exported Anki deck text file
            - Extract kanji characters using their Unicode range
            - Count how often each kanji appears
            - Print the top N with counts
            - Save the full list to CSV
Input:      Anki export file, --top N
Tech stack: Python, collections.Counter, unicodedata
```

---

## Example 207

**Intent:**
create a contact sheet from a folder of photos

**Spec:**
```
Type:       Command-line tool (image montage)
Features:   - Arrange photos in a grid with a chosen number of columns
            - Add file names under each thumbnail
            - Split into several pages when there are too many photos
            - Save as JPEG or PDF
Input:      Photo folder, --columns, --format
Tech stack: Bash, ImageMagick montage
```

---

## Example 208

**Intent:**
fix permissions in my web folder, files 644 and folders 755

**Spec:**
```
Type:       Command-line script (permissions fix)
Features:   - Set all directories under a path to 755
            - Set all files to 644
            - Make files listed in an exceptions list executable
            - Change owner to the web server user with --owner
Input:      Web root path, --owner
Tech stack: Bash, find, chmod, chown
```

---

## Example 209

**Intent:**
summarize which ip addresses hit my api the most from cloudflare logs

**Spec:**
```
Type:       Data analysis script (log analysis)
Features:   - Read Cloudflare logs exported as JSON Lines
            - Count requests per client IP, country and path
            - Show the top 20 IPs with their request rate per minute
            - Flag IPs with high error rates or many distinct paths
Input:      Log files, --top
Tech stack: Python, pandas
```

---

## Example 210

**Intent:**
what about a script for when i insert my sd card it copies the photos off automatically

**Spec:**
```
Type:       Command-line script (photo import)
Features:   - Detect when an SD card with a DCIM folder is mounted
            - Copy new photos and videos to a dated folder
            - Verify each copy by checksum
            - Eject the card when done
            - Show a desktop notification with the number of files imported
Input:      Destination folder
Tech stack: Bash, udev rule, rsync, notify-send
```

---

## Example 211

**Intent:**
Could you write something that makes a weekly PDF report from our Google Analytics data, sessions, top pages and sources?

**Spec:**
```
Type:       Scheduled script (analytics report)
Features:   - Query the Google Analytics Data API for the last 7 days
            - Get sessions per day, top 10 pages and top traffic sources
            - Draw a line chart of daily sessions
            - Build a PDF with tables and the chart
            - Email it every Monday
Input:      GA4 property ID, service account key, recipient list
Tech stack: Python, google-analytics-data, matplotlib, ReportLab, cron
```

---

## Example 212

**Intent:**
copy only certain file types from one drive to another keeping the folders

**Spec:**
```
Type:       Command-line script (selective copy)
Features:   - Copy files matching extensions (e.g. .jpg, .pdf, .docx) from a source to a destination
            - Recreate the folder structure
            - Skip files that already exist with the same size and date
            - Show progress and a final summary
Input:      Source path, destination path, extension list
Tech stack: Windows robocopy, batch file
```

---

## Example 213

**Intent:**
turn a list of urls into a markdown list with page titles

**Spec:**
```
Type:       Command-line tool (link formatter)
Features:   - Read URLs from a file or stdin
            - Fetch each page and read its title tag
            - Output a Markdown list of [title](url)
            - Fall back to the URL when no title is found
            - Fetch pages concurrently
Input:      URL file or stdin
Tech stack: Node.js, undici, cheerio
```

---

## Example 214

**Intent:**
sync my local music folder to my phone over usb

**Spec:**
```
Type:       Command-line script (device sync)
Features:   - Detect the phone through MTP or ADB
            - Copy new music files and playlists to the phone's Music folder
            - Remove files on the phone that were deleted locally with --delete
            - Skip files that are already there
Input:      Local music folder
Tech stack: Bash, adb (adb-sync)
```

---

## Example 215

**Intent:**
a script to tell me when a government website updates their page with new notices

**Spec:**
```
Type:       Scheduled script (page change monitor)
Features:   - Fetch the notices page every hour
            - Extract the notices list with a CSS selector to ignore unrelated page changes
            - Compare with the last saved version
            - Email the new notice titles and links when there are changes
Input:      Page URL, CSS selector, email settings
Tech stack: Python, requests, BeautifulSoup, difflib, cron
```

---

## Example 216

**Intent:**
remove exif from all images and rename them randomly before upload

**Spec:**
```
Type:       Command-line script (image anonymization)
Features:   - Strip all EXIF, IPTC and XMP metadata from images
            - Rename each file to a random UUID keeping the extension
            - Save a private CSV mapping original to new names
            - Write the cleaned images to an output folder
Input:      Image folder, output folder
Tech stack: Python, Pillow, uuid
```

---

## Example 217

**Intent:**
sum up hours in a timesheet excel and flag overtime

**Spec:**
```
Type:       Command-line script (timesheet calculation)
Features:   - Read start and end times per employee per day from Excel
            - Calculate daily hours minus breaks
            - Sum weekly hours per employee
            - Flag days over 10 hours and weeks over 40 hours
            - Write a summary sheet back into the workbook
Input:      Timesheet Excel file
Tech stack: Python, openpyxl, pandas
```

---

## Example 218

**Intent:**
rotate my aws access keys automatically

**Spec:**
```
Type:       Scheduled script (credential rotation)
Features:   - List access keys of an IAM user and find ones older than 90 days
            - Create a new access key
            - Update the stored secret in AWS Secrets Manager
            - Deactivate the old key and delete it after 7 days
            - Log each rotation
Input:      IAM user name, secret name
Tech stack: Python, boto3, cron
```

---

## Example 219

**Intent:**
download all photos from a shared google drive folder

**Spec:**
```
Type:       Command-line tool (Drive downloader)
Features:   - Authenticate with the Google Drive API
            - List all files in the folder, including subfolders
            - Download image files keeping the folder structure
            - Skip files that already exist with the same size
Input:      Folder ID, output path, OAuth credentials file
Tech stack: Python, google-api-python-client
```

---

## Example 220

**Intent:**
convert line endings windows to unix in a project

**Spec:**
```
Type:       Command-line tool (text processing)
Features:   - Find text files in a project, skipping binary files
            - Convert CRLF to LF
            - Skip folders like .git and node_modules
            - Report how many files were changed
Input:      Project folder
Tech stack: Bash, dos2unix, find
```

---

## Example 221

**Intent:**
i want a cli to look up passwords in my keepass file without opening the app

**Spec:**
```
Type:       Command-line tool (password manager helper)
Features:   - Open a KeePass .kdbx database with the master password from a prompt
            - Search entries by title or URL
            - Copy the password to the clipboard and clear it after 20 seconds
            - Print the username but never print the password
Input:      Database path, search term
Tech stack: Python, pykeepass, pyperclip, getpass
```

---

## Example 222

**Intent:**
Every day my Python job writes logs and I want the warnings and errors from yesterday put into a short email so I can read it over coffee.

**Spec:**
```
Type:       Scheduled script (log digest)
Features:   - Read yesterday's application log files
            - Keep only WARNING and ERROR lines
            - Group similar messages and count them
            - Email the summary with the 10 most frequent messages
            - Run daily at 07:30
Input:      Log folder, email settings
Tech stack: Python, re, collections, smtplib, cron
```

---

## Example 223

**Intent:**
put a border and caption on every image

**Spec:**
```
Type:       Command-line script (bulk image processing)
Features:   - Add a colored border of a set width around each image
            - Write a caption below the image from the file name or a CSV
            - Choose font and size
            - Save results to an output folder
Input:      Image folder, --border, --color, captions CSV
Tech stack: Python, Pillow
```

---

## Example 224

**Intent:**
script to find all symlinks that point to nothing

**Spec:**
```
Type:       Command-line tool (file system check)
Features:   - Search a directory tree for symbolic links
            - Report links whose target does not exist
            - Delete broken links with --delete after confirmation
            - Output the list as plain text
Input:      Path, --delete
Tech stack: Bash, find -xtype l
```

---

## Example 225

**Intent:**
run a speed test every hour and save to csv so i can show my isp they suck

**Spec:**
```
Type:       Scheduled script (internet speed log)
Features:   - Run an internet speed test every hour
            - Record download, upload, ping and server
            - Append results with a timestamp to a CSV
            - Generate a chart of the last 30 days with a report subcommand
Input:      Output CSV path
Tech stack: Python, speedtest-cli, matplotlib, cron
```

---

## Example 226

**Intent:**
generate an htpasswd file entry

**Spec:**
```
Type:       Command-line tool (password helper)
Features:   - Create a username and bcrypt-hashed password line for .htpasswd
            - Prompt for the password twice without echo
            - Add to or update an existing .htpasswd file
Input:      File path, username
Tech stack: Python, bcrypt, getpass
```

---

## Example 227

**Intent:**
burn subtitles into a video permanently

**Spec:**
```
Type:       Command-line tool (video subtitles)
Features:   - Render an .srt or .ass subtitle file onto the video frames
            - Set font size and outline with flags
            - Keep the original audio without re-encoding
            - Write the result as MP4
Input:      Video file, subtitle file, --font-size, -o output
Tech stack: Bash, ffmpeg (subtitles filter)
```

---

## Example 228

**Intent:**
discord says my clip is too big, make it under 25mb

**Spec:**
```
Type:       Command-line tool (video compression)
Features:   - Read the video duration with ffprobe
            - Calculate the video bitrate needed to fit a target size
            - Encode with two-pass H.264 at that bitrate
            - Lower the resolution to 720p if the bitrate would be too low
            - Print the final file size
Input:      Video file, --target-mb (default 25)
Tech stack: Python, ffmpeg, ffprobe
```

---

## Example 229

**Intent:**
all my phone videos are sideways, rotate them

**Spec:**
```
Type:       Command-line script (video rotation)
Features:   - Read rotation metadata from each video
            - Rotate selected videos by 90, 180 or 270 degrees
            - Change the rotation metadata only when --metadata-only is set (no re-encode)
            - Save results with a _rotated suffix
Input:      Video files or folder, --angle
Tech stack: Bash, ffmpeg
```

---

## Example 230

**Intent:**
make an audiobook m4b file from a folder of mp3 chapters

**Spec:**
```
Type:       Command-line tool (audiobook builder)
Features:   - Sort chapter MP3 files by name
            - Join them into one AAC audio stream
            - Add a chapter marker at the start of each file using its title
            - Embed cover art and book metadata
            - Write an .m4b file
Input:      Chapter folder, cover image, --title, --author
Tech stack: Python, ffmpeg, mutagen
```

---

## Example 231

**Intent:**
songs in my playlist have different loudness, fix it

**Spec:**
```
Type:       Command-line script (audio normalization)
Features:   - Scan MP3 and FLAC files in a folder
            - Calculate ReplayGain track and album gain
            - Write gain tags without changing the audio
            - Optionally apply the gain to the audio with --apply
Input:      Music folder, --apply
Tech stack: Bash, rsgain, ffmpeg
```

---

## Example 232

**Intent:**
dj here, i need the bpm and key of all my tracks written into the tags so i can sort them

**Spec:**
```
Type:       Command-line script (audio analysis)
Features:   - Analyze each track's tempo (BPM) and musical key
            - Write BPM and key into ID3/Vorbis tags
            - Skip tracks that already have both tags unless --force
            - Export a CSV of all tracks with BPM and key
Input:      Music folder, --force
Tech stack: Python, librosa, mutagen
```

---

## Example 233

**Intent:**
pdf to jpg every page

**Spec:**
```
Type:       Command-line tool (PDF to images)
Features:   - Render each PDF page to an image
            - Set resolution with --dpi
            - Choose JPEG or PNG output
            - Name images file_page001.jpg and so on
Input:      PDF path, --dpi, --format
Tech stack: Bash, pdftoppm (poppler-utils)
```

---

## Example 234

**Intent:**
pull out all the pictures that are inside a pdf

**Spec:**
```
Type:       Command-line tool (PDF image extraction)
Features:   - Extract embedded images from every page of a PDF
            - Save them in their original format when possible
            - Skip images smaller than a minimum width
            - Name files by page and image index
Input:      PDF path, output folder, --min-width
Tech stack: Python, PyMuPDF
```

---

## Example 235

**Intent:**
my scanner only does one side, so i scan all fronts then all backs reversed. i need them merged in the right order

**Spec:**
```
Type:       Command-line tool (PDF page interleave)
Features:   - Take a PDF of front pages and a PDF of back pages
            - Reverse the order of the back pages
            - Interleave pages as front 1, back 1, front 2, back 2
            - Check that both files have the same page count
            - Write the merged PDF
Input:      Fronts PDF, backs PDF, -o output
Tech stack: Python, pypdf
```

---

## Example 236

**Intent:**
from a big pdf, save only the pages that have a certain word

**Spec:**
```
Type:       Command-line tool (PDF page filter)
Features:   - Search the text of each page for a word or regex
            - Copy matching pages into a new PDF
            - Print the matching page numbers
            - Search case-insensitively with -i
Input:      PDF path, search term, -o output
Tech stack: Python, pdfplumber, pypdf
```

---

## Example 237

**Intent:**
Can you build me something that checks a contact list in Excel for bad emails and phone numbers before we import it into our CRM?

**Spec:**
```
Type:       Command-line tool (data validation)
Features:   - Read a contact list from Excel
            - Check email syntax and that the domain has MX records
            - Normalize phone numbers to E.164 format for a default country
            - Flag duplicates by email
            - Write a copy with a "problems" column and a clean file for import
Input:      Excel file, --country code
Tech stack: Python, pandas, email-validator, phonenumbers
```

---

## Example 238

**Intent:**
remove duplicate rows from a spreadsheet based on some columns

**Spec:**
```
Type:       Command-line tool (deduplication)
Features:   - Read CSV or Excel files
            - Remove rows that are duplicates on the columns given with --keys
            - Keep the first or last occurrence with --keep
            - Write removed rows to a separate file for review
Input:      File path, --keys, --keep
Tech stack: Python, pandas
```

---

## Example 239

**Intent:**
turn a list of addresses in excel into latitude and longitude

**Spec:**
```
Type:       Command-line script (geocoding)
Features:   - Read addresses from an Excel column
            - Geocode each address with the Nominatim API at 1 request per second
            - Cache results so repeated addresses are not looked up twice
            - Add lat and lon columns and save a new file
            - Mark addresses that could not be found
Input:      Excel file, --column
Tech stack: Python, geopy, pandas
```

---

## Example 240

**Intent:**
make certificates for all workshop attendees from a list

**Spec:**
```
Type:       Command-line script (certificate generator)
Features:   - Read attendee names and dates from a CSV
            - Place each name on a certificate background image or PDF template
            - Center the text and pick the font size to fit long names
            - Save one PDF per attendee
            - Optionally email each certificate to the attendee
Input:      Attendee CSV, template file, font file
Tech stack: Python, ReportLab, pypdf, smtplib
```

---

## Example 241

**Intent:**
low stock warning from our inventory google sheet

**Spec:**
```
Type:       Scheduled script (inventory alert)
Features:   - Read item, quantity and reorder level from the inventory sheet
            - Find items at or below the reorder level
            - Email the purchasing person a list with suggested order quantities
            - Send only once per item until it is restocked
            - Run every morning
Input:      Sheet ID, service account key, email settings
Tech stack: Python, gspread, smtplib, cron
```

---

## Example 242

**Intent:**
json to excel please, its an array of objects

**Spec:**
```
Type:       Command-line tool (format conversion)
Features:   - Read a JSON file containing an array of objects
            - Flatten nested objects into dotted column names
            - Write the rows to an .xlsx sheet with headers
            - Auto-size column widths
Input:      JSON file, -o output
Tech stack: Python, pandas (json_normalize), openpyxl
```

---

## Example 243

**Intent:**
yaml to json converter cli

**Spec:**
```
Type:       Command-line tool (format conversion)
Features:   - Convert YAML to JSON and JSON to YAML
            - Handle multi-document YAML files
            - Read from a file or stdin
            - Pretty-print output with --indent
Input:      File path or stdin, --to json or yaml
Tech stack: Go, gopkg.in/yaml.v3, cobra
```

---

## Example 244

**Intent:**
make a markdown table from csv

**Spec:**
```
Type:       Command-line tool (format conversion)
Features:   - Read a CSV file or stdin
            - Output a Markdown table with aligned columns
            - Set column alignment with --align
            - Escape pipe characters inside cells
Input:      CSV path or stdin
Tech stack: Node.js, csv-parse
```

---

## Example 245

**Intent:**
back up my laptop to a server with restic and keep it encrypted

**Spec:**
```
Type:       Scheduled script (encrypted backup)
Features:   - Run restic backup of the home folder to an SFTP repository
            - Exclude caches and large temporary folders
            - Apply a retention policy (7 daily, 4 weekly, 12 monthly) with forget --prune
            - Run a weekly restic check
            - Log results and notify on failure
Input:      Repository URL, password file, exclude file
Tech stack: Bash, restic, systemd timer
```

---

## Example 246

**Intent:**
save my home router config every week in case it resets

**Spec:**
```
Type:       Scheduled script (config backup)
Features:   - Log in to the router over SSH
            - Export the running configuration
            - Save it with the date in the file name
            - Keep only changes by comparing with the last saved version
            - Run weekly
Input:      Router address and SSH key
Tech stack: Python, Netmiko, git, cron
```

---

## Example 247

**Intent:**
export all my notion pages as markdown every week as backup

**Spec:**
```
Type:       Scheduled script (Notion backup)
Features:   - List all pages and databases shared with the integration through the Notion API
            - Convert page blocks to Markdown
            - Export databases to CSV
            - Save everything into a dated folder
            - Run weekly via cron
Input:      Notion integration token
Tech stack: Python, notion-client, cron
```

---

## Example 248

**Intent:**
clean old files in an s3 bucket

**Spec:**
```
Type:       Scheduled script (S3 cleanup)
Features:   - List objects under a prefix in an S3 bucket with pagination
            - Delete objects older than N days in batches of 1000
            - Skip objects with a "keep" tag
            - Print the count and total size deleted
            - Support --dry-run
Input:      Bucket, prefix, --days
Tech stack: Python, boto3, cron
```

---

## Example 249

**Intent:**
once a month try to restore our database backup to check it actually works

**Spec:**
```
Type:       Scheduled script (restore test)
Features:   - Download the latest database backup from S3
            - Restore it into a temporary PostgreSQL container
            - Run sanity queries (table counts, latest record date)
            - Report pass or fail by email
            - Remove the temporary container
Input:      Bucket name, sanity queries file, email settings
Tech stack: Bash, Docker, pg_restore, aws CLI, cron
```

---

## Example 250

**Intent:**
i have 3 phones worth of contacts exported as vcf and they overlap, merge them

**Spec:**
```
Type:       Command-line tool (contacts merge)
Features:   - Read contacts from several .vcf files
            - Match duplicates by normalized phone number or email
            - Merge fields from duplicates into one contact
            - Write a single cleaned .vcf file
            - Print how many duplicates were merged
Input:      VCF files, -o output
Tech stack: Python, vobject, phonenumbers
```

---

## Example 251

**Intent:**
forward emails from certain senders to my work email automatically

**Spec:**
```
Type:       Scheduled script (email forwarding)
Features:   - Check a mailbox over IMAP every 5 minutes
            - Match new emails against sender and subject rules from a config file
            - Forward matching emails with attachments through SMTP
            - Tag forwarded emails so they are not sent twice
Input:      Rules config, IMAP and SMTP settings in .env
Tech stack: Python, imapclient, smtplib, cron
```

---

## Example 252

**Intent:**
turn emails with a certain label into todoist tasks

**Spec:**
```
Type:       Scheduled script (email to tasks)
Features:   - Search Gmail for messages with a given label
            - Create a Todoist task with the email subject and a link to the message
            - Set a due date if the subject contains "by <date>"
            - Remove the label after the task is created
Input:      Gmail OAuth credentials, Todoist API token
Tech stack: Python, Gmail API, Todoist REST API, cron
```

---

## Example 253

**Intent:**
flight price tracker for a route and dates

**Spec:**
```
Type:       Scheduled script (flight price tracker)
Features:   - Query a flight search API for a route and travel dates twice a day
            - Save the lowest price found for each run
            - Email an alert when the price falls below a target or drops by more than 10%
            - Show the price history with a history subcommand
Input:      Origin, destination, dates, target price, API key
Tech stack: Python, Amadeus API, sqlite3, cron
```

---

## Example 254

**Intent:**
send me the top hacker news stories every morning

**Spec:**
```
Type:       Scheduled script (news digest)
Features:   - Fetch the top stories from the Hacker News API
            - Keep stories with a score above a threshold
            - Email a list with title, score, link and comments link
            - Run every morning at 07:00
Input:      Score threshold, email settings
Tech stack: Python, requests, smtplib, cron
```

---

## Example 255

**Intent:**
steam game sale alert

**Spec:**
```
Type:       Scheduled script (game price alert)
Features:   - Read a list of Steam app IDs from a file
            - Fetch current price and discount from the Steam store API
            - Send a Discord webhook message when a game is on sale above a minimum discount
            - Avoid repeating alerts for the same sale
Input:      App ID list, --min-discount, Discord webhook URL
Tech stack: Python, requests, cron
```

---

## Example 256

**Intent:**
pre commit hook to stop me committing files bigger than 5mb

**Spec:**
```
Type:       Command-line tool (git hook)
Features:   - Check the size of each staged file
            - Block the commit when a file exceeds the size limit
            - Print the large files and suggest Git LFS
            - Allow an override with an environment variable
Input:      Size limit in git config (hooks.maxfilesize)
Tech stack: Bash, git pre-commit hook
```

---

## Example 257

**Intent:**
find the biggest files ever committed in my git history

**Spec:**
```
Type:       Command-line tool (git helper)
Features:   - List every blob in the repository history with its size
            - Map each blob to its file path
            - Show the top N largest blobs with the commits that added them
            - Mark blobs that are no longer in the current tree
Input:      Repository path, --top N
Tech stack: Bash, git rev-list, git cat-file
```

---

## Example 258

**Intent:**
i use different emails for work and personal github, make git choose the right one per folder

**Spec:**
```
Type:       Command-line script (git configuration)
Features:   - Create separate git config files for work and personal identities
            - Add includeIf rules to ~/.gitconfig based on folder path
            - Set different SSH keys per identity with core.sshCommand
            - Show which identity is active in the current folder with a check command
Input:      Folder paths and identities asked interactively
Tech stack: Bash, git
```

---

## Example 259

**Intent:**
show git status of all repos in a folder at once

**Spec:**
```
Type:       Command-line tool (git helper)
Features:   - Find git repositories under a folder
            - Show for each one the branch, uncommitted changes and ahead/behind counts
            - Fetch remotes first with --fetch
            - Show only repositories that need attention with --dirty
Input:      Root folder, --fetch, --dirty
Tech stack: Go, os/exec, git
```

---

## Example 260

**Intent:**
keep my github forks up to date with upstream

**Spec:**
```
Type:       Scheduled script (fork sync)
Features:   - List my forked repositories through the GitHub API
            - Call the merge-upstream endpoint for the default branch of each fork
            - Report forks that could not be synced because of conflicts
            - Run weekly
Input:      GitHub token in environment variable
Tech stack: Python, requests, GitHub REST API, cron
```

---

## Example 261

**Intent:**
bump version number and create git tag

**Spec:**
```
Type:       Command-line tool (release helper)
Features:   - Read the current version from package.json or a VERSION file
            - Bump the major, minor or patch number
            - Commit the change and create an annotated tag v<version>
            - Refuse to run when the working tree is dirty
            - Push the commit and tag with --push
Input:      major, minor or patch, --push
Tech stack: Node.js, semver, simple-git
```

---

## Example 262

**Intent:**
which commit added this line of code

**Spec:**
```
Type:       Command-line tool (git search)
Features:   - Search history for commits that added or removed a string with git log -S
            - Show commit hash, author, date and message
            - Limit the search to a path
            - Show the diff for a chosen commit with --show
Input:      Search string, --path, --show
Tech stack: Bash, git
```

---

## Example 263

**Intent:**
monitor raspberry pi temperature and throttle

**Spec:**
```
Type:       Scheduled script (Pi monitoring)
Features:   - Read the CPU temperature with vcgencmd every minute
            - Read throttling flags
            - Log values to a CSV
            - Send a notification when the temperature is above 75°C
Input:      Threshold, ntfy topic
Tech stack: Bash, vcgencmd, curl (ntfy), cron
```

---

## Example 264

**Intent:**
remove old linux kernels to free up boot partition

**Spec:**
```
Type:       Command-line script (system cleanup)
Features:   - List installed kernel packages
            - Keep the running kernel and the newest one
            - Remove the older kernels with the package manager
            - Show /boot free space before and after
Tech stack: Bash, apt, dpkg
```

---

## Example 265

**Intent:**
limit the size of the systemd journal and clean it weekly

**Spec:**
```
Type:       Scheduled script (log cleanup)
Features:   - Show current journal disk usage
            - Vacuum journal files to a maximum size and age
            - Set SystemMaxUse in journald.conf if it is not set
            - Run weekly with a systemd timer
Input:      Max size and max age settings
Tech stack: Bash, journalctl, systemd timer
```

---

## Example 266

**Intent:**
windows script to clear the stuck print queue

**Spec:**
```
Type:       Command-line script (Windows maintenance)
Features:   - Stop the Print Spooler service
            - Delete files in the spool PRINTERS folder
            - Start the spooler again
            - Show the printer status after restart
            - Require administrator rights and warn when missing
Tech stack: PowerShell
```

---

## Example 267

**Intent:**
list everything that starts when windows boots

**Spec:**
```
Type:       Command-line tool (startup audit)
Features:   - Read startup entries from Run registry keys for user and machine
            - Read Startup folders and scheduled tasks with logon triggers
            - Show name, command and source
            - Export to CSV
Tech stack: PowerShell, Get-CimInstance, Get-ScheduledTask
```

---

## Example 268

**Intent:**
save a full offline copy of my old blog before the host shuts down

**Spec:**
```
Type:       Command-line script (website archiving)
Features:   - Mirror the site recursively with all pages, images, CSS and JS
            - Convert links to work offline
            - Stay within the blog domain
            - Wait between requests to be polite
            - Pack the mirror into a zip file at the end
Input:      Blog URL, output folder
Tech stack: Bash, wget (--mirror --convert-links --page-requisites)
```

---

## Example 269

**Intent:**
submit a list of urls to the wayback machine

**Spec:**
```
Type:       Command-line tool (web archiving)
Features:   - Read URLs from a file
            - Submit each URL to the Wayback Machine Save Page Now API
            - Wait between requests to respect rate limits
            - Record the archived snapshot URL for each submission in a CSV
Input:      URL list file, API keys for archive.org
Tech stack: Python, requests
```

---

## Example 270

**Intent:**
turn our slack export into readable html pages

**Spec:**
```
Type:       Command-line tool (chat archive converter)
Features:   - Read the Slack export ZIP
            - Build one HTML page per channel per month
            - Show user names and avatars instead of user IDs
            - Render threads, links and file attachments
            - Create an index page listing channels
Input:      Slack export ZIP, output folder
Tech stack: Python, Jinja2, zipfile
```

---

## Example 271

**Intent:**
terminal 2fa codes like google authenticator

**Spec:**
```
Type:       Command-line tool (TOTP generator)
Features:   - Store TOTP secrets in an encrypted file
            - Add accounts from a secret key or otpauth:// URI
            - Show the current 6-digit code and seconds left for an account
            - Copy the code to the clipboard
Input:      add, list or code subcommands
Tech stack: Go, pquerna/otp, filippo.io/age
```

---

## Example 272

**Intent:**
check how strong a password is

**Spec:**
```
Type:       Command-line tool (password strength)
Features:   - Estimate password strength with a score from 0 to 4
            - Show the estimated crack time
            - Give suggestions to improve it
            - Read the password from a hidden prompt
Tech stack: Python, zxcvbn, getpass
```

---

## Example 273

**Intent:**
make an ssh key and put it on all my servers

**Spec:**
```
Type:       Command-line script (SSH key setup)
Features:   - Generate an ed25519 key pair if none exists
            - Read a list of servers from a file
            - Copy the public key to each server with ssh-copy-id
            - Test key login on each server and report failures
Input:      Servers file (user@host per line)
Tech stack: Bash, ssh-keygen, ssh-copy-id
```

---

## Example 274

**Intent:**
encrypt a folder before uploading it to dropbox

**Spec:**
```
Type:       Command-line tool (folder encryption)
Features:   - Pack a folder into a tar archive
            - Encrypt it with GPG symmetric AES-256 using a passphrase
            - Write the encrypted file to the Dropbox folder
            - Decrypt and unpack with a restore subcommand
Input:      Folder path, Dropbox folder path
Tech stack: Bash, tar, gpg
```

---

## Example 275

**Intent:**
slugify a list of titles

**Spec:**
```
Type:       Command-line tool (text processing)
Features:   - Convert each input line to a URL slug
            - Transliterate accented and non-Latin characters to ASCII
            - Replace spaces and symbols with hyphens and lowercase the result
            - Set a maximum length with --max
Input:      Lines from a file or stdin
Tech stack: Python, python-slugify
```

---

## Example 276

**Intent:**
strip html tags from text files and keep only the text

**Spec:**
```
Type:       Command-line tool (text extraction)
Features:   - Read HTML files or stdin
            - Remove scripts, styles and tags
            - Keep paragraph breaks and decode HTML entities
            - Write plain text output
Input:      HTML files or stdin
Tech stack: Python, BeautifulSoup
```

---

## Example 277

**Intent:**
spell check all my markdown blog posts b4 publishing

**Spec:**
```
Type:       Command-line tool (spell checker)
Features:   - Check spelling in .md files, skipping code blocks and URLs
            - Use a custom word list for names and technical terms
            - Print each misspelling with file, line and suggestions
            - Exit non-zero when errors are found
Input:      File glob, --dict custom word list
Tech stack: Node.js, cspell
```

---

## Example 278

**Intent:**
Good morning. In our office we have a shared folder where people put scanned documents. I need that every evening the program makes OCR on new scans and puts them into folder of the right customer, the customer number is written on the document.

**Spec:**
```
Type:       Scheduled script (document sorting)
Features:   - Find scans added to the shared folder since the last run
            - Run OCR on each scan
            - Find the customer number with a regex pattern
            - Move the searchable PDF to the customer's folder, creating it when needed
            - Put scans without a customer number into a "review" folder
Input:      Shared folder path, customers root folder, number pattern
Tech stack: Python, OCRmyPDF, re, Windows Task Scheduler
```

---

## Example 279

**Intent:**
yo need a script that makes my pc shut down at 1am if im not doing anything

**Spec:**
```
Type:       Scheduled script (idle shutdown)
Features:   - Check at 01:00 how long the user has been idle
            - Shut down if idle for more than 20 minutes
            - Show a 60-second warning that can cancel the shutdown
            - Skip shutdown when a download or game process is running
Input:      Idle limit and process whitelist in the script
Tech stack: PowerShell, Windows Task Scheduler
```

---

## Example 280

**Intent:**
so at work every month i get a zip from our payroll provider with like 100 pdf payslips, one per employee, all named by employee number, and i have to email each person their own payslip. it takes me half a day. there must be a better way right

**Spec:**
```
Type:       Command-line script (payslip mailing)
Features:   - Extract the payslip ZIP into a temporary folder
            - Match each PDF's employee number to an email address from an employee CSV
            - Email each employee only their own payslip with a standard message
            - Encrypt each PDF with the employee's birth date as password with --encrypt
            - Write a log of sent emails and payslips with no matching employee
Input:      Payslip ZIP, employee CSV, SMTP settings in .env
Tech stack: Python, zipfile, pandas, pypdf, smtplib
```

---

## Example 281

**Intent:**
watch my clipboard and save everything i copy to a history file

**Spec:**
```
Type:       Command-line tool (clipboard history)
Features:   - Poll the clipboard every second for new text
            - Append new entries with a timestamp to a history file
            - Ignore entries that look like passwords or are longer than a limit
            - Search history with a search subcommand
            - Restore an entry to the clipboard by number
Tech stack: Python, pyperclip, sqlite3
```

---

## Example 282

**Intent:**
bash on mac, find every file i downloaded more than 6 months ago and move to an "old stuff" folder

**Spec:**
```
Type:       Command-line script (file cleanup)
Features:   - Find files in ~/Downloads not modified for 180 days
            - Move them into ~/Downloads/old stuff, keeping subfolders
            - Skip files that are still open
            - Print a count of moved files and their total size
Input:      Days threshold (default 180)
Tech stack: Bash, find, lsof
```

---

## Example 283

**Intent:**
plz i need csv of all files in folder with size and date for my manager

**Spec:**
```
Type:       Command-line script (file inventory)
Features:   - List all files in a folder and its subfolders
            - Record path, name, extension, size in MB and last modified date
            - Write the list to CSV with a header row
            - Sort by folder then name
Input:      Folder path, output CSV path
Tech stack: Python, os.walk, csv
```

---

## Example 284

**Intent:**
I am not programmer. We have 20 computers in school, I want once a week a list which ones have low disk or are not updated.

**Spec:**
```
Type:       Scheduled script (computer inventory report)
Features:   - Connect to each school computer in a list through PowerShell remoting
            - Collect free disk space, last Windows Update install date and uptime
            - Mark computers with less than 10% free disk or no updates in 30 days
            - Save an Excel report and email it every Monday
Input:      Computer name list, email settings
Tech stack: PowerShell, Invoke-Command, ImportExcel module, Windows Task Scheduler
```

---

## Example 285

**Intent:**
rename tv episode files to Show - S01E02 format

**Spec:**
```
Type:       Command-line tool (media renaming)
Features:   - Parse season and episode numbers from messy file names (s1e2, 1x02, S01.E02)
            - Look up the episode title from the TVmaze API
            - Rename to "Show - S01E02 - Title.ext"
            - Rename matching subtitle files too
            - Preview with --dry-run
Input:      Folder path, show name
Tech stack: Python, requests, TVmaze API, re
```

---

## Example 286

**Intent:**
i want a little script where i type the name of a city and it shows the time there

**Spec:**
```
Type:       Command-line tool (world clock)
Features:   - Look up a city's time zone from a built-in city list
            - Show the current local time and UTC offset
            - Show several cities at once
            - Convert a given time from one city to another with --at
Input:      City names as arguments
Tech stack: Python, zoneinfo, geonamescache
```

---

## Example 287

**Intent:**
need daily csv dump of a mongodb collection for the analytics people

**Spec:**
```
Type:       Scheduled script (data export)
Features:   - Query documents from a MongoDB collection updated in the last 24 hours
            - Flatten selected fields into columns
            - Write a dated CSV file
            - Upload it to a shared SFTP folder
            - Run daily at 01:00
Input:      Mongo URI, collection, field list, SFTP settings
Tech stack: Python, pymongo, pandas, paramiko, cron
```

---

## Example 288

**Intent:**
make a shell script that tells me which docker containers restarted a lot

**Spec:**
```
Type:       Command-line tool (container check)
Features:   - List all containers with their restart count and status
            - Show containers with restarts above a threshold
            - Print the last 30 log lines of each unstable container
            - Output as a table
Input:      --min-restarts
Tech stack: Bash, Docker CLI (docker inspect, docker logs)
```

---

## Example 289

**Intent:**
im writing a novel in many txt chapter files and want them joined into one epub

**Spec:**
```
Type:       Command-line tool (ebook builder)
Features:   - Read chapter text files sorted by number
            - Turn each file into an EPUB chapter titled from its first line
            - Add title, author and cover image metadata
            - Generate the table of contents
            - Write a valid .epub file
Input:      Chapter folder, --title, --author, --cover
Tech stack: Python, ebooklib
```

---

## Example 290

**Intent:**
delete thumbs.db and .DS_Store junk from all folders

**Spec:**
```
Type:       Command-line script (file cleanup)
Features:   - Find Thumbs.db, desktop.ini, .DS_Store and ._* files recursively
            - Show the list and total count
            - Delete them after confirmation
            - Skip folders matching an exclude pattern
Input:      Root folder
Tech stack: Bash, find
```

---

## Example 291

**Intent:**
hey can u make python thing that counts how many times each ip appears in apache error log and also what errors

**Spec:**
```
Type:       Command-line tool (log analysis)
Features:   - Parse Apache error log lines into time, level, client IP and message
            - Count entries per client IP
            - Group messages by error type, removing numbers and paths
            - Print the top IPs and top error types
Input:      Error log path, --top N
Tech stack: Python, re, collections.Counter
```

---

## Example 292

**Intent:**
rename photos with the city where they were taken

**Spec:**
```
Type:       Command-line script (photo renaming)
Features:   - Read GPS coordinates from each photo's EXIF
            - Find the city name by reverse geocoding
            - Rename files to YYYY-MM-DD_City_001.jpg
            - Cache coordinates so nearby photos reuse the lookup
            - Leave photos without GPS unchanged
Input:      Photo folder
Tech stack: Python, Pillow, geopy (Nominatim)
```

---

## Example 293

**Intent:**
Hello, I need help. Every week our supplier send excel price list. I need to compare with last week and see which prices go up.

**Spec:**
```
Type:       Command-line script (price list comparison)
Features:   - Read this week's and last week's supplier Excel files
            - Match products by item code
            - Calculate price change in amount and percent
            - List products whose price went up, sorted by percent
            - Save a report Excel with increases highlighted in red
Input:      Old price list, new price list
Tech stack: Python, pandas, openpyxl
```

---

## Example 294

**Intent:**
script that empties the trash folder and recycle bin of files older than a month

**Spec:**
```
Type:       Scheduled script (trash cleanup)
Features:   - Find items in the user's trash older than 30 days by deletion date
            - Delete them permanently
            - Report the space freed
            - Run weekly
Tech stack: Bash, trash-cli (trash-empty), cron
```

---

## Example 295

**Intent:**
generate a gitignore for python and node

**Spec:**
```
Type:       Command-line tool (gitignore generator)
Features:   - Download templates for chosen languages and tools from the gitignore.io API
            - Merge them into one .gitignore without duplicate lines
            - Append to an existing .gitignore instead of replacing it
            - List available templates with --list
Input:      Template names as arguments
Tech stack: Bash, curl
```

---

## Example 296

**Intent:**
ping me when a youtube channel i follow uploads

**Spec:**
```
Type:       Scheduled script (upload notifier)
Features:   - Read YouTube channel IDs from a file
            - Fetch each channel's RSS feed every 15 minutes
            - Detect videos not seen before
            - Send a Pushover notification with title and link
Input:      Channel ID list, Pushover keys
Tech stack: Python, feedparser, requests, cron
```

---

## Example 297

**Intent:**
python tool to check if a list of websites use https and redirect http properly

**Spec:**
```
Type:       Command-line tool (HTTPS checker)
Features:   - Request the http:// version of each domain without following redirects
            - Check that it redirects to https:// with a 301
            - Check that the https version loads with a valid certificate
            - Check for the Strict-Transport-Security header
            - Print a pass/fail table
Input:      Domains file
Tech stack: Python, requests, ssl
```

---

## Example 298

**Intent:**
weekly email report of failed windows logins on our server

**Spec:**
```
Type:       Scheduled script (security report)
Features:   - Read Security event log entries with ID 4625 from the last 7 days
            - Group failures by account name and source IP
            - Highlight accounts with more than 20 failures
            - Email an HTML table to the admin
            - Run every Monday with Task Scheduler
Input:      SMTP settings
Tech stack: PowerShell, Get-WinEvent, Send-MailMessage
```

---

## Example 299

**Intent:**
compress old logs into monthly zip files

**Spec:**
```
Type:       Command-line script (log archiving)
Features:   - Group .log files by month from their modification date
            - Create one zip archive per month
            - Verify each archive and then delete the original logs
            - Skip the current month
Input:      Log folder
Tech stack: Python, zipfile, pathlib
```

---

## Example 300

**Intent:**
i got 10k images from a scraper and a lot are tiny icons or broken, clean them up

**Spec:**
```
Type:       Command-line script (image cleanup)
Features:   - Try to open each image and move broken files to a "broken" folder
            - Move images below a minimum width or height to a "small" folder
            - Find exact duplicates by hash and keep one copy
            - Print counts for each category
Input:      Image folder, --min-size pixels
Tech stack: Python, Pillow, hashlib
```

---

## Example 301

**Intent:**
a cron that pulls new rows from an api into a google sheet every hour

**Spec:**
```
Type:       Scheduled script (sheet sync)
Features:   - Call the API for records created since the last sync
            - Map JSON fields to sheet columns
            - Append new rows to the Google Sheet in one batch
            - Save the last synced record ID
            - Run hourly
Input:      API URL and key, sheet ID, service account key
Tech stack: Python, requests, gspread, cron
```

---

## Example 302

**Intent:**
make a node script that resizes product images to 3 sizes for my shop

**Spec:**
```
Type:       Command-line tool (image variants)
Features:   - Read product images from an input folder
            - Create small (300 px), medium (800 px) and large (1600 px) versions
            - Output both JPEG and WebP for each size
            - Name files product_small.jpg, product_small.webp and so on
            - Skip images that are already processed
Input:      Input folder, output folder
Tech stack: Node.js, sharp
```

---

## Example 303

**Intent:**
kill zombie processes

**Spec:**
```
Type:       Command-line script (process cleanup)
Features:   - List processes in zombie (Z) state with their parent PIDs
            - Send SIGCHLD to the parent so it can reap them
            - Offer to kill the parent process if zombies remain
            - Log actions taken
Tech stack: Bash, ps, kill
```

---

## Example 304

**Intent:**
I'm a researcher and I download a lot of papers as PDFs with names like 2103.04512.pdf. I'd love a tool that renames them to "Author Year - Title.pdf" so I can actually find stuff.

**Spec:**
```
Type:       Command-line tool (paper renaming)
Features:   - Detect arXiv IDs or DOIs in the file name or first page
            - Fetch title, first author and year from the arXiv API or Crossref
            - Rename the file to "Author Year - Title.pdf" with unsafe characters removed
            - Write a BibTeX entry for each paper to a .bib file
            - Leave files that cannot be identified unchanged
Input:      Papers folder
Tech stack: Python, requests, arxiv API, Crossref API, pdfplumber
```

---

## Example 305

**Intent:**
clean up my desktop every friday into a folder named with the date

**Spec:**
```
Type:       Scheduled script (desktop cleanup)
Features:   - Move all files from the Desktop into Desktop Archive/YYYY-MM-DD
            - Leave shortcuts and a list of pinned files in place
            - Skip if the Desktop is already empty
            - Run every Friday at 17:00
Input:      Pinned file list
Tech stack: PowerShell, Windows Task Scheduler
```

---

## Example 306

**Intent:**
extract phone numbers from a bunch of word docs

**Spec:**
```
Type:       Command-line tool (data extraction)
Features:   - Read text from all .docx files in a folder, including tables
            - Find phone numbers in common formats
            - Normalize them to international format
            - Write a CSV with number and source file
            - Remove duplicates
Input:      Folder path, --country
Tech stack: Python, python-docx, phonenumbers
```

---

## Example 307

**Intent:**
script for my teacher website that downloads the daily cafeteria menu pdf and posts the text

**Spec:**
```
Type:       Scheduled script (menu fetcher)
Features:   - Download the daily menu PDF from the district website
            - Extract the text for today's date
            - Save it as a small HTML snippet for the class website
            - Run on school days at 06:00
Input:      Menu page URL, output path
Tech stack: Python, requests, pdfplumber, cron
```

---

## Example 308

**Intent:**
check which python packages in requirements have security problems

**Spec:**
```
Type:       Command-line tool (dependency audit)
Features:   - Read requirements.txt or a lock file
            - Check each pinned package version against a vulnerability database
            - Show vulnerability ID, severity and fixed version
            - Exit non-zero when vulnerabilities are found
Input:      Requirements file path
Tech stack: Python, pip-audit
```

---

## Example 309

**Intent:**
compare 2 folders of photos and copy the ones missing in the backup

**Spec:**
```
Type:       Command-line script (backup catch-up)
Features:   - Hash files in the source and backup folders
            - Find source files whose hash is not in the backup
            - Copy missing files keeping their relative paths
            - Show the count and size of copied files
Input:      Source folder, backup folder
Tech stack: Python, hashlib, shutil
```

---

## Example 310

**Intent:**
convert all the tabs to spaces in my code

**Spec:**
```
Type:       Command-line tool (whitespace fixer)
Features:   - Replace leading tabs with a set number of spaces
            - Optionally remove trailing whitespace with --trim
            - Process files by extension
            - Report files changed
Input:      Folder, --spaces N, --ext list
Tech stack: Python, pathlib
```

---

## Example 311

**Intent:**
i run a small online course, want a script that every sunday pulls new students from stripe and adds them to my mailchimp list

**Spec:**
```
Type:       Scheduled script (customer sync)
Features:   - List Stripe charges or checkout sessions from the last 7 days
            - Get each customer's email and name
            - Add or update each contact in a Mailchimp audience with a "student" tag
            - Skip refunded payments
            - Log added contacts
Input:      Stripe secret key, Mailchimp API key and audience ID
Tech stack: Python, stripe, mailchimp-marketing, cron
```

---

## Example 312

**Intent:**
merge all txt files in a folder into one with file names as headers

**Spec:**
```
Type:       Command-line tool (file concatenation)
Features:   - Read all .txt files in a folder sorted by name
            - Write them into one output file
            - Put a header line with the file name before each file's content
            - Add a blank line between files
Input:      Folder path, -o output
Tech stack: Bash, for loop, cat
```

---

## Example 313

**Intent:**
get alerts when my AWS bill goes above a limit this month

**Spec:**
```
Type:       Scheduled script (cost alert)
Features:   - Query AWS Cost Explorer for month-to-date cost every day
            - Compare with the monthly budget
            - Forecast the end-of-month cost
            - Send a Slack message when the cost or forecast passes the budget
Input:      Budget amount, Slack webhook URL
Tech stack: Python, boto3 (Cost Explorer), requests, cron
```

---

## Example 314

**Intent:**
script that warns before my dropbox runs out of space

**Spec:**
```
Type:       Scheduled script (storage quota alert)
Features:   - Query used and total space from the Dropbox API
            - Calculate the percentage used
            - Send an email when usage passes 90%
            - List the 20 largest files to help clean up
Input:      Dropbox access token, email settings
Tech stack: Python, dropbox SDK, smtplib, cron
```

---

## Example 315

**Intent:**
anonymize names in interview transcripts for my thesis

**Spec:**
```
Type:       Command-line tool (text anonymization)
Features:   - Detect person names in text files with named entity recognition
            - Replace each name with a consistent pseudonym (Participant A, B)
            - Also replace names from a custom list
            - Save a private key file mapping names to pseudonyms
Input:      Transcript folder, custom names list
Tech stack: Python, spaCy
```

---

## Example 316

**Intent:**
download stock price history for a list of tickers to excel

**Spec:**
```
Type:       Command-line tool (market data download)
Features:   - Read tickers from arguments or a file
            - Download daily open, high, low, close and volume for a date range
            - Write one sheet per ticker in an Excel workbook
            - Add a summary sheet with return over the period
Input:      Tickers, --start, --end, -o output
Tech stack: Python, yfinance, pandas, openpyxl
```

---

## Example 317

**Intent:**
windows: map network drives at login based on the user's group

**Spec:**
```
Type:       Scheduled script (logon script)
Features:   - Read group memberships of the current user
            - Map network drives for each group from a mapping file
            - Remove old mappings first
            - Log errors to a file in the user's profile
Input:      Group to drive mapping file (CSV)
Tech stack: PowerShell, Group Policy logon script
```

---

## Example 318

**Intent:**
wordle-style word finder from a word list

**Spec:**
```
Type:       Command-line tool (word search)
Features:   - Filter a word list by length and known letter positions
            - Exclude letters that are not in the word
            - Require letters that are in the word but in a different position
            - Print matching words sorted by letter frequency
Input:      Pattern like "a__le", --has, --not
Tech stack: Python, argparse
```

---

## Example 319

**Intent:**
convert my old video tapes digitized avi files to mp4 and deinterlace

**Spec:**
```
Type:       Command-line script (video conversion)
Features:   - Find .avi files in a folder
            - Deinterlace with the yadif filter
            - Encode to H.264 MP4 with AAC audio
            - Keep the original aspect ratio
            - Show progress for each file
Input:      Folder path, --crf
Tech stack: Bash, ffmpeg
```

---

## Example 320

**Intent:**
my dad has 40 years of family photos scanned as huge tiff files on an old disk, theyre eating all the space, i want to make jpg copies for sharing but keep the tiffs on another drive just in case, and keep the same folders

**Spec:**
```
Type:       Command-line script (photo archive conversion)
Features:   - Walk the TIFF archive folder recursively
            - Convert each TIFF to a high-quality JPEG in a mirror folder structure
            - Copy the original TIFFs to the archive drive and verify by checksum
            - Delete originals from the old disk only with --free-space after verification
            - Write a CSV log of every file processed
Input:      Source folder, JPEG output folder, archive drive path
Tech stack: Python, Pillow, hashlib, shutil
```

---

## Example 321

**Intent:**
wanna add all my receipts amounts from pdfs into a total

**Spec:**
```
Type:       Command-line script (receipt totals)
Features:   - Extract text from receipt PDFs in a folder
            - Find the total amount near words like "Total" or "Summe"
            - Sum amounts per month based on the receipt date
            - Export a CSV of file, date and amount
            - Flag receipts where no total was found
Input:      Folder of receipt PDFs
Tech stack: Python, pdfplumber, re, pandas
```

---

## Example 322

**Intent:**
Please, I want a program which reads all CSV in folder and makes one chart per file, our machines write sensor data every day.

**Spec:**
```
Type:       Data analysis script (sensor charts)
Features:   - Read each sensor CSV with timestamp and value columns
            - Draw a line chart of the values over time
            - Mark values outside the allowed range in red
            - Save one PNG chart per file with the same name
            - Create an index HTML page showing all charts
Input:      Folder of CSV files, min and max allowed values
Tech stack: Python, pandas, matplotlib
```

---

## Example 323

**Intent:**
list the git repos on my machine that have unpushed commits before i wipe it

**Spec:**
```
Type:       Command-line tool (git helper)
Features:   - Search the home folder for .git directories
            - For each repository, list branches with commits not on their upstream
            - List branches with no upstream at all
            - Report repositories with uncommitted or stashed changes
            - Print a final list of repositories that are not safe to delete
Input:      Root folder (defaults to home)
Tech stack: Bash, git, find
```

---

## Example 324

**Intent:**
script to put all photos from the same day into one folder

**Spec:**
```
Type:       Command-line script (photo organizer)
Features:   - Read the date taken from EXIF, falling back to file modification date
            - Create a folder per day named YYYY-MM-DD
            - Move photos and videos into their day folder
            - Handle name clashes with a counter
Input:      Photo folder
Tech stack: Bash, ExifTool
```

---

## Example 325

**Intent:**
convert powerpoints to pdf in bulk on windows

**Spec:**
```
Type:       Command-line script (format conversion)
Features:   - Find .ppt and .pptx files in a folder
            - Open each one in PowerPoint through COM automation
            - Save it as PDF next to the original
            - Close PowerPoint when finished, even after errors
Input:      Folder path
Tech stack: PowerShell, PowerPoint COM automation
```

---

## Example 326

**Intent:**
tell me if any of my servers' load goes crazy

**Spec:**
```
Type:       Scheduled script (load monitor)
Features:   - Read the 5-minute load average on each server over SSH
            - Compare load to the number of CPU cores
            - Send a Slack alert when load stays above 2x the core count for 3 checks
            - Include the top 5 processes by CPU in the alert
Input:      Server list, Slack webhook URL
Tech stack: Python, Paramiko, requests, cron
```

---

## Example 327

**Intent:**
tool to make a quick backup copy of a file with timestamp before i edit it

**Spec:**
```
Type:       Command-line tool (file snapshot)
Features:   - Copy a file to file.YYYYMMDD-HHMMSS.bak in the same folder
            - Or to a central backup folder with --dir
            - List previous backups of a file with --list
            - Restore a chosen backup with --restore
Input:      File path
Tech stack: Bash
```

---

## Example 328

**Intent:**
need the text from a bunch of images (screenshots) into a txt file

**Spec:**
```
Type:       Command-line tool (OCR)
Features:   - Run OCR on PNG and JPG images in a folder
            - Pre-process images (grayscale, upscale) for better accuracy
            - Write the text of each image to a .txt with the same name
            - Also write one combined file with headers
Input:      Image folder, --lang
Tech stack: Python, pytesseract, Pillow
```

---

## Example 329

**Intent:**
send me a text when its going to rain tomorrow

**Spec:**
```
Type:       Scheduled script (weather alert)
Features:   - Fetch tomorrow's forecast for my location every evening
            - Check the probability of rain against a threshold
            - Send an SMS with the expected rain hours when above the threshold
            - Do nothing on dry days
Input:      Coordinates, threshold, phone number, Twilio credentials
Tech stack: Python, Open-Meteo API, Twilio API, cron
```

---

## Example 330

**Intent:**
i have a csv of products with prices in euros, add a column in dollars using todays rate

**Spec:**
```
Type:       Command-line tool (currency conversion)
Features:   - Fetch today's exchange rate from a public rates API
            - Read the price column of a CSV
            - Add a converted price column rounded to 2 decimals
            - Allow any currency pair with --from and --to
            - Write the updated CSV
Input:      CSV path, --column, --from, --to
Tech stack: Python, requests, pandas
```

---

## Example 331

**Intent:**
Can you make a script for our helpdesk that checks every morning which user passwords in AD will expire in the next 7 days and emails those users a reminder?

**Spec:**
```
Type:       Scheduled script (password expiry reminder)
Features:   - Query enabled AD users with expiring passwords
            - Calculate each user's expiry date from the domain password policy
            - Email users whose password expires within 7 days
            - Send the helpdesk a summary list
            - Run every morning with Task Scheduler
Input:      Days ahead, SMTP settings, email template
Tech stack: PowerShell, ActiveDirectory module, Send-MailMessage
```

---

## Example 332

**Intent:**
clean html exported from word, its full of junk styles

**Spec:**
```
Type:       Command-line tool (HTML cleanup)
Features:   - Remove Word-specific tags, classes and inline styles
            - Remove empty spans and paragraphs
            - Keep headings, lists, links, tables and bold/italic
            - Pretty-print the cleaned HTML
Input:      HTML file, -o output
Tech stack: Python, BeautifulSoup, bleach
```

---

## Example 333

**Intent:**
lowercase all file extensions

**Spec:**
```
Type:       Command-line script (file renaming)
Features:   - Find files with uppercase extensions (.JPG, .PDF)
            - Rename the extension to lowercase
            - Handle case-insensitive file systems by renaming through a temporary name
            - Work recursively with -r
Input:      Folder path
Tech stack: Bash, find, mv
```

---

## Example 334

**Intent:**
hourly job to pull new orders from woocommerce and print shipping labels

**Spec:**
```
Type:       Scheduled script (order processing)
Features:   - Fetch orders with status "processing" from the WooCommerce REST API
            - Create a shipping label PDF for each order with address and order number
            - Send each label to the default printer
            - Add a note to the order that the label was printed
            - Skip orders already printed
Input:      Store URL, API keys, printer name
Tech stack: Python, woocommerce, ReportLab, CUPS (lp), cron
```

---

## Example 335

**Intent:**
script that makes daily zip of my obsidian vault and keeps 30 days

**Spec:**
```
Type:       Scheduled script (notes backup)
Features:   - Zip the vault folder excluding the .obsidian/cache folder
            - Name the zip with the date
            - Save it to a cloud-synced folder
            - Delete zips older than 30 days
Input:      Vault path, backup folder
Tech stack: Python, zipfile, cron
```

---

## Example 336

**Intent:**
hi i would like tool that make all my pdf in black white for cheap printing

**Spec:**
```
Type:       Command-line tool (PDF grayscale)
Features:   - Convert color PDFs to grayscale
            - Process one file or a folder
            - Keep text as vector text, not images
            - Save results with a _bw suffix
Input:      PDF file or folder
Tech stack: Bash, Ghostscript
```

---

## Example 337

**Intent:**
show me which files in a folder were changed today

**Spec:**
```
Type:       Command-line tool (recent files)
Features:   - List files modified since midnight or in the last N hours
            - Show modification time and size
            - Sort by newest first
            - Search recursively and filter by extension
Input:      Folder path, --hours, --ext
Tech stack: Bash, find -newermt
```

---

## Example 338

**Intent:**
I want to auto-categorize my old emails into folders by sender domain, my inbox has 40k messages and it's chaos.

**Spec:**
```
Type:       Command-line script (mailbox organizer)
Features:   - Read message headers from the inbox over IMAP in batches
            - Group messages by sender domain
            - Create a folder per domain with more than N messages
            - Move messages into their domain folder with server-side MOVE
            - Save progress so the script can be resumed
Input:      IMAP settings, --min-messages
Tech stack: Python, imapclient
```

---

## Example 339

**Intent:**
monitor a csv file that keeps getting appended and alert on bad values

**Spec:**
```
Type:       Command-line tool (data stream monitor)
Features:   - Follow a CSV file as new rows are appended
            - Check each value against min and max rules per column
            - Print and log rule violations with the row number
            - Send a webhook alert for critical violations
Input:      CSV path, rules file (YAML), webhook URL
Tech stack: Python, PyYAML, requests
```

---

## Example 340

**Intent:**
rename my downloaded bank pdfs from random numbers to Bank_YYYY-MM

**Spec:**
```
Type:       Command-line script (statement renaming)
Features:   - Read the statement period from the first page of each PDF
            - Detect the bank name from known text patterns
            - Rename the file to Bank_YYYY-MM.pdf
            - Skip files that do not match any known bank
Input:      Folder of PDFs, patterns file
Tech stack: Python, pdfplumber
```

---

## Example 341

**Intent:**
ps script to check if windows defender is on and updated on all pcs

**Spec:**
```
Type:       Command-line script (security check)
Features:   - Connect to each computer in a list with PowerShell remoting
            - Read Defender real-time protection status and signature age
            - Mark computers with protection off or signatures older than 3 days
            - Export the results to CSV
Input:      Computer list file
Tech stack: PowerShell, Get-MpComputerStatus, Invoke-Command
```

---

## Example 342

**Intent:**
replace a word in a bunch of word docx files

**Spec:**
```
Type:       Command-line tool (document find and replace)
Features:   - Open every .docx in a folder
            - Replace a word or phrase in paragraphs, tables, headers and footers
            - Keep the original formatting of each run where possible
            - Save changed files to an output folder
            - Report replacements per file
Input:      Folder, --find, --replace
Tech stack: Python, python-docx
```

---

## Example 343

**Intent:**
daily summary of my fitness tracker csv export

**Spec:**
```
Type:       Data analysis script (fitness summary)
Features:   - Read the exported activity CSV
            - Calculate daily steps, distance and active minutes
            - Compare each day with the 7-day average
            - Print a short summary and save a weekly chart as PNG
Input:      Export CSV path
Tech stack: Python, pandas, matplotlib
```

---

## Example 344

**Intent:**
auto delete docker images older than 2 weeks on build server

**Spec:**
```
Type:       Scheduled script (build server cleanup)
Features:   - List images with their creation dates
            - Delete images older than 14 days that no container uses
            - Keep images with tags matching protected patterns (latest, release-*)
            - Log reclaimed disk space
            - Run nightly
Input:      Retention days, protected tag patterns
Tech stack: Bash, Docker CLI, cron
```

---

## Example 345

**Intent:**
Make me a CLI that checks my markdown files for broken internal links between notes, like [[note name]] wiki links

**Spec:**
```
Type:       Command-line tool (wiki link checker)
Features:   - Scan Markdown files for [[wiki links]] and relative Markdown links
            - Check that the linked note or file exists
            - Report broken links with file and line
            - List orphan notes that nothing links to with --orphans
Input:      Notes folder
Tech stack: Python, re, pathlib
```

---

## Example 346

**Intent:**
i need to resize a lot of photos so they are under 1mb for an upload form

**Spec:**
```
Type:       Command-line script (image size limit)
Features:   - Check each image's file size
            - Lower the JPEG quality step by step until it is under the limit
            - Scale down the resolution if quality alone is not enough
            - Save results to an output folder
Input:      Image folder, --max-kb (default 1000)
Tech stack: Python, Pillow
```

---

## Example 347

**Intent:**
tool to see which processes use the network

**Spec:**
```
Type:       Command-line tool (network usage)
Features:   - List processes with open network connections
            - Show local and remote address, state and process name
            - Show bytes sent and received per process when available
            - Refresh every 2 seconds in watch mode
Tech stack: Python, psutil, rich
```

---

## Example 348

**Intent:**
export my spotify playlists to csv

**Spec:**
```
Type:       Command-line tool (playlist export)
Features:   - Log in to the Spotify Web API with OAuth
            - List all playlists of the user
            - Export each playlist's tracks with title, artist, album and duration
            - Write one CSV per playlist
Input:      Spotify client ID and secret
Tech stack: Python, spotipy
```

---

## Example 349

**Intent:**
whenever i push to main, run tests on my home server and message me if they fail

**Spec:**
```
Type:       Webhook service (CI runner)
Features:   - Receive GitHub push webhooks and verify the signature
            - Pull the latest code for pushes to main
            - Run the test command and capture output
            - Send a Telegram message with the result and the failing tests
API:        REST
            POST /webhook/github
Tech stack: Python, Flask, git, Telegram Bot API
```

---

## Example 350

**Intent:**
count lines words chars in a csv column

**Spec:**
```
Type:       Command-line tool (text statistics)
Features:   - Read a text column from a CSV
            - Count words and characters per row
            - Print totals, average and maximum
            - Add count columns to a new CSV with --annotate
Input:      CSV path, --column
Tech stack: Python, pandas
```

---

## Example 351

**Intent:**
merge multiple excel workbooks, every sheet into a single workbook

**Spec:**
```
Type:       Command-line tool (workbook merge)
Features:   - Read every sheet from several Excel workbooks
            - Copy each sheet into one output workbook
            - Name copied sheets "<file>-<sheet>" truncated to 31 characters
            - Keep cell values and basic formatting
Input:      Workbook paths or glob, -o output
Tech stack: Python, openpyxl
```

---

## Example 352

**Intent:**
tool that gives me the md5 sha1 sha256 of a file and compares with a given hash

**Spec:**
```
Type:       Command-line tool (checksum)
Features:   - Calculate MD5, SHA-1 and SHA-256 of a file
            - Compare against an expected hash given with --expect
            - Detect the algorithm from the expected hash length
            - Verify a SHA256SUMS file with --check
Input:      File path, --expect, --check
Tech stack: Go, crypto/sha256, crypto/md5
```

---

## Example 353

**Intent:**
crawl a site and find all broken images

**Spec:**
```
Type:       Command-line tool (broken image checker)
Features:   - Crawl internal pages from a start URL
            - Collect image URLs from img tags and CSS backgrounds
            - Check each image URL once
            - Report broken images with the pages that use them
Input:      Start URL, --max-pages
Tech stack: Python, Scrapy
```

---

## Example 354

**Intent:**
auto update all my docker compose services every sunday

**Spec:**
```
Type:       Scheduled script (container updates)
Features:   - Pull new images for each docker compose project in a list
            - Recreate only services whose image changed
            - Remove old images after the update
            - Send a summary of updated services to a Discord webhook
Input:      List of compose project folders, webhook URL
Tech stack: Bash, Docker Compose, curl, cron
```

---

## Example 355

**Intent:**
hello sir i need a tool for convert many image in pdf, each image one pdf

**Spec:**
```
Type:       Command-line script (image to PDF)
Features:   - Find JPG and PNG images in a folder
            - Convert each image to its own PDF file
            - Keep the image's original size and orientation
            - Save PDFs with the same name as the image
Input:      Image folder
Tech stack: Python, img2pdf
```

---

## Example 356

**Intent:**
find which of our 300 product pages are missing a meta description

**Spec:**
```
Type:       Command-line tool (SEO check)
Features:   - Read page URLs from a sitemap.xml
            - Fetch each page
            - Check for title, meta description and h1
            - Flag missing, empty or too-long descriptions
            - Export results to CSV
Input:      Sitemap URL
Tech stack: Node.js, axios, cheerio, p-limit
```

---

## Example 357

**Intent:**
script to rename a bunch of files from a csv with old and new names

**Spec:**
```
Type:       Command-line script (mapped renaming)
Features:   - Read old and new names from a two-column CSV
            - Rename each file in the folder that matches an old name
            - Report names in the CSV that were not found
            - Refuse to overwrite existing files
            - Write an undo CSV
Input:      Folder path, mapping CSV
Tech stack: Python, csv, pathlib
```

---

## Example 358

**Intent:**
i want a little terminal pomodoro timer that logs my sessions

**Spec:**
```
Type:       Command-line tool (pomodoro timer)
Features:   - Run 25-minute focus and 5-minute break timers with a countdown
            - Play a sound and show a notification at the end of each period
            - Ask for a task name and log completed sessions
            - Show today's and this week's totals with a stats command
Tech stack: Python, rich, plyer
```

---

## Example 359

**Intent:**
Our marketing team gets a CSV of leads every day by email; I want it automatically imported into our Postgres database without anyone touching it.

**Spec:**
```
Type:       Scheduled script (lead import)
Features:   - Check the mailbox over IMAP for the daily leads email
            - Download the CSV attachment
            - Validate required columns and email format
            - Upsert leads into PostgreSQL by email
            - Email a summary of imported and rejected rows
Input:      IMAP settings, database URL
Tech stack: Python, imaplib, pandas, psycopg2, cron
```

---

## Example 360

**Intent:**
delete all empty folders

**Spec:**
```
Type:       Command-line script (folder cleanup)
Features:   - Find empty directories recursively
            - Delete them from the deepest level up so parents that become empty are removed too
            - Ignore folders containing only hidden system files with --ignore-junk
            - Print removed folders
Input:      Root folder
Tech stack: Bash, find -empty
```

---

## Example 361

**Intent:**
generate random strong secrets for my .env files

**Spec:**
```
Type:       Command-line tool (secret generator)
Features:   - Generate random secrets as hex, base64 or URL-safe strings
            - Set the length in bytes
            - Fill empty values in a .env file that match a key pattern with new secrets
            - Never overwrite existing values
Input:      --format, --bytes, --fill .env
Tech stack: Node.js, crypto
```

---

## Example 362

**Intent:**
check that our backups in s3 are encrypted and not public

**Spec:**
```
Type:       Command-line tool (S3 audit)
Features:   - List all buckets in the account
            - Check default encryption, public access block and bucket policy for each bucket
            - Flag buckets with public access or no encryption
            - Output a report as a table or JSON
Tech stack: Python, boto3
```

---

## Example 363

**Intent:**
im on linux mint, how do i make something that cleans my browser cache every week

**Spec:**
```
Type:       Scheduled script (cache cleanup)
Features:   - Find cache folders of Firefox and Chrome in the home directory
            - Skip cleaning if the browser is running
            - Delete cache contents but keep profiles, history and passwords
            - Run weekly with a cron job
Tech stack: Bash, pgrep, cron
```

---

## Example 364

**Intent:**
convert a google sheets export to json for my website

**Spec:**
```
Type:       Command-line tool (sheet to JSON)
Features:   - Download a published Google Sheet as CSV
            - Convert rows to JSON objects using the header row
            - Convert numeric and boolean strings to proper types
            - Write the JSON file to the website data folder
Input:      Sheet CSV URL, output path
Tech stack: Node.js, csv-parse
```

---

## Example 365

**Intent:**
something to tell me what changed on my linux system config files since last week

**Spec:**
```
Type:       Scheduled script (config change tracking)
Features:   - Commit /etc into a local git repository every night
            - Show a diff of changes since the last commit
            - Email the diff when files changed
            - Ignore files listed in an exclude list
Tech stack: Bash, etckeeper, git, cron
```

---

## Example 366

**Intent:**
split audio podcast by chapters into separate mp3s

**Spec:**
```
Type:       Command-line tool (audio chapter split)
Features:   - Read chapter markers from the audio file
            - Split the audio at each chapter without re-encoding
            - Name files with the chapter number and title
            - Copy cover art and tags into each part
Input:      Audio file
Tech stack: Python, ffmpeg, ffprobe, mutagen
```

---

## Example 367

**Intent:**
weekly report of my github issues opened and closed

**Spec:**
```
Type:       Scheduled script (issue report)
Features:   - Query issues opened and closed in the last 7 days across my repositories through the GitHub API
            - Group them by repository and label
            - Calculate average time to close
            - Post the report as a Markdown message to Slack
Input:      GitHub token, repository list, Slack webhook URL
Tech stack: Python, PyGithub, requests, cron
```

---

## Example 368

**Intent:**
pdf metadata editor cli

**Spec:**
```
Type:       Command-line tool (PDF metadata)
Features:   - Show title, author, subject, keywords and dates of a PDF
            - Set any field with flags
            - Remove all metadata with --clear
            - Apply changes to many files at once
Input:      PDF paths, --title, --author, --clear
Tech stack: Python, pypdf
```

---

## Example 369

**Intent:**
tbh i just want a thing that cleans up my screenshots folder, anything older than 2 weeks gone

**Spec:**
```
Type:       Scheduled script (screenshot cleanup)
Features:   - Find images in the Screenshots folder older than 14 days
            - Move them to the trash instead of deleting permanently
            - Skip files tagged or named with "keep"
            - Run daily
Input:      Screenshots folder path, --days
Tech stack: Python, send2trash, cron
```

---

## Example 370

**Intent:**
my company uses jira and every friday i copy the closed tickets into an excel for the client. automate pls

**Spec:**
```
Type:       Scheduled script (Jira export)
Features:   - Query Jira with JQL for issues resolved in the last 7 days
            - Collect key, summary, assignee, resolution date and time spent
            - Write them to a formatted Excel sheet with totals
            - Email the file to the client contact every Friday at 16:00
Input:      Jira URL, API token, JQL filter, SMTP settings
Tech stack: Python, jira, openpyxl, smtplib, cron
```

---

## Example 371

**Intent:**
Dear, I want to have small program that check every hour if our shop webpage show correct price, sometimes the price get wrong after update.

**Spec:**
```
Type:       Scheduled script (price validation)
Features:   - Read product URLs and expected prices from a CSV
            - Fetch each product page every hour and read the shown price
            - Compare it with the expected price
            - Email the shop owner a list of products with wrong prices
            - Log every check
Input:      CSV with URLs and expected prices, email settings
Tech stack: Python, requests, BeautifulSoup, smtplib, cron
```

---

## Example 372

**Intent:**
copy files modified in the last 24h to a usb stick

**Spec:**
```
Type:       Command-line script (incremental copy)
Features:   - Find files in a folder changed in the last 24 hours
            - Copy them to the USB stick keeping folder structure
            - Check that the stick is plugged in and has enough space first
            - Print the list of copied files
Input:      Source folder, USB drive letter or mount path
Tech stack: PowerShell, Copy-Item
```

---

## Example 373

**Intent:**
ok weird one but i want to sort a folder of fonts by font family name

**Spec:**
```
Type:       Command-line script (font organizer)
Features:   - Read the family and style names from .ttf and .otf files
            - Move each font into a folder named after its family
            - Rename files to "Family-Style.ext"
            - Report files that are not valid fonts
Input:      Fonts folder
Tech stack: Python, fontTools
```

---

## Example 374

**Intent:**
make a script that tells me the total duration of all videos in a folder

**Spec:**
```
Type:       Command-line tool (media duration)
Features:   - Read the duration of each video with ffprobe
            - Print each file's duration in HH:MM:SS
            - Print the total duration and file count
            - Search subfolders with -r
Input:      Folder path
Tech stack: Bash, ffprobe, awk
```

---

## Example 375

**Intent:**
i need to find all excel files on a shared drive that contain a certain customer name

**Spec:**
```
Type:       Command-line tool (spreadsheet search)
Features:   - Find .xlsx and .xlsm files under a folder
            - Search every cell of every sheet for a text, case-insensitive
            - Print the file, sheet and cell address of each match
            - Skip files that are password protected or corrupt
Input:      Folder path, search text
Tech stack: Python, openpyxl
```

---

## Example 376

**Intent:**
fetch all my strava activities into a csv

**Spec:**
```
Type:       Command-line tool (activity export)
Features:   - Authorize with the Strava API using OAuth and refresh tokens
            - Download all activities with pagination
            - Write date, type, distance, time, elevation and average speed to CSV
            - Fetch only new activities on later runs
Input:      Client ID and secret
Tech stack: Python, requests, Strava API
```

---

## Example 377

**Intent:**
My Raspberry Pi takes photos with a camera every 10 minutes for a plant timelapse, but the SD card fills up. I'd like it to upload the photos to my NAS each night and then delete them from the Pi.

**Spec:**
```
Type:       Scheduled script (photo offload)
Features:   - Copy the day's photos from the Pi to a NAS share with rsync
            - Verify each file arrived using checksums
            - Delete local photos only after successful verification
            - Log the number of photos moved
            - Run every night at 23:30
Input:      Photo folder, NAS SSH target
Tech stack: Bash, rsync, cron
```

---

## Example 378

**Intent:**
fix my csv where some rows have the wrong number of columns

**Spec:**
```
Type:       Command-line tool (CSV repair)
Features:   - Read a CSV and count fields on each row
            - Report rows with too many or too few fields with line numbers
            - Write good rows to a clean file and bad rows to a separate file
            - Try to fix rows with unquoted delimiters using a column count hint
Input:      CSV path, --expected-columns
Tech stack: Python, csv
```

---

## Example 379

**Intent:**
auto archive gmail emails older than 1 year from inbox

**Spec:**
```
Type:       Scheduled script (email archiving)
Features:   - Search the Gmail inbox for messages older than one year
            - Remove the INBOX label in batches to archive them
            - Skip starred and important messages
            - Log the count each run
            - Run weekly
Input:      OAuth credentials file
Tech stack: Python, Gmail API, cron
```

---

## Example 380

**Intent:**
show cpu ram disk in one line for my tmux status bar

**Spec:**
```
Type:       Command-line tool (status line)
Features:   - Read CPU usage, memory usage and root disk usage
            - Print them in one short line like "CPU 12% MEM 48% DISK 71%"
            - Color values above thresholds with tmux color codes
            - Return quickly so it can run every few seconds
Tech stack: Bash, /proc/stat, free, df
```

---

## Example 381

**Intent:**
i want to copy all my notes from apple notes into markdown files

**Spec:**
```
Type:       Command-line script (notes export)
Features:   - Read all notes from the Notes app with AppleScript
            - Convert each note's HTML body to Markdown
            - Save each note as a .md file in a folder per Notes folder
            - Use the note title as file name and keep creation dates
Input:      Output folder
Tech stack: Python, osascript (AppleScript), markdownify
```

---

## Example 382

**Intent:**
find duplicate songs in my music folder even if file names different

**Spec:**
```
Type:       Command-line tool (duplicate music finder)
Features:   - Read artist, title and duration tags from audio files
            - Group tracks with matching normalized artist and title and similar duration
            - Optionally compare audio fingerprints with --fingerprint
            - Show duplicate groups with bitrate so the best copy can be kept
            - Export the list to CSV
Input:      Music folder, --fingerprint
Tech stack: Python, mutagen, pyacoustid (Chromaprint)
```

---

## Example 383

**Intent:**
script so every new pdf in a folder gets printed automatically

**Spec:**
```
Type:       Command-line script (auto print)
Features:   - Watch a folder for new PDF files
            - Send each new PDF to a chosen printer
            - Move printed files to a "printed" subfolder
            - Log print jobs and errors
Input:      Watched folder, printer name
Tech stack: Python, watchdog, CUPS (lp)
```

---

## Example 384

**Intent:**
python cli for notes in the terminal, add list search

**Spec:**
```
Type:       Command-line tool (terminal notes)
Features:   - Add a note with a title and optional tags
            - List notes sorted by date
            - Search notes by keyword or tag
            - Open a note in $EDITOR to edit it
            - Delete a note by ID
Tech stack: Python, Typer, sqlite3
```

---

## Example 385

**Intent:**
need to download all the files from our sharepoint document library before migration

**Spec:**
```
Type:       Command-line script (SharePoint export)
Features:   - Authenticate to Microsoft Graph with an app registration
            - List all files in a document library recursively
            - Download each file keeping the folder structure
            - Retry throttled requests based on the Retry-After header
            - Write a CSV inventory of downloaded files with sizes
Input:      Site URL, library name, client credentials
Tech stack: Python, msal, requests (Microsoft Graph API)
```

---

## Example 386

**Intent:**
put the date and time on top of my security cam snapshots

**Spec:**
```
Type:       Command-line script (image timestamp)
Features:   - Read each image's capture time from EXIF or file time
            - Draw the date and time in a corner with a dark background box
            - Choose the format with --format
            - Overwrite the images or save to an output folder
Input:      Image folder, --format, --output
Tech stack: Python, Pillow
```

---

## Example 387

**Intent:**
windows batch to backup chrome bookmarks every day

**Spec:**
```
Type:       Scheduled script (bookmarks backup)
Features:   - Copy the Chrome Bookmarks file from the user profile
            - Save it with the date in a backup folder
            - Keep the last 30 copies
            - Run daily with Task Scheduler
Input:      Backup folder path
Tech stack: Windows batch (cmd), xcopy, forfiles, Windows Task Scheduler
```

---

## Example 388

**Intent:**
Every quarter I have to pull our numbers from three different CSV exports, stick them in a PowerPoint template and send it to the board. Would be amazing if a script could build the slides.

**Spec:**
```
Type:       Command-line script (presentation generation)
Features:   - Read the three CSV exports and calculate quarterly totals and changes
            - Create charts for revenue, costs and customers
            - Fill a PowerPoint template's placeholders with numbers and charts
            - Save the deck with the quarter in the file name
Input:      CSV exports, PowerPoint template, --quarter
Tech stack: Python, pandas, matplotlib, python-pptx
```

---

## Example 389

**Intent:**
grep but for pdfs

**Spec:**
```
Type:       Command-line tool (PDF search)
Features:   - Search the text of PDFs in a folder for a pattern
            - Print file name, page number and the matching line
            - Support regular expressions and -i for case-insensitive search
            - Search folders recursively
Input:      Pattern, folder path, -i
Tech stack: Bash, pdfgrep
```

---

## Example 390

**Intent:**
check if my external hdd backups are older than a week and remind me

**Spec:**
```
Type:       Scheduled script (backup reminder)
Features:   - Read the date of the last backup from a marker file on the drive or a local log
            - Show a desktop notification when the last backup is older than 7 days
            - Repeat the reminder every day until a backup happens
Input:      Marker file path
Tech stack: Python, plyer, cron
```

---

## Example 391

**Intent:**
trim the first 10 seconds off a bunch of videos

**Spec:**
```
Type:       Command-line script (video trimming)
Features:   - Cut a set number of seconds from the start of each video
            - Optionally cut from the end with --end
            - Use stream copy for speed or re-encode for frame-exact cuts with --exact
            - Save results with a _trimmed suffix
Input:      Folder or files, --start seconds, --end seconds
Tech stack: Bash, ffmpeg
```

---

## Example 392

**Intent:**
make a script that creates folders for every client from a list

**Spec:**
```
Type:       Command-line script (folder creation)
Features:   - Read client names from a text or CSV file
            - Create a folder per client with a standard set of subfolders (Contracts, Invoices, Correspondence)
            - Remove characters not allowed in folder names
            - Skip folders that already exist
Input:      Client list, root folder, subfolder template
Tech stack: PowerShell, New-Item
```

---

## Example 393

**Intent:**
monitor how long my cron jobs run and alert if one never finished

**Spec:**
```
Type:       Webhook service (cron job monitor)
Features:   - Receive start and finish pings from each job
            - Record run duration and exit status
            - Alert by email when a job does not report within its expected schedule
            - Show the last runs of each job on a status page
API:        REST
            POST /ping/{job}/start
            POST /ping/{job}/finish
            GET /status
Tech stack: Python, FastAPI, APScheduler
```

---

## Example 394

**Intent:**
download my bandcamp purchases

**Spec:**
```
Type:       Command-line tool (music purchase downloader)
Features:   - Log in with a browser cookie
            - List all items in the collection
            - Download each item in a chosen format (FLAC, MP3)
            - Skip items already downloaded and unzip albums
Input:      Cookie file, --format, output folder
Tech stack: Python, requests, BeautifulSoup
```

---

## Example 395

**Intent:**
i want to know when someone logs into my server by ssh

**Spec:**
```
Type:       Command-line script (login alert)
Features:   - Run on every SSH login through a PAM exec hook
            - Send a Telegram message with user, source IP and time
            - Look up the IP's country
            - Skip alerts for IPs on a trusted list
Input:      Telegram bot token and chat ID, trusted IP list
Tech stack: Bash, pam_exec, curl
```

---

## Example 396

**Intent:**
average every column of a csv by group

**Spec:**
```
Type:       Command-line tool (CSV aggregation)
Features:   - Group rows by one or more columns
            - Calculate the mean (or sum, min, max with --agg) for all numeric columns
            - Write the summary to CSV or print it as a table
Input:      CSV path, --by, --agg
Tech stack: Python, pandas
```

---

## Example 397

**Intent:**
tool for making a zip of only the files git tracks

**Spec:**
```
Type:       Command-line tool (git archive)
Features:   - Create a zip or tar.gz of the files tracked by git at HEAD or a given ref
            - Prefix paths with the project name
            - Add uncommitted changes with --include-dirty
            - Name the archive with the short commit hash
Input:      --ref, --format
Tech stack: Bash, git archive
```

---

## Example 398

**Intent:**
Hello, our sales people put photos of visits in one folder and I need them in folders by the sales person name, the name is in the file name before the underscore.

**Spec:**
```
Type:       Command-line script (file sorting)
Features:   - Read the part of each file name before the first underscore
            - Create a folder for each salesperson name
            - Move each photo into its salesperson's folder
            - Put files without an underscore into an "unknown" folder
Input:      Photos folder
Tech stack: Python, pathlib, shutil
```

---

## Example 399

**Intent:**
watch a website for when tickets for a concert go on sale

**Spec:**
```
Type:       Scheduled script (ticket monitor)
Features:   - Check the event page every 2 minutes
            - Detect when the "sold out" or "coming soon" text changes to a buy button
            - Send a push notification with the link immediately
            - Stop checking after the alert is sent
Input:      Event URL, CSS selector, ntfy topic
Tech stack: Python, Playwright, requests
```

---

## Example 400

**Intent:**
convert all .doc in folder to .docx so new word stops complaining

**Spec:**
```
Type:       Command-line script (format conversion)
Features:   - Find all .doc files in a folder and subfolders
            - Open each one in Word through COM and save as .docx
            - Keep the original modified date
            - Move the old .doc files to an archive folder
Input:      Folder path
Tech stack: PowerShell, Word COM automation
```

---

## Example 401

**Intent:**
track my website's google ranking for some keywords every week

**Spec:**
```
Type:       Scheduled script (rank tracking)
Features:   - Query a search API for each keyword every week
            - Find the position of my domain in the top 100 results
            - Save the position with the date
            - Email a table showing changes since last week
Input:      Keywords, domain, SerpAPI key
Tech stack: Python, SerpAPI, sqlite3, cron
```

---

## Example 402

**Intent:**
Generate a monthly PDF of my personal expenses from a google sheet with a pie chart

**Spec:**
```
Type:       Scheduled script (expense report)
Features:   - Read last month's expense rows from a Google Sheet
            - Sum spending by category
            - Draw a pie chart of categories
            - Build a PDF with the chart, totals and the 10 largest expenses
            - Save it to a Reports folder on the 1st of each month
Input:      Sheet ID, service account key
Tech stack: Python, gspread, matplotlib, fpdf2, cron
```

---

## Example 403

**Intent:**
show me all cron jobs on all my servers in one list

**Spec:**
```
Type:       Command-line tool (cron inventory)
Features:   - Connect to each server over SSH
            - Read user crontabs, /etc/crontab and /etc/cron.d files
            - Parse schedules and commands
            - Show a combined table of server, user, schedule and command
            - Export to CSV
Input:      Server list file
Tech stack: Python, Fabric
```

---

## Example 404

**Intent:**
shuffle lines in a file

**Spec:**
```
Type:       Command-line tool (text processing)
Features:   - Randomly shuffle the lines of a file or stdin
            - Use a seed for repeatable output with --seed
            - Output only the first N lines with -n
Input:      File path or stdin
Tech stack: Python, random
```

---

## Example 405

**Intent:**
i got thousands of json files from an api, need them all in one big csv

**Spec:**
```
Type:       Command-line tool (JSON to CSV)
Features:   - Read all .json files in a folder
            - Flatten nested fields into columns
            - Combine records from all files into one CSV with the union of columns
            - Add a source_file column
            - Stream records to keep memory use low
Input:      Folder path, -o output
Tech stack: Python, pandas, json
```

---

## Example 406

**Intent:**
make my bash history searchable across all my machines

**Spec:**
```
Type:       Command-line tool (shell history sync)
Features:   - Save each shell command with time, host and directory to a database
            - Sync the database to a server with end-to-end encryption
            - Search history across machines with a fuzzy search interface
            - Filter by host or directory
Tech stack: Atuin, Bash
```

---

## Example 407

**Intent:**
rename files using text from inside them (first line is the title)

**Spec:**
```
Type:       Command-line script (content-based renaming)
Features:   - Read the first non-empty line of each text file
            - Turn it into a safe file name
            - Rename the file keeping its extension
            - Add a counter when two files get the same title
Input:      Folder path, --ext
Tech stack: Python, pathlib
```

---

## Example 408

**Intent:**
need weekly check that all our domains point to the right IP

**Spec:**
```
Type:       Scheduled script (DNS check)
Features:   - Read domains and expected IP addresses from a CSV
            - Resolve A and AAAA records for each domain
            - Report domains that point to unexpected addresses or do not resolve
            - Email the report weekly
Input:      Domains CSV, email settings
Tech stack: Python, dnspython, smtplib, cron
```

---

## Example 409

**Intent:**
resize and compress images before i email them

**Spec:**
```
Type:       Command-line tool (email image prep)
Features:   - Resize selected images to a maximum of 1600 px on the long side
            - Compress them as JPEG at quality 80
            - Zip the results into one file ready to attach
            - Print the final zip size
Input:      Image files
Tech stack: Bash, ImageMagick, zip
```

---

## Example 410

**Intent:**
im on windows w/ python, wanna open a list of urls in chrome every morning at 9

**Spec:**
```
Type:       Scheduled script (morning tabs)
Features:   - Read URLs from a text file
            - Open each URL in a new Chrome tab
            - Run on weekdays at 09:00 with Task Scheduler
            - Skip URLs commented out with #
Input:      URL list file
Tech stack: Python, webbrowser, Windows Task Scheduler
```

---

## Example 411

**Intent:**
list all the email addresses that ever sent me mail

**Spec:**
```
Type:       Command-line script (sender export)
Features:   - Read the From header of every message in all IMAP folders
            - Extract name and email address
            - Count messages per sender
            - Export a CSV sorted by count
Input:      IMAP settings
Tech stack: Python, imapclient, email.utils
```

---

## Example 412

**Intent:**
script that makes a new python project folder with venv and git ready

**Spec:**
```
Type:       Command-line tool (project scaffolding)
Features:   - Create a project folder with src, tests and README.md
            - Create a virtual environment and install starter packages
            - Write a .gitignore for Python
            - Run git init and make the first commit
            - Accept the project name as an argument
Input:      Project name, --packages
Tech stack: Bash, python -m venv, git
```

---

## Example 413

**Intent:**
check that all images on my site have alt text

**Spec:**
```
Type:       Command-line tool (accessibility check)
Features:   - Scan built HTML files in a folder
            - Find img tags with a missing or empty alt attribute
            - Report file, line and image source
            - Exit non-zero for use in CI
Input:      Site folder
Tech stack: Node.js, cheerio, fast-glob
```

---

## Example 414

**Intent:**
delete specific pages from a pdf

**Spec:**
```
Type:       Command-line tool (PDF utility)
Features:   - Remove pages given as a list or ranges (2,5,7-9)
            - Support negative numbers for counting from the end
            - Write the result to a new file
            - Validate page numbers against the page count
Input:      PDF path, --pages, -o output
Tech stack: Bash, qpdf
```

---

## Example 415

**Intent:**
a script that moves finished torrents into movies or tv folders

**Spec:**
```
Type:       Command-line script (media sorting)
Features:   - Run when a download completes (called by the torrent client)
            - Detect TV episodes by SxxEyy patterns and movies by year in the name
            - Move TV files to TV/Show/Season XX and movies to Movies/Title (Year)
            - Remove leftover sample files and .nfo files
Input:      Download path passed by the torrent client
Tech stack: Python, re, shutil
```

---

## Example 416

**Intent:**
count unique visitors per day from my access log

**Spec:**
```
Type:       Command-line tool (log analysis)
Features:   - Parse access log lines into date, IP and user agent
            - Count unique IP and user agent pairs per day
            - Exclude known bots by user agent
            - Print a daily table and optional CSV
Input:      Log files, --csv
Tech stack: Go, bufio, regexp
```

---

## Example 417

**Intent:**
notify me on my phone when my long running command finishes

**Spec:**
```
Type:       Command-line tool (command notifier)
Features:   - Wrap any command and run it
            - Measure how long it ran
            - Send a push notification with the command, exit code and duration when it ends
            - Only notify if it ran longer than a minimum time
Input:      Command after --, --min-seconds
Tech stack: Bash, curl (ntfy.sh)
```

---

## Example 418

**Intent:**
zip up and email the logs folder when the app crashes

**Spec:**
```
Type:       Command-line script (crash report)
Features:   - Run after the app exits with a non-zero code
            - Zip the logs folder and the latest crash dump
            - Email the zip to the developer with host name and exit code
            - Delete zips older than 7 days
Input:      Logs folder, email settings
Tech stack: PowerShell, Compress-Archive, Send-MailMessage
```

---

## Example 419

**Intent:**
unpack all the rar and 7z archives in my downloads

**Spec:**
```
Type:       Command-line script (archive extraction)
Features:   - Find .rar, .7z and .zip files
            - Extract multi-part archives only once from the first part
            - Extract each to a folder with the archive's name
            - Delete archives after successful extraction with --cleanup
Input:      Folder path, --cleanup
Tech stack: Bash, 7-Zip (7z)
```

---

## Example 420

**Intent:**
need to convert hundreds of heic and png screenshots to one format, jpg, and make names consistent like img_0001

**Spec:**
```
Type:       Command-line script (image normalization)
Features:   - Find HEIC, PNG and JPEG files in a folder
            - Convert all non-JPEG images to JPEG
            - Sort files by date taken or modification date
            - Rename them to img_0001.jpg in that order
            - Write converted files to a new folder
Input:      Input folder, output folder
Tech stack: Python, Pillow, pillow-heif
```

---
