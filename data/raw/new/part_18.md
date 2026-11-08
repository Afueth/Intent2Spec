## Example 1

**Intent:**
a link shortener for my small business

**Spec:**
```
Type:       Web application (URL shortener)
Auth:       Email + password login for the business owner
Data model: User(id, email, password_hash)
            ShortLink(id, user_id -> User, slug, target_url, created_at, expires_at)
            Click(id, link_id -> ShortLink, clicked_at, referrer, country)
Features:   - Create a short link with a random or custom slug
            - Redirect visitors from the slug to the target URL with HTTP 302
            - Record each click with referrer and country
            - Show click counts per link per day
            - Disable links after an optional expiry date
API:        REST
            POST /links
            GET  /links
            GET  /{slug}
            GET  /links/{id}/stats
Storage:    PostgreSQL
Tech stack: Go, chi router, PostgreSQL, Svelte dashboard
```

---

## Example 2

**Intent:**
I run an online store and the product photos people upload are huge. I'd like a service that takes an image URL and gives back a resized, compressed version in whatever width I ask for, so my pages load faster.

**Spec:**
```
Type:       REST API service (image resizing)
Auth:       Signed URLs (HMAC of the parameters with a shared secret)
Features:   - Fetch the source image from an allowed origin domain
            - Resize to the requested width while keeping the aspect ratio
            - Convert to WebP or AVIF when the browser accepts it
            - Compress with a configurable quality level
            - Cache resized results and serve them with long cache headers
API:        REST
            GET  /img?url={source}&w={width}&q={quality}&sig={signature}
Storage:    S3 bucket (resized image cache)
Tech stack: Node.js, Fastify, sharp, AWS S3, CloudFront CDN
```

---

## Example 3

**Intent:**
need an api that turns html invoices into pdf files

**Spec:**
```
Type:       REST API service (PDF generation)
Auth:       API key per client (X-API-Key header)
Data model: ApiClient(id, name, api_key_hash)
            RenderJob(id, client_id -> ApiClient, status, pdf_url, created_at)
Features:   - Accept HTML and CSS and render it to a PDF with a headless browser
            - Support page size, margins, header and footer options
            - Return small PDFs directly and queue large ones as jobs
            - Store finished PDFs and return a time-limited download link
            - Delete stored PDFs after 24 hours
API:        REST
            POST /render
            GET  /jobs/{id}
            GET  /jobs/{id}/download
Storage:    PostgreSQL (jobs), S3-compatible object storage (PDF files)
Tech stack: Node.js, Express, Puppeteer, BullMQ, Redis
```

---

## Example 4

**Intent:**
Our delivery team keeps getting wrong addresses from customers. Can we check the address when they type it and fix it before the order is saved?

**Spec:**
```
Type:       REST API service (address validation)
Auth:       Internal service token
Data model: AddressCheck(id, raw_input, normalized_address, latitude, longitude, confidence, checked_at)
Features:   - Normalize street, city and postal code formatting
            - Geocode the address to latitude and longitude
            - Return suggestions when the match confidence is low
            - Reject addresses outside the delivery zone polygon
            - Cache results for repeated addresses
API:        REST
            POST /addresses/validate
            GET  /addresses/suggest?q={partial}
Storage:    PostgreSQL with PostGIS (delivery zones), Redis (cache)
Tech stack: Python, FastAPI, Nominatim geocoder, Shapely
```

---

## Example 5

**Intent:**
currency converter api with daily rates

**Spec:**
```
Type:       REST API service (currency conversion)
Data model: ExchangeRate(id, base_currency, quote_currency, rate, rate_date)
Features:   - Fetch daily reference rates from the European Central Bank feed
            - Convert an amount between any two supported currencies
            - Return historical rates for a given date
            - Compute cross rates through EUR when no direct pair exists
            - Round results to each currency's minor unit
API:        REST
            GET  /convert?from={code}&to={code}&amount={value}
            GET  /rates/{date}
            GET  /currencies
Storage:    PostgreSQL
Tech stack: Python, FastAPI, httpx, APScheduler
```

---

## Example 6

**Intent:**
i want to turn features on and off in my app without redeploying it, like for 10% of users first

**Spec:**
```
Type:       Web application (feature flag service)
Auth:       Admin login (email + password); SDK keys per environment
Data model: Project(id, name)
            Environment(id, project_id -> Project, name, sdk_key)
            Flag(id, project_id -> Project, key, description)
            FlagRule(id, flag_id -> Flag, environment_id -> Environment, enabled, rollout_percent, user_segment)
Features:   - Create flags and toggle them per environment
            - Roll out a flag to a percentage of users using a stable hash of user ID
            - Target flags at user segments by attributes
            - Serve flag values to client SDKs with low latency
            - Keep a history of every flag change
API:        REST
            GET  /sdk/flags
            POST /flags
            PATCH /flags/{id}/rules
Storage:    PostgreSQL, Redis (flag cache)
Tech stack: TypeScript, NestJS, React admin UI
```

---

## Example 7

**Intent:**
Put a gateway in front of our APIs that limits how many requests each customer can make per minute.

**Spec:**
```
Type:       REST API service (rate-limiting gateway)
Auth:       API key per customer, checked at the gateway
Data model: Customer(id, name, plan)
            ApiKey(id, customer_id -> Customer, key_hash, active)
            Plan(id, name, requests_per_minute, burst)
Features:   - Proxy requests to upstream services by path prefix
            - Enforce per-key limits with a token bucket algorithm
            - Return HTTP 429 with a Retry-After header when the limit is hit
            - Add X-RateLimit-Remaining headers to every response
            - Reload plan limits without restarting
API:        REST
            ANY  /api/{service}/{path}
            GET  /admin/usage/{customer_id}
Storage:    Redis (counters), PostgreSQL (customers and plans)
Tech stack: Go, net/http reverse proxy, go-redis
```

---

## Example 8

**Intent:**
so we're a small saas and right now api keys are just hardcoded strings in a config file lol. i want customers to be able to make their own keys, give them names, revoke them, and see when each was last used

**Spec:**
```
Type:       Web application (API key management)
Auth:       Customer account login (email + password)
Data model: Account(id, email, password_hash)
            ApiKey(id, account_id -> Account, name, prefix, key_hash, scopes, last_used_at, revoked_at)
Features:   - Generate a key, show it once and store only its hash
            - Name keys and limit them to scopes like read or write
            - Revoke a key immediately
            - Record last-used time on each authenticated request
            - Show a key prefix so customers can tell keys apart
API:        REST
            GET  /keys
            POST /keys
            DELETE /keys/{id}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, PostgreSQL, Hotwire
```

---

## Example 9

**Intent:**
Charge our customers by how many API calls they make each month, different price per plan.

**Spec:**
```
Type:       REST API service (usage metering and billing)
Auth:       Internal service tokens
Data model: Tenant(id, name, plan_id -> Plan)
            Plan(id, name, included_calls, price_per_1000_calls)
            UsageEvent(id, tenant_id -> Tenant, metric, quantity, occurred_at)
            Invoice(id, tenant_id -> Tenant, period_start, period_end, total_cents, status)
Features:   - Ingest usage events from services in batches
            - Aggregate usage per tenant per billing period
            - Calculate overage charges above the included amount
            - Generate monthly invoices and mark them paid or unpaid
            - Show current-period usage to each tenant
API:        REST
            POST /usage/events
            GET  /tenants/{id}/usage
            GET  /tenants/{id}/invoices
Storage:    PostgreSQL, ClickHouse (raw usage events)
Tech stack: Python, FastAPI, Celery
```

---

## Example 10

**Intent:**
when someone emails support@ourcompany, turn the email into a ticket automatically

**Spec:**
```
Type:       Webhook service (inbound email parsing)
Data model: Ticket(id, subject, requester_email, status, created_at)
            Message(id, ticket_id -> Ticket, body_text, from_email, received_at)
            Attachment(id, message_id -> Message, filename, storage_key)
Features:   - Receive parsed inbound emails from the mail provider webhook
            - Create a new ticket or append to an existing one by matching the ticket ID in the subject
            - Strip quoted replies and signatures from the body
            - Save attachments to object storage
            - Verify the webhook signature before processing
API:        REST
            POST /webhooks/inbound-email
Storage:    PostgreSQL, S3 (attachments)
Tech stack: Node.js, Express, Mailgun Routes, email-reply-parser
```

---

## Example 11

**Intent:**
My dental clinic sends appointment reminders by SMS. I want patients to reply YES or NO and have the calendar update.

**Spec:**
```
Type:       Webhook service (two-way SMS)
Data model: Patient(id, name, phone)
            Appointment(id, patient_id -> Patient, starts_at, status)
            SmsMessage(id, appointment_id -> Appointment, direction, body, sent_at)
Features:   - Send a reminder SMS 24 hours before each appointment
            - Receive replies from the SMS provider webhook
            - Mark the appointment confirmed on YES and cancelled on NO
            - Reply with a help message for anything else
            - Notify the front desk when a patient cancels
API:        REST
            POST /webhooks/sms/inbound
            GET  /appointments?date={day}
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio Programmable Messaging, Celery beat
```

---

## Example 12

**Intent:**
sync my google calendar and my outlook work calendar both ways

**Spec:**
```
Type:       Scheduled script (calendar sync)
Data model: SyncedEvent(id, google_event_id, outlook_event_id, last_hash, updated_at)
Features:   - Read changed events from Google Calendar using sync tokens
            - Read changed events from Outlook using Microsoft Graph delta queries
            - Create, update or delete the matching event on the other side
            - Skip events that were created by the sync itself to avoid loops
            - Run every 5 minutes and log each change
Storage:    SQLite (event ID mapping)
Tech stack: Python, Google Calendar API, Microsoft Graph API, OAuth 2.0
```

---

## Example 13

**Intent:**
Users upload files to our site and we need to check them for viruses before anyone else can download them.

**Spec:**
```
Type:       REST API service (file upload and virus scanning)
Auth:       User session token
Data model: Upload(id, user_id, filename, size_bytes, sha256, status, scanned_at)
Features:   - Accept uploads into a quarantine bucket
            - Scan each file with ClamAV in a background worker
            - Move clean files to the public bucket and mark them available
            - Delete infected files and notify the uploader
            - Block downloads of files that are not yet scanned
API:        REST
            POST /uploads
            GET  /uploads/{id}
            GET  /uploads/{id}/download
Storage:    S3 (quarantine and clean buckets), PostgreSQL
Tech stack: Python, FastAPI, ClamAV (clamd), RQ workers
```

---

## Example 14

**Intent:**
search for our docs site, typo tolerant

**Spec:**
```
Type:       REST API service (search indexing)
Data model: Document(id, url, title, headings, body, updated_at)
Features:   - Crawl the docs site sitemap and extract page content
            - Index pages into a search engine with typo tolerance
            - Boost matches in titles and headings
            - Return highlighted snippets with each result
            - Re-index changed pages on each docs deploy
API:        REST
            GET  /search?q={query}
            POST /reindex
Storage:    Meilisearch index
Tech stack: Node.js, Meilisearch, Cheerio
```

---

## Example 15

**Intent:**
hey so i have a little bookshop website, could we show "people who bought this also bought" under each book? we have like 3 years of orders

**Spec:**
```
Type:       REST API service (recommendations)
Data model: Order(id, customer_id, created_at)
            OrderItem(id, order_id -> Order, book_id)
            BookSimilarity(book_id, similar_book_id, score)
Features:   - Compute item-to-item co-purchase scores from past orders
            - Recalculate similarities nightly
            - Return the top 6 related books for a given book
            - Exclude out-of-stock books from results
            - Fall back to bestsellers in the same category for new books
API:        REST
            GET  /recommendations/books/{book_id}
Storage:    PostgreSQL
Tech stack: Python, pandas, scikit-learn, FastAPI
```

---

## Example 16

**Intent:**
I'd like to publish my city's bus stop and timetable data as a free public API that anyone can use.

**Spec:**
```
Type:       REST API service (public open data)
Data model: Stop(id, code, name, latitude, longitude)
            Route(id, short_name, long_name)
            StopTime(id, route_id -> Route, stop_id -> Stop, arrival_time, service_day)
Features:   - Import GTFS timetable files into the database
            - List stops near a coordinate
            - Return the next departures from a stop
            - Serve responses as JSON with CORS enabled
            - Apply a generous anonymous rate limit per IP
API:        REST
            GET  /stops?near={lat},{lon}
            GET  /stops/{id}/departures
            GET  /routes
Storage:    PostgreSQL with PostGIS
Tech stack: Python, FastAPI, gtfs-kit, OpenAPI docs
```

---

## Example 17

**Intent:**
We have about 200 temperature sensors in a warehouse that send readings every 30 seconds. Need an endpoint to collect all of it.

**Spec:**
```
Type:       IoT system (sensor ingestion)
Auth:       Per-device token issued at registration
Data model: Device(id, name, location, token_hash, last_seen_at)
            Reading(device_id -> Device, temperature_c, humidity, recorded_at)
Features:   - Receive readings over MQTT and HTTP
            - Validate and batch-insert readings into a time-series table
            - Flag devices that have not reported for 5 minutes
            - Downsample old data to 5-minute averages after 30 days
            - Show latest reading per sensor on a map of the warehouse
API:        REST
            POST /ingest
            GET  /devices/{id}/readings?from={t}&to={t}
Storage:    TimescaleDB
Tech stack: Go, Eclipse Mosquitto, TimescaleDB, Grafana
```

---

## Example 18

**Intent:**
audit log so we know who changed what in the admin panel

**Spec:**
```
Type:       REST API service (audit logging)
Auth:       Service token for writers; admin login for readers
Data model: AuditEvent(id, actor_id, actor_ip, action, resource_type, resource_id, before_json, after_json, created_at)
Features:   - Record an event for every create, update and delete in the admin panel
            - Store before and after values for changed fields
            - Make events append-only with no update or delete endpoint
            - Filter events by user, resource and date range
            - Export filtered events to CSV
API:        REST
            POST /audit-events
            GET  /audit-events?actor={id}&resource={type}
Storage:    PostgreSQL (append-only table)
Tech stack: Java, Spring Boot, PostgreSQL
```

---

## Example 19

**Intent:**
customers keep asking under GDPR for a copy of their data or for us to delete their account. we do it by hand now, takes hours

**Spec:**
```
Type:       Web application (GDPR data requests)
Auth:       Customer email verification link; staff login for review
Data model: DataRequest(id, customer_email, type, status, requested_at, completed_at)
            RequestLog(id, request_id -> DataRequest, system, result, logged_at)
Features:   - Let customers submit export or deletion requests
            - Verify identity through an email confirmation link
            - Collect the customer's data from each internal system into a ZIP of JSON files
            - Delete or anonymize records across systems on deletion requests
            - Track the 30-day deadline and alert staff when it is close
API:        REST
            POST /requests
            GET  /requests/{id}
            GET  /requests/{id}/export
Storage:    PostgreSQL, S3 (export archives)
Tech stack: Python, Django, Celery
```

---

## Example 20

**Intent:**
Every Monday morning email my managers a sales summary from our database as an Excel file.

**Spec:**
```
Type:       Scheduled script (report emailer)
Features:   - Run every Monday at 7:00 with cron
            - Query last week's sales totals by region and product
            - Build an Excel file with one sheet per region
            - Email the file to a list of managers
            - Log failures and retry once
Input:      Database connection string, recipient list in a YAML config
Tech stack: Python, SQLAlchemy, openpyxl, smtplib
```

---

## Example 21

**Intent:**
every pull request should get its own temporary test website that gets deleted when the PR is merged

**Spec:**
```
Type:       Infrastructure setup (preview environments)
Features:   - Build a container image for each pull request
            - Deploy it to a Kubernetes namespace named after the PR number
            - Create a subdomain like pr-123.preview.example.com with TLS
            - Seed a fresh database copy for the preview
            - Post the preview URL as a comment on the PR
            - Delete the namespace when the PR is closed or merged
Tech stack: GitHub Actions, Kubernetes, Helm, cert-manager, external-dns
```

---

## Example 22

**Intent:**
How can I deploy new versions of my web app without any downtime? I want to switch traffic over only when the new one is healthy.

**Spec:**
```
Type:       Infrastructure setup (blue-green deployment)
Features:   - Run two identical environments named blue and green behind a load balancer
            - Deploy the new version to the idle environment
            - Run health checks and smoke tests against the idle environment
            - Switch the load balancer target to the new environment
            - Roll back by switching traffic back to the old environment
Tech stack: AWS Application Load Balancer, ECS, Terraform, GitHub Actions
```

---

## Example 23

**Intent:**
rotate database passwords automatically every 30 days

**Spec:**
```
Type:       Scheduled script (secrets rotation)
Features:   - Generate a new strong password for each database user
            - Update the password in the database with ALTER USER
            - Store the new password in the secrets manager as the current version
            - Keep the previous version valid until apps have reloaded
            - Send a report of rotated secrets to the ops channel
Input:      List of database users and secret names in a config file
Tech stack: Python, AWS Secrets Manager, boto3, psycopg
```

---

## Example 24

**Intent:**
I have one Postgres database and I'm scared of losing it. Set up a second copy that follows the first one live and can take over.

**Spec:**
```
Type:       Infrastructure setup (database replication)
Features:   - Configure streaming replication from primary to a standby server
            - Use a replication slot so WAL is kept until the standby receives it
            - Monitor replication lag and alert above 30 seconds
            - Promote the standby to primary during failover
            - Document the steps to rebuild the old primary as a new standby
Storage:    PostgreSQL 16 (primary and hot standby)
Tech stack: PostgreSQL, Patroni, etcd, Ansible
```

---

## Example 25

**Intent:**
self hosted git server for me and 3 friends

**Spec:**
```
Type:       Infrastructure setup (self-hosted Git)
Auth:       User accounts with SSH keys and 2FA
Features:   - Host private Git repositories with a web interface
            - Allow push and pull over SSH and HTTPS
            - Provide issues and pull requests
            - Back up repositories and the database nightly
            - Serve the site over HTTPS with automatic certificates
Storage:    SQLite (Gitea metadata), local disk (repositories)
Tech stack: Gitea, Docker Compose, Caddy
```

---

## Example 26

**Intent:**
i got an old pc and want to make it a home server for movies, file sharing and backups of our phones

**Spec:**
```
Type:       Infrastructure setup (home lab server)
Auth:       Local user accounts per family member
Features:   - Install a Linux server OS with RAID 1 across two disks
            - Run a media server for streaming movies to the TV
            - Share folders on the home network over SMB
            - Back up phone photos automatically over Wi-Fi
            - Manage all services as containers from a web dashboard
Storage:    Local disks (ZFS mirror)
Tech stack: Ubuntu Server, Docker Compose, Jellyfin, Samba, Immich, Portainer
```

---

## Example 27

**Intent:**
I want to reach my home network safely when I'm travelling, using WireGuard.

**Spec:**
```
Type:       Infrastructure setup (VPN)
Auth:       Per-device WireGuard key pairs
Features:   - Install a WireGuard server on a home Raspberry Pi
            - Generate a config and QR code for each phone and laptop
            - Route home LAN traffic through the tunnel
            - Forward one UDP port on the router
            - Update a dynamic DNS name when the home IP changes
Tech stack: WireGuard, Raspberry Pi OS, ddclient
```

---

## Example 28

**Intent:**
host my static website cheap with https and my own domain

**Spec:**
```
Type:       Infrastructure setup (static site hosting)
Features:   - Store the site files in an object storage bucket
            - Serve the site through a CDN with HTTPS
            - Point the custom domain to the CDN with DNS records
            - Redirect HTTP to HTTPS and www to the apex domain
            - Upload and invalidate the cache on each push to main
Tech stack: AWS S3, CloudFront, Route 53, ACM certificate, GitHub Actions
```

---

## Example 29

**Intent:**
plz make a qr code generator api, give text get png back

**Spec:**
```
Type:       REST API service (QR code generation)
Features:   - Encode text or a URL into a QR code
            - Return the code as PNG or SVG
            - Set size, margin and error correction level from query parameters
            - Reject inputs longer than the QR capacity
            - Cache generated images by input hash
API:        REST
            GET  /qr?data={text}&size={px}&format={png|svg}
Storage:    In-memory LRU cache
Tech stack: Python, Flask, segno
```

---

## Example 30

**Intent:**
I translate websites as a freelancer. I want a service that takes a page and extracts all the text strings into a file I can translate, then puts the translations back.

**Spec:**
```
Type:       REST API service (translation string extraction)
Auth:       Single user API token
Data model: Project(id, name, source_lang, target_lang)
            Page(id, project_id -> Project, url, html)
            Segment(id, page_id -> Page, xpath, source_text, translated_text)
Features:   - Fetch a page and split visible text into segments
            - Export segments as an XLIFF file
            - Import a translated XLIFF and match segments by ID
            - Rebuild the page HTML with translations inserted
            - Report segments that are still untranslated
API:        REST
            POST /projects/{id}/pages
            GET  /projects/{id}/export.xliff
            POST /projects/{id}/import
Storage:    SQLite
Tech stack: Python, FastAPI, lxml
```

---

## Example 31

**Intent:**
timezone lookup api from coordinates

**Spec:**
```
Type:       REST API service (timezone lookup)
Features:   - Return the IANA timezone name for a latitude and longitude
            - Return the current UTC offset and whether DST is active
            - Use timezone boundary polygons for accurate borders
            - Handle points at sea with nautical timezones
API:        REST
            GET  /timezone?lat={lat}&lon={lon}
Storage:    In-memory spatial index of timezone polygons
Tech stack: Rust, Axum, timezone-boundary-builder data, rstar
```

---

## Example 32

**Intent:**
Our accountant wants every invoice we send to also be saved as a PDF in a shared Google Drive folder, sorted by month.

**Spec:**
```
Type:       Webhook service (invoice archiving)
Data model: ArchivedInvoice(id, invoice_number, customer_name, drive_file_id, archived_at)
Features:   - Receive an "invoice finalized" webhook from the billing system
            - Download the invoice PDF
            - Create a Year/Month folder in Google Drive if it does not exist
            - Upload the PDF with a name like 2026-11_INV-0042_CustomerName.pdf
            - Skip invoices that were already archived
API:        REST
            POST /webhooks/invoice-finalized
Storage:    SQLite (archived invoice log)
Tech stack: Node.js, Express, Google Drive API (service account)
```

---

## Example 33

**Intent:**
i need a service where i send it a long video and it gives me back thumbnails and a smaller version for phones

**Spec:**
```
Type:       REST API service (video transcoding)
Auth:       API key
Data model: TranscodeJob(id, source_url, status, progress_percent, created_at)
            Output(id, job_id -> TranscodeJob, kind, resolution, url)
Features:   - Accept a video upload or a source URL
            - Transcode to 480p and 720p H.264 MP4 renditions
            - Extract thumbnails at 10% intervals
            - Report job progress and status
            - Call a callback URL when the job finishes
API:        REST
            POST /jobs
            GET  /jobs/{id}
            GET  /jobs/{id}/outputs
Storage:    PostgreSQL (jobs), S3 (videos and thumbnails)
Tech stack: Python, FastAPI, FFmpeg, Celery, Redis
```

---

## Example 34

**Intent:**
Make a status page for our product that shows if the API, website and payments are up, and lets us post incident updates.

**Spec:**
```
Type:       Web application (public status page)
Auth:       Staff login for posting incidents; public page has no login
Data model: Component(id, name, status, check_url)
            Incident(id, title, impact, status, started_at, resolved_at)
            IncidentUpdate(id, incident_id -> Incident, message, posted_at)
            Subscriber(id, email, confirmed)
Features:   - Show each component as operational, degraded or down
            - Check component URLs every minute and update status
            - Post incidents with timestamped updates
            - Show 90 days of uptime history per component
            - Email subscribers when an incident is opened or resolved
API:        REST
            GET  /api/status
            POST /api/incidents
            POST /api/incidents/{id}/updates
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 35

**Intent:**
something that checks every night that our ssl certificates arent about to expire

**Spec:**
```
Type:       Scheduled script (certificate expiry check)
Features:   - Connect to each domain on port 443 and read the certificate
            - Calculate days until expiry
            - Warn by email when a certificate expires within 14 days
            - Flag hostname mismatches and incomplete chains
            - Print a summary table of all domains
Input:      Text file with one domain per line
Tech stack: Python, ssl and socket modules, smtplib, cron
```

---

## Example 36

**Intent:**
We store customer passport scans. I need them encrypted so even if someone gets the bucket, they can't read them.

**Spec:**
```
Type:       REST API service (encrypted document storage)
Auth:       Staff SSO login with role check
Data model: Document(id, customer_id, type, storage_key, wrapped_data_key, uploaded_at)
            AccessLog(id, document_id -> Document, staff_id, action, accessed_at)
Features:   - Encrypt each file with its own AES-256-GCM data key before upload
            - Wrap data keys with a master key in a key management service
            - Decrypt files only for staff with the documents role
            - Log every view and download
            - Delete documents automatically after the retention period
API:        REST
            POST /documents
            GET  /documents/{id}
            DELETE /documents/{id}
Storage:    S3 (ciphertext), PostgreSQL (metadata)
Tech stack: Go, AWS KMS, AWS S3, OIDC
```

---

## Example 37

**Intent:**
Webhooks from our app to customers sometimes fail. I want a reliable outgoing webhook system with retries.

**Spec:**
```
Type:       REST API service (outgoing webhook delivery)
Auth:       Internal service token; HMAC signatures on outgoing requests
Data model: Endpoint(id, customer_id, url, secret, event_types, active)
            Delivery(id, endpoint_id -> Endpoint, event_type, payload_json, status, attempts, next_attempt_at)
Features:   - Accept events from internal services and fan them out to subscribed endpoints
            - Sign each payload with the endpoint secret
            - Retry failed deliveries with exponential backoff for up to 3 days
            - Disable endpoints after repeated failures and email the customer
            - Let customers view and resend recent deliveries
API:        REST
            POST /events
            GET  /endpoints/{id}/deliveries
            POST /deliveries/{id}/resend
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix, Oban
```

---

## Example 38

**Intent:**
cron job runner with a web ui so i can see which jobs failed

**Spec:**
```
Type:       Web application (job scheduler)
Auth:       Admin login
Data model: Job(id, name, cron_expression, command, timeout_seconds, enabled)
            JobRun(id, job_id -> Job, started_at, finished_at, exit_code, output_log)
Features:   - Define jobs with cron expressions and shell commands
            - Run jobs on schedule and capture their output
            - Kill jobs that exceed their timeout
            - Show run history with success or failure per job
            - Trigger a job manually from the UI
API:        REST
            GET  /jobs
            POST /jobs
            POST /jobs/{id}/run
            GET  /jobs/{id}/runs
Storage:    SQLite
Tech stack: Go, robfig/cron, htmx
```

---

## Example 39

**Intent:**
I sell online courses and want to make sure the same account isn't shared by 10 people. Can we limit how many devices can be logged in?

**Spec:**
```
Type:       REST API service (device session limiting)
Auth:       Email + password login with JWT access tokens
Data model: User(id, email, password_hash, max_devices)
            Session(id, user_id -> User, device_fingerprint, user_agent, ip, last_active_at)
Features:   - Register a session per device at login
            - Block login when the device limit is reached
            - Let users see and sign out their active devices
            - Expire sessions inactive for 30 days
            - Flag accounts with logins from many countries in one day
API:        REST
            POST /login
            GET  /sessions
            DELETE /sessions/{id}
Storage:    PostgreSQL, Redis (active sessions)
Tech stack: PHP, Laravel, Laravel Sanctum
```

---

## Example 40

**Intent:**
sitemap generator that crawls my site

**Spec:**
```
Type:       Command-line tool (sitemap generator)
Features:   - Crawl all internal links starting from the home page
            - Respect robots.txt and a max depth option
            - Skip URLs with noindex or non-200 status
            - Write sitemap.xml with last-modified dates
            - Split into multiple sitemaps above 50,000 URLs
Input:      Start URL, optional max depth and output path
Tech stack: Python, httpx, BeautifulSoup
```

---

## Example 41

**Intent:**
hi, i am working in small logistic company, we need to know the distance and drive time between many warehouses and customers, for planning. please help

**Spec:**
```
Type:       REST API service (distance matrix)
Auth:       API key
Data model: Location(id, name, latitude, longitude, type)
            DistanceCache(origin_id -> Location, destination_id -> Location, distance_km, duration_min, computed_at)
Features:   - Store warehouses and customer locations
            - Compute driving distance and time for many origin and destination pairs
            - Cache results and refresh them monthly
            - Export the matrix as CSV for planning
API:        REST
            POST /locations
            POST /matrix
            GET  /matrix/export.csv
Storage:    PostgreSQL
Tech stack: Python, FastAPI, OSRM routing engine (self-hosted)
```

---

## Example 42

**Intent:**
An API that tells me if an email address is real before I add it to my mailing list.

**Spec:**
```
Type:       REST API service (email validation)
Auth:       API key
Features:   - Check email syntax against RFC 5322
            - Look up MX records for the domain
            - Detect disposable email providers from a block list
            - Flag role addresses like info@ and admin@
            - Return a verdict of valid, risky or invalid with reasons
API:        REST
            GET  /validate?email={address}
            POST /validate/bulk
Storage:    Redis (DNS lookup cache)
Tech stack: Node.js, Fastify, dns module
```

---

## Example 43

**Intent:**
staging server that copies production every night but with fake customer data

**Spec:**
```
Type:       Scheduled script (staging data refresh)
Features:   - Dump the production database every night
            - Replace names, emails, phones and addresses with fake values
            - Keep foreign keys and data shapes intact
            - Restore the anonymized dump into the staging database
            - Notify the team when the refresh is done
Input:      Production and staging connection strings, anonymization rules file
Tech stack: Bash, pg_dump, pg_restore, Python Faker
```

---

## Example 44

**Intent:**
We have five microservices and I want to know which version of each is running in each environment, on one page.

**Spec:**
```
Type:       Web application (deployment inventory)
Auth:       Company SSO login
Data model: Service(id, name, repo_url)
            Environment(id, name)
            Deployment(id, service_id -> Service, environment_id -> Environment, version, commit_sha, deployed_by, deployed_at)
Features:   - Record a deployment from a CI pipeline call
            - Show a grid of services by environments with current versions
            - Highlight services where staging is ahead of production
            - Link each version to its commit
            - Show deployment history per service
API:        REST
            POST /deployments
            GET  /services
            GET  /services/{id}/deployments
Storage:    PostgreSQL
Tech stack: Python, Flask, Jinja templates
```

---

## Example 45

**Intent:**
tiny pastebin for my team, code snippets with syntax highlight, expiring links

**Spec:**
```
Type:       Web application (pastebin)
Data model: Paste(id, slug, content, language, created_at, expires_at, burn_after_read)
Features:   - Create a paste with a language for syntax highlighting
            - Generate a short random URL for each paste
            - Expire pastes after 1 hour, 1 day or 1 week
            - Delete a paste after the first view when burn-after-read is set
            - Show a raw text view
API:        REST
            POST /pastes
            GET  /p/{slug}
            GET  /p/{slug}/raw
Storage:    SQLite
Tech stack: Rust, Axum, syntect
```

---

## Example 46

**Intent:**
Every time someone submits our contact form, we're getting spam. Could you build a small service that checks submissions before they reach us?

**Spec:**
```
Type:       REST API service (form spam filtering)
Data model: Submission(id, name, email, message, ip, spam_score, verdict, created_at)
Features:   - Verify a CAPTCHA token on each submission
            - Score messages with a spam classifier and link counts
            - Rate limit submissions per IP
            - Forward clean submissions to the team inbox
            - Keep rejected submissions for review for 7 days
API:        REST
            POST /contact
            GET  /admin/rejected
Storage:    SQLite
Tech stack: Python, Flask, Cloudflare Turnstile, scikit-learn
```

---

## Example 47

**Intent:**
backend for a "download my data" button

**Spec:**
```
Type:       REST API service (user data export)
Auth:       Logged-in user session
Data model: ExportJob(id, user_id, status, file_key, requested_at, expires_at)
Features:   - Start an export job when the user clicks the button
            - Gather profile, posts, comments and uploads into a ZIP
            - Email a download link when the export is ready
            - Expire the download link after 7 days
            - Allow only one export per user every 24 hours
API:        REST
            POST /me/export
            GET  /me/export/{id}
Storage:    PostgreSQL, S3 (ZIP files)
Tech stack: Ruby on Rails, Sidekiq, Active Storage
```

---

## Example 48

**Intent:**
I use Cloudflare and want to update my DNS records from a YAML file in git instead of clicking in the dashboard.

**Spec:**
```
Type:       Infrastructure setup (DNS as code)
Features:   - Define DNS records for each zone in YAML files
            - Show a diff of planned changes on every pull request
            - Apply changes to Cloudflare when merged to main
            - Refuse to delete records not managed by the config unless forced
Input:      YAML zone files in a Git repository
Tech stack: OctoDNS, Cloudflare API, GitHub Actions
```

---

## Example 49

**Intent:**
want an api that tells me the country and city of an IP adress

**Spec:**
```
Type:       REST API service (IP geolocation)
Features:   - Look up country, region, city and coordinates for an IPv4 or IPv6 address
            - Return the ASN and organization name
            - Update the GeoLite2 database weekly
            - Detect the caller's own IP when none is given
API:        REST
            GET  /ip/{address}
            GET  /ip/me
Storage:    MaxMind GeoLite2 database files
Tech stack: Go, oschwald/geoip2-golang, net/http
```

---

## Example 50

**Intent:**
Our product is used by many companies and each needs its own subdomain and its data kept separate from the others.

**Spec:**
```
Type:       Web application (multi-tenant SaaS foundation)
Auth:       Per-tenant user login (email + password), tenant admin role
Data model: Tenant(id, name, subdomain, plan, created_at)
            User(id, tenant_id -> Tenant, email, password_hash, role)
            Project(id, tenant_id -> Tenant, name)
Features:   - Resolve the tenant from the request subdomain
            - Scope every query by tenant_id with row-level security
            - Let a new company sign up and pick its subdomain
            - Let tenant admins invite and remove users
            - Issue wildcard TLS certificates for all subdomains
API:        REST
            POST /signup
            GET  /projects
            POST /users/invite
Storage:    PostgreSQL with row-level security
Tech stack: TypeScript, Node.js, Express, Prisma
```

---

## Example 51

**Intent:**
log every change to our product prices so we can see the price history

**Spec:**
```
Type:       Data pipeline (change data capture)
Data model: PriceHistory(id, product_id, old_price, new_price, changed_at, source)
Features:   - Read changes from the products table using the database's write-ahead log
            - Keep only events where the price column changed
            - Write each change to a price history table
            - Show a price history chart per product
Storage:    PostgreSQL (source and history table), Kafka (change events)
Tech stack: Debezium, Kafka Connect, Python consumer
```

---

## Example 52

**Intent:**
I'm moving our app from Heroku to our own server. Need it to run with Docker, a database, and auto HTTPS.

**Spec:**
```
Type:       Infrastructure setup (single-server deployment)
Features:   - Containerize the app with a multi-stage Dockerfile
            - Run the app, PostgreSQL and Redis with Docker Compose
            - Terminate HTTPS with automatic Let's Encrypt certificates
            - Deploy by pulling a new image and restarting with no data loss
            - Back up the database volume daily to object storage
