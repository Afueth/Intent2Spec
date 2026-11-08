## Example 1

**Intent:**
campus app to find free study rooms

**Spec:**
```
Type:       Mobile application with backend (campus study rooms)
Auth:       University single sign-on (SAML)
Data model: Building(id, name, lat, lng)
            StudyRoom(id, building_id -> Building, name, capacity, has_whiteboard)
            Booking(id, room_id -> StudyRoom, student_id, starts_at, ends_at)
Features:   - Show rooms that are free right now, grouped by building
            - Filter rooms by capacity and equipment
            - Book a room in 30-minute slots up to 3 hours
            - Release a booking automatically if not checked in within 15 minutes
            - Check in by scanning the QR code on the room door
API:        REST
            GET  /rooms/available?at={time}
            POST /bookings
            POST /bookings/{id}/checkin
            DELETE /bookings/{id}
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express
```

---

## Example 2

**Intent:**
My mother is in hospital for a few weeks and the visiting rules are confusing. I'd like an app where families can book a visiting slot for a patient so the ward isn't overcrowded, and the nurses can see who is coming.

**Spec:**
```
Type:       Mobile application with backend (hospital visitor booking)
Auth:       Visitor phone number + SMS code; staff email + password
Data model: Ward(id, name, max_visitors_per_slot)
            Patient(id, ward_id -> Ward, bed_number, visitor_code)
            VisitSlot(id, ward_id -> Ward, starts_at, ends_at)
            Visit(id, slot_id -> VisitSlot, patient_id -> Patient, visitor_name, phone)
Features:   - Link a visitor to a patient using a code given by the ward
            - Show open visiting slots for the patient's ward
            - Book a slot while the per-slot visitor limit is respected
            - Show nurses today's visit list per bed
            - Notify visitors by SMS if a slot is cancelled
API:        REST
            POST /patients/link
            GET  /wards/{id}/slots
            POST /visits
            GET  /wards/{id}/visits?date={date}
Storage:    PostgreSQL
Tech stack: Flutter, Python, Django REST Framework, Twilio
```

---

## Example 3

**Intent:**
app for our mosque so people see prayer times and announcements

**Spec:**
```
Type:       Mobile application with backend (mosque community)
Auth:       Admin email + password; members use the app without login
Data model: PrayerTime(id, date, fajr, dhuhr, asr, maghrib, isha, jumuah)
            Announcement(id, title, body, published_at)
            Event(id, title, starts_at, location)
Features:   - Show today's prayer and iqamah times
            - Send a push reminder before each prayer if enabled
            - Post announcements and events from an admin panel
            - Upload a month of prayer times from a CSV file
            - Show the qibla direction using the phone compass
API:        REST
            GET  /prayer-times?month={yyyy-mm}
            GET  /announcements
            POST /announcements
            POST /prayer-times/import
Storage:    PostgreSQL
Tech stack: Flutter, Firebase Cloud Messaging, Node.js, Express
```

---

## Example 4

**Intent:**
resident app for apartment building - report broken stuff, get parcel notices

**Spec:**
```
Type:       Mobile application with backend (apartment residents)
Auth:       Email + password, account approved by building manager
Data model: Resident(id, name, email, unit_number)
            MaintenanceRequest(id, resident_id -> Resident, category, description, photo_url, status)
            Parcel(id, unit_number, carrier, received_at, picked_up_at)
Features:   - Submit a maintenance request with a photo
            - Track request status from open to fixed
            - Notify a resident when a parcel arrives at the front desk
            - Let the front desk mark parcels as picked up
            - Show building notices on a home screen
API:        REST
            POST /maintenance-requests
            GET  /maintenance-requests/mine
            POST /parcels
            PATCH /parcels/{id}/pickup
Storage:    PostgreSQL, S3 (photos)
Tech stack: React Native, Python, FastAPI
```

---

## Example 5

**Intent:**
hoa app where homeowners pay dues and vote on stuff

**Spec:**
```
Type:       Mobile application with backend (HOA management)
Auth:       Email + password, one account per property
Data model: Property(id, address, owner_name, email)
            DuesInvoice(id, property_id -> Property, amount, due_date, paid_at)
            Proposal(id, title, description, closes_at)
            Vote(id, proposal_id -> Proposal, property_id -> Property, choice)
Features:   - Show dues invoices and pay them by card
            - Send reminders for overdue dues
            - Create proposals with a voting deadline
            - Allow one vote per property and show results after closing
            - Store meeting minutes as PDFs
API:        REST
            GET  /invoices
            POST /invoices/{id}/pay
            POST /proposals
            POST /proposals/{id}/votes
Storage:    PostgreSQL, S3 (PDFs)
Tech stack: Flutter, Node.js, NestJS, Stripe
```

---

## Example 6

**Intent:**
neighbourhood watch app to report suspicious things to neighbours fast

**Spec:**
```
Type:       Mobile application with backend (neighbourhood watch)
Auth:       Phone number + SMS code, address verified by a coordinator
Data model: Member(id, name, phone, street_id -> Street, verified)
            Street(id, name, area_id)
            Alert(id, member_id -> Member, category, description, lat, lng, created_at)
Features:   - Post an alert with category, location and optional photo
            - Push the alert to verified members within 1 km
            - Show recent alerts on a map
            - Let coordinators remove false or abusive alerts
            - Show a button to call the police emergency number
API:        REST
            POST /alerts
            GET  /alerts?lat={lat}&lng={lng}
            DELETE /alerts/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin (Android), Swift (iOS), Go backend, Firebase Cloud Messaging
```

---

## Example 7

**Intent:**
I have a driveway I don't use during the day, and I live near the train station. I want an app where people like me can rent out their parking spot by the hour to commuters.

**Spec:**
```
Type:       Mobile application with backend (parking spot sharing)
Auth:       Email + password or Google sign-in
Data model: User(id, name, email, stripe_account_id)
            ParkingSpot(id, owner_id -> User, address, lat, lng, hourly_price, instructions)
            Availability(id, spot_id -> ParkingSpot, weekday, from_time, to_time)
            Reservation(id, spot_id -> ParkingSpot, driver_id -> User, starts_at, ends_at, total)
Features:   - List a spot with price, photos and weekly availability
            - Search spots on a map near a destination
            - Reserve and pay for a time window
            - Pay out owners after each reservation minus a fee
            - Rate drivers and spot owners
API:        REST
            POST /spots
            GET  /spots/search?lat={lat}&lng={lng}&from={t}&to={t}
            POST /reservations
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Node.js, Express, Stripe Connect, Mapbox
```

---

## Example 8

**Intent:**
ev charger finder that shows if the charger is free right now

**Spec:**
```
Type:       Mobile application with backend (EV charger finder)
Auth:       Optional email + password for saving favourites
Data model: Station(id, name, lat, lng, operator, network)
            Connector(id, station_id -> Station, type, power_kw, status, updated_at)
            Favourite(id, user_id, station_id -> Station)
Features:   - Show stations on a map coloured by live availability
            - Filter by connector type (CCS, CHAdeMO, Type 2) and power
            - Sync connector status from operator feeds every minute
            - Save favourite stations
            - Open navigation to a station in the maps app
API:        REST
            GET  /stations?bbox={bbox}&connector={type}
            GET  /stations/{id}
            POST /favourites
Storage:    PostgreSQL with PostGIS, Redis (live status)
Tech stack: Flutter, Python, FastAPI, OCPI feeds
```

---

## Example 9

**Intent:**
e-scooter rental app, unlock with qr, pay per minute

**Spec:**
```
Type:       Mobile application with backend (scooter rental)
Auth:       Phone number + SMS code, card required before first ride
Data model: Scooter(id, qr_code, lat, lng, battery_pct, status)
            Ride(id, scooter_id -> Scooter, user_id, started_at, ended_at, distance_m, cost)
            User(id, phone, payment_method_id)
Features:   - Show nearby scooters with battery level on a map
            - Unlock a scooter by scanning its QR code
            - Charge an unlock fee plus a price per minute
            - Require a parking photo when ending the ride
            - Block ending rides inside no-parking zones
API:        REST
            GET  /scooters/nearby
            POST /rides/start
            POST /rides/{id}/end
Storage:    PostgreSQL with PostGIS
Tech stack: Swift (iOS), Kotlin (Android), Go, MQTT (scooter locks), Stripe
```

---

## Example 10

**Intent:**
laundry pickup app. customer schedules pickup, we wash and bring back

**Spec:**
```
Type:       Mobile application with backend (laundry pickup)
Auth:       Email + password
Data model: Customer(id, name, phone, address)
            Order(id, customer_id -> Customer, pickup_window, delivery_window, status, weight_kg, price)
            ServiceType(id, name, price_per_kg)
Features:   - Schedule a pickup window and choose wash, dry clean or iron
            - Weigh the bag at the shop and price the order per kg
            - Charge the saved card once the order is weighed
            - Track status from picked up to delivered
            - Show drivers their pickup and drop-off route for the day
API:        REST
            POST /orders
            PATCH /orders/{id}/weigh
            GET  /orders/{id}
            GET  /driver/route?date={date}
Storage:    PostgreSQL
Tech stack: Flutter, Python, Django, Stripe
```

---

## Example 11

**Intent:**
Book a cleaner for my house through an app.

**Spec:**
```
Type:       Mobile application with backend (home cleaning booking)
Auth:       Email + password for customers and cleaners
Data model: Cleaner(id, name, rating, service_area, hourly_rate)
            Booking(id, customer_id, cleaner_id -> Cleaner, date, hours, rooms, status)
            Review(id, booking_id -> Booking, stars, comment)
Features:   - Estimate hours from number of bedrooms and bathrooms
            - Show available cleaners for the chosen date
            - Book and prepay a cleaning
            - Let cleaners accept or decline jobs
            - Leave a rating and review after the job
API:        REST
            GET  /cleaners/available?date={date}
            POST /bookings
            PATCH /bookings/{id}/accept
            POST /bookings/{id}/review
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails, Stripe
```

---

## Example 12

**Intent:**
i want app where student can call tutor right now for math homework help, like on demand, pay by minute

**Spec:**
```
Type:       Mobile application with backend (on-demand tutoring)
Auth:       Email + password; tutors verified by admin
Data model: Tutor(id, name, subjects, per_minute_rate, online)
            Student(id, name, email, credit_balance)
            Session(id, tutor_id -> Tutor, student_id -> Student, started_at, ended_at, cost)
Features:   - Show online tutors for a chosen subject
            - Start a video call with a shared whiteboard
            - Bill the student per minute from prepaid credit
            - Top up credit by card
            - Rate the tutor after the session
API:        REST
            GET  /tutors/online?subject={s}
            POST /sessions
            POST /sessions/{id}/end
            POST /credits/topup
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Agora (video), Stripe
```

---

## Example 13

**Intent:**
telehealth app for our small clinic, patients book video consult with doctor

**Spec:**
```
Type:       Mobile application with backend (telehealth)
Auth:       Email + password with two-factor authentication
Data model: Doctor(id, name, specialty)
            Patient(id, name, date_of_birth, email)
            Appointment(id, doctor_id -> Doctor, patient_id -> Patient, starts_at, status)
            ConsultNote(id, appointment_id -> Appointment, notes, created_at)
Features:   - Book a video appointment from a doctor's open slots
            - Join an encrypted video call from the app
            - Upload photos or documents before the consult
            - Let doctors write private consult notes
            - Send appointment reminders by push and email
API:        REST
            GET  /doctors/{id}/slots
            POST /appointments
            POST /appointments/{id}/join
            POST /appointments/{id}/notes
Storage:    PostgreSQL (encrypted at rest), S3 (uploads)
Tech stack: React Native, Python, Django, Twilio Video
```

---

## Example 14

**Intent:**
pharmacy refill app - scan the label, pharmacy gets the request

**Spec:**
```
Type:       Mobile application with backend (pharmacy refills)
Auth:       Phone number + date of birth, SMS code
Data model: Patient(id, name, phone, date_of_birth)
            Prescription(id, patient_id -> Patient, rx_number, drug_name, refills_left)
            RefillRequest(id, prescription_id -> Prescription, status, ready_at)
Features:   - Scan the barcode on a bottle label to read the Rx number
            - Request a refill and pick a pickup time
            - Show refills left on each prescription
            - Notify the patient when the refill is ready
            - Let pharmacy staff update request status in a dashboard
API:        REST
            POST /refill-requests
            GET  /prescriptions
            PATCH /refill-requests/{id}
Storage:    PostgreSQL
Tech stack: Flutter, ML Kit barcode scanning, Java, Spring Boot
```

---

## Example 15

**Intent:**
Blood donation app: tells donors when they can donate again and lets them book at a blood centre.

**Spec:**
```
Type:       Mobile application with backend (blood donation)
Auth:       Email + password
Data model: Donor(id, name, blood_type, last_donation_at)
            Centre(id, name, address, lat, lng)
            DonationSlot(id, centre_id -> Centre, starts_at, capacity)
            Appointment(id, donor_id -> Donor, slot_id -> DonationSlot, status)
Features:   - Calculate the next eligible donation date
            - Book a slot at a nearby centre
            - Send urgent push alerts for low-stock blood types
            - Record completed donations and show a history
API:        REST
            GET  /centres/nearby
            GET  /centres/{id}/slots
            POST /appointments
            POST /alerts/shortage
Storage:    PostgreSQL
Tech stack: Kotlin Multiplatform, Ktor, Firebase Cloud Messaging
```

---

## Example 16

**Intent:**
so food bank helpers can grab shifts on their phone

**Spec:**
```
Type:       Mobile application with backend (volunteer shifts)
Auth:       Email + magic link
Data model: Volunteer(id, name, email, phone)
            Shift(id, role, starts_at, ends_at, slots)
            Signup(id, shift_id -> Shift, volunteer_id -> Volunteer, checked_in_at)
Features:   - Show upcoming shifts with open slots
            - Sign up or cancel a shift
            - Send a reminder the day before a shift
            - Check volunteers in on a tablet at the door
            - Export volunteer hours as CSV for reports
API:        REST
            GET  /shifts
            POST /shifts/{id}/signups
            DELETE /signups/{id}
            GET  /reports/hours.csv
Storage:    PostgreSQL
Tech stack: React Native (Expo), Supabase
```

---

## Example 17

**Intent:**
After the floods last year our town had no way to coordinate who needed help and who could give it. I want an app where people request help (food, water, transport, shelter) and volunteers claim the requests, and it should still work a bit when the internet is bad.

**Spec:**
```
Type:       Mobile application with backend (disaster relief coordination)
Auth:       Phone number + SMS code
Data model: HelpRequest(id, requester_id, category, people_count, lat, lng, status, created_at)
            Volunteer(id, name, phone, skills, has_vehicle)
            Assignment(id, request_id -> HelpRequest, volunteer_id -> Volunteer, claimed_at, done_at)
Features:   - Create help requests offline and sync when a connection returns
            - Show open requests on a map by category and urgency
            - Let volunteers claim a request and mark it done
            - Send SMS fallback updates to requesters without data
            - Give coordinators a dashboard of unassigned requests
API:        REST
            POST /requests
            GET  /requests?status=open
            POST /requests/{id}/claim
            POST /requests/{id}/complete
Storage:    PostgreSQL with PostGIS, SQLite on device (offline queue)
Tech stack: Flutter, Python, FastAPI, Twilio SMS
```

---

## Example 18

**Intent:**
lost pet alert app

**Spec:**
```
Type:       Mobile application with backend (lost pet alerts)
Auth:       Email + password
Data model: Pet(id, owner_id, name, species, breed, photo_url)
            LostReport(id, pet_id -> Pet, last_seen_lat, last_seen_lng, last_seen_at, status)
            Sighting(id, report_id -> LostReport, reporter_id, lat, lng, photo_url, note)
Features:   - Report a pet as lost with last-seen location
            - Push an alert to users within 5 km
            - Submit a sighting with photo and location
            - Show sightings on a map for the owner
            - Mark the pet as found and close the alert
API:        REST
            POST /lost-reports
            POST /lost-reports/{id}/sightings
            PATCH /lost-reports/{id}
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: React Native, Node.js, Firebase Cloud Messaging
```

---

## Example 19

**Intent:**
safe ticket resale for concerts, price can't go above face value

**Spec:**
```
Type:       Mobile application with backend (ticket resale)
Auth:       Email + password with identity check for sellers
Data model: Event(id, name, venue, starts_at)
            Ticket(id, event_id -> Event, seller_id, face_value, barcode_hash, status)
            Listing(id, ticket_id -> Ticket, price, created_at)
            Sale(id, listing_id -> Listing, buyer_id, paid_at)
Features:   - List a ticket for resale with a price cap at face value
            - Hold payment in escrow until the event
            - Reissue the barcode to the buyer and void the old one
            - Search listings by event
            - Refund the buyer if the ticket fails at the gate
API:        REST
            POST /listings
            GET  /events/{id}/listings
            POST /listings/{id}/buy
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, Java, Spring Boot, Stripe Connect
```

---

## Example 20

**Intent:**
gym class booking app (spin, yoga, hiit) with waitlist

**Spec:**
```
Type:       Mobile application with backend (gym class booking)
Auth:       Member email + password
Data model: ClassType(id, name, duration_min)
            ClassSession(id, class_type_id -> ClassType, instructor, starts_at, capacity)
            Booking(id, session_id -> ClassSession, member_id, status, position)
Features:   - Show the weekly class timetable
            - Book a class until it is full
            - Join a waitlist and auto-promote when someone cancels
            - Block cancellations less than 2 hours before class
            - Check in with a QR code at the front desk
API:        REST
            GET  /sessions?week={date}
            POST /sessions/{id}/book
            DELETE /bookings/{id}
            POST /checkin
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, NestJS
```

---
## Example 21

**Intent:**
barbershop queue app, customers join line from home and see how many ahead

**Spec:**
```
Type:       Mobile application with backend (salon queue)
Auth:       Phone number + SMS code
Data model: Shop(id, name, address, avg_service_min)
            Barber(id, shop_id -> Shop, name, on_shift)
            QueueEntry(id, shop_id -> Shop, customer_id, barber_id -> Barber, position, status, joined_at)
Features:   - Join a shop's queue remotely, optionally for a specific barber
            - Show position and estimated wait time live
            - Notify the customer when they are 2 places away
            - Let staff call the next customer and mark no-shows
            - Remove a customer who misses their turn by 5 minutes
API:        REST + WebSocket
            POST /shops/{id}/queue
            GET  /shops/{id}/queue
            POST /queue/{id}/call
            WS   /shops/{id}/queue/live
Storage:    PostgreSQL, Redis (live queue)
Tech stack: Flutter, Node.js, Socket.IO
```

---

## Example 22

**Intent:**
Our restaurant doesn't take reservations and people crowd the door. Can we have a digital waitlist where they leave their number and get a text when the table is ready?

**Spec:**
```
Type:       Mobile application with backend (restaurant waitlist)
Auth:       Staff PIN login on the host tablet
Data model: Party(id, name, phone, size, quoted_wait_min, status, added_at)
            Table(id, number, seats, status)
Features:   - Add a party with name, size and phone at the host stand
            - Quote a wait time from current table turnover
            - Send an SMS when the table is ready
            - Let guests check their place in line from a link
            - Mark parties seated or left
API:        REST
            POST /parties
            GET  /parties?status=waiting
            POST /parties/{id}/notify
            PATCH /parties/{id}
Storage:    PostgreSQL
Tech stack: React Native (tablet), Python, Flask, Twilio
```

---

## Example 23

**Intent:**
order food from your seat in the stadium and pick up or get it delivered to seat

**Spec:**
```
Type:       Mobile application with backend (stadium food ordering)
Auth:       Guest checkout with Apple Pay / Google Pay; optional account
Data model: Stand(id, name, section, open)
            MenuItem(id, stand_id -> Stand, name, price, in_stock)
            Order(id, stand_id -> Stand, seat_section, seat_row, seat_number, mode, status, total)
Features:   - Enter seat by scanning the ticket barcode
            - Browse menus of stands near the seat
            - Choose pickup or in-seat delivery
            - Notify when the order is ready
            - Give stand staff a live order screen
API:        REST + WebSocket
            GET  /stands?section={s}
            POST /orders
            PATCH /orders/{id}/status
            WS   /stands/{id}/orders
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe Terminal, Socket.IO
```

---

## Example 24

**Intent:**
museum audio guide app, visitor types number next to painting and hears story

**Spec:**
```
Type:       Mobile application with backend (museum audio guide)
Auth:       Curator email + password for the content admin
Data model: Exhibit(id, stop_number, title, room, image_url)
            AudioTrack(id, exhibit_id -> Exhibit, language, audio_url, transcript)
            Tour(id, name, exhibit_ids)
Features:   - Play the track for a stop number typed by the visitor
            - Download a full tour for offline use in the building
            - Switch between languages
            - Show the transcript for hearing-impaired visitors
            - Let curators upload audio and edit exhibits
API:        REST
            GET  /exhibits/{stop_number}?lang={code}
            GET  /tours/{id}/bundle
            POST /exhibits
Storage:    PostgreSQL, S3 + CloudFront (audio files)
Tech stack: Flutter, Python, FastAPI
```

---

## Example 25

**Intent:**
QR code walking trail for tourists in our old town, scan plaques to unlock history

**Spec:**
```
Type:       Mobile application with backend (tourism QR trail)
Auth:       Anonymous device ID; admin login for content editors
Data model: Trail(id, name, distance_km, language)
            Stop(id, trail_id -> Trail, order, title, story, lat, lng, qr_token)
            Progress(id, device_id, stop_id -> Stop, scanned_at)
Features:   - Show the trail route and stops on a map
            - Unlock a stop's story by scanning its plaque QR code
            - Track which stops a visitor has completed
            - Give a digital badge when the full trail is done
            - Show scan statistics to the tourism office
API:        REST
            GET  /trails/{id}
            POST /scan
            GET  /stats/stops
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express, Leaflet
```

---

## Example 26

**Intent:**
Scavenger hunt app for team building - teams solve clues and upload photo proof, organiser approves

**Spec:**
```
Type:       Mobile application with backend (scavenger hunt)
Auth:       Join code per team; organiser email + password
Data model: Hunt(id, name, starts_at, ends_at, organiser_id)
            Team(id, hunt_id -> Hunt, name, join_code, score)
            Clue(id, hunt_id -> Hunt, text, points, lat, lng, radius_m)
            Submission(id, team_id -> Team, clue_id -> Clue, photo_url, status)
Features:   - Show clues to teams once the hunt starts
            - Unlock location clues only within their radius
            - Upload photo proof for a clue
            - Let the organiser approve or reject submissions
            - Show a live leaderboard
API:        REST
            POST /teams/join
            GET  /hunts/{id}/clues
            POST /submissions
            PATCH /submissions/{id}
            GET  /hunts/{id}/leaderboard
Storage:    PostgreSQL, S3 (photos)
Tech stack: Flutter, Firebase (Auth, Firestore, Storage)
```

---

## Example 27

**Intent:**
our sales reps visit shops all day, need app to log visits, take orders and see customer history even offline

**Spec:**
```
Type:       Mobile application with backend (field sales)
Auth:       Company SSO (Azure AD)
Data model: Rep(id, name, territory)
            Customer(id, name, address, lat, lng, credit_limit)
            Visit(id, rep_id -> Rep, customer_id -> Customer, checked_in_at, notes)
            SalesOrder(id, visit_id -> Visit, lines_json, total, synced)
Features:   - Show today's planned visits on a route map
            - Check in at a customer with GPS verification
            - Take orders from the product catalogue offline
            - Sync orders to the ERP when online
            - Show past orders and open invoices per customer
API:        REST
            GET  /reps/me/plan?date={date}
            POST /visits
            POST /orders/sync
            GET  /customers/{id}/history
Storage:    PostgreSQL, SQLite on device
Tech stack: .NET MAUI, ASP.NET Core
```

---

## Example 28

**Intent:**
car insurance claim app, take photos of damage and submit

**Spec:**
```
Type:       Mobile application with backend (insurance claims)
Auth:       Policy number + email, then password
Data model: Policy(id, policy_number, holder_name, vehicle_reg)
            Claim(id, policy_id -> Policy, incident_date, location, description, status)
            ClaimPhoto(id, claim_id -> Claim, url, angle, taken_at)
Features:   - Guide the user to photograph damage from required angles
            - Attach GPS location and time to each photo
            - Submit a claim with a description of the incident
            - Track claim status and adjuster messages
            - Upload the other driver's details and police report
API:        REST
            POST /claims
            POST /claims/{id}/photos
            GET  /claims/{id}
            POST /claims/{id}/messages
Storage:    PostgreSQL, S3 (photos)
Tech stack: Swift (iOS), Kotlin (Android), Java, Spring Boot
```

---

## Example 29

**Intent:**
real estate agents need an app to schedule house showings with buyers and get feedback after

**Spec:**
```
Type:       Mobile application with backend (real-estate showings)
Auth:       Email + password for agents; buyers via invite link
Data model: Listing(id, agent_id, address, price, lockbox_code)
            Showing(id, listing_id -> Listing, buyer_agent_id, starts_at, status)
            Feedback(id, showing_id -> Showing, interest_level, price_opinion, comments)
Features:   - Request a showing slot for a listing
            - Let the listing agent approve or decline requests
            - Reveal the lockbox code only during the showing window
            - Collect buyer feedback after the showing
            - Send sellers a weekly feedback summary
API:        REST
            POST /listings/{id}/showings
            PATCH /showings/{id}
            POST /showings/{id}/feedback
            GET  /listings/{id}/feedback
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails
```

---

## Example 30

**Intent:**
church app: sermons, giving, small groups

**Spec:**
```
Type:       Mobile application with backend (church community)
Auth:       Email + password
Data model: Sermon(id, title, speaker, date, audio_url, video_url)
            SmallGroup(id, name, leader_id, meeting_day, location)
            GroupMember(id, group_id -> SmallGroup, user_id)
            Donation(id, user_id, fund, amount, recurring, created_at)
Features:   - Stream and download past sermons
            - Give once or set up recurring giving to a fund
            - Browse and join small groups
            - Send yearly giving statements by email
API:        REST
            GET  /sermons
            POST /donations
            GET  /groups
            POST /groups/{id}/join
Storage:    PostgreSQL, S3 (media)
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 31

**Intent:**
hindu temple wants app for booking pujas and seeing festival calendar

**Spec:**
```
Type:       Mobile application with backend (temple services)
Auth:       Email or phone + OTP
Data model: PujaService(id, name, duration_min, fee)
            PujaBooking(id, service_id -> PujaService, devotee_id, date, time, gotra, nakshatra, status)
            Festival(id, name, date, description)
Features:   - Book a puja and enter family details like gotra and nakshatra
            - Pay the puja fee online
            - Show the festival calendar with push reminders
            - Let priests see their daily booking list
API:        REST
            GET  /pujas
            POST /puja-bookings
            GET  /festivals?year={y}
            GET  /priest/bookings?date={date}
Storage:    PostgreSQL
Tech stack: React Native, Python, Django, Razorpay
```

---

## Example 32

**Intent:**
where is the campus shuttle bus right now

**Spec:**
```
Type:       Mobile application with backend (campus shuttle tracker)
Data model: Route(id, name, color)
            Stop(id, route_id -> Route, name, lat, lng, order)
            BusPosition(bus_id, route_id -> Route, lat, lng, recorded_at)
Features:   - Receive GPS positions from a driver phone every 5 seconds
            - Show buses moving live on a map by route
            - Estimate arrival time at each stop
            - Alert a student when the bus is 3 minutes from their stop
API:        REST + WebSocket
            POST /positions
            GET  /routes
            WS   /routes/{id}/live
Storage:    Redis (positions), PostgreSQL (routes and stops)
Tech stack: Flutter, Go, Google Maps SDK
```

---

## Example 33

**Intent:**
uni lost and found app — post what you found, search for what you lost

**Spec:**
```
Type:       Mobile application with backend (campus lost and found)
Auth:       University email login (domain restricted)
Data model: Item(id, poster_id, kind, title, description, category, location, photo_url, status)
            Claim(id, item_id -> Item, claimant_id, message, status)
Features:   - Post a found or lost item with photo and location
            - Search and filter items by category and date
            - Suggest matches between lost and found posts
            - Send a claim message to the finder
            - Mark an item as returned
API:        REST
            POST /items
            GET  /items?q={text}&kind={lost|found}
            POST /items/{id}/claims
Storage:    PostgreSQL, S3
Tech stack: React Native, Supabase
```

---

## Example 34

**Intent:**
I run the dining halls at a college. Students always ask what's on the menu and if it has allergens. I want an app with the daily menu per hall, allergen info, and how busy each hall is.

**Spec:**
```
Type:       Mobile application with backend (campus dining)
Auth:       Staff login for menu editors; students without login
Data model: DiningHall(id, name, opening_hours)
            MenuItem(id, hall_id -> DiningHall, date, meal, name, allergens, is_vegan)
            Occupancy(hall_id -> DiningHall, count, updated_at)
Features:   - Show today's menu per hall by meal
            - Filter dishes by allergen and dietary tag
            - Show live busyness from door counters
            - Let staff upload the weekly menu from a spreadsheet
API:        REST
            GET  /halls
            GET  /halls/{id}/menu?date={date}
            POST /menus/import
            POST /occupancy
Storage:    PostgreSQL
Tech stack: Swift (iOS), Kotlin (Android), Python, FastAPI
```

---

## Example 35

**Intent:**
hospital wayfinding app so visitors dont get lost going to xray etc

**Spec:**
```
Type:       Mobile application with backend (hospital wayfinding)
Auth:       Admin login for facilities staff
Data model: Floor(id, building, level, map_image_url)
            Place(id, floor_id -> Floor, name, department, x, y)
            PathNode(id, floor_id -> Floor, x, y, neighbours)
Features:   - Search for a department or room
            - Show step-by-step route across floors and lifts
            - Use Bluetooth beacons to show the visitor's position
            - Offer an accessible route without stairs
API:        REST
            GET  /places?q={text}
            GET  /route?from={id}&to={id}&accessible={bool}
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, iBeacon, Node.js
```

---

## Example 36

**Intent:**
bike share with docking stations, see how many bikes and free docks

**Spec:**
```
Type:       Mobile application with backend (station-based bike share)
Auth:       Email + password, card on file
Data model: Station(id, name, lat, lng, total_docks)
            Bike(id, station_id -> Station, dock_number, is_electric)
            Trip(id, bike_id -> Bike, user_id, start_station_id -> Station, end_station_id -> Station, started_at, ended_at)
Features:   - Show stations with available bikes and empty docks
            - Release a bike with a code typed at the dock
            - Charge after the first 30 free minutes
            - Buy day passes and annual memberships
API:        REST
            GET  /stations
            POST /trips/unlock
            POST /trips/{id}/end
            POST /passes
Storage:    PostgreSQL
Tech stack: React Native, Elixir, Phoenix, Stripe
```

---

## Example 37

**Intent:**
book hot desks at our coworking space from phone

**Spec:**
```
Type:       Mobile application with backend (coworking desk booking)
Auth:       Email + password, membership plan required
Data model: Member(id, name, plan, credits)
            Desk(id, zone, number, has_monitor)
            DeskBooking(id, desk_id -> Desk, member_id -> Member, date)
            MeetingRoomBooking(id, room, member_id -> Member, starts_at, ends_at)
Features:   - Pick a desk from a floor plan for a date
            - Book meeting rooms using monthly credits
            - Unlock the front door with a phone QR code
            - Show who else from the community is in today
API:        REST
            GET  /desks?date={date}
            POST /desk-bookings
            POST /room-bookings
            GET  /door/qr
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, NestJS
```

---

## Example 38

**Intent:**
car wash subscriptions — app shows plate QR, unlimited washes monthly

**Spec:**
```
Type:       Mobile application with backend (car wash membership)
Auth:       Email + password
Data model: Member(id, name, email, plan, stripe_subscription_id)
            Vehicle(id, member_id -> Member, plate)
            Wash(id, vehicle_id -> Vehicle, location_id, washed_at)
Features:   - Subscribe to a monthly unlimited wash plan
            - Register up to 2 vehicles per plan
            - Show a QR code scanned at the wash entrance
            - Log each wash and show history
            - Pause or cancel the subscription in the app
API:        REST
            POST /subscriptions
            POST /vehicles
            POST /washes/verify
            GET  /washes
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe Billing
```

---

## Example 39

**Intent:**
students need app to report broken stuff in dorm and see when fixed

**Spec:**
```
Type:       Mobile application with backend (dorm maintenance)
Auth:       University SSO
Data model: Room(id, hall, number)
            WorkOrder(id, room_id -> Room, student_id, category, description, photo_url, status, created_at)
            Technician(id, name, trade)
Features:   - Submit a work order with photo and permission to enter
            - Assign work orders to technicians by trade
            - Notify the student when the job is scheduled and done
            - Show housing staff open orders by hall
API:        REST
            POST /work-orders
            GET  /work-orders/mine
            PATCH /work-orders/{id}/assign
Storage:    PostgreSQL
Tech stack: Flutter, Python, Django
```

---

## Example 40

**Intent:**
app for hospice nurses doing home visits to record vitals at patient house and sync later

**Spec:**
```
Type:       Mobile application with backend (home nursing visits)
Auth:       Staff login with PIN and biometric unlock
Data model: Patient(id, name, address, care_plan)
            Visit(id, patient_id -> Patient, nurse_id, scheduled_at, arrived_at, left_at)
            Vitals(id, visit_id -> Visit, bp, pulse, temp, pain_score, notes)
Features:   - Show the day's visit list with addresses
            - Record vitals and notes offline during a visit
            - Sync encrypted records when connected
            - Log arrival and departure time with GPS
            - Flag readings outside the care plan ranges
API:        REST
            GET  /visits?date={date}
            POST /visits/{id}/vitals
            POST /sync
Storage:    PostgreSQL, encrypted SQLite on device
Tech stack: Kotlin (Android tablets), Java, Spring Boot
```

---

## Example 41

**Intent:**
I want app my aunt can use: she book massage at our spa and choose therapist

**Spec:**
```
Type:       Mobile application with backend (spa booking)
Auth:       Phone number + SMS code
Data model: Therapist(id, name, specialties, photo_url)
            Treatment(id, name, duration_min, price)
            Appointment(id, treatment_id -> Treatment, therapist_id -> Therapist, client_id, starts_at, status)
Features:   - Choose a treatment and a preferred therapist
            - Show free time slots for that therapist
            - Book and pay a deposit
            - Send a reminder 24 hours before
            - Let the front desk manage the daily schedule
API:        REST
            GET  /treatments
            GET  /therapists/{id}/slots?date={date}
            POST /appointments
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Express, Stripe
```

---

## Example 42

**Intent:**
campus events app where clubs post events and students RSVP

**Spec:**
```
Type:       Mobile application with backend (campus club events)
Auth:       University email + password
Data model: Club(id, name, description, admin_ids)
            Event(id, club_id -> Club, title, starts_at, location, capacity)
            Rsvp(id, event_id -> Event, student_id, created_at)
Features:   - Let club admins post events
            - RSVP and add the event to the phone calendar
            - Follow clubs to get their new events in a feed
            - Check attendees in by QR at the door
API:        REST
            POST /clubs/{id}/events
            GET  /feed
            POST /events/{id}/rsvp
            POST /events/{id}/checkin
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI
```

---

## Example 43

**Intent:**
want an app that tracks shared washing machines in our building and tells me when mine is done

**Spec:**
```
Type:       Mobile application with backend (shared laundry room)
Auth:       Building invite code + email
Data model: Machine(id, building_id, kind, label, status, cycle_ends_at)
            Session(id, machine_id -> Machine, user_id, started_at, ends_at)
            Reservation(id, machine_id -> Machine, user_id, slot_start)
Features:   - Show which washers and dryers are free
            - Start a timer when loading a machine
            - Notify the user when the cycle is done
            - Remind others if laundry is left over 15 minutes
            - Reserve a machine for a time slot
API:        REST
            GET  /machines
            POST /machines/{id}/start
            POST /reservations
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase Cloud Functions
```

---

## Example 44

**Intent:**
synagogue app for minyan signups so we know we have 10

**Spec:**
```
Type:       Mobile application with backend (synagogue minyan)
Auth:       Email + password
Data model: Service(id, kind, starts_at)
            Commitment(id, service_id -> Service, member_id, status)
            Member(id, name, phone)
Features:   - List upcoming services with the count of committed attendees
            - Commit to attend or cancel
            - Alert members when a service is short of 10
            - Notify the gabbai when the minyan is confirmed
API:        REST
            GET  /services
            POST /services/{id}/commit
            DELETE /commitments/{id}
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 45

**Intent:**
hospital needs app so patients' families get surgery status updates on phone while waiting

**Spec:**
```
Type:       Mobile application with backend (surgery status updates)
Auth:       Family access code given at check-in
Data model: SurgeryCase(id, tracking_code, status, updated_at)
            FamilyContact(id, case_id -> SurgeryCase, name, phone, push_token)
            StatusChange(id, case_id -> SurgeryCase, status, note, created_at)
Features:   - Show anonymous status: in pre-op, in surgery, in recovery, ready
            - Push a notification on each status change
            - Let OR staff update status from a staff screen
            - Let the surgeon send a short message to the family
            - Delete case data 48 hours after discharge
API:        REST
            GET  /cases/{tracking_code}
            POST /cases/{id}/status
            POST /cases/{id}/contacts
Storage:    PostgreSQL
Tech stack: Flutter, C#, ASP.NET Core
```

---

## Example 46

**Intent:**
tool rental shop wants customers reserve tools in app before coming

**Spec:**
```
Type:       Mobile application with backend (tool rental)
Auth:       Email + password, ID checked at first pickup
Data model: Tool(id, name, category, daily_rate, deposit)
            ToolUnit(id, tool_id -> Tool, serial, condition)
            Rental(id, unit_id -> ToolUnit, customer_id, start_date, end_date, status)
Features:   - Browse tools by category with daily price
            - Check availability for a date range
            - Reserve and pre-authorise the deposit
            - Remind customers of the return date
            - Record damage notes on return
API:        REST
            GET  /tools?category={c}
            GET  /tools/{id}/availability
            POST /rentals
            PATCH /rentals/{id}/return
Storage:    PostgreSQL
Tech stack: React Native, Django, Stripe
```

---
## Example 47

**Intent:**
meditation centre retreat booking app

**Spec:**
```
Type:       Mobile application with backend (meditation retreats)
Auth:       Email + password
Data model: Retreat(id, title, teacher, starts_on, ends_on, capacity, suggested_donation)
            Registration(id, retreat_id -> Retreat, participant_id, room_type, status)
            Participant(id, name, email, dietary_needs, experience_level)
Features:   - Browse upcoming retreats with teacher and dates
            - Register and choose dormitory or private room
            - Put registrations on a waitlist when full
            - Collect dietary needs and health notes
            - Let staff export the room allocation list
API:        REST
            GET  /retreats
            POST /retreats/{id}/registrations
            GET  /retreats/{id}/rooming.csv
Storage:    PostgreSQL
Tech stack: Flutter, Python, Django
```

---

## Example 48

**Intent:**
gurdwara langar seva signup, who cooks who cleans each sunday

**Spec:**
```
Type:       Mobile application with backend (gurdwara seva rota)
Auth:       Phone number + OTP
Data model: SevaTask(id, name, date, slots_needed)
            SevaSignup(id, task_id -> SevaTask, sevadar_id, status)
            Sevadar(id, name, phone, family_name)
Features:   - Show Sunday seva tasks like cooking, serving and cleaning
            - Sign up a family member for a task
            - Remind sevadars on Saturday evening
            - Let the committee see unfilled tasks and message members
API:        REST
            GET  /seva-tasks?date={date}
            POST /seva-tasks/{id}/signups
            GET  /seva-tasks/unfilled
Storage:    Firebase Firestore
Tech stack: React Native, Firebase Cloud Functions, Firebase Cloud Messaging
```

---

## Example 49

**Intent:**
My son's Quran teacher gives him pages to memorise each week and I never know how he is doing. I want an app where the teacher logs what each kid recited and how well, and parents see progress and get a note.

**Spec:**
```
Type:       Mobile application with backend (Quran memorisation tracking)
Auth:       Teacher email + password; parents linked by invite code
Data model: Student(id, name, class_id, parent_id)
            Assignment(id, student_id -> Student, surah, from_ayah, to_ayah, due_date)
            Recitation(id, assignment_id -> Assignment, grade, mistakes, comment, recited_at)
Features:   - Let teachers assign verses to memorise per student
            - Record each recitation with a grade and mistake count
            - Show parents a progress chart of surahs completed
            - Notify parents after each recitation
API:        REST
            POST /students/{id}/assignments
            POST /assignments/{id}/recitations
            GET  /students/{id}/progress
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Express
```

---

## Example 50

**Intent:**
find catholic mass times near me in any city

**Spec:**
```
Type:       Mobile application with backend (mass times finder)
Auth:       Parish admin email + password for editing times
Data model: Parish(id, name, address, lat, lng, website)
            MassTime(id, parish_id -> Parish, weekday, time, language, kind)
Features:   - Show parishes near the user's location on a map
            - List next mass times today, filterable by language
            - Show confession and adoration times
            - Let parish admins update their schedule
API:        REST
            GET  /parishes/nearby?lat={lat}&lng={lng}
            GET  /parishes/{id}/times
            PUT  /parishes/{id}/times
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Go
```

---

## Example 51

**Intent:**
campus print queue app send document from phone print at any library printer

**Spec:**
```
Type:       Mobile application with backend (campus printing)
Auth:       University SSO
Data model: PrintJob(id, student_id, file_url, pages, color, copies, cost, status)
            Printer(id, location, supports_color, status)
            Account(student_id, balance)
Features:   - Upload a PDF or photo and set copies and colour
            - Show the cost and deduct from print balance
            - Release the job by scanning the QR code on any printer
            - Delete unreleased jobs after 24 hours
API:        REST
            POST /jobs
            POST /printers/{id}/release
            GET  /account/balance
Storage:    PostgreSQL, S3 (temporary files)
Tech stack: Flutter, Python, FastAPI, CUPS
```

---

## Example 52

**Intent:**
lab equipment booking for our research dept, like microscopes and centrifuge

**Spec:**
```
Type:       Mobile application with backend (lab equipment booking)
Auth:       University SSO, training certification per instrument
Data model: Instrument(id, name, room, requires_training)
            Certification(id, user_id, instrument_id -> Instrument, granted_at)
            Reservation(id, instrument_id -> Instrument, user_id, starts_at, ends_at, grant_code)
Features:   - Show instrument calendars by week
            - Allow booking only for users certified on that instrument
            - Bill usage hours to a research grant code
            - Report instrument faults to the lab manager
API:        REST
            GET  /instruments/{id}/calendar
            POST /reservations
            POST /instruments/{id}/faults
            GET  /reports/usage?grant={code}
Storage:    PostgreSQL
Tech stack: React Native, Java, Spring Boot
```

---

## Example 53

**Intent:**
college counselling centre appointments, private, students can book anonymous-ish

**Spec:**
```
Type:       Mobile application with backend (student counselling)
Auth:       University SSO with minimal data shared to counsellors
Data model: Counsellor(id, name, focus_areas)
            Slot(id, counsellor_id -> Counsellor, starts_at, mode)
            Appointment(id, slot_id -> Slot, student_ref, reason_category, status)
Features:   - Book an in-person or video appointment
            - Pick a counsellor by focus area or first available
            - Show crisis hotline numbers on every screen
            - Send discreet reminders without appointment details
            - Allow cancelling up to 2 hours before
API:        REST
            GET  /slots?mode={in_person|video}
            POST /appointments
            DELETE /appointments/{id}
Storage:    PostgreSQL (encrypted)
Tech stack: Swift, Kotlin, Python, Django
```

---

## Example 54

**Intent:**
walk me home safety escort for campus at night

**Spec:**
```
Type:       Mobile application with backend (campus safety escort)
Auth:       University SSO
Data model: EscortRequest(id, student_id, pickup_lat, pickup_lng, destination, status, created_at)
            Escort(id, name, on_duty, lat, lng)
            LocationShare(id, student_id, contact_phone, expires_at)
Features:   - Request a security escort from the current location
            - Show the assigned escort approaching on a map
            - Share a live walking route with a friend
            - Trigger an SOS that calls campus police with location
API:        REST + WebSocket
            POST /escort-requests
            WS   /escort-requests/{id}/track
            POST /sos
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Node.js, Socket.IO
```

---

## Example 55

**Intent:**
TA office hours queue so students dont wait in hallway

**Spec:**
```
Type:       Mobile application with backend (office hours queue)
Auth:       University email login
Data model: Course(id, code, name)
            OfficeHour(id, course_id -> Course, ta_id, starts_at, ends_at, location)
            Ticket(id, office_hour_id -> OfficeHour, student_id, question, status, created_at)
Features:   - Join the queue with a short question description
            - Show position in line live
            - Let TAs call the next student or group similar questions
            - Record help time per student for the instructor
API:        REST + WebSocket
            POST /office-hours/{id}/tickets
            POST /tickets/{id}/call
            WS   /office-hours/{id}/queue
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI
```

---

## Example 56

**Intent:**
attendance by scanning qr code shown by lecturer at start of lecture

**Spec:**
```
Type:       Mobile application with backend (lecture attendance)
Auth:       University SSO
Data model: Lecture(id, course_id, starts_at, room)
            QrToken(id, lecture_id -> Lecture, token, expires_at)
            Attendance(id, lecture_id -> Lecture, student_id, scanned_at)
Features:   - Show a rotating QR code on the lecturer's screen every 10 seconds
            - Mark attendance when a student scans a valid code
            - Reject scans from outside the room's Wi-Fi network
            - Export attendance per course as CSV
API:        REST
            POST /lectures/{id}/qr
            POST /attendance/scan
            GET  /courses/{id}/attendance.csv
Storage:    PostgreSQL
Tech stack: Flutter, Go
```

---

## Example 57

**Intent:**
dorm guests registration app, resident registers visitor, desk sees list

**Spec:**
```
Type:       Mobile application with backend (dorm guest registration)
Auth:       University SSO for residents; staff accounts for front desk
Data model: Resident(id, name, room)
            Guest(id, resident_id -> Resident, name, id_last4, arrives_at, leaves_at, status)
Features:   - Register an overnight guest in advance
            - Enforce a limit of 3 guest nights per week
            - Show the front desk a list of expected guests today
            - Sign guests in and out at the desk
API:        REST
            POST /guests
            GET  /guests/expected?date={date}
            PATCH /guests/{id}/sign-in
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 58

**Intent:**
connect alumni mentors with current students for career advice

**Spec:**
```
Type:       Mobile application with backend (alumni mentoring)
Auth:       LinkedIn sign-in for alumni; university SSO for students
Data model: Mentor(id, name, industry, company, grad_year, availability)
            Mentee(id, name, major, interests)
            Match(id, mentor_id -> Mentor, mentee_id -> Mentee, status)
            Meeting(id, match_id -> Match, scheduled_at, notes)
Features:   - Suggest mentors by industry and interests
            - Send and accept mentoring requests
            - Schedule 30-minute calls
            - Message inside the app
API:        REST
            GET  /mentors?industry={i}
            POST /matches
            POST /matches/{id}/meetings
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails
```

---

## Example 59

**Intent:**
ER wait time app for our 3 hospitals so people go to the least busy one

**Spec:**
```
Type:       Mobile application with backend (ER wait times)
Data model: Hospital(id, name, address, lat, lng)
            WaitSnapshot(id, hospital_id -> Hospital, wait_minutes, patients_waiting, recorded_at)
Features:   - Show current estimated wait for each emergency department
            - Sort hospitals by wait plus travel time
            - Pull wait data from the hospital system every 5 minutes
            - Show a warning to call emergency services for serious symptoms
API:        REST
            GET  /hospitals/waits
            POST /waits (internal)
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, C#, ASP.NET Core
```

---

## Example 60

**Intent:**
check-in for clinic appointments on the phone instead of the front desk, with forms filled before

**Spec:**
```
Type:       Mobile application with backend (clinic self check-in)
Auth:       Date of birth + SMS code
Data model: Appointment(id, patient_id, clinician, starts_at, status)
            IntakeForm(id, appointment_id -> Appointment, answers_json, signed_at)
            InsuranceCard(id, patient_id, front_url, back_url)
Features:   - Fill intake and consent forms before arrival
            - Photograph the insurance card
            - Check in when within 200 m of the clinic
            - Notify the patient when the room is ready
API:        REST
            GET  /appointments/upcoming
            POST /appointments/{id}/intake
            POST /appointments/{id}/checkin
Storage:    PostgreSQL, S3 (card images)
Tech stack: Flutter, Node.js, NestJS
```

---

## Example 61

**Intent:**
physio gives me exercises on paper which I lose. app where physio assigns exercise videos and I tick them off and she sees

**Spec:**
```
Type:       Mobile application with backend (physiotherapy home exercises)
Auth:       Email + password; patients invited by therapist
Data model: Exercise(id, name, video_url, instructions)
            Program(id, patient_id, therapist_id, start_date)
            ProgramExercise(id, program_id -> Program, exercise_id -> Exercise, sets, reps, days)
            Completion(id, program_exercise_id -> ProgramExercise, date, pain_level)
Features:   - Let therapists build a program from an exercise video library
            - Show today's exercises to the patient with videos
            - Tick off exercises and log pain level
            - Show therapists adherence per patient
API:        REST
            POST /programs
            GET  /programs/mine/today
            POST /completions
            GET  /patients/{id}/adherence
Storage:    PostgreSQL, S3 (videos)
Tech stack: React Native, Python, FastAPI
```

---

## Example 62

**Intent:**
blood pressure readings from home sent to my doctor automatically

**Spec:**
```
Type:       Mobile application with backend (remote BP monitoring)
Auth:       Email + password; clinician accounts separate
Data model: Patient(id, name, clinician_id)
            Reading(id, patient_id -> Patient, systolic, diastolic, pulse, measured_at, source)
            AlertRule(id, patient_id -> Patient, max_systolic, max_diastolic)
Features:   - Read measurements from a Bluetooth blood pressure cuff
            - Allow manual entry of readings
            - Upload readings to the clinician dashboard
            - Alert the clinician when readings pass thresholds
            - Show weekly averages to the patient
API:        REST
            POST /readings
            GET  /patients/{id}/readings
            PUT  /patients/{id}/alert-rule
Storage:    PostgreSQL
Tech stack: Flutter, flutter_blue_plus, Python, Django
```

---

## Example 63

**Intent:**
grandpa forget his pills. app reminds him and tells me if he dont take

**Spec:**
```
Type:       Mobile application with backend (medication adherence)
Auth:       Email + password for caregiver; senior device paired by code
Data model: Medication(id, patient_id, name, dose, times)
            DoseEvent(id, medication_id -> Medication, scheduled_at, taken_at, status)
            Caregiver(id, name, phone, patient_id)
Features:   - Show a big-button reminder at each dose time
            - Mark a dose as taken with one tap
            - Notify the caregiver when a dose is missed by 30 minutes
            - Show the caregiver a weekly adherence report
API:        REST
            POST /medications
            POST /dose-events/{id}/taken
            GET  /patients/{id}/adherence
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Firebase Cloud Messaging, Twilio SMS
```

---

## Example 64

**Intent:**
vaccine clinic booking with dose 2 automatically scheduled

**Spec:**
```
Type:       Mobile application with backend (vaccination booking)
Auth:       National ID number + SMS code
Data model: Clinic(id, name, address, vaccines)
            Slot(id, clinic_id -> Clinic, starts_at, capacity)
            Booking(id, slot_id -> Slot, person_id, vaccine, dose_number, status)
Features:   - Book a first dose at a clinic slot
            - Reserve the second dose automatically at the correct interval
            - Show a digital vaccination record with QR code
            - Send reminders 1 day before
API:        REST
            GET  /clinics/{id}/slots
            POST /bookings
            GET  /records/me
Storage:    PostgreSQL
Tech stack: Kotlin, Swift, Java, Spring Boot
```

---

## Example 65

**Intent:**
lab sends nurse to home to take blood sample, patient books in app

**Spec:**
```
Type:       Mobile application with backend (home sample collection)
Auth:       Phone number + OTP
Data model: TestPackage(id, name, price, fasting_required)
            CollectionBooking(id, patient_id, package_id -> TestPackage, address, slot, phlebotomist_id, status)
            Report(id, booking_id -> CollectionBooking, pdf_url, released_at)
Features:   - Choose test packages and a home visit time slot
            - Show fasting instructions before the visit
            - Track the phlebotomist on the way
            - Download the lab report PDF when released
API:        REST
            GET  /packages
            POST /bookings
            GET  /bookings/{id}/track
            GET  /bookings/{id}/report
Storage:    PostgreSQL, S3 (reports)
Tech stack: Flutter, Node.js, Express, Razorpay
```

---

## Example 66

**Intent:**
hospital patients order their meals from bedside tablet, respecting diet restrictions

**Spec:**
```
Type:       Mobile application with backend (patient meal ordering)
Auth:       Bed tablet linked to patient admission by staff
Data model: Patient(id, bed, diet_order, allergies)
            MenuItem(id, name, meal, diet_tags, allergens)
            MealOrder(id, patient_id -> Patient, meal, items, status)
Features:   - Show only menu items allowed by the patient's diet order
            - Hide items containing the patient's allergens
            - Order breakfast, lunch and dinner before cut-off times
            - Print tray tickets for the kitchen
API:        REST
            GET  /patients/{id}/menu
            POST /meal-orders
            GET  /kitchen/tickets?meal={m}
Storage:    PostgreSQL
Tech stack: Kotlin (Android tablets), Python, Django
```

---

## Example 67

**Intent:**
nurses swap shifts with each other, manager approves

**Spec:**
```
Type:       Mobile application with backend (nurse shift swaps)
Auth:       Hospital SSO
Data model: Nurse(id, name, unit, qualifications)
            Shift(id, unit, starts_at, ends_at, nurse_id -> Nurse)
            SwapRequest(id, shift_id -> Shift, offered_by_id -> Nurse, taken_by_id -> Nurse, status)
Features:   - Post a shift for swap
            - Show eligible nurses with matching qualifications
            - Block swaps that break rest-hour rules
            - Send swaps to the unit manager for approval
API:        REST
            POST /swap-requests
            POST /swap-requests/{id}/take
            PATCH /swap-requests/{id}/approve
Storage:    PostgreSQL
Tech stack: React Native, C#, ASP.NET Core
```

---

## Example 68

**Intent:**
porters in hospital get jobs on phone to move patients or samples

**Spec:**
```
Type:       Mobile application with backend (hospital porter tasks)
Auth:       Staff badge number + PIN
Data model: Porter(id, name, on_shift, current_location)
            Task(id, kind, from_location, to_location, priority, requested_by, status, created_at)
Features:   - Let wards request a patient move or sample delivery
            - Assign the task to the nearest free porter
            - Accept, start and complete tasks on the phone
            - Escalate tasks not picked up within 10 minutes
API:        REST + WebSocket
            POST /tasks
            PATCH /tasks/{id}
            WS   /porters/me/tasks
Storage:    PostgreSQL
Tech stack: Flutter, Elixir, Phoenix Channels
```

---

## Example 69

**Intent:**
Book the pool, gym and BBQ area in our condo.

**Spec:**
```
Type:       Mobile application with backend (condo amenity booking)
Auth:       Email + password, unit verified by management
Data model: Amenity(id, name, max_people, slot_minutes, rules)
            AmenityBooking(id, amenity_id -> Amenity, unit_id, starts_at, guests)
            Unit(id, number, owner_name)
Features:   - Show amenity calendars and free slots
            - Limit each unit to 2 bookings per week per amenity
            - Collect a refundable deposit for the party room
            - Let management block dates for maintenance
API:        REST
            GET  /amenities/{id}/slots
            POST /amenity-bookings
            POST /amenities/{id}/blackouts
Storage:    PostgreSQL
Tech stack: React Native, Laravel, Stripe
```

---

## Example 70

**Intent:**
gated community visitor passes - i invite guest, guard scans QR

**Spec:**
```
Type:       Mobile application with backend (gated community visitor passes)
Auth:       Resident phone + OTP; guard accounts on gate tablets
Data model: Resident(id, name, house_number, phone)
            Pass(id, resident_id -> Resident, guest_name, vehicle_plate, valid_from, valid_to, qr_token)
            GateLog(id, pass_id -> Pass, gate, scanned_at, direction)
Features:   - Create a one-time or recurring visitor pass
            - Send the QR pass to the guest by WhatsApp or SMS
            - Let guards scan and validate passes at the gate
            - Notify the resident when the guest enters
API:        REST
            POST /passes
            POST /passes/scan
            GET  /gate-logs?date={date}
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, NestJS
```

---

## Example 71

**Intent:**
reserve the freight elevator for move in day

**Spec:**
```
Type:       Mobile application with backend (elevator reservation)
Auth:       Email + password, resident or incoming tenant invite
Data model: ElevatorSlot(id, date, start_time, end_time, status)
            MoveReservation(id, slot_id -> ElevatorSlot, unit, mover_company, insurance_doc_url)
Features:   - Show free 3-hour slots for the freight elevator
            - Upload the moving company's insurance certificate
            - Require manager approval before confirming
            - Send the doorman the day's move schedule
API:        REST
            GET  /elevator/slots
            POST /move-reservations
            PATCH /move-reservations/{id}/approve
Storage:    PostgreSQL, S3
Tech stack: React Native (Expo), Supabase
```

---

## Example 72

**Intent:**
5 of us share a student house, need app for chores rotation and who paid the electric

**Spec:**
```
Type:       Mobile application with backend (shared house chores and bills)
Auth:       Email + password, house joined by invite code
Data model: House(id, name, invite_code)
            Housemate(id, house_id -> House, name)
            Chore(id, house_id -> House, name, rotation_order, current_index)
            Bill(id, house_id -> House, paid_by_id -> Housemate, amount, description)
Features:   - Rotate chores weekly and notify who is next
            - Tick chores off when done
            - Record bills and split them equally
            - Show who owes whom
API:        REST
            POST /houses/join
            GET  /houses/{id}/chores
            POST /houses/{id}/bills
            GET  /houses/{id}/balances
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase
```

---

## Example 73

**Intent:**
Airbnb hosts send guests a digital guidebook with wifi password, checkin instructions, local tips

**Spec:**
```
Type:       Mobile application with backend (vacation rental guidebook)
Auth:       Host email + password; guests open a link with a stay code
Data model: Property(id, host_id, name, address, wifi_ssid, wifi_password)
            GuideSection(id, property_id -> Property, title, body, order)
            Stay(id, property_id -> Property, guest_name, check_in, check_out, code)
Features:   - Build a guidebook from sections with photos
            - Reveal door code and Wi-Fi only during the stay dates
            - Show recommended places on a map
            - Send guests the link 2 days before check-in
API:        REST
            POST /properties/{id}/sections
            GET  /stays/{code}/guide
            POST /stays
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express
```

---

## Example 74

**Intent:**
bin day reminders for our council area, also which bin

**Spec:**
```
Type:       Mobile application with backend (waste collection reminders)
Data model: Address(id, street, number, postcode, zone_id -> Zone)
            Zone(id, name)
            Collection(id, zone_id -> Zone, date, bin_type)
Features:   - Look up the collection zone by address
            - Notify the evening before which bin to put out
            - Show changes for public holidays
            - Answer "which bin does this go in" from a searchable item list
API:        REST
            GET  /addresses?q={text}
            GET  /zones/{id}/collections
            GET  /items?q={text}
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 75

**Intent:**
community garden plots, members water rota and harvest sharing

**Spec:**
```
Type:       Mobile application with backend (community garden)
Auth:       Email + password
Data model: Plot(id, number, size_m2, member_id)
            Member(id, name, email)
            WateringShift(id, date, member_id -> Member)
            HarvestPost(id, member_id -> Member, produce, quantity, pickup_until)
Features:   - Assign plots and keep a waitlist for new members
            - Run a watering rota with reminders
            - Post surplus harvest for others to collect
            - Log shared tool checkouts
API:        REST
            GET  /plots
            GET  /watering?month={m}
            POST /harvest-posts
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 76

**Intent:**
borrow tools from neighbors library of things app

**Spec:**
```
Type:       Mobile application with backend (library of things)
Auth:       Email + password, address verified once
Data model: Item(id, owner_id, name, category, photo_url, deposit, available)
            Loan(id, item_id -> Item, borrower_id, from_date, to_date, status)
            Member(id, name, neighbourhood)
Features:   - List items you are willing to lend
            - Request to borrow for a date range
            - Approve requests and agree a handover time
            - Remind borrowers on the return date
            - Rate borrowers after each loan
API:        REST
            POST /items
            GET  /items?neighbourhood={n}
            POST /items/{id}/loans
            PATCH /loans/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework
```

---

## Example 77

**Intent:**
tenants submit monthly water meter readings with photo to landlord

**Spec:**
```
Type:       Mobile application with backend (meter readings)
Auth:       Email + password
Data model: Meter(id, unit_id, kind, serial)
            Reading(id, meter_id -> Meter, value, photo_url, read_at)
            Unit(id, address, tenant_id)
Features:   - Remind tenants to submit readings on the 1st of the month
            - Take a photo and read the number with OCR
            - Flag readings lower than last month
            - Calculate usage and charges per unit
API:        REST
            POST /meters/{id}/readings
            GET  /units/{id}/usage
Storage:    PostgreSQL, S3
Tech stack: React Native, Google ML Kit text recognition, Node.js
```

---
## Example 78

**Intent:**
pay for parking garage with app, no ticket, plate camera

**Spec:**
```
Type:       Mobile application with backend (garage parking payment)
Auth:       Email + password, card on file
Data model: Garage(id, name, hourly_rate, daily_max)
            Vehicle(id, user_id, plate)
            ParkingSession(id, garage_id -> Garage, vehicle_id -> Vehicle, entered_at, exited_at, amount)
Features:   - Register vehicle plates on the account
            - Open a session when the entry camera reads a known plate
            - Charge the card automatically on exit
            - Show receipts for expense reports
API:        REST
            POST /vehicles
            POST /lpr/events
            GET  /sessions
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, Go, Stripe
```

---

## Example 79

**Intent:**
parking officer app to check if car paid and write ticket

**Spec:**
```
Type:       Mobile application with backend (parking enforcement)
Auth:       Officer ID + PIN on issued devices
Data model: Permit(id, plate, zone, valid_to)
            PaidSession(id, plate, zone, ends_at)
            Citation(id, plate, officer_id, zone, violation, photo_urls, lat, lng, issued_at)
Features:   - Scan a plate with the camera and check paid sessions and permits
            - Issue a citation with photos and GPS
            - Print the citation on a Bluetooth printer
            - Sync citations to the city system
API:        REST
            GET  /plates/{plate}/status?zone={z}
            POST /citations
Storage:    PostgreSQL
Tech stack: Kotlin (Android), OpenALPR, Java, Spring Boot
```

---

## Example 80

**Intent:**
valet parking - customer gets digital ticket and requests car from phone so it's ready

**Spec:**
```
Type:       Mobile application with backend (valet parking)
Auth:       Phone number on the digital ticket; attendant login
Data model: ValetTicket(id, venue_id, phone, plate, key_tag, spot, status, created_at)
            Venue(id, name, fee)
Features:   - Create a ticket by texting a link to the customer
            - Record spot and key tag with car photos
            - Let the customer request their car from the link
            - Queue requests for attendants with estimated time
            - Collect the valet fee and tip in the app
API:        REST
            POST /tickets
            POST /tickets/{id}/request
            GET  /venues/{id}/queue
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Twilio, Stripe
```

---

## Example 81

**Intent:**
rent kayaks at the lake by the hour, sign waiver in app

**Spec:**
```
Type:       Mobile application with backend (kayak rental)
Auth:       Email + password
Data model: Boat(id, kind, seats, status)
            Rental(id, boat_id -> Boat, customer_id, starts_at, hours, status)
            Waiver(id, customer_id, signature_url, signed_at)
Features:   - Book a kayak or paddleboard for a time slot
            - Sign the liability waiver with a finger signature
            - Show weather and wind warnings for the day
            - Check out and return boats at the dock with a tablet
API:        REST
            GET  /boats/availability?date={date}
            POST /rentals
            POST /waivers
Storage:    PostgreSQL, S3 (signatures)
Tech stack: Flutter, Python, FastAPI, OpenWeatherMap API
```

---

## Example 82

**Intent:**
marina boat slip booking for visiting boats

**Spec:**
```
Type:       Mobile application with backend (marina slip booking)
Auth:       Email + password
Data model: Slip(id, dock, number, max_length_m, has_power)
            Vessel(id, owner_id, name, length_m, beam_m)
            SlipBooking(id, slip_id -> Slip, vessel_id -> Vessel, arrive_on, depart_on, status)
Features:   - Search slips that fit the boat's length for given nights
            - Book and pay nightly fees
            - Show fuel dock hours and marina map
            - Let the harbour master assign or move boats
API:        REST
            GET  /slips/available?length={m}&from={d}&to={d}
            POST /slip-bookings
            PATCH /slip-bookings/{id}
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails, Stripe
```

---

## Example 83

**Intent:**
people share their home EV charger with others for money, like airbnb for chargers

**Spec:**
```
Type:       Mobile application with backend (peer-to-peer EV charging)
Auth:       Email + password
Data model: HomeCharger(id, host_id, lat, lng, connector, power_kw, price_per_kwh)
            ChargeBooking(id, charger_id -> HomeCharger, driver_id, starts_at, ends_at, kwh, amount)
Features:   - List a home charger with price and available hours
            - Book a charging window on a map
            - Enter final kWh from the charger display
            - Pay the host through the app
            - Rate hosts and drivers
API:        REST
            POST /chargers
            GET  /chargers/nearby
            POST /bookings
            POST /bookings/{id}/complete
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Node.js, Stripe Connect
```

---

## Example 84

**Intent:**
we have 40 company EVs and 12 chargers in the depot, need app so drivers book charging time

**Spec:**
```
Type:       Mobile application with backend (fleet charging scheduler)
Auth:       Company SSO
Data model: Charger(id, bay, power_kw, status)
            Vehicle(id, plate, battery_kwh)
            ChargeSlot(id, charger_id -> Charger, vehicle_id -> Vehicle, starts_at, ends_at)
Features:   - Book a charger slot for a vehicle
            - Suggest slot length from current battery level
            - Notify drivers to move cars when charging finishes
            - Show managers charger utilisation per day
API:        REST
            GET  /chargers/schedule?date={d}
            POST /charge-slots
            GET  /reports/utilisation
Storage:    PostgreSQL
Tech stack: React Native, C#, ASP.NET Core, OCPP
```

---

## Example 85

**Intent:**
ferry tickets on phone for island trips

**Spec:**
```
Type:       Mobile application with backend (ferry ticketing)
Auth:       Email + password or guest checkout
Data model: Sailing(id, route, departs_at, passenger_capacity, car_capacity)
            Ticket(id, sailing_id -> Sailing, passenger_count, vehicle_plate, qr_token, status)
Features:   - Search sailings by route and date
            - Buy passenger and vehicle tickets
            - Show a QR ticket that works offline
            - Notify on delays or cancellations due to weather
API:        REST
            GET  /sailings?route={r}&date={d}
            POST /tickets
            POST /tickets/validate
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, Java, Spring Boot
```

---

## Example 86

**Intent:**
broke down on highway, app to call tow truck and see where it is

**Spec:**
```
Type:       Mobile application with backend (roadside assistance)
Auth:       Membership number + phone OTP
Data model: Member(id, name, plan, vehicle)
            AssistRequest(id, member_id -> Member, issue, lat, lng, status, created_at)
            Truck(id, operator, lat, lng, available)
Features:   - Request a tow, jump start or tyre change with GPS location
            - Dispatch the nearest available truck
            - Track the truck's arrival on a map
            - Share the request with a family contact
API:        REST + WebSocket
            POST /requests
            WS   /requests/{id}/track
            PATCH /trucks/{id}/location
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Go, Google Maps SDK
```

---

## Example 87

**Intent:**
office carpool app match coworkers who live close

**Spec:**
```
Type:       Mobile application with backend (corporate carpooling)
Auth:       Company email domain sign-in
Data model: Commuter(id, name, home_lat, home_lng, office_id, schedule)
            CarpoolGroup(id, driver_id -> Commuter, seats)
            CarpoolMember(id, group_id -> CarpoolGroup, commuter_id -> Commuter)
Features:   - Match coworkers by home distance and work hours
            - Create carpool groups with a driver
            - Log shared trips for commuter benefit reports
            - Reserve carpool parking spots at the office
API:        REST
            GET  /matches
            POST /groups
            POST /trips
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Python, Django
```

---

## Example 88

**Intent:**
shoe repair shop, customer sends photo for a quote then books pickup

**Spec:**
```
Type:       Mobile application with backend (shoe repair)
Auth:       Phone number + OTP
Data model: RepairRequest(id, customer_id, photo_urls, description, quote, status)
            Pickup(id, request_id -> RepairRequest, address, slot)
Features:   - Send photos of shoes and describe the problem
            - Receive a price quote from the cobbler
            - Accept the quote and book a pickup slot
            - Track repair status and delivery
API:        REST
            POST /requests
            PATCH /requests/{id}/quote
            POST /requests/{id}/accept
Storage:    PostgreSQL, S3
Tech stack: Flutter, Laravel
```

---

## Example 89

**Intent:**
tailor alterations booking - measurements saved, fitting appointments

**Spec:**
```
Type:       Mobile application with backend (tailor alterations)
Auth:       Email + password
Data model: Customer(id, name, phone)
            Measurement(id, customer_id -> Customer, chest, waist, inseam, sleeve, updated_at)
            AlterationOrder(id, customer_id -> Customer, garment, work, price, ready_on, status)
            Fitting(id, order_id -> AlterationOrder, starts_at)
Features:   - Save customer measurements
            - Create alteration orders with price and ready date
            - Book fitting appointments
            - Notify when the garment is ready
API:        REST
            POST /orders
            POST /orders/{id}/fittings
            GET  /customers/{id}/measurements
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 90

**Intent:**
pool cleaning company - techs log chemicals per visit and customers get a report

**Spec:**
```
Type:       Mobile application with backend (pool service)
Auth:       Technician login; customer email + password
Data model: Pool(id, customer_id, address, volume_litres)
            ServiceVisit(id, pool_id -> Pool, tech_id, visited_at, ph, chlorine_ppm, alkalinity, notes)
            ChemicalAdded(id, visit_id -> ServiceVisit, chemical, amount)
Features:   - Show techs their weekly route
            - Record water test values and chemicals added
            - Suggest chemical doses from the test values and pool volume
            - Email customers a visit report with photos
API:        REST
            GET  /routes/me?week={w}
            POST /visits
            GET  /pools/{id}/history
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 91

**Intent:**
lawn mowing subscription, weekly or every 2 weeks, skip when raining

**Spec:**
```
Type:       Mobile application with backend (lawn care subscription)
Auth:       Email + password
Data model: Property(id, customer_id, address, lawn_size_m2)
            Subscription(id, property_id -> Property, frequency, price, active)
            Visit(id, subscription_id -> Subscription, scheduled_on, status, photo_url)
Features:   - Quote a price from lawn size measured on a satellite map
            - Subscribe weekly or fortnightly
            - Skip or reschedule a visit
            - Auto-reschedule visits when rain is forecast
            - Send an after photo when done
API:        REST
            POST /quotes
            POST /subscriptions
            PATCH /visits/{id}
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe Billing, Google Maps API
```

---

## Example 92

**Intent:**
pest control technicians record bait station checks by scanning barcode on each station

**Spec:**
```
Type:       Mobile application with backend (pest control inspections)
Auth:       Technician login
Data model: Site(id, client_name, address)
            BaitStation(id, site_id -> Site, barcode, location_desc)
            StationCheck(id, station_id -> BaitStation, tech_id, activity_level, bait_replaced, checked_at)
Features:   - Scan each bait station barcode to start a check
            - Record activity level and whether bait was replaced
            - Work offline in basements
            - Generate a PDF compliance report for the client
API:        REST
            GET  /sites/{id}/stations
            POST /station-checks
            GET  /sites/{id}/report.pdf
Storage:    PostgreSQL, SQLite on device
Tech stack: Kotlin, Java, Spring Boot
```

---

## Example 93

**Intent:**
cracked phone screen repair, technician comes to your office

**Spec:**
```
Type:       Mobile application with backend (on-site phone repair)
Auth:       Email or Google sign-in
Data model: DeviceModel(id, brand, model)
            RepairPrice(id, model_id -> DeviceModel, repair_type, price)
            RepairJob(id, customer_id, model_id -> DeviceModel, repair_type, address, slot, tech_id, status)
Features:   - Show the price for a model and repair type
            - Book a technician visit at home or office
            - Track technician arrival
            - Pay after the repair and get a warranty card
API:        REST
            GET  /prices?model={id}
            POST /jobs
            GET  /jobs/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, NestJS, Stripe
```

---

## Example 94

**Intent:**
mobile vet that comes to your house for cats who hate carriers lol

**Spec:**
```
Type:       Mobile application with backend (mobile vet visits)
Auth:       Email + password
Data model: Pet(id, owner_id, name, species, birth_date, weight_kg)
            HomeVisit(id, pet_id -> Pet, vet_id, address, slot, reason, status)
            MedicalRecord(id, pet_id -> Pet, visit_id -> HomeVisit, diagnosis, treatment)
Features:   - Book a home visit for one or more pets
            - Show vaccination due dates per pet
            - Store visit notes and prescriptions
            - Let vets plan their daily driving route
API:        REST
            POST /home-visits
            GET  /pets/{id}/records
            GET  /vets/me/route
Storage:    PostgreSQL
Tech stack: React Native, Python, Django
```

---

## Example 95

**Intent:**
dog daycare app with live webcam and daily report cards for owners

**Spec:**
```
Type:       Mobile application with backend (dog daycare)
Auth:       Email + password
Data model: Dog(id, owner_id, name, breed, vaccinations_valid_to)
            Attendance(id, dog_id -> Dog, date, checked_in_at, checked_out_at)
            ReportCard(id, attendance_id -> Attendance, mood, ate, notes, photo_urls)
Features:   - Book daycare days and buy day packs
            - Block booking if vaccinations are expired
            - Stream the playroom webcams during opening hours
            - Send a report card with photos at pickup
API:        REST
            POST /bookings
            GET  /cameras/{id}/stream-url
            POST /attendance/{id}/report-card
Storage:    PostgreSQL, S3
Tech stack: Flutter, Node.js, AWS IVS (video)
```

---

## Example 96

**Intent:**
junk removal - upload pics of stuff and get price

**Spec:**
```
Type:       Mobile application with backend (junk removal)
Auth:       Phone number + OTP
Data model: Job(id, customer_id, address, photo_urls, estimated_volume, quote, slot, status)
            Crew(id, truck, members)
Features:   - Upload photos of items to remove
            - Get a quote based on truck-load fraction
            - Book a pickup slot
            - Show crew arrival and take payment after the job
API:        REST
            POST /jobs
            PATCH /jobs/{id}/quote
            POST /jobs/{id}/book
Storage:    PostgreSQL, S3
Tech stack: React Native, Supabase, Stripe
```

---

## Example 97

**Intent:**
hire 2 guys to help move boxes for few hours

**Spec:**
```
Type:       Mobile application with backend (moving helpers)
Auth:       Email + password; helpers verified with ID
Data model: Helper(id, name, rating, has_van, hourly_rate)
            MoveJob(id, customer_id, from_address, to_address, date, hours, helpers_needed, status)
            JobAssignment(id, job_id -> MoveJob, helper_id -> Helper)
Features:   - Post a job with addresses, date and number of helpers
            - Let helpers accept jobs until filled
            - Pay helpers per hour with tracked start and end times
            - Rate helpers after the job
API:        REST
            POST /jobs
            POST /jobs/{id}/accept
            POST /jobs/{id}/finish
Storage:    PostgreSQL
Tech stack: Flutter, Go, Stripe Connect
```

---

## Example 98

**Intent:**
snow plowing on demand for driveways in winter

**Spec:**
```
Type:       Mobile application with backend (snow plowing)
Auth:       Email + password
Data model: Driveway(id, customer_id, address, size)
            PlowRequest(id, driveway_id -> Driveway, plower_id, status, before_photo, after_photo)
            SeasonPlan(id, driveway_id -> Driveway, trigger_cm, price)
Features:   - Request a one-time plow or buy a season plan
            - Trigger plowing automatically when snowfall passes a threshold
            - Dispatch nearby plowers
            - Send before and after photos
API:        REST
            POST /requests
            POST /season-plans
            POST /requests/{id}/complete
Storage:    PostgreSQL
Tech stack: React Native, Node.js, OpenWeatherMap API
```

---

## Example 99

**Intent:**
Im a piano teacher and want app for my students parents to book lesson and pay me

**Spec:**
```
Type:       Mobile application with backend (music lesson booking)
Auth:       Email + password
Data model: Student(id, parent_id, name, level)
            LessonSlot(id, weekday, start_time, duration_min)
            Lesson(id, student_id -> Student, date, slot_id -> LessonSlot, status, paid)
Features:   - Let parents book a weekly recurring lesson
            - Reschedule with 24 hours' notice
            - Pay per term or per lesson
            - Share practice notes after each lesson
API:        REST
            GET  /slots
            POST /lessons
            PATCH /lessons/{id}
            POST /lessons/{id}/notes
Storage:    PostgreSQL
Tech stack: Flutter, Firebase, Stripe
```

---

## Example 100

**Intent:**
driving school app: book lessons with instructor and track skills learned

**Spec:**
```
Type:       Mobile application with backend (driving school)
Auth:       Email + password
Data model: Instructor(id, name, car, areas)
            Learner(id, name, licence_number, test_date)
            DrivingLesson(id, instructor_id -> Instructor, learner_id -> Learner, starts_at, pickup_address)
            SkillProgress(id, learner_id -> Learner, skill, level)
Features:   - Book lessons from the instructor's calendar
            - Track skills like parallel parking and roundabouts
            - Let instructors rate skills after each lesson
            - Buy lesson packs
API:        REST
            GET  /instructors/{id}/slots
            POST /lessons
            PUT  /learners/{id}/skills
Storage:    PostgreSQL
Tech stack: React Native, Laravel, Stripe
```

---

## Example 101

**Intent:**
swim school, parents see which level kid is in and book make-up lessons

**Spec:**
```
Type:       Mobile application with backend (swim school)
Auth:       Email + password
Data model: Swimmer(id, parent_id, name, level)
            ClassGroup(id, level, weekday, time, pool_lane, capacity)
            Enrolment(id, swimmer_id -> Swimmer, class_id -> ClassGroup)
            MakeUp(id, swimmer_id -> Swimmer, class_id -> ClassGroup, date)
Features:   - Show the child's level and skills to pass
            - Report an absence and earn a make-up credit
            - Book make-ups in classes of the same level
            - Notify parents when the child moves up a level
API:        REST
            GET  /swimmers/{id}
            POST /absences
            POST /make-ups
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework
```

---

## Example 102

**Intent:**
language exchange app where I meet a native speaker for coffee and we teach each other

**Spec:**
```
Type:       Mobile application with backend (language exchange)
Auth:       Email + password or Apple sign-in
Data model: User(id, name, city, native_languages, learning_languages, level)
            ExchangeRequest(id, from_id -> User, to_id -> User, status)
            Meetup(id, request_id -> ExchangeRequest, place, starts_at)
Features:   - Match people with opposite native and learning languages in the same city
            - Send exchange requests and chat after accepting
            - Suggest public cafes for meetups
            - Report and block users
API:        REST
            GET  /matches
            POST /requests
            POST /meetups
            POST /reports
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Socket.IO
```

---

## Example 103

**Intent:**
beach clean up events, volunteers log how much trash they collect

**Spec:**
```
Type:       Mobile application with backend (beach cleanup)
Auth:       Email + password
Data model: Cleanup(id, beach, date, organiser_id)
            Participation(id, cleanup_id -> Cleanup, volunteer_id, hours)
            DebrisLog(id, cleanup_id -> Cleanup, volunteer_id, category, count, weight_kg)
Features:   - Join upcoming cleanups
            - Log collected items by category like plastic bottles and nets
            - Show total kilos collected per beach
            - Export data for marine research partners
API:        REST
            GET  /cleanups
            POST /cleanups/{id}/join
            POST /cleanups/{id}/debris
            GET  /stats/beaches
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 104

**Intent:**
animal shelter volunteers sign up to walk dogs and log walks

**Spec:**
```
Type:       Mobile application with backend (shelter volunteers)
Auth:       Email + password, orientation completed flag
Data model: Animal(id, name, kennel, walk_level, notes)
            Volunteer(id, name, level)
            Walk(id, animal_id -> Animal, volunteer_id -> Volunteer, started_at, ended_at, behaviour_notes)
Features:   - Show dogs not yet walked today
            - Allow walking only dogs at or below the volunteer's level
            - Log walk time and behaviour notes
            - Let staff update animal notes
API:        REST
            GET  /animals/needs-walk
            POST /walks
            PATCH /animals/{id}
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails
```

---

## Example 105

**Intent:**
report potholes and broken streetlights to the city with photo

**Spec:**
```
Type:       Mobile application with backend (civic issue reporting)
Auth:       Optional email login; anonymous reports allowed
Data model: Issue(id, category, description, photo_url, lat, lng, status, created_at)
            IssueUpdate(id, issue_id -> Issue, status, note, created_at)
            Upvote(id, issue_id -> Issue, device_id)
Features:   - Submit an issue with photo and map location
            - Detect duplicates nearby and upvote instead
            - Route issues to the right city department
            - Notify the reporter when the issue is fixed
API:        REST
            POST /issues
            GET  /issues?bbox={bbox}
            POST /issues/{id}/upvote
            POST /issues/{id}/updates
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Python, Django, Open311
```

---

## Example 106

**Intent:**
community fridge app shows what food is inside right now

**Spec:**
```
Type:       Mobile application with backend (community fridges)
Auth:       Anonymous browsing; volunteers sign in with email
Data model: Fridge(id, name, address, lat, lng)
            StockPost(id, fridge_id -> Fridge, photo_url, items_text, posted_at)
            CleanLog(id, fridge_id -> Fridge, volunteer_id, cleaned_at)
Features:   - Show fridges on a map with the latest photo of contents
            - Post a photo when dropping off food
            - Let followers get alerts when a fridge is restocked
            - Track cleaning rota and temperature checks
API:        REST
            GET  /fridges
            POST /fridges/{id}/stock
            POST /fridges/{id}/clean
Storage:    Supabase (PostgreSQL + storage)
Tech stack: React Native, Supabase
```

---

## Example 107

**Intent:**
restaurants post leftover food at closing time, charities claim and pick it up

**Spec:**
```
Type:       Mobile application with backend (food rescue)
Auth:       Email + password; organisations verified
Data model: Donor(id, name, address)
            Charity(id, name, address)
            Donation(id, donor_id -> Donor, description, portions, pickup_until, status)
            Claim(id, donation_id -> Donation, charity_id -> Charity, picked_up_at)
Features:   - Post surplus food with portions and pickup deadline
            - Alert nearby charities about new donations
            - Claim a donation and confirm pickup
            - Report kilos of food rescued per month
API:        REST
            POST /donations
            GET  /donations/nearby
            POST /donations/{id}/claim
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Node.js, Firebase Cloud Messaging
```

---

## Example 108

**Intent:**
old people living alone, volunteers visit them, need app to plan visits and write how they were

**Spec:**
```
Type:       Mobile application with backend (senior companion visits)
Auth:       Volunteer email + password, background check status
Data model: Senior(id, name, address, emergency_contact, interests)
            Volunteer(id, name, phone, checked)
            CompanionVisit(id, senior_id -> Senior, volunteer_id -> Volunteer, scheduled_at, wellbeing_score, notes)
Features:   - Match volunteers with seniors by area and interests
            - Schedule recurring weekly visits
            - Record a short wellbeing check after each visit
            - Alert the coordinator when a concern is flagged
API:        REST
            POST /visits
            POST /visits/{id}/report
            GET  /seniors/{id}/visits
Storage:    PostgreSQL
Tech stack: React Native, Python, Django
```

---
## Example 109

**Intent:**
zoo app with map and animal feeding times notification

**Spec:**
```
Type:       Mobile application with backend (zoo visitor guide)
Auth:       Staff login for content updates
Data model: Enclosure(id, name, species, lat, lng)
            FeedingTalk(id, enclosure_id -> Enclosure, time, days)
            Notice(id, enclosure_id -> Enclosure, message, active_until)
Features:   - Show an interactive zoo map with the visitor's position
            - Remind visitors 10 minutes before a chosen feeding talk
            - Show closures like "lions inside today"
            - Give walking directions between enclosures
API:        REST
            GET  /enclosures
            GET  /feeding-talks?date={d}
            POST /notices
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Mapbox
```

---

## Example 110

**Intent:**
trail conditions in national park, hikers report mud or fallen trees

**Spec:**
```
Type:       Mobile application with backend (trail conditions)
Auth:       Email + password; rangers have verified role
Data model: Trail(id, name, length_km, difficulty, geojson)
            ConditionReport(id, trail_id -> Trail, user_id, condition, note, photo_url, lat, lng, created_at)
            Closure(id, trail_id -> Trail, reason, until)
Features:   - Show trails with the latest reported conditions
            - Submit a report with photo and GPS point
            - Let rangers post official closures
            - Download trail maps for offline use
API:        REST
            GET  /trails
            POST /trails/{id}/reports
            POST /trails/{id}/closures
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Go, Mapbox offline maps
```

---

## Example 111

**Intent:**
brewery passport app: visit breweries in our region, get stamp by scanning, prize at 10

**Spec:**
```
Type:       Mobile application with backend (brewery passport)
Auth:       Email + password, age 21+ confirmation
Data model: Brewery(id, name, address, qr_secret)
            Stamp(id, user_id, brewery_id -> Brewery, stamped_at)
            Reward(id, user_id, tier, redeemed_at)
Features:   - Show breweries on a map with opening hours
            - Collect a stamp by scanning the brewery's rotating QR code
            - Unlock rewards at 5 and 10 stamps
            - Prevent more than one stamp per brewery per day
API:        REST
            GET  /breweries
            POST /stamps
            POST /rewards/{id}/redeem
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 112

**Intent:**
hotel guests order room service and request towels from app

**Spec:**
```
Type:       Mobile application with backend (hotel guest services)
Auth:       Room number + last name, valid during stay
Data model: Stay(id, room_number, guest_last_name, check_in, check_out)
            RoomServiceOrder(id, stay_id -> Stay, items, total, status)
            HousekeepingRequest(id, stay_id -> Stay, item, status)
Features:   - Order room service and charge it to the room
            - Request towels, pillows or cleaning
            - Chat with reception
            - Show staff a live queue of requests by department
API:        REST + WebSocket
            POST /orders
            POST /requests
            WS   /staff/queue
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Socket.IO
```

---

## Example 113

**Intent:**
ski resort app lift queue times and which runs are open

**Spec:**
```
Type:       Mobile application with backend (ski resort)
Data model: Lift(id, name, status, wait_minutes, updated_at)
            Run(id, name, difficulty, status, groomed_today)
            SnowReport(id, date, base_cm, new_cm, temperature)
Features:   - Show live lift wait times from gate scanners
            - Show open runs and grooming on a trail map
            - Display the daily snow report
            - Track the skier's vertical metres for the day
API:        REST
            GET  /lifts
            GET  /runs
            GET  /snow-report
Storage:    PostgreSQL, Redis
Tech stack: Swift, Kotlin, Node.js
```

---

## Example 114

**Intent:**
campsite booking, choose exact pitch on map, electric or not

**Spec:**
```
Type:       Mobile application with backend (campsite booking)
Auth:       Email + password
Data model: Pitch(id, number, x, y, has_electric, max_length_m, type)
            Reservation(id, pitch_id -> Pitch, guest_id, arrive_on, depart_on, people, status)
Features:   - Pick a pitch on a site map
            - Filter by electric hookup and vehicle length
            - Pay a deposit at booking
            - Show arrival instructions and gate code
API:        REST
            GET  /pitches/available?from={d}&to={d}
            POST /reservations
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Stripe
```

---

## Example 115

**Intent:**
theme park wait times + virtual queue for rides

**Spec:**
```
Type:       Mobile application with backend (theme park virtual queue)
Auth:       Ticket barcode linked to the app
Data model: Ride(id, name, status, wait_minutes, height_min_cm)
            VirtualQueueSlot(id, ride_id -> Ride, return_from, return_to, capacity)
            Reservation(id, slot_id -> VirtualQueueSlot, ticket_id, status)
Features:   - Show live wait times for every ride
            - Reserve a return time instead of standing in line
            - Allow one active virtual reservation per ticket
            - Notify when the return window opens
            - Scan the reservation at the ride entrance
API:        REST
            GET  /rides
            POST /rides/{id}/virtual-queue
            POST /reservations/{id}/scan
Storage:    PostgreSQL, Redis
Tech stack: React Native, Go
```

---

## Example 116

**Intent:**
tennis court booking at our club, members only, 1 hour slots

**Spec:**
```
Type:       Mobile application with backend (tennis court booking)
Auth:       Member number + password
Data model: Court(id, name, surface, has_lights)
            CourtBooking(id, court_id -> Court, member_id, partner_ids, starts_at)
Features:   - Show court grid for the next 7 days
            - Book 1-hour slots and add partner members
            - Limit each member to 3 bookings per week
            - Unlock the court gate with a code during the booking
API:        REST
            GET  /courts/schedule?date={d}
            POST /bookings
            DELETE /bookings/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Express
```

---

## Example 117

**Intent:**
golf tee times and score card on phone

**Spec:**
```
Type:       Mobile application with backend (golf course)
Auth:       Email + password
Data model: TeeTime(id, starts_at, max_players, price)
            TeeBooking(id, tee_time_id -> TeeTime, golfer_id, players)
            Scorecard(id, golfer_id, played_on, holes_json, total)
Features:   - Book tee times for up to 4 players
            - Enter scores hole by hole with GPS distance to the green
            - Calculate net score with handicap
            - Show the club's weekly leaderboard
API:        REST
            GET  /tee-times?date={d}
            POST /tee-bookings
            POST /scorecards
Storage:    PostgreSQL
Tech stack: React Native, Python, Django
```

---

## Example 118

**Intent:**
climbing gym app track which routes I sent and see new routes

**Spec:**
```
Type:       Mobile application with backend (climbing gym routes)
Auth:       Email + password
Data model: Route(id, wall, grade, colour, setter, set_on, removed_on)
            Ascent(id, route_id -> Route, climber_id, style, attempts, climbed_at)
Features:   - Show current routes by wall and grade
            - Log ascents as flash, redpoint or attempt
            - Let setters add and retire routes
            - Show a personal grade pyramid
API:        REST
            GET  /routes?wall={w}
            POST /routes/{id}/ascents
            POST /routes
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 119

**Intent:**
lane booking for lap swimming at public pool

**Spec:**
```
Type:       Mobile application with backend (pool lane booking)
Auth:       Email + password
Data model: Lane(id, number, speed)
            LaneSession(id, lane_id -> Lane, starts_at, capacity)
            LaneBooking(id, session_id -> LaneSession, swimmer_id, checked_in)
Features:   - Book a spot in a slow, medium or fast lane
            - Show remaining spots per session
            - Check in at the turnstile with a QR code
            - Free no-show spots 10 minutes after the start
API:        REST
            GET  /sessions?date={d}
            POST /bookings
            POST /checkin
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 120

**Intent:**
escape room booking, choose room, players count, waiver

**Spec:**
```
Type:       Mobile application with backend (escape room booking)
Auth:       Email + password
Data model: Room(id, name, theme, min_players, max_players, duration_min)
            GameBooking(id, room_id -> Room, leader_id, players, starts_at, total)
            Waiver(id, booking_id -> GameBooking, player_name, signed_at)
Features:   - Show available time slots per room
            - Price the booking by number of players
            - Send waiver links to each player
            - Show the team's escape time and photo after the game
API:        REST
            GET  /rooms/{id}/slots
            POST /bookings
            POST /bookings/{id}/waivers
Storage:    PostgreSQL
Tech stack: Flutter, Django, Stripe
```

---

## Example 121

**Intent:**
karaoke room booking + order drinks to room

**Spec:**
```
Type:       Mobile application with backend (karaoke rooms)
Auth:       Phone number + OTP
Data model: KaraokeRoom(id, name, capacity, hourly_rate)
            RoomBooking(id, room_id -> KaraokeRoom, customer_id, starts_at, hours)
            DrinkOrder(id, booking_id -> RoomBooking, items, total, status)
Features:   - Book a room by size and time
            - Extend the booking from the app if the next slot is free
            - Order drinks and snacks to the room
            - Pay the full bill at the end in the app
API:        REST
            POST /bookings
            POST /bookings/{id}/extend
            POST /bookings/{id}/orders
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe
```

---

## Example 122

**Intent:**
food truck locator where trucks post where they are parked today

**Spec:**
```
Type:       Mobile application with backend (food truck locator)
Auth:       Truck owner email + password; eaters without login
Data model: Truck(id, name, cuisine, menu_url)
            Location(id, truck_id -> Truck, lat, lng, from_time, to_time, date)
            Follow(id, device_id, truck_id -> Truck)
Features:   - Let owners post today's location and hours
            - Show trucks open now on a map
            - Follow trucks and get a push when they post
            - Show menus and prices
API:        REST
            POST /trucks/{id}/locations
            GET  /locations/now
            POST /follows
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase
```

---

## Example 123

**Intent:**
order coffee ahead and skip the line, for my 2 cafes

**Spec:**
```
Type:       Mobile application with backend (coffee pre-order)
Auth:       Email + password or Apple/Google sign-in
Data model: Cafe(id, name, address)
            Product(id, name, price, modifiers)
            Order(id, cafe_id -> Cafe, customer_id, items, pickup_time, status)
            LoyaltyAccount(customer_id, stamps)
Features:   - Order drinks with modifiers like milk and size
            - Choose a pickup time at either cafe
            - Show orders on a barista tablet
            - Earn a free drink after 9 stamps
API:        REST
            GET  /menu
            POST /orders
            PATCH /orders/{id}/status
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe
```

---

## Example 124

**Intent:**
we order lunch together at office every friday, app collects everyones order and one person pays

**Spec:**
```
Type:       Mobile application with backend (office group lunch order)
Auth:       Company email sign-in
Data model: GroupOrder(id, organiser_id, restaurant, deadline, status)
            OrderLine(id, group_order_id -> GroupOrder, person_id, item, price, notes)
            Repayment(id, group_order_id -> GroupOrder, person_id, amount, paid)
Features:   - Start a group order with a restaurant menu link and deadline
            - Add personal items before the deadline
            - Show the organiser a combined order
            - Track who has paid the organiser back
API:        REST
            POST /group-orders
            POST /group-orders/{id}/lines
            GET  /group-orders/{id}/summary
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 125

**Intent:**
farmers market vendors take preorders so customers pick up at stall saturday

**Spec:**
```
Type:       Mobile application with backend (farmers market preorders)
Auth:       Email + password
Data model: Vendor(id, name, stall_number)
            Product(id, vendor_id -> Vendor, name, unit, price, stock)
            Preorder(id, customer_id, vendor_id -> Vendor, items, pickup_date, status)
Features:   - Let vendors list products and weekly stock
            - Preorder from several vendors in one basket
            - Close orders on Thursday night
            - Give vendors a packing list per customer
API:        REST
            GET  /vendors
            POST /preorders
            GET  /vendors/{id}/packing-list
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI, Stripe Connect
```

---

## Example 126

**Intent:**
bakery preorders for birthday cakes with custom text

**Spec:**
```
Type:       Mobile application with backend (cake preorders)
Auth:       Email or phone login
Data model: CakeDesign(id, name, sizes, base_price, photo_url)
            CakeOrder(id, design_id -> CakeDesign, size, flavour, message_text, pickup_date, status)
Features:   - Browse cake designs with sizes and flavours
            - Add custom text and an optional photo print
            - Require at least 48 hours' notice
            - Take a deposit and notify when ready
API:        REST
            GET  /designs
            POST /orders
            PATCH /orders/{id}/status
Storage:    PostgreSQL, S3
Tech stack: React Native, Laravel, Stripe
```

---

## Example 127

**Intent:**
surplus food from shops sold cheap at end of day as surprise bags

**Spec:**
```
Type:       Mobile application with backend (surplus food bags)
Auth:       Email + password
Data model: Store(id, name, address, lat, lng)
            BagOffer(id, store_id -> Store, price, quantity, pickup_from, pickup_to, date)
            Reservation(id, offer_id -> BagOffer, customer_id, code, collected)
Features:   - Show today's surprise bags near the user
            - Reserve and pay for a bag
            - Show a pickup code to the store
            - Let stores set daily quantities
API:        REST
            GET  /offers/nearby
            POST /offers/{id}/reserve
            POST /reservations/{id}/collect
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 128

**Intent:**
taproom tab app, open tab with card, order beers at table, close yourself

**Spec:**
```
Type:       Mobile application with backend (taproom tabs)
Auth:       Phone number + OTP, age verified at first visit
Data model: Tab(id, customer_id, table_number, opened_at, closed_at, total)
            TabItem(id, tab_id -> Tab, beer_id, size, price)
            Beer(id, name, style, abv, on_tap)
Features:   - Open a tab by pre-authorising a card
            - Order from the live tap list to the table
            - Close the tab and add a tip from the phone
            - Auto-close tabs at closing time
API:        REST
            POST /tabs
            POST /tabs/{id}/items
            POST /tabs/{id}/close
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails, Stripe
```

---

## Example 129

**Intent:**
Every year we organise a 3-day folk music festival in a field with about 4000 people, and the printed programme is always out of date. I'd love an app with the stage timetable that we can change on the fly, a map of toilets and food, and a way to send urgent messages like weather warnings.

**Spec:**
```
Type:       Mobile application with backend (festival programme)
Auth:       Organiser login for the admin panel
Data model: Stage(id, name, lat, lng)
            Performance(id, stage_id -> Stage, artist, starts_at, ends_at)
            PointOfInterest(id, kind, name, lat, lng)
            Broadcast(id, title, message, severity, sent_at)
Features:   - Show the live timetable per stage and day
            - Build a personal schedule with clash warnings
            - Show toilets, food and first aid on a site map
            - Push urgent broadcasts to all devices
            - Cache all data for poor field signal
API:        REST
            GET  /performances
            PUT  /performances/{id}
            POST /broadcasts
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Firebase Cloud Messaging
```

---

## Example 130

**Intent:**
conference app scan badges to exchange contacts

**Spec:**
```
Type:       Mobile application with backend (conference networking)
Auth:       Attendee email + registration code
Data model: Attendee(id, name, company, title, email, badge_code)
            Connection(id, scanner_id -> Attendee, scanned_id -> Attendee, note, created_at)
            Session(id, title, room, starts_at)
Features:   - Scan another attendee's badge QR to save their contact
            - Add a private note to each connection
            - Export connections as CSV after the event
            - Show the session agenda
API:        REST
            POST /connections
            GET  /connections/export
            GET  /sessions
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI
```

---

## Example 131

**Intent:**
cruise ship app daily activities and book shore excursions, works on ship wifi only

**Spec:**
```
Type:       Mobile application with backend (cruise ship guest app)
Auth:       Cabin number + date of birth
Data model: Activity(id, name, deck, starts_at)
            Excursion(id, port, date, title, price, capacity)
            ExcursionBooking(id, excursion_id -> Excursion, cabin, guests)
            Message(id, from_cabin, to_cabin, body, sent_at)
Features:   - Show the daily programme of onboard activities
            - Book shore excursions charged to the cabin account
            - Message other guests on board for free over ship Wi-Fi
            - Show deck plans
API:        REST
            GET  /activities?date={d}
            POST /excursions/{id}/book
            POST /messages
Storage:    PostgreSQL on an onboard server
Tech stack: Swift, Kotlin, Java, Spring Boot
```

---

## Example 132

**Intent:**
aquarium app tells you the show times and lets you scan tank signs to learn about fish

**Spec:**
```
Type:       Mobile application with backend (aquarium guide)
Data model: Tank(id, name, zone, qr_code)
            Species(id, tank_id -> Tank, common_name, latin_name, fact, image_url)
            Show(id, title, location, times)
Features:   - Scan a tank sign to see the species inside
            - Remind visitors before chosen shows
            - Show a map of zones
            - Offer content in 5 languages
API:        REST
            GET  /tanks/{qr_code}
            GET  /shows
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 133

**Intent:**
historic house tours, book a timed entry and audio tour unlocks inside

**Spec:**
```
Type:       Mobile application with backend (historic house timed entry)
Auth:       Email + password or guest checkout
Data model: TimedEntry(id, starts_at, capacity)
            EntryTicket(id, entry_id -> TimedEntry, visitor_count, qr_token)
            RoomStory(id, room_name, order, audio_url, beacon_id)
Features:   - Book a 30-minute entry slot
            - Scan the ticket at the door
            - Play each room's story automatically when the visitor's phone detects that room's beacon
            - Show member discounts
API:        REST
            GET  /entries?date={d}
            POST /tickets
            GET  /room-stories
Storage:    PostgreSQL
Tech stack: Flutter, iBeacon, Python, Django
```

---

## Example 134

**Intent:**
birdwatchers log what birds they saw where, share rare sightings

**Spec:**
```
Type:       Mobile application with backend (bird sightings)
Auth:       Email + password
Data model: Species(id, common_name, latin_name, rarity)
            Sighting(id, species_id -> Species, user_id, count, lat, lng, seen_at, photo_url)
            Alert(id, user_id, species_id -> Species, radius_km)
Features:   - Log a sighting with count, location and photo
            - Keep a personal life list
            - Push alerts for rare species seen nearby
            - Hide exact location of sensitive nesting species
API:        REST
            POST /sightings
            GET  /sightings?bbox={bbox}
            POST /alerts
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Go
```

---

## Example 135

**Intent:**
bowling alley lane reservation and shoe sizes

**Spec:**
```
Type:       Mobile application with backend (bowling lane booking)
Auth:       Phone number + OTP
Data model: Lane(id, number, bumpers_available)
            LaneReservation(id, lane_id -> Lane, customer_id, starts_at, games, players)
            Bowler(id, reservation_id -> LaneReservation, name, shoe_size)
Features:   - Book a lane for 1 or 2 hours
            - Enter bowler names and shoe sizes ahead
            - Request bumpers for kids
            - Send names to the scoring system before arrival
API:        REST
            GET  /lanes/availability
            POST /reservations
            POST /reservations/{id}/bowlers
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 136

**Intent:**
ice rink public skate sessions tickets and skate rental

**Spec:**
```
Type:       Mobile application with backend (ice rink sessions)
Auth:       Email + password
Data model: SkateSession(id, starts_at, ends_at, capacity, price)
            SessionTicket(id, session_id -> SkateSession, buyer_id, skaters, rental_sizes)
Features:   - Buy tickets for public sessions
            - Pre-book rental skates by size
            - Show sessions cancelled for hockey games
            - Scan tickets at the entrance
API:        REST
            GET  /sessions
            POST /tickets
            POST /tickets/scan
Storage:    PostgreSQL
Tech stack: React Native, Django
```

---

## Example 137

**Intent:**
horse riding stable, book lessons and see which horse you get

**Spec:**
```
Type:       Mobile application with backend (riding stable)
Auth:       Email + password
Data model: Horse(id, name, level, max_rider_weight, rest_day)
            Rider(id, name, level, weight_kg)
            RidingLesson(id, starts_at, instructor, level, capacity)
            LessonBooking(id, lesson_id -> RidingLesson, rider_id -> Rider, horse_id -> Horse)
Features:   - Book group or private lessons by level
            - Assign suitable horses by level and weight
            - Prevent horses being booked more than 2 lessons a day
            - Show riders their assigned horse before the lesson
API:        REST
            GET  /lessons
            POST /lessons/{id}/book
            PATCH /bookings/{id}/horse
Storage:    PostgreSQL
Tech stack: Flutter, Laravel
```

---

## Example 138

**Intent:**
fishing tournament app anglers submit catch photo with length

**Spec:**
```
Type:       Mobile application with backend (fishing tournament)
Auth:       Email + password, entry paid
Data model: Tournament(id, name, starts_at, ends_at, species_allowed)
            Angler(id, name, tournament_id -> Tournament)
            Catch(id, angler_id -> Angler, species, length_cm, photo_url, lat, lng, status)
Features:   - Submit a catch with a photo on a measuring board
            - Lock submissions to the tournament time window
            - Let judges verify or reject catches
            - Show a live leaderboard by total length
API:        REST
            POST /catches
            PATCH /catches/{id}/verify
            GET  /tournaments/{id}/leaderboard
Storage:    PostgreSQL, S3
Tech stack: React Native, Node.js
```

---
## Example 139

**Intent:**
home inspector app, go room by room, photos and notes, makes pdf report

**Spec:**
```
Type:       Mobile application with backend (home inspection reports)
Auth:       Inspector email + password
Data model: Inspection(id, inspector_id, address, client_name, inspected_on, status)
            Finding(id, inspection_id -> Inspection, area, item, severity, note)
            FindingPhoto(id, finding_id -> Finding, url)
Features:   - Walk through a checklist room by room
            - Add findings with severity and annotated photos
            - Work offline and sync when back in signal
            - Generate a branded PDF report and email it to the client
API:        REST
            POST /inspections
            POST /inspections/{id}/findings
            POST /inspections/{id}/report
Storage:    PostgreSQL, S3
Tech stack: Flutter, Python, FastAPI, WeasyPrint
```

---

## Example 140

**Intent:**
property manager does move-out inspections and compares with move-in photos

**Spec:**
```
Type:       Mobile application with backend (rental inspections)
Auth:       Company email + password
Data model: Unit(id, address, landlord_id)
            Inspection(id, unit_id -> Unit, kind, done_on, inspector_id)
            RoomPhoto(id, inspection_id -> Inspection, room, url, note)
Features:   - Record move-in and move-out inspections by room
            - Show move-in and move-out photos side by side
            - Mark damages with estimated repair cost
            - Send the deposit deduction summary to the tenant
API:        REST
            POST /units/{id}/inspections
            GET  /units/{id}/compare
            POST /inspections/{id}/deductions
Storage:    PostgreSQL, S3
Tech stack: React Native, Node.js, NestJS
```

---

## Example 141

**Intent:**
construction foreman daily log - weather, workers on site, what got done, photos

**Spec:**
```
Type:       Mobile application with backend (construction daily logs)
Auth:       Company SSO
Data model: Project(id, name, address)
            DailyLog(id, project_id -> Project, date, weather, crew_count, work_done, delays)
            LogPhoto(id, log_id -> DailyLog, url, caption)
            SafetyIncident(id, log_id -> DailyLog, description, severity)
Features:   - Fill a daily log with auto-filled weather
            - Record crew counts by trade
            - Attach photos and safety incidents
            - Export weekly logs as PDF for the client
API:        REST
            POST /projects/{id}/logs
            GET  /projects/{id}/logs?week={w}
            GET  /projects/{id}/logs/export
Storage:    PostgreSQL, S3
Tech stack: .NET MAUI, ASP.NET Core
```

---

## Example 142

**Intent:**
drivers do pre-trip truck inspection checklist on phone, defects go to mechanic

**Spec:**
```
Type:       Mobile application with backend (fleet vehicle inspections)
Auth:       Driver ID + PIN
Data model: Vehicle(id, unit_number, type, odometer)
            Inspection(id, vehicle_id -> Vehicle, driver_id, done_at, passed)
            Defect(id, inspection_id -> Inspection, item, description, photo_url, fixed_at)
Features:   - Scan the vehicle QR to start a checklist
            - Tick off brakes, lights, tyres and other items
            - Report defects with photos
            - Block a vehicle marked unsafe until a mechanic clears it
API:        REST
            POST /inspections
            POST /inspections/{id}/defects
            PATCH /defects/{id}/fix
Storage:    PostgreSQL
Tech stack: Kotlin, Java, Spring Boot
```

---

## Example 143

**Intent:**
HVAC company technicians get work orders on phone, parts used, customer signs

**Spec:**
```
Type:       Mobile application with backend (HVAC field service)
Auth:       Technician login
Data model: WorkOrder(id, customer_id, address, equipment, problem, tech_id, scheduled_at, status)
            PartUsed(id, work_order_id -> WorkOrder, part_number, qty)
            Signature(id, work_order_id -> WorkOrder, image_url, signed_at)
Features:   - Show assigned jobs with navigation
            - Record diagnosis, labour time and parts used
            - Capture the customer's signature
            - Create the invoice and email it on completion
API:        REST
            GET  /work-orders/mine
            POST /work-orders/{id}/parts
            POST /work-orders/{id}/complete
Storage:    PostgreSQL, S3
Tech stack: React Native, Ruby on Rails, QuickBooks API
```

---

## Example 144

**Intent:**
security guards scan nfc tags at checkpoints during patrol so we prove they did rounds

**Spec:**
```
Type:       Mobile application with backend (guard patrol)
Auth:       Guard ID + PIN on company phones
Data model: Site(id, name)
            Checkpoint(id, site_id -> Site, name, nfc_uid)
            PatrolRound(id, site_id -> Site, guard_id, started_at, finished_at)
            CheckpointScan(id, round_id -> PatrolRound, checkpoint_id -> Checkpoint, scanned_at)
Features:   - Scan NFC tags at each checkpoint
            - Report incidents with photos during a round
            - Alert supervisors when a round is missed
            - Send clients a daily patrol report
API:        REST
            POST /rounds
            POST /rounds/{id}/scans
            POST /incidents
Storage:    PostgreSQL
Tech stack: Kotlin (Android), Android NFC API, Go
```

---

## Example 145

**Intent:**
merchandisers visit supermarkets and photograph our shelf, check price and stock

**Spec:**
```
Type:       Mobile application with backend (retail merchandising audits)
Auth:       Company SSO
Data model: Store(id, chain, address)
            Audit(id, store_id -> Store, rep_id, visited_at)
            ShelfCheck(id, audit_id -> Audit, sku, facings, price, out_of_stock, photo_url)
Features:   - Show planned store visits
            - Record facings, price and stock per SKU
            - Photograph the shelf before and after fixing
            - Flag prices off from the agreed promotion
API:        REST
            GET  /visits/today
            POST /audits
            POST /audits/{id}/checks
Storage:    PostgreSQL, S3
Tech stack: Flutter, Python, Django
```

---

## Example 146

**Intent:**
fire extinguisher inspection app for buildings, monthly tag replaced by app

**Spec:**
```
Type:       Mobile application with backend (fire equipment inspections)
Auth:       Inspector login
Data model: Building(id, name, address)
            Extinguisher(id, building_id -> Building, qr_code, location, type, expires_on)
            InspectionRecord(id, extinguisher_id -> Extinguisher, inspector_id, pressure_ok, seal_ok, inspected_at)
Features:   - Scan the extinguisher QR code to open its record
            - Complete a monthly checklist
            - List units due or overdue per building
            - Generate compliance reports for the fire marshal
API:        REST
            GET  /extinguishers/{qr}
            POST /inspections
            GET  /buildings/{id}/due
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 147

**Intent:**
hotel housekeeping, maids see rooms to clean and mark them done, front desk sees

**Spec:**
```
Type:       Mobile application with backend (hotel housekeeping)
Auth:       Staff PIN
Data model: Room(id, number, floor, status)
            CleaningTask(id, room_id -> Room, attendant_id, kind, started_at, finished_at)
            MaintenanceIssue(id, room_id -> Room, description, photo_url)
Features:   - Assign rooms to attendants each morning
            - Mark rooms dirty, cleaning, clean or inspected
            - Report broken items with a photo
            - Show the front desk live room status
API:        REST + WebSocket
            GET  /tasks/mine
            PATCH /rooms/{id}/status
            WS   /rooms/live
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Socket.IO
```

---

## Example 148

**Intent:**
solar panel installer app, site survey with roof measurements and photos

**Spec:**
```
Type:       Mobile application with backend (solar site surveys)
Auth:       Company email + password
Data model: Lead(id, customer_name, address, monthly_bill)
            Survey(id, lead_id -> Lead, roof_pitch, orientation, shading, panel_count)
            SurveyPhoto(id, survey_id -> Survey, label, url)
Features:   - Record roof pitch, orientation and shading
            - Capture photos of roof, meter and breaker panel
            - Estimate yearly production and savings
            - Send the survey to the design team
API:        REST
            POST /leads/{id}/surveys
            POST /surveys/{id}/photos
            GET  /surveys/{id}/estimate
Storage:    PostgreSQL, S3
Tech stack: Swift (iPad), Python, FastAPI, PVWatts API
```

---

## Example 149

**Intent:**
roofers send estimates from the roof w/ photos, customer signs on the ipad

**Spec:**
```
Type:       Mobile application with backend (roofing estimates)
Auth:       Company login
Data model: Estimate(id, customer_name, address, squares, material, price, status)
            EstimatePhoto(id, estimate_id -> Estimate, url)
            Signature(id, estimate_id -> Estimate, image_url, signed_at)
Features:   - Calculate price from roof squares and material
            - Attach damage photos
            - Collect the customer's signature on the device
            - Email a signed PDF contract
API:        REST
            POST /estimates
            POST /estimates/{id}/sign
            GET  /estimates/{id}/pdf
Storage:    PostgreSQL, S3
Tech stack: Swift, SwiftUI, Node.js
```

---

## Example 150

**Intent:**
car dealership test drive booking, customer uploads license before

**Spec:**
```
Type:       Mobile application with backend (test drive booking)
Auth:       Email + password
Data model: Vehicle(id, vin, model, trim, colour, status)
            TestDrive(id, vehicle_id -> Vehicle, customer_id, starts_at, salesperson_id, status)
            Licence(id, customer_id, front_url, verified)
Features:   - Browse in-stock cars and book a test drive
            - Upload a driver's licence photo for verification
            - Assign a salesperson and confirm by SMS
            - Collect feedback after the drive
API:        REST
            GET  /vehicles
            POST /test-drives
            POST /licences
Storage:    PostgreSQL, S3
Tech stack: React Native, Java, Spring Boot
```

---

## Example 151

**Intent:**
warehouse pickers use phone to scan items for orders

**Spec:**
```
Type:       Mobile application with backend (warehouse picking)
Auth:       Employee badge scan + PIN
Data model: PickList(id, order_id, picker_id, status)
            PickLine(id, pick_list_id -> PickList, sku, bin_location, qty, picked_qty)
            Bin(id, code, zone)
Features:   - Show the next pick sorted by bin path
            - Scan the bin and item barcode to confirm
            - Report short picks
            - Show supervisors picks per hour per worker
API:        REST
            GET  /pick-lists/next
            POST /pick-lines/{id}/scan
            POST /pick-lines/{id}/short
Storage:    PostgreSQL
Tech stack: Kotlin (Zebra Android scanners), Go
```

---

## Example 152

**Intent:**
restaurant staff schedule and shift swap, also tips split

**Spec:**
```
Type:       Mobile application with backend (restaurant staff scheduling)
Auth:       Email + password
Data model: Employee(id, name, role, hourly_wage)
            Shift(id, employee_id -> Employee, starts_at, ends_at, role)
            TipPool(id, date, total)
            TipShare(id, pool_id -> TipPool, employee_id -> Employee, hours, amount)
Features:   - Publish the weekly schedule
            - Request and approve shift swaps
            - Split the daily tip pool by hours worked
            - Notify staff of schedule changes
API:        REST
            GET  /shifts?week={w}
            POST /swap-requests
            POST /tip-pools
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 153

**Intent:**
tree surgeon quotes from photos, customer picks date

**Spec:**
```
Type:       Mobile application with backend (tree work quotes)
Auth:       Phone + OTP
Data model: QuoteRequest(id, customer_id, address, photo_urls, work_type, status)
            Quote(id, request_id -> QuoteRequest, price, notes, valid_until)
            Job(id, quote_id -> Quote, date, crew)
Features:   - Request a quote with photos of the trees
            - Send a quote with price and notes
            - Accept and choose a job date
            - Remind the customer to move cars the day before
API:        REST
            POST /requests
            POST /requests/{id}/quote
            POST /quotes/{id}/accept
Storage:    PostgreSQL, S3
Tech stack: React Native, Laravel
```

---

## Example 154

**Intent:**
mobile notary booking, notary drives to you

**Spec:**
```
Type:       Mobile application with backend (mobile notary)
Auth:       Email + password; notaries verified by commission number
Data model: Notary(id, name, commission_number, commission_expires, area)
            NotaryAppointment(id, notary_id -> Notary, client_id, address, doc_type, signer_count, starts_at)
            JournalEntry(id, appointment_id -> NotaryAppointment, signer_name, id_type)
Features:   - Book a notary at an address and time
            - Price by number of signers and travel distance
            - Keep the notary's journal entries
            - Pay and receive a receipt
API:        REST
            POST /appointments
            POST /appointments/{id}/journal
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 155

**Intent:**
I sell agricultural seeds and my agronomists visit farms. They need to record crop problems with photos and GPS of the field, and give the farmer a recommendation sheet. Many farms have no signal at all.

**Spec:**
```
Type:       Mobile application with backend (agronomist farm visits)
Auth:       Company email + password
Data model: Farm(id, farmer_name, phone, village)
            Field(id, farm_id -> Farm, crop, area_ha, boundary_geojson)
            FieldVisit(id, field_id -> Field, agronomist_id, visited_at, problem, severity, recommendation)
            VisitPhoto(id, visit_id -> FieldVisit, url, lat, lng)
Features:   - Record visits fully offline and sync later
            - Draw field boundaries by walking with GPS
            - Attach geotagged photos of pests or disease
            - Send the farmer a recommendation by SMS
API:        REST
            POST /sync
            GET  /farms/{id}/fields
            GET  /fields/{id}/visits
Storage:    PostgreSQL with PostGIS, SQLite on device
Tech stack: Flutter, Python, Django, Africa's Talking SMS
```

---

## Example 156

**Intent:**
elevator inspector app, checklist per elevator and certificate issue

**Spec:**
```
Type:       Mobile application with backend (elevator inspections)
Auth:       Inspector licence number + password
Data model: Elevator(id, building_address, serial, capacity_kg, last_certified)
            ElevatorInspection(id, elevator_id -> Elevator, inspector_id, result, inspected_at)
            ChecklistItem(id, inspection_id -> ElevatorInspection, item, ok, note)
Features:   - Look up an elevator by serial number
            - Complete the statutory checklist
            - Issue a digital certificate when it passes
            - Schedule re-inspection when it fails
API:        REST
            GET  /elevators/{serial}
            POST /inspections
            GET  /inspections/{id}/certificate
Storage:    PostgreSQL
Tech stack: React Native, C#, ASP.NET Core
```

---

## Example 157

**Intent:**
online auction for our charity gala, guests bid from phone at tables

**Spec:**
```
Type:       Mobile application with backend (charity silent auction)
Auth:       Phone number + OTP, card on file
Data model: Lot(id, title, description, photo_url, starting_bid, closes_at)
            Bid(id, lot_id -> Lot, bidder_id, amount, placed_at)
            Bidder(id, name, table_number, paddle_number)
Features:   - Show lots with current high bid
            - Place bids with a minimum increment
            - Notify bidders when they are outbid
            - Close all lots at a set time and charge winners
API:        REST + WebSocket
            GET  /lots
            POST /lots/{id}/bids
            WS   /lots/live
Storage:    PostgreSQL, Redis
Tech stack: React Native, Node.js, Socket.IO, Stripe
```

---

## Example 158

**Intent:**
event staffing agency, workers pick up bar and catering shifts and clock in by GPS

**Spec:**
```
Type:       Mobile application with backend (event staffing)
Auth:       Email + password, right-to-work documents checked
Data model: Worker(id, name, skills, rating)
            EventShift(id, venue, role, starts_at, ends_at, pay_rate, slots)
            ShiftClaim(id, shift_id -> EventShift, worker_id -> Worker, clock_in, clock_out)
Features:   - Show open shifts matching the worker's skills
            - Claim shifts until slots are filled
            - Clock in and out only within 200 m of the venue
            - Export timesheets for payroll
API:        REST
            GET  /shifts/open
            POST /shifts/{id}/claim
            POST /claims/{id}/clock
Storage:    PostgreSQL
Tech stack: Flutter, Go
```

---

## Example 159

**Intent:**
cleaning crew checklist for offices, supervisor checks quality with score

**Spec:**
```
Type:       Mobile application with backend (commercial cleaning)
Auth:       Staff PIN
Data model: Site(id, client, address)
            Area(id, site_id -> Site, name, tasks)
            CleanRecord(id, area_id -> Area, cleaner_id, done_at)
            QualityAudit(id, site_id -> Site, supervisor_id, score, notes, audited_at)
Features:   - Show cleaners the task list per area
            - Tick tasks off with timestamps
            - Let supervisors score areas with photos
            - Send clients a monthly quality report
API:        REST
            GET  /sites/{id}/areas
            POST /clean-records
            POST /audits
Storage:    PostgreSQL
Tech stack: React Native, Django
```

---

## Example 160

**Intent:**
meter reader app water utility, route list, enter reading, photo if suspicious

**Spec:**
```
Type:       Mobile application with backend (utility meter reading)
Auth:       Employee login
Data model: Route(id, name, reader_id)
            Meter(id, route_id -> Route, account_no, address, last_reading)
            MeterRead(id, meter_id -> Meter, value, photo_url, read_at, flag)
Features:   - Download a route for offline reading
            - Enter readings in route order
            - Flag readings far from expected usage and require a photo
            - Upload reads to the billing system
API:        REST
            GET  /routes/{id}/download
            POST /reads/batch
Storage:    PostgreSQL, SQLite on device
Tech stack: Kotlin, Java, Spring Boot
```

---

## Example 161

**Intent:**
pharma reps log doctor visits and samples given

**Spec:**
```
Type:       Mobile application with backend (pharma rep visits)
Auth:       Company SSO
Data model: Physician(id, name, specialty, clinic_address)
            CallReport(id, physician_id -> Physician, rep_id, visited_at, products_discussed, notes)
            SampleDrop(id, call_id -> CallReport, product, lot_number, qty, signature_url)
Features:   - Plan visits to physicians in the territory
            - Record discussed products and notes
            - Capture the physician's signature for samples
            - Track sample inventory per rep
API:        REST
            POST /calls
            POST /calls/{id}/samples
            GET  /reps/me/inventory
Storage:    PostgreSQL
Tech stack: Swift (iPad), Java, Spring Boot
```

---

## Example 162

**Intent:**
tenants pay rent in app and see receipts

**Spec:**
```
Type:       Mobile application with backend (rent payments)
Auth:       Email + password, invited by landlord
Data model: Lease(id, unit, tenant_id, rent_amount, due_day)
            RentCharge(id, lease_id -> Lease, month, amount, late_fee, paid_at)
            Payment(id, charge_id -> RentCharge, method, amount, receipt_url)
Features:   - Show the monthly rent due
            - Pay by bank transfer or card
            - Set up autopay
            - Add late fees after the grace period
            - Download receipts
API:        REST
            GET  /charges
            POST /charges/{id}/pay
            POST /autopay
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe ACH
```

---

## Example 163

**Intent:**
savings group app like susu/chama, members contribute monthly and one member gets the pot each month

**Spec:**
```
Type:       Mobile application with backend (rotating savings group)
Auth:       Phone number + OTP
Data model: Group(id, name, contribution_amount, cycle_start)
            Member(id, group_id -> Group, name, phone, payout_order)
            Contribution(id, member_id -> Member, cycle_month, amount, paid_at)
            Payout(id, group_id -> Group, member_id -> Member, month, amount)
Features:   - Create a group and set the payout order
            - Record monthly contributions by mobile money
            - Remind members who have not paid
            - Show whose turn it is to receive the pot
API:        REST
            POST /groups
            POST /groups/{id}/contributions
            GET  /groups/{id}/status
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, M-Pesa Daraja API
```

---

## Example 164

**Intent:**
kids allowance app, parents add money weekly, kids see balance and save goals

**Spec:**
```
Type:       Mobile application with backend (kids allowance)
Auth:       Parent email + password; child profiles with PIN
Data model: Child(id, parent_id, name, balance)
            Allowance(id, child_id -> Child, amount, weekday)
            Transaction(id, child_id -> Child, amount, kind, note, created_at)
            Goal(id, child_id -> Child, name, target_amount)
Features:   - Pay allowance automatically each week
            - Let parents add or subtract money for chores
            - Show kids their balance and goal progress
            - Request money for a purchase with parent approval
API:        REST
            POST /children/{id}/transactions
            POST /children/{id}/goals
            POST /requests/{id}/approve
Storage:    PostgreSQL
Tech stack: Flutter, Firebase
```

---

## Example 165

**Intent:**
coffee shop baristas split tips by hours automatically

**Spec:**
```
Type:       Mobile application with backend (tip pooling)
Auth:       Staff email + password
Data model: Staff(id, name, role)
            ClockEntry(id, staff_id -> Staff, clock_in, clock_out)
            TipDay(id, date, cash_tips, card_tips)
            Payout(id, tip_day_id -> TipDay, staff_id -> Staff, amount)
Features:   - Clock in and out from the phone
            - Enter daily cash and card tips
            - Split tips by hours worked
            - Show each barista their weekly tip total
API:        REST
            POST /clock
            POST /tip-days
            GET  /payouts?week={w}
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 166

**Intent:**
gutter cleaning and window washing company app to book and see before/after

**Spec:**
```
Type:       Mobile application with backend (exterior cleaning service)
Auth:       Email + password
Data model: Home(id, customer_id, address, storeys, window_count)
            ServiceBooking(id, home_id -> Home, services, date, price, status)
            JobPhoto(id, booking_id -> ServiceBooking, stage, url)
Features:   - Price by storeys and window count
            - Book gutter cleaning, windows or both
            - Upload before and after photos
            - Offer a twice-a-year repeat plan
API:        REST
            POST /quotes
            POST /bookings
            POST /bookings/{id}/photos
Storage:    PostgreSQL, S3
Tech stack: Flutter, Python, Flask
```

---
## Example 167

**Intent:**
hi, i am working in a hospital in Germany. we want app for blood bank so donors with rare blood type get message when stock is low. please use Kotlin and Spring

**Spec:**
```
Type:       Mobile application with backend (rare blood donor alerts)
Auth:       Email + password, blood type confirmed by lab
Data model: Donor(id, name, blood_type, rh_subtype, phone, last_donation_at)
            StockLevel(id, blood_type, units, updated_at)
            DonorAlert(id, blood_type, message, sent_at)
            AlertResponse(id, alert_id -> DonorAlert, donor_id -> Donor, response)
Features:   - Store confirmed blood types including rare subtypes
            - Send alerts only to eligible donors of the needed type
            - Let donors answer "I can come" or "not now"
            - Show staff responses and expected arrivals
API:        REST
            POST /alerts
            POST /alerts/{id}/responses
            GET  /alerts/{id}/responses
Storage:    PostgreSQL
Tech stack: Kotlin (Android), Java, Spring Boot, Firebase Cloud Messaging
```

---

## Example 168

**Intent:**
plz make app 4 my yoga studio ppl buy class packs n book

**Spec:**
```
Type:       Mobile application with backend (yoga studio)
Auth:       Email + password
Data model: ClassPack(id, name, classes, price, valid_days)
            PackPurchase(id, pack_id -> ClassPack, member_id, classes_left, expires_on)
            YogaClass(id, style, teacher, starts_at, capacity)
            Reservation(id, class_id -> YogaClass, member_id, status)
Features:   - Buy class packs like 5 or 10 classes
            - Book classes using pack credits
            - Return a credit when cancelled 12 hours ahead
            - Warn members before a pack expires
API:        REST
            POST /packs/{id}/purchase
            GET  /classes?week={w}
            POST /classes/{id}/reserve
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe
```

---

## Example 169

**Intent:**
Our church runs a food pantry on Wednesdays and the line goes around the block in the cold. I want families to get a time slot from their phone and we see how many are coming and what they need, like diapers or baby formula.

**Spec:**
```
Type:       Mobile application with backend (food pantry appointments)
Auth:       Phone number + SMS code
Data model: Household(id, name, phone, size, zip_code)
            PantrySlot(id, date, start_time, capacity)
            Visit(id, slot_id -> PantrySlot, household_id -> Household, special_needs, status)
Features:   - Book a 15-minute pickup slot for Wednesday
            - Request extras like diapers or formula
            - Show volunteers the expected households and needs per slot
            - Check families in and record visits for reporting
            - Send an SMS reminder the morning of the visit
API:        REST
            GET  /slots?date={d}
            POST /visits
            PATCH /visits/{id}/checkin
            GET  /reports/monthly
Storage:    PostgreSQL
Tech stack: Flutter, Python, Django, Twilio
```

---

## Example 170

**Intent:**
neighbours share babysitting hours, earn points when you babysit, spend points when you need sitter

**Spec:**
```
Type:       Mobile application with backend (babysitting co-op)
Auth:       Email + password, invite-only group
Data model: Family(id, name, points_balance)
            SitRequest(id, family_id -> Family, starts_at, ends_at, children_count, status)
            SitAssignment(id, request_id -> SitRequest, sitter_family_id -> Family, hours)
Features:   - Post a request for a sitter
            - Accept requests from other co-op families
            - Transfer points per hour per child
            - Block requests when a family's balance is too low
API:        REST
            POST /requests
            POST /requests/{id}/accept
            POST /assignments/{id}/complete
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 171

**Intent:**
plant sitter app — someone waters your plants while on holiday

**Spec:**
```
Type:       Mobile application with backend (plant sitting)
Auth:       Email + password
Data model: Plant(id, owner_id, name, photo_url, water_every_days, notes)
            SittingJob(id, owner_id, sitter_id, starts_on, ends_on, price, status)
            CareLog(id, job_id -> SittingJob, plant_id -> Plant, watered_at, photo_url)
Features:   - Add plants with watering instructions
            - Find and book a sitter nearby
            - Send a photo each time plants are watered
            - Pay the sitter at the end of the job
API:        REST
            POST /plants
            POST /jobs
            POST /jobs/{id}/care-logs
Storage:    PostgreSQL, S3
Tech stack: Flutter, Node.js, Stripe Connect
```

---

## Example 172

**Intent:**
house sitter matching for people with pets, reviews both ways

**Spec:**
```
Type:       Mobile application with backend (house sitting)
Auth:       Email + password with ID verification
Data model: Listing(id, owner_id, location, pets_desc, starts_on, ends_on)
            Application(id, listing_id -> Listing, sitter_id, message, status)
            Review(id, listing_id -> Listing, author_id, target_id, stars, text)
Features:   - Post a house sit with dates and pet details
            - Apply to house sits as a sitter
            - Video call before confirming
            - Leave reviews in both directions after the sit
API:        REST
            POST /listings
            POST /listings/{id}/applications
            POST /reviews
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails, Twilio Video
```

---

## Example 173

**Intent:**
furniture assembly guy book, IKEA stuff, price per item

**Spec:**
```
Type:       Mobile application with backend (furniture assembly)
Auth:       Phone number + OTP
Data model: FurnitureType(id, name, price)
            AssemblyJob(id, customer_id, items, address, slot, assembler_id, total, status)
Features:   - Pick items from a list with fixed prices
            - Book a time slot
            - Assign an assembler by area
            - Charge the card after completion with optional tip
API:        REST
            GET  /furniture-types
            POST /jobs
            POST /jobs/{id}/complete
Storage:    PostgreSQL
Tech stack: Flutter, Go, Stripe
```

---

## Example 174

**Intent:**
appliance repair - washer broke, book technician, upload model number sticker

**Spec:**
```
Type:       Mobile application with backend (appliance repair)
Auth:       Email + password
Data model: Appliance(id, customer_id, kind, brand, model_number, sticker_photo_url)
            RepairVisit(id, appliance_id -> Appliance, symptom, slot, technician_id, diagnosis, cost, status)
Features:   - Photograph the model sticker and read it with OCR
            - Describe the symptom and book a visit
            - Let technicians order parts and book a second visit
            - Show warranty on the repair
API:        REST
            POST /appliances
            POST /visits
            PATCH /visits/{id}
Storage:    PostgreSQL, S3
Tech stack: React Native, Google ML Kit, Laravel
```

---

## Example 175

**Intent:**
locksmith emergency app locked out

**Spec:**
```
Type:       Mobile application with backend (emergency locksmith)
Auth:       Phone number + OTP
Data model: LockoutRequest(id, customer_id, lat, lng, lock_type, status, created_at)
            Locksmith(id, name, licence_no, lat, lng, available)
            Quote(id, request_id -> LockoutRequest, locksmith_id -> Locksmith, price, eta_min)
Features:   - Send a lockout request with GPS location
            - Receive quotes with price and arrival time
            - Accept a quote and track the locksmith
            - Require proof of residence before opening
API:        REST
            POST /requests
            POST /requests/{id}/quotes
            POST /quotes/{id}/accept
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Node.js
```

---

## Example 176

**Intent:**
car detailing van comes to your parking spot, choose package

**Spec:**
```
Type:       Mobile application with backend (mobile car detailing)
Auth:       Email + password
Data model: Package(id, name, duration_min, price)
            Car(id, customer_id, make, model, size)
            DetailBooking(id, car_id -> Car, package_id -> Package, address, slot, status)
Features:   - Choose a package priced by car size
            - Book a slot at home or work
            - Check water and power access with a short form
            - Send before and after photos
API:        REST
            GET  /packages
            POST /bookings
            POST /bookings/{id}/photos
Storage:    PostgreSQL, S3
Tech stack: React Native, Django, Stripe
```

---

## Example 177

**Intent:**
grooming van for dogs, book a slot, groomer sees dog notes like bites

**Spec:**
```
Type:       Mobile application with backend (mobile dog grooming)
Auth:       Email + password
Data model: Dog(id, owner_id, name, breed, coat, temperament_notes)
            GroomAppointment(id, dog_id -> Dog, service, address, starts_at, groomer_id)
            GroomNote(id, appointment_id -> GroomAppointment, note, photo_url)
Features:   - Book a groom at home by service and breed size
            - Show groomers temperament and health notes
            - Plan the groomer's route to minimise driving
            - Send a photo of the finished groom
API:        REST
            POST /appointments
            GET  /groomers/me/route
            POST /appointments/{id}/notes
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI, Google Directions API
```

---

## Example 178

**Intent:**
pet boarding kennel booking and vaccine upload

**Spec:**
```
Type:       Mobile application with backend (pet boarding)
Auth:       Email + password
Data model: Pet(id, owner_id, name, species, vaccine_doc_url, vaccine_valid_to)
            Kennel(id, size, type)
            Stay(id, pet_id -> Pet, kennel_id -> Kennel, check_in, check_out, feeding_instructions)
Features:   - Upload vaccination certificates for staff approval
            - Book a stay by dates and kennel size
            - Send daily photo updates during the stay
            - Bill extras like medication or walks
API:        REST
            POST /pets/{id}/vaccines
            POST /stays
            POST /stays/{id}/updates
Storage:    PostgreSQL, S3
Tech stack: React Native, Node.js
```

---

## Example 179

**Intent:**
I'd like a Flutter + Firebase app for our dog park: people check in so others know how many dogs and how big are there now

**Spec:**
```
Type:       Mobile application with backend (dog park check-in)
Auth:       Firebase Authentication (email or Google)
Data model: Park(id, name, lat, lng)
            CheckIn(id, park_id -> Park, user_id, dog_name, dog_size, checked_in_at, expires_at)
Features:   - Check in a dog with its size when arriving
            - Expire check-ins automatically after 90 minutes
            - Show current dogs by size per park
            - Notify when a friend's dog arrives
API:        Firebase Firestore SDK (no custom REST)
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase (Auth, Firestore, Cloud Functions)
```

---

## Example 180

**Intent:**
pet adoption from shelter, see dogs and cats and apply

**Spec:**
```
Type:       Mobile application with backend (pet adoption)
Auth:       Email + password
Data model: Animal(id, shelter_id, name, species, age, good_with_kids, photo_urls, status)
            AdoptionApplication(id, animal_id -> Animal, applicant_id, home_type, other_pets, status)
            Shelter(id, name, address)
Features:   - Browse adoptable animals with filters
            - Save favourites
            - Submit an adoption application
            - Let shelter staff review applications and book meet-and-greets
API:        REST
            GET  /animals?species={s}
            POST /animals/{id}/applications
            PATCH /applications/{id}
Storage:    PostgreSQL, S3
Tech stack: React Native, Laravel
```

---

## Example 181

**Intent:**
foster families for shelter animals log how pet is doing, request supplies

**Spec:**
```
Type:       Mobile application with backend (animal foster network)
Auth:       Email + password, approved foster status
Data model: Foster(id, name, address, capacity)
            Placement(id, animal_id, foster_id -> Foster, started_on, ended_on)
            Update(id, placement_id -> Placement, weight_kg, notes, photo_url)
            SupplyRequest(id, foster_id -> Foster, items, status)
Features:   - Show fosters their current animals and vet appointments
            - Post weekly weight and behaviour updates
            - Request food, litter and medicine
            - Let coordinators find fosters with free space
API:        REST
            POST /placements/{id}/updates
            POST /supply-requests
            GET  /fosters/available
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 182

**Intent:**
uber for wheelchair accessible rides to hospital appointments

**Spec:**
```
Type:       Mobile application with backend (accessible medical transport)
Auth:       Phone number + OTP; caregivers can book for patients
Data model: Rider(id, name, mobility_needs, caregiver_phone)
            TransportBooking(id, rider_id -> Rider, pickup_address, clinic_address, appointment_at, return_needed, status)
            Vehicle(id, driver_id, ramp, wheelchair_spaces)
Features:   - Book a ride before a medical appointment with return trip
            - Match vehicles with ramps or lifts to the rider's needs
            - Notify the caregiver at pickup and drop-off
            - Bill insurance or the rider
API:        REST
            POST /bookings
            PATCH /bookings/{id}/status
            GET  /bookings/{id}
Storage:    PostgreSQL
Tech stack: React Native, Java, Spring Boot
```

---

## Example 183

**Intent:**
elderly mum lives alone, app where she presses "I'm ok" every morning, if not i get alert

**Spec:**
```
Type:       Mobile application with backend (daily wellbeing check-in)
Auth:       Family email + password; senior phone paired by code
Data model: Senior(id, name, checkin_deadline, timezone)
            CheckIn(id, senior_id -> Senior, checked_at, mood)
            Contact(id, senior_id -> Senior, name, phone, order)
Features:   - Show one big "I'm OK" button each morning
            - Call the senior automatically if no check-in by the deadline
            - Alert family contacts in order by SMS and push
            - Show a monthly check-in history
API:        REST
            POST /checkins
            GET  /seniors/{id}/history
            POST /seniors/{id}/contacts
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Twilio (voice and SMS)
```

---

## Example 184

**Intent:**
caregivers for my dad (me, brother, nurse) need shared calendar and notes who did what

**Spec:**
```
Type:       Mobile application with backend (family care coordination)
Auth:       Email + password, care team invite
Data model: CareRecipient(id, name, conditions)
            CareTeamMember(id, recipient_id -> CareRecipient, name, role)
            CareTask(id, recipient_id -> CareRecipient, title, due_at, assigned_to_id -> CareTeamMember, done_at)
            CareNote(id, recipient_id -> CareRecipient, author_id -> CareTeamMember, text, created_at)
Features:   - Share a calendar of appointments and visits
            - Assign tasks like groceries or pharmacy pickups
            - Log notes after each visit
            - Store medication list and doctor contacts
API:        REST
            POST /tasks
            PATCH /tasks/{id}/done
            POST /notes
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 185

**Intent:**
therapist matching app ask questions and match with licensed therapist

**Spec:**
```
Type:       Mobile application with backend (therapist matching)
Auth:       Email + password with two-factor authentication
Data model: Therapist(id, name, licence_state, specialties, languages, accepts_insurance)
            Questionnaire(id, client_id, concerns, preferences_json)
            Match(id, client_id, therapist_id -> Therapist, score, status)
Features:   - Ask intake questions about concerns and preferences
            - Rank therapists licensed in the client's state
            - Book a free 15-minute intro call
            - Switch therapist at any time
API:        REST
            POST /questionnaires
            GET  /matches
            POST /matches/{id}/intro-call
Storage:    PostgreSQL (encrypted)
Tech stack: Swift, Kotlin, Python, Django
```

---

## Example 186

**Intent:**
dental clinic app - book cleaning, see xray photos, reminder every 6 months

**Spec:**
```
Type:       Mobile application with backend (dental clinic)
Auth:       Email + password
Data model: Patient(id, name, email, last_cleaning_on)
            DentalAppointment(id, patient_id -> Patient, dentist, kind, starts_at)
            XRay(id, patient_id -> Patient, image_url, taken_on)
Features:   - Book cleanings and check-ups
            - View x-ray images shared by the dentist
            - Remind patients 6 months after the last cleaning
            - Show treatment plan costs
API:        REST
            POST /appointments
            GET  /patients/me/xrays
Storage:    PostgreSQL, S3
Tech stack: Flutter, Node.js
```

---

## Example 187

**Intent:**
diabetes patients log glucose and clinic nurse checks it weekly

**Spec:**
```
Type:       Mobile application with backend (diabetes care)
Auth:       Email + password
Data model: Patient(id, name, nurse_id, target_low, target_high)
            GlucoseReading(id, patient_id -> Patient, mg_dl, context, measured_at)
            InsulinDose(id, patient_id -> Patient, units, type, given_at)
            NurseComment(id, patient_id -> Patient, text, created_at)
Features:   - Log glucose and insulin with meal context
            - Import readings from a CGM via HealthKit or Health Connect
            - Show time-in-range charts
            - Let the nurse review and comment weekly
API:        REST
            POST /readings
            POST /doses
            GET  /patients/{id}/summary
Storage:    PostgreSQL
Tech stack: React Native, HealthKit, Health Connect, Python, FastAPI
```

---

## Example 188

**Intent:**
maternity ward app for new parents: baby feeding log, nurse call, discharge checklist

**Spec:**
```
Type:       Mobile application with backend (maternity ward)
Auth:       Room-linked code from admission
Data model: Admission(id, room, mother_name, baby_name, admitted_at)
            FeedLog(id, admission_id -> Admission, kind, side, duration_min, logged_at)
            NurseRequest(id, admission_id -> Admission, reason, status)
            DischargeItem(id, admission_id -> Admission, item, done)
Features:   - Log feeds and diapers for the newborn
            - Request a nurse for non-urgent help
            - Show the discharge checklist and education videos
            - Share the feed log with the nurse
API:        REST
            POST /admissions/{id}/feeds
            POST /admissions/{id}/nurse-requests
            PATCH /discharge-items/{id}
Storage:    PostgreSQL
Tech stack: Flutter, C#, ASP.NET Core
```

---

## Example 189

**Intent:**
eye glasses shop reminds when eye test due and you can order contacts again

**Spec:**
```
Type:       Mobile application with backend (optician)
Auth:       Email + password
Data model: Customer(id, name, last_exam_on)
            Prescription(id, customer_id -> Customer, sphere, cylinder, axis, valid_to)
            ContactOrder(id, customer_id -> Customer, brand, boxes, status)
Features:   - Remind customers when the eye exam is due
            - Book an exam slot
            - Reorder contact lenses using the valid prescription
            - Block reorders after the prescription expires
API:        REST
            POST /exams
            POST /contact-orders
            GET  /prescriptions/me
Storage:    PostgreSQL
Tech stack: React Native, Django
```

---

## Example 190

**Intent:**
I work for a dialysis centre. Patients come 3 times a week and when there is a delay we have to phone everyone. App to tell them their chair time and send delays.

**Spec:**
```
Type:       Mobile application with backend (dialysis scheduling)
Auth:       Patient ID + SMS code
Data model: Chair(id, number)
            DialysisSlot(id, chair_id -> Chair, patient_id, starts_at, status)
            Delay(id, slot_ids, minutes, reason, created_at)
Features:   - Show patients their weekly chair times
            - Push and SMS delay notices to affected patients
            - Let patients request a slot change
            - Show transport drivers updated pickup times
API:        REST
            GET  /slots/mine
            POST /delays
            POST /slot-change-requests
Storage:    PostgreSQL
Tech stack: Flutter, Python, Django, Twilio
```

---

## Example 191

**Intent:**
mental health crisis line volunteers need app for their shift schedule and to swap

**Spec:**
```
Type:       Mobile application with backend (crisis line volunteer rota)
Auth:       Email + password with two-factor authentication
Data model: Volunteer(id, name, training_level)
            LineShift(id, starts_at, ends_at, needed)
            ShiftAssignment(id, shift_id -> LineShift, volunteer_id -> Volunteer, status)
Features:   - Show the monthly rota and open shifts
            - Require a minimum of 2 shifts per month
            - Swap shifts with another trained volunteer
            - Alert coordinators to unfilled overnight shifts
API:        REST
            GET  /shifts?month={m}
            POST /shifts/{id}/assign
            POST /assignments/{id}/swap
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 192

**Intent:**
refugee newcomers find services in their language (doctor, lawyer, school)

**Spec:**
```
Type:       Mobile application with backend (newcomer services directory)
Auth:       Organisation login for editors; public browsing
Data model: Service(id, org_name, category, address, lat, lng, phone, free)
            ServiceLanguage(id, service_id -> Service, language)
            Translation(id, service_id -> Service, language, description)
Features:   - Browse services by category in 8 languages
            - Filter by services that speak the user's language
            - Call or navigate with one tap
            - Let organisations update their own listings
API:        REST
            GET  /services?category={c}&lang={l}
            PUT  /services/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Strapi CMS
```

---

## Example 193

**Intent:**
donate old clothes, app schedules pickup from my door by charity

**Spec:**
```
Type:       Mobile application with backend (clothing donation pickup)
Auth:       Email + password
Data model: DonationPickup(id, donor_id, address, bags, categories, date, status)
            Route(id, date, driver_id, pickup_ids)
Features:   - Schedule a pickup date for bags of clothes
            - Choose categories like adult, kids or shoes
            - Group pickups into driver routes by area
            - Email a tax receipt after pickup
API:        REST
            POST /pickups
            GET  /routes?date={d}
            POST /pickups/{id}/complete
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI
```

---

## Example 194

**Intent:**
tree planting volunteer days and track trees planted on map

**Spec:**
```
Type:       Mobile application with backend (tree planting)
Auth:       Email + password
Data model: PlantingDay(id, site, date, capacity)
            Tree(id, day_id -> PlantingDay, species, lat, lng, planted_by)
            SurvivalCheck(id, tree_id -> Tree, alive, checked_at)
Features:   - Sign up for planting days
            - Record each tree's species and GPS location
            - Show all planted trees on a map
            - Log survival checks a year later
API:        REST
            POST /days/{id}/signup
            POST /trees
            POST /trees/{id}/checks
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Go
```

---

## Example 195

**Intent:**
polling station wait time, voters report how long line is

**Spec:**
```
Type:       Mobile application with backend (polling station wait times)
Data model: PollingStation(id, name, address, lat, lng)
            WaitReport(id, station_id -> PollingStation, minutes, reported_at, device_hash)
Features:   - Find the polling station by address
            - Report the current line wait in minutes
            - Show the median wait from the last 30 minutes
            - Rate-limit reports per device to stop spam
API:        REST
            GET  /stations?address={a}
            POST /stations/{id}/reports
            GET  /stations/{id}/wait
Storage:    PostgreSQL, Redis
Tech stack: React Native, Node.js
```

---

## Example 196

**Intent:**
organ donor registry app sign up and carry digital card

**Spec:**
```
Type:       Mobile application with backend (organ donor registry)
Auth:       National ID + bank-grade e-ID login
Data model: Registrant(id, national_id_hash, name, date_of_birth)
            DonorDecision(id, registrant_id -> Registrant, organs, decision, updated_at)
            FamilyNotice(id, registrant_id -> Registrant, contact_email)
Features:   - Register a donation decision per organ
            - Show a digital donor card
            - Email chosen family members about the decision
            - Let only authorised hospitals query the registry
API:        REST
            PUT  /decisions/me
            GET  /cards/me
            GET  /registry/{national_id} (hospital only)
Storage:    PostgreSQL (encrypted)
Tech stack: Kotlin, Swift, Java, Spring Boot
```

---
## Example 197

**Intent:**
campus parking permits app

**Spec:**
```
Type:       Mobile application with backend (campus parking permits)
Auth:       University SSO
Data model: PermitType(id, name, lots, price, term)
            Permit(id, permit_type_id -> PermitType, holder_id, plate, valid_from, valid_to)
            Citation(id, plate, lot, amount, status)
Features:   - Buy a semester or daily permit
            - Register up to 2 plates per permit
            - Show which lots the permit allows
            - Pay or appeal parking citations
API:        REST
            POST /permits
            GET  /permits/mine
            POST /citations/{id}/appeal
Storage:    PostgreSQL
Tech stack: React Native, Java, Spring Boot
```

---

## Example 198

**Intent:**
students swap textbooks with each other at my uni

**Spec:**
```
Type:       Mobile application with backend (textbook exchange)
Auth:       University email login
Data model: Book(id, isbn, title, author)
            BookListing(id, book_id -> Book, seller_id, condition, price, status)
            CourseBook(id, course_code, book_id -> Book)
Features:   - Scan an ISBN barcode to list a book
            - Search listings by course code
            - Message the seller and agree a campus meetup
            - Mark the book as sold
API:        REST
            POST /listings
            GET  /listings?course={code}
            PATCH /listings/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Open Library API
```

---

## Example 199

**Intent:**
meal plan balance and dining dollars on student phone

**Spec:**
```
Type:       Mobile application with backend (campus card balance)
Auth:       University SSO
Data model: CampusAccount(student_id, meal_swipes_left, dining_dollars)
            CardTransaction(id, student_id, location, amount, kind, at)
Features:   - Show remaining meal swipes and dining dollars
            - List recent transactions by location
            - Top up dining dollars by card
            - Report a lost student card and freeze it
API:        REST
            GET  /account
            GET  /transactions
            POST /topups
            POST /card/freeze
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, C#, ASP.NET Core
```

---

## Example 200

**Intent:**
international students get matched with local buddy before arrival

**Spec:**
```
Type:       Mobile application with backend (international buddy programme)
Auth:       University email login
Data model: Student(id, name, home_country, languages, faculty, arrival_date, role)
            BuddyPair(id, newcomer_id -> Student, buddy_id -> Student, created_at)
            Checklist(id, newcomer_id -> Student, item, done)
Features:   - Match newcomers with local buddies by faculty and language
            - Chat before arrival
            - Track an arrival checklist (bank, SIM, housing)
            - Invite pairs to welcome events
API:        REST
            POST /pairs/auto-match
            GET  /pairs/mine
            PATCH /checklist/{id}
Storage:    PostgreSQL
Tech stack: React Native, Firebase
```

---

## Example 201

**Intent:**
on campus job board for student assistant jobs, apply in app

**Spec:**
```
Type:       Mobile application with backend (campus jobs)
Auth:       University SSO
Data model: Job(id, department, title, hours_per_week, pay_rate, closes_on)
            JobApplication(id, job_id -> Job, student_id, cv_url, status)
Features:   - List student jobs by department
            - Apply with a CV saved in the profile
            - Let departments shortlist and reject applicants
            - Check work-hour limits for international students
API:        REST
            GET  /jobs
            POST /jobs/{id}/applications
            PATCH /applications/{id}
Storage:    PostgreSQL, S3
Tech stack: Flutter, Python, Django
```

---

## Example 202

**Intent:**
how full is the campus gym right now

**Spec:**
```
Type:       Mobile application with backend (campus gym occupancy)
Data model: Facility(id, name, max_capacity)
            OccupancyEvent(id, facility_id -> Facility, direction, at)
            HourlyAverage(facility_id -> Facility, weekday, hour, avg_count)
Features:   - Count entries and exits from turnstile events
            - Show the current number of people per area
            - Show a busy-times chart by hour
            - Notify when the gym drops below 50% full
API:        REST
            POST /events
            GET  /facilities/occupancy
            GET  /facilities/{id}/hourly
Storage:    Redis (live counts), PostgreSQL (history)
Tech stack: React Native, Go
```

---

## Example 203

**Intent:**
library app reserve seat and renew books

**Spec:**
```
Type:       Mobile application with backend (university library)
Auth:       University SSO
Data model: Seat(id, floor, zone, has_power)
            SeatReservation(id, seat_id -> Seat, student_id, starts_at, ends_at)
            Loan(id, student_id, item_title, due_on, renewals)
Features:   - Reserve a seat in quiet or group zones
            - Renew loans up to 3 times
            - Remind students 2 days before a due date
            - Show a digital library card barcode
API:        REST
            POST /seat-reservations
            GET  /loans
            POST /loans/{id}/renew
Storage:    PostgreSQL
Tech stack: Flutter, Java, Spring Boot
```

---

## Example 204

**Intent:**
uni recycling: scan bottle at reverse vending machine, earn points for campus cafe

**Spec:**
```
Type:       Mobile application with backend (campus recycling rewards)
Auth:       University email login
Data model: Machine(id, location, qr_code)
            Deposit(id, machine_id -> Machine, student_id, items, points, at)
            Redemption(id, student_id, reward, points, at)
Features:   - Link a deposit to the student by scanning the machine QR code
            - Award points per bottle and can
            - Redeem points for coffee discounts
            - Show a leaderboard by residence hall
API:        REST
            POST /deposits
            POST /redemptions
            GET  /leaderboard
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 205

**Intent:**
self service bike repair stations on campus, report broken pump

**Spec:**
```
Type:       Mobile application with backend (bike repair stations)
Data model: RepairStation(id, name, lat, lng, tools)
            StationIssue(id, station_id -> RepairStation, description, photo_url, status)
            Guide(id, title, video_url)
Features:   - Show repair stations on a campus map
            - Report a missing tool or broken pump
            - Show how-to videos for common fixes
            - Notify facilities staff of new issues
API:        REST
            GET  /stations
            POST /stations/{id}/issues
            GET  /guides
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 206

**Intent:**
we r a big masjid n want app for ramadan iftar registration and zakat payment, also donation for building

**Spec:**
```
Type:       Mobile application with backend (mosque Ramadan and donations)
Auth:       Email or phone + OTP
Data model: IftarNight(id, date, capacity, sponsor)
            IftarRegistration(id, night_id -> IftarNight, user_id, people)
            Donation(id, user_id, fund, amount, created_at)
            ZakatCalculation(id, user_id, assets_json, zakat_due)
Features:   - Register family members for community iftar nights
            - Sponsor an iftar night
            - Calculate zakat from savings, gold and investments
            - Donate to zakat, sadaqah or building funds
            - Email yearly donation receipts
API:        REST
            POST /iftar-nights/{id}/register
            POST /zakat/calculate
            POST /donations
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Stripe
```

---

## Example 207

**Intent:**
choir members see what songs for sunday, sheet music and practice audio by voice part

**Spec:**
```
Type:       Mobile application with backend (church choir)
Auth:       Email + password
Data model: Song(id, title, composer)
            Part(id, song_id -> Song, voice, sheet_pdf_url, audio_url)
            ServiceSetList(id, date, song_ids)
            Attendance(id, member_id, date, attending)
Features:   - Show the song list for the coming service
            - Play practice tracks for the member's voice part
            - Open sheet music PDFs offline
            - Mark attendance for rehearsals
API:        REST
            GET  /setlists/next
            GET  /songs/{id}/parts
            POST /attendance
Storage:    PostgreSQL, S3
Tech stack: React Native, Node.js
```

---

## Example 208

**Intent:**
confession appointment booking for parish priests

**Spec:**
```
Type:       Mobile application with backend (parish confession booking)
Auth:       Priests and staff log in; parishioners book without account
Data model: Priest(id, name, languages)
            ConfessionSlot(id, priest_id -> Priest, starts_at, language, booked)
Features:   - Show open slots by priest and language
            - Book a slot with only a first name for privacy
            - Let priests open and close slots
            - Delete booking records after the date
API:        REST
            GET  /slots
            POST /slots/{id}/book
            POST /slots
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 209

**Intent:**
buddhist temple app for dharma talk recordings and meditation timer with bell

**Spec:**
```
Type:       Mobile application with backend (Buddhist temple)
Auth:       Admin login for uploading talks
Data model: DharmaTalk(id, title, teacher, recorded_on, audio_url, duration_min)
            Schedule(id, title, weekday, time)
            SitSession(id, device_id, minutes, completed_at)
Features:   - Stream and download dharma talks
            - Run a meditation timer with interval bells
            - Show the weekly sitting schedule
            - Track total minutes meditated
API:        REST
            GET  /talks
            POST /talks
            GET  /schedule
Storage:    PostgreSQL, S3
Tech stack: Flutter, Node.js
```

---

## Example 210

**Intent:**
bible study group app - weekly reading plan, discussion questions, prayer requests

**Spec:**
```
Type:       Mobile application with backend (bible study groups)
Auth:       Email + password, group invite link
Data model: StudyGroup(id, name, leader_id)
            ReadingPlan(id, group_id -> StudyGroup, week, passage, questions)
            PrayerRequest(id, group_id -> StudyGroup, author_id, text, answered)
Features:   - Show this week's passage and questions
            - Post and pray for prayer requests in the group
            - Mark prayer requests as answered
            - Remind members before the meeting
API:        REST
            GET  /groups/{id}/plan
            POST /groups/{id}/prayer-requests
            PATCH /prayer-requests/{id}
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 211

**Intent:**
condo board needs app for owners: announcements, documents, maintenance fund balance

**Spec:**
```
Type:       Mobile application with backend (condo association portal)
Auth:       Email + password, unit ownership verified
Data model: Owner(id, name, unit, share_pct)
            Document(id, title, category, file_url, published_at)
            FundEntry(id, fund, amount, description, date)
Features:   - Post board announcements with push notifications
            - Share bylaws, minutes and budgets as documents
            - Show reserve fund balance and expenses
            - Collect owner feedback through polls
API:        REST
            GET  /documents
            GET  /funds/summary
            POST /announcements
Storage:    PostgreSQL, S3
Tech stack: Flutter, Django REST Framework
```

---

## Example 212

**Intent:**
noise complaint in apartment building, anonymous to neighbour but manager sees

**Spec:**
```
Type:       Mobile application with backend (noise complaints)
Auth:       Email + password per resident
Data model: Complaint(id, reporter_unit, target_unit, kind, occurred_at, description, status)
            Warning(id, target_unit, complaint_ids, sent_at)
Features:   - File a complaint against a unit with time and description
            - Hide the reporter's identity from the neighbour
            - Let the manager send a warning after repeated complaints
            - Show complaint history per unit to the manager
API:        REST
            POST /complaints
            GET  /units/{id}/complaints
            POST /warnings
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 213

**Intent:**
bike storage room in building, lockers assigned by app and door opens with phone

**Spec:**
```
Type:       Mobile application with backend (bike storage access)
Auth:       Resident email + password
Data model: BikeLocker(id, number, size, resident_id)
            AccessEvent(id, resident_id, door, at)
            Waitlist(id, resident_id, joined_at)
Features:   - Assign lockers and keep a waitlist
            - Unlock the storage room door with Bluetooth
            - Log every entry
            - Release lockers unused for 60 days
API:        REST
            POST /lockers/{id}/assign
            POST /door/unlock
            GET  /access-log
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, Go, BLE smart lock
```

---

## Example 214

**Intent:**
intercom on phone, visitor rings at building door and I see video and open

**Spec:**
```
Type:       Mobile application with backend (smart building intercom)
Auth:       Resident email + password
Data model: Building(id, address)
            Apartment(id, building_id -> Building, number)
            Resident(id, apartment_id -> Apartment, name, device_tokens)
            CallLog(id, apartment_id -> Apartment, started_at, answered, door_opened)
Features:   - Ring residents' phones when a visitor presses the panel
            - Show live video from the door panel
            - Open the door remotely
            - Keep a call log with snapshots
API:        REST + WebRTC signalling
            POST /calls
            POST /calls/{id}/open
            GET  /call-logs
Storage:    PostgreSQL, S3 (snapshots)
Tech stack: Flutter, Node.js, WebRTC, VoIP push
```

---

## Example 215

**Intent:**
retirement village residents app: activities, dinner menu, call for help

**Spec:**
```
Type:       Mobile application with backend (retirement village)
Auth:       Resident PIN on large-text app; staff login
Data model: Resident(id, name, cottage)
            Activity(id, title, starts_at, place)
            ActivitySignup(id, activity_id -> Activity, resident_id -> Resident)
            HelpCall(id, resident_id -> Resident, kind, created_at, answered_at)
Features:   - Show today's activities and dining menu in large text
            - Sign up for outings
            - Send a help call to staff with one button
            - Let family view the activity calendar
API:        REST
            GET  /activities
            POST /activities/{id}/signup
            POST /help-calls
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 216

**Intent:**
student hall laundry card top-up and machine status

**Spec:**
```
Type:       Mobile application with backend (student hall laundry)
Auth:       University SSO
Data model: LaundryMachine(id, hall, kind, status)
            Wallet(student_id, balance)
            WashPayment(id, machine_id -> LaundryMachine, student_id, amount, at)
Features:   - Show free machines per hall
            - Pay for a cycle by scanning the machine QR code
            - Top up the laundry wallet
            - Report a broken machine
API:        REST
            GET  /machines?hall={h}
            POST /machines/{id}/pay
            POST /wallet/topup
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI
```

---

## Example 217

**Intent:**
moped sharing city, electric mopeds, helmet in box, check ID licence

**Spec:**
```
Type:       Mobile application with backend (e-moped sharing)
Auth:       Email + password with driving licence verification
Data model: Moped(id, plate, lat, lng, battery_pct, status)
            Rider(id, name, licence_verified, licence_expires)
            MopedRide(id, moped_id -> Moped, rider_id -> Rider, started_at, ended_at, km, cost)
Features:   - Verify licence with a selfie and document scan
            - Reserve a moped for 15 minutes free
            - Unlock the helmet box and start the ride
            - Charge per minute and show the route after
API:        REST
            POST /riders/verify
            POST /mopeds/{id}/reserve
            POST /rides
            POST /rides/{id}/end
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin, Swift, Go, Onfido, Stripe
```

---

## Example 218

**Intent:**
park and ride lot spaces free + next shuttle

**Spec:**
```
Type:       Mobile application with backend (park and ride)
Data model: Lot(id, name, total_spaces, occupied, updated_at)
            ShuttleDeparture(id, lot_id -> Lot, departs_at)
Features:   - Show free spaces per lot from gate counters
            - Show next shuttle departures
            - Predict when a lot will be full
            - Notify commuters when their lot is nearly full
API:        REST
            GET  /lots
            GET  /lots/{id}/departures
            POST /lots/{id}/count
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Node.js
```

---

## Example 219

**Intent:**
airport parking prebook cheaper, shuttle to terminal

**Spec:**
```
Type:       Mobile application with backend (airport parking)
Auth:       Email + password
Data model: ParkingProduct(id, name, distance_to_terminal, daily_price)
            ParkingBooking(id, product_id -> ParkingProduct, plate, drop_off_at, pick_up_at, flight_number, total)
Features:   - Compare long-stay and short-stay prices by dates
            - Book and get a barrier code from the plate
            - Track the return flight to time the shuttle
            - Extend the booking if the flight is delayed
API:        REST
            GET  /quotes?from={d}&to={d}
            POST /bookings
            PATCH /bookings/{id}/extend
Storage:    PostgreSQL
Tech stack: React Native, C#, ASP.NET Core, AviationStack API
```

---

## Example 220

**Intent:**
truck drivers find safe overnight parking with free spots

**Spec:**
```
Type:       Mobile application with backend (truck parking)
Auth:       Email + password
Data model: TruckStop(id, name, lat, lng, total_spots, amenities)
            SpotReport(id, stop_id -> TruckStop, free_spots, reporter_id, at)
            Reservation(id, stop_id -> TruckStop, driver_id, night_of, price)
Features:   - Find truck stops along a route
            - Show free spot counts reported by drivers
            - Reserve a paid spot at partner stops
            - Show showers, food and security amenities
API:        REST
            GET  /stops/along-route
            POST /stops/{id}/reports
            POST /reservations
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin, Swift, Python, FastAPI
```

---

## Example 221

**Intent:**
bike mechanic comes to fix your bike at home

**Spec:**
```
Type:       Mobile application with backend (mobile bike repair)
Auth:       Email + password
Data model: Bike(id, owner_id, type, brand, photo_url)
            ServiceJob(id, bike_id -> Bike, service, address, slot, mechanic_id, price, status)
Features:   - Pick a service like puncture repair or full tune-up
            - Book a slot at home or work
            - Add parts approved by the customer during the job
            - Pay in the app
API:        REST
            POST /jobs
            POST /jobs/{id}/parts
            POST /jobs/{id}/complete
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Stripe
```

---

## Example 222

**Intent:**
want an app in Swift for iPhone where my bakery customers pick up leftover bread at 6pm for cheap, backend with Vapor

**Spec:**
```
Type:       Mobile application with backend (end-of-day bread offers)
Auth:       Sign in with Apple
Data model: Offer(id, date, description, quantity, price)
            OfferReservation(id, offer_id -> Offer, customer_id, code, collected)
Features:   - Post the evening's leftover bread at 4pm
            - Reserve and pay for a bag
            - Show a pickup code at the counter
            - Notify regulars when offers go live
API:        REST
            GET  /offers/today
            POST /offers/{id}/reserve
            POST /reservations/{id}/collect
Storage:    PostgreSQL
Tech stack: Swift, SwiftUI, Vapor, Apple Pay
```

---

## Example 223

**Intent:**
my shop is ice cream, I want customers queue online in summer cause line is huge, number shows on TV

**Spec:**
```
Type:       Mobile application with backend (shop virtual queue)
Auth:       No login; tickets tied to device
Data model: QueueTicket(id, number, device_id, status, created_at, called_at)
            ShopStatus(open, avg_serve_seconds)
Features:   - Take a queue number from the app when near the shop
            - Show numbers being served on a TV screen
            - Notify customers when 3 numbers are left
            - Skip customers who do not show within 2 minutes
API:        REST + WebSocket
            POST /tickets
            POST /tickets/next
            WS   /queue/live
Storage:    Redis
Tech stack: React Native, Node.js, Socket.IO
```

---

## Example 224

**Intent:**
nail salon booking, choose technician + design photos inspiration

**Spec:**
```
Type:       Mobile application with backend (nail salon)
Auth:       Phone number + OTP
Data model: Technician(id, name, specialties)
            NailService(id, name, duration_min, price)
            NailAppointment(id, technician_id -> Technician, service_id -> NailService, client_id, starts_at, inspiration_url)
Features:   - Book a service with a chosen technician
            - Upload an inspiration photo for the design
            - Show a gallery of each technician's work
            - Send reminders and allow rescheduling
API:        REST
            GET  /technicians/{id}/slots
            POST /appointments
            POST /appointments/{id}/inspiration
Storage:    PostgreSQL, S3
Tech stack: Flutter, Firebase
```

---

## Example 225

**Intent:**
walk-in clinic join queue online then come when nearly ur turn

**Spec:**
```
Type:       Mobile application with backend (walk-in clinic queue)
Auth:       Phone number + SMS code
Data model: Clinic(id, name, address, open)
            QueuePatient(id, clinic_id -> Clinic, name, phone, reason, position, status, joined_at)
Features:   - Join a clinic queue remotely with reason for visit
            - Show estimated wait time
            - Text the patient when 20 minutes from their turn
            - Let reception reorder for urgent cases
API:        REST
            POST /clinics/{id}/queue
            GET  /queue/{id}
            PATCH /queue/{id}
Storage:    PostgreSQL
Tech stack: React Native, Django, Twilio
```

---
## Example 226

**Intent:**
home insurance claim after storm, upload video of damage, adjuster schedules visit

**Spec:**
```
Type:       Mobile application with backend (home insurance claims)
Auth:       Policy number + email verification
Data model: Policy(id, number, holder_id, property_address)
            HomeClaim(id, policy_id -> Policy, peril, occurred_on, description, status)
            ClaimMedia(id, claim_id -> HomeClaim, kind, url, room)
            AdjusterVisit(id, claim_id -> HomeClaim, adjuster_id, scheduled_at)
Features:   - File a claim by peril type (storm, flood, fire)
            - Upload photos and short videos by room
            - Book an adjuster visit from open slots
            - Show claim status and payment
API:        REST
            POST /claims
            POST /claims/{id}/media
            POST /claims/{id}/visits
Storage:    PostgreSQL, S3
Tech stack: React Native, Java, Spring Boot
```

---

## Example 227

**Intent:**
pet insurance claim photo of vet invoice and get paid

**Spec:**
```
Type:       Mobile application with backend (pet insurance claims)
Auth:       Email + password
Data model: PetPolicy(id, holder_id, pet_name, plan, deductible_left)
            VetClaim(id, policy_id -> PetPolicy, invoice_url, vet_name, amount, condition, status)
            ClaimPayout(id, claim_id -> VetClaim, amount, paid_at)
Features:   - Photograph a vet invoice and extract amounts with OCR
            - Submit the claim with condition details
            - Apply deductible and coverage rules
            - Pay out by bank transfer
API:        REST
            POST /claims
            GET  /claims/{id}
Storage:    PostgreSQL, S3
Tech stack: Flutter, AWS Textract, Python, FastAPI
```

---

## Example 228

**Intent:**
travel insurance app: buy cover for trip, emergency number, claim lost luggage

**Spec:**
```
Type:       Mobile application with backend (travel insurance)
Auth:       Email + password
Data model: TripPolicy(id, holder_id, destination, start_date, end_date, cover_level, premium)
            TravelClaim(id, policy_id -> TripPolicy, kind, description, receipts, status)
Features:   - Quote and buy cover for a trip
            - Show the policy card and 24/7 assistance number offline
            - Submit lost luggage or medical claims with receipts
            - Track claim status
API:        REST
            POST /quotes
            POST /policies
            POST /policies/{id}/claims
Storage:    PostgreSQL, S3
Tech stack: React Native, Node.js, Stripe
```

---

## Example 229

**Intent:**
renters see apartments and book viewing, agent sees calendar

**Spec:**
```
Type:       Mobile application with backend (rental viewings)
Auth:       Email + password
Data model: RentalListing(id, agent_id, address, rent, bedrooms, available_from)
            ViewingSlot(id, listing_id -> RentalListing, starts_at, max_groups)
            Viewing(id, slot_id -> ViewingSlot, renter_id, status)
Features:   - Browse rentals with filters
            - Book a viewing slot
            - Let agents run group viewings
            - Apply for the rental after viewing
API:        REST
            GET  /listings
            POST /slots/{id}/viewings
            POST /listings/{id}/applications
Storage:    PostgreSQL
Tech stack: Flutter, Laravel
```

---

## Example 230

**Intent:**
open house sign in sheet on ipad then follow up emails to visitors

**Spec:**
```
Type:       Mobile application with backend (open house sign-in)
Auth:       Agent email + password
Data model: OpenHouse(id, agent_id, address, date)
            Visitor(id, open_house_id -> OpenHouse, name, email, phone, has_agent, interest)
Features:   - Show a kiosk sign-in form on a tablet
            - Ask if the visitor already has an agent
            - Send an automatic thank-you email with the listing
            - Export visitors to the agent's CRM
API:        REST
            POST /open-houses
            POST /open-houses/{id}/visitors
            GET  /open-houses/{id}/export
Storage:    PostgreSQL
Tech stack: React Native (tablet), Node.js, SendGrid
```

---

## Example 231

**Intent:**
self tour homes for sale, buyer unlocks smart lock with app after ID check

**Spec:**
```
Type:       Mobile application with backend (self-guided home tours)
Auth:       Email + password with ID and selfie verification
Data model: Home(id, address, lock_device_id, price)
            SelfTour(id, home_id -> Home, buyer_id, starts_at, ends_at, status)
            LockEvent(id, tour_id -> SelfTour, action, at)
Features:   - Verify buyer identity before the first tour
            - Book a 30-minute self tour
            - Unlock the smart lock only during the booked window
            - Alert the agent if the door is left unlocked
API:        REST
            POST /tours
            POST /tours/{id}/unlock
            POST /tours/{id}/lock
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, Node.js, August/Yale lock API, Persona
```

---

## Example 232

**Intent:**
students hire tutors on campus who took the same course, pay by session

**Spec:**
```
Type:       Mobile application with backend (peer tutoring)
Auth:       University email login
Data model: TutorProfile(id, student_id, courses, grade_received, hourly_rate)
            TutoringSession(id, tutor_id -> TutorProfile, learner_id, course, starts_at, location, status)
Features:   - Find peer tutors who passed a course with a good grade
            - Book a session at a library room or online
            - Pay through the app
            - Rate the tutor
API:        REST
            GET  /tutors?course={c}
            POST /sessions
            POST /sessions/{id}/rate
Storage:    PostgreSQL
Tech stack: React Native, Python, Django, Stripe Connect
```

---

## Example 233

**Intent:**
hey so i run a small after school coding club for kids and parents keep asking what the kids made. could there be an app where kids upload their projects (scratch or python) and parents can see them and leave a heart, and i can post the weekly homework

**Spec:**
```
Type:       Mobile application with backend (kids coding club)
Auth:       Teacher email + password; parents linked to child by code
Data model: Kid(id, name, parent_id)
            Project(id, kid_id -> Kid, title, kind, file_url, thumbnail_url, created_at)
            Heart(id, project_id -> Project, parent_id)
            Homework(id, title, description, due_on)
Features:   - Let kids upload Scratch or Python projects with a screenshot
            - Show parents their child's project gallery
            - Let parents leave hearts on projects
            - Post weekly homework to all families
API:        REST
            POST /projects
            GET  /kids/{id}/projects
            POST /projects/{id}/hearts
            POST /homework
Storage:    PostgreSQL, S3
Tech stack: Flutter, Node.js, Express
```

---

## Example 234

**Intent:**
test centre booking for IELTS-like exams, upload passport, pick seat date

**Spec:**
```
Type:       Mobile application with backend (exam centre booking)
Auth:       Email + password
Data model: ExamSession(id, centre, date, kind, seats)
            Candidate(id, name, passport_number, passport_scan_url)
            ExamBooking(id, session_id -> ExamSession, candidate_id -> Candidate, paid, status)
            ExamResult(id, booking_id -> ExamBooking, scores_json, released_at)
Features:   - Pick an exam session by city and date
            - Upload passport for identity check
            - Pay the exam fee
            - Release results to the app on results day
API:        REST
            GET  /sessions
            POST /bookings
            GET  /bookings/{id}/result
Storage:    PostgreSQL, S3
Tech stack: React Native, Java, Spring Boot
```

---

## Example 235

**Intent:**
public library app - card barcode, holds, events

**Spec:**
```
Type:       Mobile application with backend (public library)
Auth:       Library card number + PIN
Data model: Patron(id, card_number, name)
            Hold(id, patron_id -> Patron, title_id, position, ready_on)
            LibraryEvent(id, branch, title, starts_at, audience)
Features:   - Show a scannable digital library card
            - Search the catalogue and place holds
            - Notify when a hold is ready for pickup
            - List events at each branch
API:        REST
            GET  /catalogue?q={text}
            POST /holds
            GET  /events
Storage:    PostgreSQL (synced from ILS via SIP2)
Tech stack: Flutter, Node.js
```

---

## Example 236

**Intent:**
office building visitors pre registered by employee, get QR, reception prints badge

**Spec:**
```
Type:       Mobile application with backend (office visitor management)
Auth:       Employee SSO
Data model: VisitorInvite(id, host_id, visitor_name, visitor_email, visit_date, qr_token)
            VisitLog(id, invite_id -> VisitorInvite, arrived_at, left_at, badge_number)
Features:   - Pre-register a visitor and email them a QR code
            - Scan the QR at reception and print a badge
            - Notify the host when the visitor arrives
            - Show a live list of people in the building for evacuation
API:        REST
            POST /invites
            POST /checkin
            GET  /onsite
Storage:    PostgreSQL
Tech stack: React Native, C#, ASP.NET Core, Microsoft Graph
```

---

## Example 237

**Intent:**
meeting room booking with tablet outside each room

**Spec:**
```
Type:       Mobile application with backend (meeting room booking)
Auth:       Company SSO
Data model: MeetingRoom(id, name, floor, capacity, equipment)
            RoomBooking(id, room_id -> MeetingRoom, organiser_id, title, starts_at, ends_at, checked_in)
Features:   - Book rooms from the phone
            - Show room status on a door tablet
            - Release rooms not checked into within 10 minutes
            - Sync with Google Calendar
API:        REST
            GET  /rooms/free?at={t}
            POST /bookings
            POST /bookings/{id}/checkin
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Google Calendar API
```

---

## Example 238

**Intent:**
company shuttle bus seats reservation for employees

**Spec:**
```
Type:       Mobile application with backend (employee shuttle)
Auth:       Company SSO
Data model: ShuttleRun(id, route, departs_at, seats)
            SeatBooking(id, run_id -> ShuttleRun, employee_id, boarded)
Features:   - Book a seat on morning and evening runs
            - Show live bus location
            - Board by scanning a QR code
            - Report ridership per route
API:        REST
            GET  /runs?date={d}
            POST /runs/{id}/book
            POST /board
Storage:    PostgreSQL
Tech stack: React Native, Go
```

---

## Example 239

**Intent:**
factory workers report safety hazard with photo anonymously

**Spec:**
```
Type:       Mobile application with backend (safety hazard reporting)
Auth:       Anonymous reports allowed; supervisor login
Data model: HazardReport(id, area, kind, description, photo_url, anonymous, status, created_at)
            CorrectiveAction(id, report_id -> HazardReport, owner, due_on, done_on)
Features:   - Report a hazard with photo and area
            - Choose to stay anonymous
            - Assign corrective actions with due dates
            - Show reporters when the hazard is fixed
API:        REST
            POST /reports
            POST /reports/{id}/actions
            GET  /reports/{id}
Storage:    PostgreSQL, S3
Tech stack: Flutter, Python, Django
```

---

## Example 240

**Intent:**
Construction company: workers sign in to site with face pic, induction done check

**Spec:**
```
Type:       Mobile application with backend (site sign-in)
Auth:       Phone number + OTP
Data model: Worker(id, name, company, induction_completed_on, cert_expiry)
            Site(id, name, lat, lng, radius_m)
            SiteAttendance(id, worker_id -> Worker, site_id -> Site, signed_in_at, signed_out_at, selfie_url)
Features:   - Sign in only within the site geofence
            - Take a selfie at sign-in
            - Block sign-in without a completed induction
            - Show the site manager who is on site
API:        REST
            POST /attendance/sign-in
            POST /attendance/{id}/sign-out
            GET  /sites/{id}/onsite
Storage:    PostgreSQL, S3
Tech stack: React Native, Laravel
```

---

## Example 241

**Intent:**
farmers sell milk to cooperative, app shows liters and payment each delivery

**Spec:**
```
Type:       Mobile application with backend (dairy cooperative)
Auth:       Phone number + OTP
Data model: Farmer(id, name, phone, village)
            MilkDelivery(id, farmer_id -> Farmer, litres, fat_pct, price_per_litre, delivered_at)
            Payment(id, farmer_id -> Farmer, period, amount, paid_at)
Features:   - Record each delivery with litres and fat test
            - Calculate price from fat content
            - Show farmers their delivery history
            - Pay fortnightly through mobile money
API:        REST
            POST /deliveries
            GET  /farmers/{id}/deliveries
            POST /payments
Storage:    PostgreSQL
Tech stack: Kotlin (Android), Python, Django, SMS gateway
```

---

## Example 242

**Intent:**
hunting and fishing licence buy on phone and show to warden

**Spec:**
```
Type:       Mobile application with backend (hunting and fishing licences)
Auth:       Email + password with date of birth check
Data model: LicenceType(id, name, season, price)
            Licence(id, holder_id, type_id -> LicenceType, valid_from, valid_to, qr_token)
            HarvestReport(id, licence_id -> Licence, species, count, area, reported_at)
Features:   - Buy licences and tags
            - Show the licence offline with a signed QR code
            - Report harvests by species
            - Let wardens verify licences by scanning
API:        REST
            POST /licences
            POST /licences/{id}/harvests
            GET  /licences/verify/{token}
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, Java, Spring Boot
```

---

## Example 243

**Intent:**
taxi rank in small town has no app, drivers want simple booking where passengers call by app and drivers in rank take turn

**Spec:**
```
Type:       Mobile application with backend (taxi rank dispatch)
Auth:       Phone number + OTP for passengers and drivers
Data model: Driver(id, name, plate, rank_position, status)
            TaxiRequest(id, passenger_phone, pickup, destination, status, driver_id -> Driver)
Features:   - Request a taxi with pickup address
            - Offer the request to the driver first in the rank queue
            - Move drivers to the back of the queue after a job
            - Show the passenger the driver's plate and arrival
API:        REST + WebSocket
            POST /requests
            POST /requests/{id}/accept
            WS   /drivers/me
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Node.js
```

---

## Example 244

**Intent:**
moving to new city, app where i book truck rental for the day and return in other city

**Spec:**
```
Type:       Mobile application with backend (moving truck rental)
Auth:       Email + password with licence check
Data model: TruckClass(id, name, size_m3, daily_rate, per_km_rate)
            Depot(id, city, address)
            TruckRental(id, class_id -> TruckClass, pickup_depot_id -> Depot, return_depot_id -> Depot, pickup_at, return_at, total)
Features:   - Pick truck size by apartment size
            - Book one-way rentals between depots
            - Add extras like dollies and blankets
            - Record odometer photos at pickup and return
API:        REST
            GET  /quotes
            POST /rentals
            POST /rentals/{id}/odometer
Storage:    PostgreSQL
Tech stack: React Native, Java, Spring Boot
```

---

## Example 245

**Intent:**
self storage units rent online and open gate with app

**Spec:**
```
Type:       Mobile application with backend (self storage)
Auth:       Email + password with ID check
Data model: StorageUnit(id, size_m2, floor, monthly_price, status)
            UnitRental(id, unit_id -> StorageUnit, customer_id, start_date, end_date)
            GateAccess(id, rental_id -> UnitRental, at)
Features:   - Show available unit sizes and prices
            - Rent a unit and pay monthly
            - Open the gate with Bluetooth from the app
            - Share temporary access with a friend
API:        REST
            GET  /units/available
            POST /rentals
            POST /gate/open
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe Billing, BLE
```

---

## Example 246

**Intent:**
lockers at train station rent for few hours with phone code

**Spec:**
```
Type:       Mobile application with backend (luggage lockers)
Auth:       Email or Apple/Google sign-in
Data model: LockerBank(id, station, lat, lng)
            Locker(id, bank_id -> LockerBank, size, status)
            LockerRental(id, locker_id -> Locker, user_id, starts_at, ends_at, pin)
Features:   - Show free lockers by size at each station
            - Rent a locker and receive an opening code
            - Charge per hour with a daily cap
            - Extend rental from the phone
API:        REST
            GET  /banks/{id}/lockers
            POST /rentals
            POST /rentals/{id}/extend
Storage:    PostgreSQL
Tech stack: React Native, Go, Stripe
```

---

## Example 247

**Intent:**
i need app like this: people leave luggage in local cafes while sightseeing, cafe gets paid

**Spec:**
```
Type:       Mobile application with backend (luggage storage network)
Auth:       Email + password; partner shops have business accounts
Data model: PartnerShop(id, name, lat, lng, capacity, opening_hours)
            BagBooking(id, shop_id -> PartnerShop, traveller_id, bags, drop_at, pick_at, seal_code)
Features:   - Find partner shops near the user
            - Book storage for a number of bags
            - Seal bags with numbered tags recorded in the app
            - Pay partners per bag per day
API:        REST
            GET  /shops/nearby
            POST /bookings
            POST /bookings/{id}/checkin
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Node.js, Stripe Connect
```

---

## Example 248

**Intent:**
city pass for tourists — one QR gets into 20 museums and bus

**Spec:**
```
Type:       Mobile application with backend (city tourist pass)
Auth:       Email + password
Data model: CityPass(id, buyer_id, duration_hours, activated_at, qr_token)
            Attraction(id, name, address, category)
            Entry(id, pass_id -> CityPass, attraction_id -> Attraction, scanned_at)
Features:   - Buy 24, 48 or 72-hour passes
            - Activate at the first scan
            - Let attractions scan the pass once each
            - Show attractions and opening hours on a map
API:        REST
            POST /passes
            POST /attractions/{id}/scan
            GET  /attractions
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI
```

---

## Example 249

**Intent:**
wine tasting tour app to book winery visits and log wines I liked

**Spec:**
```
Type:       Mobile application with backend (winery tours)
Auth:       Email + password, 18+ check
Data model: Winery(id, name, region, lat, lng)
            TastingSlot(id, winery_id -> Winery, starts_at, capacity, price)
            TastingBooking(id, slot_id -> TastingSlot, user_id, guests)
            WineNote(id, user_id, winery_id -> Winery, wine, rating, notes)
Features:   - Book tasting slots at several wineries in one day
            - Warn if travel time between bookings is too short
            - Save tasting notes and ratings
            - Order bottles to be shipped home
API:        REST
            GET  /wineries
            POST /bookings
            POST /notes
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Stripe
```

---

## Example 250

**Intent:**
botanical garden app, point camera at plant to identify and read about it

**Spec:**
```
Type:       Mobile application with backend (botanical garden guide)
Data model: Plant(id, latin_name, common_name, bed_id, description, image_url)
            Bed(id, name, lat, lng)
            Season(id, plant_id -> Plant, blooms_from, blooms_to)
Features:   - Identify a plant from a photo with an image classifier
            - Show the plant's information and garden location
            - List what is in bloom this week
            - Show a garden map
API:        REST
            POST /identify
            GET  /plants/{id}
            GET  /blooming
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI, PyTorch (image classifier)
```

---

## Example 251

**Intent:**
self guided cemetery tour w famous graves map

**Spec:**
```
Type:       Mobile application with backend (cemetery heritage tour)
Data model: Grave(id, name, born, died, lat, lng, biography, photo_url)
            TourRoute(id, name, grave_ids, duration_min)
Features:   - Show notable graves on a map
            - Follow themed walking routes
            - Read short biographies at each grave
            - Search for any burial by name
API:        REST
            GET  /graves?q={name}
            GET  /routes
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Node.js, Leaflet
```

---

## Example 252

**Intent:**
whale watching boat tours booking and sightings log

**Spec:**
```
Type:       Mobile application with backend (whale watching)
Auth:       Email + password
Data model: BoatTrip(id, departs_at, capacity, price)
            TripBooking(id, trip_id -> BoatTrip, customer_id, guests)
            WhaleSighting(id, trip_id -> BoatTrip, species, count, lat, lng)
Features:   - Book a tour seat
            - Offer free rebooking when no whales are seen
            - Cancel trips for bad sea conditions and notify guests
            - Show sightings from recent trips
API:        REST
            GET  /trips
            POST /bookings
            POST /trips/{id}/sightings
Storage:    PostgreSQL
Tech stack: React Native, Django
```

---
## Example 253

**Intent:**
power outage report app for our electric company, see map of outages and when fixed

**Spec:**
```
Type:       Mobile application with backend (power outage reporting)
Auth:       Account number + email
Data model: OutageReport(id, account_no, lat, lng, reported_at)
            Outage(id, area_geojson, cause, customers_affected, estimated_restore_at, status)
Features:   - Report an outage at the customer's address
            - Group reports into outages on a map
            - Show estimated restoration time
            - Push updates when power is restored
API:        REST
            POST /reports
            GET  /outages
            PATCH /outages/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Java, Spring Boot
```

---

## Example 254

**Intent:**
order 20 litre water bottles delivered to office, return empties

**Spec:**
```
Type:       Mobile application with backend (water bottle delivery)
Auth:       Phone number + OTP
Data model: Customer(id, name, address, bottle_deposit_count)
            WaterOrder(id, customer_id -> Customer, full_bottles, empties_returned, date, status)
            Subscription(id, customer_id -> Customer, bottles, every_days)
Features:   - Order full bottles and schedule delivery
            - Track deposits for bottles held by the customer
            - Set a recurring delivery every N days
            - Plan delivery routes for drivers
API:        REST
            POST /orders
            POST /subscriptions
            GET  /routes?date={d}
Storage:    PostgreSQL
Tech stack: React Native, Laravel
```

---

## Example 255

**Intent:**
gas cylinder refill order, in my country people call shop, want app instead, payment cash or mobile money

**Spec:**
```
Type:       Mobile application with backend (LPG cylinder refill)
Auth:       Phone number + OTP
Data model: Customer(id, phone, address, lat, lng)
            CylinderOrder(id, customer_id -> Customer, size_kg, brand, payment_method, status)
            Dealer(id, name, lat, lng, stock_json)
Features:   - Order a refill by cylinder size and brand
            - Route the order to the nearest dealer with stock
            - Pay cash on delivery or by mobile money
            - Show delivery status
API:        REST
            POST /orders
            PATCH /orders/{id}/status
            GET  /dealers/nearby
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, MTN MoMo API
```

---

## Example 256

**Intent:**
book bulky trash pickup like old sofa from city

**Spec:**
```
Type:       Mobile application with backend (bulky waste pickup)
Auth:       Email + password, address check
Data model: BulkyPickup(id, resident_id, address, items, pickup_date, status)
            ItemType(id, name, fee)
Features:   - Choose items from a list with fees
            - Pick an available collection date for the area
            - Limit free pickups to 2 per year
            - Send a reminder with what to put out
API:        REST
            GET  /item-types
            GET  /dates?address={a}
            POST /pickups
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI
```

---

## Example 257

**Intent:**
makerspace members need app to unlock laser cutter only if trained

**Spec:**
```
Type:       Mobile application with backend (makerspace tool access)
Auth:       Member email + password
Data model: Tool(id, name, controller_id, requires_training)
            Training(id, member_id, tool_id -> Tool, signed_off_by, at)
            ToolSession(id, tool_id -> Tool, member_id, started_at, ended_at)
Features:   - Unlock a tool's power relay from the app if trained
            - Book tools by the hour
            - Log usage minutes for billing
            - Let trainers sign off members
API:        REST
            POST /tools/{id}/unlock
            POST /trainings
            POST /bookings
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, MQTT, ESP32 relays
```

---

## Example 258

**Intent:**
recording studio booking by hour with engineer option

**Spec:**
```
Type:       Mobile application with backend (recording studio booking)
Auth:       Email + password
Data model: Studio(id, name, hourly_rate)
            Engineer(id, name, hourly_rate)
            Session(id, studio_id -> Studio, engineer_id -> Engineer, client_id, starts_at, hours, total)
Features:   - Book studio hours with or without an engineer
            - Take a 50% deposit
            - Share session files after the booking
            - Show the studio calendar
API:        REST
            GET  /studios/{id}/calendar
            POST /sessions
            GET  /sessions/{id}/files
Storage:    PostgreSQL, S3
Tech stack: React Native, Node.js, Stripe
```

---

## Example 259

**Intent:**
dance studio - kids classes, parents pay monthly, recital costume orders

**Spec:**
```
Type:       Mobile application with backend (dance studio)
Auth:       Parent email + password
Data model: Dancer(id, parent_id, name, age)
            DanceClass(id, style, level, weekday, time)
            Enrolment(id, dancer_id -> Dancer, class_id -> DanceClass)
            CostumeOrder(id, dancer_id -> Dancer, costume, size, paid)
Features:   - Enrol children in classes
            - Charge monthly tuition automatically
            - Order and pay for recital costumes by size
            - Post studio announcements
API:        REST
            POST /enrolments
            POST /costume-orders
            GET  /announcements
Storage:    PostgreSQL
Tech stack: Flutter, Django, Stripe Billing
```

---

## Example 260

**Intent:**
martial arts dojo track belts, attendance, grading eligibility

**Spec:**
```
Type:       Mobile application with backend (martial arts dojo)
Auth:       Email + password
Data model: Student(id, name, belt, belt_since)
            ClassAttendance(id, student_id -> Student, class_date)
            Grading(id, date, student_ids, results_json)
Features:   - Check in to class with a QR code
            - Count classes since the last belt
            - Show students when they are eligible for grading
            - Record grading results and new belts
API:        REST
            POST /checkin
            GET  /students/{id}/progress
            POST /gradings
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 261

**Intent:**
sauna booking public sauna by the lake, 1.5h slots

**Spec:**
```
Type:       Mobile application with backend (sauna booking)
Auth:       Email or phone login
Data model: SaunaSlot(id, starts_at, capacity, private)
            SaunaBooking(id, slot_id -> SaunaSlot, user_id, people, door_code)
Features:   - Book shared or private 90-minute slots
            - Send a door code valid for the slot
            - Buy 10-visit cards
            - Show water temperature of the lake
API:        REST
            GET  /slots?date={d}
            POST /bookings
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 262

**Intent:**
mountain hut beds booking for hikers, multi day route

**Spec:**
```
Type:       Mobile application with backend (mountain hut booking)
Auth:       Email + password
Data model: Hut(id, name, altitude_m, beds, lat, lng)
            HutNight(id, hut_id -> Hut, date, beds_free)
            RouteBooking(id, user_id, nights_json, people, status)
Features:   - Plan a multi-day route with one hut per night
            - Book beds across several huts in one go
            - Show half-board meal options
            - Cancel nights if weather closes a pass
API:        REST
            GET  /huts
            GET  /huts/{id}/availability
            POST /route-bookings
Storage:    PostgreSQL
Tech stack: React Native, Java, Spring Boot
```

---

## Example 263

**Intent:**
photo studio rental hourly with lights and backdrops add ons

**Spec:**
```
Type:       Mobile application with backend (photo studio rental)
Auth:       Email + password
Data model: StudioSpace(id, name, size_m2, hourly_rate)
            AddOn(id, name, price)
            StudioBooking(id, space_id -> StudioSpace, user_id, starts_at, hours, add_on_ids, total)
Features:   - Book studio spaces by the hour
            - Add lights, backdrops and props
            - Pay and receive the door code
            - Charge for overtime when checkout is late
API:        REST
            GET  /spaces/{id}/availability
            POST /bookings
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Stripe
```

---

## Example 264

**Intent:**
ok so our neighbourhood association has like 300 houses and we use a facebook group but it's chaos. we need an app where only verified residents join, there's a section for safety alerts, one for lost and found, one for events, and the committee can do polls. nothing fancy

**Spec:**
```
Type:       Mobile application with backend (neighbourhood association)
Auth:       Email + password, address verified by committee
Data model: Resident(id, name, address, verified)
            Post(id, author_id -> Resident, section, title, body, photo_url, created_at)
            Poll(id, question, options, closes_at)
            PollVote(id, poll_id -> Poll, resident_id -> Resident, option)
Features:   - Approve new residents by address
            - Post in safety, lost and found, or events sections
            - Push safety alerts to all residents
            - Run polls with one vote per household
API:        REST
            POST /posts
            GET  /posts?section={s}
            POST /polls/{id}/votes
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 265

**Intent:**
gated community: residents pay security guard fee monthly + report incidents

**Spec:**
```
Type:       Mobile application with backend (estate security levy)
Auth:       Phone number + OTP
Data model: House(id, number, owner_phone)
            LevyPayment(id, house_id -> House, month, amount, paid_at)
            Incident(id, house_id -> House, description, photo_url, status)
Features:   - Pay the monthly security levy
            - Show houses in arrears to the committee
            - Report incidents to the guard house
            - Broadcast messages from the committee
API:        REST
            POST /levies/pay
            GET  /levies/arrears
            POST /incidents
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Paystack
```

---

## Example 266

**Intent:**
parcel lockers in apartment lobby, courier drops, resident gets code

**Spec:**
```
Type:       Mobile application with backend (parcel lockers)
Auth:       Resident email + password; courier app with company login
Data model: ParcelLocker(id, building_id, size, status)
            Delivery(id, locker_id -> ParcelLocker, resident_id, courier, pickup_code, dropped_at, collected_at)
Features:   - Let couriers pick a free locker by size
            - Send the resident a pickup code
            - Remind residents after 48 hours
            - Release the locker after collection
API:        REST
            POST /deliveries
            POST /deliveries/{id}/collect
            GET  /lockers/free
Storage:    PostgreSQL
Tech stack: Kotlin, Go
```

---

## Example 267

**Intent:**
utility bill splitting for roommates with photo of bill

**Spec:**
```
Type:       Mobile application with backend (roommate bill splitting)
Auth:       Email + password
Data model: Household(id, name)
            Roommate(id, household_id -> Household, name, move_in, move_out)
            UtilityBill(id, household_id -> Household, kind, amount, period_start, period_end, photo_url)
            Share(id, bill_id -> UtilityBill, roommate_id -> Roommate, amount, paid)
Features:   - Photograph a bill and extract amount and dates
            - Split by days each roommate lived there in the period
            - Request payment through a payment link
            - Show unpaid shares
API:        REST
            POST /bills
            GET  /households/{id}/shares
            PATCH /shares/{id}/paid
Storage:    PostgreSQL, S3
Tech stack: React Native, Python, FastAPI
```

---

## Example 268

**Intent:**
temple in india wants app for darshan time slot booking cause too much crowd

**Spec:**
```
Type:       Mobile application with backend (temple darshan booking)
Auth:       Phone number + OTP, Aadhaar last 4 digits
Data model: DarshanSlot(id, date, start_time, capacity, kind)
            DarshanTicket(id, slot_id -> DarshanSlot, devotee_name, people, qr_token)
Features:   - Book free or special-entry darshan slots
            - Limit bookings per phone number per day
            - Show the QR ticket at the gate
            - Show live crowd level
API:        REST
            GET  /slots?date={d}
            POST /tickets
            POST /tickets/scan
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Java, Spring Boot, Razorpay
```

---

## Example 269

**Intent:**
wedding hall booking at our church, couples check date and send request

**Spec:**
```
Type:       Mobile application with backend (church venue booking)
Auth:       Email + password
Data model: Venue(id, name, capacity)
            VenueRequest(id, venue_id -> Venue, couple_names, date, guests, status)
            PrepMeeting(id, request_id -> VenueRequest, starts_at)
Features:   - Show free dates for the church and hall
            - Send a booking request with details
            - Let the office approve and take a deposit
            - Schedule marriage prep meetings
API:        REST
            GET  /venues/{id}/dates
            POST /requests
            PATCH /requests/{id}
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails, Stripe
```

---

## Example 270

**Intent:**
funeral home app families pick service options and share livestream link

**Spec:**
```
Type:       Mobile application with backend (funeral planning)
Auth:       Family email + invite from funeral director
Data model: Arrangement(id, deceased_name, director_id, service_date, venue)
            ArrangementItem(id, arrangement_id -> Arrangement, category, choice, price)
            Tribute(id, arrangement_id -> Arrangement, author, message, photo_url)
Features:   - Choose service options like casket, flowers and music
            - Show a running cost total
            - Share the livestream link and service details
            - Collect tribute messages and photos
API:        REST
            POST /arrangements/{id}/items
            GET  /arrangements/{id}
            POST /arrangements/{id}/tributes
Storage:    PostgreSQL, S3
Tech stack: Flutter, Node.js
```

---

## Example 271

**Intent:**
hospice volunteers log visits n hours

**Spec:**
```
Type:       Mobile application with backend (hospice volunteer log)
Auth:       Email + password
Data model: Volunteer(id, name, role)
            VolunteerVisit(id, volunteer_id -> Volunteer, patient_ref, date, minutes, activity)
Features:   - Log visit date, minutes and activity
            - Show total hours this year
            - Remind volunteers of annual training
            - Export hours for the coordinator
API:        REST
            POST /visits
            GET  /volunteers/me/hours
            GET  /reports/hours.csv
Storage:    PostgreSQL
Tech stack: React Native, Firebase
```

---

## Example 272

**Intent:**
emergency shelter beds availability for homeless outreach workers

**Spec:**
```
Type:       Mobile application with backend (shelter bed availability)
Auth:       Outreach worker and shelter staff accounts
Data model: Shelter(id, name, address, population_served)
            BedCount(id, shelter_id -> Shelter, beds_free, updated_at)
            Referral(id, shelter_id -> Shelter, worker_id, client_initials, status)
Features:   - Let shelters update free beds in two taps
            - Show outreach workers free beds by population served
            - Hold a bed with a referral for 1 hour
            - Show the time since the last update
API:        REST
            PUT  /shelters/{id}/beds
            GET  /shelters/available
            POST /referrals
Storage:    PostgreSQL
Tech stack: Flutter, Python, Django
```

---

## Example 273

**Intent:**
cooling centres map during heatwave with open hours

**Spec:**
```
Type:       Mobile application with backend (heatwave cooling centres)
Data model: CoolingCentre(id, name, address, lat, lng, opens_at, closes_at, accessible)
            HeatAlert(id, level, message, starts_on, ends_on)
Features:   - Show open cooling centres on a map
            - Push heat alerts issued by the city
            - Filter by wheelchair access and pets allowed
            - Give directions by walking or transit
API:        REST
            GET  /centres?open_now=true
            GET  /alerts/current
            POST /alerts
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 274

**Intent:**
evacuation app for wildfires, people mark themselves safe and see shelters

**Spec:**
```
Type:       Mobile application with backend (wildfire evacuation)
Auth:       Phone number + SMS code
Data model: EvacZone(id, name, status, polygon)
            Shelter(id, name, lat, lng, capacity, pets_allowed)
            SafeCheck(id, phone, name, status, location_note, at)
Features:   - Show the user's evacuation zone status
            - List open shelters with capacity
            - Mark yourself safe so family can search
            - Push orders when a zone changes to evacuate
API:        REST
            GET  /zones/at?lat={lat}&lng={lng}
            POST /safe-checks
            GET  /safe-checks?phone={p}
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Go, Firebase Cloud Messaging
```

---

## Example 275

**Intent:**
earthquake app in my country: people report damage to buildings and needs, rescue teams see

**Spec:**
```
Type:       Mobile application with backend (earthquake damage reporting)
Auth:       Phone number + OTP; rescue teams verified
Data model: DamageReport(id, reporter_phone, lat, lng, building_state, people_trapped, needs, photo_url, created_at)
            Team(id, name, kind)
            TeamAssignment(id, report_id -> DamageReport, team_id -> Team, status)
Features:   - Report building damage and trapped people with GPS
            - Queue reports offline until signal returns
            - Prioritise reports with trapped people
            - Let rescue teams claim and close reports
API:        REST
            POST /reports
            GET  /reports?priority=high
            POST /reports/{id}/assign
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin (Android), Python, FastAPI
```

---

## Example 276

**Intent:**
church app to plan who drives elderly members to service sunday

**Spec:**
```
Type:       Mobile application with backend (church ride coordination)
Auth:       Email + password
Data model: RideNeed(id, member_name, address, date, needs_wheelchair_space)
            DriverOffer(id, driver_id, date, seats, area)
            RideMatch(id, need_id -> RideNeed, offer_id -> DriverOffer)
Features:   - Record members who need a ride on Sunday
            - Let drivers offer seats by area
            - Match riders to drivers and notify both
            - Send drivers the pickup address on Saturday
API:        REST
            POST /needs
            POST /offers
            POST /matches/auto
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 277

**Intent:**
parish bulletin weekly in the app instead of paper

**Spec:**
```
Type:       Mobile application with backend (parish bulletin)
Auth:       Editor login
Data model: Bulletin(id, week_of, pdf_url, published_at)
            BulletinItem(id, bulletin_id -> Bulletin, title, body, category)
Features:   - Publish the weekly bulletin as sections and a PDF
            - Push a notification when it is out
            - Search past bulletins
            - Show mass intentions for the week
API:        REST
            GET  /bulletins/latest
            GET  /bulletins?q={text}
            POST /bulletins
Storage:    PostgreSQL, S3
Tech stack: Flutter, Strapi CMS
```

---

## Example 278

**Intent:**
I'm a hijab-wearing woman and finding women-only gym hours is hard, app that lists gyms and pools with ladies only sessions

**Spec:**
```
Type:       Mobile application with backend (women-only sessions finder)
Auth:       Email + password; venue owners can claim listings
Data model: Venue(id, name, kind, address, lat, lng, female_staff)
            WomenSession(id, venue_id -> Venue, weekday, start_time, end_time, notes)
            Review(id, venue_id -> Venue, user_id, stars, comment)
Features:   - Search gyms and pools with women-only sessions nearby
            - Show session times and whether staff are female
            - Let users suggest corrections to times
            - Rate and review venues
API:        REST
            GET  /venues/nearby?kind={k}
            POST /venues/{id}/sessions
            POST /venues/{id}/reviews
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Node.js
```

---

## Example 279

**Intent:**
halal restaurant finder with certification photo proof

**Spec:**
```
Type:       Mobile application with backend (halal restaurant finder)
Auth:       Email + password
Data model: Restaurant(id, name, address, lat, lng, cuisine)
            Certificate(id, restaurant_id -> Restaurant, authority, expires_on, photo_url, verified)
            Report(id, restaurant_id -> Restaurant, user_id, text, status)
Features:   - Find restaurants nearby with halal status
            - Show certification body and expiry
            - Flag expired certificates
            - Let users report changes for moderators
API:        REST
            GET  /restaurants/nearby
            POST /restaurants/{id}/certificates
            POST /restaurants/{id}/reports
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Python, FastAPI
```

---
## Example 280

**Intent:**
hearing aid users book adjustment appointments and audiologist sends settings remotely

**Spec:**
```
Type:       Mobile application with backend (hearing care)
Auth:       Email + password
Data model: Patient(id, name, device_model, audiologist_id)
            FittingProgram(id, patient_id -> Patient, name, settings_json, sent_at, applied_at)
            Appointment(id, patient_id -> Patient, starts_at, kind)
Features:   - Book in-clinic or remote fitting appointments
            - Receive new hearing programmes from the audiologist
            - Apply programmes to the device over Bluetooth
            - Rate how well each programme works in daily life
API:        REST
            POST /appointments
            POST /patients/{id}/programs
            POST /programs/{id}/feedback
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, Bluetooth LE, Node.js
```

---

## Example 281

**Intent:**
pregnancy clinic: moms track kicks, contractions, and send to midwife

**Spec:**
```
Type:       Mobile application with backend (midwife care)
Auth:       Email + password, linked by midwife
Data model: Mother(id, name, due_date, midwife_id)
            KickCount(id, mother_id -> Mother, kicks, minutes, at)
            Contraction(id, mother_id -> Mother, started_at, duration_s)
            Message(id, mother_id -> Mother, from_midwife, body, at)
Features:   - Count baby kicks with a timer
            - Time contractions and show intervals
            - Share logs with the assigned midwife
            - Message the midwife during office hours
API:        REST
            POST /kick-counts
            POST /contractions
            POST /messages
Storage:    PostgreSQL (encrypted)
Tech stack: Flutter, Python, Django
```

---

## Example 282

**Intent:**
sleep clinic, patient wears device at home, app uploads data to doctor

**Spec:**
```
Type:       Mobile application with backend (home sleep study)
Auth:       Study code + date of birth
Data model: SleepStudy(id, patient_id, device_serial, nights_required, status)
            NightRecording(id, study_id -> SleepStudy, night_of, file_url, quality)
Features:   - Pair with the home sleep device over Bluetooth
            - Guide the patient through sensor setup with videos
            - Upload each night's recording when on Wi-Fi
            - Tell the patient if a night must be repeated
API:        REST
            GET  /studies/{code}
            POST /studies/{id}/recordings
Storage:    PostgreSQL, S3
Tech stack: Kotlin, Swift, Java, Spring Boot
```

---

## Example 283

**Intent:**
cancer patients log side effects during chemo, nurse sees alerts

**Spec:**
```
Type:       Mobile application with backend (oncology symptom monitoring)
Auth:       Email + password with two-factor authentication
Data model: Patient(id, name, regimen, nurse_team_id)
            SymptomEntry(id, patient_id -> Patient, symptom, grade, temperature, at)
            NurseAlert(id, entry_id -> SymptomEntry, level, acknowledged_by, acknowledged_at)
Features:   - Log daily symptoms with severity grades
            - Raise an urgent alert for fever above 38 C
            - Show nurses a triage list by severity
            - Give self-care tips for mild symptoms
API:        REST
            POST /symptoms
            GET  /alerts?team={id}
            PATCH /alerts/{id}/ack
Storage:    PostgreSQL (encrypted)
Tech stack: React Native, C#, ASP.NET Core
```

---

## Example 284

**Intent:**
rehab after knee surgery, patient does exercises and phone camera counts reps

**Spec:**
```
Type:       Mobile application with backend (knee rehab)
Auth:       Email + password, invited by surgeon's clinic
Data model: RehabPlan(id, patient_id, surgery_date, phase)
            ExerciseSession(id, plan_id -> RehabPlan, exercise, reps_counted, max_angle_deg, at)
Features:   - Show exercises for the current recovery phase
            - Count reps and knee angle using on-device pose detection
            - Upload session results to the physiotherapist
            - Advance phases when goals are met
API:        REST
            GET  /plans/mine
            POST /sessions
Storage:    PostgreSQL
Tech stack: Flutter, Google ML Kit pose detection, Python, FastAPI
```

---

## Example 285

**Intent:**
hospital volunteer greeters app shifts + which entrance

**Spec:**
```
Type:       Mobile application with backend (hospital volunteer rota)
Auth:       Email + password
Data model: Post(id, name, location)
            VolunteerShift(id, post_id -> Post, starts_at, ends_at, volunteer_id)
Features:   - Show open greeter shifts by entrance
            - Claim and drop shifts
            - Clock in at the volunteer office kiosk
            - Notify when urgent cover is needed
API:        REST
            GET  /shifts/open
            POST /shifts/{id}/claim
            POST /clock-in
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 286

**Intent:**
NICU parents can see when nurse updates baby weight and photo

**Spec:**
```
Type:       Mobile application with backend (NICU family updates)
Auth:       Parent account with code from the unit plus SMS verification
Data model: Baby(id, bed, name, admitted_at)
            BabyUpdate(id, baby_id -> Baby, weight_g, feeding_ml, note, photo_url, posted_at)
            ParentLink(id, baby_id -> Baby, parent_id)
Features:   - Let nurses post weight, feeding and a photo
            - Notify linked parents of each update
            - Show a weight chart
            - Remove all data at discharge on request
API:        REST
            POST /babies/{id}/updates
            GET  /babies/{id}/updates
Storage:    PostgreSQL (encrypted), S3
Tech stack: React Native, Node.js
```

---

## Example 287

**Intent:**
patients rate hospital food and cleanliness before discharge

**Spec:**
```
Type:       Mobile application with backend (patient feedback)
Data model: Ward(id, name)
            FeedbackForm(id, ward_id -> Ward, food, cleanliness, staff, comment, submitted_at)
Features:   - Open the survey by scanning a bedside QR code
            - Rate food, cleanliness and staff
            - Show ward managers weekly averages
            - Flag negative comments for follow-up
API:        REST
            POST /feedback
            GET  /wards/{id}/scores
Storage:    PostgreSQL
Tech stack: Flutter, Go
```

---

## Example 288

**Intent:**
gym where personal trainers sell sessions, clients book and see workout log

**Spec:**
```
Type:       Mobile application with backend (personal training)
Auth:       Email + password
Data model: Trainer(id, name, rate)
            PtSession(id, trainer_id -> Trainer, client_id, starts_at, status)
            WorkoutLog(id, session_id -> PtSession, exercise, sets, reps, weight_kg)
Features:   - Buy session packs from a trainer
            - Book sessions from the trainer's calendar
            - Let trainers record the workout during the session
            - Show the client strength progress charts
API:        REST
            POST /sessions
            POST /sessions/{id}/logs
            GET  /clients/{id}/progress
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails, Stripe
```

---

## Example 289

**Intent:**
padel courts booking and find players at my level to fill 4

**Spec:**
```
Type:       Mobile application with backend (padel booking)
Auth:       Email + password
Data model: Player(id, name, level)
            PadelCourt(id, club, name)
            OpenMatch(id, court_id -> PadelCourt, starts_at, level_min, level_max, player_ids)
Features:   - Book a court for 90 minutes
            - Open a match for others to join by level
            - Split the court fee between players
            - Adjust player levels after results
API:        REST
            POST /matches
            POST /matches/{id}/join
            POST /matches/{id}/result
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 290

**Intent:**
skatepark app check how crowded and events

**Spec:**
```
Type:       Mobile application with backend (skatepark community)
Auth:       Optional email login
Data model: Skatepark(id, name, lat, lng, features)
            CrowdReport(id, park_id -> Skatepark, level, at)
            ParkEvent(id, park_id -> Skatepark, title, starts_at)
Features:   - Show skateparks with features like bowl or rails
            - Report how crowded a park is
            - List upcoming jams and lessons
            - Upload clips to a park feed
API:        REST
            GET  /parks
            POST /parks/{id}/crowd
            GET  /parks/{id}/events
Storage:    PostgreSQL, S3
Tech stack: React Native, Supabase
```

---

## Example 291

**Intent:**
swimming lake water quality and lifeguard on duty status

**Spec:**
```
Type:       Mobile application with backend (bathing water status)
Data model: Beach(id, name, lat, lng)
            WaterTest(id, beach_id -> Beach, ecoli, quality, tested_on)
            BeachStatus(beach_id -> Beach, lifeguard_on_duty, flag_colour, water_temp, updated_at)
Features:   - Show beaches with latest water quality rating
            - Show flag colour and lifeguard status
            - Alert followers when swimming is advised against
            - Let staff update status from the lifeguard tower
API:        REST
            GET  /beaches
            PUT  /beaches/{id}/status
            POST /beaches/{id}/tests
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 292

**Intent:**
marathon runners tracked live on course for family

**Spec:**
```
Type:       Mobile application with backend (race live tracking)
Auth:       Runners log in with bib number + email
Data model: Runner(id, bib, name, wave)
            TimingSplit(id, runner_id -> Runner, checkpoint_km, time)
            GpsPing(id, runner_id -> Runner, lat, lng, at)
Features:   - Receive chip timing splits from mats
            - Optionally share live GPS from the runner's phone
            - Let family follow runners and predict finish time
            - Notify followers at each split
API:        REST + WebSocket
            POST /splits
            GET  /runners?bib={b}
            WS   /runners/{id}/live
Storage:    PostgreSQL, Redis
Tech stack: React Native, Elixir, Phoenix
```

---

## Example 293

**Intent:**
cycling club group rides, members rsvp and see route gpx

**Spec:**
```
Type:       Mobile application with backend (cycling club rides)
Auth:       Email + password
Data model: Ride(id, title, starts_at, meeting_point, pace, gpx_url)
            RideRsvp(id, ride_id -> Ride, member_id)
Features:   - Post group rides with pace and route file
            - RSVP and see who is coming
            - Show the route map and elevation
            - Cancel rides for weather with a push alert
API:        REST
            POST /rides
            POST /rides/{id}/rsvp
            GET  /rides/{id}/route
Storage:    PostgreSQL, S3
Tech stack: Flutter, Go
```

---

## Example 294

**Intent:**
plz app for my laundromat show washer free + pay with phone instead of coins

**Spec:**
```
Type:       Mobile application with backend (laundromat payments)
Auth:       Email or phone login
Data model: Machine(id, number, kind, price, status, ends_at)
            CyclePayment(id, machine_id -> Machine, user_id, amount, started_at)
            Wallet(user_id, balance)
Features:   - Show which washers and dryers are free
            - Start a machine by paying from the app wallet
            - Notify when the cycle is done
            - Offer bonus credit on larger top-ups
API:        REST
            GET  /machines
            POST /machines/{id}/start
            POST /wallet/topup
Storage:    PostgreSQL
Tech stack: React Native, Node.js, MQTT (machine controllers), Stripe
```

---

## Example 295

**Intent:**
dry cleaner drop box 24h, customer scans bag and gets text when ready

**Spec:**
```
Type:       Mobile application with backend (dry cleaning drop box)
Auth:       Phone number + OTP
Data model: Bag(id, tag_code, customer_id)
            CleaningOrder(id, bag_id -> Bag, items, total, status, ready_at)
Features:   - Scan a bag tag before dropping it in the box
            - Itemise and price the order at the shop
            - Charge the saved card
            - Text the customer when ready for pickup
API:        REST
            POST /orders
            PATCH /orders/{id}/items
            PATCH /orders/{id}/ready
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Twilio, Stripe
```

---

## Example 296

**Intent:**
mosque wants to manage parking for jummah, people reserve parking spots

**Spec:**
```
Type:       Mobile application with backend (Friday prayer parking)
Auth:       Phone number + OTP
Data model: ParkingLot(id, name, spaces)
            ParkingPass(id, lot_id -> ParkingLot, user_id, date, plate)
Features:   - Reserve a parking space for Friday prayer
            - Give priority spaces to elderly and disabled worshippers
            - Show volunteers a plate list at the gate
            - Suggest nearby overflow parking when full
API:        REST
            GET  /lots?date={d}
            POST /passes
            GET  /lots/{id}/passes
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 297

**Intent:**
students rate campus bathrooms lol and report no toilet paper

**Spec:**
```
Type:       Mobile application with backend (campus restroom reports)
Auth:       University email login
Data model: Restroom(id, building, floor, accessible, gender)
            RestroomRating(id, restroom_id -> Restroom, user_id, stars)
            SupplyIssue(id, restroom_id -> Restroom, issue, created_at, resolved_at)
Features:   - Find the nearest restroom by building
            - Rate cleanliness
            - Report missing supplies by scanning a door QR code
            - Send issues to custodial staff
API:        REST
            GET  /restrooms?building={b}
            POST /restrooms/{id}/ratings
            POST /restrooms/{id}/issues
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 298

**Intent:**
graduation ceremony app - guest tickets, seating, live stream, order photos

**Spec:**
```
Type:       Mobile application with backend (graduation ceremony)
Auth:       University SSO for graduates; guests by ticket link
Data model: Ceremony(id, faculty, starts_at, venue, stream_url)
            GuestTicket(id, ceremony_id -> Ceremony, graduate_id, guest_name, seat, qr_token)
            PhotoOrder(id, graduate_id, package, paid)
Features:   - Request up to 4 guest tickets
            - Assign seats and send QR tickets
            - Show the ceremony livestream
            - Order professional photos of the stage moment
API:        REST
            POST /tickets
            POST /tickets/scan
            POST /photo-orders
Storage:    PostgreSQL
Tech stack: React Native, Python, Django
```

---

## Example 299

**Intent:**
open day campus tour app for prospective students with GPS stops

**Spec:**
```
Type:       Mobile application with backend (campus tour)
Data model: TourStop(id, name, lat, lng, video_url, description, order)
            Visitor(id, email, intended_major)
            OpenDaySession(id, title, building, starts_at)
Features:   - Guide visitors along tour stops with GPS
            - Play a student video at each stop
            - Show open day talks by major
            - Collect emails for follow-up
API:        REST
            GET  /stops
            GET  /sessions
            POST /visitors
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Mapbox
```

---

## Example 300

**Intent:**
student housing roommate matching survey sleep time cleanliness etc

**Spec:**
```
Type:       Mobile application with backend (roommate matching)
Auth:       University SSO
Data model: Profile(id, student_id, sleep_time, cleanliness, guests, smoking, bio)
            RoommateRequest(id, from_id -> Profile, to_id -> Profile, status)
Features:   - Fill a lifestyle questionnaire
            - Show compatibility scores with other students
            - Send and accept roommate requests
            - Send confirmed pairs to housing office
API:        REST
            PUT  /profiles/me
            GET  /matches
            POST /requests
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI
```

---

## Example 301

**Intent:**
lab safety training app for chemistry students, quiz before lab access

**Spec:**
```
Type:       Mobile application with backend (lab safety training)
Auth:       University SSO
Data model: Module(id, title, video_url)
            Question(id, module_id -> Module, text, options, answer)
            Completion(id, module_id -> Module, student_id, score, passed_at)
Features:   - Watch safety videos per module
            - Take a quiz requiring 80% to pass
            - Show a pass badge that the lab tech can scan
            - Send yearly refresher reminders
API:        REST
            GET  /modules
            POST /modules/{id}/attempts
            GET  /students/{id}/badge
Storage:    PostgreSQL
Tech stack: Flutter, Django
```

---

## Example 302

**Intent:**
I'm the facilities person at a private school campus with 12 buildings. Teachers email me when a projector breaks or room is too cold and I lose half of it. I need a little app for staff to submit tickets with the room, and my 3 guys get assigned.

**Spec:**
```
Type:       Mobile application with backend (school facilities tickets)
Auth:       Google Workspace sign-in (school domain)
Data model: Room(id, building, number)
            FacilityTicket(id, room_id -> Room, reporter_id, category, description, photo_url, priority, status)
            Technician(id, name, skills)
            TicketAssignment(id, ticket_id -> FacilityTicket, technician_id -> Technician)
Features:   - Submit a ticket by picking building and room
            - Attach a photo and priority
            - Assign tickets to technicians by category
            - Notify the reporter when fixed
            - Show open tickets by building
API:        REST
            POST /tickets
            PATCH /tickets/{id}/assign
            PATCH /tickets/{id}/close
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express
```

---

## Example 303

**Intent:**
rideshare for students going home on weekends, split fuel

**Spec:**
```
Type:       Mobile application with backend (student weekend rideshare)
Auth:       University email verification
Data model: Trip(id, driver_id, from_city, to_city, departs_at, seats, fuel_share)
            SeatRequest(id, trip_id -> Trip, rider_id, status)
Features:   - Post a trip with seats and fuel cost share
            - Search trips by destination and date
            - Request and confirm seats
            - Rate drivers and riders
API:        REST
            POST /trips
            GET  /trips?to={city}&date={d}
            POST /trips/{id}/requests
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 304

**Intent:**
campus pantry for students in need, order privately and pick up locker

**Spec:**
```
Type:       Mobile application with backend (campus food pantry)
Auth:       University SSO
Data model: PantryItem(id, name, category, stock, limit_per_week)
            PantryOrder(id, student_ref, items, locker_number, pickup_code, status)
Features:   - Browse pantry items with weekly limits
            - Place an order privately
            - Pick up from a locker with a code
            - Show staff stock levels and popular items
API:        REST
            GET  /items
            POST /orders
            GET  /stock
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 305

**Intent:**
church kids check in sunday school with printed name tag and parent pickup code

**Spec:**
```
Type:       Mobile application with backend (children's ministry check-in)
Auth:       Parent phone + OTP; volunteer login on kiosk
Data model: Child(id, family_id, name, allergies, classroom)
            CheckIn(id, child_id -> Child, date, security_code, checked_out_at)
Features:   - Check children in from the parent's phone or kiosk
            - Print a name tag with allergies and a matching parent tag
            - Require the matching code at pickup
            - Page parents during service if needed
API:        REST
            POST /checkins
            POST /checkins/{id}/checkout
            POST /checkins/{id}/page
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Brother label printer SDK
```

---

## Example 306

**Intent:**
quiz app for our islamic weekend school, kids n teachers, leaderboard per class

**Spec:**
```
Type:       Mobile application with backend (Islamic studies quiz)
Auth:       Teacher email + password; student class codes
Data model: ClassGroup(id, name, teacher_id, code)
            Quiz(id, class_id -> ClassGroup, title, questions_json, due_on)
            QuizAttempt(id, quiz_id -> Quiz, student_id, score, finished_at)
Features:   - Let teachers create multiple-choice quizzes
            - Assign quizzes to a class with a due date
            - Score attempts automatically
            - Show a class leaderboard
API:        REST
            POST /quizzes
            POST /quizzes/{id}/attempts
            GET  /classes/{id}/leaderboard
Storage:    PostgreSQL
Tech stack: Flutter, Firebase
```

---

## Example 307

**Intent:**
apartment building gym time slots during covid style limits

**Spec:**
```
Type:       Mobile application with backend (building gym slots)
Auth:       Resident email + password
Data model: GymSlot(id, starts_at, capacity)
            GymReservation(id, slot_id -> GymSlot, resident_id, checked_in)
Features:   - Reserve a 45-minute gym slot
            - Limit each resident to one slot a day
            - Unlock the gym door during the slot
            - Cancel a no-show after 10 minutes
API:        REST
            GET  /slots?date={d}
            POST /reservations
            POST /reservations/{id}/unlock
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---
## Example 308

**Intent:**
Hello, I have small hotel in Bali, want app where guest can book scooter, tours and spa from phone and pay at checkout. Backend in Laravel please.

**Spec:**
```
Type:       Mobile application with backend (hotel guest activities)
Auth:       Booking reference + last name
Data model: GuestStay(id, booking_ref, last_name, room, check_in, check_out)
            Activity(id, kind, name, price, duration)
            ActivityBooking(id, stay_id -> GuestStay, activity_id -> Activity, date, people, status)
Features:   - Show scooter rental, tours and spa treatments
            - Book activities and add them to the room bill
            - Let staff confirm or reschedule bookings
            - Show the final bill at checkout
API:        REST
            GET  /activities
            POST /stays/{id}/bookings
            GET  /stays/{id}/bill
Storage:    MySQL
Tech stack: Flutter, PHP, Laravel
```

---

## Example 309

**Intent:**
mi familia tiene restaurante, we want customers do waitlist and also see menu before sit, and send sms when table ok

**Spec:**
```
Type:       Mobile application with backend (restaurant waitlist and menu)
Auth:       Staff PIN on host tablet
Data model: WaitingParty(id, name, phone, size, added_at, status)
            MenuItem(id, name, description, price, category, language)
Features:   - Add guests to the waitlist with phone number
            - Text a link where guests can see their place and the menu
            - Show the menu in Spanish and English
            - Send an SMS when the table is ready
API:        REST
            POST /parties
            GET  /parties/{id}
            POST /parties/{id}/ready
            GET  /menu?lang={l}
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Twilio
```

---

## Example 310

**Intent:**
I need React Native app with Supabase for our scout troop, parents see camp trips, pay fees, sign permission

**Spec:**
```
Type:       Mobile application with backend (scout troop)
Auth:       Supabase Auth (email magic link)
Data model: Scout(id, parent_id, name, patrol, rank)
            Trip(id, title, starts_on, ends_on, fee, gear_list)
            Permission(id, trip_id -> Trip, scout_id -> Scout, signed_by, signed_at, paid)
Features:   - List upcoming trips with gear lists
            - Sign permission slips in the app
            - Pay trip fees
            - Track rank advancement requirements
API:        Supabase client SDK with row-level security
Storage:    Supabase (PostgreSQL)
Tech stack: React Native, Supabase, Stripe
```

---

## Example 311

**Intent:**
bus company: intercity tickets, choose seat, show QR to driver

**Spec:**
```
Type:       Mobile application with backend (intercity bus tickets)
Auth:       Email + password or guest checkout
Data model: Trip(id, route, departs_at, bus_id)
            Seat(id, bus_id, number, type)
            BusTicket(id, trip_id -> Trip, seat_id -> Seat, passenger_name, qr_token, status)
Features:   - Search trips by cities and date
            - Pick a seat from the bus layout
            - Pay and show a QR ticket offline
            - Let drivers scan tickets with the driver app
API:        REST
            GET  /trips?from={c}&to={c}&date={d}
            GET  /trips/{id}/seats
            POST /tickets
            POST /tickets/scan
Storage:    PostgreSQL
Tech stack: Flutter, Java, Spring Boot
```

---

## Example 312

**Intent:**
water taxi on river book seat and see boat arriving

**Spec:**
```
Type:       Mobile application with backend (water taxi)
Auth:       Phone number + OTP
Data model: Pier(id, name, lat, lng)
            Boat(id, name, seats, lat, lng)
            Sailing(id, boat_id -> Boat, from_pier_id -> Pier, to_pier_id -> Pier, departs_at)
            SeatBooking(id, sailing_id -> Sailing, passenger_id, seats)
Features:   - Show piers and live boat positions
            - Book seats on the next sailing
            - Show arrival countdown at the pier
            - Validate tickets on board
API:        REST
            GET  /sailings?from={pier}
            POST /bookings
            GET  /boats/live
Storage:    PostgreSQL
Tech stack: React Native, Go
```

---

## Example 313

**Intent:**
transit app for deaf riders, shows service disruptions as text and vibrate

**Spec:**
```
Type:       Mobile application with backend (accessible transit alerts)
Auth:       Optional email login for saved lines
Data model: Line(id, name, mode)
            Disruption(id, line_id -> Line, message, severity, starts_at, ends_at)
            Subscription(id, user_id, line_id -> Line, time_windows)
Features:   - Show disruptions as large text with icons
            - Vibrate in a distinct pattern for subscribed lines
            - Convert station announcements to text from the GTFS-realtime feed
            - Show sign-language video for major disruptions
API:        REST
            GET  /disruptions
            POST /subscriptions
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, Python, FastAPI, GTFS-realtime
```

---

## Example 314

**Intent:**
blind users need app to request help from station staff when arriving at train

**Spec:**
```
Type:       Mobile application with backend (station assistance)
Auth:       Email + password
Data model: AssistanceRequest(id, user_id, station_from, station_to, departs_at, needs, status)
            StationStaff(id, station, name, on_duty)
Features:   - Book assistance for a journey with a fully screen-reader friendly interface
            - Notify staff at the departure and arrival stations
            - Confirm meeting point and staff name
            - Update staff if the train is delayed
API:        REST
            POST /requests
            PATCH /requests/{id}
            GET  /stations/{id}/requests
Storage:    PostgreSQL
Tech stack: Swift (VoiceOver), Kotlin (TalkBack), Node.js
```

---

## Example 315

**Intent:**
library delivers books to housebound elderly, volunteer drivers app

**Spec:**
```
Type:       Mobile application with backend (housebound library delivery)
Auth:       Volunteer email + password
Data model: Reader(id, name, address, preferences)
            BookDelivery(id, reader_id -> Reader, books, scheduled_on, driver_id, status)
            Return(id, delivery_id -> BookDelivery, books, collected_at)
Features:   - Show volunteers their monthly delivery list
            - Mark books delivered and returns collected
            - Record reading preferences for the next selection
            - Let staff plan routes by area
API:        REST
            GET  /deliveries/mine
            PATCH /deliveries/{id}
            POST /deliveries/{id}/returns
Storage:    PostgreSQL
Tech stack: Flutter, Django
```

---

## Example 316

**Intent:**
shopping helper volunteers for elderly during flu season, request groceries

**Spec:**
```
Type:       Mobile application with backend (grocery help for seniors)
Auth:       Phone number + OTP
Data model: GroceryRequest(id, requester_id, list_text, address, budget, status)
            Helper(id, name, area, verified)
            Delivery(id, request_id -> GroceryRequest, helper_id -> Helper, receipt_url, amount)
Features:   - Post a grocery list by text or voice
            - Let verified helpers in the area accept
            - Upload the receipt for reimbursement
            - Allow requests by phone call through a coordinator
API:        REST
            POST /requests
            POST /requests/{id}/accept
            POST /requests/{id}/delivered
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 317

**Intent:**
bloodmobile schedule where is the blood bus this week

**Spec:**
```
Type:       Mobile application with backend (mobile blood drives)
Auth:       Optional donor login for booking
Data model: Drive(id, host, address, lat, lng, date, start_time, end_time)
            DriveSlot(id, drive_id -> Drive, time, capacity)
            DriveBooking(id, slot_id -> DriveSlot, donor_id)
Features:   - Show upcoming blood drives on a map
            - Book a slot at a drive
            - Let companies request to host a drive
            - Remind donors the day before
API:        REST
            GET  /drives?near={lat,lng}
            POST /slots/{id}/book
            POST /host-requests
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 318

**Intent:**
plasma donation centre pay donors, track visits and payments

**Spec:**
```
Type:       Mobile application with backend (plasma donation centre)
Auth:       Email + password with ID verification at first visit
Data model: Donor(id, name, weight_kg, status)
            PlasmaVisit(id, donor_id -> Donor, at, volume_ml, compensation)
            PrepaidCard(id, donor_id -> Donor, card_ref, balance)
Features:   - Book donation appointments
            - Enforce minimum days between donations
            - Show compensation per visit and promotions
            - Show the prepaid card balance
API:        REST
            POST /appointments
            GET  /visits
            GET  /card
Storage:    PostgreSQL
Tech stack: React Native, C#, ASP.NET Core
```

---

## Example 319

**Intent:**
bone marrow registry cheek swab kit order and status

**Spec:**
```
Type:       Mobile application with backend (marrow donor registry)
Auth:       Email + password
Data model: Registrant(id, name, date_of_birth, address, ethnicity)
            SwabKit(id, registrant_id -> Registrant, tracking_number, status)
            MatchContact(id, registrant_id -> Registrant, contacted_at, response)
Features:   - Check eligibility by age and health questions
            - Order a cheek swab kit to the home address
            - Track kit status from sent to typed
            - Respond quickly if contacted as a possible match
API:        REST
            POST /registrants
            GET  /kits/mine
            POST /match-contacts/{id}/respond
Storage:    PostgreSQL (encrypted)
Tech stack: Flutter, Java, Spring Boot
```

---

## Example 320

**Intent:**
Event volunteer marshals for a city marathon, they get assigned a spot and check in there

**Spec:**
```
Type:       Mobile application with backend (race marshal management)
Auth:       Email + password
Data model: MarshalPost(id, name, km, lat, lng, required)
            Marshal(id, name, phone, tshirt_size)
            PostAssignment(id, post_id -> MarshalPost, marshal_id -> Marshal, checked_in_at)
Features:   - Assign marshals to posts along the course
            - Check in by GPS at the post
            - Show the race director unstaffed posts
            - Broadcast instructions to all marshals
API:        REST
            POST /assignments
            POST /assignments/{id}/checkin
            GET  /posts/unstaffed
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 321

**Intent:**
soup kitchen volunteers + how many meals served each night

**Spec:**
```
Type:       Mobile application with backend (soup kitchen)
Auth:       Email + password
Data model: ServiceNight(id, date, volunteers_needed)
            VolunteerSignup(id, night_id -> ServiceNight, volunteer_id)
            MealCount(id, night_id -> ServiceNight, meals_served, leftovers_kg)
Features:   - Sign up to serve on a night
            - Record meals served at the end of the night
            - Show monthly totals for funders
            - Post donation needs like rice or oil
API:        REST
            POST /nights/{id}/signups
            POST /nights/{id}/count
            GET  /reports/monthly
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 322

**Intent:**
habitat style house build volunteers sign up for build days with skill level

**Spec:**
```
Type:       Mobile application with backend (home build volunteers)
Auth:       Email + password, waiver signed
Data model: BuildDay(id, site, date, tasks, max_volunteers)
            BuildVolunteer(id, name, skill_level, waiver_signed_at)
            BuildSignup(id, day_id -> BuildDay, volunteer_id -> BuildVolunteer)
Features:   - Sign up for build days
            - Require a signed safety waiver
            - Show tasks and what to bring
            - Record hours and skills used
API:        REST
            GET  /build-days
            POST /build-days/{id}/signups
            POST /waivers
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails
```

---

## Example 323

**Intent:**
lost dog posters are so last century, want app where my dog has a QR tag, finder scans and I get location

**Spec:**
```
Type:       Mobile application with backend (pet QR tags)
Auth:       Owner email + password; finders need no account
Data model: Pet(id, owner_id, name, photo_url, medical_notes, tag_code)
            TagScan(id, pet_id -> Pet, lat, lng, finder_message, scanned_at)
Features:   - Register a pet and link a QR tag
            - Show finders a page with the pet's name and contact button
            - Send the owner the scan location instantly
            - Hide owner phone number behind an in-app relay
API:        REST
            POST /pets
            GET  /tags/{code}
            POST /tags/{code}/scans
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Twilio Proxy
```

---

## Example 324

**Intent:**
stray animal feeding volunteers in our city mark where they fed and cats needing vet

**Spec:**
```
Type:       Mobile application with backend (stray animal care)
Auth:       Email + password
Data model: Colony(id, name, lat, lng, est_count)
            Feeding(id, colony_id -> Colony, volunteer_id, at)
            VetNeed(id, colony_id -> Colony, description, photo_url, status)
Features:   - Map feeding spots and colonies
            - Log feedings so spots are not fed twice
            - Report animals needing a vet
            - Track neutering progress per colony
API:        REST
            GET  /colonies
            POST /colonies/{id}/feedings
            POST /colonies/{id}/vet-needs
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Python, FastAPI
```

---

## Example 325

**Intent:**
venue ticket scanning app for door staff, check in fast, works offline

**Spec:**
```
Type:       Mobile application with backend (door ticket scanning)
Auth:       Staff code per event
Data model: Event(id, name, starts_at)
            Ticket(id, event_id -> Event, code, holder_name, type, scanned_at)
Features:   - Download all ticket codes before doors open
            - Scan and validate codes offline
            - Warn on already-scanned tickets
            - Sync scans across devices when online
API:        REST
            GET  /events/{id}/tickets
            POST /scans/sync
Storage:    PostgreSQL, SQLite on device
Tech stack: Kotlin, Swift, Go
```

---

## Example 326

**Intent:**
transfer my season ticket to friend for one game at the stadium

**Spec:**
```
Type:       Mobile application with backend (season ticket transfers)
Auth:       Email + password
Data model: SeasonTicket(id, holder_id, section, row, seat)
            Fixture(id, opponent, kicks_off_at)
            Transfer(id, ticket_id -> SeasonTicket, fixture_id -> Fixture, recipient_email, status)
Features:   - List the season's fixtures for the seat
            - Transfer one game to a friend by email
            - Issue a new barcode to the recipient
            - Cancel transfers until 2 hours before kickoff
API:        REST
            GET  /tickets/mine/fixtures
            POST /transfers
            DELETE /transfers/{id}
Storage:    PostgreSQL
Tech stack: React Native, Java, Spring Boot
```

---

## Example 327

**Intent:**
stadium seat upgrade during game if better seats empty

**Spec:**
```
Type:       Mobile application with backend (in-game seat upgrades)
Auth:       Ticket barcode linked to an account
Data model: SeatInventory(id, section, row, seat, game_id, status, upgrade_price)
            Upgrade(id, ticket_id, new_seat_id -> SeatInventory, paid, at)
Features:   - Show unsold better seats after kickoff
            - Pay to move and get a new barcode
            - Release the old seat back to inventory
            - Show the route to the new section
API:        REST
            GET  /games/{id}/upgrades
            POST /upgrades
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 328

**Intent:**
concert venue app: merch preorder and pickup at booth, skip line

**Spec:**
```
Type:       Mobile application with backend (merch preorder)
Auth:       Email or Apple/Google sign-in
Data model: MerchItem(id, show_id, name, sizes, price, stock)
            MerchOrder(id, show_id, user_id, items, pickup_code, status)
Features:   - Browse tour merch for tonight's show
            - Order and pay before the show
            - Pick up at a dedicated booth with a code
            - Show the merch team live stock levels
API:        REST
            GET  /shows/{id}/merch
            POST /orders
            POST /orders/{id}/pickup
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe
```

---

## Example 329

**Intent:**
want to make museum app for kids where they hunt for objects and collect stickers

**Spec:**
```
Type:       Mobile application with backend (museum kids trail)
Data model: Trail(id, name, age_range)
            TrailObject(id, trail_id -> Trail, gallery, clue, answer, sticker_url)
            TrailProgress(id, device_id, object_id -> TrailObject, found_at)
Features:   - Give kids picture clues to find objects in galleries
            - Unlock a sticker when they answer a question about the object
            - Show a sticker book of collected items
            - Let staff edit trails for temporary exhibits
API:        REST
            GET  /trails
            POST /progress
            PUT  /trails/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Python, Django
```

---

## Example 330

**Intent:**
open air cinema tickets with blanket rental

**Spec:**
```
Type:       Mobile application with backend (open-air cinema)
Auth:       Email + password or guest checkout
Data model: Screening(id, film, date, starts_at, capacity, rain_policy)
            CinemaTicket(id, screening_id -> Screening, qty, blanket_rentals, qr_token)
Features:   - Buy tickets for outdoor screenings
            - Add blanket and chair rentals
            - Notify and refund if cancelled for rain
            - Scan tickets at the gate
API:        REST
            GET  /screenings
            POST /tickets
            POST /screenings/{id}/cancel
Storage:    PostgreSQL
Tech stack: React Native, Laravel, Stripe
```

---

## Example 331

**Intent:**
temple app to see the live darshan video and donate online, Kotlin android only

**Spec:**
```
Type:       Mobile application with backend (temple live darshan)
Auth:       Phone number + OTP for donations
Data model: LiveStream(id, title, stream_url, is_live)
            Donation(id, user_id, purpose, amount, receipt_number, at)
Features:   - Watch live darshan streams
            - Donate online for annadanam or upkeep
            - Download 80G tax receipts
            - Show daily aarti timings
API:        REST
            GET  /streams/live
            POST /donations
            GET  /donations/{id}/receipt
Storage:    PostgreSQL
Tech stack: Kotlin (Android), Jetpack Compose, ExoPlayer, Spring Boot, Razorpay
```

---

## Example 332

**Intent:**
pilgrimage group trip app for umrah, group leader sends schedule and finds lost members

**Spec:**
```
Type:       Mobile application with backend (pilgrimage group coordination)
Auth:       Group invite code + phone OTP
Data model: PilgrimGroup(id, name, leader_id)
            Pilgrim(id, group_id -> PilgrimGroup, name, phone, hotel_room, share_location)
            ItineraryItem(id, group_id -> PilgrimGroup, title, starts_at, meeting_point)
Features:   - Share the daily schedule and meeting points
            - Let members share location with the leader
            - Send an SOS when a member is lost
            - Broadcast messages in Arabic, English or Urdu
API:        REST + WebSocket
            GET  /groups/{id}/itinerary
            POST /pilgrims/{id}/location
            POST /sos
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Node.js, Socket.IO
```

---
## Example 333

**Intent:**
hair salon stylists save each client's colour formula and photos

**Spec:**
```
Type:       Mobile application with backend (salon client records)
Auth:       Stylist email + password
Data model: Client(id, name, phone, allergies)
            ColourFormula(id, client_id -> Client, stylist_id, products, ratios, developer, processing_min, created_at)
            VisitPhoto(id, client_id -> Client, url, taken_on)
Features:   - Save colour formulas per visit
            - Attach before and after photos
            - Flag allergy patch-test dates
            - Share client history between stylists in the salon
API:        REST
            POST /clients/{id}/formulas
            POST /clients/{id}/photos
            GET  /clients/{id}
Storage:    PostgreSQL, S3
Tech stack: Flutter, Firebase
```

---

## Example 334

**Intent:**
24 hour gym door access with phone, no staff at night

**Spec:**
```
Type:       Mobile application with backend (24/7 gym access)
Auth:       Email + password, active membership required
Data model: Membership(id, member_id, plan, status, valid_to)
            DoorEvent(id, member_id, door, at, granted)
Features:   - Open the gym door with Bluetooth from the app
            - Deny entry for frozen or unpaid memberships
            - Prevent tailgating by logging one entry per scan
            - Show a panic button that alerts security
API:        REST
            POST /door/open
            POST /panic
            GET  /memberships/me
Storage:    PostgreSQL
Tech stack: React Native, Node.js, BLE access controller
```

---

## Example 335

**Intent:**
big group restaurant bookings need deposit and pre-order menu

**Spec:**
```
Type:       Mobile application with backend (group dining bookings)
Auth:       Email + password
Data model: GroupBooking(id, organiser_id, date, time, guests, deposit_paid, status)
            GuestChoice(id, booking_id -> GroupBooking, guest_name, starter, main, dessert, dietary)
Features:   - Request a table for 10 or more guests
            - Pay a per-person deposit
            - Send guests a link to choose from the set menu
            - Give the kitchen a summary of choices
API:        REST
            POST /group-bookings
            POST /group-bookings/{id}/choices
            GET  /group-bookings/{id}/kitchen-summary
Storage:    PostgreSQL
Tech stack: React Native, Django, Stripe
```

---

## Example 336

**Intent:**
beverage distributor reps take orders from bars and see what they ordered last month

**Spec:**
```
Type:       Mobile application with backend (beverage distribution sales)
Auth:       Company login
Data model: Account(id, venue_name, address, licence_type)
            Product(id, sku, name, case_size, price)
            AccountOrder(id, account_id -> Account, rep_id, lines_json, delivery_date)
Features:   - Show account order history and suggested reorder
            - Create orders by case or keg
            - Check stock before confirming
            - Schedule delivery dates by route
API:        REST
            GET  /accounts/{id}/history
            POST /orders
            GET  /stock?sku={s}
Storage:    PostgreSQL
Tech stack: Flutter, Java, Spring Boot
```

---

## Example 337

**Intent:**
crop insurance for small farmers, file claim with photo of damaged field

**Spec:**
```
Type:       Mobile application with backend (crop insurance)
Auth:       Phone number + OTP
Data model: Farmer(id, name, phone, national_id)
            InsuredPlot(id, farmer_id -> Farmer, crop, area_ha, lat, lng, season)
            CropClaim(id, plot_id -> InsuredPlot, cause, photo_urls, status, payout)
Features:   - Register plots with GPS location
            - File a claim with geotagged photos
            - Check claims against satellite rainfall data
            - Pay out to mobile money
API:        REST
            POST /plots
            POST /plots/{id}/claims
            GET  /claims/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin (Android), Python, Django, M-Pesa API
```

---

## Example 338

**Intent:**
tenant maintenance requests for property manager with 200 units, vendors assigned

**Spec:**
```
Type:       Mobile application with backend (property maintenance)
Auth:       Email + password for tenants, managers and vendors
Data model: Unit(id, property, number, tenant_id)
            MaintenanceTicket(id, unit_id -> Unit, category, description, photo_url, urgency, status)
            Vendor(id, name, trade, phone)
            WorkAssignment(id, ticket_id -> MaintenanceTicket, vendor_id -> Vendor, scheduled_at, cost)
Features:   - Let tenants submit tickets with photos and entry permission
            - Assign vendors by trade
            - Let vendors update status and upload invoices
            - Show managers costs per property
API:        REST
            POST /tickets
            POST /tickets/{id}/assign
            PATCH /assignments/{id}
Storage:    PostgreSQL, S3
Tech stack: React Native, Laravel
```

---

## Example 339

**Intent:**
motorcycle parking spots in city centre, few, app shows free ones from sensors

**Spec:**
```
Type:       Mobile application with backend (motorcycle parking sensors)
Data model: Bay(id, street, lat, lng, spaces)
            SensorReading(id, bay_id -> Bay, occupied, at)
Features:   - Receive occupancy from in-ground sensors
            - Show free motorcycle bays on a map
            - Navigate to the nearest free bay
            - Show predicted availability for later
API:        REST
            POST /readings
            GET  /bays/free
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Node.js, LoRaWAN sensors
```

---

## Example 340

**Intent:**
city walking tours led by local guides, book spot and tip the guide

**Spec:**
```
Type:       Mobile application with backend (guided walking tours)
Auth:       Email + password
Data model: Guide(id, name, languages, bio)
            WalkingTour(id, guide_id -> Guide, title, meeting_point, starts_at, max_people)
            TourBooking(id, tour_id -> WalkingTour, user_id, people)
            Tip(id, booking_id -> TourBooking, amount)
Features:   - Book a free spot on a walking tour
            - Show the meeting point on a map
            - Tip the guide in the app after the tour
            - Rate the tour
API:        REST
            GET  /tours?city={c}
            POST /tours/{id}/bookings
            POST /bookings/{id}/tip
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe Connect
```

---

## Example 341

**Intent:**
outdoor escape game in city, team solves puzzles at locations, gps unlocks next

**Spec:**
```
Type:       Mobile application with backend (outdoor puzzle game)
Auth:       Game code per team
Data model: Game(id, city, title, duration_min)
            Puzzle(id, game_id -> Game, order, lat, lng, radius_m, question, answer_hash, hint)
            TeamRun(id, game_id -> Game, team_name, started_at, current_puzzle, hints_used)
Features:   - Unlock each puzzle only within its GPS radius
            - Check answers on the server
            - Give hints with a time penalty
            - Show the final time on a city leaderboard
API:        REST
            POST /runs
            GET  /runs/{id}/puzzle
            POST /runs/{id}/answer
            GET  /games/{id}/leaderboard
Storage:    PostgreSQL
Tech stack: Flutter, Go
```

---

## Example 342

**Intent:**
i manage 6 car parks at hospital, staff and patients different prices, want app to pay

**Spec:**
```
Type:       Mobile application with backend (hospital car parks)
Auth:       Patients by email; staff by hospital SSO
Data model: CarPark(id, name, staff_only)
            Tariff(id, car_park_id -> CarPark, user_type, hourly, daily_cap)
            ParkingStay(id, car_park_id -> CarPark, plate, user_type, started_at, ended_at, amount)
Features:   - Start and stop parking by plate
            - Apply staff or patient tariffs
            - Give free parking to blue-badge holders and long-stay relatives
            - Show estates staff usage per car park
API:        REST
            POST /stays
            POST /stays/{id}/end
            GET  /reports/usage
Storage:    PostgreSQL
Tech stack: React Native, C#, ASP.NET Core
```

---

## Example 343

**Intent:**
mosque funeral (janazah) announcements and volunteer for ghusl

**Spec:**
```
Type:       Mobile application with backend (janazah announcements)
Auth:       Admin login; members by phone + OTP
Data model: Janazah(id, deceased_name, prayer_time, location, burial_place)
            GhuslVolunteer(id, name, phone, gender)
            GhuslCall(id, janazah_id -> Janazah, volunteer_id -> GhuslVolunteer, response)
Features:   - Post janazah announcements with prayer time
            - Push notifications to the community
            - Call trained ghusl volunteers of the same gender
            - Collect condolence messages for the family
API:        REST
            POST /janazahs
            POST /janazahs/{id}/ghusl-calls
            POST /janazahs/{id}/condolences
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 344

**Intent:**
want simple app for our church to track attendance each Sunday and see who missed 3 weeks so we call them

**Spec:**
```
Type:       Mobile application with backend (church attendance follow-up)
Auth:       Staff email + password
Data model: Member(id, name, phone, family_id)
            ServiceAttendance(id, member_id -> Member, date)
            FollowUp(id, member_id -> Member, assigned_to, note, done_at)
Features:   - Mark attendance by family on a tablet
            - List members absent 3 Sundays in a row
            - Assign follow-up calls to pastoral team
            - Record follow-up notes
API:        REST
            POST /attendance
            GET  /members/absent?weeks=3
            POST /follow-ups
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 345

**Intent:**
seniors center lunch reservations each day with transport

**Spec:**
```
Type:       Mobile application with backend (senior centre lunches)
Auth:       Phone number; staff can book for members
Data model: Senior(id, name, phone, diet, needs_transport)
            LunchReservation(id, senior_id -> Senior, date, transport, status)
Features:   - Reserve lunch by 10am the day before
            - Request a van pickup
            - Show kitchen counts per diet
            - Give drivers the pickup list
API:        REST
            POST /reservations
            GET  /kitchen/counts?date={d}
            GET  /transport/list?date={d}
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 346

**Intent:**
community choir rehearsal attendance and part learning tracks

**Spec:**
```
Type:       Mobile application with backend (community choir)
Auth:       Email + password
Data model: Singer(id, name, voice_part)
            Rehearsal(id, date, venue, songs)
            RsvpRecord(id, rehearsal_id -> Rehearsal, singer_id -> Singer, attending)
            LearningTrack(id, song, voice_part, audio_url)
Features:   - RSVP to rehearsals
            - Show the director attendance by voice part
            - Play learning tracks with tempo control
            - Collect yearly membership fees
API:        REST
            POST /rehearsals/{id}/rsvp
            GET  /tracks?part={p}
            POST /fees
Storage:    PostgreSQL, S3
Tech stack: React Native, Node.js, Stripe
```

---

## Example 347

**Intent:**
coworking for parents with creche, book desk and childcare slot together

**Spec:**
```
Type:       Mobile application with backend (coworking with creche)
Auth:       Email + password
Data model: Child(id, parent_id, name, birth_date, allergies)
            DeskDay(id, date, desks_free)
            CrecheSlot(id, date, session, places)
            CombinedBooking(id, parent_id, date, desk, creche_session, child_ids)
Features:   - Book a desk and creche session in one step
            - Enforce staff-to-child ratios by age
            - Share daily creche notes with parents
            - Bill monthly
API:        REST
            GET  /availability?date={d}
            POST /bookings
            POST /creche-notes
Storage:    PostgreSQL
Tech stack: Flutter, Django
```

---

## Example 348

**Intent:**
I own 3 vending machines in hospitals and need app to know what's empty before I drive there

**Spec:**
```
Type:       Mobile application with backend (vending machine monitoring)
Auth:       Owner email + password
Data model: VendingMachine(id, location, model)
            Slot(id, machine_id -> VendingMachine, product, stock, capacity)
            SaleEvent(id, slot_id -> Slot, price, at)
Features:   - Receive sales events from the machine telemetry board
            - Show stock per slot and machine
            - Build a restock pick list before driving out
            - Show sales by product per week
API:        REST
            POST /telemetry
            GET  /machines/{id}/stock
            GET  /restock-list
Storage:    PostgreSQL
Tech stack: React Native, Node.js, MQTT
```

---

## Example 349

**Intent:**
hospital chaplain visit requests from patients

**Spec:**
```
Type:       Mobile application with backend (chaplaincy requests)
Auth:       Staff login; patients request via bedside tablet
Data model: VisitRequest(id, ward, bed, faith, urgency, note, status, created_at)
            Chaplain(id, name, faiths, on_call)
Features:   - Request a chaplain by faith tradition
            - Page the on-call chaplain for urgent end-of-life requests
            - Let chaplains accept and close requests
            - Record visits without clinical details
API:        REST
            POST /requests
            PATCH /requests/{id}
            GET  /requests/open
Storage:    PostgreSQL
Tech stack: Flutter, Java, Spring Boot
```

---

## Example 350

**Intent:**
interpreter booking for hospitals, video interpreter on demand

**Spec:**
```
Type:       Mobile application with backend (medical interpreting)
Auth:       Hospital SSO for staff; interpreter accounts
Data model: Interpreter(id, name, languages, certified, online)
            InterpretingCall(id, staff_id, language, started_at, ended_at, interpreter_id -> Interpreter)
Features:   - Request an interpreter by language with one tap
            - Connect a video call to the first available interpreter
            - Book in-person interpreters for scheduled appointments
            - Report minutes used per department
API:        REST
            POST /calls
            POST /bookings
            GET  /reports/minutes
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Twilio Video
```

---

## Example 351

**Intent:**
lice removal service home visits book lol my kids again

**Spec:**
```
Type:       Mobile application with backend (home lice treatment)
Auth:       Phone number + OTP
Data model: HouseholdBooking(id, address, people_count, slot, technician_id, status)
            FollowUp(id, booking_id -> HouseholdBooking, due_on, done)
Features:   - Book a discreet home visit by number of people
            - Pay per person
            - Schedule a free follow-up check after 7 days
            - Send prevention tips after the visit
API:        REST
            POST /bookings
            POST /bookings/{id}/follow-up
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 352

**Intent:**
key holding service: give spare keys to company, request emergency key drop when locked out

**Spec:**
```
Type:       Mobile application with backend (key holding)
Auth:       Email + password with security question
Data model: KeySet(id, customer_id, tag_number, address, safe_location)
            KeyRequest(id, keyset_id -> KeySet, deliver_to, status, requested_at)
Features:   - Register key sets with anonymous tag numbers
            - Request emergency delivery to the door
            - Authorise trusted contacts to request keys
            - Log every key movement
API:        REST
            POST /keysets
            POST /keysets/{id}/requests
            GET  /keysets/{id}/log
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI
```

---

## Example 353

**Intent:**
caravan park owner wants residents to report issues and pay site fees

**Spec:**
```
Type:       Mobile application with backend (caravan park residents)
Auth:       Email + password
Data model: Site(id, number, resident_id, monthly_fee)
            FeePayment(id, site_id -> Site, month, amount, paid_at)
            SiteIssue(id, site_id -> Site, description, photo_url, status)
Features:   - Pay monthly site fees
            - Report issues with photos
            - Receive park notices like water shutoffs
            - Book the shared laundry and BBQ
API:        REST
            POST /fees/pay
            POST /issues
            GET  /notices
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Stripe
```

---

## Example 354

**Intent:**
houseboat moorings: boaters register stay, rangers check overstays

**Spec:**
```
Type:       Mobile application with backend (canal mooring)
Auth:       Boat licence number + email
Data model: Mooring(id, name, max_stay_days, lat, lng)
            MooringStay(id, mooring_id -> Mooring, boat_id, arrived_on, left_on)
            Boat(id, licence_number, name)
Features:   - Check in at a mooring with GPS
            - Warn when the maximum stay is near
            - Let rangers see boats overstaying
            - Show water points and pump-outs
API:        REST
            POST /stays
            GET  /moorings/{id}/overstays
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Go
```

---

## Example 355

**Intent:**
real estate agent team: who has keys to which property now

**Spec:**
```
Type:       Mobile application with backend (property key tracking)
Auth:       Company email + password
Data model: Property(id, address, key_tag)
            KeyCheckout(id, property_id -> Property, agent_id, out_at, due_back_at, returned_at)
Features:   - Scan a key tag to check it out
            - Show who holds each key right now
            - Remind agents of overdue keys
            - Keep a full key history per property
API:        REST
            POST /checkouts
            PATCH /checkouts/{id}/return
            GET  /properties/{id}/history
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 356

**Intent:**
students submit lab reports photos and TA grades on tablet, with stylus comments

**Spec:**
```
Type:       Mobile application with backend (lab report grading)
Auth:       University SSO
Data model: Assignment(id, course_id, title, due_at, rubric_json)
            Submission(id, assignment_id -> Assignment, student_id, pages_urls, submitted_at)
            Grade(id, submission_id -> Submission, ta_id, score, annotated_pdf_url)
Features:   - Photograph and submit lab notebook pages as one PDF
            - Annotate submissions with a stylus on a tablet
            - Score with a rubric
            - Return graded PDFs to students
API:        REST
            POST /assignments/{id}/submissions
            POST /submissions/{id}/grade
            GET  /submissions/{id}
Storage:    PostgreSQL, S3
Tech stack: Swift (iPadOS), PencilKit, Python, Django
```

---

## Example 357

**Intent:**
plant nursery delivery trees and big pots, slot booking

**Spec:**
```
Type:       Mobile application with backend (garden centre delivery)
Auth:       Email + password
Data model: Plant(id, name, pot_size, price, stock)
            GardenOrder(id, customer_id, items, delivery_slot, needs_two_people, status)
Features:   - Order plants and large pots
            - Choose a delivery slot sized to the load
            - Add planting service
            - Notify on delivery day
API:        REST
            GET  /plants
            GET  /slots?load={l}
            POST /orders
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---
## Example 358

**Intent:**
vet video call app for pet owners at night when clinic closed

**Spec:**
```
Type:       Mobile application with backend (veterinary telehealth)
Auth:       Email + password
Data model: Pet(id, owner_id, name, species, age, weight_kg)
            VetConsult(id, pet_id -> Pet, vet_id, symptoms, started_at, advice, fee)
Features:   - Describe symptoms and upload photos or video
            - Connect to an available vet by video
            - Pay a fixed consult fee
            - Send the consult summary to the regular clinic
API:        REST
            POST /consults
            POST /consults/{id}/join
            GET  /consults/{id}/summary
Storage:    PostgreSQL, S3
Tech stack: Flutter, Node.js, Agora, Stripe
```

---

## Example 359

**Intent:**
skin doctor app send photo of mole and dermatologist answer in 48h

**Spec:**
```
Type:       Mobile application with backend (teledermatology)
Auth:       Email + password with two-factor authentication
Data model: Case(id, patient_id, body_location, duration, symptoms, status)
            CasePhoto(id, case_id -> Case, url, distance)
            Assessment(id, case_id -> Case, dermatologist_id, diagnosis, urgency, advice)
Features:   - Guide the patient to take close-up and distance photos
            - Submit a case with symptom questions
            - Let dermatologists answer within 48 hours
            - Flag urgent cases for in-person referral
API:        REST
            POST /cases
            POST /cases/{id}/photos
            POST /cases/{id}/assessment
Storage:    PostgreSQL (encrypted), S3
Tech stack: React Native, Python, Django
```

---

## Example 360

**Intent:**
pharmacy delivers prescriptions to home same day, driver needs signature

**Spec:**
```
Type:       Mobile application with backend (prescription delivery)
Auth:       Patient phone + date of birth; driver login
Data model: RxDelivery(id, patient_id, address, items, copay, slot, driver_id, status)
            ProofOfDelivery(id, delivery_id -> RxDelivery, signature_url, id_checked, at)
Features:   - Request delivery when a prescription is ready
            - Pay copay in the app
            - Require signature and ID check for controlled drugs
            - Keep medicines in a cold-chain log when needed
API:        REST
            POST /deliveries
            POST /deliveries/{id}/pod
            GET  /deliveries/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Java, Spring Boot
```

---

## Example 361

**Intent:**
free tax help volunteers book appointments with low income families

**Spec:**
```
Type:       Mobile application with backend (volunteer tax clinic)
Auth:       Phone number + OTP for clients; volunteer email login
Data model: TaxSite(id, name, address)
            TaxAppointment(id, site_id -> TaxSite, client_name, phone, starts_at, docs_needed, status)
            Preparer(id, name, certified_level)
Features:   - Book an appointment at a tax site
            - Show a checklist of documents to bring
            - Assign certified preparers by return complexity
            - Send reminders by SMS
API:        REST
            GET  /sites/{id}/slots
            POST /appointments
            PATCH /appointments/{id}/assign
Storage:    PostgreSQL
Tech stack: React Native, Django, Twilio
```

---

## Example 362

**Intent:**
flood coming, sandbag pickup points and volunteers to fill bags

**Spec:**
```
Type:       Mobile application with backend (flood sandbag coordination)
Auth:       Phone number + OTP
Data model: SandbagPoint(id, name, lat, lng, bags_available, open)
            FillShift(id, point_id -> SandbagPoint, starts_at, volunteers_needed)
            ShiftVolunteer(id, shift_id -> FillShift, phone)
Features:   - Show sandbag points with stock on a map
            - Sign up for filling shifts
            - Update bag counts from the site
            - Push river level warnings
API:        REST
            GET  /points
            PATCH /points/{id}/stock
            POST /shifts/{id}/volunteers
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 363

**Intent:**
shelters post found animals so owners can check if their pet is there

**Spec:**
```
Type:       Mobile application with backend (found pets registry)
Auth:       Shelter staff accounts; owners browse without login
Data model: FoundAnimal(id, shelter_id, species, colour, sex, found_area, intake_on, photo_url, microchip)
            Shelter(id, name, phone, address)
            OwnerAlert(id, email, species, area, colour)
Features:   - Post found animals at intake
            - Search by species, colour and area
            - Alert owners when a matching animal is posted
            - Look up a microchip number
API:        REST
            POST /found-animals
            GET  /found-animals?species={s}&area={a}
            POST /owner-alerts
Storage:    PostgreSQL, S3
Tech stack: React Native, Ruby on Rails
```

---

## Example 364

**Intent:**
sell my football tickets to other fans of same club, club approves

**Spec:**
```
Type:       Mobile application with backend (club ticket exchange)
Auth:       Club membership number + password
Data model: MatchTicket(id, member_id, match_id, seat, face_value)
            ExchangeListing(id, ticket_id -> MatchTicket, price, status)
            ExchangeSale(id, listing_id -> ExchangeListing, buyer_member_id, at)
Features:   - List a ticket at face value only
            - Allow purchases only by club members
            - Reissue the ticket in the buyer's name
            - Pay the seller after the match
API:        REST
            POST /listings
            GET  /matches/{id}/listings
            POST /listings/{id}/buy
Storage:    PostgreSQL
Tech stack: Flutter, Java, Spring Boot
```

---

## Example 365

**Intent:**
hey can u make app where my bootcamp outdoor fitness classes in park get booked, cancel if rain

**Spec:**
```
Type:       Mobile application with backend (outdoor fitness classes)
Auth:       Email + password
Data model: ParkClass(id, park, starts_at, capacity, status)
            ClassBooking(id, class_id -> ParkClass, member_id)
Features:   - Book a spot in park classes
            - Check the rain forecast 2 hours before
            - Cancel and notify everyone when rain is likely
            - Track attendance streaks
API:        REST
            GET  /classes
            POST /classes/{id}/book
            POST /classes/{id}/cancel
Storage:    PostgreSQL
Tech stack: React Native, Node.js, OpenWeatherMap API
```

---

## Example 366

**Intent:**
students tutoring at home need tutor agency app: match, schedule, parents pay agency

**Spec:**
```
Type:       Mobile application with backend (tutoring agency)
Auth:       Email + password for parents and tutors
Data model: TutorProfile(id, name, subjects, grades, area)
            Placement(id, student_name, parent_id, tutor_id -> TutorProfile, subject, weekly_hours)
            TutorLesson(id, placement_id -> Placement, date, hours, notes, confirmed)
Features:   - Match tutors by subject, grade and area
            - Let tutors log lessons and notes
            - Let parents confirm lessons
            - Invoice parents monthly and pay tutors
API:        REST
            POST /placements
            POST /placements/{id}/lessons
            POST /lessons/{id}/confirm
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Stripe
```

---

## Example 367

**Intent:**
exam prep app for medical students where they book 1:1 sessions with residents

**Spec:**
```
Type:       Mobile application with backend (medical exam coaching)
Auth:       Email + password
Data model: Coach(id, name, specialty, score_percentile, rate)
            CoachingSession(id, coach_id -> Coach, student_id, starts_at, topic, status)
Features:   - Browse coaches by specialty and exam score
            - Book a video session
            - Share question bank stats before the session
            - Pay per session
API:        REST
            GET  /coaches
            POST /sessions
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Zoom SDK, Stripe
```

---

## Example 368

**Intent:**
Telehealth for rural farmers, they have bad internet, so audio only call with doctor and SMS prescriptions

**Spec:**
```
Type:       Mobile application with backend (low-bandwidth telehealth)
Auth:       Phone number + OTP
Data model: Patient(id, name, phone, village)
            AudioConsult(id, patient_id -> Patient, doctor_id, requested_at, called_at, notes)
            SmsPrescription(id, consult_id -> AudioConsult, text, pharmacy_code)
Features:   - Request a callback from a doctor
            - Connect an audio-only call over the phone network
            - Send the prescription by SMS with a pharmacy code
            - Work on low-end Android phones
API:        REST
            POST /consults
            POST /consults/{id}/prescription
Storage:    PostgreSQL
Tech stack: Kotlin (Android Go), Python, Django, Twilio Voice
```

---

## Example 369

**Intent:**
gym class booking but for climbing gym yoga + intro courses, belay test required

**Spec:**
```
Type:       Mobile application with backend (climbing gym courses)
Auth:       Email + password, waiver signed
Data model: Course(id, kind, starts_at, capacity, prerequisite)
            CourseBooking(id, course_id -> Course, member_id)
            BelayCert(id, member_id, passed_on, staff_id)
Features:   - Book yoga, intro and lead courses
            - Require belay certification for lead classes
            - Record belay test results
            - Sign the waiver in the app
API:        REST
            POST /courses/{id}/book
            POST /belay-certs
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 370

**Intent:**
barber chain wants loyalty points + book across all 8 shops

**Spec:**
```
Type:       Mobile application with backend (barber chain booking)
Auth:       Phone number + OTP
Data model: Shop(id, name, address)
            Barber(id, shop_id -> Shop, name)
            Booking(id, barber_id -> Barber, client_id, starts_at, service)
            Points(client_id, balance)
Features:   - Book at any shop with any barber
            - Earn points per visit
            - Redeem points for a free cut
            - Let shop managers see their bookings
API:        REST
            GET  /shops/{id}/slots
            POST /bookings
            POST /points/redeem
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 371

**Intent:**
church small business directory so members support each other

**Spec:**
```
Type:       Mobile application with backend (congregation business directory)
Auth:       Email + password, member approval
Data model: Business(id, owner_member_id, name, category, phone, website, description)
            Recommendation(id, business_id -> Business, member_id, text)
Features:   - List member-owned businesses by category
            - Search and call or visit websites
            - Recommend a business to others
            - Approve listings before publishing
API:        REST
            GET  /businesses?category={c}
            POST /businesses
            POST /businesses/{id}/recommendations
Storage:    PostgreSQL
Tech stack: Flutter, Firebase
```

---

## Example 372

**Intent:**
neighborhood watch patrol volunteers log route walked tonight

**Spec:**
```
Type:       Mobile application with backend (citizen patrol log)
Auth:       Email + password, coordinator approval
Data model: Patrol(id, started_at, ended_at, member_ids, gps_track)
            Observation(id, patrol_id -> Patrol, note, lat, lng, at)
Features:   - Start a patrol and record the walked route
            - Log observations with location
            - Show patrol coverage on a heatmap
            - Share a nightly summary with members
API:        REST
            POST /patrols
            POST /patrols/{id}/observations
            GET  /coverage
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Python, FastAPI
```

---

## Example 373

**Intent:**
appt for car tyre change seasonal swap, tyres stored at shop

**Spec:**
```
Type:       Mobile application with backend (tyre hotel)
Auth:       Email + password
Data model: Vehicle(id, customer_id, plate)
            TyreSet(id, vehicle_id -> Vehicle, season, rack_location, tread_mm)
            SwapAppointment(id, vehicle_id -> Vehicle, starts_at, status)
Features:   - Book a seasonal tyre swap
            - Show where stored tyres are and their tread depth
            - Recommend replacement under 4 mm
            - Remind customers in autumn and spring
API:        REST
            POST /appointments
            GET  /vehicles/{id}/tyres
Storage:    PostgreSQL
Tech stack: Flutter, Django
```

---

## Example 374

**Intent:**
mobile car mechanic come to house oil change

**Spec:**
```
Type:       Mobile application with backend (mobile mechanic)
Auth:       Phone number + OTP
Data model: Car(id, owner_id, make, model, year)
            ServiceRequest(id, car_id -> Car, service, address, slot, mechanic_id, quote, status)
Features:   - Choose service and get an instant quote
            - Book a home or work visit
            - Approve extra work found during the visit
            - Pay and keep the service history
API:        REST
            POST /requests
            POST /requests/{id}/approve-extra
            GET  /cars/{id}/history
Storage:    PostgreSQL
Tech stack: React Native, Laravel, Stripe
```

---

## Example 375

**Intent:**
coin laundromat owner wants to see revenue per machine on phone

**Spec:**
```
Type:       Mobile application with backend (laundromat revenue)
Auth:       Owner email + password
Data model: Machine(id, store_id, kind, number)
            CycleEvent(id, machine_id -> Machine, amount, at)
            ErrorEvent(id, machine_id -> Machine, code, at)
Features:   - Collect cycle and payment events from machines
            - Show revenue per machine and store
            - Alert the owner on machine errors
            - Compare this month with last month
API:        REST
            POST /events
            GET  /stores/{id}/revenue
Storage:    PostgreSQL
Tech stack: Flutter, Go, MQTT
```

---

## Example 376

**Intent:**
ambulance crews need app to see hospital ED capacity before choosing hospital

**Spec:**
```
Type:       Mobile application with backend (ED capacity for EMS)
Auth:       EMS agency login
Data model: Hospital(id, name, lat, lng, specialties)
            CapacityStatus(id, hospital_id -> Hospital, ed_status, trauma_open, stroke_open, updated_at)
            Prenotification(id, hospital_id -> Hospital, unit, eta_min, complaint)
Features:   - Show ED status and specialty availability
            - Send a pre-arrival notice to the chosen hospital
            - Show travel times from the crew's position
            - Let hospitals update status quickly
API:        REST
            GET  /hospitals/status
            PUT  /hospitals/{id}/status
            POST /prenotifications
Storage:    PostgreSQL
Tech stack: Kotlin, Java, Spring Boot
```

---

## Example 377

**Intent:**
community first responders get alert when someone nearby has cardiac arrest, AED locations

**Spec:**
```
Type:       Mobile application with backend (cardiac arrest responder alerts)
Auth:       Email + password, CPR certificate verified
Data model: Responder(id, name, cpr_expires, last_lat, last_lng, available)
            Aed(id, lat, lng, access_hours, status)
            Incident(id, lat, lng, created_at)
            ResponderDispatch(id, incident_id -> Incident, responder_id -> Responder, role, accepted)
Features:   - Receive incidents from the emergency dispatch system
            - Alert available responders within 500 m
            - Send some responders to fetch the nearest AED
            - Show AED locations on a map
API:        REST
            POST /incidents
            POST /dispatches/{id}/accept
            GET  /aeds
Storage:    PostgreSQL with PostGIS
Tech stack: Swift, Kotlin, Go, critical alerts push
```

---

## Example 378

**Intent:**
seed library at our public library, borrow seeds and return seeds from harvest

**Spec:**
```
Type:       Mobile application with backend (seed library)
Auth:       Library card number
Data model: SeedPacket(id, variety, plant_type, stock)
            SeedLoan(id, packet_id -> SeedPacket, patron_id, borrowed_on)
            SeedReturn(id, packet_id -> SeedPacket, patron_id, grown_location, returned_on)
Features:   - Browse seed varieties in stock
            - Reserve packets for pickup
            - Log seed returns after harvest
            - Show growing tips per variety
API:        REST
            GET  /seeds
            POST /seeds/{id}/loan
            POST /seeds/{id}/return
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 379

**Intent:**
Uni app built with Kotlin Multiplatform where students see exam timetable and seat number

**Spec:**
```
Type:       Mobile application with backend (exam timetable)
Auth:       University SSO
Data model: Exam(id, course_code, starts_at, duration_min, room)
            SeatAssignment(id, exam_id -> Exam, student_id, seat)
Features:   - Show the student's personal exam timetable
            - Show the room and seat number
            - Notify about room changes
            - Show what items are allowed in the exam
API:        REST
            GET  /exams/mine
            GET  /exams/{id}/seat
Storage:    PostgreSQL
Tech stack: Kotlin Multiplatform, Compose Multiplatform, Ktor
```

---

## Example 380

**Intent:**
shared kitchen for food startups book cooking stations by hour

**Spec:**
```
Type:       Mobile application with backend (commissary kitchen booking)
Auth:       Email + password, food hygiene certificate uploaded
Data model: Station(id, name, equipment)
            KitchenBooking(id, station_id -> Station, member_id, starts_at, ends_at)
            StorageShelf(id, member_id, kind)
Features:   - Book stations and equipment by the hour
            - Rent cold and dry storage shelves
            - Require valid hygiene certificates
            - Log cleaning checklist after each booking
API:        REST
            POST /bookings
            POST /bookings/{id}/cleaning
            POST /certificates
Storage:    PostgreSQL, S3
Tech stack: Flutter, Node.js
```

---

## Example 381

**Intent:**
farm stay booking and kids can feed animals activity slots

**Spec:**
```
Type:       Mobile application with backend (farm stay)
Auth:       Email + password
Data model: Cabin(id, name, sleeps, nightly_rate)
            CabinStay(id, cabin_id -> Cabin, guest_id, arrive_on, depart_on)
            FarmActivity(id, title, starts_at, places)
            ActivitySpot(id, activity_id -> FarmActivity, stay_id -> CabinStay, kids)
Features:   - Book cabins
            - Reserve activities like feeding animals and egg collecting
            - Order farm produce boxes for arrival
            - Send check-in details
API:        REST
            POST /stays
            POST /activities/{id}/spots
Storage:    PostgreSQL
Tech stack: React Native, Django, Stripe
```

---

## Example 382

**Intent:**
church youth group trip signups and medical forms

**Spec:**
```
Type:       Mobile application with backend (youth group trips)
Auth:       Parent email + password
Data model: Youth(id, parent_id, name, grade)
            YouthTrip(id, title, departs_at, returns_at, cost, spots)
            MedicalForm(id, youth_id -> Youth, allergies, medications, emergency_contact, signed_at)
Features:   - Sign up teens for trips
            - Complete and sign medical forms once per year
            - Pay trip costs with scholarships applied
            - Give leaders offline access to medical info
API:        REST
            POST /trips/{id}/signups
            PUT  /youth/{id}/medical
Storage:    PostgreSQL
Tech stack: Flutter, Supabase, Stripe
```

---

## Example 383

**Intent:**
ice cream truck where is it now kids want to know

**Spec:**
```
Type:       Mobile application with backend (ice cream truck tracker)
Auth:       Driver login
Data model: Truck(id, name, lat, lng, on_duty, updated_at)
            StreetRequest(id, street, lat, lng, votes, date)
Features:   - Share the truck's live location while on duty
            - Show the truck on a map for families
            - Notify when the truck is within 500 m
            - Let families vote for streets to visit
API:        REST + WebSocket
            POST /trucks/{id}/location
            WS   /trucks/live
            POST /street-requests
Storage:    Redis, PostgreSQL
Tech stack: React Native, Node.js
```

---
## Example 384

**Intent:**
i want to build an app in flutter for hospital visitors to order flowers and gifts delivered to patient room from the gift shop

**Spec:**
```
Type:       Mobile application with backend (hospital gift shop delivery)
Auth:       Email + password or guest checkout
Data model: GiftItem(id, name, category, price, stock, allowed_in_icu)
            GiftOrder(id, patient_name, ward, room, items, card_message, status)
Features:   - Browse flowers, balloons and gifts
            - Block items not allowed in intensive care wards
            - Add a card message
            - Let volunteers deliver and mark orders done
API:        REST
            GET  /items?ward={w}
            POST /orders
            PATCH /orders/{id}/delivered
Storage:    PostgreSQL
Tech stack: Flutter, Dart Frog
```

---

## Example 385

**Intent:**
student union bar app order drinks to table, ID check once

**Spec:**
```
Type:       Mobile application with backend (student bar ordering)
Auth:       University SSO plus one-time ID age verification
Data model: Drink(id, name, price, alcoholic)
            BarOrder(id, student_id, table_number, items, total, status)
Features:   - Verify age once by scanning ID at the bar
            - Order to a table number
            - Block alcohol for unverified accounts
            - Show bar staff an order queue
API:        REST
            GET  /menu
            POST /orders
            PATCH /orders/{id}
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe
```

---

## Example 386

**Intent:**
temple volunteers for festival kitchen and parking, plus donate materials

**Spec:**
```
Type:       Mobile application with backend (temple festival volunteers)
Auth:       Phone number + OTP
Data model: FestivalTask(id, festival, area, starts_at, needed)
            TaskSignup(id, task_id -> FestivalTask, volunteer_id)
            MaterialPledge(id, item, quantity, donor_id, delivered)
Features:   - Sign up for kitchen, parking or cleaning shifts
            - Pledge materials like rice, oil and flowers
            - Show organisers what is still needed
            - Send reminders before each shift
API:        REST
            POST /tasks/{id}/signups
            POST /pledges
            GET  /needs
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 387

**Intent:**
students borrow laptops and chargers from IT desk, app shows what available

**Spec:**
```
Type:       Mobile application with backend (campus equipment loans)
Auth:       University SSO
Data model: Device(id, kind, asset_tag, status)
            DeviceLoan(id, device_id -> Device, student_id, out_at, due_at, returned_at)
Features:   - Show available laptops, chargers and cameras
            - Reserve for pickup within 1 hour
            - Scan asset tags at checkout and return
            - Charge fines for late returns
API:        REST
            GET  /devices/available
            POST /loans
            PATCH /loans/{id}/return
Storage:    PostgreSQL
Tech stack: Flutter, Django
```

---

## Example 388

**Intent:**
hospital staff find free parking + shuttle from remote lot

**Spec:**
```
Type:       Mobile application with backend (staff parking and shuttle)
Auth:       Hospital SSO
Data model: StaffLot(id, name, spaces, occupied)
            ShuttleBus(id, lat, lng, route)
Features:   - Show free spaces in staff lots
            - Track the remote-lot shuttle live
            - Notify night shift staff of security escort availability
            - Show permit status
API:        REST
            GET  /lots
            GET  /shuttles/live
Storage:    PostgreSQL, Redis
Tech stack: React Native, Go
```

---

## Example 389

**Intent:**
a lot of people in my building want to share a car, book it by hour

**Spec:**
```
Type:       Mobile application with backend (residential car sharing)
Auth:       Email + password with licence check
Data model: SharedCar(id, plate, model, parking_spot, keybox_id)
            CarBooking(id, car_id -> SharedCar, resident_id, starts_at, ends_at, km_start, km_end)
            FuelLog(id, booking_id -> CarBooking, litres, cost)
Features:   - Book the shared car by the hour
            - Open the key box from the app during the booking
            - Record kilometres and split costs monthly
            - Report damage with photos
API:        REST
            POST /bookings
            POST /bookings/{id}/keybox
            GET  /costs?month={m}
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 390

**Intent:**
snowmobile trail permits and trail grooming status

**Spec:**
```
Type:       Mobile application with backend (snowmobile trails)
Auth:       Email + password
Data model: TrailPermit(id, rider_id, sled_registration, season, qr_token)
            TrailSegment(id, name, status, groomed_at, geojson)
Features:   - Buy a seasonal trail permit
            - Show groomed and closed trail segments
            - Download maps offline
            - Show permit QR to trail wardens
API:        REST
            POST /permits
            GET  /segments
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Python, FastAPI
```

---

## Example 391

**Intent:**
day care for adults with dementia, families see daily activities and meals

**Spec:**
```
Type:       Mobile application with backend (adult day care)
Auth:       Family email + password
Data model: Participant(id, name, family_id, dietary_needs)
            DailyNote(id, participant_id -> Participant, date, meals, activities, mood, photos)
            AttendanceDay(id, participant_id -> Participant, date, picked_up_by)
Features:   - Share a daily note with meals, activities and mood
            - Book extra days
            - Record who picked the participant up
            - Message staff
API:        REST
            GET  /participants/{id}/notes
            POST /attendance
            POST /messages
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 392

**Intent:**
hospital discharge app gives patient their meds list and follow-up appointments

**Spec:**
```
Type:       Mobile application with backend (discharge instructions)
Auth:       Patient code from discharge papers + date of birth
Data model: Discharge(id, patient_id, discharged_on, diagnosis_summary)
            DischargeMed(id, discharge_id -> Discharge, drug, dose, schedule, new_or_changed)
            FollowUpAppt(id, discharge_id -> Discharge, clinic, starts_at)
Features:   - Show the medication list highlighting new or changed drugs
            - Remind follow-up appointments
            - Show warning signs to return to hospital
            - Ask a nurse question within 7 days
API:        REST
            GET  /discharges/{code}
            POST /discharges/{id}/questions
Storage:    PostgreSQL (encrypted)
Tech stack: React Native, C#, ASP.NET Core
```

---

## Example 393

**Intent:**
want app where neighbors share extra fruit from their trees

**Spec:**
```
Type:       Mobile application with backend (backyard fruit sharing)
Auth:       Email + password
Data model: FruitPost(id, owner_id, fruit, quantity, lat, lng, pickup_until, photo_url)
            PickRequest(id, post_id -> FruitPost, requester_id, status)
Features:   - Post extra fruit with pickup window
            - Find fruit nearby on a map
            - Request to pick and agree a time
            - Show approximate location until approved
API:        REST
            POST /posts
            GET  /posts/nearby
            POST /posts/{id}/requests
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Supabase
```

---

## Example 394

**Intent:**
gleaning volunteers harvest leftover crops on farms for food banks

**Spec:**
```
Type:       Mobile application with backend (farm gleaning)
Auth:       Email + password, waiver signed
Data model: GleanEvent(id, farm, crop, date, volunteers_needed)
            GleanSignup(id, event_id -> GleanEvent, volunteer_id)
            Harvest(id, event_id -> GleanEvent, kg, food_bank)
Features:   - Let farms post gleaning opportunities at short notice
            - Alert volunteers by text
            - Record kilos harvested per food bank
            - Show yearly impact
API:        REST
            POST /events
            POST /events/{id}/signups
            POST /events/{id}/harvest
Storage:    PostgreSQL
Tech stack: Flutter, Django, Twilio
```

---

## Example 395

**Intent:**
small island tourist office wants app with ferry times, beaches, and emergency info offline

**Spec:**
```
Type:       Mobile application with backend (island visitor guide)
Auth:       Editor login for the tourist office
Data model: FerryTime(id, route, departs_at, days)
            Place(id, kind, name, lat, lng, description)
            EmergencyContact(id, name, phone)
Features:   - Show ferry timetables
            - List beaches, restaurants and viewpoints on an offline map
            - Show emergency contacts and nearest clinic
            - Push notices like ferry cancellations
API:        REST
            GET  /bundle
            POST /notices
Storage:    PostgreSQL, on-device cache
Tech stack: Flutter, Node.js, Mapbox offline
```

---

## Example 396

**Intent:**
caves tour booking, helmets sizes, minimum age

**Spec:**
```
Type:       Mobile application with backend (cave tours)
Auth:       Email + password
Data model: CaveTour(id, name, starts_at, min_age, capacity)
            CaveBooking(id, tour_id -> CaveTour, contact_id, participants_json)
Features:   - Book tours with participant ages and sizes
            - Block participants under the minimum age
            - Send what-to-wear instructions
            - Cancel tours after heavy rain
API:        REST
            GET  /tours
            POST /bookings
Storage:    PostgreSQL
Tech stack: React Native, Laravel
```

---

## Example 397

**Intent:**
church app for prayer chain, request prayer, people commit to pray

**Spec:**
```
Type:       Mobile application with backend (prayer chain)
Auth:       Email + password
Data model: PrayerRequest(id, author_id, text, anonymous, visibility, created_at)
            PrayerCommit(id, request_id -> PrayerRequest, member_id, at)
Features:   - Post a prayer request, optionally anonymous
            - Choose pastors only or whole church visibility
            - Tap to commit to pray and notify the requester
            - Archive requests after 30 days
API:        REST
            POST /requests
            POST /requests/{id}/commit
            GET  /requests
Storage:    PostgreSQL
Tech stack: Flutter, Firebase
```

---

## Example 398

**Intent:**
students in residence report roommate conflicts to RA privately

**Spec:**
```
Type:       Mobile application with backend (resident advisor reports)
Auth:       University SSO
Data model: ConcernReport(id, student_id, floor, category, description, status)
            RaMeeting(id, report_id -> ConcernReport, ra_id, starts_at, notes)
Features:   - Submit a private concern to the floor RA
            - Book a meeting with the RA
            - Escalate serious cases to residence life staff
            - Keep reports confidential to staff
API:        REST
            POST /reports
            POST /reports/{id}/meetings
            POST /reports/{id}/escalate
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI
```

---

## Example 399

**Intent:**
my friend has a sound bath / gong meditation studio, bookings and mat rentals

**Spec:**
```
Type:       Mobile application with backend (sound bath studio)
Auth:       Email + password
Data model: SoundSession(id, starts_at, capacity, price)
            SessionBooking(id, session_id -> SoundSession, client_id, mat_rental)
Features:   - Book sessions and rent a mat
            - Buy gift cards
            - Show a waitlist for full sessions
            - Send a post-session reflection prompt
API:        REST
            POST /sessions/{id}/book
            POST /gift-cards
Storage:    PostgreSQL
Tech stack: Flutter, Supabase, Stripe
```

---

## Example 400

**Intent:**
insurance agents in field sell policies on tablet and customer signs e-sign

**Spec:**
```
Type:       Mobile application with backend (field insurance sales)
Auth:       Agent SSO with device PIN
Data model: Prospect(id, name, phone, date_of_birth)
            PolicyApplication(id, prospect_id -> Prospect, product, premium, answers_json, status)
            ESignature(id, application_id -> PolicyApplication, image_url, signed_at)
Features:   - Quote premiums offline
            - Fill the application with health questions
            - Capture an e-signature and ID photo
            - Submit for underwriting when online
API:        REST
            POST /applications
            POST /applications/{id}/sign
            POST /applications/sync
Storage:    PostgreSQL, SQLite on device
Tech stack: .NET MAUI, ASP.NET Core
```

---

## Example 401

**Intent:**
inventory count app for church thrift shop donations

**Spec:**
```
Type:       Mobile application with backend (thrift shop inventory)
Auth:       Volunteer PIN
Data model: DonatedItem(id, category, description, price, photo_url, status, received_on)
            Sale(id, item_id -> DonatedItem, sold_at, amount)
Features:   - Log donated items with photos and price
            - Print price tags with barcodes
            - Mark items sold at the till
            - Mark down items unsold after 30 days
API:        REST
            POST /items
            POST /items/{id}/sell
            POST /items/markdown
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 402

**Intent:**
vet clinic wait - customers wait in car and get called in

**Spec:**
```
Type:       Mobile application with backend (curbside vet check-in)
Auth:       Phone number + OTP
Data model: VetVisit(id, pet_name, owner_phone, parking_spot, status, arrived_at)
Features:   - Check in from the car with parking spot number
            - Fill a symptom update form
            - Notify the owner when it is their turn
            - Let staff collect the pet curbside
API:        REST
            POST /visits/checkin
            PATCH /visits/{id}/call
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Twilio
```

---

## Example 403

**Intent:**
apartment complex pet registry so manager knows which dogs and vaccine dates

**Spec:**
```
Type:       Mobile application with backend (apartment pet registry)
Auth:       Resident email + password
Data model: Pet(id, unit, name, species, breed, weight_kg, rabies_valid_to, photo_url)
            PetFee(id, pet_id -> Pet, month, amount, paid)
Features:   - Register pets with vaccine certificates
            - Remind residents before vaccines expire
            - Charge monthly pet rent
            - Show staff a photo directory for lost pets
API:        REST
            POST /pets
            GET  /pets?unit={u}
            POST /pets/{id}/fees
Storage:    PostgreSQL, S3
Tech stack: React Native, Laravel
```

---

## Example 404

**Intent:**
uni sports facility booking, badminton courts and squash, students pay less

**Spec:**
```
Type:       Mobile application with backend (campus sports facilities)
Auth:       University SSO; public users by email
Data model: Facility(id, sport, name)
            Price(id, facility_id -> Facility, user_type, hourly)
            FacilityBooking(id, facility_id -> Facility, user_id, starts_at, price_paid)
Features:   - Book courts by sport and time
            - Apply student, staff or public prices
            - Open bookings 7 days ahead
            - Check in at reception with a QR code
API:        REST
            GET  /facilities/{id}/slots
            POST /bookings
Storage:    PostgreSQL
Tech stack: Flutter, Java, Spring Boot
```

---

## Example 405

**Intent:**
bridal shop fitting appointments and dress alteration tracking

**Spec:**
```
Type:       Mobile application with backend (bridal boutique)
Auth:       Email + password
Data model: Bride(id, name, wedding_date)
            DressOrder(id, bride_id -> Bride, dress, size, ordered_on, arrival_on)
            FittingAppointment(id, bride_id -> Bride, starts_at, number)
Features:   - Book try-on and fitting appointments
            - Track dress order arrival
            - Schedule fittings counting back from the wedding date
            - Share photos of try-on dresses
API:        REST
            POST /appointments
            GET  /orders/{id}
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 406

**Intent:**
we organise night markets monthly, vendors apply for stall and pay

**Spec:**
```
Type:       Mobile application with backend (night market stalls)
Auth:       Email + password
Data model: Market(id, date, location, stalls_total)
            StallApplication(id, market_id -> Market, vendor_id, category, needs_power, status)
            StallAssignment(id, application_id -> StallApplication, stall_number, paid)
Features:   - Apply for a stall at upcoming markets
            - Approve vendors balancing categories
            - Assign stall numbers and power
            - Collect stall fees
API:        REST
            POST /markets/{id}/applications
            PATCH /applications/{id}
            POST /assignments/{id}/pay
Storage:    PostgreSQL
Tech stack: Flutter, Django, Stripe
```

---

## Example 407

**Intent:**
pick your own strawberries farm, book a time to avoid crowds, pay by kilo

**Spec:**
```
Type:       Mobile application with backend (pick-your-own farm)
Auth:       Email or phone login
Data model: PickSlot(id, starts_at, capacity, crop)
            PickBooking(id, slot_id -> PickSlot, visitor_id, people)
            Weighing(id, booking_id -> PickBooking, kg, amount)
Features:   - Book a picking time slot
            - Show which crops are ripe this week
            - Weigh at exit and pay per kilo in the app
            - Cancel slots after rain
API:        REST
            GET  /slots
            POST /bookings
            POST /bookings/{id}/weigh
Storage:    PostgreSQL
Tech stack: React Native, Supabase, Stripe
```

---
## Example 408

**Intent:**
christmas tree farm pick and cut booking

**Spec:**
```
Type:       Mobile application with backend (Christmas tree farm)
Auth:       Email + password
Data model: VisitSlot(id, starts_at, cars_capacity)
            TreeVisit(id, slot_id -> VisitSlot, family_name, cars)
            TreeSale(id, visit_id -> TreeVisit, variety, height_m, price)
Features:   - Book an arrival slot to manage parking
            - Show available varieties and price per height
            - Pay for the tree at the netting station
            - Offer tree delivery for an extra fee
API:        REST
            GET  /slots
            POST /visits
            POST /visits/{id}/sale
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 409

**Intent:**
boarding school students sign out to town and back, staff see who out

**Spec:**
```
Type:       Mobile application with backend (boarding school sign-out)
Auth:       School SSO
Data model: Boarder(id, name, house, year)
            SignOut(id, boarder_id -> Boarder, destination, out_at, expected_back, back_at, approved_by)
Features:   - Request permission to leave campus
            - Let house staff approve by year group rules
            - Show who is currently out
            - Alert staff when a student is late back
API:        REST
            POST /sign-outs
            PATCH /sign-outs/{id}/approve
            GET  /sign-outs/active
Storage:    PostgreSQL
Tech stack: React Native, Django
```

---

## Example 410

**Intent:**
apartment building rooftop solar shares, residents see their part of production

**Spec:**
```
Type:       Mobile application with backend (shared rooftop solar)
Auth:       Resident email + password
Data model: Share(id, resident_id, unit, share_pct)
            ProductionReading(id, kwh, at)
            Credit(id, share_id -> Share, month, kwh, amount)
Features:   - Import production from the inverter API
            - Show each resident's share of production
            - Calculate monthly bill credits
            - Compare with weather and past months
API:        REST
            GET  /production?range={r}
            GET  /credits/mine
Storage:    PostgreSQL, TimescaleDB
Tech stack: Flutter, Python, FastAPI, SolarEdge API
```

---

## Example 411

**Intent:**
car boot sale sellers book pitch and buyers see whats being sold

**Spec:**
```
Type:       Mobile application with backend (car boot sale)
Auth:       Email + password for sellers
Data model: SaleDay(id, date, pitches_total)
            Pitch(id, day_id -> SaleDay, number, seller_id, paid)
            SellerPreview(id, pitch_id -> Pitch, photo_url, description)
Features:   - Book and pay for a pitch
            - Post preview photos of items
            - Let buyers browse previews by category
            - Cancel the day for bad weather with refunds
API:        REST
            POST /days/{id}/pitches
            POST /pitches/{id}/previews
            GET  /days/{id}/previews
Storage:    PostgreSQL, S3
Tech stack: React Native, Laravel, Stripe
```

---

## Example 412

**Intent:**
hospital needs app for blood sample couriers between clinics, temperature logged

**Spec:**
```
Type:       Mobile application with backend (specimen courier)
Auth:       Courier login
Data model: SpecimenBox(id, barcode, from_clinic, to_lab, status)
            CourierRun(id, courier_id, started_at, finished_at)
            TempLog(id, box_id -> SpecimenBox, celsius, at)
Features:   - Scan boxes at pickup and drop-off
            - Log box temperature from a Bluetooth sensor
            - Alert the lab when temperature leaves range
            - Show the lab expected arrivals
API:        REST
            POST /runs
            POST /boxes/{id}/scan
            POST /boxes/{id}/temps
Storage:    PostgreSQL
Tech stack: Kotlin, BLE sensors, Go
```

---

## Example 413

**Intent:**
nursing home families book video calls with residents, staff help with ipad

**Spec:**
```
Type:       Mobile application with backend (care home video visits)
Auth:       Family email + password
Data model: Resident(id, name, room)
            VideoVisit(id, resident_id -> Resident, family_id, starts_at, status)
            StaffDevice(id, name, assigned_staff)
Features:   - Book a 20-minute video visit slot
            - Assign a staff tablet to each visit
            - Start the call from the family's phone
            - Send residents' activity photos to family
API:        REST
            GET  /residents/{id}/slots
            POST /visits
            POST /visits/{id}/start
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Jitsi
```

---

## Example 414

**Intent:**
apt complex package room, staff log packages with photo of label

**Spec:**
```
Type:       Mobile application with backend (package room log)
Auth:       Staff PIN; residents email
Data model: Package(id, unit, carrier, tracking, label_photo_url, logged_at, picked_up_at)
Features:   - Read unit number from the label photo with OCR
            - Notify residents of new packages
            - Record pickup with resident signature
            - Flag packages older than 7 days
API:        REST
            POST /packages
            POST /packages/{id}/pickup
            GET  /packages/old
Storage:    PostgreSQL, S3
Tech stack: React Native, Google Cloud Vision, Node.js
```

---

## Example 415

**Intent:**
Hi! I teach surf lessons on the beach and I lose track of bookings on WhatsApp. I'd like an app where people book a lesson time, choose board rental size, and I can cancel all lessons when waves are dangerous.

**Spec:**
```
Type:       Mobile application with backend (surf school)
Auth:       Email or phone login
Data model: SurfLesson(id, starts_at, level, capacity, status)
            LessonBooking(id, lesson_id -> SurfLesson, student_name, board_size, wetsuit_size)
Features:   - Book a lesson by level and time
            - Choose board and wetsuit sizes
            - Cancel a day's lessons and notify students
            - Show the surf forecast
API:        REST
            GET  /lessons
            POST /lessons/{id}/book
            POST /lessons/cancel-day
Storage:    PostgreSQL
Tech stack: Flutter, Supabase, Stormglass API
```

---

## Example 416

**Intent:**
kids birthday party venue booking with packages (pizza, cake, host)

**Spec:**
```
Type:       Mobile application with backend (party venue booking)
Auth:       Email + password
Data model: PartyPackage(id, name, max_kids, price, includes)
            PartyBooking(id, package_id -> PartyPackage, parent_id, child_name, date, start_time, kids)
            GuestRsvp(id, booking_id -> PartyBooking, child_name, allergies, attending)
Features:   - Book a party room with a package
            - Send digital invitations with RSVP
            - Collect allergy info from guests
            - Pay deposit and balance
API:        REST
            POST /bookings
            POST /bookings/{id}/rsvps
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe
```

---

## Example 417

**Intent:**
app for lifeguards at pools to log incidents and water tests

**Spec:**
```
Type:       Mobile application with backend (lifeguard logs)
Auth:       Staff PIN
Data model: PoolSite(id, name)
            WaterCheck(id, site_id -> PoolSite, chlorine, ph, at, staff_id)
            IncidentReport(id, site_id -> PoolSite, kind, description, first_aid_given, at)
Features:   - Log water tests every 2 hours with reminders
            - Record incidents and first aid
            - Alert the manager on out-of-range readings
            - Export logs for health inspections
API:        REST
            POST /checks
            POST /incidents
            GET  /sites/{id}/export
Storage:    PostgreSQL
Tech stack: Flutter, Django
```

---

## Example 418

**Intent:**
church live stream viewers can check in online and give

**Spec:**
```
Type:       Mobile application with backend (online church service)
Auth:       Optional email login
Data model: Stream(id, title, starts_at, video_id)
            OnlineCheckIn(id, stream_id -> Stream, name, email, first_time)
            Gift(id, stream_id -> Stream, amount, fund)
Features:   - Watch the live service
            - Check in as an online attendee
            - Give during the service
            - Follow up with first-time visitors by email
API:        REST
            GET  /streams/live
            POST /streams/{id}/checkins
            POST /gifts
Storage:    PostgreSQL
Tech stack: React Native, Node.js, YouTube Live API, Stripe
```

---

## Example 419

**Intent:**
tram museum heritage rides tickets and volunteer driver rota

**Spec:**
```
Type:       Mobile application with backend (heritage tramway)
Auth:       Email + password
Data model: RideDay(id, date, trams_running)
            RideTicket(id, day_id -> RideDay, buyer_id, kind, qr_token)
            CrewShift(id, day_id -> RideDay, role, volunteer_id)
Features:   - Sell day tickets for heritage rides
            - Roster volunteer drivers and conductors
            - Require qualified drivers per tram
            - Scan tickets on board
API:        REST
            POST /tickets
            POST /crew-shifts
            POST /tickets/scan
Storage:    PostgreSQL
Tech stack: Flutter, Laravel
```

---

## Example 420

**Intent:**
rental bikes for tourists at hotels, hotel staff hands out, app tracks

**Spec:**
```
Type:       Mobile application with backend (hotel bike rental)
Auth:       Hotel staff login; guests by room number
Data model: HotelBike(id, hotel_id, frame_number, size, status)
            BikeRental(id, bike_id -> HotelBike, room_number, out_at, back_at, fee)
Features:   - Check bikes out and in by scanning a frame QR code
            - Charge rentals to the room
            - Suggest cycling routes from the hotel
            - Show bikes due for service
API:        REST
            POST /rentals
            PATCH /rentals/{id}/return
            GET  /bikes/service-due
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 421

**Intent:**
mobile app for HOA pool: residents scan to enter, guests count

**Spec:**
```
Type:       Mobile application with backend (HOA pool access)
Auth:       Resident email + password
Data model: Household(id, address, dues_paid)
            PoolEntry(id, household_id -> Household, residents, guests, at)
Features:   - Show a QR pass for households with paid dues
            - Let the attendant scan and record guest counts
            - Limit guests per household per day
            - Show live pool occupancy
API:        REST
            GET  /passes/mine
            POST /entries
            GET  /occupancy
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 422

**Intent:**
ATV tour company waivers and video of rules before ride

**Spec:**
```
Type:       Mobile application with backend (ATV tours)
Auth:       Email + password
Data model: AtvTour(id, starts_at, vehicles, price)
            Rider(id, booking_id, name, age, licence_number)
            AtvBooking(id, tour_id -> AtvTour, contact_id, vehicles)
Features:   - Book vehicles on a tour
            - Require each rider to watch a safety video
            - Sign waivers per rider
            - Check licences for drivers
API:        REST
            POST /bookings
            POST /bookings/{id}/riders
Storage:    PostgreSQL
Tech stack: React Native, Django, Stripe
```

---

## Example 423

**Intent:**
emergency vet triage app tell you if go to ER or wait, then book

**Spec:**
```
Type:       Mobile application with backend (pet symptom triage)
Auth:       Email + password
Data model: TriageSession(id, pet_id, answers_json, result, at)
            ErVisit(id, session_id -> TriageSession, clinic_id, eta)
Features:   - Ask symptom questions with branching logic
            - Recommend emergency, same-day or home care
            - Find the nearest open emergency vet
            - Send triage answers to the clinic before arrival
API:        REST
            POST /triage
            GET  /clinics/open
            POST /er-visits
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 424

**Intent:**
wedding guests upload photos to shared album through app, couple downloads all

**Spec:**
```
Type:       Mobile application with backend (event photo album)
Auth:       Event code; couple email + password
Data model: Album(id, event_name, code, owner_id)
            Photo(id, album_id -> Album, uploader_name, url, taken_at)
Features:   - Join an album with a code
            - Upload photos and videos in full quality
            - Show a live slideshow on a screen
            - Download everything as a zip
API:        REST
            POST /albums/join
            POST /albums/{id}/photos
            GET  /albums/{id}/download
Storage:    PostgreSQL, S3
Tech stack: React Native, Node.js
```

---

## Example 425

**Intent:**
field app for water well technicians record pump tests in villages offline

**Spec:**
```
Type:       Mobile application with backend (water point maintenance)
Auth:       Technician login
Data model: WaterPoint(id, village, lat, lng, pump_type, status)
            PumpTest(id, water_point_id -> WaterPoint, flow_lpm, water_quality, repaired_parts, at)
Features:   - Download water points for the district offline
            - Record flow tests, water quality and repairs
            - Mark points broken or working
            - Sync and show a map of functional points
API:        REST
            GET  /water-points?district={d}
            POST /sync
Storage:    PostgreSQL with PostGIS, SQLite on device
Tech stack: Kotlin (Android), Python, Django
```

---

## Example 426

**Intent:**
real estate open house app for buyers: see which homes open this weekend near me

**Spec:**
```
Type:       Mobile application with backend (open house finder)
Auth:       Optional email login for saved homes
Data model: OpenHouseEvent(id, listing_id, starts_at, ends_at)
            ListingSummary(id, address, price, beds, lat, lng, photo_url)
            SavedHome(id, user_id, listing_id -> ListingSummary)
Features:   - Show this weekend's open houses on a map
            - Plan a route through chosen open houses
            - Save homes and add notes
            - Import listings from the MLS feed nightly
API:        REST
            GET  /open-houses?bbox={b}&from={d}
            POST /saved
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Python, FastAPI, RESO Web API
```

---

## Example 427

**Intent:**
caretakers of a cemetery need app to look up plot owners and record burials

**Spec:**
```
Type:       Mobile application with backend (cemetery records)
Auth:       Staff login
Data model: Plot(id, section, row, number, owner_name, status)
            Burial(id, plot_id -> Plot, deceased_name, date)
Features:   - Look up plots by section or name
            - Record new burials
            - Show plot availability on a map
            - Track plot sales and maintenance
API:        REST
            GET  /plots?q={name}
            POST /plots/{id}/burials
Storage:    PostgreSQL
Tech stack: Flutter, Laravel
```

---
## Example 428

**Intent:**
uni chaplaincy and multi-faith prayer room booking

**Spec:**
```
Type:       Mobile application with backend (campus faith rooms)
Auth:       University SSO
Data model: FaithRoom(id, building, name, capacity, facilities)
            FaithRoomBooking(id, room_id -> FaithRoom, student_id, purpose, starts_at, ends_at)
Features:   - Show free prayer and quiet rooms
            - Book a room for group prayer
            - Keep drop-in times open for individuals
            - List chaplain office hours
API:        REST
            GET  /rooms/free
            POST /bookings
Storage:    PostgreSQL
Tech stack: React Native, Node.js
```

---

## Example 429

**Intent:**
hospital blood test results on phone with doctor comment

**Spec:**
```
Type:       Mobile application with backend (lab results portal)
Auth:       Patient ID + password with two-factor authentication
Data model: LabResult(id, patient_id, test, value, unit, ref_low, ref_high, released_at)
            DoctorComment(id, result_id -> LabResult, text, at)
Features:   - Show results with reference ranges
            - Hold results until a doctor releases them
            - Show the doctor's comment
            - Chart trends for repeated tests
API:        REST
            GET  /results
            GET  /results/{test}/trend
Storage:    PostgreSQL (encrypted), HL7 FHIR import
Tech stack: Flutter, Java, Spring Boot, HAPI FHIR
```

---

## Example 430

**Intent:**
caring for bees community, beekeepers report swarms, public reports swarm in their garden

**Spec:**
```
Type:       Mobile application with backend (swarm collection)
Auth:       Beekeepers email + password; public without login
Data model: SwarmReport(id, reporter_phone, lat, lng, height_m, photo_url, status, created_at)
            Beekeeper(id, name, phone, range_km, available)
Features:   - Let the public report a swarm with photo and location
            - Alert available beekeepers within range
            - Let a beekeeper claim the swarm
            - Notify the reporter who is coming
API:        REST
            POST /swarms
            POST /swarms/{id}/claim
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Supabase
```

---

## Example 431

**Intent:**
tool for mobile food inspectors at restaurants, score and photos, offline

**Spec:**
```
Type:       Mobile application with backend (food safety inspections)
Auth:       Inspector login
Data model: Establishment(id, name, address, risk_level)
            FoodInspection(id, establishment_id -> Establishment, inspector_id, score, at)
            Violation(id, inspection_id -> FoodInspection, code, severity, photo_url)
Features:   - Record violations from a code list
            - Calculate the inspection score
            - Work offline and sync later
            - Publish grades to the public website
API:        REST
            POST /inspections
            POST /inspections/{id}/violations
            POST /inspections/{id}/publish
Storage:    PostgreSQL, SQLite on device
Tech stack: .NET MAUI, ASP.NET Core
```

---

## Example 432

**Intent:**
app to rent camping gear like tents for weekend trips

**Spec:**
```
Type:       Mobile application with backend (camping gear rental)
Auth:       Email + password
Data model: GearItem(id, name, kind, daily_rate, stock)
            GearRental(id, customer_id, items, pickup_on, return_on, deposit, status)
Features:   - Browse tents, sleeping bags and stoves
            - Check stock for dates
            - Bundle kits for 2 or 4 people
            - Record cleaning and damage on return
API:        REST
            GET  /gear?from={d}&to={d}
            POST /rentals
            PATCH /rentals/{id}/return
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 433

**Intent:**
students order campus printing of posters big format and pickup

**Spec:**
```
Type:       Mobile application with backend (large-format print shop)
Auth:       University SSO
Data model: PosterOrder(id, student_id, file_url, size, paper, copies, price, status)
Features:   - Upload a PDF and choose size and paper
            - Preview and check resolution
            - Pay with department code or card
            - Notify when ready for pickup
API:        REST
            POST /orders
            GET  /orders/{id}
Storage:    PostgreSQL, S3
Tech stack: React Native, Python, FastAPI
```

---

## Example 434

**Intent:**
uhh some app for my apartment where we vote on stuff like painting the hallway

**Spec:**
```
Type:       Mobile application with backend (residents voting)
Auth:       Email + password, one vote per unit
Data model: Unit(id, number)
            Ballot(id, question, options, closes_at)
            BallotVote(id, ballot_id -> Ballot, unit_id -> Unit, option)
Features:   - Create a ballot with options and deadline
            - Allow one vote per unit
            - Show results when the ballot closes
            - Remind units that have not voted
API:        REST
            POST /ballots
            POST /ballots/{id}/votes
            GET  /ballots/{id}/results
Storage:    PostgreSQL
Tech stack: Flutter, Firebase
```

---

## Example 435

**Intent:**
gym equipment broken report via qr on machine

**Spec:**
```
Type:       Mobile application with backend (gym equipment faults)
Auth:       Member login optional
Data model: Equipment(id, name, qr_code, status)
            FaultReport(id, equipment_id -> Equipment, description, photo_url, status)
Features:   - Scan a machine QR to report a fault
            - Mark machines out of order in the app
            - Assign repairs to a technician
            - Show members which machines are down
API:        REST
            POST /equipment/{qr}/faults
            PATCH /faults/{id}
            GET  /equipment/down
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 436

**Intent:**
wedding venue with rooms, guests book room block at discount

**Spec:**
```
Type:       Mobile application with backend (wedding room blocks)
Auth:       Booking code for guests; couple login
Data model: RoomBlock(id, wedding_id, rooms, rate, release_on)
            BlockReservation(id, block_id -> RoomBlock, guest_name, nights, room_type)
Features:   - Let guests book from the reserved block
            - Release unbooked rooms after the cutoff date
            - Show the couple who has booked
            - Send arrival information
API:        REST
            POST /blocks/{id}/reservations
            GET  /blocks/{id}/reservations
Storage:    PostgreSQL
Tech stack: Flutter, Laravel
```

---

## Example 437

**Intent:**
helpers for disabled people at airports - request wheelchair assistance before flight

**Spec:**
```
Type:       Mobile application with backend (airport mobility assistance)
Auth:       Email + password
Data model: AssistRequest(id, passenger_id, flight_number, airport, kind, status)
            Agent(id, name, terminal, available)
Features:   - Request assistance with flight details
            - Notify the airport's assistance team
            - Show where to meet the agent
            - Update agent if the flight changes gate
API:        REST
            POST /requests
            PATCH /requests/{id}
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, Node.js
```

---

## Example 438

**Intent:**
people who sew masks/blankets for hospitals coordinate donations

**Spec:**
```
Type:       Mobile application with backend (handmade donations)
Auth:       Email + password
Data model: Need(id, facility, item, quantity, deadline)
            Pledge(id, need_id -> Need, maker_id, quantity, dropped_off)
Features:   - Let facilities post needs for handmade items
            - Pledge quantities
            - Show drop-off points
            - Track how much was delivered
API:        REST
            POST /needs
            POST /needs/{id}/pledges
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 439

**Intent:**
minibus hire for groups with driver

**Spec:**
```
Type:       Mobile application with backend (minibus hire)
Auth:       Email + password
Data model: Minibus(id, seats, wheelchair_access)
            HireRequest(id, group_name, seats, pickup, destination, date, return_trip, status)
            Quote(id, request_id -> HireRequest, price)
Features:   - Request a minibus with driver for a group trip
            - Receive a quote
            - Accept and pay a deposit
            - Share driver details on the day
API:        REST
            POST /requests
            POST /requests/{id}/quote
            POST /quotes/{id}/accept
Storage:    PostgreSQL
Tech stack: Flutter, Django
```

---

## Example 440

**Intent:**
staff canteen at factory pre-order lunch to reduce waste

**Spec:**
```
Type:       Mobile application with backend (staff canteen pre-orders)
Auth:       Employee badge number + PIN
Data model: Dish(id, date, name, price, portions)
            LunchOrder(id, employee_id, dish_id -> Dish, collected)
Features:   - Show the weekly menu
            - Pre-order lunch by 10am
            - Deduct price from payroll
            - Show the kitchen order counts
API:        REST
            GET  /menu?week={w}
            POST /orders
            GET  /kitchen/counts
Storage:    PostgreSQL
Tech stack: React Native, C#, ASP.NET Core
```

---

## Example 441

**Intent:**
tool to schedule chimney sweep visits and remind yearly

**Spec:**
```
Type:       Mobile application with backend (chimney sweep)
Auth:       Phone number + OTP
Data model: Home(id, address, fireplaces)
            SweepVisit(id, home_id -> Home, date, certificate_url)
Features:   - Book a sweep visit
            - Issue a digital sweep certificate
            - Remind customers a year later
            - Plan routes by area
API:        REST
            POST /visits
            GET  /visits/{id}/certificate
Storage:    PostgreSQL, S3
Tech stack: Flutter, Node.js
```

---

## Example 442

**Intent:**
retail store staff app to request help from other staff, like "cleanup aisle 5"

**Spec:**
```
Type:       Mobile application with backend (store staff requests)
Auth:       Employee PIN
Data model: StaffRequest(id, store_id, kind, location, created_by, claimed_by, status)
Features:   - Send a request like cleanup, price check or carry-out
            - Push to staff on shift
            - Claim and close requests
            - Show response times per store
API:        REST + WebSocket
            POST /requests
            POST /requests/{id}/claim
            WS   /stores/{id}/requests
Storage:    PostgreSQL
Tech stack: Kotlin, Node.js, Socket.IO
```

---

## Example 443

**Intent:**
Islamic centre wants app for Quran classes registration and tuition, Next.js admin plus mobile

**Spec:**
```
Type:       Mobile application with backend (Islamic centre classes)
Auth:       Parent email + password
Data model: QuranClass(id, level, teacher, days, fee)
            StudentEnrolment(id, class_id -> QuranClass, child_name, parent_id, status)
            TuitionPayment(id, enrolment_id -> StudentEnrolment, month, amount, paid_at)
Features:   - Register children for Quran classes by level
            - Pay monthly tuition
            - Let admins manage classes in a web dashboard
            - Notify parents about class cancellations
API:        REST
            GET  /classes
            POST /enrolments
            POST /payments
Storage:    PostgreSQL
Tech stack: React Native, Next.js (admin and API routes), Prisma, Stripe
```

---

## Example 444

**Intent:**
rowing club boat booking and damage reports

**Spec:**
```
Type:       Mobile application with backend (rowing club boats)
Auth:       Member login
Data model: Boat(id, name, type, seats, status)
            Outing(id, boat_id -> Boat, crew_ids, starts_at, ends_at)
            DamageReport(id, boat_id -> Boat, description, photo_url)
Features:   - Book boats for outings
            - Log crew members and distance rowed
            - Report damage and take boats out of service
            - Show river conditions flag
API:        REST
            POST /outings
            POST /boats/{id}/damage
            GET  /river-status
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 445

**Intent:**
let people rent their garage or basement for storage to neighbours

**Spec:**
```
Type:       Mobile application with backend (peer-to-peer storage)
Auth:       Email + password with ID verification
Data model: StorageSpace(id, host_id, kind, size_m2, monthly_price, lat, lng)
            StorageRental(id, space_id -> StorageSpace, renter_id, start_date, end_date, status)
Features:   - List a space with size and access rules
            - Search nearby spaces by size
            - Pay monthly through the app
            - Record an item inventory with photos at move-in
API:        REST
            POST /spaces
            GET  /spaces/nearby
            POST /rentals
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Ruby on Rails, Stripe Connect
```

---

## Example 446

**Intent:**
hairdressers that go to care homes, book residents in batches

**Spec:**
```
Type:       Mobile application with backend (care home hairdressing)
Auth:       Care home staff and hairdresser logins
Data model: CareHome(id, name, address)
            ResidentClient(id, care_home_id -> CareHome, name, room, usual_service)
            SalonDay(id, care_home_id -> CareHome, date, hairdresser_id)
            HairAppointment(id, day_id -> SalonDay, resident_id -> ResidentClient, service, price)
Features:   - Schedule salon days at each care home
            - Let staff book residents into a day
            - Bill families or the home monthly
            - Record usual styles per resident
API:        REST
            POST /salon-days
            POST /salon-days/{id}/appointments
            GET  /invoices?month={m}
Storage:    PostgreSQL
Tech stack: Flutter, Django
```

---

## Example 447

**Intent:**
uni students rate and review campus housing buildings

**Spec:**
```
Type:       Mobile application with backend (campus housing reviews)
Auth:       University email login
Data model: HousingBuilding(id, name, type, price_range)
            HousingReview(id, building_id -> HousingBuilding, student_id, year, stars, noise, cleanliness, text)
Features:   - Browse buildings with average ratings
            - Write reviews per academic year
            - Upload room photos
            - Report inappropriate reviews
API:        REST
            GET  /buildings
            POST /buildings/{id}/reviews
Storage:    PostgreSQL, S3
Tech stack: React Native, Supabase
```

---

## Example 448

**Intent:**
scavenger hunt for my daughter's birthday party in our garden, I set clues, kids scan QR stickers

**Spec:**
```
Type:       Mobile application with backend (party treasure hunt)
Auth:       Parent email + password
Data model: Hunt(id, parent_id, title)
            ClueCard(id, hunt_id -> Hunt, order, text, qr_code)
            KidTeam(id, hunt_id -> Hunt, name, current_clue)
Features:   - Write clues and print QR stickers
            - Let kids scan a sticker to get the next clue
            - Show the parent each team's progress
            - Play a celebration when the treasure is found
API:        REST
            POST /hunts
            POST /hunts/{id}/clues
            POST /teams/{id}/scan
Storage:    Firebase Firestore
Tech stack: Flutter, Firebase
```

---

## Example 449

**Intent:**
moving company crew app inventory items room by room and note damage

**Spec:**
```
Type:       Mobile application with backend (moving inventory)
Auth:       Crew login
Data model: Move(id, customer_name, from_address, to_address, date)
            InventoryItem(id, move_id -> Move, room, description, tag_number, condition, photo_url)
Features:   - Tag and list items room by room
            - Record pre-existing damage with photos
            - Check items off at unload
            - Get the customer's signature at both ends
API:        REST
            POST /moves/{id}/items
            PATCH /items/{id}/unloaded
            POST /moves/{id}/signature
Storage:    PostgreSQL, S3
Tech stack: React Native, Laravel
```

---

## Example 450

**Intent:**
parking lot at church shared with nearby businesses on weekdays, they pay monthly

**Spec:**
```
Type:       Mobile application with backend (shared lot permits)
Auth:       Email + password
Data model: LotPermit(id, business_name, plates, spaces, monthly_fee, valid_to)
            BlackoutDate(id, date, reason)
Features:   - Sell weekday parking permits to businesses
            - Show blackout dates like funerals
            - Notify permit holders of blackout days
            - Collect monthly payments
API:        REST
            POST /permits
            POST /blackouts
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe Billing
```

---

## Example 451

**Intent:**
residents of tower block share rides to supermarket

**Spec:**
```
Type:       Mobile application with backend (building grocery rides)
Auth:       Resident email + password
Data model: GroceryRun(id, driver_id, store, departs_at, seats)
            RunSeat(id, run_id -> GroceryRun, resident_id)
Features:   - Post a trip to the supermarket with free seats
            - Reserve a seat
            - Add small shopping requests for those who stay home
            - Notify when the car leaves
API:        REST
            POST /runs
            POST /runs/{id}/seats
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 452

**Intent:**
clinic for refugees appointments with interpreter language picked

**Spec:**
```
Type:       Mobile application with backend (refugee clinic booking)
Auth:       Phone number + OTP
Data model: ClinicSlot(id, starts_at, clinician)
            Booking(id, slot_id -> ClinicSlot, patient_name, language, needs_interpreter)
Features:   - Book in 10 languages
            - Request an interpreter for the visit
            - Send reminders in the patient's language
            - Show the clinic address with photos of the entrance
API:        REST
            GET  /slots
            POST /bookings
Storage:    PostgreSQL
Tech stack: Flutter, Django
```

---

## Example 453

**Intent:**
I'm opening a padel bar, people book court and preorder drinks for after match

**Spec:**
```
Type:       Mobile application with backend (sports bar court booking)
Auth:       Email + password
Data model: Court(id, name)
            CourtSlot(id, court_id -> Court, starts_at, booked_by)
            AfterMatchOrder(id, slot_id -> CourtSlot, items, ready_at)
Features:   - Book a court slot
            - Preorder drinks ready at the end of the match
            - Split the bill between players
            - Earn a free drink after 10 bookings
API:        REST
            POST /slots/{id}/book
            POST /slots/{id}/orders
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe
```

---

## Example 454

**Intent:**
wildlife rescue hotline: public reports injured animal, rescuers dispatched

**Spec:**
```
Type:       Mobile application with backend (wildlife rescue dispatch)
Auth:       Rescuer email + password; public reports without login
Data model: AnimalReport(id, species_guess, condition, lat, lng, photo_url, reporter_phone, status)
            Rescuer(id, name, species_skills, lat, lng, available)
Features:   - Report an injured animal with photo and location
            - Show first-aid advice while waiting
            - Dispatch the nearest rescuer with the right skills
            - Update the reporter on the outcome
API:        REST
            POST /reports
            POST /reports/{id}/dispatch
            PATCH /reports/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Python, FastAPI
```

---

## Example 455

**Intent:**
schools sports hall rented by clubs in evenings, booking + invoice

**Spec:**
```
Type:       Mobile application with backend (community hall lettings)
Auth:       Club email + password
Data model: Hall(id, name, hourly_rate)
            Letting(id, hall_id -> Hall, club_id, weekday, start_time, end_time, term)
            LettingInvoice(id, club_id, term, amount, paid)
Features:   - Request regular weekly lettings
            - Approve lettings around school events
            - Invoice clubs per term
            - Notify clubs of closures
API:        REST
            POST /lettings
            PATCH /lettings/{id}/approve
            GET  /invoices
Storage:    PostgreSQL
Tech stack: Flutter, Laravel
```

---
## Example 456

**Intent:**
sports stadium lost and found, fans report lost items after game

**Spec:**
```
Type:       Mobile application with backend (stadium lost property)
Auth:       Email + password
Data model: LostClaim(id, fan_id, game_date, section, description, status)
            FoundItem(id, game_date, section, description, photo_url, status)
Features:   - Report a lost item with game and section
            - Log found items with photos at the stadium
            - Suggest matches by date, section and keywords
            - Arrange pickup or paid shipping
API:        REST
            POST /claims
            POST /found-items
            GET  /claims/{id}/matches
Storage:    PostgreSQL, S3
Tech stack: React Native, Node.js
```

---

## Example 457

**Intent:**
mosque wudu area and toilet cleaning checklist for volunteers

**Spec:**
```
Type:       Mobile application with backend (facility cleaning rota)
Auth:       Volunteer phone + OTP
Data model: CleanArea(id, name, qr_code)
            CleanTask(id, area_id -> CleanArea, volunteer_id, done_at)
Features:   - Scan the area QR code to log cleaning
            - Show areas overdue for cleaning
            - Assign weekly volunteers
            - Report supply shortages
API:        REST
            POST /areas/{qr}/clean
            GET  /areas/overdue
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 458

**Intent:**
I want to make it easier for my hospital's outpatients to find which floor and which desk, scan their appointment letter and the app tells them

**Spec:**
```
Type:       Mobile application with backend (outpatient letter scanner)
Data model: Clinic(id, code, name, building, floor, desk, directions)
            AppointmentLetter(barcode, clinic_code, starts_at)
Features:   - Scan the appointment letter barcode
            - Show the clinic's building, floor and desk
            - Give step-by-step directions with photos
            - Show a countdown to the appointment
API:        REST
            GET  /letters/{barcode}
            GET  /clinics/{code}
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, Node.js
```

---

## Example 459

**Intent:**
students with disabilities request exam accommodations and note takers

**Spec:**
```
Type:       Mobile application with backend (disability services)
Auth:       University SSO
Data model: AccommodationPlan(id, student_id, extra_time_pct, separate_room, approved_on)
            ExamRequest(id, plan_id -> AccommodationPlan, course, exam_date, status)
            NoteTakerMatch(id, student_id, course, note_taker_id)
Features:   - Request accommodations for each exam
            - Notify instructors of approved arrangements
            - Recruit volunteer note takers in the same course
            - Share notes privately
API:        REST
            POST /exam-requests
            POST /note-taker-matches
Storage:    PostgreSQL
Tech stack: React Native, Django
```

---

## Example 460

**Intent:**
heat pump installers record commissioning data and send to manufacturer warranty

**Spec:**
```
Type:       Mobile application with backend (heat pump commissioning)
Auth:       Installer accreditation number + password
Data model: Installation(id, address, model, serial, installed_on)
            CommissioningRecord(id, installation_id -> Installation, flow_temp, refrigerant_charge, photos, at)
            WarrantyRegistration(id, installation_id -> Installation, status)
Features:   - Scan the unit serial number
            - Record commissioning readings and photos
            - Register the warranty with the manufacturer
            - Remind homeowners of annual service
API:        REST
            POST /installations
            POST /installations/{id}/commissioning
            POST /installations/{id}/warranty
Storage:    PostgreSQL, S3
Tech stack: Flutter, Java, Spring Boot
```

---

## Example 461

**Intent:**
car rental at small island airport, keys in box, contactless

**Spec:**
```
Type:       Mobile application with backend (contactless car rental)
Auth:       Email + password with licence verification
Data model: RentalCar(id, plate, model, keybox_slot)
            CarReservation(id, car_id -> RentalCar, renter_id, pickup_at, return_at, keybox_code)
            ConditionPhoto(id, reservation_id -> CarReservation, stage, url)
Features:   - Book a car for flight arrival time
            - Send the key box code after licence check
            - Require walk-around photos at pickup and return
            - Charge fuel and extras after return
API:        REST
            POST /reservations
            POST /reservations/{id}/photos
            POST /reservations/{id}/return
Storage:    PostgreSQL, S3
Tech stack: React Native, Node.js, Stripe
```

---

## Example 462

**Intent:**
want app that tells me how busy my local post office is

**Spec:**
```
Type:       Mobile application with backend (branch queue status)
Data model: Branch(id, name, lat, lng)
            QueueSample(id, branch_id -> Branch, waiting, at)
Features:   - Read queue counts from the ticket machine
            - Show current waiting count per branch
            - Show typical busy hours
            - Suggest a nearby less busy branch
API:        REST
            POST /samples
            GET  /branches/nearby
Storage:    PostgreSQL
Tech stack: Flutter, Go
```

---

## Example 463

**Intent:**
Christian summer camp app, parents see photos, send letters to kids

**Spec:**
```
Type:       Mobile application with backend (summer camp)
Auth:       Parent email + password
Data model: Camper(id, parent_id, name, cabin, session)
            CampPhoto(id, session, url, tagged_camper_ids)
            Letter(id, camper_id -> Camper, from_parent, body, printed)
Features:   - Show daily camp photos filtered to the parent's child
            - Send letters printed and delivered at mail time
            - Share camp schedule and packing list
            - Contact the camp office
API:        REST
            GET  /photos?camper={id}
            POST /letters
Storage:    PostgreSQL, S3
Tech stack: React Native, Node.js
```

---

## Example 464

**Intent:**
kayak / canoe club members borrow club boats and log trips

**Spec:**
```
Type:       Mobile application with backend (paddling club)
Auth:       Member login
Data model: ClubBoat(id, name, type)
            PaddleTrip(id, boat_id -> ClubBoat, member_id, route, out_at, back_at)
Features:   - Sign out a boat with the planned route and return time
            - Alert the safety officer if not back on time
            - Log distance paddled
            - Show boat availability
API:        REST
            POST /trips
            PATCH /trips/{id}/back
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 465

**Intent:**
hotel minibar restock app for staff, scan room and what was used

**Spec:**
```
Type:       Mobile application with backend (minibar restocking)
Auth:       Staff PIN
Data model: MinibarItem(id, name, price)
            RoomCheck(id, room_number, staff_id, items_used, at)
Features:   - Scan the room QR and record used items
            - Post charges to the guest folio
            - Build a restock list per floor
            - Flag rooms checking out today
API:        REST
            POST /room-checks
            GET  /restock?floor={f}
Storage:    PostgreSQL
Tech stack: Kotlin, Java, Spring Boot
```

---

## Example 466

**Intent:**
vintage clothing pop-up shop queue and entry time slots

**Spec:**
```
Type:       Mobile application with backend (pop-up shop entry)
Auth:       Email or phone login
Data model: EntrySlot(id, starts_at, capacity)
            EntryPass(id, slot_id -> EntrySlot, user_id, qr_token)
Features:   - Reserve a 20-minute entry slot
            - Show the QR pass at the door
            - Release no-show passes to walk-ins
            - Notify followers before the next pop-up
API:        REST
            GET  /slots
            POST /passes
            POST /passes/scan
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 467

**Intent:**
for apartment, residents offer services to each other like dog walking, tutoring, small paid jobs

**Spec:**
```
Type:       Mobile application with backend (building skills exchange)
Auth:       Email + password, unit verified
Data model: Offer(id, resident_id, title, category, price, description)
            JobRequest(id, offer_id -> Offer, requester_id, date, status)
            Review(id, request_id -> JobRequest, stars, text)
Features:   - Post services offered within the building
            - Request a service and agree a date
            - Leave reviews after the job
            - Keep everything visible only to residents
API:        REST
            POST /offers
            POST /offers/{id}/requests
            POST /requests/{id}/review
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 468

**Intent:**
ngo distributes food vouchers to families, shops scan and redeem

**Spec:**
```
Type:       Mobile application with backend (aid voucher distribution)
Auth:       Beneficiary phone + PIN; shop and staff logins
Data model: Beneficiary(id, household_id, phone, monthly_allowance)
            Voucher(id, beneficiary_id -> Beneficiary, amount, qr_token, expires_on, status)
            Redemption(id, voucher_id -> Voucher, shop_id, amount, at)
Features:   - Issue monthly vouchers to registered households
            - Let shops scan and redeem vouchers
            - Block redemption of expired or used vouchers
            - Reimburse shops weekly
API:        REST
            POST /vouchers/issue
            POST /vouchers/redeem
            GET  /shops/{id}/reimbursements
Storage:    PostgreSQL
Tech stack: Flutter, Python, Django
```

---

## Example 469

**Intent:**
museum membership app shows card, member events, and guest passes

**Spec:**
```
Type:       Mobile application with backend (museum membership)
Auth:       Email + password
Data model: Membership(id, member_id, tier, valid_to, guest_passes_left)
            MemberEvent(id, title, starts_at, tier_required)
            EventRsvp(id, event_id -> MemberEvent, member_id, guests)
Features:   - Show a digital membership card
            - RSVP to member previews
            - Send guest passes to friends
            - Renew membership in the app
API:        REST
            GET  /membership
            POST /events/{id}/rsvp
            POST /guest-passes
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails, Stripe
```

---

## Example 470

**Intent:**
students report broken campus wifi spots, IT sees heatmap

**Spec:**
```
Type:       Mobile application with backend (campus Wi-Fi reports)
Auth:       University SSO
Data model: WifiReport(id, building, floor, lat, lng, signal_dbm, speed_mbps, at)
            AccessPoint(id, building, floor, name)
Features:   - Run a speed test and attach location
            - Report dead zones in one tap
            - Show IT a heatmap of complaints
            - Notify reporters when an area is fixed
API:        REST
            POST /reports
            GET  /reports/heatmap
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Python, FastAPI
```

---

## Example 471

**Intent:**
residents association bulk buy heating oil together for cheaper price

**Spec:**
```
Type:       Mobile application with backend (heating oil group buying)
Auth:       Email + password
Data model: BuyRound(id, closes_on, supplier, price_per_litre)
            OilOrder(id, round_id -> BuyRound, household_id, litres, address)
Features:   - Open a buying round with a closing date
            - Let households order litres
            - Send the combined order to suppliers for quotes
            - Notify delivery dates
API:        REST
            POST /rounds
            POST /rounds/{id}/orders
            GET  /rounds/{id}/summary
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 472

**Intent:**
church van pick up list each sunday morning with route

**Spec:**
```
Type:       Mobile application with backend (church van pickups)
Auth:       Driver and coordinator logins
Data model: Rider(id, name, address, lat, lng, phone)
            VanRun(id, date, driver_id, rider_ids)
Features:   - Let riders request a pickup by Saturday
            - Build an optimised route for the van
            - Text riders when the van is 5 minutes away
            - Mark riders picked up
API:        REST
            POST /requests
            GET  /runs/{date}/route
            POST /runs/{id}/pickups
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Google Directions API, Twilio
```

---

## Example 473

**Intent:**
night shift workers at hospital order food from 24h canteen ahead

**Spec:**
```
Type:       Mobile application with backend (night canteen ordering)
Auth:       Hospital SSO
Data model: NightMenuItem(id, name, price, available)
            NightOrder(id, staff_id, items, pickup_at, status)
Features:   - Order food for a pickup time during the break
            - Pay with staff payroll deduction
            - Notify when the order is ready
            - Show the canteen a printable order list
API:        REST
            GET  /menu
            POST /orders
Storage:    PostgreSQL
Tech stack: React Native, C#, ASP.NET Core
```

---

## Example 474

**Intent:**
ski school kids lessons, parents see instructor notes and pickup point

**Spec:**
```
Type:       Mobile application with backend (ski school)
Auth:       Parent email + password
Data model: SkiChild(id, parent_id, name, level)
            SkiGroup(id, level, instructor, meeting_point, date)
            InstructorNote(id, child_id -> SkiChild, group_id -> SkiGroup, note, level_up)
Features:   - Book group lessons by level
            - Show the meeting and pickup point
            - Share instructor notes and level progress
            - Call the instructor in an emergency
API:        REST
            POST /bookings
            GET  /children/{id}/notes
Storage:    PostgreSQL
Tech stack: Flutter, Laravel
```

---

## Example 475

**Intent:**
want a Swift iOS app with CloudKit for my synagogue's Shabbat meal hosting, families sign up to host guests

**Spec:**
```
Type:       Mobile application with backend (Shabbat meal hosting)
Auth:       Sign in with Apple
Data model: HostOffer(id, host_family, date, seats, kosher_level, notes)
            GuestRequest(id, offer_id -> HostOffer, guest_name, party_size, status)
Features:   - Let families offer seats for a Shabbat meal
            - Let guests request a place
            - Confirm or decline requests
            - Remind hosts and guests on Friday morning
API:        CloudKit public and private databases
Storage:    CloudKit
Tech stack: Swift, SwiftUI, CloudKit
```

---

## Example 476

**Intent:**
grocery store app scan as you shop and pay in app, skip checkout

**Spec:**
```
Type:       Mobile application with backend (scan-and-go shopping)
Auth:       Email + password, card on file
Data model: Product(id, barcode, name, price)
            Basket(id, user_id, store_id, items, status)
            ExitPass(id, basket_id -> Basket, qr_token, audited)
Features:   - Scan product barcodes while shopping
            - Show a running total
            - Pay in the app and show an exit QR code
            - Randomly flag baskets for staff audit
API:        REST
            GET  /products/{barcode}
            POST /baskets/{id}/items
            POST /baskets/{id}/checkout
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe
```

---

## Example 477

**Intent:**
neighbourhood snow shovel volunteers help elderly clear walk

**Spec:**
```
Type:       Mobile application with backend (snow shovelling help)
Auth:       Phone number + OTP
Data model: ShovelRequest(id, address, requester_name, phone, status, created_at)
            ShovelVolunteer(id, name, area)
Features:   - Let seniors request help after snowfall
            - Notify volunteers nearby
            - Claim and complete requests
            - Thank volunteers with a season tally
API:        REST
            POST /requests
            POST /requests/{id}/claim
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 478

**Intent:**
uni research participant recruitment, students sign up for studies for credit

**Spec:**
```
Type:       Mobile application with backend (research participant pool)
Auth:       University SSO
Data model: Study(id, title, researcher_id, credits, eligibility, location)
            StudyTimeslot(id, study_id -> Study, starts_at, spots)
            Participation(id, timeslot_id -> StudyTimeslot, student_id, status)
Features:   - Browse studies the student is eligible for
            - Sign up for a timeslot
            - Let researchers grant credits after attendance
            - Show credits earned per course
API:        REST
            GET  /studies
            POST /timeslots/{id}/signup
            POST /participations/{id}/credit
Storage:    PostgreSQL
Tech stack: React Native, Django
```

---

## Example 479

**Intent:**
apartment trash valet, put bag at door and porter collects nightly, app confirms

**Spec:**
```
Type:       Mobile application with backend (doorstep trash valet)
Auth:       Resident email + password; porter login
Data model: Unit(id, number, floor)
            Pickup(id, unit_id -> Unit, date, collected_at, issue)
Features:   - Show porters the nightly floor-by-floor list
            - Mark bags collected per door
            - Report violations like loose trash with a photo
            - Let residents skip nights
API:        REST
            GET  /pickups?date={d}
            PATCH /pickups/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 480

**Intent:**
library of musical instruments for kids, borrow violin for term

**Spec:**
```
Type:       Mobile application with backend (instrument lending)
Auth:       Parent email + password
Data model: Instrument(id, kind, size, condition, status)
            InstrumentLoan(id, instrument_id -> Instrument, child_name, term, deposit, returned_on)
Features:   - Browse instruments by kind and size
            - Request a term loan
            - Track condition at checkout and return
            - Suggest a size change as children grow
API:        REST
            GET  /instruments
            POST /loans
            PATCH /loans/{id}/return
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 481

**Intent:**
temples and churches in our town share a calendar for interfaith events

**Spec:**
```
Type:       Mobile application with backend (interfaith events calendar)
Auth:       Organisation admin email + password
Data model: Community(id, name, faith, address)
            InterfaithEvent(id, community_id -> Community, title, starts_at, open_to_public)
Features:   - Let each community post events
            - Show a combined town calendar
            - Filter by faith or event type
            - Avoid clashes by warning about overlapping events
API:        REST
            POST /events
            GET  /events?month={m}
Storage:    PostgreSQL
Tech stack: Flutter, Django
```

---

## Example 482

**Intent:**
beach chair and umbrella rental, choose row on map

**Spec:**
```
Type:       Mobile application with backend (beach umbrella rental)
Auth:       Email or phone login
Data model: UmbrellaSpot(id, row, number, price)
            SpotBooking(id, spot_id -> UmbrellaSpot, user_id, date, loungers)
Features:   - Pick an umbrella on a beach map by row
            - Book for a day or week
            - Add extra loungers
            - Show the QR booking to the attendant
API:        REST
            GET  /spots?date={d}
            POST /bookings
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe
```

---
