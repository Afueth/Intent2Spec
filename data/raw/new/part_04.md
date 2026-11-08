# Part 04: Mobile applications with backend / multi-user

---

## Example 1

**Intent:**
app for sharing photos with just my family

**Spec:**
```
Type:       Mobile application with backend (social)
Auth:       Invite-only sign-up via family invite link, email + password
Data model: User(id, name, email, password_hash, family_id -> Family)
            Family(id, name, invite_code)
            Photo(id, family_id -> Family, uploader_id -> User, image_url, caption, created_at)
            Comment(id, photo_id -> Photo, user_id -> User, text, created_at)
Features:   - Upload photos from the camera or gallery
            - Show a private feed of the family's photos
            - Comment on and like photos
            - Invite relatives with a shareable code
            - Send a push notification when a new photo is posted
API:        REST
            POST /auth/login
            POST /families/join
            GET  /photos
            POST /photos
            POST /photos/{id}/comments
Storage:    PostgreSQL (data), S3 (images)
Tech stack: Flutter, Node.js, Express, Firebase Cloud Messaging
```

---

## Example 2

**Intent:**
I want a chat app for my small team at work, with group channels and direct messages.

**Spec:**
```
Type:       Mobile application with backend (real-time)
Auth:       Email + password login, workspace admin invites members
Data model: User(id, name, email, password_hash, avatar_url)
            Channel(id, name, is_private, created_by -> User)
            ChannelMember(channel_id -> Channel, user_id -> User)
            Message(id, channel_id -> Channel, sender_id -> User, body, sent_at, edited_at)
Features:   - Create public and private channels
            - Send direct messages between two users
            - Deliver messages instantly over WebSockets
            - Show unread counts per channel
            - Search message history
API:        REST + WebSocket
            GET  /channels
            POST /channels
            GET  /channels/{id}/messages
            POST /channels/{id}/messages
            WS   /ws
Storage:    PostgreSQL (messages), Redis (presence and pub/sub)
Tech stack: React Native, Node.js, Socket.IO, PostgreSQL
```

---

## Example 3

**Intent:**
grocery delivery app for my neighborhood store

**Spec:**
```
Type:       Mobile application with backend (e-commerce)
Auth:       Phone number login with SMS one-time code
Data model: Customer(id, phone, name, address)
            Product(id, name, price, stock, category, image_url)
            Order(id, customer_id -> Customer, status, total, delivery_slot, created_at)
            OrderItem(order_id -> Order, product_id -> Product, quantity)
Features:   - Browse products by category
            - Add items to a cart and check out
            - Choose a delivery time slot
            - Pay online by card
            - Track order status from packed to delivered
API:        REST
            GET  /products
            POST /orders
            GET  /orders/{id}
            POST /payments/intent
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework, Stripe, Twilio
```

---

## Example 4

**Intent:**
carpool app for parents at my kids school so we can share the morning drive

**Spec:**
```
Type:       Mobile application with backend (ride sharing)
Auth:       Email login restricted to parents approved by a school admin
Data model: Parent(id, name, email, phone, home_location)
            Child(id, parent_id -> Parent, name, grade)
            Carpool(id, driver_id -> Parent, date, departure_time, seats_free)
            CarpoolSeat(carpool_id -> Carpool, child_id -> Child)
Features:   - Offer a morning drive with free seats
            - Request a seat for a child on a drive
            - Show nearby parents on a map
            - Notify parents when the driver leaves and arrives
            - Keep a weekly driving rotation
API:        REST
            GET  /carpools?date={date}
            POST /carpools
            POST /carpools/{id}/seats
            DELETE /carpools/{id}/seats/{child_id}
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, NestJS, Google Maps SDK, Expo push notifications
```

---

## Example 5

**Intent:**
meetup app for board game nights

**Spec:**
```
Type:       Mobile application with backend (events)
Auth:       Sign in with Google or Apple
Data model: User(id, name, avatar_url, city)
            Event(id, host_id -> User, title, game_list, location, starts_at, max_players)
            Rsvp(event_id -> Event, user_id -> User, status)
Features:   - Create a game night with a location and player limit
            - Browse upcoming events in your city
            - RSVP and join a waitlist when full
            - Message attendees of an event
            - Remind attendees one hour before start
API:        REST
            GET  /events?city={city}
            POST /events
            POST /events/{id}/rsvp
            GET  /events/{id}/attendees
Storage:    PostgreSQL
Tech stack: Kotlin (Android), Swift (iOS), Ktor backend
```

---

## Example 6

**Intent:**
hey can u make me a dating app but for dog owners lol, match people whose dogs would get along

**Spec:**
```
Type:       Mobile application with backend (matching)
Auth:       Phone number login with SMS code
Data model: User(id, name, age, bio, location)
            Dog(id, owner_id -> User, name, breed, size, energy_level, temperament)
            Swipe(id, from_user_id -> User, to_user_id -> User, liked, created_at)
            Match(id, user_a_id -> User, user_b_id -> User, created_at)
Features:   - Create a profile for owner and dog
            - Show nearby profiles filtered by dog size and energy
            - Swipe to like or pass
            - Create a match when both users like each other
            - Chat with matches
API:        REST
            GET  /profiles/nearby
            POST /swipes
            GET  /matches
            GET  /matches/{id}/messages
            POST /matches/{id}/messages
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Flutter, Firebase Auth, Go backend
```

---

## Example 7

**Intent:**
An app where people in my town can hire a local handyman, see reviews and book a time.

**Spec:**
```
Type:       Mobile application with backend (marketplace)
Auth:       Email + password login with separate customer and provider roles
Data model: User(id, name, email, password_hash, role)
            ProviderProfile(id, user_id -> User, skills, hourly_rate, service_area)
            Booking(id, customer_id -> User, provider_id -> ProviderProfile, job_description, scheduled_at, status)
            Review(id, booking_id -> Booking, rating, comment)
Features:   - Search providers by skill and distance
            - Show provider profiles with ratings
            - Book a time slot and describe the job
            - Let providers accept or decline bookings
            - Leave a review after the job is done
API:        REST
            GET  /providers?skill={skill}
            POST /bookings
            PATCH /bookings/{id}
            POST /bookings/{id}/review
Storage:    PostgreSQL
Tech stack: React Native, Ruby on Rails API, Stripe Connect
```

---

## Example 8

**Intent:**
app for our delivery drivers to see their route and mark packages delivered

**Spec:**
```
Type:       Mobile application with backend (field operations)
Auth:       Driver login with employee ID and PIN, issued by dispatch
Data model: Driver(id, employee_id, name, pin_hash)
            Route(id, driver_id -> Driver, date, status)
            Stop(id, route_id -> Route, address, lat, lng, sequence, status)
            Proof(id, stop_id -> Stop, photo_url, signature_url, delivered_at)
Features:   - Show today's route stops on a map in order
            - Open turn-by-turn navigation to the next stop
            - Mark a package delivered with a photo or signature
            - Report a failed delivery with a reason
            - Sync updates when the phone is back online
API:        REST
            GET  /drivers/me/route
            PATCH /stops/{id}
            POST /stops/{id}/proof
Storage:    PostgreSQL (server), SQLite (offline cache on device)
Tech stack: Kotlin (Android), Spring Boot, Mapbox Navigation SDK
```

---

## Example 9

**Intent:**
school app so teachers can message parents

**Spec:**
```
Type:       Mobile application with backend (messaging)
Auth:       Accounts created by the school, login with email + password
Data model: Teacher(id, name, email, password_hash)
            Parent(id, name, email, password_hash)
            Student(id, name, class_id -> Class)
            Class(id, name, teacher_id -> Teacher)
            Message(id, sender_id, recipient_id, class_id -> Class, body, sent_at, read_at)
Features:   - Send a message to one parent or a whole class
            - Show read receipts to teachers
            - Translate messages into the parent's language
            - Notify parents with push notifications
API:        REST
            GET  /classes
            POST /messages
            GET  /messages?thread={id}
            POST /messages/{id}/read
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Google Cloud Translation API
```

---

## Example 10

**Intent:**
hi, i coach a kids soccer team (under 10s) and organizing everything over text messages is a nightmare. parents never know when practice is, who is bringing snacks, if a game got moved because of rain. i want one app where i post the schedule and they can say if their kid comes

**Spec:**
```
Type:       Mobile application with backend (sports team)
Auth:       Coach creates the team; parents join with a team code and email login
Data model: Team(id, name, coach_id -> User, join_code)
            User(id, name, email, role)
            Player(id, team_id -> Team, parent_id -> User, name)
            Event(id, team_id -> Team, type, starts_at, location, status)
            Attendance(event_id -> Event, player_id -> Player, response)
            SnackDuty(event_id -> Event, parent_id -> User)
Features:   - Post practices and games on a team calendar
            - Let parents mark their child as attending or absent
            - Assign snack duty for each game
            - Send a push alert when an event is moved or cancelled
            - Show the coach an attendance summary per event
API:        REST
            GET  /teams/{id}/events
            POST /teams/{id}/events
            PATCH /events/{id}
            PUT  /events/{id}/attendance/{player_id}
Storage:    PostgreSQL
Tech stack: React Native (Expo), Supabase (database and auth), Expo push notifications
```

---

## Example 11

**Intent:**
share live location with my wife when im driving home

**Spec:**
```
Type:       Mobile application with backend (real-time location)
Auth:       Email login; users pair accounts by accepting an invite
Data model: User(id, name, email)
            Share(id, owner_id -> User, viewer_id -> User, active, expires_at)
            LocationPoint(id, user_id -> User, lat, lng, speed, recorded_at)
Features:   - Start a live location share for a set time
            - Show the sharer's position on a map in real time
            - Show estimated arrival time to home
            - Notify the viewer when the sharer arrives
            - Stop sharing automatically when time runs out
API:        REST + WebSocket
            POST /shares
            DELETE /shares/{id}
            POST /locations
            WS   /shares/{id}/live
Storage:    Redis (latest positions), PostgreSQL (shares)
Tech stack: Swift (iOS), Kotlin (Android), Node.js, Socket.IO
```

---

## Example 12

**Intent:**
coffee shop loyalty card app, buy 9 get the 10th free

**Spec:**
```
Type:       Mobile application with backend (loyalty)
Auth:       Phone number login with SMS code; staff accounts for baristas
Data model: Customer(id, phone, name)
            Stamp(id, customer_id -> Customer, store_id -> Store, staff_id -> Staff, created_at)
            Reward(id, customer_id -> Customer, redeemed_at)
            Store(id, name, address)
            Staff(id, store_id -> Store, name)
Features:   - Show the customer a QR code at checkout
            - Let staff scan the QR code to add a stamp
            - Issue a free-drink reward after 9 stamps
            - Redeem a reward at the counter
            - Show stamp progress on the home screen
API:        REST
            GET  /me/card
            POST /stamps
            POST /rewards/{id}/redeem
Storage:    PostgreSQL
Tech stack: Flutter, Firebase (Auth, Firestore, Cloud Functions)
```

---

## Example 13

**Intent:**
Neighbourhood watch app where residents report suspicious things and get alerts.

**Spec:**
```
Type:       Mobile application with backend (community safety)
Auth:       Email login with address verification by a moderator
Data model: Resident(id, name, email, verified_address, neighbourhood_id -> Neighbourhood)
            Neighbourhood(id, name, boundary_polygon)
            Report(id, resident_id -> Resident, category, description, photo_url, lat, lng, created_at)
            Comment(id, report_id -> Report, resident_id -> Resident, text)
Features:   - Post a report with category, photo and location
            - Show recent reports on a map
            - Send push alerts to residents in the same neighbourhood
            - Comment on reports
            - Let moderators hide false or abusive reports
API:        REST
            GET  /reports?neighbourhood={id}
            POST /reports
            POST /reports/{id}/comments
            DELETE /reports/{id}
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: React Native, Express, Firebase Cloud Messaging
```

---

## Example 14

**Intent:**
multiplayer trivia game on phones, like play with friends live

**Spec:**
```
Type:       Mobile game (multiplayer, real-time)
Auth:       Guest play with a nickname, optional Google sign-in to keep stats
Data model: Player(id, nickname, google_id, total_wins)
            Room(id, code, host_id -> Player, status)
            Question(id, text, choices, correct_index, category)
            Answer(room_id -> Room, player_id -> Player, question_id -> Question, choice, answered_ms)
Features:   - Create a room and share a join code
            - Start a round of 10 timed questions
            - Score answers by correctness and speed
            - Show a live leaderboard after each question
            - Save win counts for signed-in players
API:        REST + WebSocket
            POST /rooms
            POST /rooms/{code}/join
            WS   /rooms/{code}
Storage:    Redis (live rooms), PostgreSQL (questions and stats)
Tech stack: Unity (C#), Node.js, Colyseus
```

---

## Example 15

**Intent:**
app to control my smart plugs and see how much power they use

**Spec:**
```
Type:       Mobile application with backend (IoT companion)
Auth:       Email + password login
Data model: User(id, email, password_hash)
            Device(id, owner_id -> User, name, mac_address, is_on)
            PowerReading(id, device_id -> Device, watts, recorded_at)
            Schedule(id, device_id -> Device, on_time, off_time, days)
Features:   - Pair a new smart plug over Wi-Fi
            - Turn plugs on and off remotely
            - Show live and daily power usage charts
            - Set on/off schedules
            - Alert when a device uses more power than usual
API:        REST
            GET  /devices
            POST /devices
            POST /devices/{id}/toggle
            GET  /devices/{id}/readings
            POST /devices/{id}/schedules
Storage:    TimescaleDB (readings), PostgreSQL (devices)
Tech stack: Flutter, Go, MQTT (Mosquitto broker)
```

---

## Example 16

**Intent:**
my wife and me run a small home bakery, people order cakes from instagram DMs and we lose track. i want an app where customers pick a cake, pick a date for pickup, pay a deposit, and we see all orders on our phone in a list by day

**Spec:**
```
Type:       Mobile application with backend (ordering)
Auth:       Customer login with email; owner login with admin role
Data model: Customer(id, name, email, phone)
            Cake(id, name, description, base_price, photo_url)
            Order(id, customer_id -> Customer, cake_id -> Cake, size, message_on_cake, pickup_date, deposit_paid, status)
Features:   - Show a catalog of cakes with photos and prices
            - Let customers pick a pickup date that still has capacity
            - Take a deposit payment at checkout
            - Show the owners a daily list of orders
            - Notify customers when the cake is ready
API:        REST
            GET  /cakes
            POST /orders
            GET  /orders?date={date}
            PATCH /orders/{id}
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express, Stripe
```

---

## Example 17

**Intent:**
i want a app where students can sell old textbooks to other students at same university

**Spec:**
```
Type:       Mobile application with backend (marketplace)
Auth:       Sign-up with a university email address (verified by link)
Data model: Student(id, name, university_email, campus)
            Listing(id, seller_id -> Student, title, isbn, course_code, condition, price, photo_url, status)
            Conversation(id, listing_id -> Listing, buyer_id -> Student)
            Message(id, conversation_id -> Conversation, sender_id -> Student, body, sent_at)
Features:   - Post a book with ISBN lookup, photo and price
            - Search listings by course code or title
            - Message the seller inside the app
            - Mark a listing as sold
API:        REST
            GET  /listings?q={query}
            POST /listings
            PATCH /listings/{id}
            POST /listings/{id}/conversations
            POST /conversations/{id}/messages
Storage:    PostgreSQL, S3 (photos)
Tech stack: Flutter, FastAPI, Open Library API
```

---

## Example 18

**Intent:**
food truck finder

**Spec:**
```
Type:       Mobile application with backend (location-based)
Auth:       Food truck owners log in with email; customers browse without an account
Data model: Truck(id, owner_id -> Owner, name, cuisine, menu_url)
            Owner(id, email, password_hash)
            TruckLocation(id, truck_id -> Truck, lat, lng, open_until, updated_at)
            Favorite(device_id, truck_id -> Truck)
Features:   - Show open food trucks on a map near the user
            - Let owners check in their current location and hours
            - Filter trucks by cuisine
            - Favorite trucks and get a push when they open nearby
API:        REST
            GET  /trucks/nearby?lat={lat}&lng={lng}
            POST /trucks/{id}/checkin
            POST /favorites
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Node.js, Google Maps SDK
```

---

## Example 19

**Intent:**
Please I need an application for my cleaning company, the workers go to houses and must say when they arrive and leave, with the GPS, and I see it in the office.

**Spec:**
```
Type:       Mobile application with backend (field workforce)
Auth:       Worker login with phone number and PIN; manager login with email + password
Data model: Worker(id, name, phone, pin_hash)
            Client(id, name, address, lat, lng)
            Job(id, client_id -> Client, worker_id -> Worker, scheduled_at, status)
            CheckEvent(id, job_id -> Job, type, lat, lng, recorded_at)
Features:   - Show each worker their jobs for the day
            - Check in and check out with GPS position and time
            - Warn if check-in is far from the client address
            - Show managers a live board of who is where
            - Export hours worked per worker each week
API:        REST
            GET  /workers/me/jobs
            POST /jobs/{id}/check-in
            POST /jobs/{id}/check-out
            GET  /admin/jobs?date={date}
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, MySQL
```

---

## Example 20

**Intent:**
app that lets friends split a shared grocery list in real time

**Spec:**
```
Type:       Mobile application with backend (real-time collaboration)
Auth:       Sign in with Apple or Google
Data model: User(id, name, email)
            List(id, name, owner_id -> User)
            ListMember(list_id -> List, user_id -> User)
            Item(id, list_id -> List, name, quantity, added_by -> User, checked_by -> User, checked_at)
Features:   - Create a shared list and invite friends by link
            - Add and check off items with instant sync
            - Show who added or bought each item
            - Work offline and merge changes later
API:        REST + WebSocket
            GET  /lists
            POST /lists
            POST /lists/{id}/items
            PATCH /items/{id}
            WS   /lists/{id}/sync
Storage:    PostgreSQL
Tech stack: Swift (SwiftUI), Supabase Realtime
```

---

## Example 21

**Intent:**
firebase app for a book club to vote on next book

**Spec:**
```
Type:       Mobile application with backend (community)
Auth:       Firebase Authentication (email link sign-in)
Data model: Member(id, name, email)
            Club(id, name, admin_id -> Member)
            BookProposal(id, club_id -> Club, title, author, proposed_by -> Member)
            Vote(proposal_id -> BookProposal, member_id -> Member)
Features:   - Propose books for the next month
            - Vote once per round for a favorite book
            - Close the vote and announce the winner
            - Schedule the next meeting date
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase (Auth, Firestore, Cloud Functions, Cloud Messaging)
```

---

## Example 22

**Intent:**
ride sharing app for a small island, only like 20 drivers

**Spec:**
```
Type:       Mobile application with backend (ride hailing)
Auth:       Phone number login with SMS code; drivers approved by an admin
Data model: Rider(id, name, phone)
            Driver(id, name, phone, vehicle, is_online, lat, lng)
            Ride(id, rider_id -> Rider, driver_id -> Driver, pickup, dropoff, fare, status, requested_at)
Features:   - Request a ride with pickup and dropoff on a map
            - Offer the request to the nearest online driver
            - Show the driver's live position to the rider
            - Calculate a fixed fare by zone
            - Rate the driver after the trip
API:        REST + WebSocket
            POST /rides
            PATCH /rides/{id}
            POST /drivers/me/location
            WS   /rides/{id}/track
Storage:    PostgreSQL, Redis (driver locations)
Tech stack: React Native, NestJS, Google Maps Platform
```

---

## Example 23

**Intent:**
volunteer signup app for our food bank shifts

**Spec:**
```
Type:       Mobile application with backend (scheduling)
Auth:       Email + password login; coordinators have admin role
Data model: Volunteer(id, name, email, phone)
            Shift(id, task, starts_at, ends_at, capacity)
            Signup(shift_id -> Shift, volunteer_id -> Volunteer, checked_in)
Features:   - List upcoming shifts with open spots
            - Sign up for or cancel a shift
            - Remind volunteers the day before
            - Check in at arrival by scanning a QR code
            - Report total volunteer hours per month
API:        REST
            GET  /shifts
            POST /shifts/{id}/signups
            DELETE /shifts/{id}/signups/me
            POST /shifts/{id}/checkin
Storage:    PostgreSQL
Tech stack: Ionic (Angular), Node.js, Express
```

---

## Example 24

**Intent:**
dog walking app where owners book walkers and track the walk on gps

**Spec:**
```
Type:       Mobile application with backend (services marketplace)
Auth:       Email login with owner and walker roles; walkers pass background check
Data model: Owner(id, name, email, address)
            Dog(id, owner_id -> Owner, name, notes)
            Walker(id, name, rating, service_radius_km)
            Walk(id, dog_id -> Dog, walker_id -> Walker, scheduled_at, duration_min, status, route_geojson)
Features:   - Book a walk with a nearby walker
            - Track the walk live on a map
            - Send a photo and summary when the walk ends
            - Pay automatically after the walk
            - Rate the walker
API:        REST + WebSocket
            GET  /walkers/nearby
            POST /walks
            POST /walks/{id}/points
            WS   /walks/{id}/live
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Node.js, Stripe Connect, Mapbox
```

---

## Example 25

**Intent:**
anonymous confession app for my college

**Spec:**
```
Type:       Mobile application with backend (social)
Auth:       College email verification, but posts are shown anonymously
Data model: User(id, college_email_hash, college_id)
            Post(id, author_id -> User, college_id, body, created_at, score)
            Vote(post_id -> Post, user_id -> User, value)
            Flag(id, post_id -> Post, reason)
Features:   - Post anonymous text confessions
            - Upvote and downvote posts
            - Sort the feed by new or top
            - Flag posts and auto-hide after several flags
            - Filter profanity before posting
API:        REST
            GET  /posts?sort={sort}
            POST /posts
            POST /posts/{id}/vote
            POST /posts/{id}/flag
Storage:    PostgreSQL
Tech stack: React Native, Go, Perspective API (toxicity filter)
```

---

## Example 26

**Intent:**
walkie talkie app push to talk for my hiking group

**Spec:**
```
Type:       Mobile application with backend (real-time voice)
Auth:       Login with Google; join groups by invite code
Data model: User(id, name, email)
            Group(id, name, invite_code)
            GroupMember(group_id -> Group, user_id -> User)
            VoiceClip(id, group_id -> Group, sender_id -> User, audio_url, duration_s, sent_at)
Features:   - Hold a button to talk to the whole group
            - Play incoming voice clips automatically
            - Show members on a map with last known position
            - Queue clips when offline and send when signal returns
API:        REST + WebSocket
            POST /groups/join
            GET  /groups/{id}/clips
            POST /groups/{id}/clips
            WS   /groups/{id}
Storage:    PostgreSQL, S3 (audio clips)
Tech stack: Kotlin (Android), Swift (iOS), WebRTC, Node.js
```

---

## Example 27

**Intent:**
Restaurant table reservation app for diners.

**Spec:**
```
Type:       Mobile application with backend (booking)
Auth:       Email or Google login for diners; restaurant staff accounts
Data model: Restaurant(id, name, cuisine, address, opening_hours)
            Table(id, restaurant_id -> Restaurant, seats)
            Reservation(id, restaurant_id -> Restaurant, diner_id -> Diner, party_size, reserved_at, status)
            Diner(id, name, email, phone)
Features:   - Search restaurants by cuisine and area
            - Show available times for a party size
            - Book and cancel reservations
            - Send a reminder two hours before
            - Let staff see and manage tonight's bookings
API:        REST
            GET  /restaurants
            GET  /restaurants/{id}/availability?date={date}&party={n}
            POST /reservations
            DELETE /reservations/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Spring Boot, Twilio (SMS reminders)
```

---

## Example 28

**Intent:**
building a pickup basketball app with supabase where people post when they're at the court and others can join

**Spec:**
```
Type:       Mobile application with backend (sports)
Auth:       Supabase Auth (email magic link)
Data model: Player(id, username, skill_level)
            Court(id, name, lat, lng)
            Session(id, court_id -> Court, host_id -> Player, starts_at, players_needed)
            SessionPlayer(session_id -> Session, player_id -> Player)
Features:   - Show courts on a map with active sessions
            - Post a session saying you're at a court
            - Join a session and see who is playing
            - Notify followers of a court when a game starts
Storage:    Supabase PostgreSQL
Tech stack: React Native (Expo), Supabase (Auth, Database, Realtime, Edge Functions)
```

---

## Example 29

**Intent:**
tenants app for our apartment building to report repairs and get announcements

**Spec:**
```
Type:       Mobile application with backend (property management)
Auth:       Email login; tenants invited by building manager per unit
Data model: Tenant(id, name, email, unit_id -> Unit)
            Unit(id, number, building_id -> Building)
            Building(id, address)
            RepairRequest(id, tenant_id -> Tenant, category, description, photo_url, status, created_at)
            Announcement(id, building_id -> Building, title, body, posted_at)
Features:   - Submit a repair request with photos
            - Track repair status updates
            - Receive building announcements as push notifications
            - Let the manager assign repairs to a contractor
API:        REST
            GET  /repairs
            POST /repairs
            PATCH /repairs/{id}
            GET  /announcements
            POST /announcements
Storage:    PostgreSQL, S3 (photos)
Tech stack: React Native, Django REST Framework
```

---

## Example 30

**Intent:**
lost and found pets app

**Spec:**
```
Type:       Mobile application with backend (community)
Auth:       Email or Google login
Data model: User(id, name, email, phone)
            PetPost(id, user_id -> User, type, species, description, photo_url, lat, lng, status, created_at)
            Sighting(id, post_id -> PetPost, user_id -> User, lat, lng, note, seen_at)
Features:   - Post a lost or found pet with photo and location
            - Show nearby posts on a map
            - Report a sighting on a lost pet post
            - Alert users within 5 km of a new lost pet
            - Mark a pet as reunited
API:        REST
            GET  /posts/nearby
            POST /posts
            POST /posts/{id}/sightings
            PATCH /posts/{id}
Storage:    PostgreSQL with PostGIS, Cloud Storage (photos)
Tech stack: Flutter, Firebase Cloud Messaging, Node.js
```

---

## Example 31

**Intent:**
plz make app for gym where members book classes, like spin and yoga, limited spots

**Spec:**
```
Type:       Mobile application with backend (booking)
Auth:       Member login with email + password; gym staff admin
Data model: Member(id, name, email, membership_status)
            ClassType(id, name, description)
            ClassSession(id, class_type_id -> ClassType, instructor, starts_at, capacity)
            Booking(id, session_id -> ClassSession, member_id -> Member, status)
Features:   - Show the weekly class timetable
            - Book a spot or join the waitlist
            - Promote the first waitlisted member when someone cancels
            - Block bookings for expired memberships
            - Remind members 1 hour before class
API:        REST
            GET  /sessions?week={date}
            POST /sessions/{id}/bookings
            DELETE /bookings/{id}
Storage:    PostgreSQL
Tech stack: Flutter, NestJS
```

---

## Example 32

**Intent:**
gift exchange app secret santa for the office

**Spec:**
```
Type:       Mobile application with backend
Auth:       Join a group with an invite link, name + email
Data model: Group(id, name, budget, exchange_date, organizer_email)
            Participant(id, group_id -> Group, name, email, wishlist)
            Assignment(group_id -> Group, giver_id -> Participant, receiver_id -> Participant)
            Exclusion(group_id -> Group, a_id -> Participant, b_id -> Participant)
Features:   - Create a group with budget and date
            - Collect participant wishlists
            - Draw names randomly while respecting exclusions
            - Reveal each person's receiver only to them
            - Send anonymous questions to your receiver
API:        REST
            POST /groups
            POST /groups/{id}/participants
            POST /groups/{id}/draw
            GET  /groups/{id}/my-assignment
Storage:    PostgreSQL
Tech stack: React Native, Express, SendGrid
```

---

## Example 33

**Intent:**
Our church wants an app with prayer requests, event calendar and small group chats.

**Spec:**
```
Type:       Mobile application with backend (community)
Auth:       Email login; membership approved by church staff
Data model: Member(id, name, email, role)
            PrayerRequest(id, member_id -> Member, text, is_anonymous, prayed_count, created_at)
            Event(id, title, starts_at, location)
            SmallGroup(id, name, leader_id -> Member)
            GroupMessage(id, group_id -> SmallGroup, sender_id -> Member, body, sent_at)
Features:   - Post prayer requests, optionally anonymous
            - Tap "I prayed" to encourage the requester
            - Show the church event calendar
            - Chat inside small groups
            - Send announcements to all members
API:        REST + WebSocket
            GET  /prayers
            POST /prayers
            POST /prayers/{id}/prayed
            GET  /events
            WS   /groups/{id}/chat
Storage:    PostgreSQL
Tech stack: Flutter, Firebase (Auth, Firestore, Cloud Messaging)
```

---

## Example 34

**Intent:**
bike sharing for our campus, unlock bikes with qr code

**Spec:**
```
Type:       Mobile application with backend (IoT, rentals)
Auth:       Campus single sign-on (SAML) via the university login
Data model: Student(id, campus_id, name, balance)
            Bike(id, lock_id, status, lat, lng, battery)
            Station(id, name, lat, lng)
            Rental(id, student_id -> Student, bike_id -> Bike, started_at, ended_at, cost)
Features:   - Show available bikes and stations on a map
            - Scan the QR code to unlock a bike
            - Lock the bike to end the ride and charge the account
            - Report a damaged bike
            - Show ride history
API:        REST
            GET  /bikes/available
            POST /rentals
            POST /rentals/{id}/end
            POST /bikes/{id}/reports
Storage:    PostgreSQL
Tech stack: React Native, Node.js, MQTT (smart lock communication)
```

---

## Example 35

**Intent:**
app for my band to share setlists and rehearsal times

**Spec:**
```
Type:       Mobile application with backend (collaboration)
Auth:       Email login; band members join by invite
Data model: Band(id, name)
            Member(id, band_id -> Band, name, instrument)
            Song(id, band_id -> Band, title, key, tempo, notes)
            Setlist(id, band_id -> Band, name, gig_date)
            SetlistSong(setlist_id -> Setlist, song_id -> Song, position)
            Rehearsal(id, band_id -> Band, starts_at, location)
Features:   - Build setlists by dragging songs in order
            - Store key, tempo and notes per song
            - Schedule rehearsals and collect availability
            - Notify the band when a setlist changes
API:        REST
            GET  /bands/{id}/songs
            POST /setlists
            PUT  /setlists/{id}/songs
            POST /rehearsals
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 36

**Intent:**
Tinder for roommates. People looking for a room and people who have a room, swipe and match by budget and habits.

**Spec:**
```
Type:       Mobile application with backend (matching)
Auth:       Email or phone sign-up with ID verification
Data model: User(id, name, age, role, budget_min, budget_max, city, move_in_date)
            Habits(user_id -> User, smoker, pets, sleep_schedule, cleanliness)
            Room(id, owner_id -> User, rent, address, photos)
            Like(from_id -> User, to_id -> User)
            Match(id, seeker_id -> User, host_id -> User)
Features:   - Create a profile with budget, city and living habits
            - Show seekers rooms within their budget
            - Rank candidates by habit compatibility
            - Swipe to like and match on mutual likes
            - Chat after matching
API:        REST
            GET  /candidates
            POST /likes
            GET  /matches
            POST /matches/{id}/messages
Storage:    PostgreSQL, S3 (room photos)
Tech stack: Flutter, Django REST Framework
```

---

## Example 37

**Intent:**
alert app for a factory: if a machine sensor goes over temperature, workers phones buzz

**Spec:**
```
Type:       IoT system (with mobile alert app)
Auth:       Employee login with company email; supervisors manage thresholds
Data model: Machine(id, name, line, location)
            Sensor(id, machine_id -> Machine, type, threshold_high)
            Reading(sensor_id -> Sensor, value, recorded_at)
            Alert(id, sensor_id -> Sensor, value, raised_at, acknowledged_by -> Employee)
            Employee(id, name, email, shift)
Features:   - Collect sensor readings from machines over MQTT
            - Raise an alert when a reading exceeds the threshold
            - Send a high-priority push notification to on-shift workers
            - Let workers acknowledge an alert in the app
            - Show alert history per machine
API:        REST
            GET  /machines
            GET  /alerts?status=open
            POST /alerts/{id}/ack
            PUT  /sensors/{id}/threshold
Storage:    InfluxDB (readings), PostgreSQL (machines, alerts)
Tech stack: Flutter, Python, FastAPI, Eclipse Mosquitto, Firebase Cloud Messaging
```

---

## Example 38

**Intent:**
a karaoke battle game where friends sing and others vote from their phones

**Spec:**
```
Type:       Mobile game (party, multiplayer)
Auth:       Guest nicknames per room
Data model: Room(id, code, host_device_id, status)
            Player(id, room_id -> Room, nickname, score)
            Round(id, room_id -> Room, song_title, singer_id -> Player)
            Vote(round_id -> Round, voter_id -> Player, stars)
Features:   - Host a room and show a join code
            - Pick a random singer and song each round
            - Let the other players vote 1-5 stars from their phones
            - Show running scores and crown a winner
API:        REST + WebSocket
            POST /rooms
            POST /rooms/{code}/players
            WS   /rooms/{code}
Storage:    Redis (room state)
Tech stack: React Native, Node.js, Socket.IO
```

---

## Example 39

**Intent:**
whatsapp-like app but only for my extended family, with voice notes

**Spec:**
```
Type:       Mobile application with backend (messaging)
Auth:       Phone number login with SMS code, invite-only
Data model: User(id, phone, name, avatar_url)
            Chat(id, is_group, title)
            ChatMember(chat_id -> Chat, user_id -> User)
            Message(id, chat_id -> Chat, sender_id -> User, type, text, media_url, sent_at, delivered_at, read_at)
Features:   - Send text, photo and voice note messages
            - Create group chats
            - Show delivered and read ticks
            - Notify recipients with push notifications
            - Encrypt messages end to end
API:        REST + WebSocket
            GET  /chats
            POST /chats
            GET  /chats/{id}/messages
            POST /media
            WS   /ws
Storage:    PostgreSQL, S3 (media)
Tech stack: Flutter, Elixir, Phoenix Channels, Signal Protocol library
```

---

## Example 40

**Intent:**
Need app for my laundromat: customers schedule pickup, we wash, deliver back

**Spec:**
```
Type:       Mobile application with backend (on-demand service)
Auth:       Email or phone login for customers; staff login with admin role
Data model: Customer(id, name, phone, address)
            LaundryOrder(id, customer_id -> Customer, pickup_at, delivery_at, weight_kg, price, status)
            Driver(id, name, phone)
Features:   - Schedule a pickup window
            - Weigh the bag at the shop and price the order by kg
            - Update status from picked up to washing to delivered
            - Assign pickups and deliveries to drivers
            - Charge the saved card after weighing
API:        REST
            POST /orders
            GET  /orders/{id}
            PATCH /orders/{id}
            GET  /drivers/me/tasks
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe
```

---

## Example 41

**Intent:**
app where my running club logs runs and competes on a monthly leaderboard

**Spec:**
```
Type:       Mobile application with backend (fitness, social)
Auth:       Sign in with Strava (OAuth)
Data model: Runner(id, strava_id, name, club_id -> Club)
            Club(id, name)
            Run(id, runner_id -> Runner, distance_km, duration_s, started_at)
            Challenge(id, club_id -> Club, month, goal_km)
Features:   - Import runs automatically from Strava
            - Show a monthly distance leaderboard for the club
            - Set a club challenge with a distance goal
            - Give kudos to clubmates' runs
API:        REST
            GET  /clubs/{id}/leaderboard?month={m}
            GET  /runs
            POST /webhooks/strava
            POST /runs/{id}/kudos
Storage:    PostgreSQL
Tech stack: Flutter, FastAPI, Strava API
```

---

## Example 42

**Intent:**
i want to make a app to order from the cafeteria at our hospital, staff skip the line and pick up

**Spec:**
```
Type:       Mobile application with backend (food ordering)
Auth:       Hospital staff single sign-on (Azure AD)
Data model: Staff(id, employee_id, name, department)
            MenuItem(id, name, price, available, category)
            Order(id, staff_id -> Staff, pickup_time, status, total)
            OrderItem(order_id -> Order, item_id -> MenuItem, quantity)
Features:   - Show today's cafeteria menu
            - Order ahead and choose a pickup time
            - Pay by payroll deduction
            - Notify when the order is ready
            - Let kitchen staff see incoming orders on a tablet
API:        REST
            GET  /menu
            POST /orders
            PATCH /orders/{id}/status
            GET  /kitchen/orders
Storage:    SQL Server
Tech stack: .NET MAUI, ASP.NET Core, Azure AD (MSAL)
```

---

## Example 43

**Intent:**
hiking app where you see where your friends are on the trail

**Spec:**
```
Type:       Mobile application with backend (location sharing)
Auth:       Sign in with Apple or Google
Data model: User(id, name)
            Trip(id, name, trail_name, leader_id -> User)
            TripMember(trip_id -> Trip, user_id -> User)
            Position(user_id -> User, trip_id -> Trip, lat, lng, altitude, recorded_at)
Features:   - Create a hiking trip and invite friends
            - Show all members' positions on an offline topo map
            - Upload positions when there is signal and cache when not
            - Send an SOS with location to the group
            - Alert when someone is far behind the group
API:        REST
            POST /trips
            POST /trips/{id}/positions
            GET  /trips/{id}/positions
            POST /trips/{id}/sos
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin Multiplatform, Ktor, MapLibre (offline maps)
```

---

## Example 44

**Intent:**
pet sitter app

**Spec:**
```
Type:       Mobile application with backend (services marketplace)
Auth:       Email login with owner and sitter roles
Data model: Owner(id, name, email)
            Pet(id, owner_id -> Owner, name, species, care_notes)
            Sitter(id, name, bio, price_per_day, rating)
            Stay(id, pet_id -> Pet, sitter_id -> Sitter, start_date, end_date, status)
            Update(id, stay_id -> Stay, photo_url, note, posted_at)
Features:   - Search sitters by location and dates
            - Request and confirm a stay
            - Share care notes for each pet
            - Post daily photo updates during the stay
            - Review the sitter afterwards
API:        REST
            GET  /sitters
            POST /stays
            PATCH /stays/{id}
            POST /stays/{id}/updates
Storage:    PostgreSQL, S3 (photos)
Tech stack: React Native, Express, Stripe
```

---

## Example 45

**Intent:**
our football club has 6 youth teams and the parents need to pay fees, get kits ordered and see match results. something on phone. we have a little budget, so maybe use firebase so we don't pay for a server

**Spec:**
```
Type:       Mobile application with backend (sports club)
Auth:       Firebase Authentication (email + password); club admins and coaches have roles
Data model: Team(id, name, age_group, coach_id -> Member)
            Member(id, name, email, role)
            Player(id, team_id -> Team, parent_id -> Member, name, kit_size)
            Fee(id, player_id -> Player, season, amount, paid)
            Match(id, team_id -> Team, opponent, kickoff, home_score, away_score)
Features:   - Show fixtures and results per team
            - Let parents pay season fees by card
            - Collect kit sizes and create a kit order
            - Show admins who has not paid yet
            - Push match results to parents
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase (Auth, Firestore, Cloud Functions), Stripe
```

---

## Example 46

**Intent:**
party playlist app, guests add songs and vote what plays next

**Spec:**
```
Type:       Mobile application with backend (real-time)
Auth:       Host signs in with Spotify; guests join with a party code
Data model: Party(id, code, host_spotify_id, active)
            Guest(id, party_id -> Party, nickname)
            QueueItem(id, party_id -> Party, spotify_track_id, added_by -> Guest, votes)
Features:   - Create a party linked to the host's Spotify
            - Let guests search and add songs
            - Upvote songs to move them up the queue
            - Play the top song next on the host device
API:        REST + WebSocket
            POST /parties
            POST /parties/{code}/queue
            POST /queue/{id}/vote
            WS   /parties/{code}
Storage:    Redis
Tech stack: React Native, Node.js, Spotify Web API
```

---

## Example 47

**Intent:**
Hello, I am from Brazil and I have small shop of açaí. I want app that client make order and moto boy deliver, client see where is moto boy in map.

**Spec:**
```
Type:       Mobile application with backend (food delivery)
Auth:       Phone number login with SMS code for clients and couriers
Data model: Client(id, name, phone, address)
            Product(id, name, size, price, toppings)
            Order(id, client_id -> Client, courier_id -> Courier, total, status, created_at)
            Courier(id, name, phone, lat, lng, available)
Features:   - Show the açaí menu with sizes and toppings
            - Place an order and pay by Pix or card
            - Assign the order to an available courier
            - Show the courier's live position to the client
            - Notify the client when the courier arrives
API:        REST + WebSocket
            GET  /products
            POST /orders
            PATCH /orders/{id}
            POST /couriers/me/location
            WS   /orders/{id}/track
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Mercado Pago API, Google Maps SDK
```

---

## Example 48

**Intent:**
app to swap clothes with other people nearby

**Spec:**
```
Type:       Mobile application with backend (marketplace)
Auth:       Email or Google login
Data model: User(id, name, location, rating)
            Item(id, owner_id -> User, title, size, category, condition, photo_url, available)
            SwapOffer(id, from_user -> User, to_user -> User, offered_item_id -> Item, wanted_item_id -> Item, status)
Features:   - Post clothes with photos, size and condition
            - Browse items nearby filtered by size
            - Offer one of your items in exchange
            - Accept or decline swap offers
            - Rate the other person after a swap
API:        REST
            GET  /items?size={size}
            POST /items
            POST /swaps
            PATCH /swaps/{id}
Storage:    PostgreSQL, Cloudinary (photos)
Tech stack: React Native, NestJS
```

---

## Example 49

**Intent:**
babysitting coop where parents trade hours instead of money

**Spec:**
```
Type:       Mobile application with backend (community exchange)
Auth:       Invite-only email login
Data model: Parent(id, name, email, hour_balance)
            SitRequest(id, requester_id -> Parent, sitter_id -> Parent, starts_at, ends_at, kids_count, status)
            Transaction(id, request_id -> SitRequest, hours, from_id -> Parent, to_id -> Parent)
Features:   - Post a request for a babysitter with date and hours
            - Let other parents accept the request
            - Transfer hours from requester to sitter after the sitting
            - Show each parent's hour balance
            - Block requests when the balance is too negative
API:        REST
            GET  /requests
            POST /requests
            POST /requests/{id}/accept
            POST /requests/{id}/complete
            GET  /me/balance
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 50

**Intent:**
plant watering sensor app, tells me when my plants are thirsty

**Spec:**
```
Type:       IoT system (with mobile companion app)
Auth:       Email login
Data model: User(id, email)
            Sensor(id, owner_id -> User, plant_name, moisture_threshold)
            MoistureReading(sensor_id -> Sensor, moisture_pct, battery, recorded_at)
Features:   - Register a soil moisture sensor by scanning its QR code
            - Show moisture history per plant
            - Send a push notification when moisture drops below the threshold
            - Warn when a sensor battery is low
API:        REST
            POST /sensors
            GET  /sensors
            POST /sensors/{id}/readings
            PUT  /sensors/{id}
Storage:    PostgreSQL
Tech stack: ESP32 (Arduino), Flutter, Node.js, Firebase Cloud Messaging
```

---

## Example 51

**Intent:**
real estate agents app to share listings and schedule viewings with clients

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email + password login with agent and client roles
Data model: Agent(id, name, email, agency)
            Client(id, name, email, agent_id -> Agent)
            Listing(id, agent_id -> Agent, address, price, bedrooms, photos, status)
            Viewing(id, listing_id -> Listing, client_id -> Client, scheduled_at, feedback)
Features:   - Add listings with photos and details
            - Share selected listings with a client
            - Let clients request viewing times
            - Collect client feedback after a viewing
API:        REST
            GET  /listings
            POST /listings
            POST /clients/{id}/shared-listings
            POST /viewings
            PATCH /viewings/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Swift (iOS), Kotlin (Android), Spring Boot
```

---

## Example 52

**Intent:**
kids chore app where parents approve and kids earn points

**Spec:**
```
Type:       Mobile application with backend (family)
Auth:       Parent account with email; kid profiles with a 4-digit PIN under the parent
Data model: Family(id, name)
            Parent(id, family_id -> Family, email)
            Kid(id, family_id -> Family, name, pin_hash, points)
            Chore(id, family_id -> Family, title, points, recurring)
            Completion(id, chore_id -> Chore, kid_id -> Kid, photo_url, approved)
Features:   - Create chores with point values
            - Let kids mark chores done with a photo
            - Let parents approve or reject completions
            - Add points and let kids redeem them for rewards
            - Sync between parents' and kids' phones
API:        REST
            GET  /families/{id}/chores
            POST /chores
            POST /chores/{id}/completions
            PATCH /completions/{id}
Storage:    PostgreSQL
Tech stack: React Native, Firebase Auth, Node.js
```

---

## Example 53

**Intent:**
concert ticket resale app thats safe, no scams

**Spec:**
```
Type:       Mobile application with backend (marketplace)
Auth:       Email login with identity verification for sellers
Data model: User(id, name, email, verified)
            Event(id, name, venue, date)
            Ticket(id, event_id -> Event, seller_id -> User, section, seat, price, barcode_encrypted, status)
            Purchase(id, ticket_id -> Ticket, buyer_id -> User, paid_at, payout_released)
Features:   - List tickets for an event with a price cap
            - Hold the buyer's payment in escrow
            - Transfer the ticket barcode only after payment
            - Release payout to the seller after the event
            - Open a dispute if a ticket fails at the door
API:        REST
            GET  /events/{id}/tickets
            POST /tickets
            POST /tickets/{id}/purchase
            POST /purchases/{id}/dispute
Storage:    PostgreSQL
Tech stack: React Native, Django, Stripe Connect
```

---

## Example 54

**Intent:**
an app for my rowing club to book boats

**Spec:**
```
Type:       Mobile application with backend (booking)
Auth:       Member login with email; captains have admin rights
Data model: Member(id, name, email, level)
            Boat(id, name, type, seats, min_level, status)
            BoatBooking(id, boat_id -> Boat, member_id -> Member, starts_at, ends_at)
            DamageReport(id, boat_id -> Boat, member_id -> Member, description)
Features:   - Show boat availability by day
            - Book a boat if the member's level allows it
            - Prevent overlapping bookings
            - Report damage and mark the boat out of service
API:        REST
            GET  /boats
            GET  /boats/{id}/bookings
            POST /bookings
            POST /boats/{id}/damage
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 55

**Intent:**
Mobile app for a farmers market — vendors post what they have today, people preorder and pick up.

**Spec:**
```
Type:       Mobile application with backend (marketplace)
Auth:       Email login for vendors and shoppers
Data model: Vendor(id, name, stall_number, description)
            Product(id, vendor_id -> Vendor, name, unit, price, quantity_today)
            Preorder(id, shopper_id -> Shopper, vendor_id -> Vendor, pickup_time, status)
            PreorderItem(preorder_id -> Preorder, product_id -> Product, quantity)
            Shopper(id, name, email)
Features:   - Let vendors post today's produce and quantities
            - Browse vendors and products at the market
            - Preorder and pick a pickup time
            - Reduce stock when an order is placed
            - Notify vendors of new preorders
API:        REST
            GET  /vendors
            GET  /vendors/{id}/products
            POST /products
            POST /preorders
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 56

**Intent:**
app for a gaming cafe to reserve PCs

**Spec:**
```
Type:       Mobile application with backend (booking)
Auth:       Phone login with SMS code
Data model: Customer(id, phone, nickname, credit)
            Station(id, label, specs, status)
            Session(id, station_id -> Station, customer_id -> Customer, starts_at, ends_at, cost)
Features:   - Show which PCs are free right now
            - Reserve a PC for a time block
            - Top up credit in the app
            - Extend a running session from the phone
API:        REST
            GET  /stations
            POST /sessions
            POST /sessions/{id}/extend
            POST /credit/topup
Storage:    PostgreSQL
Tech stack: Flutter, Go, Stripe
```

---

## Example 57

**Intent:**
something so me and my long distance gf can leave little notes and photos for each other daily

**Spec:**
```
Type:       Mobile application with backend (couples)
Auth:       Email login; two accounts linked with a pairing code
Data model: User(id, name, email, partner_id -> User)
            Note(id, author_id -> User, text, photo_url, created_at, opened_at)
            Countdown(id, pair_key, title, date)
Features:   - Pair two accounts with a code
            - Leave a daily note or photo for your partner
            - Show a countdown to the next visit
            - Send a "thinking of you" tap with a push notification
            - Keep a timeline of past notes
API:        REST
            POST /pair
            GET  /notes
            POST /notes
            POST /taps
Storage:    Cloud Firestore, Firebase Storage
Tech stack: SwiftUI, Firebase
```

---

## Example 58

**Intent:**
carpool to work for company employees going same direction

**Spec:**
```
Type:       Mobile application with backend (carpooling)
Auth:       Company single sign-on (Google Workspace)
Data model: Employee(id, name, email, home_lat, home_lng, has_car)
            Ride(id, driver_id -> Employee, departure_at, seats, route_polyline)
            RideRequest(id, ride_id -> Ride, passenger_id -> Employee, status)
Features:   - Match passengers with drivers whose route passes nearby
            - Offer a ride with departure time and seats
            - Request and confirm seats
            - Track saved CO2 per employee
            - Show a monthly leaderboard of carpoolers
API:        REST
            GET  /rides/matching
            POST /rides
            POST /rides/{id}/requests
            PATCH /requests/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, NestJS, Google Directions API
```

---

## Example 59

**Intent:**
uber but for tow trucks

**Spec:**
```
Type:       Mobile application with backend (on-demand service)
Auth:       Phone login with SMS code; tow operators verified by admin
Data model: Customer(id, name, phone)
            Operator(id, company, phone, truck_type, is_online, lat, lng)
            TowRequest(id, customer_id -> Customer, operator_id -> Operator, pickup_lat, pickup_lng, destination, vehicle_info, price, status)
Features:   - Request a tow with the car's location and problem
            - Send the request to nearby online operators
            - Show the operator's ETA and live position
            - Quote a price by distance before confirming
            - Pay in the app after drop-off
API:        REST + WebSocket
            POST /tow-requests
            POST /tow-requests/{id}/accept
            PATCH /tow-requests/{id}
            WS   /tow-requests/{id}/track
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Node.js, Google Maps Platform, Stripe
```

---

## Example 60

**Intent:**
chat app for gamers to find a squad

**Spec:**
```
Type:       Mobile application with backend (social, matchmaking)
Auth:       Sign in with Discord (OAuth)
Data model: Gamer(id, discord_id, username, platform, region, rank)
            SquadPost(id, author_id -> Gamer, game, mode, slots_open, created_at)
            SquadMember(post_id -> SquadPost, gamer_id -> Gamer)
            Message(id, post_id -> SquadPost, sender_id -> Gamer, text, sent_at)
Features:   - Post a "looking for group" with game, mode and rank
            - Filter posts by game, platform and region
            - Join a squad and chat with members
            - Expire posts after two hours
API:        REST + WebSocket
            GET  /squads?game={game}
            POST /squads
            POST /squads/{id}/join
            WS   /squads/{id}/chat
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Go, Discord OAuth2
```

---

## Example 61

**Intent:**
neighbors lending tools to each other app

**Spec:**
```
Type:       Mobile application with backend (sharing economy)
Auth:       Email login with address verification
Data model: Neighbor(id, name, email, street, trust_score)
            Tool(id, owner_id -> Neighbor, name, description, photo_url, available)
            Loan(id, tool_id -> Tool, borrower_id -> Neighbor, start_date, due_date, returned_at)
Features:   - List tools you are willing to lend
            - Search tools available on nearby streets
            - Request to borrow for set dates
            - Remind borrowers when a tool is due back
            - Rate borrowers after return
API:        REST
            GET  /tools?q={query}
            POST /tools
            POST /tools/{id}/loans
            PATCH /loans/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework
```

---

## Example 62

**Intent:**
app to order drinks from your seat at the stadium

**Spec:**
```
Type:       Mobile application with backend (in-venue ordering)
Auth:       Guest checkout with email receipt; staff login for runners
Data model: Venue(id, name)
            Seat(id, venue_id -> Venue, section, row, number)
            MenuItem(id, venue_id -> Venue, name, price, age_restricted)
            Order(id, seat_id -> Seat, total, status, runner_id -> Runner, created_at)
            Runner(id, name, section_assigned)
Features:   - Scan the QR code on the seat to open the menu
            - Order and pay with Apple Pay or Google Pay
            - Ask runners to check ID for alcohol orders
            - Route orders to the runner covering that section
            - Show order status until delivery
API:        REST
            GET  /venues/{id}/menu
            POST /orders
            GET  /runners/me/orders
            PATCH /orders/{id}
Storage:    PostgreSQL
Tech stack: React Native, NestJS, Stripe
```

---

## Example 63

**Intent:**
wanna make an app where ppl rate public bathrooms lmao

**Spec:**
```
Type:       Mobile application with backend (crowdsourced reviews)
Auth:       Optional login with Google to post reviews
Data model: User(id, name)
            Restroom(id, name, lat, lng, accessible, baby_changing, added_by -> User)
            Review(id, restroom_id -> Restroom, user_id -> User, cleanliness, rating, comment, created_at)
Features:   - Show restrooms near you on a map
            - Add a new restroom location
            - Rate cleanliness and leave a short review
            - Filter by accessible and baby changing
API:        REST
            GET  /restrooms/nearby
            POST /restrooms
            POST /restrooms/{id}/reviews
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Express, Mapbox
```

---

## Example 64

**Intent:**
app where tutors and students find each other and do lessons

**Spec:**
```
Type:       Mobile application with backend (marketplace)
Auth:       Email + password with tutor and student roles
Data model: Tutor(id, name, subjects, hourly_rate, bio, rating)
            Student(id, name, grade_level)
            Lesson(id, tutor_id -> Tutor, student_id -> Student, subject, starts_at, duration_min, status, video_room_url)
            Review(id, lesson_id -> Lesson, stars, text)
Features:   - Search tutors by subject and price
            - Book a lesson in the tutor's free slots
            - Join the lesson by video call in the app
            - Pay per lesson with card
            - Review the tutor after the lesson
API:        REST
            GET  /tutors?subject={s}
            POST /lessons
            GET  /lessons/{id}/join
            POST /lessons/{id}/review
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Twilio Video, Stripe
```

---

## Example 65

**Intent:**
i run a scout troop. want an app for parents: permission slips signed on the phone, trip info, and a way to message all the parents. also want to see allergies of each kid in one place when we go camping

**Spec:**
```
Type:       Mobile application with backend (youth organization)
Auth:       Email login; leaders have admin role, parents linked to their scouts
Data model: Leader(id, name, email)
            Parent(id, name, email, phone)
            Scout(id, parent_id -> Parent, name, allergies, medications)
            Trip(id, title, date, location, details)
            PermissionSlip(id, trip_id -> Trip, scout_id -> Scout, signed_by -> Parent, signature_url, signed_at)
Features:   - Post trip details and request permission slips
            - Let parents sign slips with a finger signature
            - Show leaders which slips are still missing
            - Show an allergy and medication list for everyone on a trip
            - Broadcast messages to all parents
API:        REST
            GET  /trips
            POST /trips
            POST /trips/{id}/slips
            GET  /trips/{id}/medical
            POST /broadcasts
Storage:    PostgreSQL (medical fields encrypted at rest)
Tech stack: React Native, Ruby on Rails API
```

---

## Example 66

**Intent:**
real time quiz for my classroom, students answer on phones

**Spec:**
```
Type:       Mobile application with backend (real-time, education)
Auth:       Teacher login with email; students join with a game PIN and name
Data model: Teacher(id, email)
            Quiz(id, teacher_id -> Teacher, title)
            Question(id, quiz_id -> Quiz, text, options, correct_index, time_limit_s)
            GameSession(id, quiz_id -> Quiz, pin, status)
            StudentAnswer(session_id -> GameSession, student_name, question_id -> Question, choice, ms_taken)
Features:   - Build a quiz with multiple-choice questions
            - Start a live session with a 6-digit PIN
            - Push each question to all students at the same time
            - Show answer distribution after each question
            - Show a final podium
API:        REST + WebSocket
            POST /quizzes
            POST /sessions
            POST /sessions/{pin}/join
            WS   /sessions/{pin}
Storage:    PostgreSQL, Redis (live sessions)
Tech stack: Flutter, Node.js, Socket.IO
```

---

## Example 67

**Intent:**
grocery price comparing app where users post prices they saw

**Spec:**
```
Type:       Mobile application with backend (crowdsourced)
Auth:       Email or Google login
Data model: User(id, name, points)
            Store(id, name, chain, lat, lng)
            Product(id, barcode, name, brand)
            PriceReport(id, product_id -> Product, store_id -> Store, user_id -> User, price, reported_at)
Features:   - Scan a barcode and enter the shelf price
            - Compare the latest prices across nearby stores
            - Award points for each confirmed price report
            - Hide price reports older than two weeks
API:        REST
            GET  /products/{barcode}/prices
            POST /price-reports
            GET  /stores/nearby
Storage:    PostgreSQL
Tech stack: Kotlin (Android), Ktor, ML Kit (barcode scanning)
```

---

## Example 68

**Intent:**
An app for a hotel so guests can request towels, room service, and chat with reception.

**Spec:**
```
Type:       Mobile application with backend (hospitality)
Auth:       Guest login with booking number and last name
Data model: Stay(id, booking_number, guest_name, room_number, check_in, check_out)
            ServiceRequest(id, stay_id -> Stay, type, details, status, created_at)
            ChatMessage(id, stay_id -> Stay, from_staff, text, sent_at)
Features:   - Request housekeeping items like towels or pillows
            - Order room service from the menu
            - Chat with reception in real time
            - Show request status updates
            - Expire access after check-out
API:        REST + WebSocket
            POST /auth/stay
            POST /requests
            GET  /requests
            WS   /stays/{id}/chat
Storage:    PostgreSQL
Tech stack: React Native, NestJS, Socket.IO
```

---

## Example 69

**Intent:**
running buddies app

**Spec:**
```
Type:       Mobile application with backend (social fitness)
Auth:       Sign in with Apple or Google
Data model: Runner(id, name, pace_min_per_km, usual_distance_km, lat, lng)
            RunInvite(id, host_id -> Runner, meet_point, starts_at, pace, distance_km)
            InviteResponse(invite_id -> RunInvite, runner_id -> Runner, status)
Features:   - Find runners nearby with a similar pace
            - Post a run with meeting point and time
            - Accept or decline run invites
            - Chat with runners going on the same run
API:        REST
            GET  /runners/nearby
            POST /invites
            POST /invites/{id}/respond
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, FastAPI
```

---

## Example 70

**Intent:**
i'd like my mom (she's 78) to press one button if she falls and it texts me and my brother where she is

**Spec:**
```
Type:       Mobile application with backend (personal safety)
Auth:       Caregiver email login; senior phone linked by pairing code
Data model: Senior(id, name, device_token, pairing_code)
            Caregiver(id, name, phone, email)
            CareLink(senior_id -> Senior, caregiver_id -> Caregiver)
            Alert(id, senior_id -> Senior, lat, lng, created_at, acknowledged_by -> Caregiver)
Features:   - Show one large emergency button on the senior's phone
            - Send an SMS and push alert with GPS location to all caregivers
            - Call the first caregiver automatically if nobody acknowledges
            - Let caregivers acknowledge an alert
            - Keep an alert history
API:        REST
            POST /pair
            POST /alerts
            POST /alerts/{id}/ack
            GET  /alerts
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Twilio (SMS and voice)
```

---

## Example 71

**Intent:**
kitesurf spot app, users post wind conditions now

**Spec:**
```
Type:       Mobile application with backend (crowdsourced)
Auth:       Email login
Data model: Spot(id, name, lat, lng)
            Condition(id, spot_id -> Spot, user_id -> User, wind_knots, direction, wave_height, photo_url, posted_at)
            User(id, name)
Features:   - Show kite spots on a map with the latest report
            - Post current wind and wave conditions with a photo
            - Combine user reports with a wind forecast
            - Follow spots and get alerts when wind is good
API:        REST
            GET  /spots
            GET  /spots/{id}/conditions
            POST /spots/{id}/conditions
            POST /spots/{id}/follow
Storage:    PostgreSQL
Tech stack: React Native, Express, Open-Meteo API
```

---

## Example 72

**Intent:**
make app plz for my taxi company, 30 cars, customers call now but want app

**Spec:**
```
Type:       Mobile application with backend (taxi dispatch)
Auth:       Customer phone login with SMS code; drivers log in with company ID
Data model: Customer(id, phone, name)
            Driver(id, company_id, name, car_plate, status, lat, lng)
            Trip(id, customer_id -> Customer, driver_id -> Driver, pickup, dropoff, booked_for, status, fare)
Features:   - Book a taxi now or for a later time
            - Dispatch to the nearest free driver automatically
            - Let dispatchers reassign trips from a web panel
            - Show the car's position and plate number to the customer
            - Calculate the fare from the taximeter tariff
API:        REST + WebSocket
            POST /trips
            PATCH /trips/{id}
            POST /drivers/me/location
            WS   /dispatch
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Laravel, Pusher
```

---

## Example 73

**Intent:**
a scavenger hunt game with friends using gps, you find checkpoints in the city

**Spec:**
```
Type:       Mobile game (location-based, multiplayer)
Auth:       Login with Google
Data model: Hunt(id, creator_id -> Player, title, city)
            Checkpoint(id, hunt_id -> Hunt, lat, lng, radius_m, riddle, order)
            Team(id, hunt_id -> Hunt, name)
            Player(id, name, team_id -> Team)
            Capture(team_id -> Team, checkpoint_id -> Checkpoint, captured_at, photo_url)
Features:   - Create a hunt with checkpoints and riddles
            - Join a team with friends
            - Unlock a checkpoint when inside its GPS radius
            - Require a photo proof at each checkpoint
            - Show a live team ranking
API:        REST + WebSocket
            POST /hunts
            POST /hunts/{id}/teams
            POST /checkpoints/{id}/capture
            WS   /hunts/{id}/scores
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Unity (C#), Firebase Auth, Node.js
```

---

## Example 74

**Intent:**
event check-in app with qr tickets

**Spec:**
```
Type:       Mobile application with backend (ticketing)
Auth:       Organizer email login; door staff get scanner access per event
Data model: Event(id, organizer_id -> Organizer, name, date, venue)
            Ticket(id, event_id -> Event, holder_name, email, qr_token, checked_in_at)
            Organizer(id, email)
Features:   - Generate a QR ticket for each attendee
            - Email tickets to attendees
            - Scan QR codes at the door to check people in
            - Reject tickets already used
            - Show a live count of checked-in guests
API:        REST
            POST /events
            POST /events/{id}/tickets
            POST /checkin
            GET  /events/{id}/stats
Storage:    PostgreSQL
Tech stack: React Native (Expo Camera), Node.js, SendGrid
```

---

## Example 75

**Intent:**
My brother and I want to build a fantasy league app for our local amateur cricket league so friends can pick players and score points from real match stats that the league scorer enters after each game.

**Spec:**
```
Type:       Mobile application with backend (fantasy sports)
Auth:       Email login; league scorer has admin role
Data model: User(id, name, email)
            Player(id, name, club, role, price)
            FantasyTeam(id, user_id -> User, name, budget_left)
            Pick(team_id -> FantasyTeam, player_id -> Player, is_captain)
            MatchStat(id, player_id -> Player, match_date, runs, wickets, catches, points)
Features:   - Pick a squad of 11 within a budget
            - Choose a captain who scores double points
            - Let the scorer enter stats after each match
            - Calculate fantasy points automatically
            - Show a season leaderboard
API:        REST
            GET  /players
            POST /teams
            PUT  /teams/{id}/picks
            POST /matches/stats
            GET  /leaderboard
Storage:    PostgreSQL
Tech stack: React Native, Django REST Framework
```

---

## Example 76

**Intent:**
app for moving companies to give quotes from photos of your stuff

**Spec:**
```
Type:       Mobile application with backend (quotes marketplace)
Auth:       Email login for customers and movers
Data model: Customer(id, name, email)
            MoveRequest(id, customer_id -> Customer, from_address, to_address, move_date, photos, room_count)
            Mover(id, company, email, rating)
            Quote(id, request_id -> MoveRequest, mover_id -> Mover, price, notes, status)
Features:   - Post a move with addresses, date and room photos
            - Notify movers who serve that area
            - Let movers send quotes
            - Compare quotes and accept one
            - Message the chosen mover
API:        REST
            POST /moves
            GET  /moves/open
            POST /moves/{id}/quotes
            POST /quotes/{id}/accept
Storage:    PostgreSQL, S3 (photos)
Tech stack: Flutter, NestJS
```

---

## Example 77

**Intent:**
hey so we're doing a hackathon and want a chat where you can only talk to people within 500m of you

**Spec:**
```
Type:       Mobile application with backend (proximity chat)
Auth:       Anonymous accounts with random usernames
Data model: User(id, username, last_lat, last_lng, last_seen)
            Message(id, user_id -> User, text, lat, lng, sent_at)
Features:   - Show messages posted within 500 m of your current position
            - Post short text messages tagged with location
            - Update the visible feed as you move
            - Delete messages older than 24 hours
API:        REST + WebSocket
            GET  /messages/nearby?lat={lat}&lng={lng}
            POST /messages
            WS   /feed
Storage:    Redis (geospatial index)
Tech stack: React Native (Expo), Node.js, Redis GEO commands
```

---

## Example 78

**Intent:**
Plant swap community app

**Spec:**
```
Type:       Mobile application with backend (community)
Auth:       Email login
Data model: Member(id, name, city)
            Plant(id, owner_id -> Member, species, cutting_or_full, photo_url, available)
            SwapRequest(id, plant_id -> Plant, requester_id -> Member, message, status)
Features:   - Post plants and cuttings available to swap
            - Browse plants in your city
            - Send a swap request with a message
            - Organize local swap meetups
API:        REST
            GET  /plants?city={city}
            POST /plants
            POST /plants/{id}/requests
            PATCH /requests/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 79

**Intent:**
app for my parking lot, people pay for parking with phone and enforcement checks plates

**Spec:**
```
Type:       Mobile application with backend (parking)
Auth:       Driver email login; enforcement officers have staff accounts
Data model: Driver(id, email, default_plate)
            Lot(id, name, hourly_rate, max_hours)
            ParkingSession(id, lot_id -> Lot, plate, driver_id -> Driver, starts_at, ends_at, paid)
            Citation(id, lot_id -> Lot, plate, officer_id -> Officer, issued_at, reason)
            Officer(id, name)
Features:   - Start a parking session by lot number and plate
            - Extend a session remotely before it expires
            - Remind drivers 10 minutes before expiry
            - Let officers look up a plate to check payment
            - Issue a citation for unpaid cars
API:        REST
            POST /sessions
            POST /sessions/{id}/extend
            GET  /lots/{id}/plates/{plate}
            POST /citations
Storage:    PostgreSQL
Tech stack: React Native, Spring Boot, Stripe
```

---

## Example 80

**Intent:**
dating app for people over 50

**Spec:**
```
Type:       Mobile application with backend (dating)
Auth:       Email login with selfie verification
Data model: Member(id, name, birth_year, gender, seeking, bio, city, verified)
            Photo(id, member_id -> Member, url, position)
            Interest(from_id -> Member, to_id -> Member, created_at)
            Conversation(id, member_a -> Member, member_b -> Member)
            Message(id, conversation_id -> Conversation, sender_id -> Member, body, sent_at)
Features:   - Create a profile with large, easy-to-read text
            - Browse suggested members by age range and distance
            - Send interest and start a chat on mutual interest
            - Verify members with a selfie check
            - Block and report members
API:        REST
            GET  /suggestions
            POST /interests
            GET  /conversations
            POST /conversations/{id}/messages
            POST /reports
Storage:    PostgreSQL, S3 (photos)
Tech stack: Flutter, Node.js, AWS Rekognition (selfie check)
```

---

## Example 81

**Intent:**
amazon style delivery tracking for my bakery's wholesale customers

**Spec:**
```
Type:       Mobile application with backend (delivery tracking)
Auth:       Business customer email login; driver PIN login
Data model: BusinessCustomer(id, name, email, address)
            Delivery(id, customer_id -> BusinessCustomer, driver_id -> Driver, date, eta, status)
            Driver(id, name, pin_hash, lat, lng)
Features:   - Show customers today's delivery with an ETA
            - Update ETA from the driver's live location
            - Notify customers when the driver is 10 minutes away
            - Capture a signature on delivery
API:        REST
            GET  /deliveries/today
            POST /drivers/me/location
            PATCH /deliveries/{id}
Storage:    PostgreSQL
Tech stack: Flutter, FastAPI, Google Distance Matrix API
```

---

## Example 82

**Intent:**
nail salon booking app with each technician calendar

**Spec:**
```
Type:       Mobile application with backend (appointments)
Auth:       Customer phone login with SMS code; salon staff login
Data model: Technician(id, name, services)
            Service(id, name, duration_min, price)
            Appointment(id, customer_id -> Customer, technician_id -> Technician, service_id -> Service, starts_at, status)
            Customer(id, name, phone)
Features:   - Pick a service and a technician
            - Show free slots from that technician's calendar
            - Book, reschedule and cancel appointments
            - Send SMS reminders the day before
API:        REST
            GET  /services
            GET  /technicians/{id}/slots?date={date}
            POST /appointments
            PATCH /appointments/{id}
Storage:    PostgreSQL
Tech stack: React Native, Laravel, Twilio
```

---

## Example 83

**Intent:**
i make jewelry and sell at craft fairs. would love an app that tells my followers which fair im at this weekend and they can reserve a piece to see in person

**Spec:**
```
Type:       Mobile application with backend (maker shop)
Auth:       Follower login with email; seller admin account
Data model: Fair(id, name, location, date, booth)
            Piece(id, name, price, photo_url, status)
            Reservation(id, piece_id -> Piece, follower_id -> Follower, fair_id -> Fair, status)
            Follower(id, name, email)
Features:   - Post upcoming fairs with booth number
            - Show the jewelry catalog with photos
            - Reserve a piece to see at a fair
            - Notify followers when a new fair is added
            - Release reservations not picked up after the fair
API:        REST
            GET  /fairs
            POST /fairs
            GET  /pieces
            POST /pieces/{id}/reserve
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase
```

---

## Example 84

**Intent:**
Mobile app for my sushi restaurant: online ordering for takeaway and loyalty points.

**Spec:**
```
Type:       Mobile application with backend (restaurant ordering)
Auth:       Email or phone login
Data model: Customer(id, name, phone, points)
            MenuItem(id, name, category, price, image_url)
            Order(id, customer_id -> Customer, pickup_time, total, status)
            OrderLine(order_id -> Order, item_id -> MenuItem, qty)
            PointsTransaction(id, customer_id -> Customer, delta, reason)
Features:   - Show the menu by category
            - Order takeaway with a pickup time
            - Earn 1 point per euro spent
            - Redeem points for a discount at checkout
            - Send the order to a kitchen printer
API:        REST
            GET  /menu
            POST /orders
            GET  /me/points
            POST /orders/{id}/redeem
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Stripe, ESC/POS printer integration
```

---

## Example 85

**Intent:**
an app where i can see when my washing machine is done

**Spec:**
```
Type:       IoT system (with mobile companion app)
Auth:       Email login
Data model: User(id, email)
            Appliance(id, owner_id -> User, name, sensor_id)
            Cycle(id, appliance_id -> Appliance, started_at, finished_at)
Features:   - Detect cycle start and end from a vibration or power sensor
            - Send a push notification when the cycle finishes
            - Show the history of cycles
            - Share the appliance with housemates
API:        REST
            POST /appliances
            GET  /appliances/{id}/cycles
            POST /devices/events
Storage:    PostgreSQL
Tech stack: ESP8266 with Shelly plug, Home Assistant webhook, Flutter, Firebase Cloud Messaging
```

---

## Example 86

**Intent:**
gym buddy matching app based on workout times

**Spec:**
```
Type:       Mobile application with backend (matching)
Auth:       Email or Apple login
Data model: User(id, name, gym_id -> Gym, goals, level)
            Gym(id, name, address)
            Availability(user_id -> User, weekday, start_time, end_time)
            BuddyRequest(id, from_id -> User, to_id -> User, status)
Features:   - Pick your gym and weekly workout times
            - Suggest buddies at the same gym with overlapping times
            - Send and accept buddy requests
            - Chat with buddies
API:        REST
            GET  /buddies/suggested
            POST /buddy-requests
            PATCH /buddy-requests/{id}
Storage:    PostgreSQL
Tech stack: SwiftUI, Vapor (Swift server)
```

---

## Example 87

**Intent:**
we want a mobile app for our hiking club in Kotlin with a Spring backend, members sign up for trips and carpool to the trailhead

**Spec:**
```
Type:       Mobile application with backend (club events)
Auth:       Email + password login with JWT
Data model: Member(id, name, email, has_car, seats)
            Trip(id, title, trailhead, date, difficulty, max_people)
            TripSignup(trip_id -> Trip, member_id -> Member, is_driver, ride_with -> Member)
Features:   - List upcoming club trips with difficulty
            - Sign up for a trip until it is full
            - Offer seats as a driver or ask for a ride
            - Match riders to drivers for each trip
            - Notify members of trip changes
API:        REST
            GET  /trips
            POST /trips/{id}/signups
            GET  /trips/{id}/rides
            PUT  /trips/{id}/signups/me
Storage:    PostgreSQL
Tech stack: Kotlin (Jetpack Compose), Spring Boot, Spring Security (JWT)
```

---

## Example 88

**Intent:**
social app where you post what you're cooking tonight

**Spec:**
```
Type:       Mobile application with backend (social)
Auth:       Email or Google login
Data model: User(id, username, avatar_url)
            Post(id, user_id -> User, photo_url, dish_name, recipe_link, created_at)
            Follow(follower_id -> User, followee_id -> User)
            Like(post_id -> Post, user_id -> User)
Features:   - Post a photo of tonight's dinner
            - Follow friends and see their dinners in a feed
            - Like and comment on posts
            - Show a daily "what's cooking" trending list
API:        REST
            GET  /feed
            POST /posts
            POST /users/{id}/follow
            POST /posts/{id}/like
Storage:    PostgreSQL, S3 (photos)
Tech stack: React Native, Express
```

---

## Example 89

**Intent:**
I work at a pharmacy. Want an app where patients upload prescription photo and we tell them when the medicine is ready to collect.

**Spec:**
```
Type:       Mobile application with backend (healthcare)
Auth:       Patient phone login with SMS code; pharmacist staff login
Data model: Patient(id, name, phone, date_of_birth)
            Prescription(id, patient_id -> Patient, image_url, status, uploaded_at, ready_at)
            StaffNote(id, prescription_id -> Prescription, text)
Features:   - Upload a photo of a paper prescription
            - Show pharmacists a queue of new prescriptions
            - Mark prescriptions as in progress or ready
            - Notify the patient by push when ready
            - Delete images after collection
API:        REST
            POST /prescriptions
            GET  /prescriptions
            PATCH /prescriptions/{id}
Storage:    PostgreSQL, encrypted S3 bucket (images)
Tech stack: Flutter, Django REST Framework
```

---

## Example 90

**Intent:**
city bus app showing where the bus is right now

**Spec:**
```
Type:       Mobile application with backend (real-time transit)
Auth:       No login for riders; drivers log in on a tablet with an ID
Data model: Route(id, number, name)
            Stop(id, route_id -> Route, name, lat, lng, sequence)
            Bus(id, route_id -> Route, lat, lng, updated_at)
Features:   - Send the bus GPS position every 10 seconds from the driver tablet
            - Show buses moving live on a map
            - Estimate arrival time at each stop
            - Save favorite stops
API:        REST + WebSocket
            GET  /routes
            GET  /routes/{id}/stops
            POST /buses/{id}/position
            WS   /routes/{id}/live
Storage:    Redis (live positions), PostgreSQL (routes)
Tech stack: Flutter, Go, GTFS-Realtime format
```

---

## Example 91

**Intent:**
app for photographers to share client galleries and clients pick favs

**Spec:**
```
Type:       Mobile application with backend (client proofing)
Auth:       Photographer email login; clients open galleries with a password link
Data model: Photographer(id, name, email)
            Gallery(id, photographer_id -> Photographer, client_name, password_hash, expires_at)
            Photo(id, gallery_id -> Gallery, url, thumb_url)
            Selection(gallery_id -> Gallery, photo_id -> Photo, comment)
Features:   - Upload a gallery from the phone
            - Share a password-protected link with the client
            - Let the client heart favorite photos and comment
            - Show the photographer the final selection
API:        REST
            POST /galleries
            POST /galleries/{id}/photos
            POST /galleries/{id}/access
            PUT  /galleries/{id}/selections
Storage:    PostgreSQL, Cloudflare R2 (images)
Tech stack: React Native, Node.js, Sharp (thumbnails)
```

---

## Example 92

**Intent:**
mobile game like among us but in real life, players walk around the office and do tasks on their phones

**Spec:**
```
Type:       Mobile game (real-world multiplayer)
Auth:       Guest nicknames inside a private lobby
Data model: Lobby(id, code, status, impostor_count)
            Player(id, lobby_id -> Lobby, nickname, role, alive)
            Task(id, lobby_id -> Lobby, name, qr_code, location_hint)
            TaskCompletion(task_id -> Task, player_id -> Player)
            Vote(lobby_id -> Lobby, voter_id -> Player, target_id -> Player)
Features:   - Assign crewmate or impostor roles secretly
            - Complete tasks by scanning QR codes placed around the office
            - Let impostors eliminate players by tapping a code
            - Call meetings and vote players out
            - Win when all tasks are done or impostors equal crew
API:        REST + WebSocket
            POST /lobbies
            POST /lobbies/{code}/join
            WS   /lobbies/{code}
Storage:    Redis (game state)
Tech stack: React Native, Node.js, Colyseus
```

---

## Example 93

**Intent:**
pls app for my mosque, prayer times, donations and announcements

**Spec:**
```
Type:       Mobile application with backend (community)
Auth:       Optional email login for donors; admin login for mosque staff
Data model: PrayerTime(date, fajr, dhuhr, asr, maghrib, isha)
            Announcement(id, title, body, posted_at)
            Donation(id, donor_email, amount, fund, paid_at)
            Fund(id, name, goal)
Features:   - Show daily prayer and iqama times
            - Send push reminders before each prayer
            - Accept donations to different funds
            - Post announcements from the admin panel
API:        REST
            GET  /prayer-times?date={date}
            GET  /announcements
            POST /announcements
            POST /donations
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 94

**Intent:**
pizza delivery app with driver tracking. using react native and firebase pls

**Spec:**
```
Type:       Mobile application with backend (food delivery)
Auth:       Firebase Authentication (phone number)
Data model: Customer(id, name, phone, address)
            Pizza(id, name, sizes, toppings, price)
            Order(id, customer_id -> Customer, items, total, status, driver_id -> Driver)
            Driver(id, name, location)
Features:   - Build a pizza with size and toppings
            - Place an order and pay by card
            - Show the order stage from oven to on the way
            - Track the driver's location live
            - Rate the delivery
Storage:    Cloud Firestore
Tech stack: React Native, Firebase (Auth, Firestore, Cloud Functions), Stripe
```

---

## Example 95

**Intent:**
Make app for my english school, students see homework, teachers give grades, parents can see too.

**Spec:**
```
Type:       Mobile application with backend (education)
Auth:       Email login with teacher, student and parent roles
Data model: User(id, name, email, role)
            Class(id, name, teacher_id -> User)
            Enrollment(class_id -> Class, student_id -> User)
            Homework(id, class_id -> Class, title, due_date)
            Grade(id, homework_id -> Homework, student_id -> User, score, comment)
            ParentLink(parent_id -> User, student_id -> User)
Features:   - Post homework with due dates
            - Let students submit homework with photos
            - Let teachers grade and comment
            - Show parents their child's grades
            - Notify about new homework
API:        REST
            GET  /classes/{id}/homework
            POST /homework
            POST /homework/{id}/submissions
            PUT  /submissions/{id}/grade
Storage:    PostgreSQL, S3 (submissions)
Tech stack: Flutter, Laravel
```

---

## Example 96

**Intent:**
tennis court booking and finding a partner

**Spec:**
```
Type:       Mobile application with backend (sports booking)
Auth:       Email login
Data model: Player(id, name, ntrp_level, club_id)
            Court(id, club_id, name, surface)
            CourtBooking(id, court_id -> Court, booked_by -> Player, starts_at, ends_at)
            PartnerRequest(id, player_id -> Player, level_wanted, date, status)
Features:   - Book a court in one-hour slots
            - Post a request for a partner at your level
            - Accept a partner request and attach a court booking
            - Report scores to update your level
API:        REST
            GET  /courts/{id}/slots
            POST /bookings
            GET  /partner-requests
            POST /partner-requests/{id}/accept
Storage:    PostgreSQL
Tech stack: React Native, NestJS
```

---

## Example 97

**Intent:**
I want an app where the residents of our village can sell vegetables from their garden to each other

**Spec:**
```
Type:       Mobile application with backend (local marketplace)
Auth:       Phone login with SMS code
Data model: Resident(id, name, phone, street)
            Produce(id, seller_id -> Resident, name, quantity, unit, price, picked_on, photo_url)
            Reservation(id, produce_id -> Produce, buyer_id -> Resident, quantity, status)
Features:   - Post today's garden produce
            - Browse what is available in the village
            - Reserve a quantity and pick up at the seller's house
            - Mark produce as sold out
API:        REST
            GET  /produce
            POST /produce
            POST /produce/{id}/reservations
            PATCH /produce/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 98

**Intent:**
realtime poll app for conferences, audience votes on phone and speaker sees results

**Spec:**
```
Type:       Mobile application with backend (real-time)
Auth:       Speaker login with email; audience joins with an event code
Data model: Speaker(id, email)
            Event(id, speaker_id -> Speaker, code, title)
            Poll(id, event_id -> Event, question, options, open)
            Response(poll_id -> Poll, device_id, option_index)
Features:   - Create polls before the talk
            - Open a poll live during the talk
            - Let the audience vote once per device
            - Show results updating in real time on the speaker screen
            - Collect anonymous audience questions
API:        REST + WebSocket
            POST /events
            POST /events/{id}/polls
            POST /polls/{id}/responses
            WS   /events/{code}
Storage:    Redis, PostgreSQL
Tech stack: Flutter, Node.js, Socket.IO
```

---

## Example 99

**Intent:**
blood donor finder app, hospitals post urgent needs for a blood type

**Spec:**
```
Type:       Mobile application with backend (healthcare, community)
Auth:       Donor phone login with SMS code; hospital accounts verified by admin
Data model: Donor(id, name, phone, blood_type, lat, lng, last_donation_date)
            Hospital(id, name, address, verified)
            BloodRequest(id, hospital_id -> Hospital, blood_type, units_needed, urgency, created_at)
            Response(request_id -> BloodRequest, donor_id -> Donor, status)
Features:   - Register as a donor with blood type
            - Let hospitals post urgent blood requests
            - Alert compatible donors within 20 km
            - Skip donors who donated in the last 3 months
            - Let donors confirm they are coming
API:        REST
            POST /donors
            POST /requests
            GET  /requests/nearby
            POST /requests/{id}/responses
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Django REST Framework, Firebase Cloud Messaging
```

---

## Example 100

**Intent:**
wedding app for guests to upload pics from the party in one album

**Spec:**
```
Type:       Mobile application with backend (event photo sharing)
Auth:       Guests join by scanning a QR code at the venue, name only
Data model: Wedding(id, couple_names, date, join_code)
            Guest(id, wedding_id -> Wedding, name)
            Photo(id, wedding_id -> Wedding, guest_id -> Guest, url, taken_at)
Features:   - Join the wedding album by scanning a QR code
            - Upload photos and videos from the phone
            - Show a shared live album sorted by time
            - Let the couple download all photos as a zip
API:        REST
            POST /weddings/{code}/guests
            POST /weddings/{id}/photos
            GET  /weddings/{id}/photos
            GET  /weddings/{id}/export
Storage:    PostgreSQL, S3 (media)
Tech stack: React Native, Express, AWS S3 presigned uploads
```

---

## Example 101

**Intent:**
drone delivery companion app for a pilot program, customers see the drone coming

**Spec:**
```
Type:       Mobile application with backend (delivery tracking)
Auth:       Customer email login
Data model: Customer(id, name, email, landing_lat, landing_lng)
            Drone(id, serial, battery_pct, lat, lng, altitude)
            DroneDelivery(id, customer_id -> Customer, drone_id -> Drone, status, eta)
Features:   - Pick a safe landing spot in the yard on a map
            - Show the drone's live position and ETA
            - Alert the customer one minute before landing
            - Confirm package received
API:        REST + WebSocket
            POST /deliveries
            GET  /deliveries/{id}
            POST /drones/{id}/telemetry
            WS   /deliveries/{id}/live
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Python, FastAPI, MAVLink telemetry
```

---

## Example 102

**Intent:**
sorry my english. i want app for my gym in Turkey, members see how many people inside now so they come when not crowded

**Spec:**
```
Type:       Mobile application with backend (occupancy)
Auth:       Member login with membership number and phone
Data model: Member(id, membership_no, name, phone)
            Visit(id, member_id -> Member, entered_at, left_at)
            OccupancySnapshot(timestamp, count)
Features:   - Count members inside from entry and exit card scans
            - Show the current number of people on the home screen
            - Show a busy-hours chart for each weekday
            - Notify members when the gym is quiet
API:        REST
            GET  /occupancy/now
            GET  /occupancy/history
            POST /visits/enter
            POST /visits/exit
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, RFID turnstile integration
```

---

## Example 103

**Intent:**
app that matches surplus restaurant food with people who want it cheap at closing time

**Spec:**
```
Type:       Mobile application with backend (marketplace)
Auth:       Email or Google login; restaurant partner accounts
Data model: Restaurant(id, name, address, lat, lng)
            SurpriseBag(id, restaurant_id -> Restaurant, price, quantity_left, pickup_start, pickup_end)
            Purchase(id, bag_id -> SurpriseBag, user_id -> User, paid_at, collected)
            User(id, name, email)
Features:   - Let restaurants post discounted surprise bags before closing
            - Show bags available nearby
            - Pay in the app and get a pickup code
            - Mark bags collected at the shop
API:        REST
            GET  /bags/nearby
            POST /bags
            POST /bags/{id}/purchase
            POST /purchases/{id}/collect
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, NestJS, Stripe
```

---

## Example 104

**Intent:**
Could you make an app for apartment roommates to split bills and track who owes who?

**Spec:**
```
Type:       Mobile application with backend (shared expenses)
Auth:       Email login; roommates join a household by invite
Data model: Household(id, name)
            Member(id, household_id -> Household, name, email)
            Bill(id, household_id -> Household, title, amount, paid_by -> Member, due_date)
            Share(bill_id -> Bill, member_id -> Member, amount, settled)
Features:   - Add bills and split them equally or by custom amounts
            - Show running balances between roommates
            - Simplify debts into the fewest payments
            - Remind roommates of upcoming rent and utilities
            - Mark shares as settled
API:        REST
            GET  /households/{id}/balances
            POST /bills
            PATCH /shares/{bill_id}/{member_id}
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 105

**Intent:**
game where players capture territory by walking around the real map

**Spec:**
```
Type:       Mobile game (location-based, multiplayer)
Auth:       Sign in with Google or Apple
Data model: Player(id, name, team, total_area_m2)
            Tile(id, h3_index, owner_id -> Player, captured_at)
            Walk(id, player_id -> Player, path_geojson, started_at, ended_at)
Features:   - Track the player's GPS path while walking
            - Capture map hexagons when a loop is closed
            - Steal hexagons from other players
            - Show a world map colored by team
            - Rank players by area owned
API:        REST
            POST /walks
            POST /walks/{id}/points
            GET  /tiles?bbox={bbox}
            GET  /leaderboard
Storage:    PostgreSQL with PostGIS, Redis
Tech stack: Flutter, Go, Uber H3, Mapbox
```

---

## Example 106

**Intent:**
app for my sports bar where people predict scores for the game and win a free beer

**Spec:**
```
Type:       Mobile application with backend (loyalty game)
Auth:       Phone login with SMS code
Data model: Customer(id, phone, nickname)
            Match(id, home_team, away_team, kickoff, final_home, final_away)
            Prediction(match_id -> Match, customer_id -> Customer, home_goals, away_goals)
            Prize(id, customer_id -> Customer, match_id -> Match, redeemed)
Features:   - Show tonight's matches
            - Submit a score prediction before kickoff
            - Lock predictions at kickoff
            - Award a free-beer voucher for exact scores
            - Redeem the voucher at the bar with a QR code
API:        REST
            GET  /matches
            POST /matches/{id}/predictions
            POST /matches/{id}/result
            POST /prizes/{id}/redeem
Storage:    PostgreSQL
Tech stack: React Native, Express, football-data.org API
```

---

## Example 107

**Intent:**
house sitting exchange

**Spec:**
```
Type:       Mobile application with backend (marketplace)
Auth:       Email login with ID verification
Data model: Member(id, name, bio, verified, rating)
            Home(id, owner_id -> Member, city, description, pets, photos)
            Sit(id, home_id -> Home, start_date, end_date, sitter_id -> Member, status)
            Application(sit_id -> Sit, sitter_id -> Member, message)
Features:   - List your home with dates you need a sitter
            - Search sits by city and dates
            - Apply to a sit with a message
            - Choose a sitter and confirm
            - Review each other after the sit
API:        REST
            GET  /sits
            POST /sits
            POST /sits/{id}/applications
            POST /sits/{id}/confirm
Storage:    PostgreSQL
Tech stack: Flutter, Ruby on Rails API
```

---

## Example 108

**Intent:**
ok so me n my friends always argue where to eat. app where we each swipe restaurants and it shows the one we all liked

**Spec:**
```
Type:       Mobile application with backend (group decision)
Auth:       Guest nickname per session
Data model: Session(id, code, lat, lng, radius_m)
            Participant(id, session_id -> Session, nickname)
            RestaurantOption(id, session_id -> Session, place_id, name, photo_url)
            SwipeVote(option_id -> RestaurantOption, participant_id -> Participant, liked)
Features:   - Start a session and share the code
            - Load nearby restaurants for everyone to swipe
            - Show a match when all participants like the same place
            - Show the top choices if nobody fully agrees
API:        REST + WebSocket
            POST /sessions
            POST /sessions/{code}/join
            POST /options/{id}/vote
            WS   /sessions/{code}
Storage:    Redis
Tech stack: React Native, Node.js, Google Places API
```

---

## Example 109

**Intent:**
app for managing our apartment's shared laundry room booking

**Spec:**
```
Type:       Mobile application with backend (booking)
Auth:       Resident login with apartment number and PIN
Data model: Resident(id, apartment_no, pin_hash)
            Machine(id, type, label)
            Slot(id, machine_id -> Machine, starts_at, ends_at, resident_id -> Resident)
Features:   - Show washer and dryer slots for the week
            - Book up to 3 slots per week
            - Cancel a booking
            - Remind residents 15 minutes before their slot
API:        REST
            GET  /slots?week={date}
            POST /slots/{id}/book
            DELETE /slots/{id}/book
Storage:    SQLite
Tech stack: Flutter, Python, Flask
```

---

## Example 110

**Intent:**
need a backend + app for a smart bird feeder that takes pictures and tells me what bird it is

**Spec:**
```
Type:       IoT system (with mobile companion app)
Auth:       Email login; feeder linked by serial number
Data model: User(id, email)
            Feeder(id, owner_id -> User, serial, name, food_level)
            Sighting(id, feeder_id -> Feeder, photo_url, species, confidence, seen_at)
Features:   - Upload a photo when the feeder's motion sensor triggers
            - Identify the bird species with an image classifier
            - Show a gallery of visitors by species
            - Notify when a rare species visits
            - Alert when food is running low
API:        REST
            POST /feeders/{id}/sightings
            GET  /feeders/{id}/sightings
            GET  /species/stats
Storage:    PostgreSQL, S3 (photos)
Tech stack: Raspberry Pi camera, Python, FastAPI, TensorFlow Lite, Flutter
```

---

## Example 111

**Intent:**
voice chat rooms app like clubhouse

**Spec:**
```
Type:       Mobile application with backend (live audio)
Auth:       Phone login with SMS code
Data model: User(id, username, bio, avatar_url)
            Room(id, title, host_id -> User, topic, is_live, started_at)
            RoomParticipant(room_id -> Room, user_id -> User, role, hand_raised)
            Follow(follower_id -> User, followee_id -> User)
Features:   - Start a live audio room on a topic
            - Join rooms as a listener
            - Raise a hand and let the host bring you on stage
            - Show live rooms from people you follow
            - End the room and remove all participants
API:        REST + WebSocket
            GET  /rooms/live
            POST /rooms
            POST /rooms/{id}/join
            POST /rooms/{id}/hand
            WS   /rooms/{id}/signal
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Node.js, Agora SDK (audio)
```

---

## Example 112

**Intent:**
barbershop queue app

**Spec:**
```
Type:       Mobile application with backend (virtual queue)
Auth:       Phone number login with SMS code
Data model: Shop(id, name, address, avg_cut_minutes)
            Barber(id, shop_id -> Shop, name, is_working)
            QueueEntry(id, shop_id -> Shop, customer_phone, barber_id -> Barber, position, joined_at, status)
Features:   - Join the queue remotely for a shop or a specific barber
            - Show your position and estimated wait
            - Text the customer when they are 2 places away
            - Let barbers call the next customer from a tablet
API:        REST + WebSocket
            POST /shops/{id}/queue
            GET  /shops/{id}/queue
            POST /shops/{id}/queue/next
            WS   /shops/{id}/queue
Storage:    PostgreSQL
Tech stack: React Native, Express, Twilio
```

---

## Example 113

**Intent:**
scooter rental like lime

**Spec:**
```
Type:       Mobile application with backend (IoT, micromobility)
Auth:       Phone login with SMS code and card on file
Data model: Rider(id, phone, payment_method_id)
            Scooter(id, qr_code, battery_pct, lat, lng, status, locked)
            Ride(id, rider_id -> Rider, scooter_id -> Scooter, started_at, ended_at, distance_m, cost)
            ParkingZone(id, polygon, allowed)
Features:   - Show available scooters with battery level on a map
            - Scan the QR code to unlock a scooter
            - Charge per minute with an unlock fee
            - Only allow ending the ride inside a parking zone
            - Require a photo of the parked scooter
API:        REST
            GET  /scooters/nearby
            POST /rides
            POST /rides/{id}/end
            POST /scooters/{id}/telemetry
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin (Android), Swift (iOS), Go, MQTT, Stripe
```

---

## Example 114

**Intent:**
yo i want an app to rate my friends outfits every day lol like a daily fit check

**Spec:**
```
Type:       Mobile application with backend (social)
Auth:       Sign in with Apple or Google
Data model: User(id, username)
            Friendship(user_id -> User, friend_id -> User, status)
            Fit(id, user_id -> User, photo_url, posted_on)
            Rating(fit_id -> Fit, rater_id -> User, score)
Features:   - Post one outfit photo per day
            - Rate friends' fits from 1 to 10
            - Show the daily top fit among friends
            - Keep a streak counter for daily posting
API:        REST
            POST /fits
            GET  /fits/friends
            POST /fits/{id}/ratings
            POST /friends
Storage:    PostgreSQL, S3 (photos)
Tech stack: SwiftUI, Firebase Auth, Node.js
```

---

## Example 115

**Intent:**
app for elderly people to request help with groceries from young volunteers in the same city

**Spec:**
```
Type:       Mobile application with backend (volunteering)
Auth:       Phone login with SMS code; volunteers verified with ID
Data model: Senior(id, name, phone, address)
            Volunteer(id, name, phone, verified, lat, lng)
            HelpRequest(id, senior_id -> Senior, shopping_list, deliver_by, status, volunteer_id -> Volunteer)
            Receipt(id, request_id -> HelpRequest, amount, photo_url)
Features:   - Let seniors post a shopping list with large simple buttons
            - Show nearby open requests to volunteers
            - Accept a request and contact the senior
            - Upload a receipt photo so the senior can repay
            - Thank volunteers with badges
API:        REST
            POST /requests
            GET  /requests/nearby
            POST /requests/{id}/accept
            POST /requests/{id}/receipt
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Django REST Framework
```

---

## Example 116

**Intent:**
I'm a landscaper with 4 crews. I want each crew lead to have the day's jobs on their phone, take before/after photos, and log hours and materials used so I can bill customers correctly at the end of the month.

**Spec:**
```
Type:       Mobile application with backend (field service)
Auth:       Owner email login; crew leads log in with phone and PIN
Data model: Crew(id, name, lead_id -> Worker)
            Worker(id, name, phone, pin_hash)
            Customer(id, name, address, billing_email)
            Job(id, customer_id -> Customer, crew_id -> Crew, date, tasks, status)
            JobLog(id, job_id -> Job, hours, materials, before_photo_url, after_photo_url)
Features:   - Show each crew its jobs for the day
            - Capture before and after photos per job
            - Log hours and materials used
            - Mark jobs complete with notes
            - Generate monthly invoices per customer
API:        REST
            GET  /crews/me/jobs
            POST /jobs/{id}/logs
            PATCH /jobs/{id}
            GET  /invoices?month={m}
Storage:    PostgreSQL, S3 (photos)
Tech stack: React Native, Ruby on Rails API, QuickBooks Online API
```

---

## Example 117

**Intent:**
dorm room app to report noise and message RA

**Spec:**
```
Type:       Mobile application with backend (residential life)
Auth:       University single sign-on
Data model: Student(id, name, room_id -> Room)
            Room(id, building, floor, number)
            RA(id, name, floor)
            NoiseReport(id, reporter_id -> Student, room_reported, note, created_at, status)
            Message(id, student_id -> Student, ra_id -> RA, body, sent_at)
Features:   - Report noise from a specific room anonymously
            - Notify the RA on duty
            - Message your RA privately
            - Show quiet hours and floor events
API:        REST
            POST /noise-reports
            GET  /ra/reports
            POST /messages
            GET  /events
Storage:    PostgreSQL
Tech stack: React Native, Node.js, SAML (Shibboleth)
```

---

## Example 118

**Intent:**
Peer-to-peer car rental app.

**Spec:**
```
Type:       Mobile application with backend (marketplace)
Auth:       Email login with driver's license verification
Data model: User(id, name, email, license_verified)
            Car(id, owner_id -> User, make, model, year, daily_price, location, photos)
            Rental(id, car_id -> Car, renter_id -> User, start_date, end_date, total, status)
            Inspection(id, rental_id -> Rental, phase, photos, fuel_level, odometer)
Features:   - List a car with photos, price and availability
            - Search cars by location and dates
            - Book and pay with a security deposit
            - Record photos and odometer at pickup and return
            - Review owners and renters
API:        REST
            GET  /cars?lat={lat}&lng={lng}&from={d}&to={d}
            POST /cars
            POST /rentals
            POST /rentals/{id}/inspections
Storage:    PostgreSQL, S3 (photos)
Tech stack: Flutter, NestJS, Stripe, Onfido (ID verification)
```

---

## Example 119

**Intent:**
pls build chat app for my customers to talk with support, in flutter

**Spec:**
```
Type:       Mobile application with backend (customer support chat)
Auth:       Customer email login; agents log in to a web dashboard
Data model: Customer(id, name, email)
            Agent(id, name, email, online)
            Ticket(id, customer_id -> Customer, agent_id -> Agent, status, opened_at)
            Message(id, ticket_id -> Ticket, sender_type, text, attachment_url, sent_at)
Features:   - Open a support conversation from the app
            - Assign new conversations to an online agent
            - Send text and image attachments
            - Show typing indicators and read receipts
            - Rate the support after closing
API:        REST + WebSocket
            POST /tickets
            GET  /tickets/{id}/messages
            POST /tickets/{id}/messages
            PATCH /tickets/{id}
            WS   /tickets/{id}
Storage:    PostgreSQL, S3 (attachments)
Tech stack: Flutter, Node.js, Socket.IO
```

---

## Example 120

**Intent:**
daily vocab duel game with friends

**Spec:**
```
Type:       Mobile game (asynchronous multiplayer)
Auth:       Sign in with Google or Apple
Data model: Player(id, name, rating)
            Duel(id, player_a -> Player, player_b -> Player, date, status)
            DuelRound(duel_id -> Duel, word, a_answer, b_answer, a_time_ms, b_time_ms)
Features:   - Challenge a friend to a daily word duel
            - Play 5 rounds asynchronously
            - Score by correctness and speed
            - Update an Elo rating after each duel
            - Notify when it is your turn
API:        REST
            POST /duels
            GET  /duels
            POST /duels/{id}/rounds
            GET  /players/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Firebase (Auth, Firestore, Cloud Functions)
```

---

## Example 121

**Intent:**
track my kids phones location and get alert when they leave school

**Spec:**
```
Type:       Mobile application with backend (family location)
Auth:       Parent email login; child devices paired with a code
Data model: Parent(id, email)
            Child(id, parent_id -> Parent, name, device_id)
            Geofence(id, parent_id -> Parent, name, lat, lng, radius_m)
            LocationPing(child_id -> Child, lat, lng, recorded_at)
            GeofenceEvent(id, child_id -> Child, geofence_id -> Geofence, type, at)
Features:   - Show each child's location on a map
            - Define places like school and home as geofences
            - Notify parents when a child enters or leaves a place
            - Show today's location history
API:        REST
            POST /children/pair
            POST /pings
            GET  /children/{id}/location
            POST /geofences
            GET  /events
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin (Android), Swift (iOS, Core Location), Node.js
```

---

## Example 122

**Intent:**
Hi! I'm a yoga teacher and I teach in parks in summer. I want students to see where class is today (changes with weather), sign up, and pay drop-in or with a 10-class pass.

**Spec:**
```
Type:       Mobile application with backend (class booking)
Auth:       Student email login; teacher admin
Data model: Student(id, name, email, pass_credits)
            ClassEvent(id, location_name, lat, lng, starts_at, capacity, status)
            Signup(class_id -> ClassEvent, student_id -> Student, paid_with)
            Pass(id, student_id -> Student, credits, purchased_at)
Features:   - Post today's class with a park location on the map
            - Sign up and pay drop-in or use a pass credit
            - Buy a 10-class pass
            - Notify students if class moves or is cancelled for rain
API:        REST
            GET  /classes
            POST /classes
            POST /classes/{id}/signups
            POST /passes
Storage:    PostgreSQL
Tech stack: React Native, Supabase, Stripe
```

---

## Example 123

**Intent:**
anonymous Q&A with classmates

**Spec:**
```
Type:       Mobile application with backend (social)
Auth:       School email verification
Data model: Student(id, school_email_hash, school_id)
            Question(id, author_id -> Student, school_id, text, created_at)
            Answer(id, question_id -> Question, author_id -> Student, text, upvotes)
Features:   - Ask questions anonymously to your school
            - Answer and upvote answers
            - Filter abusive language before posting
            - Let school moderators remove posts
API:        REST
            GET  /questions
            POST /questions
            POST /questions/{id}/answers
            POST /answers/{id}/upvote
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI
```

---

## Example 124

**Intent:**
firewood delivery app for our rural area

**Spec:**
```
Type:       Mobile application with backend (delivery ordering)
Auth:       Phone login
Data model: Customer(id, name, phone, address, lat, lng)
            Product(id, wood_type, unit, price)
            Order(id, customer_id -> Customer, product_id -> Product, quantity, delivery_date, status)
Features:   - Order firewood by cord or half-cord
            - Choose a delivery day from available route days
            - Group orders into delivery runs by area
            - Text customers the day before delivery
API:        REST
            GET  /products
            POST /orders
            GET  /delivery-days
            GET  /runs?date={date}
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Twilio
```

---

## Example 125

**Intent:**
ice hockey team app for beer league, tracks who's paying for ice time

**Spec:**
```
Type:       Mobile application with backend (sports team)
Auth:       Email login with captain role
Data model: Team(id, name, captain_id -> Player)
            Player(id, team_id -> Team, name, position)
            Game(id, team_id -> Team, rink, starts_at, ice_cost)
            Availability(game_id -> Game, player_id -> Player, status)
            Payment(id, player_id -> Player, game_id -> Game, amount, paid)
Features:   - List the season schedule
            - Mark yourself in or out for each game
            - Warn the captain when fewer than 10 skaters are in
            - Split ice cost among players who show up
            - Track who has paid
API:        REST
            GET  /teams/{id}/games
            PUT  /games/{id}/availability
            GET  /games/{id}/payments
            PATCH /payments/{id}
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 126

**Intent:**
app to report potholes to city with photo and gps

**Spec:**
```
Type:       Mobile application with backend (civic reporting)
Auth:       Optional email login; city staff accounts
Data model: Report(id, category, description, photo_url, lat, lng, status, reporter_email, created_at)
            StaffUser(id, name, department)
            StatusUpdate(id, report_id -> Report, staff_id -> StaffUser, status, note, at)
Features:   - Report a pothole, broken light or graffiti with a photo
            - Attach the GPS location automatically
            - Detect duplicates within 20 m
            - Let city staff update the status
            - Notify the reporter when it is fixed
API:        REST
            POST /reports
            GET  /reports?bbox={bbox}
            PATCH /reports/{id}
            GET  /reports/{id}/updates
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: React Native, Django REST Framework, GeoDjango
```

---

## Example 127

**Intent:**
app for my wine club, members rate wines at tastings

**Spec:**
```
Type:       Mobile application with backend (club)
Auth:       Email login
Data model: Member(id, name, email)
            Tasting(id, date, host_id -> Member, theme)
            Wine(id, name, vintage, region, grape)
            TastingWine(tasting_id -> Tasting, wine_id -> Wine)
            Score(wine_id -> Wine, tasting_id -> Tasting, member_id -> Member, points, notes)
Features:   - Create a tasting with the wines to try
            - Score each wine blind with notes
            - Reveal wine names and average scores at the end
            - Show each member's favorite regions
API:        REST
            POST /tastings
            POST /tastings/{id}/scores
            POST /tastings/{id}/reveal
            GET  /members/{id}/stats
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 128

**Intent:**
Im a personal trainer. clients should log workouts on their phone and i can see it and leave comments

**Spec:**
```
Type:       Mobile application with backend (coaching)
Auth:       Trainer and client email login
Data model: Trainer(id, name, email)
            Client(id, trainer_id -> Trainer, name, email)
            Program(id, client_id -> Client, name, weeks)
            Workout(id, client_id -> Client, date, exercises_json, notes)
            Comment(id, workout_id -> Workout, trainer_id -> Trainer, text)
Features:   - Assign a training program to each client
            - Let clients log sets, reps and weights
            - Show the trainer a feed of client workouts
            - Comment on workouts
            - Chart a client's progress on main lifts
API:        REST
            GET  /clients
            POST /programs
            POST /workouts
            GET  /clients/{id}/workouts
            POST /workouts/{id}/comments
Storage:    PostgreSQL
Tech stack: React Native, NestJS
```

---

## Example 129

**Intent:**
app where musicians find bandmates

**Spec:**
```
Type:       Mobile application with backend (matching)
Auth:       Email or Google login
Data model: Musician(id, name, instruments, genres, level, city)
            BandAd(id, author_id -> Musician, looking_for, genres, city)
            Message(id, from_id -> Musician, to_id -> Musician, body, sent_at)
            Clip(id, musician_id -> Musician, audio_url)
Features:   - Create a profile with instruments, genres and audio clips
            - Post an ad looking for a bandmate
            - Search musicians by instrument and city
            - Message other musicians
API:        REST
            GET  /musicians?instrument={i}
            POST /ads
            GET  /ads
            POST /messages
Storage:    PostgreSQL, S3 (audio)
Tech stack: Flutter, Node.js
```

---

## Example 130

**Intent:**
snow plow app: customers request driveway clearing after a snowfall, nearest plow driver takes it

**Spec:**
```
Type:       Mobile application with backend (on-demand service)
Auth:       Phone login with SMS code for customers and drivers
Data model: Customer(id, phone, address, lat, lng, driveway_size)
            PlowDriver(id, phone, is_online, lat, lng)
            ClearingJob(id, customer_id -> Customer, driver_id -> PlowDriver, price, status, after_photo_url)
Features:   - Request driveway clearing with one tap
            - Price the job by driveway size
            - Offer the job to the nearest online driver
            - Upload an after photo when done
            - Charge the customer automatically
API:        REST
            POST /jobs
            POST /jobs/{id}/accept
            POST /jobs/{id}/complete
            POST /drivers/me/location
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Go, Stripe
```

---

## Example 131

**Intent:**
crowd-sourced gas prices

**Spec:**
```
Type:       Mobile application with backend (crowdsourced)
Auth:       Optional email login
Data model: Station(id, name, brand, lat, lng)
            FuelPrice(id, station_id -> Station, fuel_type, price, reported_by, reported_at)
Features:   - Show cheapest stations nearby by fuel type
            - Report the current price at a station
            - Sort by price or distance
            - Show how old each price is
API:        REST
            GET  /stations/nearby?fuel={type}
            POST /stations/{id}/prices
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin (Android), Ktor
```

---

## Example 132

**Intent:**
social app for sharing what books ur reading with friends, with goodreads import

**Spec:**
```
Type:       Mobile application with backend (social reading)
Auth:       Email or Google login
Data model: Reader(id, name, avatar_url)
            Book(id, isbn, title, author, cover_url)
            Shelf(reader_id -> Reader, book_id -> Book, status, rating, finished_at)
            Follow(follower_id -> Reader, followee_id -> Reader)
Features:   - Import a reading history from a Goodreads CSV export
            - Mark books as reading, finished or want to read
            - Show a feed of friends' reading updates
            - Set a yearly reading goal
API:        REST
            POST /imports/goodreads
            GET  /feed
            PUT  /shelf/{book_id}
            GET  /books/search?q={q}
Storage:    PostgreSQL
Tech stack: React Native, FastAPI, Open Library API
```

---

## Example 133

**Intent:**
we are association of beekeepers in Slovenia, want app where members register hives and report swarms, other members can come catch the swarm

**Spec:**
```
Type:       Mobile application with backend (association)
Auth:       Member email login approved by the association
Data model: Member(id, name, email, phone, region)
            Hive(id, member_id -> Member, lat, lng, colonies)
            SwarmReport(id, reporter_name, phone, lat, lng, photo_url, status, catcher_id -> Member, reported_at)
Features:   - Register hive locations
            - Let the public report a swarm with photo and location
            - Notify members near the swarm
            - Let one member claim the swarm
            - Mark swarms as caught
API:        REST
            POST /hives
            POST /swarms
            GET  /swarms/open
            POST /swarms/{id}/claim
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Django REST Framework
```

---

## Example 134

**Intent:**
digital business card app, tap phones to share contact

**Spec:**
```
Type:       Mobile application with backend
Auth:       Email or LinkedIn login
Data model: User(id, name, title, company, phone, email, links)
            Card(id, user_id -> User, slug, theme)
            Connection(id, owner_id -> User, contact_user_id -> User, met_at, note)
Features:   - Design a digital business card
            - Share the card with NFC tap or QR code
            - Open shared cards as a web page for people without the app
            - Save received cards to your contacts
            - Add notes about where you met
API:        REST
            GET  /cards/{slug}
            PUT  /cards/me
            POST /connections
Storage:    PostgreSQL
Tech stack: React Native, NFC Manager library, Next.js (public card pages)
```

---

## Example 135

**Intent:**
app for food bank to schedule pickups from grocery stores with surplus

**Spec:**
```
Type:       Mobile application with backend (logistics)
Auth:       Email login for store managers and volunteer drivers
Data model: Store(id, name, address, manager_email)
            Donation(id, store_id -> Store, description, weight_kg, ready_at, status)
            Driver(id, name, phone)
            Pickup(id, donation_id -> Donation, driver_id -> Driver, picked_at)
Features:   - Let stores post surplus food ready for pickup
            - Notify volunteer drivers of new donations
            - Claim a pickup and get directions
            - Log pounds collected per store
            - Report monthly totals
API:        REST
            POST /donations
            GET  /donations/open
            POST /donations/{id}/claim
            GET  /reports/monthly
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 136

**Intent:**
pub crawl game app

**Spec:**
```
Type:       Mobile game (location-based, social)
Auth:       Guest names inside a crawl group
Data model: Crawl(id, code, name, route)
            Bar(id, name, lat, lng)
            CrawlStop(crawl_id -> Crawl, bar_id -> Bar, order)
            Participant(id, crawl_id -> Crawl, name, points)
            Challenge(id, stop_id, text, points)
Features:   - Create a crawl route of bars
            - Check in at each bar when nearby
            - Complete challenges at each stop for points
            - Show the group leaderboard
API:        REST
            POST /crawls
            POST /crawls/{code}/join
            POST /stops/{id}/checkin
            GET  /crawls/{code}/scores
Storage:    Firebase Realtime Database
Tech stack: Flutter, Firebase
```

---

## Example 137

**Intent:**
secure messaging app for a law firm and its clients

**Spec:**
```
Type:       Mobile application with backend (secure messaging)
Auth:       Email + password with mandatory two-factor authentication
Data model: Lawyer(id, name, email)
            Client(id, name, email)
            Matter(id, title, lawyer_id -> Lawyer, client_id -> Client)
            Message(id, matter_id -> Matter, sender_id, ciphertext, sent_at)
            Document(id, matter_id -> Matter, file_url, uploaded_at)
Features:   - Organize conversations by legal matter
            - Encrypt messages end to end
            - Share documents securely
            - Keep an audit log of access
            - Wipe local data after failed unlock attempts
API:        REST + WebSocket
            GET  /matters
            GET  /matters/{id}/messages
            POST /matters/{id}/messages
            POST /matters/{id}/documents
            WS   /ws
Storage:    PostgreSQL, encrypted S3 bucket
Tech stack: Swift (iOS), Kotlin (Android), libsignal, ASP.NET Core
```

---

## Example 138

**Intent:**
little league baseball live scoring for parents who cant attend

**Spec:**
```
Type:       Mobile application with backend (live sports)
Auth:       Scorekeeper login; parents follow teams without an account
Data model: Team(id, name, league)
            Game(id, home_id -> Team, away_id -> Team, starts_at, inning, home_runs, away_runs, status)
            Play(id, game_id -> Game, inning, description, created_at)
Features:   - Let the scorekeeper enter plays pitch by pitch
            - Update the score live for followers
            - Show a play-by-play feed
            - Send a push alert at the end of the game
API:        REST + WebSocket
            GET  /games/{id}
            POST /games/{id}/plays
            WS   /games/{id}/live
Storage:    PostgreSQL
Tech stack: React Native, Supabase Realtime
```

---

## Example 139

**Intent:**
Swift app + backend for sharing parking spots in our office garage when people are on vacation

**Spec:**
```
Type:       Mobile application with backend (resource sharing)
Auth:       Company email login via Microsoft Entra ID
Data model: Employee(id, name, email)
            Spot(id, number, owner_id -> Employee)
            Release(id, spot_id -> Spot, date)
            Claim(id, release_id -> Release, employee_id -> Employee)
Features:   - Release your assigned spot for days you are away
            - Claim a released spot for a day
            - Notify employees on the waitlist when a spot frees up
            - Show today's spot on the home screen
API:        REST
            POST /releases
            GET  /releases?date={date}
            POST /releases/{id}/claim
Storage:    PostgreSQL
Tech stack: Swift (SwiftUI), Vapor, MSAL
```

---

## Example 140

**Intent:**
memory game multiplayer online

**Spec:**
```
Type:       Mobile game (turn-based multiplayer)
Auth:       Guest play with optional Google login
Data model: Player(id, nickname, wins)
            Match(id, player1 -> Player, player2 -> Player, board_seed, turn, status)
            Move(match_id -> Match, player_id -> Player, card_a, card_b, matched)
Features:   - Find a random opponent or invite a friend
            - Flip two cards per turn and keep the turn on a match
            - Sync the board in real time
            - Declare a winner by pairs found
API:        REST + WebSocket
            POST /matches/queue
            POST /matches/invite
            WS   /matches/{id}
Storage:    Redis, PostgreSQL
Tech stack: Godot (GDScript), Node.js
```

---

## Example 141

**Intent:**
plumbers app to get emergency jobs at night

**Spec:**
```
Type:       Mobile application with backend (on-call marketplace)
Auth:       Email login with plumber license verification
Data model: Plumber(id, name, phone, license_no, on_call, lat, lng)
            Homeowner(id, name, phone)
            EmergencyJob(id, homeowner_id -> Homeowner, plumber_id -> Plumber, description, photo_url, callout_fee, status, created_at)
Features:   - Let homeowners post an emergency with a photo
            - Alert on-call plumbers within 15 km
            - Accept a job and share ETA
            - Show the callout fee upfront
            - Pay after the visit
API:        REST
            POST /jobs
            GET  /jobs/open
            POST /jobs/{id}/accept
            POST /jobs/{id}/complete
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Node.js, Stripe
```

---

## Example 142

**Intent:**
whats a good way to make an app where my customers book my mobile car wash and I see bookings on a map?

**Spec:**
```
Type:       Mobile application with backend (booking)
Auth:       Customer phone login; owner admin login
Data model: Customer(id, name, phone)
            Vehicle(id, customer_id -> Customer, type, plate)
            Booking(id, customer_id -> Customer, vehicle_id -> Vehicle, package, address, lat, lng, scheduled_at, status)
Features:   - Choose a wash package and time slot
            - Enter the address where the car is parked
            - Show the owner all bookings on a map for the day
            - Order the day's stops by shortest route
            - Notify the customer when on the way
API:        REST
            POST /bookings
            GET  /bookings?date={date}
            PATCH /bookings/{id}
            GET  /route?date={date}
Storage:    PostgreSQL
Tech stack: Flutter, FastAPI, Google Maps SDK
```

---

## Example 143

**Intent:**
fishing spot sharing app but private with only friends

**Spec:**
```
Type:       Mobile application with backend (private social)
Auth:       Sign in with Google
Data model: Angler(id, name)
            Friendship(a_id -> Angler, b_id -> Angler)
            Spot(id, owner_id -> Angler, lat, lng, name, visibility)
            Catch(id, spot_id -> Spot, angler_id -> Angler, species, weight_kg, photo_url, caught_at)
Features:   - Save fishing spots privately or share them with friends
            - Log catches with species, weight and photo
            - Show friends' recent catches
            - Record weather and moon phase with each catch
API:        REST
            GET  /spots
            POST /spots
            POST /catches
            GET  /feed
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Firebase Auth, Node.js, OpenWeatherMap API
```

---

## Example 144

**Intent:**
Language exchange app. People meet to practice languages, I learn your language you learn mine.

**Spec:**
```
Type:       Mobile application with backend (matching)
Auth:       Email or Google login
Data model: User(id, name, native_languages, learning_languages, level, city)
            Partnership(id, user_a -> User, user_b -> User, status)
            Message(id, partnership_id -> Partnership, sender_id -> User, text, translation, sent_at)
Features:   - Match users whose native and learning languages complement each other
            - Chat with built-in translation help
            - Suggest correcting a partner's message inline
            - Schedule video practice calls
API:        REST + WebSocket
            GET  /matches
            POST /partnerships
            GET  /partnerships/{id}/messages
            WS   /chat
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, DeepL API, Agora
```

---

## Example 145

**Intent:**
neighborhood garage sale map app

**Spec:**
```
Type:       Mobile application with backend (local events)
Auth:       Email login for sellers
Data model: Sale(id, seller_id -> Seller, address, lat, lng, date, start_time, end_time, description, photos)
            Seller(id, email)
Features:   - Post a garage sale with date, time and photos
            - Show this weekend's sales on a map
            - Plan a route through selected sales
            - Save favorite sales
API:        REST
            GET  /sales?weekend={date}
            POST /sales
            GET  /route?ids={ids}
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Express, Mapbox Directions API
```

---

## Example 146

**Intent:**
tour guide app where tourists join a live walking tour and hear the guide through their earbuds

**Spec:**
```
Type:       Mobile application with backend (live audio)
Auth:       Guide email login; tourists join with a tour code
Data model: Guide(id, name, email)
            Tour(id, guide_id -> Guide, title, code, status)
            Listener(id, tour_id -> Tour, device_id, language)
Features:   - Start a live tour broadcast
            - Stream the guide's voice to tourists with low latency
            - Show the guide's position on a map
            - Offer translated subtitles of the guide's speech
API:        REST
            POST /tours
            POST /tours/{code}/join
            GET  /tours/{id}/token
Storage:    PostgreSQL
Tech stack: Flutter, LiveKit (WebRTC), Google Speech-to-Text
```

---

## Example 147

**Intent:**
hi i want to know how to build app for my cousin's tuk tuk business in sri lanka, customers book ride and pay cash

**Spec:**
```
Type:       Mobile application with backend (ride booking)
Auth:       Phone number login with SMS code
Data model: Customer(id, phone, name)
            Driver(id, phone, name, vehicle_no, available, lat, lng)
            Booking(id, customer_id -> Customer, driver_id -> Driver, pickup, dropoff, estimated_fare, status)
Features:   - Book a tuk tuk with pickup on a map
            - Show an estimated fare by distance
            - Assign a nearby available driver
            - Pay the driver in cash and record it
            - Let customers call the driver from the app
API:        REST
            POST /bookings
            PATCH /bookings/{id}
            GET  /drivers/nearby
            POST /drivers/me/location
Storage:    PostgreSQL
Tech stack: Flutter, Firebase (Auth, Firestore)
```

---

## Example 148

**Intent:**
i wanna track my sourdough starter temp w a sensor n see it on my phone

**Spec:**
```
Type:       IoT system (with mobile companion app)
Auth:       Email login
Data model: Device(id, owner_email, name)
            TempReading(device_id -> Device, celsius, humidity, recorded_at)
Features:   - Send temperature and humidity readings every 5 minutes
            - Show a live chart on the phone
            - Alert when the starter gets too cold or too warm
            - Note feeding times on the chart
API:        REST
            POST /devices/{id}/readings
            GET  /devices/{id}/readings?hours=24
            POST /devices/{id}/feedings
Storage:    InfluxDB
Tech stack: ESP32 with DS18B20 sensor, Flutter, Node.js
```

---

## Example 149

**Intent:**
social app for posting hikes with photos and the GPS track

**Spec:**
```
Type:       Mobile application with backend (social, outdoors)
Auth:       Email or Google login
Data model: Hiker(id, name, avatar_url)
            Hike(id, hiker_id -> Hiker, title, track_geojson, distance_km, elevation_m, date)
            HikePhoto(id, hike_id -> Hike, url, lat, lng)
            Like(hike_id -> Hike, hiker_id -> Hiker)
Features:   - Record a GPS track during a hike
            - Attach geotagged photos along the track
            - Post hikes to a feed for followers
            - Like and comment on hikes
API:        REST
            POST /hikes
            POST /hikes/{id}/photos
            GET  /feed
            POST /hikes/{id}/like
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Flutter, Django REST Framework
```

---

## Example 150

**Intent:**
pharmacy delivery app for meds

**Spec:**
```
Type:       Mobile application with backend (delivery)
Auth:       Patient phone login with SMS code
Data model: Patient(id, name, phone, address)
            MedOrder(id, patient_id -> Patient, prescription_id, items, total, status)
            Courier(id, name, phone)
Features:   - Order refills of existing prescriptions
            - Upload new prescription photos for review
            - Pay at checkout
            - Track the courier during delivery
            - Require a signature on delivery
API:        REST
            POST /orders
            GET  /orders/{id}
            POST /prescriptions
            PATCH /orders/{id}
Storage:    PostgreSQL
Tech stack: React Native, NestJS
```

---

## Example 151

**Intent:**
mobile app where a building's residents can see the elevator status and report when it breaks

**Spec:**
```
Type:       Mobile application with backend (building services)
Auth:       Resident login with building code
Data model: Elevator(id, building_id, name, status, updated_at)
            OutageReport(id, elevator_id -> Elevator, reporter, note, created_at)
Features:   - Show each elevator's current status
            - Report an outage with one tap
            - Notify all residents when an elevator goes down or comes back
            - Let the building manager post repair estimates
API:        REST
            GET  /buildings/{id}/elevators
            POST /elevators/{id}/reports
            PATCH /elevators/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Express, Firebase Cloud Messaging
```

---

## Example 152

**Intent:**
football (soccer) pickup game organizer with player ratings

**Spec:**
```
Type:       Mobile application with backend (sports)
Auth:       Sign in with Google
Data model: Player(id, name, rating, preferred_position)
            Game(id, organizer_id -> Player, field, starts_at, max_players, price)
            GamePlayer(game_id -> Game, player_id -> Player, team)
            PeerRating(game_id -> Game, from_id -> Player, to_id -> Player, score)
Features:   - Organize a pickup game with a field and time
            - Join games and pay your share
            - Auto-balance teams by player rating
            - Rate other players after the game
API:        REST
            GET  /games
            POST /games
            POST /games/{id}/join
            POST /games/{id}/balance
            POST /games/{id}/ratings
Storage:    PostgreSQL
Tech stack: React Native, Express, Stripe
```

---

## Example 153

**Intent:**
an app for my daycare: teachers log naps, meals and diapers and parents see it live

**Spec:**
```
Type:       Mobile application with backend (childcare)
Auth:       Staff and parent email login
Data model: Child(id, name, room_id -> Room)
            Room(id, name)
            Teacher(id, name, room_id -> Room)
            Parent(id, name, email)
            ParentChild(parent_id -> Parent, child_id -> Child)
            ActivityLog(id, child_id -> Child, type, details, photo_url, logged_at, teacher_id -> Teacher)
Features:   - Log naps, meals, diaper changes and moods quickly
            - Share photos of the day with parents
            - Show parents a live daily timeline
            - Send a daily summary at pickup time
            - Message teachers
API:        REST
            GET  /rooms/{id}/children
            POST /logs
            GET  /children/{id}/logs?date={date}
            POST /messages
Storage:    PostgreSQL, S3 (photos)
Tech stack: Flutter, Laravel
```

---

## Example 154

**Intent:**
Construction site app — workers clock in with GPS, foremen log incidents and daily progress photos.

**Spec:**
```
Type:       Mobile application with backend (construction field management)
Auth:       Company email login with worker and foreman roles
Data model: Site(id, name, address, lat, lng, radius_m)
            Worker(id, name, role)
            Shift(id, worker_id -> Worker, site_id -> Site, clock_in, clock_out)
            Incident(id, site_id -> Site, reported_by -> Worker, severity, description, photo_url)
            DailyLog(id, site_id -> Site, date, notes, photos)
Features:   - Clock in only when inside the site geofence
            - Report safety incidents with photos
            - Post a daily progress log
            - Show the office total hours per site
API:        REST
            POST /shifts/clock-in
            POST /shifts/clock-out
            POST /incidents
            POST /daily-logs
            GET  /sites/{id}/hours
Storage:    PostgreSQL, S3 (photos)
Tech stack: React Native, ASP.NET Core, Azure Blob Storage
```

---

## Example 155

**Intent:**
I'm thinking about an app for our cat rescue: adopters browse cats, apply online, and fosters update each cat's profile with photos

**Spec:**
```
Type:       Mobile application with backend (animal rescue)
Auth:       Email login with adopter, foster and admin roles
Data model: Cat(id, name, age, sex, temperament, status, foster_id -> Foster)
            CatPhoto(id, cat_id -> Cat, url)
            Foster(id, name, email)
            Application(id, cat_id -> Cat, adopter_name, email, home_details, status)
Features:   - Browse adoptable cats with filters
            - Apply to adopt a cat
            - Let fosters post updates and photos
            - Let admins review and approve applications
API:        REST
            GET  /cats
            POST /cats/{id}/photos
            POST /applications
            PATCH /applications/{id}
Storage:    PostgreSQL, Cloudinary
Tech stack: Flutter, Supabase
```

---

## Example 156

**Intent:**
realtime stock trading game with friends using fake money

**Spec:**
```
Type:       Mobile game (multiplayer simulation)
Auth:       Sign in with Google or Apple
Data model: Player(id, name)
            League(id, name, start_cash, ends_at)
            LeagueMember(league_id -> League, player_id -> Player, cash)
            Holding(member_id, symbol, shares, avg_price)
            Trade(id, member_id, symbol, side, shares, price, executed_at)
Features:   - Create a private league with starting cash
            - Buy and sell stocks at live prices
            - Show each player's portfolio value
            - Rank players by portfolio return
            - End the league on a set date
API:        REST
            POST /leagues
            POST /leagues/{id}/join
            POST /leagues/{id}/trades
            GET  /leagues/{id}/standings
Storage:    PostgreSQL, Redis (price cache)
Tech stack: React Native, NestJS, Finnhub API
```

---

## Example 157

**Intent:**
just a simple app to RSVP to my birthday party

**Spec:**
```
Type:       Mobile application with backend
Data model: Party(id, title, date, location, host_email)
            Rsvp(id, party_id -> Party, name, response, plus_ones)
Features:   - Share an invite link
            - Let guests answer yes, no or maybe
            - Show the host a guest count
            - Send a reminder the day before
API:        REST
            GET  /parties/{id}
            POST /parties/{id}/rsvps
            GET  /parties/{id}/rsvps
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase
```

---

## Example 158

**Intent:**
escape room booking app with team leaderboard of fastest times

**Spec:**
```
Type:       Mobile application with backend (booking)
Auth:       Email login
Data model: Room(id, name, difficulty, duration_min)
            Slot(id, room_id -> Room, starts_at, booked)
            Booking(id, slot_id -> Slot, team_name, players, contact_email)
            Result(booking_id -> Booking, escaped, time_s)
Features:   - Book a slot for a room
            - Pay a deposit
            - Record the team's escape time
            - Show a leaderboard per room
API:        REST
            GET  /rooms/{id}/slots
            POST /bookings
            POST /bookings/{id}/result
            GET  /rooms/{id}/leaderboard
Storage:    PostgreSQL
Tech stack: React Native, Express, Stripe
```

---

## Example 159

**Intent:**
app for my tattoo studio customers to send ideas and book consults

**Spec:**
```
Type:       Mobile application with backend (appointments)
Auth:       Customer email login; artists have staff accounts
Data model: Artist(id, name, styles)
            Customer(id, name, email)
            Idea(id, customer_id -> Customer, artist_id -> Artist, description, reference_images, placement, size_cm)
            Consult(id, idea_id -> Idea, scheduled_at, deposit_paid)
Features:   - Browse artists' portfolios
            - Send a tattoo idea with reference images
            - Let the artist reply with a quote
            - Book a consult and pay a deposit
API:        REST
            GET  /artists
            POST /ideas
            POST /ideas/{id}/quote
            POST /consults
Storage:    PostgreSQL, S3 (images)
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 160

**Intent:**
carpool app for concerts and festivals so fans share rides

**Spec:**
```
Type:       Mobile application with backend (ride sharing)
Auth:       Email or Google login
Data model: Fan(id, name, rating)
            Festival(id, name, location, dates)
            RideOffer(id, festival_id -> Festival, driver_id -> Fan, from_city, departure_at, seats, cost_per_seat)
            SeatBooking(offer_id -> RideOffer, fan_id -> Fan, status)
Features:   - Search rides to a festival from your city
            - Offer seats with a cost share
            - Book a seat and chat with the driver
            - Rate drivers and passengers
API:        REST
            GET  /festivals/{id}/rides?from={city}
            POST /rides
            POST /rides/{id}/bookings
Storage:    PostgreSQL
Tech stack: React Native, Laravel
```

---

## Example 161

**Intent:**
group chat for my D&D party with dice rolls

**Spec:**
```
Type:       Mobile application with backend (real-time chat)
Auth:       Sign in with Discord
Data model: Player(id, discord_id, name)
            Campaign(id, name, dm_id -> Player)
            Character(id, campaign_id -> Campaign, player_id -> Player, name, stats_json)
            ChatMessage(id, campaign_id -> Campaign, player_id -> Player, text, roll_expr, roll_result, sent_at)
Features:   - Chat in a campaign channel
            - Roll dice with commands like /roll 2d6+3
            - Show roll results to everyone in the chat
            - Keep character sheets for each player
            - Let the DM whisper to one player
API:        REST + WebSocket
            GET  /campaigns
            POST /campaigns/{id}/characters
            GET  /campaigns/{id}/messages
            WS   /campaigns/{id}/chat
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Socket.IO
```

---

## Example 162

**Intent:**
helmet app for motorcyclists to share location with group on rides

**Spec:**
```
Type:       Mobile application with backend (group location)
Auth:       Phone login with SMS code
Data model: Rider(id, name, bike)
            GroupRide(id, leader_id -> Rider, name, route_gpx, starts_at)
            GroupMember(ride_id -> GroupRide, rider_id -> Rider)
            Position(rider_id -> Rider, ride_id -> GroupRide, lat, lng, speed, at)
Features:   - Create a group ride with a planned route
            - Show every rider's position on the map
            - Alert the group when someone stops unexpectedly
            - Detect a crash from sudden deceleration and notify the group
API:        REST + WebSocket
            POST /rides
            POST /rides/{id}/join
            WS   /rides/{id}/positions
Storage:    Redis, PostgreSQL
Tech stack: Flutter, Elixir, Phoenix Channels
```

---

## Example 163

**Intent:**
app for referees, assign them to matches

**Spec:**
```
Type:       Mobile application with backend (scheduling)
Auth:       Email login; assignor has admin role
Data model: Referee(id, name, email, grade, home_lat, home_lng)
            Match(id, competition, venue, kickoff, level_required)
            Assignment(id, match_id -> Match, referee_id -> Referee, role, status)
            Unavailability(referee_id -> Referee, date)
Features:   - Let referees mark days they are unavailable
            - Assign referees to matches by grade and distance
            - Let referees accept or decline assignments
            - Track match fees owed to each referee
API:        REST
            GET  /matches
            POST /assignments
            PATCH /assignments/{id}
            POST /unavailability
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework
```

---

## Example 164

**Intent:**
an app to find someone to split an uber with after a concert

**Spec:**
```
Type:       Mobile application with backend (ride splitting)
Auth:       Phone login with SMS code
Data model: User(id, name, phone, rating)
            RideShareRequest(id, user_id -> User, origin_lat, origin_lng, destination_lat, destination_lng, leave_at, status)
            Group(id, request_ids, chat_room_id)
Features:   - Post where you are going and when
            - Match riders with destinations close to each other
            - Group matched riders into a chat
            - Split the fare evenly and send payment requests
API:        REST
            POST /requests
            GET  /requests/{id}/matches
            POST /groups
            POST /groups/{id}/split
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Go
```

---

## Example 165

**Intent:**
My grandma's church choir has 40 members and the director wants to send them practice recordings for their part (soprano, alto, tenor, bass) and know who listened. They all have smartphones but are not techy at all.

**Spec:**
```
Type:       Mobile application with backend (group communication)
Auth:       Phone number login with SMS code, members added by the director
Data model: Member(id, name, phone, voice_part)
            Recording(id, title, voice_part, audio_url, uploaded_at)
            Listen(recording_id -> Recording, member_id -> Member, listened_at, completed)
Features:   - Upload practice recordings tagged by voice part
            - Show each member only the recordings for their part
            - Play recordings with large, simple controls
            - Track who listened to each recording
            - Send a push reminder before rehearsal
API:        REST
            GET  /recordings
            POST /recordings
            POST /recordings/{id}/listens
            GET  /recordings/{id}/listens
Storage:    PostgreSQL, S3 (audio)
Tech stack: Flutter, Node.js
```

---

## Example 166

**Intent:**
app to rent kayaks from unattended lockers with a code

**Spec:**
```
Type:       Mobile application with backend (IoT rentals)
Auth:       Email login with card on file
Data model: Locker(id, location_name, lat, lng, kayak_count)
            Kayak(id, locker_id -> Locker, status)
            Rental(id, kayak_id -> Kayak, user_id -> User, unlock_code, started_at, returned_at, cost)
            User(id, email)
Features:   - Show lockers with available kayaks
            - Reserve and pay for a time block
            - Send a one-time unlock code to the locker
            - Detect the return via the locker sensor
            - Charge extra for late returns
API:        REST
            GET  /lockers
            POST /rentals
            POST /lockers/{id}/events
            POST /rentals/{id}/return
Storage:    PostgreSQL
Tech stack: React Native, Node.js, AWS IoT Core, Stripe
```

---

## Example 167

**Intent:**
i want build an app where teachers from different schools in my country share lesson plans, they can like and download, i am from Indonesia

**Spec:**
```
Type:       Mobile application with backend (content sharing)
Auth:       Email login with teacher verification
Data model: Teacher(id, name, school, subject, verified)
            LessonPlan(id, author_id -> Teacher, title, subject, grade, file_url, language)
            Like(plan_id -> LessonPlan, teacher_id -> Teacher)
            Download(plan_id -> LessonPlan, teacher_id -> Teacher, at)
Features:   - Upload lesson plans as PDF or Word
            - Search by subject, grade and keyword
            - Like and download plans
            - Show the most popular plans each week
API:        REST
            GET  /plans?subject={s}&grade={g}
            POST /plans
            POST /plans/{id}/like
            GET  /plans/{id}/download
Storage:    PostgreSQL, Google Cloud Storage
Tech stack: Flutter, Laravel
```

---

## Example 168

**Intent:**
ride along app for driving instructors, students book lessons and see their progress

**Spec:**
```
Type:       Mobile application with backend (lesson booking)
Auth:       Email login with instructor and student roles
Data model: Instructor(id, name, car, area)
            Student(id, name, permit_no, instructor_id -> Instructor)
            Lesson(id, student_id -> Student, instructor_id -> Instructor, starts_at, pickup_address, status)
            SkillScore(student_id -> Student, skill, score, updated_at)
Features:   - Book lessons in the instructor's open slots
            - Set a pickup address
            - Let the instructor score skills like parking and merging after each lesson
            - Show progress toward test readiness
API:        REST
            GET  /instructors/{id}/slots
            POST /lessons
            POST /lessons/{id}/scores
            GET  /students/{id}/progress
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 169

**Intent:**
chess app to play friends online with clocks

**Spec:**
```
Type:       Mobile game (online multiplayer)
Auth:       Email or Google login
Data model: Player(id, username, rating)
            Game(id, white_id -> Player, black_id -> Player, time_control, pgn, status, result)
            Challenge(id, from_id -> Player, to_id -> Player, time_control, status)
Features:   - Challenge a friend with a chosen time control
            - Validate moves on the server
            - Run synced chess clocks
            - Detect checkmate, stalemate and timeouts
            - Update ratings after rated games
API:        REST + WebSocket
            POST /challenges
            POST /challenges/{id}/accept
            GET  /games/{id}
            WS   /games/{id}
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Node.js, chess.js
```

---

## Example 170

**Intent:**
thrift store app where stores post new arrivals

**Spec:**
```
Type:       Mobile application with backend (retail)
Auth:       Shopper email login; store staff accounts
Data model: Store(id, name, address)
            Arrival(id, store_id -> Store, title, category, price, photo_url, posted_at, sold)
            Follow(shopper_id -> Shopper, store_id -> Store)
            Shopper(id, email)
Features:   - Let store staff post new arrivals with photos
            - Follow favorite stores
            - Show a feed of new arrivals from followed stores
            - Hold an item for 24 hours
API:        REST
            GET  /feed
            POST /stores/{id}/arrivals
            POST /arrivals/{id}/hold
            POST /stores/{id}/follow
Storage:    PostgreSQL, S3 (photos)
Tech stack: React Native, NestJS
```

---

## Example 171

**Intent:**
home care nurses visit app

**Spec:**
```
Type:       Mobile application with backend (healthcare field visits)
Auth:       Nurse login with email, password and biometric unlock
Data model: Nurse(id, name, license_no)
            Patient(id, name, address, care_plan)
            Visit(id, nurse_id -> Nurse, patient_id -> Patient, scheduled_at, arrived_at, left_at, notes)
            Vitals(visit_id -> Visit, blood_pressure, pulse, temperature)
Features:   - Show the day's patient visits in route order
            - Record arrival and departure times
            - Enter vital signs and visit notes
            - Work offline and sync later
            - Flag abnormal vitals to the supervisor
API:        REST
            GET  /nurses/me/visits
            PATCH /visits/{id}
            POST /visits/{id}/vitals
Storage:    PostgreSQL (encrypted), SQLite on device
Tech stack: Kotlin (Android), Spring Boot
```

---

## Example 172

**Intent:**
create app for my friends and me to bet on stupid stuff with points not money

**Spec:**
```
Type:       Mobile application with backend (social game)
Auth:       Sign in with Google
Data model: Friend(id, name, points)
            Group(id, name)
            Bet(id, group_id -> Group, question, options, closes_at, resolved_option)
            Wager(bet_id -> Bet, friend_id -> Friend, option, points)
Features:   - Create a bet with options and a closing time
            - Wager points on an option
            - Resolve the bet and pay out points
            - Show a group points leaderboard
API:        REST
            POST /groups/{id}/bets
            POST /bets/{id}/wagers
            POST /bets/{id}/resolve
            GET  /groups/{id}/leaderboard
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase
```

---

## Example 173

**Intent:**
Build me a react native app with a django backend for a community garden: plots, watering schedule, and shared tool checkout.

**Spec:**
```
Type:       Mobile application with backend (community garden)
Auth:       Email login with gardener and coordinator roles
Data model: Gardener(id, name, email)
            Plot(id, number, gardener_id -> Gardener)
            WateringShift(id, date, gardener_id -> Gardener)
            Tool(id, name, checked_out_by -> Gardener, checked_out_at)
Features:   - Assign plots to gardeners
            - Sign up for watering days
            - Check tools out and back in
            - Notify the gardener on their watering day
API:        REST
            GET  /plots
            GET  /watering?month={m}
            POST /watering
            POST /tools/{id}/checkout
            POST /tools/{id}/return
Storage:    PostgreSQL
Tech stack: React Native, Django REST Framework
```

---

## Example 174

**Intent:**
clinic waiting room app, patients check in and get notified when doctor is ready

**Spec:**
```
Type:       Mobile application with backend (patient queue)
Auth:       Patient check-in with date of birth and appointment code
Data model: Appointment(id, patient_name, dob, doctor_id -> Doctor, scheduled_at, code, status)
            Doctor(id, name, room)
Features:   - Check in on arrival from the phone
            - Show the patient's place in line
            - Let reception mark a doctor as ready
            - Notify the patient to go to the room
            - Let patients wait in the car instead of the lobby
API:        REST + WebSocket
            POST /checkin
            GET  /appointments/{id}/status
            PATCH /appointments/{id}
            WS   /appointments/{id}
Storage:    PostgreSQL
Tech stack: Flutter, ASP.NET Core, SignalR
```

---

## Example 175

**Intent:**
sticker trading app for world cup album

**Spec:**
```
Type:       Mobile application with backend (trading)
Auth:       Email or Google login
Data model: Collector(id, name, city)
            Sticker(id, number, team, player)
            CollectorSticker(collector_id -> Collector, sticker_id -> Sticker, count)
            TradeOffer(id, from_id -> Collector, to_id -> Collector, give_ids, get_ids, status)
Features:   - Mark which stickers you have and how many duplicates
            - Find collectors nearby with the stickers you need
            - Propose a trade of duplicates
            - Show album completion percentage
API:        REST
            PUT  /me/stickers
            GET  /matches
            POST /trades
            PATCH /trades/{id}
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 176

**Intent:**
news app for our small town with comments

**Spec:**
```
Type:       Mobile application with backend (local news)
Auth:       Reader email login to comment; editor accounts
Data model: Article(id, title, body, image_url, category, published_at, author_id -> Editor)
            Editor(id, name)
            Reader(id, name, email)
            Comment(id, article_id -> Article, reader_id -> Reader, text, created_at, hidden)
Features:   - Publish local news articles by category
            - Send push alerts for breaking news
            - Let readers comment on articles
            - Let editors moderate comments
API:        REST
            GET  /articles
            POST /articles
            GET  /articles/{id}/comments
            POST /articles/{id}/comments
Storage:    PostgreSQL
Tech stack: Flutter, Strapi (headless CMS)
```

---

## Example 177

**Intent:**
I run a small IT company. I'd like my technicians to get support tickets on their phone, chat with customers, and log time spent per ticket.

**Spec:**
```
Type:       Mobile application with backend (field technicians)
Auth:       Technician email login with SSO; customers log in on a web portal
Data model: Technician(id, name, email)
            Customer(id, company, contact_email)
            Ticket(id, customer_id -> Customer, technician_id -> Technician, subject, priority, status)
            TimeEntry(id, ticket_id -> Ticket, minutes, note)
            TicketMessage(id, ticket_id -> Ticket, author, body, sent_at)
Features:   - Show assigned tickets by priority
            - Chat with the customer on a ticket
            - Start and stop a timer per ticket
            - Close tickets with a resolution note
            - Export time entries for billing
API:        REST
            GET  /tickets?assigned=me
            POST /tickets/{id}/messages
            POST /tickets/{id}/time
            PATCH /tickets/{id}
Storage:    PostgreSQL
Tech stack: React Native, NestJS
```

---

## Example 178

**Intent:**
real time multiplayer drawing guessing game

**Spec:**
```
Type:       Mobile game (real-time multiplayer)
Auth:       Guest nicknames
Data model: Room(id, code, round, drawer_id)
            Player(id, room_id -> Room, nickname, score)
            Word(id, text, difficulty)
Features:   - Take turns drawing a secret word
            - Stream strokes to other players live
            - Let others type guesses
            - Award points for fast correct guesses
API:        WebSocket
            WS   /rooms/{code}
Storage:    Redis
Tech stack: Flutter (CustomPainter), Node.js, Socket.IO
```

---

## Example 179

**Intent:**
meal train app so friends can bring food to someone who just had a baby

**Spec:**
```
Type:       Mobile application with backend (community care)
Auth:       Organizer email login; helpers sign up with name and email
Data model: MealTrain(id, recipient_name, address, dietary_notes, organizer_email)
            MealSlot(id, train_id -> MealTrain, date, helper_name, helper_email, dish)
Features:   - Create a meal train with dates and dietary notes
            - Share a link with friends
            - Let helpers claim a date and say what they bring
            - Remind helpers the day before
API:        REST
            POST /trains
            GET  /trains/{id}
            POST /slots/{id}/claim
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 180

**Intent:**
smart door lock app, give guests temporary access codes

**Spec:**
```
Type:       IoT system (with mobile companion app)
Auth:       Owner email login with two-factor authentication
Data model: Owner(id, email)
            Lock(id, owner_id -> Owner, name, serial, battery_pct, is_locked)
            AccessCode(id, lock_id -> Lock, code_hash, guest_name, valid_from, valid_until)
            AccessEvent(id, lock_id -> Lock, code_id -> AccessCode, method, at)
Features:   - Lock and unlock the door remotely
            - Create time-limited codes for guests
            - Show an access log
            - Alert when the battery is low
API:        REST
            GET  /locks
            POST /locks/{id}/command
            POST /locks/{id}/codes
            GET  /locks/{id}/events
Storage:    PostgreSQL
Tech stack: Swift (iOS), Kotlin (Android), AWS IoT Core, Node.js
```

---

## Example 181

**Intent:**
alumni network app for our university

**Spec:**
```
Type:       Mobile application with backend (professional network)
Auth:       LinkedIn login and alumni verification by graduation year
Data model: Alumnus(id, name, grad_year, degree, company, city)
            Post(id, author_id -> Alumnus, body, created_at)
            Event(id, title, city, date)
            MentorRequest(id, from_id -> Alumnus, to_id -> Alumnus, status)
Features:   - Search alumni by company, city and year
            - Post job openings and news
            - Join local alumni events
            - Ask an alumnus to be a mentor
API:        REST
            GET  /alumni
            GET  /posts
            POST /posts
            GET  /events
            POST /mentor-requests
Storage:    PostgreSQL
Tech stack: Flutter, Spring Boot
```

---

## Example 182

**Intent:**
ugh our hoa uses email for everything. need an app with dues payments, pool booking, and complaints

**Spec:**
```
Type:       Mobile application with backend (HOA management)
Auth:       Homeowner email login; board members as admins
Data model: Homeowner(id, name, email, lot_number)
            Due(id, homeowner_id -> Homeowner, period, amount, paid_at)
            PoolSlot(id, starts_at, capacity)
            PoolBooking(slot_id -> PoolSlot, homeowner_id -> Homeowner, guests)
            Complaint(id, homeowner_id -> Homeowner, category, description, status)
Features:   - Pay quarterly dues online
            - Book pool time slots with a guest count
            - Submit complaints and track status
            - Post board announcements
API:        REST
            GET  /dues
            POST /dues/{id}/pay
            POST /pool/bookings
            POST /complaints
Storage:    PostgreSQL
Tech stack: React Native, Express, Stripe
```

---

## Example 183

**Intent:**
Ludo game online with friends

**Spec:**
```
Type:       Mobile game (online multiplayer)
Auth:       Guest play or Facebook login
Data model: Player(id, name, coins)
            Table(id, code, player_count, status)
            Seat(table_id -> Table, player_id -> Player, color)
            GameState(table_id -> Table, pieces_json, turn, last_roll)
Features:   - Create a private table and invite friends
            - Roll dice and move pieces on the server
            - Sync moves between 2-4 players
            - Reconnect after dropping out
API:        REST + WebSocket
            POST /tables
            POST /tables/{code}/join
            WS   /tables/{code}
Storage:    Redis
Tech stack: Unity (C#), Photon PUN
```

---

## Example 184

**Intent:**
app where farmers rent tractors to each other

**Spec:**
```
Type:       Mobile application with backend (equipment rental)
Auth:       Phone login with SMS code
Data model: Farmer(id, name, phone, village)
            Equipment(id, owner_id -> Farmer, type, model, daily_rate, with_operator)
            RentalRequest(id, equipment_id -> Equipment, farmer_id -> Farmer, start_date, days, status)
Features:   - List equipment with a daily rate
            - Search equipment nearby by type
            - Request a rental for given days
            - Confirm and pay a deposit
API:        REST
            GET  /equipment?type={t}
            POST /equipment
            POST /rentals
            PATCH /rentals/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework
```

---

## Example 185

**Intent:**
i need app that tell my staff in restaurant which table need what, waiters take order on phone and kitchen see it

**Spec:**
```
Type:       Mobile application with backend (restaurant POS)
Auth:       Staff PIN login per shift
Data model: Staff(id, name, role, pin_hash)
            Table(id, number, status)
            Ticket(id, table_id -> Table, waiter_id -> Staff, status, opened_at)
            TicketItem(id, ticket_id -> Ticket, menu_item_id -> MenuItem, notes, status)
            MenuItem(id, name, price, station)
Features:   - Take orders by table on the waiter's phone
            - Send items to the kitchen screen by station
            - Mark dishes ready and notify the waiter
            - Show table status on a floor plan
            - Close the bill
API:        REST + WebSocket
            POST /tickets
            POST /tickets/{id}/items
            PATCH /items/{id}
            WS   /kitchen
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Socket.IO
```

---

## Example 186

**Intent:**
dating app with voice notes instead of photos

**Spec:**
```
Type:       Mobile application with backend (dating)
Auth:       Phone login with SMS code
Data model: User(id, name, age, city, prompt_answers)
            VoiceIntro(id, user_id -> User, audio_url, duration_s)
            Like(from_id -> User, to_id -> User)
            Match(id, a_id -> User, b_id -> User)
            VoiceMessage(id, match_id -> Match, sender_id -> User, audio_url)
Features:   - Record a 30-second voice intro
            - Listen to profiles and like or skip
            - Reveal photos only after a match
            - Send voice messages to matches
API:        REST
            POST /intros
            GET  /profiles
            POST /likes
            POST /matches/{id}/voice
Storage:    PostgreSQL, S3 (audio)
Tech stack: SwiftUI, Kotlin (Jetpack Compose), Go
```

---

## Example 187

**Intent:**
vending machine stock app for route drivers

**Spec:**
```
Type:       Mobile application with backend (route operations)
Auth:       Driver login with email
Data model: Machine(id, location, lat, lng)
            Slot(id, machine_id -> Machine, product_id -> Product, capacity, current)
            Product(id, name, price)
            Visit(id, machine_id -> Machine, driver_id, restocked_json, cash_collected, at)
Features:   - Show machines on today's route with low stock
            - Record restocked quantities per slot
            - Log cash collected
            - Generate a picking list for the warehouse
API:        REST
            GET  /routes/today
            POST /machines/{id}/visits
            GET  /picklist?date={date}
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 188

**Intent:**
twitch-like app for streaming my cooking live

**Spec:**
```
Type:       Mobile application with backend (live streaming)
Auth:       Email or Google login
Data model: Streamer(id, name, stream_key)
            Stream(id, streamer_id -> Streamer, title, status, started_at, viewer_count)
            ChatMessage(id, stream_id -> Stream, user_id, text, at)
            Follow(user_id, streamer_id -> Streamer)
Features:   - Go live from the phone camera
            - Watch streams with low latency
            - Chat during the stream
            - Notify followers when a stream starts
            - Save the stream as a replay
API:        REST + WebSocket
            POST /streams
            GET  /streams/live
            WS   /streams/{id}/chat
Storage:    PostgreSQL, S3 (replays)
Tech stack: Flutter, Mux Live Streaming, Node.js
```

---

## Example 189

**Intent:**
help us make app that ambulance staff in our hospital can see which ER has free beds

**Spec:**
```
Type:       Mobile application with backend (healthcare coordination)
Auth:       Staff login with hospital SSO
Data model: Hospital(id, name, lat, lng)
            Department(id, hospital_id -> Hospital, type, free_beds, updated_at)
            Arrival(id, hospital_id -> Hospital, eta, severity, crew_id)
Features:   - Show emergency departments with free beds on a map
            - Let charge nurses update bed counts
            - Send a pre-arrival notice with ETA and severity
            - Show travel time from the ambulance position
API:        REST + WebSocket
            GET  /hospitals
            PATCH /departments/{id}
            POST /arrivals
            WS   /beds
Storage:    PostgreSQL
Tech stack: Kotlin (Android), Spring Boot, WebSocket (STOMP)
```

---

## Example 190

**Intent:**
secret santa but for book swaps by mail across the country

**Spec:**
```
Type:       Mobile application with backend (gift exchange)
Auth:       Email login
Data model: Member(id, name, address, favorite_genres)
            Round(id, name, signup_deadline, ship_by)
            Entry(round_id -> Round, member_id -> Member)
            Pairing(round_id -> Round, sender_id -> Member, receiver_id -> Member, tracking_no, received)
Features:   - Sign up for a swap round with genre preferences
            - Pair members randomly across the country
            - Show the sender the receiver's address and genres
            - Enter a tracking number and confirm receipt
API:        REST
            POST /rounds/{id}/entries
            POST /rounds/{id}/pair
            GET  /rounds/{id}/my-pairing
            PATCH /pairings/{id}
Storage:    PostgreSQL
Tech stack: Flutter, FastAPI
```

---

## Example 191

**Intent:**
Moving out soon and want an app to hand off my furniture to people for free, first come first serve.

**Spec:**
```
Type:       Mobile application with backend (free giveaway)
Auth:       Email login
Data model: Giver(id, email)
            Item(id, giver_id -> Giver, title, photo_url, pickup_area, status)
            Claim(id, item_id -> Item, claimer_email, pickup_time, created_at)
Features:   - Post items with a photo and pickup area
            - Let the first person claim an item
            - Propose a pickup time
            - Mark items as picked up
API:        REST
            GET  /items
            POST /items
            POST /items/{id}/claim
            PATCH /items/{id}
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 192

**Intent:**
app where diabetics share glucose readings with their doctor

**Spec:**
```
Type:       Mobile application with backend (health monitoring)
Auth:       Patient and doctor email login with two-factor authentication
Data model: Patient(id, name, doctor_id -> Doctor)
            Doctor(id, name, clinic)
            GlucoseReading(id, patient_id -> Patient, mg_dl, context, measured_at)
            DoctorNote(id, patient_id -> Patient, doctor_id -> Doctor, text, at)
Features:   - Log glucose readings manually or from a Bluetooth meter
            - Show trends and time in range
            - Share readings with the patient's doctor
            - Alert the doctor about repeated lows
            - Let the doctor send notes
API:        REST
            POST /readings
            GET  /patients/{id}/readings
            POST /patients/{id}/notes
Storage:    PostgreSQL (encrypted at rest)
Tech stack: Flutter (flutter_blue_plus), FastAPI
```

---

## Example 193

**Intent:**
i make a food delivery app for students in my campus, order from canteen deliver to dorm by other students, they earn a bit

**Spec:**
```
Type:       Mobile application with backend (peer delivery)
Auth:       University email login
Data model: Student(id, name, email, dorm, is_courier)
            Canteen(id, name)
            FoodOrder(id, buyer_id -> Student, courier_id -> Student, canteen_id -> Canteen, items, tip, status)
Features:   - Post an order with what to buy and a tip
            - Let student couriers accept orders
            - Chat between buyer and courier
            - Mark delivered to the dorm
            - Rate couriers
API:        REST
            POST /orders
            GET  /orders/open
            POST /orders/{id}/accept
            PATCH /orders/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 194

**Intent:**
friend birthday reminder app that syncs between my friends

**Spec:**
```
Type:       Mobile application with backend
Auth:       Sign in with Google
Data model: User(id, name, birthday)
            Friendship(a_id -> User, b_id -> User)
            GiftIdea(id, owner_id -> User, friend_id -> User, text)
Features:   - Share your birthday with friends
            - Show upcoming birthdays of friends
            - Send a reminder 3 days and on the day
            - Keep private gift ideas per friend
API:        REST
            GET  /birthdays/upcoming
            POST /friends
            POST /gift-ideas
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase
```

---

## Example 195

**Intent:**
app for flight attendants to swap shifts

**Spec:**
```
Type:       Mobile application with backend (shift trading)
Auth:       Airline employee SSO
Data model: Crew(id, employee_no, name, base, qualification)
            Pairing(id, flight_numbers, start_at, end_at, base)
            Assignment(pairing_id -> Pairing, crew_id -> Crew)
            SwapRequest(id, offered_pairing -> Pairing, from_crew -> Crew, to_crew -> Crew, status)
Features:   - List your assigned trips
            - Post a trip you want to give away or swap
            - Check legality rules like rest time before a swap
            - Require scheduler approval
API:        REST
            GET  /me/assignments
            POST /swaps
            POST /swaps/{id}/accept
            POST /swaps/{id}/approve
Storage:    PostgreSQL
Tech stack: Kotlin Multiplatform, Spring Boot
```

---

## Example 196

**Intent:**
kayak club live trip tracker so the people on shore can see us

**Spec:**
```
Type:       Mobile application with backend (location sharing)
Auth:       Club member email login
Data model: Paddler(id, name)
            Trip(id, name, started_at, planned_end)
            TripPaddler(trip_id -> Trip, paddler_id -> Paddler)
            Fix(paddler_id -> Paddler, trip_id -> Trip, lat, lng, at)
Features:   - Start a trip and share a public tracking link
            - Upload positions every minute
            - Show paddlers on a map for the shore crew
            - Alert the shore crew if the trip runs past the planned end
API:        REST
            POST /trips
            POST /trips/{id}/fixes
            GET  /trips/{id}/public
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Supabase
```

---

## Example 197

**Intent:**
app for collecting signatures for local petitions

**Spec:**
```
Type:       Mobile application with backend (civic)
Auth:       Email login with verified phone
Data model: Petition(id, creator_id -> Citizen, title, description, goal, deadline)
            Citizen(id, name, email, phone_verified, postcode)
            Signature(petition_id -> Petition, citizen_id -> Citizen, signed_at)
Features:   - Create a petition with a signature goal
            - Sign once per verified person
            - Show progress toward the goal
            - Export signatures as a PDF for the council
API:        REST
            GET  /petitions
            POST /petitions
            POST /petitions/{id}/sign
            GET  /petitions/{id}/export
Storage:    PostgreSQL
Tech stack: React Native, Express, PDFKit
```

---

## Example 198

**Intent:**
shazam for birds but people share recordings and experts confirm the species

**Spec:**
```
Type:       Mobile application with backend (citizen science)
Auth:       Email or Google login with expert role
Data model: User(id, name, is_expert)
            Recording(id, user_id -> User, audio_url, lat, lng, recorded_at, predicted_species, confirmed_species)
            Verification(recording_id -> Recording, expert_id -> User, species, at)
Features:   - Record bird song and upload it
            - Suggest a species with a sound classifier
            - Let experts confirm or correct the species
            - Show a map of confirmed sightings
API:        REST
            POST /recordings
            GET  /recordings?unverified=true
            POST /recordings/{id}/verify
            GET  /sightings
Storage:    PostgreSQL with PostGIS, S3 (audio)
Tech stack: Flutter, FastAPI, BirdNET model
```

---

## Example 199

**Intent:**
need an app where my students upload videos of their piano practice and i give feedback

**Spec:**
```
Type:       Mobile application with backend (music lessons)
Auth:       Teacher and student email login
Data model: Teacher(id, name)
            Student(id, name, teacher_id -> Teacher)
            PracticeVideo(id, student_id -> Student, piece, video_url, uploaded_at)
            Feedback(id, video_id -> PracticeVideo, timestamp_s, comment)
Features:   - Upload practice videos from the phone
            - Leave comments at specific timestamps
            - Track practice streaks per student
            - Notify students when feedback arrives
API:        REST
            POST /videos
            GET  /students/{id}/videos
            POST /videos/{id}/feedback
Storage:    PostgreSQL, S3 (video)
Tech stack: React Native, NestJS, AWS MediaConvert
```

---

## Example 200

**Intent:**
nightclub guest list app

**Spec:**
```
Type:       Mobile application with backend (venue)
Auth:       Promoter email login; door staff accounts
Data model: Promoter(id, name)
            Night(id, date, theme, capacity)
            GuestEntry(id, night_id -> Night, promoter_id -> Promoter, guest_name, plus_count, checked_in)
Features:   - Let promoters add names to a night's guest list
            - Cap the list at venue capacity
            - Search and check in names at the door
            - Show promoters how many of their guests arrived
API:        REST
            POST /nights/{id}/guests
            GET  /nights/{id}/guests?q={name}
            POST /guests/{id}/checkin
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 201

**Intent:**
Water quality sensor network for our lake, with an app so volunteers see readings and add manual tests.

**Spec:**
```
Type:       IoT system (environmental monitoring)
Auth:       Volunteer email login
Data model: Buoy(id, name, lat, lng)
            SensorReading(buoy_id -> Buoy, ph, temperature, turbidity, dissolved_oxygen, at)
            ManualTest(id, volunteer_id -> Volunteer, lat, lng, ph, nitrate, photo_url, at)
            Volunteer(id, name)
Features:   - Collect readings from buoys over LoRaWAN
            - Show readings per buoy on a map and chart
            - Let volunteers add manual test results
            - Alert when values cross safe limits
API:        REST
            GET  /buoys
            GET  /buoys/{id}/readings
            POST /manual-tests
            POST /ingest/lorawan
Storage:    TimescaleDB
Tech stack: The Things Network (LoRaWAN), Python, FastAPI, Flutter
```

---

## Example 202

**Intent:**
ride sharing for wheelchair users, accessible vans

**Spec:**
```
Type:       Mobile application with backend (accessible transport)
Auth:       Phone or email login
Data model: Rider(id, name, phone, mobility_needs)
            Van(id, plate, ramp, wheelchair_spaces, lat, lng)
            Driver(id, name, van_id -> Van)
            Trip(id, rider_id -> Rider, driver_id -> Driver, pickup, dropoff, scheduled_at, companion, status)
Features:   - Book an accessible van now or in advance
            - Record mobility needs like ramp or lift
            - Show the van's live position
            - Work fully with screen readers
            - Let a caregiver book on behalf of the rider
API:        REST
            POST /trips
            GET  /trips/{id}
            PATCH /trips/{id}
            POST /drivers/me/location
Storage:    PostgreSQL
Tech stack: React Native (accessibility APIs), NestJS
```

---

## Example 203

**Intent:**
pickleball

**Spec:**
```
Type:       Mobile application with backend (sports)
Auth:       Email or Google login
Data model: Player(id, name, dupr_rating)
            Court(id, name, lat, lng, courts_count)
            OpenPlay(id, court_id -> Court, starts_at, level, max_players)
            OpenPlayPlayer(open_play_id -> OpenPlay, player_id -> Player)
Features:   - Find pickleball courts nearby
            - Join open play sessions by level
            - Post your own session
            - Rotate players for games on the court
API:        REST
            GET  /courts
            GET  /open-plays
            POST /open-plays
            POST /open-plays/{id}/join
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 204

**Intent:**
app for my coworking space, members book desks and meeting rooms and see who's in today

**Spec:**
```
Type:       Mobile application with backend (workspace booking)
Auth:       Member email login
Data model: Member(id, name, email, company, plan)
            Desk(id, label, zone)
            Room(id, name, capacity)
            Booking(id, member_id -> Member, resource_type, resource_id, starts_at, ends_at)
Features:   - Book a desk for a day
            - Book meeting rooms by the hour within plan credits
            - Show who is in today
            - Open the door with a phone key
API:        REST
            GET  /desks?date={date}
            GET  /rooms/{id}/availability
            POST /bookings
            GET  /presence/today
Storage:    PostgreSQL
Tech stack: Flutter, NestJS, Kisi API (door access)
```

---

## Example 205

**Intent:**
airbnb for camping spots on private land

**Spec:**
```
Type:       Mobile application with backend (marketplace)
Auth:       Email login for hosts and campers
Data model: Host(id, name, email, payout_account)
            Campsite(id, host_id -> Host, title, lat, lng, max_tents, amenities, nightly_price)
            Stay(id, campsite_id -> Campsite, camper_id -> Camper, check_in, nights, status)
            Camper(id, name, email)
Features:   - List land as a campsite with amenities
            - Search campsites on a map by date
            - Book and pay per night
            - Share directions and gate codes after booking
            - Review hosts and campers
API:        REST
            GET  /campsites?bbox={bbox}&date={d}
            POST /campsites
            POST /stays
            POST /stays/{id}/review
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Django REST Framework, Stripe Connect
```

---

## Example 206

**Intent:**
dog park check-in app

**Spec:**
```
Type:       Mobile application with backend (location-based social)
Auth:       Sign in with Google or Apple
Data model: Owner(id, name)
            Dog(id, owner_id -> Owner, name, size, photo_url)
            Park(id, name, lat, lng)
            CheckIn(id, park_id -> Park, dog_id -> Dog, at, left_at)
Features:   - Check in your dog when arriving at a park
            - See which dogs are at the park right now
            - Get notified when a dog friend checks in
            - Auto check out after 2 hours
API:        REST
            GET  /parks/{id}/present
            POST /parks/{id}/checkins
            POST /checkins/{id}/leave
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 207

**Intent:**
meetup app for expats in a new city

**Spec:**
```
Type:       Mobile application with backend (community events)
Auth:       Email or Google login
Data model: Member(id, name, home_country, city, languages)
            Event(id, host_id -> Member, title, city, venue, starts_at, capacity)
            Attendance(event_id -> Event, member_id -> Member)
            Group(id, city, home_country, name)
Features:   - Join groups by city and home country
            - Create and RSVP to events
            - Chat in a group
            - Show a city guide written by members
API:        REST
            GET  /groups?city={city}
            POST /events
            POST /events/{id}/attend
            GET  /groups/{id}/messages
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 208

**Intent:**
snapchat clone

**Spec:**
```
Type:       Mobile application with backend (ephemeral messaging)
Auth:       Phone login with SMS code
Data model: User(id, username, phone)
            Friendship(a_id -> User, b_id -> User, status)
            Snap(id, sender_id -> User, recipient_id -> User, media_url, duration_s, viewed_at)
            Story(id, user_id -> User, media_url, expires_at)
Features:   - Take a photo or short video and send it to friends
            - Delete snaps after they are viewed
            - Post stories that expire after 24 hours
            - Notify the sender when a screenshot is taken
API:        REST
            POST /snaps
            GET  /snaps/inbox
            POST /snaps/{id}/viewed
            POST /stories
            GET  /stories/friends
Storage:    PostgreSQL, S3 with lifecycle expiry
Tech stack: React Native, Go
```

---

## Example 209

**Intent:**
ride app for teens where parents approve every ride

**Spec:**
```
Type:       Mobile application with backend (supervised ride booking)
Auth:       Parent email login; teen accounts linked under the parent
Data model: Parent(id, email, payment_method_id)
            Teen(id, parent_id -> Parent, name, phone)
            Driver(id, name, background_checked, lat, lng)
            Ride(id, teen_id -> Teen, driver_id -> Driver, pickup, dropoff, status, approved_at)
Features:   - Let teens request a ride
            - Ask the parent to approve each ride
            - Use only background-checked drivers
            - Share the live ride with the parent
            - Send a text when the teen arrives
API:        REST + WebSocket
            POST /rides
            POST /rides/{id}/approve
            WS   /rides/{id}/track
Storage:    PostgreSQL
Tech stack: React Native, NestJS, Twilio
```

---

## Example 210

**Intent:**
chat with ai matchmaker that sets you up on dates

**Spec:**
```
Type:       Mobile application with backend (AI matchmaking)
Auth:       Phone login with SMS code
Data model: Member(id, name, age, city, preferences_json)
            MatchmakerChat(id, member_id -> Member, role, text, at)
            Introduction(id, member_a -> Member, member_b -> Member, reason, status)
Features:   - Chat with an AI matchmaker that learns your preferences
            - Propose one introduction per week with a reason
            - Let both members accept before revealing contacts
            - Suggest a first-date venue
API:        REST
            POST /chat
            GET  /introductions
            POST /introductions/{id}/respond
Storage:    PostgreSQL with pgvector
Tech stack: Flutter, FastAPI, OpenAI API
```

---

## Example 211

**Intent:**
walking school bus app

**Spec:**
```
Type:       Mobile application with backend (school safety)
Auth:       Parent email login approved by school
Data model: Route(id, name, stops)
            Stop(id, route_id -> Route, name, lat, lng, time)
            Child(id, parent_id -> Parent, name, route_id -> Route)
            Parent(id, name, phone)
            WalkDay(id, route_id -> Route, date, leader_id -> Parent)
            Pickup(walk_day_id -> WalkDay, child_id -> Child, picked_at)
Features:   - Organize walking routes with stops and times
            - Assign a parent leader for each day
            - Tick off children at each stop
            - Notify parents when their child is picked up and arrives at school
API:        REST
            GET  /routes
            POST /walk-days
            POST /walk-days/{id}/pickups
            POST /walk-days/{id}/arrived
Storage:    PostgreSQL
Tech stack: Flutter, Firebase
```

---

## Example 212

**Intent:**
hey i need app for my laundry pickup but with lockers in apartment lobbies, people drop clothes in locker, our driver collect

**Spec:**
```
Type:       Mobile application with backend (locker-based service)
Auth:       Phone login with SMS code
Data model: Customer(id, phone, building_id -> Building)
            Building(id, address)
            Locker(id, building_id -> Building, number, status)
            LaundryJob(id, customer_id -> Customer, locker_id -> Locker, status, weight_kg, price)
Features:   - Reserve a lobby locker and get its code
            - Drop off clothes and confirm in the app
            - Notify the driver of full lockers on the route
            - Return clean clothes to a locker and send the code
            - Charge by weight
API:        REST
            POST /jobs
            POST /jobs/{id}/dropped
            GET  /drivers/route
            PATCH /jobs/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Stripe
```

---

## Example 213

**Intent:**
an app for my volleyball league to post scores and standings

**Spec:**
```
Type:       Mobile application with backend (sports league)
Auth:       Team captains log in with email; public can view
Data model: Team(id, name, captain_email)
            Match(id, home_id -> Team, away_id -> Team, scheduled_at, court, sets_home, sets_away, status)
            Standing(team_id -> Team, wins, losses, points)
Features:   - Show the season schedule
            - Let captains submit set scores
            - Require the other captain to confirm
            - Update standings automatically
API:        REST
            GET  /matches
            POST /matches/{id}/score
            POST /matches/{id}/confirm
            GET  /standings
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 214

**Intent:**
Please app for my small hotel in Vietnam, guest can book tour and motorbike rental from the reception by phone

**Spec:**
```
Type:       Mobile application with backend (hotel services)
Auth:       Guest login with room number and booking code
Data model: Guest(id, name, room_number, booking_code)
            Tour(id, name, date, price, seats_left)
            Motorbike(id, plate, daily_price, status)
            Order(id, guest_id -> Guest, item_type, item_id, date, status, total)
Features:   - Show tours and motorbikes available
            - Book a tour or rent a motorbike
            - Add the cost to the room bill
            - Show booking confirmation in Vietnamese and English
API:        REST
            GET  /tours
            GET  /motorbikes
            POST /orders
            GET  /guests/me/bill
Storage:    PostgreSQL
Tech stack: Flutter (with i18n), Node.js
```

---

## Example 215

**Intent:**
app to organize our dinner club where everyone hosts once a month

**Spec:**
```
Type:       Mobile application with backend (social club)
Auth:       Email login
Data model: Member(id, name, email, diet)
            Dinner(id, host_id -> Member, date, theme, menu)
            Seat(dinner_id -> Dinner, member_id -> Member, bringing)
Features:   - Rotate the host each month
            - Show the next dinner with theme and menu
            - Sign up for a seat and say what you bring
            - Show members' dietary restrictions to the host
API:        REST
            GET  /dinners
            POST /dinners
            POST /dinners/{id}/seats
Storage:    SQLite
Tech stack: Flutter, PocketBase
```

---

## Example 216

**Intent:**
social app for sharing car meets

**Spec:**
```
Type:       Mobile application with backend (enthusiast community)
Auth:       Email or Google login
Data model: Driver(id, name)
            Car(id, owner_id -> Driver, make, model, year, mods, photos)
            Meet(id, organizer_id -> Driver, title, location, starts_at)
            MeetAttendee(meet_id -> Meet, driver_id -> Driver, car_id -> Car)
Features:   - Show off your car with photos and mods
            - Post car meets on a map
            - RSVP with the car you are bringing
            - Follow other drivers
API:        REST
            POST /cars
            GET  /meets
            POST /meets
            POST /meets/{id}/rsvp
Storage:    PostgreSQL, S3 (photos)
Tech stack: React Native, NestJS
```

---

## Example 217

**Intent:**
bus pass app with qr code tickets that the driver scans

**Spec:**
```
Type:       Mobile application with backend (mobile ticketing)
Auth:       Email login with card on file
Data model: Rider(id, email)
            Pass(id, rider_id -> Rider, type, valid_from, valid_until)
            Ticket(id, rider_id -> Rider, qr_token, activated_at, expires_at)
            Validation(id, ticket_id -> Ticket, bus_id, at)
Features:   - Buy single tickets or monthly passes
            - Show a rotating QR code that cannot be screenshotted
            - Let drivers scan and validate tickets offline
            - Sync validations when the bus is back online
API:        REST
            POST /tickets
            POST /passes
            GET  /me/tickets
            POST /validations/batch
Storage:    PostgreSQL
Tech stack: Kotlin (Android), Swift (iOS), Spring Boot, Stripe
```

---

## Example 218

**Intent:**
app where i can play poker with my friends online, fake chips

**Spec:**
```
Type:       Mobile game (online card game)
Auth:       Sign in with Google
Data model: Player(id, name, chips)
            Table(id, code, small_blind, max_seats, status)
            Seat(table_id -> Table, player_id -> Player, stack)
            Hand(id, table_id -> Table, deck_seed, pot, board, winner_id -> Player)
Features:   - Create a private Texas Hold'em table
            - Deal cards and run betting rounds on the server
            - Hide each player's hole cards from others
            - Evaluate hands and split pots
            - Give daily free chips
API:        REST + WebSocket
            POST /tables
            POST /tables/{code}/sit
            WS   /tables/{code}
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Node.js, Colyseus
```

---

## Example 219

**Intent:**
I teach swimming to kids at 3 pools in my city and want parents to book lessons, see which pool and get messages if a lesson is cancelled. Also parents should see the level their kid reached.

**Spec:**
```
Type:       Mobile application with backend (lesson booking)
Auth:       Parent email login; instructor admin login
Data model: Pool(id, name, address)
            Child(id, parent_id -> Parent, name, birth_year, level)
            Parent(id, name, email)
            LessonSlot(id, pool_id -> Pool, starts_at, level, capacity)
            Enrollment(slot_id -> LessonSlot, child_id -> Child)
Features:   - Show lesson slots by pool and level
            - Enroll a child in a slot
            - Cancel lessons and notify enrolled parents
            - Update each child's swimming level after lessons
API:        REST
            GET  /slots?pool={id}
            POST /slots/{id}/enrollments
            POST /slots/{id}/cancel
            PATCH /children/{id}/level
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 220

**Intent:**
lost item finder for airports

**Spec:**
```
Type:       Mobile application with backend (lost and found)
Auth:       Passenger email login; airport staff accounts
Data model: FoundItem(id, category, description, photo_url, found_at, location, status)
            LostReport(id, passenger_email, category, description, flight_no, lost_at)
            MatchCandidate(report_id -> LostReport, item_id -> FoundItem, score)
Features:   - Let staff log found items with photos
            - Let passengers report a lost item
            - Suggest matches by category, time and description
            - Arrange pickup or shipping for matched items
API:        REST
            POST /found-items
            POST /lost-reports
            GET  /lost-reports/{id}/matches
            POST /matches/{id}/claim
Storage:    PostgreSQL
Tech stack: Flutter, FastAPI, sentence-transformers (text matching)
```

---

## Example 221

**Intent:**
fleet app for my 12 delivery vans, see where they are and fuel used

**Spec:**
```
Type:       Mobile application with backend (fleet tracking)
Auth:       Manager email login; drivers log in with PIN
Data model: Van(id, plate, driver_id -> Driver, lat, lng, odometer)
            Driver(id, name, pin_hash)
            FuelLog(id, van_id -> Van, liters, cost, odometer, receipt_url, at)
            Trip(id, van_id -> Van, started_at, ended_at, km)
Features:   - Track each van's live location on a map
            - Let drivers log fuel with a receipt photo
            - Calculate fuel consumption per van
            - Alert on harsh braking or speeding
API:        REST
            GET  /vans
            POST /vans/{id}/positions
            POST /fuel-logs
            GET  /reports/fuel
Storage:    PostgreSQL, TimescaleDB (positions)
Tech stack: Flutter, NestJS, Google Maps SDK
```

---

## Example 222

**Intent:**
give me an app that alerts everyone on our street if theres a power outage

**Spec:**
```
Type:       Mobile application with backend (community alerts)
Auth:       Phone login with street address
Data model: Resident(id, phone, street_id -> Street)
            Street(id, name, city)
            OutageReport(id, street_id -> Street, resident_id -> Resident, at)
            Outage(id, street_id -> Street, started_at, ended_at)
Features:   - Report an outage with one tap
            - Confirm an outage when 3 neighbors report it
            - Push an alert to everyone on the street
            - Mark power restored
API:        REST
            POST /outages/report
            GET  /streets/{id}/outage
            POST /outages/{id}/restored
Storage:    PostgreSQL
Tech stack: Flutter, Firebase Cloud Functions, Cloud Firestore
```

---

## Example 223

**Intent:**
a family calendar that every family member can edit with kids pickup duties

**Spec:**
```
Type:       Mobile application with backend (shared calendar)
Auth:       Email login; members join a family by invite
Data model: Family(id, name)
            Member(id, family_id -> Family, name, color)
            Event(id, family_id -> Family, title, starts_at, ends_at, assigned_to -> Member, recurring_rule)
Features:   - Show a shared family calendar color-coded by person
            - Assign pickup and drop-off duties
            - Repeat events weekly
            - Notify the assigned person 30 minutes before
API:        REST
            GET  /families/{id}/events?week={d}
            POST /events
            PATCH /events/{id}
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 224

**Intent:**
wifi password sharing app for cafes lol

**Spec:**
```
Type:       Mobile application with backend (crowdsourced)
Auth:       Optional Google login
Data model: Place(id, name, lat, lng)
            WifiEntry(id, place_id -> Place, ssid, password, added_by, confirmed_count, updated_at)
Features:   - Show nearby cafes with known Wi-Fi
            - Add the network name and password
            - Confirm the password still works
            - Connect to the network with one tap on Android
API:        REST
            GET  /places/nearby
            POST /places/{id}/wifi
            POST /wifi/{id}/confirm
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin (Android WifiNetworkSuggestion API), Ktor
```

---

## Example 225

**Intent:**
mobile app for my orchestra to manage sheet music for each player

**Spec:**
```
Type:       Mobile application with backend (music ensemble)
Auth:       Member email login; librarian admin
Data model: Musician(id, name, instrument, chair)
            Piece(id, title, composer)
            Part(id, piece_id -> Piece, instrument, pdf_url)
            Concert(id, date, venue)
            ConcertPiece(concert_id -> Concert, piece_id -> Piece, order)
Features:   - Upload part PDFs for each piece
            - Show each musician the parts for upcoming concerts
            - Annotate PDFs on the tablet and sync annotations
            - Notify players when a new part is added
API:        REST
            GET  /concerts
            GET  /concerts/{id}/my-parts
            POST /pieces/{id}/parts
            PUT  /parts/{id}/annotations
Storage:    PostgreSQL, S3 (PDFs)
Tech stack: Flutter (Syncfusion PDF viewer), Django REST Framework
```

---

## Example 226

**Intent:**
farm to table subscription box with weekly delivery and skip option

**Spec:**
```
Type:       Mobile application with backend (subscription delivery)
Auth:       Email login
Data model: Subscriber(id, name, email, address, box_size)
            Box(id, week, contents)
            Delivery(id, subscriber_id -> Subscriber, box_id -> Box, status, skipped)
Features:   - Choose a box size and subscribe
            - Show this week's box contents
            - Skip a week before the cutoff
            - Charge weekly automatically
            - Pause or cancel the subscription
API:        REST
            POST /subscriptions
            GET  /boxes/current
            POST /deliveries/{id}/skip
            PATCH /subscriptions/{id}
Storage:    PostgreSQL
Tech stack: React Native, Rails API, Stripe Billing
```

---

## Example 227

**Intent:**
chat app for neighbors in the same apartment building to borrow stuff and gossip

**Spec:**
```
Type:       Mobile application with backend (building community)
Auth:       Email login with apartment verification by manager
Data model: Resident(id, name, unit, building_id -> Building)
            Building(id, name)
            Post(id, building_id -> Building, author_id -> Resident, kind, body, created_at)
            Reply(id, post_id -> Post, author_id -> Resident, body)
Features:   - Post borrow requests, offers and general chat
            - Reply in threads
            - Only show posts from your building
            - Notify residents of new borrow requests
API:        REST
            GET  /buildings/{id}/posts
            POST /posts
            POST /posts/{id}/replies
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 228

**Intent:**
tiny app for my church youth group to share a weekly bible verse and discuss

**Spec:**
```
Type:       Mobile application with backend (small group)
Auth:       Join with a group code and name
Data model: Group(id, name, code)
            Verse(id, group_id -> Group, reference, text, week)
            Post(id, verse_id -> Verse, author_name, text, at)
Features:   - Post the verse of the week
            - Discuss it in a comment thread
            - Send a push notification when the new verse is posted
API:        REST
            GET  /groups/{code}/verse
            POST /verses
            POST /verses/{id}/posts
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase
```

---

## Example 229

**Intent:**
i need help building an app with flutter + supabase for my tutoring center where parents see attendance and pay invoices

**Spec:**
```
Type:       Mobile application with backend (education center)
Auth:       Supabase Auth (email + password) with parent and staff roles
Data model: Parent(id, name, email)
            Student(id, parent_id -> Parent, name, grade)
            Session(id, subject, starts_at, tutor_name)
            Attendance(session_id -> Session, student_id -> Student, present)
            Invoice(id, parent_id -> Parent, month, amount, paid)
Features:   - Let staff mark attendance per session
            - Show parents their child's attendance history
            - Generate monthly invoices by sessions attended
            - Pay invoices by card
Storage:    Supabase PostgreSQL with row-level security
Tech stack: Flutter, Supabase (Auth, Database, Edge Functions), Stripe
```

---

## Example 230

**Intent:**
soundboard app where friends upload sounds and play them in a shared room

**Spec:**
```
Type:       Mobile application with backend (real-time social)
Auth:       Guest nickname in a room
Data model: Room(id, code)
            Sound(id, room_id -> Room, name, audio_url, uploaded_by)
Features:   - Upload short sound clips to a room
            - Tap a sound to play it on everyone's phone
            - Limit clips to 5 seconds
            - Delete rooms after a day of inactivity
API:        REST + WebSocket
            POST /rooms
            POST /rooms/{code}/sounds
            WS   /rooms/{code}
Storage:    Redis, S3 (audio)
Tech stack: React Native, Node.js
```

---

## Example 231

**Intent:**
i want build app that connect old people that are lonely with young people for phone calls every week. i am social worker in Germany

**Spec:**
```
Type:       Mobile application with backend (social connection)
Auth:       Phone login; volunteers verified by the social worker
Data model: Senior(id, name, phone, interests, language)
            Volunteer(id, name, phone, interests, verified)
            Pairing(id, senior_id -> Senior, volunteer_id -> Volunteer, weekly_slot)
            CallLog(id, pairing_id -> Pairing, called_at, duration_min, note)
Features:   - Pair seniors with volunteers by interests and language
            - Schedule a weekly call slot
            - Remind the volunteer before each call
            - Log calls and flag concerns to the social worker
API:        REST
            POST /pairings
            GET  /volunteers/me/pairings
            POST /pairings/{id}/calls
            GET  /admin/concerns
Storage:    PostgreSQL (hosted in the EU)
Tech stack: Flutter, Django REST Framework
```

---

## Example 232

**Intent:**
in-app chat for my marketplace app buyers and sellers

**Spec:**
```
Type:       Mobile application with backend (messaging feature)
Auth:       Uses existing marketplace JWT login
Data model: Conversation(id, listing_id, buyer_id, seller_id, last_message_at)
            Message(id, conversation_id -> Conversation, sender_id, text, image_url, sent_at, read_at)
Features:   - Start a conversation from a listing
            - Send text and image messages
            - Show unread badges
            - Block a user from messaging
API:        REST + WebSocket
            GET  /conversations
            POST /conversations
            GET  /conversations/{id}/messages
            WS   /chat
Storage:    PostgreSQL, Redis (pub/sub)
Tech stack: React Native, Node.js, Socket.IO
```

---

## Example 233

**Intent:**
app for golf buddies to keep score and settle bets

**Spec:**
```
Type:       Mobile application with backend (sports social)
Auth:       Sign in with Apple or Google
Data model: Golfer(id, name, handicap)
            Round(id, course_name, date)
            RoundPlayer(round_id -> Round, golfer_id -> Golfer)
            HoleScore(round_id -> Round, golfer_id -> Golfer, hole, strokes)
            Bet(id, round_id -> Round, type, stake)
Features:   - Start a round with friends
            - Enter scores hole by hole with live sync
            - Apply handicaps for net scores
            - Calculate skins and Nassau bet results
API:        REST + WebSocket
            POST /rounds
            PUT  /rounds/{id}/scores
            GET  /rounds/{id}/settlement
            WS   /rounds/{id}
Storage:    PostgreSQL
Tech stack: Swift (SwiftUI), Firebase
```

---

## Example 234

**Intent:**
community fridge map

**Spec:**
```
Type:       Mobile application with backend (crowdsourced)
Auth:       Optional email login
Data model: Fridge(id, name, lat, lng, hours)
            StockUpdate(id, fridge_id -> Fridge, level, photo_url, note, at)
Features:   - Show community fridges on a map
            - Post how full a fridge is with a photo
            - Show the last update time
            - Notify followers when a fridge is restocked
API:        REST
            GET  /fridges
            POST /fridges/{id}/updates
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 235

**Intent:**
wanna build a mobile app for my airsoft field: players sign waivers, book game days, and track kills with team scoring

**Spec:**
```
Type:       Mobile application with backend (sports venue)
Auth:       Email login
Data model: Player(id, name, email, birth_date)
            Waiver(player_id -> Player, signature_url, signed_at)
            GameDay(id, date, scenario, capacity)
            Registration(game_day_id -> GameDay, player_id -> Player, team)
            Hit(id, game_day_id -> GameDay, shooter_id -> Player, target_id -> Player, at)
Features:   - Sign the waiver digitally once a year
            - Book a spot on a game day
            - Assign teams to balance numbers
            - Log hits and show team scores live
API:        REST
            POST /waivers
            GET  /game-days
            POST /game-days/{id}/registrations
            POST /game-days/{id}/hits
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 236

**Intent:**
app for my bakery's daily bread pre-orders

**Spec:**
```
Type:       Mobile application with backend (preordering)
Auth:       Phone login with SMS code
Data model: Customer(id, phone, name)
            Bread(id, name, price, daily_limit)
            Preorder(id, customer_id -> Customer, bread_id -> Bread, quantity, pickup_date)
Features:   - Show tomorrow's breads and how many are left
            - Preorder before 8 pm
            - Show the baker a bake list for tomorrow
            - Pay at pickup
API:        REST
            GET  /breads?date={d}
            POST /preorders
            GET  /bake-list?date={d}
Storage:    SQLite
Tech stack: Flutter, FastAPI
```

---

## Example 237

**Intent:**
ride hailing app for women, drivers are women only

**Spec:**
```
Type:       Mobile application with backend (ride hailing)
Auth:       Phone login with SMS code and ID verification
Data model: Rider(id, name, phone, verified)
            Driver(id, name, phone, verified, vehicle, is_online, lat, lng)
            Ride(id, rider_id -> Rider, driver_id -> Driver, pickup, dropoff, fare, status)
            EmergencyContact(rider_id -> Rider, name, phone)
Features:   - Verify riders and drivers with ID and selfie
            - Match rides with nearby women drivers
            - Share the trip live with an emergency contact
            - Add an in-app SOS button
            - Rate each ride
API:        REST + WebSocket
            POST /rides
            PATCH /rides/{id}
            POST /rides/{id}/sos
            WS   /rides/{id}/track
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, NestJS, Veriff (ID verification)
```

---

## Example 238

**Intent:**
duolingo but you compete with friends weekly

**Spec:**
```
Type:       Mobile application with backend (gamified learning)
Auth:       Email or Google login
Data model: Learner(id, name, language, xp_total)
            Lesson(id, language, unit, exercises_json)
            LessonResult(id, learner_id -> Learner, lesson_id -> Lesson, xp, finished_at)
            League(id, week)
            LeagueMember(league_id -> League, learner_id -> Learner, weekly_xp)
Features:   - Complete short vocabulary lessons for XP
            - Join a weekly league with friends
            - Show a weekly XP leaderboard
            - Reset leagues every Monday
API:        REST
            GET  /lessons/next
            POST /lessons/{id}/results
            GET  /leagues/current
Storage:    PostgreSQL, Redis (leaderboards)
Tech stack: React Native, NestJS
```

---

## Example 239

**Intent:**
whiteboard app where my team draws together from tablets

**Spec:**
```
Type:       Mobile application with backend (real-time collaboration)
Auth:       Email login
Data model: Board(id, title, owner_id -> User)
            BoardMember(board_id -> Board, user_id -> User)
            Stroke(id, board_id -> Board, user_id -> User, points, color, width, at)
            User(id, email)
Features:   - Create boards and invite teammates
            - Draw with a stylus and sync strokes instantly
            - Show other users' cursors
            - Undo your own strokes
            - Export the board as PNG
API:        REST + WebSocket
            POST /boards
            GET  /boards/{id}
            WS   /boards/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Yjs (CRDT), y-websocket server
```

---

## Example 240

**Intent:**
carpool for skiers going to the mountain from the city on weekends

**Spec:**
```
Type:       Mobile application with backend (carpooling)
Auth:       Email or Google login
Data model: Skier(id, name, rating)
            Trip(id, driver_id -> Skier, resort, date, departure_point, seats, gear_space)
            Booking(trip_id -> Trip, skier_id -> Skier, status)
Features:   - Offer seats to a ski resort on a date
            - Show gear space for skis and boards
            - Book a seat and split fuel costs
            - Show road conditions for the route
API:        REST
            GET  /trips?resort={r}&date={d}
            POST /trips
            POST /trips/{id}/bookings
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 241

**Intent:**
pet microchip lookup app for vets and shelters to reach owners

**Spec:**
```
Type:       Mobile application with backend (registry)
Auth:       Vet and shelter staff accounts verified by admin
Data model: Owner(id, name, phone, email)
            Pet(id, owner_id -> Owner, name, species, chip_number)
            Lookup(id, chip_number, staff_id -> Staff, at)
            Staff(id, organization, email)
Features:   - Scan or type a microchip number
            - Show the pet and a way to contact the owner without exposing details
            - Notify the owner that their pet was found
            - Log every lookup
API:        REST
            GET  /chips/{number}
            POST /chips/{number}/notify-owner
Storage:    PostgreSQL
Tech stack: Kotlin (Android), Ktor
```

---

## Example 242

**Intent:**
interactive fan app for our minor league baseball team: trivia between innings, seat upgrades, and food ordering

**Spec:**
```
Type:       Mobile application with backend (fan engagement)
Auth:       Email or Apple login
Data model: Fan(id, name, points)
            Game(id, opponent, date)
            TriviaQuestion(id, game_id -> Game, inning, question, options, answer)
            TriviaAnswer(question_id -> TriviaQuestion, fan_id -> Fan, choice)
            FoodOrder(id, fan_id -> Fan, seat, items, status)
Features:   - Push a trivia question between innings
            - Award points for correct answers
            - Spend points on seat upgrades
            - Order food to your seat
API:        REST + WebSocket
            GET  /games/today
            POST /trivia/{id}/answer
            POST /orders
            WS   /games/{id}/live
Storage:    PostgreSQL
Tech stack: React Native, NestJS, Socket.IO
```

---

## Example 243

**Intent:**
whos at the office today app

**Spec:**
```
Type:       Mobile application with backend (hybrid work)
Auth:       Company Google Workspace login
Data model: Employee(id, name, team)
            OfficeDay(employee_id -> Employee, date, office)
Features:   - Mark which days you will be in the office
            - See which teammates are in on a day
            - Suggest days when most of your team is in
API:        REST
            GET  /office-days?week={d}
            PUT  /office-days/{date}
Storage:    PostgreSQL
Tech stack: Flutter, Firebase Auth, Express
```

---

## Example 244

**Intent:**
app 4 my frat to track who owes dues and party signups

**Spec:**
```
Type:       Mobile application with backend (student organization)
Auth:       University email login; treasurer admin role
Data model: Brother(id, name, email, pledge_class)
            Due(id, brother_id -> Brother, semester, amount, paid)
            Party(id, theme, date, capacity)
            PartySignup(party_id -> Party, brother_id -> Brother, guest_names)
Features:   - Show each member's dues balance
            - Pay dues by card
            - Sign up for parties with guest names
            - Cap guests at party capacity
API:        REST
            GET  /me/dues
            POST /dues/{id}/pay
            GET  /parties
            POST /parties/{id}/signups
Storage:    PostgreSQL
Tech stack: React Native, Express, Stripe
```

---

## Example 245

**Intent:**
need mobile app tracking garbage trucks so people know when to put bins out

**Spec:**
```
Type:       Mobile application with backend (municipal services)
Auth:       No login for residents; driver tablet login
Data model: Truck(id, route_id -> Route, lat, lng, updated_at)
            Route(id, name, area_polygon, weekday)
            Subscription(device_token, route_id -> Route)
Features:   - Find your collection route by address
            - Show the truck's live position on collection day
            - Notify residents when the truck is 2 streets away
            - Show the holiday schedule
API:        REST
            GET  /routes/lookup?address={a}
            GET  /routes/{id}/truck
            POST /trucks/{id}/position
            POST /subscriptions
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Go, Firebase Cloud Messaging
```

---

## Example 246

**Intent:**
guess the song game, play with friends real time

**Spec:**
```
Type:       Mobile game (real-time music quiz)
Auth:       Guest nicknames; host signs in with Spotify
Data model: Room(id, code, playlist_id, round)
            Player(id, room_id -> Room, nickname, score)
            Round(id, room_id -> Room, track_id, started_at)
Features:   - Pick a Spotify playlist for the game
            - Play a 10-second snippet each round
            - Let players type the song title
            - Score by speed and show a leaderboard
API:        REST + WebSocket
            POST /rooms
            POST /rooms/{code}/join
            WS   /rooms/{code}
Storage:    Redis
Tech stack: React Native, Node.js, Spotify Web API
```

---

## Example 247

**Intent:**
sports team app in flutterflow + firebase for my rugby club, fixtures, availability, and player stats

**Spec:**
```
Type:       Mobile application with backend (sports club)
Auth:       Firebase Authentication (email + password)
Data model: Player(id, name, position, email)
            Fixture(id, opponent, kickoff, venue, result)
            Availability(fixture_id -> Fixture, player_id -> Player, available)
            PlayerStat(fixture_id -> Fixture, player_id -> Player, tries, tackles, minutes)
Features:   - Show upcoming fixtures
            - Mark availability for each fixture
            - Let the coach pick the team sheet
            - Record player stats after each game
            - Show season stats per player
Storage:    Cloud Firestore
Tech stack: FlutterFlow, Firebase (Auth, Firestore, Cloud Messaging)
```

---

## Example 248

**Intent:**
An app for parents in my kid's class to coordinate playdates.

**Spec:**
```
Type:       Mobile application with backend (parent community)
Auth:       Email login with class invite code
Data model: Parent(id, name, email, class_id -> Class)
            Child(id, parent_id -> Parent, name, interests)
            Class(id, school, name, code)
            Playdate(id, host_id -> Parent, date, location, max_kids)
            PlaydateGuest(playdate_id -> Playdate, child_id -> Child, status)
Features:   - Join your child's class group
            - Propose a playdate with date and place
            - Invite specific kids or open it to the class
            - Track who is coming
API:        REST
            POST /classes/join
            POST /playdates
            POST /playdates/{id}/invites
            PATCH /invites/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 249

**Intent:**
app so contractors can send daily photo updates to homeowners during a renovation

**Spec:**
```
Type:       Mobile application with backend (client updates)
Auth:       Contractor email login; homeowners join by project invite
Data model: Contractor(id, company, email)
            Project(id, contractor_id -> Contractor, address, homeowner_email)
            Update(id, project_id -> Project, text, photos, posted_at)
            ChangeOrder(id, project_id -> Project, description, cost, approved_at)
Features:   - Post daily photo updates for a project
            - Let homeowners comment on updates
            - Send change orders for homeowner approval
            - Keep a timeline of the whole renovation
API:        REST
            POST /projects
            POST /projects/{id}/updates
            POST /projects/{id}/change-orders
            POST /change-orders/{id}/approve
Storage:    PostgreSQL, S3 (photos)
Tech stack: React Native, Ruby on Rails API
```

---

## Example 250

**Intent:**
hiii can u make a app for my friends to vote on movie for movie night every friday

**Spec:**
```
Type:       Mobile application with backend (group voting)
Auth:       Join a group with a code and nickname
Data model: Group(id, name, code)
            Member(id, group_id -> Group, nickname)
            MovieNight(id, group_id -> Group, date, winner_tmdb_id)
            Nomination(id, night_id -> MovieNight, tmdb_id, title, poster_url)
            Vote(nomination_id -> Nomination, member_id -> Member)
Features:   - Nominate movies by searching TMDB
            - Vote for up to 3 movies
            - Close voting Friday at 6 pm and announce the winner
            - Avoid movies already watched
API:        REST
            POST /groups
            GET  /groups/{id}/nights/current
            POST /nights/{id}/nominations
            POST /nominations/{id}/vote
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase, TMDB API
```

---

## Example 251

**Intent:**
app for cleaners and clients, clients rate cleaning and tip

**Spec:**
```
Type:       Mobile application with backend (home services)
Auth:       Email login with client and cleaner roles
Data model: Client(id, name, address)
            Cleaner(id, name, rating)
            Cleaning(id, client_id -> Client, cleaner_id -> Cleaner, scheduled_at, checklist, status)
            Rating(cleaning_id -> Cleaning, stars, comment, tip)
Features:   - Book recurring cleanings
            - Show the cleaner a checklist per home
            - Let clients rate each cleaning
            - Add a tip after the rating
            - Pay cleaners weekly
API:        REST
            POST /cleanings
            GET  /cleaners/me/cleanings
            POST /cleanings/{id}/rating
Storage:    PostgreSQL
Tech stack: Flutter, NestJS, Stripe Connect
```

---

## Example 252

**Intent:**
geocaching style app for our city museum with hidden digital treasures

**Spec:**
```
Type:       Mobile game (location-based)
Auth:       Guest play with optional email to save progress
Data model: Treasure(id, name, story, lat, lng, radius_m, image_url)
            Player(id, nickname)
            Find(player_id -> Player, treasure_id -> Treasure, found_at)
Features:   - Show hint areas on the city map
            - Unlock a treasure when inside its radius
            - Show the museum story behind each treasure
            - Award a badge for finding all treasures
API:        REST
            GET  /treasures
            POST /treasures/{id}/find
            GET  /players/{id}/finds
Storage:    PostgreSQL
Tech stack: Flutter, Supabase, Mapbox
```

---

## Example 253

**Intent:**
we are students in Spain making app for share apartments rooms between Erasmus students, with chat and reviews of landlords

**Spec:**
```
Type:       Mobile application with backend (student housing)
Auth:       University email verification
Data model: Student(id, name, university, country)
            Landlord(id, name, rating)
            RoomListing(id, landlord_id -> Landlord, city, rent, available_from, photos)
            LandlordReview(id, landlord_id -> Landlord, student_id -> Student, stars, text)
            Chat(id, listing_id -> RoomListing, student_id -> Student)
Features:   - Post and search rooms by city and date
            - Review landlords after the stay
            - Chat about a listing
            - Translate listings between languages
API:        REST
            GET  /rooms?city={c}
            POST /rooms
            POST /landlords/{id}/reviews
            POST /rooms/{id}/chats
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, DeepL API
```

---

## Example 254

**Intent:**
app that alerts my neighbors if my house alarm goes off when I'm away

**Spec:**
```
Type:       IoT system (with mobile app)
Auth:       Email login; neighbors invited by the homeowner
Data model: Home(id, owner_id -> User, address)
            Alarm(id, home_id -> Home, device_serial)
            Watcher(home_id -> Home, user_id -> User)
            AlarmEvent(id, alarm_id -> Alarm, type, at, resolved_by -> User)
            User(id, name, phone)
Features:   - Receive alarm triggers from the home system
            - Notify the owner and invited neighbors
            - Let a neighbor say "I'm checking" to others
            - Resolve the event with a note
API:        REST
            POST /alarms/{id}/events
            POST /events/{id}/claim
            POST /events/{id}/resolve
            POST /homes/{id}/watchers
Storage:    PostgreSQL
Tech stack: Home Assistant webhook, Node.js, React Native
```

---

## Example 255

**Intent:**
hey, so I run a dance studio with like 200 students, mostly teens. right now we use paper sign-in sheets and a facebook group. i'd love an app where they see the class schedule, get notified when a class is cancelled, buy class packs, and check in with a QR code at the front desk

**Spec:**
```
Type:       Mobile application with backend (studio management)
Auth:       Email login; parents manage accounts for students under 16
Data model: Student(id, name, birth_date, guardian_id -> Guardian, credits)
            Guardian(id, name, email)
            DanceClass(id, style, level, instructor, starts_at, room)
            CheckIn(class_id -> DanceClass, student_id -> Student, at)
            Purchase(id, student_id -> Student, pack_size, paid_at)
Features:   - Show the weekly class schedule by style and level
            - Push alerts when a class is cancelled
            - Buy class packs online
            - Check in by scanning the desk QR code
            - Deduct one credit per check-in
API:        REST
            GET  /classes
            POST /classes/{id}/checkin
            POST /purchases
            PATCH /classes/{id}
Storage:    PostgreSQL
Tech stack: React Native, NestJS, Stripe
```

---

## Example 256

**Intent:**
festival app

**Spec:**
```
Type:       Mobile application with backend (event guide)
Auth:       Optional login to save a personal schedule
Data model: Stage(id, name, lat, lng)
            Act(id, name, genre, bio, image_url)
            Performance(id, act_id -> Act, stage_id -> Stage, starts_at, ends_at)
            FavoriteAct(user_id, act_id -> Act)
Features:   - Show the lineup by day and stage
            - Build a personal schedule and warn about clashes
            - Show a festival map with stages and food
            - Push urgent announcements like weather alerts
API:        REST
            GET  /lineup
            GET  /map
            POST /me/favorites
            GET  /announcements
Storage:    PostgreSQL
Tech stack: Flutter, Strapi
```

---

## Example 257

**Intent:**
horse riding stable app for lesson bookings and horse care schedule

**Spec:**
```
Type:       Mobile application with backend (stable management)
Auth:       Email login with rider and staff roles
Data model: Horse(id, name, level, max_lessons_per_day)
            Rider(id, name, level)
            Lesson(id, rider_id -> Rider, horse_id -> Horse, starts_at, instructor)
            CareTask(id, horse_id -> Horse, type, due_at, done_by)
Features:   - Book riding lessons
            - Assign horses without exceeding their daily limit
            - Schedule feeding, farrier and vet tasks
            - Mark care tasks done
API:        REST
            POST /lessons
            GET  /horses/{id}/schedule
            POST /care-tasks
            PATCH /care-tasks/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Laravel
```

---

## Example 258

**Intent:**
plz make like a whatsapp channel app for our football fan club to get match news and meetup spots

**Spec:**
```
Type:       Mobile application with backend (broadcast channel)
Auth:       Phone login with SMS code
Data model: Fan(id, phone, name)
            Post(id, author_id -> Admin, text, image_url, posted_at)
            Meetup(id, match, place, lat, lng, at)
            Admin(id, name)
Features:   - Broadcast news posts to all fans
            - Post meetup spots before away matches
            - React to posts with emoji
            - Push notifications for new posts
API:        REST
            GET  /posts
            POST /posts
            GET  /meetups
            POST /posts/{id}/reactions
Storage:    PostgreSQL
Tech stack: Flutter, Express, OneSignal
```

---

## Example 259

**Intent:**
iot app for my aquarium, monitor ph and temp and control the lights

**Spec:**
```
Type:       IoT system (with mobile companion app)
Auth:       Email login
Data model: Tank(id, owner_id -> User, name, volume_l)
            Reading(tank_id -> Tank, ph, temp_c, at)
            LightSchedule(tank_id -> Tank, on_time, off_time, intensity)
            User(id, email)
Features:   - Show live pH and temperature
            - Alert when values leave a safe range
            - Switch the lights on and off remotely
            - Set a daily light schedule with sunrise dimming
API:        REST
            GET  /tanks/{id}/readings
            PUT  /tanks/{id}/lights
            POST /tanks/{id}/lights/toggle
Storage:    InfluxDB, PostgreSQL
Tech stack: ESP32, MQTT, Node-RED, Flutter
```

---

## Example 260

**Intent:**
classified ads app for my country, like craigslist

**Spec:**
```
Type:       Mobile application with backend (classifieds)
Auth:       Phone login with SMS code
Data model: User(id, phone, name)
            Category(id, name, parent_id -> Category)
            Ad(id, user_id -> User, category_id -> Category, title, description, price, city, photos, status, created_at)
            Favorite(user_id -> User, ad_id -> Ad)
Features:   - Post an ad with photos in a category
            - Search ads by keyword, category and city
            - Call or message the seller
            - Expire ads after 30 days
            - Report scam ads
API:        REST
            GET  /ads?q={q}&city={c}
            POST /ads
            POST /ads/{id}/report
            POST /favorites
Storage:    PostgreSQL, Elasticsearch, S3
Tech stack: Flutter, Django REST Framework
```

---

## Example 261

**Intent:**
pool party RSVP and who brings what

**Spec:**
```
Type:       Mobile application with backend
Data model: Party(id, host_name, date, address)
            Guest(id, party_id -> Party, name, coming)
            ItemToBring(id, party_id -> Party, name, claimed_by -> Guest)
Features:   - Share an invite link
            - RSVP with a name
            - Claim items to bring from a list
            - Show the host who is bringing what
API:        REST
            GET  /parties/{id}
            POST /parties/{id}/guests
            POST /items/{id}/claim
Storage:    SQLite
Tech stack: React Native, PocketBase
```

---

## Example 262

**Intent:**
My team does on-site sound engineering for events and we need an app to share gear checklists for each gig, see who loaded which case into the van, and report broken equipment.

**Spec:**
```
Type:       Mobile application with backend (gear logistics)
Auth:       Email login for crew
Data model: CrewMember(id, name)
            Gig(id, venue, date)
            GearItem(id, name, case_id -> Case, status)
            Case(id, label, qr_code)
            GigCase(gig_id -> Gig, case_id -> Case, loaded_by -> CrewMember, loaded_at, returned_at)
            DamageReport(id, item_id -> GearItem, reporter_id -> CrewMember, note, photo_url)
Features:   - Build a gear checklist for each gig
            - Scan case QR codes when loading and unloading
            - Show which cases are still missing
            - Report broken gear with photos
            - Flag damaged items as unavailable
API:        REST
            GET  /gigs/{id}/cases
            POST /gigs/{id}/cases/{case_id}/load
            POST /gigs/{id}/cases/{case_id}/return
            POST /damage-reports
Storage:    PostgreSQL
Tech stack: React Native (Expo Camera), Express
```

---

## Example 263

**Intent:**
app where kids in a school bus can be tracked by parents

**Spec:**
```
Type:       Mobile application with backend (school transport)
Auth:       Parent login with phone; driver login with PIN
Data model: Bus(id, number, driver_id -> Driver, lat, lng)
            Student(id, name, bus_id -> Bus, parent_id -> Parent, stop_name)
            Parent(id, phone)
            BoardingEvent(student_id -> Student, bus_id -> Bus, type, at)
Features:   - Show the bus location to parents
            - Record when each child boards and leaves with an NFC card
            - Notify the parent on boarding and drop-off
            - Alert when the bus is near the stop
API:        REST + WebSocket
            POST /buses/{id}/position
            POST /boarding-events
            GET  /parents/me/children
            WS   /buses/{id}
Storage:    PostgreSQL
Tech stack: Flutter, NestJS, NFC readers
```

---

## Example 264

**Intent:**
build an app in xamarin for our company's field inspectors with offline forms

**Spec:**
```
Type:       Mobile application with backend (field inspections)
Auth:       Azure AD login
Data model: Inspector(id, name, region)
            Site(id, name, address)
            FormTemplate(id, name, fields_json, version)
            Inspection(id, site_id -> Site, inspector_id -> Inspector, template_id -> FormTemplate, answers_json, photos, completed_at)
Features:   - Download form templates and site lists for offline use
            - Fill inspections with photos and signatures offline
            - Sync completed inspections when online
            - Flag failed items for follow-up
API:        REST
            GET  /templates
            GET  /sites
            POST /inspections
Storage:    Azure SQL Database, SQLite on device
Tech stack: Xamarin.Forms (C#), ASP.NET Core, Azure Blob Storage
```

---

## Example 265

**Intent:**
matchmaking for chess clubs to play friendly matches

**Spec:**
```
Type:       Mobile application with backend (club matchmaking)
Auth:       Club captain email login
Data model: Club(id, name, city, avg_rating)
            Captain(id, club_id -> Club, email)
            MatchProposal(id, from_club -> Club, to_club -> Club, date, boards, status)
            BoardResult(match_id -> MatchProposal, board, white_player, black_player, result)
Features:   - Find clubs with similar average rating nearby
            - Propose a friendly match with a date and number of boards
            - Enter board-by-board results
            - Show club match history
API:        REST
            GET  /clubs?near={city}
            POST /matches
            PATCH /matches/{id}
            POST /matches/{id}/results
Storage:    PostgreSQL
Tech stack: Flutter, Spring Boot
```

---

## Example 266

**Intent:**
mom group app

**Spec:**
```
Type:       Mobile application with backend (parent community)
Auth:       Email login with invite from an existing member
Data model: Mom(id, name, neighborhood, kids_ages)
            Thread(id, author_id -> Mom, topic, body, created_at)
            Reply(id, thread_id -> Thread, author_id -> Mom, body)
            Meetup(id, title, place, at)
Features:   - Post questions and advice threads by topic
            - Reply and react to threads
            - Organize local meetups
            - Find moms with kids of a similar age nearby
API:        REST
            GET  /threads
            POST /threads
            POST /threads/{id}/replies
            GET  /meetups
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 267

**Intent:**
game where friends race to finish daily sudoku, see each other's times

**Spec:**
```
Type:       Mobile game (asynchronous competition)
Auth:       Sign in with Google or Apple
Data model: Player(id, name)
            Puzzle(id, date, grid, solution, difficulty)
            Solve(puzzle_id -> Puzzle, player_id -> Player, time_s, mistakes)
            Friendship(a_id -> Player, b_id -> Player)
Features:   - Serve the same daily puzzle to everyone
            - Time each solve and count mistakes
            - Show friends' times on a daily board
            - Keep solve streaks
API:        REST
            GET  /puzzles/today
            POST /puzzles/{id}/solves
            GET  /puzzles/{id}/friends-board
Storage:    PostgreSQL
Tech stack: Flutter, Go
```

---

## Example 268

**Intent:**
Can you design an app for a recycling company where households schedule pickup of electronics and get points?

**Spec:**
```
Type:       Mobile application with backend (pickup scheduling, rewards)
Auth:       Email or phone login
Data model: Household(id, name, address, points)
            Pickup(id, household_id -> Household, items_description, scheduled_date, status, weight_kg)
            Reward(id, name, points_cost)
            Redemption(id, household_id -> Household, reward_id -> Reward, at)
Features:   - Schedule an e-waste pickup with item descriptions
            - Award points by weight collected
            - Redeem points for vouchers
            - Show recycling impact over time
API:        REST
            POST /pickups
            PATCH /pickups/{id}
            GET  /rewards
            POST /redemptions
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 269

**Intent:**
my food co-op wants members to order bulk goods together and split the cases

**Spec:**
```
Type:       Mobile application with backend (group buying)
Auth:       Member email login
Data model: Member(id, name, email)
            Product(id, name, case_size, case_price, supplier)
            OrderRound(id, closes_at, status)
            Split(id, round_id -> OrderRound, product_id -> Product)
            Share(split_id -> Split, member_id -> Member, units)
Features:   - Open a monthly order round
            - Let members claim units from a case
            - Order only cases that are fully claimed
            - Calculate each member's bill
API:        REST
            GET  /rounds/current
            POST /splits/{id}/shares
            POST /rounds/{id}/close
            GET  /rounds/{id}/bills
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework
```

---

## Example 270

**Intent:**
i want somthing for my moving truck rental, ppl book the truck pick it up with a key box code and i see milage

**Spec:**
```
Type:       Mobile application with backend (vehicle rental)
Auth:       Email login with driver's license photo
Data model: Truck(id, name, size, keybox_id, odometer)
            Customer(id, name, email, license_photo_url)
            Rental(id, truck_id -> Truck, customer_id -> Customer, start_at, end_at, start_km, end_km, keybox_code, total)
Features:   - Book a truck for a time window
            - Send the key box code shortly before pickup
            - Record start and end mileage with photos
            - Charge per km driven after return
API:        REST
            GET  /trucks/availability
            POST /rentals
            POST /rentals/{id}/start
            POST /rentals/{id}/end
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 271

**Intent:**
grocery list app that my roommates and I share using firebase

**Spec:**
```
Type:       Mobile application with backend (shared list)
Auth:       Firebase Authentication (Google sign-in)
Data model: Household(id, name, member_ids)
            GroceryItem(id, household_id -> Household, name, added_by, bought)
Features:   - Share one grocery list per household
            - Add items and check them off live
            - Show who added each item
            - Clear bought items
Storage:    Cloud Firestore
Tech stack: React Native, Firebase
```

---

## Example 272

**Intent:**
social running game: run routes shaped like art (drawing with gps), share them

**Spec:**
```
Type:       Mobile application with backend (social fitness)
Auth:       Sign in with Strava
Data model: Runner(id, name)
            Artwork(id, runner_id -> Runner, title, track_geojson, distance_km, created_at)
            Like(artwork_id -> Artwork, runner_id -> Runner)
Features:   - Import a run from Strava as a GPS drawing
            - Post artworks to a public gallery
            - Like and comment on artworks
            - Feature the best drawing of the week
API:        REST
            POST /artworks/import
            GET  /artworks
            POST /artworks/{id}/like
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, FastAPI, Strava API
```

---

## Example 273

**Intent:**
neighborhood babysitter recommendations

**Spec:**
```
Type:       Mobile application with backend (local recommendations)
Auth:       Parent email login with neighborhood verification
Data model: Parent(id, name, neighborhood)
            Sitter(id, name, phone, age, added_by -> Parent)
            Recommendation(sitter_id -> Sitter, parent_id -> Parent, stars, comment)
Features:   - Add a babysitter you trust
            - Recommend sitters with stars and comments
            - Search sitters recommended by neighbors
            - Share contact only with verified parents
API:        REST
            GET  /sitters
            POST /sitters
            POST /sitters/{id}/recommendations
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 274

**Intent:**
emergency alert app for a university campus

**Spec:**
```
Type:       Mobile application with backend (emergency notification)
Auth:       University SSO
Data model: Alert(id, title, body, severity, area, created_at, created_by)
            SafetyCheck(alert_id -> Alert, user_id, status, lat, lng, at)
            User(id, campus_id, name)
Features:   - Push critical alerts that bypass silent mode
            - Ask students to mark themselves safe
            - Show a campus map with safe zones
            - Let security see who needs help
API:        REST
            POST /alerts
            POST /alerts/{id}/check-in
            GET  /alerts/{id}/status
Storage:    PostgreSQL
Tech stack: Swift (iOS critical alerts), Kotlin (Android), Spring Boot
```

---

## Example 275

**Intent:**
app where tattoo artists post flash designs and clients claim them

**Spec:**
```
Type:       Mobile application with backend (creative marketplace)
Auth:       Email login with artist and client roles
Data model: Artist(id, name, studio, city)
            FlashDesign(id, artist_id -> Artist, image_url, size, price, status)
            Claim(id, design_id -> FlashDesign, client_id -> Client, appointment_at, deposit_paid)
            Client(id, name, email)
Features:   - Post flash designs with price and size
            - Browse flash from artists in your city
            - Claim a design with a deposit
            - Remove claimed designs from the feed
API:        REST
            GET  /flash?city={c}
            POST /flash
            POST /flash/{id}/claim
Storage:    PostgreSQL, S3
Tech stack: React Native, NestJS, Stripe
```

---

## Example 276

**Intent:**
Hi, I am a coach of children chess in Ukraine. I need app where children solve puzzles every day and I see results of my group.

**Spec:**
```
Type:       Mobile application with backend (education)
Auth:       Coach email login; children log in with a code given by the coach
Data model: Coach(id, name, email)
            ChessGroup(id, coach_id -> Coach, name)
            Child(id, group_id -> ChessGroup, name, login_code)
            Puzzle(id, fen, solution, rating)
            Attempt(id, child_id -> Child, puzzle_id -> Puzzle, solved, time_s, at)
Features:   - Give children a set of daily puzzles by level
            - Check moves against the solution
            - Show the coach results per child and group
            - Adjust puzzle difficulty by success rate
API:        REST
            GET  /puzzles/daily
            POST /attempts
            GET  /groups/{id}/results
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework, Lichess puzzle database
```

---

## Example 277

**Intent:**
boat sharing club app with fuel log

**Spec:**
```
Type:       Mobile application with backend (shared ownership)
Auth:       Member email login
Data model: Member(id, name, share_pct)
            Boat(id, name, mooring, engine_hours)
            Booking(id, boat_id -> Boat, member_id -> Member, start_at, end_at)
            FuelLog(id, booking_id -> Booking, liters, cost, engine_hours_after)
Features:   - Book the boat fairly by share
            - Log fuel and engine hours after each trip
            - Split costs by usage
            - Show maintenance due by engine hours
API:        REST
            GET  /boats/{id}/bookings
            POST /bookings
            POST /bookings/{id}/fuel
            GET  /costs?month={m}
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 278

**Intent:**
realtime auction app for a charity gala, guests bid from their phones

**Spec:**
```
Type:       Mobile application with backend (live auction)
Auth:       Guest login with table number and phone
Data model: Guest(id, name, phone, table_no)
            Lot(id, title, description, photo_url, start_price, closes_at)
            Bid(id, lot_id -> Lot, guest_id -> Guest, amount, at)
Features:   - Browse auction lots with photos
            - Place bids and see the top bid instantly
            - Notify guests when they are outbid
            - Close lots at a set time and announce winners
            - Collect payment from winners
API:        REST + WebSocket
            GET  /lots
            POST /lots/{id}/bids
            WS   /lots
Storage:    PostgreSQL, Redis
Tech stack: React Native, Node.js, Socket.IO, Stripe
```

---

## Example 279

**Intent:**
vet clinic app, owners see pet records and get vaccine reminders

**Spec:**
```
Type:       Mobile application with backend (veterinary)
Auth:       Owner email login
Data model: Owner(id, name, email)
            Pet(id, owner_id -> Owner, name, species, birth_date)
            Vaccination(id, pet_id -> Pet, vaccine, given_on, due_on)
            Visit(id, pet_id -> Pet, date, reason, notes)
Features:   - Show each pet's medical history
            - Remind owners when a vaccine is due
            - Book appointments
            - Message the clinic
API:        REST
            GET  /pets
            GET  /pets/{id}/history
            POST /appointments
            POST /messages
Storage:    PostgreSQL
Tech stack: Flutter, ASP.NET Core
```

---

## Example 280

**Intent:**
hackathon team finder app

**Spec:**
```
Type:       Mobile application with backend (matching)
Auth:       Sign in with GitHub
Data model: Hacker(id, github_login, skills, looking_for)
            Hackathon(id, name, date)
            Team(id, hackathon_id -> Hackathon, name, needs)
            TeamMember(team_id -> Team, hacker_id -> Hacker)
            JoinRequest(id, team_id -> Team, hacker_id -> Hacker, status)
Features:   - Join a hackathon and list your skills
            - Browse teams that need your skills
            - Request to join a team
            - Let team leads accept members
API:        REST
            GET  /hackathons/{id}/teams
            POST /teams
            POST /teams/{id}/requests
            PATCH /requests/{id}
Storage:    PostgreSQL
Tech stack: React Native, Express, GitHub OAuth
```

---

## Example 281

**Intent:**
mobile app that helps people in my village share one electric car, book it and charge it

**Spec:**
```
Type:       Mobile application with backend (car sharing)
Auth:       Email login approved by the village association
Data model: Member(id, name, email)
            Car(id, name, battery_pct, location, status)
            Booking(id, car_id -> Car, member_id -> Member, start_at, end_at, km_driven)
            ChargeLog(id, car_id -> Car, kwh, at)
Features:   - Book the car for a time slot
            - Show the battery level from the car's API
            - Log kilometers driven per booking
            - Split costs by kilometers at month end
API:        REST
            GET  /cars/{id}
            POST /bookings
            POST /bookings/{id}/finish
            GET  /costs?month={m}
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Smartcar API
```

---

## Example 282

**Intent:**
online bingo night for our seniors center, played on tablets

**Spec:**
```
Type:       Mobile game (multiplayer bingo)
Auth:       Players join with a room code and first name
Data model: Room(id, code, called_numbers, status)
            Player(id, room_id -> Room, name)
            Card(id, player_id -> Player, grid)
Features:   - Generate a random card per player
            - Let the host call numbers that appear on every tablet
            - Auto-mark called numbers in large print
            - Detect a bingo and announce the winner
API:        REST + WebSocket
            POST /rooms
            POST /rooms/{code}/join
            WS   /rooms/{code}
Storage:    Redis
Tech stack: Flutter, Node.js, Socket.IO
```

---

## Example 283

**Intent:**
badminton court sharing app

**Spec:**
```
Type:       Mobile application with backend (sports booking)
Auth:       Phone login with SMS code
Data model: Player(id, name, level)
            CourtSession(id, venue, starts_at, courts, cost_total, organizer_id -> Player)
            SessionPlayer(session_id -> CourtSession, player_id -> Player, paid)
Features:   - Post a court session with total cost
            - Join and split the cost evenly
            - Track who has paid the organizer
            - Rotate doubles pairings fairly
API:        REST
            GET  /sessions
            POST /sessions
            POST /sessions/{id}/join
            PATCH /sessions/{id}/players/{pid}
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 284

**Intent:**
mobile app for a cinema: buy tickets, choose seats, order popcorn to pick up

**Spec:**
```
Type:       Mobile application with backend (ticketing)
Auth:       Email or Apple login
Data model: Film(id, title, rating, runtime)
            Screening(id, film_id -> Film, hall_id -> Hall, starts_at)
            Hall(id, name, seat_map)
            SeatBooking(id, screening_id -> Screening, seat, customer_id, status)
            SnackOrder(id, booking_id -> SeatBooking, items, ready)
Features:   - Show screenings by film and date
            - Pick seats on an interactive seat map
            - Hold seats for 10 minutes during checkout
            - Add snacks to pick up at the counter
            - Show a QR ticket
API:        REST
            GET  /screenings?date={d}
            GET  /screenings/{id}/seats
            POST /bookings
            POST /bookings/{id}/snacks
Storage:    PostgreSQL, Redis (seat holds)
Tech stack: React Native, Spring Boot, Stripe
```

---

## Example 285

**Intent:**
tinder for adopting shelter dogs

**Spec:**
```
Type:       Mobile application with backend (adoption matching)
Auth:       Email or Google login
Data model: Adopter(id, name, home_type, has_kids, other_pets)
            Dog(id, shelter_id -> Shelter, name, age, good_with_kids, energy, photos)
            Shelter(id, name, city)
            Swipe(adopter_id -> Adopter, dog_id -> Dog, liked)
            Inquiry(id, adopter_id -> Adopter, dog_id -> Dog, status)
Features:   - Swipe through adoptable dogs nearby
            - Filter by compatibility with kids and other pets
            - Send an inquiry to the shelter on a like
            - Let shelters manage inquiries
API:        REST
            GET  /dogs/feed
            POST /swipes
            POST /inquiries
            PATCH /inquiries/{id}
Storage:    PostgreSQL
Tech stack: Flutter, NestJS
```

---

## Example 286

**Intent:**
we have 3 food trucks n want customers to order ahead from their phone and get a text when its ready, using square for payments

**Spec:**
```
Type:       Mobile application with backend (order ahead)
Auth:       Phone login with SMS code
Data model: Truck(id, name, today_location)
            MenuItem(id, truck_id -> Truck, name, price, sold_out)
            Order(id, truck_id -> Truck, customer_phone, items, total, square_payment_id, status)
Features:   - Pick a truck and see its menu
            - Pay ahead with Square
            - Show orders on a tablet in the truck
            - Text the customer when the order is ready
API:        REST
            GET  /trucks
            GET  /trucks/{id}/menu
            POST /orders
            PATCH /orders/{id}
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Square Payments SDK, Twilio
```

---

## Example 287

**Intent:**
an app where volunteers in disaster areas register and get assigned tasks

**Spec:**
```
Type:       Mobile application with backend (disaster response)
Auth:       Phone login with SMS code; coordinators verified
Data model: Volunteer(id, name, phone, skills, lat, lng, available)
            Task(id, title, skills_needed, lat, lng, priority, status)
            Assignment(task_id -> Task, volunteer_id -> Volunteer, status)
Features:   - Register with skills like first aid or driving
            - Assign tasks by skills and distance
            - Let volunteers accept tasks and report done
            - Work offline and send updates by SMS fallback
API:        REST
            POST /volunteers
            GET  /tasks/nearby
            POST /tasks/{id}/accept
            PATCH /tasks/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin (Android), Django REST Framework, Twilio SMS
```

---

## Example 288

**Intent:**
friends location sharing app like zenly

**Spec:**
```
Type:       Mobile application with backend (real-time location)
Auth:       Phone login with SMS code
Data model: User(id, name, phone, ghost_mode)
            Friendship(a_id -> User, b_id -> User, status)
            LastLocation(user_id -> User, lat, lng, battery_pct, updated_at)
Features:   - Show friends on a map with battery level
            - Add friends from phone contacts
            - Turn on ghost mode to hide your location
            - Notify when a friend arrives nearby
API:        REST + WebSocket
            POST /locations
            GET  /friends/locations
            POST /friends
            WS   /live
Storage:    Redis (live locations), PostgreSQL
Tech stack: Swift (iOS), Kotlin (Android), Elixir, Phoenix
```

---

## Example 289

**Intent:**
game night scorekeeper synced across phones

**Spec:**
```
Type:       Mobile application with backend (real-time sync)
Auth:       Join a game with a code
Data model: Game(id, code, name, players)
            ScoreEntry(game_id -> Game, player, round, points)
Features:   - Create a game with player names
            - Add scores per round from any phone
            - Show running totals live
            - Save past games
API:        REST + WebSocket
            POST /games
            POST /games/{code}/scores
            WS   /games/{code}
Storage:    Firebase Realtime Database
Tech stack: Flutter, Firebase
```

---

## Example 290

**Intent:**
I'd like an app for my hairdresser salon so clients see my Instagram style portfolio and book, and I can block days off

**Spec:**
```
Type:       Mobile application with backend (appointments)
Auth:       Client phone login; stylist admin login
Data model: Stylist(id, name)
            PortfolioPost(id, stylist_id -> Stylist, image_url, caption)
            Service(id, name, duration_min, price)
            Appointment(id, client_id, service_id -> Service, starts_at, status)
            TimeOff(id, stylist_id -> Stylist, date)
Features:   - Show a photo portfolio of past work
            - Book services in open time slots
            - Block days off and holidays
            - Send reminders and allow rescheduling
API:        REST
            GET  /portfolio
            GET  /slots?date={d}&service={id}
            POST /appointments
            POST /time-off
Storage:    PostgreSQL, S3
Tech stack: Flutter, Supabase
```

---

## Example 291

**Intent:**
walkie talkie for warehouse staff with channels by zone

**Spec:**
```
Type:       Mobile application with backend (push-to-talk)
Auth:       Employee badge number and PIN
Data model: Employee(id, badge_no, name, zone)
            Channel(id, name, zone)
            Transmission(id, channel_id -> Channel, employee_id -> Employee, audio_url, at)
Features:   - Push to talk on a zone channel
            - Switch channels by zone
            - Send an emergency call to all channels
            - Keep 24 hours of transmissions for review
API:        WebSocket + REST
            WS   /channels/{id}
            GET  /channels
            GET  /channels/{id}/transmissions
Storage:    PostgreSQL, S3 (audio)
Tech stack: Kotlin (Android rugged devices), Go, WebRTC
```

---

## Example 292

**Intent:**
shared playlist for my running club

**Spec:**
```
Type:       Mobile application with backend
Auth:       Sign in with Spotify
Data model: Club(id, name)
            Member(id, club_id -> Club, spotify_id)
            PlaylistTrack(club_id -> Club, track_id, added_by -> Member, bpm)
Features:   - Add songs to the club playlist
            - Filter tracks by BPM for tempo runs
            - Sync the playlist to Spotify
API:        REST
            GET  /clubs/{id}/tracks
            POST /clubs/{id}/tracks
            POST /clubs/{id}/sync
Storage:    PostgreSQL
Tech stack: React Native, Express, Spotify Web API
```

---

## Example 293

**Intent:**
mobile app where my employees request vacation and managers approve

**Spec:**
```
Type:       Mobile application with backend (HR)
Auth:       Company SSO (Okta)
Data model: Employee(id, name, manager_id -> Employee, days_left)
            LeaveRequest(id, employee_id -> Employee, start_date, end_date, type, status, comment)
Features:   - Request vacation or sick days
            - Show remaining days
            - Let managers approve or reject
            - Show a team calendar of who is away
API:        REST
            POST /leave-requests
            GET  /me/leave
            PATCH /leave-requests/{id}
            GET  /teams/{id}/calendar
Storage:    PostgreSQL
Tech stack: React Native, NestJS, Okta
```

---

## Example 294

**Intent:**
hi! I'm starting a small boba tea shop and want customers to collect stamps and also order ahead, and I want to send them promos on rainy days lol

**Spec:**
```
Type:       Mobile application with backend (loyalty and ordering)
Auth:       Phone login with SMS code
Data model: Customer(id, phone, name, stamps, birthday)
            Drink(id, name, base_price, toppings)
            Order(id, customer_id -> Customer, items, total, pickup_at, status)
            Promo(id, title, discount_pct, valid_until, trigger)
Features:   - Order drinks ahead with custom sugar and ice levels
            - Earn a stamp per drink
            - Send promo pushes when the weather forecast shows rain
            - Give a free drink on the customer's birthday
API:        REST
            GET  /drinks
            POST /orders
            GET  /me/stamps
            POST /promos
Storage:    PostgreSQL
Tech stack: Flutter, Firebase Cloud Functions, OpenWeatherMap API
```

---

## Example 295

**Intent:**
courier app for documents between law offices in the city

**Spec:**
```
Type:       Mobile application with backend (courier dispatch)
Auth:       Office email login; couriers log in with phone
Data model: Office(id, name, address)
            Courier(id, name, phone, lat, lng, status)
            Job(id, from_office -> Office, to_office -> Office, courier_id -> Courier, urgency, picked_at, delivered_at, signature_url)
Features:   - Request a pickup with urgency level
            - Assign the nearest courier
            - Capture recipient signature on delivery
            - Send proof of delivery to the sender
API:        REST
            POST /jobs
            PATCH /jobs/{id}
            POST /jobs/{id}/proof
            POST /couriers/me/location
Storage:    PostgreSQL
Tech stack: React Native, Express, Google Maps SDK
```

---

## Example 296

**Intent:**
social app for sharing and rating bouldering problems at our gym

**Spec:**
```
Type:       Mobile application with backend (climbing community)
Auth:       Email login
Data model: Climber(id, name)
            Wall(id, name)
            Problem(id, wall_id -> Wall, grade, color, set_on, removed_on)
            Ascent(problem_id -> Problem, climber_id -> Climber, flashed, at)
            ProblemRating(problem_id -> Problem, climber_id -> Climber, stars, suggested_grade)
Features:   - Show current problems by wall and grade
            - Log ascents and flashes
            - Rate problems and suggest grades
            - Show a monthly ascent leaderboard
API:        REST
            GET  /problems
            POST /problems/{id}/ascents
            POST /problems/{id}/ratings
            GET  /leaderboard
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 297

**Intent:**
hey i want an app like nextdoor but for apartment complexes in nigeria, residents post security alerts and pay estate levies

**Spec:**
```
Type:       Mobile application with backend (estate community)
Auth:       Phone login with SMS code; estate admin approves residents
Data model: Estate(id, name, city)
            Resident(id, estate_id -> Estate, name, phone, house_no)
            Alert(id, estate_id -> Estate, resident_id -> Resident, text, at)
            Levy(id, estate_id -> Estate, title, amount, due_date)
            LevyPayment(levy_id -> Levy, resident_id -> Resident, paid_at)
Features:   - Post security alerts to the whole estate
            - Pay estate levies online
            - Show admins who has not paid
            - Issue gate passes for visitors
API:        REST
            POST /alerts
            GET  /levies
            POST /levies/{id}/pay
            POST /gate-passes
Storage:    PostgreSQL
Tech stack: Flutter, NestJS, Paystack
```

---

## Example 298

**Intent:**
app to share ebike batteries among friends lol

**Spec:**
```
Type:       Mobile application with backend (sharing)
Auth:       Sign in with Google
Data model: Friend(id, name)
            Battery(id, owner_id -> Friend, model, charge_pct, holder_id -> Friend)
            Handoff(id, battery_id -> Battery, from_id -> Friend, to_id -> Friend, at)
Features:   - List batteries and who has them now
            - Request a battery from a friend
            - Record handoffs
            - Update charge level manually
API:        REST
            GET  /batteries
            POST /batteries/{id}/request
            POST /handoffs
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase
```

---

## Example 299

**Intent:**
Make a coach booking app for long distance buses in Kenya with M-Pesa payments.

**Spec:**
```
Type:       Mobile application with backend (bus ticketing)
Auth:       Phone login with SMS code
Data model: Route(id, origin, destination)
            Trip(id, route_id -> Route, bus_id, departs_at, fare)
            Seat(trip_id -> Trip, number, status)
            Booking(id, trip_id -> Trip, phone, seat_number, mpesa_receipt, status)
Features:   - Search trips by route and date
            - Pick a seat on the bus layout
            - Pay with M-Pesa STK push
            - Send an SMS ticket
            - Let conductors verify tickets by code
API:        REST
            GET  /trips?from={a}&to={b}&date={d}
            POST /bookings
            POST /mpesa/callback
            GET  /bookings/{id}/verify
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework, Safaricom Daraja API, Africa's Talking SMS
```

---

## Example 300

**Intent:**
lacrosse team app

**Spec:**
```
Type:       Mobile application with backend (sports team)
Auth:       Email login with coach, player and parent roles
Data model: Team(id, name)
            Player(id, team_id -> Team, name, number)
            Event(id, team_id -> Team, type, starts_at, location)
            Rsvp(event_id -> Event, player_id -> Player, status)
            Message(id, team_id -> Team, sender_id, body, at)
Features:   - Show practices and games on a calendar
            - RSVP for each event
            - Team chat with announcements
            - Track goals and assists per player
API:        REST
            GET  /teams/{id}/events
            PUT  /events/{id}/rsvp
            GET  /teams/{id}/messages
            POST /teams/{id}/messages
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 301

**Intent:**
blind date app where you only see the profile after 10 messages

**Spec:**
```
Type:       Mobile application with backend (dating)
Auth:       Phone login with SMS code
Data model: User(id, name, age, city, interests, photo_url)
            Match(id, a_id -> User, b_id -> User, message_count, revealed)
            Message(id, match_id -> Match, sender_id -> User, text, at)
Features:   - Match users by shared interests
            - Hide photos and names in a new chat
            - Reveal profiles after 10 messages from each side
            - Let either user end the chat
API:        REST + WebSocket
            GET  /matches
            POST /matches/{id}/messages
            WS   /chat
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 302

**Intent:**
soil moisture sensors on our farm fields with alerts to my phone and irrigation control

**Spec:**
```
Type:       IoT system (agriculture)
Auth:       Farmer email login
Data model: Field(id, name, crop, area_ha)
            Sensor(id, field_id -> Field, depth_cm, battery)
            Reading(sensor_id -> Sensor, moisture_pct, at)
            Valve(id, field_id -> Field, is_open)
            IrrigationRun(id, valve_id -> Valve, started_at, ended_at)
Features:   - Collect moisture readings over LoRaWAN
            - Show moisture per field on a map
            - Alert when a field is too dry
            - Open and close irrigation valves remotely
            - Schedule irrigation runs
API:        REST
            GET  /fields
            GET  /fields/{id}/readings
            POST /valves/{id}/open
            POST /valves/{id}/close
Storage:    TimescaleDB
Tech stack: LoRaWAN (ChirpStack), Python, FastAPI, Flutter
```

---

## Example 303

**Intent:**
lowkey want an app where my gym friends and i post our PRs and hype each other

**Spec:**
```
Type:       Mobile application with backend (social fitness)
Auth:       Sign in with Apple or Google
Data model: Lifter(id, name)
            Crew(id, name)
            CrewMember(crew_id -> Crew, lifter_id -> Lifter)
            PR(id, lifter_id -> Lifter, lift, weight_kg, reps, video_url, at)
            Hype(pr_id -> PR, lifter_id -> Lifter)
Features:   - Post a PR with an optional video
            - Hype friends' PRs
            - Show a crew feed
            - Chart your PR history per lift
API:        REST
            POST /prs
            GET  /crews/{id}/feed
            POST /prs/{id}/hype
Storage:    PostgreSQL, S3 (videos)
Tech stack: React Native, Supabase
```

---

## Example 304

**Intent:**
app for car mechanics to send repair quotes with photos and customer approves in app

**Spec:**
```
Type:       Mobile application with backend (auto repair)
Auth:       Shop staff email login; customers open quotes via SMS link
Data model: Shop(id, name)
            Customer(id, name, phone)
            Vehicle(id, customer_id -> Customer, make, model, plate)
            RepairOrder(id, vehicle_id -> Vehicle, status)
            QuoteLine(id, order_id -> RepairOrder, description, parts_cost, labor_cost, photo_url, approved)
Features:   - Create a repair order for a vehicle
            - Add quote lines with photos of the problem
            - Let customers approve or decline each line
            - Notify when the car is ready
API:        REST
            POST /orders
            POST /orders/{id}/lines
            POST /lines/{id}/decision
            PATCH /orders/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Twilio
```

---

## Example 305

**Intent:**
cricket scoring app ball by ball with live view

**Spec:**
```
Type:       Mobile application with backend (live scoring)
Auth:       Scorer email login; viewers need no account
Data model: Match(id, team_a, team_b, overs, status)
            Innings(id, match_id -> Match, batting_team)
            Ball(id, innings_id -> Innings, over, ball, batter, bowler, runs, extra, wicket)
Features:   - Record each ball with runs, extras and wickets
            - Calculate scorecard and run rate
            - Show a live scorecard to viewers
            - Undo the last ball
API:        REST + WebSocket
            POST /matches
            POST /innings/{id}/balls
            DELETE /innings/{id}/balls/last
            WS   /matches/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 306

**Intent:**
mobile app for a cleaning products sales rep visiting shops

**Spec:**
```
Type:       Mobile application with backend (sales field app)
Auth:       Rep email login
Data model: Rep(id, name, territory)
            Shop(id, name, address, lat, lng)
            Visit(id, rep_id -> Rep, shop_id -> Shop, at, notes)
            SalesOrder(id, visit_id -> Visit, items, total)
Features:   - Plan visits on a map
            - Check in at a shop with GPS
            - Take orders from the catalog
            - Sync orders to the head office
API:        REST
            GET  /shops
            POST /visits
            POST /visits/{id}/orders
            GET  /products
Storage:    PostgreSQL, SQLite (offline)
Tech stack: Flutter, Spring Boot
```

---

## Example 307

**Intent:**
we need app where parents in our kindergarten in Poland can sign kids out and say who picks them up today

**Spec:**
```
Type:       Mobile application with backend (childcare pickup)
Auth:       Parent email login; teacher accounts
Data model: Parent(id, name, email)
            Child(id, name, group_name)
            AuthorizedPerson(id, child_id -> Child, name, id_photo_url)
            PickupNotice(id, child_id -> Child, person_id -> AuthorizedPerson, date, time)
Features:   - Register people allowed to pick up the child
            - Tell teachers who picks up today and when
            - Show teachers today's pickup list with photos
            - Record the actual pickup time
API:        REST
            POST /children/{id}/authorized
            POST /pickup-notices
            GET  /groups/{name}/pickups/today
            POST /pickups/{id}/done
Storage:    PostgreSQL (EU hosting)
Tech stack: Flutter, Django REST Framework
```

---

## Example 308

**Intent:**
app for my friends to plan a trip together, vote on activities and split costs

**Spec:**
```
Type:       Mobile application with backend (group travel)
Auth:       Email or Google login
Data model: Trip(id, name, destination, start_date, end_date)
            Traveler(id, trip_id -> Trip, user_id)
            ActivityIdea(id, trip_id -> Trip, title, cost, votes)
            Expense(id, trip_id -> Trip, paid_by -> Traveler, amount, description)
Features:   - Create a trip and invite friends
            - Suggest and vote on activities
            - Build a day-by-day itinerary
            - Log expenses and show who owes whom
API:        REST
            POST /trips
            POST /trips/{id}/ideas
            POST /ideas/{id}/vote
            POST /trips/{id}/expenses
            GET  /trips/{id}/balances
Storage:    PostgreSQL
Tech stack: React Native, NestJS
```

---

## Example 309

**Intent:**
real-time bus seat availability for a shuttle between campus and train station

**Spec:**
```
Type:       Mobile application with backend (shuttle)
Auth:       Student SSO
Data model: Shuttle(id, capacity, lat, lng, passengers)
            Departure(id, shuttle_id -> Shuttle, departs_at, from_stop)
            SeatReservation(departure_id -> Departure, student_id, at)
Features:   - Show the next departures and free seats
            - Reserve a seat on a departure
            - Let the driver count boardings
            - Show the shuttle position live
API:        REST + WebSocket
            GET  /departures
            POST /departures/{id}/reserve
            POST /shuttles/{id}/count
            WS   /shuttles/{id}
Storage:    PostgreSQL
Tech stack: Flutter, FastAPI
```

---

## Example 310

**Intent:**
firebase + flutter social app for sharing recipes with friends, with likes and saved collections

**Spec:**
```
Type:       Mobile application with backend (social)
Auth:       Firebase Authentication (Google and email)
Data model: User(id, name, photo_url)
            Recipe(id, author_id -> User, title, ingredients, steps, photo_url, created_at)
            Like(recipe_id -> Recipe, user_id -> User)
            Collection(id, owner_id -> User, name, recipe_ids)
Features:   - Post recipes with photos
            - Follow friends and see their recipes
            - Like recipes
            - Save recipes into named collections
Storage:    Cloud Firestore, Firebase Storage
Tech stack: Flutter, Firebase (Auth, Firestore, Storage)
```

---

## Example 311

**Intent:**
bounty hunter style game where you hunt other players in the city via gps

**Spec:**
```
Type:       Mobile game (location-based, multiplayer)
Auth:       Sign in with Google
Data model: Player(id, name, lat, lng, alive, bounty)
            Hunt(id, area_polygon, starts_at, ends_at)
            Contract(id, hunt_id -> Hunt, hunter_id -> Player, target_id -> Player, status)
Features:   - Assign each player a secret target
            - Show a fuzzy target area that shrinks over time
            - Confirm a tag by scanning the target's QR code
            - Pass the target's contract to the hunter
API:        REST + WebSocket
            POST /hunts/{id}/join
            POST /contracts/{id}/tag
            WS   /hunts/{id}
Storage:    PostgreSQL with PostGIS, Redis
Tech stack: Unity (C#), Node.js
```

---

## Example 312

**Intent:**
help me make app for my kebab shop, delivery only in 3km and they pay cash or card

**Spec:**
```
Type:       Mobile application with backend (food delivery)
Auth:       Phone login with SMS code
Data model: Customer(id, phone, address, lat, lng)
            MenuItem(id, name, price, extras)
            Order(id, customer_id -> Customer, items, total, payment_method, status)
Features:   - Check the address is within 3 km before ordering
            - Show the menu with extras
            - Pay by card or choose cash on delivery
            - Show order status to the customer
API:        REST
            GET  /menu
            POST /delivery-check
            POST /orders
            PATCH /orders/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe
```

---

## Example 313

**Intent:**
Little app so my book club can pick dates when most people are free

**Spec:**
```
Type:       Mobile application with backend (scheduling poll)
Data model: Poll(id, title, options)
            Response(poll_id -> Poll, name, available_options)
Features:   - Propose several dates
            - Let members tick the dates they can make
            - Highlight the best date
            - Share the poll by link
API:        REST
            POST /polls
            GET  /polls/{id}
            POST /polls/{id}/responses
Storage:    SQLite
Tech stack: React Native, Flask
```

---

## Example 314

**Intent:**
app where workers on oil rigs log their safety checks and supervisors sign off

**Spec:**
```
Type:       Mobile application with backend (safety compliance)
Auth:       Employee SSO with supervisor role
Data model: Worker(id, name, crew)
            Checklist(id, name, items_json)
            CheckRun(id, checklist_id -> Checklist, worker_id -> Worker, answers_json, at, signed_off_by)
            Issue(id, run_id -> CheckRun, description, severity)
Features:   - Complete safety checklists on a rugged tablet
            - Work offline on the rig
            - Raise issues from failed items
            - Supervisor sign-off with digital signature
            - Sync logs when connectivity returns
API:        REST
            GET  /checklists
            POST /check-runs
            POST /check-runs/{id}/signoff
Storage:    PostgreSQL, SQLite on device
Tech stack: Kotlin (Android), Spring Boot
```

---

## Example 315

**Intent:**
chat app that auto translates messages between me and my in-laws

**Spec:**
```
Type:       Mobile application with backend (translated messaging)
Auth:       Phone login with SMS code
Data model: User(id, name, phone, language)
            Chat(id, member_ids)
            Message(id, chat_id -> Chat, sender_id -> User, original_text, source_lang, translations_json, at)
Features:   - Send messages in your own language
            - Translate each message into the reader's language
            - Show the original on tap
            - Translate voice messages too
API:        REST + WebSocket
            GET  /chats
            POST /chats/{id}/messages
            WS   /chat
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Google Cloud Translation, Whisper (speech to text)
```

---

## Example 316

**Intent:**
mobile app for refugee families to find free services nearby (food, legal help, doctors)

**Spec:**
```
Type:       Mobile application with backend (service directory)
Auth:       No login for users; NGO staff login to manage listings
Data model: Service(id, name, category, languages, address, lat, lng, hours, phone)
            Organization(id, name)
            Update(id, service_id -> Service, note, at)
Features:   - Show free services nearby by category
            - Show the app in many languages
            - Filter services by language spoken
            - Let NGOs update hours and notes
API:        REST
            GET  /services?lat={lat}&lng={lng}&category={c}
            POST /services
            PATCH /services/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: React Native (i18n), Django REST Framework
```

---

## Example 317

**Intent:**
car pool app for night shift nurses at our hospital

**Spec:**
```
Type:       Mobile application with backend (carpooling)
Auth:       Hospital email login
Data model: Nurse(id, name, home_area, ward)
            Shift(id, nurse_id -> Nurse, starts_at, ends_at)
            CarpoolMatch(id, driver_id -> Nurse, rider_id -> Nurse, shift_date)
Features:   - Enter shifts and home area
            - Match nurses with the same shift times and nearby homes
            - Confirm a carpool for a shift
            - Alert if a driver cancels late
API:        REST
            POST /shifts
            GET  /matches?date={d}
            POST /matches
            DELETE /matches/{id}
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 318

**Intent:**
puzzle game where two players cooperate on separate phones to solve rooms

**Spec:**
```
Type:       Mobile game (co-op multiplayer)
Auth:       Guest play with room code
Data model: Session(id, code, level, state_json)
            Player(id, session_id -> Session, slot)
Features:   - Pair two phones in a session
            - Show each player different clues
            - Sync puzzle state between both phones
            - Unlock the next room when both solve their part
API:        WebSocket
            WS   /sessions/{code}
Storage:    Redis
Tech stack: Godot, Nakama game server
```

---

## Example 319

**Intent:**
app to organize a ultimate frisbee league, teams, spirit scores, standings

**Spec:**
```
Type:       Mobile application with backend (sports league)
Auth:       Captain email login
Data model: Team(id, name, captain_email)
            Game(id, team_a -> Team, team_b -> Team, field, at, score_a, score_b)
            SpiritScore(game_id -> Game, from_team -> Team, to_team -> Team, total)
Features:   - Publish the league schedule
            - Submit game scores
            - Submit spirit of the game scores for the opponent
            - Show standings and spirit rankings
API:        REST
            GET  /games
            POST /games/{id}/score
            POST /games/{id}/spirit
            GET  /standings
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 320

**Intent:**
mobile app for the residents of a retirement home to order meals and book activities, staff see everything

**Spec:**
```
Type:       Mobile application with backend (senior living)
Auth:       Resident login with room number and PIN; staff email login
Data model: Resident(id, name, room, diet)
            Meal(id, date, course, options)
            MealChoice(meal_id -> Meal, resident_id -> Resident, option)
            Activity(id, title, at, capacity)
            ActivitySignup(activity_id -> Activity, resident_id -> Resident)
Features:   - Choose meals for the next day with large buttons
            - Book activities like bingo or excursions
            - Respect each resident's diet
            - Show staff kitchen counts and activity lists
API:        REST
            GET  /meals?date={d}
            POST /meals/{id}/choice
            GET  /activities
            POST /activities/{id}/signup
Storage:    PostgreSQL
Tech stack: Flutter, Laravel
```

---

## Example 321

**Intent:**
dashcam footage sharing for car accidents witnesses

**Spec:**
```
Type:       Mobile application with backend (evidence sharing)
Auth:       Email login
Data model: Driver(id, name, email)
            Clip(id, driver_id -> Driver, video_url, lat, lng, recorded_at)
            WitnessRequest(id, requester_id -> Driver, lat, lng, occurred_at, description)
            ClipShare(request_id -> WitnessRequest, clip_id -> Clip)
Features:   - Post a request for witnesses to an accident at a place and time
            - Notify drivers whose app recorded near that place and time
            - Share dashcam clips with the requester
            - Blur license plates before sharing
API:        REST
            POST /requests
            GET  /requests/nearby
            POST /requests/{id}/clips
Storage:    PostgreSQL with PostGIS, S3 (video)
Tech stack: Kotlin (Android), Go, OpenCV
```

---

## Example 322

**Intent:**
a app for my small gym where trainers post workouts of the day and members log results

**Spec:**
```
Type:       Mobile application with backend (gym community)
Auth:       Member email login
Data model: Member(id, name)
            Wod(id, date, title, description)
            WodResult(wod_id -> Wod, member_id -> Member, score, rx, notes)
Features:   - Post the workout of the day
            - Log results with Rx or scaled
            - Show a daily results board
            - Comment on results
API:        REST
            GET  /wods/today
            POST /wods
            POST /wods/{id}/results
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 323

**Intent:**
ok i wanna make a skateboard spot app, people pin spots, rate them, post clips

**Spec:**
```
Type:       Mobile application with backend (community map)
Auth:       Email or Google login
Data model: Skater(id, name)
            Spot(id, name, type, lat, lng, bust_level)
            SpotRating(spot_id -> Spot, skater_id -> Skater, stars)
            Clip(id, spot_id -> Spot, skater_id -> Skater, video_url, at)
Features:   - Pin skate spots on a map with a type
            - Rate spots and note security risk
            - Upload trick clips to a spot
            - Browse top spots in a city
API:        REST
            GET  /spots?bbox={b}
            POST /spots
            POST /spots/{id}/ratings
            POST /spots/{id}/clips
Storage:    PostgreSQL with PostGIS, S3
Tech stack: React Native, NestJS
```

---

## Example 324

**Intent:**
surf lesson booking

**Spec:**
```
Type:       Mobile application with backend (lesson booking)
Auth:       Email login
Data model: Instructor(id, name, beach)
            SurfLesson(id, instructor_id -> Instructor, starts_at, level, spots)
            Booking(lesson_id -> SurfLesson, student_name, email, board_size)
Features:   - Show lessons by beach and level
            - Book a spot with board size
            - Cancel lessons when waves are unsafe
            - Notify booked students of cancellations
API:        REST
            GET  /lessons
            POST /lessons/{id}/bookings
            POST /lessons/{id}/cancel
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 325

**Intent:**
app to rent out my driveway as parking near the stadium on game days

**Spec:**
```
Type:       Mobile application with backend (parking marketplace)
Auth:       Email login for hosts and drivers
Data model: Host(id, name, payout_account)
            Driveway(id, host_id -> Host, address, lat, lng, spaces, price)
            EventDay(id, venue, date)
            Reservation(id, driveway_id -> Driveway, event_day_id -> EventDay, driver_email, plate, paid)
Features:   - List a driveway with spaces and price
            - Show driveways near the stadium for a game
            - Reserve and pay ahead
            - Show the host the expected plates
API:        REST
            GET  /driveways?event={id}
            POST /driveways
            POST /reservations
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Express, Stripe Connect
```

---

## Example 326

**Intent:**
My grandson said I should ask here. I sell eggs from my chickens to about 30 neighbours. I would like them to order on their phone and I see who wants how many each week.

**Spec:**
```
Type:       Mobile application with backend (simple ordering)
Auth:       Neighbours log in with phone number and SMS code
Data model: Neighbour(id, name, phone)
            WeekStock(week, eggs_available)
            EggOrder(id, neighbour_id -> Neighbour, week, dozens, picked_up)
Features:   - Show how many eggs are available this week
            - Let neighbours order by the dozen
            - Show the seller a simple weekly list
            - Mark orders as picked up and paid
API:        REST
            GET  /weeks/current
            POST /orders
            GET  /orders?week={w}
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase
```

---

## Example 327

**Intent:**
friendship app for new moms to meet nearby

**Spec:**
```
Type:       Mobile application with backend (social matching)
Auth:       Phone login with SMS code
Data model: Mom(id, name, baby_age_months, lat, lng, interests)
            Wave(from_id -> Mom, to_id -> Mom)
            Connection(id, a_id -> Mom, b_id -> Mom)
            Message(id, connection_id -> Connection, sender_id -> Mom, text, at)
Features:   - Show moms nearby with babies of similar age
            - Wave to start a connection
            - Chat after both wave
            - Suggest local baby-friendly cafes to meet
API:        REST
            GET  /moms/nearby
            POST /waves
            GET  /connections
            POST /connections/{id}/messages
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Node.js
```

---

## Example 328

**Intent:**
rideshare for rural doctor visits

**Spec:**
```
Type:       Mobile application with backend (community transport)
Auth:       Phone login; volunteer drivers checked by coordinator
Data model: Patient(id, name, phone, address)
            Driver(id, name, phone, approved)
            Appointment(id, patient_id -> Patient, clinic, at)
            RideOffer(id, appointment_id -> Appointment, driver_id -> Driver, status)
Features:   - Let patients request a ride to an appointment
            - Notify volunteer drivers
            - Let a driver claim a ride
            - Remind both the day before
            - Log mileage for reimbursement
API:        REST
            POST /appointments
            GET  /rides/open
            POST /rides/{id}/claim
            POST /rides/{id}/mileage
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework, Twilio
```

---

## Example 329

**Intent:**
make me a kotlin android app + ktor server for my cycling club's weekend rides with gpx routes

**Spec:**
```
Type:       Mobile application with backend (club rides)
Auth:       Email + password with JWT
Data model: Cyclist(id, name, email)
            Ride(id, title, date, start_point, gpx_url, pace_group)
            RideSignup(ride_id -> Ride, cyclist_id -> Cyclist)
Features:   - Publish weekend rides with GPX routes
            - Show the route on a map
            - Sign up by pace group
            - Notify if the ride is cancelled for weather
API:        REST
            GET  /rides
            POST /rides
            POST /rides/{id}/signups
            GET  /rides/{id}/gpx
Storage:    PostgreSQL, S3 (GPX files)
Tech stack: Kotlin (Jetpack Compose), Ktor, Exposed ORM, osmdroid
```

---

## Example 330

**Intent:**
app that lets fans vote on the setlist before a concert

**Spec:**
```
Type:       Mobile application with backend (fan voting)
Auth:       Email or Google login
Data model: Show(id, artist, venue, date)
            Song(id, artist, title)
            SetlistVote(show_id -> Show, song_id -> Song, user_id)
            Fan(id, name)
Features:   - List upcoming shows
            - Vote for up to 5 songs per show
            - Show live vote rankings
            - Let the band lock the setlist
API:        REST
            GET  /shows
            POST /shows/{id}/votes
            GET  /shows/{id}/rankings
            POST /shows/{id}/lock
Storage:    PostgreSQL
Tech stack: React Native, NestJS
```

---

## Example 331

**Intent:**
tool for my HVAC technicians on the road, see jobs, customer history, take payment on site

**Spec:**
```
Type:       Mobile application with backend (field service)
Auth:       Technician email login
Data model: Technician(id, name)
            Customer(id, name, address, phone)
            Equipment(id, customer_id -> Customer, type, model, installed_on)
            ServiceJob(id, customer_id -> Customer, technician_id -> Technician, scheduled_at, notes, status, amount)
Features:   - Show assigned jobs with directions
            - Show the customer's equipment and service history
            - Record work done and parts used
            - Take card payment on site
API:        REST
            GET  /jobs?assigned=me
            GET  /customers/{id}/history
            PATCH /jobs/{id}
            POST /jobs/{id}/payment
Storage:    PostgreSQL
Tech stack: React Native, Rails API, Stripe Terminal
```

---

## Example 332

**Intent:**
ppl in my town wanna share rides to the airport, can u build it

**Spec:**
```
Type:       Mobile application with backend (ride sharing)
Auth:       Phone login with SMS code
Data model: Rider(id, name, phone)
            AirportTrip(id, creator_id -> Rider, airport, departure_at, seats, direction)
            TripJoin(trip_id -> AirportTrip, rider_id -> Rider)
Features:   - Post a trip to or from the airport
            - Join trips with free seats
            - Split the taxi or parking cost
            - Chat with trip members
API:        REST
            GET  /trips
            POST /trips
            POST /trips/{id}/join
            GET  /trips/{id}/messages
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 333

**Intent:**
coloring game where kids color the same picture together online

**Spec:**
```
Type:       Mobile game (kids, co-op)
Auth:       Parent-created kid profiles, join by room code
Data model: Room(id, code, picture_id)
            Fill(room_id -> Room, region_id, color, by_player)
Features:   - Pick a picture and invite a friend
            - Tap regions to fill with color
            - Sync fills instantly
            - Save finished pictures to the parent's gallery
API:        WebSocket
            WS   /rooms/{code}
Storage:    Redis
Tech stack: Flutter, Firebase Realtime Database
```

---

## Example 334

**Intent:**
Gardening app where neighbors share surplus seeds

**Spec:**
```
Type:       Mobile application with backend (sharing)
Auth:       Email login
Data model: Gardener(id, name, area)
            SeedPacket(id, owner_id -> Gardener, plant, variety, quantity)
            SeedRequest(id, packet_id -> SeedPacket, requester_id -> Gardener, status)
Features:   - List seeds you have extra
            - Request seeds from neighbors
            - Arrange pickup in chat
            - Show planting seasons per plant
API:        REST
            GET  /seeds
            POST /seeds
            POST /seeds/{id}/requests
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 335

**Intent:**
smart parking sensor system with an app showing free spots in our downtown garage

**Spec:**
```
Type:       IoT system (smart parking)
Auth:       No login for drivers; operator admin login
Data model: Garage(id, name, address)
            Level(id, garage_id -> Garage, name)
            Bay(id, level_id -> Level, number, occupied, updated_at)
Features:   - Read occupancy from ultrasonic sensors in each bay
            - Show free spots per level in the app
            - Guide drivers to the nearest free bay
            - Show occupancy history to the operator
API:        REST + WebSocket
            GET  /garages/{id}/levels
            POST /bays/{id}/state
            WS   /garages/{id}
Storage:    PostgreSQL, Redis
Tech stack: ESP32 sensors, MQTT, Go, React Native
```

---

## Example 336

**Intent:**
anonymous mental health peer support chat for students

**Spec:**
```
Type:       Mobile application with backend (peer support)
Auth:       University email verification; anonymous display names
Data model: Student(id, email_hash, alias)
            Listener(id, student_id -> Student, trained)
            Session(id, student_id -> Student, listener_id -> Listener, started_at, ended_at)
            Message(id, session_id -> Session, sender_alias, text, at)
Features:   - Connect a student to an available trained listener
            - Chat anonymously
            - Detect crisis keywords and show hotline numbers
            - Let users rate sessions
API:        REST + WebSocket
            POST /sessions
            POST /listeners/available
            WS   /sessions/{id}
Storage:    PostgreSQL (encrypted)
Tech stack: Flutter, Node.js
```

---

## Example 337

**Intent:**
need a app for my taekwondo school, belts progress, class attendance and tournament signups

**Spec:**
```
Type:       Mobile application with backend (martial arts school)
Auth:       Email login with student, parent and instructor roles
Data model: Student(id, name, belt, parent_id)
            Attendance(student_id -> Student, class_date)
            BeltTest(id, student_id -> Student, from_belt, to_belt, passed, date)
            Tournament(id, name, date, fee)
            TournamentEntry(tournament_id -> Tournament, student_id -> Student, division)
Features:   - Track attendance toward the next belt test
            - Record belt test results
            - Show each student's progress
            - Register for tournaments and pay fees
API:        REST
            POST /attendance
            GET  /students/{id}/progress
            POST /belt-tests
            POST /tournaments/{id}/entries
Storage:    PostgreSQL
Tech stack: React Native, Express, Stripe
```

---

## Example 338

**Intent:**
radio station app with live stream and song requests

**Spec:**
```
Type:       Mobile application with backend (streaming radio)
Auth:       Optional login to send requests
Data model: Listener(id, name)
            SongRequest(id, listener_id -> Listener, song, message, status, at)
            NowPlaying(title, artist, started_at)
Features:   - Play the live audio stream in the background
            - Show the current song
            - Send song requests with a message
            - Let the DJ accept requests
API:        REST
            GET  /now-playing
            POST /requests
            GET  /requests
            PATCH /requests/{id}
Storage:    PostgreSQL
Tech stack: Flutter (just_audio), Express, Icecast
```

---

## Example 339

**Intent:**
i want a mobile app for my hostel guests to meet each other and join activities like pub crawl or walking tour

**Spec:**
```
Type:       Mobile application with backend (guest community)
Auth:       Guest login with booking reference
Data model: Guest(id, name, country, check_in, check_out)
            Activity(id, title, at, meeting_point, cost)
            ActivityJoin(activity_id -> Activity, guest_id -> Guest)
            Post(id, guest_id -> Guest, text, at)
Features:   - See who is staying at the hostel now
            - Join hostel activities
            - Post in a guest wall
            - Expire access at check-out
API:        REST
            GET  /guests/current
            GET  /activities
            POST /activities/{id}/join
            POST /posts
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 340

**Intent:**
app for my fleet of rental bikes in a tourist town

**Spec:**
```
Type:       Mobile application with backend (bike rental)
Auth:       Email login with card on file
Data model: Bike(id, type, size, status, smart_lock_id)
            Rental(id, bike_id -> Bike, customer_id, started_at, ended_at, cost)
            Route(id, name, gpx_url, difficulty)
Features:   - Reserve a bike type and size
            - Unlock with the app via Bluetooth smart lock
            - Suggest scenic routes
            - Charge per hour
API:        REST
            GET  /bikes/available
            POST /rentals
            POST /rentals/{id}/end
            GET  /routes
Storage:    PostgreSQL
Tech stack: React Native (BLE), NestJS, Stripe
```

---

## Example 341

**Intent:**
bingo for road trips, kids spot things and race each other on separate phones

**Spec:**
```
Type:       Mobile game (multiplayer, family)
Auth:       Join with a family code
Data model: Game(id, code, card_items)
            Player(id, game_id -> Game, name)
            Spot(player_id -> Player, item, at)
Features:   - Generate a road trip bingo card per player
            - Tap items as you spot them
            - Sync spotted items between phones
            - Announce the winner
API:        WebSocket + REST
            POST /games
            POST /games/{code}/join
            WS   /games/{code}
Storage:    Firebase Realtime Database
Tech stack: Flutter, Firebase
```

---

## Example 342

**Intent:**
Hey! Building an MVP: a marketplace where college students offer services like haircuts, tutoring, photography, to other students on campus. Need profiles, booking, payments, reviews. Using React Native + Supabase.

**Spec:**
```
Type:       Mobile application with backend (student services marketplace)
Auth:       Supabase Auth with university email verification
Data model: Student(id, name, university)
            Offering(id, provider_id -> Student, category, title, price, description)
            Booking(id, offering_id -> Offering, client_id -> Student, at, status)
            Review(booking_id -> Booking, stars, text)
Features:   - Create a service offering with price
            - Browse offerings by category on your campus
            - Book and pay in the app
            - Review after the service
Storage:    Supabase PostgreSQL
Tech stack: React Native (Expo), Supabase (Auth, Database, Storage), Stripe Connect
```

---

## Example 343

**Intent:**
app for my family to track the dog's walks and feeding so we dont double feed

**Spec:**
```
Type:       Mobile application with backend (shared household)
Auth:       Join family with an invite code
Data model: Family(id, code)
            Pet(id, family_id -> Family, name)
            CareEvent(id, pet_id -> Pet, type, by_name, at)
Features:   - Log a feeding or walk with one tap
            - Show the last feeding time on the home screen
            - Notify the family when the dog is fed
            - Warn before logging a second meal too soon
API:        REST
            GET  /pets/{id}/events
            POST /pets/{id}/events
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase
```

---

## Example 344

**Intent:**
delivery app for alcohol with age check at the door

**Spec:**
```
Type:       Mobile application with backend (regulated delivery)
Auth:       Email login with age verification at sign-up
Data model: Customer(id, name, birth_date, id_verified)
            Product(id, name, abv, price)
            Order(id, customer_id -> Customer, items, total, status)
            DoorCheck(order_id -> Order, id_scanned, passed, at)
Features:   - Verify age with ID scan at sign-up
            - Order drinks for delivery
            - Require the courier to scan ID at the door
            - Return the order if the check fails
API:        REST
            POST /verify-id
            POST /orders
            POST /orders/{id}/door-check
Storage:    PostgreSQL
Tech stack: React Native, NestJS, Onfido
```

---

## Example 345

**Intent:**
mobile app for our kayak rental with waivers and a fleet board

**Spec:**
```
Type:       Mobile application with backend (rental operations)
Auth:       Staff PIN login; customers sign waivers without account
Data model: Kayak(id, number, type, status)
            Waiver(id, name, email, signature_url, signed_at)
            Rental(id, kayak_id -> Kayak, waiver_id -> Waiver, out_at, back_at)
Features:   - Let customers sign waivers on a tablet
            - Check kayaks out and in
            - Show which kayaks are out and overdue
            - Email a receipt
API:        REST
            POST /waivers
            POST /rentals
            POST /rentals/{id}/return
            GET  /fleet
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 346

**Intent:**
My English not so good. I have small taxi boat in Greece, tourist want book a trip to the islands, I want app for book and pay.

**Spec:**
```
Type:       Mobile application with backend (boat trip booking)
Auth:       Email or Google login
Data model: Boat(id, name, seats)
            BoatTrip(id, boat_id -> Boat, destination, departs_at, price, seats_left)
            Booking(id, trip_id -> BoatTrip, name, email, people, paid)
Features:   - Show trips to islands by day
            - Book seats and pay online
            - Send a confirmation with meeting point
            - Cancel trips in bad weather and refund
API:        REST
            GET  /trips?date={d}
            POST /bookings
            POST /trips/{id}/cancel
Storage:    PostgreSQL
Tech stack: Flutter (Greek and English), Node.js, Stripe
```

---

## Example 347

**Intent:**
neighborhood tool to organize street cleanup days

**Spec:**
```
Type:       Mobile application with backend (community events)
Auth:       Email login
Data model: Volunteer(id, name)
            Cleanup(id, area, date, meeting_point, organizer_id -> Volunteer)
            Signup(cleanup_id -> Cleanup, volunteer_id -> Volunteer)
            Haul(cleanup_id -> Cleanup, bags, photo_url)
Features:   - Post cleanup events on a map
            - Sign up to join
            - Record bags collected with photos
            - Show total impact per neighborhood
API:        REST
            GET  /cleanups
            POST /cleanups
            POST /cleanups/{id}/signups
            POST /cleanups/{id}/haul
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 348

**Intent:**
social trivia app where questions come from what your friends answered about themselves

**Spec:**
```
Type:       Mobile game (social quiz)
Auth:       Sign in with Apple or Google
Data model: Player(id, name)
            SelfAnswer(player_id -> Player, question_id -> Prompt, answer)
            Prompt(id, text)
            Guess(id, guesser_id -> Player, subject_id -> Player, question_id -> Prompt, guess, correct)
Features:   - Answer fun prompts about yourself
            - Guess how friends answered
            - Score points for correct guesses
            - Show who knows whom best
API:        REST
            GET  /prompts
            POST /self-answers
            GET  /quiz/{friend_id}
            POST /guesses
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 349

**Intent:**
app for my pizza place drivers to see orders and directions, kitchen marks ready

**Spec:**
```
Type:       Mobile application with backend (driver dispatch)
Auth:       Driver PIN login
Data model: Driver(id, name, pin_hash, status)
            DeliveryOrder(id, address, lat, lng, ready_at, driver_id -> Driver, delivered_at)
Features:   - Show ready orders waiting for a driver
            - Assign two nearby orders to one run
            - Open directions in Google Maps
            - Mark orders delivered and return to store
API:        REST
            GET  /orders/ready
            POST /runs
            PATCH /orders/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 350

**Intent:**
bday gift pooling app for coworkers

**Spec:**
```
Type:       Mobile application with backend (group payments)
Auth:       Company email login
Data model: Pool(id, recipient_name, organizer_id, goal, deadline)
            Contribution(pool_id -> Pool, contributor_email, amount, paid_at)
            Card(pool_id -> Pool, author, message)
Features:   - Start a gift pool for a coworker
            - Let colleagues chip in by card
            - Collect messages for a shared card
            - Hide the pool from the recipient
API:        REST
            POST /pools
            POST /pools/{id}/contributions
            POST /pools/{id}/messages
Storage:    PostgreSQL
Tech stack: React Native, NestJS, Stripe
```

---

## Example 351

**Intent:**
transit app for wheelchair users showing elevators working at metro stations

**Spec:**
```
Type:       Mobile application with backend (accessibility)
Auth:       Optional login to report
Data model: Station(id, name, line)
            Elevator(id, station_id -> Station, location, status, updated_at)
            ElevatorReport(id, elevator_id -> Elevator, status, at)
Features:   - Show elevator status for each station
            - Plan step-free routes avoiding broken elevators
            - Let users report outages
            - Import official status from the transit API
API:        REST
            GET  /stations
            GET  /routes/step-free?from={a}&to={b}
            POST /elevators/{id}/reports
Storage:    PostgreSQL
Tech stack: React Native, FastAPI
```

---

## Example 352

**Intent:**
we need an app so parents at our swim club can volunteer for timing at meets

**Spec:**
```
Type:       Mobile application with backend (volunteer scheduling)
Auth:       Parent email login
Data model: Meet(id, name, date, venue)
            Role(id, meet_id -> Meet, name, session, slots)
            VolunteerSignup(role_id -> Role, parent_id -> Parent)
            Parent(id, name, email, hours_owed)
Features:   - Post meet volunteer roles by session
            - Sign up for roles
            - Track required hours per family
            - Remind volunteers before the meet
API:        REST
            GET  /meets/{id}/roles
            POST /roles/{id}/signups
            GET  /me/hours
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 353

**Intent:**
snow day closure alerts for schools in our district

**Spec:**
```
Type:       Mobile application with backend (notifications)
Auth:       Parents subscribe without account; district staff login
Data model: School(id, name)
            Closure(id, school_id -> School, date, type, message)
            Subscription(device_token, school_id -> School)
Features:   - Subscribe to one or more schools
            - Post closures and delays
            - Push alerts immediately
            - Show closure history
API:        REST
            POST /subscriptions
            POST /closures
            GET  /schools/{id}/closures
Storage:    PostgreSQL
Tech stack: Flutter, Firebase Cloud Messaging, Express
```

---

## Example 354

**Intent:**
whats needed to build an app for my yacht club, berth booking and guest moorings

**Spec:**
```
Type:       Mobile application with backend (marina)
Auth:       Member email login; visiting sailors book as guests
Data model: Berth(id, pontoon, number, length_m)
            BerthBooking(id, berth_id -> Berth, boat_name, length_m, arrive, depart, guest_email)
            Member(id, name, berth_id -> Berth)
Features:   - Let members mark their berth free while away
            - Let visiting boats book free berths by length
            - Charge nightly mooring fees
            - Show the harbor master arrivals for today
API:        REST
            GET  /berths/available?length={l}&from={d}&to={d}
            POST /bookings
            POST /berths/{id}/release
Storage:    PostgreSQL
Tech stack: React Native, Django REST Framework, Stripe
```

---

## Example 355

**Intent:**
robot vacuum companion app with cloud maps

**Spec:**
```
Type:       IoT system (with mobile companion app)
Auth:       Email login
Data model: User(id, email)
            Robot(id, owner_id -> User, serial, battery_pct, status)
            FloorMap(id, robot_id -> Robot, image_url, rooms_json)
            CleanJob(id, robot_id -> Robot, rooms, started_at, ended_at, area_m2)
Features:   - Pair the robot over Wi-Fi
            - Show the cleaned floor map
            - Clean selected rooms on demand
            - Schedule cleanings
            - Share control with household members
API:        REST
            GET  /robots
            POST /robots/{id}/jobs
            GET  /robots/{id}/map
            POST /robots/{id}/schedules
Storage:    PostgreSQL, S3 (maps)
Tech stack: Flutter, AWS IoT Core, Node.js
```

---

## Example 356

**Intent:**
comic swap meet app

**Spec:**
```
Type:       Mobile application with backend (collectors marketplace)
Auth:       Email login
Data model: Collector(id, name, city)
            Comic(id, owner_id -> Collector, title, issue, grade, for_trade)
            TradeRequest(id, from_id -> Collector, to_id -> Collector, offered, wanted, status)
Features:   - Catalog your comics with condition grade
            - Mark comics for trade
            - Find collectors who have your want list
            - Send trade requests
API:        REST
            POST /comics
            GET  /comics/search
            POST /trades
            PATCH /trades/{id}
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 357

**Intent:**
i need a app that my security guards use on patrol, scan checkpoint tags and report incidents

**Spec:**
```
Type:       Mobile application with backend (guard tour)
Auth:       Guard login with ID and PIN; supervisor web login
Data model: Guard(id, name, pin_hash)
            Site(id, name)
            Checkpoint(id, site_id -> Site, nfc_tag, name)
            Scan(id, guard_id -> Guard, checkpoint_id -> Checkpoint, at, lat, lng)
            IncidentReport(id, guard_id -> Guard, site_id -> Site, text, photo_url, at)
Features:   - Scan NFC tags at each checkpoint
            - Alert the supervisor when a patrol round is missed
            - Report incidents with photos
            - Send a panic alert with location
API:        REST
            POST /scans
            POST /incidents
            POST /panic
            GET  /sites/{id}/rounds
Storage:    PostgreSQL
Tech stack: Kotlin (Android NFC), Spring Boot
```

---

## Example 358

**Intent:**
carpooling for teens to sports practice, but parents drive

**Spec:**
```
Type:       Mobile application with backend (parent carpool)
Auth:       Parent email login, team invite
Data model: Parent(id, name, phone, seats)
            Athlete(id, parent_id -> Parent, name)
            Practice(id, team, at, location)
            DriveSlot(practice_id -> Practice, driver_id -> Parent, direction, riders)
Features:   - Show practices for the team
            - Volunteer to drive to or from a practice
            - Assign riders to drivers
            - Notify parents of their child's ride
API:        REST
            GET  /practices
            POST /practices/{id}/drives
            PUT  /drives/{id}/riders
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 359

**Intent:**
spin the wheel prize game for my shop customers once per visit

**Spec:**
```
Type:       Mobile application with backend (loyalty game)
Auth:       Phone login with SMS code
Data model: Customer(id, phone)
            Visit(id, customer_id -> Customer, store_code, at)
            Prize(id, name, probability, stock)
            Win(id, customer_id -> Customer, prize_id -> Prize, redeemed)
Features:   - Scan the in-store QR to unlock one spin per visit
            - Pick prizes by weighted chance on the server
            - Show won coupons
            - Redeem coupons at checkout
API:        REST
            POST /visits
            POST /spins
            GET  /me/wins
            POST /wins/{id}/redeem
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 360

**Intent:**
Social app for hikers to post trail conditions like mud, snow, fallen trees.

**Spec:**
```
Type:       Mobile application with backend (crowdsourced)
Auth:       Email or Google login
Data model: Trail(id, name, region, geometry)
            ConditionReport(id, trail_id -> Trail, user_id, condition, note, photo_url, at)
Features:   - Search trails by region
            - Post a trail condition report with photo
            - Show the latest conditions per trail
            - Follow trails and get updates
API:        REST
            GET  /trails
            GET  /trails/{id}/reports
            POST /trails/{id}/reports
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Django REST Framework
```

---

## Example 361

**Intent:**
make an app like venmo but just for my friend group splitting stuff, no real money moves, just tracking

**Spec:**
```
Type:       Mobile application with backend (IOU tracking)
Auth:       Sign in with Google
Data model: Friend(id, name)
            Iou(id, from_id -> Friend, to_id -> Friend, amount, note, at, settled)
Features:   - Log who paid for what
            - Show net balances between friends
            - Mark debts as settled
            - Notify friends of new IOUs
API:        REST
            POST /ious
            GET  /balances
            POST /ious/{id}/settle
Storage:    Cloud Firestore
Tech stack: React Native, Firebase
```

---

## Example 362

**Intent:**
app that matches truck drivers with loads to carry

**Spec:**
```
Type:       Mobile application with backend (freight marketplace)
Auth:       Email login with carrier and shipper roles, verified DOT number
Data model: Shipper(id, company)
            Carrier(id, company, dot_number, truck_type)
            Load(id, shipper_id -> Shipper, origin, destination, pickup_date, weight_kg, rate, status)
            LoadBid(load_id -> Load, carrier_id -> Carrier, amount)
Features:   - Post loads with route, weight and rate
            - Search loads by lane and truck type
            - Bid on or book a load
            - Share live tracking with the shipper
            - Upload proof of delivery
API:        REST
            GET  /loads?origin={o}&dest={d}
            POST /loads
            POST /loads/{id}/bids
            POST /loads/{id}/pod
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Go, Google Maps SDK
```

---

## Example 363

**Intent:**
meetup for people learning to code

**Spec:**
```
Type:       Mobile application with backend (community)
Auth:       Sign in with GitHub
Data model: Coder(id, github_login, languages, city)
            StudySession(id, host_id -> Coder, topic, place, at)
            Join(session_id -> StudySession, coder_id -> Coder)
Features:   - Post study sessions by topic
            - Join sessions in your city
            - Show members' GitHub activity
            - Pair beginners with mentors
API:        REST
            GET  /sessions
            POST /sessions
            POST /sessions/{id}/join
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 364

**Intent:**
car wash membership with license plate recognition at the gate

**Spec:**
```
Type:       Mobile application with backend (subscription, IoT)
Auth:       Email login with card on file
Data model: Member(id, email, plan)
            Vehicle(id, member_id -> Member, plate)
            WashVisit(id, vehicle_id -> Vehicle, at, site)
Features:   - Subscribe to a monthly unlimited plan
            - Register plates for your cars
            - Open the gate when the camera reads a member plate
            - Show wash history
API:        REST
            POST /subscriptions
            POST /vehicles
            POST /gates/{id}/plate-read
            GET  /me/visits
Storage:    PostgreSQL
Tech stack: React Native, Python, FastAPI, OpenALPR, Stripe Billing
```

---

## Example 365

**Intent:**
app where kids league coaches post lineups and parents see playing time

**Spec:**
```
Type:       Mobile application with backend (youth sports)
Auth:       Coach and parent email login
Data model: Team(id, name)
            Kid(id, team_id -> Team, name, parent_id)
            Game(id, team_id -> Team, at)
            Lineup(game_id -> Game, kid_id -> Kid, position, minutes)
Features:   - Build a lineup for each game
            - Track minutes per kid
            - Show parents their kid's playing time
            - Warn the coach about unequal playing time
API:        REST
            POST /games/{id}/lineup
            GET  /kids/{id}/minutes
            GET  /teams/{id}/fairness
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 366

**Intent:**
gym check-in with nfc phones

**Spec:**
```
Type:       Mobile application with backend (access control)
Auth:       Member email login
Data model: Member(id, email, status)
            Entry(id, member_id -> Member, door_id, at)
Features:   - Tap the phone on the door reader to enter
            - Deny entry for expired memberships
            - Log entries
            - Show peak times
API:        REST
            POST /entries
            GET  /me/entries
Storage:    PostgreSQL
Tech stack: Kotlin (Android HCE), Swift (iOS Wallet pass), Express
```

---

## Example 367

**Intent:**
im a nanny agency owner. families need to request nannies for dates, nannies accept jobs, i see everything and send invoices. please help

**Spec:**
```
Type:       Mobile application with backend (staffing agency)
Auth:       Email login with family, nanny and agency admin roles
Data model: Family(id, name, address)
            Nanny(id, name, skills, hourly_rate)
            JobRequest(id, family_id -> Family, date, start_time, hours, kids, status, nanny_id -> Nanny)
            Invoice(id, family_id -> Family, period, total, paid)
Features:   - Let families request a nanny for a date
            - Offer jobs to matching nannies
            - Let nannies accept and log hours
            - Show the agency all jobs
            - Generate monthly invoices
API:        REST
            POST /jobs
            GET  /nannies/me/offers
            POST /jobs/{id}/accept
            POST /jobs/{id}/hours
            GET  /invoices
Storage:    PostgreSQL
Tech stack: Flutter, Laravel, Stripe
```

---

## Example 368

**Intent:**
tap game where whole school competes by class, live scoreboard

**Spec:**
```
Type:       Mobile game (mass multiplayer, casual)
Auth:       Join with school code and class name
Data model: School(id, code)
            ClassTeam(id, school_id -> School, name, taps)
            Player(id, class_id -> ClassTeam, nickname)
Features:   - Tap as fast as you can for your class
            - Batch taps every second to the server
            - Show a live class scoreboard
            - Reset the competition each week
API:        REST + WebSocket
            POST /join
            WS   /schools/{code}
Storage:    Redis
Tech stack: Flutter, Go
```

---

## Example 369

**Intent:**
ugh my building's package room is chaos. app where front desk logs packages and tenants get a notif + pickup code

**Spec:**
```
Type:       Mobile application with backend (package management)
Auth:       Tenant email login; front desk staff login
Data model: Tenant(id, name, unit, email)
            Package(id, tenant_id -> Tenant, carrier, shelf, logged_at, pickup_code, picked_at)
Features:   - Scan the package label to log it
            - Match the package to a tenant by name
            - Notify the tenant with a pickup code
            - Mark picked up when the code is entered
            - Remind about uncollected packages
API:        REST
            POST /packages
            GET  /me/packages
            POST /packages/{id}/pickup
Storage:    PostgreSQL
Tech stack: React Native (ML Kit OCR), Express
```

---

## Example 370

**Intent:**
app for people to book a slot at the recycling center to avoid queues

**Spec:**
```
Type:       Mobile application with backend (slot booking)
Auth:       Email login with license plate
Data model: Resident(id, email, plate)
            Slot(id, starts_at, capacity)
            SlotBooking(slot_id -> Slot, resident_id -> Resident, waste_types)
Features:   - Book a 15-minute slot
            - Select waste types you bring
            - Check bookings at the gate by plate
            - Limit bookings per household per month
API:        REST
            GET  /slots?date={d}
            POST /slots/{id}/book
            GET  /gate/check?plate={p}
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework
```

---

## Example 371

**Intent:**
build trivia livestream game show app like hq trivia

**Spec:**
```
Type:       Mobile game (live game show)
Auth:       Phone login with SMS code
Data model: Player(id, username, balance)
            Show(id, starts_at, prize_pool, status)
            ShowQuestion(id, show_id -> Show, text, options, answer, order)
            PlayerAnswer(question_id -> ShowQuestion, player_id -> Player, choice)
Features:   - Stream the host live at a scheduled time
            - Push each question to all players with a 10-second timer
            - Eliminate wrong answers
            - Split the prize among winners
            - Handle 100k concurrent players
API:        REST + WebSocket
            GET  /shows/next
            POST /questions/{id}/answers
            WS   /shows/{id}
Storage:    Redis, PostgreSQL
Tech stack: React Native, Go, AWS IVS (live video)
```

---

## Example 372

**Intent:**
an app for the members of my credit union to find ATMs and branches and chat with staff

**Spec:**
```
Type:       Mobile application with backend (member services)
Auth:       Member login with online banking credentials and two-factor
Data model: Branch(id, name, lat, lng, hours)
            Atm(id, lat, lng, deposit_enabled)
            ChatThread(id, member_id, staff_id, status)
            ChatMessage(id, thread_id -> ChatThread, sender, text, at)
Features:   - Show ATMs and branches on a map
            - Filter ATMs that accept deposits
            - Chat securely with staff
            - Book a branch appointment
API:        REST + WebSocket
            GET  /branches
            GET  /atms
            POST /chats
            WS   /chats/{id}
Storage:    PostgreSQL
Tech stack: Swift, Kotlin, ASP.NET Core, SignalR
```

---

## Example 373

**Intent:**
virtual pet game where friends visit and feed each others pets

**Spec:**
```
Type:       Mobile game (social simulation)
Auth:       Sign in with Google or Apple
Data model: Player(id, name)
            Pet(id, owner_id -> Player, name, hunger, happiness, level)
            Visit(id, visitor_id -> Player, pet_id -> Pet, action, at)
Features:   - Raise a pet whose stats decay over time
            - Visit friends' pets and feed or play with them
            - Reward visitors with coins
            - Notify owners when friends visit
API:        REST
            GET  /pets/{id}
            POST /pets/{id}/actions
            GET  /friends/pets
Storage:    PostgreSQL
Tech stack: Unity (C#), PlayFab
```

---

## Example 374

**Intent:**
language school app in Japan for foreign students, see schedule and ask questions to staff in their language

**Spec:**
```
Type:       Mobile application with backend (school communication)
Auth:       Student login with student number
Data model: Student(id, number, name, language)
            Lesson(id, class_id, room, starts_at)
            Inquiry(id, student_id -> Student, text, translated_text, reply, status)
Features:   - Show the weekly timetable
            - Ask staff questions in your own language
            - Translate questions to Japanese for staff
            - Push school notices translated
API:        REST
            GET  /me/timetable
            POST /inquiries
            PATCH /inquiries/{id}
            GET  /notices
Storage:    PostgreSQL
Tech stack: Flutter, NestJS, DeepL API
```

---

## Example 375

**Intent:**
home cooks selling meals to neighbors app

**Spec:**
```
Type:       Mobile application with backend (home food marketplace)
Auth:       Phone login with SMS code; cooks verified with food permit
Data model: Cook(id, name, permit_no, area)
            Dish(id, cook_id -> Cook, name, portions, price, ready_at)
            MealOrder(id, dish_id -> Dish, buyer_id, portions, status)
Features:   - Post dishes with portions and pickup time
            - Browse dishes nearby
            - Order and pay ahead
            - Rate cooks
API:        REST
            GET  /dishes/nearby
            POST /dishes
            POST /orders
            POST /cooks/{id}/ratings
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Supabase, Stripe
```

---

## Example 376

**Intent:**
Small app so our hiking club's leaders can do roll call on the trail.

**Spec:**
```
Type:       Mobile application with backend (group safety)
Auth:       Leader email login
Data model: Hike(id, name, date, leader_id)
            Participant(id, hike_id -> Hike, name, phone)
            RollCall(id, hike_id -> Hike, at, present_ids)
Features:   - Load the participant list for a hike
            - Tick off people at each roll call
            - Work offline on the trail
            - Sync roll calls afterwards
API:        REST
            GET  /hikes/{id}/participants
            POST /hikes/{id}/rollcalls
Storage:    PostgreSQL, SQLite on device
Tech stack: Flutter, Express
```

---

## Example 377

**Intent:**
grocery delivery from asian supermarket with ingredients by recipe

**Spec:**
```
Type:       Mobile application with backend (grocery delivery)
Auth:       Email login
Data model: Product(id, name, category, price, stock)
            Recipe(id, title, cuisine, steps)
            RecipeIngredient(recipe_id -> Recipe, product_id -> Product, qty)
            Order(id, customer_id, items, total, delivery_at, status)
Features:   - Browse recipes like pho or bibimbap
            - Add all ingredients of a recipe to the cart
            - Choose a delivery slot
            - Substitute out-of-stock items with approval
API:        REST
            GET  /recipes
            POST /cart/recipe/{id}
            POST /orders
            PATCH /orders/{id}/substitutions
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework, Stripe
```

---

## Example 378

**Intent:**
mobile game where you build a town together with your friends

**Spec:**
```
Type:       Mobile game (co-op building)
Auth:       Sign in with Google or Apple
Data model: Town(id, name)
            Citizen(town_id -> Town, player_id)
            Building(id, town_id -> Town, type, x, y, level, built_by)
            Resource(town_id -> Town, wood, stone, gold)
Features:   - Place buildings on a shared grid
            - Gather resources over time
            - Upgrade buildings together
            - Sync changes to all town members
API:        REST + WebSocket
            GET  /towns/{id}
            POST /towns/{id}/buildings
            WS   /towns/{id}
Storage:    PostgreSQL
Tech stack: Unity (C#), Nakama
```

---

## Example 379

**Intent:**
app that helps blind people get help from volunteers via video call

**Spec:**
```
Type:       Mobile application with backend (assistive video)
Auth:       Email login with user and volunteer roles
Data model: User(id, name, language)
            Volunteer(id, name, language, available)
            HelpCall(id, user_id -> User, volunteer_id -> Volunteer, started_at, ended_at, rating)
Features:   - Start a help call with one large button
            - Connect to the first available volunteer speaking the same language
            - Stream the rear camera live
            - Let users rate the call
API:        REST
            POST /calls
            POST /calls/{id}/accept
            POST /calls/{id}/end
Storage:    PostgreSQL
Tech stack: Swift (VoiceOver support), Kotlin (TalkBack support), Node.js, Twilio Video
```

---

## Example 380

**Intent:**
help with app for local lending library of board games

**Spec:**
```
Type:       Mobile application with backend (lending library)
Auth:       Member email login
Data model: Game(id, title, players_min, players_max, status)
            Member(id, name)
            Loan(id, game_id -> Game, member_id -> Member, out_at, due_at, returned_at)
            Hold(game_id -> Game, member_id -> Member, at)
Features:   - Browse the game catalog by player count
            - Place a hold on a game
            - Check games out and in
            - Remind members of due dates
API:        REST
            GET  /games
            POST /games/{id}/holds
            POST /loans
            POST /loans/{id}/return
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 381

**Intent:**
i want my soccer academy kids to upload skill videos and get badges from coaches

**Spec:**
```
Type:       Mobile application with backend (training)
Auth:       Coach and player email login, parent consent for under 13
Data model: Player(id, name, age, parent_email)
            Skill(id, name, level)
            Submission(id, player_id -> Player, skill_id -> Skill, video_url, status)
            Badge(player_id -> Player, skill_id -> Skill, awarded_at)
Features:   - Show skill challenges by level
            - Upload a video attempt
            - Let coaches approve and award badges
            - Show a badge collection
API:        REST
            GET  /skills
            POST /submissions
            PATCH /submissions/{id}
            GET  /players/{id}/badges
Storage:    PostgreSQL, S3 (video)
Tech stack: Flutter, NestJS
```

---

## Example 382

**Intent:**
neighborhood emergency kit sharing (generators, first aid) during storms

**Spec:**
```
Type:       Mobile application with backend (community resilience)
Auth:       Phone login with SMS code
Data model: Neighbor(id, name, phone, lat, lng)
            Resource(id, owner_id -> Neighbor, type, description, available)
            Request(id, resource_id -> Resource, requester_id -> Neighbor, status)
Features:   - Register resources like generators and first aid kits
            - Find nearby resources during an emergency
            - Request to borrow
            - Work with SMS when data is down
API:        REST
            GET  /resources/nearby
            POST /resources
            POST /resources/{id}/requests
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Express, Twilio SMS
```

---

## Example 383

**Intent:**
app to sell tickets for my village's summer fair rides with tokens

**Spec:**
```
Type:       Mobile application with backend (token payments)
Auth:       Phone login
Data model: Visitor(id, phone, tokens)
            Ride(id, name, token_cost)
            Purchase(id, visitor_id -> Visitor, tokens, amount)
            RideUse(id, visitor_id -> Visitor, ride_id -> Ride, at)
Features:   - Buy ride tokens with card
            - Show a QR code to the ride operator
            - Deduct tokens when scanned
            - Show remaining tokens
API:        REST
            POST /purchases
            POST /rides/{id}/scan
            GET  /me/tokens
Storage:    PostgreSQL
Tech stack: Flutter, Express, Stripe
```

---

## Example 384

**Intent:**
Can u make app where i track my kids screen time across their phones and set limits from mine

**Spec:**
```
Type:       Mobile application with backend (parental controls)
Auth:       Parent email login; child devices paired by code
Data model: Parent(id, email)
            ChildDevice(id, parent_id -> Parent, name, platform)
            UsageRecord(device_id -> ChildDevice, app_package, minutes, date)
            Limit(device_id -> ChildDevice, app_package, daily_minutes)
Features:   - Report app usage from each child device
            - Show daily screen time per child
            - Set daily limits per app
            - Block apps when the limit is reached
API:        REST
            POST /devices/pair
            POST /devices/{id}/usage
            GET  /devices/{id}/usage
            PUT  /devices/{id}/limits
Storage:    PostgreSQL
Tech stack: Kotlin (Android UsageStatsManager), Swift (Screen Time API), Node.js
```

---

## Example 385

**Intent:**
wedding planner app where couple and vendors share tasks and timeline

**Spec:**
```
Type:       Mobile application with backend (collaboration)
Auth:       Email login with couple and vendor roles
Data model: Wedding(id, date, venue)
            Participant(wedding_id -> Wedding, user_id, role)
            Task(id, wedding_id -> Wedding, title, owner_id, due_date, done)
            TimelineItem(id, wedding_id -> Wedding, time, title, vendor)
Features:   - Invite vendors to the wedding workspace
            - Assign tasks with due dates
            - Build the day-of timeline
            - Notify vendors of changes
API:        REST
            POST /weddings
            POST /weddings/{id}/tasks
            PUT  /weddings/{id}/timeline
            POST /weddings/{id}/invites
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 386

**Intent:**
queue app for food stalls at a night market

**Spec:**
```
Type:       Mobile application with backend (virtual queue)
Auth:       No login; ticket stored on the device
Data model: Stall(id, name, avg_wait_min)
            QueueTicket(id, stall_id -> Stall, number, device_token, status)
Features:   - Scan the stall's QR to get a queue number
            - Show how many are ahead
            - Push when your food is ready
            - Let stall owners call the next number
API:        REST
            POST /stalls/{id}/tickets
            GET  /tickets/{id}
            POST /stalls/{id}/call-next
Storage:    Redis
Tech stack: Flutter, Express, Firebase Cloud Messaging
```

---

## Example 387

**Intent:**
hey can u make an app where gamers rate each other after matches like a reputation system

**Spec:**
```
Type:       Mobile application with backend (player reputation)
Auth:       Sign in with Steam
Data model: Gamer(id, steam_id, name, reputation)
            MatchRecord(id, game, played_at)
            Endorsement(match_id -> MatchRecord, from_id -> Gamer, to_id -> Gamer, type)
Features:   - Import recent matches from Steam
            - Endorse teammates as friendly or skilled
            - Report toxic players
            - Show a reputation score on profiles
API:        REST
            GET  /matches/recent
            POST /endorsements
            POST /reports
            GET  /gamers/{id}
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Steam Web API
```

---

## Example 388

**Intent:**
dorm laundry machine status with sensors

**Spec:**
```
Type:       IoT system (with mobile app)
Auth:       Student SSO
Data model: Machine(id, dorm, floor, type, status, updated_at)
            WatchRequest(machine_id -> Machine, student_id)
Features:   - Detect running or free machines from current sensors
            - Show machine status per floor
            - Notify when a machine becomes free
            - Notify when your cycle ends
API:        REST
            GET  /dorms/{id}/machines
            POST /machines/{id}/watch
            POST /machines/{id}/state
Storage:    Redis, PostgreSQL
Tech stack: ESP32 with current sensors, MQTT, Express, Flutter
```

---

## Example 389

**Intent:**
football club membership card app

**Spec:**
```
Type:       Mobile application with backend (membership)
Auth:       Email login
Data model: Member(id, name, number, tier, valid_until)
            Benefit(id, tier, description)
            MatchAttendance(member_id -> Member, match_date)
Features:   - Show a digital membership card with QR
            - Scan cards at the turnstile
            - Show benefits by tier
            - Renew membership in the app
API:        REST
            GET  /me/card
            POST /scan
            POST /renewals
Storage:    PostgreSQL
Tech stack: Flutter, Express, Stripe
```

---

## Example 390

**Intent:**
swap shifts app for my restaurant staff

**Spec:**
```
Type:       Mobile application with backend (shift scheduling)
Auth:       Staff phone login; manager role
Data model: Employee(id, name, role)
            Shift(id, employee_id -> Employee, starts_at, ends_at, role)
            ShiftSwap(id, shift_id -> Shift, offered_by -> Employee, taken_by -> Employee, status)
Features:   - Show the weekly schedule
            - Offer a shift to coworkers
            - Let a coworker with the same role take it
            - Require manager approval
            - Notify everyone of schedule changes
API:        REST
            GET  /schedule?week={d}
            POST /shifts/{id}/offer
            POST /swaps/{id}/take
            POST /swaps/{id}/approve
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 391

**Intent:**
ice cream truck tracker so kids know when its on their street

**Spec:**
```
Type:       Mobile application with backend (live tracking)
Auth:       Driver login; families use the app without an account
Data model: Truck(id, name, lat, lng, active, updated_at)
            StreetAlert(device_token, lat, lng, radius_m)
Features:   - Share the truck's location while it is on route
            - Show the truck live on a map
            - Notify families when it comes within 500 m
            - Show today's planned route
API:        REST + WebSocket
            POST /trucks/{id}/position
            POST /alerts
            WS   /trucks/live
Storage:    Redis
Tech stack: Flutter, Express, Firebase Cloud Messaging
```

---

## Example 392

**Intent:**
game where people in the same bar play trivia against other bars

**Spec:**
```
Type:       Mobile game (venue-based trivia)
Auth:       Team name per bar check-in
Data model: Bar(id, name, city)
            Team(id, bar_id -> Bar, name)
            QuizNight(id, date)
            TeamScore(night_id -> QuizNight, team_id -> Team, points)
Features:   - Check in to a bar to join tonight's quiz
            - Answer questions synced across all bars
            - Rank teams within the bar and nationally
            - Award the top bar a trophy badge
API:        REST + WebSocket
            POST /nights/{id}/teams
            WS   /nights/{id}
            GET  /nights/{id}/rankings
Storage:    PostgreSQL, Redis
Tech stack: React Native, Node.js, Socket.IO
```

---

## Example 393

**Intent:**
helo, i have small company of water delivery in Mexico, 20 liter bottles. clients order from app and the driver see the route.

**Spec:**
```
Type:       Mobile application with backend (water delivery)
Auth:       Phone login with SMS code
Data model: Client(id, name, phone, address, lat, lng)
            WaterOrder(id, client_id -> Client, bottles, empties_returned, status, date)
            Driver(id, name, phone)
Features:   - Order bottles of water with one tap
            - Repeat the last order
            - Show the driver today's orders on a route map
            - Record empty bottles collected
            - Pay cash or card
API:        REST
            POST /orders
            POST /orders/repeat
            GET  /drivers/me/route
            PATCH /orders/{id}
Storage:    PostgreSQL
Tech stack: Flutter (Spanish UI), Node.js, Mercado Pago, Google Maps SDK
```

---

## Example 394

**Intent:**
app for clubs at my university to post events and members check in for points

**Spec:**
```
Type:       Mobile application with backend (campus engagement)
Auth:       University SSO
Data model: Club(id, name)
            ClubEvent(id, club_id -> Club, title, at, location, checkin_code)
            Student(id, name)
            CheckIn(event_id -> ClubEvent, student_id -> Student, at)
Features:   - Browse club events this week
            - Check in with the event's code
            - Earn points per event
            - Show a semester leaderboard
API:        REST
            GET  /events
            POST /events
            POST /events/{id}/checkin
            GET  /leaderboard
Storage:    PostgreSQL
Tech stack: React Native, Express
```

---

## Example 395

**Intent:**
book sharing between offices in our company with internal shipping

**Spec:**
```
Type:       Mobile application with backend (internal sharing)
Auth:       Company SSO
Data model: Employee(id, name, office)
            Book(id, owner_id -> Employee, title, isbn, holder_id -> Employee)
            BorrowRequest(id, book_id -> Book, requester_id -> Employee, status)
Features:   - List books you can lend
            - Request a book from another office
            - Generate an internal mail label
            - Track who holds each book
API:        REST
            GET  /books
            POST /books
            POST /books/{id}/requests
            PATCH /requests/{id}
Storage:    PostgreSQL
Tech stack: Flutter, ASP.NET Core
```

---

## Example 396

**Intent:**
realtime hide and seek game with phone gps in a park

**Spec:**
```
Type:       Mobile game (location-based)
Auth:       Guest nickname per game
Data model: Game(id, code, area_polygon, seeker_id, ends_at)
            Player(id, game_id -> Game, nickname, lat, lng, found)
Features:   - Set the play area on a map
            - Reveal hiders' positions to the seeker every 2 minutes
            - Mark players found by tapping their phones
            - Warn players who leave the area
API:        WebSocket + REST
            POST /games
            POST /games/{code}/join
            WS   /games/{code}
Storage:    Redis
Tech stack: React Native, Node.js
```

---

## Example 397

**Intent:**
app where i check my 5 airbnb apartments' smart locks and thermostats

**Spec:**
```
Type:       IoT system (property automation)
Auth:       Owner email login with two-factor
Data model: Property(id, name, address)
            Device(id, property_id -> Property, type, vendor_id, state)
            GuestStay(id, property_id -> Property, guest_name, check_in, check_out, door_code)
Features:   - Show all devices per apartment
            - Create door codes valid during each stay
            - Set thermostats to eco mode after check-out
            - Alert on low battery or offline devices
API:        REST
            GET  /properties
            GET  /properties/{id}/devices
            POST /stays
            POST /devices/{id}/command
Storage:    PostgreSQL
Tech stack: React Native, Node.js, SmartThings API, Airbnb iCal sync
```

---

## Example 398

**Intent:**
drivers app for school buses, report breakdowns and delays to the office

**Spec:**
```
Type:       Mobile application with backend (fleet operations)
Auth:       Driver PIN login
Data model: Driver(id, name)
            Bus(id, number)
            Run(id, bus_id -> Bus, driver_id -> Driver, date)
            DelayReport(id, run_id -> Run, minutes, reason, at)
Features:   - Start today's run
            - Report a delay with minutes and reason
            - Report a breakdown with location
            - Notify the office and affected parents
API:        REST
            POST /runs
            POST /runs/{id}/delays
            POST /runs/{id}/breakdown
Storage:    PostgreSQL
Tech stack: Flutter, Express, Twilio
```

---

## Example 399

**Intent:**
tinder for jobs, swipe on job posts

**Spec:**
```
Type:       Mobile application with backend (job matching)
Auth:       Email or LinkedIn login
Data model: Candidate(id, name, skills, city)
            Employer(id, company)
            JobPost(id, employer_id -> Employer, title, skills, salary_range, city)
            Swipe(candidate_id -> Candidate, job_id -> JobPost, liked)
            EmployerLike(employer_id -> Employer, candidate_id -> Candidate)
            Match(id, candidate_id -> Candidate, job_id -> JobPost)
Features:   - Swipe through jobs matching your skills
            - Let employers swipe on candidates who liked them
            - Create a match on mutual interest
            - Chat after matching
API:        REST
            GET  /jobs/feed
            POST /swipes
            GET  /employers/me/candidates
            GET  /matches
Storage:    PostgreSQL
Tech stack: React Native, NestJS
```

---

## Example 400

**Intent:**
thermostats in our office floors, employees vote too hot / too cold from phone

**Spec:**
```
Type:       IoT system (with mobile voting app)
Auth:       Company SSO
Data model: Zone(id, floor, name, setpoint_c, current_c)
            ComfortVote(zone_id -> Zone, employee_id, vote, at)
Features:   - Show the current temperature for your zone
            - Vote too hot, too cold or just right
            - Adjust the setpoint by half a degree when votes lean one way
            - Show facilities a comfort report
API:        REST
            GET  /zones
            POST /zones/{id}/votes
            GET  /reports/comfort
Storage:    PostgreSQL
Tech stack: Flutter, Python, BACnet integration
```

---

## Example 401

**Intent:**
farmers market vendor payments with tokens

**Spec:**
```
Type:       Mobile application with backend (market payments)
Auth:       Vendor email login
Data model: Vendor(id, name, stall)
            Shopper(id, phone, balance)
            TokenPayment(id, shopper_id -> Shopper, vendor_id -> Vendor, amount, at)
Features:   - Let shoppers load market credit with SNAP or card
            - Pay vendors by scanning their QR code
            - Show vendors daily totals
            - Reimburse vendors weekly
API:        REST
            POST /shoppers/topup
            POST /payments
            GET  /vendors/me/totals
Storage:    PostgreSQL
Tech stack: Flutter, Django REST Framework, Stripe
```

---

## Example 402

**Intent:**
help my gaming clan with an app for raid sign ups and roles

**Spec:**
```
Type:       Mobile application with backend (gaming community)
Auth:       Sign in with Discord
Data model: Member(id, discord_id, name)
            Character(id, member_id -> Member, name, class, role)
            Raid(id, name, at, tanks_needed, healers_needed, dps_needed)
            RaidSignup(raid_id -> Raid, character_id -> Character, status)
Features:   - Post raids with role slots
            - Sign up a character for a role
            - Put extras on the bench
            - Post the roster to Discord
API:        REST
            GET  /raids
            POST /raids
            POST /raids/{id}/signups
            POST /raids/{id}/discord
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Discord Webhooks
```

---

## Example 403

**Intent:**
mobile app for my piano studio recitals, parents buy tickets and see the program

**Spec:**
```
Type:       Mobile application with backend (event ticketing)
Auth:       Parent email login
Data model: Recital(id, date, venue)
            ProgramItem(id, recital_id -> Recital, student_name, piece, order)
            TicketOrder(id, recital_id -> Recital, parent_email, quantity, paid)
Features:   - Publish the recital program
            - Sell tickets with a seat limit
            - Show QR tickets
            - Share recordings after the recital
API:        REST
            GET  /recitals/{id}
            POST /recitals/{id}/tickets
            GET  /me/tickets
Storage:    PostgreSQL
Tech stack: Flutter, Supabase, Stripe
```

---

## Example 404

**Intent:**
app for street vendors to accept orders over whatsapp and track them

**Spec:**
```
Type:       Mobile application with backend (order management)
Auth:       Vendor phone login
Data model: Vendor(id, name, whatsapp_number)
            Customer(id, phone, name)
            Order(id, vendor_id -> Vendor, customer_id -> Customer, text, total, status, at)
Features:   - Receive WhatsApp messages as orders
            - Parse items and totals from the message
            - Track order status
            - Reply to customers from the app
API:        REST
            POST /webhooks/whatsapp
            GET  /orders
            PATCH /orders/{id}
            POST /orders/{id}/reply
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, WhatsApp Business Cloud API
```

---

## Example 405

**Intent:**
geofenced coupons app for a shopping mall

**Spec:**
```
Type:       Mobile application with backend (proximity marketing)
Auth:       Email or Google login
Data model: Store(id, name, floor)
            Coupon(id, store_id -> Store, title, discount, valid_until)
            Beacon(id, store_id -> Store, uuid)
            CouponClaim(coupon_id -> Coupon, user_id, redeemed)
Features:   - Detect when a shopper is near a store via Bluetooth beacons
            - Push a coupon for that store
            - Save coupons to a wallet
            - Redeem coupons at checkout
API:        REST
            GET  /coupons
            POST /beacons/{id}/enter
            POST /coupons/{id}/claim
            POST /claims/{id}/redeem
Storage:    PostgreSQL
Tech stack: Swift (iBeacon), Kotlin (Android BLE), Express
```

---

## Example 406

**Intent:**
Seriously need a way for our 12 person ultimate team to sort out who's driving to tournaments, where we're staying, and who paid for the airbnb

**Spec:**
```
Type:       Mobile application with backend (team travel)
Auth:       Sign in with Google
Data model: Teammate(id, name)
            Tournament(id, name, city, dates)
            Car(id, tournament_id -> Tournament, driver_id -> Teammate, seats)
            CarSeat(car_id -> Car, teammate_id -> Teammate)
            Lodging(id, tournament_id -> Tournament, address, cost, paid_by -> Teammate)
Features:   - Add upcoming tournaments
            - Assign teammates to cars
            - Share lodging details
            - Split lodging and gas costs
API:        REST
            GET  /tournaments
            POST /tournaments/{id}/cars
            POST /cars/{id}/seats
            GET  /tournaments/{id}/costs
Storage:    Cloud Firestore
Tech stack: Flutter, Firebase
```

---

## Example 407

**Intent:**
parking ticket dispute helper where drivers share photos of unclear signs

**Spec:**
```
Type:       Mobile application with backend (crowdsourced)
Auth:       Email login
Data model: Sign(id, lat, lng, photo_url, description, confusing_votes)
            Ticket(id, user_id, sign_id -> Sign, amount, outcome)
Features:   - Post photos of confusing parking signs
            - Vote on how confusing a sign is
            - Log tickets and dispute outcomes
            - Show win rates for disputes at a sign
API:        REST
            GET  /signs/nearby
            POST /signs
            POST /signs/{id}/vote
            POST /tickets
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Express
```

---

## Example 408

**Intent:**
mini golf scorecard shared by the group

**Spec:**
```
Type:       Mobile application with backend
Auth:       Join with a game code
Data model: Round(id, code, course, holes)
            Player(id, round_id -> Round, name)
            Score(player_id -> Player, hole, strokes)
Features:   - Start a round and share the code
            - Enter strokes per hole from any phone
            - Show live totals
            - Crown the winner
API:        REST + WebSocket
            POST /rounds
            POST /rounds/{code}/scores
            WS   /rounds/{code}
Storage:    Firebase Realtime Database
Tech stack: React Native, Firebase
```

---

## Example 409

**Intent:**
im a uni student, want app where students sell leftover meal plan swipes to each other

**Spec:**
```
Type:       Mobile application with backend (peer marketplace)
Auth:       University email login
Data model: Student(id, name, email)
            SwipeOffer(id, seller_id -> Student, dining_hall, price, available_at)
            SwipeDeal(id, offer_id -> SwipeOffer, buyer_id -> Student, status)
Features:   - Post spare swipes with a dining hall and time
            - Buy a swipe and meet at the hall
            - Pay through the app
            - Rate buyers and sellers
API:        REST
            GET  /offers
            POST /offers
            POST /offers/{id}/buy
            POST /deals/{id}/rate
Storage:    PostgreSQL
Tech stack: React Native, Supabase, Stripe
```

---

## Example 410

**Intent:**
animal shelter volunteers dog walking schedule

**Spec:**
```
Type:       Mobile application with backend (volunteer scheduling)
Auth:       Volunteer email login
Data model: Volunteer(id, name)
            ShelterDog(id, name, walk_level)
            WalkLog(id, dog_id -> ShelterDog, volunteer_id -> Volunteer, at, duration_min, notes)
Features:   - Show which dogs have not been walked today
            - Log a walk with notes
            - Restrict difficult dogs to experienced volunteers
            - Show weekly walk counts
API:        REST
            GET  /dogs/today
            POST /walks
            GET  /reports/weekly
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 411

**Intent:**
build me an app on Expo with Convex where my friends and I keep a shared bucket list

**Spec:**
```
Type:       Mobile application with backend (shared list)
Auth:       Convex Auth (email magic link)
Data model: Group(id, name)
            BucketItem(id, group_id -> Group, title, added_by, done, done_at, photo_url)
Features:   - Add bucket list items
            - Mark items done with a photo
            - Sync changes live to all friends
            - Show completed items as a timeline
Storage:    Convex database
Tech stack: React Native (Expo), Convex
```

---

## Example 412

**Intent:**
chat rooms for each flight so passengers can share taxis on arrival

**Spec:**
```
Type:       Mobile application with backend (travel social)
Auth:       Phone login with SMS code
Data model: Flight(id, number, date, destination)
            Passenger(id, name, flight_id -> Flight)
            FlightMessage(id, flight_id -> Flight, passenger_id -> Passenger, text, at)
Features:   - Join a chat room by flight number and date
            - Post where you are heading after landing
            - Group up for a shared taxi
            - Close the room a day after arrival
API:        REST + WebSocket
            POST /flights/join
            GET  /flights/{id}/messages
            WS   /flights/{id}
Storage:    Redis, PostgreSQL
Tech stack: Flutter, Node.js
```

---

## Example 413

**Intent:**
compost pickup app

**Spec:**
```
Type:       Mobile application with backend (subscription pickup)
Auth:       Email login
Data model: Household(id, address, plan)
            Pickup(id, household_id -> Household, date, weight_kg, status)
Features:   - Subscribe to weekly compost pickup
            - Remind the night before
            - Record weight collected
            - Show compost returned to gardens
API:        REST
            POST /subscriptions
            GET  /me/pickups
            PATCH /pickups/{id}
Storage:    PostgreSQL
Tech stack: React Native, Express, Stripe Billing
```

---

## Example 414

**Intent:**
Hello, we are a small team in Egypt. We want a mobile app for women to find female tutors who come to home, with booking and safety check-in.

**Spec:**
```
Type:       Mobile application with backend (home tutoring)
Auth:       Phone login with SMS code; tutors verified with national ID
Data model: Parent(id, name, phone, address)
            Tutor(id, name, subjects, verified, rating)
            Session(id, parent_id -> Parent, tutor_id -> Tutor, subject, at, status)
            SafetyCheck(session_id -> Session, type, at, lat, lng)
Features:   - Search verified female tutors by subject
            - Book home sessions
            - Let the tutor check in and out with location
            - Alert the agency if check-out is missed
            - Support Arabic and English
API:        REST
            GET  /tutors
            POST /sessions
            POST /sessions/{id}/check
            GET  /sessions/{id}
Storage:    PostgreSQL
Tech stack: Flutter (RTL Arabic support), Laravel, Paymob
```

---

## Example 415

**Intent:**
real time multiplayer word game like scrabble

**Spec:**
```
Type:       Mobile game (turn-based multiplayer)
Auth:       Sign in with Google or Apple
Data model: Player(id, name, rating)
            Match(id, players, board_json, bag_json, turn, status)
            Rack(match_id -> Match, player_id -> Player, tiles)
            Play(id, match_id -> Match, player_id -> Player, word, score, at)
Features:   - Start a match with up to 4 players
            - Validate words against a dictionary on the server
            - Score plays with letter and word multipliers
            - Notify players when it's their turn
API:        REST
            POST /matches
            POST /matches/{id}/plays
            GET  /matches/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Go
```

---

## Example 416

**Intent:**
my church wants a bus pickup app for elderly members on Sunday

**Spec:**
```
Type:       Mobile application with backend (community transport)
Auth:       Phone login
Data model: Member(id, name, phone, address)
            SundayRide(id, date, member_id -> Member, needed, picked_up)
            Driver(id, name)
Features:   - Let members request a ride for Sunday
            - Build the pickup route for the driver
            - Mark members picked up
            - Call the member from the app
API:        REST
            POST /rides
            GET  /rides?date={d}
            PATCH /rides/{id}
Storage:    PostgreSQL
Tech stack: Flutter, Express
```

---

## Example 417

**Intent:**
escape game in the city with clues unlocked by gps and qr codes, teams compete

**Spec:**
```
Type:       Mobile game (outdoor team puzzle)
Auth:       Team login with booking code
Data model: Booking(id, code, team_name, starts_at)
            Clue(id, order, lat, lng, qr_code, puzzle, answer)
            Progress(booking_id -> Booking, clue_id -> Clue, solved_at, hints_used)
Features:   - Unlock clues at locations by GPS or QR code
            - Check answers on the server
            - Give hints with a time penalty
            - Rank teams by finish time
API:        REST
            POST /auth/booking
            GET  /clues/current
            POST /clues/{id}/answer
            POST /clues/{id}/hint
Storage:    PostgreSQL
Tech stack: React Native, NestJS
```

---

## Example 418

**Intent:**
walkie app for ski instructors on the mountain

**Spec:**
```
Type:       Mobile application with backend (team communication)
Auth:       Instructor login with school code
Data model: Instructor(id, name, school)
            Group(id, school, name)
            Ping(id, from_id -> Instructor, group_id -> Group, type, lat, lng, at)
Features:   - Send voice messages to the ski school group
            - Share location on the slope map
            - Send an injury alert with location
            - Work on weak mobile signal
API:        WebSocket + REST
            WS   /groups/{id}
            POST /pings
            GET  /groups/{id}/positions
Storage:    Redis
Tech stack: Flutter, Elixir, Phoenix
```

---

## Example 419

**Intent:**
pantry app where shelters post needed items and donors pledge

**Spec:**
```
Type:       Mobile application with backend (donation matching)
Auth:       Shelter staff and donor email login
Data model: Shelter(id, name, address)
            Need(id, shelter_id -> Shelter, item, quantity, urgent)
            Pledge(id, need_id -> Need, donor_id, quantity, delivered)
Features:   - Post needed items with quantities
            - Let donors pledge items
            - Mark pledges delivered
            - Highlight urgent needs
API:        REST
            GET  /needs
            POST /needs
            POST /needs/{id}/pledges
            PATCH /pledges/{id}
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 420

**Intent:**
smart beehive scale app, see hive weight from my phone

**Spec:**
```
Type:       IoT system (with mobile app)
Auth:       Email login
Data model: Hive(id, owner_id, name, lat, lng)
            WeightReading(hive_id -> Hive, kg, temp_c, at)
Features:   - Send hive weight every hour over cellular
            - Chart weight to spot honey flow
            - Alert on sudden weight loss (swarm or theft)
            - Share hives with other beekeepers
API:        REST
            POST /hives/{id}/readings
            GET  /hives/{id}/readings
            POST /hives/{id}/share
Storage:    InfluxDB
Tech stack: Arduino MKR NB 1500, HX711 load cell, Node.js, Flutter
```

---

## Example 421

**Intent:**
help me make app where people report stray animals and rescuers pick up the case

**Spec:**
```
Type:       Mobile application with backend (animal rescue)
Auth:       Email login; rescuers verified
Data model: Report(id, reporter_id, species, condition, photo_url, lat, lng, status, rescuer_id)
            Rescuer(id, name, phone, verified)
Features:   - Report a stray with photo and location
            - Alert rescuers nearby
            - Let a rescuer claim the case
            - Update the reporter on the outcome
API:        REST
            POST /reports
            GET  /reports/nearby
            POST /reports/{id}/claim
            PATCH /reports/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Django REST Framework
```

---

## Example 422

**Intent:**
chat with ur neighbours during a blackout over bluetooth mesh no internet

**Spec:**
```
Type:       Mobile application (offline mesh messaging, with optional sync backend)
Data model: Peer(id, nickname)
            MeshMessage(id, sender_id -> Peer, text, hop_count, created_at)
Features:   - Discover nearby phones over Bluetooth LE
            - Relay messages through other phones
            - Limit relays with a hop count
            - Sync messages to a server when internet returns
API:        REST
            POST /messages/sync
Storage:    SQLite on device, PostgreSQL (sync)
Tech stack: Kotlin (Android Nearby Connections), Swift (MultipeerConnectivity), Express
```

---

