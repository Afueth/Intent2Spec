## Example 1

**Intent:**
slack message when someone pays on stripe

**Spec:**
```
Type:       Webhook service (Stripe to Slack)
Data model: PaymentEvent(id, stripe_event_id, amount, currency, customer_email, received_at)
Features:   - Receive Stripe webhook events at a single endpoint
            - Verify the Stripe-Signature header with the signing secret
            - Ignore duplicate events by checking the stored event ID (idempotency)
            - Post a message to a Slack channel for each payment_intent.succeeded event
            - Retry failed Slack posts up to 3 times with backoff
API:        REST
            POST /webhooks/stripe
Storage:    PostgreSQL (processed events)
Tech stack: Node.js, Express, Stripe SDK, Slack Incoming Webhooks
```

---

## Example 2

**Intent:**
I run a small online candle shop on Shopify and I want every new order to be added as a row in a Google Sheet so my mum can see what to pack each morning.

**Spec:**
```
Type:       Webhook service (Shopify to Google Sheets)
Data model: SyncedOrder(id, shopify_order_id, sheet_row, synced_at)
Features:   - Receive Shopify orders/create webhooks
            - Verify the X-Shopify-Hmac-Sha256 header
            - Append a row with order number, customer name, items, quantities and shipping address
            - Skip orders that were already synced (idempotent by order ID)
            - Mark the row as cancelled when an orders/cancelled webhook arrives
API:        REST
            POST /webhooks/shopify/orders-create
            POST /webhooks/shopify/orders-cancelled
Storage:    SQLite (synced order IDs)
Tech stack: Python, Flask, Google Sheets API (gspread), Shopify webhooks
```

---

## Example 3

**Intent:**
discord bot that tells my server when my twitch stream goes live

**Spec:**
```
Type:       Bot (Discord)
Data model: StreamerSub(id, guild_id, channel_id, twitch_login, last_live_at)
Features:   - Subscribe to Twitch EventSub stream.online events for configured streamers
            - Verify Twitch EventSub message signatures
            - Post an embed with stream title, game and link to the chosen Discord channel
            - Add a /notify-add slash command to register a Twitch channel
            - Skip repeat announcements for the same stream session
API:        REST
            POST /twitch/eventsub
Storage:    SQLite
Tech stack: Node.js, discord.js, Twitch EventSub API
```

---

## Example 4

**Intent:**
uptime checker for my 5 websites, text me if one goes down

**Spec:**
```
Type:       Scheduled script (uptime monitoring)
Data model: Site(id, name, url, expected_status)
            CheckResult(id, site_id -> Site, status_code, response_ms, checked_at, is_up)
Features:   - Send an HTTP request to each site every minute
            - Mark a site as down after 3 consecutive failures
            - Send an SMS when a site goes down and again when it recovers
            - Record response times for each check
            - Print a daily uptime percentage summary
Storage:    SQLite
Tech stack: Python, httpx, APScheduler, Twilio SMS API
```

---

## Example 5

**Intent:**
We need a REST API for our mobile app where users log in with email and password and get a JWT, plus refresh tokens so they stay logged in.

**Spec:**
```
Type:       REST API service (authentication)
Auth:       Email + password (bcrypt), short-lived JWT access tokens, rotating refresh tokens
Data model: User(id, email, password_hash, email_verified, created_at)
            RefreshToken(id, user_id -> User, token_hash, expires_at, revoked_at)
Features:   - Register users and send an email verification link
            - Issue a 15-minute access token and a 30-day refresh token on login
            - Rotate refresh tokens on every use and revoke reused ones
            - Log out by revoking the current refresh token
            - Rate limit login attempts per IP and per email
API:        REST
            POST /auth/register
            POST /auth/login
            POST /auth/refresh
            POST /auth/logout
            GET  /auth/verify-email?token={token}
Storage:    PostgreSQL
Tech stack: Go, chi router, golang-jwt, bcrypt
```

---

## Example 6

**Intent:**
github actions to run my python tests on every push

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Trigger a workflow on every push and pull request
            - Test against Python 3.10, 3.11 and 3.12 in a matrix
            - Cache pip dependencies between runs
            - Run linting with ruff before the test step
            - Run pytest and upload the coverage report as an artifact
            - Block merging a pull request when the workflow fails
Tech stack: GitHub Actions, Python, pytest, ruff, pytest-cov
```

---

## Example 7

**Intent:**
telegram bot that reminds our team of standup at 10

**Spec:**
```
Type:       Bot (Telegram)
Data model: Team(id, chat_id, standup_time, timezone)
            StandupReply(id, team_id -> Team, user_name, text, date)
Features:   - Post a standup reminder in the group chat at the set time on weekdays
            - Collect each member's reply with a /standup command
            - Post a summary of all replies 30 minutes later
            - Let an admin change the time with /settime
            - Skip public holidays from a configured list
Storage:    SQLite
Tech stack: Python, python-telegram-bot, APScheduler
```

---

## Example 8

**Intent:**
i want backups of my postgres database every night and keep them for 30 days

**Spec:**
```
Type:       Scheduled script (database backup)
Features:   - Run pg_dump every night at 02:00 in custom format
            - Compress and encrypt each dump with GPG
            - Upload the file to an S3 bucket with a dated name
            - Delete backups older than 30 days with an S3 lifecycle rule
            - Send an email alert if the backup fails
            - Test-restore the latest backup into a scratch database once a week
Storage:    Amazon S3
Tech stack: Bash, pg_dump, GPG, AWS CLI, cron
```

---

## Example 9

**Intent:**
Can you make something so when a lead fills out the contact form on our website it goes straight into HubSpot and pings the sales channel in Slack?

**Spec:**
```
Type:       Webhook service (form to CRM)
Data model: Lead(id, name, email, company, message, hubspot_contact_id, created_at)
Features:   - Accept form submissions from the website with a honeypot field for spam
            - Create or update the contact in HubSpot by email
            - Post the lead's name, company and message to the #sales Slack channel
            - Queue failed HubSpot calls and retry them with exponential backoff
            - Return a thank-you response to the website immediately
API:        REST
            POST /forms/contact
Storage:    PostgreSQL (leads), Redis (retry queue)
Tech stack: Node.js, Fastify, HubSpot API, Slack Web API, BullMQ
```

---

## Example 10

**Intent:**
graphql api for a bookstore

**Spec:**
```
Type:       GraphQL API service
Auth:       JWT bearer tokens; admin role for write operations
Data model: Book(id, title, isbn, price, stock, author_id -> Author)
            Author(id, name, bio)
            Review(id, book_id -> Book, user_id, rating, text)
Features:   - Query books with filters by author, price range and stock
            - Resolve authors and reviews with batched loaders to avoid N+1 queries
            - Add, update and delete books through admin-only mutations
            - Paginate book lists with cursor-based pagination
            - Limit query depth and complexity
API:        GraphQL
            POST /graphql
Storage:    PostgreSQL
Tech stack: TypeScript, Apollo Server, Prisma, DataLoader
```

---

## Example 11

**Intent:**
my wordpress site went down last week and nobody noticed for 2 days. i need something that watches it and also checks the ssl certificate isnt about to expire, and emails me and my co-founder. we dont have a big budget so cheap please

**Spec:**
```
Type:       Scheduled script (uptime and SSL monitoring)
Data model: Check(id, url, status_code, response_ms, ssl_expires_at, checked_at)
Features:   - Request the homepage every 5 minutes and check for a 200 response and expected text
            - Read the SSL certificate expiry date once a day
            - Email both founders when the site is down for 2 checks in a row
            - Warn 14 days and 3 days before the certificate expires
            - Send a recovery email with total downtime
Storage:    SQLite
Tech stack: Python, requests, ssl module, cron on a small VPS, SMTP (Gmail)
```

---

## Example 12

**Intent:**
whatsapp bot for my restaurant to take table bookings

**Spec:**
```
Type:       Bot (WhatsApp)
Data model: Booking(id, phone, name, party_size, date, time, status)
            Table(id, seats)
Features:   - Reply to incoming messages with a guided booking flow (date, time, party size)
            - Check table availability before confirming
            - Send a confirmation message with booking details
            - Let customers cancel by replying CANCEL
            - Send a reminder message 3 hours before the booking
API:        REST
            POST /webhooks/whatsapp
            GET  /webhooks/whatsapp (verification challenge)
Storage:    PostgreSQL
Tech stack: Python, FastAPI, WhatsApp Cloud API
```

---

## Example 13

**Intent:**
deploy my node app to aws with docker

**Spec:**
```
Type:       Infrastructure setup (deployment)
Features:   - Build a Docker image for the Node.js app with a multi-stage Dockerfile
            - Push the image to Amazon ECR
            - Run the container on ECS Fargate behind an Application Load Balancer
            - Store secrets in AWS Secrets Manager and inject them as environment variables
            - Add a health check endpoint used by the load balancer
            - Roll out new versions with zero-downtime rolling deployments
Tech stack: Docker, AWS ECR, ECS Fargate, ALB, Secrets Manager, Terraform
```

---

## Example 14

**Intent:**
helo, i need service for send email notifications when user do actions in our app, like register or forgot password. we use java

**Spec:**
```
Type:       REST API service (notifications)
Auth:       Internal API key for calling services
Data model: EmailTemplate(id, name, subject, body_html, locale)
            EmailJob(id, template_id -> EmailTemplate, to_address, variables_json, status, attempts, sent_at)
Features:   - Accept send requests with a template name and variables
            - Render templates in the user's language
            - Put jobs on a queue and send them in the background
            - Retry failed sends up to 5 times with backoff
            - Record delivery, bounce and complaint events from the email provider
API:        REST
            POST /notifications/email
            GET  /notifications/email/{id}
            POST /webhooks/ses
Storage:    PostgreSQL, RabbitMQ (job queue)
Tech stack: Java, Spring Boot, Thymeleaf templates, Amazon SES
```

---

## Example 15

**Intent:**
collect logs from all our servers in one place

**Spec:**
```
Type:       Infrastructure setup (log aggregation)
Features:   - Ship logs from each server with an agent that tails application and system logs
            - Parse JSON and plain-text log lines into structured fields
            - Index logs by service, host and level
            - Search and filter logs in a web UI
            - Keep logs for 14 days and delete older data automatically
            - Alert when the error count for a service passes a threshold
Storage:    Loki (log storage), object storage for chunks
Tech stack: Grafana Loki, Promtail, Grafana, Docker Compose
```

---

## Example 16

**Intent:**
pls make a bot for our discord that gives roles when ppl react to a msg

**Spec:**
```
Type:       Bot (Discord)
Data model: ReactionRole(id, guild_id, message_id, emoji, role_id)
Features:   - Let admins link an emoji on a message to a role with /reactionrole add
            - Give the role when a member adds the reaction
            - Remove the role when the reaction is removed
            - List all reaction-role links with /reactionrole list
            - Check the bot's role is high enough before assigning
Storage:    SQLite
Tech stack: Python, discord.py
```

---

## Example 17

**Intent:**
An internal API that our different services call to check if a user is allowed to do something, like role based permissions.

**Spec:**
```
Type:       REST API service (authorization)
Auth:       Service-to-service mTLS
Data model: Role(id, name)
            Permission(id, resource, action)
            RolePermission(role_id -> Role, permission_id -> Permission)
            UserRole(user_id, role_id -> Role, tenant_id)
Features:   - Check if a user can perform an action on a resource
            - Manage roles and their permissions
            - Assign and remove roles per user and tenant
            - Cache permission lookups for 60 seconds
            - Log every denied check for auditing
API:        REST
            POST /authz/check
            GET  /roles
            POST /roles/{id}/permissions
            POST /users/{id}/roles
Storage:    PostgreSQL, Redis (cache)
Tech stack: Go, chi router, PostgreSQL, Redis
```

---

## Example 18

**Intent:**
quickbooks invoice paid -> mark the job done in our airtable

**Spec:**
```
Type:       Webhook service (QuickBooks to Airtable)
Data model: InvoiceLink(id, qb_invoice_id, airtable_record_id, paid_at)
Features:   - Receive QuickBooks Online webhook notifications for invoice changes
            - Verify the intuit-signature header
            - Fetch the invoice and check that its balance is zero
            - Set the matching Airtable job record's status to Done
            - Log invoices that have no linked Airtable record
API:        REST
            POST /webhooks/quickbooks
Storage:    SQLite
Tech stack: Python, FastAPI, QuickBooks Online API, Airtable API
```

---

## Example 19

**Intent:**
server monitoring with prometheus and grafana

**Spec:**
```
Type:       Infrastructure setup (monitoring)
Features:   - Install node_exporter on every server for CPU, memory, disk and network metrics
            - Scrape all targets from Prometheus every 15 seconds
            - Show server dashboards in Grafana
            - Alert through Alertmanager when disk usage passes 85% or a host stops reporting
            - Route alerts to email and a Slack channel
            - Keep metrics for 30 days
Storage:    Prometheus time-series database
Tech stack: Prometheus, node_exporter, Alertmanager, Grafana, Docker Compose
```

---

## Example 20

**Intent:**
my small team keeps forgetting to renew domain names and we lost one last year which was super embarrassing. something that checks all our domains and warns us like a month before

**Spec:**
```
Type:       Scheduled script (domain expiry monitoring)
Data model: Domain(id, name, registrar, expires_at, last_checked_at)
Features:   - Look up each domain's expiry date with RDAP once a day
            - Warn the team 30, 14 and 3 days before a domain expires
            - Post warnings to a Slack channel and send an email
            - Add and remove domains from a YAML config file
            - Report domains whose lookup fails
Storage:    SQLite
Tech stack: Python, httpx (RDAP lookups), Slack Incoming Webhooks
```

---

## Example 21

**Intent:**
api so customers can pay with paypal on our site

**Spec:**
```
Type:       REST API service (payments)
Auth:       Session-based login for customers
Data model: Order(id, user_id, total, currency, status)
            Payment(id, order_id -> Order, paypal_order_id, status, captured_at)
Features:   - Create a PayPal order for a checkout
            - Capture the payment after the customer approves it
            - Receive PayPal webhooks and verify them with the PayPal API
            - Mark orders as paid only after a confirmed capture
            - Handle refunds and update the order status
API:        REST
            POST /payments/paypal/orders
            POST /payments/paypal/orders/{id}/capture
            POST /webhooks/paypal
Storage:    PostgreSQL
Tech stack: PHP, Laravel, PayPal Orders API v2
```

---

## Example 22

**Intent:**
slack bot for /lunch to pick a random restaurant

**Spec:**
```
Type:       Bot (Slack)
Data model: Restaurant(id, workspace_id, name, cuisine, added_by)
Features:   - Respond to /lunch with a random restaurant from the list
            - Add restaurants with /lunch add <name>
            - Avoid picking the same place twice in one week
            - Start a quick vote with buttons when called with /lunch vote
            - Verify Slack request signatures
API:        REST
            POST /slack/commands
            POST /slack/interactions
Storage:    SQLite
Tech stack: Python, Slack Bolt
```

---

## Example 23

**Intent:**
we use gitlab, want the app to build and deploy to the staging server automatically when merging to develop branch

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Run tests and lint on every merge request
            - Build a Docker image and push it to the GitLab Container Registry on merges to develop
            - Deploy to the staging server over SSH with docker compose pull and up
            - Run database migrations as part of the deploy job
            - Notify the team in chat when a deploy succeeds or fails
            - Require manual approval for production deploys from main
Tech stack: GitLab CI/CD, Docker, Docker Compose, SSH deploy keys
```

---

## Example 24

**Intent:**
send customers a text when their order ships

**Spec:**
```
Type:       Webhook service (shipping notifications)
Data model: Shipment(id, order_id, phone, carrier, tracking_number, notified_at)
Features:   - Receive fulfillment-created webhooks from the store
            - Build a tracking link from the carrier and tracking number
            - Send an SMS with the tracking link to the customer
            - Respect customers who replied STOP (opt-out list)
            - Skip duplicate webhooks for the same shipment
API:        REST
            POST /webhooks/fulfillment
            POST /webhooks/sms-inbound
Storage:    PostgreSQL
Tech stack: Node.js, Express, Twilio Programmable SMS
```

---

## Example 25

**Intent:**
ok so we have this legacy SOAP service from a supplier that nobody understands and our new frontend team wants JSON. could you design a little layer in between that turns their stuff into a normal REST API? it's slow too so caching would be nice

**Spec:**
```
Type:       REST API service (SOAP wrapper)
Auth:       API key per frontend client
Features:   - Translate REST calls into SOAP requests to the supplier service
            - Convert SOAP XML responses into clean JSON
            - Cache product and price lookups for 15 minutes
            - Map SOAP faults to proper HTTP error codes
            - Time out supplier calls after 10 seconds and return 504
            - Expose OpenAPI documentation
API:        REST
            GET  /products
            GET  /products/{sku}
            GET  /products/{sku}/price
            POST /orders
Storage:    Redis (cache)
Tech stack: Python, FastAPI, zeep (SOAP client), Redis
```

---

## Example 26

**Intent:**
telegram bot to track my expenses by typing them

**Spec:**
```
Type:       Bot (Telegram)
Data model: Expense(id, chat_id, amount, category, note, spent_at)
Features:   - Parse messages like "12.50 food lunch" into amount, category and note
            - Show today's and this month's totals with /total
            - Show spending by category with /report
            - Delete the last entry with /undo
            - Export expenses as a CSV file with /export
Storage:    SQLite
Tech stack: Python, aiogram
```

---

## Example 27

**Intent:**
terraform for a basic aws setup: vpc, rds, ec2

**Spec:**
```
Type:       Infrastructure setup (infrastructure as code)
Features:   - Create a VPC with public and private subnets in two availability zones
            - Launch an EC2 instance in the public subnet with a security group for HTTP, HTTPS and SSH
            - Create a PostgreSQL RDS instance in the private subnets
            - Allow database access only from the EC2 security group
            - Store Terraform state in S3 with a DynamoDB lock table
            - Output the instance IP and database endpoint
Tech stack: Terraform, AWS (VPC, EC2, RDS, S3, DynamoDB)
```

---

## Example 28

**Intent:**
webhook that gets github push events and posts commit messages to our teams chat

**Spec:**
```
Type:       Webhook service (GitHub to Microsoft Teams)
Features:   - Receive GitHub push events
            - Verify the X-Hub-Signature-256 HMAC header
            - Format the branch, author and commit messages into one message card
            - Post the message to a Microsoft Teams channel
            - Ignore pushes to branches not in an allow list
API:        REST
            POST /webhooks/github
Tech stack: Node.js, Express, Microsoft Teams Incoming Webhook
```

---

## Example 29

**Intent:**
Our customers keep asking where their package is. I want a chatbot on our website that can look up the order status from Shopify when they give their order number and email.

**Spec:**
```
Type:       Chatbot (order support)
Data model: Conversation(id, session_id, started_at)
            Message(id, conversation_id -> Conversation, role, text, created_at)
Features:   - Ask for the order number and email address
            - Look up the order in Shopify and check that the email matches
            - Reply with order status, carrier and tracking link
            - Answer common questions about returns and shipping times from an FAQ list
            - Hand over to a human by creating a support ticket when it cannot help
API:        REST
            POST /chat/messages
Storage:    PostgreSQL
Tech stack: Node.js, Express, Shopify Admin API, small JavaScript chat widget
```

---

## Example 30

**Intent:**
status page for our saas

**Spec:**
```
Type:       Web application (status page)
Auth:       Admin login for staff
Data model: Component(id, name, status)
            Incident(id, title, status, started_at, resolved_at)
            IncidentUpdate(id, incident_id -> Incident, message, created_at)
            Subscriber(id, email, confirmed)
Features:   - Show the current status of each component
            - Post incidents and timed updates
            - Show 90-day uptime history per component
            - Email subscribers when an incident is opened or resolved
            - Update component status automatically from uptime checks
API:        REST
            GET  /api/status
            POST /api/incidents
            POST /api/incidents/{id}/updates
            POST /api/subscribers
Storage:    PostgreSQL
Tech stack: Python, Django, Celery, Redis
```

---

## Example 31

**Intent:**
rate limiter for our api

**Spec:**
```
Type:       REST API service (rate limiting gateway)
Data model: ClientPlan(client_id, plan, requests_per_minute, burst)
Features:   - Sit in front of the main API as a reverse proxy
            - Identify clients by API key
            - Apply a token bucket limit per client based on their plan
            - Return 429 with a Retry-After header when the limit is hit
            - Add X-RateLimit-Remaining headers to every response
API:        REST
            ANY /* (proxied to the upstream API)
Storage:    Redis (counters), PostgreSQL (client plans)
Tech stack: Go, net/http reverse proxy, Redis
```

---

## Example 32

**Intent:**
bot que responde preguntas frecuentes en telegram para mi tienda, my english not so good, i want answer about horario, envios and pagos

**Spec:**
```
Type:       Bot (Telegram)
Data model: Faq(id, keywords, answer_es, answer_en)
Features:   - Detect the topic of a message (opening hours, shipping, payments) by keywords
            - Answer in Spanish or English depending on the user's language
            - Show a menu with buttons for the main topics
            - Forward unknown questions to the shop owner
            - Let the owner edit answers with an /editar command
Storage:    SQLite
Tech stack: Python, python-telegram-bot
```

---

## Example 33

**Intent:**
when a payment fails in stripe email the customer a link to update their card

**Spec:**
```
Type:       Webhook service (Stripe dunning)
Data model: DunningAttempt(id, stripe_invoice_id, customer_email, attempt_number, emailed_at)
Features:   - Receive invoice.payment_failed webhook events
            - Verify the Stripe webhook signature
            - Create a Stripe customer portal session link for the customer
            - Email the customer a link to update their payment method
            - Send at most one email per invoice attempt
            - Stop emails when invoice.paid arrives
API:        REST
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Ruby, Sinatra, Stripe Ruby SDK, Postmark
```

---

## Example 34

**Intent:**
k8s cluster for our microservices

**Spec:**
```
Type:       Infrastructure setup (Kubernetes)
Features:   - Create a managed Kubernetes cluster with an autoscaling node pool
            - Deploy each microservice with Helm charts
            - Route external traffic through an NGINX ingress controller with TLS from cert-manager
            - Sync secrets from a cloud secrets manager into Kubernetes Secrets
            - Scale pods automatically with the Horizontal Pod Autoscaler
            - Collect metrics and logs with Prometheus and Loki
Tech stack: Kubernetes (GKE), Helm, NGINX Ingress, cert-manager, Terraform
```

---

## Example 35

**Intent:**
i need an api where i can upload a csv and it gives back json

**Spec:**
```
Type:       REST API service (file conversion)
Features:   - Accept CSV uploads up to 10 MB
            - Detect the delimiter and header row automatically
            - Convert rows into a JSON array of objects
            - Infer number and boolean types where possible
            - Return clear errors for malformed rows with line numbers
API:        REST
            POST /convert/csv-to-json
Tech stack: Python, FastAPI, pandas
```

---

## Example 36

**Intent:**
alert me on phone when cpu is over 90% on my server

**Spec:**
```
Type:       Scheduled script (resource alerting)
Features:   - Check CPU usage every 30 seconds
            - Trigger an alert only when CPU stays above 90% for 5 minutes
            - Send a push notification to the phone
            - Include the top 5 processes by CPU in the alert
            - Wait 30 minutes before alerting again for the same problem
Tech stack: Python, psutil, ntfy.sh push notifications, systemd service
```

---

## Example 37

**Intent:**
Hi! Our yoga studio uses Calendly for class bookings and Mailchimp for newsletters. Could new people who book a class be added to our Mailchimp list automatically with a tag for the class they booked?

**Spec:**
```
Type:       Webhook service (Calendly to Mailchimp)
Features:   - Receive Calendly invitee.created webhooks
            - Verify the Calendly webhook signature
            - Add or update the invitee in the Mailchimp audience
            - Tag the contact with the class name
            - Skip people who already unsubscribed in Mailchimp
API:        REST
            POST /webhooks/calendly
Tech stack: Node.js, Express, Calendly API v2, Mailchimp Marketing API
```

---

## Example 38

**Intent:**
sso for our internal tools using google workspace accounts

**Spec:**
```
Type:       Infrastructure setup (single sign-on)
Auth:       Google Workspace OIDC, restricted to the company domain
Features:   - Put an authenticating reverse proxy in front of each internal tool
            - Allow only accounts from the company's Google Workspace domain
            - Limit tools to specific Google groups
            - Pass the user's email to the tools in a request header
            - Expire sessions after 12 hours
Tech stack: oauth2-proxy, NGINX, Google Workspace OIDC, Docker
```

---

## Example 39

**Intent:**
a service that takes webhooks from many places and makes sure they get delivered to our app even if our app is down

**Spec:**
```
Type:       Webhook service (webhook relay)
Data model: InboundWebhook(id, source, headers_json, body, received_at)
            DeliveryAttempt(id, webhook_id -> InboundWebhook, status_code, attempted_at)
Features:   - Accept webhooks from any source and store them before replying 200
            - Forward each webhook to the internal app
            - Retry failed deliveries with exponential backoff for up to 24 hours
            - Move webhooks that keep failing to a dead-letter list
            - Replay any stored webhook from an admin endpoint
API:        REST
            POST /in/{source}
            GET  /admin/webhooks?status=failed
            POST /admin/webhooks/{id}/replay
Storage:    PostgreSQL, SQS (delivery queue)
Tech stack: Go, AWS SQS, PostgreSQL
```

---

## Example 40

**Intent:**
make a discord bot for music

**Spec:**
```
Type:       Bot (Discord)
Features:   - Join the user's voice channel with /play <song or URL>
            - Search for the song and stream its audio
            - Keep a queue per server with /queue, /skip and /remove
            - Pause, resume and set the volume
            - Leave the channel after 5 minutes of no activity
Tech stack: Node.js, discord.js, @discordjs/voice, Lavalink
```

---

## Example 41

**Intent:**
connect our shopify inventory to our warehouse system so stock is the same in both

**Spec:**
```
Type:       Data pipeline (inventory sync)
Data model: SkuMap(id, shopify_inventory_item_id, warehouse_sku)
            SyncLog(id, sku, old_qty, new_qty, source, synced_at)
Features:   - Pull stock levels from the warehouse API every 10 minutes
            - Update Shopify inventory levels for changed SKUs
            - Receive Shopify inventory_levels/update webhooks and push manual changes back
            - Use the warehouse as the source of truth on conflicts
            - Report SKUs that exist in only one system
Storage:    PostgreSQL
Tech stack: Python, Shopify Admin GraphQL API, warehouse REST API, Celery
```

---

## Example 42

**Intent:**
cicd for my react app to netlify

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Install dependencies and run tests on every pull request
            - Build the React app with production settings
            - Deploy a preview site for each pull request
            - Deploy to production when main is updated
            - Comment the preview URL on the pull request
Tech stack: GitHub Actions, Node.js, Netlify CLI
```

---

## Example 43

**Intent:**
we have a bunch of cron jobs on different servers and sometimes they silently stop running. i want a dashboard that shows when each job last ran and screams at us if one misses its schedule

**Spec:**
```
Type:       Web application (cron job monitoring)
Auth:       Team login (email + password)
Data model: Job(id, name, schedule_cron, grace_minutes, ping_token, last_ping_at, status)
            Ping(id, job_id -> Job, kind, received_at)
Features:   - Give each job a unique ping URL to call when it starts and finishes
            - Mark a job as late when no ping arrives within schedule plus grace time
            - Alert by email and Slack when a job is late or reports failure
            - Show all jobs with last run time and status on a dashboard
            - Show run duration history per job
API:        REST
            GET  /ping/{token}
            GET  /ping/{token}/start
            GET  /ping/{token}/fail
            GET  /api/jobs
Storage:    PostgreSQL
Tech stack: Python, Django, Celery beat
```

---

## Example 44

**Intent:**
sms 2 factor auth for login

**Spec:**
```
Type:       REST API service (two-factor authentication)
Auth:       Password login followed by an SMS one-time code
Data model: User(id, email, password_hash, phone, two_factor_enabled)
            OtpCode(id, user_id -> User, code_hash, expires_at, attempts)
Features:   - Send a 6-digit code by SMS after a correct password
            - Expire codes after 5 minutes
            - Lock the code after 5 wrong attempts
            - Limit resend requests to one per 30 seconds
            - Issue a session token only after the code is verified
API:        REST
            POST /login
            POST /login/verify-code
            POST /login/resend-code
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Twilio Verify
```

---

## Example 45

**Intent:**
hey i have a minecraft server and want a discord bot that shows whos online and can start the server

**Spec:**
```
Type:       Bot (Discord)
Features:   - Show online players and player count with /players
            - Show server status in the bot's presence text
            - Start the server with /start for users with an admin role
            - Stop the server safely with /stop after warning players in-game
            - Send a message when the server crashes
Tech stack: Python, discord.py, mcstatus, RCON
```

---

## Example 46

**Intent:**
backup google drive of the company to another cloud

**Spec:**
```
Type:       Scheduled script (cloud backup)
Features:   - Copy all shared drives to a Backblaze B2 bucket every night
            - Copy only new and changed files after the first run
            - Export Google Docs, Sheets and Slides as Office files
            - Keep old file versions for 90 days
            - Send a summary email with the number of files copied and any errors
Storage:    Backblaze B2
Tech stack: rclone, cron, Google Drive API (service account)
```

---

## Example 47

**Intent:**
api that gives exchange rates and converts money

**Spec:**
```
Type:       REST API service
Auth:       API key in the X-API-Key header
Data model: Rate(base, quote, rate, fetched_at)
Features:   - Fetch exchange rates from the European Central Bank feed once an hour
            - Convert an amount from one currency to another
            - Return historical rates for a given date
            - Cache the latest rates in Redis
            - Limit free keys to 1,000 requests per day
API:        REST
            GET  /rates/latest?base={code}
            GET  /rates/{date}
            GET  /convert?from={code}&to={code}&amount={n}
Storage:    PostgreSQL (history), Redis (cache)
Tech stack: Python, FastAPI, httpx
```

---

## Example 48

**Intent:**
automatic dependency updates and security scanning for our repos

**Spec:**
```
Type:       Infrastructure setup (CI security)
Features:   - Open weekly pull requests for outdated dependencies
            - Group minor and patch updates into one pull request
            - Scan dependencies for known vulnerabilities on every pull request
            - Scan Docker images for vulnerabilities before pushing them
            - Fail the build on critical vulnerabilities
Tech stack: GitHub Dependabot, GitHub Actions, Trivy
```

---

## Example 49

**Intent:**
zendesk new ticket -> create jira issue if it's tagged bug

**Spec:**
```
Type:       Webhook service (Zendesk to Jira)
Data model: TicketLink(id, zendesk_ticket_id, jira_issue_key, created_at)
Features:   - Receive Zendesk ticket webhooks
            - Verify the Zendesk webhook signature
            - Create a Jira bug when the ticket has the bug tag
            - Add the Jira issue link back to the ticket as an internal note
            - Avoid creating a second issue for the same ticket