Storage:    PostgreSQL (Docker volume)
Tech stack: Docker, Docker Compose, Traefik, restic
```

---

## Example 53

**Intent:**
Store and search millions of server log lines cheaply? We dont need it fast, just searchable for 90 days.

**Spec:**
```
Type:       Data pipeline (log archive)
Features:   - Ship logs from servers as compressed batches every minute
            - Store batches in object storage partitioned by date and host
            - Query logs with SQL over the stored files
            - Delete partitions older than 90 days with a lifecycle rule
Storage:    S3 (Parquet files)
Tech stack: Vector, AWS S3, Amazon Athena
```

---

## Example 54

**Intent:**
podcast rss feed host

**Spec:**
```
Type:       Web application (podcast hosting)
Auth:       Creator login (email + password)
Data model: Podcast(id, owner_id, title, description, artwork_url, category)
            Episode(id, podcast_id -> Podcast, title, audio_url, duration_s, published_at)
            Download(id, episode_id -> Episode, ip_hash, user_agent, downloaded_at)
Features:   - Upload episode audio and artwork
            - Generate an RSS feed that passes Apple Podcasts validation
            - Serve audio through a CDN with byte-range support
            - Count unique downloads per episode
            - Schedule episodes to publish at a future time
API:        REST
            GET  /feeds/{podcast_id}.xml
            POST /podcasts/{id}/episodes
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, Django, Bunny CDN
```

---

## Example 55

**Intent:**
can you make me a thing that watches a folder on our ftp server and imports new csv orders into our database

**Spec:**
```
Type:       Scheduled script (SFTP import)
Features:   - Poll the SFTP folder every 10 minutes for new CSV files
            - Validate each row against the expected columns
            - Insert valid orders and skip duplicates by order number
            - Move processed files to an archive folder
            - Email a report of rejected rows
Input:      SFTP host and credentials, target folder, database URL
Tech stack: Python, paramiko, pandas, SQLAlchemy
```

---

## Example 56

**Intent:**
For our hackathon we need a service that issues short-lived download links for big dataset files.

**Spec:**
```
Type:       REST API service (signed download links)
Auth:       Participant login via email magic link
Data model: Dataset(id, name, storage_key, size_bytes)
            DownloadGrant(id, dataset_id -> Dataset, user_email, expires_at, used_count)
Features:   - List datasets available to participants
            - Issue a pre-signed URL valid for 15 minutes
            - Limit downloads per participant per dataset
            - Log who downloaded what and when
API:        REST
            GET  /datasets
            POST /datasets/{id}/link
Storage:    PostgreSQL, Google Cloud Storage
Tech stack: Python, FastAPI, google-cloud-storage
```

---

## Example 57

**Intent:**
My band sells tickets through a few different websites. I'd love one place that pulls in all the sales so I know how many seats are left.

**Spec:**
```
Type:       Web application (ticket sales aggregator)
Auth:       Band manager login
Data model: Event(id, venue, date, capacity)
            Channel(id, name, api_credentials_ref)
            Sale(id, event_id -> Event, channel_id -> Channel, external_order_id, quantity, sold_at)
Features:   - Pull new sales from each ticket platform every 15 minutes
            - Deduplicate sales by external order ID
            - Show seats sold per channel and seats remaining
            - Alert when an event reaches 90% capacity
API:        REST
            GET  /events/{id}/summary
            POST /channels/{id}/sync
Storage:    PostgreSQL
Tech stack: Python, Django, Celery beat
```

---

## Example 58

**Intent:**
honeypot ssh server that logs what attackers type

**Spec:**
```
Type:       Infrastructure setup (SSH honeypot)
Data model: Session(id, source_ip, username_tried, password_tried, started_at, ended_at)
            Command(id, session_id -> Session, input, entered_at)
Features:   - Expose a fake SSH service on port 22 of an isolated VM
            - Record login attempts and commands typed
            - Save files that attackers try to download
            - Show top source IPs and passwords on a dashboard
Storage:    Elasticsearch
Tech stack: Cowrie, Elasticsearch, Kibana, Docker
```

---

## Example 59

**Intent:**
I want our app to show nice previews when people paste a link, like the title, image and description.

**Spec:**
```
Type:       REST API service (link preview)
Features:   - Fetch the URL with a short timeout and size limit
            - Extract Open Graph and Twitter Card tags
            - Fall back to the HTML title and first image
            - Block requests to private IP ranges to prevent SSRF
            - Cache previews for 24 hours
API:        REST
            GET  /preview?url={link}
Storage:    Redis (cache)
Tech stack: Node.js, Fastify, open-graph-scraper
```

---

## Example 60

**Intent:**
nightly copy of our s3 bucket to a different cloud just in case

**Spec:**
```
Type:       Scheduled script (cross-cloud bucket replication)
Features:   - Sync new and changed objects from AWS S3 to Backblaze B2 every night
            - Keep deleted objects in the copy for 30 days
            - Verify checksums after transfer
            - Report bytes transferred and errors by email
Input:      Source and destination bucket names, credentials from environment variables
Tech stack: rclone, cron, Bash
```

---

## Example 61

**Intent:**
Build a service that converts Word and PowerPoint files to PDF for our document portal.

**Spec:**
```
Type:       REST API service (document conversion)
Auth:       Internal API token
Data model: Conversion(id, original_name, input_format, status, output_key, created_at)
Features:   - Accept .docx, .xlsx and .pptx uploads up to 50 MB
            - Convert to PDF with LibreOffice in headless mode
            - Run conversions in isolated worker containers with a timeout
            - Return the PDF or an error describing the failure
API:        REST
            POST /convert
            GET  /conversions/{id}
Storage:    MinIO (input and output files), PostgreSQL
Tech stack: Python, FastAPI, LibreOffice, Docker
```

---

## Example 62

**Intent:**
backend for a smart doorbell that sends a photo to my phone when someone rings

**Spec:**
```
Type:       IoT system (smart doorbell)
Auth:       Device certificate; user login in the mobile app
Data model: Device(id, owner_id, name, firmware_version)
            RingEvent(id, device_id -> Device, image_url, rang_at)
Features:   - Capture a photo on button press on the ESP32 camera
            - Publish the event and image to the cloud over MQTT with TLS
            - Send a push notification with the photo to the owner's phone
            - Keep a history of rings for 30 days
Storage:    S3 (photos), DynamoDB (events)
Tech stack: ESP32-CAM, AWS IoT Core, AWS Lambda, Firebase Cloud Messaging
```

---

## Example 63

**Intent:**
I'd like a shared clipboard between my laptop and phone through my own server.

**Spec:**
```
Type:       Web application (self-hosted clipboard sync)
Auth:       Single user token stored on each device
Data model: ClipItem(id, device_name, content_type, content, created_at)
Features:   - Push text or an image from any device
            - Show new items instantly on other devices over WebSockets
            - Keep the last 50 items
            - Encrypt items end-to-end with a shared passphrase
API:        REST
            POST /clips
            GET  /clips
            WS   /ws
Storage:    SQLite
Tech stack: Go, gorilla/websocket, PWA frontend
```

---

## Example 64

**Intent:**
handle unsubscribe links for all our marketing emails in one place

**Spec:**
```
Type:       REST API service (unsubscribe management)
Data model: Contact(id, email)
            Topic(id, name)
            Preference(contact_id -> Contact, topic_id -> Topic, subscribed, updated_at)
Features:   - Generate signed unsubscribe links per contact and topic
            - Support one-click List-Unsubscribe POST requests
            - Show a preference page to opt out of single topics
            - Expose a check endpoint for senders before each campaign
API:        REST
            GET  /u/{token}
            POST /u/{token}
            GET  /contacts/{email}/preferences
Storage:    PostgreSQL
Tech stack: Python, Flask, itsdangerous
```

---

## Example 65

**Intent:**
I made a desktop app and want to sell it. Need license keys that the app checks online, max 2 computers per key.

**Spec:**
```
Type:       REST API service (software licensing)
Auth:       Admin login for the dashboard; license key in activation requests
Data model: License(id, key, customer_email, product, max_activations, revoked)
            Activation(id, license_id -> License, machine_fingerprint, activated_at, last_check_at)
Features:   - Generate signed license keys after purchase
            - Activate a key on a machine and refuse beyond 2 machines
            - Let customers deactivate an old machine
            - Return a signed offline token valid for 14 days
            - Revoke keys after refunds
API:        REST
            POST /licenses/activate
            POST /licenses/deactivate
            POST /licenses/validate
Storage:    PostgreSQL
Tech stack: Go, Ed25519 signatures, Gin
```

---

## Example 66

**Intent:**
auto update server for my electron app

**Spec:**
```
Type:       REST API service (app update server)
Auth:       Admin token for publishing releases
Data model: Release(id, version, channel, platform, file_url, sha512, notes, published_at)
Features:   - Publish a release with files for Windows, macOS and Linux
            - Return the latest version for a platform and channel
            - Serve update manifests in the format electron-updater expects
            - Roll out a release to a percentage of clients
            - Pull a broken release so clients stop updating to it
API:        REST
            GET  /update/{platform}/{channel}/latest.yml
            POST /releases
            PATCH /releases/{id}
Storage:    PostgreSQL, S3 (installers)
Tech stack: Node.js, Express, electron-updater
```

---

## Example 67

**Intent:**
Collect crash reports from our game when it crashes on players' PCs and group the same crashes together.

**Spec:**
```
Type:       REST API service (crash reporting)
Data model: CrashGroup(id, signature, first_seen, last_seen, count, status)
            CrashReport(id, group_id -> CrashGroup, game_version, os, gpu, minidump_key, received_at)
Features:   - Receive minidumps uploaded by the game's crash handler
            - Symbolicate stack traces using uploaded debug symbols
            - Group reports by the top frames of the stack
            - Show crash counts per game version
            - Mark crash groups as fixed in a version
API:        REST
            POST /crashes
            POST /symbols
            GET  /groups?version={v}
Storage:    PostgreSQL, S3 (minidumps and symbols)
Tech stack: Python, FastAPI, Breakpad minidump_stackwalk
```

---

## Example 68

**Intent:**
we want to A/B test two checkout pages and each user always sees the same one

**Spec:**
```
Type:       REST API service (A/B test assignment)
Data model: Experiment(id, key, variants_json, traffic_percent, status)
            Assignment(experiment_id -> Experiment, user_id, variant, assigned_at)
            Conversion(id, experiment_id -> Experiment, user_id, event, occurred_at)
Features:   - Assign users to variants with a deterministic hash of user ID and experiment key
            - Return the same variant on every request
            - Record conversion events per experiment
            - Compute conversion rate and significance per variant
API:        REST
            GET  /experiments/{key}/assignment?user={id}
            POST /experiments/{key}/conversions
            GET  /experiments/{key}/results
Storage:    PostgreSQL
Tech stack: Kotlin, Ktor, Exposed
```

---

## Example 69

**Intent:**
Before launch I want a waitlist page where people sign up, get a referral link, and move up the list when friends join.

**Spec:**
```
Type:       Web application (referral waitlist)
Data model: Signup(id, email, referral_code, referred_by_id -> Signup, position, confirmed, created_at)
Features:   - Collect emails and send a confirmation link
            - Give each confirmed signup a unique referral link
            - Move a person up 5 places for each confirmed referral
            - Show each person their current position
            - Export the list as CSV for launch invites
API:        REST
            POST /signup
            GET  /confirm/{token}
            GET  /position/{referral_code}
Storage:    PostgreSQL
Tech stack: TypeScript, SvelteKit, Drizzle ORM, Resend
```

---

## Example 70

**Intent:**
look up sales tax rate by us zip code api

**Spec:**
```
Type:       REST API service (sales tax lookup)
Auth:       API key
Data model: TaxRate(zip_code, state, county, city, combined_rate, effective_from)
Features:   - Return the combined state, county and city sales tax rate for a ZIP code
            - Break down the rate by jurisdiction
            - Calculate tax for an amount
            - Import updated rate tables monthly
API:        REST
            GET  /rates/{zip}
            GET  /calculate?zip={zip}&amount={value}
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core minimal API, Entity Framework Core
```

---

## Example 71

**Intent:**
We ship parcels with three couriers. I'd like one API that asks all of them for a price and returns the cheapest.

**Spec:**
```
Type:       REST API service (shipping rate comparison)
Auth:       API key
Data model: Carrier(id, name, credentials_ref, enabled)
            Quote(id, carrier_id -> Carrier, service, price_cents, transit_days, requested_at)
Features:   - Accept parcel weight, dimensions and addresses
            - Request rates from each courier API in parallel
            - Normalize prices and delivery estimates to one format
            - Return quotes sorted by price
            - Skip couriers that time out after 3 seconds
API:        REST
            POST /quotes
            GET  /carriers
Storage:    PostgreSQL (quote log)
Tech stack: Node.js, TypeScript, Fastify, axios
```

---

## Example 72

**Intent:**
I sell the same stuff on Etsy and on my own shop, and keep overselling. Keep the stock numbers in sync please.

**Spec:**
```
Type:       Scheduled script (inventory sync)
Data model: Product(id, sku, title, quantity)
            ChannelListing(id, product_id -> Product, channel, external_id, last_synced_qty)
Features:   - Pull new orders from both shops every 5 minutes
            - Subtract sold quantities from the master stock
            - Push updated quantities to both shops
            - Mark listings sold out when stock reaches zero
            - Log every stock change with its source
Storage:    SQLite
Tech stack: Python, Etsy Open API v3, WooCommerce REST API
```

---

## Example 73

**Intent:**
turn photos of receipts into data, amount date and shop name

**Spec:**
```
Type:       REST API service (receipt OCR)
Auth:       API key
Data model: Receipt(id, image_key, merchant, total, currency, purchase_date, confidence, created_at)
Features:   - Accept a receipt photo upload
            - Correct rotation and perspective of the image
            - Run OCR and extract merchant, date, total and currency
            - Return a confidence score per field
            - Store results for later review
API:        REST
            POST /receipts
            GET  /receipts/{id}
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, FastAPI, OpenCV, Tesseract OCR
```

---

## Example 74

**Intent:**
Could you make a service that turns our recorded meetings into text? We use Zoom, the recordings are in the cloud.

**Spec:**
```
Type:       Webhook service (meeting transcription)
Data model: Recording(id, zoom_meeting_id, topic, duration_s, audio_key, status)
            Transcript(id, recording_id -> Recording, text, segments_json, language)
Features:   - Receive the recording.completed webhook from Zoom
            - Download the audio file from Zoom cloud recordings
            - Transcribe with speaker timestamps
            - Save the transcript and make it searchable
            - Email the host a link when it is ready
API:        REST
            POST /webhooks/zoom
            GET  /transcripts/{id}
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, FastAPI, faster-whisper, Zoom API
```

---

## Example 75

**Intent:**
calendar feed of our team's holidays that people can subscribe to in outlook or google

**Spec:**
```
Type:       Web application (iCalendar feed)
Auth:       Employee login; secret token in feed URL
Data model: Employee(id, name, email, feed_token)
            Absence(id, employee_id -> Employee, start_date, end_date, type)
Features:   - Let employees enter their holidays
            - Generate an .ics feed with all-day events for each absence
            - Give each person a private subscription URL
            - Regenerate a feed token if the URL leaks
API:        REST
            POST /absences
            GET  /calendar/{token}.ics
Storage:    PostgreSQL
Tech stack: Python, Flask, icalendar
```

---

## Example 76

**Intent:**
I follow a lot of blogs. I want new posts from their RSS feeds sent to me as one email every morning.

**Spec:**
```
Type:       Scheduled script (RSS email digest)
Data model: Feed(id, url, title)
            SeenItem(feed_id -> Feed, guid, seen_at)
Features:   - Fetch all feeds every morning at 6:00
            - Collect posts not sent before
            - Render a digest email grouped by blog
            - Send it through SMTP
            - Remove feeds that fail for 7 days in a row and report them
Input:      OPML file with feed URLs, SMTP settings
Storage:    SQLite
Tech stack: Python, feedparser, Jinja2, smtplib
```

---

## Example 77

**Intent:**
need a request bin to see what webhooks third parties are sending me

**Spec:**
```
Type:       Web application (webhook inspector)
Data model: Bin(id, slug, created_at, expires_at)
            CapturedRequest(id, bin_id -> Bin, method, path, headers_json, body, received_at)
Features:   - Create a bin with a unique URL
            - Capture any HTTP method sent to the bin
            - Show headers, query string and body live in the browser
            - Replay a captured request to another URL
            - Delete bins after 48 hours
API:        REST
            POST /bins
            ANY  /b/{slug}
            GET  /bins/{slug}/requests
Storage:    Redis
Tech stack: Node.js, Express, Server-Sent Events, Vue
```

---

## Example 78

**Intent:**
We wrote an OpenAPI file but the backend isn't done. Can the frontend team get a fake server that answers with example data?

**Spec:**
```
Type:       Command-line tool (OpenAPI mock server)
Features:   - Load an OpenAPI 3 YAML or JSON file
            - Serve every path and method defined in it
            - Return response examples or generate fake data from schemas
            - Validate incoming requests and return 400 on mismatches
            - Reload when the spec file changes
Input:      Path to an OpenAPI file, port number
Tech stack: TypeScript, Node.js, Express, json-schema-faker
```

---

## Example 79

**Intent:**
render our transactional emails from templates so marketing can edit them without devs

**Spec:**
```
Type:       Web application (email template service)
Auth:       Staff login with editor and viewer roles
Data model: Template(id, key, subject, mjml_source, version, published)
            TemplateVersion(id, template_id -> Template, mjml_source, created_by, created_at)
Features:   - Edit templates in MJML with a live preview
            - Use variables like {{first_name}} with sample data
            - Publish a version and keep older versions for rollback
            - Render a template with variables to HTML via API
            - Send a test email to yourself
API:        REST
            POST /render/{key}
            GET  /templates
            POST /templates/{id}/publish
Storage:    PostgreSQL
Tech stack: Node.js, MJML, Handlebars, React
```

---

## Example 80

**Intent:**
SSH keys are a mess on our 40 servers. I'd like engineers to get short-lived SSH certificates after logging in with Google.

**Spec:**
```
Type:       Infrastructure setup (SSH certificate authority)
Auth:       Google Workspace OIDC login
Features:   - Run an SSH certificate authority that signs user keys
            - Issue certificates valid for 8 hours after OIDC login
            - Put the engineer's group in the certificate principals
            - Configure servers to trust only the CA
            - Log every certificate issued
Tech stack: Smallstep step-ca, OpenSSH, Ansible
```

---

## Example 81

**Intent:**
bastion host so devs can reach private databases

**Spec:**
```
Type:       Infrastructure setup (bastion host)
Auth:       SSH keys plus MFA through the identity provider
Features:   - Place a hardened jump host in the public subnet
            - Allow SSH only from the office and VPN IP ranges
            - Forward ports to private database hosts
            - Record sessions for audit
            - Auto-patch the host weekly
Tech stack: AWS EC2, Terraform, Teleport
```

---

## Example 82

**Intent:**
Every month our cloud bill surprises us. I want a weekly email that says what each team spent and what grew the most.

**Spec:**
```
Type:       Scheduled script (cloud cost report)
Features:   - Pull last week's costs grouped by the team tag
            - Compare with the previous week and flag increases over 20%
            - List the top 10 most expensive services
            - Report untagged spend separately
            - Email an HTML report to team leads
Input:      AWS credentials, team-to-email mapping file
Tech stack: Python, boto3 (Cost Explorer API), Jinja2
```

---

## Example 83

**Intent:**
find and delete old unused stuff in our aws account, like unattached disks and old snapshots

**Spec:**
```
Type:       Command-line tool (cloud resource cleanup)
Features:   - List unattached EBS volumes, old snapshots and idle load balancers
            - Find Elastic IPs not attached to anything
            - Estimate monthly savings for each resource
            - Run in dry-run mode by default
            - Delete selected resources after confirmation
Input:      AWS profile, region list, age threshold in days
Tech stack: Python, boto3, Click, rich
```

---

## Example 84

**Intent:**
We have a rule that every cloud resource must have owner and cost-center tags. Check it daily and nag people.

**Spec:**
```
Type:       Scheduled script (tag compliance)
Features:   - Scan resources in all accounts and regions daily
            - Find resources missing owner or cost-center tags
            - Group violations by the creator from CloudTrail
            - Message each creator with their untagged resources
            - Write a compliance percentage to a dashboard
Input:      List of AWS accounts and required tag keys
Tech stack: Python, boto3, AWS Config, Slack API
```

---

## Example 85

**Intent:**
generate an SBOM for each release and check the dependencies' licenses

**Spec:**
```
Type:       Command-line tool (SBOM and license check)
Features:   - Generate a CycloneDX SBOM from the project's lock files
            - Read the license of each dependency
            - Fail when a dependency uses a license on the deny list like AGPL
            - Attach the SBOM to the release artifacts
Input:      Project directory, allowed and denied license lists
Tech stack: Syft, Grype, Python script, GitHub Releases
```

---

## Example 86

**Intent:**
Someone changed things in our cloud by hand and Terraform doesn't know. I want to catch that every night.

**Spec:**
```
Type:       Scheduled script (infrastructure drift detection)
Features:   - Run terraform plan for every workspace every night
            - Parse the plan for resources that differ from the code
            - Open an issue listing drifted resources per workspace
            - Close the issue when drift is resolved
Input:      List of Terraform workspace directories
Tech stack: Terraform, Bash, GitHub Actions scheduled workflow, GitHub CLI
```

---

## Example 87

**Intent:**
too many db connections from our app, the database falls over at peak times

**Spec:**
```
Type:       Infrastructure setup (database connection pooling)
Features:   - Put a connection pooler between the app servers and PostgreSQL
            - Use transaction pooling mode with a fixed pool size
            - Route read-only queries to a read replica
            - Expose pool metrics for wait time and active connections
            - Set statement timeouts to kill runaway queries
Storage:    PostgreSQL primary and read replica
Tech stack: PgBouncer, PostgreSQL, Prometheus postgres_exporter
```

---

## Example 88

**Intent:**
I want our own S3-like storage on our servers because of data rules in our country.

**Spec:**
```
Type:       Infrastructure setup (self-hosted object storage)
Auth:       Access keys per application with bucket policies
Features:   - Deploy a 4-node distributed object store with erasure coding
            - Expose an S3-compatible API over HTTPS
            - Enable versioning and object locking for important buckets
            - Replicate buckets to a second data center
            - Monitor disk health and capacity
Storage:    Local disks on 4 servers
Tech stack: MinIO, Kubernetes, Prometheus
```

---

## Example 89

**Intent:**
Before Black Friday I need to know how many users our shop can handle. Simulate lots of people browsing and buying.

**Spec:**
```
Type:       Command-line script (load testing)
Features:   - Simulate users who browse, add to cart and check out
            - Ramp up from 10 to 2,000 virtual users over 20 minutes
            - Measure response time percentiles and error rates per step
            - Stop the test when error rate passes 5%
            - Export an HTML report
Input:      Target base URL, user scenarios, ramp profile
Tech stack: k6, JavaScript, Grafana
```

---

## Example 90

**Intent:**
release new version to 5% of traffic first and auto rollback if errors go up

**Spec:**
```
Type:       Infrastructure setup (canary deployment)
Features:   - Deploy the new version alongside the stable one
            - Send 5% of traffic to the canary, then 25%, 50%, 100%
            - Compare error rate and latency of canary vs stable at each step
            - Roll back automatically when metrics get worse
Tech stack: Kubernetes, Argo Rollouts, Istio, Prometheus
```

---

## Example 91

**Intent:**
Our app keeps deleted users' data forever. I want a nightly job that really deletes records soft-deleted more than 90 days ago.

**Spec:**
```
Type:       Scheduled script (data retention purge)
Features:   - Find rows with deleted_at older than 90 days in each configured table
            - Delete in small batches to avoid long locks
            - Delete related files from object storage
            - Write a purge summary to the audit log
            - Run in dry-run mode with a flag
Input:      Retention rules per table in a YAML file
Tech stack: Python, SQLAlchemy, boto3, Kubernetes CronJob
```

---

## Example 92

**Intent:**
gateway that lets old clients keep using api v1 while we build v2

**Spec:**
```
Type:       REST API service (API versioning gateway)
Features:   - Route requests by version header or /v1 and /v2 path prefix
            - Transform v1 request and response shapes to and from v2
            - Add Deprecation and Sunset headers to v1 responses
            - Count v1 usage per client to plan the shutdown
API:        REST
            ANY  /v1/{path}
            ANY  /v2/{path}
Storage:    Redis (usage counters)
Tech stack: Kong Gateway, Lua plugins
```

---

## Example 93

**Intent:**
generate a changelog page from our merged pull requests every release

**Spec:**
```
Type:       Command-line tool (changelog generator)
Features:   - Collect PRs merged since the last Git tag
            - Group them by labels like feature, fix and breaking
            - Write a Markdown section for the new version
            - Prepend it to CHANGELOG.md and create a GitHub release
Input:      Repository name, new version number, GitHub token
Tech stack: Go, GitHub REST API, Cobra
```

---

## Example 94

**Intent:**
Tired of the internet going slow at home. I want to run a speed test every hour and see a graph over weeks.

**Spec:**
```
Type:       Infrastructure setup (home speedtest logger)
Data model: SpeedResult(id, download_mbps, upload_mbps, ping_ms, server, tested_at)
Features:   - Run a speed test every hour
            - Store results in a database
            - Show download, upload and ping graphs over time
            - Highlight results below the plan's promised speed
Storage:    SQLite
Tech stack: Docker, Speedtest Tracker, Raspberry Pi
```

---

## Example 95

**Intent:**
block ads for every device on my wifi

**Spec:**
```
Type:       Infrastructure setup (network ad blocking)
Features:   - Run a DNS sinkhole on a Raspberry Pi
            - Load public ad and tracker block lists
            - Set the router's DHCP to hand out the Pi as DNS server
            - Forward allowed queries to an encrypted upstream resolver
            - Show blocked queries per device on a dashboard
Tech stack: Pi-hole, Unbound, Raspberry Pi OS
```

---

## Example 96

**Intent:**
I have a solar inverter with a Modbus port. I want to log its power output and see it on my phone.

**Spec:**
```
Type:       IoT system (solar monitoring)
Data model: InverterReading(timestamp, pv_power_w, grid_power_w, battery_soc, daily_yield_kwh)
Features:   - Poll the inverter registers over Modbus TCP every 10 seconds
            - Write readings to a time-series database
            - Show live power and daily yield charts
            - Alert when output drops to zero during daylight
Storage:    InfluxDB
Tech stack: Python, pymodbus, InfluxDB, Grafana
```

---

## Example 97

**Intent:**
We rent out 30 vans. Track where they are with GPS trackers that send their position every minute.

**Spec:**
```
Type:       IoT system (fleet tracking)
Auth:       Staff login; device IMEI whitelist
Data model: Vehicle(id, plate, tracker_imei)
            Position(vehicle_id -> Vehicle, latitude, longitude, speed_kmh, ignition, recorded_at)
            Geofence(id, name, polygon)
Features:   - Receive tracker packets over TCP in the tracker's protocol
            - Show all vans live on a map
            - Replay a van's route for a chosen day
            - Alert when a van leaves a geofence or speeds
API:        REST
            GET  /vehicles
            GET  /vehicles/{id}/positions?date={d}
Storage:    PostgreSQL with PostGIS
Tech stack: Traccar server, Leaflet, PostgreSQL
```

---

## Example 98

**Intent:**
over the air firmware updates for our esp32 sensors in the field

**Spec:**
```
Type:       IoT system (OTA firmware updates)
Auth:       Per-device tokens; signed firmware images
Data model: Device(id, hardware_rev, firmware_version, last_check_at)
            Firmware(id, version, hardware_rev, file_key, signature, rollout_percent)
Features:   - Upload a firmware build with its signature
            - Let devices check for updates on boot and daily
            - Roll out to a percentage of devices
            - Verify the signature on the device before flashing
            - Roll back to the previous partition if the new firmware fails to boot
API:        REST
            GET  /ota/check?device={id}&version={v}
            POST /firmware
Storage:    PostgreSQL, S3 (firmware binaries)
Tech stack: ESP-IDF, Python, FastAPI
```

---

## Example 99

**Intent:**
Farm with soil moisture sensors on LoRaWAN — I want to store the data and get told when a field is too dry.

**Spec:**
```
Type:       IoT system (LoRaWAN soil monitoring)
Data model: Sensor(dev_eui, field_name, depth_cm)
            MoistureReading(dev_eui -> Sensor, moisture_percent, battery_v, received_at)
Features:   - Receive uplinks from the network server via webhook
            - Decode the sensor payload bytes
            - Store readings per field
            - Send an SMS when moisture stays below the threshold for 2 hours
            - Warn when a sensor battery is low
API:        REST
            POST /webhooks/uplink
Storage:    InfluxDB
Tech stack: The Things Stack, Node-RED, InfluxDB, Twilio
```

---

## Example 100

**Intent:**
wake my pc at home from my phone

**Spec:**
```
Type:       Web application (wake-on-LAN)
Auth:       Single password login
Data model: Machine(id, name, mac_address, ip_address)
Features:   - Save computers with their MAC addresses
            - Send a Wake-on-LAN magic packet on button press
            - Ping the machine to show if it is online
            - Reach it from outside through the home VPN
API:        REST
            GET  /machines
            POST /machines/{id}/wake
Storage:    SQLite
Tech stack: Python, Flask, wakeonlan
```

---

## Example 101

**Intent:**
Self-host a password manager for my family that works with the Bitwarden apps.

**Spec:**
```
Type:       Infrastructure setup (self-hosted password manager)
Auth:       Per-user master password with 2FA
Features:   - Run a Bitwarden-compatible server in a container
            - Serve it over HTTPS on a subdomain
            - Create an organization to share family logins
            - Disable public signups after accounts are made
            - Back up the vault database nightly with encryption
Storage:    SQLite (vault data)
Tech stack: Vaultwarden, Docker Compose, Caddy, restic
```

---

## Example 102

**Intent:**
nextcloud on my own server instead of google drive

**Spec:**
```
Type:       Infrastructure setup (self-hosted file cloud)
Auth:       Nextcloud user accounts with TOTP
Features:   - Install Nextcloud with a database and cache
            - Sync files with desktop and phone clients
            - Share folders with links that expire
            - Run background jobs with cron
            - Encrypt backups and store them offsite
Storage:    MariaDB, Redis, local disk
Tech stack: Nextcloud, Docker Compose, Nginx, Let's Encrypt
```

---

## Example 103

**Intent:**
I'd like to run my own email server for my domain, but I'm worried mails will go to spam.

**Spec:**
```
Type:       Infrastructure setup (self-hosted mail server)
Auth:       IMAP and SMTP login per mailbox
Features:   - Install SMTP, IMAP and webmail on a VPS
            - Set SPF, DKIM and DMARC DNS records
            - Set reverse DNS for the server IP
            - Filter incoming spam
            - Use TLS for all mail connections
Storage:    Local Maildir storage
Tech stack: Mailcow, Docker, Postfix, Dovecot, Rspamd
```

---

## Example 104

**Intent:**
k3s cluster on 3 raspberry pis for learning kubernetes

**Spec:**
```
Type:       Infrastructure setup (home Kubernetes cluster)
Features:   - Install a lightweight Kubernetes distribution on three Raspberry Pi 5 boards
            - Use one node as server and two as agents
            - Provide persistent volumes with distributed storage
            - Expose services with a load balancer on the home network
            - Deploy apps from a Git repository
Tech stack: k3s, Longhorn, MetalLB, Flux CD, Ansible
```

---

## Example 105

**Intent:**
I got a second-hand server with 64GB RAM. I want to run lots of virtual machines and containers on it and manage them from a browser.

**Spec:**
```
Type:       Infrastructure setup (home lab virtualization)
Auth:       Web UI login with TOTP
Features:   - Install a hypervisor on bare metal
            - Create VMs and lightweight Linux containers from templates
            - Use ZFS storage with snapshots before changes
            - Back up VMs weekly to a separate backup server
            - Put management on its own VLAN
Storage:    ZFS pool on local SSDs
Tech stack: Proxmox VE, Proxmox Backup Server, ZFS
```

---

## Example 106

**Intent:**
one login page in front of all my homelab apps

**Spec:**
```
Type:       Infrastructure setup (single sign-on reverse proxy)
Auth:       Username + password with TOTP or WebAuthn
Features:   - Route each app subdomain through a reverse proxy
            - Require login before any app is reached
            - Allow some paths like APIs to bypass with tokens
            - Remember logins for 7 days across subdomains
            - Get wildcard certificates with a DNS challenge
Storage:    SQLite (users and sessions)
Tech stack: Traefik, Authelia, Docker Compose, Cloudflare DNS
```

---

## Example 107

**Intent:**
minecraft server for my kids and their friends that backs itself up

**Spec:**
```
Type:       Infrastructure setup (game server hosting)
Auth:       Whitelist of player accounts
Features:   - Run a Minecraft Java server in a container
            - Allow only whitelisted players
            - Back up the world every 6 hours and keep 7 days
            - Restart nightly and update to the newest version
            - Shut down when nobody has played for 30 minutes
Storage:    Docker volume (world files)
Tech stack: itzg/minecraft-server image, Docker Compose, cron
```

---

## Example 108

**Intent:**
Our team wants a chat server we host ourselves, encrypted, not Slack.

**Spec:**
```
Type:       Infrastructure setup (self-hosted chat)
Auth:       Accounts through the company OIDC provider
Features:   - Run a Matrix homeserver for the company domain
            - Enable end-to-end encrypted rooms by default
            - Provide a web client on a subdomain
            - Disable federation with outside servers
            - Purge media older than one year
Storage:    PostgreSQL, local media store
Tech stack: Synapse, Element Web, PostgreSQL, Nginx
```

---

## Example 109

**Intent:**
when power goes out my UPS has 10 minutes. shut down my NAS and servers cleanly before battery dies

**Spec:**
```
Type:       Infrastructure setup (UPS shutdown)
Features:   - Connect the UPS by USB to one server running the UPS daemon
            - Share UPS status over the network to other machines
            - Start shutdown on all machines when battery drops under 40%
            - Send a notification when power fails and returns
            - Power machines back on when mains returns
Tech stack: Network UPS Tools (NUT), Proxmox, Synology DSM
```

---

## Example 110

**Intent:**
connect my laptop, my parents' house and my vps into one private network without opening ports

**Spec:**
```
Type:       Infrastructure setup (mesh VPN)
Auth:       Device keys approved by an admin
Features:   - Install a mesh VPN client on each device
            - Give each device a stable private IP and hostname
            - Use one machine as subnet router for the parents' LAN
            - Use the VPS as exit node when travelling
            - Restrict which devices can reach which with ACLs
