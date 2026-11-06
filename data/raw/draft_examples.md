# Draft Examples

First drafts of intent -> spec pairs, used to work out the spec format (step 01).
The format rules are in `docs/spec_format.md`.

---

## Example 1

**Intent:**
I want a website where people can sign up and save their favourite recipes.

**Spec:**
```
Type:       Web application (CRUD)
Auth:       User registration and login (email + password, hashed with bcrypt)
Data model: User(id, email, password_hash)
            Recipe(id, user_id -> User, title, ingredients, steps, is_favourite)
Features:   - Create, read, update and delete recipes
            - Mark recipes as favourite
            - List a user's favourite recipes
API:        REST
            POST /signup
            POST /login
            GET  /recipes
            POST /recipes
            PUT  /recipes/{id}
            DELETE /recipes/{id}
Storage:    SQLite (development), PostgreSQL (production)
Tech stack: Python, FastAPI, HTML/CSS/JavaScript frontend
```

---

## Example 2

**Intent:**
An app on my phone to keep track of how much water I drink each day, and remind me if I forget.

**Spec:**
```
Type:       Mobile application
Data model: WaterLog(id, amount_ml, logged_at)
            Settings(daily_goal_ml, reminder_interval_minutes)
Features:   - Log a drink with its amount
            - Show total intake for today against the daily goal
            - Show history for past days
            - Send push notification reminders at a set interval
Storage:    Local on-device database (SQLite)
Tech stack: Flutter (Android and iOS)
```

---

## Example 3

**Intent:**
something that renames all the photos in a folder by the date they were taken

**Spec:**
```
Type:       Command-line script (automation)
Features:   - Scan a folder for image files (.jpg, .jpeg, .png, .heic)
            - Read the "date taken" from each photo's EXIF metadata
            - Rename each file to YYYY-MM-DD_HHMMSS.ext
            - Add a number suffix when two photos share the same timestamp
            - Skip files with no EXIF date and report them
Input:      Path to a folder of image files
Tech stack: Python, Pillow (EXIF reading)
```

---

## Example 4

**Intent:**
a backend that other apps can call to get the weather for a city

**Spec:**
```
Type:       REST API service
Auth:       API key per client app (sent in the X-API-Key header)
Data model: ApiClient(id, name, api_key_hash, created_at)
            WeatherCache(city, data_json, fetched_at)
Features:   - Return current weather for a city by name
            - Return a 5-day forecast for a city
            - Cache results for 10 minutes to reduce calls to the weather provider
            - Reject requests with a missing or invalid API key
            - Limit each client to 100 requests per minute
API:        REST
            GET  /weather/current?city={name}
            GET  /weather/forecast?city={name}
Storage:    Redis (cache), PostgreSQL (API clients)
Tech stack: Python, FastAPI, OpenWeatherMap API
```

---

## Example 5

**Intent:**
I want to make a simple snake game I can play in my browser

**Spec:**
```
Type:       Browser game (2D)
Features:   - Draw the game board on an HTML canvas
            - Move the snake with the arrow keys
            - Place food at a random empty cell
            - Grow the snake and add a point when it eats food
            - End the game when the snake hits a wall or itself
            - Save the high score between sessions
Storage:    Browser localStorage (high score)
Tech stack: HTML, CSS, JavaScript (Canvas API)
```

---

## Example 6

**Intent:**
look at my sales excel file and tell me which product sold the most every month

**Spec:**
```
Type:       Data analysis script
Features:   - Load the sales data from an Excel file
            - Clean the data: remove empty rows, parse dates
            - Group sales by month and product
            - Find the top-selling product for each month
            - Plot monthly sales of the top products as a bar chart
            - Export the results to a new Excel file
Input:      Excel file (.xlsx) with columns: date, product, quantity, price
Tech stack: Python, pandas, openpyxl, matplotlib
```

---

## Example 7

**Intent:**
something in chrome that blocks youtube while im working

**Spec:**
```
Type:       Browser extension
Features:   - Block chosen websites during set working hours
            - Show a "blocked" page instead of the site
            - Let the user edit the list of blocked sites
            - Let the user set working hours and working days
            - Turn blocking on or off from the toolbar button
Storage:    chrome.storage.sync (settings)
Tech stack: JavaScript, Chrome Extension Manifest V3 (declarativeNetRequest)
```

---

## Example 8

**Intent:**
a chat bot on my shop website that can answer customer questions about products and delivery

**Spec:**
```
Type:       Chatbot (web widget)
Data model: Document(id, title, content, embedding)
            Conversation(id, started_at)
            Message(id, conversation_id -> Conversation, role, text, created_at)
Features:   - Show a chat window on every page of the website
            - Answer questions using the shop's product and delivery information
            - Find relevant information with semantic search (RAG)
            - Hand over to a human by email when the bot cannot answer
            - Save conversations for later review
API:        REST
            POST /chat
            GET  /conversations/{id}
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, LLM API, JavaScript chat widget
```

---

## Example 9

**Intent:**
I need a page where I can see my server's CPU and memory usage live

**Spec:**
```
Type:       Monitoring dashboard (web)
Auth:       Single admin login (username + password)
Data model: Metric(id, server_id, cpu_percent, memory_percent, recorded_at)
Features:   - Collect CPU and memory usage every 5 seconds
            - Show live line charts of CPU and memory usage
            - Show history for the last 24 hours
            - Highlight values above a set threshold
            - Delete data older than 7 days
API:        REST + WebSocket
            GET  /metrics?from={time}&to={time}
            WS   /metrics/live
Storage:    SQLite
Tech stack: Python, FastAPI, psutil, JavaScript, Chart.js
```

---

## Example 10

**Intent:**
a notes app for my laptop that works without internet

**Spec:**
```
Type:       Desktop application
Data model: Note(id, title, body, tags, created_at, updated_at)
Features:   - Create, edit and delete notes
            - Search notes by title, text or tag
            - Format notes with Markdown
            - Save changes automatically
            - Export a note as a Markdown or PDF file
Storage:    Local SQLite database
Tech stack: Electron, React, TypeScript
```

---

## Example 11

**Intent:**
I want a site where dog owners can book local dog walkers and pay them online

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Email + password signup with separate owner and walker roles
Data model: User(id, email, password_hash, role, name, city)
            WalkerProfile(id, user_id -> User, bio, price_per_walk, service_area)
            Dog(id, owner_id -> User, name, breed, notes)
            Booking(id, dog_id -> Dog, walker_id -> User, start_time, duration_min, status)
            Review(id, booking_id -> Booking, rating, comment)
Features:   - Search walkers by area, price and availability
            - Book a walk for a chosen dog and time slot
            - Let walkers accept or decline booking requests
            - Charge the owner by card when the walk is confirmed
            - Pay out walkers after completed walks
            - Leave a star rating and review after each walk
API:        REST
            GET  /walkers?area={area}
            POST /bookings
            PATCH /bookings/{id}/status
            POST /bookings/{id}/review
            POST /payments/webhook
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma, Stripe Connect
```

---

## Example 12

**Intent:**
link shortener with click stats

**Spec:**
```
Type:       Web application (URL shortener)
Auth:       Email + password login (optional for anonymous short links)
Data model: User(id, email, password_hash)
            Link(id, user_id -> User, slug, target_url, created_at, expires_at)
            Click(id, link_id -> Link, clicked_at, referrer, country, user_agent)
Features:   - Create a short link from a long URL with a random or custom slug
            - Redirect visitors from the short link to the target URL
            - Record each click with referrer, country and device
            - Show a chart of clicks per day for each link
            - Expire links after an optional end date
API:        REST
            POST /links
            GET  /{slug}
            GET  /links/{id}/stats
            DELETE /links/{id}
Storage:    PostgreSQL (links, clicks), Redis (slug lookup cache)
Tech stack: Go, chi router, React dashboard, MaxMind GeoLite2
```

---

## Example 13

**Intent:**
hey so I want to build a job board just for remote software jobs, companies post listings and devs can apply

**Spec:**
```
Type:       Web application (job board)
Auth:       Email + password login with employer and candidate roles
Data model: Company(id, name, website, logo_url)
            User(id, email, password_hash, role, company_id -> Company)
            Job(id, company_id -> Company, title, description, salary_range, timezone_range, tags, published_at)
            Application(id, job_id -> Job, candidate_id -> User, resume_url, cover_letter, status)
Features:   - Post, edit and close job listings as an employer
            - Filter jobs by tag, salary and timezone
            - Apply to a job with a resume upload and cover letter
            - Track application status for employers and candidates
            - Send a weekly email digest of new jobs matching saved tags
API:        REST
            GET  /jobs?tag={tag}&tz={range}
            POST /jobs
            PUT  /jobs/{id}
            POST /jobs/{id}/applications
            GET  /applications
Storage:    PostgreSQL, S3 (resumes)
Tech stack: Ruby, Ruby on Rails, Hotwire, Sidekiq, Postmark
```

---

## Example 14

**Intent:**
internal wiki for our team

**Spec:**
```
Type:       Web application (wiki)
Auth:       Single sign-on with Google Workspace (company domain only)
Data model: User(id, email, name)
            Page(id, title, slug, parent_id -> Page, created_by -> User)
            Revision(id, page_id -> Page, author_id -> User, content_md, created_at)
Features:   - Create and edit pages in Markdown
            - Organize pages in a nested tree
            - Keep a full revision history and restore old versions
            - Search pages by title and full text
            - Link between pages with [[page name]] syntax
API:        REST
            GET  /pages/{slug}
            POST /pages
            PUT  /pages/{slug}
            GET  /pages/{slug}/revisions
            GET  /search?q={text}
Storage:    PostgreSQL (full-text search with tsvector)
Tech stack: Python, Django, HTMX, markdown-it
```

---

## Example 15

**Intent:**
portfolio website for my photography

**Spec:**
```
Type:       Web application (portfolio)
Auth:       Single admin login for the photographer
Data model: Album(id, title, slug, cover_photo_id, sort_order)
            Photo(id, album_id -> Album, image_url, caption, taken_at)
            ContactMessage(id, name, email, message, sent_at)
Features:   - Show albums as a responsive photo grid
            - Open photos in a full-screen lightbox
            - Upload photos and generate resized thumbnails automatically
            - Reorder albums and photos by drag and drop in the admin area
            - Send contact form messages to the photographer's email
Storage:    Cloudinary (images), SQLite (albums and messages)
Tech stack: Astro, TypeScript, Cloudinary, Resend (email)
```

---

## Example 16

**Intent:**
i want a forum for board game fans where ppl can make threads and reply and upvote stuff

**Spec:**
```
Type:       Web application (forum)
Auth:       Email + password registration with email verification
Data model: User(id, username, email, password_hash, reputation)
            Category(id, name, description)
            Thread(id, category_id -> Category, author_id -> User, title, body, created_at)
            Post(id, thread_id -> Thread, author_id -> User, body, created_at)
            Vote(id, user_id -> User, post_id -> Post, value)
Features:   - Create threads inside categories like strategy, reviews and trading
            - Reply to threads with Markdown formatting
            - Upvote and downvote posts
            - Sort threads by newest, most active or top voted
            - Let moderators lock, pin or delete threads
            - Notify users of replies to their threads
API:        REST
            GET  /categories/{id}/threads
            POST /threads
            POST /threads/{id}/posts
            POST /posts/{id}/vote
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Livewire, Tailwind CSS
```

---

## Example 17

**Intent:**
A table reservation system for my restaurant so guests can book online instead of calling. We have 15 tables of different sizes and two seatings each evening. I also want staff to see the bookings for the night on a tablet.

**Spec:**
```
Type:       Web application (booking system)
Auth:       Staff login with email + password; guests book without an account
Data model: Table(id, number, seats)
            Seating(id, date, start_time)
            Reservation(id, table_id -> Table, seating_id -> Seating, guest_name, phone, email, party_size, status)
Features:   - Show available seatings for a chosen date and party size
            - Assign the smallest free table that fits the party automatically
            - Send a confirmation email with a cancel link
            - Show tonight's bookings on a tablet-friendly staff view
            - Mark reservations as seated, no-show or cancelled
            - Block tables for walk-ins or private events
API:        REST
            GET  /availability?date={date}&party={n}
            POST /reservations
            DELETE /reservations/{token}
            GET  /staff/reservations?date={date}
            PATCH /staff/reservations/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, SQLAlchemy, Vue.js, SendGrid
```

---

## Example 18

**Intent:**
online shop for my handmade jewelry

**Spec:**
```
Type:       Web application (e-commerce)
Auth:       Customer accounts optional (guest checkout), admin login for the shop owner
Data model: Product(id, name, description, price, stock, material, images)
            Customer(id, email, name, password_hash)
            Order(id, customer_email, total, shipping_address, status, created_at)
            OrderItem(id, order_id -> Order, product_id -> Product, quantity, unit_price)
Features:   - Browse products by category and material
            - Add products to a cart and check out with card payment
            - Reduce stock when an order is paid
            - Email order confirmations and shipping updates
            - Manage products, stock and orders in an admin panel
API:        REST
            GET  /products
            POST /cart/checkout
            POST /webhooks/stripe
            GET  /admin/orders
Storage:    PostgreSQL, S3 (product images)
Tech stack: Medusa.js, Next.js storefront, Stripe
```

---

## Example 19

**Intent:**
personal blog in next.js where i write posts in mdx

**Spec:**
```
Type:       Web application (blog, static)
Data model: Post(slug, title, date, tags, summary, body_mdx)
Features:   - Render MDX posts with code syntax highlighting
            - List posts by date and filter by tag
            - Generate an RSS feed and sitemap at build time
            - Show estimated reading time for each post
            - Support dark and light themes
Storage:    MDX files in the Git repository
Tech stack: Next.js, TypeScript, next-mdx-remote, Shiki, Vercel
```

---

## Example 20

**Intent:**
multi tenant invoicing saas for small businesses, each business has own customers and invoices

**Spec:**
```
Type:       Web application (multi-tenant SaaS)
Auth:       Email + password login, users belong to one or more organizations with owner or member role
Data model: Organization(id, name, currency, logo_url, plan)
            Membership(id, user_id -> User, org_id -> Organization, role)
            User(id, email, password_hash)
            Client(id, org_id -> Organization, name, email, address)
            Invoice(id, org_id -> Organization, client_id -> Client, number, issue_date, due_date, status, total)
Features:   - Isolate each organization's data with row-level tenant filtering
            - Create invoices with line items, tax and discounts
            - Generate invoice PDFs and email them to clients
            - Mark invoices paid and send reminders for overdue ones
            - Bill organizations a monthly subscription by plan
API:        REST
            GET  /orgs/{orgId}/invoices
            POST /orgs/{orgId}/invoices
            GET  /orgs/{orgId}/invoices/{id}/pdf
            POST /orgs/{orgId}/invoices/{id}/send
            POST /orgs/{orgId}/clients
Storage:    PostgreSQL with row-level security
Tech stack: TypeScript, NestJS, React, Puppeteer (PDF), Stripe Billing
```

---

## Example 21

**Intent:**
Can you make a whiteboard website where several people draw on the same board at the same time?

**Spec:**
```
Type:       Web application (real-time collaborative)
Auth:       Guest access by shareable board link, optional Google login to save boards
Data model: User(id, email, name)
            Board(id, owner_id -> User, title, share_token, created_at)
            Snapshot(id, board_id -> Board, data_json, saved_at)
Features:   - Draw freehand lines, shapes and sticky notes on an infinite canvas
            - Sync every stroke to all connected users in real time
            - Show other users' cursors with their names
            - Undo and redo own changes
            - Save the board automatically every few seconds
            - Export the board as PNG
API:        REST + WebSocket
            POST /boards
            GET  /boards/{id}
            WS   /boards/{id}/sync
Storage:    PostgreSQL (boards and snapshots)
Tech stack: TypeScript, React, Yjs (CRDT), y-websocket, Node.js
```

---

## Example 22

**Intent:**
landing page with a waitlist signup form

**Spec:**
```
Type:       Web application (landing page)
Data model: WaitlistEntry(id, email, referral_code, referred_by, created_at)
Features:   - Show a hero section, feature list and FAQ
            - Collect email addresses in a waitlist form with validation
            - Give each signup a referral link to move up the list
            - Send a welcome email with the user's position in line
            - Export the waitlist as CSV
API:        REST
            POST /waitlist
            GET  /waitlist/position?email={email}
Storage:    Supabase (PostgreSQL)
Tech stack: SvelteKit, Supabase, Tailwind CSS, Resend
```

---

## Example 23

**Intent:**
we run small concerts and want to sell tickets ourselves instead of paying ticketmaster fees

**Spec:**
```
Type:       Web application (event ticketing)
Auth:       Organizer login with email + password; buyers check out as guests
Data model: Event(id, title, venue, starts_at, capacity, description)
            TicketType(id, event_id -> Event, name, price, quantity)
            Order(id, event_id -> Event, buyer_email, total, status)
            Ticket(id, order_id -> Order, ticket_type_id -> TicketType, qr_code, checked_in_at)
Features:   - Create events with several ticket types and prices
            - Sell tickets with card payment and stop sales when sold out
            - Email tickets with a unique QR code to the buyer
            - Scan QR codes at the door with a phone to check people in
            - Show sales and check-in numbers per event
API:        REST
            GET  /events
            POST /events/{id}/orders
            POST /tickets/{code}/checkin
            GET  /events/{id}/stats
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe Checkout, qrcode
```

---

## Example 24

**Intent:**
marketplace for tutors and students

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Email + password or Google login with tutor and student roles
Data model: User(id, email, name, role, timezone)
            TutorProfile(id, user_id -> User, subjects, hourly_rate, bio)
            AvailabilitySlot(id, tutor_id -> User, start_time, end_time)
            Lesson(id, tutor_id -> User, student_id -> User, slot_id -> AvailabilitySlot, status, meeting_url)
Features:   - Search tutors by subject, price and rating
            - Book a lesson from a tutor's open time slots
            - Take payment upfront and release it after the lesson
            - Create a video meeting link for each lesson
            - Message between student and tutor
            - Rate tutors after lessons
API:        REST
            GET  /tutors?subject={s}
            GET  /tutors/{id}/slots
            POST /lessons
            POST /lessons/{id}/complete
Storage:    PostgreSQL
Tech stack: Python, Django, Django REST Framework, React, Stripe, Zoom API
```

---

## Example 25

**Intent:**
car rental website with booking

**Spec:**
```
Type:       Web application (booking system)
Auth:       Customer login with email + password, admin login for staff
Data model: Location(id, name, address)
            Car(id, location_id -> Location, model, category, seats, daily_rate, plate)
            Customer(id, email, password_hash, name, license_number)
            Rental(id, car_id -> Car, customer_id -> Customer, pickup_at, return_at, total_price, status)
Features:   - Search available cars by location and date range
            - Prevent double-booking of the same car
            - Calculate the total price with extras like child seats
            - Pay a deposit by card when booking
            - Manage the fleet and rentals in an admin panel
API:        REST
            GET  /cars/available?location={id}&from={date}&to={date}
            POST /rentals
            GET  /rentals/{id}
            DELETE /rentals/{id}
Storage:    MySQL
Tech stack: Java, Spring Boot, Spring Data JPA, Thymeleaf, Stripe
```

---

## Example 26

**Intent:**
my parents have a small bed and breakfast with 4 rooms, they need a website where guests can check free dates and book a room

**Spec:**
```
Type:       Web application (booking system)
Auth:       Owner login only; guests book without an account
Data model: Room(id, name, description, price_per_night, max_guests, photos)
            Booking(id, room_id -> Room, guest_name, email, check_in, check_out, guests, status)
            BlockedDate(id, room_id -> Room, date)
Features:   - Show room photos and a calendar of free dates
            - Book a room for a date range and pay a deposit
            - Send booking confirmation emails to guest and owner
            - Block dates manually for maintenance or private use
            - Sync bookings with Booking.com and Airbnb through iCal feeds
API:        REST
            GET  /rooms
            GET  /rooms/{id}/availability?month={yyyy-mm}
            POST /bookings
            GET  /rooms/{id}/calendar.ics
Storage:    SQLite
Tech stack: PHP, Laravel, Alpine.js, Stripe
```

---

## Example 27

**Intent:**
Gym class booking app for members, using react and firebase

**Spec:**
```
Type:       Web application (booking system)
Auth:       Firebase Authentication (email + password and Google)
Data model: Member(uid, name, email, membership_type)
            GymClass(id, name, instructor, starts_at, capacity)
            Booking(id, class_id -> GymClass, member_uid -> Member, booked_at, status)
Features:   - Show the weekly class timetable
            - Book and cancel a spot in a class
            - Add members to a waitlist when a class is full
            - Promote the first waitlisted member when someone cancels
            - Let staff create classes and see attendee lists
Storage:    Cloud Firestore
Tech stack: React, Firebase Authentication, Cloud Firestore, Cloud Functions
```

---

## Example 28

**Intent:**
barber appointmnt booking site, customers pick a barber and time

**Spec:**
```
Type:       Web application (booking system)
Auth:       Barber login with email + password; customers book with name and phone
Data model: Barber(id, name, photo_url, working_hours)
            Service(id, name, duration_min, price)
            Appointment(id, barber_id -> Barber, service_id -> Service, customer_name, phone, starts_at, status)
Features:   - Pick a barber, a service and a free time slot
            - Calculate free slots from working hours and service duration
            - Send an SMS reminder the day before the appointment
            - Let barbers see and edit their daily schedule
            - Let customers cancel through a link in the SMS
API:        REST
            GET  /barbers/{id}/slots?date={date}&service={id}
            POST /appointments
            DELETE /appointments/{token}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js, Twilio (SMS)
```

---

## Example 29

**Intent:**
a bug tracker for my dev team

**Spec:**
```
Type:       Web application (issue tracker)
Auth:       Email + password login, invite-only per project
Data model: User(id, email, name)
            Project(id, name, key)
            Issue(id, project_id -> Project, number, title, description, status, priority, assignee_id -> User)
            Comment(id, issue_id -> Issue, author_id -> User, body, created_at)
            Attachment(id, issue_id -> Issue, file_url, filename)
Features:   - Create issues with priority, labels and an assignee
            - Move issues through statuses: open, in progress, review, closed
            - Comment on issues and attach screenshots
            - Filter issues by status, assignee and label
            - Link issues to GitHub commits by issue key
API:        REST
            GET  /projects/{key}/issues
            POST /projects/{key}/issues
            PATCH /issues/{id}
            POST /issues/{id}/comments
            POST /webhooks/github
Storage:    PostgreSQL, S3 (attachments)
Tech stack: TypeScript, Express, React, Prisma
```

---

## Example 30

**Intent:**
trello like kanban board where my team sees changes live

**Spec:**
```
Type:       Web application (real-time collaborative)
Auth:       Email + password or GitHub login
Data model: User(id, email, name, avatar_url)
            Board(id, name, owner_id -> User)
            BoardMember(id, board_id -> Board, user_id -> User, role)
            List(id, board_id -> Board, title, position)
            Card(id, list_id -> List, title, description, position, due_date, assignee_id -> User)
Features:   - Create boards, lists and cards
            - Drag cards between lists and reorder them
            - Broadcast every change to other members in real time
            - Assign cards to members and set due dates
            - Invite members to a board by email
API:        REST + WebSocket
            GET  /boards/{id}
            POST /lists/{id}/cards
            PATCH /cards/{id}
            WS   /boards/{id}/events
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView, Ecto
```

---

## Example 31

**Intent:**
something to make surveys and send them to people

**Spec:**
```
Type:       Web application (survey builder)
Auth:       Email + password login for survey creators; respondents answer anonymously
Data model: User(id, email, password_hash)
            Survey(id, owner_id -> User, title, is_open, public_token)
            Question(id, survey_id -> Survey, type, text, options, position)
            Response(id, survey_id -> Survey, submitted_at)
            Answer(id, response_id -> Response, question_id -> Question, value)
Features:   - Build surveys with multiple choice, rating and text questions
            - Share a public link to collect responses
            - Show results as charts per question
            - Close a survey to stop new responses
            - Export responses as CSV
API:        REST
            POST /surveys
            GET  /s/{token}
            POST /s/{token}/responses
            GET  /surveys/{id}/results
Storage:    PostgreSQL
Tech stack: Python, Django, Chart.js
```

---

## Example 32

**Intent:**
website for our book club, members suggest books, vote on next one and discuss

**Spec:**
```
Type:       Web application (community)
Auth:       Invite link + email magic link login
Data model: Member(id, email, name)
            Book(id, title, author, cover_url, suggested_by -> Member)
            Vote(id, book_id -> Book, member_id -> Member, round_id -> Round)
            Round(id, month, chosen_book_id -> Book, closes_at)
            Comment(id, book_id -> Book, member_id -> Member, text, created_at)
Features:   - Suggest books by searching the Open Library catalog
            - Vote once per round on the next book
            - Close the round and announce the winner by email
            - Discuss each book in a comment thread
            - Show the history of books read
API:        REST
            GET  /books/search?q={title}
            POST /books
            POST /rounds/{id}/votes
            POST /books/{id}/comments
Storage:    SQLite
Tech stack: Ruby, Sinatra, Open Library API, Postmark
```

---

## Example 33

**Intent:**
a place for students on my campus to sell used textbooks to each other

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Login with university email only (magic link to .edu address)
Data model: Student(id, email, name, campus)
            Listing(id, seller_id -> Student, isbn, title, course_code, condition, price, status)
            Message(id, listing_id -> Listing, sender_id -> Student, receiver_id -> Student, text, sent_at)
Features:   - Create a listing by scanning or typing the ISBN
            - Fill in title and cover automatically from the ISBN
            - Search listings by course code or title
            - Message the seller inside the site
            - Mark a listing as sold
API:        REST
            GET  /listings?course={code}
            POST /listings
            GET  /isbn/{isbn}
            POST /listings/{id}/messages
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Supabase, Google Books API
```

---

## Example 34

**Intent:**
farmers market vendors list their produce and customers can preorder for saturday pickup

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Vendor login with email + password; customers order with email
Data model: Vendor(id, name, email, password_hash, stall_number)
            Product(id, vendor_id -> Vendor, name, unit, price, weekly_quantity)
            Preorder(id, customer_email, pickup_date, status)
            PreorderItem(id, preorder_id -> Preorder, product_id -> Product, quantity)
Features:   - Show each vendor's produce for the coming Saturday
            - Preorder items from several vendors in one cart
            - Close preorders on Thursday night automatically
            - Give each vendor a packing list for their orders
            - Email customers a pickup reminder on Saturday morning
API:        REST
            GET  /vendors
            GET  /vendors/{id}/products
            POST /preorders
            GET  /vendors/me/packing-list
Storage:    PostgreSQL
Tech stack: Python, Flask, Jinja2, APScheduler
```

---

## Example 35

**Intent:**
community events calendar for our town

**Spec:**
```
Type:       Web application (CRUD)
Auth:       Email + password login for organizers; admin approves new organizers
Data model: Organizer(id, name, email, password_hash, approved)
            Event(id, organizer_id -> Organizer, title, description, location, starts_at, ends_at, category, status)
Features:   - Submit events with date, place and category
            - Approve or reject submitted events as an admin
            - Show events in month, week and list views
            - Filter events by category
            - Subscribe to the calendar as an iCal feed
API:        REST
            GET  /events?from={date}&to={date}
            POST /events
            PATCH /admin/events/{id}
            GET  /calendar.ics
Storage:    MySQL
Tech stack: PHP, Symfony, FullCalendar
```

---

## Example 36

**Intent:**
website for my podcast with episodes and show notes

**Spec:**
```
Type:       Web application (CMS)
Auth:       Single admin login for the host
Data model: Episode(id, number, title, slug, audio_url, duration_sec, show_notes_md, published_at)
            Guest(id, name, bio, website)
            EpisodeGuest(episode_id -> Episode, guest_id -> Guest)
Features:   - Publish episodes with audio upload and Markdown show notes
            - Play episodes in an embedded audio player
            - Generate an RSS feed compatible with Apple Podcasts and Spotify
            - Show guest pages with all their episodes
            - Search episodes by title and notes
API:        REST
            GET  /episodes
            GET  /episodes/{slug}
            POST /admin/episodes
            GET  /feed.xml
Storage:    PostgreSQL, S3 (audio files)
Tech stack: Python, Django, Wagtail CMS
```

---

## Example 37

**Intent:**
Our animal shelter needs a site to show adoptable pets and let people apply to adopt one.

**Spec:**
```
Type:       Web application (CRUD)
Auth:       Staff login with email + password; adopters apply without an account
Data model: Pet(id, name, species, breed, age_months, sex, description, photos, status)
            Application(id, pet_id -> Pet, applicant_name, email, phone, home_type, has_other_pets, message, status)
            Staff(id, email, password_hash, name)
Features:   - List adoptable pets with photos and filters by species and age
            - Submit an adoption application for a pet
            - Review applications and approve or reject them
            - Mark pets as adopted and hide them from the list
            - Email applicants when their status changes
API:        REST
            GET  /pets?species={s}
            GET  /pets/{id}
            POST /pets/{id}/applications
            PATCH /applications/{id}
Storage:    PostgreSQL, Cloudinary (photos)
Tech stack: Ruby, Ruby on Rails, Active Storage, Action Mailer
```

---

## Example 38

**Intent:**
rental listings site for apartments

**Spec:**
```
Type:       Web application (listings)
Auth:       Email + password login with landlord and tenant roles
Data model: User(id, email, password_hash, role, phone)
            Listing(id, landlord_id -> User, title, address, lat, lng, rent, bedrooms, available_from, photos)
            Inquiry(id, listing_id -> Listing, tenant_id -> User, message, created_at)
            SavedListing(id, user_id -> User, listing_id -> Listing)
Features:   - Post apartment listings with photos and details
            - Search listings by rent, bedrooms and area
            - Show listings on an interactive map
            - Save favourite listings
            - Send inquiries to landlords
API:        REST
            GET  /listings?min_rent={n}&max_rent={n}&beds={n}
            POST /listings
            POST /listings/{id}/inquiries
            POST /listings/{id}/save
Storage:    PostgreSQL with PostGIS
Tech stack: TypeScript, Nuxt, Node.js, Leaflet, OpenStreetMap
```

---

## Example 39

**Intent:**
freelance marketplace like fiverr but for video editors only

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Email + password login with client and editor roles
Data model: User(id, email, password_hash, role, display_name)
            Gig(id, editor_id -> User, title, description, price, delivery_days, sample_video_url)
            Order(id, gig_id -> Gig, client_id -> User, requirements, status, due_at)
            Delivery(id, order_id -> Order, file_url, note, delivered_at)
            Review(id, order_id -> Order, rating, text)
Features:   - Publish gigs with sample videos, price and delivery time
            - Order a gig and upload raw footage
            - Hold payment in escrow until the client accepts the delivery
            - Request revisions on a delivery
            - Rate the editor after the order is complete
API:        REST
            GET  /gigs?q={text}
            POST /gigs/{id}/orders
            POST /orders/{id}/deliveries
            POST /orders/{id}/accept
            POST /orders/{id}/review
Storage:    PostgreSQL, S3 (videos, multipart upload)
Tech stack: Python, FastAPI, React, Stripe Connect, AWS S3
```

---

## Example 40

**Intent:**
q&a site for our company like stackoverflow

**Spec:**
```
Type:       Web application (Q&A community)
Auth:       Single sign-on with Microsoft Entra ID (company accounts)
Data model: User(id, email, name, reputation)
            Question(id, author_id -> User, title, body, tags, accepted_answer_id -> Answer, created_at)
            Answer(id, question_id -> Question, author_id -> User, body, created_at)
            Vote(id, user_id -> User, target_type, target_id, value)
Features:   - Ask questions with tags and Markdown code blocks
            - Answer questions and accept the best answer
            - Vote on questions and answers to earn reputation
            - Search questions by text and tag
            - Suggest similar questions while typing a new one
API:        REST
            GET  /questions?tag={tag}
            POST /questions
            POST /questions/{id}/answers
            POST /votes
            GET  /search?q={text}
Storage:    PostgreSQL, Elasticsearch (search)
Tech stack: C#, ASP.NET Core, Blazor, Elasticsearch
```

---

## Example 41

**Intent:**
feature request board where users vote on ideas for my product

**Spec:**
```
Type:       Web application (SaaS feedback board)
Auth:       Email magic link login for voters; admin login for the product team
Data model: User(id, email, name)
            Idea(id, author_id -> User, title, description, status, vote_count)
            Vote(id, idea_id -> Idea, user_id -> User)
            Comment(id, idea_id -> Idea, user_id -> User, body)
            ChangelogEntry(id, title, body, published_at)
Features:   - Submit ideas and vote on them once per user
            - Sort ideas by votes or newest
            - Set idea status: planned, in progress, shipped
            - Notify voters when an idea is shipped
            - Publish a public changelog
API:        REST
            GET  /ideas?sort={votes|new}
            POST /ideas
            POST /ideas/{id}/vote
            PATCH /admin/ideas/{id}
            GET  /changelog
Storage:    PostgreSQL
Tech stack: TypeScript, Remix, Prisma, Postmark
```

---

## Example 42

**Intent:**
bookmark manager wiht tags that i can use from any browser

**Spec:**
```
Type:       Web application (CRUD)
Auth:       Email + password login
Data model: User(id, email, password_hash)
            Bookmark(id, user_id -> User, url, title, description, favicon_url, created_at)
            Tag(id, user_id -> User, name)
            BookmarkTag(bookmark_id -> Bookmark, tag_id -> Tag)
Features:   - Save bookmarks with a bookmarklet from any browser
            - Fetch the page title and favicon automatically
            - Tag bookmarks and filter by one or more tags
            - Search bookmarks by title, URL and description
            - Import bookmarks from a browser HTML export
API:        REST
            GET  /bookmarks?tag={tag}&q={text}
            POST /bookmarks
            PUT  /bookmarks/{id}
            DELETE /bookmarks/{id}
            POST /import
Storage:    SQLite
Tech stack: Go, Echo, HTMX, Tailwind CSS
```

---

## Example 43

**Intent:**
desk booking for our coworking space

**Spec:**
```
Type:       Web application (booking system)
Auth:       Member login with email + password; admin role for the space manager
Data model: Member(id, email, name, plan, credits)
            Desk(id, name, zone, has_monitor)
            Booking(id, desk_id -> Desk, member_id -> Member, date, half_day)
Features:   - Show a floor map with free and booked desks per day
            - Book a desk for a full or half day
            - Deduct booking credits based on the member's plan
            - Cancel bookings until 9am on the same day
            - Show occupancy reports to the manager
API:        REST
            GET  /desks?date={date}
            POST /bookings
            DELETE /bookings/{id}
            GET  /admin/occupancy?month={yyyy-mm}
Storage:    PostgreSQL
Tech stack: Python, Django, React, react-konva (floor map)
```

---

## Example 44

**Intent:**
inventory tracker

**Spec:**
```
Type:       Web application (CRUD)
Auth:       Email + password login with admin and staff roles
Data model: Item(id, sku, name, category, unit, reorder_level)
            Location(id, name)
            StockLevel(item_id -> Item, location_id -> Location, quantity)
            Movement(id, item_id -> Item, from_location_id -> Location, to_location_id -> Location, quantity, reason, created_at)
Features:   - Add, edit and archive items with SKU and category
            - Record stock in, stock out and transfers between locations
            - Show current stock per item and location
            - Highlight items below their reorder level
            - Export stock reports as CSV
API:        REST
            GET  /items
            POST /items
            POST /movements
            GET  /stock?location={id}
            GET  /reports/low-stock
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Spring Security, React
```

---

## Example 45

**Intent:**
Helpdesk ticket system for our customer support team. Customers should be able to email support@ and it becomes a ticket, then agents reply from the web app and the customer gets the reply by email. We also need canned responses and SLA timers.

**Spec:**
```
Type:       Web application (helpdesk SaaS)
Auth:       Agent login with email + password and 2FA; customers interact by email only
Data model: Agent(id, email, name, password_hash, team)
            Customer(id, email, name)
            Ticket(id, customer_id -> Customer, subject, status, priority, assignee_id -> Agent, sla_due_at)
            Message(id, ticket_id -> Ticket, sender_type, body, created_at)
            CannedResponse(id, title, body)
Features:   - Turn incoming support emails into tickets and thread replies
            - Reply to tickets from the web app and send replies by email
            - Assign tickets to agents and set priority
            - Insert canned responses into replies
            - Show SLA countdowns and flag breached tickets
            - Report response times per agent
API:        REST
            POST /inbound/email
            GET  /tickets?status={s}&assignee={id}
            POST /tickets/{id}/replies
            PATCH /tickets/{id}
            GET  /canned-responses
Storage:    PostgreSQL
Tech stack: Ruby, Ruby on Rails, Action Mailbox, Hotwire, Sidekiq
```

---

## Example 46

**Intent:**
newsletter platform like substack

**Spec:**
```
Type:       Web application (publishing platform)
Auth:       Email + password login for writers; readers subscribe with email
Data model: Writer(id, email, password_hash, publication_name)
            Post(id, writer_id -> Writer, title, body_html, is_paid, published_at)
            Subscriber(id, writer_id -> Writer, email, tier, status)
            EmailSend(id, post_id -> Post, subscriber_id -> Subscriber, opened_at)
Features:   - Write posts in a rich-text editor
            - Publish posts to the web and send them by email to subscribers
            - Offer free and paid subscription tiers
            - Hide paid posts behind a paywall
            - Track email opens and subscriber growth
API:        REST
            POST /posts
            POST /posts/{id}/publish
            POST /subscribe
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Tiptap, Amazon SES, Stripe
```

---

## Example 47

**Intent:**
i want to sell my online courses, videos split in lessons and students track progress

**Spec:**
```
Type:       Web application (learning platform)
Auth:       Email + password login, admin role for the course creator
Data model: Course(id, title, description, price)
            Lesson(id, course_id -> Course, title, video_url, position)
            Enrollment(id, course_id -> Course, student_id -> Student, purchased_at)
            Student(id, email, password_hash, name)
            Progress(id, student_id -> Student, lesson_id -> Lesson, completed_at)
Features:   - Buy a course with card payment
            - Stream lesson videos only to enrolled students
            - Mark lessons complete and show course progress
            - Issue a PDF certificate when a course is finished
            - Upload and reorder lessons as the creator
API:        REST
            GET  /courses
            POST /courses/{id}/checkout
            GET  /lessons/{id}/stream
            POST /lessons/{id}/complete
Storage:    PostgreSQL, Mux (video hosting)
Tech stack: PHP, Laravel, Inertia.js, Vue.js, Mux, Stripe
```

---

## Example 48

**Intent:**
wedding website where guests can RSVP

**Spec:**
```
Type:       Web application (event site)
Auth:       Guests enter a personal invite code; couple logs in as admin
Data model: Invite(id, code, household_name, max_guests)
            Guest(id, invite_id -> Invite, name, attending, meal_choice, dietary_notes)
Features:   - Show the schedule, venue map and travel info
            - RSVP for each guest in the household with a meal choice
            - Limit the number of guests per invite
            - Show the couple a live RSVP count and meal totals
            - Export the guest list as CSV for the caterer
API:        REST
            GET  /invites/{code}
            POST /invites/{code}/rsvp
            GET  /admin/guests
Storage:    Supabase (PostgreSQL)
Tech stack: SvelteKit, Supabase, Google Maps embed
```

---

## Example 49

**Intent:**
google docs style editor but for markdown where my team edits same doc together

**Spec:**
```
Type:       Web application (real-time collaborative)
Auth:       Email + password or Google login; documents shared by invite
Data model: User(id, email, name)
            Document(id, owner_id -> User, title, ydoc_state, updated_at)
            Share(id, document_id -> Document, user_id -> User, permission)
            Comment(id, document_id -> Document, user_id -> User, anchor, body, resolved)
Features:   - Edit Markdown documents together with live cursors
            - Merge concurrent edits without conflicts using CRDTs
            - Show a live preview of the rendered Markdown
            - Share documents with view or edit permission
            - Comment on selected text and resolve comments
            - Keep a version history with restore
API:        REST + WebSocket
            GET  /documents
            POST /documents
            POST /documents/{id}/shares
            WS   /documents/{id}/collab
Storage:    PostgreSQL
Tech stack: TypeScript, React, CodeMirror 6, Yjs, Hocuspocus server
```

---

## Example 50

**Intent:**
status page for our saas showing if services are up or down

**Spec:**
```
Type:       Web application (status page)
Auth:       Admin login with email + password; public page needs no login
Data model: Component(id, name, group, status)
            Incident(id, title, impact, status, started_at, resolved_at)
            IncidentUpdate(id, incident_id -> Incident, message, status, created_at)
            Subscriber(id, email, confirmed)
Features:   - Show the current status of each service component
            - Post incidents with timeline updates
            - Show 90-day uptime bars per component
            - Email subscribers when an incident is created or resolved
            - Schedule maintenance windows
API:        REST
            GET  /status
            POST /incidents
            POST /incidents/{id}/updates
            POST /subscribe
Storage:    PostgreSQL
Tech stack: Python, Flask, HTMX, Amazon SES
```

---

## Example 51

**Intent:**
neighbours lending tools to each other, like a ladder or drill

**Spec:**
```
Type:       Web application (sharing community)
Auth:       Email + password login with address verification by postcard code
Data model: User(id, email, name, neighbourhood, verified)
            Tool(id, owner_id -> User, name, description, photo_url, available)
            Loan(id, tool_id -> Tool, borrower_id -> User, start_date, end_date, status)
Features:   - List tools available to lend with a photo
            - Browse tools in your own neighbourhood only
            - Request to borrow a tool for a date range
            - Approve or decline loan requests
            - Remind borrowers by email when a tool is due back
API:        REST
            GET  /tools?neighbourhood={id}
            POST /tools
            POST /tools/{id}/loans
            PATCH /loans/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, Express, React, Cloudinary
```

---

## Example 52

**Intent:**
e-shop for car parts where customer select his car model and see only parts which fit

**Spec:**
```
Type:       Web application (e-commerce)
Auth:       Customer accounts with email + password, guest checkout allowed
Data model: Vehicle(id, make, model, year_from, year_to, engine)
            Part(id, sku, name, brand, price, stock)
            Fitment(part_id -> Part, vehicle_id -> Vehicle)
            Order(id, customer_id -> Customer, total, status, shipping_address)
            Customer(id, email, password_hash, saved_vehicle_id -> Vehicle)
Features:   - Select make, model, year and engine to set "my car"
            - Show only parts that fit the selected vehicle
            - Search parts by name, SKU or OEM number
            - Check out with card or PayPal
            - Import parts and fitment data from supplier CSV files
API:        REST
            GET  /vehicles/makes
            GET  /parts?vehicle={id}&q={text}
            POST /orders
            POST /admin/import
Storage:    PostgreSQL, Meilisearch (part search)
Tech stack: PHP, Symfony, Meilisearch, Stripe, PayPal
```

---

## Example 53

**Intent:**
print on demand tshirt shop where people upload their own design

**Spec:**
```
Type:       Web application (e-commerce)
Auth:       Optional customer accounts; guest checkout
Data model: Design(id, image_url, width_px, height_px, uploaded_at)
            Product(id, garment_type, color, size, base_price)
            Order(id, email, shipping_address, total, status, fulfillment_id)
            OrderItem(id, order_id -> Order, product_id -> Product, design_id -> Design, quantity)
Features:   - Upload a design and preview it on a t-shirt mockup
            - Warn when the design resolution is too low for print
            - Choose garment, color and size
            - Pay by card and send the order to a print provider
            - Show tracking info once the shirt is shipped
API:        REST
            POST /designs
            POST /orders
            POST /webhooks/printful
Storage:    PostgreSQL, S3 (designs)
Tech stack: TypeScript, Next.js, Fabric.js (mockup editor), Printful API, Stripe
```

---

## Example 54

**Intent:**
sell my ebooks and pdf templates as downloads

**Spec:**
```
Type:       Web application (digital store)
Auth:       Buyers receive a download link by email; admin login for the seller
Data model: Product(id, title, description, price, file_key)
            Purchase(id, product_id -> Product, email, paid_at, download_count)
            DownloadToken(id, purchase_id -> Purchase, token, expires_at)
Features:   - List products with cover images and descriptions
            - Pay with Stripe Checkout
            - Email a time-limited download link after payment
            - Limit each purchase to 5 downloads
            - Offer discount codes
API:        REST
            GET  /products
            POST /checkout
            POST /webhooks/stripe
            GET  /download/{token}
Storage:    SQLite, S3 (files with signed URLs)
Tech stack: Python, Flask, Stripe, boto3
```

---

## Example 55

**Intent:**
Classifieds website like craigslist

**Spec:**
```
Type:       Web application (classifieds)
Auth:       Email + password login with email verification
Data model: User(id, email, password_hash, phone)
            Category(id, name, parent_id -> Category)
            Ad(id, user_id -> User, category_id -> Category, title, body, price, city, photos, expires_at)
            Report(id, ad_id -> Ad, reason, created_at)
Features:   - Post ads with photos in a category and city
            - Browse and search ads by category, city and price
            - Contact the seller through a relay email that hides addresses
            - Expire ads automatically after 30 days
            - Report spam ads for moderator review
API:        REST
            GET  /ads?category={id}&city={city}
            POST /ads
            POST /ads/{id}/contact
            POST /ads/{id}/report
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, PostgreSQL full-text search, Celery
```

---

## Example 56

**Intent:**
I run an amateur football league with 12 teams. I want a website with the fixtures, results, league table and top scorers, and team captains should be able to enter match scores themselves after each game.

**Spec:**
```
Type:       Web application (sports league management)
Auth:       Captain and admin login with email + password; public pages need no login
Data model: Team(id, name, captain_id -> User)
            User(id, email, password_hash, role)
            Player(id, team_id -> Team, name, number)
            Match(id, home_team_id -> Team, away_team_id -> Team, kickoff_at, home_score, away_score, status)
            Goal(id, match_id -> Match, player_id -> Player, minute)
Features:   - Generate a round-robin fixture list for the season
            - Let captains submit scores and goal scorers after a match
            - Require the other captain to confirm the result
            - Calculate the league table with points and goal difference
            - Show a top scorers list
API:        REST
            GET  /fixtures
            GET  /table
            POST /matches/{id}/result
            POST /matches/{id}/confirm
            GET  /scorers
Storage:    PostgreSQL
Tech stack: Ruby, Ruby on Rails, Tailwind CSS
```

---

## Example 57

**Intent:**
volunteer shift signup for our food bank

**Spec:**
```
Type:       Web application (scheduling)
Auth:       Volunteer login with email magic link; coordinator admin role
Data model: Volunteer(id, email, name, phone)
            Shift(id, date, start_time, end_time, role, slots)
            Signup(id, shift_id -> Shift, volunteer_id -> Volunteer, status)
Features:   - Show upcoming shifts with remaining open slots
            - Sign up for and cancel shifts
            - Send a reminder email 24 hours before a shift
            - Let coordinators create recurring weekly shifts
            - Track volunteer hours per person
API:        REST
            GET  /shifts?from={date}
            POST /shifts/{id}/signups
            DELETE /signups/{id}
            GET  /admin/hours
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Jinja2, HTMX, Celery
```

---

## Example 58

**Intent:**
i need a website for my clinic where patients can book apointment with doctor, please make in django

**Spec:**
```
Type:       Web application (booking system)
Auth:       Patient registration with email + password; doctor and receptionist staff roles
Data model: Patient(id, user_id -> User, name, phone, date_of_birth)
            Doctor(id, user_id -> User, name, specialty)
            Schedule(id, doctor_id -> Doctor, weekday, start_time, end_time, slot_minutes)
            Appointment(id, patient_id -> Patient, doctor_id -> Doctor, starts_at, reason, status)
            User(id, email, password_hash, role)
Features:   - Show each doctor's free slots based on their weekly schedule
            - Book, reschedule and cancel appointments
            - Send email and SMS reminders the day before
            - Let receptionists see the daily appointment list per doctor
            - Block holidays and leave days for doctors
API:        REST
            GET  /doctors
            GET  /doctors/{id}/slots?date={date}
            POST /appointments
            PATCH /appointments/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Django REST Framework, Celery, Twilio
```

---

## Example 59

**Intent:**
QR code menu for my cafe where people order from the table

**Spec:**
```
Type:       Web application (online ordering)
Auth:       Staff login with PIN code; customers order without an account
Data model: Table(id, number, qr_token)
            MenuItem(id, category, name, description, price, available)
            Order(id, table_id -> Table, status, total, created_at)
            OrderItem(id, order_id -> Order, menu_item_id -> MenuItem, quantity, note)
Features:   - Open the menu by scanning the QR code on the table
            - Add items with notes and place an order linked to the table
            - Show new orders live on a kitchen screen
            - Mark orders as preparing, served and paid
            - Hide sold-out items from the menu
API:        REST + WebSocket
            GET  /t/{qr_token}/menu
            POST /t/{qr_token}/orders
            PATCH /orders/{id}
            WS   /kitchen/orders
Storage:    PostgreSQL
Tech stack: TypeScript, Express, Socket.IO, React, qrcode
```

---

## Example 60

**Intent:**
food delivery platform with many restaurants, customers, and couriers

**Spec:**
```
Type:       Web application (multi-sided marketplace)
Auth:       Email + password or phone OTP login with customer, restaurant and courier roles
Data model: Restaurant(id, owner_id -> User, name, address, lat, lng, is_open)
            MenuItem(id, restaurant_id -> Restaurant, name, price, available)
            Order(id, customer_id -> User, restaurant_id -> Restaurant, courier_id -> User, status, total, delivery_address)
            CourierLocation(courier_id -> User, lat, lng, updated_at)
            User(id, phone, email, role)
Features:   - Browse nearby restaurants and order from their menu
            - Let restaurants accept orders and set preparation time
            - Assign the nearest available courier to ready orders
            - Track the courier's position live on a map
            - Pay by card and split the payment between restaurant, courier and platform
API:        REST + WebSocket
            GET  /restaurants?lat={lat}&lng={lng}
            POST /orders
            PATCH /orders/{id}/status
            POST /couriers/me/location
            WS   /orders/{id}/track
Storage:    PostgreSQL with PostGIS, Redis (courier locations)
Tech stack: Java, Spring Boot, React, Mapbox, Stripe Connect
```

---

## Example 61

**Intent:**
kahoot style quiz game in the browser, host shows questions and players answer on their phones

**Spec:**
```
Type:       Web application (real-time multiplayer)
Auth:       Host login with email + password; players join with a game PIN and nickname
Data model: Quiz(id, host_id -> User, title)
            Question(id, quiz_id -> Quiz, text, options, correct_index, time_limit_sec)
            Game(id, quiz_id -> Quiz, pin, status, started_at)
            Player(id, game_id -> Game, nickname, score)
            User(id, email, password_hash)
Features:   - Create quizzes with multiple choice questions and time limits
            - Start a game and show a PIN for players to join
            - Push each question to all players at the same time
            - Score answers by correctness and speed
            - Show a live leaderboard after each question
API:        REST + WebSocket
            POST /quizzes
            POST /quizzes/{id}/games
            WS   /games/{pin}
Storage:    PostgreSQL (quizzes), Redis (live game state)
Tech stack: TypeScript, Node.js, Socket.IO, React
```

---

## Example 62

**Intent:**
shared grocery list for my family that updates live when someone adds stuff

**Spec:**
```
Type:       Web application (real-time collaborative, PWA)
Auth:       Email magic link login; family members join a household by invite link
Data model: Household(id, name, invite_code)
            User(id, email, name, household_id -> Household)
            Item(id, household_id -> Household, name, quantity, checked, added_by -> User)
Features:   - Add, edit and tick off items on a shared list
            - Sync changes to everyone in the household instantly
            - Group items by store aisle
            - Clear all ticked items with one tap
            - Install on phones as a progressive web app
Storage:    Supabase (PostgreSQL with Realtime)
Tech stack: Vue.js, Supabase Realtime, Vite PWA plugin
```

---

## Example 63

**Intent:**
async standup tool, everyone writes what they did yesterday/today/blockers and it posts summary to slack

**Spec:**
```
Type:       Web application (team SaaS)
Auth:       Sign in with Slack (OAuth)
Data model: Workspace(id, slack_team_id, name, bot_token)
            Team(id, workspace_id -> Workspace, name, channel_id, standup_time, timezone)
            Member(id, team_id -> Team, slack_user_id, name)
            Update(id, member_id -> Member, date, yesterday, today, blockers)
Features:   - Ask each member for their standup via Slack DM at the set time
            - Collect answers in the web app or directly in Slack
            - Post a combined summary to the team's channel
            - Highlight blockers at the top of the summary
            - Show each member's update history
API:        REST
            GET  /oauth/slack/callback
            POST /slack/events
            GET  /teams/{id}/updates?date={date}
            POST /teams/{id}/updates
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Slack Bolt SDK, React
```

---

## Example 64

**Intent:**
time tracker for freelancers with invoices

**Spec:**
```
Type:       Web application (SaaS)
Auth:       Email + password login
Data model: User(id, email, password_hash, hourly_rate, currency)
            Client(id, user_id -> User, name, email)
            Project(id, client_id -> Client, name, rate_override)
            TimeEntry(id, project_id -> Project, started_at, ended_at, description, invoiced)
            Invoice(id, client_id -> Client, number, total, status, issued_at)
Features:   - Start and stop a timer for a project
            - Add and edit time entries manually
            - Show weekly hours per client and project
            - Turn uninvoiced entries into an invoice PDF
            - Mark invoices as sent and paid
API:        REST
            POST /timer/start
            POST /timer/stop
            GET  /entries?week={yyyy-ww}
            POST /clients/{id}/invoices
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Drizzle ORM, react-pdf
```

---

## Example 65

**Intent:**
simple crm for our marketing agency using laravel

**Spec:**
```
Type:       Web application (CRM)
Auth:       Email + password login with admin and account manager roles
Data model: Company(id, name, industry, website)
            Contact(id, company_id -> Company, name, email, phone, position)
            Deal(id, company_id -> Company, owner_id -> User, title, value, stage, expected_close)
            Activity(id, deal_id -> Deal, user_id -> User, type, note, due_at, done)
            User(id, email, password_hash, role)
Features:   - Manage companies and their contacts
            - Track deals on a pipeline board by stage
            - Log calls, meetings and emails against deals
            - Remind account managers about due follow-ups
            - Report won and lost deal value per month
API:        REST
            GET  /deals?stage={stage}
            POST /deals
            PATCH /deals/{id}
            POST /deals/{id}/activities
Storage:    MySQL
Tech stack: PHP, Laravel, Filament admin panel
```

---

## Example 66

**Intent:**
split bills with friends app like splitwise but web

**Spec:**
```
Type:       Web application (CRUD)
Auth:       Email + password or Google login
Data model: User(id, email, name)
            Group(id, name, currency)
            GroupMember(group_id -> Group, user_id -> User)
            Expense(id, group_id -> Group, payer_id -> User, amount, description, date)
            Share(id, expense_id -> Expense, user_id -> User, amount)
Features:   - Create groups and invite friends by email
            - Add expenses split equally, by percentage or by exact amounts
            - Show who owes whom in each group
            - Simplify debts to the fewest payments
            - Record settle-up payments
API:        REST
            POST /groups
            POST /groups/{id}/expenses
            GET  /groups/{id}/balances
            POST /groups/{id}/settlements
Storage:    PostgreSQL
Tech stack: Python, Django, Django REST Framework, React
```

---

## Example 67

**Intent:**
Tenants of my 3 buildings should report repair problems online with photos, and I want to assign them to the handyman and see what is still open.

**Spec:**
```
Type:       Web application (maintenance portal)
Auth:       Tenant login with email + password; landlord and handyman roles
Data model: Building(id, name, address)
            Unit(id, building_id -> Building, number, tenant_id -> User)
            Request(id, unit_id -> Unit, category, description, photos, urgency, status, assignee_id -> User)
            RequestNote(id, request_id -> Request, author_id -> User, text, created_at)
            User(id, email, password_hash, role)
Features:   - Submit repair requests with photos and urgency
            - Assign requests to a handyman
            - Update request status and add notes
            - Notify the tenant by email on each status change
            - Show open requests per building on a dashboard
API:        REST
            POST /requests
            GET  /requests?status={s}&building={id}
            PATCH /requests/{id}
            POST /requests/{id}/notes
Storage:    PostgreSQL, S3 (photos)
Tech stack: Ruby, Ruby on Rails, Active Storage, Turbo
```

---

## Example 68

**Intent:**
portal for my school where students submit homework and teachers grade it

**Spec:**
```
Type:       Web application (education portal)
Auth:       Login with school Google accounts; teacher and student roles
Data model: Class(id, name, teacher_id -> User)
            Enrollment(class_id -> Class, student_id -> User)
            Assignment(id, class_id -> Class, title, instructions, due_at, max_points)
            Submission(id, assignment_id -> Assignment, student_id -> User, file_url, submitted_at, grade, feedback)
            User(id, email, name, role)
Features:   - Create assignments with due dates and attachments
            - Upload homework files before the deadline
            - Mark submissions as late after the due date
            - Grade submissions with points and written feedback
            - Show students their grades per class
API:        REST
            GET  /classes/{id}/assignments
            POST /assignments/{id}/submissions
            PATCH /submissions/{id}/grade
            GET  /me/grades
Storage:    PostgreSQL, Google Cloud Storage (files)
Tech stack: Python, Flask, Flask-Dance (Google OAuth), Bootstrap
```

---

## Example 69

**Intent:**
alumni directory for my university, alumni can find each other by city and industry

**Spec:**
```
Type:       Web application (directory)
Auth:       Email + password login, verified against the alumni graduation list
Data model: Alumnus(id, email, name, graduation_year, degree, city, industry, company, linkedin_url, visible)
            ConnectionRequest(id, from_id -> Alumnus, to_id -> Alumnus, message, status)
Features:   - Create and edit an alumni profile
            - Search alumni by city, industry, company and graduation year
            - Hide the profile from search if the user wants
            - Send connection requests with a short message
            - Show alumni on a world map
API:        REST
            GET  /alumni?city={c}&industry={i}
            PUT  /me/profile
            POST /alumni/{id}/connect
Storage:    PostgreSQL
Tech stack: TypeScript, Angular, NestJS, Leaflet
```

---

## Example 70

**Intent:**
platform where artists upload their artwork and people can follow them and like stuff

**Spec:**
```
Type:       Web application (social portfolio)
Auth:       Email + password or Google login
Data model: User(id, username, email, bio, avatar_url)
            Artwork(id, artist_id -> User, title, image_url, tags, created_at)
            Follow(follower_id -> User, followed_id -> User)
            Like(user_id -> User, artwork_id -> Artwork)
            Comment(id, artwork_id -> Artwork, user_id -> User, text)
Features:   - Upload artworks with title and tags
            - Follow artists and see their new work in a feed
            - Like and comment on artworks
            - Browse trending artworks by tag
            - Show each artist's portfolio page
API:        REST
            GET  /feed
            POST /artworks
            POST /artworks/{id}/like
            POST /users/{id}/follow
            GET  /explore?tag={tag}
Storage:    PostgreSQL, Cloudflare R2 (images)
Tech stack: TypeScript, SvelteKit, Drizzle ORM, Cloudflare R2
```

---

## Example 71

**Intent:**
photo contest site

**Spec:**
```
Type:       Web application (contest)
Auth:       Email + password login with email verification
Data model: Contest(id, title, theme, submission_deadline, voting_deadline)
            Entry(id, contest_id -> Contest, user_id -> User, photo_url, title)
            Vote(id, entry_id -> Entry, user_id -> User)
            User(id, email, password_hash, name)
Features:   - Submit one photo per user per contest
            - Vote for up to three entries during the voting period
            - Prevent voting for your own entry
            - Announce winners automatically after voting closes
            - Show a gallery of past winners
API:        REST
            GET  /contests
            POST /contests/{id}/entries
            POST /entries/{id}/vote
            GET  /contests/{id}/results
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 72

**Intent:**
movie watchlist site where u can see what friends are watching

**Spec:**
```
Type:       Web application (social)
Auth:       Email + password login
Data model: User(id, username, email, password_hash)
            Movie(id, tmdb_id, title, poster_url, year)
            WatchlistItem(id, user_id -> User, movie_id -> Movie, status, rating, updated_at)
            Friendship(id, user_id -> User, friend_id -> User, status)
Features:   - Search movies from the TMDB database
            - Add movies to a watchlist and mark them as watched
            - Rate watched movies
            - Add friends and see their recent activity
            - Show movies that several friends want to watch
API:        REST
            GET  /movies/search?q={title}
            POST /watchlist
            PATCH /watchlist/{id}
            GET  /friends/activity
Storage:    PostgreSQL
Tech stack: TypeScript, Express, React, TMDB API
```

---

## Example 73

**Intent:**
book review site

**Spec:**
```
Type:       Web application (reviews)
Auth:       Email + password login
Data model: User(id, username, email, password_hash)
            Book(id, isbn, title, author, cover_url, published_year)
            Review(id, book_id -> Book, user_id -> User, rating, text, created_at)
            Shelf(id, user_id -> User, book_id -> Book, shelf_name)
Features:   - Search books and import details by ISBN
            - Write reviews with a 1-5 star rating
            - Show average rating per book
            - Put books on shelves: want to read, reading, read
            - Show a yearly reading goal and progress
API:        REST
            GET  /books?q={text}
            GET  /books/{id}
            POST /books/{id}/reviews
            POST /shelves
Storage:    PostgreSQL
Tech stack: Ruby, Ruby on Rails, Open Library API
```

---

## Example 74

**Intent:**
newsroom CMS for our local news site where reporters write articles and editors approve them before publishing

**Spec:**
```
Type:       Web application (CMS)
Auth:       Email + password login with reporter, editor and admin roles
Data model: User(id, email, password_hash, name, role)
            Article(id, author_id -> User, title, slug, body, section, status, published_at)
            ArticleRevision(id, article_id -> Article, body, edited_by -> User, created_at)
            Media(id, file_url, caption, credit)
Features:   - Write and save article drafts with images
            - Submit drafts for editor review
            - Approve, request changes or schedule articles for publishing
            - Keep revision history for each article
            - Show the published site by section with SEO metadata
API:        REST
            GET  /articles?status={s}
            POST /articles
            POST /articles/{id}/submit
            POST /articles/{id}/publish
Storage:    PostgreSQL, S3 (media)
Tech stack: TypeScript, Strapi (headless CMS), Next.js frontend
```

---

## Example 75

**Intent:**
docs website for our open source library with versions for each release

**Spec:**
```
Type:       Web application (documentation site)
Data model: DocPage(version, path, title, body_md)
Features:   - Render Markdown docs with code highlighting
            - Switch between documentation versions with a dropdown
            - Search docs with instant results
            - Generate API reference pages from source comments
            - Deploy a new version automatically on each Git release tag
Storage:    Markdown files in the Git repository, Algolia DocSearch index
Tech stack: Docusaurus, React, TypeDoc, GitHub Actions, Algolia DocSearch
```

---

## Example 76

**Intent:**
pastebin clone for code snippets

**Spec:**
```
Type:       Web application (snippet sharing)
Auth:       Optional email + password login; anonymous pastes allowed
Data model: Paste(id, slug, user_id -> User, title, content, language, visibility, expires_at, created_at)
            User(id, email, password_hash)
Features:   - Create pastes with syntax highlighting for many languages
            - Set visibility to public, unlisted or private
            - Expire pastes after 1 hour, 1 day, 1 week or never
            - Show the raw text version of a paste
            - Fork an existing paste into a new one
API:        REST
            POST /pastes
            GET  /p/{slug}
            GET  /p/{slug}/raw
            DELETE /pastes/{id}
Storage:    PostgreSQL
Tech stack: Go, Gin, Chroma (syntax highlighting)
```

---

## Example 77

**Intent:**
image hosting site like imgur

**Spec:**
```
Type:       Web application (image hosting)
Auth:       Optional email + password login; anonymous uploads allowed
Data model: Image(id, user_id -> User, key, mime_type, width, height, size_bytes, views, created_at)
            Album(id, user_id -> User, title, privacy)
            User(id, email, password_hash)
Features:   - Upload images by drag and drop or paste from clipboard
            - Generate a short link and embed code for each image
            - Create thumbnails and WebP versions on upload
            - Group images into albums
            - Delete an anonymous upload with a secret delete link
API:        REST
            POST /images
            GET  /i/{id}
            DELETE /images/{id}?token={deleteToken}
            POST /albums
Storage:    S3 (images) behind CloudFront CDN, PostgreSQL (metadata)
Tech stack: Python, FastAPI, Pillow, boto3
```

---

## Example 78

**Intent:**
send big files with a link that expires after some days

**Spec:**
```
Type:       Web application (file sharing)
Auth:       Optional login; anonymous transfers allowed
Data model: Transfer(id, sender_email, recipient_emails, message, password_hash, expires_at, download_count)
            File(id, transfer_id -> Transfer, filename, size_bytes, storage_key)
Features:   - Upload large files with resumable chunked upload
            - Generate a download link that expires after 1 to 7 days
            - Protect a transfer with an optional password
            - Email the link to recipients
            - Delete files from storage after expiry
API:        REST
            POST /transfers
            POST /transfers/{id}/files
            GET  /d/{id}
            GET  /d/{id}/files/{fileId}
Storage:    S3 (files with lifecycle rules), PostgreSQL (metadata)
Tech stack: TypeScript, Express, tus (resumable uploads), React
```

---

## Example 79

**Intent:**
a calendly clone so people can book meetings with me

**Spec:**
```
Type:       Web application (scheduling)
Auth:       Google OAuth login for the host (for calendar access); bookers need no account
Data model: Host(id, email, name, google_refresh_token, timezone)
            EventType(id, host_id -> Host, name, duration_min, buffer_min, slug)
            Booking(id, event_type_id -> EventType, invitee_name, invitee_email, starts_at, status)
Features:   - Create meeting types with duration and buffer time
            - Read busy times from Google Calendar to show free slots
            - Show slots in the booker's own timezone
            - Create a calendar event with a Google Meet link on booking
            - Send confirmation and reschedule links by email
API:        REST
            GET  /{host}/{slug}/slots?date={date}
            POST /{host}/{slug}/bookings
            POST /bookings/{id}/cancel
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Google Calendar API, Prisma
```

---

## Example 80

**Intent:**
conference call for papers website, speakers submit talks and reviewers score them

**Spec:**
```
Type:       Web application (submission and review)
Auth:       Email + password or GitHub login; speaker, reviewer and organizer roles
Data model: Conference(id, name, cfp_closes_at)
            Submission(id, conference_id -> Conference, speaker_id -> User, title, abstract, level, status)
            Review(id, submission_id -> Submission, reviewer_id -> User, score, comment)
            User(id, email, name, role)
Features:   - Submit talk proposals before the deadline
            - Hide speaker names from reviewers for blind review
            - Score submissions from 1 to 5 with comments
            - Rank submissions by average score
            - Email accept or reject decisions to speakers
API:        REST
            POST /conferences/{id}/submissions
            GET  /reviewer/submissions
            POST /submissions/{id}/reviews
            POST /submissions/{id}/decision
Storage:    PostgreSQL
Tech stack: Python, Django, Django Allauth
```

---

## Example 81

**Intent:**
Platform for hackathon where participants without team can find teammates by skills

**Spec:**
```
Type:       Web application (matching platform)
Auth:       GitHub OAuth login
Data model: Participant(id, github_username, name, skills, looking_for_team)
            Team(id, name, idea, max_size, looking_for_skills)
            TeamMember(team_id -> Team, participant_id -> Participant)
            JoinRequest(id, team_id -> Team, participant_id -> Participant, status)
Features:   - Create a profile with skills taken from GitHub languages
            - Create a team and list the skills still needed
            - Suggest teams that match a participant's skills
            - Request to join a team and accept or decline requests
            - Lock teams when they reach the maximum size
API:        REST
            GET  /teams?skill={s}
            POST /teams
            POST /teams/{id}/requests
            PATCH /requests/{id}
Storage:    Firebase Firestore
Tech stack: React, Firebase Authentication (GitHub provider), Cloud Firestore
```

---

## Example 82

**Intent:**
mentorship matching site in flask, juniors get matched with senior devs

**Spec:**
```
Type:       Web application (matching platform)
Auth:       Email + password login with mentor and mentee roles
Data model: User(id, email, password_hash, role, name, bio)
            Profile(id, user_id -> User, skills, goals, experience_years, timezone, capacity)
            Match(id, mentor_id -> User, mentee_id -> User, status, started_at)
            Session(id, match_id -> Match, scheduled_at, notes)
Features:   - Fill in a profile with skills, goals and timezone
            - Suggest mentors ranked by skill overlap and timezone
            - Send and accept mentorship requests
            - Limit mentors to their chosen number of mentees
            - Log mentoring sessions with notes
API:        REST
            GET  /mentors/suggestions
            POST /matches
            PATCH /matches/{id}
            POST /matches/{id}/sessions
Storage:    PostgreSQL
Tech stack: Python, Flask, SQLAlchemy, Flask-Login, Jinja2
```

---

## Example 83

**Intent:**
carpool site for people in our office who live near each other

**Spec:**
```
Type:       Web application (ride sharing)
Auth:       Company Microsoft 365 login
Data model: Employee(id, email, name, home_lat, home_lng)
            Ride(id, driver_id -> Employee, date, departure_time, direction, seats)
            RideRequest(id, ride_id -> Ride, passenger_id -> Employee, status)
Features:   - Offer a ride with date, time and free seats
            - Find rides starting near your home on a map
            - Request a seat and let the driver accept it
            - Send a reminder notification the evening before
            - Show monthly CO2 saved per employee
API:        REST
            GET  /rides?date={date}&near={lat,lng}
            POST /rides
            POST /rides/{id}/requests
            PATCH /requests/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: C#, ASP.NET Core, Microsoft Identity Web, React, Leaflet
```

---

## Example 84

**Intent:**
lost and found for our campus, ppl post stuff they found and owners can claim it

**Spec:**
```
Type:       Web application (CRUD)
Auth:       University SSO login (SAML)
Data model: User(id, email, name)
            Item(id, finder_id -> User, title, description, category, found_location, found_at, photo_url, status)
            Claim(id, item_id -> Item, claimant_id -> User, proof_description, status)
Features:   - Post found items with a photo, place and date
            - Search items by category, place and date
            - Claim an item by describing a hidden detail
            - Let the finder approve or reject a claim
            - Archive unclaimed items after 60 days
API:        REST
            GET  /items?category={c}
            POST /items
            POST /items/{id}/claims
            PATCH /claims/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: TypeScript, NestJS, Angular, passport-saml
```

---

## Example 85

**Intent:**
I search a website for find roommate, people make profile with budget and habits and the system show who is good match

**Spec:**
```
Type:       Web application (matching platform)
Auth:       Email + password login with phone verification
Data model: User(id, email, password_hash, phone, verified)
            Profile(id, user_id -> User, city, budget_min, budget_max, move_in_date, smoker, pets, sleep_schedule, cleanliness)
            Like(id, from_id -> User, to_id -> User)
            Conversation(id, user_a_id -> User, user_b_id -> User)
            Message(id, conversation_id -> Conversation, sender_id -> User, text, sent_at)
Features:   - Create a profile with budget, move-in date and living habits
            - Calculate a compatibility score between two profiles
            - Show matches in the same city sorted by score
            - Open a chat when both users like each other
            - Report and block users
API:        REST + WebSocket
            GET  /matches
            POST /likes
            GET  /conversations/{id}/messages
            WS   /chat
Storage:    PostgreSQL
Tech stack: Python, Django, Django Channels, React
```

---

## Example 86

**Intent:**
coffee subscription shop with next.js and stripe, people get beans every 2 or 4 weeks

**Spec:**
```
Type:       Web application (subscription e-commerce)
Auth:       Customer login with email magic link
Data model: Customer(id, email, name, shipping_address, stripe_customer_id)
            Coffee(id, name, origin, roast, price_per_bag)
            Subscription(id, customer_id -> Customer, coffee_id -> Coffee, bags, interval_weeks, next_ship_date, stripe_subscription_id, status)
            Shipment(id, subscription_id -> Subscription, shipped_at, tracking_number)
Features:   - Choose coffee, number of bags and delivery interval
            - Charge customers automatically with Stripe subscriptions
            - Pause, skip or cancel a delivery from the account page
            - Generate a packing list of upcoming shipments each week
            - Email tracking numbers when orders ship
API:        REST
            GET  /coffees
            POST /subscriptions
            PATCH /subscriptions/{id}
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Stripe Billing, Prisma, Resend
```

---

## Example 87

**Intent:**
My bakery want a order form for custom cakes, customer choose size, flavour, decoration and the date for pick up, and we confirm it.

**Spec:**
```
Type:       Web application (order form)
Auth:       Staff login with email + password; customers order without an account
Data model: CakeOrder(id, customer_name, email, phone, size, flavour, filling, decoration_notes, reference_photo_url, pickup_date, price, status)
            BlockedDay(id, date, reason)
Features:   - Build a cake step by step with size, flavour and decoration
            - Show the price as options are chosen
            - Allow pickup dates at least 3 days ahead and not on blocked days
            - Upload a reference photo for the decoration
            - Let staff confirm or reject orders and email the customer
API:        REST
            GET  /availability?month={yyyy-mm}
            POST /orders
            PATCH /admin/orders/{id}
Storage:    SQLite
Tech stack: PHP, Laravel, Alpine.js, Mailgun
```

---

## Example 88

**Intent:**
live auction website using laravel where bids show up instantly for everyone

**Spec:**
```
Type:       Web application (real-time auction)
Auth:       Email + password login with verified payment card before bidding
Data model: User(id, email, password_hash, stripe_customer_id)
            Auction(id, seller_id -> User, title, description, photos, starting_price, reserve_price, ends_at, status)
            Bid(id, auction_id -> Auction, bidder_id -> User, amount, created_at)
Features:   - List items for auction with an end time and reserve price
            - Place bids that must beat the current highest bid
            - Broadcast new bids to all viewers in real time
            - Extend the auction by 2 minutes when a bid comes in at the last moment
            - Charge the winner's card when the auction closes
            - Email outbid notifications
API:        REST + WebSocket
            GET  /auctions
            POST /auctions
            POST /auctions/{id}/bids
            WS   /auctions/{id}
Storage:    MySQL, Redis (bid locking)
Tech stack: PHP, Laravel, Laravel Reverb, Livewire, Stripe
```

---

## Example 89

**Intent:**
plant swap community website

**Spec:**
```
Type:       Web application (community marketplace)
Auth:       Email + password login
Data model: User(id, email, password_hash, city)
            Plant(id, owner_id -> User, species, description, photo_url, type, status)
            SwapOffer(id, wanted_plant_id -> Plant, offered_plant_id -> Plant, status)
Features:   - List plants and cuttings available for swapping
            - Browse plants near your city
            - Offer one of your plants in exchange for another
            - Accept or decline swap offers
            - Leave feedback after a completed swap
API:        REST
            GET  /plants?city={c}
            POST /plants
            POST /plants/{id}/offers
            PATCH /offers/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Bootstrap
```

---

## Example 90

**Intent:**
fan wiki for a video game with item and monster pages that anyone can edit, built with nuxt

**Spec:**
```
Type:       Web application (wiki)
Auth:       Email + password or Discord login; trusted editors can revert edits
Data model: User(id, username, email, role)
            Page(id, slug, title, type, infobox_json, current_revision_id -> Revision)
            Revision(id, page_id -> Page, editor_id -> User, content_md, summary, created_at)
Features:   - Create item and monster pages with structured infoboxes
            - Edit pages in Markdown with a live preview
            - Compare any two revisions with a diff view
            - Revert vandalism to an earlier revision
            - Search pages and filter by page type
API:        REST
            GET  /pages/{slug}
            PUT  /pages/{slug}
            GET  /pages/{slug}/revisions
            POST /pages/{slug}/revert/{revisionId}
            GET  /search?q={text}
Storage:    PostgreSQL
Tech stack: Nuxt, Vue.js, Nitro server routes, Drizzle ORM, diff-match-patch
```

---

## Example 91

**Intent:**
budget tracker web app for me and my wife with supabase so we both see the same data

**Spec:**
```
Type:       Web application (CRUD)
Auth:       Supabase Auth (email + password), both partners in one shared household
Data model: Household(id, name)
            Profile(id, household_id -> Household, name)
            Category(id, household_id -> Household, name, monthly_limit)
            Transaction(id, household_id -> Household, category_id -> Category, paid_by -> Profile, amount, date, note)
Features:   - Add income and expenses with category and who paid
            - Set monthly limits per category
            - Show spending against limits for the current month
            - Show a chart of spending by category over time
            - Import transactions from a bank CSV export
Storage:    Supabase (PostgreSQL with row-level security)
Tech stack: React, Supabase, Recharts, Papa Parse
```

---

## Example 92

**Intent:**
habit tracker web app in rails

**Spec:**
```
Type:       Web application (CRUD)
Auth:       Email + password login (Devise)
Data model: User(id, email, encrypted_password, timezone)
            Habit(id, user_id -> User, name, frequency, target_days, color)
            Checkin(id, habit_id -> Habit, date)
Features:   - Create daily or weekly habits
            - Check off habits for today
            - Show current and longest streaks
            - Show a yearly heatmap per habit
            - Send a daily email reminder for unfinished habits
API:        REST
            GET  /habits
            POST /habits
            POST /habits/{id}/checkins
            DELETE /habits/{id}/checkins/{date}
Storage:    PostgreSQL
Tech stack: Ruby, Ruby on Rails, Devise, Stimulus, Solid Queue
```

---

## Example 93

**Intent:**
we need system for employees request leave and manager approve it, our company use java spring boot

**Spec:**
```
Type:       Web application (HR workflow)
Auth:       Company LDAP login with employee, manager and HR roles
Data model: Employee(id, email, name, manager_id -> Employee, annual_allowance)
            LeaveType(id, name, paid)
            LeaveRequest(id, employee_id -> Employee, leave_type_id -> LeaveType, start_date, end_date, days, reason, status)
            PublicHoliday(id, date, name)
Features:   - Request leave for a date range and see remaining days
            - Skip weekends and public holidays when counting days
            - Let managers approve or reject requests from their team
            - Show a team calendar of who is away
            - Notify employees by email when a request is decided
API:        REST
            GET  /me/balance
            POST /leave-requests
            GET  /team/leave-requests?status=pending
            PATCH /leave-requests/{id}
            GET  /team/calendar?month={yyyy-mm}
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Spring Security LDAP, Spring Data JPA, Thymeleaf
```

---

## Example 94

**Intent:**
A review site for restaurants in my city like Yelp. People should be able to write reviews with photos, give ratings for food, service and price, and search restaurants by cuisine and neighbourhood. Restaurant owners should be able to claim their page and reply to reviews.

**Spec:**
```
Type:       Web application (reviews platform)
Auth:       Email + password or Google login; owner role after a verified claim
Data model: User(id, email, name, role)
            Restaurant(id, name, cuisine, neighbourhood, address, lat, lng, owner_id -> User)
            Review(id, restaurant_id -> Restaurant, user_id -> User, food, service, price, text, photos, created_at)
            OwnerReply(id, review_id -> Review, text, created_at)
            Claim(id, restaurant_id -> Restaurant, user_id -> User, proof_url, status)
Features:   - Search restaurants by cuisine, neighbourhood and rating
            - Write reviews with separate food, service and price ratings
            - Upload photos with a review
            - Claim a restaurant page with proof of ownership
            - Let owners reply publicly to reviews
            - Flag fake reviews for moderation
API:        REST
            GET  /restaurants?cuisine={c}&area={a}
            POST /restaurants/{id}/reviews
            POST /restaurants/{id}/claim
            POST /reviews/{id}/reply
            POST /reviews/{id}/flag
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Django REST Framework, Next.js frontend
```

---

## Example 95

**Intent:**
website for my band with our tour dates, music and a little merch store

**Spec:**
```
Type:       Web application (portfolio + store)
Auth:       Band admin login
Data model: Show(id, date, venue, city, ticket_url)
            Track(id, title, album, audio_url, spotify_url)
            MerchItem(id, name, price, sizes, stock, image_url)
            Order(id, email, items_json, total, shipping_address, status)
Features:   - Show upcoming tour dates with ticket links
            - Play tracks with an embedded player
            - Sell merch with size selection and card payment
            - Collect emails for the band's mailing list
            - Manage shows and merch stock in an admin page
API:        REST
            GET  /shows
            GET  /merch
            POST /orders
            POST /newsletter
Storage:    SQLite
Tech stack: Astro, Svelte components, Stripe Checkout, Mailchimp API
```

---

## Example 96

**Intent:**
landing page for my design agency in wordpress with a contact form that goes to our crm

**Spec:**
```
Type:       Web application (landing page)
Features:   - Show services, portfolio case studies and client logos
            - Collect leads with a contact form and spam protection
            - Send each lead to the CRM and to the team's email
            - Track form submissions as conversions in analytics
            - Load fast with caching and optimized images
Storage:    MySQL (WordPress database)
Tech stack: WordPress, PHP, Gravity Forms, HubSpot integration, reCAPTCHA
```

---

## Example 97

**Intent:**
Shopify-like platform where anyone can open their own online store on a subdomain. Each store has its own products, theme colors and orders, and the platform takes a small fee from every sale.

**Spec:**
```
Type:       Web application (multi-tenant SaaS e-commerce)
Auth:       Email + password login for merchants; separate customer accounts per store
Data model: Store(id, owner_id -> Merchant, subdomain, name, theme_json, stripe_account_id)
            Merchant(id, email, password_hash)
            Product(id, store_id -> Store, name, price, stock, images)
            Order(id, store_id -> Store, customer_email, total, platform_fee, status)
Features:   - Create a store with a unique subdomain
            - Resolve the tenant from the request's subdomain
            - Customize store colors, logo and homepage sections
            - Manage products and orders per store
            - Take card payments to the merchant's account minus a platform fee
            - Connect a custom domain with automatic HTTPS
API:        REST
            POST /stores
            GET  /api/storefront/products
            POST /api/storefront/checkout
            GET  /stores/{id}/orders
Storage:    PostgreSQL (tenant_id on every table), S3 (images)
Tech stack: TypeScript, Next.js (middleware for subdomains), Stripe Connect, Caddy (on-demand TLS)
```

---

## Example 98

**Intent:**
typeform style form builder in vue

**Spec:**
```
Type:       Web application (form builder)
Auth:       Email + password login for form creators
Data model: Form(id, owner_id -> User, title, theme, slug, published)
            Field(id, form_id -> Form, type, label, required, options, logic_json, position)
            Submission(id, form_id -> Form, answers_json, submitted_at)
            User(id, email, password_hash)
Features:   - Build forms with drag and drop fields
            - Show one question at a time with keyboard navigation
            - Skip questions with conditional logic
            - Send a webhook on every new submission
            - Show submissions in a table and export CSV
API:        REST
            POST /forms
            PUT  /forms/{id}
            GET  /f/{slug}
            POST /f/{slug}/submissions
            GET  /forms/{id}/submissions
Storage:    PostgreSQL
Tech stack: Vue.js, Pinia, vuedraggable, Node.js, Fastify
```

---

## Example 99

**Intent:**
Registration site for our kids summer sports camp. Parents register one or more children for weekly sessions, fill in medical info and pay online, and we need a sibling discount and a cap on places per week.

**Spec:**
```
Type:       Web application (registration and payments)
Auth:       Parent login with email + password; admin role for camp staff
Data model: Parent(id, email, password_hash, name, phone)
            Child(id, parent_id -> Parent, name, birth_date, allergies, medical_notes)
            Session(id, week_start, sport, capacity, price)
            Registration(id, child_id -> Child, session_id -> Session, status, paid_amount)
Features:   - Register several children for one or more weekly sessions
            - Collect medical and allergy information per child
            - Apply a sibling discount automatically at checkout
            - Close a session when it reaches capacity and offer a waitlist
            - Pay online by card
            - Print attendance lists with allergy notes for coaches
API:        REST
            GET  /sessions
            POST /children
            POST /registrations
            POST /checkout
            GET  /admin/sessions/{id}/roster
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe, WeasyPrint (PDF rosters)
```

---

## Example 100

**Intent:**
website where peoples can rent their private parking place when they not use it

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Email + password login; any user can be host or driver
Data model: User(id, email, password_hash, phone)
            Spot(id, host_id -> User, address, lat, lng, type, price_per_hour, instructions)
            Availability(id, spot_id -> Spot, weekday, start_time, end_time)
            Reservation(id, spot_id -> Spot, driver_id -> User, starts_at, ends_at, total, status)
Features:   - List a parking spot with address, price and weekly availability
            - Search free spots near a destination on a map
            - Reserve a spot for a time window and pay by card
            - Pay out hosts after each reservation
            - Rate hosts and drivers after a reservation
API:        REST
            GET  /spots?lat={lat}&lng={lng}&from={t}&to={t}
            POST /spots
            POST /spots/{id}/reservations
            POST /reservations/{id}/rating
Storage:    PostgreSQL with PostGIS
Tech stack: TypeScript, Express, React, Mapbox, Stripe Connect
```

---

## Example 101

**Intent:**
camera gear rental shop websit, customers rent lenses and cameras for a few days

**Spec:**
```
Type:       Web application (rental booking)
Auth:       Customer login with email + password and ID verification
Data model: Product(id, name, category, daily_rate, deposit, photos)
            Unit(id, product_id -> Product, serial_number, condition)
            Rental(id, unit_id -> Unit, customer_id -> Customer, start_date, end_date, total, status)
            Customer(id, email, password_hash, name, id_verified)
Features:   - Show availability calendar per product
            - Reserve gear for a date range with a deposit
            - Assign a free physical unit to each rental
            - Track pickup and return with condition notes
            - Charge late fees for returns after the end date
API:        REST
            GET  /products/{id}/availability
            POST /rentals
            PATCH /rentals/{id}/return
Storage:    PostgreSQL
Tech stack: Ruby, Ruby on Rails, Stripe, Hotwire
```

---

## Example 102

**Intent:**
discord like chat site for our gaming community written in go with websockets

**Spec:**
```
Type:       Web application (real-time chat)
Auth:       Email + password login with JWT
Data model: User(id, username, email, password_hash, avatar_url)
            Server(id, name, owner_id -> User)
            Channel(id, server_id -> Server, name, type)
            Membership(server_id -> Server, user_id -> User, role)
            Message(id, channel_id -> Channel, author_id -> User, content, created_at, edited_at)
Features:   - Create servers with text channels
            - Send and receive messages in real time
            - Show who is online in each server
            - Edit and delete own messages
            - Let moderators kick and ban members
            - Load older messages when scrolling up
API:        REST + WebSocket
            POST /servers
            GET  /channels/{id}/messages?before={id}
            POST /servers/{id}/invites
            WS   /gateway
Storage:    PostgreSQL, Redis (presence and pub/sub)
Tech stack: Go, gorilla/websocket, React, TypeScript
```

---

## Example 103

**Intent:**
I want a browser-based code editor where two people can pair program on the same file, with live cursors and a shared terminal output. Use Monaco editor and Liveblocks for the sync.

**Spec:**
```
Type:       Web application (real-time collaborative)
Auth:       GitHub OAuth login
Data model: User(id, github_id, username, avatar_url)
            Room(id, owner_id -> User, name, language, created_at)
            FileSnapshot(id, room_id -> Room, path, content, saved_at)
Features:   - Edit code together with live cursors and selections
            - Sync edits through Liveblocks storage
            - Run code in a sandbox and show output to both users
            - Invite a partner with a room link
            - Save file snapshots to restore later
API:        REST
            POST /rooms
            GET  /rooms/{id}
            POST /rooms/{id}/run
            POST /api/liveblocks-auth
Storage:    PostgreSQL (rooms and snapshots), Liveblocks (live state)
Tech stack: TypeScript, Next.js, Monaco Editor, Liveblocks, Judge0 API
```

---

## Example 104

**Intent:**
our NGO want a donation page, donor can give one time or monthly and get the tax receipt automatic

**Spec:**
```
Type:       Web application (donations)
Auth:       Admin login for NGO staff; donors give without an account
Data model: Donor(id, email, name, address, tax_id)
            Donation(id, donor_id -> Donor, amount, currency, recurring, stripe_payment_id, donated_at)
            Receipt(id, donation_id -> Donation, number, pdf_url, sent_at)
            Campaign(id, name, goal_amount)
Features:   - Donate once or monthly by card
            - Generate a numbered PDF tax receipt for every donation
            - Email the receipt to the donor automatically
            - Show progress toward a campaign goal
            - Send donors a yearly summary receipt
API:        REST
            POST /donations
            POST /webhooks/stripe
            GET  /campaigns/{id}
            GET  /admin/donations?year={yyyy}
Storage:    PostgreSQL, S3 (receipts)
Tech stack: Python, FastAPI, Stripe, WeasyPrint
```

---

## Example 105

**Intent:**
languge exchange site to find someone who speaks spanish and wants to learn english etc

**Spec:**
```
Type:       Web application (matching platform)
Auth:       Email + password or Google login
Data model: User(id, email, name, native_languages, learning_languages, level, timezone, bio)
            Conversation(id, user_a_id -> User, user_b_id -> User)
            Message(id, conversation_id -> Conversation, sender_id -> User, text, sent_at)
Features:   - Set the languages you speak and want to learn
            - Find partners whose native and learning languages match yours
            - Filter partners by timezone and level
            - Chat with partners in the site
            - Block and report users
API:        REST + WebSocket
            GET  /partners?learn={lang}
            PUT  /me/profile
            GET  /conversations
            WS   /chat
Storage:    PostgreSQL
Tech stack: TypeScript, Express, Socket.IO, React
```

---

## Example 106

**Intent:**
movie theater seat booking with express and mongodb

**Spec:**
```
Type:       Web application (booking system)
Auth:       Customer login with email + password; staff role for managing showtimes
Data model: Movie(_id, title, runtime_min, rating, poster_url)
            Screen(_id, name, seat_map)
            Showtime(_id, movie_id -> Movie, screen_id -> Screen, starts_at, price)
            Booking(_id, showtime_id -> Showtime, user_id -> User, seats, total, status)
            User(_id, email, password_hash, role)
Features:   - Show movies and showtimes for each day
            - Pick seats on an interactive seat map
            - Hold chosen seats for 10 minutes during checkout
            - Pay by card and email a ticket with a QR code
            - Let staff add movies and showtimes
API:        REST
            GET  /showtimes?date={date}
            GET  /showtimes/{id}/seats
            POST /showtimes/{id}/holds
            POST /bookings
Storage:    MongoDB
Tech stack: Node.js, Express, MongoDB, Mongoose, React, Stripe
```

---

## Example 107

**Intent:**
escape room booking

**Spec:**
```
Type:       Web application (booking system)
Auth:       Staff login with email + password; customers book as guests
Data model: Room(id, name, difficulty, min_players, max_players, duration_min, price_per_player)
            Slot(id, room_id -> Room, starts_at, is_booked)
            Booking(id, slot_id -> Slot, customer_name, email, players, total, status)
Features:   - Show rooms with difficulty and player limits
            - Book an open time slot for a group
            - Calculate the price from the number of players
            - Pay online or reserve with a deposit
            - Show the day's bookings to game masters
API:        REST
            GET  /rooms/{id}/slots?date={date}
            POST /bookings
            GET  /staff/bookings?date={date}
Storage:    PostgreSQL
Tech stack: Python, Flask, Stripe, Bootstrap
```

---

## Example 108

**Intent:**
a saas using nuxt where people make a personal resume website by filling a form and get their own url

**Spec:**
```
Type:       Web application (SaaS site builder)
Auth:       Email + password or LinkedIn login
Data model: User(id, email, name, username, plan)
            Resume(id, user_id -> User, headline, summary, theme, published)
            Experience(id, resume_id -> Resume, company, role, start_date, end_date, description)
            Project(id, resume_id -> Resume, title, url, description)
Features:   - Fill in experience, education and projects in a form
            - Pick a theme and preview the site live
            - Publish the resume at username.domain.com
            - Download the resume as PDF
            - Unlock custom domains on the paid plan
API:        REST
            GET  /me/resume
            PUT  /me/resume
            POST /me/resume/publish
            GET  /r/{username}
Storage:    PostgreSQL
Tech stack: Nuxt, Vue.js, Prisma, Stripe, Playwright (PDF)
```

---

## Example 109

**Intent:**
homeowners association portal with fastapi where residents vote on proposals and see announcements

**Spec:**
```
Type:       Web application (community portal)
Auth:       Resident login with email + password, one verified account per household
Data model: Household(id, address, unit_number)
            Resident(id, household_id -> Household, email, password_hash, is_board_member)
            Proposal(id, title, description, opens_at, closes_at, status)
            Vote(id, proposal_id -> Proposal, household_id -> Household, choice)
            Announcement(id, author_id -> Resident, title, body, posted_at)
Features:   - Post announcements as a board member
            - Open proposals for voting with a deadline
            - Allow one vote per household per proposal
            - Show results once voting closes
            - Share documents like meeting minutes and budgets
API:        REST
            GET  /announcements
            GET  /proposals
            POST /proposals/{id}/votes
            GET  /proposals/{id}/results
Storage:    PostgreSQL
Tech stack: Python, FastAPI, SQLAlchemy, React
```

---

## Example 110

**Intent:**
I want an android app in kotlin that tracks my runs with GPS and shows my pace and distance

**Spec:**
```
Type:       Mobile application (Android)
Data model: Run(id, started_at, ended_at, distance_m, duration_s, avg_pace_s_per_km)
            RoutePoint(id, run_id -> Run, lat, lng, altitude, recorded_at)
Features:   - Record the route with GPS in a foreground service while running
            - Show live distance, duration and current pace on screen
            - Announce each completed kilometre with voice feedback
            - Draw the finished route on a map
            - List past runs with weekly and monthly distance totals
Storage:    Local Room database (SQLite)
Tech stack: Kotlin, Jetpack Compose, Fused Location Provider, Room, Google Maps SDK
```

---

## Example 111

**Intent:**
budget app with envelopes

**Spec:**
```
Type:       Mobile application
Data model: Envelope(id, name, monthly_budget, balance, color)
            Transaction(id, envelope_id -> Envelope, amount, note, date)
Features:   - Create envelopes with a monthly budget amount
            - Add expenses and income to an envelope
            - Move money between envelopes
            - Show remaining balance per envelope with a progress bar
            - Reset or roll over balances at the start of each month
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, fl_chart
```

---

## Example 112

**Intent:**
hey, could you help me build a habit tracker in Flutter where I tick off habits every day and see my streaks?

**Spec:**
```
Type:       Mobile application
Data model: Habit(id, name, icon, frequency, reminder_time, created_at)
            CheckIn(id, habit_id -> Habit, date)
Features:   - Create habits with a daily or weekly frequency
            - Tick off a habit for today with one tap
            - Calculate current and longest streak per habit
            - Show a calendar heatmap of completed days
            - Send a local notification at each habit's reminder time
Storage:    Local on-device database (Hive)
Tech stack: Flutter, Hive, flutter_local_notifications
```

---

## Example 113

**Intent:**
Our hiking club organises trips every weekend and we need a mobile app with group chats per trip, a list of who is coming, and photos everyone can share after the hike. Members should only see trips they joined.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password login, invite code to join the club
Data model: Member(id, name, email, avatar_url)
            Trip(id, title, date, meeting_point, difficulty, organizer_id -> Member)
            Attendance(id, trip_id -> Trip, member_id -> Member, status)
            Message(id, trip_id -> Trip, member_id -> Member, text, sent_at)
            Photo(id, trip_id -> Trip, member_id -> Member, url, uploaded_at)
Features:   - Create trips and let members RSVP as going, maybe or not going
            - Open a group chat for each trip visible only to its attendees
            - Upload and browse shared photos per trip
            - Send push notifications for new messages and trip changes
            - Show upcoming and past trips for the logged-in member
API:        REST + WebSocket
            POST /auth/login
            GET  /trips
            POST /trips
            POST /trips/{id}/attendance
            GET  /trips/{id}/photos
            POST /trips/{id}/photos
            WS   /trips/{id}/chat
Storage:    PostgreSQL, S3 (photos)
Tech stack: React Native, Node.js, Express, Socket.IO, Firebase Cloud Messaging
```

---

## Example 114

**Intent:**
dating app but only for people who have dogs lol

**Spec:**
```
Type:       Mobile application with backend
Auth:       Phone number login with SMS verification code
Data model: User(id, name, birthdate, bio, location, photos)
            Dog(id, user_id -> User, name, breed, size, photo_url)
            Swipe(id, from_user_id -> User, to_user_id -> User, liked, created_at)
            Match(id, user_a_id -> User, user_b_id -> User, created_at)
            Message(id, match_id -> Match, sender_id -> User, text, sent_at)
Features:   - Create a profile with owner and dog photos
            - Swipe through nearby profiles filtered by distance and dog size
            - Create a match when two users like each other
            - Chat with matches in real time
            - Suggest dog parks halfway between two matches
            - Report and block users
API:        REST + WebSocket
            POST /auth/verify
            GET  /profiles/nearby
            POST /swipes
            GET  /matches
            WS   /matches/{id}/chat
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Flutter, Node.js, NestJS, Socket.IO
```

---

## Example 115

**Intent:**
i wnat a trip planner app that works offline when im abroad with no data

**Spec:**
```
Type:       Mobile application (offline-first)
Data model: Trip(id, name, start_date, end_date, destination)
            Day(id, trip_id -> Trip, date)
            Activity(id, day_id -> Day, title, time, address, lat, lng, notes)
            Booking(id, trip_id -> Trip, kind, confirmation_code, file_path)
Features:   - Create trips with a day-by-day itinerary
            - Add activities with time, address and notes
            - Save booking confirmations and tickets as PDFs or images
            - Download offline map tiles for the destination
            - Show today's plan on the home screen
Storage:    Local SQLite database, on-device file storage (tickets, map tiles)
Tech stack: Flutter, drift, flutter_map with offline tile caching
```

---

## Example 116

**Intent:**
I'd like a flashcard app for learning Spanish words that shows me the hard ones more often.

**Spec:**
```
Type:       Mobile application
Data model: Deck(id, name, language)
            Card(id, deck_id -> Deck, front, back, audio_path)
            Review(id, card_id -> Card, rating, ease_factor, interval_days, due_at)
Features:   - Create decks and cards with a word and its translation
            - Schedule reviews with the SM-2 spaced repetition algorithm
            - Rate each answer as again, hard, good or easy
            - Play text-to-speech pronunciation for each card
            - Show daily due count and review statistics
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, expo-speech
```

---

## Example 117

**Intent:**
meditation timer with bells

**Spec:**
```
Type:       Mobile application
Data model: Session(id, duration_min, started_at, completed)
            Preset(id, name, duration_min, interval_bell_min, ambient_sound)
Features:   - Start a timed meditation with a start and end bell
            - Ring interval bells at a chosen interval
            - Play optional ambient sounds such as rain or forest
            - Keep the timer running with the screen locked
            - Show total minutes meditated and the current daily streak
Storage:    Local on-device storage (SwiftData)
Tech stack: Swift, SwiftUI, AVFoundation, SwiftData
```

---

## Example 118

**Intent:**
I run a small pizza place and I want my own delivery app so customers order directly from me instead of paying the big apps commission

**Spec:**
```
Type:       Mobile application with backend
Auth:       Customer login with email or phone, staff login for the shop
Data model: Customer(id, name, phone, email)
            Address(id, customer_id -> Customer, line, lat, lng)
            MenuItem(id, name, description, price, category, available)
            Order(id, customer_id -> Customer, address_id -> Address, status, total, created_at)
            OrderItem(id, order_id -> Order, menu_item_id -> MenuItem, quantity, options)
Features:   - Browse the menu with sizes and extra toppings
            - Place an order for delivery or pickup and pay by card
            - Track order status from accepted to out for delivery
            - Let staff accept orders and update status from a tablet
            - Send push notifications when the order status changes
API:        REST
            GET  /menu
            POST /orders
            GET  /orders/{id}
            PATCH /orders/{id}/status
            POST /payments/intent
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI, Stripe, Firebase Cloud Messaging
```

---

## Example 119

**Intent:**
A carpool app for students of our university, drivers post rides to the campus and others can book a seat and share the petrol cost.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Sign up with a university email address, verified by email link
Data model: User(id, name, email, phone, rating)
            Ride(id, driver_id -> User, origin, destination, departs_at, seats, price_per_seat)
            Booking(id, ride_id -> Ride, passenger_id -> User, status)
            Review(id, booking_id -> Booking, author_id -> User, stars, comment)
Features:   - Post a ride with route, departure time and free seats
            - Search rides by origin, destination and date
            - Book a seat and get driver approval
            - Split the petrol cost per seat automatically
            - Rate drivers and passengers after the ride
API:        REST
            POST /auth/signup
            GET  /rides?from={place}&to={place}&date={date}
            POST /rides
            POST /rides/{id}/bookings
            PATCH /bookings/{id}
            POST /bookings/{id}/review
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express, Google Maps Places API
```

---

## Example 120

**Intent:**
camera app that makes photos look like old film

**Spec:**
```
Type:       Mobile application
Features:   - Show a live camera preview with the selected film filter applied
            - Apply film looks with grain, color grading and light leaks
            - Add an optional date stamp in the corner
            - Save photos to the system photo library
            - Apply filters to existing photos from the gallery
Storage:    Device photo library
Tech stack: Swift, SwiftUI, AVFoundation, Core Image (custom CIFilter kernels)
```

---

## Example 121

**Intent:**
a unit converter for my phone, no ads, no internet needed

**Spec:**
```
Type:       Mobile application (offline)
Data model: Favorite(id, category, from_unit, to_unit)
Features:   - Convert length, weight, volume, temperature, speed and area
            - Update the result instantly while typing
            - Swap the from and to units with one tap
            - Save favourite conversions for quick access
            - Copy the result to the clipboard
Storage:    Local key-value storage (DataStore)
Tech stack: Kotlin, Jetpack Compose, DataStore
```

---

## Example 122

**Intent:**
Please make app for finding garage sales near to me on the map, people can post their sale with the date and photos.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password or Google sign-in
Data model: User(id, name, email)
            Sale(id, user_id -> User, title, description, address, lat, lng, starts_at, ends_at)
            SalePhoto(id, sale_id -> Sale, url)
            SavedSale(id, user_id -> User, sale_id -> Sale)
Features:   - Show upcoming garage sales as pins on a map around the user
            - Post a sale with address, date, time and photos
            - Filter sales by date and distance
            - Save sales and get a reminder on the morning of the sale
            - Open directions to a sale in the maps app
API:        REST
            GET  /sales?lat={lat}&lng={lng}&radius_km={r}
            POST /sales
            POST /sales/{id}/photos
            POST /sales/{id}/save
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Flutter, google_maps_flutter, Python, Django REST Framework
```

---

## Example 123

**Intent:**
I have a cheap fitness band that tracks sleep but its app is terrible, can I make my own companion app that reads the data over bluetooth and shows nicer sleep charts?

**Spec:**
```
Type:       Mobile application (wearable companion)
Data model: Device(id, name, mac_address, last_synced_at)
            SleepSession(id, device_id -> Device, start_at, end_at, score)
            SleepStage(id, session_id -> SleepSession, stage, start_at, end_at)
Features:   - Pair with the band over Bluetooth Low Energy
            - Sync sleep records from the band's GATT characteristics
            - Show a nightly hypnogram of light, deep and REM sleep
            - Show weekly averages for duration, bedtime and wake time
            - Export sleep data as a CSV file
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, flutter_blue_plus, sqflite, fl_chart
```

---

## Example 124

**Intent:**
parental control app to limit how long my kid can use the phone each day

**Spec:**
```
Type:       Mobile application with backend (parent and child apps)
Auth:       Parent account with email + password, child device linked by pairing code
Data model: Parent(id, email, password_hash)
            ChildDevice(id, parent_id -> Parent, name, platform, paired_at)
            Limit(id, device_id -> ChildDevice, app_package, daily_minutes, bedtime_start, bedtime_end)
            UsageReport(id, device_id -> ChildDevice, app_package, minutes, date)
Features:   - Set a daily screen time limit per app or for the whole device
            - Lock the device during bedtime hours
            - Report daily app usage from the child device to the parent
            - Let the child request extra time and the parent approve it
            - Notify the parent when a limit is reached
API:        REST
            POST /auth/login
            POST /devices/pair
            GET  /devices/{id}/usage?date={date}
            PUT  /devices/{id}/limits
            POST /devices/{id}/time-requests
Storage:    PostgreSQL
Tech stack: Kotlin (Android UsageStatsManager, Device Policy), Node.js, Express, Firebase Cloud Messaging
```

---

## Example 125

**Intent:**
lost and found pets for our neighbourhood

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password login
Data model: User(id, name, email, phone)
            PetReport(id, user_id -> User, kind, species, description, photo_url, lat, lng, reported_at, resolved)
            Sighting(id, report_id -> PetReport, user_id -> User, lat, lng, note, seen_at)
Features:   - Post a lost or found pet with photo and last known location
            - Show active reports on a map and in a list
            - Add sightings to a lost pet report
            - Notify users within 2 km when a new pet is reported lost
            - Mark a report as resolved when the pet is home
API:        REST
            GET  /reports?lat={lat}&lng={lng}
            POST /reports
            POST /reports/{id}/sightings
            PATCH /reports/{id}
Storage:    Supabase Postgres with PostGIS, Supabase Storage (photos)
Tech stack: React Native, Supabase
```

---

## Example 126

**Intent:**
private period tracker app that dont upload my data anywhere

**Spec:**
```
Type:       Mobile application (offline)
Auth:       Optional PIN or biometric lock on app open
Data model: Cycle(id, start_date, end_date)
            DayLog(id, date, flow, symptoms, mood, notes)
Features:   - Log period start and end days
            - Log daily symptoms, flow and mood
            - Predict the next period and fertile window from past cycles
            - Show cycle length history on a chart
            - Export and import an encrypted backup file
Storage:    Local encrypted database (SQLCipher)
Tech stack: Flutter, sqflite_sqlcipher, local_auth
```

---

## Example 127

**Intent:**
something to split bills with my flatmates so we know who owes who

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password or Google sign-in
Data model: User(id, name, email)
            Group(id, name, currency)
            GroupMember(id, group_id -> Group, user_id -> User)
            Expense(id, group_id -> Group, paid_by -> User, amount, description, date)
            ExpenseShare(id, expense_id -> Expense, user_id -> User, amount)
            Settlement(id, group_id -> Group, from_user -> User, to_user -> User, amount, date)
Features:   - Add an expense and split it equally, by percentage or by exact amounts
            - Show each member's balance in the group
            - Simplify debts to the fewest possible payments
            - Record a settlement when someone pays back
            - Send a reminder to members who owe money
API:        REST
            GET  /groups
            POST /groups/{id}/expenses
            GET  /groups/{id}/balances
            POST /groups/{id}/settlements
Storage:    PostgreSQL
Tech stack: React Native, TypeScript, Node.js, NestJS
```

---

## Example 128

**Intent:**
My mum is 78 and forgets her pills. I want an app with big buttons that reminds her to take each medicine, and if she doesn't confirm within 30 minutes it should send me a message so I can call her.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Caregiver account with email login, senior device linked by code
Data model: Caregiver(id, name, email, phone)
            Patient(id, caregiver_id -> Caregiver, name)
            Medication(id, patient_id -> Patient, name, dose, photo_url)
            Schedule(id, medication_id -> Medication, time_of_day, days_of_week)
            DoseLog(id, schedule_id -> Schedule, due_at, taken_at, status)
Features:   - Show a large-button reminder screen with the pill photo at each dose time
            - Confirm a dose as taken with one tap
            - Alert the caregiver by push and SMS if a dose is not confirmed in 30 minutes
            - Let the caregiver edit medicines and schedules remotely
            - Show the caregiver a weekly adherence report
API:        REST
            POST /auth/login
            GET  /patients/{id}/schedule
            PUT  /patients/{id}/medications
            POST /doses/{id}/taken
            GET  /patients/{id}/adherence?week={date}
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI, Celery (missed-dose checks), Twilio SMS, Firebase Cloud Messaging
```

---

## Example 129

**Intent:**
gym log app for sets reps and weight

**Spec:**
```
Type:       Mobile application
Data model: Exercise(id, name, muscle_group, equipment)
            Workout(id, date, notes)
            WorkoutSet(id, workout_id -> Workout, exercise_id -> Exercise, reps, weight_kg, rpe)
Features:   - Start a workout and log sets with reps and weight
            - Show the previous session's numbers for each exercise
            - Run a rest timer between sets
            - Track personal records and estimated one-rep max
            - Chart strength progress per exercise over time
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, Victory Native
```

---

## Example 130

**Intent:**
calorie counter where i can just scan the barcode on food packets

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password login
Data model: User(id, email, daily_calorie_goal)
            Food(id, barcode, name, kcal_per_100g, protein_g, carbs_g, fat_g)
            FoodEntry(id, user_id -> User, food_id -> Food, grams, meal, eaten_at)
Features:   - Scan a product barcode with the camera to look up nutrition data
            - Search foods by name when there is no barcode
            - Log foods to breakfast, lunch, dinner or snacks with a portion size
            - Show calories and macros eaten today against the goal
            - Add a custom food when a product is not found
API:        REST
            GET  /foods/barcode/{code}
            GET  /foods?search={text}
            POST /entries
            GET  /entries?date={date}
Storage:    PostgreSQL
Tech stack: Kotlin, Jetpack Compose, ML Kit Barcode Scanning, Ktor server, Open Food Facts API
```

---

## Example 131

**Intent:**
track all my subscriptions like netflix spotify etc and remind me before they renew

**Spec:**
```
Type:       Mobile application
Data model: Subscription(id, name, price, currency, billing_cycle, next_renewal, category, icon)
Features:   - Add subscriptions with price, billing cycle and next renewal date
            - Notify a set number of days before each renewal
            - Show total monthly and yearly spending
            - Group spending by category in a pie chart
            - Mark a subscription as cancelled and keep it in history
Storage:    Local on-device storage (SwiftData)
Tech stack: Swift, SwiftUI, SwiftData, UserNotifications, Swift Charts
```

---

## Example 132

**Intent:**
I always kill my houseplants. Can you make me an app that reminds me when to water each one?

**Spec:**
```
Type:       Mobile application
Data model: Plant(id, name, species, photo_path, location, water_every_days, last_watered_at)
            CareLog(id, plant_id -> Plant, action, done_at)
Features:   - Add plants with a photo and a watering interval
            - Show which plants need water today
            - Mark a plant as watered and schedule the next reminder
            - Log fertilizing and repotting in each plant's history
            - Send a daily notification listing plants that are due
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, flutter_local_notifications, image_picker
```

---

## Example 133

**Intent:**
walkie talkie app, hold button and talk to friends

**Spec:**
```
Type:       Mobile application with backend
Auth:       Phone number login with SMS code
Data model: User(id, name, phone)
            Channel(id, name, owner_id -> User)
            ChannelMember(id, channel_id -> Channel, user_id -> User)
            VoiceClip(id, channel_id -> Channel, sender_id -> User, audio_url, duration_ms, sent_at)
Features:   - Hold a button to record and release to send a voice message
            - Play incoming voice messages automatically when the app is open
            - Create channels and invite friends from contacts
            - Show who is currently online in a channel
            - Keep the last 24 hours of voice messages for replay
API:        REST + WebSocket
            POST /auth/verify
            GET  /channels
            POST /channels
            POST /channels/{id}/clips
            WS   /channels/{id}/live
Storage:    PostgreSQL, S3 (audio clips)
Tech stack: React Native, Node.js, Socket.IO, Opus audio encoding
```

---

## Example 134

**Intent:**
Im learning german and want to find native speakers who learn english so we can practise by chatting, like a tandem partner app

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password or Apple / Google sign-in
Data model: User(id, name, native_language, learning_language, level, country, bio)
            PartnerRequest(id, from_user -> User, to_user -> User, status)
            Conversation(id, user_a -> User, user_b -> User)
            Message(id, conversation_id -> Conversation, sender_id -> User, text, correction_of_id -> Message, sent_at)
Features:   - Match users whose native language is the other's learning language
            - Send and accept partner requests
            - Chat in real time with text and voice messages
            - Correct a partner's message inline and show the correction
            - Translate a message with one tap
Storage:    Cloud Firestore (real-time listeners for chat), Firebase Storage (voice messages)
Tech stack: Flutter, Firebase Auth, Cloud Firestore, Cloud Functions, Google Cloud Translation API
```

---

## Example 135

**Intent:**
our street has like 40 houses and everyone owns a drill they use once a year, would be cool to have an app where neighbours lend tools to each other

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password login, address verified by a neighbour invite
Data model: User(id, name, email, street_id -> Street, house_number)
            Street(id, name, invite_code)
            Tool(id, owner_id -> User, name, category, photo_url, available)
            Loan(id, tool_id -> Tool, borrower_id -> User, requested_at, due_back, returned_at, status)
Features:   - List tools you are willing to lend with a photo
            - Browse and search tools owned by people on your street
            - Request to borrow a tool for chosen dates
            - Let the owner accept or decline a request
            - Remind the borrower when a tool is due back
API:        REST
            GET  /tools?search={text}
            POST /tools
            POST /tools/{id}/loans
            PATCH /loans/{id}
Storage:    Supabase Postgres, Supabase Storage (photos)
Tech stack: Flutter, Supabase
```

---

## Example 136

**Intent:**
yoga app with poses and timer

**Spec:**
```
Type:       Mobile application
Data model: Pose(id, name, sanskrit_name, image_path, instructions, difficulty)
            Flow(id, name, level)
            FlowStep(id, flow_id -> Flow, pose_id -> Pose, position, hold_seconds)
Features:   - Browse a library of poses with images and instructions
            - Build custom flows by ordering poses and setting hold times
            - Play a flow with a timer and voice cue for the next pose
            - Offer ready-made beginner, intermediate and advanced flows
            - Track practice days and total minutes
Storage:    Local on-device database (SQLite), bundled pose images
Tech stack: React Native, expo-sqlite, expo-speech
```

---

## Example 137

**Intent:**
crypto portfoilo tracker that shows how much my coins are worth rn and my profit

**Spec:**
```
Type:       Mobile application
Data model: Holding(id, coin_id, symbol, quantity)
            Trade(id, coin_id, side, quantity, price, fee, traded_at)
            PriceCache(coin_id, price_usd, change_24h, fetched_at)
Features:   - Add buy and sell trades for each coin
            - Fetch current prices every minute while the app is open
            - Show total portfolio value and 24h change
            - Calculate profit and loss per coin using average cost
            - Set price alerts for a coin
API:        REST (external)
            GET  https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd
Storage:    Local on-device database (Room)
Tech stack: Kotlin, Jetpack Compose, Retrofit, Room, CoinGecko API
```

---

## Example 138

**Intent:**
I'm trying to quit smoking, can you make an app that shows how many days I've been smoke free and how much money I've saved?

**Spec:**
```
Type:       Mobile application
Data model: QuitPlan(quit_date, cigarettes_per_day, price_per_pack, cigarettes_per_pack)
            Craving(id, intensity, trigger, resisted, logged_at)
            Milestone(id, title, days_required, unlocked_at)
Features:   - Show time smoke-free, cigarettes avoided and money saved
            - Log cravings with intensity and trigger
            - Unlock health milestones such as 24 hours or 1 month
            - Offer a 2-minute distraction exercise during a craving
            - Show progress in a home screen widget
Storage:    Local on-device storage (SwiftData)
Tech stack: Swift, SwiftUI, SwiftData, WidgetKit
```

---

## Example 139

**Intent:**
My family is spread over three countries and we use WhatsApp, but my father does not trust big companies with our messages. I want a simple private messenger only for our family, with end-to-end encryption, group chat, and photo sharing. It should be easy enough for my grandmother.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Invite-only sign-up by link from an existing family member, device keys generated on install
Data model: Member(id, display_name, identity_public_key, avatar_url)
            Device(id, member_id -> Member, prekey_bundle, push_token)
            Chat(id, name, is_group)
            ChatMember(id, chat_id -> Chat, member_id -> Member)
            EncryptedMessage(id, chat_id -> Chat, sender_device_id -> Device, ciphertext, sent_at)
Features:   - Encrypt every message end-to-end with the Signal protocol
            - Chat one-to-one and in a family group
            - Send encrypted photos and voice notes
            - Show large text and simple buttons in an easy mode
            - Invite a new family member with a one-time link
API:        REST + WebSocket
            POST /invites
            POST /members
            GET  /devices/{member_id}/prekeys
            POST /messages
            WS   /messages/stream
Storage:    PostgreSQL (ciphertext only), S3 (encrypted attachments)
Tech stack: Flutter, libsignal, Go, WebSocket, Firebase Cloud Messaging
```

---

## Example 140

**Intent:**
I am 58 and divorced, the dating apps are all for young people. Can you make a dating app for persons over 50 that is simple and more serious?

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password login, photo selfie verification
Data model: User(id, name, birthdate, gender, seeking, city, bio, verified)
            Photo(id, user_id -> User, url, position)
            Interest(id, user_id -> User, tag)
            Like(id, from_user -> User, to_user -> User, note, created_at)
            Conversation(id, user_a -> User, user_b -> User)
            Message(id, conversation_id -> Conversation, sender_id -> User, text, sent_at)
Features:   - Restrict sign-up to users aged 50 and over
            - Browse a few curated profiles per day instead of endless swiping
            - Send a like with a short personal note
            - Start a conversation when a like is returned
            - Show a verified badge after selfie verification
            - Use large fonts and simple navigation throughout
API:        REST + WebSocket
            GET  /profiles/daily
            POST /likes
            GET  /conversations
            WS   /conversations/{id}
            POST /verification/selfie
Storage:    PostgreSQL, S3 (photos)
Tech stack: React Native, Python, Django, Django Channels, AWS Rekognition (face comparison)
```

---

## Example 141

**Intent:**
backpacking through south east asia next year, an app to find other travellers going to the same place at the same time would be sick

**Spec:**
```
Type:       Mobile application with backend
Auth:       Google or Apple sign-in
Data model: Traveler(id, name, age, country, bio, photo_url, travel_style)
            TripLeg(id, traveler_id -> Traveler, city, arrive_on, leave_on)
            Connection(id, from_id -> Traveler, to_id -> Traveler, status)
            Message(id, connection_id -> Connection, sender_id -> Traveler, text, sent_at)
Features:   - Add upcoming trip legs with city and dates
            - Find travellers whose legs overlap in place and time
            - Send a connection request with a short message
            - Chat with connected travellers
            - Hide your profile from specific users
Storage:    Cloud Firestore (real-time listeners for chat), Firebase Storage (photos)
Tech stack: Flutter, Firebase Auth, Cloud Firestore, Cloud Functions
```

---

## Example 142

**Intent:**
hey can I get a flutter app to teach my 4 year old daughter the english alphabet with sounds and little games?

**Spec:**
```
Type:       Mobile application (kids, offline)
Data model: Letter(char, word, image_path, sound_path)
            Progress(letter_char, stars, times_played)
Features:   - Show each letter with a picture and play its sound and example word
            - Play a tap-the-letter game where the child finds the spoken letter
            - Trace letters with a finger on screen
            - Award stars and stickers for completed letters
            - Lock settings behind a parental gate
Storage:    Local key-value storage (shared_preferences), bundled audio and images
Tech stack: Flutter, audioplayers, shared_preferences
```

---

## Example 143

**Intent:**
simple mood tracker app

**Spec:**
```
Type:       Mobile application
Data model: MoodEntry(id, mood_level, emotions, note, created_at)
            Activity(id, name, icon)
            EntryActivity(id, entry_id -> MoodEntry, activity_id -> Activity)
Features:   - Log mood on a 5-point scale with optional emotions and note
            - Tag what you were doing such as work, sport or friends
            - Show a monthly mood calendar
            - Show which activities link to better moods
            - Remind the user to log their mood each evening
Storage:    Local on-device database (Room)
Tech stack: Kotlin, Jetpack Compose, Room, Vico charts
```

---

## Example 144

**Intent:**
In my restaurant on weekend there is always queue outside. I want app where customer put his name in the waiting list and receive message when the table is ready, so they can walk around meanwhile.

**Spec:**
```
Type:       Mobile application with backend (staff app and customer web link)
Auth:       Staff login with PIN, customers join without an account
Data model: Restaurant(id, name, avg_turn_minutes)
            QueueEntry(id, restaurant_id -> Restaurant, name, phone, party_size, status, joined_at, notified_at)
Features:   - Let customers join the waitlist by scanning a QR code at the door
            - Show each customer their position and estimated wait time
            - Let staff mark a table as ready for the next suitable party
            - Send an SMS when the customer's table is ready
            - Remove entries that do not show up within 10 minutes
API:        REST + WebSocket
            POST /restaurants/{id}/queue
            GET  /queue/{entry_id}
            PATCH /queue/{entry_id}
            WS   /restaurants/{id}/queue/live
Storage:    PostgreSQL
Tech stack: React Native (staff tablet), Next.js (customer page), Node.js, Twilio SMS
```

---

## Example 145

**Intent:**
I want to build an app for booking small moving vans with a driver, like Uber but for moving furniture. The customer enters pickup and drop-off addresses, picks the van size and number of helpers, and sees a fixed price up front. Drivers get job offers on their own app and the customer can track the van on the day.

**Spec:**
```
Type:       Mobile application with backend (customer and driver apps)
Auth:       Phone number login with SMS code, drivers verified with licence upload
Data model: Customer(id, name, phone)
            Driver(id, name, phone, van_size, licence_url, approved, lat, lng)
            Job(id, customer_id -> Customer, driver_id -> Driver, pickup_address, dropoff_address, van_size, helpers, scheduled_at, price, status)
            JobOffer(id, job_id -> Job, driver_id -> Driver, status, sent_at)
Features:   - Calculate a fixed price from route distance, van size and helpers
            - Book a move for a date and pay up front
            - Offer jobs to approved drivers with the matching van size
            - Track the van live on the day of the move
            - Let the customer and driver message each other about the job
API:        REST + WebSocket
            POST /quotes
            POST /jobs
            GET  /drivers/me/offers
            POST /offers/{id}/accept
            WS   /jobs/{id}/tracking
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Python, FastAPI, Google Maps Routes API, Stripe
```

---

## Example 146

**Intent:**
I've started birdwatching and I'd love an app where I point my camera at a bird and it tells me what species it is, then saves it to my list

**Spec:**
```
Type:       Mobile application
Data model: Species(id, common_name, scientific_name, description)
            Sighting(id, species_id -> Species, photo_path, lat, lng, confidence, seen_at)
Features:   - Identify the bird species from a photo with an on-device image model
            - Show the top 3 guesses with confidence scores
            - Save sightings with photo, location and date to a life list
            - Show sightings as pins on a map
            - Work without internet in the field
Storage:    Local on-device database (SQLite), on-device photo files
Tech stack: Kotlin, Jetpack Compose, TensorFlow Lite (bird classifier), CameraX, Room
```

---

## Example 147

**Intent:**
inventry app for my small shop scan barcodes to count stock, internet in shop is very bad so needs offline

**Spec:**
```
Type:       Mobile application (offline-first)
Data model: Product(id, barcode, name, price, quantity, reorder_level)
            StockMovement(id, product_id -> Product, change, reason, created_at)
Features:   - Scan barcodes with the camera to find or add a product
            - Add or subtract stock with a reason such as sale or delivery
            - Show products below their reorder level
            - Export stock levels as a CSV file
            - Back up the database to Google Drive when online
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, mobile_scanner, drift, googleapis (Drive backup)
```

---

## Example 148

**Intent:**
I'm bored of running the same route, could an app generate a new loop route from my house for a distance I choose?

**Spec:**
```
Type:       Mobile application
Data model: SavedRoute(id, name, distance_m, polyline, created_at)
Features:   - Generate a loop route starting and ending at the current location
            - Let the user pick the target distance and preferred surface
            - Regenerate a different route with one tap
            - Show the route and elevation profile on a map
            - Save favourite routes and export them as GPX
API:        REST (external)
            GET  https://graphhopper.com/api/1/route?point={lat,lng}&algorithm=round_trip
Storage:    Local on-device storage (Core Data)
Tech stack: Swift, SwiftUI, MapKit, GraphHopper Routing API
```

---

## Example 149

**Intent:**
app for my bluetooth bathroom scale

**Spec:**
```
Type:       Mobile application (wearable companion)
Data model: User(id, name, height_cm, birthdate, sex)
            Measurement(id, user_id -> User, weight_kg, body_fat_percent, muscle_kg, measured_at)
Features:   - Read weight and body composition from the scale over BLE
            - Assign each measurement to the right family member by weight range
            - Show weight trends with a 7-day moving average
            - Set a goal weight and show progress
            - Sync measurements to Apple Health or Health Connect
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-ble-plx, react-native-health, react-native-health-connect
```

---

## Example 150

**Intent:**
Our school has 8 buses and parents keep calling the office asking where the bus is. I want an app for parents that shows the live bus location, sends a notification when the bus is 5 minutes from their stop, and lets the driver mark which kids got on and off.

**Spec:**
```
Type:       Mobile application with backend (parent and driver apps)
Auth:       Parent login with email + password, driver login with PIN, accounts created by school admin
Data model: Bus(id, number, driver_id -> Driver)
            Driver(id, name, phone)
            Stop(id, route_id -> Route, name, lat, lng, position)
            Route(id, bus_id -> Bus, name)
            Student(id, name, parent_id -> Parent, stop_id -> Stop)
            Parent(id, name, email)
            BoardingEvent(id, student_id -> Student, bus_id -> Bus, kind, recorded_at)
Features:   - Send the bus GPS position from the driver app every 10 seconds
            - Show the live bus location and ETA to each parent
            - Notify parents when the bus is 5 minutes from their stop
            - Let the driver mark students as boarded or dropped off
            - Notify parents when their child gets on or off the bus
API:        REST + WebSocket
            POST /buses/{id}/location
            WS   /buses/{id}/live
            POST /boarding-events
            GET  /students/{id}/today
Storage:    PostgreSQL, Redis (latest positions)
Tech stack: Flutter, Node.js, NestJS, Socket.IO, Firebase Cloud Messaging
```

---

## Example 151

**Intent:**
something where neighbours can warn each other about stuff like break-ins, suspicious cars or a broken street light

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password login, neighbourhood verified by postcode
Data model: User(id, name, email, neighbourhood_id -> Neighbourhood)
            Neighbourhood(id, name, boundary)
            Alert(id, author_id -> User, category, description, photo_url, lat, lng, created_at)
            Comment(id, alert_id -> Alert, author_id -> User, text, created_at)
Features:   - Post an alert with category, description, photo and location
            - Notify all users in the neighbourhood immediately for urgent categories
            - Show recent alerts on a map and in a timeline
            - Comment on alerts with updates
            - Report misleading posts to moderators
API:        REST
            GET  /alerts?neighbourhood={id}
            POST /alerts
            POST /alerts/{id}/comments
            POST /alerts/{id}/report
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Python, FastAPI, Firebase Cloud Messaging
```

---

## Example 152

**Intent:**
honestly I just want my apple watch to count my swimming laps and show my 100m splits, the built in one doesn't show what I want

**Spec:**
```
Type:       Smartwatch application (watchOS) with iPhone companion
Data model: SwimWorkout(id, pool_length_m, started_at, ended_at, total_laps, total_distance_m)
            Lap(id, workout_id -> SwimWorkout, number, duration_s, stroke_count, stroke_type)
Features:   - Start a pool swim workout with a chosen pool length
            - Count laps automatically using the watch's swim tracking
            - Show the last 100 m split on screen after each 100 m
            - Lock the screen against water with water lock
            - Show the full lap list and splits on the iPhone afterwards
Storage:    HealthKit, local SwiftData on iPhone
Tech stack: Swift, SwiftUI, watchOS HealthKit (HKWorkoutSession), WatchConnectivity
```

---

## Example 153

**Intent:**
im a freelancer and i lose all my receipts, app to take photo of receipt and it reads the amount and date automaticly

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password login
Data model: User(id, email, currency)
            Receipt(id, user_id -> User, image_url, merchant, total, tax, date, category, ocr_text)
Features:   - Photograph a receipt and crop it automatically
            - Extract merchant, date, total and tax with OCR
            - Let the user correct extracted fields and choose a category
            - Search receipts by merchant, date or amount
            - Export receipts for a quarter as a CSV and a ZIP of images
API:        REST
            POST /receipts
            GET  /receipts?from={date}&to={date}
            PUT  /receipts/{id}
            GET  /exports?quarter={q}
Storage:    PostgreSQL, S3 (receipt images)
Tech stack: React Native, Node.js, Express, Google Cloud Vision API
```

---

## Example 154

**Intent:**
track books I read and pages per day

**Spec:**
```
Type:       Mobile application
Data model: Book(id, title, author, isbn, total_pages, cover_url, status)
            ReadingSession(id, book_id -> Book, pages_read, minutes, date)
Features:   - Add books by scanning the ISBN barcode or searching by title
            - Log pages read each day for the current book
            - Show progress percentage and estimated finish date
            - Set a yearly book goal and show progress
            - Show a reading streak and pages-per-day chart
API:        REST (external)
            GET  https://openlibrary.org/isbn/{isbn}.json
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, mobile_scanner, sqflite, Open Library API
```

---

## Example 155

**Intent:**
I'm kinda sick of instagram, I'd like a small social app where me and my close friends just send each other short voice notes in a shared feed

**Spec:**
```
Type:       Mobile application with backend
Auth:       Phone number login with SMS code
Data model: User(id, name, phone, avatar_url)
            Circle(id, name, owner_id -> User)
            CircleMember(id, circle_id -> Circle, user_id -> User)
            VoicePost(id, circle_id -> Circle, author_id -> User, audio_url, duration_s, created_at)
            Reaction(id, post_id -> VoicePost, user_id -> User, emoji)
Features:   - Record and post voice notes up to 60 seconds to a circle
            - Show a feed of voice posts from your circles only
            - React to posts with emoji
            - Limit each circle to 20 members
            - Delete voice posts automatically after 7 days
API:        REST
            GET  /circles
            POST /circles/{id}/members
            GET  /circles/{id}/posts
            POST /circles/{id}/posts
            POST /posts/{id}/reactions
Storage:    Supabase Postgres, Supabase Storage (audio)
Tech stack: Swift, SwiftUI, AVFoundation, Supabase
```

---

## Example 156

**Intent:**
I move to new city for job and need room. Please app where people with free room and people searching room can find each other by budget and habits.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password or Google sign-in
Data model: User(id, name, age, occupation, smoker, pets, sleep_schedule, cleanliness)
            Listing(id, owner_id -> User, city, address, rent, available_from, description)
            ListingPhoto(id, listing_id -> Listing, url)
            SearchProfile(id, user_id -> User, city, max_budget, move_in_date)
            Message(id, listing_id -> Listing, sender_id -> User, receiver_id -> User, text, sent_at)
Features:   - Post a room with rent, photos and available date
            - Create a search profile with city, budget and move-in date
            - Rank rooms by compatibility of habits such as smoking, pets and sleep
            - Message the room owner from a listing
            - Save listings and get alerts for new matching rooms
API:        REST
            GET  /listings?city={c}&max_rent={n}
            POST /listings
            GET  /listings/{id}/compatibility
            POST /messages
Storage:    PostgreSQL, S3 (photos)
Tech stack: Flutter, Python, Django REST Framework
```

---

## Example 157

**Intent:**
I just got an electric car and want an app that plans a road trip with charging stops based on my battery range

**Spec:**
```
Type:       Mobile application
Data model: Vehicle(id, model, battery_kwh, consumption_kwh_per_100km, connector_type)
            Trip(id, origin, destination, start_charge_percent, created_at)
            ChargingStop(id, trip_id -> Trip, station_name, lat, lng, power_kw, arrive_percent, charge_minutes)
Features:   - Plan a route with charging stops so the battery never drops below 10%
            - Filter chargers by connector type and minimum power
            - Estimate charging time at each stop
            - Show total travel and charging time
            - Open the route in the phone's navigation app
API:        REST (external)
            GET  https://api.openchargemap.io/v3/poi?latitude={lat}&longitude={lng}
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-maps, Open Charge Map API, Google Directions API
```

---

## Example 158

**Intent:**
kanji writting practice app where i draw with finger and it checks the stroke order

**Spec:**
```
Type:       Mobile application
Data model: Kanji(id, character, meanings, readings, jlpt_level, stroke_data)
            PracticeResult(id, kanji_id -> Kanji, correct_strokes, mistakes, practiced_at)
Features:   - Show a kanji with meanings, readings and an animated stroke order
            - Let the user draw each stroke with a finger on a canvas
            - Check stroke direction and order against KanjiVG data
            - Highlight the correct stroke after a mistake
            - Organise practice by JLPT level and repeat missed kanji
Storage:    Local on-device database (SQLite), bundled KanjiVG data
Tech stack: Kotlin, Jetpack Compose (Canvas), Room, KanjiVG
```

---

## Example 159

**Intent:**
binaural beats app for focus and sleep

**Spec:**
```
Type:       Mobile application
Data model: Preset(id, name, base_hz, beat_hz, background_noise, duration_min)
Features:   - Generate binaural beats with a different tone in each ear
            - Offer presets for focus, relaxation and sleep
            - Mix in background noise such as brown noise or rain
            - Play in the background with a fade-out timer
            - Warn the user to use headphones
Storage:    Local on-device storage (SharedPreferences)
Tech stack: Kotlin, Jetpack Compose, Android AudioTrack, Media3 session
```

---

## Example 160

**Intent:**
I travel many countries and want app to note my spendings in local money and see the total in euro at end of the trip.

**Spec:**
```
Type:       Mobile application
Data model: Trip(id, name, home_currency, start_date, end_date)
            Expense(id, trip_id -> Trip, amount, currency, category, note, spent_at)
            ExchangeRate(base, quote, rate, fetched_at)
Features:   - Add an expense in any local currency with a category
            - Convert each expense to the home currency at the rate of that day
            - Cache exchange rates so entries can be added offline
            - Show total trip cost and a breakdown by category and country
            - Export the trip expenses as a CSV file
API:        REST (external)
            GET  https://api.frankfurter.app/{date}?from={currency}
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, drift, http, Frankfurter exchange rate API
```

---

## Example 161

**Intent:**
I get panic attacks sometimes, would be nice to have an app that guides my breathing with an animation, like box breathing or 4-7-8

**Spec:**
```
Type:       Mobile application
Data model: Pattern(id, name, inhale_s, hold_in_s, exhale_s, hold_out_s)
            Session(id, pattern_id -> Pattern, duration_s, completed_at)
Features:   - Guide breathing with an expanding and shrinking circle animation
            - Offer box breathing, 4-7-8 and custom patterns
            - Vibrate gently at each phase change so the eyes can stay closed
            - Start a session instantly from a home screen widget
            - Show a history of completed sessions
Storage:    Local on-device storage (SwiftData)
Tech stack: Swift, SwiftUI, Core Haptics, WidgetKit
```

---

## Example 162

**Intent:**
We are a cooperative of 15 small farms and want a mobile app where people in the city can order vegetables, eggs and cheese from several farms in one basket. Deliveries happen twice a week, so customers pick a delivery slot, and each farm needs to see what it has to pack.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Customer login with email + password, farm accounts created by an admin
Data model: Farm(id, name, description, photo_url)
            Product(id, farm_id -> Farm, name, unit, price, stock)
            Customer(id, name, email, phone, address)
            DeliverySlot(id, date, window_start, window_end, capacity)
            Order(id, customer_id -> Customer, slot_id -> DeliverySlot, status, total)
            OrderLine(id, order_id -> Order, product_id -> Product, quantity, price)
Features:   - Browse products from all farms and add them to a single basket
            - Choose a delivery slot with remaining capacity
            - Pay online at checkout
            - Show each farm a packing list of its items per delivery day
            - Reduce stock automatically and hide sold-out products
API:        REST
            GET  /products?farm={id}
            GET  /delivery-slots
            POST /orders
            GET  /farms/{id}/packing-list?date={date}
            PUT  /products/{id}/stock
Storage:    PostgreSQL
Tech stack: React Native, Python, Django REST Framework, Stripe
```

---

## Example 163

**Intent:**
bike sharing app, scan QR to unlock

**Spec:**
```
Type:       Mobile application with backend
Auth:       Phone number login with SMS code, card on file required
Data model: User(id, phone, payment_method_id, balance)
            Bike(id, qr_code, lock_id, lat, lng, battery_percent, status)
            Rental(id, user_id -> User, bike_id -> Bike, started_at, ended_at, distance_m, cost)
Features:   - Show available bikes on a map near the user
            - Scan the QR code on a bike to unlock its smart lock
            - Charge per minute and show the running cost during a ride
            - End the ride only when the bike is parked inside an allowed zone
            - Show ride history with receipts
API:        REST
            GET  /bikes/nearby?lat={lat}&lng={lng}
            POST /rentals
            POST /rentals/{id}/end
            GET  /rentals
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, mobile_scanner, Go, MQTT (lock commands), Stripe
```

---

## Example 164

**Intent:**
app to scan documents with phone camera and make pdf, like camscanner but without teh watermark

**Spec:**
```
Type:       Mobile application
Data model: Document(id, title, created_at, page_count, pdf_path)
            Page(id, document_id -> Document, image_path, position)
Features:   - Detect document edges automatically in the camera view
            - Correct perspective and enhance contrast of each page
            - Combine several pages into one PDF file
            - Reorder, rotate and delete pages before saving
            - Recognise text with OCR so PDFs are searchable
            - Share PDFs to email or other apps
Storage:    On-device file storage, local SQLite index
Tech stack: Kotlin, Jetpack Compose, ML Kit Document Scanner, ML Kit Text Recognition
```

---

## Example 165

**Intent:**
I'd love a hiking app using react native that records my trail and works with downloaded maps in the mountains where there's no signal

**Spec:**
```
Type:       Mobile application (offline-first)
Data model: Hike(id, name, started_at, ended_at, distance_m, elevation_gain_m)
            TrackPoint(id, hike_id -> Hike, lat, lng, altitude, recorded_at)
            OfflineRegion(id, name, bounds, min_zoom, max_zoom, size_mb)
Features:   - Download a map region with topographic tiles for offline use
            - Record the trail with GPS in the background
            - Show distance, elevation gain and time while hiking
            - Export a recorded hike as a GPX file
            - Import a GPX route and follow it on the map
Storage:    Local SQLite database, on-device tile packs
Tech stack: React Native, MapLibre React Native (offline packs), expo-location, expo-sqlite
```

---

## Example 166

**Intent:**
want to make a treasure hunt game for my nephew's birthday where clues unlock when you walk to the right spot in the park

**Spec:**
```
Type:       Mobile application (location-based game)
Data model: Hunt(id, name, created_at)
            Clue(id, hunt_id -> Hunt, position, text, hint, lat, lng, radius_m)
            Progress(id, hunt_id -> Hunt, clue_id -> Clue, found_at)
Features:   - Create a hunt by dropping clue locations on a map
            - Unlock the next clue when the player is within the clue's radius
            - Show a hot or cold distance indicator to the next spot
            - Reveal a hint after a set time without progress
            - Show a celebration screen when the last clue is found
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, geolocator, google_maps_flutter, sqflite
```

---

## Example 167

**Intent:**
I train for triathlons with a Bluetooth chest strap heart rate monitor. I want an app that connects to the strap, shows my live heart rate zone in big colours, and beeps if I go above zone 3 during easy runs. After the workout it should show time spent in each zone.

**Spec:**
```
Type:       Mobile application (wearable companion)
Data model: Profile(max_hr, resting_hr, zone_thresholds)
            Workout(id, started_at, ended_at, avg_hr, max_hr, target_zone)
            HeartRateSample(id, workout_id -> Workout, bpm, recorded_at)
Features:   - Connect to the chest strap via the BLE Heart Rate Service
            - Show live heart rate with a full-screen color for the current zone
            - Beep and vibrate when heart rate goes above the target zone
            - Calculate zones from max and resting heart rate (Karvonen)
            - Show time in each zone after the workout
            - Sync finished workouts to Apple Health
Storage:    Local on-device storage (Core Data), HealthKit
Tech stack: Swift, SwiftUI, Core Bluetooth, HealthKit, Swift Charts
```

---

## Example 168

**Intent:**
I want to see where is my children when they go to school, the app must show me their location on map and tell me when they arrive.

**Spec:**
```
Type:       Mobile application with backend (parent and child apps)
Auth:       Parent account with email + password, child phone linked by QR code
Data model: Family(id, name)
            Member(id, family_id -> Family, name, role, device_token)
            LocationUpdate(id, member_id -> Member, lat, lng, battery, recorded_at)
            Place(id, family_id -> Family, name, lat, lng, radius_m)
Features:   - Share the child's location in the background every few minutes
            - Show all family members on a live map
            - Notify the parent when a child arrives at or leaves a saved place
            - Show the child's battery level
            - Let the child send an "I'm OK" or "pick me up" message
API:        REST
            POST /locations
            GET  /families/{id}/members/locations
            POST /families/{id}/places
            POST /members/{id}/check-in
Storage:    PostgreSQL
Tech stack: Flutter, flutter_background_geolocation, Node.js, Express, Firebase Cloud Messaging
```

---

## Example 169

**Intent:**
events board for our small town

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email login for organisers, browsing without an account
Data model: Organizer(id, name, email, verified)
            Event(id, organizer_id -> Organizer, title, description, category, venue, starts_at, image_url)
            Interest(id, event_id -> Event, device_id)
Features:   - List upcoming events by date and category
            - Let verified organisers post and edit events
            - Mark an event as interested and add it to the phone calendar
            - Send a reminder the day before an interested event
            - Moderate new events before they go live
API:        REST
            GET  /events?from={date}&category={c}
            POST /events
            PUT  /events/{id}
            POST /events/{id}/interest
Storage:    Supabase Postgres
Tech stack: Flutter, Supabase, add_2_calendar
```

---

## Example 170

**Intent:**
me and my coworkers wanna do step challenges against each other, can we build that with firebase?

**Spec:**
```
Type:       Mobile application with backend
Auth:       Firebase Authentication (Google sign-in)
Data model: User(id, name, avatar_url)
            Challenge(id, name, creator_id -> User, start_date, end_date, invite_code)
            Participant(id, challenge_id -> Challenge, user_id -> User)
            DailySteps(id, user_id -> User, date, steps)
Features:   - Read daily step counts from Health Connect and Apple HealthKit
            - Create a challenge and invite coworkers with a code
            - Show a live leaderboard for each challenge
            - Send a push notification when someone overtakes you
            - Announce the winner when the challenge ends
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase Auth, Cloud Firestore, Cloud Functions, health package
```

---

## Example 171

**Intent:**
so I want to save money without thinking about it, like rounding up every card purchase to the next euro and putting the change in a savings goal

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password with 2FA, bank connection via open banking consent
Data model: User(id, email, password_hash, totp_secret)
            BankAccount(id, user_id -> User, provider_account_id, iban, kind)
            Transaction(id, account_id -> BankAccount, amount, merchant, booked_at)
            Goal(id, user_id -> User, name, target_amount, saved_amount, deadline)
            RoundUp(id, transaction_id -> Transaction, goal_id -> Goal, amount, transferred_at)
Features:   - Connect a bank account through an open banking provider
            - Calculate the round-up for each new card transaction
            - Transfer collected round-ups to the savings account once a week
            - Create savings goals and show progress toward each one
            - Let the user pause round-ups or set a multiplier
API:        REST
            POST /auth/login
            POST /bank-connections
            GET  /transactions
            GET  /goals
            POST /goals
            PATCH /round-up-settings
Storage:    PostgreSQL
Tech stack: React Native, Node.js, NestJS, GoCardless Bank Account Data API
```

---

## Example 172

**Intent:**
gratitude journal, 3 things a day

**Spec:**
```
Type:       Mobile application
Data model: Entry(id, date, item_1, item_2, item_3, photo_path, mood)
Features:   - Write three things you are grateful for each day
            - Attach an optional photo and mood to an entry
            - Send an evening reminder to write today's entry
            - Show a random past entry on the home screen
            - Lock the journal with Face ID or fingerprint
Storage:    Local on-device database (SQLite)
Tech stack: React Native, expo-sqlite, expo-local-authentication, expo-notifications
```

---

## Example 173

**Intent:**
anonymus posts app just for my college students where u need college email to join

**Spec:**
```
Type:       Mobile application with backend
Auth:       Sign up with a college email domain, verified by one-time code
Data model: College(id, name, email_domain)
            User(id, email_hash, college_id -> College, created_at)
            Post(id, author_id -> User, college_id -> College, text, created_at, score)
            Comment(id, post_id -> Post, author_id -> User, text, created_at)
            Vote(id, post_id -> Post, user_id -> User, value)
            Report(id, post_id -> Post, reporter_id -> User, reason)
Features:   - Show posts from the user's college only, without author names
            - Post text and upvote or downvote posts
            - Comment anonymously under posts
            - Sort the feed by new or top
            - Hide posts automatically after several reports and flag them for moderators
API:        REST
            POST /auth/request-code
            POST /auth/verify
            GET  /posts?sort={new|top}
            POST /posts
            POST /posts/{id}/votes
            POST /posts/{id}/comments
            POST /posts/{id}/report
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI, Redis (rate limiting)
```

---

## Example 174

**Intent:**
I organise singles events in my city and want to move them online. The idea is a speed dating app where people buy a ticket to a scheduled event, then get paired for 4-minute video calls one after another. After the event everyone picks who they'd like to see again, and mutual picks get each other's contact.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password login, age verification at sign-up
Data model: User(id, name, birthdate, gender, interested_in, photo_url)
            Event(id, title, starts_at, round_minutes, age_min, age_max, ticket_price)
            Ticket(id, event_id -> Event, user_id -> User, paid_at)
            Round(id, event_id -> Event, number, user_a -> User, user_b -> User)
            Pick(id, event_id -> Event, from_user -> User, to_user -> User)
Features:   - List upcoming events and sell tickets by card payment
            - Generate round pairings based on preferences and age range
            - Run 4-minute one-to-one video calls with a countdown and auto-switch
            - Let users pick who they want to meet again after the event
            - Reveal contact details only for mutual picks
API:        REST + WebSocket
            GET  /events
            POST /events/{id}/tickets
            WS   /events/{id}/live
            POST /events/{id}/picks
            GET  /events/{id}/matches
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express, Twilio Video, Stripe
```

---

## Example 175

**Intent:**
packing list app for trips

**Spec:**
```
Type:       Mobile application
Data model: Template(id, name)
            TemplateItem(id, template_id -> Template, name, category, quantity)
            PackingList(id, trip_name, date, template_id -> Template)
            Item(id, list_id -> PackingList, name, category, quantity, packed)
Features:   - Create a packing list from reusable templates such as beach or business
            - Add, edit and remove items grouped by category
            - Tick items off as they are packed
            - Show how many items are still left to pack
            - Save a finished list as a new template
Storage:    Local on-device database (Room)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 176

**Intent:**
can you spec out a SwiftUI app that listens to me say french words and tells me if my pronunciation is right?

**Spec:**
```
Type:       Mobile application (iOS)
Data model: Word(id, text, translation, phonetic, audio_path, level)
            Attempt(id, word_id -> Word, transcript, score, attempted_at)
Features:   - Play the native pronunciation of a word
            - Record the user saying the word
            - Transcribe the recording with on-device French speech recognition
            - Score the attempt by comparing the transcript with the target word
            - Repeat words with low scores more often
            - Show progress per word list
Storage:    Local on-device storage (SwiftData)
Tech stack: Swift, SwiftUI, Speech framework (SFSpeechRecognizer fr-FR), AVFoundation, SwiftData
```

---

## Example 177

**Intent:**
I fall asleep to stories on youtube but the ads wake me up, I want my own sleep stories app with a sleep timer

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email login, subscription managed by the app store
Data model: User(id, email, is_subscribed)
            Story(id, title, narrator, duration_s, audio_url, cover_url, category)
            Favorite(id, user_id -> User, story_id -> Story)
            ListenProgress(id, user_id -> User, story_id -> Story, position_s)
Features:   - Stream sleep stories with background audio playback
            - Set a sleep timer that fades out the audio
            - Download stories for offline listening
            - Save favourites and resume where you left off
            - Unlock premium stories with an in-app subscription
API:        REST
            GET  /stories?category={c}
            GET  /stories/{id}
            POST /favorites
            PUT  /progress/{story_id}
Storage:    PostgreSQL, S3 + CloudFront (audio files)
Tech stack: Flutter, just_audio, RevenueCat, Python, FastAPI
```

---

## Example 178

**Intent:**
App where home cooks in my area can sell their extra food to neighbours, the buyer come and pick it up.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Phone number login with SMS code
Data model: User(id, name, phone, lat, lng, rating)
            Dish(id, cook_id -> User, title, description, photo_url, price, portions_left, pickup_from, pickup_until)
            Reservation(id, dish_id -> Dish, buyer_id -> User, portions, status)
            Review(id, reservation_id -> Reservation, stars, comment)
Features:   - Post a dish with photo, price, portions and pickup time
            - Show dishes available nearby sorted by distance
            - Reserve portions and pay in the app
            - Show the cook's pickup address after the reservation is confirmed
            - Rate the cook after pickup
API:        REST
            GET  /dishes?lat={lat}&lng={lng}
            POST /dishes
            POST /dishes/{id}/reservations
            PATCH /reservations/{id}
            POST /reservations/{id}/review
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: React Native, Node.js, Express, Stripe Connect
```

---

## Example 179

**Intent:**
there are only 6 taxi drivers in our town and people call them on the phone, I'd like an app where you request a taxi and the nearest free driver gets it

**Spec:**
```
Type:       Mobile application with backend (rider and driver apps)
Auth:       Phone number login with SMS code, driver accounts approved by admin
Data model: Rider(id, name, phone)
            Driver(id, name, phone, car, plate, is_available, lat, lng)
            RideRequest(id, rider_id -> Rider, driver_id -> Driver, pickup_lat, pickup_lng, destination, status, created_at)
Features:   - Request a taxi from the current location with a destination
            - Offer the request to the nearest available driver first
            - Pass the request to the next driver if not accepted within 30 seconds
            - Show the driver's live position and arrival time to the rider
            - Let drivers toggle available or busy
API:        REST + WebSocket
            POST /rides
            POST /rides/{id}/accept
            POST /rides/{id}/complete
            PATCH /drivers/me/availability
            WS   /rides/{id}/tracking
Storage:    PostgreSQL, Redis (driver locations)
Tech stack: Flutter, Node.js, Socket.IO, Google Maps SDK
```

---

## Example 180

**Intent:**
photo collage maker app with templates and stickers i can share to insta

**Spec:**
```
Type:       Mobile application
Features:   - Pick several photos from the gallery
            - Arrange photos in grid and freestyle collage templates
            - Pan, zoom and swap photos inside each frame
            - Add stickers, text and a background color
            - Export the collage in square or story size
            - Share directly to Instagram or save to the gallery
Storage:    Device photo library
Tech stack: Flutter, image_picker, photo_manager, share_plus
```

---

## Example 181

**Intent:**
first aid guide that works offline

**Spec:**
```
Type:       Mobile application (offline)
Data model: Topic(id, title, category, steps, image_path, keywords)
            Bookmark(id, topic_id -> Topic)
Features:   - Show step-by-step first aid instructions with illustrations
            - Search topics such as burns, choking or bleeding
            - Run a CPR metronome at 110 beats per minute
            - Call the local emergency number with one tap
            - Bookmark important topics for quick access
Storage:    Bundled read-only SQLite database
Tech stack: React Native, expo-sqlite, expo-haptics
```

---

## Example 182

**Intent:**
I never remember where I parked in big car parks, an app where I tap once to save the spot and later it guides me back would be great

**Spec:**
```
Type:       Mobile application
Data model: ParkingSpot(id, lat, lng, floor, note, photo_path, parked_at, meter_expires_at)
Features:   - Save the current location as the parking spot with one tap
            - Add a floor number, note or photo of the spot
            - Show a compass arrow and distance back to the car
            - Remind the user before the parking meter runs out
            - Show the walking route on a map
Storage:    Local on-device storage (UserDefaults)
Tech stack: Swift, SwiftUI, Core Location, MapKit
```

---

## Example 183

**Intent:**
companion app in kotlin for my smart ring, sync steps and heart rate to Health Connect

**Spec:**
```
Type:       Mobile application (wearable companion, Android)
Data model: Ring(id, name, mac_address, firmware_version, battery_percent)
            StepRecord(id, ring_id -> Ring, steps, start_at, end_at, synced)
            HeartRateRecord(id, ring_id -> Ring, bpm, recorded_at, synced)
Features:   - Scan for and pair the ring over Bluetooth Low Energy
            - Sync step and heart rate data from the ring in a background worker
            - Write synced records to Health Connect
            - Show today's steps and resting heart rate on a dashboard
            - Show the ring's battery level and notify when it is low
Storage:    Local Room database, Health Connect
Tech stack: Kotlin, Jetpack Compose, Android BLE API, WorkManager, Health Connect SDK, Room
```

---

## Example 184

**Intent:**
My 14-year-old son can't focus on homework because of his phone. I'd like an app where he (or I) can turn on homework mode that blocks games and social media for a set time, but still allows calculator, dictionary and school apps. I want to get a weekly summary of how often he used it.

**Spec:**
```
Type:       Mobile application with backend (parent and teen apps)
Auth:       Parent account with email + password, teen device paired by code
Data model: Parent(id, email, password_hash)
            TeenDevice(id, parent_id -> Parent, name, paired_at)
            AllowedApp(id, device_id -> TeenDevice, package_name)
            FocusSession(id, device_id -> TeenDevice, started_by, started_at, planned_minutes, ended_at)
Features:   - Start homework mode for a set time from the teen or parent phone
            - Block all apps except an allowlist during homework mode
            - Require a parent PIN to end a session early
            - Schedule recurring homework hours on school days
            - Send the parent a weekly summary of focus sessions
API:        REST
            POST /devices/pair
            PUT  /devices/{id}/allowed-apps
            POST /devices/{id}/sessions
            GET  /devices/{id}/sessions?week={date}
Storage:    PostgreSQL
Tech stack: Kotlin (Android AccessibilityService), Python, FastAPI, Firebase Cloud Messaging
```

---

## Example 185

**Intent:**
My mother cooks home lunch boxes for office workers in our area, she want an app where customers subscribe for the week and choose veg or non-veg, and she see how many boxes to make each day.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Customer login with phone OTP, single admin login for the kitchen
Data model: Customer(id, name, phone, office_address, lat, lng)
            Plan(id, name, meals_per_week, price)
            Subscription(id, customer_id -> Customer, plan_id -> Plan, diet, start_date, end_date, status)
            DailyMenu(id, date, veg_item, nonveg_item)
            Skip(id, subscription_id -> Subscription, date)
Features:   - Subscribe to a weekly lunch plan and choose veg or non-veg
            - Show the daily menu for the coming week
            - Skip a day before 9 pm the evening before
            - Show the kitchen a daily count of veg and non-veg boxes
            - Generate a delivery list sorted by office area
            - Pay weekly by UPI
API:        REST
            POST /auth/otp
            GET  /menus?week={date}
            POST /subscriptions
            POST /subscriptions/{id}/skips
            GET  /admin/daily-count?date={date}
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Express, Razorpay (UPI payments)
```

---

## Example 186

**Intent:**
I'm making the driver side of a parcel delivery service, riders need to see their stops for the day, navigate to each one and take a photo as proof of delivery

**Spec:**
```
Type:       Mobile application with backend (courier app)
Auth:       Courier login with employee ID + password
Data model: Courier(id, name, phone, vehicle)
            Route(id, courier_id -> Courier, date, status)
            Stop(id, route_id -> Route, sequence, address, lat, lng, recipient_name, status)
            ProofOfDelivery(id, stop_id -> Stop, photo_url, signature_url, lat, lng, delivered_at)
Features:   - Show today's stops in optimised order
            - Open turn-by-turn navigation to the next stop
            - Capture a photo and signature as proof of delivery
            - Mark a stop as failed with a reason such as nobody home
            - Queue updates offline and sync when the connection returns
API:        REST
            GET  /couriers/me/route?date={date}
            POST /stops/{id}/delivered
            POST /stops/{id}/failed
            POST /couriers/me/location
Storage:    PostgreSQL, S3 (proof photos), local SQLite queue on device
Tech stack: React Native, react-native-vision-camera, Node.js, NestJS
```

---

## Example 187

**Intent:**
progres photo app for my gym journey, take photo every week in same pose and compare side by side

**Spec:**
```
Type:       Mobile application
Data model: ProgressPhoto(id, pose, image_path, weight_kg, taken_at)
            Measurement(id, waist_cm, chest_cm, arm_cm, measured_at)
Features:   - Show a ghost overlay of the last photo to match the same pose
            - Take front, side and back photos each week
            - Compare two dates side by side or with a slider
            - Create a time-lapse video from all photos of one pose
            - Keep photos in a private folder hidden from the gallery
Storage:    Private app storage (photos), local SQLite database
Tech stack: Kotlin, Jetpack Compose, CameraX, Room, Media3 Transformer
```

---

## Example 188

**Intent:**
prayer times app with qibla direction

**Spec:**
```
Type:       Mobile application (offline)
Data model: Settings(calculation_method, madhab, lat, lng, city_name)
            PrayerAlert(prayer, enabled, sound, minutes_before)
Features:   - Calculate the five daily prayer times from the location without internet
            - Show the qibla direction with the phone compass
            - Play an adhan notification at each prayer time
            - Let the user choose the calculation method and madhab
            - Show a countdown to the next prayer in a widget
Storage:    Local key-value storage (UserDefaults)
Tech stack: Swift, SwiftUI, Adhan Swift library, Core Location, WidgetKit
```

---

## Example 189

**Intent:**
I have IBS so finding a toilet fast is important, can there be an app showing the nearest public toilets and if they're open or accessible?

**Spec:**
```
Type:       Mobile application with backend
Auth:       Optional email login to add toilets and reviews
Data model: Toilet(id, name, lat, lng, opening_hours, wheelchair_accessible, baby_change, fee, source)
            Review(id, toilet_id -> Toilet, user_id -> User, cleanliness, comment, created_at)
            User(id, email, display_name)
Features:   - Show the nearest toilets with walking distance from the current location
            - Filter by open now, accessible, free and baby changing
            - Import toilet locations from OpenStreetMap
            - Let users add missing toilets and rate cleanliness
            - Open walking directions with one tap
API:        REST
            GET  /toilets/nearby?lat={lat}&lng={lng}&open_now=true
            POST /toilets
            POST /toilets/{id}/reviews
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, flutter_map, Python, FastAPI, OpenStreetMap Overpass API
```

---

## Example 190

**Intent:**
HIIT interval timer for Wear OS watches so I don't need my phone in the gym

**Spec:**
```
Type:       Smartwatch application (Wear OS)
Data model: Workout(id, name, work_s, rest_s, rounds, sets, set_rest_s)
            CompletedWorkout(id, workout_id -> Workout, avg_hr, calories, finished_at)
Features:   - Run work and rest intervals with a large countdown on the watch face
            - Vibrate at each interval change and at the last 3 seconds
            - Show live heart rate during the workout
            - Save custom interval workouts on the watch
            - Record finished workouts to Health Connect
Storage:    Local Room database on the watch
Tech stack: Kotlin, Compose for Wear OS, Health Services API, Room
```

---

## Example 191

**Intent:**
my kids never do their chores, thinking of an app where they earn pocket money for each chore and I approve it

**Spec:**
```
Type:       Mobile application with backend
Auth:       Parent account with email + password, kid profiles with PIN on a shared or own device
Data model: Family(id, name, currency)
            Parent(id, family_id -> Family, email)
            Kid(id, family_id -> Family, name, avatar, pin_hash, balance)
            Chore(id, family_id -> Family, title, reward, recurrence, assigned_kid_id -> Kid)
            Completion(id, chore_id -> Chore, kid_id -> Kid, photo_url, status, completed_at)
            Payout(id, kid_id -> Kid, amount, paid_at)
Features:   - Create chores with a reward and a daily or weekly schedule
            - Let kids mark a chore done with an optional photo
            - Let parents approve or reject completed chores
            - Add approved rewards to the kid's balance
            - Record payouts and set savings goals for each kid
API:        REST
            GET  /families/{id}/chores
            POST /chores
            POST /chores/{id}/completions
            PATCH /completions/{id}
            POST /kids/{id}/payouts
Storage:    Supabase Postgres
Tech stack: React Native, Supabase
```

---

## Example 192

**Intent:**
I manage a 120-unit apartment building and communication is a mess of paper notices and WhatsApp groups. I'd like an app where residents see official announcements, book shared spaces like the party room, and submit maintenance requests with photos that I can assign to our handyman and track until done.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Resident sign-up with unit number and an access code, manager and staff roles
Data model: Unit(id, number, floor)
            User(id, unit_id -> Unit, name, email, role)
            Announcement(id, author_id -> User, title, body, pinned, created_at)
            Space(id, name, capacity, rules)
            Booking(id, space_id -> Space, user_id -> User, starts_at, ends_at)
            MaintenanceRequest(id, unit_id -> Unit, reporter_id -> User, assignee_id -> User, title, description, photo_url, status, created_at)
Features:   - Post announcements and notify all residents
            - Book shared spaces in free time slots without double bookings
            - Submit maintenance requests with photos
            - Assign requests to staff and track status from open to done
            - Notify residents when their request status changes
API:        REST
            GET  /announcements
            POST /announcements
            GET  /spaces/{id}/availability?date={date}
            POST /bookings
            POST /maintenance-requests
            PATCH /maintenance-requests/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Flutter, Python, Django REST Framework, Firebase Cloud Messaging
```

---

## Example 193

**Intent:**
The doctor tell me to measure blood pressure two times daily, I need app for write the values and send report to doctor in PDF.

**Spec:**
```
Type:       Mobile application
Data model: Reading(id, systolic, diastolic, pulse, arm, note, measured_at)
            Reminder(id, time_of_day, enabled)
Features:   - Enter systolic, diastolic and pulse values with date and time
            - Remind the user to measure in the morning and evening
            - Color readings by blood pressure category
            - Show charts and averages for the last 7, 30 and 90 days
            - Create a PDF report for a date range and share it by email
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, fl_chart, pdf, share_plus
```

---

## Example 194

**Intent:**
debt payoff planner snowball vs avalanche

**Spec:**
```
Type:       Mobile application
Data model: Debt(id, name, balance, interest_rate, minimum_payment)
            Plan(strategy, monthly_budget)
            Payment(id, debt_id -> Debt, amount, paid_on)
Features:   - Add debts with balance, interest rate and minimum payment
            - Calculate a payoff schedule using snowball or avalanche order
            - Compare total interest and debt-free date for both strategies
            - Log payments and update remaining balances
            - Celebrate each debt that is paid off
Storage:    Local on-device storage (SwiftData)
Tech stack: Swift, SwiftUI, SwiftData, Swift Charts
```

---

## Example 195

**Intent:**
study app where me and frnds join a room and do pomodoro together and see who is studying rn

**Spec:**
```
Type:       Mobile application with backend
Auth:       Google sign-in
Data model: User(id, name, avatar_url)
            Room(id, name, owner_id -> User, focus_minutes, break_minutes, invite_code)
            RoomMember(id, room_id -> Room, user_id -> User, status)
            FocusSession(id, user_id -> User, room_id -> Room, minutes, completed_at)
Features:   - Create a study room and invite friends with a code
            - Run a shared pomodoro timer that is in sync for everyone in the room
            - Show which members are focusing or on a break
            - Show weekly study hours on a friends leaderboard
            - Send a nudge to a friend who is not studying
API:        REST + WebSocket
            POST /rooms
            POST /rooms/{code}/join
            WS   /rooms/{id}/timer
            GET  /leaderboard?week={date}
Storage:    PostgreSQL, Redis (room state)
Tech stack: React Native, Node.js, Socket.IO
```

---

## Example 196

**Intent:**
For our wedding I want guests to scan a QR code on the tables and upload their photos straight into one shared album, without installing anything complicated

**Spec:**
```
Type:       Mobile web application (PWA) with backend
Auth:       Guests join by QR code link with a name, couple login with email for admin
Data model: Event(id, couple_names, date, access_code)
            Guest(id, event_id -> Event, name)
            Media(id, event_id -> Event, guest_id -> Guest, url, kind, uploaded_at, hidden)
Features:   - Open the album from a QR code without an app install
            - Upload photos and short videos from the phone camera roll
            - Show a live gallery wall of new uploads
            - Let the couple hide unwanted photos
            - Download all originals as a ZIP after the wedding
API:        REST
            POST /events/{code}/guests
            POST /events/{id}/media
            GET  /events/{id}/media
            PATCH /media/{id}
            GET  /events/{id}/download
Storage:    PostgreSQL, S3 (originals and thumbnails)
Tech stack: Next.js (PWA), Node.js, AWS S3 presigned uploads, Sharp (thumbnails)
```

---

## Example 197

**Intent:**
I play badminton but my partners always cancel. Is possible an app to find other players near me of same level and book the court together?

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password or Google sign-in
Data model: Player(id, name, level, home_lat, home_lng, rating)
            Court(id, name, address, lat, lng)
            Game(id, court_id -> Court, host_id -> Player, starts_at, format, level_min, level_max, spots)
            GamePlayer(id, game_id -> Game, player_id -> Player, status)
Features:   - Create a game at a court with time, singles or doubles and level range
            - Find open games near you that match your level
            - Join a game and get a confirmation when it is full
            - Split the court fee between players
            - Rate players' level after the game to keep levels accurate
API:        REST
            GET  /games?lat={lat}&lng={lng}&level={n}
            POST /games
            POST /games/{id}/join
            POST /games/{id}/ratings
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Python, FastAPI, Stripe
```

---

## Example 198

**Intent:**
wallet for boarding passes with flight status

**Spec:**
```
Type:       Mobile application
Data model: Flight(id, airline, flight_number, date, origin, destination, gate, status, departs_at)
            BoardingPass(id, flight_id -> Flight, passenger_name, seat, barcode_data, format)
Features:   - Import a boarding pass by scanning its barcode or from a PDF
            - Show the barcode full screen at maximum brightness
            - Track live flight status, gate and delay changes
            - Notify the user about gate changes and boarding time
            - Show upcoming flights in a home screen widget
API:        REST (external)
            GET  https://aerodatabox.p.rapidapi.com/flights/number/{flight}/{date}
Storage:    Local on-device database (SQLite)
Tech stack: React Native, react-native-vision-camera, expo-sqlite, AeroDataBox API
```

---

## Example 199

**Intent:**
My cousin is deaf and I want to learn sign language properly. I'm imagining a Duolingo-style app with short daily lessons where videos show each sign, then quizzes ask me to pick the right meaning. It would be amazing if the camera could check if I'm doing the sign correctly.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password or Apple / Google sign-in
Data model: Course(id, sign_language, title)
            Lesson(id, course_id -> Course, position, title)
            Sign(id, lesson_id -> Lesson, word, video_url, handshape_landmarks)
            UserProgress(id, user_id -> User, lesson_id -> Lesson, xp, completed_at)
            User(id, email, streak_days, daily_goal_xp)
Features:   - Teach signs in short lessons with looping videos
            - Quiz the user by matching videos to words and words to videos
            - Check the user's sign with the camera using hand landmark detection
            - Award XP and track a daily streak
            - Download lessons for offline practice
API:        REST
            GET  /courses
            GET  /lessons/{id}
            POST /progress
            GET  /users/me/streak
Storage:    PostgreSQL, CDN (sign videos), on-device cache
Tech stack: Flutter, MediaPipe Hands (on-device), Python, FastAPI
```

---

## Example 200

**Intent:**
something for mindful walks, like it plays a guided audio while I walk and adapts to my walking pace

**Spec:**
```
Type:       Mobile application
Data model: Walk(id, guide_id, started_at, duration_s, distance_m, avg_cadence)
            Guide(id, title, theme, audio_path, duration_s)
Features:   - Play guided walking meditations with background audio
            - Measure walking cadence with the motion sensors
            - Suggest slowing down when the pace gets too fast
            - Play a soft bell every few minutes to return attention to the steps
            - Log walks with duration and distance
Storage:    Local on-device storage (Core Data)
Tech stack: Swift, SwiftUI, Core Motion (CMPedometer), AVFoundation
```

---

## Example 201

**Intent:**
app were bakeries and supermarkets sell there leftover food cheap at end of day so it dont get thrown away

**Spec:**
```
Type:       Mobile application with backend (customer and store apps)
Auth:       Customer login with email or Google, store accounts verified by admin
Data model: Store(id, name, address, lat, lng, category)
            SurpriseBag(id, store_id -> Store, title, price, original_value, quantity, pickup_from, pickup_until)
            Customer(id, name, email)
            Reservation(id, bag_id -> SurpriseBag, customer_id -> Customer, code, status, paid_at)
Features:   - Let stores post leftover food bags with price and pickup window
            - Show nearby bags on a map and in a list
            - Reserve and pay for a bag in the app
            - Show a pickup code that the store scans to confirm collection
            - Show customers how much food and CO2 they have saved
API:        REST
            GET  /bags/nearby?lat={lat}&lng={lng}
            POST /stores/{id}/bags
            POST /bags/{id}/reservations
            POST /reservations/{code}/collect
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin Multiplatform (Compose Multiplatform), Ktor server, Stripe
```

---

## Example 202

**Intent:**
taxis from the airport are so expensive, an app to find other people landing at the same time going the same direction and split a cab would be great

**Spec:**
```
Type:       Mobile application with backend
Auth:       Phone number login with SMS code
Data model: User(id, name, phone, rating)
            ShareRequest(id, user_id -> User, airport_code, flight_number, arrives_at, destination_lat, destination_lng, bags)
            Group(id, airport_code, status, created_at)
            GroupMember(id, group_id -> Group, request_id -> ShareRequest, share_amount)
Features:   - Enter flight number and destination to look for cab partners
            - Match travellers landing within 45 minutes with similar directions
            - Create a group chat and a meeting point at arrivals
            - Calculate each person's share by distance along the route
            - Rate co-travellers after the ride
API:        REST + WebSocket
            POST /share-requests
            GET  /share-requests/{id}/matches
            POST /groups
            WS   /groups/{id}/chat
            POST /groups/{id}/ratings
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Node.js, Express, Socket.IO, AeroDataBox API (flight arrivals)
```

---

## Example 203

**Intent:**
offline phrasebook for travelling in Japan

**Spec:**
```
Type:       Mobile application (offline)
Data model: Category(id, name, icon)
            Phrase(id, category_id -> Category, english, japanese, romaji, audio_path)
            Favorite(id, phrase_id -> Phrase)
Features:   - Browse phrases by category such as restaurant, transport and emergency
            - Play recorded native audio for each phrase
            - Show a phrase in large text to hand the phone to a local
            - Search phrases in English or romaji
            - Save favourite phrases
Storage:    Bundled SQLite database and audio files
Tech stack: Flutter, sqflite, just_audio
```

---

## Example 204

**Intent:**
we got a GPS collar for our dog, I want to build a react native app that shows where he is and alerts me if he leaves the garden

**Spec:**
```
Type:       Mobile application with backend (wearable companion)
Auth:       Email + password login, collar linked by serial number
Data model: Owner(id, email, password_hash)
            Pet(id, owner_id -> Owner, name, photo_url, collar_serial)
            Position(id, pet_id -> Pet, lat, lng, battery, recorded_at)
            SafeZone(id, pet_id -> Pet, polygon, active)
Features:   - Show the dog's live position on a map
            - Draw a safe zone around the garden on the map
            - Send a push alert when the dog leaves the safe zone
            - Show the walk history and daily activity minutes
            - Warn when the collar battery is low
API:        REST + WebSocket
            POST /collars/{serial}/positions
            GET  /pets/{id}/positions?from={time}
            PUT  /pets/{id}/safe-zone
            WS   /pets/{id}/live
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, react-native-maps, Node.js, Express, MQTT (collar data), Firebase Cloud Messaging
```

---

## Example 205

**Intent:**
bedtime routine app for my toddler with pictures so he knows whats next, bath teeth pyjamas story

**Spec:**
```
Type:       Mobile application
Data model: Routine(id, name, start_time)
            Step(id, routine_id -> Routine, position, title, image_path, minutes)
            RoutineRun(id, routine_id -> Routine, date, completed_steps, finished_at)
Features:   - Build a routine from picture cards in a set order
            - Show one big picture card at a time for the toddler to follow
            - Play a cheerful sound and show a star when a step is done
            - Show a visual timer for each step
            - Use the parent's own photos as step pictures
Storage:    Local on-device database (Room), on-device images
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 206

**Intent:**
map of vendors at the farmers market

**Spec:**
```
Type:       Mobile application with backend
Auth:       Vendor login with email + password, shoppers without an account
Data model: Market(id, name, address, open_days, map_image_url)
            Vendor(id, name, description, products, photo_url)
            Stall(id, market_id -> Market, vendor_id -> Vendor, x, y, date)
Features:   - Show the market layout with each vendor's stall position
            - Search vendors by product such as honey or bread
            - Let vendors mark what they are bringing this week
            - Save favourite vendors and get notified when they attend
            - Show market opening days and hours
Storage:    Cloud Firestore, Firebase Storage (vendor photos)
Tech stack: Flutter, Firebase Auth, Cloud Firestore, Cloud Functions
```

---

## Example 207

**Intent:**
I walk home alone late after my shifts and want a personal safety app. If I press the SOS button or shake the phone it should send my live location to three trusted contacts by SMS, start recording audio, and keep updating my location until I mark myself safe. It should also have a "walk with me" mode where friends can watch my route.

**Spec:**
```
Type:       Mobile application with backend
Auth:       Phone number login with SMS code
Data model: User(id, name, phone)
            TrustedContact(id, user_id -> User, name, phone)
            Alert(id, user_id -> User, started_at, resolved_at, audio_url)
            LocationPing(id, alert_id -> Alert, lat, lng, recorded_at)
            WalkSession(id, user_id -> User, destination, eta, share_token, ended_at)
Features:   - Trigger an SOS with a button, shake gesture or power button presses
            - Send an SMS with a live location link to trusted contacts
            - Record audio in the background and upload it to the cloud
            - Update the shared location every 15 seconds until marked safe
            - Share a walk with friends and alert them if the ETA is missed
API:        REST + WebSocket
            POST /alerts
            POST /alerts/{id}/locations
            POST /alerts/{id}/resolve
            POST /walks
            WS   /walks/{token}/live
Storage:    PostgreSQL, S3 (encrypted audio)
Tech stack: Kotlin (Android foreground service), Swift (iOS), Node.js, Twilio SMS
```

---

## Example 208

**Intent:**
cute little app for me and my girlfriend with a shared to-do list, date ideas and a countdown to our next trip, using supabase

**Spec:**
```
Type:       Mobile application with backend
Auth:       Supabase Auth (email magic link), two accounts linked by pairing code
Data model: Couple(id, pair_code, anniversary)
            Partner(id, couple_id -> Couple, name, avatar_url)
            Todo(id, couple_id -> Couple, text, done, created_by -> Partner)
            DateIdea(id, couple_id -> Couple, title, category, done_on)
            Countdown(id, couple_id -> Couple, title, target_date)
Features:   - Share a to-do list that updates live on both phones
            - Save date ideas and pick a random one
            - Show countdowns to trips and anniversaries
            - Send a quick "thinking of you" push to the partner
            - Mark date ideas as done with a photo memory
Storage:    Supabase Postgres (realtime), Supabase Storage (photos)
Tech stack: Flutter, supabase_flutter, Firebase Cloud Messaging
```

---

## Example 209

**Intent:**
my downloads folder is a total mess, can you make something that sorts everything into folders like images, docs, videos etc

**Spec:**
```
Type:       Command-line script (automation)
Features:   - Scan the Downloads folder for files (not subfolders)
            - Map file extensions to categories (Images, Documents, Videos, Audio, Archives, Installers)
            - Move each file into its category subfolder, creating it if missing
            - Add a number suffix when a file with the same name already exists
            - Put unknown extensions into an "Other" folder
            - Print a summary of how many files were moved per category
Input:      Path to the folder to organise (defaults to the user's Downloads folder)
Tech stack: Python, pathlib, shutil
```

---

## Example 210

**Intent:**
a bash script that backs up my home folder to an external drive every night and keeps the last 7 backups

**Spec:**
```
Type:       Command-line script (scheduled backup)
Features:   - Check that the external drive is mounted before starting
            - Copy the home folder to a dated snapshot folder with rsync
            - Hard-link unchanged files to the previous snapshot to save space (--link-dest)
            - Exclude cache folders and files listed in an exclude file
            - Delete snapshots older than the last 7
            - Write a log line with start time, end time and exit status
Input:      Source folder, backup drive mount point, exclude file
Storage:    External drive (dated snapshot folders)
Tech stack: Bash, rsync, cron (daily at 02:00)
```

---

## Example 211

**Intent:**
convert heic photos to jpg

**Spec:**
```
Type:       Command-line script (file conversion)
Features:   - Find all .heic files in a folder and its subfolders
            - Convert each file to .jpg with a set quality (default 90)
            - Keep the original EXIF data and date taken
            - Save the JPGs next to the originals or in an output folder
            - Skip files that were already converted
Input:      Folder path, optional output folder and JPEG quality
Tech stack: Python, Pillow, pillow-heif
```

---

## Example 212

**Intent:**
I'm job hunting and want something that checks a job board every morning for new python developer jobs in my city and saves them to a spreadsheet so I don't miss any. It should ignore jobs it has already seen.

**Spec:**
```
Type:       Web scraper (scheduled)
Data model: Job(id, title, company, location, salary, url, posted_at, first_seen_at)
Features:   - Fetch job search result pages for a keyword and location
            - Parse title, company, location, salary and link from each listing
            - Skip jobs whose URL is already saved
            - Append new jobs to a spreadsheet with the date found
            - Run automatically every morning at 08:00
            - Print how many new jobs were found
Input:      Search keyword, location, number of result pages to check
Storage:    SQLite (seen jobs), Excel file (job list)
Tech stack: Python, requests, BeautifulSoup, openpyxl, schedule
```

---

## Example 213

**Intent:**
clean old log files on linux server automaticaly

**Spec:**
```
Type:       Scheduled maintenance script
Features:   - Find log files in /var/log and app log folders older than a set number of days
            - Compress logs older than 7 days with gzip
            - Delete compressed logs older than 30 days
            - Skip files that are currently open by a process
            - Report how much disk space was freed
Input:      List of log folders, compress age and delete age in days
Tech stack: Bash, find, gzip, cron
```

---

## Example 214

**Intent:**
every month I have to email invoice PDFs to like 40 clients one by one, can a script do that for me?

**Spec:**
```
Type:       Email automation script
Features:   - Read the client list (name, email, invoice number) from a spreadsheet
            - Match each client to their invoice PDF by invoice number in the filename
            - Fill a personalised email body from a template
            - Send each email with the PDF attached over SMTP
            - Log sent and failed emails to a CSV file
            - Support a dry-run mode that shows emails without sending
Input:      Excel file of clients, folder of invoice PDFs, email template file
Tech stack: Python, smtplib, email.mime, openpyxl, Jinja2
```

---

## Example 215

**Intent:**
merge all pdfs in a folder into one file

**Spec:**
```
Type:       Command-line script (PDF processing)
Features:   - Collect all .pdf files in a folder
            - Sort files by name (or by modified date with a flag)
            - Merge all pages into a single PDF
            - Add a bookmark for each source file
            - Skip encrypted or broken PDFs and report them
Input:      Folder of PDF files, output file name
Tech stack: Python, pypdf
```

---

## Example 216

**Intent:**
need to parse our nginx access logs and see which IPs hit us the most and which urls give 404

**Spec:**
```
Type:       Log analysis script
Features:   - Parse nginx access log lines in the combined log format
            - Read plain and gzip-compressed log files
            - Count requests per IP and show the top 20
            - List URLs that returned 404 with their counts
            - Show requests per hour and status code breakdown
            - Export the results to CSV files
Input:      Path to one or more nginx access log files, optional date range
Tech stack: Python, re, gzip, collections.Counter
```

---

## Example 217

**Intent:**
powershell script to clean temp files and empty recycle bin on my windows pc

**Spec:**
```
Type:       System maintenance script
Features:   - Delete files in the user and Windows temp folders older than 2 days
            - Clear the Windows Update download cache
            - Empty the Recycle Bin on all drives
            - Skip files that are locked by running programs
            - Show disk space before and after cleanup
Input:      Optional switch to include the Windows Update cache
Tech stack: PowerShell, Clear-RecycleBin, Windows Task Scheduler
```

---

## Example 218

**Intent:**
i want to write my tweets in a spreadsheet and have them post themselves at the times i put in

**Spec:**
```
Type:       Social media posting automation
Features:   - Read posts with text, image path and scheduled time from a CSV file
            - Check every minute for posts whose time has come
            - Post the text and optional image to X (Twitter)
            - Mark each post as posted with the post URL in the CSV
            - Retry failed posts once and log the error
Input:      CSV file with columns: text, image_path, scheduled_at, status
API:        X API v2
            POST /2/tweets
Tech stack: Python, tweepy, pandas, schedule
```

---

## Example 219

**Intent:**
watch the price of some products on amazon and email me when it drops below what i want to pay

**Spec:**
```
Type:       Price monitoring script (scheduled)
Data model: Product(id, url, name, target_price)
            PriceCheck(id, product_id -> Product, price, checked_at)
Features:   - Read the list of product URLs and target prices from a config file
            - Fetch each product page and extract the current price
            - Save every price check to keep a price history
            - Send an email alert when the price falls below the target
            - Avoid sending the same alert twice for the same price
            - Run every 6 hours
Input:      YAML config with product URLs and target prices
Storage:    SQLite (price history)
Tech stack: Python, Playwright, smtplib, PyYAML, cron
```

---

## Example 220

**Intent:**
download a whole youtube playlist as mp3

**Spec:**
```
Type:       Command-line script (download manager)
Features:   - Read all video links from a YouTube playlist URL
            - Download the best audio stream for each video
            - Convert audio to MP3 at 192 kbps
            - Name files with the playlist index and video title
            - Skip videos that were already downloaded
Input:      Playlist URL, output folder
Tech stack: Python, yt-dlp, ffmpeg
```

---

## Example 221

**Intent:**
use imagemagick to resize all my product photos to 1200px wide and put our logo in the corner

**Spec:**
```
Type:       Batch image processing script
Features:   - Find all JPG and PNG files in the input folder
            - Resize each image to 1200px wide, keeping the aspect ratio
            - Overlay the logo in the bottom-right corner with 20px padding
            - Set the logo to 70% opacity
            - Save results to an output folder with the same file names
Input:      Input folder, output folder, logo PNG file
Tech stack: Bash, ImageMagick (magick, composite)
```

---

## Example 222

**Intent:**
My phone videos are huge. I want to shrink them all down to 720p with ffmpeg so they take less space but still look ok.

**Spec:**
```
Type:       Batch video conversion script
Features:   - Find all video files (.mp4, .mov) in a folder
            - Scale videos taller than 720p down to 720p, keeping the aspect ratio
            - Re-encode with H.264 at CRF 23 and AAC audio
            - Keep the original creation date in the new file
            - Show the size before and after for each file
            - Skip videos that are already 720p or smaller
Input:      Folder of videos, output folder
Tech stack: Bash, ffmpeg, ffprobe
```

---

## Example 223

**Intent:**
delete local git branches that are already merged

**Spec:**
```
Type:       Developer workflow script
Features:   - Fetch from the remote and prune deleted remote branches
            - List local branches already merged into main
            - Never delete main, master, develop or the current branch
            - Ask for confirmation before deleting
            - Delete the confirmed branches and print their names
Input:      Path to a git repository, optional base branch name
Tech stack: Bash, git
```

---

## Example 224

**Intent:**
every region sends me their own excel file with the same columns and I have to copy paste them all into one big sheet, please automate it

**Spec:**
```
Type:       Spreadsheet automation script
Features:   - Read every .xlsx file in a folder
            - Check that each file has the expected column headers
            - Add a "Region" column taken from the file name
            - Combine all rows into one table
            - Write the combined table to a master Excel file with a header style and filters
            - Report files that were skipped because of wrong columns
Input:      Folder of Excel files with the same columns
Tech stack: Python, pandas, openpyxl
```

---

## Example 225

**Intent:**
when my downloads finish on my home server I want the tv episodes moved into my plex folders with proper names

**Spec:**
```
Type:       Home server automation script
Features:   - Watch the completed downloads folder for new video files
            - Parse show name, season and episode from the file name
            - Rename files to "Show Name - S01E02.ext"
            - Move them to /media/TV/Show Name/Season 01
            - Trigger a Plex library refresh after moving
            - Ignore sample files and incomplete downloads
Input:      Downloads folder path, TV library root path, Plex token
API:        Plex Media Server API
            GET /library/sections/{id}/refresh
Tech stack: Python, watchdog, guessit, requests, systemd service
```

---

## Example 226

**Intent:**
find duplicate files on my drive

**Spec:**
```
Type:       Command-line script (file utility)
Features:   - Walk a folder tree and group files by size
            - Hash files with the same size using SHA-256
            - List groups of identical files with their paths
            - Show how much space duplicates are using
            - Optionally move duplicates to a review folder instead of deleting
Input:      Folder path, optional minimum file size
Tech stack: Go (filepath.WalkDir, crypto/sha256)
```

---

## Example 227

**Intent:**
i have hundreds of files named like "IMG_final_v2 (copy).png" and want to rename them with find and replace or regex

**Spec:**
```
Type:       Command-line script (bulk rename)
Features:   - List files in a folder that match a regex pattern
            - Replace the matched text with a replacement string (with capture groups)
            - Show a preview of old and new names before renaming
            - Stop if two files would end up with the same name
            - Save an undo file mapping new names back to old names
Input:      Folder path, regex pattern, replacement string
Tech stack: Python, re, pathlib, argparse
```

---

## Example 228

**Intent:**
please make tool which is converting many word documents to pdf at one time

**Spec:**
```
Type:       Batch document conversion script
Features:   - Find all .doc and .docx files in a folder
            - Convert each document to PDF
            - Save the PDFs to an output folder with the same names
            - Skip documents that already have an up-to-date PDF
            - Report documents that failed to convert
Input:      Folder of Word documents, output folder
Tech stack: Python, LibreOffice (soffice --headless --convert-to pdf), subprocess
```

---

## Example 229

**Intent:**
get the transactions out of my bank statement pdfs into excel

**Spec:**
```
Type:       PDF data extraction script
Features:   - Read the transaction tables from each statement PDF
            - Parse date, description, debit, credit and balance columns
            - Join descriptions that wrap onto two lines
            - Combine all statements into one table sorted by date
            - Export the table to an Excel file with number formatting
Input:      Folder of bank statement PDFs (text-based, not scanned)
Tech stack: Python, pdfplumber, pandas, openpyxl
```

---

## Example 230

**Intent:**
save all attachments from my gmail emails from a certain sender into a folder on my computer

**Spec:**
```
Type:       Email automation script
Features:   - Log in to Gmail with OAuth
            - Search emails by sender and optional date range
            - Download every attachment from the matching emails
            - Save files into folders named by email date
            - Skip attachments already downloaded
Input:      Sender email address, date range, output folder
API:        Gmail API
            GET /gmail/v1/users/me/messages?q={query}
            GET /gmail/v1/users/me/messages/{id}/attachments/{attachmentId}
Storage:    Local folder (attachments), JSON file (downloaded message IDs)
Tech stack: Python, google-api-python-client, google-auth-oauthlib
```

---

## Example 231

**Intent:**
my inbox is full of promo emails, delete the old ones automaticly every week

**Spec:**
```
Type:       Email cleanup script (scheduled)
Features:   - Connect to the mailbox over IMAP
            - Find emails in the Promotions category older than 30 days
            - Move them to the trash in batches
            - Keep emails from a whitelist of senders
            - Log how many emails were deleted each run
            - Run once a week
Input:      IMAP credentials (app password), age in days, whitelist file
Tech stack: Python, imapclient, cron
```

---

## Example 232

**Intent:**
check if my websites are up every 5 minutes and send me a telegram message if one goes down

**Spec:**
```
Type:       Uptime monitoring script
Data model: Site(url, expected_status, last_status, down_since)
Features:   - Send an HTTP request to each site every 5 minutes
            - Mark a site as down after 2 failed checks in a row
            - Send a Telegram message when a site goes down
            - Send a recovery message with the downtime length when it comes back
            - Record response time for each check
Input:      List of URLs, Telegram bot token and chat ID
API:        Telegram Bot API
            POST /bot{token}/sendMessage
Storage:    SQLite (check history)
Tech stack: Python, httpx, APScheduler
```

---

## Example 233

**Intent:**
bash script to email me when disk usage goes over 90%

**Spec:**
```
Type:       System monitoring script
Features:   - Check usage of every mounted filesystem with df
            - Compare usage against a threshold (default 90%)
            - Send an email listing the full filesystems and their usage
            - Include the 10 largest folders on the full disk
            - Run every 15 minutes
Input:      Threshold percentage, alert email address
Tech stack: Bash, df, du, mailx, cron
```

---

## Example 234

**Intent:**
backup our mysql database every night and upload it to s3, keep 30 days

**Spec:**
```
Type:       Scheduled backup script
Features:   - Dump the database with mysqldump using a single transaction
            - Compress the dump with gzip and add a timestamp to the file name
            - Upload the file to an S3 bucket
            - Delete backups older than 30 days from S3
            - Send an alert email if any step fails
Input:      Database credentials file, S3 bucket name, retention days
Storage:    Amazon S3 (backup files)
Tech stack: Bash, mysqldump, AWS CLI, cron
```

---

## Example 235

**Intent:**
when I scan documents they land in a folder as images-only pdfs, I want them OCR'd automatically so I can search the text

**Spec:**
```
Type:       Folder watcher (background script)
Features:   - Watch the scan folder for new PDF files
            - Wait until the file has finished writing
            - Run OCR and add a searchable text layer to the PDF
            - Save the result to a processed folder
            - Move failed files to an error folder and log the reason
Input:      Scan folder path, output folder, OCR language
Tech stack: Python, watchdog, OCRmyPDF, Tesseract
```

---

## Example 236

**Intent:**
post every new article from my blog's rss feed to my mastodon account

**Spec:**
```
Type:       Social media posting automation
Features:   - Read the blog RSS feed every 30 minutes
            - Find articles that have not been posted yet
            - Post the title, a short summary and the link to Mastodon
            - Add hashtags from the article's categories
            - Save posted article IDs so nothing is posted twice
Input:      RSS feed URL, Mastodon instance URL, access token
API:        Mastodon API
            POST /api/v1/statuses
Storage:    JSON file (posted article IDs)
Tech stack: Python, feedparser, Mastodon.py, cron
```

---

## Example 237

**Intent:**
python script that logs bitcoin and ethereum prices every hour into a google sheet

**Spec:**
```
Type:       Scheduled data logging script
Features:   - Fetch current BTC and ETH prices in USD every hour
            - Append a row with timestamp and prices to a Google Sheet
            - Add the 24-hour percentage change for each coin
            - Retry on network errors up to 3 times
Input:      Coin list, Google Sheet ID, service account key file
API:        CoinGecko API
            GET /api/v3/simple/price?ids={coins}&vs_currencies=usd
Storage:    Google Sheets
Tech stack: Python, requests, gspread, schedule
```

---

## Example 238

**Intent:**
track flight prices from bangalore to london for my dates and tell me when its cheap

**Spec:**
```
Type:       Price monitoring script (scheduled)
Data model: Route(id, origin, destination, depart_date, return_date, max_price)
            PriceQuote(id, route_id -> Route, airline, price, currency, checked_at)
Features:   - Search flight offers for each saved route twice a day
            - Save the cheapest price found on each check
            - Send an email when the price drops below the max price
            - Show the lowest price seen so far for each route
            - Plot price history per route as a line chart
Input:      Routes with airport codes, dates and max price
API:        Amadeus Flight Offers Search API
            GET /v2/shopping/flight-offers
Storage:    SQLite
Tech stack: Python, requests, matplotlib, cron
```

---

## Example 239

**Intent:**
tell me when games on my steam wishlist go on sale

**Spec:**
```
Type:       Price monitoring script (scheduled)
Features:   - Load the games on a public Steam wishlist
            - Check the current price and discount for each game daily
            - Send a Discord message when a game has a discount above a set percentage
            - Include the old price, new price and store link in the message
            - Remember alerts so each sale is only reported once
Input:      Steam profile ID, minimum discount, Discord webhook URL
API:        Steam Store API
            GET /api/appdetails?appids={id}&cc={country}
Storage:    JSON file (sent alerts)
Tech stack: Python, requests, cron
```

---

## Example 240

**Intent:**
batch convert wav files to mp3 using ffmpeg

**Spec:**
```
Type:       Batch audio conversion script
Features:   - Find all .wav files in a folder and its subfolders
            - Convert each file to MP3 with a chosen bitrate (default 320 kbps)
            - Copy title and artist tags into the MP3 file
            - Keep the same folder structure in the output folder
            - Run several conversions in parallel
Input:      Input folder, output folder, bitrate
Tech stack: Bash, ffmpeg, GNU parallel
```

---

## Example 241

**Intent:**
make thumbnails for all my videos

**Spec:**
```
Type:       Batch video processing script
Features:   - Find all video files in a folder
            - Read each video's length with ffprobe
            - Grab a frame at 10% of the video length
            - Save it as a 640px wide JPG with the video's name
            - Create a contact sheet with 9 frames per video as an option
Input:      Folder of videos, output folder
Tech stack: Python, ffmpeg, ffprobe, subprocess
```

---

## Example 242

**Intent:**
I keep accidentally committing API keys and debug prints. Can you set up a git pre-commit hook that checks the staged files for secrets and runs the linter, and blocks the commit if something is wrong?

**Spec:**
```
Type:       Git hook (developer workflow)
Features:   - Run on every commit before it is created
            - Scan staged files for secret patterns (API keys, tokens, private keys)
            - Block commits that add print or console.log debug lines
            - Run the linter and formatter only on staged files
            - Show which file and line failed each check
            - Allow skipping a check with a comment marker on the line
Input:      Staged files in the git repository
Tech stack: pre-commit framework, detect-secrets, Ruff, YAML config
```

---

## Example 243

**Intent:**
github actions workflow that creates a release with a changelog when i push a version tag

**Spec:**
```
Type:       CI/CD workflow (release automation)
Features:   - Trigger when a tag matching v*.*.* is pushed
            - Collect commit messages since the previous tag
            - Group commits into Features, Fixes and Other by conventional commit prefix
            - Build the project and attach the build files to the release
            - Create a GitHub release with the changelog as its description
Input:      Git tag pushed to the repository
Tech stack: GitHub Actions, git, gh CLI
```

---

## Example 244

**Intent:**
every friday turn the sales csv export into a nice formatted excel report with totals

**Spec:**
```
Type:       Report generation script (scheduled)
Features:   - Load the weekly sales CSV export
            - Calculate totals per product and per salesperson
            - Write data, summary and chart sheets to an Excel workbook
            - Apply currency formatting, bold headers and column widths
            - Add a bar chart of sales per salesperson
            - Run every Friday at 17:00 and save the report with the week number
Input:      CSV file with columns: date, salesperson, product, quantity, amount
Tech stack: Python, pandas, XlsxWriter, Windows Task Scheduler
```

---

## Example 245

**Intent:**
we run a workshop and need to make certificates for 200 people, names are in excel and we have a word template

**Spec:**
```
Type:       Document generation script (mail merge)
Features:   - Read participant names and course details from an Excel file
            - Fill the placeholders in the Word certificate template for each person
            - Save one .docx certificate per participant
            - Convert each certificate to PDF
            - Name files after the participant
Input:      Excel file of participants, Word template with {{name}} placeholders
Tech stack: Python, docxtpl, openpyxl, docx2pdf
```

---

## Example 246

**Intent:**
fill the same pdf form for many people from a spreadsheet

**Spec:**
```
Type:       PDF form filling script
Features:   - List the fillable field names in the PDF form
            - Map spreadsheet columns to form fields with a config file
            - Fill one copy of the form for each row in the spreadsheet
            - Flatten the filled forms so they can't be edited
            - Save each PDF named by a chosen column
Input:      Fillable PDF form, Excel or CSV file, field mapping file
Tech stack: Python, pypdf, pandas
```

---

## Example 247

**Intent:**
split a huge csv into smaller files

**Spec:**
```
Type:       Command-line script (file utility)
Features:   - Read a large CSV file in a streaming way without loading it all in memory
            - Split it into files of a set number of rows
            - Copy the header row into every part
            - Name parts with a running number (data_001.csv, data_002.csv)
            - Print the number of parts and rows written
Input:      CSV file path, rows per file
Tech stack: Python, csv module, argparse
```

---

## Example 248

**Intent:**
my desktop always ends up covered in files, can it get cleaned up every evening into a folder for that day

**Spec:**
```
Type:       Scheduled file organisation script
Features:   - Collect all files on the Desktop except shortcuts
            - Create an archive folder named with today's date
            - Move the files into that folder
            - Skip files that are still open or modified in the last 10 minutes
            - Delete empty archive folders older than 60 days
Input:      Desktop path, archive folder path
Tech stack: PowerShell, Windows Task Scheduler (daily at 18:00)
```

---

## Example 249

**Intent:**
keep a copy of my work folder synced to the nas with robocopy powershell

**Spec:**
```
Type:       Folder sync script (scheduled)
Features:   - Mirror the source folder to the NAS share with robocopy /MIR
            - Retry copy errors 3 times with a 5 second wait
            - Exclude temp files and Office lock files (~$*)
            - Write a log file per run with copied and failed files
            - Send a Windows toast notification when the sync fails
Input:      Source folder, NAS UNC path, log folder
Tech stack: PowerShell, robocopy, BurntToast module, Windows Task Scheduler
```

---

## Example 250

**Intent:**
docker on my server is eating all the disk, clean up the unused stuff weekly

**Spec:**
```
Type:       Scheduled maintenance script
Features:   - Remove stopped containers older than 24 hours
            - Remove dangling and unused images
            - Remove unused networks and build cache
            - Keep volumes unless a flag is passed
            - Log disk space reclaimed after each run
Input:      Optional flags for including volumes and minimum age
Tech stack: Bash, Docker CLI (docker system prune), cron (weekly)
```

---

## Example 251

**Intent:**
automaticaly update my ubuntu server every sunday and tell me if it needs reboot

**Spec:**
```
Type:       Scheduled maintenance script
Features:   - Refresh package lists and upgrade all packages without prompts
            - Remove packages that are no longer needed
            - Check if /var/run/reboot-required exists after upgrading
            - Send an email with the upgraded packages and reboot status
            - Stop and alert if the upgrade fails
Input:      Alert email address
Tech stack: Bash, apt, mailutils, cron
```

---

## Example 252

**Intent:**
my home IP keeps changing, update my cloudflare dns record from the raspberry pi when it does

**Spec:**
```
Type:       Home server automation script (dynamic DNS)
Features:   - Get the current public IP address every 5 minutes
            - Compare it with the last known IP
            - Update the A record in Cloudflare when the IP changes
            - Log every IP change with a timestamp
Input:      Cloudflare API token, zone ID, record name
API:        Cloudflare API
            GET /client/v4/zones/{zone_id}/dns_records?name={record}
            PUT /client/v4/zones/{zone_id}/dns_records/{record_id}
Storage:    Text file (last known IP)
Tech stack: Bash, curl, jq, cron
```

---

## Example 253

**Intent:**
check my home server hard disks health and warn me before they die

**Spec:**
```
Type:       System monitoring script
Features:   - Read SMART data from every disk
            - Check reallocated sectors, pending sectors and temperature
            - Run a short self-test on each disk weekly
            - Send an email alert when a value crosses its warning threshold
            - Send a weekly summary of all disks
Input:      List of disk devices, alert thresholds, email address
Tech stack: Bash, smartmontools (smartctl), msmtp, cron
```

---

## Example 254

**Intent:**
find failed logins in windows event log with powershell

**Spec:**
```
Type:       Log analysis script
Features:   - Read Security log events with ID 4625 (failed logon)
            - Extract time, user name, source IP and failure reason
            - Group failed attempts by user and by source IP
            - Flag IPs with more than 10 failures in one hour
            - Export the results to CSV
Input:      Time range in hours, optional computer name
Tech stack: PowerShell, Get-WinEvent, Export-Csv
```

---

## Example 255

**Intent:**
I want a daily html report from our apache logs, visitors, top pages, browsers, that kind of stuff

**Spec:**
```
Type:       Report generation script (scheduled)
Features:   - Parse yesterday's Apache access log
            - Count unique visitors by IP and user agent
            - List the top 20 pages and top referrers
            - Break down visits by browser and operating system
            - Render an HTML report with tables and charts
            - Run every day at 01:00 and keep reports for 90 days
Input:      Apache access log path, report output folder
Tech stack: Python, apache-log-parser, user-agents, Jinja2, Chart.js
```

---

## Example 256

**Intent:**
our app log is thousands of lines, group the errors by exception type so i can see which happen most

**Spec:**
```
Type:       Log analysis script
Features:   - Read application log files line by line
            - Join multi-line tracebacks into one error entry
            - Group errors by exception type and the file where they happened
            - Count each group and show first and last time seen
            - Print the groups sorted by count
            - Export the summary as JSON
Input:      Log file path, optional time range
Tech stack: Python, re, collections, argparse
```

---

## Example 257

**Intent:**
send me an email every morning with top headlines from a few news sites

**Spec:**
```
Type:       Web scraper (scheduled digest)
Features:   - Fetch the front pages or RSS feeds of the chosen news sites
            - Extract the top 5 headlines and links from each site
            - Remove duplicate stories across sites
            - Build an HTML email grouped by site
            - Send the email every day at 07:00
Input:      List of news site URLs, recipient email
Tech stack: Python, requests, BeautifulSoup, feedparser, smtplib, cron
```

---

## Example 258

**Intent:**
Looking for a flat. I want a script to check a property listing site every hour and send me new listings under 1500 a month with at least 2 bedrooms, with the photo and link.

**Spec:**
```
Type:       Web scraper (scheduled alerts)
Data model: Listing(id, url, title, price, bedrooms, area, photo_url, found_at)
Features:   - Load the search results page for the chosen area
            - Parse price, bedrooms, address, photo and link from each listing
            - Filter listings by max price and min bedrooms
            - Send each new listing to Telegram with its photo and link
            - Save seen listings so they are only sent once
            - Run every hour
Input:      Search URL, max price, min bedrooms, Telegram bot token
Storage:    SQLite (seen listings)
Tech stack: Python, Playwright, python-telegram-bot, cron
```

---

## Example 259

**Intent:**
download all images from a web page

**Spec:**
```
Type:       Command-line script (web scraper)
Features:   - Load the web page from a URL
            - Find image URLs in img tags, srcset and CSS backgrounds
            - Turn relative URLs into full URLs
            - Download images into a folder, skipping duplicates
            - Filter images by minimum width and height
Input:      Page URL, output folder, minimum size
Tech stack: Python, requests, BeautifulSoup, Pillow
```

---

## Example 260

**Intent:**
write me a download manager in go that takes a list of urls, downloads several at once and can resume if it stops

**Spec:**
```
Type:       Command-line download manager
Features:   - Read download URLs from a text file, one per line
            - Download up to N files at the same time
            - Resume partial downloads with HTTP Range requests
            - Show a progress bar per file with speed and ETA
            - Retry failed downloads with backoff
            - Check SHA-256 checksums when given
Input:      Text file of URLs, output folder, number of parallel downloads
Tech stack: Go, net/http, goroutines, mpb (progress bars)
```

---

## Example 261

**Intent:**
auto download new episodes of my podcasts

**Spec:**
```
Type:       Scheduled download script
Features:   - Read the list of podcast RSS feeds from a config file
            - Check each feed for new episodes every 2 hours
            - Download new episode audio into a folder per podcast
            - Name files with the publish date and episode title
            - Keep only the latest 10 episodes per podcast
Input:      Config file with feed URLs and episodes to keep
Storage:    JSON file (downloaded episode GUIDs)
Tech stack: Python, feedparser, requests, cron
```

---

## Example 262

**Intent:**
i have a lot of anime and series episodes with ugly names, please rename them to like "Show S01E05" format

**Spec:**
```
Type:       Command-line script (bulk rename)
Features:   - Scan a folder for video and subtitle files
            - Detect show name, season and episode number from the messy file name
            - Look up the episode title from TheTVDB
            - Rename files to "Show Name S01E05 - Episode Title.ext"
            - Rename matching subtitle files the same way
            - Show a preview and ask before renaming
Input:      Folder of episode files, optional show name override
API:        TheTVDB API v4
            GET /search?query={name}
            GET /series/{id}/episodes/default
Tech stack: Python, guessit, requests
```

---

## Example 263

**Intent:**
rename my research paper pdfs to the actual paper title and author

**Spec:**
```
Type:       Command-line script (bulk rename)
Features:   - Read the title and author from each PDF's metadata
            - Fall back to finding a DOI in the first page text
            - Look up title, first author and year from the DOI
            - Rename files to "Author Year - Title.pdf"
            - Remove characters that are not allowed in file names
Input:      Folder of PDF files
API:        Crossref REST API
            GET /works/{doi}
Tech stack: Python, pypdf, requests
```

---

## Example 264

**Intent:**
sort my mp3 collection into artist and album folders using the tags

**Spec:**
```
Type:       Command-line script (file organisation)
Features:   - Read artist, album, track number and title tags from each audio file
            - Move files to Music/Artist/Album/
            - Rename files to "01 - Title.mp3"
            - Put files with missing tags into an "Unknown" folder
            - Remove empty folders left behind
Input:      Music folder path, target library folder
Tech stack: Python, mutagen, pathlib
```

---

## Example 265

**Intent:**
convert all my markdown notes to pdf with pandoc

**Spec:**
```
Type:       Batch document conversion script
Features:   - Find all .md files in the notes folder
            - Convert each file to PDF with pandoc
            - Use a shared LaTeX template and table of contents
            - Keep images by resolving relative image paths
            - Only rebuild PDFs for notes that changed
Input:      Notes folder, output folder, optional template file
Tech stack: Bash, pandoc, xelatex, make
```

---

## Example 266

**Intent:**
look at our invoices excel, color the overdue ones red and email the customers a reminder

**Spec:**
```
Type:       Spreadsheet automation script
Features:   - Open the invoice workbook and read invoice rows
            - Find unpaid invoices past their due date
            - Fill overdue rows red and rows due in 7 days yellow
            - Send a reminder email to each overdue customer with the amount and days late
            - Write the reminder date into a "Last reminder" column
            - Save the updated workbook
Input:      Excel file with columns: invoice_no, customer, email, amount, due_date, paid
Tech stack: Python, openpyxl, smtplib
```

---

## Example 267

**Intent:**
every week my team members send timesheets in excel, i need one summary of hours per person per project for payroll

**Spec:**
```
Type:       Spreadsheet automation script
Features:   - Read all timesheet files in the week folder
            - Take the employee name from each file
            - Validate dates and hours (no negative values, max 24 per day)
            - Sum hours per employee per project
            - Write a summary workbook with a pivot-style table and totals
            - List files with errors in a separate sheet
Input:      Folder of timesheet Excel files with columns: date, project, hours
Tech stack: Python, pandas, openpyxl
```

---

## Example 268

**Intent:**
take a full page screenshot of some websites every day using playwright and keep them as an archive

**Spec:**
```
Type:       Scheduled web capture script
Features:   - Read the list of URLs from a text file
            - Open each page in headless Chromium and wait for it to load
            - Take a full page screenshot at 1440px width
            - Save screenshots in folders named by date and site
            - Delete screenshots older than one year
Input:      Text file of URLs, archive folder
Tech stack: Python, Playwright, cron
```

---

## Example 269

**Intent:**
tell me when a web page changes

**Spec:**
```
Type:       Web change monitor (scheduled)
Features:   - Fetch each watched page on a set interval
            - Extract only the chosen part of the page with a CSS selector
            - Compare the text with the last saved version
            - Send an email with a diff of what changed
            - Save each new version with a timestamp
Input:      List of URLs with CSS selectors and check interval
Storage:    Local folder (saved page versions)
Tech stack: Python, requests, BeautifulSoup, difflib, smtplib
```

---

## Example 270

**Intent:**
the sneakers i want are sold out, wanna get notified the moment they are back in stock

**Spec:**
```
Type:       Stock monitoring script
Features:   - Load the product page every 2 minutes with a random delay
            - Check if the chosen size shows as available
            - Send a push notification to the phone when it is in stock
            - Include the product link in the notification
            - Stop checking after the first alert until restarted
Input:      Product URL, shoe size, ntfy topic name
API:        ntfy
            POST /{topic}
Tech stack: Node.js, Playwright, node-fetch
```

---

## Example 271

**Intent:**
I want to send birthday wishes email automatic to my staffs from the excel list on their birthday

**Spec:**
```
Type:       Email automation script (scheduled)
Features:   - Read names, emails and birth dates from an Excel file
            - Find people whose birthday is today
            - Send a personalised birthday email from an HTML template
            - Send a list of today's birthdays to the manager
            - Run every morning at 09:00
Input:      Excel file with columns: name, email, birth_date
Tech stack: Python, openpyxl, smtplib, Jinja2, Windows Task Scheduler
```

---

## Example 272

**Intent:**
any email that comes in with an invoice attached should get forwarded to our accounting address automatically

**Spec:**
```
Type:       Email automation script
Features:   - Check the inbox over IMAP every 10 minutes for unread emails
            - Detect emails with PDF attachments and "invoice" in the subject or file name
            - Forward the matching emails with attachments to the accounting address
            - Move forwarded emails to an "Invoices/Forwarded" folder
            - Log each forwarded email with sender, subject and time
Input:      IMAP and SMTP settings, accounting email address, keyword list
Tech stack: Python, imap-tools, smtplib, schedule
```

---

## Example 273

**Intent:**
pdfs too big to email, make them smaller

**Spec:**
```
Type:       Batch PDF compression script
Features:   - Find all PDF files in a folder
            - Compress each PDF with a quality preset (screen, ebook, printer)
            - Downsample embedded images to a set DPI
            - Keep the original if the compressed file is not smaller
            - Show size before and after for each file
Input:      Folder of PDFs, quality preset, output folder
Tech stack: Bash, Ghostscript (gs -sDEVICE=pdfwrite)
```

---

## Example 274

**Intent:**
pull the audio out of a bunch of lecture videos so i can listen on my phone

**Spec:**
```
Type:       Batch audio extraction script
Features:   - Find all video files in a folder
            - Extract the audio track without the video
            - Encode audio as mono MP3 at 64 kbps to keep files small
            - Speed up audio by a chosen factor (e.g. 1.25x) as an option
            - Name the audio files after the videos
Input:      Folder of lecture videos, output folder, optional speed factor
Tech stack: Python, ffmpeg (atempo filter), subprocess
```

---

## Example 275

**Intent:**
turn a part of a video into a gif

**Spec:**
```
Type:       Command-line script (video to GIF)
Features:   - Cut the clip between a start and end time
            - Scale the clip to a chosen width and frame rate
            - Generate an optimised color palette for better quality
            - Write the GIF using the palette
            - Print the final file size
Input:      Video file, start time, end time, width, fps
Tech stack: Bash, ffmpeg (palettegen, paletteuse)
```

---

## Example 276

**Intent:**
i set my camera to take a photo every 30 seconds all day, now i want to make a timelapse video out of the thousands of photos

**Spec:**
```
Type:       Batch image to video script
Features:   - Sort photos in the folder by capture time from EXIF
            - Resize all photos to 1920x1080 with cropping to 16:9
            - Combine photos into an MP4 at a chosen frame rate
            - Add a deflicker filter to smooth brightness changes
            - Add an optional music track that fades out at the end
Input:      Folder of photos, frame rate, optional audio file
Tech stack: Python, Pillow, ffmpeg
```

---

## Example 277

**Intent:**
burn the srt subtitles into my videos permanantly so they show on any player

**Spec:**
```
Type:       Batch video processing script
Features:   - Match each video with the .srt file of the same name
            - Burn the subtitles into the video with a chosen font and size
            - Keep the original audio without re-encoding
            - Save results with a "_subbed" suffix
            - List videos that have no matching subtitle file
Input:      Folder of videos and .srt files, font name, font size
Tech stack: Bash, ffmpeg (subtitles filter), libass
```

---

## Example 278

**Intent:**
before I post photos online I want to remove the GPS location and camera info from them

**Spec:**
```
Type:       Command-line script (privacy tool)
Features:   - Read all JPG, PNG and HEIC files in a folder
            - Remove GPS tags and camera make, model and serial number
            - Keep the date taken and orientation tags
            - Save cleaned copies to an output folder
            - Print which tags were removed from each file
Input:      Folder of photos, output folder
Tech stack: ExifTool, Bash
```

---

## Example 279

**Intent:**
a node script using sharp to convert my website images from png and jpg to webp in different sizes

**Spec:**
```
Type:       Build-time image processing script
Features:   - Find all PNG and JPG files in the source images folder
            - Create WebP versions at 480, 960 and 1920px wide
            - Never upscale images smaller than the target width
            - Skip images whose WebP output is newer than the source
            - Write a JSON manifest of generated files for use in srcset
Input:      Source images folder, output folder, list of widths
Tech stack: Node.js, sharp, fast-glob
```

---

## Example 280

**Intent:**
I take photos of my receipts on my phone. I want a script that reads the shop, date and total from each photo and puts them in an expenses spreadsheet. It should flag the ones it can't read properly.

**Spec:**
```
Type:       OCR data extraction script
Features:   - Read receipt photos from a folder
            - Straighten and increase contrast before OCR
            - Extract text with OCR and find the shop name, date and total with patterns
            - Add one row per receipt to an expenses Excel file
            - Flag rows where the date or total could not be found
            - Move processed photos to a "done" folder
Input:      Folder of receipt photos (JPG, PNG)
Storage:    Excel file (expenses)
Tech stack: Python, OpenCV, pytesseract, openpyxl
```

---

## Example 281

**Intent:**
git pull all the repos inside a folder at once

**Spec:**
```
Type:       Developer workflow script
Features:   - Find every git repository one level below the folder
            - Run git pull --ff-only in each repository in parallel
            - Skip repos with uncommitted changes and list them
            - Show a table of repo name, branch and result
Input:      Parent folder path
Tech stack: PowerShell, git, ForEach-Object -Parallel
```

---

## Example 282

**Intent:**
github action to bump version and publish my package to npm when i merge to main

**Spec:**
```
Type:       CI/CD workflow (package publishing)
Features:   - Trigger on push to the main branch
            - Run the tests and stop if any fail
            - Bump the version from commit messages (major, minor, patch)
            - Commit the new version and create a git tag
            - Publish the package to npm with provenance
Input:      Commits merged to main
Tech stack: GitHub Actions, Node.js, npm, semantic-release
```

---

## Example 283

**Intent:**
backup all my github repos to my own server in case github account gets lost

**Spec:**
```
Type:       Scheduled backup script
Features:   - List all repositories of the user, including private ones
            - Clone new repositories as mirrors
            - Update existing mirrors with git remote update
            - Archive each mirror into a dated tar.gz weekly
            - Send an email summary with the number of repos backed up
Input:      GitHub username, personal access token, backup folder
API:        GitHub REST API
            GET /user/repos?per_page=100&page={n}
Storage:    Local disk (mirror repositories and archives)
Tech stack: Python, requests, git, cron
```

---

## Example 284

**Intent:**
weekly report of which pip packages are outdated in our projects

**Spec:**
```
Type:       Scheduled report script
Features:   - Read requirements.txt from each project folder
            - Look up the latest version of each package on PyPI
            - Mark packages as major, minor or patch behind
            - Highlight packages with known security advisories
            - Post the report to a Slack channel every Monday
Input:      List of project folders, Slack webhook URL
API:        PyPI JSON API
            GET /pypi/{package}/json
Tech stack: Python, requests, packaging, pip-audit, cron
```

---

## Example 285

**Intent:**
commit my notes folder to git every hour automaticly so i have history

**Spec:**
```
Type:       Scheduled git automation script
Features:   - Check the notes folder for changed files every hour
            - Stage all changes and commit with a timestamp message
            - Push the commit to the remote repository
            - Do nothing when there are no changes
            - Log push errors to a file
Input:      Notes repository path
Tech stack: Bash, git, cron
```

---

## Example 286

**Intent:**
sometimes our api service crashes at night and nobody notices, i want it restarted automatically and someone told about it

**Spec:**
```
Type:       Service watchdog script
Features:   - Check the service health endpoint every minute
            - Restart the service with systemctl after 3 failed checks
            - Wait and confirm the service is healthy after restart
            - Send a Slack message with the time and the last 50 log lines
            - Stop restarting after 5 tries in one hour and send an urgent alert
Input:      Service name, health check URL, Slack webhook URL
Tech stack: Bash, curl, systemctl, journalctl, systemd timer
```

---

## Example 287

**Intent:**
check ssl certificates of our domains and warn before they expire

**Spec:**
```
Type:       Scheduled monitoring script
Features:   - Connect to each domain on port 443 and read the certificate
            - Calculate days until the certificate expires
            - Send an email listing certificates expiring within 21 days
            - Report domains where the connection or handshake fails
            - Run once a day
Input:      Text file of domain names, warning days, email address
Tech stack: Go, crypto/tls, net/smtp, cron
```

---

## Example 288

**Intent:**
powershell script that shuts down my pc at night if nobody is using it

**Spec:**
```
Type:       System automation script
Features:   - Run every 15 minutes between 23:00 and 06:00
            - Check how long the user has been idle
            - Skip shutdown if a download, game or video call program is running
            - Show a warning popup with a 5 minute countdown
            - Shut down the PC if the warning is not cancelled
Input:      Idle time in minutes, list of programs that block shutdown
Tech stack: PowerShell, user32 GetLastInputInfo, Windows Task Scheduler
```

---

## Example 289

**Intent:**
backup a folder to google drive every night with rclone

**Spec:**
```
Type:       Scheduled backup script
Features:   - Sync the folder to a Google Drive remote with rclone sync
            - Move deleted or changed files to a dated backup folder on Drive
            - Limit bandwidth during working hours
            - Write a log file and send an email if the sync fails
Input:      Local folder path, rclone remote name, bandwidth limit
Storage:    Google Drive
Tech stack: Bash, rclone, cron
```

---

## Example 290

**Intent:**
when i put my camera sd card in, copy the photos to my pc sorted into year and month folders

**Spec:**
```
Type:       Photo import script
Features:   - Detect when a drive with a DCIM folder is connected
            - Copy photos and videos to Pictures/YYYY/MM based on date taken
            - Skip files already imported by comparing name and size
            - Verify each copy with a checksum
            - Show a notification with the number of files imported
Input:      SD card drive, target photo library folder
Tech stack: Python, exifread, psutil, plyer (notifications)
```

---

## Example 291

**Intent:**
change my desktop wallpaper every day to a nice photo

**Spec:**
```
Type:       Desktop automation script (scheduled)
Features:   - Download a random landscape photo once a day
            - Pick a photo that matches the screen resolution
            - Set the photo as the desktop wallpaper
            - Keep the last 30 wallpapers in a folder
Input:      Search keyword, Unsplash access key
API:        Unsplash API
            GET /photos/random?query={keyword}&orientation=landscape
Tech stack: Python, requests, ctypes (SystemParametersInfo), Windows Task Scheduler
```

---

## Example 292

**Intent:**
remind my team in slack to write their standup update every morning, and ping the ones who didn't

**Spec:**
```
Type:       Chat automation script (scheduled)
Features:   - Post a standup reminder in the team channel at 09:30 on weekdays
            - Read replies in the reminder's thread at 10:30
            - Find team members who have not replied
            - Send each missing member a direct message
            - Skip people marked as on holiday in a config file
Input:      Slack bot token, channel ID, team member list
API:        Slack Web API
            POST /api/chat.postMessage
            GET  /api/conversations.replies
Tech stack: Python, slack_sdk, APScheduler
```

---

## Example 293

**Intent:**
node script that posts yesterday's sales total from our postgres database to slack every morning

**Spec:**
```
Type:       Scheduled reporting script
Features:   - Query yesterday's order count and revenue from PostgreSQL
            - Compare them with the same weekday last week
            - Format a Slack message with totals and percentage change
            - Post the message to the sales channel at 08:00
Input:      Database connection string, Slack webhook URL
Storage:    PostgreSQL (read only)
Tech stack: Node.js, pg, node-cron, Slack incoming webhooks
```

---

## Example 294

**Intent:**
post in our discord when a youtube channel uploads a new video

**Spec:**
```
Type:       Social media automation script
Features:   - Check the channel's YouTube RSS feed every 10 minutes
            - Detect videos that have not been announced yet
            - Post the title, thumbnail and link to a Discord channel
            - Save announced video IDs to avoid repeats
Input:      YouTube channel ID, Discord webhook URL
API:        Discord Webhooks
            POST /api/webhooks/{id}/{token}
Storage:    JSON file (announced video IDs)
Tech stack: Python, feedparser, requests, cron
```

---

## Example 295

**Intent:**
we are small bakery, I want to plan the facebook page posts in excel with picture and they go online on the date by itself

**Spec:**
```
Type:       Social media posting automation
Features:   - Read posts with text, image file and publish date from an Excel sheet
            - Upload each post as a scheduled post on the Facebook Page
            - Mark the row as scheduled with the returned post ID
            - Skip rows with missing images or past dates and report them
Input:      Excel file with columns: text, image_path, publish_at, status
API:        Facebook Graph API
            POST /{page_id}/photos
            POST /{page_id}/feed
Tech stack: Python, requests, openpyxl
```

---

## Example 296

**Intent:**
convert old xls files to xlsx

**Spec:**
```
Type:       Batch file conversion script
Features:   - Find all .xls files in a folder and subfolders
            - Open each file in Excel and save it as .xlsx
            - Keep formulas, formatting and all sheets
            - Move the original .xls files to an "old" folder
            - Report files that could not be opened
Input:      Folder path
Tech stack: PowerShell, Excel COM automation
```

---

## Example 297

**Intent:**
our contacts sheet has duplicates and phone numbers written in every format possible, clean it up

**Spec:**
```
Type:       Data cleaning script
Features:   - Load contacts from an Excel or CSV file
            - Normalise phone numbers to E.164 format with a default country
            - Trim names and lower-case email addresses
            - Find duplicates by email or phone and merge their fields
            - Write the cleaned list and a separate sheet of removed duplicates
Input:      Contacts file with columns: name, email, phone, company
Tech stack: Python, pandas, phonenumbers, openpyxl
```

---

## Example 298

**Intent:**
replace the old company name with the new one in all our word documents

**Spec:**
```
Type:       Batch document editing script
Features:   - Find all .docx files in a folder tree
            - Replace text in paragraphs, tables, headers and footers
            - Keep the original formatting of the replaced text
            - Save a backup copy before changing each file
            - Print the number of replacements per document
Input:      Folder path, find text, replace text
Tech stack: Python, python-docx
```

---

## Example 299

**Intent:**
add page numbers and a CONFIDENTIAL watermark to pdf

**Spec:**
```
Type:       PDF processing script
Features:   - Draw a diagonal semi-transparent "CONFIDENTIAL" text on every page
            - Add "Page X of Y" at the bottom centre of each page
            - Handle pages with different sizes and rotations
            - Save the result as a new PDF
Input:      PDF file, watermark text, output file
Tech stack: Python, pypdf, reportlab
```

---

## Example 300

**Intent:**
I have a 600 page manual pdf, split it into separate pdfs by chapter

**Spec:**
```
Type:       PDF processing script
Features:   - Read the top-level bookmarks to find where each chapter starts
            - Split the PDF into one file per chapter
            - Name files with the chapter number and title
            - Split by fixed page ranges when there are no bookmarks
Input:      PDF file, optional page ranges file
Tech stack: Python, pypdf
```

---

## Example 301

**Intent:**
scrape our competitors prices for our product list every monday and put it next to our prices in excel

**Spec:**
```
Type:       Web scraper (scheduled)
Data model: Product(sku, name, our_price)
            CompetitorUrl(sku -> Product, competitor, url, css_selector)
            PriceRecord(sku -> Product, competitor, price, scraped_at)
Features:   - Read products and competitor page URLs from a config sheet
            - Scrape the price from each competitor page using its selector
            - Save every price with the date for history
            - Write a comparison sheet with our price, competitor prices and difference
            - Highlight products where a competitor is cheaper
Input:      Excel config file with products and competitor URLs
Storage:    SQLite (price history), Excel file (weekly report)
Tech stack: Python, requests, BeautifulSoup, pandas, openpyxl, cron
```

---

## Example 302

**Intent:**
desktop notification when a stock i own goes above or below a price

**Spec:**
```
Type:       Price alert script
Features:   - Read stock symbols with upper and lower limits from a config file
            - Fetch the latest price every 5 minutes during market hours
            - Show a desktop notification when a price crosses a limit
            - Only alert once per crossing until the price returns inside the range
Input:      YAML config with symbols and limits
Tech stack: Python, yfinance, plyer, schedule
```

---

## Example 303

**Intent:**
my internet feels slow at night, log speed test results every hour so i can prove it to my isp

**Spec:**
```
Type:       Scheduled data logging script
Data model: SpeedTest(id, tested_at, download_mbps, upload_mbps, ping_ms, server)
Features:   - Run an internet speed test every hour
            - Save download, upload and ping with a timestamp
            - Draw a chart of speeds by hour of day
            - Export the results to CSV for the ISP complaint
Input:      Test interval, optional preferred server ID
Storage:    SQLite
Tech stack: Python, speedtest-cli, matplotlib, cron
```

---

## Example 304

**Intent:**
bash script to backup my minecraft server world without corrupting it

**Spec:**
```
Type:       Scheduled backup script
Features:   - Send save-off and save-all to the server console through screen or RCON
            - Wait for the save to finish, then archive the world folder with tar and zstd
            - Turn saving back on with save-on, even if the backup fails
            - Keep 24 hourly and 7 daily backups
            - Announce the backup in the in-game chat
Input:      Server folder, backup folder, RCON password
Tech stack: Bash, mcrcon, tar, zstd, cron
```

---

## Example 305

**Intent:**
our college puts exam notices on a website page, i want telegram msg when new notice come

**Spec:**
```
Type:       Web scraper (scheduled alerts)
Features:   - Fetch the notices page every 15 minutes
            - Parse notice titles, dates and PDF links
            - Compare with saved notices to find new ones
            - Send each new notice to a Telegram chat with its link
Input:      Notice page URL, Telegram bot token, chat ID
API:        Telegram Bot API
            POST /bot{token}/sendMessage
Storage:    JSON file (seen notices)
Tech stack: Python, requests, BeautifulSoup, cron
```

---

## Example 306

**Intent:**
convert my epub ebooks to pdf for my old reader

**Spec:**
```
Type:       Batch ebook conversion script
Features:   - Find all .epub files in a folder
            - Convert each ebook with calibre's ebook-convert
            - Set page size and margins for a 6-inch screen
            - Keep the cover and table of contents
            - Skip books that are already converted
Input:      Folder of EPUB files, output folder, page size
Tech stack: Bash, calibre (ebook-convert)
```

---

## Example 307

**Intent:**
I record all my meetings as audio files and I'd like them turned into text automatically. Put the transcript next to each recording and also make a short summary of each file if possible.

**Spec:**
```
Type:       Batch transcription script
Features:   - Watch a folder for new audio files (.mp3, .m4a, .wav)
            - Transcribe each file to text with timestamps
            - Save the transcript as .txt and .srt next to the recording
            - Generate a short bullet summary of each transcript with an LLM
            - Skip recordings that already have a transcript
Input:      Folder of meeting recordings, Whisper model size
Tech stack: Python, faster-whisper, watchdog, LLM API
```

---

## Example 308

**Intent:**
I'm launching a small SaaS and need a backend that handles monthly and yearly subscriptions through Stripe, so people can upgrade, downgrade or cancel.

**Spec:**
```
Type:       REST API service (payments)
Auth:       Email + password login with JWT access tokens
Data model: User(id, email, password_hash, stripe_customer_id)
            Plan(id, name, interval, price_cents, stripe_price_id)
            Subscription(id, user_id -> User, plan_id -> Plan, stripe_subscription_id, status, current_period_end)
Features:   - Create a Stripe Checkout session for the chosen plan
            - Upgrade or downgrade a subscription with proration
            - Cancel a subscription at the end of the billing period
            - Verify and handle Stripe webhooks (invoice.paid, customer.subscription.updated)
            - Open the Stripe customer portal for card and invoice management
            - Block paid features when a subscription is past due
API:        REST
            GET  /plans
            POST /billing/checkout
            POST /billing/change-plan
            POST /billing/cancel
            POST /billing/portal
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Node.js, Express, Stripe Node SDK, Prisma
```

---

## Example 309

**Intent:**
sms reminders for my dental clinic patients the day before their appointment

**Spec:**
```
Type:       Background notification service
Auth:       Staff login (email + password, session cookie)
Data model: Patient(id, name, phone, opted_out)
            Appointment(id, patient_id -> Patient, starts_at, dentist, reminder_sent_at)
            SmsLog(id, appointment_id -> Appointment, twilio_sid, status, sent_at)
Features:   - Run a scheduled job every hour to find appointments starting in the next 24 hours
            - Send an SMS reminder through Twilio with date, time and dentist name
            - Let patients reply C to confirm or R to request a reschedule
            - Record delivery status from Twilio status callbacks
            - Stop messaging patients who reply STOP
API:        REST
            POST /appointments
            GET  /appointments?date={date}
            POST /webhooks/twilio/inbound
            POST /webhooks/twilio/status
Storage:    PostgreSQL
Tech stack: Python, Django, Celery + Celery Beat, Redis (broker), Twilio API
```

---

## Example 310

**Intent:**
url shortener in go with click stats

**Spec:**
```
Type:       REST API service (URL shortener)
Auth:       API key per user (Authorization: Bearer header)
Data model: User(id, email, api_key_hash)
            Link(id, user_id -> User, code, target_url, created_at, expires_at)
            Click(id, link_id -> Link, clicked_at, referrer, country, user_agent)
Features:   - Create a short code (random 7-character base62 or custom alias)
            - Redirect short URLs to the target with HTTP 302
            - Record each click with referrer, country and device
            - Show click counts per day, top referrers and top countries
            - Expire links after an optional date
API:        REST
            POST /links
            GET  /links
            GET  /links/{code}/stats
            DELETE /links/{code}
            GET  /{code}
Storage:    PostgreSQL (links, clicks), Redis (hot code lookup cache)
Tech stack: Go, Gin, pgx, go-redis, MaxMind GeoLite2
```

---

## Example 311

**Intent:**
QR code generator API

**Spec:**
```
Type:       REST API service
Auth:       API key (X-API-Key header)
Features:   - Generate a QR code from text or a URL
            - Return the image as PNG or SVG
            - Set size, margin, error correction level and colors
            - Add an optional logo in the center of the code
            - Limit each API key to 1000 codes per day
API:        REST
            POST /qr
            GET  /qr?data={text}&format={png|svg}&size={px}
Storage:    Redis (rate limit counters)
Tech stack: Python, FastAPI, segno, Pillow
```

---

## Example 312

**Intent:**
can you make a slack bot that pings my team every morning to post their standup and then collects the answers in one thread?

**Spec:**
```
Type:       Slack bot (integration service)
Auth:       Slack OAuth 2.0 app install per workspace
Data model: Workspace(id, slack_team_id, bot_token, channel_id, standup_time, timezone)
            Member(id, workspace_id -> Workspace, slack_user_id, active)
            StandupAnswer(id, member_id -> Member, date, yesterday, today, blockers)
Features:   - Send each team member a DM with the standup questions at a set time
            - Collect answers through a Slack modal form
            - Post all answers as replies in one daily thread in the team channel
            - Remind members who have not answered after 1 hour
            - Configure time, days and channel with a /standup slash command
API:        REST
            POST /slack/events
            POST /slack/interactions
            POST /slack/commands
            GET  /slack/oauth/callback
Storage:    PostgreSQL
Tech stack: Node.js, Slack Bolt for JavaScript, node-cron, PostgreSQL
```

---

## Example 313

**Intent:**
when someone pushes to our github repo or opens a PR i want a message in our discord channel

**Spec:**
```
Type:       Webhook receiver (integration service)
Data model: RepoMapping(id, github_repo, discord_webhook_url, events)
Features:   - Receive GitHub webhooks for push, pull_request and release events
            - Verify the X-Hub-Signature-256 HMAC signature
            - Format each event as a Discord embed with author, branch and link
            - Forward the message to the Discord channel webhook mapped to the repo
            - Ignore events that are not enabled for the repo
API:        REST
            POST /webhooks/github
            GET  /health
Storage:    SQLite
Tech stack: Python, Flask, requests
```

---

## Example 314

**Intent:**
I need an image upload service for our app: users upload photos, we store them in S3, generate thumbnails in a few sizes and return CDN URLs. Files over 10 MB or non-image types should be rejected.

**Spec:**
```
Type:       File upload and storage service
Auth:       JWT issued by the main app (verified with a shared public key)
Data model: Image(id, owner_id, original_key, content_type, size_bytes, width, height, created_at)
            Thumbnail(id, image_id -> Image, size_label, key, width, height)
Features:   - Accept multipart uploads up to 10 MB
            - Reject files whose magic bytes are not JPEG, PNG or WebP
            - Store originals in S3 under a random key
            - Generate 150px, 600px and 1200px thumbnails in a background worker
            - Return CloudFront URLs for the original and each thumbnail
            - Delete an image and all its thumbnails
API:        REST
            POST /images
            GET  /images/{id}
            DELETE /images/{id}
Storage:    Amazon S3 (files), PostgreSQL (metadata)
Tech stack: Python, FastAPI, boto3, Pillow, Celery, Amazon CloudFront
```

---

## Example 315

**Intent:**
build me an auth service with nestjs: signup, login, refresh tokens, email verification

**Spec:**
```
Type:       Authentication service (microservice)
Auth:       Email + password (argon2 hashing), JWT access tokens (15 min) + rotating refresh tokens (30 days)
Data model: User(id, email, password_hash, email_verified, created_at)
            RefreshToken(id, user_id -> User, token_hash, expires_at, revoked_at)
            EmailVerification(id, user_id -> User, token_hash, expires_at)
Features:   - Register a user and send a verification email
            - Verify the email address from a one-time link
            - Log in and return an access token and refresh token
            - Rotate refresh tokens and revoke the whole chain on reuse
            - Log out by revoking the current refresh token
            - Expose a JWKS endpoint so other services can verify tokens
API:        REST
            POST /auth/signup
            POST /auth/verify-email
            POST /auth/login
            POST /auth/refresh
            POST /auth/logout
            GET  /.well-known/jwks.json
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Passport, TypeORM, Nodemailer
```

---

## Example 316

**Intent:**
email sending microservice other services can call

**Spec:**
```
Type:       Notification microservice (email)
Auth:       Service-to-service API keys
Data model: Template(id, name, subject, html_body, text_body)
            EmailJob(id, template_id -> Template, to_address, variables_json, status, attempts, sent_at)
Features:   - Accept send requests and put them on a queue
            - Render templates with variables using Handlebars
            - Send emails through Amazon SES
            - Retry failed sends with exponential backoff up to 5 times
            - Track bounces and complaints from SES notifications
API:        REST
            POST /emails
            GET  /emails/{id}
            POST /templates
            PUT  /templates/{id}
            POST /webhooks/ses
Storage:    PostgreSQL (templates, jobs), Redis (queue)
Tech stack: Node.js, Fastify, BullMQ, AWS SDK (SES), Handlebars
```

---

## Example 317

**Intent:**
a graphql api for a bookstore with books, authors and reviews

**Spec:**
```
Type:       GraphQL API service
Auth:       JWT login; only admins can add or edit books
Data model: Author(id, name, bio)
            Book(id, title, isbn, price, published_at, author_id -> Author)
            User(id, email, password_hash, role)
            Review(id, book_id -> Book, user_id -> User, rating, text, created_at)
Features:   - Query books with filters for author, price range and title text
            - Paginate lists with cursor-based pagination
            - Add, edit and delete books and authors (admin only)
            - Let logged-in users post one review per book
            - Batch author lookups with DataLoader to avoid N+1 queries
API:        GraphQL
            query books
            query book
            query authors
            mutation createBook
            mutation updateBook
            mutation addReview
Storage:    PostgreSQL
Tech stack: TypeScript, Apollo Server, Prisma, DataLoader
```

---

## Example 318

**Intent:**
hey, I want a chat server where people can join rooms and send messages in real time, and see the old messages when they come back

**Spec:**
```
Type:       Real-time WebSocket server
Auth:       JWT login (email + password)
Data model: User(id, username, password_hash)
            Room(id, name, created_by -> User, created_at)
            Message(id, room_id -> Room, user_id -> User, text, created_at)
Features:   - Join and leave chat rooms over a WebSocket connection
            - Broadcast new messages to everyone in the room
            - Load the last 50 messages when joining and page back through older ones
            - Show who is online in each room
            - Scale across server instances with Redis pub/sub
API:        REST + WebSocket
            POST /login
            GET  /rooms
            POST /rooms
            GET  /rooms/{id}/messages?before={id}
            WS   /ws?token={jwt}
Storage:    PostgreSQL (messages), Redis (pub/sub, presence)
Tech stack: Node.js, Socket.IO, Express, Redis adapter
```

---

## Example 319

**Intent:**
i do personal training and want clients to book sessions that show up in my google calender automaticaly

**Spec:**
```
Type:       Booking API service (Google Calendar integration)
Auth:       Google OAuth 2.0 for the trainer; clients book with name and email only
Data model: Trainer(id, email, google_refresh_token, calendar_id, working_hours_json)
            Booking(id, trainer_id -> Trainer, client_name, client_email, starts_at, ends_at, google_event_id)
Features:   - Read free/busy times from the trainer's Google Calendar
            - Return available 60-minute slots inside working hours
            - Create a Google Calendar event with the client as an attendee
            - Cancel a booking and delete the matching calendar event
            - Send a confirmation email to the client
API:        REST
            GET  /availability?date={date}
            POST /bookings
            DELETE /bookings/{id}
            GET  /oauth/google/callback
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Google Calendar API, google-auth, SendGrid
```

---

## Example 320

**Intent:**
Our online shop has around 200k products and the SQL LIKE search is slow and bad. We need a search backend with typo tolerance, filters for brand, price and category, and autocomplete as the user types.

**Spec:**
```
Type:       Search service (microservice)
Data model: ProductDocument(id, name, description, brand, category, price, in_stock, popularity)
Features:   - Index products from the main database and update the index on product changes
            - Search with full-text matching and typo tolerance
            - Filter by brand, category, price range and stock status
            - Return facet counts for each filter
            - Suggest completions as the user types
            - Boost results by popularity
API:        REST
            GET  /search?q={text}&brand={b}&category={c}&min_price={p}&max_price={p}
            GET  /autocomplete?q={prefix}
            POST /index/reindex
Storage:    Elasticsearch
Tech stack: Java, Spring Boot, Elasticsearch Java client, Kafka (product change events)
```

---

## Example 321

**Intent:**
service that makes pdf invoices from order data

**Spec:**
```
Type:       Document generation service
Auth:       API key per calling service
Data model: Invoice(id, order_id, number, customer_json, lines_json, total, currency, pdf_key, created_at)
Features:   - Generate a PDF invoice from order and customer data
            - Assign sequential invoice numbers per year
            - Render the invoice from an HTML template with the company logo
            - Store the PDF and return a time-limited download link
            - Regenerate an invoice without changing its number
API:        REST
            POST /invoices
            GET  /invoices/{id}
            GET  /invoices/{id}/pdf
Storage:    PostgreSQL (invoice records), Amazon S3 (PDF files)
Tech stack: Python, Flask, WeasyPrint, Jinja2, boto3
```

---

## Example 322

**Intent:**
i want a api that give currency exchange rates, cached, and convert amounts between currencies

**Spec:**
```
Type:       REST API service
Auth:       API key (X-API-Key header)
Data model: Rate(base, quote, rate, fetched_at)
            ApiClient(id, name, api_key_hash, daily_limit)
Features:   - Fetch exchange rates from an upstream provider every hour
            - Return the latest rates for a base currency
            - Convert an amount from one currency to another
            - Return historical rates for a given date
            - Limit each client to its daily request quota
API:        REST
            GET  /rates/latest?base={code}
            GET  /rates/{date}?base={code}
            GET  /convert?from={code}&to={code}&amount={n}
Storage:    Redis (latest rates cache), PostgreSQL (history, clients)
Tech stack: Go, Echo, Open Exchange Rates API, go-redis
```

---

## Example 323

**Intent:**
feature flags service so we can turn features on for some users only

**Spec:**
```
Type:       Feature flag service
Auth:       Admin login (OAuth 2.0 via Google Workspace); SDK keys for client apps
Data model: Project(id, name, sdk_key_hash)
            Flag(id, project_id -> Project, key, enabled, rollout_percent)
            Rule(id, flag_id -> Flag, attribute, operator, value)
            AuditEntry(id, flag_id -> Flag, changed_by, change_json, changed_at)
Features:   - Create flags and turn them on or off per project
            - Roll out a flag to a percentage of users with stable hashing
            - Target users by attributes like country, plan or email domain
            - Evaluate all flags for a user in one call
            - Push flag changes to connected SDKs over server-sent events
            - Record every flag change in an audit log
API:        REST + SSE
            GET  /flags
            POST /flags
            PATCH /flags/{key}
            POST /evaluate
            GET  /stream
Storage:    PostgreSQL, Redis (evaluation cache)
Tech stack: Go, chi router, PostgreSQL, Redis
```

---

## Example 324

**Intent:**
I want a service that sends a 6 digit code by SMS to verify phone number when user sign up, please.

**Spec:**
```
Type:       Verification service (OTP)
Data model: OtpRequest(id, phone, code_hash, attempts, expires_at, verified_at)
Features:   - Generate a random 6-digit code and send it by SMS
            - Expire codes after 5 minutes
            - Allow at most 5 wrong attempts per code
            - Limit to 3 code requests per phone number per hour
            - Return a signed verification token after a correct code
API:        REST
            POST /otp/send
            POST /otp/verify
Storage:    Redis (codes with TTL, rate limits)
Tech stack: Node.js, Express, Twilio Verify API, ioredis
```

---

## Example 325

**Intent:**
we let users upload videos and need a worker that converts them to 720p and 1080p HLS and makes a thumbnail, then tells the main app when its done

**Spec:**
```
Type:       Background job worker (video processing)
Data model: TranscodeJob(id, video_id, source_key, status, progress, error, created_at, finished_at)
            Rendition(id, job_id -> TranscodeJob, resolution, playlist_key, bitrate)
Features:   - Pick up transcode jobs from a queue
            - Download the source video from S3
            - Transcode to 720p and 1080p HLS with FFmpeg
            - Extract a thumbnail at the 3-second mark
            - Upload outputs to S3 and update job progress
            - Call the main app's webhook when the job succeeds or fails
API:        REST
            POST /jobs
            GET  /jobs/{id}
Storage:    Amazon S3 (videos), PostgreSQL (jobs), Amazon SQS (queue)
Tech stack: Python, FFmpeg, boto3, FastAPI (job API)
```

---

## Example 326

**Intent:**
We are building a platform where customers register webhook URLs and we must send them events reliably. Deliveries should be signed, retried with backoff when they fail, and customers should be able to see the delivery history and replay failed events.

**Spec:**
```
Type:       Webhook delivery service
Auth:       Customer API keys
Data model: Endpoint(id, customer_id, url, secret, event_types, active)
            Event(id, customer_id, type, payload_json, created_at)
            Delivery(id, event_id -> Event, endpoint_id -> Endpoint, status, attempt, response_code, next_attempt_at)
Features:   - Register, update and disable webhook endpoints
            - Sign each payload with an HMAC-SHA256 header using the endpoint secret
            - Retry failed deliveries with exponential backoff for up to 24 hours
            - Disable endpoints that fail continuously for 3 days
            - Show delivery attempts with status codes and response times
            - Replay a single event or all failed events for an endpoint
API:        REST
            POST /endpoints
            PATCH /endpoints/{id}
            POST /events
            GET  /endpoints/{id}/deliveries
            POST /deliveries/{id}/replay
Storage:    PostgreSQL, Redis (delivery queue)
Tech stack: Go, River (Postgres job queue), net/http
```

---

## Example 327

**Intent:**
public api of random quotes with rate limits

**Spec:**
```
Type:       Public REST API
Auth:       Optional API key; anonymous requests get a lower limit
Data model: Quote(id, text, author, tags)
            ApiKey(id, owner_email, key_hash, tier)
Features:   - Return a random quote, optionally filtered by tag or author
            - Search quotes by text
            - Limit anonymous clients to 60 requests per hour by IP
            - Limit keyed clients to 1000 requests per hour
            - Return X-RateLimit-Remaining and Retry-After headers
API:        REST
            GET  /quotes/random?tag={tag}
            GET  /quotes?author={name}&q={text}
            GET  /quotes/{id}
            POST /keys
Storage:    PostgreSQL, Redis (sliding window rate limits)
Tech stack: Python, FastAPI, slowapi, SQLAlchemy
```

---

## Example 328

**Intent:**
inventory microservice that keeps stock counts and tells other services when stuff runs out

**Spec:**
```
Type:       Microservice (inventory)
Auth:       Internal service tokens (mTLS between services)
Data model: Warehouse(id, name, location)
            StockItem(id, sku, warehouse_id -> Warehouse, quantity, reserved, reorder_level)
            StockMovement(id, stock_item_id -> StockItem, change, reason, order_id, created_at)
Features:   - Reserve stock when an order is placed and release it on cancel
            - Decrease stock when an order ships
            - Record every stock change as a movement
            - Publish a low-stock event when quantity drops below the reorder level
            - Consume order events from the message broker
API:        REST
            GET  /stock/{sku}
            POST /stock/reserve
            POST /stock/release
            POST /stock/adjust
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Spring Data JPA, Apache Kafka
```

---

## Example 329

**Intent:**
every new shopify order should be added as a row in a google sheet

**Spec:**
```
Type:       Webhook receiver (integration service)
Data model: SyncedOrder(shopify_order_id, sheet_row, synced_at)
Features:   - Receive Shopify orders/create webhooks
            - Verify the X-Shopify-Hmac-Sha256 signature
            - Append order number, customer, items, total and date as a new sheet row
            - Skip orders that were already synced
            - Retry Google Sheets API calls when rate limited
API:        REST
            POST /webhooks/shopify/orders-create
Storage:    SQLite (synced order IDs)
Tech stack: Python, Flask, gspread, Google service account
```

---

## Example 330

**Intent:**
push notifications backend for our ios and android apps

**Spec:**
```
Type:       Notification service (push)
Auth:       Server-to-server API key; device registration with the app's user JWT
Data model: Device(id, user_id, platform, token, last_seen_at)
            Notification(id, user_id, title, body, data_json, sent_at)
Features:   - Register and unregister device tokens per user
            - Send a push to one user, a list of users or a topic
            - Deliver through Firebase Cloud Messaging for Android and iOS
            - Remove tokens that FCM reports as invalid
            - Schedule notifications for a later time
API:        REST
            POST /devices
            DELETE /devices/{token}
            POST /notifications
            GET  /notifications?user_id={id}
Storage:    PostgreSQL, Redis (scheduled queue)
Tech stack: Node.js, NestJS, firebase-admin SDK, BullMQ
```

---

## Example 331

**Intent:**
api to find cafes and shops near a location

**Spec:**
```
Type:       REST API service (geolocation)
Auth:       API key
Data model: Place(id, name, category, address, location_point, rating, opening_hours_json)
Features:   - Find places within a radius of a latitude and longitude
            - Sort results by distance or rating
            - Filter by category and open-now
            - Return places inside a map bounding box
            - Import places in bulk from a CSV file
API:        REST
            GET  /places/nearby?lat={lat}&lng={lng}&radius={m}&category={c}
            GET  /places/bbox?sw={lat,lng}&ne={lat,lng}
            GET  /places/{id}
            POST /places/import
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django REST Framework, GeoDjango
```

---

## Example 332

**Intent:**
so we have a B2B SaaS and every customer company needs their own isolated data but share the same API, how would I set that up

**Spec:**
```
Type:       Multi-tenant REST API
Auth:       User login with JWT containing tenant_id; per-tenant API keys for integrations
Data model: Tenant(id, name, subdomain, plan)
            User(id, tenant_id -> Tenant, email, password_hash, role)
            ApiKey(id, tenant_id -> Tenant, key_hash, scopes, last_used_at)
            Project(id, tenant_id -> Tenant, name, created_at)
Features:   - Resolve the tenant from the subdomain or token on every request
            - Enforce tenant isolation with PostgreSQL row-level security
            - Let tenant admins invite users and assign roles
            - Create and revoke scoped API keys per tenant
            - Apply rate limits based on the tenant's plan
API:        REST
            POST /auth/login
            POST /users/invite
            GET  /projects
            POST /projects
            POST /api-keys
            DELETE /api-keys/{id}
Storage:    PostgreSQL (shared schema with row-level security)
Tech stack: TypeScript, NestJS, Prisma, PostgreSQL
```

---

## Example 333

**Intent:**
headless blog backend using django rest framework, our frontend is nextjs

**Spec:**
```
Type:       Headless CMS API
Auth:       JWT for editors (djangorestframework-simplejwt); public read access
Data model: Author(id, user_id, name, bio, avatar_url)
            Post(id, author_id -> Author, title, slug, body_markdown, status, published_at)
            Tag(id, name, slug)
            PostTag(post_id -> Post, tag_id -> Tag)
Features:   - Create, edit and publish posts as drafts or scheduled posts
            - List published posts with pagination and tag filters
            - Fetch a post by slug for the frontend
            - Upload images for posts to object storage
            - Trigger a Next.js revalidation webhook when a post is published
API:        REST
            GET  /api/posts?tag={slug}&page={n}
            GET  /api/posts/{slug}
            POST /api/posts
            PATCH /api/posts/{id}
            POST /api/uploads
Storage:    PostgreSQL, Amazon S3 (images)
Tech stack: Python, Django REST Framework, djangorestframework-simplejwt, django-storages
```

---

## Example 334

**Intent:**
api that makes a podcast rss feed from episodes we upload

**Spec:**
```
Type:       REST API service (podcast hosting)
Auth:       Admin API key
Data model: Show(id, title, description, author, cover_url, category)
            Episode(id, show_id -> Show, title, description, audio_key, duration_seconds, size_bytes, published_at)
Features:   - Upload MP3 episodes and read their duration
            - Generate an RSS 2.0 feed with iTunes podcast tags
            - Serve audio files with HTTP range requests
            - Schedule episodes to publish at a future time
            - Count downloads per episode
API:        REST
            POST /shows
            POST /shows/{id}/episodes
            GET  /shows/{id}/feed.xml
            GET  /episodes/{id}/audio
Storage:    PostgreSQL, Amazon S3 (audio)
Tech stack: Node.js, Express, music-metadata, podcast (RSS builder)
```

---

## Example 335

**Intent:**
upload a meeting recording and get the transcript back when its ready

**Spec:**
```
Type:       Background job worker (speech-to-text)
Auth:       API key
Data model: TranscriptionJob(id, audio_key, language, status, error, created_at, finished_at)
            Segment(id, job_id -> TranscriptionJob, start_seconds, end_seconds, speaker, text)
Features:   - Accept audio and video uploads up to 2 GB
            - Extract audio with FFmpeg and split long files into chunks
            - Transcribe each chunk with Whisper on a GPU worker
            - Return timestamped segments and full text
            - Export transcripts as TXT, SRT and VTT
            - Call a callback URL when the job finishes
API:        REST
            POST /transcriptions
            GET  /transcriptions/{id}
            GET  /transcriptions/{id}/export?format={txt|srt|vtt}
Storage:    Amazon S3 (audio), PostgreSQL (jobs, segments), Redis (queue)
Tech stack: Python, FastAPI, faster-whisper, FFmpeg, RQ
```

---

## Example 336

**Intent:**
receipt scanning api, photo in, store name total and date out

**Spec:**
```
Type:       REST API service (OCR)
Auth:       API key
Data model: Receipt(id, image_key, merchant, total, currency, purchase_date, raw_text, created_at)
            ReceiptLine(id, receipt_id -> Receipt, description, quantity, amount)
Features:   - Accept a receipt photo as JPEG, PNG or PDF
            - Straighten and clean the image before OCR
            - Extract merchant name, date, total and line items
            - Return a confidence score for each field
            - Store results so they can be fetched again later
API:        REST
            POST /receipts
            GET  /receipts/{id}
Storage:    PostgreSQL, Amazon S3 (images)
Tech stack: Python, Flask, AWS Textract (AnalyzeExpense), OpenCV
```

---

## Example 337

**Intent:**
barcode lookup api

**Spec:**
```
Type:       REST API service (product lookup)
Auth:       API key
Data model: Product(barcode, name, brand, category, image_url, nutrition_json, source, updated_at)
Features:   - Look up a product by EAN-13 or UPC barcode
            - Validate the barcode check digit
            - Fall back to Open Food Facts when the product is not stored locally
            - Save fetched products to the local database
            - Let users submit missing products for review
API:        REST
            GET  /products/{barcode}
            POST /products
Storage:    MongoDB
Tech stack: Node.js, Express, Mongoose, Open Food Facts API
```

---

## Example 338

**Intent:**
library book lending api in rails, members borrow books, due dates, fines if late

**Spec:**
```
Type:       REST API service (library)
Auth:       Devise with JWT (devise-jwt); roles Member and Librarian
Data model: Member(id, email, password_hash, name, role)
            Book(id, isbn, title, author, total_copies)
            Loan(id, book_id -> Book, member_id -> Member, borrowed_at, due_at, returned_at)
            Fine(id, loan_id -> Loan, amount, paid_at)
Features:   - Check out a book when a copy is available
            - Set a due date 14 days after borrowing and allow one renewal
            - Calculate late fines per day on return
            - Put members on a waitlist when no copies are free
            - Email reminders 2 days before the due date
API:        REST
            GET  /books?q={text}
            POST /loans
            POST /loans/{id}/renew
            POST /loans/{id}/return
            GET  /members/me/loans
Storage:    PostgreSQL
Tech stack: Ruby, Ruby on Rails (API mode), devise-jwt, Sidekiq
```

---

## Example 339

**Intent:**
gym class booking backend, classes have limited spots and waitlist

**Spec:**
```
Type:       REST API service (class booking)
Auth:       JWT login for members and trainers
Data model: Member(id, email, password_hash, membership_ends_at)
            GymClass(id, name, trainer, starts_at, capacity)
            ClassBooking(id, class_id -> GymClass, member_id -> Member, status, created_at)
Features:   - Book a spot when the class is not full
            - Add members to a waitlist when the class is full
            - Move the first waitlisted member up when someone cancels
            - Block cancellations less than 2 hours before class
            - Block bookings for members with an expired membership
API:        REST
            GET  /classes?date={date}
            POST /classes/{id}/bookings
            DELETE /bookings/{id}
            GET  /members/me/bookings
Storage:    MySQL
Tech stack: PHP, Symfony, Doctrine ORM, LexikJWTAuthenticationBundle
```

---

## Example 340

**Intent:**
parking lot sensors tell if a spot is free, i want an api that apps can use to find free spots

**Spec:**
```
Type:       REST + WebSocket API service (parking)
Auth:       Sensor gateways use API keys; app clients use public API keys
Data model: ParkingLot(id, name, address, lat, lng, total_spots)
            Spot(id, lot_id -> ParkingLot, label, type, occupied, updated_at)
Features:   - Receive occupancy updates from sensor gateways
            - Return free spot counts per lot
            - Find the nearest lots with free spots
            - Push changes to connected apps in real time
            - Mark sensors offline when no update arrives for 10 minutes
API:        REST + WebSocket
            POST /sensors/updates
            GET  /lots?lat={lat}&lng={lng}
            GET  /lots/{id}/spots
            WS   /lots/{id}/live
Storage:    PostgreSQL, Redis (live occupancy)
Tech stack: C#, ASP.NET Core, SignalR, Entity Framework Core
```

---

## Example 341

**Intent:**
Car rental company needs a booking backend. Customers search cars by location and dates, see price, book and pay a deposit. Staff should mark cars as picked up and returned and record damage.

**Spec:**
```
Type:       REST API service (car rental)
Auth:       JWT login with roles Customer and Staff
Data model: Branch(id, name, city, address)
            Car(id, branch_id -> Branch, make, model, category, daily_rate, status)
            Rental(id, car_id -> Car, customer_id, starts_at, ends_at, total_price, deposit_payment_id, status)
            DamageReport(id, rental_id -> Rental, description, photo_keys, reported_at)
Features:   - Search available cars by branch, dates and category
            - Calculate the total price with weekend and long-rental discounts
            - Take a deposit with Stripe when booking
            - Let staff check cars out and in with mileage and fuel level
            - Record damage with photos on return
API:        REST
            GET  /cars/available?branch={id}&from={date}&to={date}
            POST /rentals
            POST /rentals/{id}/pickup
            POST /rentals/{id}/return
            POST /rentals/{id}/damage
Storage:    PostgreSQL, Amazon S3 (damage photos)
Tech stack: Java, Spring Boot, Spring Data JPA, Stripe Java SDK
```

---

## Example 342

**Intent:**
real estate listings search api with filters like price, bedrooms, area and map search

**Spec:**
```
Type:       Search API service (real estate)
Auth:       Agent login (JWT) for creating listings; public search
Data model: Agent(id, email, password_hash, agency)
            Listing(id, agent_id -> Agent, title, price, bedrooms, bathrooms, area_sqm, type, location_point, status)
            ListingPhoto(id, listing_id -> Listing, url, position)
Features:   - Search listings by price, bedrooms, area, type and keywords
            - Search inside a map polygon or radius
            - Sort by price, newest or distance
            - Let agents create, edit and mark listings as sold
            - Save searches and email users new matching listings daily
API:        REST
            GET  /listings?min_price={p}&max_price={p}&bedrooms={n}&bbox={coords}
            GET  /listings/{id}
            POST /listings
            PATCH /listings/{id}
            POST /saved-searches
Storage:    PostgreSQL with PostGIS
Tech stack: Python, FastAPI, GeoAlchemy2, SQLAlchemy
```

---

## Example 343

**Intent:**
job board api, companies post jobs and people apply with cv

**Spec:**
```
Type:       REST API service (job board)
Auth:       JWT login with roles Employer and Candidate
Data model: Company(id, name, website, logo_url)
            Job(id, company_id -> Company, title, location, remote, salary_min, salary_max, description, status)
            Candidate(id, email, password_hash, name)
            Application(id, job_id -> Job, candidate_id -> Candidate, cv_key, cover_letter, status, applied_at)
Features:   - Post, edit and close job listings
            - Search jobs by keyword, location, remote and salary
            - Apply to a job with an uploaded CV (PDF)
            - Let employers move applications through stages
            - Email candidates when their application status changes
API:        REST
            GET  /jobs?q={text}&location={loc}&remote={bool}
            POST /jobs
            POST /jobs/{id}/applications
            GET  /jobs/{id}/applications
            PATCH /applications/{id}
Storage:    PostgreSQL, Amazon S3 (CVs)
Tech stack: TypeScript, Express, Prisma, Multer, AWS SDK v3
```

---

## Example 344

**Intent:**
pet adoption api with graphql, shelters list animals and people send adoption requests

**Spec:**
```
Type:       GraphQL API service
Auth:       JWT login with roles Shelter and Adopter
Data model: Shelter(id, name, city, email)
            Pet(id, shelter_id -> Shelter, name, species, breed, age_months, description, status)
            AdoptionRequest(id, pet_id -> Pet, adopter_id, message, status, created_at)
Features:   - Query pets with filters for species, age and city
            - Let shelters add, update and remove pets
            - Let adopters send an adoption request for a pet
            - Let shelters approve or reject requests
            - Notify adopters by email on decision
API:        GraphQL
            query pets
            query pet
            mutation addPet
            mutation updatePet
            mutation requestAdoption
            mutation decideAdoption
Storage:    PostgreSQL
Tech stack: Python, Strawberry GraphQL, FastAPI, SQLAlchemy
```

---

## Example 345

**Intent:**
connect to strava so when users finish a run it's imported into our training app automatically

**Spec:**
```
Type:       Integration service (Strava)
Auth:       Strava OAuth 2.0 per user, refresh tokens stored encrypted
Data model: StravaConnection(id, user_id, athlete_id, access_token_enc, refresh_token_enc, expires_at)
            Activity(id, user_id, strava_activity_id, type, distance_m, moving_time_s, started_at, polyline)
Features:   - Connect a user's Strava account with OAuth
            - Subscribe to Strava webhook events for new activities
            - Fetch activity details and save runs to the training app
            - Refresh access tokens before they expire
            - Remove data when the user deauthorizes the app
API:        REST
            GET  /strava/connect
            GET  /strava/callback
            GET  /webhooks/strava
            POST /webhooks/strava
Storage:    PostgreSQL
Tech stack: Python, Flask, Strava API v3, cryptography (Fernet)
```

---

## Example 346

**Intent:**
make spotify playlist from a mood or genre user type

**Spec:**
```
Type:       Integration service (Spotify)
Auth:       Spotify OAuth 2.0 (Authorization Code with PKCE)
Data model: User(id, spotify_user_id, access_token_enc, refresh_token_enc)
            GeneratedPlaylist(id, user_id -> User, prompt, spotify_playlist_id, created_at)
Features:   - Map a mood or genre text to seed genres and audio features
            - Pick tracks from the user's top artists and Spotify search
            - Create a playlist in the user's Spotify account
            - Let the user regenerate or remove tracks
            - Keep a history of generated playlists
API:        REST
            GET  /auth/spotify
            GET  /auth/spotify/callback
            POST /playlists
            GET  /playlists
Storage:    MongoDB
Tech stack: Node.js, Express, spotify-web-api-node, Mongoose
```

---

## Example 347

**Intent:**
nightly backup of our database dumps to google drive, keep last 30

**Spec:**
```
Type:       Background job worker (backups)
Auth:       Google service account with access to one Drive folder
Data model: BackupRecord(id, filename, drive_file_id, size_bytes, checksum, created_at)
Features:   - Run pg_dump every night at 02:00
            - Compress and encrypt the dump with GPG
            - Upload the file to a Google Drive folder with resumable upload
            - Delete backups older than the newest 30
            - Send a Slack message on success or failure
Storage:    Google Drive (backup files), SQLite (backup records)
Tech stack: Python, Google Drive API (google-api-python-client), APScheduler, gnupg
```

---

## Example 348

**Intent:**
file storage api that keeps old versions of a file so you can go back

**Spec:**
```
Type:       File storage service (versioned)
Auth:       JWT login; files are private to their owner unless shared
Data model: File(id, owner_id, path, current_version_id, deleted_at)
            FileVersion(id, file_id -> File, s3_key, size_bytes, sha256, created_at, created_by)
            Share(id, file_id -> File, user_id, permission)
Features:   - Upload a file and create a new version on every change
            - List all versions with size, date and author
            - Download or restore any earlier version
            - Skip storing a new version when the content hash is unchanged
            - Keep deleted files in a trash for 30 days
API:        REST
            PUT  /files/{path}
            GET  /files/{path}
            GET  /files/{id}/versions
            POST /files/{id}/versions/{versionId}/restore
            DELETE /files/{id}
Storage:    Amazon S3 (file contents), PostgreSQL (metadata)
Tech stack: Go, Gin, AWS SDK for Go v2, pgx
```

---

## Example 349

**Intent:**
let the browser upload straight to s3 with presigned urls instead of going through our server

**Spec:**
```
Type:       File upload service (presigned URLs)
Auth:       JWT (existing app users)
Data model: Upload(id, user_id, key, filename, content_type, size_bytes, status, created_at)
Features:   - Check file type and size before signing
            - Return a presigned PUT or POST URL valid for 10 minutes
            - Use multipart presigned URLs for files over 100 MB
            - Confirm the upload with an S3 event notification and mark it complete
            - Return presigned GET URLs for downloads
API:        REST
            POST /uploads
            POST /uploads/{id}/complete
            GET  /uploads/{id}/download-url
Storage:    Amazon S3, DynamoDB (upload records)
Tech stack: Node.js, AWS Lambda, API Gateway, AWS SDK v3
```

---

## Example 350

**Intent:**
online/offline and typing status for our chat app

**Spec:**
```
Type:       Real-time presence service
Auth:       JWT from the chat app, checked on connect
Features:   - Mark a user online on connect and offline after 30 seconds without a heartbeat
            - Broadcast presence changes to the user's contacts
            - Send typing started and stopped events to a conversation
            - Return the last-seen time for offline users
            - Support many connections per user across devices
API:        WebSocket + REST
            WS   /presence
            GET  /presence?user_ids={ids}
Storage:    Redis (presence keys with TTL, pub/sub)
Tech stack: Go, nhooyr/websocket, go-redis
```

---

## Example 351

**Intent:**
alert me on telegram when bitcoin or eth goes above or below a price i set

**Spec:**
```
Type:       Background worker (price alerts)
Data model: Alert(id, telegram_chat_id, symbol, direction, target_price, triggered_at, active)
Features:   - Add alerts with a Telegram command like /alert BTC above 70000
            - Check prices every 30 seconds from the CoinGecko API
            - Send a Telegram message when an alert's condition is met
            - Disable an alert after it fires once
            - List and delete alerts from the chat
API:        REST
            POST /telegram/webhook
Storage:    SQLite
Tech stack: Python, python-telegram-bot, httpx, APScheduler
```

---

## Example 352

**Intent:**
websocket server that relays live stock prices from a data provider to our trading frontend

**Spec:**
```
Type:       Real-time WebSocket server (market data)
Auth:       JWT on connect
Features:   - Keep one upstream connection to the market data provider
            - Let clients subscribe and unsubscribe to ticker symbols
            - Fan out price updates only to subscribed clients
            - Throttle updates to at most 4 per second per symbol
            - Reconnect to the provider with backoff and resubscribe
API:        WebSocket
            WS   /prices
Storage:    Redis (last price per symbol)
Tech stack: Rust, Tokio, tokio-tungstenite, Polygon.io WebSocket API
```

---

## Example 353

**Intent:**
I'm a freelancer and I keep forgetting to chase unpaid invoices, so I want something that emails clients a polite reminder 3 days before due, on the due date and every week after until it's marked paid.

**Spec:**
```
Type:       Scheduled notification service
Auth:       Single owner login (email + password)
Data model: Client(id, name, email)
            Invoice(id, client_id -> Client, number, amount, currency, due_date, paid_at, pdf_url)
            Reminder(id, invoice_id -> Invoice, kind, sent_at)
Features:   - Run a daily job that finds invoices needing a reminder
            - Send reminders 3 days before, on the due date and weekly when overdue
            - Use a different email template for each reminder type
            - Stop reminders when an invoice is marked paid
            - Never send the same reminder twice
API:        REST
            GET  /invoices
            POST /invoices
            POST /invoices/{id}/mark-paid
            GET  /invoices/{id}/reminders
Storage:    PostgreSQL
Tech stack: Node.js, Express, node-cron, SendGrid
```

---

## Example 354

**Intent:**
typeform answers should go to airtable automaticly

**Spec:**
```
Type:       Webhook receiver (integration service)
Data model: FieldMapping(id, typeform_form_id, typeform_field_ref, airtable_field_name)
            ProcessedResponse(typeform_response_id, airtable_record_id, processed_at)
Features:   - Receive Typeform form_response webhooks
            - Verify the Typeform-Signature HMAC header
            - Map answers to Airtable fields using saved mappings
            - Create a record in the Airtable base
            - Skip responses that were already processed
API:        REST
            POST /webhooks/typeform
Storage:    SQLite
Tech stack: Python, FastAPI, pyairtable
```

---

## Example 355

**Intent:**
survey api, create surveys, collect responses, get result stats

**Spec:**
```
Type:       REST API service (surveys)
Auth:       JWT for survey creators; respondents anonymous with a one-response cookie
Data model: Survey(id, owner_id, title, status, created_at)
            Question(id, survey_id -> Survey, text, type, options_json, required, position)
            Response(id, survey_id -> Survey, submitted_at)
            Answer(id, response_id -> Response, question_id -> Question, value)
Features:   - Create surveys with single choice, multiple choice, rating and text questions
            - Validate required questions on submit
            - Count answers per option and average ratings
            - Export raw responses as CSV
            - Close a survey after a date or response limit
API:        REST
            POST /surveys
            GET  /surveys/{id}
            POST /surveys/{id}/responses
            GET  /surveys/{id}/results
            GET  /surveys/{id}/export.csv
Storage:    PostgreSQL
Tech stack: Python, Django REST Framework, PostgreSQL
```

---

## Example 356

**Intent:**
dictionary api, word meanings and synonyms, free but rate limited

**Spec:**
```
Type:       Public REST API
Data model: Word(id, lemma, language, part_of_speech, phonetic)
            Definition(id, word_id -> Word, text, example)
            Synonym(word_id -> Word, synonym_id -> Word)
Features:   - Return definitions, examples and phonetics for a word
            - Return synonyms and antonyms
            - Suggest close words for misspellings
            - Limit each IP to 100 requests per 15 minutes
            - Cache popular words at the CDN
API:        REST
            GET  /words/{word}
            GET  /words/{word}/synonyms
            GET  /suggest?q={prefix}
Storage:    PostgreSQL (pg_trgm for fuzzy match)
Tech stack: Node.js, Express, express-rate-limit, Cloudflare CDN
```

---

## Example 357

**Intent:**
live auction backend where bids show up instantly for everyone watching

**Spec:**
```
Type:       Real-time WebSocket server (auctions)
Auth:       JWT login (email + password)
Data model: User(id, email, password_hash, display_name)
            Auction(id, seller_id -> User, title, starting_price, min_increment, ends_at, status)
            Bid(id, auction_id -> Auction, bidder_id -> User, amount, created_at)
Features:   - Place a bid and reject it if it is below the current price plus the increment
            - Lock the auction row while checking a bid to prevent race conditions
            - Broadcast new highest bids to all watchers of the auction
            - Extend the end time by 2 minutes when a bid arrives in the last minute
            - Close the auction at the end time and notify the winner
API:        REST + WebSocket
            POST /auctions
            GET  /auctions/{id}
            POST /auctions/{id}/bids
            WS   /auctions/{id}/live
Storage:    PostgreSQL, Redis (pub/sub between instances)
Tech stack: Elixir, Phoenix, Phoenix Channels, Ecto
```

---

## Example 358

**Intent:**
leaderboard api for my mobile game

**Spec:**
```
Type:       REST API service (game leaderboard)
Auth:       API key per game plus a signed player ID from the game client
Data model: Game(id, name, api_key_hash)
            Player(id, game_id -> Game, external_id, nickname)
            Score(id, player_id -> Player, board, value, submitted_at)
Features:   - Submit a score and keep only the player's best per board
            - Return the top 100 players for a board
            - Return a player's rank and the players just above and below
            - Support daily, weekly and all-time boards
            - Reject scores with invalid signatures to stop cheating
API:        REST
            POST /scores
            GET  /boards/{board}/top?period={daily|weekly|all}
            GET  /boards/{board}/players/{id}/rank
Storage:    Redis (sorted sets), PostgreSQL (score history)
Tech stack: Go, Fiber, go-redis
```

---

## Example 359

**Intent:**
forgot password flow for our api, send a reset link by email

**Spec:**
```
Type:       Authentication API (password reset)
Auth:       Existing email + password login (bcrypt)
Data model: User(id, email, password_hash, password_changed_at)
            PasswordResetToken(id, user_id -> User, token_hash, expires_at, used_at)
Features:   - Request a reset link by email and always return the same response
            - Store only a SHA-256 hash of the reset token
            - Expire reset links after 30 minutes and allow single use
            - Set a new password that meets the strength rules
            - Invalidate all existing sessions after a reset
            - Limit reset requests to 3 per email per hour
API:        REST
            POST /password/forgot
            POST /password/reset
Storage:    PostgreSQL
Tech stack: Ruby, Ruby on Rails (API mode), Action Mailer, bcrypt
```

---

## Example 360

**Intent:**
users upload big CSV files of contacts and it should import them in background and show progress

**Spec:**
```
Type:       Background job worker (CSV import)
Auth:       JWT (existing app users)
Data model: ImportJob(id, user_id, file_key, status, total_rows, processed_rows, failed_rows, created_at)
            ImportError(id, job_id -> ImportJob, row_number, message)
            Contact(id, user_id, name, email, phone, company)
Features:   - Upload a CSV file and create an import job
            - Map CSV columns to contact fields
            - Process rows in batches of 1000 in a background worker
            - Validate emails and phone numbers and record bad rows
            - Report progress and a downloadable error file
API:        REST
            POST /imports
            GET  /imports/{id}
            GET  /imports/{id}/errors.csv
Storage:    PostgreSQL, Amazon S3 (uploaded files), Redis (job queue)
Tech stack: Python, Django, Celery, pandas
```

---

## Example 361

**Intent:**
login with google and github for my app backend

**Spec:**
```
Type:       Authentication service (social login)
Auth:       OAuth 2.0 / OpenID Connect with Google and GitHub; app session via JWT
Data model: User(id, email, name, avatar_url, created_at)
            Identity(id, user_id -> User, provider, provider_user_id)
Features:   - Redirect to Google or GitHub with state and PKCE
            - Handle the callback and exchange the code for tokens
            - Create a user on first login or link to an existing one by verified email
            - Issue an app JWT in an HttpOnly cookie
            - Let a user link or unlink providers from their account
API:        REST
            GET  /auth/{provider}/start
            GET  /auth/{provider}/callback
            GET  /me
            POST /logout
Storage:    PostgreSQL
Tech stack: Node.js, Express, Passport (passport-google-oauth20, passport-github2)
```

---

## Example 362

**Intent:**
Hello, I am running small charity and want to take donations by PayPal on our website, also need list of donors for thank-you mails.

**Spec:**
```
Type:       REST API service (payments)
Auth:       Admin login (email + password) for the donor list
Data model: Donation(id, paypal_order_id, donor_name, donor_email, amount, currency, status, created_at)
            Admin(id, email, password_hash)
Features:   - Create a PayPal order for a chosen donation amount
            - Capture the payment after the donor approves it
            - Confirm payments with PayPal webhooks
            - Send a thank-you email after a successful donation
            - List and export donors as CSV for admins
API:        REST
            POST /donations
            POST /donations/{id}/capture
            POST /webhooks/paypal
            GET  /admin/donations
            GET  /admin/donations/export.csv
Storage:    MySQL
Tech stack: PHP, Laravel, PayPal Checkout REST API, Laravel Mail
```

---

## Example 363

**Intent:**
need razorpay payment for my online course website, after payment student should get acess to course

**Spec:**
```
Type:       REST API service (payments)
Auth:       Student login with email + password (JWT)
Data model: Student(id, email, password_hash, name)
            Course(id, title, price_inr)
            Order(id, student_id -> Student, course_id -> Course, razorpay_order_id, status, amount)
            Enrollment(id, student_id -> Student, course_id -> Course, enrolled_at)
Features:   - Create a Razorpay order when a student clicks buy
            - Verify the payment signature after checkout
            - Enroll the student in the course after a verified payment
            - Handle payment.captured and refund webhooks
            - Block course content for students who are not enrolled
API:        REST
            POST /orders
            POST /orders/verify
            POST /webhooks/razorpay
            GET  /courses/{id}/content
Storage:    MongoDB
Tech stack: Node.js, Express, Razorpay Node SDK, Mongoose
```

---

## Example 364

**Intent:**
Build a ticket booking API for concerts where users choose specific seats. When someone selects seats they should be held for 10 minutes while they pay, and no two people can ever buy the same seat.

**Spec:**
```
Type:       REST API service (ticket booking)
Auth:       JWT login (email + password)
Data model: Event(id, name, venue, starts_at)
            Seat(id, event_id -> Event, section, row, number, price, status)
            Hold(id, user_id, event_id -> Event, seat_ids, expires_at)
            Booking(id, user_id, event_id -> Event, seat_ids, total, payment_id, created_at)
Features:   - Show the seat map with available, held and sold seats
            - Hold selected seats for 10 minutes using atomic Redis locks
            - Release held seats automatically when the hold expires
            - Confirm a booking only after a successful Stripe payment
            - Use a database unique constraint so a seat is never sold twice
            - Email tickets with a QR code after booking
API:        REST
            GET  /events/{id}/seats
            POST /events/{id}/holds
            DELETE /holds/{id}
            POST /holds/{id}/checkout
            GET  /bookings
Storage:    PostgreSQL, Redis (seat holds with TTL)
Tech stack: Java, Spring Boot, Spring Data JPA, Redisson, Stripe Java SDK
```

---

## Example 365

**Intent:**
audit log service

**Spec:**
```
Type:       Microservice (audit logging)
Auth:       Service API keys for writing; admin JWT for reading
Data model: AuditEvent(id, actor_id, actor_type, action, resource_type, resource_id, before_json, after_json, ip, occurred_at)
Features:   - Accept audit events from other services over HTTP and a message queue
            - Store events append-only with no update or delete
            - Search events by actor, resource, action and time range
            - Export search results as CSV
            - Delete events older than the retention period
API:        REST
            POST /events
            GET  /events?actor={id}&resource={type}:{id}&from={time}&to={time}
            GET  /events/export.csv
Storage:    PostgreSQL (partitioned by month)
Tech stack: Go, Gin, RabbitMQ, pgx
```

---

## Example 366

**Intent:**
something where i can register urls to be called on a cron schedule, like a hosted cron

**Spec:**
```
Type:       Job scheduler service
Auth:       User login (email + password) and API tokens
Data model: User(id, email, password_hash)
            CronJob(id, user_id -> User, name, url, method, headers_json, body, cron_expression, timezone, enabled)
            Run(id, job_id -> CronJob, started_at, status_code, duration_ms, response_snippet)
Features:   - Create jobs with a cron expression and timezone
            - Call the job's URL on schedule with the saved method, headers and body
            - Record each run with status code and duration
            - Email the user after 3 failed runs in a row
            - Pause, resume or trigger a job manually
API:        REST
            GET  /jobs
            POST /jobs
            PUT  /jobs/{id}
            POST /jobs/{id}/run
            GET  /jobs/{id}/runs
Storage:    PostgreSQL
Tech stack: Python, FastAPI, APScheduler, httpx
```

---

## Example 367

**Intent:**
a text to speech api, wrap some cloud tts and cache the audio so we dont pay twice for the same sentence

**Spec:**
```
Type:       REST API service (text-to-speech proxy)
Auth:       API key
Data model: AudioCache(hash, text, voice, format, s3_key, created_at)
            Usage(id, api_key_id, characters, created_at)
Features:   - Convert text to speech with a chosen voice and format (MP3 or OGG)
            - Hash text + voice + format and return cached audio when it exists
            - Store new audio files in S3
            - Track characters used per API key
            - Reject text longer than 5000 characters
API:        REST
            POST /speech
            GET  /voices
            GET  /usage
Storage:    Amazon S3 (audio), PostgreSQL (cache index, usage)
Tech stack: Python, FastAPI, Amazon Polly (boto3)
```

---

## Example 368

**Intent:**
api that takes a link and gives back title, description and preview image like slack does

**Spec:**
```
Type:       REST API service (link preview)
Auth:       API key
Data model: Preview(url_hash, url, title, description, image_url, site_name, fetched_at)
Features:   - Fetch the page and read Open Graph, Twitter Card and HTML meta tags
            - Fall back to the page title and first image when tags are missing
            - Block private IP ranges to prevent SSRF
            - Time out slow pages after 5 seconds
            - Cache previews for 24 hours
API:        REST
            GET  /preview?url={url}
Storage:    Redis (cache)
Tech stack: Node.js, Express, got, cheerio
```

---

## Example 369

**Intent:**
customers email support@ our domain and i want those emails turned into tickets automatically via mailgun

**Spec:**
```
Type:       Webhook receiver (inbound email)
Data model: Ticket(id, customer_email, subject, status, created_at)
            TicketMessage(id, ticket_id -> Ticket, from_address, body_text, attachments_json, received_at)
Features:   - Receive parsed inbound emails from Mailgun routes
            - Verify the Mailgun webhook signature
            - Create a new ticket or add to an existing one by the ticket ID in the subject
            - Save attachments to object storage
            - Send an auto-reply with the ticket number
API:        REST
            POST /webhooks/mailgun/inbound
            GET  /tickets
            GET  /tickets/{id}
Storage:    PostgreSQL, Amazon S3 (attachments)
Tech stack: Python, Flask, Mailgun API, boto3
```

---

## Example 370

**Intent:**
I want rest api for restaurant table reservations using spring boot and mysql

**Spec:**
```
Type:       REST API service (reservations)
Auth:       JWT for staff; guests reserve with name, phone and email
Data model: RestaurantTable(id, number, seats, area)
            Reservation(id, table_id -> RestaurantTable, guest_name, guest_phone, guest_email, party_size, starts_at, status)
            Staff(id, email, password_hash, role)
Features:   - Check free tables for a date, time and party size
            - Book the smallest free table that fits the party
            - Block double booking within a 2-hour seating window
            - Let staff confirm, cancel or mark reservations as no-show
            - Send a confirmation email to the guest
API:        REST
            GET  /availability?date={date}&time={time}&party={n}
            POST /reservations
            PATCH /reservations/{id}
            GET  /reservations?date={date}
Storage:    MySQL
Tech stack: Java, Spring Boot, Spring Data JPA, Spring Security, MySQL
```

---

## Example 371

**Intent:**
backend for clinic appointments in asp.net core, doctors have schedules, patients book slots

**Spec:**
```
Type:       REST API service (appointments)
Auth:       ASP.NET Core Identity with JWT; roles Patient, Doctor, Admin
Data model: Doctor(id, user_id, name, specialty)
            ScheduleSlot(id, doctor_id -> Doctor, day_of_week, start_time, end_time, slot_minutes)
            Patient(id, user_id, name, phone, date_of_birth)
            Appointment(id, doctor_id -> Doctor, patient_id -> Patient, starts_at, status, notes)
Features:   - Define weekly working hours and slot length per doctor
            - List free slots for a doctor on a given day
            - Book, reschedule and cancel appointments
            - Let doctors see their daily schedule and add notes
            - Send email reminders 24 hours before an appointment
API:        REST
            GET  /doctors?specialty={s}
            GET  /doctors/{id}/slots?date={date}
            POST /appointments
            PUT  /appointments/{id}
            DELETE /appointments/{id}
Storage:    SQL Server
Tech stack: C#, ASP.NET Core Web API, Entity Framework Core, Hangfire
```

---

## Example 372

**Intent:**
graphql movie reviews api with django

**Spec:**
```
Type:       GraphQL API service
Auth:       JWT login (django-graphql-jwt)
Data model: Movie(id, title, year, genre, director)
            User(id, username, password_hash)
            Review(id, movie_id -> Movie, user_id -> User, rating, text, created_at)
Features:   - Query movies with filters for genre and year
            - Return each movie's average rating and review count
            - Let logged-in users add, edit and delete their own reviews
            - Paginate reviews with Relay-style connections
            - Search movies by title
API:        GraphQL
            query movies
            query movie
            mutation tokenAuth
            mutation createReview
            mutation updateReview
            mutation deleteReview
Storage:    PostgreSQL
Tech stack: Python, Django, Graphene-Django, django-graphql-jwt
```

---

## Example 373

**Intent:**
like wetransfer but for my team, upload a file get a link that expires in a week

**Spec:**
```
Type:       File sharing service
Auth:       Team login (email + password); download links need no login
Data model: User(id, email, password_hash)
            SharedFile(id, owner_id -> User, filename, size_bytes, s3_key, token, password_hash, expires_at, download_count)
Features:   - Upload files up to 5 GB directly to S3 with presigned multipart URLs
            - Create a share link with a random token and 7-day expiry
            - Protect a link with an optional password
            - Count downloads and email the owner on the first download
            - Delete expired files with a daily cleanup job
API:        REST
            POST /files
            POST /files/{id}/complete
            GET  /s/{token}
            DELETE /files/{id}
Storage:    Amazon S3 (files), PostgreSQL (metadata)
Tech stack: TypeScript, Express, AWS SDK v3, node-cron
```

---

## Example 374

**Intent:**
we have temperature and humidity sensors in a warehouse sending data every 10 seconds and need a backend to collect it and alert if it gets too hot

**Spec:**
```
Type:       IoT data ingestion service
Auth:       Per-device credentials on the MQTT broker; JWT for dashboard users
Data model: Device(id, name, location, api_secret_hash)
            Reading(device_id -> Device, temperature_c, humidity_percent, recorded_at)
            AlertRule(id, device_id -> Device, metric, threshold, direction)
            Alert(id, rule_id -> AlertRule, value, triggered_at, resolved_at)
Features:   - Subscribe to sensor readings over MQTT
            - Store readings in a time-series table
            - Trigger an alert when a reading crosses a rule's threshold
            - Send alerts by email and SMS
            - Return downsampled history (1-minute averages) for charts
API:        REST
            GET  /devices
            GET  /devices/{id}/readings?from={time}&to={time}&bucket={interval}
            POST /alert-rules
            GET  /alerts
Storage:    TimescaleDB
Tech stack: Python, FastAPI, paho-mqtt, Eclipse Mosquitto, Twilio
```

---

## Example 375

**Intent:**
live football scores pushed to app users

**Spec:**
```
Type:       Real-time WebSocket server (live scores)
Data model: Match(id, home_team, away_team, kickoff_at, status, home_score, away_score, minute)
            MatchEvent(id, match_id -> Match, type, team, player, minute)
Features:   - Poll a sports data provider every 10 seconds for live matches
            - Detect goals, cards and substitutions as new events
            - Push score updates to clients subscribed to a match
            - Let clients subscribe to all matches of a competition
            - Send the current state when a client first connects
API:        REST + WebSocket
            GET  /matches?date={date}
            GET  /matches/{id}
            WS   /live
Storage:    Redis (current match state, pub/sub), PostgreSQL (match history)
Tech stack: Node.js, ws library, API-Football, ioredis
```

---

## Example 376

**Intent:**
I'd like a server that lets several people edit the same document at the same time, like google docs, without overwriting each other

**Spec:**
```
Type:       Real-time collaboration server
Auth:       JWT from the main app, checked on WebSocket connect
Data model: Document(id, owner_id, title, ydoc_state, updated_at)
            DocumentAccess(id, document_id -> Document, user_id, role)
Features:   - Sync document edits between clients using CRDTs
            - Merge concurrent edits without conflicts
            - Show other users' cursors and presence
            - Save document state to the database every few seconds
            - Allow read-only access for viewers
API:        REST + WebSocket
            GET  /documents
            POST /documents
            POST /documents/{id}/share
            WS   /collab/{documentId}
Storage:    PostgreSQL
Tech stack: Node.js, Yjs, Hocuspocus, TypeScript
```

---

## Example 377

**Intent:**
translation api in front of deepl that keeps our company words translated the same way

**Spec:**
```
Type:       REST API service (translation proxy)
Auth:       API key per internal team
Data model: GlossaryEntry(id, source_lang, target_lang, source_term, target_term)
            TranslationCache(hash, source_lang, target_lang, text, result, created_at)
Features:   - Translate text between supported languages
            - Apply the company glossary through DeepL glossaries
            - Cache translations to reduce cost
            - Manage glossary entries and sync them to DeepL
            - Report characters translated per team each month
API:        REST
            POST /translate
            GET  /glossary
            POST /glossary
            DELETE /glossary/{id}
            GET  /usage
Storage:    PostgreSQL, Redis (cache)
Tech stack: Python, FastAPI, DeepL API (deepl Python library)
```

---

## Example 378

**Intent:**
resize images on the fly from the url, like /img/photo.jpg?w=300

**Spec:**
```
Type:       Image processing service
Features:   - Read the original image from S3 by path
            - Resize, crop and convert format based on query parameters
            - Serve WebP or AVIF when the browser accepts it
            - Allow only a fixed list of widths to stop abuse
            - Sign URLs with HMAC so only the app can create new sizes
            - Set long cache headers for the CDN
API:        REST
            GET  /img/{path}?w={width}&h={height}&fit={cover|contain}&sig={hmac}
Storage:    Amazon S3 (originals), CloudFront (cache)
Tech stack: Node.js, Fastify, sharp, AWS SDK v3
```

---

## Example 379

**Intent:**
backend for the contact form on my static site, should block spam

**Spec:**
```
Type:       Form handling API
Data model: Submission(id, name, email, message, ip, is_spam, created_at)
Features:   - Accept contact form posts from the static site
            - Verify a Cloudflare Turnstile token
            - Reject submissions that fill the hidden honeypot field
            - Limit each IP to 5 submissions per hour
            - Forward valid messages to the site owner's email
API:        REST
            POST /contact
Storage:    SQLite
Tech stack: Python, Flask, Flask-Limiter, Cloudflare Turnstile, SMTP
```

---

## Example 380

**Intent:**
newsletter signup api with double opt in and unsubscribe link

**Spec:**
```
Type:       REST API service (newsletter)
Auth:       Admin API key for sending and exports
Data model: Subscriber(id, email, status, confirm_token_hash, subscribed_at, unsubscribed_at)
            Campaign(id, subject, html_body, sent_at)
Features:   - Add a subscriber as pending and email a confirmation link
            - Activate the subscriber when the link is clicked
            - Include a one-click unsubscribe link in every email
            - Send a campaign to all active subscribers in batches
            - Export subscribers as CSV
API:        REST
            POST /subscribe
            GET  /confirm?token={token}
            GET  /unsubscribe?token={token}
            POST /campaigns
            POST /campaigns/{id}/send
Storage:    PostgreSQL
Tech stack: Ruby, Sinatra, Sequel, Postmark API
```

---

## Example 381

**Intent:**
referral codes for our app, user invites friend, both get credit when friend signs up and pays

**Spec:**
```
Type:       Microservice (referrals)
Auth:       JWT from the main app
Data model: ReferralCode(id, user_id, code, created_at)
            Referral(id, code_id -> ReferralCode, referred_user_id, status, created_at, rewarded_at)
            Credit(id, user_id, amount, reason, referral_id -> Referral, created_at)
Features:   - Generate a unique short referral code per user
            - Attach a new signup to the referrer's code
            - Reward both users with credit after the friend's first payment
            - Block self-referrals and repeat referrals from the same device
            - Show a user how many friends joined and credit earned
API:        REST
            GET  /referrals/code
            POST /referrals/claim
            POST /events/payment-succeeded
            GET  /referrals/summary
Storage:    PostgreSQL
Tech stack: Kotlin, Ktor, Exposed, PostgreSQL
```

---

## Example 382

**Intent:**
discount coupon service for checkout

**Spec:**
```
Type:       Microservice (coupons)
Auth:       Internal service API key; admin JWT for managing coupons
Data model: Coupon(id, code, type, value, min_order_total, max_uses, uses_count, starts_at, ends_at)
            Redemption(id, coupon_id -> Coupon, user_id, order_id, discount_amount, redeemed_at)
Features:   - Create percentage and fixed-amount coupons with start and end dates
            - Validate a code against cart total, dates and usage limits
            - Limit each user to one use per coupon
            - Redeem a coupon atomically when an order is paid
            - Report redemptions and total discount per coupon
API:        REST
            POST /coupons
            POST /coupons/validate
            POST /coupons/redeem
            GET  /coupons/{code}/stats
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core Minimal APIs, Dapper
```

---

## Example 383

**Intent:**
loyalty points for a coffee chain, customers earn points per purchase and redeem for free drinks

**Spec:**
```
Type:       REST API service (loyalty program)
Auth:       Customer login by phone number + OTP; store POS uses API keys
Data model: Customer(id, phone, name, points_balance)
            Store(id, name, api_key_hash)
            PointsTransaction(id, customer_id -> Customer, store_id -> Store, points, type, receipt_id, created_at)
            Reward(id, name, points_cost, active)
Features:   - Earn 1 point per currency unit spent when the POS sends a purchase
            - Redeem points for a reward and return a one-time code for the barista
            - Show the customer's balance and transaction history
            - Expire points not used within 12 months
            - Prevent the same receipt from earning points twice
API:        REST
            POST /purchases
            GET  /customers/me/points
            GET  /rewards
            POST /rewards/{id}/redeem
Storage:    PostgreSQL
Tech stack: Python, FastAPI, SQLAlchemy, Alembic
```

---

## Example 384

**Intent:**
Our delivery drivers have a phone app and customers want to see where their order is on a map. I need the backend that receives driver GPS every few seconds and streams it to the customer tracking page, plus the order status changes.

**Spec:**
```
Type:       Real-time tracking service
Auth:       JWT for drivers; signed tracking link token for customers
Data model: Driver(id, name, phone, vehicle)
            Delivery(id, order_id, driver_id -> Driver, status, pickup_address, dropoff_address, eta)
            LocationPing(driver_id -> Driver, lat, lng, heading, recorded_at)
Features:   - Receive driver GPS pings every 5 seconds
            - Stream the driver's position to customers tracking that delivery
            - Update delivery status (assigned, picked up, nearby, delivered)
            - Recalculate the ETA with a routing API
            - Expire the tracking link once the order is delivered
API:        REST + WebSocket
            POST /drivers/me/location
            PATCH /deliveries/{id}/status
            GET  /track/{token}
            WS   /track/{token}/live
Storage:    Redis (latest positions, pub/sub), PostgreSQL (deliveries)
Tech stack: Go, gorilla/websocket, Google Maps Routes API, go-redis
```

---

## Example 385

**Intent:**
telegram bot where i type what i spent and it keeps track of my expenses

**Spec:**
```
Type:       Chat bot backend (Telegram)
Data model: User(id, telegram_id, currency)
            Expense(id, user_id -> User, amount, category, note, spent_at)
Features:   - Parse messages like "12.50 lunch" into amount and category
            - Receive updates through a Telegram webhook
            - Show totals for today, this week and this month with commands
            - Undo the last expense with /undo
            - Export all expenses as a CSV file in the chat
API:        REST
            POST /telegram/webhook
Storage:    SQLite
Tech stack: Python, aiogram, aiohttp
```

---

## Example 386

**Intent:**
send whatsapp message to customer when there order is shipped

**Spec:**
```
Type:       Notification service (WhatsApp)
Auth:       API key from the shop backend
Data model: MessageTemplate(id, name, language, whatsapp_template_name)
            OutboundMessage(id, order_id, phone, template_id -> MessageTemplate, wa_message_id, status, sent_at)
Features:   - Receive order shipped events from the shop backend
            - Send an approved WhatsApp template message with order number and tracking link
            - Track sent, delivered and read status from WhatsApp webhooks
            - Fall back to SMS when the number is not on WhatsApp
            - Avoid sending the same message twice for one order
API:        REST
            POST /notifications/order-shipped
            GET  /webhooks/whatsapp
            POST /webhooks/whatsapp
Storage:    MySQL
Tech stack: Node.js, Express, WhatsApp Cloud API (Meta Graph API), Twilio SMS
```

---

## Example 387

**Intent:**
create zoom meetings automatically when someone books a call with us

**Spec:**
```
Type:       Integration service (Zoom)
Auth:       Zoom Server-to-Server OAuth app
Data model: CallBooking(id, name, email, starts_at, duration_minutes, zoom_meeting_id, join_url)
Features:   - Accept a booking with name, email and time
            - Create a Zoom meeting through the Zoom API
            - Email the join link and a calendar invite (.ics) to the guest
            - Update or delete the Zoom meeting when the booking changes
            - Record attendance from Zoom meeting.ended webhooks
API:        REST
            POST /bookings
            PUT  /bookings/{id}
            DELETE /bookings/{id}
            POST /webhooks/zoom
Storage:    PostgreSQL
Tech stack: Python, Flask, Zoom REST API, ics, SendGrid
```

---

## Example 388

**Intent:**
post jira ticket updates to the right slack channel per project

**Spec:**
```
Type:       Webhook receiver (integration service)
Data model: ProjectChannel(id, jira_project_key, slack_channel_id, events)
Features:   - Receive Jira issue created, updated and commented webhooks
            - Check a shared secret in the webhook URL
            - Map each Jira project to a Slack channel
            - Post formatted messages with issue key, title, status and assignee
            - Thread updates for the same issue under its first message
API:        REST
            POST /webhooks/jira/{secret}
            GET  /mappings
            POST /mappings
Storage:    Cloudflare D1
Tech stack: TypeScript, Hono, Slack Web API, Cloudflare Workers
```

---

## Example 389

**Intent:**
keep hubspot contacts in sync with users in our database, both directions

**Spec:**
```
Type:       Background sync worker (CRM integration)
Auth:       HubSpot private app token
Data model: SyncLink(id, user_id, hubspot_contact_id, last_synced_at, last_hash)
            SyncError(id, user_id, direction, message, created_at)
Features:   - Push new and changed users to HubSpot as contacts
            - Pull contact changes from HubSpot webhooks into the database
            - Resolve conflicts by the most recent update time
            - Batch API calls and respect HubSpot rate limits
            - Log failed syncs and retry them hourly
API:        REST
            POST /webhooks/hubspot
            POST /sync/full
Storage:    PostgreSQL, Redis (job queue)
Tech stack: Ruby, Ruby on Rails, Sidekiq, HubSpot API client
```

---

## Example 390

**Intent:**
uptime checker that pings my websites every minute and tells me when one is down

**Spec:**
```
Type:       Monitoring service (uptime)
Auth:       User login (email + password)
Data model: User(id, email, password_hash)
            Monitor(id, user_id -> User, url, interval_seconds, expected_status, keyword, active)
            Check(id, monitor_id -> Monitor, status_code, response_ms, ok, checked_at)
            Incident(id, monitor_id -> Monitor, started_at, resolved_at, reason)
Features:   - Send HTTP requests to each monitored URL on its interval
            - Mark a site down after 2 failed checks in a row
            - Alert by email and Slack when a site goes down and recovers
            - Calculate uptime percentage for 24 hours, 7 days and 30 days
            - Provide a public status page per user
API:        REST
            GET  /monitors
            POST /monitors
            DELETE /monitors/{id}
            GET  /monitors/{id}/checks
            GET  /status/{user_slug}
Storage:    PostgreSQL
Tech stack: Go, net/http, robfig/cron, PostgreSQL
```

---

## Example 391

**Intent:**
pastebin api with expiring pastes

**Spec:**
```
Type:       REST API service (paste sharing)
Data model: Paste(id, slug, content, language, password_hash, burn_after_read, expires_at, created_at)
Features:   - Create a paste with optional syntax language and expiry time
            - Return the paste by a short random slug
            - Delete a paste after its first read when burn-after-read is set
            - Protect pastes with an optional password
            - Limit paste size to 512 KB
API:        REST
            POST /pastes
            GET  /pastes/{slug}
            GET  /pastes/{slug}/raw
Storage:    Redis (pastes with TTL)
Tech stack: Rust, Axum, redis-rs
```

---

## Example 392

**Intent:**
small api: send markdown, get html back, safe for putting on a page

**Spec:**
```
Type:       REST API service (Markdown rendering)
Features:   - Convert GitHub-flavored Markdown to HTML
            - Sanitize the output to remove scripts and unsafe attributes
            - Highlight code blocks by language
            - Optionally add anchor links to headings
            - Reject input larger than 1 MB
API:        REST
            POST /render
Tech stack: Node.js, Express, markdown-it, DOMPurify (jsdom), Shiki
```

---

## Example 393

**Intent:**
an api to check if an email adress is real before people sign up

**Spec:**
```
Type:       REST API service (email validation)
Auth:       API key
Data model: DomainCache(domain, has_mx, is_disposable, checked_at)
Features:   - Check email syntax against RFC 5322 rules
            - Look up MX records for the domain
            - Flag disposable email providers from a maintained list
            - Suggest fixes for common typos like gmial.com
            - Validate up to 1000 emails in one batch request
API:        REST
            GET  /validate?email={address}
            POST /validate/batch
Storage:    Redis (domain cache)
Tech stack: Python, FastAPI, dnspython, email-validator
```

---

## Example 394

**Intent:**
IP address to country and city lookup service

**Spec:**
```
Type:       REST API service (IP geolocation)
Auth:       API key with monthly quota
Data model: ApiKey(id, owner_email, key_hash, monthly_quota, used_this_month)
Features:   - Return country, region, city, timezone and ASN for an IP address
            - Look up the caller's own IP when none is given
            - Support IPv4 and IPv6
            - Update the GeoIP database weekly
            - Count usage per API key and return 429 over quota
API:        REST
            GET  /lookup/{ip}
            GET  /lookup/me
Storage:    MaxMind GeoLite2 database file, PostgreSQL (API keys)
Tech stack: Go, Gin, oschwald/geoip2-golang
```

---

## Example 395

**Intent:**
I am working with team in many countries, please make API that tell time in other timezone and find meeting time good for everyone.

**Spec:**
```
Type:       REST API service (time zones)
Features:   - Convert a date and time from one time zone to another
            - Return the current time for a list of cities
            - Find meeting slots that fall inside working hours for all given time zones
            - Handle daylight saving time changes correctly
            - Search time zones by city name
API:        REST
            GET  /convert?time={iso}&from={tz}&to={tz}
            GET  /now?zones={tz,tz}
            POST /meeting-slots
            GET  /zones?q={city}
Tech stack: Python, FastAPI, zoneinfo (IANA tz database)
```

---

## Example 396

**Intent:**
bulk email sender with celery, we send like 50k emails to customers and it shouldnt block the web app

**Spec:**
```
Type:       Background job worker (bulk email)
Auth:       Admin login (Django auth)
Data model: Campaign(id, subject, template, status, created_at, scheduled_at)
            Recipient(id, campaign_id -> Campaign, email, status, sent_at, error)
Features:   - Split a campaign into chunks of 500 recipients
            - Send chunks in parallel Celery tasks
            - Throttle sending to stay under the provider's rate limit
            - Retry temporary failures and mark hard bounces
            - Show campaign progress and failure counts
API:        REST
            POST /campaigns
            POST /campaigns/{id}/send
            GET  /campaigns/{id}/progress
Storage:    PostgreSQL, Redis (Celery broker)
Tech stack: Python, Django, Celery, Amazon SES (django-ses)
```

---

## Example 397

**Intent:**
users click export and get a big excel report emailed to them later

**Spec:**
```
Type:       Background job worker (report generation)
Auth:       JWT (existing app users)
Data model: ReportRequest(id, user_id, report_type, filters_json, status, file_key, created_at, finished_at)
Features:   - Queue a report request with its filters
            - Query data in pages to keep memory low
            - Build an .xlsx file with formatted headers and totals
            - Upload the file and email the user a download link valid for 48 hours
            - Show the status of recent report requests
API:        REST
            POST /reports
            GET  /reports
            GET  /reports/{id}/download
Storage:    PostgreSQL, Amazon S3 (report files), Redis (queue)
Tech stack: Node.js, NestJS, BullMQ, ExcelJS
```

---

## Example 398

**Intent:**
I run a marketplace where freelancers sell services, I need customers to pay through the platform, we keep 10% fee and the rest goes to the freelancer automatically. Freelancers must onboard with their bank details and get paid out weekly.

**Spec:**
```
Type:       REST API service (marketplace payments)
Auth:       JWT login with roles Customer and Freelancer
Data model: User(id, email, password_hash, role, stripe_account_id)
            Service(id, freelancer_id -> User, title, price_cents)
            Order(id, service_id -> Service, customer_id -> User, amount_cents, fee_cents, stripe_payment_intent_id, status)
            Payout(id, freelancer_id -> User, amount_cents, stripe_payout_id, status, paid_at)
Features:   - Onboard freelancers with Stripe Connect Express accounts
            - Charge customers with a PaymentIntent and a 10% application fee
            - Transfer the remaining amount to the freelancer's connected account
            - Schedule weekly payouts to freelancers' bank accounts
            - Handle refunds and disputes from Stripe webhooks
API:        REST
            POST /freelancers/onboarding-link
            POST /orders
            POST /orders/{id}/refund
            GET  /payouts
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, Django REST Framework, Stripe Python SDK (Connect)
```

---

## Example 399

**Intent:**
add 2fa with authenticator app codes to our login api

**Spec:**
```
Type:       Authentication service (two-factor)
Auth:       Email + password, then TOTP code (RFC 6238)
Data model: User(id, email, password_hash, totp_secret_encrypted, totp_enabled)
            RecoveryCode(id, user_id -> User, code_hash, used_at)
Features:   - Generate a TOTP secret and return a QR code for authenticator apps
            - Enable 2FA only after the user confirms a valid code
            - Require a TOTP code after password login when 2FA is on
            - Issue 10 single-use recovery codes
            - Lock the account for 15 minutes after 5 wrong codes
API:        REST
            POST /2fa/setup
            POST /2fa/enable
            POST /login
            POST /login/2fa
            POST /2fa/disable
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Spring Security, GoogleAuth (TOTP), ZXing
```

---

## Example 400

**Intent:**
central session store so all our services know who is logged in

**Spec:**
```
Type:       Session management service
Auth:       Opaque session tokens in secure cookies; internal services use mTLS
Data model: Session(id, user_id, created_at, last_seen_at, expires_at, ip, user_agent)
Features:   - Create a session after login and return an opaque token
            - Validate a token and return the user ID for other services
            - Slide the expiry on activity up to a 30-day maximum
            - List a user's active sessions with device and IP
            - Revoke one session or all sessions for a user
API:        REST
            POST /sessions
            GET  /sessions/validate
            GET  /users/{id}/sessions
            DELETE /sessions/{id}
            DELETE /users/{id}/sessions
Storage:    Redis
Tech stack: Go, chi router, go-redis
```

---

## Example 401

**Intent:**
roles and permissions service, like who can edit what

**Spec:**
```
Type:       Authorization service (RBAC)
Auth:       Service tokens for permission checks; admin JWT for managing roles
Data model: Role(id, name, description)
            Permission(id, action, resource)
            RolePermission(role_id -> Role, permission_id -> Permission)
            UserRole(user_id, role_id -> Role, scope_id)
Features:   - Define roles and attach permissions like project:edit
            - Assign roles to users globally or within a scope such as one project
            - Answer whether a user can do an action on a resource in one call
            - Check many permissions in one batch request
            - Cache permission results and clear the cache on role changes
API:        REST
            POST /roles
            POST /roles/{id}/permissions
            POST /users/{id}/roles
            POST /check
            POST /check/batch
Storage:    PostgreSQL, Redis (cache)
Tech stack: TypeScript, NestJS, Casbin, TypeORM
```

---

## Example 402

**Intent:**
api gateway in front of our microservices with auth and rate limit

**Spec:**
```
Type:       API gateway
Auth:       JWT validation (RS256) against the auth service's JWKS
Data model: Route(id, path_prefix, upstream_url, auth_required, rate_limit_per_minute)
Features:   - Route requests to upstream services by path prefix
            - Validate JWTs and forward the user ID in a header
            - Rate limit per user and per IP with a token bucket
            - Add request IDs and log each request with latency
            - Return 503 with a circuit breaker when an upstream keeps failing
API:        REST
            ANY  /{service}/{path}
            GET  /health
Storage:    Redis (rate limit counters), YAML file (route config)
Tech stack: Go, net/http/httputil (reverse proxy), go-redis, sony/gobreaker
```

---

## Example 403

**Intent:**
users choose how they want notifications - email, sms or push - and a service sends through the right channel

**Spec:**
```
Type:       Notification routing service
Auth:       Service API keys; user JWT for preference endpoints
Data model: Preference(user_id, notification_type, email_enabled, sms_enabled, push_enabled, quiet_hours_json)
            Notification(id, user_id, type, payload_json, created_at)
            DeliveryAttempt(id, notification_id -> Notification, channel, status, provider_id, sent_at)
Features:   - Store per-user channel choices for each notification type
            - Route each notification to the enabled channels
            - Hold non-urgent notifications during the user's quiet hours
            - Send email via SendGrid, SMS via Twilio and push via FCM
            - Record delivery status per channel
API:        REST
            GET  /preferences
            PUT  /preferences
            POST /notifications
            GET  /notifications/{id}
Storage:    PostgreSQL, RabbitMQ (channel queues)
Tech stack: Python, FastAPI, aio-pika, SendGrid, Twilio, firebase-admin
```

---

## Example 404

**Intent:**
a kahoot style quiz game server with socket.io, host starts questions and players answer from phones

**Spec:**
```
Type:       Real-time WebSocket server (multiplayer quiz)
Auth:       Host login (email + password); players join with a game PIN and nickname
Data model: Quiz(id, host_id, title)
            Question(id, quiz_id -> Quiz, text, options_json, correct_index, time_limit_seconds)
            GameSession(id, quiz_id -> Quiz, pin, status, started_at)
            PlayerScore(id, session_id -> GameSession, nickname, score)
Features:   - Create a game session with a 6-digit PIN
            - Let players join the lobby with the PIN and a nickname
            - Push each question to all players with a countdown
            - Score answers by correctness and speed
            - Show the leaderboard after each question and at the end
API:        REST + WebSocket
            POST /quizzes
            POST /quizzes/{id}/sessions
            WS   /socket.io
Storage:    PostgreSQL (quizzes), Redis (live game state)
Tech stack: Node.js, Socket.IO, Express, Redis adapter
```

---

## Example 405

**Intent:**
live poll for presentations, audience votes and results update on screen

**Spec:**
```
Type:       Real-time polling service
Auth:       Presenter login (magic link email); voters anonymous with a device cookie
Data model: Poll(id, presenter_id, question, options_json, status, code)
            Vote(id, poll_id -> Poll, option_index, voter_id, created_at)
Features:   - Create a poll and get a short join code
            - Let the audience vote once per device
            - Push live result counts to the presenter screen
            - Open and close voting from the presenter view
            - Export results as CSV
API:        REST + SSE
            POST /polls
            POST /polls/{code}/votes
            PATCH /polls/{id}
            GET  /polls/{id}/results/stream
Storage:    Redis (live counts), PostgreSQL (polls, votes)
Tech stack: Python, FastAPI, sse-starlette, redis-py
```

---

## Example 406

**Intent:**
customer support ticket api for our helpdesk app

**Spec:**
```
Type:       REST API service (helpdesk)
Auth:       JWT login with roles Customer, Agent, Admin
Data model: User(id, email, password_hash, role)
            Ticket(id, customer_id -> User, assignee_id -> User, subject, status, priority, created_at)
            Reply(id, ticket_id -> Ticket, author_id -> User, body, is_internal, created_at)
            Attachment(id, reply_id -> Reply, filename, s3_key)
Features:   - Open tickets and add replies with attachments
            - Assign tickets to agents automatically by round robin
            - Add internal notes that customers cannot see
            - Change status and priority and record the history
            - Flag tickets that break the SLA response time
API:        REST
            GET  /tickets?status={s}&assignee={id}
            POST /tickets
            GET  /tickets/{id}
            PATCH /tickets/{id}
            POST /tickets/{id}/replies
Storage:    PostgreSQL, Amazon S3 (attachments)
Tech stack: TypeScript, NestJS, Prisma, AWS SDK v3
```

---

## Example 407

**Intent:**
hey so we keep losing phone plan customers and my boss wants to know who's likely to cancel next month, we have a big csv export from the billing system

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load the customer export and drop duplicate and empty rows
            - Encode plan type, contract length and payment method as features
            - Train a gradient-boosted classifier to predict churn next month
            - Evaluate with ROC AUC, precision and recall on a held-out set
            - Rank current customers by churn probability
            - Show the top features that drive churn
            - Export a CSV of at-risk customers with their scores
Input:      CSV file with columns: customer_id, tenure_months, plan_type, monthly_charge, support_calls, contract, churned
Storage:    Local files (trained model saved with joblib)
Tech stack: Python, pandas, scikit-learn, LightGBM, matplotlib
```

---

## Example 408

**Intent:**
analyse our google forms survey results

**Spec:**
```
Type:       Data analysis script
Features:   - Load survey responses from the Google Forms CSV export
            - Clean column names and normalise answer text
            - Count answers for each multiple-choice question
            - Calculate average scores for rating-scale questions
            - Cross-tabulate answers by respondent age group
            - Plot a bar chart for every question
            - Save all charts and tables into a single PDF report
Input:      CSV export from Google Forms (one row per response)
Tech stack: Python, pandas, matplotlib, seaborn, matplotlib PdfPages
```

---

## Example 409

**Intent:**
I need a nightly pipeline using Airflow that pulls orders and customers from our Shopify store and loads them into Postgres so the analysts can query them.

**Spec:**
```
Type:       Scheduled data pipeline (ETL)
Data model: Customer(id, email, first_name, last_name, country, created_at)
            Order(id, customer_id -> Customer, total_price, currency, status, created_at)
            OrderLine(id, order_id -> Order, product_id, sku, quantity, unit_price)
Features:   - Run every night at 02:00 as an Airflow DAG
            - Fetch orders and customers changed since the last run from the Shopify Admin API
            - Handle API pagination and rate limits with retries
            - Flatten nested order JSON into order and order line rows
            - Upsert rows into Postgres tables by primary key
            - Log row counts and send an alert email when a task fails
Input:      Shopify Admin API (access token)
Storage:    PostgreSQL
Tech stack: Python, Apache Airflow, requests, pandas, SQLAlchemy, psycopg2
```

---

## Example 410

**Intent:**
can you build something with hugging face that reads our amazon product reviews and says if they are positive negative or neutral

**Spec:**
```
Type:       NLP script (sentiment analysis)
Features:   - Load product reviews from a CSV file
            - Clean review text: strip HTML, URLs and extra whitespace
            - Classify each review as positive, negative or neutral with a pretrained transformer
            - Process reviews in batches on GPU when available
            - Summarise sentiment share per product
            - Export reviews with their sentiment label and confidence score
Input:      CSV file with columns: review_id, product_id, rating, review_text
Tech stack: Python, Hugging Face Transformers (cardiffnlp/twitter-roberta-base-sentiment), PyTorch, pandas
```

---

## Example 411

**Intent:**
I'd like to train a model in PyTorch that looks at a photo of a tomato leaf and tells which disease it has. I have about 10,000 labelled pictures in folders by disease name. It should run on a normal laptop afterwards.

**Spec:**
```
Type:       Machine learning model (image classification)
Features:   - Load images from class-named folders and split into train, validation and test sets
            - Augment training images with random flips, rotations and colour jitter
            - Fine-tune a pretrained MobileNetV3 on the leaf disease classes
            - Track validation accuracy and save the best checkpoint
            - Show a confusion matrix and per-class accuracy on the test set
            - Export the model to ONNX for fast CPU inference
            - Predict the disease for a single image from the command line
Input:      Folder of labelled leaf images (one subfolder per disease)
Storage:    Local files (model checkpoints, ONNX model)
Tech stack: Python, PyTorch, torchvision, ONNX Runtime, matplotlib
```

---

## Example 412

**Intent:**
detect weird credit card transactions

**Spec:**
```
Type:       Machine learning model (anomaly detection)
Features:   - Load card transactions and parse timestamps
            - Build features: amount, hour of day, distance from home, spend vs card average
            - Train an Isolation Forest on past transactions
            - Score new transactions with an anomaly score
            - Flag transactions above a tunable threshold
            - Plot score distribution and flagged transactions
            - Export flagged transactions to a CSV for review
Input:      CSV file with columns: transaction_id, card_id, amount, merchant_category, timestamp, latitude, longitude
Tech stack: Python, pandas, scikit-learn, matplotlib
```

---

## Example 413

**Intent:**
we ran an a/b test on our signup page for two weeks, version b has a different button, i want to know if it actually did better or its just luck

**Spec:**
```
Type:       Statistical analysis (A/B test)
Features:   - Load visitor-level experiment data and check the sample ratio between groups
            - Calculate conversion rate for version A and version B
            - Run a two-proportion z-test and report the p-value
            - Calculate the 95% confidence interval for the uplift
            - Check the result day by day to spot novelty effects
            - Plot conversion rates with confidence intervals
            - Print a plain-language verdict on whether B is better
Input:      CSV file with columns: visitor_id, variant, converted, visit_date
Tech stack: Python, pandas, statsmodels, SciPy, matplotlib
```

---

## Example 414

**Intent:**
movie recomendation system like netflix for my side project using the movielens dataset

**Spec:**
```
Type:       Recommendation system (web API)
Data model: User(id, created_at)
            Movie(id, title, genres, year)
            Rating(id, user_id -> User, movie_id -> Movie, score, rated_at)
Features:   - Load the MovieLens ratings and movie metadata
            - Train a matrix factorisation model on user ratings
            - Recommend the top 10 unseen movies for a user
            - Recommend similar movies for a given movie
            - Fall back to popular movies for new users with no ratings
            - Evaluate the model with RMSE and precision@10
API:        REST
            GET  /users/{id}/recommendations
            GET  /movies/{id}/similar
            POST /ratings
Storage:    SQLite (ratings), local file (trained model)
Tech stack: Python, Surprise (SVD), pandas, FastAPI
```

---

## Example 415

**Intent:**
I have solar panels on my roof and an export of the daily kWh they produced for 3 years, could I forecast next month's output with Prophet?

**Spec:**
```
Type:       Forecasting script (time series)
Features:   - Load daily solar output and fill missing days
            - Add daily sunshine hours as an extra regressor when available
            - Fit a Prophet model with yearly seasonality
            - Forecast daily output for the next 30 days with uncertainty intervals
            - Back-test the model on the last 3 months and report MAPE
            - Plot history, forecast and seasonal components
Input:      CSV file with columns: date, kwh_produced (optional: sunshine_hours)
Tech stack: Python, Prophet, pandas, matplotlib
```

---

## Example 416

**Intent:**
Set up dbt models in BigQuery for our marketing data: raw ad spend from Google Ads and Facebook Ads, plus website sessions, and I want clean tables for spend, clicks and cost per signup by campaign and day.

**Spec:**
```
Type:       Data warehouse transformation (dbt project)
Data model: StgGoogleAds(date, campaign_id, campaign_name, spend, clicks, impressions)
            StgFacebookAds(date, campaign_id, campaign_name, spend, clicks, impressions)
            StgSessions(session_id, date, utm_source, utm_campaign, signed_up)
            FctCampaignDaily(date, channel, campaign_name, spend, clicks, signups, cost_per_signup)
Features:   - Build staging models that rename and type-cast the raw source tables
            - Union Google Ads and Facebook Ads into one ad spend model
            - Join ad spend with sessions on campaign and date
            - Calculate cost per click and cost per signup per campaign and day
            - Add dbt tests for not-null, unique keys and accepted channel values
            - Build the fact table incrementally by date
            - Generate dbt docs with a lineage graph
Storage:    Google BigQuery
Tech stack: dbt Core, dbt-bigquery, SQL, Google BigQuery
```

---

## Example 417

**Intent:**
our customer list is a mess, same people entered twice with different spellings and addresses all over the place

**Spec:**
```
Type:       Data cleaning script
Features:   - Load the customer list and standardise case, whitespace and punctuation
            - Normalise phone numbers to E.164 format and validate emails
            - Parse addresses into street, city and postcode
            - Find likely duplicates with fuzzy matching on name, email and address
            - Merge duplicate records keeping the most complete values
            - Write a cleaned file and a report of merged records
Input:      CSV or Excel file with columns: name, email, phone, address
Tech stack: Python, pandas, RapidFuzz, phonenumbers, usaddress
```

---

## Example 418

**Intent:**
make me a streamlit dashboard where i upload my bank statements and it shows where my money goes each month

**Spec:**
```
Type:       Data dashboard (web)
Features:   - Upload one or more bank statement CSV files
            - Parse dates and amounts and remove duplicate transactions
            - Categorise transactions with keyword rules the user can edit
            - Show monthly spending by category as a stacked bar chart
            - Show income vs expenses and savings rate per month
            - Filter by date range and category
            - Download the categorised transactions as a CSV
Input:      Bank statement CSV files with columns: date, description, amount
Storage:    Local JSON file (category rules)
Tech stack: Python, Streamlit, pandas, Plotly
```

---

## Example 419

**Intent:**
I want a house price prediction model that our website can call through an API

**Spec:**
```
Type:       Model-serving API
Auth:       API key per client (sent in the X-API-Key header)
Features:   - Train a regression model on historical house sales
            - Validate request fields and reject out-of-range values
            - Return a predicted price with a prediction interval
            - Return the model version with every prediction
            - Log every request and prediction for later monitoring
API:        REST
            POST /predict
            GET  /model/info
            GET  /health
Storage:    Local file (model artefact), PostgreSQL (prediction logs)
Tech stack: Python, scikit-learn, XGBoost, FastAPI, Pydantic, Docker
```

---

## Example 420

**Intent:**
spam filter for emails using scikit-learn

**Spec:**
```
Type:       Machine learning model (text classification)
Features:   - Load labelled emails and split into train and test sets
            - Convert email text to TF-IDF features with word and character n-grams
            - Train a Multinomial Naive Bayes and a Logistic Regression model
            - Compare models with precision, recall and F1 score
            - Save the best model as a single scikit-learn pipeline
            - Classify a new email from the command line
Input:      CSV file with columns: text, label (spam or ham)
Storage:    Local file (pipeline saved with joblib)
Tech stack: Python, scikit-learn, pandas, joblib
```

---

## Example 421

**Intent:**
i have a year of bike share trip data from my city and want to just explore it in a jupyter notebook and find interesting patterns

**Spec:**
```
Type:       Jupyter notebook (exploratory data analysis)
Features:   - Load monthly trip files and combine them into one table
            - Clean trips with negative or extreme durations
            - Show trips by hour of day, weekday and month
            - Compare members vs casual riders on duration and time of use
            - Map the busiest start and end stations
            - Find the most common station-to-station routes
            - Summarise key findings in markdown cells
Input:      Monthly CSV files with columns: ride_id, started_at, ended_at, start_station, end_station, member_type, lat, lng
Tech stack: Python, Jupyter, pandas, seaborn, Folium
```

---

## Example 422

**Intent:**
Every evening I want to fetch closing prices for my watchlist of stocks and keep them in DuckDB so I can query history later with SQL.

**Spec:**
```
Type:       Scheduled data pipeline (ETL)
Data model: Ticker(symbol, name, exchange)
            DailyPrice(symbol -> Ticker, date, open, high, low, close, adj_close, volume)
Features:   - Read the watchlist of ticker symbols from a config file
            - Download daily prices since the last stored date for each ticker
            - Skip weekends and market holidays without errors
            - Insert new rows and ignore rows that already exist
            - Run automatically every weekday evening
            - Print a summary of rows added per ticker
Input:      YAML config file with the list of ticker symbols
Storage:    DuckDB database file
Tech stack: Python, yfinance, DuckDB, pandas, cron (scheduling)
```

---

## Example 423

**Intent:**
HR gave me the employee data and want to understand why people are leaving, i prefer to do it in R

**Spec:**
```
Type:       Data analysis report
Features:   - Load the employee dataset and clean factor levels
            - Compare attrition rates by department, role, tenure and salary band
            - Test differences between leavers and stayers with chi-square and t-tests
            - Fit a logistic regression to find factors linked to leaving
            - Plot attrition rates and model odds ratios
            - Render the analysis as an HTML report
Input:      CSV file with columns: employee_id, department, job_role, tenure_years, salary, satisfaction_score, overtime, left_company
Tech stack: R, tidyverse, broom, ggplot2, R Markdown
```

---

## Example 424

**Intent:**
what are people tweeting about our brand, group the tweets into topics

**Spec:**
```
Type:       NLP script (topic modelling)
Features:   - Load tweets and remove retweets, links and mentions
            - Embed tweets with a sentence transformer model
            - Cluster tweets into topics with BERTopic
            - Label each topic with its top keywords
            - Show topic sizes and how topics change over time
            - Export each tweet with its topic label
Input:      CSV file with columns: tweet_id, created_at, text
Tech stack: Python, BERTopic, sentence-transformers, pandas, Plotly
```

---

## Example 425

**Intent:**
i own small bakery, i want to know how many breads to bake each day so not so much is thrown away

**Spec:**
```
Type:       Forecasting script (demand forecasting)
Features:   - Load daily sales per product from the till export
            - Add weekday, holiday and weather features
            - Train a forecasting model per product
            - Predict tomorrow's demand for each product
            - Suggest a bake quantity with a small safety margin
            - Compare forecast error against the current baking plan
            - Print a daily bake list
Input:      CSV file with columns: date, product, quantity_sold, quantity_baked
Tech stack: Python, pandas, scikit-learn (Gradient Boosting), holidays
```

---

## Example 426

**Intent:**
I want to find strange activity in our nginx access logs, like sudden spikes of errors or one IP doing way too many requests.

**Spec:**
```
Type:       Anomaly detection script (log analysis)
Features:   - Parse nginx access log lines into structured fields
            - Aggregate requests, error rates and unique IPs per minute
            - Detect spikes with a rolling median and z-score threshold
            - Flag IPs with request rates far above normal
            - Plot traffic and error rate with anomalies marked
            - Write an anomaly report with timestamps and reasons
Input:      nginx access log files (combined log format, plain or .gz)
Tech stack: Python, pandas, NumPy, matplotlib
```

---

## Example 427

**Intent:**
we have terabytes of clickstream json in s3 and need a spark job that turns it into daily parquet tables partitioned by date

**Spec:**
```
Type:       Batch data processing job
Data model: Event(event_id, user_id, session_id, event_type, page_url, referrer, event_time, event_date)
            DailySessionSummary(session_id, user_id, event_date, page_views, duration_seconds, converted)
Features:   - Read raw JSON event files for a given date from S3
            - Apply an explicit schema and drop malformed records
            - Deduplicate events by event_id
            - Build session summaries with page views, duration and conversion
            - Write events and summaries as Parquet partitioned by event_date
            - Accept the processing date as a job argument for backfills
Input:      Raw JSON clickstream files in S3 (s3://bucket/raw/clickstream/date=YYYY-MM-DD/)
Storage:    Amazon S3 (Parquet)
Tech stack: Apache Spark (PySpark), Amazon EMR, AWS Glue Data Catalog
```

---

## Example 428

**Intent:**
build a sales dashboard in power bi from our sql server database

**Spec:**
```
Type:       BI dashboard
Data model: FactSales(sale_id, date_key -> DimDate, product_key -> DimProduct, store_key -> DimStore, quantity, revenue, cost)
            DimDate(date_key, date, month, quarter, year)
            DimProduct(product_key, name, category, brand)
            DimStore(store_key, name, region, city)
Features:   - Import sales tables from SQL Server into a star-schema model
            - Calculate revenue, margin and year-over-year growth with DAX measures
            - Show KPI cards for revenue, margin and units sold
            - Show revenue by region on a map and by category in a bar chart
            - Filter by date, region, store and product category with slicers
            - Refresh the data automatically every morning
Input:      Microsoft SQL Server sales database
Tech stack: Power BI Desktop, Power BI Service, DAX, Power Query
```

---

## Example 429

**Intent:**
every monday i copy numbers from 3 spreadsheets into one kpi report and email it, please automate this

**Spec:**
```
Type:       Command-line script (report automation)
Features:   - Read the three source spreadsheets from a shared folder
            - Calculate weekly KPIs and compare them with the previous week
            - Fill the KPI report Excel template with values and charts
            - Highlight KPIs that dropped more than 10% in red
            - Email the report as an attachment to a recipient list
            - Run automatically every Monday at 08:00
Input:      Three Excel files (.xlsx) in a shared folder, plus a report template
Tech stack: Python, pandas, openpyxl, smtplib, Windows Task Scheduler
```

---

## Example 430

**Intent:**
I'm a teacher and have all my students test scores for the year in an excel sheet, I want to see who is struggling and how each class compares.

**Spec:**
```
Type:       Data analysis script
Features:   - Load test scores for all classes from the Excel workbook
            - Calculate each student's average and trend across the year
            - Flag students whose average is below the pass mark or falling
            - Compare class averages and score spread with box plots
            - Show score distribution per test
            - Export a summary sheet per class to a new Excel file
Input:      Excel file (.xlsx) with columns: student_name, class, test_name, test_date, score
Tech stack: Python, pandas, openpyxl, seaborn
```

---

## Example 431

**Intent:**
analyse my strava runs

**Spec:**
```
Type:       Jupyter notebook (personal data analysis)
Features:   - Load activities from the Strava bulk export
            - Filter to runs and convert pace and distance units
            - Show weekly and monthly distance totals
            - Plot pace trend over time for similar-distance runs
            - Find personal bests for 5K, 10K and half marathon
            - Show heart rate zones per run when available
Input:      Strava bulk export (activities.csv and GPX/FIT files)
Tech stack: Python, Jupyter, pandas, gpxpy, fitparse, Plotly
```

---

## Example 432

**Intent:**
a little web page where you draw a digit with your mouse and a neural net guesses which number it is

**Spec:**
```
Type:       Web application (ML demo)
Features:   - Train a small convolutional network on the MNIST dataset
            - Show a canvas where the user draws a digit with the mouse or finger
            - Resize and centre the drawing to 28x28 pixels
            - Predict the digit in the browser and show the top 3 guesses with probabilities
            - Clear the canvas with a button
Storage:    Static files (model weights served with the page)
Tech stack: Python, TensorFlow/Keras (training), TensorFlow.js, HTML, JavaScript (Canvas API)
```

---

## Example 433

**Intent:**
we are a recruiting agency and we want to match uploaded CVs to our open job ads automatically, giving a score for each match so recruiters see the best candidates first

**Spec:**
```
Type:       Web application (ML matching service)
Auth:       Recruiter login (email + password)
Data model: Recruiter(id, email, password_hash)
            Job(id, title, description, required_skills, location)
            Candidate(id, name, email, cv_text, skills, embedding)
            Match(id, job_id -> Job, candidate_id -> Candidate, score, created_at)
Features:   - Upload CVs as PDF or Word files and extract their text
            - Extract skills from CVs and job ads with an NER model
            - Embed CVs and job ads with a sentence transformer
            - Score each candidate per job with cosine similarity plus skill overlap
            - Show a ranked candidate list for each job
            - Explain each score with matched and missing skills
API:        REST
            POST /candidates
            POST /jobs
            GET  /jobs/{id}/matches
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, sentence-transformers, spaCy, pdfplumber, python-docx, React
```

---

## Example 434

**Intent:**
segment our customers into groups based on how they buy (rfm)

**Spec:**
```
Type:       Data analysis script (customer segmentation)
Features:   - Load order history and compute recency, frequency and monetary value per customer
            - Scale RFM values and remove extreme outliers
            - Choose the number of clusters with the elbow method and silhouette score
            - Cluster customers with K-means
            - Describe each segment with average RFM values and size
            - Plot segments in 2D and export customers with their segment label
Input:      CSV file with columns: order_id, customer_id, order_date, order_total
Tech stack: Python, pandas, scikit-learn, seaborn
```

---

## Example 435

**Intent:**
We put air quality sensors in 20 classrooms that send PM2.5, CO2 and temperature every minute, and I want a Plotly Dash web dashboard that shows the readings and warns when CO2 is too high.

**Spec:**
```
Type:       Data dashboard (web)
Data model: Sensor(id, room_name, building, installed_at)
            Reading(id, sensor_id -> Sensor, pm25, co2_ppm, temperature_c, recorded_at)
Features:   - Receive readings from sensors over MQTT and store them
            - Show the latest readings for every room on an overview grid
            - Plot readings over time for a chosen room and date range
            - Colour rooms by CO2 level (good, moderate, poor)
            - Send an email alert when CO2 stays above 1200 ppm for 10 minutes
            - Download readings for a room as a CSV
Input:      MQTT messages from classroom sensors (JSON payloads)
Storage:    TimescaleDB (PostgreSQL)
Tech stack: Python, Plotly Dash, paho-mqtt, SQLAlchemy, TimescaleDB
```

---

## Example 436

**Intent:**
factory machines have vibration and temprature sensors streaming to kafka, need to catch anomalys in real time before machines break

**Spec:**
```
Type:       Real-time anomaly detection service
Data model: Machine(id, name, line, model)
            SensorReading(machine_id -> Machine, vibration_rms, temperature_c, recorded_at)
            Alert(id, machine_id -> Machine, metric, value, anomaly_score, created_at)
Features:   - Consume sensor readings from a Kafka topic
            - Compute rolling statistics per machine over 5-minute windows
            - Score each window with a model trained on normal operation
            - Raise an alert when the anomaly score passes a threshold
            - Publish alerts to a Kafka topic and a Slack channel
            - Retrain the baseline model weekly on recent normal data
Input:      Kafka topic with JSON sensor readings
Storage:    InfluxDB (readings), PostgreSQL (alerts)
Tech stack: Python, Faust (Kafka stream processing), scikit-learn, InfluxDB, Slack API
```

---

## Example 437

**Intent:**
pull out the invoice number, date, supplier and total from scanned pdf invoices into a spreadsheet

**Spec:**
```
Type:       Document data extraction script
Features:   - Read scanned PDF invoices from a folder
            - Convert each page to an image and run OCR
            - Extract invoice number, date, supplier name and total amount with regex and layout rules
            - Normalise dates and amounts to a standard format
            - Flag invoices where a field could not be found
            - Write one row per invoice to an Excel file
Input:      Folder of scanned PDF invoices
Tech stack: Python, Tesseract OCR (pytesseract), pdf2image, pandas, openpyxl
```

---

## Example 438

**Intent:**
Our support team gets 500 tickets a day and someone sorts them by hand into billing, technical, account and shipping. Could a model do the sorting and send each ticket to the right queue?

**Spec:**
```
Type:       Machine learning service (text classification)
Data model: Ticket(id, subject, body, predicted_category, confidence, final_category, created_at)
Features:   - Train a classifier on past tickets labelled with their queue
            - Classify new tickets into billing, technical, account or shipping
            - Send low-confidence tickets to a manual triage queue
            - Record agent corrections to use as new training data
            - Retrain the model monthly and compare it with the current one
            - Report accuracy per category on a weekly basis
API:        REST
            POST /classify
            POST /tickets/{id}/feedback
Storage:    PostgreSQL
Tech stack: Python, scikit-learn, FastAPI, pandas
```

---

## Example 439

**Intent:**
download daily weather station data from NOAA and load it into our warehouse

**Spec:**
```
Type:       Scheduled data pipeline (ETL)
Data model: Station(station_id, name, latitude, longitude, elevation, country)
            DailyObservation(station_id -> Station, date, tmax_c, tmin_c, precipitation_mm, snow_mm)
Features:   - Download the latest daily GHCN files for a list of stations from NOAA
            - Parse fixed-width records and convert tenths of units to normal units
            - Drop values with failed quality flags
            - Load new observations into the warehouse without duplicates
            - Run once a day and backfill missing dates on request
            - Log stations with no data for more than 3 days
Input:      NOAA GHCN-Daily files over HTTPS, station list CSV
Storage:    PostgreSQL (warehouse schema)
Tech stack: Python, Prefect, pandas, requests, SQLAlchemy
```

---

## Example 440

**Intent:**
our data pipelines sometimes load garbage (nulls, negative prices, dates in the future) and nobody notices until the reports look wrong. I want automatic data quality checks that stop the pipeline and tell us what failed.

**Spec:**
```
Type:       Data quality validation framework
Features:   - Define expectation suites per table: not-null, unique keys, value ranges and allowed values
            - Check that dates are not in the future and prices are not negative
            - Compare row counts with the previous load and flag big drops
            - Run checks as a step after each pipeline load
            - Stop downstream tasks when a critical check fails
            - Publish an HTML data docs report with every run's results
            - Send a Slack message listing failed checks
Input:      Tables in the data warehouse after each load
Storage:    Amazon S3 (validation results and data docs)
Tech stack: Python, Great Expectations, Apache Airflow, Slack API
```

---

## Example 441

**Intent:**
i downloaded my spotify data and wanna see my top artists, when i listen the most and how my taste changed over the years

**Spec:**
```
Type:       Data analysis script (personal data)
Features:   - Load all streaming history JSON files from the Spotify export
            - Drop plays shorter than 30 seconds
            - Rank top artists and tracks per year by listening time
            - Show a heatmap of listening by weekday and hour
            - Plot how the share of top artists changes over the years
            - Save all charts as PNG files
Input:      Spotify extended streaming history export (JSON files)
Tech stack: Python, pandas, seaborn, matplotlib
```

---

## Example 442

**Intent:**
predict which hospital patients are likely to be readmitted within 30 days after discharge

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load discharge records and join diagnoses, procedures and medications
            - Engineer features: length of stay, prior admissions, comorbidity score, age group
            - Handle class imbalance with class weights
            - Train and tune a gradient-boosted model with cross-validation
            - Report ROC AUC, recall and calibration curve on a test set
            - Explain predictions with SHAP values
            - Output a risk score per patient at discharge
Input:      De-identified CSV extracts: admissions, diagnoses, medications
Tech stack: Python, pandas, XGBoost, scikit-learn, SHAP
```

---

## Example 443

**Intent:**
I am agronomist, I want to predict the yield of maize per field using the soil data, the rain and the fertiliser we put, we have data of 8 seasons.

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Merge soil tests, rainfall and fertiliser records per field and season
            - Fill missing soil values with field averages
            - Train a random forest regressor to predict yield in tonnes per hectare
            - Validate by leaving one season out at a time
            - Show which factors affect yield the most
            - Predict yield for planned fertiliser amounts on each field
Input:      CSV files: soil_tests.csv, rainfall.csv, fertiliser.csv, yields.csv (keyed by field_id and season)
Tech stack: Python, pandas, scikit-learn, matplotlib
```

---

## Example 444

**Intent:**
compare rent prices across neighbourhoods in my city from a listings dataset

**Spec:**
```
Type:       Data analysis script
Features:   - Load rental listings and remove duplicates and obvious outliers
            - Calculate rent per square metre for each listing
            - Compare median rent by neighbourhood and number of bedrooms
            - Plot rent per square metre on a neighbourhood map
            - Show how rents changed month by month
            - Export a summary table per neighbourhood
Input:      CSV file with columns: listing_id, neighbourhood, bedrooms, size_sqm, monthly_rent, listed_date, lat, lng
Tech stack: Python, pandas, GeoPandas, Folium, matplotlib
```

---

## Example 445

**Intent:**
We trained an image classifier for product photos and now need to serve it in production with versioning so we can roll back a bad model quickly.

**Spec:**
```
Type:       Model-serving API
Auth:       API key per client service
Data model: ModelVersion(id, name, version, artefact_uri, metrics_json, status, deployed_at)
            PredictionLog(id, model_version_id -> ModelVersion, image_hash, label, confidence, latency_ms, created_at)
Features:   - Accept an image upload and return the top 5 labels with confidence
            - Load the active model version at startup and on change
            - Promote or roll back a model version with one request
            - Batch concurrent requests to use the GPU efficiently
            - Log every prediction with model version and latency
            - Expose Prometheus metrics for request rate and latency
API:        REST
            POST /predict
            GET  /models
            POST /models/{version}/activate
            GET  /health
Storage:    Amazon S3 (model artefacts), PostgreSQL (versions and logs)
Tech stack: Python, PyTorch, FastAPI, Prometheus client, Docker
```

---

## Example 446

**Intent:**
set up mlflow so my team can track experiments

**Spec:**
```
Type:       ML experiment tracking setup
Auth:       Team login through an authenticating reverse proxy
Features:   - Run a shared MLflow tracking server for the team
            - Log parameters, metrics and artefacts from training scripts
            - Compare runs side by side in the MLflow UI
            - Register the best models in the model registry with stages
            - Provide a template training script that logs automatically
Storage:    PostgreSQL (tracking backend), Amazon S3 (artefact store)
Tech stack: Python, MLflow, Docker Compose, nginx
```

---

## Example 447

**Intent:**
show unemployment rate per county on an interactive map with a slider for the year

**Spec:**
```
Type:       Data visualisation (interactive map)
Features:   - Load county unemployment data and county boundary GeoJSON
            - Join data to boundaries by FIPS code
            - Draw a choropleth map coloured by unemployment rate
            - Change the displayed year with a slider
            - Show county name and rate on hover
            - Export the map as a standalone HTML file
Input:      CSV file with columns: fips, county, state, year, unemployment_rate; county GeoJSON file
Tech stack: Python, pandas, Plotly Express
```

---

## Example 448

**Intent:**
pandas keeps running out of memory on the NYC taxi data (like 40GB of parquet), can you do it with polars instead? i need avg fare, tips and trip counts by pickup zone and hour

**Spec:**
```
Type:       Data processing script
Features:   - Scan all Parquet files lazily without loading them into memory
            - Filter out trips with zero distance, negative fares or bad timestamps
            - Join pickup zone names from the taxi zone lookup table
            - Aggregate trip count, average fare and average tip percentage by zone and hour
            - Run the query with the streaming engine to keep memory low
            - Write the aggregated table to a Parquet file
Input:      NYC TLC yellow taxi Parquet files, taxi_zone_lookup.csv
Tech stack: Python, Polars (lazy API)
```

---

## Example 449

**Intent:**
how much do sales go down when we raise the price? we have price and sales history for all products

**Spec:**
```
Type:       Statistical analysis (price elasticity)
Features:   - Load weekly price and units sold per product
            - Control for seasonality and promotions with dummy variables
            - Fit a log-log regression of units sold on price per product
            - Report the price elasticity with confidence intervals
            - Group products into elastic and inelastic
            - Simulate revenue at different price points
Input:      CSV file with columns: week, product_id, price, units_sold, on_promotion
Tech stack: Python, pandas, statsmodels, matplotlib
```

---

## Example 450

**Intent:**
forecast incoming calls per half hour for our call centre so we can plan agent shifts

**Spec:**
```
Type:       Forecasting script (time series)
Features:   - Load call history in 30-minute intervals
            - Model daily and weekly seasonality and public holidays
            - Forecast call volume per interval for the next 4 weeks
            - Convert forecast volume into required agents using Erlang C
            - Compare forecast accuracy against last year's actuals
            - Export a staffing plan to Excel
Input:      CSV file with columns: interval_start, calls_offered, avg_handle_time_sec
Tech stack: Python, pandas, statsmodels (MSTL + exponential smoothing), pyworkforce, openpyxl
```

---

## Example 451

**Intent:**
detect fake news articles

**Spec:**
```
Type:       Machine learning model (text classification)
Features:   - Load labelled real and fake news articles
            - Clean text and remove source names that leak the label
            - Fine-tune a DistilBERT model on title and body text
            - Evaluate with accuracy, F1 and a confusion matrix
            - Predict whether a pasted article is likely fake with a confidence score
Input:      CSV file with columns: title, text, label
Tech stack: Python, Hugging Face Transformers, PyTorch, pandas
```

---

## Example 452

**Intent:**
On our Q&A forum people post the same question many times. When someone writes a new question I want to show them existing questions that are basically the same before they post it.

**Spec:**
```
Type:       Semantic search service (duplicate detection)
Data model: Question(id, title, body, embedding, created_at)
Features:   - Embed all existing questions with a sentence transformer
            - Index embeddings for fast nearest-neighbour search
            - Return the 5 most similar existing questions for a new draft
            - Mark pairs above a similarity threshold as likely duplicates
            - Add new questions to the index when they are posted
API:        REST
            POST /similar
            POST /questions
Storage:    PostgreSQL (questions), FAISS index file
Tech stack: Python, sentence-transformers (all-MiniLM-L6-v2), FAISS, FastAPI
```

---

## Example 453

**Intent:**
classify bird species from short audio recordings

**Spec:**
```
Type:       Machine learning model (audio classification)
Features:   - Load labelled audio clips and resample to 32 kHz mono
            - Split recordings into 5-second windows
            - Convert windows to log-mel spectrograms
            - Train a CNN on spectrograms with noise and time-shift augmentation
            - Predict the top 3 species for a new recording
            - Report per-species precision and recall
Input:      Folder of WAV/MP3 recordings with a labels CSV (filename, species)
Tech stack: Python, PyTorch, torchaudio, librosa
```

---

## Example 454

**Intent:**
count how many cars are in our parking lot from the cctv camera snapshots every 5 min

**Spec:**
```
Type:       Computer vision script (object detection)
Data model: OccupancyRecord(id, camera_id, car_count, free_spaces, captured_at)
Features:   - Fetch a snapshot from each camera every 5 minutes
            - Detect cars with a pretrained YOLO model
            - Count cars inside the parking area polygon only
            - Calculate free spaces from the lot capacity
            - Save counts and plot occupancy by hour of day
Input:      CCTV snapshot URLs (JPEG over HTTP)
Storage:    SQLite
Tech stack: Python, Ultralytics YOLOv8, OpenCV, Shapely, matplotlib
```

---

## Example 455

**Intent:**
nps survey dashbord for our product, score over time plus what people complain about in the comments

**Spec:**
```
Type:       Data dashboard (web)
Features:   - Load NPS responses with score, comment and customer segment
            - Calculate NPS per month and per segment
            - Show promoters, passives and detractors as a stacked chart
            - Extract the most common complaint themes from detractor comments
            - Show example comments for each theme
            - Filter by date range, plan and country
Input:      CSV export from the survey tool with columns: response_id, date, score, comment, plan, country
Tech stack: Python, Streamlit, pandas, scikit-learn (TF-IDF + NMF), Plotly
```

---

## Example 456

**Intent:**
We spend on Google, Meta, TikTok and email, and last-click attribution gives all the credit to Google search. I would like a data-driven attribution model using our user journey data to see what each channel really contributes.

**Spec:**
```
Type:       Data analysis script (marketing attribution)
Features:   - Build ordered touchpoint paths per user from journey events
            - Calculate first-click, last-click and linear attribution as baselines
            - Fit a Markov chain model and compute channel removal effects
            - Calculate Shapley value attribution per channel
            - Compare credited conversions and ROI per channel across models
            - Plot channel contribution for each method
Input:      CSV file with columns: user_id, timestamp, channel, converted, conversion_value
Tech stack: Python, pandas, NumPy, matplotlib
```

---

## Example 457

**Intent:**
write sql in bigquery on our ga4 export to get weekly traffic, top landing pages and conversion by source

**Spec:**
```
Type:       SQL analysis (data warehouse queries)
Features:   - Unnest GA4 event parameters into flat session-level rows
            - Calculate weekly users, sessions and engagement rate
            - Rank top landing pages by sessions and engagement rate
            - Calculate conversion rate by traffic source and medium
            - Save results as scheduled queries that refresh every Monday
            - Connect the result tables to Looker Studio for charts
Input:      GA4 BigQuery export tables (events_*)
Storage:    Google BigQuery
Tech stack: SQL, Google BigQuery, Looker Studio
```

---

## Example 458

**Intent:**
how many users come back to our app after the first week, by signup month

**Spec:**
```
Type:       Data analysis script (cohort retention)
Features:   - Assign each user to a cohort by signup month
            - Calculate the share of each cohort active in each following week
            - Draw a retention triangle heatmap
            - Plot retention curves for recent cohorts
            - Compare week-1 and week-4 retention across cohorts
            - Export the retention table to CSV
Input:      CSV files: users.csv (user_id, signup_date), events.csv (user_id, event_date)
Tech stack: Python, pandas, seaborn
```

---

## Example 459

**Intent:**
we make metal parts and want a camera on the line to spot scratches and dents automatically, we have only few photos of defective parts

**Spec:**
```
Type:       Computer vision system (defect detection)
Data model: Inspection(id, part_serial, image_path, anomaly_score, is_defective, inspected_at)
Features:   - Capture an image of each part from the line camera
            - Train an anomaly detection model mostly on images of good parts
            - Score each new part and highlight suspected defect areas with a heatmap
            - Reject parts above a threshold and signal the PLC
            - Let operators confirm or overrule decisions to collect labels
            - Show daily defect rate on a simple dashboard
Input:      Industrial camera images (GigE camera)
Storage:    PostgreSQL (inspections), local disk (images)
Tech stack: Python, anomalib (PatchCore), PyTorch, OpenCV, Streamlit
```

---

## Example 460

**Intent:**
predict how many cycles a jet engine has left before it fails using the NASA turbofan dataset

**Spec:**
```
Type:       Machine learning model (remaining useful life regression)
Features:   - Load the C-MAPSS training and test files and name the sensor columns
            - Drop sensors with constant values
            - Calculate remaining useful life labels capped at 125 cycles
            - Build sliding windows of 30 cycles per engine
            - Train an LSTM regressor on the windows
            - Evaluate with RMSE and the NASA scoring function
            - Plot predicted vs true RUL per engine
Input:      NASA C-MAPSS text files (train_FD001.txt, test_FD001.txt, RUL_FD001.txt)
Tech stack: Python, PyTorch, pandas, NumPy, matplotlib
```

---

## Example 461

**Intent:**
loan default model with xgboost, and the bank needs to explain every decision to customers

**Spec:**
```
Type:       Machine learning model (credit risk classification)
Features:   - Load loan applications and repayment outcomes
            - Engineer features: debt-to-income, credit utilisation, payment history
            - Train an XGBoost classifier with monotonic constraints on key features
            - Tune hyperparameters with cross-validation and report ROC AUC and KS
            - Explain each decision with SHAP values
            - Generate the top 3 reason codes for every rejected application
            - Check approval rates across age and gender groups for fairness
Input:      CSV file with application fields and a defaulted label
Tech stack: Python, XGBoost, SHAP, pandas, scikit-learn
```

---

## Example 462

**Intent:**
the sales team keeps their data in google sheets, sync it every hour into postgres pls

**Spec:**
```
Type:       Scheduled data pipeline (sync)
Features:   - Read the configured tabs from the Google Sheet with a service account
            - Clean headers and convert columns to the correct types
            - Replace the matching Postgres table in a single transaction
            - Skip the load and alert when required columns are missing
            - Run every hour
            - Log row counts for each sync
Input:      Google Sheets spreadsheet ID and tab names
Storage:    PostgreSQL
Tech stack: Python, gspread, pandas, SQLAlchemy, cron
```

---

## Example 463

**Intent:**
I want my bank transactions to be auto categorised (food, rent, transport...) by a model that learns from the ones I already labelled

**Spec:**
```
Type:       Machine learning script (text classification)
Features:   - Load labelled and unlabelled transactions
            - Clean merchant descriptions by removing card numbers and reference codes
            - Train a classifier on description text and amount
            - Predict categories for unlabelled transactions with a confidence score
            - Ask the user to confirm low-confidence predictions in the terminal
            - Add confirmed labels to the training data and retrain
Input:      CSV file with columns: date, description, amount, category (empty if unlabelled)
Tech stack: Python, pandas, scikit-learn (TF-IDF + LinearSVC)
```

---

## Example 464

**Intent:**
election results dashboard in tableau by constituency

**Spec:**
```
Type:       BI dashboard
Features:   - Import results per constituency and party
            - Show a map coloured by winning party
            - Show vote share and seat count per party
            - Compare turnout and swing with the previous election
            - Filter by region and party
            - Publish the dashboard to Tableau Public
Input:      CSV files: results.csv (constituency, party, votes), constituencies boundary shapefile
Tech stack: Tableau Desktop, Tableau Public
```

---

## Example 465

**Intent:**
i want to predict football match results (home win draw away win) for the premier league from the past seasons data

**Spec:**
```
Type:       Machine learning model (multi-class classification)
Features:   - Load past match results for several seasons
            - Build features: recent form, goals scored and conceded, Elo ratings, head-to-head
            - Use only data available before each match to avoid leakage
            - Train a multinomial logistic regression and a gradient-boosted model
            - Evaluate with log loss and accuracy on the latest season
            - Predict probabilities for upcoming fixtures
Input:      CSV files of match results (date, home_team, away_team, home_goals, away_goals)
Tech stack: Python, pandas, scikit-learn, LightGBM
```

---

## Example 466

**Intent:**
help me pick my fantasy premier league team each week

**Spec:**
```
Type:       Recommendation tool (optimisation)
Features:   - Fetch player prices, form and fixtures from the Fantasy Premier League API
            - Predict expected points per player for the next gameweek
            - Pick the best 15-player squad within budget and club limits with linear programming
            - Suggest the best transfers for the current team
            - Choose captain and vice-captain
Input:      Fantasy Premier League public API, user's team ID
Tech stack: Python, requests, pandas, PuLP, scikit-learn
```

---

## Example 467

**Intent:**
For my online bookshop I want "books like this one" suggestions based on the description and genre, because we don't have many ratings yet.

**Spec:**
```
Type:       Recommendation system (content-based)
Data model: Book(id, title, author, genres, description)
            SimilarBook(book_id -> Book, similar_book_id -> Book, score)
Features:   - Combine description, genres and author into one text per book
            - Turn book texts into TF-IDF vectors
            - Find the 8 most similar books with cosine similarity
            - Remove books by the same author from results when requested
            - Precompute similar books nightly for the whole catalogue
API:        REST
            GET  /books/{id}/similar
Storage:    PostgreSQL
Tech stack: Python, scikit-learn, pandas, FastAPI
```

---

## Example 468

**Intent:**
music genre classifier from mp3 files

**Spec:**
```
Type:       Machine learning model (audio classification)
Features:   - Load labelled 30-second clips (GTZAN dataset)
            - Extract MFCC, chroma and spectral contrast features
            - Train an SVM and a random forest on the features
            - Compare models with cross-validated accuracy
            - Predict the genre of a new MP3 file
Input:      Folder of audio clips organised by genre
Tech stack: Python, librosa, scikit-learn, NumPy
```

---

## Example 469

**Intent:**
We are moving our retail reporting to Snowflake and need a proper star schema for sales, with history of product and store changes kept.

**Spec:**
```
Type:       Data warehouse (dimensional model)
Data model: DimDate(date_key, date, week, month, quarter, year, is_holiday)
            DimProduct(product_key, product_id, name, category, price, valid_from, valid_to, is_current)
            DimStore(store_key, store_id, name, region, manager, valid_from, valid_to, is_current)
            FactSales(date_key -> DimDate, product_key -> DimProduct, store_key -> DimStore, quantity, revenue, discount)
Features:   - Load raw sales and master data into a staging schema
            - Track product and store changes as slowly changing dimensions (type 2)
            - Load the fact table with surrogate keys from the dimensions
            - Load new data incrementally every night
            - Create role-based access for analysts and loaders
Input:      Daily CSV extracts from the POS system in cloud storage
Storage:    Snowflake
Tech stack: Snowflake, SQL, dbt (snapshots for SCD2), Snowpipe
```

---

## Example 470

**Intent:**
stream every change in our mysql database into the data lake in near real time

**Spec:**
```
Type:       Streaming data pipeline (change data capture)
Features:   - Capture inserts, updates and deletes from the MySQL binlog
            - Publish change events per table to Kafka topics
            - Handle schema changes with a schema registry
            - Write changes to the data lake as Delta tables with merge
            - Keep end-to-end latency under one minute
            - Monitor connector lag and alert on failure
Input:      MySQL database with binlog enabled
Storage:    Amazon S3 (Delta Lake)
Tech stack: Debezium, Apache Kafka, Confluent Schema Registry, Spark Structured Streaming, Delta Lake
```

---

## Example 471

**Intent:**
estimate how much each customer will spend with us over the next year

**Spec:**
```
Type:       Data analysis script (customer lifetime value)
Features:   - Build a recency, frequency, tenure and average spend summary per customer
            - Fit a BG/NBD model to predict future purchase counts
            - Fit a Gamma-Gamma model to predict average order value
            - Combine both models into a 12-month CLV per customer
            - Validate predictions on a held-out calibration period
            - Export customers ranked by predicted CLV
Input:      CSV file with columns: customer_id, order_date, order_value
Tech stack: Python, pandas, lifetimes, matplotlib
```

---

## Example 472

**Intent:**
I hold about 15 stocks and ETFs. I want a script that tells me the risk of my portfolio, like value at risk and max drawdown, and how correlated my holdings are.

**Spec:**
```
Type:       Data analysis script (portfolio risk)
Features:   - Load holdings and download daily adjusted prices for each ticker
            - Calculate daily returns and portfolio value over time
            - Calculate historical and parametric 1-day 95% value at risk
            - Calculate annualised volatility, Sharpe ratio and maximum drawdown
            - Show a correlation heatmap of the holdings
            - Run a Monte Carlo simulation of portfolio value over one year
Input:      CSV file with columns: ticker, shares
Tech stack: Python, pandas, NumPy, yfinance, seaborn
```

---

## Example 473

**Intent:**
jupyter notebook looking at bitcoin and ethereum volatilty over last 5 years

**Spec:**
```
Type:       Jupyter notebook (exploratory data analysis)
Features:   - Download daily OHLCV data for BTC and ETH from an exchange API
            - Calculate log returns and 30-day rolling volatility
            - Compare volatility between the two coins and with the S&P 500
            - Fit a GARCH(1,1) model to each coin's returns
            - Plot volatility regimes and the largest daily moves
Input:      Public exchange OHLCV API (via ccxt)
Tech stack: Python, Jupyter, ccxt, pandas, arch, matplotlib
```

---

## Example 474

**Intent:**
we send newsletters and want the system to automatically learn which subject line works best and send more of that one while the campaign runs

**Spec:**
```
Type:       Optimisation service (multi-armed bandit)
Data model: Campaign(id, name, started_at)
            Variant(id, campaign_id -> Campaign, subject_line, sends, opens)
Features:   - Create a campaign with several subject line variants
            - Pick a variant for each batch of emails with Thompson sampling
            - Update open counts from email provider webhooks
            - Shift sends towards the best-performing variant over time
            - Show each variant's open rate and probability of being best
API:        REST
            POST /campaigns
            GET  /campaigns/{id}/next-variant
            POST /webhooks/open
            GET  /campaigns/{id}/stats
Storage:    PostgreSQL
Tech stack: Python, FastAPI, NumPy, SendGrid webhooks
```

---

## Example 475

**Intent:**
survival analysis in R for a clinical trial, comparing time to relapse between the treatment and placebo group

**Spec:**
```
Type:       Statistical analysis (survival analysis)
Features:   - Load patient-level trial data and create survival objects
            - Plot Kaplan-Meier curves for treatment and placebo with risk tables
            - Compare groups with a log-rank test
            - Fit a Cox proportional hazards model adjusted for age and stage
            - Check the proportional hazards assumption with Schoenfeld residuals
            - Render results as a Word report
Input:      CSV file with columns: patient_id, arm, time_to_event_days, relapsed, age, stage
Tech stack: R, survival, survminer, tidyverse, R Markdown
```

---

## Example 476

**Intent:**
predict wine quality score from its chemistry

**Spec:**
```
Type:       Machine learning model (regression)
Features:   - Load the red and white wine quality datasets
            - Explore feature distributions and correlations
            - Train linear regression, random forest and gradient boosting models
            - Compare models with cross-validated RMSE
            - Show feature importance for the best model
            - Save the best model for later predictions
Input:      UCI wine quality CSV files (semicolon-separated)
Tech stack: Python, pandas, scikit-learn, seaborn
```

---

## Example 477

**Intent:**
i read a lot of research papers, make me a tool that gives a short summary of a pdf paper

**Spec:**
```
Type:       Command-line tool (text summarisation)
Features:   - Extract text from a research paper PDF
            - Detect and keep the abstract, introduction and conclusion sections
            - Split long text into chunks that fit the model's input size
            - Summarise each chunk and merge the results into one summary
            - Print a 5-bullet summary and save it as Markdown
Input:      Path to a PDF file
Tech stack: Python, PyMuPDF, Hugging Face Transformers (BART large CNN)
```

---

## Example 478

**Intent:**
which skills are most wanted in data job ads and how is it changing, i have scraped job postings

**Spec:**
```
Type:       Data analysis script (text mining)
Features:   - Load job postings and remove duplicates across job boards
            - Match skills in descriptions against a skills dictionary with aliases
            - Count skill mentions per month and per job title
            - Show the top 20 skills and the fastest-growing skills
            - Find skills that often appear together
            - Export skill counts to CSV
Input:      CSV file with columns: posting_id, title, company, description, posted_date
Tech stack: Python, pandas, spaCy (PhraseMatcher), matplotlib
```

---

## Example 479

**Intent:**
using geopandas find the road accident hotspots in our city from the police accident data

**Spec:**
```
Type:       Geospatial analysis script
Features:   - Load accident records and convert coordinates to points
            - Reproject points to a metric coordinate system
            - Find accident clusters with DBSCAN
            - Snap accidents to road segments and count accidents per kilometre
            - Rank the top 20 hotspots by count and severity
            - Draw hotspots on an interactive map
Input:      CSV file with columns: accident_id, date, severity, latitude, longitude; road network from OpenStreetMap
Tech stack: Python, GeoPandas, OSMnx, scikit-learn, Folium
```

---

## Example 480

**Intent:**
Classify satellite images into land cover types (forest, water, farmland, urban) for a region so we can track deforestation from year to year.

**Spec:**
```
Type:       Machine learning model (remote sensing classification)
Features:   - Download cloud-free Sentinel-2 images for the region and years
            - Calculate NDVI and other spectral indices per pixel
            - Train a random forest on labelled training polygons
            - Classify every pixel into a land cover class
            - Compare forest area between years and map forest loss
            - Export classified maps as GeoTIFF files
Input:      Sentinel-2 imagery, training polygons as a GeoJSON file
Tech stack: Python, Google Earth Engine Python API, rasterio, scikit-learn, GeoPandas
```

---

## Example 481

**Intent:**
our ml models each compute the same customer features in different ways, we need one feature store

**Spec:**
```
Type:       ML feature store
Data model: Entity(name, join_key)
            FeatureView(name, entity -> Entity, features, source_table, ttl)
Features:   - Define customer features once as code in a shared repository
            - Materialise features from the warehouse to an online store on a schedule
            - Serve the latest feature values for a customer at low latency
            - Build point-in-time correct training sets from historical feature values
            - Track which models use which features
Input:      Feature source tables in the data warehouse
Storage:    BigQuery (offline store), Redis (online store)
Tech stack: Python, Feast, BigQuery, Redis, Apache Airflow
```

---

## Example 482

**Intent:**
a simple web tool where my team can draw boxes on images to label them for training an object detection model

**Spec:**
```
Type:       Web application (data labelling tool)
Auth:       Team login (email + password)
Data model: User(id, email, password_hash)
            Project(id, name, label_classes)
            Image(id, project_id -> Project, file_path, status, assigned_to -> User)
            Annotation(id, image_id -> Image, label, x, y, width, height, created_by -> User)
Features:   - Upload a folder of images to a project
            - Draw, move and resize bounding boxes and choose a label
            - Assign images to team members and track progress
            - Review and approve other people's annotations
            - Export annotations in COCO and YOLO formats
API:        REST
            POST /projects/{id}/images
            GET  /images/{id}
            POST /images/{id}/annotations
            GET  /projects/{id}/export?format={coco|yolo}
Storage:    PostgreSQL, local disk or S3 (images)
Tech stack: Python, FastAPI, React, Konva.js
```

---

## Example 483

**Intent:**
need fake but realistic customer and order data to test our pipeline, cannot use the production data

**Spec:**
```
Type:       Command-line script (synthetic data generation)
Data model: Customer(id, name, email, city, signup_date)
            Order(id, customer_id -> Customer, order_date, total, status)
Features:   - Generate realistic customers with names, emails and addresses
            - Generate orders with seasonal patterns and realistic totals
            - Keep foreign keys valid between customers and orders
            - Set the number of rows and a random seed from the command line
            - Write the output as CSV or Parquet files
Input:      Command-line options: --customers, --orders, --seed, --format
Tech stack: Python, Faker, NumPy, pandas, pyarrow
```

---

## Example 484

**Intent:**
government publishes stats only in pdf reports with tables, i want to get those tables out into csv each month

**Spec:**
```
Type:       Command-line script (PDF table extraction)
Features:   - Download the latest monthly PDF report from the publication page
            - Detect and extract tables from the configured pages
            - Fix merged header rows and numbers with thousands separators
            - Append the month's data to a combined CSV file
            - Warn when the table layout changes and extraction looks wrong
Input:      URL of the PDF report page, page numbers config
Tech stack: Python, Camelot, requests, BeautifulSoup, pandas
```

---

## Example 485

**Intent:**
Every night we need to score all active customers with the latest approved model and write the scores back to the warehouse so the CRM can use them.

**Spec:**
```
Type:       Scheduled batch scoring pipeline
Features:   - Fetch the latest production model from the model registry
            - Extract features for all active customers from the warehouse
            - Score customers in batches and attach the model version
            - Write scores to a warehouse table partitioned by date
            - Check score distribution against the previous night and alert on large shifts
            - Retry failed tasks and notify the team on final failure
Input:      Customer feature tables in the warehouse, MLflow model registry
Storage:    Snowflake
Tech stack: Python, Apache Airflow, MLflow, pandas, snowflake-connector-python
```

---

## Example 486

**Intent:**
how do i know when my model in production starts going bad because the data changed

**Spec:**
```
Type:       Model monitoring service
Features:   - Collect production inputs and predictions from the prediction logs daily
            - Compare feature distributions with the training data using drift tests
            - Track prediction distribution and, when labels arrive, accuracy over time
            - Generate an HTML drift report each day
            - Send an alert when drift passes a set threshold
Input:      Training dataset (reference) and daily prediction logs
Storage:    PostgreSQL (metrics history), S3 (reports)
Tech stack: Python, Evidently, pandas, Grafana, Apache Airflow
```

---

## Example 487

**Intent:**
we have 120 stores, need weekly sales forecast for every store and department, lightgbm maybe

**Spec:**
```
Type:       Forecasting pipeline (multi-series)
Features:   - Load weekly sales per store and department with holidays and promotions
            - Build lag, rolling mean and calendar features
            - Train one global LightGBM model across all store-department series
            - Forecast the next 8 weeks with a recursive strategy
            - Evaluate with weighted MAE on the last 8 weeks of history
            - Export forecasts per store and department to CSV
Input:      CSV files: sales.csv (store, dept, week, sales), stores.csv, holidays.csv
Tech stack: Python, LightGBM, pandas, scikit-learn
```

---

## Example 488

**Intent:**
hotel want to know which bookings will be cancelled so we can overbook a little

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load booking history with lead time, channel, deposit type and season
            - Remove columns only known after cancellation to avoid leakage
            - Train a classifier to predict cancellation probability
            - Evaluate with ROC AUC and a calibration curve
            - Estimate expected cancellations per arrival date
            - Suggest a safe overbooking number per night
Input:      CSV file of past bookings with an is_canceled column
Tech stack: Python, pandas, CatBoost, scikit-learn
```

---

## Example 489

**Intent:**
sales funnel report from salesforce export, where do we lose deals

**Spec:**
```
Type:       Data analysis report
Features:   - Load opportunity history from the Salesforce export
            - Calculate conversion rates between each pipeline stage
            - Calculate average days spent in each stage
            - Compare win rate by sales rep, lead source and deal size
            - Draw a funnel chart for each quarter
            - Export a summary to Excel
Input:      Salesforce report exports (Opportunity and OpportunityHistory CSVs)
Tech stack: Python, pandas, Plotly, openpyxl
```

---

## Example 490

**Intent:**
every week pull our google ads spend and conversions and make a report with roas per campaign, emailed to the marketing team

**Spec:**
```
Type:       Scheduled reporting script
Features:   - Fetch last week's spend, clicks and conversions per campaign from the Google Ads API
            - Calculate CPC, conversion rate, cost per conversion and ROAS
            - Compare each metric with the week before
            - Build an HTML email with a summary table and a chart
            - Email the report to the marketing team every Monday morning
Input:      Google Ads API credentials and customer ID
Tech stack: Python, google-ads, pandas, matplotlib, Jinja2, smtplib
```

---

## Example 491

**Intent:**
I designed a questionnaire with 30 likert items for my master thesis, i need check reliability and if the items group into the factors I expected, in R please

**Spec:**
```
Type:       Statistical analysis (psychometrics)
Features:   - Load questionnaire responses and reverse-score negative items
            - Calculate Cronbach's alpha and McDonald's omega per scale
            - Run exploratory factor analysis with parallel analysis
            - Run confirmatory factor analysis for the expected factor model
            - Report fit indices (CFI, TLI, RMSEA) and factor loadings
            - Export APA-style tables
Input:      CSV or SPSS (.sav) file with one column per item
Tech stack: R, psych, lavaan, haven, tidyverse
```

---

## Example 492

**Intent:**
track what reddit says about our brand daily and show if mood is getting better or worse

**Spec:**
```
Type:       Data pipeline and dashboard (social listening)
Data model: Mention(id, subreddit, author, text, score, created_at, sentiment, sentiment_score)
Features:   - Search Reddit daily for posts and comments mentioning the brand
            - Remove duplicates and posts from excluded subreddits
            - Score each mention's sentiment with a pretrained model
            - Show daily mention count and average sentiment on a dashboard
            - List the most upvoted negative mentions
Input:      Reddit API (brand keywords list)
Storage:    SQLite
Tech stack: Python, PRAW, Hugging Face Transformers, Streamlit, pandas
```

---

## Example 493

**Intent:**
find duplicate and near duplicate images in my dataset before training

**Spec:**
```
Type:       Command-line script (dataset cleaning)
Features:   - Scan a folder of images recursively
            - Find exact duplicates by file hash
            - Find near duplicates with perceptual hashing
            - Find visually similar images with CLIP embeddings and a similarity threshold
            - Write a report of duplicate groups with thumbnails
            - Move duplicates to a separate folder on request
Input:      Path to an image folder
Tech stack: Python, imagehash, Pillow, open_clip, FAISS
```

---

## Example 494

**Intent:**
We still receive paper application forms filled in by hand. I want to scan them and get the fields (name, date of birth, address, signature yes/no) into our database without typing.

**Spec:**
```
Type:       Document processing pipeline (handwriting OCR)
Data model: Form(id, scan_path, status, uploaded_at)
            ExtractedField(id, form_id -> Form, field_name, value, confidence, corrected_value)
Features:   - Align each scanned form to the blank template
            - Crop each field region using template coordinates
            - Recognise handwritten text with a handwriting OCR model
            - Detect whether the signature box is filled
            - Send fields with low confidence to a review screen for correction
            - Save confirmed values to the database
Input:      Scanned forms as PDF or JPEG
Storage:    PostgreSQL
Tech stack: Python, OpenCV, Hugging Face Transformers (TrOCR), FastAPI, React
```

---

## Example 495

**Intent:**
train intent classifier for our bank chatbot, things like check balance, block card, talk to human

**Spec:**
```
Type:       Machine learning model (intent classification)
Features:   - Load labelled example utterances for each intent
            - Augment training data with paraphrases
            - Fine-tune a small BERT model for intent classification
            - Return a fallback intent when confidence is below a threshold
            - Evaluate per-intent precision and recall
            - Serve predictions to the chatbot over HTTP
API:        REST
            POST /intent
Tech stack: Python, Hugging Face Transformers, PyTorch, FastAPI
```

---

## Example 496

**Intent:**
used car price predictor, you type make model year mileage and it tells the fair price

**Spec:**
```
Type:       Web application (ML prediction)
Features:   - Train a regression model on used car listings
            - Show a form for make, model, year, mileage, fuel type and gearbox
            - Predict a fair price with a low-high range
            - Show how mileage and age affect the price for the chosen model
            - Retrain the model when new listings data is added
Input:      CSV file of car listings with columns: make, model, year, mileage, fuel, gearbox, price
Tech stack: Python, CatBoost, pandas, Streamlit
```

---

## Example 497

**Intent:**
predict if a flight will be delayed more than 15 min

**Spec:**
```
Type:       Machine learning model (classification)
Features:   - Load historical flight records and join weather at the origin airport
            - Build features: airline, route, scheduled hour, weekday, month, weather
            - Train a gradient-boosted classifier on past years
            - Evaluate on the most recent year with ROC AUC
            - Show delay probability by airline and hour of day
Input:      BTS on-time performance CSV files, NOAA hourly weather data
Tech stack: Python, pandas, XGBoost, scikit-learn, matplotlib
```

---

## Example 498

**Intent:**
want to see wikipedia pageviews trends for a list of topics, which got popular and when

**Spec:**
```
Type:       Data analysis script (trend analysis)
Features:   - Read a list of article titles
            - Fetch daily pageviews for each article from the Wikimedia API
            - Smooth series with a 7-day rolling average
            - Detect spikes and the dates they happened
            - Plot all topics on one interactive chart
Input:      Text file with one Wikipedia article title per line
Tech stack: Python, requests, pandas, Plotly
```

---

## Example 499

**Intent:**
each of our 12 branches send monthly excel with diffrent column names, need to merge all into one report using pandas

**Spec:**
```
Type:       Data processing script (consolidation)
Features:   - Read every branch Excel file from a monthly folder
            - Map each branch's column names to one standard schema
            - Check for missing columns and wrong data types per file
            - Combine all branches into one table with a branch column
            - Build summary pivot tables by branch and category
            - Write the combined data and summaries to one Excel workbook
Input:      Folder of Excel files (.xlsx), column mapping YAML file
Tech stack: Python, pandas, openpyxl, PyYAML
```

---

## Example 500

**Intent:**
Before we share our support data with the analytics vendor we must remove personal information like names, emails, phone numbers and card numbers from the text fields and also the columns.

**Spec:**
```
Type:       Data processing pipeline (PII anonymisation)
Features:   - Detect names, emails, phone numbers, addresses and card numbers in free text
            - Replace detected values with type placeholders like <EMAIL>
            - Hash customer IDs with a secret salt so records can still be joined
            - Drop or generalise direct identifier columns (birth date to year)
            - Write an audit report of what was found and removed per column
            - Process large files in chunks
Input:      CSV or Parquet files of support tickets
Tech stack: Python, Microsoft Presidio, spaCy, pandas
```

---

## Example 501

**Intent:**
find which products are bought together in our supermarket receipts

**Spec:**
```
Type:       Data analysis script (market basket analysis)
Features:   - Load receipt line items and group them into baskets
            - Convert baskets to a one-hot encoded transaction matrix
            - Find frequent itemsets with FP-Growth
            - Generate association rules with support, confidence and lift
            - Filter rules by minimum lift and show the top 30
            - Draw a network graph of strongly linked products
Input:      CSV file with columns: receipt_id, product_name, quantity
Tech stack: Python, pandas, mlxtend, NetworkX
```

---

## Example 502

**Intent:**
live dashboard of orders per minute and revenue as they come in, orders are already in kafka

**Spec:**
```
Type:       Real-time analytics dashboard
Features:   - Consume order events from a Kafka topic
            - Aggregate orders and revenue in 1-minute tumbling windows
            - Push live updates to the browser
            - Show orders per minute, revenue today and top products
            - Compare today's numbers with the same time last week
API:        REST + WebSocket
            GET  /metrics/today
            WS   /metrics/live
Storage:    ClickHouse
Tech stack: Apache Flink, ClickHouse, Kafka, Python, FastAPI, Grafana
```

---

## Example 503

**Intent:**
the city wants detect potholes from dashcam videos of garbage trucks and put them on a map

**Spec:**
```
Type:       Computer vision pipeline (object detection)
Data model: Video(id, truck_id, file_path, recorded_at)
            Pothole(id, video_id -> Video, latitude, longitude, confidence, image_path, detected_at)
Features:   - Extract frames from dashcam videos at 2 frames per second
            - Detect potholes in frames with a fine-tuned YOLO model
            - Match each detection to GPS position from the video's GPS log
            - Merge detections of the same pothole from different trips
            - Show potholes on a web map with photos and confidence
Input:      Dashcam MP4 videos with GPS track files (GPX)
Storage:    PostGIS
Tech stack: Python, Ultralytics YOLOv8, OpenCV, gpxpy, PostGIS, Leaflet
```

---

## Example 504

**Intent:**
api that checks if a forum comment is toxic before posting

**Spec:**
```
Type:       Model-serving API (text moderation)
Auth:       API key per client app
Features:   - Score a comment for toxicity, insults, threats and hate
            - Return allow, review or block based on configurable thresholds
            - Handle batches of up to 100 comments per request
            - Log decisions and scores for moderator review
            - Return results in under 100 ms on CPU
API:        REST
            POST /moderate
            POST /moderate/batch
Storage:    PostgreSQL (moderation logs)
Tech stack: Python, Detoxify, ONNX Runtime, FastAPI
```

---

## Example 505

**Intent:**
I teach a stats class and want a Jupyter notebook that explains linear regression step by step with real data and interactive sliders.

**Spec:**
```
Type:       Jupyter notebook (teaching material)
Features:   - Load a simple real dataset (advertising spend vs sales)
            - Explain least squares with markdown and formulas
            - Let students change slope and intercept with sliders and see the error change
            - Fit the model with statsmodels and explain the summary table
            - Show residual plots and explain the regression assumptions
            - Include short exercises with hidden solutions
Input:      CSV dataset bundled with the notebook
Tech stack: Python, Jupyter, ipywidgets, statsmodels, matplotlib
```

---

## Example 506

**Intent:**
I want to make a little tower defense game in the browser where you place turrets along a path and waves of enemies come at you

**Spec:**
```
Type:       Browser game (2D)
Features:   - Draw a map with a fixed enemy path on a tile grid
            - Spawn waves of enemies that follow the path with rising health and speed
            - Place, upgrade and sell turrets on free tiles using earned gold
            - Target the nearest enemy in range and fire projectiles automatically
            - Lose a life when an enemy reaches the end and end the game at zero lives
            - Save the highest wave reached between sessions
Storage:    Browser localStorage (best wave)
Tech stack: TypeScript, Phaser 3, Vite
```

---

## Example 507

**Intent:**
a sudoku app for my phone

**Spec:**
```
Type:       Mobile game (puzzle)
Data model: Puzzle(id, difficulty, givens, solution)
            GameState(puzzle_id -> Puzzle, current_grid, notes, elapsed_seconds, mistakes)
Features:   - Generate puzzles with a unique solution at easy, medium and hard levels
            - Enter numbers and pencil notes into cells
            - Highlight conflicting numbers in the same row, column and box
            - Give a hint that fills one correct cell
            - Resume an unfinished game after the app is closed
            - Show best times per difficulty
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, Dart, sqflite
```

---

## Example 508

**Intent:**
make a 2D platformer in godot with double jump and collectible coins

**Spec:**
```
Type:       Desktop game (2D platformer)
Features:   - Move the player with run, jump and double jump using CharacterBody2D physics
            - Build levels from a TileMap with platforms, spikes and moving platforms
            - Collect coins and show the coin count on a HUD
            - Respawn the player at the last checkpoint after falling or touching spikes
            - Unlock the next level when the player reaches the exit flag
            - Save unlocked levels and best coin counts to a file
Storage:    Local save file (user://save.json)
Tech stack: Godot 4, GDScript
```

---

## Example 509

**Intent:**
wnat a discord bot that runs trivia quizes in my server and keeps score

**Spec:**
```
Type:       Discord bot (game)
Data model: Question(id, category, question, correct_answer, wrong_answers)
            Player(discord_user_id, guild_id, total_points, correct_count)
            Round(id, guild_id, channel_id, question_id -> Question, started_at)
Features:   - Start a trivia round with a slash command and a chosen category
            - Post a question with four answer buttons and a 20-second timer
            - Award points to the first correct answer and reveal the answer when time runs out
            - Show a server leaderboard with a slash command
            - Load questions from the Open Trivia DB API with a local fallback list
Storage:    SQLite
Tech stack: Python, discord.py, aiosqlite, Open Trivia DB API
```

---

## Example 510

**Intent:**
I'd like to build an online game like Pictionary where one player draws a secret word and everyone else in the room tries to guess it in the chat. Each player should take turns drawing, guesses closer to the start of the round should get more points, and rooms should be joinable with a short code so friends can play together.

**Spec:**
```
Type:       Multiplayer browser game (real-time)
Data model: Room(code, host_id, round_count, current_drawer_id, status)
            Player(id, room_code -> Room, nickname, score)
            Word(id, text, difficulty)
Features:   - Create a room and join it with a short code and nickname
            - Rotate the drawer each round and give them three words to choose from
            - Stream brush strokes from the drawer's canvas to all players in real time
            - Check chat guesses against the word and hide correct guesses from others
            - Score guessers by how fast they answer and the drawer by how many guessed
            - Show the final scoreboard after the last round
API:        WebSocket
            WS   /rooms/{code}
Storage:    In-memory room state on the server, word list in a JSON file
Tech stack: Node.js, Socket.IO, HTML Canvas, JavaScript
```

---

## Example 511

**Intent:**
I am wanting to make one memory card matching game for my small daughter to learn animals names

**Spec:**
```
Type:       Educational game (kids, tablet browser)
Features:   - Show a grid of face-down cards with pairs of animal pictures
            - Flip two cards on tap and keep them open when they match
            - Play the animal's name and sound when a pair is matched
            - Choose a grid size of 2x3, 3x4 or 4x4 for different ages
            - Show a celebration animation with stars when all pairs are found
Storage:    Browser localStorage (chosen grid size and stars earned)
Tech stack: HTML, CSS, JavaScript, Howler.js (audio)
```

---

## Example 512

**Intent:**
a clicker game where you mine ore and buy upgrades, kind of like cookie clicker

**Spec:**
```
Type:       Browser game (idle/clicker)
Data model: SaveState(ore, total_ore_mined, pickaxe_level, upgrades_owned, last_saved_at)
            Upgrade(id, name, base_cost, cost_multiplier, ore_per_second)
Features:   - Mine ore by clicking the rock
            - Buy upgrades like drills and miners that produce ore per second
            - Raise each upgrade's price after every purchase
            - Calculate offline earnings from the time since the last save
            - Unlock achievements at ore milestones
            - Auto-save every 30 seconds and export the save as a text string
Storage:    Browser localStorage
Tech stack: JavaScript, Vue 3, break_infinity.js (large numbers)
```

---

## Example 513

**Intent:**
online chess with friends

**Spec:**
```
Type:       Multiplayer web game (turn-based)
Auth:       User registration and login (email + password, JWT)
Data model: User(id, username, email, password_hash, rating)
            Game(id, white_id -> User, black_id -> User, fen, pgn, status, time_control)
            Invite(id, from_id -> User, to_id -> User, status)
Features:   - Invite a friend to a game with a chosen time control
            - Validate moves and detect check, checkmate and stalemate
            - Sync moves and clocks between both players in real time
            - Offer draws and resign
            - Show past games with a move-by-move replay
API:        REST + WebSocket
            POST /signup
            POST /login
            POST /invites
            GET  /games/{id}
            WS   /games/{id}/live
Storage:    PostgreSQL
Tech stack: Node.js, Express, Socket.IO, chess.js, React, chessboard.jsx
```

---

## Example 514

**Intent:**
a endless runner for android made in unity

**Spec:**
```
Type:       Mobile game (3D endless runner)
Features:   - Run forward automatically and switch between three lanes with swipes
            - Jump and slide over or under obstacles with swipe up and down
            - Spawn track chunks with obstacles and coins procedurally ahead of the player
            - Increase running speed over time
            - Spend collected coins on character skins in a shop
            - Show distance score and personal best on the game over screen
Storage:    Local save file (PlayerPrefs for settings, JSON for coins and skins)
Tech stack: Unity, C#, Unity Input System, Android build
```

---

## Example 515

**Intent:**
text adventure game in python taht runs in the terminal with rooms and items

**Spec:**
```
Type:       Terminal game (text adventure)
Data model: Room(id, name, description, exits, item_ids)
            Item(id, name, description, can_take)
            Player(current_room_id -> Room, inventory)
Features:   - Parse typed commands like go north, take lamp, use key and look
            - Describe the current room, its exits and visible items
            - Pick up, drop and use items from the inventory
            - Unlock doors and paths when the right item is used
            - Save and load the game to a file
Input:      World definition file (rooms.json) and typed player commands
Storage:    Local JSON save file
Tech stack: Python 3 (standard library only)
```

---

## Example 516

**Intent:**
a leaderboard backend for my mobile game so players can submit scores and see the top ones

**Spec:**
```
Type:       REST API service (game backend)
Auth:       API key per game build plus anonymous player ID issued on first launch
Data model: Player(id, display_name, country, created_at)
            Score(id, player_id -> Player, leaderboard_id -> Leaderboard, value, submitted_at)
            Leaderboard(id, name, sort_order, reset_period)
Features:   - Submit a score and keep only each player's best per leaderboard
            - Return the global top 100 for a leaderboard
            - Return a player's rank and the scores around them
            - Reset daily and weekly leaderboards on a schedule
            - Reject impossible scores above a per-leaderboard limit
API:        REST
            POST /players
            POST /leaderboards/{id}/scores
            GET  /leaderboards/{id}/top?limit={n}
            GET  /leaderboards/{id}/players/{player_id}
Storage:    Redis sorted sets (rankings), PostgreSQL (players and score history)
Tech stack: Go, Gin, Redis, PostgreSQL
```

---

## Example 517

**Intent:**
a VR escape room for the Quest headset

**Spec:**
```
Type:       VR game (standalone headset)
Features:   - Grab, rotate and throw objects with hand controllers
            - Solve linked puzzles like keypads, hidden keys and lever sequences
            - Give hints from an in-world notebook after a set time
            - Move with teleport or smooth locomotion and snap turning
            - Count down a 30-minute timer and show the escape time at the end
Storage:    Local save file (best escape time per room)
Tech stack: Unity, C#, XR Interaction Toolkit, Meta XR SDK
```

---

## Example 518

**Intent:**
I need a level editor for my tile-based puzzle game so my designer can build levels without touching code. It should let her paint tiles on a grid, place enemies and items with properties, and test the level right away. Levels need to be saved as JSON that the game already loads.

**Spec:**
```
Type:       Desktop application (game level editor)
Data model: Level(id, name, width, height, tile_layers, entities)
            Entity(id, type, x, y, properties)
            Tileset(id, image_path, tile_size, tile_names)
Features:   - Paint and erase tiles on multiple layers with brush, fill and rectangle tools
            - Place enemies and items and edit their properties in a side panel
            - Undo and redo every edit
            - Launch a play-test of the current level in the game
            - Validate that every level has exactly one start and one exit
            - Save and load levels as JSON in the game's format
Storage:    Local JSON files (one per level)
Tech stack: C#, .NET 8, Avalonia UI
```

---

## Example 519

**Intent:**
Please make game where kids practice multiplication tables and get stars for right answer

**Spec:**
```
Type:       Educational game (kids, web)
Data model: Profile(id, name, avatar)
            Progress(profile_id -> Profile, table_number, stars, best_streak)
Features:   - Choose a multiplication table from 1 to 12 or a mixed mode
            - Ask timed questions with large number buttons for answers
            - Give a star for each correct answer and show the right answer after a mistake
            - Repeat questions the child got wrong more often
            - Show a progress chart of stars per table for each child
Storage:    Browser IndexedDB
Tech stack: React, TypeScript, Dexie.js
```

---

## Example 520

**Intent:**
breakout clone using pygame

**Spec:**
```
Type:       Desktop game (2D arcade)
Features:   - Move the paddle with the arrow keys or mouse
            - Bounce the ball off walls, the paddle and bricks with angle based on hit position
            - Break bricks that need one, two or three hits
            - Drop power-ups like wider paddle and multi-ball from broken bricks
            - Load the next level layout when all bricks are cleared
            - Save the high score to a file
Storage:    Local JSON file (high score)
Tech stack: Python, Pygame
```

---

## Example 521

**Intent:**
a wordle-style game but you guess countries from their outline shape

**Spec:**
```
Type:       Browser game (daily puzzle)
Data model: Country(code, name, outline_svg, lat, lon)
            DailyPuzzle(date, country_code -> Country)
Features:   - Show the outline of the day's mystery country
            - Autocomplete country names when typing a guess
            - Show distance and direction from each wrong guess to the answer
            - Allow six guesses and reveal the country on the map at the end
            - Track streaks and guess distribution
            - Copy an emoji summary of the result to share
Storage:    Static JSON (countries and schedule), browser localStorage (stats)
Tech stack: Svelte, TypeScript, D3-geo, Natural Earth data
```

---

## Example 522

**Intent:**
multiplayer uno card game online with rooms where me and friends can play from our phones

**Spec:**
```
Type:       Multiplayer web game (card game)
Data model: Room(code, host_id, status, direction, current_turn_player_id)
            Player(id, room_code -> Room, nickname, hand)
            Pile(room_code -> Room, draw_pile, discard_pile)
Features:   - Create a private room and share its code with friends
            - Deal seven cards to each of 2-8 players and shuffle the deck on the server
            - Validate plays by color, number and action cards like skip, reverse and draw four
            - Prompt the player to call UNO and penalize them if they forget
            - Reconnect a player to their hand after a dropped connection
API:        WebSocket
            WS   /rooms/{code}
Storage:    In-memory game state on the server
Tech stack: Node.js, Colyseus, React (mobile-friendly UI)
```

---

## Example 523

**Intent:**
pub quiz app for hosting trivia nights

**Spec:**
```
Type:       Web application (live quiz hosting)
Auth:       Host login (email + password); teams join with a code
Data model: Host(id, email, password_hash)
            Quiz(id, host_id -> Host, title)
            Question(id, quiz_id -> Quiz, round, text, answer, points)
            Team(id, quiz_id -> Quiz, name)
            Answer(id, team_id -> Team, question_id -> Question, text, is_correct)
Features:   - Build a quiz with rounds and questions
            - Let teams join from their phones with a quiz code
            - Push each question to all teams when the host reveals it
            - Let the host mark answers correct and adjust points
            - Show a live scoreboard on a projector view
API:        REST + WebSocket
            POST /quizzes
            POST /quizzes/{id}/teams
            POST /questions/{id}/answers
            WS   /quizzes/{id}/live
Storage:    PostgreSQL
Tech stack: Python, Django, Django Channels, HTMX
```

---

## Example 524

**Intent:**
a top down roguelike dungeon crawler in love2d

**Spec:**
```
Type:       Desktop game (2D roguelike)
Features:   - Generate a new dungeon of rooms and corridors on each floor
            - Move and attack on a turn-based grid with field of view
            - Spawn monsters that chase the player using A* pathfinding
            - Pick up potions, weapons and scrolls into a limited inventory
            - Delete the run on death and record it in a run history
            - Descend stairs to deeper floors with harder monsters
Storage:    Local save file (run history)
Tech stack: Lua, LÖVE (love2d), rotLove
```

---

## Example 525

**Intent:**
an interactive choose-your-own-adventure story app where readers pick what happens next and writers can publish their stories

**Spec:**
```
Type:       Web application (interactive fiction)
Auth:       User registration and login (email + password, OAuth with Google)
Data model: User(id, username, email, password_hash)
            Story(id, author_id -> User, title, summary, start_node_id, published)
            Node(id, story_id -> Story, text, image_url)
            Choice(id, from_node_id -> Node, to_node_id -> Node, label)
            ReadingProgress(user_id -> User, story_id -> Story, node_id -> Node)
Features:   - Write stories as passages connected by choices in a visual node editor
            - Publish stories and browse them by genre and popularity
            - Read a story one passage at a time and pick a choice to continue
            - Save reading progress and allow going back one step
            - Show which endings a reader has unlocked
API:        REST
            GET  /stories
            POST /stories
            GET  /stories/{id}/nodes/{node_id}
            PUT  /progress/{story_id}
Storage:    PostgreSQL, S3 (images)
Tech stack: Next.js, TypeScript, Prisma, React Flow
```

---

## Example 526

**Intent:**
an AR app that lets kids find hidden virtual animals around the house

**Spec:**
```
Type:       Mobile AR game (kids)
Data model: Animal(id, name, model_file, fact_text)
            Found(animal_id -> Animal, found_at)
Features:   - Detect floors and tables with plane detection
            - Hide 3D animals on random detected surfaces around the room
            - Play a sound hint that gets louder as the phone gets closer
            - Catch an animal by tapping it and show a fun fact
            - Fill a sticker album with every animal found
Storage:    Local on-device storage (album progress)
Tech stack: Unity, C#, AR Foundation (ARKit and ARCore)
```

---

## Example 527

**Intent:**
I play a lot of modded Minecraft and managing mods by hand is a pain. I want a desktop tool that lets me create separate profiles, search and download mods from Modrinth, and automatically pull in their dependencies. It should also warn me when a mod doesn't match the Minecraft or loader version.

**Spec:**
```
Type:       Desktop application (mod manager)
Data model: Profile(id, name, minecraft_version, loader, loader_version, folder_path)
            InstalledMod(id, profile_id -> Profile, project_id, version_id, file_name, enabled)
Features:   - Create profiles with their own Minecraft version, loader and mods folder
            - Search mods on Modrinth and install a chosen version into a profile
            - Resolve and install required dependencies automatically
            - Warn when a mod version does not support the profile's game or loader version
            - Check installed mods for updates and update them in one click
            - Enable or disable mods without deleting the files
API:        REST (client of the Modrinth API)
            GET  /v2/search?query={text}&facets={filters}
            GET  /v2/project/{id}/version
Storage:    Local SQLite database, mod files in each profile folder
Tech stack: Tauri, Rust, TypeScript, React
```

---

## Example 528

**Intent:**
I want make a game of tic tac toe that play against computer and it is never losing

**Spec:**
```
Type:       Browser game (board game)
Features:   - Draw a 3x3 board and let the player place X by clicking
            - Pick the computer's move with the minimax algorithm so it never loses
            - Let the player choose to go first or second
            - Detect wins and draws and highlight the winning line
            - Keep a running count of wins, losses and draws
Storage:    Browser localStorage (score counts)
Tech stack: HTML, CSS, JavaScript
```

---

## Example 529

**Intent:**
a typing speed game where words fall from the sky and you have to type them before they hit the ground

**Spec:**
```
Type:       Browser game (typing)
Features:   - Drop words from the top of the screen at increasing speed
            - Lock onto the word that matches the first typed letters and destroy it when finished
            - Lose a shield when a word reaches the ground and end the game at zero
            - Show words per minute and accuracy after each game
            - Choose word lists for easy, medium and programming terms
            - Save the top ten scores
Storage:    Browser localStorage (top scores)
Tech stack: TypeScript, PixiJS
```

---

## Example 530

**Intent:**
a crossword puzzle generator

**Spec:**
```
Type:       Web application (puzzle generator)
Data model: WordClue(word, clue)
            Puzzle(id, title, grid, placements, created_at)
Features:   - Accept a list of words and clues from the user
            - Place words on a grid with backtracking to maximize crossings
            - Number the grid and split clues into across and down
            - Let people solve the puzzle in the browser with answer checking
            - Export a printable PDF with the empty grid and clues
Input:      List of word and clue pairs (typed in or uploaded as CSV)
Storage:    SQLite (saved puzzles)
Tech stack: Python, Flask, ReportLab, JavaScript
```

---

## Example 531

**Intent:**
a 3D marble maze game in the browser with three.js where you tilt the board to roll the ball

**Spec:**
```
Type:       Browser game (3D)
Features:   - Render a 3D maze board with walls, holes and a goal
            - Tilt the board with the mouse, arrow keys or phone gyroscope
            - Roll the marble with realistic physics and collisions
            - Restart the level when the marble falls into a hole
            - Time each level and unlock the next one on completion
            - Store best times per level
Storage:    Browser localStorage (unlocked levels and best times)
Tech stack: JavaScript, Three.js, cannon-es (physics)
```

---

## Example 532

**Intent:**
a bot for discord that lets ppl play blackjack with fake coins

**Spec:**
```
Type:       Discord bot (card game)
Data model: Wallet(discord_user_id, guild_id, coins, last_daily_claim)
            Hand(id, discord_user_id, player_cards, dealer_cards, bet, status)
Features:   - Start a blackjack hand with a bet using a slash command
            - Show cards in an embed with Hit, Stand and Double buttons
            - Play the dealer automatically and stand on 17
            - Pay out wins and blackjacks and update the wallet
            - Give a free daily coin bonus and show a richest-players list
Storage:    SQLite
Tech stack: Node.js, discord.js, better-sqlite3
```

---

## Example 533

**Intent:**
a battle royale io game like agar.io where you're a blob eating smaller blobs

**Spec:**
```
Type:       Multiplayer browser game (real-time .io)
Data model: Player(id, nickname, x, y, mass, color)
            Pellet(id, x, y, mass)
Features:   - Move the blob toward the mouse cursor with speed that drops as mass grows
            - Eat pellets and smaller players to gain mass
            - Split and eject mass with keyboard shortcuts
            - Run the simulation on the server at 20 ticks per second with client interpolation
            - Show a live top-10 leaderboard of the current arena
API:        WebSocket
            WS   /arena
Storage:    In-memory arena state on the server
Tech stack: Node.js, Colyseus, TypeScript, HTML Canvas
```

---

## Example 534

**Intent:**
Our group meets every Friday for board game night and we always argue about who's actually winning overall. I want a little web app where we log which game we played, who played, and the final scores. It should then show stats like win rates per person and per game, and a season ranking.

**Spec:**
```
Type:       Web application (score tracker)
Auth:       Group login with a shared password, plus one admin account
Data model: Player(id, name, avatar_color)
            BoardGame(id, name, min_players, max_players, scoring_type)
            Session(id, game_id -> BoardGame, played_at, notes)
            Result(id, session_id -> Session, player_id -> Player, score, is_winner)
Features:   - Log a play session with the game, players and final scores
            - Show win rate per player overall and per game
            - Rank players over a season using Elo ratings
            - Show the most played games and longest winning streaks
            - Edit or delete a wrongly entered session
API:        REST
            GET  /sessions
            POST /sessions
            GET  /stats/players
            GET  /stats/games/{id}
Storage:    SQLite
Tech stack: Python, FastAPI, SQLModel, React, Recharts
```

---

## Example 535

**Intent:**
flappy bird clone

**Spec:**
```
Type:       Mobile game (2D arcade)
Features:   - Flap the bird upward on each tap while gravity pulls it down
            - Scroll pipe pairs with random gap heights from right to left
            - Add a point for each pipe passed
            - End the game on collision with a pipe or the ground
            - Award bronze, silver and gold medals based on score
            - Save the best score on the device
Storage:    Local on-device storage (best score)
Tech stack: Godot 4, GDScript (Android and iOS export)
```

---

## Example 536

**Intent:**
Make for me a mobile game of solitaire with daily challenge

**Spec:**
```
Type:       Mobile game (card game)
Auth:       Anonymous sign-in (Firebase Auth) to sync stats
Data model: DailyDeal(date, seed, is_winnable)
            Stats(user_id, games_played, games_won, best_time, daily_streak)
Features:   - Play Klondike solitaire with drag-and-drop and tap-to-move
            - Choose draw-one or draw-three mode
            - Deal the same winnable daily challenge to every player from a shared seed
            - Undo moves and give a hint for the next possible move
            - Track win rate, best time and daily challenge streak
Storage:    Cloud Firestore (daily deals and stats)
Tech stack: Kotlin, Jetpack Compose, Firebase (Auth, Firestore)
```

---

## Example 537

**Intent:**
a math racing game for 2nd graders where answering right makes your car go faster

**Spec:**
```
Type:       Educational game (kids, browser)
Data model: Student(id, name, class_code)
            RaceResult(id, student_id -> Student, skill, correct, wrong, finish_time, played_at)
Features:   - Race a car against three computer cars on a looping track
            - Ask addition and subtraction questions within 20 or 100
            - Give a speed boost for each right answer and slow down on wrong ones
            - Adjust question difficulty based on recent accuracy
            - Show the teacher a results page per class code
API:        REST
            POST /results
            GET  /classes/{code}/results
Storage:    PostgreSQL (Supabase)
Tech stack: TypeScript, Phaser 3, Supabase
```

---

## Example 538

**Intent:**
a hangman game for teh browser with diffrent word categories

**Spec:**
```
Type:       Browser game (word game)
Features:   - Pick a random word from a chosen category like animals, movies or countries
            - Show blanks for letters and an on-screen keyboard
            - Reveal guessed letters and draw the next hangman part on a wrong guess
            - End the round after six wrong guesses or when the word is complete
            - Track wins and current streak per category
Storage:    Static JSON word lists, browser localStorage (stats)
Tech stack: HTML, CSS, JavaScript (SVG drawing)
```

---

## Example 539

**Intent:**
a first person horror game in unreal engine 5 set in an abandoned hospital

**Spec:**
```
Type:       Desktop game (3D first-person horror)
Features:   - Explore the hospital in first person with a flashlight that drains its battery
            - Hide in lockers and under beds from a monster driven by a behavior tree
            - Let the monster track the player by sound from running and opening doors
            - Find keycards and notes that unlock new wings and reveal the story
            - Trigger scripted scares with sound and lighting events
            - Save progress at checkpoint terminals
Storage:    Local save game slots (USaveGame)
Tech stack: Unreal Engine 5, C++, Blueprints, MetaSounds
```

---

## Example 540

**Intent:**
a jigsaw puzzle app where you upload your own photo and it cuts it into pieces

**Spec:**
```
Type:       Browser game (puzzle)
Data model: Puzzle(id, image_blob, piece_count, piece_positions, completed, created_at)
Features:   - Upload a photo and choose 24, 48, 100 or 200 pieces
            - Cut the image into classic interlocking piece shapes
            - Drag pieces and snap them together when placed next to their neighbor
            - Show a ghost preview of the full image as an optional hint
            - Save an unfinished puzzle and continue later
Storage:    Browser IndexedDB (images and puzzle progress)
Tech stack: TypeScript, Konva.js, idb
```

---

## Example 541

**Intent:**
I want to make a cozy farming game kind of like Stardew Valley but much smaller in scope. The player should be able to till soil, plant seeds, water crops and harvest them over in-game days, then sell the harvest to buy better seeds and tools. Seasons should change which crops can grow.

**Spec:**
```
Type:       Desktop game (2D farming sim)
Data model: Crop(id, name, season, days_to_grow, sell_price, seed_price)
            Tile(x, y, is_tilled, is_watered, crop_id -> Crop, growth_day)
            SaveState(day, season, gold, inventory, tool_levels)
Features:   - Till soil, plant seeds and water tiles with selectable tools
            - Grow watered crops by one stage each in-game day
            - Harvest crops and sell them in a shipping box at the end of the day
            - Buy seeds and tool upgrades in a shop
            - Change seasons every 28 days and wither crops out of season
            - Save the game when the player sleeps
Storage:    Local JSON save file
Tech stack: Godot 4, GDScript, TileMapLayer
```

---

## Example 542

**Intent:**
minesweeper for desktop

**Spec:**
```
Type:       Desktop game (puzzle)
Features:   - Generate a minefield after the first click so the first click is always safe
            - Reveal cells and flood-fill empty areas automatically
            - Flag and unflag suspected mines with right click
            - Choose beginner, intermediate, expert or custom board sizes
            - Show a timer and remaining mine count
            - Keep best times for each difficulty
Storage:    Local JSON file (best times)
Tech stack: C#, .NET 8, WPF
```

---

## Example 543

**Intent:**
an online kahoot-style quiz game for my classroom where students answer on their phones

**Spec:**
```
Type:       Multiplayer web game (live quiz)
Auth:       Teacher login (Google OAuth); students join with a PIN and nickname
Data model: Teacher(id, email, name)
            Quiz(id, teacher_id -> Teacher, title)
            Question(id, quiz_id -> Quiz, text, options, correct_index, time_limit)
            GameSession(pin, quiz_id -> Quiz, status, current_question)
            Response(id, pin -> GameSession, nickname, question_id -> Question, choice, answered_ms)
Features:   - Create quizzes with multiple-choice questions and time limits
            - Start a live game that shows a join PIN on the teacher's screen
            - Show questions on the big screen and colored answer buttons on phones
            - Score answers by correctness and speed
            - Show a podium of the top three at the end and export results as CSV
API:        REST + WebSocket
            POST /quizzes
            POST /games
            WS   /games/{pin}/host
            WS   /games/{pin}/player
Storage:    PostgreSQL, Redis (live game state)
Tech stack: Node.js, NestJS, Socket.IO, React
```

---

## Example 544

**Intent:**
I need game for learning japanese hiragana with flash and points

**Spec:**
```
Type:       Mobile application (educational game)
Data model: Kana(id, character, romaji, row, audio_file)
            CardProgress(kana_id -> Kana, ease, interval_days, due_at, correct_count)
Features:   - Show a hiragana flashcard and ask the user to pick or type the romaji
            - Play the pronunciation of each character
            - Schedule reviews with spaced repetition (SM-2)
            - Award points and keep a daily streak
            - Unlock new rows of kana when the current rows are learned
Storage:    Local on-device database (SQLite)
Tech stack: React Native, Expo, expo-sqlite, expo-av
```

---

## Example 545

**Intent:**
a match-3 gem game with phaser 3

**Spec:**
```
Type:       Browser game (match-3 puzzle)
Features:   - Fill an 8x8 board with random gems and no starting matches
            - Swap neighboring gems and undo the swap if it makes no match
            - Clear matches of three or more, drop gems down and refill with cascades
            - Create special gems from matches of four and five
            - Give each level a move limit and target score with one to three stars
            - Save stars per level
Storage:    Browser localStorage (level progress)
Tech stack: JavaScript, Phaser 3
```

---

## Example 546

**Intent:**
i want a pong game that 2 people can play online from different computers with socket.io

**Spec:**
```
Type:       Multiplayer browser game (real-time)
Data model: Match(id, left_player_id, right_player_id, ball, left_score, right_score, status)
Features:   - Pair two players into a match from a waiting queue or private link
            - Run ball physics on the server and send state 60 times per second
            - Move each player's paddle with keyboard input sent to the server
            - Predict the local paddle on the client to hide latency
            - Win the match at 11 points and offer a rematch
API:        WebSocket
            WS   /socket.io
Storage:    In-memory match state on the server
Tech stack: Node.js, Express, Socket.IO, HTML Canvas
```

---

## Example 547

**Intent:**
a mobile pet game where you feed and take care of a virtual pet and it gets sad if you ignore it

**Spec:**
```
Type:       Mobile game (virtual pet)
Data model: Pet(id, name, species, hunger, happiness, energy, cleanliness, born_at, last_update)
            Item(id, name, type, effect_value, price)
Features:   - Feed, play with, wash and put the pet to sleep
            - Lower the pet's stats over real time, including while the app is closed
            - Change the pet's mood and animations based on its stats
            - Send a notification when the pet is hungry or sad
            - Earn coins from mini-games and spend them on food and toys
Storage:    Local on-device storage (Hive)
Tech stack: Flutter, Flame, Hive, flutter_local_notifications
```

---

## Example 548

**Intent:**
speedrun timer with splits

**Spec:**
```
Type:       Desktop application (speedrun timer)
Data model: Run(id, game, category, attempt_count)
            Segment(id, run_id -> Run, name, best_time, pb_split_time)
            Attempt(id, run_id -> Run, started_at, segment_times, finished)
Features:   - Start, split, undo split and reset the timer with global hotkeys
            - Compare each split with the personal best and show gain or loss in color
            - Calculate sum of best segments and possible time save
            - Save attempts and update the personal best on a finished run
            - Import and export splits in LiveSplit .lss format
Storage:    Local SQLite database
Tech stack: Rust, egui, global-hotkey
```

---

## Example 549

**Intent:**
We're a small indie studio and our players keep making custom maps and skins for our game, but they share them through random Discord links. We want a website where creators can upload mods with screenshots and version notes, players can browse, rate and download them, and the game can fetch a mod list through an API.

**Spec:**
```
Type:       Web application (mod sharing platform)
Auth:       User registration and login (email + password, OAuth with Steam)
Data model: User(id, username, email, steam_id, role)
            Mod(id, author_id -> User, title, description, category, downloads, created_at)
            ModVersion(id, mod_id -> Mod, version, game_version, file_url, changelog, uploaded_at)
            Rating(id, mod_id -> Mod, user_id -> User, stars, review)
            Screenshot(id, mod_id -> Mod, image_url)
Features:   - Upload mods with screenshots, description and versioned files
            - Scan uploaded archives for viruses before publishing
            - Browse, search and filter mods by category and game version
            - Rate and review mods and report broken ones to moderators
            - Return mod lists and download links to the game client
API:        REST
            GET  /mods?category={c}&game_version={v}
            POST /mods
            POST /mods/{id}/versions
            GET  /mods/{id}/versions/latest
            POST /mods/{id}/ratings
Storage:    PostgreSQL, S3-compatible object storage (mod files and images)
Tech stack: Python, Django, Django REST Framework, ClamAV, React
```

---

## Example 550

**Intent:**
a dice rolling discord bot for our d&d sessions that also tracks initiative

**Spec:**
```
Type:       Discord bot (tabletop RPG helper)
Data model: Character(id, guild_id, owner_id, name, initiative_bonus)
            Encounter(id, channel_id, round, current_turn_index)
            InitiativeEntry(id, encounter_id -> Encounter, name, roll, is_npc)
Features:   - Roll dice from notation like 2d6+3, 4d6kh3 and d20 with advantage
            - Start an encounter and add players and monsters to the initiative order
            - Roll initiative for everyone and sort the turn order
            - Move to the next turn and ping the player whose turn it is
            - Save characters with their initiative bonus for quick reuse
Storage:    SQLite
Tech stack: Python, discord.py, d20 (dice parser)
```

---

## Example 551

**Intent:**
a turn based tactics game on a grid made with godot 4, like a mini fire emblem

**Spec:**
```
Type:       Desktop game (turn-based tactics)
Data model: Unit(id, name, class, hp, attack, defense, move_range, attack_range, team)
            MapData(id, width, height, terrain_grid, start_positions)
Features:   - Select a unit and show reachable tiles using terrain movement costs
            - Attack enemies in range with damage based on stats and terrain bonuses
            - Preview hit chance and damage before confirming an attack
            - Run enemy turns with a simple AI that targets the weakest unit in reach
            - Win by defeating all enemies and lose when the leader falls
            - Save progress between missions
Storage:    Local save file (user://)
Tech stack: Godot 4, GDScript, AStarGrid2D
```

---

## Example 552

**Intent:**
a geography quiz were you click the country on a map

**Spec:**
```
Type:       Browser game (geography quiz)
Features:   - Show the name of a country and ask the player to click it on a world map
            - Mark correct clicks green and show the right country after a wrong click
            - Filter questions by continent
            - Count the time and accuracy for a full round of 20 countries
            - Zoom and pan the map to click small countries
Storage:    Static GeoJSON map data, browser localStorage (best scores)
Tech stack: JavaScript, Leaflet, Natural Earth GeoJSON
```

---

## Example 553

**Intent:**
We want app for party where everybody use own phone and play truth or dare together

**Spec:**
```
Type:       Multiplayer mobile web app (party game)
Data model: Party(code, host_id, intensity_level, current_player_id)
            Player(id, party_code -> Party, nickname, skips_left)
            Card(id, type, text, intensity_level)
Features:   - Create a party and let friends join with a code on their own phones
            - Pick the next player at random and let them choose truth or dare
            - Show the card to everyone at the same time
            - Filter cards by intensity like family, friends or spicy
            - Let players add their own custom cards to the party
Storage:    Firebase Realtime Database (live party state)
Tech stack: React, Vite, Firebase (Realtime Database, Hosting)
```

---

## Example 554

**Intent:**
a rhythm game where you hit notes in time with songs you load yourself

**Spec:**
```
Type:       Desktop game (rhythm)
Data model: Song(id, file_path, title, artist, bpm, offset_ms)
            Chart(id, song_id -> Song, difficulty, notes)
            Score(id, chart_id -> Chart, points, accuracy, max_combo, played_at)
Features:   - Load MP3 or OGG files and detect beats to auto-generate note charts
            - Scroll notes down four lanes in sync with the audio clock
            - Judge hits as perfect, great, good or miss by timing window
            - Count combos and show the accuracy grade at the end
            - Edit charts by hand in a simple chart editor
            - Calibrate audio latency
Input:      Audio files chosen by the player
Storage:    Local SQLite database, chart JSON files
Tech stack: C#, MonoGame, NAudio, aubio (beat detection)
```

---

## Example 555

**Intent:**
2048 game

**Spec:**
```
Type:       Browser game (puzzle)
Features:   - Draw a 4x4 grid and spawn a 2 or 4 tile after each move
            - Slide and merge tiles with arrow keys or swipe gestures
            - Animate tile movement and merges
            - Detect the 2048 tile as a win and allow continuing
            - End the game when no moves are left
            - Save the current board and best score
Storage:    Browser localStorage
Tech stack: HTML, CSS, TypeScript
```

---

## Example 556

**Intent:**
I'm dreaming of a browser-based space trading game set in a persistent universe where hundreds of players fly between star systems, buy goods cheap in one place and sell them high in another. Prices should react to what players buy and sell, and travel should take real time. Players should also be able to form corporations.

**Spec:**
```
Type:       Multiplayer browser game (persistent MMO, strategy)
Auth:       User registration and login (email + password, JWT)
Data model: Player(id, username, email, password_hash, credits, corporation_id -> Corporation)
            Ship(id, player_id -> Player, model, cargo, system_id -> StarSystem, arrives_at)
            StarSystem(id, name, x, y)
            Market(id, system_id -> StarSystem, commodity, supply, demand, price)
            Corporation(id, name, ceo_id -> Player, treasury)
Features:   - Show a galaxy map of star systems and the player's ships
            - Send a ship to another system with real-time travel based on distance
            - Buy and sell goods at local markets
            - Recalculate prices from supply and demand on every trade and slowly restore them
            - Create and join corporations with a shared treasury
API:        REST + WebSocket
            POST /login
            GET  /systems
            GET  /systems/{id}/market
            POST /ships/{id}/travel
            POST /markets/{id}/trades
            WS   /events
Storage:    PostgreSQL, Redis (job queue for ship arrivals)
Tech stack: TypeScript, NestJS, BullMQ, React, PixiJS
```

---

## Example 557

**Intent:**
a fruit slot machine style game using pixi.js, just for fun with no real money

**Spec:**
```
Type:       Browser game (casual slots)
Features:   - Spin five reels with fruit symbols and smooth stop animations
            - Pick reel stops with a weighted random generator per symbol
            - Pay out play credits for matching symbols on 10 paylines
            - Trigger free spins on three or more bonus symbols
            - Refill credits for free when the balance hits zero
Storage:    Browser localStorage (credits)
Tech stack: TypeScript, PixiJS, GSAP
```

---

## Example 558

**Intent:**
a game where you guess the price of random products from online stores, like the price is right

**Spec:**
```
Type:       Web game (guessing game)
Data model: Product(id, title, image_url, price, category, source)
            Round(id, product_ids, guesses, total_score, played_at)
Features:   - Show a product with its image and title and ask for a price guess
            - Score each guess by how close it is in percentage
            - Play rounds of ten products and show the total
            - Filter products by category like tech, home or fashion
            - Refresh the product list weekly from a scraped dataset
API:        REST
            GET  /rounds/new?category={c}
            POST /rounds/{id}/guesses
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Playwright (scraping job), React
```

---

## Example 559

**Intent:**
pokemon style monster catching game for pc

**Spec:**
```
Type:       Desktop game (2D RPG)
Data model: Species(id, name, type, base_stats, moves_learned, catch_rate)
            Monster(id, species_id -> Species, nickname, level, xp, hp, moves)
            Move(id, name, type, power, accuracy)
            SaveState(map_id, x, y, party, storage_box, items)
Features:   - Walk around a tile-based overworld and trigger wild encounters in tall grass
            - Fight turn-based battles with type advantages
            - Throw capture balls with a chance based on catch rate and remaining HP
            - Level up monsters, learn new moves and evolve at set levels
            - Keep a party of six and store the rest in a box
            - Save the game anywhere
Storage:    Local JSON save file
Tech stack: Python, Pygame, Tiled maps (pytmx)
```

---

## Example 560

**Intent:**
a fishing mini game

**Spec:**
```
Type:       Browser game (casual)
Data model: Fish(id, name, rarity, min_weight, max_weight, difficulty)
            Catch(id, fish_id -> Fish, weight, caught_at)
Features:   - Cast the line by holding and releasing for distance
            - Wait for a bite and react within a short window to hook the fish
            - Keep the fish inside a moving bar until the reel meter fills
            - Log each catch with species and weight in a fish journal
            - Show the biggest catch per species
Storage:    Browser localStorage (journal)
Tech stack: JavaScript, Kaboom.js
```

---

## Example 561

**Intent:**
a twitch chat plays game where viewers vote on what the character does next

**Spec:**
```
Type:       Interactive streaming game (desktop + Twitch chat)
Data model: Vote(viewer_id, option, round_id -> VoteRound)
            VoteRound(id, options, started_at, ends_at, winner)
Features:   - Read chat messages from the streamer's channel in real time
            - Open a vote every 15 seconds with three possible actions
            - Count one vote per viewer and show live vote bars on screen
            - Apply the winning action to the character in the game
            - Let the streamer pause voting and change round length
API:        WebSocket (client of Twitch chat IRC)
            WS   wss://irc-ws.chat.twitch.tv
Storage:    In-memory vote state
Tech stack: Godot 4, GDScript, Twitch IRC over WebSocket
```

---

## Example 562

**Intent:**
Create the karaoke game which give score how good you are singing

**Spec:**
```
Type:       Desktop game (karaoke)
Data model: Song(id, title, artist, audio_file, lyrics_file, pitch_track)
            Performance(id, song_id -> Song, singer_name, score, sung_at)
Features:   - Play the backing track and show scrolling lyrics with timing
            - Capture the microphone and detect the sung pitch in real time
            - Compare the sung pitch with the song's note track and draw both on screen
            - Score each line by pitch accuracy and timing
            - Keep a high score table per song
Input:      Songs as audio files with UltraStar-format lyrics and notes
Storage:    Local SQLite database
Tech stack: Python, PyQt6, sounddevice, aubio (pitch detection)
```

---

## Example 563

**Intent:**
a racing game in unity with ai opponents and lap times

**Spec:**
```
Type:       Desktop game (3D racing)
Data model: Track(id, name, lap_count, checkpoints)
            LapRecord(track_id -> Track, best_lap_ms, best_race_ms, ghost_data)
Features:   - Drive cars with WheelCollider physics, drifting and boost
            - Race AI opponents that follow a waypoint spline and avoid collisions
            - Count laps through ordered checkpoints to prevent shortcuts
            - Show position, current lap and lap times on the HUD
            - Save best lap times and replay them as a ghost car
Storage:    Local save files (JSON in persistentDataPath)
Tech stack: Unity, C#, Cinemachine, Unity Splines
```

---

## Example 564

**Intent:**
As a dungeon master I spend hours drawing hex maps for my tabletop campaigns. I'd love a web-based hex map editor where I can paint terrain, place towns and dungeons with labels, and hide parts of the map so I can reveal them to players as they explore during a session.

**Spec:**
```
Type:       Web application (hex map editor)
Auth:       User registration and login (email + password)
Data model: User(id, email, password_hash)
            Map(id, owner_id -> User, name, width, height, share_token)
            Hex(map_id -> Map, q, r, terrain, is_revealed)
            Marker(id, map_id -> Map, q, r, icon, label, notes)
Features:   - Paint terrain types like forest, mountain and water onto a hex grid
            - Place markers for towns and dungeons with labels and private notes
            - Hide hexes under fog of war and reveal them during a session
            - Share a player view link that updates live when hexes are revealed
            - Export the map as a PNG image
API:        REST + WebSocket
            GET  /maps/{id}
            PUT  /maps/{id}/hexes
            POST /maps/{id}/markers
            WS   /maps/{id}/player-view
Storage:    PostgreSQL
Tech stack: TypeScript, React, Konva.js, Node.js, Fastify, ws
```

---

## Example 565

**Intent:**
a spelling bee app for my kid where it says the word out loud and she types it

**Spec:**
```
Type:       Mobile application (educational game)
Data model: WordList(id, name, grade_level)
            Word(id, list_id -> WordList, text, example_sentence)
            Attempt(id, word_id -> Word, typed, is_correct, attempted_at)
Features:   - Read each word and an example sentence aloud with text-to-speech
            - Let the child type the spelling and check it
            - Show the correct spelling letter by letter after a mistake
            - Let a parent add custom weekly word lists
            - Repeat missed words at the end of a session
Storage:    Local on-device database (SwiftData)
Tech stack: Swift, SwiftUI, AVSpeechSynthesizer, SwiftData
```

---

## Example 566

**Intent:**
battleship game agianst the computer in the console using java

**Spec:**
```
Type:       Terminal game (board game)
Features:   - Place ships manually or randomly on a 10x10 grid
            - Read target coordinates like B7 from the keyboard
            - Show both boards with hits, misses and sunk ships
            - Let the computer hunt randomly and then target cells around a hit
            - Announce the winner when all of one side's ships are sunk
Tech stack: Java 21 (standard library only)
```

---

## Example 567

**Intent:**
online mahjong for four players

**Spec:**
```
Type:       Multiplayer web game (tile game)
Auth:       Guest login with nickname or account login (email + password)
Data model: User(id, username, email, password_hash, rating)
            Table(id, ruleset, status, seats)
            Hand(id, table_id -> Table, round_wind, dealer_seat, wall, discards, result)
Features:   - Seat four players at a table from a lobby or private invite
            - Deal tiles and run draw and discard turns on the server
            - Offer pon, kan, chi and win calls with a short response timer
            - Score winning hands with Riichi rules
            - Fill empty seats with bot players
API:        REST + WebSocket
            POST /tables
            POST /tables/{id}/join
            WS   /tables/{id}
Storage:    PostgreSQL, Redis (active tables)
Tech stack: Go, gorilla/websocket, Vue 3, PixiJS
```

---

## Example 568

**Intent:**
an escape room puzzle website with riddles you unlock one by one

**Spec:**
```
Type:       Web game (online escape room)
Auth:       Team login with a team name and password
Data model: Team(id, name, password_hash, started_at, finished_at)
            Puzzle(id, order, title, prompt, answer_hash, hint)
            Solve(team_id -> Team, puzzle_id -> Puzzle, solved_at, hints_used)
Features:   - Show only the current puzzle and lock the next ones
            - Check answers on the server ignoring case and spaces
            - Reveal a hint with a time penalty
            - Time each team from start to finish
            - Show a leaderboard of finish times
API:        REST
            POST /teams
            GET  /puzzles/current
            POST /puzzles/{id}/answer
            GET  /leaderboard
Storage:    SQLite
Tech stack: Python, Flask, Jinja2
```

---

## Example 569

**Intent:**
a VR boxing workout game where you punch targets to the beat of music

**Spec:**
```
Type:       VR game (fitness)
Data model: Workout(id, song, difficulty, duration_seconds)
            Session(id, workout_id -> Workout, score, accuracy, punches, calories_estimate, played_at)
Features:   - Spawn targets in sync with the music's beat map
            - Detect punch hits with controller velocity and direction
            - Make the player dodge and squat under incoming bars
            - Show combo, accuracy and estimated calories after each song
            - Track workout history and weekly totals
Storage:    Local save file on the headset
Tech stack: Unity, C#, OpenXR, XR Interaction Toolkit
```

---

## Example 570

**Intent:**
I wish to make mobile game where you are throwing ball to cups, like beer pong but for everybody

**Spec:**
```
Type:       Mobile game (3D casual)
Features:   - Flick the screen to throw a ping pong ball with the swipe's speed and angle
            - Simulate bounces on the table and cup rims with physics
            - Remove a cup when the ball lands in it and rerack at set counts
            - Play against an AI opponent with easy, normal and hard accuracy
            - Play pass-and-play with two players on one phone
Storage:    Local on-device storage (wins and settings)
Tech stack: Unity, C#, Unity Physics
```

---

## Example 571

**Intent:**
a physics puzzle game with matter.js where you draw lines to guide a ball into a cup

**Spec:**
```
Type:       Browser game (physics puzzle)
Data model: Level(id, ball_start, cup_position, obstacles, ink_limit)
Features:   - Draw lines with the mouse or finger that turn into solid physics bodies
            - Drop the ball when the player presses play and simulate with Matter.js
            - Limit the amount of ink per level
            - Complete the level when the ball rests inside the cup
            - Rate each level with stars based on ink used
Storage:    Static JSON levels, browser localStorage (stars)
Tech stack: JavaScript, Matter.js, HTML Canvas
```

---

## Example 572

**Intent:**
I run a medium-sized Discord community and want an RPG bot that keeps people chatting. Members should be able to create a character, go on timed adventures that give gold and XP, buy gear from a shop, and fight each other in duels. Admins need commands to add new items and reset the economy.

**Spec:**
```
Type:       Discord bot (RPG and economy)
Data model: Character(id, discord_user_id, guild_id, name, class, level, xp, gold, hp)
            Item(id, guild_id, name, slot, attack_bonus, defense_bonus, price)
            InventoryItem(character_id -> Character, item_id -> Item, equipped)
            Adventure(id, character_id -> Character, zone, started_at, ends_at, claimed)
Features:   - Create a character with a class using a slash command
            - Send the character on a timed adventure and reward gold, XP and loot on return
            - Buy, sell and equip items from a per-server shop
            - Challenge another member to a turn-based duel with buttons
            - Let admins add items and reset the economy with permission-checked commands
            - Show level and gold leaderboards
Storage:    PostgreSQL
Tech stack: Python, discord.py, asyncpg, APScheduler
```

---

## Example 573

**Intent:**
an asteroids clone in c++ with sfml

**Spec:**
```
Type:       Desktop game (2D arcade)
Features:   - Rotate and thrust the ship with inertia and wrap around screen edges
            - Fire bullets with a short lifetime and a fire-rate limit
            - Split large asteroids into medium and small ones when shot
            - Spawn a UFO that shoots at the player in later waves
            - Give extra lives every 10,000 points and save the high score
Storage:    Local text file (high score)
Tech stack: C++17, SFML, CMake
```

---

## Example 574

**Intent:**
sim city style city builder in the browser but small, like one screen map

**Spec:**
```
Type:       Browser game (city builder)
Data model: Tile(x, y, zone_type, building_level, has_road, has_power)
            City(name, money, population, day, tax_rate)
Features:   - Place roads, power lines and residential, commercial and industrial zones
            - Grow buildings on zones that have road and power access
            - Balance demand between zone types and show demand bars
            - Collect taxes and pay upkeep at the end of each month
            - Advance time with pause, normal and fast speeds
            - Save and load cities
Storage:    Browser IndexedDB (saved cities)
Tech stack: TypeScript, PixiJS, Vite
```

---

## Example 575

**Intent:**
a bingo caller app

**Spec:**
```
Type:       Web application (game host tool)
Features:   - Draw random numbers from 1-75 or 1-90 without repeats
            - Announce each number out loud with speech synthesis
            - Show all called numbers on a large board for a TV screen
            - Draw automatically on a timer or manually on click
            - Print random bingo cards as a PDF
Storage:    Browser localStorage (current game)
Tech stack: React, Web Speech API, jsPDF
```

---

## Example 576

**Intent:**
a werewolf / mafia game app that acts as the narrator so nobody has to sit out

**Spec:**
```
Type:       Multiplayer mobile web app (social deduction)
Data model: Game(code, phase, day_number, role_setup, status)
            Player(id, game_code -> Game, nickname, role, is_alive)
            NightAction(id, game_code -> Game, player_id -> Player, target_id -> Player, action)
            Vote(id, game_code -> Game, voter_id -> Player, target_id -> Player, day_number)
Features:   - Assign secret roles like werewolf, seer and doctor to each phone
            - Narrate night and day phases with voice and on-screen prompts
            - Collect night actions privately and resolve them on the server
            - Run day votes with a timer and eliminate the most voted player
            - Detect when villagers or werewolves win and reveal all roles
API:        WebSocket
            WS   /games/{code}
Storage:    In-memory game state on the server
Tech stack: Node.js, Socket.IO, Svelte, Web Speech API
```

---

## Example 577

**Intent:**
a game save backup tool that copies my save folders to the cloud so I don't lose progress

**Spec:**
```
Type:       Desktop application (background utility)
Data model: GameEntry(id, name, save_path, enabled)
            Backup(id, game_id -> GameEntry, created_at, size_bytes, remote_path)
Features:   - Detect save folders of installed games from a known-locations list
            - Watch save folders and back up a zipped copy after changes
            - Upload backups to Google Drive or Dropbox
            - Keep the last 10 backups per game and delete older ones
            - Restore a chosen backup to the save folder
Storage:    Local SQLite database (backup index), cloud storage (archives)
Tech stack: Python, PySide6, watchdog, Google Drive API, Dropbox API
```

---

## Example 578

**Intent:**
Need a quiz app about football where questions get more hard each level

**Spec:**
```
Type:       Mobile game (trivia)
Auth:       Anonymous sign-in with optional Google account (Firebase Auth)
Data model: Question(id, level, text, options, correct_index, image_url)
            PlayerProgress(user_id, highest_level, total_points, lives)
Features:   - Play levels of ten questions that get harder as the level rises
            - Unlock the next level after eight correct answers
            - Use jokers like 50/50 and skip once per level
            - Show player photos and club badges in picture questions
            - Rank players on a global leaderboard
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase (Auth, Firestore, Storage)
```

---

## Example 579

**Intent:**
a visual novel with renpy about a summer romance with a few different endings

**Spec:**
```
Type:       Desktop game (visual novel)
Features:   - Show character sprites with expressions over background scenes
            - Branch the story with choices that change affection points
            - Pick one of several endings based on affection and key choices
            - Unlock a CG gallery and music room as the player progresses
            - Save and load at any point with multiple slots
            - Skip already-read text on replays
Storage:    Ren'Py save files and persistent data
Tech stack: Ren'Py, Python (Ren'Py script)
```

---

## Example 580

**Intent:**
I want to make an online collectible card game similar to Hearthstone but with my own art and cards. Players should open packs, build 30-card decks and play ranked matches against other people in real time. The server has to enforce all the rules so nobody can cheat.

**Spec:**
```
Type:       Multiplayer game (online card game, web and desktop)
Auth:       User registration and login (email + password, JWT)
Data model: User(id, username, email, password_hash, rank, gold)
            Card(id, name, cost, attack, health, rarity, effect_script)
            Collection(user_id -> User, card_id -> Card, quantity)
            Deck(id, user_id -> User, name, card_ids)
            Match(id, player1_id -> User, player2_id -> User, winner_id -> User, log, played_at)
Features:   - Open card packs with rarity odds using in-game gold
            - Build and validate 30-card decks with copy limits
            - Match players of similar rank in a ranked queue
            - Run all game rules, draws and card effects on the server
            - Update ranks after each match and save a replay log
API:        REST + WebSocket
            POST /login
            POST /packs/open
            GET  /collection
            POST /decks
            POST /matchmaking/queue
            WS   /matches/{id}
Storage:    PostgreSQL, Redis (matchmaking queue)
Tech stack: Unity (client), C#, Node.js, Colyseus, TypeScript
```

---

## Example 581

**Intent:**
kids coloring game

**Spec:**
```
Type:       Mobile game (kids, creative)
Data model: Drawing(id, template_id, image_path, updated_at)
Features:   - Pick a coloring page from categories like animals, vehicles and princesses
            - Fill areas with one tap using flood fill
            - Paint freely with brushes, crayons and stickers
            - Undo mistakes and clear the page
            - Save finished pictures to a gallery and the photo library
Storage:    Local on-device files (drawings)
Tech stack: Flutter, CustomPainter, image_gallery_saver
```

---

## Example 582

**Intent:**
a couch party game with a bunch of quick minigames for up to 4 controllers on one tv

**Spec:**
```
Type:       Desktop game (local multiplayer party)
Features:   - Detect up to four gamepads and let each player pick a character
            - Pick random minigames like sumo push, hot potato and button mash
            - Award points per minigame and show the standings between rounds
            - End the match after a set number of rounds and crown the winner
            - Add CPU players when fewer than four people play
Storage:    Local settings file
Tech stack: Godot 4, GDScript (Steam Deck and Windows export)
```

---

## Example 583

**Intent:**
a sokoban puzzel game with a level select screen and undo

**Spec:**
```
Type:       Browser game (puzzle)
Features:   - Load levels from the standard Sokoban text format
            - Move the player and push boxes with arrow keys or swipes
            - Undo moves and restart the level
            - Count moves and pushes and complete the level when all boxes are on goals
            - Show a level select screen with locked and solved levels
Storage:    Browser localStorage (solved levels and best move counts)
Tech stack: JavaScript, HTML Canvas
```

---

## Example 584

**Intent:**
an online word game like scrabble where you play slowly with friends, one move whenever you have time

**Spec:**
```
Type:       Mobile application (asynchronous multiplayer word game)
Auth:       Sign in with Apple and Google (Firebase Auth)
Data model: User(id, display_name, avatar_url, push_token)
            Game(id, player_ids, board, tile_bag, scores, current_turn_id, status)
            Rack(game_id -> Game, user_id -> User, tiles)
            Move(id, game_id -> Game, user_id -> User, placed_tiles, words, points, played_at)
Features:   - Start a game with a friend or a random opponent
            - Place tiles on the board and check words against a dictionary
            - Calculate scores with letter and word multiplier squares
            - Send a push notification when it is the player's turn
            - Forfeit the game when a player does not move for 3 days
API:        REST (Cloud Functions)
            POST /games
            POST /games/{id}/moves
            GET  /games/{id}
Storage:    Cloud Firestore
Tech stack: React Native, Firebase (Auth, Firestore, Cloud Functions, Cloud Messaging)
```

---

## Example 585

**Intent:**
an obby game on roblox with checkpoints, a timer and a leaderboard

**Spec:**
```
Type:       Online game (Roblox experience)
Data model: PlayerData(user_id, current_stage, best_time_seconds, coins)
Features:   - Build stages of jumps, moving platforms and kill bricks
            - Save the player's stage at each checkpoint and respawn there after falling
            - Time the run from the first stage to the finish
            - Show stage and best time on the in-game leaderboard
            - Sell skip-stage and trail items with in-game coins
Storage:    Roblox DataStoreService (player data), OrderedDataStore (global best times)
Tech stack: Roblox Studio, Luau
```

---

## Example 586

**Intent:**
Make a game, user is a frog jumping across the road and the river, must avoid cars

**Spec:**
```
Type:       Browser game (2D arcade)
Features:   - Move the frog one tile at a time with arrow keys or swipes
            - Scroll lanes of cars and trucks at different speeds and directions
            - Ride logs and turtles across the river and die when falling in water
            - Fill the five homes at the top to finish a level
            - Speed up traffic each level and give a time limit per life
            - Save the high score
Storage:    Browser localStorage (high score)
Tech stack: TypeScript, Phaser 3
```

---

## Example 587

**Intent:**
I'm an achievement hunter with hundreds of Steam games and I want a dashboard that pulls in all my achievements. It should show which games are closest to 100%, which achievements are the rarest, and let me plan which game to complete next. Ideally it updates itself every day.

**Spec:**
```
Type:       Web application (gaming stats dashboard)
Auth:       Sign in through Steam (OpenID)
Data model: User(steam_id, persona_name, avatar_url, last_synced_at)
            Game(app_id, name, icon_url, total_achievements)
            Achievement(id, app_id -> Game, api_name, display_name, global_percent)
            UserAchievement(steam_id -> User, achievement_id -> Achievement, unlocked_at)
Features:   - Import owned games and unlocked achievements from the Steam Web API
            - Show completion percentage per game and sort by closest to 100%
            - Rank the user's rarest unlocked achievements by global unlock rate
            - Add games to a completion plan with target dates
            - Sync all data once a day in a background job
API:        REST
            GET  /me/games
            GET  /me/games/{app_id}/achievements
            GET  /me/rarest
            POST /me/plan
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Celery, Steam Web API, Vue 3
```

---

## Example 588

**Intent:**
connect four vs ai

**Spec:**
```
Type:       Browser game (board game)
Features:   - Drop discs into a 7x6 grid with a falling animation
            - Detect four in a row horizontally, vertically and diagonally
            - Choose AI difficulty that sets the minimax search depth with alpha-beta pruning
            - Highlight the winning four and offer a rematch
            - Let the player choose to go first or second
Tech stack: TypeScript, React
```

---

## Example 589

**Intent:**
a pixel art editor made specifically for making game sprites and exporting spritesheets

**Spec:**
```
Type:       Desktop application (sprite editor)
Data model: Project(id, name, width, height, palette)
            Frame(id, project_id -> Project, index, duration_ms)
            Layer(id, project_id -> Project, name, visible, opacity)
            Cel(frame_id -> Frame, layer_id -> Layer, pixels)
Features:   - Draw with pencil, eraser, fill, line and selection tools on a zoomable grid
            - Manage layers and animation frames with onion skinning
            - Preview the animation at a chosen frame rate
            - Edit and import color palettes
            - Export spritesheets as PNG with a JSON frame atlas
Storage:    Local project files (custom JSON + PNG)
Tech stack: C++, Qt 6
```

---

## Example 590

**Intent:**
a discord.py bot that posts a daily wordle-like puzzle for the whole server to solve

**Spec:**
```
Type:       Discord bot (daily puzzle)
Data model: DailyWord(date, word)
            Attempt(id, guild_id, user_id, date, guesses, solved)
            Streak(guild_id, user_id, current_streak, best_streak)
Features:   - Post a new puzzle announcement in a set channel every day at midnight UTC
            - Accept guesses through a slash command and reply privately with colored tiles
            - Limit each member to six guesses per day
            - Post a server summary with everyone's guess counts at the end of the day
            - Track streaks and show a leaderboard
Storage:    SQLite
Tech stack: Python, discord.py, aiosqlite
```

---

## Example 591

**Intent:**
a zombie survival game top down shooter with waves and you can buy guns between rounds

**Spec:**
```
Type:       Desktop game (2D top-down shooter)
Data model: Weapon(id, name, damage, fire_rate, magazine_size, price)
            RunState(wave, money, health, owned_weapon_ids)
Features:   - Move with WASD and aim and shoot toward the mouse
            - Spawn larger waves of zombies that path toward the player
            - Earn money for each kill and spend it in a shop between waves
            - Reload weapons and switch between owned guns
            - Drop health and ammo pickups at random
            - Save the best wave reached
Storage:    Local JSON file (best wave)
Tech stack: Python, Pygame
```

---

## Example 592

**Intent:**
a horse racing betting game with fake money for our office party

**Spec:**
```
Type:       Multiplayer web game (party)
Data model: Race(id, horses, odds, status, winner_horse_id)
            Horse(id, name, speed_rating, color)
            Player(id, name, balance)
            Bet(id, player_id -> Player, race_id -> Race, horse_id -> Horse, amount)
Features:   - Let guests join on their phones and get starting play money
            - Show horses with odds and accept bets before the race closes
            - Animate the race on a big screen with randomness weighted by horse speed
            - Pay out winning bets by the odds
            - Show a money leaderboard after each race
API:        REST + WebSocket
            POST /players
            POST /races/{id}/bets
            WS   /races/live
Storage:    SQLite
Tech stack: Python, FastAPI, JavaScript, HTML Canvas
```

---

## Example 593

**Intent:**
I'm learning Spanish and flashcards bore me, so I want a small RPG where you walk around a town and talk to characters in Spanish. Quests should require understanding what NPCs say and answering correctly, and new vocabulary should be added to a review list automatically.

**Spec:**
```
Type:       Desktop game (2D educational RPG)
Data model: Npc(id, name, location, dialogue_tree_id)
            Quest(id, title, npc_id -> Npc, required_words, reward_xp)
            Word(id, spanish, english, audio_file)
            ReviewItem(word_id -> Word, ease, due_at)
Features:   - Walk around a town map and start conversations with NPCs
            - Show dialogue in Spanish with a tap-to-translate option per word
            - Answer NPCs by choosing or typing the right reply to complete quests
            - Add new words seen in dialogue to a spaced-repetition review list
            - Unlock new areas of town as the player's level rises
Storage:    Local SQLite database
Tech stack: Godot 4, GDScript, Dialogic (dialogue plugin)
```

---

## Example 594

**Intent:**
a geoguessr-like game

**Spec:**
```
Type:       Web game (location guessing)
Auth:       Optional login (email + password) to save stats
Data model: Location(id, lat, lng, pano_id, country)
            Game(id, user_id, location_ids, total_score, created_at)
            Guess(id, game_id -> Game, location_id -> Location, guess_lat, guess_lng, distance_km, points)
Features:   - Drop the player into a random Street View panorama
            - Let the player place a guess pin on a world map
            - Score each guess by distance and show both points on the map
            - Play five rounds and show the total score
            - Challenge a friend with a link that uses the same locations
API:        REST
            POST /games
            POST /games/{id}/guesses
            GET  /games/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Google Maps JavaScript API (Street View)
```

---

## Example 595

**Intent:**
I like to make card game of war for the browser, very simple one

**Spec:**
```
Type:       Browser game (card game)
Features:   - Shuffle a 52-card deck and split it between the player and the computer
            - Flip the top card of each deck on click and give both cards to the higher one
            - Play a war of three face-down cards and one face-up card on ties
            - Show how many cards each side has left
            - End the game when one side has all the cards
Tech stack: HTML, CSS, JavaScript
```

---

## Example 596

**Intent:**
a minecraft server plugin in java for a custom parkour minigame with leaderboards

**Spec:**
```
Type:       Game server plugin (Minecraft)
Data model: Course(id, name, world, start_location, finish_location, checkpoints)
            RunRecord(id, course_id -> Course, player_uuid, time_ms, finished_at)
Features:   - Create courses in game with admin commands for start, checkpoints and finish
            - Start a timer when a player steps on the start pressure plate
            - Teleport players to the last checkpoint when they fall below a set height
            - Save finish times and show the top 10 on a hologram leaderboard
            - Show the current time on the action bar during a run
Storage:    SQLite (via HikariCP)
Tech stack: Java 21, Paper API, Gradle, DecentHolograms
```

---

## Example 597

**Intent:**
a game for my toddler where tapping the screen makes animal sounds and colors pop up

**Spec:**
```
Type:       Mobile game (toddler)
Features:   - Show a bright animal with a sound and burst of colors on every tap
            - Respond to multi-touch with a different animal per finger
            - Use no text, menus, ads or in-app purchases in the play area
            - Lock the parent settings behind a hold-to-unlock button
            - Work fully offline
Tech stack: Unity, C#, Unity Input System (iOS and Android)
```

---

## Example 598

**Intent:**
online checkers game wiht chat and ranked matchmaking

**Spec:**
```
Type:       Multiplayer web game (turn-based)
Auth:       User registration and login (email + password, session cookies)
Data model: User(id, username, email, password_hash, elo)
            Match(id, red_id -> User, black_id -> User, board_state, status, winner_id -> User)
            ChatMessage(id, match_id -> Match, user_id -> User, text, sent_at)
Features:   - Queue for a ranked match against a player with similar Elo
            - Validate moves including forced captures, multi-jumps and kinging
            - Chat with the opponent during the match with a profanity filter
            - Update Elo ratings after each finished match
            - Show a ranked leaderboard and match history
API:        REST + WebSocket
            POST /signup
            POST /login
            POST /queue
            GET  /leaderboard
            WS   /matches/{id}
Storage:    PostgreSQL, Redis (matchmaking queue)
Tech stack: Python, Django, Django Channels, React
```

---

## Example 599

**Intent:**
a randomizer tool for an old snes rom that shuffles where the items are, so replays feel new

**Spec:**
```
Type:       Command-line tool (ROM randomizer)
Features:   - Read item location tables from a supported ROM after checking its checksum
            - Shuffle items with a logic solver so every seed is beatable
            - Generate from a seed number so runs can be shared
            - Write a patched copy of the ROM and leave the original untouched
            - Output a spoiler log of all item locations
Input:      Path to a ROM file, optional seed number and settings file
Tech stack: Rust, clap
```

---

## Example 600

**Intent:**
Our narrative designers write branching conversations in spreadsheets and it's a mess. We need a dialogue tree editor where they can lay out lines as connected nodes, add conditions and variables like "has_key == true", and preview the conversation. The output has to be JSON our engine can load.

**Spec:**
```
Type:       Desktop application (game dialogue editor)
Data model: Conversation(id, name, start_node_id)
            DialogueNode(id, conversation_id -> Conversation, speaker, text, position)
            Link(id, from_node_id -> DialogueNode, to_node_id -> DialogueNode, choice_text, condition)
            Variable(id, name, type, default_value)
Features:   - Create speaker lines and player choices as nodes on a pannable graph canvas
            - Connect nodes and attach conditions and variable changes to links
            - Play through a conversation in a preview window with editable variables
            - Flag broken links and unreachable nodes
            - Export conversations as JSON in the engine's format
Storage:    Local project files (JSON)
Tech stack: Electron, React, TypeScript, React Flow
```

---

## Example 601

**Intent:**
a nonogram puzzle app

**Spec:**
```
Type:       Mobile game (logic puzzle)
Data model: Puzzle(id, size, row_clues, column_clues, solution, pack)
            Progress(puzzle_id -> Puzzle, grid_state, solved, best_time_seconds)
Features:   - Show row and column clues around a grid of 5x5 up to 20x20
            - Fill or cross cells with tap and drag
            - Grey out clues that are already satisfied
            - Check the grid against the solution and reveal the pixel picture when solved
            - Group puzzles into packs by size and difficulty
Storage:    Local on-device database (Room)
Tech stack: Kotlin, Jetpack Compose, Room
```

---

## Example 602

**Intent:**
a mini golf game in the browser with babylon.js where friends take turns on the same course online

**Spec:**
```
Type:       Multiplayer browser game (3D turn-based)
Data model: Room(code, course_id, hole_number, turn_player_id)
            Player(id, room_code -> Room, nickname, ball_color, strokes_per_hole)
Features:   - Render 3D holes with ramps, windmills and walls
            - Aim and set shot power by dragging back from the ball
            - Simulate the ball with Havok physics and sync the final position to all players
            - Take turns per hole and move on after everyone has holed out or hit the stroke limit
            - Show a scorecard with par and strokes per hole
API:        WebSocket
            WS   /rooms/{code}
Storage:    In-memory room state on the server
Tech stack: TypeScript, Babylon.js, Havok Physics, Node.js, Socket.IO
```

---

## Example 603

**Intent:**
Kindly build one ludo game for play with family on one tablet

**Spec:**
```
Type:       Mobile game (board game)
Features:   - Draw a ludo board for two to four players with colored tokens
            - Roll the dice with a tap and an animation
            - Move tokens out of home only on a six and give an extra roll on six
            - Send opponent tokens home when landing on them outside safe squares
            - Fill empty seats with computer players
            - Resume a paused game later
Storage:    Local on-device storage (saved game)
Tech stack: Flutter, Flame
```

---

## Example 604

**Intent:**
a guess the song game where it plays 5 seconds of a song from spotify and you have to guess

**Spec:**
```
Type:       Web game (music guessing)
Auth:       Spotify login (OAuth 2.0 with PKCE, Premium required for playback)
Data model: Round(id, track_id, artist, title, guesses, points)
            GameResult(id, playlist_id, total_points, played_at)
Features:   - Pick a playlist from the user's Spotify library
            - Play a random 5-second clip of a track with the Web Playback SDK
            - Autocomplete guesses from the track titles in the playlist
            - Give more time and fewer points after each wrong guess
            - Show the album art and track after each round
API:        REST (client of the Spotify Web API)
            GET  /v1/me/playlists
            GET  /v1/playlists/{id}/tracks
            PUT  /v1/me/player/play
Storage:    Browser localStorage (best scores)
Tech stack: React, TypeScript, Spotify Web Playback SDK, Spotify Web API
```

---

## Example 605

**Intent:**
I always have like 60 tabs open, can you make a chrome extension that saves all my tabs as a session so I can close them and bring them back later?

**Spec:**
```
Type:       Browser extension
Data model: Session(id, name, created_at)
            SavedTab(id, session_id -> Session, url, title, favicon_url, pinned, position)
Features:   - Save all tabs in the current window as a named session
            - Close the saved tabs after saving to free memory
            - List saved sessions in the toolbar popup with tab counts
            - Restore a whole session or open a single tab from it
            - Rename, merge and delete sessions
            - Export and import sessions as a JSON file
Storage:    chrome.storage.local (sessions)
Tech stack: JavaScript, Chrome Extension Manifest V3 (tabs API), HTML/CSS popup
```

---

## Example 606

**Intent:**
a firefox addon that shows me which trackers each website is loading and lets me block them

**Spec:**
```
Type:       Browser extension
Data model: TrackerRule(id, domain, category, company)
            SiteStats(hostname, blocked_count, allowed_count, last_visit)
            SiteException(hostname, allowed_tracker_domains)
Features:   - Match outgoing requests against a list of known tracker domains
            - Block matching requests before they are sent
            - Show the number of blocked trackers on the toolbar badge
            - List the trackers found on the current site grouped by company
            - Allow specific trackers per site when a page breaks
            - Update the tracker list from a remote source once a week
Storage:    browser.storage.local (rules, stats, exceptions)
Tech stack: JavaScript, Firefox WebExtensions API (webRequest, webRequestBlocking)
```

---

## Example 607

**Intent:**
highlight text on any webpage and add notes to it

**Spec:**
```
Type:       Browser extension
Data model: Page(url, title, first_annotated_at)
            Highlight(id, page_url -> Page, text, xpath_range, color, note, created_at)
Features:   - Highlight selected text on a page in a chosen color
            - Attach a short note to any highlight
            - Re-apply saved highlights when the page is visited again
            - List all highlights and notes for the current page in a side panel
            - Search highlights across all pages
            - Export highlights of a page as Markdown
Storage:    chrome.storage.local (highlights per URL)
Tech stack: TypeScript, Chrome Extension Manifest V3 (content scripts, sidePanel API)
```

---

## Example 608

**Intent:**
I keep checking Amazon to see if stuff on my wishlist got cheaper. Can an extension watch the prices for me and tell me when they drop?

**Spec:**
```
Type:       Browser extension
Data model: TrackedProduct(id, url, title, image_url, target_price, currency, added_at)
            PricePoint(id, product_id -> TrackedProduct, price, checked_at)
Features:   - Add the product on the current Amazon page to the watch list
            - Read the current price from the product page
            - Check all tracked prices every 6 hours in the background
            - Send a browser notification when a price drops below the target
            - Show a price history chart for each product in the popup
            - Remove products from the watch list
Storage:    chrome.storage.local (products and price history)
Tech stack: JavaScript, Chrome Extension Manifest V3 (alarms, notifications), Chart.js
```

---

## Example 609

**Intent:**
when i select a word or sentence on a page i want a small popup with the translation in my language

**Spec:**
```
Type:       Browser extension
Data model: Settings(target_language, auto_detect_source, show_on_select)
            TranslationCache(source_text, target_language, translated_text, cached_at)
Features:   - Show a translate button next to selected text
            - Translate the selection into the user's chosen language
            - Detect the source language automatically
            - Show the translation in a small tooltip near the selection
            - Play the pronunciation of the original text
            - Cache recent translations to avoid repeated requests
Storage:    chrome.storage.sync (settings), chrome.storage.local (cache)
Tech stack: JavaScript, Chrome Extension Manifest V3 (content scripts), DeepL API
```

---

## Example 610

**Intent:**
My son has dyslexia and struggles reading websites. Is it possible to make an extension that changes the font to something easier, adds more spacing between lines and maybe a ruler that follows the line he is reading? He uses Chrome on a school Chromebook.

**Spec:**
```
Type:       Browser extension (accessibility)
Data model: ReadingProfile(id, name, font_family, font_size, line_height, letter_spacing, background_color)
Features:   - Replace page fonts with a dyslexia-friendly font (OpenDyslexic)
            - Adjust font size, line height and letter spacing with sliders
            - Change the page background to a soft tint
            - Show a reading ruler that follows the mouse line by line
            - Save several reading profiles and switch between them
            - Turn the changes on or off per site from the popup
Storage:    chrome.storage.sync (profiles, per-site settings)
Tech stack: JavaScript, Chrome Extension Manifest V3 (scripting API, injected CSS)
```

---

## Example 611

**Intent:**
dark mode for every website

**Spec:**
```
Type:       Browser extension
Data model: SiteSetting(hostname, enabled, brightness, contrast)
Features:   - Apply a dark theme to any page by inverting and adjusting colors
            - Keep images and videos in their original colors
            - Adjust brightness and contrast from the popup
            - Turn dark mode off for specific sites
            - Follow the operating system's dark mode setting automatically
Storage:    chrome.storage.sync (global and per-site settings)
Tech stack: TypeScript, Chrome Extension Manifest V3 (content scripts, CSS filters)
```

---

## Example 612

**Intent:**
so annoying clicking "accept cookies" on every site, make something that closes those banners automatically

**Spec:**
```
Type:       Browser extension
Data model: BannerRule(id, hostname_pattern, selector, action)
            Stats(total_dismissed, last_dismissed_at)
Features:   - Detect cookie consent banners using a list of known selectors
            - Click the "reject all" or "necessary only" button when available
            - Hide the banner with CSS when no button can be clicked
            - Count dismissed banners and show the total in the popup
            - Let the user report a site where the banner was not removed
            - Pause the extension on chosen sites
Storage:    chrome.storage.local (rules, stats, paused sites)
Tech stack: JavaScript, Chrome Extension Manifest V3 (content scripts, MutationObserver)
```

---

## Example 613

**Intent:**
show how long an article will take to read

**Spec:**
```
Type:       Browser extension
Data model: Settings(words_per_minute, show_badge, show_progress_bar)
Features:   - Extract the main article text from the page
            - Count words and estimate reading time from the user's reading speed
            - Show the estimated minutes on the toolbar badge
            - Show a progress bar at the top of the page while scrolling
            - Let the user set their reading speed in words per minute
Storage:    chrome.storage.sync (settings)
Tech stack: JavaScript, Chrome Extension Manifest V3, Mozilla Readability
```

---

## Example 614

**Intent:**
my laptop gets slow becuase chrome eats all the ram, can u make an extension that puts tabs to sleep if i havent used them for a while

**Spec:**
```
Type:       Browser extension
Data model: Settings(idle_minutes, skip_pinned, skip_audible, whitelist)
            TabActivity(tab_id, last_active_at)
Features:   - Track when each tab was last active
            - Discard tabs that have been idle longer than the set time
            - Skip pinned tabs, tabs playing audio and whitelisted sites
            - Suspend or wake all tabs in a window from the popup
            - Show estimated memory saved in the popup
Storage:    chrome.storage.local (settings, activity times)
Tech stack: JavaScript, Chrome Extension Manifest V3 (tabs.discard, alarms)
```

---

## Example 615

**Intent:**
I need to take screenshots of whole long web pages, not just the visible part, and save them as PNG or PDF.

**Spec:**
```
Type:       Browser extension
Features:   - Capture the visible area, a selected region or the full scrolling page
            - Scroll the page and stitch the captures into one image
            - Hide sticky headers while capturing to avoid repeats
            - Preview the screenshot in a new tab before saving
            - Save the screenshot as PNG, JPEG or PDF
            - Copy the screenshot to the clipboard
Storage:    Downloads folder (saved files)
Tech stack: JavaScript, Chrome Extension Manifest V3 (tabs.captureVisibleTab, downloads), jsPDF
```

---

## Example 616

**Intent:**
Please make extension what generate strong password when I am on sign up page, and fill it in the field automatic.

**Spec:**
```
Type:       Browser extension
Data model: GeneratorSettings(length, use_uppercase, use_digits, use_symbols, exclude_similar)
Features:   - Detect new-password fields on sign-up forms
            - Show a small key icon inside the password field
            - Generate a random password with the chosen rules using a secure random source
            - Fill the password and confirm-password fields at once
            - Copy the generated password to the clipboard
            - Configure length and character types in the popup
Storage:    chrome.storage.sync (generator settings)
Tech stack: JavaScript, Chrome Extension Manifest V3, Web Crypto API (getRandomValues)
```

---

## Example 617

**Intent:**
reviewing pull requests on github is painful when there are 100 files, i want to collapse generated files and lockfiles automatically and see a file tree on the side

**Spec:**
```
Type:       Browser extension
Data model: Settings(collapse_patterns, show_file_tree, tree_width)
            ReviewProgress(pr_url, viewed_files, updated_at)
Features:   - Show a collapsible file tree beside the pull request diff
            - Collapse files that match patterns such as package-lock.json or *.generated.*
            - Jump to a file's diff by clicking it in the tree
            - Mark files as reviewed and remember progress per pull request
            - Filter the tree by file extension
Storage:    chrome.storage.sync (patterns), chrome.storage.local (review progress)
Tech stack: TypeScript, Chrome Extension Manifest V3 (content scripts), Preact
```

---

## Example 618

**Intent:**
double click a word and see its meaning

**Spec:**
```
Type:       Browser extension
Data model: LookupHistory(id, word, definition, page_url, looked_up_at)
Features:   - Look up a word when the user double-clicks it
            - Show the definition, part of speech and an example in a tooltip
            - Play the word's pronunciation audio
            - Keep a history of looked-up words in the popup
            - Export the word history as a CSV file for study
Storage:    chrome.storage.local (lookup history)
Tech stack: JavaScript, Chrome Extension Manifest V3, Free Dictionary API
```

---

## Example 619

**Intent:**
I'm applying to a lot of jobs on LinkedIn and Indeed and lose track of where I applied. Could there be a button on the job page that saves the job to a list where I can mark the status, like applied, interview, rejected?

**Spec:**
```
Type:       Browser extension
Data model: Job(id, title, company, location, url, source_site, saved_at)
            Application(id, job_id -> Job, status, applied_at, notes)
Features:   - Add a "Save job" button to LinkedIn and Indeed job pages
            - Extract title, company and location from the job page
            - Show saved jobs in a board grouped by status
            - Change a job's status and add notes
            - Warn when visiting a job that was already saved
            - Export all applications as a CSV file
Storage:    chrome.storage.local (jobs and applications)
Tech stack: TypeScript, Chrome Extension Manifest V3 (content scripts), React
```

---

## Example 620

**Intent:**
something to fill forms with fake test data, im a QA tester and typing names and emails over and over is killing me

**Spec:**
```
Type:       Browser extension (developer tool)
Data model: FillProfile(id, name, locale)
            FieldRule(id, profile_id -> FillProfile, selector_or_name, generator_type)
Features:   - Fill all inputs on the page with realistic fake data in one click
            - Guess the data type from field name, type and label
            - Create profiles with custom rules for specific fields
            - Fill a single field from the right-click menu
            - Fill forms with a keyboard shortcut
Storage:    chrome.storage.sync (profiles and rules)
Tech stack: JavaScript, Chrome Extension Manifest V3 (contextMenus, commands), Faker.js
```

---

## Example 621

**Intent:**
color picker extension for web designers

**Spec:**
```
Type:       Browser extension
Data model: Palette(id, name, created_at)
            SavedColor(id, palette_id -> Palette, hex, rgb, hsl, source_url, saved_at)
Features:   - Pick any color on the page with an eyedropper
            - Show the color as HEX, RGB and HSL and copy it with one click
            - Save picked colors into named palettes
            - Extract the main colors used on the current page
            - Export a palette as CSS variables or JSON
Storage:    chrome.storage.local (colors and palettes)
Tech stack: JavaScript, Chrome Extension Manifest V3, EyeDropper API
```

---

## Example 622

**Intent:**
when i open a json api url in the browser its just one big ugly line, want it formatted and collapsable

**Spec:**
```
Type:       Browser extension (developer tool)
Features:   - Detect pages whose content is JSON
            - Show the JSON as a collapsible tree with syntax colors
            - Switch between tree view and raw view
            - Copy the path or value of any node
            - Filter keys and values with a search box
            - Make URLs inside the JSON clickable
Tech stack: TypeScript, Chrome Extension Manifest V3 (content scripts)
```

---

## Example 623

**Intent:**
Can my tabs get grouped automatically by website? Like all the google docs tabs together, all stackoverflow together.

**Spec:**
```
Type:       Browser extension
Data model: GroupRule(id, name, domain_patterns, color, collapsed)
Features:   - Group open tabs by domain automatically when they are opened
            - Create custom rules that put several domains in one group
            - Give each group a name and color
            - Ungroup all tabs or regroup the window from the popup
            - Skip grouping when a domain has only one tab
Storage:    chrome.storage.sync (group rules)
Tech stack: JavaScript, Chrome Extension Manifest V3 (tabs, tabGroups API)
```

---

## Example 624

**Intent:**
read it later list, but inside the browser

**Spec:**
```
Type:       Browser extension
Data model: Article(id, url, title, excerpt, content_text, saved_at, is_read, tags)
Features:   - Save the current page to the reading list from the toolbar or right-click menu
            - Store a clean text copy of the article for offline reading
            - Show unread articles in the popup, newest first
            - Mark articles as read and archive them
            - Tag articles and filter the list by tag
Storage:    IndexedDB (articles and text), chrome.storage.sync (settings)
Tech stack: JavaScript, Chrome Extension Manifest V3, Mozilla Readability, Dexie.js
```

---

## Example 625

**Intent:**
i watch lots of lectures on youtube and udemy, want keyboard shortcuts to speed up the video past 2x and skip back 10 sec

**Spec:**
```
Type:       Browser extension
Data model: Settings(speed_step, max_speed, skip_seconds, key_bindings, remember_speed_per_site)
Features:   - Detect HTML5 video elements on any page
            - Increase or decrease playback speed with keys, up to 16x
            - Skip back or forward a set number of seconds
            - Show the current speed in a small overlay on the video
            - Remember the last speed used on each site
            - Let the user change the key bindings
Storage:    chrome.storage.sync (settings)
Tech stack: JavaScript, Chrome Extension Manifest V3 (content scripts, HTMLMediaElement API)
```

---

## Example 626

**Intent:**
At checkout pages I want the extension to automatically try coupon codes it knows for that shop and keep the one that gives the biggest discount.

**Spec:**
```
Type:       Browser extension
Data model: Store(id, domain, coupon_input_selector, apply_button_selector, total_selector)
            Coupon(id, store_id -> Store, code, description, last_worked_at)
Features:   - Detect supported checkout pages by domain
            - Try each known coupon code by filling the coupon field and applying it
            - Read the order total after each code is applied
            - Keep the code that gives the lowest total
            - Show the savings found in a small banner
API:        REST
            GET  /stores/{domain}/coupons
            POST /coupons/{id}/result
Storage:    chrome.storage.local (cached coupons), PostgreSQL (coupon service)
Tech stack: TypeScript, Chrome Extension Manifest V3, Node.js + Express (coupon service)
```

---

## Example 627

**Intent:**
I have years of bookmarks and half of them are probably dead links now. help me find and clean them

**Spec:**
```
Type:       Browser extension
Data model: CheckResult(bookmark_id, url, status_code, redirect_url, checked_at)
Features:   - Read all bookmarks from the browser
            - Check each URL with a request and record the status code
            - List dead links (404, DNS errors, timeouts) and redirected links
            - Delete selected dead bookmarks in bulk
            - Update redirected bookmarks to their new URL
            - Find and remove duplicate bookmarks
Storage:    chrome.storage.local (last check results)
Tech stack: JavaScript, Chrome Extension Manifest V3 (bookmarks API, fetch)
```

---

## Example 628

**Intent:**
whats that font? extension

**Spec:**
```
Type:       Browser extension
Features:   - Turn on an inspect mode from the toolbar button
            - Show the font family, size, weight and line height of the hovered text
            - Show the color of the hovered text
            - Detect whether the font is loaded from Google Fonts or a local file
            - Copy the CSS font properties with one click
Tech stack: JavaScript, Chrome Extension Manifest V3 (content scripts, getComputedStyle)
```

---

## Example 629

**Intent:**
I'd like my browser to read articles out loud to me while I cook, with a nice voice and the possibility to change speed.

**Spec:**
```
Type:       Browser extension (accessibility)
Data model: Settings(voice_name, rate, pitch, highlight_words)
Features:   - Extract the main article text from the current page
            - Read the text aloud with a chosen voice
            - Play, pause and stop reading from the popup or a keyboard shortcut
            - Change reading speed and pitch
            - Highlight the sentence being read and scroll to it
            - Start reading from the selected paragraph
Storage:    chrome.storage.sync (voice settings)
Tech stack: JavaScript, Chrome Extension Manifest V3 (tts API), Mozilla Readability
```

---

## Example 630

**Intent:**
watch a webpage and notify me when something on it changes, like a "sold out" product coming back

**Spec:**
```
Type:       Browser extension
Data model: Watch(id, url, css_selector, check_interval_minutes, last_content_hash, last_checked_at)
            ChangeEvent(id, watch_id -> Watch, old_text, new_text, detected_at)
Features:   - Pick the part of a page to watch by clicking on it
            - Fetch the page in the background at the chosen interval
            - Compare the selected element's text with the last saved version
            - Send a browser notification when the content changes
            - Show a diff of old and new text in the popup
            - Pause or delete watches
Storage:    chrome.storage.local (watches and change history)
Tech stack: JavaScript, Chrome Extension Manifest V3 (alarms, offscreen document, notifications)
```

---

## Example 631

**Intent:**
let me add my own CSS to specific websites to fix ugly layouts

**Spec:**
```
Type:       Browser extension
Data model: StyleRule(id, name, url_pattern, css, enabled, updated_at)
Features:   - Write custom CSS for a site in an editor in the popup
            - Inject the CSS automatically on pages matching the URL pattern
            - Preview changes live on the current tab while typing
            - Turn individual styles on or off
            - Import and export styles as a JSON file
Storage:    chrome.storage.sync (style rules)
Tech stack: TypeScript, Chrome Extension Manifest V3 (scripting.insertCSS), CodeMirror
```

---

## Example 632

**Intent:**
im a teacher and i do classes on google meet, i want an extension that records who joined and when and gives me a attendance sheet

**Spec:**
```
Type:       Browser extension
Data model: Meeting(id, meet_code, title, started_at, ended_at)
            AttendanceRecord(id, meeting_id -> Meeting, participant_name, joined_at, left_at, total_minutes)
Features:   - Detect when the user joins a Google Meet call
            - Read the participant list every 30 seconds
            - Record join and leave times for each participant
            - Calculate total minutes present per participant
            - Show past meetings in the popup
            - Export a meeting's attendance as a CSV or Excel file
Storage:    chrome.storage.local (meetings and attendance)
Tech stack: JavaScript, Chrome Extension Manifest V3 (content scripts), SheetJS
```

---

## Example 633

**Intent:**
I'm a frontend developer and I need to check if my pages pass WCAG color contrast rules. An extension that scans the page, marks every text element with bad contrast and suggests a fixed color would save me a lot of time.

**Spec:**
```
Type:       Browser extension (developer tool)
Data model: ContrastIssue(selector, text_sample, foreground, background, ratio, required_ratio, level)
Features:   - Scan all visible text elements on the current page
            - Calculate the contrast ratio between text and background colors
            - Mark elements failing WCAG AA or AAA with an outline on the page
            - List failing elements in a DevTools panel with their ratios
            - Suggest the nearest foreground color that passes
            - Export the issue list as a JSON report
Tech stack: TypeScript, Chrome Extension Manifest V3 (devtools_page, content scripts)
```

---

## Example 634

**Intent:**
extension that writes alt text for images that dont have it, for blind users with screen reader

**Spec:**
```
Type:       Browser extension (accessibility)
Data model: AltTextCache(image_url_hash, description, created_at)
Features:   - Find images on the page with missing or empty alt attributes
            - Send each image to a vision model to get a short description
            - Set the description as the image's alt text for screen readers
            - Describe a single image on demand from the right-click menu
            - Cache descriptions so the same image is not sent twice
Storage:    chrome.storage.local (description cache)
Tech stack: JavaScript, Chrome Extension Manifest V3, vision-capable LLM API
```

---

## Example 635

**Intent:**
how much time I waste on each site per day, show me

**Spec:**
```
Type:       Browser extension
Data model: DailyUsage(date, hostname, seconds_active)
Features:   - Track active time on each site while the tab is focused
            - Stop counting when the browser is idle or minimized
            - Show today's top sites with time spent in the popup
            - Show a weekly chart of total browsing time
            - Reset or delete history for a chosen day
Storage:    chrome.storage.local (daily usage)
Tech stack: JavaScript, Chrome Extension Manifest V3 (tabs, idle, windows API), Chart.js
```

---

## Example 636

**Intent:**
switch tabs fast with a search box like ctrl+p in vscode

**Spec:**
```
Type:       Browser extension
Features:   - Open a search overlay with a keyboard shortcut
            - Fuzzy search open tabs by title and URL
            - Switch to the selected tab with Enter
            - Close tabs from the result list with a shortcut
            - Include recently closed tabs and bookmarks in results
Tech stack: TypeScript, Chrome Extension Manifest V3 (tabs, sessions, commands), Fuse.js
```

---

## Example 637

**Intent:**
I learn Spanish by watching Netflix. I want to see two subtitles at the same time, the Spanish and the English, and click a word to save it for learning later.

**Spec:**
```
Type:       Browser extension
Data model: SavedWord(id, word, translation, sentence, show_title, timestamp_seconds, saved_at)
Features:   - Load a second subtitle track in the user's native language
            - Show both subtitle lines on the video at the same time
            - Pause the video and show a translation when a word is clicked
            - Save clicked words with their sentence and time in the episode
            - Review saved words in a list and export them for Anki
Storage:    chrome.storage.local (saved words)
Tech stack: JavaScript, Chrome Extension Manifest V3 (content scripts), translation API
```

---

## Example 638

**Intent:**
I copy stuff all day and lose what I copied 5 minutes ago. Want a clipboard history app, would like it built with Tauri so it's light.

**Spec:**
```
Type:       Desktop application (system tray)
Data model: ClipItem(id, content_type, text, image_path, source_app, pinned, copied_at)
Features:   - Watch the system clipboard and save every new text or image
            - Open a searchable history window with a global hotkey
            - Paste a selected item back into the active app
            - Pin items so they are never removed
            - Ignore copies from password managers
            - Delete items older than a set number of days
Storage:    Local SQLite database (rusqlite), app data folder for images
Tech stack: Tauri, Rust, TypeScript, Svelte, tauri-plugin-clipboard, tauri-plugin-global-shortcut
```

---

## Example 639

**Intent:**
screen recorder that also shows my webcam in a corner, for making tutorials

**Spec:**
```
Type:       Desktop application
Data model: Recording(id, file_path, duration_seconds, resolution, created_at)
            Settings(output_folder, fps, webcam_position, webcam_size, mic_device_id)
Features:   - Record the full screen, one window or a selected region
            - Overlay the webcam in a chosen corner as a circle or rectangle
            - Record microphone and system audio
            - Pause and resume recording with a hotkey
            - Save recordings as MP4 files and list them in a library
            - Trim the start and end of a recording before exporting
Storage:    Local video files, electron-store (settings)
Tech stack: Electron, TypeScript, desktopCapturer, MediaRecorder API, FFmpeg
```

---

## Example 640

**Intent:**
I don't trust cloud password managers. I want a desktop password manager that keeps everything encrypted in one file on my computer, with a master password, and can generate passwords too.

**Spec:**
```
Type:       Desktop application
Auth:       Master password (key derived with Argon2id)
Data model: Vault(id, kdf_salt, kdf_params, created_at)
            Entry(id, vault_id -> Vault, title, username, password_encrypted, url, notes, folder, updated_at)
Features:   - Create a vault protected by a master password
            - Encrypt the whole vault with AES-256-GCM before writing it to disk
            - Add, edit, delete and search password entries
            - Generate strong passwords with chosen length and characters
            - Copy a password to the clipboard and clear it after 30 seconds
            - Lock the vault automatically after a period of inactivity
Storage:    Single encrypted vault file on local disk
Tech stack: C#, .NET 8, WPF, System.Security.Cryptography, Konscious Argon2
```

---

## Example 641

**Intent:**
markdown editor with side by side preview

**Spec:**
```
Type:       Desktop application
Features:   - Open, edit and save .md files from the local disk
            - Show a live HTML preview next to the editor with synced scrolling
            - Highlight Markdown syntax and fenced code blocks
            - Render tables, task lists and math formulas
            - Export the document as HTML or PDF
            - Show a file tree for an opened folder
Storage:    Local Markdown files
Tech stack: Electron, TypeScript, CodeMirror 6, markdown-it, KaTeX
```

---

## Example 642

**Intent:**
i have a big collection of flac and mp3 files and every music player i try is bloated. want a simple fast one that reads the tags and lets me make playlists

**Spec:**
```
Type:       Desktop application
Data model: Track(id, file_path, title, artist, album, track_number, duration_seconds, year)
            Playlist(id, name, created_at)
            PlaylistTrack(playlist_id -> Playlist, track_id -> Track, position)
Features:   - Scan music folders and read tags from FLAC and MP3 files
            - Browse the library by artist, album and track
            - Play, pause, skip and seek with a gapless audio engine
            - Create playlists and reorder tracks by drag and drop
            - Search the library as the user types
            - Control playback with media keys
Storage:    Local SQLite database (library index)
Tech stack: Rust, Tauri, Svelte, symphonia (decoding), rodio (playback), lofty (tags)
```

---

## Example 643

**Intent:**
track how much time i spend in each app on my computer automatically

**Spec:**
```
Type:       Desktop application (background tracker)
Data model: ActivitySample(id, app_name, window_title, started_at, ended_at)
            Category(id, name, app_patterns, is_productive)
Features:   - Record the active window and app every few seconds
            - Pause tracking when the user is idle for 5 minutes
            - Group apps into categories such as work, social and games
            - Show daily and weekly time per app and category as charts
            - Export activity to a CSV file
Storage:    Local SQLite database
Tech stack: Python, PySide6, psutil, pywin32 (active window), SQLite
```

---

## Example 644

**Intent:**
small tray app that warns me when laptop battery is at 80% so i unplug it

**Spec:**
```
Type:       Desktop application (system tray)
Data model: Settings(upper_threshold, lower_threshold, check_interval_seconds, start_with_windows)
Features:   - Show the battery percentage in the system tray icon
            - Check the battery level at a set interval
            - Notify the user to unplug when charge reaches the upper threshold
            - Notify the user to plug in when charge drops below the lower threshold
            - Start automatically with Windows
Storage:    JSON settings file in the user's AppData folder
Tech stack: C#, .NET 8, WinForms (NotifyIcon), Windows toast notifications
```

---

## Example 645

**Intent:**
I work with people in 4 timezones. A SwiftUI menu bar app for my Mac that shows their local times would be great.

**Spec:**
```
Type:       Desktop application (macOS menu bar)
Data model: Clock(id, label, time_zone_identifier, sort_order)
Features:   - Show the time of a chosen city in the menu bar
            - List all configured time zones in a dropdown with their offset
            - Add, rename, reorder and remove clocks
            - Show a time slider to compare a future time across all zones
            - Mark hours outside 9-to-6 working time in a different color
Storage:    UserDefaults (clocks)
Tech stack: Swift, SwiftUI (MenuBarExtra), Foundation TimeZone
```

---

## Example 646

**Intent:**
Freelancer here. I want a Windows app in WPF to make invoices for my clients, save them, and print to PDF with my logo.

**Spec:**
```
Type:       Desktop application
Data model: Client(id, name, address, email, vat_number)
            Invoice(id, client_id -> Client, number, issue_date, due_date, status, currency)
            InvoiceLine(id, invoice_id -> Invoice, description, quantity, unit_price, tax_rate)
            BusinessProfile(name, address, logo_path, bank_details)
Features:   - Manage a list of clients
            - Create invoices with line items and automatic totals and tax
            - Number invoices automatically in sequence
            - Export an invoice as a PDF with the business logo
            - Mark invoices as paid and filter unpaid ones
Storage:    Local SQLite database (Entity Framework Core)
Tech stack: C#, .NET 8, WPF, MVVM (CommunityToolkit.Mvvm), QuestPDF
```

---

## Example 647

**Intent:**
resize lots of pictures at once with a simple window, drag and drop

**Spec:**
```
Type:       Desktop application
Features:   - Add images by dragging files or folders onto the window
            - Resize to a set width, height or percentage keeping the aspect ratio
            - Convert to JPEG, PNG or WebP with a quality setting
            - Choose the output folder and a file name suffix
            - Show a progress bar while processing in a background thread
Input:      Image files (.jpg, .png, .webp, .bmp)
Tech stack: Python, PyQt6, Pillow
```

---

## Example 648

**Intent:**
pomodoro timer for desktop in python tkinter

**Spec:**
```
Type:       Desktop application
Data model: Session(id, type, started_at, duration_minutes, completed)
Features:   - Run 25-minute work timers and 5-minute short breaks
            - Start a 15-minute long break after every 4 work sessions
            - Play a sound and show a popup when a timer ends
            - Let the user change work and break durations
            - Show the number of completed sessions today
Storage:    Local SQLite database (session history)
Tech stack: Python, Tkinter, sqlite3, playsound
```

---

## Example 649

**Intent:**
podcast app for the computer that downloads new episodes of my shows automatically

**Spec:**
```
Type:       Desktop application
Data model: Podcast(id, title, feed_url, image_url, last_checked_at)
            Episode(id, podcast_id -> Podcast, title, audio_url, published_at, local_path, played_seconds, is_played)
Features:   - Subscribe to a podcast by RSS feed URL or search
            - Check feeds for new episodes every hour
            - Download new episodes in the background
            - Play episodes and remember the playback position
            - Mark episodes as played and delete old downloads
Storage:    Local SQLite database, downloaded audio files
Tech stack: Electron, React, TypeScript, rss-parser, better-sqlite3
```

---

## Example 650

**Intent:**
my disk is full and i dont know whats taking the space, show it visualy

**Spec:**
```
Type:       Desktop application
Features:   - Scan a drive or folder and calculate folder sizes recursively
            - Show the result as an interactive treemap
            - Show a sorted list of the largest files and folders
            - Open a file's location or delete it from the app
            - Filter by file type such as video, archives and images
Input:      Drive or folder chosen by the user
Tech stack: Rust, Tauri, React, walkdir, D3.js (treemap)
```

---

## Example 651

**Intent:**
Need a tool to take a screenshot and draw arrows, boxes and blur parts before I send it to support team.

**Spec:**
```
Type:       Desktop application
Features:   - Capture a region of the screen with a global hotkey
            - Draw arrows, rectangles, text and numbered markers on the capture
            - Blur or pixelate selected areas to hide private data
            - Undo and redo edits
            - Copy the result to the clipboard or save it as PNG
Storage:    Local image files
Tech stack: C++, Qt 6 (QScreen, QPainter)
```

---

## Example 652

**Intent:**
find duplicate files on my pc even if they have different names

**Spec:**
```
Type:       Desktop application
Data model: FileEntry(path, size_bytes, quick_hash, full_hash, modified_at)
            DuplicateGroup(id, full_hash, total_wasted_bytes)
Features:   - Scan chosen folders and group files by size first
            - Compare files of the same size with a partial hash, then a full hash
            - Show groups of identical files with their paths and sizes
            - Auto-select all but the newest file in each group
            - Move selected duplicates to the recycle bin
Input:      One or more folders chosen by the user
Tech stack: C#, .NET 8, Avalonia UI, xxHash
```

---

## Example 653

**Intent:**
I look at screen too long and my eyes hurt. Can you make a app that remind me every 20 minutes to look away for 20 seconds, with a full screen message?

**Spec:**
```
Type:       Desktop application (system tray)
Data model: Settings(interval_minutes, break_seconds, allow_skip, pause_during_fullscreen)
Features:   - Show a full-screen overlay every 20 minutes with a 20-second countdown
            - Close the overlay automatically when the countdown ends
            - Skip or postpone a break with a button
            - Pause reminders while a full-screen app or video is running
            - Pause and resume reminders from the tray menu
Storage:    JSON settings file in the user config folder
Tech stack: Electron, JavaScript, electron-store
```

---

## Example 654

**Intent:**
desktop rss reader

**Spec:**
```
Type:       Desktop application
Data model: Feed(id, title, url, folder, last_fetched_at)
            Item(id, feed_id -> Feed, title, link, summary, published_at, is_read, is_starred)
Features:   - Add feeds by URL or import an OPML file
            - Refresh all feeds every 30 minutes
            - Show items in a three-pane layout: feeds, items, reading view
            - Mark items as read or starred
            - Organize feeds into folders
Storage:    Local SQLite database
Tech stack: Python, PySide6, feedparser
```

---

## Example 655

**Intent:**
a simple app to open sqlite database files, see the tables and run queries

**Spec:**
```
Type:       Desktop application (developer tool)
Data model: QueryHistory(id, database_path, sql, run_at, row_count, duration_ms)
Features:   - Open a .sqlite or .db file from disk
            - List tables, views and their column definitions
            - Browse table rows with paging and column sorting
            - Run SQL queries in an editor with syntax highlighting
            - Edit cell values and save changes in a transaction
            - Export query results as CSV
Storage:    Local SQLite file for query history
Tech stack: Rust, Tauri, rusqlite, Vue 3, Monaco Editor
```

---

## Example 656

**Intent:**
i have like 3000 fonts installed and cant find anything. app to preview them with my own text and group them

**Spec:**
```
Type:       Desktop application
Data model: Font(id, family, style, file_path, is_installed, format)
            Collection(id, name)
            CollectionFont(collection_id -> Collection, font_id -> Font)
Features:   - List installed fonts and fonts in chosen folders
            - Preview every font with custom sample text and size
            - Filter fonts by serif, sans-serif, monospace or script
            - Group fonts into collections such as "branding" or "headings"
            - Activate or deactivate fonts without deleting the files
Storage:    Local SQLite database
Tech stack: C#, .NET 8, WPF, SixLabors.Fonts
```

---

## Example 657

**Intent:**
On Windows I want to press a shortcut and have my windows arranged in a layout I saved, like browser on left 60% and terminal and slack stacked on the right.

**Spec:**
```
Type:       Desktop application (system tray)
Data model: Layout(id, name, hotkey)
            Zone(id, layout_id -> Layout, x_percent, y_percent, width_percent, height_percent, app_match)
Features:   - Draw layouts by splitting the screen into zones
            - Assign an app to each zone by executable name or window title
            - Move and resize matching windows into zones with a global hotkey
            - Save several layouts and switch between them
            - Support multiple monitors with different resolutions
Storage:    JSON file in the user's AppData folder
Tech stack: C#, .NET 8, WPF, Win32 API (SetWindowPos, RegisterHotKey)
```

---

## Example 658

**Intent:**
teleprompter app that scrolls my script while i record videos

**Spec:**
```
Type:       Desktop application
Data model: Script(id, title, text, font_size, scroll_speed, updated_at)
Features:   - Paste or import a script from a text or Word file
            - Scroll the text smoothly at an adjustable speed
            - Mirror the text horizontally for teleprompter glass
            - Control play, pause and speed with the keyboard or a remote
            - Show a reading marker line in the middle of the screen
Storage:    Local JSON files (scripts)
Tech stack: Electron, React, TypeScript, mammoth (Word import)
```

---

## Example 659

**Intent:**
typing practice program that shows me which keys i make most mistakes on

**Spec:**
```
Type:       Desktop application
Data model: TestResult(id, wpm, accuracy, duration_seconds, taken_at)
            KeyStat(key, presses, errors, avg_delay_ms)
Features:   - Show practice text and color each typed character as correct or wrong
            - Calculate words per minute and accuracy after each test
            - Track errors and delay for each key
            - Show a keyboard heatmap of the weakest keys
            - Generate practice texts focused on the weakest keys
            - Show progress over time as a line chart
Storage:    Local SQLite database
Tech stack: Python, PySide6, pyqtgraph
```

---

## Example 660

**Intent:**
I want to merge, split and rotate PDF pages on both my Windows PC and my Mac, made with .NET MAUI please.

**Spec:**
```
Type:       Desktop application (cross-platform)
Features:   - Open one or more PDF files and show page thumbnails
            - Reorder pages by drag and drop across files
            - Rotate or delete selected pages
            - Merge files into one PDF or split by page ranges
            - Save the result as a new PDF file
Input:      PDF files chosen by the user
Tech stack: C#, .NET 8, .NET MAUI (Windows and macOS), PdfSharpCore, PDFium (thumbnails)
```

---

## Example 661

**Intent:**
send files between my computers on the same wifi without usb stick or cloud

**Spec:**
```
Type:       Desktop application (peer-to-peer)
Data model: Device(id, name, ip_address, port, last_seen_at, trusted)
            Transfer(id, device_id -> Device, file_name, size_bytes, direction, status, finished_at)
Features:   - Discover other computers running the app on the local network with mDNS
            - Send files or folders by dragging them onto a device
            - Ask the receiver to accept or decline each transfer
            - Encrypt transfers with TLS and a pairing code
            - Show transfer progress and speed
Storage:    Local SQLite database (devices, transfer history), Downloads folder
Tech stack: Go, Wails, Svelte, zeroconf (mDNS)
```

---

## Example 662

**Intent:**
flash cards app for studying for medical exams, the kind that shows hard cards more often

**Spec:**
```
Type:       Desktop application
Data model: Deck(id, name, created_at)
            Card(id, deck_id -> Deck, front, back, image_path)
            Review(id, card_id -> Card, rating, reviewed_at, interval_days, ease_factor, due_at)
Features:   - Create decks and cards with text and images
            - Schedule reviews with the SM-2 spaced repetition algorithm
            - Show due cards and let the user rate them from "again" to "easy"
            - Import decks from CSV files
            - Show stats on cards reviewed per day and retention
Storage:    Local SQLite database
Tech stack: Electron, React, TypeScript, better-sqlite3
```

---

## Example 663

**Intent:**
i record interviews for my research and need them as text, but the audio can not leave my computer for privacy. can you make a desktop app that transcribes them locally

**Spec:**
```
Type:       Desktop application
Data model: Transcript(id, audio_path, language, model_size, created_at)
            Segment(id, transcript_id -> Transcript, start_seconds, end_seconds, speaker, text)
Features:   - Import audio files (MP3, WAV, M4A) by drag and drop
            - Transcribe audio fully offline with a local Whisper model
            - Show the transcript with timestamps and play audio from any segment
            - Edit transcript text and speaker names
            - Export transcripts as TXT, DOCX or SRT
Storage:    Local SQLite database, local model files
Tech stack: Python, PySide6, faster-whisper, python-docx
```

---

## Example 664

**Intent:**
mac app to pick any color on screen and keep a palette

**Spec:**
```
Type:       Desktop application (macOS menu bar)
Data model: PickedColor(id, hex, red, green, blue, picked_at, palette_name)
Features:   - Pick a color anywhere on screen with a magnifier loupe
            - Copy the color as HEX, RGB, HSL or SwiftUI Color code
            - Keep a history of recent picks in the menu bar dropdown
            - Save colors into named palettes
            - Pick a color with a global keyboard shortcut
Storage:    SwiftData (colors and palettes)
Tech stack: Swift, SwiftUI, AppKit (NSColorSampler), KeyboardShortcuts
```

---

## Example 665

**Intent:**
show internet upload and download speed in taskbar tray all the time

**Spec:**
```
Type:       Desktop application (system tray)
Data model: UsageDay(date, bytes_received, bytes_sent)
Features:   - Read network interface counters every second
            - Show current download and upload speed in the tray icon tooltip and label
            - Let the user pick which network adapter to monitor
            - Show total data used today and this month
            - Alert when monthly usage passes a set limit
Storage:    Local JSON file (daily usage)
Tech stack: Python, pystray, psutil, Pillow (tray icon drawing)
```

---

## Example 666

**Intent:**
My father has small hardware shop and still writes stock in a notebook. I want to make him a simple Windows program for products, stock in and out, and see what is low.

**Spec:**
```
Type:       Desktop application
Data model: Product(id, name, sku, category, unit, price, min_stock, current_stock)
            StockMovement(id, product_id -> Product, type, quantity, note, moved_at)
            Supplier(id, name, phone)
Features:   - Add, edit and search products by name or SKU
            - Record stock coming in and going out
            - Update the current stock level after each movement
            - Show a list of products below their minimum stock
            - Print a daily movement report
            - Back up the database to a USB drive
Storage:    Local SQLite database (Entity Framework Core)
Tech stack: C#, .NET 8, WPF, Material Design in XAML
```

---

## Example 667

**Intent:**
Mod manager for Skyrim that installs mods from zip files, lets me turn them on and off and change load order, without messing the game folder.

**Spec:**
```
Type:       Desktop application
Data model: Game(id, name, install_path, data_folder)
            Mod(id, game_id -> Game, name, version, archive_path, staging_path, enabled)
            LoadOrderEntry(mod_id -> Mod, position)
Features:   - Install mods from zip, 7z and rar archives into a staging folder
            - Enable and disable mods without changing the original game files
            - Link enabled mods into the game data folder with hard links
            - Change the load order by drag and drop
            - Detect file conflicts between mods and show which one wins
Storage:    Local SQLite database, staging folder on disk
Tech stack: C#, .NET 8, Avalonia UI, SharpCompress
```

---

## Example 668

**Intent:**
gui for ffmpeg so i can convert videos without typing commands

**Spec:**
```
Type:       Desktop application
Data model: Preset(id, name, container, video_codec, audio_codec, resolution, crf)
            Job(id, input_path, output_path, preset_id -> Preset, status, progress_percent)
Features:   - Add videos to a queue by drag and drop
            - Choose an output format and quality from presets
            - Build the ffmpeg command from the chosen options
            - Run conversions in a queue and show progress from ffmpeg output
            - Cancel a running job
            - Save custom presets
Storage:    Local JSON file (presets)
Tech stack: Electron, TypeScript, React, FFmpeg (bundled binary)
```

---

## Example 669

**Intent:**
hold a key and see all shortcuts of the current app on screen

**Spec:**
```
Type:       Desktop application (macOS overlay)
Features:   - Detect the frontmost application
            - Read the app's menu items and their keyboard shortcuts via the Accessibility API
            - Show the shortcuts in a full-screen overlay while the Command key is held
            - Group shortcuts by menu
            - Hide the overlay when the key is released
Tech stack: Swift, SwiftUI, AppKit, Accessibility API (AXUIElement)
```

---

## Example 670

**Intent:**
change my desktop wallpaper every morning with a nice photo from unsplash

**Spec:**
```
Type:       Desktop application (system tray)
Data model: Settings(search_topics, change_time, keep_last_n)
            Wallpaper(id, unsplash_id, photographer, local_path, set_at, is_favourite)
Features:   - Download a photo matching the chosen topics once a day
            - Set the photo as the desktop wallpaper
            - Show the photographer's name and link in the tray menu
            - Skip to a new photo or mark the current one as favourite
            - Delete old downloaded photos, keeping favourites
API:        REST (Unsplash)
            GET  /photos/random?query={topic}&orientation=landscape
Storage:    Local images folder, JSON settings file
Tech stack: Go, systray, Unsplash API, wallpaper library
```

---

## Example 671

**Intent:**
VS Code extension that finds all TODO and FIXME comments in my project and lists them in the sidebar

**Spec:**
```
Type:       VS Code extension
Features:   - Search the workspace for TODO, FIXME and HACK comments
            - Show results in a tree view grouped by file
            - Jump to the comment's line when an item is clicked
            - Highlight the tags in the editor with colors
            - Update the list when files are saved
            - Let the user add custom tags in settings
Storage:    VS Code workspace settings
Tech stack: TypeScript, VS Code Extension API (TreeDataProvider), ripgrep
```

---

## Example 672

**Intent:**
see who changed each line in vscode without leaving the editor, like git blame next to the code

**Spec:**
```
Type:       VS Code extension
Features:   - Show author, date and commit message at the end of the current line
            - Show full commit details on hover
            - Open the commit's diff from the hover
            - Show blame for the whole file in the gutter on demand
            - Cache blame results per file until it changes
Tech stack: TypeScript, VS Code Extension API (decorations, HoverProvider), git CLI
```

---

## Example 673

**Intent:**
in our react app we use translation keys like t('home.title') and i never know what text it is. show the english text next to the key in the editor

**Spec:**
```
Type:       VS Code extension
Features:   - Load translation JSON files from a configured locales folder
            - Detect t('key') calls in JS, TS, JSX and TSX files
            - Show the translated text inline after each key
            - Warn about keys missing in any language
            - Autocomplete translation keys while typing
            - Jump to the key's definition in the JSON file
Tech stack: TypeScript, VS Code Extension API (InlayHintsProvider, CompletionItemProvider, Diagnostics)
```

---

## Example 674

**Intent:**
regex tester inside vscode

**Spec:**
```
Type:       VS Code extension
Features:   - Open a side panel with a regex input and sample text
            - Highlight matches and capture groups as the user types
            - Switch flags such as global, ignore case and multiline
            - Run the regex against the current file and highlight matches in the editor
            - Explain each part of the regex in plain words
Tech stack: TypeScript, VS Code Extension API (Webview), regexp-tree
```

---

## Example 675

**Intent:**
Before every commit I forget console.log statements in my code. I want a VS Code extension that highlights them all and can remove them from the file or the whole project with one command.

**Spec:**
```
Type:       VS Code extension
Features:   - Highlight console.log, console.debug and debugger statements in JS and TS files
            - Show the number of statements in the status bar
            - Remove all statements from the current file with one command
            - Remove statements from the whole workspace after a confirmation
            - Ignore lines marked with a keep comment
Tech stack: TypeScript, VS Code Extension API (commands, decorations, WorkspaceEdit), Babel parser
```

---

## Example 676

**Intent:**
a vscode extension to save code snippets with tags and insert them later

**Spec:**
```
Type:       VS Code extension
Data model: Snippet(id, title, language, body, tags, created_at)
Features:   - Save selected code as a snippet with a title and tags
            - Browse snippets in a sidebar tree grouped by language
            - Search snippets by title or tag from the command palette
            - Insert a snippet at the cursor position
            - Sync snippets across machines with Settings Sync
Storage:    VS Code globalState (synced)
Tech stack: TypeScript, VS Code Extension API (TreeView, QuickPick)
```

---

## Example 677

**Intent:**
cli tool like create-react-app but for our company's node microservices template, using commander

**Spec:**
```
Type:       Command-line tool (project scaffolder)
Features:   - Ask for the service name, port and database type with interactive prompts
            - Copy the company template and replace placeholders in files
            - Add optional modules such as Docker, CI pipeline and OpenAPI docs
            - Install dependencies and initialize a git repository
            - Skip prompts when options are passed as flags
Input:      Command arguments: service name, --db, --port, --with <modules>
Tech stack: Node.js, commander, inquirer, Handlebars, execa
```

---

## Example 678

**Intent:**
helps me write commit messages in conventional commits format

**Spec:**
```
Type:       Command-line tool (git helper)
Features:   - Show staged files and ask for the commit type (feat, fix, docs, chore)
            - Ask for an optional scope, a short summary and a body
            - Mark breaking changes and add a BREAKING CHANGE footer
            - Check that the summary is under 72 characters
            - Run git commit with the built message
Input:      Interactive prompts in the terminal
Tech stack: Go, Cobra, Bubble Tea (prompts), go-git
```

---

## Example 679

**Intent:**
todo list in the terminal, written in go

**Spec:**
```
Type:       Command-line tool
Data model: Task(id, title, priority, due_date, project, done, created_at)
Features:   - Add a task with optional priority, due date and project
            - List open tasks sorted by priority and due date
            - Mark tasks as done or delete them
            - Filter tasks by project or show overdue tasks
            - Print tasks as a colored table
Input:      Subcommands: add, list, done, rm, with flags
Storage:    JSON file in the user's home folder (~/.todo.json)
Tech stack: Go, Cobra, lipgloss
```

---

## Example 680

**Intent:**
Convert big CSV files to JSON or JSON Lines really fast. I'd like it written in Rust with clap since some files are several GB.

**Spec:**
```
Type:       Command-line tool (file converter)
Features:   - Stream the CSV file row by row without loading it into memory
            - Write output as a JSON array or JSON Lines
            - Detect number, boolean and null values or keep everything as strings
            - Support custom delimiters and files without a header row
            - Read from stdin and write to stdout for piping
            - Show a progress bar for large files
Input:      CSV file path or stdin, flags: --format, --delimiter, --no-header, --infer-types
Tech stack: Rust, clap, csv, serde_json, indicatif
```

---

## Example 681

**Intent:**
check all the links in my markdown docs folder and tell me which ones are broken

**Spec:**
```
Type:       Command-line tool
Features:   - Find all .md files in a folder recursively
            - Extract inline links, reference links and image paths
            - Check external URLs with HTTP HEAD requests in parallel
            - Check that relative file links and #heading anchors exist
            - Print broken links with file name and line number
            - Exit with a non-zero code when broken links are found, for CI
Input:      Folder path, optional ignore patterns file
Tech stack: Node.js, commander, remark (Markdown parser), undici
```

---

## Example 682

**Intent:**
our app crashes in prod because someone forgot a variable in .env. want a cli that compares .env with .env.example and checks the values are right type

**Spec:**
```
Type:       Command-line tool (developer tool)
Features:   - Compare keys in .env with keys in .env.example
            - Report missing keys and extra keys not in the example
            - Validate value types from comments such as # type: int, url, bool
            - Mask secret values in all output
            - Exit with an error code so it can run before deploys
Input:      Paths to .env and .env.example (defaults to current folder)
Tech stack: Python, Typer, python-dotenv, Rich
```

---

## Example 683

**Intent:**
tail log files with colors for errors and warnings

**Spec:**
```
Type:       Command-line tool
Features:   - Follow one or more log files as new lines are written
            - Color lines by level: red for ERROR, yellow for WARN, gray for DEBUG
            - Filter lines by level or a search pattern
            - Pretty-print lines that contain JSON
            - Prefix each line with its file name when following several files
Input:      Log file paths, flags: --level, --grep, --json
Tech stack: Go, Cobra, fsnotify, fatih/color
```

---

## Example 684

**Intent:**
i have hundreds of old git branches that are already merged, delete them for me but ask first

**Spec:**
```
Type:       Command-line tool (git helper)
Features:   - List local branches already merged into main
            - List branches whose remote was deleted
            - Show the last commit date and author of each branch
            - Ask for confirmation in an interactive checklist before deleting
            - Protect main, develop and release branches from deletion
            - Delete remote branches as well with a flag
Input:      Run inside a git repository, flags: --base, --remote, --dry-run
Tech stack: Python, Click, GitPython, questionary
```

---

## Example 685

**Intent:**
convert all images in folder to webp

**Spec:**
```
Type:       Command-line tool (file converter)
Features:   - Find JPEG and PNG files in a folder, optionally recursive
            - Convert each image to WebP with a chosen quality
            - Keep PNG transparency in the output
            - Process files in parallel using all CPU cores
            - Print the size saved for each file and in total
Input:      Folder path, flags: --quality, --recursive, --delete-originals
Tech stack: Rust, clap, image, webp, rayon
```

---

## Example 686

**Intent:**
something is already using port 3000 again!! cli to see what process is on a port and kill it

**Spec:**
```
Type:       Command-line tool
Features:   - Find the process listening on a given port
            - Show the process name, PID and command line
            - Kill the process after confirmation, or at once with --force
            - List all listening ports and their processes
            - Work on Windows, macOS and Linux
Input:      Port number, flags: --force, --list
Tech stack: Node.js, commander, find-process, tree-kill
```

---

## Example 687

**Intent:**
I have several computers and want my config files (.bashrc, .gitconfig, vim, etc) synced between them through a git repo, with a tool that makes the symlinks for me.

**Spec:**
```
Type:       Command-line tool
Features:   - Move a config file into the dotfiles repo and replace it with a symlink
            - Create all symlinks on a new machine from the repo
            - Back up existing files before overwriting them
            - Choose files per machine or OS with a profile in a config file
            - Pull, commit and push the repo with one sync command
Input:      Subcommands: add, link, sync, status; config file dotfiles.toml
Storage:    Git repository in ~/.dotfiles
Tech stack: Go, Cobra, go-git, BurntSushi/toml
```

---

## Example 688

**Intent:**
tool to run SQL migration files in order and remember which ones already ran

**Spec:**
```
Type:       Command-line tool (database tool)
Data model: SchemaMigration(version, name, checksum, applied_at)
Features:   - Read migration files named like 0001_create_users.up.sql
            - Apply pending migrations in order inside transactions
            - Roll back the last migration using its .down.sql file
            - Show applied and pending migrations
            - Fail when an applied migration file was changed after running
Input:      Migrations folder, database URL from flag or DATABASE_URL
Storage:    schema_migrations table in the target database
Tech stack: Go, Cobra, pgx (PostgreSQL), go-sql-driver/mysql
```

---

## Example 689

**Intent:**
scan my repo for passwords and api keys that someone commited by mistake

**Spec:**
```
Type:       Command-line tool (security)
Features:   - Scan files in the working tree for secrets with regex rules
            - Scan the full git history, not only current files
            - Detect high-entropy strings that look like random keys
            - Ignore findings listed in an allowlist file
            - Print findings with file, line, commit and rule name
            - Install itself as a git pre-commit hook
Input:      Repository path, flags: --history, --config, --json
Tech stack: Python, Typer, GitPython, Rich
```

---

## Example 690

**Intent:**
generate CHANGELOG.md from git commits

**Spec:**
```
Type:       Command-line tool
Features:   - Read commits between the last tag and HEAD
            - Group commits by type such as features, fixes and breaking changes
            - Link commit hashes and issue numbers to the repository host
            - Add a new version section at the top of CHANGELOG.md
            - Suggest the next semantic version from the commit types
Input:      Git repository, flags: --from, --to, --release-as
Tech stack: Node.js, commander, conventional-commits-parser, simple-git
```

---

## Example 691

**Intent:**
I hate Postman being so heavy. Make me a CLI that runs requests written in .http files, supports variables for different environments and prints the response nicely.

**Spec:**
```
Type:       Command-line tool (HTTP client)
Features:   - Parse requests from .http files separated by ###
            - Replace {{variables}} with values from an environment file
            - Send a single named request or all requests in a file
            - Print status, headers and a pretty-printed, colored body
            - Save a value from a response to use in later requests
            - Assert status codes and exit with an error for CI
Input:      .http file path, flags: --env, --name, --verbose
Storage:    http-env.json (environments)
Tech stack: Rust, clap, reqwest, tokio, colored_json
```

---

## Example 692

**Intent:**
legal team asks which open source licenses we use. cli that lists the license of every dependency please

**Spec:**
```
Type:       Command-line tool
Features:   - Read dependencies from package-lock.json, requirements.txt or go.mod
            - Look up the license of each direct and transitive dependency
            - Group dependencies by license type
            - Flag licenses on a deny list such as GPL-3.0 or AGPL
            - Export the report as CSV or Markdown
Input:      Project folder, flags: --deny, --format
Tech stack: Python, Click, PyPI JSON API, npm registry API, Go proxy API
```

---

## Example 693

**Intent:**
want to track hours i spend on each client project from terminal, start and stop

**Spec:**
```
Type:       Command-line tool
Data model: Project(id, name, client, hourly_rate)
            TimeEntry(id, project_id -> Project, started_at, ended_at, note)
Features:   - Start a timer for a project with an optional note
            - Stop the running timer and save the entry
            - Show the current running timer and elapsed time
            - Print a report of hours per project for a week or month
            - Calculate the amount to bill using each project's hourly rate
            - Export entries to CSV
Input:      Subcommands: start, stop, status, report, export
Storage:    Local SQLite database in the user's home folder
Tech stack: Python, Typer, SQLite, Rich (tables)
```

---

## Example 694

**Intent:**
linter for our kubernetes yaml files with our own team rules

**Spec:**
```
Type:       Command-line tool (linter)
Features:   - Parse all YAML files in a folder, including multi-document files
            - Check custom rules such as required labels, resource limits and no latest image tag
            - Load rules from a config file with severity levels
            - Print errors with file name, line number and rule ID
            - Output results as text, JSON or SARIF for CI
Input:      Folder or file paths, flags: --config, --format
Tech stack: Go, Cobra, gopkg.in/yaml.v3
```

---

## Example 695

**Intent:**
small command to encrypt and decrypt a file with a password before i put it on google drive

**Spec:**
```
Type:       Command-line tool (security)
Features:   - Encrypt a file with a password using AES-256-GCM
            - Derive the key from the password with scrypt and a random salt
            - Decrypt a file and detect wrong passwords or tampering
            - Ask for the password without showing it on screen
            - Encrypt every file in a folder with one command
Input:      File or folder path, subcommands: encrypt, decrypt
Tech stack: Python, Click, cryptography
```

---

## Example 696

**Intent:**
docker eats my disk, clean old images containers and volumes but not the ones i use

**Spec:**
```
Type:       Command-line tool
Features:   - List stopped containers, dangling images and unused volumes with their sizes
            - Remove items older than a set age
            - Keep images matching a protect list such as postgres:*
            - Show what would be removed with a dry run
            - Print the total disk space freed
Input:      Flags: --older-than, --protect, --dry-run, --volumes
Tech stack: Go, Cobra, Docker Engine SDK for Go
```

---

## Example 697

**Intent:**
generate a README for my project automatically by looking at the code

**Spec:**
```
Type:       Command-line tool
Features:   - Detect the language, framework and package manager from project files
            - Read the project name, description and scripts from package.json or pyproject.toml
            - Generate install, usage and test sections from detected commands
            - Add a folder structure tree and license badge
            - Ask before overwriting an existing README.md
Input:      Project folder path
Tech stack: Node.js, commander, Handlebars, fast-glob
```

---

## Example 698

**Intent:**
Our backend team gives us JSON schema files and we write the TypeScript types by hand. Can you build a CLI that generates the types from the schemas, and can watch the folder?

**Spec:**
```
Type:       Command-line tool (code generator)
Features:   - Read JSON Schema files from a folder
            - Generate TypeScript interfaces and union types for each schema
            - Resolve $ref links between schema files
            - Add schema descriptions as JSDoc comments
            - Regenerate types when schema files change in watch mode
Input:      Schema folder and output folder, flags: --watch, --banner
Tech stack: Node.js, TypeScript, commander, json-schema-to-typescript, chokidar
```

---

## Example 699

**Intent:**
rename many files with regex find and replace, show preview first

**Spec:**
```
Type:       Command-line tool
Features:   - Match file names in a folder against a regex pattern
            - Build new names with a replacement using capture groups
            - Show a table of old and new names before renaming
            - Stop when two files would get the same new name
            - Undo the last rename from a saved log file
Input:      Folder path, pattern and replacement, flags: --recursive, --yes, --undo
Storage:    Rename log file (.rename-undo.json) in the folder
Tech stack: Rust, clap, regex, comfy-table
```

---

## Example 700

**Intent:**
see my stock prices in terminal updating live

**Spec:**
```
Type:       Command-line tool (terminal UI)
Data model: Holding(symbol, quantity, buy_price)
Features:   - Show a watch list of stock symbols with price and daily change
            - Refresh prices every 30 seconds
            - Color gains green and losses red
            - Calculate profit and loss for holdings from a config file
            - Show a small sparkline of today's price movement
API:        REST (market data provider)
            GET  /quote?symbol={symbol}
Storage:    YAML config file (~/.config/ticker.yaml)
Tech stack: Go, Bubble Tea, lipgloss, Finnhub API
```

---

## Example 701

**Intent:**
Which person contributed most to our repo? want a cli that gives stats per author, like commits and lines added and removed, for a time range.

**Spec:**
```
Type:       Command-line tool (git helper)
Features:   - Read the git log for a date range
            - Count commits, lines added and lines removed per author
            - Merge authors with several email addresses using a mailmap
            - Show the most changed files and directories
            - Print a table or export the stats as JSON
Input:      Repository path, flags: --since, --until, --format
Tech stack: Python, Typer, pydriller, Rich
```

---

## Example 702

**Intent:**
switching kubernetes contexts and namespaces is too many commands, make it one quick interactive command

**Spec:**
```
Type:       Command-line tool
Features:   - Read contexts from the kubeconfig file
            - Pick a context from a fuzzy-search list
            - List namespaces of the chosen cluster and pick one
            - Switch back to the previous context with a dash argument
            - Show the current context and namespace in a short line for the shell prompt
Input:      Optional context or namespace name, kubeconfig path from KUBECONFIG
Tech stack: Go, Cobra, client-go, go-fuzzyfinder
```

---

## Example 703

**Intent:**
take screenshot of a website from the command line, in different screen sizes

**Spec:**
```
Type:       Command-line tool
Features:   - Open a URL in a headless browser
            - Take screenshots at preset sizes for mobile, tablet and desktop
            - Capture the full page or only the visible area
            - Wait for a selector or a delay before capturing
            - Save screenshots as PNG files named by URL and size
Input:      One URL or a text file of URLs, flags: --sizes, --full-page, --wait-for
Tech stack: Node.js, commander, Playwright
```

---

## Example 704

**Intent:**
I run a gaming Discord server and people keep getting toxic in chat, can you make a bot with discord.py that catches it and warns them?

**Spec:**
```
Type:       Discord bot (moderation)
Data model: Guild(id, name, mod_channel_id, toxicity_threshold)
            Warning(id, guild_id -> Guild, user_id, message_text, score, created_at)
Features:   - Score every new message with a toxicity classification model
            - Delete messages that score above the server's threshold
            - Send the user a private warning with the reason
            - Log each removed message to a moderator channel
            - Time out users automatically after 3 warnings in 24 hours
            - Let moderators change the threshold with a /setthreshold slash command
Storage:    SQLite
Tech stack: Python, discord.py, Hugging Face Transformers (toxic comment classifier)
```

---

## Example 705

**Intent:**
telegram bot that turns voice messages into text

**Spec:**
```
Type:       Telegram bot (transcription)
Data model: User(telegram_id, language, created_at)
            Transcript(id, user_id -> User, duration_seconds, text, created_at)
Features:   - Receive voice messages and audio files sent to the bot
            - Convert OGG voice notes to WAV with ffmpeg
            - Transcribe the audio with a speech-to-text model
            - Reply with the transcript as a text message
            - Let users set their language with a /language command
            - Reject audio longer than 10 minutes
Storage:    SQLite
Tech stack: Python, python-telegram-bot, faster-whisper, ffmpeg
```

---

## Example 706

**Intent:**
our slack threads get super long and nobody reads them, would love a bot that sums them up when you ask

**Spec:**
```
Type:       Slack bot (summarisation)
Features:   - Respond to a /summarize slash command or an @mention inside a thread
            - Fetch every message in the thread with the Slack Web API
            - Summarise the thread into key points, decisions and open questions with an LLM
            - Post the summary as an ephemeral message visible only to the requester
            - Split very long threads into chunks and merge the partial summaries
API:        Webhook
            POST /slack/events
            POST /slack/commands
Tech stack: Python, Slack Bolt, LLM API
```

---

## Example 707

**Intent:**
A WhatsApp bot for my small dental clinic so patients can book, move or cancel appointments by texting, using Twilio. It should send them a reminder the day before and let the receptionist see all bookings.

**Spec:**
```
Type:       WhatsApp bot (appointment booking)
Auth:       Receptionist login (email + password) for the admin page; patients identified by phone number
Data model: Patient(id, phone, name)
            Slot(id, dentist_name, starts_at, is_booked)
            Appointment(id, patient_id -> Patient, slot_id -> Slot, status, created_at)
Features:   - Understand booking, rescheduling and cancelling requests from free-text messages
            - Offer the next available slots as a numbered list
            - Confirm the booking and mark the slot as taken
            - Send a reminder message 24 hours before each appointment
            - Show all upcoming appointments on a receptionist web page
API:        Webhook + REST
            POST /twilio/whatsapp
            GET  /admin/appointments
            PATCH /admin/appointments/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, Twilio WhatsApp API, APScheduler (reminders), LLM API (intent parsing)
```

---

## Example 708

**Intent:**
ask questions about our HR policy pdfs

**Spec:**
```
Type:       Document Q&A web app (RAG)
Auth:       Company single sign-on (OAuth 2.0 / OpenID Connect)
Data model: Document(id, title, file_path, uploaded_at)
            Chunk(id, document_id -> Document, text, page, embedding)
            Question(id, user_email, text, answer, created_at)
Features:   - Upload HR policy PDFs and split them into chunks
            - Create embeddings for every chunk
            - Answer employee questions using the most relevant chunks
            - Show the source document and page under each answer
            - Reply "I don't know" when no relevant policy is found
API:        REST
            POST /documents
            POST /ask
            GET  /documents
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, pypdf, embedding model API, LLM API, React
```

---

## Example 709

**Intent:**
i want to upload a recording of a meeting and get back a summary plus a list of who has to do what

**Spec:**
```
Type:       Web application (meeting summariser)
Auth:       User registration and login (email + password)
Data model: User(id, email, password_hash)
            Meeting(id, user_id -> User, title, audio_path, transcript, summary, created_at)
            ActionItem(id, meeting_id -> Meeting, owner, task, due_date)
Features:   - Upload an audio or video recording of a meeting
            - Transcribe the recording with speaker labels
            - Generate a short summary and list of decisions with an LLM
            - Extract action items with an owner and due date
            - Export the summary and action items as Markdown or email them
API:        REST
            POST /meetings
            GET  /meetings/{id}
            GET  /meetings/{id}/action-items
Storage:    PostgreSQL, S3-compatible object storage (recordings)
Tech stack: Python, FastAPI, Whisper, pyannote.audio (speaker diarisation), LLM API, Vue.js
```

---

## Example 710

**Intent:**
help me write cover letters

**Spec:**
```
Type:       Web application (AI writing assistant)
Data model: Profile(id, name, experience_summary, skills)
            CoverLetter(id, profile_id -> Profile, job_title, company, job_description, text, created_at)
Features:   - Save the user's experience and skills once as a profile
            - Paste a job description to generate a tailored cover letter
            - Choose the tone: formal, friendly or enthusiastic
            - Edit the draft and regenerate single paragraphs
            - Download the letter as DOCX or PDF
API:        REST
            POST /cover-letters
            GET  /cover-letters
            PUT  /cover-letters/{id}
Storage:    SQLite
Tech stack: Python, FastAPI, LLM API, python-docx, React
```

---

## Example 711

**Intent:**
wanna build my own alexa thing on a raspberry pi that works offline, like timers and basic questions

**Spec:**
```
Type:       Voice assistant (embedded device)
Data model: Timer(id, label, ends_at)
            Reminder(id, text, remind_at)
Features:   - Listen for a custom wake word all the time
            - Convert speech to text locally after the wake word
            - Match commands for timers, reminders, time and weather
            - Answer general questions with a small local LLM
            - Speak replies out loud with offline text-to-speech
Storage:    Local SQLite database
Tech stack: Python, openWakeWord, Vosk (offline speech-to-text), llama.cpp, Piper TTS, Raspberry Pi OS
```

---

## Example 712

**Intent:**
I have hours of podcast audio and need transcripts with who-said-what, in python with whisper

**Spec:**
```
Type:       Command-line script (transcription)
Features:   - Transcribe each audio file with Whisper
            - Detect and label different speakers
            - Merge speaker labels with transcript timestamps
            - Write the transcript as TXT, SRT and JSON
            - Process a whole folder of episodes in one run
Input:      Folder of audio files (.mp3, .wav, .m4a) and number of expected speakers
Tech stack: Python, openai-whisper, pyannote.audio, ffmpeg
```

---

## Example 713

**Intent:**
website where you drop a photo and it removes the background

**Spec:**
```
Type:       Web application (image editing)
Features:   - Upload a JPG or PNG by drag and drop
            - Remove the background with a segmentation model
            - Show a before/after preview
            - Replace the background with a solid colour or transparency
            - Download the result as a transparent PNG
API:        REST
            POST /remove-background
Storage:    Temporary file storage (deleted after 1 hour)
Tech stack: Python, FastAPI, rembg (U^2-Net), Pillow, HTML/CSS/JavaScript
```

---

## Example 714

**Intent:**
my son is in 5th grade and struggles with math, i was thinking an AI tutor that explains step by step and doesnt just give him the answer

**Spec:**
```
Type:       Web application (AI tutor)
Auth:       Parent account (email + password) with child profiles
Data model: Parent(id, email, password_hash)
            Child(id, parent_id -> Parent, name, grade)
            Session(id, child_id -> Child, topic, started_at)
            Message(id, session_id -> Session, role, text, created_at)
Features:   - Chat with the tutor about a math problem typed or photographed
            - Guide the child with hints and questions instead of final answers
            - Generate practice problems at the child's grade level
            - Track topics where the child makes repeated mistakes
            - Show the parent a weekly progress report
API:        REST
            POST /sessions
            POST /sessions/{id}/messages
            GET  /children/{id}/report
Storage:    PostgreSQL
Tech stack: Python, Django, LLM API, OCR for photographed problems, React
```

---

## Example 715

**Intent:**
A GitHub bot that reviews pull requests automatically. When a PR is opened it should read the diff, point out bugs or style issues as inline comments, and post an overall summary. Built with Node.js please.

**Spec:**
```
Type:       GitHub App (code review bot)
Auth:       GitHub App installation with a private key and webhook secret
Data model: Installation(id, github_installation_id, account_name)
            Review(id, installation_id -> Installation, repo, pr_number, commit_sha, created_at)
Features:   - Receive pull_request opened and synchronize events
            - Fetch the PR diff and split it by file
            - Ask an LLM to find bugs, risky code and style problems
            - Post findings as inline review comments on the right lines
            - Post an overall summary comment on the PR
            - Skip files that match an ignore list in .reviewbot.yml
API:        Webhook
            POST /api/github/webhooks
Storage:    PostgreSQL
Tech stack: Node.js, TypeScript, Probot, Octokit, LLM API
```

---

## Example 716

**Intent:**
sort my support inbox emails into categories and flag urgent ones

**Spec:**
```
Type:       Background service (email triage)
Data model: Email(id, message_id, sender, subject, body, category, urgency, received_at)
Features:   - Poll the support inbox for new emails every minute
            - Classify each email as billing, bug, feature request or other with an LLM
            - Score urgency and flag emails from angry or blocked customers
            - Apply matching Gmail labels to each email
            - Send a Slack alert for urgent emails
Storage:    SQLite
Tech stack: Python, Gmail API, LLM API, Slack webhook
```

---

## Example 717

**Intent:**
we get like 300 applications per job, could AI read the CVs and rank who matches the job best

**Spec:**
```
Type:       Web application (resume screening)
Auth:       Recruiter login (email + password)
Data model: Job(id, title, description, required_skills)
            Candidate(id, job_id -> Job, name, email, resume_path, resume_text)
            Score(id, candidate_id -> Candidate, match_score, strengths, gaps)
Features:   - Create a job with a description and required skills
            - Bulk upload resumes as PDF or DOCX
            - Extract text and key details from each resume
            - Score each candidate against the job with an explanation
            - Rank candidates and filter by minimum score
            - Hide names and photos during scoring to reduce bias
API:        REST
            POST /jobs
            POST /jobs/{id}/resumes
            GET  /jobs/{id}/candidates
Storage:    PostgreSQL, S3 (resume files)
Tech stack: Python, FastAPI, pdfplumber, python-docx, LLM API, React
```

---

## Example 718

**Intent:**
an api that checks user comments for hate speech and spam before they get posted

**Spec:**
```
Type:       REST API service (content moderation)
Auth:       API key per client app (sent in the X-API-Key header)
Data model: ApiClient(id, name, api_key_hash)
            ModerationResult(id, client_id -> ApiClient, text_hash, labels, scores, decision, created_at)
Features:   - Classify text for hate speech, harassment, spam and sexual content
            - Return a score for each label and an allow, review or block decision
            - Let each client set its own thresholds
            - Process up to 100 comments in one batch request
            - Keep a log of decisions for appeals
API:        REST
            POST /moderate
            POST /moderate/batch
            PUT  /settings/thresholds
Storage:    PostgreSQL, Redis (rate limiting)
Tech stack: Python, FastAPI, Hugging Face Transformers, Redis
```

---

## Example 719

**Intent:**
translation service

**Spec:**
```
Type:       REST API service (translation)
Auth:       API key per client (sent in the Authorization header)
Data model: ApiClient(id, name, api_key_hash, monthly_quota)
            TranslationCache(source_hash, source_lang, target_lang, translated_text)
Features:   - Translate text between supported languages
            - Detect the source language automatically
            - Keep placeholders and HTML tags unchanged
            - Cache repeated translations
            - Count characters used per client per month
API:        REST
            POST /translate
            POST /detect
            GET  /languages
Storage:    PostgreSQL, Redis (cache)
Tech stack: Python, FastAPI, Hugging Face Transformers (MarianMT / NLLB models)
```

---

## Example 720

**Intent:**
a chat where you tell it your mood and what you liked before and it recommends movies to watch tonight

**Spec:**
```
Type:       Chatbot (recommendation, web)
Data model: User(id, session_id)
            Movie(id, title, year, genres, overview, embedding)
            Recommendation(id, user_id -> User, movie_id -> Movie, liked)
Features:   - Ask the user about their mood, favourite films and available time
            - Search the movie catalogue by similarity to the user's description
            - Explain each recommendation in one or two sentences
            - Let the user thumbs-up or thumbs-down suggestions
            - Refine the next suggestions using that feedback
API:        REST
            POST /chat
            POST /feedback
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, TMDB API (catalogue), embedding model API, LLM API, React
```

---

## Example 721

**Intent:**
I want an assistant in Slack that can actually book meetings for me — check everyone's calendars, find a free slot and send the invite. Using langchain for the agent part.

**Spec:**
```
Type:       AI agent (Slack bot with tools)
Auth:       Google OAuth 2.0 per user for calendar access
Data model: User(id, slack_user_id, google_refresh_token)
            ScheduleRequest(id, user_id -> User, request_text, status, event_id, created_at)
Features:   - Understand requests like "find 30 minutes with Anna and Raj next week"
            - Look up free/busy times of all attendees with a calendar tool
            - Propose up to 3 slots as buttons in Slack
            - Create the event and send invites when the user picks a slot
            - Ask a follow-up question when the request is unclear
API:        Webhook
            POST /slack/events
            POST /slack/interactions
Storage:    PostgreSQL
Tech stack: Python, LangChain (tool-calling agent), Slack Bolt, Google Calendar API, LLM API
```

---

## Example 722

**Intent:**
discord bot for movie trivia nights where the questions are made up by AI

**Spec:**
```
Type:       Discord bot (game)
Data model: Game(id, guild_id, channel_id, topic, status, started_at)
            Question(id, game_id -> Game, text, options, correct_option)
            Score(id, game_id -> Game, user_id, points)
Features:   - Start a trivia game with a /trivia slash command and a topic
            - Generate multiple-choice questions on that topic with an LLM
            - Show answer buttons and a 20-second countdown
            - Award points for correct answers, more for faster ones
            - Show a leaderboard at the end of each game and all-time
Storage:    SQLite
Tech stack: Node.js, discord.js, LLM API
```

---

## Example 723

**Intent:**
i learning spanish and want telegram bot to talk with me in spanish and correct my mistakes please

**Spec:**
```
Type:       Telegram bot (language tutor)
Data model: User(telegram_id, target_language, level)
            Message(id, user_id -> User, role, text, created_at)
            Mistake(id, user_id -> User, original, correction, explanation)
Features:   - Hold a casual conversation in Spanish at the user's level
            - Point out grammar and vocabulary mistakes after each user message
            - Explain each correction briefly in English
            - Accept voice messages and reply with voice
            - Send a daily review of the user's most common mistakes
Storage:    PostgreSQL
Tech stack: Python, python-telegram-bot, LLM API, speech-to-text API, text-to-speech API
```

---

## Example 724

**Intent:**
Our team does async standups in Slack. I want a bot that DMs everyone at 9am asking what they did yesterday, what they're doing today and blockers, then posts a combined summary in the team channel at 10.

**Spec:**
```
Type:       Slack bot (standup automation)
Data model: Team(id, channel_id, timezone, ask_time, post_time)
            Member(id, team_id -> Team, slack_user_id)
            Answer(id, member_id -> Member, date, yesterday, today, blockers)
Features:   - Send each member a DM with the three standup questions at the set time
            - Store answers per member per day
            - Summarise all answers and highlight blockers with an LLM
            - Post the summary to the team channel at the set time
            - Remind members who have not answered 15 minutes before posting
API:        Webhook
            POST /slack/events
            POST /slack/commands
Storage:    PostgreSQL
Tech stack: Node.js, Slack Bolt, node-cron, LLM API
```

---

## Example 725

**Intent:**
tool that reads contracts and pulls out key clauses like termination, payment terms, liability

**Spec:**
```
Type:       Web application (document analysis)
Auth:       User login (email + password)
Data model: Contract(id, user_id, file_name, text, uploaded_at)
            Clause(id, contract_id -> Contract, type, text, page, risk_level)
Features:   - Upload contracts as PDF or DOCX
            - Extract termination, payment, liability, renewal and confidentiality clauses
            - Flag unusual or risky clauses with a short explanation
            - Ask free-text questions about a contract
            - Compare two contracts side by side
API:        REST
            POST /contracts
            GET  /contracts/{id}/clauses
            POST /contracts/{id}/ask
Storage:    PostgreSQL, encrypted file storage
Tech stack: Python, FastAPI, pdfplumber, LLM API, React
```

---

## Example 726

**Intent:**
support chat widget for our saas app that answers from our help docs and opens a ticket if it cant

**Spec:**
```
Type:       Chatbot (customer support web widget)
Data model: Article(id, url, title, content)
            Chunk(id, article_id -> Article, text, embedding)
            Conversation(id, customer_email, started_at, resolved)
            Ticket(id, conversation_id -> Conversation, subject, status)
Features:   - Crawl the help centre and keep embeddings up to date nightly
            - Answer customer questions with links to the matching articles
            - Offer to create a ticket when confidence is low or the user asks for a human
            - Pass the chat history into the ticket
            - Show admins the questions the bot could not answer
API:        REST
            POST /chat
            POST /tickets
            GET  /admin/unanswered
Storage:    PostgreSQL with pgvector
Tech stack: TypeScript, Node.js, Express, embedding model API, LLM API, Preact widget
```

---

## Example 727

**Intent:**
I sell handmade jewellery on Etsy and writing descriptions takes forever, can AI write them from a photo and a few notes?

**Spec:**
```
Type:       Web application (AI writing assistant)
Data model: Product(id, photo_path, notes, materials, title, description, tags, created_at)
Features:   - Upload a product photo and short notes
            - Describe the item from the photo with a vision model
            - Generate a title, description and 13 SEO tags
            - Keep a consistent brand voice set in settings
            - Copy each field with one click
API:        REST
            POST /products
            GET  /products
Storage:    SQLite
Tech stack: Python, Streamlit, multimodal LLM API
```

---

## Example 728

**Intent:**
turn a youtube lecture into notes

**Spec:**
```
Type:       Web application (lecture notes)
Features:   - Paste a YouTube link to a lecture
            - Fetch the captions or transcribe the audio if there are none
            - Generate structured notes with headings and bullet points
            - Add timestamps linking each section back to the video
            - Export the notes as Markdown or PDF
API:        REST
            POST /notes
Tech stack: Python, FastAPI, yt-dlp, youtube-transcript-api, Whisper, LLM API
```

---

## Example 729

**Intent:**
auto make srt subtitles for my videos

**Spec:**
```
Type:       Command-line script (subtitles)
Features:   - Extract the audio track from a video file
            - Transcribe the audio with word-level timestamps
            - Split text into subtitle lines of at most 42 characters
            - Write an SRT file next to the video
            - Optionally translate the subtitles to another language
Input:      Video file (.mp4, .mkv, .mov) and optional target language
Tech stack: Python, ffmpeg, faster-whisper
```

---

## Example 730

**Intent:**
Discord bot that makes images from text prompts using stable diffusion on my own GPU, written with discord.py

**Spec:**
```
Type:       Discord bot (image generation)
Data model: Generation(id, guild_id, user_id, prompt, negative_prompt, seed, image_path, created_at)
Features:   - Generate an image with an /imagine slash command and a prompt
            - Queue requests so only one runs on the GPU at a time
            - Show buttons to make variations or upscale
            - Block prompts that match a banned words list
            - Limit each user to 10 images per hour
Storage:    SQLite, local disk (images)
Tech stack: Python, discord.py, Hugging Face Diffusers, PyTorch (CUDA)
```

---

## Example 731

**Intent:**
restore old scratched family photos and make them sharper

**Spec:**
```
Type:       Web application (image restoration)
Features:   - Upload old scanned photos
            - Remove scratches and dust with an inpainting model
            - Restore faces with a face restoration model
            - Upscale the photo 2x or 4x
            - Optionally colourise black-and-white photos
            - Compare before and after with a slider
API:        REST
            POST /restore
            GET  /jobs/{id}
Storage:    Local file storage, Redis (job queue)
Tech stack: Python, FastAPI, GFPGAN, Real-ESRGAN, Celery, React
```

---

## Example 732

**Intent:**
make flashcards from my lecture pdfs automatically

**Spec:**
```
Type:       Web application (study tool)
Auth:       User registration and login (email + password)
Data model: User(id, email, password_hash)
            Deck(id, user_id -> User, title, source_file)
            Card(id, deck_id -> Deck, front, back, due_at, ease)
Features:   - Upload a lecture PDF and choose the number of cards
            - Generate question-and-answer flashcards with an LLM
            - Edit or delete generated cards
            - Review cards with spaced repetition
            - Export decks to Anki format
API:        REST
            POST /decks
            GET  /decks/{id}/cards
            POST /cards/{id}/review
Storage:    PostgreSQL
Tech stack: Python, Django, pypdf, LLM API, genanki
```

---

## Example 733

**Intent:**
As a high school English teacher I spend my weekends grading essays. I want something where I upload my rubric and the class essays, and it suggests a grade and written feedback for each one that I can then adjust before sending.

**Spec:**
```
Type:       Web application (AI grading assistant)
Auth:       Teacher login (Google sign-in)
Data model: Teacher(id, email)
            Assignment(id, teacher_id -> Teacher, title, rubric)
            Essay(id, assignment_id -> Assignment, student_name, text)
            Feedback(id, essay_id -> Essay, suggested_grade, comments, final_grade, approved)
Features:   - Create an assignment with a rubric
            - Upload essays as DOCX, PDF or Google Docs links
            - Score each essay against every rubric criterion with an LLM
            - Draft written feedback quoting parts of the essay
            - Let the teacher edit grades and feedback before approving
            - Export approved grades as CSV
API:        REST
            POST /assignments
            POST /assignments/{id}/essays
            PUT  /feedback/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, LLM API, Google Docs API, React
```

---

## Example 734

**Intent:**
cli that writes my git commit messages

**Spec:**
```
Type:       Command-line tool (developer)
Features:   - Read the staged diff with git
            - Generate a Conventional Commits message with an LLM
            - Show the message and let the user accept, edit or regenerate
            - Commit with the accepted message
            - Truncate very large diffs and summarise file names instead
Input:      Staged changes in the current git repository
Tech stack: Go, Cobra, LLM API
```

---

## Example 735

**Intent:**
let non tech people ask questions about our database in english and get the sql + results

**Spec:**
```
Type:       Web application (natural language to SQL)
Auth:       User login with roles (viewer, admin)
Data model: User(id, email, password_hash, role)
            QueryLog(id, user_id -> User, question, generated_sql, row_count, created_at)
Features:   - Load the database schema and table descriptions as context
            - Turn a plain-English question into a SQL query with an LLM
            - Run only read-only SELECT queries on a replica
            - Show results as a table and a simple chart
            - Let users see and copy the generated SQL
API:        REST
            POST /ask
            GET  /history
Storage:    PostgreSQL (app data), read-only replica of the business database
Tech stack: Python, FastAPI, SQLAlchemy, LLM API, React, Recharts
```

---

## Example 736

**Intent:**
i want a daily email with summaries of new arxiv papers in my field

**Spec:**
```
Type:       Scheduled script (research digest)
Data model: Paper(arxiv_id, title, authors, abstract, summary, relevance_score, published_at)
Features:   - Fetch new papers from chosen arXiv categories every morning
            - Score each paper's relevance to the user's keywords with embeddings
            - Summarise the top 10 papers in 3 sentences each
            - Send the digest as an HTML email
            - Skip papers already sent before
Storage:    SQLite
Tech stack: Python, arxiv API client, sentence-transformers, LLM API, SMTP, cron
```

---

## Example 737

**Intent:**
a private journal app where an AI asks me how my day went and notices patterns in my mood over time

**Spec:**
```
Type:       Mobile application (AI journaling)
Auth:       Local passcode or biometric lock
Data model: Entry(id, text, mood_score, emotions, created_at)
            Insight(id, period_start, period_end, text)
Features:   - Ask a short daily check-in question with a notification
            - Let the user write or dictate a journal entry
            - Detect mood and emotions in each entry with an LLM
            - Show a mood chart for the last 30 days
            - Write a weekly reflection about patterns and triggers
Storage:    Encrypted on-device SQLite database
Tech stack: React Native, Expo, SQLCipher, LLM API
```

---

## Example 738

**Intent:**
farmers here send photo of sick plant on whatsapp and get answer what disease and what to do, in local language

**Spec:**
```
Type:       WhatsApp bot (plant disease diagnosis)
Data model: Farmer(id, phone, language, region)
            Diagnosis(id, farmer_id -> Farmer, image_path, crop, disease, confidence, advice, created_at)
Features:   - Receive crop leaf photos sent on WhatsApp
            - Classify the disease with an image classification model
            - Send treatment advice in the farmer's language
            - Ask for a clearer photo when confidence is low
            - Show agronomists a map of reported diseases by region
API:        Webhook + REST
            POST /webhook/whatsapp
            GET  /admin/diagnoses
Storage:    PostgreSQL, object storage (photos)
Tech stack: Python, FastAPI, WhatsApp Business Cloud API, PyTorch (fine-tuned plant disease model), translation API
```

---

## Example 739

**Intent:**
telegram bot where I type "spent 12 on lunch" and it logs the expense, with python-telegram-bot

**Spec:**
```
Type:       Telegram bot (expense tracking)
Data model: User(telegram_id, currency, monthly_budget)
            Expense(id, user_id -> User, amount, category, note, spent_at)
Features:   - Parse free-text messages into amount, category and date with an LLM
            - Confirm each logged expense with an undo button
            - Show spending by category with a /month command
            - Warn when spending passes the monthly budget
            - Export all expenses as CSV with /export
Storage:    SQLite
Tech stack: Python, python-telegram-bot, LLM API (structured output), pandas
```

---

## Example 740

**Intent:**
we play D&D on discord but nobody wants to be the DM lol, could a bot run the game for us

**Spec:**
```
Type:       Discord bot (AI game master)
Data model: Campaign(id, guild_id, channel_id, setting, summary)
            Character(id, campaign_id -> Campaign, user_id, name, class, hp, inventory)
            Turn(id, campaign_id -> Campaign, user_id, action, narration, created_at)
Features:   - Start a campaign with a chosen setting and create characters with /join
            - Narrate scenes and respond to each player's action with an LLM
            - Roll dice for checks and combat with /roll
            - Track HP and inventory for every character
            - Keep a running story summary so the bot remembers past sessions
Storage:    PostgreSQL
Tech stack: Node.js, discord.js, LLM API
```

---

## Example 741

**Intent:**
Slack bot that answers questions from our Confluence wiki

**Spec:**
```
Type:       Slack bot (document Q&A, RAG)
Data model: Page(id, confluence_id, title, url, updated_at)
            Chunk(id, page_id -> Page, text, embedding)
Features:   - Sync Confluence pages every night and re-embed changed pages
            - Answer questions asked with @mention or in DMs
            - Link the Confluence pages used in each answer
            - Respect space permissions so users only see pages they can access
            - Collect thumbs-up and thumbs-down feedback on answers
API:        Webhook
            POST /slack/events
Storage:    Chroma
Tech stack: Python, Slack Bolt, LlamaIndex, Confluence REST API, Chroma, LLM API
```

---

## Example 742

**Intent:**
my grandma forgets her pills, something that phones her and asks if she took them and tells me if she didnt

**Spec:**
```
Type:       Voice bot (phone reminders)
Auth:       Family member login (email + password)
Data model: Caregiver(id, email, phone)
            Patient(id, caregiver_id -> Caregiver, name, phone)
            Medication(id, patient_id -> Patient, name, dose, times)
            CallLog(id, patient_id -> Patient, called_at, confirmed, transcript)
Features:   - Call the patient at each medication time with a friendly voice
            - Understand spoken yes/no answers with speech recognition
            - Call again after 15 minutes if there is no answer
            - Send the caregiver an SMS when a dose is not confirmed
            - Show a weekly adherence calendar to the caregiver
API:        Webhook + REST
            POST /twilio/voice
            POST /twilio/gather
            GET  /patients/{id}/calls
Storage:    PostgreSQL
Tech stack: Python, Flask, Twilio Programmable Voice, APScheduler
```

---

## Example 743

**Intent:**
analyse recorded customer service calls for sentiment and whether agents followed the script

**Spec:**
```
Type:       Data pipeline (call analytics)
Data model: Call(id, agent_id, recording_path, transcript, duration_seconds, recorded_at)
            Analysis(id, call_id -> Call, sentiment, script_score, issues, summary)
Features:   - Pick up new call recordings from a storage bucket
            - Transcribe calls and separate agent and customer speech
            - Score customer sentiment through the call
            - Check whether the agent covered each required script step
            - Show agent scores and trends on a dashboard
API:        REST
            GET  /calls
            GET  /agents/{id}/scores
Storage:    PostgreSQL, S3 (recordings)
Tech stack: Python, Whisper, pyannote.audio, LLM API, Airflow, Metabase
```

---

## Example 744

**Intent:**
live captions on the projector for deaf students during class

**Spec:**
```
Type:       Desktop application (live captioning)
Features:   - Capture audio from the lecturer's microphone
            - Transcribe speech in real time with low latency
            - Show large, high-contrast captions in a full-screen window
            - Let the lecturer add course-specific words to improve accuracy
            - Save the full transcript after class
Storage:    Local text files (transcripts)
Tech stack: Python, faster-whisper (streaming), PyQt6, sounddevice
```

---

## Example 745

**Intent:**
browser extension that writes alt text for images that dont have any

**Spec:**
```
Type:       Browser extension (accessibility)
Features:   - Find images on the page with missing or empty alt attributes
            - Send each image to a vision model to generate a description
            - Insert the description as alt text for screen readers
            - Cache descriptions per image URL
            - Let the user turn it off for certain sites
API:        REST
            POST /describe
Storage:    chrome.storage.local (cache and settings)
Tech stack: JavaScript, Chrome Extension Manifest V3, Node.js proxy server, multimodal LLM API
```

---

## Example 746

**Intent:**
An Outlook add-in that drafts replies to emails for me. It should read the email thread, let me pick a short intent like "accept", "decline politely" or "ask for more info", and then write the reply in my own style.

**Spec:**
```
Type:       Office add-in (AI email writing)
Auth:       Microsoft account sign-in (Office SSO)
Data model: User(id, microsoft_id, style_examples)
            Draft(id, user_id -> User, thread_id, intent, text, created_at)
Features:   - Read the open email thread from Outlook
            - Offer quick intents like accept, decline politely and ask for more info
            - Generate a reply in the user's writing style using saved example emails
            - Insert the draft into the reply window for editing
            - Adjust length and formality with sliders
API:        REST
            POST /drafts
            PUT  /users/me/style
Storage:    PostgreSQL
Tech stack: TypeScript, Office.js, React, Node.js, LLM API
```

---

## Example 747

**Intent:**
captions for instagram posts

**Spec:**
```
Type:       Web application (AI writing assistant)
Features:   - Upload a photo or describe the post
            - Generate 5 caption options in different tones
            - Suggest relevant hashtags
            - Keep captions within Instagram's character limit
            - Save favourite captions to a list
API:        REST
            POST /captions
Storage:    Browser localStorage (saved captions)
Tech stack: Next.js, TypeScript, multimodal LLM API
```

---

## Example 748

**Intent:**
tool that adds docstrings to all functions in my python project

**Spec:**
```
Type:       Command-line tool (developer)
Features:   - Parse Python files with the ast module to find functions and classes without docstrings
            - Generate Google-style docstrings with an LLM using the function code
            - Insert docstrings without changing the rest of the code
            - Show a diff and ask for confirmation before writing
            - Skip private functions with a --public-only flag
Input:      Path to a Python project folder
Tech stack: Python, ast, LibCST, LLM API, Typer
```

---

## Example 749

**Intent:**
when our monitoring fires an alert in slack, i want a bot to explain whats probably wrong using the recent logs

**Spec:**
```
Type:       Slack bot (incident assistant)
Data model: Alert(id, source, service, message, fired_at)
            Explanation(id, alert_id -> Alert, likely_cause, suggested_steps, created_at)
Features:   - Listen for alert messages in the alerts channel
            - Fetch logs from the affected service for the last 15 minutes
            - Summarise errors and suggest a likely cause with an LLM
            - Reply in the alert thread with suggested next steps
            - Link similar past alerts and how they were fixed
API:        Webhook
            POST /slack/events
            POST /alerts
Storage:    PostgreSQL
Tech stack: Python, Slack Bolt, Elasticsearch client, LLM API
```

---

## Example 750

**Intent:**
dashboard showing if our app store reviews are positive or negative and what people complain about

**Spec:**
```
Type:       Analytics dashboard (review analysis)
Data model: Review(id, store, rating, text, version, posted_at, sentiment, topics)
Features:   - Pull new App Store and Google Play reviews every day
            - Classify sentiment of each review
            - Group complaints into topics like crashes, pricing and login
            - Show sentiment over time and per app version
            - Alert the team when negative reviews spike
API:        REST
            GET  /reviews
            GET  /topics
Storage:    PostgreSQL
Tech stack: Python, Hugging Face Transformers (sentiment model), BERTopic, Streamlit
```

---

## Example 751

**Intent:**
spam filter for my phpbb forum

**Spec:**
```
Type:       Forum plugin + API service (spam detection)
Data model: Post(id, forum_post_id, author_id, text, links, spam_score, status, created_at)
Features:   - Check every new post and registration before it is published
            - Score spam probability with a trained text classifier
            - Hold suspicious posts in a moderation queue
            - Learn from moderator approve and reject decisions
            - Block new accounts that post many links in their first posts
API:        REST
            POST /check
            POST /feedback
Storage:    MySQL
Tech stack: PHP (phpBB extension), Python, FastAPI, scikit-learn
```

---

## Example 752

**Intent:**
i run an image hosting site and need to automatically block nsfw uploads

**Spec:**
```
Type:       Background service (image moderation)
Data model: Upload(id, user_id, file_path, nsfw_score, status, uploaded_at)
Features:   - Scan each uploaded image before it becomes public
            - Score NSFW content with an image classifier
            - Publish safe images and quarantine flagged ones
            - Show flagged images blurred in a review queue
            - Ban users with repeated violations
API:        REST
            POST /scan
            GET  /review-queue
            POST /review-queue/{id}/decision
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, FastAPI, PyTorch (NSFW image classifier), Celery, Redis
```

---

## Example 753

**Intent:**
our discord server has people from brazil, japan and germany, can a bot translate messages automatically between them? discord.js if possible

**Spec:**
```
Type:       Discord bot (translation)
Data model: ChannelLink(id, guild_id, source_channel_id, target_channel_id, target_lang)
            UserPref(user_id, guild_id, language)
Features:   - Detect the language of each message
            - Mirror messages into linked channels in other languages
            - Translate a single message on demand with a context menu command
            - Keep emojis, mentions and code blocks unchanged
            - Let users set their own language with /language
Storage:    SQLite
Tech stack: Node.js, discord.js, translation API
```

---

## Example 754

**Intent:**
chat with a bot to find my next book to read

**Spec:**
```
Type:       Chatbot (recommendation, web)
Data model: Book(id, title, author, genres, description, embedding)
            ReadingList(id, session_id, book_id -> Book, status)
Features:   - Ask about favourite books, genres and reading mood
            - Recommend books using semantic search over book descriptions
            - Explain why each book fits the user
            - Add books to a want-to-read list
            - Show where to buy or borrow each book
API:        REST
            POST /chat
            GET  /reading-list
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, Open Library API, embedding model API, LLM API, Svelte
```

---

## Example 755

**Intent:**
I want to say "plan me 4 days in Lisbon in May under 800 euro" and have an agent figure out the flights, weather, places and make a day-by-day plan

**Spec:**
```
Type:       AI agent (travel planning web app)
Auth:       User login (Google sign-in)
Data model: User(id, email)
            Trip(id, user_id -> User, destination, start_date, end_date, budget)
            ItineraryItem(id, trip_id -> Trip, day, time, place, cost, notes)
Features:   - Parse destination, dates and budget from the request
            - Call tools for flight search, weather forecast and points of interest
            - Build a day-by-day itinerary within the budget
            - Let the user swap out single activities and replan
            - Export the itinerary to Google Calendar
API:        REST
            POST /trips
            GET  /trips/{id}
            POST /trips/{id}/replan
Storage:    PostgreSQL
Tech stack: Python, LangGraph, flight search API, weather API, Google Places API, LLM API, React
```

---

## Example 756

**Intent:**
practice job interviews by talking out loud to an AI interviewer that gives feedback after

**Spec:**
```
Type:       Web application (voice interview practice)
Auth:       User registration and login (email + password)
Data model: User(id, email, password_hash)
            Interview(id, user_id -> User, role, level, started_at)
            Answer(id, interview_id -> Interview, question, transcript, score, feedback)
Features:   - Pick a job role and seniority level
            - Ask interview questions out loud with text-to-speech
            - Record and transcribe the user's spoken answers
            - Ask follow-up questions based on the answers
            - Give feedback on content, structure and filler words after the interview
API:        REST + WebSocket
            POST /interviews
            WS   /interviews/{id}/audio
            GET  /interviews/{id}/report
Storage:    PostgreSQL
Tech stack: Python, FastAPI, speech-to-text API, text-to-speech API, LLM API, React
```

---

## Example 757

**Intent:**
python tutor for total beginners that gives exercises and checks my code

**Spec:**
```
Type:       Web application (AI coding tutor)
Auth:       User registration and login (email + password)
Data model: User(id, email, password_hash, level)
            Exercise(id, topic, prompt, tests)
            Submission(id, user_id -> User, exercise_id -> Exercise, code, passed, feedback, created_at)
Features:   - Teach topics in order from variables to classes
            - Give exercises with an in-browser code editor
            - Run submissions against hidden tests in a sandbox
            - Explain failing tests with hints from an LLM instead of the solution
            - Track progress and unlock the next topic
API:        REST
            GET  /exercises/{id}
            POST /exercises/{id}/submissions
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Docker (code sandbox), LLM API, React, Monaco Editor
```

---

## Example 758

**Intent:**
telegram bot that sends me a summary of my rss feeds every morning

**Spec:**
```
Type:       Telegram bot (news digest)
Data model: User(telegram_id, digest_time, timezone)
            Feed(id, user_id -> User, url, title)
            Article(id, feed_id -> Feed, url, title, published_at, sent)
Features:   - Add and remove RSS feeds with /add and /remove
            - Fetch new articles from all feeds every hour
            - Summarise each article in 2 sentences with an LLM
            - Group articles by topic in a single morning message
            - Send the digest at the user's chosen time
Storage:    SQLite
Tech stack: Python, python-telegram-bot, feedparser, trafilatura, LLM API
```

---

## Example 759

**Intent:**
extract data from supplier invoices pdf to excel

**Spec:**
```
Type:       Command-line script (document extraction)
Features:   - Read PDF and scanned image invoices from a folder
            - Run OCR on scanned pages
            - Extract supplier, invoice number, date, line items, VAT and total with an LLM
            - Check that line items add up to the total
            - Write all invoices to an Excel file, one row per line item
Input:      Folder of invoice files (.pdf, .jpg, .png)
Tech stack: Python, pdfplumber, Tesseract OCR (pytesseract), LLM API (structured output), openpyxl
```

---

## Example 760

**Intent:**
Patients often don't understand their lab results or discharge letters. I'd like a tool where they upload the document and get a plain-language explanation, with a clear warning that it's not medical advice.

**Spec:**
```
Type:       Web application (medical document explainer)
Features:   - Upload a lab report or discharge letter as PDF or photo
            - Extract text with OCR
            - Explain each term and value in plain language with an LLM
            - Mark values outside the reference range
            - Show a not-medical-advice warning and suggest questions to ask the doctor
            - Delete uploaded files right after processing
API:        REST
            POST /explain
Tech stack: Python, FastAPI, Tesseract OCR, LLM API, React
```

---

## Example 761

**Intent:**
bot in microsoft teams for IT helpdesk, like reset password, check ticket status, answer common questions

**Spec:**
```
Type:       Microsoft Teams bot (IT helpdesk)
Auth:       Microsoft Entra ID (Teams single sign-on)
Data model: Ticket(id, requester_upn, category, description, status, created_at)
            KbArticle(id, title, content, embedding)
Features:   - Answer common IT questions from the knowledge base
            - Trigger self-service password resets through Microsoft Graph
            - Create tickets from a conversation and return the ticket number
            - Show the status of the user's open tickets
            - Hand over to a human agent during office hours
API:        Webhook
            POST /api/messages
Storage:    Azure SQL Database, Azure AI Search (vectors)
Tech stack: C#, .NET, Bot Framework SDK, Microsoft Graph API, LLM API
```

---

## Example 762

**Intent:**
Discord bot for my server that greets new people and answers FAQ about the rules and roles, using our docs

**Spec:**
```
Type:       Discord bot (community FAQ, RAG)
Data model: Guild(id, welcome_channel_id, welcome_message)
            FaqChunk(id, guild_id -> Guild, source, text, embedding)
Features:   - Greet new members in the welcome channel with a personalised message
            - Answer questions about rules and roles using uploaded server docs
            - Let admins upload or replace docs with /docs upload
            - Ping a moderator when the bot is unsure
            - Assign roles from a reaction menu
Storage:    Chroma, SQLite
Tech stack: Python, discord.py, sentence-transformers, Chroma, LLM API
```

---

## Example 763

**Intent:**
slack bot so i can turn any message into a jira ticket with the right fields filled in

**Spec:**
```
Type:       Slack bot (ticket creation)
Auth:       Jira OAuth 2.0 connection per workspace
Data model: Workspace(id, slack_team_id, jira_site, jira_token)
            CreatedIssue(id, workspace_id -> Workspace, slack_message_ts, issue_key, created_at)
Features:   - Add a "Create Jira ticket" message shortcut
            - Draft a title, description, issue type and priority from the message with an LLM
            - Show the draft in a modal for editing
            - Create the issue in the chosen Jira project
            - Reply in the thread with the issue link
API:        Webhook
            POST /slack/interactions
            GET  /oauth/jira/callback
Storage:    PostgreSQL
Tech stack: Node.js, Slack Bolt, Jira Cloud REST API, LLM API
```

---

## Example 764

**Intent:**
quiz generator for teachers

**Spec:**
```
Type:       Web application (quiz generation)
Auth:       Teacher login (email + password)
Data model: Teacher(id, email, password_hash)
            Quiz(id, teacher_id -> Teacher, title, source_text, created_at)
            QuizQuestion(id, quiz_id -> Quiz, type, text, options, answer)
Features:   - Paste text or upload a chapter to base the quiz on
            - Generate multiple-choice, true/false and short-answer questions
            - Choose the difficulty and number of questions
            - Edit questions before saving
            - Export the quiz as PDF or Google Forms
API:        REST
            POST /quizzes
            GET  /quizzes/{id}
            PUT  /quizzes/{id}/questions/{qid}
Storage:    PostgreSQL
Tech stack: Python, Flask, LLM API, Google Forms API, WeasyPrint
```

---

## Example 765

**Intent:**
i record voice memos all day, want them turned into a todo list automatically

**Spec:**
```
Type:       Mobile application (voice notes to tasks)
Data model: Memo(id, audio_path, transcript, recorded_at)
            Task(id, memo_id -> Memo, title, due_date, done)
Features:   - Record voice memos with one tap
            - Transcribe memos in the background
            - Extract tasks and due dates from each memo with an LLM
            - Show tasks in a checklist grouped by due date
            - Send reminders for tasks with a due time
Storage:    Local on-device SQLite database
Tech stack: Flutter, speech-to-text API, LLM API
```

---

## Example 766

**Intent:**
bedtime stories for my kids with their names in them, pictures and read aloud

**Spec:**
```
Type:       Mobile application (story generation)
Data model: Child(id, name, age, favourite_things)
            Story(id, child_id -> Child, title, text, image_paths, audio_path, created_at)
Features:   - Create a child profile with name, age and favourite things
            - Generate a short, age-appropriate story with an LLM
            - Illustrate each page with a text-to-image model
            - Read the story aloud with text-to-speech
            - Save stories to a bedtime library
            - Filter out scary or unsuitable content
Storage:    On-device storage, cloud storage for images and audio
Tech stack: Swift, SwiftUI, LLM API, image generation API, text-to-speech API
```

---

## Example 767

**Intent:**
logo generator for small business

**Spec:**
```
Type:       Web application (image generation)
Data model: Project(id, business_name, industry, style, colours)
            Logo(id, project_id -> Project, prompt, image_path, is_favourite)
Features:   - Enter business name, industry, style and colours
            - Generate 8 logo ideas with a text-to-image model
            - Regenerate variations of a chosen logo
            - Convert the chosen logo to SVG
            - Download a pack with PNG, SVG and favicon sizes
API:        REST
            POST /projects
            POST /projects/{id}/logos
            GET  /logos/{id}/download
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, FastAPI, Stable Diffusion XL, vtracer (vectorising), Next.js
```

---

## Example 768

**Intent:**
need to blur all faces and licence plates in dashcam videos before i post them, python + opencv

**Spec:**
```
Type:       Command-line script (video anonymisation)
Features:   - Read video files frame by frame
            - Detect faces and licence plates with detection models
            - Blur each detected region with a Gaussian blur
            - Track detections between frames to avoid flickering
            - Write the anonymised video with the original audio
Input:      Video file or folder of videos (.mp4, .mov) and blur strength
Tech stack: Python, OpenCV, YOLOv8 (ultralytics), ffmpeg
```

---

## Example 769

**Intent:**
take photos of my handwritten notebook pages and turn them into typed notes i can search

**Spec:**
```
Type:       Mobile application (handwriting OCR)
Data model: Notebook(id, title)
            Page(id, notebook_id -> Notebook, image_path, text, created_at)
Features:   - Scan notebook pages with the camera and auto-crop them
            - Convert handwriting to text with a handwriting recognition model
            - Clean up the text and add headings with an LLM
            - Search across all scanned pages
            - Export a notebook as Markdown or PDF
Storage:    Local SQLite database with full-text search
Tech stack: Kotlin, Jetpack Compose, CameraX, handwriting OCR API, LLM API
```

---

## Example 770

**Intent:**
chatbot for our university website that answers questions about admissions deadlines, fees and courses

**Spec:**
```
Type:       Chatbot (web widget, RAG)
Data model: Source(id, url, title, last_crawled_at)
            Chunk(id, source_id -> Source, text, embedding)
            ChatLog(id, question, answer, helpful, created_at)
Features:   - Crawl the admissions, fees and course pages every week
            - Answer prospective students' questions from that content with sources
            - Answer in English, Spanish and French
            - Collect the student's email for follow-up when the answer is unclear
            - Show staff the most asked questions each month
API:        REST
            POST /chat
            GET  /admin/top-questions
Storage:    PostgreSQL with pgvector
Tech stack: Python, Django, Scrapy, embedding model API, LLM API, JavaScript widget
```

---

## Example 771

**Intent:**
chat with my obsidian vault using llamaindex, all running locally

**Spec:**
```
Type:       Desktop application (personal knowledge Q&A)
Features:   - Index all Markdown files in an Obsidian vault
            - Re-index notes that changed since the last run
            - Answer questions with links back to the source notes
            - Follow [[wikilinks]] to pull in related notes
            - Run fully offline with a local LLM and local embeddings
Input:      Path to an Obsidian vault folder
Storage:    Local Chroma database
Tech stack: Python, LlamaIndex, Chroma, Ollama (local LLM), Gradio
```

---

## Example 772

**Intent:**
search our codebase by describing what the code does

**Spec:**
```
Type:       Developer tool (semantic code search)
Data model: Repo(id, name, url, last_indexed_commit)
            CodeChunk(id, repo_id -> Repo, file_path, start_line, end_line, symbol, embedding)
Features:   - Clone and index repositories on every push to main
            - Split code into functions and classes with tree-sitter
            - Embed each chunk with a code embedding model
            - Return the best matching code snippets for a plain-English query
            - Open results at the exact line in GitHub
API:        REST + Webhook
            GET  /search?q={query}
            POST /webhooks/github
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, tree-sitter, code embedding model, React
```

---

## Example 773

**Intent:**
we get tons of github issues, i want a bot that labels them, finds duplicates and asks for missing info

**Spec:**
```
Type:       GitHub App (issue triage)
Auth:       GitHub App installation with a private key and webhook secret
Data model: Issue(id, repo, number, title, body, labels, embedding)
Features:   - Receive issues opened events
            - Suggest labels like bug, feature and question with an LLM
            - Find likely duplicate issues with embedding similarity and comment links
            - Ask for steps to reproduce and version when they are missing
            - Close obvious duplicates after maintainer approval
API:        Webhook
            POST /api/github/webhooks
Storage:    PostgreSQL with pgvector
Tech stack: Node.js, TypeScript, Probot, embedding model API, LLM API
```

---

## Example 774

**Intent:**
telegram bot that makes memes from what you write

**Spec:**
```
Type:       Telegram bot (meme generator)
Data model: Template(id, name, image_path, text_boxes)
            Meme(id, user_id, template_id -> Template, top_text, bottom_text, created_at)
Features:   - Take a topic or joke idea from the user
            - Pick a fitting meme template and write captions with an LLM
            - Draw the captions on the image in Impact font
            - Send back the meme with a button to try another template
            - Work in group chats with the /meme command
Storage:    SQLite, local folder of templates
Tech stack: Python, aiogram, Pillow, LLM API
```

---

## Example 775

**Intent:**
describe how i feel and get a spotify playlist made for it

**Spec:**
```
Type:       Web application (playlist generator)
Auth:       Spotify OAuth 2.0 login
Data model: User(id, spotify_id, refresh_token)
            Playlist(id, user_id -> User, mood_text, spotify_playlist_id, created_at)
Features:   - Let the user describe a mood, activity or moment in free text
            - Turn the description into genres, energy and tempo with an LLM
            - Pick tracks using the user's top artists and Spotify search
            - Create the playlist in the user's Spotify account
            - Name the playlist and generate a cover image
API:        REST
            GET  /auth/spotify/callback
            POST /playlists
Storage:    PostgreSQL
Tech stack: Next.js, TypeScript, Spotify Web API, LLM API
```

---

## Example 776

**Intent:**
fitness coach chatbot that makes me a workout plan and changes it when i tell it how it went

**Spec:**
```
Type:       Mobile application (AI fitness coach)
Auth:       User registration and login (email + password)
Data model: User(id, email, goal, experience, equipment)
            Plan(id, user_id -> User, week, workouts_json)
            WorkoutLog(id, user_id -> User, date, exercises, difficulty, notes)
Features:   - Ask about goals, experience, schedule and available equipment
            - Generate a weekly workout plan with an LLM
            - Log completed workouts and how hard they felt
            - Adjust next week's plan based on logs and feedback
            - Answer exercise questions in chat
API:        REST
            POST /plans
            POST /logs
            POST /chat
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express, LLM API
```

---

## Example 777

**Intent:**
many people in our village not know which government scheme they can apply, we want whatsapp bot in hindi that ask few questions and tell them eligible schemes

**Spec:**
```
Type:       WhatsApp bot (eligibility assistant)
Data model: Scheme(id, name_hi, description_hi, rules_json, documents_needed)
            Citizen(id, phone, age, income, occupation, state)
            Match(id, citizen_id -> Citizen, scheme_id -> Scheme, created_at)
Features:   - Talk with users in Hindi by text or voice note
            - Ask simple questions about age, income, occupation and state
            - Match answers against each scheme's eligibility rules
            - Explain eligible schemes and the documents needed
            - Share the nearest help centre on request
API:        Webhook
            POST /webhook/whatsapp
Storage:    PostgreSQL
Tech stack: Python, FastAPI, WhatsApp Business Cloud API, speech-to-text API (Hindi), LLM API
```

---

## Example 778

**Intent:**
convert epub books into audiobooks

**Spec:**
```
Type:       Command-line script (text-to-speech)
Features:   - Read chapters and text from an EPUB file
            - Clean the text and split it into sentences
            - Generate speech for each chapter with a neural TTS model
            - Join the audio into one MP3 per chapter
            - Add chapter markers and cover art to an M4B file
Input:      EPUB file, voice name and speaking speed
Tech stack: Python, ebooklib, BeautifulSoup, Coqui TTS, ffmpeg
```

---

## Example 779

**Intent:**
An app that helps people practise English pronunciation. You read a sentence aloud, it shows which words or sounds you said wrong and plays the correct version. I'd like to build it with React and FastAPI.

**Spec:**
```
Type:       Web application (pronunciation coach)
Auth:       User registration and login (email + password)
Data model: User(id, email, password_hash, native_language)
            Sentence(id, text, level, reference_audio_path)
            Attempt(id, user_id -> User, sentence_id -> Sentence, audio_path, score, word_scores, created_at)
Features:   - Show a sentence and record the user reading it
            - Align the recording to expected phonemes and score each word
            - Highlight mispronounced words and sounds in red
            - Play the correct pronunciation with text-to-speech
            - Track scores over time and suggest sounds to practise
API:        REST
            GET  /sentences
            POST /attempts
            GET  /users/me/progress
Storage:    PostgreSQL, S3 (recordings)
Tech stack: Python, FastAPI, wav2vec2 phoneme model (Hugging Face Transformers), text-to-speech API, React
```

---

## Example 780

**Intent:**
check if student essays was written by ai

**Spec:**
```
Type:       Web application (AI text detection)
Auth:       Teacher login (email + password)
Data model: Submission(id, teacher_id, student_name, text, ai_probability, created_at)
Features:   - Paste or upload essays as DOCX or PDF
            - Estimate the probability that text is AI-generated
            - Highlight the sentences that look most AI-written
            - Compare with the student's earlier essays for style changes
            - Show a clear note that results are not proof
API:        REST
            POST /submissions
            GET  /submissions/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, Hugging Face Transformers (detector model), React
```

---

## Example 781

**Intent:**
something that warns me if an email in my gmail is phishing

**Spec:**
```
Type:       Browser extension (email security)
Features:   - Read the open email's sender, links and text in Gmail
            - Check sender domain and link targets against known phishing lists
            - Classify the email text for phishing signs with an LLM
            - Show a warning banner with the reasons
            - Let the user report false alarms
API:        REST
            POST /analyze
Storage:    chrome.storage.local (settings)
Tech stack: JavaScript, Chrome Extension Manifest V3, Python, FastAPI, LLM API
```

---

## Example 782

**Intent:**
discord bot for our coding server where ppl can ask programming questions and it answers with code, but dont let it get spammed

**Spec:**
```
Type:       Discord bot (programming help)
Data model: Guild(id, help_channel_id, daily_limit)
            Usage(id, guild_id -> Guild, user_id, date, count)
Features:   - Answer questions in the help channel or with /ask
            - Read attached code files and code blocks as context
            - Format answers with syntax-highlighted code blocks
            - Create a thread for each question to keep the channel clean
            - Limit each user to a set number of questions per day
Storage:    Redis (rate limits), SQLite
Tech stack: Node.js, discord.js, LLM API
```

---

## Example 783

**Intent:**
slack bot for onboarding new hires, it should answer their questions and walk them thru a checklist the first 2 weeks, using slack bolt for python

**Spec:**
```
Type:       Slack bot (employee onboarding)
Data model: NewHire(id, slack_user_id, start_date, manager_id, team)
            ChecklistItem(id, day, title, description)
            Progress(id, new_hire_id -> NewHire, item_id -> ChecklistItem, done_at)
Features:   - Send a welcome message on the first day
            - Post each day's checklist items with done buttons
            - Answer questions from the employee handbook with RAG
            - Notify the manager when items are overdue
            - Send a feedback survey at the end of week 2
API:        Webhook
            POST /slack/events
            POST /slack/interactions
Storage:    PostgreSQL with pgvector
Tech stack: Python, Slack Bolt, LLM API, embedding model API
```

---

## Example 784

**Intent:**
phone line for our city buses where you call and ask when the next bus comes

**Spec:**
```
Type:       Voice bot (phone hotline)
Data model: Stop(id, name, aliases, lat, lon)
            CallLog(id, caller_hash, question, stop_id -> Stop, answered, created_at)
Features:   - Answer incoming calls with a greeting
            - Understand spoken stop names and route numbers
            - Look up the next departures from real-time GTFS data
            - Read out the next 3 arrival times
            - Transfer to an operator when the stop is not recognised
API:        Webhook
            POST /twilio/voice
            POST /twilio/gather
Storage:    PostgreSQL (GTFS static data), Redis (real-time feed cache)
Tech stack: Python, FastAPI, Twilio Programmable Voice, gtfs-realtime-bindings, LLM API
```

---

## Example 785

**Intent:**
agent that checks our competitors websites every week and tells us what changed in pricing or features

**Spec:**
```
Type:       AI agent (scheduled web monitoring)
Data model: Competitor(id, name)
            WatchedPage(id, competitor_id -> Competitor, url, last_snapshot, last_checked_at)
            Change(id, page_id -> WatchedPage, summary, category, detected_at)
Features:   - Fetch each watched page with a headless browser every week
            - Compare the new text with the last snapshot
            - Summarise meaningful changes in pricing, features and messaging with an LLM
            - Ignore cosmetic changes like dates and cookie banners
            - Email a weekly report grouped by competitor
Storage:    PostgreSQL
Tech stack: Python, Playwright, difflib, LLM API, cron
```

---

## Example 786

**Intent:**
google sheets addon where u describe what u want and it writes teh formula

**Spec:**
```
Type:       Google Workspace add-on (spreadsheet assistant)
Features:   - Open a sidebar inside Google Sheets
            - Read the sheet headers and selected range as context
            - Turn a plain-English request into a formula
            - Explain the formula in simple words
            - Insert the formula into the selected cell
API:        REST
            POST /formula
Tech stack: Google Apps Script, HTML sidebar, LLM API
```

---

## Example 787

**Intent:**
chrome extension to fix my english when i write emails, i am not native speaker and make many grammar mistake

**Spec:**
```
Type:       Browser extension (grammar assistant)
Features:   - Check text in any text field after the user stops typing
            - Underline grammar and spelling mistakes
            - Suggest corrections with short explanations
            - Rewrite a selected sentence to sound more natural
            - Let the user add words to a personal dictionary
API:        REST
            POST /check
            POST /rewrite
Storage:    chrome.storage.sync (dictionary and settings)
Tech stack: TypeScript, Chrome Extension Manifest V3, LanguageTool server, LLM API
```

---

## Example 788

**Intent:**
A command-line coding agent in Python that I point at a repo and give a task like "fix the failing tests". It should read files, run the tests, edit code and repeat until the tests pass, asking me before risky actions.

**Spec:**
```
Type:       AI agent (command-line coding assistant)
Features:   - Explore the repository with read-file, list-files and search tools
            - Run the test command and read the output
            - Edit files with a diff-based patch tool
            - Repeat the edit-and-test loop up to a set number of steps
            - Ask the user before running shell commands or deleting files
            - Show a final summary of all changes
Input:      Path to a git repository, a task description and a test command
Tech stack: Python, LLM API (tool calling), GitPython, Rich
```

---

## Example 789

**Intent:**
upload a csv and ask questions about it in english, it should write and run pandas code to answer

**Spec:**
```
Type:       AI agent (data analysis web app)
Data model: Dataset(id, file_name, columns, row_count, uploaded_at)
            Question(id, dataset_id -> Dataset, text, code, answer, chart_path)
Features:   - Upload a CSV and show a preview of its columns
            - Write pandas code for each question with an LLM
            - Run the code in a sandbox with time and memory limits
            - Fix and retry the code automatically when it errors
            - Show the answer with a table or chart and the code used
API:        REST
            POST /datasets
            POST /datasets/{id}/questions
Storage:    SQLite, local file storage
Tech stack: Python, Streamlit, pandas, matplotlib, LLM API, Docker (sandbox)
```

---

## Example 790

**Intent:**
what plant is this bot

**Spec:**
```
Type:       Telegram bot (plant identification)
Data model: Identification(id, user_id, image_path, species, confidence, created_at)
Features:   - Receive a plant photo from the user
            - Identify the species with an image classification model
            - Reply with the common and Latin names and confidence
            - Add care tips for watering, light and toxicity to pets
            - Show the top 3 guesses when confidence is low
Storage:    SQLite
Tech stack: Python, python-telegram-bot, PyTorch (fine-tuned plant species model)
```

---

## Example 791

**Intent:**
translate whole pdf documents but keep teh same layout and pictures

**Spec:**
```
Type:       Web application (document translation)
Data model: Job(id, file_name, source_lang, target_lang, status, output_path, created_at)
Features:   - Upload PDF or DOCX files up to 50 pages
            - Extract text blocks with their position and font size
            - Translate the blocks with a translation model, keeping context between pages
            - Rebuild the document with translated text in the same layout
            - Shrink the font when translated text does not fit its box
API:        REST
            POST /jobs
            GET  /jobs/{id}
            GET  /jobs/{id}/download
Storage:    Local file storage, Redis (job queue)
Tech stack: Python, FastAPI, PyMuPDF, python-docx, Hugging Face Transformers (NLLB), RQ
```

---

## Example 792

**Intent:**
looking for apartment is pain, i want chat where i say my budget and what i need and it show matching flats from listings

**Spec:**
```
Type:       Chatbot (recommendation, web)
Data model: Listing(id, source_url, title, price, rooms, area_m2, district, features, embedding, scraped_at)
            SavedSearch(id, user_email, criteria_json, created_at)
Features:   - Collect budget, rooms, district and must-haves through chat
            - Turn the conversation into structured filters with an LLM
            - Rank matching listings by filters and description similarity
            - Show listings as cards with photos and a map
            - Email new matching listings daily for saved searches
API:        REST
            POST /chat
            POST /saved-searches
Storage:    PostgreSQL with pgvector and PostGIS
Tech stack: Python, FastAPI, Scrapy (listing scraper), LLM API, React, Leaflet
```

---

## Example 793

**Intent:**
twitch chat bot that answers viewer questions about my stream and times out spammers, tmi.js

**Spec:**
```
Type:       Twitch chat bot
Auth:       Twitch OAuth token for the bot account
Data model: Fact(id, key, value)
            Strike(id, username, reason, created_at)
Features:   - Answer viewer questions about schedule, setup and rules from a facts list
            - Answer other questions in short, stream-friendly replies with an LLM
            - Detect spam, link floods and caps spam
            - Time out spammers with escalating durations
            - Let mods add facts with !addfact
Storage:    SQLite
Tech stack: Node.js, tmi.js, LLM API
```

---

## Example 794

**Intent:**
text adventure game where AI is the narrator and the world changes with what you type

**Spec:**
```
Type:       Web game (AI text adventure)
Auth:       Optional login to save games (email + password)
Data model: Player(id, email, password_hash)
            Save(id, player_id -> Player, world_state_json, story_summary, updated_at)
Features:   - Start a new story in a chosen genre
            - Narrate the result of each typed action with an LLM
            - Keep world state such as location, inventory and characters consistent
            - Summarise older turns to keep the context small
            - Save and load games
API:        REST + Server-Sent Events
            POST /games
            POST /games/{id}/actions
            GET  /games/{id}/stream
Storage:    PostgreSQL
Tech stack: TypeScript, Node.js, Express, LLM API, React
```

---

## Example 795

**Intent:**
our hotel gets lots of emails asking about availability, prices, parking etc, we want AI to draft replies and check bookings in our system

**Spec:**
```
Type:       AI agent (email auto-responder)
Data model: Email(id, from_address, subject, body, received_at)
            Draft(id, email_id -> Email, text, tools_used, status, approved_by)
Features:   - Read new guest emails from the reservations inbox
            - Check room availability and prices with a booking system tool
            - Answer questions about parking, breakfast and check-in from the hotel FAQ
            - Draft a reply for staff to approve, edit or reject
            - Send approved replies from the shared inbox
API:        REST
            GET  /drafts
            POST /drafts/{id}/approve
Storage:    PostgreSQL
Tech stack: Python, FastAPI, IMAP/SMTP, booking system API, LLM API (tool calling), Vue.js
```

---

## Example 796

**Intent:**
For our GP practice: record the doctor-patient consultation with consent, transcribe it and draft a SOAP note the doctor reviews before saving to the patient record. Data must stay in the EU.

**Spec:**
```
Type:       Web application (clinical documentation)
Auth:       Clinician login with two-factor authentication
Data model: Clinician(id, email, password_hash, totp_secret)
            Consultation(id, clinician_id -> Clinician, patient_ref, consent_given, audio_path, transcript, created_at)
            SoapNote(id, consultation_id -> Consultation, subjective, objective, assessment, plan, approved_at)
Features:   - Record consultations only after consent is ticked
            - Transcribe the audio with medical vocabulary support
            - Draft a SOAP note from the transcript with an LLM
            - Let the doctor edit and approve the note
            - Export the approved note to the practice EHR
            - Delete audio automatically after 30 days
API:        REST
            POST /consultations
            POST /consultations/{id}/audio
            PUT  /notes/{id}
Storage:    PostgreSQL and encrypted object storage, hosted in an EU region
Tech stack: Python, Django, self-hosted Whisper, LLM API (EU-hosted), HL7 FHIR API, React
```

---

## Example 797

**Intent:**
app for travelling that listen what i say and speak it in other language for the local person

**Spec:**
```
Type:       Mobile application (speech translation)
Features:   - Record speech with a push-to-talk button
            - Transcribe the speech in the speaker's language
            - Translate the text into the other person's language
            - Speak the translation out loud
            - Switch direction with a split-screen conversation mode
            - Download language packs for offline use
Storage:    On-device storage (language packs and history)
Tech stack: Flutter, whisper.cpp, on-device translation models, platform text-to-speech
```

---

## Example 798

**Intent:**
erase unwanted people or objects from photos by painting over them

**Spec:**
```
Type:       Web application (image editing)
Features:   - Upload a photo up to 4096 x 4096 pixels
            - Paint a mask over the object with a brush tool
            - Fill the masked area with an inpainting model
            - Undo and redo edits
            - Download the edited photo in full resolution
API:        REST
            POST /inpaint
Tech stack: Python, FastAPI, LaMa inpainting model, PyTorch, React, HTML Canvas
```

---

## Example 799

**Intent:**
generate release notes from git commits and merged prs

**Spec:**
```
Type:       Command-line tool (developer)
Features:   - Collect commits and merged pull requests between two git tags
            - Group changes into features, fixes and breaking changes
            - Rewrite technical titles into user-friendly notes with an LLM
            - Credit contributors by GitHub username
            - Write the notes to CHANGELOG.md or a GitHub release
Input:      Repository path, start tag and end tag
Tech stack: Node.js, simple-git, Octokit, LLM API
```

---

## Example 800

**Intent:**
slack bot where you ask "who knows about kubernetes" and it tells you the right person based on what people talk about

**Spec:**
```
Type:       Slack bot (expert finder)
Data model: Member(id, slack_user_id, name, title)
            Topic(id, name, embedding)
            Expertise(id, member_id -> Member, topic_id -> Topic, score, last_seen_at)
Features:   - Read messages from public channels the bot is added to
            - Extract technical topics from each message with an LLM
            - Build an expertise score per person and topic, weighted by recency
            - Answer "who knows about X" with the top 3 people and example threads
            - Let people opt out with a /expertfinder optout command
API:        Webhook
            POST /slack/events
            POST /slack/commands
Storage:    PostgreSQL with pgvector
Tech stack: Python, Slack Bolt, embedding model API, LLM API
```

---

## Example 801

**Intent:**
I'm a YouTuber with thousands of comments and can't keep up. I'd like a tool that sorts comments into questions, praise and hate, and drafts replies to the questions in my voice so I can approve them in bulk.

**Spec:**
```
Type:       Web application (comment management)
Auth:       Google OAuth 2.0 (YouTube channel access)
Data model: Channel(id, youtube_channel_id, refresh_token, voice_examples)
            Comment(id, channel_id -> Channel, video_id, author, text, category, published_at)
            ReplyDraft(id, comment_id -> Comment, text, status)
Features:   - Import new comments from all videos every hour
            - Classify comments as question, praise, feedback or hate
            - Hide hateful comments for review with one click
            - Draft replies to questions in the creator's voice with an LLM
            - Approve, edit and post replies in bulk
API:        REST
            GET  /comments?category={name}
            POST /replies/approve
Storage:    PostgreSQL
Tech stack: Python, FastAPI, YouTube Data API v3, LLM API, React
```

---

## Example 802

**Intent:**
bot that records our discord voice calls and posts notes after, using pycord

**Spec:**
```
Type:       Discord bot (voice call notes)
Data model: Recording(id, guild_id, channel_id, started_at, ended_at, audio_path)
            Notes(id, recording_id -> Recording, transcript, summary, action_items)
Features:   - Join a voice channel with /record and announce that recording has started
            - Record each speaker's audio track separately
            - Transcribe each track and merge them into one transcript by timestamp
            - Summarise the call and list action items with an LLM
            - Post the notes in the text channel when /stop is used
Storage:    SQLite, local disk (audio)
Tech stack: Python, Pycord (voice receive), faster-whisper, LLM API
```

---

## Example 803

**Intent:**
I run a small hardware store and I'd love a simple system to track what's in stock and warn me when something runs low

**Spec:**
```
Type:       Web application (inventory management)
Auth:       Staff login (email + password), roles: owner, staff
Data model: User(id, name, email, password_hash, role)
            Product(id, sku, name, category, unit_price, quantity, reorder_level)
            StockMovement(id, product_id -> Product, user_id -> User, change, reason, created_at)
Features:   - Add, edit and archive products with SKU and category
            - Record stock received and stock sold as movements
            - Highlight products whose quantity is below the reorder level
            - Email the owner a daily low-stock summary
            - Search products by name, SKU or category
            - Export the current stock list to CSV
API:        REST
            POST /login
            GET  /products?low_stock={bool}
            POST /products
            PUT  /products/{id}
            POST /products/{id}/movements
            GET  /reports/low-stock
Storage:    PostgreSQL
Tech stack: Python, Django, Django admin, Celery (daily email job)
```

---

## Example 804

**Intent:**
leave request app for my team

**Spec:**
```
Type:       Web application (HR / leave management)
Auth:       Company SSO login (Google Workspace OAuth), roles: employee, manager, HR
Data model: Employee(id, name, email, manager_id -> Employee, annual_allowance_days)
            LeaveRequest(id, employee_id -> Employee, type, start_date, end_date, status, comment)
            PublicHoliday(id, date, name)
Features:   - Submit a leave request with type, dates and a comment
            - Approve or reject requests as the employee's manager
            - Calculate remaining days excluding weekends and public holidays
            - Show a team calendar of who is off each day
            - Notify employees by email when a request is approved or rejected
API:        REST
            GET  /me/leave-balance
            GET  /leave-requests?status={status}
            POST /leave-requests
            POST /leave-requests/{id}/approve
            POST /leave-requests/{id}/reject
            GET  /calendar?month={yyyy-mm}
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, React, FullCalendar
```

---

## Example 805

**Intent:**
I want an ESP32 in my greenhouse that measures temperature and humidity and shows it on a dashboard

**Spec:**
```
Type:       IoT sensor system with web dashboard
Data model: Reading(device_id, temperature_c, humidity_percent, recorded_at)
Features:   - Read temperature and humidity from a DHT22 sensor every 60 seconds
            - Publish readings to an MQTT broker over Wi-Fi
            - Store readings as time-series data
            - Show live and historical charts per sensor on a dashboard
            - Alert by Telegram when temperature leaves a set range
API:        MQTT
            PUB  greenhouse/{device_id}/temperature
            PUB  greenhouse/{device_id}/humidity
Storage:    InfluxDB
Tech stack: ESP32, Arduino C++ (PubSubClient, DHT library), Mosquitto, Telegraf, Grafana
```

---

## Example 806

**Intent:**
helpdesk ticketing system for our IT department, users email in problems and techs pick them up

**Spec:**
```
Type:       Web application (helpdesk / ticketing)
Auth:       Login for technicians (email + password); requesters identified by email address
Data model: Technician(id, name, email, password_hash)
            Ticket(id, requester_email, subject, body, priority, status, assignee_id -> Technician, created_at)
            Comment(id, ticket_id -> Ticket, author, body, is_internal, created_at)
Features:   - Create tickets automatically from emails sent to the support inbox
            - Assign tickets to technicians and set priority
            - Reply to the requester by email from the ticket page
            - Add internal notes that the requester cannot see
            - Track ticket status: open, in progress, waiting, closed
            - Show each technician a queue of their open tickets
API:        REST
            GET  /tickets?status={status}&assignee={id}
            GET  /tickets/{id}
            PATCH /tickets/{id}
            POST /tickets/{id}/comments
            POST /inbound-email
Storage:    PostgreSQL, S3 (attachments)
Tech stack: Ruby on Rails, Action Mailbox, Hotwire
```

---

## Example 807

**Intent:**
plant watering thing with raspberry pi and soil moisture sensor

**Spec:**
```
Type:       IoT automation (Raspberry Pi)
Data model: MoistureReading(id, plant_id, moisture_percent, recorded_at)
            WateringEvent(id, plant_id, duration_seconds, triggered_by, created_at)
Features:   - Read soil moisture from a capacitive sensor through an ADS1115 ADC
            - Turn on a water pump via a relay when moisture drops below a threshold
            - Limit watering to a maximum duration per day
            - Log readings and watering events
            - Show moisture history and a manual "water now" button on a local web page
API:        REST
            GET  /readings?plant={id}
            POST /plants/{id}/water
Storage:    SQLite
Tech stack: Raspberry Pi, Python, gpiozero, Adafruit ADS1x15, Flask
```

---

## Example 808

**Intent:**
We are a sales team of 12 people and we keep losing track of leads in spreadsheets. I want a lightweight CRM where we can log contacts, companies and deals, move deals through pipeline stages, and see a forecast of expected revenue for the quarter. It should also remind people when a follow-up is due.

**Spec:**
```
Type:       Web application (CRM)
Auth:       User login (email + password), roles: rep, sales manager
Data model: User(id, name, email, password_hash, role)
            Company(id, name, industry, website)
            Contact(id, company_id -> Company, name, email, phone)
            Deal(id, company_id -> Company, owner_id -> User, title, value, stage, probability, close_date)
            Activity(id, deal_id -> Deal, user_id -> User, type, note, due_at, done)
Features:   - Create and edit companies, contacts and deals
            - Drag deals between pipeline stages on a kanban board
            - Log calls, emails and meetings against a deal
            - Remind the deal owner by email when a follow-up is due
            - Show a quarterly revenue forecast weighted by stage probability
            - Filter the pipeline by owner, stage and close date
API:        REST
            GET  /deals?stage={stage}&owner={id}
            POST /deals
            PATCH /deals/{id}
            POST /deals/{id}/activities
            GET  /forecast?quarter={q}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma, Tailwind CSS
```

---

## Example 809

**Intent:**
can you make me a uptime checker that pings my websites every minute and texts me if one goes down

**Spec:**
```
Type:       Monitoring service (uptime checker)
Auth:       Single admin login (username + password)
Data model: Monitor(id, name, url, interval_seconds, expected_status, is_active)
            Check(id, monitor_id -> Monitor, status_code, response_ms, is_up, checked_at)
            Incident(id, monitor_id -> Monitor, started_at, resolved_at)
Features:   - Send an HTTP request to each monitored URL every minute
            - Mark a site down after 3 failed checks in a row
            - Send an SMS when a site goes down and when it recovers
            - Show uptime percentage and response time charts per site
            - Keep a history of incidents with their duration
API:        REST
            GET  /monitors
            POST /monitors
            DELETE /monitors/{id}
            GET  /monitors/{id}/checks?from={time}
Storage:    SQLite
Tech stack: Go, net/http, Twilio API, HTML templates, Chart.js
```

---

## Example 810

**Intent:**
i want a admin panel with retool for our orders database so support can look up and refund orders

**Spec:**
```
Type:       Internal tool (admin panel)
Auth:       Retool SSO with permission groups (support, admin)
Data model: Customer(id, name, email)
            Order(id, customer_id -> Customer, total, status, created_at)
            Refund(id, order_id -> Order, amount, reason, issued_by, created_at)
Features:   - Search orders by order ID, customer email or date range
            - Show order details with line items and payment status
            - Issue a full or partial refund through the payment provider
            - Require an admin to approve refunds above a set amount
            - Log every refund with the staff member who issued it
API:        REST
            POST /v1/refunds
Storage:    Existing PostgreSQL orders database (read), audit table for refunds
Tech stack: Retool, PostgreSQL resource, Stripe API resource
```

---

## Example 811

**Intent:**
door sensor that tells me on my phone when the front door opens

**Spec:**
```
Type:       IoT sensor (smart home)
Features:   - Detect door open and close with a magnetic reed switch
            - Wake from deep sleep on a pin change to save battery
            - Publish the door state to MQTT when it changes
            - Send a phone notification when the door opens
            - Report battery voltage once per hour
API:        MQTT
            PUB  home/front_door/state
            PUB  home/front_door/battery
Tech stack: ESP8266, Arduino C++, Mosquitto, Home Assistant (mobile app notifications)
```

---

## Example 812

**Intent:**
Hello, I need system for approve purchase requests in our company, employee make request then manager approve and after that finance approve if amount is big.

**Spec:**
```
Type:       Web application (approval workflow)
Auth:       Company login (Microsoft Entra ID SSO), roles: employee, manager, finance
Data model: User(id, name, email, role, manager_id -> User)
            PurchaseRequest(id, requester_id -> User, item, supplier, amount, currency, status, created_at)
            Approval(id, request_id -> PurchaseRequest, approver_id -> User, step, decision, comment, decided_at)
Features:   - Submit a purchase request with item, supplier, amount and a quote attachment
            - Route the request to the requester's manager for approval
            - Route requests above a set amount to finance as a second step
            - Notify the next approver and the requester by email at each step
            - Show the full approval history on each request
            - List pending approvals for the logged-in approver
API:        REST
            POST /requests
            GET  /requests?status={status}
            GET  /approvals/pending
            POST /requests/{id}/decision
Storage:    SQL Server, Azure Blob Storage (attachments)
Tech stack: C#, ASP.NET Core, Angular
```

---

## Example 813

**Intent:**
shift scheduling for my cafe staff

**Spec:**
```
Type:       Web application (employee scheduling)
Auth:       Login for manager and staff (email + password)
Data model: Employee(id, name, email, phone, max_hours_per_week)
            Availability(id, employee_id -> Employee, weekday, start_time, end_time)
            Shift(id, employee_id -> Employee, date, start_time, end_time, role)
Features:   - Build a weekly roster by dragging staff into shifts
            - Warn when a shift clashes with availability or exceeds max hours
            - Publish the roster and notify staff by SMS
            - Let staff request a shift swap that the manager approves
            - Show total scheduled hours and labour cost per week
API:        REST
            GET  /shifts?week={date}
            POST /shifts
            PUT  /shifts/{id}
            POST /shifts/{id}/swap-requests
            POST /rosters/{week}/publish
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Vue.js, Twilio API
```

---

## Example 814

**Intent:**
i wnat to see how much electricity my house uses, i have a esp32 and a ct clamp

**Spec:**
```
Type:       IoT energy monitor
Data model: PowerReading(circuit, watts, kwh_total, recorded_at)
Features:   - Measure current with an SCT-013 CT clamp on the ESP32's ADC
            - Calculate real power in watts and accumulated kWh
            - Publish readings to Home Assistant every 10 seconds
            - Show live power usage and daily kWh in a dashboard
            - Estimate the monthly cost from a set tariff
API:        MQTT
            PUB  energy/{circuit}/power
            PUB  energy/{circuit}/kwh
Storage:    InfluxDB
Tech stack: ESP32, ESPHome (CT clamp sensor), Home Assistant Energy dashboard, InfluxDB
```

---

## Example 815

**Intent:**
A KPI dashboard for our e-commerce leadership team showing revenue, orders, average order value and conversion rate. Data lives in our Postgres database and Google Analytics. It should refresh every hour and let people compare this month to last month.

**Spec:**
```
Type:       Business intelligence dashboard
Auth:       Google Workspace SSO, restricted to the leadership group
Data model: DailyKpi(date, revenue, orders, avg_order_value, sessions, conversion_rate)
Features:   - Pull orders from PostgreSQL and sessions from the Google Analytics Data API
            - Aggregate KPIs per day in an hourly scheduled job
            - Show KPI cards with change versus the previous period
            - Plot revenue and orders as trend lines over a chosen date range
            - Compare this month to last month side by side
            - Break down revenue by channel and product category
Storage:    PostgreSQL (aggregated KPI table)
Tech stack: Python, Airflow (hourly job), Metabase, Google Analytics Data API
```

---

## Example 816

**Intent:**
track where our delivery vans are on a map in real time

**Spec:**
```
Type:       Fleet tracking system (web + GPS devices)
Auth:       Dispatcher login (email + password); devices authenticate with an API token
Data model: Vehicle(id, plate_number, driver_name, device_token_hash)
            Position(id, vehicle_id -> Vehicle, lat, lng, speed_kmh, heading, recorded_at)
Features:   - Receive GPS positions from each van every 15 seconds
            - Show all vans on a live map with their current speed
            - Replay a van's route for a chosen day
            - Mark a van as offline when no position arrives for 5 minutes
            - Calculate distance driven per van per day
API:        REST + WebSocket
            POST /devices/positions
            GET  /vehicles
            GET  /vehicles/{id}/route?date={date}
            WS   /live/positions
Storage:    PostgreSQL with PostGIS
Tech stack: Node.js, Express, Socket.IO, React, Leaflet
```

---

## Example 817

**Intent:**
hey so we have a warehouse and pickers walk around with scanners, can we build something where they scan barcodes to confirm the right items are picked for each order

**Spec:**
```
Type:       Mobile web application (warehouse picking)
Auth:       Picker login with employee number and PIN
Data model: Picker(id, employee_number, name, pin_hash)
            Order(id, number, status, assigned_picker_id -> Picker)
            OrderLine(id, order_id -> Order, sku, bin_location, quantity, picked_quantity)
Features:   - Show the next order to pick with lines sorted by bin location
            - Scan an item barcode with the device camera or a hardware scanner
            - Reject a scan when the barcode does not match the expected SKU
            - Mark the order complete when all lines are fully picked
            - Report short picks to a supervisor
            - Show picks per hour per picker for supervisors
API:        REST
            GET  /pickers/me/next-order
            POST /orders/{id}/scans
            POST /orders/{id}/complete
            GET  /stats/pick-rate
Storage:    PostgreSQL
Tech stack: TypeScript, Express, React (PWA), ZXing barcode scanner
```

---

## Example 818

**Intent:**
mqtt dashboard with node-red for all my sensors at home

**Spec:**
```
Type:       Smart home dashboard
Features:   - Subscribe to all sensor topics on the local MQTT broker
            - Show gauges for temperature and humidity per room
            - Show on/off status for doors, windows and motion sensors
            - Plot the last 24 hours of each sensor on a chart
            - Send a Telegram message when a sensor stops reporting for 30 minutes
API:        MQTT
            SUB  home/+/temperature
            SUB  home/+/humidity
            SUB  home/+/contact
            SUB  home/+/motion
Storage:    Node-RED context storage (localfilesystem)
Tech stack: Node-RED, node-red-dashboard, Mosquitto, node-red-contrib-telegrambot
```

---

## Example 819

**Intent:**
something so our office knows which meeting rooms are free right now

**Spec:**
```
Type:       Web application (room availability display)
Auth:       Microsoft 365 login (OAuth) for booking; read-only display needs no login
Data model: Room(id, name, capacity, calendar_email, floor)
Features:   - Read room bookings from each room's Outlook calendar
            - Show every room as free, busy or free soon on one screen
            - Show the current and next meeting for each room
            - Book a free room for 15, 30 or 60 minutes from a tablet outside the room
            - Refresh the status every minute
API:        REST
            GET  /rooms/status
            POST /rooms/{id}/quick-book
Tech stack: TypeScript, Node.js, Microsoft Graph API, Vue.js
```

---

## Example 820

**Intent:**
I'm a landlord with 6 flats and want a place to log maintenance requests from tenants and track which contractor fixed what

**Spec:**
```
Type:       Web application (maintenance tracking)
Auth:       Landlord login (email + password); tenants submit via a per-flat link with a token
Data model: Property(id, address, unit, access_token)
            Contractor(id, name, trade, phone, email)
            MaintenanceRequest(id, property_id -> Property, title, description, photo_url, status, created_at)
            Job(id, request_id -> MaintenanceRequest, contractor_id -> Contractor, scheduled_for, cost, completed_at)
Features:   - Let tenants submit a request with a description and photo
            - Assign a contractor to a request and schedule a visit
            - Track status from reported to scheduled to fixed
            - Record the cost of each job and total spend per flat
            - Email the tenant when the visit is scheduled
API:        REST
            POST /p/{token}/requests
            GET  /requests?status={status}
            POST /requests/{id}/jobs
            PATCH /jobs/{id}
Storage:    SQLite, local disk (photos)
Tech stack: Python, Django, HTMX
```

---

## Example 821

**Intent:**
temp logger for the lab freezer, arduino

**Spec:**
```
Type:       Embedded data logger (Arduino)
Features:   - Read temperature from a DS18B20 probe every 30 seconds
            - Write timestamped readings to a CSV file on an SD card
            - Keep time with a DS3231 real-time clock module
            - Sound a buzzer and light an LED when temperature exceeds a limit
            - Show the current temperature on a 16x2 LCD
Storage:    SD card (CSV file)
Tech stack: Arduino Uno, Arduino C++, OneWire, DallasTemperature, RTClib, SD library
```

---

## Example 822

**Intent:**
build me an asset tracker for our company laptops and monitors — who has what, serial numbers, warranty dates

**Spec:**
```
Type:       Web application (IT asset management)
Auth:       IT staff login (Google Workspace SSO)
Data model: Asset(id, asset_tag, type, model, serial_number, purchase_date, warranty_until, status)
            Employee(id, name, email, department)
            Assignment(id, asset_id -> Asset, employee_id -> Employee, assigned_at, returned_at)
Features:   - Register assets with tag, model, serial number and warranty date
            - Assign an asset to an employee and record its return
            - Show the full assignment history of each asset
            - List assets whose warranty expires in the next 60 days
            - Print asset tag labels with a QR code
            - Import existing assets from a CSV file
API:        REST
            GET  /assets?status={status}
            POST /assets
            POST /assets/{id}/assign
            POST /assets/{id}/return
            GET  /assets/warranty-expiring
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, qrcode library
```

---

## Example 823

**Intent:**
Our factory has 20 machines with PLCs and we want to see on one screen which machines are running, idle or in fault, plus the OEE for each shift. The PLCs speak Modbus TCP. Supervisors should get an alert if a machine is in fault for more than 10 minutes.

**Spec:**
```
Type:       Industrial monitoring dashboard (OEE)
Auth:       Supervisor login (username + password)
Data model: Machine(id, name, line, plc_ip, ideal_cycle_seconds)
            StateChange(machine_id -> Machine, state, fault_code, changed_at)
            ProductionCount(machine_id -> Machine, good_count, reject_count, recorded_at)
Features:   - Poll each PLC over Modbus TCP every 5 seconds for state and counters
            - Show every machine as running, idle or fault on a live overview screen
            - Calculate availability, performance, quality and OEE per shift
            - Alert supervisors by email when a machine stays in fault for 10 minutes
            - Show a downtime breakdown by fault code
Storage:    TimescaleDB
Tech stack: Python, pymodbus, TimescaleDB, Grafana (dashboards and alerting)
```

---

## Example 824

**Intent:**
a status page for our saas so customers can see if something is broken

**Spec:**
```
Type:       Web application (public status page)
Auth:       Admin login for the team (email + password + TOTP)
Data model: Component(id, name, group, status)
            Incident(id, title, impact, status, started_at, resolved_at)
            IncidentUpdate(id, incident_id -> Incident, message, status, created_at)
            Subscriber(id, email, confirmed)
Features:   - Show the current status of each component on a public page
            - Post incidents and timed updates as the team investigates
            - Show 90 days of uptime history per component
            - Email subscribers when an incident is opened or resolved
            - Schedule maintenance windows in advance
API:        REST
            GET  /api/status
            POST /admin/incidents
            POST /admin/incidents/{id}/updates
            POST /subscribe
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView
```

---

## Example 825

**Intent:**
smart lights for my room controlled from my phone, i have some esp8266 boards

**Spec:**
```
Type:       IoT smart home (lighting control)
Features:   - Drive a WS2812B LED strip from an ESP8266
            - Turn lights on and off and set brightness and colour from a phone
            - Choose from preset effects (rainbow, fade, solid)
            - Turn lights on automatically at sunset
            - Remember the last state after a power cut
API:        REST
            GET  /json/state
            POST /json/state
Tech stack: ESP8266, WLED firmware, WLED mobile app
```

---

## Example 826

**Intent:**
expense claims tool, employees upload receipts and finance pays them back

**Spec:**
```
Type:       Web application (expense management)
Auth:       Company SSO (Okta), roles: employee, approver, finance
Data model: Employee(id, name, email, approver_id -> Employee, bank_account_last4)
            ExpenseClaim(id, employee_id -> Employee, title, total, status, submitted_at)
            ExpenseItem(id, claim_id -> ExpenseClaim, date, category, amount, receipt_url)
Features:   - Upload receipt photos and extract amount and date with OCR
            - Group expense items into a claim and submit it
            - Approve or reject claims as the employee's approver
            - Mark approved claims as paid in a weekly payout batch
            - Export paid claims to the accounting system as CSV
API:        REST
            POST /claims
            POST /claims/{id}/items
            POST /claims/{id}/submit
            POST /claims/{id}/decision
            GET  /payouts/next
Storage:    PostgreSQL, S3 (receipts)
Tech stack: Python, Django, React, AWS Textract
```

---

## Example 827

**Intent:**
alerting when our kafka consumers fall behind

**Spec:**
```
Type:       Monitoring and alerting setup
Features:   - Export consumer group lag per topic and partition
            - Scrape lag metrics every 30 seconds
            - Fire an alert when lag keeps growing for more than 10 minutes
            - Route alerts to the owning team's Slack channel
            - Show lag per consumer group on a dashboard
Storage:    Prometheus time-series database
Tech stack: Kafka Lag Exporter, Prometheus, Alertmanager, Grafana
```

---

## Example 828

**Intent:**
pls make a app for teh gym owners to see how many people are inside right now using a door counter

**Spec:**
```
Type:       IoT occupancy counter with web dashboard
Data model: Gym(id, name, capacity)
            CountEvent(id, gym_id -> Gym, direction, created_at)
Features:   - Detect people entering and leaving with a pair of break-beam sensors at the door
            - Work out direction from which beam breaks first
            - Send each entry and exit event to the server over Wi-Fi
            - Show current occupancy against capacity on a live dashboard
            - Show busiest hours of the week as a heatmap
            - Reset the count to zero automatically at closing time
API:        REST + WebSocket
            POST /gyms/{id}/events
            GET  /gyms/{id}/occupancy
            GET  /gyms/{id}/stats/hourly
            WS   /gyms/{id}/live
Storage:    PostgreSQL
Tech stack: ESP32, Arduino C++, Node.js, Fastify, Svelte, Chart.js
```

---

## Example 829

**Intent:**
visitor sign in tablet for reception

**Spec:**
```
Type:       Web application (visitor management kiosk)
Auth:       Reception staff login (email + password); kiosk runs in a locked session
Data model: Employee(id, name, email, phone)
            Visit(id, visitor_name, company, host_id -> Employee, photo_url, signed_in_at, signed_out_at)
Features:   - Let visitors sign in on a tablet with name, company and the person they are visiting
            - Take a photo of the visitor with the tablet camera
            - Notify the host by Slack when their visitor arrives
            - Print a name badge on a label printer
            - Show reception a list of visitors currently in the building
            - Sign visitors out and keep a log for fire roll calls
API:        REST
            POST /visits
            POST /visits/{id}/sign-out
            GET  /visits?on_site=true
Storage:    PostgreSQL, S3 (photos)
Tech stack: TypeScript, React, Node.js, Express, Slack API
```

---

## Example 830

**Intent:**
I want grafana alerts if the freezers in my restaurant get too warm, I already have some zigbee temperature sensors

**Spec:**
```
Type:       IoT monitoring and alerting
Data model: Reading(sensor, temperature_c, battery_percent, recorded_at)
Features:   - Receive readings from Zigbee temperature sensors through a USB coordinator
            - Forward readings to MQTT and store them in a time-series database
            - Show temperature history for each freezer on a Grafana dashboard
            - Alert by SMS when a freezer stays above -15 °C for 15 minutes
            - Alert when a sensor's battery is low or it stops reporting
API:        MQTT
            SUB  zigbee2mqtt/+
Storage:    InfluxDB
Tech stack: Zigbee2MQTT, Mosquitto, Telegraf, InfluxDB, Grafana (alerting with Twilio contact point)
```

---

## Example 831

**Intent:**
our company need simple system where employee can check in and check out work time with their phone and HR can see report every month

**Spec:**
```
Type:       Mobile + web application (time and attendance)
Auth:       Employee login (email + password), roles: employee, HR
Data model: Employee(id, name, email, department, password_hash)
            TimeEntry(id, employee_id -> Employee, check_in_at, check_out_at, check_in_lat, check_in_lng)
            Office(id, name, lat, lng, radius_m)
Features:   - Check in and check out with one tap on the phone
            - Record GPS location and reject check-ins outside the office radius
            - Show employees their hours worked this week
            - Generate a monthly hours report per employee for HR
            - Flag missing check-outs and late arrivals
            - Export the monthly report to Excel
API:        REST
            POST /time-entries/check-in
            POST /time-entries/check-out
            GET  /me/time-entries?month={yyyy-mm}
            GET  /reports/monthly?month={yyyy-mm}
Storage:    PostgreSQL
Tech stack: Flutter (mobile), Python, Django REST Framework, React (HR web), openpyxl
```

---

## Example 832

**Intent:**
bug tracker for a small dev team

**Spec:**
```
Type:       Web application (issue tracker)
Auth:       User login (GitHub OAuth)
Data model: User(id, github_id, name, avatar_url)
            Project(id, name, key)
            Issue(id, project_id -> Project, number, title, description, type, priority, status, assignee_id -> User)
            IssueComment(id, issue_id -> Issue, author_id -> User, body, created_at)
Features:   - Create issues with type, priority and assignee
            - Move issues across a board: backlog, todo, in progress, done
            - Comment on issues with Markdown and mention teammates
            - Link issues to GitHub pull requests by issue key
            - Filter issues by project, assignee, label and status
API:        REST
            GET  /projects/{id}/issues?status={status}
            POST /projects/{id}/issues
            PATCH /issues/{id}
            POST /issues/{id}/comments
            POST /webhooks/github
Storage:    PostgreSQL
Tech stack: Go, chi router, React, TypeScript
```

---

## Example 833

**Intent:**
I've got a 3D printer farm with 8 printers running OctoPrint and I want one page that shows every printer's progress, temperatures and webcam, and pings me on Discord when a print finishes or fails.

**Spec:**
```
Type:       Monitoring dashboard (3D printer farm)
Auth:       Single admin login (username + password)
Data model: Printer(id, name, octoprint_url, api_key)
            PrintJob(id, printer_id -> Printer, file_name, started_at, finished_at, result)
Features:   - Poll each OctoPrint instance's API every 5 seconds for job and temperature data
            - Show all printers in a grid with progress bar, time left and nozzle and bed temperature
            - Show the webcam stream of a printer when its tile is clicked
            - Send a Discord message when a print finishes, fails or is cancelled
            - Keep a history of print jobs with duration and result
API:        REST + WebSocket
            GET  /printers
            GET  /jobs?printer={id}
            WS   /live
Storage:    SQLite
Tech stack: Python, FastAPI, httpx, Vue.js, OctoPrint REST API, Discord webhooks
```

---

## Example 834

**Intent:**
dashboard for the call center showing calls waiting, average wait time and agents available

**Spec:**
```
Type:       Real-time operations dashboard (wallboard)
Auth:       Supervisor login (SSO)
Data model: QueueSnapshot(queue, calls_waiting, longest_wait_seconds, agents_available, recorded_at)
            CallRecord(id, queue, agent_id, wait_seconds, talk_seconds, answered, started_at)
Features:   - Receive live queue and agent events from the phone system
            - Show calls waiting, longest wait and available agents per queue on a TV wallboard
            - Turn a queue tile red when the longest wait exceeds the target
            - Show today's service level and abandoned call rate
            - Show a leaderboard of calls handled per agent
API:        REST + WebSocket
            POST /webhooks/telephony
            GET  /queues/summary
            WS   /wallboard/live
Storage:    Redis (live state), PostgreSQL (call records)
Tech stack: Node.js, NestJS, Socket.IO, React, Twilio TaskRouter events
```

---

## Example 835

**Intent:**
need to check every morning that all our ssl certificates arent about to expire

**Spec:**
```
Type:       Scheduled monitoring script
Data model: Domain(name, port, owner_email)
            CertCheck(domain, issuer, expires_at, days_left, checked_at)
Features:   - Connect to each domain over TLS and read its certificate
            - Calculate the days left until the certificate expires
            - Email the owner when fewer than 21 days remain
            - Report domains whose certificate is invalid or unreachable
            - Write a daily summary table to a Slack channel
Input:      YAML file listing domains, ports and owner emails
Storage:    SQLite (check history)
Tech stack: Python, ssl and socket modules, PyYAML, smtplib, Slack webhook, cron
```

---

## Example 836

**Intent:**
Hi, i want make a smart beehive. Put sensors inside for weight, temperature and humidity, and send data from field where is no wifi.

**Spec:**
```
Type:       IoT remote sensor (LoRaWAN)
Data model: HiveReading(hive_id, weight_kg, temperature_c, humidity_percent, battery_v, recorded_at)
Features:   - Measure hive weight with load cells and an HX711 amplifier
            - Measure inside temperature and humidity with an SHT31 sensor
            - Send readings every 15 minutes over LoRaWAN
            - Sleep between readings to run for months on a battery and solar panel
            - Show weight and temperature charts per hive on a dashboard
            - Alert when weight drops suddenly, which may mean swarming
API:        MQTT
            SUB  v3/{app_id}/devices/+/up
Storage:    InfluxDB
Tech stack: Heltec CubeCell (LoRa), Arduino C++, The Things Network, Node-RED, InfluxDB, Grafana
```

---

## Example 837

**Intent:**
library system for a school to check out books to students

**Spec:**
```
Type:       Web application (library management)
Auth:       Librarian login (email + password)
Data model: Book(id, isbn, title, author, copies_total)
            Copy(id, book_id -> Book, barcode, status)
            Student(id, name, class, student_number)
            Loan(id, copy_id -> Copy, student_id -> Student, borrowed_at, due_at, returned_at)
Features:   - Add books by scanning the ISBN and fetching details from Open Library
            - Check out and return copies by scanning their barcode
            - Show overdue loans grouped by class
            - Limit each student to 3 books at a time
            - Search the catalogue by title, author or ISBN
API:        REST
            GET  /books?q={query}
            POST /books
            POST /loans
            POST /loans/{id}/return
            GET  /loans/overdue
Storage:    MySQL
Tech stack: PHP, Laravel, Livewire, Open Library API
```

---

## Example 838

**Intent:**
appsmith internal tool for our customer success team to see accounts, their subscription plan and recent support tickets in one place

**Spec:**
```
Type:       Internal tool (customer 360 view)
Auth:       Appsmith login with Google SSO, restricted to the customer success group
Data model: Account(id, name, plan, mrr, renewal_date, csm_owner)
            Ticket(id, account_id -> Account, subject, status, created_at)
Features:   - Search accounts by name or domain
            - Show plan, MRR and renewal date from the billing database
            - Show the last 20 support tickets from the helpdesk API
            - Flag accounts renewing in 30 days with open high-priority tickets
            - Let CSMs add notes that are saved to the account
API:        REST
            GET  /api/v2/search?query=organization:{id}
Storage:    PostgreSQL (accounts and notes)
Tech stack: Appsmith, PostgreSQL datasource, Zendesk REST API datasource
```

---

## Example 839

**Intent:**
I'd like to know when the washing machine in the basement is done so I stop walking down there to check

**Spec:**
```
Type:       IoT smart home automation
Features:   - Measure the washing machine's power draw with a smart plug
            - Detect the end of a cycle when power stays below 5 W for 3 minutes
            - Send a phone notification when the wash is done
            - Remind again after 30 minutes if the door has not been opened
            - Show today's number of washes and energy used
API:        MQTT
            SUB  shellies/washer/relay/0/power
Tech stack: Shelly Plug S, Home Assistant (automations, mobile app), Mosquitto
```

---

## Example 840

**Intent:**
contract renewal reminders for our procurement team

**Spec:**
```
Type:       Web application (contract management)
Auth:       Company SSO (Azure AD)
Data model: Vendor(id, name, contact_email)
            Contract(id, vendor_id -> Vendor, title, value, start_date, end_date, notice_days, owner_email, file_url)
Features:   - Upload contracts with vendor, value, end date and notice period
            - Calculate the last date to cancel from the end date and notice period
            - Email the owner 60, 30 and 7 days before the notice deadline
            - Show a timeline of upcoming renewals
            - Search contracts by vendor and owner
API:        REST
            GET  /contracts?expiring_within={days}
            POST /contracts
            PUT  /contracts/{id}
Storage:    PostgreSQL, Azure Blob Storage (contract PDFs)
Tech stack: C#, ASP.NET Core, Blazor, Hangfire (scheduled emails)
```

---

## Example 841

**Intent:**
how about a little screen on my desk that shows if our ci builds are passing

**Spec:**
```
Type:       IoT status display
Features:   - Poll the CI provider's API for the latest build on each main branch
            - Show each repository as a green or red row on a small TFT screen
            - Flash the screen and beep when a build goes from passing to failing
            - Show the name of the person whose commit broke the build
            - Connect to Wi-Fi with a captive-portal setup page
API:        REST
            GET  /repos/{owner}/{repo}/actions/runs?branch=main&per_page=1
Tech stack: ESP32, ILI9341 TFT display, Arduino C++ (TFT_eSPI, WiFiManager, ArduinoJson), GitHub REST API
```

---

## Example 842

**Intent:**
Our NGO distributes food parcels at 4 locations and we need to track stock of each item per location, record which families received parcels so nobody gets two in the same week, and give donors a monthly report of how many people we helped. Volunteers use cheap Android phones.

**Spec:**
```
Type:       Web application (distribution and inventory, mobile-friendly)
Auth:       Volunteer login (phone number + one-time SMS code), roles: volunteer, coordinator
Data model: Location(id, name, address)
            Item(id, name, unit)
            Stock(id, location_id -> Location, item_id -> Item, quantity)
            Family(id, reference_code, household_size, registered_at)
            Distribution(id, family_id -> Family, location_id -> Location, volunteer_id, distributed_at)
Features:   - Look up a family by reference code or QR card
            - Block a second parcel for the same family in the same week
            - Deduct parcel items from the location's stock on each distribution
            - Record stock donations received at each location
            - Generate a monthly report of parcels given and people helped
            - Work offline and sync when the connection returns
API:        REST
            GET  /families/{code}
            POST /distributions
            GET  /locations/{id}/stock
            POST /locations/{id}/stock-in
            GET  /reports/monthly?month={yyyy-mm}
Storage:    PostgreSQL (server), IndexedDB (offline cache on phones)
Tech stack: Python, Django, Progressive Web App (Workbox), Twilio Verify
```

---

## Example 843

**Intent:**
garage door opener from my phone, raspberry pi zero

**Spec:**
```
Type:       IoT smart home (garage door controller)
Auth:       Login with a password and a long-lived session cookie
Features:   - Trigger the garage door opener through a relay wired to the wall button
            - Read the door position with a magnetic reed switch
            - Show open or closed status on a phone-friendly web page
            - Send a notification if the door is left open after 10 PM
            - Log every open and close with the time
API:        REST
            GET  /door
            POST /door/toggle
Storage:    SQLite (event log)
Tech stack: Raspberry Pi Zero W, Python, gpiozero, Flask, ntfy (push notifications)
```

---

## Example 844

**Intent:**
kpi dashbord for our support team, tickets solved per agent, first respons time, csat

**Spec:**
```
Type:       KPI dashboard (customer support)
Auth:       Login with Google SSO
Data model: TicketFact(ticket_id, agent, channel, created_at, first_response_at, solved_at, csat_score)
Features:   - Sync solved tickets and ratings from the helpdesk API every hour
            - Show tickets solved per agent for the selected period
            - Show median first response time and resolution time
            - Show CSAT score trend by week
            - Compare agents in a sortable leaderboard table
Storage:    BigQuery
Tech stack: Python (sync job on Cloud Run), Zendesk API, BigQuery, Looker Studio
```

---

## Example 845

**Intent:**
monitor the water level in our rain tank

**Spec:**
```
Type:       IoT sensor (tank level monitor)
Data model: LevelReading(tank_id, distance_cm, level_percent, litres, recorded_at)
Features:   - Measure the distance to the water surface with a waterproof ultrasonic sensor
            - Convert distance to percent full and litres from the tank dimensions
            - Send a reading every 30 minutes and deep sleep in between
            - Show the current level and a 30-day chart in Home Assistant
            - Notify when the tank drops below 20 percent
Tech stack: ESP32, ESPHome (ultrasonic sensor, deep sleep), JSN-SR04T sensor, Home Assistant
```

---

## Example 846

**Intent:**
a simple onboarding checklist tool so HR, IT and the manager each know what to do when a new hire starts

**Spec:**
```
Type:       Web application (employee onboarding workflow)
Auth:       Company SSO (Google Workspace), roles: HR, IT, manager
Data model: Template(id, name, department)
            TemplateTask(id, template_id -> Template, title, owner_role, days_from_start)
            NewHire(id, name, email, department, start_date, manager_email)
            Task(id, new_hire_id -> NewHire, title, owner_role, due_date, done_at)
Features:   - Create onboarding templates with tasks per role
            - Generate a task list with due dates when a new hire is added
            - Show each role only the tasks assigned to them
            - Send a daily email digest of tasks due and overdue
            - Show progress per new hire as a percentage
API:        REST
            POST /new-hires
            GET  /tasks?role={role}&status={status}
            POST /tasks/{id}/complete
            GET  /templates
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire, Sidekiq
```

---

## Example 847

**Intent:**
cold chain tracking for our trucks, want temperature and gps of each fridge truck

**Spec:**
```
Type:       IoT fleet monitoring system
Auth:       Dispatcher login (email + password); trackers authenticate with per-device credentials
Data model: Truck(id, plate_number, min_temp_c, max_temp_c)
            Telemetry(truck_id -> Truck, lat, lng, temperature_c, door_open, recorded_at)
            Alert(id, truck_id -> Truck, type, started_at, resolved_at)
Features:   - Send GPS position, cargo temperature and door state every minute over 4G
            - Buffer readings on the device when there is no signal
            - Show trucks on a map coloured by temperature status
            - Alert dispatchers when temperature leaves the allowed range for 10 minutes
            - Produce a temperature report per delivery for customers
API:        MQTT
            PUB  fleet/{truck_id}/telemetry
            SUB  fleet/{truck_id}/config
Storage:    TimescaleDB
Tech stack: ESP32 with SIM7600 4G module, ESP-IDF, AWS IoT Core, Python, React, Mapbox GL
```

---

## Example 848

**Intent:**
admin dashboard for our mobile app users

**Spec:**
```
Type:       Web application (admin panel)
Auth:       Admin login (email + password + TOTP), roles: viewer, admin
Data model: AppUser(id, email, display_name, plan, status, created_at, last_seen_at)
            AdminAction(id, admin_email, app_user_id -> AppUser, action, reason, created_at)
Features:   - Search users by email, name or ID
            - Show a user's profile, plan and recent activity
            - Suspend or reactivate a user account with a reason
            - Show daily signups and active users as charts
            - Log every admin action for auditing
API:        REST
            GET  /admin/users?q={query}
            GET  /admin/users/{id}
            POST /admin/users/{id}/suspend
            POST /admin/users/{id}/reactivate
            GET  /admin/stats/daily
Storage:    PostgreSQL
Tech stack: TypeScript, React Admin, Node.js, Express
```

---

## Example 849

**Intent:**
yo i want my aquarium to feed the fish and turn the light on and off on a schedule, arduino nano

**Spec:**
```
Type:       Embedded automation (Arduino)
Features:   - Turn the aquarium light on and off at set times using a relay
            - Rotate a servo-driven feeder twice a day
            - Keep accurate time with a DS3231 real-time clock
            - Read water temperature from a DS18B20 probe and show it on an OLED
            - Feed once manually with a push button
Tech stack: Arduino Nano, Arduino C++, RTClib, Servo library, OneWire, Adafruit SSD1306
```

---

## Example 850

**Intent:**
vacation request approval in slack

**Spec:**
```
Type:       Slack app (approval workflow)
Auth:       Slack workspace OAuth; user identity from Slack
Data model: Employee(slack_user_id, name, manager_slack_id, days_remaining)
            TimeOffRequest(id, employee_id -> Employee, start_date, end_date, status, created_at)
Features:   - Open a request form with a /timeoff slash command
            - Send the manager a message with Approve and Reject buttons
            - Update the employee's remaining days when a request is approved
            - Post approved time off to a team channel
            - Show remaining days with a /timeoff balance command
API:        REST
            POST /slack/commands
            POST /slack/interactions
Storage:    PostgreSQL
Tech stack: Python, Slack Bolt, Block Kit, PostgreSQL
```

---

## Example 851

**Intent:**
We run about 40 Linux VMs and want to get alerted when disks are close to full, services crash or backups did not run last night. We already use Prometheus a bit, so please build on that.

**Spec:**
```
Type:       Monitoring and alerting setup
Features:   - Collect filesystem and systemd service metrics from every VM
            - Alert when a disk is above 85 percent or will fill within 24 hours
            - Alert when a monitored systemd service is not active
            - Alert when the last successful backup is older than 26 hours
            - Group and route alerts to email and a Teams channel
            - Show disk, service and backup status per VM on a dashboard
Storage:    Prometheus time-series database
Tech stack: Prometheus, node_exporter (textfile collector for backup timestamps), Alertmanager, Grafana
```

---

## Example 852

**Intent:**
ticket system for a hotel so guests can report broken things and housekeeping fixes it

**Spec:**
```
Type:       Web application (hotel maintenance requests)
Auth:       Staff login (PIN on shared tablets), roles: front desk, housekeeping, maintenance
Data model: Room(id, number, floor)
            Issue(id, room_id -> Room, category, description, priority, status, reported_by, created_at)
            StaffMember(id, name, department, pin_hash)
Features:   - Let guests report an issue by scanning a QR code in their room
            - Route issues to housekeeping or maintenance by category
            - Show staff a mobile list of open issues sorted by priority and floor
            - Mark an issue as fixed with a photo
            - Show average time to fix per category
API:        REST
            POST /rooms/{number}/issues
            GET  /issues?department={dept}&status=open
            POST /issues/{id}/resolve
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, FastAPI, Vue.js, Quasar
```

---

## Example 853

**Intent:**
air quality monitor for my kids bedroom, co2 and pm2.5, want a light that goes red when its bad

**Spec:**
```
Type:       IoT air quality monitor
Data model: AirReading(room, co2_ppm, pm25_ugm3, temperature_c, humidity_percent, recorded_at)
Features:   - Read CO2 from an SCD40 sensor and PM2.5 from a PMS5003 sensor every minute
            - Set an RGB LED to green, amber or red based on CO2 and PM2.5 thresholds
            - Show the current values on a small e-paper display
            - Send readings to Home Assistant for history charts
            - Notify a parent's phone when CO2 stays above 1200 ppm for 20 minutes
Tech stack: ESP32-C3, ESPHome (SCD4x, PMSX003, light components), Home Assistant
```

---

## Example 854

**Intent:**
customer feedback inbox for a product team

**Spec:**
```
Type:       Web application (feedback management)
Auth:       Team login (Google SSO)
Data model: Feedback(id, source, customer_email, text, sentiment, created_at)
            Tag(id, name)
            FeedbackTag(feedback_id -> Feedback, tag_id -> Tag)
            FeatureRequest(id, title, status, vote_count)
Features:   - Collect feedback from an in-app widget, email and Intercom
            - Tag feedback and link it to feature requests
            - Detect sentiment of each message automatically
            - Rank feature requests by number of linked customers
            - Notify customers when a request they asked for is shipped
API:        REST
            POST /feedback
            GET  /feedback?tag={tag}&source={source}
            POST /feedback/{id}/link
            GET  /feature-requests?sort=votes
Storage:    PostgreSQL
Tech stack: TypeScript, Remix, Prisma, Intercom webhooks, LLM API (sentiment)
```

---

## Example 855

**Intent:**
please help, we are dental clinic and want screen in waiting room show patient queue number and which doctor room to go

**Spec:**
```
Type:       Web application (queue management display)
Auth:       Receptionist and doctor login (username + password)
Data model: Doctor(id, name, room_number)
            QueueTicket(id, number, doctor_id -> Doctor, status, created_at, called_at)
Features:   - Issue a queue number to a patient at reception for a chosen doctor
            - Let the doctor call the next patient with one button
            - Show the called number and room on a waiting room TV
            - Play a chime and announce the number when it is called
            - Reset the queue numbers every morning
API:        REST + WebSocket
            POST /tickets
            POST /doctors/{id}/call-next
            GET  /queue
            WS   /display
Storage:    SQLite
Tech stack: Node.js, Express, Socket.IO, HTML/CSS/JavaScript (TV display), Web Speech API
```

---

## Example 856

**Intent:**
uptime kuma style thing but in python for checking our internal apis and databases

**Spec:**
```
Type:       Monitoring service (health checks)
Auth:       Login for the ops team (username + password)
Data model: Target(id, name, kind, connection_string, interval_seconds, timeout_seconds)
            CheckResult(id, target_id -> Target, ok, latency_ms, error, checked_at)
Features:   - Check HTTP endpoints, TCP ports, PostgreSQL and Redis connections
            - Run each check on its own interval in the background
            - Show a status grid with the latest result and latency per target
            - Alert a Slack channel when a target fails twice in a row and when it recovers
            - Show a 7-day latency chart for each target
API:        REST
            GET  /targets
            POST /targets
            GET  /targets/{id}/results?since={time}
Storage:    SQLite
Tech stack: Python, FastAPI, APScheduler, asyncpg, redis-py, Jinja2, Chart.js
```

---

## Example 857

**Intent:**
I manage a co-working space and want members to book hot desks and see a floor map of which desks are taken today

**Spec:**
```
Type:       Web application (desk booking)
Auth:       Member login (email magic link), admin role for staff
Data model: Member(id, name, email, plan)
            Desk(id, label, zone, x, y, has_monitor)
            Booking(id, desk_id -> Desk, member_id -> Member, date)
Features:   - Show an interactive floor map with free and booked desks for a chosen day
            - Book a desk for a full day with one click
            - Limit bookings per member based on their plan
            - Cancel a booking up to the morning of the day
            - Show staff a daily occupancy report
API:        REST
            GET  /desks?date={date}
            POST /bookings
            DELETE /bookings/{id}
            GET  /reports/occupancy?from={date}&to={date}
Storage:    PostgreSQL
Tech stack: TypeScript, SvelteKit, Drizzle ORM, SVG floor plan
```

---

## Example 858

**Intent:**
energy dashboard for 3 office buildings using our smart meters

**Spec:**
```
Type:       Energy monitoring dashboard
Auth:       Facilities team login (Microsoft SSO)
Data model: Building(id, name, floor_area_m2)
            Meter(id, building_id -> Building, type, modbus_address)
            MeterReading(meter_id -> Meter, kwh, kw, recorded_at)
Features:   - Read electricity, gas and water meters over Modbus every 15 minutes
            - Show consumption per building per day, week and month
            - Normalise usage by floor area to compare buildings
            - Detect unusual night-time consumption and flag it
            - Export monthly totals for carbon reporting
Storage:    TimescaleDB
Tech stack: Node-RED (Modbus collection), TimescaleDB, Grafana, Azure AD SSO
```

---

## Example 859

**Intent:**
a vue frontend for managing product returns in our webshop warehouse, scan the return label, check the item condition and decide refund or replace

**Spec:**
```
Type:       Web application (returns processing)
Auth:       Warehouse staff login (email + password)
Data model: ReturnRequest(id, order_id, customer_email, reason, status, created_at)
            ReturnItem(id, return_id -> ReturnRequest, sku, quantity, condition, decision)
            Inspection(id, return_item_id -> ReturnItem, inspector, notes, photo_url, inspected_at)
Features:   - Find a return by scanning the barcode on its return label
            - Record each item's condition with notes and photos
            - Choose refund, replace or reject for each item
            - Put resellable items back into stock automatically
            - Trigger the refund in the shop platform when the decision is refund
API:        REST
            GET  /returns/by-label/{code}
            POST /returns/{id}/items/{item_id}/inspection
            POST /returns/{id}/complete
Storage:    PostgreSQL, S3 (photos)
Tech stack: Vue.js 3, Pinia, Python, FastAPI, Shopify Admin API
```

---

## Example 860

**Intent:**
motion sensor camera for my backyard that sends pics to telegram

**Spec:**
```
Type:       IoT camera (security)
Features:   - Detect motion with a PIR sensor
            - Take a photo with the camera module when motion is detected
            - Send the photo to a Telegram chat with the time
            - Ignore repeated triggers within 60 seconds
            - Arm and disarm the camera with a Telegram command
API:        REST
            POST /bot{token}/sendPhoto
            GET  /bot{token}/getUpdates
Tech stack: ESP32-CAM, Arduino C++ (esp_camera, UniversalTelegramBot), PIR sensor HC-SR501
```

---

## Example 861

**Intent:**
lab equipment booking

**Spec:**
```
Type:       Web application (resource booking)
Auth:       University SSO (SAML), roles: researcher, lab manager
Data model: Equipment(id, name, location, requires_training)
            Training(id, user_id, equipment_id -> Equipment, certified_at)
            Booking(id, equipment_id -> Equipment, user_id, start_at, end_at, purpose)
Features:   - Show each instrument's calendar of bookings
            - Book an instrument for a time slot without overlapping others
            - Block bookings from users not trained on that instrument
            - Let the lab manager mark an instrument as out of service
            - Report usage hours per research group for billing
API:        REST
            GET  /equipment/{id}/bookings?week={date}
            POST /bookings
            DELETE /bookings/{id}
            GET  /reports/usage?month={yyyy-mm}
Storage:    PostgreSQL
Tech stack: Python, Django, FullCalendar, django-saml2-auth
```

---

## Example 862

**Intent:**
We need an alerting pipeline for our cloud costs: pull daily spend from AWS, compare it with the budget per team and the average of the last two weeks, and send a Slack alert if a team spends 30% more than usual. Teams are identified by a cost allocation tag.

**Spec:**
```
Type:       Scheduled cost monitoring service
Data model: Team(id, name, tag_value, monthly_budget, slack_channel)
            DailyCost(team_id -> Team, date, service, amount_usd)
Features:   - Fetch yesterday's cost grouped by team tag and service from the Cost Explorer API
            - Compare each team's daily spend with its 14-day average
            - Send a Slack alert when a team spends 30 percent more than usual
            - Warn when month-to-date spend is on track to exceed the budget
            - Post a weekly cost summary per team
Storage:    PostgreSQL
Tech stack: Python, boto3 (Cost Explorer), AWS Lambda, EventBridge schedule, Slack webhooks
```

---

## Example 863

**Intent:**
i have a bunch of tasmota plugs and want to see all of them in one dashboard with how much power each uses

**Spec:**
```
Type:       Smart home energy dashboard
Data model: PlugReading(plug, power_w, today_kwh, voltage, recorded_at)
Features:   - Subscribe to telemetry from all Tasmota plugs over MQTT
            - Show each plug's current power and on/off state on one page
            - Switch a plug on or off from the dashboard
            - Show daily kWh per plug as a stacked bar chart
            - Rank plugs by energy used this month
API:        MQTT
            SUB  tele/+/SENSOR
            SUB  stat/+/POWER
            PUB  cmnd/{plug}/POWER
Storage:    InfluxDB
Tech stack: Tasmota firmware, Mosquitto, Telegraf (MQTT consumer), InfluxDB, Grafana
```

---

## Example 864

**Intent:**
fix request system for school IT

**Spec:**
```
Type:       Web application (helpdesk)
Auth:       Google Workspace for Education login, roles: teacher, technician
Data model: Device(id, asset_tag, type, room)
            Request(id, device_id -> Device, teacher_email, problem, status, technician_email, created_at)
Features:   - Let teachers report a problem with a device in their classroom
            - Pick the device from a list filtered by room
            - Assign requests to a technician and update status
            - Email the teacher when the request is resolved
            - Show devices with the most repeated problems
API:        REST
            POST /requests
            GET  /requests?status={status}
            PATCH /requests/{id}
            GET  /devices?room={room}
Storage:    Google Sheets
Tech stack: Google Apps Script, Google Forms, Google Sheets
```

---

## Example 865

**Intent:**
small dashboard to see sign ups, active users and churn for my saas, data is in postgres

**Spec:**
```
Type:       KPI dashboard (SaaS metrics)
Auth:       Single admin login (Metabase account)
Data model: User(id, email, created_at)
            Subscription(id, user_id -> User, plan, mrr, started_at, cancelled_at)
            Event(id, user_id -> User, name, created_at)
Features:   - Show daily and weekly sign-ups
            - Show daily, weekly and monthly active users
            - Calculate monthly churn rate and MRR churn
            - Show MRR growth by new, expansion and churned revenue
            - Email a weekly summary to the founders
Storage:    Existing PostgreSQL database (read-only replica)
Tech stack: Metabase, PostgreSQL SQL questions
```

---

## Example 866

**Intent:**
Me and my brother have a small farm, we want know the soil moisture in different fields and control irrigation valves from phone, fields are far, maybe 2 km.

**Spec:**
```
Type:       IoT irrigation system (long range)
Data model: Field(id, name, valve_node_id, target_moisture_percent)
            SoilReading(field_id -> Field, moisture_percent, soil_temp_c, recorded_at)
            ValveEvent(id, field_id -> Field, action, source, created_at)
Features:   - Measure soil moisture and temperature in each field with battery sensor nodes
            - Send readings to a gateway at the house over LoRa
            - Open and close solenoid valves on command from the phone
            - Close a valve automatically after a set watering time
            - Show moisture per field on a phone dashboard
API:        MQTT
            SUB  farm/+/soil
            PUB  farm/{field}/valve/set
            SUB  farm/+/valve/state
Storage:    InfluxDB
Tech stack: LILYGO LoRa32 (ESP32 + SX1276), Arduino C++ (RadioLib), Raspberry Pi gateway, Mosquitto, Node-RED Dashboard
```

---

## Example 867

**Intent:**
on-call schedule thing so we know whos on call this week and it rotates automatically

**Spec:**
```
Type:       Web application (on-call scheduling)
Auth:       Team login (GitHub OAuth)
Data model: Engineer(id, name, email, phone, slack_id)
            Rotation(id, name, handoff_weekday, handoff_time)
            RotationMember(rotation_id -> Rotation, engineer_id -> Engineer, position)
            Override(id, rotation_id -> Rotation, engineer_id -> Engineer, start_at, end_at)
Features:   - Rotate the on-call engineer automatically every week
            - Let engineers create overrides for holidays and swaps
            - Show the current and next on-call engineer
            - Update the Slack user group @oncall at each handoff
            - Export the schedule as an iCal feed
API:        REST
            GET  /rotations/{id}/current
            POST /rotations/{id}/overrides
            GET  /rotations/{id}/calendar.ics
Storage:    PostgreSQL
Tech stack: Go, Gin, React, Slack Web API
```

---

## Example 868

**Intent:**
build a fleet dashboard for our electric scooters showing battery level and location

**Spec:**
```
Type:       Fleet management dashboard
Auth:       Operations staff login (email + password)
Data model: Scooter(id, serial, status, firmware_version)
            Telemetry(scooter_id -> Scooter, lat, lng, battery_percent, speed_kmh, locked, recorded_at)
            Task(id, scooter_id -> Scooter, type, assigned_to, status, created_at)
Features:   - Show every scooter on a map coloured by battery level
            - List scooters below 20 percent battery for the charging crew
            - Create swap, repair and relocate tasks for field staff
            - Lock a scooter remotely
            - Flag scooters that have not reported for 2 hours
API:        REST + WebSocket
            GET  /scooters?battery_below={pct}
            POST /scooters/{id}/lock
            POST /tasks
            WS   /telemetry/live
Storage:    PostgreSQL with PostGIS, Redis (latest positions)
Tech stack: Kotlin, Spring Boot, Angular, Mapbox GL JS
```

---

## Example 869

**Intent:**
nursing home want call button for residents, when they press it nurse get alert on phone with room number

**Spec:**
```
Type:       IoT alert system (nurse call)
Data model: Room(id, number, resident_name, button_id)
            Call(id, room_id -> Room, pressed_at, acknowledged_at, acknowledged_by)
Features:   - Send a call when a resident presses a wireless button in their room
            - Push an alert with the room number to all nurses on shift
            - Let a nurse acknowledge the call so others see it is handled
            - Escalate to the head nurse if not acknowledged within 3 minutes
            - Report response times per shift
API:        MQTT
            SUB  nursecall/+/button
            PUB  nursecall/alerts
Storage:    PostgreSQL
Tech stack: Zigbee buttons, Zigbee2MQTT, Mosquitto, Python, FastAPI, Firebase Cloud Messaging, Flutter
```

---

## Example 870

**Intent:**
build me a laravel admin for managing the courses, teachers and student enrollments at our language school

**Spec:**
```
Type:       Web application (admin panel)
Auth:       Staff login (email + password), roles: admin, teacher
Data model: Teacher(id, name, email, languages)
            Course(id, language, level, teacher_id -> Teacher, start_date, end_date, capacity, price)
            Student(id, name, email, phone)
            Enrollment(id, course_id -> Course, student_id -> Student, paid, enrolled_at)
Features:   - Create courses with level, teacher, dates and capacity
            - Enroll students and block enrollment when a course is full
            - Track which enrollments are paid
            - Let teachers see only their own courses and student lists
            - Export a class list as PDF
Storage:    MySQL
Tech stack: PHP, Laravel, Filament admin panel, DomPDF
```

---

## Example 871

**Intent:**
alert me when my sump pump runs too often

**Spec:**
```
Type:       IoT monitoring (basement)
Features:   - Detect each pump run by measuring current with a CT clamp
            - Count pump cycles per hour
            - Detect high water with a float switch as a backup
            - Notify my phone when cycles per hour exceed a limit or water is high
            - Keep running on a small UPS during a power cut
API:        MQTT
            PUB  basement/sump/running
            PUB  basement/sump/high_water
Tech stack: ESP32, ESPHome (ct_clamp, binary_sensor), Home Assistant, Mosquitto
```

---

## Example 872

**Intent:**
The finance team keeps asking engineering for the same numbers. I want a self-serve internal dashboard with monthly revenue by region, outstanding invoices older than 60 days, and top 20 customers by revenue, pulled from our ERP's SQL Server database. Only finance should be able to see it.

**Spec:**
```
Type:       Internal reporting dashboard (finance)
Auth:       Microsoft Entra ID SSO, restricted to the finance security group
Data model: Invoice(id, customer_id -> Customer, region, amount, issued_at, due_at, paid_at)
            Customer(id, name, region, segment)
Features:   - Show monthly revenue by region for the current and previous year
            - List unpaid invoices older than 60 days with customer and amount
            - Rank the top 20 customers by revenue for a chosen period
            - Filter every page by region and date range
            - Refresh the data every night from the ERP database
Storage:    SQL Server (ERP, read-only), Power BI dataset
Tech stack: Power BI, Power BI gateway, SQL Server views
```

---

## Example 873

**Intent:**
track job progress for our print shop orders from design to delivery

**Spec:**
```
Type:       Web application (job tracking)
Auth:       Staff login (email + password)
Data model: Customer(id, name, email, phone)
            Job(id, customer_id -> Customer, title, quantity, material, stage, due_date)
            StageChange(id, job_id -> Job, stage, changed_by, changed_at)
Features:   - Create jobs with material, quantity and due date
            - Move jobs through stages: design, proof, printing, finishing, ready, delivered
            - Show a board of jobs per stage sorted by due date
            - Email the customer when the job is ready for pickup
            - Highlight jobs at risk of missing their due date
API:        REST
            GET  /jobs?stage={stage}
            POST /jobs
            POST /jobs/{id}/stage
Storage:    PostgreSQL
Tech stack: JavaScript, Express, React, react-beautiful-dnd, Nodemailer
```

---

## Example 874

**Intent:**
a little weather station on my roof with micropython

**Spec:**
```
Type:       IoT weather station
Data model: WeatherReading(temperature_c, humidity_percent, pressure_hpa, wind_kmh, rain_mm, recorded_at)
Features:   - Read temperature, humidity and pressure from a BME280 sensor
            - Count anemometer and rain gauge pulses with interrupts
            - Calculate wind speed and rainfall every 5 minutes
            - Publish readings to MQTT over Wi-Fi
            - Show current conditions and 7-day history on a dashboard
API:        MQTT
            PUB  weather/roof/readings
Storage:    InfluxDB
Tech stack: Raspberry Pi Pico W, MicroPython (umqtt.simple, bme280 driver), Mosquitto, InfluxDB, Grafana
```

---

## Example 875

**Intent:**
whatsapp bot for field technicans to log site visits and photos insted of paper forms

**Spec:**
```
Type:       Chatbot (field service reporting)
Auth:       Technicians identified by registered WhatsApp phone number
Data model: Technician(id, name, phone)
            Site(id, code, name, address)
            Visit(id, technician_id -> Technician, site_id -> Site, work_done, started_at, finished_at)
            VisitPhoto(id, visit_id -> Visit, url)
Features:   - Start a visit by sending the site code to the bot
            - Ask step-by-step questions about the work done
            - Save photos sent in the chat to the visit
            - Generate a PDF visit report and email it to the office
            - Show office staff a list of visits per site
API:        REST
            POST /webhooks/whatsapp
            GET  /visits?site={code}
            GET  /visits/{id}/report.pdf
Storage:    PostgreSQL, S3 (photos and reports)
Tech stack: Python, FastAPI, WhatsApp Cloud API, WeasyPrint
```

---

## Example 876

**Intent:**
canary checks for our login flow every 5 min

**Spec:**
```
Type:       Synthetic monitoring script
Features:   - Open the login page in a headless browser every 5 minutes
            - Log in with a dedicated test account and check the dashboard loads
            - Record the time taken for each step
            - Save a screenshot when a step fails
            - Alert PagerDuty after two failed runs in a row
Input:      Test account credentials from environment variables
Storage:    S3 (failure screenshots)
Tech stack: TypeScript, Playwright, GitHub Actions (scheduled workflow), PagerDuty Events API
```

---

## Example 877

**Intent:**
tool for our recruiters to track candidates through interview stages

**Spec:**
```
Type:       Web application (applicant tracking)
Auth:       Recruiter and hiring manager login (Google SSO)
Data model: Job(id, title, department, status)
            Candidate(id, name, email, cv_url, source)
            Application(id, job_id -> Job, candidate_id -> Candidate, stage, applied_at)
            Feedback(id, application_id -> Application, interviewer_email, score, notes)
Features:   - Post jobs and receive applications with a CV upload
            - Move candidates through stages on a kanban board per job
            - Collect structured feedback and scores from interviewers
            - Schedule interviews with Google Calendar invites
            - Show time-to-hire and conversion rate per stage
API:        REST
            POST /jobs/{id}/applications
            PATCH /applications/{id}
            POST /applications/{id}/feedback
            GET  /reports/funnel?job={id}
Storage:    PostgreSQL, Google Cloud Storage (CVs)
Tech stack: TypeScript, Next.js, tRPC, Prisma, Google Calendar API
```

---

## Example 878

**Intent:**
Our pharmacy keeps throwing away expired medicine because nobody notices the dates. I want a stock system where we scan the barcode and enter the batch number and expiry date when a delivery arrives, and every Monday it lists what expires in the next 90 days so we can sell or return it first.

**Spec:**
```
Type:       Web application (pharmacy stock and expiry tracking)
Auth:       Staff login (username + password), roles: pharmacist, assistant
Data model: Product(id, gtin, name, form, strength)
            Batch(id, product_id -> Product, batch_number, expiry_date, quantity, received_at)
            Dispense(id, batch_id -> Batch, quantity, dispensed_at)
Features:   - Scan a product barcode and record batch number, expiry date and quantity on delivery
            - Dispense from the batch with the earliest expiry first
            - List batches expiring in the next 90 days every Monday by email
            - Highlight expired batches that must be removed from shelves
            - Show the value of stock written off per month
API:        REST
            POST /deliveries
            POST /dispenses
            GET  /batches/expiring?days={n}
            GET  /reports/write-offs?month={yyyy-mm}
Storage:    PostgreSQL
Tech stack: Python, Django, Django admin, Celery beat, html5-qrcode
```

---

## Example 879

**Intent:**
parkign sensors for our office car park so ppl can see free spots before they drive in

**Spec:**
```
Type:       IoT parking availability system
Data model: Spot(id, label, level, sensor_id)
            SpotEvent(spot_id -> Spot, occupied, recorded_at)
Features:   - Detect a car in each spot with a magnetometer sensor node
            - Send occupancy changes over LoRaWAN
            - Show a live map of free and taken spots per level
            - Show the number of free spots on a display at the entrance
            - Report average occupancy per hour of the day
API:        REST + WebSocket
            GET  /levels/{id}/spots
            GET  /stats/occupancy?date={date}
            WS   /spots/live
Storage:    PostgreSQL
Tech stack: LoRaWAN magnetometer sensors, ChirpStack, Node.js, Express, React
```

---

## Example 880

**Intent:**
alert on errors in app logs

**Spec:**
```
Type:       Log monitoring and alerting setup
Features:   - Ship application logs from every server to a central store
            - Parse log level, service name and request ID from each line
            - Alert when error lines per service exceed a threshold in 5 minutes
            - Send alerts to Slack with a link to the matching log lines
            - Search logs by service, level and time range
Storage:    Grafana Loki (S3 backend)
Tech stack: Promtail, Grafana Loki, Grafana (alerting and Explore)
```

---

## Example 881

**Intent:**
we own 30 vending machines around the city and want know which one is empty or broken without driving to all of them

**Spec:**
```
Type:       IoT telemetry system with web dashboard
Auth:       Operator login (email + password)
Data model: Machine(id, location_name, lat, lng)
            Slot(id, machine_id -> Machine, product, capacity, stock_level)
            Sale(id, slot_id -> Slot, price, sold_at)
            Fault(id, machine_id -> Machine, code, started_at, cleared_at)
Features:   - Report each sale and fault from the machine's controller over 4G
            - Track remaining stock per slot after every sale
            - Show machines on a map coloured by stock level and fault state
            - Build a refill route listing machines below 30 percent stock
            - Show sales per machine per day
API:        MQTT
            PUB  vending/{machine_id}/sale
            PUB  vending/{machine_id}/fault
            PUB  vending/{machine_id}/heartbeat
Storage:    PostgreSQL
Tech stack: ESP32 with SIM7080G (MDB interface board), ESP-IDF, EMQX, Python, Django, Leaflet
```

---

## Example 882

**Intent:**
ticket scanning at the door for our events

**Spec:**
```
Type:       Mobile web application (event check-in)
Auth:       Door staff login with an event access code
Data model: Event(id, name, starts_at, venue)
            Ticket(id, event_id -> Event, code, holder_name, type, checked_in_at)
Features:   - Scan ticket QR codes with the phone camera
            - Show a green or red screen for valid, invalid or already used tickets
            - Search a ticket by holder name when the QR code is missing
            - Work offline with a downloaded ticket list and sync later
            - Show live check-in counts per ticket type
API:        REST
            GET  /events/{id}/tickets
            POST /tickets/{code}/check-in
            GET  /events/{id}/stats
Storage:    PostgreSQL (server), IndexedDB (offline on device)
Tech stack: TypeScript, Ionic, Angular, NestJS
```

---

## Example 883

**Intent:**
performance review tool where employees do self review then manager writes feedback, twice a year

**Spec:**
```
Type:       Web application (performance reviews)
Auth:       Company SSO (Okta), roles: employee, manager, HR admin
Data model: Employee(id, name, email, manager_id -> Employee)
            ReviewCycle(id, name, opens_at, closes_at)
            Review(id, cycle_id -> ReviewCycle, employee_id -> Employee, self_text, manager_text, rating, status)
Features:   - Open a review cycle for all employees with deadlines
            - Let employees write a self review against set questions
            - Let managers write feedback and a rating after the self review is done
            - Remind people by email when their part is overdue
            - Show HR completion progress per department
            - Export completed reviews as PDF
API:        REST
            POST /cycles
            GET  /me/reviews
            PUT  /reviews/{id}/self
            PUT  /reviews/{id}/manager
            GET  /cycles/{id}/progress
Storage:    PostgreSQL
Tech stack: Python, Django, React, WeasyPrint
```

---

## Example 884

**Intent:**
automatic chicken coop door that opens at sunrise and closes at sunset

**Spec:**
```
Type:       Embedded automation (Arduino)
Features:   - Calculate sunrise and sunset times from the date and location
            - Drive a linear actuator to open and close the door
            - Stop the motor using top and bottom limit switches
            - Close the door 20 minutes after sunset so the hens get in
            - Run from a 12 V battery charged by a solar panel
Tech stack: Arduino Nano, Arduino C++, DS3231 RTC, Dusk2Dawn library, L298N motor driver
```

---

## Example 885

**Intent:**
I have a cabin in the mountains with no internet, just mobile signal. Can I get an SMS if the power goes out or the temperature drops below freezing so the pipes don't burst?

**Spec:**
```
Type:       IoT remote alarm (GSM)
Features:   - Detect mains power loss with a voltage sensing module
            - Run from a backup battery when mains power is lost
            - Read indoor temperature from a DS18B20 sensor every 5 minutes
            - Send an SMS when power fails, returns, or temperature drops below 2 °C
            - Reply with the current status when an SMS "STATUS" is received
Tech stack: Arduino Uno, SIM800L GSM module, Arduino C++ (TinyGSM, DallasTemperature)
```

---

## Example 886

**Intent:**
kitchen display screen for restaurant so cooks see orders from the pos

**Spec:**
```
Type:       Web application (kitchen display system)
Auth:       Device pairing code per kitchen screen
Data model: Order(id, table_number, source, status, created_at)
            OrderItem(id, order_id -> Order, name, quantity, modifiers, station, status)
Features:   - Receive new orders from the POS by webhook
            - Show orders as tickets per station (grill, fry, cold)
            - Mark items and orders as done with a tap
            - Colour tickets yellow and red as they get older
            - Show the average ticket time for the current service
API:        REST + WebSocket
            POST /webhooks/pos/orders
            POST /orders/{id}/bump
            WS   /stations/{station}/live
Storage:    Redis (open orders), PostgreSQL (history)
Tech stack: Node.js, Fastify, Socket.IO, React, Square Orders API
```

---

## Example 887

**Intent:**
parents shuold see where the school bus is and get notifed when its 5 min away

**Spec:**
```
Type:       Mobile application with GPS tracking backend
Auth:       Parent login (phone number + SMS code); driver app login with a PIN
Data model: Bus(id, name, route_id -> Route)
            Route(id, name)
            Stop(id, route_id -> Route, name, lat, lng, order_index)
            Child(id, parent_id, stop_id -> Stop)
            BusPosition(bus_id -> Bus, lat, lng, recorded_at)
Features:   - Send the bus position every 10 seconds from the driver's phone
            - Show the bus on a live map to parents of children on that route
            - Estimate arrival time at each stop from the route and traffic
            - Notify parents when the bus is 5 minutes from their child's stop
            - Hide the bus location outside school run hours
API:        REST + WebSocket
            POST /buses/{id}/positions
            GET  /me/stop/eta
            WS   /buses/{id}/live
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Firebase Cloud Messaging, Node.js, Express, Google Maps Directions API
```

---

## Example 888

**Intent:**
timesheets for agency

**Spec:**
```
Type:       Web application (timesheets and billing)
Auth:       User login (email + password), roles: staff, project manager, admin
Data model: Client(id, name)
            Project(id, client_id -> Client, name, budget_hours, hourly_rate)
            TimeEntry(id, user_id, project_id -> Project, date, hours, description, billable)
Features:   - Log hours per project per day in a weekly grid
            - Start and stop a timer for the current task
            - Show hours used against budget for each project
            - Lock approved weeks so they cannot be edited
            - Export billable hours per client for invoicing
API:        REST
            GET  /time-entries?week={date}
            POST /time-entries
            GET  /projects/{id}/budget
            POST /weeks/{date}/approve
Storage:    PostgreSQL
Tech stack: Ruby on Rails, StimulusJS, Chartkick
```

---

## Example 889

**Intent:**
leak sensor under the sink that shuts off the water valve automatically

**Spec:**
```
Type:       IoT smart home (water leak protection)
Features:   - Detect water on the floor with leak probe contacts
            - Close a motorised ball valve on the main water line when a leak is detected
            - Sound a local buzzer and send a phone notification
            - Reopen the valve only with a manual reset or from the app
            - Exercise the valve once a month so it does not seize
API:        MQTT
            PUB  home/leak/kitchen
            SUB  home/water_valve/set
Tech stack: ESP32, ESPHome, motorised ball valve with relay, Home Assistant
```

---

## Example 890

**Intent:**
Our company has 25 cars and vans and we always miss service dates and MOT. I want to log mileage, see when each vehicle is due for service, inspection and insurance renewal, and get reminders. Drivers should be able to report damage with photos from their phone.

**Spec:**
```
Type:       Web application (fleet maintenance)
Auth:       Login (email + password), roles: fleet manager, driver
Data model: Vehicle(id, registration, make, model, mileage, mot_due, insurance_due, service_interval_km)
            ServiceRecord(id, vehicle_id -> Vehicle, date, mileage, work_done, cost)
            DamageReport(id, vehicle_id -> Vehicle, driver_id, description, photo_url, status, created_at)
Features:   - Record mileage updates from drivers
            - Calculate the next service due from mileage and service interval
            - Remind the fleet manager 30 days before MOT, insurance and service dates
            - Let drivers report damage with photos from their phone
            - Show maintenance cost per vehicle per year
API:        REST
            GET  /vehicles?due_within={days}
            POST /vehicles/{id}/mileage
            POST /vehicles/{id}/services
            POST /vehicles/{id}/damage-reports
Storage:    PostgreSQL, S3 (photos)
Tech stack: PHP, Laravel, Inertia.js, Vue.js
```

---

## Example 891

**Intent:**
heartbeat monitor for cron jobs, if a job doesnt ping in time alert me

**Spec:**
```
Type:       Monitoring service (cron job heartbeats)
Auth:       User login (email + password); each check has a secret ping URL
Data model: Check(id, name, ping_token, period_seconds, grace_seconds, last_ping_at, status)
            Ping(id, check_id -> Check, kind, received_at, source_ip)
Features:   - Give each job a unique URL to call when it finishes
            - Accept start and fail pings to measure job duration and failures
            - Mark a check as down when no ping arrives within period plus grace time
            - Alert by email and Slack when a check goes down and when it recovers
            - Show a timeline of recent pings per check
API:        REST
            GET  /ping/{token}
            GET  /ping/{token}/start
            GET  /ping/{token}/fail
            GET  /checks
            POST /checks
Storage:    PostgreSQL
Tech stack: Python, Django, Celery beat
```

---

## Example 892

**Intent:**
retool app for loan officers to review applications, see the documents and credit score, and approve or decline

**Spec:**
```
Type:       Internal tool (loan application review)
Auth:       Retool SSO, permission groups: loan officer, senior officer
Data model: Applicant(id, name, email, income)
            Application(id, applicant_id -> Applicant, amount, term_months, credit_score, status, assigned_to)
            Document(id, application_id -> Application, kind, file_url)
            Decision(id, application_id -> Application, officer_email, decision, reason, decided_at)
Features:   - Show a queue of applications assigned to the logged-in officer
            - Preview uploaded documents inside the app
            - Fetch the credit score from the credit bureau API on demand
            - Approve or decline with a required reason
            - Require a senior officer for amounts above a set limit
API:        REST
            POST /credit-reports
Storage:    PostgreSQL (applications and decisions), S3 (documents)
Tech stack: Retool, PostgreSQL resource, S3 resource, REST API resource (credit bureau)
```

---

## Example 893

**Intent:**
we have diesel generators at remote telecom sites, want to monitor fuel level and running hours

**Spec:**
```
Type:       IoT remote monitoring system
Auth:       Operations login (email + password)
Data model: Site(id, name, lat, lng, tank_capacity_l)
            GeneratorReading(site_id -> Site, fuel_level_percent, running, battery_v, run_hours, recorded_at)
Features:   - Read fuel level from a tank pressure sensor and running state from the generator controller
            - Send readings every 10 minutes over cellular
            - Calculate fuel consumption per running hour
            - Alert when fuel is below 25 percent or drops suddenly (possible theft)
            - Plan refuelling trips from sites sorted by days of fuel left
API:        MQTT
            PUB  sites/{site_id}/generator
Storage:    TimescaleDB
Tech stack: Teltonika RUT956 router (Modbus to MQTT), HiveMQ, Python, TimescaleDB, Grafana
```

---

## Example 894

**Intent:**
i want an angular dashbaord that shows how much my solar panels are producing vs what my house is using

**Spec:**
```
Type:       Energy monitoring dashboard (solar)
Data model: EnergySample(timestamp, pv_power_w, load_power_w, grid_power_w, battery_soc)
Features:   - Read inverter data from its local Modbus TCP interface every 30 seconds
            - Show live solar production, house load and grid import or export
            - Show daily production and self-consumption percentage
            - Compare this month's production with the same month last year
            - Estimate money saved from the electricity tariff
API:        REST + WebSocket
            GET  /energy/daily?from={date}&to={date}
            WS   /energy/live
Storage:    InfluxDB
Tech stack: Angular, ngx-charts, Python, pymodbus, FastAPI, InfluxDB
```

---

## Example 895

**Intent:**
warehouse cycle count app

**Spec:**
```
Type:       Mobile web application (inventory cycle counting)
Auth:       Warehouse staff login (badge number + PIN)
Data model: Location(id, code, zone)
            CountTask(id, location_id -> Location, assigned_to, status, due_date)
            CountLine(id, task_id -> CountTask, sku, expected_qty, counted_qty)
Features:   - Generate daily count tasks so every location is counted once a quarter
            - Scan the location and item barcodes and enter the counted quantity
            - Hide the expected quantity from the counter to avoid bias
            - Flag variances above a set percentage for a recount
            - Post approved adjustments back to the stock system
API:        REST
            GET  /me/count-tasks
            POST /count-tasks/{id}/lines
            POST /count-tasks/{id}/submit
            GET  /variances?status=pending
Storage:    PostgreSQL
Tech stack: TypeScript, Vue.js, Quasar (PWA), NestJS
```

---

## Example 896

**Intent:**
replace my old thermostat with a raspberry pi that controls the boiler and lets me set a schedule from my phone

**Spec:**
```
Type:       IoT smart thermostat (Raspberry Pi)
Auth:       Login with a password (single household user)
Data model: Schedule(id, weekday, start_time, target_temp_c)
            TempReading(temperature_c, boiler_on, recorded_at)
Features:   - Read room temperature from a DS18B20 sensor every 30 seconds
            - Switch the boiler on and off with a relay using hysteresis
            - Follow a weekly schedule of target temperatures
            - Override the target temperature for 2 hours from the phone
            - Show temperature and boiler run-time history
API:        REST
            GET  /status
            PUT  /schedule
            POST /override
            GET  /history?days={n}
Storage:    SQLite
Tech stack: Raspberry Pi 4, Python, gpiozero, w1thermsensor, FastAPI, React (mobile web UI)
```

---

## Example 897

**Intent:**
For our construction company we need to track safety certificates and trainings of all workers, like first aid, working at height and forklift license. Site managers must check on the phone if a worker is allowed for a task, and office should get warning before certificates expire.

**Spec:**
```
Type:       Web application (training and certification tracking)
Auth:       Login (email + password), roles: office admin, site manager
Data model: Worker(id, name, employee_number, company, photo_url)
            CertificateType(id, name, validity_months)
            Certificate(id, worker_id -> Worker, type_id -> CertificateType, issued_at, expires_at, file_url)
Features:   - Record certificates with issue date and a scanned copy
            - Calculate expiry dates from the certificate type
            - Let site managers scan a worker's QR badge to see valid certificates
            - Show a red warning when a required certificate is missing or expired
            - Email the office 60 days before a certificate expires
API:        REST
            GET  /workers/{id}/certificates
            POST /workers/{id}/certificates
            GET  /certificates/expiring?days={n}
Storage:    PostgreSQL, S3 (scanned certificates)
Tech stack: C#, ASP.NET Core, Blazor, Hangfire
```

---

## Example 898

**Intent:**
vibration monitoring on factory motors to catch bearing failures early, esp32 + accelerometer, mqtt

**Spec:**
```
Type:       IoT condition monitoring system
Data model: Motor(id, name, line, rated_rpm)
            VibrationReading(motor_id -> Motor, rms_g, peak_g, dominant_freq_hz, temperature_c, recorded_at)
Features:   - Sample an ADXL345 accelerometer at 3.2 kHz on each motor
            - Calculate RMS, peak and an FFT on the device every minute
            - Publish summary features to MQTT
            - Compare each motor with its own baseline and alert on rising vibration
            - Show trends per motor and the dominant frequency over time
API:        MQTT
            PUB  factory/{line}/{motor_id}/vibration
            SUB  factory/+/+/vibration
Storage:    TimescaleDB
Tech stack: ESP32, ESP-IDF (esp-dsp FFT), Mosquitto, Python consumer (paho-mqtt), TimescaleDB, Grafana
```

---

## Example 899

**Intent:**
temp controler for beer fermentation, fridge and heater, keep it at one temp

**Spec:**
```
Type:       Embedded temperature controller
Features:   - Read wort temperature from a waterproof DS18B20 probe
            - Switch a fridge and a heat mat through relays to hold the set temperature
            - Use a minimum off time to protect the fridge compressor
            - Ramp the set temperature over days for a fermentation profile
            - Log temperature to a web chart over Wi-Fi
API:        REST
            GET  /api/status
            POST /api/profile
Tech stack: ESP8266, Arduino C++ (OneWire, DallasTemperature, ESPAsyncWebServer), Chart.js
```

---

## Example 900

**Intent:**
feature flag admin panel for our backend

**Spec:**
```
Type:       Internal tool (feature flag management)
Auth:       Engineer login (GitHub OAuth, org members only)
Data model: Flag(id, key, description, enabled, rollout_percent, updated_at)
            FlagRule(id, flag_id -> Flag, attribute, operator, value)
            FlagAudit(id, flag_id -> Flag, changed_by, old_value, new_value, changed_at)
Features:   - Create flags with a key and description
            - Turn flags on or off per environment
            - Roll out a flag to a percentage of users
            - Target users by attributes such as country or plan
            - Keep an audit log of every flag change
API:        REST
            GET  /flags
            POST /flags
            PATCH /flags/{key}
            GET  /sdk/flags?env={env}
Storage:    PostgreSQL, Redis (cached flag config)
Tech stack: Go, React, TypeScript
```

---

## Example 901

**Intent:**
supplier purchase orders, we want to create PO, send to supplier and track when goods are delivered

**Spec:**
```
Type:       Web application (purchase order management)
Auth:       Staff login (email + password), roles: buyer, warehouse, admin
Data model: Supplier(id, name, email, payment_terms)
            PurchaseOrder(id, supplier_id -> Supplier, number, status, expected_date, total)
            PurchaseOrderLine(id, po_id -> PurchaseOrder, sku, quantity, unit_cost, received_quantity)
Features:   - Create purchase orders with lines, prices and expected delivery date
            - Email the PO to the supplier as a PDF
            - Record full or partial deliveries at the warehouse
            - Show overdue purchase orders by supplier
            - Report supplier on-time delivery rate
API:        REST
            POST /purchase-orders
            POST /purchase-orders/{id}/send
            POST /purchase-orders/{id}/receipts
            GET  /purchase-orders?status=overdue
Storage:    PostgreSQL
Tech stack: Python, Odoo (Purchase and Inventory modules)
```

---

## Example 902

**Intent:**
I run a small tuition centre and I want parents to be able to check their kid's attendance from their phone

**Spec:**
```
Type:       Web application (mobile-friendly, CRUD)
Auth:       Login for teachers (email + password); parents log in with phone number + OTP
Data model: Teacher(id, name, email, password_hash)
            Batch(id, name, subject, teacher_id -> Teacher)
            Student(id, name, parent_phone, batch_id -> Batch)
            Attendance(id, student_id -> Student, date, status)
Features:   - Mark present or absent for a whole batch in one screen
            - Show parents their child's attendance calendar for each month
            - Calculate the attendance percentage per student
            - Highlight students below 75% attendance for the teacher
            - Export monthly attendance as a CSV file
API:        REST
            POST /auth/otp
            POST /auth/verify
            GET  /batches/{id}/students
            POST /attendance
            GET  /students/{id}/attendance?month={yyyy-mm}
Storage:    PostgreSQL
Tech stack: Python, Django, Django REST Framework, HTML/CSS (responsive), MSG91 (OTP SMS)
```

---

## Example 903

**Intent:**
school homework app

**Spec:**
```
Type:       Mobile application
Auth:       Login for teachers and students (school-issued username + password)
Data model: User(id, name, role, class_id -> Class, password_hash)
            Class(id, grade, section)
            Homework(id, class_id -> Class, subject, title, description, due_date, attachment_url)
            Submission(id, homework_id -> Homework, student_id -> User, file_url, submitted_at, grade)
Features:   - Post homework with a due date and optional attachment for a class
            - Show students their pending and completed homework
            - Upload a photo or PDF of finished homework
            - Grade submissions and add a short comment
            - Send a push notification the day before homework is due
API:        REST
            GET  /classes/{id}/homework
            POST /homework
            POST /homework/{id}/submissions
            PUT  /submissions/{id}/grade
Storage:    Firebase Firestore (data), Firebase Storage (files)
Tech stack: Flutter, Firebase Auth, Firebase Cloud Messaging
```

---

## Example 904

**Intent:**
Kindly make one website for my clinic where patients can book appointment with doctor and they will get SMS reminder before the time

**Spec:**
```
Type:       Web application (booking system)
Auth:       Admin login for clinic staff (email + password); patients book without an account using phone number
Data model: Doctor(id, name, specialisation, slot_minutes)
            Schedule(id, doctor_id -> Doctor, weekday, start_time, end_time)
            Patient(id, name, phone, age)
            Appointment(id, doctor_id -> Doctor, patient_id -> Patient, starts_at, status)
Features:   - Show available time slots for each doctor by date
            - Book an appointment with patient name, phone and age
            - Send an SMS confirmation right after booking
            - Send an SMS reminder 2 hours before the appointment
            - Let staff view, reschedule or cancel the day's appointments
            - Block slots when a doctor is on leave
API:        REST
            GET  /doctors
            GET  /doctors/{id}/slots?date={date}
            POST /appointments
            PATCH /appointments/{id}
Storage:    MySQL
Tech stack: PHP, Laravel, Blade templates, Laravel Scheduler, Twilio SMS API
```

---

## Example 905

**Intent:**
i wnat a menu for my resturant that people open by scanning qr code on teh table and order from there

**Spec:**
```
Type:       Web application (QR ordering)
Auth:       Staff login for kitchen and admin (email + password); customers order without login
Data model: Table(id, number, qr_token)
            Category(id, name, sort_order)
            MenuItem(id, category_id -> Category, name, price, description, photo_url, is_available)
            Order(id, table_id -> Table, status, total, created_at)
            OrderItem(id, order_id -> Order, menu_item_id -> MenuItem, quantity, notes)
Features:   - Open the menu for the right table from a unique QR code
            - Browse items by category with photos and prices
            - Add items to a cart and place an order with special notes
            - Show new orders live on a kitchen screen
            - Update order status (received, cooking, served)
            - Hide items that are sold out
            - Generate printable QR codes for each table
API:        REST + WebSocket
            GET  /menu
            POST /tables/{token}/orders
            PATCH /orders/{id}/status
            WS   /kitchen/orders
Storage:    PostgreSQL
Tech stack: Next.js, Node.js, Prisma, Socket.IO, qrcode library
```

---

## Example 906

**Intent:**
My sister is getting married in March and we have around 300 guests spread across India and the UK. We want a simple wedding website where guests can see the events (mehendi, sangeet, wedding), RSVP for each one separately and tell us about food preferences. It would be great if we could download the final list for the caterer.

**Spec:**
```
Type:       Web application (event RSVP)
Auth:       Guests open a personal invite link (unique code); couple logs in as admin with password
Data model: Event(id, name, date, venue, address, map_url)
            Guest(id, name, email, phone, invite_code, party_size_allowed)
            Rsvp(id, guest_id -> Guest, event_id -> Event, attending, headcount, meal_preference, updated_at)
Features:   - Show event details, venues and maps on the homepage
            - Let each guest RSVP to each event separately with headcount
            - Collect meal preference (veg, non-veg, Jain, vegan) per RSVP
            - Show admin a live count of attendees per event
            - Export the guest list per event to Excel for the caterer
            - Send reminder emails to guests who have not replied
API:        REST
            GET  /invite/{code}
            POST /invite/{code}/rsvp
            GET  /admin/events/{id}/rsvps
            GET  /admin/export?event_id={id}
Storage:    Supabase (PostgreSQL)
Tech stack: Next.js, Supabase, Resend (email), SheetJS (Excel export)
```

---

## Example 907

**Intent:**
gym membership tracker

**Spec:**
```
Type:       Web application (CRUD)
Auth:       Login for gym owner and front-desk staff (email + password, role-based)
Data model: Member(id, name, phone, photo_url, joined_on)
            Plan(id, name, duration_days, price)
            Membership(id, member_id -> Member, plan_id -> Plan, start_date, end_date, amount_paid)
            CheckIn(id, member_id -> Member, checked_in_at)
Features:   - Add members and assign a membership plan
            - Record payments and renewals
            - Show memberships expiring in the next 7 days
            - Log daily check-ins at the front desk
            - Show monthly revenue and active member count
API:        REST
            GET  /members
            POST /members
            POST /memberships
            POST /checkins
            GET  /reports/expiring
Storage:    PostgreSQL
Tech stack: Python, Django, Bootstrap
```

---

## Example 908

**Intent:**
Can you set up a donation page for our church on WordPress so people can give online, including monthly giving?

**Spec:**
```
Type:       Website (WordPress donations)
Auth:       Optional donor accounts to view giving history; WordPress admin login for church staff
Data model: Donor(id, name, email, phone)
            Fund(id, name, description)
            Donation(id, donor_id -> Donor, fund_id -> Fund, amount, is_recurring, frequency, paid_at)
Features:   - Show a donation form with preset and custom amounts
            - Let donors choose a fund (tithe, building, missions)
            - Set up recurring monthly donations
            - Email an automatic receipt after each donation
            - Generate a yearly giving statement per donor
            - Show staff a donations report by fund and month
Storage:    WordPress MySQL database
Tech stack: WordPress, GiveWP plugin, GiveWP Recurring Donations add-on, Stripe
```

---

## Example 909

**Intent:**
I'm a farmer and I want to get the mandi prices for tomato and onion in my district on my phone every morning

**Spec:**
```
Type:       Scheduled script (notification bot)
Data model: Subscriber(id, phone, district, commodities)
            PriceRecord(id, market, commodity, min_price, max_price, modal_price, date)
Features:   - Fetch daily market prices from the government Agmarknet open data API
            - Filter prices for the subscriber's district and chosen crops
            - Compare today's price with yesterday's and mark up or down
            - Send a short SMS every morning at 7 AM
            - Save prices to build a price history
Input:      List of subscribers with phone number, district and crops
Storage:    SQLite
Tech stack: Python, requests, APScheduler, data.gov.in API, Twilio SMS API
```

---

## Example 910

**Intent:**
Our library is having 5000 books, we need software for issue and return of books with fine calculation, please do the needful

**Spec:**
```
Type:       Desktop application
Auth:       Librarian login (username + password)
Data model: Book(id, isbn, title, author, category, total_copies, available_copies)
            Member(id, name, member_type, phone, card_number)
            Issue(id, book_id -> Book, member_id -> Member, issued_on, due_on, returned_on, fine_amount)
Features:   - Add, edit and search books by title, author or ISBN
            - Issue a book to a member by scanning the barcode
            - Record returns and calculate the late fine per day automatically
            - Show the list of overdue books with member contact details
            - Print member library cards with barcodes
            - Import the existing book list from Excel
Storage:    Local SQLite database
Tech stack: Python, PySide6, python-barcode, openpyxl
```

---

## Example 911

**Intent:**
volunteer sign up for our ngo

**Spec:**
```
Type:       Web application (volunteer management)
Auth:       Volunteer registration and login (email + password); admin role for NGO staff
Data model: Volunteer(id, name, email, phone, skills, city)
            Activity(id, title, date, location, slots_needed, description)
            Signup(id, volunteer_id -> Volunteer, activity_id -> Activity, status, hours_logged)
Features:   - Register volunteers with skills and availability
            - List upcoming activities with open slots
            - Sign up for an activity and get an email confirmation
            - Mark attendance and log volunteer hours after each activity
            - Generate a volunteer certificate PDF with total hours
API:        REST
            POST /volunteers
            GET  /activities
            POST /activities/{id}/signups
            PUT  /signups/{id}/hours
Storage:    PostgreSQL
Tech stack: Python, Django, WeasyPrint (PDF), SendGrid
```

---

## Example 912

**Intent:**
need a way to send exam results to each student by email from the marks excel sheet

**Spec:**
```
Type:       Command-line script (automation)
Features:   - Read student names, emails and subject marks from an Excel file
            - Calculate total, percentage and pass/fail for each student
            - Create a PDF result card for each student
            - Email each student their own result card as an attachment
            - Write a log of sent and failed emails
Input:      Excel file (.xlsx) with columns: roll_no, name, email, and one column per subject
Tech stack: Python, pandas, openpyxl, ReportLab, smtplib (Gmail SMTP)
```

---

## Example 913

**Intent:**
I own a hair salon with 4 stylists and I'm tired of taking bookings over the phone, can customers book online?

**Spec:**
```
Type:       Web application (booking system)
Auth:       Customer login with phone + OTP; staff login with email + password
Data model: Stylist(id, name, working_days, start_time, end_time)
            Service(id, name, duration_minutes, price)
            Customer(id, name, phone)
            Booking(id, customer_id -> Customer, stylist_id -> Stylist, service_id -> Service, starts_at, status)
Features:   - Let customers pick a service, a stylist and a free time slot
            - Prevent double booking of the same stylist
            - Send an SMS confirmation and a reminder the day before
            - Let customers cancel or reschedule up to 2 hours before
            - Show each stylist their daily appointment list
            - Block time for breaks and holidays
API:        REST
            GET  /services
            GET  /stylists/{id}/availability?date={date}
            POST /bookings
            DELETE /bookings/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Twilio SMS API
```

---

## Example 914

**Intent:**
I'm a property agent and I want my own website where I can list flats and houses for sale or rent with photos

**Spec:**
```
Type:       Web application (listings)
Auth:       Admin login for the agent (email + password)
Data model: Property(id, title, listing_type, property_type, price, bedrooms, area_sqft, locality, description, status)
            Photo(id, property_id -> Property, url, sort_order)
            Enquiry(id, property_id -> Property, name, phone, message, created_at)
Features:   - Add and edit property listings with multiple photos
            - Filter listings by sale or rent, locality, price and bedrooms
            - Show each property on a map
            - Collect enquiries with a contact form on each listing
            - Mark properties as sold or rented to hide them
            - Add a WhatsApp click-to-chat button on each listing
API:        REST
            GET  /properties?type={sale|rent}&locality={name}
            GET  /properties/{id}
            POST /properties/{id}/enquiries
Storage:    PostgreSQL (data), Cloudinary (photos)
Tech stack: Next.js, Prisma, Leaflet + OpenStreetMap, Cloudinary
```

---

## Example 915

**Intent:**
We are having small lodge with 12 rooms in Rishikesh, kindly make online booking system so guests can book room directly without agents

**Spec:**
```
Type:       Web application (hotel booking)
Auth:       Admin login for lodge manager; guests book without account using email
Data model: RoomType(id, name, capacity, price_per_night, photos)
            Room(id, room_type_id -> RoomType, number)
            Booking(id, room_id -> Room, guest_name, email, phone, check_in, check_out, total, payment_status)
Features:   - Search room availability for check-in and check-out dates
            - Show room types with photos, amenities and price
            - Take an advance payment online to confirm the booking
            - Email a booking confirmation with lodge address and directions
            - Show the manager an occupancy calendar
            - Block rooms for maintenance or walk-in guests
API:        REST
            GET  /availability?check_in={date}&check_out={date}
            POST /bookings
            POST /payments/webhook
            GET  /admin/calendar?month={yyyy-mm}
Storage:    MySQL
Tech stack: PHP, Laravel, Razorpay, Bootstrap
```

---

## Example 916

**Intent:**
invoice maker for freelancers

**Spec:**
```
Type:       Web application (CRUD)
Auth:       User registration and login (email + password)
Data model: User(id, name, email, business_name, address, tax_id, logo_url)
            Client(id, user_id -> User, name, email, address)
            Invoice(id, user_id -> User, client_id -> Client, number, issue_date, due_date, currency, status)
            LineItem(id, invoice_id -> Invoice, description, quantity, rate)
Features:   - Create invoices with line items, tax and discount
            - Number invoices automatically
            - Download an invoice as a branded PDF
            - Email the invoice to the client with a pay link
            - Mark invoices as paid and show overdue ones
API:        REST
            GET  /invoices
            POST /invoices
            GET  /invoices/{id}/pdf
            POST /invoices/{id}/send
Storage:    PostgreSQL
Tech stack: Next.js, Supabase, react-pdf, Stripe Payment Links
```

---

## Example 917

**Intent:**
We bake cakes and have 3 delivery guys on bikes, I just want to know where each order is and tell the customer when it's coming

**Spec:**
```
Type:       Mobile application (driver app) + web dashboard
Auth:       Driver login with phone + OTP; owner login with email + password
Data model: Driver(id, name, phone)
            Delivery(id, customer_name, customer_phone, address, driver_id -> Driver, status, eta)
            LocationPing(id, driver_id -> Driver, lat, lng, recorded_at)
Features:   - Assign each order to a driver from the dashboard
            - Show the driver their delivery list with navigation links
            - Share the driver's live location every 30 seconds while on delivery
            - Show all drivers on a map in the owner dashboard
            - Send the customer an SMS with a tracking link when the order leaves
            - Mark orders as delivered with a photo proof
API:        REST
            POST /deliveries
            GET  /drivers/{id}/deliveries
            POST /drivers/{id}/location
            GET  /track/{delivery_id}
Storage:    Firebase Firestore
Tech stack: React Native, Firebase, Google Maps SDK, Twilio SMS API
```

---

## Example 918

**Intent:**
I keep my rice godown stock in google sheets, can it warn me when any variety is running low?

**Spec:**
```
Type:       Spreadsheet automation script
Features:   - Read current stock for each rice variety from the Stock sheet
            - Compare stock with a minimum level set per variety
            - Highlight low-stock rows in red
            - Send a daily email listing varieties below the minimum
            - Log each alert with date in a separate Alerts sheet
Input:      Google Sheet with columns: variety, bags_in_stock, minimum_bags
Storage:    Google Sheets
Tech stack: Google Apps Script, Google Sheets, MailApp, time-driven trigger
```

---

## Example 919

**Intent:**
tour booking site for my small travel agency in goa

**Spec:**
```
Type:       Web application (tour booking)
Auth:       Admin login for the agency; customers book with email and phone
Data model: Tour(id, name, description, duration_hours, price_per_person, pickup_points, photos)
            Departure(id, tour_id -> Tour, date, seats_total, seats_booked)
            Booking(id, departure_id -> Departure, name, email, phone, people, amount, payment_status)
Features:   - List tours with photos, itinerary and price
            - Show available dates and remaining seats
            - Book and pay online for a number of people
            - Send a confirmation email with pickup time and point
            - Show the agency a daily passenger list per tour
API:        REST
            GET  /tours
            GET  /tours/{id}/departures
            POST /bookings
            POST /payments/webhook
Storage:    PostgreSQL
Tech stack: Next.js, Prisma, Razorpay
```

---

## Example 920

**Intent:**
Parents at our school keep calling to ask where the bus is, can we have an app that shows the school bus location?

**Spec:**
```
Type:       Mobile application (parent app + driver app)
Auth:       Parent login with phone + OTP linked to their child; driver login with PIN
Data model: Bus(id, number, route_name, driver_name, driver_phone)
            Stop(id, bus_id -> Bus, name, lat, lng, order)
            Student(id, name, bus_id -> Bus, stop_id -> Stop, parent_phone)
            BusLocation(bus_id -> Bus, lat, lng, updated_at)
Features:   - Send the bus GPS location from the driver's phone during each trip
            - Show parents the bus moving on a map in real time
            - Notify parents when the bus is 5 minutes from their stop
            - Notify parents when their child's bus reaches school
            - Let the school admin manage routes and stops
Storage:    Firebase Realtime Database
Tech stack: Flutter, Firebase, Google Maps SDK, Firebase Cloud Messaging
```

---

## Example 921

**Intent:**
I'm a dentist and most of my patients forget to come back for their 6-month check-up. I'd like something that automatically reminds them by SMS and email when they're due, and lets them pick a slot from the link. It should read the patient list I already export from my clinic software as CSV.

**Spec:**
```
Type:       Web application (patient recall system)
Auth:       Admin login for clinic staff (email + password)
Data model: Patient(id, name, phone, email, last_visit_date, next_recall_date)
            RecallMessage(id, patient_id -> Patient, channel, sent_at, status)
            Slot(id, starts_at, is_booked)
            Booking(id, patient_id -> Patient, slot_id -> Slot, created_at)
Features:   - Import patients and last visit dates from a CSV export
            - Calculate the recall date 6 months after the last visit
            - Send SMS and email reminders when a patient is due
            - Include a link where the patient picks an open slot
            - Send a second reminder after 7 days if no slot is booked
            - Show staff a list of due, reminded and booked patients
API:        REST
            POST /patients/import
            GET  /recall/{token}/slots
            POST /recall/{token}/book
Storage:    PostgreSQL
Tech stack: Python, Django, Celery, Twilio SMS API, SendGrid
```

---

## Example 922

**Intent:**
event tickets with qr code

**Spec:**
```
Type:       Web application (ticketing)
Auth:       Organiser login (email + password); buyers check out with email only
Data model: Event(id, title, venue, starts_at, description)
            TicketType(id, event_id -> Event, name, price, quantity)
            Order(id, buyer_email, buyer_name, total, payment_status, created_at)
            Ticket(id, order_id -> Order, ticket_type_id -> TicketType, qr_code, checked_in_at)
Features:   - Create events with several ticket types and limits
            - Sell tickets online with card payment
            - Email each buyer a ticket with a unique QR code
            - Scan QR codes at the gate from a phone camera
            - Reject tickets that were already scanned
            - Show live sales and check-in counts
API:        REST
            POST /events
            POST /events/{id}/orders
            POST /tickets/scan
            GET  /events/{id}/stats
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe Checkout, qrcode, html5-qrcode
```

---

## Example 923

**Intent:**
My shop people are not marking attendance properly, I want app where they take selfie and location when coming and going

**Spec:**
```
Type:       Mobile application + admin web panel
Auth:       Staff login with phone + OTP; owner login with email + password
Data model: Shop(id, name, lat, lng, radius_m)
            Employee(id, name, phone, shop_id -> Shop)
            Punch(id, employee_id -> Employee, type, selfie_url, lat, lng, punched_at)
Features:   - Punch in and punch out with a selfie from the front camera
            - Capture GPS location and reject punches outside the shop radius
            - Show the owner today's present, absent and late staff
            - Calculate working hours per employee per day
            - Export a monthly attendance report to Excel
API:        REST
            POST /punches
            GET  /employees/{id}/punches?month={yyyy-mm}
            GET  /reports/monthly
Storage:    PostgreSQL (data), AWS S3 (selfies)
Tech stack: Flutter, Python, FastAPI, geolocator, AWS S3
```

---

## Example 924

**Intent:**
I have a food truck and want a simple page that shows where I'm parked today and what's on the menu

**Spec:**
```
Type:       Website (mobile-first)
Auth:       Owner login (email + password) for the update screen
Data model: Location(id, name, lat, lng, date, open_time, close_time)
            MenuItem(id, name, price, is_available)
Features:   - Show today's location on a map with opening hours
            - Show the menu with prices and sold-out items
            - Let the owner update today's location from the phone with one tap
            - Show the upcoming weekly schedule
            - Add a "get directions" link to Google Maps
Storage:    Firebase Firestore
Tech stack: React, Firebase Hosting, Firebase Auth, Leaflet
```

---

## Example 925

**Intent:**
pet clinic vaccination reminders

**Spec:**
```
Type:       Web application (reminder system)
Auth:       Staff login (email + password)
Data model: Owner(id, name, phone, email)
            Pet(id, owner_id -> Owner, name, species, breed, birth_date)
            Vaccination(id, pet_id -> Pet, vaccine_name, given_on, next_due_on)
Features:   - Record vaccinations for each pet with the next due date
            - Send an SMS and email reminder 7 days before a vaccine is due
            - Show a list of pets with vaccines due this week
            - Print a vaccination card for each pet
            - Mark reminders as done when the pet visits
API:        REST
            GET  /pets/{id}/vaccinations
            POST /vaccinations
            GET  /reminders/due?days=7
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Sidekiq, Twilio SMS API, Action Mailer
```

---

## Example 926

**Intent:**
I teach Bharatanatyam to about 60 kids and keeping track of who paid the monthly fee is a nightmare

**Spec:**
```
Type:       Web application (fee management)
Auth:       Single teacher login (email + password)
Data model: Student(id, name, parent_name, parent_phone, batch, monthly_fee, joined_on)
            Payment(id, student_id -> Student, month, amount, paid_on, mode)
Features:   - Record a fee payment with month, amount and mode (cash, UPI)
            - Show which students have not paid for the current month
            - Send a WhatsApp reminder link to parents with pending fees
            - Generate a receipt PDF for each payment
            - Show total collection per month
API:        REST
            GET  /students
            POST /payments
            GET  /fees/pending?month={yyyy-mm}
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap, WeasyPrint, WhatsApp click-to-chat links
```

---

## Example 927

**Intent:**
whatsapp bot so customers can order cakes from my home bakery without me replying to every msg

**Spec:**
```
Type:       Chatbot (WhatsApp)
Data model: Customer(id, name, whatsapp_number, address)
            Product(id, name, flavour, weight_kg, price, is_available)
            Order(id, customer_id -> Customer, delivery_date, message_on_cake, total, status)
            OrderItem(id, order_id -> Order, product_id -> Product, quantity)
Features:   - Reply to "hi" with a menu of cakes and prices
            - Guide the customer step by step to choose cake, weight and delivery date
            - Ask for the message to write on the cake and the delivery address
            - Send a UPI payment link to confirm the order
            - Notify the baker on WhatsApp about every new order
            - Let customers check their order status by typing "status"
API:        REST (webhook)
            POST /webhook/whatsapp
            GET  /orders?date={date}
Storage:    PostgreSQL
Tech stack: WhatsApp Business Cloud API, Node.js, Express, Razorpay Payment Links
```

---

## Example 928

**Intent:**
Need one portal for our college where students can download hall ticket and check exam time table

**Spec:**
```
Type:       Web application (student portal)
Auth:       Student login with register number + date of birth; admin login for exam cell
Data model: Student(id, register_no, name, dob, department, semester, photo_url)
            Exam(id, subject_code, subject_name, semester, department, exam_date, session)
            HallTicket(id, student_id -> Student, exam_cycle, is_eligible, generated_at)
Features:   - Show the exam time table for the student's department and semester
            - Generate a hall ticket PDF with photo, subjects and exam dates
            - Block hall tickets for students marked not eligible
            - Let the exam cell upload the time table from Excel
            - Publish notices on the portal homepage
API:        REST
            POST /login
            GET  /students/me/timetable
            GET  /students/me/hallticket.pdf
            POST /admin/timetable/import
Storage:    MySQL
Tech stack: PHP, Laravel, DomPDF, Laravel Excel
```

---

## Example 929

**Intent:**
parking lot management

**Spec:**
```
Type:       Web application (parking management)
Auth:       Attendant and manager login (username + password, role-based)
Data model: Slot(id, code, vehicle_type, is_occupied)
            Rate(id, vehicle_type, first_hour, per_extra_hour)
            Ticket(id, vehicle_number, vehicle_type, slot_id -> Slot, entry_at, exit_at, amount)
Features:   - Create an entry ticket with vehicle number and assign a free slot
            - Print a ticket with a barcode at entry
            - Calculate the parking fee at exit from the rate card
            - Show free and occupied slots on a live layout
            - Show daily collection and vehicle count reports
API:        REST
            POST /tickets
            POST /tickets/{id}/exit
            GET  /slots
            GET  /reports/daily?date={date}
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX, ESC/POS thermal printer library
```

---

## Example 930

**Intent:**
I'm a teacher and I'd love a quick quiz app I can run in class where kids answer on their phones and we see a leaderboard

**Spec:**
```
Type:       Web application (live quiz)
Auth:       Teacher login (Google sign-in); students join with a game PIN and nickname
Data model: Quiz(id, teacher_id, title)
            Question(id, quiz_id -> Quiz, text, options, correct_option, time_limit_s)
            Session(id, quiz_id -> Quiz, pin, status, started_at)
            Answer(id, session_id -> Session, question_id -> Question, nickname, option, answered_ms)
Features:   - Create quizzes with multiple-choice questions and time limits
            - Start a live session with a 6-digit join PIN
            - Show each question on the projector and answer buttons on phones
            - Score answers by correctness and speed
            - Show a leaderboard after every question
            - Export results per student as CSV
Storage:    Firebase Firestore (quizzes), Firebase Realtime Database (live sessions)
Tech stack: React, Firebase Auth, Firebase Realtime Database, Firestore
```

---

## Example 931

**Intent:**
I have 3 Airbnb flats and I keep messing up the cleaning schedule between guests

**Spec:**
```
Type:       Web application (scheduling)
Auth:       Host login (email + password); cleaners open a private schedule link
Data model: Property(id, name, address, ical_url, cleaning_minutes)
            Reservation(id, property_id -> Property, guest_name, check_in, check_out)
            Cleaner(id, name, phone)
            CleaningJob(id, property_id -> Property, cleaner_id -> Cleaner, date, window_start, window_end, status)
Features:   - Import reservations from each Airbnb calendar (iCal link) every hour
            - Create a cleaning job between each checkout and next check-in
            - Assign cleaners and send them an SMS with the job details
            - Let cleaners mark a job done with photos
            - Warn the host about same-day turnovers
Storage:    PostgreSQL
Tech stack: Python, Django, icalendar, Celery, Twilio SMS API
```

---

## Example 932

**Intent:**
We run a community food bank that gives monthly ration kits to around 400 families. Right now we write everything in a register and some families come twice while others are missed. We need a way to register families, record each pickup, and see who hasn't collected this month.

**Spec:**
```
Type:       Web application (distribution tracking)
Auth:       Volunteer login (email + password); coordinator role for reports
Data model: Family(id, head_name, phone, address, members_count, id_proof_number, card_code)
            Distribution(id, month, kit_type, started_on)
            Pickup(id, family_id -> Family, distribution_id -> Distribution, picked_up_at, volunteer_id)
Features:   - Register families and print a card with a QR code
            - Scan the family card at pickup to record the collection
            - Block a second pickup by the same family in the same month
            - Show families who have not collected this month with phone numbers
            - Report kits given out per month and stock needed
            - Work on a tablet with a weak internet connection
API:        REST
            POST /families
            POST /pickups
            GET  /distributions/{id}/pending
Storage:    PostgreSQL
Tech stack: Python, Django, PWA with offline sync (IndexedDB), html5-qrcode
```

---

## Example 933

**Intent:**
laundry pickup app

**Spec:**
```
Type:       Mobile application + admin web panel
Auth:       Customer login with phone + OTP; admin login with email + password
Data model: Customer(id, name, phone, address)
            Service(id, name, price_per_unit, unit)
            Order(id, customer_id -> Customer, pickup_slot, delivery_slot, status, total)
            OrderItem(id, order_id -> Order, service_id -> Service, quantity)
Features:   - Schedule a pickup slot and choose services (wash, iron, dry clean)
            - Track order status from picked up to delivered
            - Update item counts and final bill after pickup
            - Pay online or cash on delivery
            - Send push notifications on each status change
API:        REST
            POST /orders
            GET  /orders/{id}
            PATCH /orders/{id}/status
Storage:    Supabase (PostgreSQL)
Tech stack: React Native, Supabase, Razorpay, Expo Notifications
```

---

## Example 934

**Intent:**
app for my taxi drivers to log there trips and fuel so i know the real profit per car

**Spec:**
```
Type:       Mobile application + owner dashboard
Auth:       Driver login with phone + PIN; owner login with email + password
Data model: Car(id, registration_number, model)
            Driver(id, name, phone, car_id -> Car)
            Trip(id, driver_id -> Driver, car_id -> Car, start_km, end_km, fare, date)
            Expense(id, car_id -> Car, type, amount, litres, receipt_url, date)
Features:   - Log each trip with start km, end km and fare
            - Log fuel fills with litres, amount and receipt photo
            - Calculate mileage (km per litre) per car
            - Show profit per car per month (fares minus expenses)
            - Flag unusual fuel entries compared to past mileage
Storage:    Firebase Firestore (data), Firebase Storage (receipts)
Tech stack: Flutter, Firebase
```

---

## Example 935

**Intent:**
Kindly develop pharmacy billing software with expiry date alert for medicines, we are using it on one computer only

**Spec:**
```
Type:       Desktop application
Auth:       Login for owner and billing staff (username + password)
Data model: Medicine(id, name, manufacturer, hsn_code, gst_rate)
            Batch(id, medicine_id -> Medicine, batch_no, expiry_date, mrp, purchase_price, quantity)
            Bill(id, customer_name, doctor_name, total, gst_amount, created_at)
            BillItem(id, bill_id -> Bill, batch_id -> Batch, quantity, price)
Features:   - Create GST bills by searching medicine name and picking a batch
            - Reduce stock automatically after each bill
            - Alert for batches expiring in the next 60 days
            - Show low-stock medicines for reordering
            - Print bills on a thermal or A4 printer
            - Take a daily backup of the database to a USB drive
Storage:    Local SQLite database
Tech stack: C#, .NET, WPF, Entity Framework Core
```

---

## Example 936

**Intent:**
Could we have a Telegram bot that sends school notices and holiday announcements to all the parents?

**Spec:**
```
Type:       Chatbot (Telegram)
Auth:       Parents register with the bot using the student's admission number; admins listed by Telegram user ID
Data model: Parent(id, telegram_chat_id, student_admission_no, class_section)
            Notice(id, title, body, attachment_url, target_classes, sent_at)
Features:   - Register parents with /start and the admission number
            - Let admins send a notice to all parents or chosen classes
            - Attach PDFs and images to notices
            - Let parents see the last 10 notices with /notices
            - Show admins how many parents received each notice
Storage:    PostgreSQL
Tech stack: Python, python-telegram-bot, Telegram Bot API
```

---

## Example 937

**Intent:**
I'd like a website for our church where people can listen to past Sunday sermons

**Spec:**
```
Type:       Website (media archive)
Auth:       Admin login for church media team
Data model: Speaker(id, name, bio)
            Series(id, title, description, cover_url)
            Sermon(id, title, speaker_id -> Speaker, series_id -> Series, date, bible_passage, audio_url, notes)
Features:   - Upload sermon audio with title, speaker and Bible passage
            - Play sermons in the browser with a built-in audio player
            - Filter sermons by speaker, series or date
            - Publish a podcast RSS feed for Spotify and Apple Podcasts
            - Search sermons by title or passage
Storage:    PostgreSQL (data), AWS S3 (audio files)
Tech stack: Python, Django, AWS S3, Plyr audio player
```

---

## Example 938

**Intent:**
milk delivery app for dairy

**Spec:**
```
Type:       Mobile application (customer app + delivery app)
Auth:       Phone number + OTP login for customers and delivery staff
Data model: Customer(id, name, phone, address, route_id -> Route)
            Route(id, name, delivery_boy_id)
            Subscription(id, customer_id -> Customer, product, litres_per_day, is_paused)
            DeliveryLog(id, customer_id -> Customer, date, litres, delivered)
Features:   - Subscribe to a daily quantity of milk
            - Pause or change quantity for specific dates
            - Show delivery staff the day's route list with quantities
            - Mark each delivery as done or skipped
            - Generate a monthly bill and collect payment by UPI
API:        REST
            POST /subscriptions
            POST /subscriptions/{id}/pause
            GET  /routes/{id}/today
            POST /deliveries
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI, Razorpay
```

---

## Example 939

**Intent:**
I'm a wedding photographer and I want to give each couple a private online gallery to view and download their photos

**Spec:**
```
Type:       Web application (client galleries)
Auth:       Photographer login (email + password); clients open their gallery with a link + password
Data model: Gallery(id, couple_names, event_date, access_password_hash, expires_on)
            Photo(id, gallery_id -> Gallery, original_url, web_url, sort_order)
            Favourite(id, photo_id -> Photo, client_name, created_at)
Features:   - Upload hundreds of photos and create web-size previews automatically
            - Share a password-protected gallery link with the couple
            - Let clients mark favourites for the album
            - Download single photos or the full gallery as a ZIP
            - Add a watermark to previews
            - Expire galleries after a set date
API:        REST
            POST /galleries
            POST /galleries/{id}/photos
            GET  /galleries/{id}/download
Storage:    PostgreSQL (data), Cloudflare R2 (photos)
Tech stack: Next.js, Node.js, sharp (image resizing), Cloudflare R2
```

---

## Example 940

**Intent:**
need something to track eggs and feed for my poultry farm, i have 4 sheds

**Spec:**
```
Type:       Mobile application
Data model: Shed(id, name, bird_count, flock_start_date)
            DailyLog(id, shed_id -> Shed, date, eggs_collected, broken_eggs, feed_kg, mortality)
            Sale(id, date, trays_sold, price_per_tray, buyer)
Features:   - Enter daily eggs, feed used and dead birds per shed
            - Show laying percentage per shed per day
            - Show feed used per egg and per bird
            - Record egg tray sales and income
            - Show weekly charts of production for each shed
Storage:    Local on-device database (SQLite) with export to Excel
Tech stack: Flutter, sqflite, fl_chart
```

---

## Example 941

**Intent:**
We are running blood bank, need system to search donors by blood group and city and contact them in urgent case

**Spec:**
```
Type:       Web application (donor registry)
Auth:       Donor self-registration with phone + OTP; staff login with email + password
Data model: Donor(id, name, phone, blood_group, city, last_donated_on, is_available)
            Request(id, blood_group, units, hospital, city, needed_by, status)
            Contact(id, request_id -> Request, donor_id -> Donor, response, contacted_at)
Features:   - Register donors with blood group, city and last donation date
            - Search donors by blood group and city
            - Hide donors who donated in the last 90 days
            - Send an SMS alert to matching donors for an urgent request
            - Record which donors responded yes or no
API:        REST
            POST /donors
            GET  /donors?blood_group={group}&city={city}
            POST /requests
            POST /requests/{id}/alert
Storage:    PostgreSQL
Tech stack: Python, Django, MSG91 SMS API
```

---

## Example 942

**Intent:**
restaurant table booking

**Spec:**
```
Type:       Web application (reservations)
Auth:       Staff login (email + password); guests book with name, phone and email
Data model: Table(id, number, seats, area)
            Reservation(id, table_id -> Table, guest_name, phone, email, party_size, starts_at, status)
            OpeningHours(weekday, open_time, close_time)
Features:   - Show available times for a date and party size
            - Assign the smallest free table that fits the party
            - Send a confirmation email and a reminder on the day
            - Let staff see the evening's bookings on a floor plan
            - Mark guests as arrived, no-show or cancelled
API:        REST
            GET  /availability?date={date}&party={n}
            POST /reservations
            PATCH /reservations/{id}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire, Postmark
```

---

## Example 943

**Intent:**
Customers at my salon used to get a paper stamp card, I want to make it digital so they earn points every visit

**Spec:**
```
Type:       Web application (loyalty program)
Auth:       Customers identified by phone number + OTP; staff login with PIN
Data model: Customer(id, name, phone, points, joined_on)
            Visit(id, customer_id -> Customer, amount_spent, points_earned, visited_at)
            Reward(id, name, points_required)
            Redemption(id, customer_id -> Customer, reward_id -> Reward, redeemed_at)
Features:   - Add points at the counter by entering the customer's phone number
            - Earn 1 point per 100 rupees spent
            - Let customers check their points balance on their phone
            - Redeem points for rewards like a free haircut
            - Send an SMS when a customer reaches a reward
API:        REST
            POST /visits
            GET  /customers/{phone}/points
            POST /redemptions
Storage:    Supabase (PostgreSQL)
Tech stack: SvelteKit, Supabase, MSG91 SMS API
```

---

## Example 944

**Intent:**
We grow vegetables on our farm and want to sell a weekly veggie box subscription on Shopify

**Spec:**
```
Type:       E-commerce store (Shopify subscriptions)
Auth:       Shopify customer accounts
Features:   - Sell small, medium and large weekly veggie boxes as subscription products
            - Let customers skip a week, pause or cancel from their account
            - Charge customers automatically every week
            - Limit delivery to listed pincodes with a delivery-day selector
            - Export the weekly packing list with box sizes and addresses
            - Show which vegetables are in this week's box on the homepage
Storage:    Shopify (products, customers, orders)
Tech stack: Shopify, Shopify Subscriptions app, Liquid theme customisation, Zapier (export to Google Sheets)
```

---

## Example 945

**Intent:**
Our hospital OPD is very crowded and patients keep asking when their turn is. We want a token system where reception gives a token number at registration, each doctor's room has a screen showing the current token, and patients get an SMS when they are 3 tokens away. It should work on our local network even if internet goes down.

**Spec:**
```
Type:       Web application (queue management, local network)
Auth:       Login for reception and doctors (username + password, role-based)
Data model: Department(id, name)
            Doctor(id, name, department_id -> Department, room_number)
            Token(id, doctor_id -> Doctor, number, patient_name, phone, status, issued_at, called_at)
Features:   - Issue the next token number for a chosen doctor at reception
            - Print the token slip on a thermal printer
            - Let the doctor call the next token with one click
            - Show the current and next tokens on a TV screen per room
            - Announce the called token with a sound
            - Send an SMS when a patient is 3 tokens away (when internet is available)
            - Reset token numbers every day
API:        REST + WebSocket
            POST /tokens
            POST /doctors/{id}/next
            WS   /display/{doctor_id}
Storage:    PostgreSQL (on a local server)
Tech stack: Node.js, Express, Socket.IO, React, Twilio SMS API
```

---

## Example 946

**Intent:**
lost and found website for our college campus

**Spec:**
```
Type:       Web application (CRUD)
Auth:       Login with college email (Google sign-in restricted to the college domain)
Data model: User(id, name, email)
            Item(id, user_id -> User, type, title, description, category, location, photo_url, date, status)
            Claim(id, item_id -> Item, user_id -> User, message, created_at)
Features:   - Post a lost or found item with photo, place and date
            - Browse and search items by category and location
            - Send a claim message to the person who posted an item
            - Mark an item as returned
            - Hide items older than 60 days automatically
API:        REST
            GET  /items?type={lost|found}
            POST /items
            POST /items/{id}/claims
            PATCH /items/{id}
Storage:    Firebase Firestore (data), Firebase Storage (photos)
Tech stack: React, Firebase Auth, Firebase
```

---

## Example 947

**Intent:**
For my coaching institute I need online test series with all India ranking, students will pay through Razorpay to unlock the tests

**Spec:**
```
Type:       Web application (online exams)
Auth:       Student registration and login (email or phone + OTP); admin login for faculty
Data model: Student(id, name, phone, email, city)
            TestSeries(id, title, price, description)
            Test(id, series_id -> TestSeries, title, duration_min, negative_marking, starts_at)
            Question(id, test_id -> Test, text, options, correct_option, marks, solution)
            Purchase(id, student_id -> Student, series_id -> TestSeries, razorpay_payment_id, paid_at)
            Attempt(id, student_id -> Student, test_id -> Test, score, submitted_at, rank)
Features:   - Sell test series and unlock them after Razorpay payment
            - Run timed tests with auto-submit when time ends
            - Calculate score with negative marking
            - Show all-India rank and percentile after results
            - Show detailed solutions after the test
API:        REST
            POST /orders
            POST /payments/razorpay/webhook
            POST /tests/{id}/attempts
            GET  /tests/{id}/leaderboard
Storage:    PostgreSQL
Tech stack: Next.js, Node.js, Prisma, Razorpay
```

---

## Example 948

**Intent:**
hotel housekeeping checklist app

**Spec:**
```
Type:       Mobile application (staff app) + supervisor dashboard
Auth:       Staff login with employee ID + PIN; supervisor login with email + password
Data model: Room(id, number, floor, status)
            ChecklistItem(id, room_type, text)
            Task(id, room_id -> Room, assigned_to, date, status, completed_at)
            TaskCheck(id, task_id -> Task, checklist_item_id -> ChecklistItem, done, photo_url)
Features:   - Assign rooms to housekeepers for the day
            - Show a checklist per room (bed, bathroom, minibar, towels)
            - Tick items and attach photos of problems
            - Mark rooms as clean so the front desk sees them as ready
            - Report maintenance issues found during cleaning
Storage:    Supabase (PostgreSQL)
Tech stack: React Native, Supabase
```

---

## Example 949

**Intent:**
Our small town museum wants visitors to scan a QR code next to each exhibit and hear a short audio story about it

**Spec:**
```
Type:       Website (mobile audio guide)
Auth:       Admin login for museum staff
Data model: Exhibit(id, code, title, description, image_url)
            AudioTrack(id, exhibit_id -> Exhibit, language, audio_url, duration_s)
Features:   - Open the exhibit page directly from its QR code
            - Play the audio story with text transcript underneath
            - Choose the language (English, Hindi, local language)
            - Generate printable QR code labels for each exhibit
            - Count how many times each exhibit is scanned
Storage:    PostgreSQL (data), object storage (audio)
Tech stack: Python, Django, qrcode, HTML5 audio
```

---

## Example 950

**Intent:**
I run a small packers and movers business, I want customers to get a rough moving quote online

**Spec:**
```
Type:       Web application (quote calculator)
Auth:       Admin login for the business owner
Data model: QuoteRequest(id, name, phone, from_address, to_address, distance_km, home_size, floor, has_lift, move_date, estimate)
            RateCard(id, home_size, base_price, per_km, per_floor_no_lift)
Features:   - Ask for home size (1BHK, 2BHK, 3BHK), addresses and moving date
            - Calculate distance between addresses with a maps API
            - Calculate an estimated price from the rate card
            - Save each quote as a lead and email it to the owner
            - Let the owner edit rates without code
API:        REST
            POST /quotes
            GET  /admin/quotes
            PUT  /admin/rates
Storage:    MySQL
Tech stack: PHP, Laravel, Google Maps Distance Matrix API
```

---

## Example 951

**Intent:**
leave applications for my school teachers

**Spec:**
```
Type:       Web application (leave management)
Auth:       Teacher and principal login (email + password, role-based)
Data model: Teacher(id, name, email, subject)
            LeaveType(id, name, days_per_year)
            LeaveRequest(id, teacher_id -> Teacher, leave_type_id -> LeaveType, from_date, to_date, reason, status)
Features:   - Apply for leave with type, dates and reason
            - Approve or reject leave as the principal
            - Show each teacher their remaining leave balance
            - Show a calendar of who is on leave each day for substitutions
            - Email teachers when their request is approved or rejected
API:        REST
            POST /leave-requests
            PATCH /leave-requests/{id}
            GET  /teachers/me/balance
Storage:    PostgreSQL
Tech stack: Python, Django, FullCalendar
```

---

## Example 952

**Intent:**
make a site where ppl can rent my farm tractors by the day, i have 2 tractors and a rotavator

**Spec:**
```
Type:       Web application (equipment rental)
Auth:       Farmer login with phone + OTP; owner login with email + password
Data model: Equipment(id, name, type, daily_rate, with_operator_rate, photo_url, is_active)
            Farmer(id, name, phone, village)
            Rental(id, equipment_id -> Equipment, farmer_id -> Farmer, start_date, end_date, with_operator, amount, status)
Features:   - Show each machine with photo and daily rate
            - Show which dates each machine is free on a calendar
            - Request a booking for one or more days with or without an operator
            - Let the owner accept or reject requests and collect advance by UPI
            - Send an SMS confirmation to the farmer
API:        REST
            GET  /equipment
            GET  /equipment/{id}/availability?month={yyyy-mm}
            POST /rentals
            PATCH /rentals/{id}
Storage:    MySQL
Tech stack: PHP, Laravel, FullCalendar, MSG91 SMS API
```

---

## Example 953

**Intent:**
Sir I want app for my medical shop where customer can upload doctor prescription and we will deliver the medicines home

**Spec:**
```
Type:       Mobile application + shop admin panel
Auth:       Customer login with phone + OTP; shop staff login with email + password
Data model: Customer(id, name, phone, address)
            Prescription(id, customer_id -> Customer, image_url, uploaded_at, status)
            Order(id, prescription_id -> Prescription, customer_id -> Customer, items_text, total, payment_mode, status)
Features:   - Upload a photo of the doctor's prescription
            - Let the pharmacist review the prescription and send a price quote
            - Confirm the order and pay online or cash on delivery
            - Track order status until it is delivered
            - Reorder from a past prescription for monthly medicines
            - Notify the customer by push notification at each step
API:        REST
            POST /prescriptions
            POST /prescriptions/{id}/quote
            POST /orders/{id}/confirm
            GET  /orders/{id}
Storage:    Firebase Firestore (data), Firebase Storage (prescription images)
Tech stack: Flutter, Firebase, Razorpay, Firebase Cloud Messaging
```

---

## Example 954

**Intent:**
I'm a physiotherapist and I'd like to send my patients their home exercises as videos and see if they actually do them

**Spec:**
```
Type:       Web application (patient exercise programs)
Auth:       Therapist login (email + password); patients log in with a magic link sent by email
Data model: Exercise(id, name, video_url, instructions)
            Patient(id, name, email, phone, condition)
            Program(id, patient_id -> Patient, start_date, end_date)
            ProgramItem(id, program_id -> Program, exercise_id -> Exercise, sets, reps, days_per_week)
            Log(id, program_item_id -> ProgramItem, done_on, pain_level, comment)
Features:   - Build an exercise library with short demo videos
            - Assign a program of exercises with sets and reps to a patient
            - Let patients watch the videos and tick exercises as done
            - Ask patients to rate pain from 0 to 10 after each session
            - Show the therapist each patient's adherence and pain trend
API:        REST
            POST /programs
            GET  /patients/me/program
            POST /logs
            GET  /patients/{id}/progress
Storage:    PostgreSQL (data), Mux (videos)
Tech stack: Next.js, Supabase, Mux Video
```

---

## Example 955

**Intent:**
temple pooja booking online

**Spec:**
```
Type:       Web application (booking + payments)
Auth:       Devotees book with name and phone; admin login for temple office
Data model: Pooja(id, name, description, price, daily_limit)
            Booking(id, pooja_id -> Pooja, devotee_name, gothram, nakshatra, phone, pooja_date, amount, payment_status)
Features:   - List poojas and sevas with price and timings
            - Book a pooja for a date with devotee name, gothram and nakshatra
            - Pay online and get a receipt by SMS
            - Stop bookings when the daily limit for a pooja is reached
            - Print the daily list of bookings for the priests
API:        REST
            GET  /poojas
            POST /bookings
            POST /payments/webhook
            GET  /admin/bookings?date={date}
Storage:    MySQL
Tech stack: PHP, Laravel, Razorpay, MSG91 SMS API
```

---

## Example 956

**Intent:**
Planning our wedding reception and the seating chart is driving me crazy, I want to drag guests onto tables

**Spec:**
```
Type:       Web application (single-page planner)
Data model: Guest(id, name, group, dietary_note, plus_one)
            Table(id, name, seats, shape, x, y)
            Seat(table_id -> Table, guest_id -> Guest, position)
Features:   - Import the guest list from a CSV file
            - Add round or long tables with a number of seats
            - Drag and drop guests onto tables
            - Warn when a table is over capacity
            - Mark guests who should not sit together and flag conflicts
            - Print the seating chart and a per-table name list
Storage:    Browser localStorage with JSON export and import
Tech stack: React, TypeScript, dnd-kit, Papa Parse
```

---

## Example 957

**Intent:**
Our town has a small bus service with 6 routes and the timetable is only printed on paper at the bus stand. We want a simple phone app where people can see the next bus from their stop, even when they have no internet signal in the villages. The office should be able to update timings when they change.

**Spec:**
```
Type:       Mobile application (offline-first)
Auth:       Admin login for the transport office (web panel only)
Data model: Route(id, number, name)
            Stop(id, name, lat, lng)
            RouteStop(id, route_id -> Route, stop_id -> Stop, sequence)
            Trip(id, route_id -> Route, days, departure_times_json)
Features:   - Show the next departures from a chosen stop
            - Show the full timetable for each route
            - Find the nearest stop using GPS
            - Work fully offline with the last downloaded timetable
            - Download timetable updates when the phone is online
            - Let the office edit routes and timings in a web panel
API:        REST
            GET  /timetable/version
            GET  /timetable
            PUT  /admin/routes/{id}
Storage:    PostgreSQL (server), SQLite on device
Tech stack: Flutter, sqflite, Python, FastAPI
```

---

## Example 958

**Intent:**
want to send premium due reminders to my insurance customers on whatsapp automaticaly

**Spec:**
```
Type:       Scheduled script (WhatsApp notifications)
Data model: Customer(id, name, whatsapp_number)
            Policy(id, customer_id -> Customer, policy_number, plan_name, premium_amount, due_date, frequency)
            ReminderLog(id, policy_id -> Policy, sent_at, status)
Features:   - Import customers and policies from an Excel sheet
            - Find policies with premium due in 15 days, 7 days and 1 day
            - Send a WhatsApp template message with policy number, amount and due date
            - Move the due date forward after the agent marks it paid
            - Log sent and failed messages
Input:      Excel file with columns: name, whatsapp_number, policy_number, plan_name, premium_amount, due_date, frequency
Storage:    SQLite
Tech stack: Python, pandas, APScheduler, WhatsApp Business Cloud API
```

---

## Example 959

**Intent:**
car wash booking

**Spec:**
```
Type:       Mobile application + admin web panel
Auth:       Customer login with phone + OTP; admin login with email + password
Data model: Customer(id, name, phone)
            Vehicle(id, customer_id -> Customer, number, type)
            Package(id, name, vehicle_type, price, duration_minutes)
            Booking(id, vehicle_id -> Vehicle, package_id -> Package, slot_start, bay, status)
Features:   - Choose a vehicle, a wash package and a time slot
            - Limit bookings per slot to the number of wash bays
            - Pay online or at the centre
            - Notify the customer when the car is ready
            - Show the admin the day's bookings per bay
API:        REST
            GET  /packages?vehicle_type={type}
            GET  /slots?date={date}
            POST /bookings
            PATCH /bookings/{id}/status
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express, Stripe
```

---

## Example 960

**Intent:**
Kindly make simple software for my school to print report cards with grades and teacher remarks for each term

**Spec:**
```
Type:       Web application (report cards)
Auth:       Login for class teachers and admin (username + password, role-based)
Data model: Student(id, admission_no, name, class_section, roll_no, dob)
            Subject(id, name, class_level, max_marks)
            Mark(id, student_id -> Student, subject_id -> Subject, term, marks)
            Remark(id, student_id -> Student, term, text)
            GradeScale(min_percent, grade)
Features:   - Enter marks for a whole class per subject in a grid
            - Convert marks to grades using the school's grade scale
            - Add a remark for each student per term
            - Generate report cards as PDFs with the school logo and signatures
            - Print all report cards for a class in one go
API:        REST
            POST /marks/bulk
            POST /remarks
            GET  /classes/{id}/report-cards.pdf?term={term}
Storage:    MySQL
Tech stack: Python, Django, WeasyPrint
```

---

## Example 961

**Intent:**
I have a plant nursery and want an online catalog where people pick plants and send the order to me on WhatsApp

**Spec:**
```
Type:       Website (catalog with WhatsApp checkout)
Auth:       Admin login for the nursery owner
Data model: Category(id, name)
            Plant(id, category_id -> Category, name, price, pot_size, sunlight, care_tips, photo_url, in_stock)
Features:   - Show plants by category (indoor, flowering, fruit, succulents)
            - Show care tips and sunlight needs on each plant page
            - Add plants to a cart with quantities
            - Send the cart as a pre-filled WhatsApp message to the owner
            - Let the owner mark plants out of stock from the phone
Storage:    Firebase Firestore
Tech stack: Next.js, Firebase, WhatsApp click-to-chat (wa.me links)
```

---

## Example 962

**Intent:**
As a freelance photographer I want clients to sign my contract and pay a deposit online before I lock in their date, using Stripe

**Spec:**
```
Type:       Web application (booking contracts)
Auth:       Photographer login (email + password); clients open a unique booking link
Data model: Client(id, name, email, phone)
            Booking(id, client_id -> Client, shoot_type, shoot_date, package_price, deposit_amount, status)
            Contract(id, booking_id -> Booking, body_html, signed_name, signed_at, signer_ip)
            Payment(id, booking_id -> Booking, stripe_payment_intent_id, amount, paid_at)
Features:   - Create a booking from a contract template with client details filled in
            - Let the client sign the contract by typing their name
            - Take the deposit payment with Stripe Checkout
            - Lock the date on the calendar only after signing and paying
            - Email both sides a PDF copy of the signed contract
            - Send a reminder for the remaining balance before the shoot
API:        REST
            POST /bookings
            POST /bookings/{token}/sign
            POST /bookings/{token}/checkout
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Next.js, Prisma, Stripe Checkout, Stripe webhooks, react-pdf
```

---

## Example 963

**Intent:**
rent collection for my tenants

**Spec:**
```
Type:       Web application (rent tracking)
Auth:       Landlord login (email + password); tenants log in with phone + OTP
Data model: Property(id, name, address)
            Unit(id, property_id -> Property, label, monthly_rent)
            Tenant(id, unit_id -> Unit, name, phone, lease_start, lease_end, deposit)
            RentPayment(id, tenant_id -> Tenant, month, amount, paid_on, mode)
Features:   - Generate a rent due entry for each tenant every month
            - Send a payment link and reminder on the 1st and 5th
            - Record cash or bank payments manually
            - Show which units are paid, pending or late
            - Send a rent receipt to the tenant after payment
API:        REST
            GET  /rent?month={yyyy-mm}
            POST /payments
            POST /payments/webhook
Storage:    PostgreSQL
Tech stack: Python, Django, Razorpay Payment Links, MSG91 SMS API
```

---

## Example 964

**Intent:**
teh kids in my sunday school class need a points system for memorizing bible verses, something fun on a big screen

**Spec:**
```
Type:       Web application (classroom points board)
Auth:       Teacher login (email + password)
Data model: Kid(id, name, team, avatar)
            Verse(id, reference, text, points)
            Award(id, kid_id -> Kid, verse_id -> Verse, points, awarded_on)
Features:   - Add kids with a fun avatar and team colour
            - Award points when a kid recites a verse
            - Show a colourful leaderboard for the projector
            - Show team totals for a team challenge
            - Play a celebration animation when a kid passes a milestone
            - Reset points at the start of each quarter
Storage:    Supabase (PostgreSQL)
Tech stack: React, Supabase, canvas-confetti
```

---

## Example 965

**Intent:**
Our society (apartment) need app for maintenance bill and registering complaints like water leakage, lift not working

**Spec:**
```
Type:       Mobile application + committee web panel
Auth:       Resident login with phone + OTP linked to flat number; committee members have admin role
Data model: Flat(id, block, number, area_sqft, owner_name)
            Resident(id, flat_id -> Flat, name, phone, is_owner)
            MaintenanceBill(id, flat_id -> Flat, month, amount, due_date, paid_on)
            Complaint(id, flat_id -> Flat, category, description, photo_url, status, created_at)
Features:   - Generate monthly maintenance bills per flat by area or fixed rate
            - Pay maintenance online and download the receipt
            - Raise a complaint with category and photo
            - Track complaint status (open, assigned, resolved)
            - Post notices to all residents
            - Show the committee pending dues and open complaints
API:        REST
            GET  /flats/{id}/bills
            POST /bills/{id}/pay
            POST /complaints
            PATCH /complaints/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Python, Django REST Framework, Razorpay
```

---

## Example 966

**Intent:**
I run a courier counter and customers keep calling to ask where their parcel is, can they just check with the tracking number?

**Spec:**
```
Type:       Web application (parcel booking + tracking)
Auth:       Counter staff login (username + password)
Data model: Parcel(id, tracking_no, sender_name, sender_phone, receiver_name, receiver_phone, destination, weight_kg, charge, status)
            TrackingEvent(id, parcel_id -> Parcel, status, location, note, created_at)
Features:   - Book a parcel at the counter and generate a tracking number
            - Print a label with a barcode and the receipt
            - Add tracking updates (dispatched, in transit, out for delivery, delivered)
            - Let customers check status on a public page with the tracking number
            - Send an SMS to the receiver when the parcel is out for delivery
API:        REST
            POST /parcels
            POST /parcels/{tracking_no}/events
            GET  /track/{tracking_no}
Storage:    MySQL
Tech stack: PHP, Laravel, picqer/php-barcode-generator, MSG91 SMS API
```

---

## Example 967

**Intent:**
I'm a vet who visits farms in about 30 villages and I lose track of which animals I treated and when I need to go back. I'd like an app on my phone that works without network in the fields, where I can record each visit, the animal, the treatment and the follow-up date. When I'm back in town it should sync and remind me of follow-ups.

**Spec:**
```
Type:       Mobile application (offline-first)
Auth:       Single vet login (email + password)
Data model: Farmer(id, name, phone, village)
            Animal(id, farmer_id -> Farmer, species, tag_number, breed, age)
            Visit(id, animal_id -> Animal, date, diagnosis, treatment, medicines, fee, follow_up_date)
Features:   - Record visits with diagnosis, treatment and medicines given
            - Save everything on the phone when there is no network
            - Sync records to the cloud when the phone is back online
            - Show follow-ups due today and this week grouped by village
            - Search past visits by farmer name or animal tag
            - Track fees collected and pending per farmer
Storage:    Local SQLite on device, synced to Supabase (PostgreSQL)
Tech stack: Flutter, drift (SQLite), Supabase, flutter_local_notifications
```

---

## Example 968

**Intent:**
conference speaker submissions

**Spec:**
```
Type:       Web application (call for papers)
Auth:       Speaker registration and login (email + password or GitHub sign-in); reviewers and admin roles
Data model: Speaker(id, name, email, bio, photo_url)
            Proposal(id, speaker_id -> Speaker, title, abstract, track, level, status)
            Review(id, proposal_id -> Proposal, reviewer_id, score, comment)
Features:   - Submit talk proposals with title, abstract, track and level
            - Edit proposals until the submission deadline
            - Let reviewers score proposals anonymously
            - Rank proposals by average score for the selection meeting
            - Email speakers when their talk is accepted or rejected
API:        REST
            POST /proposals
            PUT  /proposals/{id}
            POST /proposals/{id}/reviews
            GET  /admin/proposals?sort=score
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Devise, OmniAuth GitHub, Action Mailer
```

---

## Example 969

**Intent:**
My mom runs a tiffin service with about 40 office customers and she wants to show the weekly menu and handle monthly subscriptions

**Spec:**
```
Type:       Web application (subscriptions)
Auth:       Customer login with phone + OTP; admin login for the owner
Data model: Customer(id, name, phone, office_address)
            Plan(id, name, meals_per_day, price_per_month)
            Subscription(id, customer_id -> Customer, plan_id -> Plan, start_date, end_date, status)
            MenuDay(id, date, lunch_items, dinner_items)
            Skip(id, subscription_id -> Subscription, date)
Features:   - Show this week's lunch and dinner menu
            - Subscribe to a monthly plan and pay online
            - Skip meals for specific days before 9 PM the day before
            - Show the owner how many tiffins to cook tomorrow
            - Send a renewal reminder 3 days before the plan ends
API:        REST
            GET  /menu?week={date}
            POST /subscriptions
            POST /subscriptions/{id}/skips
            GET  /admin/tomorrow-count
Storage:    Supabase (PostgreSQL)
Tech stack: Next.js, Supabase, Razorpay
```

---

## Example 970

**Intent:**
need excel macro or something that makes salary slips for my 20 workers and emails them each month

**Spec:**
```
Type:       Command-line script (automation)
Features:   - Read employee details and monthly attendance from an Excel file
            - Calculate gross salary, PF, ESI and net pay for each worker
            - Create a salary slip PDF per worker with the company name
            - Email each worker their slip as an attachment
            - Save all slips in a folder named by month
Input:      Excel file (.xlsx) with columns: emp_id, name, email, basic, hra, days_present, days_in_month, advance
Tech stack: Python, pandas, openpyxl, ReportLab, smtplib
```

---

## Example 971

**Intent:**
Please make a hostel mess app where students can mark if they are skipping meal so that less food is getting wasted

**Spec:**
```
Type:       Mobile application + mess manager dashboard
Auth:       Student login with college roll number + password; mess manager login
Data model: Student(id, roll_no, name, hostel, room)
            Meal(id, date, type, menu)
            OptOut(id, student_id -> Student, meal_id -> Meal, created_at)
            Feedback(id, student_id -> Student, meal_id -> Meal, rating, comment)
Features:   - Show the week's menu for breakfast, lunch and dinner
            - Mark a meal as skipped until 4 hours before it is served
            - Show the mess manager the expected headcount for each meal
            - Rate meals and leave feedback
            - Show monthly food saved compared to full attendance
API:        REST
            GET  /meals?week={date}
            POST /meals/{id}/opt-out
            GET  /admin/meals/{id}/headcount
            POST /meals/{id}/feedback
Storage:    Firebase Firestore
Tech stack: React Native, Firebase
```

---

## Example 972

**Intent:**
We're running a kids' summer camp this year and need parents to register online and fill in the medical and pickup details

**Spec:**
```
Type:       Web application (registrations)
Auth:       Parent registration and login (email + password); staff admin role
Data model: Parent(id, name, email, phone)
            Child(id, parent_id -> Parent, name, dob, allergies, medications, doctor_phone)
            Session(id, name, start_date, end_date, age_min, age_max, capacity, fee)
            Enrollment(id, child_id -> Child, session_id -> Session, payment_status)
            AuthorizedPickup(id, child_id -> Child, name, relation, phone)
Features:   - Register children for camp weeks with age limits and capacity
            - Collect allergies, medications and emergency contacts
            - Collect names of people allowed to pick up the child
            - Pay the camp fee online
            - Print a daily roster with allergy flags for counselors
API:        REST
            GET  /sessions
            POST /children
            POST /enrollments
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe Checkout
```

---

## Example 973

**Intent:**
fishing boat catch log

**Spec:**
```
Type:       Mobile application (offline-first)
Data model: Trip(id, boat_name, departed_at, returned_at, fuel_litres, crew_count)
            Catch(id, trip_id -> Trip, species, weight_kg, lat, lng, caught_at)
            Sale(id, trip_id -> Trip, buyer, species, weight_kg, price_per_kg)
Features:   - Start and end a fishing trip with fuel and crew details
            - Log each catch with species, weight and GPS position
            - Work at sea with no network connection
            - Record sales at the harbour and calculate trip income
            - Show profit per trip after fuel costs
Storage:    Local on-device database (SQLite)
Tech stack: Flutter, sqflite, geolocator
```

---

## Example 974

**Intent:**
We rent out scooters and bikes in Manali and I want tourists to book online and pay the security deposit in advance

**Spec:**
```
Type:       Web application (vehicle rental)
Auth:       Customer login with phone + OTP; staff login with email + password
Data model: Vehicle(id, model, type, registration_no, daily_rate, deposit, status)
            Customer(id, name, phone, licence_number, licence_photo_url)
            Rental(id, vehicle_id -> Vehicle, customer_id -> Customer, start_at, end_at, rent_amount, deposit_amount, status)
Features:   - Show available bikes and scooters for chosen dates
            - Upload a driving licence photo before booking
            - Pay rent and security deposit online
            - Record vehicle condition photos at pickup and return
            - Refund the deposit after return minus any damages
API:        REST
            GET  /vehicles/available?from={date}&to={date}
            POST /rentals
            POST /rentals/{id}/return
            POST /payments/webhook
Storage:    PostgreSQL (data), AWS S3 (photos)
Tech stack: Next.js, Prisma, Razorpay (payments and refunds), AWS S3
```

---

## Example 975

**Intent:**
After every workshop I run I collect feedback with Google Forms, can it automatically make a summary and email it to the trainer?

**Spec:**
```
Type:       Spreadsheet automation script
Features:   - Trigger when a new Google Form response arrives or on a daily schedule
            - Group responses by workshop name and date
            - Calculate average ratings for content, trainer and venue
            - Collect all written comments in one list
            - Email the trainer a summary with averages and comments
            - Mark summarised responses so they are not sent twice
Input:      Google Form linked to a Google Sheet (workshop, trainer_email, ratings, comments)
Storage:    Google Sheets
Tech stack: Google Forms, Google Sheets, Google Apps Script, GmailApp
```

---

## Example 976

**Intent:**
photo booth at weddings that uploads the pics and guests get there photos by scanning a qr

**Spec:**
```
Type:       Desktop application (kiosk) + web gallery
Data model: Event(id, name, date, slug)
            Photo(id, event_id -> Event, file_url, taken_at, short_code)
Features:   - Show a live camera preview with a countdown on a touch screen
            - Take photos and add the couple's frame overlay
            - Upload each photo to the cloud right after it is taken
            - Show a QR code on screen that opens that photo on the guest's phone
            - Keep photos locally and upload later if Wi-Fi drops
            - Show all photos of the event in a web gallery
API:        REST
            POST /events/{id}/photos
            GET  /p/{short_code}
            GET  /events/{slug}/gallery
Storage:    Local folder (backup), Firebase Storage + Firestore
Tech stack: Electron, React, Firebase, qrcode
```

---

## Example 977

**Intent:**
I am running small hospital of 50 beds, need system showing bed availability to reception and ambulance people so they know before bringing patient

**Spec:**
```
Type:       Web application (bed management)
Auth:       Login for nurses, reception and ambulance coordinators (username + password, role-based)
Data model: Ward(id, name, type, floor)
            Bed(id, ward_id -> Ward, number, status, updated_at)
            Admission(id, bed_id -> Bed, patient_name, admitted_at, expected_discharge, discharged_at)
Features:   - Show free, occupied and cleaning beds by ward (general, ICU, maternity)
            - Let nurses update bed status from the ward computer or phone
            - Show live updates on the reception screen without refreshing
            - Show expected discharges for the next 24 hours
            - Give ambulance coordinators a read-only view of free ICU and general beds
API:        REST + WebSocket
            GET  /beds?ward={id}
            PATCH /beds/{id}
            POST /admissions
            WS   /beds/live
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Socket.IO, React
```

---

## Example 978

**Intent:**
tutor finder app

**Spec:**
```
Type:       Mobile application (marketplace)
Auth:       Registration and login with phone + OTP for parents and tutors
Data model: Tutor(id, name, subjects, classes, area, hourly_rate, mode, bio, rating, is_verified)
            Parent(id, name, phone, area)
            Request(id, parent_id -> Parent, tutor_id -> Tutor, subject, child_class, message, status)
            Review(id, tutor_id -> Tutor, parent_id -> Parent, stars, comment)
Features:   - Create a tutor profile with subjects, classes, area and fees
            - Search tutors by subject, class, area and home or online mode
            - Send a demo class request to a tutor
            - Chat after the tutor accepts the request
            - Rate and review tutors after classes start
API:        REST
            GET  /tutors?subject={s}&area={a}
            POST /requests
            PATCH /requests/{id}
            POST /tutors/{id}/reviews
Storage:    Supabase (PostgreSQL)
Tech stack: React Native, Supabase (auth, database, realtime chat)
```

---

## Example 979

**Intent:**
We run a driving school with 5 instructors and want students to book their lessons themselves instead of calling us

**Spec:**
```
Type:       Web application (lesson booking)
Auth:       Student and instructor login (email + password); admin role for the office
Data model: Instructor(id, name, phone, car, working_hours)
            Student(id, name, phone, licence_type, lessons_purchased, lessons_used)
            Lesson(id, student_id -> Student, instructor_id -> Instructor, starts_at, pickup_location, status)
Features:   - Show each instructor's free lesson slots for the week
            - Book a lesson using a prepaid lesson package
            - Cancel up to 24 hours before without losing the lesson
            - Show instructors their daily schedule with pickup locations
            - Let instructors add notes on student progress after each lesson
API:        REST
            GET  /instructors/{id}/slots?week={date}
            POST /lessons
            DELETE /lessons/{id}
            POST /lessons/{id}/notes
Storage:    PostgreSQL
Tech stack: Python, Django, FullCalendar, Stripe
```

---

## Example 980

**Intent:**
Our farmers' cooperative collects mango from about 200 member farmers every day in season. Each farmer's produce is weighed and graded at the collection centre, and payments are made every 15 days. We want to stop using paper slips, give farmers an SMS receipt for each delivery, and calculate the payment automatically.

**Spec:**
```
Type:       Web application (collection and payments)
Auth:       Staff login at each collection centre (username + password); admin role for the cooperative office
Data model: Farmer(id, member_no, name, phone, village, bank_account, ifsc)
            Grade(id, name, rate_per_kg, valid_from)
            Collection(id, farmer_id -> Farmer, centre, grade_id -> Grade, weight_kg, amount, collected_at)
            PaymentCycle(id, start_date, end_date, status)
            Payout(id, cycle_id -> PaymentCycle, farmer_id -> Farmer, total_amount, paid_at)
Features:   - Record each delivery with farmer, grade and weight at the counter
            - Send the farmer an SMS receipt with weight, grade and amount
            - Update grade rates when market prices change
            - Calculate each farmer's total for every 15-day cycle
            - Export a bank payment file for bulk transfer
            - Show daily collection by centre and grade
API:        REST
            POST /collections
            GET  /farmers/{id}/collections?cycle={id}
            POST /cycles/{id}/close
            GET  /cycles/{id}/bank-file
Storage:    PostgreSQL
Tech stack: Python, Django, MSG91 SMS API, openpyxl
```

---

## Example 981

**Intent:**
need a program that does swiss pairings for our chess club tournamnet, we do it by hand now

**Spec:**
```
Type:       Desktop application
Data model: Tournament(id, name, rounds, date)
            Player(id, tournament_id -> Tournament, name, rating)
            Pairing(id, tournament_id -> Tournament, round, white_id -> Player, black_id -> Player, result)
Features:   - Add players with their ratings
            - Generate Swiss-system pairings for each round avoiding repeat opponents
            - Balance white and black colours for each player
            - Give a bye to one player when the count is odd
            - Enter results and show standings with Buchholz tie-break
            - Print pairings and standings for the notice board
Storage:    Local SQLite database
Tech stack: Python, PySide6
```

---

## Example 982

**Intent:**
Want mobile app for my travels company, customers can book outstation cab and see driver details before trip

**Spec:**
```
Type:       Mobile application (customer app) + admin web panel
Auth:       Customer login with phone + OTP; admin login with email + password
Data model: Customer(id, name, phone)
            CarType(id, name, seats, rate_per_km, driver_allowance_per_day)
            Driver(id, name, phone, photo_url, licence_no)
            Car(id, car_type_id -> CarType, registration_no)
            Trip(id, customer_id -> Customer, car_type_id -> CarType, driver_id -> Driver, car_id -> Car, pickup, destination, start_date, return_date, estimated_fare, status)
Features:   - Get a fare estimate for one-way or round trip by distance and car type
            - Book an outstation cab with pickup date and time
            - Let the admin assign a driver and car to each booking
            - Show the customer driver name, photo, phone and car number before the trip
            - Pay an advance online and the rest after the trip
API:        REST
            POST /fare-estimate
            POST /trips
            PATCH /trips/{id}/assign
            GET  /trips/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Google Maps Distance Matrix API, Razorpay
```

---

## Example 983

**Intent:**
prayer times screen for our mosque

**Spec:**
```
Type:       Web application (display screen)
Auth:       Admin login for mosque committee
Data model: PrayerTime(date, fajr, sunrise, dhuhr, asr, maghrib, isha)
            Iqamah(id, prayer, time, valid_from)
            Announcement(id, text, start_date, end_date)
Features:   - Calculate daily prayer times for the mosque's location
            - Show today's prayer and iqamah times on a TV in full screen
            - Count down to the next iqamah
            - Scroll announcements at the bottom of the screen
            - Let the committee change iqamah times from a phone
Storage:    SQLite
Tech stack: Python, Flask, adhan (prayer time calculation), JavaScript, Raspberry Pi in kiosk mode
```

---

## Example 984

**Intent:**
I'm a real estate agent and all my leads are in Airtable, I want it to auto-assign new leads and remind me to follow up

**Spec:**
```
Type:       No-code automation (Airtable)
Data model: Lead(id, name, phone, email, budget, area, source, status, assigned_agent -> Agent, next_follow_up)
            Agent(id, name, email, phone)
            Activity(id, lead_id -> Lead, type, notes, date)
Features:   - Capture new leads from the website form into Airtable
            - Assign new leads to agents in round-robin order
            - Email the agent when a lead is assigned to them
            - Send a daily email of leads due for follow-up
            - Show a pipeline view by lead status
Storage:    Airtable base
Tech stack: Airtable, Airtable Automations, Airtable Interfaces, Airtable Forms
```

---

## Example 985

**Intent:**
We run a care home for 25 elderly residents and the staff need to know which medicine to give to whom and at what time

**Spec:**
```
Type:       Mobile application (tablet) + manager web panel
Auth:       Staff login with PIN on a shared tablet; manager login with email + password
Data model: Resident(id, name, room, photo_url, allergies)
            Medication(id, resident_id -> Resident, drug_name, dose, times_of_day, start_date, end_date)
            Administration(id, medication_id -> Medication, scheduled_at, given_at, given_by, status, note)
Features:   - Show a medication round list grouped by time with resident photos
            - Mark each dose as given, refused or missed with a note
            - Alert staff when a dose is overdue by 30 minutes
            - Show allergy warnings on the resident's screen
            - Generate a monthly medication record per resident for doctors
API:        REST
            GET  /rounds?time={hh:mm}
            POST /administrations
            GET  /residents/{id}/mar?month={yyyy-mm}
Storage:    PostgreSQL
Tech stack: React Native, Node.js, NestJS
```

---

## Example 986

**Intent:**
warehouse pallet tracking with barcodes

**Spec:**
```
Type:       Mobile application (scanner) + web dashboard
Auth:       Staff login (username + password, role-based)
Data model: Location(id, code, zone, rack, level)
            Pallet(id, barcode, sku, quantity, location_id -> Location, status, received_at)
            Movement(id, pallet_id -> Pallet, from_location_id -> Location, to_location_id -> Location, moved_by, moved_at)
Features:   - Scan a pallet barcode to receive it into the warehouse
            - Scan a pallet and a rack location to put it away
            - Record every move with time and user
            - Search where any pallet or SKU is stored
            - Show warehouse occupancy by zone
API:        REST
            POST /pallets
            POST /pallets/{barcode}/move
            GET  /pallets?sku={sku}
            GET  /locations/occupancy
Storage:    PostgreSQL
Tech stack: Flutter, mobile_scanner, Python, FastAPI, React
```

---

## Example 987

**Intent:**
website for my village homestay with photos and a booking enquiry form

**Spec:**
```
Type:       Website (static with form)
Features:   - Show the homestay story, rooms and a photo gallery
            - Show what's nearby (treks, waterfalls, local food)
            - Collect booking enquiries with dates, guests and phone number
            - Email each enquiry to the owner and send an auto-reply to the guest
            - Show a map and how to reach by bus and car
Storage:    Netlify Forms (enquiries)
Tech stack: Astro, Netlify, Netlify Forms
```

---

## Example 988

**Intent:**
Need one system for our school canteen where children pay with ID card and parents top up money online

**Spec:**
```
Type:       Web application (cashless canteen)
Auth:       Parent login with email + password; canteen staff login at the counter
Data model: Student(id, name, class_section, card_uid, daily_limit, balance)
            Parent(id, name, email, phone)
            ParentStudent(parent_id -> Parent, student_id -> Student)
            TopUp(id, student_id -> Student, amount, razorpay_payment_id, created_at)
            Purchase(id, student_id -> Student, items, amount, created_at)
Features:   - Tap the student's RFID card at the counter to pay for items
            - Reject purchases above the balance or daily limit
            - Let parents top up the wallet online
            - Show parents what their child bought each day
            - Send a low-balance alert to parents
API:        REST
            POST /purchases
            POST /topups
            GET  /students/{id}/transactions
Storage:    PostgreSQL
Tech stack: Python, Django, Razorpay, USB RFID card reader (keyboard input)
```

---

## Example 989

**Intent:**
We're a small diagnostic lab and patients keep coming back just to collect their test reports, can they get them online?

**Spec:**
```
Type:       Web application (patient report portal)
Auth:       Patients log in with phone number + OTP; lab staff login with email + password
Data model: Patient(id, name, phone, dob)
            Order(id, patient_id -> Patient, sample_id, tests, collected_at, status)
            Report(id, order_id -> Order, pdf_url, uploaded_at, released)
Features:   - Upload the report PDF against a sample ID
            - Send an SMS with a secure link when the report is ready
            - Let patients view and download all their past reports
            - Hide reports until a pathologist releases them
            - Expire download links after 7 days
API:        REST
            POST /reports
            POST /reports/{id}/release
            GET  /patients/me/reports
Storage:    PostgreSQL (data), AWS S3 with signed URLs (PDFs)
Tech stack: Python, Django, AWS S3, MSG91 SMS API
```

---

## Example 990

**Intent:**
I have a 5-a-side football turf and want people to book hourly slots online instead of calling me at midnight

**Spec:**
```
Type:       Web application (slot booking)
Auth:       Customer login with phone + OTP; owner login with email + password
Data model: Court(id, name, sport)
            PriceRule(id, court_id -> Court, weekday, start_hour, end_hour, price)
            Booking(id, court_id -> Court, customer_phone, customer_name, date, start_hour, amount, payment_status)
Features:   - Show a grid of free and booked hourly slots for a date
            - Charge peak prices for evenings and weekends
            - Pay online to confirm the slot
            - Let the owner block slots for tournaments or maintenance
            - Send a WhatsApp or SMS confirmation after booking
API:        REST
            GET  /courts/{id}/slots?date={date}
            POST /bookings
            POST /payments/webhook
Storage:    Supabase (PostgreSQL)
Tech stack: Next.js, Supabase, Razorpay
```

---

## Example 991

**Intent:**
We run a fleet of 18 trucks and keep getting fined because an insurance, permit or fitness certificate expired without anyone noticing. I want one place to store all the documents for each truck, get alerts well before anything expires, and also log services and tyre changes. The office staff are not very technical so it must be simple.

**Spec:**
```
Type:       Web application (fleet compliance)
Auth:       Office staff login (email + password); owner has admin role
Data model: Truck(id, registration_no, model, year, driver_name)
            Document(id, truck_id -> Truck, type, number, issued_on, expires_on, file_url)
            ServiceLog(id, truck_id -> Truck, type, odometer_km, cost, workshop, date)
Features:   - Upload insurance, permit, fitness, PUC and tax documents per truck
            - Show a colour-coded list of documents expiring in 30, 15 and 7 days
            - Send email and WhatsApp alerts before each expiry
            - Log services, tyre changes and repair costs per truck
            - Show total maintenance cost per truck per year
API:        REST
            GET  /trucks
            POST /trucks/{id}/documents
            GET  /documents/expiring?days=30
            POST /trucks/{id}/services
Storage:    PostgreSQL (data), AWS S3 (document scans)
Tech stack: PHP, Laravel, Laravel Scheduler, AWS S3, WhatsApp Business Cloud API
```

---

## Example 992

**Intent:**
beauty parlour billing

**Spec:**
```
Type:       Desktop application (point of sale)
Auth:       Owner and staff login (PIN)
Data model: Service(id, name, category, price)
            Staff(id, name, commission_percent)
            Customer(id, name, phone)
            Bill(id, customer_id -> Customer, total, discount, payment_mode, created_at)
            BillItem(id, bill_id -> Bill, service_id -> Service, staff_id -> Staff, price)
Features:   - Create a bill by picking services and the staff who did them
            - Apply discounts and print a receipt
            - Calculate commission for each staff member
            - Show daily and monthly sales reports
            - Save customer visit history by phone number
Storage:    Local SQLite database
Tech stack: Electron, React, better-sqlite3
```

---

## Example 993

**Intent:**
school bell timer that rings the bell automaticaly from a pc for each period, diffrent timings on saturday

**Spec:**
```
Type:       Desktop application
Data model: Schedule(id, name, weekdays)
            BellTime(id, schedule_id -> Schedule, time, label, sound_file, duration_s)
            Holiday(id, date, reason)
Features:   - Create bell schedules for weekdays and Saturdays
            - Play the bell sound through the speakers at each set time
            - Skip bells on holidays from a holiday list
            - Ring the bell manually for emergencies or assemblies
            - Start automatically when the PC turns on and run in the system tray
Storage:    Local JSON file
Tech stack: Python, PySide6, pygame (audio), APScheduler
```

---

## Example 994

**Intent:**
We are NGO doing tree plantation in villages, want to track each sapling with photo and GPS and check if it survived after 6 months

**Spec:**
```
Type:       Mobile application (field app) + web dashboard
Auth:       Field volunteer login (phone + OTP); admin login for NGO staff
Data model: Site(id, name, village, district)
            Sapling(id, site_id -> Site, species, planted_on, lat, lng, photo_url, planted_by)
            Inspection(id, sapling_id -> Sapling, inspected_on, status, height_cm, photo_url)
Features:   - Register each sapling with species, photo and GPS location
            - Work offline in villages and sync when network is available
            - Schedule survival checks at 3, 6 and 12 months
            - Record inspection status (alive, dead, damaged) with a new photo
            - Show all saplings on a map with survival rate per site
            - Export reports for donors with photos and numbers
API:        REST
            POST /saplings
            POST /saplings/{id}/inspections
            GET  /sites/{id}/survival
Storage:    Firebase Firestore (offline persistence), Firebase Storage (photos)
Tech stack: Flutter, Firebase, Google Maps SDK
```

---

## Example 995

**Intent:**
Discord bot for my class server that reminds everyone about assignment deadlines

**Spec:**
```
Type:       Chatbot (Discord)
Auth:       Only members with the "Teacher" or "Class Rep" role can add assignments
Data model: Assignment(id, guild_id, subject, title, due_at, link, created_by)
            ReminderSetting(guild_id, channel_id, remind_hours_before)
Features:   - Add an assignment with a /assign slash command
            - List upcoming deadlines with /deadlines
            - Post reminders 3 days and 1 day before each deadline
            - Ping the class role on the due day
            - Remove assignments after the deadline passes
Storage:    SQLite
Tech stack: Python, discord.py, APScheduler
```

---

## Example 996

**Intent:**
spare parts shop inventory

**Spec:**
```
Type:       Web application (inventory)
Auth:       Owner and counter staff login (username + password, role-based)
Data model: Part(id, part_number, name, brand, compatible_models, rack_location, cost_price, sale_price, quantity, reorder_level)
            Supplier(id, name, phone)
            Purchase(id, supplier_id -> Supplier, part_id -> Part, quantity, price, date)
            Sale(id, part_id -> Part, quantity, price, date)
Features:   - Search parts by part number, name or vehicle model
            - Show the rack location of each part
            - Update stock on every purchase and sale
            - List parts below the reorder level by supplier
            - Show slow-moving parts not sold in 90 days
API:        REST
            GET  /parts?q={text}
            POST /purchases
            POST /sales
            GET  /reports/reorder
Storage:    MySQL
Tech stack: PHP, Laravel, Livewire
```

---

## Example 997

**Intent:**
I run a small language school and want new students to take a placement test online so we put them in the right level

**Spec:**
```
Type:       Web application (online placement test)
Auth:       Candidates register with name and email; staff login for results
Data model: Candidate(id, name, email, phone, language)
            Question(id, language, section, level, text, options, correct_option)
            Attempt(id, candidate_id -> Candidate, started_at, finished_at, score, level_result)
            Answer(id, attempt_id -> Attempt, question_id -> Question, chosen_option)
Features:   - Run a timed test with grammar, vocabulary and reading sections
            - Make questions harder or easier based on previous answers
            - Map the final score to a CEFR level (A1 to C1)
            - Email the result to the candidate and the school
            - Let staff see all results and add a speaking test note
API:        REST
            POST /attempts
            GET  /attempts/{id}/next-question
            POST /attempts/{id}/answers
            GET  /admin/attempts
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 998

**Intent:**
app for my small bakery to know how much bread to bake tomorrow based on past sales and the weather

**Spec:**
```
Type:       Data analysis script (forecasting)
Features:   - Load daily sales per product from the POS export
            - Add weekday, holiday and weather data for each day
            - Train a simple forecasting model per product
            - Predict tomorrow's quantity for each product with a safety margin
            - Save the baking list as a printable PDF
            - Compare yesterday's forecast with actual sales to track accuracy
Input:      CSV export of daily sales with columns: date, product, quantity_sold, quantity_wasted
Tech stack: Python, pandas, scikit-learn, Open-Meteo API, ReportLab
```

---

## Example 999

**Intent:**
Kindly create website for our cricket academy, showing batches, coaches and online admission form with fee payment

**Spec:**
```
Type:       Website with admin panel
Auth:       Admin login for academy staff
Data model: Coach(id, name, photo_url, experience, certifications)
            Batch(id, name, age_group, days, timing, coach_id -> Coach, fee_per_month, seats)
            Admission(id, batch_id -> Batch, player_name, dob, parent_name, phone, playing_role, payment_status)
Features:   - Show the academy, facilities and coaches with photos
            - List batches by age group with timings and fees
            - Fill an admission form and pay the registration fee online
            - Show remaining seats in each batch
            - Let staff view and export admissions to Excel
API:        REST
            GET  /batches
            POST /admissions
            POST /payments/webhook
            GET  /admin/admissions/export
Storage:    MySQL
Tech stack: PHP, Laravel, Razorpay, Laravel Excel
```

---

## Example 1000

**Intent:**
Guests at our little bed & breakfast always ask for the wifi password, checkout time and where to eat, could we have a digital guidebook they open on their phone?

**Spec:**
```
Type:       Website (mobile digital guidebook)
Auth:       Owner login to edit content; guests open a link or QR code without login
Data model: Section(id, title, icon, sort_order)
            Entry(id, section_id -> Section, title, body, map_url, photo_url)
Features:   - Show wifi details, check-in and checkout times and house rules
            - List recommended restaurants, sights and shops with map links
            - Show emergency numbers and the host's contact button
            - Let the owner update content from a simple editor
            - Print a QR code for each room that opens the guidebook
            - Work offline after the first visit
Storage:    Firebase Firestore
Tech stack: SvelteKit, Firebase, PWA service worker, qrcode
```