API:        REST
            POST /webhooks/zendesk
Storage:    SQLite
Tech stack: Python, Flask, Zendesk API, Jira Cloud REST API
```

---

## Example 50

**Intent:**
magic link login for my app, no passwords

**Spec:**
```
Type:       REST API service (passwordless authentication)
Auth:       Email magic links with single-use tokens, session cookie after sign-in
Data model: User(id, email, created_at, last_login_at)
            LoginToken(id, user_id -> User, token_hash, expires_at, used_at)
Features:   - Email a one-time sign-in link when a user enters their address
            - Expire links after 15 minutes and allow each link to be used once
            - Create the account automatically on first sign-in
            - Set an HttpOnly, Secure session cookie after the link is clicked
            - Rate limit link requests to 5 per hour per email
API:        REST
            POST /auth/magic-link
            GET  /auth/callback?token={token}
            POST /auth/logout
Storage:    PostgreSQL
Tech stack: TypeScript, Hono, Resend email API
```

---

## Example 51

**Intent:**
i want my discord server to have a ticket system for support

**Spec:**
```
Type:       Bot (Discord)
Data model: Ticket(id, guild_id, channel_id, opener_id, topic, status, created_at, closed_at)
Features:   - Post a panel with an "Open ticket" button
            - Create a private channel visible only to the user and the support role
            - Close a ticket with a button and save a transcript
            - Send the transcript as a file to a log channel
            - Limit each user to one open ticket at a time