Tech stack: Headscale (self-hosted control server), Tailscale clients
```

---

## Example 111

**Intent:**
I have smart plugs on my fridge, washing machine and PC. I want to see how much electricity each uses per month.

**Spec:**
```
Type:       IoT system (home energy monitoring)
Data model: Plug(id, name, ip_address)
            PowerSample(plug_id -> Plug, watts, total_kwh, sampled_at)
Features:   - Read power from each smart plug over the local API every 30 seconds
            - Store readings in a time-series database
            - Show kWh per device per day and month
            - Estimate cost using the electricity price
Storage:    InfluxDB
Tech stack: Shelly plugs, Home Assistant, InfluxDB, Grafana
```

---

## Example 112

**Intent:**
my school has a small weather station on the roof, i want the data on a public website

**Spec:**
```
Type:       IoT system (weather station)
Data model: Observation(station_id, temperature_c, humidity, pressure_hpa, wind_kmh, rain_mm, observed_at)
Features:   - Read sensors with a Raspberry Pi every minute
            - Send observations to the server over HTTPS
            - Show current conditions and 24-hour charts on a public page
            - Compute daily min, max and rain totals
            - Export history as CSV
API:        REST
            POST /observations
            GET  /observations/latest
            GET  /observations?from={d}&to={d}
Storage:    PostgreSQL
Tech stack: Python, Raspberry Pi, BME280 sensor, FastAPI, Chart.js
```

---

## Example 113

**Intent:**
Employees should check in at the office automatically with Bluetooth beacons, no app tapping.

**Spec:**
```
Type:       Mobile application with backend (BLE attendance)
Auth:       Company SSO login in the app
Data model: Employee(id, name, email)
            Beacon(id, uuid, major, minor, location)
            Presence(id, employee_id -> Employee, beacon_id -> Beacon, entered_at, left_at)
Features:   - Detect office beacons in the background on the phone
            - Send enter and exit events to the backend
            - Merge short gaps into one presence period
            - Show HR a daily attendance report
API:        REST
            POST /presence/events
            GET  /reports/attendance?date={d}
Storage:    PostgreSQL
Tech stack: React Native, react-native-ble-plx, Node.js, NestJS
```

---

## Example 114

**Intent:**
we never know what devices are on our office network. scan it and keep a list

**Spec:**
```
Type:       Scheduled script (network inventory)
Data model: Device(mac_address, ip_address, hostname, vendor, first_seen, last_seen)
Features:   - Scan the office subnets every hour
            - Identify vendors from MAC address prefixes
            - Record first-seen and last-seen times
            - Alert when an unknown device appears
            - Show the device list on a simple web page
Storage:    SQLite
Tech stack: Python, nmap, python-nmap, Flask
```

---

## Example 115

**Intent:**
Keep track of all our servers — what OS, who owns them, when they were last patched.

**Spec:**
```
Type:       Web application (server inventory / CMDB)
Auth:       Company SSO
Data model: Server(id, hostname, ip, os, os_version, owner_team, environment, last_patched_at)
            Agent(id, server_id -> Server, last_report_at)
Features:   - Collect facts from each server through a small agent
            - Show servers filtered by OS, team and environment
            - Flag servers not patched in 30 days
            - Flag servers running end-of-life OS versions
API:        REST
            POST /agents/report
            GET  /servers
Storage:    PostgreSQL
Tech stack: Go (agent), Django, PostgreSQL
```

---

## Example 116

**Intent:**
set up new developer laptops automatically, same tools and settings for everyone

**Spec:**
```
Type:       Command-line script (laptop provisioning)
Features:   - Install package manager and a list of developer tools
            - Install language runtimes with pinned versions
            - Apply shell, Git and editor configuration
            - Enable disk encryption and firewall
            - Be safe to run again without breaking anything
Input:      Role name (backend, frontend, data)
Tech stack: Ansible, Homebrew, mise
```

---

## Example 117

**Intent:**
api for barcode lookup, give EAN get product name

**Spec:**
```
Type:       REST API service (barcode lookup)
Data model: Product(ean, name, brand, category, image_url, updated_at)
Features:   - Validate the EAN-13 or UPC check digit
            - Look up the product in the local database
            - Query Open Food Facts when not found and cache the result
            - Allow users to submit missing products
API:        REST
            GET  /products/{ean}
            POST /products
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Open Food Facts API
```

---

## Example 118

**Intent:**
I need to know which days are public holidays in each country we operate in, for our shift planning tool.

**Spec:**
```
Type:       REST API service (public holidays)
Data model: Holiday(id, country_code, region_code, date, name, type)
Features:   - Return holidays for a country and year
            - Support regional holidays like German states
            - Check whether a given date is a working day
            - Count working days between two dates
API:        REST
            GET  /holidays/{country}/{year}
            GET  /is-workday?country={c}&date={d}
            GET  /workdays?country={c}&from={d}&to={d}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, holidays library
```

---

## Example 119

**Intent:**
check EU VAT numbers when business customers sign up

**Spec:**
```
Type:       REST API service (VAT number validation)
Data model: VatCheck(id, vat_number, country, valid, company_name, address, consultation_number, checked_at)
Features:   - Validate the VAT number format per country
            - Check the number against the EU VIES service
            - Store the consultation number as proof for tax records
            - Retry later when VIES is unavailable
API:        REST
            GET  /vat/{number}
Storage:    PostgreSQL
Tech stack: PHP, Symfony, SOAP client
```

---

## Example 120

**Intent:**
customers enter phone numbers in every possible format, I want them all cleaned to one format

**Spec:**
```
Type:       REST API service (phone number normalization)
Features:   - Parse numbers with or without country code
            - Use a default country when none is given
            - Return the number in E.164 format
            - Report the number type like mobile or landline
            - Reject invalid numbers with a reason
API:        REST
            POST /phone/normalize
            POST /phone/normalize/bulk
Tech stack: Java, Spring Boot, libphonenumber
```

---

## Example 121

**Intent:**
Our customers type their company name and we want to fill in the registration number and address from the official company register.

**Spec:**
```
Type:       REST API service (company register lookup)
Auth:       API key
Data model: CompanyCache(registry_id, name, status, address, incorporated_on, fetched_at)
Features:   - Search companies by name with autocomplete
            - Fetch full details by registration number
            - Cache results for 7 days
            - Show if a company is dissolved
API:        REST
            GET  /companies/search?q={name}
            GET  /companies/{number}
Storage:    Redis
Tech stack: Node.js, Fastify, UK Companies House API
```

---

## Example 122

**Intent:**
reverse geocoding: coordinates in, street address out. we have millions of points so no paid API please

**Spec:**
```
Type:       Infrastructure setup (self-hosted reverse geocoding)
Features:   - Import OpenStreetMap data for the needed countries
            - Serve reverse geocoding requests over HTTP
            - Process point files in bulk with parallel workers
            - Update the map data monthly
API:        REST
            GET  /reverse?lat={lat}&lon={lon}
Storage:    PostgreSQL with PostGIS (Nominatim database)
Tech stack: Nominatim, Docker, Python bulk client
```

---

## Example 123

**Intent:**
I want to host my own map tiles for our app instead of paying Google Maps.

**Spec:**
```
Type:       Infrastructure setup (self-hosted map tiles)
Features:   - Generate vector tiles from OpenStreetMap extracts
            - Serve tiles over HTTP with caching headers
            - Provide a map style matching our brand colors
            - Put tiles behind a CDN
Storage:    PMTiles file in object storage
Tech stack: Planetiler, PMTiles, MapLibre GL JS, Cloudflare CDN
```

---

## Example 124

**Intent:**
Our 4 delivery drivers each do 30 stops a day. Give each driver the best order of stops.

**Spec:**
```
Type:       REST API service (route optimization)
Auth:       Dispatcher login
Data model: Driver(id, name, start_location, shift_end)
            Stop(id, address, latitude, longitude, time_window_start, time_window_end)
            Route(id, driver_id -> Driver, date, stop_order_json, total_km)
Features:   - Assign stops to drivers balancing workload
            - Order stops to minimize driving time
            - Respect customer time windows and shift end
            - Send each driver a link with the route in maps
API:        REST
            POST /routes/optimize
            GET  /routes/{id}
Storage:    PostgreSQL
Tech stack: Python, Google OR-Tools, OSRM, FastAPI
```

---

## Example 125

**Intent:**
screenshot api - send url, get png of the page

**Spec:**
```
Type:       REST API service (web page screenshots)
Auth:       API key
Features:   - Load the URL in a headless browser
            - Set viewport size, full-page mode and device scale
            - Wait for network idle or a CSS selector
            - Block ads and cookie banners optionally
            - Cache screenshots per URL and options for one hour
API:        REST
            GET  /screenshot?url={url}&width={w}&full_page={bool}
Storage:    S3 (cached images)
Tech stack: Node.js, Playwright, Fastify
```

---

## Example 126

**Intent:**
For every blog post I want a nice social share image made automatically with the title on it.

**Spec:**
```
Type:       REST API service (Open Graph image generation)
Features:   - Render an image 1200x630 from a template with title and author
            - Use the blog's fonts and colors
            - Return PNG with long cache headers
            - Sign URLs so others cannot abuse the service
API:        REST
            GET  /og?title={text}&author={name}&sig={signature}
Tech stack: TypeScript, Vercel Edge Functions, Satori, resvg
```

---

## Example 127

**Intent:**
convert any article url into clean readable text without ads

**Spec:**
```
Type:       REST API service (article extraction)
Features:   - Download the page HTML
            - Extract the main article, title, author and date
            - Remove navigation, ads and comments
            - Return clean HTML, Markdown or plain text
            - Estimate reading time
API:        REST
            GET  /extract?url={link}&format={md|html|text}
Storage:    Redis (cache)
Tech stack: Python, trafilatura, FastAPI
```

---

## Example 128

**Intent:**
We cite a lot of web pages in our research reports and they disappear. Save a permanent copy of each link we use.

**Spec:**
```
Type:       Web application (web page archiving)
Auth:       Team login
Data model: Snapshot(id, url, title, archived_at, warc_key, screenshot_key, pdf_key)
            Citation(id, snapshot_id -> Snapshot, report_name, added_by)
Features:   - Archive a URL as WARC, PDF and screenshot
            - Return a permanent link to the archived copy
            - Re-check original links monthly and mark dead ones
            - Search archives by URL and title
API:        REST
            POST /snapshots
            GET  /snapshots?url={url}
Storage:    PostgreSQL, S3
Tech stack: ArchiveBox, Python, Django
```

---

## Example 129

**Intent:**
check our whole website for broken links every week

**Spec:**
```
Type:       Scheduled script (broken link checker)
Features:   - Crawl every page on the domain
            - Check internal and external links with HEAD requests
            - Report 404s, timeouts and redirect chains
            - List which page contains each broken link
            - Email the report when broken links are found
Input:      Start URL, list of URL patterns to ignore
Tech stack: Python, Scrapy, smtplib
```

---

## Example 130

**Intent:**
I'd like my own dynamic DNS like DynDNS for my domain, because my home IP keeps changing.

**Spec:**
```
Type:       REST API service (dynamic DNS updater)
Auth:       Per-host secret token
Data model: Host(id, hostname, token_hash, current_ip, updated_at)
Features:   - Accept an update call from the router with the new IP
            - Update the A and AAAA records through the DNS provider API
            - Ignore updates when the IP has not changed
            - Support the DynDNS2 protocol used by most routers
API:        REST
            GET  /nic/update?hostname={h}&myip={ip}
Storage:    SQLite
Tech stack: Go, Cloudflare API, net/http
```

---

## Example 131

**Intent:**
give every customer a random email alias that forwards to their real inbox so they can hide their address

**Spec:**
```
Type:       Web application (email alias forwarding)
Auth:       Email + password with 2FA
Data model: User(id, email, password_hash)
            Alias(id, user_id -> User, address, label, enabled, forwarded_count)
Features:   - Create random or custom aliases on our domain
            - Forward incoming mail to the user's real address
            - Let users reply through the alias without revealing their address
            - Disable an alias that gets spam
API:        REST
            GET  /aliases
            POST /aliases
            PATCH /aliases/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, Postfix, SRS rewriting
```

---

## Example 132

**Intent:**
our tests send real emails by mistake. we need a fake mail server for dev that catches everything

**Spec:**
```
Type:       Infrastructure setup (development mail catcher)
Features:   - Run a fake SMTP server in the dev Docker Compose stack
            - Catch all outgoing emails without delivering them
            - Show caught emails in a web UI with HTML and text views
            - Provide an API so tests can check sent emails
Tech stack: Mailpit, Docker Compose
```

---

## Example 133

**Intent:**
When our marketing emails bounce, mark those addresses so we stop sending to them.

**Spec:**
```
Type:       Webhook service (bounce handling)
Data model: Contact(id, email, status, bounce_count)
            BounceEvent(id, contact_id -> Contact, type, reason, received_at)
Features:   - Receive bounce and complaint notifications from the email provider
            - Suppress addresses with hard bounces immediately
            - Suppress after 3 soft bounces in 30 days
            - Suppress addresses that mark mail as spam
            - Expose a suppression check endpoint
API:        REST
            POST /webhooks/ses-notifications
            GET  /suppressions/{email}
Storage:    PostgreSQL
Tech stack: Python, AWS SES, Amazon SNS, Flask
```

---

## Example 134

**Intent:**
small restaurant: when people call, play a menu "press 1 for hours, 2 to book, 3 to talk to someone"

**Spec:**
```
Type:       Webhook service (phone IVR)
Data model: Call(id, caller_number, choice, started_at, duration_s)
Features:   - Answer calls with a recorded greeting
            - Read opening hours on option 1
            - Send a booking link by SMS on option 2
            - Forward to the restaurant phone on option 3
            - Take a voicemail outside opening hours
API:        REST
            POST /voice/incoming
            POST /voice/menu
Storage:    SQLite (call log)
Tech stack: Node.js, Express, Twilio Voice TwiML
```

---

## Example 135

**Intent:**
I'd like an API that tells me when a group of people are all free, checking their Google and Microsoft calendars.

**Spec:**
```
Type:       REST API service (free/busy availability)
Auth:       OAuth 2.0 connection per person
Data model: Person(id, email, provider, refresh_token_encrypted, timezone)
Features:   - Connect Google and Microsoft calendars through OAuth
            - Read free/busy blocks for a date range
            - Find common free slots of a given length within working hours
            - Respect each person's timezone
API:        REST
            POST /connect/{provider}
            POST /availability
Storage:    PostgreSQL
Tech stack: TypeScript, Node.js, Google Calendar API, Microsoft Graph
```

---

## Example 136

**Intent:**
my own caldav and carddav server so contacts and calendars sync between my android and linux pc

**Spec:**
```
Type:       Infrastructure setup (CalDAV/CardDAV server)
Auth:       Basic auth over HTTPS per user
Features:   - Run a CalDAV and CardDAV server
            - Sync calendars and contacts with Android through DAVx5
            - Sync with Thunderbird on Linux
            - Back up the collection folder nightly
Storage:    Local file storage
Tech stack: Radicale, Nginx, Let's Encrypt
```

---

## Example 137

**Intent:**
Match our bank transactions to the invoices in our system so the accountant doesn't do it by hand.

**Spec:**
```
Type:       Web application (payment reconciliation)
Auth:       Finance staff login
Data model: BankTransaction(id, booked_on, amount, currency, counterparty, reference)
            Invoice(id, number, customer, amount, due_date, status)
            Match(id, transaction_id -> BankTransaction, invoice_id -> Invoice, confidence, confirmed_by)
Features:   - Import bank statements in CAMT.053 or CSV format
            - Match transactions by invoice number in reference and amount
            - Suggest fuzzy matches for partial payments
            - Let staff confirm or fix matches
            - Mark matched invoices as paid
API:        REST
            POST /statements/import
            GET  /matches/suggested
            POST /matches/{id}/confirm
Storage:    PostgreSQL
Tech stack: Python, Django, pandas, rapidfuzz
```

---

## Example 138

**Intent:**
We have to send e-invoices to government customers through Peppol now. Help!

**Spec:**
```
Type:       REST API service (e-invoicing)
Auth:       Internal API token
Data model: Invoice(id, number, buyer_peppol_id, total, status, ubl_xml_key)
            TransmissionLog(id, invoice_id -> Invoice, status, message_id, sent_at)
Features:   - Convert internal invoices to UBL 2.1 XML in the Peppol BIS 3.0 format
            - Validate the XML with the official Schematron rules
            - Send it through a Peppol access point
            - Track delivery status and errors
API:        REST
            POST /einvoices
            GET  /einvoices/{id}/status
Storage:    PostgreSQL, S3 (XML files)
Tech stack: Java, Spring Boot, ph-schematron, Peppol access point provider API
```

---

## Example 139

**Intent:**
big retailer sends us orders as EDI files, we need them as normal orders in our system

**Spec:**
```
Type:       Data pipeline (EDI order import)
Data model: EdiMessage(id, sender_id, message_type, control_number, raw_key, status, received_at)
            Order(id, po_number, customer_id, lines_json)
Features:   - Receive X12 850 purchase orders over AS2 or SFTP
            - Parse segments into order headers and lines
            - Create orders in the ERP via its API
            - Send a 997 functional acknowledgment back
            - Alert on parsing errors
Storage:    PostgreSQL, S3 (raw EDI files)
Tech stack: Python, pyx12, Celery
```

---

## Example 140

**Intent:**
generate a product feed for google shopping from our shop database every night

**Spec:**
```
Type:       Scheduled script (product feed generator)
Features:   - Read active products with price, stock and images
            - Map categories to Google product taxonomy IDs
            - Write an XML feed in Google Merchant Center format
            - Skip products missing required fields and log them
            - Upload the feed to a public URL
Input:      Database connection string, category mapping CSV
Tech stack: Python, SQLAlchemy, lxml, AWS S3
```

---

## Example 141

**Intent:**
I sell print-on-demand t-shirts. When an order comes in on my shop, send it to the print company automatically with the design file.

**Spec:**
```
Type:       Webhook service (print-on-demand fulfillment)
Data model: Order(id, shop_order_id, customer_address, status)
            OrderLine(id, order_id -> Order, sku, size, quantity, design_url)
            Fulfillment(id, order_id -> Order, printer_order_id, tracking_number, status)
Features:   - Receive new orders from the shop webhook
            - Map shop SKUs to the printer's product and design IDs
            - Create the order at the print company
            - Update the shop with tracking when the printer ships
API:        REST
            POST /webhooks/shop/order-created
            POST /webhooks/printer/shipped
Storage:    PostgreSQL
Tech stack: Node.js, Express, WooCommerce API, Printful API
```

---

## Example 142

**Intent:**
loyalty points for our coffee shops — earn points with each purchase, redeem for drinks

**Spec:**
```
Type:       REST API service (loyalty points)
Auth:       Customer phone number with SMS code; POS API key
Data model: Member(id, phone, name, points_balance)
            PointsTransaction(id, member_id -> Member, store_id, type, points, reference, created_at)
            Reward(id, name, points_cost)
Features:   - Add points from POS purchases at 1 point per euro
            - Redeem rewards and subtract points atomically
            - Expire points after 12 months of inactivity
            - Show members their balance and history
API:        REST
            POST /members/{id}/earn
            POST /members/{id}/redeem
            GET  /members/{id}
Storage:    PostgreSQL
Tech stack: Go, PostgreSQL, sqlc
```

---

## Example 143

**Intent:**
gift cards api: create, check balance, spend part of it

**Spec:**
```
Type:       REST API service (gift cards)
Auth:       API key for shop systems
Data model: GiftCard(id, code_hash, initial_amount, balance, currency, expires_at, status)
            GiftCardTransaction(id, card_id -> GiftCard, amount, order_id, created_at)
Features:   - Issue gift cards with random 16-character codes
            - Check balance by code
            - Spend part of a balance with a row lock to prevent double spending
            - Refund amounts back to a card
            - Block a card after too many wrong code attempts
API:        REST
            POST /giftcards
            GET  /giftcards/{code}
            POST /giftcards/{code}/redeem
            POST /giftcards/{code}/refund
Storage:    PostgreSQL
Tech stack: Java, Quarkus, Hibernate
```

---

## Example 144

**Intent:**
We run influencer campaigns. Each influencer gets a link and we want to know clicks and sales per person.

**Spec:**
```
Type:       Web application (affiliate tracking)
Auth:       Admin login; influencer login to see their stats
Data model: Affiliate(id, name, code, commission_percent)
            Click(id, affiliate_id -> Affiliate, clicked_at, ip_hash)
            Conversion(id, affiliate_id -> Affiliate, order_id, amount, commission, converted_at)
Features:   - Generate tracking links per affiliate
            - Set a 30-day attribution cookie on click
            - Record conversions from the checkout success page
            - Calculate commissions per month
            - Show each influencer their own dashboard
API:        REST
            GET  /r/{code}
            POST /conversions
            GET  /affiliates/{id}/stats
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Livewire
```

---

## Example 145

**Intent:**
need to keep proof of cookie consent for each visitor for legal reasons

**Spec:**
```
Type:       REST API service (consent logging)
Data model: ConsentRecord(id, visitor_id, policy_version, categories_json, ip_hash, user_agent, recorded_at)
Features:   - Record each consent choice with the policy version shown
            - Store records append-only for 5 years
            - Look up the consent history of a visitor
            - Export records for an audit
API:        REST
            POST /consents
            GET  /consents/{visitor_id}
Storage:    PostgreSQL
Tech stack: Node.js, Hono, Cloudflare Workers, Cloudflare D1
```

---

## Example 146

**Intent:**
Our sales team lives in Salesforce but our product data is in Postgres. Sync account usage numbers into Salesforce every hour.

**Spec:**
```
Type:       Data pipeline (reverse ETL)
Features:   - Query usage metrics per customer account from PostgreSQL
            - Match accounts to Salesforce records by external ID
            - Upsert custom fields like active_users and last_login
            - Send only changed rows to save API calls
            - Log sync errors per record
Storage:    PostgreSQL (source), Salesforce (destination)
Tech stack: Python, simple-salesforce, Airflow
```

---

## Example 147

**Intent:**
use a google sheet as the database for my tiny app, give it a rest api

**Spec:**
```
Type:       REST API service (Google Sheets backend)
Auth:       API key
Features:   - Treat each sheet tab as a table with the header row as fields
            - List, filter, add, update and delete rows
            - Cache reads for 30 seconds to stay under quota
            - Validate column types from a schema config
API:        REST
            GET  /tables/{tab}
            POST /tables/{tab}
            PATCH /tables/{tab}/{row}
            DELETE /tables/{tab}/{row}
Storage:    Google Sheets
Tech stack: Node.js, Express, Google Sheets API (service account)
```

---

## Example 148

**Intent:**
I write in Notion. Can my Notion pages become my blog automatically?

**Spec:**
```
Type:       Scheduled script (Notion to static blog)
Features:   - Read published pages from a Notion database every hour
            - Convert blocks to Markdown with images downloaded locally
            - Build the static site
            - Deploy only when content has changed
Input:      Notion integration token, database ID
Tech stack: Node.js, Notion API, notion-to-md, Astro, Netlify
```

---

## Example 149

**Intent:**
watermark every photo our photographers upload with our logo

**Spec:**
```
Type:       REST API service (image watermarking)
Auth:       Photographer login token
Data model: Photo(id, photographer_id, original_key, watermarked_key, uploaded_at)
Features:   - Accept JPEG and PNG uploads
            - Place the logo in a corner at a set opacity and scale
            - Keep the original private and the watermarked copy public
            - Strip GPS EXIF data from the public copy
API:        REST
            POST /photos
            GET  /photos/{id}
Storage:    S3 (private and public buckets), PostgreSQL
Tech stack: Python, Pillow, FastAPI
```

---

## Example 150

**Intent:**
text to speech api for our e-learning so lessons can be listened to

**Spec:**
```
Type:       REST API service (text-to-speech)
Auth:       API key
Data model: AudioClip(id, text_hash, voice, language, audio_key, duration_s)
Features:   - Convert text to speech in several voices and languages
            - Split long lessons into sentences and join the audio
            - Return MP3 files
            - Reuse audio for identical text and voice
API:        REST
            POST /speech
            GET  /speech/{id}
Storage:    PostgreSQL, S3
Tech stack: Python, Piper TTS, FFmpeg, FastAPI
```

---

## Example 151

**Intent:**
Remove personal info like names, emails, phone numbers from support tickets before we give them to the analytics team.

**Spec:**
```
Type:       REST API service (PII redaction)
Features:   - Detect emails, phone numbers, IBANs and credit card numbers with patterns
            - Detect person names and addresses with a NER model
            - Replace each item with a placeholder like [EMAIL]
            - Optionally keep a consistent fake value per real value
            - Process batches of tickets
API:        REST
            POST /redact
            POST /redact/batch
Tech stack: Python, Microsoft Presidio, spaCy, FastAPI
```

---

## Example 152

**Intent:**
check customer names against sanctions lists when they sign up

**Spec:**
```
Type:       REST API service (sanctions screening)
Auth:       Internal service token
Data model: SanctionEntry(id, list_name, full_name, aliases, birth_date, country)
            ScreeningResult(id, customer_ref, matched_entry_id -> SanctionEntry, score, decision, reviewed_by)
Features:   - Download EU, UN and OFAC sanctions lists daily
            - Fuzzy-match names including aliases and transliterations
            - Return possible matches above a score threshold
            - Let compliance staff clear or confirm matches
API:        REST
            POST /screen
            GET  /results?status=pending
            POST /results/{id}/decision
Storage:    PostgreSQL, Elasticsearch
Tech stack: Python, Django, rapidfuzz, Elasticsearch
```

---

## Example 153

**Intent:**
We have a private Docker images problem: we pay for Docker Hub. Host our own registry instead.

**Spec:**
```
Type:       Infrastructure setup (private container registry)
Auth:       Robot accounts for CI; SSO for people
Features:   - Host private container image repositories by project
            - Scan pushed images for known vulnerabilities
            - Delete untagged images older than 30 days
            - Replicate images to a second region
Storage:    S3-compatible object storage, PostgreSQL
Tech stack: Harbor, Trivy, Kubernetes, Helm
```

---

## Example 154

**Intent:**
private npm registry for our company packages and also cache public ones

**Spec:**
```
Type:       Infrastructure setup (private package registry)
Auth:       Token login per developer
Features:   - Publish scoped packages like @company/ui privately
            - Proxy and cache the public npm registry
            - Restrict publish rights to CI tokens
            - Back up the storage folder daily
Storage:    Local disk
Tech stack: Verdaccio, Docker, Nginx
```

---

## Example 155

**Intent:**
Developers spend a day setting up the project locally. Make it one command.

**Spec:**
```
Type:       Infrastructure setup (local development environment)
Features:   - Define app, database, cache and queue services in Docker Compose
            - Seed the database with realistic sample data
            - Mount source code for hot reload
            - Provide a dev container config for VS Code
            - Add a make setup command that runs everything
Tech stack: Docker Compose, Dev Containers, Makefile, PostgreSQL, Redis
```

---

## Example 156

**Intent:**
script to fill a test database with lots of realistic fake data

**Spec:**
```
Type:       Command-line tool (test data generator)
Features:   - Read the database schema and foreign keys
            - Generate fake values based on column names and types
            - Insert rows in dependency order to keep foreign keys valid
            - Set row counts per table from a config file
            - Make output repeatable with a seed
Input:      Database URL, YAML config with row counts
Tech stack: Python, SQLAlchemy, Faker, Typer
```

---

## Example 157

**Intent:**
every morning give me a list of the slowest database queries from yesterday

**Spec:**
```
Type:       Scheduled script (slow query report)
Features:   - Read statistics from pg_stat_statements
            - Rank queries by total time and mean time
            - Compare with the previous day to show new slow queries
            - Suggest missing indexes from sequential scan counts
            - Email the report and reset statistics
Input:      Database URL, report recipients
Tech stack: Python, psycopg, Jinja2, cron
```

---

## Example 158

**Intent:**
our payment api sometimes gets the same request twice when the network is bad and charges the customer twice. how do we stop that

**Spec:**
```
Type:       REST API service (idempotency layer)
Data model: IdempotencyKey(key, client_id, request_hash, status, response_code, response_body, created_at)
Features:   - Require an Idempotency-Key header on POST requests
            - Store the first response for each key and return it on retries
            - Return 409 when the same key arrives with a different body
            - Lock the key while the first request is still running
            - Expire keys after 24 hours
API:        REST
            POST /payments
Storage:    PostgreSQL, Redis (in-flight locks)
Tech stack: Go, Echo, PostgreSQL
```

---

## Example 159

**Intent:**
When an order is saved we also need to publish an event, but sometimes the DB saves and the event gets lost.

**Spec:**
```
Type:       Data pipeline (transactional outbox)
Data model: Order(id, customer_id, total, status)
            OutboxEvent(id, aggregate_id, event_type, payload_json, created_at, published_at)
Features:   - Write the order and an outbox row in the same transaction
            - Poll unpublished outbox rows and send them to the message broker
            - Mark rows published after the broker confirms
            - Keep event order per aggregate
            - Delete published rows after 7 days
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, RabbitMQ
```

---

## Example 160

**Intent:**
a service that hands out locks so only one of our workers processes a given customer at a time

**Spec:**
```
Type:       REST API service (distributed locking)
Auth:       Internal service token
Features:   - Acquire a lock by name with a time-to-live
            - Return a fencing token that increases with each grant
            - Release a lock only by its holder
            - Extend a lock while work is still running
            - Auto-release locks when the TTL expires
API:        REST
            POST /locks/{name}/acquire
            POST /locks/{name}/release
            POST /locks/{name}/extend
Storage:    etcd
Tech stack: Go, etcd client v3, gRPC gateway
```

---

## Example 161

**Intent:**
Our signup flow calls 4 services (account, billing, email, CRM). If one fails halfway, things are left half-created. I want it to retry or undo properly.

**Spec:**
```
Type:       REST API service (workflow orchestration)
Data model: SignupWorkflow(id, user_email, state, current_step, error, started_at)
Features:   - Run signup steps as a durable workflow
            - Retry each step with backoff on temporary failures
            - Run compensating actions in reverse when a step fails permanently
            - Resume workflows after a worker crash
            - Show workflow history for debugging
API:        REST
            POST /signups
            GET  /signups/{id}
Storage:    PostgreSQL (Temporal persistence)
Tech stack: TypeScript, Temporal, Node.js
```

---

## Example 162

**Intent:**
If our main cloud region goes down we want the site to switch to a backup region by itself.

**Spec:**
```
Type:       Infrastructure setup (multi-region failover)
Features:   - Run the app in a primary and a standby region
            - Replicate the database across regions
            - Health-check the primary from DNS
            - Switch DNS to the standby when health checks fail
            - Document how to fail back after recovery
Storage:    Amazon Aurora Global Database
Tech stack: AWS Route 53 failover routing, ECS, Terraform
```

---

## Example 163

**Intent:**
we changed our site urls and lost google ranking. need to manage 301 redirects without a developer

**Spec:**
```
Type:       Web application (redirect manager)
Auth:       Marketing team login
Data model: Redirect(id, source_path, target_url, status_code, hits, created_by, created_at)
Features:   - Add, edit and delete redirects in a web form
            - Import redirects in bulk from CSV
            - Detect redirect loops and chains before saving
            - Apply redirects at the edge for fast responses
            - Count hits per redirect
API:        REST
            GET  /redirects
            POST /redirects
            POST /redirects/import
Storage:    Cloudflare KV
Tech stack: Cloudflare Workers, TypeScript, Hono
```

---

## Example 164

**Intent:**
mobile app needs to force users to update when the old version is broken

**Spec:**
```
Type:       REST API service (app version gating)
Auth:       Admin token for changes
Data model: AppVersionRule(id, platform, min_supported_version, latest_version, message, store_url)
Features:   - Return whether the app version is supported, outdated or blocked
            - Set the minimum version per platform
            - Show a custom update message in the app
            - Link to the right app store
API:        REST
            GET  /app-version?platform={ios|android}&version={v}
            PUT  /app-version/{platform}
Storage:    Firebase Firestore
Tech stack: Firebase Cloud Functions, TypeScript
```

---

## Example 165

**Intent:**
put the website in maintenance mode with one switch while we migrate the database

**Spec:**
```
Type:       Infrastructure setup (maintenance mode)
Features:   - Serve a static maintenance page with HTTP 503 and Retry-After
            - Let office IPs bypass the maintenance page
            - Toggle on and off with a single command
            - Keep health checks returning OK so the load balancer stays up
Tech stack: Nginx, Bash script, Ansible
```

---

## Example 166

**Intent:**
I want a little feedback button inside our web app that sends the message plus a screenshot to us.

**Spec:**
```
Type:       REST API service (in-app feedback)
Auth:       Logged-in user session
Data model: Feedback(id, user_id, page_url, message, screenshot_key, browser, created_at, status)
Features:   - Collect a message and an optional screenshot from a JavaScript widget
            - Attach page URL, browser and app version automatically
            - Store feedback and list it for the product team
            - Create a GitHub issue from a feedback item
API:        REST
            POST /feedback
            GET  /feedback
            POST /feedback/{id}/issue
Storage:    PostgreSQL, S3 (screenshots)
Tech stack: Node.js, Express, html2canvas, GitHub API
```

---

## Example 167

**Intent:**
website visitor stats without google analytics and without cookies

**Spec:**
```
Type:       Infrastructure setup (privacy-friendly analytics)
Features:   - Self-host a cookieless web analytics server
            - Add a small script tag to the website
            - Show visitors, pages, referrers and countries
            - Exclude own visits by IP
            - Keep data on our own server for GDPR
Storage:    ClickHouse, PostgreSQL
Tech stack: Plausible Community Edition, Docker Compose
```

---

## Example 168

**Intent:**
we cant afford sentry, self host error tracking for our django + react app

**Spec:**
```
Type:       Infrastructure setup (self-hosted error tracking)
Auth:       Team accounts
Features:   - Run a Sentry-compatible error tracker on our server
            - Send backend exceptions from Django with the Sentry SDK
            - Send frontend errors with source maps from React
            - Group errors and email on new issues
Storage:    PostgreSQL
Tech stack: GlitchTip, Docker Compose, sentry-sdk
```

---

## Example 169

**Intent:**
Hello, I need a system where our partners send us product prices by API and we keep the history, for compare later. We are a price comparison company in Poland.

**Spec:**
```
Type:       REST API service (partner price ingestion)
Auth:       API key per partner
Data model: Partner(id, name, api_key_hash)
            Offer(id, partner_id -> Partner, product_ean, price, currency, url, in_stock, updated_at)
            PriceHistory(id, offer_id -> Offer, price, recorded_at)
Features:   - Accept price updates in batches of up to 1,000 offers
            - Validate EAN codes and currency
            - Write a history row only when the price changes
            - Return the lowest current price per product
API:        REST
            PUT  /offers/batch
            GET  /products/{ean}/offers
            GET  /products/{ean}/history
