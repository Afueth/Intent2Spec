## Example 1

**Intent:**
case tracker for my small law firm

**Spec:**
```
Type:       Web application (legal case management)
Auth:       Email + password login with roles (partner, associate, paralegal)
Data model: Client(id, name, email, phone)
            Case(id, client_id -> Client, title, case_number, status, opened_at)
            Deadline(id, case_id -> Case, description, due_date, done)
            Note(id, case_id -> Case, author_id -> User, body, created_at)
            User(id, name, email, password_hash, role)
Features:   - Create and update cases linked to clients
            - Track court deadlines with a calendar view
            - Email reminders 7 days and 1 day before each deadline
            - Add internal notes to a case
            - Filter cases by status and assigned lawyer
API:        REST
            GET  /cases
            POST /cases
            GET  /cases/{id}/deadlines
            POST /cases/{id}/notes
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 2

**Intent:**
I run a cleaning company with about 15 cleaners. I want a website where I can assign jobs to cleaners and they can see their schedule for the day on their phone.

**Spec:**
```
Type:       Web application (field job scheduling)
Auth:       Email + password login; roles: manager, cleaner
Data model: Cleaner(id, name, phone, email, password_hash)
            Property(id, client_name, address, access_notes)
            Job(id, property_id -> Property, cleaner_id -> Cleaner, date, start_time, duration_min, status)
Features:   - Create cleaning jobs and assign them to a cleaner
            - Show each cleaner a mobile-friendly list of today's jobs
            - Let cleaners mark a job as started and finished
            - Show the manager a weekly schedule grid per cleaner
            - Warn when a cleaner is double-booked
API:        REST
            GET  /jobs?date={date}
            POST /jobs
            PATCH /jobs/{id}/status
            GET  /cleaners/{id}/schedule
Storage:    PostgreSQL
Tech stack: Node.js, Express, React (responsive layout)
```

---

## Example 3

**Intent:**
driving school website where students can book lessons with an instructor

**Spec:**
```
Type:       Web application (lesson booking)
Auth:       Email + password login; roles: student, instructor, admin
Data model: Instructor(id, name, car_type, transmission)
            Student(id, name, email, licence_number, lessons_taken)
            Slot(id, instructor_id -> Instructor, start_at, end_at, is_booked)
            Lesson(id, slot_id -> Slot, student_id -> Student, pickup_address, notes)
Features:   - Show available slots per instructor (manual or automatic car)
            - Book and cancel lessons up to 24 hours before
            - Record instructor notes on student progress after each lesson
            - Track the number of lessons each student has taken
            - Send SMS reminders the day before a lesson
API:        REST
            GET  /instructors/{id}/slots
            POST /lessons
            DELETE /lessons/{id}
            POST /lessons/{id}/notes
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Twilio (SMS)
```

---

## Example 4

**Intent:**
vet clinic needs to send reminders for pet vaccinations

**Spec:**
```
Type:       Web application (veterinary vaccination reminders)
Auth:       Staff email + password login
Data model: Owner(id, name, email, phone)
            Pet(id, owner_id -> Owner, name, species, breed, birth_date)
            Vaccination(id, pet_id -> Pet, vaccine_name, given_on, next_due_on)
Features:   - Record vaccinations given to each pet
            - Calculate the next due date from the vaccine interval
            - Email owners 2 weeks before a vaccination is due
            - List all pets with overdue vaccinations
            - Search pets by name or owner phone number
API:        REST
            GET  /pets?search={q}
            POST /pets/{id}/vaccinations
            GET  /vaccinations/overdue
Storage:    PostgreSQL
Tech stack: Python, Flask, Celery (scheduled emails), SendGrid
```

---

## Example 5

**Intent:**
My bakery takes custom cake orders over the phone and we lose track of them. Can we have a simple order page customers fill in themselves, with pickup date and the design they want?

**Spec:**
```
Type:       Web application (custom order intake)
Auth:       Staff login (email + password); customers order without an account
Data model: CakeOrder(id, customer_name, phone, email, pickup_date, size, flavour, filling, design_notes, reference_image_url, status)
            BlockedDate(id, date, reason)
Features:   - Let customers submit a cake order with size, flavour and design notes
            - Upload a reference photo for the design
            - Block pickup dates that are fully booked
            - Show staff a list of orders sorted by pickup date
            - Update order status (new, confirmed, baking, ready, collected)
API:        REST
            POST /orders
            GET  /orders?from={date}
            PATCH /orders/{id}/status
            GET  /blocked-dates
Storage:    PostgreSQL, S3 (reference images)
Tech stack: Next.js, Prisma
```

---

## Example 6

**Intent:**
print shop quote calculator

**Spec:**
```
Type:       Web application (price quoting)
Auth:       Admin login for editing prices
Data model: Product(id, name, base_price)
            PaperOption(id, name, price_per_sheet)
            FinishOption(id, name, price_per_unit)
            Quote(id, product_id -> Product, quantity, paper_id -> PaperOption, finish_id -> FinishOption, total, email, created_at)
Features:   - Let customers pick product, size, paper, quantity and finish
            - Calculate the price instantly with quantity discounts
            - Email the quote as a PDF to the customer
            - Let admins edit prices and discount tiers
API:        REST
            GET  /products
            POST /quotes
            PUT  /admin/prices
Storage:    PostgreSQL
Tech stack: Vue.js, Node.js, Express, PDFKit
```

---

## Example 7

**Intent:**
we are a brewery and want to track our beer batches from brewing to kegging, with the gravity readings and tank they are in

**Spec:**
```
Type:       Web application (brewery production tracking)
Auth:       Email + password login for brewery staff
Data model: Recipe(id, name, style, target_og, target_fg)
            Tank(id, name, capacity_l, type)
            Batch(id, recipe_id -> Recipe, tank_id -> Tank, brew_date, volume_l, status)
            GravityReading(id, batch_id -> Batch, gravity, temperature_c, taken_at)
Features:   - Create batches from recipes and assign them to a tank
            - Log gravity and temperature readings over time
            - Chart fermentation progress per batch
            - Calculate ABV from original and current gravity
            - Show which tanks are free or occupied
API:        REST
            GET  /batches
            POST /batches
            POST /batches/{id}/readings
            GET  /tanks
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, Chart.js
```

---

## Example 8

**Intent:**
florist delivery route planner

**Spec:**
```
Type:       Web application (delivery planning)
Auth:       Email + password login for shop staff
Data model: Order(id, recipient_name, address, lat, lng, delivery_date, time_window, card_message)
            Driver(id, name, phone)
            Route(id, driver_id -> Driver, date, stop_order_json)
Features:   - List the day's flower deliveries on a map
            - Optimise the stop order for each driver
            - Respect delivery time windows
            - Print a route sheet with card messages
            - Mark deliveries as delivered with a photo
API:        REST
            GET  /orders?date={date}
            POST /routes/optimize
            PATCH /orders/{id}/delivered
Storage:    PostgreSQL with PostGIS
Tech stack: Node.js, Express, React, Google Maps Directions API
```

---

## Example 9

**Intent:**
i do wedding photography and want a site where couples can see there photos and pick favourites for the album

**Spec:**
```
Type:       Web application (client photo gallery)
Auth:       Private gallery link with a password per couple; photographer admin login
Data model: Gallery(id, couple_names, event_date, password_hash, expires_at)
            Photo(id, gallery_id -> Gallery, file_url, thumbnail_url, taken_at)
            Selection(id, gallery_id -> Gallery, photo_id -> Photo, created_at)
Features:   - Upload a full wedding shoot to a private gallery
            - Generate web-size thumbnails automatically
            - Let the couple mark favourites for the album, up to a set limit
            - Download selected photos in full resolution
            - Show the photographer the final selection list
API:        REST
            POST /galleries/{id}/photos
            GET  /galleries/{id}
            POST /galleries/{id}/selections
            GET  /galleries/{id}/selections
Storage:    PostgreSQL, AWS S3 (photos)
Tech stack: Python, Django, Pillow, Vue.js
```

---

## Example 10

**Intent:**
Coworking space: members book meeting rooms and desks, and we bill them monthly.

**Spec:**
```
Type:       Web application (coworking management)
Auth:       Email + password login; roles: member, admin
Data model: Member(id, name, email, company, plan_id -> Plan)
            Plan(id, name, monthly_price, included_room_hours)
            Resource(id, name, type, hourly_rate)
            Booking(id, member_id -> Member, resource_id -> Resource, start_at, end_at)
Features:   - Book desks and meeting rooms on a calendar
            - Prevent overlapping bookings
            - Count room hours used against the plan allowance
            - Charge members monthly, including extra hours
            - Show admins occupancy per day
API:        REST
            GET  /resources/{id}/availability
            POST /bookings
            GET  /members/{id}/usage
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, React, Stripe Billing
```

---

## Example 11

**Intent:**
Hello, I have a laundromat with 20 machine. I want customer can see on website which machine is free now, so they don't come for nothing.

**Spec:**
```
Type:       IoT system (machine availability display)
Data model: Machine(id, number, type, status, cycle_ends_at)
            StatusEvent(id, machine_id -> Machine, status, recorded_at)
Features:   - Read each washer and dryer's power use with a smart plug
            - Mark a machine as busy or free from its power draw
            - Estimate when a running cycle will finish
            - Show a public web page with free machines and wait times
            - Keep daily usage statistics per machine
API:        REST
            GET  /machines
            POST /machines/{id}/status
Storage:    SQLite
Tech stack: Raspberry Pi, Shelly smart plugs, Python, MQTT, Flask
```

---

## Example 12

**Intent:**
B2B wholesale ordering portal for our shop customers

**Spec:**
```
Type:       Web application (B2B ordering portal)
Auth:       Email + password login per business account; admin approves new accounts
Data model: Account(id, company_name, vat_number, price_tier, approved)
            Product(id, sku, name, unit, case_size, stock)
            TierPrice(id, product_id -> Product, tier, price)
            Order(id, account_id -> Account, status, delivery_date, total)
            OrderLine(id, order_id -> Order, product_id -> Product, cases)
Features:   - Show each account its own price tier
            - Order in whole cases with a minimum order value
            - Reorder a previous order with one click
            - Choose a delivery date from available delivery days
            - Export confirmed orders to CSV for the warehouse
API:        REST
            GET  /products
            POST /orders
            POST /orders/{id}/reorder
            GET  /admin/orders/export
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Livewire
```

---

## Example 13

**Intent:**
So my dad owns a small construction company and he still does everything on paper. What I'd like is something where his foremen can write the daily site diary — who was on site, the weather, what got done, any problems — and add photos, and then he can look at it from the office.

**Spec:**
```
Type:       Web application (construction site diary)
Auth:       Email + password login; roles: owner, foreman
Data model: Site(id, name, address, client_name)
            DiaryEntry(id, site_id -> Site, foreman_id -> User, date, weather, work_done, issues)
            Attendance(id, entry_id -> DiaryEntry, worker_name, hours)
            Photo(id, entry_id -> DiaryEntry, url, caption)
            User(id, name, email, password_hash, role)
Features:   - Fill in a daily diary per site from a phone
            - Record workers on site and their hours
            - Attach photos with captions
            - Let the owner browse entries by site and date
            - Export a site's diary as a PDF
API:        REST
            GET  /sites
            POST /sites/{id}/diary
            POST /diary/{id}/photos
            GET  /sites/{id}/diary.pdf
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, WeasyPrint
```

---

## Example 14

**Intent:**
tutoring centre site to match students with tutors by subject and level

**Spec:**
```
Type:       Web application (tutor matching)
Auth:       Email + password login; roles: parent, tutor, admin
Data model: Tutor(id, name, bio, hourly_rate)
            TutorSubject(id, tutor_id -> Tutor, subject, level)
            Student(id, parent_id -> User, name, school_year)
            Session(id, tutor_id -> Tutor, student_id -> Student, start_at, duration_min, status)
Features:   - Search tutors by subject, level and price
            - Show tutor profiles with weekly availability
            - Book a trial session
            - Let tutors write a short report after each session
            - Show parents a history of sessions and reports
API:        REST
            GET  /tutors?subject={s}&level={l}
            POST /sessions
            POST /sessions/{id}/report
Storage:    PostgreSQL
Tech stack: Next.js, Supabase
```

---

## Example 15

**Intent:**
equipment checkout for our film rental warehouse, need barcode scanning

**Spec:**
```
Type:       Web application (equipment checkout)
Auth:       Staff email + password login
Data model: Item(id, barcode, name, category, serial_number, condition)
            Customer(id, name, company, phone)
            Checkout(id, customer_id -> Customer, out_at, due_back_at, returned_at)
            CheckoutItem(id, checkout_id -> Checkout, item_id -> Item)
Features:   - Scan item barcodes with the device camera to add them to a checkout
            - Record checkout and expected return dates
            - Scan items back in and note damage
            - Show all items currently out and overdue
            - Print a packing list for each checkout
API:        REST
            GET  /items/by-barcode/{code}
            POST /checkouts
            POST /checkouts/{id}/return
            GET  /checkouts/overdue
Storage:    PostgreSQL
Tech stack: React, QuaggaJS (barcode scanning), Node.js, Express
```

---

## Example 16

**Intent:**
fleet maintenance tracker for our 30 delivery vans

**Spec:**
```
Type:       Web application (fleet maintenance)
Auth:       Email + password login; roles: fleet manager, driver
Data model: Vehicle(id, registration, make, model, mileage, next_service_km, mot_due)
            ServiceRecord(id, vehicle_id -> Vehicle, date, mileage, work_done, cost, garage)
            DefectReport(id, vehicle_id -> Vehicle, driver_id -> User, description, severity, resolved)
Features:   - Log service history and costs per van
            - Alert when a van is near its service mileage or MOT date
            - Let drivers report defects from their phone
            - Show total maintenance cost per vehicle per year
            - List vans that are off the road
API:        REST
            GET  /vehicles
            POST /vehicles/{id}/services
            POST /vehicles/{id}/defects
            GET  /alerts
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 17

**Intent:**
accountants office, clients need to upload their receipts and bank statements to us every month instead of emailing

**Spec:**
```
Type:       Web application (client document portal)
Auth:       Email + password login with two-factor authentication
Data model: Client(id, business_name, email, accountant_id -> User)
            DocumentRequest(id, client_id -> Client, period, description, status)
            Document(id, request_id -> DocumentRequest, file_url, filename, uploaded_at)
            User(id, name, email, role)
Features:   - Create monthly document requests for each client
            - Let clients upload receipts and statements against a request
            - Send reminder emails for missing documents
            - Show accountants which clients are complete for the month
            - Encrypt stored files at rest
API:        REST
            GET  /requests
            POST /requests/{id}/documents
            GET  /admin/completion?period={yyyy-mm}
Storage:    PostgreSQL, S3 with server-side encryption
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 18

**Intent:**
marina berth booking

**Spec:**
```
Type:       Web application (marina berth booking)
Auth:       Email + password login for boat owners; harbour master admin
Data model: Berth(id, pontoon, number, max_length_m, max_beam_m, has_power)
            Boat(id, owner_id -> User, name, length_m, beam_m)
            BerthBooking(id, berth_id -> Berth, boat_id -> Boat, arrive_on, depart_on, total_price)
Features:   - Search free berths that fit the boat's length and beam
            - Book visitor berths by the night
            - Price stays by boat length and season
            - Show the harbour master a pontoon map of occupancy
            - Take card payment when booking
API:        REST
            GET  /berths/available?from={d}&to={d}&length={m}
            POST /bookings
            GET  /admin/occupancy?date={d}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Svelte, Stripe
```

---

## Example 19

**Intent:**
we're a small farm and want to sell veg boxes online that people subscribe to weekly and pick up at the farm or get delivered

**Spec:**
```
Type:       Web application (farm box subscriptions)
Auth:       Email + password customer accounts; farm admin login
Data model: BoxType(id, name, size, weekly_price)
            Subscription(id, customer_id -> Customer, box_type_id -> BoxType, fulfilment, status, paused_until)
            Customer(id, name, email, address, phone)
            WeeklyContents(id, week_start, box_type_id -> BoxType, items_text)
Features:   - Subscribe to a weekly veg box with pickup or delivery
            - Pause or skip a week
            - Publish what is in this week's boxes
            - Charge subscribers weekly
            - Print packing and delivery lists for harvest day
API:        REST
            GET  /box-types
            POST /subscriptions
            POST /subscriptions/{id}/pause
            GET  /admin/packing-list?week={date}
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe Subscriptions
```

---

## Example 20

**Intent:**
funeral home wants an online memorial page for each person where family and friends can leave condolences and see service details

**Spec:**
```
Type:       Web application (online memorials)
Auth:       Staff login; visitors post without an account (moderated)
Data model: Memorial(id, full_name, born_on, died_on, obituary, photo_url, slug)
            Service(id, memorial_id -> Memorial, type, starts_at, venue, address)
            Condolence(id, memorial_id -> Memorial, author_name, message, approved, created_at)
Features:   - Create a memorial page with photo and obituary
            - Show service times and venue with a map
            - Let visitors leave condolence messages
            - Moderate messages before they appear
            - Livestream link for the service when available
API:        REST
            GET  /memorials/{slug}
            POST /memorials/{id}/condolences
            PATCH /condolences/{id}/approve
Storage:    PostgreSQL
Tech stack: WordPress with a custom plugin, PHP
```

---

## Example 21

**Intent:**
quality inspection checklist app for our factory, built with Flutter

**Spec:**
```
Type:       Mobile application with backend (quality inspections)
Auth:       Email + password login for inspectors and supervisors
Data model: ChecklistTemplate(id, name, product_line)
            CheckItem(id, template_id -> ChecklistTemplate, question, type, tolerance_min, tolerance_max)
            Inspection(id, template_id -> ChecklistTemplate, inspector_id -> User, batch_number, result, created_at)
            Answer(id, inspection_id -> Inspection, item_id -> CheckItem, value, passed, photo_url)
Features:   - Run an inspection from a checklist template
            - Record measurements and check them against tolerances
            - Attach photos of defects
            - Mark the batch as passed or failed automatically
            - Show supervisors a daily pass rate per product line
API:        REST
            GET  /templates
            POST /inspections
            GET  /reports/pass-rate
Storage:    PostgreSQL (backend), SQLite (offline on device)
Tech stack: Flutter, Dart, Python, FastAPI
```

---

## Example 22

**Intent:**
car dealership website showing used cars in stock with filters

**Spec:**
```
Type:       Web application (vehicle listings)
Auth:       Staff login to manage stock
Data model: Car(id, make, model, year, mileage, fuel, transmission, price, status, description)
            CarPhoto(id, car_id -> Car, url, position)
            Enquiry(id, car_id -> Car, name, email, phone, message, created_at)
Features:   - List cars with filters for make, price, year, mileage and fuel
            - Show a detail page with a photo gallery
            - Send an enquiry or book a test drive for a car
            - Mark cars as reserved or sold
            - Let staff reorder photos by dragging
API:        REST
            GET  /cars?make={m}&max_price={p}
            GET  /cars/{id}
            POST /cars/{id}/enquiries
Storage:    PostgreSQL, Cloudinary (photos)
Tech stack: Next.js, TypeScript, Prisma
```

---

## Example 23

**Intent:**
dental lab, dentists send us cases (crowns, bridges) and we need to track each case through production and when its due back

**Spec:**
```
Type:       Web application (dental lab case tracking)
Auth:       Email + password login; roles: dentist, technician, lab admin
Data model: Practice(id, name, address)
            Case(id, practice_id -> Practice, patient_ref, restoration_type, shade, teeth, due_date, status)
            Stage(id, case_id -> Case, name, technician_id -> User, completed_at)
            Attachment(id, case_id -> Case, file_url, kind)
Features:   - Let dentists submit cases with prescription details and scan files
            - Move cases through production stages (model, design, milling, finishing)
            - Show cases due this week in date order
            - Notify the dentist when a case ships
            - Generate an invoice per practice per month
API:        REST
            POST /cases
            PATCH /cases/{id}/stage
            GET  /cases?due_before={date}
            GET  /practices/{id}/invoice?month={m}
Storage:    PostgreSQL, S3 (STL scan files)
Tech stack: Python, Django, React
```

---

## Example 24

**Intent:**
wedding planner, i need to keep every couple's vendors, budget and timeline in one place and share it with them

**Spec:**
```
Type:       Web application (wedding planning)
Auth:       Email + password login; planner owns events, couples get a shared login
Data model: Wedding(id, couple_names, date, venue, total_budget)
            Vendor(id, wedding_id -> Wedding, category, name, contact, quoted_price, deposit_paid)
            BudgetItem(id, wedding_id -> Wedding, label, estimated, actual)
            TimelineItem(id, wedding_id -> Wedding, time, description, owner)
Features:   - Add vendors per wedding with quotes and deposit status
            - Track budget estimated vs actual spend
            - Build a day-of timeline
            - Share a read-only view with the couple
            - Export the timeline as a PDF for vendors
API:        REST
            GET  /weddings/{id}
            POST /weddings/{id}/vendors
            POST /weddings/{id}/timeline
            GET  /weddings/{id}/timeline.pdf
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Puppeteer (PDF)
```

---

## Example 25

**Intent:**
purchase requests that need manager approval before ordering

**Spec:**
```
Type:       Web application (procurement approvals)
Auth:       Single sign-on with Microsoft Entra ID
Data model: PurchaseRequest(id, requester_id -> User, supplier, description, amount, cost_centre, status)
            Approval(id, request_id -> PurchaseRequest, approver_id -> User, decision, comment, decided_at)
            User(id, name, email, manager_id -> User, approval_limit)
Features:   - Submit a purchase request with quote attachment
            - Route the request to the requester's manager
            - Escalate to a director when the amount is above the manager's limit
            - Notify the requester of approval or rejection
            - Generate a purchase order number when approved
API:        REST
            POST /requests
            GET  /approvals/pending
            POST /requests/{id}/decision
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, React, Microsoft Graph (email)
```

---

## Example 26

**Intent:**
The health and safety inspector comes every year and every year we scramble to find our fire extinguisher checks, ladder inspections and training certificates. I'd love a system that reminds us when each check is due and keeps the records.

**Spec:**
```
Type:       Web application (compliance tracking)
Auth:       Email + password login; roles: admin, staff
Data model: ComplianceItem(id, name, category, location, frequency_days, last_done_on, next_due_on)
            CheckRecord(id, item_id -> ComplianceItem, done_by, done_on, result, notes, file_url)
            Certificate(id, employee_name, course, issued_on, expires_on, file_url)
Features:   - Register recurring checks with a frequency
            - Record each completed check with a signed form or photo
            - Email reminders before checks and certificates expire
            - Show a dashboard of overdue and upcoming items
            - Export an audit pack as a ZIP of records
API:        REST
            GET  /items/due
            POST /items/{id}/records
            POST /certificates
            GET  /audit-pack
Storage:    PostgreSQL, S3 (documents)
Tech stack: Python, Flask, Bootstrap
```

---

## Example 27

**Intent:**
plumbers need to fill a job sheet on site and get the customer to sign it on the tablet

**Spec:**
```
Type:       Web application (job sheets with e-signature)
Auth:       Email + password login for engineers and office staff
Data model: Customer(id, name, address, phone)
            Job(id, customer_id -> Customer, engineer_id -> User, date, description, status)
            JobSheet(id, job_id -> Job, work_done, parts_used, labour_hours, signature_url, signed_at)
Features:   - Fill in a job sheet on a tablet on site
            - List parts used with prices
            - Capture the customer's signature on screen
            - Email the signed job sheet as a PDF to the customer
            - Send completed sheets to the office for invoicing
API:        REST
            GET  /jobs/today
            POST /jobs/{id}/sheet
            POST /jobs/{id}/sheet/sign
Storage:    PostgreSQL, S3 (signatures and PDFs)
Tech stack: React (PWA), signature_pad, Node.js, Express
```

---

## Example 28

**Intent:**
asset register for IT equipment in our office - laptops, monitors, phones, who has what

**Spec:**
```
Type:       Web application (IT asset management)
Auth:       Single sign-on with Google Workspace
Data model: Asset(id, asset_tag, type, model, serial_number, purchase_date, warranty_until, status)
            Employee(id, name, email, department)
            Assignment(id, asset_id -> Asset, employee_id -> Employee, assigned_on, returned_on)
Features:   - Register assets with tag, serial and warranty
            - Assign and return assets to employees
            - Show everything an employee currently has
            - Alert before warranties expire
            - Print QR code labels for asset tags
API:        REST
            GET  /assets
            POST /assets/{id}/assign
            POST /assets/{id}/return
            GET  /employees/{id}/assets
Storage:    PostgreSQL
Tech stack: Python, Django, qrcode library
```

---

## Example 29

**Intent:**
web app for a pottery studio, people book wheel throwing classes and buy firing for their pieces

**Spec:**
```
Type:       Web application (studio classes and firing)
Auth:       Email + password login for students; studio admin
Data model: ClassSession(id, title, teacher, starts_at, capacity, price)
            Enrollment(id, session_id -> ClassSession, student_id -> User, paid)
            FiringTicket(id, student_id -> User, piece_description, kiln_type, size_cm, price, status)
Features:   - Book a place in wheel-throwing classes
            - Show remaining spaces per class
            - Buy firing tickets priced by piece size
            - Track pieces through bisque and glaze firing
            - Notify students when pieces are ready to collect
API:        REST
            GET  /classes
            POST /classes/{id}/enroll
            POST /firing-tickets
            PATCH /firing-tickets/{id}/status
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Svelte, Stripe Checkout
```

---

## Example 30

**Intent:**
locksmith callout log

**Spec:**
```
Type:       Web application (callout log)
Auth:       Email + password login
Data model: Callout(id, customer_name, phone, address, problem, received_at, arrived_at, completed_at, price, paid)
            Technician(id, name, phone)
Features:   - Log emergency callouts with time received
            - Assign a technician and record arrival time
            - Record the price and payment method
            - Show average response time per week
API:        REST
            GET  /callouts
            POST /callouts
            PATCH /callouts/{id}
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 31

**Intent:**
We sell firewood and kindling to local houses. Want to take orders online, with delivery only on Tuesdays and Fridays, and pay by card.

**Spec:**
```
Type:       Web application (online ordering with delivery days)
Auth:       Customers order as guests; admin login
Data model: Product(id, name, unit, price, in_stock)
            Order(id, customer_name, phone, address, postcode, delivery_date, total, paid, status)
            OrderItem(id, order_id -> Order, product_id -> Product, quantity)
            Postcode(id, prefix, delivery_fee)
Features:   - Order logs and kindling by the bag or crate
            - Offer only Tuesday and Friday delivery dates
            - Check the postcode is in the delivery area and add its fee
            - Pay by card at checkout
            - Print each delivery day's load list
API:        REST
            GET  /products
            GET  /delivery-dates
            POST /orders
Storage:    PostgreSQL
Tech stack: Node.js, Express, EJS, Stripe
```

---

## Example 32

**Intent:**
I have a small gallery and artists leave works on consignment. I need to know which pieces are in the gallery, which sold and how much I owe each artist after commission.

**Spec:**
```
Type:       Web application (consignment tracking)
Auth:       Gallery staff login; artists can log in to see their own works
Data model: Artist(id, name, email, commission_rate)
            Artwork(id, artist_id -> Artist, title, medium, price, received_on, status)
            Sale(id, artwork_id -> Artwork, sold_on, sale_price)
            Payout(id, artist_id -> Artist, amount, paid_on)
Features:   - Register consigned works when they arrive
            - Mark works as sold or returned
            - Calculate each artist's earnings after commission
            - Record payouts and show the balance owed
            - Let artists see their works and sales
API:        REST
            GET  /artworks?status={s}
            POST /artworks/{id}/sale
            GET  /artists/{id}/balance
            POST /payouts
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 33

**Intent:**
scaffolding company needs to know where all our scaffold parts are, which site has how many tubes and boards

**Spec:**
```
Type:       Web application (stock across job sites)
Auth:       Email + password login for yard and site managers
Data model: ComponentType(id, name, unit_weight_kg)
            Location(id, name, type, address)
            StockLevel(id, component_id -> ComponentType, location_id -> Location, quantity)
            Transfer(id, from_id -> Location, to_id -> Location, created_at, delivery_note_no)
            TransferLine(id, transfer_id -> Transfer, component_id -> ComponentType, quantity)
Features:   - Show quantities of each component at the yard and each site
            - Record deliveries and collections as transfers
            - Print delivery notes with total weight
            - Flag sites with stock still out after the job ends
API:        REST
            GET  /locations/{id}/stock
            POST /transfers
            GET  /transfers/{id}/note
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Vue.js
```

---

## Example 34

**Intent:**
mi empresa de mudanzas... sorry, my moving company need a form online where people put the rooms and things and we give a price estimate

**Spec:**
```
Type:       Web application (moving quote estimator)
Auth:       Admin login for the company
Data model: QuoteRequest(id, name, email, phone, from_address, to_address, move_date, distance_km, total_volume_m3, estimate)
            InventoryItem(id, request_id -> QuoteRequest, item_type, room, quantity)
            ItemType(id, name, volume_m3)
Features:   - Let customers list items room by room from a catalogue
            - Calculate total volume and the van size needed
            - Calculate distance between addresses
            - Produce a price estimate from volume, distance and floors
            - Send the request to the office for a final quote
API:        REST
            GET  /item-types
            POST /quote-requests
            GET  /admin/quote-requests
Storage:    PostgreSQL
Tech stack: Python, Django, Google Distance Matrix API
```

---

## Example 35

**Intent:**
online waiver form for our climbing wall

**Spec:**
```
Type:       Web application (digital waivers)
Auth:       Staff login; visitors sign without an account
Data model: Waiver(id, full_name, birth_date, email, emergency_contact, signature_url, signed_at, guardian_name)
            WaiverVersion(id, text, effective_from)
Features:   - Show the current waiver text and collect a drawn signature
            - Require a parent or guardian signature for under-18s
            - Store which waiver version was signed
            - Let front desk staff search waivers by name
            - Flag waivers older than one year as expired
API:        REST
            GET  /waiver/current
            POST /waivers
            GET  /waivers?name={q}
Storage:    PostgreSQL, S3 (signatures)
Tech stack: Svelte, Node.js, Express
```

---

## Example 36

**Intent:**
a timesheet thing for my electricians where they log hours per job so i can bill the customer right

**Spec:**
```
Type:       Web application (job timesheets)
Auth:       Email + password login; roles: owner, electrician
Data model: Job(id, customer_name, address, hourly_rate, status)
            TimeEntry(id, job_id -> Job, worker_id -> User, date, hours, description)
            Material(id, job_id -> Job, description, cost)
Features:   - Log hours per job from a phone
            - Add materials bought for the job
            - Show total labour and materials per job
            - Lock entries once the job is invoiced
            - Export a job summary for the invoice
API:        REST
            POST /jobs/{id}/time
            POST /jobs/{id}/materials
            GET  /jobs/{id}/summary
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 37

**Intent:**
Make an Airtable-style board for our recording studio sessions, but in Django please

**Spec:**
```
Type:       Web application (studio session scheduling)
Auth:       Email + password login for engineers and admin
Data model: Room(id, name, hourly_rate)
            Engineer(id, name, email)
            Artist(id, name, contact_email)
            StudioSession(id, room_id -> Room, engineer_id -> Engineer, artist_id -> Artist, start_at, end_at, status, notes)
Features:   - Show sessions in a sortable, filterable table view
            - Edit fields inline in the table
            - Group sessions by room or engineer
            - Prevent double-booking a room or engineer
            - Calculate session cost from room rate and hours
API:        REST
            GET  /sessions?group_by={field}
            PATCH /sessions/{id}
            POST /sessions
Storage:    PostgreSQL
Tech stack: Python, Django, Django REST Framework, AG Grid
```

---

## Example 38

**Intent:**
pest control company: technicians record what they found and what chemical they used at each visit, for legal records

**Spec:**
```
Type:       Web application (pest control service records)
Auth:       Email + password login for technicians and office
Data model: Site(id, client_name, address, contract_type)
            Visit(id, site_id -> Site, technician_id -> User, visited_on, findings, recommendations)
            TreatmentUse(id, visit_id -> Visit, product_name, batch_no, quantity, area_treated)
            BaitStation(id, site_id -> Site, code, location_desc)
Features:   - Record findings and treatments at each visit
            - Log the product, batch and amount used for compliance
            - Track bait station checks by station code
            - Email a visit report to the client
            - Export pesticide usage for a date range
API:        REST
            POST /sites/{id}/visits
            POST /visits/{id}/treatments
            GET  /reports/usage?from={d}&to={d}
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, React
```

---

## Example 39

**Intent:**
supplier price comparison for our restaurant group purchasing team

**Spec:**
```
Type:       Web application (supplier price comparison)
Auth:       Email + password login for the purchasing team
Data model: Supplier(id, name, contact_email)
            Item(id, name, unit, category)
            PriceQuote(id, supplier_id -> Supplier, item_id -> Item, price, valid_from, valid_to)
Features:   - Import supplier price lists from CSV
            - Show the cheapest current supplier per item
            - Chart price changes over time per item
            - Alert when an item's price rises more than 10%
API:        REST
            POST /suppliers/{id}/price-lists
            GET  /items/{id}/prices
            GET  /items/cheapest
Storage:    PostgreSQL
Tech stack: Python, FastAPI, pandas, React, Recharts
```

---

## Example 40

**Intent:**
kennel boarding bookings

**Spec:**
```
Type:       Web application (pet boarding reservations)
Auth:       Email + password login for owners; staff admin
Data model: Dog(id, owner_id -> User, name, breed, weight_kg, vaccinated_until, feeding_notes)
            Kennel(id, number, size)
            Stay(id, dog_id -> Dog, kennel_id -> Kennel, check_in, check_out, price, status)
Features:   - Book a stay for one or more dogs
            - Check kennel availability by size
            - Refuse bookings if vaccination is out of date
            - Show staff today's arrivals, departures and feeding notes
API:        REST
            GET  /availability?from={d}&to={d}&size={s}
            POST /stays
            GET  /admin/today
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 41

**Intent:**
estate agent wants viewings booked online for properties and feedback from people after viewing

**Spec:**
```
Type:       Web application (property viewings)
Auth:       Agent login; buyers book with email verification
Data model: Property(id, address, price, bedrooms, agent_id -> User, status)
            ViewingSlot(id, property_id -> Property, start_at, is_booked)
            Viewing(id, slot_id -> ViewingSlot, buyer_name, email, phone)
            Feedback(id, viewing_id -> Viewing, rating, comments, interested)
Features:   - Publish viewing slots per property
            - Let buyers book a slot and confirm by email
            - Send a feedback form after the viewing
            - Share collected feedback with the seller
API:        REST
            GET  /properties/{id}/slots
            POST /viewings
            POST /viewings/{id}/feedback
            GET  /properties/{id}/feedback
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Action Mailer
```

---

## Example 42

**Intent:**
hi i make soap and candles and sell at markets, i want to keep track of my batches and ingredients so i know my costs per bar

**Spec:**
```
Type:       Web application (small batch production costing)
Auth:       Single user email + password login
Data model: Ingredient(id, name, unit, cost_per_unit, stock)
            Recipe(id, name, product_type, yield_units)
            RecipeIngredient(id, recipe_id -> Recipe, ingredient_id -> Ingredient, amount)
            Batch(id, recipe_id -> Recipe, made_on, units_made, cure_ready_on)
Features:   - Store recipes with ingredient amounts
            - Calculate cost per bar or candle from ingredient prices
            - Deduct ingredients from stock when a batch is made
            - Show when soap batches finish curing
            - Warn when an ingredient runs low
API:        REST
            GET  /recipes/{id}/cost
            POST /batches
            GET  /ingredients/low
Storage:    SQLite
Tech stack: Python, Flask, HTMX
```

---

## Example 43

**Intent:**
For our translation agency I want clients to upload documents, get a word count based quote, and then track the translation status.

**Spec:**
```
Type:       Web application (translation job portal)
Auth:       Email + password login; roles: client, translator, project manager
Data model: Project(id, client_id -> User, source_lang, target_lang, word_count, rate_per_word, quote, status, due_date)
            SourceFile(id, project_id -> Project, file_url, words)
            Assignment(id, project_id -> Project, translator_id -> User, role)
Features:   - Upload DOCX and PDF files and count words automatically
            - Produce a quote from word count and language pair rate
            - Assign translators and reviewers to accepted projects
            - Track status from quoted to delivered
            - Deliver translated files back to the client
API:        REST
            POST /projects
            POST /projects/{id}/files
            POST /projects/{id}/accept
            PATCH /projects/{id}/status
Storage:    PostgreSQL, S3 (files)
Tech stack: Python, Django, python-docx, pdfminer
```

---

## Example 44

**Intent:**
church hall hire calendar so groups can request the hall

**Spec:**
```
Type:       Web application (venue hire requests)
Auth:       Admin login; groups request without an account
Data model: Room(id, name, capacity, hourly_rate)
            HireRequest(id, room_id -> Room, group_name, contact_email, start_at, end_at, purpose, status)
Features:   - Show a public calendar of booked times
            - Let groups request a room for a date and time
            - Let the admin approve or decline requests
            - Email the group the decision and invoice amount
API:        REST
            GET  /calendar
            POST /requests
            PATCH /requests/{id}
Storage:    SQLite
Tech stack: PHP, Slim Framework, FullCalendar
```

---

## Example 45

**Intent:**
web app for a tyre shop where customers can enter their car reg and see which tyres fit and book fitting

**Spec:**
```
Type:       Web application (tyre lookup and fitting booking)
Auth:       Customers book as guests; staff login
Data model: Tyre(id, brand, model, width, profile, rim, load_index, speed_rating, price, stock)
            VehicleLookup(id, registration, tyre_size, looked_up_at)
            FittingBooking(id, registration, customer_name, phone, tyre_id -> Tyre, quantity, slot_at)
Features:   - Look up the tyre size from a registration number
            - Show matching tyres with price and stock
            - Book a fitting slot at the shop
            - Reserve stock when a fitting is booked
API:        REST
            GET  /lookup/{registration}
            GET  /tyres?size={size}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, vehicle data API
```

---

## Example 46

**Intent:**
caterer menu builder and event quote

**Spec:**
```
Type:       Web application (catering quotes)
Auth:       Email + password login for the catering team
Data model: Dish(id, name, course, price_per_head, allergens)
            Event(id, client_name, date, guests, venue)
            EventDish(id, event_id -> Event, dish_id -> Dish)
            Quote(id, event_id -> Event, staff_cost, total, sent_at)
Features:   - Build a menu for an event from the dish list
            - Calculate cost from guest count and price per head
            - Add staff and equipment costs
            - List allergens present in the menu
            - Send the quote to the client as a PDF
API:        REST
            POST /events
            POST /events/{id}/dishes
            POST /events/{id}/quote
Storage:    PostgreSQL
Tech stack: Python, Django, WeasyPrint
```

---

## Example 47

**Intent:**
Our roofing company does free inspections. I want the inspector to take photos on the roof, mark problems, and send a nice report to the homeowner with a price.

**Spec:**
```
Type:       Web application (inspection reports)
Auth:       Email + password login for inspectors
Data model: Inspection(id, address, homeowner_name, homeowner_email, inspector_id -> User, date, roof_type, status)
            Finding(id, inspection_id -> Inspection, area, issue, severity, photo_url)
            LineItem(id, inspection_id -> Inspection, description, price)
Features:   - Start an inspection and take photos from a phone
            - Tag each photo with the roof area and problem
            - Add a priced list of recommended repairs
            - Generate a branded PDF report
            - Email the report and track when it is opened
API:        REST
            POST /inspections
            POST /inspections/{id}/findings
            POST /inspections/{id}/send
Storage:    PostgreSQL, S3 (photos)
Tech stack: React (PWA), Node.js, Express, Puppeteer, Postmark
```

---

## Example 48

**Intent:**
need a page for my dog grooming van that shows which area im in each day and lets people book

**Spec:**
```
Type:       Web application (mobile service booking by area)
Auth:       Owner login; customers book as guests
Data model: AreaDay(id, weekday, area_name, postcodes)
            Booking(id, customer_name, phone, address, postcode, dog_name, dog_size, service, date, slot)
            Service(id, name, duration_min, price_small, price_large)
Features:   - Show the weekly schedule of areas served
            - Only offer dates when the van is in the customer's postcode area
            - Book a grooming slot with dog size and service
            - Show the owner the day's route of bookings
API:        REST
            GET  /schedule
            GET  /availability?postcode={pc}
            POST /bookings
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 49

**Intent:**
online class register for a music school, teachers mark attendance and parents see it

**Spec:**
```
Type:       Web application (attendance register)
Auth:       Email + password login; roles: teacher, parent, admin
Data model: Student(id, name, parent_id -> User, instrument)
            Lesson(id, teacher_id -> User, student_id -> Student, scheduled_at)
            Attendance(id, lesson_id -> Lesson, status, note)
Features:   - Show teachers their lessons for the day
            - Mark each lesson attended, absent or cancelled
            - Add a short practice note for the student
            - Let parents see attendance and notes
            - Count missed lessons per term
API:        REST
            GET  /lessons?date={d}
            POST /lessons/{id}/attendance
            GET  /students/{id}/attendance
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView
```

---

## Example 50

**Intent:**
garden centre plant care cards with QR codes customers scan in store

**Spec:**
```
Type:       Web application (plant information via QR)
Auth:       Staff login to edit plants
Data model: Plant(id, common_name, latin_name, light, watering, hardiness, price, slug)
            ScanEvent(id, plant_id -> Plant, scanned_at)
Features:   - Create a care page for each plant
            - Generate printable QR code labels per plant
            - Show care info on a mobile-friendly page when scanned
            - Count scans per plant to see what customers look at
API:        REST
            GET  /plants/{slug}
            POST /plants
            GET  /plants/{id}/qr.png
Storage:    PostgreSQL
Tech stack: Python, Django, segno (QR codes)
```

---

## Example 51

**Intent:**
conveyancing tracker so house buyers can see what stage their purchase is at

**Spec:**
```
Type:       Web application (conveyancing progress tracker)
Auth:       Email + password login for clients; solicitor staff accounts
Data model: Matter(id, client_id -> User, property_address, solicitor_id -> User, target_completion)
            Milestone(id, matter_id -> Matter, name, position, completed_at)
            Message(id, matter_id -> Matter, author_id -> User, body, created_at)
Features:   - Show clients a step-by-step progress bar for their purchase
            - Let solicitors tick off milestones (searches, mortgage offer, exchange, completion)
            - Email the client when a milestone is completed
            - Send secure messages between client and solicitor
            - Reduce "any update?" phone calls with a status page
API:        REST
            GET  /matters/{id}
            PATCH /milestones/{id}/complete
            POST /matters/{id}/messages
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Angular
```

---

## Example 52

**Intent:**
sign-in sheet for visitors at our warehouse gate on a tablet

**Spec:**
```
Type:       Web application (visitor sign-in kiosk)
Auth:       Kiosk device token; reception admin login
Data model: Visit(id, visitor_name, company, host_id -> Employee, vehicle_reg, signed_in_at, signed_out_at, safety_ack)
            Employee(id, name, email, phone)
Features:   - Sign visitors in on a tablet with their name, company and host
            - Require acceptance of site safety rules
            - Notify the host by email or SMS on arrival
            - Sign visitors out and list who is still on site for fire roll call
API:        REST
            POST /visits
            POST /visits/{id}/sign-out
            GET  /visits/on-site
Storage:    PostgreSQL
Tech stack: React, Node.js, Express, Twilio
```

---

## Example 53

**Intent:**
were a small brewery taproom and want customers to order from the table by scanning a qr code

**Spec:**
```
Type:       Web application (table QR ordering)
Auth:       Staff login; customers order without an account
Data model: Table(id, number, qr_token)
            MenuItem(id, name, category, abv, price, available)
            TableOrder(id, table_id -> Table, status, total, paid, created_at)
            TableOrderItem(id, order_id -> TableOrder, item_id -> MenuItem, quantity, size)
Features:   - Open the menu for the right table by scanning its QR code
            - Order drinks and snacks and pay with Apple Pay or card
            - Show new orders on a bar screen in real time
            - Mark items as unavailable when a keg runs out
API:        REST
            GET  /tables/{token}/menu
            POST /orders
            PATCH /orders/{id}/status
Storage:    PostgreSQL
Tech stack: Next.js, Socket.IO, Stripe
```

---

## Example 54

**Intent:**
Hi, we are accounting firm with 6 accountant. We need a tool where we see all clients tax deadlines and who is responsible, so nobody forget a filing.

**Spec:**
```
Type:       Web application (filing deadline tracker)
Auth:       Email + password login for firm staff
Data model: Client(id, name, entity_type, tax_id, year_end)
            FilingType(id, name, months_after_year_end, day_of_month)
            Filing(id, client_id -> Client, filing_type_id -> FilingType, period, due_date, owner_id -> User, status)
Features:   - Generate filing deadlines from each client's year end
            - Assign a responsible accountant per filing
            - Show a calendar and list of filings due in the next 30 days
            - Send weekly email digests of upcoming deadlines
            - Mark filings as submitted with the submission date
API:        REST
            GET  /filings?due_within=30
            POST /clients
            PATCH /filings/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Celery
```

---

## Example 55

**Intent:**
bike repair shop job tickets

**Spec:**
```
Type:       Web application (repair job tickets)
Auth:       Staff email + password login
Data model: Customer(id, name, phone)
            Bike(id, customer_id -> Customer, make, model, colour)
            RepairTicket(id, bike_id -> Bike, problem, estimate, status, booked_in_at, ready_at)
            Part(id, ticket_id -> RepairTicket, name, price)
Features:   - Book a bike in with the problem and estimate
            - Add parts and labour to the ticket
            - Text the customer when the bike is ready
            - Print a tag to attach to the bike
API:        REST
            POST /tickets
            POST /tickets/{id}/parts
            PATCH /tickets/{id}/status
Storage:    SQLite
Tech stack: Python, Flask, Twilio
```

---

## Example 56

**Intent:**
I run a chimney sweep business on my own and I want customers to get an automatic reminder a year after their last sweep so they book again, plus I need to issue a sweep certificate each time.

**Spec:**
```
Type:       Web application (service reminders and certificates)
Auth:       Single owner login
Data model: Customer(id, name, email, phone, address)
            Appliance(id, customer_id -> Customer, type, fuel)
            Sweep(id, appliance_id -> Appliance, swept_on, condition, notes, certificate_no)
Features:   - Record each sweep with the appliance and condition found
            - Generate a numbered sweep certificate as PDF
            - Email customers a booking reminder 11 months after their last sweep
            - List customers due for a sweep this month
API:        REST
            POST /appliances/{id}/sweeps
            GET  /sweeps/{id}/certificate.pdf
            GET  /customers/due
Storage:    SQLite
Tech stack: Python, Flask, ReportLab, APScheduler
```

---

## Example 57

**Intent:**
supplier onboarding form where new vendors give us bank details tax forms and insurance certificates

**Spec:**
```
Type:       Web application (supplier onboarding)
Auth:       One-time invite link for suppliers; staff SSO
Data model: Supplier(id, legal_name, tax_id, address, contact_email, status)
            BankDetail(id, supplier_id -> Supplier, account_name, iban_encrypted, verified)
            SupplierDocument(id, supplier_id -> Supplier, kind, file_url, expires_on)
Features:   - Invite a supplier by email with a secure link
            - Collect company, tax and bank details in a step-by-step form
            - Upload insurance certificates with expiry dates
            - Let finance review and approve the supplier
            - Alert when a supplier's insurance expires
API:        REST
            POST /invites
            POST /onboarding/{token}
            POST /suppliers/{id}/approve
Storage:    PostgreSQL (encrypted bank fields), S3
Tech stack: Java, Spring Boot, React
```

---

## Example 58

**Intent:**
photographer booking site where clients pick a package pay deposit and choose date

**Spec:**
```
Type:       Web application (photography booking)
Auth:       Photographer admin login; clients book as guests
Data model: Package(id, name, hours, photo_count, price, deposit)
            Booking(id, package_id -> Package, client_name, email, event_date, location, deposit_paid, balance_due)
            BlockedDate(id, date)
Features:   - Show photography packages with prices
            - Pick a free date on a calendar
            - Pay the deposit online to confirm
            - Send a balance reminder 14 days before the shoot
API:        REST
            GET  /packages
            GET  /availability?month={m}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Astro, Netlify Functions, Stripe
```

---

## Example 59

**Intent:**
tool hire shop, customers reserve a tool online for some days and pay a deposit

**Spec:**
```
Type:       Web application (tool hire reservations)
Auth:       Email + password customer accounts; staff login
Data model: Tool(id, name, category, daily_rate, weekly_rate, deposit, quantity)
            Reservation(id, tool_id -> Tool, customer_id -> User, start_date, end_date, deposit_paid, status)
Features:   - Browse tools by category with daily and weekly rates
            - Check availability for chosen dates
            - Reserve and pay a deposit online
            - Mark tools as collected and returned
            - Charge late fees for overdue returns
API:        REST
            GET  /tools/{id}/availability
            POST /reservations
            PATCH /reservations/{id}/return
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 60

**Intent:**
can u make a page where my cleaners clock in and out at the client house with gps so i know they really were there

**Spec:**
```
Type:       Web application (GPS clock-in)
Auth:       Email + password login; roles: owner, cleaner
Data model: Site(id, client_name, address, lat, lng, radius_m)
            ClockEvent(id, cleaner_id -> User, site_id -> Site, type, lat, lng, accuracy_m, recorded_at)
Features:   - Clock in and out from the phone browser using GPS location
            - Check the location is within the site radius
            - Flag clock-ins made away from the site
            - Show the owner hours worked per cleaner per site
API:        REST
            POST /clock
            GET  /reports/hours?week={w}
Storage:    PostgreSQL
Tech stack: Vue.js, Geolocation API, Node.js, Express
```

---

## Example 61

**Intent:**
Laravel app for a plant nursery selling trees wholesale to landscapers, with stock by pot size

**Spec:**
```
Type:       Web application (wholesale nursery stock)
Auth:       Email + password login for trade accounts; staff admin
Data model: Plant(id, latin_name, common_name)
            StockLine(id, plant_id -> Plant, pot_size, height_cm, quantity, trade_price)
            TradeOrder(id, account_id -> User, status, collection_date)
            TradeOrderLine(id, order_id -> TradeOrder, stock_line_id -> StockLine, quantity)
Features:   - List available plants by pot size and height
            - Show live stock quantities
            - Place trade orders for collection or delivery
            - Reserve stock when an order is confirmed
            - Import weekly availability from a spreadsheet
API:        REST
            GET  /stock
            POST /orders
            POST /admin/stock/import
Storage:    MySQL
Tech stack: PHP, Laravel, Laravel Excel
```

---

## Example 62

**Intent:**
key register for a property management office

**Spec:**
```
Type:       Web application (key tracking)
Auth:       Staff email + password login
Data model: Key(id, tag_number, property_address, description)
            KeyLoan(id, key_id -> Key, borrower_name, company, out_at, due_at, returned_at)
Features:   - Register keys with a tag number per property
            - Sign keys out to contractors with a return time
            - Show keys currently out and overdue
            - Keep a full history per key
API:        REST
            GET  /keys
            POST /keys/{id}/loan
            POST /loans/{id}/return
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 63

**Intent:**
we run a charter fishing boat and want people to book seats on trips, max 12 people a trip

**Spec:**
```
Type:       Web application (trip seat booking)
Auth:       Captain admin login; customers book as guests
Data model: Trip(id, date, departure_time, duration_h, price_per_seat, capacity, status)
            SeatBooking(id, trip_id -> Trip, name, email, phone, seats, paid)
Features:   - List upcoming trips with seats left
            - Book and pay for one or more seats
            - Stop bookings when the trip is full
            - Cancel a trip for bad weather and refund everyone
            - Email passengers the meeting point and what to bring
API:        REST
            GET  /trips
            POST /trips/{id}/bookings
            POST /trips/{id}/cancel
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe
```

---

## Example 64

**Intent:**
auction house catalog where bidders can leave absentee bids before the sale

**Spec:**
```
Type:       Web application (auction catalogue with absentee bids)
Auth:       Email + password login with identity check for bidders
Data model: Sale(id, title, starts_at, location)
            Lot(id, sale_id -> Sale, lot_number, title, description, estimate_low, estimate_high, image_url)
            AbsenteeBid(id, lot_id -> Lot, bidder_id -> User, max_amount, created_at)
Features:   - Publish an online catalogue of lots per sale
            - Let registered bidders place a maximum absentee bid on lots
            - Lock bids when the sale starts
            - Give the auctioneer a book of absentee bids per lot
API:        REST
            GET  /sales/{id}/lots
            POST /lots/{id}/bids
            GET  /admin/sales/{id}/bid-book
Storage:    PostgreSQL
Tech stack: Python, Django, Bootstrap
```

---

## Example 65

**Intent:**
For my HVAC business, every customer has a yearly maintenance contract. I'd like to see which contracts renew this month, schedule the visit, and keep a history of the units we serviced.

**Spec:**
```
Type:       Web application (service contract management)
Auth:       Email + password login for office and technicians
Data model: Customer(id, name, address, phone)
            Unit(id, customer_id -> Customer, type, brand, model, serial, installed_on)
            Contract(id, customer_id -> Customer, start_date, renewal_date, price, status)
            ServiceVisit(id, unit_id -> Unit, technician_id -> User, date, work_done, filter_changed)
Features:   - List contracts renewing this month
            - Schedule a maintenance visit for each contract
            - Record service work per unit
            - Show a unit's full service history
            - Send renewal invoices automatically
API:        REST
            GET  /contracts/renewing?month={m}
            POST /visits
            GET  /units/{id}/history
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core MVC
```

---

## Example 66

**Intent:**
customs broker document checklist per shipment

**Spec:**
```
Type:       Web application (shipment document checklist)
Auth:       Email + password login for brokers; client view links
Data model: Shipment(id, client_name, reference, mode, origin_country, eta, status)
            RequiredDocument(id, shipment_id -> Shipment, doc_type, received, file_url)
Features:   - Create a shipment with its transport mode and origin
            - Generate the required documents list from the mode and country
            - Upload documents as they arrive
            - Show which shipments are missing documents before ETA
API:        REST
            POST /shipments
            POST /shipments/{id}/documents
            GET  /shipments/missing-docs
Storage:    PostgreSQL, S3
Tech stack: Go, Gin, React
```

---

## Example 67

**Intent:**
yo i do mobile car detailing, want ppl to pick their car size and package and get a price then book

**Spec:**
```
Type:       Web application (service quote and booking)
Auth:       Owner admin login; customers book as guests
Data model: Package(id, name, description)
            PriceRule(id, package_id -> Package, vehicle_size, price, duration_min)
            Booking(id, package_id -> Package, vehicle_size, address, date, start_time, name, phone, price)
Features:   - Pick vehicle size (small, SUV, van) and detailing package
            - Show the price and duration instantly
            - Book a time slot that fits the job duration
            - Take a deposit online
API:        REST
            GET  /packages
            GET  /quote?package={id}&size={s}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Next.js, Supabase, Stripe
```

---

## Example 68

**Intent:**
dog daycare daily report cards for owners

**Spec:**
```
Type:       Web application (daycare report cards)
Auth:       Email + password login; roles: staff, owner
Data model: Dog(id, owner_id -> User, name, breed)
            ReportCard(id, dog_id -> Dog, date, mood, ate, naps, playmates, staff_note)
            ReportPhoto(id, report_id -> ReportCard, url)
Features:   - Fill in a daily report card per dog from a tablet
            - Add photos from the day
            - Email the owner when the report is published
            - Let owners browse past report cards
API:        REST
            POST /dogs/{id}/reports
            POST /reports/{id}/photos
            GET  /dogs/{id}/reports
Storage:    PostgreSQL, S3
Tech stack: Node.js, Express, React
```

---

## Example 69

**Intent:**
Build me a Rails app for a bridal shop: brides book fitting appointments and we track dress orders from the designer and alteration dates.

**Spec:**
```
Type:       Web application (bridal shop orders and fittings)
Auth:       Email + password login for staff; brides get a client login
Data model: Bride(id, name, email, phone, wedding_date)
            DressOrder(id, bride_id -> Bride, designer, style, size, ordered_on, expected_on, received_on, deposit)
            Fitting(id, bride_id -> Bride, scheduled_at, seamstress, notes)
Features:   - Book first appointments and fittings online
            - Track dress orders from the designer with expected arrival
            - Warn when a dress arrives too close to the wedding date
            - Schedule alteration fittings in order
            - Record deposit and balance payments
API:        REST
            POST /appointments
            GET  /dress-orders?late=true
            POST /brides/{id}/fittings
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire, Stimulus
```

---

## Example 70

**Intent:**
I have a self storage place with 80 units. Want customers rent a unit online, choose size, and pay monthly automatic.

**Spec:**
```
Type:       Web application (self storage rentals)
Auth:       Email + password customer accounts; admin login
Data model: StorageUnit(id, number, size_sqft, monthly_price, status)
            Rental(id, unit_id -> StorageUnit, customer_id -> User, start_date, end_date, gate_code, status)
            Payment(id, rental_id -> Rental, amount, paid_at, status)
Features:   - Show available units by size and price
            - Rent a unit online and sign the agreement
            - Charge rent monthly by card automatically
            - Issue a personal gate code on move-in
            - Flag rentals with failed payments for lock-out
API:        REST
            GET  /units/available
            POST /rentals
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe Subscriptions
```

---

## Example 71

**Intent:**
trade counter price lookup for staff

**Spec:**
```
Type:       Web application (internal price lookup)
Auth:       Staff login with a PIN on shared counter PCs
Data model: Product(id, sku, barcode, description, list_price, stock)
            CustomerAccount(id, account_no, name, discount_pct)
Features:   - Search products by SKU, barcode or description
            - Show the net price for a selected trade account
            - Show stock levels at the branch
            - Work fast with keyboard-only navigation
API:        REST
            GET  /products/search?q={q}
            GET  /prices?sku={sku}&account={no}
Storage:    PostgreSQL
Tech stack: Go, HTMX
```

---

## Example 72

**Intent:**
tattoo studio, clients send in their idea and reference pics and the artist replies with a quote and books them

**Spec:**
```
Type:       Web application (tattoo enquiries and bookings)
Auth:       Artist login; clients use a magic link sent by email
Data model: Artist(id, name, style, hourly_rate)
            Enquiry(id, artist_id -> Artist, client_name, email, placement, size_cm, description, status)
            ReferenceImage(id, enquiry_id -> Enquiry, url)
            Appointment(id, enquiry_id -> Enquiry, starts_at, hours, deposit_paid)
Features:   - Submit a tattoo idea with placement, size and reference images
            - Let artists reply with a quote and estimated hours
            - Book a session and pay a non-refundable deposit
            - Keep the conversation history per enquiry
API:        REST
            POST /enquiries
            POST /enquiries/{id}/quote
            POST /enquiries/{id}/appointment
Storage:    PostgreSQL, S3
Tech stack: SvelteKit, Prisma, Stripe
```

---

## Example 73

**Intent:**
welding shop needs to track welder certifications and which welder did which weld on a job

**Spec:**
```
Type:       Web application (weld traceability)
Auth:       Email + password login for QA and supervisors
Data model: Welder(id, name, stamp_number)
            Qualification(id, welder_id -> Welder, process, position, expires_on)
            Job(id, number, client, drawing_ref)
            Weld(id, job_id -> Job, weld_number, welder_id -> Welder, process, date, inspection_result)
Features:   - Record each weld with the welder who made it
            - Block assigning a welder whose qualification expired
            - Alert before qualifications expire
            - Produce a weld map report per job
API:        REST
            POST /jobs/{id}/welds
            GET  /welders/{id}/qualifications
            GET  /jobs/{id}/weld-report
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Thymeleaf
```

---

## Example 74

**Intent:**
Me and my partner run a wedding venue in the countryside. Couples always ask the same things: which dates are free, what packages cost, can they do a viewing. I want a site that shows free dates, gives a price depending on the day and guest count, and lets them book a viewing.

**Spec:**
```
Type:       Web application (wedding venue availability and pricing)
Auth:       Venue admin login; couples enquire as guests
Data model: VenueDate(id, date, status)
            Season(id, name, start_month, end_month)
            PriceRule(id, season_id -> Season, weekday_type, base_price, per_guest)
            ViewingRequest(id, couple_names, email, phone, preferred_date, wedding_date, guests)
Features:   - Show a calendar of free and booked wedding dates
            - Calculate a price from season, weekday and guest count
            - Let couples request a viewing
            - Let the admin hold a date provisionally for 7 days
API:        REST
            GET  /dates?year={y}
            GET  /price?date={d}&guests={n}
            POST /viewings
Storage:    PostgreSQL
Tech stack: Nuxt, Node.js, PostgreSQL client (pg)
```

---

## Example 75

**Intent:**
dry cleaning ticket system

**Spec:**
```
Type:       Web application (garment ticketing)
Auth:       Staff PIN login at the counter
Data model: Customer(id, name, phone)
            Ticket(id, customer_id -> Customer, ticket_no, dropped_at, ready_on, total, paid, collected_at)
            Garment(id, ticket_id -> Ticket, type, service, price, notes)
Features:   - Create a ticket with each garment and service
            - Print a numbered ticket and garment tags
            - Text the customer when the order is ready
            - Look up tickets by number or phone
API:        REST
            POST /tickets
            GET  /tickets/{no}
            PATCH /tickets/{id}/collect
Storage:    SQLite
Tech stack: Python, Flask, ESC/POS receipt printer library
```

---

## Example 76

**Intent:**
small engineering firm wants a register of drawings with revisions so people don't use old versions

**Spec:**
```
Type:       Web application (drawing register)
Auth:       Email + password login; roles: engineer, approver, viewer
Data model: Project(id, code, name)
            Drawing(id, project_id -> Project, number, title)
            Revision(id, drawing_id -> Drawing, rev, file_url, status, issued_on, approved_by -> User)
Features:   - Upload drawing PDFs as new revisions
            - Mark one revision as current and older ones as superseded
            - Require approval before a revision is issued
            - Show a transmittal list of current revisions per project
API:        REST
            GET  /projects/{id}/drawings
            POST /drawings/{id}/revisions
            POST /revisions/{id}/approve
Storage:    PostgreSQL, S3
Tech stack: Python, FastAPI, React
```

---

## Example 77

**Intent:**
loading dock scheduling for trucks at our distribution center

**Spec:**
```
Type:       Web application (dock appointment scheduling)
Auth:       Carrier accounts with email login; warehouse staff accounts
Data model: Dock(id, name, type)
            Appointment(id, dock_id -> Dock, carrier_id -> User, po_number, slot_start, slot_end, status)
            ArrivalLog(id, appointment_id -> Appointment, arrived_at, unloaded_at)
Features:   - Let carriers book an inbound or outbound dock slot
            - Validate the purchase order number
            - Show the yard team a timeline of docks for the day
            - Record arrival and unload times
            - Report carrier punctuality
API:        REST
            GET  /docks/availability?date={d}
            POST /appointments
            POST /appointments/{id}/arrived
Storage:    PostgreSQL
Tech stack: TypeScript, Express, React
```

---

## Example 78

**Intent:**
hey so i fix phones and want customers to check repair status with their ticket number online

**Spec:**
```
Type:       Web application (repair status lookup)
Auth:       Staff login; customers look up with ticket number + phone
Data model: Repair(id, ticket_no, customer_name, phone, device, fault, status, price, updated_at)
            StatusChange(id, repair_id -> Repair, status, changed_at)
Features:   - Create repair tickets at the counter
            - Update status (received, diagnosing, waiting for parts, ready)
            - Let customers check status with ticket number and phone
            - Send an SMS when the repair is ready
API:        REST
            POST /repairs
            PATCH /repairs/{id}/status
            GET  /status?ticket={no}&phone={p}
Storage:    SQLite
Tech stack: Node.js, Express, Twilio
```

---

## Example 79

**Intent:**
library of standard operating procedures for our lab with sign-off that staff have read them

**Spec:**
```
Type:       Web application (SOP management)
Auth:       Single sign-on with Okta
Data model: SOP(id, code, title, version, file_url, effective_from, owner_id -> User)
            ReadReceipt(id, sop_id -> SOP, user_id -> User, read_at)
            Assignment(id, sop_id -> SOP, role, due_days)
Features:   - Publish new SOP versions
            - Assign SOPs to staff by role
            - Record electronic sign-off that the SOP was read
            - Require re-reading when a new version is published
            - Report outstanding sign-offs per person
API:        REST
            POST /sops
            POST /sops/{id}/read
            GET  /reports/outstanding
Storage:    PostgreSQL, S3
Tech stack: Java, Spring Boot, Vue.js
```

---

## Example 80

**Intent:**
Hello! I am owner of a small hotel for cats. Owners want to see webcam and know what their cat did today. Can you make something?

**Spec:**
```
Type:       Web application (cat hotel guest updates)
Auth:       Email + password login for cat owners; staff admin
Data model: Cat(id, owner_id -> User, name, diet, medication)
            Room(id, name, camera_stream_url)
            Stay(id, cat_id -> Cat, room_id -> Room, check_in, check_out)
            DailyNote(id, stay_id -> Stay, date, ate_well, played, medication_given, comment)
Features:   - Show owners a live webcam stream of their cat's room during the stay
            - Post daily notes on eating, playing and medication
            - Upload photos to the stay timeline
            - Hide the webcam after check-out
API:        REST
            GET  /stays/{id}
            GET  /stays/{id}/stream
            POST /stays/{id}/notes
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, HLS video streaming
```

---

## Example 81

**Intent:**
sample tracking for a soil testing lab

**Spec:**
```
Type:       Web application (lab sample tracking)
Auth:       Email + password login; roles: client, lab technician
Data model: Submission(id, client_id -> User, received_on, status)
            Sample(id, submission_id -> Submission, barcode, field_name, depth_cm)
            TestResult(id, sample_id -> Sample, test, value, unit, tested_on)
Features:   - Register submitted samples with barcode labels
            - Record test results (pH, nitrogen, phosphorus, potassium)
            - Show the status of every sample in the lab
            - Publish a results report to the client with fertiliser advice
API:        REST
            POST /submissions
            POST /samples/{barcode}/results
            GET  /submissions/{id}/report
Storage:    PostgreSQL
Tech stack: Python, Django, React
```

---

## Example 82

**Intent:**
staffing agency timesheets: temps submit hours, client approves, we pay

**Spec:**
```
Type:       Web application (temp timesheet approval)
Auth:       Email + password login; roles: temp worker, client approver, agency admin
Data model: Placement(id, worker_id -> User, client_id -> Client, pay_rate, charge_rate, start_date)
            Client(id, name, approver_email)
            Timesheet(id, placement_id -> Placement, week_ending, hours, status, approved_at)
Features:   - Let temps submit weekly hours per placement
            - Email the client a link to approve or reject
            - Lock approved timesheets for payroll
            - Export pay and invoice totals per week
API:        REST
            POST /timesheets
            POST /timesheets/{id}/approve
            GET  /exports/week?ending={d}
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Angular
```

---

## Example 83

**Intent:**
want to sell my bread to local cafes, they order before 2pm for next day delivery

**Spec:**
```
Type:       Web application (wholesale bakery ordering)
Auth:       Email + password login for cafe accounts; bakery admin
Data model: Cafe(id, name, address, contact)
            Bread(id, name, price, active)
            StandingOrder(id, cafe_id -> Cafe, bread_id -> Bread, weekday, quantity)
            DailyOrder(id, cafe_id -> Cafe, delivery_date, status)
            DailyOrderLine(id, order_id -> DailyOrder, bread_id -> Bread, quantity)
Features:   - Let cafes place orders for next-day delivery
            - Close ordering at 2pm each day
            - Set up standing orders per weekday
            - Produce a bake sheet with total loaves per bread
            - Produce delivery notes per cafe
API:        REST
            POST /orders
            GET  /admin/bake-sheet?date={d}
            GET  /admin/delivery-notes?date={d}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 84

**Intent:**
locker system for parcel pickup in our apartment building, residents get a code

**Spec:**
```
Type:       IoT system (smart parcel lockers)
Auth:       Resident accounts with email login; concierge admin
Data model: Locker(id, number, size, status)
            Parcel(id, resident_id -> User, locker_id -> Locker, carrier, pickup_code_hash, delivered_at, collected_at)
Features:   - Let the concierge assign a parcel to a free locker
            - Send the resident a one-time pickup code
            - Unlock the locker when the code is entered on the keypad
            - Remind residents of parcels not collected after 3 days
API:        REST
            POST /parcels
            POST /lockers/{id}/unlock
            GET  /parcels/uncollected
Storage:    PostgreSQL
Tech stack: ESP32 lock controllers, MQTT, Python, FastAPI
```

---

## Example 85

**Intent:**
For a framing shop: the customer brings a picture, we pick moulding and mount and glass, the system calculates the price by size.

**Spec:**
```
Type:       Web application (picture framing quotes)
Auth:       Staff login
Data model: Moulding(id, code, name, price_per_metre, width_mm)
            Mount(id, colour, price_per_m2)
            Glazing(id, type, price_per_m2)
            FrameOrder(id, customer_name, phone, artwork_w_mm, artwork_h_mm, moulding_id -> Moulding, mount_id -> Mount, glazing_id -> Glazing, price, status)
Features:   - Calculate moulding length from artwork size and mount border
            - Price mount and glazing by area
            - Save the job and print a work ticket
            - Track orders until collected
API:        REST
            POST /quotes
            POST /orders
            PATCH /orders/{id}/status
Storage:    SQLite
Tech stack: Python, Flask, Alpine.js
```

---

## Example 86

**Intent:**
lawn care company recurring visits schedule

**Spec:**
```
Type:       Web application (recurring service scheduling)
Auth:       Email + password login; roles: owner, crew lead
Data model: Customer(id, name, address, lawn_size_m2, price_per_visit)
            Plan(id, customer_id -> Customer, frequency_days, start_date, active)
            Visit(id, plan_id -> Plan, crew_id -> Crew, scheduled_on, done, notes)
            Crew(id, name)
Features:   - Generate visits from each customer's mowing frequency
            - Assign visits to crews by area
            - Push visits forward a day when it rains
            - Mark visits done from a phone
            - Invoice customers monthly for completed visits
API:        REST
            GET  /visits?date={d}&crew={id}
            POST /visits/reschedule
            PATCH /visits/{id}/done
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 87

**Intent:**
customer portal for our sign making business where clients approve the design proof before we print

**Spec:**
```
Type:       Web application (design proof approval)
Auth:       Magic link login for clients; staff accounts
Data model: Job(id, client_email, title, quantity, material, status)
            Proof(id, job_id -> Job, version, image_url, uploaded_at)
            ProofDecision(id, proof_id -> Proof, decision, comment, decided_at)
Features:   - Upload proof versions for a job
            - Email the client a link to review the proof
            - Let the client approve or request changes with comments
            - Release the job to production only after approval
API:        REST
            POST /jobs/{id}/proofs
            POST /proofs/{id}/decision
            GET  /jobs/{id}
Storage:    PostgreSQL, S3
Tech stack: PHP, Symfony, Twig
```

---

## Example 88

**Intent:**
I'm opening a mushroom farm and I want to track every grow bag from inoculation to harvest, with yields, so I can figure out which strains and substrates work best.

**Spec:**
```
Type:       Web application (grow batch tracking)
Auth:       Single user login
Data model: Strain(id, name, species)
            Substrate(id, recipe, cost_per_kg)
            GrowBag(id, code, strain_id -> Strain, substrate_id -> Substrate, inoculated_on, weight_kg, status)
            Harvest(id, bag_id -> GrowBag, harvested_on, yield_g, flush_number)
Features:   - Label each grow bag with a QR code
            - Scan a bag to update its stage (colonising, fruiting, spent)
            - Log harvest weights per flush
            - Compare biological efficiency by strain and substrate
            - Flag bags with contamination
API:        REST
            POST /bags
            PATCH /bags/{code}/stage
            POST /bags/{code}/harvests
            GET  /stats/efficiency
Storage:    SQLite
Tech stack: Python, FastAPI, HTMX, Chart.js
```

---

## Example 89

**Intent:**
hotel housekeeping: show which rooms need cleaning and let maids mark them done

**Spec:**
```
Type:       Web application (housekeeping board)
Auth:       PIN login for housekeepers; supervisor login
Data model: Room(id, number, floor, type, status)
            CleaningTask(id, room_id -> Room, housekeeper_id -> User, type, assigned_on, done_at, inspected)
Features:   - Show room status (dirty, cleaning, clean, inspected) by floor
            - Assign rooms to housekeepers each morning
            - Let housekeepers mark rooms done from a phone
            - Let supervisors inspect and release rooms to reception
API:        REST
            GET  /rooms?floor={f}
            POST /tasks/assign
            PATCH /tasks/{id}/done
Storage:    PostgreSQL
Tech stack: React, Firebase Firestore (real-time updates)
```

---

## Example 90

**Intent:**
insurance broker policy renewals reminder

**Spec:**
```
Type:       Web application (policy renewal tracking)
Auth:       Email + password login for brokers
Data model: Client(id, name, email, phone)
            Policy(id, client_id -> Client, insurer, type, policy_number, premium, renewal_date, broker_id -> User)
            RenewalTask(id, policy_id -> Policy, status, notes)
Features:   - List policies renewing in the next 60 days
            - Create renewal tasks automatically
            - Email clients a renewal notice
            - Track renewal outcome (renewed, moved insurer, lapsed)
API:        REST
            GET  /policies/renewing
            PATCH /renewal-tasks/{id}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 91

**Intent:**
mi taller mecanico need a system where client see the estimate and accept repair online before we start

**Spec:**
```
Type:       Web application (repair estimate approval)
Auth:       Staff login; customers open a secure link
Data model: Vehicle(id, plate, make, model, owner_phone, owner_email)
            Estimate(id, vehicle_id -> Vehicle, status, total, created_at)
            EstimateLine(id, estimate_id -> Estimate, description, parts_cost, labour_hours, required)
Features:   - Build an estimate with parts and labour lines
            - Send the estimate link to the customer by WhatsApp or SMS
            - Let the customer approve all or only some lines
            - Notify the workshop when the estimate is approved
API:        REST
            POST /estimates
            GET  /estimates/{token}
            POST /estimates/{token}/approve
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Twilio (WhatsApp)
```

---

## Example 92

**Intent:**
small hospital department wants to track loaned medical equipment like wheelchairs and pumps

**Spec:**
```
Type:       Web application (medical equipment loans)
Auth:       Single sign-on with hospital Active Directory (LDAP)
Data model: Equipment(id, asset_number, type, location, last_serviced_on, status)
            Loan(id, equipment_id -> Equipment, ward, borrowed_by, out_at, returned_at)
            ServiceRecord(id, equipment_id -> Equipment, serviced_on, result)
Features:   - Scan an asset number to loan equipment to a ward
            - Show where every item currently is
            - Block loans of items overdue for servicing
            - Record service and safety checks
API:        REST
            POST /equipment/{asset}/loan
            POST /loans/{id}/return
            GET  /equipment?status={s}
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Angular
```

---

## Example 93

**Intent:**
newsletter signup and customer list for my farm shop

**Spec:**
```
Type:       Web application (mailing list)
Auth:       Admin login
Data model: Subscriber(id, email, name, interests, confirmed, created_at)
            Campaign(id, subject, body_html, sent_at)
Features:   - Add a signup form to the farm shop website
            - Confirm subscriptions with double opt-in
            - Write and send a newsletter to all or by interest
            - Let subscribers unsubscribe with one click
API:        REST
            POST /subscribe
            GET  /confirm/{token}
            POST /campaigns/{id}/send
Storage:    SQLite
Tech stack: Python, Flask, Amazon SES
```

---

## Example 94

**Intent:**
I have a forklift rental business and customers always say the forklift broke but we don't know if they did a daily check. Make something where the operator does a daily pre-use check by scanning a sticker on the forklift.

**Spec:**
```
Type:       Web application (pre-use equipment checks)
Auth:       No login for operators (name entered); admin login
Data model: Forklift(id, fleet_no, qr_token, model, hire_customer)
            CheckQuestion(id, text, critical)
            DailyCheck(id, forklift_id -> Forklift, operator_name, hour_meter, done_at, passed)
            CheckAnswer(id, check_id -> DailyCheck, question_id -> CheckQuestion, ok, comment)
Features:   - Open the checklist by scanning the forklift's QR sticker
            - Answer pass/fail questions and enter the hour meter
            - Mark the forklift unsafe if a critical item fails
            - Alert the rental office on failed checks
            - Show the check history per forklift and customer
API:        REST
            GET  /forklifts/{token}/checklist
            POST /forklifts/{token}/checks
            GET  /forklifts/{id}/checks
Storage:    PostgreSQL
Tech stack: React (PWA), Python, FastAPI
```

---

## Example 95

**Intent:**
escape room booking with team size and pricing per person

**Spec:**
```
Type:       Web application (escape room booking)
Auth:       Admin login; customers book as guests
Data model: Room(id, name, theme, min_players, max_players, duration_min)
            Slot(id, room_id -> Room, starts_at, is_booked)
            Booking(id, slot_id -> Slot, lead_name, email, players, total_price, paid)
            PriceTier(id, players, price_per_person)
Features:   - Show rooms and their free time slots
            - Calculate price from the number of players
            - Book and pay online
            - Send a confirmation with arrival instructions
API:        REST
            GET  /rooms/{id}/slots?date={d}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe
```

---

## Example 96

**Intent:**
manage hives for my beekeeping business, inspections and honey harvest per apiary

**Spec:**
```
Type:       Web application (apiary management)
Auth:       Email + password login
Data model: Apiary(id, name, location, landowner)
            Hive(id, apiary_id -> Apiary, code, queen_year, status)
            HiveInspection(id, hive_id -> Hive, date, brood_frames, temper, queen_seen, varroa_count, notes)
            HoneyHarvest(id, hive_id -> Hive, date, weight_kg)
Features:   - Record hive inspections from the field on a phone
            - Track varroa counts and flag hives needing treatment
            - Log honey harvest weights per hive
            - Show total yield per apiary per season
API:        REST
            POST /hives/{id}/inspections
            POST /hives/{id}/harvests
            GET  /apiaries/{id}/yield?year={y}
Storage:    PostgreSQL
Tech stack: Vue.js, Node.js, Express
```

---

## Example 97

**Intent:**
web dashboard for our 3 coffee roasting machines showing roast profiles and batches

**Spec:**
```
Type:       Data dashboard (roastery production)
Data model: Roaster(id, name, capacity_kg)
            Roast(id, roaster_id -> Roaster, bean_origin, green_weight_kg, roasted_weight_kg, started_at, profile_name)
            TempPoint(id, roast_id -> Roast, seconds, bean_temp_c, rate_of_rise)
Features:   - Import roast logs exported from the roasting software
            - Plot bean temperature and rate of rise per roast
            - Overlay a roast on its target profile
            - Show weight loss percentage per batch
            - Summarise daily output per roaster
Input:      Roast log files (CSV) from each roaster
Storage:    PostgreSQL
Tech stack: Python, Streamlit, Plotly
```

---

## Example 98

**Intent:**
handyman jobs quote then invoice

**Spec:**
```
Type:       Web application (quotes and invoices)
Auth:       Single user login
Data model: Customer(id, name, email, address)
            Quote(id, customer_id -> Customer, status, total, valid_until)
            QuoteLine(id, quote_id -> Quote, description, quantity, unit_price)
            Invoice(id, quote_id -> Quote, number, issued_on, due_on, paid)
Features:   - Write a quote with line items
            - Email the quote and let the customer accept it online
            - Convert an accepted quote into an invoice
            - Mark invoices as paid and list unpaid ones
API:        REST
            POST /quotes
            POST /quotes/{id}/accept
            POST /quotes/{id}/invoice
Storage:    SQLite
Tech stack: Ruby, Sinatra, Prawn (PDF)
```

---

## Example 99

**Intent:**
I need something for my party rental company — bouncy castles, tables, chairs, marquees — where people can see what's available for their party date and book it, and my drivers get a list of drop-offs and pickups.

**Spec:**
```
Type:       Web application (party equipment rental)
Auth:       Customer accounts with email login; admin and driver logins
Data model: Item(id, name, category, quantity, daily_price, setup_required)
            Order(id, customer_id -> User, event_date, address, status, total)
            OrderItem(id, order_id -> Order, item_id -> Item, quantity)
            Run(id, date, driver_id -> User, type)
            RunStop(id, run_id -> Run, order_id -> Order, position)
Features:   - Show items available for a chosen event date
            - Book items and pay online
            - Block items already booked for that date
            - Create drop-off and pickup runs per driver
            - Show drivers their stops in order on a phone
API:        REST
            GET  /items/available?date={d}
            POST /orders
            GET  /runs?date={d}&driver={id}
Storage:    PostgreSQL
Tech stack: Python, Django, React
```

---

## Example 100

**Intent:**
shoe repair, simple: ticket, price, ready date, sms when done. using supabase

**Spec:**
```
Type:       Web application (repair ticketing)
Auth:       Supabase Auth email login for staff
Data model: Ticket(id, number, customer_name, phone, item, work, price, ready_on, status, created_at)
Features:   - Create a ticket with work description, price and ready date
            - List tickets due today and overdue
            - Mark tickets done and send an SMS
            - Mark tickets collected
API:        REST (Supabase auto-generated)
            GET  /rest/v1/tickets
            POST /rest/v1/tickets
            PATCH /rest/v1/tickets?id=eq.{id}
Storage:    Supabase (PostgreSQL)
Tech stack: React, Supabase, Supabase Edge Function (SMS via Twilio)
```

---

## Example 101

**Intent:**
conflict of interest check for new clients at a law firm

**Spec:**
```
Type:       Web application (conflict checking)
Auth:       Single sign-on with Microsoft Entra ID
Data model: Party(id, name, normalized_name, type)
            Matter(id, number, title, status)
            MatterParty(id, matter_id -> Matter, party_id -> Party, role)
            ConflictCheck(id, requested_by -> User, searched_names, result, cleared_by -> User, created_at)
Features:   - Search new client and opposing party names against all matters
            - Use fuzzy matching to catch spelling variations
            - Show matching matters with the party's role
            - Record who cleared the conflict check and when
API:        REST
            POST /conflict-checks
            GET  /conflict-checks/{id}
            POST /conflict-checks/{id}/clear
Storage:    PostgreSQL with pg_trgm
Tech stack: Python, FastAPI, React
```

---

## Example 102

**Intent:**
slack bot that tells our site managers which equipment is due for inspection this week

**Spec:**
```
Type:       Bot (Slack equipment inspection reminders)
Data model: Equipment(id, name, site, last_inspected_on, interval_days, slack_channel)
Features:   - Check every Monday which equipment is due for inspection
            - Post a list per site to that site's Slack channel
            - Let managers mark an item inspected with a slash command
            - Show overdue items in bold
API:        Slack Events API
            POST /slack/commands
            POST /slack/events
Storage:    PostgreSQL
Tech stack: Python, Slack Bolt, APScheduler
```

---

## Example 103

**Intent:**
gravestone and memorial mason order tracking from order to installation in cemetery

**Spec:**
```
Type:       Web application (memorial order tracking)
Auth:       Email + password login for office and workshop
Data model: MemorialOrder(id, family_contact, phone, cemetery, plot_ref, stone_type, inscription, status, price)
            Permit(id, order_id -> MemorialOrder, submitted_on, approved_on)
            Installation(id, order_id -> MemorialOrder, scheduled_on, fitter, done)
Features:   - Record memorial orders with exact inscription text
            - Track cemetery permit applications
            - Move orders through stages (proof, cutting, lettering, installed)
            - Send the family an inscription proof to approve
            - Schedule installation once the permit is approved
API:        REST
            POST /orders
            POST /orders/{id}/permit
            PATCH /orders/{id}/stage
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Blade
```

---

## Example 104

**Intent:**
Could you make a little tool so my sales team can configure a custom kitchen cabinet order — widths, doors, handles — and see the price as they go?

**Spec:**
```
Type:       Web application (product configurator)
Auth:       Email + password login for sales staff
Data model: CabinetType(id, name, allowed_widths, base_price)
            DoorStyle(id, name, price_factor)
            Handle(id, name, price)
            Configuration(id, customer_name, created_by -> User, total)
            ConfigItem(id, config_id -> Configuration, cabinet_type_id -> CabinetType, width_mm, door_id -> DoorStyle, handle_id -> Handle, price)
Features:   - Add cabinets with allowed widths only
            - Pick a door style and handle per cabinet
            - Update the total price live on every change
            - Save configurations and print an order summary
API:        REST
            GET  /catalogue
            POST /configurations
            GET  /configurations/{id}
Storage:    PostgreSQL
Tech stack: React, TypeScript, Node.js, Express
```

---

## Example 105

**Intent:**
crane hire lift plans approval

**Spec:**
```
Type:       Web application (lift plan management)
Auth:       Email + password login; roles: planner, appointed person, client
Data model: Crane(id, model, max_capacity_t, max_radius_m)
            LiftPlan(id, crane_id -> Crane, site, load_desc, load_weight_t, radius_m, lift_date, status)
            PlanApproval(id, plan_id -> LiftPlan, approver_id -> User, approved_at)
Features:   - Write a lift plan with load weight and radius
            - Check the load against the crane's capacity at that radius
            - Route the plan to the appointed person for sign-off
            - Share approved plans with the client as PDF
API:        REST
            POST /lift-plans
            POST /lift-plans/{id}/check
            POST /lift-plans/{id}/approve
Storage:    PostgreSQL
Tech stack: Python, Django, WeasyPrint
```

---

## Example 106

**Intent:**
i run a yoga retreat in portugal and need a site for people to book a room for a retreat week, some rooms shared some private

**Spec:**
```
Type:       Web application (retreat bookings)
Auth:       Admin login; guests book as guests
Data model: Retreat(id, title, start_date, end_date, teacher, description)
            Room(id, name, type, beds)
            RetreatPrice(id, retreat_id -> Retreat, room_type, price_per_person)
            Reservation(id, retreat_id -> Retreat, room_id -> Room, guest_name, email, beds_taken, dietary, paid)
Features:   - List retreat weeks with prices per room type
            - Book a bed in a shared room or a whole private room
            - Collect dietary needs and arrival details
            - Take a deposit and remind about the balance
API:        REST
            GET  /retreats
            GET  /retreats/{id}/availability
            POST /reservations
Storage:    PostgreSQL
Tech stack: WordPress, WooCommerce Bookings
```

---

## Example 107

**Intent:**
REST API for our wholesale customers' systems to place orders directly into our ERP

**Spec:**
```
Type:       REST API service (B2B order intake)
Auth:       OAuth 2.0 client credentials per customer
Data model: Customer(id, name, client_id, price_list_id)
            Order(id, customer_id -> Customer, external_ref, status, created_at)
            OrderLine(id, order_id -> Order, sku, quantity, unit_price)
Features:   - Accept orders with the customer's own reference
            - Validate SKUs and quantities against stock
            - Reject duplicate orders by external reference
            - Push accepted orders into the ERP
            - Send status updates to a customer webhook
API:        REST
            POST /v1/orders
            GET  /v1/orders/{id}
            GET  /v1/products
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Spring Security OAuth2
```

---

## Example 108

**Intent:**
chauffeur company booking airport transfers with flight number

**Spec:**
```
Type:       Web application (airport transfer booking)
Auth:       Customer accounts with email login; dispatcher admin
Data model: Vehicle(id, class, seats, luggage, rate_per_km)
            Transfer(id, customer_id -> User, pickup, dropoff, flight_number, pickup_at, vehicle_class, price, driver_id -> Driver, status)
            Driver(id, name, phone)
Features:   - Quote a price by vehicle class and distance
            - Book a transfer with flight number
            - Adjust pickup time automatically if the flight is delayed
            - Assign drivers from a dispatch board
            - Send the driver's details to the customer
API:        REST
            POST /quotes
            POST /transfers
            PATCH /transfers/{id}/assign
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, AviationStack API
```

---

## Example 109

**Intent:**
For my accounting practice, can we make a timer so staff record time against each client and task, and at month end I can see which fixed-fee clients are losing us money?

**Spec:**
```
Type:       Web application (time tracking and profitability)
Auth:       Email + password login; roles: partner, staff
Data model: Client(id, name, monthly_fee)
            Task(id, name)
            TimeEntry(id, user_id -> User, client_id -> Client, task_id -> Task, started_at, minutes)
            User(id, name, hourly_cost)
Features:   - Start and stop a timer against a client and task
            - Add time entries manually
            - Calculate cost of time per client per month
            - Compare cost of time with the fixed fee
            - Highlight unprofitable clients
API:        REST
            POST /time-entries
            GET  /reports/profitability?month={m}
Storage:    PostgreSQL
Tech stack: Python, Django, Vue.js
```

---

## Example 110

**Intent:**
online menu for our food truck that shows where we are parked today

**Spec:**
```
Type:       Web application (food truck location and menu)
Auth:       Owner login
Data model: Stop(id, date, location_name, lat, lng, opens_at, closes_at)
            MenuItem(id, name, price, sold_out)
Features:   - Show today's location on a map with opening hours
            - Show the week's planned stops
            - Show the menu with sold-out items marked
            - Let the owner update location from a phone in one tap
API:        REST
            GET  /today
            GET  /stops?week={w}
            POST /stops
Storage:    Firebase Firestore
Tech stack: React, Firebase, Leaflet
```

---

## Example 111

**Intent:**
dentist practice wants patients to fill in medical history form online before appointment

**Spec:**
```
Type:       Web application (pre-appointment patient forms)
Auth:       Patients verify with date of birth via a link; staff login
Data model: Patient(id, name, birth_date, email)
            FormInvite(id, patient_id -> Patient, appointment_at, token, completed)
            MedicalHistory(id, patient_id -> Patient, medications, allergies, conditions, smoker, submitted_at)
Features:   - Email patients a link to the form 3 days before their appointment
            - Pre-fill answers from their previous form
            - Highlight allergies and changes for the dentist
            - Store forms securely with an audit log
API:        REST
            GET  /forms/{token}
            POST /forms/{token}
            GET  /patients/{id}/history
Storage:    PostgreSQL (encrypted at rest)
Tech stack: C#, ASP.NET Core, Razor Pages
```

---

## Example 112

**Intent:**
greenhouse farm harvest and orders for restaurants

**Spec:**
```
Type:       Web application (farm-to-restaurant ordering)
Auth:       Email + password login for restaurant buyers; farm admin
Data model: Crop(id, name, unit, price)
            Availability(id, crop_id -> Crop, week_start, quantity)
            Order(id, restaurant_id -> User, delivery_date, status)
            OrderLine(id, order_id -> Order, crop_id -> Crop, quantity)
Features:   - Publish the expected harvest for the coming week
            - Let restaurants order within available quantities
            - Produce a harvest list per day
            - Invoice restaurants weekly
API:        REST
            GET  /availability?week={w}
            POST /orders
            GET  /admin/harvest-list?date={d}
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix
```

---

## Example 113

**Intent:**
need a gdpr data request tracker, people ask what data we have on them and we have 30 days to respond

**Spec:**
```
Type:       Web application (data subject request tracking)
Auth:       Email + password login for the privacy team
Data model: DataRequest(id, requester_name, email, type, received_on, due_on, status, verified)
            RequestTask(id, request_id -> DataRequest, system_name, owner_email, done)
            RequestNote(id, request_id -> DataRequest, body, created_at)
Features:   - Log access, deletion and correction requests
            - Calculate the 30-day deadline automatically
            - Create a task per system that holds personal data
            - Remind task owners and escalate near the deadline
            - Keep an audit trail of every action
API:        REST
            POST /requests
            GET  /requests?status={s}
            PATCH /tasks/{id}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 114

**Intent:**
we got 4 food trucks and i want to see sales from all of them in one dashboard, they use square

**Spec:**
```
Type:       Data dashboard (multi-location sales)
Features:   - Pull transactions from each truck's Square location every hour
            - Show daily revenue per truck
            - Show best-selling items per truck and overall
            - Compare sales by weekday and location stop
            - Show average order value over time
Input:      Square Payments and Orders API data
Storage:    PostgreSQL
Tech stack: Python, Square SDK, Metabase
```

---

## Example 115

**Intent:**
apartment cleaning checklist with photos for airbnb hosts we clean for

**Spec:**
```
Type:       Web application (turnover cleaning checklists)
Auth:       Email + password login; roles: cleaner, host, admin
Data model: Listing(id, host_id -> User, name, address)
            ChecklistItem(id, listing_id -> Listing, room, task, photo_required)
            Turnover(id, listing_id -> Listing, cleaner_id -> User, date, completed_at)
            TurnoverPhoto(id, turnover_id -> Turnover, item_id -> ChecklistItem, url)
Features:   - Keep a custom checklist per listing
            - Require photos for selected items
            - Let cleaners tick items off on their phone
            - Share a completion report with the host
            - Report damage or missing items
API:        REST
            GET  /turnovers/{id}
            POST /turnovers/{id}/photos
            POST /turnovers/{id}/complete
Storage:    PostgreSQL, S3
Tech stack: React Native Web, Node.js, Express
```

---

## Example 116

**Intent:**
web app to book driving tests practice route videos for students, they pay to unlock routes for their test centre

**Spec:**
```
Type:       Web application (paid video library)
Auth:       Email + password login
Data model: TestCentre(id, name, city)
            RouteVideo(id, centre_id -> TestCentre, title, video_url, duration_min)
            Purchase(id, user_id -> User, centre_id -> TestCentre, paid_at, expires_at)
Features:   - Search test centres by city
            - Preview one route free per centre
            - Unlock all routes for a centre with a one-off payment
            - Stream videos only for paid users
API:        REST
            GET  /centres?city={c}
            GET  /centres/{id}/routes
            POST /centres/{id}/purchase
Storage:    PostgreSQL, Mux (video)
Tech stack: Next.js, Stripe, Mux
```

---

## Example 117

**Intent:**
I own a small chain of 3 laundromats. Each machine takes card payment through a reader. I'd like a page where I see takings per store per day and which machines are earning the least so I can check if they're broken.

**Spec:**
```
Type:       Data dashboard (laundromat revenue)
Data model: Store(id, name)
            Machine(id, store_id -> Store, number, type)
            Transaction(id, machine_id -> Machine, amount, paid_at)
Features:   - Import card reader transactions nightly
            - Show takings per store per day and week
            - Rank machines by revenue
            - Flag machines with no transactions for 24 hours
            - Compare washers versus dryers
Input:      Card payment provider transaction export (CSV or API)
Storage:    PostgreSQL
Tech stack: Python, pandas, Grafana
```

---

## Example 118

**Intent:**
pharmacy prescription ready notification

**Spec:**
```
Type:       Web application (prescription ready alerts)
Auth:       Pharmacy staff login
Data model: Prescription(id, patient_name, phone, rx_ref, status, ready_at, collected_at)
Features:   - Mark a prescription as ready with one click
            - Send the patient an SMS that it is ready to collect
            - Send a reminder if not collected after 5 days
            - Show uncollected prescriptions to return to stock after 14 days
API:        REST
            POST /prescriptions
            PATCH /prescriptions/{id}/ready
            GET  /prescriptions/uncollected
Storage:    PostgreSQL
Tech stack: Node.js, Express, Twilio
```

---

## Example 119

**Intent:**
my company paints houses and every job we need to calculate how much paint and how many hours, do it on website please

**Spec:**
```
Type:       Web application (painting estimate calculator)
Auth:       Email + password login for estimators
Data model: Estimate(id, customer_name, address, created_by -> User, total)
            Surface(id, estimate_id -> Estimate, room, type, area_m2, coats, prep_level)
            PaintProduct(id, name, coverage_m2_per_l, price_per_l)
Features:   - Enter rooms and surfaces with measurements
            - Calculate litres of paint needed from coverage and coats
            - Estimate labour hours from area and prep level
            - Produce a customer quote with materials and labour
API:        REST
            POST /estimates
            POST /estimates/{id}/surfaces
            GET  /estimates/{id}/quote
Storage:    PostgreSQL
Tech stack: Python, Flask, Vue.js
```

---

## Example 120

**Intent:**
WooCommerce plugin for my bakery to let customers choose a pickup time slot at checkout

**Spec:**
```
Type:       Plugin (WooCommerce pickup slots)
Data model: PickupSlot(id, date, start_time, end_time, max_orders, orders_count)
Features:   - Add a pickup date and time selector to checkout
            - Limit the number of orders per slot
            - Hide slots that are full or less than 2 hours away
            - Show the chosen slot on the order and in emails
            - Let the admin set opening hours and closed days
Storage:    WordPress database (custom table)
Tech stack: PHP, WordPress, WooCommerce hooks, jQuery
```

---

## Example 121

**Intent:**
lumber yard delivery booking

**Spec:**
```
Type:       Web application (delivery slot booking)
Auth:       Staff login
Data model: Truck(id, name, max_load_kg, has_crane)
            Delivery(id, truck_id -> Truck, order_ref, customer, address, date, slot, load_kg, needs_crane)
Features:   - Book deliveries into AM and PM slots per truck
            - Check total load against the truck's limit
            - Only use crane trucks for crane deliveries
            - Print a driver's day sheet
API:        REST
            GET  /deliveries?date={d}
            POST /deliveries
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 122

**Intent:**
software for a vet practice to keep pet weight history and show a chart to the owner

**Spec:**
```
Type:       Web application (pet weight tracking)
Auth:       Staff login; owners log in with email
Data model: Pet(id, owner_id -> User, name, species, breed, target_weight_kg)
            WeightRecord(id, pet_id -> Pet, weight_kg, recorded_on, recorded_by)
Features:   - Record a pet's weight at each visit
            - Plot weight over time with the target band
            - Flag sudden weight changes of more than 10%
            - Let owners see their pet's chart
API:        REST
            POST /pets/{id}/weights
            GET  /pets/{id}/weights
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Chart.js
```

---

## Example 123

**Intent:**
compliance checklist for food trucks: daily fridge temps, cleaning, allergens, so health inspector can see records

**Spec:**
```
Type:       Web application (food safety records)
Auth:       Email + password login per business
Data model: Fridge(id, name, min_c, max_c)
            TempReading(id, fridge_id -> Fridge, temp_c, taken_by, taken_at)
            CleaningLog(id, area, done_by, done_at)
            AllergenSheet(id, dish, allergens, updated_at)
Features:   - Log fridge temperatures twice a day
            - Flag readings outside the safe range and record the action taken
            - Tick off daily cleaning tasks
            - Keep allergen sheets per dish
            - Export 90 days of records as a PDF for inspection
API:        REST
            POST /fridges/{id}/readings
            POST /cleaning
            GET  /export?days=90
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 124

**Intent:**
online consultation booking for an immigration lawyer, paid in advance, video call

**Spec:**
```
Type:       Web application (paid legal consultations)
Auth:       Clients sign up with email; lawyer admin
Data model: ConsultationType(id, name, duration_min, price)
            Availability(id, weekday, start_time, end_time)
            Consultation(id, type_id -> ConsultationType, client_id -> User, starts_at, video_link, paid, questionnaire)
Features:   - Choose a consultation type and a free time slot
            - Fill in a short questionnaire about the case
            - Pay before the booking is confirmed
            - Create a video meeting link automatically
            - Send reminders 24 hours and 1 hour before
API:        REST
            GET  /slots?type={id}
            POST /consultations
            POST /webhooks/payment
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, React, Stripe, Zoom API
```

---

## Example 125

**Intent:**
inventory of rental wedding decor — arches, vases, centerpieces — so we don't double book items between weddings

**Spec:**
```
Type:       Web application (decor rental inventory)
Auth:       Email + password login for staff
Data model: DecorItem(id, name, category, quantity, photo_url, replacement_cost)
            Event(id, couple_names, date, venue)
            Allocation(id, event_id -> Event, item_id -> DecorItem, quantity)
Features:   - Keep a photo catalogue of decor items
            - Allocate items to a wedding date
            - Block allocations over available quantity on that date
            - Produce a pick list per event
            - Record damaged or missing items after return
API:        REST
            GET  /items/available?date={d}
            POST /events/{id}/allocations
            GET  /events/{id}/pick-list
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Vue.js
```

---

## Example 126

**Intent:**
I'm a solo bookkeeper. Every month I chase clients for the same stuff. I want an automatic email that goes out on the 1st listing what each client still needs to send me, and stops once they've uploaded it.

**Spec:**
```
Type:       Scheduled script (client document chasing)
Data model: Client(id, name, email)
            Requirement(id, client_id -> Client, item, month, received)
Features:   - Create the month's requirements for each client on the 1st
            - Email each client a list of missing items
            - Check the client's upload folder for new files
            - Mark items received when a matching file appears
            - Send a follow-up every 5 days until complete
Input:      Client list and shared Google Drive upload folders
Storage:    SQLite
Tech stack: Python, Google Drive API, Gmail API, cron
```

---

## Example 127

**Intent:**
trophy engraving shop orders

**Spec:**
```
Type:       Web application (engraving orders)
Auth:       Staff login; clubs order as guests
Data model: Trophy(id, name, size, price)
            EngravingOrder(id, club_name, contact_email, needed_by, status)
            EngravingLine(id, order_id -> EngravingOrder, trophy_id -> Trophy, text, quantity)
Features:   - Order trophies with engraving text per line
            - Charge per letter above a free limit
            - Show the engraving queue ordered by needed-by date
            - Email the club when the order is ready
API:        REST
            POST /orders
            GET  /queue
            PATCH /orders/{id}/ready
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 128

**Intent:**
web app for horse livery yard: owners book services like turnout, rugs, feeding and get billed monthly

**Spec:**
```
Type:       Web application (livery yard services)
Auth:       Email + password login; roles: owner, yard staff, manager
Data model: Horse(id, owner_id -> User, name, stable_no, feed_plan)
            Service(id, name, price)
            ServiceRequest(id, horse_id -> Horse, service_id -> Service, date, done)
            MonthlyBill(id, owner_id -> User, month, total, paid)
Features:   - Let owners request daily services per horse
            - Show yard staff today's task list per stable
            - Tick off completed services
            - Generate a monthly bill per owner
API:        REST
            POST /horses/{id}/requests
            GET  /tasks?date={d}
            PATCH /requests/{id}/done
            GET  /bills?month={m}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Svelte
```

---

## Example 129

**Intent:**
Our hardware store wants to lend out a carpet cleaner and a tile cutter for free to loyal customers. Simple waiting list and loan log.

**Spec:**
```
Type:       Web application (loan and waitlist)
Auth:       Staff login
Data model: LoanItem(id, name, status)
            Customer(id, name, phone, loyalty_number)
            WaitlistEntry(id, item_id -> LoanItem, customer_id -> Customer, joined_at)
            Loan(id, item_id -> LoanItem, customer_id -> Customer, out_on, due_on, returned_on)
Features:   - Join a waiting list for an item
            - Lend the item to the next person in the queue
            - Text the next customer when the item comes back
            - Check the customer has a loyalty number
API:        REST
            POST /items/{id}/waitlist
            POST /items/{id}/loan
            POST /loans/{id}/return
Storage:    SQLite
Tech stack: Node.js, Express, Twilio
```

---

## Example 130

**Intent:**
want a chatbot on my plumbing website that asks what's wrong and books an emergency or normal visit

**Spec:**
```
Type:       Chatbot (service triage and booking)
Data model: Conversation(id, started_at, channel)
            Lead(id, conversation_id -> Conversation, name, phone, postcode, problem, urgency, slot)
Features:   - Ask guided questions about the plumbing problem
            - Classify the issue as emergency or routine
            - Offer emergency callout or routine booking slots
            - Collect name, phone and postcode
            - Send the lead to the office by email
API:        REST
            POST /chat/messages
            GET  /slots?urgency={u}
Storage:    PostgreSQL
Tech stack: JavaScript chat widget, Node.js, Rasa
```

---

## Example 131

**Intent:**
small print shop job queue for the presses

**Spec:**
```
Type:       Web application (production queue)
Auth:       Staff PIN login
Data model: Press(id, name, type)
            PrintJob(id, order_ref, customer, press_id -> Press, quantity, stock, due_at, position, status)
Features:   - Show a queue of jobs per press
            - Drag jobs to reorder priority
            - Mark jobs printing, finishing or done
            - Highlight jobs at risk of missing their due time
API:        REST
            GET  /presses/{id}/queue
            PATCH /jobs/{id}/position
            PATCH /jobs/{id}/status
Storage:    PostgreSQL
Tech stack: Vue.js, SortableJS, Node.js, Express
```

---

## Example 132

**Intent:**
contractor prequalification, subcontractors upload insurance and safety docs and we approve them before they work on our sites

**Spec:**
```
Type:       Web application (subcontractor prequalification)
Auth:       Email + password login for subcontractors; admin reviewers
Data model: Subcontractor(id, company, trade, contact_email, status)
            DocumentType(id, name, required, has_expiry)
            SubDocument(id, sub_id -> Subcontractor, type_id -> DocumentType, file_url, expires_on, approved)
Features:   - Let subcontractors register and upload required documents
            - Review and approve each document
            - Approve a subcontractor once all required documents are valid
            - Suspend subcontractors automatically when a document expires
            - Remind them 30 days before expiry
API:        REST
            POST /subcontractors
            POST /subcontractors/{id}/documents
            PATCH /documents/{id}/approve
Storage:    PostgreSQL, S3
Tech stack: Python, Django, Bootstrap
```

---

## Example 133

**Intent:**
plz make site for my piano tuning business so customers get remind every 6 month and book online

**Spec:**
```
Type:       Web application (recurring tuning reminders and booking)
Auth:       Single owner login; customers book as guests
Data model: Customer(id, name, email, phone, address)
            Piano(id, customer_id -> Customer, make, type, last_tuned_on)
            Appointment(id, piano_id -> Piano, scheduled_at, status)
Features:   - Book a tuning visit online
            - Record each tuning with notes on the piano
            - Email a reminder with a booking link 6 months after each tuning
            - Show the day's visits by area
API:        REST
            GET  /slots
            POST /appointments
            POST /pianos/{id}/tunings
Storage:    SQLite
Tech stack: Python, Flask, Mailgun
```

---

## Example 134

**Intent:**
marina fuel dock sales and boat account billing

**Spec:**
```
Type:       Web application (fuel dock point of sale)
Auth:       Staff PIN login
Data model: BoatAccount(id, boat_name, owner, berth, credit_limit)
            FuelSale(id, account_id -> BoatAccount, fuel_type, litres, price_per_l, total, sold_at, paid_now)
            Statement(id, account_id -> BoatAccount, month, total)
Features:   - Record fuel sales by litres and fuel type
            - Charge to a berth holder's account or take payment now
            - Block account sales over the credit limit
            - Produce monthly account statements
API:        REST
            POST /sales
            GET  /accounts/{id}/statement?month={m}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 135

**Intent:**
I manage a coworking space and people keep forgetting to tell us about guests. I'd like members to pre-register guests so reception gets a list and guests get a welcome email with wifi details.

**Spec:**
```
Type:       Web application (guest pre-registration)
Auth:       Member email + password login; reception staff login
Data model: Member(id, name, email, company)
            Guest(id, member_id -> Member, name, email, visit_date, arrived_at)
Features:   - Let members register guests for a date
            - Send guests a welcome email with address and wifi details
            - Show reception today's expected guests
            - Notify the member when their guest checks in
API:        REST
            POST /guests
            GET  /guests?date={d}
            POST /guests/{id}/check-in
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Nodemailer
```

---

## Example 136

**Intent:**
tile shop sample library: designers borrow tile samples and we track returns

**Spec:**
```
Type:       Web application (sample lending)
Auth:       Email + password login for trade designers; staff admin
Data model: Sample(id, sku, name, finish, size, available_count)
            SampleLoan(id, designer_id -> User, due_on, returned_on, status)
            SampleLoanItem(id, loan_id -> SampleLoan, sample_id -> Sample)
Features:   - Let designers request up to 10 samples at a time
            - Post or collect samples and set a return date
            - Remind designers of overdue samples
            - Charge for samples not returned after 30 days
API:        REST
            GET  /samples
            POST /loans
            POST /loans/{id}/return
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 137

**Intent:**
web form for warranty registration for the kitchen appliances we sell

**Spec:**
```
Type:       Web application (warranty registration)
Auth:       Admin login; customers register without an account
Data model: ProductModel(id, model_number, name, warranty_months)
            Registration(id, model_id -> ProductModel, serial_number, purchase_date, retailer, customer_name, email, receipt_url)
Features:   - Register a product with serial number and purchase date
            - Upload a photo of the receipt
            - Calculate the warranty end date
            - Email a warranty certificate
            - Let support staff look up a serial number
API:        REST
            POST /registrations
            GET  /registrations?serial={s}
Storage:    PostgreSQL, S3
Tech stack: Next.js, Prisma
```

---

## Example 138

**Intent:**
sawmill orders custom cut timber

**Spec:**
```
Type:       Web application (custom timber cutting orders)
Auth:       Email + password login for customers and mill staff
Data model: Species(id, name, price_per_m3)
            CutOrder(id, customer_id -> User, status, total, ready_on)
            CutLine(id, order_id -> CutOrder, species_id -> Species, length_mm, width_mm, thickness_mm, pieces)
Features:   - Order timber by species and exact dimensions
            - Calculate volume and price per line
            - Produce a cutting list for the sawyer
            - Notify the customer when the order is ready
API:        REST
            POST /orders
            GET  /orders/{id}/cutting-list
            PATCH /orders/{id}/ready
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 139

**Intent:**
Hello, I have small company that cleans offices at night. Client want proof we cleaned. Make please system where cleaner scan NFC tag in each room.

**Spec:**
```
Type:       Mobile application with backend (NFC cleaning verification)
Auth:       Email + password login for cleaners; client view login
Data model: Building(id, client_id -> User, name, address)
            Checkpoint(id, building_id -> Building, room_name, nfc_uid)
            Scan(id, checkpoint_id -> Checkpoint, cleaner_id -> User, scanned_at)
Features:   - Scan the NFC tag in each room with the phone
            - Record the time and cleaner for each scan
            - Show the client which rooms were cleaned each night
            - Alert the manager when rooms are missed
API:        REST
            POST /scans
            GET  /buildings/{id}/report?date={d}
Storage:    PostgreSQL
Tech stack: Android (Kotlin, NFC API), Node.js, Express
```

---

## Example 140

**Intent:**
mobile vet scheduling by route

**Spec:**
```
Type:       Web application (mobile veterinary scheduling)
Auth:       Email + password login for vets and reception
Data model: Client(id, name, address, lat, lng)
            Animal(id, client_id -> Client, name, species)
            HouseCall(id, client_id -> Client, vet_id -> User, date, reason, est_minutes, position)
Features:   - Book house calls with an estimated duration
            - Group calls by area for each vet and day
            - Order the day's calls to reduce driving time
            - Show the route on a map
API:        REST
            POST /house-calls
            GET  /vets/{id}/route?date={d}
Storage:    PostgreSQL
Tech stack: Python, Django, OpenRouteService API
```

---

## Example 141

**Intent:**
web portal for a property cleaning company where letting agents order end of tenancy cleans

**Spec:**
```
Type:       Web application (B2B cleaning orders)
Auth:       Email + password login per letting agency
Data model: Agency(id, name, billing_email)
            CleanOrder(id, agency_id -> Agency, address, bedrooms, bathrooms, keys_from, date, price, status)
            CleanReport(id, order_id -> CleanOrder, completed_at, photos_url)
Features:   - Order an end-of-tenancy clean with property size
            - Price automatically by bedrooms and bathrooms
            - Track the order until the clean is complete
            - Receive a photo report after the clean
            - Invoice each agency monthly
API:        REST
            POST /orders
            GET  /orders/{id}
            GET  /orders/{id}/report
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 142

**Intent:**
I'm a florist and I want to track standing orders from offices and hotels that get fresh flowers every Monday.

**Spec:**
```
Type:       Web application (recurring floral contracts)
Auth:       Single owner login
Data model: Account(id, name, address, contact)
            Arrangement(id, account_id -> Account, description, size, price, frequency)
            Delivery(id, arrangement_id -> Arrangement, date, delivered, notes)
Features:   - Store each account's standing arrangements
            - Generate the week's deliveries every Monday
            - Show a stem shopping list for the flower market
            - Invoice accounts monthly
API:        REST
            GET  /deliveries?week={w}
            GET  /shopping-list?week={w}
            PATCH /deliveries/{id}
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 143

**Intent:**
need a fleet fuel card report that flags weird fill ups like 2 in one hour or more litres than tank size

**Spec:**
```
Type:       Data analysis script (fuel card anomaly detection)
Features:   - Load fuel card transactions and vehicle list
            - Flag fill-ups larger than the vehicle's tank capacity
            - Flag two fill-ups for one vehicle within an hour
            - Flag fuel bought on weekends or far from the vehicle's base
            - Export flagged transactions to Excel for review
Input:      Fuel card CSV export and a vehicle list with tank sizes
Tech stack: Python, pandas, openpyxl
```

---

## Example 144

**Intent:**
Angular frontend + .NET backend for an engineering firm to request and approve overtime

**Spec:**
```
Type:       Web application (overtime approval)
Auth:       Single sign-on with Azure AD
Data model: Employee(id, name, email, manager_id -> Employee)
            OvertimeRequest(id, employee_id -> Employee, project_code, date, hours, reason, status)
Features:   - Request overtime with project code and reason
            - Route requests to the employee's manager
            - Approve or reject with a comment
            - Export approved overtime for payroll
API:        REST
            POST /api/overtime
            GET  /api/overtime/pending
            POST /api/overtime/{id}/decision
Storage:    SQL Server
Tech stack: Angular, C#, ASP.NET Core Web API, Entity Framework Core
```

---

## Example 145

**Intent:**
online gift vouchers for my spa

**Spec:**
```
Type:       Web application (gift vouchers)
Auth:       Staff login for redeeming
Data model: Voucher(id, code, amount, balance, buyer_email, recipient_name, message, expires_on)
            Redemption(id, voucher_id -> Voucher, amount, redeemed_at)
Features:   - Buy a gift voucher online for a chosen amount
            - Email a printable voucher with a unique code
            - Let staff check and redeem vouchers partly or fully
            - Expire vouchers after 12 months
API:        REST
            POST /vouchers
            GET  /vouchers/{code}
            POST /vouchers/{code}/redeem
Storage:    PostgreSQL
Tech stack: Node.js, Express, Stripe, PDFKit
```

---

## Example 146

**Intent:**
vehicle damage inspection when rental vans go out and come back, with photos on a car diagram

**Spec:**
```
Type:       Web application (vehicle condition reports)
Auth:       Staff email + password login
Data model: Van(id, registration, model)
            ConditionReport(id, van_id -> Van, type, mileage, fuel_level, customer_signature_url, created_at)
            DamageMark(id, report_id -> ConditionReport, panel, x, y, description, photo_url)
Features:   - Mark damage on a van diagram by tapping the panel
            - Attach a photo to each damage mark
            - Record mileage and fuel level at check-out and check-in
            - Compare check-in with check-out to show new damage
            - Get the customer's signature on screen
API:        REST
            POST /vans/{id}/reports
            GET  /vans/{id}/reports/compare
Storage:    PostgreSQL, S3
Tech stack: React, Konva.js, Node.js, Express
```

---

## Example 147

**Intent:**
ok so we're a family run funeral home and arranging a funeral is a lot of moving parts — the family picks a coffin, flowers, music, the celebrant, the venue, cars — and it's all on paper forms. I want a digital arrangement form that totals the cost and gives a checklist for the staff.

**Spec:**
```
Type:       Web application (funeral arrangements)
Auth:       Email + password login for funeral directors
Data model: Arrangement(id, deceased_name, family_contact, service_date, venue, director_id -> User, status)
            ProductOption(id, category, name, price)
            ArrangementItem(id, arrangement_id -> Arrangement, option_id -> ProductOption, quantity)
            Task(id, arrangement_id -> Arrangement, title, due_on, done)
Features:   - Fill in an arrangement with the family step by step
            - Choose coffin, flowers, cars and other options from a price list
            - Show a running total and produce an itemised estimate
            - Create a staff checklist from the chosen options
            - Track third-party fees such as cemetery and celebrant
API:        REST
            POST /arrangements
            POST /arrangements/{id}/items
            GET  /arrangements/{id}/estimate
            PATCH /tasks/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 148

**Intent:**
craft brewery wholesale orders from bars, kegs and cases, plus keg returns

**Spec:**
```
Type:       Web application (brewery wholesale and keg tracking)
Auth:       Email + password login for bar accounts; brewery admin
Data model: Product(id, beer, format, price, stock)
            Keg(id, serial, size_l, location, account_id -> Account)
            Account(id, venue_name, licence_no)
            Order(id, account_id -> Account, delivery_date, status)
            OrderLine(id, order_id -> Order, product_id -> Product, quantity)
Features:   - Let bars order kegs and cases online
            - Assign keg serial numbers on dispatch
            - Track which kegs are at which venue
            - Record empty keg collections
            - Flag kegs out for more than 60 days
API:        REST
            POST /orders
            POST /kegs/{serial}/dispatch
            POST /kegs/{serial}/return
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, React
```

---

## Example 149

**Intent:**
childminder app to log nappies meals naps for each kid and parents see it

**Spec:**
```
Type:       Mobile application with backend (childcare daily log)
Auth:       Email + password login; roles: childminder, parent
Data model: Child(id, name, birth_date, allergies)
            ParentLink(id, child_id -> Child, parent_id -> User)
            LogEntry(id, child_id -> Child, type, details, logged_at)
Features:   - Log meals, naps, nappy changes and activities quickly
            - Show parents a live timeline of their child's day
            - Highlight allergies on every meal entry
            - Send a daily summary at pickup time
API:        REST
            POST /children/{id}/log
            GET  /children/{id}/log?date={d}
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase
```

---

## Example 150

**Intent:**
gutter cleaning company, want quotes based on house type and number of floors from a web form

**Spec:**
```
Type:       Web application (instant quote form)
Auth:       Admin login
Data model: PriceRule(id, house_type, floors, base_price)
            QuoteLead(id, name, phone, email, postcode, house_type, floors, extras, price, created_at)
Features:   - Ask for house type, number of floors and extras
            - Show an instant price
            - Save the lead and email it to the office
            - Let the admin edit price rules
API:        REST
            POST /quotes
            GET  /admin/leads
            PUT  /admin/price-rules
Storage:    SQLite
Tech stack: Python, Flask, Alpine.js
```

---

## Example 151

**Intent:**
court bundle builder for litigation

**Spec:**
```
Type:       Web application (court bundle preparation)
Auth:       Email + password login for legal staff
Data model: Bundle(id, case_ref, title, created_by -> User, status)
            BundleSection(id, bundle_id -> Bundle, title, position)
            BundleDocument(id, section_id -> BundleSection, file_url, title, doc_date, position, page_count)
Features:   - Upload PDFs and arrange them into sections by drag and drop
            - Sort documents by date within a section
            - Generate an index with page numbers
            - Merge everything into one paginated, bookmarked PDF
API:        REST
            POST /bundles
            POST /bundles/{id}/documents
            POST /bundles/{id}/build
Storage:    PostgreSQL, S3
Tech stack: Python, FastAPI, pypdf, React
```

---

## Example 152

**Intent:**
i sell meat from my farm as half and quarter cow shares, need people reserve a share and pay deposit, then pay rest by hanging weight

**Spec:**
```
Type:       Web application (beef share reservations)
Auth:       Customer email login; farmer admin
Data model: Animal(id, tag, processing_date, hanging_weight_kg, status)
            Share(id, animal_id -> Animal, size, customer_id -> User, deposit_paid, cut_sheet)
            Invoice(id, share_id -> Share, weight_kg, price_per_kg, balance_due, paid)
Features:   - Show available half and quarter shares per animal
            - Reserve a share with a deposit
            - Fill in a cut sheet for butchering preferences
            - Calculate the balance from hanging weight after processing
            - Email the final invoice and pickup date
API:        REST
            GET  /shares/available
            POST /shares/{id}/reserve
            POST /animals/{id}/weight
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 153

**Intent:**
web app that shows our cement mixer trucks on a map live

**Spec:**
```
Type:       Web application (live fleet map)
Auth:       Email + password login for dispatchers
Data model: Truck(id, fleet_no, driver_name, tracker_id)
            Position(id, truck_id -> Truck, lat, lng, speed_kmh, drum_rotating, recorded_at)
Features:   - Receive GPS positions from truck trackers every 30 seconds
            - Show all trucks on a live map
            - Show whether the drum is rotating or discharging
            - Replay a truck's route for a chosen day
API:        REST + WebSocket
            POST /trackers/positions
            GET  /trucks
            GET  /trucks/{id}/history?date={d}
            WS   /live
Storage:    TimescaleDB
Tech stack: Go, Leaflet, React
```

---

## Example 154

**Intent:**
I run a tutoring centre and I need to give each tutor a monthly payslip based on hours taught, but the rate is different for group and private lessons.

**Spec:**
```
Type:       Web application (tutor pay calculation)
Auth:       Email + password login; roles: admin, tutor
Data model: Tutor(id, name, email, private_rate, group_rate)
            TaughtLesson(id, tutor_id -> Tutor, date, type, hours, students)
            Payslip(id, tutor_id -> Tutor, month, private_hours, group_hours, total)
Features:   - Record lessons taught with type and hours
            - Calculate monthly pay with separate private and group rates
            - Generate payslip PDFs
            - Let tutors view their payslips and lesson list
API:        REST
            POST /lessons
            POST /payslips/generate?month={m}
            GET  /tutors/{id}/payslips
Storage:    PostgreSQL
Tech stack: Python, Django, WeasyPrint
```

---

## Example 155

**Intent:**
wine shop tasting event tickets

**Spec:**
```
Type:       Web application (event ticketing)
Auth:       Staff login; customers buy as guests
Data model: Tasting(id, title, date, capacity, price, wines_list)
            Ticket(id, tasting_id -> Tasting, buyer_name, email, quantity, code, checked_in)
Features:   - List upcoming tastings with the wines poured
            - Sell tickets until capacity is reached
            - Email tickets with a QR code
            - Check guests in at the door by scanning
API:        REST
            GET  /tastings
            POST /tastings/{id}/tickets
            POST /tickets/{code}/check-in
Storage:    PostgreSQL
Tech stack: SvelteKit, Stripe, qrcode
```

---

## Example 156

**Intent:**
security guard patrol checkpoints, guards scan qr at each point and supervisor see missed ones

**Spec:**
```
Type:       Web application (guard patrol tracking)
Auth:       Email + password login; roles: guard, supervisor
Data model: Site(id, name, client)
            Checkpoint(id, site_id -> Site, name, qr_token)
            PatrolRound(id, site_id -> Site, guard_id -> User, started_at, finished_at)
            CheckpointScan(id, round_id -> PatrolRound, checkpoint_id -> Checkpoint, scanned_at, note)
Features:   - Scan each checkpoint's QR code with the phone camera
            - Add an incident note or photo at a checkpoint
            - Show supervisors missed checkpoints per round
            - Send clients a nightly patrol report
API:        REST
            POST /rounds
            POST /rounds/{id}/scans
            GET  /sites/{id}/report?date={d}
Storage:    PostgreSQL
Tech stack: React (PWA), html5-qrcode, Node.js, Express
```

---

## Example 157

**Intent:**
car dealership needs to track trade-in valuations and reconditioning costs before putting the car up for sale

**Spec:**
```
Type:       Web application (trade-in and reconditioning)
Auth:       Email + password login for sales and workshop staff
Data model: TradeIn(id, vin, make, model, mileage, appraised_value, appraised_by -> User, status)
            ReconItem(id, trade_in_id -> TradeIn, description, cost, done)
            Listing(id, trade_in_id -> TradeIn, asking_price, listed_on)
Features:   - Record trade-in appraisals with photos
            - Add reconditioning jobs with costs
            - Show total cost (appraisal + recon) per car
            - Suggest a minimum asking price from target margin
            - Track days from trade-in to listing
API:        REST
            POST /trade-ins
            POST /trade-ins/{id}/recon
            POST /trade-ins/{id}/list
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stimulus
```

---

## Example 158

**Intent:**
For our dog training school: puppy courses run over 6 weeks, people sign up for a whole course not single classes, and we want a waitlist when a course is full.

**Spec:**
```
Type:       Web application (course enrolment with waitlist)
Auth:       Email + password login for owners; trainer admin
Data model: Course(id, name, level, start_date, weeks, weekday, time, capacity, price)
            Dog(id, owner_id -> User, name, age_months)
            Enrolment(id, course_id -> Course, dog_id -> Dog, status, paid)
Features:   - List courses by level and start date
            - Enrol a dog for the whole course and pay
            - Add to a waitlist when the course is full
            - Offer freed places to the waitlist in order
            - Check puppies meet the age range for the course
API:        REST
            GET  /courses
            POST /courses/{id}/enrol
            DELETE /enrolments/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 159

**Intent:**
reconcile supplier invoices against purchase orders and goods received

**Spec:**
```
Type:       Web application (three-way invoice matching)
Auth:       Single sign-on with Google Workspace
Data model: PurchaseOrder(id, number, supplier, total)
            POLine(id, po_id -> PurchaseOrder, sku, qty, unit_price)
            GoodsReceipt(id, po_id -> PurchaseOrder, received_on)
            GRLine(id, receipt_id -> GoodsReceipt, sku, qty)
            SupplierInvoice(id, po_id -> PurchaseOrder, number, total, status)
Features:   - Match each invoice line to PO and goods received quantities
            - Flag price and quantity differences over a tolerance
            - Approve matched invoices for payment
            - Send exceptions to the buyer to resolve
API:        REST
            POST /invoices
            POST /invoices/{id}/match
            GET  /invoices/exceptions
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 160

**Intent:**
art class sign up

**Spec:**
```
Type:       Web application (class signup)
Auth:       Admin login
Data model: ArtClass(id, title, date, time, materials_included, capacity, price)
            Signup(id, class_id -> ArtClass, name, email, paid)
Features:   - List upcoming art classes
            - Sign up and pay online
            - Close signups when full
            - Email a reminder the day before
API:        REST
            GET  /classes
            POST /classes/{id}/signups
Storage:    SQLite
Tech stack: Python, Flask, Stripe Checkout
```

---

## Example 161

**Intent:**
fire alarm service company needs to record annual tests of each detector in a building

**Spec:**
```
Type:       Web application (fire alarm maintenance records)
Auth:       Email + password login for engineers; building manager view
Data model: Building(id, name, address, manager_email)
            Device(id, building_id -> Building, zone, location, type, device_code)
            ServiceVisit(id, building_id -> Building, engineer_id -> User, date)
            DeviceTest(id, visit_id -> ServiceVisit, device_id -> Device, result, note)
Features:   - Keep a register of detectors and call points per building
            - Test devices during a visit, a quarter of the system each time
            - Ensure every device is tested at least once a year
            - Record faults and remedial work needed
            - Issue a service certificate to the building manager
API:        REST
            POST /buildings/{id}/visits
            POST /visits/{id}/tests
            GET  /buildings/{id}/untested
Storage:    PostgreSQL
Tech stack: Python, Django, React
```

---

## Example 162

**Intent:**
we sell and service commercial coffee machines to cafes. need to track machines at each cafe and service history

**Spec:**
```
Type:       Web application (installed equipment service)
Auth:       Email + password login for technicians and office
Data model: Cafe(id, name, address, contact)
            Machine(id, cafe_id -> Cafe, model, serial, installed_on, under_contract)
            ServiceCall(id, machine_id -> Machine, reported_issue, technician_id -> User, visited_on, work_done, parts)
Features:   - Keep a register of machines installed at each cafe
            - Log service calls and repairs
            - Schedule descaling and preventive maintenance
            - Bill calls not covered by contract
API:        REST
            GET  /cafes/{id}/machines
            POST /machines/{id}/calls
            GET  /maintenance/due
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 163

**Intent:**
web booking for a sauna boat on the river, groups book 2 hour slots

**Spec:**
```
Type:       Web application (slot booking)
Auth:       Admin login; customers book as guests
Data model: SaunaSlot(id, starts_at, duration_min, capacity, private_price, seat_price)
            SaunaBooking(id, slot_id -> SaunaSlot, name, email, seats, private, total)
Features:   - Show 2-hour slots for the week
            - Book single seats or the whole boat privately
            - Prevent seat bookings on privately booked slots
            - Pay online and get a confirmation
API:        REST
            GET  /slots?week={w}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Node.js, Express, Stripe
```

---

## Example 164

**Intent:**
My wife runs a bridal makeup business and goes to weddings with 2 assistants. She needs to quote per person, book the date and assign assistants, and keep a trial booking before the wedding.

**Spec:**
```
Type:       Web application (on-location beauty booking)
Auth:       Email + password login for the artist and assistants
Data model: Wedding(id, bride_name, email, date, location, ready_by_time, status)
            Service(id, name, price, minutes)
            WeddingService(id, wedding_id -> Wedding, service_id -> Service, people)
            Trial(id, wedding_id -> Wedding, date, done)
            StaffAssignment(id, wedding_id -> Wedding, staff_id -> User)
Features:   - Quote per person and service, plus travel fee
            - Book the wedding date with a deposit
            - Schedule a trial before the wedding
            - Assign assistants depending on number of people
            - Build the morning schedule backwards from the ready-by time
API:        REST
            POST /weddings
            POST /weddings/{id}/trial
            GET  /weddings/{id}/schedule
Storage:    PostgreSQL
Tech stack: Next.js, Prisma, Stripe
```

---

## Example 165

**Intent:**
staff training matrix for a manufacturing plant - who is trained on which machine

**Spec:**
```
Type:       Web application (training matrix)
Auth:       Email + password login for supervisors
Data model: Employee(id, name, department)
            Machine(id, name, area)
            Training(id, employee_id -> Employee, machine_id -> Machine, level, trained_on, trainer, expires_on)
Features:   - Show a grid of employees vs machines with training level
            - Record training with trainer and date
            - Highlight machines with fewer than two trained operators
            - Alert when refresher training is due
API:        REST
            GET  /matrix
            POST /trainings
Storage:    PostgreSQL
Tech stack: Vue.js, Python, FastAPI
```

---

## Example 166

**Intent:**
please site where pupils of my driving school can see how many lessons they have left in their package

**Spec:**
```
Type:       Web application (lesson package balance)
Auth:       Email + password login for pupils; instructor admin
Data model: Pupil(id, name, email, phone)
            Package(id, pupil_id -> Pupil, lessons_bought, bought_on, price)
            LessonUse(id, pupil_id -> Pupil, date, hours)
Features:   - Sell lesson packages (5, 10 or 20 hours)
            - Deduct hours after each lesson
            - Show pupils their remaining hours and lesson history
            - Remind pupils when 2 hours are left
API:        REST
            GET  /me/balance
            POST /pupils/{id}/packages
            POST /pupils/{id}/lessons
Storage:    SQLite
Tech stack: PHP, Laravel
```

---

## Example 167

**Intent:**
API that gives lead times for our custom furniture based on current order backlog

**Spec:**
```
Type:       REST API service (lead time estimation)
Auth:       API key for the website and sales tools
Data model: ProductType(id, name, build_hours)
            BacklogOrder(id, product_type_id -> ProductType, quantity, status)
            Capacity(id, workshop_hours_per_week)
Features:   - Sum remaining build hours of all open orders
            - Calculate weeks until a new order could start
            - Return an estimated delivery date per product type
            - Recalculate when orders change status
API:        REST
            GET  /lead-time?product_type={id}&quantity={n}
            POST /backlog/sync
Storage:    PostgreSQL
Tech stack: Python, FastAPI
```

---

## Example 168

**Intent:**
church donations tracking with yearly statements for tax

**Spec:**
```
Type:       Web application (donation records)
Auth:       Email + password login for treasurers
Data model: Donor(id, name, email, address, gift_aid_declared)
            Donation(id, donor_id -> Donor, amount, method, fund, received_on)
Features:   - Record donations by method (cash, card, bank transfer)
            - Allocate donations to funds
            - Generate yearly giving statements per donor
            - Export gift aid claims
API:        REST
            POST /donations
            GET  /donors/{id}/statement?year={y}
            GET  /exports/gift-aid?year={y}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 169

**Intent:**
tool crib checkout at the mine site with badge scan

**Spec:**
```
Type:       Web application (tool crib management)
Auth:       Badge scan for workers; crib attendant login
Data model: Worker(id, badge_id, name, crew)
            Tool(id, tag, name, calibration_due)
            ToolIssue(id, tool_id -> Tool, worker_id -> Worker, issued_at, returned_at)
Features:   - Scan a worker's badge and tool tag to issue a tool
            - Block tools that are overdue for calibration
            - Show tools not returned at end of shift
            - Report tool losses by crew
API:        REST
            POST /issues
            POST /issues/{id}/return
            GET  /issues/open
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor Server
```

---

## Example 170

**Intent:**
Hi! We are a family company producing olive oil in Greece. We want to sell bottles online to customers in Europe, with shipping price by country.

**Spec:**
```
Type:       Web application (online shop with country shipping)
Auth:       Customer accounts optional; admin login
Data model: Product(id, name, volume_ml, price, stock)
            ShippingRate(id, country_code, weight_from_kg, weight_to_kg, price)
            Order(id, email, country_code, address, subtotal, shipping, total, status)
            OrderItem(id, order_id -> Order, product_id -> Product, quantity)
Features:   - Show products in English and Greek
            - Calculate shipping by country and parcel weight
            - Pay by card or PayPal
            - Email order confirmation and tracking number
API:        REST
            GET  /products
            GET  /shipping?country={c}&weight={kg}
            POST /orders
Storage:    PostgreSQL
Tech stack: Medusa.js, Next.js, Stripe, PayPal
```

---

## Example 171

**Intent:**
client intake questionnaire for a family law practice

**Spec:**
```
Type:       Web application (legal client intake)
Auth:       Clients use a secure invite link; staff login with 2FA
Data model: IntakeInvite(id, client_email, token, expires_at, completed)
            IntakeForm(id, invite_id -> IntakeInvite, full_name, spouse_name, children_count, matter_type, summary, submitted_at)
            IntakeDocument(id, form_id -> IntakeForm, file_url, label)
Features:   - Send a secure intake link to a new client
            - Ask conditional questions depending on the matter type
            - Let the client save progress and continue later
            - Upload supporting documents
            - Create a draft matter for the lawyer from the answers
API:        REST
            POST /invites
            GET  /intake/{token}
            PUT  /intake/{token}
            POST /intake/{token}/submit
Storage:    PostgreSQL (encrypted at rest), S3
Tech stack: TypeScript, Remix, Prisma
```

---

## Example 172

**Intent:**
concrete pour schedule for our batching plant

**Spec:**
```
Type:       Web application (concrete delivery scheduling)
Auth:       Email + password login for dispatch and sales
Data model: Mix(id, code, strength_mpa, price_per_m3)
            Pour(id, customer, site_address, mix_id -> Mix, volume_m3, pour_date, start_time, rate_m3_per_h, status)
            Load(id, pour_id -> Pour, truck_no, volume_m3, batched_at, delivered_at)
Features:   - Book pours with mix, volume and start time
            - Split each pour into truck loads
            - Show plant capacity per hour so pours don't clash
            - Record batch and delivery time for each load
API:        REST
            GET  /pours?date={d}
            POST /pours
            POST /pours/{id}/loads
Storage:    PostgreSQL
Tech stack: Python, Django, FullCalendar
```

---

## Example 173

**Intent:**
i want my customers at the bakery to collect stamps on their phone, every 10 coffees one free

**Spec:**
```
Type:       Web application (digital loyalty card)
Auth:       Customers log in with phone number + SMS code; staff PIN
Data model: Customer(id, phone, name, stamps, free_available)
            StampEvent(id, customer_id -> Customer, staff_id -> User, created_at, type)
Features:   - Show the customer a QR code on their phone
            - Let staff scan it to add a stamp
            - Give a free coffee reward after 10 stamps
            - Redeem the reward at the counter
            - Block more than one stamp per 5 minutes
API:        REST
            POST /auth/sms
            POST /customers/{id}/stamp
            POST /customers/{id}/redeem
Storage:    PostgreSQL
Tech stack: React (PWA), Node.js, Express, Twilio Verify
```

---

## Example 174

**Intent:**
For our accounting firm we'd like engagement letters to be generated from a template, sent to the client and e-signed, and then stored against the client.

**Spec:**
```
Type:       Web application (engagement letters with e-signature)
Auth:       Email + password login for staff
Data model: Client(id, name, email, entity_type)
            Template(id, name, body_markdown)
            EngagementLetter(id, client_id -> Client, template_id -> Template, services, fee, status, envelope_id, signed_pdf_url)
Features:   - Fill a letter template with client name, services and fee
            - Send the letter for e-signature
            - Track sent, viewed and signed status
            - Store the signed PDF against the client
API:        REST
            POST /letters
            POST /letters/{id}/send
            POST /webhooks/docusign
Storage:    PostgreSQL, S3
Tech stack: Python, Django, DocuSign eSignature API
```

---

## Example 175

**Intent:**
taxidermy orders

**Spec:**
```
Type:       Web application (commission order tracking)
Auth:       Single owner login
Data model: Customer(id, name, phone, email)
            Specimen(id, customer_id -> Customer, species, mount_type, received_on, tag_number, deposit, price, status)
Features:   - Log each specimen with a tag number and mount type
            - Track stages (received, tanning, mounting, finishing, ready)
            - Record deposits and balance due
            - Text the customer when the mount is ready
API:        REST
            POST /specimens
            PATCH /specimens/{id}/stage
Storage:    SQLite
Tech stack: Python, Flask, Twilio
```

---

## Example 176

**Intent:**
manage permit to work forms for maintenance on a chemical plant, needs approvals before work starts

**Spec:**
```
Type:       Web application (permit to work)
Auth:       Single sign-on with company Active Directory
Data model: Permit(id, type, equipment_tag, description, requested_by -> User, valid_from, valid_to, status)
            Isolation(id, permit_id -> Permit, point, method, applied_by -> User, verified)
            PermitApproval(id, permit_id -> Permit, role, approver_id -> User, approved_at)
Features:   - Raise a permit for hot work, confined space or electrical work
            - List isolations and require them to be verified
            - Require area authority and safety approvals before issue
            - Show all active permits on a plant map
            - Close permits with sign-off that the area is safe
API:        REST
            POST /permits
            POST /permits/{id}/isolations
            POST /permits/{id}/approve
            POST /permits/{id}/close
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, React
```

---

## Example 177

**Intent:**
can i get a web app where my photography studio clients pick their headshot retouching options and pay extra per photo

**Spec:**
```
Type:       Web application (photo selection and upsells)
Auth:       Clients log in with a gallery code; photographer admin
Data model: Session(id, client_name, email, code, included_images)
            Image(id, session_id -> Session, url, thumbnail_url)
            Pick(id, image_id -> Image, retouch_level, price)
Features:   - Show proofs from the client's session
            - Pick included images and buy extra ones
            - Choose a retouching level per image with its price
            - Pay for extras online
            - Give the photographer a retouching job list
API:        REST
            GET  /sessions/{code}
            POST /sessions/{code}/picks
            POST /sessions/{code}/checkout
Storage:    PostgreSQL, S3
Tech stack: Vue.js, Node.js, Express, Stripe
```

---

## Example 178

**Intent:**
nightly job that pulls our dealer stock from the DMS and posts it to car listing websites

**Spec:**
```
Type:       Scheduled script (vehicle stock syndication)
Features:   - Export current used-car stock from the dealer management system
            - Map fields to each listing site's feed format
            - Upload photos that changed since the last run
            - Remove sold cars from the feeds
            - Email a summary of added, updated and removed cars
Input:      DMS stock export (XML) and photo folder
Storage:    SQLite (sync state)
Tech stack: Python, lxml, requests, cron
```

---

## Example 179

**Intent:**
self-service kiosk at our hardware store so customers can order paint mixed to a colour code

**Spec:**
```
Type:       Web application (paint mixing order kiosk)
Auth:       Kiosk mode; staff login for the mixing station
Data model: ColourCode(id, brand, code, name, hex)
            PaintBase(id, finish, size_l, price)
            MixOrder(id, colour_id -> ColourCode, base_id -> PaintBase, quantity, customer_name, status, created_at)
Features:   - Search colours by code or name and preview the colour
            - Choose finish, can size and quantity
            - Send the order to the mixing station queue
            - Show a "ready" screen with order numbers
API:        REST
            GET  /colours?q={q}
            POST /mix-orders
            PATCH /mix-orders/{id}/status
Storage:    PostgreSQL
Tech stack: React, Node.js, Socket.IO
```

---

## Example 180

**Intent:**
online exam booking for a language school's certification tests with seat limits per date

**Spec:**
```
Type:       Web application (exam registration)
Auth:       Candidates register with email and ID number; admin login
Data model: ExamSession(id, level, date, room, seats, fee)
            Candidate(id, name, birth_date, id_number, email)
            Registration(id, session_id -> ExamSession, candidate_id -> Candidate, paid, result)
Features:   - List exam dates per level with seats left
            - Register and pay the exam fee
            - Close registration 3 weeks before the exam
            - Print attendance lists per room
            - Publish results to candidates
API:        REST
            GET  /sessions?level={l}
            POST /registrations
            PATCH /registrations/{id}/result
Storage:    PostgreSQL
Tech stack: PHP, Symfony, Stripe
```

---

## Example 181

**Intent:**
we're a small IT support company and want our clients to submit tickets by email and track them on a portal

**Spec:**
```
Type:       Web application (helpdesk ticketing)
Auth:       Email + password login; roles: client user, technician
Data model: ClientCompany(id, name, email_domain, sla_hours)
            Ticket(id, company_id -> ClientCompany, requester_email, subject, priority, status, assigned_to -> User, created_at)
            Reply(id, ticket_id -> Ticket, author_email, body, created_at)
Features:   - Turn incoming support emails into tickets
            - Match the sender's domain to the client company
            - Reply by email and keep the thread on the ticket
            - Show clients their open tickets
            - Warn when a ticket is close to breaching the SLA
API:        REST
            POST /inbound-email
            GET  /tickets
            POST /tickets/{id}/replies
Storage:    PostgreSQL
Tech stack: Python, Django, Mailgun inbound routing
```

---

## Example 182

**Intent:**
caravan park pitch bookings

**Spec:**
```
Type:       Web application (campsite pitch booking)
Auth:       Admin login; guests book with email
Data model: Pitch(id, number, type, has_hookup, max_length_m)
            PitchBooking(id, pitch_id -> Pitch, guest_name, email, arrive_on, depart_on, people, dogs, total)
            Rate(id, type, season, nightly)
Features:   - Search free pitches by type and dates
            - Price by season, people and electric hookup
            - Show a site map with pitch status
            - Email arrival information
API:        REST
            GET  /pitches/available
            POST /bookings
Storage:    PostgreSQL
Tech stack: Node.js, Express, Svelte
```

---

## Example 183

**Intent:**
helping my uncle with his carpet shop. he goes to houses to measure rooms and then has to work out how much carpet with the roll width and seams. i want a web tool for that

**Spec:**
```
Type:       Web application (carpet measuring and quoting)
Auth:       Single user login
Data model: Job(id, customer_name, address, created_at)
            Room(id, job_id -> Job, name, length_m, width_m)
            Carpet(id, name, roll_width_m, price_per_m2)
            JobCarpet(id, room_id -> Room, carpet_id -> Carpet, cut_length_m, waste_m2)
Features:   - Enter room sizes for a job
            - Work out cut lengths from the roll width, including seams
            - Show waste per room and total area to order
            - Price carpet, underlay and fitting
            - Print a cutting plan and quote
API:        REST
            POST /jobs
            POST /jobs/{id}/rooms
            GET  /jobs/{id}/quote
Storage:    SQLite
Tech stack: Python, Flask, SVG cutting diagrams
```

---

## Example 184

**Intent:**
supplier scorecard, rate our suppliers on delivery time quality and price every quarter

**Spec:**
```
Type:       Web application (supplier performance scorecards)
Auth:       Email + password login for purchasing and quality staff
Data model: Supplier(id, name, category)
            Delivery(id, supplier_id -> Supplier, promised_on, delivered_on, lines, rejected_lines)
            Scorecard(id, supplier_id -> Supplier, quarter, on_time_pct, quality_pct, price_score, total)
Features:   - Import deliveries and quality rejections from the ERP
            - Calculate on-time delivery and quality percentages
            - Let buyers enter a price competitiveness score
            - Rank suppliers each quarter
            - Share a scorecard PDF with each supplier
API:        REST
            POST /deliveries/import
            POST /scorecards/generate?quarter={q}
            GET  /suppliers/{id}/scorecards
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 185

**Intent:**
reservations for a pick your own strawberry farm so it doesnt get too crowded

**Spec:**
```
Type:       Web application (timed entry booking)
Auth:       Admin login; visitors book as guests
Data model: EntrySlot(id, date, start_time, capacity, open)
            Visit(id, slot_id -> EntrySlot, name, email, party_size, checked_in)
Features:   - Show hourly entry slots with spaces left
            - Book a slot for a party
            - Close days quickly when fields are picked out
            - Check visitors in at the gate
API:        REST
            GET  /slots?date={d}
            POST /visits
            PATCH /slots/{id}/close
Storage:    PostgreSQL
Tech stack: Next.js, Vercel Postgres
```

---

## Example 186

**Intent:**
web tool to schedule our window cleaners in rounds, every 4 or 8 weeks per house

**Spec:**
```
Type:       Web application (cleaning round scheduling)
Auth:       Email + password login
Data model: Round(id, name, area)
            House(id, round_id -> Round, address, price, frequency_weeks, last_cleaned_on)
            Clean(id, house_id -> House, done_on, paid)
Features:   - Group houses into rounds by street
            - Show which houses are due on each round this week
            - Mark houses cleaned and paid from a phone
            - List customers who owe money
API:        REST
            GET  /rounds/{id}/due
            POST /houses/{id}/cleans
            GET  /debts
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Turbo
```

---

## Example 187

**Intent:**
Dear developer, we are notary office. We need system where clients book appointment and upload documents before, so we prepare the deed.

**Spec:**
```
Type:       Web application (notary appointments and documents)
Auth:       Clients register with email and identity document; staff login
Data model: Client(id, name, email, id_number)
            Appointment(id, client_id -> Client, act_type, scheduled_at, notary_id -> User, status)
            UploadedDocument(id, appointment_id -> Appointment, kind, file_url, verified)
Features:   - Book an appointment and choose the type of deed
            - Show the documents needed for that deed type
            - Upload documents in advance
            - Let staff verify documents and request missing ones
API:        REST
            POST /appointments
            POST /appointments/{id}/documents
            PATCH /documents/{id}/verify
Storage:    PostgreSQL, S3
Tech stack: Java, Spring Boot, Thymeleaf
```

---

## Example 188

**Intent:**
greenhouse sensors dashboard for our nursery

**Spec:**
```
Type:       IoT system (greenhouse monitoring)
Data model: Greenhouse(id, name)
            Sensor(id, greenhouse_id -> Greenhouse, type, device_id)
            Reading(id, sensor_id -> Sensor, value, recorded_at)
            AlertRule(id, greenhouse_id -> Greenhouse, metric, min, max)
Features:   - Read temperature, humidity and soil moisture every 5 minutes
            - Show live and historical charts per greenhouse
            - Send an SMS when values go outside the set range
            - Detect sensors that stop reporting
API:        MQTT topics + REST
            GET  /greenhouses/{id}/readings
            PUT  /alert-rules/{id}
Storage:    InfluxDB
Tech stack: ESP32, MQTT, Node-RED, Grafana
```

---

## Example 189

**Intent:**
online order form for custom printed t-shirts for sports clubs, sizes per player

**Spec:**
```
Type:       Web application (team kit ordering)
Auth:       Club organiser email login; admin login
Data model: ClubOrder(id, club_name, organiser_id -> User, design_url, deadline, status)
            PlayerLine(id, order_id -> ClubOrder, player_name, size, number, paid)
            Garment(id, name, sizes, price)
Features:   - Create a club order with a design and deadline
            - Share a link so players add their name, size and number
            - Let each player pay their own share
            - Lock the order at the deadline and send a size breakdown to production
API:        REST
            POST /club-orders
            POST /club-orders/{id}/players
            GET  /club-orders/{id}/breakdown
Storage:    PostgreSQL
Tech stack: Django, Stripe, Bootstrap
```

---

## Example 190

**Intent:**
small dental lab needs a web price list where dentists log in and see their own discounted prices

**Spec:**
```
Type:       Web application (customer-specific price list)
Auth:       Email + password login for dentists; lab admin
Data model: Restoration(id, name, category, list_price)
            Practice(id, name, discount_pct)
            PriceOverride(id, practice_id -> Practice, restoration_id -> Restoration, price)
Features:   - Show the price list grouped by category
            - Apply the practice's discount or override price
            - Download the price list as PDF
            - Let the admin update list prices yearly
API:        REST
            GET  /prices
            PUT  /admin/restorations/{id}
            PUT  /admin/practices/{id}/overrides
Storage:    PostgreSQL
Tech stack: Node.js, Express, Handlebars
```

---

## Example 191

**Intent:**
cleaning company quote from square meters and frequency, then auto make a contract

**Spec:**
```
Type:       Web application (commercial cleaning quotes and contracts)
Auth:       Email + password login for sales staff
Data model: Quote(id, client_name, email, area_m2, visits_per_week, hours_per_visit, price_per_month, status)
            Contract(id, quote_id -> Quote, start_date, term_months, signed_at, pdf_url)
Features:   - Estimate cleaning hours from floor area and building type
            - Calculate monthly price from hours and visits per week
            - Send the quote to the client
            - Turn an accepted quote into a contract PDF to sign online
API:        REST
            POST /quotes
            POST /quotes/{id}/accept
            GET  /contracts/{id}.pdf
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Jinja2, WeasyPrint
```

---

## Example 192

**Intent:**
our warehouse does cycle counts. want a phone page where pickers count a bin and it shows if it doesn't match the system

**Spec:**
```
Type:       Web application (cycle counting)
Auth:       Email + password login for warehouse staff
Data model: Bin(id, code, zone)
            BinStock(id, bin_id -> Bin, sku, system_qty)
            CountTask(id, bin_id -> Bin, assigned_to -> User, due_on, status)
            CountResult(id, task_id -> CountTask, sku, counted_qty, variance)
Features:   - Generate daily count tasks so every bin is counted each quarter
            - Scan the bin barcode and enter counted quantities
            - Hide the system quantity until the count is entered
            - Flag variances for a recount
            - Post approved adjustments back to stock
API:        REST
            GET  /count-tasks/mine
            POST /count-tasks/{id}/results
            POST /variances/{id}/approve
Storage:    PostgreSQL
Tech stack: Vue.js (mobile), Python, FastAPI
```

---

## Example 193

**Intent:**
web calendar for our tow truck dispatch

**Spec:**
```
Type:       Web application (tow dispatch board)
Auth:       Dispatcher and driver logins
Data model: TowJob(id, caller_name, phone, pickup_location, dropoff_location, vehicle, reason, status, driver_id -> Driver, created_at)
            Driver(id, name, truck_type, status, lat, lng)
Features:   - Log incoming tow calls
            - Show available drivers and their last location
            - Assign a job and send it to the driver's phone
            - Track job status until vehicle is dropped off
API:        REST + WebSocket
            POST /jobs
            PATCH /jobs/{id}/assign
            WS   /dispatch
Storage:    PostgreSQL
Tech stack: Node.js, Socket.IO, React
```

---

## Example 194

**Intent:**
I run a small chain of three bakeries and every evening the managers text me how many of each item was wasted. It's a mess. I want a simple page where they enter the waste, and I get a weekly chart to adjust how much we bake.

**Spec:**
```
Type:       Web application (waste tracking)
Auth:       Email + password login; roles: owner, shop manager
Data model: Shop(id, name)
            Item(id, name, unit_cost)
            WasteEntry(id, shop_id -> Shop, item_id -> Item, date, baked, wasted)
Features:   - Enter baked and wasted quantities per item each evening
            - Calculate waste percentage and cost per shop
            - Show a weekly chart per item and shop
            - Suggest a bake quantity from the last 4 same weekdays
API:        REST
            POST /waste
            GET  /reports/weekly?shop={id}
            GET  /suggestions?shop={id}&date={d}
Storage:    PostgreSQL
Tech stack: Python, Django, Chart.js
```

---

## Example 195

**Intent:**
hoa architectural requests approval

**Spec:**
```
Type:       Web application (architectural review requests)
Auth:       Email + password login; roles: homeowner, committee member
Data model: Property(id, address, owner_id -> User)
            ChangeRequest(id, property_id -> Property, description, plans_url, status, submitted_at)
            Vote(id, request_id -> ChangeRequest, member_id -> User, decision, comment)
Features:   - Submit a request for an exterior change with plans
            - Let committee members vote and comment
            - Approve when a majority votes yes
            - Notify the homeowner of the decision
API:        REST
            POST /requests
            POST /requests/{id}/votes
            GET  /requests?status={s}
Storage:    PostgreSQL
Tech stack: Next.js, Prisma
```

---

## Example 196

**Intent:**
customers of my upholstery business want to choose fabric from swatches online and get a price for recovering their sofa

**Spec:**
```
Type:       Web application (upholstery fabric selection and quote)
Auth:       Admin login; customers request as guests
Data model: Fabric(id, name, colour, price_per_m, swatch_url, in_stock)
            FurnitureType(id, name, metres_needed, labour_price)
            QuoteRequest(id, furniture_type_id -> FurnitureType, fabric_id -> Fabric, name, email, photo_url, total)
Features:   - Browse fabric swatches by colour and price
            - Pick a furniture type and fabric to see an estimated price
            - Upload a photo of the piece
            - Request a free swatch sample by post
API:        REST
            GET  /fabrics
            POST /quotes
            POST /swatch-requests
Storage:    PostgreSQL
Tech stack: Astro, Netlify Functions, Cloudinary
```

---

## Example 197

**Intent:**
something with airtable for my wedding planning business to auto send vendors the timeline a week before

**Spec:**
```
Type:       Scheduled script (vendor timeline emails)
Features:   - Read weddings happening in 7 days from Airtable
            - Collect each wedding's vendors and timeline rows
            - Build a timeline PDF per wedding
            - Email each vendor the timeline with their arrival time highlighted
            - Mark the wedding as "timeline sent" in Airtable
Input:      Airtable base with Weddings, Vendors and Timeline tables
Tech stack: Python, pyairtable, ReportLab, SendGrid, GitHub Actions (daily cron)
```

---

## Example 198

**Intent:**
bus company school route registration where parents register kids for a stop

**Spec:**
```
Type:       Web application (school transport registration)
Auth:       Email + password login for parents; admin login
Data model: Route(id, name, school, capacity)
            Stop(id, route_id -> Route, name, pickup_time, lat, lng)
            Rider(id, parent_id -> User, child_name, grade, stop_id -> Stop, status)
Features:   - Show routes and stops on a map
            - Register a child for a stop
            - Put registrations on a waitlist when the bus is full
            - Print rider lists per route for drivers
            - Email parents when pickup times change
API:        REST
            GET  /routes
            POST /riders
            GET  /routes/{id}/riders
Storage:    PostgreSQL
Tech stack: Python, Django, Leaflet
```

---

## Example 199

**Intent:**
online deposit-taking for puppy reservations from our breeding kennel

**Spec:**
```
Type:       Web application (litter reservations)
Auth:       Breeder admin login; buyers sign up with email
Data model: Litter(id, dam, sire, born_on, expected_on, status)
            Puppy(id, litter_id -> Litter, sex, colour, price, status)
            Reservation(id, puppy_id -> Puppy, buyer_id -> User, position, deposit_paid)
            Application(id, buyer_id -> User, home_info, approved)
Features:   - Let buyers fill an application before reserving
            - Join a pick list for a litter with a deposit
            - Assign puppies in pick order
            - Post weekly puppy photos to reserved buyers
API:        REST
            POST /applications
            POST /litters/{id}/reservations
            PATCH /reservations/{id}/puppy
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 200

**Intent:**
quality nonconformance reports with root cause and corrective actions

**Spec:**
```
Type:       Web application (NCR and CAPA tracking)
Auth:       Single sign-on with Okta
Data model: NCR(id, number, part_number, description, qty_affected, raised_by -> User, disposition, status)
            RootCause(id, ncr_id -> NCR, method, cause)
            CorrectiveAction(id, ncr_id -> NCR, action, owner_id -> User, due_on, verified_on)
Features:   - Raise a nonconformance with photos and quantity affected
            - Choose a disposition (scrap, rework, use as is)
            - Record root cause with 5-why analysis
            - Assign corrective actions with due dates
            - Verify effectiveness before closing
API:        REST
            POST /ncrs
            POST /ncrs/{id}/root-cause
            POST /ncrs/{id}/actions
            POST /ncrs/{id}/close
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Angular
```

---

## Example 201

**Intent:**
billable hours tracker for barristers chambers

**Spec:**
```
Type:       Web application (fee and diary management)
Auth:       Email + password login with 2FA; roles: barrister, clerk
Data model: Barrister(id, name, call_year, hourly_rate)
            Brief(id, barrister_id -> Barrister, instructing_solicitor, case_name, fee_type, agreed_fee, status)
            WorkItem(id, brief_id -> Brief, date, hours, description)
            FeeNote(id, brief_id -> Brief, amount, issued_on, paid_on)
Features:   - Let clerks log incoming briefs and agreed fees
            - Record hours worked per brief
            - Issue fee notes to instructing solicitors
            - Chase unpaid fee notes after 30 days
API:        REST
            POST /briefs
            POST /briefs/{id}/work
            POST /briefs/{id}/fee-notes
            GET  /fee-notes/overdue
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 202

**Intent:**
bakery production planner that turns tomorrow's orders into a mixing plan with flour water salt amounts

**Spec:**
```
Type:       Web application (production planning)
Auth:       Email + password login for bakers
Data model: Product(id, name, dough_id -> Dough, dough_weight_g)
            Dough(id, name, hydration_pct, salt_pct, yeast_pct)
            ProductionOrder(id, product_id -> Product, date, quantity)
Features:   - Sum tomorrow's orders per product
            - Calculate total dough weight per dough type
            - Break each dough into flour, water, salt and yeast using baker's percentages
            - Split mixes that are bigger than the mixer capacity
            - Print a mixing sheet for the night shift
API:        REST
            GET  /plan?date={d}
            POST /orders
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 203

**Intent:**
hey so i run a little boat rental on a lake, kayaks and pedal boats by the hour. want people book online and see whats free

**Spec:**
```
Type:       Web application (hourly boat rental)
Auth:       Admin login; customers book as guests
Data model: BoatType(id, name, seats, hourly_price, quantity)
            Rental(id, boat_type_id -> BoatType, name, phone, date, start_hour, hours, paid, status)
Features:   - Show free kayaks and pedal boats per hour
            - Book one or more hours and pay online
            - Close bookings automatically when the weather is bad
            - Show staff today's rentals and boats out on the water
API:        REST
            GET  /availability?date={d}
            POST /rentals
            PATCH /rentals/{id}/return
Storage:    SQLite
Tech stack: Python, Flask, Stripe
```

---

## Example 204

**Intent:**
estimating software for a roofing contractor using satellite roof measurements

**Spec:**
```
Type:       Web application (roof estimating)
Auth:       Email + password login for estimators
Data model: Estimate(id, address, lat, lng, pitch, area_m2, material_id -> Material, total)
            Material(id, name, price_per_m2, waste_pct)
            Facet(id, estimate_id -> Estimate, polygon_geojson, area_m2)
Features:   - Show a satellite image of the address
            - Draw roof facets on the map to measure area
            - Correct area for roof pitch
            - Price materials with waste and labour
            - Produce a proposal PDF
API:        REST
            POST /estimates
            POST /estimates/{id}/facets
            GET  /estimates/{id}/proposal
Storage:    PostgreSQL with PostGIS
Tech stack: React, Mapbox GL Draw, Turf.js, Node.js
```

---

## Example 205

**Intent:**
I'd like a page for my accountancy clients to see their tax return progress like a pizza tracker.

**Spec:**
```
Type:       Web application (job progress tracker)
Auth:       Client magic-link login; staff login
Data model: Client(id, name, email)
            Job(id, client_id -> Client, type, tax_year, stage, updated_at)
            StageChange(id, job_id -> Job, stage, changed_by -> User, changed_at)
Features:   - Show each job as a step tracker (received, in progress, review, ready to sign, filed)
            - Let staff move a job to the next stage
            - Email the client when it is ready to sign
            - Show the expected completion date
API:        REST
            GET  /me/jobs
            PATCH /jobs/{id}/stage
Storage:    PostgreSQL
Tech stack: Next.js, Prisma, Resend
```

---

## Example 206

**Intent:**
brewery taproom keg line cleaning log

**Spec:**
```
Type:       Web application (maintenance log)
Auth:       Staff PIN login
Data model: Line(id, tap_number, current_beer)
            CleaningLog(id, line_id -> Line, cleaned_by, cleaned_at, chemical, notes)
Features:   - Record line cleaning per tap
            - Show days since each line was last cleaned
            - Flag lines overdue past 14 days
            - Track which beer is on each tap
API:        REST
            POST /lines/{id}/cleanings
            GET  /lines
Storage:    SQLite
Tech stack: Node.js, Express, HTMX
```

---

## Example 207

**Intent:**
web app for a sign language interpreting agency to match interpreters to booking requests

**Spec:**
```
Type:       Web application (interpreter booking and matching)
Auth:       Email + password login; roles: client, interpreter, coordinator
Data model: Interpreter(id, name, qualifications, regions, hourly_rate)
            Request(id, client_id -> User, setting, address, starts_at, duration_min, remote, status)
            Offer(id, request_id -> Request, interpreter_id -> Interpreter, status)
Features:   - Let clients request an interpreter with setting and time
            - Find available interpreters with the right qualification and region
            - Offer the job to several interpreters, first to accept wins
            - Confirm the booking to the client
            - Record actual hours for invoicing
API:        REST
            POST /requests
            POST /requests/{id}/offers
            POST /offers/{id}/accept
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio SMS
```

---

## Example 208

**Intent:**
online rota for church volunteers so they can swap shifts

**Spec:**
```
Type:       Web application (volunteer rota)
Auth:       Email + password login for volunteers; admin
Data model: Role(id, name)
            Shift(id, role_id -> Role, date, volunteer_id -> User)
            SwapRequest(id, shift_id -> Shift, requested_by -> User, accepted_by -> User, status)
Features:   - Show the rota by month and role
            - Request a swap for a shift
            - Let another volunteer take the swap
            - Email a reminder the day before a shift
API:        REST
            GET  /rota?month={m}
            POST /shifts/{id}/swap
            POST /swaps/{id}/accept
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 209

**Intent:**
we fabricate stainless steel kitchens for restaurants and need a job board for the workshop: cutting, bending, welding, polishing, install

**Spec:**
```
Type:       Web application (workshop job board)
Auth:       Email + password login; roles: office, workshop
Data model: Job(id, number, client, due_on, status)
            Part(id, job_id -> Job, name, drawing_url, quantity)
            Operation(id, part_id -> Part, step, done_by, done_at)
Features:   - Show a kanban board of parts by operation
            - Move parts between cutting, bending, welding and polishing
            - Open the drawing for each part from the card
            - Show jobs at risk of missing the install date
API:        REST
            GET  /board
            POST /parts/{id}/operations
            GET  /jobs/at-risk
Storage:    PostgreSQL
Tech stack: React, react-beautiful-dnd, Node.js, Express
```

---

## Example 210

**Intent:**
tool to calculate how many staff a cleaning contract needs and roster them

**Spec:**
```
Type:       Web application (contract staffing and rostering)
Auth:       Email + password login for operations managers
Data model: Contract(id, client, weekly_hours, days, start_time)
            Cleaner(id, name, max_hours_per_week, availability_json)
            RosterShift(id, contract_id -> Contract, cleaner_id -> Cleaner, date, hours)
Features:   - Calculate cleaners needed from weekly hours and days
            - Generate a roster that respects each cleaner's availability
            - Warn when a cleaner exceeds their maximum hours
            - Publish the roster to cleaners by email
API:        REST
            POST /contracts/{id}/roster
            GET  /roster?week={w}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, OR-Tools, React
```

---

## Example 211

**Intent:**
online auction for our used farm machinery

**Spec:**
```
Type:       Web application (timed online auction)
Auth:       Email + password login with verified phone for bidders
Data model: Lot(id, title, description, photos, reserve_price, ends_at, status)
            Bid(id, lot_id -> Lot, bidder_id -> User, amount, created_at)
Features:   - List machinery lots with photos and specs
            - Place bids above the current bid plus increment
            - Extend the end time by 2 minutes on last-minute bids
            - Email the winner and notify outbid users
            - Hide the reserve but show if it is met
API:        REST + WebSocket
            GET  /lots
            POST /lots/{id}/bids
            WS   /lots/{id}/live
Storage:    PostgreSQL, Redis
Tech stack: Node.js, Socket.IO, React
```

---

## Example 212

**Intent:**
nursing agency where nurses pick open shifts at care homes from their phone

**Spec:**
```
Type:       Mobile application with backend (shift marketplace)
Auth:       Email + password login with document verification for nurses; care home logins
Data model: CareHome(id, name, address)
            OpenShift(id, care_home_id -> CareHome, role, starts_at, ends_at, rate, status)
            Nurse(id, name, pin_number, dbs_checked_until)
            ShiftClaim(id, shift_id -> OpenShift, nurse_id -> Nurse, status)
Features:   - Let care homes post open shifts
            - Show nurses shifts near them that match their role
            - Claim a shift and get confirmation
            - Block nurses whose checks have expired
            - Record timesheets signed by the care home
API:        REST
            GET  /shifts/open
            POST /shifts/{id}/claim
            POST /shifts/{id}/timesheet
Storage:    PostgreSQL
Tech stack: React Native, Node.js, NestJS
```

---

## Example 213

**Intent:**
web shop for my print shop where businesses upload print ready pdf files with their order

**Spec:**
```
Type:       Web application (print ordering with file upload)
Auth:       Business customer accounts with email login
Data model: Product(id, name, size, paper, price_per_100)
            PrintOrder(id, customer_id -> User, product_id -> Product, quantity, file_url, preflight_status, status)
Features:   - Choose a product and quantity with live pricing
            - Upload a print-ready PDF
            - Check PDF page size, bleed and resolution automatically
            - Reject files that fail checks with a clear reason
            - Track the order until shipped
API:        REST
            POST /orders
            POST /orders/{id}/file
            GET  /orders/{id}
Storage:    PostgreSQL, S3
Tech stack: Python, Django, PyMuPDF
```

---

## Example 214

**Intent:**
Ok this might be odd but I run a small cemetery for our town and the plot records are in an old ledger. I'd like to put them online so families can search for where someone is buried, and we can see which plots are still free.

**Spec:**
```
Type:       Web application (cemetery plot records)
Auth:       Staff login; public search without login
Data model: Section(id, name)
            Plot(id, section_id -> Section, row, number, status, lat, lng)
            Interment(id, plot_id -> Plot, full_name, born_on, died_on, buried_on)
            PlotOwner(id, plot_id -> Plot, name, purchased_on)
Features:   - Search burials by name and year
            - Show the plot location on a cemetery map
            - Show free and reserved plots to staff
            - Enter old ledger records in bulk from a spreadsheet
API:        REST
            GET  /search?name={n}
            GET  /plots?status=free
            POST /admin/import
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django, Leaflet
```

---

## Example 215

**Intent:**
order system for a seafood wholesaler, prices change daily

**Spec:**
```
Type:       Web application (daily price wholesale ordering)
Auth:       Email + password login for restaurant accounts; staff admin
Data model: Product(id, species, cut, unit)
            DailyPrice(id, product_id -> Product, date, price, available_kg)
            Order(id, account_id -> User, delivery_date, status)
            OrderLine(id, order_id -> Order, product_id -> Product, kg, price)
Features:   - Publish today's catch with prices each morning
            - Let restaurants order before the cut-off time
            - Lock the price at the time of ordering
            - Charge by actual weight after packing
            - Notify customers when the price list is published
API:        REST
            GET  /prices/today
            POST /orders
            PATCH /order-lines/{id}/actual-weight
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Inertia.js, Vue
```

---

## Example 216

**Intent:**
web app to book tasting appointments for wedding cakes

**Spec:**
```
Type:       Web application (tasting appointments)
Auth:       Admin login; couples book as guests
Data model: TastingSlot(id, starts_at, is_booked)
            TastingBooking(id, slot_id -> TastingSlot, couple_names, email, wedding_date, guests, flavours_chosen, fee_paid)
Features:   - Show tasting slots on Saturdays
            - Let couples choose up to 4 flavours to taste
            - Charge a tasting fee that is deducted from the cake order
            - Remind couples 2 days before
API:        REST
            GET  /slots
            POST /bookings
Storage:    SQLite
Tech stack: SvelteKit, Stripe
```

---

## Example 217

**Intent:**
elevator maintenance company, record monthly inspections per lift, building owners see reports

**Spec:**
```
Type:       Web application (lift maintenance records)
Auth:       Email + password login; roles: engineer, building owner, admin
Data model: Building(id, name, owner_id -> User)
            Lift(id, building_id -> Building, serial, type, floors)
            Inspection(id, lift_id -> Lift, engineer_id -> User, date, result, findings)
            Breakdown(id, lift_id -> Lift, reported_at, fixed_at, cause)
Features:   - Record monthly inspections with a checklist
            - Log breakdowns and time to fix
            - Show owners the inspection history and uptime per lift
            - Alert when a lift misses its monthly inspection
API:        REST
            POST /lifts/{id}/inspections
            POST /lifts/{id}/breakdowns
            GET  /buildings/{id}/report
Storage:    PostgreSQL
Tech stack: Python, Django, Chart.js
```

---

## Example 218

**Intent:**
i need to keep my funeral home's pre-paid funeral plans organised, who paid what installments and which plan they chose

**Spec:**
```
Type:       Web application (pre-need plan management)
Auth:       Email + password login for staff
Data model: PlanHolder(id, name, birth_date, address, phone)
            Plan(id, holder_id -> PlanHolder, plan_type, total_price, installments, start_date, status)
            Installment(id, plan_id -> Plan, due_on, amount, paid_on)
Features:   - Record plans with chosen service options
            - Generate an installment schedule
            - Mark installments paid and send receipts
            - List overdue installments
            - Show the plan details quickly when the holder passes away
API:        REST
            POST /plans
            POST /installments/{id}/pay
            GET  /installments/overdue
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Razor Pages
```

---

## Example 219

**Intent:**
bathroom fitter project tracker for customer with photos each day

**Spec:**
```
Type:       Web application (customer project updates)
Auth:       Fitter login; customer access via private link
Data model: Project(id, customer_name, address, start_date, end_date, status, share_token)
            DailyUpdate(id, project_id -> Project, date, summary)
            UpdatePhoto(id, update_id -> DailyUpdate, url)
Features:   - Post a daily update with photos from the phone
            - Share a private progress page with the customer
            - Show the planned schedule and what is next
            - Let the customer ask questions on each update
API:        REST
            POST /projects/{id}/updates
            GET  /share/{token}
            POST /updates/{id}/comments
Storage:    PostgreSQL, Cloudinary
Tech stack: Ruby on Rails, Active Storage
```

---

## Example 220

**Intent:**
online check-in for guests at my B&B with ID scan and arrival time

**Spec:**
```
Type:       Web application (online guest check-in)
Auth:       Guests open a link from the booking email; host login
Data model: Stay(id, guest_name, email, arrive_on, nights, check_in_token)
            CheckIn(id, stay_id -> Stay, arrival_time, id_photo_url, guests, car_reg, completed_at)
Features:   - Email guests a check-in link 3 days before arrival
            - Collect arrival time, number of guests and car registration
            - Upload a photo of an ID document as required by law
            - Delete ID photos 30 days after check-out
API:        REST
            GET  /check-in/{token}
            POST /check-in/{token}
Storage:    PostgreSQL, S3 (with lifecycle rule)
Tech stack: Node.js, Express, React
```

---

## Example 221

**Intent:**
compliance training due dates for drivers in a trucking company — licence, medical, tacho card

**Spec:**
```
Type:       Web application (driver compliance)
Auth:       Email + password login for transport managers
Data model: Driver(id, name, email, depot)
            Credential(id, driver_id -> Driver, type, number, expires_on, file_url)
            LicenceCheck(id, driver_id -> Driver, checked_on, points, result)
Features:   - Store each driver's licence, medical and tacho card with expiry
            - Email the driver and manager 60 and 30 days before expiry
            - Record licence checks every 3 months
            - Show a red/amber/green status per driver
API:        REST
            POST /drivers/{id}/credentials
            GET  /compliance/status
            POST /drivers/{id}/licence-checks
Storage:    PostgreSQL
Tech stack: Python, Flask, Celery
```

---

## Example 222

**Intent:**
mobile coffee cart event bookings with menu packages and travel fee

**Spec:**
```
Type:       Web application (event catering booking)
Auth:       Owner admin login
Data model: Package(id, name, cups_included, price, hours)
            EventBooking(id, package_id -> Package, client, email, date, address, distance_km, travel_fee, total, status)
Features:   - Choose a package by number of cups and hours
            - Calculate a travel fee from distance
            - Request a date and pay a deposit
            - Let the owner confirm or decline
API:        REST
            GET  /packages
            GET  /travel-fee?address={a}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Next.js, Google Maps Distance Matrix API, Stripe
```

---

## Example 223

**Intent:**
web portal where farmers sell hay bales to horse owners, with delivery

**Spec:**
```
Type:       Web application (local hay marketplace)
Auth:       Email + password login; roles: farmer, buyer
Data model: Listing(id, farmer_id -> User, type, bale_size, price_per_bale, quantity, location, cut_year)
            HayOrder(id, listing_id -> Listing, buyer_id -> User, bales, delivery, address, status)
Features:   - Let farmers list hay and straw with bale size and price
            - Search listings by distance
            - Order with delivery or collection
            - Message between buyer and farmer
API:        REST
            GET  /listings?near={lat,lng}
            POST /listings/{id}/orders
            POST /orders/{id}/messages
Storage:    PostgreSQL with PostGIS
Tech stack: Django, GeoDjango, Leaflet
```

---

## Example 224

**Intent:**
Telegram bot for my cleaning crew to get their daily addresses and report done

**Spec:**
```
Type:       Bot (Telegram job dispatch)
Data model: Cleaner(id, name, telegram_chat_id)
            Job(id, cleaner_id -> Cleaner, address, date, time, status)
Features:   - Send each cleaner their jobs every morning at 7
            - Include a map link for each address
            - Let cleaners tap "Done" under each job
            - Notify the manager when all jobs are done or one is late
API:        Telegram Bot API (webhook)
            POST /telegram/webhook
Storage:    SQLite
Tech stack: Python, python-telegram-bot, APScheduler
```

---

## Example 225

**Intent:**
asset depreciation register for a small company's accountant

**Spec:**
```
Type:       Web application (fixed asset register)
Auth:       Email + password login for finance staff
Data model: AssetClass(id, name, method, useful_life_years)
            FixedAsset(id, class_id -> AssetClass, description, cost, acquired_on, disposed_on, disposal_value)
            DepreciationEntry(id, asset_id -> FixedAsset, period, amount, book_value)
Features:   - Register assets with cost and acquisition date
            - Calculate monthly depreciation (straight line or reducing balance)
            - Record disposals and gain or loss
            - Export depreciation journals for the accounting system
API:        REST
            POST /assets
            POST /depreciation/run?period={p}
            GET  /journals?period={p}
Storage:    PostgreSQL
Tech stack: Python, Django, pandas
```

---

## Example 226

**Intent:**
schedule for our mobile tyre fitting vans with postcodes

**Spec:**
```
Type:       Web application (mobile service scheduling)
Auth:       Staff login; customers book as guests
Data model: Van(id, name, base_postcode)
            ServiceArea(id, van_id -> Van, postcode_prefix)
            MobileBooking(id, van_id -> Van, customer, address, postcode, tyre_size, quantity, date, slot)
Features:   - Check the postcode is served by a van
            - Offer only that van's free slots
            - Reserve tyres for the job
            - Send the fitter's ETA by SMS on the day
API:        REST
            GET  /availability?postcode={p}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js, Twilio
```

---

## Example 227

**Intent:**
client portal for a architects firm to share drawings and approve stages

**Spec:**
```
Type:       Web application (architecture client portal)
Auth:       Email + password login for clients and staff
Data model: Project(id, client_id -> User, name, address, stage)
            Deliverable(id, project_id -> Project, stage, title, file_url, uploaded_at)
            StageSignoff(id, project_id -> Project, stage, signed_by -> User, signed_at)
            FeeStage(id, project_id -> Project, stage, amount, invoiced)
Features:   - Share drawings and documents per project stage
            - Let clients sign off a stage before work continues
            - Invoice the fee for a stage when signed off
            - Keep a comment thread per drawing
API:        REST
            GET  /projects/{id}
            POST /projects/{id}/deliverables
            POST /projects/{id}/signoff
Storage:    PostgreSQL, S3
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 228

**Intent:**
buy and sell second hand school uniforms for our school PTA

**Spec:**
```
Type:       Web application (uniform resale)
Auth:       Email + password login for parents; PTA volunteer admin
Data model: UniformItem(id, type, size, condition, price, status, donated_by -> User)
            Reservation(id, item_id -> UniformItem, parent_id -> User, collect_on, paid)
Features:   - List donated uniform items by type and size
            - Reserve items and collect at school
            - Mark items sold and record money raised
            - Show stock gaps by size
API:        REST
            GET  /items?type={t}&size={s}
            POST /items/{id}/reserve
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 229

**Intent:**
For a dog grooming salon: every dog has grooming notes like "nervous, use blade 7, no ears", and the groomer must see them before starting. Please also before/after photos.

**Spec:**
```
Type:       Web application (grooming records)
Auth:       Staff email + password login
Data model: Dog(id, owner_name, phone, name, breed, temperament)
            GroomNote(id, dog_id -> Dog, note, pinned)
            Groom(id, dog_id -> Dog, groomer_id -> User, date, style, before_url, after_url)
Features:   - Show pinned grooming notes when a dog is checked in
            - Record style and blade used for each groom
            - Upload before and after photos
            - Send the after photo to the owner by SMS
API:        REST
            GET  /dogs/{id}
            POST /dogs/{id}/notes
            POST /dogs/{id}/grooms
Storage:    PostgreSQL, S3
Tech stack: React, Node.js, Express, Twilio
```

---

## Example 230

**Intent:**
web app for vineyard to log spray applications per block for organic certification

**Spec:**
```
Type:       Web application (spray records)
Auth:       Email + password login
Data model: Block(id, name, variety, area_ha)
            Product(id, name, active_ingredient, organic_approved, pre_harvest_interval_days)
            SprayRecord(id, block_id -> Block, product_id -> Product, rate_per_ha, applied_on, operator, weather)
Features:   - Record each spray with product, rate and weather
            - Block products not approved for organic use
            - Show the earliest harvest date per block from pre-harvest intervals
            - Export records for the certification audit
API:        REST
            POST /blocks/{id}/sprays
            GET  /blocks/{id}/harvest-date
            GET  /export?year={y}
Storage:    PostgreSQL
Tech stack: Python, Flask, Bootstrap
```

---

## Example 231

**Intent:**
trust account ledger for a law firm

**Spec:**
```
Type:       Web application (client trust accounting)
Auth:       Email + password login with 2FA; roles: bookkeeper, partner
Data model: ClientMatter(id, client_name, matter_ref)
            TrustTransaction(id, matter_id -> ClientMatter, type, amount, reference, posted_on, posted_by -> User)
            BankReconciliation(id, month, bank_balance, ledger_balance, reconciled_by -> User)
Features:   - Record deposits and payments per client matter
            - Prevent payments that would overdraw a matter's balance
            - Show a running balance per matter
            - Run a monthly three-way reconciliation
            - Keep an unchangeable audit log of all entries
API:        REST
            POST /matters/{id}/transactions
            GET  /matters/{id}/ledger
            POST /reconciliations
Storage:    PostgreSQL (append-only ledger table)
Tech stack: Java, Spring Boot, React
```

---

## Example 232

**Intent:**
cake shop display what cakes are left today on a tv screen and the website

**Spec:**
```
Type:       Web application (live stock display)
Auth:       Staff PIN login
Data model: Cake(id, name, price, photo_url)
            TodayStock(id, cake_id -> Cake, date, quantity_left)
Features:   - Let staff update quantities left with +/- buttons on a tablet
            - Show a full-screen display for the shop TV
            - Show the same live list on the website
            - Grey out sold-out cakes
API:        REST + Server-Sent Events
            GET  /today
            PATCH /today/{id}
            GET  /today/stream
Storage:    SQLite
Tech stack: Go, HTMX, SSE
```

---

## Example 233

**Intent:**
plumbing supply company quotes for contractors with job pricing

**Spec:**
```
Type:       Web application (trade quotes)
Auth:       Email + password login for counter staff and contractors
Data model: Contractor(id, company, pricing_level)
            Product(id, sku, name, cost, list_price)
            TradeQuote(id, contractor_id -> Contractor, job_name, status, valid_until)
            TradeQuoteLine(id, quote_id -> TradeQuote, product_id -> Product, qty, price)
Features:   - Build a quote for a contractor's job from the catalogue
            - Apply the contractor's pricing level
            - Let the contractor accept the quote online
            - Convert an accepted quote into a sales order
API:        REST
            POST /quotes
            POST /quotes/{id}/accept
            POST /quotes/{id}/order
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, React
```

---

## Example 234

**Intent:**
i have 6 food vending machines in offices, i want see which need refill before driving there

**Spec:**
```
Type:       IoT system (vending machine stock monitoring)
Data model: Machine(id, location, telemetry_id)
            Slot(id, machine_id -> Machine, code, product, capacity, current_qty)
            Sale(id, slot_id -> Slot, price, sold_at)
Features:   - Receive sale events from each machine's telemetry unit
            - Track stock left in every slot
            - Show machines that need refilling, sorted by urgency
            - Generate a picking list for the refill trip
API:        REST
            POST /telemetry/sales
            GET  /machines/needs-refill
            GET  /picking-list
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 235

**Intent:**
online booking of fishing pegs at our lake, day tickets

**Spec:**
```
Type:       Web application (fishing peg booking)
Auth:       Admin login; anglers book with email
Data model: Peg(id, number, lake, swim_type)
            PegBooking(id, peg_id -> Peg, angler_name, email, date, ticket_type, price)
Features:   - Show a lake map with free and booked pegs
            - Book a peg for a day or 24 hours
            - Pay online
            - Close lakes for matches
API:        REST
            GET  /pegs?date={d}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 236

**Intent:**
I'm a freelance bookkeeper for builders and they always send me photos of receipts on WhatsApp. I want them to send the photo to an email or upload page and the system reads the total and supplier and puts it in a list for me.

**Spec:**
```
Type:       Web application (receipt capture with OCR)
Auth:       Email + password login for bookkeeper; clients upload via personal link
Data model: Client(id, name, upload_token, inbound_email)
            Receipt(id, client_id -> Client, image_url, supplier, date, total, vat, status)
Features:   - Accept receipt photos by upload link or email
            - Read supplier, date, total and VAT with OCR
            - Let the bookkeeper correct and approve extracted values
            - Export approved receipts per client to CSV for Xero
API:        REST
            POST /upload/{token}
            POST /inbound-email
            PATCH /receipts/{id}
            GET  /clients/{id}/export
Storage:    PostgreSQL, S3
Tech stack: Python, FastAPI, AWS Textract, React
```

---

## Example 237

**Intent:**
bowling alley lane reservations

**Spec:**
```
Type:       Web application (lane booking)
Auth:       Staff login; customers book as guests
Data model: Lane(id, number)
            LaneBooking(id, lane_id -> Lane, name, phone, starts_at, games, players, shoe_sizes)
Features:   - Book lanes by the hour or by number of games
            - Assign lanes automatically, keeping groups together
            - Collect shoe sizes in advance
            - Show the front desk a lane timeline
API:        REST
            GET  /availability?date={d}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 238

**Intent:**
web app where our carpenters order materials from the office for a job and the office sees whats pending

**Spec:**
```
Type:       Web application (internal material requests)
Auth:       Email + password login; roles: carpenter, office
Data model: Job(id, name, address)
            MaterialRequest(id, job_id -> Job, requested_by -> User, needed_by, status)
            RequestItem(id, request_id -> MaterialRequest, description, quantity, unit)
Features:   - Request materials for a job from a phone
            - Show the office all pending requests by needed-by date
            - Mark requests ordered and delivered
            - Notify the carpenter when materials arrive on site
API:        REST
            POST /requests
            GET  /requests?status=pending
            PATCH /requests/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 239

**Intent:**
Laundry pickup and delivery service, customer books pickup, we weigh the bag and charge by kg

**Spec:**
```
Type:       Web application (laundry pickup and delivery)
Auth:       Customer email + password login; driver and staff logins
Data model: LaundryOrder(id, customer_id -> User, pickup_slot, delivery_slot, address, weight_kg, price_per_kg, total, status)
            Driver(id, name)
            Run(id, driver_id -> Driver, date, type)
Features:   - Book a pickup and delivery slot
            - Save a card and charge after weighing
            - Record bag weight at the shop
            - Plan pickup and delivery runs for drivers
            - Notify the customer at each status change
API:        REST
            POST /orders
            PATCH /orders/{id}/weight
            GET  /runs?date={d}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe (saved payment methods)
```

---

## Example 240

**Intent:**
ISO 9001 internal audit planner

**Spec:**
```
Type:       Web application (internal audit management)
Auth:       Single sign-on with Google Workspace
Data model: Process(id, name, owner_id -> User)
            Audit(id, process_id -> Process, auditor_id -> User, planned_on, done_on, status)
            Finding(id, audit_id -> Audit, type, clause, description, action_due)
Features:   - Plan audits so every process is covered each year
            - Record findings by ISO clause
            - Assign actions for nonconformities
            - Show an annual audit calendar and completion status
API:        REST
            POST /audits
            POST /audits/{id}/findings
            GET  /audit-plan?year={y}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 241

**Intent:**
need an app for my bridal boutique so stylists see appointment and bride's preferences before she arrives

**Spec:**
```
Type:       Web application (appointment prep)
Auth:       Staff email + password login; brides fill a form via link
Data model: Appointment(id, bride_name, email, wedding_date, starts_at, stylist_id -> User)
            Preference(id, appointment_id -> Appointment, budget, silhouettes, fabrics, inspiration_urls, guests_coming)
Features:   - Send a style questionnaire after booking
            - Show the stylist a prep card with budget and preferences
            - Display inspiration images from the bride
            - Record dresses tried and favourites
API:        REST
            GET  /appointments?date={d}
            POST /appointments/{id}/preferences
            POST /appointments/{id}/tried
Storage:    PostgreSQL, S3
Tech stack: Vue.js, Node.js, Express
```

---

## Example 242

**Intent:**
small hotel minibar & room charges posted to the guest folio by housekeeping

**Spec:**
```
Type:       Web application (room charge posting)
Auth:       Staff PIN login
Data model: Room(id, number)
            Folio(id, room_id -> Room, guest_name, open, total)
            Charge(id, folio_id -> Folio, item, quantity, price, posted_by -> User, posted_at)
Features:   - Let housekeeping post minibar items to a room
            - Add the charge to the open folio
            - Show reception all charges at checkout
            - Undo a wrong charge with a reason
API:        REST
            POST /rooms/{id}/charges
            GET  /folios/{id}
            DELETE /charges/{id}
Storage:    PostgreSQL
Tech stack: PHP, Laravel
```

---

## Example 243

**Intent:**
guys i need a page where my moving crew see tomorrow jobs, how many men, truck and address

**Spec:**
```
Type:       Web application (crew job sheet)
Auth:       Email + password login; roles: dispatcher, crew
Data model: Move(id, customer, from_address, to_address, date, start_time, crew_size, truck_id -> Truck, notes)
            Truck(id, name, size_m3)
            CrewAssignment(id, move_id -> Move, worker_id -> User)
Features:   - Plan moves with crew size and truck
            - Assign workers to each move
            - Show each worker tomorrow's job with addresses and map links
            - Flag trucks booked twice on the same day
API:        REST
            GET  /moves?date={d}
            POST /moves/{id}/crew
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Bootstrap
```

---

## Example 244

**Intent:**
For my real estate photography business, agents order shoots for listings, I upload the photos and they download them after paying.

**Spec:**
```
Type:       Web application (listing photo orders)
Auth:       Email + password login for agents; photographer admin
Data model: ShootOrder(id, agent_id -> User, address, services, shoot_date, price, paid, status)
            Delivery(id, order_id -> ShootOrder, photo_url, type)
Features:   - Let agents order a shoot with photos, floor plan or drone
            - Schedule the shoot date
            - Upload finished images to the order
            - Unlock high-resolution downloads after payment
            - Download all images as a ZIP
API:        REST
            POST /orders
            POST /orders/{id}/deliveries
            GET  /orders/{id}/download
Storage:    PostgreSQL, S3
Tech stack: Next.js, Stripe, AWS S3
```

---

## Example 245

**Intent:**
small charity food bank: track donations in and food parcels out

**Spec:**
```
Type:       Web application (food bank stock)
Auth:       Volunteer email + password login
Data model: FoodItem(id, name, category, unit, stock)
            Donation(id, donor, received_on)
            DonationLine(id, donation_id -> Donation, item_id -> FoodItem, quantity, best_before)
            Parcel(id, referral_code, household_size, given_on)
Features:   - Record donations with best-before dates
            - Build parcels sized by household
            - Deduct parcel contents from stock
            - Show items close to their best-before date
API:        REST
            POST /donations
            POST /parcels
            GET  /items/expiring
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 246

**Intent:**
applicant tracking for our construction company hiring seasonal labourers every spring

**Spec:**
```
Type:       Web application (seasonal hiring pipeline)
Auth:       Email + password login for site managers and HR
Data model: Vacancy(id, trade, site, start_date, positions)
            Applicant(id, name, phone, trade, cscs_card_no, cscs_expires_on)
            Application(id, vacancy_id -> Vacancy, applicant_id -> Applicant, stage, notes)
Features:   - Post vacancies per trade and site
            - Collect applications with safety card details
            - Move applicants through stages (applied, called, inducted, started)
            - Rehire last season's workers with one click
API:        REST
            POST /vacancies
            POST /vacancies/{id}/applications
            PATCH /applications/{id}/stage
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 247

**Intent:**
coworking space door access, members unlock door with phone

**Spec:**
```
Type:       IoT system (smart door access)
Auth:       Member login in the web app; admin login
Data model: Member(id, name, email, plan, active)
            Door(id, name, controller_id)
            AccessRule(id, plan, door_id -> Door, from_time, to_time)
            AccessLog(id, member_id -> Member, door_id -> Door, opened_at, granted)
Features:   - Unlock a door from the phone web app
            - Allow access only during the member's plan hours
            - Revoke access instantly when a membership ends
            - Keep a log of every door opening
API:        REST
            POST /doors/{id}/unlock
            GET  /access-logs
Storage:    PostgreSQL
Tech stack: Raspberry Pi relay controllers, MQTT, Node.js, React
```

---

## Example 248

**Intent:**
estimate how long a print job takes on our machines and when it will be done

**Spec:**
```
Type:       Web application (job time estimation)
Auth:       Staff login
Data model: Machine(id, name, sheets_per_hour, setup_minutes)
            Job(id, machine_id -> Machine, sheets, finishing_minutes, queued_at, estimated_done_at)
Features:   - Estimate run time from sheet count and machine speed
            - Add setup and finishing time
            - Calculate completion time from the machine's queue
            - Recalculate when jobs are reordered
API:        REST
            POST /jobs/estimate
            GET  /machines/{id}/queue
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 249

**Intent:**
hi, im a farrier and i visit horses every 6-8 weeks. need to know which horses are due and where, and invoice owners

**Spec:**
```
Type:       Web application (farrier visit scheduling)
Auth:       Single user login
Data model: Owner(id, name, phone, email, yard_address)
            Horse(id, owner_id -> Owner, name, interval_weeks, shoeing_type)
            Visit(id, horse_id -> Horse, date, work_done, price, paid)
Features:   - Show horses due in the next two weeks grouped by yard
            - Record work done and price at each visit
            - Text owners to confirm the next visit
            - Email monthly invoices to owners
API:        REST
            GET  /horses/due
            POST /horses/{id}/visits
            POST /invoices/send?month={m}
Storage:    SQLite
Tech stack: Python, Django, Twilio
```

---

## Example 250

**Intent:**
SaaS for driving instructors to manage pupils, payments and diary, built with Vue and Firebase

**Spec:**
```
Type:       Web application (instructor management SaaS)
Auth:       Firebase Authentication (email + Google sign-in)
Data model: Instructor(id, name, hourly_rate, car)
            Pupil(id, instructor_id -> Instructor, name, phone, test_date, balance)
            Lesson(id, pupil_id -> Pupil, start_at, hours, paid)
            Progress(id, pupil_id -> Pupil, skill, level)
Features:   - Keep a weekly diary of lessons
            - Track prepaid balance and money owed per pupil
            - Record skill progress on a syllabus checklist
            - Send pupils lesson reminders by SMS
API:        Firebase SDK (Firestore collections)
            instructors/{id}/pupils
            instructors/{id}/lessons
Storage:    Firebase Firestore
Tech stack: Vue.js, Firebase, Cloud Functions
```

---

## Example 251

**Intent:**
I'd like a feedback kiosk at the exit of our car wash, with smiley faces, and a weekly report.

**Spec:**
```
Type:       Web application (feedback kiosk)
Auth:       Kiosk device token; owner login
Data model: Response(id, site, score, reason, created_at)
Features:   - Show four smiley buttons on a tablet
            - Ask a follow-up reason for bad scores
            - Reset the screen after 5 seconds
            - Email a weekly report with satisfaction by day and hour
API:        REST
            POST /responses
            GET  /reports/weekly
Storage:    SQLite
Tech stack: Svelte, Node.js, Express, Nodemailer
```

---

## Example 252

**Intent:**
manage chimney and stove installation jobs including building regs notification

**Spec:**
```
Type:       Web application (installation jobs and certification)
Auth:       Email + password login for installers and office
Data model: InstallJob(id, customer, address, appliance, flue_type, install_date, status)
            Checklist(id, job_id -> InstallJob, item, ok)
            Notification(id, job_id -> InstallJob, submitted_on, reference, certificate_url)
Features:   - Book installation jobs
            - Complete a commissioning checklist on site
            - Submit the building regulations notification after install
            - Store the compliance certificate and email it to the customer
API:        REST
            POST /jobs
            POST /jobs/{id}/checklist
            POST /jobs/{id}/notify
Storage:    PostgreSQL, S3
Tech stack: PHP, Laravel
```

---

## Example 253

**Intent:**
order tracking page for custom furniture

**Spec:**
```
Type:       Web application (order status page)
Auth:       Customer looks up with order number + email; staff login
Data model: FurnitureOrder(id, number, customer_email, item, stage, expected_delivery)
            StageUpdate(id, order_id -> FurnitureOrder, stage, photo_url, created_at)
Features:   - Show the order stage (design, build, finish, delivery)
            - Show workshop photos as the piece is made
            - Show the expected delivery week
            - Email the customer on each new stage
API:        REST
            GET  /track?number={n}&email={e}
            POST /orders/{id}/updates
Storage:    PostgreSQL
Tech stack: Node.js, Express, EJS
```

---

## Example 254

**Intent:**
sales commission calculator for our car dealership salespeople each month

**Spec:**
```
Type:       Web application (commission calculation)
Auth:       Email + password login; roles: salesperson, sales manager
Data model: Salesperson(id, name, email)
            Deal(id, salesperson_id -> Salesperson, vehicle, sale_date, gross_profit, finance_sold, warranty_sold)
            CommissionPlan(id, pct_of_gross, finance_bonus, warranty_bonus, monthly_target_bonus)
Features:   - Import monthly deals from the DMS
            - Calculate commission from gross profit and add-on bonuses
            - Add a bonus when the monthly unit target is hit
            - Let salespeople see their own deals and commission
            - Export the payroll file
API:        REST
            POST /deals/import
            GET  /commissions?month={m}
            GET  /me/commission
Storage:    PostgreSQL
Tech stack: Python, Django, pandas
```

---

## Example 255

**Intent:**
we are small brewery in Czech, need track excise tax for beer we produce and send out of warehouse

**Spec:**
```
Type:       Web application (excise duty records)
Auth:       Email + password login
Data model: Batch(id, beer, plato, volume_hl, produced_on)
            Movement(id, batch_id -> Batch, type, volume_hl, moved_on, document_no)
            DutyRate(id, plato_from, plato_to, rate_per_hl_plato)
Features:   - Record beer produced and leaving the bonded warehouse
            - Calculate excise duty from volume and degrees Plato
            - Keep the stock balance in the bonded warehouse
            - Produce the monthly excise return figures
API:        REST
            POST /batches
            POST /movements
            GET  /returns?month={m}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 256

**Intent:**
schedule for hospital porters

**Spec:**
```
Type:       Web application (porter task dispatch)
Auth:       Single sign-on with hospital Active Directory
Data model: Porter(id, name, status, current_location)
            PortingTask(id, from_location, to_location, type, priority, requested_by, assigned_to -> Porter, status, created_at)
Features:   - Let wards request porter tasks by type and priority
            - Assign tasks to the nearest free porter
            - Show tasks on porters' phones and let them accept
            - Report average response times by department
API:        REST + WebSocket
            POST /tasks
            POST /tasks/{id}/accept
            WS   /porters/live
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, SignalR, React
```

---

## Example 257

**Intent:**
web app for my cleaning products wholesale where reps take orders at customers on tablet even offline

**Spec:**
```
Type:       Web application (offline-capable sales rep ordering)
Auth:       Email + password login for sales reps
Data model: Customer(id, name, address, price_list)
            Product(id, sku, name, price)
            RepOrder(id, customer_id -> Customer, rep_id -> User, created_at, synced, total)
            RepOrderLine(id, order_id -> RepOrder, product_id -> Product, quantity)
Features:   - Cache customers and products on the tablet for offline use
            - Take orders without internet connection
            - Sync orders automatically when back online
            - Show each customer's last orders
API:        REST
            GET  /sync/catalogue
            POST /sync/orders
Storage:    PostgreSQL (server), IndexedDB (tablet)
Tech stack: React (PWA), Workbox, Dexie.js, Node.js
```

---

## Example 258

**Intent:**
online form for scrap metal yard to get daily metal prices and book drop off

**Spec:**
```
Type:       Web application (scrap prices and drop-off booking)
Auth:       Admin login
Data model: Metal(id, name, price_per_kg, updated_on)
            DropOff(id, name, phone, vehicle_reg, metals, estimated_kg, slot)
Features:   - Publish today's prices per metal grade
            - Estimate payout from weight entered
            - Book a drop-off slot for large loads
            - Record vehicle registration for legal compliance
API:        REST
            GET  /prices
            POST /drop-offs
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 259

**Intent:**
Every year our accounting firm sends 300 clients an organiser questionnaire for their tax return. I'd like it online, with answers saved per client and a list showing who hasn't finished yet.

**Spec:**
```
Type:       Web application (tax organiser questionnaires)
Auth:       Client login with email + password; staff login
Data model: Client(id, name, email, tax_year)
            Question(id, section, text, type, depends_on_id -> Question)
            Answer(id, client_id -> Client, question_id -> Question, value)
            Organiser(id, client_id -> Client, status, submitted_at)
Features:   - Show questions in sections with conditional follow-ups
            - Save answers automatically as the client types
            - Attach documents to answers
            - Show staff who has not started, in progress or submitted
            - Send reminders to clients who haven't finished
API:        REST
            GET  /organiser
            PUT  /organiser/answers
            POST /organiser/submit
            GET  /admin/organisers?status={s}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 260

**Intent:**
gym equipment repair company tracking warranty claims with manufacturers

**Spec:**
```
Type:       Web application (warranty claim tracking)
Auth:       Email + password login for technicians and admin
Data model: Manufacturer(id, name, claim_email)
            Equipment(id, client, model, serial, manufacturer_id -> Manufacturer, warranty_until)
            WarrantyClaim(id, equipment_id -> Equipment, fault, parts_requested, submitted_on, status, credit_amount)
Features:   - Check if a machine is still under warranty
            - Submit a claim email to the manufacturer with photos
            - Track claim status and credit received
            - Show claims waiting more than 30 days
API:        REST
            POST /claims
            PATCH /claims/{id}
            GET  /claims/pending
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 261

**Intent:**
will and estate document storage for our solicitors

**Spec:**
```
Type:       Web application (will storage register)
Auth:       Email + password login with 2FA for staff
Data model: Testator(id, full_name, birth_date, address)
            Will(id, testator_id -> Testator, signed_on, version, safe_location, scan_url, status)
            Withdrawal(id, will_id -> Will, withdrawn_by, reason, withdrawn_at)
Features:   - Register original wills held in the strongroom
            - Store a scanned copy of each will
            - Mark older wills as superseded when a new one is signed
            - Log every withdrawal of an original with reason
            - Search by testator name and date of birth
API:        REST
            POST /wills
            GET  /wills?name={n}
            POST /wills/{id}/withdraw
Storage:    PostgreSQL, S3 (encrypted)
Tech stack: Python, Django
```

---

## Example 262

**Intent:**
cleaning supplies reorder for our cleaners vans

**Spec:**
```
Type:       Web application (van stock reordering)
Auth:       Email + password login; roles: cleaner, supervisor
Data model: Van(id, name)
            Supply(id, name, unit, min_level)
            VanStock(id, van_id -> Van, supply_id -> Supply, quantity)
            Restock(id, van_id -> Van, requested_at, fulfilled_at)
Features:   - Let cleaners update supply levels on their van weekly
            - Flag supplies below the minimum level
            - Create a restock list per van
            - Show supervisors total supplies to order
API:        REST
            PUT  /vans/{id}/stock
            GET  /restock-list
Storage:    SQLite
Tech stack: Python, Flask, HTMX
```

---

## Example 263

**Intent:**
need site for my photo booth rental, customers pick a backdrop and props and book the date

**Spec:**
```
Type:       Web application (photo booth hire)
Auth:       Admin login; customers book as guests
Data model: Booth(id, name, type, price_per_hour)
            Backdrop(id, name, image_url, extra_price)
            BoothBooking(id, booth_id -> Booth, backdrop_id -> Backdrop, event_date, hours, venue, total, status)
Features:   - Show booths and backdrops with photos
            - Check booth availability on a date
            - Calculate price for hours and extras
            - Pay a deposit to confirm
            - Share an online gallery of the event's photos
API:        REST
            GET  /availability?date={d}
            POST /bookings
            GET  /events/{id}/gallery
Storage:    PostgreSQL, S3
Tech stack: Next.js, Stripe
```

---

## Example 264

**Intent:**
system for our franchise bakeries to order frozen dough from the central kitchen every day

**Spec:**
```
Type:       Web application (franchise replenishment ordering)
Auth:       Email + password login per franchise store; central kitchen admin
Data model: Store(id, name, region, delivery_days)
            DoughProduct(id, name, case_size, price)
            ReplenishOrder(id, store_id -> Store, delivery_date, status)
            ReplenishLine(id, order_id -> ReplenishOrder, product_id -> DoughProduct, cases)
Features:   - Suggest order quantities from each store's average sales
            - Let stores adjust and submit before the cut-off
            - Combine all orders into a production plan
            - Produce loading lists by delivery route
API:        REST
            GET  /stores/{id}/suggested-order
            POST /orders
            GET  /production-plan?date={d}
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Angular
```

---

## Example 265

**Intent:**
i fix computers for small businesses on contract and want to track hours used from their monthly support block

**Spec:**
```
Type:       Web application (support hour blocks)
Auth:       Email + password login; client contacts can log in
Data model: ClientCompany(id, name, monthly_hours)
            Block(id, client_id -> ClientCompany, month, hours_included, hours_used)
            WorkLog(id, client_id -> ClientCompany, date, minutes, description)
Features:   - Log work in 15-minute increments
            - Deduct work from the client's monthly block
            - Warn the client at 80% used
            - Bill overage hours at the end of the month
            - Show clients their remaining hours
API:        REST
            POST /worklogs
            GET  /clients/{id}/block
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 266

**Intent:**
online bookings for a dog hydrotherapy pool, vet referral form required

**Spec:**
```
Type:       Web application (hydrotherapy booking)
Auth:       Owner email login; therapist admin
Data model: Dog(id, owner_id -> User, name, breed, condition)
            Referral(id, dog_id -> Dog, vet_practice, file_url, approved, expires_on)
            PoolSession(id, dog_id -> Dog, starts_at, duration_min, notes)
Features:   - Upload a signed vet referral before first booking
            - Block bookings until the referral is approved
            - Book 30-minute pool sessions
            - Record session notes and progress
API:        REST
            POST /dogs/{id}/referrals
            POST /sessions
            POST /sessions/{id}/notes
Storage:    PostgreSQL, S3
Tech stack: Python, Django
```

---

## Example 267

**Intent:**
we're a freight forwarder, want to give customers a tracking page for their container with milestones from the shipping line

**Spec:**
```
Type:       Web application (container tracking)
Auth:       Customer email + password login
Data model: Shipment(id, customer_id -> User, container_no, bl_number, carrier, origin, destination, eta)
            Milestone(id, shipment_id -> Shipment, event, location, occurred_at)
Features:   - Fetch container events from carrier tracking APIs every 6 hours
            - Show a timeline of milestones per shipment
            - Show the vessel position on a map
            - Email customers when the ETA changes
API:        REST
            GET  /shipments
            GET  /shipments/{id}/milestones
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Celery, React, Leaflet
```

---

## Example 268

**Intent:**
For our recycling business I need weighbridge tickets: the truck drives on full, then empty, and the system calculates net weight and price per material.

**Spec:**
```
Type:       Web application (weighbridge ticketing)
Auth:       Operator PIN login
Data model: Customer(id, name, account_no)
            Material(id, name, price_per_tonne)
            WeighTicket(id, customer_id -> Customer, vehicle_reg, material_id -> Material, gross_kg, tare_kg, net_kg, amount, created_at)
Features:   - Read gross weight from the weighbridge indicator
            - Record tare weight on the way out
            - Calculate net weight and amount by material
            - Print a ticket for the driver
            - Remember tare weights of regular vehicles
API:        REST
            POST /tickets
            PATCH /tickets/{id}/tare
            GET  /tickets/{id}/print
Storage:    PostgreSQL
Tech stack: C#, .NET, serial port reader, Blazor
```

---

## Example 269

**Intent:**
web app for sign up to a beekeeping course

**Spec:**
```
Type:       Web application (course signup)
Auth:       Admin login
Data model: Course(id, title, dates, places, price, includes_suit_hire)
            Signup(id, course_id -> Course, name, email, suit_size, paid)
Features:   - List upcoming courses with places left
            - Sign up and pay online
            - Collect suit size for those hiring a suit
            - Email joining instructions a week before
API:        REST
            GET  /courses
            POST /courses/{id}/signups
Storage:    SQLite
Tech stack: PHP, Slim, Stripe
```

---

## Example 270

**Intent:**
appraisal system for my staff at a law firm with self review then manager review

**Spec:**
```
Type:       Web application (performance appraisals)
Auth:       Single sign-on with Microsoft Entra ID
Data model: Cycle(id, name, opens_on, closes_on)
            Review(id, cycle_id -> Cycle, employee_id -> User, reviewer_id -> User, status)
            Competency(id, name, description)
            Rating(id, review_id -> Review, competency_id -> Competency, self_score, manager_score, comment)
Features:   - Open an appraisal cycle for all staff
            - Let employees complete a self-review first
            - Let the manager rate and comment after the self-review
            - Hold a sign-off by both parties
            - Show HR completion progress
API:        REST
            POST /cycles
            PUT  /reviews/{id}/self
            PUT  /reviews/{id}/manager
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, React
```

---

## Example 271

**Intent:**
bakery allergen labels printer

**Spec:**
```
Type:       Web application (allergen label printing)
Auth:       Staff login
Data model: Ingredient(id, name, allergens)
            Product(id, name, shelf_life_days)
            ProductIngredient(id, product_id -> Product, ingredient_id -> Ingredient, weight_g)
Features:   - Build each product's ingredient list in descending weight order
            - Highlight allergens in bold on the label
            - Add the use-by date from shelf life
            - Print labels on a thermal label printer
API:        REST
            GET  /products/{id}/label
            POST /products
Storage:    SQLite
Tech stack: Python, Flask, Zebra ZPL printing
```

---

## Example 272

**Intent:**
web booking for a mobile sauna trailer that we deliver to people's homes for a weekend

**Spec:**
```
Type:       Web application (trailer rental with delivery)
Auth:       Admin login; customers book as guests
Data model: Trailer(id, name, capacity)
            Rental(id, trailer_id -> Trailer, customer, address, start_date, end_date, delivery_fee, total, status)
Features:   - Show free weekends per trailer
            - Calculate delivery fee by distance
            - Book and pay a deposit
            - Send setup instructions before delivery
API:        REST
            GET  /availability
            POST /rentals
Storage:    PostgreSQL
Tech stack: Node.js, Express, Stripe
```

---

## Example 273

**Intent:**
I manage maintenance for 12 rental buildings. Tenants report problems, I send a contractor, and I want to track cost per building per year for the owners.

**Spec:**
```
Type:       Web application (property maintenance management)
Auth:       Email + password login; roles: tenant, manager, contractor, owner
Data model: Building(id, name, owner_id -> User)
            Unit(id, building_id -> Building, number, tenant_id -> User)
            WorkOrder(id, unit_id -> Unit, issue, photo_url, priority, contractor_id -> User, status, cost)
Features:   - Let tenants report a problem with photos
            - Assign a contractor and set a priority
            - Let contractors update status and enter the cost
            - Show owners maintenance costs per building per year
API:        REST
            POST /work-orders
            PATCH /work-orders/{id}
            GET  /buildings/{id}/costs?year={y}
Storage:    PostgreSQL, S3
Tech stack: Python, Django, React
```

---

## Example 274

**Intent:**
forklift and pallet truck service intervals by engine hours

**Spec:**
```
Type:       Web application (hour-based maintenance)
Auth:       Email + password login
Data model: Machine(id, fleet_no, type, current_hours)
            HourReading(id, machine_id -> Machine, hours, read_on)
            ServicePlan(id, machine_type, interval_hours, tasks)
            ServiceDone(id, machine_id -> Machine, at_hours, done_on, notes)
Features:   - Log hour meter readings weekly
            - Calculate hours until next service
            - List machines due for service in the next 50 hours
            - Show the service task list for each interval
API:        REST
            POST /machines/{id}/hours
            GET  /machines/due
            POST /machines/{id}/services
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, Vue.js
```

---

## Example 275

**Intent:**
plz help, music lessons studio, parents pay per term, i want auto invoices each term with sibling discount

**Spec:**
```
Type:       Web application (term invoicing)
Auth:       Email + password login for parents and admin
Data model: Family(id, parent_name, email)
            Student(id, family_id -> Family, name, instrument, lesson_minutes)
            Term(id, name, start_date, weeks)
            TermInvoice(id, family_id -> Family, term_id -> Term, subtotal, discount, total, paid)
Features:   - Calculate each student's term fee from lesson length and weeks
            - Apply a sibling discount to the second and later children
            - Email invoices at the start of each term
            - Track payments and send reminders
API:        REST
            POST /terms/{id}/invoices
            GET  /families/{id}/invoices
            POST /invoices/{id}/paid
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 276

**Intent:**
online menu with ordering for a hotel room service

**Spec:**
```
Type:       Web application (room service ordering)
Auth:       Guests verify with room number and surname; kitchen staff login
Data model: MenuItem(id, name, category, price, available_from, available_to)
            RoomOrder(id, room_number, guest_surname, status, total, created_at)
            RoomOrderItem(id, order_id -> RoomOrder, item_id -> MenuItem, quantity, note)
Features:   - Show the menu by time of day
            - Order from the room by scanning a QR code
            - Charge the order to the room
            - Show orders on a kitchen screen with timers
API:        REST
            GET  /menu
            POST /orders
            PATCH /orders/{id}/status
Storage:    PostgreSQL
Tech stack: Vue.js, Node.js, Socket.IO
```

---

## Example 277

**Intent:**
small accounting firm's internal wiki of client quirks and procedures

**Spec:**
```
Type:       Web application (internal knowledge base)
Auth:       Single sign-on with Google Workspace
Data model: Page(id, title, body_markdown, client_id -> Client, updated_by -> User, updated_at)
            Client(id, name)
            Tag(id, name)
            PageTag(id, page_id -> Page, tag_id -> Tag)
Features:   - Write pages in Markdown, linked to a client or general
            - Search full text across all pages
            - Tag pages by topic
            - Keep revision history per page
API:        REST
            GET  /pages?q={q}
            POST /pages
            PUT  /pages/{id}
Storage:    PostgreSQL with full-text search
Tech stack: Python, Django, markdown-it
```

---

## Example 278

**Intent:**
order form for a stonemason's kitchen worktops with templating appointment

**Spec:**
```
Type:       Web application (worktop orders and templating)
Auth:       Staff login; customers order as guests
Data model: Stone(id, name, material, thickness_mm, price_per_m2)
            WorktopOrder(id, stone_id -> Stone, customer, address, approx_area_m2, cutouts, estimate, status)
            TemplateVisit(id, order_id -> WorktopOrder, date, measured_area_m2)
Features:   - Give an estimate from stone choice and approximate area
            - Book a templating visit
            - Update the price after exact measurement
            - Schedule fitting after fabrication
API:        REST
            POST /orders
            POST /orders/{id}/template-visit
            PATCH /orders/{id}/final-price
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 279

**Intent:**
inventory of spare parts in our factory maintenance store with min max levels

**Spec:**
```
Type:       Web application (MRO spare parts store)
Auth:       Email + password login for maintenance staff
Data model: SparePart(id, part_no, description, location_bin, min_qty, max_qty, on_hand)
            PartIssue(id, part_id -> SparePart, quantity, machine, issued_to, issued_at)
            Reorder(id, part_id -> SparePart, quantity, ordered_on, received_on)
Features:   - Issue parts to a machine repair
            - Suggest a reorder up to max when stock falls below min
            - Record receipts of reordered parts
            - Show parts used most per machine
API:        REST
            POST /parts/{id}/issue
            GET  /reorders/suggested
            POST /reorders/{id}/receive
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 280

**Intent:**
Hallo, we have a horse riding school. We want students book lessons online but each horse can only work 3 hours a day.

**Spec:**
```
Type:       Web application (riding lesson booking)
Auth:       Email + password login for riders; staff admin
Data model: Horse(id, name, max_hours_per_day, suitable_level)
            RidingLesson(id, starts_at, duration_min, level, instructor, capacity)
            LessonBooking(id, lesson_id -> RidingLesson, rider_id -> User, horse_id -> Horse)
Features:   - Book a group or private lesson by level
            - Assign a suitable horse to each rider
            - Stop assigning a horse after 3 working hours in a day
            - Show staff the horse plan for the day
API:        REST
            GET  /lessons?date={d}
            POST /lessons/{id}/bookings
            GET  /horses/plan?date={d}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 281

**Intent:**
contract renewal reminders for our company's software subscriptions and leases

**Spec:**
```
Type:       Web application (contract register)
Auth:       Single sign-on with Google Workspace
Data model: Vendor(id, name)
            Contract(id, vendor_id -> Vendor, title, owner_id -> User, annual_cost, start_date, end_date, notice_days, auto_renews, file_url)
Features:   - Store contracts with notice periods and auto-renew flag
            - Calculate the last day to cancel
            - Email the owner before the notice deadline
            - Show total annual spend by vendor
API:        REST
            GET  /contracts
            POST /contracts
            GET  /contracts/notice-due
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 282

**Intent:**
ice cream shop flavour board online

**Spec:**
```
Type:       Web application (today's flavours)
Auth:       Staff login
Data model: Flavour(id, name, dairy_free, allergens, photo_url)
            TodayFlavour(id, flavour_id -> Flavour, date, tub_level)
Features:   - Pick today's flavours from the flavour list
            - Show them on the website and a shop screen
            - Mark flavours running low or sold out
            - Filter by dairy-free and allergens
API:        REST
            GET  /today
            PUT  /today
Storage:    SQLite
Tech stack: Astro, Netlify Functions
```

---

## Example 283

**Intent:**
online job applications for a cleaning company with right to work check upload and reference requests

**Spec:**
```
Type:       Web application (applicant onboarding)
Auth:       Applicants use an email link; HR login
Data model: Applicant(id, name, email, phone, availability, status)
            RightToWorkDoc(id, applicant_id -> Applicant, file_url, checked_by -> User, checked_on)
            Reference(id, applicant_id -> Applicant, referee_email, response, received_at)
Features:   - Apply online with availability
            - Upload right to work documents
            - Email referees a short form automatically
            - Track applicants until ready to start
API:        REST
            POST /applicants
            POST /applicants/{id}/documents
            POST /references/{token}
Storage:    PostgreSQL, S3
Tech stack: Laravel, Livewire
```

---

## Example 284

**Intent:**
Webhook that creates a job in our field service tool whenever a customer books on our website calendly

**Spec:**
```
Type:       Webhook service (Calendly to field service sync)
Features:   - Receive Calendly invitee.created events
            - Verify the webhook signature
            - Create a customer and job in the field service tool
            - Cancel the job when the booking is cancelled
            - Log failures and retry
API:        REST
            POST /webhooks/calendly
Storage:    SQLite (event log)
Tech stack: Node.js, Express, Calendly API, Jobber API
```

---

## Example 285

**Intent:**
dent repair shop estimates with photo per dent and price by size

**Spec:**
```
Type:       Web application (dent repair estimates)
Auth:       Technician login
Data model: Estimate(id, customer, vehicle, created_at, total)
            Dent(id, estimate_id -> Estimate, panel, size_class, aluminium, photo_url, price)
            PriceMatrix(id, size_class, base_price, aluminium_surcharge)
Features:   - Add dents per panel with a photo
            - Price each dent from size class and panel material
            - Total the estimate and send it to the customer
API:        REST
            POST /estimates
            POST /estimates/{id}/dents
            POST /estimates/{id}/send
Storage:    PostgreSQL, S3
Tech stack: React, Node.js, Express
```

---

## Example 286

**Intent:**
web system so our coworking members can buy day passes and print credits

**Spec:**
```
Type:       Web application (passes and credits)
Auth:       Email + password login
Data model: Product(id, name, type, price, credits)
            Wallet(id, user_id -> User, print_credits)
            DayPass(id, user_id -> User, date, code)
Features:   - Buy day passes for a chosen date
            - Buy print credit bundles
            - Deduct credits when the printer reports a job
            - Show purchase history
API:        REST
            POST /day-passes
            POST /credits/purchase
            POST /printer/jobs
Storage:    PostgreSQL
Tech stack: Node.js, Express, Stripe
```

---

## Example 287

**Intent:**
online sign up sheet for a farm's CSA work shares where members do 4 hours a week instead of paying full price

**Spec:**
```
Type:       Web application (work share scheduling)
Auth:       Member email login; farm admin
Data model: Member(id, name, email, share_type)
            WorkShift(id, date, start_time, hours, task, spots)
            ShiftSignup(id, shift_id -> WorkShift, member_id -> Member, attended)
Features:   - Post weekly farm work shifts with tasks
            - Let work-share members sign up
            - Track hours done against the 4-hour weekly target
            - Remind members who are behind on hours
API:        REST
            GET  /shifts?week={w}
            POST /shifts/{id}/signup
            GET  /members/{id}/hours
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 288

**Intent:**
data pipeline that pulls our clinics' vet appointment data into a warehouse for reporting

**Spec:**
```
Type:       Data pipeline (veterinary practice reporting)
Features:   - Extract appointments, invoices and clients from each clinic's practice software nightly
            - Standardise species and service codes across clinics
            - Load into the data warehouse
            - Build daily revenue and visit tables per clinic
            - Alert on failed loads
Input:      Practice management database exports (CSV via SFTP)
Storage:    Google BigQuery
Tech stack: Python, Apache Airflow, dbt
```

---

## Example 289

**Intent:**
web booking for my van that does mobile phone screen repairs at offices

**Spec:**
```
Type:       Web application (on-site repair booking)
Auth:       Admin login; customers book as guests
Data model: Model(id, brand, name, screen_price, battery_price)
            OnsiteBooking(id, model_id -> Model, repair_type, company, address, date, slot, name, phone, price)
Features:   - Pick phone model and repair type to see the price
            - Book a slot for the van to come to the office
            - Group bookings at the same address
            - Text the customer when the van is on the way
API:        REST
            GET  /prices?model={id}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Next.js, Prisma, Twilio
```

---

## Example 290

**Intent:**
I'm the office manager of a small construction company. We hire plant machines like diggers from hire companies and keep forgetting to off-hire them, so we pay for weeks we didn't use. Help!

**Spec:**
```
Type:       Web application (plant hire tracking)
Auth:       Email + password login for office and site managers
Data model: HireCompany(id, name, email, phone)
            Hire(id, company_id -> HireCompany, item, site, start_date, weekly_rate, expected_end, off_hired_on, off_hire_ref)
Features:   - Record every hired machine with site and weekly rate
            - Ask site managers weekly if each item is still needed
            - Email the hire company an off-hire request with one click
            - Show current hire costs per site
            - Flag hires past their expected end date
API:        REST
            POST /hires
            POST /hires/{id}/off-hire
            GET  /hires/overdue
Storage:    PostgreSQL
Tech stack: Python, Django, Celery
```

---

## Example 291

**Intent:**
statute of limitations calculator for personal injury cases

**Spec:**
```
Type:       Web application (limitation date tracking)
Auth:       Email + password login for fee earners
Data model: Jurisdiction(id, name)
            LimitationRule(id, jurisdiction_id -> Jurisdiction, claim_type, years, minor_tolls)
            InjuryCase(id, client, claim_type, jurisdiction_id -> Jurisdiction, incident_date, client_birth_date, limitation_date, issued_on)
Features:   - Calculate the limitation date from incident date and claim type
            - Pause the clock until majority for child claimants
            - Show cases within 6 months of limitation on a dashboard
            - Escalate unissued cases 30 days before the date
API:        REST
            POST /cases
            GET  /cases/approaching
            GET  /rules
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 292

**Intent:**
cleaning co customer can rate each clean and leave comment, bad ones go to manager

**Spec:**
```
Type:       Web application (post-service ratings)
Auth:       Customers rate via a link; manager login
Data model: CompletedClean(id, customer_email, cleaner_id -> User, date, rating_token)
            Rating(id, clean_id -> CompletedClean, stars, comment, created_at)
Features:   - Email a rating link after each clean
            - Collect a 1-5 star rating and comment
            - Alert the manager for 1 or 2 stars
            - Show average rating per cleaner per month
API:        REST
            POST /ratings/{token}
            GET  /reports/cleaners?month={m}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Postmark
```

---

## Example 293

**Intent:**
web app for a chocolatier to plan Easter production from pre-orders

**Spec:**
```
Type:       Web application (seasonal pre-order production)
Auth:       Customer accounts; staff login
Data model: Product(id, name, mould, chocolate_type, weight_g, price)
            PreOrder(id, customer_id -> User, collection_date, paid)
            PreOrderLine(id, order_id -> PreOrder, product_id -> Product, quantity)
Features:   - Take Easter pre-orders with a collection date
            - Close pre-orders when moulds are fully booked
            - Calculate chocolate needed by type in kg
            - Plan production days back from collection dates
API:        REST
            POST /preorders
            GET  /admin/production-plan
            GET  /admin/chocolate-needed
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 294

**Intent:**
driving school car fuel and mileage logs per instructor

**Spec:**
```
Type:       Web application (vehicle usage logs)
Auth:       Email + password login; roles: instructor, owner
Data model: Car(id, registration, instructor_id -> User)
            MileageLog(id, car_id -> Car, date, start_km, end_km, lessons)
            FuelPurchase(id, car_id -> Car, date, litres, cost, receipt_url)
Features:   - Log daily mileage and lessons given
            - Upload fuel receipts
            - Calculate fuel cost per lesson hour
            - Flag mileage gaps between days
API:        REST
            POST /cars/{id}/mileage
            POST /cars/{id}/fuel
            GET  /cars/{id}/report?month={m}
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 295

**Intent:**
I'd like to build, with Django, a returns portal for our online furniture shop where customers start a return and pick a collection date.

**Spec:**
```
Type:       Web application (returns portal)
Auth:       Customers verify with order number and postcode; staff login
Data model: Order(id, number, email, postcode, delivered_on)
            ReturnRequest(id, order_id -> Order, items, reason, photos, collection_date, status, refund_amount)
Features:   - Start a return for items within the 30-day window
            - Choose a reason and upload photos of damage
            - Pick a collection date
            - Let staff approve and issue the refund after inspection
API:        REST
            POST /returns
            GET  /returns/{id}
            POST /returns/{id}/refund
Storage:    PostgreSQL
Tech stack: Python, Django, Django REST Framework, Stripe Refunds
```

---

## Example 296

**Intent:**
lab equipment calibration tracker

**Spec:**
```
Type:       Web application (calibration management)
Auth:       Email + password login for lab staff
Data model: Instrument(id, asset_no, name, location, calibration_interval_days, status)
            Calibration(id, instrument_id -> Instrument, done_on, provider, certificate_url, passed, next_due_on)
Features:   - Register instruments with calibration intervals
            - Upload calibration certificates
            - Tag instruments out of use when calibration has expired
            - Email reminders 30 days before due
API:        REST
            POST /instruments/{id}/calibrations
            GET  /instruments/due
Storage:    PostgreSQL, S3
Tech stack: Node.js, Express, Vue.js
```

---

## Example 297

**Intent:**
we run guided food tours in our city, 3 different tours, people book a date and we need guide assignment and a min of 4 guests or we cancel

**Spec:**
```
Type:       Web application (tour booking with minimum numbers)
Auth:       Admin and guide logins; customers book as guests
Data model: Tour(id, name, duration_h, price, min_guests, max_guests)
            Departure(id, tour_id -> Tour, starts_at, guide_id -> User, status)
            TourBooking(id, departure_id -> Departure, name, email, guests, dietary, paid)
Features:   - Book a tour departure and pay online
            - Collect dietary requirements
            - Cancel and refund departures under 4 guests 48 hours before
            - Assign guides and show them their tours
API:        REST
            GET  /tours/{id}/departures
            POST /departures/{id}/bookings
            POST /departures/{id}/cancel
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe
```

---

## Example 298

**Intent:**
small factory wants track downtime of machines and reasons

**Spec:**
```
Type:       Web application (machine downtime tracking)
Auth:       Operator PIN login; manager login
Data model: Machine(id, name, line)
            DowntimeReason(id, code, description, planned)
            DowntimeEvent(id, machine_id -> Machine, reason_id -> DowntimeReason, started_at, ended_at, operator)
Features:   - Start and stop a downtime event from a tablet at the machine
            - Pick a reason from a list
            - Show a Pareto chart of downtime by reason
            - Calculate availability per machine per shift
API:        REST
            POST /downtime
            PATCH /downtime/{id}/end
            GET  /reports/pareto
Storage:    PostgreSQL
Tech stack: Python, Django, Chart.js
```

---

## Example 299

**Intent:**
online order for party food platters with 48h notice

**Spec:**
```
Type:       Web application (catering platter orders)
Auth:       Admin login
Data model: Platter(id, name, serves, price, dietary_tags)
            PlatterOrder(id, name, phone, collection_at, total, paid)
            PlatterOrderItem(id, order_id -> PlatterOrder, platter_id -> Platter, quantity)
Features:   - Show platters with servings and dietary tags
            - Allow collection times at least 48 hours ahead
            - Limit platters per day to kitchen capacity
            - Pay online
API:        REST
            GET  /platters
            POST /orders
Storage:    SQLite
Tech stack: Flask, Stripe
```

---

## Example 300

**Intent:**
web app for accountants to calculate client's VAT return from their bookkeeping spreadsheet

**Spec:**
```
Type:       Web application (VAT return preparation)
Auth:       Email + password login for accountants
Data model: Client(id, name, vat_number, scheme)
            VatReturn(id, client_id -> Client, period, box1, box4, box6, box7, status)
            UploadedLedger(id, return_id -> VatReturn, file_url)
Features:   - Upload a client's sales and purchases spreadsheet
            - Map columns to net, VAT and date
            - Calculate the return boxes for the period
            - Highlight transactions with unusual VAT rates
            - Mark returns as filed
API:        REST
            POST /returns
            POST /returns/{id}/ledger
            GET  /returns/{id}/calculation
Storage:    PostgreSQL, S3
Tech stack: Python, Django, pandas
```

---

## Example 301

**Intent:**
boutique hotel lost and found log

**Spec:**
```
Type:       Web application (lost and found)
Auth:       Staff PIN login
Data model: FoundItem(id, description, room_or_area, found_by, found_at, storage_location, status, photo_url)
            Claim(id, item_id -> FoundItem, guest_name, contact, shipped_tracking, claimed_at)
Features:   - Log found items with photo and where they are stored
            - Match guest enquiries by date and room
            - Record shipping to the guest
            - Dispose of items unclaimed after 90 days
API:        REST
            POST /items
            GET  /items?room={r}
            POST /items/{id}/claim
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 302

**Intent:**
sistema para mi panaderia — sorry english — bakery wants to know daily sales vs production per product, from our POS export

**Spec:**
```
Type:       Data analysis script (sales vs production)
Features:   - Read daily POS sales export and production log
            - Match products by name or code
            - Calculate sold, produced and leftover per product per day
            - Show sell-through percentage by weekday
            - Save a weekly Excel report with charts
Input:      POS sales CSV and production log spreadsheet
Tech stack: Python, pandas, XlsxWriter
```

---

## Example 303

**Intent:**
For my wedding planning business I'd like a seating chart tool where couples drag guests to tables and I can print it for the venue.

**Spec:**
```
Type:       Web application (seating planner)
Auth:       Planner login; couples via shared link
Data model: Wedding(id, couple_names, share_token)
            Guest(id, wedding_id -> Wedding, name, meal_choice, table_id -> SeatTable)
            SeatTable(id, wedding_id -> Wedding, name, shape, seats, x, y)
Features:   - Import the guest list from a spreadsheet
            - Draw tables on a floor plan
            - Drag guests onto tables with seat limits enforced
            - Show meal counts per table
            - Print the plan and an alphabetical guest list
API:        REST
            POST /weddings/{id}/guests/import
            PATCH /guests/{id}
            GET  /weddings/{id}/print
Storage:    PostgreSQL
Tech stack: React, dnd-kit, Node.js, Express
```

---

## Example 304

**Intent:**
online calculator for a skip hire company that suggests skip size from what you're throwing away

**Spec:**
```
Type:       Web application (skip size advisor and booking)
Auth:       Admin login
Data model: SkipSize(id, name, yards, price, max_weight_t)
            WasteType(id, name, density, allowed)
            SkipBooking(id, skip_size_id -> SkipSize, address, permit_needed, delivery_date, total)
Features:   - Ask what type and roughly how much waste the customer has
            - Suggest the best skip size
            - Warn about prohibited waste like asbestos
            - Add a council permit fee if placed on the road
            - Book delivery date and pay
API:        REST
            POST /advise
            POST /bookings
Storage:    PostgreSQL
Tech stack: Vue.js, Node.js, Express, Stripe
```

---

## Example 305

**Intent:**
asset tracking with bluetooth tags for our hospital beds and pumps

**Spec:**
```
Type:       IoT system (indoor asset location)
Data model: Asset(id, type, asset_no, tag_mac)
            Gateway(id, ward, floor, mac)
            Sighting(id, asset_id -> Asset, gateway_id -> Gateway, rssi, seen_at)
Features:   - Detect BLE tags with gateways on each ward
            - Estimate each asset's current ward from signal strength
            - Search for the nearest free pump
            - Alert when an asset leaves the building
API:        REST
            POST /gateways/sightings
            GET  /assets/{id}/location
            GET  /assets/search?type={t}
Storage:    PostgreSQL, Redis (latest positions)
Tech stack: ESP32 BLE gateways, MQTT, Go, React
```

---

## Example 306

**Intent:**
bakery cafe staff tip pooling by hours worked

**Spec:**
```
Type:       Web application (tip distribution)
Auth:       Manager login
Data model: Employee(id, name)
            Shift(id, employee_id -> Employee, date, hours)
            TipPool(id, week_start, total_tips)
            TipShare(id, pool_id -> TipPool, employee_id -> Employee, hours, amount)
Features:   - Enter weekly tip totals
            - Import hours worked from the shift list
            - Split tips by hours worked
            - Show each employee their share history
API:        REST
            POST /tip-pools
            GET  /tip-pools/{id}/shares
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 307

**Intent:**
our engineering consultancy needs to track project budgets vs hours spent by each engineer

**Spec:**
```
Type:       Web application (project budget tracking)
Auth:       Single sign-on with Microsoft Entra ID
Data model: Project(id, code, name, fee, budget_hours)
            Phase(id, project_id -> Project, name, budget_hours)
            Timesheet(id, user_id -> User, phase_id -> Phase, date, hours)
            User(id, name, grade, cost_rate)
Features:   - Book hours to project phases weekly
            - Compare hours and cost against budget per phase
            - Forecast final cost from burn rate
            - Alert project managers at 80% of budget
API:        REST
            POST /timesheets
            GET  /projects/{id}/budget
Storage:    SQL Server
Tech stack: C#, ASP.NET Core, Angular
```

---

## Example 308

**Intent:**
let customers book a delivery slot for their new sofa from our furniture store

**Spec:**
```
Type:       Web application (delivery slot selection)
Auth:       Customers use a link from their order email
Data model: DeliveryOrder(id, order_no, customer_email, postcode, items_volume_m3, slot_id -> DeliverySlot)
            DeliverySlot(id, date, window, region, capacity_m3, used_m3)
Features:   - Show delivery slots for the customer's region
            - Hide slots without enough van space for the items
            - Confirm the slot by email
            - Let customers change the slot until 2 days before
API:        REST
            GET  /orders/{token}/slots
            POST /orders/{token}/slot
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 309

**Intent:**
im a dog walker with 25 clients, want them to book walks for the week and pay monthly

**Spec:**
```
Type:       Web application (dog walking bookings)
Auth:       Client email + password login
Data model: Dog(id, owner_id -> User, name, notes, key_location)
            Walk(id, dog_id -> Dog, date, slot, type, price, done)
            MonthlyBill(id, owner_id -> User, month, total, paid)
Features:   - Book group or solo walks for the coming week
            - Limit group walks to 6 dogs per slot
            - Mark walks done with a photo
            - Bill clients at the end of the month
API:        REST
            POST /walks
            PATCH /walks/{id}/done
            GET  /bills?month={m}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 310

**Intent:**
web dashboard of our bakery ovens temperature via sensors

**Spec:**
```
Type:       IoT system (oven temperature monitoring)
Data model: Oven(id, name, target_c)
            TempReading(id, oven_id -> Oven, temp_c, recorded_at)
Features:   - Send oven temperatures from thermocouples every 30 seconds
            - Show live temperature against target
            - Alert staff when an oven drifts more than 15 °C
            - Keep a daily temperature log for food safety
API:        MQTT + REST
            GET  /ovens/{id}/readings
Storage:    InfluxDB
Tech stack: ESP32, MAX31855 thermocouple boards, MQTT, Grafana
```

---

## Example 311

**Intent:**
I own a small pet shop and we sell live fish. I want a page to log water tests for each tank and see when tanks were last cleaned, because inspectors ask for it.

**Spec:**
```
Type:       Web application (aquarium tank logs)
Auth:       Staff login
Data model: Tank(id, name, type, volume_l)
            WaterTest(id, tank_id -> Tank, ph, ammonia, nitrite, nitrate, temperature_c, tested_at, tested_by)
            Maintenance(id, tank_id -> Tank, task, done_at, done_by)
Features:   - Log water test results per tank
            - Highlight values outside safe ranges
            - Record water changes and cleaning
            - Export records for animal welfare inspections
API:        REST
            POST /tanks/{id}/tests
            POST /tanks/{id}/maintenance
            GET  /export?from={d}&to={d}
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 312

**Intent:**
B2B portal for our coffee roastery, cafes subscribe to beans every 2 weeks

**Spec:**
```
Type:       Web application (wholesale coffee subscriptions)
Auth:       Email + password login for cafe accounts
Data model: Cafe(id, name, address, price_tier)
            Coffee(id, name, origin, roast, price_per_kg)
            WholesaleSub(id, cafe_id -> Cafe, coffee_id -> Coffee, kg, every_days, next_ship_on, active)
Features:   - Subscribe to beans by kg and interval
            - Change quantities before the next roast day
            - Produce a roast plan from upcoming shipments
            - Invoice cafes on shipment
API:        REST
            POST /subscriptions
            PATCH /subscriptions/{id}
            GET  /admin/roast-plan?date={d}
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Cashier (Stripe)
```

---

## Example 313

**Intent:**
temp agency payroll export

**Spec:**
```
Type:       Command-line script (payroll export)
Features:   - Read approved timesheets for a week
            - Apply day, night and weekend pay rates
            - Calculate holiday pay accrual
            - Write a CSV in the payroll software's import format
Input:      Week ending date and database connection string
Tech stack: Python, SQLAlchemy, Click
```

---

## Example 314

**Intent:**
client portal where landscaping customers approve design plans and pay stage invoices

**Spec:**
```
Type:       Web application (landscaping client portal)
Auth:       Email + password login for clients; staff admin
Data model: Project(id, client_id -> User, address, status)
            DesignPlan(id, project_id -> Project, version, file_url, approved_at)
            StageInvoice(id, project_id -> Project, stage, amount, due_on, paid)
Features:   - Share design plan versions with the client
            - Let the client approve a plan or ask for changes
            - Issue stage invoices (deposit, groundwork, planting)
            - Pay invoices online by card
API:        REST
            POST /projects/{id}/plans
            POST /plans/{id}/approve
            POST /invoices/{id}/pay
Storage:    PostgreSQL, S3
Tech stack: Next.js, Stripe
```

---

## Example 315

**Intent:**
small marina wants to track who paid annual mooring fees and send invoices

**Spec:**
```
Type:       Web application (annual mooring billing)
Auth:       Email + password login for marina office; boat owners view own account
Data model: Mooring(id, code, type, length_m)
            MooringHolder(id, mooring_id -> Mooring, owner_name, email, boat_name)
            MooringInvoice(id, holder_id -> MooringHolder, year, amount, issued_on, paid_on)
Features:   - Calculate yearly fees by mooring length
            - Send all invoices at the start of the season
            - Record payments and send reminders
            - List unpaid holders for the harbour master
API:        REST
            POST /invoices/generate?year={y}
            POST /invoices/{id}/paid
            GET  /invoices/unpaid
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 316

**Intent:**
crew timesheets for a film production with overtime and meal penalties

**Spec:**
```
Type:       Web application (production crew timecards)
Auth:       Email + password login; roles: crew, department head, payroll
Data model: CrewMember(id, name, department, day_rate, ot_threshold_h)
            Timecard(id, crew_id -> CrewMember, date, call_time, wrap_time, meal_start, meal_end, status)
Features:   - Enter call, meal and wrap times each day
            - Calculate overtime after the threshold hours
            - Add a meal penalty when lunch starts more than 6 hours after call
            - Route timecards to department heads for approval
API:        REST
            POST /timecards
            POST /timecards/{id}/approve
            GET  /payroll?week={w}
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, React
```

---

## Example 317

**Intent:**
I run a guitar repair workshop. Simple: track instruments in, work needed, parts ordered, and when ready.

**Spec:**
```
Type:       Web application (instrument repair tracking)
Auth:       Single user login
Data model: Customer(id, name, phone)
            Instrument(id, customer_id -> Customer, make, model, serial)
            RepairJob(id, instrument_id -> Instrument, work, estimate, status, booked_in, ready_on)
            PartOrder(id, job_id -> RepairJob, part, supplier, ordered_on, arrived_on)
Features:   - Book instruments in with the work needed
            - Track parts ordered and arrival
            - Move jobs through a simple board
            - Text the customer when ready
API:        REST
            POST /jobs
            POST /jobs/{id}/parts
            PATCH /jobs/{id}/status
Storage:    SQLite
Tech stack: Django, Twilio
```

---

## Example 318

**Intent:**
web app for a tea wholesaler that generates spec sheets for each tea for B2B customers

**Spec:**
```
Type:       Web application (product specification sheets)
Auth:       Staff login; customers download without login
Data model: Tea(id, name, type, origin, ingredients, allergens, brewing_temp_c, brewing_time_s, shelf_life_months)
            LabResult(id, tea_id -> Tea, pesticide_ok, tested_on, file_url)
Features:   - Store specifications for each tea
            - Attach lab test results
            - Generate a branded spec sheet PDF
            - Let B2B customers download spec sheets from a catalogue page
API:        REST
            GET  /teas
            GET  /teas/{id}/spec.pdf
            POST /teas/{id}/lab-results
Storage:    PostgreSQL, S3
Tech stack: Python, FastAPI, WeasyPrint
```

---

## Example 319

**Intent:**
wedding dj song request page for guests before the wedding

**Spec:**
```
Type:       Web application (guest song requests)
Auth:       DJ login; guests use the wedding's link
Data model: Event(id, couple_names, date, slug)
            SongRequest(id, event_id -> Event, guest_name, title, artist, votes)
            DoNotPlay(id, event_id -> Event, title, artist)
Features:   - Let guests search songs and request them
            - Vote up other requests
            - Hide songs on the couple's do-not-play list
            - Export the request list ranked by votes
API:        REST
            GET  /events/{slug}/requests
            POST /events/{slug}/requests
            POST /requests/{id}/vote
Storage:    PostgreSQL
Tech stack: SvelteKit, Spotify Web API (search)
```

---

## Example 320

**Intent:**
tell me when our company vans need tax and insurance renewal and keep the documents

**Spec:**
```
Type:       Web application (vehicle document renewals)
Auth:       Email + password login
Data model: Vehicle(id, registration, make, model)
            VehicleDocument(id, vehicle_id -> Vehicle, type, expires_on, file_url, cost)
Features:   - Store tax, insurance and inspection documents per van
            - Email reminders 30 and 7 days before expiry
            - Show a list of everything expiring this month
            - Track yearly running costs per van
API:        REST
            POST /vehicles/{id}/documents
            GET  /documents/expiring
Storage:    PostgreSQL, S3
Tech stack: Node.js, Express, Vue.js
```

---

## Example 321

**Intent:**
lawfirm needs a way 2 send clients secure docs n get them signed

**Spec:**
```
Type:       Web application (secure document exchange)
Auth:       Clients log in with email + one-time code; staff login with 2FA
Data model: Client(id, name, email)
            SecureDocument(id, client_id -> Client, title, file_url, requires_signature, sent_at, viewed_at)
            Signature(id, document_id -> SecureDocument, signed_at, ip_address, image_url)
Features:   - Upload a document and share it securely with a client
            - Expire links after 14 days
            - Let the client sign in the browser
            - Record view and signature times with IP for evidence
            - Store the signed PDF back on the matter
API:        REST
            POST /documents
            GET  /documents/{id}
            POST /documents/{id}/sign
Storage:    PostgreSQL, S3 (encrypted)
Tech stack: Node.js, Express, React, pdf-lib
```

---

## Example 322

**Intent:**
dumpster rental availability by yard

**Spec:**
```
Type:       Web application (container rental availability)
Auth:       Dispatcher login
Data model: Yard(id, name, address)
            Container(id, yard_id -> Yard, size_yd, status, current_address)
            ContainerRental(id, container_id -> Container, customer, address, drop_on, pickup_on)
Features:   - Show free containers per yard and size
            - Schedule drop-offs and pickups
            - Track where each container currently is
            - Flag rentals past their pickup date
API:        REST
            GET  /yards/{id}/containers
            POST /rentals
            PATCH /rentals/{id}/pickup
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 323

**Intent:**
our flower farm sells buckets of mixed flowers to wedding diy people, they need to reserve for a specific date months ahead

**Spec:**
```
Type:       Web application (seasonal flower reservations)
Auth:       Customer email login; farm admin
Data model: Bucket(id, name, colour_palette, stems, price)
            WeekCapacity(id, week_start, max_buckets, reserved)
            FlowerReservation(id, customer_id -> User, collection_date, deposit_paid, status)
            ReservationLine(id, reservation_id -> FlowerReservation, bucket_id -> Bucket, quantity)
Features:   - Reserve buckets for a collection date up to a year ahead
            - Limit buckets per week by expected harvest
            - Take a deposit and charge the balance 2 weeks before
            - Show what is in season for each month
API:        REST
            GET  /capacity?week={w}
            POST /reservations
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 324

**Intent:**
we hire out marquees and need to plan which crew puts up which tent at which venue each weekend

**Spec:**
```
Type:       Web application (event crew planning)
Auth:       Email + password login; roles: planner, crew
Data model: Marquee(id, name, size, crew_needed, build_hours)
            EventJob(id, marquee_id -> Marquee, venue, build_date, takedown_date)
            CrewMember(id, name, phone)
            JobCrew(id, job_id -> EventJob, crew_id -> CrewMember, role)
Features:   - Plan builds and takedowns for each weekend
            - Assign crew based on how many each marquee needs
            - Prevent double-booking crew on the same day
            - Text crew their schedule on Thursday
API:        REST
            GET  /jobs?weekend={d}
            POST /jobs/{id}/crew
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js, Twilio
```

---

## Example 325

**Intent:**
tutoring company: kids do online homework quizzes set by tutor, tutor sees results

**Spec:**
```
Type:       Web application (homework quizzes)
Auth:       Email + password login; roles: tutor, student
Data model: Quiz(id, tutor_id -> User, title, subject, due_at)
            Question(id, quiz_id -> Quiz, text, type, options, answer)
            Attempt(id, quiz_id -> Quiz, student_id -> User, score, submitted_at)
            AttemptAnswer(id, attempt_id -> Attempt, question_id -> Question, response, correct)
Features:   - Let tutors create quizzes with multiple choice and short answers
            - Assign quizzes to their students with a due date
            - Mark multiple-choice answers automatically
            - Show tutors scores and the hardest questions
API:        REST
            POST /quizzes
            POST /quizzes/{id}/attempts
            GET  /quizzes/{id}/results
Storage:    PostgreSQL
Tech stack: Next.js, Prisma
```

---

## Example 326

**Intent:**
Our property inventory clerks do check-in reports for rentals: every room, condition, meter readings, photos. Right now it's Word documents with pasted photos. I want an app for that with a nice PDF at the end.

**Spec:**
```
Type:       Web application (property inventory reports)
Auth:       Email + password login for clerks; agencies view reports
Data model: Property(id, address, agency_id -> User)
            InventoryReport(id, property_id -> Property, type, clerk_id -> User, date, status)
            RoomEntry(id, report_id -> InventoryReport, room, item, condition, notes)
            ReportPhoto(id, entry_id -> RoomEntry, url)
            MeterReading(id, report_id -> InventoryReport, meter, value, photo_url)
Features:   - Walk through rooms and record items and condition on a tablet
            - Take photos linked to each item
            - Record meter readings with photos
            - Copy a check-in report to start the check-out comparison
            - Generate a PDF report for the agency
API:        REST
            POST /reports
            POST /reports/{id}/entries
            GET  /reports/{id}.pdf
Storage:    PostgreSQL, S3
Tech stack: React (PWA), Python, FastAPI, WeasyPrint
```

---

## Example 327

**Intent:**
wholesale bakery route driver proof of delivery

**Spec:**
```
Type:       Web application (proof of delivery)
Auth:       Driver login
Data model: Stop(id, route_date, customer, address, position)
            Delivery(id, stop_id -> Stop, delivered_at, signed_by, signature_url, photo_url, shortages)
Features:   - Show drivers their stops in order
            - Capture signature or a photo of goods left at the door
            - Record shortages and returns
            - Email the customer a delivery confirmation
API:        REST
            GET  /routes/today
            POST /stops/{id}/delivery
Storage:    PostgreSQL, S3
Tech stack: React (PWA), Node.js, Express
```

---

## Example 328

**Intent:**
need site to sell tickets to our farm's pumpkin patch weekends in october with time slots

**Spec:**
```
Type:       Web application (seasonal event ticketing)
Auth:       Admin login
Data model: TimeSlot(id, date, start_time, capacity)
            TicketType(id, name, price)
            TicketOrder(id, slot_id -> TimeSlot, email, total, qr_code, scanned)
            TicketOrderLine(id, order_id -> TicketOrder, type_id -> TicketType, quantity)
Features:   - Sell adult, child and family tickets per time slot
            - Include one pumpkin per child ticket
            - Email QR code tickets
            - Scan tickets at the gate on a phone
API:        REST
            GET  /slots
            POST /orders
            POST /tickets/{code}/scan
Storage:    PostgreSQL
Tech stack: Node.js, Express, Stripe, html5-qrcode
```

---

## Example 329

**Intent:**
hey can u build a portal where our wholesale customers download invoices and statements and see what they owe

**Spec:**
```
Type:       Web application (customer account portal)
Auth:       Email + password login per customer account
Data model: Account(id, number, name, credit_limit, balance)
            Invoice(id, account_id -> Account, number, date, amount, due_on, paid, pdf_url)
            Payment(id, account_id -> Account, amount, received_on)
Features:   - Show open invoices and current balance
            - Download invoice and statement PDFs
            - Pay overdue invoices by card
            - Sync invoices nightly from the accounting system
API:        REST
            GET  /me/invoices
            GET  /me/statement
            POST /invoices/{id}/pay
Storage:    PostgreSQL
Tech stack: Python, Django, Xero API, Stripe
```

---

## Example 330

**Intent:**
safety observation cards for workers on site

**Spec:**
```
Type:       Web application (safety observations)
Auth:       Anyone with the site QR code can submit; HSE team login
Data model: Site(id, name, qr_token)
            Observation(id, site_id -> Site, type, category, description, photo_url, anonymous, status, created_at)
            Action(id, observation_id -> Observation, owner, due_on, closed_on)
Features:   - Submit a safe or unsafe observation from a phone
            - Allow anonymous reports
            - Assign actions for unsafe conditions
            - Show trends by category and site
API:        REST
            POST /sites/{token}/observations
            POST /observations/{id}/actions
            GET  /reports/trends
Storage:    PostgreSQL, S3
Tech stack: Vue.js, Python, FastAPI
```

---

## Example 331

**Intent:**
Good morning. Our company make wooden windows by order. I want customer configure window size and wood type and see price, then we produce.

**Spec:**
```
Type:       Web application (window configurator)
Auth:       Customer accounts with email; admin login
Data model: WoodType(id, name, price_factor)
            GlazingType(id, name, price_per_m2)
            WindowConfig(id, customer_id -> User, width_mm, height_mm, wood_id -> WoodType, glazing_id -> GlazingType, opening_type, price)
Features:   - Enter width and height within allowed limits
            - Choose wood, glazing and opening type
            - Show a drawing preview and the price
            - Send the configuration as an order to production
API:        REST
            POST /configurations/price
            POST /orders
Storage:    PostgreSQL
Tech stack: Vue.js, SVG preview, PHP, Symfony
```

---

## Example 332

**Intent:**
customer loyalty points for a car wash with license plate

**Spec:**
```
Type:       Web application (plate-based loyalty)
Auth:       Staff login; customers check points with their plate
Data model: Vehicle(id, plate, phone, points)
            Wash(id, vehicle_id -> Vehicle, package, price, washed_at)
Features:   - Add points per wash by plate number
            - Give a free wash at 10 washes
            - Let customers check points online
            - Text customers their points after each wash
API:        REST
            POST /washes
            GET  /vehicles/{plate}/points
Storage:    SQLite
Tech stack: Node.js, Express, Twilio
```

---

## Example 333

**Intent:**
bookkeeping firm workflow board for month end closes per client

**Spec:**
```
Type:       Web application (month-end close workflow)
Auth:       Email + password login for staff
Data model: Client(id, name, assigned_to -> User)
            CloseTemplate(id, step, position)
            Close(id, client_id -> Client, month, status)
            CloseStep(id, close_id -> Close, step, done_by -> User, done_at)
Features:   - Create each client's monthly close from a checklist template
            - Tick off steps (bank rec, payables, payroll, review)
            - Show a board of all clients by close progress
            - Flag closes not finished by the 10th
API:        REST
            POST /closes/generate?month={m}
            PATCH /close-steps/{id}
            GET  /board?month={m}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stimulus
```

---

## Example 334

**Intent:**
taxi company: drivers enter their shift takings and fuel and we calculate commission

**Spec:**
```
Type:       Web application (driver shift settlement)
Auth:       Driver login; office admin
Data model: Driver(id, name, commission_pct)
            ShiftReport(id, driver_id -> Driver, date, cash_takings, card_takings, fuel_cost, km_driven)
            Settlement(id, shift_id -> ShiftReport, company_share, driver_share)
Features:   - Enter takings and fuel at the end of each shift
            - Calculate company and driver shares
            - Show the driver's weekly earnings
            - Flag shifts with unusually low takings per km
API:        REST
            POST /shifts
            GET  /drivers/{id}/weekly
Storage:    PostgreSQL
Tech stack: Python, Flask, Bootstrap
```

---

## Example 335

**Intent:**
discord bot for our board game cafe to take table reservations

**Spec:**
```
Type:       Bot (Discord table reservations)
Data model: CafeTable(id, name, seats)
            TableReservation(id, table_id -> CafeTable, discord_user_id, name, party_size, starts_at)
Features:   - Reserve a table with a slash command and party size
            - Pick the smallest free table that fits
            - List your reservations and cancel them
            - Post tonight's reservations in a staff channel at 4pm
API:        Discord Gateway + slash commands
Storage:    SQLite
Tech stack: Python, discord.py, APScheduler
```

---

## Example 336

**Intent:**
I run a mobile bike repair service and need customers to book with their postcode and bike problem, I group jobs by area each day.

**Spec:**
```
Type:       Web application (mobile repair booking by area)
Auth:       Mechanic login; customers book as guests
Data model: AreaDay(id, date, area, postcodes, max_jobs)
            BikeJob(id, area_day_id -> AreaDay, name, phone, address, postcode, problem, bike_type, status)
Features:   - Offer dates when the mechanic is in the customer's area
            - Describe the bike problem from a list
            - Cap jobs per day
            - Show the day's jobs ordered by route
API:        REST
            GET  /dates?postcode={p}
            POST /jobs
            GET  /jobs?date={d}
Storage:    PostgreSQL
Tech stack: Svelte, Node.js, Express
```

---

## Example 337

**Intent:**
corporate gift baskets bulk order with list of recipient addresses

**Spec:**
```
Type:       Web application (bulk gift ordering)
Auth:       Business customer email + password login
Data model: Basket(id, name, price)
            BulkOrder(id, customer_id -> User, basket_id -> Basket, card_message, ship_date, total)
            Recipient(id, order_id -> BulkOrder, name, company, address, status, tracking_no)
Features:   - Upload a spreadsheet of recipient addresses
            - Validate addresses and show errors to fix
            - Add a personal card message
            - Track shipment status per recipient
API:        REST
            POST /orders
            POST /orders/{id}/recipients/import
            GET  /orders/{id}/recipients
Storage:    PostgreSQL
Tech stack: Django, openpyxl, ShipEngine API
```

---

## Example 338

**Intent:**
climbing gym route setting log, which routes are up, grades and when to strip them

**Spec:**
```
Type:       Web application (route setting management)
Auth:       Setter login; public route list
Data model: Wall(id, name, section)
            ClimbRoute(id, wall_id -> Wall, grade, colour, setter, set_on, strip_on, status)
            RouteFeedback(id, route_id -> ClimbRoute, suggested_grade, stars)
Features:   - Log new routes with grade, colour and setter
            - Show the current routes per wall
            - Plan which walls to reset by age
            - Let climbers rate routes and suggest grades
API:        REST
            GET  /routes?status=up
            POST /routes
            POST /routes/{id}/feedback
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 339

**Intent:**
bakery wants a customer recipe archive for special requests like gluten free birthday cakes they did before

**Spec:**
```
Type:       Web application (custom order history)
Auth:       Staff login
Data model: Customer(id, name, phone)
            PastOrder(id, customer_id -> Customer, date, description, dietary, recipe_notes, photo_url)
Features:   - Save each special order with the recipe notes used
            - Search by customer, dietary need or keyword
            - Duplicate a past order into a new one
            - Show photos of finished cakes
API:        REST
            GET  /orders?q={q}
            POST /orders
            POST /orders/{id}/duplicate
Storage:    SQLite, local file storage
Tech stack: Python, Flask
```

---

## Example 340

**Intent:**
a webapp to track packaging waste reporting for our food company — weights of plastic, cardboard, glass we put on the market each year

**Spec:**
```
Type:       Web application (packaging compliance reporting)
Auth:       Email + password login
Data model: Packaging(id, name, material, weight_g)
            ProductPackaging(id, product_sku, packaging_id -> Packaging, units)
            Sales(id, product_sku, year, units_sold)
Features:   - Store packaging components per product
            - Import yearly units sold per product
            - Calculate total tonnes per material
            - Produce the annual compliance report
API:        REST
            POST /packaging
            POST /sales/import
            GET  /reports/{year}
Storage:    PostgreSQL
Tech stack: Python, Django, pandas
```

---

## Example 341

**Intent:**
booking site for a recording studio using Laravel

**Spec:**
```
Type:       Web application (studio booking)
Auth:       Email + password login for artists; admin
Data model: Room(id, name, hourly_rate, day_rate)
            StudioBooking(id, room_id -> Room, artist_id -> User, starts_at, ends_at, engineer_needed, total, paid)
Features:   - Book rooms by the hour or the day
            - Add an engineer for an extra fee
            - Pay a 50% deposit online
            - Prevent overlapping bookings
API:        REST
            GET  /rooms/{id}/availability
            POST /bookings
Storage:    MySQL
Tech stack: PHP, Laravel, Stripe
```

---

## Example 342

**Intent:**
pharmacy wants patients to order repeat prescriptions online and pick up

**Spec:**
```
Type:       Web application (repeat prescription requests)
Auth:       Patient email + password login with date of birth check
Data model: Patient(id, name, birth_date, gp_practice)
            Medication(id, patient_id -> Patient, name, dose, repeat_allowed)
            RepeatRequest(id, patient_id -> Patient, requested_at, status, ready_at)
            RepeatItem(id, request_id -> RepeatRequest, medication_id -> Medication)
Features:   - Choose repeat medications from the patient's list
            - Send the request to the GP practice for approval
            - Notify the patient when it's ready to collect
            - Remind patients when a repeat is due
API:        REST
            GET  /me/medications
            POST /requests
            PATCH /requests/{id}/status
Storage:    PostgreSQL (encrypted)
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 343

**Intent:**
roofer material order calc from roof area

**Spec:**
```
Type:       Web application (materials take-off)
Auth:       Single user login
Data model: RoofJob(id, name, area_m2, pitch_deg, ridge_m, eaves_m)
            TileProduct(id, name, tiles_per_m2, price)
            MaterialLine(id, job_id -> RoofJob, item, quantity, cost)
Features:   - Calculate tiles, battens and membrane from roof area
            - Add ridge tiles from ridge length
            - Add a waste percentage
            - Produce an order list for the merchant
API:        REST
            POST /jobs
            GET  /jobs/{id}/materials
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 344

**Intent:**
so i manage 4 coffee shops and want the managers to do opening and closing checklists on a tablet that i can check from home

**Spec:**
```
Type:       Web application (opening and closing checklists)
Auth:       Manager PIN login per shop; owner login
Data model: Shop(id, name)
            ChecklistTask(id, type, text, requires_photo)
            ChecklistRun(id, shop_id -> Shop, type, manager_name, started_at, completed_at)
            TaskResult(id, run_id -> ChecklistRun, task_id -> ChecklistTask, done, photo_url)
Features:   - Run opening and closing checklists on a tablet
            - Require photos for chosen tasks like till counts
            - Show the owner which shops completed each checklist
            - Alert if a checklist is not done 30 minutes after opening
API:        REST
            POST /shops/{id}/runs
            PATCH /runs/{id}/tasks/{task}
            GET  /owner/today
Storage:    PostgreSQL, S3
Tech stack: React, Node.js, Express
```

---

## Example 345

**Intent:**
web app for a funeral director to publish funeral notices and let people send flowers through partner florists

**Spec:**
```
Type:       Web application (funeral notices with flower orders)
Auth:       Staff login; public visitors
Data model: Notice(id, deceased_name, service_at, venue, text, published)
            Florist(id, name, area, commission_pct)
            FlowerOrder(id, notice_id -> Notice, florist_id -> Florist, arrangement, card_message, sender, price, paid)
Features:   - Publish funeral notices with service details
            - Let visitors order flowers delivered to the service
            - Send orders to the local partner florist
            - Give the family a list of all flower senders and messages
API:        REST
            GET  /notices
            POST /notices/{id}/flowers
            GET  /notices/{id}/flower-cards
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe Connect
```

---

## Example 346

**Intent:**
Chrome extension for our sales reps to save LinkedIn profiles as leads into our Pipedrive

**Spec:**
```
Type:       Browser extension (save prospects to Pipedrive)
Features:   - Add a "Save to Pipedrive" button on profile pages
            - Read the name, job title and company from the page
            - Create a person and organisation in Pipedrive
            - Warn when the person already exists
            - Let the rep add a note and deal stage
API:        Pipedrive REST API
            POST /persons
            POST /organizations
            GET  /persons/search
Storage:    chrome.storage (API token)
Tech stack: JavaScript, Chrome Extensions Manifest V3
```

---

## Example 347

**Intent:**
asphalt paving company daily production report from crew

**Spec:**
```
Type:       Web application (daily production reports)
Auth:       Email + password login; roles: foreman, project manager
Data model: Project(id, name, client, total_tonnes)
            DailyReport(id, project_id -> Project, foreman_id -> User, date, tonnes_laid, area_m2, crew_hours, weather, delays)
            TruckTicket(id, report_id -> DailyReport, ticket_no, tonnes)
Features:   - Submit the day's tonnes laid and area paved
            - Enter asphalt truck ticket numbers and weights
            - Record crew hours and delays
            - Show project progress against total tonnes
API:        REST
            POST /projects/{id}/reports
            POST /reports/{id}/tickets
            GET  /projects/{id}/progress
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 348

**Intent:**
I run a costume rental shop for theatres and parties. I need to know which costume is out, who has it, when it comes back, and to book costumes for future dates without clashes.

**Spec:**
```
Type:       Web application (costume rental)
Auth:       Staff email + password login
Data model: Costume(id, code, name, period, size, condition, photo_url)
            Hirer(id, name, organisation, phone)
            CostumeHire(id, hirer_id -> Hirer, collect_on, return_on, status)
            HireItem(id, hire_id -> CostumeHire, costume_id -> Costume)
Features:   - Search costumes by period, size and type
            - Reserve costumes for future dates without overlap
            - Check costumes out and in
            - Add a cleaning buffer of 2 days after return
            - Charge for damage on return
API:        REST
            GET  /costumes/available?from={d}&to={d}
            POST /hires
            POST /hires/{id}/return
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Active Storage
```

---

## Example 349

**Intent:**
order sheets for a butcher where restaurants order cuts by kg

**Spec:**
```
Type:       Web application (butcher trade orders)
Auth:       Email + password login for restaurant accounts
Data model: Cut(id, name, animal, price_per_kg)
            TradeOrder(id, account_id -> User, delivery_date, notes, status)
            TradeLine(id, order_id -> TradeOrder, cut_id -> Cut, kg_ordered, kg_delivered)
Features:   - Order cuts by kg for a delivery date
            - Show a cutting list for the butchers each morning
            - Enter actual weights delivered
            - Invoice on actual weight
API:        REST
            POST /orders
            GET  /admin/cutting-list?date={d}
            PATCH /lines/{id}/weight
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 350

**Intent:**
pls make fastapi backend for my print shop where the website sends orders and files

**Spec:**
```
Type:       REST API service (print order backend)
Auth:       API key for the website; admin JWT
Data model: PrintProduct(id, name, sizes, base_price)
            PrintOrder(id, product_id -> PrintProduct, size, quantity, customer_email, total, status)
            PrintFile(id, order_id -> PrintOrder, url, pages)
Features:   - Return products and calculate prices
            - Accept orders with uploaded files
            - Store files and count PDF pages
            - Update order status and email the customer
API:        REST
            GET  /products
            POST /quotes
            POST /orders
            POST /orders/{id}/files
            PATCH /orders/{id}/status
Storage:    PostgreSQL, S3
Tech stack: Python, FastAPI, SQLAlchemy, pypdf
```

---

## Example 351

**Intent:**
expert witness directory and booking for law firms

**Spec:**
```
Type:       Web application (expert witness marketplace)
Auth:       Email + password login; roles: expert, solicitor, admin
Data model: Expert(id, user_id -> User, name, specialism, cv_url, hourly_rate, verified)
            Instruction(id, expert_id -> Expert, solicitor_id -> User, case_summary, deadline, status)
            Message(id, instruction_id -> Instruction, author_id -> User, body, created_at)
Features:   - Search experts by specialism and rate
            - Verify expert credentials before listing
            - Send an instruction request with case summary and deadline
            - Message securely within an instruction
API:        REST
            GET  /experts?specialism={s}
            POST /instructions
            POST /instructions/{id}/messages
Storage:    PostgreSQL, S3
Tech stack: Python, Django, React
```

---

## Example 352

**Intent:**
window blinds measuring and order to factory

**Spec:**
```
Type:       Web application (blinds measure and order)
Auth:       Email + password login for fitters and office
Data model: Survey(id, customer, address, fitter_id -> User, date)
            BlindLine(id, survey_id -> Survey, room, type, width_mm, drop_mm, fabric, control_side, price)
            FactoryOrder(id, survey_id -> Survey, sent_at, ref)
Features:   - Record measurements per window during the home visit
            - Price each blind from type, fabric and size bands
            - Produce the customer quote
            - Send the order to the factory in their CSV format
API:        REST
            POST /surveys
            POST /surveys/{id}/lines
            POST /surveys/{id}/factory-order
Storage:    PostgreSQL
Tech stack: Vue.js, Node.js, Express
```

---

## Example 353

**Intent:**
online order and click & collect for a hardware store with 2 branches

**Spec:**
```
Type:       Web application (click and collect)
Auth:       Customer accounts optional; branch staff login
Data model: Branch(id, name, address)
            Product(id, sku, name, price)
            BranchStock(id, branch_id -> Branch, product_id -> Product, quantity)
            CollectOrder(id, branch_id -> Branch, email, status, ready_at)
            CollectLine(id, order_id -> CollectOrder, product_id -> Product, quantity)
Features:   - Show stock per branch on product pages
            - Order online and choose a branch to collect
            - Let staff pick the order and mark it ready
            - Email the customer when ready
API:        REST
            GET  /products/{id}/stock
            POST /orders
            PATCH /orders/{id}/ready
Storage:    PostgreSQL
Tech stack: Next.js, Prisma, Stripe
```

---

## Example 354

**Intent:**
i do bookkeeping for farmers and need a simple subsidy payment tracker per farm per year

**Spec:**
```
Type:       Web application (subsidy tracking)
Auth:       Email + password login
Data model: Farm(id, name, holding_number)
            Scheme(id, name, year)
            Claim(id, farm_id -> Farm, scheme_id -> Scheme, claimed_amount, submitted_on, status)
            ClaimPayment(id, claim_id -> Claim, amount, paid_on)
Features:   - Record subsidy claims per farm and scheme
            - Log payments as they arrive
            - Show outstanding amounts per farm
            - Export a yearly summary for accounts
API:        REST
            POST /claims
            POST /claims/{id}/payments
            GET  /farms/{id}/summary?year={y}
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 355

**Intent:**
web tool where our electricians fill EICR electrical inspection certificates on site

**Spec:**
```
Type:       Web application (electrical inspection certificates)
Auth:       Email + password login for electricians
Data model: Installation(id, address, client, supply_type)
            Inspection(id, installation_id -> Installation, electrician_id -> User, date, overall_result)
            Circuit(id, inspection_id -> Inspection, board, number, description, breaker, r1_r2, insulation_mohm, rcd_ms)
            Observation(id, inspection_id -> Inspection, code, description)
Features:   - Enter circuit test results per board
            - Add observations with C1, C2, C3 codes
            - Set the overall result automatically from the codes
            - Generate the certificate PDF and email it to the client
API:        REST
            POST /inspections
            POST /inspections/{id}/circuits
            GET  /inspections/{id}/certificate
Storage:    PostgreSQL
Tech stack: React (PWA), Python, FastAPI, WeasyPrint
```

---

## Example 356

**Intent:**
My brother and I started a mobile oil change business. We go to customer's office parking lots. We need customers to book, tell us car model, and we need to know what oil and filter to bring.

**Spec:**
```
Type:       Web application (mobile oil change booking)
Auth:       Admin login; customers book as guests
Data model: VehicleSpec(id, make, model, year_from, year_to, oil_type, oil_litres, filter_part)
            OilBooking(id, spec_id -> VehicleSpec, name, phone, location, date, slot, price)
Features:   - Pick make, model and year when booking
            - Look up oil type, quantity and filter for the car
            - Book a slot at the customer's location
            - Show a daily packing list of oil and filters to bring
API:        REST
            GET  /vehicles/lookup?make={m}&model={mo}&year={y}
            POST /bookings
            GET  /packing-list?date={d}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 357

**Intent:**
event venue AV equipment checklist per event

**Spec:**
```
Type:       Web application (event equipment planning)
Auth:       Staff login
Data model: Equipment(id, name, category, quantity)
            VenueEvent(id, name, room, date)
            EventEquipment(id, event_id -> VenueEvent, equipment_id -> Equipment, quantity, set_up)
Features:   - Add the AV equipment needed per event
            - Warn when total use on a day exceeds stock
            - Give technicians a setup checklist
            - Mark items returned after the event
API:        REST
            POST /events/{id}/equipment
            GET  /events/{id}/checklist
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 358

**Intent:**
a portal for sub-contractors to submit their monthly invoices against our construction project budgets with retention

**Spec:**
```
Type:       Web application (subcontractor payment applications)
Auth:       Email + password login for subcontractors and commercial team
Data model: Package(id, project, subcontractor_id -> User, contract_value, retention_pct)
            PaymentApplication(id, package_id -> Package, period, gross_to_date, status)
            Valuation(id, application_id -> PaymentApplication, certified_to_date, retention_held, net_due)
Features:   - Let subcontractors submit monthly payment applications
            - Let the quantity surveyor certify the value
            - Calculate retention and net amount due
            - Issue payment notices with dates
API:        REST
            POST /packages/{id}/applications
            POST /applications/{id}/valuation
            GET  /packages/{id}/ledger
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, React
```

---

## Example 359

**Intent:**
cleaning company key safe codes, cleaners need the code only on the day of the job

**Spec:**
```
Type:       Web application (time-limited access codes)
Auth:       Email + password login with 2FA
Data model: Property(id, client, address, key_safe_code_encrypted)
            Job(id, property_id -> Property, cleaner_id -> User, date)
            CodeView(id, job_id -> Job, viewed_at)
Features:   - Store key safe codes encrypted
            - Show a cleaner the code only on the day of their job
            - Log every time a code is viewed
            - Remind clients to change codes when a cleaner leaves
API:        REST
            GET  /jobs/{id}/access-code
            GET  /properties/{id}/code-log
Storage:    PostgreSQL (pgcrypto)
Tech stack: Python, Django
```

---

## Example 360

**Intent:**
rent-a-chicken business lol. people rent 2 hens and coop for summer, need bookings and delivery

**Spec:**
```
Type:       Web application (seasonal livestock rental)
Auth:       Customer email login; owner admin
Data model: Package(id, name, hens, coop_type, price)
            HenRental(id, package_id -> Package, customer_id -> User, address, start_date, end_date, delivered, status)
            Inventory(id, coops_total, hens_available)
Features:   - Book a rental package for the season
            - Limit bookings to available coops and hens
            - Schedule delivery and collection dates
            - Offer an option to adopt the hens at the end
API:        REST
            GET  /packages
            POST /rentals
            GET  /admin/deliveries
Storage:    SQLite
Tech stack: Python, Flask, Stripe
```

---

## Example 361

**Intent:**
I need a time clock for my bakery staff on a tablet by the door, with PIN, and export hours for payroll

**Spec:**
```
Type:       Web application (tablet time clock)
Auth:       Employee PIN on the tablet; manager login
Data model: Employee(id, name, pin_hash, hourly_rate)
            Punch(id, employee_id -> Employee, type, punched_at, photo_url)
Features:   - Clock in and out with a 4-digit PIN
            - Take a photo at each punch to stop buddy punching
            - Let managers fix missed punches
            - Export weekly hours to CSV for payroll
API:        REST
            POST /punches
            PATCH /punches/{id}
            GET  /export?week={w}
Storage:    PostgreSQL
Tech stack: Vue.js, Node.js, Express
```

---

## Example 362

**Intent:**
nightly backup check script for our dental practice server that emails if backup failed

**Spec:**
```
Type:       Scheduled script (backup verification)
Features:   - Check the latest backup file exists and is from last night
            - Compare its size with the previous backups
            - Test that the archive opens without errors
            - Email the practice manager if anything fails
Input:      Backup folder path and expected schedule
Tech stack: PowerShell, Windows Task Scheduler
```

---

## Example 363

**Intent:**
Hello, I import tiles from Spain and sell to builders. Need system for containers arriving: what is on each container, when it arrives, and pre-sell before arrival.

**Spec:**
```
Type:       Web application (incoming container stock)
Auth:       Email + password login for sales staff
Data model: Container(id, ref, supplier, eta, status)
            ContainerLine(id, container_id -> Container, product_sku, m2)
            PreSale(id, line_id -> ContainerLine, customer, m2, deposit)
Features:   - Record container contents and ETA
            - Show available-to-sell quantity per product including incoming
            - Pre-sell stock from incoming containers
            - Notify customers when their container arrives
API:        REST
            POST /containers
            GET  /availability?sku={s}
            POST /lines/{id}/presales
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 364

**Intent:**
web app for barbers queue walk ins

**Spec:**
```
Type:       Web application (walk-in queue)
Auth:       Staff login
Data model: Barber(id, name, active)
            QueueEntry(id, name, phone, barber_id -> Barber, joined_at, status)
Features:   - Join the queue online or at the shop tablet
            - Show live wait time per barber
            - Text customers when they are next
            - Show a queue screen in the shop
API:        REST + WebSocket
            POST /queue
            PATCH /queue/{id}
            WS   /queue/live
Storage:    Redis
Tech stack: Node.js, Socket.IO, React, Twilio
```

---

## Example 365

**Intent:**
craft distillery wants to track barrels ageing in the warehouse

**Spec:**
```
Type:       Web application (barrel inventory)
Auth:       Email + password login
Data model: Barrel(id, number, wood, previous_use, size_l, location)
            Fill(id, barrel_id -> Barrel, spirit, filled_on, litres, abv)
            Sample(id, fill_id -> Fill, taken_on, abv, tasting_notes)
Features:   - Record each barrel fill with spirit, volume and strength
            - Track barrel location in the warehouse
            - Log samples and tasting notes over time
            - Calculate age and estimated angel's share loss
API:        REST
            POST /barrels/{id}/fills
            POST /fills/{id}/samples
            GET  /barrels?ready_after_years={n}
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 366

**Intent:**
meeting minutes and action items for our board of directors

**Spec:**
```
Type:       Web application (board meeting management)
Auth:       Email + password login with 2FA for directors
Data model: Meeting(id, date, location, agenda)
            Minute(id, meeting_id -> Meeting, item, discussion, decision)
            ActionItem(id, meeting_id -> Meeting, owner_id -> User, task, due_on, done)
            BoardPack(id, meeting_id -> Meeting, file_url)
Features:   - Publish the agenda and board pack before the meeting
            - Record minutes per agenda item
            - Assign action items and track them to the next meeting
            - Approve previous minutes electronically
API:        REST
            POST /meetings
            POST /meetings/{id}/minutes
            PATCH /actions/{id}
Storage:    PostgreSQL, S3
Tech stack: Django, HTMX
```

---

## Example 367

**Intent:**
plz app for my tutoring biz so parents can buy lesson packs and see remaining lessons, using Stripe and Next.js

**Spec:**
```
Type:       Web application (lesson pack purchases)
Auth:       Email + password login for parents; tutor admin
Data model: Child(id, parent_id -> User, name)
            Pack(id, name, lessons, price)
            PackPurchase(id, child_id -> Child, pack_id -> Pack, lessons_left, bought_at)
            LessonTaken(id, child_id -> Child, date, tutor)
Features:   - Buy lesson packs by card
            - Deduct a lesson when the tutor logs it
            - Show parents lessons left and history
            - Email when 1 lesson remains
API:        REST
            POST /api/checkout
            POST /api/lessons
            GET  /api/children/{id}/balance
Storage:    PostgreSQL
Tech stack: Next.js, Stripe Checkout, Prisma
```

---

## Example 368

**Intent:**
online pre-orders for a halal butcher for Eid with collection time slots

**Spec:**
```
Type:       Web application (holiday pre-orders)
Auth:       Admin login
Data model: Product(id, name, unit, price, max_quantity)
            CollectionSlot(id, date, start_time, capacity)
            PreOrder(id, slot_id -> CollectionSlot, name, phone, deposit_paid)
            PreOrderItem(id, order_id -> PreOrder, product_id -> Product, quantity)
Features:   - Pre-order meat with a deposit
            - Choose a collection slot over the holiday days
            - Limit orders per slot to avoid queues
            - Print collection lists per slot
API:        REST
            GET  /slots
            POST /preorders
            GET  /admin/collections?slot={id}
Storage:    PostgreSQL
Tech stack: Laravel, Stripe
```

---

## Example 369

**Intent:**
construction company needs snag lists at handover with photos marked on floor plans

**Spec:**
```
Type:       Web application (snagging)
Auth:       Email + password login; roles: site manager, subcontractor, client
Data model: Plot(id, project, number, floor_plan_url)
            Snag(id, plot_id -> Plot, x, y, description, trade, photo_url, assigned_to -> User, status)
Features:   - Pin snags on the floor plan with a photo
            - Assign each snag to a trade subcontractor
            - Let subcontractors mark snags fixed with a photo
            - Produce a snag report per plot for handover
API:        REST
            POST /plots/{id}/snags
            PATCH /snags/{id}
            GET  /plots/{id}/report
Storage:    PostgreSQL, S3
Tech stack: React, Leaflet (image overlay), Node.js
```

---

## Example 370

**Intent:**
Every Friday I count the cash in our three laundromats' change machines and coin boxes. I want a little app to enter the counts and see if anything is missing compared to the machine counters.

**Spec:**
```
Type:       Web application (cash collection reconciliation)
Auth:       Single owner login
Data model: Store(id, name)
            CashBox(id, store_id -> Store, name)
            Collection(id, box_id -> CashBox, date, counter_reading, counted_amount, expected_amount, difference)
Features:   - Enter meter readings and counted cash per box
            - Calculate expected cash from counter readings
            - Highlight differences above a tolerance
            - Show weekly totals per store
API:        REST
            POST /collections
            GET  /reports/weekly
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 371

**Intent:**
web gallery for a stone yard showing actual slabs in stock with photos so customers pick their exact slab

**Spec:**
```
Type:       Web application (slab inventory gallery)
Auth:       Staff login; customers browse and hold slabs with email
Data model: Material(id, name, type, colour)
            Slab(id, material_id -> Material, lot, length_mm, width_mm, thickness_mm, photo_url, status)
            Hold(id, slab_id -> Slab, customer_email, expires_at)
Features:   - Upload a photo of every slab with its size
            - Filter by material, colour and size
            - Put a slab on hold for 7 days
            - Release holds automatically when they expire
API:        REST
            GET  /slabs
            POST /slabs/{id}/hold
Storage:    PostgreSQL, Cloudinary
Tech stack: Nuxt, Node.js
```

---

## Example 372

**Intent:**
security company incident reports from guards

**Spec:**
```
Type:       Web application (incident reporting)
Auth:       Email + password login; roles: guard, supervisor, client
Data model: Site(id, name, client_id -> User)
            Incident(id, site_id -> Site, guard_id -> User, type, occurred_at, description, police_ref, severity)
            IncidentMedia(id, incident_id -> Incident, url)
Features:   - File an incident report with photos and video
            - Notify the supervisor immediately for high severity
            - Let clients view reports for their sites
            - Export reports as PDF
API:        REST
            POST /incidents
            POST /incidents/{id}/media
            GET  /sites/{id}/incidents
Storage:    PostgreSQL, S3
Tech stack: Flutter (web + mobile), Firebase
```

---

## Example 373

**Intent:**
small tax firm: track which client documents we received for each tax return checklist, with Airtable as database

**Spec:**
```
Type:       Web application (document checklist on Airtable)
Auth:       Staff login with Google
Data model: Client(id, name, return_type, year)
            ChecklistItem(id, client_id -> Client, document, received, received_on)
Features:   - Generate the checklist from the return type
            - Tick off documents as they arrive
            - Show clients missing documents
            - Email clients their outstanding items
API:        Airtable REST API
            GET  /v0/{base}/Clients
            PATCH /v0/{base}/ChecklistItems/{id}
Storage:    Airtable
Tech stack: React, Airtable API, Netlify Functions
```

---

## Example 374

**Intent:**
kennel runs cleaning and feeding schedule for staff

**Spec:**
```
Type:       Web application (daily care schedule)
Auth:       Staff PIN login
Data model: Run(id, number)
            Animal(id, run_id -> Run, name, feeding, medication)
            CareTask(id, animal_id -> Animal, type, due_at, done_by, done_at)
Features:   - Generate feeding, cleaning and medication tasks each day
            - Tick tasks off on a tablet
            - Highlight overdue medication
            - Keep a care log per animal
API:        REST
            GET  /tasks?date={d}
            PATCH /tasks/{id}/done
Storage:    SQLite
Tech stack: Node.js, Express, HTMX
```

---

## Example 375

**Intent:**
web app to manage our timber frame house projects from quote to delivery with stages and payments

**Spec:**
```
Type:       Web application (project lifecycle management)
Auth:       Email + password login for staff; client view
Data model: Project(id, client_id -> User, plot_address, house_model, contract_value, stage)
            StageDate(id, project_id -> Project, stage, planned_on, actual_on)
            PaymentMilestone(id, project_id -> Project, name, pct, invoiced_on, paid_on)
Features:   - Move projects through quote, design, planning, factory, delivery and erection
            - Plan and track stage dates
            - Invoice payment milestones as a percentage of the contract
            - Show the factory schedule for upcoming builds
API:        REST
            PATCH /projects/{id}/stage
            POST /projects/{id}/milestones/{mid}/invoice
            GET  /factory-schedule
Storage:    PostgreSQL
Tech stack: Python, Django, Vue.js
```

---

## Example 376

**Intent:**
vending company route planning for refilling snack machines

**Spec:**
```
Type:       Web application (refill route planning)
Auth:       Email + password login
Data model: Machine(id, location, lat, lng, fill_level_pct)
            RefillRoute(id, driver, date)
            RouteStop(id, route_id -> RefillRoute, machine_id -> Machine, position)
Features:   - Select machines under 40% full
            - Plan the shortest route from the depot
            - Show the route on a map for the driver
            - Mark machines refilled
API:        REST
            POST /routes/plan
            GET  /routes/{id}
            PATCH /stops/{id}/done
Storage:    PostgreSQL
Tech stack: Python, OR-Tools, Flask, Leaflet
```

---

## Example 377

**Intent:**
locksmith shop: let customers order copies of their registered security keys online using the key card number

**Spec:**
```
Type:       Web application (registered key copy orders)
Auth:       Customer email + password login with identity check
Data model: KeySystem(id, card_number, owner_id -> User, profile, authorised_users)
            CopyOrder(id, system_id -> KeySystem, quantity, requested_by -> User, status, collect_by)
Features:   - Register a restricted key system with its card number
            - Order copies only for registered owners
            - Require ID on collection
            - Keep an audit trail of every copy made
API:        REST
            POST /key-systems
            POST /key-systems/{id}/orders
            GET  /key-systems/{id}/audit
Storage:    PostgreSQL
Tech stack: Django
```

---

## Example 378

**Intent:**
whatsapp reminders for appointments at our hearing aid shop

**Spec:**
```
Type:       Scheduled script (WhatsApp appointment reminders)
Features:   - Read tomorrow's appointments from the booking calendar
            - Send a WhatsApp reminder with time and address
            - Let patients reply 1 to confirm or 2 to reschedule
            - Update the calendar with the reply
            - Remind patients to bring their hearing aids for servicing
Input:      Google Calendar of appointments
Tech stack: Python, Google Calendar API, Twilio WhatsApp API, cron
```

---

## Example 379

**Intent:**
point of sale for a farmers market stall that works offline

**Spec:**
```
Type:       Web application (offline point of sale)
Auth:       Stall owner login
Data model: Product(id, name, price, unit)
            Sale(id, total, method, created_at, synced)
            SaleItem(id, sale_id -> Sale, product_id -> Product, quantity)
Features:   - Ring up sales with large touch buttons
            - Work without internet and sync later
            - Take card payments with a card reader
            - Show takings by product at the end of the day
API:        REST
            POST /sync/sales
            GET  /products
Storage:    IndexedDB (device), PostgreSQL (server)
Tech stack: React (PWA), Dexie.js, Square Reader SDK, Node.js
```

---

## Example 380

**Intent:**
I'm an independent wedding officiant. Couples fill a long questionnaire about their story so I can write the ceremony. I want that online plus a way to share the draft script and get their edits.

**Spec:**
```
Type:       Web application (ceremony planning)
Auth:       Couples log in by magic link; officiant admin
Data model: Couple(id, names, email, wedding_date, venue)
            QuestionnaireAnswer(id, couple_id -> Couple, question, answer)
            Script(id, couple_id -> Couple, version, body, status)
            ScriptComment(id, script_id -> Script, author, text, anchor)
Features:   - Send a story questionnaire to each couple
            - Write the ceremony script in a rich text editor
            - Share drafts and collect inline comments
            - Lock the final version and print it
API:        REST
            POST /couples/{id}/answers
            POST /couples/{id}/scripts
            POST /scripts/{id}/comments
Storage:    PostgreSQL
Tech stack: Next.js, Tiptap editor, Prisma
```

---

## Example 381

**Intent:**
legal aid eligibility checker for our law centre

**Spec:**
```
Type:       Web application (eligibility screening)
Auth:       Caseworker login; public check without login
Data model: Threshold(id, household_size, max_gross_income, max_capital)
            Screening(id, household_size, income, capital, benefits, matter_type, eligible, created_at)
Features:   - Ask about household, income, savings and benefits step by step
            - Check the answers against current thresholds
            - Explain the result in plain language
            - Let eligible people request a callback
            - Let staff update thresholds each year
API:        REST
            POST /screenings
            POST /screenings/{id}/callback
            PUT  /admin/thresholds
Storage:    PostgreSQL
Tech stack: Svelte, Python, FastAPI
```

---

## Example 382

**Intent:**
sourdough subscription for local delivery every saturday

**Spec:**
```
Type:       Web application (bread subscriptions)
Auth:       Customer email + password login
Data model: Loaf(id, name, price)
            BreadSub(id, customer_id -> User, loaf_id -> Loaf, quantity, address, active, skip_next)
            DeliveryRun(id, date, stops_json)
Features:   - Subscribe to weekly Saturday loaves
            - Skip a week or pause
            - Charge weekly by card on Thursday
            - Produce the Saturday bake count and delivery list
API:        REST
            POST /subscriptions
            POST /subscriptions/{id}/skip
            GET  /admin/saturday
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe Billing
```

---

## Example 383

**Intent:**
generate CMR consignment notes for our trucking company from orders

**Spec:**
```
Type:       Web application (consignment note generation)
Auth:       Email + password login for dispatch staff
Data model: TransportOrder(id, sender, consignee, pickup_address, delivery_address, goods, packages, weight_kg, truck_plate)
            ConsignmentNote(id, order_id -> TransportOrder, number, issued_on, pdf_url)
Features:   - Create transport orders with sender, consignee and goods
            - Generate a numbered CMR note PDF with all required boxes
            - Print copies for sender, carrier and consignee
            - Upload the signed delivery copy as proof
API:        REST
            POST /orders
            POST /orders/{id}/cmr
            POST /notes/{id}/signed
Storage:    PostgreSQL, S3
Tech stack: Java, Spring Boot, JasperReports
```

---

## Example 384

**Intent:**
hey i do lash extensions from home and want ppl book + pay deposit + fill a patch test form first time

**Spec:**
```
Type:       Web application (beauty booking with patch test)
Auth:       Client email login; owner admin
Data model: Client(id, name, email, phone, patch_test_done_on)
            Treatment(id, name, minutes, price, deposit)
            LashBooking(id, client_id -> Client, treatment_id -> Treatment, starts_at, deposit_paid)
            ConsentForm(id, client_id -> Client, answers_json, signed_at)
Features:   - Require a patch test 48 hours before a first appointment
            - Fill a consent and health form online
            - Book and pay a deposit
            - Send infill reminders after 3 weeks
API:        REST
            POST /bookings
            POST /clients/{id}/consent
Storage:    PostgreSQL
Tech stack: Next.js, Stripe
```

---

## Example 385

**Intent:**
asbestos register for our school buildings with locations and condition checks

**Spec:**
```
Type:       Web application (asbestos management register)
Auth:       Email + password login for estates staff; read-only for contractors
Data model: Building(id, name, built_year)
            AsbestosItem(id, building_id -> Building, location, material, risk_score, photo_url)
            ConditionCheck(id, item_id -> AsbestosItem, checked_on, condition, action)
Features:   - Record known asbestos items with location and risk
            - Schedule yearly condition checks
            - Show contractors the register before they start work
            - Log contractor acknowledgement
API:        REST
            GET  /buildings/{id}/asbestos
            POST /items/{id}/checks
            POST /buildings/{id}/acknowledge
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 386

**Intent:**
my bakery uses shopify and i want a dashboard showing which items sell on which weekday

**Spec:**
```
Type:       Data dashboard (sales by weekday)
Features:   - Pull orders from the Shopify Admin API daily
            - Group units sold by product and weekday
            - Show a heatmap of products vs weekdays
            - Show trends over the last 12 weeks
Input:      Shopify orders via Admin API
Storage:    SQLite
Tech stack: Python, ShopifyAPI, pandas, Streamlit
```

---

## Example 387

**Intent:**
For our plant hire depot, customers ring to say a machine is ready to collect. I want a form where they "off-hire" online and get a reference number, and our drivers see collections to do.

**Spec:**
```
Type:       Web application (online off-hire)
Auth:       Customer account login; depot staff and drivers
Data model: HireContract(id, number, customer_id -> User, site_address)
            HireLine(id, contract_id -> HireContract, item, status)
            OffHire(id, line_id -> HireLine, reference, requested_at, collect_from, collected_at)
Features:   - Let customers off-hire items on their contract
            - Issue an off-hire reference number instantly
            - Stop charging from the off-hire date
            - Show drivers a list of collections by area
API:        REST
            GET  /contracts/{id}
            POST /lines/{id}/off-hire
            GET  /collections
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, React
```

---

## Example 388

**Intent:**
wedding venue supplier list app

**Spec:**
```
Type:       Web application (recommended supplier directory)
Auth:       Venue admin login
Data model: Supplier(id, name, category, website, phone, description, logo_url)
            Referral(id, supplier_id -> Supplier, couple_email, sent_at)
Features:   - List approved suppliers by category
            - Let couples send an enquiry to a supplier
            - Count referrals per supplier
            - Hide suppliers when their approval lapses
API:        REST
            GET  /suppliers?category={c}
            POST /suppliers/{id}/enquiries
Storage:    SQLite
Tech stack: Astro, Netlify Functions
```

---

## Example 389

**Intent:**
Hi I am working in a small transport company in Poland, we need app to check driver working hours from tachograph files and warn about breaks

**Spec:**
```
Type:       Web application (tachograph analysis)
Auth:       Email + password login for transport managers
Data model: Driver(id, name, card_number)
            TachoFile(id, driver_id -> Driver, file_url, downloaded_at)
            Activity(id, driver_id -> Driver, type, started_at, ended_at)
            Infringement(id, driver_id -> Driver, rule, occurred_on, details)
Features:   - Upload driver card files (.ddd)
            - Parse driving, rest and other work activities
            - Check daily and weekly driving limits and breaks
            - List infringements per driver
            - Remind managers to download cards every 28 days
API:        REST
            POST /tacho-files
            GET  /drivers/{id}/infringements
Storage:    PostgreSQL, S3
Tech stack: Python, Django, tachograph file parser library
```

---

## Example 390

**Intent:**
order desk for a print shop to quote banners by square metre

**Spec:**
```
Type:       Web application (banner pricing)
Auth:       Staff login
Data model: Material(id, name, price_per_m2)
            Finishing(id, name, price)
            BannerQuote(id, width_m, height_m, material_id -> Material, finishings, quantity, total)
Features:   - Enter width, height and material
            - Add hems, eyelets and pole pockets
            - Apply a minimum charge
            - Save and email the quote
API:        REST
            POST /quotes
            POST /quotes/{id}/email
Storage:    SQLite
Tech stack: Vue.js, Node.js
```

---

## Example 391

**Intent:**
online form for homeowners to book a septic tank emptying with tank size and access info

**Spec:**
```
Type:       Web application (septic service booking)
Auth:       Admin login
Data model: SepticBooking(id, name, phone, address, tank_size_l, access_notes, hose_distance_m, preferred_date, price, status)
            Tanker(id, name, capacity_l)
Features:   - Collect tank size and access details
            - Warn if the hose distance is too long
            - Price by tank size and distance
            - Plan tanker routes by capacity
API:        REST
            POST /bookings
            GET  /admin/routes?date={d}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 392

**Intent:**
a backend API for our dental lab where dentists' practice software can send digital cases

**Spec:**
```
Type:       REST API service (dental case intake)
Auth:       OAuth 2.0 per practice software integration
Data model: Practice(id, name, client_id)
            DigitalCase(id, practice_id -> Practice, external_id, patient_ref, prescription_json, due_date, status)
            ScanFile(id, case_id -> DigitalCase, url, format)
Features:   - Accept new cases with prescription details
            - Upload intraoral scan files (STL, PLY)
            - Return case status and expected ship date
            - Send status webhooks back to the practice
API:        REST
            POST /v1/cases
            POST /v1/cases/{id}/files
            GET  /v1/cases/{id}
Storage:    PostgreSQL, S3
Tech stack: Go, Echo, OpenAPI
```

---

## Example 393

**Intent:**
community garden plot allocation and waiting list

**Spec:**
```
Type:       Web application (allotment management)
Auth:       Email + password login for plot holders; committee admin
Data model: GardenPlot(id, number, size_m2, annual_fee, holder_id -> User)
            WaitingListEntry(id, user_id -> User, joined_on, preferred_size)
            Inspection(id, plot_id -> GardenPlot, date, cultivated_pct, note)
Features:   - Keep a waiting list in joining order
            - Offer vacant plots to the next person
            - Invoice annual fees
            - Record plot inspections and send warnings for neglected plots
API:        REST
            POST /waiting-list
            POST /plots/{id}/offer
            POST /plots/{id}/inspections
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 394

**Intent:**
online menu builder for caterers that shows calorie and allergen info per dish from ingredients

**Spec:**
```
Type:       Web application (nutrition and allergen calculation)
Auth:       Email + password login
Data model: Ingredient(id, name, kcal_per_100g, protein_g, fat_g, carbs_g, allergens)
            Dish(id, name, portions)
            DishIngredient(id, dish_id -> Dish, ingredient_id -> Ingredient, grams)
Features:   - Build dishes from ingredients and weights
            - Calculate calories and macros per portion
            - List the 14 major allergens automatically
            - Print menu cards with nutrition info
API:        REST
            POST /dishes
            GET  /dishes/{id}/nutrition
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 395

**Intent:**
we need simple system for our cleaning team to report broken things they see at client offices, then we tell the client

**Spec:**
```
Type:       Web application (issue reporting)
Auth:       Cleaner PIN login; client contact email
Data model: ClientSite(id, name, contact_email)
            IssueReport(id, site_id -> ClientSite, reported_by, description, photo_url, created_at, forwarded)
Features:   - Report an issue with a photo from the phone
            - Forward issues to the client contact by email
            - Group several issues into one daily email
            - Show issue history per site
API:        REST
            POST /issues
            GET  /sites/{id}/issues
Storage:    SQLite, S3
Tech stack: Node.js, Express, Nodemailer
```

---

## Example 396

**Intent:**
B2B portal for wine importer, restaurants see allocations of rare wines and request bottles

**Spec:**
```
Type:       Web application (wine allocation requests)
Auth:       Email + password login for trade accounts
Data model: Wine(id, producer, name, vintage, price)
            Allocation(id, wine_id -> Wine, total_bottles, closes_on)
            AllocationRequest(id, allocation_id -> Allocation, account_id -> User, bottles_requested, bottles_granted)
Features:   - Show open allocations with closing dates
            - Request bottles from an allocation
            - Let sales staff grant bottles to accounts
            - Notify accounts of their allocation result
API:        REST
            GET  /allocations
            POST /allocations/{id}/requests
            PATCH /requests/{id}/grant
Storage:    PostgreSQL
Tech stack: Django
```

---

## Example 397

**Intent:**
online exam practice for driving theory test with my school's logo

**Spec:**
```
Type:       Web application (theory test practice)
Auth:       Student login with code from the driving school
Data model: Question(id, category, text, image_url, options, correct_index, explanation)
            MockTest(id, student_id -> User, score, passed, taken_at)
Features:   - Run 50-question mock tests with a timer
            - Practise questions by category
            - Explain the right answer after each question
            - Show the instructor students' progress
API:        REST
            GET  /mock-test/new
            POST /mock-tests
            GET  /students/progress
Storage:    PostgreSQL
Tech stack: Vue.js, Node.js, Express
```

---

## Example 398

**Intent:**
greenhouse grower sells plug plants to garden centres, needs orders by week number

**Spec:**
```
Type:       Web application (week-based plant orders)
Auth:       Email + password login for garden centre buyers
Data model: Variety(id, name, tray_size, price_per_tray)
            WeekAvailability(id, variety_id -> Variety, iso_week, trays)
            PlugOrder(id, buyer_id -> User, iso_week, status)
            PlugOrderLine(id, order_id -> PlugOrder, variety_id -> Variety, trays)
Features:   - Show availability per variety by ISO week
            - Order trays for a future week
            - Reduce availability as orders come in
            - Produce sowing plans backwards from ready weeks
API:        REST
            GET  /availability?week={w}
            POST /orders
            GET  /admin/sowing-plan
Storage:    PostgreSQL
Tech stack: PHP, Laravel
```

---

## Example 399

**Intent:**
I own a chain of 5 dry cleaners and garments move between shops and the central plant. Things get lost. Barcode every garment and track it through each step.

**Spec:**
```
Type:       Web application (garment tracking)
Auth:       Staff PIN login per location
Data model: Location(id, name, type)
            Garment(id, barcode, ticket_no, description, customer_phone)
            GarmentScan(id, garment_id -> Garment, location_id -> Location, step, scanned_at)
Features:   - Print a barcode tag for each garment at drop-off
            - Scan garments at every step (bagged, plant in, cleaned, shop back)
            - Show where any garment is right now
            - List garments stuck in one step for more than 2 days
API:        REST
            POST /garments
            POST /garments/{barcode}/scan
            GET  /garments/stuck
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, Zebra label printer
```

---

## Example 400

**Intent:**
mortgage broker document checklist and case status for clients

**Spec:**
```
Type:       Web application (mortgage case portal)
Auth:       Client email + password login; broker login
Data model: Case(id, client_id -> User, type, lender, loan_amount, stage)
            RequiredDoc(id, case_id -> Case, name, file_url, approved)
            Note(id, case_id -> Case, body, visible_to_client)
Features:   - Show clients the documents they still need to upload
            - Upload payslips, bank statements and ID
            - Track the case from fact find to completion
            - Share updates visible to the client
API:        REST
            GET  /cases/{id}
            POST /cases/{id}/documents
            PATCH /cases/{id}/stage
Storage:    PostgreSQL, S3
Tech stack: Ruby on Rails, Active Storage
```

---

## Example 401

**Intent:**
web app for kitchen fitters to plan install days per job

**Spec:**
```
Type:       Web application (installation scheduling)
Auth:       Email + password login
Data model: KitchenJob(id, customer, address, units, worktop_type, status)
            InstallDay(id, job_id -> KitchenJob, fitter_id -> User, date, task)
Features:   - Estimate install days from number of units
            - Book fitters, electricians and plumbers on the right days
            - Show the weekly calendar per fitter
            - Notify customers of their install dates
API:        REST
            POST /jobs
            POST /jobs/{id}/days
            GET  /calendar?week={w}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, FullCalendar
```

---

## Example 402

**Intent:**
scuba dive shop: book boat dives and check certification level and last dive date

**Spec:**
```
Type:       Web application (dive trip booking)
Auth:       Diver email + password login; staff admin
Data model: Diver(id, name, cert_agency, cert_level, last_dive_on, cert_card_url)
            DiveTrip(id, site, date, departure_time, min_cert_level, spaces)
            DiveBooking(id, trip_id -> DiveTrip, diver_id -> Diver, rental_gear, paid)
Features:   - Book a boat dive and rent gear
            - Check the diver's certification level for the site
            - Require a refresher if the last dive was over a year ago
            - Print a boat manifest per trip
API:        REST
            GET  /trips
            POST /trips/{id}/bookings
            GET  /trips/{id}/manifest
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 403

**Intent:**
tool for HVAC techs to look up refrigerant charge and log refrigerant used for regulations

**Spec:**
```
Type:       Web application (refrigerant logs)
Auth:       Email + password login for technicians
Data model: Unit(id, site, model, refrigerant_type, charge_kg)
            RefrigerantLog(id, unit_id -> Unit, technician_id -> User, added_kg, recovered_kg, leak_found, date)
            Cylinder(id, number, refrigerant_type, remaining_kg)
Features:   - Look up a unit's refrigerant type and charge
            - Log refrigerant added or recovered from a cylinder
            - Schedule leak checks based on CO2-equivalent tonnes
            - Export the yearly refrigerant report
API:        REST
            GET  /units/{id}
            POST /units/{id}/refrigerant
            GET  /reports/yearly
Storage:    PostgreSQL
Tech stack: Vue.js, Python, FastAPI
```

---

## Example 404

**Intent:**
my mom has a sewing alterations shop, she wants a list of orders with due date and price, and text customers when ready, super simple pls

**Spec:**
```
Type:       Web application (alterations order list)
Auth:       Single user password login
Data model: Alteration(id, customer_name, phone, garment, work, price, due_on, status)
Features:   - Add an order with garment, work, price and due date
            - Show orders sorted by due date with big text
            - Mark done and send an SMS with one button
            - Mark collected and paid
API:        REST
            GET  /orders
            POST /orders
            PATCH /orders/{id}
Storage:    SQLite
Tech stack: Python, Flask, Twilio
```

---

## Example 405

**Intent:**
fleet tire tread depth inspections per truck axle

**Spec:**
```
Type:       Web application (tyre inspection records)
Auth:       Email + password login for fleet inspectors
Data model: Truck(id, fleet_no, axle_config)
            TyrePosition(id, truck_id -> Truck, axle, side, position)
            TreadReading(id, position_id -> TyrePosition, depth_mm, pressure_psi, inspected_on)
Features:   - Show a truck diagram with each tyre position
            - Record tread depth and pressure per tyre
            - Flag tyres below the legal minimum
            - Predict replacement dates from wear rate
API:        REST
            GET  /trucks/{id}/tyres
            POST /tyres/{id}/readings
            GET  /tyres/replace-soon
Storage:    PostgreSQL
Tech stack: React, Node.js, Express
```

---

## Example 406

**Intent:**
Our small accounting office wants to collect the client's annual questionnaire by WhatsApp chatbot instead of forms because older clients prefer chatting.

**Spec:**
```
Type:       Chatbot (WhatsApp client questionnaire)
Data model: Client(id, name, phone, tax_year)
            ChatAnswer(id, client_id -> Client, question_key, answer, received_at)
            ChatState(id, client_id -> Client, current_step)
Features:   - Start the yearly questionnaire by WhatsApp message
            - Ask one question at a time and save each answer
            - Accept photos of documents in the chat
            - Let clients stop and continue later
            - Show staff the completed answers per client
API:        REST
            POST /webhooks/whatsapp
            GET  /clients/{id}/answers
Storage:    PostgreSQL, S3
Tech stack: Python, FastAPI, WhatsApp Cloud API
```

---

## Example 407

**Intent:**
church wedding bookings w/ banns and rehearsal dates

**Spec:**
```
Type:       Web application (church wedding administration)
Auth:       Parish office login
Data model: Wedding(id, couple_names, email, date, time, status)
            Banns(id, wedding_id -> Wedding, read_on)
            Rehearsal(id, wedding_id -> Wedding, date)
            Fee(id, wedding_id -> Wedding, item, amount, paid)
Features:   - Book wedding dates and times
            - Schedule banns readings on three Sundays
            - Book a rehearsal date
            - Track fees for organist, bells and flowers
API:        REST
            POST /weddings
            POST /weddings/{id}/banns
            GET  /calendar
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 408

**Intent:**
online booking for a self service dog wash station with coin-free unlock

**Spec:**
```
Type:       IoT system (self-service dog wash)
Auth:       Customer email login
Data model: WashBay(id, name, controller_id)
            WashSession(id, bay_id -> WashBay, user_id -> User, starts_at, minutes, paid, started)
Features:   - Book and pay for a 15 or 30-minute wash slot
            - Unlock the bay with a code at the booked time
            - Switch water and dryer on through a relay controller
            - Turn the bay off when time is up
API:        REST
            POST /sessions
            POST /bays/{id}/start
Storage:    PostgreSQL
Tech stack: Raspberry Pi, relay board, Python, FastAPI, Stripe
```

---

## Example 409

**Intent:**
wholesale order form for my hot sauce brand with case pricing for stores

**Spec:**
```
Type:       Web application (wholesale order form)
Auth:       Retailer email + password login after approval
Data model: Sauce(id, name, heat_level, case_size, case_price, msrp)
            Retailer(id, store_name, address, approved)
            WholesaleOrder(id, retailer_id -> Retailer, total, status)
            WholesaleLine(id, order_id -> WholesaleOrder, sauce_id -> Sauce, cases)
Features:   - Apply to become a stockist
            - Order by the case with a minimum of 4 cases
            - Pay by invoice with 30-day terms
            - Download product photos and shelf talkers
API:        REST
            POST /retailers/apply
            POST /orders
            GET  /assets
Storage:    PostgreSQL
Tech stack: Next.js, Prisma
```

---

## Example 410

**Intent:**
labour hire company, need inductions done online before workers go to site, short video and quiz

**Spec:**
```
Type:       Web application (online site inductions)
Auth:       Workers log in with a mobile number + SMS code
Data model: Induction(id, client_site, video_url, pass_mark)
            InductionQuestion(id, induction_id -> Induction, text, options, correct)
            Completion(id, induction_id -> Induction, worker_id -> User, score, passed, completed_at, expires_at)
Features:   - Watch an induction video for the site
            - Take a quiz after the video
            - Issue a digital induction card when passed
            - Let site managers check a worker's induction by QR code
API:        REST
            GET  /inductions/{id}
            POST /inductions/{id}/attempts
            GET  /workers/{id}/card
Storage:    PostgreSQL
Tech stack: Vue.js, Node.js, Express, Twilio Verify
```

---

## Example 411

**Intent:**
probate case tracker listing assets and debts of the deceased

**Spec:**
```
Type:       Web application (estate administration)
Auth:       Email + password login for probate staff; executors view their estate
Data model: Estate(id, deceased_name, died_on, executor_id -> User, status)
            EstateAsset(id, estate_id -> Estate, type, institution, value_at_death, realised_value, closed)
            EstateDebt(id, estate_id -> Estate, creditor, amount, paid)
            Beneficiary(id, estate_id -> Estate, name, share_pct)
Features:   - List assets and debts with values at date of death
            - Track letters sent to banks and replies
            - Calculate the net estate and each beneficiary's share
            - Produce estate accounts for executors to approve
API:        REST
            POST /estates/{id}/assets
            POST /estates/{id}/debts
            GET  /estates/{id}/accounts
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 412

**Intent:**
coffee shop staff drink allowance tracker

**Spec:**
```
Type:       Web application (staff perk tracking)
Auth:       Staff PIN login; manager login
Data model: Staff(id, name, daily_allowance)
            StaffDrink(id, staff_id -> Staff, item, value, taken_at)
Features:   - Log a staff drink with a PIN
            - Count drinks against the daily allowance
            - Charge extra drinks at staff price
            - Show managers monthly totals
API:        REST
            POST /drinks
            GET  /reports/monthly
Storage:    SQLite
Tech stack: Node.js, Express, HTMX
```

---

## Example 413

**Intent:**
i want my garage customers to get an MOT reminder text a month before it's due, using our customer database export

**Spec:**
```
Type:       Scheduled script (MOT reminders)
Features:   - Load customers, vehicles and MOT due dates from the export
            - Find vehicles with MOT due in 30 days
            - Send each customer an SMS with a booking link
            - Skip customers already reminded this year
            - Log sent messages to a CSV
Input:      Garage system customer export (CSV)
Storage:    SQLite (sent log)
Tech stack: Python, pandas, Twilio, cron
```

---

## Example 414

**Intent:**
online consultation booking for a garden designer with a questionnaire and site photo upload

**Spec:**
```
Type:       Web application (design consultation booking)
Auth:       Designer admin login; clients book as guests
Data model: ConsultSlot(id, starts_at, is_booked)
            Consultation(id, slot_id -> ConsultSlot, name, email, address, garden_size_m2, budget, style, fee_paid)
            SitePhoto(id, consultation_id -> Consultation, url)
Features:   - Book a paid site consultation
            - Answer questions on budget, style and use
            - Upload photos of the current garden
            - Deduct the consultation fee from a design contract
API:        REST
            GET  /slots
            POST /consultations
            POST /consultations/{id}/photos
Storage:    PostgreSQL, S3
Tech stack: SvelteKit, Stripe
```

---

## Example 415

**Intent:**
document control for a construction company's RFIs between site and architects

**Spec:**
```
Type:       Web application (RFI management)
Auth:       Email + password login; roles: contractor, consultant
Data model: Project(id, name)
            RFI(id, project_id -> Project, number, subject, question, raised_by -> User, assigned_to -> User, due_on, status)
            RFIResponse(id, rfi_id -> RFI, answer, attachment_url, responded_at)
Features:   - Raise numbered RFIs with drawings attached
            - Assign each RFI to a consultant with a due date
            - Record responses and close the RFI
            - Show overdue RFIs and average response time
API:        REST
            POST /projects/{id}/rfis
            POST /rfis/{id}/responses
            GET  /projects/{id}/rfis?status=overdue
Storage:    PostgreSQL, S3
Tech stack: TypeScript, Express, React
```

---

## Example 416

**Intent:**
web app so customers of our boat repair yard can see work progress and approve extra jobs

**Spec:**
```
Type:       Web application (boat repair progress)
Auth:       Boat owner email login; yard staff login
Data model: Boat(id, owner_id -> User, name, model, berth)
            RepairJob(id, boat_id -> Boat, description, estimate, status)
            ExtraWork(id, job_id -> RepairJob, description, price, photo_url, approved)
Features:   - Show job progress with photos
            - Propose extra work found during repair
            - Let the owner approve or decline extras online
            - Show the running total of the bill
API:        REST
            GET  /boats/{id}/jobs
            POST /jobs/{id}/extras
            POST /extras/{id}/decision
Storage:    PostgreSQL, S3
Tech stack: Django, Bootstrap
```

---

## Example 417

**Intent:**
ice rink skate rental sizes and session tickets

**Spec:**
```
Type:       Web application (session tickets with rentals)
Auth:       Staff login; customers buy as guests
Data model: SkateSession(id, starts_at, capacity)
            SkateStock(id, size, quantity)
            RinkTicket(id, session_id -> SkateSession, skaters, skate_sizes, total)
Features:   - Sell tickets per session
            - Reserve rental skates by size
            - Stop sales when a session or skate size runs out
            - Show the rental desk which sizes to prepare
API:        REST
            GET  /sessions
            POST /sessions/{id}/tickets
Storage:    PostgreSQL
Tech stack: Node.js, Express, Stripe
```

---

## Example 418

**Intent:**
small law office: track physical files in archive boxes and who borrowed them

**Spec:**
```
Type:       Web application (file archive tracking)
Auth:       Staff email login
Data model: ArchiveBox(id, number, shelf, destroy_after)
            ClientFile(id, box_id -> ArchiveBox, client, matter_ref, closed_on)
            FileLoan(id, file_id -> ClientFile, borrowed_by, out_at, returned_at)
Features:   - Record which box each closed file is in
            - Sign files out and back in
            - Calculate destruction dates from retention periods
            - List boxes ready for secure destruction
API:        REST
            GET  /files?q={q}
            POST /files/{id}/loan
            GET  /boxes/destroy-due
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 419

**Intent:**
want app where my 3 bakery shops order cakes from our central kitchen and the kitchen sees totals per day

**Spec:**
```
Type:       Web application (internal transfer orders)
Auth:       Login per shop; kitchen login
Data model: Shop(id, name)
            CakeItem(id, name, unit)
            TransferOrder(id, shop_id -> Shop, delivery_date)
            TransferLine(id, order_id -> TransferOrder, item_id -> CakeItem, quantity)
Features:   - Let each shop order by 2pm for the next day
            - Total quantities per item for the kitchen
            - Print a packing list per shop
            - Compare ordered vs sold from shop reports
API:        REST
            POST /orders
            GET  /kitchen/totals?date={d}
Storage:    PostgreSQL
Tech stack: Django, HTMX
```

---

## Example 420

**Intent:**
For our solar panel installation company, I'd like a site survey form for the surveyor with roof orientation, shading and fuse board photos, which then calculates a rough system size and yield.

**Spec:**
```
Type:       Web application (solar site survey)
Auth:       Email + password login for surveyors
Data model: Survey(id, customer, address, lat, lng, annual_kwh_use, surveyor_id -> User)
            RoofFace(id, survey_id -> Survey, orientation_deg, pitch_deg, usable_area_m2, shading_pct)
            SurveyPhoto(id, survey_id -> Survey, type, url)
Features:   - Record roof faces with orientation, pitch and shading
            - Upload photos of the roof and fuse board
            - Estimate panel count from usable area
            - Estimate yearly yield using solar irradiation data
            - Produce a proposal with savings estimate
API:        REST
            POST /surveys
            POST /surveys/{id}/roof-faces
            GET  /surveys/{id}/estimate
Storage:    PostgreSQL, S3
Tech stack: React, Python, FastAPI, PVGIS API
```

---

## Example 421

**Intent:**
pallet tracking between our warehouse and customers, they owe us pallets

**Spec:**
```
Type:       Web application (pallet balance tracking)
Auth:       Email + password login
Data model: Customer(id, name)
            PalletMovement(id, customer_id -> Customer, type, quantity, delivery_note, moved_on)
Features:   - Record pallets sent with deliveries and pallets returned
            - Show the pallet balance per customer
            - Send monthly pallet statements
            - Charge for pallets not returned after 60 days
API:        REST
            POST /movements
            GET  /customers/{id}/balance
Storage:    PostgreSQL
Tech stack: Python, Flask
```

---

## Example 422

**Intent:**
vet practice: owners order pet food and flea treatment online for pickup at the clinic

**Spec:**
```
Type:       Web application (clinic shop ordering)
Auth:       Owner email login linked to their client record
Data model: ShopProduct(id, name, type, price, prescription_only)
            ShopOrder(id, owner_id -> User, pet_id -> Pet, status, ready_at)
            ShopOrderLine(id, order_id -> ShopOrder, product_id -> ShopProduct, quantity)
            Pet(id, owner_id -> User, name, weight_kg)
Features:   - Order food and parasite treatments for pickup
            - Require vet approval for prescription-only items
            - Suggest the right flea dose from the pet's weight
            - Notify the owner when the order is ready
API:        REST
            GET  /products
            POST /orders
            PATCH /orders/{id}/approve
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Vue.js
```

---

## Example 423

**Intent:**
office cleaning tender pricing spreadsheet replacement

**Spec:**
```
Type:       Web application (tender pricing)
Auth:       Email + password login for bid managers
Data model: Tender(id, client, due_on, status)
            Area(id, tender_id -> Tender, type, area_m2, frequency_per_week, minutes_per_100m2)
            CostSettings(id, hourly_wage, oncost_pct, margin_pct)
Features:   - Enter areas with floor type and cleaning frequency
            - Calculate labour hours from production rates
            - Add wages, on-costs, consumables and margin
            - Compare price scenarios side by side
API:        REST
            POST /tenders
            POST /tenders/{id}/areas
            GET  /tenders/{id}/pricing
Storage:    PostgreSQL
Tech stack: Vue.js, Python, FastAPI
```

---

## Example 424

**Intent:**
whats a good way to let customers track there dry stone wall repair quote and accept it

**Spec:**
```
Type:       Web application (quote acceptance page)
Auth:       Customers open a unique quote link; owner login
Data model: StoneQuote(id, customer, email, site, length_m, height_m, price, status, token, valid_until)
            QuotePhoto(id, quote_id -> StoneQuote, url)
Features:   - Send the quote as a link with site photos
            - Let the customer accept or decline online
            - Take a deposit when accepted
            - Remind customers before the quote expires
API:        REST
            GET  /quotes/{token}
            POST /quotes/{token}/accept
Storage:    SQLite
Tech stack: Python, Flask, Stripe
```

---

## Example 425

**Intent:**
manage the rental of our 6 holiday cottages including cleaners changeover schedule

**Spec:**
```
Type:       Web application (holiday cottage management)
Auth:       Owner admin; cleaner login; guests book as guests
Data model: Cottage(id, name, sleeps, nightly_rate)
            Stay(id, cottage_id -> Cottage, guest_name, email, arrive_on, depart_on, total)
            Changeover(id, cottage_id -> Cottage, date, cleaner_id -> User, done)
Features:   - Show availability and take bookings per cottage
            - Enforce Friday or Monday changeover days
            - Create changeover cleans on departure days
            - Show cleaners their changeovers for the week
API:        REST
            GET  /cottages/{id}/availability
            POST /stays
            GET  /changeovers?week={w}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 426

**Intent:**
electronic delivery notes for our builders merchant, driver gets signature on phone

**Spec:**
```
Type:       Web application (electronic delivery notes)
Auth:       Driver login
Data model: DeliveryNote(id, number, customer, site, items_json, status)
            PODRecord(id, note_id -> DeliveryNote, signed_name, signature_url, photo_url, lat, lng, signed_at)
Features:   - Load the day's delivery notes onto the driver's phone
            - Capture signature, name and photo of goods
            - Record GPS location of delivery
            - Email the signed note to the customer and office
API:        REST
            GET  /notes/today
            POST /notes/{id}/pod
Storage:    PostgreSQL, S3
Tech stack: React (PWA), Node.js, Express
```

---

## Example 427

**Intent:**
online menu with prices for my bakery cafe updated from Google Sheets

**Spec:**
```
Type:       Web application (menu from spreadsheet)
Features:   - Read menu items and prices from a Google Sheet
            - Cache the sheet for 5 minutes
            - Show the menu by category on the website
            - Hide items marked unavailable in the sheet
API:        REST
            GET  /menu
Storage:    In-memory cache
Tech stack: Node.js, Express, Google Sheets API
```

---

## Example 428

**Intent:**
web tool to plan staff for our wedding catering: number of waiters chefs bartenders by guest count

**Spec:**
```
Type:       Web application (event staffing calculator)
Auth:       Email + password login
Data model: StaffRatio(id, role, guests_per_staff, service_style)
            CateringEvent(id, name, date, guests, service_style)
            StaffBooking(id, event_id -> CateringEvent, role, worker_name, confirmed)
Features:   - Calculate required staff per role from guests and service style
            - Book freelancers into roles
            - Show unfilled roles per event
            - Estimate staff cost per event
API:        REST
            GET  /events/{id}/requirements
            POST /events/{id}/staff
Storage:    PostgreSQL
Tech stack: Django, Bootstrap
```

---

## Example 429

**Intent:**
Hi, I am owner of a car rental in Albania, small, 15 cars. Need website for booking with insurance options and deliver car to airport.

**Spec:**
```
Type:       Web application (car rental booking)
Auth:       Customer accounts with email; admin login
Data model: Car(id, model, category, transmission, daily_rate, status)
            InsuranceOption(id, name, daily_price, excess)
            CarRental(id, car_id -> Car, customer_id -> User, pickup_at, return_at, pickup_location, insurance_id -> InsuranceOption, total, deposit_paid)
Features:   - Search available cars by dates and category
            - Choose insurance level and extras
            - Choose airport or office pickup with a delivery fee
            - Pay a deposit online
            - Show the admin a calendar of cars
API:        REST
            GET  /cars/available?from={d}&to={d}
            POST /rentals
            GET  /admin/calendar
Storage:    PostgreSQL
Tech stack: Laravel, Vue.js, Stripe
```

---

## Example 430

**Intent:**
data dashboard of cleaning hours budget vs actual per client site

**Spec:**
```
Type:       Data dashboard (labour budget tracking)
Features:   - Load contracted hours per site
            - Load actual hours from the clock-in system
            - Show budget vs actual per site per week
            - Highlight sites over budget by more than 10%
            - Show trends by area manager
Input:      Contract hours spreadsheet and clock-in export (CSV)
Storage:    PostgreSQL
Tech stack: Python, pandas, Apache Superset
```

---

## Example 431

**Intent:**
shoe store wants to reserve shoes in size online and try in store

**Spec:**
```
Type:       Web application (reserve and try)
Auth:       Staff login; customers reserve as guests
Data model: Shoe(id, name, brand, price, photo_url)
            ShoeStock(id, shoe_id -> Shoe, size, quantity)
            TryReservation(id, stock_id -> ShoeStock, name, phone, expires_at, status)
Features:   - Show sizes in stock per shoe
            - Reserve a size to try in store for 48 hours
            - Hold the pair in the back room list
            - Release expired reservations
API:        REST
            GET  /shoes/{id}/sizes
            POST /reservations
Storage:    PostgreSQL
Tech stack: Next.js, Prisma
```

---

## Example 432

**Intent:**
work order system for a furniture restoration workshop with materials and time per job

**Spec:**
```
Type:       Web application (restoration work orders)
Auth:       Email + password login
Data model: Piece(id, customer, description, photos_before, photos_after)
            WorkOrder(id, piece_id -> Piece, tasks, estimate, status)
            TimeLog(id, order_id -> WorkOrder, worker, hours, date)
            MaterialUse(id, order_id -> WorkOrder, item, cost)
Features:   - Create work orders with before photos
            - Log hours and materials per job
            - Compare actual cost with the estimate
            - Share after photos with the customer
API:        REST
            POST /work-orders
            POST /work-orders/{id}/time
            POST /work-orders/{id}/materials
Storage:    PostgreSQL, S3
Tech stack: Ruby on Rails
```

---

## Example 433

**Intent:**
online class pass system for a ceramics studio with 10-class cards

**Spec:**
```
Type:       Web application (class pass cards)
Auth:       Student email + password login
Data model: ClassCard(id, student_id -> User, classes_total, classes_used, expires_on)
            StudioClass(id, title, starts_at, capacity)
            ClassBooking(id, class_id -> StudioClass, card_id -> ClassCard, attended)
Features:   - Buy a 10-class card that expires in 6 months
            - Book classes using card credits
            - Refund a credit when cancelling 24 hours ahead
            - Show remaining credits
API:        REST
            POST /cards
            POST /classes/{id}/book
            DELETE /bookings/{id}
Storage:    PostgreSQL
Tech stack: SvelteKit, Stripe
```

---

## Example 434

**Intent:**
generator rental for events with fuel refill scheduling

**Spec:**
```
Type:       Web application (generator hire)
Auth:       Staff login
Data model: Generator(id, kva, fuel_tank_l, burn_l_per_h)
            GenHire(id, generator_id -> Generator, event, site, start_at, end_at, hours_per_day)
            Refuel(id, hire_id -> GenHire, due_at, done_at, litres)
Features:   - Book generators for events by kVA
            - Calculate when each generator needs refuelling from burn rate
            - Schedule refuel visits for technicians
            - Bill fuel used per hire
API:        REST
            POST /hires
            GET  /refuels/due
            PATCH /refuels/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 435

**Intent:**
I'm a solo immigration consultant. Clients send me passport scans, bank statements etc. over email and I lose track. Need each client to have a checklist by visa type and a secure upload place.

**Spec:**
```
Type:       Web application (visa document collection)
Auth:       Client login with email + password; consultant admin with 2FA
Data model: VisaType(id, name, country)
            ChecklistTemplate(id, visa_type_id -> VisaType, document, required)
            ClientCase(id, client_id -> User, visa_type_id -> VisaType, deadline, status)
            CaseDocument(id, case_id -> ClientCase, template_id -> ChecklistTemplate, file_url, approved)
Features:   - Create a case with a checklist from the visa type
            - Upload documents securely against each checklist item
            - Approve or reject documents with a reason
            - Show progress and the submission deadline
API:        REST
            POST /cases
            POST /cases/{id}/documents
            PATCH /documents/{id}
Storage:    PostgreSQL, S3 (encrypted)
Tech stack: Python, Django
```

---

## Example 436

**Intent:**
bike shop service booking with bike drop off day

**Spec:**
```
Type:       Web application (service booking by day)
Auth:       Staff login; customers book as guests
Data model: ServiceType(id, name, price, workshop_minutes)
            DropOffDay(id, date, capacity_minutes, booked_minutes)
            ServiceBooking(id, day_id -> DropOffDay, service_id -> ServiceType, name, phone, bike, status)
Features:   - Choose a service and drop-off day
            - Fill days by workshop minutes, not time slots
            - Text the customer when the bike is ready
API:        REST
            GET  /days
            POST /bookings
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 437

**Intent:**
web app where landlords can request gas safety checks from our heating company every year

**Spec:**
```
Type:       Web application (annual safety check requests)
Auth:       Landlord email + password login; engineer login
Data model: RentalProperty(id, landlord_id -> User, address, tenant_phone, last_check_on)
            SafetyCheck(id, property_id -> RentalProperty, engineer_id -> User, date, passed, certificate_url)
Features:   - Register rental properties with tenant contact
            - Remind landlords 2 months before the certificate expires
            - Book a check and contact the tenant for access
            - Store certificates for landlords to download
API:        REST
            POST /properties
            POST /properties/{id}/checks
            GET  /properties/{id}/certificates
Storage:    PostgreSQL, S3
Tech stack: Node.js, NestJS, React
```

---

## Example 438

**Intent:**
coworking events calendar where members RSVP

**Spec:**
```
Type:       Web application (member events)
Auth:       Member email login
Data model: CommunityEvent(id, title, starts_at, room, capacity, description)
            RSVP(id, event_id -> CommunityEvent, member_id -> User, status)
Features:   - List upcoming community events
            - RSVP and add to calendar
            - Waitlist when full
            - Post events to the members' Slack channel
API:        REST
            GET  /events
            POST /events/{id}/rsvp
Storage:    SQLite
Tech stack: Django, Slack Incoming Webhooks
```

---

## Example 439

**Intent:**
online ordering system for a wholesale florist where florists see today's stems and prices with live stock

**Spec:**
```
Type:       Web application (wholesale flower ordering)
Auth:       Email + password login for trade florists
Data model: Stem(id, variety, colour, length_cm, stems_per_bunch, price_per_bunch, bunches_available)
            FloristOrder(id, florist_id -> User, delivery_or_collect, status)
            FloristLine(id, order_id -> FloristOrder, stem_id -> Stem, bunches)
Features:   - Show today's stems with photos, lengths and prices
            - Update stock live as florists order
            - Order for delivery on the van round or collection
            - Upload the morning's stock list from the auction import
API:        REST + WebSocket
            GET  /stems
            POST /orders
            WS   /stock
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView
```

---

## Example 440

**Intent:**
small landscaping company, quote builder from a price list of services and plants

**Spec:**
```
Type:       Web application (landscape quotes)
Auth:       Email + password login
Data model: PriceItem(id, name, unit, price, category)
            LandscapeQuote(id, client, address, status, total)
            LandscapeQuoteLine(id, quote_id -> LandscapeQuote, item_id -> PriceItem, quantity)
Features:   - Build quotes from a price list of labour, materials and plants
            - Group lines into sections like patio, turf and planting
            - Email a PDF quote
            - Convert accepted quotes into jobs
API:        REST
            POST /quotes
            POST /quotes/{id}/lines
            POST /quotes/{id}/send
Storage:    PostgreSQL
Tech stack: Laravel, Livewire, DomPDF
```

---

## Example 441

**Intent:**
track my food truck commissary kitchen hours used by each truck for billing

**Spec:**
```
Type:       Web application (shared kitchen time billing)
Auth:       Truck owner login; kitchen manager admin
Data model: Tenant(id, truck_name, hourly_rate)
            KitchenSlot(id, tenant_id -> Tenant, starts_at, ends_at, station)
            UsageLog(id, tenant_id -> Tenant, checked_in, checked_out)
Features:   - Book kitchen stations by the hour
            - Check in and out on a tablet
            - Bill actual hours used monthly
            - Charge for no-shows on booked slots
API:        REST
            POST /slots
            POST /usage/check-in
            GET  /invoices?month={m}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 442

**Intent:**
mobile app with backend for our tree surgeons to do risk assessments before climbing

**Spec:**
```
Type:       Mobile application with backend (arborist risk assessments)
Auth:       Email + password login for crew
Data model: TreeJob(id, address, client, date)
            RiskAssessment(id, job_id -> TreeJob, hazards, controls, rescue_plan, signed_by, signed_at)
            CrewSignoff(id, assessment_id -> RiskAssessment, crew_member, signed_at)
Features:   - Fill a site risk assessment before work starts
            - Pick hazards and controls from lists
            - Record the aerial rescue plan
            - Get every crew member to sign off
            - Work offline and sync later
API:        REST
            POST /jobs/{id}/assessments
            POST /assessments/{id}/signoffs
Storage:    PostgreSQL (server), SQLite (device)
Tech stack: React Native, Expo, Node.js
```

---

## Example 443

**Intent:**
print shop customer artwork approvals by email reply

**Spec:**
```
Type:       Webhook service (email-based proof approvals)
Data model: ProofJob(id, number, customer_email, proof_url, status)
            EmailEvent(id, job_id -> ProofJob, body, decision, received_at)
Features:   - Send proof emails with the job number in the subject
            - Receive replies through the inbound email webhook
            - Detect "approved" or change requests in the reply
            - Update the job status and notify the designer
API:        REST
            POST /webhooks/inbound-email
Storage:    PostgreSQL
Tech stack: Python, Flask, SendGrid Inbound Parse
```

---

## Example 444

**Intent:**
helping out at my aunt's horse feed store, they want farmers to order feed bags online for delivery on their usual delivery day by village

**Spec:**
```
Type:       Web application (rural feed delivery ordering)
Auth:       Customer email + password login
Data model: Village(id, name, delivery_weekday)
            FeedProduct(id, name, bag_kg, price)
            FeedOrder(id, customer_id -> User, village_id -> Village, delivery_date, status)
            FeedLine(id, order_id -> FeedOrder, product_id -> FeedProduct, bags)
Features:   - Show the next delivery date for the customer's village
            - Order feed bags for that date
            - Total bags per delivery day for loading
            - Pay on account monthly
API:        REST
            GET  /villages/{id}/next-delivery
            POST /orders
            GET  /admin/load-list?date={d}
Storage:    PostgreSQL
Tech stack: Django
```

---

## Example 445

**Intent:**
online ordering of custom engraved headstones with live preview of the text

**Spec:**
```
Type:       Web application (memorial design preview)
Auth:       Family member email login; mason admin
Data model: StoneShape(id, name, width_mm, height_mm, base_price)
            Font(id, name, price_per_letter)
            MemorialDesign(id, user_id -> User, shape_id -> StoneShape, font_id -> Font, inscription, motif, price, status)
Features:   - Choose stone shape, colour and font
            - Type the inscription and see a live preview
            - Price by letters and motifs
            - Submit the design for a proof from the mason
API:        REST
            POST /designs
            POST /designs/{id}/price
            POST /designs/{id}/submit
Storage:    PostgreSQL
Tech stack: React, Fabric.js, Node.js
```

---

## Example 446

**Intent:**
web dashboard for factory energy use per machine from smart meters

**Spec:**
```
Type:       Data dashboard (energy monitoring)
Features:   - Collect kWh readings from sub-meters every 15 minutes
            - Show energy use per machine and line
            - Compare energy per unit produced
            - Highlight machines using power while idle at night
Input:      Modbus meter readings via a gateway
Storage:    TimescaleDB
Tech stack: Python, pymodbus, Grafana
```

---

## Example 447

**Intent:**
dog groomers mobile van, need recurring appointments every 6 weeks for each dog

**Spec:**
```
Type:       Web application (recurring grooming appointments)
Auth:       Groomer login
Data model: Dog(id, owner, phone, address, name, interval_weeks)
            GroomAppointment(id, dog_id -> Dog, starts_at, status)
Features:   - Book the next appointment automatically after each groom
            - Keep each dog's interval
            - Text owners 2 days before
            - Fill cancellations from a waitlist
API:        REST
            POST /appointments
            PATCH /appointments/{id}/complete
Storage:    PostgreSQL
Tech stack: Python, Flask, Twilio
```

---

## Example 448

**Intent:**
B2B quote request system for industrial fasteners with RFQ uploads

**Spec:**
```
Type:       Web application (RFQ handling)
Auth:       Customer email + password login; sales login
Data model: RFQ(id, customer_id -> User, reference, status, due_on)
            RFQLine(id, rfq_id -> RFQ, part_desc, material, quantity, unit_price)
            RFQFile(id, rfq_id -> RFQ, url)
Features:   - Upload an RFQ spreadsheet or add lines manually
            - Let sales price each line and set lead time
            - Send the quote back to the customer
            - Convert an accepted quote to an order
API:        REST
            POST /rfqs
            POST /rfqs/{id}/lines/import
            POST /rfqs/{id}/quote
Storage:    PostgreSQL, S3
Tech stack: C#, ASP.NET Core, Angular
```

---

## Example 449

**Intent:**
cafe owner wants a web page for staff to log fridge temps twice daily with alarms

**Spec:**
```
Type:       Web application (temperature logging)
Auth:       Staff PIN login
Data model: Unit(id, name, max_c)
            Reading(id, unit_id -> Unit, temp_c, staff, taken_at, action_taken)
Features:   - Log temperatures at opening and closing
            - Require a corrective action when too warm
            - Send the owner a message if a reading is missed
API:        REST
            POST /readings
            GET  /readings?date={d}
Storage:    SQLite
Tech stack: Go, HTMX
```

---

## Example 450

**Intent:**
software for small funeral home to schedule the hearse, chapel and staff for each service

**Spec:**
```
Type:       Web application (funeral resource scheduling)
Auth:       Email + password login for staff
Data model: Resource(id, name, type)
            FuneralService(id, deceased_name, starts_at, ends_at, location)
            ResourceBooking(id, service_id -> FuneralService, resource_id -> Resource)
            StaffBooking(id, service_id -> FuneralService, staff_id -> User, role)
Features:   - Book hearse, limousines, chapel and staff for each funeral
            - Prevent double-booking any resource
            - Show a day plan with all services
            - Print a running sheet for each service
API:        REST
            POST /services
            POST /services/{id}/resources
            GET  /day-plan?date={d}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, FullCalendar
```

---

## Example 451

**Intent:**
notary journal of every signing with ID details

**Spec:**
```
Type:       Web application (notary journal)
Auth:       Notary login with 2FA
Data model: JournalEntry(id, signed_at, document_type, signer_name, signer_address, id_type, id_number_encrypted, fee, thumbprint_url)
Features:   - Record each notarisation with signer and ID details
            - Capture a thumbprint image when required
            - Make entries read-only once saved
            - Search entries by name or date
            - Export the journal for a state audit
API:        REST
            POST /entries
            GET  /entries?q={q}
            GET  /export?year={y}
Storage:    PostgreSQL (encrypted fields)
Tech stack: Python, Django
```

---

## Example 452

**Intent:**
my pressure washing biz needs before and after photo pages to send customers + review request

**Spec:**
```
Type:       Web application (job showcase and reviews)
Auth:       Owner login
Data model: WashJob(id, customer, email, address, date, share_token)
            JobPhoto(id, job_id -> WashJob, kind, url)
Features:   - Upload before and after photos per job
            - Send the customer a page with a comparison slider
            - Ask for a Google review on the same page
            - Reuse photos in a public gallery with permission
API:        REST
            POST /jobs
            POST /jobs/{id}/photos
            GET  /share/{token}
Storage:    PostgreSQL, Cloudinary
Tech stack: Next.js
```

---

## Example 453

**Intent:**
inspection app for scaffolding tags every 7 days

**Spec:**
```
Type:       Web application (scaffold inspections)
Auth:       Email + password login for inspectors
Data model: Scaffold(id, site, location, tag_code, erected_on, status)
            ScaffoldInspection(id, scaffold_id -> Scaffold, inspector_id -> User, inspected_on, safe, defects)
Features:   - Scan the scaffold tag QR code to start an inspection
            - Record defects and mark the scaffold safe or unsafe
            - Alert when a scaffold passes 7 days without inspection
            - Show the inspection register per site
API:        REST
            GET  /scaffolds/{tag}
            POST /scaffolds/{tag}/inspections
            GET  /sites/{id}/register
Storage:    PostgreSQL
Tech stack: Vue.js (PWA), Node.js, Express
```

---

## Example 454

**Intent:**
Our winery has a wine club with 3 shipments a year. Members choose red, white or mixed, and we need to charge them and create shipping labels each release.

**Spec:**
```
Type:       Web application (wine club management)
Auth:       Member email + password login; staff admin
Data model: ClubMember(id, name, email, address, preference, card_on_file, active)
            Release(id, name, ship_date, red_price, white_price, mixed_price)
            ClubShipment(id, release_id -> Release, member_id -> ClubMember, charged, label_url, status)
Features:   - Let members choose and change their preference
            - Charge all members when a release is processed
            - Retry failed payments and notify members
            - Create shipping labels in bulk
            - Allow pickup instead of shipping
API:        REST
            POST /releases/{id}/process
            GET  /releases/{id}/shipments
            PATCH /members/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe, ShipStation API
```

---

## Example 455

**Intent:**
log of complaints for a bakery and how we resolved them

**Spec:**
```
Type:       Web application (complaint log)
Auth:       Staff login
Data model: Complaint(id, customer, contact, product, batch, description, received_on, category)
            Resolution(id, complaint_id -> Complaint, action, refund_amount, resolved_on)
Features:   - Record complaints with product and batch
            - Record the resolution and any refund
            - Show complaints by product and category
            - Flag repeat issues with the same batch
API:        REST
            POST /complaints
            POST /complaints/{id}/resolution
Storage:    SQLite
Tech stack: Flask
```

---

## Example 456

**Intent:**
web app for a hearing aid clinic to track devices, warranty and battery orders per patient

**Spec:**
```
Type:       Web application (device and patient records)
Auth:       Staff email + password login
Data model: Patient(id, name, birth_date, phone)
            HearingAid(id, patient_id -> Patient, model, serial, side, fitted_on, warranty_until)
            BatteryOrder(id, patient_id -> Patient, size, packs, sent_on)
Features:   - Record hearing aids fitted per patient
            - Alert before warranty ends
            - Send battery packs and remind patients to reorder
            - Log repairs sent to the manufacturer
API:        REST
            POST /patients/{id}/aids
            POST /patients/{id}/battery-orders
            GET  /aids/warranty-ending
Storage:    PostgreSQL
Tech stack: Django
```

---

## Example 457

**Intent:**
online booking for private chef dinners at people's homes

**Spec:**
```
Type:       Web application (private dining bookings)
Auth:       Chef admin login; clients book as guests
Data model: MenuOption(id, name, courses, price_per_person)
            DinnerBooking(id, menu_id -> MenuOption, date, guests, address, allergies, total, deposit_paid)
Features:   - Choose a menu and number of guests
            - Collect allergies and kitchen details
            - Check the chef's free dates
            - Pay a deposit to confirm
API:        REST
            GET  /menus
            GET  /dates
            POST /bookings
Storage:    PostgreSQL
Tech stack: Astro, Netlify Functions, Stripe
```

---

## Example 458

**Intent:**
contract manufacturing customer portal where brands see their production run status and lot certificates

**Spec:**
```
Type:       Web application (production run portal)
Auth:       Brand customer email + password login
Data model: Brand(id, name)
            ProductionRun(id, brand_id -> Brand, product, quantity, scheduled_on, stage, lot_number)
            CertificateOfAnalysis(id, run_id -> ProductionRun, file_url, released_on)
Features:   - Show each brand its scheduled and running batches
            - Show stage updates (materials, production, QC, shipped)
            - Download certificates of analysis per lot
            - Notify the brand when a run ships
API:        REST
            GET  /runs
            GET  /runs/{id}/coa
Storage:    PostgreSQL, S3
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 459

**Intent:**
hey need a simple stock take app for my bar, count bottles by 10ths at the end of each week

**Spec:**
```
Type:       Web application (bar stock take)
Auth:       Manager login
Data model: Bottle(id, name, size_ml, cost)
            StockTake(id, date)
            CountLine(id, stocktake_id -> StockTake, bottle_id -> Bottle, full, tenths)
Features:   - Count full bottles and open bottles in tenths
            - Calculate usage since last stock take with deliveries
            - Compare usage with POS sales to find losses
            - Show stock value
API:        REST
            POST /stocktakes
            POST /stocktakes/{id}/lines
            GET  /stocktakes/{id}/variance
Storage:    SQLite
Tech stack: Svelte, Node.js
```

---

## Example 460

**Intent:**
web app for printing company to send overnight jobs to a partner printer and track them

**Spec:**
```
Type:       Web application (outsourced print jobs)
Auth:       Email + password login; roles: our staff, partner printer
Data model: Partner(id, name, email, capabilities)
            OutsourcedJob(id, partner_id -> Partner, spec, quantity, file_url, cost, due_at, status, tracking_no)
Features:   - Send a job with files to a partner printer
            - Let the partner accept and update status
            - Record cost and shipping tracking number
            - Flag jobs late against due time
API:        REST
            POST /jobs
            PATCH /jobs/{id}/status
Storage:    PostgreSQL, S3
Tech stack: Rails
```

---

## Example 461

**Intent:**
We are a small landscaping crew and need to keep track of our equipment like mowers, trimmers and blowers: who has it, when it was last serviced, and repairs.

**Spec:**
```
Type:       Web application (equipment register)
Auth:       Email + password login
Data model: Equipment(id, name, type, serial, purchased_on, hours, last_serviced_on)
            Holder(id, equipment_id -> Equipment, crew_member, from_date)
            Repair(id, equipment_id -> Equipment, date, issue, cost)
Features:   - Register equipment with serial number
            - Assign equipment to crew members
            - Track service intervals by hours or months
            - Log repairs and costs
API:        REST
            POST /equipment
            POST /equipment/{id}/assign
            POST /equipment/{id}/repairs
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 462

**Intent:**
auto parts store: look up parts by VIN and check stock across stores

**Spec:**
```
Type:       Web application (VIN parts lookup)
Auth:       Staff login
Data model: Part(id, part_number, name, brand, price)
            Fitment(id, part_id -> Part, make, model, year, engine)
            StoreStock(id, part_id -> Part, store, quantity)
Features:   - Decode a VIN to make, model, year and engine
            - Show parts that fit the vehicle by category
            - Show stock at every store
            - Request a transfer from another store
API:        REST
            GET  /vin/{vin}
            GET  /parts?vehicle={id}&category={c}
            POST /transfers
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, NHTSA vPIC API
```

---

## Example 463

**Intent:**
church cleaning and flower rota with reminders

**Spec:**
```
Type:       Web application (volunteer rota reminders)
Auth:       Admin login
Data model: Volunteer(id, name, email, phone)
            RotaDuty(id, type, week_start, volunteer_id -> Volunteer)
Features:   - Create cleaning and flower rotas for the quarter
            - Email volunteers a reminder on Monday of their week
            - Let volunteers mark that they can't do it
            - Notify the admin to find a replacement
API:        REST
            GET  /rota
            POST /duties/{id}/decline
Storage:    SQLite
Tech stack: Python, Flask, cron
```

---

## Example 464

**Intent:**
electrician wholesaler cable cutting service, customers order cable cut to length from drums

**Spec:**
```
Type:       Web application (cut-to-length orders)
Auth:       Trade account login
Data model: CableType(id, name, price_per_m)
            Drum(id, cable_type_id -> CableType, metres_left, location)
            CutOrder(id, account_id -> User, cable_type_id -> CableType, metres, drum_id -> Drum, status)
Features:   - Order cable by type and exact length
            - Choose a drum with enough left to minimise waste
            - Update the drum's remaining metres after cutting
            - Show drums that are nearly empty
API:        REST
            POST /cut-orders
            PATCH /cut-orders/{id}/cut
            GET  /drums/low
Storage:    PostgreSQL
Tech stack: Django
```

---

## Example 465

**Intent:**
web app for my wedding videography: couples choose music for their film from a licensed list

**Spec:**
```
Type:       Web application (music selection for films)
Auth:       Couples log in with a project code
Data model: Track(id, title, artist, mood, preview_url, licence_id)
            FilmProject(id, couple_names, code, status)
            TrackChoice(id, project_id -> FilmProject, track_id -> Track, part)
Features:   - Browse licensed tracks by mood with previews
            - Pick a track for the highlights film and the ceremony edit
            - Lock choices once editing starts
API:        REST
            GET  /tracks?mood={m}
            POST /projects/{code}/choices
Storage:    PostgreSQL
Tech stack: Vue.js, Node.js
```

---

## Example 466

**Intent:**
accounting firm wants a client onboarding with ID verification and anti money laundering checks

**Spec:**
```
Type:       Web application (client onboarding and AML)
Auth:       Email + password login for staff; clients via secure link
Data model: Prospect(id, name, email, type, risk_rating, status)
            IdentityCheck(id, prospect_id -> Prospect, provider_ref, result, checked_at)
            BeneficialOwner(id, prospect_id -> Prospect, name, ownership_pct, verified)
Features:   - Send a link for the client to upload ID and a selfie
            - Run an electronic identity check through a provider
            - Record beneficial owners for companies
            - Assign a risk rating and require partner approval for high risk
API:        REST
            POST /prospects
            POST /prospects/{id}/id-check
            POST /prospects/{id}/approve
Storage:    PostgreSQL, S3 (encrypted)
Tech stack: Python, Django, Onfido API
```

---

## Example 467

**Intent:**
kitchen display for a bakery's custom order production

**Spec:**
```
Type:       Web application (production display)
Auth:       Kitchen login
Data model: ProductionTask(id, order_ref, item, decoration_notes, due_at, station, status)
Features:   - Show tasks per station on a large screen
            - Colour tasks by how soon they are due
            - Tap to start and finish a task
            - Update in real time across screens
API:        REST + WebSocket
            GET  /tasks?station={s}
            PATCH /tasks/{id}
            WS   /tasks/live
Storage:    PostgreSQL
Tech stack: React, Socket.IO, Node.js
```

---

## Example 468

**Intent:**
hi! we have a little ferry for bikes and people across the river, want to sell tickets online with time of crossing

**Spec:**
```
Type:       Web application (ferry ticketing)
Auth:       Operator login
Data model: Crossing(id, departs_at, direction, passenger_capacity, bike_capacity)
            FerryTicket(id, crossing_id -> Crossing, passengers, bikes, email, code, total)
Features:   - Show crossings with seats and bike spaces left
            - Buy tickets for passengers and bikes
            - Show a QR ticket on the phone
            - Scan tickets at boarding
API:        REST
            GET  /crossings?date={d}
            POST /tickets
            POST /tickets/{code}/scan
Storage:    PostgreSQL
Tech stack: SvelteKit, Stripe
```

---

## Example 469

**Intent:**
manage hotel conference room bookings with catering add-ons and invoice the company

**Spec:**
```
Type:       Web application (meeting room sales)
Auth:       Sales staff login; corporate clients book with email login
Data model: MeetingRoom(id, name, theatre_capacity, boardroom_capacity, day_rate)
            CateringPackage(id, name, price_per_person)
            Conference(id, room_id -> MeetingRoom, company, date, delegates, layout, catering_id -> CateringPackage, total, status)
Features:   - Check room availability and capacity by layout
            - Add catering packages per delegate
            - Send a proposal and take a deposit
            - Invoice the company after the event
API:        REST
            GET  /rooms/available?date={d}&delegates={n}
            POST /conferences
            POST /conferences/{id}/invoice
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, React
```

---

## Example 470

**Intent:**
shed and garden building company, customers design their shed size, door position, windows and see price

**Spec:**
```
Type:       Web application (3D shed configurator)
Auth:       Admin login; customers order as guests
Data model: ShedModel(id, name, base_price, price_per_m2)
            Extra(id, name, price)
            ShedDesign(id, model_id -> ShedModel, width_m, depth_m, door_side, windows, extras, price)
Features:   - Choose size, door position and number of windows
            - Show a 3D preview that updates live
            - Calculate the price including base and installation
            - Order with a deposit
API:        REST
            POST /designs/price
            POST /orders
Storage:    PostgreSQL
Tech stack: React, Three.js, Node.js, Stripe
```

---

## Example 471

**Intent:**
accounts payable approval for a property management company: invoices per building approved by building manager

**Spec:**
```
Type:       Web application (invoice approval)
Auth:       Single sign-on with Google Workspace
Data model: Building(id, name, manager_id -> User)
            PayableInvoice(id, building_id -> Building, supplier, amount, file_url, status, due_on)
            ApprovalStep(id, invoice_id -> PayableInvoice, approver_id -> User, decision, decided_at)
Features:   - Upload supplier invoices and tag them to a building
            - Route to the building manager for approval
            - Require a second approval above a set amount
            - Export approved invoices to the accounting system
API:        REST
            POST /invoices
            POST /invoices/{id}/decision
            GET  /invoices/export
Storage:    PostgreSQL, S3
Tech stack: Node.js, Express, React
```

---

## Example 472

**Intent:**
reserve a table at our brewery beer garden for groups

**Spec:**
```
Type:       Web application (group table reservations)
Auth:       Staff login
Data model: GardenTable(id, number, seats, covered)
            GroupBooking(id, table_ids, name, phone, party_size, date, time, deposit_paid)
Features:   - Book tables for groups of 6 or more
            - Combine tables for larger groups
            - Charge a deposit per head for weekend bookings
            - Show staff a table plan for the day
API:        REST
            GET  /availability?date={d}&size={n}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Next.js, Stripe
```

---

## Example 473

**Intent:**
For my small tutoring centre I want to keep track of which room each class is in so we don't double book rooms when we add extra classes.

**Spec:**
```
Type:       Web application (room timetable)
Auth:       Staff login
Data model: Room(id, name, seats)
            TimetableClass(id, subject, tutor, weekday, start_time, end_time, room_id -> Room, students)
Features:   - Show a weekly timetable grid by room
            - Prevent overlapping classes in the same room
            - Warn when students exceed room seats
            - Suggest free rooms for a new class time
API:        REST
            GET  /timetable
            POST /classes
            GET  /rooms/free?weekday={w}&start={t}&end={t}
Storage:    SQLite
Tech stack: Python, Flask, FullCalendar
```

---

## Example 474

**Intent:**
fleet van booking for staff in our company to reserve a pool van

**Spec:**
```
Type:       Web application (pool vehicle booking)
Auth:       Single sign-on with Microsoft Entra ID
Data model: PoolVan(id, registration, seats, location)
            VanReservation(id, van_id -> PoolVan, user_id -> User, starts_at, ends_at, purpose, start_km, end_km)
Features:   - Reserve a pool van for a time range
            - Record mileage at pickup and return
            - Report damage or low fuel on return
            - Show usage per department
API:        REST
            GET  /vans/available
            POST /reservations
            PATCH /reservations/{id}/return
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 475

**Intent:**
web app for my cleaning company to send invoices automatically after each job is completed

**Spec:**
```
Type:       Web application (automatic job invoicing)
Auth:       Email + password login
Data model: Customer(id, name, email, billing_type)
            CompletedJob(id, customer_id -> Customer, date, hours, price, invoiced)
            Invoice(id, customer_id -> Customer, number, total, sent_at, paid_at)
Features:   - Create an invoice when a job is marked complete
            - Group jobs into one monthly invoice for business customers
            - Email invoices with a payment link
            - Send reminders for unpaid invoices
API:        REST
            POST /jobs/{id}/complete
            GET  /invoices?status=unpaid
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe Invoicing
```

---

## Example 476

**Intent:**
customer self check in kiosk for a vet clinic

**Spec:**
```
Type:       Web application (check-in kiosk)
Auth:       Kiosk device token; reception login
Data model: Appointment(id, pet_name, owner_phone, starts_at, vet, checked_in_at)
Features:   - Check in on a tablet with a phone number
            - Confirm the pet and appointment time
            - Ask if anything has changed since the last visit
            - Show reception a live waiting list
API:        REST
            POST /check-in
            GET  /waiting-list
Storage:    PostgreSQL
Tech stack: Vue.js, Node.js, Socket.IO
```

---

## Example 477

**Intent:**
tool for event planners to collect RSVPs and meal choices for corporate dinners

**Spec:**
```
Type:       Web application (event RSVPs)
Auth:       Planner login; guests RSVP via personal link
Data model: DinnerEvent(id, name, date, venue, rsvp_deadline)
            Invitee(id, event_id -> DinnerEvent, name, email, token, attending, meal_choice, dietary)
Features:   - Import invitees and send personal invite emails
            - Collect attendance, meal choice and dietary needs
            - Send reminders before the RSVP deadline
            - Export meal counts for the venue
API:        REST
            POST /events/{id}/invitees/import
            POST /rsvp/{token}
            GET  /events/{id}/meals
Storage:    PostgreSQL
Tech stack: Laravel, Mailgun
```

---

## Example 478

**Intent:**
our bakery van sells in villages, customers want to pre order so van carries the right bread

**Spec:**
```
Type:       Web application (route pre-orders)
Auth:       Customer email login; driver login
Data model: VillageStop(id, village, weekday, time)
            BreadItem(id, name, price)
            VanPreOrder(id, stop_id -> VillageStop, customer_id -> User, date, paid)
            VanPreOrderLine(id, order_id -> VanPreOrder, item_id -> BreadItem, quantity)
Features:   - Show van stops and times per village
            - Pre-order bread for the next visit
            - Give the driver a loading list per day
            - Mark pre-orders handed over at each stop
API:        REST
            GET  /stops
            POST /preorders
            GET  /loading-list?date={d}
Storage:    SQLite
Tech stack: Django, HTMX
```

---

## Example 479

**Intent:**
supplier certificate tracking for our food factory — organic, halal, allergen statements per ingredient supplier

**Spec:**
```
Type:       Web application (supplier certificate management)
Auth:       Email + password login for QA team
Data model: Supplier(id, name, contact_email)
            RawMaterial(id, supplier_id -> Supplier, name)
            Certificate(id, supplier_id -> Supplier, type, file_url, expires_on, verified)
Features:   - Store certificates per supplier and type
            - Email suppliers for a new certificate before expiry
            - Block raw materials whose supplier lacks a valid certificate
            - Produce a supplier approval report for audits
API:        REST
            POST /suppliers/{id}/certificates
            GET  /certificates/expiring
            GET  /reports/approval
Storage:    PostgreSQL, S3
Tech stack: Python, FastAPI, React
```

---

## Example 480

**Intent:**
online payment page for my driving school so pupils pay for lessons by card or bank transfer

**Spec:**
```
Type:       Web application (lesson payments)
Auth:       Pupil email login
Data model: Pupil(id, name, email, balance)
            LessonPayment(id, pupil_id -> Pupil, amount, method, status, paid_at)
Features:   - Pay for lessons by card or open banking transfer
            - Add the payment to the pupil's balance
            - Send a receipt by email
            - Show the instructor all payments this month
API:        REST
            POST /payments
            POST /webhooks/payments
            GET  /admin/payments?month={m}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Stripe, GoCardless
```

---

## Example 481

**Intent:**
log of hazardous waste collections for our garage with consignment notes

**Spec:**
```
Type:       Web application (hazardous waste records)
Auth:       Email + password login
Data model: WasteStream(id, name, ewc_code)
            Collection(id, stream_id -> WasteStream, carrier, quantity_kg, collected_on, consignment_no, note_url)
Features:   - Record each collection of oil, batteries and filters
            - Upload the consignment note
            - Show quantities per waste stream per year
            - Remind when carrier licences need checking
API:        REST
            POST /collections
            GET  /reports/yearly
Storage:    SQLite, local file storage
Tech stack: Flask
```

---

## Example 482

**Intent:**
wedding planner payment schedule tracker for each couple's vendor payments

**Spec:**
```
Type:       Web application (vendor payment schedules)
Auth:       Planner login; couples view
Data model: Wedding(id, couple_names, date)
            VendorContract(id, wedding_id -> Wedding, vendor, total)
            PaymentDue(id, contract_id -> VendorContract, amount, due_on, paid_on)
Features:   - Add vendor contracts with payment schedules
            - Remind couples of payments due in the next 14 days
            - Show paid and remaining amounts per vendor
            - Show a calendar of all payment dates
API:        REST
            POST /weddings/{id}/contracts
            PATCH /payments/{id}/paid
            GET  /weddings/{id}/payments
Storage:    PostgreSQL
Tech stack: Vue.js, Supabase
```

---

## Example 483

**Intent:**
online bookings for a mobile notary who travels to clients, with travel fee by distance

**Spec:**
```
Type:       Web application (mobile notary booking)
Auth:       Notary admin login; clients book as guests
Data model: NotaryBooking(id, name, email, address, document_type, signers, starts_at, distance_km, travel_fee, total)
Features:   - Calculate travel fee from distance to the client address
            - Price by number of signatures
            - Book a time slot and pay online
            - Remind clients to have valid ID ready
API:        REST
            GET  /quote?address={a}&signers={n}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Next.js, Google Maps Distance Matrix API, Stripe
```

---

## Example 484

**Intent:**
bakery wholesale invoices with credits for returned unsold bread

**Spec:**
```
Type:       Web application (sale-or-return invoicing)
Auth:       Email + password login
Data model: Outlet(id, name)
            Delivery(id, outlet_id -> Outlet, date, items_json, value)
            ReturnNote(id, outlet_id -> Outlet, date, items_json, credit_value)
            WeeklyInvoice(id, outlet_id -> Outlet, week_start, total)
Features:   - Record daily deliveries per outlet
            - Record unsold returns and calculate credits
            - Produce weekly invoices net of credits
            - Show return rates per outlet
API:        REST
            POST /deliveries
            POST /returns
            POST /invoices/generate?week={w}
Storage:    PostgreSQL
Tech stack: Django
```

---

## Example 485

**Intent:**
web app to track loaned demo equipment to customers for a medical device sales team

**Spec:**
```
Type:       Web application (demo kit tracking)
Auth:       Single sign-on with Okta
Data model: DemoKit(id, serial, product, status, location)
            DemoLoan(id, kit_id -> DemoKit, rep_id -> User, hospital, out_on, due_on, returned_on)
Features:   - Request a demo kit for a hospital
            - Track which kits are out and with which rep
            - Remind reps of overdue returns
            - Log cleaning and checks before the next loan
API:        REST
            POST /loans
            POST /loans/{id}/return
            GET  /kits?status={s}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