Storage:    PostgreSQL
Tech stack: TypeScript, discord.js, Prisma
```

---

## Example 52

**Intent:**
api gateway in front of 3 microservices with auth

**Spec:**
```
Type:       Infrastructure setup (API gateway)
Auth:       JWT validation at the gateway (keys from the identity provider's JWKS)
Features:   - Route /users, /orders and /billing paths to their services
            - Validate JWTs before forwarding requests
            - Apply per-consumer rate limits
            - Add a request ID header for tracing across services
            - Return 503 when an upstream service is unhealthy
Tech stack: Kong Gateway, Docker Compose, JWT plugin, rate-limiting plugin
```

---

## Example 53

**Intent:**
Every time someone stars my GitHub repo I'd like a little celebration message in my personal Telegram.

**Spec:**
```
Type:       Webhook service (GitHub to Telegram)
Features:   - Receive GitHub star (watch) events for the repository
            - Verify the X-Hub-Signature-256 header
            - Send a Telegram message with the user's name and new star count
            - Send a special message at every 100 stars
            - Ignore unstar events
API:        REST
            POST /webhooks/github
Tech stack: Python, FastAPI, Telegram Bot API, deployed on Vercel
```

---

## Example 54

**Intent:**
blue green deploys for our api on aws

**Spec:**
```
Type:       Infrastructure setup (deployment)
Features:   - Run two identical ECS services (blue and green) behind one load balancer
            - Deploy each new version to the idle environment
            - Run smoke tests against the new environment before switching traffic
            - Switch traffic with AWS CodeDeploy and keep the old version for quick rollback
            - Roll back automatically when CloudWatch alarms fire during the deploy
Tech stack: AWS ECS, Application Load Balancer, CodeDeploy, CloudWatch, GitHub Actions
```

---

## Example 55

**Intent:**
wat i need is when stripe subscription canceled remove user from our private discord

**Spec:**
```
Type:       Webhook service (Stripe to Discord)
Data model: Member(id, stripe_customer_id, discord_user_id, subscription_status)
Features:   - Receive customer.subscription.deleted and customer.subscription.updated events
            - Verify the Stripe-Signature header
            - Remove the paid-member role from the linked Discord user
            - Give the role back if the subscription becomes active again
            - Send the user a direct message explaining why access ended
API:        REST
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Node.js, Express, Stripe SDK, discord.js
```

---

## Example 56

**Intent:**
Our support team answers the same 20 questions in Slack all day. Could we have a Slack bot that answers from our internal wiki and says where it found the answer?

**Spec:**
```
Type:       Chatbot (Slack, internal knowledge base)
Data model: WikiChunk(id, page_url, title, text, embedding)
Features:   - Index wiki pages into searchable chunks every night
            - Answer questions when the bot is mentioned or messaged directly
            - Find the most relevant chunks with vector search and generate an answer from them
            - Include links to the wiki pages used in each answer
            - Let users rate answers with thumbs-up or thumbs-down buttons
API:        REST
            POST /slack/events
            POST /slack/interactions
Storage:    PostgreSQL with pgvector
Tech stack: Python, Slack Bolt, pgvector, LLM API, Confluence API
```

---

## Example 57

**Intent:**
nightly backup of my wordpress files and database to dropbox

**Spec:**
```
Type:       Scheduled script (website backup)
Features:   - Export the MySQL database with mysqldump every night
            - Archive the wp-content folder as a tar.gz file
            - Upload both files to a Dropbox folder named by date
            - Keep the last 14 backups and delete older ones
            - Email the site owner if any step fails
Storage:    Dropbox
Tech stack: Bash, mysqldump, Dropbox API (dbxcli), cron
```

---

## Example 58

**Intent:**
a REST API for managing webhooks subscriptions so our customers can get events from our platform

**Spec:**
```
Type:       REST API service (outgoing webhooks)
Auth:       API key per customer account
Data model: Endpoint(id, account_id, url, secret, event_types, active)
            Delivery(id, endpoint_id -> Endpoint, event_type, payload_json, status, attempts, next_retry_at)
Features:   - Let customers register endpoint URLs and choose event types
            - Sign each payload with an HMAC-SHA256 signature and timestamp header
            - Retry failed deliveries with exponential backoff for 3 days
            - Disable endpoints after repeated failures and notify the account owner
            - Show delivery history and allow manual resend
API:        REST
            POST /webhook-endpoints
            GET  /webhook-endpoints
            DELETE /webhook-endpoints/{id}
            GET  /webhook-endpoints/{id}/deliveries
            POST /deliveries/{id}/resend
Storage:    PostgreSQL, Redis (delivery queue)
Tech stack: Elixir, Phoenix, Oban
```

---

## Example 59

**Intent:**
setup sentry for errors

**Spec:**
```
Type:       Infrastructure setup (error tracking)
Features:   - Capture unhandled exceptions from the backend and frontend
            - Upload source maps on each release so stack traces are readable
            - Tag errors with release version and environment
            - Alert a Slack channel when a new issue appears or an issue spikes
            - Filter out personal data like emails and passwords before sending
Tech stack: Sentry, Sentry SDKs, GitHub Actions (release step)
```

---

## Example 60

**Intent:**
telegram bot that sends me crypto prices every morning

**Spec:**
```
Type:       Bot (Telegram)
Data model: Watch(id, chat_id, coin_symbol)
            Settings(chat_id, send_time, currency)
Features:   - Add coins to a watch list with /add btc
            - Send prices and 24h change for watched coins every morning
            - Show current prices on demand with /price
            - Alert when a coin moves more than a chosen percentage
            - Let the user change the time and currency
Storage:    SQLite
Tech stack: Python, python-telegram-bot, CoinGecko API
```

---

## Example 61

**Intent:**
We're a nonprofit and donations come in through Stripe. Our board wants a thank-you email sent automatically, and every donation logged in a Google Sheet for the accountant with a running total.

**Spec:**
```
Type:       Webhook service (donation processing)
Data model: Donation(id, stripe_payment_id, donor_name, donor_email, amount, currency, donated_at)
Features:   - Receive checkout.session.completed events from Stripe
            - Verify the Stripe-Signature header and skip events already processed
            - Send the donor a thank-you email with a tax receipt PDF
            - Append the donation to a Google Sheet with a running total column
            - Mark recurring donations separately from one-time gifts
API:        REST
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Stripe SDK, Google Sheets API, SendGrid, WeasyPrint
```

---

## Example 62

**Intent:**
graphql api for my fitness app with subscriptions for live workout updates

**Spec:**
```
Type:       GraphQL API service
Auth:       Firebase Authentication ID tokens
Data model: User(id, name, email)
            Workout(id, user_id -> User, type, started_at, ended_at)
            WorkoutSample(id, workout_id -> Workout, heart_rate, pace, recorded_at)
Features:   - Query a user's workout history with filters by type and date
            - Record live samples during a workout with a mutation
            - Push live workout updates to followers through GraphQL subscriptions
            - Calculate weekly totals for distance and time
            - Reject requests without a valid Firebase token
API:        GraphQL
            POST /graphql
            WS   /graphql (subscriptions)
Storage:    PostgreSQL, Redis (pub/sub)
Tech stack: TypeScript, GraphQL Yoga, graphql-ws, Prisma
```

---

## Example 63

**Intent:**
disaster recovery plan for our app on azure, if the region dies we need to be back in 1 hour

**Spec:**
```
Type:       Infrastructure setup (disaster recovery)
Features:   - Replicate the Azure SQL database to a secondary region with auto-failover groups
            - Store app files in geo-redundant storage (RA-GRS)
            - Keep a ready-to-scale copy of the App Service in the secondary region
            - Route traffic with Azure Front Door and fail over on health probe failures
            - Define everything in Bicep so it can be recreated quickly
            - Run a failover drill every quarter and record the recovery time
Tech stack: Azure SQL, Azure App Service, Azure Front Door, Azure Storage, Bicep
```

---

## Example 64

**Intent:**
bot to post new reddit posts from a subreddit into discord

**Spec:**
```
Type:       Bot (Discord)
Data model: Feed(id, guild_id, channel_id, subreddit, min_score, last_post_id)
Features:   - Check each configured subreddit every 5 minutes for new posts
            - Post new posts as embeds with title, score and link
            - Skip posts below a minimum score or marked NSFW
            - Add and remove feeds with /feed commands
            - Avoid posting the same post twice
Storage:    SQLite
Tech stack: Python, discord.py, Reddit API (PRAW)
```

---

## Example 65

**Intent:**
my landlord business needs rent reminders sent by whatsapp to tenants 3 days before due

**Spec:**
```
Type:       Scheduled script (rent reminders)
Data model: Tenant(id, name, phone, unit, rent_amount, due_day)
            Reminder(id, tenant_id -> Tenant, month, sent_at, status)
Features:   - Check every morning which tenants have rent due in 3 days
            - Send a WhatsApp template message with amount and due date
            - Send a second reminder on the due day if not marked paid
            - Record each reminder and its delivery status
            - Mark rent as paid from a simple CSV import
Storage:    SQLite
Tech stack: Python, WhatsApp Cloud API (message templates), cron
```

---

## Example 66

**Intent:**
i need my flask app hosted somewhere with https and a database, nothing fancy

**Spec:**
```
Type:       Infrastructure setup (hosting)
Features:   - Run the Flask app with Gunicorn on a small Linux VPS
            - Put Nginx in front as a reverse proxy
            - Get and renew HTTPS certificates automatically with Let's Encrypt
            - Run PostgreSQL on the same server with daily dumps
            - Restart the app automatically with systemd if it crashes
Tech stack: Ubuntu VPS, Gunicorn, Nginx, Certbot, PostgreSQL, systemd
```

---

## Example 67

**Intent:**
api for sending push notifications to our ios and android apps

**Spec:**
```
Type:       REST API service (push notifications)
Auth:       Internal service token
Data model: Device(id, user_id, platform, push_token, last_seen_at)
            PushMessage(id, user_id, title, body, data_json, status, sent_at)
Features:   - Register and update device push tokens
            - Send a notification to all devices of a user
            - Send to iOS through APNs and Android through FCM
            - Remove tokens that the provider reports as invalid
            - Schedule notifications for a later time
API:        REST
            POST /devices
            DELETE /devices/{id}
            POST /push
            GET  /push/{id}
Storage:    PostgreSQL
Tech stack: Kotlin, Ktor, Firebase Admin SDK, Pushy APNs client
```

---

## Example 68

**Intent:**
Woocommerce orders to our accounting in Xero, our bookkeeper is tired of typing it all in

**Spec:**
```
Type:       Webhook service (WooCommerce to Xero)
Data model: OrderSync(id, woo_order_id, xero_invoice_id, status, synced_at)
Features:   - Receive WooCommerce order.completed webhooks
            - Verify the X-WC-Webhook-Signature header
            - Create a paid invoice in Xero with line items, tax and shipping
            - Match or create the customer as a Xero contact
            - Retry when Xero rate limits the request
            - Skip orders already synced
API:        REST
            POST /webhooks/woocommerce
Storage:    MySQL
Tech stack: PHP, Slim Framework, Xero API (OAuth 2.0)
```

---

## Example 69

**Intent:**
health check endpoint for all our services and one page that shows them

**Spec:**
```
Type:       Web application (service health dashboard)
Data model: Service(id, name, health_url, team)
            HealthResult(id, service_id -> Service, status, latency_ms, details_json, checked_at)
Features:   - Poll each service's /health endpoint every 30 seconds
            - Show each service as green, yellow or red
            - Show dependency checks (database, cache) reported by each service
            - Show a 24-hour latency chart per service
            - Notify the owning team when a service turns red
API:        REST
            GET  /api/services
            GET  /api/services/{id}/history
Storage:    PostgreSQL
Tech stack: Go, HTMX, Chart.js
```

---

## Example 70

**Intent:**
verify phone numbers when ppl sign up

**Spec:**
```
Type:       REST API service (phone verification)
Data model: PhoneVerification(id, phone, code_hash, expires_at, attempts, verified_at)
Features:   - Send a 6-digit code by SMS to the given phone number
            - Normalize numbers to E.164 format and reject invalid ones
            - Verify the code within 10 minutes
            - Block numbers after too many attempts
            - Limit sends per IP to prevent SMS pumping fraud
API:        REST
            POST /verify/phone/start
            POST /verify/phone/check
Storage:    Redis (codes with expiry)
Tech stack: Node.js, Express, libphonenumber-js, Vonage SMS API
```

---

## Example 71

**Intent:**
we keep secrets in .env files on the servers and it's a mess

**Spec:**
```
Type:       Infrastructure setup (secrets management)
Features:   - Store all secrets in HashiCorp Vault
            - Give each app its own policy with access only to its secrets
            - Inject secrets into apps at startup with Vault Agent
            - Issue short-lived database credentials from Vault's database engine
            - Log every secret access for auditing
            - Rotate secrets on a schedule
Tech stack: HashiCorp Vault, Vault Agent, PostgreSQL secrets engine, Docker
```

---

## Example 72

**Intent:**
wanna get a msg on telegram whenever my home server reboots or a disk is almost full

**Spec:**
```
Type:       Scheduled script (home server alerts)
Features:   - Send a Telegram message when the server finishes booting
            - Check disk usage of all mounted drives every 10 minutes
            - Alert when any disk is over 90% full
            - Read SMART status of each disk once a day and alert on warnings
            - Avoid repeating the same alert more than once every 6 hours
Tech stack: Bash, smartctl, systemd timer, Telegram Bot API
```

---

## Example 73

**Intent:**
An API for our partners to check product availability and place wholesale orders. They should each have their own price list.

**Spec:**
```
Type:       REST API service (B2B partner API)
Auth:       OAuth 2.0 client credentials per partner
Data model: Partner(id, name, price_list_id -> PriceList)
            PriceList(id, name)
            Price(price_list_id -> PriceList, sku, unit_price)
            WholesaleOrder(id, partner_id -> Partner, status, total, created_at)
Features:   - Return product stock levels by SKU
            - Return prices from the partner's own price list
            - Place wholesale orders with a minimum order quantity check
            - Accept an Idempotency-Key header on order creation
            - Notify partners of order status changes by webhook
API:        REST
            GET  /products?sku={sku}
            GET  /prices
            POST /orders
            GET  /orders/{id}
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Entity Framework Core
```

---

## Example 74

**Intent:**
a slack command to deploy our app

**Spec:**
```
Type:       Bot (Slack ChatOps)
Data model: Deployment(id, service, version, environment, requested_by, status, started_at)
Features:   - Start a deploy with /deploy <service> <version> <environment>
            - Allow production deploys only for users in a deployers group
            - Trigger the CI pipeline and post progress updates in the thread
            - Roll back to the previous version with /rollback <service>
            - Keep a history of deploys with /deploys
API:        REST
            POST /slack/commands
            POST /ci/callback
Storage:    PostgreSQL
Tech stack: Go, Slack API, GitHub Actions workflow_dispatch
```

---

## Example 75

**Intent:**
Im a solo dev and my side project database got corrupted, lost 2 weeks of data. never again. it is mysql on digitalocean. please something simple and reliable

**Spec:**
```
Type:       Scheduled script (database backup)
Features:   - Dump the MySQL database every 6 hours with mysqldump --single-transaction
            - Compress the dump and upload it to DigitalOcean Spaces
            - Keep 7 daily and 4 weekly backups and delete the rest
            - Verify each upload by checking file size and checksum
            - Send a ping to a dead-man's-switch monitor after each successful run
            - Restore a backup to a test database with one command
Storage:    DigitalOcean Spaces (S3-compatible)
Tech stack: Bash, mysqldump, s3cmd, cron, Healthchecks.io
```

---

## Example 76

**Intent:**
log every api request and response time to a database so we can see slow endpoints

**Spec:**
```
Type:       REST API service (request logging middleware)
Data model: RequestLog(id, method, path, status_code, duration_ms, user_id, created_at)
Features:   - Record method, route, status and duration for each request
            - Write logs in batches in the background to keep requests fast
            - Show the slowest endpoints by 95th percentile response time
            - Show error rate per endpoint for the last 24 hours
            - Delete logs older than 30 days
API:        REST
            GET  /admin/stats/slow-endpoints
            GET  /admin/stats/errors
Storage:    ClickHouse
Tech stack: Node.js, Express middleware, ClickHouse
```

---

## Example 77

**Intent:**
bot whatsapp for my clinic, patient can see appointment and cancel. we are in brazil so portuguese

**Spec:**
```
Type:       Bot (WhatsApp)
Data model: Patient(id, name, phone, cpf)
            Appointment(id, patient_id -> Patient, doctor, starts_at, status)
Features:   - Answer patients in Portuguese
            - Identify the patient by phone number
            - Show the patient's next appointments
            - Cancel an appointment after the patient confirms
            - Send a reminder message the day before each appointment
API:        REST
            POST /webhooks/whatsapp
Storage:    PostgreSQL
Tech stack: Node.js, Express, WhatsApp Cloud API
```

---

## Example 78

**Intent:**
ansible to set up new ubuntu servers the same way every time

**Spec:**
```
Type:       Infrastructure setup (configuration management)
Features:   - Create admin users and install their SSH keys
            - Disable password and root SSH login
            - Enable the UFW firewall with only needed ports open
            - Install security updates automatically with unattended-upgrades
            - Install Docker, fail2ban and the monitoring agent
            - Run the same playbook again safely without changing anything (idempotent)
Tech stack: Ansible, Ubuntu, UFW, fail2ban
```

---

## Example 79

**Intent:**
Could you design a backend that handles subscriptions for our SaaS—monthly and yearly plans, free trial, upgrades and downgrades—using Stripe Billing?

**Spec:**
```
Type:       REST API service (subscription billing)
Auth:       JWT from the main app
Data model: Account(id, name, stripe_customer_id, plan, subscription_status, trial_ends_at)
            BillingEvent(id, account_id -> Account, stripe_event_id, type, received_at)
Features:   - Start a 14-day free trial without a card
            - Create Stripe Checkout sessions for monthly and yearly plans
            - Change plans with proration on upgrade and at period end on downgrade
            - Keep subscription status in sync from Stripe webhooks with signature checks
            - Open the Stripe customer portal for invoices and card updates
API:        REST
            POST /billing/checkout
            POST /billing/change-plan
            POST /billing/portal
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, Django, dj-stripe, Stripe Billing
```

---

## Example 80

**Intent:**
uptime robot but self hosted

**Spec:**
```
Type:       Web application (self-hosted uptime monitor)
Auth:       Single admin login with optional TOTP
Data model: Monitor(id, name, type, target, interval_seconds, active)
            Heartbeat(id, monitor_id -> Monitor, up, latency_ms, message, checked_at)
            NotificationChannel(id, type, config_json)
Features:   - Check HTTP, TCP port, ping and DNS targets on their own intervals
            - Show up/down status and response time charts
            - Send alerts to email, Slack, Telegram or Discord
            - Publish a public status page for selected monitors
            - Pause monitors during maintenance windows
API:        REST
            GET  /api/monitors
            POST /api/monitors
            GET  /api/monitors/{id}/heartbeats
Storage:    SQLite
Tech stack: Node.js, Vue, Socket.IO, Docker
```

---

## Example 81

**Intent:**
send a weekly summary of our stripe revenue to slack every monday

**Spec:**
```
Type:       Scheduled script (revenue report)
Features:   - Run every Monday at 08:00
            - Fetch last week's charges, refunds and new subscriptions from Stripe
            - Calculate gross revenue, refunds, net revenue and MRR change
            - Compare each number to the previous week
            - Post a formatted message to the #finance Slack channel
Tech stack: Python, Stripe SDK, Slack Web API, GitHub Actions schedule
```

---

## Example 82

**Intent:**
tg bot for my english class, sends a new word every day and quizzes the students on friday

**Spec:**
```
Type:       Bot (Telegram)
Data model: Word(id, word, meaning, example, sent_on)
            Student(id, chat_id, name)
            QuizAnswer(id, student_id -> Student, word_id -> Word, correct, answered_at)
Features:   - Send a word of the day with meaning and example sentence to the group
            - Run a Friday quiz with multiple-choice buttons for the week's words
            - Score each student's answers
            - Post a weekly leaderboard
            - Let the teacher add words with /addword
Storage:    SQLite
Tech stack: Python, aiogram, APScheduler
```

---

## Example 83

**Intent:**
webhook for typeform responses to go to notion database

**Spec:**
```
Type:       Webhook service (Typeform to Notion)
Features:   - Receive Typeform form_response webhooks
            - Verify the Typeform-Signature header
            - Map each answer to a matching Notion database property
            - Create a new page in the Notion database for each response
            - Retry when the Notion API returns a rate limit error
API:        REST
            POST /webhooks/typeform
Tech stack: Node.js, Cloudflare Workers, Notion API
```

---

## Example 84

**Intent:**
we want to move off heroku to something cheaper, we have a rails app, postgres, redis and sidekiq

**Spec:**
```
Type:       Infrastructure setup (hosting migration)
Features:   - Package the Rails app, Sidekiq worker and assets in one Docker image
            - Run web and worker processes on a VPS with Kamal
            - Move PostgreSQL to a managed database with daily backups
            - Run Redis for Sidekiq on the same private network
            - Set up zero-downtime deploys with health checks
            - Copy data from Heroku Postgres with pg_dump and pg_restore during a short maintenance window
Tech stack: Ruby on Rails, Kamal, Docker, Hetzner Cloud, managed PostgreSQL, Redis
```

---

## Example 85

**Intent:**
api key management for our public api

**Spec:**
```
Type:       REST API service (API key management)
Auth:       Dashboard login for developers; API keys for API calls
Data model: Developer(id, email, password_hash)
            ApiKey(id, developer_id -> Developer, prefix, key_hash, name, scopes, last_used_at, revoked_at)
Features:   - Create API keys and show the full key only once
            - Store only a hash of each key and look keys up by prefix
            - Give each key a set of scopes
            - Revoke keys and roll keys with a 24-hour overlap
            - Track last used time and request counts per key
API:        REST
            POST /keys
            GET  /keys
            POST /keys/{id}/roll
            DELETE /keys/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, argon2
```

---

## Example 86

**Intent:**
hello, we are logistic company. want that drivers send photo of delivery in telegram and it save to our system with the order number

**Spec:**
```
Type:       Bot (Telegram)
Data model: Driver(id, telegram_user_id, name, active)
            DeliveryProof(id, order_number, driver_id -> Driver, photo_url, latitude, longitude, received_at)
Features:   - Ask the driver for the order number, then the delivery photo
            - Ask for the driver's location along with the photo
            - Upload photos to object storage
            - Send the proof to the company's order system through its API
            - Allow only registered drivers to use the bot
Storage:    PostgreSQL, Amazon S3 (photos)
Tech stack: Python, aiogram, boto3
```

---

## Example 87

**Intent:**
cloudflare in front of my site for ddos protection and caching

**Spec:**
```
Type:       Infrastructure setup (CDN and security)
Features:   - Move DNS to Cloudflare and proxy the site's traffic
            - Cache static assets at the edge with long cache times
            - Turn on the web application firewall with managed rules
            - Rate limit the login page
            - Force HTTPS with full (strict) TLS to the origin
            - Allow traffic to the origin only from Cloudflare IP ranges
Tech stack: Cloudflare (DNS, CDN, WAF), Terraform Cloudflare provider
```

---

## Example 88

**Intent:**
pager duty style on-call rotation that calls the person on call when production breaks

**Spec:**
```
Type:       Web application (on-call alerting)
Auth:       Team login (email + password)
Data model: Engineer(id, name, phone, email)
            Rotation(id, name, handoff_day, handoff_time)
            Shift(id, rotation_id -> Rotation, engineer_id -> Engineer, starts_at, ends_at)
            Alert(id, source, title, status, acknowledged_by, created_at)
Features:   - Receive alerts from monitoring tools through a webhook
            - Find who is on call and phone them with a voice call
            - Escalate to the backup person if not acknowledged in 10 minutes
            - Acknowledge or resolve alerts by pressing a key on the call or in the web app
            - Show the rotation calendar and allow shift swaps
API:        REST
            POST /alerts
            POST /alerts/{id}/ack
            GET  /oncall/now
Storage:    PostgreSQL
Tech stack: Python, Django, Celery, Twilio Voice
```

---

## Example 89

**Intent:**
simple oauth login with github for my web app backend

**Spec:**
```
Type:       REST API service (OAuth login)
Auth:       GitHub OAuth 2.0 (authorization code flow with state parameter)
Data model: User(id, github_id, username, avatar_url, created_at)
Features:   - Redirect users to GitHub to sign in
            - Exchange the code for an access token and check the state value
            - Create or update the user from their GitHub profile
            - Start a signed session cookie
            - Log the user out
API:        REST
            GET  /auth/github
            GET  /auth/github/callback
            POST /auth/logout
            GET  /me
Storage:    SQLite
Tech stack: Go, golang.org/x/oauth2, gorilla/sessions
```

---

## Example 90

**Intent:**
notifcation when someone books on my airbnb listings

**Spec:**
```
Type:       Scheduled script (booking notifications)
Data model: Booking(id, listing, uid, guest_name, check_in, check_out, notified_at)
Features:   - Download each listing's iCal calendar every 15 minutes
            - Detect new and cancelled bookings by comparing with saved events
            - Send a push notification with listing and dates
            - Send a cleaning reminder the morning of each check-out
            - Warn about double bookings across listings
Storage:    SQLite
Tech stack: Python, icalendar, Pushover API, cron
```

---

## Example 91

**Intent:**
ci pipeline for a go project with docker image to github container registry

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Run go vet, golangci-lint and go test with race detection on every push
            - Build multi-architecture images (amd64 and arm64) with Docker Buildx
            - Push images to GitHub Container Registry tagged with the commit SHA
            - Tag images with the version number on git tags
            - Sign images with cosign
Tech stack: GitHub Actions, Go, Docker Buildx, GHCR, cosign
```

---

## Example 92

**Intent:**
a little rest api to store and fetch feature flags for our apps

**Spec:**
```
Type:       REST API service (feature flags)
Auth:       Admin token for writes; public read with an environment key
Data model: Flag(id, key, description, enabled, rollout_percent)
            FlagRule(id, flag_id -> Flag, attribute, operator, value)
Features:   - Create, update and delete flags
            - Evaluate a flag for a user with percentage rollout using a stable hash of the user ID
            - Target users by attributes like country or plan
            - Return all flags for an environment in one call
            - Keep an audit log of flag changes
API:        REST
            GET  /flags?env={key}
            POST /flags
            PATCH /flags/{key}
            POST /flags/{key}/evaluate
Storage:    PostgreSQL, Redis (cache)
Tech stack: Rust, Axum, sqlx
```

---

## Example 93

**Intent:**
abandoned cart emails for shopify

**Spec:**
```
Type:       Webhook service (Shopify abandoned checkout)
Data model: Checkout(id, shopify_checkout_id, email, cart_total, recovery_url, created_at, completed_at)
            RecoveryEmail(id, checkout_id -> Checkout, step, sent_at)
Features:   - Receive checkouts/create and checkouts/update webhooks with HMAC verification
            - Wait 1 hour, then email the customer a link back to their cart
            - Send a second email after 24 hours with a discount code
            - Stop the sequence when an orders/create webhook shows the checkout was completed
            - Respect customers who did not accept marketing emails
API:        REST
            POST /webhooks/shopify/checkouts
            POST /webhooks/shopify/orders
Storage:    PostgreSQL, Redis (delayed jobs)
Tech stack: Node.js, Express, BullMQ, Postmark
```

---

## Example 94

**Intent:**
an IVR phone line for my plumbing business: press 1 for emergency, 2 to book, and it should text me the caller's number

**Spec:**
```
Type:       Webhook service (voice IVR)
Data model: Call(id, caller_number, choice, recording_url, created_at)
Features:   - Answer incoming calls with a greeting and a keypad menu
            - Forward emergency calls (press 1) to the owner's mobile
            - Record a voicemail for booking requests (press 2)
            - Text the owner the caller's number and choice after each call
            - Play a closed message outside business hours, except for emergencies
API:        REST
            POST /voice/incoming
            POST /voice/menu
            POST /voice/recording-done
Storage:    SQLite
Tech stack: Python, Flask, Twilio Voice (TwiML), Twilio SMS
```

---

## Example 95

**Intent:**
moderation bot for discord that deletes spam links and warns people

**Spec:**
```
Type:       Bot (Discord)
Data model: Warning(id, guild_id, user_id, reason, moderator_id, created_at)
            GuildConfig(guild_id, log_channel_id, allowed_domains, max_warnings)
Features:   - Delete messages with links not on the allowed domain list
            - Delete repeated messages sent within a few seconds (spam)
            - Warn the user and record the warning
            - Time out users automatically after reaching the warning limit
            - Log every action to a moderator log channel
            - Show a user's warnings with /warnings @user
Storage:    PostgreSQL
Tech stack: Python, discord.py, asyncpg
```

---

## Example 96

**Intent:**
rss feed to slack channel

**Spec:**
```
Type:       Scheduled script (RSS to Slack)
Data model: SeenItem(feed_url, item_guid, seen_at)
Features:   - Read a list of RSS and Atom feeds from a config file
            - Check each feed every 15 minutes
            - Post new items with title and link to the matching Slack channel
            - Remember posted items so nothing is posted twice
            - Skip feeds that fail and report them once a day
Storage:    SQLite
Tech stack: Python, feedparser, Slack Incoming Webhooks, cron
```

---

## Example 97

**Intent:**
When a deal is marked won in Pipedrive, I want an invoice created in Stripe and sent to the client automatically.

**Spec:**
```
Type:       Webhook service (Pipedrive to Stripe)
Data model: DealInvoice(id, pipedrive_deal_id, stripe_invoice_id, amount, created_at)
Features:   - Receive Pipedrive deal update webhooks with basic auth
            - Act only when the deal status changes to won
            - Find or create the Stripe customer from the deal's contact
            - Create invoice items from the deal's products and send the invoice
            - Write the invoice link back to a custom field on the deal
            - Never create two invoices for the same deal
API:        REST
            POST /webhooks/pipedrive
Storage:    PostgreSQL
Tech stack: Node.js, Express, Pipedrive API, Stripe SDK
```

---

## Example 98

**Intent:**
i want tracing across my microservices to see where requests are slow

**Spec:**
```
Type:       Infrastructure setup (distributed tracing)
Features:   - Add OpenTelemetry SDKs to each service to create spans for requests
            - Pass trace context between services in HTTP headers
            - Send spans to an OpenTelemetry Collector
            - Store traces in Jaeger and search them by service and duration
            - Sample 10% of normal requests and 100% of errors
Tech stack: OpenTelemetry, OpenTelemetry Collector, Jaeger, Docker Compose
```

---

## Example 99

**Intent:**
backend for a url shortener with click stats

**Spec:**
```
Type:       REST API service
Auth:       API key for creating links
Data model: Link(id, code, target_url, owner_key_id, created_at, expires_at)
            Click(id, link_id -> Link, country, referrer, user_agent, clicked_at)
Features:   - Create short codes for long URLs, with optional custom codes
            - Redirect short codes with a 302
            - Record clicks with country, referrer and device
            - Return click counts per day for a link
            - Block links to known malware domains
API:        REST
            POST /links
            GET  /{code}
            GET  /links/{code}/stats
Storage:    PostgreSQL, Redis (code lookups)
Tech stack: Go, Fiber, Redis, MaxMind GeoLite2
```

---

## Example 100

**Intent:**
yo can u make a bot that posts the daily wordle results from our group chat into a leaderboard. its whatsapp

**Spec:**
```
Type:       Bot (WhatsApp)
Data model: Player(id, phone, name)
            Score(id, player_id -> Player, puzzle_number, guesses, posted_at)
Features:   - Read shared Wordle result messages from group members
            - Parse the puzzle number and number of guesses
            - Ignore duplicate results for the same puzzle
            - Post a daily leaderboard at 21:00
            - Post a weekly winner every Sunday
API:        REST
            POST /webhooks/whatsapp
Storage:    SQLite
Tech stack: Node.js, whatsapp-web.js
```

---

## Example 101

**Intent:**
auto label github issues and pull requests based on files changed and keywords

**Spec:**
```
Type:       Webhook service (GitHub App)
Features:   - Receive issues and pull_request events as a GitHub App
            - Verify webhook signatures
            - Label pull requests by changed paths using a config file in the repo
            - Label issues by keywords in the title and body
            - Add a needs-triage label to new issues without matches
API:        REST
            POST /api/github/webhooks
Tech stack: TypeScript, Probot, GitHub App
```

---

## Example 102

**Intent:**
i got a raspberry pi running pihole and home assistant, i want it backed up to my nas every week

**Spec:**
```
Type:       Scheduled script (home backup)
Features:   - Stop writes briefly and create a Home Assistant backup through its API
            - Export the Pi-hole configuration with its teleporter command
            - Copy both backups to an NFS share on the NAS with rsync
            - Keep the last 8 weekly backups
            - Send a notification through Home Assistant when the backup finishes or fails
Tech stack: Bash, rsync, Home Assistant API, systemd timer
```

---

## Example 103

**Intent:**
password reset flow for our api

**Spec:**
```
Type:       REST API service (password reset)
Data model: User(id, email, password_hash)
            ResetToken(id, user_id -> User, token_hash, expires_at, used_at)
Features:   - Email a reset link with a random single-use token
            - Return the same response whether or not the email exists
            - Expire tokens after 30 minutes
            - Set the new password after checking strength rules
            - Log the user out of all other sessions after a reset
API:        REST
            POST /password/forgot
            POST /password/reset
Storage:    PostgreSQL
Tech stack: Ruby, Rails API, Action Mailer
```

---

## Example 104

**Intent:**
I have about 40 customers on monthly retainers and I invoice them by hand every month from a Word template. Could something create the invoices in Stripe on the 1st, email them, and tell me in Slack who hasn't paid after a week?

**Spec:**
```
Type:       Scheduled script (retainer billing)
Data model: Client(id, name, email, monthly_amount, stripe_customer_id)
            InvoiceRecord(id, client_id -> Client, stripe_invoice_id, month, status)
Features:   - Create and finalize a Stripe invoice for each client on the 1st of the month
            - Let Stripe email the invoice with a payment link
            - Update invoice status from Stripe invoice.paid webhooks
            - Post a list of unpaid invoices to Slack 7 days after sending
            - Skip clients marked as paused
Storage:    PostgreSQL
Tech stack: Python, Stripe SDK, Slack Web API, cron
```

---

## Example 105

**Intent:**
graphql gateway combining our users service and orders service

**Spec:**
```
Type:       GraphQL API service (federated gateway)
Auth:       JWT validated at the gateway and passed to subgraphs
Features:   - Combine the users and orders subgraphs into one schema
            - Resolve the orders field on User from the orders service
            - Forward the user's identity to each subgraph in a header
            - Cache query plans for repeated operations
            - Report per-field timing to see slow resolvers
API:        GraphQL
            POST /graphql
Tech stack: Apollo Federation, Apollo Router, Node.js subgraphs
```

---

## Example 106

**Intent:**
slack approval bot for expense requests

**Spec:**
```
Type:       Bot (Slack)
Data model: Expense(id, requester_id, amount, description, receipt_url, status, approver_id, decided_at)
Features:   - Open a form with /expense to enter amount, description and a receipt
            - Send the request to the requester's manager with Approve and Reject buttons
            - Require a second approval from finance above 500 EUR
            - Notify the requester of the decision in a direct message
            - Export approved expenses to CSV each month
API:        REST
            POST /slack/commands
            POST /slack/interactions
Storage:    PostgreSQL
Tech stack: Node.js, Slack Bolt, Block Kit
```

---

## Example 107

**Intent:**
cost alert when our aws bill gets too high

**Spec:**
```
Type:       Infrastructure setup (cloud cost alerts)
Features:   - Create a monthly AWS Budget with alerts at 50%, 80% and 100%
            - Add a forecast alert when the month is predicted to go over budget
            - Turn on Cost Anomaly Detection for each service
            - Send alerts to an SNS topic forwarded to email and Slack
            - Tag resources by project so costs can be split
Tech stack: AWS Budgets, Cost Anomaly Detection, SNS, AWS Chatbot, Terraform
```

---

## Example 108

**Intent:**
webhook reciever that saves everything that comes in so i can debug integrations

**Spec:**
```
Type:       Webhook service (request inspector)
Data model: Bin(id, slug, created_at)
            CapturedRequest(id, bin_id -> Bin, method, headers_json, query, body, ip, received_at)
Features:   - Create a bin with a random URL
            - Capture any request sent to the bin URL
            - Show captured requests live in a web page
            - Replay a captured request to another URL
            - Delete bins and their requests after 7 days
API:        REST
            POST /bins
            ANY  /b/{slug}
            GET  /bins/{slug}/requests
Storage:    SQLite
Tech stack: Node.js, Fastify, Server-Sent Events
```

---

## Example 109

**Intent:**
restic backups of our office file server to backblaze

**Spec:**
```
Type:       Scheduled script (file server backup)
Features:   - Back up the shared folders every night with restic
            - Encrypt backups with a repository password stored in a secrets file
            - Keep 7 daily, 4 weekly and 12 monthly snapshots
            - Check repository integrity every Sunday
            - Email the office manager a short report after each run
Storage:    Backblaze B2
Tech stack: restic, Backblaze B2, systemd timers, msmtp
```

---

## Example 110

**Intent:**
we need saml sso for our enterprise customers into our saas

**Spec:**
```
Type:       REST API service (SAML single sign-on)
Auth:       SAML 2.0 SP-initiated SSO per customer organization
Data model: Organization(id, name, email_domain, idp_entity_id, idp_sso_url, idp_certificate)
            User(id, org_id -> Organization, email, name)
Features:   - Let organization admins upload their identity provider metadata
            - Route users to their company's identity provider by email domain
            - Validate signed SAML responses and assertions
            - Create users on first login (just-in-time provisioning)
            - Publish service provider metadata for each organization
API:        REST
            GET  /sso/{org}/login
            POST /sso/{org}/acs
            GET  /sso/{org}/metadata
Storage:    PostgreSQL
Tech stack: Python, Django, python3-saml
```

---

## Example 111

**Intent:**
telegram bot that downloads instagram reels when i send the link

**Spec:**
```
Type:       Bot (Telegram)
Features:   - Accept Instagram reel links sent in a chat
            - Download the video and send it back as a Telegram video
            - Reject links that are private or invalid with a clear message
            - Limit each user to 20 downloads per day
            - Delete temporary files after sending
Tech stack: Python, aiogram, yt-dlp
```

---

## Example 112

**Intent:**
the warehouse guys use a google sheet for incoming stock and i want it pushed into our odoo every hour

**Spec:**
```
Type:       Scheduled script (Google Sheets to Odoo)
Data model: ImportedRow(sheet_row_id, odoo_picking_id, imported_at)
Features:   - Read new rows from the incoming stock sheet every hour
            - Validate product codes and quantities
            - Create receipts in Odoo for valid rows through XML-RPC
            - Write "imported" or an error message back into a status column
            - Skip rows already imported
Storage:    SQLite
Tech stack: Python, gspread, Odoo XML-RPC API, cron
```

---

## Example 113

**Intent:**
Hi team, need service to receive payments from M-Pesa for our school fees system in Kenya, parents pay with paybill and we must know which student paid.

**Spec:**
```
Type:       Webhook service (M-Pesa payments)
Data model: Student(id, admission_number, name, balance)
            MpesaPayment(id, trans_id, msisdn, amount, bill_ref_number, student_id -> Student, received_at)
Features:   - Register validation and confirmation URLs with the Daraja C2B API
            - Reject payments whose account number does not match a student
            - Record confirmed payments and reduce the student's balance
            - Ignore repeated callbacks with the same transaction ID
            - Send the parent an SMS receipt with the new balance
API:        REST
            POST /mpesa/validation
            POST /mpesa/confirmation
Storage:    PostgreSQL
Tech stack: Node.js, Express, Safaricom Daraja API, Africa's Talking SMS
```

---

## Example 114

**Intent:**
synthetic monitoring for our checkout flow

**Spec:**
```
Type:       Scheduled script (synthetic monitoring)
Features:   - Run a headless browser script every 10 minutes that adds a product and goes through checkout
            - Use a test card in the payment provider's test mode
            - Save a screenshot and trace when a step fails
            - Alert the on-call channel on two failures in a row
            - Record how long each step takes
Tech stack: Playwright, Node.js, GitHub Actions schedule, Slack Incoming Webhooks
```

---

## Example 115

**Intent:**
docker compose setup for local dev with postgres redis and our api

**Spec:**
```
Type:       Infrastructure setup (local development)
Features:   - Start the API, PostgreSQL and Redis with one docker compose up
            - Mount the source folder so code changes reload automatically
            - Seed the database with sample data on first start
            - Wait for the database health check before starting the API
            - Keep database data in a named volume
Tech stack: Docker Compose, PostgreSQL, Redis
```

---

## Example 116

**Intent:**
crm sync between our app users and salesforce

**Spec:**
```
Type:       Data pipeline (app to Salesforce sync)
Data model: SyncState(user_id, salesforce_contact_id, last_synced_at, hash)
Features:   - Send new sign-ups to Salesforce as leads
            - Update the contact when plan or usage changes
            - Send only records whose data changed since the last sync
            - Use the Salesforce Bulk API for large updates
            - Respect API limits and retry later when they are reached
Storage:    PostgreSQL
Tech stack: Python, simple-salesforce, Celery, Redis
```

---

## Example 117

**Intent:**
simple bot in line app for my bakery to show menu and take preorders. customers mostly in japan

**Spec:**
```
Type:       Bot (LINE)
Data model: MenuItem(id, name_ja, price, available)
            Preorder(id, line_user_id, items_json, pickup_time, status)
Features:   - Show today's menu as a carousel with photos and prices in Japanese
            - Let customers choose items and a pickup time
            - Confirm the preorder and send a summary
            - Notify the bakery staff of each new preorder
            - Send a pickup reminder 1 hour before
API:        REST
            POST /line/webhook
Storage:    Firestore
Tech stack: Node.js, LINE Messaging API, Firebase Cloud Functions
```

---

## Example 118

**Intent:**
log alerts if someone logs in to our servers as root

**Spec:**
```
Type:       Infrastructure setup (security alerting)
Features:   - Forward auth logs from every server to a central log system
            - Detect successful root logins and failed SSH login bursts
            - Alert the security channel immediately on root logins
            - Block IPs with too many failed attempts with fail2ban
            - Keep auth logs for 1 year
Tech stack: rsyslog, Graylog, fail2ban, Slack alerts
```

---

## Example 119

**Intent:**
twilio sms opt in / opt out list for our promos

**Spec:**
```
Type:       REST API service (SMS marketing list)
Auth:       Admin API key
Data model: Subscriber(id, phone, status, opted_in_at, opted_out_at)
            Campaign(id, message, scheduled_at, sent_count)
Features:   - Add subscribers when they text JOIN to the number
            - Remove subscribers who text STOP and confirm the opt-out
            - Send a campaign to all active subscribers in batches
            - Only send between 9:00 and 20:00 in the subscriber's time zone
            - Track delivery status from Twilio callbacks
API:        REST
            POST /sms/inbound
            POST /sms/status
            POST /campaigns
Storage:    PostgreSQL
Tech stack: Python, Flask, Twilio Messaging Service
```

---

## Example 120

**Intent:**
automatic release notes and version bump when we merge to main

**Spec:**
```
Type:       Infrastructure setup (release automation)
Features:   - Read conventional commit messages since the last release
            - Pick the next version number (major, minor or patch)
            - Generate a changelog and create a GitHub release
            - Publish the package to npm
            - Post the release notes to Slack
Tech stack: GitHub Actions, semantic-release, npm
```

---

## Example 121

**Intent:**
a mastodon bot that posts the weather for my city every morning

**Spec:**
```
Type:       Bot (Mastodon)
Features:   - Fetch the day's forecast every morning at 07:00
            - Post high and low temperature, rain chance and wind
            - Add a warning emoji for storms or heat alerts
            - Reply to mentions asking "now" with the current weather
Tech stack: Python, Mastodon.py, Open-Meteo API, cron
```

---

## Example 122

**Intent:**
webhook that resizes images when uploaded to s3

**Spec:**
```
Type:       Webhook service (S3 event processing)
Features:   - Trigger on new uploads to the originals/ prefix of the bucket
            - Create thumbnail, medium and large WebP versions
            - Save resized images under the resized/ prefix
            - Skip files that are not images
            - Send failures to a dead-letter queue
Storage:    Amazon S3
Tech stack: AWS Lambda, Python, Pillow, S3 event notifications, SQS
```

---

## Example 123

**Intent:**
For our gym, members check in with a QR code at the door. I want a backend that checks if their membership is valid and opens the door, and also sends them a reminder email when it is about to expire.

**Spec:**
```
Type:       REST API service (access control)
Auth:       Device key for door scanners; admin login for staff
Data model: Member(id, name, email, qr_token, membership_ends_at, active)
            CheckIn(id, member_id -> Member, door_id, allowed, scanned_at)
Features:   - Validate a scanned QR token and the member's end date
            - Tell the door controller to unlock on success
            - Log every check-in attempt
            - Email members 7 days before their membership ends
            - Let staff renew or freeze memberships
API:        REST
            POST /doors/{id}/scan
            GET  /members/{id}
            POST /members/{id}/renew
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, MQTT (door controllers), SendGrid
```

---

## Example 124

**Intent:**
kubectl backups of our cluster in case someone deletes stuff

**Spec:**
```
Type:       Infrastructure setup (Kubernetes backup)
Features:   - Back up all Kubernetes resources and persistent volumes with Velero
            - Run a full backup every night and keep 30 days
            - Store backups in an S3 bucket in another region
            - Restore a single namespace on demand
            - Alert when a scheduled backup fails
Tech stack: Velero, Kubernetes, Amazon S3, Prometheus alert rules
```

---

## Example 125

**Intent:**
i want a bot for twitch chat that has commands and counts points for watching

**Spec:**
```
Type:       Bot (Twitch)
Data model: Viewer(id, channel, username, points, watch_minutes)
            Command(id, channel, trigger, response)
Features:   - Give viewers points for every 10 minutes they watch
            - Show points with !points
            - Let the streamer add custom commands like !discord
            - Run a !gamble command with a cooldown
            - Show the top 10 viewers with !leaderboard
Storage:    SQLite
Tech stack: Node.js, tmi.js, Twitch Helix API
```

---

## Example 126

**Intent:**
microsoft teams bot that answers hr questions about holidays and policies

**Spec:**
```
Type:       Chatbot (Microsoft Teams)
Auth:       Microsoft Entra ID (single sign-on in Teams)
Data model: PolicyDoc(id, title, text, updated_at)
Features:   - Answer questions about leave, holidays and policies from HR documents
            - Show the user's remaining holiday days from the HR system
            - Link to the source policy in each answer
            - Hand the question to an HR person when unsure
API:        REST
            POST /api/messages
Storage:    Azure AI Search
Tech stack: C#, Bot Framework SDK, Azure Bot Service, Azure OpenAI
```

---

## Example 127

**Intent:**
heartbeat monitor for my iot devices, alert if one stops sending data

**Spec:**
```
Type:       Scheduled script (device heartbeat monitoring)
Data model: Device(id, name, location, last_seen_at, status)
Features:   - Update each device's last seen time when its MQTT message arrives
            - Check every 5 minutes for devices silent longer than 15 minutes
            - Mark them offline and send an email alert
            - Send a recovery message when they come back
            - Show a list of offline devices
Storage:    PostgreSQL
Tech stack: Python, paho-mqtt, Mosquitto, cron
```

---

## Example 128

**Intent:**
eu customers need gdpr data export and delete endpoints in our backend

**Spec:**
```
Type:       REST API service (GDPR data requests)
Auth:       User session plus re-authentication for deletion
Data model: DataRequest(id, user_id, type, status, requested_at, completed_at, download_url)
Features:   - Collect all of a user's data from each service into a JSON export
            - Email a time-limited download link when the export is ready
            - Delete the account and personal data after a 14-day grace period
            - Ask connected services to delete data through internal webhooks
            - Keep an audit record of each completed request
API:        REST
            POST /privacy/export
            POST /privacy/delete
            GET  /privacy/requests/{id}
Storage:    PostgreSQL, S3 (exports)
Tech stack: Java, Spring Boot, Spring Batch
```

---

## Example 129

**Intent:**
ping me on discord when my github actions build fails

**Spec:**
```
Type:       Webhook service (GitHub to Discord)
Features:   - Receive workflow_run events from GitHub
            - Verify the webhook signature
            - Post only failed runs on the main branch
            - Include the workflow name, commit message, author and a link to the logs
            - Mention the person who pushed if their Discord ID is in a mapping file
API:        REST
            POST /webhooks/github
Tech stack: Node.js, Cloudflare Workers, Discord webhooks
```

---

## Example 130

**Intent:**
load balancer for my 3 app servers

**Spec:**
```
Type:       Infrastructure setup (load balancing)
Features:   - Spread traffic across three app servers with HAProxy
            - Remove servers that fail health checks and add them back when healthy
            - Terminate TLS at the load balancer
            - Keep sticky sessions using a cookie
            - Run two HAProxy nodes with keepalived for failover
Tech stack: HAProxy, keepalived, Let's Encrypt
```

---

## Example 131

**Intent:**
discord bot that welcomes new members and asks them to pick their language

**Spec:**
```
Type:       Bot (Discord)
Features:   - Send a welcome message in the welcome channel when someone joins
            - Show buttons for each language
            - Give the member the matching language role
            - Send a direct message with the server rules in their language
            - Kick members who don't pick a language within 24 hours
Tech stack: Python, discord.py
```

---

## Example 132

**Intent:**
ok so here's my situation. i sell handmade jewelry on etsy AND on my own shopify store, and when something sells on one i forget to lower the stock on the other, so i've oversold twice this month. i need them to stay in sync by themselves

**Spec:**
```
Type:       Data pipeline (Etsy and Shopify inventory sync)
Data model: Product(id, sku, etsy_listing_id, shopify_variant_id, quantity, updated_at)
            StockChange(id, product_id -> Product, source, delta, created_at)
Features:   - Receive Shopify order webhooks and poll Etsy for new receipts every 5 minutes
            - Lower stock on the other channel when an item sells on one
            - Keep one master quantity per SKU
            - Deactivate a listing on both channels when stock reaches zero
            - Email a warning if the two channels disagree
API:        REST
            POST /webhooks/shopify/orders
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Etsy Open API v3, Shopify Admin API, APScheduler
```

---

## Example 133

**Intent:**
cert renewal for all our internal domains

**Spec:**
```
Type:       Infrastructure setup (TLS certificates)
Features:   - Issue certificates for internal hostnames with a DNS-01 challenge
            - Renew certificates automatically 30 days before expiry
            - Push renewed certificates to the load balancers and reload them
            - Alert when a renewal fails
            - List all certificates and their expiry dates
Tech stack: cert-manager, Let's Encrypt, Route 53 DNS, Kubernetes
```

---

## Example 134

**Intent:**
bot discord pour mon serveur, je veux un système de niveaux quand les gens parlent

**Spec:**
```
Type:       Bot (Discord)
Data model: MemberXp(guild_id, user_id, xp, level, last_message_at)
            LevelReward(guild_id, level, role_id)
Features:   - Give members XP for messages, at most once per minute
            - Announce level-ups in a chosen channel
            - Give reward roles at certain levels
            - Show a member's level card with /rank
            - Show the server leaderboard with /top
Storage:    PostgreSQL
Tech stack: Python, discord.py, Pillow (rank cards)
```

---

## Example 135

**Intent:**
api to generate pdf invoices from json

**Spec:**
```
Type:       REST API service (document generation)
Auth:       API key per client
Data model: Template(id, name, html, css)
Features:   - Accept invoice data as JSON and a template name
            - Render the HTML template with the data
            - Convert the HTML to PDF with page numbers and headers
            - Return the PDF directly or store it and return a link
            - Process large batches asynchronously with a job ID
API:        REST
            POST /invoices/pdf
            POST /batches
            GET  /batches/{id}
Storage:    S3-compatible storage (generated PDFs)
Tech stack: Node.js, Fastify, Handlebars, Puppeteer, BullMQ
```

---

## Example 136

**Intent:**
alert me if our api gets lots of 500 errors

**Spec:**
```
Type:       Infrastructure setup (error rate alerting)
Features:   - Count HTTP responses by status code from the load balancer metrics
            - Calculate the 5xx error rate over a 5-minute window
            - Alert when the error rate is above 2% for 5 minutes
            - Send alerts to PagerDuty and the team Slack channel
            - Include a link to the related dashboard in each alert
Tech stack: Amazon CloudWatch alarms, ALB metrics, SNS, PagerDuty
```

---

## Example 137

**Intent:**
hubspot form submissions into our postgres too pls

**Spec:**
```
Type:       Webhook service (HubSpot to PostgreSQL)
Data model: FormSubmission(id, hubspot_submission_id, form_id, email, fields_json, submitted_at)
Features:   - Receive HubSpot form submission webhooks
            - Validate the X-HubSpot-Signature-v3 header and timestamp
            - Store each submission with all form fields as JSON
            - Skip duplicates by submission ID
            - Backfill old submissions from the HubSpot Forms API once
API:        REST
            POST /webhooks/hubspot
Storage:    PostgreSQL
Tech stack: Python, FastAPI, SQLAlchemy, HubSpot API
```

---

## Example 138

**Intent:**
An internal Slack bot where people type /oncall and it tells them who is on call this week for each team.

**Spec:**
```
Type:       Bot (Slack)
Features:   - Answer /oncall with the current on-call person for each team
            - Answer /oncall <team> for one team
            - Read schedules from the PagerDuty API
            - Post the new rotation in #engineering every Monday morning
            - Verify Slack request signatures
API:        REST
            POST /slack/commands
Tech stack: Go, Slack API, PagerDuty REST API
```

---

## Example 139

**Intent:**
Our webshop is on Magento and the ERP is SAP Business One. Orders need to go to SAP and stock and prices need to come back to Magento. Right now an intern copies it every day which is crazy.

**Spec:**
```
Type:       Data pipeline (Magento and SAP Business One integration)
Data model: OrderExport(id, magento_order_id, sap_doc_entry, status, error, exported_at)
            SyncRun(id, kind, started_at, finished_at, records)
Features:   - Export new Magento orders to SAP as sales orders every 10 minutes
            - Create SAP business partners for new customers
            - Import stock levels from SAP to Magento every 15 minutes
            - Import price list changes from SAP every night
            - Show failed orders with the error so staff can fix and retry
Storage:    PostgreSQL
Tech stack: PHP, Symfony, SAP Business One Service Layer, Magento REST API, Symfony Messenger
```

---

## Example 140

**Intent:**
bot for telegram to see my server status

**Spec:**
```
Type:       Bot (Telegram)
Features:   - Answer /status with CPU, memory, disk and uptime
            - Answer /services with the state of chosen systemd services
            - Restart a service with /restart <name> after a confirmation button
            - Respond only to the owner's Telegram user ID
            - Send an alert when a watched service stops
Tech stack: Python, python-telegram-bot, psutil
```

---

## Example 141

**Intent:**
need a webhook to recieve paddle payments and give license keys

**Spec:**
```
Type:       Webhook service (Paddle licensing)
Data model: License(id, key, email, product, paddle_transaction_id, activations_allowed, created_at)
Features:   - Receive transaction.completed events from Paddle
            - Verify the Paddle-Signature header
            - Generate a unique license key for the purchased product
            - Email the license key to the buyer
            - Revoke the license on refund events
API:        REST
            POST /webhooks/paddle
            POST /licenses/activate
Storage:    PostgreSQL
Tech stack: Node.js, Express, Paddle Billing API, Postmark
```

---

## Example 142

**Intent:**
terraform for a gcp cloud run service with cloud sql

**Spec:**
```
Type:       Infrastructure setup (infrastructure as code)
Features:   - Create a Cloud Run service from a container image in Artifact Registry
            - Create a Cloud SQL PostgreSQL instance with private IP
            - Connect Cloud Run to Cloud SQL through a VPC connector
            - Store the database password in Secret Manager
            - Map a custom domain to the service
Tech stack: Terraform, Google Cloud Run, Cloud SQL, Secret Manager, Artifact Registry
```

---

## Example 143

**Intent:**
how do i get slack notified when someone signs up to my app

**Spec:**
```
Type:       Webhook service (sign-up notifications)
Features:   - Receive a user.created event from the app's backend
            - Check a shared secret in the request header
            - Post the new user's name, email domain and plan to a Slack channel
            - Add a daily total of sign-ups at the end of the day
API:        REST
            POST /events/user-created
Tech stack: Node.js, Vercel serverless functions, Slack Incoming Webhooks
```

---

## Example 144

**Intent:**
backup for our mongodb atlas cluster outside of atlas

**Spec:**
```
Type:       Scheduled script (database backup)
Features:   - Run mongodump against a secondary node every night
            - Compress the archive with gzip
            - Upload it to a Google Cloud Storage bucket with object versioning
            - Keep 30 daily and 12 monthly backups
            - Report backup size and duration to a monitoring endpoint
Storage:    Google Cloud Storage
Tech stack: Bash, mongodump, gsutil, Kubernetes CronJob
```

---

## Example 145

**Intent:**
need a backend to store high scores from our puzzle game, players on ios and android

**Spec:**
```
Type:       REST API service (game leaderboard)
Auth:       Signed device token issued at first launch
Data model: Player(id, device_id, display_name, created_at)
            Score(id, player_id -> Player, level, points, submitted_at)
Features:   - Submit a score with a signature to stop simple cheating
            - Return the global top 100
            - Return the player's own rank and nearby players
            - Keep daily, weekly and all-time boards
            - Reject impossible scores above a level's maximum
API:        REST
            POST /scores
            GET  /leaderboards/{period}
            GET  /leaderboards/{period}/me
Storage:    Redis sorted sets, PostgreSQL
Tech stack: Go, Gin, Redis
```

---

## Example 146

**Intent:**
github actions deploy to my vps when i push to main

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Run tests on every push to main
            - Connect to the VPS over SSH with a deploy key stored in GitHub secrets
            - Pull the latest code and install dependencies
            - Restart the app with PM2 without downtime
            - Post the deploy result to Discord
Tech stack: GitHub Actions, SSH, PM2, Node.js
```

---

## Example 147

**Intent:**
email inbox to support tickets

**Spec:**
```
Type:       Webhook service (inbound email to tickets)
Data model: Ticket(id, subject, requester_email, status, created_at)
            TicketMessage(id, ticket_id -> Ticket, from_email, body, attachments_json, received_at)
Features:   - Receive inbound emails from the email provider's parse webhook
            - Create a new ticket for new conversations
            - Add replies to the existing ticket using a ticket ID in the subject
            - Save attachments to file storage
            - Send an auto-reply with the ticket number
API:        REST
            POST /inbound/email
Storage:    PostgreSQL, S3 (attachments)
Tech stack: Python, Django, SendGrid Inbound Parse
```

---

## Example 148

**Intent:**
i run a small esports org. we want a discord bot that lets players sign up teams for our weekly tournament, checks they have 5 players, and then makes the bracket and posts match times. right now its all in a messy google form

**Spec:**
```
Type:       Bot (Discord)
Data model: Tournament(id, guild_id, name, starts_at, status)
            Team(id, tournament_id -> Tournament, name, captain_id)
            TeamPlayer(team_id -> Team, discord_user_id)
            Match(id, tournament_id -> Tournament, team_a_id, team_b_id, round, scheduled_at, winner_id)
Features:   - Register teams with /register and a player list
            - Reject teams without exactly 5 players or with players in another team
            - Close sign-ups and generate a single-elimination bracket
            - Post match times and ping both teams
            - Let captains report results and advance the winner
Storage:    PostgreSQL
Tech stack: TypeScript, discord.js, Prisma
```

---

## Example 149

**Intent:**
status checks for our dns records, warn if they change

**Spec:**
```
Type:       Scheduled script (DNS monitoring)
Data model: DnsSnapshot(id, domain, record_type, values, checked_at)
Features:   - Query A, AAAA, MX, NS and TXT records for each domain every 15 minutes
            - Compare results with the last snapshot
            - Alert by email when a record changes unexpectedly
            - Alert when a domain stops resolving
            - Keep a history of all changes
Storage:    SQLite
Tech stack: Python, dnspython, cron
```

---

## Example 150

**Intent:**
sendgrid bounces and unsubscribes should update our user table

**Spec:**
```
Type:       Webhook service (SendGrid events)
Data model: EmailEvent(id, sg_event_id, email, event, reason, occurred_at)
Features:   - Receive SendGrid Event Webhook batches
            - Verify the signed event webhook with the public key
            - Mark users as bounced on hard bounces
            - Turn off marketing emails on unsubscribe and spam reports
            - Ignore events already processed
API:        REST
            POST /webhooks/sendgrid
Storage:    PostgreSQL
Tech stack: Ruby, Rails, SendGrid Event Webhook
```

---

## Example 151

**Intent:**
my clients wants an api to track their delivery trucks in real time

**Spec:**
```
Type:       REST API service (fleet tracking)
Auth:       API keys for trucks; JWT for client dashboards
Data model: Truck(id, plate, client_id, driver_name)
            Position(id, truck_id -> Truck, lat, lng, speed, recorded_at)
Features:   - Accept GPS positions from trucks every 10 seconds
            - Return the latest position of each truck
            - Stream live positions to dashboards over WebSocket
            - Return a truck's route for a given day
            - Alert when a truck leaves a set area (geofence)
API:        REST
            POST /trucks/{id}/positions
            GET  /trucks/positions/latest
            GET  /trucks/{id}/route?date={date}
            WS   /live
Storage:    PostgreSQL with PostGIS
Tech stack: Node.js, Fastify, Socket.IO, PostGIS
```

---

## Example 152

**Intent:**
make a bot in slack where i can type a customer email and it shows their stripe subscription info

**Spec:**
```
Type:       Bot (Slack)
Features:   - Answer /customer <email> with the customer's plan, status and next invoice date
            - Show the last 5 payments with their result
            - Add a button to open the customer in the Stripe dashboard
            - Allow only members of the support channel to use it
            - Verify Slack request signatures
API:        REST
            POST /slack/commands
Tech stack: Python, Slack Bolt, Stripe SDK, AWS Lambda
```

---

## Example 153

**Intent:**
we need audit logging for our backend, who changed what and when

**Spec:**
```
Type:       REST API service (audit log)
Auth:       Service tokens for writing; admin JWT for reading
Data model: AuditEvent(id, actor_id, actor_type, action, resource_type, resource_id, before_json, after_json, ip, occurred_at)
Features:   - Accept audit events from all services
            - Make events append-only (no update or delete)
            - Search events by actor, resource and time range
            - Export search results as CSV
            - Keep events for 7 years in cheaper storage after 90 days
API:        REST
            POST /audit-events
            GET  /audit-events
Storage:    PostgreSQL (recent), S3 Glacier (archive)
Tech stack: Go, PostgreSQL, AWS S3 lifecycle rules
```

---

## Example 154

**Intent:**
prometheus alert when backups did not run

**Spec:**
```
Type:       Infrastructure setup (backup monitoring)
Features:   - Push a timestamp metric to the Pushgateway after each successful backup
            - Alert when the last successful backup is older than 26 hours
            - Alert when the backup file size drops by more than 50%
            - Send alerts to email through Alertmanager
            - Show backup history on a Grafana panel
Tech stack: Prometheus, Pushgateway, Alertmanager, Grafana
```

---

## Example 155

**Intent:**
i'd like a whatsapp chatbot for my travel agency that answers common questions and collects trip requests (destination, dates, budget) and then sends them to our crm

**Spec:**
```
Type:       Chatbot (WhatsApp, travel agency)
Data model: TripRequest(id, phone, name, destination, start_date, end_date, budget, crm_id, created_at)
Features:   - Answer common questions about visas, payments and cancellations
            - Ask step by step for destination, dates, number of travelers and budget
            - Confirm the details back to the customer
            - Create a lead in the CRM with the trip request
            - Hand the chat to a human agent on request
API:        REST
            POST /webhooks/whatsapp
Storage:    PostgreSQL
Tech stack: Python, FastAPI, WhatsApp Cloud API, Zoho CRM API
```

---

## Example 156

**Intent:**
rotate aws access keys automatically

**Spec:**
```
Type:       Scheduled script (credential rotation)
Features:   - Find IAM user access keys older than 80 days
            - Create a new key and store it in AWS Secrets Manager
            - Deactivate the old key after 7 days and delete it after 14
            - Notify the key owner by email at each step
            - Write a report of all keys and their age
Tech stack: Python, boto3, AWS Lambda, EventBridge schedule
```

---

## Example 157

**Intent:**
graphql api for a recipe app but in python

**Spec:**
```
Type:       GraphQL API service
Auth:       JWT bearer tokens
Data model: User(id, username, email)
            Recipe(id, author_id -> User, title, steps, prep_minutes)
            Ingredient(id, recipe_id -> Recipe, name, amount, unit)
Features:   - Query recipes with search by title and ingredient
            - Create, update and delete own recipes through mutations
            - Save recipes to favourites
            - Return a shopping list for a set of recipes
            - Batch database lookups with DataLoader
API:        GraphQL
            POST /graphql
Storage:    PostgreSQL
Tech stack: Python, Strawberry GraphQL, FastAPI, SQLAlchemy
```

---

## Example 158

**Intent:**
send an alert to slack when someone leaves a 1 star review on google

**Spec:**
```
Type:       Scheduled script (review monitoring)
Data model: Review(id, google_review_id, location, rating, text, created_at)
Features:   - Fetch new reviews for each business location every hour
            - Post 1 and 2 star reviews to a Slack channel immediately
            - Send a daily digest of all other reviews
            - Remember which reviews were already handled
Storage:    SQLite
Tech stack: Python, Google Business Profile API, Slack Web API
```

---

## Example 159

**Intent:**
cron jobs in kubernetes with monitoring

**Spec:**
```
Type:       Infrastructure setup (Kubernetes CronJobs)
Features:   - Run scheduled jobs as Kubernetes CronJobs
            - Stop overlapping runs with concurrencyPolicy Forbid
            - Retry failed jobs up to 3 times
            - Keep the last 3 successful and failed job pods for debugging
            - Alert when a job fails or has not succeeded on schedule
Tech stack: Kubernetes CronJob, kube-state-metrics, Prometheus, Alertmanager
```

---

## Example 160

**Intent:**
the photographers in my studio upload raw files to dropbox, i want an automatic backup to s3 glacier

**Spec:**
```
Type:       Scheduled script (archive backup)
Features:   - List new files in the shared Dropbox folder every night
            - Copy new raw files to an S3 bucket using the Glacier Deep Archive storage class
            - Keep the folder structure from Dropbox
            - Check file checksums after upload
            - Email a monthly report of storage used and cost
Storage:    Amazon S3 Glacier Deep Archive
Tech stack: Python, Dropbox API, boto3, cron
```

---

## Example 161

**Intent:**
discord bot for dnd that rolls dice

**Spec:**
```
Type:       Bot (Discord)
Features:   - Roll dice with /roll 2d20+5 and show each die
            - Support advantage and disadvantage rolls
            - Save characters' modifiers so /roll stealth works
            - Keep an initiative order with /init
Tech stack: JavaScript, discord.js
```

---

## Example 162

**Intent:**
endpoint so our partners can push their product catalog to us as json

**Spec:**
```
Type:       REST API service (catalog ingestion)
Auth:       API key per partner
Data model: Partner(id, name, api_key_hash)
            Product(id, partner_id -> Partner, external_id, title, price, stock, updated_at)
            ImportJob(id, partner_id -> Partner, status, rows_total, rows_failed, created_at)
Features:   - Accept catalog uploads of up to 50,000 products
            - Validate each product against a JSON schema
            - Upsert products by partner and external ID in a background job
            - Return a job ID and let partners check import status and errors
            - Remove products missing from a full catalog upload
API:        REST
            POST /catalog/imports
            GET  /catalog/imports/{id}
            GET  /catalog/imports/{id}/errors
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Celery, jsonschema
```

---

## Example 163

**Intent:**
trello card moved to done -> post in slack and log the time in harvest

**Spec:**
```
Type:       Webhook service (Trello to Slack and Harvest)
Features:   - Receive Trello board webhooks
            - Verify the X-Trello-Webhook signature
            - Act when a card moves to the Done list
            - Post the card title and members to Slack
            - Create a Harvest time entry from the card's time estimate
API:        REST
            HEAD /webhooks/trello
            POST /webhooks/trello
Tech stack: Node.js, Express, Trello API, Harvest API v2
```

---

## Example 164

**Intent:**
we need high availability postgres

**Spec:**
```
Type:       Infrastructure setup (database high availability)
Features:   - Run a PostgreSQL primary with two streaming replicas
            - Fail over to a replica automatically when the primary is down
            - Point apps to the current primary through a single endpoint
            - Take continuous WAL archives and base backups for point-in-time recovery
            - Alert when replication lag is above 30 seconds
Tech stack: PostgreSQL, Patroni, etcd, HAProxy, pgBackRest
```

---

## Example 165

**Intent:**
sms alert for parents when school bus is near their stop

**Spec:**
```
Type:       Webhook service (bus arrival alerts)
Data model: Stop(id, route_id, name, lat, lng)
            Parent(id, phone, stop_id -> Stop)
            Alert(id, parent_id -> Parent, sent_on)
Features:   - Receive GPS updates from the bus tracker
            - Detect when the bus is within 1 km of a stop
            - Text the parents at that stop once per trip
            - Let parents pause alerts on sick days by texting PAUSE
            - Skip alerts on school holidays
API:        REST
            POST /gps
            POST /sms/inbound
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django, Twilio SMS, PostGIS
```

---

## Example 166

**Intent:**
create a central place to see logs from our aws lambdas

**Spec:**
```
Type:       Infrastructure setup (log aggregation)
Features:   - Subscribe all Lambda log groups to a central log pipeline
            - Send logs through Kinesis Data Firehose to OpenSearch
            - Parse structured JSON logs into fields
            - Build saved searches for errors and timeouts
            - Set log retention to 30 days in CloudWatch
Tech stack: AWS CloudWatch Logs, Kinesis Data Firehose, Amazon OpenSearch, Terraform
```

---

## Example 167

**Intent:**
i want a rest api for my todo app in rust

**Spec:**
```
Type:       REST API service
Auth:       JWT bearer tokens
Data model: User(id, email, password_hash)
            Todo(id, user_id -> User, title, done, due_date, created_at)
Features:   - Register and log in users
            - Create, list, update and delete todos
            - Filter todos by done status and due date
            - Return validation errors as JSON
API:        REST
            POST /auth/register
            POST /auth/login
            GET  /todos
            POST /todos
            PATCH /todos/{id}
            DELETE /todos/{id}
Storage:    PostgreSQL
Tech stack: Rust, Axum, sqlx, argon2, jsonwebtoken
```

---

## Example 168

**Intent:**
kindly create system that send otp by email for login to our portal, our company is in india and users are many

**Spec:**
```
Type:       REST API service (email OTP login)
Auth:       Email one-time password, then JWT session
Data model: User(id, email, name, status)
            Otp(id, email, code_hash, expires_at, attempts)
Features:   - Send a 6-digit OTP to the user's email
            - Expire the OTP after 5 minutes
            - Block after 3 wrong attempts for 15 minutes
            - Limit OTP requests per email and per IP
            - Scale sending with a queue during peak login times
API:        REST
            POST /auth/otp/send
            POST /auth/otp/verify
Storage:    Redis (OTPs), MySQL (users)
Tech stack: Java, Spring Boot, Amazon SES, RabbitMQ
```

---

## Example 169

**Intent:**
sync google calendar events to a slack status

**Spec:**
```
Type:       Scheduled script (Google Calendar to Slack status)
Features:   - Read the user's Google Calendar every 5 minutes
            - Set the Slack status to "In a meeting" during events
            - Set "Out of office" for all-day OOO events
            - Clear the status when the event ends
            - Skip events marked as private
Tech stack: Python, Google Calendar API, Slack Web API (users.profile.set)
```

---

## Example 170

**Intent:**
status page monitoring for 3rd party services we depend on

**Spec:**
```
Type:       Scheduled script (vendor status monitoring)
Data model: VendorStatus(id, vendor, status, incident_title, checked_at)
Features:   - Read the status pages of Stripe, AWS, GitHub and Twilio every 5 minutes
            - Detect new incidents and status changes
            - Post changes to an #outages Slack channel
            - Show all vendors' current status in one message with /vendors
Storage:    SQLite
Tech stack: Python, Statuspage JSON APIs, RSS feeds, Slack Bolt
```

---

## Example 171

**Intent:**
webhook from our form builder to create a google calendar event

**Spec:**
```
Type:       Webhook service (form to Google Calendar)
Features:   - Receive form submissions with name, email, date and time
            - Check the shared secret token in the URL
            - Create a Google Calendar event and invite the person
            - Reply with a conflict message if the slot is already taken
            - Send a confirmation email with the event link
API:        REST
            POST /webhooks/form?token={secret}
Tech stack: Node.js, Google Calendar API (service account), Nodemailer
```

---

## Example 172

**Intent:**
pls help, need ci that run my unity tests and build for android

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Run Unity edit-mode and play-mode tests on every push
            - Cache the Library folder to speed up builds
            - Build a signed Android APK and AAB with the keystore from secrets
            - Upload builds as workflow artifacts
            - Upload release builds to the Google Play internal test track
Tech stack: GitHub Actions, GameCI (unity-test-runner, unity-builder), Fastlane
```

---

## Example 173

**Intent:**
keycloak for login across our 4 apps

**Spec:**
```
Type:       Infrastructure setup (identity provider)
Auth:       OpenID Connect through Keycloak, with optional Google login
Features:   - Run Keycloak with a PostgreSQL database in Docker
            - Create one realm with a client for each app
            - Turn on single sign-on and single logout across the apps
            - Enforce TOTP two-factor login for admin users
            - Map company groups to app roles in the tokens
Tech stack: Keycloak, PostgreSQL, Docker Compose, Nginx
```

---

## Example 174

**Intent:**
bot that posts in our slack when a new job applicant comes in from greenhouse

**Spec:**
```
Type:       Webhook service (Greenhouse to Slack)
Features:   - Receive Greenhouse candidate application webhooks
            - Verify the Signature header with the shared secret
            - Post the candidate's name, job and source to the hiring channel for that job
            - Add a button that opens the candidate profile
            - Skip internal referrals marked confidential
API:        REST
            POST /webhooks/greenhouse
Tech stack: Python, Flask, Slack Web API
```

---

## Example 175

**Intent:**
grafana dashboard for our postgres

**Spec:**
```
Type:       Infrastructure setup (database monitoring)
Features:   - Collect PostgreSQL metrics with postgres_exporter
            - Show connections, transactions per second, cache hit ratio and replication lag
            - Show the slowest queries from pg_stat_statements
            - Alert when connections reach 80% of max_connections
            - Alert on long-running transactions over 10 minutes
Tech stack: Prometheus, postgres_exporter, Grafana, Alertmanager
```

---

## Example 176

**Intent:**
customer can pay invoices via bank transfer, we need to match incoming payments to invoices automatically

**Spec:**
```
Type:       Data pipeline (payment reconciliation)
Data model: Invoice(id, number, customer_id, amount, currency, status)
            BankTransaction(id, bank_ref, amount, currency, remittance_info, booked_at, invoice_id -> Invoice)
Features:   - Import bank transactions daily through the bank's open banking API
            - Match transactions to invoices by invoice number in the reference and exact amount
            - Mark matched invoices as paid
            - Put partial and unclear payments in a review list
            - Email a daily reconciliation summary to finance
Storage:    PostgreSQL
Tech stack: Python, GoCardless Bank Account Data API, SQLAlchemy, cron
```

---

## Example 177

**Intent:**
a slack bot for polls

**Spec:**
```
Type:       Bot (Slack)
Data model: Poll(id, channel_id, question, creator_id, anonymous, closes_at)
            Vote(id, poll_id -> Poll, user_id, option_index)
Features:   - Create a poll with /poll "question" "option 1" "option 2"
            - Show buttons for each option and live vote counts
            - Allow one vote per person with the option to change it
            - Support anonymous polls
            - Close the poll at a set time and post results
API:        REST
            POST /slack/commands
            POST /slack/interactions
Storage:    PostgreSQL
Tech stack: Node.js, Slack Bolt
```

---

## Example 178

**Intent:**
my team wants to stop sharing the root aws account. set up proper access

**Spec:**
```
Type:       Infrastructure setup (cloud access management)
Features:   - Create an AWS Organization with separate dev and prod accounts
            - Turn on IAM Identity Center with the company's Google Workspace as identity source
            - Give developers read-only access to prod and admin access to dev
            - Enforce MFA for all users
            - Lock away the root account with MFA and no access keys
            - Turn on CloudTrail for all accounts into a central bucket
Tech stack: AWS Organizations, IAM Identity Center, CloudTrail, Terraform
```

---

## Example 179

**Intent:**
api that checks if an email address is real before we save it

**Spec:**
```
Type:       REST API service (email validation)
Auth:       API key
Features:   - Check the email syntax
            - Check that the domain has MX records
            - Flag disposable email domains from a maintained list
            - Detect common typos like gmial.com and suggest a fix
            - Cache domain results for 24 hours
API:        REST
            GET  /validate?email={address}
Storage:    Redis (domain cache)
Tech stack: Go, net (DNS lookups), Redis
```

---

## Example 180

**Intent:**
messenger bot for facebook page of my shop to answer price questions

**Spec:**
```
Type:       Bot (Facebook Messenger)
Data model: Product(id, name, keywords, price, in_stock)
Features:   - Reply to messages asking about a product with its price and stock
            - Show quick-reply buttons for top product categories
            - Send the shop's opening hours and address on request
            - Pass the conversation to a human in the Page inbox when asked
API:        REST
            GET  /webhook (verification)
            POST /webhook
Storage:    SQLite
Tech stack: Node.js, Express, Messenger Platform API
```

---

## Example 181

**Intent:**
When our main database is under heavy load our reports page makes it worse. Can we have a read replica and send the reporting queries there?

**Spec:**
```
Type:       Infrastructure setup (read replica)
Features:   - Create a read replica of the RDS PostgreSQL database
            - Add a second database connection in the app for read-only reporting queries
            - Route the reports page and exports to the replica
            - Alert when replica lag is over 60 seconds
            - Fall back to the primary if the replica is unavailable
Tech stack: Amazon RDS PostgreSQL, CloudWatch, Django database routers
```

---

## Example 182

**Intent:**
i need a rest api in laravel for booking meeting rooms in the office

**Spec:**
```
Type:       REST API service (room booking)
Auth:       Laravel Sanctum tokens, Microsoft Entra ID sign-in
Data model: Room(id, name, capacity, floor, equipment)
            Booking(id, room_id -> Room, user_id, title, starts_at, ends_at)
Features:   - List rooms with free/busy status for a time range
            - Book a room and reject overlapping bookings
            - Cancel own bookings
            - Release rooms automatically if nobody checks in within 15 minutes
            - Sync bookings to Outlook calendars
API:        REST
            GET  /rooms?from={time}&to={time}
            POST /bookings
            DELETE /bookings/{id}
            POST /bookings/{id}/check-in
Storage:    MySQL
Tech stack: PHP, Laravel, Microsoft Graph API
```

---

## Example 183

**Intent:**
webhook from calendly to create zoom meeting

**Spec:**
```
Type:       Webhook service (Calendly to Zoom)
Data model: MeetingLink(id, calendly_event_uri, zoom_meeting_id, join_url)
Features:   - Receive invitee.created and invitee.canceled events
            - Verify the Calendly-Webhook-Signature header
            - Create a Zoom meeting at the booked time
            - Email the join link to the invitee
            - Delete the Zoom meeting when the booking is canceled
API:        REST
            POST /webhooks/calendly
Storage:    SQLite
Tech stack: Python, FastAPI, Zoom API (server-to-server OAuth), SendGrid
```

---

## Example 184

**Intent:**
discord bot that shows valorant stats

**Spec:**
```
Type:       Bot (Discord)
Data model: LinkedAccount(discord_user_id, riot_id, region)
Features:   - Link a Riot ID with /link
            - Show rank, win rate and top agents with /stats
            - Show the last 5 matches with /matches
            - Cache stats for 10 minutes to stay within API limits
Storage:    SQLite
Tech stack: Python, discord.py, Riot Games API (via a third-party Valorant stats API)
```

---

## Example 185

**Intent:**
i want my nextjs app deployed on my own server with docker and auto https

**Spec:**
```
Type:       Infrastructure setup (self-hosted deployment)
Features:   - Build the Next.js app in standalone mode inside a Docker image
            - Run the container behind Caddy for automatic HTTPS
            - Deploy new versions by pulling the image and restarting with Docker Compose
            - Restart the container automatically if it crashes
            - Rotate container logs to stop the disk filling up
Tech stack: Next.js, Docker, Docker Compose, Caddy
```

---

## Example 186

**Intent:**
notify me on telegram when a website changes

**Spec:**
```
Type:       Scheduled script (website change monitoring)
Data model: Watch(id, url, css_selector, last_hash, last_text, checked_at)
Features:   - Fetch each watched page every 30 minutes
            - Compare only the chosen part of the page using a CSS selector
            - Send a Telegram message with the changed text when the content changes
            - Ignore changes in whitespace
            - Add and remove watches from a YAML file
Storage:    SQLite
Tech stack: Python, httpx, BeautifulSoup, Telegram Bot API
```

---

## Example 187

**Intent:**
outgoing email service with templates for the whole company, so every app stops using its own smtp settings

**Spec:**
```
Type:       REST API service (shared email service)
Auth:       API key per sending app
Data model: App(id, name, api_key_hash, from_address)
            Template(id, app_id -> App, name, subject, body_mjml)
            Message(id, app_id -> App, template_id -> Template, to_address, status, provider_id, sent_at)
Features:   - Send emails through one provider for all company apps
            - Render responsive templates from MJML
            - Limit how many emails each app can send per hour
            - Track opens, bounces and complaints from provider webhooks
            - Keep a suppression list shared by all apps
API:        REST
            POST /messages
            GET  /messages/{id}
            POST /webhooks/provider
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, MJML, Amazon SES, SQS
```

---

## Example 188

**Intent:**
connect stripe to quickbooks so payouts get recorded

**Spec:**
```
Type:       Data pipeline (Stripe to QuickBooks)
Data model: PayoutSync(id, stripe_payout_id, qb_deposit_id, amount, synced_at)
Features:   - Receive payout.paid events from Stripe with signature verification
            - Fetch the balance transactions in each payout
            - Record a deposit in QuickBooks with sales, refunds and Stripe fees as separate lines
            - Skip payouts already recorded
            - Email the bookkeeper a summary of each payout
API:        REST
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Node.js, Stripe SDK, QuickBooks Online Accounting API
```

---

## Example 189

**Intent:**
uptime monitor for apis with checks on the json response too

**Spec:**
```
Type:       Scheduled script (API monitoring)
Data model: ApiCheck(id, name, method, url, headers_json, expected_status, assertions_json)
            CheckRun(id, check_id -> ApiCheck, passed, duration_ms, error, ran_at)
Features:   - Call each API endpoint every minute with configured headers
            - Check status code, response time and JSON field values
            - Alert in Slack when an assertion fails twice in a row
            - Show pass rate and latency per check
            - Load checks from a YAML file stored in git
Storage:    PostgreSQL
Tech stack: Go, gjson, Slack Incoming Webhooks
```

---

## Example 190

**Intent:**
hello, we are small hotel in vietnam, we want when guest book on booking.com we get message in zalo

**Spec:**
```
Type:       Scheduled script (booking notifications)
Data model: Reservation(id, booking_ref, guest_name, room_type, check_in, check_out, notified_at)
Features:   - Read new reservations from the hotel channel manager API every 10 minutes
            - Send a Zalo message to the staff group with guest name, room and dates
            - Send a message when a booking is cancelled
            - Send a daily list of arrivals each morning at 7:00
Storage:    SQLite
Tech stack: Python, channel manager API, Zalo Official Account API, cron
```

---

## Example 191

**Intent:**
canary releases on kubernetes

**Spec:**
```
Type:       Infrastructure setup (progressive delivery)
Features:   - Send 10% of traffic to the new version first
            - Raise traffic step by step to 25%, 50% and 100%
            - Watch error rate and latency from Prometheus at each step
            - Roll back automatically when metrics get worse
            - Post rollout progress to Slack
Tech stack: Argo Rollouts, Kubernetes, NGINX Ingress, Prometheus
```

---

## Example 192

**Intent:**
api for a newsletter signup with double opt in

**Spec:**
```
Type:       REST API service (newsletter subscriptions)
Data model: Subscriber(id, email, status, confirm_token_hash, subscribed_at, confirmed_at, unsubscribed_at)
Features:   - Accept sign-ups from the website form
            - Send a confirmation email with a single-use link
            - Activate the subscriber only after they click the link
            - Unsubscribe with a signed one-click link
            - Block sign-up spam with a CAPTCHA check
API:        REST
            POST /subscribe
            GET  /confirm?token={token}
            GET  /unsubscribe?token={token}
Storage:    PostgreSQL
Tech stack: Python, Flask, hCaptcha, Mailgun
```

---

## Example 193

**Intent:**
shopify low stock alert in slack

**Spec:**
```
Type:       Scheduled script (low stock alerts)
Features:   - Read inventory levels for all products every hour
            - Compare each variant with its own reorder threshold
            - Post low-stock variants to a Slack channel with current quantity
            - Alert only once until the item is restocked
            - Post a weekly list of out-of-stock items
Tech stack: Python, Shopify Admin GraphQL API, Slack Incoming Webhooks, GitHub Actions schedule
```

---

## Example 194

**Intent:**
Our app has users in many countries and we want to send them text messages in their own language for things like order confirmation. Need a notification backend for that.

**Spec:**
```
Type:       REST API service (localized SMS notifications)
Auth:       Internal API key
Data model: SmsTemplate(id, key, locale, text)
            SmsMessage(id, user_id, phone, template_key, locale, status, provider_id, sent_at)
Features:   - Send SMS by template key and the user's language
            - Fall back to English when a translation is missing
            - Pick the cheapest SMS provider route per country
            - Track delivery receipts from provider callbacks
            - Respect quiet hours in the user's time zone
API:        REST
            POST /sms
            POST /webhooks/sms-status
Storage:    PostgreSQL, Redis (queue)
Tech stack: Node.js, NestJS, Twilio, MessageBird, BullMQ
```

---

## Example 195

**Intent:**
wanna backup my github repos somewhere else just in case

**Spec:**
```
Type:       Scheduled script (repository backup)
Features:   - List all repositories of the user and their organizations through the GitHub API
            - Mirror-clone new repositories and fetch updates for existing ones
            - Back up issues and pull request comments as JSON
            - Upload a compressed archive to S3 every week
            - Report repositories that failed to back up
Storage:    Amazon S3
Tech stack: Python, GitHub REST API, git, boto3, cron
```

---

## Example 196

**Intent:**
we need to know when our ssl certificates on all subdomains expire, there are like 60

**Spec:**
```
Type:       Scheduled script (SSL certificate monitoring)
Data model: Certificate(hostname, issuer, expires_at, last_checked_at, error)
Features:   - Discover subdomains from certificate transparency logs and a config list
            - Connect to each hostname and read the certificate expiry
            - Alert in Slack 21 and 7 days before expiry
            - Alert on hostname mismatch or expired certificates
            - Send a weekly table of all certificates sorted by expiry
Storage:    SQLite
Tech stack: Python, ssl, crt.sh API, Slack Incoming Webhooks
```

---

## Example 197

**Intent:**
graphql api for our school's timetable and grades

**Spec:**
```
Type:       GraphQL API service
Auth:       School accounts with roles (student, parent, teacher)
Data model: Student(id, name, class_id -> Class)
            Class(id, name, year)
            Lesson(id, class_id -> Class, subject, teacher_id, weekday, period, room)
            Grade(id, student_id -> Student, subject, value, given_at)
Features:   - Query a class timetable by week
            - Let teachers add grades through mutations
            - Let students and parents see only their own grades
            - Notify parents of new grades by email
API:        GraphQL
            POST /graphql
Storage:    PostgreSQL
Tech stack: Java, Spring for GraphQL, Spring Security
```

---

## Example 198

**Intent:**
telegram bot for a crypto signals group, only paid members can join

**Spec:**
```
Type:       Bot (Telegram)
Data model: Member(id, telegram_user_id, plan, paid_until)
            Payment(id, member_id -> Member, provider_charge_id, amount, paid_at)
Features:   - Sell monthly access with Telegram Payments
            - Send a one-time invite link to the private channel after payment
            - Remove members from the channel when their access expires
            - Remind members 3 days before access ends
            - Show admins a list of active members
Storage:    PostgreSQL
Tech stack: Python, aiogram, Telegram Payments (Stripe provider)
```

---

## Example 199

**Intent:**
idempotent order api so customers never get charged twice when they click pay twice

**Spec:**
```
Type:       REST API service (order creation)
Auth:       JWT bearer tokens
Data model: Order(id, user_id, total, status, payment_intent_id, created_at)
            IdempotencyKey(key, user_id, request_hash, response_json, created_at)
Features:   - Require an Idempotency-Key header on order creation
            - Return the saved response when the same key is sent again
            - Reject a reused key with a different request body
            - Create one payment per order and confirm it with the payment provider
            - Expire idempotency keys after 24 hours
API:        REST
            POST /orders
            GET  /orders/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Stripe PaymentIntents
```

---

## Example 200

**Intent:**
gitlab runner on our own server for faster builds

**Spec:**
```
Type:       Infrastructure setup (CI runners)
Features:   - Install GitLab Runner on a dedicated build server
            - Use the Docker executor with a local cache for dependencies
            - Run up to 4 jobs at the same time
            - Tag the runner so only chosen projects use it
            - Clean up old images and volumes every night
Tech stack: GitLab Runner, Docker, cron
```

---

## Example 201

**Intent:**
alerts from grafana going to a telegram group

**Spec:**
```
Type:       Infrastructure setup (alert routing)
Features:   - Add a Telegram contact point in Grafana alerting
            - Send critical alerts to the on-call group and warnings to a quieter group
            - Group alerts by service to avoid floods of messages
            - Mute alerts during planned maintenance windows
            - Include dashboard links and current values in messages
Tech stack: Grafana Alerting, Telegram Bot API
```

---

## Example 202

**Intent:**
api to look up vat numbers of european companies for our invoices

**Spec:**
```
Type:       REST API service (VAT validation)
Auth:       API key
Data model: VatCheck(id, vat_number, country, valid, company_name, address, checked_at)
Features:   - Check a VAT number against the EU VIES service
            - Return company name and address when available
            - Cache results for 7 days
            - Return a clear error when VIES is down and retry later
            - Store each check as proof for tax audits
API:        REST
            GET  /vat/{number}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, zeep (VIES SOAP)
```

---

## Example 203

**Intent:**
github bot that comments test coverage change on prs

**Spec:**
```
Type:       Webhook service (GitHub App)
Data model: CoverageReport(id, repo, commit_sha, branch, percent, created_at)
Features:   - Accept coverage reports uploaded from CI with a repo token
            - Compare coverage with the base branch
            - Comment the change and uncovered new lines on the pull request
            - Set a failing status check if coverage drops more than 1%
            - Update the existing comment instead of posting new ones
API:        REST
            POST /reports
            POST /github/webhooks
Storage:    PostgreSQL
Tech stack: TypeScript, Probot, GitHub Checks API
```

---

## Example 204

**Intent:**
log retention policy and archive old logs cheap

**Spec:**
```
Type:       Infrastructure setup (log archiving)
Features:   - Keep searchable logs in Elasticsearch for 14 days
            - Roll indices daily with index lifecycle management
            - Snapshot old indices to S3 before deleting them
            - Move snapshots to Glacier after 90 days
            - Restore an archived day of logs on request
Tech stack: Elasticsearch ILM, snapshot repository (S3), S3 lifecycle rules
```

---

## Example 205

**Intent:**
a chatbot on our website that books appointments for the dentist

**Spec:**
```
Type:       Chatbot (appointment booking)
Data model: Patient(id, name, phone, email)
            Appointment(id, patient_id -> Patient, dentist_id, treatment, starts_at, status)
Features:   - Ask the patient for treatment type and preferred day
            - Show free slots from the practice calendar
            - Book the chosen slot and send a confirmation email
            - Answer questions about prices and insurance from a FAQ
            - Pass urgent pain cases to the reception phone number
API:        REST
            POST /chat
            GET  /slots?treatment={type}&date={date}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Google Calendar API, JavaScript chat widget
```

---

## Example 206

**Intent:**
rate limit login attempts to stop bots guessing passwords

**Spec:**
```
Type:       REST API service (brute-force protection)
Data model: LoginAttempt(key, failures, locked_until)
Features:   - Count failed logins per account and per IP address
            - Add a growing delay after each failure
            - Lock the account for 15 minutes after 10 failures
            - Show a CAPTCHA after 3 failures from the same IP
            - Email the user when their account gets locked
API:        REST
            POST /login
Storage:    Redis
Tech stack: Node.js, Express, rate-limiter-flexible, Cloudflare Turnstile
```

---

## Example 207

**Intent:**
every new paypal sale should go in my google sheet

**Spec:**
```
Type:       Webhook service (PayPal to Google Sheets)
Features:   - Receive PAYMENT.CAPTURE.COMPLETED webhooks
            - Verify the webhook with PayPal's verify-signature API
            - Append date, buyer email, amount, currency and transaction ID to the sheet
            - Skip transactions already in the sheet
            - Add a row for refunds with a negative amount
API:        REST
            POST /webhooks/paypal
Tech stack: Google Apps Script (web app), PayPal webhooks
```

---

## Example 208

**Intent:**
healthcheck and auto restart for docker containers on my server

**Spec:**
```
Type:       Infrastructure setup (container health)
Features:   - Add health checks to each container in Docker Compose
            - Restart unhealthy containers automatically
            - Update images automatically at night
            - Send a Discord message when a container restarts or updates
            - Show container status on a simple dashboard
Tech stack: Docker Compose, autoheal, Watchtower, Uptime Kuma
```

---

## Example 209

**Intent:**
So we have a Shopify Plus store and a separate loyalty program in our own system. When a customer buys something they should get points, when they return something points get taken back, and they should be able to spend points as a discount code at checkout.

**Spec:**
```
Type:       Webhook service (loyalty points)
Data model: Customer(id, shopify_customer_id, email, points_balance)
            PointsEntry(id, customer_id -> Customer, shopify_order_id, points, reason, created_at)
Features:   - Add points for paid orders from orders/paid webhooks
            - Remove points for refunds from refunds/create webhooks
            - Turn points into a single-use Shopify discount code on request
            - Verify Shopify HMAC headers and ignore duplicate webhooks
            - Show the customer's balance in the store through an app proxy
API:        REST
            POST /webhooks/shopify/orders-paid
            POST /webhooks/shopify/refunds
            POST /loyalty/redeem
            GET  /apps/loyalty/balance
Storage:    PostgreSQL
Tech stack: Ruby, Rails, shopify_app gem, Shopify Admin API
```

---

## Example 210

**Intent:**
windows servers patch status report every week

**Spec:**
```
Type:       Scheduled script (patch reporting)
Features:   - Query each Windows server for installed and pending updates
            - List servers that need a reboot
            - Flag servers missing security updates older than 30 days
            - Email an HTML report to the IT team every Monday
Tech stack: PowerShell, PSWindowsUpdate, Task Scheduler
```

---

## Example 211

**Intent:**
a bot in google chat for our team to request time off

**Spec:**
```
Type:       Bot (Google Chat)
Data model: LeaveRequest(id, user_email, start_date, end_date, type, status, approver_email)
Features:   - Open a dialog to request leave with dates and type
            - Send the request to the manager with approve and reject buttons
            - Add approved leave to a shared Google Calendar
            - Show a user's remaining days on request
API:        REST
            POST /chat/events
Storage:    Firestore
Tech stack: Node.js, Google Chat API, Google Calendar API, Cloud Run
```

---

## Example 212

**Intent:**
need smth that texts me when my etsy shop gets an order lol i always miss them

**Spec:**
```
Type:       Scheduled script (order notifications)
Data model: SeenReceipt(receipt_id, seen_at)
Features:   - Check the Etsy shop for new receipts every 5 minutes
            - Send an SMS with the item names and total for each new order
            - Remember which orders were already announced
            - Refresh the Etsy OAuth token automatically
Storage:    SQLite
Tech stack: Python, Etsy Open API v3, Twilio SMS, cron
```

---

## Example 213

**Intent:**
i am working in bank IT, we need service which collect logs from all applications and keep them 5 years for regulator, and nobody can change them

**Spec:**
```
Type:       Infrastructure setup (compliant log archiving)
Features:   - Collect application and audit logs from all servers with a log shipper
            - Store logs in write-once storage with a 5-year retention lock
            - Hash each daily log bundle and keep the hashes in a separate ledger
            - Search recent logs in a central search tool
            - Restrict log access by role and record every access
Tech stack: Fluent Bit, Amazon S3 Object Lock (compliance mode), OpenSearch, AWS KMS
```

---

## Example 214

**Intent:**
deploy django on aws elastic beanstalk

**Spec:**
```
Type:       Infrastructure setup (deployment)
Features:   - Package the Django app for Elastic Beanstalk with Gunicorn
            - Run database migrations and collectstatic during deploy
            - Use an RDS PostgreSQL database outside the environment
            - Serve static files from S3 and CloudFront
            - Deploy from GitHub Actions on pushes to main
Tech stack: AWS Elastic Beanstalk, RDS, S3, CloudFront, GitHub Actions
```

---

## Example 215

**Intent:**
discord bot so my friends can check if our palworld server is up and restart it

**Spec:**
```
Type:       Bot (Discord)
Features:   - Show server status and player count with /status
            - Start, stop and restart the game server container with buttons
            - Allow restart only for members with a Server Admin role
            - Back up the save folder before every restart
            - Post a message when the server goes down unexpectedly
Tech stack: Python, discord.py, Docker SDK for Python
```

---

## Example 216

**Intent:**
An API that our warehouse scanners call when a package is scanned, and it should update the order status and notify the customer.

**Spec:**
```
Type:       REST API service (package scanning)
Auth:       Device API key per scanner
Data model: Package(id, order_id, barcode, status, location, updated_at)
            ScanEvent(id, package_id -> Package, scanner_id, event, scanned_at)
Features:   - Record each scan with scanner, location and time
            - Move the order status forward (picked, packed, shipped)
            - Reject scans that skip a status or repeat the same event
            - Send the customer an email when the package ships
            - Show the scan history for a package
API:        REST
            POST /scans
            GET  /packages/{barcode}
Storage:    PostgreSQL
Tech stack: Kotlin, Spring Boot, RabbitMQ, SendGrid
```

---

## Example 217

**Intent:**
sync new mailchimp subscribers to our crm (zoho)

**Spec:**
```
Type:       Webhook service (Mailchimp to Zoho CRM)
Features:   - Receive Mailchimp subscribe and unsubscribe webhooks
            - Check a secret key in the webhook URL
            - Create a lead in Zoho CRM for new subscribers
            - Update the lead's email opt-out field on unsubscribe
            - Answer Mailchimp's GET validation request
API:        REST
            GET  /webhooks/mailchimp/{secret}
            POST /webhooks/mailchimp/{secret}
Tech stack: Python, Flask, Zoho CRM API v2
```

---

## Example 218

**Intent:**
the boss want daily report of website uptime in email

**Spec:**
```
Type:       Scheduled script (uptime report)
Features:   - Read check results from the monitoring tool's API
            - Calculate uptime percentage and average response time per site for yesterday
            - List each outage with start time and duration
            - Email an HTML report to management at 08:00
Tech stack: Python, UptimeRobot API, Jinja2, SMTP
```

---

## Example 219

**Intent:**
i need oauth2 server so other developers can build apps on top of our platform

**Spec:**
```
Type:       REST API service (OAuth 2.0 authorization server)
Auth:       OAuth 2.0 authorization code flow with PKCE, client credentials for server apps
Data model: OAuthClient(id, name, client_id, client_secret_hash, redirect_uris, owner_id)
            Grant(id, client_id -> OAuthClient, user_id, scopes, created_at)
            AccessToken(id, grant_id -> Grant, token_hash, expires_at)
Features:   - Let developers register apps and get client credentials
            - Show users a consent screen listing requested scopes
            - Issue access and refresh tokens
            - Let users see and revoke apps connected to their account
            - Provide a token introspection endpoint for resource servers
API:        REST
            GET  /oauth/authorize
            POST /oauth/token
            POST /oauth/introspect
            POST /oauth/revoke
Storage:    PostgreSQL
Tech stack: Node.js, node-oidc-provider, PostgreSQL
```

---

## Example 220

**Intent:**
deploy to fly.io from github

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Run tests on pull requests
            - Deploy to Fly.io with flyctl when main changes
            - Run database migrations as a release command
            - Keep secrets in Fly secrets
            - Deploy pull request preview apps and destroy them when closed
Tech stack: GitHub Actions, Fly.io, flyctl
```

---

## Example 221

**Intent:**
whatsapp message to patients when lab results ready

**Spec:**
```
Type:       Webhook service (lab result notifications)
Data model: ResultNotice(id, lab_order_id, patient_phone, sent_at, status)
Features:   - Receive result-ready events from the lab system
            - Send a WhatsApp template message saying results are ready, with no medical details
            - Include a link to the secure patient portal
            - Track delivery and read status from WhatsApp status webhooks
            - Retry with SMS if WhatsApp delivery fails
API:        REST
            POST /events/result-ready
            POST /webhooks/whatsapp
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, WhatsApp Cloud API, Twilio SMS
```

---

## Example 222

**Intent:**
i'm a freelancer and i use toggl to track time for my clients. at the end of the month i spend half a day making invoices. could toggl hours turn into draft invoices in my freshbooks automatically? each client has a different hourly rate

**Spec:**
```
Type:       Scheduled script (time tracking to invoices)
Data model: ClientRate(toggl_client_id, freshbooks_client_id, hourly_rate, currency)
Features:   - Run on the 1st of each month
            - Fetch last month's billable time entries from Toggl grouped by client and project
            - Apply each client's hourly rate
            - Create a draft invoice in FreshBooks with one line per project
            - Send a summary email listing the drafts to review
Storage:    YAML config file (client rates)
Tech stack: Python, Toggl Track API v9, FreshBooks API, cron
```

---

## Example 223

**Intent:**
graphql api with permissions per field for an hr system

**Spec:**
```
Type:       GraphQL API service
Auth:       OIDC login with roles (employee, manager, hr_admin)
Data model: Employee(id, name, email, department_id -> Department, manager_id -> Employee, salary, start_date)
            Department(id, name)
Features:   - Query employees and departments
            - Show salary only to HR admins and the employee's manager
            - Let employees update their own contact details
            - Log every read of sensitive fields
API:        GraphQL
            POST /graphql
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS GraphQL, GraphQL Shield, Prisma
```

---

## Example 224

**Intent:**
make my api respond faster with caching

**Spec:**
```
Type:       Infrastructure setup (API caching)
Features:   - Cache GET responses in Redis with a short time-to-live per route
            - Build cache keys from the path, query and user role
            - Clear related cache entries when data changes
            - Add Cache-Control and ETag headers so clients can reuse responses
            - Show cache hit rate on a dashboard
Storage:    Redis
Tech stack: Redis, Express middleware, Grafana
```

---

## Example 225

**Intent:**
bot telegram pra minha loja vender produtos digitais, cliente paga com pix e recebe o arquivo

**Spec:**
```
Type:       Bot (Telegram)
Data model: Product(id, name, price, file_id)
            Order(id, chat_id, product_id -> Product, pix_txid, status, paid_at)
Features:   - Show the product catalog in Portuguese with buttons
            - Create a Pix charge with a QR code and copy-paste code
            - Confirm payment through the payment provider's webhook
            - Send the digital file automatically after payment
            - Expire unpaid charges after 30 minutes
API:        REST
            POST /webhooks/pix
Storage:    PostgreSQL
Tech stack: Python, aiogram, Mercado Pago API (Pix)
```

---

## Example 226

**Intent:**
track deploys and show them as lines on our grafana graphs

**Spec:**
```
Type:       Infrastructure setup (deploy annotations)
Features:   - Send an annotation to Grafana at the end of every deploy job
            - Include service name, version and who deployed
            - Show annotations on all service dashboards
            - Count deploys per week per service
Tech stack: GitHub Actions, Grafana Annotations API
```

---

## Example 227

**Intent:**
api for my side project that turns text into speech mp3 files

**Spec:**
```
Type:       REST API service (text to speech)
Auth:       API key with a monthly character quota
Data model: ApiKey(id, key_hash, owner_email, monthly_chars, used_chars)
            Synthesis(id, api_key_id -> ApiKey, text_length, voice, file_url, created_at)
Features:   - Accept text up to 5,000 characters and a voice name
            - Generate an MP3 with a text-to-speech provider
            - Store the file and return a download link
            - Return the same file for identical text and voice (cache by hash)
            - Reject requests over the monthly quota
API:        REST
            POST /speech
            GET  /voices
            GET  /usage
Storage:    PostgreSQL, Cloudflare R2 (audio files)
Tech stack: Python, FastAPI, Amazon Polly
```

---

## Example 228

**Intent:**
notifications for new github releases of libraries we use

**Spec:**
```
Type:       Scheduled script (release watcher)
Data model: WatchedRepo(id, owner, name, last_release_tag)
Features:   - Check the latest release of each repository in the list every 6 hours
            - Post new releases to Slack with the version and release notes
            - Highlight releases that mention security or breaking changes
            - Read the repo list from our package.json and requirements files
Storage:    SQLite
Tech stack: Python, GitHub REST API, Slack Incoming Webhooks
```

---

## Example 229

**Intent:**
hey can u make a webhook that when a customer pays in square it adds them to our email list

**Spec:**
```
Type:       Webhook service (Square to email list)
Features:   - Receive payment.updated webhooks from Square
            - Verify the x-square-hmacsha256-signature header
            - Look up the customer's email for completed payments
            - Add the customer to the Klaviyo list if they agreed to marketing
            - Ignore payments without a customer email
API:        REST
            POST /webhooks/square
Tech stack: Node.js, Express, Square API, Klaviyo API
```

---

## Example 230

**Intent:**
isolate our staging and prod networks properly

**Spec:**
```
Type:       Infrastructure setup (network segmentation)
Features:   - Create separate VPCs for staging and production
            - Block all traffic between them by default
            - Put databases in private subnets without internet access
            - Give developers access through a VPN with per-environment rules
            - Log network flows for both VPCs
Tech stack: AWS VPC, security groups, VPC Flow Logs, WireGuard VPN, Terraform
```

---

## Example 231

**Intent:**
slack bot that turns emoji reactions into jira tickets

**Spec:**
```
Type:       Bot (Slack)
Features:   - Create a Jira issue when someone reacts to a message with :ticket:
            - Use the message text as the summary and link back to the message
            - Reply in the thread with the new issue key
            - Pick the Jira project from a channel-to-project mapping
            - Ignore a second reaction on the same message
API:        REST
            POST /slack/events
Storage:    SQLite
Tech stack: Python, Slack Bolt, Jira Cloud REST API
```

---

## Example 232

**Intent:**
create a webhook service that tells our warehouse to ship when a woocommerce order is paid

**Spec:**
```
Type:       Webhook service (WooCommerce to fulfillment)
Data model: Fulfillment(id, woo_order_id, warehouse_ref, status, tracking_number)
Features:   - Receive WooCommerce order.updated webhooks and verify the signature
            - Send paid orders to the warehouse's fulfillment API
            - Receive shipping updates from the warehouse
            - Add the tracking number to the WooCommerce order and mark it completed
            - Retry failed sends with a queue
API:        REST
            POST /webhooks/woocommerce
            POST /webhooks/warehouse
Storage:    PostgreSQL, Redis (queue)
Tech stack: Node.js, Express, BullMQ, WooCommerce REST API
```

---

## Example 233

**Intent:**
backups of our gitlab instance

**Spec:**
```
Type:       Scheduled script (application backup)
Features:   - Run gitlab-backup create every night
            - Back up gitlab.rb and gitlab-secrets.json separately
            - Copy backups to an off-site object storage bucket
            - Keep 14 days of backups
            - Restore to a test VM once a month to prove backups work
Tech stack: GitLab backup tools, rclone, cron
```

---

## Example 234

**Intent:**
discord bot that lets our members verify they own an nft from our collection

**Spec:**
```
Type:       Bot (Discord)
Data model: Verification(id, discord_user_id, wallet_address, verified_at)
Features:   - Send a link to a page where the user signs a message with their wallet
            - Check the signature and the wallet's tokens from the collection
            - Give the Holder role to verified members
            - Re-check holdings every day and remove the role if sold
API:        REST
            GET  /verify?session={id}
            POST /verify/signature
Storage:    PostgreSQL
Tech stack: TypeScript, discord.js, ethers.js, Alchemy NFT API
```

---

## Example 235

**Intent:**
github actions that builds my ios app and sends to testflight

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Run unit tests on every pull request on macOS runners
            - Sign the app with certificates managed by Fastlane match
            - Build and upload to TestFlight on pushes to main
            - Bump the build number automatically
            - Post the build link to Slack
Tech stack: GitHub Actions (macOS), Fastlane, Xcode, App Store Connect API
```

---

## Example 236

**Intent:**
we sell courses on teachable and want new students to automatically get access to our circle community

**Spec:**
```
Type:       Webhook service (Teachable to Circle)
Features:   - Receive Teachable new enrollment webhooks
            - Invite the student to the Circle community with their email
            - Add them to the space for the course they bought
            - Remove access when a refund webhook arrives
            - Log every action for support questions
API:        REST
            POST /webhooks/teachable
Storage:    SQLite
Tech stack: Node.js, Express, Teachable webhooks, Circle Admin API
```

---

## Example 237

**Intent:**
need monitoring for our rabbitmq queues, the consumers sometimes die and messages pile up

**Spec:**
```
Type:       Infrastructure setup (queue monitoring)
Features:   - Collect queue depth, consumer count and message rates from RabbitMQ
            - Alert when a queue has zero consumers
            - Alert when queue depth grows for 10 minutes
            - Show queue metrics on a Grafana dashboard
            - Restart consumer pods automatically when they stop consuming
Tech stack: RabbitMQ Prometheus plugin, Prometheus, Grafana, Kubernetes liveness probes
```

---

## Example 238

**Intent:**
a webhook that receives alerts from our monitoring and makes a phone call if critical

**Spec:**
```
Type:       Webhook service (alert escalation)
Data model: Incident(id, alert_name, severity, status, called_at, acknowledged_at)
Features:   - Receive alerts from Alertmanager webhooks
            - Phone the on-call number for critical alerts
            - Let the person press 1 to acknowledge
            - Call the backup number if not acknowledged within 5 minutes
            - Group alerts with the same name into one incident
API:        REST
            POST /alerts
            POST /voice/ack
Storage:    Redis
Tech stack: Go, Twilio Voice API
```

---

## Example 239

**Intent:**
simple rest api for a blog with posts and comments, in express

**Spec:**
```
Type:       REST API service
Auth:       JWT for the author; comments without login
Data model: Post(id, title, slug, body, published_at)
            Comment(id, post_id -> Post, name, body, approved, created_at)
Features:   - List published posts with pagination
            - Create, edit and delete posts as the author
            - Add comments that wait for approval
            - Approve or delete comments
            - Block comment spam with a rate limit per IP
API:        REST
            GET  /posts
            GET  /posts/{slug}
            POST /posts
            PUT  /posts/{id}
            POST /posts/{id}/comments
            PATCH /comments/{id}
Storage:    MongoDB
Tech stack: Node.js, Express, Mongoose
```

---

## Example 240

**Intent:**
api for my iot weather station to upload readings

**Spec:**
```
Type:       REST API service (sensor data)
Auth:       Device token per station
Data model: Station(id, name, lat, lng, token_hash)
            Reading(id, station_id -> Station, temperature, humidity, pressure, recorded_at)
Features:   - Accept batches of readings from stations
            - Reject readings with impossible values
            - Return the latest reading per station
            - Return hourly averages for a date range
API:        REST
            POST /stations/{id}/readings
            GET  /stations/{id}/latest
            GET  /stations/{id}/hourly?from={date}&to={date}
Storage:    TimescaleDB
Tech stack: Python, FastAPI, TimescaleDB
```

---

## Example 241

**Intent:**
automate offboarding: when someone leaves remove them from google, slack, github and 1password

**Spec:**
```
Type:       Scheduled script (employee offboarding)
Data model: OffboardingRun(id, employee_email, step, status, done_at)
Features:   - Read employees marked as leaving from the HR system each night
            - Suspend the Google Workspace account and move their files to their manager
            - Deactivate the Slack account
            - Remove the user from the GitHub organization
            - Suspend the 1Password account
            - Email IT a checklist of what was done and what failed
Storage:    PostgreSQL
Tech stack: Python, Google Admin SDK, Slack SCIM API, GitHub REST API, 1Password SCIM bridge
```

---

## Example 242

**Intent:**
dear sir i want to make chatbot telegram for my school students can ask exam timetable and results

**Spec:**
```
Type:       Bot (Telegram)
Data model: Student(id, roll_number, name, class, telegram_chat_id)
            Exam(id, class, subject, exam_date)
            Result(id, student_id -> Student, subject, marks)
Features:   - Link a Telegram account to a roll number with a one-time code from the school
            - Show the exam timetable for the student's class
            - Show the student's own results only
            - Send a message when new results are published
Storage:    MySQL
Tech stack: Python, python-telegram-bot, MySQL
```

---

## Example 243

**Intent:**
cdn and image optimization for our ecommerce images

**Spec:**
```
Type:       Infrastructure setup (image CDN)
Features:   - Serve product images through a CDN
            - Resize and convert images to WebP or AVIF on the fly from URL parameters
            - Cache resized images at the edge
            - Keep originals in object storage
            - Purge cached images when a product image changes
Tech stack: Cloudflare Images, Cloudflare R2, Cloudflare CDN
```

---

## Example 244

**Intent:**
backend that lets users connect their google calendar to our app

**Spec:**
```
Type:       REST API service (calendar integration)
Auth:       App session; Google OAuth 2.0 for calendar access
Data model: CalendarConnection(id, user_id, google_email, refresh_token_encrypted, sync_token)
            CalendarEvent(id, connection_id -> CalendarConnection, google_event_id, title, starts_at, ends_at)
Features:   - Connect a Google account with offline access
            - Do a full sync, then incremental syncs with sync tokens
            - Receive push notifications from Google when events change
            - Encrypt refresh tokens at rest
            - Disconnect and delete synced events
API:        REST
            GET  /integrations/google/connect
            GET  /integrations/google/callback
            POST /integrations/google/notifications
            DELETE /integrations/google
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, googleapis
```

---

## Example 245

**Intent:**
alert when my scraper stops getting data

**Spec:**
```
Type:       Scheduled script (pipeline freshness check)
Features:   - Check the newest record time in the scraped data table every hour
            - Alert when no new data has arrived for 3 hours
            - Alert when today's row count is below 50% of the usual daily count
            - Send alerts to email and Telegram
Tech stack: Python, SQLAlchemy, Telegram Bot API, cron
```

---

## Example 246

**Intent:**
we need a bot for our discord that makes temporary voice channels when someone joins a "create" channel

**Spec:**
```
Type:       Bot (Discord)
Data model: TempChannel(id, guild_id, channel_id, owner_id, created_at)
Features:   - Create a new voice channel when a member joins the "Join to create" channel
            - Move the member into the new channel and make them its owner
            - Let the owner rename, lock or set a user limit with commands
            - Delete the channel when it becomes empty
Tech stack: Node.js, discord.js
```

---

## Example 247

**Intent:**
one docker compose with traefik for all my side projects on one vps

**Spec:**
```
Type:       Infrastructure setup (reverse proxy)
Features:   - Run Traefik as the single entry point on ports 80 and 443
            - Route each domain to its project container using labels
            - Get Let's Encrypt certificates automatically for every domain
            - Protect admin dashboards with basic auth
            - Redirect all HTTP traffic to HTTPS
Tech stack: Traefik, Docker Compose, Let's Encrypt
```

---

## Example 248

**Intent:**
build a payment backend for an event ticket site with stripe connect so organizers get paid

**Spec:**
```
Type:       REST API service (marketplace payments)
Auth:       JWT; organizers onboard with Stripe Connect Express
Data model: Organizer(id, name, stripe_account_id, payouts_enabled)
            Event(id, organizer_id -> Organizer, title, price, capacity)
            Ticket(id, event_id -> Event, buyer_email, payment_intent_id, status)
Features:   - Onboard organizers through Stripe Connect account links
            - Take payment for tickets with an application fee for the platform
            - Hold seats for 10 minutes during checkout
            - Issue tickets after payment_intent.succeeded webhooks
            - Refund tickets when an event is cancelled
API:        REST
            POST /organizers/onboard
            POST /events/{id}/checkout
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Stripe Connect, Redis
```

---

## Example 249

**Intent:**
in my company we has many cronjob scripts in python on one old server. i want move to cloud with schedule and see if they fail

**Spec:**
```
Type:       Infrastructure setup (scheduled jobs migration)
Features:   - Package each script in a container image
            - Run the scripts on a schedule with Cloud Run jobs and Cloud Scheduler
            - Store passwords and keys in Secret Manager
            - Send logs to Cloud Logging
            - Alert by email when a job run fails
Tech stack: Google Cloud Run jobs, Cloud Scheduler, Secret Manager, Cloud Monitoring, Docker
```

---

## Example 250

**Intent:**
verify webhooks are from github before running my deploy script

**Spec:**
```
Type:       Webhook service (deploy trigger)
Features:   - Receive GitHub push events
            - Verify the X-Hub-Signature-256 HMAC with a constant-time comparison
            - Run the deploy script only for pushes to the production branch
            - Stop two deploys from running at the same time with a lock
            - Return 202 right away and run the deploy in the background
API:        REST
            POST /hooks/deploy
Tech stack: Go, net/http, os/exec
```

---

## Example 251

**Intent:**
patreon patrons get a role in discord automaticly

**Spec:**
```
Type:       Bot (Discord, Patreon integration)
Data model: PatronLink(id, patreon_user_id, discord_user_id, tier, status)
Features:   - Let members link their Patreon account with OAuth from a /link command
            - Give the Discord role that matches their Patreon tier
            - Receive Patreon members:pledge webhooks and verify the X-Patreon-Signature
            - Remove roles when a pledge is deleted or payment fails
            - Re-check all patrons every night in case a webhook was missed
API:        REST
            GET  /patreon/callback
            POST /webhooks/patreon
Storage:    PostgreSQL
Tech stack: Python, discord.py, Patreon API v2, FastAPI
```

---

## Example 252

**Intent:**
Facebook lead ads should go into our CRM right away, the sales team calls leads faster that way.

**Spec:**
```
Type:       Webhook service (Facebook Lead Ads to CRM)
Data model: LeadSync(id, leadgen_id, form_id, crm_lead_id, created_at)
Features:   - Receive leadgen webhooks from the Facebook page subscription
            - Verify the X-Hub-Signature-256 header with the app secret
            - Fetch the full lead data from the Graph API
            - Create the lead in Pipedrive with the ad and form name as source
            - Text the assigned salesperson the lead's name and phone
API:        REST
            GET  /webhooks/facebook (verification)
            POST /webhooks/facebook
Storage:    PostgreSQL
Tech stack: Node.js, Express, Facebook Graph API, Pipedrive API, Twilio SMS
```

---

## Example 253

**Intent:**
passkeys login for our website backend

**Spec:**
```
Type:       REST API service (WebAuthn passkeys)
Auth:       Passkeys (WebAuthn), with email magic link as fallback
Data model: User(id, email, created_at)
            Passkey(id, user_id -> User, credential_id, public_key, sign_count, transports, created_at)
Features:   - Start and finish passkey registration ceremonies
            - Start and finish passkey login with a server-side challenge
            - Check the origin, relying party ID and signature counter
            - Let users list and remove their passkeys
            - Fall back to an email magic link on devices without passkeys
API:        REST
            POST /webauthn/register/options
            POST /webauthn/register/verify
            POST /webauthn/login/options
            POST /webauthn/login/verify
Storage:    PostgreSQL, Redis (challenges)
Tech stack: TypeScript, Express, SimpleWebAuthn
```

---

## Example 254

**Intent:**
jenkins pipeline for our java maven project

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Define the pipeline in a Jenkinsfile in the repository
            - Build and run unit tests with Maven on every branch
            - Run SonarQube analysis and fail on the quality gate
            - Publish the JAR to Nexus on the main branch
            - Deploy to the test server and run integration tests
            - Email the committer when a build breaks
Tech stack: Jenkins, Maven, SonarQube, Nexus Repository
```

---

## Example 255

**Intent:**
i want a telegram bot that kicks spam bots out of my group with a captcha

**Spec:**
```
Type:       Bot (Telegram)
Data model: PendingMember(chat_id, user_id, answer, joined_at)
Features:   - Mute new members when they join
            - Ask them to press the right button in a simple captcha within 2 minutes
            - Unmute members who pass
            - Ban members who fail or don't answer
            - Delete messages with links from members who joined less than a day ago
Storage:    Redis
Tech stack: Python, aiogram, Redis
```

---

## Example 256

**Intent:**
apple in app purchase server notifications for our subscription app

**Spec:**
```
Type:       Webhook service (App Store Server Notifications)
Data model: Subscription(id, user_id, original_transaction_id, product_id, status, expires_at)
            AppleNotification(id, notification_uuid, type, subtype, received_at)
Features:   - Receive App Store Server Notifications V2
            - Verify the signed JWS payload with Apple's certificate chain
            - Update subscription status on renewals, expirations, refunds and grace periods
            - Skip notifications already processed by UUID
            - Give or remove premium access for the linked user
API:        REST
            POST /webhooks/apple
Storage:    PostgreSQL
Tech stack: Swift, Vapor, App Store Server Library
```

---

## Example 257

**Intent:**
chat ops bot in mattermost to restart services

**Spec:**
```
Type:       Bot (Mattermost)
Features:   - Restart a service with /restart <service> <env>
            - Show service status with /status
            - Ask for confirmation before acting in production
            - Allow only members of the ops team
            - Log every command with user and time
API:        REST
            POST /mattermost/commands
Tech stack: Go, Mattermost API, Kubernetes client-go
```

---

## Example 258

**Intent:**
argocd gitops for our kubernetes apps

**Spec:**
```
Type:       Infrastructure setup (GitOps)
Features:   - Keep all Kubernetes manifests in one Git repository
            - Install Argo CD and sync each app from the repository automatically
            - Use separate folders for staging and production with Kustomize overlays
            - Require a pull request to change production
            - Show out-of-sync and unhealthy apps in Argo CD and alert in Slack
Tech stack: Argo CD, Kubernetes, Kustomize, GitHub
```

---

## Example 259

**Intent:**
hi i do dropshipping and printful makes my shirts. when printful ships i want the customer to get a nice email with tracking

**Spec:**
```
Type:       Webhook service (Printful shipping emails)
Data model: ShipmentEmail(id, printful_order_id, customer_email, tracking_url, sent_at)
Features:   - Receive Printful package_shipped webhooks
            - Look up the customer's email from the store order
            - Send a branded email with carrier and tracking link
            - Send only one email per shipment
            - Email the store owner if a package_returned event arrives
API:        REST
            POST /webhooks/printful
Storage:    SQLite
Tech stack: Node.js, Express, Printful API, Resend email API
```

---

## Example 260

**Intent:**
api that gives shipping rates from several carriers so our checkout shows the cheapest

**Spec:**
```
Type:       REST API service (shipping rates)
Auth:       Internal API key
Data model: RateQuote(id, from_zip, to_zip, weight_g, carrier, service, price, days, quoted_at)
Features:   - Accept origin, destination and parcel size and weight
            - Get rates from several carriers at once
            - Sort options by price and show delivery days
            - Cache identical quotes for 30 minutes
            - Return the remaining carriers if one times out
API:        REST
            POST /rates
Storage:    Redis
Tech stack: Python, FastAPI, EasyPost API, asyncio
```

---

## Example 261

**Intent:**
discord giveaway bot

**Spec:**
```
Type:       Bot (Discord)
Data model: Giveaway(id, guild_id, channel_id, message_id, prize, winners_count, ends_at, ended)
            Entry(giveaway_id -> Giveaway, user_id)
Features:   - Start a giveaway with /giveaway start <prize> <duration> <winners>
            - Let members enter with a button
            - Pick random winners when time is up and announce them
            - Reroll a winner with /giveaway reroll
            - Require a minimum account age to enter
Storage:    PostgreSQL
Tech stack: Node.js, discord.js
```

---

## Example 262

**Intent:**
we're getting a lot of chargebacks. I'd like to be alerted in Slack whenever a dispute opens in Stripe, with the evidence deadline, and have the order details gathered so we can respond fast.

**Spec:**
```
Type:       Webhook service (Stripe disputes)
Data model: Dispute(id, stripe_dispute_id, charge_id, amount, reason, evidence_due_by, status)
Features:   - Receive charge.dispute.created and charge.dispute.closed events
            - Verify the Stripe-Signature header
            - Find the related order, shipping tracking and customer emails
            - Post a Slack alert with amount, reason, deadline and order details
            - Remind the channel 2 days before the evidence deadline
            - Post the final outcome when the dispute closes
API:        REST
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Stripe SDK, Slack Web API, APScheduler
```

---

## Example 263

**Intent:**
bitbucket pipelines for php app to run phpunit and deploy

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Run composer install and PHPUnit on every pull request
            - Run PHPStan static analysis
            - Deploy to production with Deployer on merges to master
            - Keep the last 5 releases for fast rollback
Tech stack: Bitbucket Pipelines, PHPUnit, PHPStan, Deployer
```

---

## Example 264

**Intent:**
backend for web push notifications from our blog

**Spec:**
```
Type:       REST API service (web push)
Auth:       Admin token for sending
Data model: PushSubscription(id, endpoint, p256dh, auth, topics, created_at)
Features:   - Store browser push subscriptions from the service worker
            - Send a notification to all subscribers when a post is published
            - Let readers pick topics to follow
            - Remove subscriptions that return 404 or 410
            - Sign push messages with VAPID keys
API:        REST
            POST /push/subscribe
            POST /push/unsubscribe
            POST /push/send
Storage:    PostgreSQL
Tech stack: Node.js, Express, web-push
```

---

## Example 265

**Intent:**
wireguard vpn so our remote team can reach the office servers

**Spec:**
```
Type:       Infrastructure setup (VPN)
Features:   - Run a WireGuard server on a small cloud VM
            - Create one key pair and config per employee
            - Route only office server subnets through the VPN (split tunnel)
            - Show a QR code for setting up phones
            - Revoke a person's access by removing their peer
Tech stack: WireGuard, wg-easy, Ubuntu
```

---

## Example 266

**Intent:**
i have a youtube channel and want my discord to get a post when i upload

**Spec:**
```
Type:       Bot (Discord)
Features:   - Subscribe to the channel's upload feed through YouTube PubSubHubbub
            - Verify the hub's subscription challenge
            - Post the video title, thumbnail and link in the announcements channel
            - Renew the subscription before it expires
            - Skip videos that are updated rather than new
API:        REST
            GET  /youtube/callback
            POST /youtube/callback
Tech stack: Python, FastAPI, discord.py (webhook), YouTube PubSubHubbub
```

---

## Example 267

**Intent:**
sync users from clerk to our database

**Spec:**
```
Type:       Webhook service (Clerk user sync)
Data model: User(id, clerk_user_id, email, first_name, last_name, deleted_at)
Features:   - Receive user.created, user.updated and user.deleted events from Clerk
            - Verify the Svix signature headers
            - Create or update the user row
            - Soft-delete users when deleted in Clerk
API:        REST
            POST /api/webhooks/clerk
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js route handler, Svix, Drizzle ORM
```

---

## Example 268

**Intent:**
our nginx logs show attacks sometimes, alert me if lots of 404s from one ip

**Spec:**
```
Type:       Scheduled script (log anomaly alert)
Features:   - Read new nginx access log lines every minute
            - Count 404 responses per IP over 5 minutes
            - Alert by email when one IP passes 100 404s
            - Add the IP to a block list file used by nginx
            - Unblock IPs after 24 hours
Tech stack: Python, cron, nginx deny list
```

---

## Example 269

**Intent:**
graphql api for a social app: posts, follows, feed

**Spec:**
```
Type:       GraphQL API service
Auth:       JWT bearer tokens
Data model: User(id, username, bio)
            Follow(follower_id -> User, followee_id -> User, created_at)
            Post(id, author_id -> User, text, created_at)
            Like(user_id -> User, post_id -> Post)
Features:   - Query a home feed of posts from followed users with cursor pagination
            - Create posts and like or unlike them
            - Follow and unfollow users
            - Subscribe to new likes on your own posts
            - Rate limit mutations per user
API:        GraphQL
            POST /graphql
            WS   /graphql
Storage:    PostgreSQL, Redis (feed cache)
Tech stack: Go, gqlgen, PostgreSQL, Redis
```

---

## Example 270

**Intent:**
copy production database to staging every week with personal data scrambled

**Spec:**
```
Type:       Scheduled script (database anonymization)
Features:   - Restore last night's production backup into a temporary database
            - Replace names, emails and phone numbers with fake values
            - Keep relations between tables working after the changes
            - Replace the staging database with the anonymized copy
            - Notify the team in Slack when staging is refreshed
Tech stack: Python, Faker, pg_dump, pg_restore, cron
```

---

## Example 271

**Intent:**
customer support chat for our app using intercom, and new conversations tagged "bug" should create a linear issue

**Spec:**
```
Type:       Webhook service (Intercom to Linear)
Data model: IssueLink(id, intercom_conversation_id, linear_issue_id)
Features:   - Receive Intercom conversation.admin.tagged webhooks
            - Verify the X-Hub-Signature header
            - Create a Linear issue with the conversation summary and link when tagged "bug"
            - Add a note in Intercom with the Linear issue link
            - Notify the customer in Intercom when the Linear issue is marked done
API:        REST
            POST /webhooks/intercom
            POST /webhooks/linear
Storage:    PostgreSQL
Tech stack: TypeScript, Hono, Intercom API, Linear GraphQL API
```

---

## Example 272

**Intent:**
deploy a python api as serverless on aws lambda with api gateway

**Spec:**
```
Type:       Infrastructure setup (serverless deployment)
Features:   - Package the FastAPI app for Lambda with an ASGI adapter
            - Expose it through API Gateway HTTP API with a custom domain
            - Store config in SSM Parameter Store
            - Set up separate dev and prod stages
            - Deploy with one command from CI
Tech stack: AWS SAM, AWS Lambda, API Gateway, Mangum, GitHub Actions
```

---

## Example 273

**Intent:**
kudos bot for slack

**Spec:**
```
Type:       Bot (Slack)
Data model: Kudos(id, from_user, to_user, message, created_at)
Features:   - Give kudos with /kudos @person message
            - Post the kudos in a #kudos channel
            - Limit each person to 5 kudos per day
            - Show a monthly leaderboard
            - Send a DM to the person who received kudos
API:        REST
            POST /slack/commands
Storage:    SQLite
Tech stack: Python, Slack Bolt
```

---

## Example 274

**Intent:**
msg me on whatsapp when my aws bill passes 100 dollars

**Spec:**
```
Type:       Scheduled script (billing alert)
Features:   - Check month-to-date AWS cost every morning with Cost Explorer
            - Send a WhatsApp message when cost passes 100 USD
            - Send another message for every extra 50 USD
            - Include the top 3 services by cost
Tech stack: Python, boto3 (Cost Explorer), Twilio WhatsApp API, AWS Lambda
```

---

## Example 275

**Intent:**
We are a property management company and maintenance requests come by email, phone and WhatsApp. Can you design a backend that puts them all in one queue and assigns them to the right contractor?

**Spec:**
```
Type:       REST API service (maintenance requests)
Auth:       Staff login; contractors log in with a magic link
Data model: Property(id, address, owner_id)
            Request(id, property_id -> Property, source, description, category, priority, status, contractor_id)
            Contractor(id, name, phone, categories)
Features:   - Create requests from inbound emails, WhatsApp messages and phone notes
            - Detect the category and urgency from the description
            - Assign the request to a contractor for that category
            - Notify the contractor and the tenant at each status change
            - Show open requests per property
API:        REST
            POST /inbound/email
            POST /webhooks/whatsapp
            GET  /requests
            PATCH /requests/{id}
Storage:    PostgreSQL
Tech stack: Python, Django REST Framework, WhatsApp Cloud API, Mailgun Routes
```

---

## Example 276

**Intent:**
auth service with google and apple sign in for our mobile app

**Spec:**
```
Type:       REST API service (social login)
Auth:       Sign in with Google and Sign in with Apple, then app JWTs
Data model: User(id, email, name, created_at)
            Identity(id, user_id -> User, provider, provider_user_id)
Features:   - Verify Google and Apple ID tokens on the server
            - Link both providers to one user when emails match
            - Handle Apple's private relay email addresses
            - Issue app access and refresh tokens
            - Delete the account and revoke Apple tokens on request
API:        REST
            POST /auth/google
            POST /auth/apple
            POST /auth/refresh
            DELETE /account
Storage:    PostgreSQL
Tech stack: Kotlin, Ktor, Google API Client, Nimbus JOSE + JWT
```

---

## Example 277

**Intent:**
uptime check of our office internet and the printers lol

**Spec:**
```
Type:       Scheduled script (network device monitoring)
Data model: Device(id, name, ip, type)
            PingResult(id, device_id -> Device, up, latency_ms, checked_at)
Features:   - Ping the router, printers and internet every minute
            - Mark a device down after 3 missed pings
            - Send a Teams message when a device goes down or comes back
            - Show a simple web page with current status
Storage:    SQLite
Tech stack: Python, icmplib, Flask, Microsoft Teams webhook
```

---

## Example 278

**Intent:**
a docusign completed envelope should save the pdf to google drive and update the deal in hubspot

**Spec:**
```
Type:       Webhook service (DocuSign to Drive and HubSpot)
Features:   - Receive DocuSign Connect envelope-completed events
            - Verify the HMAC signature on each event
            - Download the signed PDF and save it to the client's Google Drive folder
            - Move the HubSpot deal to the Contract Signed stage
            - Retry failed steps without repeating finished ones
API:        REST
            POST /webhooks/docusign
Storage:    PostgreSQL (step status)
Tech stack: Python, FastAPI, DocuSign eSignature API, Google Drive API, HubSpot API
```

---

## Example 279

**Intent:**
k3s cluster at home on 3 raspberry pis

**Spec:**
```
Type:       Infrastructure setup (home Kubernetes)
Features:   - Install k3s with one server and two agent nodes
            - Use MetalLB to give services local IP addresses
            - Store volumes on the NAS with the NFS provisioner
            - Expose apps through Traefik with local DNS names
            - Back up cluster state and volumes every night
Tech stack: k3s, MetalLB, NFS subdir provisioner, Traefik, Velero
```

---

## Example 280

**Intent:**
email digest of notifications instead of 50 emails a day

**Spec:**
```
Type:       Scheduled script (notification digest)
Data model: Notification(id, user_id, type, text, link, created_at, digested_at)
            DigestPreference(user_id, frequency, send_hour)
Features:   - Save notifications instead of emailing each one
            - Send a daily or weekly digest at the user's chosen hour
            - Group notifications by type in the email
            - Skip users with nothing new
            - Send urgent notification types right away
Storage:    PostgreSQL
Tech stack: Ruby, Rails, Sidekiq-cron, Action Mailer
```

---

## Example 281

**Intent:**
we use azure devops and want pipelines for our .net api with deploy to azure app service

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Build and test the .NET solution on every pull request
            - Publish the build output as a pipeline artifact
            - Deploy to a staging slot on merges to main
            - Swap staging and production slots after approval
            - Run EF Core migrations during the release stage
Tech stack: Azure DevOps Pipelines, .NET, Azure App Service deployment slots
```

---

## Example 282

**Intent:**
bot telegram that translate messages in my group between english and russian

**Spec:**
```
Type:       Bot (Telegram)
Features:   - Detect the language of each message in the group
            - Reply with a translation into the other language
            - Skip short messages, links and commands
            - Turn translation on or off per group with /translate on
Tech stack: Python, aiogram, DeepL API
```

---

## Example 283

**Intent:**
i have a webflow site and want form submissions to land in airtable and slack

**Spec:**
```
Type:       Webhook service (Webflow forms)
Features:   - Receive Webflow form_submission webhooks
            - Verify the x-webflow-signature header
            - Create an Airtable record with all form fields
            - Post a short summary to a Slack channel
            - Route each form to a different Airtable table by form name
API:        REST
            POST /webhooks/webflow
Tech stack: Node.js, Netlify Functions, Airtable API, Slack Incoming Webhooks
```

---

## Example 284

**Intent:**
secure our api with mutual tls between services

**Spec:**
```
Type:       Infrastructure setup (service mesh)
Features:   - Install a service mesh in the Kubernetes cluster
            - Turn on strict mutual TLS between all services
            - Rotate service certificates automatically
            - Allow only listed services to call each other with authorization policies
            - Show service-to-service traffic in a dashboard
Tech stack: Istio, Kubernetes, Kiali
```

---

## Example 285

**Intent:**
ko-fi donations should make a thank you post in our discord

**Spec:**
```
Type:       Webhook service (Ko-fi to Discord)
Features:   - Receive Ko-fi webhook posts
            - Check the verification token in the payload
            - Post the donor name, amount and message to a Discord channel
            - Hide the amount and name for private donations
            - Give the supporter role if the donor linked their Discord name
API:        REST
            POST /webhooks/kofi
Tech stack: Python, Flask, Discord webhooks, discord.py
```

---

## Example 286

**Intent:**
elk stack to search logs from our docker containers

**Spec:**
```
Type:       Infrastructure setup (log aggregation)
Features:   - Collect logs from all Docker containers with Filebeat
            - Add container name and image labels to each log
            - Store logs in Elasticsearch
            - Search and build dashboards in Kibana
            - Delete logs older than 30 days
Tech stack: Elasticsearch, Logstash, Kibana, Filebeat, Docker Compose
```

---

## Example 287

**Intent:**
webhook to start a build when our cms content changes

**Spec:**
```
Type:       Webhook service (CMS to static site build)
Features:   - Receive entry.publish and entry.unpublish webhooks from the CMS
            - Check a secret header on each request
            - Wait 2 minutes and combine many changes into one build (debounce)
            - Trigger a new build through the hosting provider's build hook
            - Post build status to Slack
API:        REST
            POST /webhooks/cms
Storage:    Redis
Tech stack: Node.js, Contentful webhooks, Vercel deploy hooks
```

---

## Example 288

**Intent:**
let users sign in to our app with their microsoft work account

**Spec:**
```
Type:       REST API service (enterprise login)
Auth:       Microsoft Entra ID OpenID Connect (multi-tenant)
Data model: Tenant(id, entra_tenant_id, name, allowed)
            User(id, tenant_id -> Tenant, entra_object_id, email, name)
Features:   - Redirect users to Microsoft sign-in
            - Validate ID tokens and the issuer tenant
            - Allow only tenants approved by an admin
            - Create users on first sign-in
API:        REST
            GET  /auth/microsoft
            GET  /auth/microsoft/callback
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Microsoft.Identity.Web
```

---

## Example 289

**Intent:**
alert when disk space on any of our 30 linux servers is low

**Spec:**
```
Type:       Infrastructure setup (disk monitoring)
Features:   - Install a metrics agent on every server
            - Alert at 80% and again at 90% disk usage
            - Predict when a disk will be full and alert 24 hours before
            - Send alerts to Opsgenie
            - Show disk usage for all servers on one dashboard
Tech stack: Prometheus, node_exporter, Alertmanager, Opsgenie, Grafana
```

---

## Example 290

**Intent:**
wanna make a twitter (x) bot that posts a random quote every day

**Spec:**
```
Type:       Bot (X/Twitter)
Data model: Quote(id, text, author, posted_at)
Features:   - Pick a random quote not posted in the last 90 days
            - Post it every day at 10:00
            - Add the author's name and hashtags
            - Mark the quote as posted
Storage:    SQLite
Tech stack: Python, Tweepy (X API v2), cron
```

---

## Example 291

**Intent:**
razorpay payment gateway backend for our indian online store

**Spec:**
```
Type:       REST API service (payments)
Auth:       Customer session from the store
Data model: Order(id, customer_id, amount_paise, status, razorpay_order_id)
            Payment(id, order_id -> Order, razorpay_payment_id, method, status, captured_at)
Features:   - Create a Razorpay order before checkout opens
            - Verify the payment signature returned by Razorpay Checkout
            - Confirm captures with payment.captured webhooks and the webhook secret
            - Refund full or partial amounts
            - Ignore duplicate webhook events by event ID
API:        REST
            POST /payments/orders
            POST /payments/verify
            POST /payments/{id}/refund
            POST /webhooks/razorpay
Storage:    MySQL
Tech stack: Node.js, Express, Razorpay Node SDK
```

---

## Example 292

**Intent:**
my company website is on a single server and if it dies we lose everything. i read about disaster recovery and got scared. we're on hetzner. what would a sensible setup be for a small budget, we can accept maybe half a day of downtime

**Spec:**
```
Type:       Infrastructure setup (disaster recovery)
Features:   - Take nightly encrypted backups of the database and uploaded files with restic
            - Store backups in a storage box in a different Hetzner location
            - Keep server setup in an Ansible playbook so a new server can be built quickly
            - Take weekly server snapshots through the Hetzner Cloud API
            - Write and test a step-by-step restore runbook twice a year
            - Alert when a backup is missing or older than 26 hours
Tech stack: Hetzner Cloud, Hetzner Storage Box, restic, Ansible, Healthchecks.io
```

---

## Example 293

**Intent:**
a bot in discord that reminds people of birthdays

**Spec:**
```
Type:       Bot (Discord)
Data model: Birthday(guild_id, user_id, month, day, timezone)
Features:   - Save a birthday with /birthday set <month> <day>
            - Post a birthday message at midnight in the member's time zone
            - Give a Birthday role for the day
            - List upcoming birthdays with /birthday list
Storage:    SQLite
Tech stack: Python, discord.py, APScheduler
```

---

## Example 294

**Intent:**
webhooks from strava to give our running club points

**Spec:**
```
Type:       Webhook service (Strava)
Data model: Runner(id, strava_athlete_id, name, access_token, refresh_token, points)
            Activity(id, strava_activity_id, runner_id -> Runner, distance_m, moving_time_s, started_at)
Features:   - Let members connect Strava with OAuth
            - Answer Strava's subscription validation request
            - Fetch new activities when an activity create event arrives
            - Give 1 point per km for runs only
            - Post a weekly club leaderboard to the club's group chat
API:        REST
            GET  /strava/callback
            GET  /webhooks/strava
            POST /webhooks/strava
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Strava API v3
```

---

## Example 295

**Intent:**
terraform plan comments on pull requests

**Spec:**
```
Type:       Infrastructure setup (Terraform automation)
Features:   - Run terraform plan for changed folders on every pull request
            - Comment the plan output on the pull request
            - Apply the plan after a reviewer comments "atlantis apply"
            - Lock a workspace while a pull request is changing it
            - Block applies without approval
Tech stack: Atlantis, Terraform, GitHub, AWS
```

---

## Example 296

**Intent:**
api for our library so the app can search books and reserve them

**Spec:**
```
Type:       REST API service (library)
Auth:       Library card number + PIN, JWT sessions
Data model: Book(id, isbn, title, author, copies_total)
            Copy(id, book_id -> Book, branch, status)
            Reservation(id, book_id -> Book, member_id, status, ready_at, expires_at)
Features:   - Search books by title, author or ISBN
            - Show which branches have copies available
            - Reserve a book and join the waiting list
            - Notify members by push when their reservation is ready
            - Cancel reservations not picked up within 5 days
API:        REST
            GET  /books?q={query}
            GET  /books/{id}/availability
            POST /reservations
            DELETE /reservations/{id}
Storage:    PostgreSQL
Tech stack: Java, Quarkus, Hibernate
```

---

## Example 297

**Intent:**
hey so like i want my crypto payments on my site with coinbase commerce and when it confirms send the product

**Spec:**
```
Type:       Webhook service (Coinbase Commerce)
Data model: CryptoCharge(id, charge_code, order_id, status, confirmed_at)
Features:   - Create a Coinbase Commerce charge for each order
            - Receive charge:confirmed and charge:failed webhooks
            - Verify the X-CC-Webhook-Signature header
            - Send the digital product by email after confirmation
            - Mark underpaid charges for manual review
API:        REST
            POST /checkout/crypto
            POST /webhooks/coinbase
Storage:    PostgreSQL
Tech stack: Node.js, Express, Coinbase Commerce API
```

---

## Example 298

**Intent:**
watch our kafka consumers lag

**Spec:**
```
Type:       Infrastructure setup (Kafka monitoring)
Features:   - Export consumer group lag per topic and partition
            - Alert when lag grows for more than 10 minutes
            - Alert when a consumer group has no active members
            - Show broker health and throughput on Grafana dashboards
Tech stack: Kafka, kafka-lag-exporter, Prometheus, Grafana
```

---

## Example 299

**Intent:**
when zoom recording is ready upload it to our google drive and post link in slack

**Spec:**
```
Type:       Webhook service (Zoom to Google Drive)
Features:   - Receive recording.completed webhooks from Zoom
            - Answer Zoom's endpoint URL validation and check the signature
            - Download the MP4 using the download token
            - Upload it to a Drive folder named by meeting topic and date
            - Post the Drive link to Slack and delete the cloud recording from Zoom
API:        REST
            POST /webhooks/zoom
Tech stack: Python, FastAPI, Zoom API, Google Drive API, Slack Web API
```

---

## Example 300

**Intent:**
make api with nestjs for multi tenant saas, every company has own users and data seperated

**Spec:**
```
Type:       REST API service (multi-tenant)
Auth:       JWT containing tenant ID and role
Data model: Tenant(id, name, plan, created_at)
            User(id, tenant_id -> Tenant, email, role)
            Project(id, tenant_id -> Tenant, name)
Features:   - Scope every query by the tenant ID from the token
            - Enforce isolation in the database with row-level security
            - Invite users to a tenant by email
            - Limit features by the tenant's plan
            - Let tenant admins manage roles
API:        REST
            POST /tenants
            POST /tenants/{id}/invites
            GET  /projects
            POST /projects
Storage:    PostgreSQL (row-level security)
Tech stack: TypeScript, NestJS, Prisma, PostgreSQL
```

---

## Example 301

**Intent:**
uptime for game servers

**Spec:**
```
Type:       Scheduled script (game server monitoring)
Data model: GameServer(id, name, game, host, port)
Features:   - Query each game server with its game's status protocol every minute
            - Record player count and ping
            - Post to Discord when a server goes offline or comes back
            - Show a status board with player counts
Storage:    SQLite
Tech stack: Python, python-a2s (Steam query), Discord webhooks
```

---

## Example 302

**Intent:**
preview environment for every pull request on kubernetes

**Spec:**
```
Type:       Infrastructure setup (preview environments)
Features:   - Create a namespace for each open pull request
            - Deploy the branch's images with a Helm chart into that namespace
            - Give each preview its own URL like pr-123.preview.example.com
            - Seed a small test database for the preview
            - Delete the namespace when the pull request closes
Tech stack: GitHub Actions, Kubernetes, Helm, external-dns, cert-manager
```

---

## Example 303

**Intent:**
telegram bot for my gym so members book classes

**Spec:**
```
Type:       Bot (Telegram)
Data model: GymClass(id, name, trainer, starts_at, capacity)
            ClassBooking(id, class_id -> GymClass, chat_id, member_name, status)
Features:   - Show this week's classes with free spots
            - Book a spot with a button
            - Put members on a waiting list when the class is full
            - Move the first waiting member up when someone cancels
            - Remind members 2 hours before class
Storage:    PostgreSQL
Tech stack: Python, python-telegram-bot, APScheduler
```

---

## Example 304

**Intent:**
store api keys of third party services per customer encrypted

**Spec:**
```
Type:       REST API service (credential vault)
Auth:       Internal service mTLS
Data model: Credential(id, customer_id, provider, ciphertext, key_version, created_at, rotated_at)
Features:   - Encrypt each credential with a data key from a key management service (envelope encryption)
            - Return decrypted credentials only to allowed services
            - Rotate the master key and re-encrypt data keys
            - Never write plaintext secrets to logs
            - Log every read with the calling service
API:        REST
            POST /credentials
            GET  /credentials/{id}
            DELETE /credentials/{id}
Storage:    PostgreSQL
Tech stack: Go, AWS KMS, PostgreSQL
```

---

## Example 305

**Intent:**
nightly backup sql server to azure blob

**Spec:**
```
Type:       Scheduled script (database backup)
Features:   - Run full SQL Server backups every night and log backups every 15 minutes
            - Back up directly to Azure Blob Storage with BACKUP TO URL
            - Use compression and checksums
            - Delete backups older than 35 days
            - Email the DBA when a backup job fails
Storage:    Azure Blob Storage
Tech stack: SQL Server Agent, T-SQL, Ola Hallengren maintenance scripts
```

---

## Example 306

**Intent:**
slack incident bot: /incident creates channel, invites people, keeps timeline

**Spec:**
```
Type:       Bot (Slack incident management)
Data model: Incident(id, title, severity, channel_id, commander_id, status, started_at, resolved_at)
            TimelineEntry(id, incident_id -> Incident, author_id, text, created_at)
Features:   - Start an incident with /incident <title> and pick a severity
            - Create a dedicated channel and invite the on-call team
            - Save pinned messages and commands to the timeline
            - Post status updates to a company-wide channel
            - Create a postmortem doc from the timeline when resolved
API:        REST
            POST /slack/commands
            POST /slack/events
Storage:    PostgreSQL
Tech stack: Python, Slack Bolt, Google Docs API
```

---

## Example 307

**Intent:**
shopify order -> shipstation, then tracking back to shopify

**Spec:**
```
Type:       Webhook service (Shopify and ShipStation)
Features:   - Receive Shopify orders/paid webhooks and verify the HMAC
            - Create the order in ShipStation with items and address
            - Receive ShipStation SHIP_NOTIFY webhooks
            - Fetch the shipment and create a Shopify fulfillment with the tracking number
            - Skip orders already sent
API:        REST
            POST /webhooks/shopify
            POST /webhooks/shipstation
Storage:    Redis (processed IDs)
Tech stack: Node.js, Express, ShipStation API, Shopify Admin API
```

---

## Example 308

**Intent:**
im building a saas and i keep hearing about soc2. for the infra part i want proper logging of who accesses what, backups, alerts on weird stuff. we're on aws and use github

**Spec:**
```
Type:       Infrastructure setup (security and compliance baseline)
Features:   - Turn on CloudTrail in all regions with log file validation
            - Turn on GuardDuty and Security Hub and send findings to Slack
            - Enforce encrypted, backed-up RDS and S3 with AWS Config rules
            - Require pull request reviews and signed commits on GitHub
            - Run AWS Backup plans with cross-region copies
            - Keep audit logs for 1 year in a separate account
Tech stack: AWS CloudTrail, GuardDuty, Security Hub, AWS Config, AWS Backup, Terraform, GitHub
```

---

## Example 309

**Intent:**
telegram bot convert voice messages to text

**Spec:**
```
Type:       Bot (Telegram)
Features:   - Receive voice messages in private chats and groups
            - Download and convert the audio to a supported format
            - Transcribe the speech and reply with the text
            - Detect the spoken language automatically
            - Limit transcriptions to 5 minutes per message
Tech stack: Python, aiogram, ffmpeg, OpenAI Whisper (self-hosted)
```

---

## Example 310

**Intent:**
notification preferences service so users choose email, sms or push per type

**Spec:**
```
Type:       REST API service (notification preferences)
Auth:       JWT for users; service token for internal reads
Data model: Preference(user_id, notification_type, email, sms, push)
            QuietHours(user_id, start_time, end_time, timezone)
Features:   - Return a user's preferences for every notification type
            - Let users change each channel per type
            - Answer "which channels for this user and type" for other services
            - Respect quiet hours by delaying non-urgent notifications
            - Add one-click unsubscribe links for email
API:        REST
            GET  /me/preferences
            PUT  /me/preferences
            GET  /internal/users/{id}/channels?type={type}
Storage:    PostgreSQL, Redis (cache)
Tech stack: Python, FastAPI
```

---

## Example 311

**Intent:**
deploy laravel to forge or something when i push to github

**Spec:**
```
Type:       Infrastructure setup (deployment)
Features:   - Connect the GitHub repository to a Laravel Forge server
            - Deploy automatically when main is pushed
            - Run composer install, migrations and cache commands in the deploy script
            - Restart queue workers after each deploy
            - Send deploy notifications to Slack
Tech stack: Laravel Forge, GitHub, PHP, Laravel Horizon
```

---

## Example 312

**Intent:**
api for qr code menus in restaurants

**Spec:**
```
Type:       REST API service (digital menus)
Auth:       Owner login (email + password)
Data model: Restaurant(id, name, slug, owner_id)
            MenuItem(id, restaurant_id -> Restaurant, name, description, price, category, available)
Features:   - Create and edit menu items and categories
            - Generate a QR code that links to the restaurant's menu page
            - Mark items as sold out instantly
            - Return the public menu as JSON for the menu page
API:        REST
            GET  /r/{slug}/menu
            POST /menu-items
            PATCH /menu-items/{id}
            GET  /restaurants/{id}/qr.png
Storage:    PostgreSQL
Tech stack: Ruby, Rails API, rqrcode
```

---

## Example 313

**Intent:**
github webhook to auto deploy hugo site to s3

**Spec:**
```
Type:       Infrastructure setup (static site deployment)
Features:   - Build the Hugo site on pushes to main
            - Sync the output to an S3 bucket and delete removed files
            - Invalidate the CloudFront cache after upload
            - Use GitHub OIDC to get short-lived AWS credentials
Tech stack: GitHub Actions, Hugo, Amazon S3, CloudFront, AWS IAM OIDC
```

---

## Example 314

**Intent:**
Our sales reps want to know right away when a big customer opens a support ticket. If the account is worth more than 50k a year, ping the account owner on Slack.

**Spec:**
```
Type:       Webhook service (support ticket escalation)
Features:   - Receive Freshdesk ticket-created webhooks
            - Look up the company's annual contract value in Salesforce
            - Send a direct Slack message to the account owner for accounts over 50k
            - Raise the ticket priority to high in Freshdesk
            - Cache account lookups for one hour
API:        REST
            POST /webhooks/freshdesk
Storage:    Redis (cache)
Tech stack: Python, FastAPI, simple-salesforce, Slack Web API, Freshdesk API
```

---

## Example 315

**Intent:**
log every login and send email if login from new country

**Spec:**
```
Type:       REST API service (login alerts)
Data model: LoginEvent(id, user_id, ip, country, user_agent, success, created_at)
Features:   - Record every login with IP, country and device
            - Detect logins from a country the user never used before
            - Email the user with a "this wasn't me" link
            - Lock the account and end sessions when "this wasn't me" is clicked
            - Show recent logins in the account settings
API:        REST
            GET  /me/logins
            POST /security/not-me?token={token}
Storage:    PostgreSQL
Tech stack: Node.js, Express, MaxMind GeoLite2, Postmark
```

---

## Example 316

**Intent:**
discord counting game bot

**Spec:**
```
Type:       Bot (Discord)
Data model: CountState(guild_id, channel_id, current, last_user_id, record)
Features:   - Check each message in the counting channel is the next number
            - Stop the same person counting twice in a row
            - React with a check mark for right numbers
            - Reset to zero on a wrong number and announce who broke it
            - Track the server's highest count
Storage:    SQLite
Tech stack: Python, discord.py
```

---

## Example 317

**Intent:**
need autoscaling for our api servers on aws when traffic spikes

**Spec:**
```
Type:       Infrastructure setup (autoscaling)
Features:   - Run the API on an EC2 Auto Scaling group from a launch template
            - Scale out when average CPU passes 60% and scale in below 30%
            - Register instances with the load balancer only after health checks pass
            - Keep at least 2 instances across two availability zones
            - Use a mix of on-demand and spot instances to save cost
Tech stack: AWS EC2 Auto Scaling, Application Load Balancer, CloudWatch, Terraform
```

---

## Example 318

**Intent:**
chatbot whatsapp for real estate, people ask about apartments and book a visit

**Spec:**
```
Type:       Chatbot (WhatsApp, real estate)
Data model: Listing(id, title, district, rooms, price, available)
            Visit(id, listing_id -> Listing, phone, name, visit_at, agent_id)
Features:   - Ask for district, rooms and budget
            - Show matching listings with photos
            - Book a viewing with an agent's free time slot
            - Send the agent the visit details
            - Remind the customer the day before
API:        REST
            POST /webhooks/whatsapp
Storage:    PostgreSQL
Tech stack: Node.js, Express, WhatsApp Cloud API, Google Calendar API
```

---

## Example 319

**Intent:**
s3 bucket cross region replication for backup

**Spec:**
```
Type:       Infrastructure setup (storage replication)
Features:   - Turn on versioning on the source and backup buckets
            - Replicate new objects to a bucket in another region
            - Replicate deletes as delete markers only
            - Move backup copies to Glacier after 30 days
            - Alert when replication falls behind
Tech stack: Amazon S3 Replication, S3 Lifecycle, CloudWatch, Terraform
```

---

## Example 320

**Intent:**
lemon squeezy webhooks for my saas licenses

**Spec:**
```
Type:       Webhook service (Lemon Squeezy)
Data model: Customer(id, email, ls_customer_id, plan, status, renews_at)
Features:   - Receive subscription_created, subscription_updated and subscription_expired events
            - Verify the X-Signature HMAC header
            - Update the user's plan and status
            - Remove premium features when the subscription expires
            - Save the customer portal URL for the billing page
API:        REST
            POST /webhooks/lemonsqueezy
Storage:    SQLite
Tech stack: TypeScript, SvelteKit server routes, Drizzle ORM
```

---

## Example 321

**Intent:**
grpc and rest api for inventory of our stores

**Spec:**
```
Type:       REST API service (inventory, with gRPC)
Auth:       mTLS for internal gRPC; API key for REST
Data model: Store(id, name, region)
            StockItem(store_id -> Store, sku, quantity, reserved, updated_at)
Features:   - Get stock for a SKU across all stores
            - Reserve stock for an order and release it on cancel
            - Stop stock going below zero with row locks
            - Expose the same methods over gRPC and REST via a gateway
            - Publish stock change events to Kafka
API:        REST
            GET  /stock/{sku}
            POST /reservations
            DELETE /reservations/{id}
Storage:    PostgreSQL, Kafka
Tech stack: Go, gRPC, grpc-gateway, PostgreSQL
```

---

## Example 322

**Intent:**
notion page updated -> post to slack channel

**Spec:**
```
Type:       Scheduled script (Notion to Slack)
Data model: SeenEdit(page_id, last_edited_time)
Features:   - Query a Notion database for pages edited in the last 10 minutes
            - Post the page title, editor and link to Slack
            - Skip edits that were already posted
            - Post new pages differently from edited pages
Storage:    SQLite
Tech stack: Python, Notion API, Slack Incoming Webhooks, cron
```

---

## Example 323

**Intent:**
eu hosting for our app because of gdpr, now we're on us servers. need to move

**Spec:**
```
Type:       Infrastructure setup (data residency migration)
Features:   - Create a new production environment in an EU region
            - Copy the database with ongoing replication until switch-over
            - Copy object storage files to an EU bucket
            - Switch DNS to the EU environment during a short maintenance window
            - Delete US copies of personal data after the move is verified
Tech stack: AWS (eu-central-1), AWS DMS, S3 Batch Replication, Route 53, Terraform
```

---

## Example 324

**Intent:**
rest api in flask for a pet adoption shelter with photo upload

**Spec:**
```
Type:       REST API service
Auth:       Staff login with JWT
Data model: Animal(id, name, species, breed, age_months, status, photo_url)
            Application(id, animal_id -> Animal, applicant_name, email, phone, message, status)
Features:   - List animals available for adoption with filters
            - Let staff add animals with photos
            - Accept adoption applications from the public
            - Let staff approve or reject applications and email the applicant
API:        REST
            GET  /animals
            POST /animals
            POST /animals/{id}/photo
            POST /animals/{id}/applications
            PATCH /applications/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Flask, SQLAlchemy, boto3
```

---

## Example 325

**Intent:**
make me a chatbot on signal to get our server alerts

**Spec:**
```
Type:       Bot (Signal)
Features:   - Receive alerts from Alertmanager through a webhook
            - Send each alert to a Signal group
            - Answer "status" with the list of firing alerts
            - Silence an alert for an hour with "silence <name>"
API:        REST
            POST /alerts
Tech stack: Python, signal-cli REST API, Alertmanager API
```

---

## Example 326

**Intent:**
Hi! I make a small mobile game with ads and in app purchases, google play. I need server to check purchases are real so people can't hack coins.

**Spec:**
```
Type:       REST API service (purchase verification)
Auth:       Player device token
Data model: Player(id, device_id, coins)
            Purchase(id, player_id -> Player, product_id, purchase_token, order_id, status, verified_at)
Features:   - Verify purchase tokens with the Google Play Developer API
            - Give coins only after successful verification
            - Reject a purchase token used before
            - Acknowledge purchases so Google does not refund them
            - Handle voided purchases from Real-time Developer Notifications
API:        REST
            POST /purchases/verify
            POST /webhooks/play-rtdn
Storage:    PostgreSQL
Tech stack: Node.js, Express, googleapis (Android Publisher), Google Cloud Pub/Sub
```

---

## Example 327

**Intent:**
alert when nightly etl is late

**Spec:**
```
Type:       Scheduled script (job SLA alert)
Features:   - Check at 07:00 whether the nightly ETL wrote its success marker
            - Alert the data team in Slack if it is missing
            - Include the last log lines from the job
            - Escalate to on-call at 08:00 if still missing
Tech stack: Python, boto3 (S3 marker file), Slack Web API, AWS Lambda, EventBridge
```

---

## Example 328

**Intent:**
bot for discord server that post free games from epic and steam

**Spec:**
```
Type:       Bot (Discord)
Data model: PostedDeal(id, store, game_id, posted_at)
Features:   - Check Epic Games Store free games and Steam 100% discounts every hour
            - Post each new free game with image, store and end date
            - Ping a role that members can opt into
            - Never post the same deal twice
Storage:    SQLite
Tech stack: Node.js, discord.js, Epic Games Store API, Steam store API
```

---

## Example 329

**Intent:**
a shared redis for all our apps but nobody should see each others data

**Spec:**
```
Type:       Infrastructure setup (shared Redis)
Features:   - Run Redis with ACL users for each app
            - Limit each app user to its own key prefix
            - Turn on TLS for connections
            - Set memory limits and an eviction policy
            - Monitor memory and connections per app
Tech stack: Redis 7 (ACLs), redis_exporter, Prometheus
```

---

## Example 330

**Intent:**
api to send whatsapp messages from our crm

**Spec:**
```
Type:       REST API service (WhatsApp messaging)
Auth:       API key from the CRM
Data model: Conversation(id, customer_phone, last_inbound_at)
            WaMessage(id, conversation_id -> Conversation, direction, template, body, status, wa_message_id, created_at)
Features:   - Send approved template messages to any customer
            - Send free-text replies only within 24 hours of the customer's last message
            - Receive inbound messages and status updates by webhook
            - Push inbound messages back to the CRM
API:        REST
            POST /messages
            POST /webhooks/whatsapp
Storage:    PostgreSQL
Tech stack: PHP, Laravel, WhatsApp Cloud API
```

---

## Example 331

**Intent:**
i want the bot in our slack to remind reviewers about open pull requests older than a day

**Spec:**
```
Type:       Scheduled script (pull request reminders)
Features:   - List open pull requests across the organization's repositories each weekday at 10:00
            - Find requested reviewers on pull requests older than 24 hours
            - Send each reviewer a Slack DM with their waiting pull requests
            - Skip draft pull requests
            - Map GitHub usernames to Slack users from a config file
Tech stack: Python, GitHub GraphQL API, Slack Web API, GitHub Actions schedule
```

---

## Example 332

**Intent:**
mollie payments for my dutch webshop backend

**Spec:**
```
Type:       REST API service (payments)
Data model: Order(id, total_eur, status, mollie_payment_id)
Features:   - Create a Mollie payment with iDEAL, card and Bancontact
            - Redirect the customer to Mollie's checkout page
            - Receive Mollie webhook calls and fetch the payment to get its real status
            - Mark orders paid, failed or expired
            - Create refunds from the admin
API:        REST
            POST /orders/{id}/pay
            POST /webhooks/mollie
            POST /orders/{id}/refund
Storage:    PostgreSQL
Tech stack: PHP, Symfony, Mollie API client
```

---

## Example 333

**Intent:**
wut i need: when my docker containers log an error, send it to telegram

**Spec:**
```
Type:       Scheduled script (container error alerts)
Features:   - Follow the logs of all running containers
            - Match lines containing ERROR, Exception or panic
            - Send the container name and log line to Telegram
            - Group repeated errors into one message per 5 minutes
            - Ignore patterns listed in a config file
Tech stack: Python, Docker SDK for Python, Telegram Bot API, systemd
```

---

## Example 334

**Intent:**
api so drivers in our taxi company see new rides and accept them

**Spec:**
```
Type:       REST API service (ride dispatch)
Auth:       Driver login with phone number and SMS code
Data model: Driver(id, name, phone, status, lat, lng)
            Ride(id, pickup_address, pickup_lat, pickup_lng, dropoff_address, status, driver_id -> Driver, created_at)
Features:   - Offer new rides to the nearest available drivers
            - Let the first driver to accept get the ride (atomic update)
            - Update ride status: accepted, arrived, started, finished
            - Track driver location every 5 seconds during a ride
            - Push new ride offers over WebSocket
API:        REST
            GET  /rides/offers
            POST /rides/{id}/accept
            PATCH /rides/{id}/status
            POST /drivers/me/location
            WS   /drivers/stream
Storage:    PostgreSQL with PostGIS, Redis (driver locations)
Tech stack: Node.js, Fastify, Socket.IO, Redis GEO
```

---

## Example 335

**Intent:**
jira ticket done -> notify customer by email

**Spec:**
```
Type:       Webhook service (Jira to customer email)
Features:   - Receive Jira issue_updated webhooks
            - Check for a transition to Done
            - Read the customer email from a custom field
            - Send the customer a "your request is resolved" email
            - Skip internal issues without a customer email
API:        REST
            POST /webhooks/jira
Tech stack: Node.js, Express, Jira webhooks, Amazon SES
```

---

## Example 336

**Intent:**
Please design a backend for a small SaaS that sends invoices: create customers, create invoices with line items, send them by email with a pay link, and send reminders when overdue.

**Spec:**
```
Type:       REST API service (invoicing)
Auth:       Email + password, JWT
Data model: Customer(id, account_id, name, email, address)
            Invoice(id, customer_id -> Customer, number, status, due_date, total, pay_url)
            LineItem(id, invoice_id -> Invoice, description, quantity, unit_price, tax_rate)
Features:   - Create customers and invoices with line items and tax
            - Generate a PDF and email it with a Stripe payment link
            - Mark invoices paid from Stripe webhooks
            - Send reminders 3 and 10 days after the due date
            - Number invoices in sequence per account
API:        REST
            POST /customers
            POST /invoices
            POST /invoices/{id}/send
            GET  /invoices?status={status}
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, Django REST Framework, WeasyPrint, Stripe, Celery
```

---

## Example 337

**Intent:**
cloudwatch alarms for our lambdas

**Spec:**
```
Type:       Infrastructure setup (serverless monitoring)
Features:   - Alarm on Lambda errors and throttles for each function
            - Alarm when duration gets close to the timeout
            - Alarm on messages in each dead-letter queue
            - Send alarms to an SNS topic subscribed by email and Slack
Tech stack: Amazon CloudWatch, SNS, AWS Chatbot, AWS CDK
```

---

## Example 338

**Intent:**
ich möchte einen telegram bot der mir die abfahrtszeiten von meiner bushaltestelle schickt

**Spec:**
```
Type:       Bot (Telegram)
Data model: SavedStop(chat_id, stop_id, stop_name)
Features:   - Search for a stop by name and save it as a favourite
            - Show the next departures with line, direction and delay
            - Send departures automatically every weekday at a chosen time
            - Answer in German
Storage:    SQLite
Tech stack: Python, python-telegram-bot, public transport API (HAFAS)
```

---

## Example 339

**Intent:**
secure webhook endpoint template we can reuse for all integrations

**Spec:**
```
Type:       Webhook service (reusable receiver)
Data model: WebhookEvent(id, provider, event_id, payload_json, status, attempts, received_at)
Features:   - Verify HMAC signatures with per-provider secrets
            - Reject requests with timestamps older than 5 minutes (replay protection)
            - Save the raw event and reply 200 within 1 second
            - Process events from a queue with retries
            - Ignore events with an event ID already processed
API:        REST
            POST /webhooks/{provider}
Storage:    PostgreSQL, Redis Streams
Tech stack: Go, chi router, Redis
```

---

## Example 340

**Intent:**
ok weird one. my grandma's assisted living place wants a way for families to get a text when she takes her medicine or misses it. the nurses already scan a barcode on the med cart which logs to their system, which has an export api

**Spec:**
```
Type:       Scheduled script (medication notifications)
Data model: Resident(id, name, facility_resident_id)
            FamilyContact(id, resident_id -> Resident, phone, consented)
            MedEvent(id, resident_id -> Resident, scheduled_at, given_at, status)
Features:   - Read medication events from the facility system's API every 15 minutes
            - Text consented family members when a scheduled dose is marked missed
            - Send a daily summary text of doses given
            - Leave out medicine names and use only "morning/evening dose" wording
            - Let family members stop texts by replying STOP
Storage:    PostgreSQL (encrypted at rest)
Tech stack: Python, facility export API, Twilio SMS, cron
```

---

## Example 341

**Intent:**
blue sky bot posting our blog posts

**Spec:**
```
Type:       Bot (Bluesky)
Features:   - Read the blog's RSS feed every 30 minutes
            - Post new articles with title, link card and image
            - Add hashtags from the post's tags
            - Remember posted articles
Tech stack: Python, atproto SDK, feedparser, GitHub Actions schedule
```

---

## Example 342

**Intent:**
rest api with rate limit per plan free/pro

**Spec:**
```
Type:       REST API service (plan-based rate limiting)
Auth:       API key mapped to a plan
Data model: ApiKey(id, key_hash, account_id, plan)
Features:   - Allow 60 requests per minute on Free and 1,000 on Pro
            - Allow 10,000 requests per month on Free
            - Return 429 with Retry-After when over the limit
            - Return remaining quota in response headers
            - Show usage per day in a usage endpoint
API:        REST
            GET  /v1/usage
Storage:    Redis (sliding window counters), PostgreSQL
Tech stack: Python, FastAPI, Redis
```

---

## Example 343

**Intent:**
i want my wordpress site on aws lightsail with backups and cdn

**Spec:**
```
Type:       Infrastructure setup (WordPress hosting)
Features:   - Run WordPress on a Lightsail instance
            - Use a Lightsail managed MySQL database
            - Take automatic daily snapshots of the instance
            - Serve images and static files through a Lightsail CDN distribution
            - Attach a static IP and set up HTTPS
Tech stack: AWS Lightsail, Lightsail managed database, Lightsail CDN, Let's Encrypt
```

---

## Example 344

**Intent:**
discord bot for our school club to post homework deadlines from google classroom

**Spec:**
```
Type:       Bot (Discord)
Features:   - Read coursework and due dates from Google Classroom every hour
            - Post new assignments in the matching class channel
            - Remind the channel 24 hours before each deadline
            - List upcoming deadlines with /deadlines
Tech stack: Python, discord.py, Google Classroom API
```

---

## Example 345

**Intent:**
sentry errors -> jira tickets automatically

**Spec:**
```
Type:       Webhook service (Sentry to Jira)
Data model: ErrorTicket(sentry_issue_id, jira_key)
Features:   - Receive Sentry issue alert webhooks
            - Verify the Sentry-Hook-Signature header
            - Create a Jira bug with the error title, stack trace link and event count
            - Comment on the existing Jira issue when the same error comes back
            - Close the Jira issue when the Sentry issue is resolved
API:        REST
            POST /webhooks/sentry
Storage:    SQLite
Tech stack: Python, Flask, Jira Cloud REST API
```

---

## Example 346

**Intent:**
nomad cluster to run our containers instead of kubernetes, we are 3 devs

**Spec:**
```
Type:       Infrastructure setup (container orchestration)
Features:   - Run a 3-node Nomad and Consul cluster
            - Deploy services as Nomad jobs with Docker
            - Register services in Consul for service discovery
            - Route traffic with Traefik reading the Consul catalog
            - Do rolling updates with automatic rollback
Tech stack: HashiCorp Nomad, Consul, Traefik, Docker
```

---

## Example 347

**Intent:**
graphql api for an ecommerce shop: products, cart, checkout

**Spec:**
```
Type:       GraphQL API service
Auth:       Guest carts by cookie; customer accounts with JWT
Data model: Product(id, title, slug, price, stock)
            Cart(id, customer_id, session_id)
            CartItem(cart_id -> Cart, product_id -> Product, quantity)
            Order(id, cart_id -> Cart, total, status)
Features:   - Query products with filters and cursor pagination
            - Add, update and remove cart items through mutations
            - Merge a guest cart into the customer's cart at login
            - Start checkout and return a payment client secret
            - Check stock again at checkout
API:        GraphQL
            POST /graphql
Storage:    PostgreSQL
Tech stack: Node.js, Pothos GraphQL, GraphQL Yoga, Prisma, Stripe
```

---

## Example 348

**Intent:**
a script that backs up all our notion workspace every week

**Spec:**
```
Type:       Scheduled script (Notion backup)
Features:   - Export every page and database through the Notion API
            - Save pages as Markdown and databases as CSV
            - Download attached files and images
            - Zip the export and upload it to Google Drive
            - Keep the last 12 weekly exports
Tech stack: Python, Notion API, Google Drive API, GitHub Actions schedule
```

---

## Example 349

**Intent:**
hi we are using odoo and want when customer pay on our website stripe it create the payment in odoo

**Spec:**
```
Type:       Webhook service (Stripe to Odoo)
Features:   - Receive payment_intent.succeeded events and verify the signature
            - Find the Odoo invoice by the reference in the payment metadata
            - Register the payment on the invoice in Odoo
            - Skip events already registered
            - Email accounting when no matching invoice is found
API:        REST
            POST /webhooks/stripe
Storage:    SQLite
Tech stack: Python, FastAPI, Odoo JSON-RPC, Stripe SDK
```

---

## Example 350

**Intent:**
status alerts from github, aws and cloudflare in one discord channel

**Spec:**
```
Type:       Scheduled script (provider status feed)
Data model: SeenIncident(provider, incident_id, last_status)
Features:   - Poll each provider's status feed every 5 minutes
            - Post new incidents and updates to a Discord channel
            - Color the embed by severity
            - Post when an incident is resolved
Storage:    SQLite
Tech stack: Node.js, rss-parser, Discord webhooks
```

---

## Example 351

**Intent:**
single api for sending messages to users on whatever they use: telegram, whatsapp or email

**Spec:**
```
Type:       REST API service (multi-channel messaging)
Auth:       Internal API key
Data model: Contact(id, user_id, channel, address, verified, preferred)
            OutboundMessage(id, user_id, channel, text, status, provider_id, created_at)
Features:   - Send a message to a user on their preferred channel
            - Fall back to the next channel if delivery fails
            - Format text for each channel's limits
            - Track delivery status from each provider
            - Let users verify new channels with a code
API:        REST
            POST /messages
            GET  /messages/{id}
            POST /contacts
            POST /contacts/{id}/verify
Storage:    PostgreSQL, RabbitMQ
Tech stack: Python, FastAPI, Telegram Bot API, WhatsApp Cloud API, Amazon SES
```

---

## Example 352

**Intent:**
make our github actions faster with self hosted runners on aws that scale

**Spec:**
```
Type:       Infrastructure setup (CI runners)
Features:   - Start EC2 spot instances as GitHub runners when jobs are queued
            - Shut runners down after each job (ephemeral runners)
            - Use a pre-built AMI with Docker and common tools
            - Scale to zero when no jobs are waiting
            - Keep runners in a private subnet
Tech stack: terraform-aws-github-runner, AWS EC2 spot, Lambda, Packer
```

---

## Example 353

**Intent:**
simple uptime bot on discord that checks my website every 5 min

**Spec:**
```
Type:       Bot (Discord)
Features:   - Check the website every 5 minutes
            - Post in a channel when it goes down and when it is back
            - Show uptime for the last 24 hours with /uptime
            - Change the URL with /seturl for admins
Tech stack: Node.js, discord.js, node-cron, axios
```

---

## Example 354

**Intent:**
backend for loyalty stamp cards via sms for my coffee shop, scan phone number at till

**Spec:**
```
Type:       REST API service (loyalty stamps)
Auth:       PIN for the till device
Data model: Customer(id, phone, stamps, rewards_earned)
            Stamp(id, customer_id -> Customer, created_at)
Features:   - Add a stamp when the barista enters the customer's phone number
            - Give a free coffee after 9 stamps and text the customer
            - Redeem a reward at the till
            - Stop more than 2 stamps per phone per hour
API:        REST
            POST /stamps
            POST /rewards/redeem
            GET  /customers/{phone}
Storage:    SQLite
Tech stack: Python, Flask, Twilio SMS
```

---

## Example 355

**Intent:**
we want postgres point in time recovery in case someone drops a table

**Spec:**
```
Type:       Infrastructure setup (point-in-time recovery)
Features:   - Archive WAL files continuously to object storage
            - Take a full base backup every night
            - Restore the database to any second in the last 14 days
            - Check backups each week by restoring into a test server
            - Alert when WAL archiving falls behind
Tech stack: PostgreSQL, WAL-G, Amazon S3, Prometheus
```

---

## Example 356

**Intent:**
discord bot that answers questions about our game using our wiki

**Spec:**
```
Type:       Chatbot (Discord, game wiki)
Data model: WikiPage(id, title, url, content, embedding)
Features:   - Crawl the game wiki every night and index pages
            - Answer /ask questions using the most relevant wiki pages
            - Link the wiki pages used in the answer
            - Say "I don't know" when nothing relevant is found
            - Limit each user to 20 questions per hour
Storage:    PostgreSQL with pgvector
Tech stack: Python, discord.py, pgvector, LLM API
```

---

## Example 357

**Intent:**
amazon seller orders into our sheet every hour

**Spec:**
```
Type:       Scheduled script (Amazon to Google Sheets)
Data model: SyncedAmazonOrder(amazon_order_id, synced_at)
Features:   - Fetch new orders from the Amazon Selling Partner API every hour
            - Append order ID, date, SKU, quantity and total to the sheet
            - Update the status column for shipped and cancelled orders
            - Handle API rate limits with backoff
Storage:    SQLite
Tech stack: Python, python-amazon-sp-api, gspread, cron
```

---

## Example 358

**Intent:**
add login with phone number to our app, users in africa mostly use phones not email

**Spec:**
```
Type:       REST API service (phone login)
Auth:       Phone number + SMS OTP, JWT sessions
Data model: User(id, phone, name, created_at)
            OtpRequest(id, phone, code_hash, expires_at, attempts)
Features:   - Send a 6-digit OTP by SMS through a local provider
            - Fall back to a voice call if the SMS is not received
            - Create the account on first login
            - Rate limit OTP requests per number and per IP
API:        REST
            POST /auth/otp
            POST /auth/otp/verify
            POST /auth/otp/voice
Storage:    PostgreSQL, Redis
Tech stack: Node.js, NestJS, Africa's Talking SMS and Voice API
```

---

## Example 359

**Intent:**
monitor our cron on heroku scheduler

**Spec:**
```
Type:       Infrastructure setup (job monitoring)
Features:   - Add a ping to a cron monitor at the end of each scheduled task
            - Set expected periods and grace times per task
            - Alert in Slack when a task misses its ping
            - Send failure pings with the error message
Tech stack: Heroku Scheduler, Healthchecks.io, Slack integration
```

---

## Example 360

**Intent:**
telegram bot: forward all emails from one gmail label to my chat

**Spec:**
```
Type:       Bot (Telegram)
Data model: ForwardedEmail(gmail_message_id, forwarded_at)
Features:   - Read new emails with a chosen Gmail label every 2 minutes
            - Send sender, subject and the first 500 characters to Telegram
            - Attach small attachments as files
            - Mark emails as read after forwarding
Storage:    SQLite
Tech stack: Python, Gmail API, python-telegram-bot
```

---

## Example 361

**Intent:**
alerting when someone changes our aws security groups

**Spec:**
```
Type:       Infrastructure setup (change alerting)
Features:   - Capture security group changes from CloudTrail
            - Match AuthorizeSecurityGroupIngress events with EventBridge rules
            - Alert in Slack with who changed what
            - Revert rules that open SSH to 0.0.0.0/0 automatically with a Lambda
Tech stack: AWS CloudTrail, EventBridge, Lambda, Python, Slack
```

---

## Example 362

**Intent:**
api that returns the users timezone and country from ip

**Spec:**
```
Type:       REST API service (IP geolocation)
Auth:       API key
Features:   - Look up country, city and time zone for an IP address
            - Use the caller's IP when none is given
            - Support IPv4 and IPv6
            - Update the GeoIP database weekly
API:        REST
            GET  /ip/{address}
            GET  /ip/me
Tech stack: Go, MaxMind GeoLite2, geoipupdate
```

---

## Example 363

**Intent:**
webhook so google forms answers go to a discord channel

**Spec:**
```
Type:       Webhook service (Google Forms to Discord)
Features:   - Run an Apps Script trigger on each form submission
            - Format questions and answers into a Discord embed
            - Send the embed to a Discord webhook URL
            - Split long answers to stay within Discord's limits
Tech stack: Google Apps Script, Discord webhooks
```

---

## Example 364

**Intent:**
need api documentation and mock server for our new api before backend is ready

**Spec:**
```
Type:       REST API service (API mock)
Features:   - Write the API as an OpenAPI 3 specification
            - Generate documentation pages from the spec
            - Run a mock server that returns example responses
            - Validate requests against the spec and return errors
            - Check the spec for style problems in CI
API:        REST
            ANY  /* (mocked from the OpenAPI spec)
Tech stack: OpenAPI 3.1, Redocly, Prism mock server, Spectral, GitHub Actions
```

---

## Example 365

**Intent:**
our call center wants missed calls to create a callback task in hubspot

**Spec:**
```
Type:       Webhook service (phone system to HubSpot)
Features:   - Receive call-ended webhooks from the cloud phone system
            - Detect missed and abandoned calls
            - Find the HubSpot contact by phone number or create one
            - Create a callback task assigned to the contact owner
            - Avoid duplicate tasks for repeated calls within an hour
API:        REST
            POST /webhooks/calls
Storage:    Redis
Tech stack: Node.js, Aircall webhooks, HubSpot API
```

---

## Example 366

**Intent:**
tg bot that posts cat pics every hour lmao

**Spec:**
```
Type:       Bot (Telegram)
Features:   - Fetch a random cat picture from a cat image API every hour
            - Post it to the channel with a random caption
            - Send a cat picture on demand with /cat
            - Skip images it already posted today
Tech stack: Python, python-telegram-bot, The Cat API
```

---

## Example 367

**Intent:**
hashicorp vault dynamic database passwords for our apps

**Spec:**
```
Type:       Infrastructure setup (dynamic secrets)
Features:   - Turn on Vault's database secrets engine for MySQL
            - Create a role per app with only the grants it needs
            - Give each app pod short-lived credentials through the Vault Agent sidecar
            - Revoke credentials when the lease ends
Tech stack: HashiCorp Vault, Vault Agent Injector, Kubernetes, MySQL
```

---

## Example 368

**Intent:**
when someone books a call on my site, add to google calendar and send a reminder sms an hour before

**Spec:**
```
Type:       REST API service (booking with reminders)
Data model: Booking(id, name, email, phone, starts_at, calendar_event_id, reminder_sent)
Features:   - Return free 30-minute slots from Google Calendar free/busy
            - Book a slot and create the calendar event
            - Send a confirmation email
            - Text a reminder 1 hour before the call
API:        REST
            GET  /slots?date={date}
            POST /bookings
Storage:    SQLite
Tech stack: Node.js, Express, Google Calendar API, Twilio SMS, node-cron
```

---

## Example 369

**Intent:**
want to see all our apps logs and metrics in datadog

**Spec:**
```
Type:       Infrastructure setup (observability)
Features:   - Install the Datadog agent on all hosts and containers
            - Collect logs with service and environment tags
            - Turn on APM tracing for the backend services
            - Build dashboards for each service
            - Create monitors for errors, latency and host health
Tech stack: Datadog Agent, Datadog APM, Docker, Terraform Datadog provider
```

---

## Example 370

**Intent:**
adyen payments for our app with webhooks

**Spec:**
```
Type:       Webhook service (Adyen payments)
Data model: PaymentRecord(id, psp_reference, merchant_reference, event_code, success, amount, received_at)
Features:   - Receive Adyen standard notification webhooks
            - Verify the HMAC signature on each notification item
            - Reply with "[accepted]" right after storing the notification
            - Update order status for AUTHORISATION, CAPTURE and REFUND events
            - Ignore duplicate notifications by PSP reference and event code
API:        REST
            POST /webhooks/adyen
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Adyen Java API library
```

---

## Example 371

**Intent:**
smth to tell me in slack when my vercel deploy fails

**Spec:**
```
Type:       Webhook service (Vercel to Slack)
Features:   - Receive deployment.error and deployment.succeeded webhooks from Vercel
            - Verify the x-vercel-signature header
            - Post failed deploys with project, branch, commit and log link
            - Post production successes to a quieter channel
API:        REST
            POST /webhooks/vercel
Tech stack: TypeScript, Vercel Functions, Slack Incoming Webhooks
```

---

## Example 372

**Intent:**
we are startup from poland, need api for our b2b clients to download their invoices and payment status, must be secure

**Spec:**
```
Type:       REST API service (client billing portal API)
Auth:       OAuth 2.0 client credentials per client company
Data model: ClientCompany(id, name, nip)
            Invoice(id, client_id -> ClientCompany, number, issued_at, due_date, total, status, pdf_key)
Features:   - List a client's invoices with filters by date and status
            - Download invoice PDFs through short-lived signed URLs
            - Show payment status for each invoice
            - Allow access only to the client's own invoices
            - Log every download
API:        REST
            POST /oauth/token
            GET  /invoices
            GET  /invoices/{id}
            GET  /invoices/{id}/pdf
Storage:    PostgreSQL, S3-compatible storage
Tech stack: Java, Spring Boot, Spring Authorization Server
```

---

## Example 373

**Intent:**
monitor the response time of our api from different countries

**Spec:**
```
Type:       Infrastructure setup (global latency monitoring)
Features:   - Run HTTP checks from 5 regions every minute
            - Record DNS, connect, TLS and total response times
            - Alert when the 95th percentile latency in any region is over 1 second
            - Show latency per region on a map dashboard
Tech stack: Grafana Cloud Synthetic Monitoring, Grafana dashboards
```

---

## Example 374

**Intent:**
discord bot economy with coins shop and daily reward

**Spec:**
```
Type:       Bot (Discord)
Data model: Wallet(guild_id, user_id, coins, last_daily_at)
            ShopItem(id, guild_id, name, price, role_id)
Features:   - Give coins once a day with /daily
            - Show balance with /balance
            - Buy shop items with /buy, which can give a role
            - Send coins to another member with /pay
            - Show the richest members with /leaderboard
Storage:    PostgreSQL
Tech stack: TypeScript, discord.js, Prisma
```

---

## Example 375

**Intent:**
every morning email me failed payments from yesterday

**Spec:**
```
Type:       Scheduled script (failed payment report)
Features:   - Run every morning at 07:30
            - Fetch failed charges from the last 24 hours from Stripe
            - Group them by decline reason
            - Email a table with customer, amount and reason
Tech stack: Node.js, Stripe SDK, Nodemailer, cron
```

---

## Example 376

**Intent:**
Hello, I'm a teacher and our school wants the parents group on WhatsApp to get an automatic message when school closes because of weather. The principal would just send one text and it goes to everyone.

**Spec:**
```
Type:       Bot (WhatsApp broadcast)
Data model: Parent(id, name, phone, class, opted_in)
            Broadcast(id, text, sent_by, sent_at, delivered_count)
Features:   - Accept a message from the principal's phone number only
            - Ask the principal to confirm before sending
            - Send the message to all opted-in parents with an approved template
            - Report how many messages were delivered
            - Let parents opt out by replying STOP
API:        REST
            POST /webhooks/whatsapp
Storage:    PostgreSQL
Tech stack: Python, Flask, WhatsApp Cloud API
```

---

## Example 377

**Intent:**
circleci for our node monorepo, only build what changed

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Detect which packages changed with a path-filtering setup workflow
            - Run lint and tests only for changed packages and their dependents
            - Cache node_modules by lockfile checksum
            - Build and publish Docker images for changed services on main
Tech stack: CircleCI, path-filtering orb, Nx, Docker
```

---

## Example 378

**Intent:**
webhook from our 3d printer farm when print finishes to notify in discord

**Spec:**
```
Type:       Webhook service (OctoPrint to Discord)
Features:   - Receive OctoPrint PrintDone and PrintFailed events
            - Check a secret token in the request
            - Post the printer name, file and print time
            - Attach a webcam snapshot of the finished print
API:        REST
            POST /octoprint/events
Tech stack: Python, Flask, OctoPrint webhook plugin, Discord webhooks
```

---

## Example 379

**Intent:**
sms gateway for our hospital appointment reminders, we have mysql with appointments

**Spec:**
```
Type:       Scheduled script (appointment reminders)
Data model: ReminderLog(appointment_id, phone, status, provider_message_id, sent_at)
Features:   - Read tomorrow's appointments from the hospital MySQL database each afternoon
            - Send an SMS with date, time and department
            - Let patients reply 1 to confirm or 2 to cancel
            - Write replies back to the appointment table
            - Never send more than one reminder per appointment
Storage:    MySQL
Tech stack: Python, SQLAlchemy, Vonage SMS API, cron
```

---

## Example 380

**Intent:**
dev wants: oidc login for our k8s cluster with github

**Spec:**
```
Type:       Infrastructure setup (Kubernetes authentication)
Auth:       GitHub login through Dex (OIDC)
Features:   - Run Dex in the cluster with GitHub as the connector
            - Configure the API server to trust Dex tokens
            - Map GitHub teams to Kubernetes groups
            - Give teams namespace access with RoleBindings
            - Let developers log in to kubectl with kubelogin
Tech stack: Kubernetes, Dex, kubelogin, RBAC
```

---

## Example 381

**Intent:**
an api endpoint that our customers call to get usage based billing numbers

**Spec:**
```
Type:       REST API service (usage metering)
Auth:       API key per customer
Data model: UsageEvent(id, customer_id, metric, quantity, idempotency_key, occurred_at)
            UsageSummary(customer_id, metric, period, total)
Features:   - Accept usage events with an idempotency key
            - Total usage per metric per billing period
            - Report usage to Stripe metered billing each hour
            - Return current period usage for a customer
API:        REST
            POST /usage
            GET  /usage/summary?period={yyyy-mm}
Storage:    PostgreSQL
Tech stack: Go, PostgreSQL, Stripe Billing Meters
```

---

## Example 382

**Intent:**
i keep my plex server at home and want to know if it goes down while im traveling

**Spec:**
```
Type:       Scheduled script (home server monitoring)
Features:   - Check the Plex server from outside every 5 minutes
            - Check that the home internet connection is up
            - Send a push notification when either is down for 10 minutes
            - Send a notification when it recovers
Tech stack: Uptime Kuma (on a cheap cloud VM), Pushover
```

---

## Example 383

**Intent:**
telegram bot to manage my todo list

**Spec:**
```
Type:       Bot (Telegram)
Data model: Task(id, chat_id, text, due_at, done)
Features:   - Add a task by sending a message
            - Set a due time with phrases like "tomorrow 9am"
            - List open tasks with /list and mark them done with buttons
            - Remind at the due time
Storage:    SQLite
Tech stack: Python, aiogram, dateparser, APScheduler
```

---

## Example 384

**Intent:**
for compliance we need every change to production infra reviewed and logged

**Spec:**
```
Type:       Infrastructure setup (change management)
Features:   - Manage all infrastructure as Terraform code in Git
            - Require pull request reviews from the platform team for production folders
            - Apply changes only from CI, not from laptops
            - Save every plan and apply log as a CI artifact for 1 year
            - Detect drift every night and open an issue if found
Tech stack: Terraform, GitHub (CODEOWNERS, branch protection), GitHub Actions
```

---

## Example 385

**Intent:**
hubspot deal stage changes logged to bigquery for reports

**Spec:**
```
Type:       Webhook service (HubSpot to BigQuery)
Features:   - Receive deal.propertyChange webhooks for dealstage
            - Verify the HubSpot v3 signature
            - Insert a row with deal ID, old stage, new stage and time into BigQuery
            - Backfill deal history once from the HubSpot API
API:        REST
            POST /webhooks/hubspot
Storage:    Google BigQuery
Tech stack: Python, Google Cloud Functions, BigQuery client, HubSpot API
```

---

## Example 386

**Intent:**
is it possible a bot on viber for our pizza place to take orders

**Spec:**
```
Type:       Bot (Viber)
Data model: Order(id, viber_user_id, items_json, address, phone, status, created_at)
Features:   - Show the menu with picture cards and buttons
            - Add pizzas to a cart and pick sizes
            - Ask for delivery address and phone
            - Send the order to the kitchen tablet and confirm to the customer
            - Send a message when the order is out for delivery
API:        REST
            POST /viber/webhook
Storage:    PostgreSQL
Tech stack: Node.js, viber-bot SDK, Express
```

---

## Example 387

**Intent:**
prometheus for our java spring apps

**Spec:**
```
Type:       Infrastructure setup (application metrics)
Features:   - Expose metrics from Spring Boot with Micrometer and Actuator
            - Scrape all app instances through Kubernetes service discovery
            - Track request rate, errors, latency and JVM memory
            - Alert on high error rate and long garbage collection pauses
Tech stack: Spring Boot Actuator, Micrometer, Prometheus, Grafana
```

---

## Example 388

**Intent:**
convert our heroku postgres to aws rds without much downtime

**Spec:**
```
Type:       Infrastructure setup (database migration)
Features:   - Create an RDS PostgreSQL instance with the same version
            - Copy data with pg_dump and pg_restore for a first full load
            - Keep data in sync with logical replication until the switch
            - Switch the app's DATABASE_URL during a 5-minute maintenance window
            - Compare row counts before turning off the old database
Tech stack: Amazon RDS PostgreSQL, PostgreSQL logical replication, pg_dump
```

---

## Example 389

**Intent:**
api so our crm can create shipping labels with dhl

**Spec:**
```
Type:       REST API service (shipping labels)
Auth:       API key
Data model: Label(id, order_ref, carrier, tracking_number, label_url, created_at)
Features:   - Create a DHL shipment and label from order and address data
            - Validate addresses before creating labels
            - Return the label PDF and tracking number
            - Cancel labels that were not used
API:        REST
            POST /labels
            DELETE /labels/{id}
            GET  /labels/{id}
Storage:    PostgreSQL, S3 (label PDFs)
Tech stack: Python, FastAPI, DHL Parcel API
```

---

## Example 390

**Intent:**
I want our Discord server to log moderation stuff: deleted messages, edits, bans, joins and leaves, so the mods can see what happened.

**Spec:**
```
Type:       Bot (Discord)
Data model: LogConfig(guild_id, channel_id, enabled_events)
Features:   - Log deleted and edited messages with the old content
            - Log bans, kicks and timeouts with the moderator's name
            - Log members joining and leaving with account age
            - Choose which events to log with /logs settings
Storage:    SQLite
Tech stack: Python, discord.py
```

---

## Example 391

**Intent:**
github org audit: who has admin, which repos are public

**Spec:**
```
Type:       Scheduled script (GitHub organization audit)
Features:   - List all repositories with visibility and branch protection status
            - List members and outside collaborators with admin rights
            - Flag public repositories that are not on an allow list
            - Flag members without two-factor authentication
            - Email a weekly CSV report to security
Tech stack: Python, PyGithub, cron
```

---

## Example 392

**Intent:**
live chat between customers and our support agents, backend only

**Spec:**
```
Type:       REST API service (live chat)
Auth:       Customer visitor token; agent login with JWT
Data model: ChatSession(id, visitor_id, agent_id, status, started_at, ended_at)
            ChatMessage(id, session_id -> ChatSession, sender, text, created_at)
Features:   - Start a chat and put it in a waiting queue
            - Assign chats to available agents in turn
            - Send messages in real time over WebSocket
            - Show typing indicators
            - Email the transcript to the customer when the chat ends
API:        REST
            POST /chats
            GET  /chats/{id}/messages
            POST /chats/{id}/close
            WS   /ws
Storage:    PostgreSQL, Redis (pub/sub)
Tech stack: Elixir, Phoenix Channels, PostgreSQL
```

---

## Example 393

**Intent:**
i want my raspberry pi sensors to alert me on telegram when temp in the greenhouse too high

**Spec:**
```
Type:       IoT system (greenhouse alerts)
Features:   - Read temperature and humidity from a DHT22 sensor every minute
            - Alert on Telegram when temperature is over 35°C
            - Alert when the sensor stops sending readings
            - Send a daily min/max summary
            - Change the limit with a /setmax command
Tech stack: Python, Raspberry Pi, Adafruit DHT library, python-telegram-bot
```

---

## Example 394

**Intent:**
send slack message to sales when trial user hits usage limit

**Spec:**
```
Type:       Webhook service (product usage alerts)
Features:   - Receive usage.limit_reached events from the app
            - Verify a shared HMAC signature
            - Look up the account's company and owner in the CRM
            - Post an alert in #sales with account, plan and usage
            - Send at most one alert per account per week
API:        REST
            POST /events/usage
Storage:    Redis
Tech stack: Node.js, Express, Slack Web API, HubSpot API
```

---

## Example 395

**Intent:**
backup and restore plan for our mongodb with replica set

**Spec:**
```
Type:       Infrastructure setup (database backup)
Features:   - Take daily snapshots of a hidden replica set member
            - Keep the oplog large enough for 48 hours of point-in-time restore
            - Copy snapshots to another region
            - Restore into a staging cluster every month and check data
Tech stack: MongoDB, Percona Backup for MongoDB, Amazon S3
```

---

## Example 396

**Intent:**
api pra consultar cep e calcular frete para minha loja

**Spec:**
```
Type:       REST API service (address and shipping)
Auth:       API key
Features:   - Look up an address from a Brazilian CEP
            - Calculate shipping price and days for Correios services
            - Cache CEP results for 30 days
            - Return errors in Portuguese
API:        REST
            GET  /cep/{cep}
            POST /frete
Storage:    Redis
Tech stack: Node.js, Fastify, ViaCEP API, Correios API
```

---

## Example 397

**Intent:**
pipeline that publishes my python package to pypi when i tag a release

**Spec:**
```
Type:       Infrastructure setup (CI/CD)
Features:   - Run tests on all supported Python versions
            - Build the sdist and wheel
            - Publish to PyPI with trusted publishing (no API token)
            - Publish to TestPyPI first for pre-release tags
            - Create a GitHub release with the built files
Tech stack: GitHub Actions, Python build, PyPI trusted publishing
```

---

## Example 398

**Intent:**
microsoft teams notifications from our azure alerts

**Spec:**
```
Type:       Infrastructure setup (alert routing)
Features:   - Create Azure Monitor alert rules for app errors and VM health
            - Send alerts to an action group
            - Post alerts to a Teams channel with a Logic App
            - Include resource name, severity and a portal link
Tech stack: Azure Monitor, Action Groups, Azure Logic Apps, Microsoft Teams
```

---

## Example 399

**Intent:**
whatsapp bot so customers can check their electricity bill

**Spec:**
```
Type:       Bot (WhatsApp)
Data model: Customer(id, account_number, phone, name)
Features:   - Link the customer's phone to their account number after a check
            - Show the latest bill amount and due date
            - Send a payment link
            - Send a reminder 3 days before the due date
API:        REST
            POST /webhooks/whatsapp
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, WhatsApp Cloud API, billing system API
```

---

## Example 400

**Intent:**
graphql api for a cms that our marketing team uses

**Spec:**
```
Type:       GraphQL API service (headless CMS)
Auth:       Editor login with roles (editor, publisher)
Data model: Page(id, slug, title, blocks_json, status, published_at)
            Asset(id, filename, url, alt_text)
Features:   - Query published pages by slug for the website
            - Create and edit draft pages through mutations
            - Publish pages only as a publisher
            - Upload images and return their URLs
            - Call the site rebuild webhook on publish
API:        GraphQL
            POST /graphql
Storage:    PostgreSQL, S3 (assets)
Tech stack: TypeScript, Apollo Server, TypeORM
```

---

## Example 401

**Intent:**
email when anyone in our team pushes directly to main

**Spec:**
```
Type:       Webhook service (GitHub push audit)
Features:   - Receive GitHub push events for all repositories
            - Verify the webhook signature
            - Detect pushes to main that did not come from a merged pull request
            - Email the tech lead with the pusher and commits
API:        REST
            POST /webhooks/github
Tech stack: Python, Flask, GitHub webhooks, SMTP
```

---

## Example 402

**Intent:**
need auto failover dns if our main server dies

**Spec:**
```
Type:       Infrastructure setup (DNS failover)
Features:   - Health check the main server every 30 seconds
            - Point DNS to the backup server when checks fail
            - Use a short TTL of 60 seconds
            - Switch back when the main server is healthy again
            - Email the admin on every failover
Tech stack: Amazon Route 53 health checks, failover routing, SNS
```

---

## Example 403

**Intent:**
quick api for storing form submissions from multiple static sites

**Spec:**
```
Type:       REST API service (form backend)
Auth:       Site key per website; dashboard login
Data model: Site(id, name, site_key, notify_email, allowed_origins)
            Submission(id, site_id -> Site, data_json, ip, created_at, spam)
Features:   - Accept form posts from allowed origins only
            - Filter spam with a honeypot and a rate limit
            - Email each submission to the site owner
            - Export submissions as CSV
API:        REST
            POST /f/{site_key}
            GET  /sites/{id}/submissions
Storage:    SQLite
Tech stack: Go, Fiber, SQLite
```

---

## Example 404

**Intent:**
slack bot that welcomes new hires and gives them onboarding checklist

**Spec:**
```
Type:       Bot (Slack)
Data model: OnboardingTask(id, user_id, title, due_day, done)
Features:   - Send a welcome DM when someone joins the workspace
            - Post a checklist with buttons to mark tasks done
            - Remind about open tasks on day 3 and day 7
            - Tell the manager when the checklist is finished
API:        REST
            POST /slack/events
            POST /slack/interactions
Storage:    PostgreSQL
Tech stack: Node.js, Slack Bolt
```

---

## Example 405

**Intent:**
helm chart and deploy for our django app

**Spec:**
```
Type:       Infrastructure setup (Kubernetes deployment)
Features:   - Write a Helm chart with web, Celery worker and beat deployments
            - Run migrations as a Helm pre-upgrade hook job
            - Set resource requests and limits for each pod
            - Add readiness and liveness probes
            - Keep secrets in sealed secrets in the repo
Tech stack: Helm, Kubernetes, Sealed Secrets, Django, Celery
```

---

## Example 406

**Intent:**
a service to handle our gift cards: buy, send by email, redeem at checkout

**Spec:**
```
Type:       REST API service (gift cards)
Auth:       Customer JWT; admin role for manual adjustments
Data model: GiftCard(id, code_hash, initial_amount, balance, currency, purchaser_email, recipient_email, expires_at)
            GiftCardTransaction(id, card_id -> GiftCard, amount, order_id, created_at)
Features:   - Sell gift cards and create a random code after payment
            - Email the card to the recipient on a chosen date
            - Check the balance of a code
            - Redeem part of the balance at checkout with row locking
            - Lock a code after 5 wrong guesses from one IP
API:        REST
            POST /gift-cards
            GET  /gift-cards/balance?code={code}
            POST /gift-cards/redeem
Storage:    PostgreSQL
Tech stack: Ruby, Rails API, Stripe
```

---

## Example 407

**Intent:**
make heartbeat ping from our backup script and alert if it doesnt arrive

**Spec:**
```
Type:       Webhook service (heartbeat monitor)
Data model: Heartbeat(id, name, token, period_minutes, last_ping_at, state)
Features:   - Give each job a ping URL
            - Record pings with time and optional exit code
            - Alert by email when a ping is overdue
            - Alert again when the job reports a non-zero exit code
API:        REST
            POST /hb/{token}
            GET  /heartbeats
Storage:    SQLite
Tech stack: Python, FastAPI, APScheduler
```

---

## Example 408

**Intent:**
monitor certificate and domain and uptime for our 200 client sites, we are an agency

**Spec:**
```
Type:       Web application (agency site monitoring)
Auth:       Staff login; read-only client links
Data model: Client(id, name, contact_email)
            Site(id, client_id -> Client, url, ssl_expires_at, domain_expires_at, status)
Features:   - Check every site's uptime every 3 minutes
            - Check SSL and domain expiry daily
            - Alert the account manager of that client
            - Send clients a monthly uptime report
            - Show all sites sorted by problems on one dashboard
API:        REST
            GET  /api/sites
            POST /api/sites
Storage:    PostgreSQL
Tech stack: Python, Django, Celery, Redis
```

---

## Example 409

**Intent:**
aws step functions for our order processing with retries

**Spec:**
```
Type:       Infrastructure setup (workflow orchestration)
Features:   - Model order steps (charge, reserve stock, ship, email) as a state machine
            - Retry each step with backoff on temporary errors
            - Undo earlier steps when a later step fails (saga)
            - Send failed executions to an SQS queue for review
            - Alarm on failed executions
Tech stack: AWS Step Functions, Lambda, SQS, CloudWatch, AWS CDK
```

---

## Example 410

**Intent:**
webhook gumroad sale -> add buyer to convertkit with tag

**Spec:**
```
Type:       Webhook service (Gumroad to ConvertKit)
Features:   - Receive Gumroad sale pings
            - Check the seller ID matches ours
            - Add the buyer to ConvertKit with a tag for the product
            - Skip test purchases
API:        REST
            POST /webhooks/gumroad
Tech stack: Node.js, Cloudflare Workers, ConvertKit API
```

---

## Example 411

**Intent:**
redis backups to s3

**Spec:**
```
Type:       Scheduled script (Redis backup)
Features:   - Trigger BGSAVE every 6 hours and wait for it to finish
            - Copy the RDB file to S3 with a timestamp
            - Keep 7 days of backups
            - Alert if the RDB file is older than expected
Tech stack: Bash, redis-cli, AWS CLI, cron
```

---

## Example 412

**Intent:**
mastodon instance hosting for our community, about 500 people

**Spec:**
```
Type:       Infrastructure setup (Mastodon hosting)
Features:   - Run Mastodon web, streaming and Sidekiq with Docker Compose
            - Use PostgreSQL and Redis on the same server with daily backups
            - Store media in S3-compatible object storage with a CDN
            - Send email through a transactional email provider
            - Monitor Sidekiq queues and disk usage
Tech stack: Mastodon, Docker Compose, PostgreSQL, Redis, Backblaze B2, Postmark
```

---

## Example 413

**Intent:**
kinda want a bot in our family telegram that tells us when packages arrive

**Spec:**
```
Type:       Bot (Telegram)
Data model: Parcel(id, chat_id, carrier, tracking_number, label, last_status)
Features:   - Add a parcel with /track <number> <label>
            - Detect the carrier from the tracking number
            - Check status every hour and post changes
            - Post a message when the parcel is delivered and stop tracking it
Storage:    SQLite
Tech stack: Python, aiogram, 17TRACK API
```

---

## Example 414

**Intent:**
tech: rust. need small service receiving webhooks from github and running tests in docker

**Spec:**
```
Type:       Webhook service (mini CI)
Data model: Build(id, repo, commit_sha, status, log_path, started_at, finished_at)
Features:   - Receive pull_request and push events and verify the signature
            - Clone the commit and run tests in a fresh Docker container
            - Run one build at a time per repository
            - Report pending, success and failure as GitHub commit statuses
            - Keep build logs for 14 days
API:        REST
            POST /webhooks/github
            GET  /builds/{id}/log
Storage:    SQLite
Tech stack: Rust, Axum, bollard (Docker API), octocrab
```

---

## Example 415

**Intent:**
alert our team if the number of signups suddenly drops

**Spec:**
```
Type:       Scheduled script (business metric anomaly alert)
Features:   - Count sign-ups per hour from the database
            - Compare with the same hour over the last 4 weeks
            - Alert in Slack when sign-ups fall below 50% of normal for 2 hours
            - Include links to the sign-up funnel dashboard
Tech stack: Python, pandas, PostgreSQL, Slack Incoming Webhooks, cron
```

---

## Example 416

**Intent:**
api endpoints for our mobile app to upload profile photos directly to s3

**Spec:**
```
Type:       REST API service (direct uploads)
Auth:       JWT bearer tokens
Data model: Upload(id, user_id, key, content_type, status, created_at)
Features:   - Return a presigned S3 upload URL limited to images under 5 MB
            - Confirm the upload and check the file type
            - Create a resized avatar with a Lambda after upload
            - Replace the user's old avatar and delete the old file
API:        REST
            POST /uploads/avatar
            POST /uploads/{id}/complete
Storage:    Amazon S3, PostgreSQL
Tech stack: Node.js, Express, AWS SDK v3, AWS Lambda, sharp
```

---

## Example 417

**Intent:**
matrix bot that bridges alerts from our monitoring into a room

**Spec:**
```
Type:       Bot (Matrix)
Features:   - Receive Alertmanager webhooks
            - Post firing and resolved alerts into a Matrix room with colors
            - Let users silence an alert by replying "!silence 1h"
            - Use end-to-end encryption in the room
API:        REST
            POST /alerts
Tech stack: Python, matrix-nio, Alertmanager API
```

---

## Example 418

**Intent:**
export all our slack messages every month for legal

**Spec:**
```
Type:       Scheduled script (Slack archive)
Features:   - Export messages and files from all public channels on the 1st of each month
            - Save each channel as JSON and a readable HTML file
            - Upload the archive to a locked S3 bucket
            - Keep archives for 7 years
Tech stack: Python, Slack Web API (conversations.history), boto3, S3 Object Lock
```

---

## Example 419

**Intent:**
we got hacked once through an old wordpress plugin. i want something that scans our sites every week and emails me if a plugin has a known vulnerability

**Spec:**
```
Type:       Scheduled script (WordPress vulnerability scan)
Data model: ScanResult(id, site_url, plugin, version, vulnerability_id, severity, found_at)
Features:   - Scan each site every week for WordPress core, plugin and theme versions
            - Match versions against a vulnerability database
            - Email a report listing vulnerable plugins by severity
            - Alert right away for critical vulnerabilities
Storage:    SQLite
Tech stack: WPScan CLI, WPScan vulnerability API, Python, cron
```

---

## Example 420

**Intent:**
server for receiving shopify gdpr webhooks for my app

**Spec:**
```
Type:       Webhook service (Shopify app compliance)
Data model: DataRequest(id, shop_domain, topic, customer_id, received_at, completed_at)
Features:   - Receive customers/data_request, customers/redact and shop/redact webhooks
            - Verify the HMAC header and reply 401 when it is wrong
            - Delete the customer's stored data on customers/redact
            - Delete all shop data 48 hours after shop/redact
            - Record each request and when it was completed
API:        REST
            POST /webhooks/customers/data_request
            POST /webhooks/customers/redact
            POST /webhooks/shop/redact
Storage:    PostgreSQL
Tech stack: Node.js, Shopify App Remix, Prisma
```

---

## Example 421

**Intent:**
simple tcp port checks for our database and mail servers

**Spec:**
```
Type:       Scheduled script (port monitoring)
Features:   - Try to open a TCP connection to each host and port every minute
            - Alert by email after 2 failed attempts
            - Record connect times
            - Read hosts and ports from a config file
Tech stack: Go, net.DialTimeout, SMTP alerts, systemd timer
```

---

## Example 422

**Intent:**
our sales team wants to see every new stripe customer in salesforce as an account

**Spec:**
```
Type:       Webhook service (Stripe to Salesforce)
Data model: AccountLink(stripe_customer_id, salesforce_account_id)
Features:   - Receive customer.created and customer.subscription.created events
            - Verify the Stripe-Signature header
            - Create or update a Salesforce account with plan and MRR
            - Avoid duplicates by storing the link between IDs
API:        REST
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Stripe SDK, simple-salesforce
```

---

## Example 423

**Intent:**
docker registry on our own server

**Spec:**
```
Type:       Infrastructure setup (container registry)
Features:   - Run a private Docker registry with Harbor
            - Log in with the company's LDAP accounts
            - Scan pushed images for vulnerabilities
            - Delete untagged images every week
            - Replicate images to a second site
Tech stack: Harbor, Docker, Trivy, LDAP
```

---

## Example 424

**Intent:**
webhook that gets alerts from tradingview and posts to my telegram

**Spec:**
```
Type:       Webhook service (TradingView to Telegram)
Features:   - Receive TradingView alert webhooks with a JSON message
            - Check a secret passphrase in the payload
            - Format ticker, price and signal into a Telegram message
            - Send the message to a private channel
API:        REST
            POST /tv-alerts
Tech stack: Python, FastAPI, Telegram Bot API, Fly.io
```

---