Storage:    PostgreSQL (partitioned history table)
Tech stack: Kotlin, Spring Boot, PostgreSQL
```

---

## Example 170

**Intent:**
please i need make api for check if IBAN is correct before we pay suppliers

**Spec:**
```
Type:       REST API service (IBAN validation)
Features:   - Check IBAN length for its country
            - Verify the mod-97 checksum
            - Return the bank name and BIC from the bank code
            - Format the IBAN in groups of four
API:        REST
            GET  /iban/{iban}
Storage:    SQLite (bank code directory)
Tech stack: Python, FastAPI, schwifty
```

---

## Example 171

**Intent:**
we are hotel group of 6 hotels, each hotel use different booking software. we want all bookings in one database every night for the reports

**Spec:**
```
Type:       Data pipeline (booking consolidation)
Data model: Hotel(id, name, pms_type)
            Booking(id, hotel_id -> Hotel, external_id, guest_name, arrival, departure, room_type, revenue, status)
Features:   - Extract bookings from each hotel's PMS through its API or CSV export
            - Map fields from each system to one common format
            - Load into the central database, updating changed bookings
            - Compute occupancy and revenue per hotel per day
Storage:    PostgreSQL
Tech stack: Python, Airflow, pandas
```

---

## Example 172

**Intent:**
in my company we have many SFTP servers from partners, i want one place where i see all file transfers and if something failed

**Spec:**
```
Type:       Web application (managed file transfer)
Auth:       Staff login
Data model: Partner(id, name, host, port, username, key_ref)
            TransferJob(id, partner_id -> Partner, direction, remote_path, local_path, schedule)
            TransferRun(id, job_id -> TransferJob, status, files_count, error, started_at)
Features:   - Define upload and download jobs per partner
            - Run jobs on schedule over SFTP
            - Retry failed transfers 3 times
            - Show status of all transfers on one dashboard
            - Email on failure
API:        REST
            GET  /jobs
            POST /jobs/{id}/run
            GET  /runs?status=failed
Storage:    PostgreSQL
Tech stack: Python, Django, paramiko, Celery
```

---

## Example 173

**Intent:**
plz help, our wordpress site get hacked 2 times. how to make server more secure

**Spec:**
```
Type:       Infrastructure setup (web server hardening)
Features:   - Block repeated failed logins with fail2ban
            - Put the site behind a web application firewall
            - Disable XML-RPC and file editing in WordPress
            - Run PHP as a separate user with limited file permissions
            - Apply security updates automatically
            - Scan files daily for malware
Tech stack: Ubuntu, Nginx, fail2ban, Cloudflare WAF, unattended-upgrades, ClamAV
```

---

## Example 174

**Intent:**
we are school in Spain, we want parents to get SMS when student is absent, the teacher mark in our system

**Spec:**
```
Type:       Webhook service (absence SMS alerts)
Data model: Student(id, name, class_name)
            Guardian(id, student_id -> Student, name, phone, language)
            AbsenceNotice(id, student_id -> Student, date, period, sms_status, sent_at)
Features:   - Receive absence events from the school management system
            - Send an SMS to each guardian in Spanish or their language
            - Send only one SMS per student per day
            - Record delivery status from the SMS provider
API:        REST
            POST /webhooks/absence
            POST /webhooks/sms-status
Storage:    MySQL
Tech stack: PHP, Laravel, Vonage SMS API
```

---

## Example 175

**Intent:**
want api where i send long url of product image and it remove the background

**Spec:**
```
Type:       REST API service (background removal)
Auth:       API key
Features:   - Download the image from the given URL
            - Remove the background with a segmentation model
            - Return a transparent PNG or a white-background JPEG
            - Trim empty space around the product
            - Cache results by image hash
API:        REST
            POST /remove-background
Storage:    S3 (results)
Tech stack: Python, rembg, ONNX Runtime, FastAPI
```

---

## Example 176

**Intent:**
my company use SAP and we need to send the stock levels to our webshop every 15 min

**Spec:**
```
Type:       Scheduled script (ERP stock sync)
Features:   - Read stock levels from SAP through an OData service
            - Map SAP material numbers to webshop SKUs
            - Update only changed quantities in the webshop
            - Run every 15 minutes
            - Log errors and notify IT by email
Input:      SAP OData endpoint and credentials, SKU mapping table
Tech stack: Python, pyodata, Shopware Admin API
```

---

## Example 177

**Intent:**
ocr for scanned contracts so we can search inside them

**Spec:**
```
Type:       Data pipeline (document OCR and search)
Data model: Document(id, filename, page_count, text, ocr_confidence, uploaded_at)
Features:   - Watch a folder for new scanned PDFs
            - Run OCR and embed a text layer in the PDF
            - Index the text for full-text search
            - Search across contracts and show matching pages
Storage:    PostgreSQL full-text search, file storage
Tech stack: Paperless-ngx, Tesseract, Docker
```

---

## Example 178

**Intent:**
I'm learning DevOps and want a realistic project: put a simple Python app on AWS with Terraform, load balancer, autoscaling, the works.

**Spec:**
```
Type:       Infrastructure setup (AWS web app stack)
Features:   - Create a VPC with public and private subnets in two availability zones
            - Run the app on EC2 instances in an autoscaling group
            - Put an Application Load Balancer with HTTPS in front
            - Use a managed PostgreSQL database in the private subnet
            - Scale out when CPU is above 60%
Storage:    Amazon RDS PostgreSQL
Tech stack: Terraform, AWS EC2, ALB, RDS, Python Flask
```

---

## Example 179

**Intent:**
backup restore test - every week actually restore last backup to a temp server and check it works

**Spec:**
```
Type:       Scheduled script (backup restore verification)
Features:   - Download the latest database backup every Sunday
            - Restore it into a temporary database container
            - Run sanity queries like row counts on key tables
            - Compare counts with production within a tolerance
            - Destroy the container and report pass or fail
Input:      Backup bucket, list of sanity queries
Tech stack: Bash, Docker, PostgreSQL, AWS CLI
```

---

## Example 180

**Intent:**
an API to convert units, like kg to lbs and celsius to fahrenheit, for our recipe app

**Spec:**
```
Type:       REST API service (unit conversion)
Features:   - Convert between metric and imperial units of mass, volume, length and temperature
            - Convert cooking units like cups, tablespoons and teaspoons
            - Convert volume to mass using ingredient densities
            - Round results to friendly kitchen fractions
API:        REST
            GET  /convert?value={n}&from={unit}&to={unit}&ingredient={name}
            GET  /units
Tech stack: Python, Pint, FastAPI
```

---

## Example 181

**Intent:**
Set up proper environment variables and secrets for our app so they're not in git anymore.

**Spec:**
```
Type:       Infrastructure setup (secrets management)
Auth:       Developers via SSO; apps via machine identities
Features:   - Move secrets from .env files into a secrets manager
            - Separate secrets by environment (dev, staging, production)
            - Inject secrets into containers at runtime
            - Scan the Git history for leaked secrets and rotate them
            - Block commits containing secrets with a pre-commit hook
Tech stack: HashiCorp Vault, gitleaks, pre-commit, Kubernetes
```

---

## Example 182

**Intent:**
hourly snapshots of my nas so ransomware cant destroy everything

**Spec:**
```
Type:       Infrastructure setup (immutable snapshots)
Features:   - Take ZFS snapshots every hour, day and week
            - Keep 24 hourly, 14 daily and 8 weekly snapshots
            - Make snapshots read-only and not deletable from SMB clients
            - Replicate snapshots to a second machine that pulls them
            - Alert when snapshot replication fails
Storage:    ZFS pools on two machines
Tech stack: TrueNAS SCALE, sanoid, syncoid
```

---

## Example 183

**Intent:**
A public API for our museum collection so researchers and developers can use it.

**Spec:**
```
Type:       GraphQL API service (museum collection)
Data model: Artwork(id, title, date_text, medium, dimensions, image_url, license)
            Artist(id, name, birth_year, death_year, nationality)
            Exhibition(id, title, start_date, end_date)
Features:   - Query artworks with filters for artist, period and medium
            - Return IIIF image links for high-resolution viewing
            - Include license info for open-access images
            - Rate limit anonymous clients and give higher limits with a free key
API:        GraphQL
            POST /graphql
Storage:    PostgreSQL
Tech stack: Python, Strawberry GraphQL, FastAPI, IIIF image server
```

---

## Example 184

**Intent:**
I'd like a public API with all the parliament votes in my country, scraped from the official site.

**Spec:**
```
Type:       REST API service (open parliament data)
Data model: Member(id, name, party, constituency)
            Bill(id, title, introduced_on, status)
            Vote(id, bill_id -> Bill, date, result)
            MemberVote(vote_id -> Vote, member_id -> Member, choice)
Features:   - Scrape new votes from the parliament website daily
            - Return how each member voted on a bill
            - Show a member's voting record
            - Offer full data dumps as CSV
API:        REST
            GET  /bills/{id}/votes
            GET  /members/{id}/votes
            GET  /dumps/latest.zip
Storage:    PostgreSQL
Tech stack: Python, Scrapy, Django REST Framework
```

---

## Example 185

**Intent:**
air quality sensors around the city, open data api for everyone

**Spec:**
```
Type:       IoT system (open air quality data)
Auth:       Device tokens for sensors; public read access
Data model: Station(id, name, latitude, longitude, installed_on)
            Measurement(station_id -> Station, pm25, pm10, no2, measured_at)
Features:   - Receive measurements from stations every 5 minutes
            - Calculate the air quality index per station
            - Publish a public API with latest and historical data
            - Show stations on a map with colored AQI markers
API:        REST
            POST /measurements
            GET  /stations
            GET  /stations/{id}/measurements
Storage:    TimescaleDB
Tech stack: Node.js, Fastify, TimescaleDB, Leaflet
```

---

## Example 186

**Intent:**
I run a small coworking space. Doors open with a code. I want codes that only work during a member's booking time.

**Spec:**
```
Type:       IoT system (smart door access)
Auth:       Member login on the booking site
Data model: Member(id, name, email)
            Booking(id, member_id -> Member, room_id, starts_at, ends_at)
            AccessCode(id, booking_id -> Booking, code, valid_from, valid_to)
Features:   - Create a PIN code for each booking
            - Push valid codes to the smart lock via its API
            - Remove codes after the booking ends
            - Log door openings per member
API:        REST
            POST /bookings
            POST /webhooks/lock-events
Storage:    PostgreSQL
Tech stack: Python, Django, Nuki Web API
```

---

## Example 187

**Intent:**
temperature in our server room, email me if over 30 degrees

**Spec:**
```
Type:       IoT system (server room temperature alert)
Features:   - Read a DS18B20 sensor on a Raspberry Pi every minute
            - Email an alert when temperature passes 30°C
            - Send a follow-up when it goes back to normal
            - Avoid repeat alerts more than once per 30 minutes
Storage:    CSV log file on the Pi
Tech stack: Python, w1thermsensor, smtplib, systemd timer
```

---

## Example 188

**Intent:**
We print shipping labels from many places. Send print jobs from our cloud app to printers in the warehouse.

**Spec:**
```
Type:       REST API service (cloud print relay)
Auth:       API key for the app; agent token per warehouse
Data model: Printer(id, warehouse_id, name, model, online)
            PrintJob(id, printer_id -> Printer, format, file_key, status, created_at)
Features:   - Run a small agent on a warehouse PC that connects to the cloud
            - Queue print jobs per printer
            - Send ZPL label files directly to Zebra printers
            - Report job success or errors back to the app
API:        REST
            POST /print-jobs
            GET  /printers
            WS   /agent/connect
Storage:    PostgreSQL, S3
Tech stack: Go (agent and server), WebSockets, ZPL
```

---

## Example 189

**Intent:**
search api for our 2 million products with filters by brand, price, color

**Spec:**
```
Type:       REST API service (product search)
Data model: ProductDocument(id, title, description, brand, color, price, in_stock, popularity)
Features:   - Index products from the database with a change stream
            - Full-text search with synonyms and stemming
            - Faceted filters for brand, color and price ranges
            - Boost in-stock and popular products
            - Autocomplete product names as the user types
API:        REST
            GET  /search?q={text}&brand={b}&price_min={n}&price_max={n}
            GET  /autocomplete?q={prefix}
Storage:    OpenSearch
Tech stack: Java, Spring Boot, OpenSearch
```

---

## Example 190

**Intent:**
find similar documents by meaning, not just keywords, in our knowledge base

**Spec:**
```
Type:       REST API service (semantic search)
Data model: Chunk(id, document_id, text, embedding vector(384), position)
Features:   - Split documents into chunks of about 300 words
            - Create embeddings for each chunk
            - Find the nearest chunks to a query with vector search
            - Combine vector and keyword scores
            - Re-embed documents when they change
API:        REST
            POST /documents
            GET  /search?q={query}
Storage:    PostgreSQL with pgvector
Tech stack: Python, sentence-transformers, FastAPI
```

---

## Example 191

**Intent:**
our customer database has lots of duplicates, same person typed differently. find and merge them

**Spec:**
```
Type:       Data analysis script (record deduplication)
Features:   - Normalize names, emails, phones and addresses
            - Group candidate pairs with blocking on postcode and name prefix
            - Score pairs with fuzzy matching
            - Export likely duplicates for human review
            - Merge confirmed pairs keeping the newest values
Input:      Customer table export as CSV
Tech stack: Python, pandas, Splink, DuckDB
```

---

## Example 192

**Intent:**
Our mobile app shows wrong strings in some languages. I want translators to edit texts on a website and the app fetches them.

**Spec:**
```
Type:       Web application (translation management)
Auth:       Translator and developer roles
Data model: Language(code, name)
            StringKey(id, key, description)
            Translation(id, key_id -> StringKey, language_code -> Language, value, reviewed)
Features:   - Import string keys from the app's resource files
            - Let translators edit and review strings per language
            - Show missing translations per language
            - Publish a JSON bundle per language that the app downloads
API:        REST
            GET  /bundles/{language}.json
            POST /keys/import
Storage:    PostgreSQL, CDN (bundles)
Tech stack: Tolgee (self-hosted), Docker
```

---

## Example 193

**Intent:**
Remote config for my game so I can change difficulty values without shipping an update.

**Spec:**
```
Type:       REST API service (remote config)
Auth:       Admin token for edits; public read with app key
Data model: ConfigValue(id, key, value_json, platform, min_app_version, updated_at)
Features:   - Store key-value settings as JSON
            - Return config filtered by platform and app version
            - Support ETag so clients download only when changed
            - Keep a change history with rollback
API:        REST
            GET  /config
            PUT  /config/{key}
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Unity client
```

---

## Example 194

**Intent:**
customers send us big files over email and it bounces. need a page where they upload straight to us

**Spec:**
```
Type:       Web application (secure file drop)
Auth:       Staff login; customers use a one-time upload link
Data model: UploadRequest(id, created_by, customer_email, token, expires_at)
            File(id, request_id -> UploadRequest, filename, size_bytes, storage_key, uploaded_at)
Features:   - Create an upload link for a customer
            - Upload files up to 10 GB with resumable uploads
            - Notify staff when files arrive
            - Delete files after 30 days
API:        REST
            POST /requests
            POST /upload/{token}
            GET  /requests/{id}/files
Storage:    PostgreSQL, S3
Tech stack: Node.js, tus protocol (tusd), Uppy, Next.js
```

---

## Example 195

**Intent:**
Every tenant on our platform should be able to bring their own domain name and have HTTPS work automatically.

**Spec:**
```
Type:       Infrastructure setup (custom domains with automatic TLS)
Data model: CustomDomain(id, tenant_id, hostname, verification_token, verified, cert_status)
Features:   - Let tenants add a domain and show the CNAME to set
            - Verify ownership with a DNS TXT record
            - Issue certificates on demand at first request
            - Route requests to the right tenant by Host header
            - Renew certificates automatically
API:        REST
            POST /domains
            POST /domains/{id}/verify
Storage:    PostgreSQL, certificate storage in Redis
Tech stack: Caddy (on-demand TLS), Go
```

---

## Example 196

**Intent:**
generate api client libraries for python and typescript from our openapi spec on every release

**Spec:**
```
Type:       Command-line script (SDK generation)
Features:   - Validate the OpenAPI file on each release tag
            - Generate Python and TypeScript clients
            - Run generated client tests against a mock server
            - Publish packages to PyPI and npm with the release version
Input:      OpenAPI spec file, release version
Tech stack: OpenAPI Generator, Prism mock server, GitHub Actions
```

---

## Example 197

**Intent:**
Lots of different bots hit our signup page. Can we detect fake signups using signals like IP reputation and typing speed?

**Spec:**
```
Type:       REST API service (signup fraud scoring)
Data model: SignupAttempt(id, email, ip, user_agent, fill_time_ms, risk_score, decision, created_at)
Features:   - Collect browser signals like form fill time and mouse movement
            - Check IP against proxy and data center ranges
            - Check email domain age and disposable providers
            - Combine signals into a risk score
            - Allow, challenge or block based on score thresholds
API:        REST
            POST /risk/signup
Storage:    PostgreSQL, Redis (IP reputation cache)
Tech stack: Python, FastAPI, LightGBM
```

---

## Example 198

**Intent:**
Docker logs filling the disk on our VPS. fix it

**Spec:**
```
Type:       Infrastructure setup (disk space hygiene)
Features:   - Set Docker log rotation with max size and max files
            - Prune unused images and build cache weekly
            - Rotate application logs with logrotate
            - Alert when disk usage passes 80%
Tech stack: Docker daemon.json, logrotate, systemd timer, ntfy
```

---

## Example 199

**Intent:**
Scheduled PDF reports for each of our clients with their monthly stats, emailed on the 1st.

**Spec:**
```
Type:       Scheduled script (client PDF reports)
Data model: Client(id, name, contact_email, logo_url)
            ReportRun(id, client_id -> Client, month, pdf_key, sent_at, status)
Features:   - Run on the 1st of each month
            - Query each client's metrics for the previous month
            - Render charts and tables into a branded PDF
            - Email the PDF to each client contact
            - Retry failed sends and log the result
Storage:    PostgreSQL, S3 (PDF archive)
Tech stack: Python, WeasyPrint, matplotlib, Celery beat
```

---

## Example 200

**Intent:**
QR codes on our flyers that we can point somewhere else later without reprinting

**Spec:**
```
Type:       Web application (dynamic QR codes)
Auth:       Email + password login
Data model: User(id, email, password_hash)
            QrCode(id, user_id -> User, slug, target_url, label, created_at)
            Scan(id, qr_code_id -> QrCode, scanned_at, device_type, city)
Features:   - Create a QR code that points to a short redirect URL
            - Change the destination at any time without changing the code
            - Download the code as SVG or high-resolution PNG
            - Count scans by day and device
API:        REST
            POST /codes
            PATCH /codes/{id}
            GET  /q/{slug}
Storage:    PostgreSQL
Tech stack: Python, Django, qrcode library
```

---

## Example 201

**Intent:**
default profile pictures for users who didn't upload one, generated from their name

**Spec:**
```
Type:       REST API service (avatar generation)
Features:   - Generate an SVG avatar with the user's initials
            - Pick a background color from a hash of the name
            - Return PNG at requested sizes
            - Cache with immutable headers
API:        REST
            GET  /avatar/{name}.svg
            GET  /avatar/{name}.png?size={px}
Tech stack: Rust, Axum, resvg
```

---

## Example 202

**Intent:**
Invoices in our country must have numbers with no gaps, per company, per year. Our app is multi-tenant and has many servers.

**Spec:**
```
Type:       REST API service (gapless invoice numbering)
Auth:       Internal service token
Data model: NumberSequence(tenant_id, year, prefix, next_value)
            IssuedNumber(id, tenant_id, year, number, invoice_id, issued_at)
Features:   - Issue the next number per tenant and year inside a database transaction
            - Lock the sequence row so parallel requests never get the same number
            - Format numbers with a prefix like INV-2026-00042
            - Record every issued number for audits
API:        REST
            POST /tenants/{id}/invoice-numbers
            GET  /tenants/{id}/invoice-numbers?year={y}
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Dapper
```

---

## Example 203

**Intent:**
validar CPF e CNPJ dos clientes no cadastro, api simples pfv

**Spec:**
```
Type:       REST API service (Brazilian tax ID validation)
Features:   - Validate CPF check digits
            - Validate CNPJ check digits
            - Reject known invalid sequences like 111.111.111-11
            - Return the number formatted with dots, slash and dash
API:        REST
            GET  /cpf/{number}
            GET  /cnpj/{number}
Tech stack: Node.js, Express
```

---

## Example 204

**Intent:**
UK postcode lookup so customers pick their address from a list at checkout

**Spec:**
```
Type:       REST API service (postcode address lookup)
Data model: Address(id, postcode, line1, line2, town, uprn)
Features:   - Normalize the postcode format
            - Return all addresses for a postcode
            - Autocomplete partial postcodes
            - Reload the address dataset monthly
API:        REST
            GET  /postcodes/{postcode}/addresses
            GET  /postcodes/autocomplete?q={partial}
Storage:    PostgreSQL
Tech stack: Go, PostgreSQL, Ordnance Survey AddressBase data
```

---

## Example 205

**Intent:**
Our frontend calls a weather API directly and the API key is visible in the browser. I need a small proxy that hides it.

**Spec:**
```
Type:       REST API service (API key proxy)
Features:   - Forward allowed paths to the upstream API with the secret key added
            - Accept requests only from our site's origin
            - Rate limit per visitor IP
            - Cache responses for 5 minutes
API:        REST
            GET  /proxy/weather/{path}
Tech stack: Cloudflare Workers, JavaScript, Workers KV
```

---

## Example 206

**Intent:**
We have an old SOAP service from 2009 that nobody wants to touch. Put a modern GraphQL API on top of it for our new apps.

**Spec:**
```
Type:       GraphQL API service (legacy SOAP wrapper)
Auth:       JWT from the company identity provider
Features:   - Map SOAP operations to GraphQL queries and mutations
            - Convert XML responses to typed GraphQL objects
            - Batch and cache repeated lookups per request with DataLoader
            - Translate SOAP faults into GraphQL errors
API:        GraphQL
            POST /graphql
Tech stack: Node.js, Apollo Server, node-soap, DataLoader
```

---

## Example 207

**Intent:**
copy our old ibm as400 tables to postgres every night so the new apps can read them

**Spec:**
```
Type:       Data pipeline (legacy database replication)
Features:   - Connect to DB2 for i over JDBC
            - Extract changed rows by timestamp columns
            - Convert EBCDIC text and packed decimals
            - Upsert rows into PostgreSQL tables
            - Report row counts and mismatches after each run
Storage:    IBM DB2 for i (source), PostgreSQL (target)
Tech stack: Java, JTOpen JDBC driver, Apache Camel, cron
```

---

## Example 208

**Intent:**
Migrate our app's database from MySQL to Postgres with as little downtime as possible.

**Spec:**
```
Type:       Infrastructure setup (database migration)
Features:   - Convert the schema to PostgreSQL types
            - Copy the initial data in bulk
            - Stream ongoing changes with change data capture until cutover
            - Compare row counts and checksums per table
            - Switch the app connection during a short write freeze
Storage:    MySQL (source), PostgreSQL (target)
Tech stack: pgloader, Debezium, Kafka, Python verification script
```

---

## Example 209

**Intent:**
change a big table column without locking the db for an hour

**Spec:**
```
Type:       Command-line tool (online schema change)
Features:   - Create a shadow table with the new schema
            - Copy rows in small chunks while the app keeps running
            - Capture ongoing writes with triggers
            - Swap tables in a quick rename
            - Pause when replication lag gets too high
Input:      Database URL, table name, ALTER statement
Tech stack: gh-ost, MySQL
```

---

## Example 210

**Intent:**
each big customer wants their own separate database. create it automatically when they sign the contract

**Spec:**
```
Type:       REST API service (tenant database provisioning)
Auth:       Internal admin token
Data model: Tenant(id, name, db_host, db_name, status, schema_version)
Features:   - Create a new database and user for a tenant
            - Run all schema migrations on the new database
            - Store encrypted connection details in the tenant registry
            - Run migrations across all tenant databases on deploy
            - Drop a tenant database after a grace period on cancellation
API:        REST
            POST /tenants
            GET  /tenants/{id}
            DELETE /tenants/{id}
Storage:    PostgreSQL (registry and tenant databases)
Tech stack: Go, golang-migrate, HashiCorp Vault
```

---

## Example 211

**Intent:**
Every user on our photo app has 5GB on the free plan. Block uploads when they go over and show them how much they use.

**Spec:**
```
Type:       REST API service (storage quotas)
Auth:       User session token
Data model: User(id, plan, quota_bytes, used_bytes)
            StoredFile(id, user_id -> User, size_bytes, created_at, deleted_at)
Features:   - Check remaining quota before each upload
            - Update usage atomically on upload and delete
            - Reject uploads over quota with a clear error
            - Show usage and quota in the account page
            - Recalculate usage nightly to fix drift
API:        REST
            GET  /me/storage
            POST /files
Storage:    PostgreSQL, S3
Tech stack: Node.js, NestJS, TypeORM
```

---

## Example 212

**Intent:**
saas with per-seat pricing, admins add users and billing changes automatically, prorated

**Spec:**
```
Type:       REST API service (seat-based billing)
Auth:       Organization admin role
Data model: Organization(id, name, billing_customer_id, seat_count)
            Member(id, organization_id -> Organization, email, role, active)
            SeatChange(id, organization_id -> Organization, delta, effective_at, proration_cents)
Features:   - Add or remove members and update the seat count
            - Calculate prorated charges for mid-cycle changes
            - Update the subscription quantity with the billing provider
            - Block adding members beyond the plan maximum
API:        REST
            POST /orgs/{id}/members
            DELETE /orgs/{id}/members/{member_id}
            GET  /orgs/{id}/billing
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Paddle Billing API
```

---

## Example 213

**Intent:**
Free trials of our app last 14 days. Remind people on day 10 and lock the account when it ends unless they paid.

**Spec:**
```
Type:       Scheduled script (trial lifecycle)
Data model: Account(id, email, trial_ends_at, subscription_status, locked)
            TrialEmail(id, account_id -> Account, kind, sent_at)
Features:   - Check accounts every hour
            - Send a reminder email 4 days before the trial ends
            - Lock accounts whose trial ended without a subscription
            - Unlock immediately when a payment arrives
            - Never send the same email twice
Storage:    PostgreSQL
Tech stack: Python, Celery beat, Postmark
```

---

## Example 214

**Intent:**
We sell an AI writing tool and want to charge by tokens used. Track every request's tokens per customer.

**Spec:**
```
Type:       REST API service (AI usage metering)
Auth:       Customer API keys
Data model: Customer(id, name, monthly_token_limit)
            UsageRecord(id, customer_id -> Customer, model, input_tokens, output_tokens, cost_cents, created_at)
Features:   - Record tokens for every model call
            - Calculate cost with per-model prices
            - Block requests when a monthly limit is reached
            - Show daily usage charts per customer
            - Export usage totals to the billing system each month
API:        REST
            POST /usage
            GET  /customers/{id}/usage?month={m}
Storage:    PostgreSQL, Redis (running totals)
Tech stack: TypeScript, Hono, Drizzle ORM
```

---

## Example 215

**Intent:**
services inside our cluster should only talk to each other with certificates, no plain http

**Spec:**
```
Type:       Infrastructure setup (service-to-service mTLS)
Features:   - Issue short-lived certificates to every service automatically
            - Enforce mutual TLS between all services
            - Allow only listed service pairs to communicate
            - Rotate certificates every 24 hours
            - Show service traffic in a graph
Tech stack: Kubernetes, Linkerd, cert-manager
```

---

## Example 216

**Intent:**
office of 25 people, need one login for computers, wifi and the file server

**Spec:**
```
Type:       Infrastructure setup (office directory service)
Auth:       Central user directory with group membership
Features:   - Run a directory server with users and groups
            - Join Windows and Linux computers to the domain
            - Authenticate Wi-Fi users with WPA2-Enterprise via RADIUS
            - Give file shares permissions based on groups
            - Disable all access when a user leaves
Tech stack: Samba Active Directory, FreeRADIUS, Ubuntu Server
```

---

## Example 217

**Intent:**
cafe wifi where guests get a voucher code on the receipt, works 2 hours

**Spec:**
```
Type:       Infrastructure setup (guest Wi-Fi captive portal)
Data model: Voucher(code, duration_minutes, created_at, first_used_at, device_mac)
Features:   - Show a captive portal page on the guest network
            - Generate voucher codes in batches for printing on receipts
            - Grant access for 2 hours from first use
            - Limit bandwidth per guest
            - Isolate guests from the staff network
Tech stack: UniFi Network Controller, UniFi access points, hotspot vouchers
```

---

## Example 218

**Intent:**
I have a lot of smart home gadgets and I don't trust them. Put them on their own network so they can't see my laptop.

**Spec:**
```
Type:       Infrastructure setup (IoT network segmentation)
Features:   - Create separate VLANs for trusted devices, IoT and guests
            - Give each VLAN its own Wi-Fi network name
            - Block IoT devices from reaching the trusted VLAN
            - Allow the home automation hub to reach IoT devices
            - Forward mDNS so casting still works
Tech stack: OPNsense, managed switch, VLAN-capable access points
```

---

## Example 219

**Intent:**
detect hackers on my home network, like an alarm system for the network

**Spec:**
```
Type:       Infrastructure setup (network intrusion detection)
Features:   - Mirror router traffic to a monitoring box
            - Inspect traffic against community rule sets
            - Alert on port scans, known malware traffic and odd DNS
            - Show alerts on a dashboard
            - Update rules daily
Storage:    Elasticsearch (alerts)
Tech stack: Suricata, Zeek, Elastic Stack, Raspberry Pi 5
```

---

## Example 220

**Intent:**
Our staff work from home and need to reach the office Windows PCs from a browser, no client install.

**Spec:**
```
Type:       Infrastructure setup (remote desktop gateway)
Auth:       Company SSO with MFA
Features:   - Provide browser-based RDP access to office PCs
            - Map each employee to their own PC only
            - Record sessions for admin review
            - Expose the gateway only over HTTPS
Storage:    PostgreSQL (connections and users)
Tech stack: Apache Guacamole, Keycloak, Nginx, Docker
```

---

## Example 221

**Intent:**
TVs in our shops showing offers, i want to change them all from one website

**Spec:**
```
Type:       Web application (digital signage)
Auth:       Marketing staff login
Data model: Screen(id, store_id, name, playlist_id -> Playlist, last_heartbeat)
            Playlist(id, name)
            Slide(id, playlist_id -> Playlist, media_url, duration_s, start_date, end_date)
Features:   - Upload images and videos as slides
            - Group slides into playlists with schedules
            - Assign playlists to screens per store
            - Show screens offline when no heartbeat for 5 minutes
            - Cache content on the player so it works offline
API:        REST
            GET  /player/{screen_id}/playlist
            POST /player/{screen_id}/heartbeat
Storage:    PostgreSQL, S3
Tech stack: Django, Raspberry Pi players in Chromium kiosk mode
```

---

## Example 222

**Intent:**
Keep a mirror of all our GitHub repos on our own server in case GitHub goes down or bans us.

**Spec:**
```
Type:       Scheduled script (Git repository mirroring)
Features:   - List all repositories in the GitHub organization
            - Clone new repositories as bare mirrors
            - Fetch all branches and tags every hour
            - Include wikis and LFS objects
            - Report failed mirrors by email
Input:      GitHub organization name and token, mirror directory
Tech stack: Python, GitHub REST API, git, systemd timer
```

---

## Example 223

**Intent:**
our game repo has huge texture files and git is very slow. host our own git lfs

**Spec:**
```
Type:       Infrastructure setup (Git LFS server)
Auth:       Per-user access tokens
Features:   - Store large files outside Git through the LFS API
            - Support file locking for binary assets
            - Store objects in S3-compatible storage
            - Track storage per repository
Storage:    MinIO
Tech stack: Gitea with LFS enabled, MinIO, Nginx
```

---

## Example 224

**Intent:**
team wiki on our own server that we can write in markdown

**Spec:**
```
Type:       Infrastructure setup (self-hosted wiki)
Auth:       Login through Google Workspace
Features:   - Write pages in Markdown with a live editor
            - Organize pages in a tree with search
            - Keep page history with diffs
            - Back up pages to a Git repository
Storage:    PostgreSQL
Tech stack: Wiki.js, Docker Compose, PostgreSQL
```

---

## Example 225

**Intent:**
documentation website for our library with a version picker for v1, v2, v3

**Spec:**
```
Type:       Infrastructure setup (versioned docs hosting)
Features:   - Build docs from Markdown in the repository
            - Publish each release under its own version path
            - Add a version switcher in the header
            - Add a full-text search index per version
            - Deploy automatically when a release tag is pushed
Tech stack: MkDocs Material, mike, GitHub Pages, GitHub Actions
```

---

## Example 226

**Intent:**
Our factory network has no internet. Machines still need Ubuntu updates. How?

**Spec:**
```
Type:       Infrastructure setup (offline package mirror)
Features:   - Mirror Ubuntu repositories on an internet-connected machine
            - Copy the mirror to a disk for transfer into the factory network
            - Serve the mirror over HTTP inside the network
            - Point factory machines' apt sources to the mirror
            - Verify package signatures on import
Storage:    Local disk (about 300 GB)
Tech stack: aptly, Nginx, rsync
```

---

## Example 227

**Intent:**
we have 80 raspberry pis in shops running a kiosk app. update and monitor them all from one place

**Spec:**
```
Type:       IoT system (Raspberry Pi fleet management)
Auth:       Device certificates; admin dashboard login
Features:   - Enroll each Pi with a unique device identity
            - Push new container versions to groups of devices
            - Show online status, CPU temperature and disk space
            - Open a remote shell for support
            - Roll back a release if devices fail health checks
Tech stack: balenaCloud, Docker, Raspberry Pi 4
```

---

## Example 228

**Intent:**
rotate the key we sign JWT login tokens with, without logging everyone out

**Spec:**
```
Type:       Scheduled script (JWT signing key rotation)
Data model: SigningKey(kid, private_key_encrypted, public_key, status, created_at, retire_at)
Features:   - Generate a new signing key every 30 days
            - Publish all active public keys in a JWKS endpoint
            - Sign new tokens with the newest key
            - Keep old keys for verification until their tokens expire
            - Delete retired keys
API:        REST
            GET  /.well-known/jwks.json
Storage:    PostgreSQL, AWS KMS (key encryption)
Tech stack: Node.js, jose library, cron
```

---

## Example 229

**Intent:**
Some of our enterprise customers want to use their own encryption keys for their data in our app.

**Spec:**
```
Type:       REST API service (bring-your-own-key encryption)
Auth:       Tenant admin role; cross-account IAM role for key access
Data model: TenantKey(id, tenant_id, kms_key_arn, status, last_verified_at)
Features:   - Let tenant admins register a KMS key from their own cloud account
            - Encrypt each tenant's data keys with that key
            - Verify key access daily and alert when access is lost
            - Make data unreadable when the customer revokes the key
API:        REST
            POST /tenants/{id}/keys
            POST /tenants/{id}/keys/verify
