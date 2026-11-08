## Example 1

**Intent:**
booking site for my barber shop

**Spec:**
```
Type:       Web application (booking system)
Auth:       Customer login by email magic link, separate admin login for staff
Data model: Barber(id, name, photo_url, working_hours)
            Service(id, name, duration_min, price)
            Customer(id, name, email, phone)
            Appointment(id, customer_id -> Customer, barber_id -> Barber, service_id -> Service, start_time, status)
Features:   - Show free time slots per barber and service
            - Book, reschedule and cancel appointments online
            - Send email and SMS reminders 24 hours before
            - Let staff block out breaks and days off
            - Show a daily schedule view for each barber
API:        REST
            GET  /barbers/{id}/slots?date={date}
            POST /appointments
            PATCH /appointments/{id}
            DELETE /appointments/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio (SMS), HTMX
```

---

## Example 2

**Intent:**
I run a small dental practice with three dentists. Patients should be able to request an appointment online and we confirm it from the front desk.

**Spec:**
```
Type:       Web application (appointment requests)
Auth:       Staff login (email + password, roles: receptionist, dentist)
Data model: Dentist(id, name, specialties)
            Patient(id, name, date_of_birth, phone, email)
            AppointmentRequest(id, patient_id -> Patient, dentist_id -> Dentist, preferred_date, reason, status)
            Appointment(id, request_id -> AppointmentRequest, start_time, end_time, room)
Features:   - Submit an appointment request from a public form
            - Review pending requests in a front-desk queue
            - Confirm a request by assigning a time and room
            - Email the patient when a request is confirmed or declined
            - Show each dentist's weekly calendar
API:        REST
            POST /requests
            GET  /requests?status=pending
            POST /requests/{id}/confirm
            GET  /dentists/{id}/calendar?week={date}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma, SendGrid
```

---

## Example 3

**Intent:**
need something to keep track of whats in our stockroom, we keep running out of stuff without noticing

**Spec:**
```
Type:       Web application (inventory)
Auth:       Staff login (email + password)
Data model: Product(id, sku, name, unit, reorder_level)
            StockLevel(id, product_id -> Product, location, quantity)
            StockMovement(id, product_id -> Product, change, reason, user_id -> User, created_at)
            User(id, name, email, password_hash)
Features:   - Record stock coming in and going out
            - Show current quantity per product and location
            - Flag products that fall below their reorder level
            - Send a daily low-stock email to the manager
            - Show the movement history for each product
API:        REST
            GET  /products?low_stock=true
            POST /movements
            GET  /products/{id}/movements
Storage:    PostgreSQL
Tech stack: Python, Flask, SQLAlchemy, Bootstrap
```

---

## Example 4

**Intent:**
simple invoicing tool for a freelance electrician

**Spec:**
```
Type:       Web application (invoicing)
Auth:       Single owner login (email + password)
Data model: Client(id, name, address, email)
            Invoice(id, client_id -> Client, number, issue_date, due_date, status)
            LineItem(id, invoice_id -> Invoice, description, quantity, unit_price, vat_rate)
Features:   - Create invoices with labour and material line items
            - Calculate subtotals, VAT and totals automatically
            - Generate a PDF invoice and email it to the client
            - Mark invoices as paid or overdue
            - Show unpaid totals on a dashboard
API:        REST
            GET  /invoices
            POST /invoices
            GET  /invoices/{id}/pdf
            POST /invoices/{id}/send
Storage:    SQLite
Tech stack: Python, FastAPI, WeasyPrint (PDF), Jinja2
```

---

## Example 5

**Intent:**
My wife and I own a little Italian restaurant with about 15 tables. On weekends people call constantly to reserve and we miss calls while cooking. I'd love a page on our website where guests can see if a table is free and reserve it themselves, and we get a list each morning of who's coming.

**Spec:**
```
Type:       Web application (table reservations)
Auth:       Staff login for the owners; guests book without an account
Data model: Table(id, number, seats, area)
            Reservation(id, guest_name, phone, email, party_size, start_time, table_id -> Table, status, notes)
            OpeningHours(id, weekday, open_time, close_time)
Features:   - Show available times for a chosen date and party size
            - Assign the smallest free table that fits the party
            - Send a confirmation email with a cancel link
            - Email the owners a list of the day's reservations each morning
            - Let staff add phone bookings and mark no-shows
API:        REST
            GET  /availability?date={date}&party={n}
            POST /reservations
            DELETE /reservations/{id}?token={token}
            GET  /admin/reservations?date={date}
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Mailgun, Alpine.js
```

---

## Example 6

**Intent:**
gym membership system with check in at the door

**Spec:**
```
Type:       Web application (membership management)
Auth:       Staff login (email + password); members log in to view their account
Data model: Member(id, name, email, phone, qr_code, status)
            Plan(id, name, monthly_price, access_hours)
            Membership(id, member_id -> Member, plan_id -> Plan, start_date, end_date)
            CheckIn(id, member_id -> Member, checked_in_at)
Features:   - Register members and assign a membership plan
            - Scan a member's QR code at the front desk to check in
            - Block check-in when a membership has expired
            - Bill members monthly by card
            - Show visits per day and peak hours
API:        REST
            POST /members
            POST /checkins
            GET  /members/{id}/membership
            GET  /reports/visits?from={date}&to={date}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe Billing
```

---

## Example 7

**Intent:**
hi i have nail salon and want customers book online and choose which girl do their nails, also see price before

**Spec:**
```
Type:       Web application (booking system)
Auth:       Customer login by phone number + SMS code; owner login for admin
Data model: Technician(id, name, photo_url, skills)
            Treatment(id, name, price, duration_min)
            Customer(id, name, phone)
            Booking(id, customer_id -> Customer, technician_id -> Technician, treatment_id -> Treatment, start_time, status)
Features:   - Show a price list of treatments with durations
            - Let the customer pick a technician or "any available"
            - Show open slots that fit the treatment length
            - Send an SMS confirmation and reminder
            - Let the owner edit technicians' working days
API:        REST
            GET  /treatments
            GET  /slots?treatment={id}&technician={id}&date={date}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire, Twilio
```

---

## Example 8

**Intent:**
CRM for a 5-person real estate agency to track buyers and the properties they've viewed

**Spec:**
```
Type:       Web application (CRM)
Auth:       Agent login (email + password), admin role for the office manager
Data model: Agent(id, name, email, password_hash, role)
            Buyer(id, name, phone, email, budget_max, wanted_areas, agent_id -> Agent)
            Property(id, address, price, bedrooms, status)
            Viewing(id, buyer_id -> Buyer, property_id -> Property, agent_id -> Agent, viewed_at, feedback)
Features:   - Add buyers with budget and search preferences
            - Log viewings with buyer feedback
            - Match buyers to new properties within their budget and area
            - Show each agent's follow-up list for the week
            - Search buyers by name, area or budget
API:        REST
            GET  /buyers?area={area}
            POST /viewings
            GET  /properties/{id}/matches
            GET  /agents/{id}/followups
Storage:    PostgreSQL
Tech stack: Python, Django, Django REST Framework, Vue.js
```

---

## Example 9

**Intent:**
can u make me a thing where my cleaners clock in and out from their phone

**Spec:**
```
Type:       Web application (time tracking)
Auth:       Employee login with PIN; manager login with email + password
Data model: Employee(id, name, pin_hash, hourly_rate)
            Site(id, name, address, latitude, longitude)
            Shift(id, employee_id -> Employee, site_id -> Site, clock_in, clock_out, clock_in_location)
Features:   - Clock in and out from a mobile-friendly page
            - Record GPS location at clock-in and check it against the site
            - Show who is currently on shift
            - Calculate weekly hours and pay per employee
            - Export timesheets to CSV for payroll
API:        REST
            POST /shifts/clock-in
            POST /shifts/{id}/clock-out
            GET  /shifts/active
            GET  /timesheets?week={date}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js (PWA)
```

---

## Example 10

**Intent:**
onlne tickets for our comunity theatre shows, ppl pick there seats

**Spec:**
```
Type:       Web application (event ticketing)
Auth:       Admin login for theatre volunteers; buyers check out as guests
Data model: Show(id, title, description, poster_url)
            Performance(id, show_id -> Show, starts_at)
            Seat(id, row, number, price_band)
            Order(id, performance_id -> Performance, buyer_email, total, status, created_at)
            Ticket(id, order_id -> Order, seat_id -> Seat, qr_code)
Features:   - Show an interactive seat map for each performance
            - Hold selected seats for 10 minutes during checkout
            - Take card payments and email tickets with QR codes
            - Scan QR codes at the door to admit guests
            - Show sales per performance for the organisers
API:        REST
            GET  /performances/{id}/seats
            POST /orders
            POST /tickets/{id}/scan
            POST /payments/webhook
Storage:    PostgreSQL, Redis (seat holds)
Tech stack: TypeScript, Next.js, Stripe Checkout, SVG seat map
```

---

## Example 11

**Intent:**
I manage 12 rental apartments and I want tenants to report repairs online instead of texting me photos at midnight.

**Spec:**
```
Type:       Web application (maintenance requests)
Auth:       Tenant login (email + password); landlord admin login
Data model: Property(id, address)
            Unit(id, property_id -> Property, number)
            Tenant(id, unit_id -> Unit, name, email, phone)
            RepairRequest(id, unit_id -> Unit, tenant_id -> Tenant, category, description, urgency, status, created_at)
            Photo(id, request_id -> RepairRequest, url)
Features:   - Submit a repair request with photos and urgency level
            - Track request status from submitted to fixed
            - Assign requests to a contractor and add notes
            - Notify the landlord immediately only for urgent requests
            - Show open requests grouped by property
API:        REST
            POST /requests
            POST /requests/{id}/photos
            PATCH /requests/{id}
            GET  /requests?status=open
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, AWS S3, Bootstrap
```

---

## Example 12

**Intent:**
staff rota for a cafe

**Spec:**
```
Type:       Web application (shift scheduling)
Auth:       Manager and employee login (email + password)
Data model: Employee(id, name, email, role, max_hours_week)
            Shift(id, employee_id -> Employee, date, start_time, end_time, position)
            Availability(id, employee_id -> Employee, weekday, available_from, available_to)
Features:   - Build a weekly rota on a drag-and-drop grid
            - Warn when a shift clashes with an employee's availability
            - Publish the rota and email each employee their shifts
            - Let staff request shift swaps for manager approval
            - Show total scheduled hours per employee
API:        REST
            GET  /rota?week={date}
            POST /shifts
            POST /rota/{week}/publish
            POST /swaps
Storage:    PostgreSQL
Tech stack: TypeScript, React, NestJS
```

---

## Example 13

**Intent:**
We are a small warehouse doing order fulfilment for online shops. Pickers need to see which orders to pack and scan items with a barcode scanner so we don't send the wrong product.

**Spec:**
```
Type:       Web application (warehouse management)
Auth:       Picker login with badge number + PIN; supervisor login
Data model: Client(id, name)
            Product(id, client_id -> Client, sku, barcode, name, bin_location)
            Order(id, client_id -> Client, external_ref, status, created_at)
            OrderLine(id, order_id -> Order, product_id -> Product, quantity, picked_qty)
Features:   - Show a pick list sorted by bin location
            - Scan barcodes to confirm each picked item
            - Block packing when a scanned item does not match the order
            - Mark orders as packed and print a shipping label
            - Show orders waiting, in progress and shipped
API:        REST
            GET  /orders?status=ready
            POST /orders/{id}/scan
            POST /orders/{id}/pack
            GET  /orders/{id}/label
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor, ZPL label printing
```

---

## Example 14

**Intent:**
phone repair shop job tracker so customers can check if their phone is ready

**Spec:**
```
Type:       Web application (repair tracking)
Auth:       Staff login; customers look up jobs with a ticket number and phone number
Data model: Customer(id, name, phone, email)
            RepairJob(id, ticket_no, customer_id -> Customer, device_model, issue, quote, status, created_at)
            JobNote(id, job_id -> RepairJob, text, created_at)
Features:   - Create a repair ticket at the counter and print a receipt
            - Update job status (received, diagnosing, waiting for parts, ready)
            - Text the customer automatically when the phone is ready
            - Let customers check status on a public lookup page
            - Record the quote and final price for each job
API:        REST
            POST /jobs
            PATCH /jobs/{id}/status
            GET  /track?ticket={no}&phone={phone}
Storage:    MySQL
Tech stack: PHP, Laravel, Livewire, Twilio
```

---

## Example 15

**Intent:**
attendance register for our after school club, parents should get a message if kid not signed in

**Spec:**
```
Type:       Web application (attendance tracking)
Auth:       Staff login (email + password)
Data model: Child(id, name, year_group, allergies)
            Guardian(id, name, phone, email)
            ChildGuardian(child_id -> Child, guardian_id -> Guardian)
            Session(id, date, start_time)
            Attendance(id, session_id -> Session, child_id -> Child, signed_in_at, signed_out_at, collected_by)
Features:   - Sign children in and out on a tablet
            - Record who collected each child
            - Text guardians when an expected child has not arrived 15 minutes after start
            - Show allergy notes next to each child's name
            - Export monthly attendance for invoicing
API:        REST
            GET  /sessions/{id}/register
            POST /attendance/sign-in
            POST /attendance/{id}/sign-out
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, Twilio
```

---

## Example 16

**Intent:**
church members directory and donation tracking

**Spec:**
```
Type:       Web application (membership management)
Auth:       Admin login for church office staff (email + password, 2FA)
Data model: Household(id, name, address)
            Member(id, household_id -> Household, name, email, phone, birthday, ministry_groups)
            Donation(id, household_id -> Household, amount, fund, method, received_on)
Features:   - Keep a searchable directory of members and households
            - Record donations by fund (general, building, missions)
            - Generate yearly giving statements per household as PDF
            - List upcoming birthdays for the pastoral team
            - Export members of a ministry group to CSV
API:        REST
            GET  /members?q={text}
            POST /donations
            GET  /households/{id}/statement?year={year}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Prawn (PDF), Bootstrap
```

---

## Example 17

**Intent:**
Could you build an internal tool in Python where our office staff can request supplies like paper and toner, and the office manager approves and orders them?

**Spec:**
```
Type:       Web application (internal request tool)
Auth:       Company SSO login (Google Workspace OAuth)
Data model: User(id, name, email, role)
            Item(id, name, category, unit_price)
            SupplyRequest(id, user_id -> User, item_id -> Item, quantity, reason, status, created_at)
Features:   - Submit a supply request from a catalogue of items
            - Approve or reject requests as office manager
            - Group approved requests into a weekly order list
            - Notify requesters when their items are ordered
            - Show monthly spend per category
API:        REST
            POST /requests
            POST /requests/{id}/approve
            GET  /orders/weekly
Storage:    PostgreSQL
Tech stack: Python, Django, Google OAuth, Tailwind CSS
```

---

## Example 18

**Intent:**
dog grooming appointments + keep notes on each dog (temper, coat type etc)

**Spec:**
```
Type:       Web application (booking system)
Auth:       Owner login for the groomer; clients book with email confirmation
Data model: Client(id, name, phone, email)
            Dog(id, client_id -> Client, name, breed, size, coat_type, temperament_notes)
            Appointment(id, dog_id -> Dog, service, start_time, duration_min, price, status)
Features:   - Book grooming appointments sized by dog breed and coat
            - Keep a profile per dog with temperament and coat notes
            - Show the groomer's day with each dog's notes
            - Send reminder emails the day before
            - Suggest the next appointment based on the usual interval
API:        REST
            GET  /dogs/{id}
            POST /appointments
            GET  /schedule?date={date}
Storage:    SQLite
Tech stack: Python, Flask, HTMX
```

---

## Example 19

**Intent:**
I own a small bakery and want customers to preorder cakes online for pickup, choosing size, flavour and a message on top.

**Spec:**
```
Type:       Web application (preorders)
Auth:       Admin login for the bakery; customers order as guests
Data model: Cake(id, name, base_price, photo_url)
            Option(id, cake_id -> Cake, type, label, extra_price)
            Order(id, customer_name, phone, email, pickup_date, inscription, total, status)
            OrderItem(id, order_id -> Order, cake_id -> Cake, chosen_options)
Features:   - Show a cake catalogue with size and flavour options
            - Require at least 48 hours notice for pickup dates
            - Take a deposit by card at checkout
            - Show a production list per day for the kitchen
            - Email the customer when the cake is ready
API:        REST
            GET  /cakes
            POST /orders
            GET  /admin/production?date={date}
            POST /payments/webhook
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe
```

---

## Example 20

**Intent:**
yoga studio class schedule where ppl can buy 10 class pass and book spots

**Spec:**
```
Type:       Web application (class booking)
Auth:       Member login (email + password)
Data model: Member(id, name, email, password_hash, credits)
            ClassType(id, name, description)
            ClassSession(id, class_type_id -> ClassType, teacher, starts_at, capacity)
            Booking(id, session_id -> ClassSession, member_id -> Member, status)
            PassPurchase(id, member_id -> Member, credits_added, amount_paid, purchased_at)
Features:   - Show the weekly class timetable with spots left
            - Buy a 10-class pass that adds credits to the account
            - Book a spot using one credit
            - Refund the credit for cancellations up to 12 hours before
            - Add members to a waitlist when a class is full
API:        REST
            GET  /sessions?week={date}
            POST /sessions/{id}/book
            DELETE /bookings/{id}
            POST /passes/checkout
Storage:    PostgreSQL
Tech stack: TypeScript, SvelteKit, Stripe
```

---

## Example 21

**Intent:**
We are a clinic of physiotherapy in Lisbon. We want that patients can see their exercises plan and the therapist can write progress notes after each session.

**Spec:**
```
Type:       Web application (patient portal)
Auth:       Patient and therapist login (email + password, 2FA for therapists)
Data model: Therapist(id, name, email)
            Patient(id, name, email, therapist_id -> Therapist)
            Exercise(id, name, video_url, instructions)
            PlanItem(id, patient_id -> Patient, exercise_id -> Exercise, sets, reps, frequency)
            SessionNote(id, patient_id -> Patient, therapist_id -> Therapist, date, pain_score, notes)
Features:   - Build an exercise plan per patient from an exercise library
            - Show patients their plan with demo videos
            - Write progress notes with a pain score after each session
            - Chart pain scores over time
            - Restrict notes so only the treating therapist can edit them
API:        REST
            GET  /patients/{id}/plan
            POST /patients/{id}/plan
            POST /patients/{id}/notes
Storage:    PostgreSQL (encrypted at rest)
Tech stack: Python, Django, Chart.js
```

---

## Example 22

**Intent:**
customer loyalty stamp card for my coffee shop but digital

**Spec:**
```
Type:       Web application (loyalty program)
Auth:       Customer login by phone number + SMS code; barista login on the counter tablet
Data model: Customer(id, phone, name, stamps, rewards_available)
            StampEvent(id, customer_id -> Customer, staff_id -> Staff, created_at)
            Redemption(id, customer_id -> Customer, created_at)
            Staff(id, name, pin_hash)
Features:   - Add a stamp by scanning the customer's QR code
            - Turn 10 stamps into a free drink reward
            - Redeem a reward at the counter
            - Show customers their stamp progress
            - Show the owner how many rewards were redeemed each month
API:        REST
            POST /customers/{id}/stamps
            POST /customers/{id}/redeem
            GET  /customers/me
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, Preact (PWA), Twilio Verify
```

---

## Example 23

**Intent:**
Our tennis club has 4 courts and members fight over the booking sheet on the noticeboard. Members should book courts online for 1 hour, max 2 bookings a week.

**Spec:**
```
Type:       Web application (court booking)
Auth:       Member login (email + password), admin role for the committee
Data model: Member(id, name, email, password_hash, membership_expires)
            Court(id, name, surface, has_lights)
            CourtBooking(id, court_id -> Court, member_id -> Member, starts_at, partner_names)
Features:   - Show a day grid of courts and hourly slots
            - Book a court for one hour
            - Limit each member to 2 future bookings per week
            - Let admins block courts for matches and coaching
            - Refuse bookings from members with expired membership
API:        REST
            GET  /courts/availability?date={date}
            POST /bookings
            DELETE /bookings/{id}
            POST /admin/blocks
Storage:    PostgreSQL
Tech stack: Python, Flask, SQLAlchemy, Alpine.js
```

---

## Example 24

**Intent:**
hair salon booking with deposit so ppl stop no showing!!

**Spec:**
```
Type:       Web application (booking system)
Auth:       Client login (email + password); stylist and owner logins
Data model: Stylist(id, name, working_hours)
            Service(id, name, duration_min, price, deposit_amount)
            Client(id, name, email, phone, no_show_count)
            Booking(id, client_id -> Client, stylist_id -> Stylist, service_id -> Service, start_time, deposit_paid, status)
Features:   - Book a service with a chosen stylist
            - Charge a deposit by card when booking
            - Keep the deposit when a client does not show up
            - Refund the deposit for cancellations made 48 hours ahead
            - Track no-shows per client
API:        REST
            GET  /slots?service={id}&stylist={id}&date={date}
            POST /bookings
            POST /bookings/{id}/no-show
            POST /bookings/{id}/cancel
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Stripe Payment Intents
```

---

## Example 25

**Intent:**
online menu with QR codes on the tables so guests order from their phone and the kitchen sees it

**Spec:**
```
Type:       Web application (table ordering)
Auth:       Staff login for kitchen and floor; guests order without an account
Data model: Table(id, number, qr_token)
            MenuItem(id, name, category, price, available, allergens)
            Order(id, table_id -> Table, status, total, created_at)
            OrderItem(id, order_id -> Order, menu_item_id -> MenuItem, quantity, note)
Features:   - Open the menu by scanning a table's QR code
            - Add items with notes and send the order
            - Show new orders live on a kitchen display
            - Mark items as unavailable when sold out
            - Let floor staff close the table bill
API:        REST + WebSocket
            GET  /tables/{token}/menu
            POST /orders
            PATCH /orders/{id}/status
            WS   /kitchen/orders
Storage:    PostgreSQL
Tech stack: Node.js, Socket.IO, React
```

---

## Example 26

**Intent:**
vehicle service booking for a garage, customers enter their reg plate and pick a service

**Spec:**
```
Type:       Web application (booking system)
Auth:       Mechanic and admin login; customers book with email confirmation
Data model: Customer(id, name, email, phone)
            Vehicle(id, customer_id -> Customer, reg_plate, make, model, year)
            ServiceType(id, name, duration_hours, price)
            Booking(id, vehicle_id -> Vehicle, service_type_id -> ServiceType, date, bay, status)
Features:   - Look up make and model from the registration plate
            - Book a service on a day with free workshop bay capacity
            - Record work done and parts used per booking
            - Email the customer when the car is ready to collect
            - Remind customers when their yearly service is due
API:        REST
            GET  /vehicles/lookup?reg={plate}
            POST /bookings
            PATCH /bookings/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, DVLA Vehicle Enquiry API, Celery
```

---

## Example 27

**Intent:**
i want google sheets to be my database for a small catering business orders, but with a nicer form for clients

**Spec:**
```
Type:       Web application (order form)
Data model: Order(id, client_name, email, event_date, guest_count, menu_package, dietary_notes, status)
            MenuPackage(id, name, price_per_guest)
Features:   - Show a public order form with menu packages
            - Calculate an estimated price from guest count and package
            - Append each order as a new row in Google Sheets
            - Email the client a copy of their order
            - Read package prices from a separate sheet tab
API:        REST
            GET  /packages
            POST /orders
Storage:    Google Sheets
Tech stack: Google Apps Script, HTML Service, Google Sheets
```

---

## Example 28

**Intent:**
Event registration for a two-day small business conference with early bird tickets and a discount code for members.

**Spec:**
```
Type:       Web application (event registration)
Auth:       Organiser login (email + password)
Data model: TicketType(id, name, price, sale_ends_at, quantity)
            DiscountCode(id, code, percent_off, max_uses, used)
            Attendee(id, name, email, company, ticket_type_id -> TicketType, order_id -> Order)
            Order(id, buyer_email, total, discount_code_id -> DiscountCode, paid_at)
Features:   - Sell early bird tickets until a cut-off date
            - Apply member discount codes at checkout
            - Collect name and company for each attendee
            - Email tickets with a QR code after payment
            - Export the attendee list for name badges
API:        REST
            GET  /tickets
            POST /checkout
            POST /discounts/validate
            GET  /admin/attendees.csv
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Stripe Checkout, Vue.js
```

---

## Example 29

**Intent:**
leave requests for employees. manager approves. show who is off on a calendar

**Spec:**
```
Type:       Web application (HR leave management)
Auth:       Employee and manager login (Microsoft 365 SSO)
Data model: Employee(id, name, email, manager_id -> Employee, annual_allowance)
            LeaveRequest(id, employee_id -> Employee, type, start_date, end_date, status, comment)
            PublicHoliday(id, date, name)
Features:   - Submit leave requests (holiday, sick, unpaid)
            - Approve or reject requests as the line manager
            - Show remaining days of allowance per employee
            - Show a team calendar of who is off
            - Skip weekends and public holidays when counting days
API:        REST
            POST /leave
            POST /leave/{id}/approve
            GET  /calendar?month={month}
            GET  /employees/{id}/balance
Storage:    SQL Server
Tech stack: C#, ASP.NET Core, Microsoft Entra ID, React
```

---

## Example 30

**Intent:**
Hello, I have small hotel with 9 rooms in the mountains. I want own booking page so I not pay big commission to booking platforms.

**Spec:**
```
Type:       Web application (hotel booking engine)
Auth:       Owner admin login; guests book without an account
Data model: RoomType(id, name, capacity, base_price, photos)
            Room(id, room_type_id -> RoomType, number)
            Rate(id, room_type_id -> RoomType, date, price)
            Booking(id, room_id -> Room, guest_name, email, check_in, check_out, guests, total, status)
Features:   - Search free rooms for chosen dates and guests
            - Set seasonal prices per room type and date
            - Take a card deposit when booking
            - Send confirmation and pre-arrival emails
            - Show an occupancy calendar for the owner
API:        REST
            GET  /availability?check_in={date}&check_out={date}&guests={n}
            POST /bookings
            PUT  /admin/rates
            GET  /admin/calendar?month={month}
Storage:    PostgreSQL
Tech stack: PHP, Symfony, Stripe, FullCalendar
```

---

## Example 31

**Intent:**
tool for our bike shop to log bikes in for service

**Spec:**
```
Type:       Web application (repair tracking)
Auth:       Mechanic login (name + PIN)
Data model: Customer(id, name, phone, email)
            Bike(id, customer_id -> Customer, brand, model, frame_number)
            ServiceJob(id, bike_id -> Bike, service_level, notes, due_date, status, price)
            PartUsed(id, job_id -> ServiceJob, part_name, cost)
Features:   - Log a bike in with customer details and requested work
            - Print a tag with the job number to attach to the bike
            - Show a workshop board of jobs by status
            - Add parts used and calculate the final bill
            - Text the customer when the bike is ready
API:        REST
            POST /jobs
            GET  /jobs?status={status}
            POST /jobs/{id}/parts
Storage:    SQLite
Tech stack: Python, Flask, HTMX, Twilio
```

---

## Example 32

**Intent:**
a website for my coworking space where people book hot desks and meeting rooms by the hour and pay with credits

**Spec:**
```
Type:       Web application (space booking)
Auth:       Member login (email + password)
Data model: Member(id, name, email, company, credit_balance)
            Resource(id, name, type, capacity, credits_per_hour)
            Booking(id, resource_id -> Resource, member_id -> Member, starts_at, ends_at, credits_used)
            CreditPurchase(id, member_id -> Member, credits, amount, purchased_at)
Features:   - Show a floor plan with free desks and rooms
            - Book a desk or room for a time range
            - Deduct credits based on resource and duration
            - Top up credits by card
            - Show monthly usage per member for invoicing
API:        REST
            GET  /resources/availability?date={date}
            POST /bookings
            POST /credits/checkout
            GET  /members/{id}/usage?month={month}
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView, Stripe
```

---

## Example 33

**Intent:**
small school needs to send report cards to parents online instead of paper

**Spec:**
```
Type:       Web application (school administration)
Auth:       Teacher and parent login (email + password)
Data model: Student(id, name, class_id -> Class)
            Class(id, name, teacher_id -> Teacher)
            Teacher(id, name, email)
            Parent(id, name, email)
            ReportCard(id, student_id -> Student, term, grades_json, comments, published_at)
Features:   - Enter grades and comments per student and subject
            - Review report cards before publishing
            - Publish report cards to linked parents at once
            - Let parents download report cards as PDF
            - Keep an archive of past terms
API:        REST
            POST /report-cards
            POST /classes/{id}/publish?term={term}
            GET  /parents/me/report-cards
Storage:    PostgreSQL
Tech stack: Python, Django, WeasyPrint
```

---

## Example 34

**Intent:**
Make me a quote builder for my landscaping business so I can send customers a nice quote from my phone after visiting their garden.

**Spec:**
```
Type:       Web application (quotes)
Auth:       Owner login (email + password)
Data model: Customer(id, name, address, email, phone)
            Quote(id, customer_id -> Customer, number, status, valid_until, total)
            QuoteItem(id, quote_id -> Quote, description, quantity, unit, unit_price)
            QuotePhoto(id, quote_id -> Quote, url)
Features:   - Build a quote from saved price items on a phone
            - Attach site photos to the quote
            - Send the quote as a link and PDF by email
            - Let the customer accept the quote online
            - Turn an accepted quote into an invoice
API:        REST
            POST /quotes
            POST /quotes/{id}/send
            POST /quotes/{id}/accept?token={token}
            POST /quotes/{id}/invoice
Storage:    PostgreSQL, S3 (photos)
Tech stack: TypeScript, Remix, Tailwind CSS, Puppeteer (PDF)
```

---

## Example 35

**Intent:**
library for our office, who borrowed which book

**Spec:**
```
Type:       Web application (internal lending)
Auth:       Company SSO login (Google OAuth)
Data model: Book(id, title, author, isbn, copies)
            Employee(id, name, email)
            Loan(id, book_id -> Book, employee_id -> Employee, borrowed_at, due_at, returned_at)
Features:   - Add books by scanning or typing the ISBN
            - Borrow and return books
            - Show who currently has each book
            - Send reminders when a loan is overdue
API:        REST
            GET  /books?q={text}
            POST /loans
            POST /loans/{id}/return
Storage:    SQLite
Tech stack: Python, FastAPI, Open Library API, Svelte
```

---

## Example 36

**Intent:**
we're a 3 vet practice and want owners to get vaccine reminders automatically and book from the reminder email

**Spec:**
```
Type:       Web application (veterinary clinic)
Auth:       Staff login (email + password); owners book via signed links
Data model: Owner(id, name, email, phone)
            Pet(id, owner_id -> Owner, name, species, birth_date)
            Vaccination(id, pet_id -> Pet, vaccine, given_on, next_due)
            Appointment(id, pet_id -> Pet, vet_id -> Vet, start_time, reason)
            Vet(id, name)
Features:   - Record vaccinations with next due dates
            - Email owners 2 weeks before a vaccine is due
            - Book an appointment from a link in the reminder
            - Show each vet's daily schedule
            - List pets overdue for vaccination
API:        REST
            POST /pets/{id}/vaccinations
            GET  /book?token={token}
            POST /appointments
            GET  /vaccinations/overdue
Storage:    PostgreSQL
Tech stack: Python, Django, Celery, Postmark
```

---

## Example 37

**Intent:**
inventory for my small clothing boutique, need sizes and colors per item and sync with my shopify

**Spec:**
```
Type:       Web application (inventory)
Auth:       Owner and staff login (email + password)
Data model: Product(id, name, brand, season, shopify_product_id)
            Variant(id, product_id -> Product, size, color, sku, quantity, shopify_variant_id)
            StockAdjustment(id, variant_id -> Variant, change, reason, created_at)
Features:   - Manage products with size and colour variants
            - Adjust stock for in-store sales and deliveries
            - Push stock levels to Shopify after every change
            - Pull online orders from Shopify webhooks to reduce stock
            - Show sell-through rate per product and season
API:        REST
            GET  /products
            POST /variants/{id}/adjust
            POST /webhooks/shopify/orders
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Shopify Admin API, Sidekiq
```

---

## Example 38

**Intent:**
appointment system for a tattoo studio, need deposit and a consent form signed before

**Spec:**
```
Type:       Web application (booking system)
Auth:       Artist and admin login; clients book with email verification
Data model: Artist(id, name, style, portfolio_url)
            Client(id, name, email, date_of_birth)
            Booking(id, client_id -> Client, artist_id -> Artist, start_time, hours, design_notes, deposit_paid, status)
            ConsentForm(id, booking_id -> Booking, signature_url, signed_at)
Features:   - Request a session with a chosen artist and reference images
            - Take a non-refundable deposit by card
            - Sign a digital consent form before the appointment
            - Block bookings from clients under 18
            - Show each artist's calendar
API:        REST
            POST /bookings
            POST /bookings/{id}/deposit
            POST /bookings/{id}/consent
            GET  /artists/{id}/calendar
Storage:    PostgreSQL, S3 (reference images, signatures)
Tech stack: Node.js, NestJS, Next.js, Stripe
```

---

## Example 39

**Intent:**
a dashboard for my restaurant to see daily sales from the till, best dishes and busiest hours

**Spec:**
```
Type:       Data dashboard (restaurant sales)
Auth:       Owner login (email + password)
Data model: Sale(id, receipt_no, sold_at, total, payment_method)
            SaleItem(id, sale_id -> Sale, dish_name, quantity, price)
Features:   - Import daily sales exported from the POS as CSV
            - Show revenue per day, week and month
            - Rank dishes by quantity and revenue
            - Show a heatmap of sales by weekday and hour
            - Compare this week with last week
Input:      Daily CSV export from the till system
Storage:    PostgreSQL
Tech stack: Python, Streamlit, pandas, Plotly
```

---

## Example 40

**Intent:**
cleaning company: customers book a home clean, pick hours, and we assign a cleaner

**Spec:**
```
Type:       Web application (service booking)
Auth:       Customer, cleaner and admin login (email + password)
Data model: Customer(id, name, email, phone, address, postcode)
            Cleaner(id, name, phone, postcodes_covered)
            Job(id, customer_id -> Customer, cleaner_id -> Cleaner, date, start_time, hours, extras, price, status)
Features:   - Book a clean by choosing date, hours and extras
            - Check the postcode is inside the service area
            - Assign a cleaner who covers the area and is free
            - Show cleaners their jobs for the week
            - Charge the card after the job is completed
API:        REST
            GET  /coverage?postcode={code}
            POST /jobs
            PATCH /jobs/{id}/assign
            GET  /cleaners/me/jobs
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe, Vue.js
```

---

## Example 41

**Intent:**
volunteers sign up for food bank shifts n coordinator sees gaps

**Spec:**
```
Type:       Web application (volunteer scheduling)
Auth:       Volunteer and coordinator login (email + password)
Data model: Volunteer(id, name, email, phone, skills)
            Shift(id, date, start_time, end_time, role, slots_needed)
            Signup(id, shift_id -> Shift, volunteer_id -> Volunteer, status)
Features:   - Show upcoming shifts with open spots
            - Sign up for and drop out of shifts
            - Highlight shifts that are under-staffed
            - Email volunteers a reminder the day before
            - Track total volunteer hours per person
API:        REST
            GET  /shifts?from={date}
            POST /shifts/{id}/signup
            DELETE /signups/{id}
            GET  /reports/gaps
Storage:    PostgreSQL
Tech stack: Python, Flask, Bootstrap, SendGrid
```

---

## Example 42

**Intent:**
I'm a personal trainer with like 20 clients and I keep losing track of who paid for how many sessions, who has sessions left, when their packages expire. would be nice if clients could see it too

**Spec:**
```
Type:       Web application (client management)
Auth:       Trainer login; client login by email magic link
Data model: Client(id, name, email, phone, goals)
            Package(id, client_id -> Client, sessions_total, sessions_used, price, paid, expires_on)
            Session(id, client_id -> Client, package_id -> Package, date, notes)
Features:   - Sell session packages and record payments
            - Log each session against the client's package
            - Show sessions left and expiry date per client
            - Warn the trainer about packages expiring soon
            - Let clients view their own balance and session history
API:        REST
            GET  /clients
            POST /clients/{id}/packages
            POST /sessions
            GET  /me/packages
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Supabase
```

---

## Example 43

**Intent:**
property management, rent tracking for my 6 houses

**Spec:**
```
Type:       Web application (rent tracking)
Auth:       Landlord login (email + password)
Data model: Property(id, address, purchase_price)
            Tenancy(id, property_id -> Property, tenant_name, tenant_email, rent_amount, due_day, start_date, end_date)
            Payment(id, tenancy_id -> Tenancy, amount, paid_on, method)
            Expense(id, property_id -> Property, category, amount, date)
Features:   - Record rent payments against each tenancy
            - Flag late rent after the due day
            - Email tenants a rent reminder 3 days before due
            - Record repair and insurance expenses per property
            - Show yearly income and expenses for tax returns
API:        REST
            GET  /tenancies?status=late
            POST /payments
            POST /expenses
            GET  /reports/yearly?year={year}
Storage:    SQLite
Tech stack: Python, Django, Bootstrap
```

---

## Example 44

**Intent:**
something with react and firebase where my massage clients book and I approve each request myself

**Spec:**
```
Type:       Web application (booking requests)
Auth:       Firebase Authentication (clients with Google or email; therapist admin role)
Data model: Client(id, name, email, phone, health_notes)
            Treatment(id, name, duration_min, price)
            Request(id, client_id -> Client, treatment_id -> Treatment, requested_start, status, therapist_note)
Features:   - Request a treatment at a preferred time
            - Approve, decline or propose a new time
            - Notify the client by email when the request changes
            - Show approved sessions on a calendar
            - Store a short health questionnaire per client
Storage:    Cloud Firestore
Tech stack: React, Firebase Authentication, Cloud Firestore, Cloud Functions
```

---

## Example 45

**Intent:**
fix shop that repairs laptops wants a parts inventory linked to jobs so we know what we used

**Spec:**
```
Type:       Web application (repair shop management)
Auth:       Technician login (email + password)
Data model: Part(id, name, part_number, compatible_models, quantity, cost)
            RepairJob(id, customer_name, phone, device, fault, status, labour_cost)
            JobPart(id, job_id -> RepairJob, part_id -> Part, quantity)
Features:   - Create repair jobs with device and fault details
            - Reserve parts from stock for a job
            - Reduce stock when a job is completed
            - Calculate the job total from parts and labour
            - List parts that need reordering
API:        REST
            POST /jobs
            POST /jobs/{id}/parts
            POST /jobs/{id}/complete
            GET  /parts?low_stock=true
Storage:    MySQL
Tech stack: Java, Spring Boot, Thymeleaf
```

---

## Example 46

**Intent:**
online form so new patients fill their medical history before the first visit

**Spec:**
```
Type:       Web application (patient intake)
Auth:       Patients open a one-time secure link; staff login with 2FA
Data model: Patient(id, name, date_of_birth, email)
            IntakeForm(id, patient_id -> Patient, medications, allergies, conditions, submitted_at)
            Invite(id, patient_id -> Patient, token_hash, expires_at)
Features:   - Send a secure intake link before the first appointment
            - Fill in medical history, medications and allergies
            - Save progress and continue later
            - Show submitted forms to staff in the patient record
            - Expire links after 7 days
API:        REST
            POST /invites
            GET  /intake?token={token}
            POST /intake
            GET  /patients/{id}/intake
Storage:    PostgreSQL (encrypted fields)
Tech stack: Python, FastAPI, React, AWS KMS
```

---

## Example 47

**Intent:**
football club wants to collect yearly fees from parents of the youth players and know who hasnt paid

**Spec:**
```
Type:       Web application (club membership)
Auth:       Parent login (email + password); treasurer admin login
Data model: Team(id, name, age_group, coach)
            Player(id, name, birth_date, team_id -> Team)
            Parent(id, name, email, phone)
            Fee(id, player_id -> Player, season, amount, paid_at, method)
Features:   - Register players and link them to parents
            - Pay the season fee online by card
            - Record cash payments manually
            - List unpaid players per team
            - Send reminder emails to parents with unpaid fees
API:        REST
            POST /players
            POST /fees/{id}/checkout
            GET  /teams/{id}/unpaid
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Stripe
```

---

## Example 48

**Intent:**
Driving school: students book lessons with an instructor, instructors set their availability and see where to pick students up.

**Spec:**
```
Type:       Web application (lesson booking)
Auth:       Student, instructor and admin login (email + password)
Data model: Instructor(id, name, car, transmission)
            Availability(id, instructor_id -> Instructor, starts_at, ends_at)
            Student(id, name, email, phone, licence_number, lessons_credit)
            Lesson(id, student_id -> Student, instructor_id -> Instructor, starts_at, pickup_address, status)
Features:   - Let instructors publish their available times
            - Book a lesson in an available slot with a pickup address
            - Show instructors their day's lessons on a map
            - Deduct pre-paid lesson credits
            - Track lessons completed per student
API:        REST
            GET  /instructors/{id}/availability
            POST /lessons
            GET  /instructors/me/lessons?date={date}
Storage:    PostgreSQL
Tech stack: TypeScript, Nuxt, Google Maps JavaScript API
```

---

## Example 49

**Intent:**
customer databse for accounting firm.. who we do taxes for + deadlines

**Spec:**
```
Type:       Web application (CRM)
Auth:       Staff login (email + password, 2FA)
Data model: Client(id, name, type, tax_id, email, assigned_to -> Staff)
            Staff(id, name, email)
            Engagement(id, client_id -> Client, service, tax_year, deadline, status)
            Document(id, client_id -> Client, name, url, uploaded_at)
Features:   - Keep client records with tax IDs and contacts
            - Track engagements by service and deadline
            - Show upcoming deadlines for each staff member
            - Upload client documents securely
            - Email clients a list of missing documents
API:        REST
            GET  /clients?q={text}
            GET  /engagements?due_before={date}
            POST /clients/{id}/documents
Storage:    PostgreSQL, S3 (documents, encrypted)
Tech stack: Python, Django, AWS S3
```

---

## Example 50

**Intent:**
escape room booking, groups of 2-6, one room per hour

**Spec:**
```
Type:       Web application (booking system)
Auth:       Admin login for staff; customers book as guests
Data model: Room(id, name, theme, min_players, max_players, duration_min)
            Slot(id, room_id -> Room, starts_at, is_blocked)
            Booking(id, slot_id -> Slot, lead_name, email, players, total, status)
Features:   - Show available slots for each room by date
            - Price the booking by number of players
            - Take full payment online at booking
            - Let staff block slots for maintenance
            - Record whether the team escaped and their time
API:        REST
            GET  /rooms/{id}/slots?date={date}
            POST /bookings
            PATCH /bookings/{id}/result
Storage:    PostgreSQL
Tech stack: Node.js, Express, Svelte, Stripe
```

---

## Example 51

**Intent:**
piano teacher here, I want parents to book lessons and get invoiced every month automatically

**Spec:**
```
Type:       Web application (lesson scheduling)
Auth:       Teacher login; parent login (email + password)
Data model: Parent(id, name, email)
            Student(id, parent_id -> Parent, name, level)
            Lesson(id, student_id -> Student, starts_at, duration_min, rate, status)
            Invoice(id, parent_id -> Parent, month, total, status)
Features:   - Set up weekly recurring lesson slots per student
            - Let parents cancel lessons with 24 hours notice
            - Generate a monthly invoice from attended lessons
            - Email invoices with a card payment link
            - Show unpaid invoices to the teacher
API:        REST
            GET  /lessons?month={month}
            POST /lessons/{id}/cancel
            POST /invoices/generate?month={month}
Storage:    PostgreSQL
Tech stack: Python, Django, Celery, Stripe Invoicing
```

---

## Example 52

**Intent:**
florist orders for weddings, track every bouquet and table arrangement per wedding

**Spec:**
```
Type:       Web application (event order management)
Auth:       Florist staff login (email + password)
Data model: Wedding(id, couple_names, date, venue, contact_email, budget)
            Arrangement(id, wedding_id -> Wedding, type, quantity, flowers, colour_scheme, price)
            FlowerOrder(id, supplier, flower, stems, needed_by)
Features:   - Create a wedding with venue, date and budget
            - Add arrangements with flowers and quantities
            - Calculate total stems needed per flower across all weddings in a week
            - Generate a proposal PDF for the couple
            - Show upcoming weddings on a calendar
API:        REST
            POST /weddings
            POST /weddings/{id}/arrangements
            GET  /stems?week={date}
            GET  /weddings/{id}/proposal.pdf
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Prawn (PDF), FullCalendar
```

---

## Example 53

**Intent:**
We are a plumbing company with 8 vans. The office takes calls and needs to send jobs to the plumbers and see where everybody is in the day.

**Spec:**
```
Type:       Web application (field service dispatch)
Auth:       Dispatcher and plumber login (email + password)
Data model: Plumber(id, name, phone, van_reg)
            Customer(id, name, address, latitude, longitude, phone)
            Job(id, customer_id -> Customer, plumber_id -> Plumber, description, priority, scheduled_for, status)
            LocationPing(id, plumber_id -> Plumber, latitude, longitude, recorded_at)
Features:   - Create jobs from phone calls with priority levels
            - Assign jobs to plumbers on a drag-and-drop day board
            - Show plumbers' live locations on a map
            - Let plumbers update job status from their phone
            - Capture a customer signature when the job is done
API:        REST + WebSocket
            POST /jobs
            PATCH /jobs/{id}/assign
            POST /plumbers/me/location
            WS   /dispatch/live
Storage:    PostgreSQL with PostGIS
Tech stack: TypeScript, NestJS, React, Leaflet
```

---

## Example 54

**Intent:**
tool rental shop, ppl rent drills ladders etc by the day. need to know whats out and whats late

**Spec:**
```
Type:       Web application (equipment rental)
Auth:       Staff login (email + password)
Data model: Equipment(id, name, category, serial_no, daily_rate, deposit, status)
            Customer(id, name, phone, id_document_no)
            Rental(id, equipment_id -> Equipment, customer_id -> Customer, out_at, due_back, returned_at, condition_notes)
Features:   - Check equipment out to a customer with a deposit
            - Show all items currently rented and their due dates
            - Highlight late returns and calculate late fees
            - Record condition on return
            - Show utilisation per item to decide what to buy
API:        REST
            POST /rentals
            POST /rentals/{id}/return
            GET  /rentals?status=late
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 55

**Intent:**
venue hire for our village hall

**Spec:**
```
Type:       Web application (venue booking)
Auth:       Committee admin login; hirers book with email verification
Data model: Room(id, name, capacity, hourly_rate)
            Hirer(id, name, email, phone, organisation)
            HireBooking(id, room_id -> Room, hirer_id -> Hirer, starts_at, ends_at, purpose, status, total)
Features:   - Show a public calendar of booked and free times
            - Request a booking with purpose and expected numbers
            - Approve or decline requests as the booking secretary
            - Email an invoice once a booking is approved
            - Support weekly repeat bookings for regular groups
API:        REST
            GET  /calendar?month={month}
            POST /bookings
            POST /bookings/{id}/approve
Storage:    SQLite
Tech stack: PHP, Laravel, FullCalendar
```

---

## Example 56

**Intent:**
nursery waiting list. parents put their baby on the list with start date, we offer places when free

**Spec:**
```
Type:       Web application (waiting list)
Auth:       Parent login (email + password); manager login
Data model: Child(id, name, birth_date, desired_start, days_per_week)
            Parent(id, name, email, phone)
            WaitlistEntry(id, child_id -> Child, parent_id -> Parent, joined_at, priority, status)
            Offer(id, entry_id -> WaitlistEntry, room, start_date, expires_at, response)
Features:   - Join the waiting list with desired start date and days
            - Rank entries by sibling priority and join date
            - Send place offers that expire after 5 days
            - Let parents accept or decline an offer online
            - Show expected free places per room by month
API:        REST
            POST /waitlist
            GET  /admin/waitlist?room={room}
            POST /offers
            POST /offers/{id}/respond
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 57

**Intent:**
expense claims thing for team of 25 - upload receipts, manager approves, finance pays monthly

**Spec:**
```
Type:       Web application (expense management)
Auth:       Employee login via Google Workspace SSO; roles: employee, manager, finance
Data model: Employee(id, name, email, manager_id -> Employee, bank_iban)
            Claim(id, employee_id -> Employee, month, status, total)
            ClaimItem(id, claim_id -> Claim, date, category, amount, currency, receipt_url)
Features:   - Upload receipt photos and add expense lines
            - Read amount and date from receipts with OCR
            - Approve or reject claims as the manager
            - Export approved claims for the monthly payment run
            - Convert foreign currency amounts to EUR
API:        REST
            POST /claims
            POST /claims/{id}/items
            POST /claims/{id}/approve
            GET  /finance/export?month={month}
Storage:    PostgreSQL, Google Cloud Storage (receipts)
Tech stack: Go, React, Google Cloud Vision API
```

---

## Example 58

**Intent:**
keep trak of company laptops phones and who has em

**Spec:**
```
Type:       Web application (IT asset tracking)
Auth:       IT admin login (Microsoft Entra ID SSO)
Data model: Asset(id, type, model, serial_no, purchase_date, warranty_until, status)
            Employee(id, name, email, department)
            Assignment(id, asset_id -> Asset, employee_id -> Employee, assigned_at, returned_at)
Features:   - Register assets with serial numbers and warranty dates
            - Assign and unassign assets to employees
            - Show all equipment held by a leaving employee
            - Warn before warranties expire
            - Print asset labels with QR codes
API:        REST
            GET  /assets?status=in_use
            POST /assignments
            GET  /employees/{id}/assets
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core MVC, QRCoder
```

---

## Example 59

**Intent:**
i have a pharmacy and want patients to request repeat prescription refills on website and we text them when ready

**Spec:**
```
Type:       Web application (prescription refills)
Auth:       Patient login (email + password, date of birth check); pharmacist login with 2FA
Data model: Patient(id, name, date_of_birth, phone, email)
            Medication(id, patient_id -> Patient, name, dose, repeats_left)
            RefillRequest(id, medication_id -> Medication, requested_at, status, ready_at)
Features:   - Show a patient's repeat medications
            - Request a refill with one click
            - Queue requests for pharmacist review
            - Text the patient when the refill is ready to collect
            - Block requests when no repeats are left
API:        REST
            GET  /me/medications
            POST /refills
            PATCH /refills/{id}/status
Storage:    PostgreSQL (encrypted at rest)
Tech stack: Java, Spring Boot, Angular, Twilio
```

---

## Example 60

**Intent:**
We sell coffee beans from our roastery and want a monthly subscription where customers choose grind and how many bags.

**Spec:**
```
Type:       Web application (subscriptions)
Auth:       Customer login (email + password)
Data model: Customer(id, name, email, shipping_address)
            Coffee(id, name, origin, roast_level, price_per_bag)
            Subscription(id, customer_id -> Customer, coffee_id -> Coffee, grind, bags, frequency, next_ship_date, status)
            Shipment(id, subscription_id -> Subscription, shipped_on, tracking_no)
Features:   - Choose coffee, grind, bag count and delivery frequency
            - Bill subscriptions automatically by card
            - Pause, skip or cancel a delivery
            - Show a roasting list of bags needed this week
            - Email tracking numbers when orders ship
API:        REST
            POST /subscriptions
            PATCH /subscriptions/{id}
            GET  /admin/roast-list?week={date}
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe Billing
```

---

## Example 61

**Intent:**
chiropractor needs treatment notes and appointment history per patient

**Spec:**
```
Type:       Web application (clinic records)
Auth:       Practitioner login with 2FA
Data model: Patient(id, name, date_of_birth, phone, email)
            Visit(id, patient_id -> Patient, date, subjective, objective, assessment, plan)
            Attachment(id, visit_id -> Visit, file_url, kind)
Features:   - Write SOAP notes for each visit
            - Show a timeline of past visits per patient
            - Upload X-ray images to a visit
            - Copy the previous visit's plan as a starting point
            - Lock notes 24 hours after signing
API:        REST
            GET  /patients/{id}/visits
            POST /patients/{id}/visits
            POST /visits/{id}/attachments
Storage:    PostgreSQL, S3 (encrypted attachments)
Tech stack: TypeScript, Next.js, Prisma, AWS S3
```

---

## Example 62

**Intent:**
dog kennel booking for holidays, owners pick dates and we check we have free kennels

**Spec:**
```
Type:       Web application (boarding reservations)
Auth:       Owner login (email + password); staff login
Data model: Owner(id, name, email, phone, emergency_contact)
            Dog(id, owner_id -> Owner, name, breed, vaccinated_until, feeding_notes)
            Kennel(id, number, size)
            Stay(id, dog_id -> Dog, kennel_id -> Kennel, check_in, check_out, status, price)
Features:   - Request a stay for one or more dogs and dates
            - Check kennel availability by size for the whole stay
            - Refuse stays when vaccinations expire before check-out
            - Show staff daily feeding and medication notes
            - Calculate price by nights and dog size
API:        REST
            GET  /availability?from={date}&to={date}&size={size}
            POST /stays
            GET  /staff/daily?date={date}
Storage:    PostgreSQL
Tech stack: Python, Flask, Jinja2, Bootstrap
```

---

## Example 63

**Intent:**
karate school wants to track belts and gradings for each student

**Spec:**
```
Type:       Web application (student progress)
Auth:       Instructor login (email + password)
Data model: Student(id, name, birth_date, current_belt, joined_on)
            Belt(id, name, order, min_months)
            Grading(id, date, location)
            GradingResult(id, grading_id -> Grading, student_id -> Student, belt_id -> Belt, passed, notes)
            Attendance(id, student_id -> Student, class_date)
Features:   - Record class attendance per student
            - Show which students are eligible for their next grading
            - Record grading results and update belts
            - Print certificates for passed gradings
            - Show each student's belt history
API:        REST
            GET  /students/eligible
            POST /gradings/{id}/results
            POST /attendance
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 64

**Intent:**
photo studio: clients book a shoot, then later they get a private online gallery and choose which photos they want to buy

**Spec:**
```
Type:       Web application (booking and client galleries)
Auth:       Photographer admin login; clients access galleries with a private link + password
Data model: Client(id, name, email)
            Shoot(id, client_id -> Client, package, starts_at, location, status)
            Gallery(id, shoot_id -> Shoot, password_hash, expires_at)
            Photo(id, gallery_id -> Gallery, preview_url, original_url, selected)
            PhotoOrder(id, gallery_id -> Gallery, total, paid_at)
Features:   - Book a shoot package and date
            - Upload photos to a private client gallery
            - Show watermarked previews only
            - Let clients select photos and pay for extras
            - Unlock full-resolution downloads after payment
API:        REST
            POST /shoots
            POST /galleries/{id}/photos
            POST /galleries/{id}/select
            POST /galleries/{id}/checkout
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Express, Sharp (watermarks), Stripe
```

---

## Example 65

**Intent:**
print shop order intake, customers upload files and pick paper and quantity

**Spec:**
```
Type:       Web application (print orders)
Auth:       Customer login (email + password); staff login
Data model: Customer(id, name, email, company)
            Product(id, name, sizes, paper_options, base_price)
            PrintJob(id, customer_id -> Customer, product_id -> Product, size, paper, quantity, file_url, price, status)
Features:   - Configure a print product with size, paper and quantity
            - Show an instant price from a pricing table
            - Upload print-ready PDF files
            - Check uploaded PDFs for resolution and bleed
            - Track jobs through proofing, printing and ready
API:        REST
            GET  /products/{id}/price?size={s}&paper={p}&qty={n}
            POST /jobs
            POST /jobs/{id}/file
Storage:    PostgreSQL, S3 (artwork)
Tech stack: Python, Django, PyMuPDF, Vue.js
```

---

## Example 66

**Intent:**
Laundry pickup and delivery service: customers schedule a pickup, we weigh the bag and charge per kilo.

**Spec:**
```
Type:       Web application (on-demand service)
Auth:       Customer login (email + password); driver and staff logins
Data model: Customer(id, name, email, phone, address)
            PickupOrder(id, customer_id -> Customer, pickup_slot, delivery_slot, weight_kg, price, status)
            Driver(id, name, phone)
            Route(id, driver_id -> Driver, date, order_ids)
Features:   - Book a pickup and delivery time window
            - Record bag weight and calculate price per kilo
            - Charge the saved card after weighing
            - Group the day's pickups into routes per driver
            - Text customers when the driver is on the way
API:        REST
            POST /orders
            PATCH /orders/{id}/weight
            GET  /drivers/{id}/route?date={date}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe, Twilio, Google Maps API
```

---

## Example 67

**Intent:**
alterations tailor, track garments dropped off and when they will be ready

**Spec:**
```
Type:       Web application (order tracking)
Auth:       Shop staff login (PIN)
Data model: Customer(id, name, phone)
            Garment(id, customer_id -> Customer, type, alteration, price, ticket_no, ready_by, status)
Features:   - Create a ticket when a garment is dropped off
            - Print a numbered ticket for the customer
            - Show garments due today and tomorrow
            - Send an SMS when the garment is ready
            - Mark garments as collected and paid
API:        REST
            POST /garments
            GET  /garments?due={date}
            PATCH /garments/{id}/status
Storage:    SQLite
Tech stack: Python, Flask, Twilio
```

---

## Example 68

**Intent:**
we rent 30 cars, want online booking and see wich car is where

**Spec:**
```
Type:       Web application (car rental)
Auth:       Customer login (email + password, driving licence upload); staff login
Data model: Car(id, plate, model, category, location_id -> Location, mileage, status)
            Location(id, name, address)
            Customer(id, name, email, licence_no, licence_url)
            Rental(id, car_id -> Car, customer_id -> Customer, pickup_at, return_at, pickup_location_id -> Location, return_location_id -> Location, price, status)
Features:   - Search available cars by category, dates and location
            - Book and pay online with a security deposit hold
            - Verify the driving licence before pickup
            - Record mileage and damage at pickup and return
            - Show the fleet status per location
API:        REST
            GET  /cars/available?from={dt}&to={dt}&location={id}
            POST /rentals
            POST /rentals/{id}/checkout
            POST /rentals/{id}/return
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, React, Stripe
```

---

## Example 69

**Intent:**
camp site booking pitches tents caravans

**Spec:**
```
Type:       Web application (campsite booking)
Auth:       Owner admin login; guests book without an account
Data model: Pitch(id, number, type, has_electric, max_length_m)
            Booking(id, pitch_id -> Pitch, guest_name, email, arrival, departure, adults, children, vehicle_reg, total)
            Season(id, name, start_date, end_date, nightly_rate)
Features:   - Search free pitches by type, dates and electric hookup
            - Price stays by season, people and pitch type
            - Take a deposit at booking
            - Show an arrivals list for each day
            - Show a pitch map with occupancy
API:        REST
            GET  /pitches/available?arrival={date}&departure={date}&type={type}
            POST /bookings
            GET  /admin/arrivals?date={date}
Storage:    MySQL
Tech stack: PHP, WordPress plugin, Stripe
```

---

## Example 70

**Intent:**
Hi, we rent self storage units, different sizes. Customers should rent online and pay monthly, and we need to lock out people who don't pay.

**Spec:**
```
Type:       Web application (self storage rental)
Auth:       Customer login (email + password); manager login
Data model: Unit(id, number, size_sqft, monthly_price, status)
            Customer(id, name, email, phone, address)
            Lease(id, unit_id -> Unit, customer_id -> Customer, start_date, end_date, gate_code, status)
            Payment(id, lease_id -> Lease, amount, period, paid_at)
Features:   - Show free units by size with prices
            - Rent a unit online and set up monthly card payments
            - Generate a personal gate access code
            - Disable the gate code after 10 days of unpaid rent
            - Send overdue notices by email and SMS
API:        REST
            GET  /units?size={size}&status=free
            POST /leases
            POST /leases/{id}/suspend
            POST /webhooks/payments
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Angular, Stripe
```

---

## Example 71

**Intent:**
parking permits for residents in our apartment building, guards need to check plates

**Spec:**
```
Type:       Web application (parking permits)
Auth:       Resident login (email + password); guard login (PIN)
Data model: Apartment(id, number, building)
            Resident(id, apartment_id -> Apartment, name, email)
            Vehicle(id, resident_id -> Resident, plate, make, colour)
            Permit(id, vehicle_id -> Vehicle, type, valid_from, valid_to)
Features:   - Register up to two vehicles per apartment
            - Issue temporary visitor permits for 24 hours
            - Let guards look up a plate and see if it has a valid permit
            - Log violations with a photo
            - Notify residents when a permit is about to expire
API:        REST
            POST /vehicles
            POST /permits/visitor
            GET  /permits/check?plate={plate}
            POST /violations
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React (PWA)
```

---

## Example 72

**Intent:**
homeowners association website with dues payments and members voting on proposals

**Spec:**
```
Type:       Web application (HOA portal)
Auth:       Homeowner login (email + password); board admin role
Data model: Home(id, address, lot_number)
            Owner(id, home_id -> Home, name, email)
            Dues(id, home_id -> Home, period, amount, paid_at)
            Proposal(id, title, description, opens_at, closes_at)
            Vote(id, proposal_id -> Proposal, home_id -> Home, choice)
Features:   - Pay quarterly dues online
            - Show each home's payment history
            - Publish proposals with a voting window
            - Allow one vote per home on each proposal
            - Show results after voting closes
API:        REST
            POST /dues/{id}/pay
            GET  /proposals
            POST /proposals/{id}/votes
            GET  /proposals/{id}/results
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma, Stripe
```

---

## Example 73

**Intent:**
scouts group needs to track kids badges, camps and permission slips

**Spec:**
```
Type:       Web application (youth group management)
Auth:       Leader login (email + password); parent login
Data model: Scout(id, name, birth_date, section, parent_id -> Parent)
            Parent(id, name, email, phone)
            Badge(id, name, requirements)
            BadgeAward(id, scout_id -> Scout, badge_id -> Badge, awarded_on)
            Camp(id, name, start_date, end_date, cost)
            Permission(id, camp_id -> Camp, scout_id -> Scout, signed_by, signed_at, medical_notes)
Features:   - Record badges earned per scout
            - Create camps and invite scouts
            - Collect online permission slips with medical notes
            - List scouts still missing a signed permission
            - Show badge progress for each section
API:        REST
            POST /scouts/{id}/badges
            POST /camps/{id}/permissions
            GET  /camps/{id}/missing
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 74

**Intent:**
Our Sunday amateur basketball league needs fixtures, scores and a standings table online.

**Spec:**
```
Type:       Web application (sports league)
Auth:       League admin login; team captains log in to submit scores
Data model: Season(id, name, start_date)
            Team(id, season_id -> Season, name, captain_email)
            Fixture(id, season_id -> Season, home_team_id -> Team, away_team_id -> Team, tip_off, court)
            Result(id, fixture_id -> Fixture, home_points, away_points, confirmed)
Features:   - Generate a round-robin fixture list for the season
            - Let captains submit scores after each game
            - Confirm scores as an admin
            - Calculate the standings table with wins, losses and point difference
            - Show a public page of fixtures and standings
API:        REST
            POST /seasons/{id}/fixtures/generate
            POST /fixtures/{id}/result
            GET  /seasons/{id}/standings
Storage:    PostgreSQL
Tech stack: Node.js, Express, EJS templates
```

---

## Example 75

**Intent:**
golf club tee time booking

**Spec:**
```
Type:       Web application (tee time booking)
Auth:       Member login (membership number + password); pro shop staff login
Data model: Member(id, membership_no, name, handicap, email)
            TeeTime(id, course, starts_at, max_players, member_only)
            TeeBooking(id, tee_time_id -> TeeTime, member_id -> Member, guests)
Features:   - Show tee times every 10 minutes with spots left
            - Book up to 4 players including guests
            - Restrict weekend mornings to members only
            - Open bookings 7 days ahead at 7am
            - Let staff block times for competitions
API:        REST
            GET  /tee-times?date={date}
            POST /tee-times/{id}/book
            DELETE /bookings/{id}
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Razor Pages
```

---

## Example 76

**Intent:**
kids party bookings for our soft play centre, they pick a package and food

**Spec:**
```
Type:       Web application (party booking)
Auth:       Admin login for staff; parents book as guests
Data model: PartyPackage(id, name, price_per_child, min_children, duration_min)
            FoodOption(id, name, price_per_child, allergens)
            PartySlot(id, room, starts_at)
            PartyBooking(id, slot_id -> PartySlot, package_id -> PartyPackage, food_option_id -> FoodOption, child_name, child_age, children_count, parent_email, deposit_paid)
Features:   - Show free party slots by date and room
            - Pick a package and food menu per child
            - Pay a deposit online, balance on the day
            - Collect allergy information before the party
            - Send the kitchen a food order list for each day
API:        REST
            GET  /slots?date={date}
            POST /party-bookings
            GET  /kitchen/orders?date={date}
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 77

**Intent:**
veg box scheme for our farm. members subscribe weekly and choose small or large box, can skip weeks

**Spec:**
```
Type:       Web application (subscriptions)
Auth:       Member login (email + password); farm admin login
Data model: Member(id, name, email, address, delivery_zone)
            BoxSize(id, name, weekly_price)
            Subscription(id, member_id -> Member, box_size_id -> BoxSize, start_date, status)
            Skip(id, subscription_id -> Subscription, week_start)
            WeekContent(id, week_start, items)
Features:   - Subscribe to a weekly box of a chosen size
            - Skip weeks up to Monday midnight before delivery
            - Charge cards weekly for active, non-skipped boxes
            - Publish what is in this week's box
            - Produce a packing and delivery list per zone
API:        REST
            POST /subscriptions
            POST /subscriptions/{id}/skips
            GET  /admin/packing?week={date}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe, Sidekiq
```

---

## Example 78

**Intent:**
butcher christmas preorders turkey and hams with pickup day

**Spec:**
```
Type:       Web application (seasonal preorders)
Auth:       Shop admin login; customers order as guests
Data model: Product(id, name, weight_options, price_per_kg, stock_limit)
            PickupDay(id, date, capacity)
            Preorder(id, customer_name, phone, email, pickup_day_id -> PickupDay, deposit_paid, status)
            PreorderItem(id, preorder_id -> Preorder, product_id -> Product, weight_kg)
Features:   - Show Christmas products with weight options
            - Stop orders when a product's stock limit is reached
            - Choose a pickup day with remaining capacity
            - Take a deposit by card
            - Print a pickup list with weights per day
API:        REST
            GET  /products
            POST /preorders
            GET  /admin/pickups?date={date}
Storage:    SQLite
Tech stack: Python, Flask, Stripe Checkout
```

---

## Example 79

**Intent:**
I own a takeaway pizza place and the apps take 30% so I want my own ordering site with delivery and collection, customers track the order.

**Spec:**
```
Type:       Web application (online ordering)
Auth:       Customer login (optional, email + password); staff login
Data model: MenuItem(id, name, category, price, sizes, toppings)
            Customer(id, name, email, phone, address)
            Order(id, customer_id -> Customer, type, address, total, status, created_at, eta)
            OrderLine(id, order_id -> Order, menu_item_id -> MenuItem, size, extras, quantity)
Features:   - Build pizzas with size and extra toppings
            - Choose delivery or collection and check delivery postcode
            - Pay online by card or Apple Pay
            - Show orders on a kitchen screen
            - Let customers track status from received to out for delivery
API:        REST + WebSocket
            GET  /menu
            POST /orders
            PATCH /orders/{id}/status
            WS   /orders/{id}/track
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe, Socket.IO
```

---

## Example 80

**Intent:**
recipe costing for my cafe so i know the margin on each menu item when ingredient prices change

**Spec:**
```
Type:       Web application (recipe costing)
Auth:       Owner login (email + password)
Data model: Ingredient(id, name, unit, price_per_unit, supplier, updated_at)
            Recipe(id, name, sell_price, portions)
            RecipeLine(id, recipe_id -> Recipe, ingredient_id -> Ingredient, quantity)
Features:   - Enter ingredients with supplier prices
            - Build recipes from ingredient quantities
            - Calculate cost per portion and gross margin
            - Recalculate all margins when an ingredient price changes
            - Highlight menu items with margin below 60%
API:        REST
            PUT  /ingredients/{id}
            POST /recipes
            GET  /recipes?margin_below={pct}
Storage:    SQLite
Tech stack: Python, FastAPI, Svelte
```

---

## Example 81

**Intent:**
bar stock take every week, count bottles and see what was used vs sold

**Spec:**
```
Type:       Web application (stock take)
Auth:       Bar manager login (email + password)
Data model: Product(id, name, category, bottle_ml, cost)
            StockCount(id, counted_on, counted_by)
            CountLine(id, count_id -> StockCount, product_id -> Product, full_bottles, partial_fraction)
            Delivery(id, product_id -> Product, bottles, received_on)
            PosSale(id, product_id -> Product, ml_sold, sold_on)
Features:   - Enter weekly counts on a tablet including partial bottles
            - Add deliveries received during the week
            - Calculate usage from opening count, deliveries and closing count
            - Compare usage to POS sales and show variance per product
            - Flag products with variance above 5%
API:        REST
            POST /counts
            POST /deliveries
            GET  /variance?week={date}
Storage:    PostgreSQL
Tech stack: Python, Django, pandas
```

---

## Example 82

**Intent:**
Housekeeping app for our hotel: the head housekeeper assigns rooms to cleaners every morning and sees which rooms are done.

**Spec:**
```
Type:       Web application (housekeeping management)
Auth:       Head housekeeper and staff login (username + PIN)
Data model: Room(id, number, floor, type, status)
            Housekeeper(id, name)
            CleaningTask(id, room_id -> Room, housekeeper_id -> Housekeeper, date, task_type, status, finished_at)
            Issue(id, room_id -> Room, description, photo_url, created_at)
Features:   - Assign departure and stayover rooms to housekeepers
            - Let staff mark rooms clean from their phone
            - Show a live board of room statuses by floor
            - Report maintenance issues with a photo
            - Show average cleaning time per room type
API:        REST + WebSocket
            POST /tasks/assign
            PATCH /tasks/{id}/status
            POST /rooms/{id}/issues
            WS   /rooms/live
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Vue.js, Socket.IO
```

---

## Example 83

**Intent:**
maintenance work orders for our factory machines, operators report breakdowns, techs fix them

**Spec:**
```
Type:       Web application (maintenance management)
Auth:       Operator, technician and supervisor login (Active Directory)
Data model: Machine(id, name, line, model, install_date)
            WorkOrder(id, machine_id -> Machine, reported_by, description, priority, status, opened_at, closed_at)
            WorkLog(id, work_order_id -> WorkOrder, technician, minutes, action_taken, parts_used)
            PreventiveTask(id, machine_id -> Machine, task, interval_days, next_due)
Features:   - Report a breakdown from a shop-floor terminal
            - Assign work orders to technicians by priority
            - Log time and parts used on each order
            - Generate preventive maintenance orders when due
            - Show downtime and mean time to repair per machine
API:        REST
            POST /work-orders
            POST /work-orders/{id}/logs
            GET  /machines/{id}/downtime
Storage:    SQL Server
Tech stack: C#, ASP.NET Core, Blazor Server, LDAP
```

---

## Example 84

**Intent:**
security guard company, guards scan checkpoints during patrol and office sees missed ones

**Spec:**
```
Type:       Web application (guard tour tracking)
Auth:       Guard login (ID + PIN); supervisor login
Data model: Site(id, name, address)
            Checkpoint(id, site_id -> Site, name, nfc_tag_id)
            Patrol(id, site_id -> Site, guard_id -> Guard, started_at, ended_at)
            Scan(id, patrol_id -> Patrol, checkpoint_id -> Checkpoint, scanned_at)
            Guard(id, name, phone)
Features:   - Scan NFC or QR checkpoints from the guard's phone
            - Define patrol routes and required checkpoint times
            - Alert the supervisor when a checkpoint is missed
            - Report incidents with photos during a patrol
            - Send a daily patrol report per site to the client
API:        REST
            POST /patrols
            POST /patrols/{id}/scans
            GET  /sites/{id}/missed?date={date}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React (PWA, Web NFC)
```

---

## Example 85

**Intent:**
daily site reports for my small construction company, foreman fills it in on phone with weather workers and photos

**Spec:**
```
Type:       Web application (construction site reports)
Auth:       Foreman and office login (email + password)
Data model: Project(id, name, address, client)
            DailyReport(id, project_id -> Project, date, weather, workers_on_site, work_done, delays, author_id -> User)
            ReportPhoto(id, report_id -> DailyReport, url, caption)
            User(id, name, email, role)
Features:   - Fill in a daily report from a phone
            - Fetch the day's weather automatically for the site
            - Attach photos with captions
            - Email a PDF of the report to the client
            - Search reports by project and date
API:        REST
            POST /projects/{id}/reports
            POST /reports/{id}/photos
            GET  /reports/{id}/pdf
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Open-Meteo API, WeasyPrint
```

---

## Example 86

**Intent:**
gift vouchers for my spa, people buy online and we redeem in the spa

**Spec:**
```
Type:       Web application (gift vouchers)
Auth:       Spa staff login; buyers check out as guests
Data model: Voucher(id, code, amount, balance, recipient_name, message, expires_at)
            VoucherOrder(id, buyer_email, voucher_id -> Voucher, paid_at)
            Redemption(id, voucher_id -> Voucher, amount, redeemed_at, staff_id -> Staff)
            Staff(id, name, pin_hash)
Features:   - Buy a voucher for a set amount or treatment
            - Email a printable voucher with a unique code
            - Check a code's balance at the reception
            - Redeem the full or partial amount
            - Expire vouchers after 12 months
API:        REST
            POST /vouchers/checkout
            GET  /vouchers/{code}
            POST /vouchers/{code}/redeem
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Stripe
```

---

## Example 87

**Intent:**
tutoring centre: enrol students in courses, each course has sessions and a teacher, parents pay per term

**Spec:**
```
Type:       Web application (course enrolment)
Auth:       Parent, teacher and admin login (email + password)
Data model: Course(id, subject, level, teacher_id -> Teacher, term, fee, capacity)
            Teacher(id, name, email)
            Student(id, name, school_year, parent_id -> Parent)
            Parent(id, name, email, phone)
            Enrolment(id, course_id -> Course, student_id -> Student, paid, status)
Features:   - Browse courses for the term by subject and level
            - Enrol a student while places remain
            - Pay term fees online
            - Show teachers their class lists
            - Send term-start emails with timetables
API:        REST
            GET  /courses?term={term}
            POST /enrolments
            GET  /teachers/me/classes
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, Stripe
```

---

## Example 88

**Intent:**
parents evening booking, parents choose 5 min slots with each teacher of their child

**Spec:**
```
Type:       Web application (meeting scheduler)
Auth:       Parent login with child's student ID + date of birth; teacher login
Data model: Teacher(id, name, room)
            Student(id, name, class_id)
            StudentTeacher(student_id -> Student, teacher_id -> Teacher)
            MeetingSlot(id, teacher_id -> Teacher, starts_at, booked_by_student_id -> Student)
Features:   - Generate 5-minute slots for each teacher for the evening
            - Show parents only the teachers of their child
            - Prevent double-booking the same time across teachers
            - Show each teacher their appointment list
            - Email parents their personal schedule
API:        REST
            GET  /students/{id}/teachers/slots
            POST /slots/{id}/book
            GET  /teachers/me/schedule
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 89

**Intent:**
school trips, collect consent and payment from parents online

**Spec:**
```
Type:       Web application (school trips)
Auth:       Parent login (email + password); school staff login
Data model: Trip(id, name, date, cost, deadline, class_ids)
            Student(id, name, class_id)
            Parent(id, name, email)
            TripResponse(id, trip_id -> Trip, student_id -> Student, consent, medical_notes, paid_amount, responded_at)
Features:   - Create a trip and invite selected classes
            - Collect consent and medical notes online
            - Accept full payment or instalments
            - Remind parents who have not responded by the deadline
            - Export the final list of students going
API:        REST
            POST /trips
            POST /trips/{id}/responses
            GET  /trips/{id}/outstanding
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe, Postmark
```

---

## Example 90

**Intent:**
I sell school uniforms for 4 local schools and want parents to order online by school and size, and collect in shop

**Spec:**
```
Type:       Web application (online shop)
Auth:       Customer login (optional); shop admin login
Data model: School(id, name, logo_url)
            Item(id, school_id -> School, name, price)
            ItemSize(id, item_id -> Item, size, stock)
            Order(id, customer_email, school_id -> School, total, status, ready_at)
            OrderLine(id, order_id -> Order, item_size_id -> ItemSize, quantity)
Features:   - Browse items filtered by school
            - Order items with sizes and pay online
            - Reserve stock and email when ready to collect
            - Show back-order items when a size is out of stock
            - Report best-selling sizes before the new school year
API:        REST
            GET  /schools/{id}/items
            POST /orders
            PATCH /orders/{id}/ready
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Stripe, Prisma
```

---

## Example 91

**Intent:**
sales commission for salon staff, they get % of services and products sold

**Spec:**
```
Type:       Web application (commission tracking)
Auth:       Owner login; staff login to view their own earnings
Data model: Staff(id, name, service_rate_pct, product_rate_pct)
            Sale(id, staff_id -> Staff, type, description, amount, sold_at)
            PayPeriod(id, start_date, end_date, closed)
Features:   - Record service and product sales per staff member
            - Calculate commission with separate rates for services and products
            - Show each stylist their earnings for the pay period
            - Close a pay period and export it for payroll
            - Rank staff by sales
API:        REST
            POST /sales
            GET  /staff/{id}/commission?period={id}
            POST /periods/{id}/close
Storage:    SQLite
Tech stack: Python, Flask, Chart.js
```

---

## Example 92

**Intent:**
museum membership card, members get free entry and discount in the cafe

**Spec:**
```
Type:       Web application (membership)
Auth:       Member login (email + password); front desk login
Data model: Member(id, name, email, tier, card_number, expires_on)
            Tier(id, name, yearly_price, guest_passes, cafe_discount_pct)
            Visit(id, member_id -> Member, visited_at, guests)
Features:   - Buy or renew a membership tier online
            - Show a digital membership card with a barcode
            - Scan cards at the front desk to admit members and guests
            - Send renewal reminders a month before expiry
            - Report visits and renewals per month
API:        REST
            POST /memberships/checkout
            GET  /members/me/card
            POST /visits
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, Vue.js, Apple Wallet passes
```

---

## Example 93

**Intent:**
Need lost and found register for our hotel front desk, so guests can claim items.

**Spec:**
```
Type:       Web application (lost and found)
Auth:       Front desk staff login
Data model: FoundItem(id, description, category, found_location, found_at, photo_url, status)
            Claim(id, item_id -> FoundItem, guest_name, room_number, contact, verified, claimed_at)
Features:   - Log found items with photo and location
            - Search items by category and date
            - Record a guest's claim and verification details
            - Mark items as shipped or collected
            - List unclaimed items older than 90 days for disposal
API:        REST
            POST /items
            GET  /items?category={c}
            POST /items/{id}/claims
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 94

**Intent:**
supplier ordering for a small restaurant group, 3 kitchens order from same suppliers

**Spec:**
```
Type:       Web application (purchasing)
Auth:       Chef and head office login (email + password)
Data model: Kitchen(id, name, address)
            Supplier(id, name, email, order_cutoff_time, delivery_days)
            SupplierProduct(id, supplier_id -> Supplier, name, unit, price)
            PurchaseOrder(id, kitchen_id -> Kitchen, supplier_id -> Supplier, delivery_date, status)
            PurchaseLine(id, order_id -> PurchaseOrder, product_id -> SupplierProduct, quantity)
Features:   - Build orders from each supplier's product list
            - Warn when an order misses the supplier's cut-off time
            - Email the order to the supplier as a PDF
            - Check off deliveries and note missing items
            - Compare spend per kitchen per week
API:        REST
            POST /orders
            POST /orders/{id}/send
            POST /orders/{id}/receive
            GET  /reports/spend?week={date}
Storage:    PostgreSQL
Tech stack: Python, Django, WeasyPrint
```

---

## Example 95

**Intent:**
appoinment for optician eye test and track when glasses are ready

**Spec:**
```
Type:       Web application (optician practice)
Auth:       Staff login; patients book with email confirmation
Data model: Patient(id, name, birth_date, email, phone)
            EyeTest(id, patient_id -> Patient, starts_at, optometrist, prescription_json)
            GlassesOrder(id, patient_id -> Patient, frame, lens_type, lab, ordered_at, ready_at, status)
Features:   - Book an eye test online
            - Store the prescription from each test
            - Track glasses orders sent to the lab
            - Text the patient when glasses are ready to collect
            - Remind patients when their next test is due after 2 years
API:        REST
            POST /eye-tests
            POST /glasses-orders
            PATCH /glasses-orders/{id}
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Twilio
```

---

## Example 96

**Intent:**
swim school with levels, kids move up when teacher marks skills done

**Spec:**
```
Type:       Web application (swim school)
Auth:       Teacher and parent login (email + password)
Data model: Level(id, name, order)
            Skill(id, level_id -> Level, description)
            Swimmer(id, name, birth_date, level_id -> Level, parent_id -> Parent)
            SkillCheck(id, swimmer_id -> Swimmer, skill_id -> Skill, achieved_on, teacher)
            Parent(id, name, email)
Features:   - Tick off skills for each swimmer during lessons
            - Move a swimmer up when all level skills are achieved
            - Show parents their child's progress
            - Suggest a class at the new level with free places
            - Print level certificates
API:        REST
            POST /swimmers/{id}/skills
            GET  /swimmers/{id}/progress
            POST /swimmers/{id}/promote
Storage:    PostgreSQL
Tech stack: TypeScript, SvelteKit, Prisma
```

---

## Example 97

**Intent:**
dance school recital: assign costumes to students, track sizes, who paid the costume fee

**Spec:**
```
Type:       Web application (recital management)
Auth:       Admin login for the studio
Data model: Student(id, name, age, class_id -> DanceClass)
            DanceClass(id, name, teacher)
            Costume(id, class_id -> DanceClass, name, fee, supplier)
            CostumeOrder(id, student_id -> Student, costume_id -> Costume, size, paid, received)
Features:   - Record measurements and sizes per student
            - Assign a costume to each class
            - Create a supplier order with sizes and quantities
            - Track costume fee payments
            - Mark costumes as received and handed out
API:        REST
            POST /costume-orders
            GET  /costumes/{id}/supplier-order
            PATCH /costume-orders/{id}
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 98

**Intent:**
boat rental by the hour at our lake, people book online and we see the fleet schedule

**Spec:**
```
Type:       Web application (boat rental)
Auth:       Staff login; customers book as guests
Data model: Boat(id, name, type, seats, hourly_rate, status)
            Rental(id, boat_id -> Boat, customer_name, phone, starts_at, hours, life_jackets, paid)
            WeatherClosure(id, date, reason)
Features:   - Book a boat by type and hour
            - Show a timeline of the whole fleet for the day
            - Close bookings for a day because of weather and notify customers
            - Record boat out and back times
            - Refund bookings cancelled by weather
API:        REST
            GET  /boats/availability?date={date}
            POST /rentals
            POST /closures
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js, Stripe
```

---

## Example 99

**Intent:**
timesheets for a staffing agency, temps submit hours, client signs off, we invoice the client and pay the temp

**Spec:**
```
Type:       Web application (agency timesheets)
Auth:       Temp, client approver and agency admin login (email + password)
Data model: Temp(id, name, email, pay_rate)
            ClientCompany(id, name, approver_email, charge_rate)
            Placement(id, temp_id -> Temp, client_id -> ClientCompany, start_date, end_date)
            Timesheet(id, placement_id -> Placement, week_start, hours, status, approved_at)
Features:   - Submit weekly hours for a placement
            - Send timesheets to the client for approval
            - Generate client invoices from approved timesheets
            - Export temp pay for payroll
            - Show margin per placement
API:        REST
            POST /timesheets
            POST /timesheets/{id}/approve
            POST /invoices/generate?week={date}
            GET  /payroll/export?week={date}
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, React
```

---

## Example 100

**Intent:**
bowling alley lane reservations

**Spec:**
```
Type:       Web application (lane booking)
Auth:       Staff login; customers book as guests
Data model: Lane(id, number, has_bumpers)
            LaneBooking(id, lane_id -> Lane, customer_name, phone, starts_at, games, players, shoe_sizes, paid)
Features:   - Show free lanes per hour for a date
            - Book one or more lanes for a number of games
            - Request bumpers for children
            - Record shoe sizes to prepare before arrival
            - Show the front desk a lane timeline
API:        REST
            GET  /lanes/availability?date={date}
            POST /bookings
            GET  /admin/timeline?date={date}
Storage:    SQLite
Tech stack: Python, FastAPI, Alpine.js
```

---

## Example 101

**Intent:**
So I'm a wedding planner, been doing it for 6 years mostly with spreadsheets and a paper diary, and it's getting crazy now that I have about 30 weddings a year. I need one place for each couple with their budget, the vendors I booked for them, payments due and a checklist of tasks counting down to the big day.

**Spec:**
```
Type:       Web application (CRM for event planning)
Auth:       Planner login (email + password); couples get read-only access by invite
Data model: Couple(id, names, email, wedding_date, venue, budget)
            Vendor(id, name, category, phone, email)
            VendorBooking(id, couple_id -> Couple, vendor_id -> Vendor, cost, deposit_paid, balance_due_date)
            Task(id, couple_id -> Couple, title, due_date, done)
Features:   - Keep one workspace per couple with budget and venue
            - Book vendors and track deposits and balances
            - Generate a task checklist counted back from the wedding date
            - Show budget spent versus planned
            - List all payments due in the next 30 days across weddings
API:        REST
            GET  /couples/{id}
            POST /couples/{id}/vendor-bookings
            GET  /payments/upcoming
            PATCH /tasks/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma, Tailwind CSS
```

---

## Example 102

**Intent:**
client portal for my graphic design studio where clients approve drafts and leave comments

**Spec:**
```
Type:       Web application (client portal)
Auth:       Designer login; client login by email invite
Data model: Client(id, company, contact_email)
            Project(id, client_id -> Client, name, status, deadline)
            Draft(id, project_id -> Project, version, file_url, uploaded_at, approved)
            Comment(id, draft_id -> Draft, author, text, x_pos, y_pos, created_at)
Features:   - Upload numbered draft versions to a project
            - Let clients pin comments on a spot of the image
            - Approve a draft or request changes
            - Email the designer when feedback arrives
            - Show the history of versions per project
API:        REST
            POST /projects/{id}/drafts
            POST /drafts/{id}/comments
            POST /drafts/{id}/approve
Storage:    PostgreSQL, S3 (files)
Tech stack: Python, Django, React, AWS S3
```

---

## Example 103

**Intent:**
invoicing for our translation agency in django, invoice per word count and language pair

**Spec:**
```
Type:       Web application (invoicing)
Auth:       Staff login (email + password)
Data model: Client(id, name, vat_number, email, currency)
            Rate(id, client_id -> Client, source_lang, target_lang, price_per_word)
            Job(id, client_id -> Client, source_lang, target_lang, word_count, delivered_on, invoice_id -> Invoice)
            Invoice(id, client_id -> Client, number, issued_on, total, status)
Features:   - Record translation jobs with word counts
            - Look up the client's rate for each language pair
            - Bundle a month's delivered jobs into one invoice
            - Generate PDF invoices with VAT handling for EU clients
            - Track paid and unpaid invoices
API:        REST
            POST /jobs
            POST /clients/{id}/invoices?month={month}
            GET  /invoices/{id}/pdf
Storage:    PostgreSQL
Tech stack: Python, Django, Django REST Framework, WeasyPrint
```

---

## Example 104

**Intent:**
hiring tracker, we get applicants for jobs and want to move them through stages and leave interview notes

**Spec:**
```
Type:       Web application (applicant tracking)
Auth:       Team login with Google SSO
Data model: JobOpening(id, title, department, status)
            Candidate(id, name, email, phone, cv_url)
            Application(id, job_id -> JobOpening, candidate_id -> Candidate, stage, applied_at)
            InterviewNote(id, application_id -> Application, interviewer, rating, notes)
Features:   - Publish a job and collect applications with CVs
            - Move applications across stages on a kanban board
            - Add interview notes and ratings
            - Email candidates on rejection with a template
            - Show time-to-hire per opening
API:        REST
            POST /jobs/{id}/applications
            PATCH /applications/{id}/stage
            POST /applications/{id}/notes
Storage:    PostgreSQL, S3 (CVs)
Tech stack: Node.js, NestJS, React, dnd-kit
```

---

## Example 105

**Intent:**
onboarding checklist for new employees

**Spec:**
```
Type:       Web application (employee onboarding)
Auth:       HR and employee login (email + password)
Data model: Template(id, name, role)
            TemplateTask(id, template_id -> Template, title, owner_role, due_offset_days)
            NewHire(id, name, email, role, start_date)
            OnboardingTask(id, new_hire_id -> NewHire, title, owner_role, due_date, done_at)
Features:   - Create checklist templates per role
            - Generate tasks for a new hire from a template and start date
            - Assign tasks to HR, IT or the manager
            - Remind owners of overdue tasks
            - Show onboarding progress per new hire
API:        REST
            POST /new-hires
            GET  /new-hires/{id}/tasks
            PATCH /tasks/{id}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 106

**Intent:**
our care home staff need training certificates tracked (first aid, manual handling) and warning before they expire

**Spec:**
```
Type:       Web application (training records)
Auth:       Manager login (email + password); staff view their own record
Data model: StaffMember(id, name, email, role, start_date)
            Course(id, name, valid_months, mandatory_for_roles)
            Certificate(id, staff_id -> StaffMember, course_id -> Course, completed_on, expires_on, file_url)
Features:   - Record completed courses with certificate uploads
            - Calculate expiry dates from course validity
            - Email staff and manager 30 days before expiry
            - Show a compliance matrix of staff vs mandatory courses
            - Export the matrix for inspections
API:        REST
            POST /certificates
            GET  /compliance
            GET  /compliance/export.xlsx
Storage:    PostgreSQL, S3 (certificates)
Tech stack: Python, Django, openpyxl
```

---

## Example 107

**Intent:**
nurses at our small clinic swap shifts by text and its chaos. want a page to offer a shift and someone else takes it, manager ok's it

**Spec:**
```
Type:       Web application (shift swaps)
Auth:       Staff login (email + password); manager role
Data model: Nurse(id, name, email, grade)
            Shift(id, nurse_id -> Nurse, date, start_time, end_time, ward)
            SwapOffer(id, shift_id -> Shift, offered_by -> Nurse, taken_by -> Nurse, status, created_at)
Features:   - Offer one of your shifts on a swap board
            - Take an offered shift if it doesn't clash with your own
            - Check that the taker has the required grade
            - Approve or reject swaps as the manager
            - Update the rota and notify both nurses when approved
API:        REST
            POST /shifts/{id}/offer
            POST /swaps/{id}/take
            POST /swaps/{id}/approve
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 108

**Intent:**
families book visiting times at the care home, max 3 visits per hour

**Spec:**
```
Type:       Web application (visit booking)
Auth:       Family login (email + password, verified by staff); staff login
Data model: Resident(id, name, room)
            FamilyMember(id, name, email, phone, resident_id -> Resident, verified)
            Visit(id, resident_id -> Resident, family_member_id -> FamilyMember, starts_at, visitors_count)
Features:   - Show visiting slots with remaining capacity
            - Book a visit for a linked resident
            - Limit each slot to 3 visits
            - Show reception a list of today's visitors
            - Cancel visits for a resident who is unwell and notify families
API:        REST
            GET  /slots?date={date}
            POST /visits
            DELETE /visits/{id}
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Livewire
```

---

## Example 109

**Intent:**
Home care agency, carers visit elderly clients at home several times a day. Office makes the schedule, carers see their route and log each visit.

**Spec:**
```
Type:       Web application (home care scheduling)
Auth:       Office and carer login (email + password, 2FA for office)
Data model: Client(id, name, address, care_needs, key_safe_code)
            Carer(id, name, phone, drives)
            Visit(id, client_id -> Client, carer_id -> Carer, planned_start, duration_min, tasks, status)
            VisitLog(id, visit_id -> Visit, arrived_at, left_at, notes, tasks_done)
Features:   - Plan recurring visits per client
            - Assign carers and check for overlapping visits and travel time
            - Show each carer their day route on a map
            - Log arrival, departure and tasks completed
            - Alert the office when a visit is 30 minutes late
API:        REST
            POST /visits
            GET  /carers/me/visits?date={date}
            POST /visits/{id}/log
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, React, Google Maps API
```

---

## Example 110

**Intent:**
online therapy practice, clients book a session and get a video link automatically

**Spec:**
```
Type:       Web application (therapy booking)
Auth:       Client and therapist login (email + password)
Data model: Therapist(id, name, specialties, session_price, timezone)
            Client(id, name, email, timezone)
            Session(id, therapist_id -> Therapist, client_id -> Client, starts_at, video_url, status, paid)
Features:   - Show therapists' availability in the client's timezone
            - Book and pay for a session
            - Create a video meeting link for each session
            - Send reminders 24 hours and 1 hour before
            - Allow free cancellation until 24 hours before
API:        REST
            GET  /therapists/{id}/availability
            POST /sessions
            POST /sessions/{id}/cancel
Storage:    PostgreSQL
Tech stack: Python, Django, Zoom API, Stripe
```

---

## Example 111

**Intent:**
daily report to parents from our kindergarden what kid ate, slept, nappies

**Spec:**
```
Type:       Web application (childcare daily log)
Auth:       Staff login; parent login (email + password)
Data model: Child(id, name, room, birth_date)
            Parent(id, name, email)
            LogEntry(id, child_id -> Child, type, details, logged_at, staff_name)
            Photo(id, child_id -> Child, url, taken_at)
Features:   - Log meals, naps and nappy changes in a few taps
            - Share photos with the child's parents
            - Show parents a live daily timeline
            - Email a daily summary at pickup time
API:        REST
            POST /children/{id}/log
            POST /children/{id}/photos
            GET  /children/{id}/today
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Express, React, AWS S3
```

---

## Example 112

**Intent:**
comedy club tickets for weekly shows, plus a guest list for the comedians' friends

**Spec:**
```
Type:       Web application (event ticketing)
Auth:       Promoter login; buyers check out as guests
Data model: Show(id, title, starts_at, capacity, price)
            Order(id, show_id -> Show, buyer_email, quantity, total, paid_at)
            GuestListEntry(id, show_id -> Show, name, plus_ones, added_by)
            CheckIn(id, show_id -> Show, order_id -> Order, guest_entry_id -> GuestListEntry, checked_at)
Features:   - Sell tickets per show up to venue capacity
            - Add free guest list names per show
            - Count guest list places against capacity
            - Check in ticket buyers and guests at the door
            - Show sales and attendance per show
API:        REST
            GET  /shows
            POST /orders
            POST /shows/{id}/guestlist
            POST /checkins
Storage:    PostgreSQL
Tech stack: Python, Flask, Stripe Checkout
```

---

## Example 113

**Intent:**
visitor sign in at reception on an ipad and notify the person they're visiting

**Spec:**
```
Type:       Web application (visitor management)
Auth:       Reception kiosk with device token; admin login with Microsoft SSO
Data model: Employee(id, name, email, phone)
            Visitor(id, name, company, email)
            Visit(id, visitor_id -> Visitor, host_id -> Employee, signed_in_at, signed_out_at, badge_no)
Features:   - Sign in visitors on a kiosk screen
            - Search and pick the host employee
            - Notify the host by email and Teams message
            - Print a visitor badge
            - Show who is in the building for fire evacuations
API:        REST
            POST /visits
            POST /visits/{id}/sign-out
            GET  /visits/onsite
Storage:    PostgreSQL
Tech stack: TypeScript, React, Node.js, Microsoft Graph API
```

---

## Example 114

**Intent:**
15 company vans - need to track servicing, MOT dates, fuel n which driver has which van

**Spec:**
```
Type:       Web application (fleet management)
Auth:       Fleet manager and driver login (email + password)
Data model: Van(id, reg, model, mileage, mot_due, service_due)
            Driver(id, name, licence_expiry)
            VanAssignment(id, van_id -> Van, driver_id -> Driver, from_date, to_date)
            FuelEntry(id, van_id -> Van, litres, cost, mileage, filled_at)
            ServiceRecord(id, van_id -> Van, date, garage, cost, notes)
Features:   - Assign vans to drivers
            - Log fuel fill-ups with mileage
            - Remind the manager before MOT and service dates
            - Show fuel cost per mile per van
            - Warn when a driver's licence is about to expire
API:        REST
            POST /fuel
            POST /assignments
            GET  /vans/due
Storage:    PostgreSQL
Tech stack: Python, Django, Chart.js
```

---

## Example 115

**Intent:**
B2B ordering portal for our bakery so cafes we supply can order online before 2pm for next day

**Spec:**
```
Type:       Web application (wholesale ordering)
Auth:       Business customer login (email + password); bakery admin login
Data model: Account(id, business_name, address, payment_terms, price_list_id -> PriceList)
            PriceList(id, name)
            PriceListItem(id, price_list_id -> PriceList, product_id -> Product, price)
            Product(id, name, unit)
            WholesaleOrder(id, account_id -> Account, delivery_date, status, total)
            WholesaleLine(id, order_id -> WholesaleOrder, product_id -> Product, quantity)
Features:   - Show each customer their own price list
            - Place orders for next-day delivery until 2pm
            - Repeat a standing order every weekday
            - Produce a bake sheet totalling all products for tomorrow
            - Generate monthly invoices per account
API:        REST
            GET  /catalog
            POST /orders
            GET  /admin/bake-sheet?date={date}
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Inertia.js, Vue.js
```

---

## Example 116

**Intent:**
proof of delivery for our drivers, photo + signature

**Spec:**
```
Type:       Web application (proof of delivery)
Auth:       Driver login (phone + PIN); dispatcher login
Data model: Delivery(id, customer_name, address, items, driver_id -> Driver, status, delivered_at)
            Driver(id, name, phone)
            Proof(id, delivery_id -> Delivery, signature_url, photo_url, latitude, longitude, recipient_name)
Features:   - Show each driver their deliveries for the day
            - Capture the recipient's signature on screen
            - Take a photo of the left package
            - Record GPS location and time of delivery
            - Email the customer a delivery confirmation
API:        REST
            GET  /drivers/me/deliveries
            POST /deliveries/{id}/proof
Storage:    PostgreSQL, S3 (photos and signatures)
Tech stack: Vue.js (PWA), Node.js, Express, signature_pad
```

---

## Example 117

**Intent:**
insurance broker needs to track clients policies and renewal dates so we call them before renewal

**Spec:**
```
Type:       Web application (CRM)
Auth:       Broker login (email + password, 2FA)
Data model: Client(id, name, email, phone, broker_id -> Broker)
            Broker(id, name, email)
            Policy(id, client_id -> Client, insurer, type, premium, start_date, renewal_date, commission)
            CallLog(id, client_id -> Client, broker_id -> Broker, called_at, outcome, notes)
Features:   - Record policies per client with insurer and premium
            - Show a renewal pipeline for the next 60 days
            - Assign renewal calls to brokers
            - Log call outcomes
            - Report commission earned per month
API:        REST
            GET  /renewals?days=60
            POST /clients/{id}/calls
            GET  /reports/commission?month={month}
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 118

**Intent:**
I'm an interior designer and I'd like to track each project: rooms, products I order for the client, the supplier, delivery status and my markup. At the end I send the client one invoice.

**Spec:**
```
Type:       Web application (project tracking)
Auth:       Designer login (email + password)
Data model: Client(id, name, email, address)
            Project(id, client_id -> Client, name, status)
            Room(id, project_id -> Project, name)
            ProductItem(id, room_id -> Room, name, supplier, cost, markup_pct, ordered_on, delivery_status)
Features:   - Organise products by project and room
            - Calculate client price from cost and markup
            - Track order and delivery status per item
            - Show the client a product board without cost prices
            - Generate one final invoice for the project
API:        REST
            POST /projects/{id}/rooms
            POST /rooms/{id}/items
            GET  /projects/{id}/invoice
Storage:    PostgreSQL
Tech stack: TypeScript, Remix, Prisma, Tailwind CSS
```

---

## Example 119

**Intent:**
architect office timesheets per project, see if projects go over budget hours

**Spec:**
```
Type:       Web application (project timesheets)
Auth:       Staff login (email + password); partner role
Data model: Project(id, name, client, budget_hours, fee)
            Phase(id, project_id -> Project, name, budget_hours)
            TimeEntry(id, staff_id -> Staff, phase_id -> Phase, date, hours, note)
            Staff(id, name, hourly_cost)
Features:   - Log hours per day against a project phase
            - Compare hours spent with budget per phase
            - Warn partners when a phase passes 80% of budget
            - Show project profitability from staff costs
            - Lock timesheets after the week is approved
API:        REST
            POST /time-entries
            GET  /projects/{id}/budget
            POST /weeks/{week}/approve
Storage:    PostgreSQL
Tech stack: Python, Flask, React
```

---

## Example 120

**Intent:**
small law firm case management, deadlines and documents per case

**Spec:**
```
Type:       Web application (case management)
Auth:       Lawyer and paralegal login (email + password, 2FA)
Data model: Client(id, name, email, phone)
            Case(id, client_id -> Client, title, court, case_number, lead_lawyer_id -> User, status)
            Deadline(id, case_id -> Case, title, due_date, done)
            CaseDocument(id, case_id -> Case, name, url, version, uploaded_at)
            User(id, name, email, role)
Features:   - Open cases linked to clients
            - Track court deadlines with reminders
            - Upload and version case documents
            - Restrict case access to assigned staff
            - Show a firm-wide calendar of deadlines
API:        REST
            POST /cases
            POST /cases/{id}/deadlines
            POST /cases/{id}/documents
            GET  /deadlines?from={date}
Storage:    PostgreSQL, S3 (encrypted documents)
Tech stack: C#, ASP.NET Core, Angular
```

---

## Example 121

**Intent:**
fridge temperature log for food safety, staff record temps twice a day

**Spec:**
```
Type:       Web application (food safety log)
Auth:       Staff login (PIN); manager login
Data model: Fridge(id, name, location, min_temp, max_temp)
            TempReading(id, fridge_id -> Fridge, temperature, recorded_by, recorded_at)
            CorrectiveAction(id, reading_id -> TempReading, action, recorded_by)
Features:   - Record fridge and freezer temperatures on a tablet
            - Flag readings outside the safe range
            - Require a corrective action for flagged readings
            - Warn the manager when a check is missed
            - Export logs for health inspections
API:        REST
            POST /readings
            POST /readings/{id}/action
            GET  /export?month={month}
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 122

**Intent:**
temperature sensors in our restaurant cold rooms that alert us if it gets too warm at night

**Spec:**
```
Type:       IoT system (temperature monitoring)
Auth:       Owner login to the web dashboard (email + password)
Data model: Sensor(id, name, location, min_temp, max_temp)
            Reading(id, sensor_id -> Sensor, temperature, recorded_at)
            Alert(id, sensor_id -> Sensor, value, started_at, resolved_at)
Features:   - Read temperature every minute from wireless sensors
            - Send readings to the server over MQTT
            - Text the owner when a cold room stays too warm for 10 minutes
            - Show live and historical charts per room
            - Keep a HACCP-ready log of all readings
API:        REST
            GET  /sensors
            GET  /sensors/{id}/readings?from={dt}
Storage:    InfluxDB (readings), PostgreSQL (sensors, alerts)
Tech stack: ESP32 with DS18B20 sensors, Mosquitto MQTT, Python, Grafana, Twilio
```

---

## Example 123

**Intent:**
allergen menu for my restaurant so waiters can quickly check which dishes are safe for a customer

**Spec:**
```
Type:       Web application (allergen lookup)
Auth:       Kitchen manager login to edit; staff view without login on the internal network
Data model: Allergen(id, name)
            Ingredient(id, name)
            IngredientAllergen(ingredient_id -> Ingredient, allergen_id -> Allergen)
            Dish(id, name, category, active)
            DishIngredient(dish_id -> Dish, ingredient_id -> Ingredient)
Features:   - Maintain dishes with their ingredients
            - Work out each dish's allergens from its ingredients
            - Filter the menu by allergens to avoid
            - Print an allergen matrix for the menu
            - Flag dishes when an ingredient's allergens change
API:        REST
            GET  /dishes?exclude={allergens}
            POST /dishes
            GET  /allergen-matrix
Storage:    SQLite
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 124

**Intent:**
wine list and cellar stock for my restaurant, waiters see whats in stock, sommelier does orders

**Spec:**
```
Type:       Web application (cellar inventory)
Auth:       Sommelier login; staff read-only login
Data model: Wine(id, name, producer, vintage, region, colour, bin_number, cost, list_price)
            CellarStock(id, wine_id -> Wine, bottles)
            Movement(id, wine_id -> Wine, change, reason, created_at)
Features:   - Keep the wine list with vintages and bin numbers
            - Reduce stock when a bottle is sold
            - Hide wines from the list when out of stock
            - Show cellar value at cost
            - Suggest reorders based on monthly sales
API:        REST
            GET  /wines?in_stock=true
            POST /wines/{id}/sell
            GET  /reports/cellar-value
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stimulus
```

---

## Example 125

**Intent:**
mortgage broker lead tracker with documents checklist from each client

**Spec:**
```
Type:       Web application (lead tracking)
Auth:       Broker login with 2FA; client upload portal by secure link
Data model: Lead(id, name, email, phone, source, loan_amount, stage)
            ChecklistItem(id, lead_id -> Lead, name, required, received)
            UploadedDocument(id, checklist_item_id -> ChecklistItem, url, uploaded_at)
Features:   - Capture leads from the website form
            - Move leads through stages from enquiry to completion
            - Send clients a checklist of documents to upload
            - Mark documents as received and verified
            - Show conversion rates by lead source
API:        REST
            POST /leads
            PATCH /leads/{id}/stage
            POST /upload/{token}
Storage:    PostgreSQL, S3 (encrypted documents)
Tech stack: Python, Django, AWS S3
```

---

## Example 126

**Intent:**
i want a airtable based thing for my small makeup artist business to take bookings for brides and keep track of trials

**Spec:**
```
Type:       Web application (booking requests)
Data model: Client(id, name, email, wedding_date, venue, party_size)
            Trial(id, client_id -> Client, date, notes, look_photos)
            Booking(id, client_id -> Client, date, start_time, services, deposit_paid)
Features:   - Show a public enquiry form for wedding dates
            - Check the date is not already booked
            - Save enquiries and bookings into Airtable tables
            - Schedule a trial session before the wedding
            - Send a deposit invoice link by email
API:        REST
            POST /enquiries
            GET  /dates/{date}/available
Storage:    Airtable
Tech stack: Airtable, Airtable Web API, Netlify Functions, HTML/JavaScript
```

---

## Example 127

**Intent:**
I want this in Laravel: an admin panel for my driving test centre to manage examiners and test slots

**Spec:**
```
Type:       Web application (admin panel)
Auth:       Admin and examiner login (email + password)
Data model: Examiner(id, name, email, test_categories)
            TestSlot(id, examiner_id -> Examiner, starts_at, category, vehicle_id -> Vehicle, candidate_name, status)
            Vehicle(id, plate, category, available)
Features:   - Create recurring test slots per examiner
            - Book candidates into free slots
            - Assign a test vehicle of the right category
            - Record pass or fail results
            - Show pass rates per examiner
API:        REST
            GET  /slots?date={date}
            POST /slots/{id}/book
            PATCH /slots/{id}/result
Storage:    MySQL
Tech stack: PHP, Laravel, Filament
```

---

## Example 128

**Intent:**
cinema with one screen wants own ticket site, shows films for the week with times

**Spec:**
```
Type:       Web application (cinema ticketing)
Auth:       Staff login; customers buy as guests
Data model: Film(id, title, rating, runtime_min, poster_url, trailer_url)
            Screening(id, film_id -> Film, starts_at, price)
            Seat(id, row, number, is_accessible)
            Booking(id, screening_id -> Screening, email, total, qr_code)
            BookedSeat(booking_id -> Booking, seat_id -> Seat)
Features:   - Show this week's films and screening times
            - Pick seats on a seat map
            - Pay online and receive e-tickets
            - Scan tickets at the door
            - Show occupancy per screening
API:        REST
            GET  /screenings?week={date}
            GET  /screenings/{id}/seats
            POST /bookings
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe, Alpine.js
```

---

## Example 129

**Intent:**
helpdesk 4 our 40 ppl office, ppl raise IT tickets and the IT guy works them

**Spec:**
```
Type:       Web application (helpdesk)
Auth:       Employee login with Google Workspace SSO; IT admin role
Data model: User(id, name, email, role)
            Ticket(id, requester_id -> User, category, subject, description, priority, status, created_at)
            TicketComment(id, ticket_id -> Ticket, author_id -> User, body, internal, created_at)
Features:   - Raise tickets by web form or by email
            - Prioritise and assign tickets
            - Add public replies and internal notes
            - Notify the requester on status changes
            - Show average resolution time per category
API:        REST
            POST /tickets
            POST /tickets/{id}/comments
            PATCH /tickets/{id}
            POST /inbound-email
Storage:    PostgreSQL
Tech stack: Go, HTMX, Postmark inbound email
```

---

## Example 130

**Intent:**
small hostel with dorm beds, book a bed not a room

**Spec:**
```
Type:       Web application (hostel booking)
Auth:       Staff login; guests book as guests
Data model: Dorm(id, name, gender, bed_count)
            Bed(id, dorm_id -> Dorm, label)
            BedBooking(id, bed_id -> Bed, guest_name, email, nationality, check_in, check_out, price)
Features:   - Search free beds by date and dorm type
            - Book several beds for a group in the same dorm
            - Keep the same bed for the whole stay
            - Show a bed occupancy grid for reception
            - Collect passport details at check-in
API:        REST
            GET  /beds/available?check_in={d}&check_out={d}
            POST /bookings
            GET  /admin/grid?from={date}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 131

**Intent:**
ok so basically i run a mobile car detailing business, i drive to people's homes. right now people DM me on instagram and i write it in my notes app lol. i want them to book a package, put their address, and i see my day in order with travel time between jobs

**Spec:**
```
Type:       Web application (mobile service booking)
Auth:       Owner login; customers book with email confirmation
Data model: Package(id, name, vehicle_size, price, duration_min)
            Customer(id, name, phone, email)
            Job(id, customer_id -> Customer, package_id -> Package, address, latitude, longitude, starts_at, status)
Features:   - Book a detailing package with vehicle size and address
            - Only offer times that leave travel time from the previous job
            - Limit bookings to addresses within 25 km
            - Show the day's jobs in order on a map
            - Text customers when the detailer is on the way
API:        REST
            GET  /slots?date={date}&address={address}
            POST /jobs
            GET  /day?date={date}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Google Distance Matrix API, Twilio
```

---

## Example 132

**Intent:**
notary office appointments, clients upload documents first so we can check them

**Spec:**
```
Type:       Web application (appointment booking)
Auth:       Client login (email + password); notary staff login with 2FA
Data model: Client(id, name, email, phone)
            ServiceType(id, name, required_documents, duration_min, fee)
            Appointment(id, client_id -> Client, service_type_id -> ServiceType, starts_at, status)
            UploadedDoc(id, appointment_id -> Appointment, name, url, checked)
Features:   - Book an appointment for a chosen notarial service
            - Show the list of documents needed for that service
            - Upload documents before the appointment
            - Let staff mark documents as checked or ask for corrections
            - Confirm the appointment once documents are complete
API:        REST
            POST /appointments
            POST /appointments/{id}/documents
            PATCH /documents/{id}
Storage:    PostgreSQL, S3 (encrypted documents)
Tech stack: Java, Spring Boot, Vue.js
```

---

## Example 133

**Intent:**
key register for estate agent, who took which property key and when they bring back

**Spec:**
```
Type:       Web application (key management)
Auth:       Staff login (PIN)
Data model: Property(id, address, landlord)
            KeySet(id, property_id -> Property, tag_code, hook_number)
            KeyLoan(id, key_set_id -> KeySet, taken_by, purpose, taken_at, due_back, returned_at)
Features:   - Scan a key tag to check it out
            - Record who took it and why
            - Show which keys are out and overdue
            - Find the hook number for a property
            - Keep a full history per key set
API:        REST
            POST /keys/{tag}/checkout
            POST /keys/{tag}/return
            GET  /loans?overdue=true
Storage:    SQLite
Tech stack: Python, Flask, HTMX
```

---

## Example 134

**Intent:**
Our printing company does quotes for big jobs by email which takes forever. Want sales reps to build quotes with our price rules and track if the customer said yes.

**Spec:**
```
Type:       Web application (quoting)
Auth:       Sales rep and manager login (email + password)
Data model: Customer(id, company, contact_name, email)
            PriceRule(id, product_type, min_qty, max_qty, unit_price, setup_fee)
            Quote(id, customer_id -> Customer, rep_id -> Rep, status, valid_until, total)
            QuoteLine(id, quote_id -> Quote, product_type, quantity, finishing, line_total)
            Rep(id, name, email)
Features:   - Build quotes using price rules by product and quantity
            - Add finishing options with extra costs
            - Send quotes by email with an accept link
            - Track quotes as sent, accepted, declined or expired
            - Show win rate per rep
API:        REST
            POST /quotes
            POST /quotes/{id}/send
            POST /quotes/{id}/accept?token={token}
            GET  /reports/win-rate
Storage:    PostgreSQL
Tech stack: Python, Django, React
```

---

## Example 135

**Intent:**
community garden plots, people apply for a plot and pay yearly

**Spec:**
```
Type:       Web application (allotment management)
Auth:       Member login (email + password); committee admin login
Data model: Plot(id, number, size_m2, yearly_fee, status)
            Applicant(id, name, email, phone, applied_at)
            Tenancy(id, plot_id -> Plot, member_id -> Applicant, year, paid)
Features:   - Apply to join the waiting list
            - Offer free plots in waiting list order
            - Collect yearly fees online
            - Show a map of plots and who has them
            - Send inspection notices for neglected plots
API:        REST
            POST /applications
            POST /plots/{id}/offer
            POST /tenancies/{id}/pay
Storage:    SQLite
Tech stack: Python, Django, Stripe
```

---

## Example 136

**Intent:**
music rehearsal room booking by bands, hourly, with gear add ons

**Spec:**
```
Type:       Web application (studio booking)
Auth:       Band login (email + password); staff login
Data model: Room(id, name, size, hourly_rate)
            GearItem(id, name, hourly_rate)
            Band(id, name, contact_email, phone)
            Session(id, room_id -> Room, band_id -> Band, starts_at, hours, total)
            SessionGear(session_id -> Session, gear_item_id -> GearItem)
Features:   - Book a room for a number of hours
            - Add gear like drum kits or amps to the booking
            - Offer a cheaper rate for late-night slots
            - Generate a door code valid for the session
            - Show the weekly schedule for staff
API:        REST
            GET  /rooms/availability?date={date}
            POST /sessions
            GET  /sessions/{id}/door-code
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe
```

---

## Example 137

**Intent:**
hr tool employe files contracts salary changes reviews

**Spec:**
```
Type:       Web application (HR records)
Auth:       HR login with SSO and 2FA; employees see their own file
Data model: Employee(id, name, email, job_title, department, start_date, manager_id -> Employee)
            Contract(id, employee_id -> Employee, type, start_date, end_date, file_url)
            SalaryChange(id, employee_id -> Employee, amount, effective_date, reason)
            Review(id, employee_id -> Employee, period, rating, summary)
Features:   - Keep one profile per employee with job history
            - Upload signed contracts
            - Record salary changes with effective dates
            - Store performance reviews
            - Log every access to salary data
API:        REST
            GET  /employees/{id}
            POST /employees/{id}/contracts
            POST /employees/{id}/salary-changes
Storage:    PostgreSQL, S3 (encrypted files)
Tech stack: Python, Django, Okta SSO
```

---

## Example 138

**Intent:**
Hello! My mother has a sewing school and she want students can register for courses and she send them messages about course changes. Please make it easy for her, she is not technical.

**Spec:**
```
Type:       Web application (course registration)
Auth:       Admin login for the teacher (email + password); students register with email
Data model: Course(id, title, description, start_date, sessions, price, places)
            Student(id, name, email, phone)
            Registration(id, course_id -> Course, student_id -> Student, paid, created_at)
            Announcement(id, course_id -> Course, message, sent_at)
Features:   - Show upcoming courses with free places
            - Register and pay for a course
            - Send an email and SMS message to everyone in a course
            - Use a simple admin with big buttons for common tasks
            - Show a printable list of students per course
API:        REST
            GET  /courses
            POST /registrations
            POST /courses/{id}/announcements
Storage:    PostgreSQL
Tech stack: Python, Django, Django admin, Twilio
```

---

## Example 139

**Intent:**
pest control company recurring visits for restaurants with reports after each visit

**Spec:**
```
Type:       Web application (service visits)
Auth:       Technician and office login; clients view reports by login
Data model: ClientSite(id, name, address, contact_email, visit_frequency)
            Visit(id, site_id -> ClientSite, technician, scheduled_on, completed_at)
            BaitStation(id, site_id -> ClientSite, code, location)
            StationCheck(id, visit_id -> Visit, station_id -> BaitStation, activity_level, action)
Features:   - Schedule recurring visits per site
            - Check each bait station by scanning its code
            - Record pest activity and treatments
            - Email a signed PDF report to the client
            - Show activity trends per site
API:        REST
            GET  /technicians/me/visits
            POST /visits/{id}/checks
            POST /visits/{id}/complete
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, React (PWA), Puppeteer
```

---

## Example 140

**Intent:**
mosque donations and ramadan iftar volunteer signups

**Spec:**
```
Type:       Web application (community donations and volunteering)
Auth:       Admin login for committee; donors and volunteers without accounts
Data model: Campaign(id, name, goal_amount, ends_on)
            Donation(id, campaign_id -> Campaign, donor_name, email, amount, recurring, gift_aid)
            IftarDay(id, date, volunteers_needed)
            VolunteerSignup(id, iftar_day_id -> IftarDay, name, phone, role)
Features:   - Accept one-off and monthly donations online
            - Show progress towards each campaign goal
            - Let volunteers pick iftar days and roles
            - Show which days still need volunteers
            - Email donation receipts
API:        REST
            POST /donations
            GET  /campaigns/{id}
            POST /iftar-days/{id}/signup
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Stripe
```

---

## Example 141

**Intent:**
supabase + vue app for a bike courier company, shops create pickups and riders accept them

**Spec:**
```
Type:       Web application (courier dispatch)
Auth:       Supabase Auth (shops and riders, email + password)
Data model: Shop(id, name, address, user_id)
            Rider(id, name, phone, user_id, available)
            Pickup(id, shop_id -> Shop, rider_id -> Rider, dropoff_address, size, price, status, created_at)
Features:   - Let shops create pickup requests with drop-off address
            - Show open pickups to available riders in real time
            - Let a rider accept a job so others can't take it
            - Update status from picked up to delivered
            - Bill shops weekly for delivered jobs
Storage:    Supabase Postgres with row-level security
Tech stack: Vue 3, Supabase (Auth, Realtime, Edge Functions)
```

---

## Example 142

**Intent:**
pottery studio, people buy firing and shelf space by month and book wheel time

**Spec:**
```
Type:       Web application (studio membership)
Auth:       Member login (email + password)
Data model: Member(id, name, email, plan, shelf_number)
            Plan(id, name, monthly_price, wheel_hours, firings_included)
            WheelBooking(id, member_id -> Member, wheel_no, starts_at, hours)
            Firing(id, member_id -> Member, pieces, kiln_date, extra_charge)
Features:   - Subscribe to a monthly studio plan
            - Book pottery wheels by the hour within plan limits
            - Log pieces sent for firing and charge extras
            - Assign shelf spaces
            - Show kiln load for the next firing
API:        REST
            POST /wheel-bookings
            POST /firings
            GET  /kiln/next
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe Billing
```

---

## Example 143

**Intent:**
small IT company wants to bill clients for support hours, prepaid blocks of 10 hours

**Spec:**
```
Type:       Web application (support hours billing)
Auth:       Technician login; client login to view balance
Data model: ClientAccount(id, company, contact_email)
            HourBlock(id, client_id -> ClientAccount, hours, price, purchased_on)
            WorkEntry(id, client_id -> ClientAccount, technician, date, minutes, description)
Features:   - Sell prepaid blocks of support hours
            - Log work in 15-minute increments
            - Deduct logged time from the client's balance
            - Email clients when fewer than 2 hours remain
            - Show clients a statement of work done
API:        REST
            POST /clients/{id}/blocks
            POST /work-entries
            GET  /clients/{id}/statement
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 144

**Intent:**
appointments for a beauty salon with several rooms and machines, a laser treatment needs the laser room free

**Spec:**
```
Type:       Web application (resource-aware booking)
Auth:       Client login (email + password); staff login
Data model: Therapist(id, name, qualifications)
            Room(id, name, equipment)
            Treatment(id, name, duration_min, price, required_qualification, required_equipment)
            Booking(id, client_id -> Client, therapist_id -> Therapist, room_id -> Room, treatment_id -> Treatment, start_time)
            Client(id, name, email, phone)
Features:   - Book treatments online
            - Find slots where a qualified therapist and a suitable room are both free
            - Prevent double-booking rooms and machines
            - Show a day view by therapist and by room
            - Require a patch test record before laser treatments
API:        REST
            GET  /slots?treatment={id}&date={date}
            POST /bookings
            GET  /schedule?date={date}&view=rooms
Storage:    PostgreSQL
Tech stack: Python, Django, FullCalendar
```

---

## Example 145

**Intent:**
church service rota who's doing reading, music, coffee each sunday

**Spec:**
```
Type:       Web application (volunteer rota)
Auth:       Rota coordinator login; volunteers log in with email magic link
Data model: Volunteer(id, name, email, roles)
            Service(id, date, title)
            RotaSlot(id, service_id -> Service, role, volunteer_id -> Volunteer)
            Unavailability(id, volunteer_id -> Volunteer, date)
Features:   - Fill each Sunday's roles from volunteers with that role
            - Respect dates volunteers marked as unavailable
            - Share the rota fairly across volunteers
            - Email everyone their dates for the quarter
            - Let volunteers ask for a swap
API:        REST
            POST /rota/generate?quarter={q}
            GET  /rota?from={date}
            POST /unavailability
Storage:    SQLite
Tech stack: Python, Flask, Jinja2
```

---

## Example 146

**Intent:**
online booking for a escape room but also corporate team building packages with invoice payment

**Spec:**
```
Type:       Web application (corporate event booking)
Auth:       Admin login; corporate clients log in to manage their event
Data model: Package(id, name, price_per_person, includes, min_people)
            CorporateClient(id, company, contact_name, email, vat_number)
            EventBooking(id, client_id -> CorporateClient, package_id -> Package, date, people, status)
            Invoice(id, event_booking_id -> EventBooking, number, total, due_date, paid)
Features:   - Request a team-building package for a date and group size
            - Send a quote and confirm the event
            - Invoice companies with 30-day payment terms
            - Collect team names and split groups across rooms
            - Show upcoming corporate events
API:        REST
            POST /event-bookings
            POST /event-bookings/{id}/confirm
            POST /event-bookings/{id}/invoice
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Angular
```

---

## Example 147

**Intent:**
greenhouse plant nursery stock, many plant varieties and pot sizes, garden centres order from us

**Spec:**
```
Type:       Web application (wholesale stock and orders)
Auth:       Staff login; trade customer login
Data model: Plant(id, latin_name, common_name, category)
            StockLot(id, plant_id -> Plant, pot_size, quantity, ready_week, greenhouse)
            TradeCustomer(id, business_name, email, discount_pct)
            TradeOrder(id, customer_id -> TradeCustomer, delivery_week, status)
            TradeOrderLine(id, order_id -> TradeOrder, stock_lot_id -> StockLot, quantity)
Features:   - Track stock lots by plant, pot size and ready week
            - Show trade customers what is available now and soon
            - Reserve stock when orders are placed
            - Produce picking lists per greenhouse
            - Apply trade discounts per customer
API:        REST
            GET  /availability?week={week}
            POST /orders
            GET  /picking?week={week}
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 148

**Intent:**
manage memberships for our chess club, fees and tournament entries

**Spec:**
```
Type:       Web application (club management)
Auth:       Member login (email + password); secretary admin
Data model: Member(id, name, email, rating, membership_paid_until)
            Tournament(id, name, date, rounds, entry_fee)
            Entry(id, tournament_id -> Tournament, member_id -> Member, paid)
            Pairing(id, tournament_id -> Tournament, round, white_id -> Member, black_id -> Member, result)
Features:   - Renew membership online
            - Enter tournaments and pay entry fees
            - Generate Swiss-system pairings each round
            - Record results and update standings
            - Show the club ratings list
API:        REST
            POST /tournaments/{id}/entries
            POST /tournaments/{id}/rounds
            PATCH /pairings/{id}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 149

**Intent:**
need a web app for my laundromat to see which machines are free, customers check from home

**Spec:**
```
Type:       IoT system (machine status)
Data model: Machine(id, number, type, status, cycle_ends_at)
            StatusEvent(id, machine_id -> Machine, status, recorded_at)
Features:   - Detect when each washer or dryer starts and stops using current sensors
            - Show a public page with free machines and minutes left
            - Notify a customer when their cycle ends
            - Show the owner usage per machine and per hour
API:        REST + WebSocket
            GET  /machines
            WS   /machines/live
            POST /machines/{id}/events
Storage:    PostgreSQL
Tech stack: Raspberry Pi with current clamp sensors, Python, FastAPI, Svelte
```

---

## Example 150

**Intent:**
estate agent property listings website, people search houses and book viewings

**Spec:**
```
Type:       Web application (property listings)
Auth:       Agent login; public visitors search without login
Data model: Listing(id, address, price, bedrooms, bathrooms, type, description, status, agent_id -> Agent)
            ListingPhoto(id, listing_id -> Listing, url, position)
            Agent(id, name, email, phone)
            ViewingRequest(id, listing_id -> Listing, name, email, phone, preferred_time, status)
Features:   - Search listings by area, price and bedrooms
            - Show photos and a map for each property
            - Request a viewing time from the listing page
            - Let agents confirm viewings
            - Mark properties as under offer or sold
API:        REST
            GET  /listings?area={a}&min_price={p}&beds={n}
            POST /listings/{id}/viewings
            PATCH /viewings/{id}
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: TypeScript, Next.js, Mapbox, Prisma
```

---

## Example 151

**Intent:**
farmers market organiser here, vendors apply for a stall each saturday and pay the pitch fee

**Spec:**
```
Type:       Web application (market stall booking)
Auth:       Vendor login (email + password); organiser admin login
Data model: Vendor(id, business_name, category, email, insurance_expires)
            MarketDay(id, date, stall_count)
            StallBooking(id, market_day_id -> MarketDay, vendor_id -> Vendor, stall_number, fee, paid, status)
Features:   - Apply for stalls on chosen market days
            - Approve vendors while keeping a mix of categories
            - Assign stall numbers on a market layout
            - Collect pitch fees online
            - Block vendors whose insurance has expired
API:        REST
            GET  /market-days
            POST /market-days/{id}/bookings
            PATCH /bookings/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 152

**Intent:**
slack bot so people in our office can book the meeting rooms without leaving slack

**Spec:**
```
Type:       Bot (Slack)
Auth:       Slack workspace OAuth; users identified by Slack user ID
Data model: Room(id, name, capacity, google_calendar_id)
            RoomBooking(id, room_id -> Room, slack_user_id, starts_at, ends_at, title)
Features:   - Book a room with a /book command and time
            - Show free rooms right now with /rooms
            - Create the event in the room's Google Calendar
            - Cancel your own bookings from a message button
            - Post a reminder 5 minutes before the meeting
API:        REST
            POST /slack/commands
            POST /slack/interactions
Storage:    PostgreSQL
Tech stack: Python, Slack Bolt, Google Calendar API
```

---

## Example 153

**Intent:**
telegram bot where clients join the queue at my barbershop and get a message when its their turn

**Spec:**
```
Type:       Bot (Telegram)
Data model: QueueEntry(id, telegram_chat_id, name, service, joined_at, status)
            Barber(id, name, active)
Features:   - Join the walk-in queue with /join and a chosen service
            - Show your place in the queue and estimated wait
            - Message the client when two people are ahead and when it's their turn
            - Let barbers call the next client from an admin command
            - Remove clients who do not show within 5 minutes
API:        REST
            POST /telegram/webhook
Storage:    Redis
Tech stack: Python, python-telegram-bot, Redis
```

---

## Example 154

**Intent:**
every morning check xero for overdue invoices and email the customers a polite reminder

**Spec:**
```
Type:       Scheduled script (invoice reminders)
Data model: ReminderLog(invoice_id, contact_email, stage, sent_at)
Features:   - Fetch unpaid invoices from Xero every morning at 8am
            - Pick reminder stage by days overdue (7, 14, 30)
            - Send a templated email with the invoice link
            - Skip invoices already reminded at the same stage
            - Email the owner a summary of reminders sent
Input:      Xero OAuth credentials and email templates
Storage:    SQLite (reminder log)
Tech stack: Python, Xero API (xero-python), SMTP, cron
```

---

## Example 155

**Intent:**
hearing aid clinic, follow up patients after fitting and track battery orders

**Spec:**
```
Type:       Web application (clinic follow-ups)
Auth:       Audiologist login with 2FA
Data model: Patient(id, name, phone, email, address)
            Fitting(id, patient_id -> Patient, device_model, serial_left, serial_right, fitted_on)
            FollowUp(id, fitting_id -> Fitting, due_on, done_on, notes)
            BatteryOrder(id, patient_id -> Patient, size, packs, posted_on)
Features:   - Record fittings with device serial numbers
            - Create follow-ups at 2 weeks, 3 months and 1 year
            - Show a daily list of follow-up calls
            - Record and post battery orders
            - Warn when a device warranty is ending
API:        REST
            POST /fittings
            GET  /followups?due={date}
            POST /battery-orders
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Razor Pages
```

---

## Example 156

**Intent:**
food truck, post where we are each day and let people preorder for pickup

**Spec:**
```
Type:       Web application (preorders and location schedule)
Auth:       Owner login; customers order as guests
Data model: Stop(id, date, location_name, latitude, longitude, open_time, close_time)
            MenuItem(id, name, price, sold_out)
            Preorder(id, stop_id -> Stop, customer_name, phone, pickup_time, total, status)
            PreorderItem(id, preorder_id -> Preorder, menu_item_id -> MenuItem, quantity)
Features:   - Publish the weekly schedule of truck locations
            - Show today's location on a map
            - Preorder for a 10-minute pickup window
            - Limit orders per window to what the kitchen can handle
            - Text customers when the order is ready
API:        REST
            GET  /stops?week={date}
            POST /preorders
            PATCH /preorders/{id}/ready
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, Svelte, Leaflet, Twilio
```

---

## Example 157

**Intent:**
schedule restaurant staff and see labour cost as % of forecast sales

**Spec:**
```
Type:       Web application (labour scheduling)
Auth:       Manager login (email + password)
Data model: Employee(id, name, role, hourly_wage)
            Shift(id, employee_id -> Employee, date, start_time, end_time)
            SalesForecast(id, date, expected_sales)
Features:   - Schedule shifts per day on a weekly grid
            - Calculate labour cost per day from wages and hours
            - Show labour cost as a percentage of forecast sales
            - Forecast sales from the same weekday in past weeks
            - Warn when labour goes above a target percentage
API:        REST
            GET  /week/{date}
            POST /shifts
            GET  /week/{date}/labour
Storage:    PostgreSQL
Tech stack: Python, FastAPI, pandas, React
```

---

## Example 158

**Intent:**
clock in kiosk on a tablet at the entrance, takes a photo so nobody clocks in for a friend

**Spec:**
```
Type:       Web application (time clock kiosk)
Auth:       Employee PIN on the kiosk; manager login (email + password)
Data model: Employee(id, name, pin_hash, department)
            Punch(id, employee_id -> Employee, type, punched_at, photo_url)
Features:   - Clock in and out with a PIN on a tablet
            - Take a photo with the tablet camera at each punch
            - Show managers punches with photos to review
            - Flag missing clock-outs at the end of the day
            - Export hours per employee for payroll
API:        REST
            POST /punches
            GET  /punches?date={date}
            GET  /export?from={date}&to={date}
Storage:    PostgreSQL, S3 (photos)
Tech stack: JavaScript (MediaDevices API), Node.js, Express
```

---

## Example 159

**Intent:**
pharmacy stock w batch numbers + expiry dates, use oldest 1st

**Spec:**
```
Type:       Web application (inventory with batches)
Auth:       Pharmacist and assistant login (email + password)
Data model: Drug(id, name, strength, form, reorder_level)
            Batch(id, drug_id -> Drug, batch_no, expiry_date, quantity, received_on)
            Dispense(id, batch_id -> Batch, quantity, dispensed_at)
Features:   - Receive stock with batch numbers and expiry dates
            - Suggest the batch expiring first when dispensing
            - List batches expiring in the next 90 days
            - Find all stock of a batch for recalls
            - Alert when stock falls below reorder level
API:        REST
            POST /batches
            POST /dispense
            GET  /batches?expiring_within=90
            GET  /batches/search?batch_no={no}
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Thymeleaf
```

---

## Example 160

**Intent:**
hardwear store special orders tracking. customer asks for something we dont stock, we order it, call them when in

**Spec:**
```
Type:       Web application (special orders)
Auth:       Staff login (PIN)
Data model: Customer(id, name, phone)
            SpecialOrder(id, customer_id -> Customer, item_description, supplier, deposit, ordered_on, arrived_on, collected_on, status)
Features:   - Record a special order with deposit taken
            - Track orders as requested, ordered, arrived, collected
            - Text the customer when the item arrives
            - List orders waiting longer than 2 weeks
            - Print a shelf label for arrived items
API:        REST
            POST /orders
            PATCH /orders/{id}/status
            GET  /orders?status=ordered
Storage:    SQLite
Tech stack: Python, Flask, Twilio
```

---

## Example 161

**Intent:**
trade show organiser, exhibitors choose a booth on the floor plan and pay

**Spec:**
```
Type:       Web application (booth sales)
Auth:       Exhibitor login (email + password); organiser admin
Data model: Event(id, name, venue, dates)
            Booth(id, event_id -> Event, code, size_m2, price, x, y, corner, status)
            Exhibitor(id, company, contact_email, sector)
            BoothReservation(id, booth_id -> Booth, exhibitor_id -> Exhibitor, paid, reserved_at)
Features:   - Show an interactive floor plan with booth status
            - Reserve a booth for 48 hours before payment
            - Charge extra for corner booths
            - Collect exhibitor details for the catalogue
            - Release unpaid reservations automatically
API:        REST
            GET  /events/{id}/booths
            POST /booths/{id}/reserve
            POST /reservations/{id}/pay
Storage:    PostgreSQL
Tech stack: TypeScript, React, Konva, NestJS, Stripe
```

---

## Example 162

**Intent:**
small groups at our church, leaders take attendance and members find a group near them

**Spec:**
```
Type:       Web application (small groups)
Auth:       Member login (email + password); leader and admin roles
Data model: Group(id, name, leader_id -> Member, meeting_day, area, latitude, longitude, capacity)
            Member(id, name, email, phone, postcode)
            GroupMember(group_id -> Group, member_id -> Member, joined_on)
            Meeting(id, group_id -> Group, date, attendees)
Features:   - Find groups by area and meeting day on a map
            - Request to join a group
            - Let leaders take attendance each meeting
            - Show pastors groups with falling attendance
            - Message all members of a group
API:        REST
            GET  /groups?near={postcode}
            POST /groups/{id}/join
            POST /groups/{id}/meetings
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Mapbox, Hotwire
```

---

## Example 163

**Intent:**
badminton hall courts, members pay less than non members

**Spec:**
```
Type:       Web application (court booking)
Auth:       User login (email + password)
Data model: User(id, name, email, is_member, member_until)
            Court(id, number)
            Booking(id, court_id -> Court, user_id -> User, starts_at, price, paid)
            PriceRule(id, member_price, guest_price, peak_start, peak_end, peak_extra)
Features:   - Book a court for 30 or 60 minutes
            - Price bookings by membership status and peak hours
            - Pay at booking by card
            - Allow members to book 14 days ahead, others 3 days
            - Show the hall's daily court grid
API:        REST
            GET  /courts/availability?date={date}
            POST /bookings
            GET  /prices
Storage:    PostgreSQL
Tech stack: PHP, Symfony, Stripe
```

---

## Example 164

**Intent:**
climbing gym needs online waiver before first visit and check in at desk

**Spec:**
```
Type:       Web application (waivers and check-in)
Auth:       Staff login; climbers sign without an account
Data model: Climber(id, name, birth_date, email, phone, emergency_contact)
            Waiver(id, climber_id -> Climber, version, signature_url, signed_at, guardian_name)
            Visit(id, climber_id -> Climber, checked_in_at, entry_type)
Features:   - Sign a digital waiver on phone or kiosk
            - Require a guardian signature for climbers under 18
            - Search climbers by name at the desk
            - Check in and record entry type (day pass, membership)
            - Ask climbers to re-sign when the waiver version changes
API:        REST
            POST /waivers
            GET  /climbers?q={name}
            POST /visits
Storage:    PostgreSQL, S3 (signatures)
Tech stack: TypeScript, Next.js, signature_pad
```

---

## Example 165

**Intent:**
riding stable lessons, no horse shud do more then 3 lessons a day!!

**Spec:**
```
Type:       Web application (riding lessons)
Auth:       Rider login (email + password); instructor and admin login
Data model: Horse(id, name, max_lessons_per_day, suitable_levels, available)
            Rider(id, name, level, weight_kg)
            Lesson(id, instructor, starts_at, type, max_riders)
            LessonRider(lesson_id -> Lesson, rider_id -> Rider, horse_id -> Horse)
Features:   - Book a place in group or private lessons
            - Assign horses to riders by level and weight
            - Block a horse once it has done 3 lessons that day
            - Mark horses as resting or lame
            - Show each horse's weekly workload
API:        REST
            POST /lessons/{id}/book
            PATCH /lesson-riders/{id}/horse
            GET  /horses/workload?week={date}
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 166

**Intent:**
Doggy daycare with day packages, owners book days in advance, staff see how many dogs are coming

**Spec:**
```
Type:       Web application (daycare booking)
Auth:       Owner login (email + password); staff login
Data model: Owner(id, name, email, phone)
            Dog(id, owner_id -> Owner, name, breed, size, approved)
            DayPackage(id, owner_id -> Owner, days_total, days_used, expires_on)
            DayBooking(id, dog_id -> Dog, date, status)
Features:   - Book daycare days using package credits
            - Require an assessment day before regular bookings
            - Cap daily numbers by dog size
            - Show staff the list of dogs expected today
            - Let owners buy new packages online
API:        REST
            POST /day-bookings
            GET  /staff/today
            POST /packages/checkout
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe
```

---

## Example 167

**Intent:**
board game cafe — book a table and reserve a game from our library

**Spec:**
```
Type:       Web application (table booking)
Auth:       Staff login; customers book as guests
Data model: CafeTable(id, number, seats)
            Game(id, title, min_players, max_players, play_time_min, copies)
            TableBooking(id, table_id -> CafeTable, name, email, party_size, starts_at, hours)
            GameReservation(id, booking_id -> TableBooking, game_id -> Game)
Features:   - Book a table by party size and time
            - Browse the game library by player count and length
            - Reserve a game for the booking if a copy is free
            - Charge a cover fee per person
            - Show staff tonight's tables and reserved games
API:        REST
            GET  /games?players={n}
            POST /bookings
            POST /bookings/{id}/games
Storage:    SQLite
Tech stack: Python, Flask, Alpine.js, Stripe
```

---

## Example 168

**Intent:**
language school: new students take a placement test online and get put in the right class level

**Spec:**
```
Type:       Web application (placement and enrolment)
Auth:       Student login (email + password); admin login
Data model: Question(id, level, text, options, correct_option)
            Student(id, name, email, native_language)
            TestAttempt(id, student_id -> Student, score, level_result, taken_at)
            LanguageClass(id, level, schedule, capacity, teacher)
            Enrolment(id, class_id -> LanguageClass, student_id -> Student)
Features:   - Run an adaptive placement test with multiple choice questions
            - Calculate the CEFR level from the score
            - Suggest classes at that level with free places
            - Enrol the student and send the timetable
            - Let admins edit the question bank
API:        REST
            POST /tests/start
            POST /tests/{id}/answer
            GET  /classes?level={level}
            POST /enrolments
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 169

**Intent:**
school canteen where parents preorder lunch for their kids and top up a balance

**Spec:**
```
Type:       Web application (school meals)
Auth:       Parent login (email + password); canteen staff login
Data model: Parent(id, name, email, balance)
            Child(id, parent_id -> Parent, name, class, dietary_needs)
            Meal(id, date, name, price, vegetarian)
            MealOrder(id, child_id -> Child, meal_id -> Meal, status)
Features:   - Show the weekly menu
            - Order lunches for each child a week ahead
            - Top up the account balance by card
            - Print class lists of meals for the kitchen
            - Warn parents when the balance is low
API:        REST
            GET  /menu?week={date}
            POST /orders
            POST /balance/topup
            GET  /kitchen/lists?date={date}
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Stripe
```

---

## Example 170

**Intent:**
substitute teacher cover — when a teacher is sick we need to find who is free that period

**Spec:**
```
Type:       Web application (cover management)
Auth:       Staff login via school Google accounts
Data model: Teacher(id, name, email, subjects)
            Period(id, day, number, start_time)
            TimetableEntry(id, teacher_id -> Teacher, period_id -> Period, class_name, room)
            Absence(id, teacher_id -> Teacher, date)
            Cover(id, absence_id -> Absence, entry_id -> TimetableEntry, cover_teacher_id -> Teacher)
Features:   - Record a teacher absence for a day
            - List the lessons that need cover
            - Suggest free teachers for each period, fewest covers first
            - Notify cover teachers by email
            - Track cover count per teacher for fairness
API:        REST
            POST /absences
            GET  /absences/{id}/suggestions
            POST /covers
Storage:    PostgreSQL
Tech stack: Python, Django, Google OAuth
```

---

## Example 171

**Intent:**
school fees invoices to parents every term w sibling discount

**Spec:**
```
Type:       Web application (school billing)
Auth:       Bursar login with 2FA; parent login
Data model: Family(id, name, billing_email)
            Pupil(id, family_id -> Family, name, year_group)
            FeeSchedule(id, year_group, term_fee)
            FeeInvoice(id, family_id -> Family, term, total, discount, status, due_date)
Features:   - Generate termly invoices per family
            - Apply 10% discount for the second child and later
            - Add extras like trips and lunches
            - Let parents pay by card or bank transfer
            - Show overdue balances to the bursar
API:        REST
            POST /invoices/generate?term={term}
            GET  /families/{id}/invoices
            POST /invoices/{id}/pay
Storage:    PostgreSQL
Tech stack: Ruby on Rails, GoCardless, Stripe
```

---

## Example 172

**Intent:**
behaviour points system for our school, teachers give points and parents see them

**Spec:**
```
Type:       Web application (behaviour tracking)
Auth:       Teacher login (school SSO); parent login
Data model: Student(id, name, class_id, house)
            BehaviourType(id, name, points, positive)
            BehaviourEvent(id, student_id -> Student, type_id -> BehaviourType, teacher, note, created_at)
Features:   - Award positive or negative points in two taps
            - Show running totals per student and house
            - Notify parents of serious incidents
            - Show a house leaderboard for assemblies
            - Report students with repeated negative events
API:        REST
            POST /events
            GET  /students/{id}/events
            GET  /houses/leaderboard
Storage:    PostgreSQL
Tech stack: TypeScript, SvelteKit, Prisma
```

---

## Example 173

**Intent:**
PTA raffle ticket sales online with draw

**Spec:**
```
Type:       Web application (raffle)
Auth:       PTA admin login; buyers check out as guests
Data model: Raffle(id, name, ticket_price, draw_at)
            Prize(id, raffle_id -> Raffle, name, donor, position)
            TicketPurchase(id, raffle_id -> Raffle, buyer_name, email, quantity, first_number, paid)
            Winner(id, prize_id -> Prize, ticket_number)
Features:   - Sell numbered raffle tickets online
            - List prizes and their donors
            - Run a random draw with a logged seed
            - Email winners and show results publicly
API:        REST
            POST /raffles/{id}/tickets
            POST /raffles/{id}/draw
            GET  /raffles/{id}/results
Storage:    PostgreSQL
Tech stack: Python, Flask, Stripe Checkout
```

---

## Example 174

**Intent:**
amateur theatre auditions: people sign up for a slot, directors make notes and cast them

**Spec:**
```
Type:       Web application (audition management)
Auth:       Director login; actors sign up with email
Data model: Production(id, title, audition_dates)
            Role(id, production_id -> Production, name, description)
            AuditionSlot(id, production_id -> Production, starts_at, actor_id -> Actor)
            Actor(id, name, email, phone, headshot_url)
            AuditionNote(id, slot_id -> AuditionSlot, director, role_id -> Role, rating, notes)
Features:   - Book an audition slot for a production
            - Upload a headshot
            - Rate actors for specific roles during auditions
            - Compare candidates per role
            - Publish the cast list and email everyone
API:        REST
            POST /productions/{id}/slots/book
            POST /slots/{id}/notes
            POST /productions/{id}/cast
Storage:    PostgreSQL, S3 (headshots)
Tech stack: Node.js, Express, Vue.js
```

---

## Example 175

**Intent:**
rowing club boats booking, only people with right qualification can take single sculls

**Spec:**
```
Type:       Web application (equipment booking)
Auth:       Member login (email + password); captain admin role
Data model: Boat(id, name, type, seats, min_grade, damaged)
            Member(id, name, email, grade)
            BoatBooking(id, boat_id -> Boat, member_id -> Member, starts_at, ends_at, crew)
            DamageReport(id, boat_id -> Boat, reported_by, description, created_at)
Features:   - Book boats for an outing
            - Allow only members with the required grade to book each boat
            - Report damage and take the boat out of use
            - Show the boathouse schedule for the day
            - Let captains change member grades
API:        REST
            GET  /boats/availability?date={date}
            POST /bookings
            POST /boats/{id}/damage
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 176

**Intent:**
pub quiz night, teams register online in advance, quizmaster enters scores per round and a screen shows the leaderboard

**Spec:**
```
Type:       Web application (quiz scoring)
Auth:       Quizmaster login; teams register without accounts
Data model: QuizNight(id, date, rounds, max_teams)
            Team(id, quiz_night_id -> QuizNight, name, players, contact_email)
            RoundScore(id, team_id -> Team, round, score)
Features:   - Register teams for a quiz night up to the limit
            - Enter scores per round on a tablet
            - Show a live leaderboard on the pub TV
            - Break ties with a tiebreak question score
            - Keep a season league table
API:        REST + WebSocket
            POST /nights/{id}/teams
            POST /teams/{id}/scores
            WS   /nights/{id}/leaderboard
Storage:    SQLite
Tech stack: Python, FastAPI, WebSockets, Svelte
```

---

## Example 177

**Intent:**
brewery keg tracking - which pub has which keg and when it should come back

**Spec:**
```
Type:       Web application (asset tracking)
Auth:       Brewery staff login (email + password)
Data model: Keg(id, barcode, size_litres, status)
            Customer(id, pub_name, address)
            KegMovement(id, keg_id -> Keg, customer_id -> Customer, beer, filled_on, sent_on, returned_on)
Features:   - Scan kegs when filled, sent out and returned
            - Show which customer holds each keg
            - List kegs out longer than 60 days
            - Charge customers for lost kegs
            - Show keg cycle time per customer
API:        REST
            POST /kegs/{barcode}/fill
            POST /kegs/{barcode}/dispatch
            POST /kegs/{barcode}/return
            GET  /kegs?overdue=true
Storage:    PostgreSQL
Tech stack: Go, HTMX, ZXing barcode scanning
```

---

## Example 178

**Intent:**
winery tasting reservations, groups of up to 8, different tasting flights

**Spec:**
```
Type:       Web application (tasting reservations)
Auth:       Staff login; guests book as guests
Data model: Flight(id, name, wines, price_per_person, duration_min)
            TastingSlot(id, starts_at, capacity)
            Reservation(id, slot_id -> TastingSlot, flight_id -> Flight, name, email, guests, total, paid)
Features:   - Book a tasting flight for up to 8 guests
            - Confirm guests are of legal drinking age
            - Charge in full at booking
            - Show the cellar door a day sheet with flights
            - Email a follow-up with a wine club offer
API:        REST
            GET  /slots?date={date}
            POST /reservations
            GET  /admin/day?date={date}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 179

**Intent:**
window cleaning round, customers every 4 or 8 weeks, plan my days and track who paid

**Spec:**
```
Type:       Web application (round management)
Auth:       Owner login (email + password)
Data model: Customer(id, name, address, latitude, longitude, price, frequency_weeks, last_cleaned)
            Clean(id, customer_id -> Customer, date, done, paid)
Features:   - Work out which customers are due each day
            - Order the day's stops by shortest route
            - Mark cleans as done on the phone
            - Track unpaid cleans and send payment links
            - Reschedule rained-off days
API:        REST
            GET  /due?date={date}
            PATCH /cleans/{id}
            POST /cleans/{id}/payment-link
Storage:    SQLite
Tech stack: Python, Flask, OpenRouteService API, Stripe Payment Links
```

---

## Example 180

**Intent:**
we service HVAC units in offices on yearly contracts and need to know which visits are due

**Spec:**
```
Type:       Web application (service contracts)
Auth:       Office and technician login (email + password)
Data model: ClientCompany(id, name, contact_email)
            SiteUnit(id, client_id -> ClientCompany, address, unit_model, serial_no, installed_on)
            Contract(id, client_id -> ClientCompany, start_date, end_date, visits_per_year, value)
            ServiceVisit(id, unit_id -> SiteUnit, scheduled_on, technician, report, completed_on)
Features:   - Store contracts with visits per year
            - Generate due service visits per unit
            - Assign visits to technicians
            - Record service reports and refrigerant used
            - Warn about contracts ending in 60 days
API:        REST
            GET  /visits?due_before={date}
            PATCH /visits/{id}
            GET  /contracts?ending_within=60
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, React
```

---

## Example 181

**Intent:**
fire extinguisher inspections for my clients buildings, each extinguisher has a QR sticker

**Spec:**
```
Type:       Web application (inspection tracking)
Auth:       Inspector login (email + password); client read-only login
Data model: Building(id, client, address)
            Extinguisher(id, building_id -> Building, qr_code, type, location, manufactured_on)
            Inspection(id, extinguisher_id -> Extinguisher, inspector, inspected_on, passed, notes)
Features:   - Scan a QR sticker to open the extinguisher record
            - Record a monthly or annual inspection result
            - Flag extinguishers due for replacement
            - Produce a compliance certificate per building
            - Show clients the status of all their units
API:        REST
            GET  /extinguishers/{qr}
            POST /extinguishers/{qr}/inspections
            GET  /buildings/{id}/certificate
Storage:    PostgreSQL
Tech stack: Python, Django, React (PWA)
```

---

## Example 182

**Intent:**
removals company quotes: customer lists their furniture and we calculate the van size and price

**Spec:**
```
Type:       Web application (moving quotes)
Auth:       Staff login; customers request quotes without accounts
Data model: ItemType(id, name, volume_m3)
            QuoteRequest(id, name, email, from_address, to_address, move_date, distance_km, floors)
            QuoteItem(id, request_id -> QuoteRequest, item_type_id -> ItemType, quantity)
            Quote(id, request_id -> QuoteRequest, van_size, crew, price, status)
Features:   - Let customers pick furniture from a room-by-room list
            - Calculate total volume and choose the van size
            - Calculate distance between the two addresses
            - Price by volume, distance and stairs
            - Let staff adjust and send the final quote
API:        REST
            GET  /item-types
            POST /quote-requests
            POST /quote-requests/{id}/quote
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Google Distance Matrix API
```

---

## Example 183

**Intent:**
skip hire booking with postcode check and delivery date

**Spec:**
```
Type:       Web application (skip hire)
Auth:       Admin and driver login; customers order as guests
Data model: SkipSize(id, name, cubic_yards, price, stock)
            ServiceArea(id, postcode_prefix, surcharge)
            SkipOrder(id, skip_size_id -> SkipSize, address, postcode, delivery_date, collection_date, permit_needed, status)
Features:   - Check the postcode is in a service area
            - Choose a skip size and delivery date
            - Add a road permit fee when the skip goes on the street
            - Plan driver deliveries and collections by day
            - Show skips currently out at customer sites
API:        REST
            GET  /areas/check?postcode={pc}
            POST /orders
            GET  /drivers/schedule?date={date}
Storage:    MySQL
Tech stack: PHP, Laravel, Livewire
```

---

## Example 184

**Intent:**
marquee and event furniture hire with stock check for the event date

**Spec:**
```
Type:       Web application (event hire)
Auth:       Staff login; customer login for repeat clients
Data model: HireItem(id, name, category, total_stock, daily_price)
            HireOrder(id, customer_name, email, event_date, setup_date, collect_date, venue, status)
            HireLine(id, order_id -> HireOrder, item_id -> HireItem, quantity)
Features:   - Check how many of each item are free for the hire period
            - Build an order of marquees, tables and chairs
            - Take a damage deposit
            - Produce loading lists for the van crew
            - Mark items damaged or missing on return
API:        REST
            GET  /items/availability?from={date}&to={date}
            POST /orders
            GET  /orders/{id}/loading-list
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 185

**Intent:**
bridal shop appointments for trying on dresses, max 2 brides at same time

**Spec:**
```
Type:       Web application (appointment booking)
Auth:       Consultant login; brides book with email confirmation
Data model: Consultant(id, name)
            Appointment(id, bride_name, email, phone, wedding_date, guests, budget_range, starts_at, consultant_id -> Consultant)
            DressNote(id, appointment_id -> Appointment, dress_style, size, liked)
Features:   - Book a 90-minute appointment with up to 4 guests
            - Allow only 2 appointments at the same time
            - Collect wedding date and budget in advance
            - Note dresses tried and liked during the visit
            - Send the bride a list of her favourites afterwards
API:        REST
            GET  /slots?date={date}
            POST /appointments
            POST /appointments/{id}/notes
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 186

**Intent:**
second hand clothes consignment shop, track items per consignor and pay them 50% when sold

**Spec:**
```
Type:       Web application (consignment)
Auth:       Staff login; consignor login to view their items
Data model: Consignor(id, name, email, iban, balance)
            ConsignedItem(id, consignor_id -> Consignor, description, price, tag_code, received_on, sold_on, status)
            Payout(id, consignor_id -> Consignor, amount, paid_on)
Features:   - Tag incoming items with a barcode per consignor
            - Mark items sold at the till and credit 50% to the consignor
            - Reduce prices automatically after 30 and 60 days
            - Show consignors their items and balance
            - Pay out balances monthly
API:        REST
            POST /items
            POST /items/{tag}/sell
            GET  /consignors/me
            POST /payouts
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 187

**Intent:**
comic book shop pull list, customers subscribe to series and we set aside each new issue

**Spec:**
```
Type:       Web application (pull list)
Auth:       Customer login (email + password); staff login
Data model: Series(id, title, publisher)
            Issue(id, series_id -> Series, number, release_date)
            Subscription(id, customer_id -> Customer, series_id -> Series)
            Hold(id, customer_id -> Customer, issue_id -> Issue, picked_up)
            Customer(id, name, email, box_number)
Features:   - Subscribe to series on a pull list
            - Import weekly new releases from the distributor list
            - Create holds for subscribers when issues arrive
            - Show staff how many copies to order per issue
            - Email customers when their box has new issues
API:        REST
            POST /subscriptions
            POST /releases/import
            GET  /orders/forecast?week={date}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Sidekiq
```

---

## Example 188

**Intent:**
music shop rents instruments to students monthly with rent to own option

**Spec:**
```
Type:       Web application (instrument rental)
Auth:       Staff login; parent login to manage rentals
Data model: Instrument(id, type, brand, serial_no, value, status)
            RentalAgreement(id, instrument_id -> Instrument, customer_id -> Customer, monthly_fee, start_date, months_paid, status)
            Customer(id, name, email, student_name, school)
Features:   - Rent instruments with a monthly direct debit
            - Count paid months towards owning the instrument
            - Transfer ownership when enough is paid
            - Track instrument returns and repairs
            - Show instruments out per school
API:        REST
            POST /agreements
            POST /agreements/{id}/return
            GET  /agreements/{id}/buyout
Storage:    PostgreSQL
Tech stack: Python, Django, GoCardless
```

---

## Example 189

**Intent:**
funeral home system to plan each funeral, tasks, family contacts, costs

**Spec:**
```
Type:       Web application (funeral arrangements)
Auth:       Funeral director login (email + password)
Data model: Deceased(id, name, date_of_death, place)
            FamilyContact(id, deceased_id -> Deceased, name, relation, phone, email)
            Arrangement(id, deceased_id -> Deceased, service_type, venue, service_at, burial_or_cremation)
            CostItem(id, arrangement_id -> Arrangement, description, amount, third_party)
            ArrangementTask(id, arrangement_id -> Arrangement, title, due_at, done)
Features:   - Create an arrangement with service details
            - Generate a standard task checklist for each funeral
            - Build an itemised cost estimate
            - Keep family contacts in one place
            - Show all services on a calendar
API:        REST
            POST /arrangements
            GET  /arrangements/{id}/estimate
            PATCH /tasks/{id}
Storage:    PostgreSQL
Tech stack: PHP, Laravel, FullCalendar
```

---

## Example 190

**Intent:**
dental lab takes orders from dentists for crowns and tracks each case

**Spec:**
```
Type:       Web application (lab case tracking)
Auth:       Dentist login (email + password); lab technician login
Data model: Practice(id, name, address)
            Dentist(id, practice_id -> Practice, name, email)
            LabCase(id, dentist_id -> Dentist, patient_ref, work_type, shade, due_date, status)
            CaseFile(id, case_id -> LabCase, url, kind)
Features:   - Submit a case with work type, shade and due date
            - Upload intraoral scan files (STL)
            - Track cases through design, milling and finishing
            - Show dentists the status of their cases
            - Invoice practices monthly for completed cases
API:        REST
            POST /cases
            POST /cases/{id}/files
            PATCH /cases/{id}/status
Storage:    PostgreSQL, S3 (scan files)
Tech stack: Java, Spring Boot, Angular
```

---

## Example 191

**Intent:**
walk in clinic queue, patients take a number on a tablet and a TV shows who is next

**Spec:**
```
Type:       Web application (queue management)
Auth:       Staff login on the doctor's desk
Data model: Ticket(id, number, patient_name, reason, created_at, called_at, room, status)
            Room(id, name)
Features:   - Take a queue number on a tablet at the entrance
            - Call the next patient to a room from the doctor's screen
            - Show the called number and room on a TV with a sound
            - Show estimated waiting time
            - Reset numbering each day
API:        REST + WebSocket
            POST /tickets
            POST /rooms/{id}/call-next
            WS   /display
Storage:    Redis
Tech stack: Node.js, Socket.IO, React
```

---

## Example 192

**Intent:**
nutritionist client portal, clients log food and weight, I write them a meal plan

**Spec:**
```
Type:       Web application (client portal)
Auth:       Nutritionist and client login (email + password)
Data model: Client(id, name, email, goal, start_weight)
            WeightEntry(id, client_id -> Client, weight_kg, recorded_on)
            FoodLog(id, client_id -> Client, meal, description, photo_url, logged_at)
            MealPlan(id, client_id -> Client, week_start, content)
Features:   - Log meals with photos and weekly weight
            - Write and publish a weekly meal plan per client
            - Chart weight progress over time
            - Comment on a client's food logs
            - Show clients who have not logged for 3 days
API:        REST
            POST /food-logs
            POST /weights
            POST /clients/{id}/meal-plans
Storage:    PostgreSQL, S3 (photos)
Tech stack: TypeScript, Next.js, Supabase, Chart.js
```

---

## Example 193

**Intent:**
meal prep business — customers choose meals for next week before Thursday, we cook in bulk

**Spec:**
```
Type:       Web application (meal prep ordering)
Auth:       Customer login (email + password); kitchen admin login
Data model: Meal(id, name, calories, protein_g, price, week_start)
            Customer(id, name, email, address, delivery_day)
            WeeklyOrder(id, customer_id -> Customer, week_start, total, paid)
            WeeklyOrderItem(id, order_id -> WeeklyOrder, meal_id -> Meal, quantity)
Features:   - Publish next week's menu with nutrition info
            - Close ordering on Thursday at midnight
            - Total portions per meal for the kitchen
            - Print labels with nutrition and use-by date
            - Group deliveries by day and area
API:        REST
            GET  /menu?week={date}
            POST /orders
            GET  /kitchen/totals?week={date}
            GET  /kitchen/labels?week={date}
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe, WeasyPrint
```

---

## Example 194

**Intent:**
vending machines restocking, 40 machines, drivers need to know what to load

**Spec:**
```
Type:       Web application (route restocking)
Auth:       Driver and manager login (email + password)
Data model: Machine(id, location, latitude, longitude, model)
            Slot(id, machine_id -> Machine, code, product_id -> Product, capacity, current_qty)
            Product(id, name, cost, price)
            RestockVisit(id, machine_id -> Machine, driver, visited_at, cash_collected)
Features:   - Record stock per slot at each visit
            - Estimate sales since the last visit
            - Generate a pick list per route for the van
            - Prioritise machines likely to be empty
            - Show revenue and margin per machine
API:        REST
            POST /machines/{id}/visits
            GET  /routes/{id}/picklist
            GET  /reports/machines
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 195

**Intent:**
small furniture workshop custom orders: customer picks wood, size, finish, we track production steps

**Spec:**
```
Type:       Web application (custom orders)
Auth:       Workshop staff login; customers view order status by link
Data model: Design(id, name, base_price)
            CustomOrder(id, design_id -> Design, customer_name, email, wood, width_cm, depth_cm, finish, price, deposit_paid, status)
            ProductionStep(id, order_id -> CustomOrder, step, done_at, worker)
Features:   - Configure a design with wood, size and finish
            - Calculate the price from size and material
            - Take a 50% deposit
            - Track cutting, joinery, sanding, finishing and delivery
            - Send customers progress photos
API:        REST
            GET  /designs/{id}/price
            POST /orders
            POST /orders/{id}/steps
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe
```

---

## Example 196

**Intent:**
soap making business needs batch records - which ingredient lots went in each batch for traceability

**Spec:**
```
Type:       Web application (batch traceability)
Auth:       Maker login (email + password)
Data model: Ingredient(id, name, supplier)
            IngredientLot(id, ingredient_id -> Ingredient, lot_no, quantity_g, received_on, expiry)
            Recipe(id, name, ingredients_json)
            Batch(id, recipe_id -> Recipe, batch_no, made_on, cure_until, units)
            BatchInput(batch_id -> Batch, lot_id -> IngredientLot, quantity_g)
Features:   - Receive ingredient lots with expiry dates
            - Record a batch and the lots used
            - Reduce lot stock automatically
            - Trace which batches used a given lot
            - Print batch labels with cure date
API:        REST
            POST /lots
            POST /batches
            GET  /lots/{id}/batches
Storage:    SQLite
Tech stack: Python, Flask, Jinja2
```

---

## Example 197

**Intent:**
3d printing service: upload STL, get price based on volume and material, order

**Spec:**
```
Type:       Web application (instant quote)
Auth:       Customer login (email + password); operator login
Data model: Material(id, name, price_per_cm3, colours)
            PrintOrder(id, customer_id -> Customer, stl_url, volume_cm3, material_id -> Material, colour, quantity, price, status)
            Customer(id, name, email, address)
Features:   - Upload STL files and show a 3D preview
            - Calculate model volume and bounding box
            - Quote a price from volume, material and quantity
            - Pay and place the order
            - Track the print queue and shipping
API:        REST
            POST /quotes
            POST /orders
            PATCH /orders/{id}/status
Storage:    PostgreSQL, S3 (STL files)
Tech stack: Python, FastAPI, trimesh, Three.js, Stripe
```

---

## Example 198

**Intent:**
tyre shop: book fitting, and we also store customers' winter tyres in our warehouse

**Spec:**
```
Type:       Web application (tyre fitting and storage)
Auth:       Staff login; customers book with email confirmation
Data model: Customer(id, name, phone, email)
            Car(id, customer_id -> Customer, plate, tyre_size)
            Fitting(id, car_id -> Car, starts_at, type, status)
            TyreSet(id, car_id -> Car, season, tread_mm, rack_location, stored_since)
Features:   - Book a fitting slot online
            - Register stored tyre sets with rack location
            - Pull the tyre list for tomorrow's fittings
            - Remind customers in spring and autumn to swap tyres
            - Warn when stored tyres are below legal tread
API:        REST
            POST /fittings
            POST /tyre-sets
            GET  /tyre-sets/pull?date={date}
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 199

**Intent:**
taxi company with 12 cars needs dispatch, customers call or book on web

**Spec:**
```
Type:       Web application (taxi dispatch)
Auth:       Dispatcher and driver login; customers book with phone verification
Data model: Driver(id, name, phone, car_plate, status, latitude, longitude)
            Ride(id, customer_phone, pickup_address, dropoff_address, pickup_at, driver_id -> Driver, fare, status)
Features:   - Book rides on the web or enter phone bookings
            - Suggest the nearest free driver
            - Send the ride to the driver's phone to accept
            - Track driver positions on a live map
            - Text customers the car plate when dispatched
API:        REST + WebSocket
            POST /rides
            POST /rides/{id}/assign
            POST /drivers/me/location
            WS   /dispatch
Storage:    PostgreSQL with PostGIS, Redis (live positions)
Tech stack: Node.js, NestJS, React, Leaflet, Twilio
```

---

## Example 200

**Intent:**
walking tours company, guides and tour dates, tourists buy tickets, guide sees head count

**Spec:**
```
Type:       Web application (tour booking)
Auth:       Guide and admin login; tourists book as guests
Data model: Tour(id, name, language, duration_min, price, meeting_point)
            Departure(id, tour_id -> Tour, guide_id -> Guide, starts_at, capacity)
            Guide(id, name, languages)
            TourBooking(id, departure_id -> Departure, name, email, people, paid)
Features:   - List tours by language and date
            - Buy tickets for a departure with capacity limits
            - Assign guides who speak the tour language
            - Show guides the head count and names
            - Cancel and refund departures below 2 people
API:        REST
            GET  /departures?date={date}&lang={code}
            POST /bookings
            GET  /guides/me/departures
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 201

**Intent:**
surf school lesons booking, depends on tides n weather so sometimes we cancel

**Spec:**
```
Type:       Web application (lesson booking)
Auth:       Instructor login; students book with email confirmation
Data model: LessonSlot(id, starts_at, level, capacity, instructor, status)
            Student(id, name, email, phone, swim_ability)
            LessonBooking(id, slot_id -> LessonSlot, student_id -> Student, wetsuit_size, paid)
Features:   - Show lesson slots fitted around the tide times
            - Book a group or private lesson with wetsuit size
            - Cancel a slot for bad conditions and notify all students
            - Offer rebooking or refund after a cancellation
            - Show instructors their students for the day
API:        REST
            GET  /slots?date={date}
            POST /bookings
            POST /slots/{id}/cancel
Storage:    PostgreSQL
Tech stack: Python, Django, WorldTides API, Stripe
```

---

## Example 202

**Intent:**
dive centre needs to check divers certification level before they book a dive trip

**Spec:**
```
Type:       Web application (dive trip booking)
Auth:       Diver login (email + password); staff login
Data model: Diver(id, name, email, cert_agency, cert_level, cert_card_url, last_dive_on)
            DiveTrip(id, site, starts_at, min_cert_level, max_depth_m, spaces)
            TripBooking(id, trip_id -> DiveTrip, diver_id -> Diver, rental_gear, status)
Features:   - Upload a certification card when registering
            - Only allow bookings that match the trip's minimum level
            - Suggest a refresher for divers inactive over a year
            - Add rental gear sizes to the booking
            - Print the boat manifest for each trip
API:        REST
            POST /divers/me/certification
            POST /trips/{id}/book
            GET  /trips/{id}/manifest
Storage:    PostgreSQL, S3 (certification cards)
Tech stack: Node.js, Express, Vue.js
```

---

## Example 203

**Intent:**
I have 4 holiday cottages by the sea. Right now my sister manages bookings in a paper diary and we've double booked twice this summer which was embarrassing. Want a site where guests can see availability for each cottage and book Saturday to Saturday in high season, any nights otherwise, plus a calendar sync with Airbnb so it doesn't happen again.

**Spec:**
```
Type:       Web application (holiday rental bookings)
Auth:       Owner login; guests book without an account
Data model: Cottage(id, name, sleeps, pets_allowed, base_price)
            SeasonRule(id, start_date, end_date, changeover_day, min_nights, weekly_price)
            Booking(id, cottage_id -> Cottage, guest_name, email, arrival, departure, total, source, status)
            ExternalCalendar(id, cottage_id -> Cottage, ical_url, last_synced)
Features:   - Show an availability calendar per cottage
            - Enforce Saturday changeovers in high season
            - Import Airbnb bookings from iCal feeds every 15 minutes
            - Export an iCal feed for each cottage
            - Take a deposit and the balance 6 weeks before arrival
API:        REST
            GET  /cottages/{id}/availability?month={month}
            POST /bookings
            GET  /cottages/{id}/calendar.ics
Storage:    PostgreSQL
Tech stack: Python, Django, icalendar, Stripe
```

---

## Example 204

**Intent:**
B&B guests choose their breakfast the night before on their phone

**Spec:**
```
Type:       Web application (breakfast ordering)
Auth:       Guests use a per-room QR link; owner login
Data model: Room(id, number, access_token)
            BreakfastItem(id, name, category, available)
            BreakfastOrder(id, room_id -> Room, date, serve_time, guests, notes)
            BreakfastOrderItem(order_id -> BreakfastOrder, item_id -> BreakfastItem, quantity)
Features:   - Open the breakfast menu from a QR code in the room
            - Choose dishes and a serving time for tomorrow
            - Close ordering at 9pm
            - Print the kitchen sheet for the morning
API:        REST
            GET  /rooms/{token}/menu
            POST /rooms/{token}/orders
            GET  /kitchen/sheet?date={date}
Storage:    SQLite
Tech stack: Python, Flask, Alpine.js
```

---

## Example 205

**Intent:**
airbnb cleaning turnovers: when a guest checks out, a cleaner gets assigned and does a checklist with photos

**Spec:**
```
Type:       Web application (turnover management)
Auth:       Host and cleaner login (email + password)
Data model: Listing(id, name, address, ical_url, checklist_template)
            Turnover(id, listing_id -> Listing, date, cleaner_id -> Cleaner, status, completed_at)
            Cleaner(id, name, phone, rate)
            ChecklistItem(id, turnover_id -> Turnover, task, done, photo_url)
Features:   - Read checkouts from each listing's booking calendar
            - Create a turnover job for every checkout
            - Assign cleaners and notify them by SMS
            - Complete the checklist with required photos
            - Report damage or low supplies to the host
API:        REST
            GET  /cleaners/me/turnovers
            PATCH /checklist-items/{id}
            POST /turnovers/{id}/complete
Storage:    PostgreSQL, S3 (photos)
Tech stack: TypeScript, NestJS, React (PWA), Twilio
```

---

## Example 206

**Intent:**
student housing, allocate rooms to students based on their preferences

**Spec:**
```
Type:       Web application (room allocation)
Auth:       Student login via university email; housing officer login
Data model: Building(id, name)
            HousingRoom(id, building_id -> Building, number, type, price, gender_restriction)
            Application(id, student_id -> Student, preferences_json, roommate_request, submitted_at)
            Student(id, name, email, year, gender)
            Allocation(id, application_id -> Application, room_id -> HousingRoom, status)
Features:   - Submit ranked room-type preferences and a roommate request
            - Allocate rooms automatically by priority and preference
            - Pair mutual roommate requests
            - Let students accept or decline their offer
            - Show occupancy per building
API:        REST
            POST /applications
            POST /allocations/run
            POST /allocations/{id}/respond
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 207

**Intent:**
property inspection reports for letting agent, room by room with photos and condition

**Spec:**
```
Type:       Web application (inspection reports)
Auth:       Inspector login (email + password)
Data model: Property(id, address, landlord_email)
            Inspection(id, property_id -> Property, type, inspected_on, inspector, tenant_signature_url)
            RoomReport(id, inspection_id -> Inspection, room, condition, notes)
            InspectionPhoto(id, room_report_id -> RoomReport, url)
Features:   - Run check-in, mid-term and check-out inspections
            - Rate the condition of each room with notes and photos
            - Compare check-out with check-in side by side
            - Collect the tenant's signature on screen
            - Email a PDF report to landlord and tenant
API:        REST
            POST /inspections
            POST /inspections/{id}/rooms
            GET  /inspections/{id}/compare
Storage:    PostgreSQL, S3 (photos)
Tech stack: Vue.js (PWA), Node.js, Express, Puppeteer
```

---

## Example 208

**Intent:**
letting agency tenant applications with referencing and right to rent checks

**Spec:**
```
Type:       Web application (tenant applications)
Auth:       Applicant login (email + password); agent login
Data model: Listing(id, address, rent)
            Applicant(id, name, email, phone, employer, income)
            TenancyApplication(id, listing_id -> Listing, applicant_id -> Applicant, status, submitted_at)
            Reference(id, application_id -> TenancyApplication, type, referee_email, response, received_at)
            IdDocument(id, applicant_id -> Applicant, type, url, verified)
Features:   - Apply for a listing online
            - Email employer and previous landlord reference forms
            - Upload ID for right to rent checks
            - Check income is at least 30 times monthly rent
            - Show agents the status of each application
API:        REST
            POST /listings/{id}/applications
            POST /references/{token}
            PATCH /applications/{id}
Storage:    PostgreSQL, S3 (ID documents, encrypted)
Tech stack: Ruby on Rails, Active Storage, Postmark
```

---

## Example 209

**Intent:**
commercial units, track leases, rent reviews and break dates for our landlord company

**Spec:**
```
Type:       Web application (lease management)
Auth:       Staff login with SSO
Data model: Unit(id, address, size_sqft, use_class)
            Tenant(id, company, contact_email)
            Lease(id, unit_id -> Unit, tenant_id -> Tenant, start_date, end_date, annual_rent, break_date, review_date)
            RentInvoice(id, lease_id -> Lease, quarter, amount, paid)
Features:   - Record leases with rent, break and review dates
            - Alert staff 6 months before breaks and reviews
            - Raise quarterly rent invoices
            - Show vacant units and rent roll
            - Report arrears per tenant
API:        REST
            GET  /leases?event_within=180
            POST /invoices/quarterly
            GET  /reports/rent-roll
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, React
```

---

## Example 210

**Intent:**
makerspace members can only use laser cutter after induction, book machine time

**Spec:**
```
Type:       Web application (equipment booking)
Auth:       Member login (email + password); trainer role
Data model: Member(id, name, email, membership_status)
            Machine(id, name, requires_induction, hourly_fee)
            Induction(id, member_id -> Member, machine_id -> Machine, trainer, passed_on)
            MachineBooking(id, machine_id -> Machine, member_id -> Member, starts_at, ends_at)
Features:   - Book machine time in 30-minute blocks
            - Allow booking only after a passed induction
            - Let trainers record inductions
            - Charge hourly fees for some machines
            - Show a usage log per machine
API:        REST
            POST /bookings
            POST /inductions
            GET  /machines/{id}/usage
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 211

**Intent:**
reservation for recording studio w/ engineer, they pay half upfront

**Spec:**
```
Type:       Web application (studio booking)
Auth:       Client login (email + password); studio admin
Data model: Studio(id, name, hourly_rate)
            Engineer(id, name, hourly_rate)
            StudioBooking(id, studio_id -> Studio, engineer_id -> Engineer, client_id -> Client, starts_at, hours, total, deposit_paid)
            Client(id, name, email, artist_name)
Features:   - Book a studio with or without an engineer
            - Calculate the price from room and engineer rates
            - Take 50% deposit at booking
            - Send the balance invoice after the session
            - Share session files with the client after the session
API:        REST
            GET  /availability?date={date}
            POST /bookings
            POST /bookings/{id}/files
Storage:    PostgreSQL, S3 (session files)
Tech stack: Node.js, NestJS, Next.js, Stripe
```

---

## Example 212

**Intent:**
photo booth rental for parties, check dates, choose backdrop, get gallery link after

**Spec:**
```
Type:       Web application (equipment hire)
Auth:       Owner login; customers book as guests
Data model: Booth(id, name, type)
            Backdrop(id, name, image_url)
            Hire(id, booth_id -> Booth, backdrop_id -> Backdrop, event_date, venue, hours, customer_email, total)
            EventGallery(id, hire_id -> Hire, url, access_code)
Features:   - Check booth availability for an event date
            - Choose a backdrop and print template
            - Pay a deposit to secure the date
            - Share an online gallery of the night's photos
API:        REST
            GET  /availability?date={date}
            POST /hires
            POST /hires/{id}/gallery
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Flask, Stripe
```

---

## Example 213

**Intent:**
i manage a few bands and venues email me for bookings, need a shared calendar and contracts

**Spec:**
```
Type:       Web application (booking agency)
Auth:       Agent login; band members read-only login
Data model: Band(id, name, fee_min, members)
            Venue(id, name, city, contact_email)
            Gig(id, band_id -> Band, venue_id -> Venue, date, fee, status)
            Contract(id, gig_id -> Gig, pdf_url, signed_at)
Features:   - Keep one calendar of holds and confirmed gigs per band
            - Prevent double-booking a band on the same date
            - Generate a performance contract from a template
            - Collect e-signatures from the venue
            - Show band members their upcoming gigs
API:        REST
            POST /gigs
            POST /gigs/{id}/contract
            GET  /bands/{id}/calendar
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Dropbox Sign API
```

---

## Example 214

**Intent:**
Bonjour, I have a small wedding venue (castle) and want manage the enquiries, visits and the date reservations, with payment in 3 parts.

**Spec:**
```
Type:       Web application (venue sales)
Auth:       Venue staff login (email + password)
Data model: Enquiry(id, couple_names, email, phone, wished_date, guests, source, status)
            SiteVisit(id, enquiry_id -> Enquiry, visit_at, notes)
            DateReservation(id, enquiry_id -> Enquiry, event_date, package, total_price)
            Instalment(id, reservation_id -> DateReservation, amount, due_date, paid_at)
Features:   - Collect enquiries from the website form
            - Schedule site visits with couples
            - Hold a date and convert it into a reservation
            - Split the price into 3 instalments with due dates
            - Remind couples before each instalment is due
API:        REST
            POST /enquiries
            POST /enquiries/{id}/visits
            POST /reservations
            GET  /instalments?due_before={date}
Storage:    PostgreSQL
Tech stack: PHP, Symfony, Stripe
```

---

## Example 215

**Intent:**
conference centre with 6 rooms, companies book rooms plus catering and AV

**Spec:**
```
Type:       Web application (venue booking)
Auth:       Client login (email + password); events team login
Data model: MeetingRoom(id, name, capacity, layouts, day_rate)
            Extra(id, name, type, price)
            Event(id, client_company, contact_email, date, room_id -> MeetingRoom, layout, attendees, status)
            EventExtra(event_id -> Event, extra_id -> Extra, quantity)
Features:   - Check room availability by date and capacity
            - Choose a room layout (theatre, boardroom, cabaret)
            - Add catering and AV equipment
            - Send a proposal and confirm on acceptance
            - Produce a daily function sheet for staff
API:        REST
            GET  /rooms/availability?date={date}&people={n}
            POST /events
            GET  /function-sheet?date={date}
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 216

**Intent:**
customer feedback after each visit to our salon, short survey by sms, show me ratings

**Spec:**
```
Type:       Web application (feedback surveys)
Auth:       Owner login (email + password)
Data model: Visit(id, customer_phone, stylist, visited_at)
            SurveyResponse(id, visit_id -> Visit, rating, comment, submitted_at)
Features:   - Send an SMS survey link 2 hours after each visit
            - Collect a 1-5 rating and optional comment
            - Ask happy customers to leave a Google review
            - Alert the owner about ratings of 2 or lower
            - Show average rating per stylist per month
API:        REST
            POST /visits
            GET  /survey/{token}
            POST /survey/{token}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Twilio, Chart.js
```

---

## Example 217

**Intent:**
need a CRM in hubspot style but simple, for my 3 person solar panel installer company, leads > site survey > quote > install

**Spec:**
```
Type:       Web application (sales pipeline)
Auth:       Team login (email + password)
Data model: Lead(id, name, phone, email, address, roof_type, monthly_bill, stage, owner_id -> User)
            SiteSurvey(id, lead_id -> Lead, date, roof_area_m2, orientation, shading, photos)
            SolarQuote(id, lead_id -> Lead, panels, kwp, inverter, price, status)
            Installation(id, lead_id -> Lead, install_date, crew, completed)
            User(id, name, email)
Features:   - Move leads through stages on a pipeline board
            - Record site survey details and roof photos
            - Estimate system size from roof area and energy bill
            - Send quotes and track acceptance
            - Schedule installs on a crew calendar
API:        REST
            PATCH /leads/{id}/stage
            POST /leads/{id}/survey
            POST /leads/{id}/quotes
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma, Tailwind CSS
```

---

## Example 218

**Intent:**
locksmith callouts, price depends on time of day and distance

**Spec:**
```
Type:       Web application (callout jobs)
Auth:       Locksmith login; customers request with phone number
Data model: Callout(id, customer_name, phone, address, latitude, longitude, problem, requested_at, price, status)
            PriceRule(id, day_type, start_hour, end_hour, base_fee, per_km)
Features:   - Request an emergency callout with location
            - Quote a price from time of day and distance
            - Accept the job and send an ETA by SMS
            - Take card payment on completion
            - Show monthly callout income
API:        REST
            POST /callouts
            GET  /callouts/{id}/quote
            POST /callouts/{id}/accept
Storage:    SQLite
Tech stack: Python, Flask, OpenRouteService, Twilio, Stripe
```

---

## Example 219

**Intent:**
we run a pool cleaning service, weekly visits, log chemical readings for each pool

**Spec:**
```
Type:       Web application (service logs)
Auth:       Technician and owner login (email + password); customer view link
Data model: Pool(id, owner_name, address, volume_litres, type)
            ServiceVisit(id, pool_id -> Pool, technician, visited_at)
            ChemReading(id, visit_id -> ServiceVisit, ph, chlorine_ppm, alkalinity, chemicals_added)
Features:   - Show each technician's weekly route
            - Record pH, chlorine and alkalinity at each visit
            - Suggest chemical doses from readings and pool volume
            - Email the customer a visit summary
            - Chart readings over time per pool
API:        REST
            GET  /technicians/me/route
            POST /pools/{id}/visits
            GET  /pools/{id}/readings
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Chart.js
```

---

## Example 220

**Intent:**
small car dealer, list used cars on website, track costs of preparing each car and profit

**Spec:**
```
Type:       Web application (dealer stock)
Auth:       Dealer staff login; public listing pages
Data model: Car(id, make, model, year, mileage, vin, purchase_price, list_price, status)
            PrepCost(id, car_id -> Car, description, amount)
            CarPhoto(id, car_id -> Car, url, position)
            CarSale(id, car_id -> Car, sold_price, sold_on, buyer_name)
Features:   - Publish cars with photos to the website
            - Record preparation costs per car
            - Calculate profit when a car is sold
            - Show days in stock for each car
            - Capture enquiries from the listing page
API:        REST
            GET  /cars?make={m}&max_price={p}
            POST /cars/{id}/costs
            POST /cars/{id}/sell
Storage:    PostgreSQL, S3 (photos)
Tech stack: PHP, Laravel, Livewire
```

---

## Example 221

**Intent:**
airport shuttle bookings, shared rides, group passengers by flight time

**Spec:**
```
Type:       Web application (shuttle booking)
Auth:       Admin and driver login; passengers book as guests
Data model: ShuttleBooking(id, name, email, phone, direction, flight_no, flight_time, address, passengers, price)
            ShuttleRun(id, vehicle_id -> Vehicle, driver, departs_at)
            Vehicle(id, plate, seats)
            RunStop(run_id -> ShuttleRun, booking_id -> ShuttleBooking, order)
Features:   - Book a seat to or from the airport with flight number
            - Group bookings into runs by time and area
            - Respect vehicle seat limits
            - Send drivers the ordered list of pickups
            - Text passengers their pickup time the evening before
API:        REST
            POST /bookings
            POST /runs/plan?date={date}
            GET  /runs/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Google OR-Tools, Twilio
```

---

## Example 222

**Intent:**
ski rental shop, customers reserve skis online with height weight and level so its ready when they arrive

**Spec:**
```
Type:       Web application (rental reservations)
Auth:       Shop staff login; customers reserve as guests
Data model: RentalReservation(id, lead_name, email, start_date, days, status)
            Skier(id, reservation_id -> RentalReservation, name, height_cm, weight_kg, shoe_size, level, package)
            Equipment(id, type, size, serial_no, available)
            Assignment(skier_id -> Skier, equipment_id -> Equipment)
Features:   - Reserve packages for each skier in a group
            - Recommend ski length and DIN setting from height, weight and level
            - Prepare a fitting list for the next day
            - Assign specific equipment at pickup
            - Discount longer rentals automatically
API:        REST
            POST /reservations
            GET  /fitting-list?date={date}
            POST /skiers/{id}/assign
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 223

**Intent:**
kayak tour bookings with life jacket sizes and weight limits per kayak

**Spec:**
```
Type:       Web application (tour booking)
Auth:       Guide login; customers book as guests
Data model: Tour(id, name, starts_at, max_kayaks, price)
            Kayak(id, type, seats, max_weight_kg)
            TourBooking(id, tour_id -> Tour, lead_email, total, paid)
            Paddler(id, booking_id -> TourBooking, name, weight_kg, jacket_size, kayak_id -> Kayak)
Features:   - Book a tour for a group of paddlers
            - Collect weight and life jacket size per paddler
            - Pair paddlers into kayaks within weight limits
            - Show guides the kayak plan before departure
API:        REST
            GET  /tours?date={date}
            POST /bookings
            GET  /tours/{id}/kayak-plan
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Svelte, Stripe
```

---

## Example 224

**Intent:**
fishing charter boat, book whole boat or single seat on shared trips

**Spec:**
```
Type:       Web application (charter booking)
Auth:       Captain login; anglers book with email confirmation
Data model: Trip(id, starts_at, hours, type, seats, private_price, seat_price)
            CharterBooking(id, trip_id -> Trip, name, email, seats, is_private, total, deposit_paid)
Features:   - Book the whole boat or single seats on shared trips
            - Block seat bookings once a trip is booked privately
            - Take a deposit with the balance on the day
            - Cancel for weather and offer a new date
API:        REST
            GET  /trips?month={month}
            POST /bookings
            POST /trips/{id}/cancel
Storage:    SQLite
Tech stack: Ruby, Sinatra, Stripe
```

---

## Example 225

**Intent:**
coach company day trips, seats on a coach, pickup points along the route

**Spec:**
```
Type:       Web application (coach trips)
Auth:       Office login; customers book as guests or with account
Data model: DayTrip(id, destination, date, price, coach_seats)
            PickupPoint(id, trip_id -> DayTrip, place, time)
            TripBooking(id, trip_id -> DayTrip, pickup_point_id -> PickupPoint, name, phone, seats, total)
            SeatAssignment(booking_id -> TripBooking, seat_no)
Features:   - Show upcoming day trips with seats left
            - Choose a pickup point and seats on a coach plan
            - Pay online or reserve and pay by phone
            - Print the driver a passenger list per pickup point
            - Cancel trips that don't reach minimum numbers
API:        REST
            GET  /trips
            GET  /trips/{id}/seats
            POST /bookings
            GET  /trips/{id}/manifest
Storage:    MySQL
Tech stack: PHP, Laravel, Vue.js
```

---

## Example 226

**Intent:**
chauffeur service bookings for weddings and airport, quote by distance

**Spec:**
```
Type:       Web application (chauffeur booking)
Auth:       Admin login; clients book with email confirmation
Data model: Vehicle(id, model, class, seats, rate_per_km, min_fare)
            Chauffeur(id, name, phone)
            Journey(id, vehicle_id -> Vehicle, chauffeur_id -> Chauffeur, pickup, dropoff, pickup_at, distance_km, waiting_hours, price, status)
Features:   - Quote journeys from distance and vehicle class
            - Add waiting time for weddings
            - Assign a chauffeur and vehicle
            - Send the client chauffeur details the day before
            - Show the week's journeys on a calendar
API:        REST
            POST /quotes
            POST /journeys
            PATCH /journeys/{id}/assign
Storage:    PostgreSQL
Tech stack: Python, Django, Google Maps Distance Matrix API
```

---

## Example 227

**Intent:**
i want an excel replacment for my cattering company, events, menus, staff needed, ingredients to buy

**Spec:**
```
Type:       Web application (catering management)
Auth:       Staff login (email + password)
Data model: CateringEvent(id, client, date, venue, guests, menu_id -> Menu, staff_needed, status)
            Menu(id, name, price_per_head)
            Dish(id, name, portions_per_batch)
            MenuDish(menu_id -> Menu, dish_id -> Dish)
            DishIngredient(dish_id -> Dish, ingredient, quantity, unit)
Features:   - Plan events with menu, guest count and venue
            - Scale dish recipes to the number of guests
            - Build a combined shopping list for the week's events
            - Calculate staff needed from guest numbers
            - Show the event calendar
API:        REST
            POST /events
            GET  /shopping-list?week={date}
            GET  /events/{id}/staffing
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 228

**Intent:**
office lunch orders from a local cafe, everyone picks before 11 and one person collects

**Spec:**
```
Type:       Web application (group ordering)
Auth:       Company Google SSO
Data model: LunchDay(id, date, cafe, cutoff_at, collector_id -> User)
            LunchItem(id, name, price)
            LunchOrder(id, lunch_day_id -> LunchDay, user_id -> User, item_id -> LunchItem, note, paid)
            User(id, name, email)
Features:   - Pick a lunch from the cafe menu before 11:00
            - Send one combined order to the cafe by email
            - Rotate the collector role between colleagues
            - Track who owes the collector money
API:        REST
            GET  /today
            POST /orders
            POST /days/{id}/send
Storage:    SQLite
Tech stack: Node.js, Express, HTMX
```

---

## Example 229

**Intent:**
factory canteen, workers pay with their badge and we deduct from wages monthly

**Spec:**
```
Type:       Web application (canteen payments)
Auth:       Cashier login on the till; HR admin login
Data model: Worker(id, name, badge_id, payroll_no, monthly_limit)
            CanteenItem(id, name, price)
            Purchase(id, worker_id -> Worker, total, purchased_at)
            PurchaseLine(purchase_id -> Purchase, item_id -> CanteenItem, quantity)
Features:   - Scan a worker's badge at the till
            - Record purchases against the worker
            - Block purchases above the monthly limit
            - Export monthly totals for payroll deductions
            - Let workers see their own spending
API:        REST
            POST /purchases
            GET  /workers/{badge}/balance
            GET  /payroll/export?month={month}
Storage:    SQL Server
Tech stack: C#, ASP.NET Core, Blazor, RFID badge reader
```

---

## Example 230

**Intent:**
cleaning supplies distributor: sales reps visit shops and take orders on a tablet, even offline

**Spec:**
```
Type:       Web application (field sales ordering)
Auth:       Sales rep login (email + password)
Data model: Shop(id, name, address, rep_id -> Rep, price_group)
            Product(id, sku, name, price_group_prices)
            SalesOrder(id, shop_id -> Shop, rep_id -> Rep, created_at, synced, total)
            SalesOrderLine(order_id -> SalesOrder, product_id -> Product, quantity)
            Rep(id, name, email)
Features:   - Show each rep their shops and visit plan
            - Take orders offline and sync when back online
            - Apply each shop's price group
            - Suggest reorder quantities from past orders
            - Send orders to the warehouse system
API:        REST
            GET  /reps/me/shops
            POST /orders/sync
            GET  /products
Storage:    PostgreSQL (server), IndexedDB (offline on tablet)
Tech stack: TypeScript, React (PWA), Workbox, NestJS
```

---

## Example 231

**Intent:**
small factory that makes metal parts, production orders, which machine, how many made, scrap

**Spec:**
```
Type:       Web application (production tracking)
Auth:       Operator login (badge + PIN); planner login
Data model: PartNumber(id, code, description, cycle_time_sec)
            ProductionOrder(id, part_id -> PartNumber, quantity, due_date, machine_id -> Machine, status)
            Machine(id, name, type)
            OutputLog(id, order_id -> ProductionOrder, good_qty, scrap_qty, scrap_reason, logged_at)
Features:   - Plan production orders on machines
            - Let operators log good parts and scrap per shift
            - Show progress of each order against quantity
            - Report scrap rate by reason and machine
            - Estimate finish time from cycle time
API:        REST
            POST /orders
            POST /orders/{id}/output
            GET  /reports/scrap?from={date}
Storage:    PostgreSQL
Tech stack: Python, Django, Plotly
```

---

## Example 232

**Intent:**
t-shirt printing orders, customer uploads logo, picks shirt colours and sizes, we approve a mockup

**Spec:**
```
Type:       Web application (custom print orders)
Auth:       Customer login (email + password); staff login
Data model: Garment(id, style, colours, base_price)
            PrintOrder(id, customer_id -> Customer, garment_id -> Garment, colour, logo_url, print_position, status, total)
            SizeQuantity(order_id -> PrintOrder, size, quantity)
            Mockup(id, order_id -> PrintOrder, image_url, approved_at)
            Customer(id, name, email)
Features:   - Upload a logo and place it on a shirt preview
            - Enter quantities per size
            - Price by quantity breaks and print colours
            - Send a mockup for customer approval
            - Start production only after approval and payment
API:        REST
            POST /orders
            POST /orders/{id}/mockups
            POST /mockups/{id}/approve
Storage:    PostgreSQL, S3 (artwork)
Tech stack: Node.js, Express, Fabric.js, Stripe
```

---

## Example 233

**Intent:**
trophy and engraving shop online orders with text per trophy

**Spec:**
```
Type:       Web application (engraving orders)
Auth:       Shop admin login; customers order as guests
Data model: TrophyModel(id, name, height_cm, price, max_lines)
            EngravingOrder(id, customer_email, club_name, needed_by, total, status)
            OrderTrophy(id, order_id -> EngravingOrder, model_id -> TrophyModel, engraving_lines)
Features:   - Order trophies with engraving text for each one
            - Limit engraving to the model's line count
            - Upload engraving lists from a spreadsheet for big orders
            - Email the customer a proof before engraving
            - Show orders by needed-by date
API:        REST
            POST /orders
            POST /orders/{id}/import
            POST /orders/{id}/approve-proof
Storage:    PostgreSQL
Tech stack: Python, Django, openpyxl
```

---

## Example 234

**Intent:**
MOT test centre online booking, also remind people next year

**Spec:**
```
Type:       Web application (MOT booking)
Auth:       Staff login; customers book with email confirmation
Data model: Vehicle(id, reg, make, model, mot_expiry, owner_email)
            MotSlot(id, starts_at, bay)
            MotBooking(id, slot_id -> MotSlot, vehicle_id -> Vehicle, result, advisories)
Features:   - Book an MOT slot by registration number
            - Look up the current MOT expiry date from the DVSA API
            - Record pass, fail and advisories
            - Email a reminder a month before next year's MOT
            - Offer a free retest within 10 days after a fail
API:        REST
            GET  /vehicles/{reg}/mot
            POST /bookings
            PATCH /bookings/{id}/result
Storage:    PostgreSQL
Tech stack: Python, Django, DVSA MOT History API, Celery
```

---

## Example 235

**Intent:**
my brother has a kebab shop and a small delivery area, he wants whatsapp orders to go in a system, not a notepad

**Spec:**
```
Type:       Bot (WhatsApp ordering)
Data model: Customer(id, whatsapp_number, name, address)
            MenuItem(id, name, price, options)
            WhatsappOrder(id, customer_id -> Customer, items_json, total, status, created_at)
Features:   - Reply with the menu when a customer messages
            - Take orders through numbered menu choices
            - Save the customer's address for next time
            - Show incoming orders on a kitchen tablet page
            - Message the customer when the order leaves
API:        REST
            POST /whatsapp/webhook
            GET  /orders?status=new
            PATCH /orders/{id}/status
Storage:    PostgreSQL
Tech stack: Node.js, Express, WhatsApp Cloud API
```

---

## Example 236

**Intent:**
Hi! We are 2 dentists in Poland. We want patients see free hours and book, and also remember them with SMS one day before, because many forget. Also the system in Polish language please.

**Spec:**
```
Type:       Web application (booking system)
Auth:       Patient login by phone + SMS code; dentist and receptionist login
Data model: Dentist(id, name, working_hours)
            Patient(id, name, phone, email, pesel)
            Visit(id, patient_id -> Patient, dentist_id -> Dentist, starts_at, duration_min, type, status)
Features:   - Show free hours per dentist and visit type
            - Book and cancel visits online
            - Send SMS reminders one day before
            - Let patients confirm or cancel by replying to the SMS
            - Show the whole interface in Polish
API:        REST
            GET  /dentists/{id}/free?date={date}
            POST /visits
            POST /sms/inbound
Storage:    PostgreSQL
Tech stack: Python, Django (i18n, Polish locale), SMSAPI.pl
```

---

## Example 237

**Intent:**
gym trainers and class instructors get paid per class, need monthly payout report

**Spec:**
```
Type:       Web application (instructor payroll)
Auth:       Admin login; instructors view their own report
Data model: Instructor(id, name, email, rate_per_class, rate_per_attendee)
            GymClass(id, instructor_id -> Instructor, name, starts_at, attendees)
            Payout(id, instructor_id -> Instructor, month, amount, paid_on)
Features:   - Import classes and attendance from the booking system
            - Pay a base rate per class plus a bonus per attendee
            - Generate a monthly payout report per instructor
            - Let instructors check their classes before payout
            - Export payouts as a bank CSV file
API:        REST
            POST /classes/import
            GET  /instructors/{id}/payout?month={month}
            GET  /payouts/export?month={month}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, pandas
```

---

## Example 238

**Intent:**
customer accounts for regulars at our farm shop so they can pay at the end of the month

**Spec:**
```
Type:       Web application (tab accounts)
Auth:       Shop staff login; customers view statements by email link
Data model: AccountCustomer(id, name, email, phone, credit_limit)
            TabEntry(id, customer_id -> AccountCustomer, description, amount, created_at)
            Statement(id, customer_id -> AccountCustomer, month, total, paid_at)
Features:   - Add purchases to a customer's tab at the till
            - Stop new entries above the credit limit
            - Email monthly statements with a payment link
            - Mark statements paid
            - List customers with unpaid statements
API:        REST
            POST /customers/{id}/tab
            POST /statements/generate?month={month}
            GET  /statements?unpaid=true
Storage:    SQLite
Tech stack: Python, Flask, Stripe Payment Links
```

---

## Example 239

**Intent:**
egg delivery round, customers subscribe to half dozen or dozen each week

**Spec:**
```
Type:       Web application (delivery round)
Auth:       Farmer login; customers sign up with email
Data model: Subscriber(id, name, address, quantity, day, paid_until, active)
            Delivery(id, subscriber_id -> Subscriber, date, delivered)
Features:   - Sign up for weekly eggs and choose quantity
            - Pause deliveries while on holiday
            - Show the delivery list for each round day
            - Collect monthly payments
            - Track how many eggs are needed per week
API:        REST
            POST /subscribers
            POST /subscribers/{id}/pause
            GET  /rounds?date={date}
Storage:    SQLite
Tech stack: Ruby, Sinatra, Stripe
```

---

## Example 240

**Intent:**
build a gardening service CRM with recurring jobs (mowing every 2 weeks, hedges twice a year)

**Spec:**
```
Type:       Web application (field service CRM)
Auth:       Owner and crew login (email + password)
Data model: Customer(id, name, address, phone, notes)
            RecurringJob(id, customer_id -> Customer, task, interval_days, price, next_due)
            JobVisit(id, recurring_job_id -> RecurringJob, date, crew, done, invoiced)
Features:   - Set up recurring jobs with custom intervals
            - Generate the next visit when one is completed
            - Plan each crew's week
            - Invoice completed visits monthly
            - Pause jobs in winter
API:        REST
            POST /recurring-jobs
            POST /visits/{id}/complete
            GET  /crews/{id}/week?start={date}
Storage:    PostgreSQL
Tech stack: TypeScript, SvelteKit, Prisma
```

---

## Example 241

**Intent:**
cemetery plot register for the parish council with map and burial records

**Spec:**
```
Type:       Web application (cemetery records)
Auth:       Clerk login (email + password); public search without login
Data model: Plot(id, section, row, number, status, latitude, longitude)
            Burial(id, plot_id -> Plot, name, date_of_death, burial_date)
            PlotRight(id, plot_id -> Plot, holder_name, purchased_on, expires_on)
Features:   - Record burials and plot ownership rights
            - Show plots on a cemetery map coloured by status
            - Let the public search burials by name
            - Reserve plots for future use
            - Warn when exclusive rights are expiring
API:        REST
            GET  /burials?name={name}
            GET  /plots?section={s}
            POST /plots/{id}/burials
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django, Leaflet
```

---

## Example 242

**Intent:**
charity shop wants to track donated items and gift aid declarations

**Spec:**
```
Type:       Web application (donation tracking)
Auth:       Volunteer login (PIN); manager login
Data model: Donor(id, name, address, postcode, gift_aid_declared, declared_on)
            DonatedItem(id, donor_id -> Donor, tag_code, category, price, sold_on, sold_price)
            GiftAidClaim(id, period, total, submitted_on)
Features:   - Register donors and record gift aid declarations
            - Tag donated items with the donor's ID
            - Record sale prices at the till
            - Calculate gift aid due on sold items
            - Write to donors annually with their total raised
API:        REST
            POST /donors
            POST /items
            POST /items/{tag}/sell
            GET  /gift-aid?period={p}
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Bootstrap
```

---

## Example 243

**Intent:**
running club race entries with bib numbers and results

**Spec:**
```
Type:       Web application (race entries)
Auth:       Organiser login; runners enter as guests
Data model: Race(id, name, date, distance_km, entry_fee, max_entries)
            Entry(id, race_id -> Race, name, email, birth_date, gender, club, bib_number, paid)
            RaceResult(id, entry_id -> Entry, chip_time, position)
Features:   - Enter a race and pay online
            - Assign bib numbers in order
            - Close entries at the limit
            - Import chip timing results from CSV
            - Show results by category and gender
API:        REST
            POST /races/{id}/entries
            POST /races/{id}/results/import
            GET  /races/{id}/results
Storage:    PostgreSQL
Tech stack: Python, Flask, Stripe
```

---

## Example 244

**Intent:**
choir music library: who has which sheet music copies

**Spec:**
```
Type:       Web application (music library)
Auth:       Librarian login; members view their loans
Data model: Score(id, title, composer, arrangement, voicing, copies)
            Singer(id, name, voice_part, email)
            ScoreLoan(id, score_id -> Score, singer_id -> Singer, copy_no, issued_on, returned_on)
Features:   - Catalogue scores with number of copies
            - Issue numbered copies to singers
            - Show who still has copies after a concert
            - Search the library by composer or voicing
API:        REST
            GET  /scores?q={text}
            POST /loans
            GET  /scores/{id}/outstanding
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 245

**Intent:**
cycling club, members sign up for weekend rides by pace group

**Spec:**
```
Type:       Web application (ride signups)
Auth:       Member login (email + password); ride leader role
Data model: Ride(id, date, start_point, route_url, distance_km)
            PaceGroup(id, ride_id -> Ride, name, avg_speed, leader_id -> Member, max_riders)
            RideSignup(id, group_id -> PaceGroup, member_id -> Member)
            Member(id, name, email, emergency_contact)
Features:   - Publish weekend rides with GPX routes
            - Sign up for a pace group with limited places
            - Show leaders their riders' emergency contacts
            - Cancel rides for bad weather and notify riders
API:        REST
            GET  /rides
            POST /groups/{id}/signup
            POST /rides/{id}/cancel
Storage:    PostgreSQL
Tech stack: Node.js, Express, Leaflet
```

---

## Example 246

**Intent:**
darts league for local pubs, fixtures, results by leg, player averages

**Spec:**
```
Type:       Web application (league management)
Auth:       League secretary login; captains submit results
Data model: PubTeam(id, name, pub)
            Player(id, team_id -> PubTeam, name)
            Match(id, home_id -> PubTeam, away_id -> PubTeam, date, home_legs, away_legs)
            Leg(id, match_id -> Match, home_player_id -> Player, away_player_id -> Player, winner_id -> Player, darts_thrown, score)
Features:   - Generate a home and away fixture list
            - Enter results leg by leg
            - Calculate three-dart averages per player
            - Show the league table and top players
API:        REST
            POST /matches/{id}/legs
            GET  /table
            GET  /players/averages
Storage:    SQLite
Tech stack: Python, Flask, Jinja2
```

---

## Example 247

**Intent:**
cat cafe reservations, 1 hour visits, max 15 people, kids under 8 not allowed

**Spec:**
```
Type:       Web application (visit reservations)
Auth:       Staff login; visitors book as guests
Data model: VisitSlot(id, starts_at, capacity)
            Reservation(id, slot_id -> VisitSlot, name, email, adults, children_ages, paid)
            Cat(id, name, bio, photo_url, adoptable)
Features:   - Book a one-hour visit with up to 15 people per slot
            - Refuse bookings with children under 8
            - Charge the entry fee at booking
            - Show profiles of the cats and which are adoptable
API:        REST
            GET  /slots?date={date}
            POST /reservations
            GET  /cats
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Stripe
```

---

## Example 248

**Intent:**
distillery tour tickets plus gin bought at end gets added to their order

**Spec:**
```
Type:       Web application (tours and shop)
Auth:       Staff login; visitors book as guests
Data model: TourSlot(id, starts_at, capacity, price)
            TourBooking(id, slot_id -> TourSlot, name, email, guests, total)
            ShopProduct(id, name, price, stock)
            ShopSale(id, booking_id -> TourBooking, product_id -> ShopProduct, quantity)
Features:   - Sell tour tickets with age confirmation
            - Check in guests on arrival
            - Add shop purchases to the tour booking
            - Report shop revenue per tour
API:        REST
            POST /bookings
            POST /bookings/{id}/checkin
            POST /bookings/{id}/sales
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 249

**Intent:**
staff training quiz for new waiters about the menu, manager sees scores

**Spec:**
```
Type:       Web application (staff training)
Auth:       Staff and manager login (email + password)
Data model: Quiz(id, title, topic)
            QuizQuestion(id, quiz_id -> Quiz, text, options, answer)
            QuizAttempt(id, quiz_id -> Quiz, staff_id -> Staff, score, finished_at)
            Staff(id, name, email, start_date)
Features:   - Create quizzes about dishes, allergens and wines
            - Let staff take quizzes on their phone
            - Require a pass mark before the first shift
            - Show managers scores per staff member
API:        REST
            GET  /quizzes
            POST /quizzes/{id}/attempts
            GET  /reports/scores
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 250

**Intent:**
staff in our 3 shops count the cash at end of day and send it, I want to see if anything is missing

**Spec:**
```
Type:       Web application (cash-up reports)
Auth:       Shop manager and owner login
Data model: Shop(id, name)
            CashUp(id, shop_id -> Shop, date, counted_cash, card_total, pos_cash_total, variance, submitted_by)
            Banking(id, shop_id -> Shop, amount, banked_on, bag_number)
Features:   - Enter end-of-day counts by note and coin
            - Compare counted cash with the POS cash total
            - Flag variances above a set amount
            - Record bankings and match them to cash-ups
            - Show the owner a weekly variance report per shop
API:        REST
            POST /cashups
            POST /bankings
            GET  /reports/variance?week={date}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 251

**Intent:**
watch repair shop, send customer estimate and they approve online before we start

**Spec:**
```
Type:       Web application (repair estimates)
Auth:       Watchmaker login; customers approve via secure link
Data model: Customer(id, name, email, phone)
            Watch(id, customer_id -> Customer, brand, model, serial_no)
            RepairOrder(id, watch_id -> Watch, fault, estimate_amount, estimate_notes, status, received_on)
            Approval(id, repair_order_id -> RepairOrder, approved, responded_at)
Features:   - Log watches received with photos and serial number
            - Send an itemised estimate by email
            - Let the customer approve or decline online
            - Start work only on approved orders
            - Notify the customer when the watch is ready
API:        REST
            POST /repair-orders
            POST /repair-orders/{id}/estimate
            POST /approve/{token}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Postmark
```

---

## Example 252

**Intent:**
pawn shop loans tracker interest and due dates

**Spec:**
```
Type:       Web application (pawn loans)
Auth:       Staff login with 2FA
Data model: Customer(id, name, id_number, phone, address)
            PawnItem(id, description, category, valuation, photo_url, storage_bin)
            PawnLoan(id, customer_id -> Customer, item_id -> PawnItem, principal, monthly_rate, start_date, due_date, status)
            LoanPayment(id, loan_id -> PawnLoan, amount, paid_on)
Features:   - Create loans with item valuation and photo
            - Calculate interest due at any date
            - Record redemptions and extensions
            - List loans past due for forfeiture
            - Move forfeited items into sale stock
API:        REST
            POST /loans
            GET  /loans/{id}/payoff?date={date}
            POST /loans/{id}/payments
            GET  /loans?status=overdue
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Razor Pages
```

---

## Example 253

**Intent:**
record store inventory that syncs with my discogs listings

**Spec:**
```
Type:       Web application (inventory)
Auth:       Owner login (email + password)
Data model: Record(id, discogs_release_id, artist, title, format, condition, price, location, discogs_listing_id, status)
            Sale(id, record_id -> Record, channel, price, sold_at)
Features:   - Add records by searching the Discogs database
            - List records for sale on Discogs from the app
            - Mark shop sales and remove the Discogs listing
            - Import Discogs orders and mark records sold
            - Show stock value by genre
API:        REST
            POST /records
            POST /records/{id}/sell
            POST /sync/discogs
Storage:    PostgreSQL
Tech stack: Python, Django, Discogs API, Celery
```

---

## Example 254

**Intent:**
costume rental shop, reserve costumes by size for a date range, avoid giving same costume twice

**Spec:**
```
Type:       Web application (rental reservations)
Auth:       Staff login; customers reserve with email
Data model: Costume(id, name, theme, size, photo_url, deposit, rental_price)
            CostumeReservation(id, costume_id -> Costume, customer_name, email, pickup_date, return_date, status)
Features:   - Browse costumes by theme and size
            - Reserve a costume for pickup and return dates
            - Block overlapping reservations including 2 cleaning days
            - Take a deposit and refund it after return
            - Record damage on return
API:        REST
            GET  /costumes?theme={t}&size={s}
            POST /reservations
            POST /reservations/{id}/return
Storage:    SQLite
Tech stack: Node.js, Express, EJS, Stripe
```

---

## Example 255

**Intent:**
suit hire for weddings: groom party members each enter measurements online

**Spec:**
```
Type:       Web application (suit hire)
Auth:       Shop staff login; party members use the group's invite link
Data model: WeddingParty(id, groom_name, wedding_date, suit_style, invite_token)
            PartyMember(id, party_id -> WeddingParty, name, role, chest, waist, leg, shoe_size, submitted_at)
            SuitStock(id, style, size, quantity)
Features:   - Create a party and share an invite link with the groomsmen
            - Collect measurements from each member
            - Remind members who have not submitted
            - Check stock for every size needed on the date
            - Print a pick list for the fitting day
API:        REST
            POST /parties
            POST /parties/{token}/members
            GET  /parties/{id}/stock-check
Storage:    PostgreSQL
Tech stack: Python, Flask, HTMX
```

---

## Example 256

**Intent:**
acupuncture clinic, booking + intake + treatment notes

**Spec:**
```
Type:       Web application (clinic management)
Auth:       Practitioner login with 2FA; patient login for bookings
Data model: Patient(id, name, email, phone, health_history)
            Appointment(id, patient_id -> Patient, starts_at, type, status)
            TreatmentNote(id, appointment_id -> Appointment, points_used, tongue, pulse, notes)
Features:   - Book initial and follow-up appointments online
            - Fill in a health history before the first visit
            - Record points used and observations each session
            - Show past treatments when opening an appointment
API:        REST
            POST /appointments
            POST /patients/me/intake
            POST /appointments/{id}/note
Storage:    PostgreSQL (encrypted at rest)
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 257

**Intent:**
occupational health clinic: companies refer employees for medicals, we send fitness-for-work reports back

**Spec:**
```
Type:       Web application (referral management)
Auth:       Employer HR login; clinician login with 2FA
Data model: EmployerCompany(id, name, hr_email)
            Referral(id, company_id -> EmployerCompany, employee_name, employee_email, reason, status, created_at)
            Assessment(id, referral_id -> Referral, clinician, date, outcome, restrictions, report_url)
Features:   - Let employers submit referrals with the reason
            - Invite employees to book an assessment slot
            - Record outcomes and work restrictions
            - Send employers a report without medical details
            - Bill each company per assessment monthly
API:        REST
            POST /referrals
            POST /referrals/{id}/assessment
            GET  /companies/{id}/invoices
Storage:    PostgreSQL (encrypted)
Tech stack: Java, Spring Boot, React
```

---

## Example 258

**Intent:**
lab sample tracking — samples come in with barcode, go through tests, results go to the doctor

**Spec:**
```
Type:       Web application (lab information system)
Auth:       Lab staff and doctor login (email + password, 2FA)
Data model: Sample(id, barcode, patient_ref, doctor_id -> Doctor, type, received_at, status)
            TestOrder(id, sample_id -> Sample, test_code, result_value, unit, reference_range, completed_at)
            Doctor(id, name, practice, email)
Features:   - Register samples by scanning the barcode
            - Track each sample through processing steps
            - Enter results and flag out-of-range values
            - Release results to the requesting doctor
            - Show turnaround time per test type
API:        REST
            POST /samples
            POST /tests/{id}/result
            GET  /doctors/me/results
Storage:    PostgreSQL
Tech stack: Python, Django, Django REST Framework, Vue.js
```

---

## Example 259

**Intent:**
travel vaccine clinic, people pick destination and we tell them which shots they need and book

**Spec:**
```
Type:       Web application (travel clinic)
Auth:       Nurse login; patients book with email confirmation
Data model: Country(id, name, recommended_vaccines)
            Vaccine(id, name, doses, interval_days, price)
            TravelConsult(id, patient_name, email, destinations, departure_date, starts_at)
            Dose(id, consult_id -> TravelConsult, vaccine_id -> Vaccine, given_on, batch_no)
Features:   - Show recommended vaccines for chosen destinations
            - Warn when there isn't enough time before departure for all doses
            - Book a consultation slot
            - Record doses given with batch numbers
            - Schedule follow-up doses automatically
API:        REST
            GET  /recommendations?countries={codes}
            POST /consults
            POST /consults/{id}/doses
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, React
```

---

## Example 260

**Intent:**
speech therapist portal, kids do homework exercises at home and parents record audio

**Spec:**
```
Type:       Web application (therapy homework)
Auth:       Therapist login; parent login (email + password)
Data model: Child(id, name, birth_date, parent_id -> Parent, therapist_id -> Therapist)
            Parent(id, name, email)
            Therapist(id, name, email)
            HomeworkTask(id, child_id -> Child, title, instructions, due_date)
            AudioSubmission(id, task_id -> HomeworkTask, audio_url, submitted_at, feedback)
Features:   - Assign weekly practice tasks per child
            - Record audio in the browser and upload it
            - Let the therapist listen and leave feedback
            - Show completion rates per child
API:        REST
            POST /children/{id}/tasks
            POST /tasks/{id}/audio
            POST /submissions/{id}/feedback
Storage:    PostgreSQL, S3 (audio)
Tech stack: TypeScript, Next.js, MediaRecorder API, AWS S3
```

---

## Example 261

**Intent:**
crossfit box, members log their workout scores and see a leaderboard for the day

**Spec:**
```
Type:       Web application (workout leaderboard)
Auth:       Member login (email + password); coach role
Data model: Workout(id, date, name, description, score_type)
            Score(id, workout_id -> Workout, member_id -> Member, value, rx, notes)
            Member(id, name, email, gender)
Features:   - Post the workout of the day
            - Log scores as time, reps or weight with Rx or scaled
            - Show a daily leaderboard split by gender and Rx
            - Track personal records per movement
API:        REST
            GET  /workouts/today
            POST /workouts/{id}/scores
            GET  /workouts/{id}/leaderboard
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView
```

---

## Example 262

**Intent:**
pilates studio with 8 reformers, clients book a specific machine

**Spec:**
```
Type:       Web application (class booking)
Auth:       Client login (email + password)
Data model: Reformer(id, number, near_window)
            PilatesClass(id, instructor, starts_at, level)
            ReformerBooking(id, class_id -> PilatesClass, reformer_id -> Reformer, client_id -> Client)
            Client(id, name, email, credits)
Features:   - Show a studio map with free reformers for each class
            - Book a specific reformer using a credit
            - Cancel up to 12 hours before for a credit back
            - Keep a waitlist per class
API:        REST
            GET  /classes/{id}/reformers
            POST /classes/{id}/book
            DELETE /bookings/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 263

**Intent:**
rent my dance studio rooms by the hour to teachers, they pay monthly for hours used

**Spec:**
```
Type:       Web application (room rental)
Auth:       Teacher login (email + password); owner login
Data model: StudioRoom(id, name, size_m2, hourly_rate)
            Teacher(id, name, email, discount_pct)
            RoomRental(id, room_id -> StudioRoom, teacher_id -> Teacher, starts_at, hours)
            MonthlyBill(id, teacher_id -> Teacher, month, total, paid)
Features:   - Book rooms weekly or one-off
            - Show a shared calendar of all rooms
            - Bill teachers monthly for hours booked
            - Give regular teachers a discount
API:        REST
            POST /rentals
            GET  /calendar?week={date}
            POST /bills/generate?month={month}
Storage:    SQLite
Tech stack: PHP, Laravel, FullCalendar
```

---

## Example 264

**Intent:**
school library check out with barcodes, students and staff

**Spec:**
```
Type:       Web application (library management)
Auth:       Librarian login; students log in with school account
Data model: LibraryBook(id, barcode, title, author, isbn, genre)
            Borrower(id, name, type, class_name, card_barcode)
            Checkout(id, book_id -> LibraryBook, borrower_id -> Borrower, out_on, due_on, returned_on)
Features:   - Check books in and out by scanning barcodes
            - Limit students to 3 books at a time
            - Print overdue slips per class
            - Let students search the catalogue and reserve books
API:        REST
            POST /checkouts
            POST /checkouts/{id}/return
            GET  /overdue?class={name}
Storage:    PostgreSQL
Tech stack: Python, Django, Open Library API
```

---

## Example 265

**Intent:**
students tap RFID card when getting on school bus, parents see if child is on board

**Spec:**
```
Type:       IoT system (bus attendance)
Auth:       Parent login (email + password); school admin login
Data model: BusRoute(id, name, driver)
            Student(id, name, rfid_uid, route_id -> BusRoute)
            BoardingEvent(id, student_id -> Student, route_id -> BusRoute, type, latitude, longitude, recorded_at)
Features:   - Read RFID cards when students board and leave
            - Record GPS position with each tap
            - Notify parents when their child boards and gets off
            - Show the school who is on each bus
            - Alert when a student does not tap off at the end of the route
API:        REST
            POST /events
            GET  /routes/{id}/onboard
            GET  /students/{id}/events?date={date}
Storage:    PostgreSQL
Tech stack: Raspberry Pi, RC522 RFID reader, GPS module, Python, FastAPI, Firebase Cloud Messaging
```

---

## Example 266

**Intent:**
exam season invigilator scheduling, teachers given rooms and times without clashes

**Spec:**
```
Type:       Web application (invigilation scheduling)
Auth:       Exams officer login; staff login to see duties
Data model: Exam(id, subject, date, start_time, duration_min, room, candidates)
            Invigilator(id, name, email, max_duties)
            Duty(id, exam_id -> Exam, invigilator_id -> Invigilator)
            Unavailability(id, invigilator_id -> Invigilator, date, period)
Features:   - Calculate invigilators needed per exam from candidate numbers
            - Assign duties avoiding clashes and unavailability
            - Spread duties evenly across staff
            - Email each invigilator their schedule
API:        REST
            POST /exams
            POST /duties/generate
            GET  /invigilators/me/duties
Storage:    PostgreSQL
Tech stack: Python, Flask, OR-Tools
```

---

## Example 267

**Intent:**
after school activities signup, popular ones get lottery

**Spec:**
```
Type:       Web application (activity enrolment)
Auth:       Parent login (email + password); admin login
Data model: Activity(id, name, weekday, year_groups, places, fee)
            ActivityRequest(id, activity_id -> Activity, child_id -> Child, rank, submitted_at)
            Child(id, name, year_group, parent_id)
            Placement(id, activity_id -> Activity, child_id -> Child, status)
Features:   - Let parents rank up to 3 activity choices per child
            - Run a random lottery for oversubscribed activities
            - Place children in their highest available choice
            - Collect fees for confirmed places
            - Show registers to activity leaders
API:        REST
            POST /requests
            POST /lottery/run
            GET  /activities/{id}/register
Storage:    PostgreSQL
Tech stack: TypeScript, Nuxt, Prisma, Stripe
```

---

## Example 268

**Intent:**
temple wants people to book a priest for a puja at home or in temple, with date and type

**Spec:**
```
Type:       Web application (service booking)
Auth:       Temple admin login; devotees book with email
Data model: Priest(id, name, languages)
            PujaType(id, name, duration_min, suggested_donation, location_options)
            PujaBooking(id, puja_type_id -> PujaType, priest_id -> Priest, devotee_name, phone, date, start_time, location, address)
Features:   - Choose a puja type, date and temple or home
            - Assign an available priest who speaks the requested language
            - Add travel time for home pujas
            - Accept an online donation
            - Show priests their weekly schedule
API:        REST
            GET  /puja-types
            POST /bookings
            GET  /priests/{id}/schedule
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 269

**Intent:**
synagogue high holiday seat reservations for members and guests

**Spec:**
```
Type:       Web application (seat reservations)
Auth:       Member login (email + password); office admin
Data model: Seat(id, section, row, number)
            HolidayService(id, name, starts_at)
            SeatReservation(id, seat_id -> Seat, service_id -> HolidayService, holder_name, member_id -> Member, guest, paid)
            Member(id, name, email, household_size)
Features:   - Let members renew their usual seats first
            - Open remaining seats to guests later with a fee
            - Show a seating chart per service
            - Print seat cards
API:        REST
            GET  /services/{id}/seats
            POST /reservations
            GET  /services/{id}/seat-cards
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 270

**Intent:**
sailing club race results with handicap corrected times

**Spec:**
```
Type:       Web application (race results)
Auth:       Race officer login
Data model: BoatClass(id, name, py_number)
            Entry(id, race_id -> SailRace, helm, sail_number, class_id -> BoatClass)
            SailRace(id, series, date, start_time)
            Finish(id, entry_id -> Entry, elapsed_sec, laps, status)
Features:   - Enter finish times on race day
            - Calculate corrected times with Portsmouth Yardstick numbers
            - Rank boats and score series with discards
            - Publish results to the club website
API:        REST
            POST /races/{id}/finishes
            GET  /races/{id}/results
            GET  /series/{name}/standings
Storage:    SQLite
Tech stack: Python, Flask, Jinja2
```

---

## Example 271

**Intent:**
swim club gala entries, coaches enter swimmers into events

**Spec:**
```
Type:       Web application (competition entries)
Auth:       Coach login; club admin login
Data model: Swimmer(id, name, birth_date, gender)
            Gala(id, name, date, entry_deadline, entry_fee)
            GalaEvent(id, gala_id -> Gala, stroke, distance, age_group, gender)
            EventEntry(id, event_id -> GalaEvent, swimmer_id -> Swimmer, entry_time)
Features:   - Enter swimmers into events they are eligible for by age and gender
            - Use the swimmer's best time as the entry time
            - Calculate entry fees per swimmer
            - Export entries in the meet manager format
API:        REST
            POST /galas/{id}/entries
            GET  /galas/{id}/fees
            GET  /galas/{id}/export
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 272

**Intent:**
waitlist for walk ins at my restaurant, they leave their number and get a text when table ready

**Spec:**
```
Type:       Web application (waitlist)
Auth:       Host stand login on tablet
Data model: WaitlistParty(id, name, phone, party_size, added_at, quoted_wait_min, notified_at, status)
Features:   - Add walk-in parties with size and phone number
            - Quote a wait time from current turnover
            - Text the party when their table is ready
            - Remove parties who don't come back within 10 minutes
            - Show average actual wait per night
API:        REST
            POST /parties
            POST /parties/{id}/notify
            PATCH /parties/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Twilio, React
```

---

## Example 273

**Intent:**
split tips between kitchen and floor staff fairly by hours worked each week

**Spec:**
```
Type:       Web application (tip distribution)
Auth:       Manager login; staff view their share
Data model: StaffMember(id, name, role, points_per_hour)
            WorkedHours(id, staff_id -> StaffMember, week_start, hours)
            TipPool(id, week_start, card_tips, cash_tips)
            TipShare(id, pool_id -> TipPool, staff_id -> StaffMember, amount)
Features:   - Enter weekly card and cash tips
            - Import hours worked from the rota
            - Split tips by hours weighted by role points
            - Show each staff member their share and the calculation
            - Export shares for payroll
API:        REST
            POST /pools
            POST /pools/{id}/calculate
            GET  /staff/me/shares
Storage:    SQLite
Tech stack: Python, Flask, pandas
```

---

## Example 274

**Intent:**
TV screen in our cafe showing todays specials that I can change from my phone

**Spec:**
```
Type:       Web application (digital signage)
Auth:       Owner login (email + password)
Data model: Special(id, name, description, price, photo_url, active_from, active_to)
            Screen(id, name, theme, token)
Features:   - Edit specials from a phone
            - Show active specials on a full-screen TV page
            - Rotate through specials every 10 seconds
            - Schedule breakfast and lunch specials by time of day
            - Update screens instantly when something changes
API:        REST + WebSocket
            POST /specials
            GET  /screens/{token}
            WS   /screens/{token}/updates
Storage:    SQLite
Tech stack: Node.js, Express, Socket.IO, vanilla JavaScript
```

---

## Example 275

**Intent:**
nightclub guest list and VIP table bookings with minimum spend

**Spec:**
```
Type:       Web application (guest list and tables)
Auth:       Promoter and door staff login
Data model: ClubNight(id, date, name)
            Promoter(id, name, email)
            GuestListName(id, night_id -> ClubNight, promoter_id -> Promoter, name, plus, arrived)
            VipTable(id, name, capacity, min_spend)
            TableBooking(id, night_id -> ClubNight, table_id -> VipTable, host_name, phone, deposit_paid)
Features:   - Let promoters add names to a night's guest list
            - Check in guests at the door by searching names
            - Book VIP tables with a minimum spend deposit
            - Count arrivals per promoter for commission
API:        REST
            POST /nights/{id}/guestlist
            POST /guestlist/{id}/arrive
            POST /nights/{id}/tables
            GET  /nights/{id}/promoters/report
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Stripe
```

---

## Example 276

**Intent:**
hairdresser colour formula cards so any stylist knows what colour mix a client had

**Spec:**
```
Type:       Web application (client records)
Auth:       Stylist login (PIN)
Data model: Client(id, name, phone, allergies)
            ColourRecord(id, client_id -> Client, date, stylist, formula, developer, processing_min, result_notes, photo_url)
            PatchTest(id, client_id -> Client, tested_on, result)
Features:   - Save colour formulas with developer and timing
            - Show the client's last formulas when they arrive
            - Attach before and after photos
            - Warn if the patch test is older than 6 months
API:        REST
            GET  /clients?q={name}
            POST /clients/{id}/colour
            POST /clients/{id}/patch-tests
Storage:    SQLite
Tech stack: Python, Django, HTMX
```

---

## Example 277

**Intent:**
barbers rent chairs in my shop weekly, need to track who paid chair rent

**Spec:**
```
Type:       Web application (chair rental)
Auth:       Owner login; barber login
Data model: Chair(id, number)
            ChairTenant(id, name, email, chair_id -> Chair, weekly_rent, start_date)
            RentCharge(id, tenant_id -> ChairTenant, week_start, amount, paid_at)
Features:   - Create weekly rent charges automatically
            - Collect rent by card on file
            - Show barbers their payment history
            - Flag barbers more than a week behind
API:        REST
            GET  /charges?unpaid=true
            POST /charges/{id}/pay
            GET  /tenants/me/charges
Storage:    SQLite
Tech stack: Node.js, Express, Stripe
```

---

## Example 278

**Intent:**
warehouse cycle count, count a few bins every day instead of closing for full stock take

**Spec:**
```
Type:       Web application (cycle counting)
Auth:       Counter and supervisor login (badge + PIN)
Data model: Bin(id, code, zone, abc_class, last_counted_on)
            BinStock(id, bin_id -> Bin, sku, system_qty)
            CountTask(id, bin_id -> Bin, assigned_to, date, status)
            CountResult(id, task_id -> CountTask, sku, counted_qty, variance)
Features:   - Generate daily count tasks favouring high-value A items
            - Count bins blind without showing system quantity
            - Request a recount when variance exceeds a threshold
            - Post approved adjustments to stock
            - Show inventory accuracy per zone
API:        REST
            POST /tasks/generate?date={date}
            POST /tasks/{id}/results
            POST /results/{id}/approve
Storage:    PostgreSQL
Tech stack: Go, React, PostgreSQL
```

---

## Example 279

**Intent:**
goods in at our warehouse: check deliveries against the purchase order and note shortages

**Spec:**
```
Type:       Web application (goods receiving)
Auth:       Warehouse staff login
Data model: PurchaseOrder(id, supplier, expected_date, status)
            PoLine(id, po_id -> PurchaseOrder, sku, ordered_qty, received_qty)
            Receipt(id, po_id -> PurchaseOrder, received_at, received_by, notes)
            Discrepancy(id, receipt_id -> Receipt, sku, type, quantity, photo_url)
Features:   - Look up expected deliveries for today
            - Scan received items against PO lines
            - Record shortages, overages and damaged items
            - Print putaway labels with bin suggestions
            - Email suppliers a discrepancy report
API:        REST
            GET  /pos?expected={date}
            POST /pos/{id}/receipts
            POST /receipts/{id}/discrepancies
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 280

**Intent:**
returns processing for online orders, customer requests return, warehouse inspects, refund

**Spec:**
```
Type:       Web application (returns management)
Auth:       Customer lookup by order number + email; staff login
Data model: ReturnRequest(id, order_ref, customer_email, reason, status, created_at)
            ReturnItem(id, request_id -> ReturnRequest, sku, quantity, condition)
            Refund(id, request_id -> ReturnRequest, amount, issued_at)
Features:   - Let customers request a return and print a label
            - Inspect returned items and grade condition
            - Restock items in sellable condition
            - Issue refunds through the shop platform
            - Report return rates by product and reason
API:        REST
            POST /returns
            POST /returns/{id}/inspect
            POST /returns/{id}/refund
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Shopify Admin API, React
```

---

## Example 281

**Intent:**
trucks shud book a time at our loading docks so they dont all turn up at 8am

**Spec:**
```
Type:       Web application (dock scheduling)
Auth:       Carrier login (email + password); warehouse login
Data model: Dock(id, name, type)
            Carrier(id, company, email)
            DockAppointment(id, dock_id -> Dock, carrier_id -> Carrier, po_numbers, starts_at, pallets, status, arrived_at)
Features:   - Show carriers free dock slots by day
            - Size slots by the number of pallets
            - Check in trucks at the gate
            - Track on-time and late arrivals per carrier
API:        REST
            GET  /docks/slots?date={date}
            POST /appointments
            POST /appointments/{id}/arrive
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 282

**Intent:**
forklift drivers do safety checklist before using forklift, on phone

**Spec:**
```
Type:       Web application (pre-use inspections)
Auth:       Driver login (badge + PIN)
Data model: Forklift(id, name, qr_code, status)
            CheckItem(id, text, critical)
            Inspection(id, forklift_id -> Forklift, driver, done_at, passed)
            InspectionAnswer(inspection_id -> Inspection, item_id -> CheckItem, ok, comment)
Features:   - Scan the forklift QR to start a check
            - Answer each checklist item as ok or fault
            - Lock the forklift out when a critical item fails
            - Notify maintenance about faults
            - Show which forklifts were not checked today
API:        REST
            POST /forklifts/{qr}/inspections
            GET  /inspections/missing?date={date}
Storage:    PostgreSQL
Tech stack: Vue.js (PWA), Python, FastAPI
```

---

## Example 283

**Intent:**
move stock between our 3 shops and know what is in transit

**Spec:**
```
Type:       Web application (stock transfers)
Auth:       Shop staff login (email + password)
Data model: Shop(id, name)
            Item(id, sku, name)
            ShopStock(shop_id -> Shop, item_id -> Item, quantity)
            Transfer(id, from_shop_id -> Shop, to_shop_id -> Shop, status, sent_at, received_at)
            TransferLine(transfer_id -> Transfer, item_id -> Item, quantity, received_qty)
Features:   - Request stock from another shop
            - Send a transfer and reduce the sender's stock
            - Receive and confirm quantities at the destination
            - Show stock in transit
            - Report missing items on receipt
API:        REST
            POST /transfers
            POST /transfers/{id}/send
            POST /transfers/{id}/receive
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stimulus
```

---

## Example 284

**Intent:**
appliance repair, technician goes to customer house, we need parts ordered and second visit booked

**Spec:**
```
Type:       Web application (field repair jobs)
Auth:       Office and technician login
Data model: Customer(id, name, address, phone)
            Appliance(id, customer_id -> Customer, type, brand, model_no)
            RepairCall(id, appliance_id -> Appliance, fault, status)
            CallVisit(id, call_id -> RepairCall, technician, visit_date, outcome)
            PartOrder(id, call_id -> RepairCall, part_no, supplier, eta, received)
Features:   - Book a first diagnostic visit
            - Order parts from the visit on a phone
            - Book the return visit when the part arrives
            - Take payment after the final visit
API:        REST
            POST /calls
            POST /calls/{id}/parts
            POST /calls/{id}/visits
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe Terminal
```

---

## Example 285

**Intent:**
e-waste recycling company: businesses book pickups of old computers and get a data destruction certificate

**Spec:**
```
Type:       Web application (pickup and certification)
Auth:       Business customer login; staff login
Data model: BusinessCustomer(id, company, address, contact_email)
            Pickup(id, customer_id -> BusinessCustomer, date, items_estimate, status)
            Device(id, pickup_id -> Pickup, type, serial_no, wiped_at, method)
            Certificate(id, pickup_id -> Pickup, pdf_url, issued_at)
Features:   - Book a pickup with an estimate of items
            - Log each device with serial number on arrival
            - Record the wipe or shredding method per device
            - Issue a data destruction certificate PDF
API:        REST
            POST /pickups
            POST /pickups/{id}/devices
            POST /pickups/{id}/certificate
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, OpenPDF
```

---

## Example 286

**Intent:**
360 performance reviews, colleagues give anonymous feedback

**Spec:**
```
Type:       Web application (performance reviews)
Auth:       Employee login via company SSO
Data model: ReviewCycle(id, name, opens_at, closes_at)
            Review(id, cycle_id -> ReviewCycle, employee_id -> Employee, manager_id -> Employee)
            FeedbackRequest(id, review_id -> Review, reviewer_id -> Employee, submitted_at)
            FeedbackAnswer(request_id -> FeedbackRequest, question, rating, comment)
            Employee(id, name, email)
Features:   - Pick peers to give feedback in each cycle
            - Collect ratings and comments anonymously
            - Hide individual answers when fewer than 3 people responded
            - Show managers a summary per employee
API:        REST
            POST /reviews/{id}/requests
            POST /requests/{id}/answers
            GET  /reviews/{id}/summary
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Okta
```

---

## Example 287

**Intent:**
kudos wall for our team, people thank each other and it shows on a page

**Spec:**
```
Type:       Web application (employee recognition)
Auth:       Company Google SSO
Data model: Employee(id, name, email, avatar_url)
            Kudos(id, from_id -> Employee, to_id -> Employee, message, value_tag, created_at)
Features:   - Post a thank-you to a colleague with a company value tag
            - Show a live wall of recent kudos
            - Notify the receiver by email
            - Show monthly top receivers
API:        REST
            POST /kudos
            GET  /kudos?limit=50
Storage:    SQLite
Tech stack: Python, FastAPI, Svelte
```

---

## Example 288

**Intent:**
overtime requests, staff ask before doing overtime and manager approves budget

**Spec:**
```
Type:       Web application (overtime approval)
Auth:       Employee and manager login (Microsoft SSO)
Data model: Employee(id, name, email, manager_id -> Employee, hourly_rate)
            OvertimeRequest(id, employee_id -> Employee, date, hours, reason, status, cost)
            DepartmentBudget(id, department, month, overtime_budget)
Features:   - Request overtime with date, hours and reason
            - Show managers the cost against the monthly budget
            - Approve or reject requests
            - Record actual hours worked after the day
            - Export approved overtime for payroll
API:        REST
            POST /overtime
            POST /overtime/{id}/decision
            GET  /budgets?month={month}
Storage:    SQL Server
Tech stack: C#, ASP.NET Core, React
```

---

## Example 289

**Intent:**
hybrid ofice ppl book desk for days they come in

**Spec:**
```
Type:       Web application (desk booking)
Auth:       Company SSO (Google Workspace)
Data model: Floor(id, name, plan_image_url)
            Desk(id, floor_id -> Floor, label, x, y, has_monitor)
            DeskBooking(id, desk_id -> Desk, user_email, date)
Features:   - Show a floor plan with free and booked desks
            - Book a desk for one or more days
            - See which teammates are in on a day
            - Release desks not checked into by 10am
API:        REST
            GET  /floors/{id}/desks?date={date}
            POST /bookings
            POST /bookings/{id}/checkin
Storage:    PostgreSQL
Tech stack: Go, React, Google OAuth
```

---

## Example 290

**Intent:**
company directory and org chart that updates from our HR spreadsheet

**Spec:**
```
Type:       Web application (employee directory)
Auth:       Company SSO login
Data model: Employee(id, name, email, title, department, manager_email, phone, photo_url, location)
Features:   - Import employees nightly from the HR spreadsheet
            - Search people by name, team or skill
            - Show an interactive org chart from manager links
            - Show profile pages with contact details
Input:      Google Sheet with one row per employee
API:        REST
            GET  /employees?q={text}
            GET  /orgchart
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Google Sheets API, React, d3-org-chart
```

---

## Example 291

**Intent:**
purchase approval workflow, under 500 manager approves, above that the director too

**Spec:**
```
Type:       Web application (purchase approvals)
Auth:       Employee login via Microsoft 365 SSO
Data model: PurchaseRequest(id, requester_id -> User, supplier, description, amount, cost_centre, status)
            Approval(id, request_id -> PurchaseRequest, approver_id -> User, level, decision, decided_at)
            User(id, name, email, role, manager_id -> User)
Features:   - Submit a purchase request with a quote attached
            - Route requests to the manager, and also the director above 500
            - Approve or reject from an email link
            - Issue a purchase order number once fully approved
API:        REST
            POST /requests
            POST /approvals/{id}/decision
            GET  /requests?status=pending
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Angular, Microsoft Graph API
```

---

## Example 292

**Intent:**
track all the software subscriptions our company pays for and their renewal dates

**Spec:**
```
Type:       Web application (subscription tracker)
Auth:       Finance and IT login (Google SSO)
Data model: Vendor(id, name, website)
            SoftwareSubscription(id, vendor_id -> Vendor, plan, seats, cost, billing_cycle, renewal_date, owner_email)
Features:   - Record subscriptions with cost and seats
            - Email the owner 30 days before renewal
            - Show total yearly spend by department
            - Flag subscriptions with unused seats
API:        REST
            GET  /subscriptions?renewing_within=30
            POST /subscriptions
            GET  /reports/spend
Storage:    SQLite
Tech stack: Python, Flask, Chart.js
```

---

## Example 293

**Intent:**
accident and near miss reporting for our depot, health and safety officer investigates

**Spec:**
```
Type:       Web application (incident reporting)
Auth:       Staff login; safety officer role
Data model: Incident(id, type, location, occurred_at, description, injured_person, reporter_id -> User, severity, status)
            IncidentPhoto(id, incident_id -> Incident, url)
            Action(id, incident_id -> Incident, description, owner, due_date, done)
            User(id, name, email, role)
Features:   - Report accidents and near misses from a phone
            - Attach photos of the scene
            - Investigate and assign corrective actions
            - Track overdue actions
            - Show incidents per month by type
API:        REST
            POST /incidents
            POST /incidents/{id}/actions
            GET  /reports/monthly
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Bootstrap
```

---

## Example 294

**Intent:**
dog breeder waitlist for pupies w deposits and pick order

**Spec:**
```
Type:       Web application (waiting list)
Auth:       Breeder login; families log in by email link
Data model: Family(id, name, email, phone, preferences)
            Litter(id, dam, sire, born_on, puppies_count)
            Reservation(id, family_id -> Family, litter_id -> Litter, deposit_paid, pick_order)
            Puppy(id, litter_id -> Litter, sex, colour, family_id -> Family)
Features:   - Collect applications with preferences
            - Take deposits and set pick order
            - Post puppy photos and weekly updates
            - Let families choose a puppy in pick order
API:        REST
            POST /applications
            POST /litters/{id}/reservations
            POST /puppies/{id}/choose
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Express, React, Stripe
```

---

## Example 295

**Intent:**
tutoring agency, match tutors to students by subject, level and area

**Spec:**
```
Type:       Web application (tutor matching)
Auth:       Tutor, parent and admin login (email + password)
Data model: Tutor(id, name, subjects, levels, postcode, hourly_rate, online)
            Request(id, parent_name, email, subject, level, postcode, online_ok, status)
            Match(id, request_id -> Request, tutor_id -> Tutor, status)
            TutorLesson(id, match_id -> Match, date, hours, paid)
Features:   - Collect tutoring requests from parents
            - Suggest tutors by subject, level and distance
            - Send introductions and track acceptance
            - Log lessons and charge parents
            - Pay tutors minus the agency fee
API:        REST
            POST /requests
            GET  /requests/{id}/suggestions
            POST /matches/{id}/lessons
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe Connect
```

---

## Example 296

**Intent:**
donor CRM for our small nonprofit, track gifts, campaigns and thank you letters

**Spec:**
```
Type:       Web application (donor CRM)
Auth:       Staff login (email + password, 2FA)
Data model: Donor(id, name, email, address, type)
            Campaign(id, name, goal, starts_on, ends_on)
            Gift(id, donor_id -> Donor, campaign_id -> Campaign, amount, received_on, method, thanked)
Features:   - Record gifts against donors and campaigns
            - Generate thank-you letters from templates
            - Show lapsed donors who gave last year but not this year
            - Show campaign progress against goal
            - Export year-end tax receipts
API:        REST
            POST /gifts
            GET  /donors?lapsed=true
            GET  /campaigns/{id}/progress
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Prawn
```

---

## Example 297

**Intent:**
piano tuner customer list that reminds them every 6 months to book

**Spec:**
```
Type:       Web application (service reminders)
Auth:       Tuner login
Data model: Customer(id, name, address, phone, email)
            Piano(id, customer_id -> Customer, make, type, interval_months)
            Tuning(id, piano_id -> Piano, date, pitch_raise, notes, price)
Features:   - Keep customers and their pianos
            - Email reminders when the next tuning is due
            - Let customers pick a date from a link
            - Group due tunings by area to plan days
API:        REST
            GET  /pianos/due?month={month}
            POST /tunings
            GET  /book/{token}
Storage:    SQLite
Tech stack: Python, Flask, Celery
```

---

## Example 298

**Intent:**
marketing agency retainers, bill clients monthly and track hours used against retainer

**Spec:**
```
Type:       Web application (retainer billing)
Auth:       Staff login (Google SSO)
Data model: Client(id, name, contact_email)
            Retainer(id, client_id -> Client, monthly_fee, included_hours, start_date)
            AgencyTimeEntry(id, client_id -> Client, staff, date, hours, task)
            AgencyInvoice(id, client_id -> Client, month, amount, overage_hours, status)
Features:   - Log hours per client and task
            - Show hours used against the monthly retainer
            - Invoice the retainer plus overage hours
            - Warn account managers at 80% of hours
API:        REST
            POST /time
            GET  /clients/{id}/usage?month={month}
            POST /invoices/run?month={month}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma, QuickBooks Online API
```

---

## Example 299

**Intent:**
concierge parcel log for our apartment building, residents get notified to pick up

**Spec:**
```
Type:       Web application (parcel log)
Auth:       Concierge login; residents log in by email
Data model: Resident(id, name, apartment, email, phone)
            Parcel(id, resident_id -> Resident, carrier, shelf, received_at, collected_at, collected_by)
Features:   - Log parcels by apartment number and shelf
            - Notify residents by email and SMS
            - Record collection with a signature
            - List parcels uncollected after 7 days
API:        REST
            POST /parcels
            POST /parcels/{id}/collect
            GET  /parcels?uncollected=true
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Twilio
```

---

## Example 300

**Intent:**
building amenities booking: residents book the party room and guest suite

**Spec:**
```
Type:       Web application (amenity booking)
Auth:       Resident login (email + password); building manager login
Data model: Amenity(id, name, fee, deposit, max_hours, rules)
            Resident(id, name, unit, email)
            AmenityBooking(id, amenity_id -> Amenity, resident_id -> Resident, starts_at, ends_at, status)
Features:   - Show amenity calendars
            - Book within the maximum hours per amenity
            - Charge fees and refundable deposits
            - Require manager approval for the party room
API:        REST
            GET  /amenities/{id}/calendar
            POST /bookings
            POST /bookings/{id}/approve
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 301

**Intent:**
i rent rooms in 2 houses to students and split the gas electric internet bills between them each month, its a headache

**Spec:**
```
Type:       Web application (shared bills)
Auth:       Landlord login; tenant login by email link
Data model: House(id, address)
            RoomTenant(id, house_id -> House, name, email, move_in, move_out)
            Bill(id, house_id -> House, utility, period_start, period_end, amount)
            BillShare(id, bill_id -> Bill, tenant_id -> RoomTenant, amount, paid)
Features:   - Enter utility bills per house
            - Split bills by days each tenant lived there in the period
            - Email tenants their share with a payment link
            - Show who still owes for each bill
API:        REST
            POST /houses/{id}/bills
            GET  /bills/{id}/shares
            POST /shares/{id}/pay
Storage:    SQLite
Tech stack: Python, Flask, Stripe Payment Links
```

---

## Example 302

**Intent:**
we have sub meters for each shop in our building and want to bill electricity to each tenant from the readings

**Spec:**
```
Type:       Web application (sub-metering billing)
Auth:       Building manager login
Data model: Tenant(id, name, unit, email)
            Meter(id, tenant_id -> Tenant, serial_no, multiplier)
            MeterReading(id, meter_id -> Meter, reading_kwh, read_on, photo_url)
            Tariff(id, price_per_kwh, standing_charge_day, valid_from)
            UtilityInvoice(id, tenant_id -> Tenant, period, kwh, amount, sent_at)
Features:   - Enter monthly meter readings with a photo
            - Reject readings lower than the previous one
            - Calculate usage and cost with the current tariff
            - Generate and email invoices to tenants
API:        REST
            POST /meters/{id}/readings
            POST /invoices/run?period={month}
            GET  /tenants/{id}/usage
Storage:    PostgreSQL
Tech stack: Python, Django, WeasyPrint
```

---

## Example 303

**Intent:**
holiday park where people own their lodges and pay yearly site fees and we also rent some out for them

**Spec:**
```
Type:       Web application (holiday park management)
Auth:       Owner login (email + password); park office login
Data model: Lodge(id, plot, model, owner_id -> LodgeOwner, in_rental_scheme)
            LodgeOwner(id, name, email, phone)
            SiteFee(id, lodge_id -> Lodge, year, amount, paid)
            LetBooking(id, lodge_id -> Lodge, guest_name, arrival, departure, income)
            OwnerStatement(id, owner_id -> LodgeOwner, month, rental_income, commission, payout)
Features:   - Invoice yearly site fees per lodge
            - Take guest bookings for lodges in the rental scheme
            - Block dates owners want to use themselves
            - Send owners monthly statements of rental income minus commission
API:        REST
            POST /lodges/{id}/owner-dates
            POST /bookings
            GET  /owners/me/statements
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Livewire
```

---

## Example 304

**Intent:**
charity gala: sell tables of 10, guests bid on silent auction items from their phone during the night

**Spec:**
```
Type:       Web application (gala and silent auction)
Auth:       Organiser login; guests log in with phone + SMS code
Data model: GalaTable(id, name, host_email, seats, price, paid)
            Guest(id, table_id -> GalaTable, name, phone, bidder_number)
            AuctionItem(id, title, description, photo_url, start_bid, increment, closes_at)
            Bid(id, item_id -> AuctionItem, guest_id -> Guest, amount, placed_at)
Features:   - Sell tables and collect guest names from hosts
            - Show auction items with current highest bid
            - Place bids from a phone with minimum increments
            - Notify guests when they are outbid
            - Close bidding and charge winners
API:        REST + WebSocket
            POST /tables/{id}/guests
            POST /items/{id}/bids
            WS   /items/live
            POST /auction/close
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, React, Socket.IO, Stripe
```

---

## Example 305

**Intent:**
craft workshops — candle making, pottery, wreaths — book a seat, materials fee included

**Spec:**
```
Type:       Web application (workshop booking)
Auth:       Host login; attendees book as guests
Data model: Workshop(id, title, description, host, starts_at, seats, price, materials_fee)
            WorkshopBooking(id, workshop_id -> Workshop, name, email, seats, total, paid)
Features:   - List upcoming workshops with seats left
            - Book and pay including the materials fee
            - Send a reminder with what to bring
            - Show the host a shopping list of materials per workshop
            - Sell gift bookings for a friend
API:        REST
            GET  /workshops
            POST /workshops/{id}/bookings
            GET  /workshops/{id}/materials
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe Checkout
```

---

## Example 306

**Intent:**
kids summer camp, parents book weeks, add early drop off, upload medical form

**Spec:**
```
Type:       Web application (camp registration)
Auth:       Parent login (email + password); camp admin login
Data model: CampWeek(id, start_date, theme, capacity, price)
            Camper(id, parent_id -> Parent, name, birth_date, allergies, medical_form_url)
            Parent(id, name, email, phone)
            CampBooking(id, week_id -> CampWeek, camper_id -> Camper, early_dropoff, late_pickup, paid)
Features:   - Book multiple weeks per child
            - Add early drop-off and late pickup extras
            - Upload a signed medical form once per summer
            - Offer a sibling discount
            - Print daily registers with allergy flags
API:        REST
            GET  /weeks
            POST /bookings
            POST /campers/{id}/medical-form
Storage:    PostgreSQL, S3 (forms)
Tech stack: Python, Django, Stripe
```

---

## Example 307

**Intent:**
small music festival, crew and volunteers need accreditation and wristbands by area access

**Spec:**
```
Type:       Web application (accreditation)
Auth:       Department manager login; crew apply with email
Data model: Department(id, name, manager_email)
            CrewMember(id, name, email, photo_url, department_id -> Department, status)
            AccessZone(id, name)
            Accreditation(id, crew_id -> CrewMember, zones, wristband_code, issued_at)
Features:   - Let crew apply with a photo
            - Approve crew per department
            - Assign access zones like backstage and bars
            - Issue wristbands with a scannable code
            - Scan wristbands at zone entrances
API:        REST
            POST /crew
            POST /crew/{id}/approve
            POST /scan
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 308

**Intent:**
rugby club, players say if they are available for saturday and coach picks the team

**Spec:**
```
Type:       Web application (team selection)
Auth:       Player and coach login (email + password)
Data model: Player(id, name, positions, phone)
            RugbyMatch(id, opponent, kickoff, home)
            Availability(id, match_id -> RugbyMatch, player_id -> Player, available)
            Selection(id, match_id -> RugbyMatch, player_id -> Player, shirt_number)
Features:   - Ask players for availability each week
            - Show the coach available players by position
            - Pick a matchday squad with shirt numbers
            - Text players the team sheet
API:        REST
            POST /matches/{id}/availability
            POST /matches/{id}/selection
            GET  /matches/{id}/teamsheet
Storage:    SQLite
Tech stack: Python, Flask, Twilio
```

---

## Example 309

**Intent:**
room service menu on the hotel tv/tablet, orders go to kitchen and get charged to the room

**Spec:**
```
Type:       Web application (room service ordering)
Auth:       Room tablet with device token; kitchen staff login
Data model: HotelRoom(id, number, device_token)
            RoomServiceItem(id, name, price, available_from, available_to)
            RoomServiceOrder(id, room_id -> HotelRoom, status, total, created_at)
            RoomServiceLine(order_id -> RoomServiceOrder, item_id -> RoomServiceItem, quantity, note)
Features:   - Show menu items available at the current time
            - Place orders from the room tablet
            - Show orders live in the kitchen
            - Post the charge to the guest's folio in the PMS
API:        REST + WebSocket
            GET  /menu
            POST /orders
            WS   /kitchen
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js, PMS integration API
```

---

## Example 310

**Intent:**
online check in for our hotel guests before arrival, upload passport, sign registration card

**Spec:**
```
Type:       Web application (online check-in)
Auth:       Guest access by booking reference + last name; front desk login
Data model: Reservation(id, reference, last_name, arrival, departure, room_type)
            GuestRegistration(id, reservation_id -> Reservation, nationality, passport_no, passport_image_url, address, signature_url, completed_at)
Features:   - Email a check-in link 3 days before arrival
            - Collect passport details and image
            - Sign the registration card on screen
            - Choose an arrival time and room preferences
            - Show the front desk who has checked in online
API:        REST
            GET  /checkin/{reference}
            POST /checkin/{reference}
            GET  /admin/arrivals?date={date}
Storage:    PostgreSQL, S3 (passport images, encrypted)
Tech stack: Python, FastAPI, React, signature_pad
```

---

## Example 311

**Intent:**
gym owner here, want dashbord of members cancelling, new joins, attendence trends

**Spec:**
```
Type:       Data dashboard (gym membership)
Auth:       Owner login (email + password)
Features:   - Load members, cancellations and check-ins from the gym software export
            - Show monthly joins, cancellations and net growth
            - Calculate churn rate per membership plan
            - Flag members who have not visited in 30 days
            - Show visits by weekday and hour
Input:      Weekly CSV exports of members and check-ins
Storage:    DuckDB
Tech stack: Python, Streamlit, pandas, Altair
```

---

## Example 312

**Intent:**
salon wants to know how much product (shampoo, colour) is used per service and reorder

**Spec:**
```
Type:       Web application (back-bar stock)
Auth:       Salon manager login
Data model: ProductStock(id, name, brand, unit_ml, quantity, reorder_level)
            ServiceRecipe(id, service, product_id -> ProductStock, ml_used)
            ServiceDone(id, service, done_at, stylist)
Features:   - Define how much product each service uses
            - Reduce stock as services are recorded
            - Show cost of product per service
            - Create a reorder list for the supplier
API:        REST
            POST /services-done
            GET  /stock?below_reorder=true
            GET  /reports/product-cost
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 313

**Intent:**
GP surgery consumables like gloves syringes in each room, nurses top up from store room

**Spec:**
```
Type:       Web application (consumables stock)
Auth:       Staff login (email + password)
Data model: ClinicRoom(id, name)
            Consumable(id, name, unit, store_quantity, reorder_level)
            RoomPar(id, room_id -> ClinicRoom, consumable_id -> Consumable, par_level)
            TopUp(id, room_id -> ClinicRoom, consumable_id -> Consumable, quantity, done_by, done_at)
Features:   - Set par levels per room for each item
            - Record top-ups moved from the store room
            - Show a weekly order list when store stock is low
            - Track usage per room per month
API:        REST
            POST /topups
            GET  /orders/suggested
            GET  /rooms/{id}/usage
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Razor Pages
```

---

## Example 314

**Intent:**
farm vet practice, vets visit farms, record herd treatments and withdrawal periods for milk and meat

**Spec:**
```
Type:       Web application (farm animal records)
Auth:       Vet login with 2FA; farmer read-only login
Data model: Farm(id, name, holding_number, owner_email)
            FarmVisit(id, farm_id -> Farm, vet, visited_on, mileage)
            Treatment(id, visit_id -> FarmVisit, animal_ids, medicine, dose, milk_withdrawal_days, meat_withdrawal_days)
Features:   - Record visits and treatments per farm
            - Calculate milk and meat withdrawal end dates
            - Show farmers animals still under withdrawal
            - Invoice visits with mileage and medicines
API:        REST
            POST /farms/{id}/visits
            POST /visits/{id}/treatments
            GET  /farms/{id}/withdrawals
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 315

**Intent:**
livery yard, horse owners pay monthly plus extras like hay, turnout, rugging, need invoice each month

**Spec:**
```
Type:       Web application (livery billing)
Auth:       Yard manager login; owner login
Data model: HorseOwner(id, name, email)
            LiveryHorse(id, owner_id -> HorseOwner, name, livery_package, stable_no)
            ExtraService(id, name, price)
            ExtraCharge(id, horse_id -> LiveryHorse, service_id -> ExtraService, date, quantity)
            LiveryInvoice(id, owner_id -> HorseOwner, month, total, paid)
Features:   - Record extras per horse during the month
            - Let owners request extras from their phone
            - Invoice the package plus extras monthly
            - Show owners their running total
API:        REST
            POST /horses/{id}/extras
            POST /invoices/run?month={month}
            GET  /owners/me/balance
Storage:    SQLite
Tech stack: Ruby on Rails, Stripe
```

---

## Example 316

**Intent:**
sunday school check in, kids get a name label and parents get matching pickup code

**Spec:**
```
Type:       Web application (child check-in)
Auth:       Volunteer login on check-in kiosks
Data model: Family(id, surname, phone)
            Kid(id, family_id -> Family, name, birth_date, allergies, class_room)
            CheckInRecord(id, kid_id -> Kid, date, pickup_code, checked_in_at, checked_out_at)
Features:   - Search families by phone number at the kiosk
            - Check in children and print name labels with allergies
            - Print a matching pickup code for the parent
            - Check out only when the code matches
            - Show each classroom's current list
API:        REST
            GET  /families?phone={phone}
            POST /checkins
            POST /checkins/{id}/checkout
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Brother label printer SDK
```

---

## Example 317

**Intent:**
marina berths yearly or vistors per night, harbor master assigns them

**Spec:**
```
Type:       Web application (marina management)
Auth:       Harbour master login; boat owner login
Data model: Berth(id, pontoon, number, max_length_m, has_power)
            Vessel(id, owner_id -> BoatOwner, name, length_m, beam_m)
            BoatOwner(id, name, email, phone)
            BerthContract(id, berth_id -> Berth, vessel_id -> Vessel, type, start_date, end_date, price)
Features:   - Assign berths that fit the vessel length
            - Sell annual contracts and nightly visitor stays
            - Let annual holders mark when they're away so berths can be re-let
            - Show a pontoon map with occupancy
API:        REST
            GET  /berths/available?length={m}&from={d}&to={d}
            POST /contracts
            POST /contracts/{id}/away
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 318

**Intent:**
caravan storage yard, 120 spaces, owners book collection so its ready at the gate

**Spec:**
```
Type:       Web application (storage yard)
Auth:       Owner login (email + password); yard staff login
Data model: Space(id, number, size)
            Caravan(id, owner_id -> Owner, make, reg, space_id -> Space)
            Owner(id, name, email, phone)
            Movement(id, caravan_id -> Caravan, type, requested_for, done_at)
Features:   - Request caravan collection or return with a time
            - Show staff a daily movement list
            - Charge storage fees quarterly
            - Keep a history of movements per caravan
API:        REST
            POST /movements
            GET  /movements?date={date}
            POST /fees/run?quarter={q}
Storage:    SQLite
Tech stack: PHP, Laravel, Stripe
```

---

## Example 319

**Intent:**
build a school timetable for a small secondary school, teachers, rooms, subjects, no clashes

**Spec:**
```
Type:       Web application (timetabling)
Auth:       Deputy head admin login; staff read-only
Data model: TeachingGroup(id, name, year)
            Subject(id, name, periods_per_week)
            Teacher(id, name, subjects, max_periods)
            SchoolRoom(id, name, type)
            Lesson(id, group_id -> TeachingGroup, subject_id -> Subject, teacher_id -> Teacher, room_id -> SchoolRoom, day, period)
Features:   - Enter subjects and periods per week for each group
            - Generate a timetable with no teacher, room or group clashes
            - Respect special rooms like labs and gyms
            - Allow manual drag-and-drop edits with clash checks
            - Print timetables per teacher, room and group
API:        REST
            POST /timetable/solve
            PATCH /lessons/{id}
            GET  /timetable?teacher={id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, OR-Tools CP-SAT, React
```

---

## Example 320

**Intent:**
admissions applications for our private school with interview scheduling

**Spec:**
```
Type:       Web application (admissions)
Auth:       Parent login (email + password); admissions staff login
Data model: Applicant(id, child_name, birth_date, entry_year, current_school, parent_id -> Parent)
            Parent(id, name, email, phone)
            AdmissionFile(id, applicant_id -> Applicant, kind, url)
            Interview(id, applicant_id -> Applicant, starts_at, interviewer, outcome)
Features:   - Submit an application with school reports
            - Pay the registration fee online
            - Book an interview and assessment slot
            - Record decisions and send offer letters
            - Show application numbers per entry year
API:        REST
            POST /applications
            POST /applications/{id}/files
            POST /applications/{id}/interview
Storage:    PostgreSQL, S3 (documents)
Tech stack: Ruby on Rails, Stripe
```

---

## Example 321

**Intent:**
text parents when student is absent and not called in sick by 9:30

**Spec:**
```
Type:       Web application (absence alerts)
Auth:       Office staff and teacher login (school SSO)
Data model: Pupil(id, name, form, parent_phone)
            RegisterMark(id, pupil_id -> Pupil, date, session, mark)
            ReportedAbsence(id, pupil_id -> Pupil, date, reason, reported_by)
Features:   - Take morning registers on the web
            - Let parents report absences through a form
            - Text parents of unexplained absences at 9:30
            - Show attendance percentage per pupil
API:        REST
            POST /registers
            POST /absences
            POST /alerts/run
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio
```

---

## Example 322

**Intent:**
mobile app for me as a driving instructor (just me), my diary, pupils, payments, and pupils see their next lesson

**Spec:**
```
Type:       Mobile application with backend
Auth:       Instructor login; pupils log in with phone + SMS code
Data model: Pupil(id, name, phone, address, test_date, balance)
            DrivingLesson(id, pupil_id -> Pupil, starts_at, duration_min, pickup, paid)
            SkillProgress(id, pupil_id -> Pupil, skill, level)
Features:   - Manage a weekly diary of lessons
            - Track payments and block bookings
            - Record skill progress after each lesson
            - Let pupils see their next lesson and progress
            - Send push reminders the night before
API:        REST
            GET  /lessons?week={date}
            POST /lessons
            GET  /pupils/me
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase (Auth, Firestore, Cloud Messaging)
```

---

## Example 323

**Intent:**
suppliers send PDF invoices to our restaurant email, I want them read automatically and put in a spreadsheet

**Spec:**
```
Type:       Data pipeline (invoice extraction)
Data model: SupplierInvoice(id, supplier, invoice_no, date, net, vat, total, source_file)
Features:   - Fetch new emails with PDF attachments from a mailbox
            - Extract supplier, invoice number, date and totals
            - Skip invoices already processed
            - Append each invoice as a row in Google Sheets
            - Email a weekly spend summary by supplier
Input:      IMAP mailbox with PDF supplier invoices
Storage:    Google Sheets, SQLite (processed log)
Tech stack: Python, imaplib, pdfplumber, gspread, cron
```

---

## Example 324

**Intent:**
every night copy yesterday's sales from square into google sheets so my accountant can see them

**Spec:**
```
Type:       Scheduled script (sales export)
Features:   - Fetch yesterday's payments from the Square API at 2am
            - Total sales by payment method and category
            - Append a daily row to the Google Sheet
            - Append itemised sales to a second tab
            - Email an alert if the API call fails
Input:      Square access token, Google service account key
Storage:    Google Sheets
Tech stack: Python, Square Python SDK, gspread, GitHub Actions schedule
```

---

## Example 325

**Intent:**
script that checks my shopify stock every morning and emails my supplier list of what's low

**Spec:**
```
Type:       Scheduled script (low stock alert)
Features:   - Read inventory levels for all variants from Shopify
            - Compare each with a reorder point from a config file
            - Group low items by supplier
            - Email each supplier a draft order list
            - Send me a copy of all emails sent
Input:      Shopify Admin API token, YAML file of reorder points and supplier emails
Tech stack: Node.js, Shopify Admin GraphQL API, Nodemailer, cron
```

---

## Example 326

**Intent:**
dashboard of no shows at our clinic, by day, doctor and how far ahead they booked

**Spec:**
```
Type:       Data dashboard (no-show analysis)
Auth:       Practice manager login
Features:   - Import appointment history from the practice system export
            - Show no-show rate by weekday, time and clinician
            - Compare no-shows by booking lead time
            - Show the effect of SMS reminders on no-shows
            - List patients with 3 or more no-shows
Input:      CSV export of appointments with status and booking date
Storage:    SQLite
Tech stack: Python, Dash, pandas, Plotly
```

---

## Example 327

**Intent:**
we have a gym app made by an agency and need our own API for classes and bookings that it can call

**Spec:**
```
Type:       REST API service (gym bookings)
Auth:       JWT tokens for members; API key for the mobile app
Data model: Member(id, email, password_hash, name, plan)
            GymClassSlot(id, name, coach, starts_at, capacity)
            ClassBooking(id, slot_id -> GymClassSlot, member_id -> Member, status, created_at)
Features:   - Return the class timetable for a date range
            - Book and cancel class places
            - Enforce capacity with a waitlist
            - Return a member's upcoming bookings
            - Publish OpenAPI documentation for the agency
API:        REST
            POST /auth/login
            GET  /classes?from={date}&to={date}
            POST /classes/{id}/bookings
            DELETE /bookings/{id}
            GET  /me/bookings
Storage:    PostgreSQL
Tech stack: Python, FastAPI, SQLAlchemy, Alembic
```

---

## Example 328

**Intent:**
when a customer pays on stripe, mark the invoice paid in our airtable automatically

**Spec:**
```
Type:       Webhook service (payment sync)
Features:   - Receive Stripe payment_intent.succeeded events
            - Verify the Stripe webhook signature
            - Find the matching invoice record in Airtable by invoice number
            - Set status to paid with the payment date and amount
            - Log events that have no matching invoice for review
API:        REST
            POST /webhooks/stripe
Storage:    Airtable
Tech stack: Node.js, Express, Stripe SDK, Airtable API
```

---

## Example 329

**Intent:**
chatbot on our dental clinic website answering opening hours, prices and booking an appointment

**Spec:**
```
Type:       Chatbot (clinic website)
Data model: FaqEntry(id, question, answer)
            ChatSession(id, started_at, booked_appointment_id)
            ChatMessage(id, session_id -> ChatSession, role, text, created_at)
Features:   - Answer questions about hours, prices and treatments from clinic info
            - Offer free appointment slots inside the chat
            - Book the chosen slot in the practice calendar
            - Hand over to reception during opening hours
            - Avoid giving medical advice and suggest a visit instead
API:        REST
            POST /chat
            GET  /slots?date={date}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, LLM API, JavaScript chat widget
```

---

## Example 330

**Intent:**
discord bot for my gaming cafe so people can reserve PCs from our discord server

**Spec:**
```
Type:       Bot (Discord)
Data model: Station(id, name, specs)
            StationBooking(id, station_id -> Station, discord_user_id, starts_at, hours, status)
Features:   - Show free PCs with a /pcs command
            - Reserve a PC for a time with /reserve
            - Send a reminder DM 15 minutes before
            - Let staff cancel no-shows after 10 minutes
API:        REST
            GET  /stations/free?at={time}
Storage:    SQLite
Tech stack: Python, discord.py, aiosqlite
```

---

## Example 331

**Intent:**
point of sale for my hardware shop on a windows pc, must work when internet is down

**Spec:**
```
Type:       Desktop application (point of sale)
Auth:       Cashier login with PIN
Data model: Product(id, barcode, name, price, stock, vat_rate)
            PosSaleRecord(id, cashier, total, payment_method, created_at, synced)
            PosSaleLine(sale_id -> PosSaleRecord, product_id -> Product, quantity, price)
Features:   - Scan barcodes to add items to a sale
            - Take cash and card payments
            - Print receipts on a thermal printer
            - Work fully offline and sync sales to the cloud later
            - Show end-of-day totals per payment method
Storage:    Local SQLite, synced to PostgreSQL
Tech stack: C#, .NET, WPF, ESC/POS printing
```

---

## Example 332

**Intent:**
till system for our cafe on an ipad, simple, buttons for drinks and food

**Spec:**
```
Type:       Web application (point of sale)
Auth:       Staff PIN login
Data model: PosItem(id, name, category, price, button_colour)
            Ticket(id, staff_id, total, payment_method, created_at)
            TicketLine(ticket_id -> Ticket, item_id -> PosItem, quantity, modifiers)
Features:   - Tap item buttons grouped by category
            - Add modifiers like oat milk or extra shot
            - Take card payments with a card reader
            - Show daily sales and top items
            - Work as a full-screen app on iPad
API:        REST
            GET  /items
            POST /tickets
            GET  /reports/daily
Storage:    PostgreSQL
Tech stack: React (PWA), Node.js, Stripe Terminal
```

---

## Example 333

**Intent:**
app on my phone to take card payments at my market stall and track what sold

**Spec:**
```
Type:       Mobile application with backend
Auth:       Owner login (email + password)
Data model: StallProduct(id, name, price, stock)
            StallSale(id, total, method, market_name, sold_at)
            StallSaleItem(sale_id -> StallSale, product_id -> StallProduct, quantity)
Features:   - Ring up sales from a product grid
            - Take contactless payments with tap to pay
            - Record cash sales too
            - Show takings per market day
            - Reduce stock as items sell
API:        REST
            POST /sales
            GET  /reports/markets
Storage:    Supabase Postgres
Tech stack: React Native, Stripe Terminal SDK (Tap to Pay), Supabase
```

---

## Example 334

**Intent:**
car park with barrier, cameras read number plates and people pay online after

**Spec:**
```
Type:       IoT system (car park)
Auth:       Operator login to the dashboard
Data model: ParkingVisit(id, plate, entered_at, exited_at, amount_due, paid_at)
            Permit(id, plate, valid_until)
            Tariff(id, max_minutes, price)
Features:   - Read number plates at entry and exit with ANPR cameras
            - Open the barrier automatically for permit holders
            - Calculate the fee from time parked
            - Let drivers pay online by plate within 48 hours
            - Flag unpaid visits for follow-up
API:        REST
            POST /events/entry
            POST /events/exit
            GET  /pay?plate={plate}
            POST /visits/{id}/pay
Storage:    PostgreSQL
Tech stack: OpenALPR, Raspberry Pi relay control, Python, FastAPI, Stripe
```

---

## Example 335

**Intent:**
car wash monthly unlimited membership, camera knows the plate so they just drive in

**Spec:**
```
Type:       Web application (wash membership)
Auth:       Customer login (email + password); site manager login
Data model: WashCustomer(id, name, email)
            WashPlan(id, name, monthly_price, wash_level)
            WashMembership(id, customer_id -> WashCustomer, plan_id -> WashPlan, plate, status)
            WashVisit(id, plate, visited_at, member)
Features:   - Sign up for a monthly plan with a number plate
            - Recognise member plates at the entry camera
            - Start the wash program for the plan level
            - Bill members monthly and suspend failed payments
            - Show washes per day for members and non-members
API:        REST
            POST /memberships
            POST /camera/plate
            GET  /reports/visits
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Plate Recognizer API, Stripe Billing
```

---

## Example 336

**Intent:**
office got 6 ev chargers and staff need to book slots fairly

**Spec:**
```
Type:       Web application (charger booking)
Auth:       Staff login via Microsoft SSO
Data model: Charger(id, name, power_kw)
            ChargeSlot(id, charger_id -> Charger, user_email, date, start_time, end_time, checked_in)
Features:   - Book a charger in 2-hour slots
            - Limit each person to 2 slots per week
            - Release slots not checked into within 15 minutes
            - Email a reminder to move the car at the end of the slot
API:        REST
            GET  /chargers/slots?date={date}
            POST /slots
            POST /slots/{id}/checkin
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Microsoft Entra ID
```

---

## Example 337

**Intent:**
pool cars at our council office, staff book a car for site visits and log mileage

**Spec:**
```
Type:       Web application (pool car booking)
Auth:       Staff login (Active Directory)
Data model: PoolCar(id, reg, model, fuel_type, current_mileage)
            CarBooking(id, car_id -> PoolCar, staff_email, starts_at, ends_at, purpose, start_mileage, end_mileage)
            CarDefect(id, car_id -> PoolCar, description, reported_at, fixed)
Features:   - Book a car for a time range
            - Record start and end mileage
            - Report defects and take cars out of service
            - Show mileage per department each month
API:        REST
            GET  /cars/available?from={dt}&to={dt}
            POST /bookings
            POST /bookings/{id}/return
Storage:    SQL Server
Tech stack: C#, ASP.NET Core, LDAP
```

---

## Example 338

**Intent:**
track calibration due dates for measuring tools in our workshop (calipers, torque wrenches)

**Spec:**
```
Type:       Web application (calibration tracking)
Auth:       Quality manager login; staff read-only
Data model: Instrument(id, asset_tag, type, serial_no, location, interval_months, status)
            Calibration(id, instrument_id -> Instrument, done_on, by, result, certificate_url)
Features:   - Register instruments with calibration intervals
            - Record calibrations with certificates
            - List instruments due in the next 30 days
            - Mark overdue instruments as do-not-use
API:        REST
            POST /instruments
            POST /instruments/{id}/calibrations
            GET  /instruments?due_within=30
Storage:    PostgreSQL
Tech stack: Python, Flask, SQLAlchemy
```

---

## Example 339

**Intent:**
sales reps request free product samples for customers, warehouse ships them, we track cost per rep

**Spec:**
```
Type:       Web application (sample requests)
Auth:       Rep and warehouse login (Google SSO)
Data model: SampleRequest(id, rep_email, customer_company, address, status, created_at)
            SampleLine(request_id -> SampleRequest, sku, quantity, unit_cost)
            Shipment(id, request_id -> SampleRequest, carrier, tracking_no, shipped_at)
Features:   - Request samples for a customer
            - Approve requests above a cost limit
            - Show the warehouse a queue to pick and ship
            - Report sample cost per rep and customer
API:        REST
            POST /requests
            POST /requests/{id}/ship
            GET  /reports/cost
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 340

**Intent:**
employees must read and accept new policies, we need proof who signed what

**Spec:**
```
Type:       Web application (policy acknowledgements)
Auth:       Employee login via company SSO
Data model: Policy(id, title, version, document_url, published_at, required_for)
            Acknowledgement(id, policy_id -> Policy, employee_email, accepted_at, ip_address)
Features:   - Publish a new policy version to chosen departments
            - Require employees to open and accept it
            - Remind people who haven't accepted after 7 days
            - Export a signed-off list for audits
API:        REST
            POST /policies
            POST /policies/{id}/accept
            GET  /policies/{id}/status
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Okta
```

---

## Example 341

**Intent:**
nurses bid on open shifts and the most senior one gets it

**Spec:**
```
Type:       Web application (shift bidding)
Auth:       Staff login (email + password); scheduler role
Data model: StaffNurse(id, name, hire_date, unit, grade)
            OpenShift(id, unit, date, start_time, end_time, grade, bidding_closes_at)
            ShiftBid(id, shift_id -> OpenShift, nurse_id -> StaffNurse, placed_at)
Features:   - Post open shifts with a bidding deadline
            - Let eligible nurses bid
            - Award each shift to the most senior bidder at close
            - Prevent awards that break rest-time rules
            - Notify winners and other bidders
API:        REST
            POST /shifts
            POST /shifts/{id}/bids
            POST /shifts/{id}/award
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Vue.js
```

---

## Example 342

**Intent:**
candidates pick their own interview time from slots the hiring manager opens

**Spec:**
```
Type:       Web application (interview scheduling)
Auth:       Hiring manager login (Google SSO); candidates use a private link
Data model: InterviewRound(id, job_title, manager_email, duration_min, video_link)
            InterviewSlot(id, round_id -> InterviewRound, starts_at, candidate_id -> Candidate)
            Candidate(id, name, email, invite_token)
Features:   - Open slots from free times in the manager's Google Calendar
            - Send candidates a private link to pick a slot
            - Create the calendar event with a video link
            - Let candidates reschedule once
API:        REST
            POST /rounds
            GET  /pick/{token}
            POST /pick/{token}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Google Calendar API
```

---

## Example 343

**Intent:**
builder job costing, estimate vs actual for labour and materials on each house extension

**Spec:**
```
Type:       Web application (job costing)
Auth:       Owner and site manager login
Data model: BuildJob(id, client, address, contract_value, status)
            EstimateLine(id, job_id -> BuildJob, category, description, estimated_cost)
            ActualCost(id, job_id -> BuildJob, category, description, amount, date, receipt_url)
            LabourDay(id, job_id -> BuildJob, worker, date, hours, rate)
Features:   - Build an estimate by category
            - Record material receipts and labour days against jobs
            - Compare estimate and actual per category
            - Show forecast profit per job
API:        REST
            POST /jobs/{id}/costs
            POST /jobs/{id}/labour
            GET  /jobs/{id}/variance
Storage:    PostgreSQL, S3 (receipts)
Tech stack: TypeScript, Remix, Prisma
```

---

## Example 344

**Intent:**
subcontractors must upload insurance and certificates before working on our sites

**Spec:**
```
Type:       Web application (subcontractor compliance)
Auth:       Subcontractor login; compliance officer login
Data model: Subcontractor(id, company, trade, contact_email, status)
            ComplianceDoc(id, subcontractor_id -> Subcontractor, type, file_url, expires_on, approved)
            SiteAssignment(id, subcontractor_id -> Subcontractor, site, start_date)
Features:   - Upload insurance, licences and method statements
            - Approve or reject documents
            - Block site assignments for non-compliant companies
            - Remind subcontractors before documents expire
API:        REST
            POST /subcontractors/{id}/documents
            PATCH /documents/{id}
            POST /assignments
Storage:    PostgreSQL, S3 (documents)
Tech stack: Python, Django, AWS S3
```

---

## Example 345

**Intent:**
snag list for new build houses, site manager logs defects with photo and trade fixes them

**Spec:**
```
Type:       Web application (snagging)
Auth:       Site manager and trade login (email + password)
Data model: Plot(id, development, number, handover_date)
            Snag(id, plot_id -> Plot, room, description, trade, photo_url, status, created_at)
            SnagFix(id, snag_id -> Snag, fixed_by, fixed_at, photo_url)
Features:   - Log snags by plot and room with a photo
            - Assign each snag to a trade
            - Let trades mark fixes with an after photo
            - Show outstanding snags before handover
API:        REST
            POST /plots/{id}/snags
            POST /snags/{id}/fix
            GET  /plots/{id}/snags?status=open
Storage:    PostgreSQL, S3 (photos)
Tech stack: Vue.js (PWA), Node.js, Fastify
```

---

## Example 346

**Intent:**
kitchen fitter company, book a home measure then design then fitting days

**Spec:**
```
Type:       Web application (project scheduling)
Auth:       Staff login; customer portal by email link
Data model: KitchenCustomer(id, name, address, phone, email)
            KitchenProject(id, customer_id -> KitchenCustomer, stage, design_url, price)
            ProjectAppointment(id, project_id -> KitchenProject, type, starts_at, staff)
Features:   - Book a free measure visit online
            - Share the design with the customer for approval
            - Schedule fitting days once the deposit is paid
            - Show each fitter their upcoming jobs
API:        REST
            POST /measures
            POST /projects/{id}/design
            POST /projects/{id}/fitting
Storage:    PostgreSQL
Tech stack: PHP, Symfony, Stripe
```

---

## Example 347

**Intent:**
carpet fitter quote: put room sizes and pick carpet, it works out how many metres from the roll

**Spec:**
```
Type:       Web application (flooring quotes)
Auth:       Fitter login
Data model: Carpet(id, name, roll_width_m, price_per_m2)
            FloorQuote(id, customer_name, address, carpet_id -> Carpet, total_m2, fitting_price, total)
            QuoteRoom(id, quote_id -> FloorQuote, name, length_m, width_m)
Features:   - Enter room measurements
            - Calculate roll length needed with the roll width and seams
            - Add underlay, gripper and fitting costs
            - Email the customer a PDF quote
API:        REST
            POST /quotes
            POST /quotes/{id}/rooms
            GET  /quotes/{id}/pdf
Storage:    SQLite
Tech stack: Python, FastAPI, ReportLab
```

---

## Example 348

**Intent:**
electrician inspection reports (EICR) filled in on tablet and PDF certificate generated

**Spec:**
```
Type:       Web application (inspection certificates)
Auth:       Electrician login (email + password)
Data model: Installation(id, address, client_name, client_email)
            Inspection(id, installation_id -> Installation, inspected_on, overall_result, next_due)
            Circuit(id, inspection_id -> Inspection, number, description, rcd_ms, insulation_mohm, zs_ohm)
            Observation(id, inspection_id -> Inspection, code, text)
Features:   - Enter circuit test results in a schedule
            - Record observations with C1, C2, C3 codes
            - Set the overall result from observation codes
            - Generate the certificate as a PDF
            - Remind clients when the next inspection is due
API:        REST
            POST /inspections
            POST /inspections/{id}/circuits
            GET  /inspections/{id}/certificate
Storage:    PostgreSQL
Tech stack: TypeScript, React, NestJS, pdfmake
```

---

## Example 349

**Intent:**
landlords' gas safety certs, remind landlord and book engineer before it expires

**Spec:**
```
Type:       Web application (compliance reminders)
Auth:       Agent login
Data model: Landlord(id, name, email)
            RentalProperty(id, landlord_id -> Landlord, address, tenant_phone)
            GasCertificate(id, property_id -> RentalProperty, issued_on, expires_on, file_url)
            EngineerVisit(id, property_id -> RentalProperty, engineer, date, status)
Features:   - Upload certificates with expiry dates
            - Email landlords 60 days before expiry
            - Book an engineer and text the tenant the date
            - Show properties without a valid certificate
API:        REST
            POST /properties/{id}/certificates
            POST /properties/{id}/visits
            GET  /properties?cert_expired=true
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio
```

---

## Example 350

**Intent:**
office cleaning contracts, cleaners scan QR in each office to prove they cleaned it

**Spec:**
```
Type:       Web application (cleaning verification)
Auth:       Cleaner login (PIN); supervisor and client login
Data model: ClientSite(id, name, address)
            Area(id, site_id -> ClientSite, name, qr_code, frequency)
            CleanLog(id, area_id -> Area, cleaner, scanned_at, checklist_done)
            Complaint(id, area_id -> Area, text, created_at, resolved)
Features:   - Scan an area QR code and tick its checklist
            - Show supervisors areas missed today
            - Let clients raise complaints per area
            - Send clients a monthly cleaning report
API:        REST
            POST /areas/{qr}/logs
            GET  /sites/{id}/missed?date={date}
            POST /areas/{id}/complaints
Storage:    PostgreSQL
Tech stack: Node.js, Express, React (PWA)
```

---

## Example 351

**Intent:**
private dining room enquiries for our restaurant, menus, deposits and final numbers

**Spec:**
```
Type:       Web application (private events)
Auth:       Events manager login
Data model: PrivateEvent(id, host_name, email, date, guests, menu_id -> SetMenu, min_spend, deposit_paid, status)
            SetMenu(id, name, price_per_head, courses)
            EventNote(id, event_id -> PrivateEvent, text)
Features:   - Take enquiries with date and party size
            - Send set menu options and a deposit link
            - Collect final numbers and dietary needs a week before
            - Print the event sheet for the kitchen
API:        REST
            POST /events
            POST /events/{id}/deposit
            GET  /events/{id}/sheet
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 352

**Intent:**
food bank: record which families visit and what they got, limit 1 visit per week

**Spec:**
```
Type:       Web application (client visits)
Auth:       Volunteer login (email + password)
Data model: Household(id, reference, members, postcode, dietary_needs, referred_by)
            FoodVisit(id, household_id -> Household, visited_on, parcel_type, volunteer)
Features:   - Search households by reference
            - Record visits and parcel type
            - Warn when a household visited in the last 7 days
            - Report visits and people fed per month
API:        REST
            GET  /households?ref={ref}
            POST /households/{id}/visits
            GET  /reports/monthly
Storage:    PostgreSQL
Tech stack: Python, Flask, Bootstrap
```

---

## Example 353

**Intent:**
night shelter beds, staff allocate beds each evening and keep notes on guests

**Spec:**
```
Type:       Web application (bed allocation)
Auth:       Staff login with 2FA
Data model: ShelterGuest(id, name, birth_year, support_needs, banned_until)
            ShelterBed(id, room, label)
            Stay(id, guest_id -> ShelterGuest, bed_id -> ShelterBed, date)
            CaseNote(id, guest_id -> ShelterGuest, author, text, created_at)
Features:   - Allocate free beds each evening
            - Keep the same bed for returning guests where possible
            - Record case notes visible only to staff
            - Show nightly occupancy and turned-away counts
API:        REST
            POST /stays
            GET  /beds/free?date={date}
            POST /guests/{id}/notes
Storage:    PostgreSQL (encrypted at rest)
Tech stack: Python, Django
```

---

## Example 354

**Intent:**
animal shelter adoptions, people apply for a dog and we do home check

**Spec:**
```
Type:       Web application (adoptions)
Auth:       Staff login; adopters register with email
Data model: ShelterAnimal(id, name, species, age, temperament, photo_url, status)
            Adopter(id, name, email, home_type, has_garden, other_pets)
            AdoptionApplication(id, animal_id -> ShelterAnimal, adopter_id -> Adopter, status, submitted_at)
            HomeCheck(id, application_id -> AdoptionApplication, date, volunteer, passed, notes)
Features:   - List adoptable animals with photos
            - Submit an adoption application
            - Schedule and record home checks
            - Approve adoptions and collect the fee
API:        REST
            GET  /animals?species={s}
            POST /animals/{id}/applications
            POST /applications/{id}/home-check
Storage:    PostgreSQL, S3 (photos)
Tech stack: TypeScript, Next.js, Stripe
```

---

## Example 355

**Intent:**
seniors centre classes (chair yoga, computer help) members sign up n we print registers

**Spec:**
```
Type:       Web application (class signups)
Auth:       Staff login; members sign up at reception or online
Data model: CentreMember(id, name, phone, emergency_contact, mobility_notes)
            CentreClass(id, title, weekday, time, room, places)
            ClassSignup(id, class_id -> CentreClass, member_id -> CentreMember)
Features:   - Sign members up for weekly classes
            - Use large text and simple buttons for older users
            - Print registers with emergency contacts
            - Text members when a class is cancelled
API:        REST
            GET  /classes
            POST /classes/{id}/signups
            GET  /classes/{id}/register
Storage:    SQLite
Tech stack: Python, Django, Twilio
```

---

## Example 356

**Intent:**
meals on wheels routes for volunteers drivers, who gets which meal, special diets

**Spec:**
```
Type:       Web application (meal delivery routes)
Auth:       Coordinator and driver login
Data model: MealClient(id, name, address, latitude, longitude, diet, key_info)
            MealRoute(id, name, weekday, driver_name)
            RouteStop(route_id -> MealRoute, client_id -> MealClient, order)
            MealDelivery(id, client_id -> MealClient, date, delivered, wellbeing_note)
Features:   - Organise clients into ordered delivery routes
            - Print route sheets with diets and access notes
            - Record delivery and a wellbeing check
            - Alert the coordinator when a client doesn't answer
API:        REST
            GET  /routes/{id}?date={date}
            POST /deliveries
            POST /deliveries/{id}/alert
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Leaflet
```

---

## Example 357

**Intent:**
tool library for our neighbourhood, people borrow tools for a week

**Spec:**
```
Type:       Web application (lending library)
Auth:       Member login (email + password); volunteer role
Data model: LendTool(id, name, category, condition, photo_url)
            LibraryMember(id, name, email, phone, annual_fee_paid)
            ToolLoan(id, tool_id -> LendTool, member_id -> LibraryMember, out_on, due_on, returned_on)
Features:   - Browse and reserve tools online
            - Lend tools for 7 days at opening hours
            - Remind members before the due date
            - Track condition after each return
API:        REST
            GET  /tools?category={c}
            POST /tools/{id}/reserve
            POST /loans/{id}/return
Storage:    SQLite
Tech stack: Python, Flask, HTMX
```

---

## Example 358

**Intent:**
virtual office: we receive post for companies, scan it and they decide forward or shred

**Spec:**
```
Type:       Web application (mail handling)
Auth:       Client login (email + password, 2FA); staff login
Data model: ClientCompany(id, name, plan, forwarding_address)
            MailItem(id, company_id -> ClientCompany, sender, received_on, envelope_scan_url, content_scan_url, action, status)
Features:   - Log incoming mail with an envelope scan
            - Let clients request open-and-scan, forward or shred
            - Upload scanned contents
            - Bill forwarding postage monthly
API:        REST
            POST /mail
            POST /mail/{id}/action
            POST /mail/{id}/scan
Storage:    PostgreSQL, S3 (scans, encrypted)
Tech stack: Python, Django, AWS S3
```

---

## Example 359

**Intent:**
bookkeeper portal, clients upload receipts and bank statements each month and I tick off what came in

**Spec:**
```
Type:       Web application (client document collection)
Auth:       Bookkeeper login; client login (email + password)
Data model: BookkeepingClient(id, business_name, email)
            MonthlyChecklist(id, client_id -> BookkeepingClient, month, status)
            RequiredDoc(id, checklist_id -> MonthlyChecklist, name, received)
            ClientUpload(id, client_id -> BookkeepingClient, month, file_url, uploaded_at)
Features:   - Create a monthly checklist per client
            - Let clients upload receipts and statements
            - Tick off items as they arrive
            - Chase clients with missing items by email
API:        REST
            POST /clients/{id}/uploads
            PATCH /required-docs/{id}
            POST /chase/run?month={month}
Storage:    PostgreSQL, S3 (documents)
Tech stack: TypeScript, SvelteKit, AWS S3
```

---

## Example 360

**Intent:**
immigration law firm, clients log in and see where their visa case is at

**Spec:**
```
Type:       Web application (client case portal)
Auth:       Client login (email + password, 2FA); staff login
Data model: VisaCase(id, client_id -> Client, visa_type, stage, submitted_on, decision)
            Client(id, name, email, nationality)
            CaseMessage(id, case_id -> VisaCase, from_staff, text, created_at)
            CaseUpload(id, case_id -> VisaCase, name, url)
Features:   - Show the client a timeline of their case stages
            - Request and receive documents securely
            - Message the case worker
            - Notify clients when the stage changes
API:        REST
            GET  /cases/me
            POST /cases/{id}/messages
            POST /cases/{id}/uploads
Storage:    PostgreSQL, S3 (encrypted)
Tech stack: Python, Django, AWS S3
```

---

## Example 361

**Intent:**
open house sign in sheet on ipad for real estate agents, follow up leads after

**Spec:**
```
Type:       Web application (open house sign-in)
Auth:       Agent login (email + password)
Data model: OpenHouse(id, agent_id -> Agent, address, date)
            Visitor(id, open_house_id -> OpenHouse, name, email, phone, has_agent, buying_timeline)
            Agent(id, name, email)
Features:   - Show a sign-in form in kiosk mode on a tablet
            - Ask if the visitor already has an agent
            - Send a thank-you email with the listing details
            - Export visitors as leads to the CRM
API:        REST
            POST /open-houses
            POST /open-houses/{id}/visitors
            GET  /open-houses/{id}/visitors.csv
Storage:    SQLite
Tech stack: Python, Flask, Alpine.js
```

---

## Example 362

**Intent:**
we manage flats for owners and need to send each owner a monthly statement: rent in, our fee, repairs, payout

**Spec:**
```
Type:       Web application (owner statements)
Auth:       Staff login; owner login to view statements
Data model: PropertyOwner(id, name, email, iban)
            ManagedFlat(id, owner_id -> PropertyOwner, address, fee_pct)
            LedgerEntry(id, flat_id -> ManagedFlat, date, type, description, amount)
            OwnerStatement(id, owner_id -> PropertyOwner, month, rent_total, fees, expenses, payout, pdf_url)
Features:   - Record rent received and repair costs per flat
            - Calculate management fees automatically
            - Generate monthly PDF statements per owner
            - Export the payout batch for the bank
API:        REST
            POST /flats/{id}/ledger
            POST /statements/run?month={month}
            GET  /owners/me/statements
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, QuestPDF
```

---

## Example 363

**Intent:**
box office for a 300 cap music venue, online sales plus will call list at the door

**Spec:**
```
Type:       Web application (box office)
Auth:       Venue staff login; buyers check out as guests
Data model: Gig(id, artist, doors_at, capacity, price, age_limit)
            TicketOrder(id, gig_id -> Gig, name, email, quantity, delivery, total, paid)
            DoorCheck(id, order_id -> TicketOrder, checked_at, count)
Features:   - Sell tickets online with e-ticket or will-call pickup
            - Print the will-call list alphabetically
            - Sell remaining tickets on the door
            - Show capacity left live during the night
API:        REST
            POST /gigs/{id}/orders
            GET  /gigs/{id}/will-call
            POST /orders/{id}/check
Storage:    PostgreSQL
Tech stack: Node.js, Express, Svelte, Stripe
```

---

## Example 364

**Intent:**
table tennis club tournament brackets, draw, scores, next match on screen

**Spec:**
```
Type:       Web application (tournament brackets)
Auth:       Tournament director login
Data model: Tournament(id, name, date, format)
            TtPlayer(id, tournament_id -> Tournament, name, rating, seed)
            TtMatch(id, tournament_id -> Tournament, round, table_no, player1_id -> TtPlayer, player2_id -> TtPlayer, games, winner_id -> TtPlayer)
Features:   - Seed players by rating and draw the bracket
            - Assign matches to free tables
            - Enter game scores and advance winners
            - Show the bracket and next calls on a screen
API:        REST + WebSocket
            POST /tournaments/{id}/draw
            POST /matches/{id}/score
            WS   /tournaments/{id}/live
Storage:    SQLite
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 365

**Intent:**
pet sitting business, clients book home visits for cats while on holiday, keys, notes, photo updates

**Spec:**
```
Type:       Web application (pet sitting)
Auth:       Client login (email + password); sitter login
Data model: PetClient(id, name, address, key_code, alarm_code_encrypted)
            Pet(id, client_id -> PetClient, name, species, feeding, medication)
            SitVisit(id, client_id -> PetClient, sitter, date, slot, done_at, notes, photo_url)
Features:   - Book daily visits for holiday dates
            - Store key and alarm details securely
            - Show sitters the day's visits with pet care notes
            - Send owners a photo update after each visit
API:        REST
            POST /visits
            GET  /sitters/me/visits?date={date}
            POST /visits/{id}/complete
Storage:    PostgreSQL (encrypted fields), S3 (photos)
Tech stack: Ruby on Rails, Twilio, AWS S3
```

---

## Example 366

**Intent:**
nursing agency, care homes post shifts they need covered and our nurses accept them

**Spec:**
```
Type:       Web application (agency shift marketplace)
Auth:       Care home, nurse and agency admin login (email + password)
Data model: CareHome(id, name, address, charge_rate)
            AgencyNurse(id, name, grade, pin_number, pin_expiry)
            CoverShift(id, home_id -> CareHome, date, start_time, end_time, grade, nurse_id -> AgencyNurse, status)
            ShiftTimesheet(id, shift_id -> CoverShift, hours, signed_by)
Features:   - Let care homes post shifts by grade
            - Show matching shifts to qualified nurses
            - Block nurses with expired registration
            - Get timesheets signed by the home
            - Invoice homes and pay nurses weekly
API:        REST
            POST /shifts
            POST /shifts/{id}/accept
            POST /shifts/{id}/timesheet
Storage:    PostgreSQL
Tech stack: Python, Django, React
```

---

## Example 367

**Intent:**
self audit checklist for each of our restaurants every month, scores and photos, area manager reviews

**Spec:**
```
Type:       Web application (site audits)
Auth:       Restaurant manager and area manager login
Data model: Restaurant(id, name, area_manager_email)
            AuditTemplate(id, name, questions_json)
            Audit(id, restaurant_id -> Restaurant, template_id -> AuditTemplate, month, score, submitted_at)
            AuditAnswer(audit_id -> Audit, question, score, comment, photo_url)
Features:   - Complete a monthly audit checklist with photos
            - Score each section and the total
            - Create actions for failed questions
            - Compare scores across restaurants
API:        REST
            POST /audits
            GET  /audits?month={month}
            GET  /reports/ranking
Storage:    PostgreSQL, S3 (photos)
Tech stack: TypeScript, React, NestJS
```

---

## Example 368

**Intent:**
florist weekly fresh flowers subscription for offices and restaurants, delivery route every monday

**Spec:**
```
Type:       Web application (B2B flower subscriptions)
Auth:       Florist login; business client login
Data model: BusinessClient(id, name, address, vase_count, budget_per_week)
            FlowerSubscription(id, client_id -> BusinessClient, frequency, start_date, active)
            WeeklyDelivery(id, subscription_id -> FlowerSubscription, date, arrangement_notes, delivered)
Features:   - Set up weekly or fortnightly subscriptions
            - Plan Monday deliveries in route order
            - Record what was delivered to each client
            - Invoice clients monthly
API:        REST
            POST /subscriptions
            GET  /deliveries?date={date}
            PATCH /deliveries/{id}
Storage:    SQLite
Tech stack: Python, Django, Stripe Invoicing
```

---

## Example 369

**Intent:**
sign making shop jobs from quote → design proof → production → install date

**Spec:**
```
Type:       Web application (job workflow)
Auth:       Staff login
Data model: SignJob(id, customer, description, size, material, price, stage, install_date)
            ProofVersion(id, job_id -> SignJob, file_url, version, approved)
            InstallSlot(id, job_id -> SignJob, date, crew)
Features:   - Track jobs across workflow stages on a board
            - Send design proofs and record approval
            - Book install dates with crews
            - Show jobs waiting on customer approval
API:        REST
            PATCH /jobs/{id}/stage
            POST /jobs/{id}/proofs
            POST /jobs/{id}/install
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 370

**Intent:**
embroidered uniforms for local companies, they reorder same logo items often

**Spec:**
```
Type:       Web application (B2B reorder portal)
Auth:       Company buyer login; shop staff login
Data model: CompanyAccount(id, name, logo_file_url, stitch_count)
            UniformItem(id, company_id -> CompanyAccount, garment, colour, logo_position, price)
            UniformOrder(id, company_id -> CompanyAccount, status, total, created_at)
            UniformOrderLine(order_id -> UniformOrder, item_id -> UniformItem, size, quantity, name_text)
Features:   - Show each company its approved uniform items
            - Reorder items with sizes and optional name embroidery
            - Reuse the stored logo file
            - Track orders through embroidery and dispatch
API:        REST
            GET  /companies/me/items
            POST /orders
            PATCH /orders/{id}/status
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Inertia.js, Vue.js
```

---

## Example 371

**Intent:**
e-bike rentals in our seaside town, track battery charge and which bikes are out

**Spec:**
```
Type:       Web application (bike rental)
Auth:       Staff login; customers book as guests
Data model: Ebike(id, number, size, battery_pct, status)
            BikeRental(id, ebike_id -> Ebike, customer_name, phone, starts_at, hours, helmet, price, returned_at)
Features:   - Book bikes by size for half or full days
            - Record battery level at return
            - Hide bikes below 50% battery until charged
            - Show bikes out and due back
API:        REST
            GET  /bikes/available?date={date}
            POST /rentals
            POST /rentals/{id}/return
Storage:    SQLite
Tech stack: Python, Flask, Stripe
```

---

## Example 372

**Intent:**
ice rink skating sesion tickets + skate hire sizes

**Spec:**
```
Type:       Web application (session tickets)
Auth:       Staff login; customers buy as guests
Data model: SkateSession(id, starts_at, type, capacity, price)
            SessionTicket(id, session_id -> SkateSession, email, adults, children, skate_sizes, total)
Features:   - Sell tickets per session up to capacity
            - Add skate hire with sizes
            - Show staff a skate size count per session
            - Scan tickets at entry
API:        REST
            GET  /sessions?date={date}
            POST /sessions/{id}/tickets
            GET  /sessions/{id}/skates
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 373

**Intent:**
public swimming pool lane booking for lap swimmers, slow medium fast lanes

**Spec:**
```
Type:       Web application (lane booking)
Auth:       Swimmer login (email + password)
Data model: PoolLane(id, number, speed)
            LaneSession(id, starts_at, duration_min, swimmers_per_lane)
            LaneBooking(id, session_id -> LaneSession, lane_id -> PoolLane, swimmer_id -> Swimmer)
            Swimmer(id, name, email, member)
Features:   - Book a lane by speed for a session
            - Limit swimmers per lane
            - Charge non-members per swim
            - Show reception who is booked in each lane
API:        REST
            GET  /sessions/{id}/lanes
            POST /bookings
            DELETE /bookings/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, SvelteKit, Stripe
```

---

## Example 374

**Intent:**
art gallery sells works for artists on commission, track artworks, sales and pay artists

**Spec:**
```
Type:       Web application (gallery consignment)
Auth:       Gallery staff login; artist login to view sales
Data model: Artist(id, name, email, commission_pct)
            Artwork(id, artist_id -> Artist, title, medium, size, price, status, location)
            ArtSale(id, artwork_id -> Artwork, buyer_name, price, sold_on)
            ArtistPayment(id, artist_id -> Artist, amount, paid_on)
Features:   - Catalogue consigned artworks with photos
            - Record sales and calculate artist share
            - Show artists their stock and sales
            - Pay artists monthly
API:        REST
            POST /artworks
            POST /artworks/{id}/sell
            GET  /artists/me/statement
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, Django, AWS S3
```

---

## Example 375

**Intent:**
picture framing shop calculator, moulding, mount, glass, price from size

**Spec:**
```
Type:       Web application (framing quotes and orders)
Auth:       Shop staff login
Data model: Moulding(id, code, width_mm, price_per_m, stock_m)
            MountBoard(id, colour, price_per_m2)
            GlassType(id, name, price_per_m2)
            FrameOrder(id, customer_name, phone, art_width_mm, art_height_mm, moulding_id -> Moulding, mount_id -> MountBoard, glass_id -> GlassType, price, status)
Features:   - Calculate moulding length including mitre waste
            - Price mount and glass by area
            - Add labour by frame size
            - Save the order and print a workshop ticket
API:        REST
            POST /quotes
            POST /orders
Storage:    SQLite
Tech stack: Python, FastAPI, Alpine.js
```

---

## Example 376

**Intent:**
jeweller custom ring commissions, sketches, client approves, payments in stages

**Spec:**
```
Type:       Web application (commission tracking)
Auth:       Jeweller login; client access by email link
Data model: Commission(id, client_name, email, piece_type, metal, stone, budget, stage)
            DesignSketch(id, commission_id -> Commission, image_url, version, approved)
            StagePayment(id, commission_id -> Commission, label, amount, paid_at)
Features:   - Record commission requirements and budget
            - Share sketches and 3D renders for approval
            - Take staged payments (deposit, casting, final)
            - Track stages from design to collection
API:        REST
            POST /commissions
            POST /commissions/{id}/sketches
            POST /payments/{id}/pay
Storage:    PostgreSQL, S3 (images)
Tech stack: TypeScript, Next.js, Stripe
```

---

## Example 377

**Intent:**
phone shop buys used phones, staff grade condition and app gives a price

**Spec:**
```
Type:       Web application (trade-in valuation)
Auth:       Staff login (PIN)
Data model: PhoneModel(id, brand, model, storage_gb, base_price)
            GradeRule(id, grade, multiplier)
            TradeIn(id, model_id -> PhoneModel, imei, grade, battery_health, price_offered, seller_id_number, accepted)
Features:   - Pick model and storage to get the base price
            - Grade screen, body and battery condition
            - Calculate an offer price from grade rules
            - Check the IMEI against a blacklist
            - Add accepted phones to resale stock
API:        REST
            POST /trade-ins/quote
            POST /trade-ins
            GET  /imei/{imei}/check
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 378

**Intent:**
school lends chromebooks 2 students, track who has which one and damages

**Spec:**
```
Type:       Web application (device loans)
Auth:       IT staff login (Google Workspace SSO)
Data model: Device(id, asset_tag, serial_no, model, status)
            DeviceLoan(id, device_id -> Device, student_email, issued_on, returned_on, agreement_signed)
            DamageReport(id, device_id -> Device, description, cost, charged_to)
Features:   - Issue devices by scanning asset tags
            - Record signed loan agreements
            - Log damage and repair charges
            - Collect all devices at the end of the year
API:        REST
            POST /loans
            POST /loans/{id}/return
            POST /devices/{id}/damage
Storage:    PostgreSQL
Tech stack: Python, Django, Google Admin SDK
```

---

## Example 379

**Intent:**
repair cafe events monthly, people register broken item, we match with volunteer fixer

**Spec:**
```
Type:       Web application (repair events)
Auth:       Organiser login; visitors register without account
Data model: RepairEvent(id, date, venue)
            Fixer(id, name, skills)
            BrokenItem(id, event_id -> RepairEvent, owner_name, email, category, problem, fixer_id -> Fixer, outcome)
Features:   - Register an item for the next event
            - Match items to fixers by skill
            - Record whether each item was fixed
            - Report kilograms saved from landfill
API:        REST
            POST /events/{id}/items
            PATCH /items/{id}
            GET  /reports/impact
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 380

**Intent:**
scaffolding hire, track what equipment is on which site and bill per week

**Spec:**
```
Type:       Web application (equipment hire tracking)
Auth:       Office and yard staff login
Data model: ScaffoldComponent(id, name, weekly_rate, yard_quantity)
            HireSite(id, customer, address, start_date, end_date)
            SiteDelivery(id, site_id -> HireSite, component_id -> ScaffoldComponent, quantity, direction, date)
Features:   - Record deliveries and collections per site
            - Show what is on each site right now
            - Bill weekly hire per component
            - Show yard stock available
API:        REST
            POST /sites/{id}/deliveries
            GET  /sites/{id}/onsite
            POST /invoices/run?week={date}
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 381

**Intent:**
intranet news for staff and we need to see who read the important ones

**Spec:**
```
Type:       Web application (intranet announcements)
Auth:       Employee login via Microsoft 365 SSO
Data model: Announcement(id, title, body, author, important, published_at)
            ReadReceipt(id, announcement_id -> Announcement, user_email, read_at)
Features:   - Publish news posts with rich text
            - Mark posts as important
            - Record when each employee reads a post
            - Show read rates for important posts
API:        REST
            GET  /announcements
            POST /announcements
            POST /announcements/{id}/read
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Microsoft Entra ID
```

---

## Example 382

**Intent:**
price lists for our sales team, different prices per customer group, always up to date

**Spec:**
```
Type:       Web application (price list management)
Auth:       Sales and pricing manager login
Data model: CatalogItem(id, sku, name, cost)
            CustomerGroup(id, name, margin_pct)
            PriceOverride(id, item_id -> CatalogItem, group_id -> CustomerGroup, price, valid_from)
Features:   - Calculate prices from cost and group margin
            - Override prices for specific items and groups
            - Schedule price changes from a future date
            - Export a PDF price list per group
API:        REST
            GET  /prices?group={id}
            POST /overrides
            GET  /pricelists/{group}.pdf
Storage:    PostgreSQL
Tech stack: Python, FastAPI, WeasyPrint
```

---

## Example 383

**Intent:**
nail salon

**Spec:**
```
Type:       Web application (booking system)
Auth:       Client login (phone + SMS code); salon admin login
Data model: NailService(id, name, duration_min, price)
            NailTech(id, name)
            NailAppointment(id, client_phone, service_id -> NailService, tech_id -> NailTech, starts_at, status)
Features:   - Show the service menu with prices
            - Book an appointment with a technician
            - Send SMS reminders
            - Show the salon's daily schedule
API:        REST
            GET  /services
            POST /appointments
            GET  /schedule?date={date}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Twilio
```

---

## Example 384

**Intent:**
invoice app in Go please

**Spec:**
```
Type:       Web application (invoicing)
Auth:       User login (email + password)
Data model: Customer(id, name, email, address)
            Invoice(id, customer_id -> Customer, number, issued_on, due_on, status)
            InvoiceLine(id, invoice_id -> Invoice, description, quantity, unit_price, tax_rate)
Features:   - Create and edit invoices with line items
            - Number invoices automatically
            - Generate PDF invoices
            - Email invoices to customers
            - Track paid and overdue invoices
API:        REST
            GET  /invoices
            POST /invoices
            GET  /invoices/{id}/pdf
            POST /invoices/{id}/send
Storage:    PostgreSQL
Tech stack: Go, chi router, sqlc, gofpdf, HTMX
```

---

## Example 385

**Intent:**
inventory for a bakery's ingredients

**Spec:**
```
Type:       Web application (ingredient inventory)
Auth:       Baker login
Data model: BakeryIngredient(id, name, unit, quantity, reorder_level, supplier)
            IngredientDelivery(id, ingredient_id -> BakeryIngredient, quantity, received_on, best_before)
            DailyUsage(id, ingredient_id -> BakeryIngredient, quantity, date)
Features:   - Record deliveries with best-before dates
            - Deduct usage from each day's production
            - Show ingredients below reorder level
            - Warn about stock near its best-before date
API:        REST
            POST /deliveries
            POST /usage
            GET  /ingredients?low=true
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 386

**Intent:**
gym class booking in vue + firebase

**Spec:**
```
Type:       Web application (class booking)
Auth:       Firebase Authentication (email + Google)
Data model: FitClass(id, name, coach, starts_at, capacity, booked_count)
            FitBooking(id, class_id -> FitClass, uid, created_at)
Features:   - Show the week's classes with spaces left
            - Book and cancel a class
            - Prevent overbooking with a Firestore transaction
            - Send booking confirmation emails
Storage:    Cloud Firestore
Tech stack: Vue 3, Firebase Authentication, Cloud Firestore, Cloud Functions
```

---

## Example 387

**Intent:**
crm for plumbers

**Spec:**
```
Type:       Web application (CRM)
Auth:       Staff login (email + password)
Data model: PlumbCustomer(id, name, phone, email, address)
            PlumbJob(id, customer_id -> PlumbCustomer, description, scheduled_for, status, price)
            BoilerRecord(id, customer_id -> PlumbCustomer, make, model, installed_on, next_service)
Features:   - Keep customer records with job history
            - Record boilers installed at each address
            - Remind customers when the boiler service is due
            - Turn completed jobs into invoices
API:        REST
            GET  /customers?q={text}
            POST /customers/{id}/jobs
            GET  /boilers/due
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 388

**Intent:**
hotel housekeeping lost keys? no — I mean a room key card log, which card issued to which guest

**Spec:**
```
Type:       Web application (key card log)
Auth:       Front desk login (PIN)
Data model: KeyCard(id, card_uid, status)
            CardIssue(id, card_id -> KeyCard, room_number, guest_name, issued_at, expires_at, returned_at)
Features:   - Record which card is issued to which room and guest
            - Expire cards automatically at checkout time
            - Flag cards not returned
            - Search the history of a card
API:        REST
            POST /issues
            POST /issues/{id}/return
            GET  /cards/{uid}/history
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 389

**Intent:**
vet appointment booking

**Spec:**
```
Type:       Web application (booking system)
Auth:       Pet owner login (email + password); clinic staff login
Data model: PetOwner(id, name, email, phone)
            ClinicPet(id, owner_id -> PetOwner, name, species, breed)
            VetAppointment(id, pet_id -> ClinicPet, vet_name, starts_at, reason, status)
Features:   - Book appointments for a registered pet
            - Choose a vet and a reason for the visit
            - Send email reminders
            - Show the clinic's daily list
API:        REST
            GET  /slots?date={date}
            POST /appointments
            GET  /admin/appointments?date={date}
Storage:    PostgreSQL
Tech stack: Python, Django, Bootstrap
```

---

## Example 390

**Intent:**
staff schedule for a small hotel reception, front desk 24/7 in 3 shifts

**Spec:**
```
Type:       Web application (shift scheduling)
Auth:       Manager and staff login
Data model: ReceptionStaff(id, name, email, contract_hours)
            ShiftPattern(id, name, start_time, end_time)
            RosterEntry(id, staff_id -> ReceptionStaff, pattern_id -> ShiftPattern, date)
Features:   - Fill early, late and night shifts every day
            - Warn when a shift is uncovered
            - Enforce 11 hours rest between shifts
            - Show contract hours versus scheduled hours
API:        REST
            GET  /roster?week={date}
            POST /roster
            GET  /roster/gaps?week={date}
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Thymeleaf
```

---

## Example 391

**Intent:**
wanna let ppl book my tiny photography studio by the hour for their own shoots lol, like with lights and backdrops as extras

**Spec:**
```
Type:       Web application (studio hire)
Auth:       Owner login; hirers book with email confirmation
Data model: StudioExtra(id, name, price)
            StudioHire(id, hirer_name, email, starts_at, hours, total, paid, door_code)
            HireExtra(hire_id -> StudioHire, extra_id -> StudioExtra)
Features:   - Book the studio by the hour
            - Add lights, backdrops and props as extras
            - Pay in full at booking
            - Email a door code for the slot
API:        REST
            GET  /availability?date={date}
            POST /hires
Storage:    SQLite
Tech stack: Python, Flask, Stripe
```

---

## Example 392

**Intent:**
hi pls help we r a small kindergarden and parents pay monthly fee + lunch, need system who paid who not and send them invoice

**Spec:**
```
Type:       Web application (childcare billing)
Auth:       Admin login (email + password); parent login
Data model: KinderChild(id, name, parent_email, days_per_week, lunch)
            FeeRate(id, days_per_week, monthly_fee, lunch_fee)
            KinderInvoice(id, child_id -> KinderChild, month, amount, paid_at)
Features:   - Calculate monthly fees from days and lunch choice
            - Email invoices at the start of each month
            - Mark invoices paid from bank transfers
            - List unpaid invoices and send reminders
API:        REST
            POST /invoices/run?month={month}
            PATCH /invoices/{id}/paid
            GET  /invoices?unpaid=true
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Bootstrap
```

---

## Example 393

**Intent:**
i do mobile hair cuts for old people in care homes, need to know which home which day and who wants a cut

**Spec:**
```
Type:       Web application (visit scheduling)
Auth:       Hairdresser login; care home staff login
Data model: CareHomeSite(id, name, address, visit_weekday)
            HomeResident(id, home_id -> CareHomeSite, name, room, usual_service)
            HairRequest(id, resident_id -> HomeResident, visit_date, service, done, price)
Features:   - Let care home staff add residents who want a cut
            - Show a list per home for each visit day
            - Mark services done and the price
            - Bill each home monthly
API:        REST
            POST /requests
            GET  /visits?date={date}
            PATCH /requests/{id}
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 394

**Intent:**
gotta track my food truck fleet (3 trucks) - which event each truck is at, staff on it, sales per event

**Spec:**
```
Type:       Web application (event operations)
Auth:       Owner and manager login
Data model: Truck(id, name)
            TruckEvent(id, name, date, location, pitch_fee)
            Deployment(id, truck_id -> Truck, event_id -> TruckEvent, staff_names, sales_total)
Features:   - Assign trucks and staff to events
            - Record sales per deployment
            - Show profit after pitch fee per event
            - Show a calendar of upcoming events
API:        REST
            POST /deployments
            PATCH /deployments/{id}/sales
            GET  /reports/events
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 395

**Intent:**
need a app where my cleaners see the checklist for every airbnb and i see they finished. NOT the booking part, just the cleaning tasks

**Spec:**
```
Type:       Web application (cleaning checklists)
Auth:       Owner and cleaner login (email + password)
Data model: Apartment(id, name, address, checklist_items)
            CleanTask(id, apartment_id -> Apartment, cleaner_name, date, finished_at)
            CheckedItem(task_id -> CleanTask, item, done, photo_url)
Features:   - Define a checklist per apartment
            - Assign cleaning tasks by date
            - Tick items with optional photos
            - Show the owner finished and late tasks
API:        REST
            POST /tasks
            PATCH /tasks/{id}/items
            GET  /tasks?date={date}
Storage:    PostgreSQL
Tech stack: Vue.js (PWA), Python, FastAPI
```

---

## Example 396

**Intent:**
plz make it with wordpress. my yoga retreat weekends, people book a room type and pay deposit

**Spec:**
```
Type:       Plugin (WordPress retreat booking)
Auth:       WordPress admin login; guests book without an account
Data model: Retreat(id, title, start_date, end_date, description)
            RetreatRoom(id, retreat_id -> Retreat, type, price, beds_left)
            RetreatBooking(id, room_id -> RetreatRoom, name, email, dietary, deposit_paid)
Features:   - Add retreats and room types in the WordPress admin
            - Show a booking form with a shortcode
            - Take a deposit with WooCommerce
            - Email balance reminders before the retreat
Storage:    WordPress MySQL database (custom tables)
Tech stack: PHP, WordPress Plugin API, WooCommerce
```

---

## Example 397

**Intent:**
i want angular frontend + .net backend for our physio clinic exercise prescription system

**Spec:**
```
Type:       Web application (exercise prescription)
Auth:       Physio and patient login (ASP.NET Core Identity)
Data model: ExerciseLibraryItem(id, name, body_area, video_url)
            PhysioPatient(id, name, email)
            Prescription(id, patient_id -> PhysioPatient, created_on, notes)
            PrescribedExercise(prescription_id -> Prescription, exercise_id -> ExerciseLibraryItem, sets, reps, hold_sec)
Features:   - Search the exercise library by body area
            - Build a prescription with sets and reps
            - Show patients their exercises with videos
            - Let patients log completed sessions
API:        REST
            GET  /exercises?area={area}
            POST /patients/{id}/prescriptions
            POST /prescriptions/{id}/logs
Storage:    SQL Server
Tech stack: C#, ASP.NET Core Web API, Entity Framework Core, Angular
```

---

## Example 398

**Intent:**
our old microsoft access database for the tool hire shop needs replacing with something web based, same tables more or less: customers, items, hires

**Spec:**
```
Type:       Web application (Access migration)
Auth:       Staff login (email + password)
Data model: HireCustomer(id, name, phone, address, account_number)
            HireStockItem(id, code, name, day_rate, week_rate, status)
            HireContract(id, customer_id -> HireCustomer, item_id -> HireStockItem, out_date, due_date, returned_date, total)
Features:   - Import existing customers, items and hires from the Access file
            - Create, edit and close hire contracts
            - Calculate day and week rates
            - Print hire contracts
            - Search all past hires per customer
API:        REST
            POST /import
            POST /contracts
            POST /contracts/{id}/close
Storage:    PostgreSQL
Tech stack: Python, Django, mdbtools (import)
```

---

## Example 399

**Intent:**
build with flask and sqlite: a stock list for my charity shop's furniture warehouse, items with photos and sold or not

**Spec:**
```
Type:       Web application (furniture stock)
Auth:       Volunteer login (username + password)
Data model: FurnitureItem(id, title, category, condition, price, photo_path, location, status, added_on)
Features:   - Add furniture items with photos
            - Mark items reserved or sold
            - Filter by category and status
            - Show items unsold for over 60 days
API:        REST
            GET  /items?status=available
            POST /items
            PATCH /items/{id}
Storage:    SQLite, local disk (photos)
Tech stack: Python, Flask, SQLite, Jinja2
```

---

## Example 400

**Intent:**
mongodb + express backend for barber loyalty points, every 6th haircut free

**Spec:**
```
Type:       REST API service (loyalty points)
Auth:       API key for the shop tablet
Data model: LoyaltyCustomer(id, phone, name, visits, free_cuts_available)
            LoyaltyVisit(id, customer_id -> LoyaltyCustomer, date, free)
Features:   - Look up customers by phone number
            - Add a visit and count towards the free cut
            - Grant a free haircut after every 5 paid visits
            - Redeem a free haircut
API:        REST
            GET  /customers?phone={phone}
            POST /customers/{id}/visits
            POST /customers/{id}/redeem
Storage:    MongoDB
Tech stack: Node.js, Express, Mongoose
```

---

## Example 401

**Intent:**
Dear, I am owner of small guesthouse in Bali with 6 villa. I want guests can order airport pickup, scooter rent and tour from website before they come, and my staff see all orders in one list.

**Spec:**
```
Type:       Web application (guest services ordering)
Auth:       Staff login; guests use their booking code
Data model: GuestStay(id, booking_code, guest_name, villa, arrival, departure)
            GuestService(id, name, type, price)
            ServiceOrder(id, stay_id -> GuestStay, service_id -> GuestService, date, time, quantity, status)
Features:   - Order airport pickup with flight number
            - Rent scooters for chosen days
            - Book tours with pickup time
            - Show staff all orders by date
            - Add orders to the guest's bill
API:        REST
            GET  /services
            POST /stays/{code}/orders
            GET  /admin/orders?date={date}
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Midtrans
```

---

## Example 402

**Intent:**
We are small company in Vietnam make furniture for export. Need track each container: which orders inside, when loaded, documents, and when arrive to customer.

**Spec:**
```
Type:       Web application (export shipment tracking)
Auth:       Staff login; customer login to see their shipments
Data model: ExportOrder(id, customer, po_number, items, cbm, status)
            ShippingContainer(id, number, size, loaded_on, etd, eta, port, status)
            ContainerOrder(container_id -> ShippingContainer, order_id -> ExportOrder)
            ShippingDocument(id, container_id -> ShippingContainer, type, url)
Features:   - Plan which orders go into a container by volume
            - Record loading date and departure
            - Upload bill of lading and invoices
            - Show customers the ETA of their orders
API:        REST
            POST /containers
            POST /containers/{id}/orders
            POST /containers/{id}/documents
Storage:    PostgreSQL, S3 (documents)
Tech stack: Python, Django, AWS S3
```

---

## Example 403

**Intent:**
Good day. Our association of taxi drivers need system for collect monthly member fee and show who is not paid, and send the SMS.

**Spec:**
```
Type:       Web application (association dues)
Auth:       Treasurer login
Data model: DriverMember(id, name, phone, licence_no, joined_on)
            MemberFee(id, member_id -> DriverMember, month, amount, paid_on, method)
Features:   - Record monthly fees paid in cash or mobile money
            - Show members who have not paid this month
            - Send SMS reminders to unpaid members
            - Show yearly totals per member
API:        REST
            POST /fees
            GET  /fees/unpaid?month={month}
            POST /reminders
Storage:    PostgreSQL
Tech stack: Python, Django, Africa's Talking SMS API
```

---

## Example 404

**Intent:**
Hola, I have a small academy of English in Madrid. Need system for the teachers to put attendance and marks, and parents receive it in Spanish.

**Spec:**
```
Type:       Web application (academy management)
Auth:       Teacher and parent login (email + password)
Data model: AcademyGroup(id, level, schedule, teacher_id -> AcademyTeacher)
            AcademyTeacher(id, name, email)
            Pupil(id, name, group_id -> AcademyGroup, parent_email)
            AttendanceMark(id, pupil_id -> Pupil, date, present)
            Grade(id, pupil_id -> Pupil, term, skill, mark)
Features:   - Take attendance per class
            - Enter marks by skill each term
            - Send parents a monthly report
            - Show the parent area in Spanish
API:        REST
            POST /groups/{id}/attendance
            POST /pupils/{id}/grades
            GET  /parents/me/report
Storage:    PostgreSQL
Tech stack: Python, Django (i18n, Spanish locale)
```

---

## Example 405

**Intent:**
me and my partner have a restaurant in Germany, we need the cash book (Kassenbuch) digital, each day income and expenses, and export for tax advisor

**Spec:**
```
Type:       Web application (cash book)
Auth:       Owner login with 2FA
Data model: CashBookEntry(id, date, type, description, amount, vat_rate, receipt_url, created_at)
            DayClose(id, date, opening_balance, closing_balance, counted_cash, locked)
Features:   - Record daily cash income and expenses
            - Attach receipt photos
            - Close each day and lock entries against edits
            - Export entries in DATEV format for the tax advisor
API:        REST
            POST /entries
            POST /days/{date}/close
            GET  /export/datev?month={month}
Storage:    PostgreSQL
Tech stack: Python, Django, DATEV CSV export
```

---

## Example 406

**Intent:**
I'm opening a small barber academy in Lagos. Students pay school fees in parts, attend practical days, and we must issue certificate at end.

**Spec:**
```
Type:       Web application (training academy)
Auth:       Admin and instructor login; student login
Data model: Cohort(id, name, start_date, end_date, total_fee)
            AcademyStudent(id, cohort_id -> Cohort, name, phone, email)
            FeePayment(id, student_id -> AcademyStudent, amount, paid_on, reference)
            PracticalDay(id, cohort_id -> Cohort, date)
            DayAttendance(day_id -> PracticalDay, student_id -> AcademyStudent, present)
Features:   - Record part payments and show balance due
            - Take attendance on practical days
            - Check fee and attendance rules before certification
            - Generate PDF certificates with a verification code
API:        REST
            POST /students/{id}/payments
            POST /days/{id}/attendance
            POST /students/{id}/certificate
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Paystack, PDFKit
```

---

## Example 407

**Intent:**
My English not good, sorry. I have shop of spare parts for cars. I want know stock and when customer ask part, I search by car model.

**Spec:**
```
Type:       Web application (parts inventory)
Auth:       Staff login (username + password)
Data model: SparePart(id, part_number, name, brand, price, quantity, shelf)
            CarModel(id, make, model, year_from, year_to)
            PartFitment(part_id -> SparePart, car_model_id -> CarModel)
Features:   - Search parts by car make, model and year
            - Search by part number
            - Show stock and shelf location
            - Reduce stock when a part is sold
            - Show parts with low stock
API:        REST
            GET  /parts?make={m}&model={mo}&year={y}
            GET  /parts?number={no}
            POST /parts/{id}/sell
Storage:    PostgreSQL
Tech stack: Python, Django, Bootstrap
```

---

## Example 408

**Intent:**
we are clinic for physical therapy in Brazil, want patients book and pay sessions with Pix

**Spec:**
```
Type:       Web application (booking and payments)
Auth:       Patient login (email + password); therapist login
Data model: Fisio(id, name)
            Paciente(id, name, cpf, phone, email)
            Sessao(id, paciente_id -> Paciente, fisio_id -> Fisio, starts_at, price, paid, status)
Features:   - Book sessions with a chosen therapist
            - Generate a Pix QR code to pay each session
            - Confirm payment automatically via webhook
            - Send WhatsApp reminders the day before
API:        REST
            POST /sessoes
            POST /sessoes/{id}/pix
            POST /webhooks/pix
Storage:    PostgreSQL
Tech stack: Node.js, Express, Mercado Pago API, React
```

---

## Example 409

**Intent:**
small factory in Turkey make textile, we want see each order which step it is: cutting, sewing, ironing, packing

**Spec:**
```
Type:       Web application (production tracking)
Auth:       Supervisor and office login
Data model: TextileOrder(id, customer, model_code, quantity, due_date)
            ProductionStage(id, name, order)
            StageProgress(id, order_id -> TextileOrder, stage_id -> ProductionStage, pieces_done, updated_at)
Features:   - Update pieces done per stage from a tablet
            - Show each order's progress across stages
            - Highlight orders that will miss the due date
            - Show daily output per stage
API:        REST
            POST /orders/{id}/progress
            GET  /orders?late=true
            GET  /reports/daily-output
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 410

**Intent:**
i have a hostel in portugal and want volunteers (work exchange) to apply and pick weeks, and I accept them

**Spec:**
```
Type:       Web application (volunteer applications)
Auth:       Owner login; applicants register with email
Data model: VolunteerApplicant(id, name, email, country, languages, skills, cv_url)
            VolunteerWeek(id, start_date, places)
            VolunteerApplication(id, applicant_id -> VolunteerApplicant, week_ids, status, motivation)
Features:   - Apply with skills, languages and motivation
            - Pick weeks with free volunteer places
            - Accept or decline applications
            - Email accepted volunteers house rules and arrival info
API:        REST
            POST /applications
            GET  /weeks
            POST /applications/{id}/decision
Storage:    SQLite
Tech stack: Python, Flask, Jinja2
```

---

## Example 411

**Intent:**
honestly my biggest problem running the dance school is chasing parents for term fees. i have like 140 kids across 12 classes, some pay cash, some transfer, some have siblings with a discount, and at the end of each term i'm going through bank statements line by line. if something could tell me who's paid and send polite reminders I'd cry with happiness

**Spec:**
```
Type:       Web application (fee tracking)
Auth:       Owner login (email + password); parent login
Data model: DanceFamily(id, parent_name, email, phone, payment_reference)
            Dancer(id, family_id -> DanceFamily, name, class_ids)
            TermFee(id, family_id -> DanceFamily, term, amount, discount, paid_amount, status)
            BankTransaction(id, date, amount, reference, matched_fee_id -> TermFee)
Features:   - Calculate each family's term fee with sibling discounts
            - Import bank statement CSVs and match payments by reference
            - Record cash payments manually
            - Send polite reminders to unpaid families
            - Show a paid/unpaid list per class
API:        REST
            POST /fees/generate?term={term}
            POST /bank/import
            POST /reminders/send
Storage:    PostgreSQL
Tech stack: Python, Django, pandas, Postmark
```

---

## Example 412

**Intent:**
long story short, I took over my dad's hardware and garden supply store and he ran everything from memory. There's no stock system at all. Some stuff sells by weight (soil, seed), some by piece, some by metre (chain, rope). I'd like to scan things at the counter and know what we have and what to reorder, nothing too fancy.

**Spec:**
```
Type:       Web application (inventory and counter sales)
Auth:       Staff login (PIN)
Data model: StoreItem(id, barcode, name, unit_type, unit_price, quantity, reorder_level, supplier)
            CounterSale(id, total, sold_at, staff)
            CounterSaleLine(sale_id -> CounterSale, item_id -> StoreItem, quantity)
Features:   - Sell items by piece, weight or metre
            - Scan barcodes or search by name at the counter
            - Reduce stock with decimal quantities
            - Print labels for items without barcodes
            - Show a reorder list grouped by supplier
API:        REST
            GET  /items?q={text}
            POST /sales
            GET  /reorder
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 413

**Intent:**
So we're a small community radio station run by volunteers. We have about 40 presenters, a studio schedule, and we keep losing track of who's on when, who's done their training, and who's covering for who when someone's sick. Ideally presenters can see the schedule and swap slots themselves but the station manager approves.

**Spec:**
```
Type:       Web application (studio scheduling)
Auth:       Presenter login (email + password); station manager role
Data model: Presenter(id, name, email, trained_on_desk, trained_on_ofcom)
            Show(id, title, weekday, start_time, duration_min, presenter_id -> Presenter)
            CoverRequest(id, show_id -> Show, date, cover_presenter_id -> Presenter, status)
Features:   - Show the weekly studio schedule
            - Request cover for a show on a date
            - Let trained presenters offer to cover
            - Approve swaps as the station manager
            - Block untrained presenters from solo shows
API:        REST
            GET  /schedule?week={date}
            POST /cover-requests
            POST /cover-requests/{id}/approve
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 414

**Intent:**
ok this might be a weird one. I run a small funeral flower business and my orders come from funeral directors by phone, often last minute, with the deceased's name, service time and church. I write it on paper and twice I've sent flowers to the wrong church. I want something where the funeral director fills a form and I get a clear list per day with delivery address and time.

**Spec:**
```
Type:       Web application (order intake)
Auth:       Funeral director login (email + password); florist admin login
Data model: FuneralDirector(id, firm, contact_name, email, phone)
            TributeOrder(id, director_id -> FuneralDirector, deceased_name, service_at, venue_name, venue_address, tribute_type, card_message, status)
Features:   - Let funeral directors submit orders through a form
            - Require venue address and service time
            - Show a daily delivery list sorted by service time
            - Confirm each order to the director by email
            - Bill directors monthly
API:        REST
            POST /orders
            GET  /deliveries?date={date}
            POST /invoices/run?month={month}
Storage:    PostgreSQL
Tech stack: Python, Django, Google Maps Places API
```

---

## Example 415

**Intent:**
my mum runs a sewing alteration and curtain making business from home and takes orders on whatsapp. she needs to keep measurements per customer window, fabric chosen, price, and when it's due. she's 64 so it has to be dead simple

**Spec:**
```
Type:       Web application (order book)
Auth:       Single owner login with a remembered device
Data model: CurtainCustomer(id, name, phone, address)
            WindowMeasure(id, customer_id -> CurtainCustomer, room, width_cm, drop_cm)
            CurtainOrder(id, customer_id -> CurtainCustomer, window_id -> WindowMeasure, fabric, lining, price, due_date, status)
Features:   - Save measurements per customer window
            - Create orders with fabric, lining and price
            - Calculate fabric metres needed
            - Show this week's due orders on the home screen
            - Use large buttons and few screens
API:        REST
            POST /customers/{id}/windows
            POST /orders
            GET  /orders/due
Storage:    SQLite
Tech stack: Python, Flask, Pico.css
```

---

## Example 416

**Intent:**
basically i manage a coworking cafe hybrid thing where people can either just buy coffee or pay for a day pass for the quiet room. i want the day pass to be bought online and give them a wifi code that only works that day, and I'd like to see how many day passes we sell per week

**Spec:**
```
Type:       Web application (day pass sales)
Auth:       Manager login; buyers check out as guests
Data model: DayPass(id, email, date, price, wifi_code, paid_at)
            WifiCode(id, code, valid_on, used)
Features:   - Sell day passes online for a chosen date
            - Generate a WiFi voucher valid only that day
            - Cap passes at the quiet room's seat count
            - Show weekly pass sales
API:        REST
            POST /passes
            GET  /passes/{id}
            GET  /reports/weekly
Storage:    SQLite
Tech stack: Node.js, Express, Stripe Checkout, UniFi Hotspot API
```

---

## Example 417

**Intent:**
staff rota for my pharmacy

**Spec:**
```
Type:       Web application (shift scheduling)
Auth:       Manager and staff login
Data model: PharmacyStaff(id, name, role, contracted_hours)
            RotaShift(id, staff_id -> PharmacyStaff, date, start_time, end_time)
Features:   - Build a weekly rota
            - Warn when no pharmacist is scheduled during opening hours
            - Email staff their weekly shifts
            - Show hours per staff member
API:        REST
            GET  /rota?week={date}
            POST /shifts
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 418

**Intent:**
quote and invoice for roofers

**Spec:**
```
Type:       Web application (quotes and invoices)
Auth:       Owner login
Data model: RoofCustomer(id, name, address, phone, email)
            RoofQuote(id, customer_id -> RoofCustomer, roof_type, area_m2, materials, labour_days, total, status)
            RoofInvoice(id, quote_id -> RoofQuote, number, amount, paid)
Features:   - Build quotes from roof area and materials
            - Attach roof photos to a quote
            - Convert accepted quotes into invoices
            - Track paid invoices
API:        REST
            POST /quotes
            POST /quotes/{id}/accept
            POST /quotes/{id}/invoice
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Dompdf
```

---

## Example 419

**Intent:**
pub table bookings for sunday roast

**Spec:**
```
Type:       Web application (table reservations)
Auth:       Staff login; guests book as guests
Data model: PubTable(id, number, seats)
            RoastBooking(id, table_id -> PubTable, name, phone, party_size, sitting_time, roast_preorder)
Features:   - Book a sitting time for Sunday lunch
            - Preorder roast choices for large tables
            - Allocate tables by party size
            - Show the kitchen a count of each roast per sitting
API:        REST
            GET  /sittings?date={date}
            POST /bookings
            GET  /kitchen/counts?date={date}
Storage:    SQLite
Tech stack: Python, Flask, Alpine.js
```

---

## Example 420

**Intent:**
appointment booking for a tax advisor

**Spec:**
```
Type:       Web application (appointment booking)
Auth:       Advisor login; clients book with email confirmation
Data model: AdvisorClient(id, name, email, phone)
            Consultation(id, client_id -> AdvisorClient, type, starts_at, video, notes)
Features:   - Book in-person or video consultations
            - Collect the consultation topic in advance
            - Sync bookings to the advisor's Outlook calendar
            - Send reminders the day before
API:        REST
            GET  /slots?date={date}
            POST /consultations
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Microsoft Graph API
```

---

## Example 421

**Intent:**
mechanic workshop job cards in react with a node api

**Spec:**
```
Type:       Web application (job cards)
Auth:       Mechanic and service advisor login (JWT)
Data model: WorkshopVehicle(id, reg, make, model, owner_phone)
            JobCard(id, vehicle_id -> WorkshopVehicle, complaint, mechanic, status, opened_at)
            JobTask(id, job_card_id -> JobCard, description, labour_hours, done)
            JobPart(id, job_card_id -> JobCard, part_name, quantity, price)
Features:   - Open a job card for a vehicle complaint
            - Add tasks and parts as work progresses
            - Show a workshop board by status
            - Produce the final bill from labour and parts
API:        REST
            POST /job-cards
            POST /job-cards/{id}/tasks
            POST /job-cards/{id}/parts
            GET  /job-cards/{id}/bill
Storage:    PostgreSQL
Tech stack: React, Node.js, Express, Prisma
```

---

## Example 422

**Intent:**
need to track tips n cash for my 2 food stalls daily, simple, on google sheets is fine

**Spec:**
```
Type:       Web application (daily takings form)
Data model: Takings(date, stall, cash, card, tips, staff_on_shift, notes)
Features:   - Fill in a short daily takings form on a phone
            - Append each entry to a Google Sheet
            - Total cash, card and tips per stall per week
            - Email a weekly summary every Monday
Storage:    Google Sheets
Tech stack: Google Forms, Google Sheets, Google Apps Script
```

---

## Example 423

**Intent:**
kayak and paddleboard storage racks at the lake club, members rent a rack spot per year, waiting list

**Spec:**
```
Type:       Web application (rack rental)
Auth:       Member login (email + password); committee admin
Data model: RackSpot(id, rack, level, type, yearly_fee)
            RackMember(id, name, email, craft_type)
            RackLease(id, spot_id -> RackSpot, member_id -> RackMember, year, paid)
            RackWaitlist(id, member_id -> RackMember, craft_type, joined_at)
Features:   - Renew rack spots each year
            - Offer released spots to the waiting list in order
            - Collect yearly fees online
            - Show a rack map with occupants
API:        REST
            POST /leases/{id}/renew
            POST /waitlist
            GET  /racks
Storage:    SQLite
Tech stack: Python, Django, Stripe
```

---

## Example 424

**Intent:**
ticket sales for our school christmas concert, 2 nights, families max 4 tickets

**Spec:**
```
Type:       Web application (event ticketing)
Auth:       Parent login with school email; office admin
Data model: ConcertNight(id, date, seats)
            FamilyTicketOrder(id, night_id -> ConcertNight, parent_email, quantity, paid)
Features:   - Choose a concert night and number of tickets
            - Limit each family to 4 tickets across both nights
            - Pay online
            - Print a door list per night
API:        REST
            GET  /nights
            POST /orders
            GET  /nights/{id}/door-list
Storage:    PostgreSQL
Tech stack: Python, Flask, Stripe
```

---

## Example 425

**Intent:**
booking + waiver + payment for paintball field groups

**Spec:**
```
Type:       Web application (group activity booking)
Auth:       Staff login; group organisers book without accounts
Data model: PaintballSession(id, starts_at, field, max_players)
            GroupBooking(id, session_id -> PaintballSession, organiser_email, players, package, deposit_paid)
            PlayerWaiver(id, booking_id -> GroupBooking, name, birth_date, signature_url)
Features:   - Book a session for a group with a paintball package
            - Pay a deposit per player
            - Send each player a waiver link to sign
            - Show staff which players still need waivers
API:        REST
            POST /bookings
            POST /bookings/{id}/waivers
            GET  /bookings/{id}/waivers/missing
Storage:    PostgreSQL, S3 (signatures)
Tech stack: Node.js, Express, React, Stripe
```

---

