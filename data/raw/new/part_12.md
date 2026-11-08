## Example 1

**Intent:**
alumni network for my old high school

**Spec:**
```
Type:       Web application (alumni network)
Auth:       Email + password login, admin approval of new members
Data model: Member(id, name, email, graduation_year, city, occupation, approved)
            Event(id, title, date, location, description)
            Rsvp(id, member_id -> Member, event_id -> Event, status)
Features:   - Register with graduation year and wait for admin approval
            - Search the member directory by year, city or occupation
            - Create reunion events and collect RSVPs
            - Send email announcements to a graduating class
            - Edit your own profile and privacy settings
API:        REST
            GET  /members
            POST /members
            GET  /events
            POST /events/{id}/rsvp
Storage:    PostgreSQL
Tech stack: Python, Django, Bootstrap
```

---

## Example 2

**Intent:**
I run a small chess club and want a site where members can record their games and see a club rating ladder.

**Spec:**
```
Type:       Web application (club rating ladder)
Auth:       Email + password login
Data model: Player(id, name, email, rating)
            Game(id, white_id -> Player, black_id -> Player, result, pgn, played_on)
Features:   - Record a game result between two members with optional PGN
            - Update both players' ratings with the Elo formula
            - Show the ladder sorted by current rating
            - Show each player's game history and rating chart
            - Replay a recorded game move by move on a board
API:        REST
            GET  /players
            GET  /games
            POST /games
            GET  /players/{id}/history
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, chess.js
```

---

## Example 3

**Intent:**
birdwatching log where our group can share sightings on a map

**Spec:**
```
Type:       Web application (citizen sightings map)
Auth:       Email + password login
Data model: User(id, name, email)
            Species(id, common_name, scientific_name)
            Sighting(id, user_id -> User, species_id -> Species, lat, lng, count, seen_at, photo_url)
Features:   - Log a sighting with species, count, location and photo
            - Show all group sightings as markers on a map
            - Filter sightings by species and date range
            - Show a personal life list of species seen
            - Autocomplete species names from a checklist
API:        REST
            GET  /sightings
            POST /sightings
            GET  /species?q={text}
            GET  /users/{id}/life-list
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Python, FastAPI, React, Leaflet
```

---

## Example 4

**Intent:**
fan fiction archive with tags and chapters

**Spec:**
```
Type:       Web application (fan fiction archive)
Auth:       Email + password login
Data model: Author(id, username, email, password_hash)
            Work(id, author_id -> Author, title, summary, rating, status)
            Chapter(id, work_id -> Work, number, title, body)
            Tag(id, name, kind)
            WorkTag(work_id -> Work, tag_id -> Tag)
Features:   - Publish a work and add chapters over time
            - Tag works by fandom, characters and content warnings
            - Filter and exclude works by tags
            - Leave kudos and comments on chapters
            - Subscribe to a work and get notified of new chapters
API:        REST
            GET  /works?tags={list}&exclude={list}
            POST /works
            POST /works/{id}/chapters
            POST /chapters/{id}/comments
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 5

**Intent:**
My neighbourhood has a lot of people who lose pets and keys and stuff, and we post on a facebook group but it's a mess. I'd like a simple website just for lost and found items in our area where you can post what you lost or found with a photo and the rough location.

**Spec:**
```
Type:       Web application (local lost and found)
Auth:       Email login with magic link
Data model: User(id, email, display_name)
            Post(id, user_id -> User, kind, category, title, description, photo_url, lat, lng, created_at, resolved)
            Message(id, post_id -> Post, sender_id -> User, body, sent_at)
Features:   - Post a lost or found item with photo, category and map location
            - Browse posts on a map or list filtered by category and distance
            - Message the poster privately without showing email addresses
            - Mark a post as resolved when the item is returned
            - Expire posts automatically after 60 days
API:        REST
            GET  /posts?kind={lost|found}&near={lat,lng}
            POST /posts
            POST /posts/{id}/messages
            PATCH /posts/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Flask, HTMX, Leaflet
```

---

## Example 6

**Intent:**
tool library website so neighbours can borrow drills ladders etc

**Spec:**
```
Type:       Web application (tool lending library)
Auth:       Email + password login, admin role for volunteers
Data model: Member(id, name, email, phone, is_admin)
            Tool(id, name, category, condition, photo_url, available)
            Loan(id, tool_id -> Tool, member_id -> Member, borrowed_on, due_on, returned_on)
Features:   - Browse the tool catalog by category and availability
            - Reserve a tool for pickup on a chosen date
            - Check tools out and back in at the volunteer desk
            - Send reminder emails when a loan is due or overdue
            - Record tool condition notes on return
API:        REST
            GET  /tools
            POST /tools/{id}/reservations
            POST /loans
            PATCH /loans/{id}/return
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Blade
```

---

## Example 7

**Intent:**
A skill swapping platform: I teach you guitar, you teach me Spanish. No money involved.

**Spec:**
```
Type:       Web application (skill exchange)
Auth:       Email + password login
Data model: User(id, name, email, city, bio)
            Skill(id, name)
            UserSkill(user_id -> User, skill_id -> Skill, mode)
            SwapRequest(id, from_id -> User, to_id -> User, offer_skill_id -> Skill, want_skill_id -> Skill, status)
Features:   - List skills you can teach and skills you want to learn
            - Suggest matches where both users want what the other offers
            - Send, accept or decline swap requests
            - Chat with a matched partner
            - Rate a partner after a completed swap
API:        REST
            GET  /matches
            POST /swap-requests
            PATCH /swap-requests/{id}
            GET  /users/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Vue.js
```

---

## Example 8

**Intent:**
mentorship matching for junior devs in our company

**Spec:**
```
Type:       Web application (mentorship matching)
Auth:       Company single sign-on (OAuth 2.0 / OpenID Connect)
Data model: Employee(id, name, email, team, seniority)
            Profile(id, employee_id -> Employee, role, topics, availability_hours)
            Match(id, mentor_id -> Employee, mentee_id -> Employee, score, status, started_on)
            Session(id, match_id -> Match, date, notes)
Features:   - Fill in a mentor or mentee profile with topics and availability
            - Score mentor-mentee pairs by topic overlap and team distance
            - Let an admin review and confirm proposed matches
            - Log mentoring sessions with private notes
            - Send a feedback survey after three months
API:        REST
            POST /profiles
            GET  /matches/suggestions
            POST /matches
            POST /matches/{id}/sessions
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, React
```

---

## Example 9

**Intent:**
i maintain an open source lib and want a page where companies can sponsor monthly and get there logo shown

**Spec:**
```
Type:       Web application (open-source sponsorship page)
Auth:       Email + password login for sponsors, admin login for maintainer
Data model: Sponsor(id, company_name, email, logo_url, website, tier_id -> Tier)
            Tier(id, name, monthly_price_cents, perks)
            Subscription(id, sponsor_id -> Sponsor, stripe_subscription_id, status)
Features:   - Show sponsorship tiers with prices and perks
            - Subscribe to a monthly tier with Stripe Checkout
            - Upload a logo and website link after payment
            - Display active sponsors' logos grouped by tier
            - Provide an SVG badge of sponsors for the README
            - Remove logos automatically when a subscription is cancelled
API:        REST
            GET  /tiers
            POST /checkout
            POST /webhooks/stripe
            GET  /sponsors.svg
Storage:    PostgreSQL, S3 (logos)
Tech stack: Node.js, Next.js, Stripe API
```

---

## Example 10

**Intent:**
podcast hosting site that generates the RSS feed for apple and spotify

**Spec:**
```
Type:       Web application (podcast hosting)
Auth:       Email + password login
Data model: User(id, email, password_hash)
            Show(id, user_id -> User, title, description, cover_url, category, language)
            Episode(id, show_id -> Show, title, notes, audio_url, duration_s, published_at)
            Download(id, episode_id -> Episode, ip_hash, user_agent, downloaded_at)
Features:   - Create a show with cover art and category
            - Upload episode audio and schedule publishing
            - Generate an iTunes-compatible RSS feed per show
            - Count downloads per episode and show daily stats
            - Embed an audio player on other websites
API:        REST
            POST /shows
            POST /shows/{id}/episodes
            GET  /shows/{id}/feed.xml
            GET  /episodes/{id}/stats
Storage:    PostgreSQL, S3 (audio files), CDN
Tech stack: Python, Django, Celery, FFmpeg
```

---

## Example 11

**Intent:**
photo contest for our camera club, members submit and vote

**Spec:**
```
Type:       Web application (photo contest)
Auth:       Email + password login
Data model: Member(id, name, email)
            Contest(id, theme, submit_until, vote_until, max_entries)
            Entry(id, contest_id -> Contest, member_id -> Member, title, image_url)
            Vote(id, entry_id -> Entry, voter_id -> Member, points)
Features:   - Open a monthly contest with a theme and deadlines
            - Submit up to the allowed number of photos per contest
            - Hide entrant names during the voting period
            - Give 3, 2 and 1 points to favourite entries, not your own
            - Announce winners and show a gallery of past contests
API:        REST
            GET  /contests
            POST /contests/{id}/entries
            POST /contests/{id}/votes
            GET  /contests/{id}/results
Storage:    PostgreSQL, S3 (images)
Tech stack: Node.js, Express, Svelte
```

---

## Example 12

**Intent:**
a petition website where anyone can start a petition and collect signatures

**Spec:**
```
Type:       Web application (petitions)
Auth:       Email + password login for creators, email confirmation for signers
Data model: User(id, name, email)
            Petition(id, creator_id -> User, title, body, target, goal, status)
            Signature(id, petition_id -> Petition, name, email, postcode, confirmed, signed_at)
Features:   - Create a petition with a title, text, recipient and goal
            - Sign a petition and confirm by email link
            - Show a progress bar of confirmed signatures
            - Block duplicate signatures from the same email
            - Export signatures as CSV for delivery to the target
API:        REST
            POST /petitions
            GET  /petitions/{id}
            POST /petitions/{id}/signatures
            GET  /signatures/confirm?token={token}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 13

**Intent:**
We are researchers counting butterflies and want volunteers from the public to upload their counts from gardens. Need a simple web form and a way for us to download the data.

**Spec:**
```
Type:       Web application (citizen science data collection)
Auth:       Email + password login for volunteers, researcher role
Data model: Volunteer(id, name, email, postcode)
            Survey(id, volunteer_id -> Volunteer, site_lat, site_lng, date, duration_min, weather)
            Count(id, survey_id -> Survey, species, number)
Features:   - Submit a 15-minute garden count with species and numbers
            - Pick the garden location on a map
            - Flag unusual counts for researcher review
            - Show volunteers a summary of their past surveys
            - Export all validated data as CSV for researchers
API:        REST
            POST /surveys
            GET  /surveys/mine
            GET  /admin/flagged
            GET  /admin/export.csv
Storage:    PostgreSQL
Tech stack: Python, Flask, Leaflet
```

---

## Example 14

**Intent:**
language exchange partners finder

**Spec:**
```
Type:       Web application (language exchange)
Auth:       Email + password login, Google sign-in
Data model: User(id, name, email, timezone, bio)
            UserLanguage(user_id -> User, language_code, level, role)
            Conversation(id, user_a_id -> User, user_b_id -> User)
            Message(id, conversation_id -> Conversation, sender_id -> User, body, sent_at)
Features:   - Set native languages and languages you are learning
            - Find partners whose native language is your target and vice versa
            - Filter partners by timezone overlap
            - Chat in real time with text corrections
            - Block and report users
API:        REST + WebSocket
            GET  /partners
            POST /conversations
            GET  /conversations/{id}/messages
            WS   /chat
Storage:    PostgreSQL, Redis (presence)
Tech stack: Node.js, Socket.IO, React
```

---

## Example 15

**Intent:**
study group finder for students at my uni, by course code

**Spec:**
```
Type:       Web application (study groups)
Auth:       University email login with verification code
Data model: Student(id, name, email)
            Course(id, code, title)
            Group(id, course_id -> Course, name, meets_at, location, max_size)
            Membership(group_id -> Group, student_id -> Student)
Features:   - Search study groups by course code
            - Create a group with meeting time, place and size limit
            - Join or leave a group until it is full
            - Post messages on a group board
            - Restrict sign-up to verified university email domains
API:        REST
            GET  /courses/{code}/groups
            POST /groups
            POST /groups/{id}/join
            DELETE /groups/{id}/join
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 16

**Intent:**
Our student society runs a hackathon each year and it's all spreadsheets. Want a web app for registrations, team forming, project submissions and judging scores.

**Spec:**
```
Type:       Web application (hackathon management)
Auth:       Email + password login, roles: hacker, judge, organiser
Data model: User(id, name, email, role)
            Team(id, name, invite_code)
            TeamMember(team_id -> Team, user_id -> User)
            Submission(id, team_id -> Team, title, repo_url, demo_url)
            Score(id, submission_id -> Submission, judge_id -> User, criterion, value)
Features:   - Register hackers with t-shirt size and dietary needs
            - Create or join a team with an invite code
            - Submit a project with repository and demo links
            - Let judges score submissions on fixed criteria
            - Rank submissions by average score for the closing ceremony
API:        REST
            POST /teams
            POST /teams/join
            POST /submissions
            POST /submissions/{id}/scores
            GET  /leaderboard
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 17

**Intent:**
call for papers site for a conference with blind review

**Spec:**
```
Type:       Web application (conference CFP and review)
Auth:       Email + password login, roles: author, reviewer, chair
Data model: User(id, name, email, role)
            Paper(id, author_id -> User, title, abstract, pdf_url, status)
            Assignment(id, paper_id -> Paper, reviewer_id -> User)
            Review(id, assignment_id -> Assignment, score, confidence, comments)
Features:   - Submit a paper with abstract and PDF before the deadline
            - Hide author identities from reviewers
            - Let the chair assign reviewers and record conflicts of interest
            - Collect scores and comments from each reviewer
            - Send accept or reject decisions with reviews to authors
API:        REST
            POST /papers
            POST /papers/{id}/assignments
            POST /assignments/{id}/review
            POST /papers/{id}/decision
Storage:    PostgreSQL, S3 (PDFs)
Tech stack: Python, Django
```

---

## Example 18

**Intent:**
peer code review tool for my bootcamp students, they upload code and others comment on lines

**Spec:**
```
Type:       Web application (peer code review)
Auth:       GitHub OAuth login
Data model: Student(id, github_login, cohort)
            Submission(id, student_id -> Student, assignment, created_at)
            File(id, submission_id -> Submission, path, content, language)
            Comment(id, file_id -> File, author_id -> Student, line, body)
Features:   - Upload code files or import them from a GitHub repository
            - Show code with syntax highlighting and line numbers
            - Add comments on a specific line
            - Assign each submission to two random peer reviewers
            - Mark a review as complete
API:        REST
            POST /submissions
            GET  /submissions/{id}/files
            POST /files/{id}/comments
            GET  /reviews/assigned
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Prism.js
```

---

## Example 19

**Intent:**
A/B testing service for websites, add a script and see which version converts better

**Spec:**
```
Type:       Web application (A/B testing SaaS)
Auth:       Email + password login, API key per project
Data model: Account(id, email, password_hash)
            Experiment(id, account_id -> Account, name, status, goal_event)
            Variant(id, experiment_id -> Experiment, name, weight)
            Exposure(id, variant_id -> Variant, visitor_id, seen_at)
            Conversion(id, variant_id -> Variant, visitor_id, converted_at)
Features:   - Create experiments with weighted variants
            - Serve a JavaScript snippet that assigns visitors to a variant consistently
            - Record exposures and goal conversions
            - Calculate conversion rates and statistical significance
            - Stop an experiment and roll out the winner
API:        REST
            POST /experiments
            GET  /assign?experiment={id}&visitor={id}
            POST /events
            GET  /experiments/{id}/results
Storage:    PostgreSQL, ClickHouse (events)
Tech stack: Go, React
```

---

## Example 20

**Intent:**
feature flag service like for toggling features without redeploying, with sdk for node

**Spec:**
```
Type:       Web application (feature flag SaaS)
Auth:       Email + password login, server SDK keys per environment
Data model: Project(id, name)
            Environment(id, project_id -> Project, name, sdk_key)
            Flag(id, project_id -> Project, key, description)
            FlagState(id, flag_id -> Flag, environment_id -> Environment, enabled, rollout_percent, rules_json)
Features:   - Create flags and toggle them per environment
            - Roll out a flag to a percentage of users
            - Target users by attributes with rules
            - Stream flag changes to SDKs over server-sent events
            - Keep an audit log of who changed which flag
API:        REST + SSE
            GET  /sdk/flags
            GET  /sdk/stream
            POST /flags
            PATCH /flags/{id}/environments/{env}
Storage:    PostgreSQL, Redis
Tech stack: Node.js, TypeScript, Fastify, React
```

---

## Example 21

**Intent:**
status page for our saas showing uptime

**Spec:**
```
Type:       Web application (status page)
Auth:       Email + password login for admins
Data model: Component(id, name, group, status)
            Incident(id, title, impact, status, started_at, resolved_at)
            IncidentUpdate(id, incident_id -> Incident, message, posted_at)
            Subscriber(id, email, confirmed)
Features:   - Show the current status of each component
            - Post incidents with timestamped updates
            - Show 90-day uptime bars per component
            - Email subscribers when an incident is opened or resolved
            - Schedule maintenance windows
API:        REST
            GET  /status.json
            POST /incidents
            POST /incidents/{id}/updates
            POST /subscribers
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Jinja2
```

---

## Example 22

**Intent:**
form builder where people drag fields and get a shareable link, responses go into a table

**Spec:**
```
Type:       Web application (form builder)
Auth:       Email + password login
Data model: User(id, email, password_hash)
            Form(id, owner_id -> User, title, slug, fields_json, is_open)
            Response(id, form_id -> Form, answers_json, submitted_at)
Features:   - Build a form by dragging text, choice, date and file fields
            - Mark fields as required and add validation rules
            - Share a public link to fill in the form
            - View responses in a sortable table
            - Export responses to CSV
            - Close a form after a date or response limit
API:        REST
            POST /forms
            PUT  /forms/{id}
            GET  /f/{slug}
            POST /f/{slug}/responses
            GET  /forms/{id}/responses
Storage:    PostgreSQL (JSONB)
Tech stack: TypeScript, React, dnd-kit, Node.js, Express
```

---

## Example 23

**Intent:**
Survey tool with logic jumps (skip question 5 if they answered no to question 2) and charts of the results.

**Spec:**
```
Type:       Web application (survey SaaS)
Auth:       Email + password login
Data model: Survey(id, owner_id, title, status)
            Question(id, survey_id -> Survey, position, kind, text, options_json)
            LogicRule(id, question_id -> Question, answer_value, jump_to_id -> Question)
            Answer(id, response_id, question_id -> Question, value)
Features:   - Create surveys with single choice, multiple choice, scale and text questions
            - Add skip logic rules that jump to a later question
            - Collect anonymous responses through a public link
            - Show bar and pie charts per question
            - Filter results by the answer to another question
API:        REST
            POST /surveys
            POST /surveys/{id}/questions
            POST /surveys/{id}/responses
            GET  /surveys/{id}/results
Storage:    PostgreSQL
Tech stack: Python, Django, Chart.js
```

---

## Example 24

**Intent:**
link in bio page builder

**Spec:**
```
Type:       Web application (link-in-bio pages)
Auth:       Email + password login
Data model: User(id, email, username, avatar_url, bio, theme)
            Link(id, user_id -> User, title, url, position, active)
            Click(id, link_id -> Link, clicked_at, referrer, country)
Features:   - Create a public page at /username with a list of links
            - Reorder links by drag and drop
            - Choose a theme and upload an avatar
            - Count clicks per link with referrer and country
            - Show a 30-day click chart
API:        REST
            GET  /{username}
            POST /links
            PATCH /links/{id}
            GET  /r/{link_id}
            GET  /stats
Storage:    PostgreSQL
Tech stack: Node.js, Next.js, Tailwind CSS
```

---

## Example 25

**Intent:**
like doodle, people pick which times work and we see the best slot

**Spec:**
```
Type:       Web application (scheduling poll)
Data model: Poll(id, title, organiser_email, admin_token, closes_at)
            Option(id, poll_id -> Poll, starts_at, ends_at)
            Vote(id, option_id -> Option, participant_name, answer)
Features:   - Create a poll with candidate time slots without an account
            - Share a link where participants answer yes, maybe or no per slot
            - Show participants' local times based on their timezone
            - Highlight the slot with the most yes answers
            - Let the organiser close the poll and email the chosen time
API:        REST
            POST /polls
            GET  /polls/{id}
            POST /polls/{id}/votes
            POST /polls/{id}/close
Storage:    PostgreSQL
Tech stack: Python, Flask, Alpine.js
```

---

## Example 26

**Intent:**
recipe swap website for my village, people post recipes and others can try them and give feedback

**Spec:**
```
Type:       Web application (community recipe swap)
Auth:       Email + password login
Data model: Member(id, name, email)
            Recipe(id, member_id -> Member, title, ingredients, steps, photo_url, servings)
            TryReport(id, recipe_id -> Recipe, member_id -> Member, rating, note, photo_url)
Features:   - Post a recipe with ingredients, steps and a photo
            - Report that you tried a recipe with a rating and photo
            - Scale ingredient amounts for a different number of servings
            - Show a monthly "most tried" recipe list
            - Print a recipe in a clean format
API:        REST
            GET  /recipes
            POST /recipes
            POST /recipes/{id}/tries
            GET  /recipes/popular
Storage:    SQLite
Tech stack: Python, Flask, Jinja2
```

---

## Example 27

**Intent:**
astronomy club wants observing night planner with weather and who's bringing telescopes

**Spec:**
```
Type:       Web application (observing night planner)
Auth:       Email + password login
Data model: Member(id, name, email)
            Site(id, name, lat, lng, bortle_class)
            Night(id, site_id -> Site, date, status)
            Attendance(id, night_id -> Night, member_id -> Member, telescope)
Features:   - Propose observing nights at saved dark-sky sites
            - Show cloud cover forecast and moon phase for each night
            - Sign up and list the telescope you are bringing
            - Mark a night as cancelled and notify attendees
            - Show which planets are visible that evening
API:        REST
            GET  /nights
            POST /nights
            POST /nights/{id}/attend
            GET  /nights/{id}/forecast
Storage:    PostgreSQL
Tech stack: Python, Django, Open-Meteo API, Skyfield
```

---

## Example 28

**Intent:**
I'm part of a board game group of about 30 people that meets on Thursdays at a pub. People bring games from home but we never know what's coming. I want a site where everyone lists their game collection and can say which games they're bringing this week so others can request to play.

**Spec:**
```
Type:       Web application (board game group)
Auth:       Email + password login
Data model: Member(id, name, email)
            Game(id, title, min_players, max_players, play_minutes)
            Ownership(member_id -> Member, game_id -> Game)
            Meetup(id, date)
            Bringing(id, meetup_id -> Meetup, member_id -> Member, game_id -> Game)
            PlayRequest(id, bringing_id -> Bringing, member_id -> Member)
Features:   - Add games to your collection by searching titles
            - Mark which games you are bringing to this Thursday's meetup
            - Request to play a game that someone is bringing
            - Show how many requests each game has
            - Browse the combined group collection by player count
API:        REST
            GET  /games?players={n}
            POST /collection
            POST /meetups/{id}/bringing
            POST /bringing/{id}/requests
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 29

**Intent:**
community garden plot booking and waitlist

**Spec:**
```
Type:       Web application (community garden management)
Auth:       Email + password login, coordinator role
Data model: Gardener(id, name, email, phone)
            Plot(id, number, size_m2, has_water)
            Assignment(id, plot_id -> Plot, gardener_id -> Gardener, season, fee_paid)
            WaitlistEntry(id, gardener_id -> Gardener, joined_at)
Features:   - Show a map of plots and which are free
            - Join the waitlist when no plot is available
            - Offer freed plots to the first person on the waitlist by email
            - Track yearly fee payments
            - Post shared work-day announcements
API:        REST
            GET  /plots
            POST /waitlist
            POST /plots/{id}/assign
            GET  /announcements
Storage:    PostgreSQL
Tech stack: PHP, Symfony, Twig
```

---

## Example 30

**Intent:**
hey i want site for my running club, we post routes and people join runs. we are in Brasil, must be in portuguese also

**Spec:**
```
Type:       Web application (running club)
Auth:       Email + password login, Strava OAuth (optional)
Data model: Runner(id, name, email, pace_min_per_km, language)
            Route(id, name, distance_km, gpx_url)
            GroupRun(id, route_id -> Route, starts_at, meeting_point, pace_group)
            Signup(run_id -> GroupRun, runner_id -> Runner)
Features:   - Upload routes as GPX files and show them on a map
            - Schedule group runs with meeting point and pace group
            - Sign up for a run and see who else is coming
            - Switch the interface between Portuguese and English
            - Send a reminder notification the evening before a run
API:        REST
            GET  /runs
            POST /runs
            POST /runs/{id}/signup
            POST /routes
Storage:    PostgreSQL, S3 (GPX files)
Tech stack: Python, Django (i18n), Leaflet
```

---

## Example 31

**Intent:**
knitting pattern sharing site with a row counter

**Spec:**
```
Type:       Web application (knitting pattern sharing)
Auth:       Email + password login
Data model: User(id, username, email)
            Pattern(id, author_id -> User, title, yarn_weight, needle_size, difficulty, pdf_url)
            Project(id, user_id -> User, pattern_id -> Pattern, current_row, notes)
Features:   - Upload a pattern with yarn, needle and difficulty details
            - Search patterns by yarn weight and difficulty
            - Start a project from a pattern
            - Count rows with a large tap-friendly counter saved to the project
            - Favourite patterns to a queue
API:        REST
            GET  /patterns
            POST /patterns
            POST /projects
            PATCH /projects/{id}/row
Storage:    PostgreSQL, S3 (PDFs)
Tech stack: Ruby on Rails, Stimulus
```

---

## Example 32

**Intent:**
we need a way for food bank helpers to pick their warehouse shifts online

**Spec:**
```
Type:       Web application (volunteer scheduling)
Auth:       Email + password login, coordinator role
Data model: Volunteer(id, name, email, phone)
            Shift(id, role, starts_at, ends_at, slots)
            ShiftSignup(id, shift_id -> Shift, volunteer_id -> Volunteer, attended)
Features:   - Show upcoming shifts with remaining slots
            - Sign up for or cancel a shift
            - Send SMS reminders 24 hours before a shift
            - Mark attendance after the shift
            - Report total volunteer hours per month
API:        REST
            GET  /shifts
            POST /shifts/{id}/signups
            DELETE /signups/{id}
            GET  /reports/hours
Storage:    PostgreSQL
Tech stack: Node.js, Express, Twilio API, Vue.js
```

---

## Example 33

**Intent:**
seed swapping between gardeners by mail

**Spec:**
```
Type:       Web application (seed swap)
Auth:       Email + password login
Data model: Member(id, name, email, postal_address, country)
            SeedListing(id, member_id -> Member, plant, variety, quantity, harvest_year)
            Trade(id, from_id -> Member, to_id -> Member, status)
            TradeItem(trade_id -> Trade, listing_id -> SeedListing)
Features:   - List seeds you have available with variety and harvest year
            - Search seeds by plant and variety
            - Propose a trade of your seeds for someone else's
            - Reveal postal addresses only after both sides accept
            - Mark trades as sent and received
API:        REST
            GET  /listings
            POST /listings
            POST /trades
            PATCH /trades/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 34

**Intent:**
Build me a minimal changelog page SaaS where product teams post release notes and users can subscribe.

**Spec:**
```
Type:       Web application (changelog SaaS)
Auth:       Email + password login for team members
Data model: Workspace(id, name, slug, custom_domain)
            Entry(id, workspace_id -> Workspace, title, body_md, label, published_at)
            Subscriber(id, workspace_id -> Workspace, email, confirmed)
Features:   - Write release notes in Markdown with labels (new, fixed, improved)
            - Publish a public changelog page per workspace
            - Show an embeddable "what's new" widget
            - Email subscribers when a new entry is published
            - Serve an RSS feed of entries
API:        REST
            GET  /{slug}
            POST /entries
            GET  /{slug}/rss.xml
            POST /{slug}/subscribe
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Sidekiq
```

---

## Example 35

**Intent:**
public roadmap and feature voting board for my app users

**Spec:**
```
Type:       Web application (feedback and roadmap board)
Auth:       Email login for voters, admin login for the team
Data model: User(id, email, name)
            Idea(id, author_id -> User, title, description, status, vote_count)
            Vote(idea_id -> Idea, user_id -> User)
            Comment(id, idea_id -> Idea, user_id -> User, body)
Features:   - Submit feature ideas and comment on them
            - Upvote ideas once per user
            - Move ideas through planned, in progress and done columns
            - Merge duplicate ideas and their votes
            - Notify voters when an idea is shipped
API:        REST
            GET  /ideas?sort=votes
            POST /ideas
            POST /ideas/{id}/vote
            PATCH /ideas/{id}
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView
```

---

## Example 36

**Intent:**
website to rate and review local hiking trails conditions, like mud or snow, updated by hikers

**Spec:**
```
Type:       Web application (trail condition reports)
Auth:       Email + password login
Data model: Hiker(id, name, email)
            Trail(id, name, region, length_km, elevation_gain_m, lat, lng)
            Report(id, trail_id -> Trail, hiker_id -> Hiker, condition, notes, photo_url, hiked_on)
Features:   - Browse trails on a map by region
            - Post a condition report (dry, muddy, snow, ice, blocked)
            - Show the latest condition and report age on each trail
            - Upvote helpful reports
            - Follow trails to get notified of new reports
API:        REST
            GET  /trails
            GET  /trails/{id}/reports
            POST /trails/{id}/reports
            POST /trails/{id}/follow
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django, Leaflet
```

---

## Example 37

**Intent:**
open mic night signup sheet online

**Spec:**
```
Type:       Web application (open mic signup)
Auth:       Host login with password
Data model: Event(id, venue, date, slot_minutes, slots)
            Performer(id, event_id -> Event, name, act_type, position, performed)
Features:   - Create an open mic night with a number of time slots
            - Let performers add their name and act type to the list
            - Reorder the running order by drag and drop
            - Show a live "now performing / up next" screen
            - Mark performers as done
API:        REST
            POST /events
            POST /events/{id}/performers
            PATCH /performers/{id}
            GET  /events/{id}/now
Storage:    SQLite
Tech stack: Node.js, Express, Socket.IO
```

---

## Example 38

**Intent:**
my church choir need place to share sheet music and practice recordings per voice part (soprano alto tenor bass)

**Spec:**
```
Type:       Web application (choir rehearsal library)
Auth:       Email + password login, director role
Data model: Singer(id, name, email, voice_part)
            Piece(id, title, composer, sheet_pdf_url)
            Recording(id, piece_id -> Piece, voice_part, audio_url)
            Rehearsal(id, date, notes)
Features:   - Upload sheet music PDFs for each piece
            - Upload practice recordings per voice part
            - Show each singer the recordings for their voice part first
            - Set the pieces for the next rehearsal
            - Play recordings at slower speed in the browser
API:        REST
            GET  /pieces
            POST /pieces
            POST /pieces/{id}/recordings
            GET  /rehearsals/next
Storage:    PostgreSQL, S3 (PDFs and audio)
Tech stack: PHP, Laravel, Howler.js
```

---

## Example 39

**Intent:**
writing critique circle where you must review others before posting your own

**Spec:**
```
Type:       Web application (writing critique community)
Auth:       Email + password login
Data model: Writer(id, pen_name, email, credits)
            Piece(id, writer_id -> Writer, title, genre, text, word_count, status)
            Critique(id, piece_id -> Piece, critic_id -> Writer, body, rating)
Features:   - Earn credits by writing critiques of other members' pieces
            - Spend credits to submit your own piece to the queue
            - Show pieces in the queue with genre and word count
            - Comment inline on selected passages
            - Rate critiques as helpful to reward good reviewers
API:        REST
            GET  /queue
            POST /pieces
            POST /pieces/{id}/critiques
            POST /critiques/{id}/rate
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 40

**Intent:**
uptime monitor saas that pings urls every minute and alerts on slack

**Spec:**
```
Type:       Web application (uptime monitoring SaaS)
Auth:       Email + password login
Data model: Account(id, email, slack_webhook_url)
            Monitor(id, account_id -> Account, url, interval_s, expected_status)
            Check(id, monitor_id -> Monitor, status_code, latency_ms, ok, checked_at)
            Outage(id, monitor_id -> Monitor, started_at, ended_at)
Features:   - Add URLs to monitor with a check interval
            - Send HTTP checks from a background worker
            - Open an outage after three failed checks in a row
            - Post alerts and recoveries to a Slack webhook
            - Show response time charts and uptime percentage
API:        REST
            POST /monitors
            GET  /monitors/{id}/checks
            GET  /monitors/{id}/uptime
Storage:    PostgreSQL, TimescaleDB
Tech stack: Go, React
```

---

## Example 41

**Intent:**
Sign-up sheet for parents bringing snacks to kids soccer games.

**Spec:**
```
Type:       Web application (team snack schedule)
Data model: Team(id, name, coach_email, share_token)
            Game(id, team_id -> Team, date, opponent, location)
            SnackSignup(id, game_id -> Game, parent_name, item)
Features:   - Add the season's games for a team
            - Share one link with all parents
            - Claim a game to bring snacks
            - Show which games still need a volunteer
            - Email the parent a reminder two days before
API:        REST
            GET  /teams/{token}
            POST /games/{id}/signup
            DELETE /signups/{id}
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 42

**Intent:**
online book club where we pick a book each month by vote and discuss chapters with spoiler protection

**Spec:**
```
Type:       Web application (book club)
Auth:       Email + password login
Data model: Member(id, name, email)
            Book(id, title, author, isbn, chapters)
            Nomination(id, book_id -> Book, month, votes)
            Thread(id, book_id -> Book, chapter)
            Post(id, thread_id -> Thread, member_id -> Member, body)
            Progress(member_id -> Member, book_id -> Book, chapter)
Features:   - Nominate books and vote for next month's pick
            - Look up book details by ISBN from Open Library
            - Open one discussion thread per chapter
            - Hide threads for chapters you have not reached yet
            - Update your reading progress
API:        REST
            POST /nominations
            POST /nominations/{id}/vote
            GET  /books/{id}/threads
            PATCH /progress
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Angular
```

---

## Example 43

**Intent:**
genealogy site where family members add relatives and build a shared tree

**Spec:**
```
Type:       Web application (shared family tree)
Auth:       Email + password login, invite-only
Data model: Account(id, email, name)
            Person(id, first_name, last_name, birth_date, death_date, notes, photo_url)
            Relationship(id, person_a_id -> Person, person_b_id -> Person, kind)
            Edit(id, account_id -> Account, person_id -> Person, changed_at, diff_json)
Features:   - Add people and link them as parent, child or spouse
            - Draw the family tree as an interactive chart
            - Invite relatives by email to contribute
            - Keep a history of edits and allow reverting
            - Export the tree as a GEDCOM file
API:        REST
            GET  /people
            POST /people
            POST /relationships
            GET  /export.ged
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, D3.js
```

---

## Example 44

**Intent:**
platform for local musicians to find bandmates

**Spec:**
```
Type:       Web application (musician matching)
Auth:       Email + password login
Data model: Musician(id, name, email, city, instruments, genres, bio, sample_url)
            Band(id, name, city, genres)
            Opening(id, band_id -> Band, instrument, description)
            Application(id, opening_id -> Opening, musician_id -> Musician, message)
Features:   - Create a musician profile with instruments, genres and a sample track
            - Post band openings for a missing instrument
            - Search musicians and openings by city, genre and instrument
            - Apply to an opening with a message
            - Embed SoundCloud or YouTube samples on profiles
API:        REST
            GET  /musicians
            GET  /openings
            POST /openings
            POST /openings/{id}/applications
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 45

**Intent:**
I'm organising a carpool for parents at my kids school, need somewhere to post who drives when and who has free seats

**Spec:**
```
Type:       Web application (school carpool)
Auth:       Email + password login, invite link per school
Data model: Parent(id, name, email, phone, address_area)
            Ride(id, driver_id -> Parent, date, direction, seats)
            Seat(id, ride_id -> Ride, parent_id -> Parent, child_name)
Features:   - Offer a ride for a date and direction (to or from school)
            - Book a seat for your child on an offered ride
            - Show a weekly calendar of rides and free seats
            - Notify the driver when a seat is booked or cancelled
            - Count how often each parent has driven to keep it fair
API:        REST
            GET  /rides?week={date}
            POST /rides
            POST /rides/{id}/seats
            DELETE /seats/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 46

**Intent:**
repair cafe registration, people bring broken things and volunteers fix them

**Spec:**
```
Type:       Web application (repair cafe)
Auth:       Email + password login for volunteers
Data model: Session(id, date, location)
            Volunteer(id, name, email, skills)
            Item(id, session_id -> Session, owner_name, category, problem, outcome, volunteer_id -> Volunteer)
Features:   - Let visitors register an item before a session
            - Assign items to volunteers by skill (electronics, textiles, bikes)
            - Record whether each item was fixed, partly fixed or not fixed
            - Show statistics of kilograms of waste prevented
            - Print a queue list for the session
API:        REST
            POST /sessions/{id}/items
            PATCH /items/{id}
            GET  /stats
Storage:    PostgreSQL
Tech stack: Python, Flask, Bootstrap
```

---

## Example 47

**Intent:**
meme generator community where you upload templates and others caption them

**Spec:**
```
Type:       Web application (meme community)
Auth:       Email + password login
Data model: User(id, username, email)
            Template(id, uploader_id -> User, name, image_url)
            Meme(id, template_id -> Template, author_id -> User, top_text, bottom_text, image_url, score)
            Vote(meme_id -> Meme, user_id -> User, value)
Features:   - Upload image templates
            - Add caption text to a template and render the final image
            - Upvote or downvote memes
            - Show hot, new and top feeds
            - Report memes for moderation
API:        REST
            GET  /templates
            POST /memes
            POST /memes/{id}/vote
            GET  /feed?sort={hot|new|top}
Storage:    PostgreSQL, S3 (images)
Tech stack: Node.js, Express, Sharp, React
```

---

## Example 48

**Intent:**
wish list site for families so people dont buy same present twice

**Spec:**
```
Type:       Web application (gift wish lists)
Auth:       Email + password login
Data model: User(id, name, email)
            WishList(id, owner_id -> User, title, occasion_date, share_token)
            Wish(id, list_id -> WishList, title, url, price, notes)
            Claim(id, wish_id -> Wish, claimer_id -> User)
Features:   - Create wish lists for birthdays or holidays
            - Add items with a shop link and price
            - Share a list with family by link
            - Claim an item so others see it is taken
            - Hide claims from the list owner to keep the surprise
API:        REST
            POST /lists
            POST /lists/{id}/wishes
            GET  /lists/{token}
            POST /wishes/{id}/claim
Storage:    PostgreSQL
Tech stack: TypeScript, SvelteKit, Prisma
```

---

## Example 49

**Intent:**
discord bot for our dnd group that schedules sessions with a poll and reminds everyone

**Spec:**
```
Type:       Bot (Discord)
Data model: Campaign(id, guild_id, channel_id, name)
            SessionPoll(id, campaign_id -> Campaign, options_json, closes_at)
            Session(id, campaign_id -> Campaign, starts_at)
Features:   - Create a scheduling poll with /schedule and date options
            - Collect votes with emoji reactions
            - Pick the date with the most votes when the poll closes
            - Post reminders 24 hours and 1 hour before the session
            - Show the next session with /next
Storage:    SQLite
Tech stack: Python, discord.py, APScheduler
```

---

## Example 50

**Intent:**
Website for a cosplay community to post builds with progress photos and materials used.

**Spec:**
```
Type:       Web application (cosplay build logs)
Auth:       Email + password login
Data model: Maker(id, username, email)
            Build(id, maker_id -> Maker, character, series, status)
            Step(id, build_id -> Build, title, body, photo_urls, created_at)
            Material(id, build_id -> Build, name, cost)
Features:   - Create a build log for a character costume
            - Add progress steps with photos
            - List materials and total cost
            - Browse builds by series and character
            - Follow makers and see their new steps in a feed
API:        REST
            GET  /builds
            POST /builds
            POST /builds/{id}/steps
            GET  /feed
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Alpine.js
```

---

## Example 51

**Intent:**
Hello, I am teacher in Poland. I want website where my students can find partner for speaking English with student from other school. Is possible?

**Spec:**
```
Type:       Web application (school pen-pal exchange)
Auth:       Teacher accounts with email + password, student accounts created by teachers
Data model: School(id, name, country)
            Teacher(id, school_id -> School, name, email)
            Student(id, school_id -> School, nickname, age, level, interests)
            Pairing(id, student_a_id -> Student, student_b_id -> Student, approved)
            Message(id, pairing_id -> Pairing, sender_id -> Student, body, sent_at)
Features:   - Let teachers register their school and add students
            - Suggest partners from other schools by age, level and interests
            - Require both teachers to approve each pairing
            - Let paired students exchange moderated messages
            - Show teachers all messages from their students
API:        REST
            POST /students
            GET  /pairings/suggestions
            POST /pairings/{id}/approve
            POST /pairings/{id}/messages
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 52

**Intent:**
anonymous Q&A box for my youtube channel

**Spec:**
```
Type:       Web application (anonymous question box)
Auth:       Email + password login for the creator only
Data model: Creator(id, handle, email)
            Question(id, creator_id -> Creator, text, created_at, answered, hidden)
Features:   - Show a public page where anyone can send an anonymous question
            - Rate-limit submissions by IP address
            - Filter questions containing blocked words
            - Mark questions as answered or hidden
            - Generate a shareable image card of a question for videos
API:        REST
            POST /{handle}/questions
            GET  /inbox
            PATCH /questions/{id}
            GET  /questions/{id}/card.png
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, Satori (image cards)
```

---

## Example 53

**Intent:**
ham radio contact logbook shared with my club

**Spec:**
```
Type:       Web application (amateur radio logbook)
Auth:       Email + password login with callsign
Data model: Operator(id, callsign, email, grid_square)
            Contact(id, operator_id -> Operator, their_callsign, frequency_mhz, mode, rst_sent, rst_received, logged_at)
Features:   - Log contacts with frequency, mode and signal reports
            - Import and export logs in ADIF format
            - Show worked countries on a world map
            - Show a club leaderboard of contacts this month
            - Look up a callsign's country from its prefix
API:        REST
            GET  /contacts
            POST /contacts
            POST /contacts/import
            GET  /contacts/export.adi
Storage:    PostgreSQL
Tech stack: Python, Flask, Leaflet
```

---

## Example 54

**Intent:**
puppy playdate matching by dog size and energy level

**Spec:**
```
Type:       Mobile application with backend (dog playdates)
Auth:       Email + password login, Apple and Google sign-in
Data model: Owner(id, name, email, area)
            Dog(id, owner_id -> Owner, name, breed, size, energy_level, vaccinated)
            Playdate(id, host_dog_id -> Dog, guest_dog_id -> Dog, park, starts_at, status)
Features:   - Create profiles for your dogs with size and energy level
            - Find nearby dogs with a similar size and energy
            - Propose a playdate at a park and time
            - Chat with the other owner
            - Require vaccination confirmation before booking
API:        REST
            GET  /dogs/nearby
            POST /playdates
            PATCH /playdates/{id}
            GET  /playdates/{id}/messages
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Node.js, Express
```

---

## Example 55

**Intent:**
Make a site where indie game devs post devlogs and players can follow games

**Spec:**
```
Type:       Web application (indie devlog platform)
Auth:       Email + password login
Data model: User(id, username, email, is_developer)
            Game(id, developer_id -> User, title, genre, cover_url, store_url)
            Devlog(id, game_id -> Game, title, body_md, media_urls, published_at)
            Follow(user_id -> User, game_id -> Game)
Features:   - Create a game page with cover and store link
            - Publish devlog posts with images and GIFs
            - Follow games and see new devlogs in a feed
            - Comment on devlog posts
            - Show follower count on each game
API:        REST
            POST /games
            POST /games/{id}/devlogs
            POST /games/{id}/follow
            GET  /feed
Storage:    PostgreSQL, S3 (media)
Tech stack: Go, HTMX
```

---

## Example 56

**Intent:**
plz make a site for my apartment building where ppl can borrow stuff from each other like a vacuum or extra chairs

**Spec:**
```
Type:       Web application (neighbour item sharing)
Auth:       Email login with building invite code
Data model: Resident(id, name, email, unit_number)
            Item(id, owner_id -> Resident, name, description, photo_url, available)
            BorrowRequest(id, item_id -> Item, borrower_id -> Resident, from_date, to_date, status)
Features:   - Join the building with an invite code
            - List items you are willing to lend
            - Request to borrow an item for a date range
            - Approve or decline requests as the owner
            - Show a "thank you" count on each resident's profile
API:        REST
            GET  /items
            POST /items
            POST /items/{id}/requests
            PATCH /requests/{id}
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 57

**Intent:**
Webinar registration and replay site for a nonprofit.

**Spec:**
```
Type:       Web application (webinar registration)
Auth:       Email + password login for staff
Data model: Webinar(id, title, speaker, starts_at, zoom_link, replay_url)
            Registrant(id, webinar_id -> Webinar, name, email, attended)
Features:   - Publish upcoming webinars with a registration form
            - Send a confirmation email with a calendar invite (.ics)
            - Send the join link one hour before start
            - Post the replay video and email it to registrants
            - Export registrants as CSV
API:        REST
            GET  /webinars
            POST /webinars/{id}/register
            PATCH /webinars/{id}
            GET  /webinars/{id}/registrants.csv
Storage:    PostgreSQL
Tech stack: Node.js, Express, SendGrid API
```

---

## Example 58

**Intent:**
transcribe old handwritten letters crowdsourced, volunteers type what they see

**Spec:**
```
Type:       Web application (crowdsourced transcription)
Auth:       Email + password login, reviewer role
Data model: Collection(id, title, description)
            Page(id, collection_id -> Collection, image_url, status)
            Transcription(id, page_id -> Page, volunteer_id, text, submitted_at)
            Review(id, transcription_id -> Transcription, reviewer_id, approved, notes)
Features:   - Show a scanned page next to a text box with zoom and pan
            - Save transcription drafts and submit them
            - Require two independent transcriptions per page
            - Highlight differences between the two for a reviewer
            - Export approved text as plain text and TEI XML
API:        REST
            GET  /pages/next
            POST /pages/{id}/transcriptions
            POST /transcriptions/{id}/review
            GET  /collections/{id}/export
Storage:    PostgreSQL, S3 (scans)
Tech stack: Python, Django, OpenSeadragon
```

---

## Example 59

**Intent:**
website for our climbing gym where setters post new routes and climbers log sends

**Spec:**
```
Type:       Web application (climbing route log)
Auth:       Email + password login, setter role
Data model: Climber(id, name, email)
            Route(id, wall, grade, color, setter_id -> Climber, set_on, removed_on)
            Send(id, route_id -> Route, climber_id -> Climber, style, sent_on)
            GradeVote(route_id -> Route, climber_id -> Climber, grade)
Features:   - Post new routes with wall, grade and hold colour
            - Log a send as flash, onsight or redpoint
            - Vote on whether a grade feels soft or hard
            - Show each climber's pyramid of grades
            - Archive routes when they are stripped
API:        REST
            GET  /routes?wall={id}
            POST /routes
            POST /routes/{id}/sends
            GET  /climbers/{id}/stats
Storage:    PostgreSQL
Tech stack: TypeScript, Remix, Prisma
```

---

## Example 60

**Intent:**
something to manage our neighbourhood watch, report suspicious activity and alert members

**Spec:**
```
Type:       Mobile application with backend (neighbourhood watch)
Auth:       Phone number login with SMS code, coordinator approval
Data model: Member(id, name, phone, street, approved)
            Report(id, member_id -> Member, category, description, lat, lng, photo_url, created_at)
            Alert(id, report_id -> Report, sent_at)
Features:   - Submit a report with category, location and photo
            - Let coordinators turn a report into an alert
            - Send push notifications to members in the area
            - Show recent reports on a map
            - Remove reports older than 30 days
API:        REST
            POST /reports
            GET  /reports
            POST /reports/{id}/alert
Storage:    PostgreSQL
Tech stack: Flutter, Firebase Cloud Messaging, Python, FastAPI
```

---

## Example 61

**Intent:**
i want a website for a quiz night league between pubs, teams get points each week and theres a table

**Spec:**
```
Type:       Web application (pub quiz league)
Auth:       Email + password login for quizmasters
Data model: Pub(id, name, address)
            Team(id, name, home_pub_id -> Pub)
            QuizNight(id, pub_id -> Pub, date)
            Result(id, quiz_night_id -> QuizNight, team_id -> Team, score, position)
Features:   - Enter scores for each team after a quiz night
            - Award league points by finishing position
            - Show the season league table
            - Show each team's history and best score
            - Start a new season and archive the old table
API:        REST
            POST /quiz-nights
            POST /quiz-nights/{id}/results
            GET  /league?season={year}
            GET  /teams/{id}
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Livewire
```

---

## Example 62

**Intent:**
platform where makers rent time on shared 3D printers and laser cutters at our makerspace

**Spec:**
```
Type:       Web application (makerspace equipment booking)
Auth:       Email + password login, membership check
Data model: Member(id, name, email, membership_level)
            Machine(id, name, kind, hourly_rate, requires_training)
            Training(member_id -> Member, machine_id -> Machine, passed_on)
            Booking(id, machine_id -> Machine, member_id -> Member, starts_at, ends_at)
Features:   - Show a calendar of each machine's bookings
            - Book time only on machines you are trained on
            - Prevent overlapping bookings
            - Charge machine time to the member's account at month end
            - Let staff record training sign-offs
API:        REST
            GET  /machines/{id}/bookings
            POST /bookings
            POST /trainings
            GET  /invoices/{month}
Storage:    PostgreSQL
Tech stack: Python, Django, FullCalendar
```

---

## Example 63

**Intent:**
memorial website where friends post memories and photos of someone who passed away

**Spec:**
```
Type:       Web application (online memorial)
Auth:       Email + password login for the family admin
Data model: Memorial(id, name, born_on, died_on, bio, slug, is_private, password_hash)
            Memory(id, memorial_id -> Memorial, author_name, text, photo_url, approved)
Features:   - Create a memorial page with photo and life story
            - Let visitors post memories and photos
            - Moderate posts before they appear
            - Optionally protect the page with a password
            - Show a photo slideshow of all approved memories
API:        REST
            GET  /m/{slug}
            POST /m/{slug}/memories
            PATCH /memories/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Next.js
```

---

## Example 64

**Intent:**
customer interview scheduling and notes tool for startup founders

**Spec:**
```
Type:       Web application (customer research)
Auth:       Google sign-in
Data model: Founder(id, email, google_token)
            Contact(id, founder_id -> Founder, name, company, email)
            Interview(id, contact_id -> Contact, scheduled_at, notes, recording_url)
            Insight(id, interview_id -> Interview, quote, tag)
Features:   - Share a booking link that syncs with Google Calendar
            - Take notes during an interview with a timer
            - Highlight quotes and tag them as insights
            - Group insights by tag across all interviews
            - Search all notes and quotes
API:        REST
            GET  /book/{founder}
            POST /interviews
            POST /interviews/{id}/insights
            GET  /insights?tag={tag}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Google Calendar API
```

---

## Example 65

**Intent:**
Embeddable comment section for static blogs (like a self-hosted alternative), written in Go.

**Spec:**
```
Type:       Web application (embeddable comments)
Auth:       Optional GitHub or email login for commenters, admin password
Data model: Site(id, domain, owner_email)
            Thread(id, site_id -> Site, page_url)
            Comment(id, thread_id -> Thread, parent_id -> Comment, author, body, approved, created_at)
Features:   - Embed comments on any page with one script tag
            - Reply to comments in nested threads
            - Hold first-time commenters for moderation
            - Filter spam with a honeypot field and rate limits
            - Email the site owner about new comments
API:        REST
            GET  /api/threads?url={page}
            POST /api/comments
            PATCH /api/comments/{id}
Storage:    SQLite
Tech stack: Go, vanilla JavaScript widget
```

---

## Example 66

**Intent:**
mutual aid board for requests and offers in our town

**Spec:**
```
Type:       Web application (mutual aid board)
Auth:       Phone or email login
Data model: Neighbor(id, name, contact, area)
            Post(id, neighbor_id -> Neighbor, kind, category, description, urgent, status, created_at)
            Response(id, post_id -> Post, helper_id -> Neighbor, message)
Features:   - Post a request or offer for groceries, rides, childcare or other help
            - Mark requests as urgent
            - Respond to a post and connect privately
            - Close posts when the need is met
            - Show the board in a simple low-bandwidth layout
API:        REST
            GET  /posts?kind={request|offer}
            POST /posts
            POST /posts/{id}/responses
            PATCH /posts/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, plain HTML
```

---

## Example 67

**Intent:**
ok so I collect vinyl records and theres a group of us that trade and sell between us, we use a whatsapp group but nobody can find anything. could you spec out a site where each person lists their records with condition and price and others can make offers

**Spec:**
```
Type:       Web application (record collectors trading)
Auth:       Email + password login, invite-only
Data model: Collector(id, name, email, city)
            Record(id, collector_id -> Collector, artist, title, label, year, media_grade, sleeve_grade, price, for_trade)
            Offer(id, record_id -> Record, from_id -> Collector, amount, trade_record_id -> Record, status)
Features:   - List records with Goldmine grades for media and sleeve
            - Fill record details from the Discogs database
            - Make a cash offer or offer a trade from your own list
            - Accept, decline or counter an offer
            - Search all members' records by artist and label
API:        REST
            GET  /records?artist={name}
            POST /records
            POST /records/{id}/offers
            PATCH /offers/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Discogs API
```

---

## Example 68

**Intent:**
lightweight incident postmortem tool for dev teams

**Spec:**
```
Type:       Web application (postmortem documents)
Auth:       Google Workspace SSO
Data model: Incident(id, title, severity, started_at, resolved_at, owner)
            TimelineEvent(id, incident_id -> Incident, happened_at, description)
            ActionItem(id, incident_id -> Incident, description, assignee, due_on, done)
Features:   - Create a postmortem from a template with summary, impact and root cause
            - Build a timeline of events with timestamps
            - Track action items with owners and due dates
            - Remind owners of overdue action items
            - Search past incidents by service and severity
API:        REST
            POST /incidents
            POST /incidents/{id}/timeline
            POST /incidents/{id}/actions
            GET  /incidents?severity={level}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 69

**Intent:**
plant cutting exchange for houseplant lovers

**Spec:**
```
Type:       Web application (plant cutting exchange)
Auth:       Email + password login
Data model: Member(id, username, email, city)
            Plant(id, member_id -> Member, species, cultivar, photo_url, cuttings_available)
            Wanted(id, member_id -> Member, species)
            Exchange(id, giver_id -> Member, receiver_id -> Member, plant_id -> Plant, status)
Features:   - List plants you can give cuttings from
            - Add species to your wanted list
            - Notify you when someone nearby lists a wanted species
            - Arrange local pickup exchanges
            - Show care tips for each species
API:        REST
            GET  /plants?near={city}
            POST /plants
            POST /wanted
            POST /exchanges
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 70

**Intent:**
scavenger hunt app for team building, teams solve clues at locations

**Spec:**
```
Type:       Mobile application with backend (scavenger hunt)
Auth:       Join code per team
Data model: Hunt(id, name, starts_at, ends_at)
            Clue(id, hunt_id -> Hunt, order, text, answer, lat, lng, radius_m)
            Team(id, hunt_id -> Hunt, name, join_code)
            Solve(id, team_id -> Team, clue_id -> Clue, solved_at, photo_url)
Features:   - Let organisers create hunts with clues and locations
            - Unlock a clue only when the team is within its radius
            - Accept answers by text or photo proof
            - Show a live leaderboard by clues solved and time
            - Give hints at a points penalty
API:        REST
            POST /hunts
            GET  /teams/{id}/current-clue
            POST /clues/{id}/solve
            GET  /hunts/{id}/leaderboard
Storage:    PostgreSQL
Tech stack: React Native, Expo Location, Node.js
```

---

## Example 71

**Intent:**
coworking desk booking for our small shared office, Laravel please

**Spec:**
```
Type:       Web application (desk booking)
Auth:       Email + password login
Data model: Member(id, name, email, plan)
            Desk(id, label, zone, has_monitor)
            Booking(id, desk_id -> Desk, member_id -> Member, date)
Features:   - Show a floor plan with free and booked desks for a day
            - Book a desk for one or more days
            - Limit bookings per week by membership plan
            - Cancel bookings up to the day before
            - Show who is in the office today
API:        REST
            GET  /desks?date={date}
            POST /bookings
            DELETE /bookings/{id}
            GET  /today
Storage:    MySQL
Tech stack: PHP, Laravel, Alpine.js
```

---

## Example 72

**Intent:**
Write a spec for a 'buy nothing' gifting group site: people give things away free, and recipients are chosen by the giver rather than first-come.

**Spec:**
```
Type:       Web application (free gifting group)
Auth:       Email + password login, group invite
Data model: Member(id, name, email, neighbourhood)
            Gift(id, giver_id -> Member, title, description, photo_url, status, picks_at)
            Interest(id, gift_id -> Gift, member_id -> Member, note)
Features:   - Post an item to give away with a pick time
            - Express interest with a short note
            - Let the giver choose a recipient or pick randomly
            - Hide the interest list order to avoid first-come pressure
            - Post "asks" for things you need
API:        REST
            GET  /gifts
            POST /gifts
            POST /gifts/{id}/interest
            POST /gifts/{id}/choose
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Turbo
```

---

## Example 73

**Intent:**
pickup basketball court finder, who is playing now

**Spec:**
```
Type:       Mobile application with backend (pickup games)
Auth:       Email or Google sign-in
Data model: Player(id, name, skill_level)
            Court(id, name, lat, lng, surface, lights)
            CheckIn(id, court_id -> Court, player_id -> Player, checked_in_at, expires_at)
            Game(id, court_id -> Court, starts_at, needed_players)
Features:   - Show nearby courts on a map with number of players checked in
            - Check in at a court for two hours
            - Post a game time and how many players are needed
            - Add new courts with photos
            - Notify you when a game starts at a favourite court
API:        REST
            GET  /courts?near={lat,lng}
            POST /courts/{id}/checkins
            POST /courts/{id}/games
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin (Android), Swift (iOS), Go backend
```

---

## Example 74

**Intent:**
newsletter for a local farmers market is covered, but I need a vendor application and stall assignment system

**Spec:**
```
Type:       Web application (market vendor management)
Auth:       Email + password login, manager role
Data model: Vendor(id, business_name, email, products, insurance_doc_url)
            Application(id, vendor_id -> Vendor, season, status)
            Stall(id, number, size, has_power)
            Assignment(id, stall_id -> Stall, vendor_id -> Vendor, market_date)
Features:   - Let vendors apply for a season with product list and insurance proof
            - Approve or reject applications
            - Assign stalls per market day on a drag-and-drop map
            - Collect stall fees online
            - Email vendors their stall number each week
API:        REST
            POST /applications
            PATCH /applications/{id}
            POST /assignments
            GET  /market-days/{date}/map
Storage:    PostgreSQL, S3 (documents)
Tech stack: Python, Django, Stripe API
```

---

## Example 75

**Intent:**
tournament bracket maker for esports with check-in

**Spec:**
```
Type:       Web application (tournament brackets)
Auth:       Email + password login, Discord sign-in
Data model: Tournament(id, name, game, format, starts_at, organiser_id)
            Participant(id, tournament_id -> Tournament, name, seed, checked_in)
            Match(id, tournament_id -> Tournament, round, slot, p1_id -> Participant, p2_id -> Participant, score1, score2, winner_id -> Participant)
Features:   - Create single or double elimination tournaments
            - Open check-in 30 minutes before start
            - Seed participants and generate the bracket
            - Report match scores and advance winners
            - Show a live bracket page for spectators
API:        REST
            POST /tournaments
            POST /tournaments/{id}/checkin
            POST /tournaments/{id}/start
            PATCH /matches/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, React
```

---

## Example 76

**Intent:**
helping elderly with tech, volunteers sign up and seniors book help sessions by phone or site

**Spec:**
```
Type:       Web application (tech help for seniors)
Auth:       Email + password login for volunteers and staff
Data model: Volunteer(id, name, email, skills, availability)
            Senior(id, name, phone, address)
            HelpSession(id, senior_id -> Senior, volunteer_id -> Volunteer, topic, scheduled_at, mode, outcome)
Features:   - Let seniors request help with a large-text simple form
            - Let staff book sessions on behalf of seniors who call
            - Match requests with volunteers by skill and availability
            - Send SMS confirmations to seniors
            - Record session outcomes and follow-up needs
API:        REST
            POST /requests
            GET  /volunteers/available
            POST /sessions
            PATCH /sessions/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio API
```

---

## Example 77

**Intent:**
i need a waitlist landing page for my startup with referral links that move you up the list

**Spec:**
```
Type:       Web application (viral waitlist)
Auth:       Email + password login for admin
Data model: Signup(id, email, referral_code, referred_by_id -> Signup, position, confirmed, created_at)
Features:   - Collect emails on a landing page with double opt-in
            - Give each signup a unique referral link
            - Move a signup up 5 places per confirmed referral
            - Show the user their current position and referral count
            - Export the list and invite the top N users
API:        REST
            POST /signups
            GET  /signups/confirm?token={token}
            GET  /me/{referral_code}
            POST /admin/invite
Storage:    PostgreSQL
Tech stack: Node.js, Next.js, Resend API
```

---

## Example 78

**Intent:**
directory of local therapists filterable by language and specialty, for our immigrant community center

**Spec:**
```
Type:       Web application (provider directory)
Auth:       Email + password login for providers and admins
Data model: Provider(id, name, email, specialties, languages, accepts_insurance, sliding_scale, address, verified)
            Inquiry(id, provider_id -> Provider, name, email, message, sent_at)
Features:   - Search providers by language, specialty and insurance
            - Show providers who offer sliding-scale fees
            - Let providers create and update their own listing
            - Require admin verification of licenses before publishing
            - Translate the interface into several community languages
API:        REST
            GET  /providers?language={code}&specialty={name}
            POST /providers
            PATCH /providers/{id}/verify
            POST /providers/{id}/inquiries
Storage:    PostgreSQL
Tech stack: Python, Django (i18n)
```

---

## Example 79

**Intent:**
Telegram bot for our english speaking club, it gives daily topic and collect who come to meeting

**Spec:**
```
Type:       Bot (Telegram)
Data model: Member(id, telegram_id, name)
            Topic(id, text, used_on)
            Meeting(id, date, place)
            Attendance(meeting_id -> Meeting, member_id -> Member, going)
Features:   - Post a daily conversation topic to the group chat
            - Announce the next meeting with "going" and "not going" buttons
            - Count attendees and show the list with /who
            - Let admins add topics with /addtopic
            - Avoid repeating topics until all have been used
Storage:    SQLite
Tech stack: Python, python-telegram-bot
```

---

## Example 80

**Intent:**
ride share board for festival goers

**Spec:**
```
Type:       Web application (festival ride sharing)
Auth:       Email + password login
Data model: User(id, name, email, phone)
            Festival(id, name, location, dates)
            Ride(id, festival_id -> Festival, driver_id -> User, from_city, departs_at, seats, cost_share)
            Passenger(ride_id -> Ride, user_id -> User, status)
Features:   - Offer a ride to a festival with departure city and cost share
            - Search rides by festival and starting city
            - Request a seat and wait for driver approval
            - Share phone numbers only after approval
            - Post a "looking for a ride" request
API:        REST
            GET  /festivals/{id}/rides
            POST /rides
            POST /rides/{id}/passengers
            PATCH /passengers/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 81

**Intent:**
API for a feedback widget, other websites post user feedback and screenshots to it

**Spec:**
```
Type:       REST API service (feedback collection)
Auth:       Public project key for submissions, secret key for reading
Data model: Project(id, name, public_key, secret_key_hash)
            Feedback(id, project_id -> Project, message, rating, page_url, user_agent, screenshot_url, created_at)
Features:   - Accept feedback with message, rating and page URL
            - Accept a screenshot upload as base64 PNG
            - Restrict submissions to the project's allowed origins (CORS)
            - List and filter feedback for a project
            - Forward new feedback to a Slack webhook
API:        REST
            POST /v1/feedback
            GET  /v1/projects/{id}/feedback
            DELETE /v1/feedback/{id}
Storage:    PostgreSQL, S3 (screenshots)
Tech stack: Go, chi router
```

---

## Example 82

**Intent:**
church small group finder with leader contacts

**Spec:**
```
Type:       Web application (small group directory)
Auth:       Email + password login for leaders and staff
Data model: Group(id, name, leader_name, leader_email, day, time, area, audience, open)
            JoinRequest(id, group_id -> Group, name, email, message)
Features:   - Browse groups by day, area and audience (young adults, families)
            - Show only groups open to new members
            - Send a join request to the leader by email
            - Let leaders edit their group and close it when full
API:        REST
            GET  /groups
            POST /groups/{id}/join-requests
            PATCH /groups/{id}
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 83

**Intent:**
movie night voting for friends, everyone suggests and we rank choice vote

**Spec:**
```
Type:       Web application (group movie vote)
Data model: Room(id, code, host_name, status)
            Suggestion(id, room_id -> Room, title, tmdb_id, poster_url)
            Ballot(id, room_id -> Room, voter_name, ranking_json)
Features:   - Create a room and share its code
            - Suggest movies with search from TMDB
            - Rank all suggestions by drag and drop
            - Count ballots with instant-runoff voting
            - Reveal the winner with round-by-round results
API:        REST
            POST /rooms
            POST /rooms/{code}/suggestions
            POST /rooms/{code}/ballots
            GET  /rooms/{code}/result
Storage:    Redis
Tech stack: Node.js, Express, Svelte, TMDB API
```

---

## Example 84

**Intent:**
customer loyalty stamp card SaaS for coffee shops, no app download needed

**Spec:**
```
Type:       Web application (digital loyalty cards)
Auth:       Email + password login for shop owners, phone number for customers
Data model: Shop(id, name, stamps_for_reward, reward_text)
            Customer(id, phone)
            Card(id, shop_id -> Shop, customer_id -> Customer, stamps, rewards_redeemed)
            Stamp(id, card_id -> Card, staff_pin, added_at)
Features:   - Let customers open their card by scanning a QR code at the counter
            - Add a stamp when staff enter their PIN
            - Unlock a reward when the card is full
            - Show owners visits and redemptions per week
            - Add the card to Apple Wallet or Google Wallet
API:        REST
            GET  /s/{shop}/card
            POST /cards/{id}/stamps
            POST /cards/{id}/redeem
            GET  /shops/{id}/stats
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 85

**Intent:**
place for retired engineers to volunteer advice to small businesses

**Spec:**
```
Type:       Web application (pro bono expert matching)
Auth:       Email + password login
Data model: Expert(id, name, email, field, years_experience, bio)
            Business(id, name, email, sector)
            Question(id, business_id -> Business, field, title, details, status)
            Answer(id, question_id -> Question, expert_id -> Expert, body)
            Call(id, question_id -> Question, expert_id -> Expert, scheduled_at)
Features:   - Let businesses post a question in a field
            - Notify experts in that field of new questions
            - Answer in writing or offer a video call
            - Rate the help received
            - Show experts their total volunteer hours
API:        REST
            POST /questions
            GET  /questions?field={name}
            POST /questions/{id}/answers
            POST /questions/{id}/calls
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Thymeleaf
```

---

## Example 86

**Intent:**
I want a GraphQL backend for a fan wiki of a TV show's characters and episodes

**Spec:**
```
Type:       GraphQL API service (fan database)
Auth:       JWT login for editors, public read access
Data model: Character(id, name, actor, description, first_episode_id -> Episode)
            Episode(id, season, number, title, air_date, synopsis)
            Appearance(character_id -> Character, episode_id -> Episode)
            Quote(id, character_id -> Character, episode_id -> Episode, text)
Features:   - Query characters with their appearances and quotes
            - Query episodes by season with the characters in them
            - Let editors create and update entries with mutations
            - Search quotes by text
            - Paginate lists with cursors
API:        GraphQL
            POST /graphql
Storage:    PostgreSQL
Tech stack: Node.js, Apollo Server, Prisma
```

---

## Example 87

**Intent:**
anonymous salary sharing site for designers in my country

**Spec:**
```
Type:       Web application (salary transparency)
Auth:       Optional email verification to mark entries as verified
Data model: Entry(id, role, seniority, city, company_size, salary_gross, currency, years_experience, verified, submitted_at)
Features:   - Submit salary data without an account
            - Show median and range per role and seniority
            - Filter by city and company size
            - Hide groups with fewer than 5 entries to protect anonymity
            - Remove outliers before computing statistics
API:        REST
            POST /entries
            GET  /stats?role={role}&city={city}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Svelte
```

---

## Example 88

**Intent:**
reading challenge for our library kids in summer, they log books and get badges

**Spec:**
```
Type:       Web application (summer reading challenge)
Auth:       Parent account with email + password, child profiles under it
Data model: Parent(id, email, password_hash)
            Child(id, parent_id -> Parent, first_name, age_group)
            BookLog(id, child_id -> Child, title, minutes, logged_on)
            Badge(id, name, rule, icon_url)
            EarnedBadge(child_id -> Child, badge_id -> Badge, earned_on)
Features:   - Log books and reading minutes for each child
            - Award badges at minute and book milestones
            - Show a progress bar toward the summer goal
            - Let librarians print certificates for finishers
            - Report total minutes per branch
API:        REST
            POST /children/{id}/logs
            GET  /children/{id}/badges
            GET  /admin/report
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 89

**Intent:**
Hi, we are small company making online escape rooms. We need booking site where groups choose time and pay, and game master see schedule.

**Spec:**
```
Type:       Web application (escape room booking)
Auth:       Email + password login for game masters
Data model: Room(id, name, max_players, duration_min, price)
            Slot(id, room_id -> Room, starts_at, game_master_id)
            Booking(id, slot_id -> Slot, contact_email, players, paid, meeting_link)
Features:   - Show available slots per room in a calendar
            - Book a slot for a group and pay online
            - Send the video meeting link after payment
            - Show game masters their daily schedule
            - Let customers reschedule up to 24 hours before
API:        REST
            GET  /rooms/{id}/slots
            POST /bookings
            POST /webhooks/stripe
            GET  /schedule?date={date}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Stripe API, Vue.js
```

---

## Example 90

**Intent:**
open data portal for our city council datasets

**Spec:**
```
Type:       Web application (open data portal)
Auth:       Email + password login for publishers
Data model: Dataset(id, title, description, publisher, license, tags, updated_at)
            Resource(id, dataset_id -> Dataset, format, file_url, size_bytes)
            Download(id, resource_id -> Resource, downloaded_at)
Features:   - Publish datasets with description, license and tags
            - Upload CSV, JSON and GeoJSON resources
            - Preview CSV files as a table and GeoJSON on a map
            - Search datasets by keyword and tag
            - Provide an API to fetch dataset metadata
API:        REST
            GET  /api/datasets
            GET  /api/datasets/{id}
            POST /api/datasets
            POST /api/datasets/{id}/resources
Storage:    PostgreSQL, S3 (files)
Tech stack: Python, Django, Leaflet
```

---

## Example 91

**Intent:**
leaderboard site for speedrunners of my own small game

**Spec:**
```
Type:       Web application (speedrun leaderboard)
Auth:       Email + password login, moderator role
Data model: Runner(id, username, email, country)
            Category(id, name, rules)
            Run(id, runner_id -> Runner, category_id -> Category, time_ms, video_url, status, submitted_at)
Features:   - Submit a run with time and a video link
            - Let moderators verify or reject runs
            - Show leaderboards per category with only each runner's best time
            - Show world record history as a chart
            - Embed YouTube or Twitch video on each run page
API:        REST
            GET  /categories/{id}/leaderboard
            POST /runs
            PATCH /runs/{id}
Storage:    PostgreSQL
Tech stack: Go, Templ, HTMX
```

---

## Example 92

**Intent:**
dev team standup bot in slack that asks 3 questions async and posts summary

**Spec:**
```
Type:       Bot (Slack)
Data model: Team(id, slack_channel_id, timezone, ask_at)
            Member(id, team_id -> Team, slack_user_id)
            Answer(id, member_id -> Member, date, yesterday, today, blockers)
Features:   - Send each member a DM with the three standup questions at a set time
            - Collect answers in a Slack modal
            - Post a combined summary to the team channel
            - Highlight blockers at the top of the summary
            - Skip weekends and members on leave
Storage:    PostgreSQL
Tech stack: Node.js, Slack Bolt
```

---

## Example 93

**Intent:**
online auction for a school fundraiser, parents bid on donated items

**Spec:**
```
Type:       Web application (charity silent auction)
Auth:       Email + password login
Data model: Bidder(id, name, email, phone)
            Item(id, title, donor, description, photo_url, starting_bid, increment, closes_at)
            Bid(id, item_id -> Item, bidder_id -> Bidder, amount, placed_at)
Features:   - Show donated items with current highest bid
            - Place bids that respect the minimum increment
            - Send an email when you are outbid
            - Close all items at a set time and email winners
            - Show organisers a total raised and unpaid winners list
API:        REST
            GET  /items
            POST /items/{id}/bids
            GET  /admin/totals
Storage:    PostgreSQL
Tech stack: Python, Django, Django Channels (live updates)
```

---

## Example 94

**Intent:**
moderated forum for parents of kids with diabetes is too generic, I specifically want a meal carb counting library shared by the parents

**Spec:**
```
Type:       Web application (shared carb counting library)
Auth:       Email + password login
Data model: Parent(id, name, email)
            Food(id, name, brand, carbs_per_100g, verified)
            Meal(id, parent_id -> Parent, name, photo_url)
            MealItem(meal_id -> Meal, food_id -> Food, grams)
Features:   - Search a shared food list with carbs per 100 g
            - Add foods and let other parents confirm the values
            - Build a meal from foods with gram amounts
            - Calculate total carbs per meal and per portion
            - Save favourite meals for quick reuse
API:        REST
            GET  /foods?q={name}
            POST /foods
            POST /meals
            GET  /meals/{id}/carbs
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 95

**Intent:**
platform for local bands to sell gig tickets

**Spec:**
```
Type:       Web application (gig ticketing)
Auth:       Email + password login for bands and venues
Data model: Band(id, name, email)
            Gig(id, band_id -> Band, venue, starts_at, capacity, price)
            Ticket(id, gig_id -> Gig, buyer_email, code, scanned)
Features:   - Create a gig with venue, capacity and price
            - Sell tickets online with card payments
            - Email tickets with a QR code
            - Scan QR codes at the door from a phone browser
            - Stop sales when capacity is reached
API:        REST
            POST /gigs
            POST /gigs/{id}/checkout
            POST /tickets/{code}/scan
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Stripe API, html5-qrcode
```

---

## Example 96

**Intent:**
amateur weather station network, members upload readings and see them on map

**Spec:**
```
Type:       Web application (weather station network)
Auth:       API key per station, email + password for members
Data model: Member(id, name, email)
            Station(id, member_id -> Member, name, lat, lng, elevation_m, api_key)
            Reading(id, station_id -> Station, temp_c, humidity, pressure_hpa, rain_mm, recorded_at)
Features:   - Register a station with its location and get an API key
            - Accept readings from stations every 5 minutes
            - Show the latest temperature of every station on a map
            - Draw 24-hour and 7-day charts per station
            - Flag readings outside realistic ranges
API:        REST
            POST /stations
            POST /stations/{id}/readings
            GET  /stations/latest
            GET  /stations/{id}/readings?from={date}
Storage:    PostgreSQL with TimescaleDB
Tech stack: Python, FastAPI, Leaflet, Chart.js
```

---

## Example 97

**Intent:**
babysitting co-op where families trade hours instead of money

**Spec:**
```
Type:       Web application (babysitting co-op)
Auth:       Email + password login, invite-only
Data model: Family(id, name, email, children_count, balance_hours)
            Request(id, family_id -> Family, starts_at, ends_at, children, status)
            Sit(id, request_id -> Request, sitter_family_id -> Family, hours)
Features:   - Post a request for a babysitter with time and number of children
            - Accept a request to sit for another family
            - Move hours from the requesting family to the sitter family
            - Show each family's hour balance
            - Prevent new requests when the balance is too negative
API:        REST
            GET  /requests
            POST /requests
            POST /requests/{id}/accept
            GET  /families/me/balance
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 98

**Intent:**
need a little site where streamers list their schedule and viewers get notified

**Spec:**
```
Type:       Web application (stream schedules)
Auth:       Twitch OAuth login
Data model: Streamer(id, twitch_id, name, timezone)
            ScheduledStream(id, streamer_id -> Streamer, title, game, starts_at, duration_min)
            Follower(id, streamer_id -> Streamer, email, push_subscription)
Features:   - Create a weekly stream schedule
            - Show the schedule in each viewer's local time
            - Send browser push notifications 15 minutes before a stream
            - Export the schedule as an iCal feed
            - Show a "live now" badge using the Twitch API
API:        REST
            GET  /{streamer}/schedule
            POST /schedule
            POST /{streamer}/follow
            GET  /{streamer}/schedule.ics
Storage:    PostgreSQL
Tech stack: Node.js, Next.js, Twitch API, Web Push
```

---

## Example 99

**Intent:**
Saas for gyms to manage class bookings and memberships

**Spec:**
```
Type:       Web application (gym class booking SaaS)
Auth:       Email + password login, roles: owner, instructor, member
Data model: Gym(id, name, subdomain)
            Member(id, gym_id -> Gym, name, email, plan, active_until)
            Class(id, gym_id -> Gym, name, instructor, starts_at, capacity)
            Booking(id, class_id -> Class, member_id -> Member, status)
Features:   - Give each gym its own subdomain and branding
            - Publish a weekly class timetable
            - Book classes with a waitlist when full
            - Charge recurring memberships
            - Show attendance reports per class
API:        REST
            GET  /classes
            POST /classes/{id}/bookings
            POST /members
            GET  /reports/attendance
Storage:    PostgreSQL (one schema per gym)
Tech stack: Python, Django, django-tenants, Stripe API
```

---

## Example 100

**Intent:**
cooking class host site, chefs host home classes and people book seats

**Spec:**
```
Type:       Web application (home cooking classes)
Auth:       Email + password login
Data model: Chef(id, name, email, bio, city)
            CookingClass(id, chef_id -> Chef, title, cuisine, date, seats, price, address)
            Reservation(id, class_id -> CookingClass, guest_email, seats, paid)
            Review(id, class_id -> CookingClass, rating, text)
Features:   - Publish a class with cuisine, date, seats and price
            - Book and pay for seats
            - Reveal the exact address after booking
            - Leave a review after attending
            - Search classes by city and cuisine
API:        REST
            GET  /classes?city={city}
            POST /classes
            POST /classes/{id}/reservations
            POST /classes/{id}/reviews
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe API
```

---

## Example 101

**Intent:**
wordpress plugin for a pet adoption shelter showing animals ready for adoption

**Spec:**
```
Type:       Plugin (WordPress)
Data model: Animal custom post type (name, species, breed, age, sex, photos, status)
            AdoptionInquiry(id, animal_id, name, email, phone, message)
Features:   - Add an "Animals" post type with custom fields in the admin
            - Show a filterable grid of animals with a shortcode
            - Show a detail page with a photo gallery
            - Accept adoption inquiries through a form and email staff
            - Hide animals marked as adopted
Storage:    WordPress database (MySQL)
Tech stack: PHP, WordPress Plugin API, Advanced Custom Fields
```

---

## Example 102

**Intent:**
browser extension that lets our book club highlight passages on web articles and see each others highlights

**Spec:**
```
Type:       Browser extension (shared web highlights)
Auth:       Email + password login to the backend
Data model: Group(id, name, invite_code)
            Highlight(id, group_id -> Group, user_id, url, selector_json, text, note, created_at)
Features:   - Highlight selected text on any page and add a note
            - Show group members' highlights when visiting the same page
            - List all highlights for the group in the popup
            - Join a group with an invite code
API:        REST
            GET  /highlights?url={url}
            POST /highlights
            POST /groups/join
Storage:    PostgreSQL (backend)
Tech stack: JavaScript, Chrome Extensions Manifest V3, Node.js backend
```

---

## Example 103

**Intent:**
dashboard for my discord server stats, members joined, messages per channel

**Spec:**
```
Type:       Data dashboard (community analytics)
Data model: DailyStat(date, guild_id, members_total, joins, leaves)
            ChannelStat(date, channel_id, channel_name, messages, active_users)
Features:   - Collect join, leave and message counts with a bot
            - Store daily aggregates without message content
            - Show member growth as a line chart
            - Show messages per channel as a bar chart
            - Show the most active hours as a heatmap
Storage:    PostgreSQL
Tech stack: Python, discord.py, Streamlit, Plotly
```

---

## Example 104

**Intent:**
Every Monday morning, email our club members a list of this week's events from our Google Calendar.

**Spec:**
```
Type:       Scheduled script (weekly digest email)
Features:   - Fetch events for the next 7 days from a Google Calendar
            - Format them into an HTML email grouped by day
            - Load the member email list from a Google Sheet
            - Send the email through SMTP with BCC recipients
            - Log sends and errors to a file
Input:      Google Calendar ID, Google Sheet ID, SMTP credentials (environment variables)
Tech stack: Python, Google Calendar API, gspread, cron
```

---

## Example 105

**Intent:**
webhook that adds new Stripe donors to our Mailchimp list with a donor tag

**Spec:**
```
Type:       Webhook service (Stripe to Mailchimp)
Features:   - Receive Stripe checkout.session.completed events
            - Verify the Stripe signature header
            - Add or update the donor in a Mailchimp audience
            - Tag the contact as "donor" and with the donation tier
            - Ignore duplicate events by event ID
API:        REST
            POST /webhooks/stripe
Storage:    SQLite (processed event IDs)
Tech stack: Python, Flask, Stripe API, Mailchimp Marketing API
```

---

## Example 106

**Intent:**
dog walkers co-op schedule

**Spec:**
```
Type:       Web application (dog walking co-op)
Auth:       Email + password login
Data model: Walker(id, name, email, phone)
            Dog(id, owner_name, name, address, notes)
            Walk(id, dog_id -> Dog, walker_id -> Walker, starts_at, done, notes)
Features:   - Show a weekly calendar of walks
            - Assign walks to walkers and allow swaps
            - Mark a walk done with a note for the owner
            - Text the owner when a walk is finished
API:        REST
            GET  /walks?week={date}
            POST /walks
            PATCH /walks/{id}
Storage:    SQLite
Tech stack: Python, Flask, Twilio API
```

---

## Example 107

**Intent:**
voting system for our housing co-op assembly, one vote per unit, secret ballot

**Spec:**
```
Type:       Web application (co-op voting)
Auth:       One-time voting code per unit sent by email
Data model: Unit(id, number, contact_email)
            Motion(id, title, text, opens_at, closes_at)
            VoteToken(id, motion_id -> Motion, unit_id -> Unit, used)
            Ballot(id, motion_id -> Motion, choice)
Features:   - Create motions with an open and close time
            - Send each unit a unique voting code per motion
            - Store ballots without a link to the unit to keep votes secret
            - Allow only one vote per code
            - Show results after the vote closes
API:        REST
            POST /motions
            POST /motions/{id}/vote
            GET  /motions/{id}/results
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Jinja2
```

---

## Example 108

**Intent:**
community radio station site with show schedule, live stream player and show archives

**Spec:**
```
Type:       Web application (community radio)
Auth:       Email + password login for presenters
Data model: Show(id, title, presenter, description, weekday, start_time, end_time)
            Episode(id, show_id -> Show, aired_on, audio_url, tracklist)
Features:   - Show the weekly schedule and highlight what is on now
            - Play the live Icecast stream in a sticky player
            - Upload past episodes with tracklists
            - Let listeners browse and play archived episodes
            - Generate a podcast feed per show
API:        REST
            GET  /schedule
            GET  /now-playing
            POST /shows/{id}/episodes
            GET  /shows/{id}/feed.xml
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, Django, Icecast
```

---

## Example 109

**Intent:**
hackathon judging only, judges score on phone fast

**Spec:**
```
Type:       Web application (mobile-first judging)
Auth:       Magic link login for judges
Data model: Judge(id, name, email)
            Project(id, title, team, table_number)
            Criterion(id, name, weight)
            Score(id, project_id -> Project, judge_id -> Judge, criterion_id -> Criterion, value)
Features:   - Show each judge their assigned projects by table number
            - Score each criterion with large 1-5 buttons
            - Save scores offline and sync when back online
            - Normalise scores per judge to remove harsh or generous bias
            - Rank projects by weighted normalised score
API:        REST
            GET  /judges/me/projects
            POST /scores
            GET  /rankings
Storage:    PostgreSQL
Tech stack: TypeScript, React (PWA), Node.js, Express
```

---

## Example 110

**Intent:**
a site that lets theater groups share and borrow props and costumes from each other

**Spec:**
```
Type:       Web application (props and costume exchange)
Auth:       Email + password login per theater group
Data model: Troupe(id, name, city, contact_email)
            Piece(id, troupe_id -> Troupe, kind, name, era, size, photo_url)
            Loan(id, piece_id -> Piece, borrower_id -> Troupe, from_date, to_date, status)
Features:   - Catalog props and costumes with era, size and photos
            - Search by era, kind and size across all groups
            - Request a loan for show dates
            - Show a calendar of when each piece is out
            - Record condition at return
API:        REST
            GET  /pieces
            POST /pieces
            POST /pieces/{id}/loans
            PATCH /loans/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Express, React
```

---

## Example 111

**Intent:**
my sister runs a quilting guild and wants a members only site with a block of the month and a gallery

**Spec:**
```
Type:       Web application (quilting guild)
Auth:       Email + password login, admin approval
Data model: Member(id, name, email, approved)
            BlockOfMonth(id, month, title, pattern_pdf_url, instructions)
            GalleryPhoto(id, member_id -> Member, block_id -> BlockOfMonth, image_url, caption)
Features:   - Publish a block of the month with pattern and instructions
            - Let members upload photos of their finished blocks
            - Show a gallery grouped by month
            - Keep pages visible only to approved members
API:        REST
            GET  /blocks
            POST /blocks
            POST /blocks/{id}/photos
Storage:    SQLite, local file storage
Tech stack: Python, Flask
```

---

## Example 112

**Intent:**
sports league management for amateur football: fixtures, results, league table, top scorers

**Spec:**
```
Type:       Web application (amateur league)
Auth:       Email + password login, team manager and league admin roles
Data model: Team(id, name, manager_email)
            Player(id, team_id -> Team, name, shirt_number)
            Fixture(id, home_id -> Team, away_id -> Team, kickoff, home_goals, away_goals)
            Goal(id, fixture_id -> Fixture, player_id -> Player, minute)
Features:   - Generate a round-robin fixture list
            - Let managers submit results and goal scorers
            - Calculate the league table with points and goal difference
            - Show a top scorers list
            - Show each team's upcoming fixtures
API:        REST
            POST /fixtures/generate
            PATCH /fixtures/{id}
            GET  /table
            GET  /scorers
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 113

**Intent:**
kids art gallery website for the school

**Spec:**
```
Type:       Web application (school art gallery)
Auth:       Email + password login for teachers
Data model: Class(id, name, year)
            Artwork(id, class_id -> Class, child_first_name, title, medium, image_url, approved)
Features:   - Upload children's artwork per class
            - Show only first names to protect privacy
            - Require teacher approval before publishing
            - Browse the gallery by class and year
API:        REST
            GET  /artworks?class={id}
            POST /artworks
            PATCH /artworks/{id}
Storage:    PostgreSQL, S3 (images)
Tech stack: PHP, Laravel
```

---

## Example 114

**Intent:**
Calendar of free events in my city that anyone can submit to, with moderation.

**Spec:**
```
Type:       Web application (community events calendar)
Auth:       Email + password login for moderators
Data model: Event(id, title, description, venue, starts_at, ends_at, category, link, submitter_email, approved)
Features:   - Submit an event without an account
            - Approve or reject submissions as a moderator
            - Show events in month, week and list views
            - Filter by category and date
            - Export events as an iCal feed
API:        REST
            GET  /events?from={date}&to={date}
            POST /events
            PATCH /events/{id}
            GET  /events.ics
Storage:    PostgreSQL
Tech stack: Node.js, Express, FullCalendar
```

---

## Example 115

**Intent:**
puzzle swap club, people mail jigsaw puzzles round in a circle

**Spec:**
```
Type:       Web application (jigsaw puzzle swap)
Auth:       Email + password login
Data model: Member(id, name, email, address)
            Puzzle(id, owner_id -> Member, title, pieces, missing_pieces, photo_url)
            Round(id, starts_on)
            Shipment(id, round_id -> Round, puzzle_id -> Puzzle, from_id -> Member, to_id -> Member, shipped, received)
Features:   - Register puzzles with piece count and missing pieces
            - Generate a circular swap each round so nobody gets their own puzzle back
            - Show who to send to and the address
            - Mark shipments as sent and received
            - Track the journey of each puzzle
API:        REST
            POST /puzzles
            POST /rounds
            GET  /rounds/{id}/my-shipment
            PATCH /shipments/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 116

**Intent:**
community fridge map that shows which fridges are stocked

**Spec:**
```
Type:       Web application (community fridge map)
Auth:       Anonymous updates with optional login for fridge hosts
Data model: Fridge(id, name, address, lat, lng, host_contact, hours)
            StatusUpdate(id, fridge_id -> Fridge, level, notes, photo_url, reported_at)
Features:   - Show all fridges on a map coloured by stock level
            - Report a fridge as full, half or empty with a photo
            - Show when each fridge was last checked
            - Let hosts edit opening hours and rules
API:        REST
            GET  /fridges
            POST /fridges/{id}/status
            PATCH /fridges/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, Leaflet
```

---

## Example 117

**Intent:**
email course builder SaaS where creators set up a sequence of lessons sent every day after signup

**Spec:**
```
Type:       Web application (email course SaaS)
Auth:       Email + password login for creators
Data model: Creator(id, email, sending_domain)
            Course(id, creator_id -> Creator, title, slug)
            Lesson(id, course_id -> Course, day_offset, subject, body_md)
            Enrollment(id, course_id -> Course, email, enrolled_at, unsubscribed)
            Delivery(id, enrollment_id -> Enrollment, lesson_id -> Lesson, sent_at)
Features:   - Write lessons in Markdown with a send day
            - Embed a signup form for each course
            - Send each lesson on its day after enrollment with a background job
            - Track opens and unsubscribes
            - Show completion rates per lesson
API:        REST
            POST /courses
            POST /courses/{id}/lessons
            POST /c/{slug}/enroll
            GET  /courses/{id}/stats
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Sidekiq, Postmark API
```

---

## Example 118

**Intent:**
small multiplayer trivia game in the browser for our discord community nights

**Spec:**
```
Type:       Browser game (multiplayer trivia)
Data model: Room(code, host_id, status, question_index)
            Player(id, room_code, name, score)
            Question(id, category, text, choices, answer_index)
Features:   - Host creates a room and shares a short code
            - Players join on their phones with a nickname
            - Show a question with a 15-second timer to all players
            - Award more points for faster correct answers
            - Show the leaderboard after each question
API:        WebSocket
            WS   /rooms/{code}
Storage:    In-memory rooms, JSON file of questions
Tech stack: TypeScript, Node.js, Socket.IO, React
```

---

## Example 119

**Intent:**
want a site for comic artists to post webcomics page by page, readers subscribe

**Spec:**
```
Type:       Web application (webcomic hosting)
Auth:       Email + password login
Data model: Artist(id, username, email)
            Comic(id, artist_id -> Artist, title, slug, cover_url, schedule)
            Page(id, comic_id -> Comic, number, image_url, author_note, publish_at)
            Subscription(user_id, comic_id -> Comic)
Features:   - Upload pages and schedule them to publish
            - Read with next and previous navigation and keyboard arrows
            - Subscribe to a comic and get notified of updates
            - Show an archive grid of all pages
            - Serve an RSS feed per comic
API:        REST
            GET  /c/{slug}/{page}
            POST /comics/{id}/pages
            POST /comics/{id}/subscribe
            GET  /c/{slug}/rss.xml
Storage:    PostgreSQL, S3 (images), CDN
Tech stack: Python, Django
```

---

## Example 120

**Intent:**
I coordinate a beach cleanup group. after each cleanup we weigh trash by type. I want people to log the data and see total over years

**Spec:**
```
Type:       Web application (cleanup data tracker)
Auth:       Email + password login for coordinators
Data model: Beach(id, name, lat, lng)
            Cleanup(id, beach_id -> Beach, date, volunteers)
            TrashTally(id, cleanup_id -> Cleanup, category, count, weight_kg)
Features:   - Log a cleanup with number of volunteers
            - Enter counts and weights per trash category
            - Show totals per year and per beach
            - Show the top 10 most common items
            - Export data as CSV for marine research groups
API:        REST
            POST /cleanups
            POST /cleanups/{id}/tallies
            GET  /stats?year={year}
Storage:    PostgreSQL
Tech stack: Python, Django, Chart.js
```

---

## Example 121

**Intent:**
Uptime of api endpoints isn't enough, I need synthetic transaction monitoring SaaS that runs scripted browser flows like login and checkout.

**Spec:**
```
Type:       Web application (synthetic monitoring SaaS)
Auth:       Email + password login, team accounts
Data model: Team(id, name)
            Check(id, team_id -> Team, name, script, interval_min, regions)
            Run(id, check_id -> Check, region, passed, duration_ms, screenshot_url, error, ran_at)
Features:   - Write browser flow scripts in a code editor
            - Run checks on a schedule from several regions
            - Save a screenshot and error on failure
            - Alert by email and webhook after consecutive failures
            - Show step duration trends
API:        REST
            POST /checks
            POST /checks/{id}/run
            GET  /checks/{id}/runs
Storage:    PostgreSQL, S3 (screenshots)
Tech stack: Node.js, Playwright, BullMQ, React
```

---

## Example 122

**Intent:**
neighborhood dinner club where hosts cook for strangers once a month

**Spec:**
```
Type:       Web application (supper club)
Auth:       Email + password login
Data model: Member(id, name, email, dietary_needs)
            Dinner(id, host_id -> Member, date, menu, seats, area)
            Seat(dinner_id -> Dinner, member_id -> Member)
Features:   - Host a dinner with menu, seat count and area
            - Reserve a seat and share dietary needs with the host
            - Reveal the address 24 hours before the dinner
            - Limit each member to two dinners per month
API:        REST
            GET  /dinners
            POST /dinners
            POST /dinners/{id}/seats
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix
```

---

## Example 123

**Intent:**
customer support ticket portal for my small software product

**Spec:**
```
Type:       Web application (helpdesk)
Auth:       Email + password login for customers and agents
Data model: Customer(id, name, email)
            Ticket(id, customer_id -> Customer, subject, status, priority, assignee_id)
            Reply(id, ticket_id -> Ticket, author_id, body, is_internal, created_at)
Features:   - Open tickets from a web form or by email
            - Assign tickets to agents and set priority
            - Reply to customers and add internal notes
            - Use canned responses for common questions
            - Close tickets automatically after 7 days without reply
API:        REST
            POST /tickets
            GET  /tickets?status={status}
            POST /tickets/{id}/replies
            POST /inbound-email
Storage:    PostgreSQL
Tech stack: Python, Django, Mailgun inbound routes
```

---

## Example 124

**Intent:**
spec for a fishing catch log for our angling club w/ biggest fish competition

**Spec:**
```
Type:       Web application (angling club catch log)
Auth:       Email + password login
Data model: Angler(id, name, email)
            Catch(id, angler_id -> Angler, species, weight_kg, length_cm, water, photo_url, caught_at, released)
            Competition(id, name, species, starts_on, ends_on)
Features:   - Log catches with species, weight, length and photo
            - Require a photo for competition entries
            - Show competition standings by heaviest catch
            - Show each angler's personal best per species
            - Track catch-and-release percentage
API:        REST
            POST /catches
            GET  /competitions/{id}/standings
            GET  /anglers/{id}/bests
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Express, Vue.js
```

---

## Example 125

**Intent:**
I'm a high school robotics coach. We need parts inventory and a checkout so students sign out tools and parts for builds.

**Spec:**
```
Type:       Web application (robotics team inventory)
Auth:       Email + password login, coach role
Data model: Student(id, name, email)
            Part(id, name, category, quantity, bin_location)
            Checkout(id, part_id -> Part, student_id -> Student, quantity, out_at, returned_at)
Features:   - Track parts with quantity and bin location
            - Check parts out to a student and back in
            - Scan barcodes on bins with a phone camera
            - Warn the coach when a part runs low
            - Show what each student currently has
API:        REST
            GET  /parts
            POST /checkouts
            PATCH /checkouts/{id}
Storage:    SQLite
Tech stack: Python, Flask, QuaggaJS
```

---

## Example 126

**Intent:**
tiny saas: shorten links with custom domains and qr codes

**Spec:**
```
Type:       Web application (link shortener SaaS)
Auth:       Email + password login, API keys
Data model: User(id, email, plan)
            Domain(id, user_id -> User, hostname, verified)
            ShortLink(id, user_id -> User, domain_id -> Domain, slug, target_url)
            Click(id, link_id -> ShortLink, country, device, clicked_at)
Features:   - Create short links with a custom slug
            - Connect a custom domain and verify it with a DNS record
            - Generate a downloadable QR code per link
            - Redirect with a 301 and record clicks
            - Show clicks by country and device
API:        REST
            POST /links
            GET  /{slug}
            POST /domains
            GET  /links/{id}/qr.png
Storage:    PostgreSQL, Redis (redirect cache)
Tech stack: Go, React
```

---

## Example 127

**Intent:**
ice hockey beer league stats, goals assists penalties

**Spec:**
```
Type:       Web application (rec hockey league stats)
Auth:       Email + password login for scorekeepers
Data model: Team(id, name)
            Player(id, team_id -> Team, name, number)
            Game(id, home_id -> Team, away_id -> Team, played_at)
            Event(id, game_id -> Game, kind, player_id -> Player, assist1_id -> Player, assist2_id -> Player, period, minutes)
Features:   - Enter goals with up to two assists
            - Enter penalties with minutes
            - Show player points, goals, assists and PIM tables
            - Show standings with wins, losses and overtime losses
API:        REST
            POST /games/{id}/events
            GET  /stats/players
            GET  /standings
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 128

**Intent:**
platform for nonprofits to post skilled volunteering projects (design, coding) and pros apply

**Spec:**
```
Type:       Web application (skilled volunteering)
Auth:       Email + password login, organisation and volunteer roles
Data model: Organisation(id, name, email, verified)
            Volunteer(id, name, email, skills, portfolio_url)
            Project(id, org_id -> Organisation, title, skill, hours_estimate, deadline, status)
            Application(id, project_id -> Project, volunteer_id -> Volunteer, pitch, status)
Features:   - Post projects with required skill and hour estimate
            - Verify nonprofits before they can post
            - Apply to projects with a short pitch
            - Accept one volunteer and close the project to others
            - Show completed projects on volunteer profiles
API:        REST
            GET  /projects?skill={skill}
            POST /projects
            POST /projects/{id}/applications
            PATCH /applications/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 129

**Intent:**
i want a site where gamers in my city find people to play tabletop rpgs with, filter by system like pathfinder or call of cthulhu

**Spec:**
```
Type:       Web application (tabletop RPG group finder)
Auth:       Email + password login
Data model: Player(id, name, email, city, systems, experience)
            Campaign(id, gm_id -> Player, title, system, schedule, location, seats_open, online)
            JoinRequest(id, campaign_id -> Campaign, player_id -> Player, status)
Features:   - Post a campaign with system, schedule and open seats
            - Filter campaigns by system, city and online or in person
            - Request to join and let the GM accept
            - Show safety tools used at the table (lines and veils)
API:        REST
            GET  /campaigns?system={name}
            POST /campaigns
            POST /campaigns/{id}/join
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 130

**Intent:**
Customer referral program SaaS for e-commerce stores.

**Spec:**
```
Type:       Web application (referral program SaaS)
Auth:       Email + password login for merchants, API key for stores
Data model: Merchant(id, store_url, reward_type, reward_value)
            Advocate(id, merchant_id -> Merchant, email, referral_code)
            Referral(id, advocate_id -> Advocate, order_id, amount, status)
            Reward(id, advocate_id -> Advocate, code, issued_at)
Features:   - Give each customer a referral link after purchase
            - Track referred orders through a store webhook
            - Issue a discount code reward after a qualifying order
            - Block self-referrals by email and payment fingerprint
            - Show merchants revenue from referrals
API:        REST
            POST /advocates
            POST /webhooks/orders
            GET  /merchants/me/stats
Storage:    PostgreSQL
Tech stack: Node.js, Express, Shopify API, React
```

---

## Example 131

**Intent:**
platform for parents to swap kids clothes as they outgrow them

**Spec:**
```
Type:       Web application (kids clothing swap)
Auth:       Email + password login
Data model: Parent(id, name, email, area, credits)
            Bundle(id, parent_id -> Parent, size, season, gender, item_count, photo_url, status)
            Swap(id, bundle_id -> Bundle, taker_id -> Parent, status)
Features:   - List bundles of clothes by size and season
            - Earn credits for giving bundles and spend them to take one
            - Filter bundles by size and area
            - Arrange pickup through private messages
API:        REST
            GET  /bundles?size={size}
            POST /bundles
            POST /bundles/{id}/take
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 132

**Intent:**
bird ringing (banding) data entry for our research station, Python please

**Spec:**
```
Type:       Web application (bird banding records)
Auth:       Email + password login for ringers
Data model: Ringer(id, name, permit_number)
            Bird(id, ring_number, species)
            Capture(id, bird_id -> Bird, ringer_id -> Ringer, site, captured_at, wing_mm, weight_g, age, sex, is_retrap)
Features:   - Enter a new capture or a retrap by ring number
            - Validate measurements against species ranges
            - Show the capture history of a ring number
            - Report daily totals per species
            - Export in the national ringing scheme format
API:        REST
            POST /captures
            GET  /birds/{ring}
            GET  /reports/daily
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 133

**Intent:**
lost & found for a university campus, security desk logs items, students claim them

**Spec:**
```
Type:       Web application (campus lost property)
Auth:       University SSO for students, staff login for security desk
Data model: FoundItem(id, category, description, found_location, found_at, photo_url, status)
            Claim(id, item_id -> FoundItem, student_id, proof_description, status)
Features:   - Log found items at the desk with a photo
            - Let students search found items by category and date
            - Hide identifying details like ID cards behind a claim form
            - Review claims and mark items as collected
            - Donate items unclaimed after 90 days
API:        REST
            POST /items
            GET  /items?category={name}
            POST /items/{id}/claims
            PATCH /claims/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Java, Spring Boot, React
```

---

## Example 134

**Intent:**
a site for parkrun-style free weekly 5k with timing results

**Spec:**
```
Type:       Web application (weekly 5k results)
Auth:       Email registration with personal barcode, volunteer login
Data model: Runner(id, name, email, barcode, age_group)
            Event(id, date, course)
            Result(id, event_id -> Event, runner_id -> Runner, position, time_s)
Features:   - Register runners and issue a printable barcode
            - Upload finish times and scanned barcode positions after each run
            - Merge times and positions into results
            - Show results per event with age-graded percentages
            - Show each runner's personal best and run count
API:        REST
            POST /runners
            POST /events/{id}/upload
            GET  /events/{id}/results
            GET  /runners/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 135

**Intent:**
moderation queue service for user generated images, uses ai to flag nsfw and humans review

**Spec:**
```
Type:       REST API service (content moderation)
Auth:       API key per client app, reviewer login for the dashboard
Data model: Submission(id, client_id, image_url, ai_score, status, created_at)
            Decision(id, submission_id -> Submission, reviewer_id, verdict, reason)
Features:   - Accept image URLs for moderation
            - Score images with an NSFW classifier
            - Auto-approve low scores and auto-reject very high scores
            - Send the uncertain middle to a human review queue
            - Call the client's webhook with the final verdict
API:        REST
            POST /v1/submissions
            GET  /v1/submissions/{id}
            GET  /review/queue
            POST /review/{id}/decision
Storage:    PostgreSQL
Tech stack: Python, FastAPI, PyTorch, Celery
```

---

## Example 136

**Intent:**
a place where people share their DIY home renovation projects with before/after photos and costs

**Spec:**
```
Type:       Web application (DIY renovation showcase)
Auth:       Email + password login
Data model: User(id, username, email)
            Project(id, user_id -> User, title, room, total_cost, hours, difficulty)
            Photo(id, project_id -> Project, stage, image_url)
            Comment(id, project_id -> Project, user_id -> User, body)
Features:   - Post a project with before and after photos
            - Show a before/after slider on the project page
            - Record cost, hours and difficulty
            - Filter projects by room and budget
            - Ask questions in the comments
API:        REST
            GET  /projects?room={room}
            POST /projects
            POST /projects/{id}/photos
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Next.js
```

---

## Example 137

**Intent:**
scheduling interviews for hiring panel, candidates pick from slots where all panel free

**Spec:**
```
Type:       Web application (panel interview scheduler)
Auth:       Google sign-in for interviewers, tokenized links for candidates
Data model: Interviewer(id, email, calendar_token)
            Panel(id, role, duration_min)
            PanelMember(panel_id -> Panel, interviewer_id -> Interviewer)
            Invite(id, panel_id -> Panel, candidate_email, token, chosen_slot)
Features:   - Read free/busy times from each panelist's Google Calendar
            - Compute slots where the whole panel is free
            - Send candidates a link to pick a slot
            - Create the calendar event with a video link for everyone
API:        REST
            POST /panels
            POST /panels/{id}/invites
            GET  /i/{token}/slots
            POST /i/{token}/book
Storage:    PostgreSQL
Tech stack: Python, Django, Google Calendar API
```

---

## Example 138

**Intent:**
moth trapping records

**Spec:**
```
Type:       Web application (moth recording)
Auth:       Email + password login
Data model: Recorder(id, name, email)
            TrapNight(id, recorder_id -> Recorder, site, date, trap_type, min_temp_c)
            MothRecord(id, trap_night_id -> TrapNight, species, count, photo_url)
Features:   - Log a trap night with trap type and temperature
            - Add species and counts with autocomplete
            - Request identification help by posting a photo
            - Show a flight period chart per species
API:        REST
            POST /trap-nights
            POST /trap-nights/{id}/records
            GET  /species/{name}/flight-period
Storage:    PostgreSQL
Tech stack: Python, Flask, Chart.js
```

---

## Example 139

**Intent:**
help me with site where teachers share lesson plans and rate them, by grade and subject

**Spec:**
```
Type:       Web application (lesson plan sharing)
Auth:       Email + password login
Data model: Teacher(id, name, email, school)
            LessonPlan(id, teacher_id -> Teacher, title, grade, subject, duration_min, file_url, summary)
            Rating(plan_id -> LessonPlan, teacher_id -> Teacher, stars, comment)
Features:   - Upload lesson plans as PDF or DOCX with grade and subject
            - Search and filter by grade, subject and duration
            - Rate and comment on plans
            - Save plans into personal folders
            - Preview the first page without downloading
API:        REST
            GET  /plans?grade={g}&subject={s}
            POST /plans
            POST /plans/{id}/ratings
Storage:    PostgreSQL, S3 (files)
Tech stack: PHP, Laravel, Vue.js
```

---

## Example 140

**Intent:**
SaaS for restaurants to collect reservations through a widget on their own website

**Spec:**
```
Type:       Web application (restaurant reservations SaaS)
Auth:       Email + password login for restaurant staff
Data model: Restaurant(id, name, timezone, slot_minutes)
            Table(id, restaurant_id -> Restaurant, seats)
            Reservation(id, restaurant_id -> Restaurant, table_id -> Table, name, phone, party_size, starts_at, status)
Features:   - Embed a booking widget with a script tag
            - Show available times based on free tables and party size
            - Send SMS confirmations and reminders
            - Show staff a floor plan of the evening's bookings
            - Mark no-shows and keep a guest history
API:        REST
            GET  /r/{id}/availability?date={d}&party={n}
            POST /r/{id}/reservations
            PATCH /reservations/{id}
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, React, Twilio API
```

---

## Example 141

**Intent:**
astrophotography sharing with equipment and exposure details

**Spec:**
```
Type:       Web application (astrophotography gallery)
Auth:       Email + password login
Data model: User(id, username, email)
            Equipment(id, user_id -> User, kind, name)
            Image(id, user_id -> User, target, image_url, total_exposure_min, captured_on)
            ImageEquipment(image_id -> Image, equipment_id -> Equipment)
Features:   - Upload images with target object and exposure time
            - Attach telescope, camera and mount used
            - Browse images by target (e.g. M31) and equipment
            - Like and comment on images
            - Plate-solve an image to show coordinates
API:        REST
            GET  /images?target={name}
            POST /images
            POST /equipment
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, Django, Astrometry.net API
```

---

## Example 142

**Intent:**
mod tools dashboard for subreddit-like community: reports queue, bans, mod log

**Spec:**
```
Type:       Web application (moderation dashboard)
Auth:       Email + password login with two-factor, moderator role
Data model: Report(id, content_type, content_id, reporter_id, reason, status)
            Ban(id, user_id, moderator_id, reason, expires_at)
            ModAction(id, moderator_id, action, target_id, note, created_at)
Features:   - Show a queue of reported posts and comments
            - Remove content, approve it or dismiss the report
            - Ban users temporarily or permanently
            - Record every action in a public mod log
            - Use saved removal reasons
API:        REST
            GET  /reports?status=open
            POST /reports/{id}/resolve
            POST /bans
            GET  /modlog
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, tRPC, Prisma
```

---

## Example 143

**Intent:**
i want people from my village abroad to stay in touch, news, photos, who is visiting home when

**Spec:**
```
Type:       Web application (diaspora community)
Auth:       Email + password login, approval by admin
Data model: Member(id, name, email, country, family_name)
            NewsPost(id, author_id -> Member, title, body, photo_url, created_at)
            Visit(id, member_id -> Member, arrive_on, leave_on)
Features:   - Post village news with photos
            - Announce when you are visiting home
            - Show a calendar of who is home when
            - Show a map of where members live now
            - Send a monthly email digest of news
API:        REST
            GET  /news
            POST /news
            POST /visits
            GET  /visits?month={m}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django
```

---

## Example 144

**Intent:**
coding challenge platform for our company, weekly puzzle, auto-graded

**Spec:**
```
Type:       Web application (internal coding challenges)
Auth:       Company SSO (SAML)
Data model: Employee(id, name, email)
            Challenge(id, title, description, starts_at, ends_at)
            TestCase(id, challenge_id -> Challenge, input, expected_output, hidden)
            Submission(id, challenge_id -> Challenge, employee_id -> Employee, language, code, passed, runtime_ms)
Features:   - Publish a weekly challenge with sample and hidden test cases
            - Submit solutions in Python, JavaScript or Java
            - Run code in an isolated container with time and memory limits
            - Show a leaderboard by tests passed and submission time
API:        REST
            GET  /challenges/current
            POST /challenges/{id}/submissions
            GET  /challenges/{id}/leaderboard
Storage:    PostgreSQL
Tech stack: Go, Docker (sandbox), React, Monaco Editor
```

---

## Example 145

**Intent:**
tiny site for my D&D homebrew world where players read lore pages and I hide secrets until revealed

**Spec:**
```
Type:       Web application (campaign lore site)
Auth:       Email + password login, GM and player roles
Data model: Page(id, title, category, body_md, revealed)
            Secret(id, page_id -> Page, body_md, revealed_to)
            Player(id, name, email)
Features:   - Write lore pages in Markdown with categories
            - Hide pages or sections until the GM reveals them
            - Reveal a secret to one player or to everyone
            - Link pages with [[wiki links]]
API:        REST
            GET  /pages
            POST /pages
            POST /secrets/{id}/reveal
Storage:    SQLite
Tech stack: Python, Flask, Markdown
```

---

## Example 146

**Intent:**
SaaS that turns a google sheet into a simple JSON API

**Spec:**
```
Type:       Web application (sheet-to-API SaaS)
Auth:       Google sign-in, per-endpoint API keys
Data model: User(id, email, google_refresh_token)
            Endpoint(id, user_id -> User, sheet_id, tab, slug, api_key, cache_seconds)
Features:   - Connect a Google Sheet and pick a tab
            - Return rows as JSON using the header row as keys
            - Allow adding rows with POST
            - Cache responses for a configurable time
            - Filter rows with query parameters
API:        REST
            GET  /v1/{slug}
            POST /v1/{slug}
            POST /endpoints
Storage:    PostgreSQL, Redis (cache)
Tech stack: Node.js, Fastify, Google Sheets API
```

---

## Example 147

**Intent:**
need a way for my yoga studio teachers to swap classes when they are sick

**Spec:**
```
Type:       Web application (class cover requests)
Auth:       Email + password login
Data model: Teacher(id, name, email, phone, styles)
            ClassSlot(id, style, starts_at, teacher_id -> Teacher)
            CoverRequest(id, class_id -> ClassSlot, requested_by -> Teacher, reason, covered_by -> Teacher, status)
Features:   - Post a cover request for one of your classes
            - Notify teachers qualified for that style by SMS
            - Let the first available teacher accept
            - Update the timetable with the new teacher
            - Notify the studio manager of uncovered classes 24 hours before
API:        REST
            POST /cover-requests
            POST /cover-requests/{id}/accept
            GET  /timetable
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Twilio API, React
```

---

## Example 148

**Intent:**
Website for our motorcycle club to plan rides with routes and sign up

**Spec:**
```
Type:       Web application (motorcycle club rides)
Auth:       Email + password login
Data model: Rider(id, name, email, bike)
            Ride(id, leader_id -> Rider, title, route_gpx_url, distance_km, departs_at, meeting_point)
            Signup(ride_id -> Ride, rider_id -> Rider, has_passenger)
Features:   - Plan rides with a GPX route and meeting point
            - Show the route on a map with fuel stops
            - Sign up and say if you bring a passenger
            - Post a ride report with photos afterward
API:        REST
            GET  /rides
            POST /rides
            POST /rides/{id}/signups
Storage:    PostgreSQL, S3 (GPX and photos)
Tech stack: Ruby on Rails, Leaflet
```

---

## Example 149

**Intent:**
hey can u spec a site where students rate professors and courses but its only for our uni

**Spec:**
```
Type:       Web application (course reviews)
Auth:       University email verification
Data model: Student(id, email_hash)
            Course(id, code, title, department)
            Professor(id, name, department)
            Review(id, course_id -> Course, professor_id -> Professor, student_id -> Student, difficulty, quality, workload_hours, text, term)
Features:   - Allow only verified university emails to write reviews
            - Show reviews without revealing the student
            - Rate difficulty, quality and weekly workload
            - Show averages per course and per professor
            - Let students report reviews that break the rules
API:        REST
            GET  /courses/{code}
            POST /reviews
            POST /reviews/{id}/report
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 150

**Intent:**
a SaaS that sends cron job heartbeat alerts when a job doesn't check in

**Spec:**
```
Type:       Web application (cron monitoring SaaS)
Auth:       Email + password login
Data model: Account(id, email, alert_email, slack_webhook)
            Job(id, account_id -> Account, name, ping_token, period_s, grace_s, last_ping_at, status)
            Ping(id, job_id -> Job, received_at, kind)
Features:   - Give each job a unique ping URL
            - Mark a job as down when no ping arrives within period plus grace
            - Accept start and fail pings to measure duration
            - Alert by email and Slack when a job goes down or recovers
            - Show a ping history per job
API:        REST
            GET  /ping/{token}
            GET  /ping/{token}/fail
            POST /jobs
            GET  /jobs/{id}/pings
Storage:    PostgreSQL
Tech stack: Python, Django, Celery Beat
```

---

## Example 151

**Intent:**
beekeepers association: members log hive inspections and swarm alerts go out to people nearby

**Spec:**
```
Type:       Web application (beekeeping association)
Auth:       Email + password login
Data model: Beekeeper(id, name, email, phone, lat, lng, collects_swarms)
            Hive(id, beekeeper_id -> Beekeeper, name, apiary)
            Inspection(id, hive_id -> Hive, date, queen_seen, brood_frames, temper, varroa_count, notes)
            SwarmReport(id, reporter_phone, lat, lng, photo_url, reported_at, claimed_by -> Beekeeper)
Features:   - Log hive inspections with queen, brood and varroa counts
            - Show a varroa trend chart per hive
            - Let the public report a swarm with a photo and location
            - Text swarm collectors within 10 km of the report
            - Let a collector claim the swarm
API:        REST
            POST /hives/{id}/inspections
            POST /swarms
            POST /swarms/{id}/claim
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django, Twilio API
```

---

## Example 152

**Intent:**
planning poker for scrum teams

**Spec:**
```
Type:       Web application (planning poker)
Data model: Room(id, name, deck)
            Participant(id, room_id -> Room, name, is_observer)
            Story(id, room_id -> Room, title, final_estimate)
            Vote(story_id -> Story, participant_id -> Participant, card)
Features:   - Create a room and invite the team with a link
            - Vote with Fibonacci or T-shirt cards
            - Hide votes until everyone has voted or the host reveals
            - Show the average and spread of votes
            - Save the final estimate per story
API:        WebSocket
            WS   /rooms/{id}
Storage:    Redis
Tech stack: TypeScript, Node.js, ws, React
```

---

## Example 153

**Intent:**
secret santa organizer website with exclusions like couples cant get each other

**Spec:**
```
Type:       Web application (gift exchange draw)
Data model: Exchange(id, name, budget, draw_date, organiser_email)
            Participant(id, exchange_id -> Exchange, name, email, wishlist)
            Exclusion(participant_a_id -> Participant, participant_b_id -> Participant)
            Assignment(giver_id -> Participant, receiver_id -> Participant)
Features:   - Add participants and their emails
            - Set exclusions such as couples
            - Draw assignments randomly respecting exclusions
            - Email each person only their own recipient and wishlist
            - Let people ask their recipient anonymous questions
API:        REST
            POST /exchanges
            POST /exchanges/{id}/participants
            POST /exchanges/{id}/draw
Storage:    PostgreSQL
Tech stack: Python, Flask
```

---

## Example 154

**Intent:**
retro board for remote teams: went well, to improve, action items, anonymous cards

**Spec:**
```
Type:       Web application (team retrospectives)
Auth:       Email + password login for facilitators, guest names for participants
Data model: Board(id, team, title, phase)
            Card(id, board_id -> Board, column, text, votes)
            ActionItem(id, board_id -> Board, text, owner, done)
Features:   - Add cards anonymously to three columns
            - Hide other people's cards until the facilitator reveals them
            - Group similar cards and vote with three votes each
            - Turn top cards into action items with owners
            - Show open action items from the last retro
API:        WebSocket + REST
            WS   /boards/{id}
            GET  /teams/{team}/actions
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView
```

---

## Example 155

**Intent:**
privacy friendly website analytics saas, no cookies

**Spec:**
```
Type:       Web application (privacy-friendly analytics SaaS)
Auth:       Email + password login
Data model: Site(id, owner_id, domain)
            Pageview(site_id -> Site, path, referrer, country, device, visitor_hash, ts)
Features:   - Collect pageviews with a lightweight script and no cookies
            - Count unique visitors with a daily rotating salted hash
            - Show visitors, top pages, referrers and countries
            - Share a public dashboard link
            - Respect Do Not Track
API:        REST
            POST /api/event
            GET  /api/stats/{site}?period=30d
Storage:    ClickHouse (events), PostgreSQL (accounts)
Tech stack: Elixir, Phoenix, React
```

---

## Example 156

**Intent:**
I need an error tracking service like for my JS apps, catch exceptions and group them

**Spec:**
```
Type:       Web application (error tracking SaaS)
Auth:       Email + password login, DSN key per project
Data model: Project(id, name, dsn_key)
            Issue(id, project_id -> Project, fingerprint, title, first_seen, last_seen, count, status)
            Event(id, issue_id -> Issue, stacktrace_json, browser, url, release, created_at)
Features:   - Capture uncaught exceptions with a small browser SDK
            - Group events into issues by stack trace fingerprint
            - Apply source maps to show original code lines
            - Alert by email on new issues and regressions
            - Resolve and ignore issues
API:        REST
            POST /api/{project}/store
            GET  /projects/{id}/issues
            PATCH /issues/{id}
            POST /projects/{id}/sourcemaps
Storage:    PostgreSQL, S3 (source maps)
Tech stack: Go, TypeScript SDK, React
```

---

## Example 157

**Intent:**
wedding RSVP website with meal choices and plus ones

**Spec:**
```
Type:       Web application (wedding RSVP)
Auth:       Invite code per household, admin password for the couple
Data model: Household(id, name, invite_code, max_guests)
            Guest(id, household_id -> Household, name, attending, meal_choice, dietary_notes)
Features:   - Look up an invitation by code
            - RSVP for each guest in the household
            - Choose a meal and add dietary needs
            - Add a plus one if the invite allows
            - Show the couple totals per meal and a seating export
API:        REST
            GET  /invites/{code}
            POST /invites/{code}/rsvp
            GET  /admin/summary
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 158

**Intent:**
potluck signup so we dont end up with 10 desserts

**Spec:**
```
Type:       Web application (potluck planner)
Data model: Potluck(id, title, date, host_name, share_token)
            Category(id, potluck_id -> Potluck, name, slots)
            Dish(id, category_id -> Category, guest_name, dish_name, allergens)
Features:   - Create a potluck with categories and slots per category
            - Share a link with guests
            - Claim a slot and name your dish with allergens
            - Show which categories are still open
API:        REST
            POST /potlucks
            GET  /p/{token}
            POST /categories/{id}/dishes
Storage:    SQLite
Tech stack: Node.js, Express, EJS
```

---

## Example 159

**Intent:**
OKR tracking for startups, quarterly objectives with key results and weekly check-ins

**Spec:**
```
Type:       Web application (OKR tracking)
Auth:       Google sign-in, workspace invites
Data model: Objective(id, workspace_id, owner_id, title, quarter, parent_id -> Objective)
            KeyResult(id, objective_id -> Objective, title, start_value, target_value, current_value)
            CheckIn(id, key_result_id -> KeyResult, value, confidence, comment, created_at)
Features:   - Create objectives with measurable key results
            - Align team objectives under company objectives
            - Post weekly check-ins with a value and confidence
            - Show progress percentages rolled up to each objective
            - Remind owners on Monday to check in
API:        REST
            POST /objectives
            POST /objectives/{id}/key-results
            POST /key-results/{id}/check-ins
            GET  /tree?quarter={q}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 160

**Intent:**
office lunch order collector, one person orders for everyone from a restaurant

**Spec:**
```
Type:       Web application (group lunch orders)
Auth:       Slack sign-in
Data model: OrderRound(id, organiser_id, restaurant, menu_url, closes_at, status)
            OrderLine(id, round_id -> OrderRound, user_id, item, price, notes, paid)
Features:   - Start an order round with a restaurant and closing time
            - Post the round to a Slack channel
            - Add your item and price before it closes
            - Show the organiser the full order and total
            - Track who has paid the organiser back
API:        REST
            POST /rounds
            POST /rounds/{id}/lines
            PATCH /lines/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Slack Bolt, React
```

---

## Example 161

**Intent:**
reporting potholes and broken streetlights to our town with photo and gps

**Spec:**
```
Type:       Mobile application with backend (civic issue reporting)
Auth:       Optional email login, anonymous reports allowed
Data model: Report(id, category, description, photo_url, lat, lng, status, created_at)
            StatusChange(id, report_id -> Report, status, note, changed_at)
            Upvote(report_id -> Report, device_id)
Features:   - Take a photo and attach the current GPS location
            - Pick a category (pothole, streetlight, graffiti, litter)
            - Show nearby reports to avoid duplicates and allow upvoting
            - Let town staff update status in a web dashboard
            - Notify the reporter when the issue is fixed
API:        REST
            POST /reports
            GET  /reports?near={lat,lng}
            POST /reports/{id}/upvote
            PATCH /reports/{id}/status
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Flutter, Python, Django REST Framework
```

---

## Example 162

**Intent:**
volunteer translators platform for nonprofits, documents get split and translated by many people

**Spec:**
```
Type:       Web application (volunteer translation)
Auth:       Email + password login, roles: nonprofit, translator, reviewer
Data model: Translator(id, name, email, language_pairs)
            Document(id, org_id, title, source_lang, target_lang, status)
            Segment(id, document_id -> Document, position, source_text, translated_text, translator_id -> Translator, reviewed)
Features:   - Upload a document and split it into sentence segments
            - Let translators claim and translate segments for their language pair
            - Suggest earlier translations of similar segments
            - Let reviewers approve segments
            - Rebuild the translated document when all segments are approved
API:        REST
            POST /documents
            GET  /segments/available?pair={en-fr}
            PATCH /segments/{id}
            GET  /documents/{id}/export
Storage:    PostgreSQL
Tech stack: Python, Django, spaCy (sentence splitting)
```

---

## Example 163

**Intent:**
ola, i make a site for capoeira groups in europe to find rodas and events. simple please

**Spec:**
```
Type:       Web application (capoeira events)
Auth:       Email + password login for group leaders
Data model: Group(id, name, city, country, contact)
            Event(id, group_id -> Group, title, kind, starts_at, address)
Features:   - Register a group with city and contact
            - Post rodas, workshops and batizados
            - Show events on a map and as a list by country
            - Show the site in Portuguese, English and Spanish
API:        REST
            GET  /events?country={code}
            POST /events
            POST /groups
Storage:    SQLite
Tech stack: Python, Flask, Leaflet
```

---

## Example 164

**Intent:**
OG image generator saas, give it a url template and it renders social share images

**Spec:**
```
Type:       Web application (social image generation SaaS)
Auth:       Email + password login, signed URLs
Data model: Account(id, email, signing_secret)
            Template(id, account_id -> Account, name, html, width, height)
            RenderCache(key, template_id -> Template, image_url, created_at)
Features:   - Design templates in HTML/CSS with variables
            - Render a PNG from a template and URL query parameters
            - Require an HMAC signature on render URLs
            - Cache rendered images on a CDN
            - Preview templates live in the editor
API:        REST
            GET  /render/{template}.png?title={t}&sig={sig}
            POST /templates
            PUT  /templates/{id}
Storage:    PostgreSQL, S3 (rendered images), CDN
Tech stack: Node.js, Puppeteer, React
```

---

## Example 165

**Intent:**
cemetery gravestone photo project, volunteers photograph and transcribe headstones

**Spec:**
```
Type:       Web application (gravestone records)
Auth:       Email + password login
Data model: Cemetery(id, name, lat, lng, county)
            Grave(id, cemetery_id -> Cemetery, photo_url, lat, lng, volunteer_id)
            Person(id, grave_id -> Grave, first_name, last_name, birth_year, death_year, inscription)
Features:   - Upload headstone photos with GPS from the phone
            - Transcribe names and dates from each photo
            - Search people by name and years across cemeteries
            - Show a cemetery's progress (photographed vs transcribed)
            - Let others suggest corrections
API:        REST
            POST /cemeteries/{id}/graves
            POST /graves/{id}/people
            GET  /search?name={name}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 166

**Intent:**
employee kudos wall

**Spec:**
```
Type:       Web application (peer recognition)
Auth:       Microsoft Entra ID single sign-on
Data model: Employee(id, name, email, team)
            Kudo(id, from_id -> Employee, to_id -> Employee, message, value_tag, created_at)
            Reaction(kudo_id -> Kudo, employee_id -> Employee, emoji)
Features:   - Post a thank-you to a colleague tagged with a company value
            - Show a public wall of recent kudos
            - React to kudos with emoji
            - Post kudos to a Teams channel
            - Show monthly counts per team
API:        REST
            GET  /kudos
            POST /kudos
            POST /kudos/{id}/reactions
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, React, Microsoft Graph API
```

---

## Example 167

**Intent:**
Site for language learners to submit short texts and native speakers correct them

**Spec:**
```
Type:       Web application (writing correction exchange)
Auth:       Email + password login
Data model: User(id, username, email, native_languages, learning_languages, points)
            Entry(id, author_id -> User, language, text, created_at)
            Correction(id, entry_id -> Entry, corrector_id -> User, corrected_text, explanation)
Features:   - Post a short text in a language you are learning
            - Show entries to native speakers of that language
            - Correct a text and show a word-level diff
            - Earn points for corrections that help you get your own texts seen first
API:        REST
            POST /entries
            GET  /entries/to-correct
            POST /entries/{id}/corrections
Storage:    PostgreSQL
Tech stack: Ruby on Rails, diff-lcs
```

---

## Example 168

**Intent:**
api mocking saas, devs define fake endpoints with json responses for frontend dev

**Spec:**
```
Type:       Web application (API mocking SaaS)
Auth:       GitHub OAuth login
Data model: Workspace(id, owner_id, subdomain)
            MockRoute(id, workspace_id -> Workspace, method, path_pattern, status_code, body_template, delay_ms)
            RequestLog(id, workspace_id -> Workspace, method, path, body, received_at)
Features:   - Define routes with method, path pattern and JSON response
            - Use templates to insert path params and fake data
            - Add artificial latency and error rates
            - Import routes from an OpenAPI file
            - Log incoming requests for debugging
API:        REST
            ANY  https://{subdomain}.mock.example/{path}
            POST /routes
            POST /import/openapi
            GET  /logs
Storage:    PostgreSQL
Tech stack: Go, Faker, React
```

---

## Example 169

**Intent:**
I lead a group of wild swimmers. Lakes and sea temps change a lot. would love a site where we post water temp and conditions after swims so others know before going

**Spec:**
```
Type:       Web application (wild swimming conditions)
Auth:       Email + password login
Data model: Swimmer(id, name, email)
            Spot(id, name, lat, lng, kind)
            Report(id, spot_id -> Spot, swimmer_id -> Swimmer, water_temp_c, conditions, water_quality, swum_at)
Features:   - Post water temperature and conditions after a swim
            - Show each spot's latest temperature on a map
            - Chart temperature over the season per spot
            - Flag pollution warnings for a spot
            - Arrange group swims with a meet time
API:        REST
            GET  /spots
            POST /spots/{id}/reports
            GET  /spots/{id}/temps
Storage:    PostgreSQL
Tech stack: Node.js, Express, Leaflet, Chart.js
```

---

## Example 170

**Intent:**
SaaS for e-signatures on simple contracts for freelancers

**Spec:**
```
Type:       Web application (e-signature SaaS)
Auth:       Email + password login for senders, emailed links for signers
Data model: Document(id, owner_id, title, pdf_url, status, completed_pdf_url)
            Signer(id, document_id -> Document, name, email, token, signed_at, ip_address)
            Field(id, document_id -> Document, signer_id -> Signer, page, x, y, kind)
Features:   - Upload a PDF and place signature and date fields
            - Email signers a unique signing link
            - Capture a drawn or typed signature
            - Flatten signatures into the final PDF
            - Attach an audit trail page with timestamps and IP addresses
API:        REST
            POST /documents
            POST /documents/{id}/send
            GET  /sign/{token}
            POST /sign/{token}
Storage:    PostgreSQL, S3 (PDFs)
Tech stack: Python, Django, pypdf, PDF.js
```

---

## Example 171

**Intent:**
time off requests for a team of 15 with approval and a calendar

**Spec:**
```
Type:       Web application (leave management)
Auth:       Google sign-in
Data model: Employee(id, name, email, manager_id -> Employee, annual_days)
            LeaveRequest(id, employee_id -> Employee, kind, start_date, end_date, status, note)
Features:   - Request vacation or sick days
            - Let managers approve or reject requests
            - Show a team calendar of who is off
            - Calculate remaining days per person
            - Exclude public holidays from day counts
API:        REST
            POST /leave-requests
            PATCH /leave-requests/{id}
            GET  /calendar?month={m}
            GET  /me/balance
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 172

**Intent:**
community tool to plan street parties, road closure form, who brings what, volunteers

**Spec:**
```
Type:       Web application (street party planner)
Auth:       Email login with magic link
Data model: Party(id, street, date, organiser_id, closure_status)
            Household(id, party_id -> Party, house_number, contact_name, email)
            Task(id, party_id -> Party, title, household_id -> Household)
            Contribution(id, party_id -> Party, household_id -> Household, item)
Features:   - Create a party page for a street and invite households
            - Generate a pre-filled road closure application PDF
            - List tasks and let households volunteer for them
            - Track who brings tables, food and music
            - Send update emails to all households
API:        REST
            POST /parties
            POST /parties/{id}/households
            POST /tasks/{id}/claim
            GET  /parties/{id}/closure.pdf
Storage:    PostgreSQL
Tech stack: Python, Django, WeasyPrint
```

---

## Example 173

**Intent:**
discord bot for language exchange server, pairs people randomly each week for a voice chat

**Spec:**
```
Type:       Bot (Discord)
Data model: Participant(user_id, native_lang, target_lang, active)
            Pairing(id, week, user_a_id, user_b_id, met)
Features:   - Let members opt in with /join and their languages
            - Pair members each Monday so each partner speaks the other's target language
            - Avoid repeating pairs from the last four weeks
            - Create a private voice channel for each pair
            - Ask both partners on Sunday if they met
Storage:    SQLite
Tech stack: JavaScript, discord.js, node-cron
```

---

## Example 174

**Intent:**
church sermon archive with audio, notes and search by bible passage

**Spec:**
```
Type:       Web application (sermon archive)
Auth:       Email + password login for staff
Data model: Speaker(id, name)
            Series(id, title, artwork_url)
            Sermon(id, series_id -> Series, speaker_id -> Speaker, title, date, audio_url, notes_pdf_url, passages)
Features:   - Upload sermon audio with notes and passages
            - Search by book, chapter and verse range
            - Browse by series and speaker
            - Publish a podcast feed
API:        REST
            GET  /sermons?passage={ref}
            POST /sermons
            GET  /feed.xml
Storage:    PostgreSQL, S3 (audio)
Tech stack: PHP, Laravel
```

---

## Example 175

**Intent:**
idea: site where people post 'I'll teach a free 1 hour class on X' in parks and others rsvp

**Spec:**
```
Type:       Web application (free community classes)
Auth:       Email + password login
Data model: User(id, name, email)
            Class(id, teacher_id -> User, title, topic, location_name, lat, lng, starts_at, max_people)
            Rsvp(class_id -> Class, user_id -> User)
Features:   - Post a free class with topic, park location and time
            - Browse upcoming classes on a map and list
            - RSVP and see remaining spots
            - Send a cancellation notice to attendees if the weather is bad
            - Thank the teacher with a short note afterward
API:        REST
            GET  /classes
            POST /classes
            POST /classes/{id}/rsvp
Storage:    PostgreSQL
Tech stack: Node.js, Next.js, Mapbox
```

---

## Example 176

**Intent:**
documentation hosting saas: push markdown from github, get a docs site

**Spec:**
```
Type:       Web application (docs hosting SaaS)
Auth:       GitHub OAuth login, GitHub App installation
Data model: Project(id, owner_id, repo_full_name, docs_path, subdomain)
            Build(id, project_id -> Project, commit_sha, status, log, created_at)
            Version(id, project_id -> Project, name, build_id -> Build)
Features:   - Install a GitHub App and pick the docs folder
            - Build a static site on every push via webhook
            - Host versions per git tag
            - Provide full-text search across pages
            - Show build logs and failures
API:        REST
            POST /webhooks/github
            GET  /projects/{id}/builds
            POST /projects
Storage:    PostgreSQL, S3 (built sites), CDN
Tech stack: Go, MkDocs build containers, React
```

---

## Example 177

**Intent:**
baby name voting for our family

**Spec:**
```
Type:       Web application (name voting)
Data model: Poll(id, title, admin_token, share_token)
            Name(id, poll_id -> Poll, name, suggested_by)
            Vote(name_id -> Name, voter_name, score)
Features:   - Create a poll and share a link with relatives
            - Suggest new names
            - Rate each name from 1 to 5
            - Show names ranked by average score to the parents only
API:        REST
            POST /polls
            POST /p/{token}/names
            POST /p/{token}/votes
            GET  /admin/{token}/results
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 178

**Intent:**
platform for urban sketchers groups to organise sketchwalks and post sketches from them

**Spec:**
```
Type:       Web application (sketchwalk community)
Auth:       Email + password login
Data model: Chapter(id, city, name)
            Sketcher(id, name, email, chapter_id -> Chapter)
            Sketchwalk(id, chapter_id -> Chapter, location, lat, lng, date)
            Sketch(id, sketchwalk_id -> Sketchwalk, sketcher_id -> Sketcher, image_url, medium)
Features:   - Create sketchwalks with a meeting point
            - RSVP to sketchwalks in your chapter
            - Upload sketches made at a sketchwalk
            - Show each sketchwalk's sketches as a gallery
            - Show a map of all sketched places in a city
API:        REST
            GET  /chapters/{id}/sketchwalks
            POST /sketchwalks
            POST /sketchwalks/{id}/sketches
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, Django, Leaflet
```

---

## Example 179

**Intent:**
cookie consent banner saas with logs for gdpr proof

**Spec:**
```
Type:       Web application (consent management SaaS)
Auth:       Email + password login
Data model: Site(id, owner_id, domain, banner_config_json)
            CookieCategory(id, site_id -> Site, name, required, scripts)
            ConsentRecord(id, site_id -> Site, visitor_id, choices_json, ip_hash, created_at)
Features:   - Configure banner text, colours and categories
            - Serve a script that shows the banner and blocks scripts until consent
            - Store each consent choice with a timestamp as proof
            - Scan the site for cookies and suggest categories
            - Export consent logs for audits
API:        REST
            GET  /banner/{site}.js
            POST /consent
            GET  /sites/{id}/consents.csv
Storage:    PostgreSQL
Tech stack: Node.js, TypeScript, Preact (banner), React
```

---

## Example 180

**Intent:**
kayak and canoe club boat booking, only qualified paddlers can book certain boats

**Spec:**
```
Type:       Web application (club boat booking)
Auth:       Email + password login
Data model: Paddler(id, name, email, qualification_level)
            Boat(id, name, kind, min_level, status)
            Booking(id, boat_id -> Boat, paddler_id -> Paddler, starts_at, ends_at)
            DamageReport(id, boat_id -> Boat, paddler_id -> Paddler, description, photo_url)
Features:   - Show a day view of each boat's bookings
            - Allow booking only when the paddler's level meets the boat's minimum
            - Report damage and take a boat out of service
            - Show coaches which boats are out on the water
API:        REST
            GET  /boats
            POST /bookings
            POST /boats/{id}/damage
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 181

**Intent:**
platform to sell digital sewing patterns from independent designers

**Spec:**
```
Type:       Web application (digital pattern shop)
Auth:       Email + password login, designer and buyer roles
Data model: Designer(id, name, email, payout_account_id)
            Pattern(id, designer_id -> Designer, title, sizes, price, pdf_url, preview_urls)
            Purchase(id, pattern_id -> Pattern, buyer_email, amount, download_token)
Features:   - Let designers upload PDF patterns with previews
            - Sell patterns with card payments and split payouts to designers
            - Email buyers a time-limited download link
            - Stamp the buyer's email onto the PDF
            - Show designers their sales
API:        REST
            GET  /patterns
            POST /patterns
            POST /patterns/{id}/checkout
            GET  /download/{token}
Storage:    PostgreSQL, S3 (PDFs)
Tech stack: Node.js, Express, Stripe Connect, pdf-lib
```

---

## Example 182

**Intent:**
i want a site to collect and vote on questions for our town hall meeting before it starts

**Spec:**
```
Type:       Web application (live Q&A)
Data model: Session(id, title, code, moderator_token, open)
            Question(id, session_id -> Session, text, author_name, votes, status)
Features:   - Submit questions anonymously or with a name
            - Upvote questions once per browser
            - Show questions sorted by votes in real time
            - Let the moderator hide, highlight or mark questions answered
            - Show a full-screen view for the projector
API:        REST + WebSocket
            POST /sessions/{code}/questions
            POST /questions/{id}/vote
            WS   /sessions/{code}/live
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 183

**Intent:**
SaaS with a public API: give it a URL, get back a screenshot

**Spec:**
```
Type:       REST API service (screenshot API)
Auth:       API key in the query string or header
Data model: Account(id, email, api_key_hash, plan, monthly_quota)
            Capture(id, account_id -> Account, url, width, full_page, image_url, created_at)
Features:   - Render a URL in a headless browser and return a PNG or JPEG
            - Support viewport size, full-page and delay options
            - Block ads and cookie banners optionally
            - Cache identical captures for an hour
            - Enforce monthly quotas per plan
API:        REST
            GET  /v1/screenshot?url={url}&width={w}
            GET  /v1/usage
Storage:    PostgreSQL, S3 (images)
Tech stack: Node.js, Playwright, Fastify
```

---

## Example 184

**Intent:**
neighborhood babysitter recommendations shared only between moms in our school

**Spec:**
```
Type:       Web application (trusted sitter list)
Auth:       Email + password login, invite by existing member
Data model: Parent(id, name, email, invited_by -> Parent)
            Sitter(id, name, phone, age, rate, languages)
            Recommendation(id, sitter_id -> Sitter, parent_id -> Parent, text, rating)
Features:   - Join only through an invite from an existing parent
            - Add sitters you have used with contact details
            - Write recommendations with a rating
            - Search sitters by language and availability
API:        REST
            GET  /sitters
            POST /sitters
            POST /sitters/{id}/recommendations
            POST /invites
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 185

**Intent:**
astronomy outreach: schedule public telescope viewing nights at schools, volunteers sign up to bring scopes

**Spec:**
```
Type:       Web application (outreach event scheduling)
Auth:       Email + password login for volunteers and coordinators
Data model: School(id, name, contact_email, address)
            OutreachEvent(id, school_id -> School, date, expected_attendees, status)
            VolunteerSignup(event_id -> OutreachEvent, volunteer_id, telescope)
Features:   - Let schools request a viewing night
            - Let coordinators confirm dates and publish them
            - Sign up volunteers with the telescope they bring
            - Warn when fewer than 3 telescopes are confirmed
            - Send a weather go/no-go email on the day
API:        REST
            POST /requests
            POST /events
            POST /events/{id}/signups
Storage:    PostgreSQL
Tech stack: Python, Flask, Open-Meteo API
```

---

## Example 186

**Intent:**
webhook relay service that receives webhooks and forwards them to localhost for dev testing

**Spec:**
```
Type:       Webhook service (developer relay)
Auth:       Token per channel used by the CLI client
Data model: Channel(id, slug, token, created_at)
            Delivery(id, channel_id -> Channel, method, headers_json, body, received_at, forwarded)
Features:   - Give each developer a public URL to receive webhooks
            - Stream incoming requests to a CLI over a WebSocket
            - Forward each request to a local port and return its response
            - Store recent deliveries and allow replaying them
API:        REST + WebSocket
            ANY  /h/{slug}
            WS   /channels/{slug}/stream
            POST /deliveries/{id}/replay
Storage:    Redis (recent deliveries)
Tech stack: Go, gorilla/websocket
```

---

## Example 187

**Intent:**
something for my book swap shelf in the lobby to track what's there and who took what

**Spec:**
```
Type:       Web application (little free library tracker)
Data model: Book(id, isbn, title, author, cover_url, status, added_at)
            Movement(id, book_id -> Book, action, person_name, at)
Features:   - Add a book by scanning its ISBN barcode with a phone
            - Fetch title and cover from Open Library
            - Mark a book as taken or returned with your first name
            - Show what is on the shelf now
API:        REST
            GET  /books?status=on-shelf
            POST /books
            POST /books/{id}/movements
Storage:    SQLite
Tech stack: Python, Flask, Open Library API
```

---

## Example 188

**Intent:**
saas: appointment booking for tutors with packages of lessons and online payments

**Spec:**
```
Type:       Web application (tutoring booking SaaS)
Auth:       Email + password login for tutors and students
Data model: Tutor(id, name, email, subject, hourly_rate, timezone)
            Availability(id, tutor_id -> Tutor, weekday, start_time, end_time)
            Package(id, tutor_id -> Tutor, student_id, lessons_total, lessons_used)
            Lesson(id, package_id -> Package, starts_at, meeting_url, status)
Features:   - Publish weekly availability
            - Sell lesson packages (e.g. 5 or 10 lessons) online
            - Book a lesson and deduct it from the package
            - Create a video meeting link automatically
            - Allow cancellation up to 24 hours before
API:        REST
            GET  /tutors/{id}/slots
            POST /packages/checkout
            POST /lessons
            DELETE /lessons/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Stripe API, Zoom API, React
```

---

## Example 189

**Intent:**
alumni mentoring for first gen college students, by major and industry

**Spec:**
```
Type:       Web application (alumni mentoring)
Auth:       Email + password login, university SSO for students
Data model: Alum(id, name, email, major, industry, employer, capacity)
            Student(id, name, email, major, interests)
            MentorRequest(id, student_id -> Student, alum_id -> Alum, message, status)
            Meeting(id, request_id -> MentorRequest, date, notes)
Features:   - Browse alumni by major and industry
            - Send a mentoring request with a short message
            - Limit alumni to their chosen number of mentees
            - Log meetings and shared resources
            - Show the program office participation reports
API:        REST
            GET  /alumni?industry={name}
            POST /requests
            PATCH /requests/{id}
            GET  /reports
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 190

**Intent:**
chess puzzle of the day site where club members compete on solving streaks

**Spec:**
```
Type:       Web application (daily chess puzzles)
Auth:       Email + password login
Data model: Member(id, name, email, streak, best_streak)
            Puzzle(id, fen, solution_moves, rating, publish_on)
            Attempt(id, puzzle_id -> Puzzle, member_id -> Member, solved, seconds, attempted_on)
Features:   - Publish one puzzle per day from a FEN position
            - Check moves against the solution on an interactive board
            - Count solve time and update streaks
            - Show a monthly leaderboard
API:        REST
            GET  /puzzles/today
            POST /puzzles/{id}/attempts
            GET  /leaderboard
Storage:    PostgreSQL
Tech stack: Node.js, Express, chessground, chess.js
```

---

## Example 191

**Intent:**
I'd like to build an online platform for my regional orchid society where members can register their plants, document blooms with photos each year, and see who has which species in case they want to trade divisions. We have about 200 members, many older, so it needs to be very simple.

**Spec:**
```
Type:       Web application (orchid society registry)
Auth:       Email + password login with large, simple forms
Data model: Member(id, name, email, phone)
            Plant(id, member_id -> Member, genus, species, hybrid_name, acquired_on)
            Bloom(id, plant_id -> Plant, year, spikes, flowers, photo_url)
            TradeInterest(id, plant_id -> Plant, member_id -> Member, message)
Features:   - Register plants with genus, species or hybrid name
            - Add a bloom record with photo each year
            - Search which members grow a given species
            - Express interest in a division from another member
            - Use large text and simple step-by-step forms
API:        REST
            POST /plants
            POST /plants/{id}/blooms
            GET  /plants?species={name}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django
```

---

## Example 192

**Intent:**
mastodon bot that posts our cities upcoming events every morning

**Spec:**
```
Type:       Bot (Mastodon)
Features:   - Fetch today's events from the city events iCal feed
            - Format each event as a post with time, title and link
            - Post a thread each morning at 8:00 from the bot account
            - Skip days with no events
            - Use hashtags for the city name
Input:      iCal feed URL, Mastodon instance URL and access token
Tech stack: Python, Mastodon.py, icalendar, cron
```

---

## Example 193

**Intent:**
platform where small podcasters swap guest appearances

**Spec:**
```
Type:       Web application (podcast guest swap)
Auth:       Email + password login
Data model: Podcast(id, owner_id, title, topic, feed_url, monthly_downloads)
            SwapRequest(id, from_podcast_id -> Podcast, to_podcast_id -> Podcast, pitch, status)
            Recording(id, swap_id -> SwapRequest, scheduled_at, side)
Features:   - Import show details from the RSS feed
            - Browse podcasts by topic and audience size
            - Send a guest swap pitch
            - Schedule both recordings once accepted
            - Mark swaps complete when both episodes are out
API:        REST
            GET  /podcasts?topic={t}
            POST /swap-requests
            PATCH /swap-requests/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, feedparser, React
```

---

## Example 194

**Intent:**
coworking space community board where members post what they're working on and ask for help

**Spec:**
```
Type:       Web application (coworking member board)
Auth:       Email + password login
Data model: Member(id, name, email, company, skills)
            Post(id, member_id -> Member, kind, body, created_at)
            Reply(id, post_id -> Post, member_id -> Member, body)
Features:   - Post updates or help requests
            - Show a member directory with skills
            - Suggest members whose skills match a help request
            - Show today's posts on the lobby TV display
API:        REST
            GET  /posts
            POST /posts
            POST /posts/{id}/replies
            GET  /display
Storage:    PostgreSQL
Tech stack: Node.js, SvelteKit
```

---

## Example 195

**Intent:**
dashboard of our volunteer hours and impact for the annual report

**Spec:**
```
Type:       Data dashboard (nonprofit impact)
Features:   - Load volunteer hours from a CSV export
            - Show total hours by month and program
            - Show the number of active volunteers per quarter
            - Show value of volunteer time using a set hourly rate
            - Export charts as PNG for the report
Input:      CSV export of volunteer shifts (name, program, date, hours)
Tech stack: Python, pandas, Streamlit, Altair
```

---

## Example 196

**Intent:**
plz spec quiz site where teachers make quizzes and students play live in class from phones, original not copy of any brand

**Spec:**
```
Type:       Web application (live classroom quiz)
Auth:       Email + password login for teachers, game PIN for students
Data model: Quiz(id, teacher_id, title)
            Question(id, quiz_id -> Quiz, text, choices_json, correct_index, time_limit_s)
            Game(id, quiz_id -> Quiz, pin, state)
            Answer(game_id -> Game, player_name, question_id -> Question, choice, ms)
Features:   - Build quizzes with multiple-choice questions and time limits
            - Start a game and show a PIN on the projector
            - Let students join with the PIN and a nickname
            - Score by correctness and speed
            - Show a podium at the end and export results
API:        REST + WebSocket
            POST /quizzes
            POST /games
            WS   /games/{pin}
Storage:    PostgreSQL, Redis (live game state)
Tech stack: TypeScript, Node.js, Socket.IO, Vue.js
```

---

## Example 197

**Intent:**
hobby electronics project sharing site with schematics and parts lists

**Spec:**
```
Type:       Web application (electronics project sharing)
Auth:       Email + password login
Data model: Maker(id, username, email)
            Project(id, maker_id -> Maker, title, description, schematic_url, code_repo_url)
            Part(id, project_id -> Project, name, quantity, supplier_url)
            Remix(id, original_id -> Project, remix_id -> Project)
Features:   - Publish projects with schematics, photos and code links
            - List the bill of materials with quantities
            - Export the parts list as CSV
            - Remix a project and link to the original
            - Search by microcontroller (Arduino, ESP32, RP2040)
API:        REST
            GET  /projects?mcu={name}
            POST /projects
            GET  /projects/{id}/bom.csv
Storage:    PostgreSQL, S3 (files)
Tech stack: Python, Django, HTMX
```

---

## Example 198

**Intent:**
tell me how to build a website to manage my family reunion: rsvps, room sharing at the hotel, payment for the dinner

**Spec:**
```
Type:       Web application (family reunion planner)
Auth:       Email login with magic link
Data model: Family(id, branch_name, contact_email)
            Attendee(id, family_id -> Family, name, age_group, attending)
            Room(id, label, beds)
            RoomAssignment(room_id -> Room, attendee_id -> Attendee)
            Payment(id, family_id -> Family, amount, paid_at)
Features:   - RSVP for each family member
            - Assign attendees to shared hotel rooms
            - Calculate each family's share of the dinner cost
            - Pay online or mark cash payments
            - Email updates to all families
API:        REST
            POST /families/{id}/attendees
            POST /rooms/{id}/assign
            POST /payments
Storage:    PostgreSQL
Tech stack: Python, Flask, Stripe API
```

---

## Example 199

**Intent:**
ttrpg character sheet sharing for our group, GM can see everyone's sheet

**Spec:**
```
Type:       Web application (character sheets)
Auth:       Email + password login
Data model: Campaign(id, gm_id, name, system)
            Character(id, campaign_id -> Campaign, player_id, name, stats_json, inventory_json, hp)
            DiceRoll(id, character_id -> Character, expression, result, rolled_at)
Features:   - Create a character sheet from a system template
            - Let the GM view and adjust all sheets in the campaign
            - Update HP and inventory during play
            - Roll dice from the sheet and share rolls with the table
API:        REST + WebSocket
            GET  /campaigns/{id}/characters
            PATCH /characters/{id}
            WS   /campaigns/{id}/rolls
Storage:    PostgreSQL (JSONB)
Tech stack: TypeScript, React, Node.js, Socket.IO
```

---

## Example 200

**Intent:**
transactional email templates saas, devs send template id + data via api

**Spec:**
```
Type:       Web application (email template SaaS)
Auth:       Email + password login, API keys
Data model: Template(id, account_id, name, subject, html, version)
            Message(id, template_id -> Template, to_email, data_json, status, sent_at)
Features:   - Edit HTML email templates with variables and a live preview
            - Version templates and roll back
            - Send an email with template ID and JSON data through the API
            - Track delivery, bounce and open events
            - Test-send a template to yourself
API:        REST
            POST /v1/send
            POST /templates
            GET  /messages/{id}
            POST /webhooks/provider
Storage:    PostgreSQL
Tech stack: Node.js, Handlebars, Amazon SES, React
```

---

## Example 201

**Intent:**
participatory budgeting site for our district, people propose projects and vote how to spend 100k

**Spec:**
```
Type:       Web application (participatory budgeting)
Auth:       Resident verification by postcode and SMS code
Data model: Resident(id, phone_hash, postcode, verified)
            Proposal(id, title, description, cost_estimate, category, status)
            Ballot(id, resident_id -> Resident, submitted_at)
            BallotItem(ballot_id -> Ballot, proposal_id -> Proposal)
Features:   - Let residents submit project proposals with a cost estimate
            - Let staff review feasibility and publish proposals
            - Let each resident pick projects that fit within the total budget
            - Allow only one ballot per verified resident
            - Fund winning projects in vote order until the budget runs out
API:        REST
            POST /proposals
            GET  /proposals?status=published
            POST /ballots
            GET  /results
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio Verify
```

---

## Example 202

**Intent:**
tenants association: log repair issues in the building and track how long landlord takes

**Spec:**
```
Type:       Web application (tenant repair tracker)
Auth:       Email + password login, invite by flat number
Data model: Tenant(id, name, email, flat)
            Issue(id, tenant_id -> Tenant, category, description, photo_url, reported_on, fixed_on, status)
            Update(id, issue_id -> Issue, note, created_at)
Features:   - Report a repair issue with photos and category
            - Track days open for each issue
            - Show building-wide statistics of open issues and average fix time
            - Generate a PDF summary to send to the landlord
            - Let tenants add "me too" to shared problems like heating
API:        REST
            POST /issues
            POST /issues/{id}/updates
            GET  /stats
            GET  /report.pdf
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Express, PDFKit, React
```

---

## Example 203

**Intent:**
slack bot that pairs random coworkers for virtual coffee every two weeks

**Spec:**
```
Type:       Bot (Slack)
Data model: Member(slack_user_id, opted_in, timezone)
            Pairing(id, round, user_a, user_b, created_at)
Features:   - Let people opt in or out with a slash command
            - Pair opted-in members every two weeks, avoiding recent repeats
            - Prefer pairs with overlapping working hours
            - Open a group DM for each pair with an icebreaker question
Storage:    PostgreSQL
Tech stack: Python, Slack Bolt, APScheduler
```

---

## Example 204

**Intent:**
stamp collectors catalog and want list

**Spec:**
```
Type:       Web application (stamp collection catalog)
Auth:       Email + password login
Data model: Collector(id, name, email)
            Stamp(id, country, year, catalog_number, denomination, description, image_url)
            Holding(id, collector_id -> Collector, stamp_id -> Stamp, condition, mint, quantity)
            Want(collector_id -> Collector, stamp_id -> Stamp)
Features:   - Browse stamps by country and year
            - Mark stamps you own with condition
            - Keep a want list
            - Show other collectors who have duplicates of your wants
            - Show collection completion per country
API:        REST
            GET  /stamps?country={c}
            POST /holdings
            POST /wants
            GET  /matches
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 205

**Intent:**
water quality testing by school students at rivers, upload ph and nitrate results

**Spec:**
```
Type:       Web application (river water quality monitoring)
Auth:       Teacher accounts with email + password, class codes for students
Data model: School(id, name)
            Site(id, name, river, lat, lng)
            Sample(id, site_id -> Site, school_id -> School, ph, nitrate_mg_l, temperature_c, turbidity, sampled_at)
Features:   - Enter test kit readings for a river site
            - Validate values against possible ranges
            - Map sites coloured by latest quality
            - Compare readings between schools on the same river
            - Download data for science lessons
API:        REST
            POST /samples
            GET  /sites
            GET  /sites/{id}/samples
Storage:    PostgreSQL
Tech stack: Python, Flask, Leaflet, Chart.js
```

---

## Example 206

**Intent:**
Accessibility audit SaaS that crawls a website and reports WCAG problems every week.

**Spec:**
```
Type:       Web application (accessibility monitoring SaaS)
Auth:       Email + password login
Data model: Site(id, owner_id, root_url, max_pages)
            Scan(id, site_id -> Site, started_at, finished_at, pages_scanned)
            Violation(id, scan_id -> Scan, page_url, rule_id, impact, selector, help_url)
Features:   - Crawl up to a page limit from the root URL
            - Run axe-core checks on every page in a headless browser
            - Group violations by WCAG rule and impact
            - Compare with the previous scan to show new and fixed issues
            - Email a weekly report
API:        REST
            POST /sites
            POST /sites/{id}/scans
            GET  /scans/{id}/violations
Storage:    PostgreSQL
Tech stack: Node.js, Playwright, axe-core, React
```

---

## Example 207

**Intent:**
neighbours share car, book hours, split fuel and insurance costs

**Spec:**
```
Type:       Web application (shared car booking)
Auth:       Email + password login
Data model: Member(id, name, email)
            Booking(id, member_id -> Member, starts_at, ends_at, start_km, end_km)
            Expense(id, member_id -> Member, kind, amount, date, receipt_url)
Features:   - Book the car for a time slot without overlaps
            - Record odometer readings at start and end
            - Log fuel, insurance and repair expenses with receipts
            - Split costs monthly by kilometres driven
            - Show who owes whom
API:        REST
            GET  /bookings?week={date}
            POST /bookings
            POST /expenses
            GET  /settlement?month={m}
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 208

**Intent:**
fossil hunting finds log with location kept secret except to club

**Spec:**
```
Type:       Web application (fossil finds log)
Auth:       Email + password login, club membership
Data model: Member(id, name, email)
            Find(id, member_id -> Member, taxon, formation, period, lat, lng, photo_url, found_on, location_visibility)
Features:   - Log finds with taxon, rock formation and geological period
            - Hide exact locations from the public, showing only the region
            - Show exact locations to club members only
            - Browse finds by period and formation
API:        REST
            GET  /finds
            POST /finds
            GET  /finds/{id}
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Python, Django, Leaflet
```

---

## Example 209

**Intent:**
NPS survey saas, send to customers by email and show score trend

**Spec:**
```
Type:       Web application (NPS survey SaaS)
Auth:       Email + password login
Data model: Account(id, email, company)
            Contact(id, account_id -> Account, email, segment)
            SurveySend(id, contact_id -> Contact, token, sent_at)
            Response(id, send_id -> SurveySend, score, comment, responded_at)
Features:   - Import customers from CSV or API
            - Send an email with clickable 0-10 scores
            - Collect an optional comment after the score
            - Calculate NPS as promoters minus detractors
            - Show the NPS trend by month and segment
API:        REST
            POST /contacts
            POST /campaigns
            GET  /r/{token}?score={n}
            GET  /stats/nps
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Postmark API, Chartkick
```

---

## Example 210

**Intent:**
lego set swap

**Spec:**
```
Type:       Web application (LEGO set swap)
Auth:       Email + password login
Data model: Member(id, name, email, country)
            SetListing(id, member_id -> Member, set_number, name, complete, has_box, has_instructions)
            Want(member_id -> Member, set_number)
            Swap(id, a_listing_id -> SetListing, b_listing_id -> SetListing, status)
Features:   - List sets with completeness and box status
            - Look up set name and image by set number
            - Add sets to a want list
            - Find two-way swaps where each member wants the other's set
            - Leave feedback after a swap
API:        REST
            POST /listings
            POST /wants
            GET  /swaps/suggested
            POST /swaps
Storage:    PostgreSQL
Tech stack: Node.js, Express, Rebrickable API, React
```

---

## Example 211

**Intent:**
my coding meetup needs talk submissions and a way to vote which talks people want to see

**Spec:**
```
Type:       Web application (meetup talk proposals)
Auth:       GitHub OAuth login
Data model: Member(id, github_login, name)
            Talk(id, speaker_id -> Member, title, abstract, level, duration_min, status)
            Vote(talk_id -> Talk, member_id -> Member)
            Meetup(id, date, venue)
            Slot(meetup_id -> Meetup, talk_id -> Talk, order)
Features:   - Submit talk proposals with abstract and level
            - Upvote talks you want to see
            - Let organisers schedule top talks into meetups
            - Notify speakers when their talk is scheduled
API:        REST
            GET  /talks?sort=votes
            POST /talks
            POST /talks/{id}/vote
            POST /meetups/{id}/slots
Storage:    PostgreSQL
Tech stack: Go, HTMX
```

---

## Example 212

**Intent:**
site to rent out a community hall by the hour with a calendar and deposit

**Spec:**
```
Type:       Web application (hall booking)
Auth:       Email + password login for hirers and the hall manager
Data model: Room(id, name, capacity, hourly_rate, deposit)
            Booking(id, room_id -> Room, hirer_name, hirer_email, purpose, starts_at, ends_at, status, deposit_paid)
Features:   - Show a public availability calendar per room
            - Request a booking with purpose and times
            - Approve bookings and send an invoice with deposit
            - Take card payments online
            - Refund deposits after the event
API:        REST
            GET  /rooms/{id}/availability
            POST /bookings
            PATCH /bookings/{id}
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: PHP, Symfony, Stripe API, FullCalendar
```

---

## Example 213

**Intent:**
online sign language video dictionary where deaf community members upload signs

**Spec:**
```
Type:       Web application (sign language dictionary)
Auth:       Email + password login, reviewer role
Data model: Contributor(id, name, email, region)
            Entry(id, gloss, meaning, category)
            SignVideo(id, entry_id -> Entry, contributor_id -> Contributor, video_url, region, approved)
Features:   - Search words and watch sign videos
            - Upload a sign video recorded in the browser
            - Show regional variants of the same sign
            - Let reviewers approve videos before publishing
            - Play videos slowed down and looped
API:        REST
            GET  /entries?q={word}
            POST /entries/{id}/videos
            PATCH /videos/{id}
Storage:    PostgreSQL, S3 (videos)
Tech stack: Python, Django, MediaRecorder API
```

---

## Example 214

**Intent:**
SaaS: help center widget so customers search FAQ articles inside our app before opening a ticket

**Spec:**
```
Type:       Web application (in-app help widget SaaS)
Auth:       Email + password login, public widget key
Data model: Workspace(id, name, widget_key)
            Article(id, workspace_id -> Workspace, title, body_md, tags)
            SearchLog(id, workspace_id -> Workspace, query, results_count, clicked_article_id -> Article)
Features:   - Write FAQ articles in Markdown
            - Embed a help button that opens a search panel
            - Search articles with typo-tolerant full-text search
            - Show a contact form when nothing helps
            - Report searches with no results
API:        REST
            GET  /widget/{key}/search?q={text}
            POST /articles
            GET  /reports/no-results
Storage:    PostgreSQL, Meilisearch
Tech stack: Node.js, Preact, React
```

---

## Example 215

**Intent:**
compost drop off points map for my city where people check if bins are full

**Spec:**
```
Type:       Web application (compost drop-off map)
Data model: DropPoint(id, name, lat, lng, accepts, host)
            FillReport(id, drop_point_id -> DropPoint, level, reported_at)
Features:   - Show drop-off points on a map with what they accept
            - Report a bin as empty, half or full
            - Show the latest fill level and when it was reported
            - Notify hosts when a bin is reported full
API:        REST
            GET  /points
            POST /points/{id}/reports
Storage:    PostgreSQL
Tech stack: Node.js, Express, Leaflet
```

---

## Example 216

**Intent:**
I want a site for a citizen assembly: randomly select participants from volunteers balanced by age gender and area

**Spec:**
```
Type:       Web application (sortition for citizen assemblies)
Auth:       Email + password login for organisers
Data model: Volunteer(id, name, email, age_band, gender, area, education)
            Quota(id, attribute, value, target)
            Selection(id, run_at, seed)
            SelectedMember(selection_id -> Selection, volunteer_id -> Volunteer)
Features:   - Collect volunteer registrations with demographic answers
            - Set target quotas per attribute
            - Draw a random sample that meets all quotas
            - Publish the random seed so the draw can be verified
            - Draw replacements for people who decline
API:        REST
            POST /volunteers
            POST /quotas
            POST /selections
            GET  /selections/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, OR-Tools
```

---

## Example 217

**Intent:**
ok so me and friends make a lot of mixtapes / playlists and want a site to post them with a write up and others comment

**Spec:**
```
Type:       Web application (playlist sharing)
Auth:       Email + password login, Spotify OAuth
Data model: User(id, username, email)
            Mixtape(id, user_id -> User, title, writeup, cover_url, spotify_playlist_id)
            Track(id, mixtape_id -> Mixtape, position, artist, title, note)
            Comment(id, mixtape_id -> Mixtape, user_id -> User, body)
Features:   - Import a playlist from Spotify
            - Write a note for each track and an intro
            - Show the mixtape with an embedded player
            - Comment on mixtapes
            - Follow friends and see their new mixtapes
API:        REST
            POST /mixtapes/import
            GET  /mixtapes/{id}
            POST /mixtapes/{id}/comments
Storage:    PostgreSQL
Tech stack: Node.js, Next.js, Spotify Web API
```

---

## Example 218

**Intent:**
streamer donation page with goals and on-screen alerts

**Spec:**
```
Type:       Web application (stream donations)
Auth:       Twitch OAuth login for streamers
Data model: Streamer(id, twitch_id, name, payout_account_id)
            Goal(id, streamer_id -> Streamer, title, target_amount, current_amount)
            Donation(id, streamer_id -> Streamer, donor_name, amount, message, created_at)
Features:   - Show a donation page with a message box
            - Take card payments and pay out to the streamer
            - Show an alert overlay in OBS through a browser source URL
            - Show a goal progress bar overlay
            - Filter profanity in donation messages
API:        REST + WebSocket
            POST /{streamer}/donate
            WS   /overlay/{token}
            POST /goals
Storage:    PostgreSQL
Tech stack: Node.js, Stripe Connect, Socket.IO
```

---

## Example 219

**Intent:**
coin collectors want to estimate value of their collection using mintage and grade

**Spec:**
```
Type:       Web application (coin collection valuation)
Auth:       Email + password login
Data model: Collector(id, email)
            CoinType(id, country, denomination, year, mint_mark, mintage)
            PriceGuide(coin_type_id -> CoinType, grade, value)
            OwnedCoin(id, collector_id -> Collector, coin_type_id -> CoinType, grade, purchase_price)
Features:   - Add coins by country, year and mint mark
            - Select the grade on the Sheldon scale
            - Look up value from the price guide for that grade
            - Show total collection value and gain over purchase price
API:        REST
            GET  /coin-types?country={c}&year={y}
            POST /coins
            GET  /collection/value
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Razor Pages
```

---

## Example 220

**Intent:**
platform for small theatres to sell season subscriptions and let subscribers pick shows

**Spec:**
```
Type:       Web application (theatre subscriptions)
Auth:       Email + password login
Data model: Show(id, title, starts_on, ends_on)
            Performance(id, show_id -> Show, starts_at, seats_left)
            Subscription(id, patron_email, package, shows_allowed, paid)
            Reservation(id, subscription_id -> Subscription, performance_id -> Performance, seats)
Features:   - Sell 3-show and 6-show season packages
            - Let subscribers choose performances for each show
            - Prevent picking more shows than the package allows
            - Let subscribers exchange a date up to 48 hours before
            - Email tickets as PDF
API:        REST
            POST /subscriptions
            GET  /performances
            POST /reservations
            PATCH /reservations/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe API
```

---

## Example 221

**Intent:**
remote team icebreaker questions bot for microsoft teams

**Spec:**
```
Type:       Bot (Microsoft Teams)
Data model: Question(id, text, used_on)
            Answer(id, question_id -> Question, user_id, text)
Features:   - Post a daily icebreaker question in a channel
            - Collect answers in an adaptive card
            - Reveal all answers at the end of the day
            - Let members suggest new questions
Storage:    Azure Table Storage
Tech stack: C#, Bot Framework SDK, Azure Functions
```

---

## Example 222

**Intent:**
a tool to share and rate local hiking photos? no wait, specifically for sharing sunset photos and predicting good sunsets

**Spec:**
```
Type:       Web application (sunset photo sharing)
Auth:       Email + password login
Data model: User(id, username, email)
            SunsetPhoto(id, user_id -> User, image_url, lat, lng, taken_at, rating_avg)
            Rating(photo_id -> SunsetPhoto, user_id -> User, stars)
Features:   - Upload sunset photos with time and place
            - Rate photos from 1 to 5 stars
            - Predict tonight's sunset quality from cloud cover forecasts
            - Show a map of the best rated sunset spots
API:        REST
            POST /photos
            POST /photos/{id}/ratings
            GET  /forecast?lat={lat}&lng={lng}
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, FastAPI, Open-Meteo API, Svelte
```

---

## Example 223

**Intent:**
hi, we are association of Syrian doctors in Germany, we need site where members find each other by specialty and city, and share job offers

**Spec:**
```
Type:       Web application (professional association network)
Auth:       Email + password login, admin verification of medical license
Data model: Member(id, name, email, specialty, city, languages, verified)
            JobOffer(id, poster_id -> Member, title, hospital, city, description, deadline)
Features:   - Register with specialty and city and upload license proof
            - Let admins verify members
            - Search members by specialty and city
            - Post and browse job offers
            - Show the site in Arabic, German and English (right-to-left for Arabic)
API:        REST
            GET  /members?specialty={s}&city={c}
            POST /jobs
            PATCH /members/{id}/verify
Storage:    PostgreSQL, S3 (documents)
Tech stack: Python, Django (i18n)
```

---

## Example 224

**Intent:**
bike repair workshop queue at our community bike kitchen

**Spec:**
```
Type:       Web application (bike workshop queue)
Data model: Visit(id, name, phone, bike_issue, joined_at, stand_number, status)
            Stand(id, number, mechanic_name, busy)
Features:   - Join the queue at the door from a tablet
            - Assign the next person to a free repair stand
            - Show the queue and estimated wait on a screen
            - Text people when their turn is near
            - Count visits and repair types per evening
API:        REST
            POST /queue
            POST /stands/{id}/next
            GET  /queue
Storage:    SQLite
Tech stack: Node.js, Express, Twilio API
```

---

## Example 225

**Intent:**
SaaS for managing software license keys for my desktop apps

**Spec:**
```
Type:       Web application (license key management SaaS)
Auth:       Email + password login for vendors, API key for apps
Data model: Product(id, vendor_id, name)
            License(id, product_id -> Product, key, customer_email, max_activations, expires_at, revoked)
            Activation(id, license_id -> License, machine_fingerprint, activated_at)
Features:   - Generate signed license keys after a purchase webhook
            - Activate a license on a machine up to the limit
            - Validate licenses offline with a public key signature
            - Revoke or extend licenses
            - Let customers deactivate old machines
API:        REST
            POST /v1/licenses
            POST /v1/activate
            POST /v1/validate
            DELETE /v1/activations/{id}
Storage:    PostgreSQL
Tech stack: Rust, Axum, Ed25519 signatures
```

---

## Example 226

**Intent:**
retro computer club site to log restored machines and lend them out for events

**Spec:**
```
Type:       Web application (vintage computer collection)
Auth:       Email + password login
Data model: Member(id, name, email)
            Machine(id, owner_id -> Member, model, year, condition, restoration_notes, photo_url)
            Loan(id, machine_id -> Machine, event, from_date, to_date)
Features:   - Catalog machines with model, year and condition
            - Write restoration logs with photos
            - Request machines for exhibitions and events
            - Show which machines are on loan
API:        REST
            GET  /machines
            POST /machines
            POST /machines/{id}/loans
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 227

**Intent:**
anonymous peer support chat for students, trained volunteers answer

**Spec:**
```
Type:       Web application (anonymous peer support chat)
Auth:       Anonymous sessions for students, email + password with 2FA for volunteers
Data model: Volunteer(id, name, email, trained_on, on_shift)
            Conversation(id, started_at, ended_at, volunteer_id -> Volunteer, escalated)
            Message(id, conversation_id -> Conversation, from_volunteer, body, sent_at)
Features:   - Start an anonymous chat without an account
            - Route chats to volunteers who are on shift
            - Show crisis line numbers and allow escalation to staff
            - Delete transcripts after 30 days
            - Let supervisors see queue length
API:        WebSocket + REST
            POST /conversations
            WS   /conversations/{id}
            POST /conversations/{id}/escalate
Storage:    PostgreSQL (encrypted transcripts)
Tech stack: Node.js, Socket.IO, React
```

---

## Example 228

**Intent:**
hackathon team matcher, people list skills and idea, get suggestions for teammates

**Spec:**
```
Type:       Web application (hackathon team matching)
Auth:       GitHub OAuth login
Data model: Hacker(id, name, github_login, skills, roles_wanted, looking)
            Idea(id, owner_id -> Hacker, title, needed_roles)
            Invite(id, idea_id -> Idea, hacker_id -> Hacker, status)
Features:   - List skills and the role you want (frontend, backend, design, ML)
            - Post an idea with the roles it needs
            - Suggest hackers who fill missing roles for an idea
            - Invite hackers and accept invites
            - Hide people who already have a full team
API:        REST
            POST /ideas
            GET  /ideas/{id}/suggestions
            POST /invites
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 229

**Intent:**
ham radio net check-in logger

**Spec:**
```
Type:       Web application (radio net control log)
Auth:       Email + password login for net controllers
Data model: Net(id, name, frequency, scheduled_at)
            Session(id, net_id -> Net, controller_callsign, started_at)
            CheckIn(id, session_id -> Session, callsign, name, location, traffic, checked_in_at)
Features:   - Start a net session and log check-ins quickly by callsign
            - Autofill name and location from previous check-ins
            - Flag stations with traffic to pass
            - Show a live check-in list for other operators
            - Export session logs
API:        REST
            POST /sessions
            POST /sessions/{id}/checkins
            GET  /sessions/{id}
Storage:    SQLite
Tech stack: Python, FastAPI, HTMX
```

---

## Example 230

**Intent:**
co-housing community: sign up for shared dinners and cooking rotation

**Spec:**
```
Type:       Web application (common house meals)
Auth:       Email + password login per household
Data model: Household(id, name, adults, kids)
            Meal(id, date, menu, cook_household_id -> Household, signup_deadline, cost_total)
            MealSignup(meal_id -> Meal, household_id -> Household, adults, kids, vegetarian)
Features:   - Post upcoming meals with menu and cooks
            - Sign up adults and kids before the deadline
            - Rotate cooking duty fairly across households
            - Split the meal cost per portion with half price for kids
            - Show monthly balances per household
API:        REST
            GET  /meals
            POST /meals/{id}/signups
            GET  /balances
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 231

**Intent:**
tool where youtubers find other youtubers in their niche to collaborate

**Spec:**
```
Type:       Web application (creator collaboration matching)
Auth:       Google sign-in with YouTube channel verification
Data model: Creator(id, channel_id, name, niche, subscribers, avg_views, language)
            CollabPost(id, creator_id -> Creator, idea, wanted_niche)
            Message(id, from_id -> Creator, to_id -> Creator, body, sent_at)
Features:   - Verify channel ownership through YouTube OAuth
            - Pull subscriber and view statistics from the YouTube Data API
            - Search creators by niche, language and size
            - Post collaboration ideas
            - Message other creators
API:        REST
            GET  /creators?niche={n}
            POST /collab-posts
            POST /messages
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, YouTube Data API, React
```

---

## Example 232

**Intent:**
Write a spec for an RSVP-only events API used by several community websites we run

**Spec:**
```
Type:       REST API service (shared RSVP backend)
Auth:       API key per website, signed email tokens for attendees
Data model: Site(id, name, api_key_hash)
            Event(id, site_id -> Site, title, starts_at, capacity)
            Rsvp(id, event_id -> Event, name, email, status, token)
Features:   - Create events for each website
            - Accept RSVPs and move extra people to a waitlist
            - Promote waitlisted people when someone cancels
            - Send confirmation and cancellation emails with signed links
            - Return attendee lists to site admins
API:        REST
            POST /v1/events
            POST /v1/events/{id}/rsvps
            DELETE /v1/rsvps/{token}
            GET  /v1/events/{id}/attendees
Storage:    PostgreSQL
Tech stack: Python, FastAPI, SQLAlchemy
```

---

## Example 233

**Intent:**
light pollution measurement crowd map using phone readings

**Spec:**
```
Type:       Mobile application with backend (sky brightness mapping)
Auth:       Anonymous device ID, optional account
Data model: Measurement(id, device_id, lat, lng, sky_brightness_mag, method, cloud_cover, measured_at)
Features:   - Guide the user to point the phone at the zenith on a clear night
            - Estimate sky brightness from the camera or a stars-visible count
            - Upload readings with location and time
            - Show a heatmap of measurements
            - Filter out readings taken during moonlight
API:        REST
            POST /measurements
            GET  /measurements?bbox={...}
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin (Android), Python, FastAPI
```

---

## Example 234

**Intent:**
mentors book office hours with startup founders in our accelerator

**Spec:**
```
Type:       Web application (accelerator office hours)
Auth:       Google sign-in
Data model: Mentor(id, name, email, expertise)
            Startup(id, name, founder_emails)
            OfficeHour(id, mentor_id -> Mentor, starts_at, duration_min, booked_by -> Startup, topic)
            Feedback(id, office_hour_id -> OfficeHour, rating, notes)
Features:   - Let mentors publish office hour slots
            - Let startups book slots with a topic
            - Limit each startup to two bookings per week
            - Collect feedback after each session
            - Show program managers mentor usage stats
API:        REST
            GET  /office-hours?available=true
            POST /office-hours/{id}/book
            POST /office-hours/{id}/feedback
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 235

**Intent:**
small game: browser game where players build a shared pixel mural one pixel every 5 min, for our community

**Spec:**
```
Type:       Browser game (collaborative pixel canvas)
Auth:       Discord OAuth login
Data model: Pixel(x, y, color, user_id, placed_at)
            User(id, discord_id, last_placed_at)
Features:   - Show a 500x500 canvas with zoom and pan
            - Place one pixel from a 16-colour palette every 5 minutes
            - Broadcast pixel changes to all players in real time
            - Show who placed a pixel on hover
            - Take hourly snapshots for a timelapse
API:        REST + WebSocket
            GET  /canvas.png
            POST /pixels
            WS   /live
Storage:    Redis (bitfield canvas), PostgreSQL (history)
Tech stack: TypeScript, Node.js, ws, HTML Canvas
```

---

## Example 236

**Intent:**
newsroom tip line where public sends anonymous tips and documents securely

**Spec:**
```
Type:       Web application (secure tip submission)
Auth:       Anonymous submitters with a generated codename, journalist login with hardware 2FA
Data model: Submission(id, codename_hash, message_encrypted, created_at)
            Attachment(id, submission_id -> Submission, file_encrypted_url)
            Reply(id, submission_id -> Submission, body_encrypted)
Features:   - Accept tips and files without collecting IP addresses
            - Encrypt submissions with the newsroom's public key
            - Give submitters a codename to check for replies
            - Strip metadata from uploaded documents
            - Let journalists decrypt on an offline machine
API:        REST
            POST /submissions
            GET  /replies?codename={c}
Storage:    Encrypted filesystem
Tech stack: Python, Flask, GnuPG, Tor onion service
```

---

## Example 237

**Intent:**
my friends and I do a fantasy league for reality tv show, points for things contestants do each episode

**Spec:**
```
Type:       Web application (reality TV fantasy league)
Auth:       Email + password login
Data model: League(id, name, invite_code)
            Contestant(id, name, eliminated_episode)
            Team(id, league_id -> League, owner_id, name)
            Pick(team_id -> Team, contestant_id -> Contestant)
            ScoringEvent(id, episode, contestant_id -> Contestant, action, points)
Features:   - Draft contestants into teams
            - Let the commissioner enter scoring events after each episode
            - Calculate team points automatically
            - Show a league standings table
            - Lock picks once an episode airs
API:        REST
            POST /leagues
            POST /teams/{id}/picks
            POST /episodes/{n}/events
            GET  /leagues/{id}/standings
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 238

**Intent:**
feedback on design mockups saas, clients click on image to leave pinned comments

**Spec:**
```
Type:       Web application (design feedback SaaS)
Auth:       Email + password login for designers, share links for clients
Data model: Project(id, owner_id, name)
            Mockup(id, project_id -> Project, version, image_url)
            Pin(id, mockup_id -> Mockup, x_pct, y_pct, author_name, resolved)
            PinComment(id, pin_id -> Pin, author_name, body)
Features:   - Upload mockup images with versions
            - Share a review link with clients without an account
            - Click anywhere on the image to place a numbered pin and comment
            - Resolve pins and compare versions side by side
            - Email the designer a digest of new comments
API:        REST
            POST /projects/{id}/mockups
            POST /mockups/{id}/pins
            POST /pins/{id}/comments
            PATCH /pins/{id}
Storage:    PostgreSQL, S3 (images)
Tech stack: TypeScript, React, Node.js, Express
```

---

## Example 239

**Intent:**
crowdfunding for community projects like playground with all or nothing

**Spec:**
```
Type:       Web application (civic crowdfunding)
Auth:       Email + password login
Data model: Project(id, owner_id, title, description, goal, deadline, status)
            Pledge(id, project_id -> Project, backer_email, amount, payment_intent_id, status)
            Update(id, project_id -> Project, body, posted_at)
Features:   - Publish a project with goal and deadline
            - Accept pledges by authorising cards without charging
            - Capture all payments only if the goal is met by the deadline
            - Cancel authorisations if the goal is missed
            - Post progress updates to backers
API:        REST
            POST /projects
            POST /projects/{id}/pledges
            POST /projects/{id}/updates
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe API, Celery
```

---

## Example 240

**Intent:**
dart league scoring app for pubs with live scoreboard on tv

**Spec:**
```
Type:       Web application (darts scoring)
Auth:       PIN login for scorers
Data model: Player(id, name, team)
            Match(id, format, home_team, away_team, started_at)
            Leg(id, match_id -> Match, player_id -> Player, starting_score, winner_id -> Player)
            Throw(id, leg_id -> Leg, player_id -> Player, score, darts_used)
Features:   - Enter visit scores on a tablet keypad
            - Subtract from 501 and detect busts and checkouts
            - Suggest checkout routes
            - Show a live scoreboard on a TV browser
            - Track averages per player across the season
API:        REST + WebSocket
            POST /legs/{id}/throws
            WS   /matches/{id}
            GET  /players/{id}/stats
Storage:    PostgreSQL
Tech stack: Node.js, Socket.IO, Vue.js
```

---

## Example 241

**Intent:**
foraging spots site but we want privacy - only share spots with trusted friends

**Spec:**
```
Type:       Web application (private foraging map)
Auth:       Email + password login
Data model: User(id, name, email)
            Spot(id, owner_id -> User, plant, lat, lng, season_months, notes)
            Share(spot_id -> Spot, friend_id -> User)
            Friendship(user_id -> User, friend_id -> User, status)
Features:   - Save spots privately on a map with plant and season
            - Add friends by invitation
            - Share individual spots with chosen friends
            - Show which spots are in season this month
            - Fuzz coordinates when sharing at low trust level
API:        REST
            GET  /spots
            POST /spots
            POST /spots/{id}/shares
            POST /friends
Storage:    PostgreSQL with PostGIS
Tech stack: Node.js, Express, MapLibre GL
```

---

## Example 242

**Intent:**
system for our scout group: badge progress per kid, parents can see

**Spec:**
```
Type:       Web application (scout badge tracking)
Auth:       Email + password login for leaders and parents
Data model: Scout(id, name, section, parent_email)
            Badge(id, name, section)
            Requirement(id, badge_id -> Badge, text)
            Completion(scout_id -> Scout, requirement_id -> Requirement, signed_off_by, date)
Features:   - Show each badge's requirements
            - Let leaders sign off requirements for several scouts at once
            - Show a scout's badge progress bars
            - Let parents see only their own child's progress
            - List badges ready to award at the next ceremony
API:        REST
            GET  /scouts/{id}/progress
            POST /completions
            GET  /awards/ready
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Livewire
```

---

## Example 243

**Intent:**
SaaS that checks broken links on customer websites nightly

**Spec:**
```
Type:       Web application (broken link checker SaaS)
Auth:       Email + password login
Data model: Site(id, owner_id, root_url, schedule)
            Crawl(id, site_id -> Site, started_at, pages, links_checked)
            BrokenLink(id, crawl_id -> Crawl, source_page, target_url, status_code)
Features:   - Crawl a website nightly respecting robots.txt
            - Check internal and external links with HEAD requests
            - List broken links with the page they appear on
            - Email a report only when new broken links appear
API:        REST
            POST /sites
            GET  /sites/{id}/broken-links
            POST /sites/{id}/crawl
Storage:    PostgreSQL
Tech stack: Python, Scrapy, Django
```

---

## Example 244

**Intent:**
wanna make site for people to post their aquarium setups with fish list and water params

**Spec:**
```
Type:       Web application (aquarium showcase)
Auth:       Email + password login
Data model: Keeper(id, username, email)
            Tank(id, keeper_id -> Keeper, name, volume_l, kind, photo_url)
            Inhabitant(id, tank_id -> Tank, species, count)
            WaterTest(id, tank_id -> Tank, ph, ammonia, nitrite, nitrate, temp_c, tested_at)
Features:   - Post tanks with photos and volume
            - List fish and plants in each tank
            - Log water tests and chart them over time
            - Warn about incompatible species in the same tank
            - Browse tanks by type (freshwater, reef, planted)
API:        REST
            POST /tanks
            POST /tanks/{id}/inhabitants
            POST /tanks/{id}/tests
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Chart.js
```

---

## Example 245

**Intent:**
I organize a monthly clothes swap event. Need a website where people register what they bring and get tokens to take items.

**Spec:**
```
Type:       Web application (clothes swap event)
Auth:       Email login with magic link
Data model: Participant(id, name, email, tokens)
            SwapEvent(id, date, venue)
            ItemDropOff(id, event_id -> SwapEvent, participant_id -> Participant, category, quantity, tokens_awarded)
Features:   - Register for an upcoming swap
            - Pre-register items you will bring by category
            - Award tokens at check-in after volunteers inspect items
            - Spend tokens at the event from a phone screen
            - Show how many items were swapped instead of thrown away
API:        REST
            POST /events/{id}/register
            POST /dropoffs
            POST /participants/{id}/spend
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 246

**Intent:**
tool for our dance studio recital: costume sizes, dance lineup, and ticket sales

**Spec:**
```
Type:       Web application (dance recital management)
Auth:       Email + password login for staff and parents
Data model: Dancer(id, name, parent_email, class_name)
            Costume(id, class_name, description, price)
            CostumeOrder(id, dancer_id -> Dancer, costume_id -> Costume, size, paid)
            Routine(id, class_name, song, order_in_show)
            Ticket(id, buyer_email, seat, paid)
Features:   - Collect costume sizes and payments from parents
            - Arrange the routine running order and check quick changes
            - Warn when a dancer is in back-to-back routines
            - Sell reserved-seat tickets
API:        REST
            POST /costume-orders
            PUT  /routines/order
            POST /tickets
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe API
```

---

## Example 247

**Intent:**
SaaS for collecting video testimonials from customers through a link

**Spec:**
```
Type:       Web application (video testimonials SaaS)
Auth:       Email + password login for businesses
Data model: Business(id, name, logo_url)
            Campaign(id, business_id -> Business, prompt_questions, slug)
            Testimonial(id, campaign_id -> Campaign, name, video_url, transcript, approved)
Features:   - Share a link where customers record a video in the browser
            - Show prompt questions while recording
            - Transcribe videos automatically
            - Approve testimonials and embed a wall of them on a website
API:        REST
            GET  /t/{slug}
            POST /t/{slug}/testimonials
            PATCH /testimonials/{id}
            GET  /embed/{business}.js
Storage:    PostgreSQL, S3 (videos)
Tech stack: Node.js, Next.js, MediaRecorder API, Whisper API
```

---

## Example 248

**Intent:**
cat colony care schedule for volunteers feeding street cats

**Spec:**
```
Type:       Web application (community cat care)
Auth:       Email + password login
Data model: Volunteer(id, name, phone)
            Colony(id, name, lat, lng, cat_count)
            Cat(id, colony_id -> Colony, name, description, neutered, photo_url)
            Feeding(id, colony_id -> Colony, volunteer_id -> Volunteer, date, done, notes)
Features:   - Assign daily feeding shifts per colony
            - Mark feedings done and note sick cats
            - Track trap-neuter-return status per cat
            - Remind volunteers of their feeding day by SMS
API:        REST
            GET  /colonies
            POST /feedings
            PATCH /cats/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, Twilio API
```

---

## Example 249

**Intent:**
newsletter sponsorship marketplace where brands book ad slots in newsletters

**Spec:**
```
Type:       Web application (newsletter ad marketplace)
Auth:       Email + password login, publisher and advertiser roles
Data model: Newsletter(id, publisher_id, name, topic, subscribers, open_rate)
            AdSlot(id, newsletter_id -> Newsletter, send_date, price, status)
            Booking(id, slot_id -> AdSlot, advertiser_id, ad_copy, link, paid)
Features:   - List newsletters with audience size and open rate
            - Publish available ad slots by date
            - Book and pay for a slot, holding funds in escrow
            - Let publishers approve the ad copy
            - Report clicks on the tracked link after sending
API:        REST
            GET  /newsletters?topic={t}
            POST /slots/{id}/bookings
            PATCH /bookings/{id}
            GET  /bookings/{id}/clicks
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe Connect
```

---

## Example 250

**Intent:**
church prayer request wall

**Spec:**
```
Type:       Web application (prayer requests)
Auth:       Email + password login for members, pastor role
Data model: Member(id, name, email)
            Request(id, member_id -> Member, text, visibility, created_at, answered)
            Praying(request_id -> Request, member_id -> Member)
Features:   - Post a request publicly or only to pastors
            - Click "I'm praying" to encourage the requester
            - Mark a request as answered with an update
            - Send a weekly email of new requests
API:        REST
            GET  /requests
            POST /requests
            POST /requests/{id}/praying
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 251

**Intent:**
invasive plant reporting for hikers

**Spec:**
```
Type:       Mobile application with backend (invasive species reporting)
Auth:       Optional account, anonymous reports allowed
Data model: Species(id, name, photo_url, priority)
            Report(id, species_id -> Species, lat, lng, patch_size_m2, photo_url, reported_at, verified)
            Removal(id, report_id -> Report, removed_on, volunteers)
Features:   - Identify species using a photo guide
            - Report a patch with GPS location and size
            - Save reports offline and upload when back in signal
            - Let rangers verify reports and plan removal days
            - Show a map of reported and removed patches
API:        REST
            POST /reports
            GET  /reports?bbox={...}
            PATCH /reports/{id}
            POST /reports/{id}/removals
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: React Native, Expo, Node.js
```

---

## Example 252

**Intent:**
social media post scheduler for small nonprofits, one place to post to facebook instagram and mastodon

**Spec:**
```
Type:       Web application (social media scheduler)
Auth:       Email + password login, OAuth connections to each network
Data model: Organisation(id, name)
            Account(id, org_id -> Organisation, network, access_token, handle)
            Post(id, org_id -> Organisation, text, media_urls, scheduled_at, status)
            PostTarget(post_id -> Post, account_id -> Account, external_id, error)
Features:   - Connect Facebook, Instagram and Mastodon accounts
            - Write a post once and choose target accounts
            - Schedule posts on a calendar
            - Publish at the scheduled time with a background worker
            - Show errors per network and retry
API:        REST
            POST /posts
            GET  /calendar?month={m}
            POST /accounts/connect/{network}
Storage:    PostgreSQL
Tech stack: Python, Django, Celery, Meta Graph API, Mastodon API
```

---

## Example 253

**Intent:**
i want a site for frog call surveys where volunteers upload short audio clips from ponds at night

**Spec:**
```
Type:       Web application (amphibian call survey)
Auth:       Email + password login
Data model: Volunteer(id, name, email)
            Pond(id, name, lat, lng)
            Visit(id, pond_id -> Pond, volunteer_id -> Volunteer, visited_at, air_temp_c)
            Clip(id, visit_id -> Visit, audio_url, species_guess, verified_species)
Features:   - Register ponds and log night visits
            - Upload short audio clips with a species guess
            - Let experts verify species from the clip and spectrogram
            - Show species presence per pond over the years
API:        REST
            POST /visits
            POST /visits/{id}/clips
            PATCH /clips/{id}
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, Django, wavesurfer.js
```

---

## Example 254

**Intent:**
Customer onboarding checklist SaaS, b2b companies give each new client a shared checklist portal

**Spec:**
```
Type:       Web application (client onboarding portal SaaS)
Auth:       Email + password login for vendors, magic links for clients
Data model: Vendor(id, name)
            Template(id, vendor_id -> Vendor, name, tasks_json)
            ClientPlan(id, template_id -> Template, client_name, due_date)
            Task(id, plan_id -> ClientPlan, title, owner_side, due_on, done, file_url)
Features:   - Create onboarding templates with tasks for both sides
            - Start a plan for a new client from a template
            - Share a client portal link to see and complete tasks
            - Upload files on tasks
            - Send reminders for overdue tasks
API:        REST
            POST /templates
            POST /plans
            GET  /portal/{token}
            PATCH /tasks/{id}
Storage:    PostgreSQL, S3 (files)
Tech stack: TypeScript, Remix, Prisma
```

---

## Example 255

**Intent:**
review request saas for local businesses: text customers a link to leave a google review

**Spec:**
```
Type:       Web application (review request SaaS)
Auth:       Email + password login
Data model: Business(id, name, google_place_id, sms_template)
            Customer(id, business_id -> Business, name, phone)
            ReviewRequest(id, customer_id -> Customer, sent_at, clicked_at, rating)
Features:   - Add customers manually or by CSV
            - Send an SMS with a link after a visit
            - Ask for a star rating first and send 4-5 stars to Google
            - Collect private feedback from lower ratings
            - Show click and review rates
API:        REST
            POST /customers
            POST /requests
            GET  /r/{token}
            GET  /stats
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Twilio API
```

---

## Example 256

**Intent:**
a quick way for my improv troupe to vote on show suggestions from audience via phone

**Spec:**
```
Type:       Web application (live audience voting)
Data model: Show(id, code, host_token)
            Prompt(id, show_id -> Show, question, open)
            Suggestion(id, prompt_id -> Prompt, text, votes)
Features:   - Show a QR code on stage to join the show
            - Let the audience submit suggestions for the current prompt
            - Vote on suggestions in real time
            - Show the top suggestion on the host's screen
API:        REST + WebSocket
            POST /shows/{code}/suggestions
            POST /suggestions/{id}/vote
            WS   /shows/{code}
Storage:    Redis
Tech stack: Node.js, Socket.IO, Svelte
```

---

## Example 257

**Intent:**
image resizing CDN service for our customers, urls with width param

**Spec:**
```
Type:       REST API service (image transformation)
Auth:       Signed URLs per customer
Data model: Customer(id, name, origin_url, signing_key)
            Variant(cache_key, customer_id -> Customer, width, format, size_bytes)
Features:   - Fetch the original image from the customer's origin
            - Resize, crop and convert to WebP or AVIF on the fly
            - Verify the URL signature to block abuse
            - Cache variants and serve them through a CDN
            - Report bandwidth per customer
API:        REST
            GET  /{customer}/{path}?w={width}&fmt={format}&sig={sig}
            GET  /customers/{id}/usage
Storage:    S3 (variant cache), PostgreSQL
Tech stack: Go, libvips, CloudFront
```

---

## Example 258

**Intent:**
astronomy club equipment loan, members borrow telescopes for a month

**Spec:**
```
Type:       Web application (telescope loan program)
Auth:       Email + password login
Data model: Member(id, name, email, joined_on)
            Telescope(id, name, aperture_mm, mount, accessories, status)
            Loan(id, telescope_id -> Telescope, member_id -> Member, out_on, due_on, returned_on)
            Waitlist(telescope_id -> Telescope, member_id -> Member, added_at)
Features:   - Browse loaner telescopes with accessories lists
            - Join a waitlist for a telescope
            - Offer a telescope to the next person when returned
            - Check accessories at return with a checklist
API:        REST
            GET  /telescopes
            POST /telescopes/{id}/waitlist
            POST /loans
            PATCH /loans/{id}
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 259

**Intent:**
platform connecting retired teachers with kids who need free homework help online

**Spec:**
```
Type:       Web application (volunteer homework help)
Auth:       Email + password login, background-checked tutors, parent accounts for children
Data model: Tutor(id, name, email, subjects, grades, background_check_ok)
            Parent(id, name, email)
            Child(id, parent_id -> Parent, first_name, grade)
            HelpSession(id, child_id -> Child, tutor_id -> Tutor, subject, starts_at, room_url, recorded)
Features:   - Let parents request help for a child by subject
            - Match tutors who teach that subject and grade
            - Run sessions in a video room with a shared whiteboard
            - Record sessions for safeguarding
            - Allow only tutors with a passed background check
API:        REST
            POST /requests
            GET  /tutors/available
            POST /sessions
Storage:    PostgreSQL, S3 (recordings)
Tech stack: Node.js, NestJS, Jitsi Meet, React
```

---

## Example 260

**Intent:**
lol i need a site where my friend group rates every burger place in town and keeps a ranking

**Spec:**
```
Type:       Web application (friend group food rankings)
Auth:       Email + password login, invite code
Data model: Friend(id, name, email)
            Place(id, name, address)
            Rating(place_id -> Place, friend_id -> Friend, taste, value, fries, notes, visited_on)
Features:   - Add burger places
            - Rate taste, value and fries from 1 to 10
            - Show an overall ranking by average score
            - Show who disagrees the most on each place
API:        REST
            GET  /places
            POST /places
            POST /places/{id}/ratings
Storage:    SQLite
Tech stack: Node.js, Express, EJS
```

---

## Example 261

**Intent:**
PDF generation API: send HTML template and JSON data, get invoice PDF back

**Spec:**
```
Type:       REST API service (PDF generation)
Auth:       API key per account
Data model: Account(id, email, api_key_hash, plan)
            Template(id, account_id -> Account, name, html, css)
            Render(id, template_id -> Template, pages, duration_ms, created_at)
Features:   - Store HTML/CSS templates with placeholders
            - Render a PDF from a template ID and JSON data
            - Support headers, footers and page numbers
            - Return the PDF directly or as a temporary download URL
            - Count renders per month for billing
API:        REST
            POST /v1/templates
            POST /v1/render
            GET  /v1/usage
Storage:    PostgreSQL, S3 (temporary PDFs)
Tech stack: Python, FastAPI, WeasyPrint, Jinja2
```

---

## Example 262

**Intent:**
I'm a librarian at a small public library and we want to start a "human library" event where people can book 20 minute conversations with volunteers who have unusual life stories (refugee, firefighter, etc). Need online booking per time slot.

**Spec:**
```
Type:       Web application (human library booking)
Auth:       Email + password login for librarians
Data model: Book(id, title, short_description, volunteer_name)
            Event(id, date, location)
            Slot(id, event_id -> Event, book_id -> Book, starts_at, reader_name, reader_email)
Features:   - Publish "books" (volunteers) with a title and description
            - Generate 20-minute slots per book for an event
            - Let readers book one slot per book with an email
            - Send reminder emails on the day
            - Print the day's schedule for each volunteer
API:        REST
            GET  /events/{id}/books
            POST /slots/{id}/book
            GET  /events/{id}/schedule
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 263

**Intent:**
feature request voting inside our app via widget

**Spec:**
```
Type:       Web application (in-app feature voting)
Auth:       Identified users passed from the host app with a signed JWT
Data model: Product(id, name, jwt_secret)
            Request(id, product_id -> Product, title, details, status, votes)
            Vote(request_id -> Request, external_user_id)
Features:   - Embed a widget that lists requests inside the app
            - Identify users from the host app without another login
            - Vote and submit new requests from the widget
            - Show status labels (under review, planned, shipped)
API:        REST
            GET  /widget/requests
            POST /widget/requests
            POST /widget/requests/{id}/vote
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, Preact
```

---

## Example 264

**Intent:**
tree planting tracker for our town, volunteers record each tree and later check if it survived

**Spec:**
```
Type:       Web application (tree planting tracker)
Auth:       Email + password login
Data model: Tree(id, species, lat, lng, planted_on, planted_by, photo_url)
            Checkup(id, tree_id -> Tree, checked_on, status, height_cm, photo_url)
Features:   - Record new trees with species, location and photo
            - Schedule yearly checkups for each tree
            - Log survival status and height
            - Show survival rate per species
            - Map all trees coloured by health
API:        REST
            POST /trees
            POST /trees/{id}/checkups
            GET  /stats/survival
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Flask, Leaflet
```

---

## Example 265

**Intent:**
grupo de estudio de programación, queremos web para compartir ejercicios y soluciones, in english interface is ok

**Spec:**
```
Type:       Web application (coding study group)
Auth:       GitHub OAuth login
Data model: Member(id, github_login)
            Exercise(id, author_id -> Member, title, description, difficulty, week)
            Solution(id, exercise_id -> Exercise, member_id -> Member, language, code)
            Comment(id, solution_id -> Solution, member_id -> Member, body)
Features:   - Post weekly exercises with difficulty
            - Submit solutions with syntax highlighting
            - Hide other solutions until you submit yours
            - Comment on solutions
API:        REST
            GET  /exercises?week={n}
            POST /exercises/{id}/solutions
            POST /solutions/{id}/comments
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, highlight.js
```

---

## Example 266

**Intent:**
gift card SaaS for independent shops to sell digital gift cards online

**Spec:**
```
Type:       Web application (digital gift card SaaS)
Auth:       Email + password login for shops
Data model: Shop(id, name, logo_url, payout_account_id)
            GiftCard(id, shop_id -> Shop, code, initial_amount, balance, recipient_email, message, expires_on)
            Redemption(id, card_id -> GiftCard, amount, redeemed_at)
Features:   - Sell gift cards on a hosted shop page
            - Email the card with a code and QR to the recipient
            - Redeem part of the balance at the counter
            - Show outstanding gift card liability
API:        REST
            POST /shops/{id}/cards/checkout
            GET  /cards/{code}
            POST /cards/{code}/redeem
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Stripe Connect, Vue.js
```

---

## Example 267

**Intent:**
wine tasting club notes

**Spec:**
```
Type:       Web application (wine tasting club)
Auth:       Email + password login
Data model: Member(id, name, email)
            Tasting(id, date, theme, host_id -> Member)
            Wine(id, tasting_id -> Tasting, producer, name, vintage, region, price)
            Note(id, wine_id -> Wine, member_id -> Member, score, aroma, palate)
Features:   - Create a tasting with a theme and wines
            - Reveal labels only after blind scoring
            - Record scores and tasting notes
            - Show the group ranking of each tasting
API:        REST
            POST /tastings
            POST /wines/{id}/notes
            POST /tastings/{id}/reveal
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 268

**Intent:**
platform where makers list services like 3d printing or laser cutting and people send jobs

**Spec:**
```
Type:       Web application (maker services marketplace)
Auth:       Email + password login
Data model: Maker(id, name, email, city, machines)
            Job(id, customer_id, maker_id -> Maker, file_url, material, quantity, quote, status)
            Message(id, job_id -> Job, sender_id, body)
Features:   - List machines and materials offered
            - Upload STL or SVG files with job details
            - Let makers send a quote
            - Pay when the quote is accepted
            - Track job status to delivery
API:        REST
            GET  /makers?city={c}&machine={m}
            POST /jobs
            POST /jobs/{id}/quote
            POST /jobs/{id}/accept
Storage:    PostgreSQL, S3 (design files)
Tech stack: Node.js, NestJS, Three.js (STL preview), Stripe API
```

---

## Example 269

**Intent:**
Hello. Our church have many Ghanaian families, we want web site for announcing funerals, weddings and naming ceremonies so all members know and can contribute money

**Spec:**
```
Type:       Web application (community announcements and contributions)
Auth:       Email or phone login, admin role
Data model: Member(id, name, phone, email)
            Announcement(id, kind, title, family_name, date, venue, details)
            Contribution(id, announcement_id -> Announcement, member_id -> Member, amount, method, paid_at)
Features:   - Post funerals, weddings and naming ceremonies
            - Send SMS to all members for new announcements
            - Pledge and pay contributions online or record cash
            - Show the family the list of contributions
API:        REST
            GET  /announcements
            POST /announcements
            POST /announcements/{id}/contributions
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Twilio API, Paystack API
```

---

## Example 270

**Intent:**
community darkroom booking

**Spec:**
```
Type:       Web application (darkroom booking)
Auth:       Email + password login
Data model: Member(id, name, email, inducted)
            Enlarger(id, name, format)
            Booking(id, enlarger_id -> Enlarger, member_id -> Member, starts_at, ends_at)
            ChemistryLog(id, mixed_on, prints_processed)
Features:   - Book an enlarger in 2-hour blocks
            - Allow only inducted members to book
            - Log prints processed to know when to replace chemistry
            - Show the week's bookings on a calendar
API:        REST
            GET  /bookings?week={w}
            POST /bookings
            POST /chemistry
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 271

**Intent:**
Build an API that returns public holidays per country and region, for other SaaS products to call.

**Spec:**
```
Type:       REST API service (public holidays)
Auth:       API key per client
Data model: Country(code, name)
            Region(code, country_code -> Country, name)
            Holiday(id, country_code -> Country, region_code -> Region, date, name, kind)
Features:   - Return holidays for a country and year
            - Filter by region and holiday kind
            - Check whether a date is a working day
            - Count working days between two dates
            - Rate-limit requests per key
API:        REST
            GET  /v1/holidays?country={c}&year={y}
            GET  /v1/is-workday?country={c}&date={d}
            GET  /v1/workdays?from={d1}&to={d2}
Storage:    PostgreSQL, Redis (rate limits)
Tech stack: Go, Gin
```

---

## Example 272

**Intent:**
discord bot that tracks our book club reading progress and nags people

**Spec:**
```
Type:       Bot (Discord)
Data model: Book(id, title, total_pages, due_date)
            Progress(member_id, book_id, page, updated_at)
Features:   - Set the current book with /book and a due date
            - Update your page with /page
            - Show everyone's progress bars with /progress
            - Ping members who are behind schedule each Friday
Storage:    SQLite
Tech stack: Python, discord.py
```

---

## Example 273

**Intent:**
website where my local makers market vendors upload products so customers can browse before the market day

**Spec:**
```
Type:       Web application (market vendor catalog)
Auth:       Email + password login for vendors
Data model: Vendor(id, name, email, stall_number, instagram)
            Product(id, vendor_id -> Vendor, name, price, photo_url, in_stock)
            MarketDay(id, date)
            Attendance(vendor_id -> Vendor, market_day_id -> MarketDay)
Features:   - Let vendors upload products with price and photo
            - Show which vendors attend the next market day
            - Browse products by category
            - Let customers reserve an item for pickup at the stall
API:        REST
            GET  /market-days/next/vendors
            POST /products
            POST /products/{id}/reserve
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Next.js
```

---

## Example 274

**Intent:**
email capture popups saas with exit intent

**Spec:**
```
Type:       Web application (email capture popups SaaS)
Auth:       Email + password login
Data model: Site(id, owner_id, domain)
            Popup(id, site_id -> Site, trigger, delay_s, html, active)
            Lead(id, popup_id -> Popup, email, page_url, created_at)
            Impression(popup_id -> Popup, date, count)
Features:   - Design popups with a template editor
            - Trigger on exit intent, scroll depth or delay
            - Collect emails and send them to Mailchimp
            - Show impressions and conversion rate per popup
API:        REST
            GET  /embed/{site}.js
            POST /leads
            GET  /popups/{id}/stats
Storage:    PostgreSQL
Tech stack: Node.js, Preact, React
```

---

## Example 275

**Intent:**
bat detector recordings sharing for bat group so experts can id species

**Spec:**
```
Type:       Web application (bat call identification)
Auth:       Email + password login, expert role
Data model: Recorder(id, name, email)
            Recording(id, recorder_id -> Recorder, file_url, lat, lng, recorded_at, auto_id)
            Identification(id, recording_id -> Recording, expert_id -> Recorder, species, confidence)
Features:   - Upload full-spectrum WAV files
            - Show a spectrogram of each call
            - Suggest species with an automatic classifier
            - Let experts confirm or correct the species
API:        REST
            POST /recordings
            GET  /recordings/{id}/spectrogram.png
            POST /recordings/{id}/identifications
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, Django, librosa
```

---

## Example 276

**Intent:**
reunion planning for a military unit veterans, find old comrades

**Spec:**
```
Type:       Web application (veterans reunion)
Auth:       Email + password login, admin verification of service
Data model: Veteran(id, name, email, unit, years_served, rank, city)
            Reunion(id, title, date, location, cost)
            Registration(id, reunion_id -> Reunion, veteran_id -> Veteran, guests, paid)
            Photo(id, uploader_id -> Veteran, image_url, caption, year)
Features:   - Search for comrades by unit and years served
            - Request contact through the site without exposing emails
            - Register for reunions with guests and pay
            - Share old photos with captions
API:        REST
            GET  /veterans?unit={u}
            POST /veterans/{id}/contact
            POST /reunions/{id}/registrations
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Stripe API
```

---

## Example 277

**Intent:**
competition entry platform for a short film festival, filmmakers submit links, jury scores

**Spec:**
```
Type:       Web application (film festival submissions)
Auth:       Email + password login, roles: filmmaker, juror, admin
Data model: Film(id, filmmaker_id, title, runtime_min, genre, screener_url, screener_password, fee_paid)
            Juror(id, name, email)
            JuryScore(id, film_id -> Film, juror_id -> Juror, score, comment)
Features:   - Submit a film with a private screener link and pay the entry fee
            - Assign films to jurors evenly
            - Score films and leave comments
            - Shortlist the top films per category
            - Email filmmakers the selection result
API:        REST
            POST /films
            POST /films/{id}/scores
            GET  /shortlist
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Stripe API, React
```

---

## Example 278

**Intent:**
a webhook service that posts GitHub releases of our open source project to Discord and Twitter-like sites

**Spec:**
```
Type:       Webhook service (release announcements)
Features:   - Receive GitHub release webhooks
            - Verify the webhook HMAC signature
            - Post release notes summary to a Discord channel
            - Post a short announcement to Mastodon and Bluesky
            - Skip pre-releases unless configured
API:        REST
            POST /webhooks/github
Tech stack: Node.js, Express, Discord webhooks, Mastodon API, Bluesky AT Protocol
```

---

## Example 279

**Intent:**
neighborhood kids sports equipment exchange, outgrown cleats skates etc

**Spec:**
```
Type:       Web application (kids sports gear exchange)
Auth:       Email + password login
Data model: Parent(id, name, email, area)
            GearItem(id, parent_id -> Parent, sport, kind, size, condition, photo_url, price, status)
Features:   - List outgrown gear with sport, size and condition
            - Give away or sell at a small price
            - Filter by sport and size
            - Get notified when gear in your child's size is listed
API:        REST
            GET  /gear?sport={s}&size={z}
            POST /gear
            POST /alerts
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 280

**Intent:**
I'd love a simple community notice board for our tiny island, internet is slow so pages must be super light

**Spec:**
```
Type:       Web application (lightweight notice board)
Auth:       Email login with one-time code
Data model: Resident(id, name, email)
            Notice(id, resident_id -> Resident, category, title, body, expires_on)
Features:   - Post notices in categories (ferry, for sale, events, help)
            - Serve server-rendered pages without JavaScript
            - Compress and resize images to under 50 KB
            - Expire notices automatically
            - Offer a plain-text email digest
API:        REST
            GET  /notices?category={c}
            POST /notices
Storage:    SQLite
Tech stack: Go, html/template
```

---

## Example 281

**Intent:**
SaaS for managing a waitlist + check-in queue at walk-in clinics or barbers

**Spec:**
```
Type:       Web application (virtual queue SaaS)
Auth:       Email + password login for businesses
Data model: Location(id, business_id, name, avg_service_min)
            QueueEntry(id, location_id -> Location, name, phone, party, joined_at, called_at, status)
Features:   - Let customers join the queue online or on a lobby tablet
            - Estimate wait time from the average service time
            - Text customers when it is almost their turn
            - Let staff call, skip or remove entries
            - Show a public live wait time
API:        REST
            POST /locations/{id}/queue
            GET  /locations/{id}/wait
            PATCH /queue/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Twilio API, Vue.js
```

---

## Example 282

**Intent:**
site where people upload old local photos and others guess the year and place

**Spec:**
```
Type:       Web application (historic photo guessing)
Auth:       Email + password login
Data model: Photo(id, uploader_id, image_url, actual_year, actual_lat, actual_lng, story)
            Guess(id, photo_id -> Photo, user_id, year, lat, lng, score)
Features:   - Upload historical photos with known year and place
            - Guess the year with a slider and the place on a map
            - Score guesses by year difference and distance
            - Reveal the answer and story after guessing
            - Show a weekly leaderboard
API:        REST
            GET  /photos/random
            POST /photos/{id}/guesses
            POST /photos
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, FastAPI, Leaflet, Svelte
```

---

## Example 283

**Intent:**
moderated marketplace for handmade dice and tabletop accessories? no just a showcase gallery with artist links

**Spec:**
```
Type:       Web application (artist showcase gallery)
Auth:       Email + password login for artists, admin moderation
Data model: Artist(id, name, email, shop_url, approved)
            Work(id, artist_id -> Artist, title, category, image_urls, created_at)
Features:   - Let artists apply and be approved by admins
            - Upload works with several photos
            - Browse by category with infinite scroll
            - Link each work to the artist's own shop
API:        REST
            GET  /works?category={c}
            POST /works
            PATCH /artists/{id}/approve
Storage:    PostgreSQL, S3 (images)
Tech stack: Node.js, Astro
```

---

## Example 284

**Intent:**
API rate limit and key management gateway saas for people selling APIs

**Spec:**
```
Type:       Web application (API gateway SaaS)
Auth:       Email + password login for API owners
Data model: Api(id, owner_id, name, upstream_url)
            Plan(id, api_id -> Api, name, requests_per_month, rate_per_second, price)
            ApiKey(id, plan_id -> Plan, customer_email, key_hash, active)
            UsageCounter(key_id -> ApiKey, month, count)
Features:   - Proxy requests to the upstream API
            - Check API keys and enforce per-plan rate limits
            - Count usage per month and block over quota
            - Let customers sign up for a plan and get a key
            - Bill overage through Stripe metered billing
API:        REST
            ANY  /gw/{api}/{path}
            POST /apis
            POST /apis/{id}/plans
            POST /keys
Storage:    PostgreSQL, Redis (counters)
Tech stack: Go, Redis, Stripe API, React
```

---

## Example 285

**Intent:**
oral history archive for our town, interviews with elders with transcripts and searchable

**Spec:**
```
Type:       Web application (oral history archive)
Auth:       Email + password login for archivists
Data model: Narrator(id, name, born_year, bio, consent_level)
            Interview(id, narrator_id -> Narrator, recorded_on, interviewer, audio_url, transcript)
            Clip(id, interview_id -> Interview, start_s, end_s, title, tags)
Features:   - Upload interview audio and generate a draft transcript
            - Edit transcripts with timestamps synced to audio
            - Search full text and jump to the moment in the audio
            - Create themed clips with tags
            - Respect narrator consent levels for public access
API:        REST
            GET  /search?q={text}
            POST /interviews
            POST /interviews/{id}/clips
Storage:    PostgreSQL (full-text search), S3 (audio)
Tech stack: Python, Django, Whisper, wavesurfer.js
```

---

## Example 286

**Intent:**
web platform for local chess tournaments: swiss pairings, results, standings

**Spec:**
```
Type:       Web application (Swiss tournament manager)
Auth:       Email + password login for arbiters
Data model: Tournament(id, name, rounds, time_control)
            Entrant(id, tournament_id -> Tournament, name, rating, score)
            Pairing(id, tournament_id -> Tournament, round, white_id -> Entrant, black_id -> Entrant, board, result)
Features:   - Register entrants with ratings
            - Generate Swiss-system pairings each round avoiding rematches
            - Balance white and black colours
            - Enter results and update standings with tie-breaks
            - Publish pairings and standings online
API:        REST
            POST /tournaments/{id}/entrants
            POST /tournaments/{id}/rounds
            PATCH /pairings/{id}
            GET  /tournaments/{id}/standings
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Thymeleaf
```

---

## Example 287

**Intent:**
Something like a public diary where users post one sentence a day and see others'

**Spec:**
```
Type:       Web application (one-line daily journal)
Auth:       Email + password login
Data model: User(id, username, email, public)
            Line(id, user_id -> User, date, text)
Features:   - Post one sentence per day, max 200 characters
            - Show a feed of today's public lines
            - Show your own year as a calendar of lines
            - Show "on this day" lines from past years
API:        REST
            POST /lines
            GET  /today
            GET  /users/{name}/year/{y}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 288

**Intent:**
I want to manage our choir tour: singers' passports, room assignments, flights, payments

**Spec:**
```
Type:       Web application (group tour management)
Auth:       Email + password login, organiser role
Data model: Singer(id, name, email, passport_number_encrypted, passport_expiry, dietary)
            Room(id, hotel, room_number, beds)
            RoomAssignment(room_id -> Room, singer_id -> Singer)
            Flight(id, number, departs_at, from_airport, to_airport)
            Payment(id, singer_id -> Singer, amount, paid_on)
Features:   - Collect passport details encrypted at rest
            - Warn about passports expiring within six months of the tour
            - Assign singers to hotel rooms
            - Track instalment payments per singer
            - Export a rooming list and flight manifest
API:        REST
            POST /singers
            POST /rooms/{id}/assign
            POST /payments
            GET  /exports/rooming-list.csv
Storage:    PostgreSQL
Tech stack: Python, Django, django-cryptography
```

---

## Example 289

**Intent:**
real time collaborative sticky note wall for workshops

**Spec:**
```
Type:       Web application (collaborative sticky notes)
Data model: Wall(id, title, share_code)
            Note(id, wall_id -> Wall, text, color, x, y, author_name)
            Group(id, wall_id -> Wall, title, x, y, w, h)
Features:   - Create a wall and share a join code
            - Add, move and colour notes in real time
            - Group notes into labelled areas
            - Vote on notes with dots
            - Export the wall as an image or CSV
API:        WebSocket
            WS   /walls/{code}
Storage:    PostgreSQL
Tech stack: TypeScript, Yjs, React, Node.js
```

---

## Example 290

**Intent:**
astro club light curve citizen science, members measure variable star brightness and upload

**Spec:**
```
Type:       Web application (variable star observations)
Auth:       Email + password login with observer code
Data model: Observer(id, code, name, email)
            Star(id, name, ra, dec, kind)
            Observation(id, star_id -> Star, observer_id -> Observer, jd, magnitude, band, method)
Features:   - Submit magnitude estimates with Julian date and band
            - Validate magnitudes against the star's known range
            - Plot a light curve combining all observers
            - Export observations in AAVSO extended format
API:        REST
            POST /observations
            GET  /stars/{id}/lightcurve
            GET  /stars/{id}/export
Storage:    PostgreSQL
Tech stack: Python, Flask, Plotly
```

---

## Example 291

**Intent:**
SaaS: help podcasters find and book guests — guests have profiles, hosts send invites

**Spec:**
```
Type:       Web application (podcast guest booking)
Auth:       Email + password login, host and guest roles
Data model: Guest(id, name, email, expertise, bio, past_appearances, media_kit_url)
            Host(id, name, email, podcast_name)
            Invite(id, host_id -> Host, guest_id -> Guest, topic, status)
            Recording(id, invite_id -> Invite, scheduled_at, link)
Features:   - Create guest profiles with topics and past appearances
            - Search guests by topic
            - Send invites with a proposed topic
            - Pick a recording time from shared availability
            - Send guests the episode link when published
API:        REST
            GET  /guests?topic={t}
            POST /invites
            POST /invites/{id}/schedule
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma, Cal.com API
```

---

## Example 292

**Intent:**
simple tool for my running club to do a monthly distance challenge from strava

**Spec:**
```
Type:       Web application (Strava distance challenge)
Auth:       Strava OAuth login
Data model: Athlete(id, strava_id, name, access_token, refresh_token)
            Challenge(id, month, goal_km)
            Activity(id, athlete_id -> Athlete, strava_activity_id, distance_m, date)
Features:   - Connect your Strava account
            - Import runs automatically through Strava webhooks
            - Show a monthly leaderboard of kilometres
            - Show progress toward the club goal
API:        REST
            GET  /auth/strava/callback
            POST /webhooks/strava
            GET  /leaderboard?month={m}
Storage:    PostgreSQL
Tech stack: Python, Flask, Strava API
```

---

## Example 293

**Intent:**
a place where volunteers record trail maintenance work: hours, fallen trees removed, drains cleared

**Spec:**
```
Type:       Web application (trail maintenance log)
Auth:       Email + password login, crew leader role
Data model: Volunteer(id, name, email)
            Trail(id, name, length_km)
            WorkDay(id, trail_id -> Trail, date, leader_id -> Volunteer)
            WorkEntry(id, work_day_id -> WorkDay, volunteer_id -> Volunteer, hours)
            Task(id, work_day_id -> WorkDay, kind, quantity, lat, lng)
Features:   - Log a work day with crew and hours
            - Record tasks like trees removed and drains cleared
            - Pin hazards on a map for the next crew
            - Report yearly totals for grant applications
API:        REST
            POST /work-days
            POST /work-days/{id}/tasks
            GET  /reports/yearly
Storage:    PostgreSQL
Tech stack: Python, Django, Leaflet
```

---

## Example 294

**Intent:**
saas to let shops book delivery slots for customers, like time windows with capacity

**Spec:**
```
Type:       Web application (delivery slot booking SaaS)
Auth:       Email + password login for shops, API key
Data model: Shop(id, name)
            Zone(id, shop_id -> Shop, name, postcodes)
            Window(id, zone_id -> Zone, date, start_time, end_time, capacity, booked)
            SlotBooking(id, window_id -> Window, order_ref, customer_address)
Features:   - Define delivery zones by postcode
            - Create time windows with capacity per zone
            - Show available windows at checkout via a widget
            - Reserve a slot for 15 minutes while paying
            - Show drivers a daily list per zone
API:        REST
            GET  /v1/windows?postcode={p}
            POST /v1/bookings
            GET  /v1/routes?date={d}
Storage:    PostgreSQL, Redis (temporary holds)
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 295

**Intent:**
kids coding club: kids post their scratch projects and get stickers from mentors

**Spec:**
```
Type:       Web application (kids coding showcase)
Auth:       Mentor accounts with email + password, kid accounts with username and picture password
Data model: Kid(id, username, club_id)
            Mentor(id, name, email, club_id)
            Project(id, kid_id -> Kid, title, scratch_url, description)
            Sticker(id, project_id -> Project, mentor_id -> Mentor, kind)
Features:   - Let kids share a Scratch project link with a description
            - Embed the Scratch player on the project page
            - Let mentors award stickers like "great idea" or "clever code"
            - Show only first names and no personal data
API:        REST
            POST /projects
            POST /projects/{id}/stickers
            GET  /clubs/{id}/projects
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 296

**Intent:**
expense splitting for a big group trip with multiple currencies

**Spec:**
```
Type:       Web application (group expense splitting)
Data model: Trip(id, name, base_currency, share_token)
            Person(id, trip_id -> Trip, name)
            Expense(id, trip_id -> Trip, payer_id -> Person, amount, currency, description, date)
            Share(expense_id -> Expense, person_id -> Person, weight)
Features:   - Add expenses in any currency with who paid
            - Split equally or by custom weights
            - Convert to the base currency with daily exchange rates
            - Calculate the fewest transfers to settle up
API:        REST
            POST /trips
            POST /trips/{id}/expenses
            GET  /trips/{id}/settlement
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, exchangerate API
```

---

## Example 297

**Intent:**
manage reading volunteers in primary schools, who reads with which kid when

**Spec:**
```
Type:       Web application (school reading volunteers)
Auth:       Email + password login, school coordinator role
Data model: School(id, name)
            Volunteer(id, name, email, dbs_checked)
            Pupil(id, school_id -> School, initials, year_group)
            ReadingSession(id, volunteer_id -> Volunteer, pupil_id -> Pupil, date, book, notes)
Features:   - Schedule weekly sessions between volunteers and pupils
            - Store only pupil initials for privacy
            - Record the book and notes after each session
            - Show teachers progress notes per pupil
API:        REST
            POST /sessions
            GET  /pupils/{id}/sessions
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 298

**Intent:**
cli to post to our community's status page from the terminal during incidents

**Spec:**
```
Type:       Command-line tool (status page client)
Features:   - Open an incident with a title and impact level
            - Post updates to the latest open incident
            - Resolve an incident
            - Set a component's status (operational, degraded, outage)
            - Read the API token from a config file
Input:      Subcommands and flags, e.g. incident open --title "..." --impact major
Tech stack: Go, Cobra, status page REST API
```

---

## Example 299

**Intent:**
I play in a community orchestra, we need to manage the sheet music library: which parts are out with which player

**Spec:**
```
Type:       Web application (orchestra music library)
Auth:       Email + password login, librarian role
Data model: Musician(id, name, email, instrument)
            Work(id, title, composer, publisher, shelf)
            Part(id, work_id -> Work, instrument, copy_number)
            PartLoan(id, part_id -> Part, musician_id -> Musician, out_on, returned_on)
Features:   - Catalog works and their individual parts
            - Hand out parts for a concert season to players
            - Show missing parts not yet returned
            - Upload marked bowings as scans
API:        REST
            GET  /works
            POST /part-loans
            PATCH /part-loans/{id}
            GET  /part-loans?outstanding=true
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 300

**Intent:**
saas giving restaurants a QR code menu they can edit themselves with allergens

**Spec:**
```
Type:       Web application (QR menu SaaS)
Auth:       Email + password login
Data model: Restaurant(id, name, slug, languages)
            Section(id, restaurant_id -> Restaurant, name, position)
            Dish(id, section_id -> Section, name, description, price, allergens, available)
Features:   - Edit the menu with sections and dishes
            - Mark allergens with standard icons
            - Generate a printable QR code
            - Hide dishes that are sold out instantly
            - Translate the menu into several languages
API:        REST
            GET  /m/{slug}
            POST /sections
            POST /dishes
            PATCH /dishes/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, qrcode
```

---

## Example 301

**Intent:**
karaoke queue for our bar

**Spec:**
```
Type:       Web application (karaoke queue)
Auth:       PIN login for the KJ
Data model: Night(id, date, venue_code)
            Singer(id, night_id -> Night, name)
            Request(id, singer_id -> Singer, song, artist, position, status)
Features:   - Let guests scan a QR code and add a song with their name
            - Rotate the queue fairly so each singer gets a turn
            - Let the KJ reorder, skip and mark songs done
            - Show the next three singers on a TV screen
API:        REST + WebSocket
            POST /nights/{code}/requests
            PATCH /requests/{id}
            WS   /nights/{code}/queue
Storage:    SQLite
Tech stack: Node.js, Express, Socket.IO
```

---

## Example 302

**Intent:**
DJ song request page for weddings where guests vote songs up

**Spec:**
```
Type:       Web application (event song requests)
Auth:       Email + password login for DJs
Data model: Event(id, dj_id, name, date, code, do_not_play)
            SongRequest(id, event_id -> Event, title, artist, guest_name, votes, played)
Features:   - Search songs through the Spotify API
            - Let guests request and upvote songs
            - Block songs on the couple's do-not-play list
            - Show the DJ requests sorted by votes
API:        REST
            GET  /e/{code}
            POST /e/{code}/requests
            POST /requests/{id}/vote
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Spotify Web API, Svelte
```

---

## Example 303

**Intent:**
piano teacher wants students to log practice minutes and see weekly streaks, parents see too

**Spec:**
```
Type:       Web application (music practice log)
Auth:       Email + password login for teacher and parents, student PIN
Data model: Teacher(id, name, email)
            Student(id, teacher_id -> Teacher, name, parent_email, pin)
            Assignment(id, student_id -> Student, piece, focus, week_of)
            PracticeLog(id, student_id -> Student, date, minutes, note)
Features:   - Set weekly assignments per student
            - Log practice minutes with a built-in timer
            - Show weekly totals and streaks
            - Let parents view progress
            - Let the teacher comment on practice notes
API:        REST
            POST /students/{id}/logs
            POST /students/{id}/assignments
            GET  /students/{id}/summary
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 304

**Intent:**
small record label demo submission portal

**Spec:**
```
Type:       Web application (demo submissions)
Auth:       Email + password login for label staff
Data model: Submission(id, artist_name, email, genre, track_url, bio, status, submitted_at)
            Rating(id, submission_id -> Submission, staff_id, score, note)
Features:   - Accept demos as SoundCloud links or MP3 uploads
            - Limit each artist to one submission per month
            - Let staff listen, rate and comment
            - Send polite decline or follow-up emails from templates
API:        REST
            POST /submissions
            GET  /submissions?status=new
            POST /submissions/{id}/ratings
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, Django
```

---

## Example 305

**Intent:**
musicians share stems online and others add tracks to make collab songs

**Spec:**
```
Type:       Web application (online music collaboration)
Auth:       Email + password login
Data model: Musician(id, username, email, instruments)
            Song(id, owner_id -> Musician, title, bpm, key)
            Stem(id, song_id -> Song, musician_id -> Musician, instrument, audio_url, offset_ms)
Features:   - Start a song with a first stem and its BPM and key
            - Upload new stems that line up with the song
            - Play stems together with mute and solo controls
            - Download all stems as a zip
            - Credit every contributor
API:        REST
            POST /songs
            POST /songs/{id}/stems
            GET  /songs/{id}/stems.zip
Storage:    PostgreSQL, S3 (audio)
Tech stack: TypeScript, React, Web Audio API, Node.js
```

---

## Example 306

**Intent:**
beat battle contests for producers, sample pack given, submit beat, community votes

**Spec:**
```
Type:       Web application (beat battles)
Auth:       Email + password login
Data model: Producer(id, username, email)
            Battle(id, title, sample_pack_url, submit_until, vote_until)
            Beat(id, battle_id -> Battle, producer_id -> Producer, audio_url)
            BattleVote(beat_id -> Beat, voter_id -> Producer)
Features:   - Publish a battle with a downloadable sample pack
            - Submit one beat per producer before the deadline
            - Play entries anonymously in random order during voting
            - Allow three votes per user, not for your own beat
            - Reveal producers and winners at the end
API:        REST
            POST /battles
            POST /battles/{id}/beats
            POST /beats/{id}/vote
            GET  /battles/{id}/results
Storage:    PostgreSQL, S3 (audio)
Tech stack: Node.js, Express, React
```

---

## Example 307

**Intent:**
anime watch party scheduler for our club

**Spec:**
```
Type:       Web application (watch party scheduler)
Auth:       Discord OAuth login
Data model: Member(id, discord_id, name)
            Series(id, title, episodes, anilist_id)
            WatchParty(id, series_id -> Series, episode_from, episode_to, starts_at)
            Attendance(party_id -> WatchParty, member_id -> Member)
Features:   - Suggest series and vote on the next one
            - Fetch series info from AniList
            - Schedule watch parties with episode ranges
            - RSVP and get a Discord reminder
API:        REST
            GET  /parties
            POST /parties
            POST /parties/{id}/rsvp
Storage:    PostgreSQL
Tech stack: Python, FastAPI, AniList GraphQL API, React
```

---

## Example 308

**Intent:**
gaming convention: volunteer scheduling and panel room schedule

**Spec:**
```
Type:       Web application (convention operations)
Auth:       Email + password login, roles: volunteer, staff
Data model: Room(id, name, capacity)
            Panel(id, room_id -> Room, title, host, starts_at, ends_at)
            Volunteer(id, name, email, max_hours)
            VolunteerShift(id, role, room_id -> Room, starts_at, ends_at, volunteer_id -> Volunteer)
Features:   - Build the panel schedule with no room overlaps
            - Let volunteers pick shifts up to their hour limit
            - Show attendees the public schedule by day and room
            - Give volunteers a badge for reaching 12 hours
API:        REST
            GET  /schedule
            POST /panels
            POST /shifts/{id}/claim
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 309

**Intent:**
LARP event registration with character applications

**Spec:**
```
Type:       Web application (LARP event registration)
Auth:       Email + password login
Data model: Player(id, name, email, emergency_contact)
            Event(id, title, dates, location, ticket_price, capacity)
            CharacterApplication(id, event_id -> Event, player_id -> Player, concept, faction, status)
            Ticket(id, event_id -> Event, player_id -> Player, paid)
Features:   - Publish events with factions and capacity
            - Submit a character concept for approval
            - Pay for a ticket after approval
            - Collect emergency contact and medical notes
            - Export faction lists for game masters
API:        REST
            POST /events/{id}/applications
            PATCH /applications/{id}
            POST /events/{id}/tickets
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe API
```

---

## Example 310

**Intent:**
flash fiction contest under 300 words, judges, winners anthology

**Spec:**
```
Type:       Web application (flash fiction contest)
Auth:       Email + password login, judge role
Data model: Writer(id, pen_name, email)
            Contest(id, prompt, word_limit, closes_at)
            Story(id, contest_id -> Contest, writer_id -> Writer, title, text, word_count)
            JudgeScore(story_id -> Story, judge_id, score)
Features:   - Submit a story and reject entries over the word limit
            - Hide author names from judges
            - Collect judge scores and rank stories
            - Generate an EPUB anthology of the top entries
API:        REST
            POST /contests/{id}/stories
            POST /stories/{id}/scores
            GET  /contests/{id}/anthology.epub
Storage:    PostgreSQL
Tech stack: Python, Django, ebooklib
```

---

## Example 311

**Intent:**
daily writing prompt site where people respond and read others

**Spec:**
```
Type:       Web application (daily writing prompts)
Auth:       Email + password login
Data model: Prompt(id, text, date)
            Response(id, prompt_id -> Prompt, author_id, text, created_at)
            Heart(response_id -> Response, user_id)
Features:   - Show one prompt per day
            - Write a response and publish it
            - Read and heart others' responses
            - Keep a writing streak count
API:        REST
            GET  /prompts/today
            POST /prompts/{id}/responses
            POST /responses/{id}/heart
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix
```

---

## Example 312

**Intent:**
poetry slam scoring with 5 judges drop high and low

**Spec:**
```
Type:       Web application (poetry slam scoring)
Auth:       PIN login for the host
Data model: Slam(id, date, venue)
            Poet(id, slam_id -> Slam, name, draw_order)
            Score(id, poet_id -> Poet, round, judge_number, value, time_penalty)
Features:   - Draw the reading order randomly
            - Enter five judge scores per poem
            - Drop the highest and lowest and sum the rest
            - Apply time penalties
            - Show the leaderboard on a projector
API:        REST
            POST /slams/{id}/draw
            POST /poets/{id}/scores
            GET  /slams/{id}/leaderboard
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 313

**Intent:**
letterboxing hobby site: people hide boxes with stamps and post clues, finders log finds

**Spec:**
```
Type:       Web application (letterboxing clues)
Auth:       Email + password login with trail name
Data model: Boxer(id, trail_name, email, stamp_image_url)
            Box(id, planter_id -> Boxer, name, region, clue_text, difficulty, status)
            FindLog(id, box_id -> Box, finder_id -> Boxer, found_on, note)
Features:   - Post a box with text clues and region, no exact coordinates
            - Log finds with a note
            - Report a box as missing
            - Show your personal stamp and find count on your profile
API:        REST
            GET  /boxes?region={r}
            POST /boxes
            POST /boxes/{id}/finds
Storage:    PostgreSQL
Tech stack: Node.js, Express, EJS
```

---

## Example 314

**Intent:**
FAN SITE FOR MY FAVORITE BAND WITH TOUR DIARY, setlists, fans post photos from concerts

**Spec:**
```
Type:       Web application (fan site with setlists)
Auth:       Email + password login
Data model: Fan(id, username, email)
            Show(id, date, venue, city)
            SetlistSong(id, show_id -> Show, position, song)
            ShowPhoto(id, show_id -> Show, fan_id -> Fan, image_url)
            Attended(fan_id -> Fan, show_id -> Show)
Features:   - List past and upcoming shows
            - Edit setlists collaboratively with history
            - Upload photos from a show
            - Mark shows you attended and see song stats you have heard live
API:        REST
            GET  /shows
            PUT  /shows/{id}/setlist
            POST /shows/{id}/photos
            POST /shows/{id}/attended
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django
```

---

## Example 315

**Intent:**
band rehearsal room booking for music school

**Spec:**
```
Type:       Web application (rehearsal room booking)
Auth:       Student email login
Data model: Student(id, name, email)
            RehearsalRoom(id, name, has_drums, has_piano)
            Booking(id, room_id -> RehearsalRoom, student_id -> Student, starts_at, ends_at)
Features:   - Book rooms in one-hour blocks
            - Filter rooms with drums or piano
            - Limit each student to 6 hours per week
            - Release bookings not checked in after 15 minutes
API:        REST
            GET  /rooms?date={d}
            POST /bookings
            POST /bookings/{id}/checkin
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, React
```

---

## Example 316

**Intent:**
I teach guitar and want to sell my own tab books and lesson videos as a membership

**Spec:**
```
Type:       Web application (music lesson membership)
Auth:       Email + password login
Data model: Member(id, email, stripe_customer_id, active_until)
            Lesson(id, title, level, video_url, tab_pdf_url, published_at)
            Progress(member_id -> Member, lesson_id -> Lesson, completed)
Features:   - Charge a monthly membership
            - Stream lesson videos only to active members
            - Download tab PDFs per lesson
            - Track completed lessons by level
API:        REST
            GET  /lessons
            POST /checkout
            POST /webhooks/stripe
            POST /lessons/{id}/complete
Storage:    PostgreSQL, S3 (videos and PDFs)
Tech stack: Node.js, Next.js, Stripe API, Mux
```

---

## Example 317

**Intent:**
film club screening schedule and member votes on next film, also discussion after

**Spec:**
```
Type:       Web application (film club)
Auth:       Email + password login
Data model: Member(id, name, email)
            Screening(id, film_title, tmdb_id, date, venue)
            Nomination(id, member_id -> Member, film_title, tmdb_id, votes)
            Review(id, screening_id -> Screening, member_id -> Member, rating, text)
Features:   - Nominate films and vote for the next screening
            - Show film details and poster from TMDB
            - Post ratings and short reviews after a screening
            - Show the club's all-time favourite list
API:        REST
            POST /nominations
            POST /nominations/{id}/vote
            POST /screenings/{id}/reviews
Storage:    PostgreSQL
Tech stack: PHP, Laravel, TMDB API
```

---

## Example 318

**Intent:**
pls i need site for our mosque: prayer times, events, donations, and youth classes registration

**Spec:**
```
Type:       Web application (mosque community site)
Auth:       Email + password login for admins and parents
Data model: PrayerTime(date, fajr, dhuhr, asr, maghrib, isha, jumuah)
            Event(id, title, date, description)
            Donation(id, donor_email, amount, fund, recurring)
            ClassEnrollment(id, child_name, age, class_name, parent_email)
Features:   - Show daily prayer times calculated for the location
            - Post events and announcements
            - Accept one-time and monthly donations to chosen funds
            - Register children for weekend classes
API:        REST
            GET  /prayer-times?date={d}
            GET  /events
            POST /donations
            POST /enrollments
Storage:    PostgreSQL
Tech stack: Python, Django, adhan library, Stripe API
```

---

## Example 319

**Intent:**
synagogue torah reading assignment schedule for bar/bat mitzvah students and readers

**Spec:**
```
Type:       Web application (reading assignments)
Auth:       Email + password login, gabbai role
Data model: Reader(id, name, email)
            Service(id, date, parasha)
            Aliyah(id, service_id -> Service, number, verses, reader_id -> Reader)
Features:   - List upcoming services with the weekly portion
            - Assign readers to each aliyah
            - Let readers volunteer for open aliyot
            - Email readers a reminder two weeks ahead
API:        REST
            GET  /services
            POST /aliyot/{id}/assign
            POST /aliyot/{id}/volunteer
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hebcal API
```

---

## Example 320

**Intent:**
platform for local history society to publish walking tours with audio at each stop

**Spec:**
```
Type:       Web application (audio walking tours)
Auth:       Email + password login for editors
Data model: Tour(id, title, description, distance_km, cover_url)
            Stop(id, tour_id -> Tour, position, title, lat, lng, text, audio_url, photo_url)
Features:   - Create tours with ordered stops on a map
            - Attach audio narration and photos to each stop
            - Show the walker's position and the next stop
            - Play audio automatically when near a stop
            - Work offline after the tour is loaded (PWA)
API:        REST
            GET  /tours
            GET  /tours/{id}
            POST /tours/{id}/stops
Storage:    PostgreSQL, S3 (audio)
Tech stack: TypeScript, Vue.js (PWA), Leaflet, Node.js
```

---

## Example 321

**Intent:**
survey saas but for academic research: consent forms, randomized conditions, export to SPSS

**Spec:**
```
Type:       Web application (research survey platform)
Auth:       Email + password login for researchers, anonymous participants
Data model: Study(id, researcher_id, title, consent_text, status)
            Condition(id, study_id -> Study, name, weight)
            Item(id, study_id -> Study, condition_id -> Condition, position, kind, text, options)
            Participant(id, study_id -> Study, condition_id -> Condition, consented_at, completed_at)
            ItemResponse(participant_id -> Participant, item_id -> Item, value)
Features:   - Show a consent page before any questions
            - Randomly assign participants to conditions by weight
            - Record response times per item
            - Accept panel completion codes for Prolific
            - Export data as CSV and SPSS .sav
API:        REST
            POST /studies
            GET  /s/{id}/start
            POST /s/{id}/responses
            GET  /studies/{id}/export.sav
Storage:    PostgreSQL
Tech stack: Python, Django, pyreadstat
```

---

## Example 322

**Intent:**
neighborhood seed library at the public library, checkout seeds and return seeds from harvest

**Spec:**
```
Type:       Web application (seed library)
Auth:       Library card number login
Data model: Patron(id, card_number, name)
            SeedVariety(id, crop, variety, difficulty, packets_available)
            SeedCheckout(id, patron_id -> Patron, variety_id -> SeedVariety, packets, checked_out_on)
            SeedReturn(id, patron_id -> Patron, variety_id -> SeedVariety, packets, harvest_year)
Features:   - Browse seed varieties with growing difficulty
            - Check out up to 5 packets per season
            - Log seeds returned from your harvest
            - Show which varieties need more saved seed
API:        REST
            GET  /varieties
            POST /checkouts
            POST /returns
Storage:    PostgreSQL
Tech stack: Python, Flask
```

---

## Example 323

**Intent:**
Feature flags but self hosted, Rust backend, tiny

**Spec:**
```
Type:       REST API service (self-hosted feature flags)
Auth:       Admin token for writes, read token for SDKs
Data model: Flag(key, enabled, rollout_percent, allowlist, updated_at)
Features:   - Create, update and delete flags
            - Evaluate a flag for a user ID with stable percentage hashing
            - Return all flags for a user in one call
            - Store everything in a single file database
            - Ship as one static binary
API:        REST
            GET  /flags
            PUT  /flags/{key}
            GET  /evaluate?user={id}
Storage:    SQLite
Tech stack: Rust, Axum, SQLx
```

---

## Example 324

**Intent:**
mentoring circles: groups of 5 women in tech meet monthly with one senior mentor

**Spec:**
```
Type:       Web application (mentoring circles)
Auth:       Email + password login
Data model: Participant(id, name, email, role, seniority, topics)
            Circle(id, mentor_id -> Participant, topic, meets_on_weekday)
            CircleMember(circle_id -> Circle, participant_id -> Participant)
            Meeting(id, circle_id -> Circle, date, agenda, notes)
Features:   - Collect applications with topics and seniority
            - Form circles of five around a mentor by shared topic
            - Schedule monthly meetings with agenda templates
            - Share meeting notes within the circle
API:        REST
            POST /applications
            POST /circles/generate
            POST /circles/{id}/meetings
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Angular
```

---

## Example 325

**Intent:**
something for my cycling club where people report road hazards on routes we use

**Spec:**
```
Type:       Web application (cycling hazard map)
Auth:       Email + password login
Data model: Rider(id, name, email)
            Hazard(id, rider_id -> Rider, kind, description, lat, lng, photo_url, reported_at, cleared)
            Confirmation(hazard_id -> Hazard, rider_id -> Rider, still_there)
Features:   - Drop a hazard pin with type (pothole, glass, gravel, roadworks)
            - Confirm or clear hazards reported by others
            - Show hazards along a club route GPX
            - Auto-expire hazards not confirmed in 14 days
API:        REST
            GET  /hazards
            POST /hazards
            POST /hazards/{id}/confirm
Storage:    PostgreSQL with PostGIS
Tech stack: Node.js, Express, Leaflet
```

---

## Example 326

**Intent:**
Microsite generator for local nonprofits: pick template, fill details, get a site with donate button

**Spec:**
```
Type:       Web application (nonprofit site builder)
Auth:       Email + password login
Data model: Org(id, name, subdomain, template, logo_url, mission, donate_link)
            Section(id, org_id -> Org, kind, title, body, position)
Features:   - Pick a template and fill in mission, logo and colours
            - Add sections like programs, team and contact
            - Publish to a subdomain with HTTPS
            - Add a donate button linked to a payment page
API:        REST
            POST /orgs
            PUT  /orgs/{id}/sections
            POST /orgs/{id}/publish
Storage:    PostgreSQL, S3 (static output)
Tech stack: Node.js, Eleventy, React
```

---

## Example 327

**Intent:**
app where neighbours share surplus garden produce, like i have too many zucchini

**Spec:**
```
Type:       Mobile application with backend (produce sharing)
Auth:       Email or Apple/Google sign-in
Data model: Grower(id, name, lat, lng)
            Offer(id, grower_id -> Grower, produce, quantity, photo_url, pickup_note, expires_at)
            Claim(id, offer_id -> Offer, claimer_id -> Grower, status)
Features:   - Post surplus produce with a photo and pickup note
            - Show offers within 2 km
            - Claim an offer and message the grower
            - Expire offers after 3 days
API:        REST
            GET  /offers?near={lat,lng}
            POST /offers
            POST /offers/{id}/claims
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Supabase
```

---

## Example 328

**Intent:**
status page but for an internal platform team, automatically updated from prometheus alerts

**Spec:**
```
Type:       Webhook service (alert-driven status page)
Data model: Service(id, name, status)
            Incident(id, service_id -> Service, alert_name, started_at, resolved_at)
Features:   - Receive Alertmanager webhooks
            - Map alert labels to internal services
            - Set a service to degraded or down while alerts fire
            - Resolve the incident when alerts clear
            - Render a simple internal status page
API:        REST
            POST /webhooks/alertmanager
            GET  /status
Storage:    PostgreSQL
Tech stack: Go, Prometheus Alertmanager
```

---

## Example 329

**Intent:**
mahjong club

**Spec:**
```
Type:       Web application (mahjong club)
Auth:       Email + password login
Data model: Player(id, name, email)
            Session(id, date, table_count)
            TableGame(id, session_id -> Session, east_id -> Player, south_id -> Player, west_id -> Player, north_id -> Player)
            GameScore(game_id -> TableGame, player_id -> Player, points)
Features:   - Sign up for a club session
            - Seat players at tables of four randomly
            - Enter final points per table
            - Show a season ranking by total and average points
API:        REST
            POST /sessions/{id}/signup
            POST /sessions/{id}/seat
            POST /games/{id}/scores
            GET  /ranking
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 330

**Intent:**
community newspaper wants readers to submit letters and local news tips, editors review

**Spec:**
```
Type:       Web application (reader submissions)
Auth:       Email + password login for editors
Data model: Submission(id, kind, name, email, town, title, body, attachment_url, status)
            EditorNote(id, submission_id -> Submission, editor_id, note)
Features:   - Submit a letter to the editor or a news tip with attachments
            - Enforce a 300-word limit on letters
            - Let editors accept, reject or ask for changes
            - Keep internal notes per submission
API:        REST
            POST /submissions
            GET  /submissions?status=new
            PATCH /submissions/{id}
Storage:    PostgreSQL, S3 (attachments)
Tech stack: PHP, Laravel
```

---

## Example 331

**Intent:**
skateboard spots map where skaters add spots with photos and bust levels

**Spec:**
```
Type:       Mobile application with backend (skate spot map)
Auth:       Email or Apple/Google sign-in
Data model: Skater(id, username)
            Spot(id, creator_id -> Skater, name, kind, lat, lng, bust_level, photo_urls)
            Clip(id, spot_id -> Spot, skater_id -> Skater, video_url)
Features:   - Add spots with type (ledge, rail, bowl, stairs) and photos
            - Rate how likely security kicks you out
            - Upload short clips at a spot
            - Find spots near you on a map
API:        REST
            GET  /spots?near={lat,lng}
            POST /spots
            POST /spots/{id}/clips
Storage:    PostgreSQL with PostGIS, S3 (media)
Tech stack: React Native, Node.js, Mapbox
```

---

## Example 332

**Intent:**
I want saas that monitors SSL certificate expiry for all my client domains

**Spec:**
```
Type:       Web application (certificate expiry monitoring)
Auth:       Email + password login
Data model: Domain(id, owner_id, hostname, port)
            CertCheck(id, domain_id -> Domain, issuer, expires_at, valid, checked_at)
Features:   - Add domains one by one or by CSV
            - Check certificates daily with a TLS handshake
            - Warn at 30, 14 and 3 days before expiry
            - Flag invalid chains and hostname mismatches
API:        REST
            POST /domains
            GET  /domains
            POST /domains/{id}/check
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Celery Beat
```

---

## Example 333

**Intent:**
online flea market event for one weekend only, sellers get virtual booths

**Spec:**
```
Type:       Web application (virtual flea market)
Auth:       Email + password login
Data model: Event(id, name, opens_at, closes_at)
            Booth(id, event_id -> Event, seller_id, name, banner_url)
            Item(id, booth_id -> Booth, title, price, photo_url, sold)
            Order(id, item_id -> Item, buyer_email, paid, shipping_address)
Features:   - Rent a virtual booth for the event
            - Add items with photo and price
            - Open shopping only during the event weekend
            - Pay per item and mark it sold
API:        REST
            POST /events/{id}/booths
            POST /booths/{id}/items
            POST /items/{id}/buy
Storage:    PostgreSQL, S3 (photos)
Tech stack: Ruby on Rails, Stripe API
```

---

## Example 334

**Intent:**
Weekly scheduled script that reads our meetup RSVPs and emails no-shows a friendly note

**Spec:**
```
Type:       Scheduled script (no-show follow up)
Features:   - Load last week's RSVP list from the events database
            - Compare it with the check-in list
            - Email people who RSVPed but did not attend
            - Skip people who cancelled in advance
            - Write a summary log of emails sent
Input:      Database connection string, SMTP settings, email template file
Tech stack: Python, SQLAlchemy, smtplib, cron
```

---

## Example 335

**Intent:**
my grandma's sewing circle wants a simple site to show what they made for charity and how many items donated

**Spec:**
```
Type:       Web application (charity crafting tally)
Auth:       Simple shared password for members
Data model: Maker(id, name)
            Donation(id, maker_id -> Maker, item_kind, quantity, recipient, date, photo_url)
Features:   - Log items made with kind, quantity and recipient charity
            - Show totals per year and per charity
            - Show a photo gallery of recent items
            - Use large buttons and text for older users
API:        REST
            POST /donations
            GET  /totals
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 336

**Intent:**
SaaS that lets bloggers add a "listen to this article" audio player via text to speech

**Spec:**
```
Type:       Web application (article text-to-speech SaaS)
Auth:       Email + password login, site key
Data model: Site(id, owner_id, domain, voice, site_key)
            Article(id, site_id -> Site, url, content_hash, audio_url, duration_s)
Features:   - Embed a player script on article pages
            - Extract the article text from the page
            - Generate audio with a chosen voice and cache it
            - Regenerate only when the text changes
            - Show listens per article
API:        REST
            GET  /player/{site_key}.js
            POST /articles/audio
            GET  /sites/{id}/stats
Storage:    PostgreSQL, S3 (audio)
Tech stack: Node.js, Readability, Amazon Polly
```

---

## Example 337

**Intent:**
ice cream truck tracker so kids know when its near my street lol

**Spec:**
```
Type:       Mobile application with backend (vendor truck tracker)
Auth:       Driver login, no login for customers
Data model: Truck(id, name, driver_pin, lat, lng, live, updated_at)
            StreetAlert(id, device_token, lat, lng, radius_m)
Features:   - Share the truck's live location while the driver is on shift
            - Show trucks on a map in real time
            - Notify a phone when the truck comes within a chosen radius
            - Hide the location when the driver goes off shift
API:        REST + WebSocket
            POST /trucks/{id}/location
            WS   /trucks/live
            POST /alerts
Storage:    Redis (live locations), PostgreSQL
Tech stack: Flutter, Node.js, Firebase Cloud Messaging
```

---

## Example 338

**Intent:**
rate my setup community: people post desk setups and gear lists

**Spec:**
```
Type:       Web application (desk setup showcase)
Auth:       Email + password login
Data model: User(id, username, email)
            Setup(id, user_id -> User, title, photo_urls, description)
            Gear(id, setup_id -> Setup, category, name, link)
            Like(setup_id -> Setup, user_id -> User)
Features:   - Post setups with photos and a gear list
            - Tag gear by category (monitor, keyboard, chair)
            - Browse most-liked setups this week
            - Search setups containing a product
API:        REST
            GET  /setups?sort=top
            POST /setups
            POST /setups/{id}/like
            GET  /search?gear={name}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, SvelteKit
```

---

## Example 339

**Intent:**
need web for our hiking group in japan, events in japanese and english, people join hikes, pay share for bus

**Spec:**
```
Type:       Web application (bilingual hiking group)
Auth:       Email + password login, LINE login
Data model: Member(id, name, email, language)
            Hike(id, title_ja, title_en, date, mountain, difficulty, bus_cost_total, capacity)
            HikeSignup(hike_id -> Hike, member_id -> Member, paid)
Features:   - Post hikes with Japanese and English descriptions
            - Join a hike until capacity is reached
            - Split bus cost among participants
            - Pay online or mark cash paid
            - Switch language per user
API:        REST
            GET  /hikes
            POST /hikes
            POST /hikes/{id}/signups
Storage:    PostgreSQL
Tech stack: Python, Django (i18n), PAY.JP API
```

---

## Example 340

**Intent:**
a log search saas where small teams ship app logs and search them

**Spec:**
```
Type:       Web application (log management SaaS)
Auth:       Email + password login, ingest tokens
Data model: Team(id, name, retention_days)
            Source(id, team_id -> Team, name, ingest_token)
            LogLine(source_id, ts, level, message, attributes_json)
Features:   - Ingest logs over HTTPS in JSON lines
            - Search by text, level and attributes over a time range
            - Live tail new log lines
            - Save searches as alerts that email on matches
            - Delete logs older than the retention period
API:        REST
            POST /ingest
            GET  /search?q={query}&from={t1}&to={t2}
            GET  /tail
Storage:    ClickHouse
Tech stack: Go, React
```

---

## Example 341

**Intent:**
I'm creating an alumni giving campaign page with class year competition leaderboard

**Spec:**
```
Type:       Web application (alumni giving challenge)
Auth:       Email + password login for staff
Data model: Campaign(id, name, starts_at, ends_at, goal)
            Gift(id, campaign_id -> Campaign, donor_name, class_year, amount, anonymous)
Features:   - Accept online gifts with class year
            - Show a leaderboard of class years by participation and total
            - Show a live progress bar toward the goal
            - Hide names for anonymous gifts
API:        REST
            POST /campaigns/{id}/gifts
            GET  /campaigns/{id}/leaderboard
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe API
```

---

## Example 342

**Intent:**
Hackathon project gallery after the event, public voting for people's choice

**Spec:**
```
Type:       Web application (hackathon project gallery)
Auth:       Email verification for voters, GitHub login for teams
Data model: Project(id, team_name, title, description, video_url, repo_url, image_url)
            PublicVote(project_id -> Project, voter_email_hash)
Features:   - Let teams publish a project page with video and repo
            - Browse projects in a grid with filters by track
            - Allow one people's choice vote per verified email
            - Show the winner after voting closes
API:        REST
            GET  /projects
            POST /projects
            POST /projects/{id}/vote
Storage:    PostgreSQL
Tech stack: TypeScript, Astro, Supabase
```

---

## Example 343

**Intent:**
skill-share workshop night: members propose 15 minute lightning lessons, others pick schedule

**Spec:**
```
Type:       Web application (lightning lesson night)
Auth:       Email login with magic link
Data model: Night(id, date, venue, slots)
            Lesson(id, night_id -> Night, presenter, title, materials_needed)
            Interest(lesson_id -> Lesson, member_email)
Features:   - Propose a 15-minute lesson for a night
            - Mark interest in proposed lessons
            - Build the running order from the most popular proposals
            - Show a materials checklist for the venue
API:        REST
            POST /nights/{id}/lessons
            POST /lessons/{id}/interest
            GET  /nights/{id}/schedule
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 344

**Intent:**
saas to manage online communities' membership tiers with discord role sync

**Spec:**
```
Type:       Web application (paid community memberships)
Auth:       Discord OAuth login
Data model: Community(id, owner_id, guild_id, name)
            Tier(id, community_id -> Community, name, price, discord_role_id)
            Membership(id, tier_id -> Tier, discord_user_id, stripe_subscription_id, status)
Features:   - Create paid tiers linked to Discord roles
            - Subscribe to a tier with recurring payment
            - Add the Discord role when payment succeeds
            - Remove the role when the subscription ends
            - Show the owner revenue and churn
API:        REST
            POST /tiers
            POST /tiers/{id}/subscribe
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Node.js, discord.js, Stripe API, React
```

---

## Example 345

**Intent:**
pumpkin carving contest online for our neighbourhood

**Spec:**
```
Type:       Web application (photo contest)
Data model: Entry(id, household_name, street, photo_url, created_at)
            Vote(entry_id -> Entry, voter_cookie)
Features:   - Upload one pumpkin photo per household
            - Vote once per browser for a favourite
            - Close voting on Halloween night
            - Show the winning pumpkins
API:        REST
            POST /entries
            POST /entries/{id}/vote
            GET  /results
Storage:    SQLite, local file storage
Tech stack: Node.js, Express
```

---

## Example 346

**Intent:**
alumni job referral board: alumni at companies offer referrals, grads request them

**Spec:**
```
Type:       Web application (alumni referral board)
Auth:       LinkedIn sign-in, alumni email verification
Data model: Alum(id, name, company, title, grad_year)
            ReferralOffer(id, alum_id -> Alum, company, roles, monthly_limit)
            ReferralRequest(id, offer_id -> ReferralOffer, grad_name, resume_url, job_link, status)
Features:   - Offer referrals for your company with a monthly limit
            - Let graduates request a referral with resume and job link
            - Let alumni accept or decline requests
            - Track referral outcomes
API:        REST
            GET  /offers?company={c}
            POST /offers
            POST /offers/{id}/requests
            PATCH /requests/{id}
Storage:    PostgreSQL, S3 (resumes)
Tech stack: Python, FastAPI, React
```

---

## Example 347

**Intent:**
discord bot for photography club weekly theme challenge with reactions voting

**Spec:**
```
Type:       Bot (Discord)
Data model: Challenge(id, theme, week_start, channel_id)
            Submission(id, challenge_id -> Challenge, user_id, message_id)
Features:   - Announce a new theme every Monday
            - Accept one image per member in the challenge channel
            - Count star reactions as votes on Sunday
            - Announce the winner and keep a hall of fame
Storage:    SQLite
Tech stack: JavaScript, discord.js, node-cron
```

---

## Example 348

**Intent:**
platform for remote volunteers to tag wildlife camera trap photos

**Spec:**
```
Type:       Web application (camera trap classification)
Auth:       Email + password login, researcher role
Data model: Camera(id, site, lat, lng)
            Image(id, camera_id -> Camera, url, taken_at, retired)
            Classification(id, image_id -> Image, volunteer_id, species, count, empty)
Features:   - Show volunteers images one at a time
            - Tag species and count or mark the image empty
            - Retire an image after 5 agreeing classifications
            - Use a model to pre-filter empty images
            - Export consensus results for researchers
API:        REST
            GET  /images/next
            POST /images/{id}/classifications
            GET  /export/consensus.csv
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, Django, MegaDetector
```

---

## Example 349

**Intent:**
community choir auditions booking and results

**Spec:**
```
Type:       Web application (audition booking)
Auth:       Email + password login for directors
Data model: AuditionSlot(id, starts_at, candidate_name, candidate_email, voice_type)
            Result(id, slot_id -> AuditionSlot, placed_part, accepted, notes)
Features:   - Publish 10-minute audition slots
            - Let candidates book a slot and pick a voice type
            - Record the outcome and assigned part
            - Email results to candidates
API:        REST
            GET  /slots
            POST /slots/{id}/book
            POST /slots/{id}/result
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 350

**Intent:**
saas for coaches: clients fill a weekly check-in form, coach sees trends and replies

**Spec:**
```
Type:       Web application (coaching check-ins SaaS)
Auth:       Email + password login for coaches and clients
Data model: Coach(id, name, email)
            Client(id, coach_id -> Coach, name, email)
            CheckInForm(id, coach_id -> Coach, questions_json)
            CheckIn(id, client_id -> Client, answers_json, submitted_at, coach_reply)
Features:   - Build a weekly check-in form with scales and text questions
            - Remind clients every Sunday to fill it in
            - Show trends of scale answers per client
            - Reply to each check-in
API:        REST
            POST /forms
            POST /check-ins
            PATCH /check-ins/{id}/reply
            GET  /clients/{id}/trends
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 351

**Intent:**
pottery studio kiln firing queue, members put pieces in and get notified when fired

**Spec:**
```
Type:       Web application (kiln firing queue)
Auth:       Email + password login, studio tech role
Data model: Member(id, name, email)
            Piece(id, member_id -> Member, description, clay_body, firing_type, shelf_spot, status)
            Firing(id, kiln, firing_type, cone, loaded_at, unloaded_at)
            FiringPiece(firing_id -> Firing, piece_id -> Piece)
Features:   - Register pieces for bisque or glaze firing
            - Let the tech build a firing from waiting pieces
            - Notify members when their pieces are unloaded
            - Charge firing fees by piece size
API:        REST
            POST /pieces
            POST /firings
            POST /firings/{id}/unload
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 352

**Intent:**
salsa dance partner finder

**Spec:**
```
Type:       Web application (dance partner matching)
Auth:       Email + password login
Data model: Dancer(id, name, email, city, role, level, styles, goals)
            PartnerRequest(id, from_id -> Dancer, to_id -> Dancer, message, status)
Features:   - Create a profile with lead or follow role, level and styles
            - Search partners by city, style and level
            - Send a partner request with a message
            - Hide your profile when you have found a partner
API:        REST
            GET  /dancers?city={c}&style={s}
            POST /partner-requests
            PATCH /partner-requests/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 353

**Intent:**
marathon spectator app to track friends running and know where to cheer

**Spec:**
```
Type:       Web application (race spectator tracker)
Data model: Race(id, name, course_gpx_url, start_at)
            Runner(id, race_id -> Race, bib, name)
            Split(id, runner_id -> Runner, checkpoint_km, time_s)
            Follow(device_id, runner_id -> Runner)
Features:   - Search runners by name or bib
            - Import timing mat splits as they arrive
            - Predict when a runner will reach each kilometre
            - Show the predicted position on the course map
            - Push a notification as the runner nears your spot
API:        REST
            GET  /races/{id}/runners?q={name}
            POST /races/{id}/splits
            GET  /runners/{id}/prediction
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Mapbox, Web Push
```

---

## Example 354

**Intent:**
sailing crew finder, boat owners need crew for weekend races

**Spec:**
```
Type:       Web application (sailing crew finder)
Auth:       Email + password login
Data model: Sailor(id, name, email, experience, positions, club)
            Boat(id, owner_id -> Sailor, name, class, length_ft)
            CrewCall(id, boat_id -> Boat, race_date, positions_needed)
            CrewOffer(id, call_id -> CrewCall, sailor_id -> Sailor, status)
Features:   - Post a crew call for a race with needed positions
            - Show sailors matching positions and experience
            - Offer to crew and let the skipper accept
            - Keep a sailing log per sailor
API:        REST
            GET  /crew-calls
            POST /crew-calls
            POST /crew-calls/{id}/offers
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 355

**Intent:**
open studios art trail weekend: artists register studios, visitors get map and plan route

**Spec:**
```
Type:       Web application (open studios trail)
Auth:       Email + password login for artists
Data model: Artist(id, name, email, medium, bio, image_urls)
            Studio(id, artist_id -> Artist, address, lat, lng, open_days, accessible)
            SavedStop(device_id, studio_id -> Studio)
Features:   - Register a studio with medium, images and opening days
            - Show all studios on a map with filters by medium
            - Save studios to a personal list
            - Plan a walking or driving route between saved studios
            - Show step-free access information
API:        REST
            GET  /studios?medium={m}
            POST /studios
            GET  /route?stops={ids}
Storage:    PostgreSQL
Tech stack: Python, Django, Leaflet, OSRM
```

---

## Example 356

**Intent:**
small family foundation wants online grant applications and board review

**Spec:**
```
Type:       Web application (grant applications)
Auth:       Email + password login for applicants and board members
Data model: Organisation(id, name, registration_number, email)
            GrantRound(id, title, budget, opens_at, closes_at)
            Application(id, round_id -> GrantRound, org_id -> Organisation, amount_requested, narrative, budget_file_url, status)
            BoardScore(id, application_id -> Application, member_id, score, comment)
Features:   - Fill a multi-step application with autosave
            - Upload budget and supporting documents
            - Let board members score applications
            - Track awarded amount against the round budget
            - Email decisions to applicants
API:        REST
            POST /applications
            PATCH /applications/{id}
            POST /applications/{id}/scores
            GET  /rounds/{id}/summary
Storage:    PostgreSQL, S3 (documents)
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 357

**Intent:**
dorm laundry machines status so we dont walk down for nothing

**Spec:**
```
Type:       IoT system (laundry machine status)
Data model: Machine(id, building, number, kind, status, cycle_started_at)
            Watch(id, machine_id -> Machine, push_subscription)
Features:   - Read machine power draw with a smart plug or current sensor
            - Detect running and finished cycles from power levels
            - Show live status of every machine on a web page
            - Notify a student when a watched machine finishes
Input:      Current sensor readings from each machine every 10 seconds
API:        REST
            POST /readings
            GET  /machines?building={b}
            POST /machines/{id}/watch
Storage:    SQLite
Tech stack: ESP32 (MicroPython), MQTT, Python, FastAPI
```

---

## Example 358

**Intent:**
campus leftover food alerts from catered events, students get notified

**Spec:**
```
Type:       Web application (free food alerts)
Auth:       University SSO
Data model: Student(id, email, push_subscription, dietary)
            FoodPost(id, poster_id, location, description, dietary_tags, available_until, photo_url)
Features:   - Let event staff post leftover food with a location
            - Tag posts as vegetarian, vegan or halal
            - Push notifications to subscribed students with matching diets
            - Hide posts after the available time
API:        REST
            POST /posts
            GET  /posts/active
            POST /subscriptions
Storage:    PostgreSQL
Tech stack: Node.js, Express, Web Push, React
```

---

## Example 359

**Intent:**
textbook swap for students at same uni

**Spec:**
```
Type:       Web application (textbook exchange)
Auth:       University email verification
Data model: Student(id, email, name)
            Listing(id, seller_id -> Student, isbn, title, edition, condition, price, course_code, status)
Features:   - List a textbook by scanning or typing its ISBN
            - Search by course code or ISBN
            - Message sellers inside the site
            - Mark books as sold
API:        REST
            GET  /listings?course={code}
            POST /listings
            POST /listings/{id}/messages
Storage:    PostgreSQL
Tech stack: Python, Django, Google Books API
```

---

## Example 360

**Intent:**
Lab equipment booking for our university research group (microscopes, centrifuges) with training requirements

**Spec:**
```
Type:       Web application (lab equipment booking)
Auth:       University SSO, lab manager role
Data model: Researcher(id, name, email, group)
            Instrument(id, name, room, requires_training, max_hours)
            Training(researcher_id -> Researcher, instrument_id -> Instrument, certified_on)
            Reservation(id, instrument_id -> Instrument, researcher_id -> Researcher, starts_at, ends_at, project_code)
Features:   - Reserve instruments on a calendar
            - Block reservations without valid training
            - Enforce maximum hours per reservation
            - Charge usage to project codes monthly
            - Report instrument utilisation
API:        REST
            GET  /instruments/{id}/calendar
            POST /reservations
            GET  /reports/usage?month={m}
Storage:    PostgreSQL
Tech stack: Python, Django, FullCalendar
```

---

## Example 361

**Intent:**
journal club paper picker, people suggest papers and vote, presenter rota

**Spec:**
```
Type:       Web application (journal club)
Auth:       Email + password login
Data model: Member(id, name, email)
            Paper(id, doi, title, authors, suggested_by -> Member, votes)
            Meeting(id, date, paper_id -> Paper, presenter_id -> Member)
Features:   - Suggest papers by DOI with metadata fetched from Crossref
            - Vote for papers to discuss
            - Rotate presenters fairly
            - Send the paper link to all members a week ahead
API:        REST
            POST /papers
            POST /papers/{id}/vote
            GET  /meetings
Storage:    SQLite
Tech stack: Python, Flask, Crossref API
```

---

## Example 362

**Intent:**
research participant recruitment site, studies post and people sign up if they match criteria

**Spec:**
```
Type:       Web application (study participant recruitment)
Auth:       Email + password login for participants and researchers, ethics admin role
Data model: Participant(id, email, birth_year, gender, languages, conditions)
            Study(id, researcher_id, title, criteria_json, payment, approved)
            StudySignup(id, study_id -> Study, participant_id -> Participant, status)
Features:   - Let participants fill a screening profile once
            - Show participants only studies whose criteria they match
            - Require ethics approval before a study is visible
            - Share contact details only after the participant signs up
API:        REST
            GET  /studies/eligible
            POST /studies
            POST /studies/{id}/signup
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 363

**Intent:**
employee pulse survey every 2 weeks anonymous, managers see team averages only if 5+ answers

**Spec:**
```
Type:       Web application (employee pulse surveys)
Auth:       Company SSO
Data model: Team(id, name, manager_id)
            Pulse(id, sent_on, questions_json)
            PulseAnswer(id, pulse_id -> Pulse, team_id -> Team, answers_json)
Features:   - Send a short survey every two weeks by Slack DM
            - Store answers without a link to the employee
            - Show team averages only when at least 5 people answered
            - Show trend lines per question
API:        REST
            POST /pulses
            POST /pulses/{id}/answers
            GET  /teams/{id}/results
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Slack API, React
```

---

## Example 364

**Intent:**
whistleblower reporting channel for a mid-size company, EU directive compliant

**Spec:**
```
Type:       Web application (whistleblowing channel)
Auth:       Anonymous reporters with a case key, case handler login with 2FA
Data model: Case(id, case_key_hash, category, description_encrypted, status, received_at, ack_due, feedback_due)
            CaseMessage(id, case_id -> Case, from_reporter, body_encrypted, sent_at)
Features:   - Submit a report anonymously and receive a case key
            - Acknowledge receipt within 7 days
            - Exchange messages with the reporter through the case key
            - Track the 3-month feedback deadline
            - Encrypt all report content at rest
API:        REST
            POST /reports
            GET  /cases/{key}
            POST /cases/{key}/messages
Storage:    PostgreSQL (encrypted fields)
Tech stack: Java, Spring Boot, React
```

---

## Example 365

**Intent:**
film students borrow cameras lenses and lights, checkout with damage notes

**Spec:**
```
Type:       Web application (film equipment checkout)
Auth:       University SSO, equipment officer role
Data model: Student(id, name, email, course)
            Kit(id, name, serial_number, category, status)
            Checkout(id, student_id -> Student, out_at, due_at, returned_at, notes)
            CheckoutItem(checkout_id -> Checkout, kit_id -> Kit, condition_out, condition_in)
Features:   - Reserve kits for a shoot date range
            - Check out several items at once by barcode scan
            - Record condition notes on return
            - Block students with overdue items from new bookings
API:        REST
            GET  /kits?available={from,to}
            POST /checkouts
            PATCH /checkouts/{id}/return
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 366

**Intent:**
triathlon club training log, swim bike run with weekly totals

**Spec:**
```
Type:       Web application (multisport training log)
Auth:       Email + password login, coach role
Data model: Athlete(id, name, email, coach_id)
            Workout(id, athlete_id -> Athlete, sport, date, duration_min, distance_km, rpe, notes)
            PlannedWorkout(id, athlete_id -> Athlete, sport, date, description)
Features:   - Log swim, bike and run workouts
            - Show weekly totals per sport
            - Let the coach plan workouts for athletes
            - Compare planned versus completed
            - Import workouts from .fit files
API:        REST
            POST /workouts
            POST /workouts/import
            GET  /athletes/{id}/week
Storage:    PostgreSQL
Tech stack: Python, FastAPI, fitparse, React
```

---

## Example 367

**Intent:**
model rocket club launch day log: who launched which rocket, motor, altitude

**Spec:**
```
Type:       Web application (rocket launch log)
Auth:       Email + password login, range safety officer role
Data model: Flyer(id, name, email, certification_level)
            Rocket(id, flyer_id -> Flyer, name, diameter_mm, mass_g)
            Launch(id, rocket_id -> Rocket, date, motor, altitude_m, recovery_ok, rso_approved)
Features:   - Register rockets with specs
            - Check that the motor class is allowed for the flyer's certification
            - Let the RSO approve each launch card
            - Record altitude and recovery
            - Show the club's highest flights
API:        REST
            POST /rockets
            POST /launches
            PATCH /launches/{id}/approve
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 368

**Intent:**
dog show entries site, people enter dogs in classes and judges get catalogue

**Spec:**
```
Type:       Web application (dog show entries)
Auth:       Email + password login
Data model: Exhibitor(id, name, email)
            Dog(id, exhibitor_id -> Exhibitor, registered_name, breed, sex, birth_date)
            Show(id, name, date, closing_date)
            Entry(id, show_id -> Show, dog_id -> Dog, class_name, catalogue_number, fee_paid)
Features:   - Enter dogs into breed classes before the closing date
            - Pay entry fees online
            - Assign catalogue numbers
            - Generate the show catalogue as PDF
            - Record placements and publish results
API:        REST
            POST /shows/{id}/entries
            GET  /shows/{id}/catalogue.pdf
            POST /shows/{id}/results
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Stripe API
```

---

## Example 369

**Intent:**
riding stable lesson booking, matching riders to horses

**Spec:**
```
Type:       Web application (riding lesson booking)
Auth:       Email + password login
Data model: Rider(id, name, email, level, weight_kg)
            Horse(id, name, max_rider_kg, level, lessons_per_day_max)
            Lesson(id, starts_at, instructor, level, capacity)
            LessonBooking(lesson_id -> Lesson, rider_id -> Rider, horse_id -> Horse)
Features:   - Book a group lesson for your level
            - Assign horses respecting rider weight and horse level
            - Limit each horse's lessons per day
            - Let instructors see the day's assignments
API:        REST
            GET  /lessons?level={l}
            POST /lessons/{id}/bookings
            POST /lessons/{id}/assign-horses
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 370

**Intent:**
art residency applications with portfolio and panel review

**Spec:**
```
Type:       Web application (residency applications)
Auth:       Email + password login, panelist role
Data model: Applicant(id, name, email, website)
            Application(id, applicant_id -> Applicant, proposal, cv_url, status)
            PortfolioImage(id, application_id -> Application, image_url, title, year, medium)
            PanelScore(application_id -> Application, panelist_id, score, comment)
Features:   - Submit a proposal, CV and up to 10 portfolio images
            - Show panelists portfolios in a full-screen viewer
            - Score applications and leave comments
            - Shortlist and notify applicants
API:        REST
            POST /applications
            POST /applications/{id}/images
            POST /applications/{id}/scores
Storage:    PostgreSQL, S3 (images)
Tech stack: Ruby on Rails
```

---

## Example 371

**Intent:**
student clubs submit budget requests to student union and treasurer approves

**Spec:**
```
Type:       Web application (club budget requests)
Auth:       University SSO, roles: club officer, treasurer
Data model: Club(id, name, annual_budget, spent)
            BudgetRequest(id, club_id -> Club, purpose, amount, event_date, status)
            Receipt(id, request_id -> BudgetRequest, amount, file_url)
Features:   - Submit a budget request with purpose and amount
            - Let the treasurer approve, reduce or reject
            - Upload receipts after the event
            - Show each club's remaining budget
API:        REST
            POST /requests
            PATCH /requests/{id}
            POST /requests/{id}/receipts
Storage:    PostgreSQL, S3 (receipts)
Tech stack: Node.js, Express, React
```

---

## Example 372

**Intent:**
scholarship application portal for my rotary club

**Spec:**
```
Type:       Web application (scholarship applications)
Auth:       Email + password login for applicants and reviewers
Data model: Scholarship(id, name, amount, deadline, criteria)
            Application(id, scholarship_id -> Scholarship, student_name, email, school, gpa, essay, recommendation_url, status)
            Review(application_id -> Application, reviewer_id, score)
Features:   - Apply with an essay and upload a recommendation letter
            - Request recommendation letters directly from teachers by email
            - Let reviewers score blind (names hidden)
            - Pick winners and send award letters
API:        REST
            POST /applications
            POST /applications/{id}/recommendation-request
            POST /applications/{id}/reviews
Storage:    PostgreSQL, S3 (documents)
Tech stack: Python, Django
```

---

## Example 373

**Intent:**
policy acknowledgement saas, employees must read and sign new policies, HR tracks

**Spec:**
```
Type:       Web application (policy acknowledgement SaaS)
Auth:       SSO (Google Workspace, Microsoft)
Data model: Policy(id, company_id, title, version, document_url, due_days)
            Assignment(id, policy_id -> Policy, employee_email, assigned_at)
            Acknowledgement(id, assignment_id -> Assignment, signed_at, ip_address)
Features:   - Upload policy versions
            - Assign policies to departments
            - Require employees to scroll the document before signing
            - Remind people who have not signed
            - Export an audit report of acknowledgements
API:        REST
            POST /policies
            POST /policies/{id}/assign
            POST /assignments/{id}/acknowledge
            GET  /reports/audit.csv
Storage:    PostgreSQL, S3 (documents)
Tech stack: Python, Django, React
```

---

## Example 374

**Intent:**
RC car racing club lap timing with transponders, results online

**Spec:**
```
Type:       Web application (RC racing results)
Auth:       Email + password login for race directors
Data model: Driver(id, name, transponder_id)
            Heat(id, race_day, class_name, round)
            Lap(id, heat_id -> Heat, driver_id -> Driver, lap_number, time_ms)
Features:   - Receive lap passings from the timing decoder
            - Show live lap times and positions during a heat
            - Rank drivers by laps completed and total time
            - Publish race day results and best laps
API:        REST + WebSocket
            POST /heats/{id}/passings
            WS   /heats/{id}/live
            GET  /race-days/{date}/results
Storage:    PostgreSQL
Tech stack: Python, FastAPI, pyserial, Vue.js
```

---

## Example 375

**Intent:**
ok so im on the board of a community pool. need online season passes and daily guest check in

**Spec:**
```
Type:       Web application (pool membership)
Auth:       Email + password login for families, staff PIN
Data model: Family(id, name, email, address)
            Pass(id, family_id -> Family, season, members_json, paid)
            GuestVisit(id, family_id -> Family, guest_count, date)
Features:   - Buy a family season pass online
            - Show a QR code for check-in at the gate
            - Record daily guest passes and charge them
            - Show staff today's visitor count
API:        REST
            POST /passes
            POST /checkins
            POST /guest-visits
            GET  /today
Storage:    PostgreSQL
Tech stack: Node.js, Express, Stripe API, Vue.js
```

---

## Example 376

**Intent:**
crossword makers community to share puzzles they made and others solve in browser

**Spec:**
```
Type:       Web application (crossword sharing)
Auth:       Email + password login
Data model: Constructor(id, username, email)
            Puzzle(id, constructor_id -> Constructor, title, grid_json, clues_json, difficulty)
            Solve(id, puzzle_id -> Puzzle, user_id, seconds, completed, rating)
Features:   - Build a grid with black squares and symmetry
            - Write across and down clues
            - Solve puzzles in the browser with a timer
            - Upload and download .puz files
            - Rate puzzles after solving
API:        REST
            GET  /puzzles
            POST /puzzles
            POST /puzzles/{id}/solves
Storage:    PostgreSQL
Tech stack: TypeScript, React, Node.js
```

---

## Example 377

**Intent:**
origami

**Spec:**
```
Type:       Web application (origami diagram sharing)
Auth:       Email + password login
Data model: Folder(id, username, email)
            Model(id, folder_id -> Folder, name, designer, difficulty, paper_size, diagram_pdf_url, cp_image_url)
            Attempt(id, model_id -> Model, folder_id -> Folder, photo_url, comment)
Features:   - Share diagrams and crease patterns for models
            - Credit the original designer
            - Filter by difficulty and paper size
            - Post photos of your folded attempts
API:        REST
            GET  /models?difficulty={d}
            POST /models
            POST /models/{id}/attempts
Storage:    PostgreSQL, S3 (files)
Tech stack: Python, Django
```

---

## Example 378

**Intent:**
Hi! Me and my friends play Magic cards and want site to track who owns which cards so we can borrow for decks.

**Spec:**
```
Type:       Web application (shared card collection)
Auth:       Email + password login, friend group invite
Data model: Player(id, name, email)
            Card(id, scryfall_id, name, set_code, image_url)
            Owned(player_id -> Player, card_id -> Card, quantity)
            CardLoan(id, card_id -> Card, owner_id -> Player, borrower_id -> Player, quantity, returned)
Features:   - Import a collection from a CSV export
            - Look up card data and images from Scryfall
            - Paste a deck list and see who owns each missing card
            - Record card loans and returns
API:        REST
            POST /collection/import
            POST /decks/check
            POST /loans
Storage:    PostgreSQL
Tech stack: Node.js, Express, Scryfall API, React
```

---

## Example 379

**Intent:**
community pantry inventory so volunteers know what to buy

**Spec:**
```
Type:       Web application (pantry inventory)
Auth:       Email + password login for volunteers
Data model: Product(id, name, category, unit, min_level)
            StockCount(id, product_id -> Product, quantity, counted_at, counted_by)
            Purchase(id, product_id -> Product, quantity, cost, bought_on)
Features:   - Record stock counts after each opening
            - Show items below minimum level as a shopping list
            - Log purchases and donations
            - Show monthly spend by category
API:        REST
            POST /counts
            GET  /shopping-list
            POST /purchases
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 380

**Intent:**
QR codes in public toilets in our mall, people tap a smiley and cleaners get alerted if bad

**Spec:**
```
Type:       Web application (facility feedback)
Auth:       Email + password login for facility staff
Data model: Restroom(id, location, qr_token)
            Feedback(id, restroom_id -> Restroom, rating, issue, created_at)
            Alert(id, restroom_id -> Restroom, opened_at, resolved_at, resolved_by)
Features:   - Show a one-tap smiley page per QR code
            - Ask for the issue type on a negative rating
            - Open an alert after two bad ratings within 30 minutes
            - Notify cleaners on duty by SMS
            - Report satisfaction per restroom
API:        REST
            POST /r/{token}/feedback
            GET  /alerts?open=true
            PATCH /alerts/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Twilio API
```

---

## Example 381

**Intent:**
woodworking plans store where makers sell PDF plans and customers post their builds

**Spec:**
```
Type:       Web application (woodworking plans)
Auth:       Email + password login
Data model: Designer(id, name, email)
            Plan(id, designer_id -> Designer, title, difficulty, tools, price, pdf_url)
            Order(id, plan_id -> Plan, buyer_email, paid)
            Build(id, plan_id -> Plan, user_id, photo_url, notes)
Features:   - Sell PDF plans with a cut list and tool list
            - Deliver plans by download link after payment
            - Let buyers post photos of their builds
            - Filter plans by difficulty and tools needed
API:        REST
            GET  /plans
            POST /plans/{id}/checkout
            POST /plans/{id}/builds
Storage:    PostgreSQL, S3 (PDFs and photos)
Tech stack: Node.js, Next.js, Stripe API
```

---

## Example 382

**Intent:**
training compliance tracker for volunteer firefighters certifications

**Spec:**
```
Type:       Web application (certification tracking)
Auth:       Email + password login, chief role
Data model: Firefighter(id, name, email, station)
            CertType(id, name, valid_months)
            Certification(id, firefighter_id -> Firefighter, cert_type_id -> CertType, issued_on, expires_on, file_url)
            TrainingSession(id, title, date, hours)
Features:   - Record certifications with expiry dates
            - Warn members and the chief 60 days before expiry
            - Log attendance at training sessions
            - Show a station readiness matrix
API:        REST
            POST /certifications
            POST /sessions/{id}/attendance
            GET  /readiness
Storage:    PostgreSQL, S3 (certificates)
Tech stack: Python, Django
```

---

## Example 383

**Intent:**
neighborhood pickup soccer for adults, rsvp with max 22 players and a waitlist

**Spec:**
```
Type:       Web application (pickup game RSVP)
Auth:       Email login with magic link
Data model: Player(id, name, email)
            PickupGame(id, field, starts_at, max_players)
            GameRsvp(game_id -> PickupGame, player_id -> Player, status, created_at)
Features:   - Post weekly games
            - RSVP until 22 players then join a waitlist
            - Promote the first waitlisted player when someone drops out
            - Split RSVPed players into two balanced teams
API:        REST
            GET  /games
            POST /games/{id}/rsvp
            DELETE /games/{id}/rsvp
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 384

**Intent:**
surf report community, locals post wave conditions with photo each morning

**Spec:**
```
Type:       Web application (community surf reports)
Auth:       Email + password login
Data model: Surfer(id, username, email)
            Break(id, name, lat, lng)
            SurfReport(id, break_id -> Break, surfer_id -> Surfer, wave_height_ft, wind, crowd, rating, photo_url, posted_at)
Features:   - Post a morning report with size, wind, crowd and photo
            - Show buoy and tide data next to reports
            - Show the latest report per break
            - Rate reports for accuracy
API:        REST
            GET  /breaks
            POST /breaks/{id}/reports
            GET  /breaks/{id}/tides
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Express, NOAA API, React
```

---

## Example 385

**Intent:**
platform for open source projects to post good first issues for newcomers, pulls from github

**Spec:**
```
Type:       Web application (beginner issue finder)
Auth:       GitHub OAuth login
Data model: Repo(id, full_name, language, stars, added_by)
            Issue(id, repo_id -> Repo, number, title, labels, url, updated_at, open)
            Bookmark(user_id, issue_id -> Issue)
Features:   - Add repositories to track
            - Sync issues labelled "good first issue" from the GitHub API hourly
            - Filter by language and repository size
            - Bookmark issues
            - Hide closed or assigned issues
API:        REST
            GET  /issues?language={l}
            POST /repos
            POST /issues/{id}/bookmark
Storage:    PostgreSQL
Tech stack: Go, GitHub REST API, HTMX
```

---

## Example 386

**Intent:**
sudoku league for retirement home residents, weekly puzzles printed and scores entered by staff

**Spec:**
```
Type:       Web application (puzzle league)
Auth:       Email + password login for staff
Data model: Resident(id, name, home)
            WeeklyPuzzle(id, week, difficulty, puzzle_pdf_url, solution)
            Result(id, puzzle_id -> WeeklyPuzzle, resident_id -> Resident, minutes, correct)
Features:   - Generate weekly puzzles at three difficulties as printable PDFs
            - Enter residents' completion times
            - Show a league table per home
            - Print certificates for monthly winners
API:        REST
            POST /puzzles/generate
            POST /results
            GET  /league
Storage:    SQLite
Tech stack: Python, Flask, ReportLab
```

---

## Example 387

**Intent:**
self hosted alternative to a link-in-bio page, Go and no javascript

**Spec:**
```
Type:       Web application (self-hosted link page)
Auth:       Single admin password
Data model: Profile(name, bio, avatar_path, theme)
            Link(id, title, url, position)
Features:   - Render a single profile page with links
            - Edit links and profile from an admin page
            - Count clicks through a redirect handler
            - Serve everything without client-side JavaScript
API:        REST
            GET  /
            GET  /go/{id}
            POST /admin/links
Storage:    SQLite
Tech stack: Go, html/template
```

---

## Example 388

**Intent:**
cleanup volunteer events where you register, get gloves bags at a meeting point, and log trash bags collected

**Spec:**
```
Type:       Web application (cleanup events)
Auth:       Email + password login
Data model: Organiser(id, name, email)
            CleanupEvent(id, organiser_id -> Organiser, location, lat, lng, starts_at, kits_available)
            Registration(id, event_id -> CleanupEvent, name, email, needs_kit, bags_collected)
Features:   - Create cleanup events with a meeting point
            - Register and request a glove-and-bag kit
            - Stop kit requests when kits run out
            - Record bags collected per person after the event
            - Show totals across all events
API:        REST
            POST /events
            POST /events/{id}/registrations
            PATCH /registrations/{id}
            GET  /totals
Storage:    PostgreSQL
Tech stack: Node.js, Next.js
```

---

## Example 389

**Intent:**
gaming clan website with members roster, ranks and match history

**Spec:**
```
Type:       Web application (gaming clan site)
Auth:       Steam OpenID login
Data model: ClanMember(id, steam_id, nickname, rank, joined_on)
            ClanMatch(id, opponent, played_at, map, our_score, their_score)
            MatchPlayer(match_id -> ClanMatch, member_id -> ClanMember, kills, deaths)
Features:   - Show a roster with ranks and avatars from Steam
            - Record matches with per-player stats
            - Show win rate per map
            - Let officers promote and demote members
API:        REST
            GET  /roster
            POST /matches
            PATCH /members/{id}/rank
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Steam Web API
```

---

## Example 390

**Intent:**
I need simple ticket raffle site for our charity, people buy numbered tickets and draw is random and provable

**Spec:**
```
Type:       Web application (charity raffle)
Auth:       Email + password login for organisers
Data model: Raffle(id, title, ticket_price, max_tickets, draw_at, seed_hash, seed)
            RaffleTicket(id, raffle_id -> Raffle, number, buyer_email, paid)
            Prize(id, raffle_id -> Raffle, rank, description, winning_ticket_id -> RaffleTicket)
Features:   - Sell numbered tickets online
            - Publish a hash of the random seed before the draw
            - Draw winners from the seed and reveal it for verification
            - Email winners and show results publicly
API:        REST
            POST /raffles/{id}/tickets
            POST /raffles/{id}/draw
            GET  /raffles/{id}/results
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Stripe API
```

---

## Example 391

**Intent:**
platform for peer reviewing pull requests between solo developers who have no team

**Spec:**
```
Type:       Web application (peer PR review exchange)
Auth:       GitHub OAuth login
Data model: Dev(id, github_login, languages, karma)
            ReviewRequest(id, author_id -> Dev, pr_url, language, size_lines, status)
            PeerReview(id, request_id -> ReviewRequest, reviewer_id -> Dev, helpful)
Features:   - Submit a pull request link for review
            - Earn karma by reviewing others' PRs and spend it to request reviews
            - Match requests to reviewers by language
            - Confirm the review was left on GitHub through the API
            - Rate review helpfulness
API:        REST
            POST /requests
            GET  /requests/for-me
            POST /requests/{id}/claim
            POST /requests/{id}/complete
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, GitHub API, React
```

---

## Example 392

**Intent:**
small game: online word guessing game for our language exchange club, original rules, multiplayer

**Spec:**
```
Type:       Browser game (multiplayer word guessing)
Data model: Room(code, language, round, clue_giver_id)
            Player(id, room_code, name, score)
Features:   - Create a room in a chosen language
            - Give one player a secret word and let them type one-word clues
            - Let others guess within 60 seconds
            - Award points to the guesser and clue giver
            - Rotate the clue giver each round
API:        WebSocket
            WS   /rooms/{code}
Storage:    In-memory, word lists in JSON files
Tech stack: JavaScript, Node.js, Socket.IO
```

---

## Example 393

**Intent:**
mobile library bus schedule and stops, people request books to be brought

**Spec:**
```
Type:       Web application (mobile library service)
Auth:       Library card login
Data model: Stop(id, name, lat, lng)
            Visit(id, stop_id -> Stop, arrives_at, departs_at)
            HoldRequest(id, patron_card, title, isbn, stop_id -> Stop, status)
Features:   - Show the bus timetable and stops on a map
            - Request a book to be brought to your stop
            - Notify patrons when the bus is running late
            - Give staff a packing list per route day
API:        REST
            GET  /stops
            GET  /visits?stop={id}
            POST /holds
Storage:    PostgreSQL
Tech stack: Python, Django, Leaflet
```

---

## Example 394

**Intent:**
hiking club gear library: tents, sleeping bags, stoves lent to members for trips

**Spec:**
```
Type:       Web application (outdoor gear library)
Auth:       Email + password login, gear officer role
Data model: Member(id, name, email)
            GearItem(id, name, kind, size, condition)
            GearLoan(id, member_id -> Member, trip_name, out_on, due_on, returned_on)
            GearLoanItem(loan_id -> GearLoan, item_id -> GearItem)
Features:   - Show gear available for trip dates
            - Reserve a set of items for a trip
            - Record condition and missing parts on return
            - Flag items that need repair
API:        REST
            GET  /gear?from={d1}&to={d2}
            POST /loans
            PATCH /loans/{id}/return
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 395

**Intent:**
Website where people offer free rooms for visiting musicians on tour (couch hosting for bands)

**Spec:**
```
Type:       Web application (touring musician hosting)
Auth:       Email + password login, verified profiles
Data model: Host(id, name, email, city, beds, has_parking, notes)
            Band(id, name, email, members_count)
            StayRequest(id, band_id -> Band, host_id -> Host, date, status)
            StayReview(id, request_id -> StayRequest, author_kind, rating, text)
Features:   - List a couch or spare room with beds and van parking
            - Search hosts by city and date
            - Request a stay for a tour date
            - Leave reviews after the stay in both directions
API:        REST
            GET  /hosts?city={c}
            POST /stay-requests
            PATCH /stay-requests/{id}
            POST /stay-requests/{id}/reviews
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 396

**Intent:**
pigeon racing club results with distance and velocity calc

**Spec:**
```
Type:       Web application (pigeon race results)
Auth:       Email + password login for club secretary
Data model: Fancier(id, name, loft_lat, loft_lng)
            PigeonRace(id, release_point, release_lat, release_lng, released_at)
            Arrival(id, race_id -> PigeonRace, fancier_id -> Fancier, ring_number, clocked_at)
Features:   - Calculate each loft's distance from the release point
            - Calculate velocity in metres per minute from clock time
            - Rank arrivals by velocity
            - Publish results and season averages
API:        REST
            POST /races
            POST /races/{id}/arrivals
            GET  /races/{id}/results
Storage:    PostgreSQL
Tech stack: Python, Django, geopy
```

---

## Example 397

**Intent:**
quiz bowl practice question bank for high school teams with buzzer mode

**Spec:**
```
Type:       Web application (quiz bowl practice)
Auth:       Email + password login, coach role
Data model: Question(id, category, difficulty, text, answer)
            PracticeSession(id, coach_id, started_at)
            Buzz(id, session_id -> PracticeSession, question_id -> Question, student_name, word_index, correct)
Features:   - Read questions word by word on screen
            - Let students buzz from their phones
            - Record where in the question they buzzed
            - Show category strengths per student
API:        REST + WebSocket
            GET  /questions?category={c}
            WS   /sessions/{id}
            GET  /sessions/{id}/stats
Storage:    PostgreSQL
Tech stack: TypeScript, Node.js, Socket.IO, React
```

---

## Example 398

**Intent:**
platform for local farms offering volunteer days, people sign up to help harvest

**Spec:**
```
Type:       Web application (farm volunteer days)
Auth:       Email + password login
Data model: Farm(id, name, email, address)
            VolunteerDay(id, farm_id -> Farm, date, task, spots, includes_lunch)
            DaySignup(day_id -> VolunteerDay, volunteer_email, name)
Features:   - Let farms post volunteer days with tasks
            - Sign up for a day until spots run out
            - Send directions and what to bring
            - Cancel days for bad weather with notifications
API:        REST
            GET  /days
            POST /days
            POST /days/{id}/signups
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 399

**Intent:**
anonymous compliments site for school, every compliment moderated

**Spec:**
```
Type:       Web application (moderated compliments)
Auth:       School SSO for students, teacher moderator role
Data model: Compliment(id, to_student_id, text, status, created_at)
            Student(id, name, email)
Features:   - Send an anonymous compliment to a classmate
            - Hold every compliment for teacher approval
            - Block messages with flagged words automatically
            - Show students their approved compliments
API:        REST
            POST /compliments
            GET  /compliments/mine
            PATCH /compliments/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 400

**Intent:**
neighborhood solar group-buy, households sign up to get a discount when 30 join

**Spec:**
```
Type:       Web application (solar group purchase)
Auth:       Email + password login
Data model: Household(id, name, email, address, roof_type, annual_kwh)
            Campaign(id, area, target_signups, deadline, installer)
            Signup(campaign_id -> Campaign, household_id -> Household, status)
            Quote(id, household_id -> Household, kw, price)
Features:   - Show campaign progress toward the signup target
            - Collect roof type and yearly usage
            - Unlock the group price when the target is reached
            - Let the installer upload individual quotes
API:        REST
            GET  /campaigns/{id}
            POST /campaigns/{id}/signups
            POST /households/{id}/quotes
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 401

**Intent:**
homebrew beer club: share recipes, and run a judged competition with BJCP style scoresheets

**Spec:**
```
Type:       Web application (homebrew club)
Auth:       Email + password login, judge role
Data model: Brewer(id, name, email)
            Recipe(id, brewer_id -> Brewer, name, style, og, fg, ibu, grain_bill, hops, yeast)
            CompEntry(id, brewer_id -> Brewer, recipe_id -> Recipe, style, entry_number)
            Scoresheet(id, entry_id -> CompEntry, judge_id, aroma, appearance, flavor, mouthfeel, overall, comments)
Features:   - Share recipes and calculate ABV from gravities
            - Register competition entries by style with anonymous entry numbers
            - Fill scoresheets with the five standard sections
            - Rank entries per style and email scoresheets to brewers
API:        REST
            POST /recipes
            POST /entries
            POST /entries/{id}/scoresheets
            GET  /results
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 402

**Intent:**
sourdough starter sharing map, people give away starter

**Spec:**
```
Type:       Web application (starter sharing map)
Auth:       Email + password login
Data model: Baker(id, name, email, area, lat, lng)
            Starter(id, baker_id -> Baker, name, flour, age_years, story, available)
            Request(id, starter_id -> Starter, requester_id -> Baker, status)
Features:   - Add your starter with flour type and story
            - Find starters near you on a map
            - Request a portion and arrange pickup
            - Show a family tree of starters passed on
API:        REST
            GET  /starters?near={lat,lng}
            POST /starters
            POST /starters/{id}/requests
Storage:    PostgreSQL
Tech stack: Node.js, Express, Leaflet
```

---

## Example 403

**Intent:**
community orchard fruit picking map

**Spec:**
```
Type:       Web application (public fruit tree map)
Auth:       Email + password login for contributors
Data model: FruitTree(id, kind, variety, lat, lng, public_access, notes)
            RipeReport(id, tree_id -> FruitTree, ripe, reported_on)
Features:   - Map public fruit trees by kind
            - Report when a tree is ripe
            - Show what is ripe this week
            - Mark trees on private land as ask-first
API:        REST
            GET  /trees?kind={k}
            POST /trees
            POST /trees/{id}/ripe
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Flask, Leaflet
```

---

## Example 404

**Intent:**
adopt a street tree program, residents adopt and log watering in summer

**Spec:**
```
Type:       Web application (street tree adoption)
Auth:       Email + password login
Data model: Resident(id, name, email)
            StreetTree(id, species, planted_year, lat, lng, adopter_id -> Resident)
            Watering(id, tree_id -> StreetTree, resident_id -> Resident, liters, watered_at)
Features:   - Adopt a tree from the city tree map
            - Log watering with liters
            - Show trees not watered in the last week during heatwaves
            - Send reminders based on rainfall data
API:        REST
            GET  /trees
            POST /trees/{id}/adopt
            POST /trees/{id}/waterings
Storage:    PostgreSQL with PostGIS
Tech stack: TypeScript, Next.js, MapLibre GL, Open-Meteo API
```

---

## Example 405

**Intent:**
nest box monitoring scheme, volunteers check boxes weekly and record eggs and chicks

**Spec:**
```
Type:       Web application (nest box monitoring)
Auth:       Email + password login
Data model: Monitor(id, name, email)
            NestBox(id, code, lat, lng, monitor_id -> Monitor)
            NestCheck(id, box_id -> NestBox, date, species, eggs, chicks, outcome)
Features:   - Assign nest boxes to monitors
            - Record weekly checks with eggs and chicks
            - Calculate fledging success per species
            - Remind monitors when a check is due
API:        REST
            POST /boxes/{id}/checks
            GET  /stats/success
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 406

**Intent:**
did you feel the earthquake reports

**Spec:**
```
Type:       Web application (felt earthquake reports)
Data model: Quake(id, source_id, magnitude, lat, lng, occurred_at)
            FeltReport(id, quake_id -> Quake, lat, lng, intensity, description, reported_at)
Features:   - Import recent earthquakes from the USGS feed
            - Ask "did you feel it?" with a simple intensity questionnaire
            - Map reports as intensity by postcode area
            - Show the report count per quake
API:        REST
            GET  /quakes/recent
            POST /quakes/{id}/reports
            GET  /quakes/{id}/intensity-map
Storage:    PostgreSQL with PostGIS
Tech stack: Python, FastAPI, USGS GeoJSON feed, Leaflet
```

---

## Example 407

**Intent:**
Low-cost air quality sensor network for our neighbourhood, people host sensors on balconies

**Spec:**
```
Type:       IoT system (community air quality network)
Auth:       Device token per sensor, email login for hosts
Data model: Sensor(id, host_id, lat, lng, token, model)
            AirReading(sensor_id -> Sensor, pm25, pm10, temp_c, humidity, recorded_at)
Features:   - Send PM2.5 and PM10 readings from each sensor every 2 minutes
            - Correct readings for humidity
            - Show a live map coloured by air quality index
            - Alert hosts when a sensor goes offline
            - Publish hourly averages as open data
Input:      Readings from SDS011 particle sensors
API:        REST
            POST /readings
            GET  /sensors/latest
            GET  /sensors/{id}/hourly
Storage:    InfluxDB, PostgreSQL
Tech stack: ESP8266 (Arduino C++), Python, FastAPI, Leaflet
```

---

## Example 408

**Intent:**
noise complaint map for people living near the new nightclub, to show the council

**Spec:**
```
Type:       Web application (noise log)
Auth:       Email login with magic link
Data model: Resident(id, email, street)
            NoiseEvent(id, resident_id -> Resident, started_at, ended_at, level, kind, recording_url)
Features:   - Log noise incidents with time, type and optional audio clip
            - Measure decibel level with the phone microphone
            - Show a heatmap of incidents by night of week and hour
            - Generate a PDF report for the council
API:        REST
            POST /events
            GET  /stats
            GET  /report.pdf
Storage:    PostgreSQL, S3 (recordings)
Tech stack: Python, Django, Web Audio API, WeasyPrint
```

---

## Example 409

**Intent:**
local election candidates questionnaire site, candidates answer, voters compare

**Spec:**
```
Type:       Web application (candidate questionnaire)
Auth:       Invite link login for candidates, admin login
Data model: Race(id, office, district)
            Candidate(id, race_id -> Race, name, party, photo_url)
            QuestionnaireQuestion(id, text, position)
            CandidateAnswer(candidate_id -> Candidate, question_id -> QuestionnaireQuestion, answer)
Features:   - Send candidates invite links to answer questions
            - Show answers side by side per race
            - Look up your races by address
            - Mark candidates who did not respond
API:        REST
            GET  /races?address={a}
            GET  /races/{id}/compare
            POST /candidates/{id}/answers
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Google Civic Information API
```

---

## Example 410

**Intent:**
searchable archive of our town council meeting minutes and agendas from pdfs

**Spec:**
```
Type:       Web application (council minutes search)
Data model: Meeting(id, body, date, agenda_pdf_url, minutes_pdf_url)
            Page(id, meeting_id -> Meeting, page_number, text)
            Alert(id, email, keyword)
Features:   - Scrape new agendas and minutes from the council website
            - Extract text from PDFs, with OCR for scans
            - Search all pages with highlighted matches
            - Email alerts when a keyword appears in a new agenda
API:        REST
            GET  /search?q={text}
            GET  /meetings/{id}
            POST /alerts
Storage:    PostgreSQL (full-text search), S3 (PDFs)
Tech stack: Python, FastAPI, pdfplumber, Tesseract
```

---

## Example 411

**Intent:**
freedom of information requests tracker for journalists collective

**Spec:**
```
Type:       Web application (FOI request tracker)
Auth:       Email + password login
Data model: Journalist(id, name, email)
            Authority(id, name, email, avg_response_days)
            FoiRequest(id, journalist_id -> Journalist, authority_id -> Authority, subject, sent_on, due_on, status)
            Correspondence(id, request_id -> FoiRequest, direction, body, file_url, at)
Features:   - Log requests with authority and send date
            - Calculate legal due dates excluding holidays
            - Warn when responses are overdue
            - Attach replies and released documents
            - Show response time statistics per authority
API:        REST
            POST /requests
            POST /requests/{id}/correspondence
            GET  /authorities/{id}/stats
Storage:    PostgreSQL, S3 (documents)
Tech stack: Python, Django
```

---

## Example 412

**Intent:**
neighbors comment on planning applications in our area, get alerts when new ones filed

**Spec:**
```
Type:       Web application (planning application alerts)
Auth:       Email + password login
Data model: Application(id, reference, address, lat, lng, description, filed_on, deadline)
            Watcher(id, email, lat, lng, radius_m)
            Comment(id, application_id -> Application, user_id, body, stance)
Features:   - Import new planning applications from the council feed daily
            - Email watchers about applications within their radius
            - Show applications on a map with comment deadlines
            - Discuss applications with neighbours
API:        REST
            GET  /applications?near={lat,lng}
            POST /watchers
            POST /applications/{id}/comments
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django, Celery
```

---

## Example 413

**Intent:**
crowd audit bus stops for wheelchair accessibility

**Spec:**
```
Type:       Mobile application with backend (accessibility audit)
Auth:       Email login for auditors
Data model: BusStop(id, code, name, lat, lng)
            Audit(id, stop_id -> BusStop, auditor_id, has_curb_ramp, has_shelter, has_seat, surface, photo_url, audited_at)
Features:   - Find nearby stops from the transit GTFS data
            - Fill an accessibility checklist with photos
            - Show stops colour-coded by accessibility score
            - Export audits as CSV for the transit agency
API:        REST
            GET  /stops?near={lat,lng}
            POST /stops/{id}/audits
            GET  /export.csv
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, Node.js, GTFS
```

---

## Example 414

**Intent:**
sign language interpreter booking for deaf people, interpreters accept requests

**Spec:**
```
Type:       Web application (interpreter booking)
Auth:       Email + password login, roles: client, interpreter, coordinator
Data model: Interpreter(id, name, email, languages, certifications, region)
            BookingRequest(id, client_id, setting, address, starts_at, duration_min, remote, status)
            Assignment(request_id -> BookingRequest, interpreter_id -> Interpreter)
Features:   - Request an interpreter with setting, time and on-site or remote
            - Offer requests to qualified interpreters in the region
            - Let the first interpreter accept the job
            - Create a video link for remote sessions
            - Track hours for invoicing
API:        REST
            POST /requests
            GET  /requests/open
            POST /requests/{id}/accept
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Jitsi Meet, Vue.js
```

---

## Example 415

**Intent:**
volunteers caption local community videos, split into chunks

**Spec:**
```
Type:       Web application (crowdsourced captioning)
Auth:       Email + password login
Data model: Video(id, title, url, duration_s, status)
            Chunk(id, video_id -> Video, start_s, end_s, text, captioner_id, reviewed)
Features:   - Split videos into 30-second chunks
            - Pre-fill chunks with automatic speech recognition
            - Let volunteers correct a chunk while playing it
            - Review and merge chunks into a WebVTT file
API:        REST
            POST /videos
            GET  /chunks/next
            PATCH /chunks/{id}
            GET  /videos/{id}/captions.vtt
Storage:    PostgreSQL
Tech stack: Node.js, Express, Whisper API, React
```

---

## Example 416

**Intent:**
time zone meeting planner for distributed team

**Spec:**
```
Type:       Web application (time zone planner)
Data model: Team(id, name, share_token)
            Teammate(id, team_id -> Team, name, timezone, work_start, work_end)
Features:   - Add teammates with their time zone and working hours
            - Show a 24-hour grid of overlapping working hours
            - Suggest the best meeting slots for a selected group
            - Handle daylight saving changes for a chosen date
API:        REST
            POST /teams
            POST /teams/{id}/members
            GET  /teams/{id}/overlap?date={d}
Storage:    SQLite
Tech stack: TypeScript, SvelteKit, Luxon
```

---

## Example 417

**Intent:**
async video updates tool, record a short video update for your team instead of meeting

**Spec:**
```
Type:       Web application (async video updates)
Auth:       Google sign-in
Data model: Team(id, name)
            VideoUpdate(id, team_id -> Team, author_id, video_url, transcript, created_at)
            Reply(id, update_id -> VideoUpdate, author_id, text_or_video_url)
            View(update_id -> VideoUpdate, user_id, viewed_at)
Features:   - Record screen and camera in the browser
            - Transcribe updates automatically
            - Reply with text or a video
            - Show who has watched each update
            - Post new updates to Slack
API:        REST
            POST /updates
            POST /updates/{id}/replies
            POST /updates/{id}/views
Storage:    PostgreSQL, S3 (videos)
Tech stack: TypeScript, Next.js, MediaRecorder API, Whisper API
```

---

## Example 418

**Intent:**
interview scorecards so every interviewer rates candidates on the same criteria

**Spec:**
```
Type:       Web application (interview scorecards)
Auth:       Google sign-in
Data model: Role(id, title, criteria_json)
            Candidate(id, role_id -> Role, name, email, stage)
            Scorecard(id, candidate_id -> Candidate, interviewer_id, ratings_json, recommendation, notes, submitted_at)
Features:   - Define scoring criteria per role
            - Submit a scorecard after each interview
            - Hide other scorecards until yours is submitted
            - Show a summary across interviewers for the debrief
API:        REST
            POST /roles
            POST /candidates/{id}/scorecards
            GET  /candidates/{id}/summary
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 419

**Intent:**
visitor sign in at reception on ipad, host gets a message

**Spec:**
```
Type:       Web application (visitor sign-in)
Auth:       Email + password login for office admins
Data model: Host(id, name, email, slack_id)
            Visit(id, visitor_name, company, host_id -> Host, signed_in_at, signed_out_at, nda_signed)
Features:   - Sign in on a tablet kiosk with name, company and host
            - Sign an NDA on screen if required
            - Notify the host by Slack or email
            - Print a visitor badge
            - Show who is in the building for fire safety
API:        REST
            POST /visits
            POST /visits/{id}/signout
            GET  /visits/onsite
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Slack API
```

---

## Example 420

**Intent:**
parcel room for our apartment building, concierge logs packages and residents get notified

**Spec:**
```
Type:       Web application (package room)
Auth:       Email + password login for residents and concierge
Data model: Resident(id, name, email, phone, unit)
            Package(id, resident_id -> Resident, carrier, tracking, shelf, received_at, picked_up_at)
Features:   - Log a package by scanning the label with a phone camera
            - Notify the resident by SMS and email
            - Record pickup with a signature
            - Remind residents of packages waiting over 5 days
API:        REST
            POST /packages
            POST /packages/{id}/pickup
            GET  /packages?waiting=true
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio API
```

---

## Example 421

**Intent:**
office parking spots sharing, if you are not coming in someone else can use your spot

**Spec:**
```
Type:       Web application (parking spot sharing)
Auth:       Microsoft Entra ID single sign-on
Data model: Employee(id, name, email, assigned_spot_id)
            Spot(id, label, ev_charger)
            Release(id, spot_id -> Spot, date, claimed_by -> Employee)
Features:   - Release your assigned spot for days you are away
            - Claim a released spot for a day
            - Join a waitlist for the day
            - Show today's spot assignments to reception
API:        REST
            POST /releases
            POST /releases/{id}/claim
            GET  /today
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, React
```

---

## Example 422

**Intent:**
EV charger queue at work, you get a slack ping when its your turn

**Spec:**
```
Type:       Bot (Slack)
Data model: Charger(id, name, status, current_user, started_at)
            QueueEntry(id, user_id, joined_at)
Features:   - Join the queue with /charge
            - Ping the next person when a charger is freed
            - Give them 15 minutes to plug in before moving on
            - Remind users to move their car after 3 hours
Storage:    Redis
Tech stack: Python, Slack Bolt
```

---

## Example 423

**Intent:**
meeting room display tablet showing free/busy from outlook

**Spec:**
```
Type:       Web application (meeting room display)
Auth:       Device code per tablet
Data model: RoomDisplay(id, room_email, device_code)
Features:   - Show the current meeting and the next three bookings
            - Show green when free and red when busy
            - Book the room for 15 or 30 minutes from the tablet
            - End a meeting early to free the room
API:        REST
            GET  /displays/{code}/schedule
            POST /displays/{code}/book
            POST /displays/{code}/end
Tech stack: Node.js, Microsoft Graph API, React
```

---

## Example 424

**Intent:**
discourse plugin that gives badges for helping in our support category

**Spec:**
```
Type:       Plugin (Discourse)
Data model: Uses Discourse posts, solutions and user badges
Features:   - Count accepted solutions per user in the support category
            - Grant bronze, silver and gold badges at 5, 25 and 100 solutions
            - Show a monthly top helpers list on the category page
            - Add a site setting for the category and thresholds
Storage:    Discourse PostgreSQL database
Tech stack: Ruby, Discourse Plugin API, Ember.js
```

---

## Example 425

**Intent:**
chrome extension that shows if a github repo is looking for sponsors and how much they've raised

**Spec:**
```
Type:       Browser extension (sponsorship badge)
Features:   - Detect GitHub repository pages
            - Look up the owner's sponsors profile and open funding links
            - Show a small badge with goals and progress
            - Cache lookups for an hour
API:        REST
            GET  https://api.github.com/graphql (sponsorship data)
Storage:    chrome.storage.local (cache)
Tech stack: TypeScript, Chrome Extensions Manifest V3, GitHub GraphQL API
```

---

## Example 426

**Intent:**
command line tool that exports our forum's users and posts into a CSV for analysis

**Spec:**
```
Type:       Command-line tool (forum data export)
Features:   - Page through the forum API for users and posts
            - Write users.csv and posts.csv with chosen fields
            - Resume from the last page if interrupted
            - Anonymise usernames with a hash option
Input:      Forum base URL, API key, output directory, --anonymise flag
Tech stack: Python, requests, Click
```

---

## Example 427

**Intent:**
braille transcription volunteer network, schools request books, volunteers transcribe chapters

**Spec:**
```
Type:       Web application (braille transcription volunteers)
Auth:       Email + password login, roles: school, transcriber, proofreader
Data model: BookRequest(id, school_id, title, isbn, due_date, status)
            Chapter(id, request_id -> BookRequest, number, source_file_url, brf_file_url, transcriber_id, proofread)
Features:   - Let schools request a book with a due date
            - Split books into chapters for volunteers to claim
            - Upload BRF braille files per chapter
            - Assign proofreaders and merge approved chapters
API:        REST
            POST /requests
            POST /chapters/{id}/claim
            POST /chapters/{id}/upload
Storage:    PostgreSQL, S3 (files)
Tech stack: Ruby on Rails, liblouis
```

---

## Example 428

**Intent:**
bonsai club members track their trees progress with yearly photos and styling notes

**Spec:**
```
Type:       Web application (bonsai progression journal)
Auth:       Email + password login
Data model: Member(id, name, email)
            Bonsai(id, member_id -> Member, species, style, acquired_year, source)
            JournalEntry(id, bonsai_id -> Bonsai, date, work_done, photo_url)
Features:   - Add trees with species and style
            - Log work like pruning, wiring and repotting with photos
            - Show a photo timeline for each tree
            - Remind about seasonal work per species
API:        REST
            POST /bonsai
            POST /bonsai/{id}/entries
            GET  /bonsai/{id}/timeline
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django
```

---

## Example 429

**Intent:**
brass band contest results and adjudicator remarks archive

**Spec:**
```
Type:       Web application (band contest archive)
Auth:       Email + password login for editors
Data model: Band(id, name, region)
            Contest(id, name, date, section, test_piece)
            ContestResult(id, contest_id -> Contest, band_id -> Band, position, points, conductor, remarks_pdf_url)
Features:   - Enter contest results with points and conductor
            - Attach adjudicator remarks
            - Show a band's full contest history
            - Show rankings over the years per section
API:        REST
            POST /contests/{id}/results
            GET  /bands/{id}/history
Storage:    PostgreSQL, S3 (PDFs)
Tech stack: PHP, Laravel
```

---

## Example 430

**Intent:**
cider pressing day: people book a time slot to bring apples and press them

**Spec:**
```
Type:       Web application (apple pressing bookings)
Data model: PressDay(id, date, location, press_count)
            PressSlot(id, day_id -> PressDay, starts_at, booked_by_name, email, apples_kg)
Features:   - Generate 30-minute slots for each press
            - Book a slot with estimated apple weight
            - Remind people to bring containers
            - Show the day's schedule to volunteers
API:        REST
            GET  /days/{id}/slots
            POST /slots/{id}/book
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 431

**Intent:**
meteor shower counting app for citizen science

**Spec:**
```
Type:       Mobile application with backend (meteor counts)
Auth:       Optional account, anonymous observers allowed
Data model: CountSession(id, observer_id, lat, lng, limiting_magnitude, cloud_pct, started_at, ended_at)
            MeteorLog(id, session_id -> CountSession, shower, magnitude, seen_at)
Features:   - Start a session with sky conditions
            - Tap to log each meteor with a big dark-mode button
            - Assign meteors to the active shower or sporadic
            - Upload sessions to calculate zenithal hourly rates
API:        REST
            POST /sessions
            POST /sessions/{id}/meteors
            GET  /showers/{name}/zhr
Storage:    PostgreSQL
Tech stack: Kotlin Multiplatform, Python, FastAPI
```

---

## Example 432

**Intent:**
hedgehog sightings and garden highway holes map

**Spec:**
```
Type:       Web application (hedgehog sightings)
Data model: Sighting(id, lat, lng, seen_at, alive, count, photo_url)
            Highway(id, lat, lng, created_on, photo_url)
Features:   - Report hedgehog sightings on a map
            - Mark garden fence holes that link gardens
            - Show sightings by season
            - Show hotspots to guide where to add new holes
API:        REST
            POST /sightings
            POST /highways
            GET  /map
Storage:    PostgreSQL with PostGIS
Tech stack: Node.js, Express, Leaflet
```

---

## Example 433

**Intent:**
Write spec: reference check SaaS that emails referees a structured questionnaire and summarizes answers

**Spec:**
```
Type:       Web application (reference check SaaS)
Auth:       Email + password login for recruiters, tokenized links for referees
Data model: Candidate(id, recruiter_id, name, role)
            Referee(id, candidate_id -> Candidate, name, email, relationship, token)
            RefereeAnswer(referee_id -> Referee, question_key, value)
Features:   - Let candidates enter their referees
            - Email referees a questionnaire with rating and text questions
            - Remind referees who have not answered
            - Summarise ratings across referees with a chart
            - Detect referees sharing the candidate's IP address
API:        REST
            POST /candidates/{id}/referees
            GET  /ref/{token}
            POST /ref/{token}
            GET  /candidates/{id}/report
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Postmark API
```

---

## Example 434

**Intent:**
employee directory with org chart from our HR csv

**Spec:**
```
Type:       Web application (employee directory)
Auth:       Google Workspace SSO
Data model: Employee(id, name, email, title, department, manager_id -> Employee, location, photo_url, skills)
Features:   - Import employees from a nightly HR CSV
            - Search people by name, team or skill
            - Show an interactive org chart from manager links
            - Let employees edit their own skills and photo
API:        REST
            GET  /employees?q={text}
            GET  /orgchart
            PATCH /employees/me
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, D3.js
```

---

## Example 435

**Intent:**
key handover log for property managers, who has which keys

**Spec:**
```
Type:       Web application (key tracking)
Auth:       Email + password login
Data model: Property(id, address)
            KeySet(id, property_id -> Property, label, tag_code)
            KeyHandover(id, key_set_id -> KeySet, holder_name, holder_phone, out_at, due_at, returned_at, signature_url)
Features:   - Register key sets with a QR tag
            - Check keys out to contractors with a signature
            - Show who holds each key set
            - Alert on overdue keys
API:        REST
            POST /keysets
            POST /keysets/{id}/handovers
            PATCH /handovers/{id}/return
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 436

**Intent:**
cycling club bike rack booking at the office, 20 spots

**Spec:**
```
Type:       Web application (bike rack booking)
Auth:       Company email login with magic link
Data model: Rider(id, email)
            RackBooking(id, rider_id -> Rider, date, spot_number)
Features:   - Book one of 20 rack spots for a day
            - Show a week view of free spots
            - Cancel bookings
            - Release no-show spots at 10:00
API:        REST
            GET  /spots?date={d}
            POST /bookings
            DELETE /bookings/{id}
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 437

**Intent:**
audio description volunteers write descriptions of scenes for local theatre videos for blind audience

**Spec:**
```
Type:       Web application (audio description authoring)
Auth:       Email + password login
Data model: Production(id, title, video_url)
            Description(id, production_id -> Production, start_s, text, author_id, approved)
            Voicing(id, description_id -> Description, audio_url)
Features:   - Play the video and add descriptions at pauses in dialogue
            - Detect quiet gaps to suggest where descriptions fit
            - Record or synthesise voiced descriptions
            - Export a described audio track or WebVTT description track
API:        REST
            POST /productions/{id}/descriptions
            POST /descriptions/{id}/voicing
            GET  /productions/{id}/descriptions.vtt
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, Django, FFmpeg, pydub
```

---

## Example 438

**Intent:**
wheelchair users review accessibility of cafes and shops

**Spec:**
```
Type:       Web application (accessibility reviews)
Auth:       Email + password login
Data model: Place(id, name, address, lat, lng, osm_id)
            AccessReview(id, place_id -> Place, user_id, step_free, accessible_toilet, door_width_ok, notes, photo_url)
Features:   - Search places from OpenStreetMap
            - Review step-free entry, toilets and door width
            - Show a combined accessibility rating on a map
            - Sync wheelchair tags back to OpenStreetMap
API:        REST
            GET  /places?near={lat,lng}
            POST /places/{id}/reviews
Storage:    PostgreSQL with PostGIS
Tech stack: Node.js, Express, Overpass API, Leaflet
```

---

## Example 439

**Intent:**
drone pilots club flight log and safe flying spots

**Spec:**
```
Type:       Web application (drone club)
Auth:       Email + password login
Data model: Pilot(id, name, email, operator_id, license_level)
            FlyingSpot(id, name, lat, lng, restrictions, approved)
            Flight(id, pilot_id -> Pilot, spot_id -> FlyingSpot, drone_model, duration_min, flown_at)
Features:   - Log flights with drone, spot and duration
            - Suggest spots and let admins approve them
            - Show no-fly zones near each spot
            - Total flight hours per pilot
API:        REST
            POST /flights
            GET  /spots
            POST /spots
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django, Leaflet
```

---

## Example 440

**Intent:**
calligraphy practice community where people post daily practice sheets and get critique

**Spec:**
```
Type:       Web application (calligraphy practice)
Auth:       Email + password login
Data model: Artist(id, username, email)
            Sheet(id, artist_id -> Artist, script, tool, image_url, posted_on)
            Critique(id, sheet_id -> Sheet, author_id -> Artist, body, x_pct, y_pct)
Features:   - Upload a daily practice sheet with script and tool
            - Pin critiques to a spot on the image
            - Track a practice streak
            - Browse by script (italic, copperplate, blackletter)
API:        REST
            POST /sheets
            POST /sheets/{id}/critiques
            GET  /sheets?script={s}
Storage:    PostgreSQL, S3 (images)
Tech stack: Node.js, Express, React
```

---

## Example 441

**Intent:**
table tennis ladder at work, challenge people above you

**Spec:**
```
Type:       Web application (challenge ladder)
Auth:       Slack sign-in
Data model: Player(id, name, slack_id, position)
            Challenge(id, challenger_id -> Player, defender_id -> Player, status, created_at)
            MatchResult(id, challenge_id -> Challenge, winner_id -> Player, score)
Features:   - Challenge players up to three positions above you
            - Require the match within 7 days or the defender forfeits
            - Swap positions when the challenger wins
            - Post results to a Slack channel
API:        REST
            GET  /ladder
            POST /challenges
            POST /challenges/{id}/result
Storage:    SQLite
Tech stack: Node.js, Express, Slack API
```

---

## Example 442

**Intent:**
cricket club scoring ball by ball on a tablet, live scorecard online

**Spec:**
```
Type:       Web application (cricket scoring)
Auth:       Email + password login for scorers
Data model: CricketMatch(id, home, away, overs, toss_winner)
            Innings(id, match_id -> CricketMatch, batting_team, number)
            Ball(id, innings_id -> Innings, over, ball, batter, bowler, runs, extras, wicket_kind)
Features:   - Record each ball with runs, extras and wickets
            - Calculate batting and bowling figures
            - Show a live scorecard and run rate online
            - Undo the last ball
            - Export the scorecard as PDF
API:        REST + WebSocket
            POST /innings/{id}/balls
            DELETE /innings/{id}/balls/last
            WS   /matches/{id}/live
Storage:    PostgreSQL
Tech stack: TypeScript, React, Node.js, Socket.IO
```

---

## Example 443

**Intent:**
bowling league standings w handicap

**Spec:**
```
Type:       Web application (bowling league)
Auth:       Email + password login for the league secretary
Data model: Bowler(id, name, team_id, average)
            Team(id, name)
            Week(id, number, date)
            GameScore(id, week_id -> Week, bowler_id -> Bowler, game_number, pins)
Features:   - Enter three games per bowler each week
            - Recalculate averages and handicaps (90% of 220 minus average)
            - Award team points per game and series
            - Show standings and individual high scores
API:        REST
            POST /weeks/{id}/scores
            GET  /standings
            GET  /bowlers/{id}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 444

**Intent:**
ultimate frisbee tournament with spirit of the game scores

**Spec:**
```
Type:       Web application (ultimate tournament)
Auth:       Email + password login for team captains
Data model: Team(id, name, captain_email)
            Game(id, team_a_id -> Team, team_b_id -> Team, field, starts_at, score_a, score_b)
            SpiritScore(id, game_id -> Game, from_team_id -> Team, about_team_id -> Team, rules, fouls, fairness, attitude, communication)
Features:   - Generate pool play schedules with fields
            - Let captains submit scores and spirit scores
            - Show pool standings and bracket placement
            - Show a spirit ranking for the spirit award
API:        REST
            POST /games/{id}/score
            POST /games/{id}/spirit
            GET  /standings
            GET  /spirit
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 445

**Intent:**
time bank for our town, everyone's hour is equal, earn by helping spend by asking

**Spec:**
```
Type:       Web application (community time bank)
Auth:       Email + password login, coordinator approval
Data model: Member(id, name, email, skills, hours_balance, approved)
            Offer(id, member_id -> Member, skill, description)
            Exchange(id, giver_id -> Member, receiver_id -> Member, hours, description, confirmed)
Features:   - List skills you can offer
            - Search offers by skill
            - Record an exchange and have the receiver confirm the hours
            - Update both members' balances
            - Start new members with 2 free hours
API:        REST
            GET  /offers?skill={s}
            POST /exchanges
            POST /exchanges/{id}/confirm
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 446

**Intent:**
befriending service matching volunteers to lonely older people for weekly calls

**Spec:**
```
Type:       Web application (befriending service)
Auth:       Email + password login for volunteers and coordinators
Data model: Volunteer(id, name, email, interests, languages, dbs_checked)
            Befriendee(id, name, phone, interests, languages, preferred_time)
            Friendship(id, volunteer_id -> Volunteer, befriendee_id -> Befriendee, started_on, active)
            CallLog(id, friendship_id -> Friendship, date, duration_min, wellbeing, concerns)
Features:   - Suggest matches by interests, language and call time
            - Log each call with a wellbeing rating
            - Flag concerns to the coordinator immediately
            - Alert when no call has happened for two weeks
API:        REST
            GET  /matches/suggestions
            POST /friendships
            POST /friendships/{id}/calls
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 447

**Intent:**
families host refugees in spare rooms, need matching and safeguarding checks tracked

**Spec:**
```
Type:       Web application (refugee hosting matching)
Auth:       Email + password login, roles: host, caseworker
Data model: Host(id, name, email, address, rooms, languages, checks_passed)
            Guest(id, caseworker_id, household_size, languages, needs)
            Placement(id, host_id -> Host, guest_id -> Guest, starts_on, ends_on, status)
            Check(id, host_id -> Host, kind, result, checked_on)
Features:   - Register host households with room details
            - Track background and home checks per host
            - Match guests to hosts by size, language and needs
            - Record check-ins during the placement
API:        REST
            POST /hosts
            POST /hosts/{id}/checks
            POST /placements
Storage:    PostgreSQL (encrypted personal data)
Tech stack: Python, Django
```

---

## Example 448

**Intent:**
prom dress and suit lending library for students who cant afford

**Spec:**
```
Type:       Web application (formalwear lending)
Auth:       Email login with school verification
Data model: Garment(id, kind, size, color, photo_url, status)
            FittingAppointment(id, student_email, starts_at)
            GarmentLoan(id, garment_id -> Garment, student_email, event_date, returned)
Features:   - Browse garments by kind, size and colour
            - Book a private fitting appointment
            - Reserve a garment for an event date
            - Track returns and cleaning
API:        REST
            GET  /garments?size={s}
            POST /fittings
            POST /garments/{id}/loans
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Next.js
```

---

## Example 449

**Intent:**
toy library for families, borrow toys for 3 weeks, like a book library

**Spec:**
```
Type:       Web application (toy library)
Auth:       Email + password login, membership fee
Data model: Family(id, name, email, membership_until)
            Toy(id, name, age_range, pieces_count, photo_url, status)
            ToyLoan(id, toy_id -> Toy, family_id -> Family, out_on, due_on, returned_on, pieces_ok)
Features:   - Browse toys by age range
            - Reserve up to 4 toys at once
            - Check toys out for 3 weeks
            - Count pieces on return and flag missing parts
API:        REST
            GET  /toys?age={a}
            POST /toys/{id}/reserve
            POST /loans
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 450

**Intent:**
board game cafe table booking with game reservation

**Spec:**
```
Type:       Web application (board game cafe booking)
Auth:       Email + password login
Data model: CafeTable(id, seats)
            Game(id, title, min_players, max_players, copies)
            TableBooking(id, table_id -> CafeTable, name, party_size, starts_at, ends_at, game_id -> Game)
Features:   - Book a table for a party size and time
            - Reserve a game with the table if copies are free
            - Charge a table fee per person
            - Show staff the evening's bookings
API:        REST
            GET  /availability?date={d}&party={n}
            POST /bookings
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Stripe API
```

---

## Example 451

**Intent:**
LAN party seat booking with seat map and tournaments

**Spec:**
```
Type:       Web application (LAN party)
Auth:       Email + password login, Steam linking
Data model: Attendee(id, nickname, email, steam_id)
            Seat(id, row, number, attendee_id -> Attendee)
            Tournament(id, game, format)
            TournamentEntry(tournament_id -> Tournament, attendee_id -> Attendee)
Features:   - Buy a ticket and pick a seat on a map
            - Sit next to friends by swapping seats
            - Sign up for in-event tournaments
            - Show a schedule and announcements during the event
API:        REST
            GET  /seats
            POST /seats/{id}/claim
            POST /tournaments/{id}/entries
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Stripe API
```

---

## Example 452

**Intent:**
game jam site: theme voting before, submissions, then rating by participants

**Spec:**
```
Type:       Web application (game jam)
Auth:       Email + password login
Data model: Jam(id, title, starts_at, ends_at, rating_ends_at)
            Theme(id, jam_id -> Jam, text, votes)
            GameEntry(id, jam_id -> Jam, team, title, play_url, download_url)
            EntryRating(entry_id -> GameEntry, rater_id, fun, art, audio, theme_fit)
Features:   - Vote on theme ideas before the jam
            - Reveal the winning theme at the start
            - Submit a game with web build or download
            - Rate other entries in several categories
            - Boost visibility of entries with few ratings
API:        REST
            POST /jams/{id}/themes
            POST /jams/{id}/entries
            POST /entries/{id}/ratings
            GET  /jams/{id}/results
Storage:    PostgreSQL, S3 (builds)
Tech stack: Python, Django
```

---

## Example 453

**Intent:**
mod hosting site for my indie games community, with versions and dependency info

**Spec:**
```
Type:       Web application (game mod hosting)
Auth:       Email + password login
Data model: Modder(id, username, email)
            Mod(id, author_id -> Modder, name, description, downloads)
            ModVersion(id, mod_id -> Mod, version, game_version, file_url, changelog)
            Dependency(version_id -> ModVersion, depends_on_mod_id -> Mod, min_version)
Features:   - Upload mod versions with changelogs
            - Declare dependencies on other mods
            - Scan uploads for malware
            - Show compatible versions per game version
            - Provide an API for mod managers
API:        REST
            GET  /api/mods
            GET  /api/mods/{id}/versions
            POST /mods/{id}/versions
Storage:    PostgreSQL, S3 (files)
Tech stack: Go, ClamAV, React
```

---

## Example 454

**Intent:**
minecraft server whitelist application form, mods review then bot adds them

**Spec:**
```
Type:       Web application (server whitelist applications)
Auth:       Discord OAuth login
Data model: WhitelistApplication(id, discord_id, minecraft_username, minecraft_uuid, age, why_join, status, reviewed_by)
Features:   - Apply with Minecraft username and short answers
            - Verify the username through the Mojang API
            - Let moderators approve or deny
            - Add approved players to the whitelist via RCON
            - Give a Discord role on approval
API:        REST
            POST /applications
            PATCH /applications/{id}
Storage:    SQLite
Tech stack: Python, FastAPI, mcrcon, discord.py
```

---

## Example 455

**Intent:**
giveaway picker saas: pull youtube comments and pick random winner fairly

**Spec:**
```
Type:       Web application (giveaway picker)
Auth:       Google sign-in
Data model: Giveaway(id, owner_id, video_id, keyword, created_at)
            Winner(id, giveaway_id -> Giveaway, author_channel, comment_text, picked_at)
Features:   - Fetch all comments for a YouTube video
            - Filter by keyword and remove duplicate commenters
            - Pick winners randomly with a shown seed
            - Share a public result page as proof
API:        REST
            POST /giveaways
            POST /giveaways/{id}/draw
            GET  /g/{id}
Storage:    PostgreSQL
Tech stack: Node.js, YouTube Data API, React
```

---

## Example 456

**Intent:**
affiliate tracking for my small SaaS, partners get links and commission on sign ups

**Spec:**
```
Type:       Web application (affiliate program)
Auth:       Email + password login for affiliates and admin
Data model: Affiliate(id, name, email, code, commission_pct, payout_email)
            AffiliateClick(id, affiliate_id -> Affiliate, landed_at, cookie_id)
            Conversion(id, affiliate_id -> Affiliate, customer_id, amount, commission, status)
Features:   - Give affiliates a tracked link with a 60-day cookie
            - Attribute paid signups through the billing webhook
            - Calculate commissions and hold them for 30 days
            - Pay out monthly and show affiliates their earnings
API:        REST
            GET  /r/{code}
            POST /webhooks/billing
            GET  /affiliates/me/stats
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe API
```

---

## Example 457

**Intent:**
cancel flow survey saas: when user cancels subscription, ask why and offer discount

**Spec:**
```
Type:       Web application (cancellation flow SaaS)
Auth:       Email + password login, publishable key
Data model: Account(id, company, stripe_account_id)
            FlowConfig(id, account_id -> Account, reasons_json, offer_pct, offer_months)
            CancelSession(id, account_id -> Account, customer_id, reason, feedback, accepted_offer, cancelled)
Features:   - Show an embedded modal when a user clicks cancel
            - Ask for a reason and optional feedback
            - Offer a discount or pause based on the reason
            - Apply the coupon or cancel through Stripe
            - Report saved revenue and top reasons
API:        REST
            POST /sessions
            POST /sessions/{id}/complete
            GET  /reports
Storage:    PostgreSQL
Tech stack: TypeScript, Preact, Node.js, Stripe API
```

---

## Example 458

**Intent:**
usage-based billing meter API: SaaS sends usage events, we aggregate and bill monthly

**Spec:**
```
Type:       REST API service (usage metering)
Auth:       API key per vendor
Data model: Meter(id, vendor_id, name, aggregation)
            UsageEvent(id, meter_id -> Meter, customer_id, value, idempotency_key, ts)
            Invoice(id, vendor_id, customer_id, period, amount, status)
Features:   - Ingest usage events with idempotency keys
            - Aggregate by sum, count or max per billing period
            - Price usage with tiered rates
            - Create invoices at period end
            - Show customers current usage
API:        REST
            POST /v1/events
            GET  /v1/customers/{id}/usage
            POST /v1/meters
Storage:    PostgreSQL, ClickHouse (events)
Tech stack: Go, Stripe Invoicing API
```

---

## Example 459

**Intent:**
customer health score dashboard for our customer success team from product usage and tickets

**Spec:**
```
Type:       Data dashboard (customer health)
Features:   - Load logins, feature usage, ticket counts and NPS per account nightly
            - Calculate a weighted health score from 0 to 100
            - Show accounts sorted by score with trend arrows
            - Highlight accounts whose score dropped over 20 points
            - Filter by account manager and plan
Input:      Product events table, helpdesk export, NPS export
Storage:    PostgreSQL
Tech stack: Python, dbt, Metabase
```

---

## Example 460

**Intent:**
dunning emails service that retries failed card payments and emails customers nicely

**Spec:**
```
Type:       Webhook service (payment recovery)
Data model: FailedPayment(id, invoice_id, customer_email, amount, attempts, next_retry_at, recovered)
            EmailSent(id, failed_payment_id -> FailedPayment, template, sent_at)
Features:   - Receive invoice.payment_failed webhooks
            - Retry charges on a smart schedule (1, 3, 5 and 7 days)
            - Send a sequence of friendly emails with an update-card link
            - Mark payments recovered and stop emails
            - Report monthly recovered revenue
API:        REST
            POST /webhooks/stripe
            GET  /stats
Storage:    PostgreSQL
Tech stack: Ruby, Sinatra, Sidekiq, Stripe API
```

---

## Example 461

**Intent:**
cheer squad routine builder? no.. gymnastics club meet scoring with judges panels

**Spec:**
```
Type:       Web application (gymnastics meet scoring)
Auth:       PIN login per judge panel
Data model: Gymnast(id, name, club, level)
            Apparatus(id, name)
            Routine(id, gymnast_id -> Gymnast, apparatus_id -> Apparatus, d_score, final_score)
            ExecutionScore(routine_id -> Routine, judge_number, deduction)
Features:   - Enter difficulty and execution scores per panel
            - Drop highest and lowest execution scores and average the rest
            - Rank all-around and per apparatus by level
            - Show live results on a scoreboard
API:        REST + WebSocket
            POST /routines/{id}/scores
            GET  /results?level={l}
            WS   /meet/live
Storage:    PostgreSQL
Tech stack: Node.js, Socket.IO, React
```

---

## Example 462

**Intent:**
gym buddy finder at my university gym by schedule and goals

**Spec:**
```
Type:       Web application (workout partner matching)
Auth:       University SSO
Data model: Student(id, name, email, goals, experience, schedule_json)
            BuddyRequest(id, from_id -> Student, to_id -> Student, status)
Features:   - Set goals (strength, cardio, weight loss) and weekly gym times
            - Suggest buddies with overlapping times and goals
            - Send and accept buddy requests
            - Share contact details only after acceptance
API:        REST
            GET  /suggestions
            POST /buddy-requests
            PATCH /buddy-requests/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, Vue.js
```

---

## Example 463

**Intent:**
Hi, i am from Vietnam, I want make website where Vietnamese students in Australia share used furniture when they move house

**Spec:**
```
Type:       Web application (student furniture sharing)
Auth:       Email or Facebook login
Data model: Student(id, name, email, city, university)
            FurnitureItem(id, owner_id -> Student, title, category, price, photo_urls, pickup_suburb, available_until)
            ItemMessage(id, item_id -> FurnitureItem, sender_id -> Student, body)
Features:   - Post furniture with photos, price and pickup suburb
            - Filter by city, suburb and category
            - Message the owner in Vietnamese or English
            - Mark items as given away
API:        REST
            GET  /items?city={c}
            POST /items
            POST /items/{id}/messages
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Express, React (i18n)
```

---

## Example 464

**Intent:**
twitch clip of the month contest from our community

**Spec:**
```
Type:       Web application (clip contest)
Auth:       Twitch OAuth login
Data model: ClipEntry(id, clip_slug, submitted_by, month, title, thumbnail_url)
            ClipVote(entry_id -> ClipEntry, voter_twitch_id)
Features:   - Submit Twitch clips from the channel by URL
            - Verify the clip belongs to the channel with the Twitch API
            - Vote for one clip per month
            - Show the winner and past winners
API:        REST
            POST /entries
            POST /entries/{id}/vote
            GET  /months/{m}/winner
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Twitch API, Svelte
```

---

## Example 465

**Intent:**
uniform swap shop for our primary school

**Spec:**
```
Type:       Web application (school uniform swap)
Auth:       Parent email login
Data model: UniformItem(id, kind, size, condition, donor_email, status)
            UniformRequest(id, parent_email, kind, size, status)
Features:   - Donate uniform items by kind and size
            - Request items in your child's size
            - Match requests with donated stock automatically
            - Let volunteers mark items ready for collection
API:        REST
            POST /items
            POST /requests
            GET  /matches
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 466

**Intent:**
baby gear lending among parents (prams, cots, car seats) with safety expiry dates

**Spec:**
```
Type:       Web application (baby gear lending)
Auth:       Email + password login
Data model: Parent(id, name, email, area)
            BabyGear(id, owner_id -> Parent, kind, brand, manufactured_on, expires_on, photo_url)
            GearBorrow(id, gear_id -> BabyGear, borrower_id -> Parent, from_date, to_date, status)
Features:   - List gear with manufacture date
            - Block lending of car seats past their expiry date
            - Request to borrow for a date range
            - Show recall notices for listed models
API:        REST
            GET  /gear?kind={k}
            POST /gear
            POST /gear/{id}/borrow
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, React
```

---

## Example 467

**Intent:**
appointment booking for a free clothing bank, families pick a time to shop

**Spec:**
```
Type:       Web application (clothing bank appointments)
Auth:       Referral code from partner agencies
Data model: Referral(id, code, agency, family_size, used)
            ShopSlot(id, starts_at, capacity, booked)
            ShopVisit(id, referral_id -> Referral, slot_id -> ShopSlot, attended)
Features:   - Let families book a 30-minute shopping slot with a referral code
            - Allow one visit per referral
            - Send SMS reminders
            - Show volunteers the day's list
API:        REST
            GET  /slots
            POST /visits
            GET  /today
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio API
```

---

## Example 468

**Intent:**
discord server application form, answer questions to get member role

**Spec:**
```
Type:       Bot (Discord)
Data model: ServerApplication(id, user_id, answers_json, status, reviewer_id)
Features:   - Send new members a form in a modal when they join
            - Post answers to a private staff channel with approve and deny buttons
            - Give the member role on approval
            - DM the user the decision
Storage:    SQLite
Tech stack: TypeScript, discord.js
```

---

## Example 469

**Intent:**
web app for my art class to sell student prints at the end of term show, money goes to school

**Spec:**
```
Type:       Web application (student art sale)
Auth:       Email + password login for the teacher
Data model: Artwork(id, student_first_name, title, image_url, price, edition_size, sold_count)
            ArtOrder(id, artwork_id -> Artwork, buyer_email, quantity, paid, collected)
Features:   - List student prints with price and edition size
            - Sell online with card payments
            - Stop sales when an edition is sold out
            - Give the teacher a collection list for the show
API:        REST
            GET  /artworks
            POST /artworks/{id}/orders
            GET  /collection-list
Storage:    PostgreSQL, S3 (images)
Tech stack: Node.js, Next.js, Stripe API
```

---

## Example 470

**Intent:**
anonymous feedback for teachers at end of term from students

**Spec:**
```
Type:       Web application (course feedback)
Auth:       One-time access codes handed out in class
Data model: Course(id, teacher_id, name, term)
            AccessCode(id, course_id -> Course, code, used)
            FeedbackForm(id, course_id -> Course, answers_json, submitted_at)
Features:   - Generate one-time codes per class
            - Collect feedback without storing who answered
            - Show the teacher averages and comments after the term ends
            - Hide results for classes with fewer than 5 responses
API:        REST
            POST /courses/{id}/codes
            POST /feedback
            GET  /courses/{id}/results
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 471

**Intent:**
neighbourhood skill directory, find a plumber neighbour or someone who speaks french

**Spec:**
```
Type:       Web application (neighbour skills directory)
Auth:       Email + password login, address verification by postcard code
Data model: Neighbor(id, name, email, street, verified)
            NeighborSkill(neighbor_id -> Neighbor, skill, paid_or_free)
Features:   - List your skills and whether you help for free or paid
            - Search neighbours by skill
            - Verify addresses with a code sent by post
            - Contact neighbours through a form
API:        REST
            GET  /skills?q={text}
            POST /skills
            POST /neighbors/{id}/contact
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 472

**Intent:**
plz spec site where rock climbers find a partner for a day at the crag

**Spec:**
```
Type:       Mobile application with backend (climbing partner finder)
Auth:       Email or Google sign-in
Data model: Climber(id, name, grade_sport, grade_trad, belay_certified, region)
            Outing(id, creator_id -> Climber, crag, date, style, spots)
            OutingJoin(outing_id -> Outing, climber_id -> Climber, status)
Features:   - Post an outing with crag, date and style
            - Filter partners by grade and belay certification
            - Request to join and chat once accepted
            - Leave partner feedback after the day
API:        REST
            GET  /outings?region={r}
            POST /outings
            POST /outings/{id}/join
Storage:    PostgreSQL
Tech stack: Flutter, Firebase
```

---

## Example 473

**Intent:**
SaaS: event check-in app with QR badges for conference organizers

**Spec:**
```
Type:       Web application (event check-in SaaS)
Auth:       Email + password login for organisers, staff device codes
Data model: Event(id, organiser_id, name, date)
            Attendee(id, event_id -> Event, name, email, ticket_type, qr_code, checked_in_at)
            Session(id, event_id -> Event, title, room)
            SessionScan(session_id -> Session, attendee_id -> Attendee, scanned_at)
Features:   - Import attendees from CSV and email QR badges
            - Scan badges at the door with any phone camera
            - Work offline and sync scans later
            - Print name badges on check-in
            - Track session attendance
API:        REST
            POST /events/{id}/attendees/import
            POST /checkins
            POST /sessions/{id}/scans
Storage:    PostgreSQL
Tech stack: TypeScript, React (PWA), Node.js
```

---

## Example 474

**Intent:**
alumni magazine archive online, scanned issues searchable

**Spec:**
```
Type:       Web application (magazine archive)
Auth:       Alumni login for full access, public previews
Data model: Issue(id, year, season, cover_url, pdf_url)
            IssuePage(id, issue_id -> Issue, number, text, image_url)
Features:   - Upload scanned issues and split them into pages
            - Run OCR to make text searchable
            - Read issues in a page-flip viewer
            - Search for names across all issues
API:        REST
            GET  /issues
            GET  /search?q={name}
            POST /issues
Storage:    PostgreSQL, S3 (scans)
Tech stack: Python, Django, Tesseract, PDF.js
```

---

## Example 475

**Intent:**
open source project sponsorship fund that splits donations across dependencies we use

**Spec:**
```
Type:       Web application (dependency funding)
Auth:       GitHub OAuth login for companies
Data model: Company(id, name, monthly_budget)
            Dependency(id, package_name, ecosystem, maintainer_github, funding_url)
            CompanyDependency(company_id -> Company, dependency_id -> Dependency, weight)
            Payout(id, dependency_id -> Dependency, month, amount)
Features:   - Upload a lockfile to detect dependencies
            - Weight dependencies by usage
            - Split the monthly budget across maintainers
            - Pay out through GitHub Sponsors or Open Collective
API:        REST
            POST /lockfiles
            GET  /companies/{id}/allocation
            POST /payouts/run
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, GitHub GraphQL API
```

---

## Example 476

**Intent:**
cooperative grocery buying club, members order bulk and split cases

**Spec:**
```
Type:       Web application (bulk buying club)
Auth:       Email + password login
Data model: Member(id, name, email)
            Product(id, name, case_size, case_price, supplier)
            OrderCycle(id, closes_at, delivery_on)
            OrderLine(id, cycle_id -> OrderCycle, member_id -> Member, product_id -> Product, units)
Features:   - Open an order cycle with a closing date
            - Order units of products sold by the case
            - Show how many units are needed to fill each case
            - Drop unfilled cases and adjust orders
            - Calculate each member's bill
API:        REST
            GET  /cycles/current
            POST /cycles/{id}/lines
            GET  /cycles/{id}/cases
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView
```

---

## Example 477

**Intent:**
coding bootcamp alumni demo day site where employers browse student projects and request intros

**Spec:**
```
Type:       Web application (demo day showcase)
Auth:       Email + password login for students and employers
Data model: Graduate(id, name, email, github_url, skills)
            DemoProject(id, graduate_id -> Graduate, title, video_url, live_url)
            Employer(id, company, email)
            IntroRequest(id, employer_id -> Employer, graduate_id -> Graduate, message, status)
Features:   - Show graduate profiles with project videos
            - Filter by skills
            - Let employers request an intro
            - Notify graduates and staff of requests
API:        REST
            GET  /graduates?skill={s}
            POST /intro-requests
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 478

**Intent:**
wildflower meadow survey where volunteers do quadrat counts each june

**Spec:**
```
Type:       Web application (meadow quadrat survey)
Auth:       Email + password login
Data model: Meadow(id, name, lat, lng)
            Quadrat(id, meadow_id -> Meadow, survey_year, number, surveyor_id)
            PlantCount(id, quadrat_id -> Quadrat, species, cover_pct)
Features:   - Record species and percentage cover per quadrat
            - Calculate species richness per meadow per year
            - Compare years to see changes
            - Export data for the botanical society
API:        REST
            POST /quadrats
            POST /quadrats/{id}/counts
            GET  /meadows/{id}/richness
Storage:    PostgreSQL
Tech stack: Python, Flask, Chart.js
```

---

## Example 479

**Intent:**
idk just a simple site so my band's fans can join our mailing list and see tour dates

**Spec:**
```
Type:       Web application (band homepage)
Auth:       Admin password for the band
Data model: TourDate(id, date, city, venue, ticket_url)
            Fan(id, email, city, confirmed)
Features:   - Show upcoming tour dates with ticket links
            - Collect fan emails with their city
            - Email fans when a show is added near their city
            - Let fans unsubscribe with one click
API:        REST
            GET  /tour
            POST /fans
            POST /admin/tour-dates
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 480

**Intent:**
conference speaker travel reimbursement tracking for a nonprofit conf

**Spec:**
```
Type:       Web application (speaker reimbursements)
Auth:       Email + password login for speakers and organisers
Data model: Speaker(id, name, email, travel_budget)
            ExpenseClaim(id, speaker_id -> Speaker, category, amount, currency, receipt_url, status)
            Reimbursement(id, speaker_id -> Speaker, total, paid_on, method)
Features:   - Show each speaker their travel budget
            - Submit expense claims with receipts
            - Let organisers approve claims within budget
            - Convert currencies and record payouts
API:        REST
            POST /claims
            PATCH /claims/{id}
            POST /reimbursements
Storage:    PostgreSQL, S3 (receipts)
Tech stack: Python, Django
```

---

## Example 481

**Intent:**
a place for amateur astronomers to book time on our club's remote robotic telescope

**Spec:**
```
Type:       Web application (remote telescope scheduling)
Auth:       Email + password login
Data model: Member(id, name, email, credits)
            ObservationRequest(id, member_id -> Member, target, ra, dec, filter, exposure_s, frames, status)
            ObsImage(id, request_id -> ObservationRequest, fits_url, captured_at)
Features:   - Submit observation requests with target and exposures
            - Check the target is above the horizon tonight
            - Queue requests for the telescope control software
            - Deliver FITS images to the member when done
            - Charge credits per minute of exposure
API:        REST
            POST /requests
            GET  /queue/tonight
            POST /requests/{id}/images
Storage:    PostgreSQL, S3 (FITS files)
Tech stack: Python, Django, Astropy
```

---

## Example 482

**Intent:**
neighbourhood WhatsApp alternative for announcements only, admins post and everyone gets push

**Spec:**
```
Type:       Mobile application with backend (announcement channel)
Auth:       Phone number login with SMS code
Data model: Channel(id, name, invite_code)
            ChannelAdmin(channel_id -> Channel, user_id)
            Announcement(id, channel_id -> Channel, author_id, text, image_url, created_at)
            Subscriber(channel_id -> Channel, user_id, push_token)
Features:   - Join a channel with an invite code
            - Let only admins post announcements
            - Send push notifications to all subscribers
            - Show read counts to admins
API:        REST
            POST /channels/join
            POST /channels/{id}/announcements
            GET  /channels/{id}/announcements
Storage:    PostgreSQL
Tech stack: React Native, Expo Notifications, Node.js
```

---