Storage:    PostgreSQL
Tech stack: Go, AWS KMS, envelope encryption
```

---

## Example 230

**Intent:**
we must not store raw card numbers in our main db. tokenize them

**Spec:**
```
Type:       REST API service (card tokenization vault)
Auth:       mTLS between internal services
Data model: CardToken(token, encrypted_pan, last4, brand, expiry, created_at)
Features:   - Accept a card number and return a random token
            - Encrypt card numbers with keys from an HSM
            - Return only the last 4 digits and brand to other services
            - Detokenize only for the payment gateway service
            - Log every detokenize call
API:        REST
            POST /tokens
            POST /tokens/{token}/detokenize
Storage:    PostgreSQL in an isolated network segment
Tech stack: Java, Spring Boot, AWS CloudHSM
```

---

## Example 231

**Intent:**
How can we prove nobody edited our audit logs later? Auditors asked us.

**Spec:**
```
Type:       REST API service (tamper-evident audit log)
Data model: LogEntry(seq, actor, action, payload_json, created_at, prev_hash, entry_hash)
            Checkpoint(id, last_seq, root_hash, signed_at, signature)
Features:   - Chain each entry with the SHA-256 hash of the previous entry
            - Sign a checkpoint of the latest hash every hour
            - Store checkpoints in write-once storage
            - Verify the chain on demand and report the first broken entry
API:        REST
            POST /entries
            GET  /verify
Storage:    PostgreSQL, S3 Object Lock (checkpoints)
Tech stack: Rust, Axum, ed25519-dalek
```

---

## Example 232

**Intent:**
when someone leaves the company, remove them from google, slack, github, aws all at once

**Spec:**
```
Type:       Command-line tool (employee offboarding)
Features:   - Suspend the Google Workspace account and transfer Drive files to the manager
            - Deactivate the Slack user
            - Remove the user from the GitHub organization
            - Delete AWS IAM user access keys
            - Print a checklist of what was done and what failed
Input:      Employee email, manager email
Tech stack: Python, Google Admin SDK, Slack SCIM API, GitHub API, boto3
```

---

## Example 233

**Intent:**
Our app needs to support SCIM so customers' IT can create and remove users from Okta automatically.

**Spec:**
```
Type:       REST API service (SCIM 2.0 provisioning)
Auth:       Bearer token per customer organization
Data model: Organization(id, name, scim_token_hash)
            User(id, organization_id -> Organization, external_id, user_name, email, active)
            Group(id, organization_id -> Organization, display_name)
Features:   - Create, update and deactivate users from SCIM requests
            - Support filtering like userName eq "x"
            - Sync group memberships
            - Return SCIM-formatted errors
API:        REST
            GET  /scim/v2/Users
            POST /scim/v2/Users
            PATCH /scim/v2/Users/{id}
            GET  /scim/v2/Groups
Storage:    PostgreSQL
Tech stack: Python, Django, PostgreSQL
```

---

## Example 234

**Intent:**
track company laptops and monitors with qr stickers, who has what

**Spec:**
```
Type:       Web application (IT asset tracking)
Auth:       IT staff login
Data model: Asset(id, tag, type, model, serial, purchase_date, status)
            Employee(id, name, email, department)
            Assignment(id, asset_id -> Asset, employee_id -> Employee, assigned_at, returned_at)
Features:   - Print QR stickers with asset tags
            - Scan a sticker with a phone to open the asset
            - Assign and return assets with history
            - Warn when warranties are about to expire
API:        REST
            GET  /assets/{tag}
            POST /assets/{id}/assign
Storage:    PostgreSQL
Tech stack: Snipe-IT, Docker
```

---

## Example 235

**Intent:**
We pay for 40 SaaS tools. Who uses which, and are we paying for seats nobody uses?

**Spec:**
```
Type:       Web application (SaaS license tracking)
Auth:       Company SSO
Data model: Tool(id, name, monthly_cost_per_seat, renewal_date)
            Seat(id, tool_id -> Tool, user_email, last_login_at)
Features:   - Import seat lists from tool admin exports and APIs
            - Read last-login dates from the SSO provider logs
            - Flag seats unused for 60 days
            - Remind owners 30 days before renewals
API:        REST
            GET  /tools
            GET  /tools/{id}/seats
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Okta System Log API
```

---

## Example 236

**Intent:**
access review every quarter: managers confirm their people still need each system

**Spec:**
```
Type:       Web application (access review)
Auth:       Company SSO
Data model: Campaign(id, quarter, status, due_date)
            AccessItem(id, campaign_id -> Campaign, employee_email, system, role, manager_email, decision)
Features:   - Pull current access lists from connected systems
            - Create a review task for each manager
            - Let managers keep or revoke each access
            - Create revoke tickets for removed access
            - Export results as evidence for SOC 2
API:        REST
            POST /campaigns
            GET  /campaigns/{id}/items?manager={email}
            POST /items/{id}/decision
Storage:    PostgreSQL
Tech stack: Python, Django, Jira API
```

---

## Example 237

**Intent:**
Mirror PyPI packages we use so our builds don't break when pypi is slow or a package is deleted.

**Spec:**
```
Type:       Infrastructure setup (Python package proxy)
Features:   - Proxy and cache packages from PyPI
            - Host private internal packages
            - Point pip and uv to the proxy through config
            - Keep cached versions even if removed upstream
Storage:    Local disk or S3 blob store
Tech stack: Sonatype Nexus Repository, Docker
```

---

## Example 238

**Intent:**
i need a cors proxy for my side project, the api i use doesnt allow browser calls

**Spec:**
```
Type:       REST API service (CORS proxy)
Features:   - Forward requests to an allow-listed set of hosts
            - Add Access-Control-Allow-Origin headers to responses
            - Answer preflight OPTIONS requests
            - Limit request size and rate per IP
API:        REST
            ANY  /proxy/{url}
Tech stack: Deno, Deno Deploy
```

---

## Example 239

**Intent:**
Old supplier still sends us stock lists by FTP as fixed-width text files. Put them into S3 as JSON so the cloud apps can use them.

**Spec:**
```
Type:       Data pipeline (FTP to S3 bridge)
Features:   - Poll the FTP server for new files every 30 minutes
            - Parse fixed-width records with a column layout config
            - Convert each file to JSON lines
            - Upload to S3 partitioned by date
            - Archive the original file
Input:      FTP credentials, column layout YAML
Storage:    AWS S3
Tech stack: Python, ftplib, boto3, AWS Lambda
```

---

## Example 240

**Intent:**
make sure all our server clocks are correct, logs are messed up because of time differences

**Spec:**
```
Type:       Infrastructure setup (time synchronization)
Features:   - Run two internal NTP servers synced to public pools
            - Point all servers to the internal NTP servers
            - Alert when a server's clock offset exceeds 100 ms
            - Set all servers to UTC
Tech stack: chrony, Ansible, Prometheus node_exporter
```

---

## Example 241

**Intent:**
For legal reasons, EU customer data must stay in EU servers and US data in US. Our app is one codebase.

**Spec:**
```
Type:       Infrastructure setup (data residency routing)
Data model: Account(id, region, name)
            RegionDirectory(account_id, region, api_base_url)
Features:   - Deploy the same app stack in an EU and a US region
            - Store each account's data only in its home region
            - Route requests to the right region from a global directory
            - Choose the region at signup by the customer's country
            - Keep backups inside the same region
Storage:    PostgreSQL per region
Tech stack: Kubernetes, Terraform, Cloudflare load balancing
```

---

## Example 242

**Intent:**
cut the time our data team spends asking "where does this column come from" — need a data catalog

**Spec:**
```
Type:       Web application (data catalog)
Auth:       Company SSO
Features:   - Ingest table and column metadata from the warehouse
            - Show lineage from dbt models
            - Let owners add descriptions and tags
            - Search tables and columns by name and description
            - Show who uses each table most
Storage:    MySQL, Elasticsearch
Tech stack: DataHub, dbt, Snowflake connector
```

---

## Example 243

**Intent:**
If we ever have a data breach we have 72 hours to report. Build a simple tool to manage that process.

**Spec:**
```
Type:       Web application (breach incident workflow)
Auth:       Security team login
Data model: Incident(id, title, detected_at, severity, status, report_deadline)
            AffectedDataset(id, incident_id -> Incident, system, data_types, record_count)
            Task(id, incident_id -> Incident, title, owner, done)
Features:   - Open an incident and start a 72-hour countdown
            - Record affected systems and data categories
            - Create a checklist of response tasks from a template
            - Generate a draft report for the data protection authority
            - Keep a timeline of every action
API:        REST
            POST /incidents
            GET  /incidents/{id}
            POST /incidents/{id}/tasks
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue
```

---

## Example 244

**Intent:**
expose my local dev server to the internet for testing webhooks, but self hosted not ngrok

**Spec:**
```
Type:       Infrastructure setup (self-hosted tunnel)
Auth:       Token per developer
Features:   - Run a tunnel server on a small VPS with a wildcard domain
            - Connect a local port to a public subdomain with one command
            - Terminate HTTPS with a wildcard certificate
            - Show request logs for each tunnel
Tech stack: frp (fast reverse proxy), Caddy, Cloudflare DNS
```

---

## Example 245

**Intent:**
api that follows a short link and tells me where it really goes, all the redirects

**Spec:**
```
Type:       REST API service (redirect tracing)
Features:   - Follow HTTP 3xx redirects up to 15 hops
            - Detect meta refresh and JavaScript redirects
            - Return each hop with status code and URL
            - Flag destinations on a malware domain list
            - Block private network addresses
API:        REST
            GET  /trace?url={link}
Tech stack: Python, httpx, FastAPI
```

---

## Example 246

**Intent:**
We own 60 domains and almost lost one because it expired. Warn us in time.

**Spec:**
```
Type:       Scheduled script (domain expiry check)
Data model: Domain(name, registrar, expires_on, auto_renew, last_checked_at)
Features:   - Look up expiry dates with RDAP every day
            - Warn at 60, 30 and 7 days before expiry
            - Flag domains without auto-renew
            - Detect nameserver changes
Storage:    SQLite
Tech stack: Python, whoisit (RDAP client), smtplib
```

---

## Example 247

**Intent:**
tool that checks if our domain email setup is right, spf dkim dmarc, and explains problems in simple words

**Spec:**
```
Type:       Web application (email authentication checker)
Features:   - Look up SPF, DKIM selectors, DMARC and MX records for a domain
            - Detect common mistakes like too many SPF lookups
            - Explain each problem in plain language with a fix
            - Send a test email address to check DKIM signatures on real mail
API:        REST
            GET  /check/{domain}
Tech stack: Go, miekg/dns, htmx
```

---

## Example 248

**Intent:**
Users on our forum upload images and some are inappropriate. Check every image automatically.

**Spec:**
```
Type:       REST API service (image moderation)
Data model: ModerationResult(id, image_key, nsfw_score, violence_score, decision, reviewed_by, created_at)
Features:   - Score each uploaded image with a classification model
            - Auto-approve low scores and auto-block high scores
            - Send borderline images to a human review queue
            - Match known bad images by perceptual hash
API:        REST
            POST /moderate
            GET  /review-queue
            POST /review-queue/{id}/decision
Storage:    PostgreSQL, S3
Tech stack: Python, ONNX Runtime, imagehash, FastAPI
```

---

## Example 249

**Intent:**
podcast episodes have different volume levels, fix them all to the same loudness automatically

**Spec:**
```
Type:       Command-line tool (audio loudness normalization)
Features:   - Measure integrated loudness of each audio file
            - Normalize to -16 LUFS for stereo podcasts
            - Limit true peak to -1 dBTP
            - Process a whole folder and keep originals
Input:      Folder of MP3 or WAV files, target loudness
Tech stack: Python, FFmpeg loudnorm filter, Typer
```

---

## Example 250

**Intent:**
online course: give students a PDF certificate with their name when they finish, and a way to verify it is real

**Spec:**
```
Type:       REST API service (certificate generation)
Data model: Certificate(id, code, student_name, course_title, completed_on, pdf_key)
Features:   - Generate a PDF certificate from a template on course completion
            - Add a unique verification code and QR code
            - Provide a public verification page by code
            - Re-issue a certificate if the name was misspelled
API:        REST
            POST /certificates
            GET  /verify/{code}
Storage:    PostgreSQL, S3
Tech stack: Python, ReportLab, qrcode, FastAPI
```

---

## Example 251

**Intent:**
Send real paper letters to customers from our software, like reminders for unpaid bills.

**Spec:**
```
Type:       REST API service (physical mail sending)
Auth:       Internal API key
Data model: Letter(id, recipient_name, address_json, template_id, pdf_key, status, provider_id, sent_at)
Features:   - Render a letter PDF from a template and variables
            - Validate the postal address before sending
            - Send it through a print-and-mail provider API
            - Track status from printed to delivered
API:        REST
            POST /letters
            GET  /letters/{id}
Storage:    PostgreSQL, S3
Tech stack: Node.js, Lob API, Puppeteer
```

---

## Example 252

**Intent:**
contract templates in word, fill in client name, price, dates and make the final docx and pdf

**Spec:**
```
Type:       REST API service (document template filling)
Auth:       Staff API token
Data model: Template(id, name, docx_key, fields_json)
            GeneratedDocument(id, template_id -> Template, values_json, docx_key, pdf_key, created_at)
Features:   - Upload Word templates with placeholders like {{client_name}}
            - Fill placeholders, tables and conditional sections
            - Output DOCX and PDF
            - Check that all required fields are provided
API:        REST
            POST /templates
            POST /templates/{id}/generate
Storage:    PostgreSQL, S3
Tech stack: Python, docxtpl, LibreOffice headless, FastAPI
```

---

## Example 253

**Intent:**
customers upload csv files and half of them are broken. validate them and tell them exactly which rows are wrong

**Spec:**
```
Type:       REST API service (CSV validation)
Data model: ImportSchema(id, name, columns_json)
            ValidationRun(id, schema_id -> ImportSchema, filename, row_count, error_count, created_at)
Features:   - Detect delimiter and encoding automatically
            - Check required columns, types, formats and unique keys
            - Return errors with row number, column and message
            - Return a cleaned file with valid rows only
API:        REST
            POST /schemas/{id}/validate
            GET  /runs/{id}/errors
Storage:    PostgreSQL
Tech stack: Python, Frictionless Framework, FastAPI
```

---

## Example 254

**Intent:**
compare data between production db and the new reporting db, find rows that dont match

**Spec:**
```
Type:       Command-line tool (database diff)
Features:   - Compare tables between two databases by primary key
            - Use checksums on row ranges to find differences fast
            - List missing, extra and changed rows
            - Work across different database engines
Input:      Two connection strings, table names
Tech stack: Python, reladiff, Click
```

---

## Example 255

**Intent:**
Every feature branch should get its own copy of the database for testing, created in seconds.

**Spec:**
```
Type:       Infrastructure setup (database branching)
Features:   - Create a copy-on-write database branch per Git branch
            - Inject the branch connection string into preview deployments
            - Reset a branch to the latest production schema
            - Delete branches when the Git branch is deleted
Storage:    Neon serverless PostgreSQL
Tech stack: Neon API, GitHub Actions, Vercel
```

---

## Example 256

**Intent:**
a partner api we use is slow and has a small quota. put a cache in front so we call it less

**Spec:**
```
Type:       REST API service (caching proxy)
Features:   - Forward requests to the partner API
            - Cache GET responses by URL with per-path TTLs
            - Serve stale data while refreshing in the background
            - Coalesce identical concurrent requests into one
            - Expose hit and miss counts
API:        REST
            GET  /partner/{path}
            GET  /cache/stats
Storage:    Redis
Tech stack: Go, groupcache-style singleflight, go-redis
```

---

## Example 257

**Intent:**
People send huge GraphQL queries that kill our server. Limit how expensive a query can be.

**Spec:**
```
Type:       GraphQL API service (query cost limiting)
Auth:       API key per client
Features:   - Calculate query cost from field weights and list sizes before execution
            - Reject queries above a max cost or depth
            - Give each client a cost budget per minute
            - Return remaining budget in response extensions
            - Allow only persisted queries for anonymous clients
API:        GraphQL
            POST /graphql
Storage:    Redis (budgets)
Tech stack: TypeScript, GraphQL Yoga, graphql-query-complexity
```

---

## Example 258

**Intent:**
We want other companies to build apps on our platform, so they need OAuth to access our users' data with permission.

**Spec:**
```
Type:       REST API service (OAuth 2.0 authorization server)
Auth:       OAuth 2.0 authorization code flow with PKCE
Data model: ClientApp(id, name, client_id, client_secret_hash, redirect_uris, owner_id)
            Grant(id, user_id, client_app_id -> ClientApp, scopes, created_at, revoked_at)
            AccessToken(id, grant_id -> Grant, token_hash, expires_at)
Features:   - Register third-party apps with redirect URIs
            - Show a consent screen listing requested scopes
            - Issue access and refresh tokens
            - Let users revoke apps from their settings
API:        REST
            GET  /oauth/authorize
            POST /oauth/token
            POST /oauth/revoke
Storage:    PostgreSQL
Tech stack: Python, Django, django-oauth-toolkit
```

---

## Example 259

**Intent:**
make our app work with zapier so users can connect it to other tools

**Spec:**
```
Type:       REST API service (Zapier integration)
Auth:       OAuth 2.0 or API key for Zapier connections
Data model: HookSubscription(id, account_id, event, target_url, created_at)
Features:   - Provide REST hook subscribe and unsubscribe endpoints for triggers
            - Send new-record events to subscribed Zapier URLs
            - Offer polling endpoints with sample data for setup
            - Provide actions to create records
API:        REST
            POST /zapier/hooks
            DELETE /zapier/hooks/{id}
            GET  /zapier/triggers/new-contact
            POST /zapier/actions/create-contact
Storage:    PostgreSQL
Tech stack: Node.js, Express, Zapier Platform CLI
```

---

## Example 260

**Intent:**
messages that fail in our queue end up in a dead letter queue and we never look. need a tool to see and replay them

**Spec:**
```
Type:       Web application (dead-letter queue manager)
Auth:       Engineer SSO login
Features:   - List messages in dead-letter queues with error reasons
            - Show message body and headers
            - Replay selected messages to the original queue
            - Edit a message before replay
            - Purge messages older than 14 days
API:        REST
            GET  /queues/{name}/dead-letters
            POST /queues/{name}/dead-letters/replay
Tech stack: Python, Flask, Amazon SQS, boto3
```

---

## Example 261

**Intent:**
Workers should scale up when the queue has lots of jobs and down to zero at night.

**Spec:**
```
Type:       Infrastructure setup (queue-based autoscaling)
Features:   - Scale worker pods by queue length
            - Scale to zero when the queue is empty for 10 minutes
            - Cap the maximum number of workers
            - Drain jobs gracefully before a pod stops
Tech stack: Kubernetes, KEDA, RabbitMQ, Helm
```

---

## Example 262

**Intent:**
our lab has 4 GPU machines and 15 phd students fighting over them. need a queue system

**Spec:**
```
Type:       Infrastructure setup (GPU job scheduler)
Auth:       Lab Linux accounts via LDAP
Features:   - Submit training jobs with requested GPUs and time limit
            - Queue jobs fairly across users
            - Kill jobs that exceed their time limit
            - Show the queue and GPU usage per user
            - Run jobs in containers with the user's environment
Tech stack: Slurm, Enroot/Pyxis, NVIDIA drivers, Ansible
```

---

## Example 263

**Intent:**
I'm teaching a Python course with 60 students. Each needs a Jupyter notebook in the browser without installing anything.

**Spec:**
```
Type:       Infrastructure setup (classroom notebook server)
Auth:       Login with university accounts through OAuth
Features:   - Start a personal notebook server for each student
            - Give each student persistent storage
            - Distribute and collect assignments
            - Cull idle servers after 1 hour
            - Limit CPU and memory per student
Storage:    Persistent volumes per user
Tech stack: JupyterHub, Kubernetes, nbgrader
```

---

## Example 264

**Intent:**
api that runs untrusted code from students safely and returns the output, for an online judge

**Spec:**
```
Type:       REST API service (sandboxed code execution)
Auth:       API key for the judge platform
Data model: Submission(id, language, source_code, stdin, status, stdout, stderr, time_ms, memory_kb)
Features:   - Run code in Python, C++, Java and JavaScript
            - Isolate each run with no network and a read-only filesystem
            - Enforce CPU time, memory and output limits
            - Compare output to expected answers for test cases
API:        REST
            POST /submissions
            GET  /submissions/{id}
Storage:    PostgreSQL, Redis (queue)
Tech stack: Judge0, Docker, isolate
```

---

## Example 265

**Intent:**
run our browser tests in parallel on many chrome and firefox instances

**Spec:**
```
Type:       Infrastructure setup (browser test grid)
Features:   - Run a grid with Chrome, Firefox and Edge nodes
            - Scale nodes up when tests are waiting
            - Record videos of each test session
            - Run as part of the test environment on Kubernetes
Tech stack: Selenium Grid 4, Docker, Kubernetes, KEDA
```

---

## Example 266

**Intent:**
Our suppliers email order confirmations as PDFs. Read them and update the order status in our system.

**Spec:**
```
Type:       Data pipeline (supplier email parsing)
Data model: PurchaseOrder(id, po_number, supplier_id, status, confirmed_delivery_date)
            InboundEmail(id, from_address, subject, attachment_key, parsed, received_at)
Features:   - Read a dedicated mailbox over IMAP every 5 minutes
            - Extract text from PDF attachments
            - Find the PO number, delivery date and prices with per-supplier rules
            - Update the purchase order and flag price differences
            - Move unparsed emails to a review folder
Storage:    PostgreSQL
Tech stack: Python, imap-tools, pdfplumber
```

---

## Example 267

**Intent:**
Employees forward their receipts to expenses@ourcompany and the expense gets created for them.

**Spec:**
```
Type:       Webhook service (expense email intake)
Data model: Employee(id, email, name)
            Expense(id, employee_id -> Employee, merchant, amount, currency, date, receipt_key, status)
Features:   - Receive forwarded emails through the inbound mail webhook
            - Match the sender to an employee
            - Extract amount, date and merchant from the receipt with OCR
            - Create a draft expense for the employee to confirm
            - Reply to the sender with a link to the draft
API:        REST
            POST /webhooks/inbound
Storage:    PostgreSQL, S3
Tech stack: Ruby on Rails, Postmark inbound, AWS Textract
```

---

## Example 268

**Intent:**
food bank: people text JOIN to a number and get SMS when we have food distribution days

**Spec:**
```
Type:       Webhook service (SMS keyword subscriptions)
Data model: Subscriber(id, phone, language, subscribed, joined_at)
            Broadcast(id, message, sent_by, sent_at, recipient_count)
Features:   - Subscribe numbers that text JOIN
            - Unsubscribe numbers that text STOP
            - Let staff send a broadcast from a web form
            - Send in Spanish to subscribers who chose it
API:        REST
            POST /sms/inbound
            POST /broadcasts
Storage:    SQLite
Tech stack: Python, Flask, Twilio Messaging
```

---

## Example 269

**Intent:**
I rent two apartments on Airbnb and Booking.com. I keep getting double bookings because the calendars don't talk.

**Spec:**
```
Type:       Scheduled script (vacation rental calendar sync)
Data model: Property(id, name)
            ChannelCalendar(id, property_id -> Property, channel, import_ical_url)
            BlockedDate(property_id -> Property, start_date, end_date, source)
Features:   - Import iCal feeds from each platform every 10 minutes
            - Merge booked dates per property
            - Publish one combined iCal export per property for each platform to import
            - Email me when two bookings overlap
API:        REST
            GET  /export/{property_id}.ics
Storage:    SQLite
Tech stack: Python, icalendar, Flask
```

---

## Example 270

**Intent:**
meeting rooms booked in google calendar, show availability on a tablet outside each room

**Spec:**
```
Type:       Web application (meeting room display)
Auth:       Device token per tablet
Data model: Room(id, name, google_resource_email)
Features:   - Show the current and next meetings for the room
            - Show free or busy in large colors
            - Book the room now for 15 or 30 minutes from the tablet
            - Release rooms when nobody checks in within 10 minutes
API:        REST
            GET  /rooms/{id}/schedule
            POST /rooms/{id}/book-now
Tech stack: Node.js, Google Calendar API (resource calendars), React kiosk app
```

---

## Example 271

**Intent:**
i have an excel with 5000 customer addresses, add latitude and longitude to each

**Spec:**
```
Type:       Command-line script (batch geocoding)
Features:   - Read addresses from an Excel or CSV file
            - Geocode each address with rate limiting
            - Add latitude, longitude and match quality columns
            - Resume where it stopped if interrupted
            - Write unmatched rows to a separate file
Input:      Excel file path, address column names
Tech stack: Python, pandas, geopy, Nominatim
```

---

## Example 272

**Intent:**
store locator for our 150 shops, nearest to the user with opening hours

**Spec:**
```
Type:       REST API service (store locator)
Data model: Store(id, name, address, location geography(Point), phone)
            OpeningHours(store_id -> Store, weekday, opens_at, closes_at)
Features:   - Return the nearest stores to a coordinate or postcode
            - Show distance and whether each store is open now
            - Filter by services like click-and-collect
            - Import store data from a spreadsheet
API:        REST
            GET  /stores/nearby?lat={lat}&lon={lon}&limit={n}
            GET  /stores/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: Java, Spring Boot, Hibernate Spatial
```

---

## Example 273

**Intent:**
Real estate site: show which areas are within 20 minutes by public transport from a workplace.

**Spec:**
```
Type:       REST API service (travel-time isochrones)
Features:   - Compute reachable areas from a point within N minutes
            - Support walking, cycling, driving and public transport
            - Return polygons as GeoJSON
            - Cache results per point and time budget
API:        REST
            GET  /isochrone?lat={lat}&lon={lon}&minutes={n}&mode={mode}
Storage:    Redis (cache)
Tech stack: OpenTripPlanner, GTFS feeds, OpenStreetMap, Java
```

---

## Example 274

**Intent:**
alert me when a delivery van enters or leaves a customer area

**Spec:**
```
Type:       REST API service (geofencing)
Data model: Geofence(id, name, polygon geometry)
            GeofenceEvent(id, vehicle_id, geofence_id -> Geofence, type, occurred_at)
Features:   - Accept position updates from vehicles
            - Detect enter and exit events against all geofences
            - Ignore GPS jitter with a minimum dwell time
            - Send events to a webhook URL
API:        REST
            POST /positions
            POST /geofences
            GET  /geofences/{id}/events
Storage:    PostgreSQL with PostGIS, Redis (last known state)
Tech stack: Go, PostGIS, Redis
```

---

## Example 275

**Intent:**
hiking app needs elevation profile for a gpx route

**Spec:**
```
Type:       REST API service (elevation profile)
Features:   - Accept a GPX file or list of coordinates
            - Look up elevation for each point from a digital elevation model
            - Smooth the profile and compute total ascent and descent
            - Return the profile as JSON for charting
API:        REST
            POST /elevation/profile
Storage:    Copernicus DEM GeoTIFF tiles
Tech stack: Python, rasterio, gpxpy, FastAPI
```

---

## Example 276

**Intent:**
Show prices in our shop in the visitor's currency, but rounded nicely like 19.99 not 18.73.

**Spec:**
```
Type:       REST API service (localized pricing)
Data model: PriceList(id, currency, base_rate, rounding_rule, updated_at)
            ProductPrice(product_id, currency, price, is_override)
Features:   - Detect currency from visitor country
            - Convert base prices with daily exchange rates
            - Round to charm prices like .99 per currency rules
            - Allow manual price overrides per product and currency
            - Recalculate prices daily
API:        REST
            GET  /prices?currency={code}&products={ids}
            PUT  /products/{id}/prices/{currency}
Storage:    PostgreSQL
Tech stack: PHP, Symfony, moneyphp
```

---

## Example 277

**Intent:**
customer pays in crypto, lock the exchange rate for 15 minutes so the price doesnt change while they pay

**Spec:**
```
Type:       REST API service (crypto payment quotes)
Data model: Quote(id, order_id, fiat_amount, fiat_currency, crypto_currency, crypto_amount, rate, expires_at, status)
Features:   - Fetch the current rate from several exchanges and take the median
            - Create a quote valid for 15 minutes
            - Generate a payment address per quote
            - Mark the quote paid when the transaction is confirmed
            - Expire unpaid quotes
API:        REST
            POST /quotes
            GET  /quotes/{id}
Storage:    PostgreSQL
Tech stack: Node.js, BTCPay Server API, ccxt
```

---

## Example 278

**Intent:**
kill switch for features in our mobile app in case something breaks in production

**Spec:**
```
Type:       REST API service (feature kill switches)
Auth:       On-call engineer login for changes; app key for reads
Data model: KillSwitch(id, key, disabled, reason, changed_by, changed_at)
Features:   - Turn off a feature instantly for all users
            - Return all switches in one small cached response
            - Require a reason for every change
            - Default to enabled when the app cannot reach the server
API:        REST
            GET  /switches
            PUT  /switches/{key}
Storage:    PostgreSQL, CDN cache with 30-second TTL
Tech stack: Kotlin, Ktor, Fastly
```

---

## Example 279

**Intent:**
people try thousands of passwords on our login page. slow them down

**Spec:**
```
Type:       REST API service (login brute-force protection)
Data model: LoginAttempt(id, username, ip, success, attempted_at)
Features:   - Count failed logins per username and per IP
            - Add increasing delays after 5 failures
            - Require a CAPTCHA after 10 failures
            - Temporarily lock the account and email the owner after 20
            - Never reveal if a username exists
API:        REST
            POST /login
Storage:    Redis (counters), PostgreSQL (attempt log)
Tech stack: Python, FastAPI, Redis
```

---

## Example 280

**Intent:**
Our customers' API keys never get rotated. Remind them when a key is older than 90 days and let them roll it with overlap.

**Spec:**
```
Type:       REST API service (API key rotation)
Auth:       Customer dashboard login
Data model: ApiKey(id, account_id, key_hash, created_at, expires_at, replaced_by_id)
Features:   - Email owners when a key is older than 90 days
            - Create a replacement key while the old key keeps working for 7 days
            - Expire the old key automatically after the overlap
            - Show key age in the dashboard
API:        REST
            POST /keys/{id}/roll
            GET  /keys
Storage:    PostgreSQL
Tech stack: Go, PostgreSQL, Postmark
```

---

## Example 281

**Intent:**
web hosting company, need to bill customers for bandwidth they use each month

**Spec:**
```
Type:       Data pipeline (bandwidth metering)
Data model: Customer(id, name)
            Site(id, customer_id -> Customer, hostname)
            BandwidthDaily(site_id -> Site, date, bytes_out)
Features:   - Parse CDN and web server access logs every hour
            - Sum bytes sent per site per day
            - Aggregate to monthly totals per customer
            - Calculate charges above the included bandwidth
            - Push monthly usage to the billing system
Storage:    ClickHouse
Tech stack: Vector, ClickHouse, Python
```

---

## Example 282

**Intent:**
scan our website and list all cookies and trackers it sets, for our privacy policy

**Spec:**
```
Type:       Command-line tool (cookie scanner)
Features:   - Crawl up to N pages with a headless browser
            - Record every cookie with domain, expiry and first page seen
            - Detect third-party scripts and trackers
            - Check whether cookies are set before consent
            - Export a report as CSV and HTML
Input:      Website URL, max pages
Tech stack: Node.js, Playwright, Commander.js
```

---

## Example 283

**Intent:**
record every change in our important tables automatically, at the database level, even if someone uses SQL directly

**Spec:**
```
Type:       Infrastructure setup (database-level audit trail)
Data model: AuditRecord(id, table_name, record_id, operation, old_data jsonb, new_data jsonb, db_user, changed_at)
Features:   - Attach triggers to selected tables for insert, update and delete
            - Store old and new row values as JSON
            - Record the database user and application user
            - Partition audit records by month
Storage:    PostgreSQL
Tech stack: PostgreSQL triggers (PL/pgSQL), pgAudit
```

---

## Example 284

**Intent:**
Every morning send the founders an email with yesterday's signups, revenue and active users.

**Spec:**
```
Type:       Scheduled script (daily KPI email)
Features:   - Query signups and active users from the app database
            - Fetch yesterday's revenue from the payment provider
            - Compare each number with the same day last week
            - Send a short HTML email at 8:00
Input:      Database URL, payment API key, recipient list
Tech stack: Node.js, node-cron, Stripe API, Nodemailer
```

---

## Example 285

**Intent:**
every friday a pdf of what our team finished in jira this week for the client

**Spec:**
```
Type:       Scheduled script (weekly Jira report)
Features:   - Query issues resolved this week with JQL
            - Group them by epic
            - Render a branded PDF with a summary table
            - Email it to the client contact on Friday at 16:00
Input:      Jira project key, API token, client email
Tech stack: Python, jira library, WeasyPrint, cron
```

---

## Example 286

**Intent:**
let developers spin up a full staging copy of the app from the terminal and tear it down after

**Spec:**
```
Type:       Command-line tool (on-demand staging)
Features:   - Create a staging environment for a branch with one command
            - Provision app containers, database and DNS name
            - Print the URL and credentials when ready
            - List running environments with owner and age
            - Destroy environments automatically after 48 hours
Input:      Branch name, optional time-to-live
Tech stack: Go, Cobra, Terraform, AWS ECS
```

---

## Example 287

**Intent:**
how do i do blue green deploys when the new version also changes the database schema?

**Spec:**
```
Type:       Infrastructure setup (blue-green with schema migrations)
Features:   - Split schema changes into expand and contract steps
            - Apply expand migrations before deploying the new version
            - Run old and new versions against the same database during switch
            - Switch traffic to the new version after health checks
            - Apply contract migrations only after the old version is retired
Storage:    PostgreSQL
Tech stack: Flyway, Kubernetes, Argo Rollouts
```

---

## Example 288

**Intent:**
internal services use TLS certs from our own CA and they keep expiring. renew them automatically

**Spec:**
```
Type:       Infrastructure setup (internal certificate automation)
Features:   - Run an internal ACME certificate authority
            - Issue 30-day certificates to services automatically
            - Renew certificates at two-thirds of their lifetime
            - Reload services after renewal
            - Distribute the root CA to all servers
Tech stack: step-ca, certbot, Ansible
```

---

## Example 289

**Intent:**
rotate the api tokens we use for third party services like sendgrid and twilio without downtime

**Spec:**
```
Type:       Scheduled script (third-party credential rotation)
Features:   - Create a new API key with each provider's API
            - Store the new key in the secrets manager
            - Trigger a rolling restart of services using the key
            - Delete the old key after services report healthy
            - Log each rotation result
Input:      Rotation config listing providers and secret names
Tech stack: Python, AWS Secrets Manager rotation Lambda, SendGrid API, Twilio API
```

---

## Example 290

**Intent:**
MongoDB on one server only, make it highly available

**Spec:**
```
Type:       Infrastructure setup (MongoDB replica set)
Features:   - Deploy a three-member replica set across availability zones
            - Enable automatic primary election
            - Use keyfile authentication between members
            - Set app connection strings with readPreference and retryWrites
            - Monitor replication lag
Storage:    MongoDB 7
Tech stack: MongoDB, Ansible, Percona Monitoring and Management
```

---

## Example 291

**Intent:**
our redis cache goes down sometimes and the whole app breaks. make it fail over automatically

**Spec:**
```
Type:       Infrastructure setup (Redis high availability)
Features:   - Run one Redis primary and two replicas
            - Run three Sentinel processes to detect failure and promote a replica
            - Configure clients to discover the primary through Sentinel
            - Make the app fall back to the database when cache is unavailable
Storage:    Redis
Tech stack: Redis Sentinel, Docker Compose, redis-py
```

---

## Example 292

**Intent:**
I want cameras at home recording to my own server, with person detection, no cloud subscription

**Spec:**
```
Type:       Infrastructure setup (home NVR)
Features:   - Record RTSP streams from IP cameras continuously
            - Detect people and cars with a local AI accelerator
            - Save event clips and snapshots
            - Send phone notifications for detected people
            - Keep recordings 14 days and events 30 days
Storage:    Local disk
Tech stack: Frigate, Google Coral TPU, Home Assistant, Docker
```

---

## Example 293

**Intent:**
run chatgpt-like models on my own gaming pc and use them from any device at home

**Spec:**
```
Type:       Infrastructure setup (home LLM server)
Auth:       User accounts in the web UI
Features:   - Run open-weight language models on the local GPU
            - Expose an OpenAI-compatible API on the home network
            - Provide a chat web interface for family devices
            - Download and switch between models
Tech stack: Ollama, Open WebUI, Docker, NVIDIA Container Toolkit
```

---

## Example 294

**Intent:**
start page for my homelab with links and status of every service

**Spec:**
```
Type:       Infrastructure setup (homelab dashboard)
Features:   - Show tiles for each self-hosted service with icons
            - Display service status from Docker labels
            - Show widgets for disk usage, weather and media stats
            - Configure everything from YAML files
Tech stack: Homepage, Docker, YAML config
```

---

## Example 295

**Intent:**
ebook library on my server so I can read on my kindle and phone

**Spec:**
```
Type:       Infrastructure setup (self-hosted ebook library)
Auth:       User accounts per family member
Features:   - Serve an existing Calibre library through a web interface
            - Read books in the browser
            - Send books to a Kindle by email
            - Provide an OPDS feed for reading apps
Storage:    Calibre library folder (SQLite metadata)
Tech stack: Calibre-Web, Docker
```

---

## Example 296

**Intent:**
connect our two office networks in different cities permanently so they act like one

**Spec:**
```
Type:       Infrastructure setup (site-to-site VPN)
Features:   - Create an IPsec tunnel between the two office firewalls
            - Route each office's subnet through the tunnel
            - Restart the tunnel automatically after outages
            - Allow only needed ports between the sites
Tech stack: pfSense, IPsec IKEv2
```

---

## Example 297

**Intent:**
Company VPN for 50 remote employees, each person only gets access to the systems their team needs.

**Spec:**
```
Type:       Infrastructure setup (zero-trust remote access)
Auth:       Company SSO with MFA
Features:   - Install a client on employee laptops that connects after SSO login
            - Grant access to internal resources by team group
            - Check device posture like disk encryption before connecting
            - Log every connection
Tech stack: Netbird (self-hosted), Keycloak, WireGuard
```

---

## Example 298

**Intent:**
my hugo blog needs hosting with a contact form and automatic deploy from github

**Spec:**
```
Type:       Infrastructure setup (static site hosting with forms)
Features:   - Build the Hugo site on each push to main
            - Deploy to a CDN with HTTPS on a custom domain
            - Handle the contact form with built-in form processing
            - Create preview deploys for pull requests
Tech stack: Hugo, Netlify, Netlify Forms
```

---

## Example 299

**Intent:**
agency with 30 small client websites, all static. host them all cheaply in one setup

**Spec:**
```
Type:       Infrastructure setup (multi-site static hosting)
Features:   - Store each site in its own folder of one bucket
            - Route each custom domain to its folder with an edge function
            - Issue certificates for all domains automatically
            - Deploy a site with one command per client
Storage:    Cloudflare R2
Tech stack: Cloudflare Workers, Cloudflare R2, Wrangler CLI
```

---

## Example 300

**Intent:**
We run an airport shuttle. Check the flights of today's pickups and text the driver when a flight is delayed.

**Spec:**
```
Type:       Scheduled script (flight arrival tracking)
Data model: Pickup(id, flight_number, scheduled_arrival, estimated_arrival, driver_phone, notified_at)
Features:   - Check flight status every 10 minutes for today's pickups
            - Detect delays over 15 minutes and cancellations
            - Text the assigned driver the new arrival time
            - Update the pickup schedule
Storage:    SQLite
Tech stack: Python, AeroDataBox API, Twilio
```

---

## Example 301

**Intent:**
iphone photos are heic and our website wont accept them, convert on upload

**Spec:**
```
Type:       REST API service (HEIC conversion)
Features:   - Accept HEIC and HEIF uploads
            - Convert to JPEG or WebP keeping orientation
            - Keep or strip EXIF metadata based on a flag
            - Reject files over 25 MB
API:        REST
            POST /convert?format={jpeg|webp}
Tech stack: Python, pillow-heif, FastAPI
```

---

## Example 302

**Intent:**
Merge, split and compress PDFs through an API so our office staff stop using random websites with customer documents.

**Spec:**
```
Type:       REST API service (PDF utilities)
Auth:       Company SSO for the web UI; internal API token
Features:   - Merge several PDFs in a chosen order
            - Split a PDF by page ranges
            - Compress PDFs by downsampling images
            - Delete all files right after processing
            - Provide a simple internal web page for staff
API:        REST
            POST /pdf/merge
            POST /pdf/split
            POST /pdf/compress
Tech stack: Python, pikepdf, Ghostscript, FastAPI
```

---

## Example 303

**Intent:**
fill official government pdf forms automatically from our client data

**Spec:**
```
Type:       REST API service (PDF form filling)
Data model: FormTemplate(id, name, pdf_key, field_mapping_json)
            FilledForm(id, template_id -> FormTemplate, client_id, pdf_key, created_at)
Features:   - Read AcroForm field names from uploaded government PDFs
            - Map client data fields to form fields
            - Fill text fields, checkboxes and dates
            - Flatten the result so fields cannot be edited
API:        REST
            POST /templates
            POST /templates/{id}/fill
Storage:    PostgreSQL, S3
Tech stack: Java, Apache PDFBox, Spring Boot
```

---

## Example 304

**Intent:**
I need our customers to sign contracts online with a legally valid signature and a full audit trail.

**Spec:**
```
Type:       Web application (e-signature workflow)
Auth:       Sender login; signers via emailed one-time link with SMS code
Data model: Envelope(id, sender_id, title, status, created_at, completed_at)
            Signer(id, envelope_id -> Envelope, email, phone, order, signed_at, ip)
            Document(id, envelope_id -> Envelope, original_key, signed_key)
Features:   - Upload a PDF and place signature fields for each signer
            - Send signing requests in order
            - Verify signers with an SMS code
            - Seal the final PDF with a digital certificate
            - Attach an audit trail page with timestamps and IPs
API:        REST
            POST /envelopes
            POST /envelopes/{id}/send
            POST /sign/{token}
Storage:    PostgreSQL, S3
Tech stack: Documenso (self-hosted), Next.js
```

---

## Example 305

**Intent:**
print shipping labels with barcodes for our parcels, 4x6 inch

**Spec:**
```
Type:       REST API service (shipping label generation)
Data model: Label(id, tracking_number, sender_json, recipient_json, weight_g, format, file_key)
Features:   - Generate a tracking number with check digit
            - Render a 4x6 inch label with Code 128 barcode and addresses
            - Output as PDF or ZPL for thermal printers
            - Create labels in batches for a day's orders
API:        REST
            POST /labels
            POST /labels/batch
            GET  /labels/{id}
Storage:    PostgreSQL, S3
Tech stack: Python, reportlab, python-barcode, FastAPI
```

---

## Example 306

**Intent:**
we send SMS campaigns and want a short link per person so we know exactly who clicked

**Spec:**
```
Type:       REST API service (personalized short links)
Data model: Campaign(id, name, target_url)
            RecipientLink(id, campaign_id -> Campaign, recipient_id, code, clicked_at, click_count)
Features:   - Generate a unique 6-character code per recipient in bulk
            - Redirect clicks to the campaign URL with UTM parameters
            - Record first click time and total clicks per recipient
            - Export clickers for follow-up
API:        REST
            POST /campaigns/{id}/links
            GET  /c/{code}
            GET  /campaigns/{id}/clicks
Storage:    PostgreSQL, Redis (code lookup)
Tech stack: Go, Fiber, PostgreSQL
```

---

## Example 307

**Intent:**
Our construction sites must stop crane work when wind is too strong. Check the forecast each morning and warn site managers.

**Spec:**
```
Type:       Scheduled script (site weather warnings)
Data model: Site(id, name, latitude, longitude, manager_phone, wind_limit_kmh)
Features:   - Fetch the hourly forecast for each site at 5:00
            - Find hours where wind gusts exceed the site limit
            - Text the site manager the risky hours
            - Also warn about heavy rain and frost
Storage:    SQLite
Tech stack: Python, Open-Meteo API, Twilio
```

---

## Example 308

**Intent:**
bike share stations from several cities in one api, how many bikes are free

**Spec:**
```
Type:       REST API service (bike share aggregator)
Data model: System(id, city, gbfs_url)
            Station(id, system_id -> System, name, latitude, longitude, capacity)
            StationStatus(station_id -> Station, bikes_available, docks_available, updated_at)
Features:   - Poll GBFS feeds from each city every minute
            - Normalize stations and availability into one format
            - Return stations near a location with free bikes
            - Keep hourly history for analysis
API:        REST
            GET  /stations/nearby?lat={lat}&lon={lon}
            GET  /systems
Storage:    PostgreSQL
Tech stack: Node.js, TypeScript, Fastify, node-cron
```

---

## Example 309

**Intent:**
library catalog of our town as an open API, books, availability per branch

**Spec:**
```
Type:       REST API service (library catalog)
Data model: Title(id, isbn, title, authors, year, subjects)
            Copy(id, title_id -> Title, branch_id -> Branch, barcode, status, due_date)
            Branch(id, name, address)
Features:   - Export records nightly from the library system in MARC format
            - Search titles by keyword, author and ISBN
            - Show copies available per branch
            - Serve data under an open license with CORS
API:        REST
            GET  /titles?q={query}
            GET  /titles/{id}/availability
Storage:    PostgreSQL
Tech stack: Python, pymarc, Django REST Framework
```

---

## Example 310

**Intent:**
We want feature flags but stored as files in git and reviewed in pull requests, not in some web UI.

**Spec:**
```
Type:       Infrastructure setup (GitOps feature flags)
Features:   - Define flags and targeting rules in YAML files in a repository
            - Validate flag files in CI
            - Sync flag files to a flag daemon in each environment
            - Evaluate flags in apps with a standard SDK
Tech stack: OpenFeature, flagd, GitHub Actions, Kubernetes
```

---

## Example 311

**Intent:**
customers submit render jobs to our platform, limit each one to 3 running at the same time based on their plan

**Spec:**
```
Type:       REST API service (per-tenant concurrency limits)
Auth:       Customer API key
Data model: Tenant(id, plan, max_concurrent_jobs)
            Job(id, tenant_id -> Tenant, status, queued_at, started_at, finished_at)
Features:   - Queue jobs per tenant
            - Start a job only when the tenant is under its concurrency limit
            - Use fair scheduling across tenants
            - Show queue position to the customer
API:        REST
            POST /jobs
            GET  /jobs/{id}
Storage:    PostgreSQL, Redis (semaphores)
Tech stack: Python, FastAPI, Dramatiq
```

---

## Example 312

**Intent:**
When we manufacture a sensor, give it unique credentials so it can connect to our cloud securely.

**Spec:**
```
Type:       IoT system (device provisioning)
Auth:       X.509 device certificates signed by our CA
Data model: Device(id, serial_number, certificate_fingerprint, provisioned_at, status)
            ProvisioningBatch(id, factory, created_at, count)
Features:   - Generate a key pair and certificate per device at the factory station
            - Register devices with the IoT cloud in batches
            - Attach a policy that allows each device only its own topics
            - Revoke certificates of stolen or broken devices
API:        REST
            POST /batches
            POST /devices/{serial}/revoke
Storage:    PostgreSQL
Tech stack: Python, cryptography, AWS IoT Core
```

---

## Example 313

**Intent:**
we sell hosted ci runners, charge customers per build minute

**Spec:**
```
Type:       Data pipeline (build minute metering)
Data model: Customer(id, name, included_minutes)
            BuildRun(id, customer_id -> Customer, runner_type, started_at, finished_at, billed_minutes)
Features:   - Receive job start and finish events from runners
            - Round each job up to the next minute and apply a runner multiplier
            - Total minutes per customer per month
            - Send overage to the billing system at month end
Storage:    PostgreSQL
Tech stack: Go, NATS, PostgreSQL
```

---

## Example 314

**Intent:**
I'm subscribed to too many email newsletters. Turn them into an RSS feed I can read in my reader.

**Spec:**
```
Type:       Webhook service (newsletter to RSS)
Data model: Feed(id, name, inbox_address)
            Item(id, feed_id -> Feed, subject, sender, html, received_at)
Features:   - Give each feed a unique email address
            - Receive emails through the inbound mail webhook
            - Store the HTML content of each newsletter
            - Publish each feed as an Atom file
API:        REST
            POST /inbound
            GET  /feeds/{id}.atom
Storage:    SQLite
Tech stack: Python, Flask, Cloudflare Email Workers, feedgen
```

---

## Example 315

**Intent:**
let me publish blog posts by sending an email from my phone

**Spec:**
```
Type:       Webhook service (email to blog)
Data model: Post(id, title, body_markdown, images_json, published_at, status)
Features:   - Accept emails only from my address with a valid DKIM signature
            - Use the subject as title and the body as Markdown
            - Upload attached photos and insert them in the post
            - Commit the post to the blog repository to trigger a build
API:        REST
            POST /inbound-email
Tech stack: Node.js, SendGrid Inbound Parse, GitHub API, Eleventy
```

---

## Example 316

**Intent:**
delivery drivers should confirm each drop by replying to an SMS with the stop number, we have no app

**Spec:**
```
Type:       Webhook service (SMS delivery confirmation)
Data model: Driver(id, name, phone)
            Stop(id, driver_id -> Driver, number, address, status, confirmed_at)
Features:   - Text each driver their stop list in the morning
            - Parse replies like "DONE 4" or "FAIL 4 nobody home"
            - Update the stop status and reason
            - Show dispatchers a live board of stops
API:        REST
            POST /sms/inbound
            GET  /board
Storage:    PostgreSQL
Tech stack: Ruby, Sinatra, Plivo SMS API
```

---

## Example 317

**Intent:**
customer satisfaction survey by SMS after each repair, rate 1-5 and optional comment

**Spec:**
```
Type:       Webhook service (SMS survey)
Data model: Repair(id, customer_phone, technician_id, completed_at)
            SurveyResponse(id, repair_id -> Repair, rating, comment, received_at)
Features:   - Send the survey SMS 2 hours after a repair is completed
            - Accept a number 1-5 as rating and ask for an optional comment
            - Link replies to the repair by phone number and time
            - Show average ratings per technician
API:        REST
            POST /webhooks/repair-completed
            POST /sms/inbound
            GET  /reports/technicians
Storage:    PostgreSQL
Tech stack: Python, Django, MessageBird API
```

---

## Example 318

**Intent:**
my kid's football league has a fixture list in a spreadsheet. make it a calendar parents subscribe to, per team

**Spec:**
```
Type:       Web application (fixture calendar feeds)
Data model: Team(id, name, slug)
            Fixture(id, home_team_id -> Team, away_team_id -> Team, kickoff_at, pitch)
Features:   - Import fixtures from a Google Sheet
            - Publish one .ics feed per team
            - Update feeds when a match is moved
            - Add pitch location to each event
API:        REST
            GET  /teams/{slug}.ics
Storage:    SQLite
Tech stack: Python, gspread, icalendar, Flask
```

---

## Example 319

**Intent:**
lots of users upload the same files, store each file only once to save space

**Spec:**
```
Type:       REST API service (deduplicated file storage)
Data model: Blob(sha256, size_bytes, storage_key, ref_count)
            UserFile(id, user_id, filename, blob_sha256 -> Blob, uploaded_at)
Features:   - Hash files during upload
            - Store a blob once and point user files at it
            - Increment and decrement reference counts
            - Delete blobs when no file references them
            - Check hash before upload so clients can skip sending known files
API:        REST
            POST /files
            HEAD /blobs/{sha256}
            DELETE /files/{id}
Storage:    PostgreSQL, S3
Tech stack: Go, PostgreSQL, minio-go
```

---

## Example 320

**Intent:**
job board search with location, show jobs within 30 km

**Spec:**
```
Type:       REST API service (job search)
Data model: JobPosting(id, title, company, description, location geo_point, salary_min, salary_max, posted_at)
Features:   - Full-text search on title and description
            - Filter by distance from a city or coordinate
            - Filter by salary range and posting age
            - Sort by relevance or newest
            - Expire postings after 60 days
API:        REST
            GET  /jobs?q={text}&lat={lat}&lon={lon}&radius_km={n}
Storage:    Elasticsearch
Tech stack: Python, Elasticsearch, FastAPI
```

---

## Example 321

**Intent:**
A news site wants "read next" suggestions at the end of each article based on what readers actually read.

**Spec:**
```
Type:       REST API service (article recommendations)
Data model: ReadEvent(id, reader_id, article_id, read_seconds, read_at)
            ArticleEmbedding(article_id, vector)
Features:   - Record read events with time spent
            - Combine co-reading signals with content similarity
            - Prefer fresh articles from the last 7 days
            - Exclude articles the reader already read
API:        REST
            POST /events/read
            GET  /recommendations?article={id}&reader={id}
Storage:    Redis, PostgreSQL with pgvector
Tech stack: Python, implicit, sentence-transformers, FastAPI
```

---

## Example 322

**Intent:**
fashion shop: show visually similar products when you look at a dress

**Spec:**
```
Type:       REST API service (visual similarity)
Data model: ProductImage(product_id, image_url, embedding vector(512))
Features:   - Compute image embeddings for every product photo
            - Find nearest products by vector similarity
            - Filter results to the same category and in-stock items
            - Embed new products when they are added
API:        REST
            GET  /similar/{product_id}
            POST /products/{id}/embed
Storage:    Qdrant
Tech stack: Python, open_clip, Qdrant, FastAPI
```

---

## Example 323

**Intent:**
refrigerated trucks need temperature logs for food safety, alert if cargo gets too warm

**Spec:**
```
Type:       IoT system (cold chain monitoring)
Data model: Truck(id, plate)
            Shipment(id, truck_id -> Truck, min_temp_c, max_temp_c, started_at, ended_at)
            TempReading(truck_id -> Truck, temperature_c, latitude, longitude, recorded_at)
Features:   - Receive readings from cellular loggers every 2 minutes
            - Alert the driver and dispatcher when out of range for 10 minutes
            - Store readings offline on the device and upload later
            - Produce a temperature report PDF per shipment for the customer
API:        REST
            POST /readings
            GET  /shipments/{id}/report.pdf
Storage:    TimescaleDB
Tech stack: Node.js, MQTT, TimescaleDB, Puppeteer
```

---

## Example 324

**Intent:**
I keep bees. Put a scale under the hive and send the weight to a website daily so I know when honey is ready.

**Spec:**
```
Type:       IoT system (beehive scale)
Data model: Hive(id, name)
            WeightReading(hive_id -> Hive, weight_kg, temperature_c, battery_v, recorded_at)
Features:   - Read load cells with an HX711 on an ESP32
            - Send readings over LoRa or Wi-Fi every hour
            - Sleep between readings to save solar battery
            - Chart weight per hive and flag sudden drops from swarming
Storage:    InfluxDB
Tech stack: ESP32, Arduino, HX711, InfluxDB, Grafana
```

---

## Example 325

**Intent:**
parking lot with sensors in each spot, show free spaces on a sign and website

**Spec:**
```
Type:       IoT system (smart parking)
Data model: Spot(id, zone, sensor_id, occupied, changed_at)
            Zone(id, name, capacity)
Features:   - Receive occupancy changes from magnetic spot sensors
            - Count free spots per zone
            - Update the LED sign at the entrance
            - Show a live map of free spots on a website
API:        REST
            POST /sensors/events
            GET  /zones
Storage:    Redis (current state), PostgreSQL (history)
Tech stack: Node.js, LoRaWAN network server, Socket.IO
```

---

## Example 326

**Intent:**
water tank on the farm, ultrasonic sensor measures level, text me when below 20%

**Spec:**
```
Type:       IoT system (water tank level)
Features:   - Measure distance to water with an ultrasonic sensor
            - Convert distance to percent full using tank dimensions
            - Send level every 15 minutes over a cellular module
            - Text a warning below 20% and again below 10%
Storage:    ThingSpeak channel
Tech stack: Arduino, JSN-SR04T sensor, SIM7000 module, ThingSpeak, Twilio
```

---

## Example 327

**Intent:**
our electricity meter has a blinking LED, read it to know consumption live

**Spec:**
```
Type:       IoT system (smart meter LED reader)
Features:   - Count LED pulses with a photodiode on an ESP8266
            - Convert pulses to watts using the meter's impulses per kWh
            - Publish power and total energy over MQTT every 10 seconds
            - Show live and daily consumption in Home Assistant
Tech stack: ESP8266, ESPHome, MQTT, Home Assistant
```

---

## Example 328

**Intent:**
Factory motors sometimes break without warning. Put vibration sensors on them and detect when something is off.

**Spec:**
```
Type:       IoT system (vibration monitoring)
Data model: Machine(id, name, line, rated_rpm)
            VibrationFeature(machine_id -> Machine, rms, peak, dominant_freq_hz, recorded_at)
Features:   - Sample accelerometers at high rate on edge gateways
            - Compute RMS and frequency features on the edge
            - Send features every minute to the server
            - Flag anomalies against each machine's learned baseline
            - Alert maintenance staff with a trend chart
Storage:    InfluxDB
Tech stack: Python, OPC UA, scikit-learn Isolation Forest, Grafana
```

---

## Example 329

**Intent:**
support staff can log in as a customer to help them, but every time they do it must be recorded

**Spec:**
```
Type:       REST API service (audited impersonation)
Auth:       Staff SSO with support role
Data model: ImpersonationSession(id, staff_id, customer_id, reason, started_at, ended_at)
            ImpersonatedAction(id, session_id -> ImpersonationSession, method, path, at)
Features:   - Start impersonation only with a written reason
            - Issue a short-lived token that marks requests as impersonated
            - Log every request made during the session
            - Block sensitive actions like changing passwords
            - Show the customer a history of support access
API:        REST
            POST /impersonations
            DELETE /impersonations/{id}
            GET  /me/support-access
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Devise
```

---

## Example 330

**Intent:**
newsletter signups need double opt-in and we need to prove when each person agreed

**Spec:**
```
Type:       REST API service (double opt-in)
Data model: Subscriber(id, email, status, consent_text, signup_ip, signup_at, confirmed_at)
Features:   - Store the signup with the exact consent text shown
            - Send a confirmation email with a signed link
            - Mark the subscriber confirmed with time and IP
            - Delete unconfirmed signups after 7 days
API:        REST
            POST /subscribe
            GET  /confirm/{token}
Storage:    PostgreSQL
Tech stack: Go, Chi, Amazon SES
```

---

## Example 331

**Intent:**
when a customer asks to be deleted, we also have to tell mailchimp, intercom and our analytics tool to delete them

**Spec:**
```
Type:       REST API service (third-party deletion propagation)
Data model: DeletionRequest(id, customer_email, requested_at, status)
            ProcessorDeletion(id, request_id -> DeletionRequest, processor, status, response, completed_at)
Features:   - Accept a deletion request from the main app
            - Call each processor's deletion API
            - Retry failed calls daily
            - Produce a completion record per processor
API:        REST
            POST /deletions
            GET  /deletions/{id}
Storage:    PostgreSQL
Tech stack: Python, Celery, Mailchimp API, Intercom API, Mixpanel API
```

---

## Example 332

**Intent:**
school wants report cards as PDF emailed to parents at the end of term

**Spec:**
```
Type:       Scheduled script (report card mailing)
Data model: Student(id, name, class_name)
            Grade(student_id -> Student, subject, grade, teacher_comment)
            Parent(id, student_id -> Student, email)
Features:   - Collect grades and comments for each student
            - Render a report card PDF with the school logo
            - Email each parent their child's report card
            - Log delivery and resend on failure
Input:      Term name, grades export from the school system
Tech stack: Python, Jinja2, WeasyPrint, smtplib
```

---

## Example 333

**Intent:**
each developer wants their own small database with anonymized prod data, refreshed weekly

**Spec:**
```
Type:       Scheduled script (developer database snapshots)
Features:   - Take a weekly snapshot of production
            - Anonymize personal data and subset to 5% of customers keeping relations
            - Publish the snapshot as a downloadable dump
            - Provide a script developers run to load it locally
Input:      Subset rules and anonymization config
Tech stack: Greenmask, PostgreSQL, AWS S3
```

---

## Example 334

**Intent:**
our app is on AWS Lambda; shift traffic to the new version gradually

**Spec:**
```
Type:       Infrastructure setup (serverless traffic shifting)
Features:   - Publish a new Lambda version on each deploy
            - Point an alias at old and new versions with weighted traffic
            - Shift 10% every 5 minutes
            - Roll back automatically on CloudWatch error alarms
Tech stack: AWS Lambda aliases, AWS CodeDeploy, AWS SAM
```

---

## Example 335

**Intent:**
keep our secrets in the git repo but encrypted, so only the servers can decrypt them

**Spec:**
```
Type:       Infrastructure setup (encrypted secrets in Git)
Features:   - Encrypt secret values in YAML files while keeping keys readable
            - Use cloud KMS keys for production and age keys for developers
            - Decrypt at deploy time in the pipeline
            - Rotate data keys when someone leaves the team
Tech stack: SOPS, age, AWS KMS, Flux CD
```

---

## Example 336

**Intent:**
my small app uses SQLite. how do i not lose data if the server dies

**Spec:**
```
Type:       Infrastructure setup (SQLite streaming replication)
Features:   - Stream SQLite WAL changes continuously to object storage
            - Restore the database automatically when a new server starts
            - Keep point-in-time snapshots for 7 days
            - Run as a sidecar next to the app
Storage:    SQLite, S3-compatible storage
Tech stack: Litestream, Docker, Backblaze B2
```

---

## Example 337

**Intent:**
copy some tables from our main Postgres to the analytics Postgres in real time, not the whole db

**Spec:**
```
Type:       Infrastructure setup (logical replication)
Features:   - Create a publication with only the selected tables
            - Subscribe from the analytics database
            - Exclude personal columns using a column list
            - Monitor replication slot lag
Storage:    PostgreSQL 16 (source and analytics)
Tech stack: PostgreSQL logical replication, Terraform
```

---

## Example 338

**Intent:**
self hosted forgejo with its own CI runners for our open source project

**Spec:**
```
Type:       Infrastructure setup (self-hosted forge with CI)
Auth:       Accounts with 2FA; registration via approval
Features:   - Host repositories, issues and pull requests on Forgejo
            - Run CI workflows with Forgejo Actions runners
            - Isolate runners in containers per job
            - Mirror releases to a public download site
Storage:    PostgreSQL, local disk
Tech stack: Forgejo, Forgejo Runner, Docker, Caddy
```

---

## Example 339

**Intent:**
reject pushes to our git server if the commit message doesnt have a ticket number

**Spec:**
```
Type:       Command-line script (server-side Git hook)
Features:   - Run as a pre-receive hook on the Git server
            - Check each new commit message for a ticket ID like ABC-123
            - Allow merge commits and a bypass for release managers
            - Print a helpful error listing the bad commits
Input:      Ref updates from stdin
Tech stack: Bash, git, Gitea server hooks
```

---

## Example 340

**Intent:**
keep folders in sync between my 3 computers without dropbox

**Spec:**
```
Type:       Infrastructure setup (peer-to-peer file sync)
Features:   - Sync chosen folders directly between devices
            - Keep old versions of changed files for 30 days
            - Use an always-on home server as one peer
            - Ignore build folders with patterns
Tech stack: Syncthing, Docker on home server
```

---

## Example 341

**Intent:**
Audiobooks and podcasts server for the family, remembers where each person stopped.

**Spec:**
```
Type:       Infrastructure setup (self-hosted audiobook server)
Auth:       User accounts per family member
Features:   - Scan an audiobook folder and fetch metadata and covers
            - Stream to phones with progress saved per user
            - Download books for offline listening
            - Subscribe to podcast feeds and download new episodes
Storage:    Local disk
Tech stack: Audiobookshelf, Docker
```

---

## Example 342

**Intent:**
kubernetes cluster shared by 6 teams, stop one team from using all resources

**Spec:**
```
Type:       Infrastructure setup (multi-team Kubernetes)
Features:   - Give each team its own namespace
            - Set resource quotas and default limits per namespace
            - Restrict network traffic between namespaces
            - Grant team members access only to their namespace
            - Report CPU and memory cost per team
Tech stack: Kubernetes, Kyverno, Calico, Kubecost
```

---

## Example 343

**Intent:**
users all over the world, send them to the nearest server

**Spec:**
```
Type:       Infrastructure setup (latency-based routing)
Features:   - Deploy the app in three regions
            - Answer DNS with the region closest to the user
            - Remove a region from DNS when its health check fails
            - Serve static assets from a CDN
Tech stack: AWS Route 53 latency routing, AWS Global Accelerator, CloudFront
```

---

## Example 344

**Intent:**
when editors publish an article in the CMS, clear just that page from the CDN cache

**Spec:**
```
Type:       Webhook service (CDN cache purge)
Features:   - Receive the publish webhook from the CMS
            - Compute affected URLs like the article, home page and category pages
            - Purge those URLs and cache tags from the CDN
            - Retry purges that fail
API:        REST
            POST /webhooks/cms-publish
Tech stack: Node.js, Express, Fastly purge API, Contentful webhooks
```

---

## Example 345

**Intent:**
engineers should request production database access for a few hours, a lead approves, access removes itself

**Spec:**
```
Type:       Web application (just-in-time access)
Auth:       Company SSO
Data model: AccessRequest(id, requester, resource, role, reason, duration_hours, status, approver, expires_at)
Features:   - Request access to a resource with a reason and duration
            - Notify approvers and let them approve or deny
            - Grant a temporary database role on approval
            - Revoke access automatically at expiry
            - Keep a full log for audits
API:        REST
            POST /requests
            POST /requests/{id}/approve
            GET  /requests?status=active
Storage:    PostgreSQL
Tech stack: Go, HashiCorp Vault database secrets engine, React
```

---

## Example 346

**Intent:**
analysts need SQL access to production data but without seeing emails and phone numbers

**Spec:**
```
Type:       Infrastructure setup (masked read-only database access)
Auth:       Analyst SSO accounts mapped to database roles
Features:   - Create a read replica for analytics queries
            - Expose views that mask emails, phones and names
            - Grant analysts access only to masked views
            - Log every query run by analysts
            - Kill queries running over 5 minutes
Storage:    PostgreSQL read replica
Tech stack: PostgreSQL Anonymizer, pgAudit, Metabase
```

---

## Example 347

**Intent:**
invoices made in our app should appear in quickbooks automatically

**Spec:**
```
Type:       Webhook service (QuickBooks invoice sync)
Data model: SyncedInvoice(id, app_invoice_id, qbo_invoice_id, status, synced_at, error)
            CustomerMap(app_customer_id, qbo_customer_id)
Features:   - Connect the QuickBooks Online company with OAuth 2.0
            - Create or match the customer in QuickBooks
            - Create the invoice with line items and tax codes
            - Sync payment status back to the app
            - Show sync errors for manual fixing
API:        REST
            POST /webhooks/invoice-created
            POST /webhooks/quickbooks
Storage:    PostgreSQL
Tech stack: Node.js, intuit-oauth, QuickBooks Online Accounting API
```

---

## Example 348

**Intent:**
Our customer list is in our database and the marketing list is in Mailchimp, they never match. Sync them nightly.

**Spec:**
```
Type:       Scheduled script (Mailchimp audience sync)
Features:   - Read customers who opted in to marketing
            - Upsert members with merge fields like plan and signup date
            - Tag members by their product usage segment
            - Archive members who opted out in the app
            - Respect Mailchimp unsubscribes and write them back
Input:      Database URL, Mailchimp API key, audience ID
Tech stack: Python, mailchimp-marketing, SQLAlchemy
```

---

## Example 349

**Intent:**
send our purchases to facebook from the server because browser tracking is blocked a lot now

**Spec:**
```
Type:       REST API service (server-side conversion tracking)
Data model: ConversionEvent(id, event_name, event_id, order_value, currency, hashed_email, sent_at, status)
Features:   - Receive purchase events from the shop backend
            - Hash email and phone with SHA-256
            - Send events to the Meta Conversions API with an event ID for deduplication
            - Send only events from users who gave marketing consent
API:        REST
            POST /events/purchase
Storage:    PostgreSQL
Tech stack: Node.js, Meta Conversions API, Fastify
```

---

## Example 350

**Intent:**
when someone signs a contract in docusign, save the signed pdf in the client folder in sharepoint

**Spec:**
```
Type:       Webhook service (signed contract archiving)
Features:   - Receive envelope-completed events from DocuSign Connect
            - Download the signed PDF and certificate of completion
            - Find the client folder in SharePoint by client ID
            - Upload both files and update the CRM record
API:        REST
            POST /webhooks/docusign
Tech stack: C#, Azure Functions, DocuSign eSignature API, Microsoft Graph
```

---

## Example 351

**Intent:**
github issues and jira tickets both used by different teams, keep them in sync both ways

**Spec:**
```
Type:       Webhook service (GitHub-Jira two-way sync)
Data model: IssueLink(id, github_issue_number, jira_key, last_synced_at)
Features:   - Create a Jira ticket when an issue gets the jira label
            - Sync title, description, status and comments both ways
            - Map GitHub labels to Jira fields
            - Prevent echo loops by ignoring changes made by the sync user
API:        REST
            POST /webhooks/github
            POST /webhooks/jira
Storage:    PostgreSQL
Tech stack: Python, FastAPI, PyGithub, jira library
```

---

## Example 352

**Intent:**
typeform survey answers into our postgres database as they come in

**Spec:**
```
Type:       Webhook service (form responses to database)
Data model: Response(id, form_id, submitted_at, answers_json)
            Answer(id, response_id -> Response, question_ref, value)
Features:   - Receive Typeform webhooks and verify the signature
            - Store each response and a row per answer
            - Ignore duplicate deliveries by response token
            - Backfill older responses from the Responses API
API:        REST
            POST /webhooks/typeform
Storage:    PostgreSQL
Tech stack: Python, Flask, psycopg
```

---

## Example 353

**Intent:**
zendesk tickets marked as bug should create jira issue for dev team, and when dev closes it the ticket gets a note

**Spec:**
```
Type:       Webhook service (Zendesk to Jira escalation)
Data model: Escalation(id, zendesk_ticket_id, jira_key, status, created_at)
Features:   - Create a Jira bug when a Zendesk ticket gets the bug tag
            - Copy the description and attachments
            - Add a private note in Zendesk with the Jira link
            - Post a note to the ticket when the Jira issue is resolved
API:        REST
            POST /webhooks/zendesk
            POST /webhooks/jira
Storage:    SQLite
Tech stack: Node.js, Express, Zendesk API, Jira Cloud REST API
```

---

## Example 354

**Intent:**
hubspot form leads into our own postgres too

**Spec:**
```
Type:       Webhook service (HubSpot lead capture)
Data model: Lead(id, hubspot_contact_id, email, name, company, source_form, created_at)
Features:   - Receive form submission webhooks from HubSpot
            - Fetch full contact details from the HubSpot API
            - Upsert the lead into PostgreSQL by contact ID
            - Retry on HubSpot rate limits
API:        REST
            POST /webhooks/hubspot
Storage:    PostgreSQL
Tech stack: Python, FastAPI, hubspot-api-client
```

---

## Example 355

**Intent:**
Our sales close offline after people click our Google ads. Upload those sales back to Google Ads so it learns which clicks are worth it.

**Spec:**
```
Type:       Scheduled script (offline conversion upload)
Data model: Deal(id, gclid, closed_at, value, currency, uploaded_at)
Features:   - Store the click ID (gclid) with each lead from the website form
            - Find deals closed in the CRM since the last run
            - Upload conversions with value and time to Google Ads
            - Mark uploaded deals and log rejected ones
Input:      CRM API token, Google Ads developer token and customer ID
Storage:    PostgreSQL
Tech stack: Python, google-ads library, cron
```

---

## Example 356

**Intent:**
amazon seller orders into our warehouse system every 15 min

**Spec:**
```
Type:       Scheduled script (marketplace order import)
Data model: ImportedOrder(amazon_order_id, status, imported_at, wms_order_id)
Features:   - Fetch new and updated orders from the Selling Partner API
            - Request restricted buyer address data with an RDT token
            - Create orders in the warehouse system
            - Send shipment confirmations with tracking back to Amazon
Storage:    PostgreSQL
Tech stack: Python, python-amazon-sp-api, WMS REST API
```

---

## Example 357

**Intent:**
Wir brauchen einen Export unserer Buchungen im DATEV-Format für den Steuerberater, jeden Monat automatisch.

**Spec:**
```
Type:       Scheduled script (DATEV accounting export)
Features:   - Collect last month's invoices, payments and expenses
            - Map accounts to the SKR03 chart of accounts
            - Write a DATEV EXTF booking CSV with the correct header
            - Attach receipt PDFs in a ZIP
            - Email the export to the tax advisor on the 3rd of each month
Input:      Database URL, account mapping file, advisor email
Tech stack: Python, pandas, smtplib
```

---

## Example 358

**Intent:**
turn our toggl hours into client invoices at the end of the month

**Spec:**
```
Type:       Scheduled script (time tracking invoicing)
Data model: Client(id, name, toggl_client_id, hourly_rate, currency)
            Invoice(id, client_id -> Client, month, hours, total, pdf_key)
Features:   - Fetch billable time entries per client from the Toggl API
            - Round entries to 15 minutes
            - Build invoice lines grouped by project
            - Generate a PDF invoice and save it as a draft
Storage:    SQLite, local PDF folder
Tech stack: Python, Toggl Track API v9, WeasyPrint
```

---

## Example 359

**Intent:**
watch a google drive folder, any new scanned document gets OCR and renamed by its content

**Spec:**
```
Type:       Scheduled script (Drive document processing)
Features:   - Poll the Drive folder for new PDFs and images every 5 minutes
            - Run OCR on each file
            - Detect document type and date from the text
            - Rename files like 2026-10-12_Invoice_SupplierName.pdf
            - Move them to subfolders by type
Input:      Drive folder ID, service account key
Tech stack: Python, Google Drive API, OCRmyPDF
```

---

## Example 360

**Intent:**
when a client books a call on our site, create a zoom meeting and put the link in the confirmation email

**Spec:**
```
Type:       Webhook service (meeting link creation)
Data model: Booking(id, client_email, starts_at, zoom_meeting_id, join_url)
Features:   - Receive the booking-created webhook from the booking form
            - Create a Zoom meeting with the booking time
            - Send a confirmation email with the join link and .ics attachment
            - Delete the Zoom meeting when the booking is cancelled
API:        REST
            POST /webhooks/booking-created
            POST /webhooks/booking-cancelled
Storage:    SQLite
Tech stack: Node.js, Express, Zoom API (server-to-server OAuth), Nodemailer
```

---

## Example 361

**Intent:**
youtube channel stats every day into a google sheet

**Spec:**
```
Type:       Scheduled script (YouTube stats export)
Features:   - Fetch subscribers, views and video count daily
            - Fetch views and likes for the 20 newest videos
            - Append a dated row to a Google Sheet
            - Run on a free scheduled cloud function
Input:      Channel ID, API key, sheet ID
Tech stack: Google Apps Script, YouTube Data API v3
```

---

## Example 362

**Intent:**
let me know if there's an earthquake over magnitude 4 within 200km of my parents' town

**Spec:**
```
Type:       Scheduled script (earthquake alert)
Features:   - Poll the USGS earthquake GeoJSON feed every 5 minutes
            - Calculate distance from the town with the haversine formula
            - Send a push notification for quakes over magnitude 4 within 200 km
            - Remember sent events to avoid duplicates
Storage:    JSON file of seen event IDs
Tech stack: Python, requests, ntfy
```

---

## Example 363

**Intent:**
one tracking page for parcels from DHL, UPS, FedEx and local post, customers dont care which courier

**Spec:**
```
Type:       REST API service (parcel tracking aggregator)
Data model: Shipment(id, order_id, carrier, tracking_number, status, last_event_at)
            TrackingEvent(id, shipment_id -> Shipment, status, location, description, occurred_at)
Features:   - Detect the carrier from the tracking number format
            - Poll each carrier API and normalize events to common statuses
            - Show a branded tracking page per order
            - Email the customer on out-for-delivery and delivered
API:        REST
            POST /shipments
            GET  /track/{order_id}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Sidekiq, carrier tracking APIs
```

---

## Example 364

**Intent:**
VIN decoder api for our used car marketplace, give make model year engine

**Spec:**
```
Type:       REST API service (VIN decoding)
Data model: VinCache(vin, make, model, model_year, engine, body_type, decoded_at)
Features:   - Validate the 17-character VIN and its check digit
            - Decode make, model, year and engine from the NHTSA vPIC database
            - Cache decoded VINs
            - Return partial results for older vehicles
API:        REST
            GET  /vin/{vin}
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, NHTSA vPIC API
```

---

## Example 365

**Intent:**
ISBN in, book info out (title, author, cover). for my used bookstore inventory

**Spec:**
```
Type:       REST API service (ISBN metadata)
Data model: Book(isbn13, title, authors, publisher, year, cover_url, fetched_at)
Features:   - Convert ISBN-10 to ISBN-13
            - Look up metadata from Open Library, then Google Books as fallback
            - Download and store the cover image
            - Cache results permanently
API:        REST
            GET  /books/{isbn}
Storage:    SQLite, local covers folder
Tech stack: Python, Flask, Open Library API, Google Books API
```

---

## Example 366

**Intent:**
We translate product descriptions with machine translation but brand names get translated wrong. Wrap the translation API with our glossary.

**Spec:**
```
Type:       REST API service (glossary-aware translation)
Data model: GlossaryTerm(id, source_lang, target_lang, source_term, target_term, do_not_translate)
            TranslationCache(text_hash, target_lang, translated_text)
Features:   - Protect do-not-translate terms with placeholders before translation
            - Apply glossary replacements after translation
            - Cache translations of identical texts
            - Let editors manage glossary terms
API:        REST
            POST /translate
            GET  /glossary
            POST /glossary
Storage:    PostgreSQL
Tech stack: Python, FastAPI, DeepL API
```

---

## Example 367

**Intent:**
grammar and spell check inside our internal tools but data cant leave our servers

**Spec:**
```
Type:       Infrastructure setup (self-hosted grammar checking)
Features:   - Run a grammar and spelling server inside the company network
            - Support English, German and French
            - Add company terms to a custom dictionary
            - Call it from internal apps through an HTTP API
Tech stack: LanguageTool server, Docker, n-gram data
```

---

## Example 368

**Intent:**
users write comments in markdown, render them to html safely without XSS

**Spec:**
```
Type:       REST API service (safe Markdown rendering)
Features:   - Render CommonMark with tables and code blocks
            - Sanitize the HTML with an allow-list of tags and attributes
            - Add rel="nofollow ugc" to external links
            - Highlight code blocks
            - Cache rendered output by content hash
API:        REST
            POST /render
Tech stack: Node.js, markdown-it, DOMPurify with jsdom, Shiki
```

---

## Example 369

**Intent:**
make url slugs from titles in any language, also chinese and russian

**Spec:**
```
Type:       REST API service (slug generation)
Features:   - Transliterate Cyrillic, Greek and other scripts to Latin
            - Convert Chinese to pinyin
            - Lowercase, remove punctuation and join with hyphens
            - Add a number when the slug already exists in a namespace
API:        REST
            POST /slugs
Storage:    Redis (taken slugs per namespace)
Tech stack: Python, python-slugify, pypinyin, FastAPI
```

---

## Example 370

**Intent:**
api that takes "next tuesday at 3pm" and gives me a real date

**Spec:**
```
Type:       REST API service (natural language date parsing)
Features:   - Parse phrases like "in 2 weeks" or "next Tuesday 3pm"
            - Use the caller's timezone and reference time
            - Support English, Spanish and German
            - Return ISO 8601 datetime and the matched text
API:        REST
            POST /parse
Tech stack: Python, dateparser, FastAPI
```

---

## Example 371

**Intent:**
explain cron expressions in plain english and show next 5 run times

**Spec:**
```
Type:       REST API service (cron expression explainer)
Features:   - Validate standard and extended cron syntax
            - Describe the schedule in plain English
            - Return the next N run times in a timezone
            - Point out common mistakes like day-of-month and day-of-week both set
API:        REST
            GET  /cron/explain?expr={expression}&tz={zone}&count={n}
Tech stack: Node.js, cron-parser, cronstrue
```

---

## Example 372

**Intent:**
Every time our base Docker image gets a security fix, our services should rebuild automatically.

**Spec:**
```
Type:       Infrastructure setup (automated dependency updates)
Features:   - Run a dependency update bot across all repositories
            - Open pull requests when base images or packages get new versions
            - Group minor updates weekly and open security fixes immediately
            - Automerge patch updates that pass tests
Tech stack: Renovate (self-hosted), GitLab, Docker
```

---

## Example 373

**Intent:**
nobody knows if we can actually recover if the main database server dies. practice it

**Spec:**
```
Type:       Infrastructure setup (disaster recovery drills)
Features:   - Write a runbook with recovery steps for each critical system
            - Schedule a quarterly drill that kills the primary database in staging
            - Measure actual recovery time and data loss against targets
            - Record findings and fix tasks after each drill
Tech stack: Ansible, Patroni, Markdown runbooks in Git
```

---

## Example 374

**Intent:**
randomly kill pods in staging to see if our app survives

**Spec:**
```
Type:       Infrastructure setup (chaos testing)
Features:   - Kill random pods of selected deployments on a schedule
            - Inject network latency and packet loss between services
            - Run experiments only in staging namespaces
            - Report which experiments caused errors
Tech stack: Chaos Mesh, Kubernetes, Grafana
```

---

## Example 375

**Intent:**
check our linux servers against the CIS security benchmark and fix what fails

**Spec:**
```
Type:       Infrastructure setup (server hardening compliance)
Features:   - Scan servers against the CIS Ubuntu benchmark
            - Apply fixes for failed controls with automation
            - Allow documented exceptions per server
            - Produce a compliance report per scan
Tech stack: OpenSCAP, Ansible Lockdown roles, Ubuntu 24.04
```

---

## Example 376

**Intent:**
which of our s3 buckets are public? need a weekly check

**Spec:**
```
Type:       Scheduled script (public bucket audit)
Features:   - List all buckets in every account
            - Check block-public-access settings, bucket policies and ACLs
            - Flag buckets readable or writable by anyone
            - Compare with an allow-list of intentionally public buckets
            - Post findings to the security channel
Input:      List of AWS accounts and allow-list file
Tech stack: Python, boto3, AWS Organizations
```

---

## Example 377

**Intent:**
find IAM users and roles that have permissions they never use

**Spec:**
```
Type:       Scheduled script (unused permissions report)
Features:   - Read last-accessed data for each IAM role and user
            - List services never used in 90 days
            - Suggest a reduced policy with only used actions
            - Flag users without MFA and with old access keys
Input:      AWS account credentials
Tech stack: Python, boto3, IAM Access Analyzer
```

---

## Example 378

**Intent:**
firewall rules on our 20 servers are all different. manage them from one place

**Spec:**
```
Type:       Infrastructure setup (firewall as code)
Features:   - Define allowed ports per server role in YAML
            - Generate nftables rules from the definitions
            - Apply rules with automation and keep SSH reachable
            - Review rule changes in pull requests
Tech stack: Ansible, nftables, Git
```

---

## Example 379

**Intent:**
hi we are 3 person startup in vietnam, we need simple way to send our app logs of payments to a place auditor can see but not change

**Spec:**
```
Type:       REST API service (write-once payment logs)
Auth:       App service token for writing; read-only auditor accounts
Data model: PaymentLog(id, payment_id, event, amount, currency, actor, created_at)
Features:   - Accept payment log events from the app
            - Store them in write-once object storage with a retention lock
            - Give auditors a read-only search page
            - Export logs by date range as CSV
API:        REST
            POST /logs
            GET  /logs?from={d}&to={d}
Storage:    S3 with Object Lock (compliance mode)
Tech stack: Node.js, Express, AWS S3
```

---

## Example 380

**Intent:**
i am running small isp in village, need to see bandwidth of each customer and cut them when not paid

**Spec:**
```
Type:       Web application (ISP customer management)
Auth:       Operator login
Data model: Customer(id, name, phone, ip_address, plan_mbps, paid_until, active)
            UsageSample(customer_id -> Customer, rx_bytes, tx_bytes, sampled_at)
Features:   - Read per-customer traffic from the router every 5 minutes
            - Set bandwidth limits per plan with queues
            - Disable customers automatically when payment is overdue
            - Show monthly usage per customer
API:        REST
            GET  /customers
            POST /customers/{id}/payments
Storage:    PostgreSQL
Tech stack: Python, Django, MikroTik RouterOS API
```

---

## Example 381

**Intent:**
we are travel agency in Morocco, our website need show prices in dirham, euro and dollar with today rate

**Spec:**
```
Type:       REST API service (multi-currency prices)
Data model: Rate(currency, rate_to_mad, fetched_at)
            Tour(id, name, price_mad)
Features:   - Fetch exchange rates every morning
            - Return tour prices in MAD, EUR and USD
            - Round prices to whole numbers
            - Keep the last rates if the rate source is down
API:        REST
            GET  /tours?currency={code}
            GET  /rates
Storage:    MySQL
Tech stack: PHP, Laravel, exchangerate.host API
```

---

## Example 382

**Intent:**
my company in Kenya use M-Pesa, need to know automatically when customer pay to our paybill and mark invoice paid

**Spec:**
```
Type:       Webhook service (mobile money payment confirmation)
Data model: Invoice(id, account_number, amount_kes, status)
            MpesaPayment(id, trans_id, msisdn_hash, amount_kes, bill_ref, received_at)
Features:   - Register validation and confirmation URLs with the M-Pesa C2B API
            - Match payments to invoices by account number in the bill reference
            - Mark invoices paid or partly paid
            - Send the customer an SMS receipt
API:        REST
            POST /mpesa/validation
            POST /mpesa/confirmation
Storage:    PostgreSQL
Tech stack: Python, Django, Safaricom Daraja API, Africa's Talking SMS
```

---

## Example 383

**Intent:**
please make for me system where many shop branches upload the sales file every night and head office see total

**Spec:**
```
Type:       Web application (branch sales consolidation)
Auth:       Branch login and head office login
Data model: Branch(id, name, city)
            SalesUpload(id, branch_id -> Branch, business_date, file_key, status)
            DailySales(branch_id -> Branch, business_date, product_code, quantity, revenue)
Features:   - Let branches upload their daily sales CSV
            - Validate and load rows into the central database
            - Show totals per branch, product and day to head office
            - Show which branches did not upload yet
API:        REST
            POST /uploads
            GET  /reports/daily?date={d}
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Thymeleaf
```

---

## Example 384

**Intent:**
our hospital lab machines output results in HL7, we need them in the new patient system

**Spec:**
```
Type:       Data pipeline (HL7 interface engine)
Data model: LabMessage(id, control_id, patient_mrn, message_type, status, received_at)
Features:   - Receive HL7 v2 ORU messages over MLLP
            - Parse results and map codes to LOINC
            - Convert to FHIR Observation resources
            - Post them to the patient system's FHIR API
            - Send ACKs and queue failed messages for retry
Storage:    PostgreSQL (message log)
Tech stack: Mirth Connect (NextGen Connect), HAPI FHIR
```

---

## Example 385

**Intent:**
tiny file sharing link like wetransfer for our design team, files gone after 7 days

**Spec:**
```
Type:       Web application (temporary file transfer)
Auth:       Team login for sending; recipients use the link
Data model: Transfer(id, sender_id, message, password_hash, expires_at, download_count)
            TransferFile(id, transfer_id -> Transfer, filename, size_bytes, storage_key)
Features:   - Upload several files up to 20 GB
            - Create a share link with optional password
            - Email the sender when files are downloaded
            - Delete files after 7 days
API:        REST
            POST /transfers
            GET  /t/{id}
            GET  /t/{id}/files/{file_id}
Storage:    PostgreSQL, S3 with lifecycle rule
Tech stack: TypeScript, SvelteKit, S3 multipart upload
```

---

## Example 386

**Intent:**
send newsletters from our own server instead of paying mailchimp a fortune

**Spec:**
```
Type:       Infrastructure setup (self-hosted newsletter)
Auth:       Admin login
Features:   - Manage lists and subscribers with double opt-in
            - Create campaigns with templates
            - Send through an SMTP relay with rate limits
            - Track opens, clicks and bounces
            - Import existing subscribers from CSV
Storage:    PostgreSQL
Tech stack: listmonk, Amazon SES, Docker
```

---

## Example 387

**Intent:**
backend for the tv screen in our gym that shows class schedule and who's checked in

**Spec:**
```
Type:       REST API service (gym display feed)
Data model: GymClass(id, name, instructor, starts_at, capacity)
            CheckIn(id, class_id -> GymClass, member_first_name, checked_in_at)
Features:   - Read today's classes from the booking system
            - Receive check-in events from the door scanner
            - Return a display feed with next classes and check-in counts
            - Push updates to the screen with Server-Sent Events
API:        REST
            GET  /display/feed
            GET  /display/stream
            POST /checkins
Storage:    Redis
Tech stack: Node.js, Fastify, Redis
```

---

## Example 388

**Intent:**
I'm building a game and want global leaderboards that players can't easily cheat.

**Spec:**
```
Type:       REST API service (game leaderboards)
Auth:       Player session tokens from the game server
Data model: Player(id, display_name, platform_id)
            ScoreSubmission(id, player_id -> Player, board, score, replay_hash, submitted_at, verified)
Features:   - Accept scores only from authenticated game sessions
            - Validate scores against max plausible values and session length
            - Keep daily, weekly and all-time boards
            - Return top 100 and the player's own rank
API:        REST
            POST /scores
            GET  /boards/{board}?period={day|week|all}
            GET  /boards/{board}/me
Storage:    Redis sorted sets, PostgreSQL
Tech stack: Go, Redis, PostgreSQL
```

---

## Example 389

**Intent:**
dedicated server for our multiplayer indie game, start new match servers when players queue

**Spec:**
```
Type:       Infrastructure setup (game server fleet)
Features:   - Run game server containers on a Kubernetes cluster
            - Allocate a ready server when matchmaking finds a match
            - Keep a buffer of warm servers
            - Shut down servers after each match
            - Scale nodes with player demand
Tech stack: Agones, Kubernetes, Open Match
```

---

## Example 390

**Intent:**
Our photo contest site: people vote once per entry. Stop people voting many times with new accounts.

**Spec:**
```
Type:       REST API service (vote integrity)
Auth:       Email verification plus phone verification for voting
Data model: Voter(id, email, phone_hash, verified_at)
            Vote(id, voter_id -> Voter, entry_id, ip_hash, device_hash, created_at)
Features:   - Allow one vote per verified voter per entry
            - Require a unique phone number per voter
            - Flag bursts of votes from the same IP or device
            - Hide suspicious votes from totals until reviewed
API:        REST
            POST /entries/{id}/votes
            GET  /entries/{id}/votes/count
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio Verify
```

---

## Example 391

**Intent:**
make my raspberry pi a print server so phones can print to my old usb printer

**Spec:**
```
Type:       Infrastructure setup (network print server)
Features:   - Install CUPS on a Raspberry Pi
            - Share the USB printer on the home network
            - Advertise it with AirPrint and Mopria through Avahi
            - Restrict the admin page to the local network
Tech stack: Raspberry Pi OS, CUPS, Avahi
```

---

## Example 392

**Intent:**
home assistant automations: lights off when everyone leaves, heater on when someone is coming home

**Spec:**
```
Type:       IoT system (home presence automation)
Features:   - Track family presence from phone apps and Wi-Fi
            - Turn off lights and plugs when the last person leaves
            - Turn on heating when someone is within 10 km of home
            - Send a notification if a window is open when leaving
Tech stack: Home Assistant, Home Assistant Companion app, Zigbee2MQTT
```

---

## Example 393

**Intent:**
greenhouse controller, open windows when hot, water when soil dry, all logged

**Spec:**
```
Type:       IoT system (greenhouse automation)
Data model: SensorReading(air_temp_c, humidity, soil_moisture, light_lux, recorded_at)
            ActuatorEvent(actuator, action, reason, occurred_at)
Features:   - Read temperature, humidity, soil moisture and light every minute
            - Open window motors above 28°C and close below 22°C
            - Run the irrigation valve when soil is dry, with a daily max
            - Log readings and actions
            - Allow manual override from a phone
Storage:    SQLite on the controller
Tech stack: Raspberry Pi, Python, gpiozero, Node-RED dashboard
```

---

## Example 394

**Intent:**
cat feeder that feeds on schedule and i can trigger from my phone, logs every meal

**Spec:**
```
Type:       IoT system (smart pet feeder)
Data model: Feeding(id, portion_grams, trigger, fed_at)
            Schedule(id, time_of_day, portion_grams, enabled)
Features:   - Turn a servo-driven dispenser at scheduled times
            - Trigger a meal from the phone
            - Weigh the bowl to confirm food was dispensed
            - Warn when the food container is low
Storage:    SQLite
Tech stack: ESP32, MicroPython, MQTT, Home Assistant
```

---

## Example 395

**Intent:**
hotel minibar sensors report what was taken so reception can charge on checkout

**Spec:**
```
Type:       IoT system (smart minibar)
Data model: Room(id, number)
            MinibarItem(id, name, price)
            Consumption(id, room_id -> Room, item_id -> MinibarItem, detected_at, charged)
Features:   - Detect removed items with weight sensors per slot
            - Ignore items returned within 60 seconds
            - Post charges to the guest folio in the hotel system
            - Show restock lists for housekeeping
API:        REST
            POST /minibar/events
            GET  /restock
Storage:    PostgreSQL
Tech stack: ESP32, MQTT, Python, FastAPI, Opera PMS interface
```

---

## Example 396

**Intent:**
log of who opens the server room door with the badge reader

**Spec:**
```
Type:       IoT system (door access logging)
Data model: Badge(id, uid, employee_name, active)
            DoorEvent(id, badge_uid, granted, occurred_at)
Features:   - Read RFID badges at the door
            - Unlock only for active badges on the allow-list
            - Log every attempt, granted or denied
            - Email security after 3 denied attempts in 5 minutes
Storage:    SQLite
Tech stack: Raspberry Pi, RC522 RFID reader, Python, relay module
```

---

## Example 397

**Intent:**
Our municipality wants to publish its yearly budget and spending as open data with an API journalists can query.

**Spec:**
```
Type:       REST API service (public spending data)
Data model: Department(id, name)
            BudgetLine(id, department_id -> Department, year, category, planned_amount)
            Payment(id, department_id -> Department, supplier, amount, paid_on, category)
Features:   - Import yearly budget and payment files
            - Filter spending by department, supplier, category and date
            - Compare planned budget with actual spending
            - Offer bulk CSV and JSON downloads
API:        REST
            GET  /budget?year={y}
            GET  /payments?supplier={name}
            GET  /downloads
Storage:    PostgreSQL
Tech stack: Python, Datasette, sqlite-utils
```

---

## Example 398

**Intent:**
gtfs realtime bus positions are protobuf, make a simple json api for our hobby app

**Spec:**
```
Type:       REST API service (GTFS-Realtime JSON proxy)
Features:   - Fetch the GTFS-Realtime vehicle positions feed every 15 seconds
            - Decode protobuf messages
            - Join with static GTFS for route names
            - Return vehicles as JSON or GeoJSON
API:        REST
            GET  /vehicles
            GET  /routes/{id}/vehicles
Storage:    In-memory cache
Tech stack: Python, gtfs-realtime-bindings, FastAPI
```

---

## Example 399

**Intent:**
Researchers ask us for our survey data constantly. Make an API with the anonymized data so they can get it themselves.

**Spec:**
```
Type:       REST API service (research data access)
Auth:       Researcher accounts with approved data-use agreement
Data model: Researcher(id, name, institution, approved_at)
            Dataset(id, title, version, description)
            DownloadLog(id, researcher_id -> Researcher, dataset_id -> Dataset, downloaded_at)
Features:   - Publish anonymized survey datasets with versions
            - Check that small groups are suppressed for privacy
            - Let approved researchers query and download data
            - Log all downloads
API:        REST
            GET  /datasets
            GET  /datasets/{id}/data
Storage:    PostgreSQL
Tech stack: R, plumber API, PostgreSQL
```

---

## Example 400

**Intent:**
plz help we need api where our partners can check stock of our products live, but only products they are allowed to sell

**Spec:**
```
Type:       REST API service (partner stock availability)
Auth:       API key per partner
Data model: Partner(id, name, api_key_hash)
            PartnerProduct(partner_id -> Partner, product_sku)
            Stock(product_sku, warehouse, quantity, updated_at)
Features:   - Return stock only for products assigned to the partner
            - Sum stock across warehouses with a safety buffer
            - Support bulk lookups of up to 500 SKUs
            - Rate limit each partner
API:        REST
            GET  /stock/{sku}
            POST /stock/lookup
Storage:    PostgreSQL, Redis (cache)
Tech stack: C#, ASP.NET Core, StackExchange.Redis
```

---

## Example 401

**Intent:**
heartbeat check for our cron jobs is not what i want. i want to track how long each batch job takes and see trends

**Spec:**
```
Type:       Web application (batch job duration tracking)
Auth:       Team login
Data model: Job(id, name, owner_team)
            JobRun(id, job_id -> Job, started_at, finished_at, duration_s, rows_processed, status)
Features:   - Receive start and finish calls from batch jobs
            - Chart duration and rows processed per run
            - Flag runs more than 50% slower than the 30-day median
            - Compare jobs by team
API:        REST
            POST /jobs/{name}/start
            POST /runs/{id}/finish
            GET  /jobs/{name}/runs
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Plotly Dash
```

---

## Example 402

**Intent:**
expose our internal data warehouse tables as a read-only API for partners, with only their rows

**Spec:**
```
Type:       REST API service (partner data API)
Auth:       OAuth 2.0 client credentials per partner
Data model: PartnerScope(partner_id, table_name, filter_column, filter_value)
Features:   - Serve selected warehouse tables as paginated JSON
            - Filter every query to the partner's rows automatically
            - Allow field selection and date filters
            - Log query volume per partner
API:        REST
            GET  /data/{table}?fields={list}&since={date}
Storage:    Snowflake
Tech stack: Python, FastAPI, snowflake-connector-python
```

---

## Example 403

**Intent:**
convert a 10GB json lines file to csv without running out of memory

**Spec:**
```
Type:       Command-line tool (JSON Lines to CSV)
Features:   - Stream the input line by line
            - Flatten nested objects into dotted column names
            - Detect columns from the first N lines or a given list
            - Write gzip-compressed output optionally
            - Show progress and skipped bad lines
Input:      Path to a .jsonl file, output path, optional column list
Tech stack: Rust, serde_json, csv crate, clap
```

---

## Example 404

**Intent:**
api that shows the differences between two versions of a text, like track changes

**Spec:**
```
Type:       REST API service (text diff)
Features:   - Compare two texts by word or by line
            - Return insertions and deletions with positions
            - Render a side-by-side HTML view
            - Ignore whitespace changes optionally
API:        REST
            POST /diff
            POST /diff/html
Tech stack: Python, diff-match-patch, FastAPI
```

---

## Example 405

**Intent:**
our support inbox gets mails in 20 languages, detect the language so we route to the right agent

**Spec:**
```
Type:       REST API service (language detection)
Features:   - Detect the language of a text with a confidence score
            - Return the top 3 candidates for short texts
            - Process batches of texts
            - Map languages to support queues from a config file
API:        REST
            POST /detect
            POST /detect/batch
Tech stack: Python, fastText lid.176 model, FastAPI
```

---

## Example 406

**Intent:**
filter bad words from usernames and chat in our kids game

**Spec:**
```
Type:       REST API service (profanity filter)
Data model: BlockedTerm(id, term, language, severity)
            AllowedTerm(id, term)
Features:   - Detect bad words including leetspeak and spacing tricks
            - Mask words in chat messages with asterisks
            - Reject usernames containing blocked terms
            - Let moderators edit the block and allow lists
API:        REST
            POST /check/username
            POST /filter/message
            POST /terms
Storage:    PostgreSQL
Tech stack: Go, Aho-Corasick matcher, Gin
```

---

## Example 407

**Intent:**
get the favicon of any website for our bookmarks app

**Spec:**
```
Type:       REST API service (favicon fetcher)
Features:   - Read icon links from the page HTML
            - Fall back to /favicon.ico and manifest icons
            - Pick the closest size to the request
            - Return a default icon when none is found
            - Cache icons for 7 days
API:        REST
            GET  /icon?domain={host}&size={px}
Storage:    S3 (icon cache)
Tech stack: Node.js, Fastify, cheerio, sharp
```

---

## Example 408

**Intent:**
Our web fonts are 400KB each. Make a service that strips them down to only the characters a page needs.

**Spec:**
```
Type:       REST API service (font subsetting)
Features:   - Accept a font file and a set of characters or a text sample
            - Create a subset with only needed glyphs
            - Output WOFF2
            - Cache subsets by font and character set hash
API:        REST
            POST /subset
Storage:    S3 (subset cache)
Tech stack: Python, fontTools, Brotli, FastAPI
```

---

## Example 409

**Intent:**
at build time make every image in my static site in 4 sizes and webp, update the html

**Spec:**
```
Type:       Command-line tool (responsive image build step)
Features:   - Find images referenced in HTML files
            - Create 480, 960, 1440 and 1920 pixel versions in WebP and JPEG
            - Rewrite img tags with srcset and sizes attributes
            - Skip images that are already processed
            - Add width and height to prevent layout shift
Input:      Build output folder
Tech stack: Node.js, sharp, cheerio
```

---

## Example 410

**Intent:**
markdown files to nice pdf from the command line, with a table of contents

**Spec:**
```
Type:       Command-line tool (Markdown to PDF)
Features:   - Convert one or many Markdown files into a single PDF
            - Generate a table of contents from headings
            - Apply a CSS theme for fonts and margins
            - Highlight code blocks
            - Add page numbers in the footer
Input:      Markdown files, optional theme CSS
Tech stack: Python, markdown-it-py, WeasyPrint, Typer
```

---

## Example 411

**Intent:**
Suppliers send us product feeds in their own XML formats. Convert each to our one JSON format.

**Spec:**
```
Type:       Data pipeline (supplier feed transformation)
Data model: Supplier(id, name, feed_url, mapping_file)
            FeedRun(id, supplier_id -> Supplier, product_count, error_count, ran_at)
Features:   - Download each supplier's XML feed daily
            - Apply an XSLT or mapping config per supplier
            - Validate output against our JSON Schema
            - Load valid products into the catalog database
Storage:    PostgreSQL
Tech stack: Python, lxml (XSLT), jsonschema, Prefect
```

---

## Example 412

**Intent:**
need a service that makes excel files from our data with formatting, other services call it

**Spec:**
```
Type:       REST API service (Excel generation)
Auth:       Internal service token
Features:   - Accept a JSON description of sheets, columns and rows
            - Apply number formats, column widths and header styles
            - Add formulas and frozen header rows
            - Return the .xlsx file or a download link for big files
API:        REST
            POST /xlsx
Storage:    S3 (large files)
Tech stack: Java, Apache POI (SXSSF streaming), Spring Boot
```

---

## Example 413

**Intent:**
nutrition info api for our meal planner, calories protein carbs per 100g

**Spec:**
```
Type:       REST API service (nutrition lookup)
Data model: Food(id, name, calories_kcal, protein_g, carbs_g, fat_g, fiber_g, source)
Features:   - Import foods from the USDA FoodData Central dataset
            - Search foods by name with fuzzy matching
            - Calculate nutrition for a recipe from ingredient weights
            - Allow custom foods per user
API:        REST
            GET  /foods?q={name}
            POST /recipes/nutrition
Storage:    PostgreSQL
Tech stack: Python, FastAPI, pg_trgm
```

---

## Example 414

**Intent:**
sunrise and sunset times api for any place, photographers app

**Spec:**
```
Type:       REST API service (sun times)
Features:   - Calculate sunrise, sunset and solar noon for a location and date
            - Include golden hour and blue hour times
            - Return times in the location's local timezone
            - Return a whole month in one call
API:        REST
            GET  /sun?lat={lat}&lon={lon}&date={d}
            GET  /sun/month?lat={lat}&lon={lon}&month={m}
Tech stack: Python, astral, timezonefinder, FastAPI
```

---

## Example 415

**Intent:**
we sell on ebay too, keep the ebay listings price and stock same as our shop

**Spec:**
```
Type:       Scheduled script (eBay listing sync)
Data model: ListingMap(sku, ebay_item_id, last_price, last_quantity, synced_at)
Features:   - Read price and stock from the shop every 10 minutes
            - Update eBay listings in bulk through the Inventory API
            - Only send listings that changed
            - Import eBay orders back into the shop
Storage:    SQLite
Tech stack: Python, eBay Inventory API, WooCommerce REST API
```

---

## Example 416

**Intent:**
woocommerce orders into odoo for invoicing and stock, we do it by hand now

**Spec:**
```
Type:       Webhook service (WooCommerce to Odoo)
Data model: OrderSync(woo_order_id, odoo_sale_order_id, status, synced_at, error)
Features:   - Receive order-created webhooks from WooCommerce
            - Find or create the customer in Odoo
            - Create a confirmed sale order with matching products by SKU
            - Push stock levels from Odoo back to WooCommerce hourly
API:        REST
            POST /webhooks/woocommerce/order
Storage:    PostgreSQL
Tech stack: Python, Flask, Odoo XML-RPC API, WooCommerce REST API
```

---

## Example 417

**Intent:**
running club: pull everyone's runs from Strava and make a monthly distance leaderboard

**Spec:**
```
Type:       Web application (club leaderboard)
Auth:       Strava OAuth login
Data model: Member(id, strava_athlete_id, name, refresh_token_encrypted)
            Activity(id, member_id -> Member, distance_m, moving_time_s, started_at)
Features:   - Let members connect their Strava account
            - Receive new activities through Strava webhook events
            - Show a monthly leaderboard of total distance
            - Remove data when a member disconnects
API:        REST
            GET  /auth/strava/callback
            POST /webhooks/strava
            GET  /leaderboard?month={m}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Strava API v3
```

---

## Example 418

**Intent:**
save invoice attachments from my gmail into a drive folder automatically

**Spec:**
```
Type:       Scheduled script (email attachment archiving)
Features:   - Search Gmail for messages with PDF attachments and invoice keywords
            - Save attachments to a Drive folder by year and month
            - Label processed emails so they are not saved twice
            - Run every hour
Tech stack: Google Apps Script, Gmail service, Drive service
```

---

## Example 419

**Intent:**
host our own helm charts so other teams can install our services

**Spec:**
```
Type:       Infrastructure setup (Helm chart repository)
Features:   - Package charts on each release tag
            - Push charts as OCI artifacts to the registry
            - Sign charts and verify on install
            - Publish a chart index with versions and docs
Tech stack: Helm, Harbor OCI registry, cosign, GitLab CI
```

---

## Example 420

**Intent:**
our docker images are 2GB, make them small

**Spec:**
```
Type:       Infrastructure setup (container image slimming)
Features:   - Use multi-stage builds to drop build tools
            - Switch to distroless or slim base images
            - Order layers to maximize cache reuse
            - Add a .dockerignore for unneeded files
            - Report image size per build and fail above a limit
Tech stack: Docker BuildKit, distroless images, dive
```

---

## Example 421

**Intent:**
stop storing database passwords for our apps, let them log in with their cloud identity

**Spec:**
```
Type:       Infrastructure setup (IAM database authentication)
Features:   - Enable IAM authentication on the managed database
            - Map each app's service role to a database user
            - Generate short-lived auth tokens in the app at connect time
            - Remove static passwords from config
Storage:    Amazon RDS PostgreSQL
Tech stack: AWS IAM, RDS IAM auth, Terraform
```

---

## Example 422

**Intent:**
We have 12 servers in a rented rack and want to move to the cloud step by step without a big bang.

**Spec:**
```
Type:       Infrastructure setup (phased cloud migration)
Features:   - Inventory servers and their dependencies
            - Set up a site-to-site VPN between the rack and the cloud VPC
            - Move stateless services first behind a shared load balancer
            - Replicate databases to the cloud and cut over one at a time
            - Decommission rack servers after each successful move
Tech stack: AWS, Terraform, AWS Database Migration Service, WireGuard
```

---

## Example 423

**Intent:**
who has ssh access to which servers? find old keys of people who left

**Spec:**
```
Type:       Command-line tool (SSH key audit)
Features:   - Collect authorized_keys from all servers over SSH
            - Match key fingerprints to a list of current employees
            - Report unknown keys and keys of former employees
            - Optionally remove flagged keys
Input:      Server inventory file, employee key list
Tech stack: Python, Fabric, paramiko
```

---

## Example 424

**Intent:**
scan our public IPs every week for open ports that shouldn't be open

**Spec:**
```
Type:       Scheduled script (external port audit)
Features:   - List all public IPs from cloud accounts
            - Scan them for open TCP ports
            - Compare with an approved port list per host
            - Report new open ports since the last scan
Input:      Cloud credentials, approved ports YAML
Tech stack: Python, masscan, boto3
```

---

## Example 425

**Intent:**
Copy our search cluster's indexes to a second data center so search still works if one goes down.

**Spec:**
```
Type:       Infrastructure setup (search cluster replication)
Features:   - Set up a follower cluster in the second data center
            - Replicate selected indexes with cross-cluster replication
            - Auto-follow new indexes matching a pattern
            - Switch search traffic to the follower during an outage
Storage:    Elasticsearch
Tech stack: Elasticsearch cross-cluster replication, HAProxy
```

---

## Example 426

**Intent:**
upgrade postgres 12 to 16, we are scared, big database

**Spec:**
```
Type:       Infrastructure setup (PostgreSQL major upgrade)
Features:   - Rehearse the upgrade on a restored copy
            - Replicate to a new PostgreSQL 16 server with logical replication
            - Check extensions and query plans on the new version
            - Switch the app to the new server in a short write freeze
            - Keep the old server for quick rollback
Storage:    PostgreSQL 12 (old), PostgreSQL 16 (new)
Tech stack: PostgreSQL logical replication, pg_upgrade (rehearsal), pgbench
```

---

## Example 427

**Intent:**
mirror our kafka topics to another datacenter

**Spec:**
```
Type:       Infrastructure setup (Kafka cross-cluster mirroring)
Features:   - Replicate selected topics to the second cluster
            - Sync consumer group offsets for failover
            - Prefix mirrored topics with the source cluster name
            - Monitor replication lag
Tech stack: Kafka MirrorMaker 2, Kafka Connect, Prometheus JMX exporter
```

---

## Example 428

**Intent:**
a third-party api only allows 10 calls a second and our workers keep getting blocked

**Spec:**
```
Type:       REST API service (outbound rate limiter)
Features:   - Route all calls to the third-party API through one shared limiter
            - Enforce 10 requests per second across all workers
            - Queue requests briefly instead of failing them
            - Retry 429 responses after the Retry-After time
API:        REST
            ANY  /outbound/{path}
Storage:    Redis (shared token bucket)
Tech stack: Python, aiohttp, Redis Lua script
```

---

## Example 429

**Intent:**
one webhook url from our payment provider but we need the events in dev, staging and prod

**Spec:**
```
Type:       Webhook service (webhook fan-out relay)
Data model: Destination(id, name, url, active)
            RelayedEvent(id, provider_event_id, destination_id -> Destination, status, attempts)
Features:   - Receive webhooks at one public URL and verify the signature
            - Forward each event to every active destination
            - Retry failed forwards with backoff
            - Show recent events and replay one to a destination
API:        REST
            POST /incoming
            GET  /events
            POST /events/{id}/replay
Storage:    PostgreSQL
Tech stack: Go, net/http, PostgreSQL
```

---

## Example 430

**Intent:**
applicants email their CV to jobs@ and it should create a candidate in our hiring system

**Spec:**
```
Type:       Webhook service (CV email intake)
Data model: Candidate(id, name, email, phone, cv_key, source, created_at)
Features:   - Receive inbound emails with attachments
            - Extract name, email and phone from the CV PDF
            - Create the candidate in the applicant tracking system
            - Detect the job from the email subject
            - Reply to the applicant with a confirmation
API:        REST
            POST /inbound/jobs
Storage:    S3 (CV files)
Tech stack: Python, AWS SES inbound, AWS Lambda, pdfminer.six
```

---

## Example 431

**Intent:**
When people reply to our notification emails, their reply should be added as a comment on the task.

**Spec:**
```
Type:       Webhook service (email reply to comment)
Data model: ReplyAddress(token, task_id, user_id, expires_at)
            Comment(id, task_id, user_id, body, source, created_at)
Features:   - Use a unique reply-to address per notification
            - Receive inbound replies and look up the token
            - Strip quoted text and signatures
            - Add the reply as a comment by the right user
            - Reject replies from senders that don't match the user
API:        REST
            POST /inbound/replies
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix, Postmark inbound
```

---

## Example 432

**Intent:**
tenants should text a number to report broken stuff in their apartment and it creates a maintenance ticket

**Spec:**
```
Type:       Webhook service (SMS maintenance requests)
Data model: Tenant(id, name, phone, unit_id)
            MaintenanceTicket(id, tenant_id -> Tenant, description, photo_urls, status, created_at)
Features:   - Match incoming SMS to a tenant by phone number
            - Create a ticket with the message and any photos sent by MMS
            - Reply with the ticket number
            - Text the tenant when the ticket status changes
API:        REST
            POST /sms/inbound
            PATCH /tickets/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Telnyx Messaging
```

---

## Example 433

**Intent:**
missed call on our shop phone -> auto send sms "sorry we missed you, book here"

**Spec:**
```
Type:       Webhook service (missed call text-back)
Data model: MissedCall(id, caller_number, called_at, sms_sent)
Features:   - Receive call status webhooks from the phone provider
            - Detect calls that were not answered
            - Send a text with a booking link
            - Skip numbers that were texted in the last 24 hours
API:        REST
            POST /voice/status
Storage:    SQLite
Tech stack: Node.js, Express, Twilio Voice and Messaging
```

---

## Example 434

**Intent:**
transcribe voicemails and email them to me so I can read instead of listening

**Spec:**
```
Type:       Webhook service (voicemail transcription)
Features:   - Receive the recording-ready webhook from the phone provider
            - Download the recording
            - Transcribe it with a speech-to-text model
            - Email the transcript with caller number and audio attached
API:        REST
            POST /voicemail/recording
Tech stack: Python, Flask, Vonage Voice API, OpenAI Whisper (local)
```

---

## Example 435

**Intent:**
I want to know how much time I spend in meetings each week from my calendar

**Spec:**
```
Type:       Data analysis script (calendar time analysis)
Features:   - Read events from Google Calendar for a date range
            - Skip declined events and all-day events
            - Sum meeting hours per week and per attendee count
            - Chart meeting load over the last 3 months
Input:      Date range, OAuth credentials
Tech stack: Python, Google Calendar API, pandas, matplotlib
```

---

## Example 436

**Intent:**
our mobile app uploads videos and they fail on bad networks, need resumable uploads

**Spec:**
```
Type:       REST API service (resumable uploads)
Auth:       User access token
Data model: UploadSession(id, user_id, filename, total_bytes, received_bytes, status, expires_at)
Features:   - Create an upload session and return an upload URL
            - Accept chunks with offsets and resume after disconnects
            - Report the current offset so clients know where to continue
            - Assemble and verify the file with a checksum
            - Clean up abandoned sessions after 24 hours
API:        REST
            POST /uploads
            PATCH /uploads/{id}
            HEAD /uploads/{id}
Storage:    S3 multipart upload, PostgreSQL
Tech stack: Go, tusd, AWS S3
```

---

## Example 437

**Intent:**
scan all email attachments for viruses before they reach our staff

**Spec:**
```
Type:       Infrastructure setup (mail gateway virus scanning)
Features:   - Route inbound mail through a filtering gateway
            - Scan attachments with an antivirus engine
            - Block dangerous file types like .exe and macro documents
            - Quarantine infected mail and notify the recipient
            - Update virus signatures hourly
Tech stack: Rspamd, ClamAV, Postfix
```

---

## Example 438

**Intent:**
law firm: search all our past contracts and court documents by words and phrases, with highlighted results

**Spec:**
```
Type:       Web application (legal document search)
Auth:       Staff SSO with matter-based permissions
Data model: Document(id, matter_id, title, doc_type, text, filed_on)
            Matter(id, name, client)
Features:   - Index PDFs and Word files with extracted text
            - Search exact phrases and terms near each other
            - Highlight matches in context
            - Show only documents from matters the user can access
API:        REST
            GET  /search?q={query}&matter={id}
Storage:    Apache Solr
Tech stack: Java, Apache Tika, Solr, Spring Boot
```

---

## Example 439

**Intent:**
search all our company's code repositories at once

**Spec:**
```
Type:       Infrastructure setup (self-hosted code search)
Auth:       Company SSO
Features:   - Index all repositories from the Git server
            - Search with regular expressions and file filters
            - Re-index on every push
            - Respect repository permissions
Tech stack: Zoekt, Sourcegraph (self-hosted), GitLab
```

---

## Example 440

**Intent:**
suggest training courses to employees based on their role and what similar colleagues took

**Spec:**
```
Type:       REST API service (course recommendations)
Data model: Employee(id, role, department, seniority)
            Course(id, title, skills, duration_h)
            Enrollment(employee_id -> Employee, course_id -> Course, completed_at)
Features:   - Recommend courses taken by colleagues in the same role
            - Match course skills to skills required for the role
            - Exclude completed courses
            - Explain why each course was suggested
API:        REST
            GET  /employees/{id}/recommendations
Storage:    PostgreSQL
Tech stack: Python, LightFM, FastAPI
```

---

## Example 441

**Intent:**
count parts made by each machine on the line and show how efficient each one is

**Spec:**
```
Type:       IoT system (production counting / OEE)
Data model: Machine(id, name, ideal_cycle_s)
            PartCount(machine_id -> Machine, good, scrap, counted_at)
            Downtime(id, machine_id -> Machine, reason, started_at, ended_at)
Features:   - Count parts from machine PLC signals
            - Detect stops longer than 2 minutes and ask operators for a reason
            - Calculate availability, performance and quality per shift
            - Show live OEE on a shop floor screen
Storage:    InfluxDB, PostgreSQL
Tech stack: Node-RED, Siemens S7 protocol, InfluxDB, Grafana
```

---

## Example 442

**Intent:**
co2 sensors in every classroom, show teachers when to open the windows

**Spec:**
```
Type:       IoT system (classroom air quality)
Data model: Room(id, name)
            Co2Reading(room_id -> Room, co2_ppm, temperature_c, recorded_at)
Features:   - Measure CO2 every minute with NDIR sensors
            - Show a green, yellow or red light in the room
            - Show all rooms on a dashboard for the school
            - Report weekly averages per room
Storage:    InfluxDB
Tech stack: ESP32, SCD40 sensor, ESPHome, InfluxDB, Grafana
```

---

## Example 443

**Intent:**
reef aquarium controller: heater, lights schedule, ph and temp logging, alarm on my phone

**Spec:**
```
Type:       IoT system (aquarium controller)
Data model: Reading(temperature_c, ph, recorded_at)
Features:   - Keep water temperature in range by switching the heater relay
            - Ramp lights on a sunrise and sunset schedule
            - Log temperature and pH every 5 minutes
            - Push a phone alert when values leave the safe range
Storage:    SQLite
Tech stack: Raspberry Pi, Python, Atlas Scientific pH probe, Pushover
```

---

## Example 444

**Intent:**
my boat is in the harbour all winter, tell me if the bilge water gets high or the battery is low

**Spec:**
```
Type:       IoT system (boat monitoring)
Features:   - Read a bilge float switch and battery voltage
            - Send status once a day over LTE-M
            - Send an immediate alert when the bilge switch triggers
            - Report GPS position if the boat moves
Tech stack: Particle Boron, Particle Cloud webhooks, Pushover
```

---

## Example 445

**Intent:**
Customers of our API want to see a log of every request their keys made, with status codes.

**Spec:**
```
Type:       Data pipeline (customer API request logs)
Data model: RequestLog(customer_id, api_key_prefix, method, path, status, latency_ms, occurred_at)
Features:   - Emit a log event from the gateway for each request
            - Store logs per customer for 30 days
            - Let customers filter by key, status and endpoint
            - Hide request bodies and secrets
API:        REST
            GET  /me/request-logs?status={code}&from={t}
Storage:    ClickHouse
Tech stack: Envoy access logs, Vector, ClickHouse, Go
```

---

## Example 446

**Intent:**
GDPR says we need a list of all processing activities and what data each system holds

**Spec:**
```
Type:       Web application (records of processing activities)
Auth:       Staff SSO; DPO role for approval
Data model: System(id, name, owner, hosting_location)
            ProcessingActivity(id, name, purpose, legal_basis, retention, system_ids)
            DataCategory(id, name, sensitive)
Features:   - Register systems and the data categories they hold
            - Describe processing activities with purpose and legal basis
            - Remind owners to review entries yearly
            - Export the register as a PDF for regulators
API:        REST
            GET  /activities
            POST /activities
            GET  /export.pdf
Storage:    PostgreSQL
Tech stack: Python, Django, WeasyPrint
```

---

## Example 447

**Intent:**
email each of our customers a monthly usage summary of their account

**Spec:**
```
Type:       Scheduled script (monthly usage emails)
Features:   - Run on the 2nd of each month
            - Calculate each account's usage for the past month
            - Compare with the previous month
            - Send a personalized HTML email to the account owner
            - Skip accounts that opted out of reports
Input:      Database URL, email provider API key
Tech stack: TypeScript, Node.js, React Email, Resend
```

---

## Example 448

**Intent:**
static site deploys should switch instantly, no half-uploaded state

**Spec:**
```
Type:       Infrastructure setup (atomic static deploys)
Features:   - Upload each build into a new timestamped release folder
            - Switch a current symlink to the new folder in one step
            - Keep the last 5 releases for instant rollback
            - Clean up older releases
Tech stack: Nginx, rsync, Bash, GitHub Actions
```

---

## Example 449

**Intent:**
self-host a family recipe collection where we can import recipes from websites

**Spec:**
```
Type:       Infrastructure setup (self-hosted recipe manager)
Auth:       Family member accounts
Features:   - Import recipes from a URL with structured data
            - Plan meals for the week
            - Build shopping lists from planned meals
            - Back up the database nightly
Storage:    PostgreSQL
Tech stack: Mealie, Docker Compose
```

---

## Example 450

**Intent:**
I want names like nas.home and printer.home to work on my home network instead of IPs

**Spec:**
```
Type:       Infrastructure setup (local DNS)
Features:   - Run a local DNS server on the home network
            - Add local records for each device
            - Hand out the DNS server through router DHCP
            - Forward other queries to public resolvers
Tech stack: AdGuard Home, Raspberry Pi
```

---

## Example 451

**Intent:**
wireguard vpn for our 8 person team with a simple web page to add people

**Spec:**
```
Type:       Infrastructure setup (team WireGuard VPN)
Auth:       Admin password for the web UI
Features:   - Run WireGuard on a small cloud server
            - Add and remove users from a web interface
            - Show QR codes and config files for each device
            - Route only office network ranges through the tunnel
Tech stack: wg-easy, Docker, WireGuard
```

---

## Example 452

**Intent:**
pocket travel router so all my devices use VPN in hotels

**Spec:**
```
Type:       Infrastructure setup (travel VPN router)
Features:   - Connect the travel router to hotel Wi-Fi including captive portals
            - Send all traffic through a WireGuard tunnel to home
            - Block traffic if the tunnel drops
            - Share one private Wi-Fi network with all devices
Tech stack: GL.iNet router, OpenWrt, WireGuard
```

---

## Example 453

**Intent:**
my portfolio site on github pages with my own domain

**Spec:**
```
Type:       Infrastructure setup (GitHub Pages hosting)
Features:   - Build the site with a GitHub Actions workflow
            - Publish to GitHub Pages
            - Add the custom domain with a CNAME file and DNS records
            - Enforce HTTPS
Tech stack: GitHub Pages, GitHub Actions, Jekyll
```

---

## Example 454

**Intent:**
Different endpoints of our public API need different limits — search 10/min, reads 100/min.

**Spec:**
```
Type:       Infrastructure setup (per-endpoint rate limiting)
Features:   - Define limit zones per location in the reverse proxy
            - Key limits by API key header, falling back to IP
            - Allow small bursts above the rate
            - Return 429 with JSON error bodies
Tech stack: Nginx limit_req, Lua (OpenResty)
```

---

## Example 455

**Intent:**
cheap url shortener on my shared php hosting

**Spec:**
```
Type:       Web application (self-hosted URL shortener)
Auth:       Admin login
Data model: Url(keyword, url, title, created_at, clicks)
Features:   - Shorten URLs with custom keywords
            - Track clicks and referrers
            - Provide a bookmarklet for quick shortening
            - Offer an API for other tools
API:        REST
            GET  /yourls-api.php?action=shorturl
Storage:    MySQL
Tech stack: YOURLS, PHP, MySQL
```

---

## Example 456

**Intent:**
address autocomplete for the whole world without paying google

**Spec:**
```
Type:       Infrastructure setup (self-hosted address autocomplete)
Features:   - Run a search-as-you-type geocoder on OpenStreetMap data
            - Bias results to the user's location
            - Return structured address parts
            - Update the data monthly
API:        REST
            GET  /api?q={text}&lat={lat}&lon={lon}
Tech stack: Photon geocoder, OpenStreetMap, Docker
```

---

## Example 457

**Intent:**
our accounting needs invoice amounts converted to euro at the rate of the invoice date, not today

**Spec:**
```
Type:       REST API service (historical currency conversion)
Data model: DailyRate(date, currency, rate_to_eur, source)
Features:   - Store daily ECB rates going back 10 years
            - Convert an amount at the rate of a given date
            - Use the previous business day's rate on weekends and holidays
            - Return the rate and date used for audit
API:        REST
            GET  /convert?amount={n}&currency={c}&date={d}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, ECB SDMX API
```

---

## Example 458

**Intent:**
which features each customer can use depends on their plan and add-ons. one service that answers "can this customer use X?"

**Spec:**
```
Type:       REST API service (entitlements)
Data model: Plan(id, name)
            Feature(id, key, type)
            PlanFeature(plan_id -> Plan, feature_id -> Feature, limit_value)
            CustomerEntitlement(customer_id, feature_id -> Feature, limit_value, source, expires_at)
Features:   - Combine plan features with purchased add-ons and overrides
            - Answer boolean and numeric limit checks
            - Cache entitlements per customer
            - Update entitlements when the subscription changes
API:        REST
            GET  /customers/{id}/entitlements
            GET  /customers/{id}/entitlements/{feature}
Storage:    PostgreSQL, Redis
Tech stack: TypeScript, NestJS, Prisma
```

---

## Example 459

**Intent:**
our tenants send SMS through our platform, bill them per message by country

**Spec:**
```
Type:       Data pipeline (SMS usage billing)
Data model: SmsRecord(id, tenant_id, country, segments, provider_cost, sent_at)
            CountryPrice(country, price_per_segment)
Features:   - Record each sent SMS with country and segment count
            - Price messages from a per-country price list
            - Total usage per tenant per month
            - Show margin between provider cost and price
Storage:    PostgreSQL
Tech stack: Python, dbt, PostgreSQL
```

---

## Example 460

**Intent:**
let me host my static website on IPFS so it can't be taken down easily

**Spec:**
```
Type:       Infrastructure setup (IPFS static hosting)
Features:   - Build the site and add the folder to IPFS
            - Pin the content on own node and a pinning service
            - Point a domain at it with DNSLink
            - Serve it through a public gateway for normal browsers
Tech stack: Kubo (IPFS), Pinata, Cloudflare DNS
```

---

## Example 461

**Intent:**
Internal event bus so our services can publish and subscribe to events without calling each other directly.

**Spec:**
```
Type:       Infrastructure setup (event bus)
Features:   - Run a clustered message broker with persistent streams
            - Define subjects per domain like orders.created
            - Give each consumer a durable subscription with acknowledgments
            - Keep events for 7 days for replay
            - Restrict publish and subscribe rights per service
Tech stack: NATS JetStream, Kubernetes, Helm
```

---

## Example 462

**Intent:**
rotate kubernetes service account tokens and stop using the old never-expiring ones

**Spec:**
```
Type:       Infrastructure setup (Kubernetes token hygiene)
Features:   - Switch workloads to projected tokens that expire after 1 hour
            - Find and delete legacy long-lived token secrets
            - Disable automatic token mounting where not needed
            - Audit which service accounts have cluster-wide rights
Tech stack: Kubernetes, kubectl, Kyverno policies
```

---

## Example 463

**Intent:**
barcode images api, give a number get code128 or qr png

**Spec:**
```
Type:       REST API service (barcode image generation)
Features:   - Generate Code 128, EAN-13, DataMatrix and QR images
            - Validate input for each symbology
            - Return PNG or SVG at a requested height
            - Print the human-readable text under linear barcodes
API:        REST
            GET  /barcode/{type}/{value}?format={png|svg}&height={px}
Tech stack: Java, Zxing, Javalin
```

---

## Example 464

**Intent:**
validate json sent by partners against our schemas before it goes into the system

**Spec:**
```
Type:       REST API service (JSON Schema validation)
Data model: Schema(id, name, version, schema_json)
Features:   - Register versioned JSON Schemas
            - Validate payloads and return all errors with JSON paths
            - Let partners test payloads in a sandbox endpoint
            - Count validation failures per partner and schema
API:        REST
            POST /schemas
            POST /schemas/{name}/{version}/validate
Storage:    PostgreSQL
Tech stack: Node.js, Ajv, Fastify
```

---

## Example 465

**Intent:**
Our IT shared mailbox gets 300 mails a day. Sort them into folders automatically: password resets, hardware, access requests.

**Spec:**
```
Type:       Scheduled script (mailbox categorization)
Features:   - Read new messages from the shared Outlook mailbox every 5 minutes
            - Classify each message by keywords and a small text classifier
            - Move messages to matching folders and add categories
            - Leave unsure messages in the inbox
Input:      Mailbox address, Azure app credentials
Tech stack: Python, Microsoft Graph API, scikit-learn
```

---

## Example 466

**Intent:**
people upload photos to a dropbox folder for our event and we want them on a slideshow website

**Spec:**
```
Type:       Webhook service (Dropbox photo slideshow)
Data model: Photo(id, dropbox_path, thumbnail_key, uploaded_at, approved)
Features:   - Receive Dropbox change webhooks for the event folder
            - Download new photos and create web-sized versions
            - Let an organizer approve photos
            - Show approved photos in a full-screen slideshow page
API:        REST
            POST /webhooks/dropbox
            GET  /slideshow/photos
Storage:    SQLite, local disk
Tech stack: Python, Flask, Dropbox API, Pillow
```

---

## Example 467

**Intent:**
kubernetes ingress with automatic https certificates for all our services

**Spec:**
```
Type:       Infrastructure setup (Kubernetes ingress and TLS)
Features:   - Install an ingress controller with a cloud load balancer
            - Issue Let's Encrypt certificates automatically per hostname
            - Redirect HTTP to HTTPS
            - Create DNS records from ingress hostnames
Tech stack: ingress-nginx, cert-manager, external-dns, Kubernetes
```

---

## Example 468

**Intent:**
report of which employees still don't have 2FA turned on in google workspace and github

**Spec:**
```
Type:       Scheduled script (MFA enforcement report)
Features:   - List Google Workspace users without 2-step verification
            - List GitHub organization members without 2FA
            - Combine results by email
            - Email the report weekly to IT and remind each person
Input:      Admin credentials for both services
Tech stack: Python, Google Admin SDK Directory API, GitHub REST API
```

---

## Example 469

**Intent:**
Set up MySQL with a replica so reports don't slow down the main shop database.

**Spec:**
```
Type:       Infrastructure setup (MySQL read replica)
Features:   - Configure GTID-based replication from primary to replica
            - Point reporting tools at the replica only
            - Make the replica read-only
            - Alert when replica lag exceeds 60 seconds
Storage:    MySQL 8 (primary and replica)
Tech stack: MySQL, Ansible, Percona Toolkit
```

---

## Example 470

**Intent:**
background job queue as a service for our small apps, so each app doesnt need its own

**Spec:**
```
Type:       REST API service (job queue)
Auth:       API key per app
Data model: Queue(id, app_id, name, max_retries, visibility_timeout_s)
            Job(id, queue_id -> Queue, payload_json, status, attempts, run_at, locked_until)
Features:   - Enqueue jobs with optional delay
            - Let workers lease jobs with a visibility timeout
            - Acknowledge or fail jobs with retry backoff
            - Move jobs to a dead-letter state after max retries
API:        REST
            POST /queues/{name}/jobs
            POST /queues/{name}/lease
            POST /jobs/{id}/ack
            POST /jobs/{id}/fail
Storage:    PostgreSQL (SELECT FOR UPDATE SKIP LOCKED)
Tech stack: Go, pgx, Chi
```

---

## Example 471

**Intent:**
every PR's preview site needs test data too, not an empty database

**Spec:**
```
Type:       Command-line script (preview environment seeding)
Features:   - Run after each preview environment is created
            - Apply migrations to the fresh database
            - Load a curated seed dataset with demo users
            - Print demo login credentials into the PR comment
Input:      Preview database URL, PR number
Tech stack: Node.js, Prisma migrate, Prisma seed, GitHub CLI
```

---

## Example 472

**Intent:**
small private image host for our forum, users upload and get a link to embed

**Spec:**
```
Type:       Web application (image hosting)
Auth:       Forum account login via OAuth
Data model: Image(id, user_id, key, width, height, size_bytes, uploaded_at, deleted)
Features:   - Upload images by drag and drop or paste
            - Resize large images and strip EXIF
            - Return a direct link and BBCode embed
            - Let users delete their images
            - Serve images through a CDN
API:        REST
            POST /images
            DELETE /images/{id}
            GET  /i/{key}
Storage:    PostgreSQL, Cloudflare R2
Tech stack: Go, libvips, Cloudflare CDN
```

---

## Example 473

**Intent:**
generate my resume as pdf from a json file so i can update it easily

**Spec:**
```
Type:       Command-line tool (resume generator)
Features:   - Read resume data from a JSON Resume file
            - Render it with a chosen HTML theme
            - Export a one-page PDF
            - Validate the JSON against the schema first
Input:      resume.json, theme name
Tech stack: Node.js, resumed, Puppeteer
```

---

## Example 474

**Intent:**
optimize all svg icons in our repo, they have lots of junk from illustrator

**Spec:**
```
Type:       Command-line tool (SVG optimization)
Features:   - Remove editor metadata, comments and hidden elements
            - Merge paths and round numbers
            - Keep viewBox and accessibility titles
            - Fail CI when an unoptimized SVG is committed
Input:      Folder of SVG files
Tech stack: Node.js, SVGO, lint-staged
```

---

## Example 475

**Intent:**
wikidata is hard to query. a simple api: give a city name, get population, country, coordinates

**Spec:**
```
Type:       REST API service (Wikidata city facts)
Data model: CityCache(qid, name, country, population, latitude, longitude, fetched_at)
Features:   - Search Wikidata entities that are instances of city
            - Run a SPARQL query for population, country and coordinates
            - Pick the latest population value by date
            - Cache answers for 30 days
API:        REST
            GET  /cities?name={name}
Storage:    SQLite
Tech stack: Python, SPARQLWrapper, FastAPI
```

---

## Example 476

**Intent:**
historical weather for any date and place for our insurance claims checks

**Spec:**
```
Type:       REST API service (historical weather)
Auth:       Internal API key
Data model: WeatherDay(lat_rounded, lon_rounded, date, temp_max_c, precipitation_mm, wind_gust_kmh, hail_flag)
Features:   - Return daily weather for a coordinate and date
            - Fetch from a reanalysis archive and cache results
            - Flag storm, hail and heavy rain days
            - Produce a PDF summary for a claim file
API:        REST
            GET  /weather/history?lat={lat}&lon={lon}&date={d}
            GET  /weather/history/report.pdf
Storage:    PostgreSQL
Tech stack: Python, Open-Meteo Historical API, FastAPI, ReportLab
```

---

## Example 477

**Intent:**
Calendly bookings should create a deal in Pipedrive with the meeting time.

**Spec:**
```
Type:       Webhook service (Calendly to Pipedrive)
Features:   - Receive invitee.created webhooks from Calendly
            - Find or create the person and organization in Pipedrive
            - Create a deal and an activity at the meeting time
            - Mark the activity cancelled on invitee.canceled
API:        REST
            POST /webhooks/calendly
Tech stack: Node.js, Express, Pipedrive API
```

---

## Example 478

**Intent:**
moving dropbox photos into thumbnails for our real estate listings site automatically

**Spec:**
```
Type:       Data pipeline (listing photo processing)
Data model: Listing(id, reference, dropbox_folder)
            ListingPhoto(id, listing_id -> Listing, original_key, large_key, thumb_key, position)
Features:   - Watch each listing's Dropbox folder for new photos
            - Create large and thumbnail sizes
            - Upload them to the website storage
            - Keep photo order from the file names
Storage:    PostgreSQL, S3
Tech stack: Python, Dropbox API, Pillow, AWS Lambda
```

---

## Example 479

**Intent:**
mi empresa necesita un servidor git propio porque no podemos usar github por contrato con el cliente

**Spec:**
```
Type:       Infrastructure setup (on-premise Git platform)
Auth:       LDAP login with 2FA
Features:   - Install a self-managed Git platform on the company server
            - Connect user accounts to the company LDAP
            - Run CI pipelines on internal runners
            - Back up repositories and configuration daily
            - Restrict access to the internal network and VPN
Storage:    PostgreSQL, local disk
Tech stack: GitLab Community Edition, GitLab Runner, Ubuntu Server
```

---

## Example 480

**Intent:**
ok so our app server is a single VM and when we deploy it's down for 2 min. users complain. fix w/o kubernetes pls

**Spec:**
```
Type:       Infrastructure setup (zero-downtime single-host deploys)
Features:   - Run two app containers behind a local reverse proxy
            - Start the new version on a second port and wait for health checks
            - Switch the proxy upstream and reload without dropping connections
            - Stop the old container after in-flight requests finish
Tech stack: Docker, Caddy, Bash deploy script
```

---

## Example 481

**Intent:**
want to see when my aws costs spike same day not end of month

**Spec:**
```
Type:       Scheduled script (daily cost anomaly check)
Features:   - Pull yesterday's cost by service each morning
            - Compare with the 14-day average per service
            - Flag services more than 50% above normal
            - Send a short message with the top increases
Input:      AWS credentials, threshold percent
Tech stack: Python, boto3 Cost Explorer, AWS Lambda, EventBridge Scheduler
```

---

## Example 482

**Intent:**
I run a tiny SaaS and want customers to download their invoices as PDF from their account page.

**Spec:**
```
Type:       REST API service (customer invoice downloads)
Auth:       Customer session login
Data model: Invoice(id, customer_id, number, issued_on, total, currency, pdf_key)
Features:   - List a customer's invoices
            - Generate the PDF on first download and store it
            - Return a time-limited download link
            - Allow access only to the customer's own invoices
API:        REST
            GET  /me/invoices
            GET  /me/invoices/{id}/pdf
Storage:    PostgreSQL, S3
Tech stack: Python, Django, WeasyPrint
```

---

